# Company Run — Forum Energy Technologies, Inc. (NYSE and NYSE Texas: FET) — 2026-10-15
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run, 2026-10-15. The template was copied to this file and committed (e4a382bb) before any fetch. Working
folder: `Test Runs/_research 2026-10-15 FET/` (notes, fetch and arithmetic scripts, tool outputs; raw filings in its
gitignored `cache/`). The lock in `Screens/_daily/` is held by the dispatching session (its file name was seen in a listing;
it was not opened).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-15), after the run was committed: not held (`PORTFOLIO.md` carries no line for FET or Forum Energy).

**Contamination, declared.** Seen by accident and not used: the session's opening context showed the last five commit
subjects of the repository (a SCHYY run and its fold) and, in `git status`, the names of files in the research folders of
two other companies (AYI, ARCB); none concerns this company. The memory index loaded with the session carries one-line
summaries of the queue state (counts of gate-clearers, a paused wave, owed holding reviews); none names FET, and none was
used. No run file, holding review, `PORTFOLIO.md`, register, resume-state file or reading list was opened, listed or
searched; the only listing of `Test Runs/` made was filtered to today's date and returned nothing.

**The lines of evidence chosen** (the brief's one departure: derived from the FY2025 10-K's Item 1, Item 1A and Item 7).
Item 7 says "Our revenues, over the long-term, are highly correlated to the global drilling rig count" and Item 1 that
about 80% of 2025 revenue came from consumables and activity-based equipment; Item 1A opens with dependence on oil and
gas activity, then "The markets in which we operate are highly competitive", lower-cost foreign rivals, customers who are
also competitors, tariffs, impairments, debt covenants and asbestos claims. So the lines read were: (1) revenue, margins and
owner cash over the whole span 2010 to 2025, against the activity cycle the filer names; (2) the two segments and their
predecessor three segments, for the parts test; (3) the named rivals' own filings over the same span; (4) the acquisitions
and their write-offs (Variperm in 2024; the goodwill impairments of 2015 to 2019); (5) the debt, the 2029 Bonds and the
credit facility; (6) the proxy, for pay and the figures management features; (7) the asbestos and Tenaris litigation notes.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $77.11 (2026-10-15, the quote printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator
  rule 5). Consistency check from the filings, not a substitute: the company's own repurchases were at an average $59.79 in
  April 2026 and $50.77 in June 2026 (10-Q for Q2 2026, Part II Item 2, accession 0001401257-26-000053).
- **Shares by class** from the latest filing's cover: **11,246,295** common shares, a single class (10-Q for the period
  ended 2026-06-30, filed 2026-07-31, accession 0001401257-26-000053; `python Screens/cover_shares.py FET`). Check against
  the balance sheet of the same 10-Q: 13,507,226 issued less 2,244,808 in treasury = 11,262,418 at 2026-06-30; the 10-Q
  reports about 16 thousand shares bought back from 2026-06-30 to 2026-07-24, which closes the gap. After the 10-Q: the
  S-3ASR and 424B7 of 2026-08-28 (accessions 0001401257-26-000061 and 0001401257-26-000064) register 237,552 shares for
  resale by a selling stockholder, the company selling none; the 8-K of 2026-08-31 (0001401257-26-000065) files only the
  legal opinion for that supplement. No change to the count. `tools/run.py` used the older cover count of 11.304M
  (2026-04-24); the 10-Q count is used here.
- **Market cap:** $77.11 × 11.246M = **$867.2M**.
- **Sovereign for the earnings currency:** **5.43%**, the US Treasury daily par yield curve, 30-year, 2026-10-15
  (`python tools/sources.py`). The earnings currency is USD: the statements are presented in dollars, though about a third
  of long-lived assets sit in Canada (10-K note 15).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-27, accession 0001401257-26-000015), Items 1, 1A,
  5, 7 and notes 6, 7, 11, 15, 16; the 10-Q for Q2 2026 (filed 2026-07-31, 0001401257-26-000053), statements and MD&A; the
  proxy (DEF 14A filed 2026-03-27, 0001401257-26-000021), letter, compensation and Appendix A; the 10-Ks for FY2024
  (0001401257-25-000012; note 4, the Variperm acquisition; segments), FY2023 (0001401257-24-000038; three-segment table),
  FY2021 (0001401257-22-000022; market conditions, the ABZ and Quadrant sale) and FY2020 (0001401257-21-000031); the 8-K
  list since 2023-06 (submissions index) and the 8-K of 2026-08-31. The earlier years' figures are from the XBRL company
  facts as first filed, each with the 10-K accession `tools/run.py` lists (0001401257-18-000060 to 0001401257-26-000015).
  **One figure cross-checked against the filed statement:** net cash from operating activities for 2025, $70,402 thousand
  in the 10-K's cash-flow table (Item 7), equals the $70.4M of the XBRL series; total assets at 2025-12-31, $752,455
  thousand in note 15, equal the $752.5M of the balance-sheet table below.
