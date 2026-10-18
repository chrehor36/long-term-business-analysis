# Company Run — Ryder System, Inc. (NYSE: R) — 2026-10-16
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for R or Ryder).

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure (the
lines of evidence and the competitor slot are derived by the analyst from the 10-K's Items 1, 1A and 7, named below).
Working folder `Test Runs/_research 2026-10-16 R/` (raw filings under its ignored `cache/`; the arithmetic scripts
`ownercash.py`, `returns.py` and their outputs are tracked).

**Contamination declared.** A directory listing of `Test Runs/`, made only to check that this run file did not yet exist,
showed one other research-folder name dated today for a different ticker; nothing in it was opened and it is not used.
The session's memory index carries one-line summaries of the project's queue state that name no company relevant here.
The repository's recent commit subjects shown at session start concern a different company (aircraft leasing); they
were seen, not opened, and are not used in any judgment below. No other run, research pass, holding review,
`PORTFOLIO.md`, `Screens/RESUME STATE*`, the register or the reading list was opened, listed or searched.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $240.38 (2026-10-16, as printed by `tools/run.py` from its aggregator, a live quote during the session;
  **aggregator flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $0.50 par, **38,346,868** outstanding at
  2026-06-30 (10-Q for Q2 2026, filed 2026-07-23, accession `0001628280-26-049417`; `python Screens/cover_shares.py R`).
  Cross-checked against the 10-Q balance sheet (outstanding June 30, 2026: 38,346,868; December 31, 2025: 39,417,224).
  Shares are retired on repurchase (10-Q Note 10), so there is no treasury count to subtract. No 8-K or prospectus after
  the 10-Q changes the count (8-K list read through 2026-07-23: item 2.02 results only).
- **Market cap:** 240.38 x 38.346868M = **$9,217.8M**.
- **Net debt (Q7 basis), 2026-06-30:** total debt $7,457M (10-Q Note 9, which includes finance lease obligations and
  other, $117M) less cash $219M = **$7,238M**. Operating leases left out (operating lease right-of-use assets $966M).
  No subsequent event stated in the 10-Q changes it.
- **Sovereign for the earnings currency (USD):** **5.43%**, US Treasury daily par yield curve, 30-year, 2026-10-15
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025, filed 2026-02-11, accession `0000085961-26-000007` (Items 1, 1A, 2,
  3, 5, 7, 8 notes 3, 13, 15, 21); 10-Q Q2 2026, filed 2026-07-23, `0001628280-26-049417`; DEF 14A filed 2026-03-11,
  `0001628280-26-016651`; 10-K FY2022 `0000085961-23-000031`, 10-K FY2023 `0000085961-24-000030`, 10-K FY2019
  `0000085961-20-000089`, 10-K FY2016 `0000085961-17-000013` (cash-flow statements, segment notes, the securities
  litigation note); the 8-K list from 2025-02 to 2026-07 (8-K of 2025-12-11 `0001628280-25-056650` on the CEO
  succession).
- **One figure cross-checked against the filed statement:** net cash from operating activities, continuing operations,
  FY2025: $2,594M in the XBRL series `tools/run.py` prints and $2,594M on the filed consolidated statement of cash flows
  (10-K FY2025, page 61). Agrees.
- `python tools/run.py R` arithmetic lines: OCF 2,353 / 2,265 / 2,594 (2023-2025), SBC 44 / 42 / 39, capital spending
  3,234 / 2,683 / 2,135, D&A 2,085 / 2,228 / 2,240. **Its owner-earnings columns are not used:** they deduct gross
  purchases of revenue earning equipment and ignore the proceeds of the used vehicles the same fleet sells
  ($468M in 2025, $532M in 2024, $764M in 2023, filed cash-flow statement, investing section), which for a leasing fleet
  is the return of the residual. Owner cash is recast below and at Q4.
- **Owner cash after every real cost, recast from the filed cash-flow statements** (`ownercash.py`, sources in its
  header): operating cash flow (continuing) less share-based compensation, plus sales of revenue earning equipment and
  operating property, less purchases of property and revenue earning equipment. Acquisitions shown separately. The
  depreciation basis beside it: operating cash less SBC less depreciation, plus the gain on used vehicle sales (the
  part of the residual realised above book).

| year | owner cash, all spending ($M) | acquisitions | after acquisitions | depreciation basis |
|---|---|---|---|---|
| 2014 | -336 | 10 | -346 | 495 |
| 2015 | -749 | 0 | -749 | 469 |
| 2016 | 175 | 0 | 175 | 473 |
| 2017 | 178 | 7 | 170 | 334 |
| 2018 | -961 | 167 | -1,129 | 282 |
| 2019 | -1,102 | 0 | -1,102 | 177 |
| 2020 | 1,557 | 0 | 1,557 | 124 |
| 2021 | 1,009 | 325 | 684 | 599 |
| 2022 | 868 | 458 | 410 | 1,001 |
| 2023 | -98 | 250 | -348 | 793 |
| 2024 | 91 | 314 | -223 | 601 |
| 2025 | 906 | 1 | 905 | 874 |

  Five-year averages 2021-2025: all spending **$555M**, after acquisitions $286M, depreciation basis $774M. Twelve
  years 2014-2025: all spending **$128M**, after acquisitions **$0M**. Ten years 2016-2025: all spending $262M, after
  acquisitions $110M.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own Ryder "if the market closed for five years"
**[M1997-109]**, which turns the question onto the trucks, the leases and the used-vehicle market rather than the
quote. The market "just tells us prices" **[M2006-077]**; the stock's moves since 2020 carry no instruction here. No
macro view enters: the freight cycle is read as a property of the business (how its earnings move through the cycle in
its own filings), never as a forecast, since "macro conclusions are — just never enter into the discussion"
**[M2000-094]**. Margin of safety: if the case needs "pencil and paper, it’s too close to think about"
**[M1996-084]**. The analyst's habit is to look for "what’s wrong in things" **[M2025-013]** and use the reading "to
possibly reject your original hypothesis" **[M1998-144]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) over twelve years (2014-2025) the business produced about zero owner cash after its own fleet
spending and acquisitions, while it paid dividends and bought back stock and its debt rose from $4.7B to $7.6B;
(2) management's own residual-value estimates for the fleet were wrong for years and were cut in 2019-2020, and a
securities class action over them (class period 2015-2020) survived a motion to dismiss and was settled in 2023
(10-K FY2022 note 22; 10-K FY2023 note); (3) the 10-K says competitors include some "which have greater capital
resources or lower cost structures than we do" and that "cost of capital is a significant competitive factor"
(10-K FY2025, Item 1A).

## THE STANDING RULE
A part-interest bought for cash with no borrowing, sized so that its loss cannot touch what the buyer has and needs,
does not put the buyer at risk of ruin: "We are never going to risk what we have and need for what we don’t have and
don’t need" **[M2012-081]**, and "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target
itself carries debt at 2.5 to 2.6 times equity; that is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The lines of evidence this name needs**, derived from the 10-K FY2025 Item 1 (three segments, FMS 38%, SCS 43%,
DTS 18% of revenue; ChoiceLease 60% of FMS revenue; 141,700 lease vehicles, 31,600 rental), Item 1A (cyclicality,
residual-value risk, contract assumptions, technology change, competition including lower-cost-of-capital rivals,
customer concentration in SCS and DTS, self-insurance) and Item 7 (segment EBT, used-vehicle results, capital
spending, free cash flow, debt and ratings): (a) the lease spread and fleet size in FMS; (b) the used-vehicle residual
and its cycle; (c) commercial rental utilisation and the freight cycle; (d) SCS and DTS contract margins and customer
concentration; (e) the fleet capital required and what it returns; (f) the cost of funds against rivals; (g) the
technology risk to diesel trucks and drivers.

- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**. The key
  variables must be identified and their predictability weighed first **[M1998-044]**, and the question is whether
  "the financial statements will tell me the information that’s useful to me" about the future statements
  **[M2008-033]**.
- **Applied.** The economics are plain and have been visible in the filings for decades: Ryder buys trucks, tractors
  and trailers to customer specification, leases them for three to seven years (trailers ten) with maintenance,
  rents a smaller fleet short-term, and sells the used units at the end; SCS and DTS run warehouses and dedicated
  fleets under multi-year contracts (Item 1). What the business earns is a spread over its depreciation, maintenance
  and cost of funds; twelve years of statements show what that spread has been, from a loss in 2019-2020 to a peak in
  2022, and the cash the fleet consumes (Step 0). That is what one needs to be "able to asses where the business will
  be in 10 years" **[M2000-037]**: a capital-heavy service earning roughly its cost of capital, as the record shows.
  As with the petroleum additives, the product needs no expertise; what matters is "the economic dynamics of the
  industry", "Is there ease of entry?" **[M2011-014]**, and those are readable from Ryder's and its rival's filings.
- **The unpredictable variables, and why they do not close the file here.** Used-vehicle prices fall and rise by
  double digits a year (tractor proceeds per unit -21% in 2024 and -11% in 2025, MD&A), and management itself got the
  residuals wrong for years (contrary evidence above). But a dependence on a price the analyst cannot forecast is
  "never by itself a STOP at Q1 or Q2" under the framework's commodity-business paragraph, whose rows say "We don’t
  think we can predict commodity prices" **[M2016-025]** and still decide "off the figures" **[M2008-069]**; reading
  the used-truck price the same way is the analyst's reading by analogy, not the paragraph's text. The price enters at
  Q7 as the cycle base. Technology (zero-emission trucks, driver-assist and autonomy, warehouse automation) is named
  in Item 1A, but the vehicles still change slowly over the life of a lease, and Ryder's three-to-seven-year terms
  re-price the risk at each renewal; nothing in the filings shows the "fast-moving technology" of **[L1993-023]** or a
  technological component of the kind that "won’t make it through the filter" **[M1998-008]**.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The
  doubt here is about how good the business is, not whether its economics can be read; the economics read plainly
  as ordinary, and that is a Q2 matter.
- Routing: not a bank; not a holding company; operating segments read by parts at Q2.
- **VERDICT: IN.** The key variables are identified and their range is on the filed record over a full cycle; the
  unforecastable one (the used-vehicle price) is a price, carried to Q7 **[M2016-025]**, **[M2008-069]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**; the moat is what "protects excellent returns on invested capital"
**[L2007-004]**.

**The parts table** (segment EBT, 10-K FY2022 `0000085961-23-000031` note 3 for 2021-2022 and 10-K FY2025
`0000085961-26-000007` note 3 for 2023-2025; segment EBT is after allocated interest; $M):

| part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| FMS (lease, rental, maintenance) | 663 | 1,054 | 665 | 516 | 501 | 3,399 | 66% | see below | **yes** (more than half) |
| SCS (contract logistics) | 117 | 186 | 231 | 332 | 355 | 1,221 | 24% | not judged further | no |
| DTS (dedicated fleets) | 49 | 102 | 121 | 125 | 140 | 537 | 10% | not judged further | no |

The parts have different economics, so they are read apart, since "lumping them together [...] impedes analysis"
**[L2008-005]**; FMS carries more than half of five-year segment profit and decides (the business-of-parts paragraph).
SCS and DTS are themselves partly FMS: their EBT includes an "Equipment Contribution" of $131M in 2025 from FMS
vehicles (MD&A), eliminated on consolidation.

**The castle tests, applied to FMS, each with its filing fact.**
- **What keeps it standing.** FMS is a national network: 789 operating locations, 401 fuel sites, 61 used-vehicle
  retail centres, 141,700 lease and 31,600 rental vehicles at 2025-12-31 (Item 1). A bank lessor can fund a truck but
  cannot maintain it; the maintenance network is the reason a customer leases from Ryder and not from a bank.
- **The money test.** Could a well-funded attacker take it? The attacker is already inside: Penske Truck Leasing
  (PTS), owned 41.1% by Penske Corporation, 28.9% by Penske Automotive Group and 30.0% by Mitsui, manages over 396,600
  trucks, tractors and trailers, of which over 262,900 are owned and leased or rented (PAG 10-K FY2025
  `0001628280-26-012830`, Item 1), against Ryder's 175,400 lease, rental and service units. The 10-K names the rest of
  the field as categories: "finance lessors, truck and trailer manufacturers and independent dealers" and "managed
  maintenance providers" (Item 1, FMS competition). By Ryder's own count about 1 million US commercial vehicles are
  leased or rented from third parties against 5 million privately owned (Item 1, Market Trends), so the customer's
  first alternative is to own the truck. The test's failing answer: "If the answer had been yes, we wouldn’t have
  done it" **[M2011-015]**; and "one competitor is frequently enough to ruin a business" **[M2012-108]**.
- **Pricing power, and how the price is set.** Ryder prices the lease "using the projected cash outflows related to
  the underlying leased vehicle, net of the estimated disposal proceeds, and a certain targeted return considering the
  weighted average cost of capital" (10-K FY2025, Critical Accounting Estimates, Revenue Recognition). That is cost
  plus a cost-of-capital return, set against rivals: the 10-K lists that "competitors may periodically reduce their
  prices to gain business", that "many customers periodically accept bids from multiple carriers", and that some
  rivals have "greater capital resources or lower cost structures than we do" (Item 1A). When the residuals behind the
  old leases proved too high, the remedy was "lease pricing initiatives" so that the portfolio "is renewed at higher
  returns" (10-K FY2022, MD&A): the price had to be repaired, and the fleet shrank while it was (ChoiceLease units
  145,300 to 141,700 and rental 35,500 to 31,600 in 2025). This is the business where "you have to have a prayer
  session before you raise your prices a penny" **[M2005-020]**, not the one that raises prices at will.
- **Would the customer still choose it over the low bid?** The customer chooses on "service quality, price, technology
  and service offerings" (Item 1) and rebids; the rows' failing answer is the customer "buying candy for the low bid"
  **[M2017-009]** turned the other way.
- **The low-cost position.** No filing read shows Ryder as the low-cost operator; its own risk factor says the
  opposite of some rivals (above), and the larger rival earns more on its assets (field returns, below). "commodity
  businesses have risk unless you’re the low-cost producer" **[M1997-010]**.
- **Cost of funds as the edge.** Money leasing is the business the rows decline when "we’ve got other people with a
  lower cost of funds", and the same row names the practice of "using short-term money to finance longer-term assets
  which have big residual risks" **[M2016-029]**. Ryder's own Item 1A: "because cost of capital is a significant
  competitive factor", a rating cut "could have a significant impact on our competitive position". Ryder is rated
  BBB+/Baa2 (MD&A); a lessor's spread over funding is the product, and no funding advantage is shown in any filing read.
- **Widening or narrowing.** Narrowing on the last five years' evidence in FMS: the lease and rental fleets fell in
  2025, rental utilisation fell from 75% (2023) to 70%, and FMS EBT fell from $665M (2023) to $501M (2025); Ryder
  exited its UK FMS business (a $188M currency translation loss in 2023, MD&A). Against it, contractual lease
  earnings rose on pricing and maintenance savings (MD&A 2025). The question is "whether it’s likely to widen further
  or shrink on you" **[M1999-108]**; the evidence is mixed, and it is not the deciding test here.

**The competitor row.** FMS decides. The 10-K names no rival by name, so the rivals are a **CONVENTION of this run**:
Penske Truck Leasing, the one national full-service lessor of Ryder's kind whose figures reach the SEC, through its
28.9% holder's 10-Ks; rationale: the 10-K's competitor categories are banks, OEM dealers and private fleets, none of
which files a comparable segment. Named-category rivals that do not file comparable figures: finance lessors, OEM and
dealer lessors, independent dealers, managed maintenance providers. For the non-deciding parts, GXO Logistics (contract
logistics) and J.B. Hunt's Dedicated Contract Services segment are shown, under the same CONVENTION.

| company | metric | span | figure | source |
|---|---|---|---|---|
| Ryder | pre-tax earnings plus interest / average debt plus equity | 2014-2025 | **7.9%** aggregate; by year from 1.4% (2020) to 15.5% (2022) | 10-Ks listed in Step 0; `returns.py` |
| Ryder | net earnings (continuing) / average total assets | 2019-2025 | **2.6%** (pre-tax 3.6%) | same |
| Ryder | net earnings / average equity | 2014-2025 | 11.5% to 16.2% in ordinary years, 30.1% at the 2022 peak, -4.7% in 2020; debt about 2.5 times equity | same |
| Penske (PTS; PAG's equity-method investees combined, PTS the bulk) | net income / average total assets | 2019-2025 | **4.8%** aggregate; 2.9% in 2024 and 2025, 9.3% in 2022 | PAG 10-Ks FY2019 `0001558370-20-001163`, FY2020 `0001558370-21-001299`, FY2022 `0001019849-23-000038`, FY2023 `0001019849-24-000033`, FY2025 `0001628280-26-012830` |
| Penske (same) | net income / average equity | 2019-2025 | 13.2% to 40.0%; equity about a fifth to a quarter of assets | same |
| GXO Logistics | operating income / average total assets | 2021-2025 | **2.5%** aggregate (2.1% to 3.4%) | GXO 10-K FY2025 `0001852244-26-000007` (XBRL series) |
| J.B. Hunt DCS | segment operating income / segment assets | 2024-2025 | 16.5% (2024), 17.7% (2025) | J.B. Hunt 10-K FY2025 `0001437749-26-005294`, segment note and MD&A |

Penske's net income is a partnership's and is shown only as filed (PAG reports no pre-tax line for it), so the
comparison on assets is approximate; it runs against Ryder either way (Penske 4.8% after whatever entity tax it pays,
Ryder 3.6% before tax). J.B. Hunt's DCS owns its tractors while Ryder's DTS rents them from FMS, so the two dedicated
figures are not comparable on assets; DTS does not decide. GXO, the SCS comparator, earns about 2.5% on its assets.

**The field's returns over the last full cycle, judged in words.** The cycle runs from the used-vehicle and freight
peak of 2014-2015, through the residual-value losses of 2019-2020, the peak of 2021-2022 and the downturn of 2023-2025
(MD&A of each 10-K). Over it Ryder earned about 7.9% before tax on all the capital in the business, roughly 6% after a
quarter of it goes in tax, and its larger rival earned under 5% on its assets after its own taxes. Returns on equity in
the teens exist by borrowing about two and a half dollars for each dollar of equity. These are ordinary returns: a
lessor's spread over its cost of funds, priced by the company itself as a "targeted return considering the weighted
average cost of capital", in a field of two national lessors, banks, dealers and the customer's own garage. "you can
have only two competitors and they’re still terrible businesses" **[M2013-052]** is too strong for this field, which
is not terrible; but the castle protects no "excellent returns on invested capital" **[L2007-004]**. Under the
framework's Q2 list, the standing castle that protects only ordinary returns, shown from the filer's and the rival's
filings over a full cycle, is OUT, not TOO HARD: the returns are known, so the reason the tenuous moat goes to TOO
HARD, "We don’t know how to valuate that" **[M2000-019]**, does not apply. No regulator sets these returns, so the
second-best exception does not apply.

**What is said for the business, written down against the verdict** **[M1997-127]**: the maintenance network is a real
barrier to a bank or a new entrant; contractual lease earnings rose in 2024-2025 on pricing; SCS reported record sales
in 2025 and is growing; returns on capital in 2023-2025 (9.4% to 10.1% before tax) were higher than in 2014-2020 at
the bottom of a freight cycle, which management credits to its "transformed business model" (MD&A). The framework
credits a change for the better only on a full cycle in which the price behaviour held (Q2, Change); the recent
improvement has not been through one, and even at 10% before tax on capital the return is not excellent.

- **VERDICT: OUT.** FMS, the deciding part, is a standing castle that protects only ordinary returns: about 8% before
  tax on capital over 2014-2025 for Ryder and under 5% on assets for its larger rival, prices set at cost plus a
  cost-of-capital return against rivals with equal or lower funding costs **[L2007-004]**, **[M2016-029]**,
  **[M2005-020]**, **[M1997-010]**. Box OUT **[M2011-015]**, **[M2006-013]**.

## STEP 0 (continued): THE BALANCE SHEETS, READ BECAUSE THE FILE CLOSED BEFORE Q4
Read as the template asks when the file closes before Q4, "balance sheets over an 8 or 10 year period before I even
look at the income account" **[M2025-032]**. Figures are the first-filed XBRL vintage printed by `tools/run.py`
(accessions 0000085961-17-000013 to 0000085961-26-000007, one per year), checked against the filed statements for
2016, 2019, 2022 and 2025; equity for 2017-2018 was later restated down by the 2019 adoption of the lease standard
(latest-filed equity 2017 $2,454M, 2018 $2,537M), and the later column is used in `returns.py`. $M.

| year-end | total assets | equity | goodwill + intangibles | total debt | cash | receivables | retained earnings |
|---|---|---|---|---|---|---|---|
| 2016 | 10,902 | 2,052 | 435 | 5,391 | 59 | 832 | 1,827 |
| 2017 | 11,452 | 2,835 | 439 | 5,410 | 78 | 1,011 | 2,465 |
| 2018 | 13,051 | 2,910 | 534 | 6,624 | 68 | 1,219 | 2,711 |
| 2019 | 14,475 | 2,476 | 526 | 7,925 | 74 | 1,228 | 2,178 |
| 2020 | 12,932 | 2,256 | 518 | 6,610 | 151 | 1,182 | 1,913 |
| 2021 | 13,834 | 2,798 | 741 | 6,580 | 234 | 1,465 | 2,266 |
| 2022 | 14,395 | 2,937 | 1,156 | 6,352 | 267 | 1,610 | 2,518 |
| 2023 | 15,778 | 3,069 | 1,336 | 7,114 | 204 | 1,714 | 2,554 |
| 2024 | 16,672 | 3,117 | 1,615 | 7,779 | 154 | 1,861 | 2,644 |
| 2025 | 16,387 | 3,052 | 1,564 | 7,645 | 198 | 1,897 | 2,569 |
| 2026-06-30 | 16,089 | 2,879 | 1,539 | 7,457 | 219 | 1,997 | 2,434 |

What the figures say. (1) **Equity barely grew while the business earned.** Net earnings 2016-2025 summed to about
$3.9B (XBRL NetIncomeLoss by year), yet equity rose only from $2.05B to $3.05B: dividends took about $1.2B and
buybacks about $2.0B (cash-flow statements), and the residual-value charges of 2019-2020 took two years of earnings
(net loss $24M in 2019 and $122M in 2020). Retained earnings stood at $2.43B in mid-2026, below their 2018 level.
(2) **Debt rose by $2.3B** (2016 to 2025) and carried the buybacks: owner cash after acquisitions summed to about
$1.1B over the ten years (Step 0 table) against $3.2B paid to owners. Debt stayed at 2.3 to 3.2 times equity
throughout; the 10-Q puts it at 259% of equity at 2026-06-30. (3) **Goodwill and intangibles more than tripled**
(from $435M to $1,564M) on the acquisitions of 2018-2024 (Cardinal Logistics among them, 10-K FY2025 MD&A), so the
growth of SCS and DTS was partly bought; they now exceed half of equity. (4) **Receivables grew faster than sales**,
from 12.3% of revenue (2016: $832M on $6,758M) to 15.0% (2025: $1,897M on $12,665M), as the mix moved to SCS and
DTS. (5) **Cash is kept low** ($59M to $267M); liquidity is the $1.6B revolver and the $300M receivables facility,
with $723M of commercial paper outstanding at mid-2026 (10-Q Note 9). (6) **The deferred tax liability**, $1.8B at
2025 (`DeferredIncomeTaxLiabilitiesNet`), is the accumulated benefit of accelerated tax depreciation on the fleet;
cash taxes paid were $52M in 2025 against a $184M provision (MD&A; XBRL `IncomeTaxesPaidNet`). (7) **A pension
deficit** sits in equity: an accumulated net pension equity charge of $575M after tax at 2025 (MD&A, plans 94%
funded). What the figures cannot say: what the fleet would fetch in a forced sale; the 10-K's sensitivity says a 10%
cut in residual estimates would add about $340M of depreciation over the fleet's life (MD&A, Critical Accounting
Estimates).

---
## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out? WEIGHING.
NOT REACHED (the file closed OUT at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read above, as the template asks; facts under AFTER THE STOP.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED. Integrity facts found are recorded, not judged, under AFTER THE STOP.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback facts that Q6's test would read against Q7's bottom are recorded under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The owner's reporting figures are computed below under the protocol's heading.

### COMPUTATION, NOT A CLEARANCE
*(Operator rule 3 and the brief's reporting convention. Q7's range convention applied in full; no entry language.)*

**Inputs.** Owner cash as recast in Step 0 (`ownercash.py`). All-equity basis: owner cash plus interest expense after
tax, the tax at 25% (**CONVENTION of this run**: the comparable tax rate was 26.0% in 2025, 25.7% in 2024 and 26.1% in
2023, MD&A; rationale: a round figure near the filer's own). Company's own tax as paid in operating cash, no
conversion; no carryforward or credit that runs out inside ten years was found (the low cash tax is deferral, carried
as the deferred tax liability, not a credit). Rate 5.43% (Treasury 30-year, 2026-10-15). Net debt $7,238M (Step 0).
Shares 38,346,868. Price $240.38 (aggregator). Market value $9,217.8M; market value plus net debt $16,455.8M.

**How each specific was applied.**
- **The maintenance guess, (e).** The filing allows it: the fleet count did not grow over the decade (185,200 vehicles
  at 2015 year-end, 10-K FY2016; 184,900 at 2025 year-end, 10-K FY2025; 213,800 at the 2019 peak, 10-K FY2019),
  so the spending above depreciation was the cost of standing still in a fleet whose unit prices rose, not growth.
  The central case therefore charges all fleet spending, net of the used-vehicle proceeds, as maintenance; the
  depreciation basis is shown beside it as the variant that would hold only if depreciation were the full cost of
  replacement, which the decade's record does not show.
- **Cycles, (a).** The literal window's first year (2021) is aberrational by the filer's own words ("Pricing in the
  used vehicle market significantly declined in 2019 and 2020 and then significantly increased in 2021", 10-K FY2022),
  2022 held "elevated performance levels" (same), and the last year (2025) sits in "weak market conditions" for used
  vehicles and rental (10-K FY2025). The cycle base is therefore the last full cycle, trough to trough, from the
  weak used-vehicle market the filer describes for "the latter part of 2015 and continuing through 2016" (10-K FY2016)
  to that of 2025: the ten years 2016-2025. The literal window is shown beside.
- **Growth and decline, (b), and the cap, (f).** On the cycle base, growth is measured between the halves of the
  decade (the series changes sign year to year): all-equity owner cash after acquisitions averaged $80M in 2016-2020
  and $515M in 2021-2025, about 45% a year, which carried ten years would require owner cash far above any share of
  sales the business has earned (its best all-equity year, 2020, was about 21% of revenue only because purchases were
  cut to $1.1B). It is cut to the business's own sales growth between the same halves (average revenue $7,960M to
  $11,752M, about 8.1% a year, part of it bought and part of it pass-through fuel and subcontracted freight), and
  that is cut again to the discount rate, **5.43%**, which the convention says it may never exceed. On the literal
  window the series changes sign, so growth is measured between its first two and last two years ($713M to $637M,
  about -3.7% a year) and carried as the bottom, with no growth the top.
- **Acquisitions, (c).** Deducted, with the total growth credited (the default pair). Net purchases over the window,
  $1,348M, are less than half of owner cash before purchases on either basis ($2,776M owner cash; $3,922M all-equity),
  so the serial-acquirer rule does not apply. Ryder does not report organic growth in the filings read, so the organic
  pair is not shown. No signed, unclosed deal is stated in the 10-Q.
- **Working capital, (d).** Counted: the changes in operating assets and liabilities are inside operating cash.
- **The floor is tested first.**

**The value range (central case: all-equity, all spending, acquisitions deducted, cycle base 2016-2025 of $297M a year,
growth 5.43% for ten years then none, at 5.43%).**

| case | base $M/yr | growth | business value at 5.43% ($M) | per share after net debt | expected return at the price |
|---|---|---|---|---|---|
| central, no growth (bottom) | 297 | 0 | 5,471 | **-$46.07** | 1.8% |
| central, shown growth capped (top) | 297 | 5.43% | 8,442 | **$31.41** | 2.9% |
| literal window 2021-2025, decline (bottom) | 515 | -3.7% | 7,070 | -$4.38 | 2.2% |
| literal window, no growth (top) | 515 | 0 | 9,484 | $58.58 | 3.1% |
| beside: depreciation as maintenance, cycle base, no growth | 561 | 0 | 10,331 | $80.67 | 3.4% |
| beside: depreciation as maintenance, cycle base, growth | 561 | 5.43% | 15,941 | $226.97 | 5.3% |
| beside: depreciation as maintenance, literal window, growth | 733 | 5.43% | 20,829 | $354.42 | 6.7% |

**Value range (central): -$46.07 to $31.41 a share, against $240.38.** The whole business is worth $5.5B to $8.4B
at the long rate on the central case, less than the $7.2B the lenders are owed at its bottom. The floor is tested
first: **no case in the table, central or beside, earns the floor of about ten percent at the price**; the best, the
depreciation basis on the literal window with growth credited at the discount rate, expects about 6.7%. On the
framework's terms the file would close OUT at Q7 had it reached Q7, before any width test **[M2003-149]**.

**Fair price** (the price at which the midpoint of the range earns the floor: each end case valued at ten percent, the
two averaged; company's own tax; Part VII): **all-equity basis (central): -$93.77 a share** (ends -$111.27 and
-$76.26); **equity-only beside: $35.17 a share** (owner cash after interest and acquisitions, cycle base $110M a year,
ends at ten percent $28.69 and $41.65). The all-equity figure is negative because, at ten percent, the central cash
stream is worth less than the net debt; the equity-only figure, which lets the lenders' cheaper money flatter the
per-share result, is shown beside and does not decide. On the depreciation basis beside, the all-equity fair price
would be -$9.40 (cycle base) or $45.59 (literal window). Neither figure is a verdict or entry language.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (No business the rows name for Q12 is involved: truck leasing, maintenance, logistics.)

---
## THE BOX
**OUT at Q2.** FMS, the deciding part (66% of five-year segment profit), is a standing castle that protects only
ordinary returns: about 7.9% before tax on all capital over the 2014-2025 cycle, a larger rival (Penske) earning under
5% on its assets, lease prices set by the company as cost plus a return "considering the weighted average cost of
capital" against rivals with equal or lower funding costs; equity returns in the teens come from debt of about 2.5
times equity. **Integrity facts recorded, not judged** (the residual-value securities class action and its settlement;
see below). COMPUTATION, NOT A CLEARANCE: value range -$46.07 to $31.41 a share (all-equity central) against $240.38;
no case earns the floor at the price; fair price -$93.77 all-equity, $35.17 equity-only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found **[M1997-127]**; no verdict; the box unchanged (operator rule 2).

**Q3 (capital).** Pre-tax earnings plus interest on average debt plus equity: 7.9% aggregate 2014-2025, 9.4% to 10.1%
in 2023-2025 (`returns.py`). Fleet units flat over the decade (185,200 in 2015, 184,900 in 2025) while net fleet
spending ran above depreciation: ten-year owner cash $262M a year on all spending against $526M on the depreciation
basis (Step 0). The 10-K expects gross capital spending of about $2.4B in 2026, up from $2.1B, "reflecting higher
investments in the lease fleet" (MD&A, 10-K FY2025).

**Q4 (the accounts).** (a) Depreciation rests on management's residual-value estimates; the 10-K says "In the past, we
have realized losses on sales of used vehicles at the end of a vehicle's useful life when our residual value estimates
were above used vehicle market prices" (Item 1A, 10-K FY2022), and 2019-2020 carried those losses and higher
depreciation (depreciation $1,879M in 2019 and $2,027M in 2020 against $1,389M in 2018). Residual estimates are now
"at historically low levels" (10-K FY2025, MD&A); a further cut "for certain tractors" is expected from 2026-01-01.
(b) The highlights of the 10-K and the proxy feature non-GAAP figures: comparable EPS, comparable EBT, comparable
EBITDA, adjusted ROE, operating revenue and free cash flow (10-K FY2025 MD&A, "2025 HIGHLIGHTS"; DEF 14A). Comparable
earnings exclude non-operating pension costs every year ($36M to $41M, 2023-2025). (c) The 10-K states forecasts for
2026: operating cash "approximately $2.7 billion", free cash flow "approximately $800 million", gross capital spending
"approximately $2.4 billion" (MD&A). The quarterly earnings releases (8-K exhibits) were not read. (d) `tools/run.py`'s
owner-earnings columns omit the used-vehicle proceeds for this name (Step 0).

**Q5 (the people): integrity facts, recorded, not judged.** (a) **Securities litigation over the residual values:** a
putative class action filed 2020-05-20 for purchasers between 2015-07-23 and 2020-02-13 alleged that Ryder and current
and former officers "misrepresented Ryder's depreciation policy and residual value estimates"; the motion to dismiss was
denied on 2022-05-12; the parties reached an agreement in principle to settle on 2023-04-18, with the settlement
expected to be covered by insurance (10-K FY2022 note 22, `0000085961-23-000031`; 10-K FY2023 note,
`0000085961-24-000030`). Five shareholder derivative complaints on the same allegations were filed 2020-2021 and were
stayed (same notes). The 10-K FY2025 contingencies note no longer mentions either; the FY2024 10-K, which would show
the final approval and the derivative cases' end, was not read. (b) Robert E. Sanchez was CEO from 2013 and Chair from
2013; he retired as CEO on 2026-03-31 and became Executive Chair; John J. Diez, with Ryder since at least 2011 in
asset management, DTS, FMS and as CFO, became CEO (10-K FY2025 Item 1; 8-K 2025-12-11). "Ryder has historically
combined the positions of Board Chair and CEO" (DEF 14A). (c) Mr. Sanchez's beneficial holding includes 441,532 shares
(DEF 14A, beneficial ownership note); total 2025 compensation $10,178,386, of which stock awards $7,159,495 (DEF 14A,
Summary Compensation Table). (d) The forecasts of (Q4 c) are public statements of the kind Q5 reads with the record.

**Q6 (the money and the owners).** (a) Buybacks: $519M in 2025 (Q4 2025 at an average $168.90 a share, Item 5), $332M
in the first half of 2026 (10-Q cash-flow statement); two programmes, an anti-dilutive one of up to 1.5 million shares
and a discretionary one of up to 2 million shares over two years (10-Q Note 10); no price limit is stated in either.
The prices paid sit far above the bottom of the COMPUTATION's central range (-$46.07), the test Q6 would apply, had
Q6 been reached. (b) Dividends $145M in 2025; the annual rate raised 12% to $3.64 (10-K FY2025). (c) Pay: the annual
incentive weights comparable EBITDA at 60%, operating revenue at 20% and strategic objectives at 20%; the long-term
plan is 60% performance-based restricted stock earned on three-year average adjusted ROE and strategic revenue growth
with a relative-TSR modifier, 40% time-vested; the 2023-2025 performance award paid at 168% (DEF 14A, CD&A).
(d) Acquisitions 2018-2025 about $1.5B (cash-flow statements); goodwill and intangibles from $435M to $1,564M.

**Q9 (debt and exposures).** Total debt $7,457M at 2026-06-30, 259% of equity; $700M of medium-term notes mature in
2026 (the November 2019 and November 2021 notes) and $1,375M of notes and unsecured obligations in 2027; commercial paper $723M backed by a $1.6B
revolver to April 2030; asset-backed obligations $57M (10-Q Note 9). Ratings BBB+ (S&P, Fitch), Baa2 (Moody's,
outlook positive) at 2025-12-31 (MD&A). Self-insured for vehicle liability and workers' compensation; a 5% adverse
change in claim estimates would add $25M (MD&A). Pension plans 94% funded. Residual exposure: a 10% cut in residual
estimates adds about $340M of depreciation over the fleet's remaining life (MD&A). Top ten customers in each of SCS and
DTS are about one-third of each segment's revenue (Item 1A).

**Q12.** Nothing found.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `c48e1fb9`); written question by question; committed after
      Q1 (`ad43374b`), after Q2 (`c8ec1982`), after the balance sheets and the computation (`d46c762d`), and at the close.
- [x] Dispatched to an analyst: the brief allowed per-question pathspec commits; the lock is the dispatching session's,
      not checked here; the fold into the register is the dispatcher's (operator rule ten). A run not in the register
      binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, except the one directory
      listing of `Test Runs/` declared under contamination (a different ticker's research folder name seen; not opened).
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (`check_ids.py`); every quoted fragment beside an id is in
      that row; no E-id; every filing fact carries its document or accession; numbers carry a filing or a CONVENTION.
- [x] The order was kept; Q2 was the first STOP to fail and closed the file; everything after it is NOT REACHED or
      headed COMPUTATION, NOT A CLEARANCE, with no entry language.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      SBC deducted; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations; Q2's "what is said for the business"); facts for later
      questions under AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor applies.
- [x] Only the arithmetic lines of `tools/run.py` were used, and its owner-earnings columns were rejected for this name
      with the reason stated.
- [x] `python tools/check_framework.py` PASS before the closing commit.
- Weaknesses confessed: the price is an intraday aggregator quote; Penske's figures are PAG's combined equity-method
  investees (PTS the bulk, with small others), after its own partnership-level taxes, against Ryder's pre-tax and
  after-tax figures; the 10-K FY2024 and the earnings-release exhibits were not read; segment assets for FMS are not
  reported for 2023-2025, so FMS's own return on assets could not be computed for those years and the field return is
  measured on the whole company.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A leasing fleet's residual is not addressed anywhere.** The framework's Q4 costs list depreciation, and Q7's (e)
asks for the maintenance guess, but nothing says that for a lessor the cash recovered on selling the used fleet is part
of the capital-spending line; `tools/run.py`'s owner earnings deduct gross fleet purchases and ignore $0.5B to $1.2B a
year of proceeds, which would have made every year's owner cash negative. I recast it from the statements. (2) **Q1's
commodity paragraph covers commodity prices only**; the used-truck price, which management itself could not forecast,
is the same kind of variable, and I applied the paragraph by analogy, saying so. A line naming residual-value prices
would settle it. (3) **Q7 (a) on a decade with two troughs**: "the last full cycle, peak to peak or trough to trough"
with growth "between the averages of successive cycles" needs a previous cycle; I took 2016-2025 trough to trough and
measured growth between its halves, borrowing (b)'s fallback, which the text gives only for a sign change. (4) **Q7
(f) then hands the discount rate back as the growth rate**: a shown rate cut to sales growth (8.1%, partly bought and
partly pass-through fuel and freight) and then to the discount rate makes the ten-year sum exactly ten times the base;
the text does not say whether total or operating revenue is the sales figure. (5) **A negative fair price** (the
all-equity central case is worth less than the net debt) is not contemplated by Part VII's reporting convention; I
report it as computed, with the equity-only figure beside. (6) **The all-equity add-back of interest** needs a tax rate
on the interest, which the framework does not give, for a company whose cash tax is mostly deferred; I used 25% as a
CONVENTION of the run. (7) **Q2's "ordinary returns" judged in words** depends on the competitor row, and the best
rival here reports only a partnership's net income through a minority holder, so the comparison mixes tax bases; the
framework might say which return a field comparison should use when the rivals' filings differ.
