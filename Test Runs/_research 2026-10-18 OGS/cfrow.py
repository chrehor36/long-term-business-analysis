import re, sys
f, start = sys.argv[1], int(sys.argv[2])
lines = open(f, encoding="utf-8").read().splitlines()[start-1:start+400]
text = "\n".join(lines)
labels = ["Net income","Depreciation and amortization","Deferred income taxes","Share-based compensation expense","Provision for doubtful accounts","Asset removal costs","Cash provided by operating activities","Cash provided by (used in) operating activities","Capital expenditures","Other investing expenditures","Other investing receipts","Issuance of common stock","Dividends paid","Cash paid for interest, net of amounts capitalized","Cash paid (received) for income taxes, net","Cash paid for income taxes, net"]
for lab in labels:
    i = text.find("\n"+lab)
    if i < 0: continue
    seg = text[i+len(lab)+1:i+len(lab)+400]
    nums = re.findall(r"\(?[\d,]+\.?\d*\s*\n?\s*\|?\s*\)?", seg)
    vals=[]
    for m in re.finditer(r"(\(?)\s*([\d]{1,3}(?:,\d{3})+|\d+)\s*(\n\s*\|\s*\))?", seg):
        v = float(m.group(2).replace(",",""))
        neg = m.group(1)=="(" or (m.group(3) is not None)
        vals.append(-v if neg else v)
        if len(vals)==3: break
    print(f"{lab:55s} {vals}")
