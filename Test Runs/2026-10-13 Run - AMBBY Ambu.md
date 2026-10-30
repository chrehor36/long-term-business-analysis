# Company Run — Ambu A/S (Nasdaq Copenhagen: AMBU B; OTC unsponsored ADR: AMBBY) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md` with three stated departures: (1) the lines of evidence
are derived by the analyst from the annual report; (2) Ambu A/S is not an SEC registrant, so the primary documents are the
company's own annual reports, interim reports, remuneration report and company announcements, each recorded by title and
date in place of an accession number; (3) the SEC-based tools could not serve the name (below).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule; the dispatching session
fills it at the fold. *Filled at the fold, 2026-10-13, after the run was committed: not held (`PORTFOLIO.md` carries no line for AMBBY, AMBU B or Ambu).*

**Contamination declared (the blind rule).** Nothing about Ambu, AMBU B or AMBBY from any other run, research pass,
holding review, register or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and not used: the session's
opening context showed recent commit subjects about another company's run and fold (ACHC), the names of two other
research folders in the working-tree status (AYI, ARCB), and the memory index lines on queue state ("57 gate-clearers,
nothing buyable" and the wave counts); `.gitignore`, read to keep raw filings out of commits, names other runs in its
comments (SNPS, DELL, MGM, Ford). None concerns this company; none was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Tools (departure 3).** `python tools/run.py AMBBY` printed "AMBBY: not an SEC filer. Use the evidence ladder";
  `python Screens/cover_shares.py AMBBY` printed "NOT AN SEC REGISTRANT". All arithmetic below is by hand from the
  filed statements, in `Test Runs/_research 2026-10-13 AMBBY/owner_cash.py` with its printout `owner_cash_output.txt`.
- **Price:** DKK 76.20 a class B share, Nasdaq Copenhagen, 2026-10-13 (Yahoo Finance chart feed for AMBU-B.CO, live quote;
  **aggregator, flagged**; the prior close was DKK 72.85 on 2026-10-09). **ADR beside it:** AMBBY last USD 11.00
  (Yahoo, stale, thin: 2 units traded the week of 2026-10-12; **aggregator, flagged**). **ADR ratio:** one ADS to one class B
  share, by the depositary's own SEC filing, Citibank N.A. Form F-6 POS of 2018-01-16 (accession 0001193805-18-000045):
  "each ADS representing the right to receive one (1) Class B share of Ambu A/S"; an earlier F-6EF of 2017-06-08 (accession
  0001193805-17-001051) stated a different ratio before the January 2018 split, and a BNY Mellon F-6EF of 2020-06-29
  (accession 0001019155-20-000152) exists for a second program whose ratio its opinion does not state. The quote
  agrees with one to one: DKK 76.20 at USD/DKK 6.6803 (Yahoo DKK=X, 2026-10-13, aggregator, flagged) is USD 11.41.
- **Split history:** a 1:5 share split in January 2018, nominal value from DKK 2.50 to DKK 0.50 (Annual Report 2017/18,
  "Share split"). No later split or consolidation found in the reports read to 2025/26 Q3.
- **Shares by class:** 34,320,000 class A (unlisted, ten votes, held by the founder's descendants) and 234,974,389 class B,
  total 269,294,389, "equal economic rights" (Annual Report 2024/25, Shareholder information, published 2025-11-05). Treasury
  B shares: 2,738,985 at 2025-09-30 (same); plus 1,746,034 bought 2025-12-29 to 2026-02-11 for DKK 150m at an average
  DKK 85.91 (Interim report Q3 2025/26, company announcement no. 17 2025/26, 2026-08-25, p. 16); plus 4,492,076 under the
  program of 2026-05-06, finished in September for DKK 299,999,938 at an average DKK 66.78, after which the company "owns
  8,641,687 treasury shares, corresponding to 3.2% of the share capital" (company announcement of 2026-09-21, "Ambu's share
  buyback program has been finalized", read on placera.se, a redistributor; **flagged**; its stated number "12 2025/26"
  sits oddly beside no. 17 of August and is recorded as found). The shares are bought "with the aim of completing a share
  capital decrease"; no registered decrease found. **Shares outstanding: 269,294,389 less 8,641,687 = 260,652,702**, both
  classes counted alike because their economic rights are equal.
- **Market cap:** 260.653m x DKK 76.20 = **DKK 19,862m** (USD 2,973m).
- **Sovereign for the earnings currency (DKK):** **3.50%**, the yield at the 2026-09-02 auction of DGB 0.25% 2052
  (ISIN DK0009924029), the longest Danish government bond, Danish Debt Management Office, Danmarks Nationalbank, "Auction
  results - government bonds", fetched 2026-10-13 (saved as `sovereign_DK_auction_results_2026-10-13.txt`). It is the
  issuing authority's own figure but six weeks old; the latest auction (2026-10-07) priced the 2035 bond at 3.29% against
  3.20% on 2026-09-02, so the long end has not fallen since. `python tools/sources.py` serves USD, JPY and EUR only.
- **Filings read** (operator rule 4, departure 2): Annual Reports 2014/15 to 2024/25 (eleven reports, ambu.com
  "Reports in English", each the company's published PDF; 2024/25 published 2025-11-05); interim reports Q1, Q2 and Q3
  2025/26 (company announcements no. 10, no. 11 of 2026-05-06, and no. 17 of 2026-08-25); Remuneration Report 2024/25;
  company announcement no. 16 2025/26 (2026-08-25, outlook update, read on inderes.fi, **flagged**); the buyback
  announcement above. **One figure cross-checked:** cash flow from operating activities 2024/25, DKK 791m, in the filed
  consolidated cash flow statement (Annual Report 2024/25, p. 136) equals the five-year summary (p. 10) and the FY column of
  the Q3 2025/26 cash flow statement; revenue 2024/25, DKK 6,037m, equals note 2.2's sum of the four business groups
  (1,818 + 1,826 + 1,249 + 1,144).
- **Owner cash after every real cost** (DKKm; operating cash flow, which is after interest, tax and the working-capital
  change, less all capital spending including capitalised development, less lease principal, less share-based pay, which
  the cash flow statement adds back as a non-cash item; acquisitions shown apart):

| FY to 30 Sep | revenue | CFO | capex (intang. + tang.) | lease principal | stock pay | owner cash, all spending | owner cash, maintenance guess | interest paid net, after 22% tax | acquisitions |
|---|---|---|---|---|---|---|---|---|---|
| 2015/16 | 2,084 | 369 | 84 | 1 | n/f | 284 | | 22.6 | 155 |
| 2016/17 | 2,355 | 462 | 141 | 4 | n/f | 317 | | 25.0 | 0 |
| 2017/18 | 2,606 | 554 | 233 | 3 | 26 | 292 | | 34.3 | 928 |
| 2018/19 | 2,820 | 533 | 259 | 8 | 12 | 254 | | 15.6 | 2 |
| 2019/20 | 3,567 | 295 | 428 | 32 | 19 | -184 | | 21.8 | 2 |
| 2020/21 | 4,013 | 328 | 573 | 44 | 11 | -300 | 143 | 11.7 | 301 |
| 2021/22 | 4,444 | 95 | 553 | 52 | 12 | -522 | -146 | 22.6 | 5 |
| 2022/23 | 4,775 | 518 | 326 | 63 | 17 | 112 | 224 | 49.1 | 0 |
| 2023/24 | 5,391 | 813 | 289 | 65 | 26 | 433 | 493 | 12.5 | 0 |
| 2024/25 | 6,037 | 791 | 384 | 63 | 31 | 313 | 433 | 10.1 | 0 |

  Sources: the consolidated cash flow statements of the Annual Reports 2015/16 (p. 42), 2016/17 (p. 39), 2018/19 (p. 51),
  2020/21 (p. 47), 2022/23 (p. 117) and 2024/25 (p. 136), each giving two years; stock pay from the same statements and the
  equity statements ("n/f" = not found as a line in the 2015/16 and 2016/17 statements read). IFRS 16 from 2019/20: lease
  principal before it is finance-lease principal only, with operating leases inside CFO. The maintenance guess (2020/21 on)
  is depreciation of property, plant and equipment excluding right-of-use assets plus amortisation of own development
  projects and IT, from note 2.4 of the Annual Reports 2020/21, 2022/23, 2023/24 and 2024/25 (2020/21's PP&E depreciation of
  118 included leased assets; lease principal of 44 was taken out as the estimate, **a guess, said so**). Nine months to
  2026-06-30: CFO 692, capex 421, lease principal 54, stock pay 21 (Interim report Q3 2025/26, p. 15): owner cash 196
  against 186 a year earlier.
- **Five-year averages, 2020/21 to 2024/25:** owner cash, all spending, **DKK 7.2m**; maintenance guess **DKK 229.4m**;
  interest after tax DKK 21.2m. Net purchases of businesses over the window DKK 306m (the 2020/21 payment of DKK 298m was
  largely contingent consideration on the 2018 Invendo purchase, whose liability fell from DKK 426m to 137m that year).
- **Net debt.** At 2026-06-30: cash and short-term deposits DKK 705m, credit institutions DKK 19m, lease liabilities DKK
  560m (473 + 87) (Interim report Q3 2025/26, balance sheet). Lease liabilities are left out of net debt because lease
  principal is charged inside owner cash; the company's own NIBD of DKK -126m includes them. Subsequent event the filing
  states: the buyback of up to DKK 300m, DKK 123.6m done by 2026-06-30, completed for DKK 300.0m by September, so DKK
  176.4m paid after the balance-sheet date. **Net cash DKK 509.6m.** Enterprise value at the price DKK 19,352m.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is the question "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**, and here that turns on whether the cash a single-use endoscope maker throws off in 2030 to 2036 can be
pictured at all. "the market is there to serve you and not to instruct you" **[M2006-077]**: the class B share fell from DKK 262 (the January
2021 placing price) to DKK 66 to 86 (the 2026 buyback prices), and neither the fall nor the 2019/20 rise says anything about
value by itself. Margin of safety: if the case needs pencil and paper "it ought to just kind of scream at you" **[M1996-084]**.
No macro enters: tariffs (DKK 40m+ of cost in 2024/25, refunds in 2025/26) are read only as a property of the business's
footprint. Who is paid to tell you: the search engine summary gave "9 analysts" and an average 2027 target of DKK 102; it was
not used. **Contrary evidence, written down as found**, the habit of "write it down in the first 30 minutes" **[M1997-127]**: (1) the company's own one-year guidance for 2021/22
was organic growth 15-19% and EBIT margin 7-9% (Annual Report 2020/21, "Financial guidance 2021/22"); it delivered 4.3% and
2.7% before special items (Annual Report 2024/25, five-year summary), so the insiders' own forecast missed by a wide margin
one year out; (2) the 2018 Invendo GI technology (DKK 926m paid plus contingent consideration) and later GI work were
impaired by DKK 327m in 2023/24 "reflecting the longer time required to penetrate the market" (Annual Report 2024/25, note
2.4); (3) reported EBIT margin ran 21.6% (2017/18), 10.9%, 12.0%, 8.5%, -0.6% (2021/22), 6.2%, 5.8%, 13.0% (2024/25); (4) the
Anesthesia business lost volume in "selected U.S. accounts operating under non-exclusive contracts" after "price increases
implemented in prior years" (Interim reports Q2 and Q3 2025/26), evidence that the older half of the business has less
pricing power than its owners assumed; (5) for the record on the other side, Endoscopy Solutions grew 15.4% organically in
2024/25 and 16.0% in Q3 2025/26, and owner cash has been positive and rising since 2022/23.

## THE STANDING RULE
The rule binds the buyer, not the target: "figure out what can really go wrong with this place" **[M2012-081]**. Nothing in the
target forces leverage or a sudden cash demand on a buyer of its listed shares; a holder must be prepared to see a stock "go
down 50 percent" **[M2020-022]**, and this one has done more than that from 2021 to 2026. No bearing on the buyer's ruin
provided the purchase is unlevered and sized within the buyer's means. Not a ground for closing the file.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**Lines of evidence chosen (departure 1).** From the Annual Report 2024/25: the business description ("Strategy", the two
business areas and four business groups, note 2.2), the risk-management section (pp. 37-41: innovation and development,
product supply and quality, commercial, geopolitical, legal and compliance), and the management's review (pp. 10-35:
outlook, revenue, margins, special items, capital allocation). Back through the cycle: the Annual Reports 2014/15 to 2023/24
for the strategy targets, the guidance set and met or missed, the GI programme and its impairment, the share issues; the
2025/26 interim reports and outlook announcement for the present.

