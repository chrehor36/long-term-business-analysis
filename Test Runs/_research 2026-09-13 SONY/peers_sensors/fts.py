import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
for phrase, cik, forms in [("Sony", "0000932787", "20-F"), ("image sensor", "0000932787", "20-F"), ("Sony Semiconductor", "0001097864", "10-K"), ("image sensors", "0001097864", "10-K")]:
    try:
        print(phrase, cik, forms, sources.fts_count(phrase, cik=cik, forms=forms))
    except Exception as e:
        print(phrase, cik, "ERR", e)
