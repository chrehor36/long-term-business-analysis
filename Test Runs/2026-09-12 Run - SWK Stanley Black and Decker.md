# Company Run — STANLEY BLACK & DECKER, INC. (SWK) — 2026-09-12
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Filled top to bottom. **Stopped at the first verdict that is not IN.**

Research folder: `Test Runs/_research 2026-09-12 SWK/` — every figure below is reproducible
from the scripts and stripped filings committed there.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.35 %** · date **09/11/2026** · source **US Treasury daily par yield curve, 30 Yr
  (issuing authority; cache deleted and re-struck fresh for this run — the 2026-09-12 print
  was not yet published at 18:24 local, so 09/11 is the currently observed rate)**
- FX: **none needed.** SWK reports in USD. Non-US sales are roughly a third of revenue but
  the reporting and the quote are both USD; no ADR ratio.

**Price and share count, re-struck (the brief's instruction, and it was right):**
- price **$89.24**, close **2026-09-11**, source Yahoo chart via `tools/sources.py:price()` —
  **aggregator, flagged, live quote only.**
- shares **151,016,641**, from the **cover of the Q2 FY2026 10-Q filed 2026-07-29, period
  2026-07-04, accession 0000093556-26-000031** (`python Screens/cover_shares.py SWK`).
- **market cap = $13,477M.**
- **THE QUEUE'S CAP WAS WRONG AGAIN — the tenth check and the ninth miss.** The row carries
  `cap_m 14826`; the struck figure is **$13,477M, 10.0% lower**. The queue cap embeds a
  stale price, not a stale share count (the cover count is unchanged since FY2025).

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **FY2025 Form 10-K, fiscal year ended 2026-01-03, filed
  2026-02-24, accession 0000093556-26-000009.** Also read: Q2 FY2026 10-Q (period 2026-07-04,
  acc. 0000093556-26-000031), Q1 FY2026 10-Q (acc. 0000093556-26-000015), the FY2024, FY2023,
  FY2022, FY2021 and FY2019 10-Ks, and the 2026 and 2025 DEF 14A proxies.
- figure cross-checked against the filed statement: **net cash provided by operating
  activities, FY2025 — XBRL `NetCashProvidedByUsedInOperatingActivities` $971.2M against the
  filed Consolidated Statements of Cash Flows line "Net cash provided by operating activities
  971.2". Also matched on the same page: stock-based compensation expense $94.1M, accounts
  payable change $(284.6)M, capital and software expenditures $(283.3)M.**

**Live-deal check, run by hand (operator rule 4; the ROKU rule of 2026-09-12).**
`tools/sources.py:deal_note()` raised a `TypeError` on my first call — **my error, not the
tool's**: I passed `cik_for()`'s two-tuple where it wants the bare padded CIK. Re-run
correctly it returns **no hard deal form and one 8-K Item 1.01 since the annual report of
2026-02-24: filed 2026-06-24, accession 0001193125-26-281077, items 1.01 / 1.02 / 2.03 /
9.01.** Items 1.01+1.02+2.03 together are the signature of a credit-facility replacement,
not a merger, and the document confirms it. **No live merger. The quote is not a spread.**
- **But there IS a live divestiture, and the screen cannot see it.** In December 2025 SWK
  agreed to sell **Consolidated Aerospace Manufacturing (CAM) to Howmet Aerospace for
  $1.8 billion cash**, expected to close in the first half of 2026, net proceeds
  $1.525–1.600bn earmarked to reduce debt. CAM contributed **$413.9M of net sales and
  $31.3M of segment profit** to Engineered Fastening in FY2025 (10-K p. 602). Every
  owner-earnings figure below therefore describes a perimeter that is about to shrink again.
- **TWO CORRECTIONS TO THE TWO PASSAGES ABOVE, found at Q2 and inserted rather than overwritten
  (operator rule 6; both passages were committed in `e7f2c42`).**
  1. **"The document confirms it" was written before I had opened the document.** That is the
     error the resume state records as its item 4B — trusting a filename, here an item-code
     pattern. **Opened afterwards** (`8K_2026-06-24_item101.txt`): Item 1.01 is a **$1.0 billion
     364-Day Credit Agreement dated 2026-06-18**, Citibank as administrative agent, advances due by
     2027-06-17 with a one-year term-out option; Exhibits 10.1 and 10.2 are credit agreements. The
     conclusion stands — no merger — but it now rests on the document.
  2. **CAM is not pending. The sale CLOSED in April 2026.** The Q2 2026 release (8-K of 2026-07-29):
     *"Successfully completed the sale of Consolidated Aerospace Manufacturing ('CAM') in April"*,
     and *"the Company reduced debt by $1.7 billion and repurchased approximately 3.2 million shares
     for $250 million."* I had read only the 10-K's description when writing Step 0. **The perimeter
     has already shrunk**, and the Q2 FY2026 10-Q reflects it.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.**
Stanley designs and sources hand tools, cordless power tools, lawn machines and industrial
fasteners, and sells them mostly through two American retail chains. It buys resin, steel,
zinc, copper, aluminium, nickel, battery cells, motors and electronics; it assembles or
has assembled; it ships to a home-centre distribution centre and gets paid. Revenue
FY2025 **$15,130.4M**, of which **Tools & Outdoor $13,158.2M (87%)** and **Engineered
Fastening $1,972.2M (13%)**. Gross profit **$4,588M (30.3%)**; segment profit T&O
**$1,329M (10.1%)**, EF **$197.0M (10.0%)**; corporate overhead **$270.4M**. The margin
between what a DeWalt drill costs to land in Atlanta and what Home Depot will pay for it
is the whole business, and the buyer of the shares is buying that spread times units.

**The number I keep in my head:** gross margin 30.3%, distribution costs of **$522.5M**
sitting in SG&A rather than cost of sales (10-K p. 828) — so SWK's gross margin is
**3.5 points flattered relative to a peer that puts warehousing in COGS**, and the company
says so itself. That disclosure is a candor point and it also means the peer row must be
built on operating margin, not gross margin.

**The scarce input this business controls.** Two candidates, and only one survives.
- *Brand and the battery platform.* DEWALT's 20V MAX / FLEXVOLT / POWERSTACK system is a
  real switching cost: a tradesman with nine DEWALT batteries buys the tenth DEWALT tool.
- *Retail shelf.* This is the one that is genuinely scarce — and **SWK does not control it.**
  **The Home Depot was 15% of consolidated net sales in FY2025 (14% in FY2024) and Lowe's
  12% (14%)** — 27% of the company between two buyers (10-K p. 186). The 10-K's own
  competition paragraph: *"Certain large customers offer private label brands ("house
  brands") that compete across a wide spectrum of the Company's Tools & Outdoor segment
  product offerings."* The scarce asset is owned by the customer, who is also a competitor.

**Will the fundamentals look broadly the same in ten years?** Yes, and that is the point of
Q1. Drills, sockets, blades, rivets and mowers are not a rapid-change industry; cordless
displaced corded over two decades, and the next substitution (higher-density cells, robotic
mowers) will be slow and visible. **This is a simple and stable business in [E3-31]'s sense.
Understanding it does not require months.** [E4-46] is satisfied: nothing here would take
five months to learn.

**What I had to work through, and it is not a Q1 failure.** The reported series is not
continuous, and three separate things break it:
1. **A perimeter that has been rebuilt four times.** Black & Decker merged in March 2010
   (revenue $3.7bn → $8.4bn); Craftsman and Newell Tools bought in March 2017 ($2,583.5M of
   cash out that year); **Security sold in July 2022** (CSS $3.1bn net, MAS $916M), Oil &
   Gas August 2022, **Infrastructure April 2024 ($729M net)**, and **CAM pending at $1.8bn.** *(Corrected at Q2: CAM closed in April 2026 — see the Step 0 correction.)*
   Cumulative acquisitions since 2002 are **~$13.5 billion** by the company's own count
   (FY2021 10-K p. 627).
2. **A restatement that moved three quarters of a billion dollars out of operating cash.**
   The originally filed FY2017 operating cash flow was **$1,418.6M**; the FY2019 10-K
   reports FY2017 at **$668.5M**, because **$705 million of "proceeds related to deferred
   purchase price receivable related to an accounts receivable sales program, which was
   terminated in February 2018"** was reclassified from operating to investing (FY2019 10-K
   pp. 4083, 5144). Same direction in FY2016 (restated $1,485.2M → $1,185.5M). **Every
   figure in this run uses the newest vintage** — `tools/run.py` does this correctly since
   the 2026-09-07 fix, and this is the second name in the project where the withdrawn
   vintage would have changed the answer materially.
