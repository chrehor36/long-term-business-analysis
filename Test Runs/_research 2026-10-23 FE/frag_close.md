## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED (Q5 closed the file). Facts found are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The reporting figures are computed under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q5, integrity, on doubt** **[M2013-088]**. Q1 IN, Q2 IN, Q3 weighs against, Q4 weighs against; Q6 to Q12 not
reached. COMPUTATION beside the price (not a clearance): the value range is the no-growth case alone, **-$14.77 a share**
on the equity-only basis (central for a regulated utility), against **$46.49**; fair price **-$7.81** equity-only and
**-$57.55** all-equity. No case of the range, nor any variant shown beside it, earns the floor at the price, so the file
would have closed OUT at Q7 had it reached it.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.

**Q6, the money and the owners.**
- Retention: retained earnings were $-1,605M at 2021-12-31 and $35M at 2025-12-31; common dividends paid 2021-2025 were
  $4,632M against earnings attributable to FE of $4,789M (cash-flow statements and XBRL, FY2023 and FY2025 10-Ks). Over the
  same years FE raised $6,848M of equity: $1,000M of common stock in 2021, $2,348M net from the sale of 19.9% of FET in 2022,
  and $3,500M from the sale of a further 30% of FET in 2024 (same). The 10-K plans further common equity "averaging
  approximately 1% of its now current market capitalization in each year" of 2026-2030 (Item 7). Shares outstanding rose
  from 442.3M (2016) to 578.6M (2026-06-30), 31% (XBRL; 10-Q cover).
- Buybacks: none in 2021-2025 (no repurchase line in the financing sections, FY2023 and FY2025 10-Ks). The bottom of the
  Q7 range below is -$14.77 a share, so no price paid could have sat at or below it. *(The Q6 buyback line the brief asks
  to write back with Q7: no buyback to test.)*
- Issuance and deals: 49.9% of FET, the transmission holding company of the Stand-Alone Transmission segment, is now
  Brookfield's (Item 1); FE receives its share through FET's distributions and its special interest in MAIT's Class B
  distributions (Item 1). The serial-issuer row **[L2014-015]** is the candidate second STOP of Q6, unresolved in the
  framework's section VI. No all-stock acquisition in the window.
- Part B: CEO total compensation for 2025 $13,452,559 (DEF 14A); the CEO chairs the board; the mid-cycle change of the LTIP
  KPI from Operating EPS to Core EPS (Q5, item 5).

**Q7, COMPUTATION, NOT A CLEARANCE** (script and output: `q7.py`, `q7_output.txt` in the research folder).
- **Basis.** The deciding part (Distribution, Q2's parts table) earns a return a regulator allows on its invested capital,
  so the equity-only basis is central and the all-equity basis is beside (Q7, The regulated utility, **[L2017-012]**,
  **[M2010-037]**). Owner cash after interest and after the company's own tax: operating cash flow (cash taxes and interest
  already paid), less stock issued under the plans, less capital investments and asset removal costs, less distributions
  to the FET minority, plus the long-term debt raised over the window to fund the fixed assets, capped at the regulator's
  allowed debt share.
- **The window**, 2021-2025, from the filed statements (2021-2022: FY2023 10-K `0001031296-24-000008`; 2023-2025: FY2025
  10-K `0001031296-26-000046`), $M:

  | | 2021 | 2022 | 2023 | 2024 | 2025 | sum |
  |---|---|---|---|---|---|---|
  | operating cash flow | 2,811 | 2,683 | 1,387 | 2,891 | 3,700 | 13,472 |
  | less Ohio restitution accrued in 2025, paid 2026 | | | | | -275 | -275 |
  | less stock issued under the plans | -50 | -98 | -89 | -74 | -60 | -371 |
  | less capital investments | -2,487 | -2,848 | -3,356 | -4,030 | -4,705 | -17,426 |
  | less asset removal costs | -226 | -213 | -274 | -305 | -376 | -1,394 |
  | less distributions to the FET minority | 0 | -21 | -72 | -86 | -100 | -279 |
  | plus net long-term debt raised (issued less redeemed) | 1,568 | -2,305 | 2,613 | -660 | 2,796 | 4,012 |
  | **equity-only owner cash** | **1,616** | **-2,802** | **209** | **-2,264** | **980** | **-2,261** |

  The credit: net long-term debt raised over the window $4,012M, against a cap of $9,184M (48.8% of the $18,820M of capital
  investments and removal costs). 48.8% is "a hypothetical capital structure of 48.8% debt" in the PUCO's order of
  2025-11-19, the only allowed debt share the 10-K states for any jurisdiction; FE's own debt share of capital at 2026-06-30
  is 67% ($28,983M of borrowings against $14,426M of total equity, 10-Q). The cap does not bind under either. The 2025
  restitution is charged in the year it was recognized because the cash left in 2026 (10-Q, H1 operating cash flow), the one
  adjustment to the filed operating cash flow; the 2021 DPA penalty, the 2023 $750M pension contribution and the 2024 SEC and
  Ohio settlements are left in their years as real costs of the business as run (Q4).
