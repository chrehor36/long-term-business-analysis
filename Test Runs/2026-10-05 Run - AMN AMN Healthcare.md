# Company Run: AMN Healthcare Services, Inc. (NYSE: AMN), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Working folder:
`Test Runs/_research 2026-10-05 AMN/` (filings as text, `fetch.py`, `htm2txt.py`, `series.py`, `peers.py`, `calc.py`,
`idcheck.py`, `runpy_output.txt`, `peers_table.txt`). Every judgment cites a v5 row in bold; quotations inside double
quotes are the row's own words. Run begun 2026-10-05, resumed and finished 2026-10-06 after a session limit; the
dates of the price and the rate stay those of 2026-10-05.

**POSITION NOTE, declared before any verdict:** not known to this analyst. The blind rule forbids opening `PORTFOLIO.md`,
so whether the operator holds AMN was not checked.

**BLIND RULE AND CONTAMINATION, declared.** Not opened: `PORTFOLIO.md`, any holding review, `Screens/RESUME STATE*`,
the run queue, the prepped reading list, any other `Test Runs/` file about AMN, the unadopted gaps case. Seen without
opening: (1) the recent commit subjects in the session context, which give the boxes of the INVA (OUT at Q1), PBH
(OUT at Q7) and RHI (TOO HARD (NATURE) at Q1, contract hours down and AI disagreement) runs, and a `run.py` note from
the SKYW run; RHI is one of this run's named comparators, so its box was known before Q1 here; (2) the git status
naming a POOL run file and the directory listing naming other companies' 2026-10-05 research folders (names only);
(3) one `grep -o` for the string "COMPUTATION" in the INVA run file and a file-list `grep -l` in the PBH run file, run
only to learn how sibling runs spelled the protocol heading without an em dash. That command returned fragments of
INVA's text around the word (no figures of AMN, nothing on staffing); it was a breach of the letter of the blind rule
and is declared as such. (4) The session memory index says "57 gate-clearers, nothing buyable" across the queue. None
of these bears on AMN's facts; the RHI box is the one that could have steered the Q1 choice, and Q1 below says how
the choice was made.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $36.82 (2026-10-05; printed by `tools/run.py` as "aggregator, live quote only"; flagged under operator
  rule 5).
- **Shares:** 38,729,991 common, one class, from the cover of the 10-Q for the quarter ended 2026-06-30, filed
  2026-08-07, accession `0001628280-26-054507` (`python Screens/cover_shares.py AMN`). Balance sheet the same date:
  38,716 thousand outstanding, 51,414 thousand issued, 12,698 thousand in treasury.
- **Market cap:** $1,426M. Net debt at 2025-12-31 (audited): debt $775.0M face less cash $34.0M = $741M; enterprise
  value about $2,167M. At 2026-06-30: debt $750.0M, cash $361.8M, but "client deposits and reserves" of $237.2M sit in
  current liabilities against strike engagements still being reconciled, some of which may be refunded (10-Q, note on
  revenue and balance sheet details).
- **Sovereign, earnings currency USD:** 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05 (via
  `tools/run.py`, which calls the Treasury; issuing authority).
- **Filings read (operator rule 4):** 10-K FY2025, filed 2026-02-20, accession `0001628280-26-009918` (Business, Risk
  Factors, Item 5, MD&A, the four statements, notes 2, 3, 5, 9, 10, 11, 12, 13, segment note 1(t)); 10-K FY2024,
  `0001142750-25-000011` (Kaiser share, 2024 impairment reasons, 2024 bill rates); 10-Q Q2 2026,
  `0001628280-26-054507` (MD&A, balance sheet, contingencies, buyback table); proxy filed 2026-03-18,
  `0001104659-26-029908` (letter, CD&A, summary compensation table, ownership); 8-Ks of 2025-09-22
  (`0000950142-25-002494`, 2031 notes and redemption of the 2027 notes), 2025-10-06 (`0000950142-25-002687`, credit
  amendment), 2026-08-06 (`0001142750-26-000008`, Q2 results, cover only); selected financial data from the 10-K FY2005
  (`0001193125-06-051648`) and FY2010 (`0001193125-11-062637`) for 2001 to 2010. XBRL company facts for 2009 to 2025.
