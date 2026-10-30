import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fetch_core import get
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
c = collections.Counter(); yrs = collections.defaultdict(set)
for frm in range(0, 200, 100):
    j = json.loads(get(f'https://efts.sec.gov/LATEST/search-index?q=%22PubMatic%22&forms=10-K&from={frm}'))
    for h in j["hits"]["hits"]:
        n = h["_source"]["display_names"][0]; c[n] += 1; yrs[n].add(h["_source"]["file_date"][:4])
out = open(os.path.join(H,"fts_out.txt"),"w",encoding="utf-8")
for n, k in c.most_common():
    s = f"{k:3d} {n} {sorted(yrs[n])}"; print(s); out.write(s+"\n")