**What the business is, from the filings.** One operating segment ("Ambu is engaged in a single business activity of
medical technology solutions", note 2.1), revenue reported in four groups: Respiratory (single-use bronchoscopes,
video laryngoscopes, double-lumen tubes) DKK 1,818m; Urology, ENT and GI (single-use cystoscopes, ureteroscopes,
rhinolaryngoscopes, duodenoscopes and colonoscopes) DKK 1,826m; Anesthesia (resuscitators, masks, airway devices) DKK 1,249m;
Patient Monitoring (ECG, EEG and neurology electrodes) DKK 1,144m (2024/25, note 2.2). Endoscopy Solutions, the first two, is
60% of revenue (64% in Q3 2025/26) and, in the company's words, "the more profitable Endoscopy Solutions business" (Annual
Report 2023/24, gross margin). Profit by part is not filed (one segment), so Q2's parts threshold cannot be applied on
operating profit; on revenue share and on the company's statement of relative profitability, **Endoscopy Solutions decides**
(CONVENTION of this run: where operating profit by part is not filed, the part that is larger by revenue and stated by the
filer to be the more profitable is taken to decide; rationale: the framework's threshold needs a figure the filer does not
publish, and this is the reading that uses only what it does publish).

**The test, applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
look like in five or 10 years" **[M2012-065]**; the object is "the predictability of the economics of the situation 10 years
out" **[M2000-104]**, not the product, which is plain (a disposable scope replaces a reusable one that must be reprocessed).

