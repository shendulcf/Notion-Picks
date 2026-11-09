#!/usr/bin/env python3
"""Check this repository's Markdown links and bilingual resource parity offline.

Supports inline Markdown links, autolinks, ATX headings, and explicit HTML IDs.
External services are not contacted. Run from any directory with Python 3.
"""
from collections import Counter
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted([*ROOT.glob('*.md'), *ROOT.glob('docs/*.md')])
ERRORS = []


def fail(path, message):
    ERRORS.append(f'{path.relative_to(ROOT)}: {message}')


def prose(text):
    return re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$', '', text,
                  flags=re.M | re.S)


def headings(text):
    used, result = Counter(), set(re.findall(r'<a id="([^"]+)"', text))
    for title in re.findall(r'^#{1,6}\s+(.+)$', prose(text), re.M):
        title = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', title)
        slug = ''.join(c for c in title.lower().strip().replace(' ', '-')
                       if c in '-_' or unicodedata.category(c)[0] in 'LN')
        result.add(slug if not used[slug] else f'{slug}-{used[slug]}')
        used[slug] += 1
    return result


def external_urls(text):
    # The avatar project provides equivalent localized landing pages.
    return Counter(url.replace('notion-avatar.app/en', 'notion-avatar.app/zh')
                   for url in re.findall(r'https?://[^\s)<>]+', prose(text)))


def commands(text):
    return ['\n'.join(line for line in block.splitlines()
                      if line.strip() and not line.lstrip().startswith('#'))
            for block in re.findall(r'```bash\n(.*?)```', text, re.S)]


texts = {p: p.read_text(encoding='utf-8') for p in FILES}
links_checked = 0
for path, text in texts.items():
    if not text.endswith('\n'):
        fail(path, 'missing final newline')
    for number, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            fail(path, f'line {number}: trailing whitespace')
    if text.count('<details>') != text.count('</details>'):
        fail(path, 'unbalanced details tags')
    for table in re.findall(r'(?:^\|.*\n)+', prose(text), re.M):
        widths = {len(re.split(r'(?<!\\)\|', row)) for row in table.splitlines()}
        if len(widths) > 1:
            fail(path, 'inconsistent table columns')
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', prose(text)):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        links_checked += 1
        if not destination.is_relative_to(ROOT) or not destination.is_file():
            fail(path, f'missing or out-of-repository target: {target}')
        elif parsed.fragment and unquote(parsed.fragment) not in headings(destination.read_text()):
            fail(path, f'missing anchor: {target}')
    if path.name.endswith('.en.md'):
        if path.with_name(path.name.replace('.en.md', '.md')) not in texts:
            fail(path, 'missing Chinese counterpart')
        continue
    english = path.with_name(path.stem + '.en.md')
    if english not in texts:
        fail(path, 'missing English counterpart')
        continue
    other = texts[english]
    for source, label, counterpart in [(path, 'English', english),
                                       (english, '简体中文', path)]:
        if f'[{label}]({counterpart.name})' not in texts[source]:
            fail(source, 'missing language switch')
    if external_urls(text) != external_urls(other):
        fail(path, 'external resource links differ between languages')
    if commands(text) != commands(other):
        fail(path, 'shell examples differ between languages')
    if len(re.findall(r'^\|', prose(text), re.M)) != len(re.findall(r'^\|', prose(other), re.M)):
        fail(path, 'table row counts differ between languages')

if ERRORS:
    print('\n'.join(ERRORS), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {len(FILES)} documents; {links_checked} local links; bilingual resources and commands match.')
