# Company Run — Wyndham Hotels & Resorts, Inc. (NYSE: WH) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Working folder:
`Test Runs/_research 2026-10-14 WH/` (raw filings in its ignored `cache/`). Dispatched blind run.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for WH or Wyndham).

**CONTAMINATION, declared before any reading.** (1) To confirm the dated file name was free I listed `Test Runs/` with a
filter on today's date; the listing showed run files and research folders dated 2026-10-14 for CHH, HLT, MAR and four steel
names. Not opened. (2) The session context carried the repository's recent commit subjects, one of which is the fold of the
CHH run of the same day and states, in passing, a return-on-tangible-operating-assets comparison in which Wyndham, Hilton and
Marriott "rose". I did not use it: every rival figure below is computed from the rivals' own filings in my research folder,
and where my figure and that subject agree or disagree I say nothing of it. (3) A memory line loaded by the harness gives
queue counts and says "nothing buyable"; it names no company and is not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $73.42 (close 2026-10-13, as printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: **74,211,122** common shares outstanding as of July 15, 2026 (Form 10-Q
  for the quarter ended June 30, 2026, filed 2026-07-23, accession `0001722684-26-000074`; `python Screens/cover_shares.py WH`
  prints the same). One class; preferred authorized 6.0M, none issued. Check against the balance sheet of the same 10-Q:
  76.1M issued less 1.6M treasury = 74.5M at June 30, 2026; the further fall to 74.2M by July 15 is consistent with the
  buybacks the 10-Q reports (1.3M shares in the first half at $80.31). No 8-K or prospectus after the 10-Q changes the count
  (EDGAR index read to 2026-10-14: after 2026-07-23 only Forms 3, 4 and 144).
- **Market cap:** 74.211M x $73.42 = **$5,449M**.
- **Sovereign for the earnings currency:** USD (royalty contribution 77% U.S. in FY2025, 10-K Item 1; reporting currency USD).
  **5.56%**, US Treasury daily par yield curve, 30-year, 10/13/2026 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-19, `0001722684-26-000007`): Item 1, Item 1A, Item 5,
  Item 7 in full, the statements and the notes on deferred revenues, loans receivable, development advance notes, Revo and
  debt. 10-Q Q2 2026 (filed 2026-07-23, `0001722684-26-000074`): statements, Revo, debt, MD&A operating statistics. Proxy
  DEF 14A (filed 2026-03-25, `0001722684-26-000050`). 8-Ks of 2025-11-04 (`0001140361-25-040345`, CFO departure),
  2025-11-17 (`0001722684-25-000081`, new director), 2026-02-24 and 2026-02-27 (`0001140361-26-006580`,
  `0001140361-26-007147`, the $650M 5.625% notes due 2033), 2026-03-03 (`0001140361-26-007444`, new CFO), 2026-05-18
  (`0001140361-26-021771`, the CEO's illness and the Chief Accounting Officer's departure effective 2026-07-31). Earlier
  10-Ks for the cycle: FY2023 (`0001722684-24-000006`), FY2021 (`0001722684-22-000005`), FY2019 (`0001722684-20-000007`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$367M**
  on the filed Consolidated Statement of Cash Flows (10-K FY2025, page F-8) equals the `tools/run.py` XBRL line (367.0).
  Also checked: FY2023 OCF 376 and FY2024 OCF 290 (filed statements) equal the tool's lines.
- `python tools/run.py WH`, arithmetic lines only (Part VII): OCF 376 / 290 / 367 (2023-2025); SBC 39 / 45 / 43; capex
  37 / 49 / 46; D&A 76 / 71 / 62; finance-lease principal 5 (2023) and 39 (2024) flagged as an alternate the tool does not
  choose. The tool's three-year means and yields are not used; Q4 and Q7 recast owner cash from the filed statements over
  the full span. Ten balance sheets 2016-2025 are printed by the tool and read at Q4 against the filed statements.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is **who is paid to tell you**: the filer's own featured number is "adjusted EBITDA"
($718M FY2025), which adds back stock pay, development advance note amortization (the cost of the cash the company pays
hotel owners to sign) and the Revo losses, and its stated use includes "the evaluation of selected compensation decisions"
(10-K FY2025, Item 7). The foundations say not to take a seller's projection of what he sells **[M2011-083]**; the run
recasts every figure from the cash statements. **A share is a business:** the test is whether I would be content to own it
"if the market closed for five years" **[M1997-109]**, which turns the run onto the franchise system's economics and away
from the price, which fell from $113.07 to $69.21 inside 2025 (10-K Item 1A). **Margin of safety** is carried as an
attitude here and an arithmetic at Q7 **[M1997-126]**. No macro forecast enters **[M2000-094]**: the hotel cycle enters
only through the filed figures.
**Contrary evidence, written down as found** **[M1997-127]**:
1. U.S. rooms 510,200 at end-2019 and 505,100 at end-2025; U.S. properties 6,342 and 5,934 (10-K FY2019 selected data,
   `0001722684-20-000007`; 10-K FY2025 Item 7). The home system, 77% of royalties, is smaller in rooms than six years ago.
2. U.S. RevPAR $46.39 (2019), $50.72 (2022), $48.44 (2025): six years of nominal RevPAR growth of about 4% in total.
3. Payments of development advance notes (cash paid to owners to sign or convert) $19M (2019), $32M (2021), $52M (2022),
   $73M (2023), $114M (2024), $112M (2025); loans to franchisees a further $58M in 2025 (filed cash-flow statements).
4. Revo, a single European franchisee, filed for insolvency in January 2026; $160M of charges in FY2025 (10-K Note on
   Revo), including the Vienna House brand bought for $44M in 2022.
5. Deferred co-branded credit card revenue rose from $22M to $98M in 2025 (10-K, Deferred Revenues note): a partner's
   advance that lifts 2025 operating cash once.
6. Q2 2026 royalties and franchise fees $139M against $147M a year earlier (10-Q), "primarily due to lower franchise fees
   and the deferral of fees from Revo".

## THE STANDING RULE
The buyer is assumed to pay cash, unlevered, for a part-interest sized so that its total loss could not touch what he has
and needs **[M2012-081]**; nothing in the instrument (a listed common share) can make a sudden demand for cash on the holder
**[L2014-024]**. The rule is not engaged by the target; the target's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The business, from Item 1 (10-K FY2025).** Wyndham licenses 25 brands to over 6,200 franchisees owning 8,389 hotels and
868,900 rooms (ex the Super 8 China master licence); 77% of royalty contribution is U.S.; the brands sit in economy,
midscale and upper midscale, "primarily located in secondary and tertiary cities". A direct franchisee pays "a royalty fee
of approximately 5% of gross room revenue and a marketing and reservation fee of 2% to 4%"; agreements run "typically 10 to
20 years". The company also "strategically provide[s] financial support in the form of development advances or loans to
help generate new business". Wyndham Rewards has 122 million members, 53% of U.S. check-ins. About 2,000 employees; the
managed business was exited in the U.S. and folded into the single Hotel Franchising segment from 2023.

**The key variables** **[M1998-044]**: (1) rooms in the system, which is gross additions less deletions (2025: 71,600
added, 38,400 deleted); (2) RevPAR of those rooms; (3) the royalty rate actually collected; (4) what the company must pay
owners to sign and stay (development advance notes, loans, the marketing fund it must spend); (5) the co-brand card and
Travel + Leisure licence fees (ancillary revenue $317M in 2025). Each is a figure the 10-K reports every year, so "the
financial statements will tell me the information that's useful" about the future ones **[M2008-033]**, with the one
caution that RevPAR, rooms and royalty rate were restated in 2025 to drop the Super 8 China rooms.

**Is it foreseeable ten years out?** The forecast is about two sets of customers, hotel owners choosing a flag and
travellers choosing a room, not about a technology **[M2017-019]**: a select-service hotel in a secondary U.S. town is the
kind of thing where one can "project out in terms of consumer behavior and threats to a business" **[M2023-030]**. I do
not need the hotelier's trade; what is needed is "the economic dynamics of the industry" **[M2011-014]**, and those are
legible: a franchisor rents a name, a reservation system and a loyalty base for a share of room revenue, and its capital is
the money it advances to owners. The one variable that could move fast is distribution (online travel agents and, named
new in this 10-K, large language models "a rapidly evolving space"); that bears on whether the castle holds and is read at
Q2, not here, since it does not make the ten-year economics unreadable, it is the main threat to them **[M1999-063]**.
Insiders would write a ten-year forecast of rooms, RevPAR and fee rates down (the 10-K itself states a 2026 room-growth goal
of 4.0% to 4.5%), which is the test the tech field fails **[M2000-105]**. Is it important and knowable **[M2006-076]**: yes
on every variable above.

**Doubt about the perimeter** **[M2002-092]**: the one item I could not read to the bottom is the loyalty liability
(estimated by a third-party actuary) and the franchisee credit book; both are disclosed and small against revenue, and
neither puts the business outside the circle.

**VERDICT: IN.** A franchisor of select-service hotels whose economics are fixed by rooms, RevPAR, fee rate and the price of
signing owners, all reported annually (10-K FY2025, `0001722684-26-000007`, Items 1 and 7); "a reasonable fix on about what
the earning power and competitive position will look like in five or 10 years" is available **[M2012-065]**, and whether the
castle holds is Q2's question.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**Lines of evidence chosen, and why** (the brief's one departure: derived from Item 1, Item 1A and Item 7 of the FY2025
10-K). Item 1 says franchisees decide "based principally upon the perceived value and quality of the brand and the services
offered" (Competition) and that the company pays owners to sign (development advances and loans); Item 1A names the
threats as competition for franchisees that "may reduce fee structures, potentially causing us to lower our fees and/or
offer other incentives", online intermediaries and LLMs, alternative lodging, and franchisee credit; Item 7 calls rooms,
RevPAR and royalty rate "drivers of our revenues". So the castle is read on six lines: (1) U.S. rooms and properties over
the cycle (77% of royalties); (2) U.S. RevPAR; (3) the royalty rate and the core fee revenue it produces; (4) the price of
signing owners (development advance notes and loans) against the rooms gained; (5) the loyalty programme's share of stays,
the defence against intermediaries; (6) the field's returns on tangible capital and its unit and fee growth, from three
rivals' own filings.

