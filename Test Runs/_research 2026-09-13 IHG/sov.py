import sys, os, urllib.request, json
sys.path.insert(0, os.path.join("..", "..", "tools"))
import sources as S
print("USD", S.sovereign("USD"))
print("EUR", S.sovereign("EUR"))
UA = {"User-Agent": "Mozilla/5.0"}
base = "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Aug/2026&Dateto=13/Sep/2026&SeriesCodes={}&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N"
for code in ("IUDLNPY", "XUDLUSS", "IUDMNPY"):
    try:
        raw = urllib.request.urlopen(urllib.request.Request(base.format(code), headers=UA), timeout=45).read().decode("utf-8", "replace")
        print(code, raw[-400:])
        open(f"boe_{code}.csv", "w").write(raw)
    except Exception as e:
        print(code, "ERROR", repr(e))
