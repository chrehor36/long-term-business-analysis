# Company Run — TPI Composites, Inc. (OTC Pink: TPICQ; SEC CIK 1455684) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md`, with three departures stated in the brief: the lines of
evidence are derived by the analyst from the FY2025 10-K (listed below); the competitors are the rivals the 10-K names;
the ticker is not in SEC's ticker file (deregistered), so the CIK is used and the tools' ticker lookups are bypassed by hand.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. The dispatching session
fills it at the fold. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (TPICQ; also searched for TPIC and TPI Composites); not held.*

**CONTAMINATION, declared:** (1) a directory listing of `Test Runs/` made to check for today's file names showed the names of
eleven other run files and research folders dated 2026-10-13 (other companies; none opened). (2) The session-start git log
showed commit subjects of another company's run and fold of 2026-10-13, with its box and figures. (3) The memory index loaded
into the session names queue state (a wave count, a gate-clearer count). None of it bears on this company; none was used.
No `Test Runs/` file about TPI Composites under any name or ticker was opened, listed or searched.

**Lines of evidence, chosen by the analyst from the FY2025 10-K's Item 1, Item 1A and Item 7** (accession
0001193125-26-124194): (i) the chapter 11 cases and what the filer says the common stock will receive; (ii) the section 363
sales of 2026 and their prices; (iii) customer concentration and its history (Vestas, GE Vernova; earlier Nordex, Siemens
Gamesa, ENERCON); (iv) how blades are priced (dedicated-capacity supply agreements, annual price reductions, raw-material
pass-through); (v) competition, including the OEMs' own in-house blade plants and the Chinese makers; (vi) operating margin
and owner cash over the ten filed years; (vii) the balance sheets over ten years, the debt, the DIP facility and the
liabilities subject to compromise; (viii) the CBP/UFLPA import restriction and the wind tax-credit phase-out; (ix) pay
and retention awards around the petition (integrity facts, recorded only).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $0.01 a share (OTC Pink; aggregator digrin.com, latest monthly close shown "October 2026", fetched 2026-10-13;
  **aggregator, flagged**, operator rule 5; Yahoo, Stooq and the OTC Markets API returned nothing; a web search summary gave the
  same $0.01). The quote is rounded to the cent and its exact level below a cent is not known.
- **Shares by class** from the latest filing's cover: **48,765,812 common shares outstanding as of 2026-01-31** (FY2025 10-K
  cover, filed 2026-03-25, accession 0001193125-26-124194). `python Screens/cover_shares.py TPICQ` returned "NOT AN SEC
  REGISTRANT in the live ticker file", so the count is taken by hand. Checked against the filed balance sheet: 50,381 thousand
  issued less treasury, 48,766 thousand outstanding at 2025-12-31. One class only. No 8-K or prospectus after the 10-K changes
  the count; the Form 15 (15-12G, 2026-03-26, accession 0001193125-26-126250) ends reporting, so no later count will be filed.
- **Market cap:** $0.49M (0.01 × 48.766M).
- **Sovereign for the earnings currency (USD):** 5.60%, US Treasury daily par yield curve, 30-year, 10/09/2026 (via
  `tools/sources.py`, printed by `tools/run.py`; issuing authority).
- **Filings read** (operator rule 4): FY2025 10-K, filed 2026-03-25, accession 0001193125-26-124194 (Items 1, 1A, 5, 7 in
  part, 11 in part, the balance sheet, the explanatory note); FY2024 10-K, accession 0000950170-25-024274 (Items 1, 1A in
  part); FY2020 10-K, accession 0001564590-21-008945 (Item 1 and the customer-concentration risk factor); 8-K of 2026-03-05,
  accession 0001193125-26-094276 (Vestas India and Mexico agreements; DIP default); 8-K of 2026-03-09, accession
  0001193125-26-097651 (ECP purchase agreement). The latest 10-Q (Q3 2025, accession 0001193125-25-274259) was not read
  in full: the 10-K supersedes it. No proxy was filed for 2025 (the last DEF 14A is 2024-04-22, accession
  0001193125-24-104830, not read); FY2025 Part III is inside the 10-K and its Item 11 was read in part.
  **One figure cross-checked against the filed statement:** total liabilities $1,021,909 thousand on the filed balance sheet
  at 2025-12-31 against $1,022M in `tools/run.py`'s XBRL table; agrees.
