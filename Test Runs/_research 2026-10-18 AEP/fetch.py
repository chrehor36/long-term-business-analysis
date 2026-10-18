"""Fetch SEC EDGAR documents for the AEP run into cache/ (gitignored). Usage: python -I fetch.py URL OUTNAME"""
import sys, urllib.request, gzip, os, time
H={'User-Agent':'Chris Hrehor chrehor36@gmail.com','Accept-Encoding':'gzip, deflate'}
here=os.path.dirname(os.path.abspath(__file__))
def get(url):
    for i in range(5):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=H),timeout=60)
            b=r.read()
            if r.headers.get('Content-Encoding')=='gzip': b=gzip.decompress(b)
            return b
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(2+i*2)
    raise SystemExit('failed '+url)
b=get(sys.argv[1])
out=os.path.join(here,'cache',sys.argv[2])
open(out,'wb').write(b)
print(out,len(b))
