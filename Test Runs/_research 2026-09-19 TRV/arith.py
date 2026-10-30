"""TRV run 2026-09-19 -- all arithmetic, reproducible.
Tags read from companyfacts.json (transcription/screening only, operator rule 4);
every headline figure cross-checked against the filed 10-K text in this folder.
"""
import json, sys

F = json.load(open('companyfacts.json'))['facts']['us-gaap']

def ann(tags, unit='USD'):
    """Tag list is a UNION -- filers switch concepts mid-history (the defect
    tools/sources.py:annual() documents). Earlier tags win where both cover a year."""
    if isinstance(tags, str): tags = [tags]
    out = {}
    for t in tags:
        for k, v in _ann1(t, unit).items():
            out.setdefault(k, v)
    return dict(sorted(out.items()))


def _ann1(tag, unit='USD'):
    """Annual (FY, ~365d) duration facts, keyed by fiscal year end. Earliest-filed wins."""
    out = {}
    for x in F[tag]['units'][unit]:
        if x.get('form') not in ('10-K',): continue
        s, e = x.get('start'), x['end']
        if not s: continue
        from datetime import date
        d0 = date.fromisoformat(s); d1 = date.fromisoformat(e)
        if not (350 <= (d1-d0).days <= 380): continue
        y = d1[:4] if isinstance(d1,str) else e[:4]
        k = e
        if k not in out or x['fy'] < out[k][1]:
            out[k] = (x['val'], x['fy'])
    return {k[:4]: v[0]/1e6 for k, v in sorted(out.items())}

def inst(tags, unit='USD'):
    if isinstance(tags, str): tags = [tags]
    out = {}
    for t in tags:
        for k, v in _inst1(t, unit).items():
            out.setdefault(k, v)
    return dict(sorted(out.items()))


def _inst1(tag, unit='USD'):
    out = {}
    for x in F[tag]['units'][unit]:
        if x.get('form') not in ('10-K',): continue
        if x.get('start'): continue
        k = x['end']
        if not k.endswith('12-31'): continue
        if k not in out or x['fy'] < out[k][1]:
            out[k] = (x['val'], x['fy'])
    return {k[:4]: v[0]/1e6 for k, v in sorted(out.items())}

YRS = [str(y) for y in range(2014, 2026)]

nep  = ann('PremiumsEarnedNet')
clm  = ann('PolicyholderBenefitsAndClaimsIncurredNet')
dac  = ann('DeferredPolicyAcquisitionCostAmortizationExpense')
ga   = ann(['SellingGeneralAndAdministrativeExpense', 'GeneralAndAdministrativeExpense'])
nii  = ann('NetInvestmentIncome')
ni   = ann('NetIncomeLoss')
ocf  = ann('NetCashProvidedByUsedInOperatingActivities')
bb   = ann('PaymentsForRepurchaseOfCommonStock')
div  = ann('PaymentsOfDividendsCommonStock')
sbc  = ann('AllocatedShareBasedCompensationExpense')

invt = inst('Investments')
resv = inst('LiabilityForClaimsAndClaimsAdjustmentExpense')
unep = inst('UnearnedPremiums')
recv = inst(['ReinsuranceRecoverablesOnPaidAndUnpaidLosses', 'ReinsuranceRecoverables'])
prem = inst('PremiumsReceivableAtCarryingValue')
dpac = inst('DeferredPolicyAcquisitionCosts')
eq   = inst('StockholdersEquity')

def g(d, y):
    return d.get(y)

print("=" * 108)
print("A.  WHERE THE EARNINGS COME FROM -- GAAP underwriting result vs net investment income ($m, pre-tax)")
print("=" * 108)
print(f"{'yr':<6}{'NEP':>9}{'claims':>9}{'DACamort':>10}{'G&A':>9}{'UWresult':>10}{'NII':>9}{'UW%ofsum':>10}")
tot_uw = tot_nii = 0
uwr = {}
for y in YRS:
    if not all(g(d,y) is not None for d in (nep,clm,dac,ga,nii)): continue
    u = nep[y] - clm[y] - dac[y] - ga[y]
    uwr[y] = u
    tot_uw += u; tot_nii += nii[y]
    print(f"{y:<6}{nep[y]:>9,.0f}{clm[y]:>9,.0f}{dac[y]:>10,.0f}{ga[y]:>9,.0f}{u:>10,.0f}{nii[y]:>9,.0f}{100*u/(u+nii[y]):>9.1f}%")
