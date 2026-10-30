import re,glob
for f in ["424B4_IPO.txt","10K_FY2021.txt","10K_FY2022.txt","10K_FY2023.txt","10K_FY2024.txt","10K_FY2025.txt","10Q_2025Q2.txt","10Q_2026Q1.txt","10Q_2026Q2.txt"]:
    s=open(f,encoding="utf-8").read()
    s=re.sub(r"[\s|]+"," ",s)
    i=s.find("Key Operating and Financial Metrics We regularly")
    if i<0: i=s.find("Key Operating and Financial Metrics")
    print("==",f, s[i:i+700])
    for m in re.finditer(r"(auction marketplace revenue|Auction marketplace revenue|other marketplace revenue|data services revenue|Data services revenue)[^.]{0,250}", s):
        print("   ~", m.group(0)[:260])
