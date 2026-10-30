# Company Run: Lincoln Educational Services Corporation (NASDAQ: LINC), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated name before any fetch. Working folder:
`Test Runs/_research 2026-10-05 LINC/` (filings as text, `run_py.txt`, `cover.txt`, `rows.txt`, `peers/`).

**POSITION NOTE, declared before any verdict:** not checked. This run was dispatched under a blind rule that forbids
opening `PORTFOLIO.md`, any holding review, the session-state files, the run queue, the prepped reading list and any
other run file on this company. I did not open them and do not know whether the operator holds or wants this name.
**Contamination declared:** none from the forbidden files. `tools/run.py` printed its own v4 material beside the
arithmetic (a "yield" against the sovereign and a refusal line); only the arithmetic lines are used here (Part VII).
UTI's 10-K names Lincoln among its public competitors; that is a filing fact, not contamination.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $22.28 (2026-10-05; `tools/run.py`; **aggregator quote, live quote only, flagged** per operator rule 5).
- **Shares by class:** one class, Common Stock, no par value, **31,721,479** shares (10-Q for the period ended
  2026-06-30, filed 2026-08-10, cover page, accession `0001140361-26-031995`; `python Screens/cover_shares.py LINC`).
  No second class; the Series A preferred was mandatorily converted and none remains (10-K FY2025, note on equity).
- **Market cap:** 31,721,479 x $22.28 = **$706.8M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, US Treasury daily par yield curve, 30-year, 10/02/2026
  (issuing authority, via `tools/sources.py` inside `tools/run.py`).
- **Filings read** (operator rule 4), all from SEC EDGAR, CIK 0001286613:
  - 10-K FY2025, filed 2026-03-02, accession `0001140361-26-007380` (Items 1, 1A in part, 3, 7, 8: balance sheet,
    cash flows, lease and debt notes).
  - 10-Q Q2 2026, filed 2026-08-10, accession `0001140361-26-031995` (MD&A, liquidity, credit facility).
  - DEF 14A 2026, filed 2026-03-26, accession `0001140361-26-011290` (ownership, pay design, bonus metrics).
  - 8-Ks: 2025-12-23 `0001140361-25-046577` (employment agreements to 2028); 2026-04-16 `0001140361-26-014854`
    ($125M revolver to 2031); 2026-05-13 `0001140361-26-021084` (Melrose Park purchase agreement, $18.8M);
    2026-07-10 `0001140361-26-028230` (Melrose Park closed, $15.04M mortgage at 5.99% fixed five years).
  - History: 10-K FY2010 `0001140361-11-016427`; 10-K FY2013 `0001140361-14-012117`; 10-K FY2016
    `0001140361-17-011579`; 10-K FY2024 `0001140361-25-006937`; XBRL company facts (transcription only).
  - Competitor: Universal Technical Institute 10-K FY2025 (year to 2025-09-30), filed 2025-11-26, accession
    `0001261654-25-000025`, CIK 0001261654, and its XBRL company facts.
- **One figure cross-checked against the filed statement:** total assets at 2025-12-31, **$493,164 thousand**, in the
  filed Consolidated Balance Sheet (10-K FY2025, `0001140361-26-007380`) equals the `tools/run.py` table; cash
  ($28,519K) and stockholders' equity ($199,688K) also agree.
- **`tools/run.py` arithmetic lines only:** owner cash = (operating cash flow minus stock pay) minus capital spending
  (low end) or minus depreciation (high end), $M:

  | FY | OCF | SBC | D&A | capex | after all capex | after D&A |
  |---|---|---|---|---|---|---|
  | 2023 | 26 | 6 | 7 | 41 | -21 | 13 |
  | 2024 | 29 | 5 | 13 | 57 | -32 | 12 |
  | 2025 | 59 | 5 | 21 | 87 | -33 | 33 |
  | 3-yr mean | | | | | -29 | 19 |
  | 5-yr mean (FY2021-25) | | | | | -16 | 13 |

  Checked against the filed FY2025 cash-flow statement: OCF $59,311K, stock pay $5,488K, capital expenditures
  $86,633K, depreciation and amortization $19,161K plus finance-lease amortization $1,670K. Stock pay is deducted;
  operating lease rent is already inside OCF.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is "Would I be happy buying this stock if the market closed for five years?"