1. **The key variables**, "trying to identify the key variables in that particular business, and evaluating how predictable they were" **[M1998-044]**: (a) the pace at which hospitals convert each
   procedure from reusable to single-use scopes, which the company itself lists as a risk, "Pace of market creation and
   product acceptance in single-use endoscopy" (Annual Report 2024/25, Commercial risks); (b) the price per scope as
   reusable makers and new single-use entrants answer (the report names no rival; the filings give no market-share figure
   for any endoscopy area); (c) whether each new procedure (GI above all) can be won at all: the duodenoscope was guided for
   launch "in early Q4 2019/20" (Annual Report 2018/19) and the GI assets were written down by DKK 327m in 2023/24; (d)
   the product cycle: "Ambu's achievement of our strategic targets depends on our ability to develop relevant and unique
   solutions" (Innovation & development risks), with new generations (aScope 5, SureSight, aView 2 Advance, EndoIntelligence
   software and AI) every few years. Each is a forecast about technology adoption and rival response, not about consumer habit.
2. **Do the past statements tell the future ones?** "do I understand enough about this business so that the financial statements will tell me" **[M2008-033]** what the future ones will look like? They have not. The insiders' own one-year forecast for
   2021/22 (organic 15-19%, EBIT 7-9%) became 4.3% and 2.7%; the 2018/19 targets were followed in the same year by a "Review
   of the Big Five 2020 Strategy" and a new chief executive (company announcements no. 10 and no. 12, 2018/19); a third
   strategy (Zoom In, 2022) and a fourth (ZOOM AHEAD, 2025) followed under a third chief executive. Margins over the decade
   ran from 21.6% to -0.6% and back to 13.0% on revenue that rose every year; the past figures do not show where the
   earning power sits in 2035.
