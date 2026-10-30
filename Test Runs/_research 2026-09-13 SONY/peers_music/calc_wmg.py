d={"FY25":dict(rev=6707,rm=5408,mp=1306,rmoi=850,mpoi=224,oi=694,rmad=1269,mpad=361,ad=1443,capex=139,da=376,cat=195,adv=312,cfo=678),
   "FY24":dict(rev=6426,rm=5223,mp=1210,rmoi=916,mpoi=238,oi=823,rmad=1282,mpad=330,ad=1432,capex=116,da=327,cat=187,adv=222,cfo=754),
   "FY23":dict(rev=6037,rm=4955,mp=1088,rmoi=875,mpoi=200,oi=790,rmad=1094,mpad=296,ad=1235,capex=127,da=332,cat=114,adv=191,cfo=687)}
for k,v in d.items():
    print(k, "RM OI%%=%.1f MP OI%%=%.1f Tot OI%%=%.1f RM AdjOIBDA%%=%.1f MP AdjOIBDA%%=%.1f capex/rev=%.1f%% catalog/rev=%.1f%% CFO-capex-catalog=%d" % (
      100*v['rmoi']/v['rm'],100*v['mpoi']/v['mp'],100*v['oi']/v['rev'],100*v['rmad']/v['rm'],100*v['mpad']/v['mp'],100*v['capex']/v['rev'],100*v['cat']/v['rev'],v['cfo']-v['capex']-v['cat']))
