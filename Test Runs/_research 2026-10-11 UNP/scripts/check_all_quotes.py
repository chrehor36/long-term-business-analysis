"""Every quoted fragment in the run file: is it in a v5 row cited within 400 characters after it? Lists the rest for
manual review (filer quotes, framework wording)."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RUN = "Test Runs/2026-10-11 Run - UNP Union Pacific.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
text = open(RUN, encoding="utf-8").read()
norm = lambda x: re.sub(r"\s+", " ", x).strip()
n_row = n_other = 0
for m in re.finditer(r'(?:(?<=[\s(:])|^)"([^"\n]{12,}?(?:\n[^"\n]*?)*?)"(?=[\s,.;:)])', text):
    frag = m.group(1)
    after = text[m.end():m.end() + 400]
    ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", after)
    pieces = [norm(p).strip(' .,;') for p in frag.split("[...]") if norm(p)]
    hit = [i for i in ids if all(p in norm(rows.get(i, "")) for p in pieces)]
    if hit:
        n_row += 1
    else:
        n_other += 1
        print("NOT IN A NEARBY ROW:", norm(frag)[:150], "| ids after:", ids[:3])
print("in a cited row:", n_row, " other:", n_other)
