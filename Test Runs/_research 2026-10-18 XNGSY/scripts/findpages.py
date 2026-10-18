# Print 1-based page numbers whose text contains all given phrases.
import sys, warnings
warnings.filterwarnings("ignore")
import fitz
d = fitz.open(sys.argv[1])
for i in range(d.page_count):
    t = " ".join(d[i].get_text().split())
    if all(k.lower() in t.lower() for k in sys.argv[2:]): print(i + 1)
