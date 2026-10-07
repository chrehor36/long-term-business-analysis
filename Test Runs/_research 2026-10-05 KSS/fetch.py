import sys, json, time, re, os, urllib.request
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'identity'}
NL = chr(10)
def get(url):
    req=urllib.request.Request(url,headers=UA)
    for i in range(4):
        try:
            with urllib.request.urlopen(req,timeout=60) as r: return r.read()
        except Exception as e:
            print('retry',url,e,file=sys.stderr); time.sleep(2)
    raise SystemExit('fail '+url)
def sub(cik):
    return json.loads(get(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json'))
def html2txt(b):
    import html as H
    s=b.decode('utf-8','ignore')
    s=re.sub(r'(?is)<(script|style).*?</\1>','',s)
    s=re.sub(r'(?is)<ix:header>.*?</ix:header>','',s)
    def tab(m):
        t=m.group(0)
        t=re.sub(r'(?i)</tr>','@@NL@@',t)
        t=re.sub(r'(?i)</td>|</th>',' |',t)
        t=re.sub(r'<[^>]+>',' ',t)
        t=re.sub(r'\s+',' ',t)
        return NL+t.replace('@@NL@@',NL)+NL
    s=re.sub(r'(?is)<table.*?</table>',tab,s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</h\d>',NL,s)
    s=re.sub(r'<[^>]+>','',s)
    s=H.unescape(s).replace(chr(160),' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'(\| ?)+\|','|',s)
    s=re.sub(r'\$ \| ?','$',s)
    s=re.sub(r'\n\s*\n+',NL,s)
    return s
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='list':
        cik=sys.argv[2]; forms=sys.argv[3].split(',')
        d=sub(cik); r=d['filings']['recent']
        for i in range(len(r['form'])):
            if r['form'][i] in forms:
                print(r['form'][i],r['filingDate'][i],r['accessionNumber'][i],r['primaryDocument'][i],r['reportDate'][i])
        for f in d['filings'].get('files',[]):
            print('OLDER',f['name'])
    elif cmd=='older':
        d=json.loads(get('https://data.sec.gov/submissions/'+sys.argv[2])); forms=sys.argv[3].split(',')
        for i in range(len(d['form'])):
            if d['form'][i] in forms:
                print(d['form'][i],d['filingDate'][i],d['accessionNumber'][i],d['primaryDocument'][i],d['reportDate'][i])
    elif cmd=='doc':
        cik,acc,doc,out=sys.argv[2:6]
        url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
        b=get(url); open(out,'w',encoding='utf-8').write(html2txt(b)); print(out,len(b))
    elif cmd=='raw':
        cik,acc,doc,out=sys.argv[2:6]
        url=f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}'
        b=get(url); open(out,'wb').write(b); print(out,len(b))
    elif cmd=='facts':
        cik,out=sys.argv[2:4]
        b=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json'); open(out,'wb').write(b); print(out,len(b))
    elif cmd=='index':
        cik,acc=sys.argv[2:4]
        b=get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/')
        for m in re.findall(r'href="([^"]+)"',b.decode()):
            if acc.replace('-','') in m: print(m)
