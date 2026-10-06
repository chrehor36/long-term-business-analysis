# Company Run — Johnson & Johnson (NYSE: JNJ) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run from the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Every judgment cites a v5
ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Research folder: `Test Runs/_research 2026-10-06 JNJ/` (the `tools/run.py` output, the
EDGAR fetch script, the owner-cash arithmetic script and its output; raw filings under `cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the queue register, the prepped reading list and `tools/alerts.json` were not opened,
and no attempt was made to learn whether the operator holds this name.

**CONTAMINATION, declared.** (1) My training memory carries a prior about Johnson & Johnson: a long dividend record, a
AAA credit rating, the talc litigation, the Kenvue separation, and that Berkshire once owned the shares. Every fact below
is taken from the filings, not from that memory. (2) Searching the v5 ledger for this industry turned up one row that
names the company, **[M2009-016]** (Munger on decentralised models "like Johnson & Johnson"); it bears on Q5, which this
run does not reach, and it is recorded here so that a reader can judge whether it leaned on anything. (3) The repository's
listing of other run files dated 2026-10-05 was seen when the template was copied; one file (ETN) was opened for form
only. No earlier JNJ run file or research folder was opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $252.93 (2026-10-05, live quote via `tools/run.py`; **aggregator, flagged** per operator rule 5, used for
  the quote only).
- **Shares:** one class of common stock. `python Screens/cover_shares.py JNJ`: **2,409,898,597** shares, from the cover of
  the 10-Q for the quarter ended 2026-06-28, filed 2026-07-23, accession `0000200406-26-000153` (the dei cover count is
  as of 2026-07-17). Single class, so no charter note to read before adding classes.
- **Market cap:** $252.93 × 2,409.899M = **$609.5B** (`owner_cash.py` in the research folder prints $609,536M).
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 2026-10-05 (`python tools/sources.py`, the issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (fiscal year ended 2025-12-28), filed 2026-02-11, accession
  `0000200406-26-000016` (Item 1 Business, including Patents and the regulation paragraphs on the IRA and the January 2026
  agreement with the U.S. Administration; Item 1A Risk factors; Item 7 MD&A, the sales by product and franchise, R&D and
  segment income; the consolidated statement of cash flows). 10-Q for the quarter ended 2026-06-28, accession
  `0000200406-26-000153` (sales, segment income, Note 11 on talc, liquidity). 8-K of 2026-07-28, accession
  `0000200406-26-000155`, EX-99.1 (the proposed resolution of the ovarian talc litigation); 8-K of 2026-07-29,
  `0000200406-26-000163`, EX-99.1 (Firefly Bio acquired for $1 billion in cash); 8-K of 2026-08-04,
  `0000200406-26-000167`, EX-99.1 (the head of Innovative Medicine to retire). The Q2 2026 earnings release (8-K of
  2026-07-15, `0000200406-26-000146`, EX-99.1 and EX-99.2) and the proxy (DEF 14A filed 2026-03-11,
  `0000200406-26-000063`) were fetched; they are the evidence for Q4's non-GAAP habits and for Q5 and Q6, which this run
  does not reach (see Q1), so they were not read for judgment.
- **One figure cross-checked against the filed statement:** operating cash flow FY2025, **$24,530M** in the XBRL facts
  (`tools/run.py`) and **$24,530M** on the filed Consolidated Statement of Cash Flows (10-K FY2025, page 47). Agrees. The
  same statement shows a **tool defect**: `tools/run.py` took stock pay for 2024 and 2025 from the tag
  `AllocatedShareBasedCompensationExpense` ($1,200M and $1,400M); the filed cash-flow line "Stock based compensation" reads
  **$1,176M and $1,354M**. The filed figures are used below.
- **`tools/run.py JNJ`, arithmetic lines only** (Part VII; the tool's v4 wording and floor were ignored); output saved as
  `run_py_output.txt`.

**COMPUTATION — NOT A CLEARANCE** (operator rule 3; arithmetic made before Q1 to Q4 closed, carrying no entry language).
Owner cash after every real cost, from the filed cash-flow statements (USD millions; `owner_cash.py`):

| year | OCF | stock pay | capex | owner cash | acquisitions, net of cash | acquired IPR&D and milestones | owner cash after both |
|---|---|---|---|---|---|---|---|
| 2023 | 22,791 | 1,162 | 4,543 | **17,086** | 0 | 470 | 16,616 |
| 2024 | 24,266 | 1,176 | 4,424 | **18,666** | 15,146 | 1,783 | 1,737 |
| 2025 | 24,530 | 1,354 | 4,832 | **18,344** | 17,541 | 385 | 418 |
| three-year mean | | | | **18,032** | | | 6,257 |

The three-year mean is $7.48 a share, a 2.96% yield on the market cap against a 5.66% sovereign; after the purchased
pipeline (Shockwave in 2024, Intra-Cellular in 2025, the acquired in-process research), $2.60 a share and 1.03%. 2023 is
not recast for Kenvue, which left in August 2023 (10-K, cash-flow statement footnote: "Amounts presented for 2023 have not
been recast to exclude discontinued operations"), so a five-year window would mix in the consumer business; the three
years are shown and no five-year figure is used. Depreciation and amortization were $7,503M in 2025, against capex of
$4,832M; most of the gap is amortization of acquired intangibles, whose treatment is a Q4 question this run does not
reach. Whether buying the pipeline is a cost of standing still is the question the right-hand columns pose; it belongs to
Q3 and Q4 and is not answered here.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**: the question is what the business will produce, and for this business that turns
on what its laboratories and its acquisitions produce, which Q1 takes up. No macro forecast enters **[M2000-094]**: the
pricing law, tariffs and the "agreement with the U.S. Administration" of January 2026 are read below only as facts about
the business's freedom to price, not as forecasts. The market serves and does not instruct **[M2006-077]**: nothing about
the quote is evidence here. Who is paid to tell you **[M2020-037]**: the July 2026 talc release is written by the company's
litigation chief and calls the claims "junk science"; it is the defendant's account and is read as such.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the speakers called missing the drug industry in 1993 a
mistake, "we did blow it" **[M1999-043]**, and said its future was easier to predict than technology's, with "a far, far
better record of returns on large amounts of equity over time" **[M2001-002]**; (b) the 10-K gives a ten-year compound
sales growth of 5.2% (10-K FY2025, MD&A), so the company has replaced lost exclusivity before; (c) the speakers praised the
company's decentralised model by name **[M2009-016]**; (d) health care is an industry whose incumbents resist change, which
the speakers learned at their own cost **[M2021-053]**, **[M2025-056]**; that stability favours incumbents. Each of these is
weighed at Q1.

## THE STANDING RULE
Bought for cash, unlevered, at a size the buyer can hold through a fall of half, a share of Johnson & Johnson puts the
buyer at no risk of ruin; the rule binds the buyer's financing and sizing, and borrowing to buy is ruled out
**[L2014-005]**, **[M2012-081]**. The target's own debt ($49.0B of notes payable and long-term debt at 2026-06-28, 10-Q)
and the talc commitment are the target's, weighed at Q9, which this run does not reach.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**; the product can be
understood while the economics are not **[M2000-104]**. Johnson & Johnson is two businesses (10-K, Item 1, "two business
segments"), so the holding-company convention applies: the whole is understood only if each part that matters is
**[M2002-092]**.

**Which part matters.** Innovative Medicine (prescription drugs) was $60.4B of $94.2B of 2025 sales and **$22,266M of the
$26,379M of segment income before tax, 84%** (10-K FY2025, Note 17). MedTech was $33.8B of sales and $4,113M of segment
income, 16%. The ten-year question is therefore first a question about the drug segment.

**The key variables and how predictable they are** **[M1998-044]**. From the filings:
1. *Exclusivity.* The largest product, DARZALEX, was about 15.0% of 2025 revenues; the two Genmab patent families "both
   expire in the United States in 2029" (FASPRO and IV have separate Janssen portfolios whose dates the 10-K does not
   give). STELARA, the second, fell 41.3% in 2025 to biosimilars. TREMFYA, the third, has a composition patent "projected to
   expire in the United States in 2031". The 10-K also expects "generic competition for OPSUMIT in 2026" and SIMPONI
   biosimilars, and ERLEADA is on the government's 2028 selected-drug list (10-K, Item 1 and MD&A). Those six products were
   $34.2B of 2025 sales, 36% of the company and 57% of the drug segment, each with an exclusivity or government-pricing event
   that the filing itself dates inside the ten years. So the drug segment's 2036 earning power rests mostly on products
   that are not yet approved, or not yet owned.
2. *What replaces them.* The company says it in its own words: "Only a very few biopharmaceutical research and development
   programs result in commercially viable products", and "The Company cannot be certain when or whether it will be able to
   develop, license or otherwise acquire companies, products and technologies, whether particular product candidates will
   be granted regulatory approval, and, if approved, whether the products will be commercially successful" (10-K, Item 1A).
   "New products introduced within the past five years accounted for approximately 25% of 2025 sales" (same). The
   replacement is bought as well as discovered: $15.1B of acquisitions in 2024, $17.5B in 2025, and Firefly Bio for $1B
   in July 2026 (cash-flow statement; 8-K `0000200406-26-000163`).
3. *Price.* The government now sets prices for selected drugs under the IRA (10-K, Item 1); the company sued and has sought
   Supreme Court review; in January 2026 it "reached an agreement with the U.S. Administration to improve access to
   medicines and lower costs for U.S. patients", and it expects "additional regulations, including models or other
   mechanisms to increase pricing controls" (same). 2025 sales growth was volume 8.4% and **price minus 3.1%** (10-K, MD&A).

**Applying the tests.**
- *Would the insiders write it down* **[M2000-105]**? They decline to, in the passage quoted under variable 2: which
  candidates will be approved and succeed is the thing the company says it cannot be certain of. That is the industry's own
  insiders, in their filed risk factors, declining the ten-year forecast.
- *Can I name the winner, not just the industry* **[M2012-067]**? The speakers asked exactly this of this industry, and
  answered it for the single company: "it’s easy for me to figure out that Coca-Cola’s the soft drink company to be in [...]
  than it is for me to figure out which one in the pharmaceutical" **[M1997-119]**; "It would not have been within our circle
  of competence to try and pick a single company" **[M1998-073]**; "I do think it’s very hard to pick out the winner"
  **[M1999-044]**; "We would not have great insights on specific companies" **[M2002-060]**.
- *Does it live on continued invention* **[M1999-075]**? "Take pharmaceuticals, if they had never invented any more
  pharmaceuticals, it would be a terrible business." The filing's own sentence that new products "offset revenue losses
  when the Company’s existing products lose market share due to [...] loss of patent exclusivity" (10-K, Item 1A) is the
  same fact from the inside.
- *Is the deciding variable important and knowable* **[M2006-076]**? Pipeline success is important and, by the company's
  account, unknowable product by product. Price is important and "much of it is in the political realm. And my judgment
  about the — what politicians will do is probably not better than yours." **[M2005-098]**; Munger in the same answer: "We
  just throw some decisions into the “too hard” pile and go on to others." **[M2005-099]**. In 2026 the political variable
  is live, in the IRA list, the lawsuit and the January agreement above.
- *MedTech, the other part.* Its 2025 segment margin was 12.2% before tax (10-K, MD&A); Electrophysiology growth was
  "partially offset by competitive pressures in Pulsed Field Ablation catheters", a technology shift the filing names, and
  the company intends to separate Orthopaedics within 18 to 24 months of October 2025 (10-K, Item 1). A technological
  component that "could hurt the business as it presently exists" does not pass the filter **[M1998-008]**. The MedTech
  part is not needed to decide the box, since the drug part decides it, and it was not worked further.

**Contrary evidence, weighed** **[M1997-127]**. The strongest case for IN is the company's record and the speakers' regret:
the industry "as a whole represented a group that would achieve good returns on equity" and it "was within our circle of
competence to identify the industry as likely to enjoy very high profits over time" **[M1998-073]**; Munger found its
future "easier to predict than the future of the high-technology sector" **[M2001-002]**; and the ten-year sales growth of
5.2% shows that Johnson & Johnson has replaced lost exclusivity before. But each of those rows places the understanding
at the industry and not at the company, and prescribes the package, not the single name: "if I did buy them, I would buy
[...] a group of the leading companies" **[M1999-044]**; "we should have taken a package approach" **[M2002-060]**. The record
is past, and "You don’t get paid for what’s already happened." **[M2007-025]**. Whether a large drug company is itself a
package is the reader's question that section VI leaves open (**[M2002-060]**, **[M2010-085]** against **[M2002-092]**,
marked READER); I do not settle it in the company's favour, because "if you have doubts about something being into your
circle of competence, it isn’t" **[M2002-092]**, and the 2005 rows, later than the package rows, send the industry's future
itself to "too hard" on the political variable **[M2005-098]**, **[M2005-099]**. The stop costs nothing the speakers count
as an error here, since their own rows put the single drug company outside the circle **[M1998-073]**, **[M2001-006]**.

**Routing.** The framework lists "Businesses that live on continued invention" **[M1999-075]** among what Q1 rules OUT,
and routes a business whose ten-year economics cannot be foreseen to TOO HARD, "never OUT on the business" **[M2000-038]**,
**[M2006-013]**. The rows that speak of this industry give ignorance as the reason, not a finding against the business
(the 2005 answer sits under the transcript heading "Future of pharmaceuticals is “too hard”" and ends in the "too hard"
pile **[M2005-099]**; "very hard to pick out the winner" **[M1999-044]**), and the speakers call the industry good. So
the box is TOO HARD, and the OUT listing of **[M1999-075]** is reported below as a framework ambiguity.

**Cause.** NATURE, not WORK: the deciding questions are which compounds succeed and what governments will let them be
priced at, and the company's own insiders decline to write the first down while the speakers say their judgment of the
second "is probably not better than yours" **[M2005-098]**. More reading would not answer either: "Our problem -- which we
can't solve by studying up" **[L1999-018]**; **[L1993-023]**. A lower price does not reopen it **[M2000-038]**.

**VERDICT: TOO HARD (NATURE).** The drug segment, 84% of segment income, has exclusivity or government-pricing events
dated by its own filing inside ten years on 57% of its sales, and its 2036 earning power rests on candidates whose success
the company says it cannot foresee and on prices set in the political realm **[M2012-065]**, **[M2000-105]**,
**[M1998-073]**, **[M2005-098]**, **[M2002-092]**. The file closes here; Q2 to Q12 are NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed TOO HARD). The competitor row was therefore not filled.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED. Left for any later reader: whether the $34.9B of acquisitions and acquired research in 2024 and 2025 (Step 0)
is the price of standing still in this business is the question this section would have had to answer first.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten-year balance-sheet table is in `run_py_output.txt` and was not read for judgment; the earnings
release (EX-99.1 and EX-99.2 of `0000200406-26-000146`) was fetched and not read for judgment.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. The proxy (`0000200406-26-000063`) was fetched and not read for judgment.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range was built; the Step 0 yields are a computation, not a clearance, and carry no entry language.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found on the way, recorded for a later reader and not weighed: $49.0B of notes payable and long-term
debt against $20.8B of cash and marketable securities at 2026-06-28 (10-Q `0000200406-26-000153`); a talc reserve of
about $3.7B at the same date (10-Q, Note 11); and the proposed ovarian talc resolution of 2026-07-27, "a $5.5 billion
commitment by the Company", conditioned on participation of at least 95% of the remaining claims (8-K
`0000200406-26-000155`, EX-99.1).

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. What the draft would have the buyer do: nothing; a TOO HARD name is not a pitch **[M2006-013]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**. The drug segment that earns 84% of segment income faces exclusivity or
government-pricing events, dated by its own filing inside ten years, on 57% of its sales, and its 2036 earning power rests
on which candidates succeed, which the company says it cannot foresee, and on prices set in the political realm
**[M2000-105]**, **[M2005-098]**. The speakers placed the single drug company outside their circle and the industry, if
anywhere, inside it as a package **[M1998-073]**, **[M1999-044]**, **[M2002-060]**. Q7 was not reached; no range is
written beside the price of $252.93.

**What would reverse it.** No price does **[M2000-038]**. The rows name one different purchase, a group of the leading
drug companies bought as a package at a below-market multiple **[M1999-043]**, **[M2002-060]**; that is a separate run of a
separate thing, not a reopening of this one.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits for Step 0 and for Q1, then this close.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv`); every filing fact has its accession; no number
      without a row or a filing. The derived shares (84%, 57%, 36%) are computed from 10-K figures in the text.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): OCF less filed stock pay less all
      capital spending, from the filed cash-flow statement; the sovereign from the US Treasury; the price quote flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (Foundations, items a to d; weighed in Q1).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the rows cited
      run 1993 to 2025.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its stock-pay tag was corrected from the filed
      statement.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 names this industry under OUT and the routing sends it to TOO HARD.** "Businesses that live on continued
