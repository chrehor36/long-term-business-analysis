# Company Run: Companhia Siderurgica Nacional (NYSE: SID; B3: CSNA3), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Filled top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied to this dated name before any fetch (commit
4291e2d9).

**Quotation marks.** Words from the ledger are in double quotation marks beside their id; words from filings are in single
quotation marks (‘...’) or plain double marks where no id stands beside them.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-13), after the run was committed: not held (`PORTFOLIO.md` carries no line for SID, CSNA3, CSN or Companhia Siderurgica Nacional).

**Dispatched run.** Done by a dispatched analyst under `Screens/_daily/_dispatch_brief.md` with its slots filled. The brief
departs from the canonical brief in one place, which it states: the lines of evidence were not hand-written by the dispatcher;
this analyst derived them from the 20-F's Item 4B, Item 3D and Item 5 (see Step 0, Lines of evidence chosen).

**Contamination, declared and not used.**
- The session context that launched this run showed recent commit subjects of another company's run (GGB, Gerdau, folded
  2026-10-13, with its box and its reasons). Gerdau is one of the steel rivals CSN's 20-F names. Nothing of that run was used;
  steel does not decide this file (Q2, parts table), and no Gerdau filing was read for this run.
- Before the run file existed I listed `Test Runs/` file names through a filter for "SID" or "siderurg", to check that no
  run of this name already existed at today's path. The filter returned four unrelated file names (two 2026-07-15 runs of
  residential REITs, a 2026-10-13 run of a property trust, and an addendum of 2026-10-06 about two other names). None was
  opened. No file about CSN under any name or ticker was returned or opened.
- The memory index loaded with the session carries one-line summaries of the queue's state (counts of gate-clearers, a
  paused wave). No line names CSN. Not used.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** R$ 6.45 a common share (CSNA3, B3, 2026-10-13, Yahoo Finance via `tools/sources.py`; **aggregator, live quote
  only, flagged**). The NYSE ADS (one common share each) was US$ 1.24 the same day, with BRL=X at 5.0264 (same aggregator);
  US$ 1.24 x 5.0264 = R$ 6.23, against R$ 6.45 on B3. The home listing in the earnings currency is used throughout.
- **Shares by class** from the latest annual filing's cover: 1,326,093,947 common shares, one class (20-F for FY2025, filed
  2026-04-30, accession `0001292814-26-002714`; `python Screens/cover_shares.py SID` returned the same figure). Checked:
  note 25 of the same 20-F gives outstanding shares 1,326,093,947, 100%, and the weighted average used for per-share
  loss is the same number, so no parent treasury shares are netted; the repurchase of treasury shares in the six months
  to 2026-06-30 (R$ 128.5m, ITR on 6-K `0001292814-26-004375`) is shown as "Effect of treasury shares acquired by parent
  companies" and arises in the listed subsidiary CSN Mineracao, not in CSN's own count. No 6-K after the 2Q26 interim
  report changes the count (the 6-Ks of 2026-09-02, 09-14, 09-29 and 10-09 were read).
- **Market cap:** R$ 8,553m (1,326.094m x R$ 6.45).
- **Sovereign for the earnings currency (BRL):** **12.57%**, Tesouro Prefixado com Juros Semestrais (NTN-F) maturing
  2037-01-01, purchase rate (Taxa Compra Manha), base date 2026-10-09, from the Brazilian National Treasury (Tesouro
  Nacional) file `PrecoTaxaTesouroDireto.csv` on tesourotransparente.gov.br, fetched 2026-10-13. It is the longest nominal
  (fixed-rate) Treasury issue in the file; the 2035 issue was 12.61% and the 2033 issue 12.59% the same day. `tools/sources.py`
  has no BRL source configured (it says so), so the file was read directly.
- **Filings read** (operator rule 4):
  - 20-F FY2025, filed 2026-04-30, `0001292814-26-002714`: Items 3D, 4B, 5, 6, 7, 8A and the audited statements with notes
    (balance sheet, income, cash flows, note 14 debt, note 18 advances from customers, note 31 segments).
  - 20-F FY2022, filed 2023-04-28, `0001292814-23-001912` (cash flows and segment results 2020 to 2022, balance sheets 2021
    and 2022); 20-F FY2019, filed 2020-04-03, `0001292814-20-001135` (cash flows 2017 to 2019); 20-F FY2017, filed
    2018-05-01, `0001292814-18-001534`.
  - Interim statements at 2026-06-30 (ITR, 6-K filed 2026-08-27, `0001292814-26-004375`) and the 2Q26 results release
    (6-K filed 2026-08-13, `0001292814-26-004216`).
  - The fourth-quarter results releases FY2016 to FY2025 on 6-K (accessions `0001292814-17-002646`, `-18-000845`,
    `-19-000404`, `-20-000608`, `-21-000527`, `-22-000856`, `-23-000810`, `-24-000690`, `-25-000842`, `-26-000805`), for
    the mining segment's adjusted EBITDA, margin and C1 cost by year (the FY2019 and FY2020 releases did not parse to text;
    their years are filled from the neighbouring releases where those state the comparison, and marked).
  - Material facts on 6-K: 2026-08-10 (`0001292814-26-004156`, binding proposals for CSN Cimentos), 2026-08-11
    (`0001292814-26-004186` and `-004188`, the CSN Inova notes exchange), 2026-09-02 (`0001292814-26-004460`, Chairman and
    CEO), 2026-09-14 (`0001292814-26-004556`, board and officers list), 2026-09-29 (`0001292814-26-004734`, mining guidance
    cut), 2026-10-09 (`0001292814-26-004888`, SWT term sheet).
  - A 20-F filer files no proxy; pay, control and related parties were read from Items 6 and 7 of the FY2025 20-F.
- **One figure cross-checked against the filed statement:** net cash generated by operating activities FY2024, R$ 8,651m in
  the SEC XBRL company facts, against R$ 8,650,505 thousand on the face of the FY2025 20-F's cash flow statement: agrees.
  A second check failed and is recorded: the XBRL instants for property, plant and equipment at 2021-12-31 read R$ 26,370m
  when taken from the latest-filed fact, while the FY2022 20-F's balance sheet gives R$ 21,531m for 2021 and R$ 26,370m
  for 2022. The XBRL instants for 2020 to 2022 are shifted in a later filing; every balance-sheet figure below is taken from
  the year's own 20-F.
