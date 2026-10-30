# Company Run — Pentair plc (NYSE: PNR) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run under `Screens/_daily/_dispatch_brief.md`. Copied from the template before any fetch (commit
24b63333). Working folder `Test Runs/_research 2026-10-10 PNR/` (notes in `_notes.md`, scripts `fetch.py`, `comp.py`,
`ids.py`, `q7.py`, `check_quotes.py`; raw filings in the ignored `cache/`).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold (overnight cycle, 2026-10-10), after the run was committed: **not held**; `PORTFOLIO.md` carries PNR only as a row of the ranked opportunity set from the v4.1 run of 2026-09-01, in no account.*

**Contamination, declared:** before any work, the session context showed (a) the subjects of the five latest commits,
which name runs of four other companies (MA, MSA, NDSN, ORLY) and their boxes; (b) a memory index line on the state of the
queue (counts of gate-clearers, a paused wave); (c) the dispatch message's statement that earlier run files about Pentair
exist. No PNR run file, holding review, `PORTFOLIO.md` or register entry was opened, listed or searched; nothing of (a) to
(c) bears on Pentair's facts and none of it is used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $52.47 (close 2026-10-09; Yahoo chart API via `tools/sources.py`; **aggregator, live quote only, flagged**
  per operator rule 5). The same series shows a 52-week high of $112.13 and closes of about $105 to $110 from
  September 2025 to January 2026; no split in the two years (the chart's split events are empty). The price has
  roughly halved in a year. That fact is the first thing written down: why it halved is read below, not assumed.
- **Shares by class** from the latest filing's cover: 159,637,950 ordinary shares, nominal value $0.01, one class
  (Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-28, accession `0000077360-26-000045`;
  `python Screens/cover_shares.py PNR`). Check: the 10-Q balance sheet shows 159.6 million issued at 2026-06-30 and the
  company holds its repurchased shares as cancelled (issued fell from 163.2 million at 2025-12-31 to 159.6 million
  after 4.0 million were bought in the half), so issued equals outstanding. No 8-K after the 10-Q reports an issuance
  (8-Ks of 2026-09-02, 2026-09-18, 2026-09-22 read: financing and officer items only).
- **Market cap:** 159.638M × $52.47 = **$8,376M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, 30-year par yield, US Treasury daily par yield curve,
  2026-10-09 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-24, `0000077360-26-000007` (business, risk factors, MD&A, statements, notes).
  - 10-Q Q2 2026, filed 2026-07-28, `0000077360-26-000045`; 10-Q Q1 2026, filed 2026-04-28, `0000077360-26-000027`.
  - DEF 14A 2026, filed 2026-03-20, `0000077360-26-000014`.
  - 8-Ks: 2025-10-21 `0000077360-25-000045` (CFO resignation); 2026-02-03 `0000077360-26-000003` (Q4 release);
    2026-04-28 `0000077360-26-000023` (Q1 release) and `0000077360-26-000024` (Pool CEO resignation); 2026-05-06
    `0001104659-26-056228` (credit facility amendment); 2026-07-14 `0000077360-26-000039` (preliminary Q2, guidance cut,
    CFO resignation); 2026-07-28 `0000077360-26-000042` (Q2 release); 2026-09-02 `0001104659-26-104725` (Taco term loans);
    2026-09-18 `0000077360-26-000047`; 2026-09-22 `0000077360-26-000050` (new CFO).
  - 10-Ks for the span: FY2024 `0000077360-25-000006`, FY2023 `0000077360-24-000007`, FY2022 `0000077360-23-000006`,
    FY2021 `0000077360-22-000006`, FY2020 `0000077360-21-000005`, FY2019 `0000077360-20-000006`, FY2018
    `0000077360-19-000006`, FY2017 `0000077360-18-000007`, FY2015 `0000077360-16-000058`, FY2013 `0000077360-14-000010`.
  - Forms 3, 4 and 144 filed 2025-07-01 to 2026-10-10 (insider transactions, read for Q5).
- **One figure cross-checked against the filed statement:** cash from operating activities of continuing operations
  FY2025, $814.8M in the filed cash-flow statement (10-K `0000077360-26-000007`) against $814.8M in `tools/run.py`'s
  tagged line. They agree.
- `python tools/run.py PNR`, arithmetic lines only (its rule lines, ids and verdicts are not read, framework Part VII):
  OCF $619.2M / $766.7M / $814.8M (FY2023 to FY2025), SBC $29.1M / $39.7M / $37.0M, capex $76.0M / $74.4M / $68.8M,
  D&A $114.8M / $114.6M / $117.7M; "none in the window" for securities inside operating cash, other stock pay or
  unusual capital lines. The tool's three-year window is not the run's window; the run's five-year owner cash is
  built from the filed statements at Q7 (script `q7.py`). The tool's balance-sheet table is used at Q4 as a
  transcription and checked against the filed balance sheets.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the market as servant **[M2006-077]**: the quotation has gone from about
$110 to $52 in a year, and the price "doesn’t tell us anything. It just tells us prices" **[M2006-077]**; whether the fall
is the business or only the quotation is what the questions must find, asked as "Would I be happy buying this stock if
the market closed for five years?" **[M1997-109]**. No macro enters **[M2000-094]**: the filer's own excuse, "higher
interest rates and inflation", is noted as the filer's words and not weighed as a forecast. The analyst's habit that
governs this file is to look for "what’s wrong in things" **[M2025-013]** and to write the contrary evidence down at once.
**Contrary evidence, written down as found** **[M1997-127]**: (1) 2026-07-14, preliminary Q2 2026 sales of about $930M,
"down 17 percent versus previous guide of up approximately 1 percent", attributed to "Pool channel inventory"; full-year
sales guide cut from up 2% to 4% to down 4% to 7% (8-K `0000077360-26-000039`, EX-99.1). (2) The CFO resigned on
2026-07-10 after about four months in the role; his predecessor, who had resigned in October 2025, returned as interim
CFO (same 8-K; 8-K `0000077360-25-000045`). (3) The Pool segment's chief executive resigned on 2026-04-24 and the role was
eliminated (8-K `0000077360-26-000024`). (4) In Q2 2026, while Pentair's Pool volume fell 46.3% (10-Q
`0000077360-26-000045`), Hayward's North America volume rose 1.8% and its sales 8.8% (Hayward 10-Q `0001834622-26-000047`),
and Pool Corporation's equipment sales rose 3% (POOL 10-Q `0001193125-26-322532`). (5) Pentair bought back $350.0M of
its shares in H1 2026 at about $87.50 a share, then agreed on 2026-07-27 to buy Taco Group Holdings for $1.425B with
$1.4B of new term loans (10-Q note 16; 8-K `0001104659-26-104725`). (6) FY2025 year-end receivables rose 19% on sales up
2% (10-K FY2025). Each is weighed at the question it bears on.

## THE STANDING RULE
The buyer's own conduct: a purchase from cash, unlevered, sized so that a further halving of the quotation forces no
sale, puts the buyer at no risk of ruin **[M2012-081]**; borrowed money to own it would be ruled out **[L2014-005]**,
**[M2016-062]**. Nothing in this run is a financing or sizing decision. The target's own debt is Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test** **[M1995-051]**, **[M2012-065]**: "a reasonable fix on about what the earning power and competitive position
will look like in five or 10 years" **[M2012-065]**.

**What the business is** (10-K FY2025, Item 1 and MD&A, `0000077360-26-000007`). Three segments in FY2025: Pool
(residential and commercial pool equipment: pumps, filters, heaters, lights, automation, chlorinators, cleaners; sales
$1,558.8M, segment income $527.1M); Water Solutions (commercial filtration, Manitowoc ice machines, Everpure, residential
softeners and filters, RainSoft; $1,062.1M, $253.9M); Flow (pumps for residential, irrigation, commercial,
infrastructure and industrial uses, membranes, Hydra-Stop insertion valves; $1,553.6M, $362.1M). From 2026-01-01 the
residential and irrigation pumps moved from Flow to Water Solutions; Pool is unchanged. Irish plc, tax resident in the
UK, US GAAP, SEC filer; management office in Golden Valley, Minnesota.

