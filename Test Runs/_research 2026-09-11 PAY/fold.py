#!/usr/bin/env python3
"""The six-step fold for the PAY run: queue entry, roster strike, narrative fold, standing count."""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 1. QUEUE: COMPLETED entry at the top; 2. roster strike
q = os.path.join(ROOT, "Screens", "WATCHLIST RUN QUEUE.md")
s = open(q, encoding="utf-8").read()
entry = """- **PAY (Paymentus), 2026-09-11 (killed twice by session limits, resumed with zero question
  loss) - FAIL at Q2, ON THE BUSINESS. Q1 IN, Q2 OUT.** `Test Runs/2026-09-11 Run - PAY
  Paymentus.md`, `check_framework.py` PASS.
  Price **$36.28** (2026-09-10 close, aggregator, flagged) x **125,939,647 shares** (Class A
  63,114,220 + Class B 62,825,427, read off the **Q2 2026 10-Q cover, period 2026-06-30,
  accession `0001193125-26-330940`**; the classes are identical except for votes and
  conversion on the charter's own words, so they sum) = cap **$4,569M**. Sovereign **5.37%
  USD** (US Treasury 30-yr, issuing authority, 2026-09-10).
  **THE QUEUE'S `cap_m 3635` IS THE PRE-IPO COUNT, SEVENTH INSTANCE.** Reproduced to the
  dollar: $35.13 (2026-09-01 close) x **103,479,239** = `us-gaap:CommonStockSharesOutstanding`
  at **2020-12-31**, five months before the May 2021 listing and the last undimensioned share
  fact this filer ever tagged (every later cover is by class; the FY2021 10-K tags 2021 as 0).
  Cap understated **20.4%**; the 550-day guard did not fire because the FY2021 10-K re-tagged
  the 2020 value in 2022 and reset the clock. Corrected `yield_bottom` **0.55%**.
  **REVENUE IS GROSS.** *"The Company recognizes fees charged to customers primarily on a
  gross basis ... when the Company is the principal"*; interchange and network fees sit in cost
  of revenue. Of each revenue dollar in 2025, **67.7 cents** went to the networks, **32.3
  cents** was Paymentus's own top line (its filed "contribution profit"), **24.8** survived the
  cost of serving, **6.3** was operating income. Six years earlier the kept share was 41.0
  cents. Payment volume in dollars is **not filed** (sweep of 7 filings), so the fraction of a
  *billed* dollar cannot be computed; the fraction of a *revenue* dollar can.
  **THE UNIT SERIES DECIDED THE GATE [E4-55].** Transactions 146.2M (2019) to **724.0M**
  (2025), +21.3% in 2025, +19.4% in H1 2026; **contribution profit per transaction $0.661 to
  $0.534, down 19% in six years** and down in five of the six, while revenue per transaction
  rose 2.5% only because pass-through per transaction rose 18%. The filer wrote the same
  sentence in four consecutive 10-Ks - CP grew slower than transactions *"due to a continued
  mix shift to larger, high volume clients"* - and its Item 1 says *"We also compete on
  pricing"*, and its MD&A that *"our adjustments typically lag ... We may be unable to fully
  adjust our pricing."* [E2-44] half two passes outright (capital 3.1% of revenue, $378M net
  cash, PP&E $0.9M); half one fails. Q2 OUT on [E3-03](2); class NONE.
  **Competitor row of 8** (Fiserv, FIS, ACIW, Repay, JKHY, FLYW, BILL, EngageSmart FY2022
  stale), four private named as a hard limit (Alacriti, Kubra, One Inc., PayNearMe). ACI
  Worldwide names Paymentus eighth of nine; Repay third of six and **took a $254.7M
  impairment on that segment in 2025**; Fiserv and FIS do not name it. On its own net top
  line Paymentus earns 19.6% operating margin against Fiserv 27.5% and JKHY 23.9%.
  **[E2-49] FIRES (the prior is now 2 for 6):** the biller count (1,300 / 1,700 / 1,900 /
  2,200 / 2,500 across five vintages) is **absent from the FY2025 10-K**; net revenue
  retention was **never filed**. **[E4-29] fires at full strength in the releases**: *"record
  adjusted EBITDA margin 41.3%"* is adjusted EBITDA over contribution profit - a non-GAAP over
  a non-GAAP; on GAAP revenue it is 13.5%; three of four bonus metrics are non-GAAP; eight
  consecutive releases beat and raised. Founder-CEO granted a **$34.2M one-time RSU** in July
  2025 *"to address the fact that he had not previously been awarded any RSUs"* while owning
  18%; 480,000 more in April 2026. AKKR 58.2% + founder 31.3% of votes on 52% of the shares;
  ~27M Class B converted in H2 2025 as the sponsor sold. All recorded, none adjudicated.
  **Priors refuted:** customer funds are **off balance sheet** ($215.7M custodial, held by
  Braintree and sponsor banks) so OCF is not float-flattered; the OE sign change is
  2021-2022 from a capitalised-software ramp against flat OCF, not the IPO; the 2025 OCF step
  ($64M to $162M) is one-third a $60.8M receivables swing. Years chosen **2023-2025**; rebuilt
  width **$21.4M to $106.4M** (published $24M to $48M); bottom positive, one-fifth of the top.
  **SBC/OCF 11.5%** - the lowest in the calibrated row (CRWD 68.0, PINS 68.6, QLYS 24.9, CRM
  23.4, SHOP 22.1, **PAY 11.5**). Under `COMPUTATION - NOT A CLEARANCE`: yield **0.47% to
  2.33%**, -4.9 to -3.0 points vs the bond; zero-growth value **~$4 to $16/share** at the bare
  sovereign, ~$2 to $8 at the floor; the only path over the floor is the single best year plus
  a decade of 20%+.
  **No alert, no PORTFOLIO row** - the failure is on the business; reversal condition (CP per
  transaction rising three fiscal years on a flat-or-rising gross margin) recorded in words
  in the run's REGISTER.
"""
hdr = "## COMPLETED FROM THE QUEUE\n"
assert hdr in s
if "PAY (Paymentus), 2026-09-11" not in s:
    s = s.replace(hdr, hdr + entry, 1)