- `tools/run.py` could not resolve the ticker ("not an SEC filer"). It was run through a wrapper in the research folder
  (`run_wrapper.py`) that patches only the CIK lookup to 0001455684 and injects the aggregator price; the arithmetic is
  run.py's own (output in `run_py_output.txt`). Arithmetic lines only were used (Part VII). Owner cash after every real cost,
  as filed (OCF less stock pay less capital spending; USD millions): 2021 −71.1, 2022 −96.2, 2023 −127.0, 2024 −20.4, 2025
  −143.4; five-year mean **−91.6** (capex basis), −103.8 on the depreciation basis. The alternates run.py prints but does not
  choose: paid-in-kind interest added back inside operating cash, +46.1 in 2024 and +51.9 in 2025 (non-cash interest owed to
  the term lenders), and finance-lease principal of 0.7 to 5.8 a year; with them the five-year mean is −114.4. Stock pay is
  2.4 to 15.1 a year. Earlier years, from the same XBRL facts (first-filed values, which include operations later
  discontinued): 2016 +19.4, 2017 +22.7, 2018 −63.8, 2019 −23.0, 2020 −38.5. **Ten-year sum −541.3; owner cash was positive
  in two of ten years.**
- **The balance sheets, ten year-ends (read here because the file closes before Q4; USD millions, run.py's first-filed XBRL
  table, the 2025 column checked against the filed statement):** equity 107 (2016), 161, 221, 205, 201, 122, 50, −122, −373,
  **−679 (2025)**; retained earnings −183 (2016) falling every year after 2018 to **−1,118**; total assets 437 → 1,008 (2021) →
  **342**; total liabilities 331 → **1,022**; cash 119 (2016) → 242 (2021) → **13.9** (plus 10.2 restricted); receivables 68 on
  sales of 769 (2016) and 51 on sales of 918.5 (2025); inventory small throughout (6 to 67); goodwill 3 throughout, so the
  business was not built by purchase. Debt: long-term debt 125 (2016) to 218 (2020), down to 61 (2022) after the 2021
  preferred issue, then **606 (2023) and 705 (2024)** after the Series A preferred was exchanged for an Oaktree term loan
  (December 2023) carrying paid-in-kind interest. At 2025-12-31: DIP financing 23.9, current maturities of debt 432.2,
  liabilities subject to compromise 323.8 (including 31.4 of warranty reserve), operating leases 67.7. What the figures say
  "and what they don’t say and what they can’t say" **[M2025-032]**: the equity was consumed by eight years of losses and is
  now negative by $679M; the debt that replaced it is senior to the common; the balance sheet does not say what the assets
  fetch, and the March 2026 sale agreements do (below).

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own it "if the market closed for five years" **[M1997-109]**? The filer
itself says what a share of TPICQ will be at the end of the case: "the Company expects that holders of the Company’s common
stock will not receive distributions in the Chapter 11 Cases, and that the equity will be canceled" (FY2025 10-K,
explanatory note, accession 0001193125-26-124194), and it calls trading in the stock "highly speculative". Anyone paying $0.01
for the share is paying for "what the next fellow will pay for it" **[L2000-027]**, since what the asset produces goes to the
creditors. The market's $0.49M is a price, not an instruction **[M2006-077]**. **Contrary evidence, written down as found**
**[M1997-127]**: for the business, the filer's case is real: over 103,000 blades made since 2001, a quality record it calls
strong, two of the world's largest OEMs as customers, and buyers (Vestas, ECP, GE Vernova as back-up) willing to pay to
keep the plants running. For the share, no contrary evidence was found in the filings read: the 10-K's explanatory note says
it cannot assure "creditors or stockholders will receive any recovery".

