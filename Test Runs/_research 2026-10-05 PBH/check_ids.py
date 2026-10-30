import csv, re, sys
L="C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv"
rows={r["id"]:r["quote_verbatim"] for r in csv.DictReader(open(L,encoding="utf-8-sig"))}
t=open("C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-05 Run - PBH Prestige Consumer Healthcare.md",encoding="utf-8").read()
norm=lambda s: re.sub(r"\s+"," ",s).strip()
eids=re.findall(r"\[E\d+-\d+\]",t); print("E-ids:",eids)
ids=list(re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",t))
print("id occurrences:",len(ids),"distinct:",len(set(m.group(1) for m in ids)))
bad=[m.group(1) for m in ids if m.group(1) not in rows]; print("missing ids:",bad)
prev_end=0; problems=0
for m in ids:
    seg=t[prev_end:m.start()]
    prev_end=m.end()
    # quotes in the segment; take the last up to 2 quotes that end within 40 chars of each other near the id
    qs=list(re.finditer(r'"([^"]{3,}?)"',seg))
    if not qs: continue
    # the quote(s) adjacent: last quote must end within 12 chars of the id
    tail=seg[qs[-1].end():]
    if len(norm(tail))>12: continue
    cand=[qs[-1]]
    if len(qs)>1:
        gap=seg[qs[-2].end():qs[-1].start()]
        if norm(gap) in ("and",",","and the",";"): cand.insert(0,qs[-2])
    row=norm(rows.get(m.group(1),""))
    for q in cand:
        for frag in q.group(1).split("[...]"):
            f=norm(frag.strip(" .,;"))
            if f and f not in row:
                problems+=1; print("NOT IN ROW",m.group(1),"|",f[:120])
print("fragment problems:",problems)