- **One figure cross-checked against the filed statement:** operating cash flow FY2025 $269,457 thousand in the filed
  cash-flow statement; `run.py` printed 269.5. Also the 2025 balance-sheet row (equity 642.1, goodwill 755.8,
  intangibles 283.5, debt 767.1) matches the filed balance sheet.
- **`tools/run.py AMN`, arithmetic lines only** (its v4 rule text, ids and floor were not used; Part VII):

| FY | OCF | SBC | capex | D&A | OCF − SBC − capex | OCF − SBC − D&A |
|---|---|---|---|---|---|---|
| 2021 | 305.4 | 25.2 | 53.6 | 103.7 | 226.6 | 176.5 |
| 2022 | 653.7 | 30.1 | 75.8 | 137.1 | 547.8 | 486.5 |
| 2023 | 372.2 | 18.0 | 103.7 | 160.9 | 250.5 | 193.2 |
| 2024 | 320.4 | 23.3 | 80.9 | 173.8 | 216.2 | 123.3 |
| 2025 | 269.5 | 30.7 | 35.6 | 156.6 | 203.1 | 82.2 |
| 5-yr mean | | | | | 288.8 | 212.3 |

  USD millions. D&A includes amortization of acquired intangibles ($78.0M in 2025); depreciation alone was $78.5M in
  2025 ($69.8M plus $8.7M in cost of revenue), against capex of $35.6M. SBC resolved: one line, `ShareBasedCompensation`,
  each year; no other stock-pay line found in the cash-flow statement.

### The fifteen-to-twenty-five-year record (filed selected data 2001 to 2010; XBRL 2009 to 2025)
| Year | Revenue | Op. income | Op. margin | Note |
|---|---|---|---|---|
| 2001 | 518 | 16 | 3% | IPO year, stock-pay charge |
| 2002 | 776 | 86 | 11% | first travel-nurse boom |
| 2003 | 714 | 64 | 9% | |
| 2004 | 629 | 36 | 6% | bust: revenue down 19% from 2002 |
| 2006 to 2008 | 1,082 to 1,217 | 72 to 73 | about 6% | |
| 2009 | 760 | (154) | | $187M impairment and restructuring; revenue down 38% from 2008 |
| 2010 | 689 | (43) | | $51M impairment and restructuring |
| 2011 to 2014 | 888 to 1,036 | 38 to 68 | 4% to 7% | |
| 2015 to 2020 | 1,463 to 2,394 | 129 to 212 | 6% to 11% | growth largely bought: acquisitions $84M to $477M a year |
| 2021 | 3,984 | 478 | 12% | pandemic boom |
| 2022 | 5,243 | 647 | 12% | peak |
| 2023 | 3,789 | 338 | 9% | MSDR bought for $292M |
| 2024 | 2,984 | (103) | | goodwill impairment $222M |
| 2025 | 2,730 | (55) | | goodwill impairment $110M, intangible $18M, gain on sale $(39)M |
| H1 2026 | 2,052 | 7% of revenue | | $747M of labor-disruption (strike) revenue in the half |

Segment gross margins FY2025 (10-K, segment note): nurse and allied 23.0% (24.5% in 2024), physician and leadership
27.6% (29.7%), technology and workforce 52.7% (58.9%). Consolidated gross margin 33.5% in 2019, 32.7% in 2022, 28.3% in
2025 (XBRL). Segment operating income 2023 $672M, 2024 $426M, 2025 $309M.

### The balance sheets, ten year-ends, read before the income account **[M2025-032]**
| Year-end | Assets | Equity | Cash | Receivables | Goodwill | Intangibles | LT debt | Retained |
|---|---|---|---|---|---|---|---|---|
| 2016 | 1,187 | 449 | 11 | 342 | 342 | 246 | 359 | 10 |
| 2018 | 1,493 | 639 | 14 | 366 | 439 | 326 | 441 | 286 |
| 2020 | 2,354 | 820 | 29 | 376 | 864 | 565 | 858 | 470 |
| 2021 | 3,132 | 1,162 | 181 | 789 | 892 | 514 | 842 | 797 |
| 2022 | 2,888 | 1,044 | 65 | 676 | 935 | 477 | 844 | 1,241 |
| 2023 | 2,924 | 831 | 33 | 623 | 1,112 | 474 | 1,305 | 1,452 |
| 2024 | 2,416 | 707 | 11 | 438 | 897 | 381 | 1,056 | 1,305 |
| 2025 | 2,094 | 642 | 34 | 383 | 756 | 284 | 767 | 1,209 |

