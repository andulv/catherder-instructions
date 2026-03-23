#!/usr/bin/env python3
import json
import hashlib
import re
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr
from pathlib import Path
from html import unescape

PLAN_ROOT = Path('.instructions/plans/plan011-svein-email-and-attachment-extraction')
SOURCE_ROOT = Path('reference/mailbox-anders-plantedamp')
OUTPUT_ROOT = PLAN_ROOT / 'output'
FRAGMENTS_DIR = OUTPUT_ROOT / 'fragments'
ATTACHMENTS_DIR = OUTPUT_ROOT / 'attachments'
MANIFESTS_DIR = OUTPUT_ROOT / 'manifests'
FRAGMENTS_MANIFEST = MANIFESTS_DIR / 'fragments.jsonl'
CANDIDATE_MANIFEST = MANIFESTS_DIR / 'candidate-documents.jsonl'

SVEIN_EMAIL = 'svein@byrknes.no'
SVEIN_NAME = 'svein skorpen'
ATTACH_EXTS = {'.pdf', '.doc', '.docx', '.xls', '.xlsx', '.xlsm', '.csv', '.ppt', '.pptx', '.txt', '.rtf', '.odt', '.ods'}
QUOTE_MARKER_RE = re.compile(r'(?im)^(fra|from|sent|sendt|to|til|subject|emne):\s+|^[- ]*forwarded message[- ]*$|^[- ]*opprinnelig melding[- ]*$|^>+')
STRONG_HISTORY_RE = re.compile(r'(?im)^(fra|from|sent|sendt|to|til|subject|emne):\s+|^[- ]*forwarded message[- ]*$|^[- ]*opprinnelig melding[- ]*$|^on .+wrote:\s*$|^>+')
MAIL_REF_RE = re.compile(r'(?i)\b(svein).{0,40}\b(skrev|sendte|vedlagt|utkast|fil|dokument|rapport|oversikt|regneark)\b|\b(vedlagt|utkast|rapport|oversikt|regneark).{0,40}\bSvein\b')
TAG_RE = re.compile(r'<[^>]+>')
WS_RE = re.compile(r'\s+')


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_filename(name: str) -> str:
    name = name.strip().replace('/', '_').replace('\\', '_')
    return name or 'attachment.bin'


def html_to_text(value: str) -> str:
    value = unescape(value)
    value = re.sub(r'(?is)<(script|style).*?>.*?</\1>', ' ', value)
    value = re.sub(r'(?i)<br\s*/?>', '\n', value)
    value = re.sub(r'(?i)</p\s*>', '\n\n', value)
    value = TAG_RE.sub(' ', value)
    value = value.replace('\r\n', '\n').replace('\r', '\n')
    lines = [WS_RE.sub(' ', line).strip() for line in value.split('\n')]
    return '\n'.join(line for line in lines if line).strip()


def plain_normalize(value: str) -> str:
    value = value.replace('\r\n', '\n').replace('\r', '\n')
    lines = [line.rstrip() for line in value.split('\n')]
    return '\n'.join(lines).strip()


def extract_body(msg):
    plain_parts = []
    html_parts = []
    for part in msg.walk():
        if part.is_multipart():
            continue
        dispo = (part.get_content_disposition() or '').lower()
        if dispo == 'attachment':
            continue
        ctype = part.get_content_type()
        try:
            content = part.get_content()
        except Exception:
            payload = part.get_payload(decode=True) or b''
            charset = part.get_content_charset() or 'utf-8'
            content = payload.decode(charset, errors='replace')
        if ctype == 'text/plain':
            plain_parts.append(str(content))
        elif ctype == 'text/html':
            html_parts.append(str(content))
    if plain_parts:
        return plain_normalize('\n\n'.join(plain_parts))
    if html_parts:
        return html_to_text('\n\n'.join(html_parts))
    return ''


def from_matches(value: str):
    name, email = parseaddr(value or '')
    low_name = (name or '').strip().lower()
    low_email = (email or '').strip().lower()
    evidence = []
    if low_email == SVEIN_EMAIL:
        evidence.extend(['FROM_EXACT', 'FROM_EMAIL_MATCH'])
    elif SVEIN_EMAIL in low_email:
        evidence.append('FROM_EMAIL_MATCH')
    if low_name == SVEIN_NAME or SVEIN_NAME in low_name:
        evidence.append('FROM_NAME_MATCH')
    return sorted(set(evidence))


def first_history_index(lines):
    for idx, line in enumerate(lines):
        if STRONG_HISTORY_RE.match(line.strip()) or STRONG_HISTORY_RE.match(line):
            return idx
    return None


def split_primary_and_context(text: str):
    lines = text.split('\n')
    idx = first_history_index(lines)
    if idx is None:
        primary = text.strip()
        context = ''
    else:
        primary = '\n'.join(lines[:idx]).strip()
        context = '\n'.join(lines[idx:]).strip()
    return primary, context


