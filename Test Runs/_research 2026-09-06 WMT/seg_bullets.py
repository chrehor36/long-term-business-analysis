import os,re,io,json
D=os.path.dirname(os.path.abspath(__file__))
QS=['q1fy22','q2fy22','q3fy22','q4fy22','q1fy23','q2fy23','q3fy23','q4fy23','q1fy24','q2fy24',
'q3fy24','q4fy24','q1fy25','q2fy25','q3fy25','q4fy25','q1fy26','q2fy26','q3fy26','q4fy26','q1fy27','q2fy27']
HDR=re.compile(r"^(Walmart U\.?S\.?|Walmart International|International|Sam.{1,3}s Club U\.?S\.?|Sam.{1,3}s Club|Consolidated|Total Company)\s*\d?\s*$")
KEY=re.compile(r'(advertis|Walmart Connect|MAP\b|membership|eCommerce|e-commerce|operating income)', re.I)
out={}
for q in QS:
    lines=open(os.path.join(D,f"8k-{q}-ex991.txt"),encoding='utf-8',errors='replace').read().split('\n')
    cur=None; res={}
    for l in lines[:200]:
        s=re.sub(r'\s+',' ',l.strip())
        s=s.lstrip('| ').strip()
        if HDR.match(s): cur=HDR.match(s).group(1); res.setdefault(cur,[]); continue
        if cur and 20<len(s)<340 and KEY.search(s) and not s.startswith(('1 ','2 ','3 ','4 ','5 ')):
            if s not in res[cur]: res[cur].append(s)
    out[q]=res
o=io.open(os.path.join(D,'seg_bullets.txt'),'w',encoding='utf-8')
for q,res in out.items():
    o.write('\n===== '+q+'\n')
    for seg,bs in res.items():
        if not bs: continue
        o.write('  ## '+seg+'\n')
        for b in bs[:9]: o.write('     - '+b[:300]+'\n')
o.close()
json.dump(out,open(os.path.join(D,'seg_bullets.json'),'w'),indent=1)
print("ok")
