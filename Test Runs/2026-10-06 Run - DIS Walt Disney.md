# Company Run: The Walt Disney Company (NYSE: DIS), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md` was not
opened, so whether the operator holds DIS is unknown to the analyst. The run is written as for a name not held.

**CONTAMINATION DECLARED.** (1) Listing `Test Runs/` for the v5 form showed that a file named
`2026-09-19 Run - DIS Walt Disney.md` exists. Its name was seen; it was not opened, and nothing in it is known to this
run. (2) The session's opening commit log showed the subjects of the last five commits (S&P 600 screen runs, tool fixes,
session state); none names DIS. (3) One other company's v5 run (CAG, 2026-10-05) was read for form only. (4) `tools/run.py`
prints v4 material; only its arithmetic lines are used (Part VII). (5) The analyst's training memory holds Berkshire's
history with this company (the 1967 sale, the Capital Cities merger of 1996) and Disney's public history to mid-2025.
The ledger rows that name Disney were found by a text search of `principle_ledger_v5.csv` during this run and are cited
as rows, not as memory. Every company fact used below is from a filing with its accession.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $103.61 (2026-10-05, the live quote printed by `tools/run.py`; an aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: **1,726,686,902** common shares, $0.01 par, one class (10-Q for the
  quarter ended 2026-06-27, filed 2026-08-05, accession `0001744489-26-000057`; `python Screens/cover_shares.py DIS`,
  cover as of 2026-07-29).
- **Market cap:** $103.61 x 1,726.69M = **$178,902M**.
- **Debt beside it** (10-Q balance sheet, 2026-06-27): current portion of borrowings $8,627M, borrowings $37,414M,
  total **$46,041M**, against cash and cash equivalents of $5,185M. Noncontrolling interests in equity $6,810M.
- **Sovereign for the earnings currency (USD):** **5.66%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-05 (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K for the fiscal year ended 2025-09-27, filed 2025-11-13,
  `0001744489-25-000155` (business, risk factors, MD&A by segment, cash-flow statement, commitments note); 10-Q for the
  quarter ended 2026-06-27, filed 2026-08-05, `0001744489-26-000057` (segment results, cash flows, capital spending,
  balance sheet); 8-K of 2026-08-05 with the EX-99.1 earnings release, `0001744489-26-000056`; 8-K of 2025-11-13 with the
  FY2025 release, `0001744489-25-000154`; 8-K of 2026-02-03 (CEO succession), `0001744489-26-000022`; 8-Ks of 2026-02-24
  `0001744489-26-000025` and 2026-03-20 `0001628280-26-020172`. The proxy (DEF 14A filed 2026-01-22,
  `0001744489-26-000013`) was fetched; it is not read in full because Q5 and Q6 were not reached. Extracts:
  `Test Runs/_research 2026-10-06 DIS/notes - filing extracts.md`.
- **One figure cross-checked against the filed statement:** cash provided by operations FY2025 **$18,101M** on the filed
  Consolidated Statement of Cash Flows (10-K `0001744489-25-000155`) against 18,101 in `tools/run.py`; also investments
  in parks, resorts and other property $8,024M and equity-based compensation $1,363M, each matching.
- **`tools/run.py` arithmetic lines only** (USD millions; output saved as `run_py_output.txt` in the research folder):

| FY end | OCF | stock pay | capex | D&A | OCF less SBC less capex | OCF less SBC less D&A |
|---|---|---|---|---|---|---|
| 2023-09-30 | 9,866 | 1,143 | 4,969 | 5,369 | 3,754 | 3,354 |
| 2024-09-28 | 13,971 | 1,366 | 5,412 | 4,990 | 7,193 | 7,615 |
| 2025-09-27 | 18,101 | 1,363 | 8,024 | 5,326 | 8,714 | 11,412 |
| **three-year mean** | | | | | **6,554** | **7,460** |

  `run.py`'s five-year window gives 4,226 (capex basis) and 4,420 (D&A basis), 40.9% below the three-year window on the
  lower basis. Not carried to a value: Q1 closed the run (below). Three facts from the filings that any later Q4 must
  resolve are recorded as found: (a) income taxes paid were $1,193M, $3,963M and $1,221M in FY2023 to FY2025, and the
  FY2025 federal and California taxes were deferred under wildfire relief and paid in FY2026 (10-K and 10-Q MD&A), so
  FY2025's $18,101M is lifted by a deferral that reverses; (b) outside the capex line sit dividends to noncontrolling
  holders ($0.6bn FY2025, $0.5bn FY2024) and the Hulu buyout ($8,610M FY2024, $439M FY2025); (c) in the nine months to
  2026-06-27 borrowings rose $3,689M while $7,245M of stock was repurchased (10-Q).

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own this "if the market closed for five years"
**[M1997-109]**, which for Disney turns on what its three segments will earn, not on the quote. The market serves and
does not instruct **[M2006-077]**. No macro forecast enters **[M2000-094]**; the run asks about subscribers, rights costs
and park attendance, not the economy. Who is paid to tell you **[M2020-037]**: the company now issues EPS guidance into
the next fiscal year ("double-digit growth in adjusted EPS in fiscal 2027", EX-99.1 of 2026-08-05); it is a projection
and is not used **[M1995-050]**, **[M2003-065]**. The analyst's habits govern the reading: write contrary evidence down
at once **[M1997-127]**, state the other side's case better than its holder **[M2016-055]**, look for "what you’re
missing" **[M2025-013]**, and ask "What do I not know that I need to know?" **[M1999-129]**; the worst anchor is "your
previous conclusion" **[M2016-054]**, here the speakers' own past praise of this company. **Contrary evidence, written
down as found** **[M1997-127]**: (1) the speakers named Disney, in 1997 and 1998, among the few businesses whose ten-year
shape they thought they knew: "it’s easy for me to figure out that [...] Disney’s the entertainment company to be in"
**[M1997-119]**; "what Disney’s going to look like in ten years" **[M1998-024]**; its brand "travels" **[M1997-068]**.
(2) Entertainment operating income rose 19% in FY2025 and Direct-to-Consumer went from $143M to $1,327M (10-K), and in the
third quarter of FY2026 Entertainment rose 64% (10-Q): the streaming business is now profitable. (3) Experiences, 57% of
FY2025 segment operating income, grew its income 8% (10-K). Each is weighed at Q1 below.

## THE STANDING RULE
The buyer's own conduct: a purchase of DIS stock with the buyer's own money, unlevered, puts nothing at risk beyond the
sum paid; borrowed money to buy it is ruled out **[L2014-005]**, **[M2004-065]**, and nothing here risks "what we have and
need for what we don’t have and don’t need" **[M2012-081]**. No position is taken; the rule is met by the absence of one.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** "can I understand it?" **[M1995-051]**, where understanding is "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" and "how the industry will develop and where the
company will stand within the industry" **[M2012-065]**, **[M2000-037]**; first "identify the key variables [...] and
evaluating how predictable they were" **[M1998-044]**.

**How the parts are read.** Disney reports three segments with different economics (10-K `0001744489-25-000155`, segment
note). The framework's rule for a holding company is that it "is understood when each part that matters to its earnings
can be understood", and a part that cannot be, and that matters, keeps the whole outside, since doubt means outside
**[M2002-092]** (Q1, A holding company; a CONVENTION of the framework, with **[M2023-031]** OPEN against it). It is
applied here to a single company's reported segments; that extension is the analyst's, and is noted below under what was
unclear. FY2025 segment operating income (10-K MD&A): Experiences $9,995M (57%), Entertainment $4,674M (27%; Linear
Networks $2,955M, Direct-to-Consumer $1,327M, Content Sales/Licensing $392M), Sports $2,882M (16%; ESPN domestic $2,801M).

**Part 1, Experiences (57%).** Key variables: park attendance and per-capita spending, cruise and resort capacity, the
return on a capital budget rising from $8.0bn (FY2025) to "approximately $9 billion" (FY2026, 10-Q
`0001744489-26-000057`). Filing facts: domestic attendance (1)%, per-capita spending +5%, segment income +8% in FY2025
(10-K); Q3 FY2026 Experiences income +20%, of which "roughly four points" a tariff refund (EX-99.1,
`0001744489-26-000056`). The forecast here is about what families will do, a consumer question of the kind the rows
accept **[M2017-019]**, **[M2023-030]**, and about a share of mind the speakers asked of this very company, "what place
in the mind of billions of children around the world, and their parents, does Disney itself have" **[M1996-063]**. On
its own this part is the kind of business the circle can hold. One qualification from the filing: its new lands are
built on the studio's franchises (the 8-K of 2026-02-03 names Monsters, Inc., Avatar, Cars and Disney Villains lands), and
Consumer Products' $2,178M is the licensing of that same IP, so the part's ten-year shape is tied to the studio's hits.

**Part 2, Linear Networks (17% of segment income; the largest piece of Entertainment).** Key variables: pay-TV
subscribers and viewership. Filing facts (10-K): domestic affiliate fees "a decline of 9% from fewer subscribers,
partially offset by an increase of 7% from higher effective rates"; domestic advertising "a decline of 8% from fewer
impressions attributable to lower average viewership"; revenue (12)%. The direction is plain; the rows have seen it:
"If the technology had not changed, they’d still be impregnable franchises. But the technology did change."
**[M2006-065]**; the substitute test, "if cable and satellite broadcasting, as well as the internet, had come along first,
newspapers as we know them probably would never have existed" **[L2006-008]**, asks the same of a cable network bundle
against streaming. The rate of the decline and the price at which affiliates will keep carrying the networks (the 10-K
records YouTube TV dropping Disney's channels on 2025-10-30 and renewals that include "fewer of our linear networks") are
not foreseeable from the filings, and "slow change can be much harder to perceive, and can lull you to sleep easier"
**[M2014-038]**. In FY2026 the GAAP filing no longer reports Linear Networks and Direct-to-Consumer income separately (the
10-Q shows Entertainment by revenue type); the split is now given only as a non-GAAP "Entertainment SVOD operating
income" in the release. Test 3, do the past statements tell me the future ones **[M2008-033]**: the series changed
shape in FY2023 (two segments made from one), FY2024 (Star India out) and FY2026 (the Linear and DTC split dropped).

**Part 3, Direct-to-Consumer streaming (8% of FY2025 segment income).** Key variables: price, churn and the margin a
crowded field allows. Filing facts: FY2025 revenue $24,614M, income $1,327M (5.4%), subscription growth "8% attributable
to higher effective rates reflecting increases in pricing and 4% from more subscribers" (10-K); Q3 FY2026 non-GAAP SVOD
income $712M on $5,532M (12.9%) against $329M a year earlier (EX-99.1). The company's own risk factor: "There are a number
of competing DTC businesses. Consumers may not be willing to pay for an expanding set of DTC services at increasing prices
[...] The highly competitive environment in which we operate puts pricing pressure on our DTC offerings and may require us
to lower our prices or not increase our prices" (10-K). **Competitor, from its own filing:** Netflix, 10-K FY2025 filed
2026-01-23, accession `0001065280-26-000034`: revenue $45,183M, operating income $13,327M (29.5%); 2024 $39,001M and
$10,418M; 2023 $33,723M and $6,954M. The speakers, on this industry, in 2023: "you need fewer companies, or you need
higher prices [...] And you’ve got a bunch of companies that don’t want to quit. And who knows what pricing does under
that. But anybody who tells you that they know what pricing will do in the future is kidding themselves." **[M2023-078]**;
and the rival who sets the price **[M2023-079]**, said of the same streaming question. Test 6, can I name the winner,
not just the industry **[M2012-067]**, **[L2009-005]**: the filed margins name a leader that is not Disney's service, and
whether Disney's margin closes on it over ten years is the forecast **[M2023-078]** says no one can make.

**Part 4, Sports, ESPN (16%).** Key variables: subscribers to the bundle, the new direct-to-consumer ESPN (launched
August 2025), advertising, and rights costs. Filing facts: domestic ESPN fees "an increase of 7% from higher effective
rates was offset by a decrease of 7% from fewer subscribers"; domestic programming costs $11,240M against $10,435M (+8%)
"primarily due to expanded college football programming rights and contractual rate increases"; ESPN domestic income
(8)% (10-K); Sports income (14)% in the nine months to 2026-06-27 with programming costs +10% (10-Q). Fixed commitments
for sports rights at 2025-09-27: **$84,076M**, about $9.1bn to $9.9bn a year through FY2030 and $36,610M thereafter (10-K
commitments note). Rights bought for fixed sums years ahead, carried on a subscriber base that falls each year, is the
shape the rows record for newspapers, "Fixed costs are high [...] and that's bad news when unit volume heads south"
**[L2006-009]**; whether the direct product replaces the bundle's fee per head, and what the leagues charge at the next
renewals, is the ten-year variable, and the filing itself says ESPN's structure is still moving (the NFL to take 10% of
ESPN for the NFL Network and other assets; 10-K).

**Change.** The 10-K's own list of strategy changes in three years (Star India to a joint venture, a segment
reorganisation, content removed from the streaming services with impairments, the Hulu buyout, the Fubo combination, the
NFL transaction; risk factors) is the record of "industries prone to rapid and continuous change", which "precludes
investment certainty" **[L2007-005]**; "those are the businesses of rapid change" where "it’s very hard to evaluate moats"
**[M2001-069]**; "we view change as more of a threat" **[M1999-063]**; "a business that must deal with fast-moving
technology is not going to lend itself to reliable evaluations of its long-term economics" **[L1993-023]**; where a
"technological component that’s of significance" enters, "it won’t make it through the filter" **[M1998-008]**. Disney's
own risk factor says its businesses depend "on consumer tastes and preferences that change in often unpredictable ways".

**The other side's case, stated as well as the analyst can** **[M2016-055]**. The speakers themselves once put Disney
among the few businesses whose ten-year shape they could see, "Disney’s the entertainment company to be in"
**[M1997-119]**, "what Disney’s going to look like in ten years" **[M1998-024]**; the brand "travels" **[M1997-068]**;
"if you own the mouse, you own the mouse" **[M1996-079]**. Streaming is now profitable and its margin rising (above);
Experiences, more than half the income, is understandable; and the media decline is now a smaller share of the whole
than it was. **Why it does not carry.** The 1997 and 1998 rows were said of a company whose media income came from a
bundle that the 2025 filing shows losing 7% to 9% of its subscribers a year, and the same speakers later recorded what
technology did to such franchises **[M2006-065]**, **[L2006-008]** and that no one knows streaming's pricing
**[M2023-078]**; the worst anchor "is always your previous conclusion" **[M2016-054]**, and here the anchor is the
speakers' own. A margin rising for four quarters is a fact about the past, not the ten-year fix **[M2012-065]** asks for.
And Experiences' understandability does not reach the 43% of segment income in Entertainment and Sports, which matters
by any reading, nor the studio on which Experiences' franchises depend.

**The remaining tests.** Is the deciding question important and knowable **[M2006-076]**? Important, yes; knowable, no,
by the row on this industry **[M2023-078]**. Would the insiders write the ten-year forecast down **[M2000-105]**? The
filer writes no forecast past fiscal 2027 adjusted EPS (EX-99.1), and its own risk factors say pricing "may require us to
lower our prices or not increase our prices" and that YouTube TV's blackout's impact cannot be "reasonably estimate[d]"
(10-K). How far off could I be **[M2011-084]**? On streaming margin, between Disney's 5.4% of FY2025 and the leader's
29.5%, and on ESPN, between a direct product that carries the rights and one that does not: wider than any range Q7
could hold. Do I doubt it is inside? Yes, and "if you have doubts about something being into your circle of competence,
it isn’t" **[M2002-092]**; "it’s better to be well within the circle than to be trying to tiptoe along the line"
**[M2002-093]**. Do I only think I understand it **[M1997-024]**? The rows' own warning about believing one understands a
consumer business **[M2014-052]** applies.

- **VERDICT: TOO HARD (NATURE).** The ten-year economics of 43% of Disney's segment income (Entertainment and Sports)
  turn on streaming prices and margins in a field of companies "that don’t want to quit" and on sports-rights costs
  ($84,076M committed) against a bundle shrinking 7% to 9% a year; the speakers say of the first that "anybody who tells
  you that they know what pricing will do in the future is kidding themselves" **[M2023-078]**, and the industry changes
  fast **[L2007-005]**, **[L1993-023]**. A part that matters cannot be understood, so the whole is outside **[M2002-092]**.
  The cause is NATURE, not WORK: the deciding forecast is one the industry's insiders do not write down **[M2000-105]**,
  and "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those industries."
  **[L1993-023]**; **[L1999-018]**. The box is "too hard" **[M2006-013]**, which "doesn’t mean it isn’t a good buy [...]
  It just means that we don’t know how to evaluate it" **[M2000-038]**, and a lower price does not reopen it
  **[M2000-038]**. The circle is not widened to take it **[M1995-018]**. Q2 to Q12 are NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed the run). The competitor row (Netflix, from its own 10-K) was gathered for Q1's test 6 and is