**The portfolio reshaping, so that the history is read as the history of today's business.** Pentair, Inc. combined
with Tyco's flow-control business on 2012-09-28: Tyco spun off Flow Control, distributing about 110.9 million shares to
Tyco's holders, and the merger with Pentair, Inc. "was accounted for as a reverse acquisition" (FY2013 10-K
`0000077360-14-000010`); the filer's revenue went from $3.5B (FY2011) to $7.5B (FY2013), equity from $1.9B to $6.1B and
goodwill from $2.3B to $5.1B (XBRL first-filed facts, `comp.py`). It bought ERICO "for approximately $1.8 billion" in
2015 (FY2015 10-K `0000077360-16-000058`). It sold Valves & Controls to Emerson on 2017-04-28 "for $3.15 billion in
cash" (FY2017 10-K `0000077360-18-000007`), so the Tyco flow-control business was largely sold five years after it was
bought, and it separated the Electrical business as nVent on 2018-04-30 (FY2018 10-K `0000077360-19-000006`; total
assets $8,634M at 2017 year-end to $3,806M at 2018 year-end, equity $5,038M to $1,836M).
What is left from 2018 is the old Pentair water business: pool (Sta-Rite and Pentair pool, the core of the Pentair
Water Pool and Spa company that Pool Corporation names as its largest supplier from 2014), water treatment and pumps.
Since then: Aquion and Pelican 2019 ($287.8M acquisitions that year), Pleatco and Ken's Beverage 2021 ($338.5M), Manitowoc Ice
2022 ($1,580.9M), G & F Manufacturing 2024 ($108.0M), Hydra-Stop 2025 ($292.1M), and Taco agreed in 2026 ($1.425B,
not closed at the last filing). So the comparable history is FY2018 onward, and the merger and the spin are read as
Q7's window specifics require (Q7, below): none of them falls inside the five-year window FY2021 to FY2025; the
acquisitions inside it are deducted there.

**The key variables** **[M1998-044]**: (1) the installed base of pools and its replacement and repair demand; Pool
Corporation, the largest distributor, reports more than 5.5 million US in-ground pools and that in 2025 about 64% of its
sales were maintenance and minor repair, 22% remodel and upgrade and 14% new construction (POOL 10-K FY2025
`0001193125-26-074833`); new in-ground pools were about 61,000 in 2024, 72,000 in 2023, 98,000 in 2022 and 117,000 in
2021 (POOL 10-Ks FY2022 `0000945841-23-000015`, FY2024 `0000945841-25-000032`), so each year's new pools are one or two
percent of the base and the aftermarket carries the business; Hayward puts aftermarket at about 85% of its own sales
(Hayward 10-K FY2025 `0001834622-26-000008`); (2) Pentair's place on the distributor's shelf (Q2); (3) price against
cost. These are the economics of a slowly changing equipment aftermarket, foreseeable in direction over ten years
**[M2000-037]**. The product changes (variable-speed pumps, heat pumps, automation) are improvements to equipment that
is still bought by the same servicers through the same distributors; the forecast is about customers more than
technology **[M2017-019]**. "I never would understand the chemistry of it, but [...] What is important is that I
understand the economic dynamics of the industry" **[M2011-014]**: the dynamics here are three makers, a few
distributors and a large installed base.

**Do the past statements tell me the future ones** **[M2008-033]**? For the deciding part, over 2017 to 2025, yes in
direction: Pool margins of 27% to 34% through a boom and a bust. 2026 is the warning: the channel's inventory decisions
moved Pool's sales by $250M in one year (guidance, 10-Q `0000077360-26-000045`), so a single year's statements tell
less than the span. That is a reason to read the span, not a reason the span cannot be read.

**The parts** (framework Q1, A holding company, extended to segments): the part that decides under Q2's business of parts
is Pool (Q2's parts table). Water Solutions and Flow are pumps, filters, softeners and ice machines, inside the same
circle; the industrial membranes and gas recovery lines in Flow are a minor slice of a non-deciding part. Doubt about the
deciding part being inside the circle **[M2002-092]**: none found; the doubt this file carries is about the castle's
recent behaviour, which is Q2's question, not about whether the economics can be understood. Governance and tax abroad
**[M2000-141]**: an Irish plc reporting in US GAAP with its tax residence in the UK, effective tax rate 13% to 14% in
2024 and 2025; understood.

**VERDICT: IN.** The deciding part's economics (an installed-base equipment aftermarket served through distributors) can
be pictured ten years out in direction and in its key variables **[M2012-065]**, **[M1998-044]**; nothing in it
changes fast enough to put the forecast beyond reach.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The question** **[M1995-038]**: "why is that castle still standing? And what’s going to keep it standing or cause it
not to be standing five, 10, 20 years from now." A moat is what "protects excellent returns on invested capital"
**[L2007-004]**, and it is judged, not measured **[M1999-108]**.

**The parts table** (framework Q2, A business of parts, CONVENTION adopted 2026-10-06; "lumping them together [...]
impedes analysis" **[L2008-005]**). Segment income as the filer defines it (before intangible amortization,
restructuring and transformation costs), FY2021 to FY2025 on the 2025 segment structure, from the FY2023 10-K
(`0000077360-24-000007`, which restates 2021 and 2022) and the FY2025 10-K (`0000077360-26-000007`):

| part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year total | share | decides |
|---|---|---|---|---|---|---|---|---|
| Pool | 452.7 | 462.1 | 417.0 | 476.5 | 527.1 | 2,335.4 | 49.1% | yes (the largest; none above half) |
| Flow | 213.3 | 242.3 | 282.3 | 318.1 | 362.1 | 1,418.1 | 29.8% | no |
| Water Solutions | 101.7 | 149.0 | 247.6 | 255.1 | 253.9 | 1,007.3 | 21.2% | no |

On the 2026 structure (residential and irrigation pumps moved to Water Solutions; the FY2025 10-K restates 2023 to 2025
only) Pool is 1,420.6 of 3,139.7 over three years, 45%, still the largest. **Pool decides.**

**The deciding part's record over the span** (Pool, or Aquatic Systems before 2020; sales / segment income / margin,
$M): FY2017 939.6 / 254.1 / 27.0%; FY2018 1,026.1 / 277.6 / 27.1%; FY2019 985.3 / 268.9 / 27.3% (FY2019 10-K
`0000077360-20-000006`); FY2020 1,123.5 / 321.4 / 28.6%; FY2021 1,572.0 / 452.7 / 28.8%; FY2022 1,632.7 / 462.1 / 28.3%
(FY2022 10-K `0000077360-23-000006`); FY2023 1,343.6 / 417.0 / 31.0%; FY2024 1,436.1 / 476.5 / 33.2%; FY2025
1,558.8 / 527.1 / 33.8%; H1 2026 633.7 / 185.7 / 29.3%, of which Q2 2026 246.6 / 57.6 / 23.4% (10-Q
`0000077360-26-000045`).

**The castle tests, each with its filing fact.**
1. *What keeps it standing* **[M1995-038]**. Three things the filings show: an installed base that must be repaired
   and replaced (Q1's key variable; Hayward puts the aftermarket at about 85% of its sales); the place on the
   distributor's shelf, through which "approximately 80% of residential pool equipment in the U.S. was sold" (Hayward
   10-K FY2025 `0001834622-26-000008`); and the servicer's and builder's habit, which Hayward names as "the loyalty of our
   builders and servicers with whom we have built a large installed base" (same). Pentair's own filing claims only that
   "our distribution channels and reputation for quality also provide us a competitive advantage" (10-K FY2025).
2. *Ask the customer, over twelve years.* Pool Corporation, the largest distributor, names its largest suppliers each
   year with their share of its cost of products sold: Pentair 19% (2014), 20% (2016), 20% (2018), 20% (2020), 18%
   (2022), 20% (2024), 20% (2025); Hayward 11%, 10%, 9%, 10%, 11%, 11%, 11%; Zodiac 7%, 8%, 8%, 9%, 9%, 12%, 12% (POOL
   10-Ks FY2014 `0000945841-15-000034`, FY2016 `0000945841-17-000028`, FY2018 `0000945841-19-000013`, FY2020
   `0000945841-21-000022`, FY2022 `0000945841-23-000015`, FY2024 `0000945841-25-000032`, FY2025
   `0001193125-26-074833`). Pentair has been the largest supplier to the largest distributor at a steady fifth of its
   purchases through a bust (2014), a boom (2020 to 2022) and the normalization after it.
