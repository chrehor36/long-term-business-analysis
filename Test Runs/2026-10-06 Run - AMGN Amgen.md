# Company Run — Amgen Inc. (NASDAQ: AMGN) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule (`PORTFOLIO.md` not opened). Contamination: the analyst carries a training-memory prior of Amgen (a large biotechnology company; Enbrel, Prolia, Repatha; the Horizon acquisition of 2023); it is a prior to be replaced by the filings.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
Working folder: `Test Runs/_research 2026-10-06 AMGN/` (`run_py_output.txt`, `cover_shares_output.txt`,
`sources_output.txt`, `facts.py` and `facts_output.txt` (SEC companyfacts transcription), `calc.py` and
`calc_output.txt` (the arithmetic below), `row.py` (ledger lookup), `h2t.py`; raw filings and their text in `cache/`,
gitignored).

- **Price:** $402.98 (2026-10-05; `tools/run.py` live quote, AGGREGATOR, flagged per operator rule 5).
- **Shares by class:** 540,632,005 common, $0.0001 par, one class, cover of the 10-Q for the quarter to 2026-06-30, filed
  2026-08-05, accession `0000318154-26-000126` (`python Screens/cover_shares.py AMGN`). Balance-sheet count 540.6M at
  2026-06-30 (same 10-Q). Average diluted shares Q2 2026: 544M (earnings release, below).
- **Market cap:** about $217,864M (540.632M x $402.98).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-13, accession `0000318154-26-000010` (Item 1 business,
  significant developments, products, the patent table; Item 1A risk factors in part; Item 7 MD&A overview and product
  sales; the cash-flow statement); 10-Q for the quarter to 2026-06-30, filed 2026-08-05, `0000318154-26-000126` (cover,
  cash-flow statement); 8-K of 2026-08-04, `0000318154-26-000124`, Exhibit 99.1, the second-quarter 2026 earnings release
  (product table, non-GAAP reconciliation, 2026 guidance, pipeline update); 8-K of 2026-07-31, `0000318154-26-000119`
  (Item 1.05, a material cybersecurity incident); 8-K of 2026-01-30, `0001193125-26-030518` (Item 1.02, the rocatinlimab
  collaboration terminated); 8-K of 2026-02-19, `0001193125-26-059490` (Item 1.01, $4.0B of new senior notes); 8-Ks of
  2026-04-22 `0000318154-26-000048` and 2026-05-19 `0000318154-26-000097` (Item 5.02, the chief technology officer's
  retirement and a new chief financial officer from 2026-09-01). DEF 14A filed 2026-04-07, `0001193125-26-145588`:
  retrieved, not read, because the file closed at Q1 before the pay questions.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 $9,958M,
  Consolidated Statements of Cash Flows, 10-K `0000318154-26-000010`; `tools/run.py` transcribed 9,958. Agrees.
  **A discrepancy found in the same check:** stock-based compensation FY2023 is $431M on the filed cash-flow statement
  (10-K FY2025 and the companyfacts value from 10-K FY2023 `0000318154-24-000011`); `tools/run.py` printed 473 from the
  element `AllocatedShareBasedCompensationExpense`. The filed 431 is used below. Reported as a tool defect.
- **Arithmetic lines** (`tools/run.py` for 2023 to 2025; 2021 and 2022 from SEC companyfacts, the values reported in the
  10-Ks `0000318154-22-000010` and `0000318154-23-000017`; `calc.py`; USD M):

| FY | OCF | stock pay | capex | owner cash (capex basis) | D&A | owner cash (D&A basis) | businesses acquired, net of cash | owner cash after acquisitions |
|---|---|---|---|---|---|---|---|---|
| 2021 | 9,261 | 341 | 880 | 8,040 | 3,398 | 5,522 | 2,529 | 5,511 |
| 2022 | 9,721 | 401 | 936 | 8,384 | 3,417 | 5,903 | 3,839 | 4,545 |
| 2023 | 8,471 | 431 | 1,112 | 6,928 | 4,071 | 3,969 | 26,989 (Horizon) | -20,061 |
| 2024 | 11,490 | 530 | 1,096 | 9,864 | 5,592 | 5,368 | 0 | 9,864 |
| 2025 | 9,958 | 494 | 1,858 | 7,606 | 5,167 | 4,297 | 53 | 7,553 |

  Five-year mean: 8,164 (capex basis), 5,012 (D&A basis), 1,482 after the businesses bought. Shown change of the
  aggregate, capex basis, 2021 to 2025: -1.4% a year. Against the market cap: 3.75% (capex basis) and 0.68% (after
  acquisitions). D&A runs four to five times capex because most of it is amortization of acquired product rights
  (`run.py` balance-sheet table: intangibles $32,641M at the end of 2023, $22,276M at the end of 2025). Which of these
  bases is the owner's cash, and whether buying products is the reinvestment needed to stand still, is a Q3 and Q4
  question; it is NOT REACHED (the file closes at Q1), and nothing above is a clearance. **COMPUTATION — NOT A
  CLEARANCE.** 2026 guidance (earnings release): capex about $2.6B; share repurchases "not to exceed $3.0 billion".

