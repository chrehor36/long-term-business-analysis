"""Summarise each *_row.txt: sales CAGR 2016->2025 (9y) and 2020->2025 (5y), op margin, NTOA return, incl-GW return for 2023-2025."""
import re,glob,sys
sys.stdout.reconfigure(encoding='utf-8')
print('| co | 9y CAGR | 5y CAGR | op margin 23/24/25 | ret NTOA 23/24/25 | ret incl gw 23/24/25 | gw share 25 | op source |')
for f in ['ABBV_row.txt']+sorted(x for x in glob.glob('*_row.txt') if x!='ABBV_row.txt'):
    s=open(f,encoding='utf-8').read()
    src='proxy' if 'PROXY' in s else 'filed'
    ser=dict((k[:4],float(v.replace(',',''))) for k,v in re.findall(r'(\d{4}-\d\d-\d\d):([\d,]+)',s.split('sales series:')[1].split('\n')[0]))
    # JNJ: 2016-01-03 is FY2015 end; key by year of end-3 days
    ser={}
    for k,v in re.findall(r'(\d{4})-(\d\d)-\d\d:([\d,]+)',s.split('sales series:')[1].split('\n')[0]) and [(a+'-'+b,c) for a,b,c in re.findall(r'(\d{4})-(\d\d)-\d\d:([\d,]+)',s.split('sales series:')[1].split('\n')[0])]:
        y=int(k[:4])-(1 if k[5:7]=='01' else 0); ser[y]=float(v.replace(',',''))
    g=lambda a,b,n: '%.1f%%'%(100*((ser[b]/ser[a])**(1/n)-1)) if a in ser and b in ser else 'n/f'
    rows={}
    for line in s.splitlines():
        m=re.match(r'\| (\d{4})-(\d\d)-\d\d \|(.*)',line)
        if m:
            y=int(m.group(1))-(1 if m.group(2)=='01' else 0); c=[x.strip() for x in m.group(3).split('|')]
            rows[y]=c
    pick=lambda i: ' / '.join(rows.get(y,['']*9)[i] for y in (2023,2024,2025))
    print(f"| {f[:-8]} | {g(2016,2025,9)} | {g(2020,2025,5)} | {pick(2)} | {pick(4)} | {pick(7)} | {rows.get(2025,['']*9)[6]} | {src} |")