3. *The attacker with money* **[M2011-015]**. The attacker that gained is Zodiac (Fluidra's; **Fluidra is not an SEC
   filer, so its own figures are not on this record, flagged**): its share of POOL's purchases rose from 7% to 12% over
   the span, while Pentair's held and Hayward's held. So a funded attacker has taken ground on the shelf, but not
   Pentair's ground at that distributor, on this evidence.
4. *Pricing power and the agony before a rise* **[M2005-020]**. Pool price added 2.9% in 2024, 5.1% in 2025, and 3.9%
   in Q2 2026 in the middle of a 46% volume fall (10-K FY2025; 10-Q Q2 2026); consolidated price added 4.6%, 13.3%, 6.4%,
   1.9% and 4.0% in 2021 to 2025, about 33% compounded, while volume fell 7.1%, 11.3%, 2.3% and 2.1% in 2022 to 2025
   (FY2021, FY2022, FY2023 and FY2025 10-Ks, "Price" and "Volume" lines). Pool's margin rose from 27% to 34% through the
   last inflation, the evidence that the strong position passes cost through **[M2005-017]**. The test cuts the other
   way too **[M2001-087]**: a seller can price past its moat and lose share. Read against the rival, it did not here:
   Hayward took more price in the same quarter, 7.0% in North America, and its volume still rose (Hayward 10-Q Q2 2026
   `0001834622-26-000047`).
5. *Unit volume* **[M1999-054]**. Pool volume rose 4.1% in 2024 and 1.4% in 2025, then fell 27.2% in H1 2026 and
   46.3% in Q2 2026. This is the evidence against, taken up under test 9.
6. *The brand against the intermediary* **[M2019-041]**, **[M2001-090]**. This is the castle's soft wall. One customer
   in Pool (Pool Corporation, named in the FY2018 to FY2020 10-Ks) took about 15% of Pentair's consolidated sales in 2016
   to 2020, 20% in 2021 and 2022, 15% in 2023 and 2024 and 18% in 2025 (FY2019, FY2021, FY2023 and FY2025 10-Ks): about
   half of Pool's sales. POOL says it is growing "proprietary and exclusive brands" and "increased private label sales"
   (POOL 10-K FY2025; 10-Q Q2 2026), and Hayward warns that "a competitor-customer may reduce or discontinue purchases in
   favor of internally developed or alternative products" (Hayward 10-K FY2025). The rows put it plainly: where the
   intermediary is trusted as much as the brand, "the value of having the brand moves over to the retailer"
   **[M2001-090]**. The evidence that the brand still holds is test 2: the distributor has kept buying a fifth of its
   goods from Pentair for twelve years while building its own lines.
7. *The low-cost position* **[M2018-043]**: not claimed by the filer and no evidence for it; not the castle here.
8. *The field's returns over the last full cycle* (framework Q2, What it rules OUT, the standing castle that protects
   only ordinary returns). Pentair Pool's segment margin was 27% to 34% in every year from 2017 to 2025, through the
   boom of 2020 to 2022 and the fall of 2023 (Pool sales down 18%, margin up to 31%). Hayward, the one pool rival that
   files: segment margin 23.1% (2020), 29.9% (2021), 27.1% (2022), 25.1% (2023); North America 24.3%, 31.0%, 27.8%,
   26.2%, 29.2%, 29.7% for 2020 to 2025 (Hayward 10-Ks FY2021 `0001834622-22-000024`, FY2023 `0001834622-24-000010`,
   FY2025). Both spend 2% to 3% of sales on capital goods (Pentair capex $60M to $85M a year on $3.8B to $4.2B of sales;
   Hayward $14M to $31M on $0.9B to $1.4B; `comp.py` from the filed cash-flow statements). Judged in words: the field's
   two filing members earn high operating margins on little tangible capital through a full boom and bust; the returns
   it protects are not ordinary. (Hayward's return on what its buyers paid is ordinary, because its balance sheet
   carries $951M of goodwill and $1,003M of intangibles from its buy-out; that is price, not castle.)
9. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**, and *what could reduce it* **[M2000-014]**. The 2026
   evidence, set out side by side:
   - Pentair Pool sales Q2 2026 $246.6M against $427.2M, a fall of $180.6M; volume down 46.3%, price up 3.9%; the filer
     attributes it to "a more pronounced inventory realignment with major channel partners than previously estimated and
     worsening business conditions" and guides a full-year destock of about $250M of Pool sales (10-Q Q2 2026).
   - Hayward, same quarter: sales up $18.8M (6.3%); North America up $22.5M (8.8%), of which price 7.0 points and
     volume 1.8 points (Hayward 10-Q Q2 2026).
   - Pool Corporation, same quarter: sales of equipment "increased 3%", building materials up 4%; its inventory up 4%
     year on year (POOL 10-Q Q2 2026 `0001193125-26-322532`).
   - The year before: Pentair Pool 2025 sales up 8.5%, core up 6.5%, Q4 2025 up 11% (Q4 release, 8-K
     `0000077360-26-000003`), while POOL's sales of equipment in 2025 "were flat compared to 2024" (POOL 10-K FY2025).
   Reading: the end customer kept buying pool equipment from the distributor (POOL's equipment sales up), and Pentair's
   lost $180M in the quarter did not reappear as a rival's gain of anything like that size (Hayward's North America gain
   was $22.5M, most of it price; Zodiac's is not on the record). So most of the fall was the channel drawing down Pentair
   stock that Pentair had shipped ahead of sell-through in 2025, not end customers leaving Pentair. That is a cyclical,
   self-made problem of the kind the rows say to sort from a secular one **[L1995-022]**, but the sorting cannot be
   finished from the record: whether POOL used the reset to give shelf to its own lines will show only in its next
   supplier percentages (FY2026 10-K, February 2027). The resignation of the Pool chief executive four days before the
   Q1 release, with the role eliminated, and the filer's promise of "strengthening its relationships with channel
   partners" (8-K `0000077360-26-000039`) say the relationship was strained; they do not say it was lost.
10. *Would it stand without the lord* **[M1996-037]**: the Pool segment's own chief executive role was eliminated on
   2026-04-28 and Pool is now run by the president of all three segments (8-K `0000077360-26-000024`); the business ran on the installed base and the shelf, which is the kind of castle that does not depend
   on the lord.

**The non-deciding parts.** Flow and Water Solutions: margins rose from 15.0% and 13.2% (2021) to 23.3% and 23.9%
(2025) on price and "transformation" productivity, while their volumes fell (Flow volume down 6.0% in 2024 and 2.4% in
2025; Water Solutions down 4.8% and 6.3%; 10-K FY2025), and the filer says each "faces numerous domestic and
international competitors, some of which have substantially greater resources" and is "competitively priced" (10-K
FY2025). Their castles are not shown by these filings; under the convention they do not close the file and, if open,
are carried to Q7 at no growth. Q7's organic growth for the whole company over the window is 0.6% a year, so the
carriage changes nothing material there.

**The competitor row** (same metric, own filings): pool segment margin, Pentair Pool 28.3% to 33.8% (2021 to 2025) against
Hayward 25.1% to 29.9% total and 26.2% to 31.0% North America over the same years; share of POOL's purchases 2014 to
2025, Pentair 18% to 20%, Hayward 9% to 11%, Zodiac 7% to 12% (accessions above). Pool Corporation itself (the
distributor): operating margin 11.0% (2025) and 16.6% (2022), gross margin 29.7% (2025) (`comp.py`; POOL 10-K FY2025):
the intermediary earns less on sales than the maker. A. O. Smith and Xylem bear on the non-deciding water parts only:
A. O. Smith operating margin 10% to 21% over 2019 to 2025 (17% to 21% in every year but 2022), Xylem 7% to 14% (`comp.py`, XBRL first-filed facts, CIKs
91142 and 1524472); Pentair's Water Solutions and Flow at 13% to 24% sit inside that band, ordinary-to-good water
equipment returns, which is why their castles are not credited here.

