import re,glob,json
def norm(t):
    t='\n'.join(l for l in t.split('\n') if len(l)<3000)
    t=re.sub(r'[ \t]*\|[ \t]*',' | ',t); t=re.sub(r'(\|\s*)+','| ',t); return re.sub(r'\s+',' ',t)
def num(s):
    s=s.replace('$','').replace(',','').replace(' ','').replace('|','')
    neg=s.startswith('(')
    s=s.strip('()')
    try: v=float(s)
    except: return None
    return -v if neg else v
LINES={'ocf':r'Net cash provided by operating activities','sbc':r'Amortization of (unearned share-based compensation|unearned compensation|share-based compensation|stock-based compensation)|Share-based compensation|Stock-based compensation','da':r'Depreciation and amortization','capex':r'Capital expenditures','acq':r'Acquisitions? of businesses?( and marine equipment)?,?( net of cash acquired)?|Acquisitions of marine equipment','proc':r'Proceeds from (the )?disposition of assets','mm':r'Amortization of major maintenance costs','int':r'Cash paid (\(received\) )?during the (year|period): \| Interest( paid)?','tax':r'Income taxes( paid)?(?= \|)','buy':r'(Purchase of treasury stock|Treasury stock purchases)','div':r'Dividends paid'}
out={}
for fn in sorted(glob.glob('tenk_*.txt')):
    y=int(fn[5:9]); t=norm(open(fn,encoding='utf-8').read())
    i=t.find('Cash flows from operating activities')
    if i<0: i=t.find('Operating activities:')
    seg=t[i:i+9000]
    j=t.find('Supplemental disclosures of cash flow',i); sup=t[j:j+700]; row={}
    for k,pat in LINES.items():
        m=re.search(r'('+pat+r')[^|\d(]{0,60}\| (\$ \| )?(\(? ?[\d,]+ ?\|? ?\)?)',sup if k in ('int','tax') else seg)
        if m:
            row[k]=num(m.group(m.lastindex))
    out[y]=row; print(y,row)
json.dump(out,open('cf_parsed.json','w'),indent=1)