**Rivals.** The 10-K names no rival company: Item 1 says only "We encounter competition among hotel franchisors and lodging
operators", and a text search of the whole 10-K for Choice, Marriott, Hilton, IHG, InterContinental, Hyatt, Airbnb,
Expedia and Booking found none. **CONVENTION of this run:** the three rivals are Choice Hotels (CHH), Hilton (HLT) and
Marriott (MAR); rationale: they are the three SEC-filing hotel franchisors with large U.S. franchised systems, and Choice
is the one in the same economy and midscale chain scales. IHG (a 20-F filer, not read) and Hyatt are not used. Rival 10-Ks
read: CHH FY2025 `0001046311-26-000008` and FY2019 `0001046311-20-000011`; HLT FY2025 `0001585689-26-000007` and FY2019
`0001585689-20-000013`; MAR FY2025 `0001048286-26-000007` and FY2019 `0001628280-20-002376`; balance-sheet and income lines
for the years between from each filer's 10-K XBRL company facts (`cache/cf_*.json`, transcription, checked against the
FY2019 and FY2025 statements for the end years).

**The castle tests, each with its filing fact.**
- *What keeps it standing* **[M1995-038]**: 10-to-20-year contracts with over 6,200 owners whose hotels sit where
  "approximately 80% of the U.S. population lives within ten miles of at least one of our affiliated hotels", a reservation
  system and a loyalty base; the owner pays about 5% royalty plus 2% to 4% marketing for it (Item 1). It does not rest on
  "the genius of the lord in the castle": the fee stream ran through a CFO departure, an interim CFO, a new CFO and a
  Chief Accounting Officer's departure inside nine months (8-Ks above).
- *The attacker with money* **[M2011-015]**: the one recorded attacker bid for the castle rather than against it (the
  "unsuccessful hostile takeover attempt", Item 1A; $47M of defence payments in 2024, Item 7). The attack on the franchise
  base is made with money owners are paid to switch: competition "may require us to reduce or change fee structures, make
  greater use of financial incentives, including franchise agreement acquisition costs, loans and guaranties to acquire
  franchisees" (CHH 10-K FY2025, Item 1A), and Wyndham answers in kind. Its payments of development advance notes were $19M
  (2019), $17M (2020), $32M (2021), $52M (2022), $73M (2023), $114M (2024), $112M (2025); loan advances a further $29M
  (2023), $17M (2024), $58M (2025) (filed cash-flow statements). The balance of development advance notes: $108M (2021),
  $144M (2022), $228M (2023), $308M (2024), $343M (2025) (10-K notes).
- *Pricing power and the agony before a rise* **[M2005-020]**: the U.S. royalty rate rose 4.37% (2015), 4.51% (2019), 4.62%
  (2021), 4.59% (2023), 4.76% (2025) (selected data of the FY2019 and FY2025 10-Ks). That line reads for the castle. Against
  it: the rate is computed "excluding the impact of amortization of development advance notes", which is deducted from
  royalty revenue ($11M in 2021, $32M in 2025); core royalty and franchise-fee revenue was $480M in 2019 and $541M in 2025,
  12.7% more in six years in nominal dollars, while U.S. RevPAR went from $46.39 to $48.44, 4.4% in six years. In Q2 2026
  royalties and franchise fees were $139M against $147M a year before (10-Q). A contract rate that rises while the money
  collected per room barely moves in nominal terms is not the business that can "charge more for a product and maintain or
  increase market share against wellentrenched, well-known competitors" **[M2000-031]**.
