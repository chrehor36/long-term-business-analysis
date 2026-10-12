# Company Run — RPM International Inc. (NYSE: RPM) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under the canonical brief `Screens/_daily/_dispatch_brief.md`. Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Copied from the template before any fetch (commit acc64c21).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold (overnight cycle, 2026-10-10), after the run was committed: **not held**; `PORTFOLIO.md` carries RPM only as a row of the ranked opportunity set from the v4.1 run of 2026-08-31, in no account.*

**CONTAMINATION, declared as found (the blind rule):**
- The session's opening git status listed other files by name only, not opened: `Test Runs/2026-10-10 Run - OTIS Otis
  Worldwide.md`, `Test Runs/2026-10-10 Run - PNR Pentair.md`, research files under `Test Runs/_research 2026-09-26 AYI/`
  and `Test Runs/_research 2026-09-27 ARCB/`. Not opened, not used.
- The same opening context showed five recent commit subjects of other names' runs (MA, MSA, NDSN, ORLY: each "OUT at Q7 on
  price", with alert prices). Read in passing, not used; none is about RPM or its industry's castle.
- The session's memory index carried one line on the queue state (a count of gate-clearers and "nothing buyable", and that
  holding reviews are owed). It names no company. Not used; it does not tell me whether anyone holds RPM.
- The lock file `Screens/_daily/_overnight.lock` was read to confirm the dispatcher holds it; its one line reads
  "interactive v5 re-runs batch 9". It tells me this may be a re-run; it says nothing of any earlier RPM verdict. Not used.
- The dispatching message says earlier run files about RPM exist. None was opened, listed or searched; `Test Runs/` was never
  listed.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $97.73 (close 2026-10-09, as printed by `python tools/run.py RPM`; **aggregator, live quote only, flagged** per
  operator rule 5).
- **Shares by class** from the latest filing's cover: 127,533,690 common shares, single class (Form 10-Q for the quarter ended
  2026-08-31, filed 2026-10-06, accession `0001193125-26-415321`; `python Screens/cover_shares.py RPM`). Check: the 10-Q
  balance sheet states 146,910 thousand issued and 127,554 thousand outstanding at 2026-08-31 (treasury 19,356 thousand), so
  issued less treasury agrees with the cover within the month's net buyback (the 10-Q equity statement shows 196 thousand
  shares repurchased in the quarter). No 8-K or prospectus after the 10-Q issues shares (the 8-K of 2026-10-06,
  `0001193125-26-414916`, is the quarter's results only).
- **Market cap:** 127.534M x $97.73 = **$12,464M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, US Treasury daily par yield curve, 30-year, 2026-10-09
  (`python tools/sources.py`). Earnings currency: USD (about 70% of sales in the United States; 10-K FY2026, Item 1).
- **Filings read** (operator rule 4):
  - 10-K for FY2026 (year ended 2026-05-31), filed 2026-07-22, accession `0001193125-26-312142`.
  - 10-Q for the quarter ended 2026-08-31, filed 2026-10-06, accession `0001193125-26-415321`.
  - Proxy (DEF 14A), filed 2026-08-25, accession `0001193125-26-365259`.
  - 8-Ks of 2026: `0001193125-26-414916` (Q1 FY2027 results), `0001193125-26-311276` (FY2026 results; a President and COO
    named 2026-07-17), `0001193125-26-253577` (receivables facility amended), `0001193125-26-173804` (a director added),
    `0001193125-26-094139` (revolver extended to 2031; interest-coverage covenant removed, leverage covenant 3.75x kept).
  - 10-Ks FY2020 to FY2025 (`0001564590-20-033611`, `0001564590-21-037949`, `0000950170-22-012972`, `0000950170-23-034640`,
    `0000950170-24-086386`, `0000950170-25-098313`), and the FY2016 to FY2019 10-Ks with their Exhibit 13 annual reports,
    which carry the statements in those years (`0001564590-16-021706`, `0001564590-17-013863`, `0001564590-18-017180`,
    `0001564590-19-025795`).
  - **One figure cross-checked against the filed statement:** cash provided by operating activities FY2026, $898,708 thousand
    in the filed Consolidated Statement of Cash Flows (10-K FY2026), against $898.7M in the XBRL series `tools/run.py` reads.
    Agrees.
- `python tools/run.py RPM`, arithmetic lines only (Part VII: nothing it prints as a rule, id or verdict is used). As filed,
  USD millions, OCF less stock pay less capital spending: FY2024 882, FY2025 511, FY2026 642 (three-year mean 679); the
  five-year mean on the same basis is 449. Depreciation and amortization FY2026 213.5 (depreciation 165.4, amortization of
  intangibles 45.8, per XBRL). Stock pay is in every year (FY2026 $32.8M). The tool found no securities, other stock-pay,
  intangible or software lines beside capital spending. The full ten-year owner-cash table is built from the filed statements
  at Q4 below.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the one on the analyst's habits: RPM is a long-lived, well-known, steady-dividend
industrial, the kind of name an analyst wants to clear, so the run looks first for "what’s wrong" and "what you’re missing"
**[M2025-013]**, and asks "And then what?" of each claim the company makes about itself **[M1997-110]**. A share is a business
**[M1997-109]**: the question is whether I would be content to own these roofing, sealant, coating and DIY businesses if the
market closed. No macro view enters **[M2000-094]**; the raw-material and tariff headwinds the 10-K names for FY2027 are read
only as a property of the business (can it price through them), never as a forecast. Who is paid to tell me: the company's
own featured figure is "adjusted EBIT", and its incentive pay is set on it (proxy, `0001193125-26-365259`), so the reported
GAAP and cash figures are used and the adjusted ones are not **[M2020-037]**.
**Contrary evidence, written down as found** **[M1997-127]**:
1. The construction side (Industrial to FY2019, CPG and PCG after) earned about 10% pretax on sales for thirteen years
   (FY2008 to FY2020); the higher margins of FY2022 to FY2026 are the product of two restructuring programmes and have not
   met a construction downturn.
2. Consumer's organic sales fell in four of the last five fiscal years (FY2022, FY2024, FY2025, FY2026), price included; its
   ten largest customers took 64% to 68% of Consumer sales in every year shown from FY2014 to FY2025, and one customer took
   20% to 23% in FY2024 to FY2026.
3. Restructuring charges appear in every year from FY2018 to FY2026 (the "one-time" that recurs).
4. The SEC sued the company and its General Counsel in 2016 over the timing of the disclosure and accrual of a DOJ and GSA
   matter in FY2013 (a restatement of three quarters); settled in December 2020 with a $2.0M penalty and an injunction,
   neither admitted nor denied. The General Counsel stayed in office until 2024.
5. A jury in 2024 found a Consumer subsidiary liable to a former supplier for breach, trade-secret misappropriation and
   fraud, $190.0M with punitive damages; judgment entered at $110.8M plus interest; the company accrues the low end
   ($0.5M) of a $0.5M to $152.5M range and is appealing.
6. Working capital is heavy: receivables and inventory were about 35% of sales at FY2026 year-end.

## THE STANDING RULE
Nothing in this run finances, sizes or holds a position; the run is an analysis. A buyer of RPM shares with his own money,
unlevered and sized so that a halving of the quote changes nothing he needs, risks nothing he has and needs **[M2012-081]**,
**[L2023-005]**. The rule binds the buyer's conduct, not the target's; RPM's own debt is weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look like
in five or 10 years" **[M2012-065]**; the chemistry need not be understood if "the economic dynamics of the industry" are
**[M2011-014]**.

**What the business is** (10-K FY2026, `0001193125-26-312142`, Item 1): specialty coatings, sealants, roofing systems,
concrete admixtures, polymer flooring, corrosion-control coatings and DIY paints, caulks and cleaners, sold in about 167
countries; net sales $7.86B; about 70% United States. Three reportable segments since 2026-06-01 (the brief's list of four,
with Specialty, is out of date: the Specialty Products Group was dissolved into the other three on 2025-06-01 and its history
recast): CPG, construction products, about 39% of sales; PCG, performance coatings, about 27%; Consumer, about 34%.

**The key variables, and whether they are foreseeable** **[M1998-044]**:
1. Demand from the repair, maintenance and restoration of existing buildings, infrastructure and homes. The filer: "re-roofing
   applications have historically accounted for over three-quarters of U.S. demand" (Item 1, Roofing Systems Products). Slow-moving
   and need-driven; foreseeable in direction, not in year.
2. Price against raw materials, "many of our raw materials are petroleum-based derivatives, minerals and metals" (Item 1, Raw
   Materials). The record of two inflations (FY2017 to FY2019, FY2021 to FY2023) is in the filings and is read at Q2.
3. The big-box channel's power over Consumer (point 2 of the contrary evidence above).
4. What the acquisition programme earns on the capital it consumes (cash paid for businesses FY2015 to FY2026 is about $2.27B,
   from the filed cash-flow statements; read at Q3 and Q6).
None is a fast-moving technology. The products are formulated chemistry sold into slow, mature, maintenance-driven uses; the
change threat named in the rows **[M1999-063]** is not the nature of this industry. The past statements tell the future ones
in the sense of **[M2008-033]**: eighteen years of segment results (FY2008 to FY2026, read below) show the same pattern of
margins falling in raw-material inflations and recovering, through one recession.

**The parts** (Q1's holding-company paragraph, by Q2's threshold): no segment carries more than half of five-year operating
profit (table under Q2); CPG is the largest and decides. CPG's own economics (roofing restoration, building-envelope
sealants and waterproofing, admixtures, EIFS cladding, insulated concrete forms, restoration equipment) are maintenance and
specification businesses whose dynamics I can state; I do not doubt that it is inside the perimeter **[M2002-092]**. Would the
insiders write down a ten-year forecast of these product lines' economics? The filer writes its own description of the field
("Barriers to market entry are relatively high ... the importance of brand identity and the difficulty in establishing a
reputation as a reliable supplier", Item 1, Competition), which is the kind of statement the tech insiders of **[M2000-105]**
would not make.

**Doubts carried, not closing:** RPM is a collection of well over a hundred brands built by acquisition; the run reads it by
its three parts and not brand by brand, which is the CONVENTION of Q1's holding-company paragraph, with **[M2023-031]** open
against it.

**VERDICT: IN.** The key variables are important and knowable **[M2006-076]**, and none rests on fast technology
**[M1999-063]**.


## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]** A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

### The parts table (CONVENTION of Q2, a business of parts; "lumping them together [...] impedes analysis" **[L2008-005]**)
Segment income before income taxes, USD millions, as the filer reports each segment (corporate/other expense is held outside
the segments). The structure changed twice in the window, so the vintages are mixed and labelled: FY2022 from the 10-K FY2023
(`0000950170-23-034640`, four segments); FY2023 from the 10-K FY2025 (`0000950170-25-098313`, four segments recast); FY2024
to FY2026 from the 10-K FY2026 (`0001193125-26-312142`, three segments recast). The former SPG's FY2022 and FY2023 profit
(now split among the three) is shown on its own line.

| part | FY22 | FY23 | FY24 | FY25 | FY26 | five-year sum | share | castle | decides |
|---|---|---|---|---|---|---|---|---|---|
| CPG (roofing, sealants, waterproofing, admixtures, cladding) | 396.5 (a) | 301.0 | 388.3 | 425.1 | 448.3 | 1,959.2 | 39.6% | stands (below) | **yes, the largest** |
| Consumer (Rust-Oleum, DAP, Zinsser, cleaners) | 175.1 | 378.2 | 403.2 | 332.8 | 362.4 | 1,651.7 | 33.4% | under pressure, not shown open | no |
| PCG (Stonhard flooring, Carboline coatings, FRP) | 139.1 | 142.5 | 245.8 | 278.0 | 309.0 | 1,114.4 | 22.5% | not judged (does not decide) | no |
| former SPG (FY22 and FY23 only) | 121.9 | 103.3 | n/a | n/a | n/a | 225.2 | 4.5% | n/a | no |

(a) FY2022 CPG includes a $41.9M gain on the sale of real property (10-K FY2023, MD&A); without it 354.6.
No part carries more than half; CPG is the largest even if all of the former SPG were added to Consumer (1,876.9 against
1,959.2). **CPG decides.**

### CPG's record over the span (segment income before taxes over segment sales)
The construction side was reported as "Industrial" to FY2019 (it held what is now CPG and PCG); CPG alone from FY2019 on.
- Industrial, EBIT over sales: FY2008 10.9%, FY2009 7.6%, FY2010 9.8% (annual report FY2010, Exhibit 13 to
  `0000950123-10-069889`); FY2011 10.4%, FY2012 11.1%, FY2013 6.6% (Exhibit 13 to `0001193125-13-300693`); FY2014 9.9%,
  FY2015 10.1%, FY2016 10.6% (Exhibit 13 to `0001564590-16-021706`); FY2017 9.5%, FY2018 9.6%, FY2019 8.4% (Exhibit 13 to
  `0001564590-19-025795`).
- CPG: FY2019 9.4%, FY2020 11.2%, FY2021 14.1% (10-K FY2021, `0001564590-21-037949`); FY2022 15.9% (14.3% without the
  property gain); FY2023 12.0%; FY2024 13.7%; FY2025 14.8%; FY2026 14.6% (10-K FY2026, recast).
So: about 10% for thirteen years, through the 2009 trough (7.6% at the bottom, never a loss), then about 14% to 15% from
FY2021 under the two restructuring programmes (MAP to Growth from 2018, MAP 2025 from August 2022).

### The castle tests, applied to CPG, with the filing fact for each
1. **What keeps it standing, and how permanent** **[M1995-038]**. Re-roofing is "over three-quarters of U.S. demand" (Item 1);
   CPG sells restoration systems backed by a "whole building warranty" and turnkey service through its own contracting
   subsidiary (10-K FY2025, Item 1; 10-K FY2026, Item 1); the filer credits CPG's FY2025 organic growth to "its restoration
   project focus, direct sales model, and high growth in the service business" (10-K FY2025, MD&A). The reason the customer
   comes is a roof that must be kept dry and a warranty that must be honoured, on buildings already standing; that reason
   does not move with fashion or technology.
2. **Would it stand without the lord.** No superstar: CPG is run by group presidents who now report to a newly named COO
   (8-K `0001193125-26-311276`); its results held through three changes of segment structure.
3. **The money test** **[M2011-015]**. Against: the filer says that "Several of our competitors have access to greater financial
   resources and larger sales organizations than we do" (Item 1, Competition), and the field has large, funded consolidators
   (below). For: the filer's account of the barrier, "Barriers to market entry are relatively high for new market entrants due
   to the lengthy intervals between product development and market acceptance, the importance of brand identity and the
   difficulty in establishing a reputation as a reliable supplier of these products" (Item 1); and in roofing it says it
   competes "primarily for the higher-end, multi-ply and modified bitumen applications in the built-up and low-slope roofing industry", while the largest roofing manufacturers
   compete "mainly on price and, to a lesser degree, service" (10-K FY2016, `0001564590-16-021706`, Item 1). A rival with
   money can buy share in single-ply; it cannot quickly buy decades of specifications and honoured warranties.
4. **Pricing power and the agony** **[M2005-020]**; "over time the businesses with strong competitive positions manage to pass
   through increases in raw material costs" **[M2005-017]**. Through the last inflation CPG's margin was 14.1% (FY2021),
   14.3% (FY2022 without the gain), 12.0% (FY2023), 13.7% (FY2024): a dip of about two points, recovered within two years.
   The filer for FY2023: CPG growth helped by "Improved pricing in response to continued cost inflation" (10-K FY2023, MD&A).
   Consolidated gross margin fell from 39.4% (FY2021) to 36.3% (FY2022) and stood at 41.4% in FY2026 (10-Ks FY2022 and
   FY2026, MD&A). Price passed through with a lag: agony, measured, not a prayer session.
5. **Unit volume.** CPG organic growth (price and volume, the filer's measure): FY2021 9.5%, FY2022 19.3%, FY2023 6.8%,
   FY2024 6.6%, FY2025 3.4%, FY2026 4.5% (10-Ks FY2021 to FY2026, MD&A tables). Positive in every year shown; the filer does
   not split price from volume.
6. **Low cost.** No filing evidence either way. Not claimed.
7. **The brand.** Tremco, founded 1928; nearly 800 registrations and applications cover the Tremco brand family (Item 1,
   Intellectual Property). A specification brand, asked for by the architect and the roof consultant, not by the public.
8. **The low bid** **[M2017-009]**. The higher-end multi-ply niche of test 3 is where the low bid is not the rule (10-K FY2016).
   Concrete admixtures, inside CPG, sit closer to a bid business against larger rivals; the filer claims share gains there in
   FY2023 (MD&A), its own claim.
9. **Ask the competitors** **[M1998-145]**. Not done: no scuttlebutt is on the public record for this run. Recorded as a gap.
10. **Widening or narrowing** **[M1999-108]**. The margin rose by four to five points after FY2020. Under Q2's CONVENTION a
    change for the better is credited only on a full cycle in which the price behaviour held; one inflation has been passed,
    no construction downturn has. **The improvement is not credited here**; it is carried to Q7 as the question of which base
    to use. The castle does not need it: the thirteen years before it already show a standing, profitable franchise.
11. **What could destroy or reduce it** **[M2000-014]**. A funded single-ply rival moving up into restoration; a product failure
    across many roofs or walls (the company runs captive insurers for product liability and keeps warranty reserves, 10-K
    FY2026 Note P); exclusion from public-sector work (the FY2013 GSA matter arose in Tremco Roofing's government contracts).
    None is shown happening in the filings.

### The competitor row (each filer's own XBRL facts, 10-K annual values; research file `peers_table.txt`)
Metric: income before income taxes plus interest expense, over revenue. Ten fiscal years (RPM FY2017 to FY2026, years ending
in May; the others calendar or near-calendar 2016 to 2025, so offset by about five months).

| filer | range over the ten years | mean | accession of the latest revenue fact |
|---|---|---|---|
| RPM | 6.9% to 12.5% | 10.4% | `0001193125-26-312142` |
| Sherwin-Williams (SHW) | 9.8% to 16.7% | 14.0% | `0000089800-26-000008` |
| PPG (PPG) | 6.7% to 14.4% | 11.4% | `0000079879-26-000046` |
| Axalta (AXTA) | 6.5% to 14.1% | 9.9% | `0001628280-26-008008` |
| H.B. Fuller (FUL) | 4.4% to 10.5% | 8.8% | `0001437749-26-001767` |
| Carlisle (CSL) | 9.5% to 23.7% | 15.2% | `0000790051-26-000012` |

Carlisle was a conglomerate until its divestitures of 2021 to 2023; its 2023 to 2025 figures (21.9%, 23.7%, 20.5%) are its
construction-materials business nearly alone and are the closest filed comparison for CPG's roofing. CPG's segment margin of
about 15% is before about three points of RPM corporate cost (corporate/other expense $249.5M on $7,863.4M of sales in FY2026),
so CPG earns less on sales than Carlisle's roofing does. **Not SEC filers, flagged:** Sika (Switzerland; sealants, roofing,
admixtures), Holcim's building-envelope arm (roofing), Saint-Gobain (owner of GCP's admixtures since 2022), Henkel, Soprema.
Their filings are not read; their size is why test 3 cuts against.

### The field's returns over the last full cycle, judged in words
On sales, RPM sits in the middle of the field: below Sherwin-Williams and Carlisle, near PPG and Axalta, above H.B. Fuller.
On capital, which is what the moat protects **[L2007-004]**, judged on the capital the business needs and not what was paid
for it **[M2010-090]**, **[M2011-060]**: RPM's income before tax and interest over equity plus net debt less goodwill and
intangibles ran from 23% to 60% in FY2010 to FY2026 (FY2010 40.8%, FY2016 59.6%, FY2019 23.7%, FY2023 27.8%, FY2026 32.5%;
XBRL balance sheets, transcription, script in the research folder notes), and over total capital including the purchased
goodwill from 10.7% to 20.8% (FY2026 17.8%). In the year after the 2009 trough the total-capital figure was 17.5% (FY2010).
These are not ordinary returns on the capital the business needs; the durable filers of the field (Sherwin-Williams, PPG,
Carlisle) also earn well; this is not a field where "you can have only two competitors and they’re still terrible
businesses" **[M2013-052]**.

### Consumer, the second part (does not decide; carried)
Consumer's margin (segment income before taxes over sales) fell from 15.5% (FY2021) to 7.8% (FY2022), the filer citing
"inflation, and the unfavorable impact of supply chain shortages on production" (10-K FY2022, MD&A), and recovered to 15.0% in
FY2023 with "improved pricing to catch up with continued cost inflation" and a $20.0M insurance gain (10-K FY2023, MD&A); it
fell in the earlier inflation too (16.4% in FY2016 to 9.8% in FY2018). Its organic sales fell in four of five years to FY2026.
This is the battle between brand and retailer that the rows name **[M2001-090]**, **[M2019-041]**: Rust-Oleum and DAP are
strong brands, but their price is negotiated with a handful of retailers who take about two-thirds of the segment's sales.
The castle is under pressure, not shown open: the segment earned 13% to 17% of sales in the normal years FY2014 to FY2016,
FY2021 and FY2023 to FY2025. It is carried as a doubt to Q7, not as an open part valued at no growth.

**VERDICT: IN.** The deciding part's castle stands on the evidence of a full cycle: profitable through the 2009 trough, price
passed through the last inflation within two years, and returns on the capital the business needs well above ordinary
**[M2011-060]**, **[M2005-017]**. Not a great castle: its margin trails the best roofing filer, its funded rivals are larger,
much of Consumer's brand power sits with the retailer, and the recent margin gain is not credited **[M2017-026]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The rows: "we always look at what a business does in terms of what it earns on capital" **[M1998-005]**; earnings on net
tangible assets are "the way to measure profitability overall" **[M2014-007]**; growth is good or bad according to "what we
earn on that incremental $130 million over time" **[M2001-019]**. All figures below are from RPM's XBRL facts (10-K annual
values, May year-ends) with the arithmetic in `capital.py` and its output `capital_out.txt` in the research folder.

**1. What it earns on the capital it needs.** Income before tax and interest over equity plus net debt less goodwill and
intangibles: 40.8% (FY2010), 59.6% (FY2016), 23.4% (FY2017), 23.7% (FY2019), 39.6% (FY2021), 27.8% (FY2023), 32.5% (FY2026).
Over total capital including purchased goodwill: 17.5%, 20.8%, 10.7%, 11.9%, 19.4%, 16.7%, 17.8% in the same years. The
tangible figure is high in every year of the span. It is read with the cautions of **[L1994-009]** in mind: not a cyclical peak
(it held through the 2009 trough and the 2022 inflation), not a monopoly, and not leverage (it is computed before interest on
capital that includes the debt).

**2. What must go back in to stand still, and to grow.** The filer states no maintenance figure; it says its capital expenditures
"facilitate our continued growth, allow us to achieve production and distribution efficiencies, expand capacity" and more
(10-K FY2026, MD&A, Investing Activities). So the maintenance need is my guess, disclosed as one **[M2000-144]**: depreciation,
the proxy the rows call "not inappropriate in most companies" **[M1998-127]**, $165.4M in FY2026, against capital spending of
$223.5M. Capital spending ran 1.35 to 2.35 times depreciation in every year FY2012 to FY2026 (2.13 and 2.35 in FY2022 and
FY2023, the MAP 2025 plant consolidations). Working capital is the heavier claim: receivables plus inventory less payables
was 21% to 27.5% of sales across FY2010 to FY2026 (23.7% in FY2026), so each added dollar of sales ties up about 24 cents
before any plant is built **[M2008-036]**.

**3. The growth arithmetic.** Sales rose from $4,813.6M (FY2016) to $7,863.4M (FY2026), about 5.0% a year compounded; cash paid
for acquisitions in FY2017 to FY2026 was about $1.75B (filed cash-flow statements: 254.2, 112.4, 168.2, 65.1, 165.2, 127.5, 47.5,
15.5, 595.8, 202.4). Organic growth as the filer reports it (price and volume, consolidated): FY2021 8.1%, FY2022 8.9%, FY2023
10.1%, FY2024 1.3%, FY2025 0.8%, FY2026 2.0%, the large years being the inflation's price. What the added capital earned:
averaging FY2015 to FY2017 against FY2024 to FY2026, income before tax and interest rose from $485.7M to $925.7M (+$440.0M) while
total capital rose from $2,904.7M to $5,054.7M (+$2,150.0M), about 20% pretax on the added capital. Book capital understates
what went in: about $244M of goodwill and intangible write-downs (FY2017 $193.2M, FY2023 $39.2M, FY2025 $11.4M) and $123.6M of
asbestos trust payments in FY2018 left the books; added back, the incremental return is about 17% to 18% pretax.

**4. The second-best business.** RPM is not the first kind of business, "more and more money every year without putting up
anything to get it" **[M1998-081]**; it is the second kind, whose growth "takes more money, but the rate at which you invest
[...] the money to get that growth is a very satisfactory rate" **[M1998-081]**, and the 2009 letter's test is met, "decent returns
on the incremental sums they invest" **[L2009-012]**. Against it: the growth needs working capital and acquisitions in about
equal measure with plant, and depreciation alone does not hold the place (spending above it in every year for fifteen years)
**[L2000-035]**.

**WEIGHS FOR, modestly.** High returns on the tangible capital the business needs and decent returns on the capital added,
including what was paid for acquisitions **[M2011-060]**; a capital-hungry second-best business, not a See's **[M1998-081]**.
(The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten year-ends, before the income account** **[M2025-032]** (`tools/run.py` table, first-filed XBRL
vintage, read against the filed statements of the 10-Ks listed in Step 0; USD millions):

| May 31 | assets | equity | cash | receivables | inventory | goodwill | intangibles | retained | debt |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 5,090 | 1,436 | 350 | 995 | 788 | 1,144 | 573 | 1,172 | 2,090 |
| 2018 | 5,272 | 1,631 | 244 | 1,114 | 834 | 1,192 | 584 | 1,343 | 2,174 |
| 2019 | 5,441 | 1,406 | 223 | 1,232 | 842 | 1,246 | 601 | 1,425 | 2,526 |
| 2020 | 5,631 | 1,262 | 233 | 1,138 | 810 | 1,250 | 584 | 1,544 | 2,539 |
| 2021 | 6,253 | 1,741 | 247 | 1,281 | 938 | 1,346 | 629 | 1,852 | 2,380 |
| 2022 | 6,708 | 1,982 | 202 | 1,433 | 1,213 | 1,338 | 592 | 2,139 | 2,687 |
| 2023 | 6,782 | 2,141 | 216 | 1,503 | 1,135 | 1,294 | 555 | 2,404 | 2,684 |
| 2024 | 6,587 | 2,511 | 237 | 1,419 | 956 | 1,309 | 513 | 2,761 | 2,127 |
| 2025 | 7,776 | 2,885 | 302 | 1,509 | 1,036 | 1,618 | 781 | 3,194 | 2,647 |
| 2026 | 8,345 | 3,312 | 315 | 1,662 | 1,059 | 1,688 | 825 | 3,583 | 2,534 |

**What moved, and why.** Equity more than doubled (1,436 to 3,312) while goodwill and intangibles rose from 1,717 to 2,513, so
tangible equity turned from negative (−281 in FY2017) to positive (+799 in FY2026); the equity of FY2019 to FY2020 was held
down by buybacks ($325M in those two years) and by pension and currency losses in other comprehensive income. Receivables
moved with sales (20.1% of sales in FY2017, 21.1% in FY2026). Inventory jumped to 18.1% of sales in FY2022 (the filer: raw
material inflation and supply shortages, 10-K FY2022, MD&A) and was worked back to 13.5% by FY2026, releasing $180M of cash in
FY2024 alone. Debt is roughly flat in dollars over the decade (2,090 to 2,534) against more than double the equity. Retained
earnings tripled. Cash is small and stable. **What they do not say:** the balance sheet of a roll-up carries its purchases at
cost; the $1.75B paid for businesses in FY2017 to FY2026 is in goodwill and intangibles, net of $244M written down (FY2017,
FY2023, FY2025). **What they cannot say:** whether the $110.8M judgment (below) will stand.

**Two balance-sheet tells looked at twice** **[M1995-064]**:
1. Prepaid expenses and other current assets rose from $322.6M to $423.2M in FY2026 (+31% against sales +6.7%), and other
   noncurrent assets from $216.0M to $303.0M (10-K FY2026 balance sheet). The filer's contract assets in the first line fell
   ($73.0M to $61.8M, Note Q), and its captive insurers' securities rose about $40M (MD&A, Investing Activities); the rest
   of the rise is not explained in the 10-K I read. The 10-Q shows the current line back down to $405.1M at 2026-08-31.
   Recorded as unexplained, about 1% of assets; not confusion over what the business earns, since operating cash already
   carries it ("(Increase) ... in prepaid expenses and other current and long-term assets (85,596)" in FY2026).
2. Accrued losses: the company carries $0.5M against a judgment entered at $110.8M plus 9% prejudgment interest from 2018
   (range $0.5M to $152.5M), reasoning that affirmance is "not probable" (10-K FY2026, Note P; 10-Q Note 13). The disclosure is
   full and plain; the accrual is the low end that the rules allow when no point in a range is better. It is read with the
   company's history on exactly this kind of accrual (the FY2013 restatement, under Q5).

**The real costs.**
- **Depreciation** is a real cost **[R1996-023]**; capital spending exceeded it every year (Q3).
- **Stock pay** is in every year ($19.8M to $40.9M, FY2017 to FY2026) and is deducted below **[L2015-003]**.
- **Restructuring** appears in every year FY2018 to FY2026: $17.5M, 42.3, 33.1, 18.1, 6.3, 15.5, 30.0, 25.0, 42.6 (XBRL,
  RestructuringCharges), $230M in nine years, and the 10-K FY2026 already speaks of "our next MAP initiative". It is a
  recurring cost of running this collection of businesses, not a one-time item **[L2016-007]**; it is in operating cash and
  stays in owner cash.
- **Asbestos.** The former Bondex/SPHC asbestos liability was settled through a section 524(g) trust; RPM paid $221.6M in FY2015
  and $123.6M in FY2018, shown in financing activities (annual reports FY2017 and FY2018). Before the Q7 window, but a real
  cost of the business's past, counted in the ten-year view below.
- **EBITDA in the filer's own mouth.** From fiscal 2027, "the company’s primary measure of profit and loss has transitioned to
  adjusted earnings before interest, taxes, depreciation and amortization (adjusted EBITDA), from adjusted EBIT", "to better
  reflect underlying profitability during periods of acquisition activity" (press release, 8-K `0001193125-26-311276`, Ex.
  99.1); the FY2027 outlook and the Q1 FY2027 release lead with it (8-K `0001193125-26-414916`, Ex. 99.1). The rows: "References
  to EBITDA make us shudder" **[L2000-036]**; "the number of times we’re going to buy into a company [...] where people are
  talking about EBITDA, is going to be about zero" **[M2002-026]**; "I’ll look at that figure when you tell me you’ll make all
  the capital expenditures" **[M2003-108]**. Before the switch the featured figures were adjusted EBIT and adjusted EPS, with
  "the 16th time we have generated record adjusted EBIT out of the past 18 quarters" (same release), and the company gives
  quarterly and annual outlooks. Under the Q4 CONVENTION of 2026-10-06 these are weighed here against **[L2016-006]**,
  **[L2019-006]**, **[L2002-041]** and carried to Q5.

**Owner cash after every real cost** (operating cash less stock pay less all capital spending; filed cash-flow statements,
USD millions; acquisitions shown separately for Q7's specific (c)):

| FY | operating cash | stock pay | capital spending | owner cash | acquisitions, net of cash | asset and business sales |
|---|---|---|---|---|---|---|
| 2017 | 386.1 | 32.5 | 126.1 | 227.5 | 254.2 | 0.9 |
| 2018 | 390.4 | 25.4 | 114.6 | 250.4 (126.8 after the asbestos trust) | 112.4 | n/a |
| 2019 | 292.9 | 31.2 | 136.8 | 124.9 | 168.2 | n/a |
| 2020 | 549.9 | 19.8 | 147.8 | 382.3 | 65.1 | n/a |
| 2021 | 766.2 | 40.9 | 157.2 | 568.1 | 165.2 | 0 |
| 2022 | 178.7 | 40.1 | 222.4 | −83.8 | 127.5 | 76.6 |
| 2023 | 577.1 | 28.7 | 254.4 | 294.0 | 47.5 | 58.3 |
| 2024 | 1,122.3 | 25.9 | 214.0 | 882.4 | 15.5 | 6.9 |
| 2025 | 768.2 | 27.0 | 229.9 | 511.3 | 595.8 | 0 |
| 2026 | 898.7 | 32.8 | 223.5 | 642.4 | 202.4 | 23.2 |

Five-year mean FY2022 to FY2026: 449.3 (matches `tools/run.py`); three-year 678.7; ten-year 380.0 (367.6 after the FY2018
trust payment). The swing from −83.8 to 882.4 is working capital: the FY2022 inventory build and the FY2024 release. Net
income over the same five years averaged $582M, so owner cash ran at about 77% of reported earnings, the gap being the
growth spending above depreciation and the working capital.

**VERDICT on the accounts: WEIGHS AGAINST; not a STOP.** The accounts are readable and the cash ties to the statements; no
confusion over what the business earns **[M1995-063]**, and the tells found (an unexplained prepaid rise of about 1% of assets,
a low-end accrual fully disclosed) do not rise to suspicion of the accounts themselves **[M1995-065]**. Against: a management
that features adjusted figures, now EBITDA, gives guidance and counts its records **[M1994-018]**, **[M2002-026]**; carried to Q5.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**The people** (proxy `0001193125-26-365259`; 10-K FY2026 executive officers; 8-K `0001193125-26-311276`): Frank C. Sullivan,
Chairman and CEO (a director since 1995, CEO since 2008, son of the former chairman); David C. Dennsteadt, President and COO
from 2026-07-17; Russell L. Gordon, CFO; Tracy D. Crandall, General Counsel and Chief Compliance Officer, "elected [...] in
2024" (10-K FY2026, executive officers). Twelve director nominees, eleven independent, Robert A. Livingston Lead Director
(director since 2017); the board declassified by the 2024 annual meeting. The CEO's brother, Thomas C. Sullivan, Jr., is Vice
President, Corporate Development, and "earned $640,000 in salary and bonus in fiscal 2026" (proxy, Related Person
Transactions). CEO total pay $11,133,668, a pay ratio of 185:1 (proxy, Pay Ratio Disclosure).

### The first yardstick: how well they run it **[M1994-008]**
Sales from $3.4B (FY2010) to $7.9B (FY2026); returns on the tangible capital the business needs high in every year of the span
(Q3); the construction margin raised by about four points since FY2020 under two restructuring programmes (Q2), not yet tested
by a construction downturn. Read against the hand dealt: a mature, fragmented field in which the larger filers (Sherwin-Williams,
Carlisle) earn more on sales (Q2's competitor row). Capital allocation belongs to Q6. **Ability WEIGHS FOR**, with two
reservations: the margin gains are recent, and the "records" the company counts are adjusted figures (Q4).

### The habits carried from Q4, read with the integrity record
"things that they do in public in relation to their investors and the promises they make" **[M2004-067]**: quarterly and annual
outlooks; a featured adjusted figure, adjusted EBIT and now adjusted EBITDA; "the 16th time we have generated record adjusted EBIT
out of the past 18 quarters" (Q4). The rows: of CEOs who "consistently reach their declared targets", "we become downright
incredulous" **[L2002-041]**. To the company's credit, the record does not show targets always made: the three-year PSUs for
June 2023 to May 2026 paid nothing, "each recipient earned 0.0% of the recipient's grant and forfeited 100.0% of such grant", and
the fiscal 2026 PERS grants were awarded "at 44.4% of target" (proxy, CD&A and the outstanding-awards notes). Against that, the
annual cash incentive for fiscal 2026 paid "approximately 130% of their salaries for fiscal 2026 or 120% of target bonus level"
(proxy, CD&A), from a pool set at 1.5% of pre-tax income. The pay plan let the executives miss on the long-term measures; the
habit of the featured adjusted figure and the guidance stands.

### The integrity record, from the primary documents
1. **The DOJ matter.** From 2011 to 2013 RPM and a subsidiary (Tremco Roofing, in its government contracts) were under DOJ
   investigation for overcharging the government; the company expected to pay "approximately $65.1 million" to resolve it
   (annual report FY2013, Exhibit 13 to `0001193125-13-300693`). The SEC's account: "RPM sent DOJ estimates showing RPM's
   subsidiary overcharged the government on the contracts under investigation by a material amount", and "prior to submitting the
   settlement offer to DOJ, RPM's overcharge estimates increased substantially to at least $28 million" (SEC Litigation Release
   No. 23639, 2016-09-09, sec.gov, a primary source; saved in the research folder's cache).
2. **What the General Counsel did not tell.** The SEC alleged that Edward W. Moore, "RPM's General Counsel and Chief Compliance
   Officer, oversaw RPM's response to the DOJ investigation" and "did not inform RPM's CEO, CFO, Audit Committee, and independent
   auditors, of material facts about the investigation" (same release). RPM restated three quarters of FY2013 in August 2014 and
   disclosed a material weakness in internal control for the first two quarters of FY2013 (SEC Litigation Release No. 24994,
   2020-12-23). The audit committee's investigation "concluded that there was no intentional misconduct on the part of any of our
   officers" (10-K FY2016, `0001564590-16-021706`). The Wells notice of 2015 proposed a clawback of the CEO's and CFO's incentive
   pay for the periods before the restatement; "The Staff did not indicate an intention to recommend any charges against either
   of these officers" (10-K FY2016).
3. **How the company answered.** After the SEC sued in 2016 the company said it believed "the allegations in the complaint
   mischaracterize both our and our General Counsel's actions [...] and are without merit" and that it would "contest the
   allegations in the complaint vigorously" (10-K FY2017, `0001564590-17-013863`). On 2020-12-22 it consented to a final judgment,
   a $2.0M penalty and permanent injunctions under the reporting, books-and-records and internal-controls provisions; Moore paid
   $22,500 and was "permanently enjoined from violating the books and records provision of Exchange Act Rule 13b2-1"; both
   "neither admitted nor denied" (10-K FY2021, `0001564590-21-037949`; Litigation Release No. 24994).
4. **What the board did with the man.** Moore remained General Counsel and Chief Compliance Officer, and a named executive
   officer, into fiscal 2025 (proxy 2026, pay-versus-performance notes list him among the non-PEO NEOs for fiscal 2022 to 2025;
   his successor was "elected [...] in 2024", 10-K FY2026): about eleven years after the conduct alleged and nearly four after
   the injunction. Four of today's directors, the Lead Director among them, sat on the board through those years (Nance since
   2007, Fazzolari since 2013, Deckard since 2015, Livingston since 2017; proxy). The framework's inversion of Berkshire's own rule
   asks whether a management acted when it learned of a problem, and the row is "the main problem was they didn’t act when they
   learned about it" **[M2017-005]**; "a pound of cure, promptly applied, is worth a ton of cure that’s delayed" **[M2017-007]**;
   the instruction to managers is "tell us the bad news immediately" **[M1998-039]**. The conduct alleged was the opposite: rising
   overcharge estimates kept from the CEO, the CFO, the audit committee and the auditors, the people whose job is to hear bad
   news, while the shareholders' filings omitted the contingency.
5. **A jury's finding of fraud at a subsidiary (2024).** A Consumer subsidiary was found by a jury to have breached contracts with
   a former supplier, misappropriated trade secrets and committed fraud; judgment $110.8M plus interest; the company is appealing
   and accrues $0.5M (10-K FY2026, Note P; 10-Q, Note 13). Disputed and on appeal; recorded, given less weight than the settled
   matter.
6. **What weighs the other way.** The restatement moved accruals between quarters and changed no fiscal year; the CEO and CFO were
   not charged; the General Counsel was replaced in 2024; incentive pay has been allowed to fail (above); at least six of the
   eleven independent nominees joined the board in 2021 or later (Whited 2021, Pawlikowski 2022, Beck, Mapes and Morford 2025,
   Gentile 2026; proxy); the litigation disclosures I read in the 10-K and 10-Q are full and plain (Q4).

### The judgment
The test is not proof but doubt: "If you’ve got doubts, forget it." **[M2013-088]**; the speakers accept the cost, "we rule out
90 percent of the times. And we may be wrong about a fair number that we’re ruling out" **[M2007-092]**; "trustworthiness is more
important than the brains" **[M2015-047]**. The question for a part-owner is the second yardstick, "how well that they treat their
owners" **[M1994-008]**, and whether I can count on this management to tell the owners and their auditors the bad news when it is
theirs to hear. The record is a government-overcharging investigation in the company's largest business; on the SEC's account a
chief compliance officer who kept the rising estimates from the CEO, the CFO, the audit committee and the auditors; a company that
called the case meritless for four years and then took a permanent injunction; and a CEO and a board, whose senior members are
still in place, who left the same man in charge of compliance for nearly four years after he was enjoined under the rule against
falsifying books and records. Read with it, today's habits: the featured adjusted figure, now one that leaves out depreciation,
which the rows call "an economic cost every bit as real as wages, materials, or taxes" **[R1996-023]**, and of the talk of which
they say "either they’re trying to con you in some way, or they’ve conned themselves" **[M2002-026]**. "There are also readings in
corporate culture that have to be made" **[M1998-121]**; "people leave track records in life" **[M1998-168]**; "everybody mouths
the integrity, even when it’s lacking" **[M2010-069]**. I do not find dishonesty proved against the present CEO, and the SEC's own
account puts the knowledge with the General Counsel, not with him; what the record leaves me is doubt about the culture of candour
with owners and auditors at the top of this company, which the board's retention of its compliance officer shows was not treated
as disqualifying. That is the kind of doubt the rows say closes the file **[M2013-088]**, **[M2015-047]**.

**VERDICT on integrity: OUT (on doubt, M2013-088).** Ability WEIGHS FOR. The file closes here; Q6 to Q12 are NOT REACHED as
judgments. Facts already found for later questions are written under AFTER THE STOP, and the Q7 arithmetic the owner asks for is
reported there under COMPUTATION, NOT A CLEARANCE.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED (the file closed at Q5). Facts found are under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a judgment. The arithmetic is under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT, at Q5 (integrity, on doubt).** Q1 IN, Q2 IN, Q3 weighs for modestly, Q4 weighs against without a STOP, Q5 OUT. The
integrity facts were judged at Q5, so the flag "recorded, not judged" does not apply. For the owner's record only, the Q7
arithmetic done after the stop (COMPUTATION, NOT A CLEARANCE): value range $71.94 to $89.52 a share, all-equity, against $97.73;
no case computed earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down under the question each bears on **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).

### Bearing on Q6 (the money and the owners)
- **Buybacks and their prices.** "we may repurchase shares [...] for prices that our management deems appropriate" (10-K FY2026,
  Note I); no value is stated. Prices paid under the programme: FY2024 526,113 shares at an average $104.50; FY2025 581,759 at
  $120.32; FY2026 699,931 at $110.72 (Note I); first quarter of FY2027 196 thousand shares for $22.386M, about $114.21 (10-Q,
  equity statement and cash-flow statement). Every one of these prices is above the top of the computed range below ($89.52
  all-equity). Earlier: $200.2M in FY2019 and $125.0M in FY2020 under a goal to "return $1.0 billion in capital to stockholders by
  May 31, 2021" (Note I; XBRL PaymentsForRepurchaseOfCommonStock). Remaining authorization $114.8M at 2026-05-31.
- **Dividends.** $271.7M in FY2026, about 42% of that year's owner cash (Q4 table); paid every year of the span, rising.
- **Deals.** Cash paid for businesses about $1.75B in FY2017 to FY2026 (Q3), all in cash on the filed cash-flow statements; no
  all-stock acquisition found in the filings read. Goodwill and intangible write-downs of about $244M in the same years (Q4).
- **Pay and the board.** The annual cash pool is 1.5% of pre-tax income, paid at 120% of target in FY2026; the PSUs of FY2026 are
  measured on "Adjusted EBIT Margin" and adjusted revenue growth (proxy, CD&A); the PSUs for FY2024 to FY2026 paid 0.0%. The CEO's
  brother is employed as a vice president (Q5). CEO pay $11.1M, ratio 185:1.

### Bearing on Q7: COMPUTATION, NOT A CLEARANCE
Script `q7calc.py`, output `q7calc_out.txt`, in the research folder. USD millions unless stated. Inputs from the filed cash-flow
statements (10-Ks FY2017 to FY2026, accessions in Step 0) and the 10-Q of 2026-08-31 (`0001193125-26-415321`).
- **The window and the cycle (specific (a)).** The literal window is FY2022 to FY2026. FY2022 is aberrational on the filer's own
  description (inventory built in raw-material inflation and supply shortages, 10-K FY2022, MD&A, as Q4 records) and FY2024 is the release ($179.8M of
  inventory cash); both lie inside the window, which therefore holds the whole build and release, and its average serves as the
  cycle base. The six-year mean FY2021 to FY2026 on the all-capex basis (469.1) is shown beside the five-year (449.3).
- **The cash series.** Owner cash after all capital spending (OCF less stock pay less capital spending): mean 449.3. After
  maintenance only, depreciation standing for maintenance as Q3 disclosed its guess (OCF less stock pay less depreciation): mean
  547.3. Acquisitions net of the filer's single line "Proceeds from sales of assets and businesses": 50.9, -10.8, 8.6, 595.8,
  179.2, mean 164.7; owner cash after all spending and purchases: mean 284.5. Working capital is inside operating cash in every
  case (specific (d)).
- **The growth shown.** The series changes sign (FY2022 negative), and the halves of the window give a meaningless multiple from an
  inventory year (specific (b)); growth is therefore measured between the averages of the two successive five-year blocks FY2017
  to FY2021 and FY2022 to FY2026 (CONVENTION of this run: (a) names growth between the averages of successive cycles, and the run
  has no cleaner cycle than the two blocks; rationale: the only measure in the text that the series allows). Aggregate, not per
  share. After purchases, the default pair of (c): 157.6 to 284.5, **12.5% a year**. All-capex before purchases: 310.6 to 449.3,
  7.7% a year. Sales over the same blocks: 5,491.5 to 7,307.1, **5.9% a year**. Organic growth as the filer reports it
  (consolidated, FY2022 to FY2026): 4.5% a year compounded.
- **The cap (Q3 and specific (f)).** The shown 12.5% is owner-cash growth well above sales growth, and the difference is the
  margin gain of FY2021 to FY2026 that Q2 did not credit (one inflation passed, no construction downturn). Q3's growth arithmetic
  (about 17% to 20% pretax on the capital added, reinvestment of roughly the size of the purchases plus spending above
  depreciation) supports growth near the sales rate. The growth carried is therefore capped at the sales growth, 5.9%; the
  uncapped 12.5% is shown beside. (The absurdity test of (f) does not bind: 12.5% for ten years would put owner cash after
  purchases near 7% of sales, below the 12.0% of FY2024.)
- **Tax and basis.** Owner cash is after the company's own cash taxes (Q7, Whose tax). All-equity: after-tax interest added back,
  interest mean 106.6 at the window's own tax rate (tax expense over pre-tax income FY2022 to FY2026, 21.4%; CONVENTION of this
  run: the company's own average rate rather than a statutory figure; rationale: the floor is applied after the company's own
  tax), 83.8. Net debt at 2026-08-31: current debt 407.5 plus long-term debt 1,999.0 less cash 312.8 = **2,093.7**; operating
  lease liabilities ($334.7M long-term) left out; the captive insurers' marketable securities, held inside other assets against
  insurance liabilities and not on the face of the balance sheet, not subtracted (CONVENTION of this run; rationale: they back
  reserves). No subsequent event in the 10-Q changes it. Shares 127.534M.
- **The two ends (specific (e)).** The filing allows the maintenance guess (Q3), so the case without growth is owner cash after
  maintenance only, with no purchases; the growth case charges all spending, purchases included, against the growth it buys,
  carried ten years, then zero nominal growth with purchases stopped (on owner cash before purchases, after all capital spending).
  The growth case comes out above the no-growth case at the sovereign, so the growth bought is worth more than its cost at 5.60%;
  at ten percent the two ends nearly meet (33.06 against 35.66), so at the floor the growth bought roughly breaks even.

| case, per share | all-equity at 5.60% | equity-only at 5.60% | all-equity at 10% | equity-only at 10% |
|---|---|---|---|---|
| no growth, after maintenance only (**bottom**) | **$71.94** | $76.63 | $33.06 | $42.91 |
| growth 5.9% (capped), all spending and purchases deducted (**top**) | **$89.52** | $87.22 | $35.66 | $42.24 |
| beside: growth 12.5% uncapped, same spending | $166.29 | $151.05 | $68.90 | $69.60 |
| beside: no growth, after all capital spending | $58.22 | $62.90 | $25.38 | $35.23 |
| beside: organic pair (purchases left out, 4.5%) | $90.65 | $90.23 | $40.65 | $48.09 |

- **The floor tested first.** The expected return at $97.73, all-equity: no-growth maintenance case 4.33%; capped growth case 5.26%;
  even the uncapped 12.5% case 8.06%. No case reaches about ten percent **[M2003-149]**. The price is above the top of the range,
  and the range (about 1.24 to one) is narrow. Were Q7 reached, this arithmetic would close it OUT, not TOO HARD.
- **Fair price (Part VII's definition, reporting only):** all-equity ($33.06 + $35.66) / 2 = **$34.36**; equity-only ($42.91 +
  $42.24) / 2 = **$42.57**.

### Bearing on Q8 (the alternatives)
- The 30-year Treasury at 5.60% (Step 0). Owner cash on the all-capex basis over the market value is 3.6% (449.3 over $12,464M);
  on the all-equity basis 3.7% (533.1 over $14,558M). Below the bond with no growth.

### Bearing on Q9 (the target's debt and exposures)
- Debt $2,406.5M at 2026-08-31 (net $2,093.7M), about 5.4 times the five-year mean owner cash after all capital spending; income
  before tax and interest covered interest about 8.8 times in FY2026 (982 over 111.5). The revolver was extended to 2031 with the
  interest-coverage covenant removed and a 3.75x leverage covenant kept (8-K `0001193125-26-094139`); a receivables securitization
  facility amended (8-K `0001193125-26-253577`). Operating lease liabilities $334.7M long-term (10-Q balance sheet).
- Exposures: the $110.8M judgment plus 9% prejudgment interest against a $0.5M accrual (range to $152.5M); product-liability risk
  carried in captive insurers with warranty reserves (Note P); the asbestos liability of the former Bondex/SPHC units resolved
  through a section 524(g) trust (payments FY2015 and FY2018, Q4); pension plans (a favourable $44.3M change in FY2026, MD&A).

### Bearing on Q12
- Nothing found: specialty coatings, sealants, roofing and DIY products. The FY2013 government-overcharging matter is recorded at Q5.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (acc64c21); written question by question; committed after each (Step 0 eb3f4cb8,
      Q1 ccf8c842, Q2 cddb0d02, Q3 0d340cb9, Q4 1b701c47, Q5 f6804362, this close). The run was killed after Q4 and resumed by the
      same analyst brief from the committed file and the research folder; no closed question was redone.
- [x] Dispatched: the brief allowed per-question pathspec commits; the dispatcher holds the lock (`Screens/_daily/_overnight.lock`,
      read once in the first session). The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared, not used
      (resumed session, in addition to the list at the top): the session's opening git status again named other research folders
      (AYI, ARCB), daily digests and coursework files, by name only; the five most recent commit subjects named another company's
      run and fold (PNR: "OUT at Q7 on price", its range and a fair-price alert) and a restatement of fair-price alerts across 44
      runs naming CB, BRK.B, TRV, HON, ATR, CSL and EFX; a directory listing of the system temp folder showed a file name with the
      ticker LRCX. None is about RPM; none was used.
- [x] Every v5 id resolves (`check_quotes.py` in the research folder: 69 ids, none missing, no E-ids; every fragment standing
      directly before an id is in that row). Every filing fact carries its accession or names its filing and note; the two SEC
      litigation releases are primary documents from sec.gov, saved to the research folder's cache.
- [x] The order was kept; Q5 closed the file; everything after it is under AFTER THE STOP, and the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE and carry no entry language.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; the sovereign from the US
      Treasury par yield curve, dated; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations list; Q5's integrity record).
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the final commit (see the commit).
- **Corrections found on resuming:** my own uncommitted Q5 draft said the board had thirteen directors, twelve independent; the proxy
  has twelve nominees, eleven independent, and the run says so. The draft said the General Counsel was a named executive officer
  "through fiscal 2024"; the proxy lists him among the NEOs for fiscal 2025 too, and the run says "into fiscal 2025". The draft
  omitted that the FY2026 cash incentive paid 120% of target; added. No closed question (Step 0 to Q4) needed correction.
- **Doubts about my own judgment, stated:** the Q5 close rests on a matter of FY2013 settled without admission, and on the board's
  retention of the officer the SEC charged; a reader who weighs the age of the matter and the new board more heavily could pass Q5.
  The box would not change: the Q7 arithmetic finds no case earning the floor at the price.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The Q3 cap against Q2's uncredited improvement.** Q2's convention credits a change for the better only on a full cycle, and
Q7 carries "the growth the business has actually shown [...] capped by the growth arithmetic of Q3"; neither says how an improvement
Q2 declined to credit is removed from Q7's growth. Here the shown owner-cash growth (12.5%) is mostly that margin gain. I capped at
the business's own sales growth (5.9%), which is the figure (f) uses for the absurdity cut, and showed the uncapped case beside. A
sentence in Q7 saying which growth carries a margin gain Q2 did not credit would settle it. (2) **Specific (b) and (a) on a
sign-changing series.** The halves of a five-year window are meaningless when one year is an inventory build; (a) speaks of
"successive cycles" but gives no fallback where cycles cannot be dated from the series. I used successive five-year blocks and
confessed it. (3) **The no-growth end and purchases.** The text stops acquisition spending "after year ten, when growth stops"; it
does not say that the no-growth case spends nothing on purchases in years one to ten. I read it so (a business that buys no growth
spends nothing to buy it, the rationale the text gives) and said so. (4) **Q5's row for doubt.** **[M2013-088]** is short and, in
its own row, follows a remark about hiring salesmen; the framework uses it as the integrity rule. It carries the rule well enough
read with **[M2015-047]** and **[M2007-092]**, but the doubt rule leans on a thin row. (5) **The "recorded, not judged" flag** of
Part VII is written for a file closed before Q5; for a file closed at Q5 itself the template's box line has no wording, and I wrote
that the flag does not apply.
