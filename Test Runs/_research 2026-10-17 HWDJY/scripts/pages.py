import sys, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
# usage: pages.py file.txt "regex" [maxpages] [width]
f, pat = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 3
w = int(sys.argv[4]) if len(sys.argv) > 4 else 400
pages = open(f, encoding='utf-8', errors='replace').read().split('\f')
n = 0
for i, p in enumerate(pages):
    if re.search(pat, p):
        print(f"===== page {i+1} =====")
        for line in p.splitlines():
            if line.strip():
                print(line[:w].rstrip())
        n += 1
        if n >= mx: break