3. **A cost programme that has been the headline for four years.** The "Global Cost
   Reduction Program" launched mid-2022: $500M of SG&A savings plus a supply-chain
   transformation promising **$1.5bn of run-rate savings and "35%+ adjusted gross margins."**
   Declared **complete at the end of 2025** at ~$2bn of claimed run-rate savings. Restructuring
   charges are not a single quarter's dump — they are an annuity: **~$89M (2025), ~$100M
   (2024), $39.4M (2023), $140.8M (2022), $14.5M (2021), $83.0M (2020), $154.1M (2019),
   $160.3M (2018)** (`RestructuringCharges`, newest vintage, cross-checked to the FY2025
   restructuring-reserve rollforward: reserve $45.4M + net additions $89.1M − usage $85.6M
   − currency $1.1M = $47.8M). **[E3-53] and [E5-33]: these are real costs and they stay in
   the owner-earnings mean.** Fifteen of the eighteen filed years carry a "non-GAAP
   adjustment" to gross profit or segment profit. **[E2-57] fires** — "except for" is not
   excised from this lexicon, it is the lexicon.

None of that stops Q1. I can say what the business does, who pays, and what it buys, and I
can name the document behind every number above.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

### FIRST, THE CASE AT FULL STRENGTH — the prior was IN NARROW on DEWALT, and it deserves to be built properly

The bull case is not a straw man and I build it from SWK's own filings before attacking it.
1. **A battery platform is a real switching cost.** A tradesman's cordless kit is a system: the
   tool, the battery, the charger. DEWALT 20V MAX, FLEXVOLT, POWERSTACK and POWERSHIFT are named
   trademarks in the FY2025 10-K (p. 193). Each battery already owned lowers the price of the next
   DEWALT tool against a MILWAUKEE one. That is [E3-03] criterion (2) in the one place it can live
   in this industry.
2. **DEWALT has grown through the whole downturn, on the company's own telling.** Q3 2024: *"growth
   in DEWALT was offset by the weak consumer and DIY backdrop."* Q4 2024 headline: *"DEWALT Posts 7th
   Consecutive Quarter of Organic Growth."* Q1 2025 headline: *"DEWALT Posts 8th Consecutive Quarter
   of Revenue Growth."* Q2 2025: *"continued DEWALT professional growth."* Q3 2025: *"Continued
   Growth in DEWALT."* FY2025 10-K p. 865: *"growth in DEWALT®."*
3. **The shelf is scarce and SWK holds a large piece of it.** The Home Depot 15% and Lowe's 12% of
   net sales in FY2025 (10-K p. 186) is not only a risk — it is also physical space in the two
   rooms every American contractor walks through, and a competitor without it cannot reach the
   customer at SWK's cost.
4. **The tariff test's first half passes on margin.** Tools & Outdoor raised price **+2%, +5%, +5%,
   +4%** in the four quarters Q2 2025 – Q1 2026 (8-K EX-99.1 releases of 2025-07-29, 2025-11-04,
   2026-02-04, 2026-04-29), and consolidated adjusted gross margin went **27.5% (Q2 2025, "a
   3-point gross impact" from tariffs) → 31.6% (Q3) → 33.3% (Q4)** — recovery within one to two
   quarters. That is faster than ELF's three quarters and it is the PLPC instrument passing on price.
5. **The newest quarter is the best one.** Q2 2026 (release of 2026-07-29): T&O **volume +3% with
   price flat**, organic +3%, *"primarily driven by power tools strength in U.S. retail and C&I
   channels"*; T&O adjusted segment margin **11.8%, up 380bp**; debt cut **$1.7bn** after the CAM
   sale closed in April.

That is a real case. Now the attack, and the filing supplies every weapon.

### NOW THE ATTACK

**Criterion (2), in the company's own words.** FY2025 10-K p. 184, verbatim: *"The Company
encounters active competition in the Tools & Outdoor and Engineered Fastening segments from both
larger and smaller companies that offer the same or similar products or services or that produce
different products appropriate for the same uses. **Certain large customers offer private label
brands ("house brands") that compete across a wide spectrum of the Company's Tools & Outdoor
segment product offerings.**"* The two customers that are 27% of the company are also competitors
who own the shelf, set the promotional calendar, and sell their own brand beside SWK's. **A franchise
is a product its customers think has "no close substitute" [E3-03]; SWK's largest customers sell the
close substitute on the next hook.** And the private label is not the only one: the competitor row
below shows a direct rival, in the same two stores, larger than SWK and growing while SWK shrank.

### [E2-44] — BOTH HALVES, ON THE TARIFF-AND-INFLATION YEARS

**Half one: can it raise prices "even when product demand is flat and capacity is not fully
utilized"?** The filed price/volume decomposition, Tools & Outdoor (named Tools & Storage before
2022), from each year's 10-K MD&A (FY2019 10-K p. 3886-3888; FY2021 p. 872-874, 922-924; FY2022
p. 803-805; FY2023 p. 906-908, 955-957; FY2024 p. 883-885; FY2025 p. 825-826, 866):

| Fiscal year | T&O price | T&O volume | consolidated gross margin, GAAP / adjusted | T&O segment margin, GAAP / adjusted |
|---|---|---|---|---|
| 2018 | organic +7% (not split) | | 34.7% / 35.2% | |
| 2019 | +1% | +4% | 33.3% / 33.5% — *"volume, productivity and price were more than offset by **tariffs**, commodity inflation and foreign exchange"* | 15.1% / 15.5% |
| 2020 | +2% | +2% | 33.7% / — | 17.6% / 18.1% |
| 2021 | +3% | **+17%** | 33.3% / 33.6% | 15.5% / 16.9% |
| **2022** | **+7%** | **−12%** | **25.3% / 26.0%** | **6.7% / 8.4%** |
| **2023** | **0%** (none named; *"due to a 7% decline in volume"*) | **−7%** | **24.9% / 26.0%** | **5.1% / 6.6%** |
| **2024** | **−1%** | +1% | 29.4% / 30.0% | 9.0% / 10.1% |
| **2025** | **+3%** | **−5%** | 30.3% / 30.7% | 10.1% / 10.7% |

**The tariff quarters**, Tools & Outdoor, from the 8-K EX-99.1 releases (all in the research folder):

| Quarter | price | volume | consolidated GM, GAAP / adjusted |
|---|---|---|---|
| Q3 2024 | +1% | −3% | |
| Q4 2024 | −1% | +4% | |
| Q1 2025 | 0% | +1% | 29.9% / 30.4% |
| **Q2 2025** | +2% | **−5%** | **27.0% / 27.5%** |
| **Q3 2025** | **+5%** | **−7%** | 31.4% / 31.6% |
| **Q4 2025** | **+5%** | **−9%** | 33.2% / 33.3% |
| **Q1 2026** | **+4%** | **−5%** | 30.1% / 30.2% |
| Q2 2026 | **0%** | +3% | 33.0% / 33.7% — **incl. ~250bp of IEEPA tariff refunds** |

**Reading it.** Stanley did hold price while volume fell — **four consecutive quarters of +2% to
+5% price against −5% to −9% volume.** But look at what the price bought. **In every one of those
four quarters volume fell by more than price rose**, and **the first quarter in which volume grew is
the quarter in which price went to zero.** Price and volume are trading against each other quarter by
quarter. That is a demand curve with close substitutes on it, and it is the thing [E2-44]'s first
characteristic is designed to exclude: the corpus asks for price rises that hold *"even when product
demand is flat"*; SWK's price rises were followed every time by falling demand.

**The 2018-19 tariff round already answered once.** Adjusted gross margin fell 35.2% → 33.5% with
price +1%, and the 10-K named tariffs as a cause (FY2019 10-K p. 3888).

**The gross-margin recovery the PLPC instrument asks for — and the answer depends on which shock.**
- **The 2025 tariff shock:** trough 27.5% adjusted (Q2 2025) to 33.3% (Q4 2025): **recovered in two
  quarters.** That passes, and I record it as passing.
- **The 2022 inflation shock — the larger one:** adjusted gross margin 33.6% (FY2021) → 26.0%
  (FY2022) → 26.0% (FY2023) → 30.0% (FY2024) → 30.7% (FY2025). **Four years later it has not
  recovered**: **2.9 points below FY2021, 2.8 below FY2019**, and the company's own objective —
  *"returning adjusted gross margins to historical 35%+ levels"*, stated in the FY2022, FY2023 and
  FY2024 10-Ks — **was not met** when the programme built to reach it was declared complete at the
  end of 2025 (FY2025 10-K p. 292). **Q2 2026's 33.7% contains ~250bp of one-time tariff refunds.**
- **T&O segment margin, which is where DEWALT lives: 15.5% adjusted (FY2019) → 10.7% (FY2025).**
  Adjusted for everything the company chooses to adjust for, the segment earns **about two-thirds of
  its pre-shock margin.**

**Half two: can it grow dollar volume "with only minor additional investment of capital"?** Build
the physical series **[E4-55]** — compounding the filed T&O volume percentages, FY2019 = 100
*(CONVENTION: compounding rounded MD&A percentages is my index, not a filed series; it carries ±1
point a year of rounding, and the MTD and Excel outdoor businesses bought in late 2021 join the
organic base after their first twelve months, so the product mix is not constant)* — `volindex.py`:


| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|---|---|
| **T&O volume index** | 100.0 | 102.0 | 119.3 | 105.0 | 97.7 | 98.6 | **93.7** |
| T&O price index | 100.0 | 102.0 | 105.1 | 112.4 | 112.4 | 111.3 | 114.6 |

**Tools & Outdoor ships about 6% fewer units than in 2019 and about 21% fewer than at the 2021
peak**, after **$2,043.8M of acquisitions in FY2021** (`PaymentsToAcquireBusinessesNetOfCashAcquired`,
mainly MTD and Excel) were added to the segment in between. This is the Precision Steel shape
**[E4-55]**: *"a serious reverse, not likely to disappear in some 'bounce back' effect"* — dollar
revenue level ($15.28bn FY2021 restated, $15.13bn FY2025) while the physical series fell.
**Half two fails.**

### [E3-62] — THE SECOND STEP: HOW MUCH OF THE SAVINGS STAYED HOME?

The Global Cost Reduction Program is the cleanest test of this in the project so far, because the
company published the savings. Mid-2022: *"a supply chain transformation expected to deliver $1.5
billion of pre-tax run-rate cost savings by the end of 2025 to achieve projected 35%+ adjusted gross
margins"* plus *"$500 million"* of SG&A savings (FY2023 10-K p. 621); *"on track to grow to
approximately $2 billion of pre-tax run-rate savings by year-end 2025"* (p. 630). Declared complete
at the end of 2025.

**What stuck to the ribs:** gross profit **$5,194M (FY2021 as originally filed)** → **$4,588M
(FY2025)** on revenue of $15.6bn → $15.1bn. EBIT (pretax + interest expense − interest income,
continuing operations, newest vintage, `roic.py`) **$1,763M (FY2021) → $736M (FY2025)**. **Two
billion dollars of claimed annual savings, and a billion dollars less operating profit on roughly
the same revenue.** The corpus's vendor never asks *"how much is going to stay home and how much is
just going to flow through to the customer"* **[E3-62]**; this filing answers it by subtraction. The
savings went to the customer or to covering costs the price could not, and either way *"nothing was
going to stick to our ribs as owners."*

### [E4-32] DIRECTION, AND [E4-04] REBUILD

