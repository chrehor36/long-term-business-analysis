import sys, os, re, json
sys.path.insert(0,'tools')
import sources as S
R='Test Runs/_research 2026-09-21 SGC/'
def idx(acc):
    a=acc.replace('-','')
    url=f"https://www.sec.gov/Archives/edgar/data/95574/{a}/"
    return url
def get(acc, doc, out):
    url=idx(acc)+doc
    t=S._get(url, headers=S.SEC_UA, cache_name=f"sgc_{out}", max_age_h=240)
    open(R+out,'w',encoding='utf-8',errors='replace').write(t)
    print(out, len(t))
    return t
def getidx(acc):
    a=acc.replace('-','')
    url=f"https://www.sec.gov/Archives/edgar/data/95574/{a}/index.json"
    t=S._get(url, headers=S.SEC_UA, cache_name=f"sgcidx_{a}.json", max_age_h=240)
    return json.loads(t)
if __name__=='__main__':
    pass
