# Company Run — Levi Strauss & Co. (NYSE: LEVI) — 2026-08-31
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`. Evidence pack, competitor row and every
accession: `Test Runs/_research 2026-08-26/LEVI evidence pack + competitor row (KTB-VFC-RL, Uniqlo-Zara gap).md`.

**Position context: NONE HELD. Fresh entry run.** ~$2,750 of taxable capital is earmarked
for a dividend payer that compounds.

**BIAS DECLARED, both directions, per operator rule 9 [E4-27].** Five apparel/consumer names
have now died at Q2 in this project (ETD, FLO, OXM, WEYS, COLM). A reflexive "apparel
therefore no" is as much a failure of judgment as a reflexive yes, and the incentive to
close this file fast is real. It is also true that the operator wants a name to graduate,
which is the opposite incentive. **The antidote applied [E4-26]: the hypothesis hunted
hardest is the one this file arrived believing — that a rising consolidated gross margin at
a DTC-transitioning apparel brand is channel arithmetic, not pricing power.** That
hypothesis is tested against the filed record in §Q2 and it substantially survives, but the
three facts that cut against it are carried in full, not buried. **A "no" is a fully
successful run, and so is a "yes."**

---
# STAGE 0 — THE FIVE-MINUTE ARTIFACT CHECK, REPORTED FIRST

## (a) THE CAP WAS AN ARTIFACT. THE SCREEN UNDERSTATED IT BY 10.2x.

**LEVI is dual class.** Class A (NYSE: LEVI, one vote) and Class B (Haas family and family
trusts, ten votes, **convertible 1-for-1 into Class A**). Economics are identical across the
classes; only votes differ. The cap must be computed on total economic shares.

From the **Q2 FY2026 10-Q cover, acc. 0000094845-26-000037**, as of 2026-07-01:

> "the registrant had **100,456,337** shares of Class A common stock… and **284,394,225**
> shares of Class B common stock… outstanding."

| | shares | cap at $21.29 |
|---|---|---|
| Class A only, current | 100,456,337 | $2,138.7M |
| **TOTAL ECONOMIC SHARES** | **384,850,562** | **$8,193.5M** |
| what the screen used | **37,602,843** | **~$801M** |

**The screen was not using Class A alone. It was worse than that.** It used the **2018 10-K
cover count, dated 2019-01-30 — pre-IPO, pre-split, single class.** XBRL
`dei:EntityCommonStockSharesOutstanding` for CIK 0000094845 has 30 rows and **the last one is
2019-01-30**; after the March 2019 IPO the tag became dimensioned by Class A / Class B member
and the `companyfacts` API drops dimensioned facts. Any screen reading that tag inherits a
seven-and-a-half-year-old number from before the company was public.

And that number is pre-split. From the IPO prospectus (**Form 424B4, 2019-03-21,
acc. 0001193125-19-082264**):

> "the completion of the **ten-for-one stock split** of our common stock that became
> effective on **March 4, 2019**"

37,602,843 × 10 = 376,028,430, plus 9,460,557 primary IPO shares and seven years of net
stock-compensation issuance less buybacks = 384,850,562 today.

**Reconciliation: 37,602,843 × $21.30 = $800.9M. The screen's $801M is exact.**
**Ratio: 384,850,562 ÷ 37,602,843 = 10.2346. The screen captured 9.8% of the company.**

This is precisely the failure `CLAUDE.md` names as the fix for the four voided backtests:
*"cap = close(anchor) × shares(measurement) × splits AFTER measurement."* **The ten-for-one
split happened after the measurement date and was never applied.**

**Every downstream yield in this run uses $8,193.5M.**

**Third occurrence of a dual-class cap error in this project** — RMR priced a class with no
economic interest; CHWY's Class A alone understated its cap by 43%; **LEVI is understated by
a factor of ten and by a different mechanism: a stale, pre-split cover tag that XBRL stopped
updating at the IPO.** Any dual-class filer whose cover tag went dimensional at IPO carries
the same trap. *(Observation only. `Screens/` and `tools/` were not edited, per the
instruction.)*

## (c) THE STATUTE YIELD WAS THE CAP FIRST AND THE BOOM SECOND.

The screen's **26.3%** statute yield ÷ 10.2346 = **2.57%** — below the 5.19% sovereign,
before any other correction. This run's independent owner-earnings computation lands at
**2.9% to 4.0%**, confirming it.

The boom is also in the window and is named [E4-41]. FY2021 ROE 37.3%, FY2022 31.9%; FY2021
gross margin rose 530bp **while the DTC mix fell three points** — full-price selling with no
promotional cadence, the boom undisguised. Then the hangover: inventory $898.0M → $1,416.8M
in FY2022 and OCF collapsing $737.3M → $228.1M. Two further one-offs are named and one is
stripped: FY2024 OCF includes **~$87.1M** of upfront third-party-logistics payments recorded
in operating cash flow (stripped from the mean below), and FY2024 was a **53-week year**
worth **~$78M, or 1.3%,** of revenue (flagged).

**THE ENTIRE SCREEN ENTRY WAS AN ARTIFACT.** LEVI never belonged on a high-statute-yield
list. Corrected, it is a low-yield name. **The run continues on corrected numbers, because
the operator asked for a verdict on the business, not on the screen.**

## (b) THE DIVIDEND — regular, never special; the record is short and it was interrupted.

All declarations are regular quarterly (or, before 2020, a single annual declaration). **No
special dividends found** in the filings read.

| FY | Q1 | Q2 | Q3 | Q4 | year | note |
|---|---|---|---|---|---|---|
| 2019 | 0.29 | 0 | 0 | 0.01 | 0.30 | IPO year; annual-style |
| 2020 | 0.08 | 0.08 | **0** | **0** | **0.16** | **two quarters skipped outright** |
| 2021 | 0.04 | 0.06 | 0.08 | 0.08 | 0.26 | **restarted at half the pre-COVID rate** |
| 2022 | 0.10 | 0.10 | 0.12 | 0.12 | 0.44 | |
| 2023 | 0.12 | 0.12 | 0.12 | 0.12 | 0.48 | |
| 2024 | 0.12 | 0.12 | 0.13 | 0.13 | 0.50 | |
| 2025 | 0.13 | 0.13 | 0.14 | 0.14 | 0.54 | |
| 2026 | 0.14 | 0.14 | **0.16** | 0.16e | 0.60e | raised 14% July 2026, ~$62M/qtr |

**Growth, every window published [E4-38]:** FY2020→FY2025 **27.5%** (the headline);
FY2021→FY2026e 18.2%; **pre-COVID run-rate ($0.32 annualized) → FY2026e: 11.0%**;
FY2019→FY2026e 10.4%; FY2022→FY2026e 8.1%; **FY2023→FY2026e 7.7%.** The prior pass's +26.4%
and +21.3% reproduce against the FY2020 and FY2021 bases. **Both are artifacts of a base year
in which half the year's dividends were not paid.**

**What this record can support:** seven years of payment as a public company and a real
recent trajectory of 7-8% growth.
**What it cannot support:** any claim of a dividend policy with a record. The 10-K says so
itself — *"In the absence of a dividend policy, we will continue to evaluate and consider
declaration of dividends on a quarterly basis."* There is one precedent under stress and it
was to skip two quarters and restart at half.

### The decomposition, as tasked

DPS = payout ratio × EPS; EPS = earnings ÷ shares. Log-contributions:

| window | ΔDPS | from earnings | from share retirement | **from payout expansion** |
|---|---|---|---|---|
| FY2021 → FY2025 | ×2.077 | 5.9% | 3.4% | **90.7%** (payout ×1.940) |
| FY2022 → FY2025 | ×1.227 | 7.7% | 5.0% | **87.4%** (×1.196) |
| FY2019 → FY2025 | ×1.800 | 65.0% | 3.6% | 31.4% (×1.203) |

**Share retirement contributes almost nothing in any window.** Diluted shares are *higher*
than at the IPO (388.6M FY2018 → 399.7M FY2025) because stock compensation offset the
buybacks; only in the last two years has the count genuinely fallen (390.4M at FY2025
year-end → 384.9M at 2026-07-01, via the $120M and $200M ASRs).

### Cash dividends as a share of owner earnings — then vs now

| | dividends | OE (c = D&A) | OE (c = total capex) | payout of OE |
|---|---|---|---|---|
| **FY2019** | $113.9M | $233.1M | $181.6M | **49% – 63%** |
| **FY2025** | $212.9M | $241.7M | $226.6M | **88% – 94%** |
| **forward run-rate** | ~$246M | $241.7M | $226.6M | **102% – 109%** |

**The dividend has gone from roughly half of owner earnings to all of it.** That is the
arithmetic behind "90% of the growth was payout expansion," stated in cash.

**But the [E2-52] and [E2-60] flags do NOT fire, and the honest reason matters.** FY2025
distributions ($212.9M dividends + $150.5M repurchases = $363.4M) exceeded adjusted free cash
flow ($308.2M), and the 10-K discloses that the ASR upfront was funded from the Dockers sale
proceeds. Yet **net debt fell $309.5M → $190.4M**, no shares were issued, and cash rose.
Financial strength improved while paying out — the opposite of the OXM pattern. The narrower
honest statement: **the incremental FY2025 payout came from selling a business.**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · 2026-08-27 · FRED `DGS30`** (`fredgraph.csv`, the project's standing
  USD source; the known 1-2 day lag is noted and immaterial). LEVI reports in USD; 57% of
  net revenues are international, so translation risk is real and is disclosed at every line,
  but the reporting and earnings currency is USD and no FX conversion is required.
- **Price: $21.29, NYSE close 2026-08-28** (Yahoo — aggregator, live quote only, **flagged**).
  Intraday 2026-08-31: $20.86. 52-week range $17.72–$25.70. The verdict below is identical at
  either price.
- **Market cap: 384,850,562 × $21.29 = $8,193.5M** (see Stage 0). Net debt ~$190M → EV ≈ $8.4bn.

**The filing was read — not tagged data [E3-27]:**
- **Form 10-K FY2025 (year ended 2025-11-30), filed 2026-01-28, acc. 0000094845-26-000008**
  — [x] MD&A (results, channel and segment tables, gross-margin drivers, SG&A detail,
  liquidity and capital-allocation priorities, cash-flow discussion, non-GAAP definitions)
  [x] cash-flow statement including its detail lines [x] footnotes (Note 2 discontinued
  operations; Note 9 debt and the Credit Agreement covenants; leases; equity compensation;
  Beyond Yoga impairments; supplier finance; Item 3 legal; Item 5 buyback table; Item 1
  sourcing and competition). Auditor **PricewaterhouseCoopers LLP**, unqualified opinion
  including ICFR; one critical audit matter (the annual Beyond Yoga trademark impairment
  assessment).
- **Form 10-Q Q2 FY2026 (quarter ended 2026-05-31), filed 2026-07-08, acc. 0000094845-26-000037**
  — cover share counts, channel tables, gross-margin drivers, the IEEPA tariff note.
- **DEF 14A filed 2026-03-11, acc. 0001308179-26-000050** — beneficial ownership, related-party
  transactions, Summary Compensation Table.
- Earnings 8-K Ex-99.1 read for the guidance record: **2024-01-25** (acc. 0000094845-24-000011),
  **2025-01-29** (acc. 0000094845-25-000006), **2026-01-28** (acc. 0000094845-26-000009),
  **2026-04-07** (acc. 0000094845-26-000021), **2026-07-08** (acc. 0000094845-26-000038).
- Prior 10-Ks for the multi-year series: FY2024 acc. 0000094845-25-000005; FY2023 acc.
  0000094845-24-000010; FY2021 acc. 0000094845-22-000010; 2018 acc. 0000094845-19-000006.
  IPO prospectus 424B4 acc. 0001193125-19-082264 (the ten-for-one split).
- **Figure cross-checked against the filed statement:** FY2025 operating cash flow. The filed
  Consolidated Statements of Cash Flows reads **"Net cash provided by operating activities
  529.6"**; the MD&A cash-flow table carries **$529.6 million**; XBRL `companyfacts` carries
  **529,600,000**. Three-way match. Second check: net revenues **$6,282.0M** identical in the
  filed income statement and the Q4 FY2025 press release.
- **52/53-week flag:** **FY2024 was a 53-week year** (ended 2024-12-01), benefiting net revenues
  by **~$78M, or 1.3%**. FY2023, FY2025 and FY2026 are 52 weeks. Flagged wherever it bears.
- **Discontinued operations flag:** Dockers was classified as held for sale at the end of Q1
  FY2025 and is reported as discontinued operations **for all periods presented from FY2023
  forward**. FY2022 and earlier figures include Dockers. Every comparison below states which
  basis it uses.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.** Levi Strauss owns a
trademark on a garment it invented in 1873 and sells that garment two ways. It designs jeans
and denim-adjacent apparel, has essentially all of it cut and sewn by independent contract
manufacturers in about 32 countries (no more than 30% from any one), and then either
(a) sells it wholesale into roughly 50,000 third-party retail doors — 51% of FY2025 revenue,
48% in H1 FY2026, with the top ten customers 24% of revenue and none above 10% — or
(b) sells it itself through 1,231 company-operated stores in 38 countries, about 500
company-operated shop-in-shops, and levi.com — 49% of FY2025 revenue and 52% in H1 FY2026.
It also licenses the trademark for royalties, and it owns Beyond Yoga (2% of revenue,
loss-making).

The two channels have different economics and this is the whole of the accounting story:
DTC carries a structurally higher gross margin and a structurally higher selling cost.
FY2025 consolidated: gross margin **61.7%**, SG&A **50.5%** (selling 21.7%, advertising 7.0%,
distribution 7.3%, other 14.5%), operating margin **10.8%**, adjusted EBIT margin 11.4%.
Levi's-branded product is **94% of revenue**; denim bottoms are **64%** and everything else
36%. 57% of revenue is earned outside the United States. Capital intensity is modest —
capex $221.4M on $6,282.0M of revenue, **3.5%**, against D&A of $206.3M — with the real
capital commitment sitting in leases ($1,449.6M undiscounted, 6.7-year weighted term) and
inventory ($1,237.7M).

**The scarce input this business controls:** the Levi's trademark and the associated trade
dress — the 501, the Arcuate Stitching Design, the Tab Device, the Two Horse Design — more
than 5,100 trademark registrations and applications in about 190 jurisdictions, with
approximately 370 infringement matters being pursued. That is the only proprietary asset.
Manufacturing is rented, cotton is a commodity, the stores are leased, and the distribution
centers are now run by third parties.

**Will the fundamentals look broadly the same in ten years?** Yes. People will buy denim
bottoms; a brand will command a premium or it will not; a mix of wholesale and owned retail
will carry them. What is genuinely open is **share and realized price**, not mechanism. That
is a Q2 question, not a Q1 one.

- **VERDICT: [x] IN** — relatively simple and stable in character [E3-31]. Nothing here
  required five months of study; the model is legible from one 10-K.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [x]** — demonstrably, at premium prices, for 150+ years, and the filed
  record shows the premium being *increased* while units grow (below).
- **Not price-regulated [x]** — no price regulation. But note the asymmetry: the *cost* base
  is administered by tariff policy, which is the mirror image and is treated at Q4.
- **No close substitute — this is the contested criterion, and the company itself argues
  against it.** From Item 1: *"The global apparel industry is highly competitive and
  fragmented. It is characterized by **low barriers to entry**, brands targeted at specific
  consumer segments, many regional and local competitors, and an increasing number of global
  competitors."* That is management stating that its own category has low barriers. A pair of
  jeans has close substitutes at every price point, and holding the preference costs
  **$437.0M a year, 7.0% of revenue,** in advertising — a Beyoncé campaign run across two
  fiscal years.

**THE CRUX, RESOLVED FROM THE FILED SERIES: is the rising gross margin MIX or PRICING?**

LEVI never quantifies the mix component in any filing read; it names the drivers and
quantifies only currency. So it has to be solved. Every figure below is as reported in that
year's own 10-K.

| FY | DTC % of net revenues | gross margin | the 10-K's own attribution |
|---|---|---|---|
| 2021 | 36% | 58.1% | *(mix fell 3pts, margin rose 530bp — the boom)* |
| 2022 | 38% | 57.5% | |
| 2023 | 43% | **56.9%** | "**increased product costs and lower full priced sales**, partially offset by favorable channel mix"; FX +20bp |
| 2024 | 46% (47% ex-Dockers) | 60.0% (60.6% ex-Dockers) | "**lower product costs and favorable channel and brand mix**"; FX −50bp |
| 2025 | 49% | 61.7% | "favorable channel mix, **price increases**, and lower product costs, partially offset by the impact of tariffs"; FX +40bp |
| H1 2026 | 52% | **62.3%, flat YoY** | "**pricing actions** and lower product costs and the **unfavorable impact of tariffs**"; FX +10bp |

**Window A, FY2021 → FY2024** (both as reported, both including Dockers): DTC **+10 points**,
gross margin **+190bp**. The DTC-minus-wholesale gross-margin spread that would make channel
mix explain **100%** of the move is 190 ÷ 10 = **19.0 points** — an entirely ordinary apparel
channel spread. **On that window nothing beyond channel mix is needed to explain the whole
gross-margin gain.** *(Judgment, disclosed: the 19.0 points is solved for from LEVI's own
series under the null "all mix," not assumed. Sensitivity: at a 15-point spread mix explains
150 of the 190bp; at 25 points it over-explains.)*

**Window B, FY2024 → FY2025** (ex-Dockers): DTC +2 points → mix ≈ **+38bp**; currency,
company-disclosed, **+40bp**; actual **+110bp**; residual for price + lower product cost −
tariffs ≈ **+32bp**.

**Window C, H1 FY2026:** DTC +1 point → mix ≈ **+19bp**; currency **+10bp**; actual **0bp**;
residual ≈ **−29bp**.

**FINDING: the consolidated gross-margin expansion is overwhelmingly channel mix, and it
stops when the mix contribution shrinks.** DTC is already 52%. Each further point buys ~19bp.
**Management guides FY2026 gross margin to +10 basis points.** Anyone extrapolating the
FY2024-25 margin trend is extrapolating an arithmetic that has nearly run out.

**And the competitor row makes the same point from outside.** LEVI's 61.7% gross margin next
to Kontoor's 45.2% reads as brand power and is mostly channel structure — LEVI is 49% DTC,
Kontoor 15.2%. **At the segment operating line, before corporate expense, Wrangler runs 23.0%
and Levi's Brands runs 20.2%** (Americas 21.9%, Europe 21.6%, Asia 13.1%). **The direct denim
comparator's flagship brand is more profitable per revenue dollar than Levi's is.** That is
the most disconfirming filed fact in this file and it is stated as its advocate would state
it [E4-51].

**THE THREE FACTS THAT CUT THE OTHER WAY, hunted and carried [E4-26]:**

1. **Price and volume rose together** in H1 FY2026, in both channels. Americas: *"Wholesale
   revenues increased primarily due to an increase in volumes, with higher sales of Levi's
   women's products. DTC and wholesale revenues also benefited from price increases."* Asia:
   *"The increase in wholesale revenues was primarily due to an increase in units sold."*
   DTC comparable sales **+7% (Q1), +6% (Q2)**; e-commerce +19-21%. **Raising realized price
   while units grow is stronger evidence than [E2-44] asks for** — the test is price rises
   *with demand flat*; here demand is not flat.
2. **The tariff shock was passed through.** ~$80M of IEEPA tariffs paid through Q1 FY2026,
   and gross margin still rose 110bp in FY2025 and held flat in H1 FY2026. **The [E4-37] agony
   metric reads: agony in FY2023 (cost inflation eaten, "lower full priced sales"), no agony
   in FY2025-26.** That is a two-year improvement, not a decade of pricing power — but it is
   exactly the test OXM failed and LEVI passed.
3. **Levi's is taking share from the direct comps.** Organic +7.2% (FY2025) and +7.5% (H1
   FY2026) against Wrangler ~+4% organic, **Lee −5.1% in its third straight down year**, and
   VF Corp 19% below its FY2022 peak.

**Against those, two facts that must not be laundered.** First, **"lower product costs" appears
in the FY2024, FY2025 and H1 FY2026 attributions** — an exogenous input tailwind (cotton,
freight), and **[E4-41] instructs that it be named and not credited to the moat.** Second,
**Europe's organic net revenues went NEGATIVE in Q2 FY2026 (−0.8%)** — the company attributes
it entirely to a prior-year shipment shift from the Dorsten distribution-center transition, and
the six-month figure is +4.7%, but it is the first negative organic segment print in the
current run and it belongs in the Q6 watch list rather than in a footnote.

**[E4-55] units vs dollars — the gap, named.** **LEVI files no total unit-volume series
anywhere in the filings read.** It files unit *mix* (pants 67%/66%/67% of total units sold
FY2025/24/23; tops 29%/28%/27%) and qualitative volume language. The closest physical proxies
are DTC comparable sales and the store count (1,231; 110 opened and 70 closed in FY2025). One
Precision-Steel-pattern instance exists in the record — **FY2025 Asia wholesale, "a decrease
in units sold offset by an increase in average revenues per unit"** — and it reverses in H1
FY2026. **No document in the filed record resolves total units; this is a disclosure gap, not
an unperformed retrieval, and it is the single most useful number LEVI does not publish.**

**[E2-44] two-characteristic test: 1.5 of 2.**
1. *Raise prices with demand flat and capacity not fully utilized?* **Pass, in the stronger
   form** — price up with volume up, in both channels, through a tariff year.
2. *Grow dollar volume with only minor additional investment of capital?* **Partial.** Capex
   is 3.5% of revenue against D&A of 3.3% — genuinely modest. But the growth is bought with
   110 store openings a year, a rising working-capital base (inventory $898.0M in FY2021 →
   $1,237.7M in FY2025), and $437M a year of expensed advertising. Cumulative capex exceeded
   D&A by **$329.6M over FY2021-25** (~$66M a year). The capital is modest but it is not
   trivial and it is what separates the cash view from the accrual view at Q5.

**[E4-04] continuously rebuilt?** **No — and this is where LEVI genuinely differs from the
excluded class.** The advertising defends the *same* trademark; it does not buy a replacement
asset. That is the Coca-Cola case [E5-23, E3-49], not the Rhodes Ridge case. The 501 is 136
years old and has never needed replacing. [E4-04] does not disqualify.

**[E2-45] attacker's test.** With ample capital and skilled personnel: **you cannot attack the
trademark** — nobody else may sell a 501 or an Arcuate, and the company pursues ~370
infringement matters to keep it that way. **You can attack the category**, and the world does:
vertically integrated specialty retailers, private label, fast fashion, and every athleisure
brand sell denim bottoms. The filed answer to the attack is the share record above — LEVI is
currently winning against the direct comps and losing to nobody visible in the pulled rows.

**[E2-53] dominance class.** The 10-K claims *"the #1 brand globally in jeanswear (measured by
total retail sales)."* Self-reported, but supported at scale by the row: LEVI $6,282.0M
against Wrangler $1,914.6M plus Lee $750.4M combined.

**[E3-33]/[E5-28] untapped pricing power: NO.** Claiming that class claims near-monopoly, and
the row does not support it. LEVI is taking price and it is landing, but taking price in a
tariff year is cost recovery, not untapped power.

**[E5-35] the retailer-versus-brand struggle: structurally improving.** Top ten wholesale
customers 27% → 25% → 24% of revenue; no customer at 10%; wholesale 51% and falling. The DTC
shift is exactly the move that reduces the retailer's leverage over the brand.

**[E4-32] direction: WIDENING, from a low base, by a finite mechanism.** Adjusted EBIT margin
9.0% (FY2023) → 10.2% → 11.4% → guided 12.0%; two consecutive up revenue years; share taken
from the direct comps. But the widener has been channel mix and mix is nearly spent.

**[E4-23] the Mayo test, recorded HERE at Q2 as a moat matter, not at Q3 as a compliment.**
The trademark endures and would endure under a mediocre CEO — it has survived 170 years and
three restructurings (2014, 2020, 2024) and you need not know who runs it. **But the
economics being extrapolated today are two years old and coincide exactly with one CEO
(Michelle Gass, President January 2023, CEO January 2024) and one program (Project Fuel).**
**Recorded as a moat defect: the moat is the trademark and it is durable; the returns being
priced are an execution record two years long.**

### THE COMPETITOR ROW — required [E3-28]
*(Full row with accessions and Kontoor's brand-level detail in the evidence pack.)*

| Company | fiscal year end | net revenue | gross margin | operating margin | DTC % | revenue trend |
|---|---|---|---|---|---|---|
| **LEVI** | 2025-11-30 | **$6,282.0M** | **61.7%** | **10.8%** (adj EBIT 11.4%) | **49%** | +4.1% reported, **+7.2% organic**; 2nd consecutive up year |
| Kontoor (KTB) | 2026-01-03 (53wk) | $3,152.5M | 45.2% | 10.7% | 15.2% | +20.9% but **acquisition-driven**: Wrangler +6.0% (incl ~2pt 53rd wk), **Lee −5.1%** (3rd down year), Helly Hansen $459.7M new |
| VF Corp (VFC) | 2026-03-28 | $9,605.2M | 54.8% | 6.0% | n/d | +1.1%; **−18.9% below the FY2022 peak** |
| Ralph Lauren (RL) | 2026-03-28 | $8,114.5M | **69.9%** | **14.5%** | n/d | **+14.6%, record** |

- **Peers named: 3 of roughly 6-8 real public comparators.**
- **Gaps named with routes (UNRESEARCHED work orders, not load-bearing):** **Fast Retailing
  (Uniqlo)** — foreign private issuer, no EDGAR; route is the TSE/TDnet annual securities
  report and the English IR site (evidence-ladder rung 4). **Inditex (Zara)** — foreign private
  issuer; route is the CNMV/BME annual report, English version on the IR site (rung 4).
  **Shein** — private, no route. **Abercrombie, American Eagle, Gap** — US filers, EDGAR,
  ordinary retrieval; not pulled, and they are channel comps rather than brand comps.
- **Effect on the class, stated honestly:** the missing rows are **the reason the class is held
  at NARROW rather than WIDE.** They could show global category share moving to fast fashion.
  They cannot overturn LEVI's own realized units-and-price record, which is the deciding
  evidence and which comes from the subject's own filings. **The class is therefore not marked
  PROVISIONAL, and this gate does not carry a provisional caveat.**
- **Row limit stated [E3-61]:** the row shows position, not conduct. Kontoor's Wrangler margin
  advantage says nothing about how either management behaves next year.

- **Class: [x] NARROW** — one genuinely unattackable trademark inside a category with, in the
  company's own words, low barriers to entry. · **Direction: WIDENING on execution, by a
  mechanism (channel mix) that is nearly spent.**
- **VERDICT: [x] IN.** Under [E3-03] the operative evidence for what customers think is what
  they do, and what they did in FY2025 and H1 FY2026 was **pay a price increase and buy more
  units, in both channels, through a tariff shock, while the direct denim comparators shrank.**
  That is not the OXM pattern (three down years at a growing store count, promotional cadence
  rising, margin falling); it is close to its opposite. **It is NARROW, not WIDE**, because the
  category has close substitutes by management's own account, because the margin expansion is
  mostly channel arithmetic rather than pricing power, because the direct comparator's
  flagship brand earns a higher segment operating margin, and because the record being
  extrapolated is two years long. **A narrow moat is enough to continue; it is not enough to
  pay for.** [E5-13] noted: most names should end here, and this one does not — which raises
  the burden on the questions that follow, not lowers it.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`.*