- *Unit volume* **[M1999-107]**: U.S. rooms 510,200 (2019), 487,300 (2020), 490,600 (2021), 505,100 (2025), 501,100 (June
  2026, "flat year-over-year", Q2 2026 release, exhibit 99.1 of `0001722684-26-000072`); U.S. properties 6,342 (2019),
  6,139 (2021), 5,934 (2025). Global rooms grew (2025: 4%, "including 1% growth in the U.S. and 7% growth" in EMEA and
  Latin America), but the growth is international, at a royalty rate of 2.5% against 4.8% in the U.S. (Item 7). Every year
  about 4% of rooms leave: deletions 38,900 (2021), 38,000 (2022), 33,000 (2023), 31,400 (2024), 38,400 (2025) against
  additions of 53,100 to 71,600 (portfolio tables, FY2021, FY2023 and FY2025 10-Ks; 2023 on the recast basis). Over
  2021-2025, 179,700 rooms left and 319,300 came in, so 56% of the rooms signed only replaced rooms lost.
- *Share of mind* **[M1997-099]**: Wyndham Rewards accounted for "over 40%" of U.S. occupancy in 2019 (FY2019 10-K), 47% in
  2021 (FY2021 10-K) and "over 53%" of U.S. check-ins in 2025 (FY2025 10-K, Item 1); 122 million members. This is the
  evidence for the castle against the intermediary: a direct link to the traveller that a single owner cannot build. The
  rows name the battle: to the extent the customer trusts the intermediary as much, "the value of having the brand moves
  over to the retailer from the product itself" **[M2001-090]**; Item 1A says intermediaries "may be able to obtain higher
  commissions and reduced room rates" and that LLM providers "may choose to source their information from third-party
  travel intermediaries instead of directly from us". "the brand is our protection against the intermediaries making all
  the money" **[M2019-041]**: the rising loyalty share says the protection is holding.
- *Would the customer choose it over the low bid* **[M2017-009]**: the owner's choice is renewed at contract end and is
  bought, more each year, with cash; the economy traveller chooses largely on price, often through channels the company
  does not own. Retention: "Our 2023 global retention rate was 95.6%" (FY2023 10-K, Item 1).
- *Ask the competitors* **[M1999-130]**: the rival that tried to buy Wyndham in 2023-24 answered the desert-island question
  for it; that is a statement of the system's value to a rival, not of its moat against rivals, and it is not weighed
  further.

**The competitor row, same metrics from the competitors' own filings (2019 to 2025).**

| Metric | WH | CHH | HLT | MAR |
|---|---|---|---|---|
| System rooms 2019 → 2025 | 831,000 → 868,900 (2025 ex Super 8 China; on the old basis 2019 → 2024: 831,000 → 903,000, +8.7%) | 590,897 → 656,825 (+11.2%, includes Radisson Americas bought 2022) | 971,780 → 1,351,351 (+39.1%) | 1,380,921 → 1,779,936 (+28.9%) |
| U.S. rooms 2019 → 2025 | 510,200 → 505,100 (−1.0%) | 462,973 → 496,979 (+7.3%, includes Radisson) | not taken | not taken |
| Core franchise fees 2019 → 2025 | royalties and franchise fees $480M → $541M (+12.7%) | caption changed in 2025, not comparable | franchise and licensing fees $1,681M → $2,780M (+65%) | franchise fees $2,006M → $3,325M (+66%) |
| Cash paid to sign owners in 2025, against core fees | development advances $112M = 21% of $541M | franchise agreement acquisition costs, net, $83M = 12% of franchise and management fees $673M | contract acquisition costs, net, $231M = 8% of $2,780M | contract acquisition costs $434M = 13% of franchise fees (8% of gross fees $5,438M) |
| Pre-tax return on tangible capital (operating income over total assets less goodwill, intangibles and cash), 2019 / 2023 / 2025 | 32% / 58% / 36% (51% before the Revo charges); 67% in 2022 | 35% / 28% / 30% | 46% / 51% / 51% | 25% / 53% / 52% |

The return line is computed in `rotc.py` (research folder) from each filer's own 10-K figures. It flatters CHH and MAR
against WH: their payments to owners are capitalized as intangibles and drop out of the capital, while Wyndham's
development advances sit in other non-current assets and stay in. Taking Wyndham's advances out of its capital to match:
56% (2021), 81% (2022), 79% (2023), 67% (2024), 53% (2025), 74% in 2025 before the Revo charges.

**The parts table.** One reportable segment, Hotel Franchising, carries all net revenue and all segment profit (adjusted
EBITDA $781M against Corporate $(63)M in 2025, Item 7); the ancillary streams (co-brand card, the Travel + Leisure licence)
sit inside it and the filer reports no separate capital for them. The file closes on the one part.

**The field's returns over the last full cycle, judged in words.** The field's durable players earn excellent returns on
the tangible capital the business needs, on both sides of the 2020 trough: Hilton about half its tangible capital before
tax in every year read, Marriott the same since 2022, Choice about a third, Wyndham between a third and two thirds. This is
not a standing castle that protects only ordinary returns; the castle protects "excellent returns on invested capital"
**[L2007-004]**.

**Widening or narrowing** **[M1999-108]**, **[M2000-075]**: on the evidence, narrowing at home and bought abroad. The home
system is smaller in rooms than in 2019 while Hilton and Marriott grew their systems by about a third and their franchise
fees by about two thirds; Wyndham's core fees grew an eighth; the cash it pays owners to sign rose about sixfold since 2019
and is the highest share of core fees of the four; its return on tangible capital, the highest of the four in 2022, fell in
each year since. The rows' word for this is the notch: "the industry retains its excellent economics, but has lost still
another notch" **[L1995-023]**. What holds the other way: the U.S. contract royalty rate is the highest in the span, the
loyalty programme's share of stays rose in every year read, and a rival offered a premium for the whole system.

**What could destroy, modify or reduce it** **[M2000-014]**: the intermediary (online agents, and the LLM channel the 10-K
now names); a key-money contest in which the system is kept only by paying owners more each year, the moat "that must be
continuously rebuilt" **[L2007-005]**; and franchisee credit, which Revo has shown can cost $160M in one year.

**Verdict reasoning.** The castle is standing on the evidence: a contracted fee stream from over 6,200 owners, retention
near 96%, a rising contract rate, a loyalty base that carries more of the stays each year, and returns on the capital
needed that are excellent and in line with the field. It is not shown open, so the file does not close OUT; its threats
are named and measurable year by year from the filings, so it is not a moat whose future cannot be judged, the case in
which "We don’t know how to valuate that" **[M2000-019]**. But it is a narrowing castle, and the narrowing is in the
numbers that feed value: the money paid to keep and fill the system rises faster than the fees it collects. That is
carried to Q3 and Q7 as the capital and growth inputs, not used here to close the file.