## THE FOUNDATIONS (not a gate)
Two foundations bear. **A share is a business:** "Would I be happy buying this stock if the market closed for five
years?" **[M1997-109]**; the answer turns entirely on what the business will be when the market reopens, which is Q1's
question here. **The analyst's habits:** the prior carried into this run (a durable large biotechnology franchise) is
the anchor the rows warn about, "the worst anchoring effect, which is always your previous conclusion" **[M2016-054]**,
and every business is read for "what’s wrong in things" **[M2025-013]**. **Who is paid to tell you:** the one forward
statement on file is the chief executive's, "we remain confident in our ability to deliver growth well into the next
decade" (earnings release, 8-K `0000318154-26-000124`); "don’t ask the barber whether you need a haircut"
**[M2011-083]**, and projections are not consulted **[M1995-050]**.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the record is strong on its face: product sales grew
10% in 2025 on 13% volume growth (10-K MD&A); Repatha (+36%), EVENITY (+34%), TEZSPIRE (+52%) and BLINCYTO (+28%) grew in
2025; in Q2 2026 "Twenty-two products delivered at least double-digit sales growth" and "Seventeen products are
annualizing at more than $1 billion" (release); owner cash, capex basis, has stood between $6.9B and $9.9B a year for five
years. (b) The rows themselves record the pharmaceutical group, read as a group, as a moat they underrated: "the
pharmaceutical industry, as a whole, has done very well" and "we did blow it" **[M1999-043]**. (c) The cybersecurity 8-K
says the company "has not identified any impact to its products, manufacturing operations, or financial reporting
systems" (`0000318154-26-000119`). All three are carried into Q1.

## THE STANDING RULE
A cash purchase of this stock, without borrowed money and sized so that a fall of half the price would not force a
sale, does not put the buyer at risk of ruin: "We are never going to risk what we have and need for what we don’t have
and don’t need." **[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**; the owner must
be prepared "to have it go down 50 percent — or more — and be comfortable with it" **[M2020-022]**. The rule is met by the
buyer's conduct, not by the target.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**, and "do I understand enough about this business so that the financial statements
will tell me the information that’s useful to me in making a judgment about what the future financial statements are
going to look like" **[M2008-033]**. The method is to identify "the key variables in that particular business, and
evaluating how predictable they were first, because that is the first step. If something is not very predictable,
forget it." **[M1998-044]**

**The filing facts.**
- *What the business is.* One segment, human therapeutics; 2025 product sales $35,148M (US 73%), total revenues $36,751M;
  three wholesalers took 77% of gross revenues (10-K FY2025 `0000318154-26-000010`, Item 1 and MD&A). The fourteen
  principal products run from ENBREL (launched 1998) to TEZSPIRE; "Other products" were $7,263M.
- *The products losing exclusivity, and how fast.* Prolia and XGEVA ($6,498M together in 2025, 18% of product sales):
  "Our patents for RANKL antibodies, including sequences, for Prolia expired in February 2025 in the United States and in
  November 2025 in select countries in Europe", and the same for XGEVA (10-K Item 1). In Q2 2026 the pair sold $1,111M
  against $1,654M a year earlier, -32.8%, "as multiple biosimilars have launched globally with more biosimilars
  expected" (release, 8-K `0000318154-26-000124`). The filer's general statement: "Upon the expiration or loss of patent
  protection and/or applicable exclusivity for one of our products, we can lose the majority of revenues for that
  product in a very short period of time." (10-K Item 1A). In the patent table of the same 10-K, the first-listed US
  antibody, compound or protein patent (for Nplate the only listed patent, a formulation) has expired or expires by the
  end of 2029 for Prolia, XGEVA, Repatha (8/27/2029), Otezla (2/16/2028), ENBREL (11/22/2028 and 4/24/2029), EVENITY
  (4/25/2026), TEPEZZA (3/3/2029), Nplate (2/12/2028), KYPROLIS (12/7/2027) and KRYSTEXXA (4/11/2026): $22,284M, 63.4% of
  2025 product sales (`calc.py`). Later method, formulation and use patents are listed for several of them (to 2037 to
  2042 for ENBREL, Otezla XR, TEPEZZA and KRYSTEXXA); what they protect is a question of litigation the filing does not
  settle.
