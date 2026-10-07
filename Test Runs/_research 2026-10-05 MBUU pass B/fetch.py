import json, sys, time, re, html, urllib.request
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def get(url):
    for k in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60).read()
        except Exception as e:
            print('retry',url,e); time.sleep(2)
    raise SystemExit('fail '+url)
def totext(b):
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',s)
    s=re.sub(r'(?i)</td>|</th>',' | ',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    return s
def save(cik,acc,doc,name):
    url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
    t=totext(get(url))
    open(name,'w',encoding='utf-8').write(f'URL {url} | accession {acc}\n'+t)
    print(name,len(t)); time.sleep(0.3)
if __name__=='__main__':
    for f,cik,pre,yrs in [('mbuu_sub.json','1590976','MBUU',range(2017,2027)),('mcft_sub.json','1638290','MCFT',range(2019,2027))]:
        r=json.load(open(f))['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i]=='10-K' and int(r['reportDate'][i][:4]) in yrs:
                save(cik,r['accessionNumber'][i],r['primaryDocument'][i],f"{pre}_10K_FY{r['reportDate'][i][:4]}.txt")