3. **Would the insiders write it down?** They did write it down, every year, and the record above shows how
   far off it was; the company still frames the decisive variable as a risk it cannot control ("pace of market creation").
   The speakers' test is whether insiders "would not want to put down on paper their predictions" **[M2000-105]** for the economics ten
   years out; here even the one-year paper was wrong by about three-quarters of its growth (4.3% against the 17% midpoint) and about two-thirds of its margin (2.7% against 8%).
4. **Can I name the winner, not just the industry?** Of "industries we know that may have a wonderful future" **[M2012-067]** the row says the winners may be unknown. The industry's direction (more single-use) is the
   company's claim and may be right; "Just because Charlie and I can clearly see dramatic growth ahead for an industry does
   not mean we can judge what its profit margins and returns on capital will be as a host of competitors battle for
   supremacy" **[L2009-005]**. The filings name no competitor and give no share figure; the GI impairment shows that leading
   in bronchoscopy did not carry over to the next procedure. "And we try to stick with businesses where we know the
   winners." **[M2014-097]**
5. **Is the forecast about customers or about technology?** The row's contrast is "in terms of laying out what their prospective customers will do in the future" **[M2017-019]**. Here it is about technology and its adoption by hospital
   committees: image quality, cost per procedure against reprocessing, infection data, software. "We view change as more of
   a threat into the investment process than an opportunity." **[M1999-063]**; where "the future technology could hurt the
   business as it presently exists, [...] we look at that as something to worry about" **[M1998-008]**. A business whose growth
   part lives on the next generation of devices is the case the rows send to the too-hard box: "if they had never invented
   any more pharmaceuticals, it would be a terrible business" **[M1999-075]**.
6. **How far off could I be?** The model must include "how far off we can be" **[M2011-084]**. Very far: owner cash after all spending was DKK 254m to 317m a year in
   2015/16 to 2018/19, DKK -522m in 2021/22, DKK 433m in 2023/24. A model of 2035 that cannot place the margin within a
   factor of three is not a model.
7. **Do I doubt it is inside?** "if you have doubts about something being into your circle of competence" **[M2002-092]**,
   it is not. I do.

**The part that does not decide.** Anesthesia and Patient Monitoring (40% of revenue, organic growth guided at 3-5% a
year to 2029/30) is a plainer business of masks, resuscitators and electrodes, easier to picture; it does not decide by the
run's convention above, and its own recent record (volume lost after price rises) is carried to AFTER THE STOP.

**Which cause.** The deciding question, the ten-year economics of single-use endoscopy for this company, is important and,
on the evidence, not knowable; the row asks for "things that are important and knowable" **[M2006-076]**, and here the people with the most information, the company's own management, missed
their one-year forecast badly and wrote off their biggest new-procedure bet. More reading of Ambu's own reports would not
cure it, "even if we were to spend years intensely studying those industries" **[L1993-023]**; the roadblock is "the nature
of the industry" **[L1993-023]**, a fast-changing device field where "those are the businesses of rapid change" **[M2001-069]**.
That is NATURE, not WORK. It is no judgment that the business is bad or the price wrong: "The only way we know how to make
money is to try and evaluate businesses." **[M2000-038]**

