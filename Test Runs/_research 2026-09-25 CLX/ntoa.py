"""NTOA return series for CLX. ARITHMETIC ONLY. Balance-sheet inputs FY2010-FY2025 from SEC companyfacts
(companyfacts_live.json, pulled 2026-09-25; it does not yet carry the FY2026 10-K), FY2026 typed by hand from the
filed balance sheet (10-K 0000021076-26-000034, Exhibit 99.1 p.29). Same NTOA definition as the CL run's
peer_metrics.py: total assets - cash - current marketable securities - goodwill - other intangibles - operating ROU
- (current liabilities - debt due within one year - current operating lease liabilities).
EBIT = earnings (continuing) before income taxes + interest expense, typed from the filed income statements
(10-Ks FY2013, FY2016, FY2019, FY2022, FY2025, FY2026). 'Charges' = goodwill/trademark impairments, loss on
divestiture, pension settlement, typed from the same statements."""
import json,sys
sys.path.insert(0,'../_research 2026-09-13 CL/peers')
import peer_metrics as P
P.load=lambda tk: json.load(open('companyfacts_live.json',encoding='utf-8'))['facts']
F=P.load('CLX')
f=lambda tags,inst=True: P.first(F,tags,inst)
assets=f(['Assets']);cash=f(['CashAndCashEquivalentsAtCarryingValue']);gw=f(['Goodwill'])
intang=f(['IntangibleAssetsNetExcludingGoodwill']);tm=f(['IndefiniteLivedTrademarks']);oth=f(['FiniteLivedIntangibleAssetsNet','OtherIntangibleAssetsNet'])
rou=f(['OperatingLeaseRightOfUseAsset']);cl=f(['LiabilitiesCurrent'])
np_=f(['ShortTermBorrowings','NotesPayableCurrent','CommercialPaper','OtherShortTermBorrowings']);ltdc=f(['LongTermDebtCurrent']);leasec=f(['OperatingLeaseLiabilityCurrent'])
M=1e6
# hand FY2026 (and check FY2025) from filed balance sheet
hand={2026:dict(assets=7794,cash=143,gw=1945,intang=989+606,rou=401,cl=2773,debt=1086+1,leasec=86),
      2025:dict(assets=5561,cash=167,gw=1229,intang=502+64,rou=333,cl=1919,debt=4+0,leasec=87)}
EBIT={2011:563+123,2012:791+125,2013:853+122,2014:884+103,2015:921+100,2016:983+88,2017:1033+88,2018:1054+85,
      2019:1024+97,2020:1185+99,2021:900+99,2022:607+106,2023:238+90,2024:398+90,2025:1078+88,2026:791+130}
CHG={2011:258,2021:329,2023:445,2024:240+171,2025:118}
SALES={2011:5231,2012:5468,2013:5623,2014:5514,2015:5655,2016:5761,2017:5973,2018:6124,2019:6214,2020:6721,2021:7341,2022:7107,2023:7389,2024:7093,2025:7104,2026:6720}
nt={}
for y in range(2010,2027):
    if y in hand:
        h=hand[y]; nt_h=(h['assets']-h['cash']-h['gw']-h['intang']-h['rou'])-(h['cl']-h['debt']-h['leasec'])
    if y<2026:
        if y not in assets: continue
        ia=intang.get(y)
        if ia is None: ia=(tm.get(y) or 0)+(oth.get(y) or 0)
        d=(np_.get(y) or 0)+(ltdc.get(y) or 0)
        v=(assets[y]-(cash.get(y) or 0)-(gw.get(y) or 0)-ia-(rou.get(y) or 0))-(cl[y]-d-(leasec.get(y) or 0))
        nt[y]=v/M
        if y in hand: print(f'  check FY{y}: companyfacts NTOA {nt[y]:,.0f} vs hand from filed BS {nt_h:,.0f}; intang cf {ia/M:,.0f}')
    else:
        nt[y]=nt_h
print('| FY | net sales | EBIT (GAAP) | EBIT margin | charges | EBIT ex-charges | margin ex | NTOA year-end | avg NTOA | pre-tax return on avg NTOA (GAAP / ex-charges) |')
print('|---|---|---|---|---|---|---|---|---|---|')
for y in range(2011,2027):
    if y not in nt or y-1 not in nt: continue
    a=(nt[y]+nt[y-1])/2; e=EBIT[y]; c=CHG.get(y,0)
    print(f'| {y} | {SALES[y]:,} | {e:,} | {e/SALES[y]:.1%} | {c} | {e+c:,} | {(e+c)/SALES[y]:.1%} | {nt[y]:,.0f} | {a:,.0f} | {e/a:.1%} / {(e+c)/a:.1%} |')