- **Central: -$452M a year, -$0.78 a share** (window mean, debt credited at the window total).
- **The specifics, in order.** (a) Cycle base: neither end year is described by the filer as aberrational; the literal window
  is the base, and is the only one shown. (b) Decline and sign: the series changes sign; between halves (2021-2022 mean
  -$593M, 2024-2025 mean -$642M) no compound rate has meaning; **the range is the no-growth case alone, said so**. (c)
  Acquisitions: none in the window; the 2025 sale of the Signal Peak stake ($47.5M at book) is immaterial. The FET minority
  sales are the filer's financing and equity transactions and are treated as equity issued, not as businesses sold
  (CONVENTION of this run; rationale: they are sales of a share of the deciding business's sister segment, booked by the
  filer as equity, and crediting $5.85B of one-time proceeds as negative capital spending would carry a sale that cannot
  recur into ten years of value, the absurdity **[M1999-067]** names). No signed unclosed deal; no deal after the window.
  (d) Working capital: inside operating cash flow as filed. (e) Maintenance: the filing names maintenance projects but gives
  no amounts, so the guess is not allowed in dollars; the depreciation variant is shown beside. (f) Cap: no growth is
  carried, so nothing to cut. The four PG specifics: the series is aggregate, not per share; all spending is deducted;
  zero growth after year ten is moot; a price above the top closes OUT.
- **The floor, tested first** (Q7): at $46.49 the floor needs about $2,690M a year of owner cash on the equity (10% of
  $26,901M). No case earns it. **Value range: -$14.77 to -$14.77 a share** (the no-growth case at the 5.29% sovereign,
  equity-only), against $46.49: OUT by the floor whatever the width.
