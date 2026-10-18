# fetch an EDGAR document and strip to text; usage: fetch.py accession primarydoc outname
import sys, urllib.request, re, html, os
cik="1991261"
acc, doc, out = sys.argv[1], sys.argv[2], sys.argv[3]
url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
req=urllib.request.Request(url, headers={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"})
raw=urllib.request.urlopen(req).read().decode('utf-8','replace')
os.makedirs('cache',exist_ok=True)
open(os.path.join('cache',out+'.htm'),'w',encoding='utf-8').write(raw)
t=re.sub(r'(?is)<(script|style).*?</\1>','',raw)
t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
t=re.sub(r'(?i)</td>',' | ',t)
t=re.sub(r'<[^>]+>','',t)
t=html.unescape(t).replace('\xa0',' ')
t=re.sub(r'[ \t]+',' ',t)
t=re.sub(r'\n\s*\n+','\n',t)
open(os.path.join('cache',out+'.txt'),'w',encoding='utf-8').write(t)
print(out, len(t))