**[M1997-109]**, and for this company that question is really about the federal student-aid rules over those five
years, because Title IV funds "represented approximately 85% and 82% of our revenue on a cash basis during fiscal years
2025 and 2024" (10-K FY2025, MD&A). Who is paid to tell you also bears: the company pays about 286 recruiters and
spent $84.6M on sales and marketing in FY2025 (10-K FY2025), and the proxy leads its highlights with Adjusted EBITDA;
the row's words are "you do not get impartial advice" and "enormous amount of fees possible from one action"
**[M2020-037]**.
**Contrary evidence, written down as found** **[M1997-127]**, in the order found:
1. Demand is real and rising: starts 20,906 in FY2025 against 18,660 in FY2024; revenue $518.2M, up 17.8%; H1 2026
   revenue up 22.4% with average population up 16.3% (10-K FY2025; 10-Q Q2 2026).
2. The FY2022 cohort default rates of the existing institutions were zero, and none was at or above 30% for FY2020 or
   FY2021 (10-K FY2025). The filer itself attributes this to the repayment pause and expects rates to rise.
3. The DOE issued each institution a new program participation agreement without provisional certification; composite
   score 2.0 (10-K FY2025).
4. Tuition has risen about 2 to 3% a year while enrollment grew (10-K FY2025, MD&A), the shape of the pricing test
   "charge more for a product and maintain or increase market share" **[M2000-031]**. Read against item 6 below.
5. UTI, the nearest competitor, is also growing fast (starts 29,793 against 26,885; operating income $83.5M, FY2025):
   the demand for trades training is not Lincoln's alone.
6. Against item 4: the rising "gap" is financed by private loans and by Lincoln's own credit, and the provision for
   credit losses was $58.1M, 11.2% of revenue, in FY2025 (12.9% in FY2024). Part of each price rise is booked as
   revenue and written off as bad debt.
7. Lincoln's institutions are on the Sweet v. Cardona presumptive-relief list, which the DOE and the plaintiffs said
   rested on "strong indicia regarding substantial misconduct by the institutions, whether credibly alleged or in some
   instances proven" (10-K FY2025, Item 3, the company's own summary; the company contested it and has left the appeal).
   The Massachusetts Attorney General's 2015 consent judgment cost $850,000 plus $165,000 of forgiven student debt,
   with all wrongdoing denied (10-K FY2016). These go to Q5 and Q12, not reached.

## THE STANDING RULE
Nothing in the purchase as framed borrows, gives a call on the buyer or concentrates a ruin: the rule binds the buyer's
financing and sizing, "never going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. Not engaged by this run.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, found by "trying to identify the key variables in that particular
  business, and evaluating how predictable they were first" **[M1998-044]**.
- **The key variables, from the filings.** (1) Access to federal money: Title IV about 85% of cash revenue; 90/10
  percentages of 82.9% to 88.0% across the institutions against a 90% line (10-K FY2025). (2) Starts, which the filer
  says are driven by "the availability of financial aid", marketing, high-school graduates, "the job market and
  seasonality" (10-K FY2025, MD&A); UTI's filing calls this demand "counter cyclical". (3) Price against the public and
  apprenticeship alternatives. (4) Cost of acquiring and keeping a student: sales and marketing 16.3% of revenue, credit
  losses 11.2%.