- *The price, set by government.* "CMS has set Medicare Part D prices for ENBREL, effective January 1, 2026, and Otezla,
  effective January 1, 2027, in each case at significantly lower prices"; the IRA adds drugs each year "such that by 2031
  approximately 100 drugs would be subject to such set prices"; in December 2025 Amgen announced it is "taking actions
  that satisfy the components outlined in the July MFN Letter, including the Administration’s MFN pricing requests"; and
  of the whole pricing contest the filer writes: "the outcome of any such alignment is difficult to predict" (10-K Item 1,
  Reimbursement). ENBREL, its US patents intact and US biosimilars "approved but not launched", fell from $3,697M (2023)
  to $2,226M (2025), -39.8%, the 2025 fall "primarily driven by lower net selling price of 36% resulting from the impact
  of increased 340B Program mix, U.S. Medicare Part D redesign and higher commercial discounts" (10-K MD&A). Otezla's
  intangible asset was impaired $1.2B in 2025 after its selection for price setting (10-K MD&A, other operating
  expenses); it was bought in November 2019, a year in which payments for businesses acquired were $13,617M (companyfacts,
  10-K FY2019 `0000318154-20-000017`).
- *The filer says the business must keep inventing or buying to stand still.* "Our long-term success depends, to a great
  extent, on our ability to continue to discover, develop and commercialize innovative products and acquire or collaborate
  on therapies currently in development by other companies. We must grow sales from existing and new products to achieve
  revenue growth and to offset revenue losses caused by products’ loss of their exclusivity or launches of competing
  products." and "We devote considerable resources to R&D activities, but successful product development in the
  biotechnology industry is highly uncertain." (10-K MD&A overview). R&D was $7,272M in 2025, up 22% (10-K MD&A).
  Businesses bought 2021 to 2025: $33,410M, of which Horizon $26,989M in 2023 (Step 0 table).
- *What is to replace the eroding products is not yet approved.* The largest programme, MariTide, is in nine Phase 3
  studies in obesity and its complications, with three more to start in 2026, against "weekly tirzepatide or weekly
  semaglutide" named in its own switch study (release); olpasiran is in three Phase 3 outcome or plaque studies;
  xaluritamig and dazodalibep are in Phase 3 (release). The record of the last twelve months: bemarituzumab dropped after
  two Phase 3 studies (10-K Item 1); rocatinlimab returned to Kyowa Kirin (8-K `0001193125-26-030518`); AMG 513
  discontinued; two subcutaneous blinatumomab studies on partial clinical hold; and the FDA asked that TAVNEOS, bought
  with ChemoCentryx in 2022, be withdrawn from the US market, citing "the process followed by ChemoCentryx to
  re-adjudicate primary endpoint results" (10-K Item 1; release).

**The key variables and whether they are foreseeable** **[M1998-044]**. (1) The pace at which today's products erode:
foreseeable in direction for the denosumab pair and for the products whose first patents run out by 2029, not in pace
or depth, which the filer itself says can be "the majority of revenues [...] in a very short period of time", and which
for ENBREL was set by price policy before any patent fell. (2) Which of the Phase 3 programmes succeed, and at what share
of a market already held by others: the filer calls development "highly uncertain"; twelve months produced one Phase 3
failure, one returned programme, one discontinued molecule, one withdrawal request and one clinical hold. (3) The price
the US government and the large payers will allow on whatever is sold in the 2030s: the filer calls the outcome
"difficult to predict", and its own ten-largest-selling product list already carries two government-set prices. The ten-
year earning power is the product of (2) and (3) applied to sales that do not yet exist; (1) only tells how large a gap
they must fill.

**The tests.**
1. *Where will it be in ten years?* "You’re trying to print the next 10 years of Value Line in your head. And there’s
   some companies that you can do a reasonable job with, and there’s others that are just too tough." **[M1999-132]**. On
   the filings, nearly two thirds of today's product sales face the end of their first US patent within four years, and
   what stands in its place in 2035 is a set of trial results not yet read. I cannot print it.
