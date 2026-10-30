import re,html,sys
s=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
s=re.sub(r'</(tr|p|div|li|h\d)>','\n',s)
s=re.sub(r'</t[dh]>',' | ',s)
t=re.sub(r'<[^>]+>',' ',s); t=html.unescape(re.sub(r'[ \t\r]+',' ',t)); t=re.sub(r'\n\s*\n+','\n',t)
sys.stdout.reconfigure(encoding='utf-8')
print(t)
