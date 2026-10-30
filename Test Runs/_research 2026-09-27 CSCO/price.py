import sys, json, datetime
sys.path.insert(0, r'C:\Users\chreh\OneDrive\Documents\BRK\tools')
import sources
p = sources.price('CSCO')
print('price()', p)
import urllib.request
u = 'https://query1.finance.yahoo.com/v8/finance/chart/CSCO?range=1mo&interval=1d'
r = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
b = urllib.request.urlopen(r, timeout=60).read()
open('price_raw_CSCO.json', 'wb').write(b)
j = json.loads(b)['chart']['result'][0]
m = j['meta']
print('regularMarketPrice', m.get('regularMarketPrice'), 'time', datetime.datetime.utcfromtimestamp(m['regularMarketTime']), m.get('exchangeName'), m.get('currency'))
print('52w', m.get('fiftyTwoWeekLow'), m.get('fiftyTwoWeekHigh'))
for t, c in zip(j['timestamp'], j['indicators']['quote'][0]['close']):
    print(datetime.datetime.utcfromtimestamp(t).date(), round(c, 2) if c else c)