**VERDICT: IN.** The deciding part's castle stands on the evidence of twelve years at a steady fifth of the largest
distributor's purchases **[M1999-108]**, margins held and widened through the last inflation by price that rivals
matched **[M2005-017]**, **[M2005-020]**, and a field that protects excellent returns **[L2007-004]**. The 2026 collapse
in Pentair's sell-in is written down as the strongest evidence against and is not shown, on the record, to be the
customer choosing the rival; it is shown to be largely the channel unwinding Pentair's own 2025 shipments
**[L1995-022]**. What could reduce the castle is named **[M2000-014]**: the distributor's own brands and its power over
timing **[M2001-090]**, **[M2019-041]**. It is carried to Q7 as a matter of how sure, not settled here.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**The capital the business needs** **[M2010-090]**, read on tangible assets **[M2011-060]** (script `q3.py`, from the
filed balance sheets and income statements of the 10-Ks listed at Step 0). Tangible capital employed (equity plus debt
less cash, less goodwill and intangibles) was $146M to $795M from 2019 to 2025, against operating income before
amortization of $459M to $916M: the business runs on almost no tangible capital, more than 100% pretax on it in every
year. Capital spending was $58M to $85M a year (1.5% to 2.1% of sales), against depreciation of $46M to $60M; the
filing gives no split between keeping and growing **[M2000-144]**, **[L1999-024]**, so capex at about 1.2 times
depreciation is read as mostly maintenance, the kind of spending that keeps the business "in the same economic place"
**[L2000-035]**. Working capital (receivables plus inventory less payables) is about a quarter of sales and swings with
the early-buy season.

**What the added capital earned** (goodwill included, "because we paid for it" **[M2011-060]**). Capital employed went
from $2,550M (2018, just after the spin) to $5,406M (2025), up $2,856M, of which $2,649M was paid for businesses net of
businesses sold (2019 to 2025). Operating income went from $437M to $858M, up $420M: about 14.7% pretax on the added
capital, roughly 12.7% after the company's 13% to 14% tax. The pretax return on all capital employed ran 12.1% (2022,
the Manitowoc year) to 19.8% (2021), 15.9% in 2025. So the business itself is the best kind, which "gives you more and
more money every year without putting up anything to get it, or very little" **[M1998-081]**, but its growth since 2018
has been bought, at returns that are decent rather than high: the second-best case of "decent returns on the incremental
sums they invest" **[L2009-012]**. Organic growth over the window was small (core sales growth 6.2%, minus 4.9%, minus
0.4% and 1.9% in 2022 to 2025, about 0.6% a year compounded; 10-Ks FY2022 to FY2025), with price covering a fall in
volume.

**WEIGHS FOR** on the business (high return on the tangible capital it needs, little spending to stand still
**[M1998-081]**), with the qualification that the growth was bought at about 13% after tax, a decent second-best rate
**[L2009-012]**; the buying is weighed again at Q6 as a use of the money.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, nine year-ends** **[M2025-032]** (`tools/run.py` transcription, checked against the filed
balance sheets for 2024 and 2025 in the FY2025 10-K and for 2019 to 2023 in their 10-Ks; $M):

| year-end | assets | equity | goodwill | intangibles | LT debt | cash | receivables | inventory | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 8,634 | 5,038 | 4,351 | 1,558 | 1,441 | 113 | n.r. | 581 | 2,482 |
| 2018 | 3,806 | 1,836 | 2,073 | 276 | 788 | 74 | n.r. | 388 | 169 |
| 2019 | 4,140 | 1,954 | 2,258 | 339 | 1,029 | 82 | 503 | 377 | 401 |
| 2020 | 4,197 | 2,106 | 2,392 | 326 | 840 | 82 | 368 | 420 | 631 |
| 2021 | 4,754 | 2,422 | 2,504 | 428 | 894 | 94 | 534 | 563 | 1,051 |
| 2022 | 6,448 | 2,708 | 3,253 | 1,095 | 2,317 | 109 | 532 | 790 | 1,390 |
| 2023 | 6,563 | 3,217 | 3,275 | 1,042 | 1,988 | 170 | 562 | 678 | 1,866 |
| 2024 | 6,446 | 3,563 | 3,287 | 1,034 | 1,639 | 119 | 565 | 611 | 2,336 |
| 2025 | 6,869 | 3,869 | 3,538 | 1,073 | 1,639 | 102 | 673 | 633 | 2,823 |
| 2026-06-30 | 6,712 | 3,749 | 3,518 | 1,041 | 1,606 | 92 | 483 | 666 | 3,037 |

(n.r. = not read for that year. 2026-06-30 from the Q2 10-Q.) What moved and why: the 2018 spin of nVent took equity
from $5.0B to $1.8B and retained earnings from $2.5B to $0.2B (the dividend in specie). Since then retained earnings
rose by $2.65B while net income summed to about $4.0B and dividends to about $1.2B, which reconciles. Goodwill and
intangibles doubled, from $2.35B to $4.61B, almost all of it bought (in 2022, the Manitowoc Ice year, goodwill rose $749M
and intangibles $667M); equity ($3.87B) is now less than goodwill and intangibles ($4.61B), so tangible
equity is negative, which is what a capital-light business that buys its growth looks like. Debt rose with Manitowoc to
$2.3B, was paid down to $1.6B, and is about to rise by $1.4B for Taco. Receivables against sales: 17.0% (2019), 12.2%,
14.2%, 12.9%, 13.7%, 13.8%, 16.1% (2025); the 2025 year-end figure is high but inside the span, and the filer has said
before that early-buy shipments with extended terms move between years (FY2021 10-K, on 2020 into 2021). Inventory
against sales 15% in 2024 and 2025; at 2026-06-30 inventory is up to $666M while sales fall: Pentair now holds stock the
channel did not take. What the figures cannot say: how much of Pentair's product sits in the distributors' warehouses.

**Looked at twice** **[M1995-064]**. Receivables rose 19% in 2025 on sales up 2%, in a year when Pool's sales rose 8.5%
and the distributor's own equipment sales were flat (Q2, test 9). The second look: the receivables were collected; they
fell from $673.2M to $482.7M by 2026-06-30, and the filer reports "an increase in cash collections during the period"
(10-Q Q2 2026). The sales of 2025 were real sales, paid for in cash; what they did was borrow from 2026's. That is a
fact for Q7's base year and for Q5, not a profit that may not exist.

**The real costs.**
- *Depreciation* ($59.6M in 2025) against capex ($68.8M): close, capex slightly above; owner cash takes capex.
- *Amortization* ($58.1M in 2025) of acquired customer relationships, trade names and technology; owner cash is built
  from operating cash flow, which already adds it back, and the capital spent to buy those intangibles is charged at
  Q7 as acquisition spending.
- *Stock pay*: $29.8M, $24.9M, $29.1M, $39.7M, $37.0M (2021 to 2025, filed cash-flow statements); a real cost
  **[L2015-003]** and deducted in owner cash. The filer's "free cash flow" (operating cash flow less capex plus asset-sale
  proceeds) does not deduct it.
- *The recurring "one-time"*: restructuring $7.4M, $36.7M, $9.1M, $34.4M, $31.3M and transformation $11.7M, $27.2M,
  $44.3M, $52.0M, $41.0M in 2021 to 2025, $295M together, about $59M a year, every year, and $77.3M more in H1 2026 (MD&A
  of the FY2022 to FY2025 10-Ks and the Q2 2026 10-Q). They are excluded from "segment income", "adjusted operating
  income" and "adjusted EPS". Told year after year not to count necessary adjustments, owners are being misled
  **[L2016-007]**; "a large chunk of costs that should properly be attributed to a number of years" **[L1998-031]**. They
  are cash, and owner cash bears them.
- *Tax*: effective rate 14.1% (2025), 13.0% (2024), a benefit in 2023 (minus 0.6%, discrete items); cash taxes paid
  $86.9M, $121.0M, $120.0M (2025, 2024, 2023). Owner cash uses cash taxes actually paid, inside operating cash flow.

**EBITDA and the adjusted figure in the filer's own mouth.** The 2026-07-14 release gave "EBITDA for the year is
expected to be approximately $1,050 million", defined as adjusted operating income plus depreciation (8-K
`0000077360-26-000039`); the regular releases feature "core sales", "adjusted operating income", "adjusted EPS" and "free
cash flow", and the filer says "adjusted EPS is used as a criterion to measure and pay long-term incentive compensation
and adjusted operating income is used as a criterion to measure and pay annual incentive compensation" (8-K
`0000077360-26-000042`). Guidance is given every quarter and was missed by about 18 points of sales growth within eleven
weeks (guide of up about 1% for Q2 on 2026-04-28, preliminary down 17% on 2026-07-14). These are the habits the
framework weighs here and carries to Q5: "a management that regularly attempts to wave away very real costs by
highlighting" an adjusted per-share figure "makes us nervous" **[L2016-006]**; guidance is "the scourge"
**[L2019-006]**; EBITDA as a figure is "utter nonsense" **[M1998-086]**, and of companies "where people are talking about
EBITDA" the count of purchases "is going to be about zero" **[M2002-026]**.

