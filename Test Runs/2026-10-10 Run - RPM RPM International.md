# Company Run — RPM International Inc. (NYSE: RPM) — 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under the canonical brief `Screens/_daily/_dispatch_brief.md`. Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession; a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Copied from the template before any fetch (commit acc64c21).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

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
