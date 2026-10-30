"""Citation check for the AME run file.
1. No E-ids (v4 ledger ids) anywhere in the run file.
2. Every M/L/R id cited exists in principle_ledger_v5.csv.
3. Every quoted fragment that sits immediately before an id (the quote, then optional words, then **[id]**
   within the same sentence-span) is found verbatim in that row's quote (curly/straight quotes and the
   [...] elision normalised; each piece between [...] must be in the row, in order).
Usage: python check_cites.py "<run file>"
"""
import csv, re, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEDGER = os.path.join(ROOT, "principle_ledger_v5.csv")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace("�", "?")
    s = re.sub(r"\*\*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def main(path):
    rows = {}
    with open(LEDGER, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            rows[r["id"]] = norm(r["quote_verbatim"])
    text = open(path, encoding="utf-8").read()
    bad = 0
    eids = re.findall(r"\[E\d-\d+\]", text)
    if eids:
        print("E-ids found:", sorted(set(eids))); bad += 1
    ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
    missing = sorted(set(i for i in ids if i not in rows))
    if missing:
        print("ids not in ledger:", missing); bad += 1
    # quoted fragment followed (within 40 chars, no other quote between) by one or more ids
    pat = re.compile(r"\"([^\"]{3,600})\"([^\"\n]{0,40}?)((?:\s*,?\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)")
    checked = 0
    for m in pat.finditer(text.replace("“", '"').replace("”", '"')):
        frag = m.group(1)
        cited = re.findall(r"\[([MLR]\d{4}-\d{3})\]", m.group(3))
        pieces = [norm(p) for p in re.split(r"\[\.\.\.\]|\.\.\.", frag) if norm(p).strip(" .,;:")]
        ok_any = False
        for cid in cited:
            q = rows.get(cid, "")
            pos, ok = 0, True
            for p in pieces:
                p2 = p.strip(" .,;:")
                j = q.find(p2, pos)
                if j < 0:
                    ok = False; break
                pos = j + len(p2)
            if ok:
                ok_any = True; break
        checked += 1
        if not ok_any:
            bad += 1
            print(f"FRAGMENT NOT IN ROW {cited}: \"{frag[:120]}\"")
    print(f"ids cited: {len(set(ids))} distinct; fragments checked: {checked}; problems: {bad}")
    return bad


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1]) else 0)