2. *The key variables, and how predictable* **[M1998-044]**: above; the deciding two are not predictable.
3. *Is it important and knowable?* "If something’s important but unknowable, forget it." **[M2006-076]**. Trial
   outcomes and future price setting are the most important inputs and are not knowable from any document on file.
4. *Would the insiders write it down?* "They would say, “That’s too hard.”" **[M2000-105]**. The insiders here have
   written, in the 10-K, that development "is highly uncertain" and the pricing outcome "difficult to predict". The one
   forward statement, "well into the next decade", carries no figures.
5. *The row that names this industry.* "Take pharmaceuticals, if they had never invented any more pharmaceuticals, it
   would be a terrible business." **[M1999-075]**, said of businesses "quite dependent on the technology continuing to
   gallop". The filer's own sentence, "We must grow sales from existing and new products [...] to offset revenue losses
   caused by products’ loss of their exclusivity", is the same statement made from the inside.
6. *Can I name the winner, not just the industry?* "there’s industries we know that may have a wonderful future, but we
   don’t have the faintest idea who the winners will be" **[M2012-067]**; of this industry in particular, "I do think
   it’s very hard to pick out the winner." **[M1999-044]**. The obesity market MariTide aims at is held by the makers of
   the two drugs its own switch study names.
7. *Is the forecast about customers or about technology?* **[M2017-019]**, **[M2023-030]**. Here it is about clinical
   results and government price, not about how a consumer will behave.
8. *How far off could I be?* "The chances of being way wrong in IBM are probably less, at least for us, than being way
   wrong with Google or Apple." **[M2012-073]**. The company's own purchase of Otezla was written down $1.2B six years
   after it was bought, on a price decision no one put in the purchase case; TAVNEOS, bought in 2022, is under a
   withdrawal request. The buyer with the most information has been way wrong twice in seven years.
9. *Do I doubt it is inside?* Then it is not: "if you have doubts about something being into your circle of competence,
   it isn’t." **[M2002-092]**.

**Contrary evidence weighed, not dismissed** **[M1997-127]**. The record in the foundations is real: 2025 volume growth of
13%, the growing products named there, owner cash steady at $6.9B to $9.9B a year. But "You don’t get paid for what’s already happened." **[M2007-025]**; the
question is the ten-year fix **[M2012-065]**, and growth in an industry does not tell "what its profit margins and returns
on capital will be as a host of competitors battle for supremacy" **[L2009-005]**. **[M1999-043]** says the speakers
erred in not buying "a group of leading pharmaceutical companies at a below-market multiple"; the same answer says "it’s
very hard to pick out the winner" and that the purchase would have been a group **[M1999-044]**. It is evidence for the
industry, read as a basket, not for this one company read alone; whether a basket can be inside the circle when no
member is (section VI, Q1: **[M2002-060]** and **[M2010-085]** against **[M2002-092]**, READER) is not this run's question.

**The cause, WORK or NATURE** (section I, the two causes). The deciding questions are (2) and (3) above: which molecules
now in Phase 3 will succeed against the incumbents, and what the US price of the products sold in the 2030s will be. More
reading of Amgen's documents would not answer them: the company's own scientists and officers, with every document,
call the first "highly uncertain" and the second "difficult to predict". That is the insiders declining to write the
forecast down **[M2000-105]**, the industry's own roadblock: "the nature of the industry would be the roadblock" and
"We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries."
**[L1993-023]**; **[L1999-018]**. NATURE.

