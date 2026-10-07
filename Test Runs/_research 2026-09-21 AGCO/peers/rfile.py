import urllib.request,re,html,sys
UA={'User-Agent':'chrehor36@gmail.com research'}
def g(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read().decode('utf-8','ignore')
def reports(base, pat):
    x=g(base+"FilingSummary.xml")
    for m in re.finditer(r'(?s)<Report[^>]*>(.*?)</Report>', x):
        b=m.group(1)
        sn=re.search(r'<ShortName>(.*?)</ShortName>',b); fn=re.search(r'<HtmlFileName>(.*?)</HtmlFileName>',b)
        if sn and fn and re.search(pat, sn.group(1), re.I): print(fn.group(1),'|',sn.group(1))
def table(u, maxrows=60):
    s=g(u); s=re.sub(r'(?s)<(script|style).*?</\1>','',s)
    n=0
    for r in re.findall(r'(?s)<tr[^>]*>(.*?)</tr>',s):
        cells=[html.unescape(re.sub(r'<[^>]+>','',c)).strip() for c in re.findall(r'(?s)<t[dh][^>]*>(.*?)</t[dh]>',r)]
        cells=[c for c in cells if c not in ('','$',')')]
        if cells:
            line=' :: '.join(cells)[:200]
            if line.startswith('X') or line.startswith('- Definition') or line.startswith('Namespace'): break
            print(line); n+=1
            if n>maxrows: break
if __name__=='__main__':
    if sys.argv[1]=='ls': reports(sys.argv[2], sys.argv[3])
    else: table(sys.argv[2], int(sys.argv[3]) if len(sys.argv)>3 else 60)
