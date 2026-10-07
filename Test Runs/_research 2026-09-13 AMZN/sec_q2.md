
*Resume note, 2026-09-13 ~14:40, added beneath the line above rather than replacing it (operator rule 6): the session that wrote Step 0 and
Q1 was killed by a session limit while building the Q2 competitor row. This run resumed from the files on disk. **The sovereign was re-struck
at the resume** (`python tools/sources.py`: *"USD 5.35% 09/11/2026 US Treasury daily par yield curve"*), unchanged, so Step 0 stands.
Everything below Q1 was written by the resuming session.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

> *"An economic franchise arises from a product or service that: (1) is needed or desired; (2) is thought by its customers to have no close
> substitute and; (3) is not subject to price regulation. The existence of all three conditions will be demonstrated by a company's ability to
> regularly price its product or service aggressively and thereby to earn high rates of return on capital."* — **[E3-03]**, **[E3-43]**, 1991

### How a business with three legs is judged, from the text
**What THE FRAMEWORK v4 says:** [E3-03] defines a franchise as *"a product or service"*, so the test runs per product. The one rule in the
document about segments is at Q3, and it is a warning about blending: the consolidated series can *"camouflage repeated failures in capital
allocation elsewhere"* — *"judge retention segment-by-segment, incrementally, never on the blended return"* **[E2-56]**. The metric set is
chosen *"by business type first"* **[E5-37]**. **No instance found** in the framework of a rule for combining leg verdicts into one Q2 verdict
(searched "segment", "leg", "conglomerate", "divisions": one hit, the [E2-56] line).
**What this queue has done, recorded as practice and not as framework:** the verdict must hold for **what the shareholder actually buys**
(GHC, 2026-09-02); where legs split, it is decided by **where the profit and the capital actually are** (HAS, 2026-09-03: IN because the profit
was *"overwhelmingly"* the franchise leg and the rest *"neither grows nor eats material capital"*; SONY, 2026-09-13: OUT with two NARROW legs
carrying ~55% of profit). MSFT and GOOGL (2026-09-06) passed Q2 on the franchise leg that carried the weight, with their cloud legs recorded as
narrowing. **That practice is followed here, and each leg is tested on its own first, so the weighting cannot hide a leg's verdict.**

**Where the weight is (filed segment note; TTM to 2026-06-30):**
| | net sales | operating income | share of OI | net additions to P&E | share of additions |
|---|---|---|---|---|---|
| North America + International (stores, marketplace, advertising, Prime) | 627,276 | 39,031 | **42%** | FY2025 43,536 · H1 2026 27,532 | FY2025 30.6% · **H1 2026 23.2%** |
| **AWS** | 148,404 | 54,681 | **58%** | FY2025 96,496 · H1 2026 90,120 | FY2025 67.8% · **H1 2026 76.0%** |
AWS's share of consolidated net additions: **51.4% (2023) → 62.1% (2024) → 67.8% (2025) → 76.0% (H1 2026)**. Corporate additions omitted from the
shares above (2,320 in 2025; 996 in H1 2026).

---
### LEG 1 — AWS (58% of operating income; three-quarters of the new capital)

**Criterion (1) — needed or desired: [x] YES.** $148.4bn TTM sales, +32.7% in H1 2026.

**Criterion (2) — thought by its customers to have no close substitute: [ ] NO, on the filed record.**
- **Three rivals of scale sell the same service, and each grows faster or earns more** (Table A, `peers/competitor_row.md`, every figure with its
  accession): FY growth AWS **+19.7%** · Microsoft Intelligent Cloud +29.7% · Google Cloud +35.8% · Oracle cloud infrastructure +76.9%. Segment margin
  AWS **35.4%** · Intelligent Cloud **41.3%** · Google Cloud 23.7%. **AWS is second of three on margin and last of four on growth.** H1 2026 closed the
  growth gap (AWS +32.7%, IC +30.7%, Google Cloud +73.1% including a new hardware line).
- **Backlog is no longer AWS's lead either:** AWS *"approximately $496 billion"* (2026-06-30) · Microsoft commercial RPO $678bn (2026-06-30) · Oracle
  $664bn (2026-08-31) · Google Cloud $513.9bn (2026-06-30).
