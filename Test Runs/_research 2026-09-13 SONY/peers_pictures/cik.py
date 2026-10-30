import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
for t in ["WBD","DIS","LION","LGF-A","LGF.A","STRZ","PARA","PSKY","CMCSA","SONY"]:
    print(t, sources.cik_for(t))