**VERDICT: IN, narrowly.** The castle stands and protects excellent returns **[L2007-004]**; it has lost a notch on unit
growth, fee growth and the price of signing owners against all three rivals **[L1995-023]**, carried forward.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**: operating income over total assets less
  goodwill, trademarks, franchise-agreement intangibles and cash: 32% (2019), 50% (2021), 67% (2022), 58% (2023), 47%
  (2024), 36% (2025; 51% before the $160M Revo charges), pre-tax (`rotc.py`; filed balance sheets and income statements).
  The capital needed is small: property and equipment $104M, receivables $291M, development advances $343M, net loans $33M
  at end-2025. On that test this is close to the first of the three grades, the business that gives "more and more money
  every year without putting up anything to get it, or very little" **[M1998-081]**.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**: the capital the business must keep putting
  in is not its capital expenditure ($37M to $49M a year, "primarily related to information technology", Item 7) but the
  cash paid to owners to sign and convert: development advances net of proceeds $30M (2021), $48M (2022), $72M (2023),
  $109M (2024), $105M (2025), guided to "approximately $110 million for 2026", and loans net $29M (2023), $16M (2024),
  $57M (2025). The filing does not split it between keeping the system and growing it. **CONVENTION of this run (the
  maintenance guess the rows ask for):** the share of each year's developer support that maintains the system is the share
  of that year's gross room additions that only replaced deleted rooms (deletions over additions, from the portfolio
  tables); rationale: the filing gives both counts every year and no other split, and a room signed to replace a room lost
  keeps the system where it was. On that guess 56% of 2021-2025 developer support was maintenance. That spending is
  compulsory in the rows' sense, since a franchisor that stops paying owners loses about 4% of its rooms a year
  (deletions, Q2), the "compulsory reinvestment just in order to stand still" **[M1997-016]**.
- **What the added capital earned** **[M2001-019]**: from 2022 to 2025 tangible capital rose from $831M to $1,103M (+$272M),
  mostly development advances and loans, while operating income before the 2022 asset-sale gain and the 2025 Revo charges
  went from $523M to $562M (+$39M): about 14% pre-tax on the increment, against 63% on the 2022 base. Owner cash fell
  over the same years (Q7 table). Fee revenue grew 1.8% a year from 2022 to 2025 ($1,354M to $1,429M). The rows' warning
  fits: earnings that rise because "We just put way more capital into the business" are not a higher return **[M2023-081]**;
  here operating income did not even rise much.
- **The growth arithmetic and its caps**: shown growth in owner cash over the window is negative (Q7), so no cap binds;
  fee revenue growth of 1.8% a year is the business's own sales growth and is used at Q7 only as a case beside.
- **WEIGHS AGAINST.** The business needs little capital and earns very high returns on it **[M1998-081]**, but the
  capital that must now go in each year to hold and fill the system has tripled since 2021 and the increment since 2022
  has earned about a seventh of its cost before tax, so the added money is not earning "a very satisfactory rate"
  **[M1998-081]**. The "little or no debt" criterion is applied at Q9.


## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]** (`tools/run.py` table, read against
the filed balance sheets of the FY2019, FY2021, FY2023 and FY2025 10-Ks and the Q2 2026 10-Q; USD millions):

| Year-end | Total assets | Goodwill | Trademarks + franchise intangibles | Cash | Receivables | Debt | Equity | Other non-current assets |
|---|---|---|---|---|---|---|---|---|
| 2016 | 1,998 | 377 | n/a (carve-out) | 30 | n/a | 0 | 1,086 | n/a |
| 2017 | 2,137 | 423 | n/a | 57 | 194 | 0 | 1,262 | n/a |
| 2018 | 4,976 | 1,547 | 1,397 + 590 | 366 | 293 | 2,141 | 1,418 | n/a |
| 2019 | 4,533 | 1,539 | 1,395 + 551 | 94 | 304 | 2,122 | 1,212 | n/a |
| 2020 | 4,644 | 1,525 | 1,203 + 512 | 493 | 295 | 2,597 | 963 | 226 |
| 2021 | 4,269 | 1,525 | 1,202 + 473 | 171 | 246 | 2,084 | 1,089 | 243 |
| 2022 | 4,123 | 1,525 | 1,232 + 374 | 161 | 234 | 2,077 | 962 | 348 |
| 2023 | 4,033 | 1,525 | 1,232 + 347 | 66 | 241 | 2,201 | 746 | 468 |
| 2024 | 4,223 | 1,525 | 1,230 + 318 | 103 | 271 | 2,463 | 650 | 589 |
| 2025 | 4,182 | 1,525 | 1,208 + 282 | 64 | 291 | 2,560 | 468 | 628 |
| Jun 2026 | 4,332 | 1,525 | 1,208 + 269 | 69 | 331 | 2,675 | 480 | 685 |

What moved and why. (1) **2018: the La Quinta purchase** for cash, debt-financed: assets more than doubled, goodwill went
from $423M to $1,547M, debt from nil to $2.1B; one more deferred payment of $195M for La Quinta's tax liability ran
through 2019 operating cash. Since then goodwill has not moved and trademarks have only been impaired (2020; Vienna House
in 2025), so goodwill and the purchased intangibles are 72% of total assets ($3,015M of $4,182M at end-2025), and nothing
has been added to them since but Vienna House (bought for $44M in 2022), whose trademark was written from $33M to $7M in 2025. (2) **Equity fell from $1,418M to $468M while retained earnings stayed positive ($471M)**:
$1.9B of buybacks at an average $69.37 since 2018 (Item 7), plus dividends, were paid out of earnings and new debt; in
Q4 2025 the company retired 28 million treasury shares at cost $1.9B, which is why treasury stock and paid-in capital both
collapsed on the 2025 balance sheet. Tangible equity is deeply negative. (3) **Debt** stayed near $2.1B from 2018 to 2022
and rose to $2.68B by June 2026, all of it after the system had stopped growing in the U.S. (4) **Receivables** are flat
with revenue ($293M in 2018, $291M in 2025, $331M at the seasonal June 2026 peak) against fee-related revenue of about
$1.4B throughout; no sign of revenue booked ahead of cash. (5) **Other non-current assets tripled**, $226M (2020) to $685M
(June 2026), and this is the line that "the figures are saying": development advances ($92M to $343M), loans to
franchisees, capitalized contract costs ($84M) and, from 2026, two hotels taken from Revo. A deferred-asset account
building up is the first tell the rows name, to be looked at twice **[M1995-064]**; here it is explained, line by line, by
cash payments that the cash-flow statement shows inside operating activities, amortized against revenue, and impaired
when a franchisee failed ($48M of Revo advances), so it reads as a real and rising cost of the business, not as a hidden
one. (6) What the balance sheet cannot say: it is not cumulative across restatements of the system (the Super 8 China rooms
were dropped from all statistics in 2025) or across the exit from the owned and managed hotels (two owned hotels sold for
$263M in 2022; cost-reimbursement revenue $320M in 2021, nil in 2025), so revenue and RevPAR before and after are not on
one basis.

**The real costs.**
- *Depreciation and capital expenditure*: D&A ($62M in 2025) is mostly amortization of purchased franchise agreements;
  capital expenditure is $37M to $50M a year. Owner cash below charges all capital expenditure.
- *The cost of signing owners*: development advances are cash paid out and recovered, if at all, as forgiven notes over the
  franchise term; their amortization is deducted from royalty revenue ($32M in 2025). The cash, not the amortization, is
  charged in owner cash, and the loans in investing are charged as well.