- `python tools/run.py FET` arithmetic lines only (`_research 2026-10-15 FET/run_py_output.txt`): OCF, SBC, capex and D&A
  for 2023 to 2025 as filed (8.2 / 92.2 / 70.4; 4.6 / 7.1 / 9.0; 7.9 / 8.1 / 6.0; 34.7 / 53.7 / 33.8), finance-lease
  principal of 1.2 / 1.7 / 2.0 in the financing section, the ten balance sheets. The tool's three-year means (42.6 on all
  capital spending, 9.3 on D&A) and its yield lines are not used; owner cash is rebuilt below over sixteen years
  (`compute.py`, `compute_output.txt`), because the brief and Q7 need the cycle.
- **Owner cash after every real cost** (operating cash less stock pay, capital spending and finance-lease principal; before
  purchases of businesses; after interest), USD millions: 2016 27.3 · 2017 -88.2 · 2018 -42.6 · 2019 72.0 · 2020 -9.3 ·
  2021 -27.3 · 2022 -30.0 · 2023 -5.5 · 2024 75.3 · 2025 53.4. Five-year average 2021 to 2025: **13.2** before purchases;
  **-17.9** after the $155.6M net paid for businesses (Variperm $150.4M in 2024). Before interest (all-equity): 35.8. Stock
  pay is complete as the filer tags it (ShareBasedCompensation; 2023 under AllocatedShareBasedCompensationExpense). Cash
  withheld for employees' taxes on vested stock ($9.3M in the first half of 2026, 10-Q cash-flow statement) is not deducted a
  second time, since the stock pay is already charged at its grant value. Proceeds of sale-leasebacks ($20.3M in 2024,
  $14.6M in 2025; 10-K Item 7) are left out: they are a financing of buildings the company keeps using, and the rent then
  sits inside operating cash.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest on this name is the first: a share is a business. Would an owner be content "if the
market closed for five years?" **[M1997-109]** The quotation is the thing that has moved here (the proxy's opening line is
"FET's stock price increased 139% in 2025"), and "It just tells us prices." **[M2006-077]**; what the analyst is owed is the
business's own record over a whole cycle. No macro view enters: the run does not forecast oil, rigs or the energy
transition, "macro conclusions are — just never enter into the discussion." **[M2000-094]**; it reads what the filings
show the business earned through the cycle that happened. **Contrary evidence, written down as found** **[M1997-127]**:
(1) the first half of 2026 is the best in years (operating income $31.5M, net income $16.9M; 10-Q 0001401257-26-000053),
backlog at 2025 year end was $311.6M against $213.5M a year earlier, and 2025 bookings were $891.0M against revenue of
$791.5M (10-K Item 1), so the business is showing improvement now; (2) the Artificial Lift and Downhole segment earned 13.1%
to 14.1% segment margins in 2023 to 2025 (10-K note 15; 10-K FY2024 Item 7), a part that looks better than the whole;
(3) the company has cut debt from $398.9M (2019) to $135.9M (2025) and bought in about 11% of its shares in 2025. Each is
carried to the question it bears on.

## THE STANDING RULE
Owning this need not put the buyer at risk of ruin, provided it is bought without borrowed money and sized so that a fall
of the kind this stock has had (equity fell from $1,409M in 2017 to $291M in 2025) cannot force a sale: "We are never going
to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**; "borrowed money has no place in the
investor's tool kit" **[L2014-005]**. The rule binds the buyer's conduct and is met by that conduct; the target's own debt
is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**. The product chemistry need not be understood;
  "What is important is that I understand the economic dynamics of the industry." **[M2011-014]**