**STEP 1 — THE WEIGHT CASE, DECLARED FIRST.**
- [x] **Daily execution [E3-38] — TICKED.** This is Buffett's own worked example class:
  **1,231 company-operated stores in 38 countries**, ~500 shop-in-shops, seasonal fashion
  buying committed months ahead, a sourcing footprint across 32 countries under a tariff
  regime that changed twice in eighteen months, and a live third-party-logistics transition
  the 10-Q itself says *"has and may continue to cause interruptions… shipping delays, order
  cancellations and increased costs."* *"For a retailer, hiring that nephew would be an
  express ticket to bankruptcy."*
- [ ] **Control [E1-16] — NOT ticked, but recorded.** This is a marketable minority and I can
  exit. However: **Class B is 96.5% of total voting power** (286.8M shares × 10 votes against
  103.6M Class A votes), every disclosed >5% holder is a Haas family member or family fund,
  and the 10-K states the consequence itself — *"these stockholders could cause our company to
  take actions that are at odds with the investment goals or interests of institutional,
  short-term or other non-controlling investors"* and *"we might be a less attractive takeover
  target."* **As a Class A holder I would own economics with no vote and no takeover option.
  That binds position size; it does not tick the gate, because the exit exists.**
- [ ] **Leverage [E3-29] — NOT ticked.** $1,039.2M of debt, **100% fixed rate, unsecured, no
  maturity before August 2030**; $848.8M of cash and short-term investments; net debt ~$190M;
  the $1.0bn revolver undrawn to November 2029.