**VERDICT on the accounts: WEIGHS AGAINST, no STOP.** The statements are clear and reconcile; the one tell found in them
(receivables against sales) was looked at twice and turned into cash **[M1995-064]**, so there is no confusion
**[M1995-063]** and no suspicion that the statements themselves raise. A management "preoccupied with accounting
considerations" is "a negative" and not "a total exclusionary factor" **[M1994-018]**: the recurring adjustments,
adjusted figures paid on, the EBITDA line and quarterly guidance weigh against and are carried to Q5. The recast owner
cash (operating cash flow less stock pay less capital spending, before and after acquisitions) feeds Q7.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
*(pending)*

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**Who.** John L. Stauch, chief executive since 2018, the company's chief financial officer from 2007 to 2018 (10-K
FY2025, executive officers), so the man who ran the money through the Tyco merger, ERICO, the sale of Valves & Controls
and the nVent spin now runs the business. An independent chair (DEF 14A 2026 `0000077360-26-000014`). The two yardsticks
are how well they run the business, read against "the hand they were dealt", and "how well that they treat their
owners" **[M1994-008]**.

**The integrity record, with the habits carried from Q4** **[M2004-067]**, **[M2013-088]**.
- *For candour.* The Q2 miss was announced on 2026-07-14, two weeks after the quarter closed and two weeks before the
  regular release, with a CFO change and a guidance cut in one document (8-K `0000077360-26-000039`): that is telling
  "the bad news immediately" **[M1998-039]**. The chief executive's own words own the miss: "our results were below
  expectations due primarily to a larger-than-anticipated inventory correction in the Pool channel" (Q2 release, 8-K
  `0000077360-26-000042`).
- *Against candour.* The same releases add "worsening business conditions, including higher interest rates and
  inflation"; in the same quarter the rival's volume and the distributor's equipment sales rose (Q2, test 9), so the
  outside cause is not borne out by the filings of the outside world. The Q1 release of 2026-04-28 guided Q2 sales up
  about 1%, four days after the Pool chief executive resigned, and said nothing of channel inventory (8-K
  `0000077360-26-000023`, searched for "destock", "channel inventor", "channel partner" and "early buy": no instance). The
  10-K of 2026-02-24 explained a 33% fall in Pool's year-end backlog by "timing of delivery of orders associated with
  certain advance sale (“early buy”) programs" (10-K FY2025, MD&A).
- *The make-the-numbers habit.* 2025 annual incentive for the chief executive and CFO: adjusted operating income 50%,
  revenue 30%, free cash flow 20%; revenue came in at 100.3% of target and the plan paid 109.9% (DEF 14A 2026, CD&A).
  Pool's Q4 2025 sales rose 11% while the distributor's own equipment sales for 2025 were flat, and that stock came back
  in 2026 (Q2, test 9). The rows warn that targets declared and met tempt "to make up the numbers" **[L2002-041]** and
  that predictions "corrode CEO behavior" **[L2000-039]**.
- *What the record does not show.* No restatement, no investigation and no securities class action disclosed in the Q2
  2026 10-Q (read for "class action", "subpoena", "investigation"; no instance bearing on the company's own reporting).
  The receivables of 2025 were collected in cash (Q4). The early-buy programme, with its "extended payment terms and/or
  additional discounts", is disclosed in every 10-K read back to FY2017. Insider selling before the reset was small
  and the chief executive sold none: Forms 4 and 144 from 2025-07-01 show open-market sales of 7,786 shares by the
  departing CFO (2025-11), 6,558 by a director (2025-12), 7,000 by a director (2026-02) and 6,493 by the technology
  officer (2026-02), each under $1M; the chief executive's only dispositions were shares withheld for tax. He held
  893,949 shares worth $93.1M at 2025 year-end (DEF 14A 2026), about eight years of his total pay, and has lost about
  half of it in the fall.

**Judgment on integrity.** The facts against are of judgment and of habit: a channel loaded in a pay year, a guide that
did not see it coming, an outside cause that the outside world does not confirm. The facts for are of conduct: the
sales were real and paid, the bad news came early and in the chief executive's own words, and the chief executive has
his own fortune in the stock and did not sell ahead of the news. Read together, they leave doubt about how well the
channel was seen and managed, which is ability; they do not leave doubt that the people are honest, which is the STOP
**[M2015-047]**, **[M2013-088]**. Integrity is applied on doubt alone, and this is the closest call in the file: it is
recorded so that a later run reads it first.

**Ability.** The record against the hand dealt **[M1994-008]**: a castle handed over with a steady fifth of the largest
distributor's purchases, margins raised from 27% to 34% in Pool and, from 2021 to 2025, from 15.0% to 23.3% in Flow and from
13.2% to 23.9% in Water Solutions; set against that, in twelve months: the CFO resigned (2025-10) and was paid severance on a voluntary
resignation (8-K `0000077360-25-000045`), his successor left after four months (8-K `0000077360-26-000039`), the Pool
chief executive resigned and his role was abolished (8-K `0000077360-26-000024`), guidance missed by 18 points within
eleven weeks, $350M of stock bought back at about $87.50 in the half before the price halved (Q6), and a $1.425B
debt-financed purchase agreed two weeks after the miss (Q6). "the number one risk factor is that this business gets
the wrong management" **[M2021-042]**; the business is good enough that the people matter less than the castle
**[M1996-037]**, but the year shows a management that did not see its own channel.

**VERDICT on integrity: IN** (no doubt found that the people are honest; the habits and the channel facts are recorded
and weighed) **[M2013-088]**, **[M1998-039]**. **Ability WEIGHS AGAINST** **[M1994-008]**, **[M2021-042]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
*(Written by the resuming session, 2026-10-10, after reading the run file and `_notes.md`; the buyback line uses the
bottom of Q7's range and was written with Q7, as the template asks.)* The question is how "to wisely employ its cash
flows" **[L1993-020]**, and "What do we do with the money, as it comes in?" **[M2001-111]**.

### Part A: the money
**Where the money went, FY2021 to FY2025** (filed cash-flow statements and equity notes, 10-Ks FY2021 `0000077360-22-000006`,
FY2023 `0000077360-24-000007`, FY2025 `0000077360-26-000007`; $M): net income 2,935.8; dividends 733.4; share
repurchases 575.0; acquisitions net of businesses sold 2,318.7 (Manitowoc Ice $1,580.9M in 2022 the largest); capital
spending 364.6. Then H1 2026: repurchases $350.0M, dividends $87.5M, and on 2026-07-27 Taco agreed at $1.425B (10-Q
`0000077360-26-000045`). Organic growth over the window was about 0.6% a year (Q3): the business does not use its own
cash internally, and the filer spends it on purchases, buybacks and a dividend.

**The retention test** **[R1995-009]**, **[M1998-110]**. Earnings kept after dividends, FY2021 to FY2025: $2,202M ($1,627M
after buybacks as well). Market value: 166.1M shares at $53.09 = $8,818M at 2020 year-end (shares, FY2021 10-K balance
sheet; price, Yahoo chart series, aggregator, flagged); 163.2M at $104.14 = $16,996M at 2025 year-end; 159.6M at $52.47
= $8,376M on 2026-10-09. To 2025 year-end the test passes easily, "at least $1 of market value for each $1 retained"
**[R1995-009]**; measured to today it fails, the market value being below 2020's after $2.2B kept. The market leg alone
misleads "When the stock market has declined sharply over a five-year stretch" **[R2009-002]**, so the intrinsic leg is
read too, and it splits: Q3 found the capital added since 2018 earning about 14.7% pretax, about 12.7% after the
company's tax, a dollar kept worth more than a dollar at the 5.60% rate; Q7 below finds that the purchases, about $464M a
year over the window, bought total sales growth of 2.6% a year against 0.6% organic, and that on Q7's convention the
range with the purchases deducted ($36.95 to $49.63) sits wholly below the organic range ($58.74 to $62.18): on the
arithmetic, the buying spent more than the growth it bought was worth at the cap (f) imposes. The forward question,
"Can you keep using all of the capital you generate, effectively, for a very long time?" **[M2010-097]**, the filer
answers by buying businesses; the internal use the rows put first, "reinvestment possibilities offered by its current
business" **[L2012-011]**, is small here by the business's own nature (capital-light, Q3).

**Buybacks** **[L1999-023]**, **[L2016-002]**. The authorizations are dollar sums with an expiry and no price: $750.0M
(2020 Authorization, to 2025-12-31) and $1.0B (2025 Authorization, to 2028-12-31) (10-K FY2025, Item 5); no
instance found in the 10-Ks FY2021 to FY2025 or the Q2 2026 10-Q of a price above which repurchases stop (searched for
"repurchase"). That is the programme the rows describe, "almost never refer to a price above which repurchases will be
eschewed" **[L2016-002]**; "Most companies adopt repurchase programs and they just say" a sum **[M2019-002]**. The prices
paid, from the filed counts and sums: $40.59 (2020), $71.43 (2021), $50.00 (2022), none (2023), $93.75 (2024), $97.83
(2025), $100.00 (Q1 2026), $75.00 (Q2 2026). **The convention's exception, tested** (framework Q6, the buyback with no
stated price): the bottom of Q7's central range is **$36.95** (all-equity; $37.61 equity-only); every purchase from 2021
sits above it, and the purchases of 2021 and 2024 to 2026 sit above the top of every range Q7 builds with the growth cut
by (f) (the highest such top is $65.40, the seven-year case). So the exception does not apply and the programme weighs
against: "If you’re repurchasing shares above a rationally calculated intrinsic value, you are harming your shareholders"
**[M1996-013]**. Confessed: the range is today's, set against prices paid in earlier years when the record was better;
against the uncut literal top ($95.85), only the purchases of 2025 ($97.83) and Q1 2026 ($100.00) sit above it. The funds test cuts against too: the $350M of H1 2026 was bought while the company drew a new $500M term loan and
its revolver (8-K `0001104659-26-056228`), in the half its sales fell, and a month before it committed to $1.4B of new
debt for Taco; the rows ask for funds "cash plus sensible borrowing capacity -- beyond the near-term needs of the
business" **[L1999-023]**.

**Issuance and deals** **[M1995-001]**, **[L2017-004]**. No shares issued for a deal: the count fell from 166.1M (2020)
to 159.6M (2026-06-30). Taco is paid in cash and new debt (10-Q note 16; 8-K `0001104659-26-104725`), so **the one STOP
of Part A, the all-stock deal by an undervalued acquirer** **[L2009-019]**, **is not met**. The deals are weighed by value
given against value got: with cash, "we are worse off. We may not have issued a share of stock." **[M1995-001]** applies
the same test. Manitowoc Ice ($1,580.9M, 2022, financed by a term loan and the 2032 notes, $1,391.3M; FY2023 10-K) is
the one large deal inside the window; Water Solutions' segment income went from $149.0M (2022) to $253.9M (2025) (Q2's
parts table), and Q3's return on the capital added (about 12.7% after tax) is the record of the buying as a whole. No
instance found of a comparison of the Manitowoc result with its projections in the 10-Ks FY2023 to FY2025 (searched for
"Manitowoc"); "Post mortems of acquisitions, in which reality is honestly compared to the original projections, are rare
in American boardrooms" **[L2014-013]**. Taco: $1.425B for a private company whose sales and earnings are not filed (the
8-K of 2026-07-28 carries one exhibit, the Q2 release; the Taco release was not filed), so value given against value got
cannot be tested from the record; the filer's own risk factor speaks of "revenue synergies, cost savings and operational
efficiencies" (10-Q Q2 2026, Item 1A), where the rows "never count on synergies when we acquire companies"
**[L2016-008]**; and it is debt-financed, where the rows "evaluate acquisitions on an all-equity basis" **[L2017-004]**. It
was agreed thirteen days after the guidance cut and the CFO's departure, with an interim CFO in the chair; the board's
third job is to "bring some independent judgment in on major acquisitions" **[M2007-120]**, and the rows name "all these
forces that push toward deals" **[M2014-076]**. Whether the board did so is not on the record.

