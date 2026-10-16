"""Builds COMPATIBILITY.md from data/titles.json, or checks that the committed file is up to date.
usage: python -I tools/gen_table.py          (write COMPATIBILITY.md)
       python -I tools/gen_table.py --check  (exit 1 if COMPATIBILITY.md is stale or the data is invalid)"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATUS = {
    'playable': ('Playable', 'Can be played start to finish; only minor problems.'),
    'ingame': ('In-game', 'Gets into gameplay, with problems that affect play or looks.'),
    'menus': ('Menus', 'Reaches menus but not stable gameplay.'),
    'boots': ('Boots', 'Starts and shows something, then stops or fails.'),
    'nothing': ('Nothing', 'Does not start.'),
}
ORDER = list(STATUS)


def load():
    data = json.load(open(os.path.join(ROOT, 'data', 'titles.json'), encoding='utf-8'))
    problems = []; seen = set()
    for i, t in enumerate(data['titles']):
        name = t.get('title', '#%d' % i)
        for k in ('title', 'region', 'executable_sha256', 'status', 'summary'):
            if not t.get(k): problems.append('%s: missing %s' % (name, k))
        h = t.get('executable_sha256', '')
        if not re.fullmatch(r'[0-9a-f]{64}', h): problems.append('%s: executable_sha256 must be 64 lowercase hex characters' % name)
        if h in seen: problems.append('%s: duplicate executable hash' % name)
        seen.add(h)
        if t.get('status') not in STATUS: problems.append('%s: status must be one of %s' % (name, ', '.join(ORDER)))
        for r in t.get('reports', []):
            if r.get('result') not in STATUS: problems.append('%s: a report has an invalid result' % name)
    return data['titles'], problems


def anchor(t):
    # GitHub's heading anchor: lowercase, punctuation dropped, spaces to hyphens
    h = '%s (%s)' % (t['title'], t['region']); return re.sub(r'\s', '-', re.sub(r'[^\w\s-]', '', h.lower()))


def render(titles):
    out = ['# Compatibility list', '',
           'What has been tried on [Reforged](https://github.com/lPuffyy/reforged) and how it went. Entries are per **build** of a program (the SHA-256 of its main executable, which the',
           'companion tool prints), so different regions or revisions of the same title are separate rows. This file is generated from `data/titles.json`; do not edit it by hand.', '',
           'This list only describes results. It contains no game files, no links to them and no instructions for getting them. Names are used only to say which program was tested;',
           'the project is not affiliated with or endorsed by any console maker or publisher.', '', '## Status levels', '']
    out += ['- **%s**: %s' % STATUS[k] for k in ORDER]
    out += ['', '## Tested', '', '| Title | Region | Status |', '|---|---|---|']
    for t in sorted(titles, key=lambda t: (ORDER.index(t['status']), t['title'].lower(), t['region'])):
        out.append('| [%s](#%s) | %s | %s |' % (t['title'], anchor(t), t['region'], STATUS[t['status']][0]))
    out += ['', '## Details', '']
    for t in sorted(titles, key=lambda t: (t['title'].lower(), t['region'])):
        out += ['### %s (%s)' % (t['title'], t['region']), '', '**Status:** %s' % STATUS[t['status']][0], '', t['summary'], '']
        if t.get('known_issues'): out += ['**Known issues**', ''] + ['- ' + x for x in t['known_issues']] + ['']
        out += ['**Executable SHA-256**', '', '```', t['executable_sha256'], '```', '']
        if t.get('reports'):
            out += ['**Reports** (newest first)', '']
            for r in t['reports']:
                bits = [r.get('date', ''), 'Reforged ' + r['reforged'] if r.get('reforged') else '', r.get('device', ''), ('iOS ' + r['ios']) if r.get('ios') else '', STATUS[r['result']][0], (r['fps'] + ' fps') if r.get('fps') else '']
                line = '- ' + ', '.join(b for b in bits if b)
                if r.get('notes'): line += '. ' + r['notes']
                out.append(line)
            out.append('')
    out += ['## Add or update a result', '', 'Open an issue with the "Compatibility report" form, or send a pull request that edits `data/titles.json` and the regenerated table. See [CONTRIBUTING.md](CONTRIBUTING.md).', '']
    return '\n'.join(out)


def main():
    titles, problems = load()
    if problems: print('\n'.join(problems)); return 1
    text = render(titles); path = os.path.join(ROOT, 'COMPATIBILITY.md')
    if '--check' in sys.argv:
        have = open(path, encoding='utf-8').read() if os.path.exists(path) else ''
        if have.replace('\r\n', '\n') != text.replace('\r\n', '\n'): print('COMPATIBILITY.md is stale: run python -I tools/gen_table.py'); return 1
        print('ok: %d title(s)' % len(titles)); return 0
    open(path, 'w', encoding='utf-8', newline='\n').write(text); print('wrote COMPATIBILITY.md (%d title(s))' % len(titles)); return 0


if __name__ == '__main__': sys.exit(main())
