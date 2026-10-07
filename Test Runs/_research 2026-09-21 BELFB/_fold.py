# -*- coding: utf-8 -*-
import io

QP = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\WATCHLIST RUN QUEUE.md"
s = io.open(QP, encoding='utf-8').read()
marker = "## COMPLETED FROM THE QUEUE\n"
i = s.index(marker) + len(marker)

entry = u"""- **BELFB (Bel Fuse Inc.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 18 of 218. Register entry 150** (re-derived, not inherited: line-start
  `^- \\*\\*` counted **by index** in the slice from this file's `## COMPLETED FROM THE QUEUE`
  heading line (line 502) to `## THE WRITE-EARLY PROTOCOL` (line 11931). **149 entries stood above
  this one**, which agrees with the dispatcher's count of 149 at 06:47 and with the BLMN entry
  directly below claiming 149 for itself. After insertion: 150. No BELFB or BELFA entry existed
  anywhere in the slice.)
  **TWO CLASSES, TWO QUOTES, AND THE CAP HAD TO BE BUILT FROM BOTH.** **Price BELFB US$241.97 and
  BELFA US$198.83**, both closes of 2026-09-18, aggregator (Yahoo Finance chart endpoint),
  **flagged as an aggregator, live quote only**. **Shares 2,115,263 Class A and 12,324,187 Class B,
  total 14,439,450**, hand-read from the **cover of the 10-Q for the quarter ended 2026-06-30,
  accession `0001437749-26-025619`, filed 2026-08-04**, "Number of Shares of Common Stock
  Outstanding as of July 31, 2026", and cross-checked against the filed balance sheet in the same
  10-Q. Split factor after the measurement date is **1.0** on both tickers.
  **CAP, STRUCK BY HAND: (2,115,263 x $198.83) + (12,324,187 x $241.97) = $420.6M + $2,982.1M =
  $3,402.7M.** The screen carried **541**. **THE SCREEN IS WRONG BY 6.29x AND THE BRIEF'S PRIOR IS
  REFUTED: IT WAS NOT A STALE PRICE.** `dei:EntityCommonStockSharesOutstanding` resolves
  **undimensioned exactly once in the whole companyfacts file** - `end 2011-08-01, val 2,174,912,
  form 10-Q/A, frame CY2011Q2I` - because every filing since tags it **dimensioned by class**. The
  screen's figure reproduces to the dollar as **$248.69 (BELFB close, 2026-08-28) x 2,174,912 =
  $540.85M**: the price was three weeks old and immaterial, and **the share count was both the wrong
  class and fifteen years stale.** `cap_m` is the denominator of `yield_bottom`, `vs_sovereign` and
  `growth_required`, so all three are void, in the direction that made the name look **6.29x
  cheaper** than it is; and the `acq_note`'s "acquisitions are $337M, 62% of cap" is really **9.9%
  of cap**.
  **Sovereign US$ 30-year 5.34% at 09/18/2026**, struck fresh 2026-09-21 from the **US Treasury
  daily par yield curve** (issuing authority; FRED not used). Earnings currency USD, no FX.
  **Anchor filing read: 10-K FY2025, period ended 2025-12-31, accession `0001437749-26-005354`,
  filed 2026-02-24.** Figure cross-checked by hand: FY2025 *"Net cash provided by operating
  activities"* **$80,612 thousand** on the filed statement, equal to the tagged fact. A second hand
  check was made on the FY2021 10-K (`0001437749-22-006139`) and a third on a **peer** (Amphenol's
  FY2025 10-K `0001104659-26-013549`, *"Operating income was $5,868.6, or 25.4% of net sales, in
  2025"*, which the peer-row construction reproduces).
  **FAIL AT Q2 - OUT ON THE BUSINESS, at [E3-03] criterion 2 (no close substitute), on the
  registrant's own Item 1 and Item 1A.** Item 1A: *"Our business operates in a globally competitive
  industry, **with relatively low barriers to entry.** ... our major competitors, many of which are
  larger than Bel, have significant financial resources and technological capabilities."* Item 1A
  again, first bullet of *There are several factors which can cause our margins to suffer*:
  *"**The average selling prices for certain of our products tend to decrease over their life
  cycles, and customers put pressure on suppliers to lower prices even when production costs are
  increasing.** Further, increased competition from low-cost suppliers around the world has put
  additional pressures on pricing."* Item 1: *"There are numerous independent companies and
  divisions of major companies that manufacture products that are competitive with one or more of
  our products."* **A customer who believes there is no close substitute does not extract falling
  prices from a supplier whose costs are rising.**
  **THE SEVENTEEN-YEAR SERIES IS WHAT MADE IT OUT RATHER THAN UNKNOWABLE.** Operating margin,
  FY2009-FY2025, all 10-K-tagged: `-9.5 / 5.0 / 2.5 / 0.6 / 4.3 / 2.8 / 5.0 / -15.3 / 3.5 / 4.9 /
  -0.3 / 4.0 / 5.8 / 10.0 / 13.8 / 12.0 / 16.4`. **Thirteen of seventeen years below 6%, two
  negative, and no year above 5.8% before 2022.** ROE on the same seventeen years averages **4.0%**
  (**[E2-01]**), against **15.9%** for FY2021-25. **[E2-53]**'s dominance test - *"Once dominant,
  the newspaper itself, not the marketplace, determines just how good or how bad the paper will be.
  Good or bad, it will prosper"* - is the gate that fails: for thirteen of seventeen years Bel did
  not prosper, so position never set the economics. **[E2-58]** supplies the class and the filing
  prices it: **raw-material expedite fee revenue of $14.9 million in FY2023 against $0.1 million in
  FY2024** is a supply-tight year paying and then not paying.
  **COMPETITOR ROW [E3-28], ELEVEN PEERS, one construction applied identically, newest fiscal year
  and the five most recent** (workpaper:
  `Test Runs/_research 2026-09-21 BELFB/WORKPAPER - the competitor row.md`). GAAP operating margin,
  newest FY: APH 25.4% (`0001104659-26-013549`) / SXI 21.7% / VICR 20.1% / TEL 18.6% / **BELFB
  16.4%** / CTS 15.3% / AEIS 9.3% / ALNT 7.9% / RFIL 2.2% / VSH 1.9% / LFUS 1.6% / MEI 0.9%.
  **Five-year minimum operating margin is the line that decides it: APH 19.4% and TEL 14.4% - both
  above BELFB's BEST of seventeen years - against BELFB's five-year minimum of 5.8%.** Same
  industry, same customers, same five years, so **[E3-61]** cuts the useful way: the row cannot show
  conduct, and that is precisely what takes the environment off the table as a defence.
  EBIT on unleveraged net tangible assets **[E2-43]**, same construction: CTS 43.8%, **BELFB 39.2%**,
  TEL 39.1%, APH 37.8%, ALNT 17.0%, VICR 11.5%, AEIS 8.0%, RFIL 7.2%, LFUS 2.6%, VSH 2.0%, MEI 1.4%
  (SXI n/a, it does not tag `Liabilities` undimensioned). **One disclosure gap stated and not
  papered over: TDK, Murata, Delta, Yageo and Sumida are not SEC registrants**, and they are the
  main competition for Magnetic Solutions (13% of 2025 sales); Molex, Pulse, Halo, Bourns and Samtec
  are private. The gap does **not** hold the moat class PROVISIONAL, because the verdict rests on
  the subject's own filed statements about its own pricing. **Bel's DEF 14A peer group
  (`0001437749-26-011998`) was read and NOT used as a competitor list** - it is a pay-and-talent
  group by its own words and it contains Northwest Pipe Company, which makes steel water pipe; the
  four genuine product competitors on it (CTS, SXI, RFIL, ALNT) are all in the row.
  **Q3 AND Q4 RECORDED BELOW THE GATE under an explicit banner and ARE NOT CLEARANCES. Q5 AND Q6
  NOT OPENED** (operator rule 2). No yield, no value range, no ranking position and no floor
  computation appears anywhere in the file; all below-gate arithmetic is headed **COMPUTATION - NOT
  A CLEARANCE**.
  **THE STANDING 8-K EX-99.1 INSTRUCTION EARNED ITS PLACE AGAIN, AND WITH A NEW EDGE.** The
  **10-K reads clean on [E4-29]**: EBITDA appears ten times and **every one is contractual**. The
  **furnished 8-K EX-99.1 of 2026-07-29 (`0001437749-26-024893`) does not**: headline bullet
  *"Adjusted EBITDA of $48.9 million (23.2% of sales)"* against a filed income from operations of
  **$38,419 thousand** and GAAP net earnings attributable to Bel shareholders of **$25,480
  thousand**; non-GAAP net earnings **$39.1M UP 86%** in the same bullet as GAAP **$25.5M DOWN 5%**;
  and the release's own subtitle is *"Provides Q3-26 Sales and Gross Margin Guidance"* (**[E4-22]**
  third flag, **[E5-30]**). **The new edge: EBITDA is not only the narrative metric here, it is the
  CONTRACTUAL one.** The 10-K discloses that the Enercon redemption value *"is calculated based on a
  pre-determined multiple of trailing twelve-months EBITDA"* and that the earnout turns on *"certain
  specified EBITDA targets"* - so the measure that deletes already-spent depreciation (**[E5-41]**'s
  *"reverse float"*) is the measure that sets what Bel pays for the remaining 20% of Enercon.
  **THREE PRIORS REFUTED, ONE CONFIRMED-BUT-INVERTED.** (1) **The cap prior is refuted**: not a
  stale price, a wrong-class fifteen-year-old share count (above). (2) **The `wc_note` reading is
  refuted while its arithmetic is upheld.** Read by hand off the FY2021 10-K, accounts payable
  **+$23,961** against OCF **$4,632** is **517.3%**, so the ratio is right - but the same statement's
  working-capital block nets to a **DRAIN of $36.1 million** (AR -12,982, unbilled -14,140,
  inventories -34,005, other current -2,240, other assets -1,182, AP +23,961, accrued +4,684, other
  liabilities +1,441, taxes -1,510). **The payable did not make the cash; it partly offset a block
  that consumed seven times the year's operating cash.** The flag catches overstatement and this was
  understatement. **A live instance in the flag's own direction does exist and is newer than its
  data: H1 2026 shows accounts payable +$33,072 against operating cash of $31,762 - 104%.**
  (3) **`level_note` STEP UP, `level_note_oe` EARLY HALF STRADDLES ZERO and `flags_disagree` are all
  three CONFIRMED on the rebuilt seventeen-year series**, and they disagree for a diagnosable
  reason: the ratio is being taken on a series that crosses zero, which is the same defect class
  already fixed once in `level_shift` for the RECENT half (RESUME STATE item 3A) - **here it is the
  EARLY half that crosses zero and the guard does not refuse.** **[E4-41]** was then applied and
  three favourable exogenous breaks were named and are removable: the **$14.9M FY2023 expedite
  fees**, a **$10.1M FY2025 foreign exchange revaluation gain**, and **gains on disposal of PP&E of
  $5,701 thousand (FY2025) and $6,440 thousand (FY2021)**.
  **THE SCREEN'S OWNER-EARNINGS BAND REPRODUCES; ONLY THE CAP DOES NOT.** Rebuilt by hand over
  **all seventeen filed years** as the `spread_caveat` ordered: OCF less SBC less (c), $M -
  3y **70.3 / 64.2**, 5y **46.5 / 40.2**, 7y **40.4 / 33.4**, 10y **32.1 / 23.7**, 15y
  **27.8 / 19.6**, **17y 26.2 / 18.3** (capex end / D&A end). The four-construction min and max are
  **40.2 and 70.3** against the published **40 and 70**. Spread ratio comes out **0.747** against
  the published **0.734**, a difference not diagnosed and not material.
  **THE (c) JUDGMENT, DISCLOSED [E2-23]: the corpus default runs BACKWARDS on this filer.**
  **[E3-44]**'s D&A default and **[E5-20]**'s upward exception both assume D&A tracks renewal. Bel's
  capex is **$12.0M on $675.5M of sales (1.8%)** while D&A is **$26.6M**, and FY2025's D&A jumped
  from $16.5M because it now carries purchase-accounting amortisation of Enercon's acquired customer
  relationships and technology ($217,966 thousand of intangibles). **Amortising a bought customer
  list is not "capitalized expenditures for plant and equipment ... that the business requires to
  fully maintain its long-term competitive position and its unit volume."** (c) is judged at or near
  **total capex, $12-14M**, and the D&A end is the conservative display rather than the valid one -
  the mirror image of the railroad case.
  **PERIMETER, named from the filings**: 80% of **Enercon for $325.6M cash, closed 2024-11-14**
  ($85.6M from cash, ~$240M from the revolver), contributing **$136.6M of FY2025 sales against
  $20.8M of FY2024**; **EOS Power $7.8M (2021-03-31)**; **rms Connectors $9.0M (2021-01-08)**;
  **one-third of innolectric, EUR 8.0M (2023-02-01), written to zero in Q4 2025**; **Czech Republic
  business sold in 2023**. **FY2025 is the first year on the current perimeter and it is one year.**
  **BALANCE SHEET, and it changed inside the window**: long-term debt **$287,500 -> $197,500 -> $0**
  thousand at 2024-12-31, 2025-12-31 and 2026-06-30; cash **$306,106 thousand** at 2026-06-30 against
  $57,800 six months earlier; redeemable noncontrolling interest **$102,601 thousand** (the Enercon
  20%, accreting on a trailing-EBITDA multiple, intended for purchase *"by early 2027"*). The change
  is a **follow-on of 1,500,000 Class B shares at $266.00 plus a 225,000-share over-allotment**
  (8-K `0001213900-26-056732`), **net proceeds $441.6 million**, used to retire the revolver.
  **[E5-15]**'s serial-issuance flag was read and **does not fire**: one marketed offering, priced
  **above** today's quote, retiring all debt, is **[E5-24]**'s first law applied correctly to the
  company's own paper.
  **[E4-39]'S RARE-POSITIVE TELL FIRES, IN ITS NEGATIVE FORM.** The 8-K of 2025-12-03
  (`0001437749-25-036765`, Item 2.06) publishes the post-mortem on Bel's own EUR 8.0M innolectric
  investment, names the causes, records that Bel *"ultimately determined not to invest further
  capital"* rather than doubling down, and quantifies the loss - **$13,087 thousand** charged in
  FY2025. Auditor change Grant Thornton to Deloitte (8-K `0001437749-25-037380`, 2025-12-10) carries
  Item 304's express **no disagreements and no reportable events**; recorded, not scored.
  **TOOLING DEFECTS FOUND, REPORTED NOT PATCHED (three).** (1) **The share-count denominator has a
  two-class hole.** Whatever reads `dei:EntityCommonStockSharesOutstanding` undimensioned returns a
  2011 Class A count for this filer and **does not refuse**, which is the failure mode the SBC fix
  of RESUME STATE item 3F was built to end (`sbc.get(e, 0.0)` returning a plausible zero). **A guard
  that returns a plausible number on a dimensioned tag is worse than no guard.** The cheap test is
  the one the row's own `cap_flag` already performs: **cap against `dei:EntityPublicFloat`** - it
  fired here and it was right, and **it should refuse rather than annotate.** (2) **`level_shift`'s
  zero-crossing guard still only covers the recent half** (item 3A fixed one side; the early half
  produced this row's `flags_disagree`). (3) **No tool reads a multi-class cover**; the count has to
  be read by hand, and that should be written into the queue's standing method for dual-class
  filers, of which this is the first in Wave 7.
  **NO ALERT ARMED AND NO PORTFOLIO ROW** - a name that failed on the business gets a reversal
  condition in words (the QLYS ruling), and **price is not a reopening condition at any level
  [E5-35]**: **a 10-K Item 1A that no longer says "relatively low barriers to entry" and no longer
  carries the Declines in Selling Prices bullet; an MD&A that attributes a margin gain to PRICE
  rather than to facility consolidations, mix and exchange rates ([E4-37] read forward); and a
  competitor row in which Bel's operating margin clears Amphenol's five-year minimum of 19.4%
  through a supply-AMPLE year.** Two consecutive 10-Ks meeting all three would be a new question,
  not a re-run of this one.
  `check_framework.py` PASS, and separately **83 distinct ledger ids cited with ZERO phantom**
  against the ledger.
  Run file: `Test Runs/2026-09-21 Run - BELFB Bel Fuse.md`.
"""

s = s[:i] + entry + s[i:]
io.open(QP, 'w', encoding='utf-8').write(s)
print("register entry inserted")

WP = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\_daily\_wave7_done.txt"
t = io.open(WP, encoding='utf-8').read()
if not t.endswith("\n"):
    t += "\n"
t += "BELFB\n"
io.open(WP, 'w', encoding='utf-8').write(t)
print("wave7_done appended")