- **VERDICT: TOO HARD (NATURE)**, the rows' "three boxes at the company: in, out, and too hard" **[M2006-013]**. The file
  closes at Q1. Q2 to Q12 are NOT REACHED; every figure below is COMPUTATION, NOT A CLEARANCE.

**The balance sheets, read in Step 0 because the file closed before Q4** (DKKm at 30 September; Annual Reports 2016/17
p. 38, 2018/19 p. 50, 2020/21 p. 46, 2022/23 p. 118, 2024/25 p. 137; "borrowings" include lease liabilities in 2020 and
2021, where the report does not separate them):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| revenue (year) | 2,084 | 2,355 | 2,606 | 2,820 | 3,567 | 4,013 | 4,444 | 4,775 | 5,391 | 6,037 |
| equity | 990 | 1,279 | 1,882 | 2,182 | 2,372 | 3,952 | 4,261 | 5,393 | 5,594 | 6,035 |
| goodwill | 819 | 781 | 1,505 | 1,547 | 1,497 | 1,504 | 1,623 | 1,565 | 1,527 | 1,497 |
| other intangibles | 419 | 434 | 1,135 | 1,242 | 1,438 | 1,740 | 1,996 | 2,046 | 1,703 | 1,752 |
| inventories | 287 | 313 | 382 | 506 | 515 | 748 | 1,222 | 907 | 1,078 | 1,272 |
| trade receivables | 416 | 437 | 478 | 474 | 521 | 699 | 747 | 766 | 745 | 834 |
| cash | 35 | 19 | 63 | 120 | 98 | 64 | 187 | 157 | 615 | 866 |
| borrowings | 990 | 786 | 1,308 | 1,155 | 1,444 | 823 | 1,250 | 0 | 0 | 5 |
| lease liabilities | | | | | (in borrowings) | (in borrowings) | 595 | 584 | 558 | 542 |
| contingent consideration | | | 498 | 378 | 426 | 137 | | | | |

What moved and why. (1) **Equity rose about DKK 5.0bn, and roughly DKK 3bn of it was sold, not earned:** share issues of
DKK 667m (2017/18, the year of the Invendo purchase, beside DKK 493m of treasury shares bought), DKK 1,225m (January 2021,
4,711,832 new B shares and 250,000 treasury shares at DKK 262, Annual Report 2020/21) and DKK 1,054m (2022/23, 11,577,957 new
B shares at DKK 93, net DKK 91.10, Annual Report 2022/23 note 4.5); net profit over the ten years sums to DKK 2,798m and
dividends paid to about DKK 660m. (2) **Intangibles grew faster than the business:** goodwill and acquired technology jumped
with Invendo in 2017/18 (GI technology, DKK 926m paid plus contingent consideration of DKK 498m), and capitalised development
(completed plus in progress) rose from about DKK 140m (2016) to DKK 1,313m (2025); DKK 327m of the GI assets was impaired in
2023/24. Reported earnings lean on a growing pool of capitalised development amortised over years, which is why owner cash
here deducts all of it as it is spent. (3) **Inventory ran far ahead of sales** in 2021 and 2022 (13.8% of revenue in
2016, 27.5% in 2022, 21.1% in 2025): the 2021/22 operating cash flow of DKK 95m is mostly that build, and inventory has not
returned to the 2016 to 2019 ratio. Receivables fell from 20% to 14% of revenue, an improvement. (4) **Debt came and went
with the issues:** borrowings of DKK 1,250m at 2022 were repaid in 2022/23 (repayments DKK 1,575m in the cash flow statement)
out of the DKK 93 issue; since 2024 the company holds net cash. (5) What the figures do not say: profit by business group,
price and volume by product, market share, and the cost of a scope against a reprocessed one; none is filed.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (closed at Q1).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED (the balance sheets were read above, in Step 0).
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.

## Q7 — WHAT IS IT WORTH? NOT REACHED. COMPUTATION, NOT A CLEARANCE (the reporting figures the brief asks for)
Built by Q7's range convention as the text states it; nothing here is a clearance, a verdict or entry language.
- **Cash input.** Five-year window 2020/21 to 2024/25. The maintenance case is central (specific (e)): the filing allows the
  guess (note 2.4 splits depreciation of property and equipment from amortisation of own development), DKK 229.4m a year
  after interest; the all-spending case beside it, DKK 7.2m. All-equity basis: interest paid, net of interest received, after
  the 22% Danish rate, added back (DKK 21.2m), giving DKK 250.6m and DKK 28.4m. The company's own tax is inside operating
  cash flow; no carryforward found that runs out inside ten years.
