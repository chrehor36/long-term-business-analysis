# converts a filing's HTML to plain text for reading (no figures added)
import re,html,sys
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='replace').read()
    t=re.sub(r'(?is)<(script|style).*?</\1>',' ',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>','\n',t)
    t=re.sub(r'(?i)</td>',' | ',t)
    t=re.sub(r'<[^>]+>',' ',t)
    t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n',t)
    open(f.replace('.htm','.txt'),'w',encoding='utf-8').write(t)
    print(f,len(t))
