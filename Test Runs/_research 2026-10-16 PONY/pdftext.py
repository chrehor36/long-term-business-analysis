import sys, pypdf
r = pypdf.PdfReader(sys.argv[1]); t = '\n'.join((p.extract_text() or '') for p in r.pages)
open(sys.argv[2], 'w', encoding='utf-8').write(t); print(len(r.pages), len(t))
