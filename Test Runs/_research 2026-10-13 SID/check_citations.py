import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run=open("Test Runs/2026-10-13 Run - SID Companhia Siderurgica Nacional.md",encoding="utf-8").read()
rows={r["id"]:r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv",encoding="utf-8-sig"))}
bad=0
eids=re.findall(r"\[E\d+-\d+\]",run)
if eids: print("E-ids found:",eids); bad+=1
ids=re.findall(r"\[([MLR]\d{4}-\d{3})\]",run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id",i); bad+=1
def norm(s): return re.sub(r"\s+"," ",s.replace("\u2019","'").replace("\u2018","'").replace("\u201c",'"').replace("\u201d",'"')).strip()
# a quoted fragment directly before an id (same paragraph): "...." **[ID]** or "..." [...] "..." **[ID]**
checked=0
for para in re.split(r"\n\s*\n|\n- |\n\| ",run):
    for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*",para):
        pid=m.group(1)
        # take text since previous id marker
        start=max([x.end() for x in re.finditer(r"\*\*\[[MLR]\d{4}-\d{3}\]\*\*",para[:m.start()])] or [0])
        seg=para[start:m.start()]
        # drop backtick spans (file names) before finding quotes
        seg=re.sub(r"`[^`]*`","",seg)
        quotes=re.findall(r'"([^"]{6,})"',seg)
        for q in quotes:
            checked+=1
            row=norm(rows.get(pid,""))
            if norm(q) not in row:
                print(f"NOT IN ROW {pid}: \"{q[:90]}\""); bad+=1
print(f"ids cited: {len(set(ids))}; fragments checked: {checked}; problems: {bad}")
