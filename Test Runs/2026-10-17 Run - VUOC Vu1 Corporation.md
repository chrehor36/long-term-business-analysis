# Company Run — Vu1 Corporation (formerly OTC Bulletin Board: VUOC; registration revoked 2023-03-10) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (902833f2): `PORTFOLIO.md` read for this one ticker; the operator does not hold VUOC (no line names VUOC, Vu1 or Telegen).*

**Dispatched run.** Written by a dispatched analyst under the brief of 2026-10-17, which states one departure from the
canonical brief (`Screens/_daily/_dispatch_brief.md`): the lines of evidence are derived by the analyst from the 10-K's
Item 1, Item 1A and Item 7, not given in the brief. The lines chosen are stated under Step 0.

**Contamination, declared and not used.** Before any reading, the session context showed (a) the subjects of the
repository's five most recent commits, which concern a run of another company (LBYYQ) and its fold, including that run's
box and its computed figures; (b) a git status listing naming research folders of other companies (AYI, ARCB) and
dated daily digests; (c) the one-line index of the operator's memory files, which mentions queue state and a count of
gate-clearers without naming this company. None names Vu1 or VUOC; none was opened further; nothing of them is used
here. No blind-listed file was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING

**What the security is today, from the filings that can be read.** The company filed nothing periodic after the 10-Q
for the quarter ended 2015-03-31 (filed 2015-05-20, accession `0001096906-15-000592`). The Commission's opinion and order
of 2023-03-09 (Exchange Act Release No. 97085, Admin. Proc. File No. 3-20992; EDGAR form REVOKED, accession
`9999999997-23-000886`) found the company in default, deemed the order instituting proceedings true, and revoked "the
registration of all classes of the registered securities of Vu1 Corporation under Section 12(g)", effective
2023-03-10. The deemed-true allegations describe the respondent as "a suspended California corporation located in
Berkeley, California", delinquent since that 10-Q, and record that as of 2022-07-15 "unsolicited quotations" for the
common stock were on OTC Link. The last filing by anyone about the shares is an SC 13G of 2018-02-12 (accession
`0001457716-18-000099`) by Virtu Americas LLC, a broker-dealer, reporting 847,705 shares, 5.94%, computed on the share
count of the 2015 10-Q, which says only that a market maker held shares at 2017-12-29. What this means for the run:
**every figure below is ten or more years old; there are no audited statements after FY2014 and no unaudited ones after
2015-03-31; the condition of the company since then is not on any public record found.**

- **Price:** no current quote obtainable. The tool's aggregator (`tools/sources.py`, Yahoo chart) returns HTTP 404 for
  VUOC; the OTC Markets endpoints returned a maintenance page on 2026-10-17. With the registration revoked, an
  aggregator quote, if one existed, would not be a market an owner could rely on (flagged; operator rule 5). **Last
  price on a filing:** "The closing price of our common stock on April 15, 2015 was $0.62 per share" (10-K FY2014,
  Item 5, filed 2015-04-30, accession `0001096906-15-000450`). FY2014 quarterly range on the OTC Bulletin Board: high
  $1.49, low $0.46 (same Item 5).
- **Shares by class** from the latest filing's cover: 14,273,093 common shares, no par value, "issued and outstanding"
  on 2015-05-12 (10-Q for Q1 2015, cover, accession `0001096906-15-000592`); one class; preferred authorized
  10,000,000, none issued. The 10-K cover gives 14,173,093 on 2015-04-16. The balance sheet of 2015-03-31 shows
  13,973,093 issued and outstanding; no treasury shares are shown (California no-par stock). `python
  Screens/cover_shares.py VUOC` returns "NOT AN SEC REGISTRANT in the live ticker file": the ticker is gone from the SEC
  ticker map, so the count was taken from CIK 0000906448 directly. **Dilution not in the count:** the convertible
  debentures were repriced on 2015-06-04 to convert at $0.50 a share (8-K filed 2015-06-09, accession
  `0001096906-15-000628`), with interest to be paid in shares; $2,788,300 of debentures at $0.50 would be about 5.58
  million more shares, beside warrants and options (Q1 2015 10-Q, notes). Any issuance after 2015 is unknown.