import re as _re
s = _re.sub(r"(~~SHOP~~, )PAY,", r"~~PAY~~,", s, count=1)
assert "~~PAY~~" in s
open(q, "w", encoding="utf-8", newline="\n").write(s)
print("queue ok")

# 3. NARRATIVE FOLD into the reading list, and the standing count
r = os.path.join(ROOT, "Screens", "2026-08-31 PREPPED READING LIST (operator lists).md")
t = open(r, encoding="utf-8").read()
fold = """## PAY FOLDED IN - 2026-09-11. SIXTY-FOUR RUNS; THE FILER PASSES TWO-THIRDS OF EVERY DOLLAR THROUGH AND SAYS IT COMPETES ON PRICE.

### PAY (Paymentus) - Q1 IN . **Q2 OUT.** FAIL, on the business, not on price. Price $36.28.
`Test Runs/2026-09-11 Run - PAY Paymentus.md`. Killed twice by session limits, resumed each time
with zero question loss (Step 0 and Q1 were on disk and committed before the first kill; the Q2
draft was on disk before the second). Cap **$4,569M** on **125,939,647** cover-read shares (Q2
2026 10-Q, acc. `0001193125-26-330940`; two classes, identical but for votes and conversion,
summed on the charter's words); sovereign **5.37%** (US Treasury 30-yr, 2026-09-10). Owner
earnings **$21.4M to $106.4M** across seven windows (published $24M to $48M); yield **0.47 to
2.33%**, 3.0 to 4.9 points under the bond; value **~$4 to $16/share** at the bare bond, ~$2 to $8
at the floor. All under `COMPUTATION - NOT A CLEARANCE`.

- **THE FINDING THAT MATTERS BEYOND THIS NAME: WHEN A PRINCIPAL REPORTS GROSS, THE HONEST UNIT
  PRICE IS THE NET TOP LINE PER UNIT, AND IT CAN FALL WHILE REVENUE PER UNIT RISES.** Paymentus
  recognises interchange gross and files "contribution profit" (revenue less network fees) in
  every vintage. Revenue per transaction rose 2.5% over 2019-2025; **contribution profit per
  transaction fell 19%**, five years out of six; the difference is pass-through on bigger bills.
  A run that read revenue per unit would have scored [E4-55] clean. The company itself wrote in
  four consecutive 10-Ks that its net top line grew slower than units *"due to a continued mix
  shift to larger, high volume clients"* - the PayPal/Block/Adyen mechanism from the SHOP row,
  named by the subject about itself.
- **[E3-03](2) DECIDED BY THE FILER'S OWN ITEM 1.** *"We also compete on pricing, particularly in
  certain lower-margin industries"* (every 10-K since FY2022), and *"our adjustments typically
  lag behind the impact of inflation ... We may be unable to fully adjust our pricing."* [E4-37]'s
  prayer-session end. The one price action on record was a 2023 recovery of interchange
  inflation, taken with a lag. Half two of [E2-44] passes outright - capital 3.1% of revenue,
  PP&E $0.9M, $378M net cash, units up 4.95x on $150M of cumulative capital.
- **THE INDUSTRY MAP CAME FROM A PEER, NOT THE SUBJECT.** Paymentus names no competitor. ACI
  Worldwide's 10-K names nine (*"Alacriti, FIS, Fiserv, InvoiceCloud, Kubra, One Inc., Paymentus,
  PayNearMe, Repay"*); Repay names six and **impaired that segment by $254.7M in 2025** citing
  peer multiples; Fiserv and FIS name nobody. Row of 8, four private named as a hard limit,
  EngageSmart (InvoiceCloud) carried from its last 10-K (FY2022, +40.5% growth, faster than
  Paymentus) and italicised. On its own net top line Paymentus earns 19.6% against the
  "legacy" incumbents' 24-28%.
- **[E2-49] FIRES - the operator's prior is now 2 for 6.** The biller count (1,300 / 1,700 /
  1,900 / 2,200 / 2,500 over five vintages, growing ~14% a year) is absent from the FY2025 10-K,
  replaced by *"tens of thousands of billers"* through IPN partners. Net revenue retention has
  never been filed. The vertical mix appeared once, in the prospectus.
- **THREE FLAGS, ONE MECHANISM, AND IT WAS NOT THE IPO.** `STEP UP 4.25`, `EARLY HALF STRADDLES
  ZERO`, `ONE YEAR CARRIES THE WINDOW`: the OE sign change (2021-2022) is capitalised software
  ramping $14M to $30M against an OCF flat at $19-20M while G&A doubled - the cost of becoming
  public, not pre-monetisation; the 2025 step ($64M to $162M OCF) is one-third a **$60.8M
  receivables swing** (-$43.6M in 2024, +$17.1M in 2025). Years chosen **2023-2025**; the five-year
  window carried. Rebuilt width $21.4M to $106.4M - the fifteenth consecutive run to find the
  published width understated; here the capex band is $4M wide and the whole width is the window.
- **THE CUSTOMER-FUNDS PRIOR WAS REFUTED.** $215.7M of payer money sits in custodial accounts
  at PayPal's Braintree and the sponsor banks, *"not included in the Company's consolidated
  balance sheets."* OCF is not float-flattered. What moves it is receivables, and *"one reseller
  accounted for more than 10% of accounts receivable"* - the warrant note identifies JPMorgan
  Chase as the partner with revenue minimums through 2026.
- **[E4-29] READ CLEAN IN THE 10-K'S KPI LIST AND FIRED IN THE RELEASES, the CGNX rule again.**
  *"record adjusted EBITDA margin 41.3%"* is adjusted EBITDA **over contribution profit** - a
  non-GAAP numerator over a non-GAAP denominator; on GAAP revenue 13.5%, GAAP net margin 7.1%.
  Three of four bonus metrics non-GAAP; eight consecutive beat-and-raise releases; a $34.2M
  one-time RSU to an 18% founder *"to address the fact that he had not previously been awarded
  any RSUs"*, 480,000 more nine months later, a discretionary 20% on top of the formula bonus;
  no performance-based equity; no pay ratio (EGC exemption). Recorded, not adjudicated.
- **SBC/OCF 11.5%, the lowest in the calibrated row** (CRWD 68.0 . PINS 68.6 . QLYS 24.9 . CRM
  23.4 . SHOP 22.1 . **PAY 11.5**). The subtraction uses the cash-flow add-back (18.6), not the
  total expense (20.8), because $2.2M of SBC is capitalised into the software line the run also
  subtracts - `tools/run.py` uses the larger tag and double-counts.
- **THE CAP, SEVENTH INSTANCE.** `cap_m 3635` = $35.13 x **103,479,239**, the 2020-12-31
  pre-IPO `CommonStockSharesOutstanding`; understated 20.4%. New wrinkle for the guard: the
  FY2021 10-K re-tagged the 2020 value in March 2022, so the 550-day clock ran from the re-tag
  date, not the period date.
- **Strongest fact against:** JPMorgan Chase, U.S. Bank and PayPal resell the platform rather
  than build; JPM signed minimums and took warrants. Answered in the run: the reseller holds
  the customer and is paid in equity and revenue share, and is the one party over 10% of AR.
- **Brief defects:** "fraction of a billed dollar" is unanswerable (no dollar volume filed);
  NRR does not exist here; the PINS framing fits loosely. **Tooling defects:** the pre-IPO count
  (7th); `run.py`'s SBC tag; `run.py`'s fall-through to the diluted weighted average;
  `S.cik_for` returns None for FI (SEC map says FISV) and for delisted filers.

"""
old_count = "### THE STANDING COUNT — 63 WATCHLIST RUNS\n**Gate-clearers, failed at Q5 (24)** · **Q2 OUT (37):** + **CORT** ·"
new_count = "### THE STANDING COUNT — 64 WATCHLIST RUNS\n**Gate-clearers, failed at Q5 (24)** · **Q2 OUT (38):** + **CORT**, **PAY** ·"
if "PAY FOLDED IN" not in t:
    assert old_count in t, "standing count block not found"
    t = t.replace(old_count, fold + new_count, 1)
    open(r, "w", encoding="utf-8", newline="\n").write(t)
print("reading list ok")