- *Stock pay*: $43M in 2025 (cash-flow add-back), charged in owner cash **[L2015-003]**.
- *Restructuring*: "restructuring and other-related" $15M (2024), $18M (2025) and $10M in the first half of 2026: three
  years running, which the rows say is not to be waved away **[L2016-007]**; it is inside owner cash.
- *Revo*: $160M of charges in 2025; the cash had already gone out as advances, loans and unpaid receivables in earlier
  years and is inside those years' owner cash.
- *Interest*: $142M paid in 2025, inside operating cash; added back after tax for the all-equity basis at Q7.
- *A one-off inflow*: deferred co-branded credit card revenue rose from $22M to $98M in 2025, "payments received in advance
  from the Company’s co-branded credit card partners, primarily for card member activity" (Deferred Revenues note); the $76M
  rise lifted 2025 operating cash once and is removed from the 2025 base at Q7 (specific (d)).

**EBITDA in the filer's own mouth.** The featured figures are adjusted EBITDA ($718M), adjusted diluted EPS ($4.58 against
GAAP $2.50) and "adjusted free cash flow" ($433M against operating cash of $367M). Adjusted EBITDA adds back stock pay,
development advance amortization, impairments, the Revo charges, restructuring and "transaction-related" items, and the
company says it uses it "in the evaluation of selected compensation decisions" (Item 7). "Free cash flow" is defined as
"net cash provided by operating activities excluding development advances, less capital expenditures", and the adjusted
version further excludes the takeover-defence and separation payments (Q4 2025 release, exhibit 99.1 of
`0001722684-26-000004`). So the headline cash figure leaves out the very cost that Q3 shows is the business's compulsory
reinvestment, about $105M a year: "I’ll look at that figure when you tell me you’ll make all the capital expenditures"
**[M2003-108]**; EBITDA as a figure "before the cash requirements and merely staying in the same place" **[M1998-086]**.
The Q2 2026 release is headed "REPORTS STRONG SECOND QUARTER RESULTS" in a quarter when royalties and franchise fees fell
5% and U.S. rooms were flat, and announces "Company Raises Full-Year 2026 Outlook": the company guides annually (a 2026
outlook with an effective tax rate of "approximately 25%"). Featured adjusted figures and guidance weigh against here and
are carried to Q5 **[L2016-006]**, **[L2019-006]**.

**Confusion or suspicion?** None found that the statements raise. Every adjusted figure is reconciled to GAAP in the
filing; the deferred-asset build is explained by disclosed cash; receivables move with revenue; the Revo loss was reserved
and impaired in the year it became known; no restatement was found in the four 10-Ks read. The accounts are legible, and
the business's real earnings can be recast from the cash statements, which is what Q7 does. The preoccupation with
adjusted figures is "a negative" but not "a total exclusionary factor" **[M1994-018]**.

**VERDICT on the accounts: WEIGHS AGAINST** (no STOP: no confusion, no suspicion raised by the statements). The cash
statements show what it earns; the company's own headline cash and earnings figures leave out the cost of signing owners,
stock pay and recurring restructuring, which is carried to Q5. The recast owner cash feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**The people.** Geoffrey Ballotti, 64, CEO since the 2018 spin-off and of the hotel group since 2014; a Starwood veteran.
Non-executive chair Stephen Holmes, 69, chair since 2018 and also non-executive chairman of Travel + Leisure, which pays
Wyndham licence fees; lead director James Buckman, also Travel + Leisure's lead director (proxy, `0001722684-26-000050`;
the 10-K's own risk factor names the conflict). The finance chair has turned over: the CFO and head of strategy left on
2025-11-04 "to pursue a new career opportunity outside the hotel industry", an interim CFO served to 2026-03-03, a new
CFO (formerly Chief Development Officer, North America) took over, and the Chief Accounting Officer of the company and its
predecessor since 2006 left on 2026-07-31, replaced by the controller (8-Ks above). On 2026-05-18 the CEO disclosed that he
is being treated for multiple myeloma and "plans to continue working largely as normal".

**The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt and against the competitors*: the
hand was a franchise system of about 800,000 rooms with high returns and little capital need. Against the three rivals
over 2019-2025 (Q2 table), Wyndham's U.S. system shrank while Choice's, Hilton's and Marriott's grew; its core fees grew
an eighth against two thirds at Hilton and Marriott; it pays the most, as a share of fees, to sign owners; and it lost
$160M on one European franchisee (Revo) to which it had lent and advanced money through 2025, learning of the insolvency
while "in the process of preparing its financial statements" (10-K, Revo note). *How they treat the owners*: read in the proxy
and the releases, below.

**The tells of dishonesty, applied on doubt** **[M2013-088]**.
- *Reports that dance; the key figure* **[M2007-082]**: the key figure of a franchisor that pays owners to sign is what it
  pays for each room it keeps and adds. That figure is in the cash-flow statement (operating activities) and in the
  outlook ("approximately $110 million for 2026"), not hidden; but the headline "free cash flow" is defined to exclude it
  (Q4). I read this as the preoccupation the rows call "a negative" **[M1994-018]**, not as a figure left out or touched on
  dishonestly: the definition is printed beside the number, and the advances are stated in the MD&A in dollars.
- *Targets made and guidance* **[L2002-041]**, **[L2019-006]**: the company guides each year. The record is mixed, not
  consistently made: the proxy states 2025 adjusted EBITDA "was $27 million below our original full-year outlook of $745
  million to $755 million", and the bonus tier for adjusted EBITDA paid 0%. A company that misses its own outlook and says
  so in its proxy is not the "consistently reach their declared targets" case.
- *How they talk about mistakes* **[L2024-003]**: Revo is described in the filings as the franchisee's failure ("its
  inability to successfully execute on integrating its acquisitions as well as higher than expected operating costs");
  no filing read says the company erred in lending to it or in buying Vienna House in 2022, whose trademark was written
  down by $26M of its $33M. The Q2 2026 release is headed "REPORTS STRONG SECOND QUARTER RESULTS" in a quarter in which
  royalties and franchise fees fell 5%. That is a promotional voice; it is not a misstatement, since the release gives the
  royalty figures.
- *The proxy: how they treat themselves against the owners* **[M1994-009]**: CEO total pay $13.55M in 2025 (Summary
  Compensation Table), of which $12.0M stock awards; long-term grant values were raised 5% to 20% for 2025. The CEO asked
  for and received a zero bonus for 2025 when the EBITDA tier paid nothing, and owns 832,015 shares (1.11%, proxy), about
  $61M at the price, much of it from grants. The committee used "positive discretion" to pay staff below the named
  officers 25% of target although their only metric paid 0%.
- *Fixation on the stock price* **[M2004-067]**: the board rejected Choice's offers of $80, $85 and $90 a share in 2023 as
  ones that "substantially undervalued Wyndham" and spent $47M defending; it then bought back stock at $85.73 on average in
  2025. That is a view of value, held consistently; it is weighed at Q6 as capital allocation, not here as dishonesty.