def split_blocks(text: str):
    text = text.strip()
    if not text:
        return []
    blocks = []
    current = []
    for line in text.split('\n'):
        marker = bool(QUOTE_MARKER_RE.match(line.strip())) or bool(QUOTE_MARKER_RE.match(line))
        if marker and current:
            blocks.append('\n'.join(current).strip())
            current = [line]
        else:
            current.append(line)
    if current:
        blocks.append('\n'.join(current).strip())
    expanded = []
    for block in blocks:
        expanded.extend([b.strip() for b in re.split(r'\n\s*\n+', block) if b.strip()])
    return expanded


def classify_embedded_block(block: str):
    low = block.lower()
    evidence = []
    frag_type = None
    confidence = None
    if 'from:' in low and (SVEIN_EMAIL in low or SVEIN_NAME in low):
        if 'forwarded message' in low:
            evidence.append('FORWARDED_FROM_MATCH')
            frag_type = 'forwarded_svein'
        else:
            evidence.append('QUOTED_FROM_MATCH')
            frag_type = 'quoted_svein'
        confidence = 'high'
    elif MAIL_REF_RE.search(block):
        evidence.append('MAIL_TEXT_REFERENCE')
        frag_type = 'review_block'
        confidence = 'review'
    else:
        return None
    return {
        'fragment_type': frag_type,
        'confidence': confidence,
        'evidence_codes': sorted(set(evidence)),
        'text': block.strip(),
    }


def relevant_message_for_attachments(top_evidence, fragment_records):
    if 'FROM_EXACT' in top_evidence or 'FROM_EMAIL_MATCH' in top_evidence:
        return True
    return any(r['confidence'] in ('high', 'medium') and r['fragment_type'] in ('quoted_svein', 'forwarded_svein', 'direct_primary') for r in fragment_records)


def attachment_candidate_info(msg, filename: str, top_evidence, body_text: str):
    evidence = []
    note_parts = []
    ext = Path(filename).suffix.lower()
    if ext in ATTACH_EXTS:
        evidence.append('FILENAME_MATCH')
        note_parts.append(f'extension {ext} is in candidate document set')
    if MAIL_REF_RE.search(body_text or ''):
        evidence.append('MAIL_TEXT_REFERENCE')
        note_parts.append('message body references Svein as author/sender of material')
    subject = msg.get('Subject', '')
    if re.search(r'(?i)utkast|rapport|oversikt|regneark|vedlegg|re:|sv:|styreprotokoll|redegjørelse', subject):
        evidence.append('THREAD_CONTEXT_MATCH')
        note_parts.append('subject suggests document/work-product context')
    classification = None
    confidence = 'medium'
    if ('FROM_EXACT' in top_evidence or 'FROM_EMAIL_MATCH' in top_evidence) and ('MAIL_TEXT_REFERENCE' in evidence or 'THREAD_CONTEXT_MATCH' in evidence):
        evidence.append('FROM_EXACT' if 'FROM_EXACT' in top_evidence else 'FROM_EMAIL_MATCH')
        note_parts.append('attachment is on a direct Svein message with work-product context')
        classification = 'likely_svein_created'
        confidence = 'high' if 'MAIL_TEXT_REFERENCE' in evidence else 'medium'
    elif 'FILENAME_MATCH' in evidence and ('FROM_EXACT' in top_evidence or 'FROM_EMAIL_MATCH' in top_evidence):
        evidence.append('FROM_EXACT' if 'FROM_EXACT' in top_evidence else 'FROM_EMAIL_MATCH')
        note_parts.append('attachment is on a direct Svein message')
        classification = 'relevant_svein_related'
    elif 'FILENAME_MATCH' in evidence or 'MAIL_TEXT_REFERENCE' in evidence or 'THREAD_CONTEXT_MATCH' in evidence:
        classification = 'relevant_svein_related'
    if not classification:
        return None
    return classification, sorted(set(evidence)), confidence, '; '.join(note_parts)


def save_fragment(record, text, context_text=None):
    folder = FRAGMENTS_DIR / record['mailbox_folder']
    folder.mkdir(parents=True, exist_ok=True)
    safe_mid = sha256_bytes((record['message_id'] or record['source_path']).encode('utf-8'))[:12]
    fname = f"{safe_mid}-{record['fragment_id']}.txt"
    path = folder / fname
    header = [
        f"message_id: {record['message_id']}",
        f"source_path: {record['source_path']}",
        f"mailbox_folder: {record['mailbox_folder']}",
        f"top_level_from: {record['top_level_from']}",
        f"fragment_id: {record['fragment_id']}",
        f"fragment_type: {record['fragment_type']}",
        f"confidence: {record['confidence']}",
        f"evidence_codes: {', '.join(record['evidence_codes'])}",
        '',
        '## PRIMARY_TEXT' if record['fragment_type'] == 'direct_primary' else '## TEXT',
        text.strip(),
    ]
    if context_text:
        header.extend(['', '## QUOTED_CONTEXT', context_text.strip()])
    path.write_text('\n'.join(header).strip() + '\n', encoding='utf-8')
    return str(path)