- **The key variables and whether they are foreseeable** ("trying to identify the key variables" **[M1998-044]**). The filer
  names them itself: activity (its revenue is "highly correlated to the global drilling rig count", 10-K Item 7; demand
  "depends largely upon prevailing industry conditions", Item 1A) and its competitive position in "highly competitive"
  markets against "large national and multinational companies" (Item 1A). The first is a dependence on a commodity
  cycle. The framework's commodity paragraph (Q2, decided 2026-10-12) rules that such a dependence is never by itself a STOP
  at Q1 or Q2, on the rows' own ground: "We don’t think we can predict commodity prices." **[M2016-025]**, and the business is judged "off the
  figures" **[M2008-069]**. The second is readable from the filings: sixteen years of statements, two segment structures,
  the named rivals' filings. So the question Q1 asks is whether "the financial statements will tell me the information
  that’s useful to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**.
  They do: across 2010 to 2025 they show one shape repeatedly (revenue rising and falling with activity, from $1,739.7M in
  2014 to $587.6M in 2016, $1,064.2M in 2018, $512.5M in 2020 and $791.5M in 2025; margins that fell to losses in every
  downturn; acquisitions written off), and the economic dynamics behind that shape (equipment and consumables sold into a
  customer's capital budget, against larger and lower-cost rivals) are stated by the filer. Where the business will stand
  in ten years, in the sense of earning power and competitive position, can be judged from that record; whether the judgment
  is favourable is Q2's.
- **Routing.** This is not fast-moving technology: the products are tubular-handling tools, valves, pumps and fluid ends,
  coiled tubing, ROVs, casing tools and sand screens (Item 1), and the risk factor on technology ("Our success depends on
  our ability to implement new technologies and services more efficiently and quickly than our competitors", Item 1A) is a
  competitive point, carried to Q2. Not a bank, not a holding company. Two segments with different economics, read by parts
  at Q2.
- **Contrary evidence, written down** **[M1997-127]**: the filer says "We are unable to predict what effect consolidations
  and the energy transition in the industry may have on prices, spending by customers, selling strategies, competitive
  position, customer retention" (Item 1A). That is a statement that the level of future activity is unknown; the framework
  places that unknown at Q7 (the cycle base and the width), not here **[M2016-025]**. And "if you have doubts about something
  being into your circle of competence, it isn’t." **[M2002-092]**: the doubt here is not about what drives the economics,
  which the filings state, but about the level of activity, which no one states. The reading, mine: IN, with that doubt
  recorded for Q2 and Q7.
- **VERDICT: IN.** The economic dynamics can be read from the figures and the filer's own description **[M2011-014]**,
  **[M2008-069]**, **[M2012-065]**; the commodity-type dependence on drilling activity is not by itself a stop **[M2016-025]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now." **[M1995-038]** The castle the rows ask for is one that "protects excellent returns on invested capital"
**[L2007-004]**.

**The castle tests, each with its filing fact.**
- **The attacker with money** **[M2011-015]**. The filer answers it itself: "New competitors have also entered the markets in
  which we compete" and "Competitors may be able to offer more attractive pricing, duplicate strategies, or develop
  enhancements to products that offer performance features that are superior to our products" (10-K FY2025 Item 1A,
  0001401257-26-000015). The rows' kin of the test, "why are there no new entrants into the field?" **[M2000-077]**, is
  answered the other way: there are new entrants.
- **Pricing power and the agony before a rise** **[M2005-020]**. No instance found in the filings read of a price rise
  that held through a downturn; the evidence runs against: gross margin fell from 31.2% (2024) to 27.7% (2025) as cost of
  sales in Drilling and Completions rose 7.7% on revenue up 1.4% (Item 7), and tariffs cut valve volumes instead of being
  passed on (Item 7: "tariff-related impacts on valve products sales volumes"). Strong positions "manage to pass through
  increases in raw material costs" **[M2005-017]**; this one reports that "Increased costs of raw materials and other
  components, and inflationary pressure, may result in increased operating expenses" (Item 1A).
- **Unit volume and share of mind.** Revenue is set by the customer's activity ("highly correlated to the global drilling
  rig count", Item 7) and fell 3.1% in 2025 as the global rig count fell 6.7%; no market share figure is filed.
- **The low-cost position.** For a business tied to a commodity cycle the framework asks whether it is the low-cost
  producer, measured "more by cost of production" **[M2006-004]**, since "The figures are available." **[M2009-059]** The
  filer states that it is not: "We also have competitors outside of the U.S. with lower structural costs due to labor and
  raw material cost in and around their manufacturing centers"; "Our larger competitors are able to use their size and
  purchasing power to seek economies of scale and pricing concessions" (Item 1A). It sources the majority of its valve
  products from international manufacturing partners (Item 1), which is the shipped-in product the rows warn of, "a
  product that can be shipped in from abroad very easily" **[M2007-116]**, here with the filer as the importer and the
  foreign maker able to sell past it. "The guy who could sell it cheaper than we could made it risky for us." **[M1997-010]**
- **The brand in the customer's mind.** Brands are named (Perry, Sub-Atlantic, Global Tubing, Davis-Lynch, Variperm, PBV),
  but the filer lists the competitive factors as "product quality, price, breadth of product offering, availability of
  products and services, performance, distribution capabilities" (Item 1A): price is on the list, and no brand is said to be
  asked for by name.
- **Would the customer still choose it over the low bid?** **[M2017-009]** The filer: "some of our customers are our
  competitors and have in the past ceased buying from us, and may do the same in the future"; customers "have consolidated
  and are seeking to achieve economies of scale and pricing concessions" (Item 1A). Availability is the one thing customers
  are said to pay a premium for ("Customers may pay a premium for earlier or immediate availability", Item 1, Working
  Capital), and it is bought by carrying "substantial inventories", which is capital, not a moat.
- **Ask the competitors.** Not on the public record beyond the filings. One fact: Tenaris, a named rival, litigated its
  coiled-tubing patents against the company's Global Tubing subsidiary from 2017 (10-K note 11).
- **Widening or narrowing** **[M1999-108]**. Narrowing on the record of the decade: revenue from $1,739.7M (2014) to $791.5M
  (2025); $961M of goodwill written off in 2015 to 2019 (XBRL GoodwillImpairmentLoss, 10-Ks of those years) and $119.1M of
  Coiled Tubing intangibles in 2024 (10-K FY2025 note 6); the FY2025 Item 7 records a "strategic decision to consolidate
  facilities and discontinue certain products" with $20.2M of write-downs.
- **What could destroy it.** The filer names it: customer consolidation and "the energy transition" (Item 1A), and
  "A greater focus on budgetary discipline and technological advances have caused a decline in customer spending that may
  remain at a low level despite an increase in commodity prices" (Item 1A summary). The activity level itself is not judged
  here **[M2016-025]**.

**The competitor row** (the rivals the 10-K names, Item 1: "NOV Inc. and Tenaris S.A., and the manufacturing arms of SLB,
TechnipFMC plc, Baker Hughes and Weatherford International PLC"; all six file with the SEC, so none is flagged as a
non-filer; the first three in the filer's order are taken, a rule fixed before any figure was fetched; for SLB, TechnipFMC,
Baker Hughes and Weatherford the filer competes only with a "manufacturing arm", so a whole-company figure is not the arm's
figure, and no SLB segment matches the filer's lines). Same metrics, each from the company's own XBRL as first filed
(`compare.py`, `compare_output.txt`), over 2015 to 2025 and over the trough-to-trough cycle 2016 to 2020:

| | source | operating margin 2015-25 (sum of operating income over sum of revenue) | average return on equity 2015-25 (net income over average equity) | operating margin 2016-20 | best year |
|---|---|---|---|---|---|
| FET | 10-Ks, CIK 1401257 | -18.7% | -18.9% | -36.4% | 3.8% (2025) |
| NOV | 10-Ks, CIK 1021860 | -10.3% | -9.4% | -29.8% | 9.9% (2024) |
| SLB | 10-Ks, CIK 87347 (pre-tax income; operating income untagged) | 0.8% pre-tax | -0.8% | -15.0% pre-tax | 15.9% pre-tax (2023) |
| Tenaris | 20-Fs, CIK 1190723 (IFRS) | 15.0% | 8.9% | 4.4% | 29.0% (2023) |

Margins include the impairments each filer booked; they are write-offs of capital paid in. Before impairments, the filer's
segment operating income in 2019, near the last peak, was 2.2% to 2.4% in each of the three segments it then reported (10-K
FY2020 Item 7, 0001401257-21-000031). The filer is the lowest of the four on every measure and on both spans; the one rival
with a decent record, Tenaris, makes pipe and coiled tubing at scale and is the rival that litigated against it.

**The parts table** (the framework's business-of-parts convention; "lumping them together [...] impedes analysis"
**[L2008-005]**). The present two segments exist from 2024, recast for 2023 only (10-K FY2024 Item 1); 2021 and 2022 were
reported in three other segments and were not recast, so the share is taken on the three years filed on the present basis,
said so:

| part | segment operating income 2023 / 2024 / 2025 ($M; corporate cost 27.3 / 31.0 / 34.9 not allocated) | share of the three years | castle | decides |
|---|---|---|---|---|
| Artificial Lift and Downhole (downhole protection, casing tools, Variperm sand control, production equipment, valves) | 31.6 / 48.9 / 41.2 | 70.9% | ordinary returns at best, see below | **yes** (more than half) |
| Drilling and Completions (drilling tools and consumables, subsea vehicles, stimulation and intervention, coiled tubing) | 19.4 / 17.7 / 12.8 | 29.1% | open: margins of 2.7% to 3.9%; $119.1M of its Coiled Tubing intangibles written off in 2024 | no; carried to Q7 at no growth |

Sources: 10-K FY2025 note 15; 10-K FY2024 note 17 and Item 7 (0001401257-25-000012).

**The deciding part.** Artificial Lift and Downhole earned segment operating income of $48.9M on segment assets of
$371.2M in 2024 and $41.2M on $353.5M in 2025 (note 15): 13.2% and 11.7% pre-tax before any corporate cost; with corporate
cost shared by revenue (42.3% and 39.8% of revenue, Item 7), 9.6% and 7.7%. Segment liabilities are not filed, so these are
on gross segment assets; on the company's own balance sheet the trade payables, accrued liabilities, deferred revenue and
billings in excess are about a quarter of total assets, which would lift the figures to roughly 13% and 10% pre-tax on
capital employed. These are its good years, in the middle of an upturn, not its trough. Its predecessor parts through the
last downturn: the Production segment (the valves and production equipment now inside it) earned 2.4% (2019), -18.8%
(2020), -12.3% (2021), -0.3% (2022) and 4.4% (2023); the Downhole line sat inside Drilling & Downhole, which earned 2.2%,
-22.1%, 2.0%, 10.6% and 10.2% over the same years (10-K FY2020, FY2021 and FY2023 Item 7). Its most profitable piece,
Variperm, is a castle bought rather than kept: $150.0M of cash and 2.0M shares, total consideration $199.0M, of which $66.8M
goodwill and $104.6M intangibles (10-K FY2024 note 4); it contributed revenue of $109.3M and net income of $19.0M in 2024,
and in 2025 the segment's revenue fell 8.9% on "lower sand control sales" (Item 7). The valves inside the part are sourced
abroad and lost volume to tariffs (Item 1, Item 7).

**The field's returns over the last full cycle**, judged in words. Over 2015 to 2025 and over the trough-to-trough cycle
2016 to 2020, the filer lost money on its capital and so did two of its three named rivals; the third earned an ordinary
return. "you can have only two competitors and they’re still terrible businesses" **[M2013-052]**; "the improvement you get
one day, your competitor gets the next day" **[M2004-053]**. The filer's deciding part, at its best in an upturn, earns
ordinary returns on its assets, and its components lost money in the last trough. This is not a castle whose future cannot
be judged ("We don’t know how to valuate that" **[M2000-019]**): its returns are known from the filings, and they are not
excellent in any year read. The recovery of 2023 to 2026 is not a candidate for the framework's full-cycle credit for a
change for the better, because even the improved returns are ordinary; that credit is for a business whose price behaviour
holds through a downturn **[M2005-020]**, and the question here does not turn on it.

**Contrary evidence, written down** **[M1997-127]**: the first half of 2026 shows operating income of $31.5M on revenue of
$434.9M (7.2%) and net income of $16.9M (10-Q 0001401257-26-000053), and the backlog has grown; a reader who credits the
recovery would call the castle improving. On the rows it is an upturn in a business whose best years are ordinary, and
"What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "Time is the enemy of the
poor business" **[M1998-006]**.

- **VERDICT: OUT.** The castle is shown open on the evidence: the filer says it is not the low-cost producer and that its
  rivals include larger and lower-cost ones **[M1997-010]**, **[M2006-004]**; customers press for the low bid and some are
  themselves competitors **[M2017-009]**; and over the full cycle the filer and its field earned at best ordinary returns,
  which the framework sends OUT, not TOO HARD, since the returns are known from the filings **[M2013-052]** and a moat is what
  "protects excellent returns on invested capital" **[L2007-004]**. The box is OUT, one of "in, out, and too hard"
  **[M2006-013]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (Q2 closed the file). Facts are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The template asks that the balance sheets be read in Step 0 when the file closes before Q4; they are read under
AFTER THE STOP, Q4, with no verdict.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The two reporting figures are computed below under COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q2**: the castle is shown open on the filer's own evidence (not the low-cost producer; larger and lower-cost rivals;
customers who are competitors and press for price) and the filer, its named field and its deciding part earned at best
ordinary returns over the full cycle; integrity facts recorded, not judged. Not a TOO HARD, so no cause is named and no
research pass is opened. For the record only, beneath the stop: the COMPUTATION below gives a value of $22.15 a share (the
no-growth case alone, all-equity basis) against $77.11.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on a later question, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).*

