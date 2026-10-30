import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
print(sources.fts_count("unpredictable and volatile", cik="0001437107", forms="10-K"))
print(sources.fts_count("difficult to predict", cik="0002052959", forms="10-K"))