- **Predictable or not.** (2), (3) and (4) are readable from the filings and the public record, and the business is
  simple: a campus, a program, a federally financed tuition. Variable (1) is a political forecast, and the filer will not
  write it down: on the OBBB Act "We cannot predict the timing and content of any rules", and on the new earnings-premium
  test "We cannot predict the timing, scope, and content of the final regulations [...] or how our programs will perform under the final metrics" (10-K FY2025). That is test 5 of
  Q1, whether the insiders would put the forecast "down on paper" **[M2000-105]**.
- **Why the file still passes Q1.** The unforecastable variable sets how bad the bad case is, not whether a protected
  return exists in the good case. Across both regimes on record (2009 to 2025) the competitive position can be read from
  the filings: in the best year the company earned an operating margin of 19% (FY2010 operating income
  $122.6M on revenue $639.5M, filed income statement, 10-K FY2010, `0001140361-11-016427`), and in today's
  favourable regime, with starts up double digits, it earns 5.8% ($30.3M on $518.2M, FY2025) and 3.4% in H1 2026. The
  financial statements do "tell me the information that’s useful" to judge where the competitive position will stand
  **[M2008-033]**, enough for Q2 to be answered on evidence. This is a narrow pass and is flagged under "What in the
  framework was wrong or unclear": the doubt rule **[M2002-092]** pulls the other way.
- **VERDICT: IN** (narrow), **[M2012-065]**, **[M1998-044]**, **[M2008-033]**.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now" **[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The castle tests, each with its filing fact.**
1. **The attacker with money** **[M2011-015]**, **[M2012-106]**. The filer answers it in its own words: "because
   schools can add new programs within six to 12 months, competition can emerge relatively quickly", and "each of our
   schools has at least three direct competitors and at least a dozen indirect competitors"; the industry is "highly
   competitive and highly fragmented with no one provider controlling significant market share" (10-K FY2025, Item 1,
   Competition). UTI's 10-K uses the same words for the industry. This is the row's failing answer: industries "that
   are just never going to have barriers to entry" **[M2012-106]**; "If the answer had been yes, we wouldn’t have done
   it." **[M2011-015]**.
2. **The low-cost position** **[M2018-043]**, **[M2004-091]**. Lincoln is the high-cost seller. Its own filing:
   "Public institutions are generally able to charge lower tuition than our schools" (10-K FY2025). Skilled-trades
   tuition $21,000 to $36,000 (10-K FY2025, Programs). Public record, **not a filing, flagged:** Dallas College, near
   Lincoln's new Rowlett campus, lists its Residential HVAC certificate at $3,888 for in-county residents
   (dallascollege.edu, via web search 2026-10-05); IBEW and NECA joint apprenticeships charge no tuition and pay the
   apprentice from the first week (IBEW local and NECA chapter pages, via web search 2026-10-05). UTI's 10-K adds that
   community colleges compete on "low tuition rates and in certain cases free tuition". The rows on the high-cost seller:
   "sooner or later, the nature of a capitalist society is that the guy with the lower cost comes in and kills you"
   **[M2001-013]**.
3. **Would the customer still choose it over the low bid?** **[M2017-009]**. The student chooses with someone else's
   money: about 85% of cash revenue is Title IV, and "the remainder was primarily derived from state grants
   and cash payments made by students", with
   the gap financed by private loans and company credit (10-K FY2025). The choice is bought with a recruiting force of
   about 286 representatives and $84.6M of sales and marketing (10-K FY2025) and is kept with a 17.7-to-1 teaching ratio,
   not with a premium the student pays from his own pocket. No filing fact shows students choosing Lincoln over the free
   or cheap alternative on their own funds.
4. **Pricing power and the agony before a rise** **[M2005-020]**. Tuition rises 2 to 3% a year; the increase widens the
   "gap" the company finances itself; credit losses run at 11.2% of revenue (FY2025) against 6.1% in FY2010 (10-K
   FY2010). The price is set inside the federal aid limits, and the new OBBB loan limits and the earnings-premium test
   are a ceiling written by Congress, not by the customer. This is not "incredible pricing power" **[M2010-092]**; it is
   the limit case reversed: the more the price rises, the more of it is not collected.
