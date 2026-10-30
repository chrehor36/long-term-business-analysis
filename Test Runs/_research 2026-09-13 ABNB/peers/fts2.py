import sys, time
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\tools')
import sources
for t,c,ph,f in [("BKNG","0001075531","Airbnb","10-K"),("TCOM","0001269238","Airbnb","20-F"),("TCOM","0001269238","in addition to listing on",None),("TCOM","0001269238","multiple platforms",None)]:
    for i in range(3):
        try:
            print(t, repr(ph), f, sources.fts_count(ph, cik=c, forms=f)); break
        except Exception as e:
            print(t, repr(ph), f, "ERROR attempt", i+1, e); time.sleep(3)
