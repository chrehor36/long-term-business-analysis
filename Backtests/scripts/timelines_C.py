"""Batch C timelines -> gate_timelines_C.json

Transcribed from the batch C research. Two prompt errors the researcher caught
and corrected are recorded here so they are not silently absorbed:
  * Kate Spade belongs to Tapestry (TPR), acquired 2017-07-11 -- NOT to Capri.
    Capri's impairment in this window is Jimmy Choo, $351M, reported
    2020-07-01. (This also casts doubt on BT-14's TPR Gate 2 failure, which
    cited a "Kate Spade pre-COVID $855M impairment"; that charge was FY2025,
    and TPR's FY2020 impairments were reported 2020-08-13 -- AFTER the
    2020-06-30 anchor, so not knowable at it.)
  * The 2020 India debt-fund gating (2020-04-23) is Franklin Templeton's (BEN),
    not Invesco's. Invesco's India dispute (Zee) began 2021-09, post-window.
"""
import json, os

SCRATCH = os.path.dirname(os.path.abspath(__file__))

T = {
"WMT": {
  "gate1": {"verdict": "PASS", "note": "Discount retail; scale-driven supplier cost, earns on inventory turns. Segment economics fully disclosed."},
  "gate2": [
    {"from": None, "class": "WIDE", "note": "Largest global purchasing scale, ~13% ROIC (FY2013 10-K filed 2013-03); EDLP intact."},
    {"from": 2014, "class": "NARROW", "note": "US comps flat/negative 5 straight quarters through Q1 FY2015 (2014-05-15); 2015-10-14 guided FY2017 EPS down 6-12%, stock -10% in a day. Scale real but no pricing power."}],
  "gate3": [
    {"date": "2011-12", "severity": "SERIOUS", "note": "Q3 FY2012 10-Q disclosed internal Mexico FCPA probe, self-reported to DOJ/SEC."},
    {"date": "2012-04", "severity": "DISQUALIFYING", "note": "NYT 2012-04-21: ~$24M Mexico bribes plus a 2005-06 cover-up by senior executives who shut the internal probe down. Unresolved at every WMT anchor."}],
  "gate5_broken_by": None},

"ADM": {
  "gate1": {"verdict": "PASS", "note": "Buy/store/ship/crush ag commodities for origination and processing spreads."},
  "gate2": [
    {"from": None, "class": "NONE", "note": "Global origination network is scale, not a franchise: price taker with no pricing power, ROIC at or below cost of capital most of the window. 2013-11-29 GrainCorp block closed the M&A path."},
    {"from": 2019, "class": "NONE", "note": "Tariffs from 2018-07-06 cut soybean flows; negative ethanol margins, $26M bioproducts loss (2019-08-01)."}],
  "gate3": [
    {"date": "1996-10", "severity": "DISQUALIFYING", "note": "Pled guilty to lysine/citric acid price-fixing, $100M fine; three senior execs convicted 1998-09. Permanent public record."},
    {"date": "2013-05", "severity": "SERIOUS", "note": "Q1 2013 10-Q booked $25M FCPA provision, warned final figure could exceed it."},
    {"date": "2013-12", "severity": "DISQUALIFYING", "note": "2013-12-20 Toepfer (Ukraine) pled guilty to FCPA bribery, ~$54.3M total."}],
  "gate5_broken_by": None},

"BEN": {
  "gate1": {"verdict": "PASS", "note": "Fee on AUM; among the simplest P&Ls in finance."},
  "gate2": [
    {"from": None, "class": "NARROW", "note": "High-30s/40% operating margins, sticky intermediary distribution, large net cash."},
    {"from": 2015, "class": "NONE", "note": "Franchise erosion in reported results: 16 consecutive months of global equity outflows through Aug 2015; Templeton Global Bond worst-ever monthly outflow (2015-09-13); Q1 FY2016 (2016-01-28) -$20.6B net, AUM $763.9B. Persistent outflows every year 2015-2020."}],
  "gate3": [
    {"date": "2016-07", "severity": "SERIOUS", "note": "Cryer v. Franklin Resources ERISA self-dealing (proprietary funds in own 401k); settled $13.85M."},
    {"date": "2020-04", "severity": "SERIOUS", "note": "2020-04-23 Franklin Templeton India wound up six debt schemes (~$4.1B), gating redemptions. SEBI's adverse findings came 2021-06, post-window."}],
  "gate5_broken_by": "2016-01"},

"COF": {
  "gate1": {"verdict": "PASS", "note": "Consumer lender: card yield less charge-offs, funding and opex; monthly master-trust credit data published."},
  "gate2": [
    {"from": None, "class": "NARROW", "note": "Scale plus a real underwriting/data edge in near-prime and subprime card, but no pricing power in a rate-commoditized product."},
    {"from": 2020, "class": "NONE", "note": "2020-04-23 Q1: -$1.3B net loss on a ~$3.6B allowance build; no defence against a credit shock."}],
  "gate3": [
    {"date": "2012-07", "severity": "DISQUALIFYING", "note": "CFPB's first-ever enforcement action: deceptive marketing of card add-ons, $210M total. Systematic consumer deception."},
    {"date": "2015-07", "severity": "SERIOUS", "note": "OCC consent order, BSA/AML program deficiencies and SAR failures."},
    {"date": "2018-10", "severity": "SERIOUS", "note": "OCC $100M penalty for failing to remediate the 2015 AML order."},
    {"date": "2019-07", "severity": "SERIOUS", "note": "Breach disclosed 2019-07-29: ~106M applicants/customers via misconfigured WAF."}],
  "gate5_broken_by": None},

"CPRI": {
  "gate1": {"verdict": "PASS", "note": "Branded accessories/apparel; post-2018 three separately reported brands."},
  "gate2": [
    {"from": None, "class": "NARROW", "note": "Momentum, not moat: rapid store/wholesale expansion, high margins through FY2014."},
    {"from": 2015, "class": "NONE", "note": "2015-05-27 first comp decline since IPO (-5.8%), stock -24% in a day; over-distribution to department stores and permanent discounting. FY2017 (2017-05-31) wholesale -17.2%. Later moat was purchased (Jimmy Choo 2017-11, Versace 2018-12), not earned."}],
  "gate3": [],
  "gate5_broken_by": "2017-05"},

"IVZ": {
  "gate1": {"verdict": "PASS", "note": "Fee on AUM across active, ETF and institutional; heavy goodwill post-2019."},
  "gate2": [
    {"from": None, "class": "NARROW", "note": "Nine consecutive years of positive net flows through 2017; 2016 long-term net inflows +$12.7B; genuine ETF diversification."},
    {"from": 2018, "class": "NONE", "note": "FY2018 total net outflows -$29.0B ended the streak; FY2019 long-term -$34.4B (reported 2020-01-29), with ETF-driven fee compression against an active cost base."}],
  "gate3": [
    {"date": "2014-04", "severity": "SERIOUS", "note": "UK FCA fined Invesco Perpetual GBP 18.64M: 33 breaches of investment/risk limits 2008-2012, undisclosed leverage, unfair communications."}],
  "gate5_broken_by": "2019-01"},

"PBI": {
  "gate1": {"verdict": "PASS", "note": "Leases postage meters/mailing equipment to an installed base, plus supplies and financing."},
  "gate2": [
    {"from": None, "class": "NONE", "note": "Switching-cost meter base was real but the end market shrinks by structure: revenue peaked ~$6.3B in 2008 and fell every year after as first-class mail declined. 2013-04-30 dividend halved; serial divestitures (Management Services 2013-10, Software 2019-12)."}],
  "gate3": [],
  "gate5_broken_by": "2013-04"},
}

out = os.path.join(SCRATCH, "gate_timelines_C.json")
json.dump(T, open(out, "w"), indent=1)
print(f"wrote {out}: {len(T)} companies -> {', '.join(T)}")