print(f"{'TOTAL':<6}{'':>9}{'':>9}{'':>10}{'':>9}{tot_uw:>10,.0f}{tot_nii:>9,.0f}{100*tot_uw/(tot_uw+tot_nii):>9.1f}%")

print()
print("=" * 108)
print("B.  FLOAT, by CONVENTION 4 of the sector method (WTM run, 2026-09-02):")
print("    float = loss & LAE reserves + unearned premiums - reinsurance recoverables - premiums receivable - DAC")
print("=" * 108)
print(f"{'yr':<6}{'reserves':>10}{'unearned':>10}{'recover':>10}{'premrecv':>10}{'DAC':>8}{'FLOAT':>10}{'invts':>10}{'f/inv':>8}{'equity':>9}{'inv/eq':>8}")
flt = {}
for y in YRS:
    if not all(g(d,y) is not None for d in (resv,unep,recv,prem,dpac,invt,eq)): continue
    f = resv[y] + unep[y] - recv[y] - prem[y] - dpac[y]
    flt[y] = f
    print(f"{y:<6}{resv[y]:>10,.0f}{unep[y]:>10,.0f}{recv[y]:>10,.0f}{prem[y]:>10,.0f}{dpac[y]:>8,.0f}"
          f"{f:>10,.0f}{invt[y]:>10,.0f}{100*f/invt[y]:>7.1f}%{eq[y]:>9,.0f}{invt[y]/eq[y]:>7.2f}x")

print()
print("=" * 108)
print("C.  COST OF FLOAT [E3-69] -- underwriting result against float developed. NEGATIVE cost = float was free AND paid.")
print("=" * 108)
print(f"{'yr':<6}{'UWresult':>10}{'float(avg)':>12}{'cost of float':>15}")
ys = [y for y in YRS if y in flt and y in uwr]
tot_u = 0.0; wt = 0.0
for i, y in enumerate(ys):
    py = str(int(y)-1)
    favg = (flt[y] + flt[py]) / 2 if py in flt else flt[y]
    c = -uwr[y] / favg * 100
    tot_u += uwr[y]; wt += favg
    print(f"{y:<6}{uwr[y]:>10,.0f}{favg:>12,.0f}{c:>14.2f}%")
print(f"{'MEAN':<6}{tot_u/len(ys):>10,.0f}{wt/len(ys):>12,.0f}{-tot_u/wt*100:>14.2f}%  <- the multi-year figure [E3-69] requires")

print()
print("=" * 108)
print("D.  THE PRIMARY TEST [E2-01] -- earnings rate on equity capital employed")
print("=" * 108)
print(f"{'yr':<6}{'netinc':>9}{'avg equity':>12}{'ROE':>8}")
for y in YRS:
    py = str(int(y)-1)
    if y not in ni or y not in eq or py not in eq: continue
    ae = (eq[y] + eq[py]) / 2
    print(f"{y:<6}{ni[y]:>9,.0f}{ae:>12,.0f}{100*ni[y]/ae:>7.1f}%")

print()
print("=" * 108)
print("E.  RETENTION TEST [E3-54] -- $1 of market value per $1 retained, and capital returned")
print("=" * 108)
print(f"{'yr':<6}{'netinc':>9}{'dividends':>11}{'buybacks':>10}{'retained':>10}{'payout%':>9}{'SBC':>7}{'OCF':>10}")
for y in YRS:
    if y not in ni: continue
    d_ = div.get(y, 0); b_ = bb.get(y, 0)
    print(f"{y:<6}{ni[y]:>9,.0f}{d_:>11,.0f}{b_:>10,.0f}{ni[y]-d_-b_:>10,.0f}{100*(d_+b_)/ni[y]:>8.0f}%{sbc.get(y,0):>7,.0f}{ocf.get(y,0):>10,.0f}")
