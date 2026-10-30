import os,re,io,json
D=os.path.dirname(os.path.abspath(__file__))
QS=['q1fy22','q2fy22','q3fy22','q4fy22','q1fy23','q2fy23','q3fy23','q4fy23','q1fy24','q2fy24',
'q3fy24','q4fy24','q1fy25','q2fy25','q3fy25','q4fy25','q1fy26','q2fy26','q3fy26','q4fy26','q1fy27','q2fy27']
PATS={
 'global_ad':[r'Global advertising business\s*\d?\s*(?:grew|up|reached)[^.\n]{0,120}'],
 'wmt_connect':[r'Walmart Connect[^.\n]{0,120}', r'Walmart U\.S\. advertising up[^.\n]{0,60}',
                r'advertising[^.\n]{0,30}Walmart U\.S\.[^.\n]{0,60}'],
 'membership':[r'[Mm]embership (?:fee revenue|income|and other income)[^.\n]{0,140}'],
 'ecom_global':[r'(?:Global e[Cc]ommerce sales grew|e[Cc]ommerce sales up)\s*\d+%[^.\n]{0,110}'],
 'ecom_wmtus':[r'(?:Growth in e[Cc]ommerce(?: sales)? of|e[Cc]ommerce sales (?:up|increased|grew|accelerated with))[^.\n]{0,120}'],
 'cons_oi':[r'(?:Consolidated )?[Oo]perating income (?:up|grow(?:ing|th)|increased|decreased|declin)[^.\n]{0,150}'],
}
o=io.open(os.path.join(D,'metrics.txt'),'w',encoding='utf-8')
for q in QS:
    txt=open(os.path.join(D,f"8k-{q}-ex991.txt"),encoding='utf-8',errors='replace').read()
    head=re.sub(r'\s+',' ','\n'.join(txt.split('\n')[:150]))
    o.write('\n===== '+q+'\n')
    for k,ps in PATS.items():
        hits=[]
        for p in ps:
            for m in re.finditer(p, head):
                s=m.group(0).strip()
                if s not in hits: hits.append(s)
        o.write(f"  {k}:\n")
        for h in hits[:5]: o.write('     * '+h[:230]+'\n')
o.close(); print('ok')