(`run.py` table, first-filed XBRL vintages, accessions in `runpy_output.txt`; 2025 checked against the filed sheet.)

What the figures say: (1) **The equity is all purchased goodwill and intangibles.** At 2025-12-31 goodwill and
intangibles are $1,039M against equity of $642M: tangible equity is about minus $397M. Accumulated goodwill impairment
is $547M (note 5), against roughly $1.7B paid for acquisitions 2013 to 2023 (cash-flow statements). (2) **Receivables
are the cycle's thermometer.** They doubled in 2021 (376 to 789) and fell back to 383 by 2025; that run-off is cash
released by shrinking, and it flatters operating cash flow in 2023 to 2025 (working-capital changes added $86M in 2024
and $101M in 2025; filed cash-flow statements). (3) **Debt rose as the business shrank.** Long-term debt was $359M in
2016, $1,305M in 2023, $767M in 2025; the 2023 peak followed $1,005M of buybacks in 2022 and 2023 and the $292M MSDR
purchase. The revolver covenant was loosened twice (fourth amendment, November 2024; fifth amendment, October 2025, net
leverage up to 5.25 times through March 2027; 10-K note 9). (4) **Retained earnings of $1,209M sit beside $1,127M of
treasury stock** bought at an average $89.04 a share (Item 5); the company bought back about a third of its shares
issued at more than twice today's price. (5) Cash is kept near zero except when a strike pays in advance (June 2026:
$362M, of which $237M of client deposits and reserves stand against it). (6) Company-owned life insurance of $215.5M in
other assets is matched by a deferred-compensation liability of $214.3M (note 10; 10-Q); neither is free cash. What
they cannot say: whether the 2016 to 2022 margins were the business or the cycle.

