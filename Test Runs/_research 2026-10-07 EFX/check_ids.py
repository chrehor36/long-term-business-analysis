"""Citation check for the EFX run of 2026-10-07 (the brief's check script).

1. No E-ids (v4 ledger ids) anywhere in the run file.
2. Every M/L/R id in bold brackets exists in principle_ledger_v5.csv.
3. Every quoted fragment that sits beside an id (in the same sentence or clause) is in that row's quote,
   after normalising quotes, dashes and whitespace. Elisions written [...] are split and each piece checked.

Usage: python check_ids.py            (checks the run file)
       python check_ids.py ID [ID..]  (prints those rows, for lookup while writing)
"""
import csv, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
LEDGER = ROOT / "principle_ledger_v5.csv"
RUN = ROOT / "Test Runs" / "2026-10-07 Run - EFX Equifax.md"


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-").replace(" ", " ")
    s = re.sub(r"\*\*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def load():
    rows = {}
    with open(LEDGER, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            rows[r["id"]] = r
    return rows


def main():
    rows = load()
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            r = rows.get(i)
            print(i, "MISSING" if r is None else f"[{r['year']}] {r['source_file']}\n   {r['quote_verbatim']}\n")
        return
    text = RUN.read_text(encoding="utf-8")
    bad = 0
    eids = re.findall(r"\bE\d-\d{2}\b", text)
    if eids:
        print("E-ids found:", sorted(set(eids))); bad += 1
    ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
    missing = sorted({i for i in ids if i not in rows})
    if missing:
        print("ids not in the v5 ledger:", missing); bad += 1
    # quoted fragments beside an id: a "..." followed within 40 chars by **[ID]**, possibly several ids
    pat = re.compile(r'"([^"]{3,}?)"[^"\n]{0,60}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
    checked = 0
    for m in pat.finditer(text):
        frag, i = m.group(1), m.group(2)
        if i not in rows:
            continue
        q = norm(rows[i]["quote_verbatim"])
        for piece in re.split(r"\[\.\.\.\]|\.\.\.", frag):
            p = norm(piece).strip(" .,;:")
            if len(p) < 3:
                continue
            checked += 1
            if p not in q:
                print(f"NOT IN ROW {i}: \"{piece.strip()}\""); bad += 1
    print(f"ids cited: {len(set(ids))} distinct; fragments checked: {checked}; problems: {bad}")
    print("PASS" if bad == 0 else "FAIL")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