**Integrity judged.** I find no fact that raises doubt about honesty: the accounts reconcile, the misses are disclosed,
the CEO declined his own bonus in a missed year, the Revo loss was recognized in the year it became known, and the
CEO's illness was disclosed by 8-K the day he told his staff. The habits carried from Q4 (adjusted figures featured, a
"free cash flow" that excludes the cost of signing owners, annual guidance) "make us nervous" in the rows' word
**[L2016-006]** and weigh against the people, but they are disclosed habits of presentation, not a dishonest report; the
rows separate the two **[M1994-018]**.

**Ability, love of the business, the same after being paid.** For a marketable stake the reading tests carry the weight
**[M2007-081]**. Love of the business: a CEO with 22 years in the franchise and a large holding. Ability: the record
against the hand dealt is the weakest of the four franchisors on unit growth, fee growth and the price of growth; the
Revo loss shows credit judgment that failed on its largest single exposure; and the finance function lost its CFO and its
Chief Accounting Officer within nine months of each other, around the year of that loss. The moat and the managers enter
value as "the degree of certainty" of the stream **[M1999-104]**; here they lower it.

**VERDICT on integrity: IN** (no doubt about honesty found; the presentational habits weigh against). **Ability: WEIGHS
AGAINST** **[M1994-008]**, **[L2010-002]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *The retention test* **[M1998-110]**: little is retained. Over 2019-2025 net income totalled $1,395M; dividends paid
  $730M and buybacks $1,816M, together $2,546M (filed cash-flow statements). Owner cash before acquisitions over the same
  years was about $1,461M (Q7 table, the 2025 card advance removed). So the company paid out about $1.1B more than it
  earned in owner cash, funded by debt (total debt $2,122M at end-2019, $2,675M at June 2026), the $263M sale of two owned
  hotels in 2022, and running cash down from $366M (2018) to $69M. The question for this company is not whether a kept
  dollar becomes more than a dollar but what the borrowed and distributed dollars bought.
- *Deals: value given against value got* **[M1995-001]**: La Quinta's franchise business, 2018, about $1.95B in cash
  (FY2019 10-K: acquisition of business $1,703M in 2018 plus the $195M tax liability paid in 2019); since then U.S. rooms
  have not grown (Q2) and goodwill has not been impaired. AmericInn, 2017 ($140M cash). Vienna House, 2022 ($44M cash),
  whose trademark and franchise agreements were impaired by $38M in 2025 when Revo, the franchisee that operated it,
  failed. All paid in cash; no share issuance (shares outstanding fell from about 100M in 2018 to 74.2M), so the STOP on an
  all-stock deal in undervalued stock does not arise, and the serial-issuer tell is absent **[L2014-015]**.
- *Buybacks* **[L1999-023]**, **[L2016-002]**: an authorization in dollars ($300M in 2018, raised by $300M, $800M, $400M and
  $400M) with "no termination date" and no stated price above which buying stops (Item 5). Prices paid: $69.37 average
  since inception; $85.73 in 2025; $76.07 in Q4 2025; $80.31 in the first half of 2026 (10-K Item 7, 10-Q). The buying
  was done with borrowed money while the business's own "near-term needs" (development advances and loans of $162M in 2025)
  were rising, so the first of the two conditions, funds "beyond the near-term needs of the business", was met only by
  borrowing. *The price test against the bottom of the Q7 range (written back at Q7, 2026-10-14):* every price paid ($69.37 average since
  inception, $85.73 in 2025, $76.07 in Q4 2025, $80.31 in the first half of 2026) is above the bottom of the Q7 range
  ($34.94 a share, all-equity) and above its top ($42.59); so the programme is read by its announcement, which names no
  price, and it weighs against. The board's refusal of $90 a share was a refusal of more than twice the top of the range.
- *The takeover defence*: the board refused $90 a share (cash and Choice stock) in 2023-24 as an offer that "substantially
  undervalued Wyndham" (Schedule 14D-9, `0001140361-23-058002`) and spent $47M defending; this is a judgment of value by the
  board and is read against the Q7 range at Q7.

**Part B: the pay, the board, the owners.**
- *Pay tied to what the person controls* **[M2003-019]**, **[M2016-083]**: the annual bonus is 75% adjusted EBITDA and 25%
  global net room growth (proxy); the performance shares vest on "earnings before interest and taxes [...] per share, as
  adjusted"; most other officers' long-term pay is time-vested restricted stock (75%). The two annual metrics reward rooms
  added and an EBITDA that adds back the amortization of the cash paid to add them, so the measured result rises with
  spending whose cost is outside the measure: "you get what you reward for". A per-share EBIT target rises with
  debt-financed buybacks. The committee raised grant values 5% to 20% in a year the EBITDA metric paid nothing.
- *The board*: chair and CEO separated, with a non-executive chair; but the chair and the lead director are also the chair
  and lead director of Travel + Leisure, the licensee whose royalties are part of Wyndham's ancillary revenue, a conflict
  the 10-K itself discloses. Directors' holdings are 25,000 to 107,000 shares each, plus the chair's 373,782 (proxy); the
  proxy does not say which were bought with the directors' own money **[L2019-008]**.
- *The owners as partners*: annual guidance and adjusted figures featured (Q4, Q5); dividends raised every year since 2021
  ($0.88 to $1.64 a share; $0.43 a quarter from 2026).
- **WEIGHS AGAINST** on both parts. Part A: more than everything earned was paid out, partly borrowed, in buybacks with no
  stated price at $70 to $86 a share, and the one recent purchase (Vienna House) was largely lost **[L2016-002]**. Part B:
  pay rewards rooms and adjusted EBITDA, which leave out the cost of buying the rooms **[M2016-083]**, and the board's
  leadership sits on both sides of the Travel + Leisure licence.

## Q7 — WHAT IS IT WORTH? STOP.
**How much cash, how sure, how soon, at the long government rate** **[L2000-021]**, **[M2009-004]**; value is "the
discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**, net of what
must be put back in **[M2014-068]**. Arithmetic in `calc.py`, output in `calc_out.txt` (research folder). USD millions.

**Owner cash after every real cost, by year** (filed cash-flow statements of the FY2019, FY2021, FY2023 and FY2025 10-Ks):

| Year | OCF | SBC | Capex | Finance-lease principal | Loans to owners, net | Development advances, net (inside OCF) | Card advance removed | Owner cash, equity basis, all spending | Growth share of developer support (Q3 CONVENTION) | Owner cash, maintenance only | Interest paid after 25% tax | All-equity, all spending | All-equity, maintenance only |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | 295 (filed 100 + $195M La Quinta tax, an acquisition payment) | 20 | 50 | 5 | 2 | 17 | 0 | 218.0 | 6.3 | 224.3 | 75.0 | 293.0 | 299.3 |
| 2020 | 67 | 21 | 33 | 5 | −2 | 16 | 0 | 10.0 | 0.0 | 10.0 | 75.8 | 85.8 | 85.8 |
| 2021 | 426 | 28 | 37 | 5 | −3 | 30 | 0 | 359.0 | 8.0 | 367.0 | 72.0 | 431.0 | 439.0 |
| 2022 | 399 | 33 | 39 | 5 | 0 | 48 | 0 | 322.0 | 22.1 | 344.1 | 61.5 | 383.5 | 405.6 |
| 2023 | 376 | 39 | 37 | 5 | 29 | 72 | 0 | 266.0 | 46.2 | 312.2 | 77.2 | 343.2 | 389.4 |
| 2024 | 290 | 45 | 49 | 39 (incl. $34M HQ purchase) | 16 | 109 | 0 | 141.0 | 63.1 | 204.1 | 94.5 | 235.5 | 298.6 |
| 2025 | 367 | 43 | 46 | 0 | 57 | 105 | 76 | 145.0 | 75.1 | 220.1 | 106.5 | 251.5 | 326.6 |