---
## THE FOUNDATIONS (not a gate)
A share is a business: would I own this "if the market closed for five years?" **[M1997-109]**. The bearing foundation
here is that no macro forecast enters, yet the business's earnings are the macro: hospital census, nurse vacancy, a
pandemic, strikes, Medicaid policy (the 10-K's own demand drivers, Item 1). The speakers' instruction is to look at "the
average profitability of the business over time and how strong its competitive mode is" **[M2015-016]**, which is what
Q2 and the whole-cycle computation below try to do. The market "just tells us prices" **[M2006-077]**: a fall from
about $97 (2023 buybacks) to $36.82 says nothing by itself. Who is paid to tell you: the proxy letter calls $269M "free
cash flow" when that figure is operating cash flow before $35.6M of capex and includes $101M of working-capital release
(proxy p. 3; 10-K cash-flow statement).

**Contrary evidence, written down as found** **[M1997-127]**: (a) AMN's operating margin beat Cross Country's in every
year from 2011 to 2020 and on the whole span (6.6% against 2.4%, 2009 to 2025), so there is a relative edge over the
one listed healthcare peer; (b) 48% of 2025 revenue flowed through MSP contracts, and Kaiser, 22% of revenue, chose
AMN as its clinical managed-services provider; (c) AMN staffed "multiple large scale labor disruption events" for $747M
of revenue in H1 2026, a capacity few firms can supply at that size; (d) the proxy claims share gains in travel nurse
and allied in 2025 (company's claim, not tested); (e) at $36.82 the price is far below every whole-cycle computation
below. Each is weighed at Q2 or in the computation.

## THE STANDING RULE
The buyer's own ruin turns on the buyer's financing and size, not on AMN: buy without borrowed money, since "borrowed
money has no place in the investor's tool kit" **[L2014-005]**, and never risk "what we have and need for what we
don't have and don't need" **[M2012-081]**. A stake in a levered, cyclical, negative-tangible-equity company would have
to be sized so that its loss to zero is survivable. No conflict arises because the file closes at Q2.

---
## Q1: CAN I UNDERSTAND IT? STOP.
**What the business is.** A broker of clinical labor hours. It recruits nurses, allied staff, locum physicians,
interim leaders and interpreters, places them at hospitals, and keeps the spread between the bill rate and the pay
package (housing, travel, allowances). It also sells the procurement layer: MSPs in which it fills a client's
contingent needs with its own people and subcontracted agencies, and vendor-neutral VMS software on which agencies
compete for a fee of about a percentage of spend ($1.8B of MSP spend, $1.4B through VMS in 2025; 10-K Item 1). Capital
needs are small (capex $36M to $104M a year); the asset is the recruiter network, the client contracts and the
receivables.

**The key variables** **[M1998-044]**: travelers on assignment, the bill-to-pay spread, the MSP share, Kaiser, strike
events, and the cost of staying competitive (technology, acquisitions). Three are not predictable in any year: demand
(down 24% in travelers in 2024, 14% in 2025), strikes ("unpredictable", MD&A), and pay packages. But the speakers' test
is "a reasonable fix on about what the earning power and competitive position will look like in five or 10 years"
**[M2012-065]**, and the economics of the type are plain: "I understand the economic dynamics of the industry"
**[M2011-014]** is answerable here. Twenty-five years of filings show three booms (2002, 2008 at a lower pitch, 2022)
and three busts (2004, 2009 to 2010, 2024 to 2025), with operating margins of roughly 3% to 12% around a whole-span
mean of about 6.6%. In ten years AMN will still be a thin-margin, capital-light, cyclical intermediary in a fragmented
industry; that is a forecast an insider would write down **[M2000-105]**, though no insider would write the year of the
next boom.

**How the choice was made.** The case for TOO HARD (NATURE) at Q1 is real: the earnings level swung by more than four
times between 2022 and 2025, and management's own forecasts in the goodwill tests failed within months (2024 and 2025
impairments were "due to recent declines in forecasted revenue"). Against it: cyclicality is not "rapid and continuous
change" of the industry; the speakers judge cyclical businesses on average profitability over time **[M2015-016]** and
sort a bad year as "a cyclical problem, not a secular one" **[L1995-022]** or the other way. What is uncertain about AMN
is whether its position is eroding, which is the castle question, and the evidence on it is on the public record. I
have no doubt that the economics of a labor broker are inside the perimeter; the doubt rule **[M2002-092]** bites on the
castle, not on the understanding. The RHI box seen in the commit subjects (TOO HARD at Q1 on AI) was set aside: AI is
named as a risk in AMN's 10-K, but the decisive evidence here is present-tense and already in the accounts.

**VERDICT: IN.** The economics are understood as those of a commodity labor intermediary; Q2 tests what that
understanding shows. *(Honest note: a second analyst could close this file TOO HARD (NATURE) here; see the last
section.)*

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
The question: "why is that castle still standing?" **[M1995-038]**. The filings answer that the castle is open.

1. **The money test and new entrants.** "if I had a hundred million dollars [...] could I do it?", and "If the answer
   had been yes, we wouldn't have done it." **[M2011-015]**; "why are there no new entrants into the field?"
   **[M2000-077]**. Answered by a competitor in filed words: Cross Country's 10-K FY2025 (`0001628280-26-015791`):
   "The market continues to evolve with new competitors entering the industry as barriers to entry are fairly low."
   Aya Healthcare, a private firm, is described in Cross Country's merger proxy (`0001140361-25-001610`) as "the largest
   healthcare talent software and staffing company in the United States" (Aya's own description, unaudited; flagged).
   AMN's 10-K lists Aya first among its leading competitors and adds that it competes for clinicians with "hospital
   systems that have developed their own recruitment departments and internal travel agencies". An industry
   "just never going to have barriers to entry" **[M2012-106]**.
2. **Would the customer still choose it over the low bid?** **[M2017-009]**. The customer buys through procurement
   built to make agencies interchangeable: AMN's own VMS lets clients that "use other staffing companies (associate
   vendors)" self-manage the buying, and its MSPs "utilize other staffing agencies". The customer cares about the fill and
   the rate, not the name; "most insureds don't care from whom they buy" **[L2004-003]** is the nearer pattern than the
   brand. VMS revenue fell 31% in 2025 "due to lower staffing utilization on the platforms along with several client
   losses" (10-K MD&A).