invention", quoting the pharmaceutical row **[M1999-075]**, stands first in Q1's "What it rules OUT" list, while the
routing paragraph sends a business whose ten-year economics cannot be foreseen to TOO HARD, "never OUT on the business",
and the speakers' other rows on this industry give ignorance, not a finding against it, as the reason (**[M1998-073]**,
**[M2005-099]**), and call it a good industry (**[M1999-043]**, **[M2001-002]**). Two analysts could close the same drug
company OUT or TOO HARD at choice. I chose TOO HARD on the reason the rows give; the framework should say which governs
when **[M1999-075]** is the deciding row. (2) **The package door is open and unsized.** Section VI carries the basket rows
(**[M2002-060]**, **[M2010-085]**) against the doubt rule (**[M2002-092]**) as READER, but gives no test for when one large
diversified company counts as a package of an industry; for a drug company with dozens of products the question is real,
and I resolved it by the doubt rule and the single-company row **[M1998-073]**. (3) **Purchased pipeline in owner cash.**
Q4 and the Q7 convention say "all capital spending" but are silent on whether acquisitions that replace expiring products
are capital spending; here they move the three-year owner-cash mean from $18.0B to $6.3B. Not decided, since Q3 and Q4
were not reached. **Tool defects:** `tools/run.py` took stock pay for 2024 and 2025 from the XBRL tag
`AllocatedShareBasedCompensationExpense` ($1,200M, $1,400M) where the filed cash-flow line reads $1,176M and $1,354M; and it
offers a five-year window that mixes in the Kenvue consumer business for 2021 to 2023 without a flag.