**VERDICT: TOO HARD (NATURE).** Amgen's ten-year earning power rests on the outcome of trials not yet read and on drug
prices not yet set, both of which its own 10-K calls unpredictable; "If something is not very predictable, forget it."
**[M1998-044]**; "If something’s important but unknowable, forget it." **[M2006-076]**. The box is "too hard"
**[M2006-013]**, and it is no judgment of quality: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling
for a fraction of its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. A lower price does not
reopen it **[M2000-038]**, and the circle is not enlarged to find something to buy **[M1995-018]**. The file closes here.
*(Routing note: the framework lists **[M1999-075]** under Q1's "What it rules OUT"; this run reads the row by its stated
reason, dependence on technology continuing to gallop, which the framework's own routing sends to TOO HARD, not OUT
(**[L1993-023]**, **[M1998-008]**). Recorded below under what was unclear.)*

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**NOT REACHED.** The file closed at Q1. No competitor row was fetched, since the castle tests are reached only by a
business Q1 has passed.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.** For the record only, and not a weighing: the Step 0 table shows $33,410M paid for businesses over five
years against $40,822M of owner cash on the capex basis, which is the question Q3 would have had to answer first.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** Seen in passing and recorded for a later run, not weighed: the earnings release headlines non-GAAP EPS
beside GAAP EPS, excludes "noncash amortization of intangible assets and fair value step-up of inventory acquired from
business combinations" and "Certain net charges pursuant to our restructuring and cost-savings initiatives" (present in
both Q2 2025 and Q2 2026), does not exclude stock pay, and states that the non-GAAP measures are used "to evaluate
results relative to incentive compensation targets" (EX-99.1, 8-K `0000318154-26-000124`). The ten-year balance-sheet
table is in `run_py_output.txt`; the filed statements behind it were not read.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** The proxy (`0001193125-26-145588`) was retrieved and not read.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.**

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** No value range was built; the Step 0 yields are arithmetic, headed COMPUTATION — NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts seen, not weighed: debt outstanding $57.3B at 2026-06-30 against cash of $14.0B (release); $4.0B
of new senior notes sold in February 2026 (8-K `0001193125-26-059490`); a material cybersecurity incident with
exfiltrated "patient protected health information", the investigation "ongoing" (8-K `0000318154-26-000119`).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.** What the draft has the buyer do: nothing. Outside the circle the stop costs nothing the speakers count
**[M2018-087]**; inaction is the default **[M1996-006]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED** (optional; not asked).

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**. Amgen's ten-year earning power depends on which molecules now in Phase 3
succeed and on drug prices the US government and payers have not yet set; the 10-K itself calls the first "highly
uncertain" and the second "difficult to predict", so the insiders would not write the forecast down **[M2000-105]**,
**[L1993-023]**. Q7 was not reached; no range is stated. Price $402.98 (aggregator), 540.632M shares
(`0000318154-26-000126`), market cap about $217,864M, sovereign 5.66%. The closed box: no research file is opened, and a
lower price does not reopen it **[M2000-038]**. What would reopen it is not a price but a change in what the forecast
rests on: a ten-year cash stream carried by products whose exclusivity runs past the horizon and whose US price is
already settled, so that the forecast no longer turns on trial results and price setting still to come. Nothing in the
present filings shows that.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits `dfdcf29` (Step 0, foundations, standing rule) and `bb7768e` (Q1), then this close.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before it was written; the acceptance test's
      phantom check passes); every filing fact has its accession; no number without a row or a filing (the arithmetic is
      in `calc.py`).
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance, and the facts
      recorded under Q3, Q4 and Q9 are marked as not weighed.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): OCF less stock pay less capex, with
      the D&A basis and the after-acquisitions basis beside it; the sovereign from the US Treasury; the price flagged as
      an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: the 2025 growth record, **[M1999-043]**, and the
      cybersecurity 8-K's no-impact statement, in the foundations, and weighed in Q1.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): this run is dated today; not a
      point-in-time test.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its yield, growth-assumed and points-over lines
      were not used, and its 2023 stock-pay figure was replaced by the filed one.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **[M1999-075]**, the one row that names pharmaceuticals, is listed in Q1's "What it rules OUT", while the paragraph
"Sent to TOO HARD, not OUT" and the routing rule send businesses whose economics depend on fast-moving technology to TOO
HARD, and section I defines OUT as a question answered against the name. The row's own reason is dependence ("quite
dependent on the technology continuing to gallop"), not a finding that the business is bad, and **[M1999-043]** says the
industry did very well; so this run closed TOO HARD (NATURE), not OUT. Two analysts could close the same drug company
either way from the list as written; the list item wants either moving to the TOO HARD paragraph or a note saying which
box it fills. (2) The framework has no stated treatment for a business whose reinvestment to stand still is the purchase
of other companies' products: the Q7 CONVENTION deducts "all capital spending", and it is not said whether payments for
businesses acquired are capital spending. Here the choice moves the five-year mean from $8,164M to $1,482M. Not decided,
since Q7 was not reached; recorded in Step 0 with both bases. (3) Tool defects, reported and not fixed: `tools/run.py`
took FY2023 stock pay from `AllocatedShareBasedCompensationExpense` (473) where the filed cash-flow statement and the
`ShareBasedCompensation` element give 431; and its owner-earnings header still says "mean of 3 years [...] maintenance
capex" (a v4 construction) while the v5 CONVENTION asks for five years; the five-year means appear only as "THE OTHER
WINDOW" (8,156 capex basis, carrying the 473), with no per-year lines, so the five-year table was rebuilt from
companyfacts.