- **Beside, never deciding.** (i) The debt credited each year at the allowed share instead of the debt actually raised:
  $582M a year, $1.01 a share, worth $19.02 at the sovereign and $10.06 at ten percent; about 2.2% at the price. (ii)
  Depreciation in place of all capital spending, no debt credit: $1,033M a year, $1.78 a share; halves growth 1.28% a year;
  worth $33.74 (no growth) to $37.39 (that growth) at the sovereign, $17.85 to $19.47 at ten percent; about 3.8% to 5.2% at
  the price. (iii) A stricter minority charge (the minority's $251M share of 2025 income in place of the $100M it was paid)
  would lower every case. (iv) **All-equity basis**: owner cash before interest (interest paid $5,169M over the window,
  added back after tax at the 21% federal rate, a statutory rate and said so) is -$438M a year; net debt at 2026-06-30
  $28,920M ($28,983M of borrowings, finance leases inside "other long-term obligations", less $63M of cash; restricted cash
  and operating leases left out); value at the sovereign -$64.28 a share.
- **The two reporting figures** (a reporting convention, not a rule; nothing here is a verdict or entry language): **(a)
  value range -$14.77 to -$14.77 a share** (the no-growth case alone, equity-only, central for a regulated utility); **(b)
  fair price -$7.81 a share equity-only (central)**, with **-$57.55 a share on the all-equity basis** beside; each end case
  valued at ten percent and the two averaged (here one case), after the company's own tax.

**Q8.** The sovereign pays 5.29%; the central equity-only owner cash yields -1.7% at the price, the most generous variant
about 5.2% **[M1997-089]**.

**Q9, debt and exposures.**
- Borrowings $28,983M at 2026-06-30 against common equity of $12,935M (10-Q); "approximately $6.8 billion of external FE
  holding company debt" at 2025-12-31 (Item 1); a $750M term loan "with a maturity date of April 27, 2027" drawn to repay
  short-term borrowings, short-term borrowings of $1,376M, and a covenant "to maintain a consolidated interest coverage
  ratio of not less than 2.50 times" (10-Q). On the rows' definition, pre-tax earnings over interest **[L2012-002]**: 2025
  income before tax $1,559M (net income $1,271M plus income taxes $288M) and interest expense $1,217M give (1,559 + 1,217)
  / 1,217 = 2.3 times (FY2025 10-K).
- Exposures: the securities class action, probable loss not estimable (10-Q); a failure to comply with the DPA "may also result
  in a breach of certain covenants contained in our credit agreements and could result in an event of default" (Item 1A); the PJM capacity-price pressure on bills and on regulators (Item 1A).
- The "little or no debt" criterion **[R1997-001]** is not met (it is a STOP for a whole business only).

**Q12.** The filings read describe HB 6 as legislation FE lobbied for, and the money as "53 payments totaling approximately
$75 million made in support of the passage of HB 6 and subsequent referendum efforts" (PUCO audit, FY2025 10-K); the
front-page test is the row's **[M2016-033]**. Recorded, not weighed.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `4da61af1`); written question by question; committed after each
      (Step 0 to Q1, Q2, Q3, Q4, Q5, the close).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the run binds
      only once folded into the register by that session (operator rule ten).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; one listing of `Test Runs/` to
      confirm the dated name was free showed five other names' file names, and the session context showed commit subjects
      about the ES run; both are declared under CONTAMINATION at the top and were not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; every quoted fragment beside an id is in its row
      (`check_ids.py` in the research folder); every filing fact carries its document and accession; no E-id.
- [x] The order was kept; Q5 was the first STOP that failed and closed the run; everything after it is NOT REACHED or
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (stock pay, removal costs, the minority's cash, the HB 6 penalties and settlements
      kept in), never a net-income proxy; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, Q5's other side); the facts for later questions are under
      AFTER THE STOP.
- [x] Not a point-in-time run; no anchor bar applies.
- [x] Only the arithmetic lines of `tools/run.py` were used; its stock pay ("n/f"), its capex (without removal costs) and its
      depreciation were each read against the filing (Step 0).
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The regulated utility's debt credit** says "the long-term debt raised over the window to fund the fixed assets" but
not whether that is gross or net of redemptions, nor how to treat debt repaid out of equity proceeds. At FE the equity sales
of 2022 and 2024 ($5.85B for 49.9% of FET) repaid debt, so the net debt raised ($4,012M) is far below the allowed share of the
spending ($9,184M) and the central owner cash is negative; crediting at the allowed share instead (variant (i)) gives $582M a
year. I used the window's net long-term debt, as the words read most naturally, and showed the other beside; the box does
not turn on it, since neither earns the floor. (2) **Specific (c)** names businesses bought and sold, not a sale of a
minority stake in a consolidated subsidiary; I treated FE's FET sales as equity issued (the filer's own classification) and
confessed it as a CONVENTION of this run. (3) **Q5 and successor management**: the framework applies integrity "on doubt
alone" but says nothing of how far an institution's admitted crime attaches to the managers who follow, or of when such a
record is spent; I judged the doubt from the filings (officers then in place still in place, three directors from the
period, present habits) and stated the other side's case, but another analyst could weigh the 2020 dismissals more heavily
and pass Q5; the box would then have been decided at Q7, also OUT. (4) **The parts table** asks for five-year shares, but
FE re-cut its segments in 2024 and reports the present three for 2023-2025 only; I used three years. (5) The template's
box line clause "integrity facts recorded, not judged" covers a file closed before Q5 and has no wording for a file closed
at Q5 itself; I gave none.