- **Growth (specific (b)).** The series changes sign (all spending: -300, -522, 112, 433, 313; maintenance: 143, -146, 224,
  493, 433), so the compound rate between end years is meaningless; between the halves (2020/21 and 2021/22 against
  2023/24 and 2024/25) it is also meaningless, the first half averaging below zero (all spending -411 against 373;
  maintenance -1.5 against 463). **The range is therefore the no-growth case alone, said so.**
- **Cycles (specific (a)).** The filer describes 2020/21 and 2021/22 through Covid demand swings, freight and raw-material
  inflation and a cost-reduction programme (Annual Reports 2020/21 and 2021/22); no owner-cash cycle, peak to peak, can be
  drawn from the series, so the literal window stands as the base. Beside it, for the record only: in 2015/16 to 2018/19,
  when the EBIT margin was 11% to 22%, owner cash after all spending averaged DKK 287m.
- **Acquisitions (specific (c)).** Net purchases over the window DKK 306m, DKK 61.2m a year. Against maintenance owner cash
  before purchases (DKK 1,147m over the window) they are less than half, so the serial-acquirer rule does not apply to the
  central case and the default pair is used: purchases deducted in years one to ten, stopping with growth after year ten.
  (Against the all-spending figure, DKK 36m over the window, they would exceed half; see What was unclear.)
- **Working capital (specific (d))** is inside operating cash flow and so counted; the 2021/22 build is not separated,
  because the filer ties it to no single contract or event.
- **Net cash** DKK 509.6m (Step 0). **Shares** 260,652,702.

| case | DKK a share | USD a share (ADR, 1:1) |
|---|---|---|
| **Value range, central: no-growth, maintenance, purchases deducted years 1-10, all-equity** | **27.47** | **4.11** |
| beside: the same, equity-only (owner cash after interest, no net cash) | 23.19 | 3.47 |
| beside: organic pair, purchases left out, all-equity | 29.42 | 4.40 |
| beside: all-spending case, purchases deducted years 1-10, all-equity | 3.12 | 0.47 |
| **Price, 2026-10-13** | **76.20** | **11.41** |

- **The floor, tested first.** At DKK 76.20 the enterprise value is DKK 19,352m. The central case yields 1.0% in years one to
  ten and 1.3% after on that value; 2024/25 alone, the best year of maintenance owner cash (DKK 443m all-equity), yields 2.3%.
  Beside the range and not a case of it: 2024/25's figure carried ten years at the business's own sales growth of 2019/20 to
  2024/25 (11.1% a year, the most specific (f) allows), then flat, returns 5.5% a year at the price. **No case earns the
  floor of about ten percent** (CONVENTION at Q7; **[M2003-149]**: "it would get very sloppy to start dipping below that").
  Had Q1 passed, Q7 would close OUT on the floor before any width test; the width test does not arise, the range being one
  case.
- **Fair price (Part VII, a reporting figure, never a verdict):** each end case valued at ten percent and averaged; the
  range being a single case, the fair price is that case at ten percent: **DKK 10.13 a share all-equity (USD 1.52)**, the
  central figure; **equity-only DKK 7.36 (USD 1.10)** beside it. Tax: the company's own, no conversion.
- Calculation file: `Test Runs/_research 2026-10-13 AMBBY/owner_cash.py`, printout `owner_cash_output.txt`. Calculations of
  value are "necessarily imprecise and often seriously wrong" **[L2005-001]**.

## Q8 TO Q10, Q12 — NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE) at Q1**: the ten-year economics of single-use endoscopy for this company, the deciding part, cannot be
foreseen; the company's own one-year forecasts missed widely and its largest new-procedure bet was written down.
**Integrity facts recorded, not judged** (guidance given every year and missed in 2021/22; an adjusted EBIT margin featured;
special items in four of seven years; recalls). COMPUTATION beneath the stop: value range DKK 27.47 a share (a single
no-growth case; USD 4.11) against DKK 76.20 (USD 11.41); no case earns the floor at the price; fair price DKK 10.13
all-equity (equity-only DKK 7.36). No research pass: the cause is NATURE, and no case of the range earns the floor at the
price in any event (Part VII, When a research pass is run).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Each with its source, written down as found ("write it down in the first 30 minutes" **[M1997-127]**); no verdict; the box unchanged.

