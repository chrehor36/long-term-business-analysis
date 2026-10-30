import urllib.request, re, html, os, time
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
docs = [
 ("ON_10K_FY2025", "1097864", "0001097864-26-000006", "on-20251231.htm"),
 ("ON_10K_FY2024", "1097864", "0001628280-25-004557", "on-20241231.htm"),
 ("ON_10K_FY2023", "1097864", "0001628280-24-003201", "on-20231231.htm"),
 ("STM_20F_FY2025", "932787", "0000932787-26-000009", "stm-20251231.htm"),
 ("STM_20F_FY2024", "932787", "0000932787-25-000006", "stm-20241231.htm"),
 ("STM_20F_FY2023", "932787", "0001628280-24-006353", "stm-20231231.htm"),
]
def totext(h):
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h)
    h = re.sub(r"(?is)<ix:header>.*?</ix:header>", " ", h)
    h = re.sub(r"(?i)</(p|div|tr|li|h\d|table)>", "\n", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    h = re.sub(r"<[^>]+>", " ", h)
    h = html.unescape(h).replace("\xa0", " ")
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in h.split("\n")]
    return "\n".join(l for l in lines if l and l.strip("| "))
for name, cik, acc, doc in docs:
    if os.path.exists(name + ".txt"): continue
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read().decode("utf-8","replace")
    open(name + ".txt", "w", encoding="utf-8").write("SOURCE: " + url + "\nACCESSION: " + acc + "\n" + totext(raw))
    print(name, len(raw)); time.sleep(0.5)