**One determinant high → Q3 is a BINARY GATE. No price compensates [E3-29, E5-35].**

**Honesty — the binary [E5-16]: no integrity disqualifier found.** The sweep, named: FY2025
10-K Item 3 Legal Proceedings (ordinary-course claims only — *"We do not believe any of these
pending claims, complaints and legal proceedings will have a material impact"*); PwC
unqualified opinion including ICFR with one critical audit matter (Beyond Yoga trademark);
no restatement found in the filings read; DEF 14A related-party section shows only the 2019
registration rights agreement, standard indemnification agreements, and a **$5.7M donation to
the Levi Strauss Foundation** (on whose board the CEO, the General Counsel and a director
sit) — the proxy states there were no other transactions above the $120,000 threshold.
**Worded per the absence-claim rule: no instance found in the documents read, not "none
exists."**

**STEP 2 — THE FLAGS.**
- [ ] **Weak accounting [E4-22] — not fired.** SBC expensed in full ($81.6M). Impairments taken
  at the annual test rather than deferred. And a candor positive: the FY2025 10-K **volunteers**
  that the Beyond Yoga reporting unit's and trademark's fair values were *"less than 10% over
  their carrying values"* — an explicit near-miss disclosure most filers omit [E2-26].
- [ ] **Unintelligible footnotes [E4-22] — not fired.** Channel, brand, geography, segment,
  lease, debt and supplier-finance detail all legible.
- [x] **Trumpeted projections [E4-22] — FIRED**, and the **[E3-48] action taken: the record of
  the people who made the projections was pulled and scored.**

  | FY | initial guide (January) | outturn | score |
  |---|---|---|---|
  | 2024 | reported revenue **+1% to +3%**; adj diluted EPS **$1.15-$1.25** | +3%; **$1.25** | **met, top of range** |
  | 2025 | reported **(1)% to (2)%**; organic **+3.5-4.5%**; adj EBIT margin **10.9-11.1%**; adj EPS **$1.20-$1.25** | organic **+7.2%**; adj EBIT **11.4%**; adj EPS **$1.34** | **beat all three** |
  | 2026 | reported **+5-6%**; organic **+4-5%**; GM **flat**; adj EBIT **11.8-12.0%**; adj EPS **$1.40-$1.46** | raised at Q1 and again at Q2 to **+7.0-7.5% / +5.5-6.0% / GM +10bp / 12.0% / $1.46-$1.52** | in progress; **raised twice** |

  **This is the inverse of the OXM record.** The flag fires on the *practice* — standing
  quarterly guidance, plus Item 1's long-term targets of *"approximately $9 billion to $10
  billion in total company net revenue"* and *"Adjusted EBIT margins to approximately 15%"*,
  which is the [E4-35]/[E5-30] ratchet class exactly. **The behaviour is a ratchet whichever
  way the numbers come out; the record so far is good.**
- [x] **EBITDA / adjusted-metric promotion [E4-29] — FIRED.** **Adjusted EBITDA was added to
  the non-GAAP suite in the FY2025 10-K**, defined there as *"Adjusted EBIT excluding
  depreciation and amortization expense"* — the exact deletion [E4-29] calls *"a particularly
  pernicious practice"* and [E5-41] calls reverse float. Guidance is given on **Adjusted EBIT
  margin**, not GAAP operating margin. Three headline income figures coexist for FY2025: GAAP
  total $578.1M, GAAP continuing $502.0M, adjusted $537.1M. **The owner-earnings computation
  below runs off cash and therefore charges every excluded item [E5-33].**
- [x] **Metric-switching [E2-49] — FIRED, mildly.** In January 2025, with **reported** revenue
  guided to **−1% to −2%**, the company *"introduc[ed] organic net revenue guidance to better
  reflect the underlying growth of the company."* The new yardstick arrived in the year the old
  one read negative. Read fairly: the divestitures (Dockers, Denizen, footwear) and the 53rd
  week are real non-comparables and the full reconciliation is published. **But the timing is
  the pattern and it is recorded as one.**
- [ ] **Serial share issuance [E5-15] — not fired; the reverse.** Diluted shares 409.8M
  (FY2021) → 399.7M (FY2025); outstanding 384.85M at 2026-07-01.
- [ ] **Filed-figure tells [E4-30] — not fired.** Cash taxes paid ÷ pretax income: **18.9%,
  19.9%, 33.5%, 47.0%, 25.2%** (FY2021-25) — not falling. Reported growth visibly lumpy, not
  smoothed: net income $553.5M → $569.1M → $249.6M → $210.6M → $578.1M.
- [ ] **Dividends funded by issuance [E2-52] / restricted earnings [E2-60] — not fired.** See
  Stage 0(b): distributions exceeded adjusted FCF in FY2025, but **net debt fell** $309.5M →
  $190.4M and no shares were issued. The incremental payout came from selling Dockers, which
  is disclosed.
- [ ] **Except-for [E2-57] — not fired.** GAAP appears alongside adjusted at every line with
  full reconciliation, and there was no miss to frame away.
- [x] **The restructuring charge [E3-53] — FIRED.** FY2014 **$128.4M** · FY2015 $14.1M ·
  FY2020 **$86.8M** · FY2021 $5.7M · FY2023 $20.3M · **FY2024 $185.6M** (plus **$54.3M** of
  "restructuring related" charges buried inside SG&A) · FY2025 $24.5M (plus $12.1M). **Three
  large rebasings in twelve years**, and the 10-K warns of more: *"We may incur additional
  significant restructuring and restructuring related charges… which could be material in a
  future fiscal quarter or year."* Per [E5-33] these are real costs borne by shareholders and
  they are in the owner-earnings mean — they run through operating cash flow.
- **Flags that converge [E4-52]?** The four fired flags are the standard large-cap disclosure
  posture (guidance culture, adjusted metrics, a yardstick introduced at a convenient moment,
  recurring restructurings). They do **not** converge toward one outcome the way [E4-52]
  describes, and the two flags that would make them a lollapalooza — serial issuance and the
  filed-figure tells — are both clean.

**STEP 3 — THE PRIMARY TEST [E2-01]. Balance sheet first [E5-27].** Eight year-ends of
equity: $660.1M (FY2018, pre-IPO) → $1,563.5 → $1,299.5 → $1,665.7 → $1,903.7 → $2,046.4 →
$1,970.5 → **$2,278.6M**. Goodwill $280.6M and other intangibles $194.4M against $2,278.6M of
book — a **21% goodwill-plus-intangible wedge**, small, and reported separately [E2-43]. Debt
flat at roughly $1.0bn for eight years while cash rose $713.1M → $757.9M. A **$830.1M deferred
tax asset** (created by the FY2024 intercompany IP transfer) sits inside equity and *inflates*
the denominator, so the ROE series below is conservative, not flattered.

**ROE (net income ÷ average equity):** FY2019 **35.5%** (IPO-distorted) · FY2020 **−8.9%** ·
FY2021 **37.3%** · FY2022 **31.9%** · FY2023 **12.6%** · FY2024 **10.5%** · FY2025 **27.2%**
(**23.6%** excluding the $76.1M Dockers gain). Five-year mean (FY2021-25) ≈ **23.9%**.
Company-reported ROIC (their non-GAAP definition, **flagged**): 15.7% FY2025, 15.4% FY2024.
**Read: a genuinely high-return business on book equity, with two boom years at the front of
the window [E4-41] and a two-year hole in the middle (FY2023-24) dug by $205.9M of
restructuring and $207.1M of impairments.**

**The half-owner test [E2-26]: pass on operations, mixed on capital.**
*Pass, and unusually well:* channel, brand, geography and segment revenue every year; DTC and
wholesale as percentages; e-commerce as a share of DTC; stores opened (110) and closed (70);
the 53rd week quantified at **$78M, 1.3%**; currency quantified separately at the revenue,
gross-margin, SG&A, operating-income and EPS lines in every period; tariffs paid quantified
(**~$80M** under IEEPA) with the refund treated conservatively (**no asset recognized** beyond
phase-one claims); the Beyond Yoga headroom volunteered as *"less than 10%."*
*Mixed:* **no acquisition post-mortem for Beyond Yoga [E4-39] exists in any filing read**; and
**the mix component of gross margin — the one number that separates channel arithmetic from
pricing power — is named in every attribution and quantified in none of them.** This run had
to solve for it. That is the material disclosure gap.

**The institutional imperative [E2-30], scored:**
- [ ] **(1) resists change — NOT fired.** Dockers divested (2025, $194.7M proceeds, $155.6M
  gain), Denizen wound down, footwear exited, distribution outsourced, 10-15% of the corporate
  workforce cut. This is real change, executed, not resisted.
- [x] **(2) projects/acquisitions materialize to soak up available funds — FIRED. The central
  Q3 finding.** **Beyond Yoga: $390.9M of cash, Q4 FY2021 — the boom top.** Impaired **$90.2M**
  in FY2023 and **$111.4M** in FY2024 — **$201.6M, 52% of the price, inside three years** —
  with FY2025 revenue $151.3M and an operating **loss** of $(13.6)M in year four, and fair
  value now less than 10% above carrying. **[E5-24]: what is smart at one price is dumb at
  another.** Each impairment is attributed to *"the macroeconomic environment,"* *"an increase
  in discount rates"* or *"incremental investments in the brand and team"* — **never to the
  price paid.** *Scale, stated fairly: $390.9M is 4.8% of today's corrected market cap, against
  OXM's Johnny Was at 46% of its cap. This is the same error, one-tenth the size, and the core
  business was not neglected while it happened.*
- [ ] (3) staff studies produced to justify the leader's craving — nothing found.
- [x] (4) peer behaviour mindlessly imitated — **noted, mild.** "DTC First" is the universal
  apparel-brand strategy of the last decade and Levi's arrived late (36% DTC in FY2021 against
  Ralph Lauren's long-established direct majority). Following the pack is not a fault when the
  pack is right, but the strategy is not proprietary and the margin it delivers is arithmetic
  available to every competitor.

**Capital allocation — the two buyback conditions [E5-08], with the third [E4-31]:**
- **(1) ample funds for operations and liquidity: PASS.** $848.8M of cash and short-term
  investments, $1.0bn revolver undrawn, no maturity before 2030.
- **(2) repurchases at a material discount to conservatively calculated IV: FAILS on this run's
  numbers.** Average price paid, each from the filing that reports it: FY2020 **$18.73** ·
  FY2021 **$25.78** (the boom top) · FY2022 **$19.89** · **FY2023 $17.97 — the cheapest year,
  and they spent $8.1M** · FY2024 **$18.75** · FY2025 **$20.80** (the $120M ASR itself at
  $21.48) · FY2026 a **$200M ASR** launched in Q1 at roughly $21-22. **The largest purchases of
  the whole record were made at the highest prices, and the near-refusal came at the low —
  the [E2-51] tell.** Against this run's owner-earnings value band the current ASR is being
  executed above value.
- **(3) an adequately informed register [E4-31]:** met on operations; the un-quantified
  gross-margin mix is the one place where the register is buying a number it cannot compute.
- **The [E4-13] humility clause, in full:** this rests entirely on this run's own IV range,
  management knows the business far better than I do, many CEOs never stop believing their
  stock is cheap, and FY2023 — the cheap year — was also the year of weakest operating cash
  flow and highest inventory, which is a defensible condition-(1) reason for standing down.
  **CAPITAL-ALLOCATION FLAG recorded. It binds position size, never the discount rate.**

**Stated policy versus practice, recorded:** capex target 3.5-4% of revenue (actual 3.5% —
inside); **dividend payout target 25-35% of net income (actual FY2025 42.4% of continuing-ops
net income, 39.6% of adjusted — above)**; **return 55-65% of adjusted free cash flow (actual
118% — above)**. The July 2026 raise to $0.16 puts the forward payout at ~43% of guided FY2026
adjusted net income. A live gap between the stated policy and the practice; not a flag,
because the balance sheet strengthened anyway.

**Management, comp and transitions.** Michelle Gass joined as President January 2023 and became
CEO January 2024, succeeding Chip Bergh after twelve years. **Harmit Singh, CFO since 2013,
announced his retirement in the Q1 FY2026 release (2026-04-07)** — a second senior change
inside the window, and one that removes the executive who built the disclosure practice praised
above. Compensation (DEF 14A Summary Compensation Table): Gass FY2025 total **$16.15M** (salary
$1.475M, stock $8.13M, options $3.14M, non-equity incentive $3.03M, other $0.36M); FY2023
**$36.43M**, including an $8.1M signing bonus and $14.29M of make-whole equity. Singh FY2025
$6.05M. **Not low, and the FY2023 package is large; the incentive component does move with
performance; no extraction pattern found.** [E5-17]'s cap applies to all of it.

**THE GUARDRAIL — checked before writing the verdict.**
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** A strong Q3 cannot
  repair Q2 or substitute for Q4 [E2-37, E2-38, E3-39].
- [x] The key-person question was **recorded at Q2 as a moat defect [E4-23]** — the trademark
  is the Mayo Clinic, the two-year margin record is the surgeon — **not here as a compliment.**
- [x] **No excisable-cancer case [E2-35, E2-36] is being made.** The franchise was never
  submerged, Gass is not "the plan," and this run is not buying a manager.

- **VERDICT: [x] IN** — *IN means: I read the filed record, ran the flags as a series, and
  found no disqualifier. It is not a finding that these managers are honest — "sincerity and
  empathy can easily be faked" [E5-17] — and it does not promote the name.* **The record
  found:** no integrity disqualifier; a good and improving operating record; guidance met or
  beaten in two consecutive years and raised twice in the third; a balance sheet strengthened
  while paying out; unusually specific operating disclosure. **Against that:** four flags fired
  (the guidance/long-term-target practice, the addition of Adjusted EBITDA, the organic-revenue
  yardstick introduced in the year reported revenue turned negative, and the twelve-year
  restructuring cadence), one $390.9M acquisition made at the boom top and 52% written off with
  no post-mortem, and a repurchase record that buys most at the top and least at the bottom.
  **Under a binary weight case, that record clears — but it clears without any margin to spare,
  and it earns no premium at Q5.**

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**

Convention applied: multi-year mean of (OCF − SBC) − (c); operating cash flow nets the
working-capital increment from one audited line (constraint 3). **[E2-23]'s LIFO carve-out does
NOT apply** — LEVI values inventory at lower of cost or net realizable value, not LIFO, so the
working-capital increment stays fully in (c).

Per year ($M, filed; FY2024 is 53 weeks and its OCF is shown **net of the $87.1M one-off**):

| FY | weeks | OCF | SBC | D&A | capex | **OE (c = D&A)** | **OE (c = total capex)** |
|---|---|---|---|---|---|---|---|
| 2021 | 52 | 737.3 | 60.1 | 143.2 | 166.9 | **534.0** | **510.3** |
| 2022 | 52 | 228.1 | 60.8 | 158.9 | 267.1 | **8.4** | **−99.8** |
| 2023 | 52 | 435.5 | 74.4 | 165.3 | 313.6 | **195.8** | **47.5** |
| 2024 | **53** | 898.4 → **811.3** | 62.8 | 193.2 | 227.5 | **555.3** | **521.0** |
| 2025 | 52 | 529.6 | 81.6 | 206.3 | 221.4 | **241.7** | **226.6** |

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25]:**
- **Long-window mean (5-yr, FY2021-25, the corpus default [E2-42]): $241M – $307M**
- **Short-window mean (3-yr, FY2023-25): $265M – $331M**
- **Spread at the conservative end: ~10%** — small between windows.
- **Combined range (window spread × capex band): $240M to $330M.**

