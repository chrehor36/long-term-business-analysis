import re,html,glob,sys,os
d=sys.argv[1]
for f in sorted(glob.glob(os.path.join(d,'*.htm'))):
    out=f[:-4]+'.txt'
    if os.path.exists(out): continue
    s=open(f,encoding='utf-8',errors='ignore').read()
    s=re.sub(r'(?is)<script.*?</script>|<style.*?</style>',' ',s)
    i=s.lower().find('<ix:header'); j=s.lower().find('</ix:header>')
    if i>=0 and j>i: s=s[:i]+s[j+12:]
    s=re.sub(r'(?i)</(p|div|tr|li|h\d|table)>','\n',s)
    s=re.sub(r'(?i)</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]*>',' ',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    open(out,'w',encoding='utf-8').write(s)
    print(f,len(s),flush=True)
