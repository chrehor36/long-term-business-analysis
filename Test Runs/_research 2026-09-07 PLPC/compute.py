import json, os, datetime as dt
D=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(os.path.join(D,'peers_clean.json')))
M=1e6
TICKS=['HUBB','VMI','NVT','AZZ','ATKR','THR','WIRE']
YRS=list(range(2018,2027))
PLPC={ # $M, supplied by caller from PLPC companyfacts
 'rev':{2019:444.86,2020:466.45,2021:517.42,2022:637.02,2023:669.68,2024:593.71,2025:669.34},
 'gp' :{2019:140.59,2020:154.01,2021:166.24,2022:215.18,2023:234.85,2024:189.81,2025:208.54}}

def gm(t,y):
    r=C[t].get(str(y))
    if not r or r['rev'] in (None,0) or r['gp'] is None: return None
    return r['gp']/r['rev']
def om(t,y):
    r=C[t].get(str(y))
    if not r or r['rev'] in (None,0) or r['oi'] is None: return None
    return r['oi']/r['rev']
def roe(t,y,key='eq_used'):
    r=C[t].get(str(y)); p=C[t].get(str(y-1))
    if not r or not p or r['ni'] is None: return None
    b=p.get(key)
    if b in (None,0) or b<0: return None
    return r['ni']/b
def rote(t,y):
    return roe(t,y,'tang')

def P(x): return '   n/a ' if x is None else '%6.1f%%'%(100*x)
def Fm(x): return '    n/a' if x is None else '%7.1f'%(x/M)

print('### TASK B / 1. GROSS MARGIN %  (fiscal-year label = year of period end)')
print('%-6s'%'FY', ''.join('%8d'%y for y in range(2019,2027)))
print('%-6s'%'PLPC', ''.join(('%7.1f%%'%(100*PLPC['gp'][y]/PLPC['rev'][y]) if y in PLPC['rev'] else '%8s'%'-') for y in range(2019,2027)))
for t in TICKS:
    print('%-6s'%t, ''.join((('%7.1f%%'%(100*gm(t,y))) if gm(t,y) is not None else '%8s'%'-') for y in range(2019,2027)))

print()
print('### 2. OPERATING MARGIN %')
print('%-6s'%'FY', ''.join('%8d'%y for y in range(2019,2027)))
for t in TICKS:
    print('%-6s'%t, ''.join((('%7.1f%%'%(100*om(t,y))) if om(t,y) is not None else '%8s'%'-') for y in range(2019,2027)))

print()
print('### 3. RETURN ON BEGINNING SHAREHOLDERS EQUITY %')
print('%-6s'%'FY', ''.join('%8d'%y for y in range(2019,2027)))
for t in TICKS:
    print('%-6s'%t, ''.join((('%7.1f%%'%(100*roe(t,y))) if roe(t,y) is not None else '%8s'%'-') for y in range(2019,2027)))

print()
print('### 4. RETURN ON BEGINNING NET TANGIBLE EQUITY %  (eq - goodwill - other intangibles); neg = tangible equity was negative')
print('%-6s'%'FY', ''.join('%8d'%y for y in range(2019,2027)))
for t in TICKS:
    line=''
    for y in range(2019,2027):
        p=C[t].get(str(y-1)); r=C[t].get(str(y))
        if not p or not r or r['ni'] is None or p.get('tang') is None: line+='%8s'%'-'; continue
        if p['tang']<=0: line+='%8s'%'NEG'; continue
        line+='%7.1f%%'%(100*r['ni']/p['tang'])
    print('%-6s'%t, line)

print()
print('### TANGIBLE EQUITY $M at FY end')
print('%-6s'%'FY', ''.join('%8d'%y for y in range(2018,2027)))
for t in TICKS:
    print('%-6s'%t, ''.join((('%8.1f'%(C[t][str(y)]['tang']/M)) if C[t].get(str(y)) and C[t][str(y)].get('tang') is not None else '%8s'%'-') for y in range(2018,2027)))

print()
print('### 5. REVENUE $M and CAGR 2019 -> latest')
print('%-6s'%'FY', ''.join('%9d'%y for y in range(2019,2027)), '   CAGR')
for t in ['PLPC']+TICKS:
    if t=='PLPC':
        vals={y:PLPC['rev'][y]*M for y in PLPC['rev']}
    else:
        vals={y:C[t][str(y)]['rev'] for y in range(2019,2027) if C[t].get(str(y)) and C[t][str(y)]['rev'] is not None}
    line=''.join((('%9.1f'%(vals[y]/M)) if y in vals else '%9s'%'-') for y in range(2019,2027))
    ys=sorted(vals);
    if 2019 in vals and len(ys)>1:
        last=ys[-1]; n=last-2019
        cagr=(vals[last]/vals[2019])**(1/n)-1
        line+='  %5.1f%% (19->%d)'%(100*cagr,last)
    print('%-6s'%t, line)

print()
print('### SUPPORTING: revenue, GP, OI, NI, equity, tangible equity, CFO, capex, D&A ($M)')
for t in TICKS:
    print('\n-- %s'%t)
    print('%-5s %-11s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s'%('FY','end','rev','gp','oi','ni','eq','gw','intang','tangeq','assets','liab','cfo','capex'))
    for y in range(2018,2027):
        r=C[t].get(str(y))
        if not r: continue
        print('%-5d %-11s %s %s %s %s %s %s %s %s %s %s %s %s'%(y,r['fyend'],Fm(r['rev']),Fm(r['gp']),Fm(r['oi']),Fm(r['ni']),Fm(r['eq_used']),Fm(r['gw']),Fm(r['int']),Fm(r['tang']),Fm(r['assets']),Fm(r['liab']),Fm(r['cfo']),Fm(r['capex'])))