3. **Pricing power, the agony test** **[M2005-020]**. AMN sets neither side of its spread. In 2024 the average bill rate
   fell about 10% while goodwill was impaired for "gross margin pressures driven by higher provider pay packages" (10-K
   FY2024, note on goodwill); in 2025 nurse and allied gross margin fell from 24.5% to 23.0% on "compression in clinician
   pay packages"; language services suffer "pricing pressure [...] due to increased market competition" (10-K MD&A).
   The market sets the price on both sides; "he determined our profit, because we looked at his price every day"
   **[M2023-079]** describes the position.
4. **The low-cost position.** AMN's whole-span operating margin (6.6%, 2009 to 2025) is above Cross Country's (2.4%) and
   Kforce's (4.4%) and below Robert Half's (8.6%), so AMN is a better operator than its listed healthcare peer. It is not
   shown to be the low-cost producer of the industry: the largest firm is private and its costs are not filed, and AMN's
   2024 to 2025 margins fell as far as the peer's (both negative after impairments). Being better than the weakest public
   rival is not the commodity exception.
5. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Narrowing on the filed record: consolidated gross margin
   33.5% (2019) to 28.3% (2025) at similar revenue; technology segment gross margin 58.9% to 52.7% in one year and 48.6%
   in Q2 2026; VMS client losses; interim leadership and search hit by "insourcing"; locum days filled down 8% to 9%;
   $547M of goodwill written off in the units bought to widen it. Each acquisition (B.E. Smith, Stratus Video, Connetics,
   MSDR and others, about $1.7B from 2013 to 2023) was the moat being rebuilt with money, and "A moat that must be
   continuously rebuilt will eventually be no moat at all." **[L2007-005]**.
6. **Concentration.** Kaiser rose from 16% of revenue (2024) to 22% (2025). One customer's procurement decision or one
   rival's MSP bid can move a fifth of the revenue; "one competitor is frequently enough to ruin a business"
   **[M2012-108]**.
7. **Ask the competitors.** Cross Country's board sold, first to Aya at $18.61 (terminated 2025-12-04, a $20M fee paid to
   Cross Country) and then to Knox Lane at $13.25 a share in cash (8-K `0000950103-26-006921`; closed 2026-07-21,
   8-K `0000950103-26-011218`). The consolidators are private and one tried to buy the listed rival; the listed rival's
   price fell by a third between the two deals.
8. **What could destroy or reduce it, five to fifteen years out** **[M2000-014]**: hospital internal agencies,
   vendor-neutral platforms that make the agency a commodity, AI in scheduling and credentialing (10-K risk factor),
   the reclassification of locum contractors, and wage-and-hour class actions on per-diem practice (the Clarke matter
   settled for $62M, paid 2024; similar class and representative actions remain the "most significant" accrued
   contingencies, note 13).
9. **The strongest case for the castle**, stated as its holder would: MSP incumbency is sticky, Kaiser chose AMN, the
   strike-staffing machine is rare, and scale in recruiting gives a larger clinician pool (10-K Item 1). Against it:
   the MSP is itself a rebid contract, the strike revenue is episodic by the company's own word, and the scale did not
   protect 2024 to 2025 margins any better than the smaller peer's.

**The competitor row** (operating margin, same metric, each company's own filings via XBRL; latest 10-Ks: AMN
`0001628280-26-009918`, CCRN `0001628280-26-015791`, RHI `0000315213-26-000006`, KFRC `0000930420-26-000007`; CCRN's
2025 revenue $1,054,293 thousand cross-checked to its filed income statement):

| Span | AMN | CCRN (healthcare) | RHI (generalist) | KFRC (generalist) |
|---|---|---|---|---|
| 2009 to 2025, whole span | 6.6% | 2.4% | 8.6% | 4.4% |
| 2011 to 2020, between busts | 8.0% | -0.5% | 9.5% | 3.9% |
| 2021 to 2022, boom | 12.2% | 9.2% | 12.4% | 6.8% |
| 2024 to 2025, bust | -2.8% | -4.2% | 3.7% | 4.4% |

(Operating margins include impairments; RHI 2015 operating income untagged and excluded; RHI's SBC tag stops after
2013, so its owner-cash margin in `peers_table.txt` is overstated and is not used. Aya, Medical Solutions, CHG, Jackson
and the others are private: no filed figures.)