**Is that range too wide to reach a conclusion?** Between the two windows, no. **But a second,
much wider spread exists and it is the real finding**, so it is stated here rather than hidden
at Q5: the **cash** view above says $240-330M, while the **accrual** view — FY2026 guided
adjusted net income of ~$569M, less the ~$23M by which guided capex ($238M) exceeds D&A
(~$215M), less ~$28M after-tax for the restructuring charges [E5-33] says must be counted —
says **~$518M**. **The two views differ by more than 2x.**

**The reconciliation, so the reader can judge for himself:** over FY2021-25 the company put
**$339.7M of incremental inventory** ($898.0M → $1,237.7M) and **$329.6M of capex above
depreciation** ($1,196.5M capex against $866.9M D&A) into the ground, and took **$236.1M of
restructuring charges plus $66.4M of restructuring-related charges** — a substantial part of
it cash severance — while reporting rising adjusted earnings. Whether that spending was *maintenance* or *growth* is exactly what [E2-23] says
**"(c) must be a guess."** The cash convention charges all of it; the accrual view charges none
of it. **This run's guess is disclosed and it is the cash one, because that is the framework's
convention and because a company that has spent five years converting less than half its
adjusted earnings into distributable cash has not yet earned the benefit of the doubt.**

- **The bottom boundary [E5-34] — the number this run prices against (judgment, labelled):
  $240M**, the five-year mean on the total-capex basis with the $87.1M one-off stripped. It is
  corroborated by the FY2025 actual on the same convention ($226.6M).