recorded there.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten-year balance-sheet table is in `run_py_output.txt`; it was not read as Q4 evidence. Facts found
on the way and left for any later run are in STEP 0 (the tax deferral, the payments outside capex, the borrowing beside
the buyback) and in the research notes (the release's non-GAAP measures: adjusted EPS, total segment operating income,
SVOD operating income, free cash flow).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. (Filing fact recorded only: a new chief executive from 2026-03-18, 8-K `0001744489-26-000022`.)

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range was computed; under a TOO HARD (NATURE) close a lower price does not reopen the file
**[M2000-038]**, so the range would decide nothing.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: Entertainment and Sports, 43% of FY2025 segment operating income, turn on
streaming prices and margins in a crowded field and on $84,076M of committed sports rights against a bundle losing 7% to 9%
of its subscribers a year, a forecast the speakers say no one can make **[M2023-078]** and the insiders do not write down
**[M2000-105]**; the part that matters cannot be understood, so the whole is outside **[M2002-092]**. Price $103.61, market
cap $178,902M; Q7 not reached. No research pass is opened (that is for WORK). **What would change it** is the business,
not the price: Experiences offered as a separate security (a new name, run on its own), or the media and sports parts
shrunk, by the filings, to a share of the earnings that no longer matters to the whole.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      commits `0b6ffd1` (step 0 to the standing rule), `f7dbf87` (Q1), and the closing commit.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` by script before commit); every filing fact has
      its accession; no number without a filing. No CONVENTION of the run's own was needed.
- [x] The order was kept; Q1, the first STOP, failed and closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): only `run.py`'s OCF less stock pay
      less capex lines are shown, with the filing facts that would adjust them; the sovereign from the US Treasury;
      the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations, and Q1's statement of the
      other side's case).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the run date
      is today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The by-parts rule is written for a holding company** (Q1, A holding company), and Disney is one operating company
with three reported segments that feed one another (the parks and Consumer Products live on the studio's franchises).
The run applied the rule to segments; the framework does not say whether it reaches them, nor how interdependent parts
are read when the understandable part (Experiences) depends on the part that is not (the studio and its distribution).
(2) **"A part that matters" has no measure.** 43% of segment income was treated as mattering on any reading; a part at
10% or 15% would leave two analysts free to split. The same gap governs the reversal condition written in THE BOX. (3)
**The NATURE test is met here by a speaker's row about the industry itself** **[M2023-078]**, not by evidence of what the
insiders would write down **[M2000-105]**; the framework does not say whether a row on the industry suffices, or whether
the filer's own guidance horizon (fiscal 2027 adjusted EPS) counts as the insiders declining to write the ten-year
forecast. The run took both together. (4) **The rows that once named this company as understandable** (**[M1997-119]**,
**[M1998-024]**) sit in the same ledger as the later rows on changed franchises; the framework gives no rule for how an
old row about a named company weighs against later general rows. The run treated the old rows as contrary evidence and
the anchor rule **[M2016-054]** as governing. (5) **The filer changed its segment presentation in FY2026** and moved the
Linear and DTC split to a non-GAAP measure in the release; test 3 of Q1 **[M2008-033]** caught it, but the framework does
not say whether a lost GAAP disclosure is a Q1 fact or a Q4 tell. It was recorded at Q1 as a fact only. **Tool note:**
`tools/run.py` used the FY2025 operating cash without flagging the filer's stated tax deferral (wildfire relief) that
lifts it and reverses in FY2026. Inside its three-year window FY2023's deferral and FY2024's payment of it offset, but
FY2025's deferral does not, so the window's end year is lifted; a tool cannot read the MD&A, and the line is reported as
a reading duty for Q4, not as a defect to fix.
