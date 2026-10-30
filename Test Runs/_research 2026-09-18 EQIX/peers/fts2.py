import sys, time, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
out=[]
for name,c in [("DLR","0001297996"),("AMT","0001053507"),("IRM","0001020569"),("CYXT","0001794905"),("CONE","0001553023"),("SWCH","0001710583"),("COR","0001490892"),("QTS","0001577368")]:
    n,u=sources.fts_count("Equinix",cik=c,forms="10-K"); out.append(("Equinix",name,"10-K",n,u)); print("Equinix in",name,"10-K:",n); time.sleep(0.4)
for ph in ["Digital Realty","CoreSite","Iron Mountain","NTT","American Tower","hyperscale"]:
    n,u=sources.fts_count(ph,cik="0001101239",forms="10-K"); out.append((ph,"EQIX","10-K",n,u)); print(ph,"in EQIX 10-K:",n); time.sleep(0.4)
json.dump(out,open("FTS_queries_naming.json","w"),indent=1)
