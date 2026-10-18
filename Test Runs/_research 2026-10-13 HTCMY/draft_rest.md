
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file OUT). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten years of balance sheets were read in Step 0; other facts are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts are recorded under AFTER THE STOP, not judged.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts, including the buyback against the bottom of the computed range, are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's two reporting figures are computed below under **COMPUTATION, NOT A CLEARANCE**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (Nothing in the filings places the business among the named ones.)

---
## COMPUTATION, NOT A CLEARANCE — the value range and the fair price (the owner's reporting figures)
*Computed beneath a closing STOP at Q2. These figures decide nothing, carry no entry language, and are not a verdict
(operator rule 3). Scripts and outputs: `owner_cash.py`, `valuation.py`, `owner_cash_out.txt`, `valuation_out.txt` in the
research folder.*

**Owner cash after every real cost** (operating cash, less capital expenditure net of disposal proceeds, intangible assets,
lease principal paid, and distributions to non-controlling interests; acquisitions shown separately; the all-equity
figure adds back net interest paid after the 30.6% statutory rate). Millions of yen; FY starting April.

| FY | Operating cash | Net capex + intangibles | Lease principal | To NCI | Owner cash, equity | Owner cash, all-equity | Acquisitions, net | All-equity after acquisitions | Revenue |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 87,961 | 15,305 | 5,556 | 7,862 | 59,238 | 59,905 | 59,877 | 28 | 753,947 |
| 2017 | 84,528 | 16,748 | 4,700 | 2,103 | 60,977 | 62,740 | 20,947 | 41,793 | 959,153 |
| 2018 | (25,693) | 29,516 | 6,388 | 4,933 | (66,530) | (64,565) | 997 | (65,562) | 1,033,703 |
| 2019 | 22,682 | 36,404 | 12,770 | 5,544 | (32,036) | (28,679) | (1,635) | (27,044) | 931,347 |
| 2020 | 91,339 | 32,815 | 11,534 | 4,255 | 42,735 | 44,977 | (569) | 45,546 | 813,331 |
| 2021 | 39,317 | 25,617 | 12,699 | 8,857 | (7,856) | (5,802) | (18,920) | 13,118 | 1,024,961 |
| 2022 | 27,344 * | 47,201 | 11,745 | 9,316 | (40,918) | (36,713) | 68,311 * | (105,024) | 1,264,927 |
| 2023 | 73,035 | 54,887 | 12,890 | 6,747 | (1,489) | 6,436 | (15,289) | 21,725 | 1,405,928 |
| 2024 | 143,932 | 42,762 | 15,040 | 9,213 | 76,917 | 85,757 | 13,719 | 72,038 | 1,371,285 |
| 2025 | 164,223 | 47,865 | 13,479 | 10,574 | 92,305 | 99,543 | (861) | 100,404 | 1,405,493 |

\* FY2022: the ¥53,479M paid as guarantor of ACME's loans is moved from operating cash to acquisitions, since it ended in
the purchase of ACME (60th report, business combinations); it is deducted either way in the default pair. Operating cash
includes the rental fleet ("other property, plant and equipment [...] principally operating assets for leasing", 62nd
report note 10), bought at ¥82,249M (FY2024) and ¥64,417M (FY2025) outside the capital-expenditure line.

**The inputs.** Long government rate 4.085% (MOF, 2026/10/9). Shares 206,761,281. Net debt on the all-equity basis: bonds
and borrowings ¥498,549M less cash ¥130,831M at June 30, 2026 (the latest filed balance sheet) = ¥367,718M, **plus
¥33,999.9M** paid for the 5,999,100 shares repurchased after that date (CONVENTION of this run: the share count already
reflects the repurchase, so the cash that bought it is added; rationale: both sides of the per-share figure at one date).
Lease liabilities (¥73,684M) are left out because lease principal is charged in owner cash, and said so. Net debt used:
**¥401,718M**. Enterprise value at the price: ¥1,560,822M.

**The range, built by Q7's convention in full.**
- *Base:* the last five years, FY2021 to FY2025. (a) Neither end year is aberrational on the filer's own description; the
  one aberration inside the window (the ACME guarantee) is moved to acquisitions. The ten-year average (two cycles) is shown
  beside.
