import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from build import *
def debt_sum(*pairs):
  def f(F,fy,own):
    tot=0;ok=False;acc=None
    for cs in pairs:
      v=get(F,cs,fy,own,True)
      if v: tot+=v[0];ok=True;acc=v[1]
    return (round(tot,1),acc,'sum') if ok else None
  return f
VST=dict(name='Vistra Corp (VST, CIK 1692819)',cik='0001692819',
 own={2016:'0001692819-18-000018',2017:'0001692819-18-000018',2018:'0001692819-19-000005',2019:'0001692819-20-000005',2020:'0001692819-21-000004',2021:'0001692819-22-000005',2022:'0001692819-23-000005',2023:'0001692819-24-000012',2024:'0001692819-25-000013',2025:'0001692819-26-000006'},
 map=dict(rev='Revenues',oi='OperatingIncomeLoss',da='DepreciationDepletionAndAmortization',ocf='NetCashProvidedByUsedInOperatingActivities',capex='PaymentsToAcquirePropertyPlantAndEquipment',
  sbc='ShareBasedCompensation',ta='Assets',gw='Goodwill',intang='IntangibleAssetsNetExcludingGoodwill',debt='LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities',cash='CashAndCashEquivalentsAtCarryingValue',
  eq=['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','StockholdersEquity'],buyb='PaymentsForRepurchaseOfCommonStock'),
 ovr={2016:{'eq':6597.0},2017:{'capex':366.0,'nuc':62.0,'acq':355.0,'sbc':19.0},2018:{'capex':530.0,'nuc':118.0,'acq':0.0},2019:{'capex':713.0,'nuc':89.0,'acq':880.0},2020:{'nuc':88.0,'acq':0.0},2021:{'nuc':44.0,'acq':0.0},2022:{'nuc':198.0,'acq':0.0},2023:{'nuc':214.0,'acq':0.0},2024:{'nuc':477.0,'acq':3065.0},2025:{'acq':1140.0}},
 ytdmap=dict(acq='PaymentsToAcquireBusinessesNetOfCashAcquired'))
CEG=dict(name='Constellation Energy (CEG, CIK 1868275)',cik='0001868275',
 own={2020:'0001868275-22-000020',2021:'0001868275-22-000020',2022:'0001868275-23-000014',2023:'0001868275-24-000014',2024:'0001868275-25-000023',2025:'0001868275-26-000032'},
 map=dict(rev='Revenues',oi='OperatingIncomeLoss',da='CostOfGoodsAndServicesSoldDepreciationAndAmortization',ocf='NetCashProvidedByUsedInOperatingActivities',capex='PaymentsToAcquirePropertyPlantAndEquipment',
  acq='PaymentsToAcquireBusinessesNetOfCashAcquired',sbc='AllocatedShareBasedCompensationExpense',ta='Assets',gw='Goodwill',intang='FiniteLivedIntangibleAssetsNet',
  debt=debt_sum('LongTermDebtNoncurrent','LongTermDebtCurrent'),cash='CashAndCashEquivalentsAtCarryingValue',eq='StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest',buyb='PaymentsForRepurchaseOfCommonStock'),
 ovr={2020:{'ta':48094.0,'cash':226.0,'debt':5763.0,'eq':14676.0},2021:{'gw':47.0,'debt':6114.0,'eq':11614.0},2022:{'buyb':0.0}},
 ytdmap=dict(sbc='ShareBasedCompensation',debt=['LongTermDebtNoncurrent']))