**Q3 (capital).**
- Cash paid for businesses, net of businesses sold, 2011 to 2025: $1,208M (XBRL PaymentsToAcquireBusinessesNetOfCashAcquired
  and ProceedsFromDivestitureOfBusinesses; the $104.6M ABZ and Quadrant valve sale of 2020-12-31 in the 10-K FY2021 note on
  dispositions). Goodwill written off: $123.2M (2015), $68.0M (2017), $298.8M (2018), $471.0M (2019); Coiled Tubing intangibles $119.1M in
  2024. Owner cash before purchases summed over 2011 to 2015 was $500.7M against $930.6M paid for businesses; over 2016 to
  2020, -$40.8M against $121.7M; over 2021 to 2025, $65.9M against $155.6M (`compute_output.txt`).
- Capital spending is small and below depreciation: $6.0M in 2025, $8.1M in 2024; depreciation $7.3M in the first half of
  2025 and $6.1M in the first half of 2026 (10-Q cash-flow statement). The filer expects about $10.0M in 2026, "primarily
  for replacement of end of life machinery and equipment" (10-K Item 7). Buildings were sold and leased back ($20.3M of
  proceeds in 2024, $14.6M in 2025; operating lease liabilities $83.8M at 2026-06-30).
- The capital that matters is working capital: inventories $233.5M and receivables $174.0M at 2026-06-30 against first-half
  revenue of $434.9M (10-Q); the filer collects "in approximately 70 days from shipment" and carries "substantial
  inventories" (10-K Item 1).

