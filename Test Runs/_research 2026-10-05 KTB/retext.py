import sys
from fetch import text
for raw in sys.argv[1:]:
    open(raw.replace('.raw.html',''),'w',encoding='utf-8').write(text(open(raw,'rb').read()))