def save_attachment(mailbox_folder: str, filename: str, data: bytes):
    digest = sha256_bytes(data)
    folder = ATTACHMENTS_DIR / mailbox_folder
    folder.mkdir(parents=True, exist_ok=True)
    base = normalize_filename(filename)
    path = folder / f"{digest[:12]}-{base}"
    if not path.exists():
        path.write_bytes(data)
    return str(path), digest


def iter_message_paths():
    for folder in sorted(SOURCE_ROOT.iterdir()):
        if not folder.is_dir():
            continue
        for sub in ('cur', 'new'):
            subdir = folder / sub
            if not subdir.is_dir():
                continue
            for path in sorted(subdir.iterdir()):
                if path.is_file():
                    yield folder.name, path


def main():
    MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)
    fragment_count = 0
    candidate_count = 0
    with FRAGMENTS_MANIFEST.open('w', encoding='utf-8') as frag_out, CANDIDATE_MANIFEST.open('w', encoding='utf-8') as cand_out:
        for mailbox_folder, path in iter_message_paths():
            with path.open('rb') as f:
                try:
                    msg = BytesParser(policy=policy.default).parse(f)
                except Exception:
                    continue
            body_text = extract_body(msg)
            top_from = msg.get('From', '')
            top_evidence = from_matches(top_from)
            fragment_records = []

            if top_evidence and body_text:
                primary_text, context_text = split_primary_and_context(body_text)
                idx = 1
                if primary_text:
                    record = {
                        'message_id': msg.get('Message-ID', ''),
                        'source_path': str(path),
                        'mailbox_folder': mailbox_folder,
                        'top_level_from': top_from,
                        'fragment_id': f'f{idx:03d}',
                        'fragment_type': 'direct_primary',
                        'confidence': 'high',
                        'evidence_codes': sorted(set(top_evidence + (['QUOTED_CONTEXT_PRESENT'] if context_text else []))),
                        'text': primary_text,
                    }
                    if context_text:
                        record['quoted_context'] = context_text
                    record['saved_path'] = save_fragment(record, primary_text, context_text=context_text if context_text else None)
                    frag_out.write(json.dumps(record, ensure_ascii=False) + '\n')
                    fragment_records.append(record)
                    fragment_count += 1
                    idx += 1
                if context_text:
                    context_record = {
                        'message_id': msg.get('Message-ID', ''),
                        'source_path': str(path),
                        'mailbox_folder': mailbox_folder,
                        'top_level_from': top_from,
                        'fragment_id': f'f{idx:03d}',
                        'fragment_type': 'quoted_context',
                        'confidence': 'medium',
                        'evidence_codes': ['QUOTED_CONTEXT_PRESENT'],
                        'text': context_text,
                    }
                    context_record['saved_path'] = save_fragment(context_record, context_text)
                    frag_out.write(json.dumps(context_record, ensure_ascii=False) + '\n')
                    fragment_records.append(context_record)
                    fragment_count += 1
            else:
                idx = 1
                for block in split_blocks(body_text):
                    classified = classify_embedded_block(block)
                    if not classified:
                        continue
                    record = {
                        'message_id': msg.get('Message-ID', ''),
                        'source_path': str(path),
                        'mailbox_folder': mailbox_folder,
                        'top_level_from': top_from,
                        'fragment_id': f'f{idx:03d}',
                        'fragment_type': classified['fragment_type'],
                        'confidence': classified['confidence'],
                        'evidence_codes': classified['evidence_codes'],
                        'text': classified['text'],
                    }
                    record['saved_path'] = save_fragment(record, record['text'])
                    frag_out.write(json.dumps(record, ensure_ascii=False) + '\n')
                    fragment_records.append(record)
                    fragment_count += 1
                    idx += 1

            if relevant_message_for_attachments(top_evidence, fragment_records):
                for part in msg.walk():
                    if part.is_multipart():
                        continue
                    if (part.get_content_disposition() or '').lower() != 'attachment':
                        continue
                    filename = part.get_filename() or 'attachment.bin'
                    data = part.get_payload(decode=True) or b''
                    saved_path, digest = save_attachment(mailbox_folder, filename, data)
                    candidate = attachment_candidate_info(msg, filename, top_evidence, body_text)
                    if candidate:
                        classification, evidence_codes, confidence, note = candidate
                        record = {
                            'message_id': msg.get('Message-ID', ''),
                            'attachment_filename': filename,
                            'saved_path': saved_path,
                            'sha256': digest,
                            'classification': classification,
                            'confidence': confidence,
                            'evidence_codes': evidence_codes,
                            'evidence_note': note,
                        }
                        cand_out.write(json.dumps(record, ensure_ascii=False) + '\n')
                        candidate_count += 1
    print(json.dumps({'fragments_written': fragment_count, 'candidate_documents_written': candidate_count}, ensure_ascii=False))

if __name__ == '__main__':
    main()