**VERDICT: OUT.** The castle is shown open on the evidence: low barriers stated by a competitor in its own 10-K, a
private entrant now the largest, a customer that buys through vendor-neutral procurement, a spread squeezed from both
sides, a moat rebuilt with acquisitions and written down by $547M, and margins narrowing across the segments. This is a
finding on the evidence, so OUT, not TOO HARD **[M2011-015]**; the three boxes are "in, out, and too hard"
**[M2006-013]**. Price does not reopen it: "What you can't do is turn any investment into a good deal by paying little"
**[M2019-015]**; "marginal businesses purchased at cheap prices may be attractive as short-term investments"
**[L2014-009]**, which is not this framework's game.

---
## Q3 to Q12: NOT REACHED
The file closed at Q2. Nothing below is a clearance. Facts gathered on the way are recorded for the record only:
- **Q3 (capital), fact only:** capital-light in plant (capex 1% to 3% of revenue), capital-heavy in acquisitions:
  $1,561M of acquisitions 2016 to 2025 against $2,174M of owner cash (OCF − SBC − capex) in the same ten years; owner
  cash after acquisitions averaged about $61M a year. Capex in 2025 ($35.6M) was below depreciation ($78.5M); the
  speakers call depreciation "almost always true costs" **[L2015-004]**.
- **Q4 (the numbers), fact only:** EBITDA is the featured measure (proxy: "$234 million in adjusted EBITDA"; 70% of the
  2025 bonus on "Pre-Bonus Adjusted EBITDA"); the speakers' view: "The one figure we regard as utter nonsense is the
  so-called EBITDA" **[M1998-086]**. The proxy's "$269 million in free cash flow" is operating cash flow before capex.
  Not taken further (two tells would have to be weighed at Q4; not reached).
- **Q5 and Q6, facts only:** CEO Cary Grace's 2025 total pay $10.67M with TSR -34% and adjusted EBITDA down 29%, bonus
  paid at 87% of target (proxy); directors and officers own 412,072 shares, about 1.1%. Buybacks: 12.6M shares at an
  average $89.04 since 2016, including 4.38M in 2023 at $96.90 (10-K note 11), with no stated price limit in the
  programme; 85,487 shares in May 2026 at $26.33 (10-Q). "what is smart at one price is dumb at another" **[L2011-003]**.
  No all-stock deal found; acquisitions were paid in cash.
- **Q9, fact only:** $750M of notes (4.000% due 2029, 6.500% due 2031), secured revolver $450M undrawn at 2026-06-30,
  covenant loosened twice, negative tangible equity, $20.8M letters of credit; wage-and-hour and contractor-classification
  exposures uninsured (10-K risk factors).
- **Q12 (optional), not asked.** Labor-disruption staffing (replacement clinicians during strikes) would be put to the
  newspaper test **[M2008-011]** if the file had reached it.

## COMPUTATION - NOT A CLEARANCE (the owner's reporting request; the file closed at Q2)
Inputs: owner cash = OCF − SBC − capex (filed cash-flow statements), after interest and after cash tax, so the value is
to equity; the rate 5.66%; shares 38.730M; tax for the pre-tax floor 25.9%, the filed 2023 effective rate
($73,610 / $284,289 thousand), the last year with ordinary pre-tax income. Script: `calc.py`.

**(a) VALUE RANGE by the Q7 convention** (five-year mean FY2021 to FY2025, $288.8M; shown growth on aggregate owner
cash 2021 to 2025 is -2.7% a year; ten years then zero nominal growth, at 5.66%): **$106.63 (shown growth) to $131.77
(no growth) a share, against $36.82.** Width 1.24 to 1. Depreciation variant (5-yr mean $212.3M, D&A including acquired
amortization): no-growth $96.84. This range is misleading for this name: the window holds the 2022 peak ($547.8M, 2.7
times 2025) and the 2023 to 2025 working-capital release, and it charges nothing for the acquisitions that bought the
growth.

**Whole-cycle variant** (CONVENTION of this run: the ten fiscal years 2016 to 2025, one full cycle from mid-cycle
through the pandemic boom to the trough; receivables were $342M at the start and $383M at the end, so working capital
nets out): mean owner cash $217.4M; **$80.27 (shown growth) to $99.20 (no growth)**. Fifteen years 2011 to 2025 (mean
$153.0M, two troughs): $56.47 to $69.79. After deducting the ten-year average acquisition spend ($156M a year): about
$61M a year, worth about $28 a share at no growth at 5.66%.

