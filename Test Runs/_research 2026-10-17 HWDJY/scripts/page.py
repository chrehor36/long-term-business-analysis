import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
f = sys.argv[1]; nums = [int(x) for x in sys.argv[2].split(',')]
pages = open(f, encoding='utf-8', errors='replace').read().split('\f')
for n in nums:
    print(f"===== page {n} =====")
    print("\n".join(l for l in pages[n-1].splitlines() if l.strip()))
