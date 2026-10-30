# Company Run: Robert Half Inc. (NYSE: RHI), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run form: the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated name before any fetch. Every judgment cites a v5
ledger id in bold; every filing fact carries its accession. Working folder: `Test Runs/_research 2026-10-05 RHI/`
(raw filings, text conversions, `fetch.py`, `facts_series.py`, `value_calc.py` and its output `value_calc_output.txt`,
`peers/peer_series.py`).

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is closed to this run by its blind rule, so
whether the operator holds RHI is unknown to the analyst. The run is written as for a name not held.

**CONTAMINATION DECLARED.** (1) The session context showed the subjects of four recent commits, v5 runs of PRKS, TDS,
CENT and OGN, with their boxes and prices; none concerns RHI or a staffing company. (2) The git status listed three
untracked run files dated 2026-10-05 (CALY, PBH, SKYW) by file name only; none was opened. (3) The analyst's memory
index says, in general terms, that the watchlist has many gate-clearers and "nothing buyable"; it carries nothing on RHI.
(4) `tools/run.py` printed only arithmetic lines for RHI; no v4 rule, id or verdict was used. No `Test Runs/` file on RHI
exists (directory listing, 2026-10-05) and none of the barred files was opened.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $34.34 (2026-10-05, live quote printed by `tools/run.py`; aggregator, flagged per operator rule 5).
- **Shares, one class:** 102,361,828 common, cover of the 10-Q for the quarter to 2026-06-30, filed 2026-08-04,
  accession `0000315213-26-000046` (`python Screens/cover_shares.py RHI`; the balance-sheet count at 2026-06-30 is the
  same figure). No other class: preferred authorized, none issued (10-K FY2025, `0000315213-26-000006`).
