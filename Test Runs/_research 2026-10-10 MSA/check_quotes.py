"""Run check for the MSA run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment (in "..." or “...”) standing in the stretch of a line between the previous id
(or the line start) and an id is found verbatim in that id's row. Elisions written [...] split a
fragment into parts, each checked. Normalised before matching: curly/straight apostrophes and quotes,
whitespace runs, the replacement character, and dash forms. Nothing else is normalised."""
import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = "C:/Users/chreh/OneDrive/Documents/BRK/"
run = open(ROOT + "Test Runs/2026-10-10 Run - MSA MSA Safety.md", encoding="utf-8").read()
rows = {a["id"]: a for a in csv.DictReader(open(ROOT + "principle_ledger_v5.csv", encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\ufffd", "'").replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d+-\d+\]", run)
if eids: print("E-ids found:", eids); bad += 1
idpat = re.compile(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*")
n_ids = n_frag = 0
# logical lines: a paragraph or list item joined across its wrapped lines
logical, cur, curln = [], "", 0
for ln, raw in enumerate(run.splitlines(), 1):
    starts = (not raw.strip()) or raw.lstrip().startswith(("- ", "|", "#", "**VERDICT", "* ")) or re.match(r"\s*\d+\.\s", raw)
    if starts or not cur:
        if cur: logical.append((curln, cur))
        cur, curln = raw, ln
    else:
        cur += " " + raw.strip()
if cur: logical.append((curln, cur))
for ln, line in logical:
    last = 0
    for m in idpat.finditer(line):
        i = m.group(1); n_ids += 1
        if i not in rows:
            print(f"line {ln}: MISSING id {i}"); bad += 1; last = m.end(); continue
        seg = line[last:m.start()]
        q = norm(rows[i]["quote_verbatim"])
        for f in re.findall(r'"([^"]{3,}?)"|\u201c([^\u201d]{3,}?)\u201d', seg):
            f = f[0] or f[1]
            for part in f.split("[...]"):
                p = norm(part).strip(" .,;:")
                if len(p) < 3: continue
                n_frag += 1
                if p not in q and p.replace('"', "'") not in q.replace('"', "'"):
                    print(f"line {ln}: fragment not in {i}: {p[:90]!r}"); bad += 1
        last = m.end()
print(f"ids checked: {n_ids}; fragments checked: {n_frag}; problems: {bad}")
sys.exit(1 if bad else 0)
