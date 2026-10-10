# Company Run — Pentair plc (NYSE: PNR) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

*Dispatched blind run under `Screens/_daily/_dispatch_brief.md`. Copied from the template before any fetch (commit
24b63333). Working folder `Test Runs/_research 2026-10-10 PNR/` (notes in `_notes.md`, scripts `fetch.py`, `comp.py`,
`ids.py`, `q7.py`, `check_quotes.py`; raw filings in the ignored `cache/`).*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

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
are how well they run the business, read against "the hand they were dealt", and "how well that they treat the
shareholders" **[M1994-008]**.

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
*(pending)*

## Q7 — WHAT IS IT WORTH? STOP.
*(pending)*

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
*(pending)*

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
*(pending)*

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
*(pending)*

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
*(pending)*

---
## THE BOX
*(pending)*

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(pending)*

## SELF-AUDIT
*(pending)*

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
*(pending)*