**Trough reading:** FY2025 operating cash flow before working-capital changes was $168.4M; less SBC $30.7M less capex
$35.6M gives $102.1M; less depreciation instead of capex, $59.2M. FY2025 itself held a large Q4 strike event.

**(b) FAIR PRICE** (central case: the ten-year whole-cycle mean, $217.4M after tax, zero growth; floor about 10%
pre-tax, CONVENTION of v5, on equity at the price paid, since owner cash is after interest; after-tax converted to
pre-tax at 25.9%): pre-tax owner cash $293.4M; **fair price about $75.76 a share** (equity $2,934M). On equity plus
net debt (EV basis, adding back about $45M of interest): about the same, since the debt is carried at its own rate.
At $36.82 the whole-cycle mean would yield 20.6% pre-tax on the price; the trough on the depreciation basis 5.6%.

**(c) CHEAP PRICE** (CONVENTION of this run: the price at which the worst recent full year, FY2025 on the depreciation
basis, $59.2M, pays the 10% pre-tax floor with no growth and no recovery; chosen because the speakers want the case
obvious "without" a pencil **[M1996-084]**, and an owner paid the floor even if the trough is permanent needs no
pencil): **about $20.63 a share.** On the capex basis ($102.1M) the same rule gives $35.58.

**Reading, which is not a verdict:** the price sits below the whole-cycle range and near the trough capex-basis line.
The market is pricing the trough as permanent. Q2 says the evidence does not let the analyst assume the 2016 to 2022
margins return, so the gap between price and whole-cycle value is the cigar butt's gap, the case Q2's stop excludes
**[M2019-015]**. The range across the three bases (trough $20.63 to five-year $131.77) is more than six to one, which
the Q7 convention would itself send to TOO HARD **[L2000-025]**.

---
## THE BOX
**OUT at Q2** (the castle shown open on the evidence). Not reached Q7; computation only: whole-cycle range $80.27 to
$99.20, fair about $75.76, cheap about $20.63, against $36.82.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. Written at the end rather than question by question: the session limit
  stopped the run during the peer cross-check with only the template on disk; nothing was committed (the brief forbids
  commits). Declared: the write-early rule was not met.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row
  (`idcheck.py`, PASS); no v4 or E id; filing facts carry accessions.
- [x] The order was kept; Q2 closed the file; nothing after it is a clearance; the computation is headed as such.
- [x] Owner cash from OCF less SBC less capex, never net income; sovereign from the Treasury; the price flagged as an
  aggregator quote.
- [x] Contrary evidence written down (Foundations) and answered at Q2.
- [x] Point-in-time: not a point-in-time test; no anchor rule applies.
- [x] Only `run.py` arithmetic lines used.
- [x] `python tools/check_framework.py` PASS (2026-10-06); `idcheck.py` PASS, 35 ids.
- Breach declared: one `grep` touched two other 2026-10-05 run files for a formatting string (see the contamination
  note).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Cyclical against changing.** Q1 routes "industries prone to rapid and continuous change" to TOO HARD, and Q1's
test 5 asks whether insiders would write the forecast down. Neither says what to do with a business whose type is
plain but whose earning power swings four times within four years for reasons nobody forecasts (pandemics, strikes).
I read cyclicality as understood and sent the question to Q2; a second analyst could close TOO HARD (NATURE) at Q1, and
the RHI run seen in the commit subjects did something like that. The framework should say whether a deep cyclical's
unforecastable amplitude is a Q1 matter or a Q7 matter (the width of the range). (2) **The Q7 convention's five-year
window** breaks on a name whose window holds a once-in-a-generation boom and a working-capital release: it produced a
narrow range at three times the price, which a mechanical reader would call a screamer. The convention has no
whole-cycle rule and no rule for working-capital reversal or for acquisitions as a cost of standing still; I added all
three as conventions of this run. (3) **Acquisitions in owner cash.** Q3 and Q4 say nothing on whether recurring
acquisitions that keep a moat from filling in are maintenance; for AMN that choice moves the whole-cycle owner cash from
$217M to $61M a year. (4) **The tax rate for the pre-tax floor** is not fixed by the framework; I used the last ordinary
filed effective rate. (5) The template's em dashes in its own headings conflict with the standing no-em-dash rule; the
headings here use colons and the protocol phrase is written with a hyphen.