- **Maintenance capex — the DISCLOSED JUDGMENT with the corpus default.** The **[E5-20]
  exception is NOT invoked**: nothing in the filing says depreciation understates renewal;
  there are no railroad-class assets; the fixed asset base is store fit-outs, IT and leased
  distribution capacity. **(c) is judged at D&A ≈ $206M**, with the band displayed out to total
  capex ($221.4M actual, $238M guided for FY2026). The band is narrow at the current run-rate
  and does not change the verdict anywhere within it.
- **Stock compensation subtracted in full [E5-06]:** $81.6M in FY2025, rising ($60.1M in
  FY2021). **[E3-70]** noted: the reported charge is the floor of the subtraction, not the
  measure; no repricing was found in the filings read.
- **Look-through earnings [E3-04]:** none material. No equity-method or unconsolidated
  minority stakes of size.
- **[E4-41] normalize down for luck:** applied once — the $87.1M 3PL receipt stripped. FY2021's
  boom and FY2022's inventory bust sit at opposite ends of the window and are left to offset
  each other rather than adjusted twice (see the windage count at Q5).

### Dividend coverage — the tasked read
Forward dividend run-rate **~$246M** ($0.64 × 384.85M; the Q3 FY2026 declaration was ~$62M).

| against | coverage |
|---|---|
| **bottom-boundary OE $241M [E5-34]** | **0.98x — the payout is the whole of owner earnings** |
| 5-yr mean, c = D&A ($307M) | 1.25x |
| 3-yr mean, c = D&A ($331M) | 1.34x |
| forward accrual view (~$518M) | 2.10x |
| FY2025 actual OE, c = D&A ($241.7M) | 0.98x |

