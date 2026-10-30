import json,sys,os
from datetime import date
C=os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'..','cache','comp')
def load(cik):
  d=json.load(open(os.path.join(C,f'facts_{cik}.json'),encoding='utf-8'));F={}
  for t,cs in d['facts'].items(): F.update(cs)
  return F
def dur(f):
  if 'start' not in f: return None
  return (date.fromisoformat(f['end'])-date.fromisoformat(f['start'])).days
def get(F,concepts,fy,own,inst,form='10-K',start=None,end=None):
  if isinstance(concepts,str): concepts=[concepts]
  for c in concepts:
    if c not in F: continue
    cands=[]
    for f in F[c]['units'].get('USD',[]):
      if not f['form'].startswith(form): continue
      if end:
        if f['end']!=end: continue
        if inst and 'start' in f: continue
        if not inst and f.get('start')!=start: continue
      else:
        if f['end'][:4]!=str(fy) or f['end'][5:]!='12-31': continue
        if inst:
          if 'start' in f: continue
        else:
          dd=dur(f)
          if dd is None or dd<350 or dd>380: continue
      cands.append(f)
    if not cands: continue
    o=[f for f in cands if f['accn']==own]
    f=o[0] if o else sorted(cands,key=lambda x:x['filed'])[0]
    return round(f['val']/1e6,1),f['accn'],c
  return None
ITEMS=['rev','oi','da','ocf','capex','nuc','acq','sbc','ta','gw','intang','debt','cash','eq','buyb']
LBL={'rev':'Revenue','oi':'Operating income','da':'D&A (income stmt)','ocf':'Cash from operations','capex':'Capex (CF line, as filed)','nuc':'  of which / plus nuclear fuel','acq':'Acquisitions, net of cash','sbc':'Share-based comp','ta':'Total assets','gw':'Goodwill','intang':'Intangible assets','debt':'LT debt incl. current','cash':'Cash & equivalents','eq':'Total equity','buyb':'Share repurchases'}
FLOW={'rev','oi','da','ocf','capex','nuc','acq','sbc','buyb'}
def run(cfg):
  F=load(cfg['cik']); rows={}; src={}
  for fy,own in cfg['own'].items():
    r={}
    for it in ITEMS:
      cs=cfg['map'].get(it)
      if not cs: continue
      if callable(cs): v=cs(F,fy,own)
      else: v=get(F,cs,fy,own,it not in FLOW)
      if v: r[it]=v[0]; src[(fy,it)]=v[1]
    for it,v in cfg.get('ovr',{}).get(fy,{}).items(): r[it]=v; src[(fy,it)]='text'
    rows[fy]=r
  return rows,src
def ytd(cfg,start,end):
  F=load(cfg['cik']); r={}
  for it in ITEMS:
    cs=cfg['map'].get(it)
    if not cs or callable(cs): cs=cfg.get('ytdmap',{}).get(it)
    if not cs: continue
    v=get(F,cs,None,None,it not in FLOW,form='10-Q',start=start,end=end)
    if v: r[it]=v[0]
  return r
