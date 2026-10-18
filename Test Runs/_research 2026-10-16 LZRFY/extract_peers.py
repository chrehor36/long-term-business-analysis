"""Pre-tax return on capital for Localiza and three CVM-filing rivals from CVM DFP open data (consolidated).
EBIT (3.05) / [equity (2.03) + loans (2.01.04+2.02.01) - cash (1.01.01) - short-term investments (1.01.02)], year-end and average."""
import zipfile, csv, io, os, collections
base = os.path.dirname(os.path.abspath(__file__)); cache = os.path.join(base,'cache','cvm')
codes = {'19739':'Localiza','23825':'Movida Part.','22691':'Cia Locacao das Americas','27162':'Unidas Locadora'}
want = {'3.01','3.05','3.07','3.11','2.03','2.01.04','2.02.01','1.01.01','1.01.02','1','1.02.04'}
data = collections.defaultdict(dict)
for y in range(2015,2026):
    z = zipfile.ZipFile(os.path.join(cache,f'dfp_cia_aberta_{y}.zip'))
    for s in ('DRE_con','BPA_con','BPP_con'):
        with z.open(f'dfp_cia_aberta_{s}_{y}.csv') as f:
            r = csv.reader(io.TextIOWrapper(f,encoding='latin1'),delimiter=';'); h=next(r)
            for row in r:
                d=dict(zip(h,row)); c=d['CD_CVM'].lstrip('0')
                if c in codes and d['ORDEM_EXERC']=='ÚLTIMO' and d['CD_CONTA'] in want:
                    if s=='DRE_con' and d['DT_INI_EXERC'][5:]!='01-01': continue
                    data[(c,int(d['DT_FIM_EXERC'][:4]))][d['CD_CONTA']] = float(d['VL_CONTA'])/1000
out=[]
for (c,y),v in sorted(data.items()):
    if '3.05' not in v or '2.03' not in v: continue
    nd = v.get('2.01.04',0)+v.get('2.02.01',0)-v.get('1.01.01',0)-v.get('1.01.02',0)
    cap = v['2.03']+nd
    out.append((codes[c],y,v['3.01'],v['3.05'],v.get('3.11'),v['2.03'],nd,cap,v.get('1.02.04',0)))
prev={}
print('company,year,revenue,EBIT,net_income,equity,net_debt,capital,intangibles,EBIT/capital_end,EBIT/capital_avg,EBIT/(capital-intang)_end,NI/equity_end')
with open(os.path.join(base,'peer_returns.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['company','year','revenue_BRLm','EBIT_BRLm','net_income_BRLm','equity_BRLm','net_debt_BRLm','capital_BRLm','intangibles_BRLm','EBIT_cap_end','EBIT_cap_avg','EBIT_tangcap_end','ROE_end'])
    for (n,y,rev,ebit,ni,eq,nd,cap,intg) in out:
        pc = prev.get(n); avg = (cap+pc)/2 if pc else None; prev[n]=cap
        row=[n,y,round(rev),round(ebit),round(ni or 0),round(eq),round(nd),round(cap),round(intg),f'{ebit/cap:.3f}',f'{ebit/avg:.3f}' if avg else '',f'{ebit/(cap-intg):.3f}',f'{(ni or 0)/eq:.3f}']
        w.writerow(row); print(','.join(map(str,row)))