TLN=dict(name='Talen Energy (TLN, CIK 1622536)',cik='0001622536',
 own={2022:'0001628280-25-008786',2023:'0001628280-25-008786',2024:'0001628280-25-008786',2025:'0001622536-26-000017'},
 map=dict(rev='Revenues',oi='OperatingIncomeLoss',da='DepreciationDepletionAndAmortization',ocf='NetCashProvidedByUsedInOperatingActivities',capex='PaymentsToAcquirePropertyPlantAndEquipment',nuc='PaymentsForNuclearFuel',
  acq='PaymentsToAcquireBusinessesNetOfCashAcquired',sbc='ShareBasedCompensation',ta='Assets',gw='Goodwill',intang='IntangibleAssetsNetExcludingGoodwill',
  debt=debt_sum('LongTermDebtNoncurrent','LongTermDebtCurrent'),cash='CashAndCashEquivalentsAtCarryingValue',eq='StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest',buyb='PaymentsForRepurchaseOfCommonStock'),
 ovr={2022:{'eq':-482.0,'acq':0.0},2023:{'rev':2554.0,'oi':84.0,'da':365.0,'ocf':864.0,'capex':254.0,'nuc':94.0,'sbc':19.0,'buyb':0.0,'acq':0.0,'gw':0.0,'intang':0.0},2024:{'gw':0.0,'intang':0.0,'acq':0.0},2025:{'gw':0.0,'intang':0.0}},
 ytdmap=dict(nuc='PaymentsForNuclearFuel'))