**Q4 (the accounts), with the balance sheets the template asks to be read in Step 0.**
- Ten year-ends, USD millions (first-filed XBRL, `run_py_output.txt`; the 2025 column checked against the filed balance
  sheet): equity 1,409 (2017), 1,030, 486, 406, 329, 307, 413, 320, 291 (2025), 290 (2026-06-30); goodwill 755 (2017) to 0
  (2019), 65 after Variperm; retained earnings 439 (2017) to -844 (2025); inventory 443 (2017, 54% of that year's revenue) to
  239 (2025, 30%); receivables 203 to 142; long-term debt 399 (2019) to 135 (2025). What the figures say: the equity that
  disappeared went out through write-offs of purchased goodwill and intangibles and through losses, not through
  distributions (no dividends in 2024 or 2025, 10-K Item 5). What they do not say: the segment liabilities, so the segments'
  capital employed is not filed.
- Equity rose from $307.0M (2022) to $412.6M (2023) while net income was -$18.9M; the share count went from 5.65M (Feb 2022)
  to 10.30M (Feb 2023) to 12.28M (Feb 2024) (cover pages, 10-Ks 0001401257-22-000022, -23-000023, -24-000038). The 9.00%
  convertible secured notes due 2025 paid 2.75% of their interest "in cash or additional notes, at the Company’s option"
  (10-K FY2023 note on debt); paid-in-kind interest does not pass through operating cash, so the equity-basis owner cash of
  2021 to 2023 is overstated by it (amount not extracted).
- Featured figures: the proxy reports "$80 million of free cash flow" for 2025 against operating cash flow of $70.4M and
  capital spending of $6.0M; its reconciliation adds "Proceeds from sale-leaseback transactions" of $14,574 thousand and
  asset-sale proceeds of $1,007 thousand (DEF 14A Appendix A, 0001401257-26-000021). The same letter states leverage as "1.2
  times our 2025 Adjusted EBITDA" ("EBITDA as adjusted", $86,403 thousand, Appendix A). Gains on sale-leasebacks ($11.2M in
  2025, $4.9M in 2024, $7.0M in 2022) sit inside operating income (10-K Item 7; 10-K FY2023 Item 7). Inventory write-downs
  recur: $19.7M (2025), $2.7M (2024) (10-K Item 7, critical estimates).