5. **Unit volume and share of mind.** Volume is up now (avg population 16,622, FY2025). Over the cycle it is not: average
   enrollment 31,535 and 45 campuses in FY2010 (10-K FY2010); 15,009 in FY2013 and 33 campuses (10-K FY2013); 11,864 and
   28 campuses in FY2016 (10-K FY2016); 22 campuses today. Referrals are "approximately 11.0% of our new student starts"
   (10-K FY2025), so nearly nine starts in ten are bought by marketing and recruiting.
6. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. The regulatory wall is moving in: 90/10 now counts VA
   money (the highest institution at 88.0%), OBBB loan limits from 2026-07-01, an earnings-premium test with July 1,
   2028 the first date a program could fail (10-K FY2025). Against it: no provisional certification today.
7. **Ask the competitors.** UTI, the one public pure peer, names Lincoln among its competitors and describes the same
   fragmented field and the same free public rival (UTI 10-K FY2025, Competition).
8. **What could destroy it** **[M2000-014]**. One political decision. 2010 to 2016 is the worked case below.

**The single fact that decides it: the castle fell the last time it was attacked.** Lincoln's operating income as first
reported in each year's own 10-K, FY2012 to FY2018: -$27.7M (`0001140361-13-012003`), -$9.6M (`0001140361-14-012117`),
-$48.5M (`0001140361-15-011951`), +$0.8M (`0001140361-16-057345`), -$5.2M (`0001140361-17-011579`), -$4.7M
(`0001140361-18-012880`), -$4.0M (`0001567619-19-006729`): **a cumulative operating loss of about $98.9M over seven
years, six of them losing years** (XBRL transcription of each filing's own figure; the FY2013 and FY2016 10-Ks were
read for the reasons: the Appropriations Act ended ATB enrolment, the company stopped fully online enrolment, and
the number of "potential students who are hesitant to incur debt" rose, 10-K FY2013 MD&A). Revenue went from $639.5M (FY2010) to $261.9M
(FY2017). This was not Lincoln alone: **UTI** lost money in each of its fiscal years 2015 to 2020, -$9.2M, -$18.6M,
-$1.8M, -$35.3M, -$7.8M, -$3.9M, cumulative about -$76.6M (UTI XBRL facts, consolidated operating income as filed in
its 10-Ks `0001261654-15-000042` to `0001261654-21-000073`). A business whose returns vanish across a whole industry
for six or seven years when one funding rule moves is not protected by a moat; it has "Roman Candles" in its history
**[L2007-004]**. The rows say competitors will "repeatedly assault" a castle "earning high returns" **[L2007-004]**:
Lincoln earned 19% operating margins at the 2010 peak, was assaulted by rule changes and by cheaper rivals, and
earned losses for seven years.