**Direction: narrowing, measured.** Pre-tax return on invested capital (EBIT ÷ [equity + debt −
cash], continuing operations, `roic.py`): **15.5% (FY2016), 14.9% (FY2017), 9.7% (FY2018), 10.7%
(FY2019), 9.9% (FY2020), 9.8% (FY2021), 1.9% (FY2022), 0.0% (FY2023), 3.9% (FY2024), 5.0%
(FY2025).** EBIT margin **13.2% (FY2017) → 4.9% (FY2025).** The company is **writing down its own
brands**: trade-name impairments of **$108.4M in FY2025** (*"updates to the Company's brand
prioritization strategy impacting the Lenox, Troy-Bilt, and Irwin trade names"*) and **$41.0M in
FY2024** (Lenox) (10-K p. 820), and in 2026 is **moving gas walk-behind outdoor products to a
licensing model** (Q2 2026 release). **Brands bought in 2017 and 2021 are being impaired or licensed
out in 2024-26. The direction is narrowing in every year the filings cover since 2017 [E4-32].**

**Rebuild [E4-04].** The test: does a lapse in spending destroy the structure or merely narrow it,
and does the spending defend the same advantage or buy its replacement? R&D is **$321.4M (2.1% of
sales)** (10-K p. 197). A cordless platform is re-engineered with each cell generation, and the maker
who skips one loses the tradesman's next battery purchase to the rival who did not. FLEXVOLT,
POWERSTACK and POWERSHIFT are **replacements of the basis, not maintenance of a fixed one** — the
Rhodes Ridge case, not the Coca-Cola case. **[E4-04] bites.**

### [E3-33] / [E5-28] — UNTAPPED PRICING POWER: NO. AND THE AGONY METRIC [E4-37] IS FILED.

Claiming untapped pricing power is claiming a near-monopoly **[E5-28]**, and the row below refutes
that. The agony metric **[E4-37]**: FY2025 10-K p. 865, *"Organic revenue decreased 2% driven by a
soft market backdrop and **mid-year tariff related promotional reductions**, partially offset by
strategic pricing initiatives"*; Q3 2025, *"driven by **expected tariff related promotional
reductions**"*. Price here is a quarterly negotiation with two buyers over a promotional calendar,
and **the quarter volume came back is the quarter price went to zero.**

### [E2-45] — THE ATTACKER'S TEST

*"How I would like, assuming I had ample capital and skilled personnel, to compete with it."* It
does not need imagining; it is filed. Build one professional cordless brand with a higher gross
margin, put its cash into cell-generation R&D, sell it through the same two retailers, and let the
incumbent carry a dozen overlapping brands at a 30% gross margin. **Techtronic did, and in 2025
overtook SWK on revenue ($15,260M against $15,130M) at a 41.2% gross margin and 8.8% EBIT margin,
with $700M of net cash**, in the year SWK's T&O units fell 5%.

### [E4-36] — WHICH OF THE FOUR CAUSES?

SWK's best recent years were **wave-riding**: T&O volume **+2%, +17%** in FY2020-21 was the pandemic
DIY and housing wave, and when it ended the volume index gave all of it back and six points more.
The longer record is **serial acquisition** (~$13.5bn since 2002, FY2021 10-K p. 627). Neither is
ownable. *"If he gets off the wave, he becomes mired in shallows"* **[E3-51]**.

### THE COMPETITOR ROW — required **[E3-28]**. A moat is a relative claim.

*Same construction as the ITW run's row (`Test Runs/_research 2026-08-26/ITW evidence pack +
competitor row (DOV, PH, EMR, DHR).md`), so ITW and Emerson are carried from that run; ITW was
recomputed here and matched (26.3% margin, 63.9% return on net tangible operating assets). EBIT =
issuer's operating income, or pretax + interest expense − interest income where no operating line is
filed (SWK files none). Return on net tangible operating assets [E2-43] = EBIT ÷ (net PP&E +
inventories + trade receivables − trade payables). After-tax ROIC = EBIT × (1 − effective tax) ÷
(equity + total debt − cash). Scripts: `peers2.py`, `roic.py`.*

| Company | FY end | Revenue | **EBIT margin** | gross margin | same-year growth | return on net tangible op. assets | incl. goodwill & intangibles | after-tax ROIC | source |
|---|---|---|---|---|---|---|---|---|---|
| **SWK** | Jan-2026 | $15,130M | **4.9%** | 30.3% *(26.8% if its $522.5M of distribution costs sat in COGS)* | organic **−2%**; T&O volume **−5%**, price +3% | **15.5%** | **4.9%** | **4.8%** *(3.8% effective tax)* | FY2025 10-K, acc. 0000093556-26-000009 |
| **Techtronic** (MILWAUKEE, RYOBI) | Dec-2025 | **$15,260M** | **8.8%** (normalised 9.3%) | **41.2%** (+91bp) | **+4.1% local currency**; MILWAUKEE **+7.9%**, RYOBI **+5.4%** | n/c — see limit | n/c | n/c; **net cash $700M** | TTI 2025 Annual Results press release, 2026-03-03 (issuer, ttigroup.com) |
| **Makita** | **Mar-2026** | ¥777,600M | **13.5%** (prior 14.2%) | n/c | revenue +3.2%, *"due to the impact of depreciation in the yen"* | n/c | n/c | n/c; equity ratio **84.4%** | Consolidated Financial Results (English Kessan Tanshin), 2026-04-28 (issuer, makita.biz) |
| **Snap-on** | Jan-2026 | $4,709M | **28.2%** | n/c | n/c | PP&E not tagged; n/c | n/c | **18.8%** | SEC companyfacts, FY2025 10-K |
| **Illinois Tool Works** | Dec-2025 | $16,044M | **26.3%** | — | organic 0.0% | **63.9%** | **34.3%** | **28.3%** | ITW run, 2026-08-31 |
| **Emerson** | **Sep-2025** | $18,016M | **19.6%** | — | +3.0% | 51.9% | 10.3% | 8.5% | ITW run, 2026-08-31 |
| **Fortune Brands Innovations** | Dec-2025 | $4,463M | **11.6%** | — | n/c | 28.4% | 11.4% | n/c *(equity tag did not resolve)* | SEC companyfacts, FY2025 10-K |
| **Toro** *(closest listed outdoor-power peer; added by me)* | **Oct-2025** | $4,510M | **9.1%** | — | n/c | 26.5% | 18.7% | 16.9% | SEC companyfacts, FY2025 10-K |
| *channel:* **Home Depot** | Feb-2026 | $164,683M | **12.7%** | — | — | — | — | — | SEC companyfacts, FY2025 10-K |
| *channel:* **Lowe's** | Jan-2026 | $86,286M | **11.8%** | — | — | — | — | — | SEC companyfacts, FY2025 10-K |

- **Peers named: 9** — the operator's eight plus Toro. The industry's real competitors number more:
  **Bosch (private), Hilti (private), Festool (private), Husqvarna (Nasdaq Stockholm)** and the
  retailers' **house brands**, which file nothing separately. I took what files in a form I could
  reach, and say so.
- **The row's limits.** (1) **TTI and Makita are not SEC registrants.** TTI's figures are its own
  release of audited 2025 results (HKEX 0669, USD, December year end — the same window as SWK); **I
  did not pull TTI's full annual report**, so its balance-sheet returns are not computed. Makita's
  are its own English Kessan Tanshin — **IFRS, JPY, unaudited at release, fiscal year three months
  later than SWK's**; its growth is flattered by the yen and says so. Ladder rung: exchange filings
  via the issuer's IR site; EDINET not attempted (blocked: paid key). (2) **Gross margins are not
  comparable across filers** — SWK itself says its distribution costs sit in SG&A where others put
  them in COGS (10-K p. 828); EBIT margin is the comparable column. (3) **Window offsets**: Makita
  (Mar-2026), Emerson (Sep-2025), Toro (Oct-2025). (4) **[E3-61]: the row shows position, not
  conduct** — it cannot say whether SWK's CEO of October 2025 turns the ship.
- **What the row says. SWK is LAST OF TEN on EBIT margin — 4.9% against 8.8% to 28.2% — and last on
  every return measure that could be computed.** The decisive pair is not ITW, a different business;
  it is **Techtronic: same category, same two retailers, same tariffs, now slightly larger than SWK,
  1.8 times the EBIT margin, 11 points more gross margin, +4.1% in local currency in the year SWK's
  T&O units fell 5%, and net cash where SWK carries $5.9bn of debt.** Both suspended promotions for
  tariffs in the second half of 2025 (TTI: *"the discretionary suspension of certain second half
  promotions due to tariffs"*; SWK: *"mid-year tariff related promotional reductions"*). **Only one
  lost units.**
- **And the channel out-earns the maker.** Home Depot and Lowe's make 12.7% and 11.8% EBIT on what
  they sell, SWK's products included; SWK makes 4.9% making them. **The rent in this chain sits with
  the shelf.**
- **Class: [x] NONE** · **Direction: narrowing.** **Not PROVISIONAL**: nine peers obtained; the two
  foreign ones are stated with limits and do not carry the verdict alone — Snap-on, ITW, Emerson,
  Fortune Brands, Toro and both retailers all sit above SWK on the same construction.

### [E2-49] — A YARDSTICK ABOUT THE MOAT THAT DID NOT SURVIVE

The DEWALT growth streak — the bull case's best filed fact — **was never quantified in any release
I read.** Q4 2024 headline (2025-02-05): *"DEWALT Posts 7th Consecutive Quarter of **Organic**
Growth."* The next quarter (2025-04-30): *"DEWALT Posts 8th Consecutive Quarter of **Revenue**
Growth"* — **the definition changed between two consecutive counts.** Q2 2025: the count is gone
(*"DEWALT Delivered Topline Growth"*). Q3 2025: *"Continued Growth in DEWALT."* **Q4 2025, Q1 2026
and Q2 2026: DEWALT does not appear in the release text at all** outside the boilerplate "About"
paragraph. *"Yardsticks seldom are discarded while yielding favorable readings"* **[E2-49]**.
**Fires on the organic-to-revenue switch** — the switch between consecutive counts is the tell
whatever followed. **The disappearance is carried with its alternative**: it coincides with the CEO
change of October 2025, and a new CEO changing the release template is a different event from a
metric withdrawn after deterioration. DEWALT's revenue is disclosed nowhere, so the filings cannot
separate the two. **Prior tally 6 fires, 5 failures; SWK is the seventh fire, on the switch.**

### THE VERDICT, AND THE CASE AGAINST IT STATED FIRST **[E4-51]**

**The strongest case against OUT:** DEWALT is plausibly a narrow franchise inside a conglomerate of
weaker brands; the consolidated numbers carry CRAFTSMAN, BLACK+DECKER, outdoor and five years of
restructuring; the tariff margin recovered in two quarters; and Q2 2026 shows volume returning at
flat price. On that view the row compares TTI's best brand with SWK's whole portfolio.

**Why it does not rescue Q2.** (1) **The filings do not let anyone test it** — DEWALT's revenue and
margin are disclosed nowhere, and a moat that rests on an undisclosed unit is a *provisional* moat,
which cannot be IN. (2) **The shares own the portfolio**, and the portfolio fails criterion (2) in
the 10-K's own words. (3) **Allowing the premise anyway**, Tools & Outdoor — the segment that contains
DEWALT — earns **10.7% adjusted segment margin before corporate overhead**, against TTI's **8.8% EBIT
after** its corporate costs with 11 points more gross margin. (4) **TTI's RYOBI is a consumer brand
and grew 5.4%** the same year; the consumer mix is not an excuse the row allows.

**Can I name the document that would resolve this?** Nothing here is UNRESEARCHED — every figure is
filed. **OUT, on the business.** The product has close substitutes by the company's own description;
the customers who control the shelf sell one; price rises were followed by larger unit losses in
every tariff quarter; the physical series sits below 2019; the $2bn cost programme did not reach the
owners; and on the same construction SWK is last of ten. **This is the PLPC shape one step on** —
PLPC passed on price and failed criterion (2) for want of a cost advantage; SWK passes the tariff
margin recovery and fails criterion (2), [E2-44]'s volume leg, [E2-44] half two, [E4-55], [E3-62],
[E4-32] and the row. **And it is the ELF shape: passed on price, failed on units.**

- **VERDICT: [x] OUT** — on the business.

⛔ **THE FILE CLOSES HERE.** Everything below is **RECORDED, NOT GOVERNING** — written because the
brief asked for it and because operator rule 3 requires the price under `COMPUTATION — NOT A
CLEARANCE`. **Nothing below can reopen Q2 [E2-37, E2-38, E3-39].**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⚠️ **RECORDED, NOT GOVERNING. Q2 returned OUT and the file closed there.** Written because the
brief asked for it (the BA precedent of 2026-09-12) and because the manager record bears on how
the Q2 finding should be read. Nothing here promotes, and per the guardrail nothing here could
repair Q2 **[E2-37, E2-38, E3-39]**.

**STEP 1 — THE WEIGHT CASE.**
- [x] **Daily execution [E3-38, E3-43]** — ticked. A business with close substitutes and a
      customer-administered price is *"a business, unlike a franchise"*, and *"can be killed by
      poor management"* **[E3-43]**; every quarter's price and promotional decision with two buyers
      is have-to-be-smart-every-day.
- [ ] Control — no.
- [x] **Leverage [E3-29]** — ticked, narrowly. Total debt **$5,863.7M** at FY2025 year end (short-term
      borrowings $605.6M + current maturities $554.8M + long-term $4,703.3M), **$4,757.9M** at
      2026-07-04; tangible equity **negative** (goodwill + intangibles $10,374.8M against equity
      $9,054.6M); Moody's **Baa3**, one notch above sub-investment grade; S&P cut A- → BBB+ in Q3 2025
      (10-K p. 971).
**Case declared: BINARY GATE — no price compensates.** Recorded only; Q2 already closed the file.

### HONESTY — binary, each matter dated to when it became PUBLIC **[E5-16]**
1. **Non-reliance on filed financial statements — public 2022-01-26** (8-K
   Item 4.02, acc. 0001193125-22-018393, read in full, `8K_2022-01-26_item402.txt`). After SEC
   comments on the FY2020 10-K, the Audit Committee concluded on 2022-01-24 that the FY2018-20
   annual and three 2021 interim statements *"should no longer be relied upon"*: the equity units
   of May 2017 and November 2019 had been split into two units of account, and the shares under
   the forward purchase contracts had been kept out of diluted EPS by the treasury-stock method.
   **Direction: the error flattered diluted EPS.** The 8-K: it *"will not change the Company's
   historical net earnings"*. The FY2022 10-K (p. 421) records **material weaknesses in internal
   control over financial reporting** for these instruments, remediated in Q1 2022. **Scored as a
   weak-accounting flag [E4-22], not a conduct finding** — the error was in an EPS denominator and
   a unit of account, surfaced by the SEC, corrected by a restatement; no individual was named and
   no penalty is filed. **[E5-38]: a fired accounting flag is not a venality finding.**
2. **Litigation sweep** — Item 3 and Note R/Q of the FY2025 10-K and Note O of the Q2 2026 10-Q,
   read: environmental Superfund matters (Lower Passaic River, Kerr McGee, reserved $13.9M for the
   latter) and ordinary product-liability. **No integrity matter found.**
**Honesty: no disqualifier found** — *"sincerity and empathy can easily be faked"* **[E5-17]**.

### THE FLAGS **[E4-22, E5-15, E4-29, E4-30]** — prompts to read, and several fire
- [x] **Weak accounting [E4-22]** — the 2022 Item 4.02 non-reliance above. **Second
      cockroach? Checked and scored fairly:** the $705M FY2017 operating-cash reclassification
      (deferred purchase price receivable, Step 0) was **a change of standard (ASU 2016-15),
      applied retrospectively, not an error** — it does not count as a second cockroach. It does
      show that the operating-cash line of FY2016-17 was, as originally filed, flattered by a
      receivables structure that the company ended in February 2018.
- [ ] Unintelligible footnotes — no. The SCF, receivables-sale, restructuring and tariff-refund
      notes are clear and quantified.
- [x] **Trumpeted projections [E4-22] and the guidance record [E3-48]** — fires, and the record is
      the sharpest single thing in Q3. Guidance given each February against outturn, from the 8-K
      EX-99.1 releases on file:

| Year | guidance, as issued | outturn | verdict |
|---|---|---|---|
| **2022** (2022-02-01) | GAAP EPS $10.10-10.70; adj. EPS $12.00-12.50; **free cash flow "approximate $2.0 billion"**; *"15% to 19% adjusted earnings per share growth"* | **free cash flow = OCF −$1,459.5M − capex $530.4M = −$1,989.9M** | **missed by about $4.0 billion on a $2.0bn guide** |
| 2023 (2023-02-02) | GAAP EPS ($1.65)-$0.85; FCF $0.5-1.0bn | GAAP EPS **($2.07)**; FCF $853M | GAAP below the bottom of the range; FCF inside |
| 2024 (2024-02-01) | GAAP EPS $1.60-2.85; FCF $0.6-0.8bn | GAAP EPS $1.96; FCF $753M | inside |
| **2025** (2025-02-05) | GAAP EPS **$4.05 (+/- $0.65)**; adj. $5.25 (+/- $0.50); FCF $750M (+/- $100M) — *"Excluding new tariffs"* | GAAP diluted EPS **$2.65**; FCF $688M | **GAAP 22% below the low end**; FCF inside; the caveat made the number unfalsifiable |
| 2026 (2026-02-04 → 2026-07-29) | GAAP $3.15-4.35 → **raised** to $4.60-5.45; adj. $4.90-5.70 → $5.20-5.80; **FCF $700-900M → $600-800M** | in progress | **EPS raised while FCF guidance was cut** — the refund lifts earnings, the CAM taxes and fees take the cash |

      *"About nine cases out of ten"* **[E3-48]**; *"the record of the people who made the
      projections"* — the 2022 guide was issued under CEO Jim Loree with Donald Allan Jr. as President and CFO
      (release of 2022-02-01); Allan was CEO through October 2025 and both are gone; Patrick Hallinan
      (CFO in the February 2024 release, after an interim CFO in February 2023) owns the 2024-26
      record, which is the better half.
- [x] **Serial share issuance [E5-15]** — fires as a pattern, not as a trend. Equity units issued
      **May 2017 and November 2019** (the November 2019 units settled into **4,723,500 shares** in
      November 2022); diluted count **148.2M (FY2016) → 165.0M (FY2021)**; then **$2.3bn of
      repurchases in Q1 2022** at a **blended ASR price of $143.18** (FY2022 10-K p. 3655); diluted
      count **151.9M (FY2025)**, cover **151,016,641 (2026-07)**. Ten-year net: roughly flat to
      slightly down. **Shares issued in 2017-2022 and bought back at $143 in 2022, against a quote
      of $89.24 today.** Plus a **2015 forward share purchase contract** for 3,645,510 shares at
      $350M plus a forward component, **settlement amended in September 2025 to June 2028** (10-K
      p. 41).
- [x] **EBITDA promotion [E4-29]** — **fires at full strength, in all three places.** (1) The
      10-K's multi-year goals: *"35% to 37% adjusted gross margins with mid to high-teens adjusted
      Earnings Before Interest, Taxes, Depreciation and Amortization margin"* (FY2024 10-K p. 588,
      FY2025 p. 593), with a stated refusal to reconcile: *"not available without unreasonable
      effort"* (FY2025 p. 647). (2) The releases: Q2 2026 headlines *"EBITDA margin\* was 17.4%, an
      increase of 1140 basis points"* — **an unadjusted figure carrying the quarter's $273.7M gain on the CAM sale and the tariff refund** (the adjusted figure was 11.3%). (3)
      **The pay: Adjusted EBITDA is 45% of the 2025-27 PSUs and 70% of the 2026-28 PSUs** (DEF 14A
      2026, stripped-text lines 1976, 1984). And the **bank covenant is Adjusted EBITDA to adjusted net interest,
      with up to $250,000,000 of permitted "Applicable Adjustment Addbacks"** (10-K p. 40). *"That's
      nonsense"* **[E4-29]**; *"higher borrowing power"* **[E5-41]** is exactly what the covenant
      definition buys.
- [ ] **Filed-figure tells [E4-30]** — checked, **do not fire**. Cash taxes paid (`IncomeTaxesPaidNet`)
      run **above** book pretax income in FY2022-25 ($483M, $415M, $352M, $330M against pretax of
      $38M, −$376M, $241M, $418M); the fraud tell is cash taxes falling as a share of pretax, and
      this is the opposite. Book effective rates of 3.2%, 3.5% and 3.8% (FY2020, FY2021, FY2025) are
      low, but cash taxes paid were $242M, $442M and $330M. Reported growth is anything but smooth.

**[E2-49] metric-switching — fires three times, and on the pay it fires after deterioration.**
(1) The DEWALT streak (Q2 section). (2) **The 2025-27 PSU replaced Relative Organic Sales Growth
(35%) with Adjusted EBITDA (45%)** — adopted after the 2023-25 PSUs paid **19.2%**, *"below threshold
performance for all metrics in 2023, 2024 and 2025 other than CFROI performance for 2023"* (DEF 14A
2026 line 575). (3) **The 2026-28 PSU abandons three-year goals: "performance goals for the core
financial metrics will be established annually for each year of the cycle and averaged"** — the
precise opposite of *"pre-set, long-lived and small bullseyes"* **[E2-49]**; CFROI replaced by ROIC.
The annual plan moved the same way: a Global Cost Reduction Program modifier (2023), replaced by an
adjusted gross margin modifier (2024-25), replaced by an organic sales modifier (2026), with adjusted
EPS weight raised 30% → 40% and free cash flow cut 40% → 30%.
**And in the humility clause's favour, recorded because [E4-26] requires it:** the pay responded to
the results. **2025 MICP paid 66.8%-72.3% of target; the 2023-25 PSUs paid 19.2%.** Say on Pay fell
to **~79%** in 2025 and the company says it met its top three dissenting holders. That is not a
management extracting pay from a failing business.

**[E4-52] — do the flags converge?** Four point one way: EBITDA as the covenant, the pay and the
public goal; long-lived goals replaced by annual ones after a 19.2% payout; the 2022 guide missed by
$4bn; and the tariff-refund gain partly paid out as *"directly attributable variable incentive
compensation"* (Q2 2026 10-Q Note O). **A reinforcing system around an adjusted-earnings number**,
read as such — but **not** a conduct finding.

### STEP 3 — THE PRIMARY TEST [E2-01], balance sheet first
Net income ÷ average equity (continuing operations where filed): **FY2014-17 ≈ 12-17%; FY2023 −3.0%,
FY2024 3.2%, FY2025 4.5%.** Unleveraged net tangible operating assets [E2-43]: **15.5%** pre-tax
(FY2025) — with the **goodwill wedge of $10.4bn reported separately**, which exceeds all of book
equity, so the ROE denominator is entirely purchased premium. **Fails the primary test** on every
recent year.

### THE HALF-OWNER TEST [E2-26]
**Passes in part.** The 10-K volunteers the SCF balances and rollforward, the receivables-sale
programme, the distribution-cost classification that flatters its own gross margin, and the
restructuring reserve by segment with the savings expected. **Fails in part:** DEWALT, the claimed
growth engine, is never quantified; the long-term goals are stated in non-GAAP terms with
reconciliation refused; and the headline EBITDA margin of Q2 2026 includes a one-time refund.

### RATIONALITY — CAPITAL ALLOCATION
**The institutional imperative [E2-30]:**
- [x] **(2) acquisitions soak up funds** — **$2,043.8M in FY2021** (MTD, Excel) at the top of the
      outdoor cycle; those brands (Troy-Bilt among them) were **impaired in FY2025** and gas
      walk-behind products **moved to licensing in 2026**.
- [x] **(3) studies for the craving** — a $2bn savings programme whose target (35%+ gross margin)
      was not reached when it was declared complete.
- [ ] (1) resisting change — no; the portfolio has been changed hard.
- [ ] (4) imitation — not established from filings.

**Buybacks [E5-08, E4-31, E4-50]:**
- **Q1 2022: $2.3bn at a blended $143.18, the $2.0bn ASR "funded through borrowings under one of its
  existing 364-Day committed credit facilities"** (FY2022 10-K p. 3655), **in the year operating
  cash was −$1,459.5M.** Condition (1), ample funds for operating and liquidity needs: **fails** —
  the year's operations consumed cash and the repurchase was borrowed. Condition (2), material
  discount: the stock is $89.24 today. **[E4-50]: "the discount does the licensing, never the
  borrowing"** — here the borrowing did the licensing. **CAPITAL-ALLOCATION FLAG**, with the
  humility clause **[E4-13, E5-08]**: management knew the business better in February 2022 than any
  outsider, and *"many CEOs never stop believing their stock is cheap."*
- **Q2 2026: $250M at about $78 (3.2M shares), funded from CAM proceeds after $1.7bn of debt was
  repaid.** Condition (1) is closer to met; condition (2) cannot be judged without a value this
  file does not reach.

**The dividend [E2-52, E2-60].** Cash dividends **$474.8M, $465.8M, $482.6M, $491.2M, $500.6M**
(FY2021-25), **$2,415.0M in five years**, raised every year ($3.22 → $3.26 → $3.30 per share,
FY2023-25). **Cumulative owner earnings over the same five years: −$44.7M at the capex end, +$12.7M
at the depreciation end** (`rebuild.py`). Over the same years SWK **sold businesses for $4,882.7M**
(FY2022 $4,147.1M, FY2024 $735.6M) and **raised total debt from $4,247M (FY2020) to $5,864M (FY2025)**.
**The dividend was not paid from issuance [E2-52], but it was paid from the sale of Security and
Infrastructure and from borrowing — restricted earnings in [E2-60]'s exact sense: payout that costs
"its financial strength".** Fires.

### THE GUARDRAIL
- [x] Nothing here promotes the name.
- [x] No great-manager dependence claimed.
- [x] The new CEO (October 2025, from Carrier) is not a plan this file can buy: **the franchise is
      not intact, so there is no excisable cancer [E2-36] — the manager would be the plan.**

- **VERDICT (recorded, not governing): IN on honesty (no disqualifier found) with a live
  CAPITAL-ALLOCATION FLAG** (borrowed 2022 buyback; dividend funded by divestitures and debt) and
  converging EBITDA flags. Would not stop the file on its own; Q2 already has.

## Q4 — WILL IT SURVIVE?

⚠️ **RECORDED, NOT GOVERNING.**

### THE DEFECT IN THE QUEUE'S NUMBER, FOUND BEFORE ANYTHING ELSE
**Both published ends reproduce to the dollar and they come from DIFFERENT WINDOWS** (`bands.py`):
`oe_bottom −179` is the **5-year FY2021-25 mean at the conservative end (−$179.1M)**; `oe_top 670` is
the **3-year FY2023-25 mean at the generous end (+$670.1M)**. **This is the INTC and BA defect for
the third time: the advertised spread is a window difference, not a capex band.** And a second defect
underneath it:

**THE SCREEN'S "D&A END" SUBTRACTS AMORTISATION OF ACQUIRED INTANGIBLES AS IF IT WERE MAINTENANCE
CAPEX.** SWK tags its PP&E-only line as `DepreciationDepletionAndAmortization` ($365.6M FY2025) and
separately `AmortizationOfIntangibleAssets` ($146.8M). `tools/run.py`'s component rule (added after
CGNX, 2026-09-07) sums `Depreciation` + `AmortizationOfIntangibleAssets` and, because the sum is
larger, **prefers $512.4M over the filed $365.6M**. [E3-44] names *"the depreciation charge"* as the
proxy for required capex; acquired-customer-list amortisation is a purchase-accounting charge that
[E2-23] item (b) adds **back**. **For an acquirer the screen's conservative end is overstated by the
whole intangible-amortisation charge — $146.8M to $203.1M a year here.** Fails safe in direction
(understates owner earnings), but it is not the corpus's (c). Reported, not fixed; see the defect list.

### Owner earnings — the one number **[E2-23]**, rebuilt (`rebuild.py`, `rebuild_out.txt`)
(c) ends from the filed statement: **PP&E depreciation** (the [E3-44] default) and **capital and
software expenditures**; SBC = the cash-flow add-back, subtracted in full **[E5-06]**.

**Owner earnings by year, as filed ($M):**

| FY | OCF | SBC | capex | PP&E dep | OE @dep | OE @capex | trade-WC cash (AR+inv+AP) | AP change | AP / OCF | dividends |
|---|---|---|---|---|---|---|---|---|---|---|
| 2015 | 1,182.3 | 67.9 | 311.4 | 219.2 | 895.2 | 803.0 | −105.7 | −9.7 | −1% | 319.9 |
| 2016 | 1,185.5 | 81.2 | 347.0 | 221.8 | 882.5 | 757.3 | −274.5 | 159.7 | 13% | 330.9 |
| 2017 | 668.5 | 78.7 | 442.4 | 253.6 | 336.2 | 147.4 | −968.2 | 240.4 | 36% | 362.9 |
| 2018 | 1,260.9 | 76.5 | 492.1 | 288.4 | 896.0 | 692.3 | −239.4 | 211.0 | 17% | 384.9 |
| 2019 | 1,505.7 | 88.8 | 424.7 | 325.2 | 1,091.7 | 992.2 | 106.4 | −169.1 | −11% | 402.0 |
| 2020 | 2,022.1 | 109.1 | 348.1 | 376.5 | 1,536.5 | 1,564.9 | −130.7 | 310.4 | 15% | 431.8 |
| **2021** | 663.1 | 118.3 | 519.1 | 374.0 | 170.8 | 25.7 | **−1,492.7** | **758.3** | **114%** | 474.8 |
| **2022** | **−1,459.5** | 90.7 | 530.4 | 369.7 | **−1,919.9** | **−2,080.6** | **−1,674.8** | **−991.4** | n/m | 465.8 |
| 2023 | 1,191.3 | 83.8 | 338.7 | 432.4 | 675.1 | 768.8 | +766.6 | −23.0 | −2% | 482.6 |
| 2024 | 1,106.9 | 105.4 | 353.9 | 426.3 | 575.2 | 647.6 | +324.5 | 173.3 | 16% | 491.2 |
| 2025 | 971.2 | 94.1 | 283.3 | 365.6 | 511.5 | 593.8 | +163.9 | −284.6 | −29% | 500.6 |

*(FY2009-14 are in `rebuild_out.txt`; FY2008 has no depreciation tag. Cross-checks: FY2025 OCF, SBC,
AP and capex match the filed statement to the dollar; FY2017 matches the FY2019 10-K's restated
column — $668.5M, AR −$905.6M, capex $442.4M.)*

**Every window.** 120 contiguous windows of three or more years × both (c) ends: **−$428.7M
(FY2021-23) to +$1,174.7M (FY2018-20)** — a **$1,603M width**. Trailing windows ending FY2025: 3y
**$587M to $670M**; 4y **−$40M to −$18M**; 5y **−$9M to +$3M**; 6y $253M to $258M; 7y $359M to
$377M; 10y $411M to $476M; 17y $491M to $563M. **The sign changes between the three- and four-year
windows**, which is the screen's "straddles zero" and the whole of the problem.

**WHICH YEARS DESCRIBE THE BUSINESS THAT EXISTS NOW — the choice, stated and justified.**
Three dated breaks, all from filings:
1. **2021-12-01 / 2021-11: MTD and Excel acquired** — the Tools & Outdoor perimeter that exists now
   starts in FY2022.
2. **2022-07-05: Security (CSS, MAS) sold** — FY2022's operating cash still contains half a year of
   Security. **The first full year of the current perimeter is FY2023.**
3. **FY2021-22 inventory build and FY2023-25 release are ONE working-capital cycle**: trade working
   capital consumed **$1,492.7M (FY2021) and $1,674.8M (FY2022)** and released **$766.6M, $324.5M,
   $163.9M (FY2023-25)**. **[E4-38]: a window that keeps the release and drops the build is "a
   calculated selection of … initial or terminal dates."**

**So no window is both inside the current perimeter and across the whole cycle — the perimeter starts
in FY2023 and the cycle in FY2021. That is the finding, and I publish both answers instead of
choosing between them:**

| window | as filed | cycle-neutral (trade-WC change removed) | why |
|---|---|---|---|
| **A. FY2023-25, current perimeter** | $587M to $670M | **$169M to $252M** | only years wholly inside today's perimeter; the as-filed figure counts **$1,255.0M of working-capital release** as earnings, which **[E4-41]** forbids |
| **B. FY2021-25, the corpus five-year default [E2-42], whole cycle** | **−$9M to +$3M** | $374M to $385M | contains build and release; contains half a year of Security; cycle-neutral figure assumes the $1,912.5M net build was "required", which it was not |
| C. FY2022-25 | −$40M to −$18M | $65M to $87M | first full MTD year; half-year Security |
| D. FY2015-19, the pre-shock business | $678M to $820M | $975M to $1,117M | a different perimeter (Security, Infrastructure, CAM, no MTD) and a different margin structure — **not the business that exists** |

**(c) judgment [E3-44], disclosed:** capex has run **below PP&E depreciation for three straight years**
(FY2023-25: $338.7M / $353.9M / $283.3M against $432.4M / $426.3M / $365.6M) during plant closures and
falling units. [E2-23] asks for what maintains *"its unit volume"* — and unit volume is falling — so the
capex end rewards shrinkage. **The depreciation end is the guess I would defend; the band is carried
as a display.**

**THE REBUILT RANGE, in dollars and a word:** **about −$10M to +$250M a year** — zero across the
five-year cycle (B, as filed), and $169M to $252M for the current perimeter once the one-time
working-capital release is stripped (A, cycle-neutral). **The word is THIN** — and at the $13,477M cap
even the top is a **1.87%** yield. The only construction that reaches $670M counts an inventory
liquidation as earnings. **Is the range too wide for a conclusion [E4-25]? In width, yes; in
direction, no — every defensible construction of the current business sits below the sovereign and
far below the floor.**

### THE PAYABLES PROGRAMME — what operating cash looks like without it
**The flag is FY2021, not FY2022:** accounts payable **+$758.3M against operating cash of $663.1M =
114%**. The two sides:
- **Without the AP line, operating cash was −$95.2M in FY2021 and −$468.1M in FY2022** (reported
  $663.1M and −$1,459.5M). **Across the two years the stretch and the unwind net to −$233.1M** — the
  payables did not manufacture cash over the cycle; **they moved roughly $750M of cash from FY2022
  into FY2021**, flattering the year the inventory was bought and deepening the year it went wrong.
  AP balances: **$2,320.0M (FY2020) → $3,438.9M (FY2021, as first filed) → $2,344.4M (FY2022) →
  $2,163.0M (FY2025) → $2,422.3M (2026-07-04)**.
- **The supply-chain-finance programme itself** (inside AP, disclosed only from FY2022 under ASU
  2022-04): **$607.5M (FY2022), $528.1M (FY2023), $483.6M (FY2024), $349.3M (FY2025), $422.9M
  (2026-07-04)**. Rollforward FY2025: additions $1,715.8M, payments $1,855.5M; FY2024: $2,111.5M and
  $2,153.3M — **$1.7-2.1bn a year, 16-20% of cost of sales, runs through it.** Its balance fell
  $258.2M over FY2023-25, so **it has been DEPRESSING reported operating cash**, by about **$79M,
  $45M and $134M**. **SCF-neutral operating cash: $1,270.7M (FY2023), $1,151.4M (FY2024),
  $1,105.5M (FY2025).** In H1 2026 the balance rebuilt by **+$73.6M**, which flatters the interim.
- **The prior — that the programme props up operating cash — is refuted for FY2023-25 and
  unresolvable for FY2021.** The FY2021 SCF balance is **not disclosed** (the ASU's retrospective
  requirement reached only one comparative year), so how much of the +$758.3M was SCF cannot be
  separated. **Source limit, not a work order: no filed document carries it.**
- **The 10-Qs do not split AP at all.** The condensed interim cash-flow statements show one line,
  "Changes in working capital" (Q2 2026 YTD −$106.7M; Q1 2026 −$388.8M), so the interim AP effect
  can only be inferred from the balance sheet: **AP +$259.3M in H1 2026** (includes the removal of
  CAM's payables). **The flag cannot be run on 10-Qs for this filer.**
- **And a seasonal dependence the annual figure hides:** Q1 operating cash was **−$420.0M (2025) and
  −$388.8M (2026)**, funded each year by **commercial paper of $1,136.2M and $1,145.4M**.
- **Separate structure, stated so it is not confused with the above:** a **$110.0M receivables-sale
  programme** (derecognised balance flat at $110.0M), neutral year to year; and the **earlier
  deferred-purchase-price programme**, terminated February 2018, whose $705M was reclassified out of
  FY2017 operating cash (Step 0).

### IS SBC RESOLVED AND COMPLETE?
- **Resolves every year FY2009-25** (`ShareBasedCompensation`, $13.9M-$118.3M); equals the equity
  statement's "Stock-based compensation" line FY2023-25 ($83.8M, $105.4M, $94.1M).
- **The Boeing defect does not apply from FY2020.** 401(k) match: *"Participants direct the entire
  employer match benefit such that no participant is required to hold the Company's common stock"*;
  **"The Company made cash contributions to the plan totaling $72.7 million in 2025"** (10-K Note K).
  The equity statement's only issuance lines FY2023-25 are option/RSU settlements (817,110 / 960,437
  / 921,552 shares, net $19.0M / $24.8M / $8.9M).
- **But it did apply before FY2020, in miniature.** FY2019 10-K Note L: the U.S. Core and 401(k) plans
  were **funded through the ESOP by releasing shares bought in 1991**: **133,694 shares at $138.60
  (2017), 207,049 at $139.45 (2018), 226,212 at $138.67 (2019) — about $18.5M, $28.9M and $31.4M** of
  stock paid to employees, **in no SBC tag**, against net cash contributions of only $6.6-9.4M; the
  last unallocated shares were released in Q1 2020. **Owner earnings FY2017-19 are overstated by
  roughly $12-22M a year** — immaterial to any verdict and outside windows A-C, but it is the BA
  class, and **no XBRL-side guard would see it.**
- **[E3-70] market value vs charge:** SBC/OCF is ~10% (FY2025); not the ARM/CALX shape.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · [x] **gruesome** — **$2,043.8M of acquisitions and a $1.9bn net working-capital
  build in FY2021-22 bought a business that has since earned about zero owner earnings over the cycle
  and a 5.0% pre-tax return on invested capital (FY2025).** *"Requires you to keep adding money at
  those disappointing returns"* — and the added money is now being taken back out by selling
  businesses.

### Staying power — score all three **[E5-11]**
- **(1) large and reliable earnings: NO.** Five-year cumulative owner earnings −$44.7M / +$12.7M; FY2022
  −$2.08bn; the 120-window width is $1.6bn.
- **(2) massive liquid assets: NO.** Cash **$280.1M, "primarily held in foreign jurisdictions"** (10-K p.
  40) against $5.86bn of debt at year end.
- **(3) no significant near-term cash requirements: NO, and this is the one that usually kills.**
  (a) **Commercial paper every first quarter** ($1.14bn in both 2025 and 2026) backstopped by bank
  facilities — *"the kindness of strangers"* **[E5-39]**; (b) **a covenanted interest-coverage test on
  Adjusted EBITDA, relaxed in June 2025 from 3.50x to 2.50x for periods through Q2 2026, with up to
  $250M of addbacks** — the covenant was loosened at the trough, and **the relief has now expired**;
  (c) **$500M a year of dividends**; (d) maturities **$554.5M 2026 (repaid), $1,100.0M 2028, $750.0M
  2030, $2,900.0M beyond**; (e) the **2015 forward share purchase contract, $350M plus forward
  component, June 2028**; (f) pensions under-funded by **$221.1M** (US $79.5M, non-US $111.0M, other
  post-retirement $30.6M) — small.
- **Leverage, named and quantified [E4-16]:** total debt $5,863.7M (FY2025) → $4,757.9M (2026-07-04) after
  CAM; interest paid **$531.5M, $479.9M, $520.6M** (FY2023-25). **[E2-54] coverage, gross interest,
  out of cash flow net of capex:** FY2025 (OCF + interest expense − capex) ÷ interest expense =
  **2.3x**; **across FY2021-25, cumulative 1.2x** (cumulative OCF $2,473.0M + interest $2,097M −
  capex $2,025.4M over interest $2,097M). *"Comfortably met out of current cash flow net of ample
  capital expenditures"* — **not met across the cycle. "Zip up your wallet."**

### THE TEN-YEAR SHARE COUNT
Diluted weighted: **159.7M (FY2014), 148.2M (FY2016), 152.4M (FY2017), 156.4M (FY2019), 165.0M (FY2021),
156.6M (FY2022), 149.8M (FY2023), 151.9M (FY2025)**; cover **151,016,641** (July 2026). **Net flat over
a decade — issued through equity units 2017-2022, retired by a borrowed $2.3bn buyback in 2022.**

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40]**
**The mechanism — a FIFTH shape, not any of the four:** not ORCL (no contracted spend it cannot stop),
not ARM (SBC is ~10% of operating cash), not BE (eighteen years are filed), not BA (the cash is not
going into undoing past work — though restructuring is an annuity). **SWK's shape is the
self-liquidating distribution: a business that earns about nothing across its cycle pays a rising
dividend and a borrowed buyback out of the sale of its own divisions, so that owner earnings never
have to carry the payout — until there is nothing left to sell.** The corpus has the name:
*"a company that consistently distributes restricted earnings is destined for oblivion"* **[E2-60]**.

**Quantified from filed figures, FY2021-25:** uses — dividends **$2,415.0M**, repurchases
**$2,411.2M**, acquisitions **$2,115.7M**, cumulative owner earnings **−$44.7M**; sources — divestitures
**$4,882.7M** (plus **$1,814.6M** for CAM in H1 2026), debt **+$1,617M**. **Every remaining divisible
asset outside Tools & Outdoor has now been sold except the rest of Engineered Fastening** ($1.97bn of
FY2025 sales less CAM's $413.9M). **The exposure, not the experience [E4-40]:** the next T&O downturn
arrives with ~$4.8bn of debt, a 3.50x Adjusted-EBITDA covenant back in force, a Moody's Baa3, $280M of
cash, a $500M dividend, Q1 commercial paper of $1.1bn, and no more Security to sell. **[E3-24]-style
arithmetic:** a repeat of FY2022 (OCF −$1,459.5M) against the H1 2026 balance sheet would require about
**$2.2bn of new borrowing in a year** (the FY2022 OCF shortfall of $1.46bn, ~$0.3bn of capex and the $0.5bn dividend) at a
rating one notch above junk.
**Likelihood: [x] a real possibility** that the dividend is cut or equity is issued in the next
downturn; **[ ] likely** insolvency — no: the maturity ladder is long, the 2026 maturity is paid, and
CAM cut debt by $1.7bn. **The business survives as a company; the owner's claim does not compound.**

- **VERDICT (recorded, not governing): OUT** — gruesome on [E4-20], zero of three on [E5-11], and
  [E2-54] not met across the cycle. **Would have closed the file if Q2 had not.**

---
⛔ **Q5 does not open. Q2 returned OUT.** What follows is required by the queue's output contract
and operator rule 3, and carries no entry language.

# COMPUTATION — NOT A CLEARANCE

**Inputs:** price **$89.24** (2026-09-11, aggregator, flagged) × **151,016,641** shares (Q2 FY2026 10-Q
cover, acc. 0000093556-26-000031) = **$13,477M**. Sovereign **5.35%** (US Treasury par curve, 30-year,
09/11/2026). Floor **~10% [E4-28]**. Growth engine `tools/run.py:implied_growth()` (ten-year fade to
2.5%) — an engine, not a voter **[E3-34]**; output in `growth_engine_out.txt`.

| owner-earnings base | yield on $13,477M | vs sovereign 5.35% | year-1 growth needed to earn the ~10% floor |
|---|---|---|---|
| **B. FY2021-25 whole cycle, as filed: −$9M to +$3M** | **≈ 0%** | −5.3 pts | **not a number** — refused on a non-positive base |
| **A. FY2023-25 current perimeter, cycle-neutral: $169M** | **1.25%** | −4.1 pts | **49.5%** |
| **A. same, top: $252M** | **1.87%** | −3.5 pts | **38.1%** |
| FY2025 alone, cycle-neutral, capex end: $430M | 3.19% | −2.2 pts | 23.6% |
| A. FY2023-25 as filed, top — **counts the $1.26bn inventory release as earnings**: $670M | 4.97% | −0.4 pts | 12.1% |
| D. pre-shock FY2015-19, as filed, top — **a perimeter that no longer exists**: $820M | 6.09% | +0.7 pts | 7.0% |
| the best of all 120 windows, FY2018-20 (contains the pandemic wave): $1,175M | 8.72% | +3.4 pts | −1.7% |

**What the buyer at $89.24 is paying for, in words.** Not the business that exists: every
construction of that business yields below the sovereign, and the defensible ones yield under 2%.
**The quote is a bet that Tools & Outdoor returns to its pre-2022 economics** — segment margin back
from 10.7% toward 15-17%, gross margin to the 35%+ the company promised for three years and did not
reach, and unit volume back above 2019 — **while Techtronic, which took units in 2025, stops taking
them, and while Home Depot and Lowe's let the savings stay home.** Even a full return to the
FY2015-19 owner earnings (a perimeter that no longer exists, with Security and CAM in it) yields
about 6%, around the bond and **below the ~10% floor**. **[E4-35]:** the normalised current perimeter
needs ~38-50% year-one growth to reach the floor; *"fewer than 10 of the 200 most profitable
companies"* sustain 15%. **The ceiling [E2-63]:** capped by a customer-administered price and a
competitor with net cash — upside requires capital the company is selling divisions to find.

**Value, as a round-number range [E4-01], computation only:** capitalising the rebuilt current-business
range **(about $0 to $250M)** at the ~10% floor with no growth gives **roughly $0 to $2.5bn**; at the bare
5.35% sovereign, **roughly $0 to $5bn**; the pre-shock business at the floor, **roughly $7-8bn**. **The
quote is $13.5bn — above every one of them.** Screamer test [E4-01]: the price is **above the whole
range** → *"no."* **Price: $89.24. PASS/FAIL: FAIL — Q2 OUT, on the business.**

## Q6 — WHAT WOULD PROVE ME WRONG? *(recorded; a Q2 OUT carries reversal conditions in words, not a price alert — the QLYS ruling of 2026-09-07)*

**The reversal conditions, each read off a filing, none inferable from a price:**
1. **Tools & Outdoor unit volume above the FY2019 level** — the `volindex.py` series back above 100 —
   **while price holds positive**: four quarters in which T&O volume and price both rise in the
   8-K EX-99.1 decomposition. That is [E2-44] half one passing on the volume leg, which it has not
   done in any quarter since Q2 2025.
2. **T&O EBIT margin within reach of Techtronic's on the same year** — adjusted T&O segment margin
   minus an allocated share of corporate overhead at or above TTI's reported EBIT margin (8.8% in
   2025) **for two consecutive years**, without tariff refunds.
3. **DEWALT's revenue and margin disclosed**, and showing the franchise the bull case asserts. A moat
   inside an undisclosed unit cannot be IN; a disclosed one could be.
4. **Consolidated gross margin at 35%+ GAAP** for a full year with no one-time items — the company's
   own objective, stated since 2022.
5. **Five-year cumulative owner earnings covering the dividend** — the [E2-60] test reversed: a
   trailing five-year window in which OE at the depreciation end exceeds cash dividends, with no
   divestiture proceeds in the window.

**The sell rule [E2-28]:** not applicable — nothing is held. **[E2-40]:** the view has crystallized on
filed facts; nothing here is a reason to watch the price.
- **VERDICT: not reached (file closed at Q2).**

---
## SELF-AUDIT
- [x] Questions answered in order; the file closed at the first non-IN (Q2 OUT). Q3, Q4, the
      computation and Q6 are headed RECORDED, NOT GOVERNING or COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the
      10-K; the moat class is NOT provisional (nine peers; foreign limits stated).
- [x] No UNRESEARCHED verdict issued. The two unobtainable items (FY2021 SCF balance; DEWALT revenue)
      are stated as **source limits**: no filed document carries either.
- [x] Step 0: the filing read with accession numbers; FY2025 OCF $971.2M cross-checked to the filed
      statement, plus SBC, AP change and capex; FY2017 restated OCF cross-checked to the FY2019 10-K.
- [x] Owner earnings on multi-year means; **every one of 120 windows** published by extreme, trailing
      windows listed, four named windows; (c) band disclosed as a judgment with the depreciation end
      preferred and the reason given.
- [x] Competitor row filled: nine peers, same construction as the ITW row, limits stated.
- [x] Sovereign for the earnings currency, from the issuing authority, dated, struck fresh.
- [x] Value stated as a round-number range, headed as computation.
- [x] One bar: the screamer test, conservative end, no margin added. **Windage count: one** — the
      cycle-neutral normalisation removes a favourable one-off [E4-41]; no conservatism is added
      elsewhere (the (c) choice is the corpus default, not windage).
- [x] Prices dated; the aggregator used for the live quote only and flagged.
- [x] **Errors of my own, corrected in place with dated notes rather than overwritten:** (1) I wrote
      that the Item 1.01 document "confirms" a credit agreement before opening it — opened afterwards,
      it does; (2) I described CAM as pending when it closed in April 2026; (3) my first
      `rebuild.py` summed XBRL working-capital changes with the wrong sign — caught against the FY2025
      statement before any figure reached this file; (4) my first `deal_note()` call passed a tuple.
- [x] Run committed to git by file name.

## REGISTER
- Verdict: [x] **OUT (about the business)** at **Q2**.
- **Four-verdict line: Q1 IN · Q2 OUT · Q3 not reached (recorded: IN on honesty, capital-allocation
  flag live) · Q4 not reached (recorded: OUT, fifth survival shape) · Q5 not opened · Q6 not reached.**
- **One line:** Stanley Black & Decker is a simple business its own 10-K says faces private-label
  substitutes sold by its two largest customers; it raised price in every tariff quarter and lost
  more units than it gained in price, ships ~6% fewer Tools & Outdoor units than in 2019, turned $2bn
  of claimed savings into $1bn less EBIT, ranks last of ten peers on EBIT margin (4.9% against
  Techtronic's 8.8% in the same stores), and across FY2021-25 earned about zero owner earnings while
  paying $2.4bn of dividends out of divestitures and debt. **Price $89.24; cap $13,477M; FAIL at Q2.**

- *Fold note, 2026-09-12:* the queue entry, the tier-3 strike and the narrative fold are committed together; no alert and no PORTFOLIO row (Q2 OUT, the QLYS ruling). A 5.7MB `facts.json` dump from this run was committed in `e7f2c42` and its staged removal was swept into the ACMR commit `83d56f7`; recorded, not rebased.