- Tax: $26.2M of tax on $16.6M of pre-tax income in 2025, "impacted by losses in jurisdictions where the recording of a tax
  benefit is not available" (Item 7); gross US net operating losses of $417.8M, of which $384.6M "will not expire" (10-K
  income-tax note).

**Q5 (the people).**
- Neal A. Lux, President and CEO since February 2022, earlier COO; chairman separate (Mr. McShane); eight of nine directors
  independent by the NYSE test (DEF 14A). CEO pay $6.16M in 2025 against $5.06M in 2024; the annual plan "paid out at 144% of
  target"; half of long-term pay "contingent upon relative TSR performance", with performance units tied to "absolute and
  relative total stockholder return" and to free cash flow as the company defines it, and units that "vest upon achievement
  of minimum stock price thresholds" (DEF 14A).
- The proxy letter opens its business section with the share price: "FET's stock price increased 139% in 2025, a performance
  that is at the top of our peer group and the Russell 2000" (DEF 14A letter).
- A 2024 related-party note: sales to and purchases from Endurance Lift Holdings, about $3M, connected to a former director
  (DEF 14A). No instance found, in the filings read, of a restatement or an enforcement matter.
- These are the habits Q4 records as a weighing and Q5 reads with the integrity record (a featured adjusted figure, pay on
  the stock price); they are flagged in the box line and not judged.

