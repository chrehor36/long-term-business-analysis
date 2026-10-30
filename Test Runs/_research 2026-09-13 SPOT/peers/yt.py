import sys, io, urllib.request, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from edgar import strip_html
u = 'https://blog.youtube/inside-youtube/20-years-125-million-subscribers-lyor-cohen/'
req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 BRK research chrehor36@gmail.com'})
h = urllib.request.urlopen(req, timeout=60).read().decode('utf-8','replace')
t = strip_html(h)
open('YT_blog_2025-03-05_125m.txt','w',encoding='utf-8').write(t)
for m in re.finditer(r'125 million', t):
    print(t[max(0,m.start()-300):m.start()+200].replace('\n',' | '))
    print('----')
