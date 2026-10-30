import re,json,glob,html,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
BS=chr(92); Q=chr(39)
seen=set()
for fn in sorted(glob.glob('cache/hds/jp/j*.js'))+sorted(glob.glob('cache/hds/g*.js')):
    t=open(fn,encoding='utf-8').read()
    if 'financialData = ' in t:
        i=t.find('financialData = '); j=t.find('xjStorageChart.styleData')
        s=t[i+len('financialData = '):j].strip().rstrip(';')
        if s.startswith(BS+Q): s=s[2:]
        if s.endswith(BS+Q): s=s[:-2]
        try: d=json.loads(s)
        except Exception as e: print('fail',fn,e); continue
        cols=d.get('coltitle',{}).get('ja'); title=d['title']['ja'][0]
        rows=d.get('rowtitle',{}).get('ja')
        key=(title,str(cols))
        if key in seen: continue
        seen.add(key)
        print('##',fn,'|',title,'|cols',cols)
        for r,v in zip(rows or [],d.get('data',[])): print('   ',r,v)
    else:
        s=html.unescape(re.sub(r'<[^>]+>',' ',t.replace(BS,'')))
        s=re.sub(r'\s+',' ',s)
        print('## TABLE',fn,s[:1500])