**Q6 (the money and the owners).**
- Buybacks: about 1.4M shares for $34.3M in 2025 (about $24.50 a share on average; $30.95 in the fourth quarter), and
  148,839 shares for $7.6M in the first half of 2026 ($59.79 in April, $50.77 in June) (10-K Item 5; 10-Q Part II Item 2).
  The programme names no price: shares are bought "in amounts and at prices that the Company deems appropriate" (10-K Item
  5). The bottom of the COMPUTATION's range below is $22.15 a share; Q6's test would set the prices paid against it.
- Issuance: the split-adjusted share count rose from about 4.6M (2013, 91.9M before the 1-for-20 reverse split of 2020) to
  11.2M now (cover pages); 2.0M shares were part of the Variperm price (10-K FY2024 note 4). No dividends.

**Q9 (debt and exposures).**
- Debt at 2025-12-31: $100.0M of 10.50% senior secured 2029 Bonds (due 2029-11-07, Nordic Trustee, listed on Euronext ABM;
  covenants of maximum leverage 4.0x and minimum liquidity $25.0M; a 101% change-of-control put), $37.3M on the asset-based
  credit facility (extended in February 2026 to 2031-02-04), $4.0M other debt (10-K note 7, note 16). At 2026-06-30, debt of
  $143.7M carrying value and cash of $33.7M (10-Q balance sheet). Interest paid $16.9M in 2025.
- Asbestos: "One of our subsidiaries has been named as one of many defendants in a number of product liability claims for
  alleged exposure to asbestos used in valves", claims since 1998, defended mainly on successor liability (10-K note 11; risk
  factor in Item 1A). The rows carry a flat exclusion on asbestos for whole businesses; it is not weighed here.

## COMPUTATION, NOT A CLEARANCE
*Beneath a closing STOP; no entry language; operator rule 3. The two reporting figures the brief asks for, built by Q7's
range convention as far as the facts allow (`compute.py`, `compute_output.txt`).*

- **Basis.** Central on the all-equity basis: owner cash before interest (the cash interest paid is added back; no tax
  shield is credited, since the debt sits with the US parent, whose deferred tax assets carry a valuation allowance:
  CONVENTION of this run, rationale: crediting a shield the company does not get would overstate the cash), after the
  company's own tax, against market value plus net debt. Net debt at 2026-06-30: debt $143.7M (carrying value; principal is
  about $5.4M higher) less cash $33.7M = **$110.0M**; operating leases ($83.8M) left out, said so. Equity-only beside.
- **The window and the cycle (specific a).** The first window year, 2021, is aberrational on the filer's own description:
  "drilling and completions activity remains significantly below pre-pandemic levels" (10-K FY2021 Item 7,
  0001401257-22-000022), and owner cash was -$27.3M. The base is the last full cycle, trough to trough on the filer's revenue,
  2016 ($587.6M) to 2020 ($512.5M), taken inclusive of both troughs (CONVENTION of this run, rationale: the framework names
  trough to trough and does not say whether both ends count; inclusive is the lower, more conservative base). Base: owner
  cash before purchases **-$8.2M** a year (equity) and **$19.5M** (all-equity). The literal window 2021 to 2025 is shown
  beside: $13.2M and $35.8M.
- **Acquisitions (specific c).** Net purchases exceed half of owner cash before purchases in the cycle ($121.7M against
  -$40.8M) and in the window ($155.6M against $65.9M), so the serial-acquirer convention makes the organic pair central:
  purchases left out, organic growth only. The filer reports no organic growth figure for the span; Variperm's cash is inside
  the 2024 and 2025 figures; so no organic growth can be credited, and the growth between the cycle and the window (12.9% a
  year on the all-equity series, `compute_output.txt`) is not used, since it would credit total growth with the purchases
  left out, which specific (c) forbids. The default pair beside: the window after purchases is $4.7M a year all-equity and
  -$17.9M equity, a sign change against the cycle (-$4.8M all-equity), so no growth is measurable there either.