- **The largest customers buy from more than one of them, and the rivals' filings say so.** Microsoft 10-K FY2026: *"we recorded revenue from commercial
  arrangements with OpenAI, inclusive of revenue-sharing payments, of $24.1 billion"* — the same OpenAI that expanded its AWS commitment *"by $100.0
  billion over 8.0 years"*. Oracle 10-K FY2026: *"we offer our customers multicloud services whereby our customers can combine cloud services from multiple
  clouds with the goal of optimizing cost, functionality and performance. OCI's multicloud services work with a number of our competitors' products,
  including Microsoft Azure, Amazon Web Services and Google Cloud."* Microsoft: *"higher purchases of licenses running in multi-cloud environments"*.
  Meta carries *"$349.31 billion of non-cancelable contractual commitments ... most of which are related to third-party cloud capacity arrangements"*
  (10-Q Q2 2026) and appears in Amazon's own Q1 2026 release among *"new AWS agreements"*. **Amazon's filings contain no multi-cloud, switching or
  migration sentence at all** (0 hits, 10-K FY2025 and 10-Q Q2 2026); the only customer-change language is the competitive factor *"customers' ability and
  willingness to change business practices."*

**Criterion (3) — not subject to price regulation: [x] YES**, with open investigations into *"certain aspects of AWS's offering of cloud services"*
(10-K FY2025, Item 1A) recorded.

**The pricing test [E3-03]'s own sentence names — and [E2-44](1), [E4-37]. THIS IS THE DECISIVE EVIDENCE, AND IT IS AMAZON'S OWN.**
Every annual report read (FY2015, and FY2017 to FY2025, which between them cover every year from 2013) and both 10-Qs read explain AWS's sales with the same sentence:
- FY2015 10-K: *"The sales growth primarily reflects increased customer usage, partially offset by pricing changes. Pricing changes were driven largely by
  our continued efforts to reduce prices for our customers."* and *"The decrease in AWS segment operating income in absolute dollars in 2014 ... is
  primarily due to pricing changes"*.
- FY2017, FY2018, FY2019, FY2020 and FY2021 10-Ks: the same two sentences, verbatim.
- FY2022, FY2023, FY2024, FY2025 10-Ks, 10-Q Q3 2025 and **10-Q Q2 2026** (`0001018724-26-000026`): *"The sales growth primarily reflects increased
  customer usage, partially offset by pricing changes primarily driven by long-term customer contracts."*
**Thirteen consecutive years, 2013 to H1 2026, in which the filer says price moved against AWS revenue; no year found in which it says price added to it.**
The mechanism changed from list-price cuts to discounts for multi-year commitments; the direction did not. **[E2-44](1) asks for *"an ability to increase
prices rather easily ... without fear of significant loss of either market share or unit volume"*; the filed record is the opposite behaviour, sustained.**
The releases' price claims are price cuts under another name: Graviton *"up to 40% more price-performant than leading x86 processors"*; Kiro *"up to 50%
more cost-effective than alternatives"*.

**[E3-43]/[E3-46] — high returns on capital, and their direction [E4-32]:** AWS operating income ÷ average segment assets **25.0% (2023) → 30.1% (2024) →
22.3% (2025) → 18.1% (TTM)**; net sales ÷ average P&E 1.17× → 0.86× → **0.65×**. High, and falling fast as the plant quadruples.

**[E4-04] — must the moat be continuously rebuilt? YES, on the filer's own words.** The test the framework sets: *"does the spending defend the same
advantage, or buy its replacement?"* AWS's plant is **servers on five-year lives**, shortened in 2025 *"due to the increased pace of technology development,
particularly in the area of artificial intelligence and machine learning"*; AWS net P&E **$72.7bn → $263.8bn in thirty months**; the new spending buys a
new class of hardware (Trainium, *"our chips business"*) for a new class of workload. That is the replacement case, and [E4-04] names the class:
*"industries prone to rapid and continuous change."* **[E3-51]:** the long AWS run is a **surfing run** on the cloud wave and now the AI wave, and **[E4-36]**
places it in the fourth cause (wave-riding), the one the framework says is not ownable.

**[E2-58] — is there a wide and sustainable cost advantage?** Claimed in releases (Graviton, Trainium); **not evidenced as wide** in any filing: Google
*"began recognizing revenue from the sale of TPU systems"* (10-Q Q2 2026) — a rival selling its own custom accelerators to others — and every rival spent
3.4-9.0× depreciation in its latest period (Table A). **[E2-27]:** *"viewed collectively, the decisions neutralized each other"* is the row's picture.

