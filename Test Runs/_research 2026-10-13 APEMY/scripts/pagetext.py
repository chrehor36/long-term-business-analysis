import re,sys,html
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',t)
    m=re.search(r'(?s)<main.*?</main>',t)
    body=m.group(0) if m else t
    body=re.split(r'Newsletter Newsletter',body)[0]
    links=re.findall(r'href="([^"]+\.(?:pdf|xlsx)[^"]*)"',body)
    txt=html.unescape(re.sub(r'<[^>]+>',' ',body)); txt=re.sub(r'\s+',' ',txt)
    txt=txt.split('Newsletter Newsletter')[0]
    print('=====',f); print(txt[:6000]); print('LINKS',links[:80])
