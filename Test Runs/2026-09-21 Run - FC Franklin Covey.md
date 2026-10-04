# Company Run — FRANKLIN COVEY CO. (FC) — 2026-09-21
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**CIK 0000886206** · NYSE · Utah · SIC 8741 Services-Management Services · fiscal year ends
**31 August**. WAVE 7, name 12 of 218. Register entry 144 (143 counted before the insert;
see the fold). Unattended overnight run; every judgment below is mine and is cited.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

---
## STEP 0 — THE RATE, THE FILING, AND EVERY SCREEN FLAG RESOLVED BY HAND

**Sovereign, for the currency the business EARNS in** — currently observed, never a forecast
**[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** · source **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (struck fresh in this run through `tools/sources.py`; not
  inherited from the brief, not FRED).
- **Earnings currency ARGUED, not assumed.** FY2025 10-K Item 7: the Enterprise Division's
  three segments are *North America*, *International Direct Office* and *International
  Licensee*; consolidated revenue $267.1M, of which the Education Division ($74.6M, US and
  Canadian schools) is almost wholly domestic and the Enterprise Division ($188.1M) is led by
  North America. FX moved FY2025 consolidated revenue by **$0.2M on $267.1M — 0.07%**
  (*"In constant currency, our consolidated revenue was $267.3 million for fiscal 2025"*).
  **USD is the earnings currency on the filed evidence.**
- FX / ADR ratio: not applicable — US domestic filer, common stock on NYSE.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary document: Form 10-K for the fiscal year ended 2025-08-31, filed 2025-11-12,
  accession `0000886206-25-000085`** (`fc-20250831x10k.htm`).
- Also read: **10-Q for the quarter ended 2026-05-31, filed 2026-07-07, accession
  `0001193125-26-297572`**; **8-K/EX-99.1 earnings releases** of 2026-07-01
  (`0001193125-26-292604`), 2026-04-01 (`0001193125-26-137952`), 2026-01-07
  (`0001193125-26-006335`), 2025-11-05 (`0000886206-25-000080`), 2025-07-02
  (`0000886206-25-000046`); **8-K of 2026-09-01** (`0001193125-26-378449`, Item 5.02); the
  **8-K of 2026-06-17** (`0001193125-26-274239`, Item 8.01); **DEF 14A filed 2025-12-18**
  (`0001193125-25-324927`); and the 10-Ks for FY2010, FY2013, FY2016, FY2019, FY2021, FY2022
  and FY2024 (accessions tabled in Step 0 (iii)).
- **Figure cross-checked against the filed statement:** FY2025 **income from operations
  $5,704 thousand** (CONSOLIDATED INCOME STATEMENTS) and **total assets $242,912 thousand**
  against **total current liabilities $157,292 thousand** (CONSOLIDATED BALANCE SHEETS), giving
  capital employed **$85,620 thousand** — which reproduces the XBRL-derived series used in the
  competitor row below to the dollar.
- **EDGAR checked for anything filed since the brief was written, rather than trusting memory.**
  FY2026 ended 2026-08-31. **No FY2026 10-K and no FY2026 fourth-quarter earnings 8-K exists
  yet**; the newest filings on the index are the 8-K of 2026-09-01 (Item 5.02, executive
  changes) and Forms 3/4 of 2026-09-03 and 2026-09-09. Newest periodic remains Q3 FY2026
  (2026-05-31), as briefed. **CIK 0000886206 re-verified this cycle against the live
  `company_tickers.json`.**

---
### STEP 0 (i) — `cap_flag`. **THE CAP WAS WRONG BY 18%, AND THIS IS THE CALM / EMBC / BRBR BRANCH.**

The flag read: *"CAP BELOW FILED PUBLIC FLOAT — cap $231M against a filed float of $350M
(1.51x) as of 2025-02-28 … One of the two is wrong — RE-STRIKE THE CAP BY HAND."*

**Both numbers are right. Neither is the cap today.**

- **The float, verbatim from the FY2025 10-K cover** (accession `0000886206-25-000085`):
  *"As of February 28, 2025, the aggregate market value of the Registrant's Common Stock held
  by non-affiliates of the Registrant was approximately $ 349.5 million, which was based upon
  the closing price of $31.98 per share as reported by the New York Stock Exchange."*
  2025-02-28 is the FY2025 **second-quarter end**, as the brief expected. $349.5M ÷ $31.98 =
  **10,928,706 implied non-affiliate shares**.
- **The affiliate block is small, and it is not a control block.** The same cover states
  *"As of October 31, 2025, the Registrant had 12,155,832 shares of Common Stock outstanding"*;
  treasury purchases ran between the two dates, so the affiliate block is of the order of
  **1.0–1.2M shares, roughly 8–10%**. **This is not the MGPI branch** — there is no 33.7%
  affiliate wedge and no second voting class. One class only: *"Common Stock, $0.05 Par
  Value"*, NYSE.
- **The price fell 46% between the two dates.** FC closed **$31.98 on 2025-02-28** — which the
  aggregator chart reproduces to the cent, an independent check on the cover — and **$17.27 on
  2026-09-18**, nineteen months later. ($19.56 on 2025-08-29; $16.98 on 2025-10-31.)
- **THE CAP, RE-STRUCK BY HAND: US$195.0M.** 11,293,873 × $17.27 = **$195,045,187**.
  - **Shares 11,293,873**, from the **cover of the 10-Q for the quarter ended 2026-05-31,
    accession `0001193125-26-297572`, filed 2026-07-07**, as of **2026-06-30** — verbatim:
    *"11,293,873 sha res of common stock, $0.05 par value per share, as of June 30, 2026"*
    (the space inside "shares" is an artifact of the filer's inline-XBRL span breaks; flagged,
    not smoothed — PRIME RULE 1). The inline-XBRL fact `dei:EntityCommonStockSharesOutstanding`
    carries the same 11,293,873.
  - **Price $17.27, close of 2026-09-18**, Yahoo Finance chart endpoint — **an aggregator, used
    for a live quote only and flagged as such**; raw response on disk at
    `_research 2026-09-21 FC/yahoo_FC_chart.json`. **No splits anywhere in the available
    history**, so the split-invariant formula reduces to price × shares.
- **The screen's $231M is the FY2025 cover count (12,155,832, as of 2025-10-31) at about
  $19.00.** Both inputs are stale: the share count by three quarters and 862k shares of
  buyback, the price by a further 9%. **Every yield in this file uses $195M.**
- **BRANCH: the CALM / EMBC / BRBR class — a genuine live drawdown, both numbers right, the
  two dates nineteen months apart.** I name no fifth branch. I do second the MGPI run's
  proposed rewording: the diagnostic should say *"or the two dates differ"* — here they differ
  by nineteen months, which is the whole of the 1.51x and more.
- **NEW, AND IT IS A TOOLING DEFECT RATHER THAN A FLAG DEFECT:** the screen priced FC off the
  **annual** cover share count when a **newer 10-Q cover count existed and was 7.1% lower**.
  The `newest_periodic` column already knew the later periodic existed (`2026-05-31`); the
  share count did not follow it. On a company retiring roughly 5% of its shares a year, the
  cap is overstated on every row, and the error points the wrong way — it makes names look
  **dearer** than they are, so it will have suppressed candidates rather than promoted them.

---
### STEP 0 (ii) — `wc_note`. **THE FLAG IS RIGHT THIS TIME — the first time in four runs.**

The flag read: *"ONE LINE MADE THE CASH: ContractWithCustomerLiability moved 43% of 2021 OCF …
Read the 2021 cash-flow statement and liquidity note."*

I did not check only that line. **Every working-capital line of the FY2021 cash-flow
statement** (FY2021 10-K, accession `0000886206-21-000040`, confirmed against the FY2022 10-K
comparative, accession `0000886206-22-000028`), against FY2021 operating cash of **$46,177
thousand**, with its sign:

| FY2021 working-capital line, $000 | amount | % of OCF | direction |
|---|---:|---:|---|
| **Increase in deferred revenue** | **+19,788** | **+42.9%** | **PRODUCED cash** |
| Increase in accounts payable and accrued liabilities | +14,372 | +31.1% | produced |
| Decrease (increase) in accounts receivable, net | −14,266 | −30.9% | consumed |
| Decrease in other liabilities | −1,860 | −4.0% | consumed |
| Decrease (increase) in prepaid expenses and other assets | −880 | −1.9% | consumed |
| Decrease (increase) in inventories | +463 | +1.0% | produced |
| Increase (decrease) in income taxes payable/receivable | +273 | +0.6% | produced |
| Decrease in receivable from related party | 0 | 0.0% | — |
| **net working-capital contribution** | **+17,890** | **+38.7%** | **produced** |

**The flag names the actual largest mover and gets the sign right.** Three consecutive runs
(EMBC, MCFT, BRBR) found this diagnostic naming a line that was not the largest, and the BRBR
run recorded that as a tooling pattern rather than three coincidences. **On FC it is correct,
and the correction to the record is that the pattern is not universal.** The prior "inverted
twice, therefore expect inversion" is refuted here. The honest standing instruction is the one
the brief gave: rank every line every time, because the flag is a prompt to read and not a
score (operator rule 8).

**Is FY2021 operating cash a real number, and does any of it belong in owner earnings?**
Both answers are yes, with a condition that turns out to be the heart of this file.
- **It is real cash.** FC invoices All Access Pass and Leader in Me subscriptions in advance.
  The FY2025 balance sheet carries **deferred subscription revenue $106,534 thousand and
  customer deposits $16,327 thousand — $122.9M of customer money against $242.9M of total
  assets**. This is **[E3-52]**'s favourable class: *"liabilities without covenants or due
  dates attached to them … the benefit of debt … but saddle us with none of its drawbacks."*
  The customers fund the business, which is why FC can run on $85.6M of capital employed.
- **But the increment is a growth stream, not an earnings stream.** Under **[E2-23]**
  constraint 3 the working-capital increment belongs in (c) *where the business requires it*;
  here it runs the other way and funds growth — and the moment growth stops it goes to zero.
  **The filings prove that inside the window.** Deferred-revenue increment by fiscal year, from
  the filed statements: FY2021 **+19,788**, FY2022 **+14,245**, FY2023 **+8,806**, FY2024
  **+13,458**, **FY2025 +3,151**. Over the three quarters to 2026-05-31 deferred revenue and
  customer deposits **fell $12,022 thousand** (10-Q, accession `0001193125-26-297572`).
  Operating cash tracked it down: $60.3M (FY2024) → $29.0M (FY2025) → **$17.5M for nine months
  of FY2026** against $19.0M a year earlier.
- **Conclusion carried forward:** the increment belongs in the owner-earnings mean, but a mean
  struck on FY2021–FY2025 is a mean struck on the five years the increment was largest. That is
  exactly the **[E4-25]** problem the next section rebuilds.
- **The liquidity note, as the flag asked.** The 2023 Credit Agreement with KeyBank provides
  *"up to $70.0 million in total credit"* of which **$62.5 million is an undrawn revolver**,
  maturing **2028-03-27**, with covenants *"a Leverage Ratio of less than 3.00 to 1.00 and a
  Fixed Charge Coverage Ratio greater than 1.15 to 1.00"* and a restriction on buybacks unless
  in compliance before and after. FC states it was in compliance at 2026-05-31. Cash at
  2026-05-31 was **$11,972 thousand**, down from $31,698 at FY2025 year-end.

---
### STEP 0 (iii) — `spread_caveat`. **REBUILT OVER EIGHTEEN FISCAL YEARS, AND THE SCREEN'S BAND IS ROUGHLY DOUBLE THE LONG-RUN TRUTH.**

The caveat read: *"4-construction width only (3y/5y x two capex ends): CANNOT see variation
older than the 5-year window; rebuild it [E4-25]."* `years_filed` said 16.

**I rebuilt FY2008 through FY2025 — eighteen consecutive fiscal years — by hand from the
CONSOLIDATED STATEMENTS OF CASH FLOWS of seven 10-Ks**, each of which carries three years:

| 10-K | accession | filed | years it supplied |
|---|---|---|---|
| FY2010 | `0000886206-10-000031` | 2010-11-12 | FY2008, FY2009, FY2010 |
| FY2013 | `0000886206-13-000032` | 2013-11-14 | FY2011, FY2012, FY2013 |
| FY2016 | `0000886206-16-000075` | 2016-11-14 | FY2014, FY2015, FY2016 |
| FY2019 | `0000886206-19-000036` | 2019-11-14 | FY2017, FY2018, FY2019 |
| FY2021 | `0000886206-21-000040` | 2021-11-12 | FY2019–FY2021 (the FY2021 detail above) |
| FY2022 | `0000886206-22-000028` | 2022-11-14 | FY2020, FY2021, FY2022 |
| FY2024 | `0000886206-24-000060` | 2024-11-12 | FY2022, FY2023, FY2024 |
| FY2025 | `0000886206-25-000085` | 2025-11-12 | FY2023, FY2024, FY2025 |

Eighteen 10-Ks are on the index (FY2008 through FY2025, unbroken); eight were pulled, and the
overlaps agree year by year, which is the cross-check.

**A SECOND TOOLING DEFECT, AND IT IS THE ONE THAT MATTERS MOST HERE. FC's capital expenditure
is split across two tags and SEC `companyfacts` carries only one of them.** The investing
section has three capitalised lines — *Purchases of property and equipment*, *Capitalized
curriculum development costs*, and *Acquisition of license/content rights*. Only the first is a
us-gaap element (`PaymentsToAcquirePropertyPlantAndEquipment`). The second is the **company
extension `fc:PaymentsForCurriculumDevelopmentCosts`**, and **company extensions do not appear
in `companyfacts` at all** — FC's file carries no custom taxonomy namespace whatsoever.
**Measured:** FY2025 capex is **$8,253 + $7,561 + $1,074 = $16,888 thousand** as filed, against
**$8,253 thousand** visible to the screen — the screen sees **49%** of it. FY2023: $13,550
filed against $4,515 visible, **33%**. Over FY2008–FY2025 the screen sees **$67.4M of $149.1M —
45%**. This is the same class as the Marvell capitalised-IP-licence limit already on the
record, and it is a **source limit, not a bug**: no tag rule recovers a number the filer did
not tag to a standard element. **Every owner-earnings figure in this file is built from the
filed statements, not from the tagged capex.** The company agrees with me on the substance: its
own Free Cash Flow definition in the Q3 FY2026 release is *"GAAP calculated cash flows from
operating activities less capitalized expenditures for purchases of property and equipment,
**curriculum development**, and content or license rights."*

**A third, smaller tag defect, recorded because it would have poisoned (c).** The XBRL
depreciation-and-amortisation tags resolve to **$4.1M for FY2025** against a filed **$8,458 +
$4,440 = $12,898 thousand**; the filer splits *Depreciation* and *Amortization* on the face of
the income statement and tags the cash-flow add-backs separately, so an undimensioned D&A fetch
returns a third of the real charge. **A run that had used it would have put (c) at a third of
its true default and overstated owner earnings by roughly $8M a year.**

**The eighteen-year series, all $ thousand, all from the filed statements.** `capex` is the
three investing lines above; `D&A` is *Depreciation and amortization* plus *Amortization of
capitalized curriculum costs*; owner earnings = operating cash − SBC − (c), with (c) shown at
both ends of the band per **[E3-44, E2-41]** (D&A default) and total capex.

| FY | operating cash | capex (filed) | D&A (filed) | SBC | **OE, (c)=D&A** | **OE, (c)=capex** |
|---:|---:|---:|---:|---:|---:|---:|
| 2008 | 7,868 | 8,206 | 11,657 | (259) | **(3,530)** | **(79)** |
| 2009 | 5,282 | 4,037 | 10,301 | 468 | **(5,487)** | **777** |
| 2010 | 7,024 | 2,096 | 9,512 | 1,099 | **(3,587)** | **3,829** |
| 2011 | 15,643 | 5,423 | 8,746 | 2,788 | **4,109** | **7,432** |
| 2012 | 15,562 | 4,392 | 7,514 | 3,835 | **4,213** | **7,335** |
| 2013 | 15,528 | 5,398 | 8,022 | 3,589 | **3,917** | **6,541** |
| 2014 | 18,124 | 11,257 | 10,150 | 3,534 | **4,440** | **3,333** |
| 2015 | 26,190 | 4,612 | 11,968 | 2,536 | **11,686** | **19,042** |
| 2016 | 32,665 | 6,229 | 10,808 | 3,121 | **18,736** | **23,315** |
| 2017 | 17,357 | 14,403 | 11,188 | 3,658 | **2,511** | **(704)** |
| 2018 | 16,861 | 9,526 | 15,805 | 2,846 | **(1,790)** | **4,489** |
| 2019 | 30,452 | 6,841 | 16,313 | 4,789 | **9,350** | **18,822** |
| 2020 | 27,563 | 9,265 | 15,219 | (573) | **12,917** | **18,871** |
| 2021 | 46,177 | 4,106 | 14,641 | 8,617 | **22,919** | **33,454** |
| 2022 | 52,254 | 5,331 | 13,523 | 8,286 | **30,445** | **38,637** |
| 2023 | 35,738 | 13,550 | 11,697 | 12,520 | **11,521** | **9,668** |
| 2024 | 60,257 | 11,310 | 11,325 | 10,142 | **38,790** | **38,805** |
| 2025 | 28,977 | 16,888 | 12,898 | 5,805 | **10,274** | **6,284** |

*(FY2020 SBC is negative as filed — **(573)** — because forfeitures of unvested performance
awards exceeded the year's charge. That is the filer's own line, carried as filed and not
smoothed. **SBC did not silently resolve to zero anywhere**: it is read off the filed
cash-flow statement for all eighteen years, and it is material — FY2023's $12,520 is 35% of
that year's operating cash. **[E5-06]**.)*

**Window means, $M:**

| window | OE, (c)=D&A | OE, (c)=capex | operating cash |
|---|---:|---:|---:|
| **FY2021–FY2025 (5y, the screen's window)** | **22.79** | **25.37** | 44.68 |
| FY2016–FY2025 (10y) | 15.57 | 19.16 | 34.83 |
| FY2011–FY2025 (15y) | 12.27 | 15.69 | 29.29 |
| **FY2008–FY2025 (18y, everything filed)** | **9.52** | **13.33** | 25.53 |
| FY2013–FY2017 (an older 5y) | 8.26 | 10.31 | 21.97 |
| FY2016–FY2020 (an older 5y) | 8.34 | 12.96 | 24.98 |

**THE SCREEN'S BAND OF $24M TO $31M IS THE FY2021–FY2025 WINDOW AND NOTHING ELSE.** The
rebuild reproduces its bottom (**$25.4M** at the capex end of that window against the screen's
$24M), so the construction is not in dispute; the *window* is. **Reach back and the same
company earns $8–13M.** Two of the five years in the screen's window are the two best in the
filed history (FY2022 and FY2024) and a third (FY2021) carries the largest deferred-revenue
increment ever filed. **This is precisely what [E4-25] says a single window conceals, and the
spread is not an inconvenience to be resolved before ranking — it is part of the range.**
Carried forward as **$9.5M to $25.4M**, a factor of 2.7. It is not resolved by preference
**[E4-38]**: every window is published above so a reader can decide which is meaningful.

**`level_shift 1.31 (no step)` and `best_year_dep 0.09 ("no single-year dependence, 9-yr OCF
series")` are both false on the rebuilt series.** There **is** a level shift and it is
FY2020→FY2021: the FY2016–2020 operating-cash mean is $25.0M against an FY2021–2025 mean of
$44.7M, a **1.79x step**. It is the subscription build plus pandemic-era cost suppression, and
it did not hold — FY2025 is back to $29.0M and three quarters of FY2026 are $17.5M. And
single-year dependence is real at the owner-earnings level: **FY2024 alone is $38.8M of a
five-year sum of $126.8M — 30.6% of the window from one year.** The screen's 0.09 was measured
on operating cash over nine years; measured on owner earnings over the screen's own five, it is
0.31.

---
### STEP 0 (iv) — THE EMPTY COLUMNS. **ONE IS FALSE, ONE IS TRUE-BUT-INCOMPLETE, ONE IS GENUINELY CORRECT.**

**`acq_note` empty — FALSE, and the cash-flow statements say so.** The diagnostic is now 0 for
4 on the record after CGNX, CE and MGPI. FC made **nine acquisitions inside the filed window**,
every one a line in the investing section, $ thousand: FY2009 **1,157**, FY2010 **3,256**,
FY2011 **5,411**, FY2013 **4,185**, FY2014 **6,167**, FY2015 **262**, FY2017 **7,272**, FY2018
**1,108**, FY2019 **32**, FY2021 **10,209** — plus **license and content-rights purchases** of
750 (FY2017), 750 (FY2024) and 1,074 (FY2025). **Roughly $41.6M of cash out on perimeter,
against a $195M market capitalisation.** An empty cell here is not evidence of no acquisitions.

**`deal_note` empty — TRUE for a live deal, INCOMPLETE for the perimeter.** I read the whole
submissions index rather than the field. **No merger, tender, exchange, S-4 or 425 form appears
anywhere in the recent index**, and the Item 8.01 8-Ks of the last year (2025-06-18,
2025-10-22, 2025-12-22, 2026-03-18, 2026-06-17) are **conference-call scheduling notices** — I
**opened** the 2026-06-17 one rather than assume, and it announces the Q3 FY2026 call. The
2026-09-01 8-K is Item 5.02, executive changes, not a deal. **But two real perimeter events sit
inside the window and no flag saw either:** the **FY2008 sale of the Consumer Solutions
business unit** ($28,241 thousand of proceeds and a $9,131 thousand gain, both in the FY2010
10-K's comparative cash-flow statement — which is why FY2008 owner earnings are near zero and
why the eighteen-year mean is not a like-for-like series at its left edge), and the **FY2025
conversion of the France licensee into a directly owned office** (*"In early fiscal 2025, we
opened a new direct office operation in France, which was previously served by a licensee
partner"*), which moves revenue between the International Licensee and International Direct
Office segments. Neither breaks the series; both are recorded because the empty cell claimed
neither existed.

**`name_change_note` empty — GENUINELY CORRECT, and checked in the filing history rather than
the field.** EDGAR `formerNames` is **not** empty for this CIK: *FRANKLIN QUEST COMPANY*
(to 1994-02-14) and *FRANKLIN QUEST CO* (to 1997-02-11). The detector's window starts
2017-01-01 and correctly suppressed them. **I then ran the substitution check the BRBR run's
defect class requires:** CIK **0000886206** and Commission File Number **001-11107** carry
unbroken from the Franklin Quest era through the **1997 merger with Covey Leadership Center**
(*"The Company was incorporated in 1983 under the laws of the state of Utah, and we merged with
the Covey Leadership Center in 1997 to form Franklin Covey Co."*) to the 8-K filed three weeks
ago. This is a **rebrand after a merger, not a Rule 12g-3(a) successor-issuer substitution**,
and it is **eleven years before the earliest year in my series**, so no predecessor's figures
can contaminate FY2008–FY2025. **No new defect class; the BRBR pattern does not reproduce here.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Franklin Covey owns a library of
copyrighted corporate-training material — *The 7 Habits of Highly Effective People*, *The Speed
of Trust*, *The 4 Disciplines of Execution*, *Multipliers*, and for schools *Leader in Me* —
and rents access to it. There are two customers. An **employer** buys an annual, often
multi-year, site licence (the *All Access Pass*) that lets its staff use the content through a
web portal, and then buys days of a Franklin Covey consultant's time on top to run the
sessions. A **school or district** buys a *Leader in Me* membership: the same arrangement with
a curriculum instead of a leadership course and a former teacher instead of a management
consultant. Both are invoiced up front, which is why the customers are funding the company —
$122.9M of deferred subscription revenue and customer deposits against $242.9M of total assets
at FY2025 year-end. The cost side is **people**: gross margin is **76.2%** (FY2025 revenue
$267,067 against cost of revenue $63,498), but selling, general and administrative expense is
**68.4% of revenue** ($182,684), because the revenue must be re-sold to every client every year
by a salaried salesforce and delivered by salaried consultants. The residual in FY2025 was
**$5,704 thousand of operating income — 2.1% of revenue**. Content is refreshed continuously
and capitalised: **$7,561 thousand of curriculum development in FY2025** against $4,440
thousand of curriculum amortisation, on top of $8,253 thousand of property and equipment. There
is no factory, almost no inventory ($5,165), and essentially no debt ($823 thousand current
portion of notes payable, nothing long-term).

**The scarce input this business controls.** The copyrights and trademarks — *"We claim rights
for 706 trademarks in the United States and foreign countries"* and *"We claim 265 registered
copyrights"* — and, secondarily, the installed base of client portals and the schools already
running Leader in Me, which renew by default. **What it does not control is the consultant and
the salesperson**, and the 10-K says so itself: *"We depend on key personnel, the loss of whom
could harm our business"*; *"If we are unable to attract, retain, and motivate high-quality
employees, including sales personnel and training consultants, we may not be able to grow our
business as projected or may not be able to compete effectively."* Approximately 1,120
associates.

**Will the fundamentals look broadly the same in ten years?** The *demand* will: organisations
have bought leadership and execution training for a century and will keep buying it. The
*delivery* is explicitly in motion and the filer says so — *"novel technologies—particularly
artificial intelligence (AI)—reshape delivery models"* — and FC's own answer is to put an *"AI
Coach"* inside the All Access Pass. **That is a Q2 fact about the moat, not a Q1 fact about
comprehension.** Nothing here is complex or opaque: the revenue is one line, the cost is
people, the capital is content, the balance sheet is four pages and I have eighteen years of
its cash-flow statements. This is inside the circle, and **[E4-46]**'s test — could the
decision be made in five minutes with the filing open — is met.

**VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — yes, and the record supports it: FC has sold this for forty
  years, retained above 90% of All Access Pass revenue through FY2024, and added 624 new
  Leader in Me schools even in FY2025.
- No close substitute **[ ]** — **fails, and the strongest evidence is the filer's own.**
- Not price-regulated **[x]** — yes, unregulated.

**THE SECOND CRITERION, AND WHY IT FAILS.** The FY2025 10-K names, unprompted, **twenty-four
competitors across nine categories**: *"consulting firms such as McKinsey & Company, Deloitte,
and Accenture; recruitment and advisory firms such as Korn Ferry and Heidrick & Struggles;
leadership development organizations such as Development Dimensions International (DDI), LHH,
and Blanchard; coaching providers such as BetterUp, CoachHub, and Ezra; sales-training
organizations such as RAIN Group, Sandler, and Challenger; HR-technology providers such as
Workboard, Amplify, and Cornerstone; and learning-library providers such as Udemy Business and
LinkedIn Learning"*, plus *"7 Mindsets, Capturing Kids' Hearts, Second Step, Responsive
Classroom, and CharacterStrong"* in Education. **A list of competitors is not by itself a
finding** — Coca-Cola names Pepsi. What makes it one is the company's own ranking of what
decides a sale: ten *"principal competitive factors"*, of which the eighth is **"Competitive
pricing."** A product its customers think has no close substitute does not compete on price and
does not list price among the ten things that win the business.

**And then the customers behaved like customers with substitutes.** FY2025 MD&A, verbatim:
*"many of our clients and prospective clients have sought to reduce their spending to maintain
profitability, which led to delayed decision making, decreased contract expansion, and **lower
client retention**."* That is the demand curve of a desirable, deferrable purchase. It is also
the direct application of **[E2-44]**'s two-characteristic test: in a year when product demand
was flat and capacity was not fully utilised, FC **did not raise price** — it cut, taking
**$6,723 thousand of restructuring costs** (against $3,008 in FY2024) while operating income
fell from $33,042 to $5,704. And **[E4-37]**'s inverse metric — *"you can almost measure the
strength of a business over time by the agony they go through in determining whether a price
increase can be sustained"* — is filed as a risk factor in FC's own words: *"as we continue to
adjust our offerings and products to meet our clients' needs, we may shift the type and pricing
of our offerings, **which may adversely impact client renewal rates**."* That is the prayer
session, written down.

**Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]**
On the **rebuild** test FC passes, and it deserves the credit: the content asset is *defended*,
not replaced. The FY2025 revision of *The 7 Habits of Highly Effective People* is Coca-Cola's
advertising, not Mitsui's Rhodes Ridge, and **[E5-23]** / **[E3-49]** prescribe exactly that
continuous maintenance for every moat. The trademark and copyright portfolio is genuinely
long-lived. **On the great-manager test it does not pass cleanly, and [E4-23] says to record
that here and not at Q3:** the revenue is re-sold annually by a salesforce whose restructuring
was the largest single identified cost of FY2025 (*"we continued to restructure our sales force
in North America"*), and management attributes the FY2025 shortfall in part to *"the
implementation of our new go-to-market strategy in North America"*. A business whose year turns
on whether this year's sales reorganisation worked is **[E3-38]**'s have-to-be-smart-every-day
business, and its 1991 original is blunt: *"a business, unlike a franchise, can be killed by
poor management"* **[E3-43]**.

**PRIMARY MOAT METRIC, FILING-SOURCED, AND ITS TREND. [E3-46]** — *"the best businesses, by
definition, are going to be businesses that earn very high returns on capital employed over
time."* EBIT ÷ (total assets − current liabilities), every year the data reaches, FY2025
cross-checked against the filed statements in Step 0:

| FY | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **FC EBIT/CE** | 15.3% | 12.1% | 10.1% | **−6.8%** | **−2.8%** | 2.2% | 3.0% | 7.2% | 22.5% | 28.0% | **33.3%** | **6.7%** |

**Twelve-year mean 10.9%, with four years below 3.1% and two of them negative.** The
22.5 / 28.0 / 33.3 run the screen's window sits on is the exception in this series, not the
level — and **part of it is the denominator, not the business.** Capital employed fell from
**$162.3M (FY2014) to $85.6M (FY2025), −47%**, because FC retired stock: treasury stock stands
at **$289,933 thousand against total shareholders' equity of $66,911 thousand**. A ratio whose
denominator halves while the numerator is flat is not evidence of a widening moat, and
**[E2-47]** carves exactly this out of the primary test. *(The opposite reading is stated
fairly: on **net tangible** capital employed — stripping $31,220 of goodwill and $34,551 of
intangibles — FC's good years show very high returns indeed, which is the honest
counter-argument and the reason this run went to twelve years rather than three.
**[E2-43]** asks for the goodwill wedge to be reported separately, and it is: $65.8M of the
$85.6M.)*

**THE COMPETITOR ROW — required [E3-28].** Same metric, same construction, same source class
(each company's own 10-K, us-gaap `OperatingIncomeLoss`, `Assets`, `LiabilitiesCurrent`, newest
vintage), as many years as each filer reaches. **The peer set is derived from FC's own
competition disclosure and not from a guess.** Of the twenty-four names FC lists, **four file
with the SEC**; I add **Skillsoft** and **Coursera**, which FC does not name but which are the
listed form of the learning-library class it does name, and I say so.

| Company | EBIT ÷ capital employed, year by year | window | mean | source |
|---|---|---|---:|---|
| **FRANKLIN COVEY (subject)** | 15.3 · 12.1 · 10.1 · −6.8 · −2.8 · 2.2 · 3.0 · 7.2 · 22.5 · 28.0 · 33.3 · 6.7 | FY2014–FY2025 (12y) | **10.9%** | own 10-Ks, CIK 0000886206; FY2025 cross-checked to the filed statements |
| Accenture plc | 44.0 · 45.7 · 41.0 · 40.4 · 41.3 · 33.7 · 26.7 · 27.7 · 31.5 · 26.5 · 26.0 · 22.7 | FY2014–FY2025 (12y) | **33.9%** | ACN 10-K, CIK 0001467373 |
| Korn Ferry | 11.3 · 3.7 · 7.5 · 12.1 · 7.9 · 8.3 · 6.8 · 19.0 · 12.2 · 7.8 · 11.9 · 12.2 | FY2015–FY2026 (12y) | **10.1%** | KFY 10-K, CIK 0000056679 |
| Heidrick & Struggles | 4.1 · 7.3 · 9.9 · 9.8 · −8.3 · 18.0 · 12.7 · −7.6 · 17.2 · 19.1 · 10.7 · 1.1 | FY2013–FY2024 (12y) | **7.8%** | HSII 10-K, CIK 0001066605 |
| Udemy | −401.4 · −19.5 · −43.1 · −33.8 · −42.9 · −1.9 | FY2020–FY2025 (6y) | **negative in every filed year** | UDMY 10-K, CIK 0001607939 |
| Coursera | −25.2 · −18.9 · −25.2 · −23.4 · −18.8 · −12.1 | FY2020–FY2025 (6y) | **negative in every filed year** | COUR 10-K, CIK 0001651562 |
| Skillsoft | −0.1 · −66.0 · −35.9 · −9.5 · −15.2 | FY2020, FY2023–FY2026 (5y) | **negative in every filed year** | SKIL 10-K, CIK 0001774675 |

- **Peers taken: six, plus the subject.** Buffett says eight **[E3-28]**; the industry has more
  than eight and **only four of FC's own named competitors are reachable as filers**. The rest
  are private partnerships (McKinsey, Deloitte, DDI, Blanchard, RAIN Group, Sandler, Challenger),
  venture-held (BetterUp, CoachHub, Ezra, Workboard, Amplify), inside a foreign parent (LHH, in
  Adecco), inside Microsoft (LinkedIn Learning), private since 2021 (Cornerstone OnDemand), or
  private throughout (the five Education names). **That unavailability is named, not hidden.**
  It does **not** make the class PROVISIONAL, because the row as built already answers the
  question asked: FC sits *inside* a pack rather than above one, and the missing names are
  private *consulting* firms, which is the pack FC is already shown to belong to.
- **Who names FC.** EDGAR full-text search, run through `tools/sources.py`'s `fts_count()` with
  the bare zero-padded CIK form the CALX defect requires: *"Franklin Covey"* appears in **285**
  10-Ks, *"FranklinCovey"* in **57**, *"All Access Pass"* in **21**, *"Leader in Me"* in **19**,
  *"7 Habits of Highly Effective"* in **32**. FC is a named vendor in the filings of many
  companies; it is not named as a *competitor* by Accenture, Korn Ferry or Heidrick, which is
  itself a size statement rather than a moat statement — at $267M of revenue FC is below their
  notice.
- **The row's limit, stated [E3-61]:** it shows position, not conduct. It cannot tell me whether
  FC's management will behave like Accenture's or like Heidrick's, and the corpus concedes that
  even Munger had no model for predicting that — *"I think you'd have to know the people
  involved."*

**Untapped pricing power? [E3-33]** No. **[E5-28]** scopes the class: *"If you name some
business that has incredible pricing power, you're talking about a business that's a monopoly
or a near monopoly."* FC's own 10-K puts US corporate-training spend at *"approximately $188
billion (about $400 billion globally)"*; FC's $267.1M is **0.14% of the market it defines for
itself**, and *"none of our clients were responsible for more than 10% of our consolidated
revenues."* Not a monopoly, not near one. The one piece of filed pricing conduct runs the
other way.

**DIRECTION — and [E4-32] makes direction the primary criterion of a great business.** It is
**NARROWING**, on four independent filed series:
1. **Revenue.** FY2024 $287,233 → FY2025 $267,067 (**−7.0%**), and FY2026 guidance was cut on
   2026-07-01 to *"$260 million to $267 million"* from *"$265 million to $275 million"* — a
   second consecutive down year at the midpoint. Revenue was $225.4M in FY2019; growth to the
   FY2026 guidance midpoint of ~$263.5M is **16.9% nominal over seven years**, below US CPI
   over the same period. **In real terms this business has not grown since 2019.**
2. **Units, where units exist [E4-55].** New Leader in Me schools added: **739 (FY2022, which
   the FY2022 10-K calls *"a record"*) → 728 (FY2024) → 624 (FY2025)** — **−14%** year on year,
   in the filer's words *"in a very challenging funding environment"*. In Enterprise there is
   **no unit disclosure at all**; the only volume proxy FC publishes is a dollar figure
   (*"invoiced"*), which is exactly the substitution [E4-55] warns about.
3. **Operating margin.** 11.5% (FY2024) → **2.1%** (FY2025) on a 7.0% revenue fall. A franchise
   does not surrender four-fifths of its operating income to a 7% volume decline. That is
   **[E2-58]**'s shape — a fixed cost base with no administered price.
4. **The retention metric itself was withdrawn.** FY2021 10-K: *"annual AAP revenue retention
   remained above 90 percent for the year."* FY2022: *"annual AAP revenue retention remained
   well above 90 percent."* FY2024: *"AAP subscription revenue retention levels remained strong
   and were greater than 90%."* **FY2025: the number is gone**, replaced by *"we are pleased
   that the majority of our clients are renewing their All Access Pass subscriptions and Leader
   in Me memberships"* — in the same document that concedes *"lower client retention."* That is
   a Q3 flag **[E2-49]** and it is recorded below; it is cited **here** because it is also the
   disappearance of the only franchise metric FC ever published.

**Which of the four causes of extreme success is this? [E4-36]** The FY2022–FY2024 run reads as
**wave-riding**: a subscription conversion, a pandemic-era shift to digital delivery, and
suppressed travel and facility cost arriving together, with the deferred-revenue increment at
its filed maximum in FY2021. **[E3-51]**: *"when a surfer gets up and catches the wave and just
stays there, he can go a long, long time. But if he gets off the wave, he becomes mired in
shallows."* FY2025 and the first three quarters of FY2026 are the shallows — operating cash
$60.3M, then $29.0M, then $17.5M for nine months. **A surfing run is not a moat; the advantage
lives in the wave, not the surfer.**

**The attacker's test [E2-45].** With ample capital and skilled personnel, competing with
Franklin Covey requires a content library, a brand, and a salesforce. The copyrights are
genuinely hard to copy. The other two are purchasable, and FC's own filing names fourteen
private firms that have already bought them, plus two of the largest software companies on
earth giving libraries away inside a broader subscription. That is why the returns look like
Korn Ferry's rather than Accenture's.

**The dominance test [E2-53].** Not met. FC does not set its own economics — the FY2025 MD&A
describes at length how the market set them.

**Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: NARROWING**

**Ask it aloud: can I name the document that would resolve this?** **No — because there is no
unread document.** I have the filer's own competition disclosure, its own pricing conduct, its
own withdrawn retention metric, eighteen years of its own cash-flow statements, and six
competitors' filings on the same metric over twelve years. This is not a case of missing
evidence, so it is not UNRESEARCHED. Nor is it UNKNOWABLE: the 2026-09-20 ruling that
**[E4-04]** closes a name UNKNOWABLE at Q2 — the perimeter close — applies to a name that
**passes [E3-03]** and whose durability cannot be judged from filings. **FC does not reach that
test, because it fails [E3-03]'s second criterion on positive filed evidence.**

This is a good, understandable, asset-light business with a real and long-lived content asset,
customer-funded working capital, no debt, and ordinary competitive economics. **It is a
business, not a franchise [E3-43].** And the guardrail runs here too: nothing in the sections
below may be used to promote it **[E2-37, E2-38, E3-39]**.

**VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

---
⛔ **THE FILE CLOSES HERE. Q1–Q4 did not each show IN, so Q5 does not open (operator rule 2).**
Everything below is recorded **for the record, WITHOUT VERDICTS**, in the form the CE and MGPI
runs used. No box is ticked. No entry language is used. Any arithmetic is headed
**COMPUTATION — NOT A CLEARANCE** (operator rule 3).

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(recorded below the close, NO VERDICT)*

**STEP 1 — THE WEIGHT CASE, declared.** *How much damage can this manager do before I can react?*
- [x] **Daily execution [E3-38, E3-43, E2-70]** — **ticked.** The revenue is re-sold to every
  client every year by a salaried salesforce; FY2025's result turned on whether a sales
  reorganisation worked, and management says so (*"the implementation of our new go-to-market
  strategy in North America"*). This is the have-to-be-smart-every-day class.
- [ ] Control **[E1-16]** — not ticked; this would be a minority public position.
- [ ] Leverage **[E3-29]** — not ticked. **There is effectively no debt**: $823 thousand current
  portion of notes payable at FY2025 year-end and nothing long-term, against a $62.5M undrawn
  revolver.

**One ticked, so on a live file Q3 would be a BINARY GATE and no price would compensate.**
It is recorded here without a verdict because the file closed at Q2.

**Honesty — each matter dated to when it became PUBLIC [E5-16].** **No disqualifier found, and
that is not a finding that the managers are honest [E5-17].** Item 3 of the FY2025 10-K reports
only *"certain legal actions, which we consider routine to our business activities."* Deloitte
& Touche LLP issued **unqualified opinions on both the financial statements and the
effectiveness of internal control over financial reporting**, with **one critical audit
matter** — standalone selling price allocation for the Leader in Me subscription — and
management reported disclosure controls and ICFR effective with **no change in the fourth
quarter**. No restatement, no material weakness, no Item 4.02 filing anywhere in the index.

**STEP 2 — THE FLAGS. Each is a prompt to read, never a verdict [E5-36, E5-38].**

- [ ] **weak accounting** — does not fire. See above.
- [ ] **unintelligible footnotes** — does not fire. The revenue note, the segment note and the
  cash-flow detail lines are legible and reconcile; I rebuilt eighteen years from them.
- [x] **trumpeted earnings projections / growth targets [E4-22] third flag** — **FIRES.** FC
  guides annually and publicly on **both revenue and Adjusted EBITDA**, in constant currency,
  and re-states the guidance in every quarterly release.
- [ ] **serial share issuance [E5-15]** — **does not fire; the opposite.** Shares outstanding
  fell from 13,853k (FY2022 year-end) to **11,293,873 (2026-06-30)**.
- [x] **EBITDA / adjusted-earnings promotion [E4-29]** — **FIRES, and it is the loudest thing in
  the file.**
- [ ] **filed-figure tells [E4-30]** — **do not fire, in both directions.** Reported growth is
  conspicuously *un*smooth (net income −$9.4M, +$13.6M, +$18.4M, +$17.8M, +$23.4M, +$3.1M across
  FY2020–FY2025), and **cash taxes are RISING as a share of pretax income**, not falling: cash
  paid for income taxes $3,308 (FY2023), $4,205 (FY2024), **$7,693 (FY2025)** against pretax
  income that fell to roughly $5M. That is the opposite direction from the tell.
- [x] **metric-switching, the sixth flag [E2-49]** — **FIRES.**

**WHAT THE FILINGS ACTUALLY SAY ON THE TWO FLAGS THAT FIRE.**

**[E4-29], the EBITDA flag.** *"Trumpeting EBITDA … is a particularly pernicious practice.
Doing so implies that depreciation is not truly an expense, given that it is a 'non-cash'
charge. That's nonsense."* FC's own definition, verbatim from the Q3 FY2026 release:
*"The Company defines Adjusted EBITDA as net income or loss excluding the impact of interest,
income taxes, intangible asset amortization, depreciation, stock-based compensation expense,
and certain other infrequently occurring items such as restructuring and building exit costs."*
**That deletes three things the corpus names as real expenses in three separate places** —
depreciation and amortisation **[E4-29]**, stock-based compensation **[E5-06]** (*"To say
'stock-based compensation' is not an expense is even more cavalier"*), and restructuring
charges **[E3-53, E5-33]** (*"to tell owners year after year, 'Don't count this' … is
misleading"*). **The deletions are not small.** For FY2025: Adjusted EBITDA **$28.8M**, against
**income from operations of $5,704 thousand** and **net income of $3,068 thousand**. The wedge
is depreciation $4,066 + amortisation $4,392 + curriculum amortisation $4,440 + SBC $5,805 +
restructuring $6,723 ≈ **$25.4M**, and every dollar of it is a real cost of this business.
**[E5-41]**'s inversion is exact here: FC spends the curriculum cash first and records the
expense later, which is *"reverse float"* — and it is precisely the expense Adjusted EBITDA
deletes.

And the measure is not a footnote — **it is the narrative**. The headline block of the Q3
FY2026 release reads, in order: *"Consolidated Third Quarter Revenue Increases 1% to $67.8
Million / Invoiced Amounts in Enterprise North America Increase 4% to $36.7 Million / Deferred
Revenue Increases 7% to $96.0 Million / Net Income for the Third Quarter Increases to $3.1
Million / **Adjusted EBITDA Increases 14% to $8.3 Million**"* — five bullets in ascending order
of goodness. The CFO's quote leads with it: *"we demonstrated strong operational discipline,
with Adjusted EBITDA growing 14% to $8.3 million."* **The guidance is given in it.** The segment
note reports in it. And **management is paid on it**: the FY2025 proxy states *"this component
would be split between adjusted EBITDA (50% weighting) and a new metric, net revenue (20%
weighting)"* for the short-term plan, and names **"Qualified Adjusted EBITDA"** as the
Company-Selected Measure in the pay-versus-performance table, adding that it *"comprises the
largest portion of the performance metrics for determining our LTIP and STIP awards."*

**The mechanism the flag exists to catch is visible in the same release.** In the quarter FC
announced *"Adjusted EBITDA Increases 14%"*, **operating cash flow fell to $1.1 million from
$6.3 million**, **free cash flow was $(1.0) million against $2.8 million**, and **cash fell to
$12.0 million from $33.7 million**. The trumpeted measure rose 14% while the cash went the other
way. **A run that had read only the annual report would have missed the headline block
entirely** — which is exactly why the standing rule to pull the latest EX-99.1 exists.

**[E2-49], metric-switching.** *"Yardsticks seldom are discarded while yielding favorable
readings. But when results deteriorate, most managers favor disposition of the yardstick rather
than disposition of the manager."* The operational form is to compare the headline metric across
successive filings:

| filing | what it said about All Access Pass revenue retention |
|---|---|
| FY2021 10-K | *"annual AAP revenue retention remained above 90 percent for the year"* |
| FY2022 10-K | *"annual AAP revenue retention remained well above 90 percent"* |
| FY2024 10-K | *"AAP subscription revenue retention levels remained strong and were greater than 90%"* |
| **FY2025 10-K** | **no number. Replaced by** *"we are pleased that the majority of our clients are renewing their All Access Pass subscriptions and Leader in Me memberships"* |

**The switch follows the deterioration, and the same document concedes the deterioration** —
*"delayed decision making, decreased contract expansion, and lower client retention."* This is
the failure case, not the candor case. **My standing [E2-49] prior now reads seven fires and
five failures** (fired at SHOP, MRVL, PAY, ARM, CALX, BE and now FC; failed at QLYS, CRM, CORT,
PLTR, INOD). It remains a prior to be checked, never assumed either way.

**A SECOND INSTANCE OF THE SAME FAMILY, WHICH IS THE CANDOR CASE AND MUST BE STATED BESIDE IT
[E4-26].** Through FY2024 FC's performance share units vested on *"the highest rolling
four-quarter Adjusted EBITDA performance within the three-year cycle"* — **a high-water mark** —
and the FY2023–FY2025 cycle therefore paid against *"The highest rolling four quarters Adjusted
EBITDA achieved over the fiscal 2023-2025 period was $56.0 million"* while FY2025's actual
Adjusted EBITDA was **$28.8 million**. FC **redesigned it before the deterioration was known**:
*"Beginning in fiscal 2025, the Committee redesigned the PSU program to measure performance on a
cumulative basis, with 70% of the award tied to cumulative net revenue and 30% tied to cumulative
Adjusted EBITDA over the fiscal 2025-2027 period."* A change announced ahead, toward a harder
measure, with reasons given, is **[E2-49]**'s candor case — the same shape as Berkshire's own
1982 switch.

**MORE EVIDENCE AGAINST MY OWN READING, hunted deliberately [E4-26, E3-41].**
- **The bad year was not paid.** *"For fiscal 2025, our adjusted EBITDA was $28.8 million and
  net revenue was $267.1 million, **resulting in no payout for the financial component of the
  STIP for the NEOs**, as certified by the Compensation Committee."*
- **Upside was cut in advance, not after the fact.** *"the Committee set the maximum payout
  opportunity at 150% of target (rather than at 200% of target) in light of the significant
  investments being made to transform the business"*, and FY2025 PSUs *"would not provide upside
  opportunity above 100% of target."*
- **FC's own Free Cash Flow definition is honest**, and stricter than the screen's capex: *"cash
  flows from operating activities less capitalized expenditures for purchases of property and
  equipment, **curriculum development**, and content or license rights."* Management treats
  curriculum spend as capex; the tagged data does not.
- **The FY2025 MD&A states the bad news plainly and first**: *"Fiscal 2025 was a challenging
  year"*, with the causes itemised and quantified by segment. That is **[E2-26]**'s half-owner
  test passed on the narrative, whatever the headline metric does.

**STEP 3 — THE PRIMARY TEST [E2-01].** *"the achievement of a high earnings rate on equity
capital employed … and not the achievement of consistent gains in earnings per share."*
Net income on average shareholders' equity, fifteen years:

| FY | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ROE | 6.1% | 9.2% | 14.5% | 15.5% | 8.8% | 6.4% | −8.0% | −7.1% | −1.3% | −13.3% | 19.6% | 22.7% | 22.0% | 28.9% | 4.1% |

**Fifteen-year mean 8.5%, with five negative years.** And **[E2-47]**'s carve-out bites hard:
equity is **$66,911 thousand after $289,933 thousand of treasury stock**, so the 2022–2024
readings sit on a denominator that buybacks cut by 47% since FY2014. Balance sheet before income
statement, as the rule requires: the capital actually put into this business is additional
paid-in capital $230,251 plus retained earnings $126,272 — **$356.5M** — against which FY2025's
$3,068 thousand of net income is **0.9%**.

**The half-owner test [E2-26].** Mixed, and the mix is the point. The **narrative** passes:
FY2025's causes are itemised, the revenue decline is attributed without euphemism, and the
guidance cut of 2026-07-01 names the three specific contracts behind it. The **headline** does
not: a reader who stops at the five bullets of the Q3 FY2026 release learns that Adjusted EBITDA
rose 14% and does not learn that cash fell 64% year on year.

**The institutional imperative — all four scored [E2-30].** *"Institutional dynamics, not
venality or stupidity."*
- [ ] **resists any change in current direction** — does not fire. FC changed its North American
  go-to-market model at real cost to a reported year.
- [ ] **projects/acquisitions materialise to soak up available funds** — does not fire
  materially. Nine acquisitions across eighteen years totalling roughly $41.6M, all adjacent,
  none transformative.
- [ ] **staff studies produced to justify the leader's craving** — no filed evidence either way.
- [x] **peer behaviour mindlessly imitated** — **fires mildly.** The AI response is an *"AI
  Coach"* bolted inside the existing portal, described in the language of the moment
  (*"agentic AI interfaces"*), with no disclosed economics. A prompt to watch, not a finding.

**CAPITAL ALLOCATION — THE BUYBACK, AND IT IS THE LARGEST DECISION THIS MANAGEMENT MAKES.**
FC retires stock continuously. **Between FY2022 year-end and 2026-06-30 it spent $120,796
thousand gross** ($35,555 + $30,749 + $26,374 + $28,118 for the three quarters of FY2026),
**less $5,422 thousand of treasury reissue proceeds = $115,374 thousand net**, while the share
count fell from **13,853k to 11,293,873 — 2,559k net shares retired.** **That is $45.09 of net
cash per net share retired, against a quote of $17.27 on 2026-09-18.**

- **Condition (1), ample funds for operations and liquidity [E5-08]** — **a live question.** In
  the three quarters to 2026-05-31, FC generated **$17,476 thousand** of operating cash and
  **$8,477 thousand** of free cash flow on its own definition, and spent **$28,118 thousand** on
  buybacks. Cash fell from **$31,698 to $11,972 thousand**; the revolver was drawn $11,677 and
  repaid $11,677 inside the period. **[E5-39]** is explicit that a credit line is not liquidity
  — *"We will never be dependent on the kindness of strangers … available cash or credit is a lot like oxygen"* —
  and **[E5-25]** shows what real compliance looks like: Berkshire published its liquidity floor
  as a number, in advance. **FC has published no liquidity floor.** On 2025-08-11 the Board
  replenished the authorisation to $50.0M, and on **2025-08-14, three days later**, FC
  *"initiated a 10b5-1 plan to purchase up to $10.0 million of our common stock through daily
  purchases."*
- **Condition (2), a material discount to conservatively calculated intrinsic value [E5-08,
  E4-31]** — **on the evidence in this file, not met at the prices paid.** **[E5-24]**: *"what
  is smart at one price is dumb at another."* $45.09 per net share retired against $17.27 today.
  **The humility clause is attached and is not decorative [E4-13]:** *"it is natural for CEOs to
  be optimistic about their own businesses. They also know a whole lot more about them than I
  do"*, and **[E5-08]** adds that *"infractions, even serious ones, are innocent; many CEOs
  never stop believing their stock is cheap."* This rests on my own owner-earnings range, which
  is $9.5M–$25.4M and says so.
- **[E2-60], restricted earnings.** The distribution did **not** raise leverage — there is no
  debt to raise — so the *"financial strength"* limb was not breached through borrowing. It was
  pressed through the **cash balance**, which is the same test by another route: $31.7M to
  $12.0M in nine months.
- **[E2-51], the refusal tell**, does not apply — FC repurchases aggressively. What it has not
  done is repurchase *more* aggressively at the low, which **[E4-50]** would license; nine
  months of FY2026 spending is roughly flat on the prior year at half the price.
- **[E2-52], dividends funded by issuance** — does not apply. No dividend: *"We did not pay or
  declare dividends on our common stock during the fiscal years ended August 31, 2025 or 2024."*

**THE GUARDRAIL — checked before anything above is used [E2-37, E2-38, E3-39].**
- [x] Confirmed: **nothing in this Q3 is used to promote the name.** The file closed at Q2 and
  nothing here reopens it. *"a good managerial record … is far more a function of what business
  boat you get into than it is of how effectively you row"* **[E2-37]**.
- [x] The key-person and have-to-be-smart-every-day dependence was recorded **at Q2 as a moat
  defect [E4-23]**, not here as a strength.
- [x] No great-manager exception is invoked: there is no localised excisable cancer **[E2-35,
  E2-36]**, because there is no intact franchise to excise it from.

**NO VERDICT RECORDED — Q2 closed the file.**

## Q4 — WILL IT SURVIVE? *(recorded below the close, NO VERDICT)*

### Owner earnings — the one number **[E2-23]**
The eighteen-year construction is in Step 0 (iii) and is not repeated. It is built from the
filed cash-flow statements of eight 10-Ks, **never from a net-income proxy** (PRIME RULE 3), and
SBC is subtracted in full in every one of the eighteen years **[E5-06]**.

- **Short-window mean** (FY2021–FY2025, the corpus's five-year default **[E2-42, E1-03]**):
  **$22.8M** at the D&A end of (c), **$25.4M** at the total-capex end.
- **Long-window mean** (FY2008–FY2025, eighteen years, everything filed): **$9.5M** at the D&A
  end, **$13.3M** at the total-capex end.
- **Spread, conservative end:** it moves from **$22.8M to $9.5M** — the long window is **58%
  lower**.
- **Combined range** (window spread × capex band): **$9.5M to $25.4M**, a factor of **2.7**.
- **Is that range too wide to reach a conclusion? [E4-25]** On the price question, **yes** — and
  under [E4-25] that would itself have been the answer. It is recorded, not resolved by
  preference; all six windows are published above **[E4-38]** so a reader can decide which is
  meaningful.
- **The distorted years, named [E5-11, E4-41].** FY2021 and FY2022 carry the largest
  deferred-revenue increments ever filed (+$19.8M, +$14.2M) alongside pandemic-suppressed travel
  and facility cost; FY2024 is the single best year in eighteen and is **30.6% of the five-year
  sum on its own**. **[E4-41]** says normalise the mean *down* for favourable exogenous breaks
  before trusting it, and these are exactly that. Against it, **[E3-55]** says volatility with a
  certain endgame is not a defect — but FC's bounce is not See's seasonality; the *level* moved
  and then moved back, which is width about the level, not noise around it.
- **Maintenance capex — a DISCLOSED JUDGMENT, stated as a guess [E2-23]: "(c) must be a guess."**
  FC is **not** in **[E5-20]**'s capital-intensive exception class — not a railroad, an airline
  or a utility, and nothing in its filing says depreciation understates renewal — so
  **[E3-44]**'s default applies and D&A is a legitimate end of the band. **But I put the weight
  at the total-capex end, and the reason comes from the filing:** FC's real maintenance spend is
  **curriculum**, not plant, and curriculum spend has run **well above** curriculum amortisation
  in the recent years ($9,035 against $3,084 in FY2023; $6,866 against $3,172 in FY2024; $7,561
  against $4,440 in FY2025), because the content must be re-cut to stay saleable — the FY2025
  flagship *7 Habits* revision is the filed instance. Where renewal spend is persistently above
  the charge, the D&A end understates (c). **My guess, disclosed: (c) sits at roughly the
  total-capex end, about $12–14M a year at current scale.** The band is displayed, not collapsed.
- **The working-capital increment [E2-23] constraint 3.** It is inside operating cash by
  construction and it is a **source**, not a use — favourable while the book grows, a headwind
  the moment it does not. Step 0 (ii) shows it at +$3.2M in FY2025 and **−$12.0M** over three
  quarters of FY2026.
- **Stock compensation subtracted in full [E5-06]:** yes, all eighteen years, from the filed
  add-back line, **and it did not resolve to zero anywhere**. **[E3-70]** notes the reported
  charge is the *floor* of the correct subtraction where SBC is material; at FY2023 SBC was
  **35% of operating cash**, so the floor does real work here. No grant-date total resolves
  undimensioned — the known source limit — so the reported charge is used and the limitation is
  stated rather than hidden.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — [ ] good — [ ] gruesome — **no box ticked, because no verdict is recorded.**
  For the record: **it is not gruesome.** The worst class *"grows rapidly, requires significant
  capital to engender the growth, and then earns little or no money"*; FC does neither — it
  barely grows and it needs almost no capital: $16.9M of total capex in FY2025 against $267.1M of revenue, on $85.6M of
  capital employed. **[E4-43]** is explicit that the *good* class passes, and on the
  FY2022–FY2024 numbers FC looks like the good account. **On eighteen years it looks like a
  savings account whose interest rate has ranged from below zero to 19% and averaged single
  digits, with no growth in the deposit** — neither the great account (*"an extraordinarily high
  interest rate that will rise as the years pass"*) nor, strictly, the gruesome one.

### Staying power — all three scored **[E5-11]**
1. **A large and reliable stream of earnings — LARGE, NOT RELIABLE.** Net income was negative in
   **five of the last fifteen years** (FY2017–FY2020 consecutively). Reconstructed owner
   earnings range from **−$5.5M to +$38.8M** across the eighteen.
2. **Massive liquid assets — NO.** Cash was **$11,972 thousand at 2026-05-31** against FY2025
   revenue of $267.1M and a cost base of $246.2M — roughly **eighteen days of operating cost**.
   There is a **$62.5M undrawn revolver to 2028-03-27**, and **[E5-39] refuses to count it.**
   The real mitigant is stated: **$122.9M of customer prepayments** arrive ahead of delivery and
   are covenant-free and undated **[E3-52]**, so the working-capital cycle funds itself in the
   ordinary course.
3. **No significant near-term cash requirements — the one that usually kills, and here it is
   mostly clean.** Debt due is **$823 thousand**. No pension, no earn-out of size, no near-term
   maturity. **The requirement that is real is non-financial**: $106.5M of deferred subscription
   revenue is a promise to deliver content and consultant days, and the 2023 Credit Agreement
   restricts distributions unless the Leverage Ratio (<3.00x) and Fixed Charge Coverage Ratio
   (>1.15x) are met **before and after** — so a further Adjusted-EBITDA decline could close the
   buyback that has been the principal use of cash.
- **Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this
  framework and the corpus supplies none*: **$823 thousand of notes payable, nothing long-term,
  revolver undrawn.** **[E2-54]**'s coverage test — all interest comfortably met out of current
  cash flow **net of ample capital expenditure** — passes trivially: cash interest paid was
  **$496 thousand** in FY2025.
- **Design principle [E2-55]:** score the worst case, not the expected one. The worst case in
  FC's own filed history is FY2017–FY2020: four consecutive loss years at the net line while
  revenue oscillated between $185M and $225M. **The company survived it — with more cash than it
  has now.**

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**
**Model exposure, not experience [E4-40].** The benign reading is that FY2025 was a macro
air-pocket and FY2027 recovers, which is management's case and is supported by three consecutive
quarters of invoiced growth in Enterprise North America. The exposure is different, and it is
structural.

**The mechanism.** One hundred percent of FC's revenue is a **discretionary line in somebody
else's budget** — a training and development allocation for a corporation, a professional-
development allocation for a school district. It is sold by a fixed salesforce into a market
where the filer itself names twenty-four alternatives and lists price among the ten factors that
decide a sale, and where the marginal substitute (a generative model, or LinkedIn Learning
already inside an existing Microsoft contract) approaches zero marginal cost. The death is not a
default; it is **operating leverage running in reverse for long enough that the salesforce
cannot be maintained at the scale the content requires.**

**Quantified from filed figures.** FY2025: revenue $267,067; gross profit $203,569 (76.2%);
selling, general and administrative $182,684 — **89.7% of gross profit**; restructuring $6,723;
depreciation $4,066 and amortisation $4,392; **income from operations $5,704, 2.1% of revenue**.
A further decline of the same size as FY2025's (−7.0%) removes **$14.3 million of gross profit**
at the FY2025 margin. **Against $5.7 million of operating income that is an $8.6 million
operating loss unless costs come out first.** A decline of **2.8%** — less than half of
FY2025's — takes operating income to zero. This is not hypothetical: **FY2017 through FY2020
were four consecutive net-loss years in this very filing history**, with EBIT on capital employed
at −6.8%, −2.8%, +2.2% and +3.0%.

**Likelihood: [ ] likely [x] a real possibility [ ] a low-level possibility.** It has happened
once in eighteen filed years, the revenue line is guided down again for FY2026, and the cash
buffer is thinner than going into the last episode ($11,972 thousand at 2026-05-31 against
$27,699 thousand at FY2019 year-end). **What makes it a possibility rather than a likelihood is
the balance sheet:** no debt, no covenanted maturity, and $122.9M of customers' money arriving in
advance. **FC does not die of this. It becomes what it was between 2017 and 2020** — a going
concern earning nothing for its owners for several years at a stretch.

**[E4-51] asks whether the holders would accept that as fairly stated.** They would answer that
Enterprise North America invoiced amounts have grown for three consecutive quarters (*"4% growth
in invoiced amounts in the third quarter, or 6% year-to-date"*), that Enterprise deferred revenue
is up 15% year on year, and that **"the Company believes it is well-positioned to deliver net
revenue, Adjusted EBITDA, and Free Cash Flow growth in fiscal 2027 and beyond."** That is the
strongest fact on the other side and it is recorded here rather than buried. It does not change
the Q2 finding, because invoiced growth at flat pricing in a market with twenty-four named
substitutes is volume recovery, not franchise evidence.

**NO VERDICT RECORDED — Q2 closed the file.**

## Q5 — **COMPUTATION — NOT A CLEARANCE**

**⛔ Q5 DID NOT OPEN.** Q2 returned OUT, so under operator rule 2 no Q5 output may be reported
and no box below is ticked. What follows is arithmetic recorded so the next reader need not redo
it, and it carries **no entry language** (operator rule 3). **[E5-42]** is why the order matters:
business quality is judged at Q2–Q4 and *"whether it's a good investment for us depends on how
much we pay for that in the end"* — the price cannot rescue the business.

- Market capitalisation, re-struck by hand: **$195.0M** (11,293,873 × $17.27, 2026-09-18).
- Owner-earnings range, eighteen years reconstructed: **$9.5M to $25.4M**.
- **Implied owner-earnings yield: 4.9% to 13.0%.**
- Sovereign, struck today from the issuing authority: **5.34%**, 2026-09-18, US Treasury daily
  par yield curve, 30-year.
- **The floor [E4-28], for the record only: ~10%.** The **five-year window clears it (13.0%);
  the eighteen-year window does not (4.9%)**; the ten-year window sits at 8.0–9.8%, below it.
- **AND THE UNCOMFORTABLE PART, STATED PLAINLY BECAUSE THE PREVIOUS RUN'S FOLD DID THE SAME:
  at the top of the range the PRICE WAS NEVER THE PROBLEM.** Struck on the window the screen
  used, FC yields 13.0% against a 5.34% bond. **The file closed anyway, and it closed on the
  business.** That is the framework working in the order it is written: a name that fails
  **[E3-03]** is not ranked, whatever the yield. The ordering is **[E2-31]**'s — good economics
  do not rescue what fails the earlier test, and here the earlier test is the franchise.
- **What the range would have meant had the gates cleared.** Under **[E4-25]** a range this wide
  — a factor of 2.7, straddling the floor — is one where *"the range must be so wide that no
  useful conclusion can be reached"*, and **that would itself have been the verdict**. Nothing is
  added on top: no bar is chosen, no margin applied. **Windage count: 0**, because no
  conservatism was spent on a price question that was never reached.

**NO VERDICT RECORDED. NOT RANKED. NOT QUIT ON. THE FILE CLOSED AT Q2.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? *(recorded below the close, NO VERDICT)*

There is no position, so there is no sell rule to pre-commit **[E1-02]**. What is owed instead is
**the falsification condition for the Q2 OUT**, in words — and, per the QLYS ruling, **no price
alert and no `tools/alerts.json` band**, because a name that failed on the business does not get
a price trigger. That is a category error.

**WHAT WOULD PROVE THIS RUN WRONG.** The Q2 OUT rests on four filed series and is falsified by
their reversal, never by the share price:
1. **Pricing conduct.** A filing in which FC discloses a **price increase taken and held** with
   retention intact — **[E4-37]**'s yawn rather than the agony. Nothing in the eighteen years
   read shows one.
2. **The retention metric restored.** A 10-K or release that publishes **AAP revenue retention as
   a number again, above 90%**, would reverse the **[E2-49]** fire and restore the only franchise
   metric FC ever disclosed. Its continued absence confirms it.
3. **Real revenue growth.** Two consecutive years of revenue growth **above US CPI** would break
   the "has not grown in real terms since 2019" finding. FY2026 guidance ($260–267M) does not.
4. **The competitor row.** FC's EBIT on capital employed rising durably **above Korn Ferry's and
   Heidrick's** across a full cycle, rather than for the three years of a wave, would be evidence
   of position rather than surfing **[E3-51]**.

**And the standing caution on this direction of error [E3-47]:** *"Typically, our most egregious
mistakes fall in the omission, rather than the commission, category … their invisibility does not
reduce their cost."* A wrongly-closed file inside the circle of competence is the expensive error
class, and FC **is** inside the circle — Q1 is IN and it was not close. What makes me willing to
close it anyway is that the close is not a forecast; it is a reading of what the filer says about
its own competitive position, its own priced conduct, and its own withdrawn metric. **The way
back in is a franchise finding, not a cheaper price.**

**NO VERDICT RECORDED — Q2 closed the file.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT, file closed.** Q3–Q6
      recorded beneath the close **without verdicts**, per operator rules 2 and 3.
- [x] **No question marked IN carries an "unverified", "general knowledge" or "provisional"
      caveat.** Q1 is the only IN and it rests on the FY2025 10-K read in full.
- [x] No UNRESEARCHED verdict was returned, so no work order is owed.
- [x] No UNKNOWABLE verdict was returned. The Q2 OUT asks the separating question aloud and
      answers it: there is no unread document that would resolve it.
- [x] Step 0: the filing was read, with accession numbers for eight 10-Ks, one 10-Q, five 8-K
      exhibits, two 8-Ks and a proxy; **FY2025 income from operations $5,704 thousand, total
      assets $242,912 thousand and total current liabilities $157,292 thousand were cross-checked
      against the filed statements** and reproduce the series used in the competitor row.
- [x] Owner earnings on a multi-year mean — **eighteen years**, six windows published
      **[E4-38]**, capex band disclosed as a judgment with the filing's own reason.
      **Never a net-income proxy.** SBC subtracted in full in all eighteen years from the filed
      statements, and it did not resolve to zero anywhere.
- [x] Competitor row filled — **six peers plus the subject, twelve years each where reachable,
      each from the peer's own 10-K** — with every unreachable name listed and the reason given.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated: **5.34%,
      2026-09-18, US Treasury daily par yield curve, 30-year**; the currency is argued from the
      filer's own geographic and constant-currency disclosure, not assumed.
- [x] No value range is stated, because Q5 did not open. The owner-earnings range is stated in
      round numbers ($9.5M to $25.4M) under **COMPUTATION — NOT A CLEARANCE**.
- [x] **No bar chosen and no margin applied** — Q5 did not open. **Windage count: 0.**
- [x] Prices dated; the aggregator is used for the live quote only, flagged, with the raw
      response written to the research folder; the share count comes from a **filing cover**
      with its accession and "as of" date.
- [x] Every screen flag resolved by hand **before Q1 opened**, and reported either way.
- [x] Run committed to git after Q2 and again at the fold, each time with a pathspec and a
      freshly written message file.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line:** *Franklin Covey is an understandable, debt-free, customer-funded content and
  consulting business whose own 10-K names twenty-four substitutes and lists "Competitive
  pricing" among the ten factors that decide a sale, whose twelve-year return on capital employed
  (10.9%) is Korn Ferry's rather than Accenture's, and which answered a flat-demand year by
  restructuring rather than raising price while quietly dropping the only retention number it
  ever published — a business, not a franchise **[E3-43]** — and the file closes at Q2 even
  though the screen's own five-year window prices it at a 13.0% owner-earnings yield.*
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