**The competitor row** (same metrics, each company's own filing):

| | Lincoln (FY Dec-2025) | UTI (FY Sep-2025) |
|---|---|---|
| Accession | `0001140361-26-007380` | `0001261654-25-000025` |
| Revenue | $518.2M | $835.6M |
| Operating income, margin | $30.3M, 5.8% | $83.5M, 10.0% |
| Federal share of cash revenue | Title IV ~85%; VA 4.8% | Title IV plus VA ~78% |
| 90/10 range by institution | 82.9% to 88.0% | ~67% to ~82% |
| Capex / D&A | $86.6M / $19.2M | $42.0M / $33.0M |
| Credit-loss provision / revenue | $58.1M, 11.2% | not located as a single figure; FY2025 increase of $13.6M cited in MD&A |
| Cumulative operating result in the downturn | FY2012-18: about -$98.9M | FY2015-20: about -$76.6M |
| Free or cheap rival named in filing | public institutions "lower tuition" | community colleges, "in certain cases free tuition" |

Lincoln is the smaller, higher-federal-share, lower-margin, higher-bad-debt of the two, and both fell together.

**VERDICT: OUT.** The castle is shown open on the evidence, not merely unjudgeable: the filer says entry takes six to
twelve months; the public rival is cheaper by an order of magnitude and the union rival pays the student; the customer
pays mostly with federal money and the company writes off 11.2% of revenue; and the last attack produced seven years of
cumulative operating losses for Lincoln and six for its nearest peer. "If the answer had been yes, we wouldn’t have done
it." **[M2011-015]**; "there are some industries that are just never going to have barriers to entry" **[M2012-106]**;
"the guy with the lower cost comes in and kills you" **[M2001-013]**. Price
does not reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**;
"marginal businesses purchased at cheap prices may be attractive as short-term investments, they are the wrong
foundation" **[L2014-009]**. Box: OUT **[M2006-013]**.

## Q3 to Q12: NOT REACHED
The first STOP that failed (Q2) closes the file. Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are NOT REACHED. Nothing
below is a clearance.

---
## COMPUTATION — NOT A CLEARANCE
*Recorded because the dispatch asked for the balance-sheet reading, owner cash and the facts behind the later
questions. No entry language; nothing here reopens Q2.*

**Owner cash.** Five-year mean (FY2021 to FY2025) after all capital spending: about **-$16M a year**; after depreciation
instead of capex: about **+$13M** (tool) to +$14M (my recomputation from the XBRL D&A tag). FY2025 alone: -$32.8M after
all capex; about +$33.0M after depreciation and finance-lease amortization. Capex was 16.7% of revenue in FY2025 and is
guided to about 12.1% in 2026 (10-K FY2025, MD&A); depreciation was about 3.7%. The filing does not separate maintenance
from growth capex; the campus build-outs (Nashville, Levittown, Houston, Hicksville, Rowlett, Suitland) are growth, and
"$22.5 million for educational equipment, real estate improvements, and information technology" in FY2025 reads as
closer to maintenance, which would put maintenance well above depreciation. That is my reading, not the filer's.

**The range, for the record only.** The Part VI construction cannot be built on the all-capex base (negative). On the
depreciation variant, the no-growth case is $13M to $14M / 5.63% = about $231M to $249M, **$7.30 to $7.85 a share**,
against $22.28; a shown-growth case is not computable on a five-year series whose sign changes. Operating income
$30.3M pre-tax on a $706.8M market value is 4.3%, under the 10% pre-tax floor convention **[M2003-149]** and under the
5.63% Treasury before tax. **The price at which no pencil would be needed: none is stated.** The business is OUT at Q2,
and the rows say price does not cure that **[M2019-015]**.

**The balance sheets, FY2016 to FY2025** (`tools/run.py` table, first-filed XBRL, filed statements read for FY2025):
- **Equity** fell from $54.9M (2016) to $39.9M (2018) as losses ran, then rose to $199.7M (2025); the 2020 jump
  ($43.1M to $91.1M) carried a tax-asset release (net income $48.6M on operating income $14.8M, FY2020). Retained
  earnings were negative until 2020 (-$44.1M at 2018).
- **Goodwill** $14.5M fell to $10.7M (impairment $3.8M on the Nashville sale, FY2023); immaterial.
- **Cash** peaked at $83.3M (2021) and fell to $28.5M (2025) as capex ran at 4x depreciation; at 2026-06-30 cash
  $44.2M with **$26.0M drawn** on the new $125M revolver, plus a $15.04M mortgage in July 2026 (10-Q Q2 2026; 8-K
  2026-07-10). The company that had no funded debt at year-end now borrows to build.
- **Leases are the debt.** Operating lease liabilities $172.7M and finance lease liabilities $31.1M at 2025-12-31,
  about **$204M against equity of $199.7M** (filed balance sheet); "We currently lease all of our campuses" (10-K
  FY2025, before the Melrose purchase).
- **Receivables**: current $36.9M net of a $44.0M allowance, noncurrent $21.2M net of a $26.4M allowance; gross student
  receivables about $128.5M, more than half reserved. Revenue is booked on credit the company expects not to collect.
- **Property** rose from $103.5M to $171.6M in one year (2025). Tenant allowance receivable $8.1M.
- What the figures cannot say **[M2025-032]**: whether the new campuses will fill before the 2028 earnings test, and
  what the DOE will do with the Sweet settlement recoupment ($1.4M of discharged loans already named for Massachusetts
  schools, 10-K FY2025).

**Facts that would have gone to Q4 to Q6 and Q12, recorded only.** The proxy leads with "Adjusted EBITDA of $67.1
million, up 58.7%" and pays 50% of the annual bonus and the performance shares on Adjusted EBITDA (DEF 14A 2026); the
row on featured adjusted figures is **[L2016-006]**. CEO total pay 2025 $3,999,717; CEO holds 897,997 shares plus
206,844 restricted (DEF 14A 2026), about 3.5% of the company. Chair John A. Bartholdson of Juniper Investment Company
(7.4% holder) is non-executive and independent of management. Buyback authorization of 2022 ($30M) unused in 2024 and
2025. Sweet v. Cardona listing and the Massachusetts consent judgment: see the foundations, item 7. 90/10 at 88.0% at
one institution: in FY2010 the Dayton institution was at 96.9% (10-K FY2010).

---
## THE BOX
**OUT**, decided at **Q2**: the castle is shown open on the filings (entry in six to twelve months by the filer's own
account; a public rival far cheaper and a union rival that pays the student; about 85% of cash revenue federal; 11.2%
of revenue written off; cumulative operating losses of about $98.9M over FY2012 to FY2018 for Lincoln and about $76.6M
over FY2015 to FY2020 for UTI when the funding rules moved). Not reached: Q7, so no range is set against the price as a
clearance; the computation above puts the no-growth case on the depreciation variant at about $7.30 to $7.85 a share
against $22.28. No research pass is opened: the box is OUT, not TOO HARD (WORK).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each:
      **not done.** The file was copied first, but the questions were written in one pass after the reading, and the
      dispatch forbade commits. Declared, not ticked.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script; no E-ids); every filing fact carries its
      document and accession; the two non-filing facts (Dallas College tuition, IBEW apprenticeship terms) are flagged.