## THE STANDING RULE
The buyer's conduct, not the target's: a cash purchase sized so that its loss would not touch what the buyer needs does not
breach the rule. Recorded for the buyer: the filer expects the equity to be canceled, so the price paid is expected to be a
"permanent loss of capital" **[L2023-005]**; the rule forbids risking "what we have and need" **[M2012-081]** and binds the
financing and size of any purchase, whatever the questions conclude.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**, decided "off the figures" **[M2008-069]**; the chemistry need not be understood if "the
  economic dynamics of the industry" are, "are there competitive moats? Is there ease of entry?" **[M2011-014]**.
- **The key variables, read from the filings.** (1) Volume: dedicated capacity sold to a few turbine OEMs under supply
  agreements with minimum annual volumes (FY2025 10-K, Item 1); GE Vernova 56.4% and Vestas 41.9% of 2025 net sales (Item 1A).
  (2) Price: set by contract, with "annual sales price reductions reflecting assumptions regarding improvements in our
  manufacturing efficiency", raw-material increases "typically" shared and, for one customer, borne 100% by the customer
  (Item 1). (3) Cost: labor-heavy plants, 7,800 of 9,600 associates in Mexico (Item 1, Human Capital). (4) The customers'
  alternative: "a significant percentage of wind turbine OEMs, including all of our current customers, produce some of their
  own wind blades in-house" (Item 1A). These are the economics of a contract manufacturer whose customers are also its
  competitors, and they can be read from the figures without forecasting wind demand or policy (no macro enters).
- **Where it will be in ten years.** The filer has written it down: the company is selling "substantially all of the Debtors’
  assets" under section 363 (Item 1, Business Strategy), the Chennai and Matamoros plants to Vestas for about $10.0M and
  $14.0M, the U.S. and Mexico business to ECP Blade Holdings for about $20.0M, with GE Vernova as back-up at about $21.0M
  (explanatory note; 8-Ks 0001193125-26-094276 and 0001193125-26-097651), and the equity "will be canceled". The economics of
  the blade business are readable, and the fate of the security is stated by its issuer. Q1 does not need the wind market's
  next decade to answer either.
