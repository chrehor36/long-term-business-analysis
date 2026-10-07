import json,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def g(a,b,n): return ((b/a)**(1/n)-1)*100
print('Form 990 filers (ProPublica Nonprofit Explorer API, organizations/<EIN>.json, raw saved as pp_<EIN>.json). Tax years end Dec.')
print('surplus margin = (total revenue - total functional expenses)/total revenue; total revenue includes contributions, grants and investment income, so it is NOT operating margin; program revenue growth uses totprgmrevnue.')
for ein in ['770070930','943029559','521674086','381428955']:
    d=json.load(open(f'pp_{ein}.json',encoding='utf-8')); o=d['organization']
    F={f['tax_prd']//100:f for f in d['filings_with_data']}
    m=[round((F[y]['totrevenue']-F[y]['totfuncexpns'])/F[y]['totrevenue']*100,1) for y in range(2019,2024)]
    pr={y:F[y]['totprgmrevnue'] for y in F}
    print(o['name'],ein,'| progrev 2013 %.2fM 2018 %.2fM 2023 %.2fM'%(pr[2013]/1e6,pr[2018]/1e6,pr[2023]/1e6),'| growth 2013-23 %.1f%%/yr, 2018-23 %.1f%%/yr'%(g(pr[2013],pr[2023],10),g(pr[2018],pr[2023],5)),'| surplus margin 2019-2023',m)
W={2013:5798,2018:17804,2019:20774,2020:20076,2021:21932,2022:24845,2023:25135}
OI={2019:1552,2020:1687,2021:2303,2022:2652,2023:2697}
print('WFCF (10-K income statements, $K) | revenue 2013 %.2fM 2018 %.2fM 2023 %.2fM'%(W[2013]/1e3,W[2018]/1e3,W[2023]/1e3),'| growth 2013-23 %.1f%%/yr (acquisitions inside), 2018-23 %.1f%%/yr'%(g(W[2013],W[2023],10),g(W[2018],W[2023],5)),'| operating margin 2019-2023',[round(OI[y]/W[y]*100,1) for y in range(2019,2024)])
V={2016:(10434,5518),2017:(12335,6809),2018:(13743,7565),2019:(15564,8444),2020:(14254,7407),2021:(16058,8402),2022:(17610,9748),2023:(19413,10986),2024:(20552,11849),2025:(20102,12214)}
print('WFCF verification and certification gross margin by year:',{y:round((a-b)/a*100,1) for y,(a,b) in V.items()})
print('H1 2026 %.1f%% vs H1 2025 %.1f%%'%((9813-5921)/9813*100,(9514-5677)/9514*100))
T={2010:(3275,1800),2011:(4233,2348),2012:(5261,2830),2013:(5798,2706),2014:(8765,3763),2015:(10395,4855),2016:(11615,5413),2017:(15448,6821),2018:(17804,7744),2019:(20774,9079),2020:(20076,8928),2021:(21932,9737),2022:(24845,10468),2023:(25135,10522),2024:(25746,10562),2025:(24892,9508)}
print('WFCF total gross margin by year:',{y:round(b/a*100,1) for y,(a,b) in T.items()})
OIa={2010:359,2011:677,2012:488,2013:27,2014:345,2015:795,2016:634,2017:82,2018:875,2019:1552,2020:1687,2021:2303,2022:2652,2023:2697,2024:2207,2025:1206}
print('WFCF operating margin by year:',{y:round(OIa[y]/T[y][0]*100,1) for y in OIa})