**Bearing on Q2 (the castle).**
- Rivals: the annual reports name **no competitor** (a text search for Olympus, Boston, Storz, Verathon, Medtronic, Pentax,
  Fujifilm and Teleflex in the 2022/23 to 2024/25 reports found none). The only competitive statement found: 2022/23
  pulmonology growth of 2% was hurt by "the recall of VivaSight 2 DLT and increased competition in the U.S." (Annual Report
  2022/23). The rivals below are therefore the analyst's choice, two SEC filers that sell single-use or airway devices in
  Ambu's areas, compared on whole-company operating margin from their 10-K XBRL facts, **a weak comparison, flagged**
  (neither reports single-use endoscopy separately). Boston Scientific (10-K, CIK 885725): operating margin 2016 4.9%,
  2017 14.2%, 2018 15.3%, 2019 14.1%, 2020 -0.8%, 2021 10.1%, 2022 13.0%, 2023 16.5%, 2024 15.5%, 2025 18.0% (latest 10-K
  accession 0000885725-26-000010). Teleflex (10-K, CIK 96943): 2016 17.1%, 2017 17.3%, 2018 13.1%, 2019 16.5%, 2020 16.7%,
  2021 22.4%, 2022 17.9%, then 2023 15.1%, 2024 6.1%, 2025 5.9% on restated continuing operations (accession
  0000096943-26-000019; the restatement breaks the series). Ambu's reported EBIT margin, years to September: 2015/16 17.1%,
  2016/17 19.1%, 2017/18 21.6%, 2018/19 10.9%, 2019/20 12.0%, 2020/21 8.5%, 2021/22 -0.6%, 2022/23 6.2%, 2023/24 5.8%,
  2024/25 13.0% (five-year summaries, Annual Reports 2016/17, 2020/21, 2024/25). Rivals that do not file with the SEC and
  would decide a Q2 reading: Olympus (Tokyo) and Karl Storz (private); not read.
- Pricing: "Ambu's Anesthesia & Patient Monitoring business has historically experienced modest price pressures, while
  prices within the Endoscopy Solutions business have been more stable" (Annual Report 2024/25, Commercial risks).
  Anesthesia volume fell after "price increases implemented in prior years, which led to lower volumes in Anesthesia in
  selected U.S. accounts operating under non-exclusive contracts" (Interim report Q3 2025/26); A&PM guidance cut to "very
  low-single-digit" growth for 2025/26 (company announcement no. 16 2025/26, 2026-08-25). Gross margin 62.4% (2020/21),
  57.5%, 56.8%, 59.4%, 60.2% (2024/25).
- Unit volume: Endoscopy Solutions organic growth 15.4% in 2024/25 and 16.0% in Q3 2025/26, with "market share gains in all
  endoscopy areas" (chief executive, Q3 2025/26 report); no share figure filed.
- Tariffs: more than DKK 40m of tariff cost in 2024/25 (Annual Report 2024/25, EBIT margin); IEEPA tariff refunds received in
  Q3 2025/26; the Mexico plant scaled "to balance global footprint and manage tariff costs" (Q3 2025/26).

**Bearing on Q3 (capital).** Invested capital DKK 5,716m at 2025-09-30, of which goodwill DKK 1,497m; EBIT before special
items DKK 784m; the company's own ROIC 11% (Annual Report 2024/25, five-year summary). Capital spending including capitalised
development DKK 384m against depreciation and amortisation of DKK 372m in 2024/25; it ran at DKK 553m to 573m a year in
2020/21 and 2021/22.

**Bearing on Q4 and Q5 (the accounts and the people; integrity facts, not judged).**
- "Special items" recur: DKK -174m (2018/19), -148m (2021/22), -8m (2022/23), -334m (2023/24); margins are featured "before
  special items" throughout the reports.
- Annual guidance is given and revised: 2025/26 organic growth guided 10-13% (2025-11-05), 10-12% (2026-05-06), about 10%
  (2026-08-25); 2021/22 guided 15-19% organic and 7-9% EBIT margin, delivered 4.3% and 2.7%.
- An adjusted figure is featured: "Adjusting for tariff costs and FX, Ambu generated an EBIT margin of 14.5% in the
  quarter" (Interim report Q2 2025/26), against a reported 11.0%.
