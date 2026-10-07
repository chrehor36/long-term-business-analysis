import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pf
for tk in ["AMR","HCC","METC","BTU","ARLP"]:
    cik, name, out = pf.listing(tk)
    for f, fd, rd, acc, doc in out:
        want = f.startswith("10-K") or (f == "10-Q" and rd == "2026-06-30")
        if not want: continue
        try:
            fp = pf.fetch(tk, cik, acc, doc)
            print(tk, f, fd, rd, acc, os.path.getsize(fp))
        except Exception as e:
            print("FAIL", tk, acc, e)
