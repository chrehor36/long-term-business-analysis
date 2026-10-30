# Peer metrics from each filer's own XBRL (companyfacts), annual 10-K values, transcription only.
import json, sys, datetime, os
S = sys.argv[1]
TAGS = {
 "NI": ["NetIncomeLoss","ProfitLoss"],
 "EQ": ["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
 "GW": ["Goodwill"],
 "INT": ["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet","OtherIntangibleAssetsNet","CoreDepositsIntangibleAssetsNet"],
 "AS": ["Assets"],
 "DEP": ["Deposits"],
 "IXD": ["InterestExpenseDeposits"],
 "NII": ["InterestIncomeExpenseNet","InterestIncomeExpenseAfterProvisionForLoanLoss"],
 "PROV": ["ProvisionForLoanLeaseAndOtherLosses","ProvisionForLoanAndLeaseLosses","ProvisionForCreditLossExpenseReversal","ProvisionForLoanLossesExpensed"],
 "NCO_W": ["FinancingReceivableAllowanceForCreditLossesWriteOffs","AllowanceForLoanAndLeaseLossesWriteOffs","FinancingReceivableAllowanceForCreditLossesWriteOffsNet","AllowanceForLoanAndLeaseLossesWriteOffsNet"],
 "NCO_R": ["FinancingReceivableAllowanceForCreditLossesRecovery","AllowanceForLoanAndLeaseLossRecoveryOfBadDebts"],
 "LOANS": ["LoansAndLeasesReceivableNetOfDeferredIncome","LoansAndLeasesReceivableGrossCarryingAmount","FinancingReceivableExcludingAccruedInterestBeforeAllowanceForCreditLoss","LoansAndLeasesReceivableNetReportedAmount","NotesReceivableNet"],
 "NIE": ["NoninterestExpense"],
 "NONII": ["NoninterestIncome"],
}
def series(g, names, dur):
    out = {}
    for n in names:
        if n not in g: continue
        for u, arr in g[n]["units"].items():
            if u != "USD": continue
            for x in arr:
                if x.get("form") not in ("10-K","10-K/A"): continue
                e = x["end"]
                if dur:
                    if "start" not in x: continue
                    d = (datetime.date.fromisoformat(e) - datetime.date.fromisoformat(x["start"])).days
                    if not 340 <= d <= 380: continue
                else:
                    if "start" in x: continue
                if not e.endswith("12-31"): continue
                y = int(e[:4])
                # latest filed wins
                if y not in out or x["filed"] > out[y][1]:
                    out[y] = (x["val"], x["filed"], n)
        # do not mix tags: fill only missing years from later names
    return {y: v[0] for y, v in out.items()}
def merged(g, names, dur):
    res = {}
    for n in names:
        s = series(g, [n], dur)
        for y, v in s.items():
            res.setdefault(y, v)
    return res
rows = []
for t in sys.argv[2:]:
    g = json.load(open(os.path.join(S, f"{t}_facts.json")))["facts"]["us-gaap"]
    d = {k: merged(g, v, k in ("NI","IXD","NII","PROV","NCO_W","NCO_R","NIE","NONII")) for k, v in TAGS.items()}
    print(f"\n=== {t}")
    print("year     NI      EQ     TCE  assets   deposits  depInt  depCost%  ROA%  ROTCE%  NIM~%  prov   NCOw   loans")
    for y in range(2008, 2026):
        NI=d["NI"].get(y); EQ=d["EQ"].get(y); A=d["AS"].get(y); D=d["DEP"].get(y); IXD=d["IXD"].get(y)
        GW=d["GW"].get(y,0) or 0; IN=d["INT"].get(y,0) or 0
        if NI is None and EQ is None: continue
        Dp=d["DEP"].get(y-1); Ap=d["AS"].get(y-1); EQp=d["EQ"].get(y-1); GWp=d["GW"].get(y-1,0) or 0; INp=d["INT"].get(y-1,0) or 0
        def m(v): return f"{v/1e6:8.1f}" if v is not None else "       -"
        tce = (EQ-GW-IN) if EQ is not None else None
        tcep = (EQp-GWp-INp) if EQp is not None else None
        dc = (IXD/((D+Dp)/2)*100) if (IXD is not None and D and Dp) else None
        roa = (NI/((A+Ap)/2)*100) if (NI is not None and A and Ap) else None
        rotce = (NI/((tce+tcep)/2)*100) if (NI is not None and tce and tcep) else None
        nii = d["NII"].get(y); nim = (nii/((A+Ap)/2)*100) if (nii and A and Ap) else None
        f = lambda v: f"{v:7.2f}" if v is not None else "      -"
        print(f"{y} {m(NI)} {m(EQ)} {m(tce)} {m(A)} {m(D)} {m(IXD)} {f(dc)} {f(roa)} {f(rotce)} {f(nim)} {m(d['PROV'].get(y))} {m(d['NCO_W'].get(y))} {m(d['LOANS'].get(y))}")
