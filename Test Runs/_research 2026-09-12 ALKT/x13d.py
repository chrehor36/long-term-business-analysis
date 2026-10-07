import re,sys,html,glob
for f in sorted(glob.glob("13D*primary_doc.xml"))+sorted(glob.glob("13GA*primary_doc.xml")):
    s=open(f,encoding='utf-8',errors='replace').read()
    def g(tag):
        return [html.unescape(x) for x in re.findall(r'<(?:[a-z]+:)?%s>(.*?)</(?:[a-z]+:)?%s>'%(tag,tag),s,re.S)]
    print("=====",f)
    print(" event", g("dateOfEvent"), "filer", g("reportingPersonName")[:1], "pct", g("percentOfClass")[:1], "agg", g("aggregateAmountOwned")[:1])
    for t in ["purposeOfTransaction","transactionPurpose","item4","interestInSecurities","contractsArrangements","sourceOfFunds","fundsSource","item3","item6"]:
        for v in g(t):
            print(" --",t,":",re.sub(r'\s+',' ',v)[:3000])
