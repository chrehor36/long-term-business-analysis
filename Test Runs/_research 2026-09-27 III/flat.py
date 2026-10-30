import re,sys,glob,os
def flat(p):
    s=open(p,encoding='utf-8').read().replace('\u200b','').replace('\xa0',' ')
    s=re.sub(r'\n\s*\|',' |',s)          # continuation lines starting with |
    s=re.sub(r'\|\s*\n(?=\s*[\$\(\)\d,\.%—\-]+\s*(\||\n))',' | ',s)
    s=re.sub(r'[ \t]*\|[ \t]*(\|[ \t]*)+','| ',s)   # collapse empty cells
    s=re.sub(r'\| \$\s*\|','| $',s)
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return s
os.makedirs('flat',exist_ok=True)
for p in glob.glob('filings/*.txt'):
    if 'index' in p: continue
    o='flat/'+os.path.basename(p)
    if not os.path.exists(o): open(o,'w',encoding='utf-8').write(flat(p))
