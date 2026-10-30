import urllib.request, os, json, time, re, html
UA = {"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
OUT = "C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/_research 2026-09-12 ACVA/"
CIK = "1637873"
def get(u):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        except Exception as e: print("retry", i, u, e); time.sleep(3)
    raise SystemExit("failed "+u)
def totext(b):
    t = b.decode("utf-8", "ignore")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"(?i)</td>", " | ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t
def index(acc):
    a = acc.replace("-","")
    j = json.loads(get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/index.json")); time.sleep(0.3)
    return [x["name"] for x in j["directory"]["item"]]
def doc(acc, name, out):
    p = OUT+out
    if os.path.exists(p.replace(".htm",".txt")): print("have", out); return
    a = acc.replace("-","")
    b = get(f"https://www.sec.gov/Archives/edgar/data/{CIK}/{a}/{name}")
    open(p.replace(".htm",".txt").replace(".html",".txt"),"w",encoding="utf-8").write(totext(b)); print(out, len(b)); time.sleep(0.35)
primary = [
 ("0001637873-26-000011","acva-20251231.htm","10K_FY2025.htm"),
 ("0001628280-25-006439","acva-20241231.htm","10K_FY2024.htm"),
 ("0000950170-24-018066","acva-20231231.htm","10K_FY2023.htm"),
 ("0000950170-23-005445","acva-20221231.htm","10K_FY2022.htm"),
 ("0000950170-22-001792","acva-20211231.htm","10K_FY2021.htm"),
 ("0001637873-26-000034","acva-20260630.htm","10Q_2026Q2.htm"),
 ("0001637873-26-000020","acva-20260331.htm","10Q_2026Q1.htm"),
 ("0001637873-25-000011","acva-20250630.htm","10Q_2025Q2.htm"),
 ("0001193125-26-158987","d27393ddef14a.htm","DEF14A_2026.htm"),
 ("0001193125-25-084378","d599558ddef14a.htm","DEF14A_2025.htm"),
 ("0001193125-21-092803","d34258d424b4.htm","424B4_IPO.htm"),
]
for a,n,o in primary: doc(a,n,o)
eightks = {
 "0000950103-26-013780":"8K_20260910_101",
 "0001637873-26-000023":"8K_20260512_101",
 "0001637873-25-000025":"8K_20251212_101",
 "0001637873-25-000005":"8K_20250626_101",
 "0001628280-24-030155":"8K_20240620_101",
 "0001637873-26-000031":"8K_20260806_Q2",
 "0001637873-26-000019":"8K_20260506_Q1",
 "0001637873-26-000010":"8K_20260223_Q4",
 "0001637873-25-000019":"8K_20251105_Q3",
 "0001628280-25-006357":"8K_20250219_Q4",
 "0000950170-24-017935":"8K_20240221_Q4",
 "0000950170-23-003752":"8K_20230222_Q4",
 "0000950170-22-001351":"8K_20220216_Q4",
 "0000950103-25-011517":"8K_20250910_701",
 "0001193125-22-010659":"8K_20220118_701",
}
for acc, tag in eightks.items():
    names = index(acc); print(tag, names)
    for n in names:
        if re.search(r"\.(htm|html)$", n) and "index" not in n:
            doc(acc, n, f"{tag}__{n}")
