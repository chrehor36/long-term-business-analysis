import json,sys
p=sys.argv[1]; pat=[s.lower() for s in sys.argv[2:]]
d=json.load(open(p,encoding='utf-8'))
print(d['entityName'])
for tax,cs in d['facts'].items():
  for k,v in cs.items():
    if any(s in k.lower() for s in pat):
      fy=sorted({f.get('fy') for u in v['units'].values() for f in u if f.get('form')=='10-K' and f.get('fy')})
      print(tax,k,list(v['units'].keys()),fy[:1],fy[-1:] )