**The backlog is not pricing power, and part of it is bought.** At least $200bn of the $252bn backlog increase in six months is from OpenAI and Anthropic,
the two companies into which Amazon put $50.0bn (OpenAI, 2026, $21.3bn of it after June 30) and $10.0bn (Anthropic Series G and H, Q2 2026) of equity (Q1 table). A commitment financed partly by the vendor's own capital is
evidence of volume, not of the customer's view that no substitute exists — and the larger of the two also buys from Microsoft.

**Leg verdict: AWS is a strong position in a contested, rapidly changing category — the "business" of [E3-43], not a franchise.** Class NARROW, direction
**narrowing**.

---
### LEG 2 — North America and International: stores, marketplace, Prime (with advertising tested separately below)

**Criterion (1): [x] YES.** $627.3bn TTM sales; worldwide paid units **+8% to +17%** a year-on-year by quarter, Q1 2025 to Q2 2026 (EX-99.1
releases), accelerating — **the physical series [E4-55] is healthy.**

**Criterion (2) for shoppers: [ ] NO, on Amazon's own description of what it competes on.** 10-K FY2025, Item 1: *"We believe that the principal
competitive factors in our retail businesses include selection, price, and convenience, including fast and reliable fulfillment"*; every 10-K read, FY2015
to FY2025: *"To decrease our variable costs on a per unit basis and enable us to lower prices for customers, we seek to increase our direct sourcing"*; the
Q4 2025 release's guidance carries *"even sharper prices in our international stores business."* A business whose stated weapon is the lower price is
**[E4-36]'s first cause (extreme minimization of one variable, the Costco class)** — admirable, and the opposite of pricing aggressively. **The attacker's
test [E2-45] is being run on it now:** Walmart's eCommerce net sales **~$150.4bn, +24.4%** in fiscal 2026 (filed dollars, 10-K `0000104169-26-000055`),
against Amazon North America **+10.0%** in 2025; Walmart global advertising **+46%** (including VIZIO) and +37-38% in the last two quarters (releases).
North America's margin **6.9%** (2025) and **7.9%** (H1 2026) is above Walmart U.S.'s 5.2%/5.8% — a better position, measured, on the same metric.

**Criterion (2) for sellers: NOT EVIDENCED either way by any fee conduct, because none is filed.**
- **No Amazon seller, fulfillment, referral or Prime fee change, and no Prime fee history, is stated in any Amazon document on disk** (10-Ks FY2015,
  FY2017-FY2025; three 10-Qs; four releases; the search list is in `peers/tableB_retail.md` B.5(a)). The filing says only *"We earn fixed fees, a
  percentage of sales, per-unit activity fees, interest, or some combination thereof"*.
- **What is filed moves with volume, not price:** third-party seller services grew 7-16% ex-FX by quarter against paid-unit growth of 8-17%, with the
  seller unit mix flat at **60-62%** of paid units from Q2 2024 to Q2 2026. Revenue per seller unit is not rising on this evidence.
- **Sellers' alternatives, in a rival's filing:** eBay 10-K FY2025: *"Consumers and merchants that sell goods on our platforms also have many
  alternatives, including general ecommerce marketplaces, such as Amazon and Alibaba"*; *"Sellers may also choose to sell their goods through alternative
  channels, such as multi-channel services like Shopify"*. Shopify GMV $378.4bn, +29.5% (10-K `0001594805-26-000007`).
- **The strongest evidence FOR near-monopoly is an allegation, and it points at criterion (3), not at a moat certificate.** 10-K FY2024: the FTC complaint
  alleges *"that Amazon has a monopoly in markets for online superstores and marketplace services, and unlawfully maintains those monopolies through
  anticompetitive practices relating to our pricing policies, advertising practices, the structure of Prime, and promotion of our own products"*, and *"All
  three courts ... denied dismissal of claims alleging that Amazon's pricing policies are an unlawful restraint of trade."* The relief sought is
  *"injunctive and structural relief"*; Italy has already imposed *"remedial actions"* and a fine cut to €752 million. **[E5-28]** says incredible pricing
  power means *"a monopoly or a near monopoly"* — and **[E2-59]** says where a regime reaches the practices a franchise rests on, the moat belongs partly to
  the regime. **The three practices a seller-side franchise case would rest on (pricing policies, advertising placement, the structure of Prime) are the
  three under suit.** Recorded; not a finding of fact.

