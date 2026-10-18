import re,sys
keys=["Cash and cash equivalents","Trade accounts receivable","Property, plant and equipment","Total Assets","Borrowings","Lease liabilities","Other payable","Total Current Liabilities","Total Current Assets","Retained earnings","Accumulated","Shareholder","Total Equity","Revenue","Direct costs","Profit / (loss) for the year","Loss for the year","Profit for the year","Net cash generated from operating","Net cash from operating","Net cash (used in) / generated from operating","Net cash flows from operating","Purchase of property","Payments for property","Additions to property","Capital work","Net cash used in investing","operating activities"]
f=sys.argv[1]; t=open(f,encoding='utf-8').read().split('\n')
start=[i for i,l in enumerate(t) if re.search(r'Consolidated Statements? of Financial Position\s*\|',l,re.I)]
for s in start[:2]:
    print("=== start",s)
    blk=t[s:s+700]
    j=" ".join(x.strip() for x in blk)
    j=re.sub(r"\|\s*\|","|",j); j=re.sub(r"\s+"," ",j)
    for k in keys:
        for m in re.finditer(re.escape(k)+r"[^|]*\|(?:[^|]*\|){0,8}",j,re.I):
            print("  ",m.group(0)[:220]); 
