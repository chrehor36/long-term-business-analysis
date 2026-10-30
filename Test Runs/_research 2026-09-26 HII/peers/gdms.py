import re,glob,json
res={}
for fn in sorted(glob.glob('GD_10K_FY*.txt')):
    t=open(fn,encoding='utf-8').read()
    flat=re.sub(r'[|$\n]',' ',t); flat=re.sub(r'\s+',' ',flat)
    m=re.search(r'MARINE SYSTEMS.{0,60}?Year Ended December 31 (\d{4}) (\d{4}).{0,30}?Revenues? ([\d,]+) ([\d,]+).{0,40}?Operating earnings ([\d,]+) ([\d,]+)',flat,re.I)
    if m:
        y1,y2,r1,r2,o1,o2=m.groups()
        for y,r,o in ((y1,r1,o1),(y2,r2,o2)):
            res[int(y)]=(float(r.replace(',','')),float(o.replace(',','')))
        print(fn,m.groups())
json.dump(res,open('gdms.json','w'))
for y in sorted(res): print(y,res[y],round(100*res[y][1]/res[y][0],1))