- Chief executives: a new CEO appointed in 2018/19 (company announcement no. 10 of 2018/19, beside no. 12, "Review of the Big
  Five 2020 Strategy"); Britt Meelby Jensen chief executive since 2022, the second appointed since the start of 2019.
- Pay: CEO total remuneration DKK 17.4m for 2024/25 (base DKK 8.0m), short-term incentive at 50.8% of maximum, LTI at 53%;
  KPIs organic revenue growth, EBIT margin before special items and free cash flow, plus two ESG targets; LTI as performance
  share units (Remuneration Report 2024/25).
- Control: the founder's three family lines hold all 34.32m A shares and about 12.3m B shares, 17.3% of capital and 61.5% of
  votes (Annual Report 2024/25, Shareholder information).
- Recalls: VivaSight 2 DLT, Class II, initiated 2022-06-03 (cuff leak or rupture) and again in 2024 (hyper-angulation of the
  distal end); aScope 5 Broncho HD sampler set, Class II, initiated 2025-04-07 (labelling), FDA recall database (the 2025
  record read at accessdata.fda.gov, res.cfm id 213353; the 2022 and 2024 records from search summaries, **not opened**). A
  search summary also reported a Class I recall of "Ambu SPUR II" initiated 2025-07-09; **not verified**. No FDA warning
  letter to Ambu found in that search (one web search, not a sweep of the FDA warning-letter database).
- Litigation: "Ambu does not expect any pending litigations, claims, and investigations to have a material effect on the
  Group's financial position" (Annual Report 2024/25, note 5.6). No investigation named.

**Bearing on Q6 (the money and the owners).**
- Shares issued at DKK 262 (January 2021, DKK 1,300m gross), at DKK 93 (2022/23, DKK 1,054m net) and for DKK 667m in
  2017/18; shares bought back at an average DKK 85.91 (DKK 150m, December 2025 to February 2026) and DKK 66.78 (DKK 300m, May
  to September 2026, for cancellation). Both buyback prices sit far above the COMPUTATION range of DKK 27.47; no price
  ceiling found in the announcements read.
- Dividend: DKK 102m paid in 2024/25 (43% of 2023/24 profit); DKK 110m approved for 2024/25 at the AGM of 2025-12-04.
- The 2018 Invendo purchase (DKK 926m plus contingent consideration) and the 2023/24 impairment of DKK 327m of GI technology.

**Bearing on Q9 (debt).** Net cash DKK 509.6m after the September buyback; credit institutions DKK 19m and lease liabilities
DKK 560m at 2026-06-30. Equity ratio 79%.

**Bearing on Q12.** Medical devices for anaesthesia, patient monitoring and endoscopy; none of Q12's named businesses.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template copy and the notes file were made before the first web
      request; the first commit, 9727554c, followed the report downloads); written question by question; committed when Q1
      closed (cfc984e7) and at the close.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's; the fold is the
      dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is
      declared under contamination at the top and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      `Test Runs/_research 2026-10-13 AMBBY/check_ids.py`); every filing fact names its document and date (departure 2: the
      Danish filings carry no accession numbers; SEC accessions are given where SEC documents were used).
- [x] The order was kept; Q1 closed the run; everything after it is NOT REACHED or headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy: operating cash flow less all capital spending including
      capitalised development, lease principal and stock pay; the sovereign from the issuing authority (Danish Debt
      Management Office), dated 2026-09-02 and six weeks old, said so; aggregator quotes flagged.
- [x] Contrary evidence written down as found (Foundations, five items); facts for later questions under AFTER THE STOP,
      with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only arithmetic from the tools: `tools/run.py` and `Screens/cover_shares.py` could not serve the name and nothing
      they printed was used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Parts without profit by part.** Q2's business-of-parts paragraph, which Q1 borrows to say which part "matters", is
defined on five-year operating profit by part; Ambu reports one operating segment and files no profit by part, so the run
confessed its own CONVENTION (revenue share plus the filer's statement of relative profitability). The text should say what
to do when the filer reports revenue by part and nothing else. (2) **The serial-acquirer test against which owner cash.**
Q7(c) compares net purchases with half of "owner cash before purchases" without saying which case: against the maintenance
case (DKK 1,147m over the window) Ambu is not a serial acquirer; against the all-spending case (DKK 36m) it is. The run used
the case that is central under specific (e) and wrote both down. (3) **A single-case range and the fair price.** Where
specific (b) leaves "the no-growth case alone", Part VII's fair price (each end case at ten percent, the two averaged) has
one end; the run valued the single case at ten percent. (4) **The no-growth case and purchases.** Specific (c) stops
purchases after year ten "when growth stops"; in a range that is no-growth from year one it is unclear whether purchases are
charged in years one to ten at all, since no growth is credited for them. The run charged them (the default pair) and showed
the organic pair beside. (5) **The sovereign's date.** The Danish authority publishes its longest bond's yield at auctions,
here six weeks before the run, and no daily official series for it was found; the protocol does not say how old an
issuing-authority figure may be. (6) **Q1's test 5 when the insiders do write it down.** The row asks whether insiders
"would not want to put down on paper their predictions" **[M2000-105]**; Ambu's insiders publish a forecast every year and
have missed it badly. The run read a published forecast badly missed as evidence for NATURE at least as strong as a refusal
to write; the text does not say so, and another analyst could read the same record as a WORK question about the
management's forecasting rather than about the industry.
