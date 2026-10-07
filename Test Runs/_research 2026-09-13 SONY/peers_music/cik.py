import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
for t in ["WMG","RSVR","UMGNF","SONY"]:
    print(t, sources.cik_for(t))