- *All spending deducted, the literal window, acquisitions deducted* (specifics (c) default pair, (d) working capital
  counted): owner cash, all-equity, after acquisitions averaged **¥20,452M**. (b) The series changes sign (13,118;
  (105,024); 21,725; 72,038; 100,404); the halves of the window (first two years averaging ¥(45,953)M, last two ¥86,221M)
  also change sign, so the growth is meaningless and this leg is the no-growth case alone, said so. Aggregate, not per share
  (PG specific 1).
- *Not a serial acquirer:* net purchases over the window ¥46,960M against half of owner cash before purchases (¥149,221M,
  half ¥74,611M). No signed, unclosed acquisition was found; the planned sale of ECCO Equipment Company, LLC (a divestiture,
  62nd report note 20) is not valued. The organic pair is shown beside.
- *(e) The maintenance case:* the filer states no maintenance figure; the rows' proxy is taken, "the depreciation charge is
  not inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**, as a disclosed
  guess **[M2000-144]**: net income to the parent, the equity-method share replaced by the dividends received (Q4's
  convention), with net interest after tax added back for the all-equity basis: FY2021 to FY2025 73,135; 81,065; 99,105;
  88,701; 79,432; average **¥84,288M**. This is the maintenance-only case the specific orders, shown beside the owner-cash
  figure, not a net-income proxy for owner cash (operator rule 5): the owner cash is the bottom of the range.
- *The growth bought was worth less than its cost.* Growth spending (the gap between the maintenance case and owner cash
  before acquisitions) totalled about ¥272,217M over the five years, and the maintenance-case earnings rose by ¥6,297M a year
  (73,135 to 79,432), about 2.3% on the spending, below the 4.085% long rate. So, by (e), the maintenance-only no-growth case
  is the **top** and the all-spending case the **bottom**; "growth can destroy value if it requires cash inputs in the early
  years [...] that exceed the discounted value of the cash that those assets will generate in later years" **[L2000-023]**.
  (f) No growth is carried on either end, so the cap does not bind; zero growth after year ten (PG specific 3) is moot.

| Case | Owner cash a year | Value at 4.085% | Less net debt | Per share | Return at the price |
|---|---|---|---|---|---|
| Bottom: all spending, no growth | ¥20,452M | ¥500,666M | ¥98,948M | **¥479** | 1.31% |
| Top: maintenance only, no growth | ¥84,288M | ¥2,063,347M | ¥1,661,629M | **¥8,036** | 5.40% |
| Beside: ten-year average, all spending after acquisitions | ¥9,702M | | | ¥(794) | |
| Beside: organic pair, literal window, before acquisitions | ¥29,844M | | | ¥1,591 | |

**VALUE RANGE (a): ¥479 to ¥8,036 a share (all-equity basis), against ¥5,606.** The floor is tested first: at the price no
case earns about ten percent (the top case returns 5.40% on the enterprise value), so had Q7 been reached it would close
**OUT whatever the width** ("there’s just a point at which we drop out of the game" **[M2003-149]**). The width is 4.1 to
one on business value (above the three-to-one convention), which does not matter once the floor fails.

**FAIR PRICE (b), a reporting convention and never a verdict (Part VII):** each end valued at ten percent and the two
averaged, after the company's own tax. **All-equity (the central figure): ¥590 a share** (bottom end ¥(954), top end
¥2,134). **Equity-only, beside: ¥2,240 a share** (owner cash after interest, ¥14,400M bottom and ¥78,235M top, against the
market value alone; it never decides alone). For the record, with the filed net debt only (repurchase cash not added):
¥754. Against the price of ¥5,606. No other price figure is reported.

---
## THE BOX
**OUT at Q2** (the deciding part's castle protects only ordinary returns over a full cycle: after-tax return on capital
7.5% average FY2016 to FY2025; not the low-cost operator; the filer reports price competition). Integrity facts recorded,
not judged. COMPUTATION beneath the stop: value range ¥479 to ¥8,036 a share against ¥5,606 (no case earns the floor at
the price); fair price ¥590 all-equity, ¥2,240 equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; not weighed; no verdict; the box unchanged (operator rule 2).*

