import sys
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\tools')
import sources
C={"BKNG":"0001075531","EXPE":"0001324424","TCOM":"0001269238"}
qs=[("Airbnb",None),("Airbnb","10-K"),("Airbnb","20-F"),("in addition to listing on",None),("multiple platforms",None),("multi-list",None),("cross-list",None),("list on multiple",None),("supplier direct",None),("alternative accommodations",None),("homestay",None)]
for t,c in C.items():
    for ph,f in qs:
        try:
            r=sources.fts_count(ph, cik=c, forms=f)
            print(t, repr(ph), f, r)
        except Exception as e:
            print(t, repr(ph), f, "ERROR", type(e).__name__, e)
