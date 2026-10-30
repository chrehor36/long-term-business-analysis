import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# ISG revenue 2013-2016 sits under SalesRevenueServicesNet, which row.py does not read; filled from xb_out.txt (filed-statement tags)
fill={'III':{'2013':210982,'2014':209617,'2015':209240,'2016':216499}}
for k in ['III','HCKT','FORR','IT','CRAI','HURN']:
    rows={}
    for l in open(k+'_row.txt',encoding='utf-8'):
        c=[x.strip() for x in l.split('|')]
        if len(c)>9 and re.match(r'\d{4}-',c[1]):
            y=c[1][:4]
            if c[1][5:7] in ('01',) : y=str(int(y)-1)
            def n(x):
                try: return float(x.replace(',','').replace('%',''))
                except: return None
            rows[y]=dict(s=n(c[2]),o=n(c[3]),m=n(c[4]),r=n(c[6]),rg=n(c[9]))
    for y,v in fill.get(k,{}).items():
        rows[y]['s']=v/1000; rows[y]['m']=round(rows[y]['o']/rows[y]['s']*100,1) if rows[y]['o'] is not None else None
    ms=[(y,rows[y]['m']) for y in sorted(rows) if y>='2012' and rows[y]['m'] is not None]
    m5=[rows[y]['m'] for y in ['2021','2022','2023','2024','2025'] if y in rows and rows[y]['m'] is not None]
    m10=[rows[y]['m'] for y in [str(x) for x in range(2016,2026)] if y in rows and rows[y]['m'] is not None]
    s15=rows.get('2015',{}).get('s'); s25=rows.get('2025',{}).get('s')
    g=((s25/s15)**0.1-1)*100 if s15 and s25 else None
    print(k,'5y avg op margin 2021-25: %.1f%%'%(sum(m5)/len(m5)),'| 10y avg 2016-25: %.1f%%'%(sum(m10)/len(m10)),'| max since 2012:',max(ms,key=lambda t:t[1]),'| rev 2015->2025:',s15,s25,'CAGR %s'%(g and round(g,1)),'| ret NTOA 2021-25:',[rows[y]['r'] for y in ['2021','2022','2023','2024','2025'] if y in rows],'| incl gw:',[rows[y]['rg'] for y in ['2021','2022','2023','2024','2025'] if y in rows])