**Q3 (capital).** Owner cash after every real cost averaged ¥20,452M a year (all-equity, after acquisitions) over FY2021 to
FY2025 and ¥9,702M over ten years, against net income to the parent averaging ¥78,783M over the five; the difference went
into inventories (¥297,766M at March 2021 to ¥541,224M at March 2026), receivables and the rental fleet. After-tax return on
capital employed 2.4% to 10.3%, average 7.5% (`returns.py`). The growth spending of FY2021 to FY2025 earned about 2.3% on
its cost (computation above). Row about one named business in this industry, recorded for the later question it bears on,
not weighed: "There was never any cash. Just more used construction equipment." **[M2008-036]**.

**Q4 (the accounts).** Balance sheets: Step 0. The filer features "adjusted operating income" ("calculated by subtracting
the sum of cost of sales and selling, general and administrative expenses from revenue") as its performance indicator; it
excludes other income and expenses, which in FY2025 netted to ¥(2,807)M (adjusted ¥132,951M, operating income ¥130,144M) and
in FY2024 to ¥+9,741M (adjusted ¥144,989M, operating ¥154,730M), so it did not flatter in both years. The 60th report's plan
set "an EBITDA margin of 18% or more as an indicator of our ability to generate cash"; EBITDA in the filer's own mouth.
Compensation income from a supplier for the engine-certification violation, ¥16,826M (FY2024) and ¥9,786M (FY2025), against
related losses of ¥4,514M and ¥4,960M; insurance income ¥6,613M (FY2025) for a fire of July 4, 2024. Equity-method share
¥3,576M against dividends received ¥2,577M (FY2025). Restricted shares to executive officers (33,801 shares in FY2025). The
59th report's capital-expenditure table figure differs from its own text (Step 0).

**Q5 (the people): integrity facts, recorded, not judged.** (1) The company publishes earnings forecasts and revises them
(Q1 FY2026: revenue ¥1,470,000M, net income ¥84,000M, raised from ¥1,430,000M and ¥80,000M). (2) The adjusted-operating-
income figure featured as the performance indicator (Q4 above). (3) It states its misses plainly: FY2025 results against
the plan's targets, ROE 8.6% against "over 13%", the income ratio 9.5% against "over 13%". (4) The ACME episode: the
company guaranteed the bank loans of an equity-method affiliate (guarantee obligations ¥64,003M at March 2022), paid
¥53,479M when it defaulted, was "in dispute with ACME and its related parties", and settled in March 2024 by taking ACME
over and paying ¥2,019M "related to the resolution of a dispute". (5) Representative executive officer changed (notice of
February 27, 2026); not read further.

**Q6 (the money and the owners).** Dividends ¥175 a share for FY2025 (payout 50.9% against a 30% to 40% policy), ¥190
planned for FY2026. **The 2026 repurchase:** resolved August 18, 2026 for up to 6,420,000 shares or ¥34.0bn, completed
October 8 at 5,999,100 shares for ¥33,999,921,700, an average of about ¥5,667 a share; the stated reason was "to mitigate
the short-term impact of the aforementioned sale on the supply of and demand for the Company's shares" (Hitachi, Ltd.'s
sale of 21,462,310 shares); the resolution names a share count and an amount, not a price above which it stops. **The
buyback test's line, written back from the computation:** the prices paid (about ¥5,667) sit far above the bottom of the
computed range (¥479 a share), so under Q6's convention for a buyback with no stated price it would weigh against, had Q6
been reached. The new plan's "approximately ¥500 billion in funding for growth investments", with "strategically utilizing
financial leverage" and "inorganic growth" toward "one of the top three in the industry by 2030". Purchases of minority
stakes ¥19,022M (FY2022), ¥3,623M (FY2024); Brake Supply bought December 2024 (¥15,946M for businesses that year). Control:
ITOCHU holds about 33.4% directly and through HCJI Holdings (notice of February 19, 2026); HCJI may propose a director and
agreed to a five-year standstill from January 2022 (62nd report, Important Contracts).