**The 3.0% cash yield is real and is paid from a balance sheet that got stronger while paying
it. It is also, at the bottom boundary, the entire owner-earnings stream.** The 2020 precedent
— two quarters skipped, restart at half — is the record of what this board does when cash flow
breaks.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — [ ] **gruesome** — [x] **GOOD, with a great core.**
The savings-account test: an attractive rate of interest that is also earned on deposits added.
Five-year mean ROE ~23.9%, reported ROIC 15.7%, Levi's Brands segment operating margin 20.2%
before corporate, capex 3.5% of revenue, and the added capital *is* earning (DTC comps +6-7%,
new stores contributing). **Not gruesome** — it does not grow by pouring money into a
bottomless pit; the increment earns. **Not great** — the marginal dollar goes into leased
stores, working capital and $437M a year of expensed advertising, and one $390.9M discretionary
cheque earned nothing at all. **[E4-43] is the operative note: the good class passes.** It
simply ranks below great at Q5, and that is all.

### Staying power — score all three **[E5-11]**, worst case **[E2-55]**
1. **Large and reliable stream of earnings — PASS on level, PARTIAL on reliability.** Operating
   cash flow was positive in every year of the window, including COVID ($469.6M in FY2020).
   But the five-year range is **$228.1M to $898.4M** — a 4x swing, driven almost entirely by
   inventory. **[E3-55] scoping:** the mechanism is certain (they sell jeans; the swing is
   working capital), so the bounce is closer to noise than to genuine width — **except that
   FY2022's inventory blowout was a real management error, not a mechanism.**
2. **Massive liquid assets — PASS.** $757.9M cash + $90.9M short-term investments at FY2025
   year-end; **$849.3M + $128.5M at 2026-05-31**; total liquidity ~$1.8bn including the undrawn
   $1.0bn revolver. **[E5-39] noted honestly:** the revolver is the kindness of strangers,
   pre-arranged — but the **$978M of own cash and securities is not**, and it alone covers four
   years of dividends. **$717.1M of the cash sits in foreign subsidiaries**, which is a
   repatriation-friction fact, not a liquidity fact.
3. **No significant near-term cash requirements — PASS, and this is the strongest leg of the
   three.** **No debt maturity before August 2030** (4.000% €475M notes; then 3.50% notes in
   2031); the revolver is undrawn and matures November 2029; the **springing 1.0x fixed-charge
   covenant** arises only if availability falls below a specified threshold and is nowhere near.
   The real fixed cost is leases: **$1,449.6M undiscounted, $304.8M due in FY2026, 6.7-year
   weighted term at 4.34%**, plus $95.8M of finance leases and a **$280M Levi's Stadium naming
   commitment through 2043**. Operating lease cost including variable and short-term ran
   **$411.7M in FY2025, 6.6% of revenue** — a hard daily cost, **not float [E3-52]**.
- **Leverage, named and quantified [E4-16, E3-29] — no ratio ceiling exists in this framework
  and none is used:** total debt **$1,039.2M, 100% fixed rate, unsecured**, no ordinary-course
  financial covenants; **net debt ~$190M ≈ 0.2x** adjusted EBITDA ($719.0M adj EBIT + $206.3M
  D&A = $925.3M). **Coverage test [E2-54] with capex charged first:** (OCF $529.6M + interest
  $48.6M) − maintenance capex $206.3M = $371.9M against $48.6M of interest = **7.7x**; on the
  five-year mean OCF, ~8.4x. **Passes the wallet-zip test with room, and the terms are the
  right ones — long, fixed, unsecured, covenant-light.**
- **Jurisdiction [E3-66]:** US filer, US listing, Delaware incorporation. Shareholders stand at
  the front of the queue — **except that Class A shareholders stand behind Class B on every
  vote.** Recorded.

### Name the specific way THIS business dies **[E2-27, E3-24]** — the iron prescription **[E4-51]**
*Modelled from exposure, not experience **[E4-40]**. The current two-year run is a favourable
cycle, and a benign recent history is "not only useless, but actually dangerous" as a guide.*

1. **The denim cycle turns.** Levi's brand is 94% of revenue and denim bottoms are 64%. Fashion
   cycles in bottoms run a decade. **Quantified:** a return to the FY2023 gross margin (56.9%)
   on FY2025 revenue costs **~$300M of gross profit** — more than the entire owner-earnings
   mean, and more than the whole margin expansion of the last three years. Add the FY2023
   revenue trajectory and the operating leverage on a 1,231-store fixed base and the number is
   worse. **Likelihood over a decade: a real possibility.**
2. **The DTC transition's cost base is permanent while its margin benefit is finite.** DTC is
   52% and each further point buys only ~19bp of gross margin, while selling expense is 21.7%
   of revenue and 1,231 leased stores carry $1,449.6M of undiscounted rent on a 6.7-year
   weighted term. **Quantified:** a 10% decline in DTC revenue against a fixed store base takes
   **~$190M of gross profit** with almost no cost relief inside the lease term — **roughly
   two-thirds of the owner-earnings mean.** The 10-K names the trigger itself: *"consumers may
   reduce discretionary spending."* **Likelihood: a real possibility** in a consumer recession.
3. **The tariff regime.** ~$80M of IEEPA tariffs paid; the Supreme Court **invalidated** IEEPA
   tariffs on **2026-02-20** and the government re-imposed prospectively under separate
   authority; FY2026 guidance **assumes** China at 30% and rest-of-world at 20%. **Quantified,
   and calibrated to a filed number rather than assumed:** US revenue is ~43% of the total
   (the 10-K states international at 57%) ≈ $2.7bn, carrying ~$1.04bn of COGS at the 38.3%
   consolidated rate, of which the dutiable customs value is a substantial majority. The filed
   calibration is the **~$80M of IEEPA tariffs actually paid** over roughly three quarters at
   rates in the 10-20 point range. **Each further 10 points of tariff therefore costs roughly
   $70-100M of COGS a year ≈ 30-40% of the bottom-boundary owner-earnings figure**, before any
   pass-through. *(Estimate, labelled.)*
   **Likelihood: elevated rates persisting is likely** (it is in the guide); **a material
   escalation is a real possibility**; a refund of the ~$80M already paid is **a low-level
   possibility** and is **not counted** anywhere in this run.
4. **The next Beyond Yoga.** $390.9M in at the boom top, 52% impaired, still loss-making, fair
   value less than 10% above carrying at the FY2025 test, and **no post-mortem ever filed
   [E4-39]**. **Quantified:** writing off the remainder would be roughly $190M of the $475.0M of
   goodwill-plus-intangibles — non-cash, but it is the record of what this management does with
   a large discretionary cheque. **A further impairment is a real possibility; a repeat
   acquisition at a top is a low-level possibility** given the current narrowing focus.
5. **The third-party-logistics transition.** The 10-Q says it in terms: *"We have and may
   continue to experience shipping delays, order cancellations and increased costs."*
   Distribution expense rose **19.7% to $458.2M** in FY2025 (7.3% of revenue, from 6.3%).
   **Quantified:** that single-year increase of $75.3M is ~30% of the bottom-boundary
   owner-earnings figure. **Continuing elevated cost is likely; a severe disruption is a
   low-level possibility.**
6. **Governance — permanent, and not a death but a discount.** Class B holds **96.5% of votes**.
   No takeover premium will ever arrive; the 10-K says so. **Likelihood: certain. It is already
   in the quote and it binds position size, not survival.**

- **VERDICT: [x] IN.** **Survival is not in question inside any window this run can see.** Net
  debt ~$190M against $978M of own liquid assets; **no maturity before August 2030**; 7.7x
  interest coverage after maintenance capex; a $1.0bn undrawn revolver to 2029; staying power
  **3 of 3**, with the third leg — the one that usually kills — the strongest of the three.
  **Every death named above is an earnings death, not a solvency death.** The business survives;
  the question is what it earns, and that is Q5's.

---
⛔ **Q1 IN · Q2 IN · Q3 IN · Q4 IN. Q5 opens.**

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Market cap $8,193.5M** (384,850,562 shares × $21.29, NYSE close 2026-08-28).
**Sovereign: USD 30-year 5.19%, 2026-08-27, FRED `DGS30`.**

**THE FLOOR, BEFORE THE RANKING [E4-28].** *"That's the figure we quit on."*