Notes. Owner cash is operating cash less stock pay, capital expenditure, finance-lease principal and net loans to owners;
development advances are already inside operating cash. Acquisitions (the 2019 La Quinta tax payment, $195M; Vienna House
in 2022, $44M) and the 2022 sale of two owned hotels ($263M) are outside the columns and treated under specific (c) below.
Interest paid is from the debt notes ($100M, $101M, $96M, $82M, $103M, $126M, $142M); the 25% tax rate on it is the filer's
own outlook rate ("approximately 25%", Q4 2025 release). Tax is the company's own: owner cash is after cash taxes paid
($73M in 2025, $95M in 2024 and 2023); no carryforward or credit expiring inside ten years was found that would call for
the statutory-rate CONVENTION (section E). 2024 carries $47M of takeover-defence payments; they are a real cost and stay in.

**The six specifics, applied.**
- *(a) Cycles.* The first year of the five-year window, 2021, is aberrational on the filer's own description: "Our 2021
  adjusted EBITDA recovered to 95% of 2019 levels" and "our business was able to substantially recover from COVID’s impact
  during 2021" (FY2021 10-K, Item 7); its owner cash is the highest of the seven years because 2020's working capital
  unwound into it. So the base is the last full cycle, 2019 (the pre-pandemic year) through the 2020 trough to 2025
  **[L2005-003]**. Seven years: all-equity all-spending average **$289.1M**, maintenance-only **$320.6M**. The literal window
  2021-2025 is shown beside.
- *(b) Decline.* Within the cycle there is only one cycle, so growth between successive cycles cannot be measured; the range
  is therefore the no-growth case alone, said so. Beside, on the literal window, the shown growth is negative: all-equity
  all-spending owner cash averaged $385.2M in 2021-22 and $243.5M in 2024-25, a rate of −14.2% a year between the halves
  (−9.9% with the 2025 card advance left in); carried as the bottom of the literal range **[M2006-058]**.
- *(c) Acquisitions.* With no growth credited, no acquisition spending is charged (after growth stops, purchases stop with
  it). On the literal window the default pair deducts Vienna House ($44M, 2022); net purchases over the window ($44M) are
  far below half of owner cash, so the company is not a serial acquirer. The 2022 hotel sale ($263M) is a disposal of the
  owned-hotel business, not earnings, and is not credited to the base (crediting it would add $37.6M a year to the cycle
  average and about $9.11 a share to each end at 5.56%, leaving the top at $51.70; it does not change the close). No signed unclosed deal; no deal after
  the window (the two Revo hotels taken in 2026 by foreclosure were non-cash, $23M fair value; their $15M of mortgages are
  in net debt).
- *(d) Working capital.* Changes in working capital are inside operating cash each year. The one single-contract event is
  the co-branded card partner's advance ($22M to $98M of deferred card revenue in 2025, Deferred Revenues note), removed
  from 2025 ($76M) as aberrational; the range with it left in is shown beside.
- *(e) Growth spending.* The filing allows the maintenance guess (Q3 CONVENTION: the replacement share of each year's room
  additions); the maintenance-only case is the top, the all-spending case the bottom. On the literal window the growth bought
  is worth less than its cost (owner cash fell while the spending rose), so the inversion holds: "growth can destroy value"
  **[L2000-023]**.
- *(f) The cap.* No positive growth is carried, so no cap binds; the business's own sales growth (fee-related revenue
  $1,354M in 2022 to $1,429M in 2025, 1.8% a year) is used once below as a generous case beside.

**Net debt, all-equity basis** (Q7, On what the floor is earned): debt $23M current + $2,652M long-term = $2,675M less cash
$69M = **$2,606M** at June 30, 2026 (10-Q); operating leases left out; the $20M of Revo restricted cash is excluded, since
its release needs "certain court and insolvency administrator approvals". The 10-Q states no subsequent event that changes
it. Market value $5,449M; market value plus net debt **$8,055M**.

**Value range, central (all-equity, cycle base 2019-2025, no growth, at 5.56%):**
- bottom, all spending: $289.1M / 0.0556 = $5,200M, less net debt = $2,594M = **$34.94 a share**;
- top, maintenance only: $320.6M / 0.0556 = $5,766M, less net debt = $3,160M = **$42.59 a share**.
- Width 1.22 to 1. Equity-only beside (owner cash after interest against market value): $50.58 to $58.23 a share; higher
  than the all-equity figures because the debt costs less after tax (about 4%) than the 5.56% at which the cash is
  capitalized, the flattery of per-share figures by debt that the all-equity basis is there to remove **[L2017-004]**; it never decides alone.

**Beside: the literal window 2021-2025** (all-equity): top, maintenance only at no growth, $363.1M → $52.87 a share ($378.3M
→ $56.56 with the card advance left in); bottom, all spending at −14.2% for ten years then flat, −$8.94 a share ($2.41 with
the advance left in); all spending at no growth $42.47. **A generous case beside:** maintenance-only owner cash as filed
($378.3M) growing at the business's own sales growth, 1.8% a year, for ten years: $70.76 a share, still below the price.

**The floor is tested first** (Q7, CONVENTION of 2026-10-10). At $8,055M of market value plus net debt, the best case in the
central range (maintenance only, no growth) yields 3.98% a year; the best case on the literal window, 4.70%; the generous
growth case about 6.5% (4.7% yield plus 1.8% growth). No case earns about ten percent **[M2003-149]**; none earns even the
5.56% long Treasury. The price sits above the top of every range and every case beside it, which closes OUT however the range
is drawn. A width test is not reached. Nor is this a case for a pencil: the price would have to fall by about half to reach
the top of the central range and by far more to reach its bottom **[M2009-005]**.

**Fair price** (a reporting figure, never a verdict; Part VII): each end case valued at ten percent instead of 5.56%, the two
averaged, after the company's own tax. **All-equity (central): $5.96 a share** (all spending $289.1M / 0.10 − $2,606M =
$3.84; maintenance only $320.6M / 0.10 − $2,606M = $8.09). **Equity-only beside: $30.25 a share** (ends $28.12 and $32.38).
The two differ because, valued at ten percent, the whole business is worth little more than its debt.

**The Q6 buyback test, written back:** see Q6.

**VERDICT: OUT.** No case in the range earns the floor at $73.42; the price is above the top of the range ($42.59) and of
every case beside it **[M2003-149]**, **[L2013-012]**. Value range **$34.94 to $42.59** a share against **$73.42**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. A fact found is under AFTER THE STOP.