**Dividends.** Paid every quarter (200 consecutive) and raised for 50 consecutive years, $1.00 a share in 2025, about a
quarter of net income (10-K FY2025, Item 5 and note on equity): a policy that is "clear, consistent and rational"
**[L2012-015]**, and, for a business that grows 0.6% a year organically, the right kind of use: "a company that expects to
regularly earn more than it can profitably employ in its business, should be paying out dividends" **[M2004-089]**.

**Part A: WEIGHS AGAINST.** The dividend is sound **[M2004-089]**; the buybacks are fixed sums at prices above every range
Q7 builds **[L2016-002]**, **[M1996-013]**; the growth was bought, not grown, and at the cap the buying is worth less than
it cost **[L2000-023]**; and a $1.425B debt-financed purchase whose value cannot be tested from the record was agreed in
the quarter of the miss **[M1995-001]**, **[L2016-008]**. The all-stock STOP is not met **[L2009-019]**.

### Part B: the pay, the board and the owners
**The pay** (DEF 14A 2026 `0000077360-26-000014`, Summary Compensation Table and CD&A). Chief executive's total pay
$11.37M (2025), $10.77M (2024), $10.01M (2023). Annual incentive: adjusted operating income 50%, revenue 30%, free cash
flow 20% (Q5). Long-term, for the chief executive: performance share units 75% and stock options 25%; the units of
2023 to 2025 were measured on adjusted EPS (75%) and ROIC (25%) and paid 142.15% of target; the units of 2026 to 2028
add revenue at 25% "to accelerate the focus on growth" (DEF 14A). The options have "a term of 10 years", vest over three
years, and are struck at the closing price on the grant date (DEF 14A); no step-up is described.
- *Tied to what the person controls* **[M2003-019]**. Adjusted operating income and adjusted EPS leave out the $59M a
  year of restructuring and transformation costs Q4 found recurring; "you get what you reward for" **[M2016-083]**, and
  the rows are nervous of "a management that regularly attempts to wave away very real costs" **[L2016-006]**. Revenue at
  30% of the annual plan and 25% of the new units pays for growth however it is got, in a business whose growth is bought
  (Q3), and was the measure met in the year the channel was loaded (Q5).
- *Options* **[L1994-021]**, **[M1997-043]**: ten-year, fixed-price options are the form the rows call misaligned, "the
  combination of a ten-year option, a low dividend payout, and compound interest can provide lush gains to a manager who
  has done no more than tread water in his job" **[L1994-021]**; the dividend here is not low, which softens it.
- *For*: ROIC is a capital element in the long-term units, the practice the rows describe, "charge managers a high rate
  for incremental capital they employ" **[L1994-019]**; a clawback policy extended to equity awards (DEF 14A); the chief
  executive holds 893,949 shares (Q5), so he is a partner on the way down.
- *Who designs it*: a compensation consultant (Aon) and a comparator group benchmark pay for executives and directors
  (DEF 14A); "we do not bring in compensation consultants" **[M2004-016]**; "comp committees have become slaves to
  comparative data" **[L2005-015]**.

**The board.** An independent chair (David A. Jones), the roles separated since 2018, and every director but the chief
executive independent (DEF 14A): the opposite of the case the rows warn of, "how hard it is to replace a mediocre CEO if
that person is also Chairman" **[L2014-026]**. Director pay $336,833 to $585,947 in 2025, of which $164,957 in stock
awards; directors' holdings 3,566 to 34,138 ordinary shares (beneficial ownership table, 2026-03-06); whether any was
bought "with their savings, rather than simply having been the recipients of grants" **[L2019-008]** cannot be told from
the table.

**The owners.** Quarterly guidance is given and was missed by 18 points (Q4, Q5), "the scourge of earnings" guidance
**[L2019-006]**; the bad news came early and in the chief executive's own words (Q5). The pay sins weigh less than the man:
"any compensation sins are generally of minor importance" **[M2007-006]**.

**Part B: WEIGHS AGAINST, mildly.** Pay on adjusted figures and revenue, fixed-price ten-year options and benchmarking
**[M2016-083]**, **[L1994-021]**, **[L2005-015]**, against an independent chair, a capital element in the units and a chief
executive with his fortune in the stock **[L2014-026]**, **[L1994-019]**.