**Leg verdict: the stores are a strong low-price business, not a franchise under criterion (2); the marketplace's pricing cannot be tested from the filing.**
Class NARROW, direction **widening on margin and units**.

### LEG 2a — Advertising ($76.1bn TTM; no margin, price or unit figure filed)
- **The strongest candidate in the company, stated at full strength:** sponsored placement on the shelf where shoppers arrive intending to buy is not
  sold by anyone else; revenue **$31.2bn (2021) → $68.6bn (2025), 21.8% a year**; **+25.1%** in H1 2026, faster than Google advertising (+14.9%) and at
  Meta's rate (+30.1%). If any leg is a toll, it is this one.
- **What the filing lets the test see: nothing about price.** Alphabet files paid clicks and cost-per-click; Meta files impressions and price per ad; **Amazon
  files neither, nor any advertising margin** (0 hits; `peers/tableC_ads_and_cloud_text.md` C.2, C.3). **[E3-03]'s pricing sentence cannot be run on this
  leg from any document**, and the one price statement found is a cut: *"Advertisers using Ads Agent see 8% lower cost-per-impression"* (Q2 2026 release).
- **Substitutes for the advertiser's dollar are named and growing:** Meta's 10-K FY2025 and 10-Q Q2 2026: *"the online commerce vertical was the largest
  contributor to the increase in advertising revenue"*; Walmart Connect in the U.S. *"up 43%"* (ex-VIZIO, Q2 FY2027 release).
- **Can I name the document that would resolve this leg?** No Amazon filing discloses advertising price, volume or profit, so the leg's franchise case is
  **unresolvable from the record** — and **it is not decisive**: advertising sits inside segments earning 42% of operating income, and granting it a full
  franchise does not move the weight below.

---
### THE COMPETITOR ROW — required **[E3-28]** *(CONVENTION, confessed at VI)*
Full row with accessions: `Test Runs/_research 2026-09-13 AMZN/peers/competitor_row.md` (Table A cloud; B retail and marketplace; C advertising;
naming and multi-sourcing sweeps). Arithmetic ratios.

| | **Amazon** | Microsoft | Alphabet | Oracle | Walmart | eBay | Meta |
|---|---|---|---|---|---|---|---|
| Cloud segment margin, latest FY | **AWS 35.4%** | IC 41.3% | GC 23.7% | not filed | — | — | — |
| Cloud growth, latest FY / H1 2026 | **+19.7% / +32.7%** | +29.7% / +30.7% | +35.8% / +73.1% | infra +76.9% / +120.7% (Q1 FY27) | — | — | — |
| Backlog / RPO | **$496bn** (6.4 yrs) | $678bn commercial | $513.9bn GC | $664bn | — | — | — |
| Capex ÷ depreciation, latest FY | **3.15×** | 3.38× | 4.33× | 7.30× | 1.88× | 1.29× | — |
| Filed cloud price conduct | **"partially offset by pricing changes", 13 years** | no executed change filed | none filed | none filed | — | — | — |
| Retail margin, latest FY | **NA 6.9% · Intl 2.9%** | — | — | — | U.S. 5.2% · Intl 3.9% | 20.5% (marketplace) | — |
| E-commerce growth, latest FY | **NA sales +10.0%; 3P services +10.3%** | — | — | — | eCommerce +24.4% | GMV +7% | — |
| Advertising growth 2025 / H1 2026 | **+22.1% / +25.1%** | search +9.4% (FY26) | +11.4% / +14.9% | — | +46% incl. VIZIO / +38% (Q2) | ads +22% | +22.1% / +30.1% |
| Ad price or unit metric filed | **none** | — | CPC +3%, clicks +13% | — | none | none | price/ad +12%, impr. +14% |

