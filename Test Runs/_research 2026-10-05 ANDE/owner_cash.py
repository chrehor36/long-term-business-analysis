import xb
f=xb.load('ANDE')
A=lambda *t: xb.first(f,list(t))
pl=A('ProfitLoss'); nci=A('NetIncomeLossAttributableToNoncontrollingInterest'); ni=A('NetIncomeLoss')
da=A('DepreciationDepletionAndAmortization','DepreciationAndAmortization')
cx=A('PaymentsToAcquirePropertyPlantAndEquipment')
imp=A('AssetImpairmentCharges','ImpairmentOfLongLivedAssetsHeldForUse')
sbc=A('ShareBasedCompensation','AllocatedShareBasedCompensationExpense')
ocf=A('NetCashProvidedByUsedInOperatingActivities')
dno=A('IncomeLossFromDiscontinuedOperationsNetOfTax'); dda=A('DepreciationAndAmortizationDiscontinuedOperations'); dcx=A('CapitalExpenditureDiscontinuedOperations')
pt=A('IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest')
g=lambda d,k: d.get(k,0)/1e6
rows={}
print(f"{'FY':6}{'NIcont':>8}{'D&Acont':>8}{'impair':>7}{'capexC':>8}{'OC_capex':>9}{'OC_D&A':>8}{'NCI_NI':>7}{'OCF':>7}{'pretax':>7}")
for k in sorted(pl):
    if k<'2016': continue
    y=k[:4]
    nic=g(pl,k)-g(dno,k); dac=g(da,k)-g(dda,k); cxc=g(cx,k)-g(dcx,k); im=g(imp,k)
    # 2019 capex tag: check if PaymentsToAcquirePPE includes discontinued
    oc1=nic+dac+im-cxc; oc2=nic+im  # D&A basis: NI + impairment (D&A as the capex proxy)
    rows[y]=(nic,dac,im,cxc,oc1,oc2,g(nci,k),g(ocf,k),g(pt,k))
    print(f"{y:6}{nic:8.1f}{dac:8.1f}{im:7.1f}{cxc:8.1f}{oc1:9.1f}{oc2:8.1f}{g(nci,k):7.1f}{g(ocf,k):7.0f}{g(pt,k):7.1f}")
import statistics as st
for lo,hi in [(2021,2025),(2019,2025),(2016,2025)]:
    ys=[str(y) for y in range(lo,hi+1)]
    print(lo,hi,'mean OC capex %.1f  OC D&A %.1f  NIcont %.1f  pretax %.1f  OCF %.1f  sumOCF %.0f  sum(NIc+D&Ac+imp) %.0f' % (
      st.mean(rows[y][4] for y in ys), st.mean(rows[y][5] for y in ys), st.mean(rows[y][0] for y in ys), st.mean(rows[y][8] for y in ys), st.mean(rows[y][7] for y in ys),
      sum(rows[y][7] for y in ys), sum(rows[y][0]+rows[y][1]+rows[y][2] for y in ys)))