- **Decline, working capital, maintenance, the cap (specifics b, d, e, f).** With no growth creditable, the range is the
  no-growth case alone, said so (specific b). Working capital is inside operating cash in every year (d). All capital spending
  is replacement on the filer's own guidance, so the maintenance case and the all-spending case are the same (e);
  capital spending runs below depreciation, so a depreciation variant would be lower by roughly $5M to $8M a year. The cap (f)
  does not bind with no growth carried. The four PG specifics: aggregate cash, all spending deducted, zero growth after year
  ten, a price above the top closes OUT.
- **Value range (a reporting figure):** **$22.15 a share**, all-equity, the no-growth case at 5.43% on the cycle base, less
  net debt, over 11.246M shares; one case, so no width. Beside it: the literal window, $48.88 all-equity and $21.58
  equity-only; the cycle base on the equity-only basis is negative (-$13.36). Against **$77.11**, the price is above every
  case. **The floor is tested first:** the expected return at the price is 2.0% on the cycle base and 3.7% on the literal
  window (all-equity), and 1.5% equity-only on the window, all below the floor of about ten percent, so had Q7 been reached it
  would have closed OUT whatever the width **[M2003-149]**.
- **Fair price (a reporting figure, Part VII; never a verdict):** **$7.56 a share** on the all-equity basis, the no-growth
  case on the cycle base discounted at ten percent, less net debt (with one case, the average of the two ends is that case).
  Equity-only: no positive figure (the cycle base is negative; -$7.26). Beside, on the literal window: $22.07 all-equity,
  $11.72 equity-only. After the company's own tax. No cheap price is reported.

## RESEARCH PASS
Not opened: the box is OUT, not TOO HARD (WORK). For the record, no case of the computation earns the floor at the price, so
under Part VII a pass would in any event be written and closed unrun.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit e4a382bb); written question by question; committed after each
      (7ffcf127 for Step 0 to Q1, 5d09aa51 for Q2, then the close), each with a pathspec of the two paths only.
- [x] Dispatched: the brief allowed the per-question commits; the lock is held by the dispatching session (its file was
      seen in a listing, not opened or written by this analyst). The fold into the register is the dispatcher's.
- [x] No other run file, holding review, `PORTFOLIO.md`, register, reading list or resume-state file was opened, listed or
      searched; what was seen by accident is declared under Contamination at the top and was not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is the row's own
      (`check_citations.py`, `check_citations_output.txt`); no E-ids. Every filing fact carries its document and accession.
- [x] The order was kept: Q1 IN, Q2 OUT closed the file; nothing after Q2 is a clearance; the figures after it are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy: operating cash less stock pay, capital spending and
      finance-lease principal, with purchases of businesses shown. One gap admitted: paid-in-kind interest of 2021 to 2023
      was not extracted, so the equity-basis figures of those years are slightly high; the all-equity basis is unaffected.
      The sovereign is the US Treasury's, dated; the price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as found (foundations, Q1, Q2); the facts found for later questions are under
      AFTER THE STOP, and the integrity flag is in the box line.
- [x] No row dated after the anchor: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yield lines, means and any rule it prints were not.
- [x] `python tools/check_framework.py` PASS before the closing commit (output in `check_framework_output.txt`).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Four things. (1) **The parts test on a recent re-segmentation.** The business-of-parts convention measures the share of
"five-year operating profit", but this filer re-cut its segments in 2024 and recast only 2023; 2021 and 2022 exist only in a
three-segment form that splits the deciding part's lines across two old segments. The share was taken on the three years
filed on the present basis, and the predecessor segments were read for the cycle; the convention says nothing about a window
shorter than five years, and a rule is wanted (the years on the present basis, or a mapping of the old lines). (2) **The
serial-acquirer convention and a filer that reports no organic growth.** The convention makes the organic pair central,
"organic growth as the filer reports it"; this filer reports none, so the run credited none and fell to the no-growth case,
which then made the "range" a single point and the fair price's "average of the two ends" one case. The text should say
what happens when the organic figure is not filed (no growth, as done here, or a stated strip of the acquired business's own
filed contribution, which for Variperm is given for 2024 only). (3) **Trough to trough, inclusive or not.** Specific (a)
names peak to peak or trough to trough without saying whether both end troughs are counted; here inclusive gives an
all-equity base of $19.5M and dropping either end trough would raise it; confessed as a CONVENTION of this run. (4) **The
standing castle that protects only ordinary returns, read on a part.** The OUT item is written for "a field whose durable
players earn ordinary returns over a full cycle"; here the field lost money and the deciding part's best years were
ordinary, but the deciding part has no full cycle on its present basis. The run read the part's good years plus its
predecessors' trough, and judged it in words, as the convention asks; whether a part's full-cycle record may be assembled
from predecessor segments is not said.
