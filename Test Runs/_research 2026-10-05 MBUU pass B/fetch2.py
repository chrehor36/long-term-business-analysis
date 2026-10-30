import json, time, re, html, os
from fetch import get
def cell(s):
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s).replace('\xa0',' ')
    return re.sub(r'\s+',' ',s).strip()
def table(m):
    out=[]
    for r in re.findall(r'(?is)<tr.*?</tr>',m.group(0)):
        cells=[cell(c) for c in re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',r)]
        cells=[c for c in cells if c not in ('','$')]
        # join % and ) onto previous
        j=[]
        for c in cells:
            if c in ('%',')','%)') and j: j[-1]+=c
            else: j.append(c)
        if j: out.append(' | '.join(j))
    return '\n[TABLE]\n'+'\n'.join(out)+'\n[/TABLE]\n'
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?is)<table.*?</table>',table,s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>','\n',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    return s
def save(cik,acc,doc,name):
    url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
    raw=get(url); os.makedirs('raw',exist_ok=True); open('raw/'+name.replace('.txt','.htm'),'wb').write(raw)
    open(name,'w',encoding='utf-8').write(f'URL {url} | accession {acc}\n'+totext(raw)); print(name); time.sleep(0.3)
if __name__=='__main__':
    for f,cik,pre,yrs in [('mbuu_sub.json','1590976','MBUU',range(2017,2027)),('mcft_sub.json','1638290','MCFT',range(2019,2027))]:
        r=json.load(open(f))['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i]=='10-K' and int(r['reportDate'][i][:4]) in yrs:
                save(cik,r['accessionNumber'][i],r['primaryDocument'][i],f"{pre}_10K_FY{r['reportDate'][i][:4]}.txt")
