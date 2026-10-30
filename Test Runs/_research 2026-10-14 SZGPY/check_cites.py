"""Citation check for the SZGPY run file: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv;
(3) every quoted fragment standing directly beside an id (just before it, or just after it with no other id between)
is in that row's quote, with [...] or ... treated as elisions. Prints problems; exit 1 if any."""
import csv
import re
import sys

RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-14 Run - SZGPY Salzgitter.md"
LEDGER = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
ID_RE = re.compile(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*")
QUOTE_RE = re.compile("[\"\u201c]([^\"\u201c\u201d]{3,}?)[\"\u201d]")
NL_ITEM = "\n-"


def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


bad = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", eids)
    bad += 1
ids = list(ID_RE.finditer(text))
for m in ids:
    if m.group(1) not in rows:
        print("MISSING id", m.group(1))
        bad += 1
checked = 0
for m in ids:
    rid = m.group(1)
    if rid not in rows:
        continue
    frags = []
    before = text[max(0, m.start() - 300):m.start()]
    prev = list(ID_RE.finditer(before))
    if prev:
        before = before[prev[-1].end():]
    qs = list(QUOTE_RE.finditer(before))
    if qs:
        tail = before[qs[-1].end():]
        if len(tail) <= 40 and NL_ITEM not in tail:
            frags.append(qs[-1].group(1))
    after = text[m.end():m.end() + 400]
    nxt = ID_RE.search(after)
    if nxt:
        after = after[:nxt.start()]
    aq = QUOTE_RE.search(after)
    rest = text[m.end() + aq.end():m.end() + aq.end() + 40] if aq else ""
    owned_by_next = bool(ID_RE.search(rest))
    if aq and aq.start() < 90 and NL_ITEM not in after[:aq.start()] and not owned_by_next:
        frags.append(aq.group(1))
    row = norm(rows[rid])
    for frag in frags:
        for piece in re.split(r"\[\.\.\.\]|\.\.\.", frag):
            p = norm(piece).strip(" ,.;:")
            if p and p not in row:
                print(f"FRAGMENT NOT IN ROW {rid}: {piece!r}")
                bad += 1
        checked += 1
print(f"ids: {len(ids)} ({len(set(i.group(1) for i in ids))} distinct); fragments checked: {checked}; problems: {bad}")
sys.exit(1 if bad else 0)
