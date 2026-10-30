import sys
from fetch import get
from fetchdocs import totext
acc, doc, name = sys.argv[1], sys.argv[2], sys.argv[3]
url=f"https://www.sec.gov/Archives/edgar/data/1821825/{acc.replace('-','')}/{doc}"
get(url, "raw_"+name+".htm")
open(name+".txt","w",encoding="utf-8").write(totext(open("raw_"+name+".htm","rb").read()))
print("ok", name)