- **Market cap:** not computable at a current price. At the last filed close, $0.62 × 14,273,093 = about $8.85M
  (a 2015 figure, shown for reference only, not a price for this run).
- **Sovereign for the earnings currency (USD):** 5.43%, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 10-K for FY2014 (filed 2015-04-30, `0001096906-15-000450`), Items 1, 1A, 2,
  3, 5, 7 and the statements with Notes 3, 5 and 6; the 10-Q for Q1 2015 (filed 2015-05-20, `0001096906-15-000592`);
  the 8-Ks of 2015-06-09 (`0001096906-15-000628`), 2015-07-07 (`0001096906-15-000730`) and 2015-07-31
  (`0001096906-15-000836`, with its Exhibit 99.1); the statements of the 10-Ks for FY2012 (`0001096906-13-000398`),
  FY2010 (`0001144204-11-019116`), FY2008 (`0001144204-09-017973`) and FY2007 (`0001144204-08-018332`), which carry the
  FY2006 to FY2013 comparatives; the SC 13G of 2018 and the revocation order of 2023 above. The last proxy on file is a
  DEF 14C of 2011-09-20 (`0001144204-11-053857`) and a DEF 14A of 2008-07-07 (`0001144204-08-038742`); neither was read
  for pay, since the file closes at Q1 (downloaded, in the research cache). **One figure cross-checked against the
  filed statement:** cash at 2014-12-31 of $1,903 appears in the FY2014 10-K balance sheet and again as the comparative
  column of the Q1 2015 10-Q balance sheet. One inconsistency found in the filing itself: the FY2014 balance sheet gives
  the accumulated deficit as $91,416,708 and Note 3 of the same 10-K gives $91,417,708; the 10-K's own running header
  reads "2013 ANNUAL REPORT ON FORM 10-K", and its cover states non-affiliate market value "on June 30, 2013" in a report
  for FY2014.
