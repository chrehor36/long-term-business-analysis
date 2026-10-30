import json, re, html, os
from fetch import get
docs = {
 "10K_FY2025": ("0001628280-26-011125","ogn-20251231.htm"),
 "10K_FY2024": ("0001821825-25-000006","ogn-20241231.htm"),
 "10K_FY2023": ("0001628280-24-006733","ogn-20231231.htm"),
 "10K_FY2022": ("0001821825-23-000003","ogn-20221231.htm"),
 "10K_FY2021": ("0001821825-22-000002","ogn-20211231.htm"),
 "10Q_2026Q2": ("0001628280-26-051230","ogn-20260630.htm"),
 "DEF14A_2026": ("0001193125-26-177411","ogn-20260423.htm"),
 "Form10_A2": ("0001193125-21-140380","d56612d1012ba.htm"),
 "8K_20251027": ("0001104659-25-102324","tm2529513d1_8k.htm"),
 "8K_20260427": ("0001193125-26-178718","d38652d8k.htm"),
 "8K_20260717": ("0001193125-26-307767","d88294d8k.htm"),
 "8K_20260220": ("0001104659-26-017870","tm266880d1_8k.htm"),
 "8K_20260731": ("0001104659-26-089008","tm2621744d1_8k.htm"),
 "8K_20250415": ("0001104659-25-035173","tm2512324d1_8k.htm"),
 "8K_20251107": ("0001104659-25-108130","tm2530470d1_8k.htm"),
 "8K_20250527": ("0001104659-25-052994","tm2516205d1_8k.htm"),
 "8K_20241223": ("0001104659-24-130976","tm2431756d1_8k.htm"),
 "8K_20240923": ("0001104659-24-102053","tm2424316d1_8k.htm"),
}
def totext(raw):
    s = raw.decode("utf-8", "ignore")
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", s)
    s = re.sub(r"(?i)</td>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s
def main():
  for k,(acc,doc) in docs.items():
      url = f"https://www.sec.gov/Archives/edgar/data/1821825/{acc.replace('-','')}/{doc}"
      raw = f"raw_{k}.htm"
      try:
          get(url, raw)
          open(f"{k}.txt","w",encoding="utf-8").write(totext(open(raw,"rb").read()))
          print(k, os.path.getsize(f"{k}.txt"))
      except Exception as e:
          print("FAIL", k, e)
if __name__=="__main__": main()
