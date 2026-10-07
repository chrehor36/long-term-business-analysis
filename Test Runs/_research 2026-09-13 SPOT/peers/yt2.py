import sys, io, urllib.request, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from edgar import strip_html
u = 'https://blog.youtube/news-and-events/8-billion-youtubes-twin-engine-continues-to-fuel-the-future-of-music/'
req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 BRK research chrehor36@gmail.com'})
t = strip_html(urllib.request.urlopen(req, timeout=60).read().decode('utf-8','replace'))
open('YT_blog_8billion.txt','w',encoding='utf-8').write(t)
i = t.find('This year YouTube'); 
for pat in [r'\$8 billion', r'125 million', r'Lyor Cohen', r'20\d\d  \|']:
    for m in list(re.finditer(pat, t))[:3]:
        print(pat, '::', t[max(0,m.start()-250):m.start()+300].replace('\n',' | '))
        print('--')