- Routing checked: this is not a business whose ten-year economics cannot be foreseen because its industry changes fast
  (blade making is an established process, vacuum infusion of composites since 2001 on the filer's account); policy changes
  (the OBBBA phase-out of the PTC and AMPC, the CBP review) bear on volume, which Q2 weighs.
- **VERDICT: IN.** The economic dynamics can be read from the figures **[M2011-014]**, **[M2008-069]**, and the competitive
  position over five or ten years can be fixed well enough to judge the castle **[M2012-065]**; what that fix shows is Q2's.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]** The filings answer that it is not standing: the company is in chapter 11 and its plants
are being sold. The tests, each with its filing fact:
- **The attacker with money.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I do
  it? [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]** The answer here is on the record and is yes,
  for far less: Vestas is buying the two plants that make its blades for about $10.0M (Chennai) and about $14.0M (Matamoros),
  and ECP Blade Holdings the U.S. and Mexico business for about $20.0M in cash plus assumed liabilities, against 2025 net
  sales of $918.5M (FY2025 10-K explanatory note; 8-Ks 0001193125-26-094276, 0001193125-26-097651). The customer can take the
  capacity in-house by buying it.
- **Pricing power and the agony before a rise.** "you can almost measure the strength of a business over time by the agony
  they go through in determining whether a price increase can be sustained" **[M2005-020]**. TPI does not raise prices; its
  supply agreements provide "annual sales price reductions", give discounts for volume above commitment, and pass raw-material
  costs through, with one customer buying the critical materials itself (FY2025 10-K, Item 1, Wind Blade Supply Agreements).
  Through the inflation of 2021 and 2022 the operating margin went from +1.1% (2020) to −5.6% (2021) and −1.8% (2022)
  (XBRL facts as first filed, accessions 0000950170-22-002105, 0000950170-23-003810). Pricing power of that kind belongs to "a
  monopoly or a near monopoly" **[M2010-092]**; here the buyers are few and the sellers many.
- **The rival who sets the price; the customer who is the competitor.** "whatever he charged for gas was my price" **[M2012-109]**;
  "he determined our profit, because we looked at his price every day" **[M2023-079]**. TPI's customers are also its
  competitors: "a significant percentage of wind turbine OEMs, including all of our current customers, produce some of their
  own wind blades in-house. As a result, we compete for business from a limited number of customers that outsource the
  production of wind blades" (FY2025 10-K, Item 1A). The customer knows the in-house cost of the product it is buying.
- **Would the customer still choose it over the low bid?** The test is whether people buy "for the low bid" **[M2017-009]**, and
  the failing answer is the customer who does not care "from whom they buy" **[L2004-003]**. The 10-K lists "total delivered
  cost" among the principal competitive factors and says Chinese makers, "supported by the Chinese government", have made the
  field outside the U.S. harder (Item 1, Competition). The customer list shows the choice being made against TPI: five blade
  customers in 2020 (Vestas, GE Wind, Nordex, Siemens Gamesa, ENERCON; FY2020 10-K, accession 0001564590-21-008945), two in
  2025, and the company "expects to focus its core wind blade business on supporting its operations with a single customer, GE
  Vernova" (FY2025 10-K, Item 1). "one competitor is frequently enough to ruin a business" **[M2012-108]**; here one customer's
  withdrawal is.
- **The low-cost position; labor content.** "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**;
  "In an unregulated commodity business, a company must lower its costs to competitive levels or face extinction." **[L1994-035]**
  A blade is heavy in labor (7,800 of 9,600 associates in Mexico) and crosses a border to its market; "we do not want to buy into
  a business that has a very high labor content and that has a product that can be shipped in from abroad very easily"
  **[M2007-116]**. The CBP has restricted the import of "a substantial portion of the wind blades manufactured at our Mexico
  facilities" under the UFLPA review (FY2025 10-K, Item 1, Customs Review). No filing read states a cost advantage over the
  in-house OEM plants or the Chinese makers; the filer says it competes "favorably", and its margins (below) do not show it.
- **Unit volume.** Net sales $769.0M (2016), $1,732.6M (2021), $918.5M (2025); backlog $237.6M at 2024 year-end and $114.8M at
  2025 year-end (Item 1, Backlog).
- **Ask the competitors.** The rivals the 10-K names (Item 1, Competition): LM Wind Power (a GE Vernova subsidiary), Sinoma
  Science & Technology, Shanghai Aeolon, Aeris Industria (Brazil), ZhongFu Lianzhong, Indutch Composites (India), and the
  vertically integrated OEMs. **Only GE Vernova (LM's parent) files with the SEC; Sinoma, Aeolon, Aeris, ZhongFu, Indutch and
  Vestas do not, and are flagged as unread.** LM Wind Power's own revenue, inside GE Vernova's Wind segment, fell from $610M
  (2023) to $542M (2024) to $217M (2025) (GE Vernova FY2025 10-K, accession 0001996810-26-000015).
- **Widening or narrowing; what could destroy it.** Narrowing on every measure read: customers five to two to one, margins
  positive to negative, equity positive to −$679M, and the plants sold to a customer and a financial buyer. No formula gives the
  moat's width, "You have to understand the businesses" **[M1999-108]**, but none is needed when the castle is being sold for
  less than five percent of a year's sales.
- **The competitor row** (same metric, operating or segment margin, from the filers' own 10-Ks; whole span read):

| Year | TPI operating margin (TPI 10-Ks, first filed) | GE Renewable Energy segment profit margin (GE 10-Ks) | GE Vernova Wind segment EBITDA margin (GEV 10-K) |
|---|---|---|---|
| 2016 | 5.6% | 6.5% | |
| 2017 | 7.6% | 6.3% | |
| 2018 | 2.4% | 3.0% | |
| 2019 | 1.1% | (5.2)% | |
| 2020 | 1.1% | (4.6)% | |
| 2021 | (5.6)% | (5.1)% | |
| 2022 | (1.8)% | (17.3)% | |
| 2023 | (11.2)% | (9.5)% | (10.5)% |
| 2024 | (8.2)% | | (6.1)% |
| 2025 | (19.5)% | | (6.6)% |

  Sources: TPI operating income over net sales from XBRL facts as first filed (accessions 0001564590-19-006097 for 2016 to 2018
  sales, 0001564590-17-004685 and 0001564590-18-004934 for 2016 and 2017 operating income, 0001564590-20-007922,
  0001564590-21-008945, 0000950170-22-002105, 0000950170-23-003810, 0000950170-24-018800, 0000950170-25-024274,
  0001193125-26-124194); GE 10-K FY2018 (accession 0000040545-19-000014), FY2021 (0000040545-22-000008), FY2023
  (0000040545-24-000027); GE Vernova FY2025 10-K (0001996810-26-000015). GE's Renewable Energy segment includes Grid and Hydro;
  GE Vernova's Wind segment is onshore, offshore and LM Wind Power. The rival's figures are a segment profit or segment EBITDA,
  TPI's an operating income: the definitions differ, and the rival's EBITDA flatters it against TPI. TPI's ten-year operating
  income sums to **−$402.4M** on sales of $12.8B, an average margin of −3.1%; its best year is 7.6%.
- **The parts table.** The filer reports three geographic segments (U.S., Mexico, India) of one business, blades for OEMs under
  dedicated-capacity agreements, with field service about 5% of sales (Item 1). The parts do not have different economics in
  the filings read, so the business is read whole; Mexico, with four of six plants and 7,800 associates, is the largest part and
  would decide under the business-of-parts convention, on the same evidence.
- **The field's returns over the last full cycle.** The moat is what "protects excellent returns on invested capital"
  **[L2007-004]**. Over 2016 to 2025 neither TPI nor the one rival that files earned them: TPI's margin peaked at 7.6% and was
  negative from 2021; GE's renewable business was negative from 2019 through 2023, and GE Vernova's Wind segment from 2023
  through 2025. "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**. Judged in words, as
  the convention requires: the field's returns over the span are not ordinary but poor, and TPI's are the poorer of the two.
- **What it rules OUT.** The business whose price the customer sets **[M2012-109]**, **[M2023-079]**; the high-cost producer in a
  commodity field **[L1994-035]**, **[M1997-010]**; high labor content in a product shipped across a border **[M2007-116]**; the
  customer who buys on the low bid **[L2004-003]**, **[M2017-009]**. A cheap price does not reopen it: "What you can’t do is
  turn any investment into a good deal by paying little" **[M2019-015]**; "If you really think a business is declining, most of
  the time you should avoid it." **[M2012-062]**
- **Contrary evidence, written down** **[M1997-127]**: the filer claims long customer relationships, proprietary process
  know-how and a field quality record, and two OEMs and a financial buyer chose to buy the plants rather than let them close,
  which shows the capacity has value to someone. It shows the value goes to the buyer at a price of about $44M, not to the
  owner of the castle.
- **Why OUT and not TOO HARD.** TOO HARD is for a castle "whose future cannot be judged", the tenuous moat of "We don’t know how
  to valuate that" **[M2000-019]**. Here the future is not unknown: the filings show the castle open (the customers make the
  product, set its price, and are buying the plants) and the returns known and negative over ten years.
- **VERDICT: OUT.** The castle is shown open on the evidence of the filer's own 10-Ks and 8-Ks and the one filing rival's 10-Ks:
  the attacker with money is the customer, and it is buying the plants **[M2011-015]**; the price is set by the buyers and falls
  by contract **[M2005-020]**, **[M2012-109]**; the field's returns over the full span are poor **[L2007-004]**, **[M2013-052]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. WEIGHING.
NOT REACHED (the file closed OUT at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten balance sheets were read in Step 0, as the brief requires when the file closes before Q4.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED. Integrity facts found are recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's reporting figures are computed beneath the stop.

**COMPUTATION, NOT A CLEARANCE** (operator rule 3; nothing below changes the box).
- **Inputs.** Owner cash after every real cost (OCF less stock pay less all capital spending), the company's tax already paid
  inside OCF, from the XBRL facts as first filed (run.py's table for 2021 to 2025; the same facts for 2016 to 2020, which include
  operations later discontinued). On the all-equity basis cash interest paid is added back (2016 to 2025: 11.1, 11.8, 9.9, 8.2,
  9.9, 13.4, 5.7, 9.7, 13.5, 10.5; `InterestPaidNet`). Owner cash before interest, USD millions: 2016 +30.5, 2017 +34.5, 2018
  −53.9, 2019 −14.8, 2020 −28.6, 2021 −57.6, 2022 −90.5, 2023 −117.3, 2024 −6.9, 2025 −132.8.
- **Specific (a), the cycle base.** The last window year, 2025, is aberrational on the filer's own description (chapter 11 from
  August, $49.6M of reorganization items, the Türkiye business sold, the CBP import restriction). The filer describes no
  completed cycle. **CONVENTION of this run:** the cycle base is the ten-year record 2016 to 2025, the longest span of filings
  read; rationale: the convention asks for a peak-to-peak average and the only positive years (2016, 2017) sit at the start, so
  the ten years are the widest base the filings give and the one most favourable to the business. Cycle base **−$43.7M** a year
  (ten-year mean, before interest); the literal five-year window, beside it, **−$81.0M**.
- **Specific (b), decline.** Every year from 2018 to 2025 is negative; a compound growth rate between negative end years is
  meaningless, and so is one between the halves of the window (2021 and 2022 average −74.1; 2024 and 2025 average −69.9; both
  negative). By (b) the range is the no-growth case alone, and it is said so.
- **Specific (c), acquisitions.** None in the window (goodwill $2.8M throughout). The signed, unclosed 363 sales are a sale of
  the company's assets, not a purchase by it; their cash prices (about $44M in all, ECP's $20M or GE Vernova's $21M back-up
  alternative) go first to the DIP and pre-petition lenders on the filer's own statement that the common will receive nothing.
- **Specific (d), working capital:** inside OCF as filed. **(e), maintenance:** the filing gives no maintenance figure; the
  depreciation variant (OCF less stock pay less D&A, before interest) is shown beside: five-year mean −$93.3M; even with no
  capital spending at all the five-year mean is −$54.5M. **(f), the cap:** not reached; there is no positive growth to cap.
- **Whole-business value, no growth, at the 5.60% sovereign:** −$43.7M / 0.056 = **−$780M** (cycle base, central); −$1,446M
  (literal window, beside). **Net debt at 2025-12-31** (borrowings less cash, as the filing states them; restricted cash of
  $10.2M and operating leases of $67.7M left out, said so): DIP 23.9 + current maturities of debt 432.2 − cash 13.9 =
  **$442.2M**, before the $323.8M of liabilities subject to compromise, which also rank ahead of the common.
- **(a) VALUE RANGE, per share, all-equity basis:** **−$25.07** (cycle base, central) and **−$38.73** (literal window, beside),
  against a price of **$0.01**. Equity-only basis, beside (owner cash after interest, ten-year mean −$54.1M, five-year −$91.6M):
  −$19.81 and −$33.54. Every case is below zero, so **no case earns the floor at any positive price** and the floor test closes it
  before the width is asked (Q7, The floor is tested first): "there’s just a point at which we drop out of the game"
  **[M2003-149]**. The filer's own expectation agrees in sign: no distribution to the common.
- **(b) FAIR PRICE** (each end case valued at ten percent, averaged; Part VII; here one case, by specific (b)): all-equity,
  central: −$43.7M / 0.10 = −$437M, less net debt $442.2M, **−$18.03 a share**; equity-only, beside: −$54.1M / 0.10 = −$541M,
  **−$11.09 a share**. **There is no positive fair price.** Neither figure is a verdict or entry language.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES. STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH. WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2.** The castle is shown open on the filings: the customers make the product in-house, set its price by contract with
annual reductions, and are buying the plants (about $44M in all against 2025 sales of $918.5M); ten-year operating income
−$402.4M; the field's one SEC-filing rival is also negative from 2019. COMPUTATION beneath the stop: value range −$25.07 (all-
equity, cycle base) and −$38.73 (literal window) a share against $0.01; no case earns the floor; fair price −$18.03 all-equity,
−$11.09 equity-only, no positive figure. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; the box is unchanged (operator rule 2)* **[M1997-127]**.
- **Q3 (capital):** capital spending of $30.5M to $74.4M a year in 2016 to 2020, while sales doubled from $769.0M to $1,670.1M;
  owner cash was negative in 2018, 2019 and 2020 and every year after (XBRL facts as first filed).
