"""List R page titles in a filing folder matching a regex. Usage: python -I rfind.py folder regex"""
import sys, re, os, glob

folder, pat = sys.argv[1], sys.argv[2]
for p in sorted(glob.glob(os.path.join(folder, "R*.htm")), key=lambda x: int(re.findall(r"R(\d+)", os.path.basename(x))[0])):
    s = open(p, "rb").read().decode("utf-8", "ignore")
    m = re.search(r'<th[^>]*class="tl"[^>]*>(.*?)</th>', s, re.S)
    t = re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip() if m else ""
    if re.search(pat, t, re.I):
        print(os.path.basename(p), t[:140])
