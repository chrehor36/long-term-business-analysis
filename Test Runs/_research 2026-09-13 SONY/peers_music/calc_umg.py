d={"FY23":dict(rev=11108,rm=8461,mp=1956,rmop=1393,mpop=269,op=1418,rmad=2042,mpad=470,ad=2369,capex=47,oth=74,cat=178,cfo=1885),
   "FY24":dict(rev=11834,rm=8901,mp=2121,rmop=1752,mpop=321,op=1775,rmad=2275,mpad=511,ad=2661,capex=91,oth=92,cat=266,cfo=1755),
   "FY25":dict(rev=12507,rm=9456,mp=2260,rmop=1985,mpop=371,op=1998,rmad=2423,mpad=549,ad=2810,capex=70,oth=125,cat=345,cfo=1739)}
for k,v in d.items():
    print(k,"RM OP%%=%.1f MP OP%%=%.1f Tot OP%%=%.1f RM AdjEBITDA%%=%.1f MP AdjEBITDA%%=%.1f (capex+other intang)/rev=%.1f%% catalogue/rev=%.1f%% CFO-capex-oth-cat=%d"%(
     100*v['rmop']/v['rm'],100*v['mpop']/v['mp'],100*v['op']/v['rev'],100*v['rmad']/v['rm'],100*v['mpad']/v['mp'],100*(v['capex']+v['oth'])/v['rev'],100*v['cat']/v['rev'],v['cfo']-v['capex']-v['oth']-v['cat']))
