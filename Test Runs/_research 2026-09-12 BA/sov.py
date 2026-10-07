import urllib.request, ssl, csv, io
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
       "daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve"
       "&field_tdr_date_value=2026&page&_format=csv")
req = urllib.request.Request(url, headers={"User-Agent":"BRK framework run BA chrehor36@gmail.com"})
data = urllib.request.urlopen(req, timeout=60, context=ctx).read().decode("utf-8-sig")
rows = list(csv.DictReader(io.StringIO(data)))
print("rows:", len(rows))
for r in rows[:5]:
    print(r.get("Date"), "| 20yr", r.get("20 Yr"), "| 30yr", r.get("30 Yr"), "| 10yr", r.get("10 Yr"))
