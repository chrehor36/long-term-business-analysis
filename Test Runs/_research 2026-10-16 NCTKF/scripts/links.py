import re,sys,html,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
for fn in sys.argv[1:]:
    t=open(fn,encoding='utf-8').read()
    for m in re.finditer(r'<a[^>]+href="([^"]+\.pdf)"[^>]*>(.*?)</a>',t,re.S):
        txt=re.sub(r'<[^>]+>',' ',m.group(2)); txt=html.unescape(' '.join(txt.split()))
        print(fn.split('/')[-1], '|', txt[:140], '|', m.group(1))