- **`tools/run.py SID`** (run as `--currency BRL --years 5 --quote CSNA3.SA`) printed the price and then refused: "CURRENCY
  MISMATCH: earnings in USD, quote in BRL. Refusing to convert." (some of SID's XBRL cash-flow tags carry USD units beside
  BRL), and it has no BRL sovereign. As the brief allows, **the arithmetic was done by hand from the filed statements**
  (`Test Runs/_research 2026-10-13 SID/owner_cash.py`, output in `owner_cash_out.txt`). Nothing the tool printed was used
  beyond the price line.
- **Owner cash, by hand** (R$ millions; cash from operations is after interest paid and after taxes paid, since the filer
  classifies both inside operating activities; capital spending is "purchase of property, plant and equipment, intangible
  assets and investment property"):

| Year | Operating cash as filed | Capital spending | Customer advances inside operating cash | Forfaiting inside operating cash | Owner cash as filed (after interest) | Owner cash recast (advances and forfaiting out) | Interest paid | D&A | Revenue |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 276 | 1,632 | 0 | 0 | -1,356 | -1,356 | 3,050 | 1,322 | 17,149 |
| 2017 | 572 | 1,060 | 0 | 0 | -488 | -488 | 2,635 | 1,453 | 18,525 |
| 2018 | 2,208 | 1,319 | 0 | 0 | 889 | 889 | 2,142 | 1,273 | 22,969 |
| 2019 | 4,872 | 2,217 | 2,525 | 0 | 2,655 | 130 | 2,039 | 1,519 | 25,436 |
| 2020 | 9,577 | 1,684 | -10 | -497 | 7,893 | 8,400 | 1,922 | 2,522 | 30,064 |
| 2021 | 14,793 | 2,865 | -697 | 3,816 | 11,928 | 8,809 | 2,138 | 2,218 | 47,912 |
| 2022 | 2,043 | 3,352 | -221 | 1,269 | -1,309 | -2,357 | 2,316 | 2,878 | 44,362 |
| 2023 | 7,293 | 4,408 | 4,844 | -1,500 | 2,885 | -459 | 3,429 | 3,379 | 45,438 |
| 2024 | 8,651 | 5,494 | 6,968 | -1,328 | 3,157 | -2,483 | 4,052 | 3,791 | 43,687 |
| 2025 | -973 | 5,936 | -510 | 5 | -6,909 | -6,404 | 4,268 | 4,150 | 44,798 |

  Five-year average 2021 to 2025: owner cash as filed R$ 1,950m; recast R$ -579m. Ten-year average 2016 to 2025: as filed
  R$ 1,934m; recast R$ 468m. Stock pay: no share-based plan of size found in the cash flow or note 25 (the 20-F's key
  management compensation is cash); none to resolve. Cash paid for businesses, net of businesses sold: 2018 R$ -1,451m (the
  sale of CSN LLC), 2019 R$ 210m, 2020 R$ 132m, 2021 R$ 1,233m (Elizabeth and the Lafarge deposit), 2022 R$ 8,005m
  (LafargeHolcim Brasil, CEEE-G, Chapeco, Topazio, concession rights), 2023 R$ 339m, 2024 R$ 32m, 2025 R$ 293m (Gramperfil,
  Grupo Estrela, Galvacolor, Global Dot, less a R$ 43m sale of equity assets). Sales of minority stakes in CSN Mineracao (2021 R$ 3,165m; 2024 R$ 4,420m, "Receipt of sale
  of equity interest", the 10.74% stake sold to Itochu, Item 5) are equity raised in a subsidiary that stays controlled, and are left out of owner cash.
- **Why the advances and forfaiting are taken out (CONVENTION of this run, rationale in one line: a prepayment for ore to be
  delivered later and a bank-financed payable are borrowings in substance, and counting them as owner cash would add debt to
  earnings).** Note 18 of the FY2025 20-F: advances from customers R$ 13,375m at 2025-12-31, of which iron ore R$ 11,598m,
  "iron ore supply contracts with important international players", each a dollar sum for a tonnage over three to five
  years (for example 2024-09-25, US$ 450 million, 9.7 million tons, 4 years). The ore is delivered later against cash
  already spent. The balance is carried as debt beside the central figure at Q7.
- **Lines of evidence chosen, and why** (the brief's stated departure). From Item 4B: the five segments and note 31's
  segment results, to find which part decides; the mining section (production by mine, third-party purchases, reserves and
  grades, pit-optimization costs) because mining decides; the steel competition section, which names Gerdau, Usiminas,
  ArcelorMittal Tubarao, Ternium Brasil; the mining industry overview, which names Vale, Samarco, Anglo American and
  Simandou. From Item 3D: steel import pressure, protectionist measures, commodity price exposure, reserve estimates,
  controlling-shareholder risk. From Item 5: the segment tables 2024 and 2025, capital spending by segment, debt
  composition (36.7% in reais, the rest in dollars), macro table (average BRL rate, CDI). Because the deciding part is a
  commodity, the line of evidence that matters most is the cost position against the rivals, read from each filer's own
  reports (Q2, A commodity business).
- **The balance sheets, eight to ten years, read here in Step 0 because the file closes before Q4** (R$ millions; each
  year from its own 20-F; 2016 and 2019 from the XBRL facts of the following year's filing):

| Year-end | Total assets | Cash + current investments | Receivables | Inventories (current + non-current) | PP&E | Intangibles incl. goodwill | Borrowings (gross) | Net borrowings | Equity, controlling | Non-controlling | Revenue that year |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 44,154 | 5,631 | 1,905 | 3,964 | 18,136 | 7,258 | 30,441 | 24,810 | 6,195 | 1,190 | 17,149 |
| 2017 | 45,210 | 4,148 | 2,197 | 4,464 | 17,965 | 7,272 | 29,511 | 25,363 | 7,027 | 1,261 | 18,525 |
| 2018 | 47,328 | 3,144 | 2,078 | 5,040 | 18,047 | 7,253 | 28,827 | 25,683 | 8,703 | 1,311 | 22,969 |
| 2019 | 50,869 | 3,722 | 2,048 | 5,427 | 19,701 | 7,232 | 27,967 | 24,245 | 10,175 | 1,187 | 25,436 |
| 2020 | 63,002 | 13,728 | 2,867 | 5,165 | 19,716 | 7,317 | 35,270 | 21,542 | 9,913 | 1,338 | 30,064 |
| 2021 | 79,379 | 19,291 | 2,598 | 11,600 | 21,531 | 7,657 | 32,508 | 13,217 | 20,315 | 3,059 | 47,912 |
| 2022 | 85,354 | 13,448 | 3,233 | 12,335 | 26,370 | 10,788 | 40,919 | 27,472 | 19,489 | 2,327 | 44,362 |
| 2023 | 91,530 | 17,579 | 3,270 | 10,970 | 27,927 | 10,536 | 44,859 | 27,280 | 17,501 | 2,184 | 45,438 |
| 2024 | 103,907 | 24,221 | 2,901 | 12,201 | 30,426 | 10,438 | 56,915 | 32,694 | 12,271 | 3,188 | 43,687 |
| 2025 | 100,575 | 15,064 | 2,397 | 12,529 | 33,919 | 11,006 | 52,925 | 37,861 | 12,876 | 2,860 | 44,798 |
| 2026-06-30 | 100,602 | 14,286 | 2,532 | 11,620 | 34,534 | 10,900 | 53,366 | 39,080 | 12,166 | 3,074 | (half year) |

  What moved and why, "what the figures are saying and what they don't say and what they can't say" **[M2025-032]**: net
  borrowings fell from R$ 25bn to R$ 13.2bn in the 2020-2021 boom and then rose every year after, to R$ 37.9bn at 2025 and
  R$ 39.1bn at 2026-06-30 (borrowings only; leases of R$ 1.0bn are carried separately in the notes), while revenue was flat from 2021 to 2025 (R$ 47.9bn, 44.4, 45.4, 43.7, 44.8). Beside the
  borrowings sit R$ 13.1bn of customer advances (2026-06-30, "contracts liabilities"), where the 2021 balance sheet showed R$ 2.1bn of current advances, and
  R$ 1.5bn to 5.7bn of forfaited payables in each year since 2021. The controlling shareholders' equity doubled to R$ 20.3bn
  in 2021 and has since fallen to R$ 12.2bn; the earnings reserves are exhausted (nil at 2026-06-30, against R$ 9.9bn at
  2021) and the half-year loss is R$ 1,613m. Against that equity stand intangibles of R$ 10.9bn and deferred tax assets of
  R$ 7.35bn (2026-06-30), an asset whose value depends on future taxable profit; the controlling equity less both is
  negative by about R$ 6.1bn. Inventories rose from 23% of revenue (2016) to 28% (2025), the non-current part growing from
  nil to R$ 2.1bn; receivables fell from 11% to 5% of revenue while payables were forfaited, so part of working capital is
  carried by banks on both sides. Gross borrowings at 2025 were "336.3% of shareholders' equity" (20-F Item 5). What the
  figures cannot say: the BRL value of the debt in dollars (36.7% of debt is in reais and "substantially all of the remaining balance" in dollars, Item 5) moves with the currency, and the tax assessments the
  company rates "possible" (Item 8A, over R$ 15bn named: Namisa capital gain R$ 6,544m, Namisa goodwill R$ 1,874m and
  R$ 380m, prepayment interest R$ 907m and R$ 1,357m, CFEM royalty R$ 1,715m, PIS/COFINS R$ 1,875m, ICMS R$ 1,309m) are not
  on the balance sheet at all.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own it "if the market closed for five years" **[M1997-109]**,
and the business here is mostly a seller of iron ore and steel whose cash is spoken for by its lenders first. The market is "there to serve us" and "doesn’t tell us anything. It just tells us prices." **[M2006-077]**: a price of R$ 6.45, down to a market value of R$ 8.6bn against R$ 39bn of net
borrowings, says nothing by itself. Macro conclusions "just never enter into the discussion" **[M2000-094]**: no forecast of the iron ore price, the real or
Brazilian rates is made here. On who is paid to tell you, "you do not get impartial advice from Wall Street" **[M2020-037]**, and the company's releases lead with ‘Adjusted EBITDA’
and ‘Net Debt/EBITDA’ (2Q26 release, 3.49x), figures before capital spending. Of the margin of safety, if a decision needs pencil and paper "it’s too close to think about" **[M1996-084]**. **Contrary evidence, written down as found** **[M1997-127]** (the research notes
`_notes.md` carry each item in the order it was found): operating cash of R$ -973m in 2025; R$ 11.8bn of customer advances
inside 2023-2024 operating cash; a net loss to the controlling shareholders in 2023, 2024, 2025 and the first half of 2026;
a mining margin below Vale's in every year read; the 2026-09-29 cut of mining volume guidance with C1 cost guidance raised;
a notes exchange that moved a 6.75% coupon to 11.00%.

## THE STANDING RULE
Owning a part-interest bought with the buyer's own money, unlevered and sized so that a total loss is survivable, does not
put the buyer at risk of ruin; "We are never going to risk what we have and need for what we don't have and don't need"
**[M2012-081]**, and the one road to ruin, borrowing that can call, is the buyer's choice, not the target's **[M2004-065]**,
**[M2006-079]**. A purchase on margin of a stock this levered would breach it. Not breached as stated.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**, not knowledge of the
  product **[M2011-014]**. CSN reports five segments with different economics, so it is read by its parts, and a part
  matters when it decides under Q2's business-of-parts convention (more than half of five-year operating profit, or else the
  largest). From note 31 (proportional consolidation), the segment operating results 2021 to 2025 sum to: mining R$ 29,306m,
  steel R$ 10,720m, logistics R$ 4,653m, cement R$ 1,899m, energy R$ 448m; **mining is 62% of the five-segment total and
  decides** (Q2, parts table). The other parts do not decide and do not keep the whole outside the circle.
- **The key variables of the deciding part**, "trying to identify the key variables in that particular business, and evaluating how predictable they were first" **[M1998-044]**: tonnes sold (45.8 Mt in 2025, of which 12.4 Mt bought from
  third parties), the grade and cost of the tonne (C1 cash cost US$ 20.4 to 24.0/t in the quarters 4Q24 to 2Q26, from the
  company's releases), freight to China, and the seaborne price. Volume and cost are foreseeable from the filings: Casa de
  Pedra carries 1,180.4 Mt of reserves at 40.7% Fe (37.0 Mt proven, 1,143.4 Mt probable) and Engenho 151.1 Mt (20-F FY2025,
  Item 4B), against own production of about 33.7 Mt of product in 2025, and the pit-optimization table states the costs of
  the next ore (P15 itabirite processing at 43.8% mass recovery). The price is not foreseeable and is not asked to be: a
  commodity price is never by itself a STOP at Q1, "We don't think we can predict commodity prices." **[M2016-025]**, and the
  business is judged off its figures, "So if you can't make a decision on something like PetroChina off the figures, forget
  about going further" **[M2008-069]**. The figures needed (cost per tonne, margin per tonne, against the rivals) are
  published by the company and its named rival.
- **Abroad.** Brazil is inside the perimeter on the speakers' own terms, "we understand the nuances of the corporate
  governance system and taxation" **[M2000-141]**; of Brazil by name, "Brazil would not be off limits at all, but we'd have
  to be able to get a lot of money into a business we understood at an attractive price. We would want it to be cheaper
  than if it were in the United States." **[M2006-021]**. Control (Item 7A): Vicunha Acos 41.66% and Rio Iaco 3.45%, owned
  indirectly by the Steinbruch family; Avelina 3.98% and CFL Ana 4.70% are listed without that footnote; ADSs 24.20%. The
  controlling shareholder "has the ability to direct our business and affairs" (Item 3D heading). The tax system's reach is
  visible in Item 8A's assessments, which are disclosed by amount and stage. The governance is that of a family-controlled
  Brazilian company with a listed mining subsidiary; it is readable from the filings.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn't." **[M2002-092]**. The
  deciding part is a mine, a rail line and a port, whose economics can be stated in tonnes and dollars a tonne; I do not
  doubt that it can be understood. The confusing items found (the advances, the forfaiting, the intercompany prepayment
  contracts listed in note 18 under "Intercompany agreements entered by and between subsidiaries") bear on the accounts
  (Q4), not on whether the business can be foreseen.
- **VERDICT: IN.** The deciding part, iron ore mining, can be understood from its figures **[M2008-069]**, **[M2012-065]**;
  its price is not forecast and does not need to be at this question: "We don’t think we can predict commodity prices." **[M2016-025]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing?" **[M1995-038]**; a moat is what "protects excellent returns on invested
capital" **[L2007-004]**.

**The parts table** (note 31 of the FY2025 20-F `0001292814-26-002714` for 2023 to 2025 and note 31 of the FY2022 20-F
`0001292814-23-001912` for 2021 and 2022; ‘Operating result before Financial Income and Taxes’, proportional consolidation
of MRS; corporate expenses and eliminations, R$ -4,573m over the five years, are not a part). The parts are read
separately, since "lumping them together, as is done in standard financial statements, impedes analysis." **[L2008-005]**.

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year sum (R$m) | Share | Castle | Decides |
|---|---|---|---|---|---|---|---|---|---|
| Mining (CSN Mineracao, iron ore; tin) | 9,698 | 4,618 | 5,808 | 4,612 | 4,570 | 29,306 | 62.3% | open: not the low-cost producer (below) | **yes** |
| Steel (Volta Redonda, packaging, Lusosider, SWT, CSN LLC) | 8,447 | 3,992 | -574 | -735 | -409 | 10,720 | 22.8% | open: three operating losses, imports at a fifteen-year high | no |
| Logistics (port, rail incl. 37.49% of MRS, road from 2025) | 545 | 726 | 950 | 1,287 | 1,146 | 4,653 | 9.9% | not judged | no |
| Cement (being sold, 6-K 2026-08-10) | 283 | 354 | 55 | 471 | 737 | 1,899 | 4.0% | not judged | no |
| Energy | 86 | 1 | 235 | -7 | 133 | 448 | 1.0% | not judged | no |

Mining carries more than half of the five-year segment total, so the file closes on mining's castle. Steel, which does not
decide, is shown open on the company's own figures and is carried to Q7 as an ordinary business at no growth.

**A commodity business.** Iron ore is sold against an index; note 18 of the 20-F records ‘payments received in excess due to
adjustments by the Platts index quotation that determines the price practiced in iron ore sales contracts.’ The price is not forecast here: "We don’t think we can predict commodity prices." **[M2016-025]**. The question the text puts is whether CSN Mineracao is the
low-cost producer, read from its own and its rivals' filings: "we would measure it, probably, more by cost of production
than we would by whether copper was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**; "It’s like comparing a
copper producer whose costs are $2.50 a pound with a copper producer whose costs are $1 a pound. Those are two different
kinds of businesses." and "The figures are available." **[M2009-059]**. The measure is against the major competitors, not
absolute: "if your costs are on parity or less" [...] "than your other major competitors, that is much more important to
you than the absolute level" **[M2001-013]**.

**The competitor row.** The 20-F names, for iron ore, CSN Mineracao, Vale, Samarco and Anglo American as Brazil's
established miners, and Australia (by country) and the Simandou project in Guinea as supply (Item 4B, Overview of Mining
Industry). Of these, **Vale files with the SEC** (20-F) and is the comparison; **Samarco and Anglo American do not file with
the SEC and are flagged, not read**. For steel the 20-F names Gerdau, Usiminas, ArcelorMittal Tubarao and Ternium Brasil;
steel does not decide, so no steel rival was read (Usiminas is not an SEC filer; Gerdau, ArcelorMittal and Ternium are).
Same metric from each filer's own reports, over the whole span read:

| Year | CSN mining adjusted EBITDA margin (CSN 4Q releases) | Vale iron ore fines adjusted EBITDA / iron ore revenue (Vale 20-Fs) | Gap |
|---|---|---|---|
| 2016 | about 38% (R$ 1,759m on about R$ 4,575m; the revenue backed out of "R$ 4,621 million, 1% higher than in 2016", 4Q17 release) | 53.5% (8,445 / 15,784) | about -15 pts |
| 2017 | 42.1% (1,947 / 4,621) | 54.3% (10,051 / 18,524) | -12.2 pts |
| 2018 | not computed (EBITDA R$ 2,621m; segment revenue not read) | 54.2% (11,033 / 20,354) | n/a |
| 2019 | not read (the 4Q19 release did not parse) | 57.4% (13,398 / 23,343) | n/a |
| 2020 | about 65.4% (2021's 60% stated as "5.4p.p. lower than" 2020, 4Q21 release) | 67.4% (18,270 / 27,123) | about -2 pts |
| 2021 | 60% (R$ 10.7bn) | 69.1% (26,471 / 38,324) | -9.1 pts |
| 2022 | about 48.5% (about R$ 6,070m, backed out of 2023's R$ 7,843m "an increase of 29.2%", on R$ 12,525m) | 55.6% (15,670 / 28,188) | about -7 pts |
| 2023 | 45.8% (7,843 / 17,136) | 54.8% (15,205 / 27,760) | -9.0 pts |
| 2024 | 44.3% (R$ 5.8bn) | 46.8% (11,598 / 24,805) | -2.5 pts |
| 2025 | 41.0% (R$ 6,309.1m on R$ 15,400.5m) | 46.2% (11,562 / 25,010) | -5.2 pts |

Margin per tonne sold, the better measure because it does not depend on the mix of FOB and CFR sales: CSN at the 20-F's
average BRL rate for the year (2021 R$ 5.340, 2024 R$ 5.3885, 2025 R$ 5.5861), Vale on iron ore fines tonnes:

| Year | CSN mining EBITDA per tonne sold | Vale iron ore fines EBITDA per tonne sold | CSN as a share of Vale |
|---|---|---|---|
| 2021 | US$ 60.3 (R$ 10,700m / 33.237 Mt) | US$ 97.7 (26,471 / 270.885 Mt) | 62% |
| 2024 | US$ 25.3 (about R$ 5,799m / about 42.57 Mt) | US$ 44.6 (11,598 / 260.314 Mt) | 57% |
| 2025 | US$ 24.6 (R$ 6,309.1m / 45.849 Mt) | US$ 42.3 (11,562 / 273.027 Mt) | 58% |

Accessions: Vale 20-F FY2025 `0001292814-26-001844`, FY2022 `0001292814-23-001516`, FY2019 `0001047469-20-002065`, FY2017
`0001047469-18-002777`; CSN releases as listed in Step 0. Caveats, stated: Vale's figure is iron ore fines alone (its pellets
excluded); CSN's includes 12.4 Mt of ore bought from third parties in 2025 (27% of tonnes sold) and the dry-processed Pires
product at 53.7% Fe; each filer defines its own adjusted EBITDA. None of the caveats runs in CSN's favour: the bought ore and
the low-grade product are part of why its tonne earns less.

**The low-cost position, the test that decides.** On every year read the deciding part earned less than the one named rival
that files: a margin below Vale's in each of the eight years with both figures, by about 2 to 15 points, and 57% to 62% of
Vale's EBITDA per tonne in 2021, 2024 and 2025. Vale's own filing then places Vale itself behind the Australian producers on
the freight to the main market: its main Asian competitors are ‘located in Australia and include subsidiaries and affiliates
of BHP Group Limited (BHP), Rio Tinto Ltd (Rio Tinto) and Fortescue Metals Group Ltd’, and it sells ‘on a CFR basis, despite
higher freight costs compared to Australian producers’ (Vale 20-F FY2025, Item 4, Competition). CSN ships from the same
southeastern Brazil to the same China (85.3% of 2025 iron ore export sales to the Asian market, mainly China, 20-F Item 4B).
So CSN Mineracao is on parity neither with its Brazilian rival nor with the Australian majors on the earnings of the
delivered tonne **[M2001-013]**. And the field is already pushing on its marginal tonnes: the 6-K of 2026-09-29
(`0001292814-26-004734`) announced ‘a temporary reduction in the production of lower-grade iron ore at the dry processing
plant of the Pires Complex’, a decision reflecting ‘more challenging market conditions, including pressure from higher
freight costs’; it cut 2026 production and purchases guidance from 45.0 to 47.0 Mt to 39.0 to 41.0 Mt and raised C1 cash
cost guidance from US$ 22.0 to 23.5/t to US$ 25.0 to 26.0/t. That is the rows' failing answer in a filing: "commodity
businesses have risk unless you’re the low-cost producer, because the low-cost producer can put you out of business."
**[M1997-010]**; "a company must lower its costs to competitive levels or face extinction." **[L1994-035]**.

**The other castle tests, each with its filing fact.**
- *Pricing power and the agony before a rise.* None: the price is the index's, adjusted after shipment; the business takes
  its price from the field, "whatever he charged for gas was my price." **[M2012-109]**; "he determined our profit, because
  we looked at his price every day." **[M2023-079]**.
- *The attacker with money.* The 20-F itself names one: Simandou, which ‘commenced operations in November 2025 and is
  expected to reach a maximum capacity of up to 120 Mt per year’, against CSN's 41.8 Mt sold to third parties in 2025. The
  rows' answer for a business an attacker with money could take: "If the answer had been yes, we wouldn’t have done it."
  **[M2011-015]**; "one competitor is frequently enough to ruin a business." **[M2012-108]**.
- *Brand, share of mind, the low bid.* The customer is a steel mill buying a specification of iron content and impurities,
  on grade and delivered price. The filing makes no brand claim for the ore.
- *Widening or narrowing.* "whether it’s likely to widen further or shrink on you" **[M1999-108]**: narrowing on the
  filings. C1 cost rose from US$ 20.4/t (4Q24) to US$ 24.0/t (2Q26) and is now guided at US$ 25.0 to 26.0/t; the mining
  margin fell from 60% (2021) to 41.0% (2025) and 32.0% in 2Q26 (release `0001292814-26-004216`); the reserves that carry
  the next decade are itabirite (Casa de Pedra reserves at 40.7% Fe, 37.0 Mt proven of 1,180.4 Mt), for which the
  pit-optimization table gives a P15 mass recovery of 43.8% against 82.4% for the current PC/OS circuit, so each tonne of
  product will take about twice the ore. The competitive position "grows either weaker or stronger" **[L2005-010]**; the
  filings show it weaker, and "you do not want to have something whose competitive position is going to erode over time."
  **[M2007-117]**.
- *What could destroy, modify or reduce it.* New supply (Simandou), the freight gap, and the move to lower-grade ore are each
  named in the filings, and each is a thing that could "destroy, or modify, or reduce the economic strengths" of the deciding part **[M2000-014]**.
- *The field's returns over the last full cycle.* Not ordinary: Vale's iron ore fines earned an adjusted EBITDA margin of 46%
  to 69% in every year 2016 to 2025 read. The field protects excellent returns for its low-cost producers; the file does not
  close on "ordinary returns" but on CSN Mineracao's place in the field. A change for the better is not at issue: the trend
  in the filings runs the other way.
- *Steel, which does not decide.* Operating losses in 2023, 2024 and 2025; "imports of rolled steel into Brazil increased by
  20.5% in 2025 compared to 2024, reaching 5.7 million tons, the highest level in 15 years" (Item 3D); the 4Q25 release
  records losses from "operational idleness" at the Blast Furnace No. 2 shutdown. Carried to Q7 at no growth.

**Price does not reopen it.** "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**;
and an outcome left to the price of the commodity is a bet on the price, "If you own oil, you should only own oil, if you
expect these prices to go up significantly." **[M2020-035]**, which this run does not make.

- **VERDICT: OUT.** The deciding part sells a commodity at the field's price and is not the low-cost producer: on its named
  rival's own filings it earned a lower margin in every year read 2016 to 2025 and under two-thirds of the rival's EBITDA per
  tonne in 2021, 2024 and 2025; the rival's filing puts Brazilian ore behind Australian ore on freight; and CSN's own 6-K of
  2026-09-29 cuts its marginal low-grade tonnes for ‘pressure from higher freight costs’ while raising its cost guidance.
  The castle is shown open on the evidence **[M1997-010]**, **[M2001-013]**, **[M2009-059]**, **[L1994-035]**,
  **[M2012-109]**; the box is OUT among the three **[M2006-013]**.

## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the Q2 STOP closed the file; facts found are under AFTER THE STOP).

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict. The eight to ten balance sheets were read in Step 0, as the template asks when the file closes before Q4; the facts found are under AFTER THE STOP.

## Q5: WHO RUNS IT. NOT REACHED.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.

## Q7: WHAT IS IT WORTH. NOT REACHED as a verdict; the arithmetic the owner asked for is below, under COMPUTATION, NOT A CLEARANCE.

## Q8: IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.

## Q9: COULD IT RUIN US. NOT REACHED.

## Q10: IS IT THE FAT PITCH. NOT REACHED.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED (no business the rows name; not asked).

---
## THE BOX
**OUT at Q2** (the castle shown open on the evidence: the deciding part, iron ore mining at 62% of five-year segment
operating result, sells a commodity at the field's price and is not the low-cost producer against its named SEC-filing rival
Vale, nor, on Vale's own filing, against the Australian producers; CSN's own 6-K of 2026-09-29 cuts its low-grade tonnes for
freight pressure and raises its cost guidance); **integrity facts recorded, not judged**. Q7 not reached; beneath the stop the
computation finds no positive value per share on the all-equity basis (R$ -15.43 to R$ -13.07 against R$ 6.45) and no case
that earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts already found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged, operator rule 2.)*

**Bearing on Q3 (capital).** Capital spending rose from R$ 1,060m (2017) to R$ 5,936m (2025) while revenue was flat from 2021
(R$ 47.9bn) to 2025 (R$ 44.8bn); spending exceeded depreciation, amortization and depletion in each year 2021 to 2025 by
R$ 0.5bn to 1.8bn (cash flow statements). The 2025 spending by segment: steel R$ 2,427m ("productivity and modernization
projects [...] major overhauls of coke batteries"), mining R$ 2,397m ("mining expansion projects, investments in tailings
filtering and expansion of the Itaguai port"), cement R$ 641m ("sustaining projects"), logistics and energy R$ 498m (20-F
Item 5). The consolidated operating result in 2025 was R$ 4,817m against PP&E of R$ 33,919m and intangibles of R$ 11,006m.

**Bearing on Q4 (the accounts).**
- The releases lead with ‘Adjusted EBITDA’ and state leverage as "Net Debt/LTM EBITDA" (3.49x at 2Q26, release
  `0001292814-26-004216`); EBITDA is in the filer's own mouth in every release read.
- Guidance is given and revised: 2026 production and purchases 45.0 to 47.0 Mt cut to 39.0 to 41.0 Mt, C1 cost US$ 22.0 to
  23.5/t raised to US$ 25.0 to 26.0/t (6-K `0001292814-26-004734`).
- Operating cash includes customer prepayments for iron ore and energy (R$ 4,844m in 2023, R$ 6,968m in 2024, R$ 2,525m in
  2019) and bank-financed payables ("forfaiting", R$ 3,816m in 2021, R$ 1,269m in 2022); recast in Step 0.
- Note 18 lists, inside the consolidated contract liabilities, a schedule headed "Intercompany agreements entered by and
  between subsidiaries" (six contracts of November and December 2025, US$ 150m to 405m each); the note does not say why an
  intercompany contract appears in a consolidated liability. Knowable from a filing not yet read (the subsidiaries'
  statements); not resolved here.
- Deferred tax assets R$ 7,354m (2026-06-30) against a net loss to the controlling shareholders in 2023, 2024, 2025 and the
  first half of 2026.
- The auditor changed for FY2025: Forvis Mazars Auditores Independentes signs the FY2025 opinion ("We have served as the
  Company's auditor since 2025"); Grant Thornton "served as the Company's auditor from 2017 to 2025" and signs FY2024 and
  FY2023 (20-F FY2025, audit reports).
- SEC XBRL instants for 2020 to 2022 are shifted against the filed statements (Step 0).

**Bearing on Q5 (the people): integrity facts recorded, not judged.**
- Control: Vicunha Acos 41.66% and Rio Iaco 3.45%, "Owned indirectly by the Steinbruch family, which includes Mr. Benjamin
  Steinbruch, a member of our board of directors and our chief executive officer" (Item 7A). Mr. Steinbruch, first elected to
  the board 1993-04-23, became Chairman with Fabio Schvartsman as CEO from 2026-09-03 (6-Ks `0001292814-26-004460` and
  `0001292814-26-004556`).
- Related parties named in Item 7B include Banco Fibra, Vicunha Imoveis and Vicunha Servicos; the company "guarantee[s]
  certain indebtedness of related parties" (Item 7B).
- Tax assessments over the Namisa transactions with the Asian Consortium, rated "possible" by the company: an alleged
  untaxed capital gain (R$ 6,544m, upheld by CARF, now in the courts), goodwill amortization 2008 to 2011 (R$ 1,874m,
  reinstated by the Superior Chamber of CARF) and 2013 to 2014 (R$ 380m, upheld), and "allegedly improper deduction of
  interest expenses in pre-payment contracts between us and Namisa" (R$ 907m and R$ 1,357m) (Item 8A).
- CADE: a 2014 performance agreement (TCD) requires CSN to reduce its stake in Usiminas, rival steelmaker, with political
  rights suspended meanwhile; the timeframe has been extended twice (Item 8A).
- Any later run that reaches Q5 must answer these.

**Bearing on Q6 (the money and the owners).** Dividends and interest on equity paid: R$ 3,291m (2021), 3,757m (2022), 3,981m
(2023), 2,535m (2024), 695m (2025), R$ 14.3bn in five years, while net borrowings rose from R$ 13.2bn to R$ 37.9bn and the
controlling shareholders recorded net losses in 2023 to 2025 (part of the payout is to CSN Mineracao's minority holders; the
split was not read). Share repurchases in the consolidated cash flow R$ 1,516m (2021) and R$ 411m (2022); the R$ 336m repurchase in the FY2025
statement is CSN Mineracao's programme. Cash acquisitions R$ 8.0bn net in 2022 (LafargeHolcim Brasil R$ 4,770m less cash
acquired, CEEE-G, Chapeco, Topazio, concession rights R$ 2,024m); the cement business so bought is now offered for full
divestment (binding proposals, 6-K `0001292814-26-004156`), and SWT is under a binding term sheet at an enterprise value of
EUR 550 million (6-K `0001292814-26-004888`). Minority stakes in CSN Mineracao sold: the 2021 offering (R$ 3,165m) and 10.74%
to Itochu (R$ 4,420m received in 2024). The buyback test against the bottom of the Q7 range: the computation below gives a
negative bottom on the all-equity basis, so every price paid sat above it (recorded, not weighed).

**Bearing on Q9 (could it ruin us).** Gross borrowings R$ 53.4bn and leases R$ 1.0bn at 2026-06-30 against cash and
investments of R$ 14.3bn; customer advances R$ 13.1bn to be repaid in ore and energy; forfaited payables R$ 1.5bn. Debt is
36.7% in reais, the rest substantially in dollars; short-term debt 19.7%; average life "approximately 42 months" (Item 5).
The CSN Inova exchange of August 2026 moved US$ 1,007m of 6.750% notes due 2028 into US$ 698.3m of 11.00% notes due 2030
plus US$ 255.7m of cash (6-Ks `0001292814-26-004186` and `-004188`). Tax contingencies rated possible and not provisioned
exceed R$ 15bn (Step 0). The 20-F says that if the ADS price falls below NYSE minimums "we may be required to effect a
reverse stock split or change the ratio of common shares represented by each ADS" (Item 3D); the ADS closed 2025 at US$ 1.60
and traded at US$ 1.24 on 2026-10-13.

## COMPUTATION, NOT A CLEARANCE
*(Q7's arithmetic, reported at the owner's request under Part VII, The owner's price; it is not a verdict, carries no entry
language, and does not reopen the Q2 STOP. Scripts: `owner_cash.py`, `value.py`; outputs `owner_cash_out.txt`,
`value_out.txt`.)*
- **Cash input.** Owner cash recast as in Step 0 (customer advances and forfaiting taken out of operating cash, a CONVENTION
  of this run stated there), on the all-equity basis: owner cash before interest and after the company's tax, built as
  operating cash plus interest paid less the tax that interest saved at Brazil's 34% combined statutory rate (CONVENTION of
  this run; rationale: an unlevered company would pay the tax the interest now shields, and the 34% is the "Tax rate" of the 20-F's tax
  reconciliation, note 20). Working capital counted (it is inside operating cash), specific (d).
- **(a) Cycle base.** The literal window's first year, 2021, is aberrational on the filer's own description (‘a year marked
  by extraordinary results due to the strong commodities prices’, 4Q22 release) and its last, 2025, carries the Blast
  Furnace No. 2 idleness (‘extraordinary effects’, 4Q25 release); "If either year was aberrational, any calculation of growth will be distorted." **[L2005-003]**. On the recast owner cash series the troughs
  are 2016 (R$ -1,356m) and 2025 (R$ -6,404m) with the peak in 2021, so the base is the trough-to-trough cycle 2016 to 2025.
- **(c) Acquisitions.** Net purchases 2021 to 2025, R$ 9,902m, exceed half of owner cash before purchases over the same years
  (R$ 7,800m all-equity), so this is a serial acquirer under the text, and the central figure is the organic pair: purchases
  left out, growth measured on owner cash before purchases (the filer reports no organic growth figure; said so). The default
  pair (purchases deducted, total growth) is shown beside.
- **(e) Maintenance.** The filing allows a guess: it names cement spending ‘sustaining’ and steel spending overhauls and
  maintenance, and mining spending mostly expansion. Maintenance is guessed at depreciation, amortization and depletion, "not
  inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**; spending above it
  (R$ 546m a year over 2016 to 2025) is added back in the central case. All-spending case beside.
- **(b) Growth.** The series changes sign, so growth is measured between the halves of the cycle: all-equity, organic,
  maintenance case R$ 3,036m (2016 to 2020) to R$ 2,688m (2021 to 2025), -2.4% a year; all-spending R$ 3,071m to R$ 1,560m,
  -12.7% a year. A decline is carried as the bottom; the no-growth case is the top. (f) The cap does not bind.
- **Cycle base, central:** R$ 2,862m a year (all-equity, organic, maintenance). All-spending: R$ 2,316m.
- **Net debt** at the latest filed balance sheet, 2026-06-30 (ITR `0001292814-26-004375`): borrowings R$ 53,366m plus leases
  R$ 1,041m less cash R$ 13,631m and financial investments R$ 681m = **R$ 40,094m**. Subsequent events the filing states: the
  notes exchange changes net debt by well under R$ 0.5bn and is left out (said so). Customer advances R$ 13,101m and forfaited
  payables R$ 1,504m are not in net debt in the central figure and are shown beside.
- **Discount rate** 12.57% (NTN-F 2037, Step 0); ten years then no growth (zero nominal).

| Case (per share, R$) | At the sovereign 12.57% | Each end at 10% (for the fair price) |
|---|---|---|
| All-equity, central (organic, maintenance), top: no growth | -13.07 | -8.65 |
| All-equity, central, bottom: -2.4% a year for ten years | -15.43 | -11.86 |
| All-equity, all spending, top / bottom (-12.7%) | -16.34 / -23.57 | -12.77 / -22.44 |
| All-equity, central top, with customer advances counted as debt | -22.94 | -18.53 |
| Equity-only (owner cash after interest, recast, maintenance, R$ 1,014m), top / bottom (-18.0%) | 6.08 / 2.22 | 7.65 / 2.53 |

- **The literal window beside:** 2021 to 2025, all-equity, organic, maintenance case R$ 2,688m a year, no growth at 12.57%:
  R$ -14.11 a share. The default pair (purchases deducted) on the cycle: R$ 1,436m all-spending, lower still.
- **A signed, unclosed deal beside:** the SWT term sheet (enterprise value EUR 550 million, exclusivity up to 10 weeks, not
  closed). SWT's own record is not in the filings read, so it is not valued; the proceeds would reduce net debt, against a gap
  to a zero equity value of about R$ 17bn on the central top case. The CSN Cimentos sale has proposals but no signed deal and
  is left out.
- **The floor, tested first**, "there’s just a point at which we drop out of the game" **[M2003-149]**: on the all-equity basis the central owner cash is 5.9% of the enterprise value
  at the price (R$ 2,862m against R$ 48,648m = R$ 8,553m market value plus R$ 40,094m net debt) with no growth, and lower with
  the decline; counting the advances and forfaiting back in as owner cash gives 8.9%. **No case earns the floor at the price.**
  Q7, had it been reached, would close OUT by the floor before the width test.

**The two reporting figures (computation, not clearance):**
- **(a) VALUE RANGE**, as Q7 builds it, central on the all-equity basis: **R$ -15.43 to R$ -13.07 a share** against R$ 6.45
  (no positive value: net debt exceeds the value of the business's cash on every case). Equity-only beside: R$ 2.22 to
  R$ 6.08.
- **(b) FAIR PRICE**, the midpoint of the range valued at 10% (each end at 10%, averaged), after the company's own tax:
  **all-equity R$ -10.26 a share, so no positive fair price**; equity-only beside **R$ 5.09**. The equity-only figure does not decide; the central figure is the one built as "we evaluate acquisitions on an all-equity basis" **[L2017-004]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 4291e2d9); written question by question; committed after Step 0 to
      Q1 (b01dd904) and after Q2 (b9eaf886), then this close.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not touched
      here); the fold into the register is the dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, save the one file-name listing
      declared under contamination; what was seen there and in the session context is declared and not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `check_citations.py` in the research folder (ids exist; each
      quoted fragment beside an id is in that row); every filing fact carries its accession; no E-ids.
- [x] The order was kept; Q2 was the first STOP that failed and closed the run; the Q7 figures are headed COMPUTATION, NOT A
      CLEARANCE and carry no entry language.
- [x] Owner cash after every real cost, from the filed cash flow statements, never a net-income proxy (operator rule 5); the
      sovereign from Tesouro Nacional, dated; the price quote is an aggregator's and flagged.
- [x] Contrary evidence written as found (`_notes.md`); facts for later questions under AFTER THE STOP; the integrity flag is
      in the box line.
- [x] Not a point-in-time run; no anchor bars any row.
- [x] `tools/run.py` refused on a currency mismatch; only its price line was read; all arithmetic by hand from the filings.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the commit message).
- Honest gaps: the competitor comparison uses one rival (Vale), the only named iron ore rival that files with the SEC; the
  Australian producers enter only through Vale's own sentence on freight. CSN's mining margin for 2018 and 2019 was not
  computed (segment revenue not read; the 4Q19 and 4Q20 releases did not parse to text), and three CSN years (2016, 2020,
  2022) are backed out of the releases' stated comparisons rather than read directly. No steel rival was read.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) Q2's commodity paragraph sorts a commodity seller into the low-cost producer (castle) or the high-cost producer (OUT), and
sends the unreadable case to TOO HARD; it does not say where a middle-of-the-curve producer goes, one that is profitable at
today's price but behind its major rivals. I read low-cost against "your other major competitors" as **[M2001-013]** puts it
and closed OUT on a gap shown in every year read; another analyst could call the same evidence TOO HARD (NATURE) on the
ground that only the next downturn shows whether a middle producer's margin holds. A sentence on the middle of the curve
would settle it. (2) Q7's floor of about ten percent sits below the BRL sovereign (12.57%), so the range is discounted at a
higher rate than the fair price; in a high-rate currency the fair price at 10% is the more generous figure, the reverse of its
purpose in dollars. The text's own qualification (Munger: "he would change the numbers" **[M2003-151]**) is not
turned into a rule for a currency whose long rate is above the floor. (3) Part VII's all-equity basis asks for "owner cash
before interest and after the company's tax" but does not say whether interest is added back gross or net of the tax it
shields; I added it back net at the 34% statutory rate and said so. (4) Neither the template nor Q7 says how to treat customer
prepayments for future deliveries inside operating cash (here R$ 11.8bn in two years); the inventory-secured trade-finance
convention covers a near case only. I treated them as borrowings, a CONVENTION of this run. (5) The brief's "up to three
competitors that file with the SEC" met a deciding part with only one named SEC-filing rival; the text does not say whether
the Australian producers, named only by country in the filer's 20-F and by name in the rival's, may be read.
