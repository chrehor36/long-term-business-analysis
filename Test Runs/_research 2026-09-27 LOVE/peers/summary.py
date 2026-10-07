import json
rows=json.load(open('peers/row_rows.json'))
print('ticker  last-3-FY OM (oldest->newest)      cum OM all yrs  cum OM last 5  GM last  OI/avg(A-C) last 3            years')
for t,n,rs in rows:
    rs=[r for r in rs if r[3] is not None]
    oms=['%5.1f%%'%(100*r[3]/r[1]) for r in rs[-3:]]
    cum=sum(r[3] for r in rs)/sum(r[1] for r in rs)
    c5=sum(r[3] for r in rs[-5:])/sum(r[1] for r in rs[-5:])
    gm=rs[-1][2]/rs[-1][1] if rs[-1][2] else None
    rets=[]
    for i in range(1,len(rs)):
        if rs[i][4] and rs[i-1][4]: rets.append(rs[i][3]/((rs[i][4]+rs[i-1][4])/2))
    print('%-6s %-34s %6.1f%%        %6.1f%%     %s   %-30s %s-%s'%(t,' '.join(oms),100*cum,100*c5,('%5.1f%%'%(100*gm)) if gm else '  -  ',' '.join('%5.1f%%'%(100*x) for x in rets[-3:]),rs[0][0][:4],rs[-1][0][:4]))