- **Market cap:** about $3,515M (102.36M x $34.34).
- **Sovereign, USD:** 5.66%, US Treasury daily par yield curve, 30-year, 10/05/2026 (as fetched by `tools/run.py`
  from the Treasury, the issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 filed 2026-02-13 `0000315213-26-000006` (Business, Risk Factors,
  MD&A, all primary statements, segment note); 10-Q Q2 2026 filed 2026-08-04 `0000315213-26-000046` (MD&A, cash flow,
  equity); proxy DEF 14A filed 2026-04-10 `0000315213-26-000010` (pay tables, succession, Chairman's agreement); 8-Ks
  `0000315213-26-000043` (2026-08-03, Protiviti chief executive succession), `0000315213-26-000014` (2026-04-20,
  severance amended), `0000315213-26-000029` (2026-05-13, stock plan and vote), `0000315213-25-000057` (2025-05-29,
  $100M credit agreement). For the long span: 10-K FY2024 `0000315213-25-000007`, FY2023 `0000315213-24-000011`,
  FY2022 `0000315213-23-000016`, FY2019 `0000315213-20-000029`, FY2018 `0001628280-19-001488`, FY2015
  `0001628280-16-011322`, FY2010 `0001193125-11-038990`, FY2007 `0001193125-08-034558`, FY2005 `0001193125-06-046180`,
  FY2002 `0001047469-03-010372` (selected financial data and segment notes, 1998 to 2025).
- **One figure cross-checked against the filed statement:** net cash from operations FY2025 $319,965k in the filed
  cash-flow statement (`0000315213-26-000006`) against 320.0 printed by `tools/run.py`; capital expenditures $53,155k
  against 53.2; stock-based compensation $59,416k against 59.4. All three agree.

### `tools/run.py` arithmetic, checked line by line, and what it leaves out
`tools/run.py` prints OCF less SBC less capex for 2023 to 2025 (529.9, 290.7, 207.4; $M) and a five-year variant
(431.9). Each line agrees with the filed statements, but the figure is not yet owner cash after every real cost, for one
reason the filing states and the tool does not see:

**The deferred compensation trust, separated.** Employees defer pay into a plan; the company funds a trust that mirrors
their choices. Trust gains are booked as "Income from investments held in employee deferred compensation trusts"
($106.1M in 2025, $94.1M in 2024, $88.0M in 2023) and the equal rise in the obligation is booked in SG&A and, for
Protiviti, in costs of services, "leaving no net costs to the Company, and therefore no effect on reported net income"
(10-K FY2025, MD&A, `0000315213-26-000006`). So pre-tax income is clean of the trust, but reported operating income is
not (it carries the obligation charge without the offsetting income; 2025 operating income $76.5M reported against
$182.6M "adjusted"). In cash, the deferred pay sits in operating cash flow as a rising obligation (+$93.2M in 2025)
while the money the company puts into the trust leaves in investing ($80.1M in, $58.3M redeemed in 2025). The deferred
pay is a real compensation cost paid into a trust the owners do not control, so this run deducts the **net trust
funding** from owner cash. `tools/run.py` does not.

Other lines checked: cloud-computing implementation spending ($28.5M in 2025) is already an outflow inside operating
cash flow, so it is not deducted twice; depreciation ($50.0M) is close to capex ($53.2M), so the capex and depreciation
bases give the same five-year mean; acquisitions were small ($10.7M in 2025, $19.0M in 2022) and are not deducted.

**Owner cash after every real cost** (OCF less stock pay less capex less net trust funding; $M; filed cash-flow
statements in the accessions above; computed in `value_calc.py`):

| year | OCF | stock pay | capex | net trust funding | **owner cash** |
|---|---|---|---|---|---|
| 2016 | 442.1 | 42.7 | 83.0 | 27.1 | **289.3** |
| 2017 | 453.0 | 42.2 | 40.8 | 36.6 | **333.5** |
| 2018 | 572.3 | 45.0 | 42.5 | 46.0 | **438.9** |
| 2019 | 519.6 | 48.3 | 59.5 | 42.7 | **369.2** |
| 2020 | 596.5 | 52.5 | 33.4 | -58.7 | **569.3** |
| 2021 | 603.1 | 55.9 | 36.6 | 51.0 | **459.6** |
| 2022 | 683.8 | 57.7 | 61.1 | 36.5 | **528.4** |
| 2023 | 636.9 | 61.1 | 45.9 | 65.3 | **464.5** |
| 2024 | 410.5 | 63.4 | 56.3 | 30.5 | **260.2** |
| 2025 | 320.0 | 59.4 | 53.2 | 21.8 | **185.6** |

Five-year mean (2021 to 2025): **$379.7M**. Ten-year mean (2016 to 2025): **$389.9M**. First half 2026: operating cash
flow was **-$4M** (10-Q `0000315213-26-000046`), against $60M a year earlier. Two warnings on the table: (a) receivables
release cash in a fall (+$156.3M in 2023, +$67.0M in 2024, +$45.8M in 2025) and absorb it in a rise (-$292.6M in 2021),
so the down years are flattered and 2021 is penalised; (b) 2020 holds a net trust redemption and pandemic payroll
deferrals, an abnormal year.

### The balance sheets, ten year-ends, read before the income account (Q4's rule, read here because the file closes at Q1) **[M2025-032]**
Figures from `tools/run.py`'s ten-year table, read against the filed balance sheets of FY2025 and FY2022 ($M):

| year-end | equity | goodwill | cash | receivables | debt | retained earnings |
|---|---|---|---|---|---|---|
| 2016 | 1,087 | 210 | 260 | 703 | 1 | 85 |
| 2019 | 1,144 | 210 | 270 | 833 | 0 | 36 |
| 2021 | 1,381 | 223 | 619 | 985 | none | 168 |
| 2022 | 1,569 | 238 | 659 | 1,018 | none | 319 |
| 2023 | 1,588 | 238 | 732 | 861 | none | 266 |
| 2024 | 1,378 | 237 | 538 | 772 | none | 25 |
| 2025 | 1,276 | 251 | 464 | 748 | none | 0 |

What the figures say: no debt in any year (the FY2002 data show $2.5M of "debt financing"; the 2025 credit line of $100M
is undrawn, with $10.1M of letters of credit for a workers' compensation insurer); goodwill small (about a fifth of
equity) and moving only with small purchases; receivables steady against sales (13.4% of 2016 revenue, 13.9% of 2025),
so no sign of revenue booked ahead of cash; the deferred compensation trust assets ($773.9M) slightly exceed the
obligation ($771.6M) at 2025. Equity is small against earnings because nearly everything is paid out: retained earnings
reached zero in 2025 and $164.7M of the 2025 dividend was charged to paid-in capital (statement of stockholders' equity,
`0000315213-26-000006`). What they do not say: the castle. A business that needs about $1.0B of tangible equity
(2025: $1,276M less $251M goodwill) earned $897M pre-tax on about $1.33B in 2022 and $194M on about $1.02B in 2025; the
capital is light, and what decides the value is the volume of hours sold, which no balance sheet shows. No suspicion,
no confusion; the one presentation to keep apart is the trust (above).

### The long span: revenue and pre-tax income from the filings, 1998 to 2025 ($M)
| year | revenue | pre-tax | margin | note |
|---|---|---|---|---|
| 2000 | 2,699 | 301.6 | 11.2% | peak |
| 2002 | 1,905 | 3.5 | 0.2% | trough; revenue -29% from 2000; temp staffing segment $47.4M (2.7%), Protiviti -$35.4M |
| 2003 | 1,975 | 11.7 | 0.6% | |
| 2005 | 3,338 | 392.2 | 11.7% | new high by 2005 |
| 2007 | 4,646 | 490.4 | 10.6% | |
| 2009 | 3,037 | 66.8 | 2.2% | trough; revenue -35% from 2007; temp staffing $104.5M (4.2%), Protiviti -$30.8M |
| 2010 | 3,175 | 115.2 | 3.6% | |
| 2015 | 5,095 | 581.0 | 11.4% | |
| 2019 | 6,074 | 625.5 | 10.3% | |
| 2021 | 6,461 | 803.8 | 12.4% | |
| 2022 | 7,238 | 897.0 | 12.4% | peak |
| 2023 | 6,393 | 576.6 | 9.0% | contract hours -20.8% |
| 2024 | 5,796 | 357.7 | 6.2% | contract hours -14.6% |
| 2025 | 5,379 | 194.4 | 3.6% | contract hours -14.1%; contract talent segment $48.6M adjusted (1.6%) |

Sources: selected financial data and segment notes in the 10-Ks listed above; pre-tax rather than operating income
because the trust presentation changed and pre-tax is unaffected by it. Margins are this run's division.

---
## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own Robert Half "if the market closed for five years?" **[M1997-109]**. The
question that answers it is not the price but the hours: what the business sells is hours of accountants, clerks,
administrators, programmers and auditors, and the run turns on whether those hours will be bought from it in ten years.
The market "just tells us prices" **[M2006-077]**; a price down from about $71 (the 2024 repurchases) to $34.34 tells
nothing about that. The analyst's habit for this name: look for "what you’re missing" **[M2025-013]**, and avoid the
anchor of a "previous conclusion" **[M2016-054]**, here the pre-2023 picture of a superior, debt-free staffing firm that
always came back.

**Contrary evidence, written down as found** **[M1997-127]**:
- Against the close below (evidence for IN): the firm has sold the same service since before the filings begin; in both
  earlier troughs the temporary staffing segment stayed profitable (2002, 2009) and revenue reached new highs within
  three to five years; no debt in any year read; pre-tax margins above every staffing peer in the comparison (Kforce,
  ManpowerGroup, Kelly) for 2010 to 2023; bill rates rose in each of 2023 to 2025 and in the first half of 2026 (+1.8%), and permanent placement
  fees rose 5.1% in that half, so price held while volume fell; the decline slowed to -3.1% in the first half of 2026;
  management writes that AI "continues to complement" the professionals it places (10-Q `0000315213-26-000046`).
- Against the business (evidence for OUT): the filer's own words, "because it is a service business, the barriers to
  entry are quite low" and "The most significant competitive factors in the staffing business are price and the
  reliability of service" (10-K FY2025); contract hours fell about 42% from 2022 to 2025 (three filed declines
  compounded) while the filer reports US unemployment at 4.4% and college-educated unemployment at 2.8%; the 2025
  contract talent margin (1.6% adjusted) sits below the 2002 (2.7%) and 2009 (4.2%) recession troughs; RHI's pre-tax
  margin (3.6%) fell to Kforce's operating margin (3.8%) in 2025; Protiviti's billable hours fell 19.9% in Q2 2026 and
  it took "cost reduction charges"; dividends ($238.2M) exceeded owner cash ($185.6M) in 2025 and first-half 2026
  operating cash flow was negative.

## THE STANDING RULE
A purchase of a listed stock paid in cash, at a size the buyer can hold through a fall of half, puts no one at risk of
ruin; "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and none is contemplated. The rule is
not engaged by this name.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The product is easy
to understand; the question is the economics: "we understand the product. We understand what it does for people. We just don’t
know the economics of it 10 years from now." **[M2000-104]**.

**The key variables** **[M1998-044]**, from the filing's own words (10-K FY2025, MD&A, `0000315213-26-000006`):
contract talent (55.6% of 2025 revenue), "average hourly bill rates and the number of hours worked"; permanent placement
(8.2%), "the number of candidate placements and average fees earned per placement"; Protiviti (36.2%, of which $485.2M,
a quarter, is Robert Half contract talent resold through Protiviti per the segment note), "the billable hours worked on
client engagements and average hourly bill rates". Price per hour has held. **The variable that decides the value is
the number of hours sold.**

**Is the hours variable foreseeable ten years out?**
1. *Until 2022 it moved with the employment cycle, and that was foreseeable.* Revenue fell 29% from 2000 to 2002 and 35%
   from 2007 to 2009, each time with a recession, and each time recovered to a new high (2005, 2014), per the selected
   financial data above. A cyclical business with a stable volume trend is one whose statements tell the future ones
   **[M2008-033]**.
2. *Since 2022 it has not moved with the cycle.* Contract hours fell 20.8% (2023), 14.6% (2024), 14.1% (2025)
   (10-Ks `0000315213-24-000011`, `0000315213-25-000007`, `0000315213-26-000006`) and 5.0% in the first half of 2026
   (`0000315213-26-000046`); contract talent revenue of $2.99B in 2025 was below the $3.37B of 2013 in nominal dollars
   (FY2015 10-K segment note). Over the same span the filer reports real GDP rising and unemployment at 4.4%, and writes
   that "job openings continue to be well above historical levels". No three-year fall in volume without a recession
   appears anywhere in the 1998 to 2025 record read. Something besides the cycle is at work, and the filings do not say
   what.
3. *The filer names the candidate, and does not forecast it.* Risk factors (10-K FY2025): "The increased availability
   and maturation of AI tools may enable clients to use advanced automation capabilities in lieu of services provided by
   the Company’s contract talent personnel." And: "Technological advances such as AI, machine learning and automation are
   impacting industries served by all of the Company’s lines of business." Against that, the Q2 2026 MD&A: AI "continues
   to complement" the professionals the Company places. The hours sold are hours of finance and accounting, technology,
   administrative and customer-support work and of internal audit and consulting, the work these tools are built to do.
   The filer also writes that "Because long-term contracts are not a significant part of the Company’s business, future
   results cannot be reliably predicted by considering past trends".
4. *Ask the insiders* **[M2000-105]**. The industry's own filers disagree in writing, and none writes a number. Kforce
   (10-K FY2025, `0000930420-26-000007`): "we believe that AI and other innovative technologies will continue to drive
   higher levels of demand for technology resources". ManpowerGroup (10-K FY2025, `0001193125-26-064113`): "The rapidly
   increasing deployment of AI technology by our customers may lead to reduced demand for our services and solutions"
   and "some services and tasks currently performed by our associates may be replaced by AI automation". Robert Half:
   both sentences quoted in point 3. Three insiders, three readings, no forecast of the hours.
5. *How far off could I be?* **[M2011-084]**. The five-year owner cash runs from $528M (2022) to $186M (2025); the
   honest model of ten years out runs from a cyclical recovery to the 2013 level of volume and beyond, to a business
   whose core hours keep shrinking. The two ends of the arithmetic below differ by 4.5 to one.

**Is the question important and knowable?** It is the whole value: at flat hours the five-year owner cash is worth about
$65 a share at the sovereign; at the shown decline about $15 (Computation, below). Important, and on the evidence of the
filers themselves, not knowable: "If something’s important but unknowable, forget it." **[M2006-076]**. Change is the
enemy of the forecast: "whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going
to pass on that" **[M1999-063]**; "where we think the future technology could hurt the business as it presently exists
[...] it won’t make it through the filter" **[M1998-008]**. The change here is in the customers' own work, and it may
come slowly: "slow change can be much harder to perceive, and can lull you to sleep easier" **[M2014-038]**. And the
doubt rule: "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.

**Routing.** The framework (Q1, The routing, fixed) sends to TOO HARD at Q1 a business whose ten-year economics
cannot be foreseen because its industry changes fast. Robert Half is not a technology company; its customers' adoption of a
technology may remove the demand for its product. The run reads that as the routing's case: the forecast cannot be made
for the reason the rows give, "a business that must deal with fast-moving technology is not going to lend itself to
reliable evaluations of its long-term economics" **[L1993-023]**. Q2's castle tests are not reached.

**The cause: NATURE, not WORK.** The test between them is whether the insiders would write the forecast down
**[M2000-105]**; they do not, and they contradict one another (point 4). "in other cases the nature of the industry
would be the roadblock" **[L1993-023]**; the problem is one "which we can't solve by studying up" **[L1999-018]**. Why
not WORK: the work that could be done (separating cycle from structure in the 2023 to 2026 hours, by peer hours, the
government's temporary-help series, customers' accounting headcount) answers what has happened, not what the hours will
be in 2036; even a clean finding that 2023 to 2026 was cyclical would leave the ten-year path of AI in accounting,
administrative and audit work unforecast. "we’re not going to learn enough in the followings five months to make up for
the fact that we went in deficient in the first place." **[M2008-086]**. What would have made it WORK: a filer, or the
industry, writing a supportable long-run figure for the hours, or a record showing volume tracking the cycle through
2023 to 2026. Neither exists in the filings read.

**VERDICT: TOO HARD (NATURE).** "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of
its worth. It just means that we don’t know how to evaluate it." **[M2000-038]**. The box is "too hard" **[M2006-013]**;
a lower price does not reopen it.

## Q2: WHY IS THE CASTLE STILL STANDING? STOP.
**NOT REACHED** (Q1 closed the file). The competitor row the template asks for was gathered before the close and is
recorded under COMPUTATION below as evidence, not as a verdict.

## Q3: HOW MUCH CAPITAL MUST GO IN? WEIGHING.
**NOT REACHED.**

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion.
**NOT REACHED** as a verdict. The ten-year balance-sheet reading and the trust separation are done in Step 0; nothing
found there was confusing or suspicious.

## Q5: WHO RUNS IT? STOP on integrity.
**NOT REACHED.** Facts gathered are recorded below.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts gathered are recorded below.

## Q7: WHAT IS IT WORTH? STOP.
**NOT REACHED.** The owner's requested figures are below, under COMPUTATION: NOT A CLEARANCE.

## Q8: IS IT BETTER THAN THE ALTERNATIVES? STOP.
**NOT REACHED.**

## Q9: COULD IT RUIN US? WEIGHING.
**NOT REACHED.** (Fact only: no debt; $100M undrawn line; leases $245.5M; purchase obligations $221M.)

## Q10: IS IT THE FAT PITCH? WEIGHING.
**NOT REACHED.** What the draft would have the buyer do: nothing; the box is closed.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** No named business is involved.

---
## COMPUTATION: NOT A CLEARANCE
*(Operator rule 3. The file closed at Q1. Every figure below is arithmetic reported at the owner's request; none is a
clearance, an entry price or a recommendation. The protocol's heading carries a dash the house style does not use; the
colon stands in for it.)*

### The competitor row, from the competitors' own filings (would have been Q2's)
Margin on revenue, by year: RHI pre-tax income over revenue (its operating line is distorted by the trust presentation,
Step 0); the others operating income over revenue, XBRL as last filed, transcription only. Korn Ferry's fiscal year ends
in April and is shown in the calendar year it starts. Accession of the last filing carrying each figure:
KFRC `0000930420-26-000007`, KFY `0000056679-26-000021`, MAN `0001193125-26-064113`, KELYA `0000055135-26-000053`,
NSP `0001000753-26-000011` (latest three years; earlier years from earlier 10-Ks, listed in `peers/peer_series.py`
output).

| year | RHI | Kforce | Korn Ferry | ManpowerGroup | Kelly | Insperity |
|---|---|---|---|---|---|---|
| 2009 | 2.2% | 2.5% | -0.5% | 0.3% | -3.4% | 1.6% |
| 2012 | 8.4% | -6.5% | 5.2% | 2.0% | 1.3% | 3.1% |
| 2015 | 11.4% | 5.6% | 3.9% | 3.6% | 1.2% | 2.5% |
| 2019 | 10.3% | 5.6% | 8.9% | 3.1% | 1.5% | 4.3% |
| 2021 | 12.4% | 6.7% | 17.8% | 2.8% | 1.0% | 3.5% |
| 2022 | 12.4% | 6.8% | 11.0% | 2.9% | 0.3% | 4.2% |
| 2023 | 9.0% | 5.7% | 7.6% | 1.4% | 0.5% | 3.4% |
| 2024 | 6.2% | 5.0% | 12.5% | 1.7% | -0.3% | 1.8% |
| 2025 | 3.6% | 3.8% | 12.8% | 0.8% | -1.6% | -0.1% |
| revenue 2022 to 2025 | -25.7% | -22.3% | +2.6% | -9.4% | -14.4% | +14.7% |

Read over the whole span, not one year: RHI earned well above the staffing peers (Kforce, Manpower, Kelly) in every year
from 2010 to 2023, which is the record of an advantage of some kind in its niche; in 2025 the gap to Kforce, the nearest
peer in kind, closed. Korn Ferry (executive search and consulting) and Insperity (a payroll and benefits outsourcer) are
not like-for-like; Korn Ferry's margin rose while the staffing names fell. The two professional staffing firms that sell
the same hours (RHI, Kforce) fell together, which points to the demand for the hours, not to RHI's own execution.

### Money and owners (would have been Q6's; facts only)
- **Paid out against owner cash, 2016 to 2025:** repurchases $2,428.2M and dividends $1,697.5M (XBRL, filed cash-flow
  statements), together $4,125.7M against owner cash of $3,898.5M (table above): 106% paid out. In 2025 dividends alone
  ($238.2M) exceeded owner cash ($185.6M) and net income ($133.0M). Dividend now $0.59 a quarter (10-K FY2025).
- **Repurchase prices:** 2024, 3.5M shares for $249M (about $71 a share); 2025, 1.7M shares for $80M (about $47); first
  half 2026, none on the open market (10-Q). The authorization is a share count (5.6M remaining) with no stated price.
  Against the range below ($14.63 to $65.53), the 2024 purchases sit above its top and the 2025 purchases inside it.
  Shares outstanding fell from 127.8M (2016) to 101.1M (2025); 132.4M shares bought since 1997 (10-Q).
- **Stock pay:** $59.4M in 2025, 32% of that year's owner cash; equity grants to executive officers are 100% performance
  shares on three-year relative ROIC and relative TSR (proxy `0000315213-26-000010`). Chief executive M. Keith Waddell,
  2025 total $6.07M by the Summary Compensation Table; annual bonus targets set on net income and revenue; compensation
  consultant FW Cook.
- **Succession:** Waddell (69) chief executive since December 2019; Harold M. Messmer, Jr. (80) chief executive 1987 to
  2019 and Chairman since 1988, on an employment agreement to 2027-12-31; the proxy states a chief executive succession
  plan reviewed annually. Protiviti's chief executive Joseph A. Tarantino hands over to Cory S. Gunderson on 2027-01-01
  (8-K `0000315213-26-000043`). Severance agreements amended 2026-04-20 to remove the walk-away right after a change in
  control (8-K `0000315213-26-000014`).

### (a) VALUE RANGE, by the Q7 convention, at the 5.66% sovereign
Construction (the framework's CONVENTION): five-year mean owner cash after every real cost, carried at the growth shown
on the aggregate (never above it) for ten years, then zero nominal growth, discounted at the long government rate; the
two ends are the no-growth and shown-growth cases. Shown growth, 2021 to 2025, endpoint to endpoint on aggregate owner
cash: -20.3% a year.
- **No-growth end:** $379.7M flat: $6,708M, **$65.53 a share.**
- **Shown-growth end:** $379.7M falling 20.3% a year for ten years, then flat: $1,497M, **$14.63 a share.**
- **Range $14.63 to $65.53 against $34.34**, 4.5 to one: wider than the three-to-one line, so had Q7 been reached it
  would have closed TOO HARD on width alone.
- **Whole-cycle variant** (the five-year window holds the 2021 to 2022 peak and the 2024 to 2025 trough, so it is not a
  normal window): ten-year mean $389.9M (2016 to 2025, which holds the 2020 shock, the peak and the trough), shown growth
  2016 to 2025 -4.8% a year: **$46.11 to $67.29 a share**, 1.5 to one.
- Net cash of $464.4M ($4.54 a share) is left out of both: part of it carries the weekly payroll against $748M of
  receivables, and the convention values the cash stream only.

### (b) FAIR PRICE
**About $39.50.** The central case (CONVENTION of this run; the framework names no central case): the ten-year
whole-cycle mean owner cash, $389.9M, carried at the ten-year shown growth, -4.8% a year, for ten years, then flat. That
is the cycle the filings show, at the growth they show and not above it. **Tax treatment:** owner cash is after cash
taxes; it is grossed up to pre-tax at 30% (CONVENTION of this run; the filed effective rates were 31.6% in 2025 and
29.7% in 2024) and the pre-tax stream is discounted at 10%, the floor convention. Below $39.53 the central case clears
about ten percent pre-tax. At $34.34 it returns about 11.7% pre-tax; on the 2025 run-rate held flat, about 7.5%; on the
five-year shown decline, about 2.5%. The answer moves with the hours, which is the Q1 finding in numbers.

### (c) CHEAP PRICE
**About $14.60.** Rule (CONVENTION of this run): the lower of the bottom of the five-year convention range at the
sovereign ($14.63) and the price at which the worst case the filings show (the five-year mean falling 20.3% a year for
ten years, then flat) still returns 10% pre-tax ($15.50). Below that, even the worst shown path pays the floor without a
pencil. The price is more than twice it.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the value turns on the number of finance, accounting, administrative,
technology and audit hours clients will buy from Robert Half in ten years, and since 2022 those hours have fallen about
42% without a recession while the industry's own filers write opposite views of AI's effect on them and no forecast.
The deciding question is not knowable by more work. (Computation only: range $14.63 to $65.53 at the sovereign,
whole-cycle $46.11 to $67.29, fair about $39.50, cheap about $14.60, against $34.34.) No research file is opened: NATURE
is the closed box. Q11 belongs to a holding review, not to this run.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Committed after each question: **not done**; this session was
      instructed not to commit, so the file was written whole at the end of the reading rather than question by
      question.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (Python check run; see the last box); every filing fact has its
      accession; numbers are from filings, from `tools/run.py`'s arithmetic lines, or from this run's labelled
      computation.
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance; all valuation is under
      COMPUTATION.
- [x] Owner cash after every real cost (stock pay and the deferred-compensation trust funding deducted), never a
      net-income proxy; the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down **[M1997-127]**, both ways, in the Foundations section.
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its owner-earnings line was corrected for the trust.
- [x] `python tools/check_framework.py` run after writing: PASS. A Python check (`_research 2026-10-05 RHI/check_ids.py`)
      found no em dashes, no v4 E-ids, every cited M/L/R id in the v5 ledger, and every quoted fragment beside an id
      inside that id's row.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1's routing names an industry that changes fast; it does not say whether a change in the customers' work
counts.** Robert Half is not a technology business; a technology adopted by its customers may remove the demand for its
product. The run read this as the routing's case through **[L1993-023]** and **[M1998-008]** ("could hurt the business
as it presently exists"), but a second analyst could send the same facts to Q2 and close OUT on the filer's "barriers to
entry are quite low", or to TOO HARD at Q2. A sentence in Q1 on demand-side technological change would settle it.
(2) **The NATURE test assumes insiders either write the forecast down or call it too hard.** Here they write
contradictory qualitative views (Kforce: more demand; ManpowerGroup: reduced demand; RHI: "complement", with a risk
factor saying the opposite) and no number. The run read disagreement without a number as "would not write it down"; the
framework does not say so. (3) **The Q7 convention with a negative shown growth.** "Never above" the shown growth, on a
five-year window that starts at a peak, carries -20.3% a year for ten years, close to a liquidation path, and makes the
range 4.5 to one by construction; the convention does not say whether a window opening on a peak is a normal window, and
the owner's "central case" for a fair price is not defined anywhere in the framework (this run confessed its own).
(4) **`tools/run.py` omits the deferred compensation trust funding**, which sits in investing while the deferred pay
inflates operating cash flow; a company with a large employee deferral plan is overstated by the tool's owner-earnings
line ($21.8M to $65.3M a year here). (5) **Operator rule 3's heading contains a dash** that the operator's style rule
forbids; the run wrote "COMPUTATION: NOT A CLEARANCE". (6) The template's instruction to read the Q4 balance sheets in
Step 0 when the file closes earlier is in the run brief, not in the template; the run followed the brief.