**Q9 (debt and exposures).** Bonds and borrowings ¥498,549M at June 30, 2026, of which ¥323,331M current; net debt to
equity 0.40 on the filer's measure (FY2025). Interest expense ¥15,883M against income before taxes ¥124,226M (FY2025).
Guarantee obligations for borrowings ¥56,564M at March 2026, up from ¥42,791M a year earlier (62nd report note 29).
Sales-finance credit risk on installment sales and finance leases (Business Risks, item 5); lease receivables ¥38,137M at
March 2024. Retirement benefit liability ¥22,099M. A commitment line and credit line are maintained (liquidity note).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 9d7a24f1); written question by question; committed after each
      (Step 0 to Q1: a371894e; Q2: f7fecb59; this close: the next commit).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's; the fold is
      the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. **Declared under contamination** (header): a filtered
      listing of `Test Runs/` showed the name of a 2026-07-15 HTCMY run (not opened); a listing of the repository root
      showed the name `PORTFOLIO.md` (not opened). That root listing came from a backgrounded download command that lost its
      directory: it wrote two files of mine (`jgbcme.csv`, `results_index.html`) into the repository root, which I deleted
      at once (they were mine, untracked, never committed); three PDFs already in the root (`ar22.pdf`, `ar23.pdf`,
      `ar24.pdf`, not mine) were left untouched.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in its row (check script
      `check_ids.py` in the research folder); no E-ids. Filing facts carry their document and date (no accession numbers
      exist for this filer; the rivals' 10-K accessions are given).
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy: the range's bottom is owner cash from operating cash;
      the top is the maintenance-only case that specific (e) orders, built from earnings with depreciation as the disclosed
      maintenance guess **[M1998-127]**, **[M2000-144]**, labelled as such and never used as owner cash. Sovereign from the
      issuing authority (MOF). The price quote is an aggregator's, flagged.
- [x] Contrary evidence written down as found (foundations); the facts for later questions are under AFTER THE STOP with
      the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` produced no lines for this filer (not an SEC registrant); nothing it prints was used.
- [ ] `python tools/check_framework.py` PASS before the commit: see the result recorded below.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The ordinary-returns item of Q2 speaks of a field**, "a field whose durable players earn ordinary returns over a full
cycle". Here the field's leader earns well above the ordinary (Caterpillar's operating margin 13.7% against this
company's 8.8% over the same decade), and it is the deciding part's own castle that protects ordinary returns. I applied
the item to the part's own returns, together with the high-cost-producer item and the moat's definition **[L2007-004]**;
the text does not say whether one player's ordinary returns, in a field the leader shows is not ordinary, closes OUT under
that item or should be argued through the low-cost test alone. (2) **The all-equity net debt** is taken "at the latest filed
balance-sheet date with the subsequent events that filing itself states added"; a repurchase completed after the latest
filing and reported in later company notices is not covered, though the share count must reflect it. I added the cash
paid (a CONVENTION of this run) and showed the figure without it. (3) **IFRS 16** leaves no operating-lease category for a
lessee; the text's "operating leases left out" was read as all lease liabilities left out because lease principal is
charged in owner cash. (4) **Non-controlling interests** are not addressed in Q7; I deducted distributions to them from
owner cash and used net income to the parent in the maintenance case. (5) **Specific (e)'s "where the filing allows the
maintenance guess"**: the filing gives no maintenance figure; whether the depreciation proxy row counts as the filing
allowing the guess is unclear; I used it, disclosed, and the inversion made the maintenance case the top. (6) **Captive
sales finance**: the floor-plan convention covers notes secured by inventory, not borrowings that fund customers'
installment and lease receivables; I counted all borrowings as net debt. (7) **The fair price averages a negative end**:
the bottom end valued at ten percent is below the net debt (¥(954) a share); the definition averages it in as written.
(8) **A foreign filer under the template**: the template asks for accessions and a proxy; document names and dates were
used, and the governance section of the securities report was not reached. (9) A practical note: the dispatched brief
names a "plain browser User-Agent" for the IR site; it worked, and the MOF file needed none.
