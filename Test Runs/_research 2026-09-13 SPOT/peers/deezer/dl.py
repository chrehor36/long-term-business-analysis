import sys, io, urllib.request, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) BRK research chrehor36@gmail.com'}
U = {'DZR_URD_2025_EN.pdf':'https://www.deezer-investors.com/wp-content/uploads/2026/04/DZR2025_URD_EN_PDF_MEL_26_04_29.pdf',
     'DZR_URD_2023_EN.pdf':'https://www.deezer-investors.com/wp-content/uploads/2024/04/DZR2023_DEEZER_URD_EN_2024_04_30pdf.pdf',
     'DZR_URD_2022_EN.pdf':'https://www.deezer-investors.com/wp-content/uploads/2023/04/DZR2022_DEEZER_URD_EN_MEL_230428.pdf'}
for fn,u in U.items():
    if not os.path.exists(fn):
        d = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=180).read()
        open(fn,'wb').write(d)
    print(fn, os.path.getsize(fn))
try:
    import fitz
    for fn in U:
        doc = fitz.open(fn); out=[]
        for i,p in enumerate(doc):
            out.append(f'\n=== pdf page {i+1}\n'); out.append(p.get_text())
        open(fn.replace('.pdf','.txt'),'w',encoding='utf-8').write(''.join(out)); print(fn, len(doc), 'pages')
except ImportError:
    print('no fitz')
