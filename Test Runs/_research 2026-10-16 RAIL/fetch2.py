import sys
sys.path.insert(0, ".")
from fetch import fetch
for arg in sys.argv[1:]:
    cik, acc, doc, name = arg.split(",")
    fetch(f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}", name)