**VERDICT Q6: WEIGHS AGAINST** (Part A and Part B), recorded and carried **[L1993-020]**; the STOP inside Part A is not
met **[L2009-019]**.

## Q7 — WHAT IS IT WORTH? STOP.
*(Script `q7_final.py`, output `q7_final_out.txt`. The earlier session's draft, `q7.py` and `q7_out.txt`, is kept as its
record and not used: it was written before Q6 and before the 2026-10-10 amendments to specifics (c) and (f) were applied,
so it charged the acquisition spending after year ten and carried an uncut growth rate. Its inputs were checked line by
line against the filed cash-flow statements and are unchanged in `q7_final.py`.)*

**The definition** **[R1996-018]**: "the discounted value of the cash that can be taken out of a business during its
remaining life"; credit only "for whatever net cash is left every year" **[M1998-080]**; and "are you going to have to put
more cash into after you buy it?" **[M2014-068]**, which for this business is the acquisition spending. Rate: **5.60%**, the
30-year Treasury par yield, 2026-10-09 (Step 0).

**Owner cash, as Q4 recast it** (filed cash-flow statements; $M; all-equity = operating cash flow plus cash interest
after the company's 14% rate, less stock pay, less all capital spending; equity-only = operating cash flow less stock
pay less capital spending; acquisitions net of businesses sold):

| year | all-equity owner cash | equity-only | acquisitions | all-equity / sales |
|---|---|---|---|---|
| 2019 | 294.3 | 265.3 | 272.5 | 10.0% |
| 2020 | 527.0 | 491.7 | 58.0 | 17.5% |
| 2021 | 549.3 | 523.6 | 337.1 | 14.6% |
| 2022 | 303.2 | 254.2 | 1,580.9 | 7.4% |
| 2023 | 641.6 | 515.7 | 0.6 | 15.6% |
| 2024 | 778.0 | 652.8 | 108.0 | 19.1% |
| 2025 | 777.6 | 709.0 | 292.1 | 18.6% |

Window FY2021 to FY2025: all-equity owner cash averages **$610.0M**, equity-only $531.1M, acquisitions $463.7M, sales
$4,050M. Trailing twelve months to 2026-06-30, equity-only owner cash $637.7M against $709.0M for FY2025 (direction only;
10-Q Q2 2026).

**The window specifics applied** (Q7's range convention and its specifics, as the text stands after 2026-10-10).
- *(a) Cycles.* Both end years are unusual on the filer's own description: 2021, "In 2021 and 2020, the COVID-19
  pandemic significantly impacted economic activity and markets around the world and our business" (FY2021 10-K, Item
  1A); 2025, whose Pool shipments the filer's 2026 documents say ran ahead of the channel ("inventory realignment with
  major channel partners", 8-K `0000077360-26-000039`; 10-Q Q2 2026). "If either year was aberrational, any calculation of
  growth will be distorted" **[L2005-003]**. The cycle base is the last full cycle peak to peak on the owner-cash series:
  peaks in 2021 ($549M) and 2024 to 2025 ($778M), so the window FY2021 to FY2025 itself runs peak to peak, and the cycle
  base equals the literal window's average, $610.0M (shown together; the 2021 to 2024 peak-to-peak average, $568.0M, is
  lower and is not taken, since 2025's cash was collected, Q4). The comparable history begins in 2018 (Q1), so there is
  only one full cycle and no growth between successive cycles can be measured; the end-to-end peak-to-peak rate is the
  shown rate.
- *(b) Decline.* Not met: the shown growth is positive.
- *(c) Acquisitions.* The default pair is central: the purchases ($463.7M a year) deducted for ten years and the total
  growth credited; after year ten the purchases stop with the growth and the business is valued at no growth on owner
  cash before purchases. The organic pair (purchases left out, the filer's core growth of 0.62% a year credited) beside.
  Taco, signed and not closed, is left out of the central figure and valued beside with its price added to net debt;
  Taco files no record, so it is credited at nothing.
- *(d) Working capital.* Inside operating cash flow, every year; no single-event draw tied by the filer to one contract.
- *(e) Growth spending.* The filing gives no maintenance split (Q3); capital spending runs at 1.2 times depreciation and
  is read as mostly maintenance, so the all-spending case is central and the depreciation variant is shown beside.
- *(f) The cap.* The shown growth of all-equity owner cash is **9.08%** a year (2021 to 2025). Carried ten years it would
  be $1,454M on sales of $5,247M (sales carried at their own window growth), 27.7% of sales, against a highest share of
  **19.1%** in any year read on the comparable business (2024; the pre-2018 filings describe a different business and are
  not counted). So the growth carried is cut to the business's own **sales growth over the window, 2.62%** a year (total,
  since the default pair credits the bought growth too). The equity-only rate (7.87%) fails the same test (21.6%) and is
  cut the same way. "what the farm produces is all you’re going to get from the farm" **[M1999-067]**.

**COMPUTATION, the range** (`q7_final_out.txt`; whole business $M; per share on 159.64M shares, net debt $1,514.2M =
total debt $1,606.0M less cash $91.8M at 2026-06-30, no finance leases on the face, operating leases left out):

| case | whole business | per share | expected return at $52.47 |
|---|---|---|---|
| **central, all-equity, default pair, cut to 2.62%** | 7,413 to 9,438 (1.27 to one) | **$36.95 to $49.63** | 4.50% to 5.41% |
| equity-only, default pair, cut (against market value) | 6,004 to 7,703 | $37.61 to $48.25 | 4.40% to 5.28% |
| beside: all-equity, default pair, uncut 9.08% (literal) | 7,413 to 16,816 (2.27 to one) | $36.95 to $95.85 | 4.50% to 8.04% |
| beside: Taco added to net debt, credited at nothing | 7,413 to 9,438 | $28.03 to $40.71 | 4.05% to 4.89% |
| beside: organic pair, all-equity (core 0.62%) | 10,892 to 11,441 | $58.74 to $62.18 | 6.17% to 6.47% |
| beside: organic pair, equity-only | 9,483 to 9,961 | $59.40 to $62.40 | 6.34% to 6.65% |
| beside: organic pair, depreciation for capital spending | 11,177 to 11,740 | $60.53 to $64.06 | 6.33% to 6.64% |
| beside: seven years 2019 to 2025, purchases deducted, sales growth 5.92% | 7,036 to 11,955 | $34.59 to $65.40 | 4.28% to 6.43% |
| bound only, no convention allows it: best year's cash ($778M), no purchases, total sales growth | 13,893 to 17,109 | $77.54 to $97.69 | 7.87% to 9.44% |

**The floor is tested first** (Q7, CONVENTION adopted 2026-10-10). The floor is about ten percent pre-tax on what is
paid, applied to owner cash after the company's own tax **[M2003-149]**. At $52.47 the expected return on the central
range is 4.50% to 5.41%; on every case beside it, 4.05% to 8.04%; and even the bound that takes the best year's cash,
charges nothing for the purchases that bought its growth and credits that growth, which (c) forbids, reaches 9.44%. **No
case earns the floor at the price.** "we don’t want to buy equities where our real expectancy is below 10 percent"
**[M2003-149]**; "there’s just a point at which we drop out of the game" **[M2003-149]**. The price also sits above the top
of the central range ($49.63), which closes OUT through the same floor convention; the width (1.27 to one) never comes
into it. The Treasury itself pays 5.60%.

**How sure** **[M1999-104]** is not what decides it, but it points the same way: the trailing twelve months' owner cash is
below FY2025's, the filer guides 2026 sales down 4% to 7% (Q2 release), and the base year of the window was itself loaded
(Q2, Q5); "I paid too much, in relation to average earnings" **[M2021-039]** is the mistake a peak base invites, and the
window's average already includes the two peak years.

**What the deal would do** (specific (c), signed not closed): with the $1.425B added to net debt and Taco credited at
nothing for want of a filed record, the central range falls to $28.03 to $40.71 a share; Taco's earnings would have to be
about $142M a year of owner cash after tax, at no growth, merely to return its price at the ten percent floor, and none
are on the record.

**The two reporting figures** (Part VII, The owner's price and How the fair price is computed; a reporting convention, not
a verdict, no entry language):
- **(a) VALUE RANGE: $36.95 to $49.63 a share** (central, all-equity, default pair, growth cut by (f) to the 2.62% sales
  growth; equity-only $37.61 to $48.25); the literal window uncut gives $36.95 to $95.85, shown beside; against **$52.47**.
