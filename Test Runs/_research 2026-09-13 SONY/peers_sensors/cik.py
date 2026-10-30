import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
for t in ["ON","STM","SSNLF","SMSN"]:
    print(t, sources.cik_for(t))