### 1. THE YIELD — owner earnings ÷ market cap (OE is post-interest; an equity number)

| basis | OE | yield on $8,193.5M | points vs 5.19% | multiple |
|---|---|---|---|---|
| **Bottom boundary [E5-34]** — 5-yr mean, c = total capex, one-off stripped | **$241M** | **2.9%** | **−2.3** | **34x** |
| 3-yr mean, c = total capex | $265M | 3.2% | −2.0 | 31x |
| 5-yr mean, c = D&A | $307M | 3.7% | −1.4 | 27x |
| 3-yr mean, c = D&A | $331M | 4.0% | −1.2 | 25x |
| *memo — the accrual view: FY2026 guide-implied adj. net income, capex-over-D&A charged, restructuring charged [E5-33]* | *~$518M* | *6.3%* | *+1.1* | *16x* |

**The combined owner-earnings range is $240M to $330M — 2.9% to 4.0% — every point of it
below the 5.19% sovereign.** Only the accrual memo line clears the bond, and it clears it by
1.1 points.

### 2. WHAT THE PRICE ALREADY ASSUMES
$8,193.5M ÷ $240-330M = **25x to 34x owner earnings.**
- To merely **match the 5.19% bond**, the price needs **+1.2 to +2.3 percentage points a year
  of owner-earnings growth, forever.**
- To clear the **10% floor [E4-28]**, it needs **6.0% to 7.1% a year of real owner-earnings
  growth, forever** — or 3.7% a year if the accrual view is the right one.

**What the business has actually done.** Adjusted diluted EPS has compounded impressively:
$1.10 (FY2023) → $1.25 → $1.34 → guided $1.46-1.52 — roughly **+10-11% a year**. Adjusted EBIT
margin 9.0% → 10.2% → 11.4% → guided 12.0%, with a stated long-term goal of ~15%. Organic
revenue guided +5.5-6.0%.

**And the number that will not go away:** **owner earnings on this framework's own convention
are LOWER in FY2025 ($241.7M) than in FY2021 ($534.0M).** The reported earnings compounded;
the distributable cash did not, because it went into inventory, stores and restructuring.
**The price is asking for 6-7% a year of compounding from a series that has gone sideways to
down over five years.** Against [E4-35]'s base rate — fewer than 10 of the 200 most profitable
companies achieved 15% EPS growth over twenty years — a demand for sustained 6-7% real
owner-earnings growth from a narrow-moat apparel brand is not absurd, but **it is the whole
case, and it has to be stated in writing as the burden it is.** [E4-44] second bound: the asset
cannot grow faster than its earnings over the long term, and multiple expansion is not a
perpetual term. [E2-63] ceiling: the upside is bounded by the 15% adjusted-EBIT-margin target
and the finite DTC mix runway — roughly 3 more points of gross margin, and then growth must
come from units.

### 3. WHAT YOU ARE PAID
**−2.3 to −1.2 points versus the sovereign** on the owner-earnings base; **+1.1 points** on the
most generous accrual view. Plus a **3.0% cash dividend**, taxable as ordinary income in the
account that would hold it.
**Honest pre-tax expectancy at $21.29:** owner-earnings yield 2.9-4.0% plus honest growth.
Crediting management's own guided mid-single-digit organic growth with the margin path they
guide — a demanding assumption — gives **≈ 8-10%**. Crediting growth at a level the corpus
would accept without a projection document (say 4-5%) gives **≈ 7-9%**.
**The floor is not cleared on the base this framework requires.**

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]

| basis | discount | value | per share |
|---|---|---|---|
| owner earnings $240-330M | at the 10% floor [E4-28] | $2.4bn – $3.3bn | **$6 – $9** |
| owner earnings $240-330M | at the sovereign 5.19%, zero growth | $4.6bn – $6.4bn | **$12 – $17** |
| accrual view ~$518M | at the 10% floor | $5.2bn | **$13** |
| accrual view ~$518M | at the sovereign 5.19%, zero growth | $10.0bn | **$26** |

- conservative **$6** · optimistic **$26** · **current price $21.29**

**That range is too wide to reach a conclusion, and per [E4-25] that IS the conclusion.** The
width is not window selection and it is not the capex band — both of those are narrow here. It
is the single unresolved question of **whether Levi's true owner earnings are the $240-330M the
cash statement shows or the ~$518M the adjusted income statement implies**, and that turns on
whether five years of inventory build, store capex and restructuring were maintenance or growth
— which is exactly the thing [E2-23] says must be guessed and which no filing resolves.

**THERE IS NO HURDLE — THERE IS A RANKING [E4-21] — but first there is a floor [E4-28].**
- Points over sovereign, this name: **−2.3 to −1.2** on the required base; +1.1 on the memo base.
- **At the bottom boundary [E5-34] the honest expectancy is roughly 7-9% pre-tax. Below
  roughly 10%, the name is not ranked — it is quit on, whatever the sovereign is.**
- **It does not enter the ranking. The earmarked capital stays parked [E2-74].**

**WHICH BAR ARE YOU USING?**
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case? **No.**
  $21.29 sits **above every band built on owner earnings** and **inside the very top of the
  single most generous band** (accrual base, sovereign discount, zero growth, $26). That is the
  **middle box: no useful conclusion — move on.** *No margin is stacked on top.*
- [ ] Normal method [E4-11] — not used. Applying a margin of safety to a name that does not
  clear the floor at the conservative end would be spending conservatism twice.
- **Windage count: ONE.** The single conservatism applied is the **[E4-41] normalization
  stripping the $87.1M third-party-logistics receipt from FY2024's operating cash flow**,
  justified in writing above. The bottom-boundary base is **[E5-34]'s own required move**, not
  extra windage; the capex band is **[E2-23]'s required display**, not windage; and no margin of
  safety is applied on top of the screamer test.

- **VERDICT: [x] UNKNOWABLE → what specifically cannot be known: whether five years of
  inventory build ($339.7M), capex above depreciation ($329.6M) and cash restructuring (~$240M)
  were maintenance or growth. That single question moves owner earnings from $240M to $518M —
  a factor of more than two — and no filing resolves it. [E4-25].**
  **Ranking position: none. At the bottom boundary [E5-34] the [E4-28] floor is not cleared,
  so the name is quit on at $21.29 regardless of where inside that range the truth sits.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists. These are pre-committed yardsticks for the WATCH LIST, set prior to any
act [E1-02]. **Alert thresholds LISTED ONLY — `tools/alerts.json` was NOT edited.**)*

**THE ONE METRIC THAT WOULD RESOLVE THIS FILE.** The whole run turns on the cash-versus-accrual
gap. The metric is **cash conversion**: (operating cash flow − capex − stock-based compensation)
against adjusted net income.
- **Thesis-confirming threshold:** that figure **≥ $400M in each of two consecutive fiscal
  years** — i.e. converting ≥ 70% of adjusted net income into distributable cash. FY2025 was
  **$226.6M (42%)**. Two clean years at $400M+ would move the honest owner-earnings base to
  ~4.9-5.5% on today's cap and would make the growth case checkable rather than assumed.
- **Thesis-breaking threshold:** that figure **below $200M in any year without a named one-off**,
  or working capital consuming more than $150M in a year while revenue grows.

**Q2 / moat metrics (the reopen conditions, all required):**
1. **Gross margin ≥ 62% for a full fiscal year with the DTC mix flat** — that would be pricing,
   not mix, and it is the only thing that would upgrade the class from NARROW.
2. **DTC comparable sales positive for four consecutive quarters** with wholesale volumes also
   growing — units and price together, the [E2-44] and [E4-55] tests passing on a physical
   series rather than a qualitative sentence.
3. **The tariff regime legally settled** — the IEEPA refund resolved and the replacement
   authority litigated — so the cost base stops being an administered variable.

**Thesis-breaking metrics and their thresholds:**
- Gross margin **below 61.0% for a full year** = the mix runway spent and no pricing behind it.
- Organic revenue growth **below +2%** for two consecutive quarters = the share gain over.
  **Europe's Q2 FY2026 organic print was already −0.8%** (explained by a prior-year shipment
  shift); a second negative Europe quarter without that explanation is the first real crack.
- Any **new acquisition above $250M** = the [E2-30](2) flag hardening; the Beyond Yoga record is
  the base rate.
- **A further Beyond Yoga impairment** (fair value was less than 10% above carrying at the
  FY2025 test) — a re-read event, and the first opportunity for an [E4-39]-grade post-mortem.
- **Restructuring charges above $100M in any year** = the fourth rebasing in thirteen years.
- **Any change to the $0.16 quarterly dividend**, either direction: a cut is the 2020 precedent
  repeating; an increase that takes the payout above 50% of adjusted net income is the
  [E2-60] question reopening.
- **The revolver drawn at all**, or any 8-K Item 1.01/2.03 amending the Credit Agreement.

**Price [E4-28]:** the bottom boundary must pay the floor with zero growth credited:
**$240-330M × 10 ≈ $2.4-3.3bn ≈ roughly $6 to $9 per share**; on the accrual base at the floor,
**~$13**. At $21.29 the quote sits roughly **2.4x above the top of the owner-earnings entry
band** and **~65% above the accrual-base floor price**. **Nothing here is close, and no
plausible near-term news closes that gap** — the arithmetic requires either a very large price
decline or two years of proven cash conversion, and the second is the one worth waiting for.

