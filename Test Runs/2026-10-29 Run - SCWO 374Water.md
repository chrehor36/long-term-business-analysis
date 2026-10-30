# Company Run — 374Water Inc. (Nasdaq: SCWO) — 2026-10-29
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (2026-10-29), after the run was committed: not held (`PORTFOLIO.md` does not name SCWO, 374Water or PowerVerde).

*Dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the two departures the brief states (the repository
path is now C:\Projects\BRK; the lines of evidence and the competitors are derived by the analyst from the 10-K, not
supplied). Working folder: `Test Runs/_research 2026-10-29 SCWO/` (notes, ledger rows used, the computation script and its
output; raw filings in its ignored cache).*

**Contamination, declared.** (1) The git log shown at session start carried the subjects of another company's v5 run of
today (TURV, "OUT at Q1, a start-up in substance"). It is about a different company; it is declared and not used, and this
run's Q1 is decided on 374Water's own filings. (2) Before re-reading the blind rule I ran one filtered listing of
`Test Runs/` for file names containing "scwo", "374", "powerverde" or "vyrex"; it returned no lines, so nothing was seen,
but the listing itself is a breach of the letter of the rule and is declared here. (3) The memory index loaded with the
session names queue and wave states in general terms; none of it names this company. Nothing else from the blind-listed
files was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $2.53 (2026-10-29, live quote via `tools/run.py`; **aggregator, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: 17,718,161 common, single class (10-Q for the quarter to 2026-06-30,
  filed 2026-08-14, accession `0001654954-26-007650`; `python Screens/cover_shares.py SCWO`, cover as of 2026-08-10). Checked
  against the balance sheet of the same 10-Q: 17,718,161 shares outstanding at 2026-06-30, no treasury shares (issued equals
  outstanding in the XBRL). The 8-K of 2026-09-30 (accession `0001654954-26-008681`) gives 17,493,924 at the 2026-07-31 record
  date, which predates the cover count's own as-of and does not contradict it. No 8-K or prospectus after the 10-Q states a
  later count. Not counted and open: sales, if any, under the $50 million at-the-market programme with Robert's & Ryan of
  2026-08-10 (424B5, accession `0001654954-26-007452`); conversion of $3,020,000 of 10% convertible notes at $3.00 (about
  1.0 million shares) and the warrants attached to them (10-Q Note 5 and Note 11). The 1-for-10 reverse split took effect
  2025-12-26; every per-share and share figure from FY2025 on is post-split, earlier XBRL cover counts are pre-split
  (126,680,895 in March 2022; 169,248,799 in November 2025, about 16.9 million post-split).
- **Market cap:** $44.8M (2.53 x 17,718,161).
- **Sovereign for the earnings currency:** 5.37%, US Treasury daily par yield curve, 30-year, 2026-10-28 (issuing authority;
  `tools/run.py` sovereign line).
- **Filings read** (operator rule 4): 10-K for FY2025, filed 2026-03-31, accession `0001654954-26-003094` (Items 1, 1A, 7, 9A,
  the auditor's report, Notes 3 and the cash-flow statement); 10-K/A, filed 2026-04-30, accession `0001654954-26-004179`
  (Part III only, by its own explanatory note); 10-Q to 2026-06-30, accession `0001654954-26-007650` (balance sheet, Notes 3,
  5, 9 and 11, MD&A); 10-Q to 2026-03-31, accession `0001654954-26-004903` (fetched, scanned); DEF 14A filed 2026-08-25,
  accession `0001654954-26-007870` (summary compensation table); 8-Ks of 2026-10-29 (`0001654954-26-009210`, Reg FD, an
  investor presentation), 2026-09-30 (`0001654954-26-008681`, charter amendment and annual-meeting votes), 2026-08-18 and
  2026-08-11 (`0001654954-26-007728`, `0001654954-26-007472`, results releases), 2025-12-15 (`0001193125-25-318380`, the
  letter agreement with Mr. Nagar); 424B5 of 2026-08-11 (`0001654954-26-007452`). **One figure cross-checked against the filed
  statement:** net cash used in operating activities for FY2025, $(14,326,205) in the filed cash-flow statement and in
  Note 3 of the 10-K, against $-14.3M in `tools/run.py`'s OCF column: agrees.
- `python tools/run.py SCWO` arithmetic lines only: OCF $-9.0M, $-10.6M, $-14.3M (FY2023 to FY2025); SBC $0.9M, $1.2M, $3.5M;
  capex $0.1M, $0.6M, $1.9M; owner cash (capex basis) $-10.1M, $-12.4M, $-19.8M. Checked against the filed statements and
  completed (see Q7 COMPUTATION below): the tool omits "Issuance of common stock for services" ($71,200, $383,879, $290,872 in
  FY2023 to FY2025), which is stock pay and is deducted here, and FY2024's $98,602 of intangible spending. Owner cash after
  every real cost, five years: FY2021 $-2.05M, FY2022 $-5.70M, FY2023 $-10.14M, FY2024 $-12.84M, FY2025 $-20.06M; average
  $-10.16M. Negative in every year, and growing more negative.
- **The lines of evidence chosen from the 10-K, and why.** From Item 1: the stage of the business (revenue sources, the
  Orlando hub, the OC San and Olathe contracts, the product road map), because Q1 asks whether the ten-year economics can be
  foreseen at all; the competition paragraph, for Q2's rival set. From Item 1A: "limited operating history with no material
  revenues", going concern and financing, material weaknesses, competition and patents, because each bears on whether the
  business exists yet as an earning business. From Item 7: revenue and its make-up, the cost lines, liquidity and the
  at-the-market programmes, because they show what the business earns and how it is funded.
- **The balance sheets first, ten year-ends** (`tools/run.py` table from first-filed XBRL, read against the filed FY2025 and
  June 2026 statements; read here because the file closes before Q4) **[M2025-032]**. FY2016 to FY2020 are the PowerVerde
  shell: total assets $37K to $509K, equity negative in three of five years. FY2021 is the reverse merger with private
  374Water (April 2021): assets jump to $12.4M, almost all cash ($11.1M) from issuance. From FY2021 to FY2025 the accumulated
  deficit goes from $-3.2M to $-49.9M ($-57.2M at 2026-06-30); equity rises only when shares are sold ($14.7M at FY2023, $15.5M
  at FY2024) and falls to $6.7M at FY2025 as cash runs down to $3.2M; it is $3.0M at 2026-06-30 with cash of $1.78M. Inventory
  of $1.5M to $2.3M from FY2022 and receivables of up to $0.7M are against revenue of $0.2M to $3.0M a year. Debt is nil until
  FY2025; at 2026-06-30 it is $2.96M of 10% convertible notes due 2029 (carried at $2.74M net of discount) plus small notes,
  against $2.55M of long-term unearned revenue (a customer deposit). What the figures say: a company funded by its owners'
  new money, whose retained earnings have only ever gone down. What they cannot say: what the business will earn, since it
  has never earned.

## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. Here the
business has no earnings to own through a closed market; its survival over the next twelve months depends on selling more
shares into the open one (the going-concern paragraphs below), so the price is not a servant here but the company's main
source of cash **[M2006-077]**. Who is paid to tell you: the 10-K's market sizes ($347 billion municipal, $15 billion
federal, $144.5 billion industrial) are third-party estimates the company says it has "not independently verified" (10-K
`0001654954-26-003094`, Industry and Market Data); they describe the field, not this company's share of it. **Contrary
evidence, written down as found** **[M1997-127]**: the business case for the company is real in one respect: there is
filed, paying demand (the OC San equipment contract, revenue of $2.26M recognised in Q2 2026 after a factory acceptance test;
the Olathe sale with $2.55M of deposits; DoD demonstrations; the City of Orlando hub), and the half-year loss narrowed to
$7.27M from $8.28M with operating cash use down to $2.30M from $7.62M (10-Q `0001654954-26-007650`). This is written down
because it is the strongest evidence against the stop below; it is evidence of a product finding first customers, not of
an earning business.

## THE STANDING RULE
The buyer's own conduct: a cash purchase of a part-interest, with no borrowed money and no position that can be called,
does not put the buyer at risk of ruin **[M2012-081]**, **[L2014-024]**; the size of any purchase is the buyer's to cap. The
target's own going-concern doubt is a fact about the business, weighed (if reached) at Q9, not a breach of this rule. Passes.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable probability of being able to asses where the business will be in 10 years"
  **[M2000-037]**, a fix on "what the earning power and competitive position will look like in five or 10 years"
  **[M2012-065]**. The product can be understood (supercritical water oxidation destroys organic waste, PFAS among it), and
  that is not the test: "We understand what it does for people. We just don’t know the economics of it 10 years from now."
  **[M2000-104]**.
- **The filing facts.** 374Water's own 10-K (`0001654954-26-003094`) says: "We have a limited operating history with no
  material revenues"; "We have yet to generate material revenues from our business. Therefore, the commercial value of our
  systems is uncertain. There can be no assurance that we will ever generate significant revenues or become profitable";
  and "we are subject to all the risks inherent in a new business". Revenue was $215,037 in FY2025 and $445,445 in FY2024,
  against a net loss of $20,975,052 and operating cash use of $14,326,205 in FY2025. The auditor's report carries a going-concern
  paragraph ("recurring losses and negative cash flows from operations that raise substantial doubt"), and management states
  it does "not have sufficient cash resources to meet our plans for the next twelve months". The road map is to scale the
  systems "to 20+, 30+, and 50+ tons per day in the near- to mid-term" from the present six to ten tons a day; two
  commercial-scale AS systems exist (one at Orlando, one for OC San). The patent position is applications: four pending US
  non-provisional, six provisional, three PCT; the core technology is licensed from Duke (Item 1). The present company is the
  2021 reverse merger of private 374Water into the PowerVerde shell. Owner cash after every real cost has been negative in every
  year on record and more negative each year (Step 0).
- **The key variables, and whether they are foreseeable.** The variables are the price per ton the customers will pay, the
  cost to run and maintain the systems at scale, how fast the systems scale, which destruction technology wins in each market
  (the 10-K names "other SCWO technology providers, other emerging technology providers (e.g., plasma and electrochemical
  oxidation), as well as anaerobic digestion, landfilling, drying and incineration"), and the PFAS rules and federal budgets
  that set demand. None has a record yet: there is no year of earnings from which "the financial statements will tell me the
  information that’s useful to me in making a judgment about what the future financial statements are going to look like"
  **[M2008-033]** (Q1 test 3), and no installed base at scale to read a unit cost from.
- **Routing.** Two routes are open in the text, and the filings decide which. Q1 lists start-ups among what it rules OUT:
  "Start-ups are not our game." **[L2007-015]**; "We don’t do startups." **[M2008-088]**. Fast-moving technology goes to TOO HARD
  instead **[M1998-008]**, **[L1993-023]**. This company is a start-up in substance by its own description ("all the risks
  inherent in a new business", no material revenue, funded by share sales, going-concern doubt), so the ruled-OUT item
  applies on the filing's own words. The technology route points the same way (a new process with "a technological component
  that’s of significance" **[M1998-008]**) and is recorded, not used to decide the box; see the framework section below for
  the overlap. A TOO HARD (WORK) would mean the deciding question is knowable and the work not done; here there is no
  earnings record to research, and more study would not supply one **[M2008-086]**.
- **VERDICT: OUT** at Q1: a start-up in substance on its own 10-K, "Start-ups are not our game." **[L2007-015]**,
  **[M2008-088]**; no fix on its ten-year earning power is possible because it has none yet **[M2000-037]**, **[M2012-065]**.
  The box is the rows' "out" **[M2006-013]**, not a judgment that the technology fails.

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (closed at Q1).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED.
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED.

## Q7 — WHAT IS IT WORTH? NOT REACHED as a question. The reporting figures follow as a computation.

**COMPUTATION, NOT A CLEARANCE** (operator rule 3; the owner's price, Part VII). No entry language; nothing here reopens Q1.
- **Owner cash after every real cost** (OCF less stock-based compensation, less common stock issued for services, less
  capital spending and intangible spending; from the filed cash-flow statements, accessions `0001654954-22-002303`,
  `0001654954-23-003036`, `0001654954-24-003957`, `0001654954-25-003443`, `0001654954-26-003094`): FY2021 $-2,046,357;
  FY2022 $-5,704,304; FY2023 $-10,137,358; FY2024 $-12,842,782; FY2025 $-20,061,935. Five-year average $-10,158,547. Stock
  issued for services is not tagged for FY2021 and FY2022 and is read as nil there, said so. Script and output:
  `Test Runs/_research 2026-10-29 SCWO/computation.py`, `computation_output.txt`.
- **The range, by Q7's convention in full.** The four PG specifics: growth on aggregate owner cash (here meaningless, below);
  all spending deducted (above; the depreciation variant is no better, D&A of $0.75M in FY2025 against capex of $1.90M); zero
  growth after year ten; a price above the top closes OUT. The six more: (a) no year is a cyclical peak or trough on the
  filer's description; the window is a ramp from a shell, every year negative; (b) the series is negative throughout, so a
  compound rate between end years is meaningless; between the halves (FY2021 to FY2022 average $-3.88M, FY2024 to FY2025
  average $-16.45M) it is also meaningless, both being negative, so **the range is the no-growth case alone, said so**;
  (c) no acquisitions paid in cash in the window; the 2021 reverse merger was paid in shares and the combined company is the
  only filer, so the window is already on the combined record; (d) working capital is inside OCF as filed; (e) the filing
  gives no maintenance guess for a business with no steady state, so the all-spending case is the only case; (f) no cap is
  reached, the shown growth being of losses. The floor tested first: no case earns the floor at any positive price, since
  every case values the business below zero. The literal window shown beside is the same five years.
- **Value range (the no-growth case alone):** whole business $-189.2M at 5.37%, less net debt of $1.29M at 2026-06-30
  (convertible notes $2,960,000 principal, the July 2026 note $60,000, notes payable $39,125, financing liability $10,159,
  less cash $1,776,259; operating leases left out, said so) = **$-10.75 a share**, against a price of $2.53. Not positive.
- **Fair price (a reporting figure, never a verdict; Part VII):** the no-growth case valued at ten percent, the only end
  case, so the average is that case: $-101.6M, less net debt = **$-5.81 a share on the all-equity basis (central)**;
  equity-only beside it (owner cash after interest, interest in the window nil) **$-5.73 a share**. Not positive: no price
  earns the floor. Company tax: none paid in the window; no carryforward is credited, since no profit to shelter is in view.
  Growth spending (above maintenance): not separable, none charged separately. Utility debt credit: not applicable.
- **Close the computation would give:** OUT on the floor, tested first **[M2003-149]**; and the deeper reason is Q7's first
  stop, the stream cannot be pictured **[M1994-077]**, so the negative figures describe the past, not a value.

## Q8 — Q10, Q12 — NOT REACHED.

---
## THE BOX
**OUT at Q1** (a start-up in substance on its own 10-K: no material revenue, going-concern doubt, owner cash negative in every
year, **[L2007-015]**, **[M2008-088]**). COMPUTATION beside it: value range $-10.75 a share (no-growth case alone) against
$2.53; fair price not positive ($-5.81 all-equity, $-5.73 equity-only). **Integrity facts recorded, not judged** (see Q5 below).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.
- **Q2 (castle; competitors).** The 10-K (`0001654954-26-003094`, Item 1 Competition and Item 1A) names **no rival by name**:
  "We compete with other SCWO technology providers, other emerging technology providers (e.g., plasma and electrochemical
  oxidation), as well as anaerobic digestion, landfilling, drying and incineration, lagoon and spray-fields, lime
  stabilization, and others", and "We believe many of our competitors and potential competitors have significant competitive
  advantages, including longer operating histories [...] greater financial, research and development, marketing,
  distribution, and other resources than we do". So no SEC-filing rival could be taken from the 10-K, and no comparison set
  was chosen, Q2 not being reached. Patents: applications only, none issued stated as of 2025-12-31; core technology
  licensed from Duke University (2021) with royalties on sales. "We compete primarily based on our product offering, quality
  of service and price."
- **Q3 (capital).** Capital spending rose from $0.1M (FY2023) to $1.9M (FY2025) while revenue fell; the WDS model puts the
  company's own systems at partner sites.
- **Q4 (accounts).** Material weaknesses in internal control over financial reporting at 2025-12-31; disclosure controls not
  effective (Item 9A). FY2025 equipment revenue was negative, $(1,653,007), after the OC San variable consideration was
  "fully constrained" for delivery delays; $2.0M of it was recognised again in Q2 2026 after a factory acceptance test. An
  accrued contract-loss provision of $1.6M stands at 2026-06-30. Item 7 describes the November 2024 offering as 978,350 shares
  at "$1.25" for one share and 1.5 warrants, with gross proceeds of $12.2 million: the share count is post-split and the price
  pre-split in the same sentence, an internal inconsistency in a filed document.
- **Q5 (people), integrity facts.** CFO Russell Kline terminated effective 2026-03-02; on 2026-07-10 he served a demand and
  draft complaint for at least $433,500 of severance, bonus and statutory damages (10-Q Note 11). CEO turnover: Christian
  Gannon (2024 to 2025), Stephen Jones (interim, 2025), Danny Bogar (signing 8-Ks in 2026). A letter agreement of 2025-12-14 with
  Mr. Yaacov (Kobe) Nagar, co-developer of the technology, replaced three directors with mutually acceptable candidates
  (8-K `0001193125-25-318380`), amended 2026-02-07. On 2026-05-26 the company modified its 10% convertible notes, cutting the
  conversion price from $5.00 to $3.00 and the warrant price from $7.50 to $4.50; $700,000 of the notes are held by three
  non-employee directors, and the change was booked as a $1.02M loss on extinguishment (10-Q Note 5 and Part II Item 2). A
  stockholder class action (Delaware Chancery, 2026-03-18) sought to invalidate the charter's exculpation clause; the charter
  was amended on 2026-09-30 to conform it to DGCL 102(b)(7) (8-K `0001654954-26-008681`). These bear on **[M2013-088]** if the
  name is ever run to Q5.
- **Q6 (money and owners).** Share issuance is the funding: at-the-market programmes of $15.1M (Lake Street, 2025), $50M
  (Lake Street, December 2025) and $50M (Robert's & Ryan, August 2026); a registered direct offering with 1.5 warrants a share
  in November 2024; convertible notes with full warrant coverage in 2026. Shares outstanding rose from 126.7M pre-split
  (March 2022, about 12.7M post-split) to 17.7M post-split (August 2026), about forty percent, before the convertibles and
  warrants **[L2014-015]** (weighed at Q6 if reached). CEO total pay in the proxy (`0001654954-26-007870`): $7,508,321 in 2024,
  $1,271,875 in 2025, against revenue of $445,445 and $215,037.
- **Q9 (ruin).** Cash $1,776,259 at 2026-06-30 against half-year operating cash use of $2,297,376; interest on the notes due
  semi-annually from 2026-09-30; the "baby shelf" rule limits S-3 sales to a third of a public float of about $27M (424B5).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Commits:
      template and framework notes; Step 0 to Q1 and the closing sections (the file closed at Q1).
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (the lock file was present in `Screens/_daily/` when the run began); the fold is the dispatcher's.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched: **not fully kept.** One filtered
      listing of `Test Runs/` by this company's names was run at the start and returned nothing; declared under
      contamination above. No other blind-listed file was opened.
- [x] Every v5 id resolves (checked by `check_ids.py` in the research folder); every filing fact has its accession; no
      number without a row or a filing.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; aggregator quote flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]**; facts for later questions are under AFTER THE STOP,
      with the integrity flag in the box line.
- [x] No row dated after the anchor is cited (not a point-in-time run).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); two of its lines were completed from the filing.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Q1 carries a start-up in two places that point to different boxes: "What it rules OUT" lists start-ups (**[L2007-015]**,
**[M2008-088]**), while a business with "a technological component that’s of significance" is sent to TOO HARD
(**[M1998-008]**, "Sent to TOO HARD, not OUT"). A pre-revenue company commercialising a new destruction technology is both,
and the text does not say which governs when both fit. This run took the start-up item, because the company's own filing
describes itself in start-up terms and the rows on start-ups refuse the category outright, while the technology rows give
ignorance of the economics as the reason; a sentence saying that a business with no earnings record closes OUT as a start-up
whatever its technology would settle it. Second, Q7's specific (b) ends in "the range is the no-growth case alone" for a
series that is negative throughout; the fair-price definition then asks for "the average of the two" end cases where there is
one, and gives no wording for a fair price that is not positive. This run reported the one case and said "not positive";
the brief's reporting figures assume a positive number. Third, `tools/run.py` omits "issuance of common stock for services"
from its stock-pay columns for this filer and reports a three-year mean beside a five-year one; both were completed by hand.