- **Peers named: 9 companies** (Microsoft, Alphabet, Oracle; Walmart, eBay, MercadoLibre, Shopify, PDD; Meta) across the three legs, of perhaps a dozen
  real competitors. **Not rowed, and stated:** Alibaba (20-F, not fetched), Temu (inside PDD), Shein and the Chinese and private clouds (no SEC filings),
  CoreWeave (not fetched). **None is load-bearing**: the AWS verdict rests on Amazon's own pricing sentence and three filed rivals; the stores verdict on
  Amazon's own competitive-factor text and Walmart's filed dollars. **Not PROVISIONAL.**
- **Names Amazon as a competitor?** Oracle (Item 1, and Item 1A's multicloud sentence) and eBay (twice, Item 1A). Alphabet, Meta, Microsoft, Walmart,
  Shopify and PDD: no instance found. Amazon's own 10-K names no competitor.
- **The row's limit [E3-61]:** it shows position, not conduct. Whether four hyperscalers behave like *"a demented Kellogg"* in a capacity glut, no filing
  and no model can say.
- **Untapped pricing power [E3-33]:** **not claimed for any leg.** AWS prices down; the stores price down by policy; the marketplace and advertising
  prices are not filed. **[E5-28]:** the near-monopoly claim exists only as a contested allegation whose remedy would cap it.
- **[E4-23] key person:** none filed; not a moat defect here.
- **[E2-53] dominance class:** not met for any leg on the row (a rival grows faster in every one).

### What the franchise case rests on — stated at full strength, because it is the strongest case against this verdict **[E4-26, E4-51]**
*"Amazon is three tolls. AWS is the largest installed base of cloud workloads, earning 36.8% on $148bn, with $496bn of contracted revenue over 6.4
years and its own chips; the stores are the default shelf of the Western internet, with paid units accelerating to +17% and North America's margin up a
point in a year; and on that shelf Amazon sells $76bn a year of advertising nobody else can sell, growing faster than Google. Regulators and plaintiffs on
three continents say it is a monopoly. The capital is going into AI capacity that two of the world's leading laboratories have contracted to buy for a
decade."*
**The answer, on the filed record:** (1) the tolls are not priced up: AWS's own MD&A has said for thirteen years that price moved against revenue, and the
stores' own strategy is lower prices; the one leg that might be a toll files no price at all; (2) the contracted revenue comes largely from two customers
Amazon is funding, one of which also buys $24.1bn a year from Microsoft; (3) the leading position in cloud is a wave, and the filer itself shortened its
server lives for the pace of change — [E4-04]'s excluded class in its own words; (4) the monopoly claim is an allegation whose remedy is aimed at the very
practices a franchise case would rest on; (5) even granting advertising and the marketplace a franchise in full, **58% of the profit and 76% of the new
capital are in the AWS leg**, and the queue's weighting practice (HAS, SONY) passes a bundle only where the franchise leg carries the weight and the rest
eats no material capital. **The strongest case is real, and it describes excellent businesses; [E3-03] asks a narrower question, and the filings answer it.**
The omission cost of a wrong close **[E3-47]** is acknowledged: this is the largest business in wave 5, and the reopening conditions at Q6 are written to
catch the error.

- **Class: [ ] WIDE [x] NARROW [ ] NONE [ ] PROVISIONAL** · **Direction: MIXED** — narrowing at AWS (returns on segment assets 30.1% → 18.1%, growth
  last of four, backlog behind three rivals), widening in the stores on margin and units, advertising growing faster than Google with its pricing unfiled;
  **and the capital is going into the narrowing leg.**
- **Can I name the document that would resolve it?** For AWS and the stores, the documents exist and were read, and they answer criterion (2). For
  advertising, no filing discloses price or profit, and that leg does not carry the weight. **So the verdict is not UNRESEARCHED and not UNKNOWABLE.**
- **VERDICT: [ ] IN  [x] OUT**  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *OUT on the business as constituted, on [E3-03] criterion (2) as [E3-03]'s own pricing sentence, [E2-44](1) and [E4-04] test it: the AWS leg, which
  earns 58% of operating income on three-quarters of the new capital, has had price move against its revenue in every filed year from 2013 to H1 2026,
  sells a service three filed rivals sell and its largest customers buy from them too, and replaces its basis on five-year lives the filer shortened for
  the pace of AI; the stores compete on price by their own description; advertising, the strongest candidate, files no price and does not carry the weight.
  Not a finding that any leg is a poor business. **The file closes here.** Q3-Q6 below are RECORDED, NOT GOVERNING.*