- **Q4 (accounts):** the MD&A features adjusted EBITDA (the phrase appears 33 times in the FY2025 10-K text; the FY2024 10-K
  reconciles "EBITDA, adjusted EBITDA, free cash flow and net cash (debt)"); paid-in-kind interest of $46.1M (2024) and $51.9M
  (2025) is added back inside operating cash; the Series A preferred was exchanged for the Oaktree term loan in December 2023
  with a gain on extinguishment recorded; revenue is recognized over time on the ratio of costs incurred to "total estimated
  direct costs", and the filer lists the complexity of those forecasting assumptions among the reasons its results are hard to
  predict (FY2025 10-K, Items 1A and 7).
- **Q5 (integrity, recorded, not judged):** on 2025-06-13 the compensation committee approved retention bonuses, paid in June
  2025, two months before the petition, including $1,225,459 to the chief executive and $518,155 to the chief financial officer,
  in place of the 2025 cash incentive and equity awards (FY2025 10-K, Item 11, "Special award granted in 2025"); performance
  stock units had been tied to "three annual Adjusted EBITDA targets" (Item 11). Any later run that reaches Q5 must answer them.
- **Q6 (owners):** the common is expected to be canceled; shareholders' equity of $221M at 2018 was consumed by losses and by the
  preferred-to-loan exchange. No buyback or dividend found in the filings read.