**The sell rule [E2-28]** — not applicable, no position. Recorded for completeness: the three
hold conditions (return on equity capital satisfactory · management competent and honest ·
market does not overvalue) would fail today on the third alone.

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question
for this name: **is the FY2024-26 margin expansion an aberrational recovery from a bad
2022-23 — restocking, cotton deflation and a mix shift that has now nearly run its course — or
has the business permanently improved?** This run's reading of the filed evidence is that
roughly two-thirds of it is mix and cost, one-third is real pricing, and that the honest answer
arrives in the FY2027 and FY2028 gross margins once DTC stops moving. **Beliefs change quite
gradually; this one should be allowed to.**

**Position size — a judgment, stated [E3-45]:** **zero.** The name does not enter the ranking.
Were it ever to enter, it would be sized down for the live capital-allocation flag and again for
the 96.5% Class B voting bloc — economics without a vote and without a takeover option.

**Taxable-account note, as tasked — the never-switch test [E2-46, E3-64, E4-45].** **LEVI fails
it, and it fails it on its own bull case.** The mandate wants a dividend payer that compounds.
At $21.29 the dividend is **3.0%, taxable as ordinary income annually**, and the compounding
case requires the 15% adjusted-EBIT-margin target to arrive — a management projection, not a
record. [E3-64]'s arithmetic is direct: a holding that pays out its return annually in
ordinary-income form and needs a projection to justify the price is precisely the shape that
loses 3.5 points a year to friction and tax against a single deferred compounder. **The $2,750
stays parked [E2-74].**

**Next catalyst dates (LISTED ONLY):** Q3 FY2026 earnings **~2026-10-07/08** · Q4 FY2026 +
initial FY2027 guidance **~late January 2027** (score it against the [E3-48] table above) ·
FY2026 10-K ~late January 2027 · DEF 14A ~March 2027 · the residual Dockers sale completion ·
IEEPA refund phases disclosed in each 10-Q · the $200M ASR settlement (Q3 FY2026).
**Alert candidates (LISTED ONLY, `tools/alerts.json` NOT edited):** LEVI < $13.00 (accrual-base
floor price); LEVI < $9.00 (owner-earnings band top); quarterly dividend ≠ $0.16; any LEVI 8-K
Item 1.01/2.03; any 8-K announcing an acquisition.

- **VERDICT: [x] IN** — "what would prove me wrong" is answered with pre-committed, dated,
  document-named conditions on both sides, and the one metric that would actually resolve the
  file is named with a threshold.

---
## SELF-AUDIT
- [x] Questions answered in order; Q1-Q4 IN, stopped at Q5 UNKNOWABLE; Q6 written as tasked
- [x] **Stage 0 was run and reported FIRST**: the corrected cap, the exact mechanism of the
      artifact (pre-split pre-IPO cover tag), the reconciliation to $801M, the multiple (10.23x),
      the corrected statute yield (2.57%), the dividend record from the raw filed series with
      the skipped quarters named, the decomposition, and the boom-window read
- [x] No question marked IN carries an "unverified", "general knowledge" or "provisional" caveat
- [x] Every UNRESEARCHED item names the artifact and the route (register below); the
      Uniqlo/Inditex rows are named work orders, are recorded as the reason the class is NARROW
      rather than WIDE, and are not load-bearing for the verdict
- [x] The UNKNOWABLE verdict states what specifically cannot be known (maintenance vs growth
      across $670M of five-year spending) and why no filing resolves it
- [x] Step 0: the filing was read with accession numbers; **FY2025 OCF $529.6M cross-checked
      three ways** (filed statement, MD&A table, XBRL); net revenues cross-checked twice;
      53-week year flagged (FY2024, +$78M/1.3%); the Dockers discontinued-operations basis break
      flagged at every comparison
- [x] Owner earnings on multi-year means; **both windows shown**; the spread stated; the capex
      band displayed; **(c) a disclosed judgment at the D&A default with the reason written
      [E3-44, E2-41]** and the [E5-20] exception explicitly not invoked; SBC subtracted in full;
      bottom boundary [E5-34] computed and labelled a judgment; the [E2-23] LIFO carve-out
      explicitly ruled inapplicable; the one-off normalization [E4-41] named and counted as the
      single windage
- [x] Competitor row: **3 of ~6-8 pulled**, filing-sourced with accessions, committed as a
      separate research file; the two foreign-filer gaps named with routes; the class decided on
      the subject's own filed series plus the pulled rows — **not PROVISIONAL**
- [x] Sovereign for the earnings currency (USD) from the standing issuing-authority source
      (FRED DGS30), dated 2026-08-27, lag noted
- [x] Value stated as round-number ranges; **the cash-versus-accrual width identified as itself
      the conclusion [E4-25]**
- [x] **One bar (screamer test), not both; windage count: one, justified in writing**
- [x] Prices dated; aggregator used for live quotes only and flagged
- [x] **The bias declared in both directions and the disconfirming evidence carried in full
      [E4-26, E4-51]** — the three facts that argue against this run's opening hypothesis are
      stated in Q2 as their advocate would state them
- [x] The market-beating claim is not made anywhere; every judgment carries a ledger id or is
      labelled a judgment or estimate
- [x] Shared files untouched — `PORTFOLIO.md`, `Screens/*`, `tools/*`, `Framework/*` and all
      other run files unmodified; only this run file and one research file created
- [x] Run committed to git (1c85527; this hash added in the follow-up commit)
- [x] `python tools/check_framework.py` re-run after this file was written: **PASS** — 0 phantom
      citations, 0 unlabelled numbers. All 82 ledger ids cited in this file and all 28 in the
      evidence pack resolve against `principle_ledger.csv` (261 rows)

## REGISTER
- **Verdict: [x] UNKNOWABLE (about my evidence) at Q5.** Q1 IN · Q2 IN (NARROW) · Q3 IN
  (no disqualifier found) · Q4 IN (survives comfortably) · **Q5 UNKNOWABLE, not ranked — the
  [E4-28] floor is not cleared at the bottom boundary [E5-34].** No position held; no [E2-28]
  hold read required.
- **One line:** **a genuinely narrow-moat business — a 170-year-old trademark nobody can attack,
  taking share from Wrangler and Lee, raising price while units grow, passing a tariff shock
  through, with net debt of $190M and no maturity before 2030 — whose rising gross margin is
  mostly channel arithmetic that has nearly run out, whose owner earnings on this framework's
  own convention are lower today than in 2021, whose dividend now consumes the whole of them,
  and whose price at $21.29 pays 2.9-4.0% against a 5.19% Treasury and needs 6-7% a year of
  compounding forever to clear the floor. The screen that surfaced it priced the company at
  one-tenth its size.**
- **Work orders (UNRESEARCHED, none load-bearing):** (1) **Fast Retailing (Uniqlo)** annual
  securities report — TSE/TDnet and the English IR site, evidence-ladder rung 4 — for global
  category share; (2) **Inditex (Zara)** annual report — CNMV/BME and the English IR site,
  rung 4 — same purpose; (3) Abercrombie / American Eagle / Gap 10-Ks — EDGAR, ordinary
  retrieval — for the US channel context row; (4) LEVI Q3 FY2026 10-Q and release
  (~2026-10-07) — EDGAR — refresh gross margin, DTC mix, comps, cash conversion and the IEEPA
  refund; (5) the FY2021 10-K Beyond Yoga purchase-price allocation note (acc.
  0000094845-22-000010) read in full for the acquisition post-mortem that has never been filed.
- **If UNKNOWABLE — what specifically cannot be known:** whether the **$339.7M of incremental
  inventory, $329.6M of capex above depreciation and $302.5M of restructuring and
  restructuring-related charges** taken over FY2021-25 were maintenance capital or growth
  capital. That one question moves owner earnings
  from **$240M to $518M** and the fair value from **$6 to $26 a share**. [E2-23] says "(c) must
  be a guess"; this run's guess is disclosed and is the conservative one; **no filing resolves
  it, and two more years of cash-conversion data would.**
- **The single biggest concern:** **not the business — the price, and the reason the price
  looks reasonable.** Every number the market is using is an *adjusted accrual* number:
  adjusted EPS compounding at 10-11%, adjusted EBIT margin rising three years running,
  Adjusted EBITDA newly promoted into the filing. **Every one of those has been true while the
  cash the owner could actually take out fell from $534M to $242M.** The gap is five years of
  spending on inventory, stores and three restructurings, and it is exactly the gap that
  [E2-23]'s owner-earnings definition exists to expose. At $21.29 the buyer is paying 25-34x the
  cash and 16x the accrual, and taking a 3.0% ordinary-income dividend that at the bottom
  boundary is the entire owner-earnings stream. **The business will very likely survive and may
  well prosper. The price already assumes it does.**

*This file is a judgment by the AI running the framework. The underlying facts are the FY2025
10-K (acc. 0000094845-26-000008), the Q2 FY2026 10-Q (acc. 0000094845-26-000037), the DEF 14A
(acc. 0001308179-26-000050), the five earnings 8-Ks, the FY2024/FY2023/FY2021/2018 10-Ks and the
2019 IPO prospectus (acc. 0001193125-19-082264) named in Step 0, SEC XBRL `companyfacts` for CIK
0000094845 and for KTB/VFC/RL, FRED `DGS30`, and one flagged live quote. Where a number is a
judgment or an estimate — the (c) band, the 19.0-point channel spread solved from the filed
series, the bottom-boundary owner-earnings figure, the tariff and DTC-decline sensitivities, and
the entry bands — it is labelled as one.*