- **The lines of evidence this name needs** (derived from Item 1, Item 1A and Item 7 of the FY2014 10-K, as the brief
  directs): (1) whether there is a business at all: revenue, customers and going-concern status (Item 1, Item 1A first
  risk factor, Item 7 liquidity, auditor's report); (2) the technology and the field: ESL against LED, CFL and
  incandescent, and the filer's own words on the pace of change (Item 1 Overview, Competition; Item 1A); (3) the claims
  on the assets: convertible debentures, judgments and the levy on the patents, the insolvent Czech subsidiary (Item 3;
  Notes 5 and 6); (4) the funding history: losses, share issuance, the 1-for-20 reverse split (statements; Item 5);
  (5) what happened after the last report: the 8-Ks of 2015 and the 2023 revocation.
- `python tools/run.py VUOC`: "VUOC: not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE." The tool cannot find
  the CIK through the ticker map, so no tool arithmetic exists for this name. The arithmetic below is transcribed by
  hand from the filed statements and summed in `Test Runs/_research 2026-10-17 VUOC/compute.py` (output in
  `compute_out.txt` beside it). **Owner cash after every real cost by year** (operating cash flow, less equipment,
  construction and building-deposit spending, less costs paid in stock: share-based pay, stock and warrants for
  services, stock issued for rent): FY2007 −$3.54M; FY2008 −$10.08M; FY2009 −$5.85M; FY2010 −$5.00M; FY2011 −$7.39M;
  FY2012 −$2.16M; FY2013 −$2.86M; FY2014 −$1.74M. **Five-year average FY2010 to FY2014: −$3.83M** (−$2.91M before the
  stock-paid costs). Capex and depreciation: depreciation $19,479 against equipment bought $157,052 in FY2014; neither
  matters beside the losses. Stock pay is resolved and complete as listed above; it is a real cost and is charged.
  Revenue in the whole span: $7,816 in FY2011 (at a cost of revenue of $47,357) and $8,715 in Q1 2015 (cost $17,553);
  none in any other year read.

**The balance sheets, eight to ten years, read now because the file closes before Q4** **[M2025-032]**. As filed;
shares before the 1-for-20 reverse split of 2011-11-23 (stated in the FY2011 and FY2012 10-Ks, Item 5) are divided by 20
so the column is comparable.

| Dec 31 | cash | total assets | total liabilities | equity (incl. minority) | accumulated deficit | shares (post-split basis) |
|---|---|---|---|---|---|---|
| 2006 | $289,795 | $300,145 | $344,403 | −$44,258 | −$45.42M | 2.37M |
| 2007 | $1,014,512 | $3,324,167 | $624,666 | $2,699,501 | −$48.53M | 3.23M |
| 2008 | $2,486,609 | $3,390,351 | $606,303 | $2,784,048 | −$58.39M | 4.28M |
| 2009 | $366,303 | $1,873,026 | $4,054,926 | −$2,181,900 | −$65.87M | 4.31M |
| 2010 | $119,619 | $1,768,929 | $729,895 | $1,039,034 | −$70.50M | 5.25M |
| 2011 | $10,992 | $437,629 | $5,093,045 | −$4,655,416 | −$79.58M | 5.57M |
| 2012 | $328,188 | $489,410 | $5,712,367 | −$5,222,957 | −$83.41M | 7.13M |
| 2013 | $92,795 | $313,414 | $6,227,053 | −$5,913,639 | −$88.43M | 10.58M |
| 2014 | $1,903 | $207,864 | $6,874,392 | −$6,666,528 | −$91.42M | 12.95M |
| 2015-03-31 | $2,432 | $196,032 | $6,515,320 | −$6,319,288 | −$92.34M | 13.97M |

What the figures say: there is no receivable, no inventory to speak of and no revenue line in most years, so there is
nothing for working capital to be measured against; the only assets that were ever more than a rounding error were
cash raised from share sales, prepaid rent paid in stock (FY2007, $1.59M) and the fixed assets, construction and building
deposit of the Czech subsidiary, written off in the FY2011 impairment of $1,812,728 "due to the insolvency proceedings
of Sendio filed in February 2012" (FY2012 10-K, MD&A). The accumulated deficit roughly doubled, from $45.4M to $92.3M, while the share count rose
about six times on a comparable basis. From 2011 every year ends with liabilities of about $5M to $7M against assets
under $0.5M: at 2015-03-31, $2,788,300 of convertible debentures, $1,295,920 of judgments, $1,505,938 of payables,
$555,454 of liabilities of the insolvent Czech subsidiary, all current. What they cannot say: anything after
2015-03-31. What the management would like them to say, in its words, is that its lights "will capture a growing share
of the general illumination market" (Item 1); the auditor's report says "substantial doubt about the Company's ability
to continue as a going concern" (FY2014 10-K, report of Peterson Sullivan LLP).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is **a share is a business**: the test is whether I would be content to own it "if
the market closed for five years" **[M1997-109]**, or if the stock were delisted and reopened years later **[M1996-067]**.
Here the market has in effect closed: the registration is revoked and nothing has been reported for over ten years, so
the owner would hold a claim on a business whose last audited statement is FY2014. The question the foundation asks,
what the business itself will produce, can only be put to the 2015 record. **The market serves, it does not instruct**:
there is no price to be out of line with "where the facts and reasoning lead" **[M2006-077]**. **Margin of safety**: no
pencil is in reach either way **[M1996-084]**. **Who is paid to tell you**: the only narrative about the business is
the filer's own, written while it was selling shares to fund losses. **Contrary evidence, written down as found**
**[M1997-127]**: the evidence that runs *for* the business, recorded so it is not lost: nine patents granted of eleven
filed (Item 1); UL safety certification for the R30 (October 2010) and the A19 (August 2011); "we have not identified any
competitors with a similar technology to ESL" (Item 1, Competition); a first limited shipment of R30 bulbs to a customer
in Q1 2015 (Item 1; $8,715 revenue in the 10-Q); the board's statement of 2015-07-31 that it would seek "a possible sale
of the Company, a strategic partnership, a technology licensing agreement" (8-K Exhibit 99.1). Nothing on the public
record shows any of these led anywhere.

## THE STANDING RULE
A cash purchase of a small position, with no borrowing, cannot ruin the buyer; the rule bears only on sizing: the rows'
rule is "Never risk permanent loss of capital." **[L2023-005]**, and with the registration revoked and no report since
2015, the whole outlay would be at risk. Nothing in the standing rule closes the
file; a leveraged or large purchase would breach it **[M2004-065]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**; "being able to asses where the business
  will be in 10 years" **[M2000-037]**. The key variables, and how predictable they are, come first: "If something is not
  very predictable, forget it." **[M1998-044]**. For Vu1 the key variables, from the 10-K's own Item 1 and Item 1A, are:
  (i) whether an ESL bulb can be made at a commercial cost at all ("Our progress has been limited, primarily due to lack
  of adequate funding"; "In 2015, our success will depend on our ability to secure additional funding, reach commercial
  manufacturing levels for our R30 and R40 lights", Item 7); (ii) whether it can sell against LEDs in a field the filer
  calls "characterized by rapid technological change and evolving industry standards" in which "The introduction of
  lighting products embodying new technology [...] can render existing products and technologies obsolete" and "The
  market for lighting technology is changing rapidly" (Item 1A); (iii) whether the company keeps its own patents, on
  which judgment holders "placed a levy on all of our intellectual property, demanding that we turn over our patents,
  trade secrets, manufacturing methods and other intellectual property" in April 2015 (Item 3; Note 3); (iv) whether it
  survives, the auditor having raised "substantial doubt about the Company's ability to continue as a going concern"
  (FY2014 report). None of the four is foreseeable from the filings; the filer itself says "we may never generate
  significant revenue or achieve net income" (Item 1A).
- **Do the past statements tell me the future ones?** **[M2008-033]**. They do not: ten years of statements show only
  research spending funded by share sales, and there are no statements of any kind after 2015-03-31.
- **It is a start-up.** The filer: "We have historically been a research and product development company. We have a
  limited operating history with minimal revenue to date" and "we had no revenues in 2014 or 2013" (Item 1A); research on
  the lighting technology began "In late 2004" (Item 1, Corporate Information); in the whole span read, revenue was
  $7,816 in FY2011 and $8,715 in Q1 2015, each below its cost of revenue; "As of December 31, 2014, we had no employees"
  (Item 1, Employees). The rows: "Start-ups are not our game." **[L2007-015]**; "I say, “We don’t do startups.” They
  don’t exist." **[M2008-088]**. The framework lists start-ups first among what Q1 rules OUT.
- **It is also fast-moving technology.** The filer's own words above meet the rows' description: "a business that must
  deal with fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics."
  **[L1993-023]**; "if something comes in where there’s a technological component that’s of significance [...] it won’t
  make it through the filter." **[M1998-008]**. On that ground alone the framework's routing sends the file to TOO HARD
  at Q1, and the cause would be NATURE: the forecast is one the industry's insiders "would not want to put down on paper"
  **[M2000-105]**.
- **Which box.** Two of Q1's items apply and they name different boxes: start-ups are on the list of what Q1 rules OUT,
  fast-moving technology is "Sent to TOO HARD, not OUT". The box is **OUT**, for this reason: the rows send fast-moving
  technology to TOO HARD because of ignorance, "It just means that we don’t know how to evaluate it." **[M2000-038]**, but
  here the deciding fact is not ignorance of the field; it is a finding on the filer's own record that there is no
  operating business to understand: no revenue to speak of after a decade of development, no employees, a going-concern
  doubt, the patents under levy, the CEO gone (8-K, 2015-07-07), the board seeking "a possible sale of the Company" (8-K,
  2015-07-31), and after that ten years of silence ending in a revoked registration of "a suspended California
  corporation" (Release No. 97085). The start-up rule is the rows' blotter, applied before any evaluation is attempted
  ("They don’t exist." **[M2008-088]**), and study does not cure it: "we’re not going to learn enough in the followings
  five months to make up for the fact that we went in deficient in the first place." **[M2008-086]**. The choice
  between the two items is mine, recorded under What in the framework was wrong or unclear; either box closes the file
  here, and no answer to the rapid-change question could make the start-up item not apply.
- **Doubt.** Even setting both items aside, "if you have doubts about something being into your circle of competence, it
  isn’t." **[M2002-092]**; there is nothing in the record of the last ten years to be inside or outside a circle.
- **VERDICT: OUT** at Q1: a pre-revenue start-up on its own filings **[L2007-015]**, **[M2008-088]**, in a field the
  filer calls rapidly changing **[L1993-023]**; filing facts: 10-K FY2014 (`0001096906-15-000450`) Items 1, 1A, 3 and
  the auditor's report; 10-Q Q1 2015 (`0001096906-15-000592`); Release No. 97085 (`9999999997-23-000886`).

## Q2 — WHY IS THE CASTLE STILL STANDING? NOT REACHED (Q1 closed the file).
## Q3 — HOW MUCH CAPITAL MUST GO IN? NOT REACHED.
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? NOT REACHED. (The balance sheets were read at Step 0, as the template asks when the file closes before Q4.)
## Q5 — WHO RUNS IT? NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? NOT REACHED. (No buyback exists to test against Q7.)
## Q7 — WHAT IS IT WORTH? NOT REACHED as a question; the arithmetic is below under COMPUTATION, NOT A CLEARANCE.
## Q8 — BETTER THAN THE ALTERNATIVES? NOT REACHED.
## Q9 — COULD IT RUIN US? NOT REACHED.
## Q10 — THE FAT PITCH? NOT REACHED.
## Q12 — PROUD OF HOW THE MONEY IS MADE? NOT REACHED.

---
## THE BOX
**OUT at Q1** (a pre-revenue start-up on its own filings, in a field the filer calls rapidly changing; the
alternative reading, TOO HARD (NATURE) on rapid change, was considered and is recorded under Q1 and below). No current
price exists; the computation below gives a value range of nil to nil per share and a fair price of nil, against a last
filed close of $0.62 (2015-04-15). **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.*

- **Q2 (the castle).** Rivals named by the 10-K (Item 1, Competition; Item 1A): General Electric Company, Philips
  Electronics NV, Osram Sylvania, "hundreds of small manufacturers of low-end products", and "Many companies are now
  developing products utilizing solid-state LED technology". Filing status checked against the SEC's ticker file on
  2026-10-17: General Electric files (CIK 40545); Koninklijke Philips files (CIK 313216); Osram Sylvania has no entry in
  the ticker file, and the only EDGAR entity found by name is "OSRAM Licht AG/ADR" (CIK 1603194), whose filings were
  not read. No competitor's filing was read: Q2 was not reached, so **there is no competitor comparison in this run.**
  The filer's own claim for its position: "we have not identified any competitors with a similar technology to ESL"
  (Item 1). The filer's own words on the attackers: the field is "dominated by a number of well-funded multi-national
  companies" (Item 1A).
- **Q3 (capital).** Eight years of owner cash, FY2007 to FY2014, sum to about −$38.6M; the accumulated deficit at
  2015-03-31 is $92.3M (Step 0). There is no return on capital to measure.
- **Q4 (the accounts).** Going-concern paragraph in the FY2014 auditor's report. Three defects in the FY2014 10-K
  itself: the running header "2013 ANNUAL REPORT ON FORM 10-K"; the cover's non-affiliate market value "on June 30,
  2013"; the accumulated deficit $91,416,708 on the balance sheet against $91,417,708 in Note 3. The FY2014 cash-flow
  statement shows accrued interest rising $851,681 while the balance-sheet line rose $176,284 ($324,531 to $500,815);
  part of the difference is the reclassification of accrued interest to "Judgment payable" (Item 3); I did not
  reconcile the rest. The losses were funded by share sales: net proceeds of $1,265,000 (FY2014) and $1,503,465
  (FY2013) against operating cash outflows of $1,081,190 and $1,716,606.
- **Q5 (integrity; flagged in the box line).** The Commission held that the company's repeated failure to file evinced
  "a high degree of culpability" (Release No. 97085, its words quoting earlier opinions; the order's inner quotation
  marks omitted), and found that the company answered neither the order instituting proceedings nor the order to show
  cause. The Chairman and CEO resigned on 2015-06-30, "effective immediately", with "no disagreements" (8-K filed
  2015-07-07). The FY2014 10-K claims "Experienced Management" (Item 1) for a company with no revenue and no employees.
  The 2015-07-31 release says the company "does not expect to update its progress or disclose developments" of its
  strategic review; no later filing exists. Five debenture holders obtained judgments for unpaid principal and interest
  (Item 3).
- **Q6 (the money and the owners).** Shares outstanding rose from about 2.37M (2006, split-adjusted) to 14.27M
  (2015-05-12), across a 1-for-20 reverse split on 2011-11-23. On 2015-06-04 the debenture conversion price was cut from
  $2.00 to $0.50 a share and the interest due on 2015-12-22 and 2016-06-22 was made payable in shares (8-K,
  `0001096906-15-000628`). The board raised the 2007 Stock Incentive Plan from 1,000,000 to 2,500,000 shares on
  2013-08-26, with stockholder approval still to be sought in 2015 (Item 5).
- **Q9 (debt and exposures).** At 2015-03-31 every liability is current: convertible debentures $2,788,300, judgments
  $1,295,920, payables $1,505,938, accrued payroll $192,725, accrued interest $176,983, liabilities of the insolvent
  Czech subsidiary Sendio $555,454 (Sendio declared insolvent by the Regional Court in Olomouc in March 2012, Note 5).
  Cash $2,432. Judgment holders levied on all the company's intellectual property in April 2015.

## COMPUTATION, NOT A CLEARANCE
*Q7's construction applied after the Q1 stop, for the two reporting figures the operator asks for; not a value, not a
verdict, no entry language (operator rule 3). Script and output: `Test Runs/_research 2026-10-17 VUOC/compute.py`,
`compute_out.txt`.*

- **Base.** Owner cash after every real cost, five-year average FY2010 to FY2014: −$3,829,780 on the equity-only basis
  (after cash interest); −$3,780,215 on the all-equity basis (before cash interest paid, which averaged $49,565). Every
  year in the window, and every year read from FY2007, is negative. The literal window and the base are the same: there
  is no cycle, and the filer calls no year aberrational.
- **Growth, by specific (b).** The series is negative in every year, so a growth rate between end years or between the
  halves of the window is meaningless; by (b) the range is the no-growth case alone, said so. Specifics (a), (c), (e)
  and (f) do not apply (no cycle, no acquisitions, no maintenance guess the filing allows, no positive rate to cap).
  Specific (d): working capital is inside operating cash as filed; the rise in unpaid payables and accrued interest
  makes the outflow smaller than the losses, and it is left as filed.
- **The floor, tested first.** No case earns any return at any positive price: the cash stream is an outflow. On the
  framework's convention the file would close OUT here whatever the width.
- **Value range (all-equity basis, the central figure):** the no-growth case at the 5.43% long rate, −$3.78M a year
  carried without end, is −$69.6M for the whole business; less net debt of $4.08M at 2015-03-31 (debentures $2,788,300
  plus judgments $1,295,920 less cash $2,432; payables, accrued items and the Sendio liabilities are not borrowings and
  are left out of net debt, said so), −$73.7M, or −$5.16 a share on 14,273,093 shares. Reported as **nil to nil per
  share**. **CONVENTION of this run:** a negative computed value per share is reported as nil, because an owner of the
  shares cannot lose more than the price paid; the signed figure is shown so nothing is hidden. Rationale: Part VII asks
  for a figure per share and gives no rule for a negative one. A perpetuity of losses is itself absurd, since no owner
  would fund it; the plainer reading, the balance sheet of 2015-03-31, gives assets of $196,032 against liabilities of
  $6,515,320, a deficit of $6.32M or −$0.44 a share: nil as well.
- **Fair price (Part VII: each end case valued at ten percent, the two averaged; the range has one case, so the average
  is that case):** all-equity basis −$37.8M for the whole business, −$41.9M after net debt, −$2.93 a share: **nil**.
  Equity-only beside it: −$38.3M, −$2.68 a share: **nil**. Tax: the company paid no income tax in any year read (the
  provision is nil every year); no carryforward is credited on the $92M of losses, because section E prices a shelter on
  owner cash that is taxable, and no filed figure shows taxable income in prospect.
- **Against the price:** there is no current price; the last filed close, $0.62 on 2015-04-15, is above a fair price of
  nil.

*No research pass is written: the box is OUT, not TOO HARD (WORK); and by Part VII a pass would be closed unrun in any
case, since no case of the range earns the floor at any price.*

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after Step 0, after Q1, and
      at the close (write-early).
- [x] Dispatched: the brief allowed per-question pathspec commits of the two paths; the lock and the fold are the
      dispatching session's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what the session context
      showed by accident is declared under Contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check
      script `Test Runs/_research 2026-10-17 VUOC/check_ids.py`); every filing fact carries its accession; the numbers
      come from the filings or are CONVENTION-labelled.
- [x] The order was kept; Q1, the first STOP, failed and closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, stock-paid costs charged, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the aggregator quote could not be had, and that is flagged.
- [x] Contrary evidence written down as found (foundations); the facts for later questions are under AFTER THE STOP,
      with "integrity facts recorded, not judged" in the box line.
- [x] Not a point-in-time run; no anchor applies. (The figures are ten years old because the company stopped filing,
      not because the run is anchored.)
- [x] `tools/run.py` produced no arithmetic for this name (ticker not in the SEC map); its printed text was not used.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Two Q1 items, two boxes.** Q1's list of what it rules OUT begins with start-ups **[L2007-015]**, **[M2008-088]**,
and the paragraph after it sends fast-moving technology to TOO HARD, not OUT. A pre-revenue technology start-up meets
both, and the text does not say which governs. I chose OUT on the start-up item, because the rows give the TOO HARD
reason as ignorance ("we don’t know how to evaluate it" **[M2000-038]**) and here the filer's own record is a finding
that there is no operating business; a second analyst could defensibly write TOO HARD (NATURE). The file closes at Q1
either way, but the box differs, and the box decides whether a research pass is owed. A sentence saying which item
wins when both apply would settle it. (2) **An issuer that has stopped reporting.** The framework has no item for a
security whose issuer has filed nothing for a decade and whose registration is revoked; section I records that a
verdict "for a document not yet read" has no row, and this is the case of a document that does not exist. I decided on
the last filings and said so in Step 0. (3) **Negative values in the reporting figures.** Part VII asks for a range and
a fair price per share and does not say how to report a negative one; I reported nil and confessed it as a CONVENTION
of this run, with the signed figure shown. (4) **Specific (b) and a series negative throughout.** (b) names a series
that changes sign; a series negative in every year is not named, and I read it as the same case (the range is the
no-growth case alone). (5) **Step 0 asks for a price and a market cap**; where no market exists the template has no
line for it, and I recorded the last filed close as a reference only.
