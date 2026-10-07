import sys, os, re, json, urllib.request, html
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
CIK='886206'
def get(url, binary=False):
    return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=90).read()
def idx(acc):
    a=acc.replace('-','')
    return f'https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/'
def filing_index(acc):
    u=idx(acc)+acc+'-index.htm'
    return get(u).decode('utf-8','replace')
def strip(h):
    h=re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>',' ',h)
    h=re.sub(r'(?i)<br[^>]*>','\n',h)
    h=re.sub(r'(?i)</(p|div|tr|h\d|li|table)>','\n',h)
    h=re.sub(r'(?i)</t[dh]>',' | ',h)
    h=re.sub(r'(?s)<[^>]+>',' ',h)
    h=html.unescape(h)
    h=re.sub(r'[ \t\xa0]+',' ',h)
    h=re.sub(r'\n\s*\n+','\n',h)
    return h
def doc(acc, name, out):
    if os.path.exists(out): print('have',out); return
    raw=get(idx(acc)+name).decode('utf-8','replace')
    open(out+'.raw.html','w',encoding='utf-8').write(raw)
    open(out,'w',encoding='utf-8').write(strip(raw))
    print('wrote',out,len(raw))
if __name__=='__main__':
    print(filing_index(sys.argv[1])[:0])
