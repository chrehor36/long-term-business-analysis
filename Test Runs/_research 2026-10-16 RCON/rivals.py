"""Rivals named in RCON's FY2026 20-F that file with the SEC: annual revenue and operating income from their 10-K XBRL. Transcription only."""
import json, urllib.request, sys
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
cos={"HON":773840,"EMR":32604,"ROK":1024478}
for tk,cik in cos.items():
    raw=open(f"cache/facts_{tk}.json","rb").read()
    g=json.loads(raw)["facts"]["us-gaap"]
    def ser(tags):
        out={}
        for t in tags:
            for r in g.get(t,{}).get("units",{}).get("USD",[]):
                if r.get("form")=="10-K" and r.get("fp")=="FY" and "start" in r:
                    from datetime import date
                    d=(date.fromisoformat(r["end"])-date.fromisoformat(r["start"])).days
                    if not 350<=d<=380: continue
                    y=r["end"][:4]
                    if y not in out or r["filed"]>out[y][1]: out[y]=(r["val"],r["filed"],t,r["accn"])
        return out
    rev=ser(["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet"])
    op=ser(["OperatingIncomeLoss"])
    ni=ser(["NetIncomeLoss"])
    print(tk)
    for y in sorted(rev):
        if y<"2015": continue
        o=op.get(y,(None,))[0]; n=ni.get(y,(None,))[0]
        print(f"  FY{y} rev {rev[y][0]/1e6:,.0f}M  opinc {'' if o is None else f'{o/1e6:,.0f}M ({o/rev[y][0]*100:.1f}%)'}  NI {'' if n is None else f'{n/1e6:,.0f}M ({n/rev[y][0]*100:.1f}%)'}  accn {rev[y][3]}")