- [x] The order was kept; Q2 closed the run; everything after it is under COMPUTATION — NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the US Treasury;
      the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, items 1 to 7).
- [x] No row dated after the anchor is cited (the run is dated today; no point-in-time anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` run after writing; result recorded in the session reply.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
**Q1 and a political key variable.** The Q1 routing sends to TOO HARD a business whose ten-year economics cannot be
foreseen because its industry changes fast (the framework's own routing sentence), and its rows are about technology. Here the unforecastable variable is
Congress and the Department of Education, and the filer itself will not write the forecast down (test 5,
**[M2000-105]**), which on its face is TOO HARD (NATURE) at Q1, while the doubt rule **[M2002-092]** says a doubt is a
no. I passed Q1 narrowly because the competitive position could be read across both regimes on record, and the
unforecastable variable changes only the depth of the bad case; Q2 then closed OUT on filed facts. A second analyst could
close at Q1 TOO HARD (NATURE) with equal fidelity to the text, and the two boxes differ in what follows (OUT is a
finding against the business; TOO HARD (NATURE) is not). The framework has no rule for a key variable that is a
government's decision rather than a market's change; it needs one, or an explicit statement that regulatory regime risk
is read at Q2 test 11 ("what could destroy") and not at Q1. A second, smaller gap: the dispatch asked for the
balance-sheet reading and owner cash, which belong to Q4 and Q7; after a Q2 OUT the template has no place for them, so
they are recorded under the protocol's COMPUTATION — NOT A CLEARANCE heading.
