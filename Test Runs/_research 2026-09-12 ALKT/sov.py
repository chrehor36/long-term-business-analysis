import urllib.request, io, csv, sys
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv"
req = urllib.request.Request(url, headers={"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"})
d = urllib.request.urlopen(req, timeout=60).read().decode("utf-8-sig")
rows = list(csv.DictReader(io.StringIO(d)))
print("rows:", len(rows))
print("cols:", list(rows[0].keys()))
for r in rows[:6]:
    print(r.get("Date"), "| 30Y:", r.get("30 Yr"), "| 20Y:", r.get("20 Yr"), "| 10Y:", r.get("10 Yr"))