- **(b) FAIR PRICE: $13.43 a share on the all-equity basis** (each end of the central range valued at ten percent,
  $3,250M and $4,065M, averaged, less net debt of $1,514M); **equity-only $17.49** (each end of the equity-only range at
  ten percent against the market value). Owner cash after the company's own tax (effective rate 14.1% in 2025, 13.0% in
  2024), no conversion. The low rate is structural, not a shelter that runs out: the FY2025 reconciliation takes the
  25.0% U.K. statutory rate down by 9.7 points for the Swiss rate difference and 3.1 points for partnership impacts, with
  no line for carryforwards used; the $3,016.5M of tax loss carryforwards (a $716.0M valuation allowance against them,
  part expiring from 2026) do not appear as a driver of the rate, so the statutory-rate convention of Q7 (Whose tax) is
  not triggered (10-K FY2025, income tax note). On the organic pair, beside:
  $29.54 all-equity, $33.98 equity-only. With Taco added to net debt: $4.50.

**VERDICT Q7: OUT.** Valued, but the price does not clear the floor on any case the analyst could defend, and it sits
above the top of the central range **[M2003-149]**, **[L2013-012]**; growth was cut to what the business produces
**[M1999-067]**, and the purchases that bought the growth were charged for it **[M1998-080]**, **[L2000-023]**. The range is
narrow, so this is not TOO HARD: the cash can be estimated, and at the price it earns less than the floor. Q8 to Q10 and
Q12 are NOT REACHED; what was found for them is under AFTER THE STOP.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED** (Q7 closed the file OUT). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.**

---
## THE BOX
**OUT, at Q7** (the floor: at $52.47 no case in the range earns about ten percent; the central case returns 4.50% to
5.41%, below even the 5.60% Treasury). **Range $36.95 to $49.63 a share** (all-equity, default pair, growth cut by (f) to
the 2.62% sales growth; equity-only $37.61 to $48.25) **against $52.47** (close 2026-10-09). Fair price, a reporting figure:
$13.43 all-equity, $17.49 equity-only. Q1 IN, Q2 IN, Q3 weighs for, Q4 weighs against (no STOP), Q5 integrity IN with
ability weighing against, Q6 weighs against. Q5 was answered, so no integrity flag is carried.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box is unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the alternatives).** The 30-year Treasury paid 5.60% on 2026-10-09 (Step 0). At $52.47 the expected return on
  the central range is 4.50% to 5.41%, on the organic pair 6.17% to 6.65% and on the uncut literal top 8.04%
  (`q7_final_out.txt`).
- **Q9 (the target's debt).** Total debt $1,606.0M and cash $91.8M at 2026-06-30 (10-Q `0000077360-26-000045`); about
  $1.4B of new debt to come for Taco: a $400.0M tranche 1 term loan maturing 18 months after the closing and a $1.0B
  tranche 2 maturing 2030-05-05, with a $1.4B bridge commitment behind them (8-K `0001104659-26-104725`; 10-Q note 16),
  so total debt of about $3.0B against the window's average all-equity owner cash of $610M. Covenants: debt to the
  credit agreement's EBITDA not above 3.75 to 1 (4.25 for four quarters after a material acquisition) and that EBITDA
  at least 3.0 times interest (10-K FY2025, liquidity); the filer's own 2026 EBITDA guide is about $1,050M (8-K
  `0000077360-26-000039`). A new $500M term loan and revolver drawings were taken in May 2026 (8-K
  `0001104659-26-056228`); net interest expense $39.5M in H1 2026 (10-Q). One customer, Pool Corporation, took 18% of
  consolidated sales in 2025 (Q2, test 6).
- **Q10, Q12.** Nothing found that bears on them; pool and water equipment is not among the businesses Q12 names.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 24b63333); written question by question. Committed after each
      question, with two exceptions: Q3 and Q4 went in one commit (0dc9b503, the first session), and Q6 went with Q7
      (5d69eb1f), as the brief asks, because Q6's buyback test needs Q7's bottom.
- [x] Dispatched: the brief allowed per-question pathspec commits of the two paths only, and every commit here used
      them. The lock is the dispatcher's (operator rule ten); this session did not open it. The fold is the dispatcher's.
- [x] The blind rule. No other run file, holding review, register, reading list, resume state or `PORTFOLIO.md` was
      opened, listed or searched by either session. **Contamination added by the resuming session:** (a) the session
      context's git status listed file names in other research folders (AYI 2026-09-26, BDC, ARCB 2026-09-27) and the
      daily digest files; (b) the five latest commit subjects named the fair-price alert restatement, the operator's
      sheet added to the order, and an OTIS fold with its box and figures; (c) the memory index carried queue counts;
      (d) to apply the 2026-10-10 amendments exactly, the session read sections A to E of the adopted case
      `Framework/v5/CASE 2026-10-10 - seven gaps found by the v5 re-runs, for the operator's approval.md` (its DECIDED
      block shows all seven sections approved), which names other runs (ACLS, AVGO, BMI, CHD, KLAC, NDSN, MA, ORLY, JKHY,
      ECL, EFX, AME, ESI, CMG, EPAC, CTAS, CB) and how each met a gap. None of it concerns Pentair and none of it is used.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check_quotes.py`: no E-ids; ids and
      fragments checked). **One misquote corrected before completion:** the first session's Q5 quoted **[M1994-008]** as
      "how well that they treat the shareholders"; the row has "owners" where that has "the shareholders", and the text
      now follows the row. Every filing fact carries its accession or names its filing.
- [x] The order was kept: Q7 is the first STOP that failed and closed the file; Q8 to Q12 are NOT REACHED and nothing
      after Q7 is a clearance.
- [x] Owner cash is operating cash flow less stock pay less capital spending (all-equity adds back cash interest after
      the company's rate), never a net-income proxy (operator rule 5); the sovereign is the Treasury's par yield; the
      price and the year-end prices of the retention test are Yahoo quotes, aggregator, flagged.
- [x] Contrary evidence was written down as found (foundations list; Q6 and Q7 add the fixed-sum buybacks above the
      range and Taco's missing record). The facts for later questions are under AFTER THE STOP.
- [x] No anchor date: not a point-in-time run.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` run before the final commit (result in the commit message).
- **The record as left.** The run file carries the Q4 heading twice: the answered section and, after it, a second Q4
  heading with "(pending)" left by the first session. The brief asked that the record be left as it is; it is.
- **The price.** The first session's close of 2026-10-09, $52.47, is kept: 2026-10-10 is a Saturday, and a re-quote
  through `tools/sources.py` returned the same close.
- **The Q7 draft.** `q7.py` and `q7_out.txt` were the first session's uncommitted draft; they are committed as its
  record and not used, since they predate the 2026-10-10 amendments to (c) and (f) and the floor-first rule.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Specific (c) as amended on 2026-10-10 says the acquisition spending stops "after year ten, when growth stops", but does not
say what the no-growth end of the default pair charges in years one to ten. Read literally, that end deducts $464M a year
of purchases for ten years and credits no growth for them, which is the thing the amendment's own rationale ("a business
that buys no growth spends nothing to buy it") refuses after year ten. The other reading values the no-growth end at owner
cash before purchases, $58.74 a share, above the growth end ($49.63): the inversion specific (e) calls the finding. The run
took the literal text and showed the other reading beside; the box does not turn on it, since no case earns the floor at
the price either way, but the bottom of the range and the fair price do. Second, specific (f) tests the cap against "the
highest share of sales the business has earned in the filings read"; the filings read here include 10-Ks of a different
business (before the 2017 sale and the 2018 spin), and the text does not say whether those count. The run used only the
comparable years, 2019 to 2025. It also gives no rule for projecting sales in the test; the run carried the window's
average sales at the window's own sales growth. Third, specific (a) measures growth "between the averages of successive
cycles", which cannot be done where the comparable history holds one cycle; the run used the peak-to-peak rate between
the end years and let (f) cut it. Fourth, Q6's buyback test sets the prices paid against "the bottom of the Q7 range",
which is today's range, while the prices were paid in earlier years on an earlier record; the text does not say whether
the range should be the one the record supported when the shares were bought. Fifth, the retention test does not say
whether the market leg ends at the last year-end or at the price date; here the two give opposite answers, and both are
reported.
