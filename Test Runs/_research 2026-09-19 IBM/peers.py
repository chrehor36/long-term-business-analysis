import urllib.request, json, os, time, datetime
UA = {'User-Agent': 'chrehor36@gmail.com research'}
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'peers')
os.makedirs(D, exist_ok=True)

PEERS = {
    'MSFT': '0000789019', 'GOOGL': '0001652044', 'AMZN': '0001018724',
    'ORCL': '0001341439', 'ACN': '0001467373', 'DELL': '0001571996',
    'HPE': '0001645590', 'AVGO': '0001730168', 'SAP': '0001000184',
    'NOW': '0001373715',
}

def fetch(tkr, cik):
    p = os.path.join(D, tkr + '_companyfacts.json')
    if os.path.exists(p) and os.path.getsize(p) > 10000:
        return p
    u = 'https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json' % cik
    for i in range(4):
        try:
            b = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=180).read()
            open(p, 'wb').write(b)
            print('wrote', tkr, len(b))
            return p
        except Exception as e:
            print('retry', tkr, i, e); time.sleep(4)
    print('FAILED', tkr)
    return None

def annual(facts, tags, unit='USD'):
    out = {}
    for ns in ('us-gaap', 'ifrs-full'):
        blk = facts.get('facts', {}).get(ns, {})
        for tag in tags:
            if tag not in blk: continue
            for u, arr in blk[tag]['units'].items():
                if u != unit: continue
                for f in arr:
                    if 'start' not in f: continue
                    s = datetime.date(*map(int, f['start'].split('-')))
                    e = datetime.date(*map(int, f['end'].split('-')))
                    if not (340 <= (e - s).days <= 400): continue
                    k = f['end']
                    prev = out.get(k)
                    if prev is None or f.get('accn', '') > prev[1]:
                        out[k] = (f['val'], f.get('accn', ''), tag)
    return dict(sorted(out.items()))

def instant(facts, tags, unit='USD'):
    out = {}
    for ns in ('us-gaap', 'ifrs-full'):
        blk = facts.get('facts', {}).get(ns, {})
        for tag in tags:
            if tag not in blk: continue
            for u, arr in blk[tag]['units'].items():
                if u != unit: continue
                for f in arr:
                    if 'start' in f: continue
                    k = f['end']
                    prev = out.get(k)
                    if prev is None or f.get('accn', '') > prev[1]:
                        out[k] = (f['val'], f.get('accn', ''), tag)
    return dict(sorted(out.items()))

REV = ['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues',
       'RevenueFromContractWithCustomerIncludingAssessedTax', 'Revenue']
COGS = ['CostOfRevenue', 'CostOfGoodsAndServicesSold', 'CostOfSales']
GP = ['GrossProfit']
OI = ['OperatingIncomeLoss']
RD = ['ResearchAndDevelopmentExpense']
OCF = ['NetCashProvidedByUsedInOperatingActivities',
       'NetCashProvidedByUsedInOperatingActivitiesContinuingOperations',
       'CashFlowsFromUsedInOperatingActivities']
SBC = ['ShareBasedCompensation', 'AllocatedShareBasedCompensationExpense']
CAPEX = ['PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireProductiveAssets']
TA = ['Assets']
GW = ['Goodwill']
IA = ['IntangibleAssetsNetExcludingGoodwill', 'FiniteLivedIntangibleAssetsNet']
TL = ['Liabilities']
EQ = ['StockholdersEquity']
CASH = ['CashAndCashEquivalentsAtCarryingValue']

if __name__ == '__main__':
    for t, c in PEERS.items():
        fetch(t, c)
    for t in list(PEERS) + ['IBM']:
        p = os.path.join(D, t + '_companyfacts.json') if t != 'IBM' else os.path.join(os.path.dirname(D), 'companyfacts.json')
        if not os.path.exists(p):
            print(t, 'MISSING'); continue
        f = json.load(open(p, encoding='utf-8'))
        print('=====', t, f.get('entityName'))
        for label, tags in [('rev', REV), ('gp', GP), ('cogs', COGS), ('oi', OI), ('rd', RD),
                            ('ocf', OCF), ('sbc', SBC), ('capex', CAPEX)]:
            a = annual(f, tags)
            items = [(k, v[0], v[2]) for k, v in a.items() if k >= '2019-01-01']
            print(' ', label, [(k, round(v / 1e6, 1), tg) for k, v, tg in items][-7:])
        for label, tags in [('assets', TA), ('gw', GW), ('ia', IA), ('liab', TL), ('eq', EQ)]:
            a = instant(f, tags)
            items = [(k, v[0]) for k, v in a.items() if k >= '2024-06-01']
            print(' ', label, [(k, round(v / 1e6, 1)) for k, v in items][-4:])
