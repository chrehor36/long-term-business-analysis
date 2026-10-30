import re,html,sys,os,glob
src=sys.argv[1]; dst=sys.argv[2]; os.makedirs(dst,exist_ok=True)
def clean(s):
  s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s).replace('\xa0',' '); return re.sub(r'\s+',' ',s).strip()
def row(m):
  cells=re.findall(r'(?is)<t[dh][^>]*>(.*?)</t[dh]>',m.group(0))
  cs=[clean(c) for c in cells]; cs=[c for c in cs if c not in('','$',')','%')]
  return '\n'+' | '.join(cs)+'\n'
for p in glob.glob(os.path.join(src,'*.htm')):
  t=open(p,encoding='utf-8',errors='replace').read()
  t=re.sub(r'(?is)<(script|style|ix:header).*?</\1>','',t)
  t=re.sub(r'(?is)<tr[^>]*>.*?</tr>',row,t)
  t=re.sub(r'(?i)</(p|div|li|h\d)>|<br\s*/?>','\n',t)
  t=re.sub(r'<[^>]+>','',t); t=html.unescape(t).replace('\xa0',' ')
  t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
  open(os.path.join(dst,os.path.basename(p)[:-4]+'.txt'),'w',encoding='utf-8').write(t)
