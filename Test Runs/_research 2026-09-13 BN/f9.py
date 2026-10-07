import urllib.request, os, sys
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
base="https://www.sec.gov/Archives/edgar/data/1001085/000100108526000011/"
for p in sys.argv[1:]:
    fn=f"a_bnar2025narrativexpage{p}a.jpg" if p!="1" else "a_bnar2025narrativexpagea.jpg"
    out=os.path.join("ar_img",fn)
    if not os.path.exists(out):
        open(out,"wb").write(urllib.request.urlopen(urllib.request.Request(base+fn,headers=UA),timeout=120).read())
    print(out)