---
## THE BOX
**OUT at Q7.** Value range **$34.94 to $42.59** a share (all-equity, cycle base 2019-2025, no growth, at the 5.56% Treasury)
against **$73.42**; no case in the range or beside it earns the floor at the price (best case 4.0%; best case on the literal
window 4.7%). Q1 IN; Q2 IN, narrowly (a standing castle that has lost a notch against all three rivals); Q3 weighs against;
Q4 weighs against, no STOP; Q5 integrity IN, ability weighs against; Q6 weighs against on both parts. Fair price (reporting
figure, not a verdict): **$5.96** all-equity (central), **$30.25** equity-only. Q11 belongs to the holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]***.)*
- **Bears on Q8.** The 30-year Treasury at 5.56% (US Treasury par yield curve, 2026-10-13) exceeds the yield of every
  owner-cash case at the price (3.98% to 4.70% with no growth; about 6.5% in the generous growth case beside).
- **Bears on Q9.** Total debt $2,675M at June 30, 2026: term loan B $1.5B due 2030 (about 95% swapped to fixed at 3.31% to
  3.84% plus spread, the swaps expiring Q4 2027 to Q3 2028), $500M 4.375% notes due August 2028, $650M 5.625% notes due
  March 2033 (issued February 2026 to repay the revolver and term loan A), $27M drawn on a $1.0B revolver due 2030, $15M of
  mortgages on the two Revo hotels (10-Q). Ratings Ba1 / BB+ (10-K). One financial covenant: first-lien leverage at most 5.0
  times, 2.8 times at end-2025 (10-K). Interest paid $142M in 2025; pre-tax earnings plus interest over interest: 2.9 times
  in 2025, 4.0 times in 2024 (income statements). Net debt $2,606M against all-equity owner cash of $289M to $321M a year
  (Q7). The acquisition criterion "little or no debt" **[R1997-001]** is stated for whole businesses; the company carries
  debt of about eight to nine years of its owner cash before interest. Franchisee credit: development advances $343M and
  loans $88M gross ($33M net) at end-2025, and "a program that guarantees a portion of loans taken by franchisees for
  certain new construction projects" (10-K Item 1A); the largest single exposure (Revo, about 22,000 rooms) failed in
  January 2026.
- **Bears on Q12.** The 10-K discloses that the company and subsidiaries "have been named as defendants in litigation
  matters [...] alleging statutory and common law claims arising from purported incidents of human trafficking perpetrated
  by third parties at certain franchised facilities and hotels once managed by certain of our subsidiaries" (Item 1A); no
  amount is accrued that the run found, and the 10-K's estimate of exposure in excess of accruals for all legal matters is
  "up to approximately $7 million" (Item 7).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): commits
      for Step 0 to Q1, Q2, Q3, Q4, Q5, Q6, Q7 (with the Q6 buyback line written back), and the close.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's. The run binds
      nothing until the dispatcher folds it into the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Declared under contamination at
      the top: a date-filtered listing of `Test Runs/` that showed today's CHH, HLT and MAR run names, and a commit subject
      in the session context about the CHH fold. Neither was opened or used; the rival figures are from the rivals' own
      filings. No `Framework/v5/CASE` file was opened.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`, and every quoted fragment beside an id is in that row
      (`check_run.py` in the research folder: CLEAN); no E-ids. Every filing fact carries its document and accession.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance, and Q8 to Q12
      are NOT REACHED with their facts under AFTER THE STOP.
- [x] Owner cash after every real cost (stock pay, all capital expenditure, finance-lease principal, loans and advances to
      owners), never a net-income proxy; the sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations, items 1 to 6, and at each question).
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its yields, means and any printed rules were not.
- [x] `python tools/check_framework.py` PASS before the closing commit (run 2026-10-14 after the close was written:
      "PASS — every number resolves to a verbatim source or a confessed convention"); `check_run.py` CLEAN (81 ids, 94 citations).
- **Two CONVENTIONS of this run, confessed:** (1) the three rivals (Q2), since the 10-K names none; (2) the maintenance
  share of developer support as the replacement share of room additions (Q3, used at Q7). And one judgment that moves the
  range, not the box: 2021 read as aberrational under specific (a), which lowers the top from $52.87 (literal window) to
  $42.59.
- **What I could not get:** the 2025 annual report's chairman or CEO letter (the ARS is filed as a PDF, `a2025annualreport.pdf`,
  not read); IHG and Hyatt (not used); the U.S. room counts of Hilton and Marriott for 2019 (not taken); Choice's 2019
  core-fee figure on its 2025 caption (the caption changed); the split of development advances between conversions and new
  construction, and between keeping and adding rooms (the filing gives neither, hence CONVENTION (2)); the development
  advance balance at end-2019; any SEC enforcement or litigation history beyond the 10-K's own note.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (a) and a recovery year.** The filer calls 2021 a recovery year (earnings depressed, 95% of 2019 adjusted
EBITDA), but its owner cash is the highest of seven years because 2020's working capital unwound into it; (a) says the series
that defines the cycle is owner cash and the aberration is on the filer's description, and here the two point in opposite
directions. I took the filer's description, which drew in 2019 (with a $195M acquisition payment inside operating cash) and
the 2020 trough, and then (b) gave a no-growth range alone because one cycle has no successor. The top moved from $52.87 to
$42.59; the box did not move. A rule for which way to read a year that is low in earnings and high in cash would settle it.
(2) **Key money is neither capital expenditure nor working capital in the text.** For a franchisor the compulsory
reinvestment is cash paid to owners, inside operating cash; specific (e) asks for the maintenance guess "where the filing
allows", and the filing gives no split, so I confessed one. Two analysts could split it differently (all maintenance, all
growth, or by replacement share), and the top of the range moves by about $4 a share between the first two. (3) **Specific
(c) and a disposal that is not a business sale.** "Net of businesses sold" would credit the $263M sale of two owned hotels
to the base; I did not, as a liquidation of the owned-hotel business rather than earnings, and showed the effect beside
($9.11 a share). The text does not say. (4) **A negative end case.** On the literal window the bottom (all spending at the
shown −14.2%) is −$8.94 a share after net debt; neither Q7 nor Part VII says how a negative end enters the fair-price
average. It did not arise in the central range. (5) **Q2 is binary where the evidence is a slope.** The castle stands and
protects excellent returns, but it lost ground on every comparative line against all three rivals; Q2 offers OUT for a
castle "shown open", TOO HARD for one whose future cannot be judged, and IN otherwise, with nothing for a standing castle that
is narrowing on the evidence, except to carry it to Q7 as growth, which is what I did. (6) **The brief's rival rule** worked
as written: the 10-K names no rival company, which I confirmed by search and recorded. (7) **The equity-only figure can exceed
the all-equity range** whenever debt costs less after tax than the long Treasury, which makes the equity-only fair price
($30.25) five times the central one ($5.96); the text says it "never decides alone", but an operator reading the two
reporting figures side by side may need the reason stated, as it is here at Q7.
