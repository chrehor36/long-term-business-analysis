import sys, json, subprocess, os
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 ABNB')
from fetch import get
H2T = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-13 ABNB\h2t.py'
cik=sys.argv[1]; tag=sys.argv[2]
for acc in sys.argv[3:]:
    a=acc.replace('-','')
    j=json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/index.json"))
    names=[x['name'] for x in j['directory']['item']]
    ex=[n for n in names if ('99' in n.lower() or 'ex99' in n.lower()) and n.endswith('.htm')]
    print(acc, names)
    for n in ex[:1]:
        out=f"8K_{tag}_{acc}"
        get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{a}/{n}", out+".htm")
        subprocess.run([sys.executable,H2T,out+".htm",out+".txt"]); os.remove(out+".htm")
