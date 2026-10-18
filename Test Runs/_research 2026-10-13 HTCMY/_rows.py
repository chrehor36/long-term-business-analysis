import sys, warnings; warnings.filterwarnings("ignore"); import fitz as pymupdf
# Rebuild text rows by y coordinate: usage _rows.py file.pdf firstpage lastpage (1-based pdf page index)
doc = pymupdf.open(sys.argv[1])
for pno in range(int(sys.argv[2])-1, int(sys.argv[3])):
    page = doc[pno]
    words = page.get_text("words")
    rows = {}
    for x0,y0,x1,y1,w,*_ in words:
        key = round((y0+y1)/2/3)
        rows.setdefault(key, []).append((x0,w))
    print(f"=== pdf page {pno+1}")
    for k in sorted(rows):
        ws = sorted(rows[k])
        line=""; lastx=0
        for x,w in ws:
            gap = int((x-lastx)/5) if lastx else int(x/5)
            line += (" "*max(1,gap) if line else " "*gap) + w
            lastx = x + len(w)*5
        print(line.rstrip())