- **Q9 (debt):** DIP event of default notified 2026-03-01, waived 2026-03-16 with an extended maturity (8-K
  0001193125-26-094276; 10-K Item 1A); the pre-petition Oaktree credit agreement in default and accelerated, enforcement stayed;
  operations funded in part by customers' "advance payments and other accommodations" (8-K 0001193125-26-094276); warranty
  reserves $45.8M, $31.4M of it subject to compromise.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). The copy
      preceded the first fetch; the first commit followed the price fetch and the run.py arithmetic by minutes.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's; the run is folded by the
      dispatcher (operator rule ten). Pathspec commits of the two paths only.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (file names
      in a directory listing, commit subjects at session start, memory-index lines) is declared under contamination, not used.
- [x] Every v5 id resolves and every quoted fragment beside an id is in its row (`check_ids.py` in the research folder); every
      filing fact has its accession; no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION.
- [x] Owner cash after every real cost, never a net-income proxy; the sovereign from the Treasury; the aggregator quote flagged.
- [x] Contrary evidence written down as found (foundations, Q2); facts for later questions under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; it was run through a CIK-patching wrapper, said so in Step 0.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) The framework has no route for a security its own issuer says will be canceled. Q1 asks about the business,
Q2 about its castle, Q7 about the cash to the owner; none asks first whether the instrument offered is still a claim on the
business at all. Here the answer sat in the 10-K's explanatory note, and the file had to travel to Q2 to close on the business
when the filer had already closed it on the share; the run recorded it in the foundations and let Q2 decide. A line in the
foundations or Q1 for the common of a company liquidating in chapter 11 would save the trip and say which box it goes in. (2)
Q7's specific (a) asks for "the average over the last full cycle, peak to peak or trough to trough", which a business with its
only positive years at the start of its filed record does not have; the run confessed its own CONVENTION (the ten-year record),
and the sign of every figure is the same without it. (3) `tools/run.py` and `Screens/cover_shares.py` resolve names only through
SEC's live ticker file, so a deregistered filer cannot be run without a hand-made wrapper; a `--cik` argument would make the
brief's departure unnecessary. Also unclear in practice: the brief's reporting figures assume a positive range; the run reports
them as negative numbers and says there is no positive fair price, which is the honest form but may not be what an alert
script expects.