GNE=dict(name='Genie Energy (GNE, CIK 1528356)',cik='0001528356',
 own={2016:'0001213900-17-002459',2017:'0001213900-18-003067',2018:'0001213900-19-004396',2019:'0001213900-20-006416',2020:'0001213900-21-015538',2021:'0001213900-22-012716',2022:'0001213900-23-020226',2023:'0001213900-24-022573',2024:'0001213900-25-024009',2025:'0001437749-26-014294'},
 map=dict(rev=['Revenues','RevenueFromContractWithCustomerIncludingAssessedTax','RevenueFromContractWithCustomerExcludingAssessedTax'],oi='OperatingIncomeLoss',da='DepreciationAndAmortization',ocf='NetCashProvidedByUsedInOperatingActivities',
  capex=['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsForCapitalImprovements'],acq=['PaymentsToAcquireBusinessesNetOfCashAcquired','PaymentsToAcquireBusinessesGross'],sbc='ShareBasedCompensation',ta='Assets',gw='Goodwill',
  intang=['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],debt=debt_sum(['LongTermDebtNoncurrent','LongTermDebt','LongTermLineOfCredit','LineOfCredit'],['LongTermDebtCurrent']),cash='CashAndCashEquivalentsAtCarryingValue',
  eq=['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','StockholdersEquity'],buyb='PaymentsForRepurchaseOfCommonStock'),
 ovr={2025:{'capex':8.2,'buyb':8.7,'acq':0.0},2016:{'debt':0.0,'eq':79.9},2021:{'debt':0.0,'acq':0.0},2022:{'debt':0.0,'acq':0.0},2023:{'debt':0.0},2020:{'acq':0.0}},
 ytdmap=dict())
VIA=dict(name='Via Renewables, formerly Spark Energy (VIA, CIK 1606268)',cik='0001606268',
 own={2016:'0001606268-17-000012',2017:'0001606268-18-000017',2018:'0001606268-19-000008',2019:'0001606268-20-000008',2020:'0001606268-21-000015',2021:'0001606268-22-000008',2022:'0001606268-23-000009',2023:'0001606268-24-000008',2024:'0001606268-25-000006',2025:'0001606268-26-000013'},
 map=dict(rev='Revenues',oi='OperatingIncomeLoss',da='DepreciationAndAmortization',ocf='NetCashProvidedByUsedInOperatingActivities',capex='PaymentsToAcquirePropertyPlantAndEquipment',
  acq='PaymentsToAcquireBusinessesNetOfCashAcquired',sbc='ShareBasedCompensation',ta='Assets',gw='Goodwill',intang='FiniteLivedIntangibleAssetsNet',
  cash='CashAndCashEquivalentsAtCarryingValue',eq='StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest',buyb='PaymentsForRepurchaseOfCommonStock'),
 ovr={2016:{'intang':33.5,'debt':71.8,'eq':123.7,'gw':79.1},2017:{'debt':159.2,'eq':161.3},2018:{'debt':146.4,'eq':90.3},2019:{'debt':123.0,'eq':67.3},2020:{'debt':100.0,'eq':88.5},2021:{'debt':135.0,'eq':50.4,'acq':0.0,'buyb':0.0},2022:{'debt':120.0,'eq':28.3,'acq':0.0,'buyb':0.0},2023:{'debt':97.0,'eq':38.7,'acq':0.0,'buyb':0.0},2024:{'debt':106.0,'eq':81.0,'acq':0.0,'buyb':0.0},2025:{'debt':120.0,'eq':77.4,'acq':0.0,'buyb':0.0,'sbc':0.0}},
 ytdmap=dict(debt=['LongTermDebt','LongTermLineOfCredit']))
COS=[('VST',VST,('2026-01-01','2026-06-30')),('CEG',CEG,('2026-01-01','2026-06-30')),('TLN',TLN,('2026-01-01','2026-06-30')),('GNE',GNE,('2026-01-01','2026-06-30')),('VIA',VIA,('2026-01-01','2026-03-31'))]
def fmt(v):
  if v is None: return 'n/a'
  return f'{v:,.0f}' if abs(v)>=100 else f'{v:,.1f}'
def pct(r): return 'n/a' if r is None else f'{r*100:.1f}%'
def ratios(r,nuc_separate):
  try: r1=r['oi']/(r['ta']-r.get('gw',0)-r.get('intang',0))
  except Exception: r1=None
  try:
    cap=r['capex']+(r.get('nuc',0) if nuc_separate else 0)
    r2=(r['ocf']-r.get('sbc',0)-cap)/r['rev']
  except Exception: r2=None
  return r1,r2
def avg(L,lo,hi):
  v=[r for yy,r in L if r is not None and lo<=yy<=hi]
  return (sum(v)/len(v),len(v)) if v else (None,0)
def fa(a): return 'n/a' if a[0] is None else f'{a[0]*100:.1f}% (n={a[1]})'
out=[];summary={}
for tk,cfg,(s,e) in COS:
  rows,src=run(cfg)
  y=ytd(cfg,s,e)
  nucsep = tk=='TLN'
  yrs=sorted(rows)
  out.append(f'\n### {cfg["name"]} -- annual data (USD millions)\n')
  out.append('| Item | '+' | '.join(f'FY{yy}' for yy in yrs)+f' | YTD to {e} |')
  out.append('|'+'---|'*(len(yrs)+2))
  for it in ITEMS:
    vals=[rows[yy].get(it) for yy in yrs]
    if all(v is None for v in vals) and it not in y: continue
    out.append(f'| {LBL[it]} | '+' | '.join(fmt(v) for v in vals)+f' | {fmt(y.get(it))} |')
  R1=[];R2=[]
  for yy in yrs:
    r1,r2=ratios(rows[yy],nucsep); R1.append((yy,r1)); R2.append((yy,r2))
  y1,y2=ratios(y,nucsep)
  out.append('| **OI / (TA - GW - intangibles)** | '+' | '.join(pct(r) for _,r in R1)+f' | {pct(y1)} (not annualised) |')
  out.append('| **(OCF - SBC - capex) / revenue** | '+' | '.join(pct(r) for _,r in R2)+f' | {pct(y2)} |')
  lo=2021 if tk=='CEG' else 2016
  a1=avg(R1,2021,2025);a2=avg(R2,2021,2025);w1=avg(R1,lo,2025);w2=avg(R2,lo,2025)
  out.append(f'\nAverages (simple mean of yearly ratios). OI/(TA-GW-intang): FY2021-25 = {fa(a1)}; whole span = {fa(w1)}. (OCF-SBC-capex)/revenue: FY2021-25 = {fa(a2)}; whole span = {fa(w2)}.\n')
  summary[tk]=(R1,R2,a1,a2,w1,w2,y1,y2)
  acc=sorted({v for v in src.values() if v not in('text',None,'sum')})
  out.append('XBRL company-facts values in this table come from these 10-K accessions: '+', '.join(acc)+'. Cells marked in the notes below were transcribed from filing text instead.\n')
open(sys.argv[1],'w',encoding='utf-8').write('\n'.join(out))
for tk,(R1,R2,a1,a2,w1,w2,y1,y2) in summary.items():
  print(tk,'R1:',' '.join(f'{yy}:{pct(r)}' for yy,r in R1),'| 5y',fa(a1),'all',fa(w1),'ytd',pct(y1))
  print(tk,'R2:',' '.join(f'{yy}:{pct(r)}' for yy,r in R2),'| 5y',fa(a2),'all',fa(w2),'ytd',pct(y2))
