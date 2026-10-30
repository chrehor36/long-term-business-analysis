import json,sys
d=json.load(open(sys.argv[1])); g=d['facts']['us-gaap']
def inst(tag):
    out={}
    for x in g.get(tag,{}).get('units',{}).get('USD',[]):
        if x['form'].startswith('10-K') and x['end'][5:]=='12-31':
            y=x['end'][:4]
            if y not in out or x['filed']>out[y][1]: out[y]=(x['val'],x['filed'])  # latest filed
    return out
tags=sys.argv[2:]
yrs=[str(y) for y in range(2015,2026)]
print('tag'.ljust(42),' '.join(y.rjust(7) for y in yrs))
for t in tags:
    a=inst(t); print(t[:42].ljust(42),' '.join((f"{a[y][0]/1e6:7.0f}" if y in a else '      -') for y in yrs))
