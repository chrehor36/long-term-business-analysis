import json,urllib.request,sys,time,os,re,gzip,io
H={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url,headers=H))
    d=r.read()
    if r.headers.get('Content-Encoding')=='gzip':
        d=gzip.decompress(d)
    return d
def idx(cik,acc):
    a=acc.replace('-','')
    return json.loads(get(f'https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json'))
def strip(h):
    h=h.decode('utf-8','ignore')
    h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h)
    h=re.sub(r'(?is)<br\s*/?>','\n',h)
    h=re.sub(r'(?is)</(p|div|tr|h[1-6]|li)>','\n',h)
    h=re.sub(r'(?is)</t[dh]>',' | ',h)
    h=re.sub(r'(?s)<[^>]+>',' ',h)
    import html as H2
    h=H2.unescape(h)
    h=re.sub(r'[ \t\xa0]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
