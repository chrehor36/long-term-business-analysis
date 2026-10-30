# Company Run — Certara, Inc. (CERT) — 2026-09-07
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

---
## STEP 0 — THE RATE, THE COVER, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- rate **5.24 %** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority; struck fresh this session, not the FRED fallback)**
- FX: **none for the quote.** Certara reports and is quoted in USD. It does earn abroad —
  the 10-K names operations in nineteen countries and **$76.2M of the $189.4M cash balance
  is held outside the United States** — but the reporting currency is USD and no ADR ratio
  applies. Recorded as a translation exposure at Q4, not a quote-conversion problem.

**THE COVER COUNT, BY HAND.**
- 10-Q filed **2026-08-04**, accession **`0001827090-26-000028`**, period **2026-06-30**,
  cover verbatim: *"As of August 1, 2026, the registrant had **152,538,780** shares of
  common stock, par value $0.01 per share, outstanding."* **The operator's figure verifies
  to the digit.**
- **Independent cross-check inside the same filing.** The balance sheet reads: *"Common
  shares, $0.01 par value, 600,000,000 shares authorized, **166,959,761** shares and
  164,005,450 shares **issued** as of June 30, 2026 and December 31, 2025; **152,499,023**
  and 159,139,562 shares **outstanding**."* Cover (152,538,780, at 2026-08-01) against
  balance sheet (152,499,023, at 2026-06-30) differ by 39,757 shares over one month —
  ordinary vesting. **Both agree.**
- **Single class.** No preferred issued or outstanding. No split in the filing history.
- **A live buyback, and it is large relative to the cap.** Shares outstanding fell
  **159,139,562 → 152,499,023** in six months, −4.2%. Held at Q3.

- **price $7.94 · 2026-09-04 · aggregator, FLAGGED, live quote only** (operator rule 5)
- **shares 152,538,780** (10-Q cover, 2026-08-01)
- **MARKET CAP = $7.94 × 152,538,780 = $1,211M**
  *(the screen row's $1,236M used a slightly earlier quote; the difference is 2% and
  changes nothing. This run uses $1,211M.)*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: FY2025 10-K, FYE 2025-12-31, filed 2026-02-26, accession
  `0001827090-26-000011`** (`cert-20251231.htm`).
- Also read in full: FY2024 10-K `0001827090-25-000014`; FY2023 10-K `0001827090-24-000006`;
  FY2022 10-K `0001558370-23-002605`; FY2021 10-K `0001558370-22-002608`; Q2 2026 10-Q
  `0001827090-26-000028`; DEF 14A 2026 `0001104659-26-039372`; DEF 14A 2025
  `0001104659-25-032816`.
- **Figure cross-checked against the filed statement:** XBRL returns FY2025 operating cash
  flow of $96,325k. The filed Consolidated Statements of Cash Flows shows **"Net cash
  provided by operating activities 96,325"** — agrees to the dollar. Second cross-check,
  because the (c) judgment turns on it: XBRL `DepreciationDepletionAndAmortization` FY2025 =
  $75,162k; the filed cash-flow statement shows **"Depreciation and amortization 75,162"** —
  agrees to the dollar, and it is **$18,606k larger than the $56,556k "Depreciation and
  Amortization" line the MD&A discusses**, because amortisation of capitalised software sits
  in cost of revenue. Recorded here because that gap is exactly where an owner-earnings error
  would hide.

---

## THE SCREEN ROW — REPRODUCED TO THE DECIMAL, AND IT IS THE EIGHTH CONSECUTIVE SPREAD DEFECT

**The published row:**

    CERT, cap_m 1236 · oe_bottom_m 28 · oe_top_m 35 · spread 0.232 · yield_bottom 2.28%
    vs_sovereign −2.96 pts · growth_required 7.72% · level_shift 1.47 "no step"
    best_year_dep 0.06 · acq_note "$432M, 35% of cap, inside the window"
    newest_filing 2025-12-31

**BOTH ENDS REPRODUCE, AND NEITHER OF THEM IS A CAPEX END.** Re-running
`tools/run.py:owner_earnings` on today's facts returns, to three decimals:

| window | `mean_lo` (the "D&A" end) | `mean_hi` (the capex end) |
|---|---|---|
| 3-year 2023–25 | **28.153** | 52.819 |
| 5-year 2021–25 | **34.739** | 49.797 |

`oe_bottom 28` is the **3-year** `mean_lo`. `oe_top 35` is the **5-year** `mean_lo`.
The published "spread" is `(34.739 − 28.153) ÷ 28.153 = 0.234`, which rounds to the
published 0.232. **Two windows, one end — and the end used is the D&A end at both.**
The capex end (49.8 / 52.8) never entered the published row at all. This is the identical
structural defect the CRWD run recorded earlier the same day: *a window spread wearing a
capex band's clothes*. The framework requires the band to be the capex judgment
**[E2-23, E3-44, E5-20]** and the window spread to be carried *alongside* it **[E4-25]**.

### **AND THE D&A SERIES IT USED IS BROKEN IN A WAY NO PRIOR RUN HAS RECORDED**

This is a **new defect class** and it is worth more than the row. `da_annual()` **does**
return a series for this filer — the operator asked me to check whether it returns anything,
and the answer is that it returns something, **which is worse than returning nothing**:

    da_annual(CERT) -> 2019: 2.60 | 2020: 2.44 | 2021: 2.13 | 2022: 1.73
                       2023: 1.55 | 2024: 1.99 | 2025: 75.16

**A 38x discontinuity inside one seven-year series, printed without a flag.** The cause is
in the filings and it is legitimate accounting. Through the FY2022 10-K, Certara's income
statement carried **two** lines — *"Intangible asset amortization 41,429"* and
*"Depreciation and amortization expense 1,731"* — and tagged only the second as
`DepreciationAndAmortization`. From the FY2023 vintage the presentation was consolidated and
the same tag began carrying the combined figure. **The XBRL element did not change; its
semantic content did, because the filer changed presentation mid-window.** Nothing in the
pipeline detects that, and the consequence is that the published `oe_bottom`/`oe_top` for
2021 and 2022 subtracted **$2.1M and $1.7M** as "maintenance capital" from a company that
actually spent **$8.9M and $12.5M** — so for those two years the row's "conservative" end was
in fact the *generous* one. **The band is inverted mid-series.** Recorded as a tooling
finding, not as a company finding.

### **THE CAPITALIZED-SOFTWARE FIX WORKS — AND THE PUBLISHED ROW DID NOT USE IT**

The operator's correction 3 asked me to check for a separately-tagged capitalised-software
line. There is one, and it is **fourteen times larger than PP&E capex**:

> *"Capital expenditures **(1,760)** … Capitalized software development costs **(24,796)**"*
> — filed Consolidated Statements of Cash Flows, FY2025 10-K

`Screens/floor_screen.py:capital_acquired()` **resolves it correctly** — it returns
9.52 / 7.94 / 8.90 / 12.53 / 15.27 / 21.04 / **26.56** for 2019–2025, which reconciles to the
filed statement to the dollar in every year. The HAS fix of 2026-09-03 works on this filer;
`PaymentsForSoftware` is the element and it is in `SOFTWARE_CAPX_TAGS`. **But the published
row came through `tools/run.py`, whose `CAP` list still contains only
`PaymentsToAcquirePropertyPlantAndEquipment`, and `tools/screen.py` imports
`owner_earnings` from `run.py`.** The fix exists in one of the two owner-earnings paths.
**Recorded as a live tooling defect: the two paths disagree, and the queue was built from
the unfixed one.**

### **`level_shift 1.47 "no step"` AND `best_year_dep 0.06` ARE BOTH CORRECT AND BOTH BENIGN**

Unusually for this queue, these two flags are right. Operating cash flow really has been a
level — $60.4M, $92.5M, $82.8M, $80.5M, $96.3M across 2021–25, a 1.47x range with no step —
and no single year carries the window (best-year dependence 0.06). **The volatility here is
not in the cash flow. It is entirely in what you subtract from it**, which is precisely the
quantity the row got wrong.

### **THE ACQUISITION FLAG IS LIVE, IT IS THE BIGGEST FACT ON THE ROW, AND IT IS UNDERSTATED**

The row says **$432M, 35% of cap**. That figure is the **investing-section cash line only**.
Read from the business-combination notes, total consideration in the same window was:

| year | acquisitions | **total consideration** | cash in *investing* |
|---|---|---|---|
| 2021 | Author! B.V. $2.7M · Insight Medical Writing $15.2M · **Pinnacle 21 $339.1M** | **$357.0M** | $261.0M |
| 2022 | Integrated Nonclinical Development Solutions $8.0M · Vyasa Analytics $29.3M | **$37.3M** | $15.3M |
| 2023 | DIDB $8.3M · Formedix $41.4M · Applied BioMath $36.6M | **$86.3M** | $64.2M |
| 2024 | **Chemaxon $96.4M** | **$96.4M** | $91.3M |
| 2025 | none | **$0** | $0 |
| | | **$577.0M** | **$431.8M** |

**$577.0M of consideration against a $1,211M market cap — 47.6%, not 35%.** The gap is
$145M and it is in two places the operating-cash-flow numerator cannot see:

1. **Stock.** Pinnacle 21 was *"a total consideration of $339.1 million, consisting of cash
   $266.3 million … and **2,239,717 shares of our restricted common stock**"* — the equity
   statement carries *"Common shares issued in connections with the Pinnacle acquisition
   $72,760"*. A further **$3,707k (2024) and $5,670k (2025)** of shares were issued to settle
   acquisition contingent consideration.
2. **Financing.** *"Payments for business acquisition related contingent consideration"* —
   **$15,156k (2024) and $13,230k (2025)**, sitting in the financing section.

**And the round trip is invisible from both ends.** The Vyasa earnout was expensed through
G&A and then **added back as a non-cash item inside operating cash flow** — *"Change in fair
value of contingent considerations 24,118 (2023) / 8,089 (2024) / (3,597) (2025)"* — and then
**paid in cash out of financing**. An owner-earnings numerator built from operating cash flow
**[CONVENTION, v4.1]** never sees the expense and never sees the payment. $37.8M of
acquisition consideration was settled in 2024–25 entirely outside operating cash flow.

**The operator's instruction was to check every 8-K/A. There are none.** Recorded sweep of
the full submissions feed for CIK 1827090: **zero filings of form 8-K/A in the company's
entire history**, because every acquisition was disclosed as *"not significant to our
consolidated financial statements"* and none triggered a Rule 3-05 financial-statement
requirement. **The Broadcom method — let the filed pro forma do the perimeter work — is
unavailable here.** The perimeter had to be built by hand from the notes, and that is what
the table above is.

### **THE ROW'S LARGEST OMISSION IS NOT A DEFECT IN THE ROW. IT IS A DATE.**

`newest_filing 2025-12-31`. **The company sold a business line four months ago and the row
cannot see it.** See Q1.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics, in my own words, without management's language.** A drug company must
prove to a regulator that a dose is safe and effective. Doing that entirely by dosing humans
is slow and expensive. Certara sells two things that substitute computer work for some of
that human work.

The first is **software**: mathematical models of how a compound moves through a body, sold
as an annual licence or subscription to the scientists who run the simulations. In 2025 this
was **$183.3M, 44% of revenue.** The second is **services**: Certara's own PhDs run the
simulations for the customer, write the report, and — in the part of the business just
divested — wrote the regulatory submission itself. In 2025 that was **$235.6M, 56% of
revenue.**

**These are two different businesses and the operator was right to insist on the split.**
The software half is a licence renewed annually against a model the customer's scientists
have learned and validated; the marginal cost of the next licence is near zero. The services
half is people at a day rate — the marginal cost of the next project is another PhD, and
growth requires hiring. **They do not have the same economics and the framework's franchise
test does not return the same answer on both.**

**Does Certara file segment gross profit? No, and the answer is structural.** Recorded sweep
of the FY2025 10-K: the company reports **one** reportable segment. Note 14 verbatim: *"The
Company manages its operations as a single segment for the purpose of assessing and making
operating decisions. The Company's CODM allocates resources and assesses performance based
upon financial information at the **consolidated level**."* Cost of revenues is a single
$161.1M line covering both halves. **There is no filed gross margin for software and none for
services, and there has never been one in six 10-K vintages.** So the AMAT move — waiting for
a segment gross margin to arrive and letting it kill the claim that the services half is the
quality half — **cannot be run here.** The document that would resolve it does not exist, and
the company states in terms that it does not manage the business in a way that would produce
it. That is an **UNKNOWABLE sub-question inside an IN gate**, and it is recorded as a limit
on everything below rather than papered over.

*(The company does disclose **three reporting units for goodwill purposes** — Certara Data
Science Software, Certara Predictive Technologies, and Certara Drug Development Services —
"within a single operating segment." That is the closest thing to a segment split in the
file, and it exists only to be impairment-tested. It has been used for exactly that once.
See Q3.)*

**What I could get instead is the revenue split by half over five vintages, and it answers
the operator's question a different way:**

| $M | 2021 | 2022 | 2023 | 2024 | 2025 | 4-yr CAGR |
|---|---|---|---|---|---|---|
| **Software** | 86.8 | 115.5 | 131.7 | 155.7 | **183.3** | **+20.5%/yr** |
| **Services** | 199.3 | 220.2 | 222.7 | 229.5 | **235.6** | **+4.3%/yr** |
| Total | 286.1 | 335.6 | 354.3 | 385.1 | **418.8** | +10.0%/yr |

**The 56% of revenue that is services has compounded at 4.3% a year for four years — and
that figure INCLUDES the services businesses Certara bought over the same window** (Insight
Medical Writing 2021, Integrated Nonclinical Development Solutions 2022, Applied BioMath
2023). Organic services growth is below 4.3% and the filings do not let me say by how much.
The 20.5% on the software line is likewise not what it looks like: Pinnacle 21, Formedix,
Vyasa, DIDB and Chemaxon all landed in it.

**The company's own organic figure, filed, closes the question:**

| | 2024 | 2025 |
|---|---|---|
| Total revenue | $385.1M · **+9%** | $418.8M · **+9%** |
| Revenue related to acquisitions | $(27.4)M · 7 pts | $(17.0)M · 3 pts |
| **Organic revenue** | $357.7M · **+2%** | $401.8M · **+6%** |

**In 2024, seven of the nine points of growth were purchased. Organic growth was 2%.**

**The scarce input this business controls.** Not the mathematics — the equations are
published science, and Certara's own 10-K names **open-source substitutes by name**. Not the
scientists — they are hireable, and the services half is nothing but hired scientists. What
is genuinely scarce is **the validated model plus the regulatory precedent attached to it**:
a simulation engine a reviewer at the FDA has seen before, in submissions that were approved,
and that the customer's own scientists have already qualified inside their quality system.
That is a real asset, and it is why the software half prices better than the services half.
**It is also an asset Certara owns in the software half and essentially does not own in the
services half**, where the scarce input is a PhD's time and the competitor set is the whole
contract-research industry.

**Will the fundamentals look broadly the same in ten years?** **Here Q1 gets its hardest
test, and it is not the science — it is that the company itself has just changed shape.**

> *"On April 21, 2026, the Company entered into a definitive Purchase Agreement … with
> Veristat, LLC to sell its global medical writing and related regulatory services business
> … On May 8, 2026, the Company completed the sale."* — 10-Q, accession
> `0001827090-26-000028`

**A new CEO took office on 2026-01-01** — Jon Resnick succeeded William Feehery, whose
2025-12-31 departure the 2026 proxy records as a *"termination without cause"* — **and four
months later sold a business line.** Every historical figure in this run describes a company
that no longer exists in that form. The 10-Q restates all prior periods for the discontinued
operation; the FY2025 10-K, which is the newest annual filing and the one the screen row
used, does not.

**Is that enough to fail Q1? No, and I want to say why rather than wave it through.**
[E3-31] asks whether the business is *"relatively simple and stable in character"* and
whether I can *"predict future cash flows."* The **revenue mechanism** is simple and I have
stated it in two sentences. The **disposal narrows the perimeter rather than changing the
mechanism**: what left was the medical-writing services line, the least software-like part of
the company and the part I would have discounted hardest in any case. The remaining company
sells biosimulation software and biosimulation services, and I understand both. **Q1 asks
whether I can understand how the money is made, and I can.**

**What I record and carry forward, unresolved, to Q2:** the [E3-31] instability concern is
live in its *second* form — not "is the science too complex" but **"is this the same business
from year to year at all."** Twenty-one acquisitions since 2013, $577M of consideration in
five years, one $47.0M goodwill impairment, one divestiture at a $65.5M loss, and a new CEO.
That is adjudicated at Q2 under **[E4-04]** — *does the spending defend the same advantage,
or buy its replacement?* — which is where the framework puts the mechanism.

- **VERDICT: [x] IN**
  *Recorded and carried: the software half and the services half are different businesses,
  the company files no gross margin for either, 56% of revenue compounds at 4.3%, and the
  perimeter changed in May 2026. None of that is a Q1 failure; all of it is Q2 evidence.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — yes. Model-informed drug development is now part of how drugs
  get approved, and the filing evidences it below.
- No close substitute **[ ]** — **FAILS, and the evidence is Certara's own competition
  section naming free substitutes by name.**
- Not price-regulated **[x]** — no price regulation on the software or the services.

### **FIRST, THE OPERATOR'S PRIOR, TESTED — AND IT IS HALF CONFIRMED AND HALF REFUTED**

*The prior: "the moat claim rests on regulatory acceptance — that FDA and EMA accept
model-informed drug development submissions built on Certara's tools. Test whether the
filings actually say this or whether it is deck language."*

**It is not deck language. It is in the 10-K, and it is more specific than the prior
assumed.** Three filed statements, all from the FY2025 10-K, accession
`0001827090-26-000011`:

> *"Our software products are licensed by more than **160,000 users** and are also **used by
> 20 global drug regulatory agencies**, including the FDA, Japan's Pharmaceuticals and
> Medical Devices Agency (the "PMDA"), and China's Center for Drug Evaluation (the "CDE")
> within the National Medical Product Administration (the "NMPA")."*

> *"Certara supports applications to **all major health agencies**, including the FDA, the
> European Medicines Agency (the "EMA"), Health Canada, Japan's PMDA, and China's NMPA."*

> *"According to **our internal data**, Certara's customers have received **90% or more of
> all novel drug approvals** by the U.S. Food and Drug Administration … from 2014 through
> 2025."*

And from the FY2022 10-K on the largest acquisition in the company's history:

> *"**Pinnacle's products are used by the FDA and Japan's PMDA to review the quality of
> submissions.**"*

**That last one is the strongest sentence in the file for the moat case.** The regulator
does not merely accept submissions built on the tool; the regulator runs the tool on its
own side of the desk. A vendor whose software sits inside the reviewing agency has a
switching cost its customers cannot unilaterally resolve. **The prior is CONFIRMED, filed,
and I am not going to discount it.**

**But the prior is also refuted in the place that decides Q2, and the refutation is in the
same document.** Three things cut against it:

1. **The company says its product is not approved by anyone.** *"Although our biosimulation
   software products and platforms are **not approved by the FDA or other government
   agencies**, our customers' products are subject to these regulations."* There is no
   licence, no exclusivity, and no regulatory barrier to a competitor's model being used in
   a submission. What exists is familiarity, not authorisation.
2. **The company ranks regulator acceptance as ONE OF NINE competitive factors, not as the
   moat.** *"In our view, the principal competitive factors in our market are the
   functionality and quality of models, the breadth of molecular types, therapeutic areas,
   and modalities supported, **regulator acceptance of our solutions**, ease of use and
   functionality of applications, depth of experience in drug development, brand awareness
   and reputation, total cost, and the ability to securely integrate with other enterprise
   applications."* Nine factors, one of which is regulator acceptance, in the company's own
   ordering.
3. **The company files a risk factor saying regulatory acceptance could go the other way.**
   *"**Deceleration in, or resistance to, the acceptance of model-informed biopharmaceutical
   discovery and development by regulatory authorities** or academic institutions could
   damage our reputation or reduce the demand for our products and services."* Regulatory
   acceptance is disclosed as a **demand driver that can reverse**, not as an owned
   position. Under [E2-59] that is the correct reading: **regulation floors or lifts a
   business; it does not create the franchise class.** *"the moat belongs to the regime."*

### **[E3-03] CRITERION (2) — "NO CLOSE SUBSTITUTE" — FAILS ON THE COMPANY'S OWN WORDS**

> *"In the biosimulation software market, we compete with other technology companies
> including **Mathworks, Dassault Systemes, Ansys, Simulations Plus, and NONMEM, a division
> of ICON**. **Other competitors include open-sourced solutions such as R and PK-Sim** and
> **internally developed software from biopharmaceutical companies**."*
> — FY2025 10-K, Competition

**A company that names five commercial competitors, two free open-source substitutes, and
its own customers' in-house software, in its own competition section, is telling you its
product is not thought by its customers to have no close substitute.** [E3-03] criterion (2)
is a claim about what customers *think*, and the honest reading of that sentence is that
they think there are alternatives, including alternatives that cost nothing. **PK-Sim is
open-source PBPK software — the same category as Certara's Simcyp — and R is the language
half of pharmacometrics runs in.** This is a materially worse position on criterion (2) than
the CRWD run found, because there the substitute was commercial; here the company names a
free one.

*(Stated fairly the other way, because it is the honest counter: Certara adds in the same
paragraph that *"the time, effort, and investment necessary to develop validated models,
modeling solutions, enterprise software and extensive MIDD experience presents a
**significant barrier to new entrants**."* That is a real claim and the 160,000-user and
20-agency figures support it. **A barrier to entry is not the same thing as an absence of
substitutes**, and [E3-03] asks for the second.)*

### **THE FILED METRICS — AND I MUST CORRECT MY OWN WORKING ASSUMPTION HERE**

**I initially recorded, from a phrase-level sweep, that Certara names net retention and
bookings as key performance indicators and never quantifies them. That was wrong, and the
error was mine: the numbers sit in a table separated from the defining sentence.** Certara
publishes both, quarterly, with three years of history. Correcting it in the run rather than
after it, per prime rule 2.

**And the correction matters in Certara's favour on disclosure and against it on
substance.** The company introduced this table in the FY2024 10-K, in the same vintage in
which the older ACV metric disappeared. That is a **metric swap for a better metric, not a
withdrawal**, and under [E2-49] it is the candid form rather than the flagged one.

**Filed net software retention rate — the [E2-44](1) price test, run on the company's own
series:**

| | Q1 | Q2 | Q3 | Q4 | **FULL YEAR** |
|---|---|---|---|---|---|
| 2022 | 101.5% | 104.5% | 104.3% | 109.2% | **105.1%** |
| 2023 | 108.3% | 110.5% | 106.4% | 103.4% | **108.4%** |
| 2024 | 114.1% | 108.0% | 107.6% | 105.5% | **108.8%** ← peak |
| 2025 | 102.4% | 107.6% | 103.9% | 107.2% | **105.3%** |
| **2026** *(continuing ops)* | **106.1%** | **101.5%** | — | — | — |

**The definition is the company's and it is the one that matters:** *"our net retention rates
measure the percentage of recurring revenue that is retained from existing software
customers over a specific period of time, **inclusive of price increases and expansion**,
excluding revenue from acquisitions occurred within the past 12 months."*

**So the whole of price increases plus expansion plus churn nets to 5.3% for 2025 and 1.5%
in the latest filed quarter.** [E2-44] asks whether the business can raise prices *"even when
product demand is flat and capacity is not fully utilized."* On the company's own metric, at
the latest reading, price and expansion together bought **one and a half points**. [E4-37]
supplies the inverse metric — *"you can almost measure the strength of a business over time
by the agony they go through in determining whether a price increase can be sustained"* —
and a 101.5% reading on a measure that explicitly includes price increases is what the agony
end of that scale looks like in a number.

**Filed bookings — the demand series:**

| $M | Q1 | Q2 | Q3 | Q4 | **FULL YEAR** |
|---|---|---|---|---|---|
| 2022 | 108.5 | 100.3 | 79.8 | 120.4 | **409.0** |
| 2023 | 112.7 | 85.9 | 84.8 | 118.9 | **402.3** (−1.6%) |
| 2024 | 105.8 | 98.9 | 96.1 | 144.5 | **445.3** (+10.7%) |
| 2025 | 118.2 | 112.0 | 96.6 | 155.3 | **482.1** (+8.3%) |
| **2026** *(continuing)* | **97.2** | **98.3** | — | — | H1 **195.5** |
| 2025 *(continuing, restated)* | 98.4 | 97.4 | — | — | H1 **195.8** |

**On a like-for-like continuing-operations basis, bookings in the first half of 2026 were
$195.5M against $195.8M a year earlier — down 0.2%.** The operator asked for the
bookings/backlog trend on a customer base of cash-constrained biotechs. That is it: flat.
The remaining-performance-obligation series says the same thing — **$150.8M at 2025-06-30
against $151.0M at 2026-06-30, up 0.1%** after growing 25% the year before.

### **[E4-55] — WHERE UNITS EXIST, MONITOR UNITS. ONE UNIT SERIES EXISTED AND IT WAS WITHDRAWN.**

*Dollar revenue flattered by pricing is how a shrinking franchise hides; the physical series
is the honest one.* **[E4-55]**

The only customer-count series Certara ever filed was the number of customers with Annual
Customer Value of $100,000 or more:

| year | customers with ACV ≥ $100k | growth |
|---|---|---|
| 2020 | 261 | — |
| 2021 | 299 | **+15%** |
| 2022 | 370 | **+24%** |
| 2023 | 389 | **+5.1%** |
| 2024 | **WITHDRAWN** | — |
| 2025 | withdrawn | — |

**Recorded sweep:** the FY2024 and FY2025 10-Ks were searched for `ACV`, `Annual Customer
Value` and `annual customer value` in any case. **Zero instances in either — no instance
found in two filings searched.** The series was last filed in the FY2023 10-K, in the
vintage in which its growth rate collapsed from 24% to 5.1%, and it has not appeared since.

**Stated at full strength both ways, because this is the one place [E2-49] could be
over-read.** The disposal-of-the-yardstick pattern fits the dating exactly: the metric went
in the year it went bad. **But the same vintage that dropped it introduced the bookings and
net-retention tables**, which are better metrics, quantified, with three years of history and
quarterly granularity. On [E2-49]'s own standard — *"pre-set, long-lived and small
bullseyes"* — what Certara has today is **better disclosure than what it withdrew.** I record
the dating, I decline to call it a flag, and I note that the replacement metric is the one
now deteriorating.

### **[E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT? THIS IS WHERE Q2 IS DECIDED.**

*The framework's test: does a lapse in spending destroy the structure, or merely narrow it —
and **does the spending defend the same advantage, or buy its replacement?***

**Certara buys its replacement, and the filings quantify how much.** Over 2021–2025:

| | $M | as % of the $1,211M cap |
|---|---|---|
| Total acquisition consideration | **577.0** | **47.6%** |
| R&D expensed (inside OCF) | 161.3 | 13.3% |
| Capitalized software development (in investing) | 76.6 | 6.3% |
| **Total spend on product and position** | **814.9** | **67.3%** |
| Owner earnings produced over the same five years, generous end | **171.9** | 14.2% |

**Certara spent $815M over five years to produce $172M of cumulative owner earnings** — and
that is at the *generous* (c) end computed at Q4. The company's own organic growth figure
says what the acquisition half bought: **2% organic in 2024, 6% in 2025, and +1% total
revenue in the latest quarter.**

**The balance sheet is the same fact in stock terms.** At 2026-06-30, goodwill $718.1M plus
intangibles $345.2M is **$1,063.3M against $1,399.8M of total assets — 76.0%.** Net tangible
equity is **negative $96.8M.** Of the $863.3M gross intangible base at year-end 2025,
**$762.1M (88%) was purchased** and only $101.2M was internally developed. **Three-quarters
of this company is what it bought**, and property and equipment net is **$1.7M** — a
$1.4bn balance sheet with less than two million dollars of physical plant.

**Mitsui's Rhodes Ridge, not Coca-Cola's trademark.** The [E4-04] mechanism is
**competitive destruction**, and the twenty-one acquisitions since 2013 are the tell: the
advantage does not renew itself, it is repurchased. A lapse in acquisition spending would not
merely narrow this structure; on the filed organic numbers it would leave a business growing
at 2–6% while amortising $54.4M a year of previously-purchased customer relationships.

### **[E5-40] — AND THE SERIAL ACQUIRER HAS TOLD YOU THE RETURNS, TWICE, IN WRITING**

*"a serial acquirer that has impaired what it bought is telling you the returns"* — the
operator's prior, and it is confirmed with the two hardest numbers in this file.

**One line of business, assembled by acquisition, written down and then sold at a loss:**

1. **2021 — bought.** Author! B.V. (March, $2.7M) and **Insight Medical Writing Limited**
   (June, $15.2M), both regulatory/medical-writing businesses.
2. **2023 — impaired.** *"Goodwill impairment expense was **$47.0 million** for the year
   ended December 31, 2023 … due to recognizing a goodwill impairment for **legacy regulatory
   and writing reporting unit** as the carrying value exceeded its fair value."*
3. **2026 — sold at a loss.** *"On May 8, 2026, the Company completed the sale of the
   **Regulatory and Medical Writing business** to Veristat, LLC. The Company received cash
   consideration of **$69,435**, with an additional $15,000 placed in escrow … The
   transaction resulted in an estimated **pretax loss on sale of $65,481**, including an
   estimated after-tax loss of $48,576."*

**$47.0M of impairment plus $65.5M of loss on disposal is $112.5M destroyed on one line of
business — 9.3% of the entire market capitalisation.** [E5-40] asked for the returns; the
company has published them.

*(Fairly stated, and it is a genuine point for the new management: **selling it was the right
decision and it was made quickly.** The proceeds are real cash, the perimeter is now cleaner,
and the 10-Q says the sale *"is part of management's strategy to simplify the Company's
portfolio and focus on its core businesses."* The loss was incurred by the prior
administration's purchases, not by the disposal. I record the disposal as good capital
allocation and the purchase as bad, and they are separate judgments about separate people.)*

### **[E4-32] — DIRECTION OUTRANKS EXISTENCE, AND THE DIRECTION IS NEGATIVE**

*The moat widened every year is "the primary criterion of a great business."* **[E4-32]**

Every measurable series in this file points the same way over the last two years:

| series, filed | best reading | latest reading | direction |
|---|---|---|---|
| Net software retention rate | 108.8% (FY2024) | **101.5% (Q2 2026)** | ↓ |
| Bookings, continuing ops, half-year | $195.8M (H1 2025) | **$195.5M (H1 2026)** | ↓ |
| Remaining performance obligation | $150.8M (2025-06) | **$151.0M (2026-06)**, +0.1% | flat |
| Organic revenue growth | 6% (2025) | **+1% total revenue (Q2 2026)** | ↓ |
| Customers with ACV ≥ $100k | 389 (2023) | **withdrawn** | unobservable |
| Goodwill + intangibles ÷ total assets | — | **76.0%** | — |

### THE COMPETITOR ROW — required **[E3-28]**

*Full working, with 28 accession numbers, in
`Test Runs/_research 2026-09-07 CERT/COMPETITOR_ROW.md`.*

**Peers named: 2 of the 8 competitors Certara itself names — and the reason the other six are
missing is a finding, not a gap.** Certara's competition section names **Mathworks** (private),
**Dassault Systemes** (French issuer; BIOVIA/Medidata revenue is not separately reported at a
biosimulation level, **evidence rung R3/R4 — NOT OBTAINED**, and no estimate is substituted),
**Ansys** (absorbed into Synopsys), **Simulations Plus** (covered), **NONMEM, a division of
ICON** (embedded inside a contract-research organisation, not separable), and on the services
side **Metrum Research, qPharmetra and Pharmetheus** (all private). **Exactly one of the eight
files comparable segment data, and it is being taken private this year.** Schrodinger is added
because it names Certara in its own competition section under securities liability, which
makes it a two-way comparable even though Certara does not name it.

**Under the framework's rule, an unavailable peer holds the moat class PROVISIONAL. Six of
eight are unavailable, so the class is PROVISIONAL and I say so.** What follows does not rest
on the missing six.

| same metric, latest filed FY | **CERT** FY2025 | **SLP** FY2025 (Aug) | **SDGR** FY2025 |
|---|---|---|---|
| Accession | `0001827090-26-000011` | `0001023459-25-000060` | `0001490978-26-000010` |
| Revenue | **$418.8M** | $79.2M | $255.9M |
| Revenue growth, latest / prior | +8.7% / +8.7% | +13.1% / +17.5% | +23.3% / −4.2% |
| Gross margin, as filed | 61.5% *(see caveat)* | **58.4%** | 55.7% |
| **Software vs services GM split filed?** | **NO** | **YES — software 79%, services 30%** | **YES — software 74.4%** |
| GAAP operating margin | **+5.0%** | (89.3)% | (65.2)% |
| GAAP net income | **$(1.6)M** | $(64.7)M | $(103.3)M |
| Operating cash flow | **$96.3M (23.0% of revenue)** | $18.1M | $13.9M |
| SBC ÷ revenue | **7.9%** | 8.0% | 16.8% |
| Total capex incl. capitalised software | $26.6M (6.3%) | $3.3M (4.2%) | $1.4M (0.6%) |
| **Goodwill + intangibles ÷ total assets** | **78.4%** | 55.3% | **0.66%** |
| Goodwill impairment, last 5 FY | **$47.0M (2023)** | **$51.6M (2025)** | **$0, every year** |
| Total debt | **$293.1M** | **$0** | **$0** |
| Net debt / (net cash) | **+$103.7M** | $(32.4)M | $(395.5)M |
| Retention metric filed as a number? | **YES — 101.5% Q2 2026** | **NO — 0 hits in 23 filings** | **YES — NDR 100%, from 113%** |
| Customer concentration | **lowest — top 10 = 24%** | low | **one customer 17% of revenue** |

**THE ROW'S SINGLE STRONGEST FACT FOR CERTARA, AND IT IS THE OPERATOR'S PRIOR SURVIVING ITS
OWN TEST.** *"Our software products are **licensed by the FDA and other regulatory
authorities**, who may use them in assessing new drug applications."* **Neither peer makes
this statement, and Simulations Plus makes the opposite one** — *"Our pharmaceutical software
products and platforms are tools used in research and/or development and are **neither
approved nor approvable by the FDA** or other government agencies."* SLP can say the FDA funds
it and partners with it; only Certara can say the regulator is a paying licensee. **If a
reviewer runs your simulator when assessing your customer's dossier, your customer's switching
cost is not a licence fee, it is a review risk.** That is a genuine, filed, checkable moat
mechanism and it is the best thing in this file.

**THE ROW'S SINGLE STRONGEST FACT AGAINST, AND IT IS ALSO CERTARA'S OWN WORDS, TWELVE PAGES
LATER.** From the risk factors, on those same regulator licences:

> *"These licenses are **typically renewed on an annual basis**, and **there is no obligation
> for these regulatory authorities to renew** these licenses at the same or any level. **While
> these licenses account for a small amount of our annual revenue** …"*

**Annual, revocable at the regulator's option, and immaterial in revenue.** The moat mechanism
is real and the company has quantified its own hold on it as "a small amount."

**THE DISCLOSURE ASYMMETRY IS THE ROW'S MOST USEFUL FINDING, AND IT ANSWERS THE AMAT PRIOR BY
PROXY.** The operator's prior was that AMAT's run showed what happens when a segment gross
margin finally becomes available. **Certara will never file one — but its closest pure-play
peer does, and the number is brutal: software 79%, services 30%** (and 88% / 43% at SLP's
latest quarter). **Services was 56.2% of Certara's FY2025 revenue.** If Certara's services
half carries anything like SLP's economics, the blended 61.5% is concealing a great deal.

**And the 61.5% is not comparable in the first place.** Certara tags its cost line
`CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization` and carries D&A on a
separate line below it; SLP puts $6.7M of amortisation **inside** cost of revenue. **On a
full-D&A basis Certara's gross margin is 48.0%, not 61.5%.** The like-for-like number sits
between the two and the filings do not locate it.

**THE ROW'S LIMIT, STATED [E3-61].** *"In some businesses, the participants behave like a
demented Kellogg. In other businesses, they don't … I think you'd have to know the people
involved."* Two limits specific to this row. First, **six of eight named competitors are
unobtainable**, so the class stays PROVISIONAL. Second, and more important: **the whole
category is decelerating together.** Schrodinger's net dollar retention fell **113% → 100%**
in one year. SLP cut FY2025 revenue guidance from $90–93M to $76–80M **102 days after
reaffirming it**, wrote off $77.2M in the same quarter, changed auditors in the same quarter,
and has agreed to be taken private by Altaris at **$18.50 a share, ~$375M of equity, roughly
4.3x EV/revenue**. **That materially softens the reading of Certara's own deceleration as a
Certara failure — it is at least as likely to be an end-market fact**, which is precisely what
the operator's biotech-funding prior anticipated. It does not soften [E3-03] criterion (2),
which is a question about substitutes and is answered by Certara's own competition section.

- **Untapped pricing power [E3-33] / [E5-28]?** **No.** Claiming that class is claiming
  near-monopoly, and the row does not support it: eight named competitors, two of them free,
  a market the company itself calls *"competitive and **highly fragmented**"*, and a net
  retention rate of 101.5% on a metric that explicitly includes price increases. There is no
  ungathered pricing here; there is pricing being tested and coming back at 1.5%.
- Class: **NARROW on the software half, NONE on the services half, PROVISIONAL overall, and
  NARROWING over the measured window.**

- **VERDICT: [x] OUT — on [E3-03] criterion (2), evidenced by Certara's own competition
  section, and on [E4-32] direction, evidenced by Certara's own retention table.**

### **WHY THIS IS NOT A PASS, STATED AT FULL STRENGTH FOR THE OTHER SIDE FIRST [E4-51, E4-26]**

*"I'm not entitled to have an opinion unless I can state the arguments against my position
better than the people who are in opposition."* **[E4-51]** Here is the bull case as well as I
can put it, and I hold a framework that wants me to reject things, which is exactly the
incentive [E4-27] tells me to watch in myself:

> Certara is the scale player in a real and growing scientific discipline. Twenty global drug
> regulatory agencies — the FDA, the EMA, the PMDA, the CDE, the MHRA — **pay Certara for
> licences and run its software when they review drug applications.** No competitor in the
> world can say that; the nearest listed one says in its own 10-K that its products are
> *"neither approved nor approvable."* Certara serves **38 of the top 40 biopharmaceutical
> companies by R&D spend**, has 160,000 users, no customer over 10% of revenue, and datasets
> *"compiled over decades … that cannot be readily replicated."* It is **five times the size
> of the nearest pure-play**, it is **the only company in its peer row generating GAAP
> operating profit**, and it converts **23% of revenue into operating cash flow** while both
> peers convert under 23% combined. Its net retention rate has been **above 100% in every one
> of the fourteen quarters it has ever disclosed** — through the worst biotech funding
> drawdown in twenty years. Its closest comparable was just bid for at **4.3x EV/revenue** by
> a financial sponsor; **Certara trades at about 3.1x**, so the informed marginal buyer of
> this exact asset class is paying more than the market is asking here. And the new management
> has already done the right thing with the worst asset: it sold it.

**That case is real, the regulator-licensee fact is the best single sentence in this queue,
and I am not discounting it. Here is why it does not carry Q2 anyway.**

**First, [E3-03] criterion (2) is not "customers stay." It is that the product is *"thought by
its customers to have no close substitute."*** Certara's own competition section names
**Mathworks, Dassault Systemes, Ansys, Simulations Plus, NONMEM, open-source R, open-source
PK-Sim, and the customer's own in-house software.** PK-Sim is open-source PBPK modelling — the
same category as Simcyp — and it costs nothing. **A company that names a free substitute for
its flagship product, in its own 10-K, in a market it describes as "highly fragmented," has
answered criterion (2) against itself.** This is a worse position than the CRWD run found,
because there the substitute at least had to be bought.

**Second, the company's own price metric returns 1.5%.** [E2-44](1) asks whether the business
can raise prices *"even when product demand is flat and capacity is not fully utilized."*
Certara publishes a number that is defined as *"inclusive of price increases and expansion"*
and it reads **101.5% in the latest filed quarter, the lowest reading in the entire disclosed
series, down from 108.8% two years ago.** [E4-37]'s inverse metric — the agony over whether a
price increase can be sustained — is not something I have to infer here; the company publishes
the outcome quarterly and it is deteriorating.

**Third, [E4-32] settles direction, which the framework says outranks existence.** Net
retention down, bookings flat, remaining performance obligation up 0.1%, organic growth 2% and
6%, latest-quarter revenue +1% with services **−3%**, and the one physical unit series ever
filed withdrawn after its growth collapsed. **Over the only window that can be measured, this
moat narrowed.** [E4-32] says the moat *widened every year* is *"the primary criterion of a
great business"*; the opposite is filed here.

**Fourth, [E4-04] — and this is the deepest reason.** *Does the spending defend the same
advantage, or buy its replacement?* **$577M of acquisition consideration in five years, 21
companies since 2013, 76% of the balance sheet in goodwill and purchased intangibles, and
$2.2M of return per $100 of retained capital.** This is a moat that is repurchased, not
defended. And the company has published what the repurchasing returns: **$47.0M of impairment
in 2023 and a $65.5M loss on disposal in 2026 on one acquired unit — $112.5M, 9.3% of the
market capitalisation.** [E5-40] asked what the serial acquirer's returns were. That is the
answer, in the company's own filings, twice.

**What would flip this verdict, named in advance so it is falsifiable:** a filed net software
retention rate at or above 110% for four consecutive quarters; or a filed cost-of-revenue
disaggregation showing the software half at SLP-like margins **together** with software growing
organically at a double-digit rate; or evidence that the regulator licences have become
material rather than *"a small amount of our annual revenue."* Each of those is a document I
can name, so this verdict is reviewable. **But it is OUT, not UNRESEARCHED, because the
documents that exist have been read and they answer the question.**

**One honest caveat on the verdict, recorded rather than buried.** There is a real UNKNOWABLE
sitting inside this OUT: **Certara's software gross margin does not exist in any filing and
never will**, because the company reports one segment and ASC 280 does not compel the split.
I decided Q2 without it, and I can defend that — the net retention rate is a software-only
metric that Certara does file, and it is more direct evidence on criterion (2) than a margin
would be. **But I record that the missing number can only cut one way**: if Certara's services
half runs at SLP's 30%, then the software half is smaller and the blended business worse than
the headline suggests, and the verdict gets stronger rather than weaker. **A missing number
that can only hurt is not a reason to hold the file open.**

**Q2 CLOSES THE FILE. Everything below this line is recorded because the operator's brief
asked for it and because a closed file still owes the register its findings. None of it is a
verdict, and per operator rule 2 none of it can promote the name.**

---

### ⚑ **ADDENDUM TO THE COMPETITOR ROW — added the same session, on completion of the peer
### sweep. Two items arrived after the Q2 verdict was written. NEITHER CHANGES IT; the first
### strengthens it and the second softens it, and both are recorded rather than folded in.**

**ADDENDUM 1 — THE COMPETITOR LIST ITSELF IS A DATED SERIES, AND IT RUNS AGAINST THE MOAT.**
Certara's competition section did not always read as it does now:

| 10-K vintage | named software competitors | the characterisation |
|---|---|---|
| FY2021–FY2022 | Mathworks, Simulations Plus, NONMEM (ICON) — **three** | *"companies **smaller than ourselves**"* |
| FY2023 | same three | **the "smaller than ourselves" phrase is DELETED**, replaced by the barrier-to-entry assertion |
| FY2024–FY2025 | Mathworks, **Dassault Systemes**, **Ansys**, Simulations Plus, NONMEM — **five** | barrier-to-entry assertion only |

**The company stopped describing its competitors as smaller than itself in the FY2023 10-K,
and has since added two of the largest engineering-software companies in the world to the
list.** That is management's own dated account of a competitive set getting bigger and closer,
and it is the [E4-32] direction test evidenced from the disclosure language rather than the
numbers. **It strengthens the OUT.**

**ADDENDUM 2 — DASSAULT SYSTEMES, OBTAINED AT RUNG R3, AND IT CUTS THE OTHER WAY.**
The SEC rung is structurally dead — **Form 15F-12G filed 2008-10-16; the last 20-F was
FY2007** — so no filing-grade US data exists and none was invented. At rung R3 (the AMF-filed
Universal Registration Documents, the company's own published annual report):

- **Life Sciences product line revenue €1,081.1M in FY2025, down 2% at constant currency —
  the group's only declining product line**, on *"lower study starts volume of −7%."*
- The trend is **+6% → −1% → −2%** constant-currency over three years.
- **No MEDIDATA or BIOVIA revenue is disclosed at any rung**, so the head-to-head against
  Certara's biosimulation revenue **cannot be constructed. Recorded as the blocked rung; no
  estimate substituted.**
- MEDIDATA carries **€2,191.7M of goodwill, 46.5% of group goodwill, never impaired.**

**This is the third independent confirmation of the end-market reading and it is the strongest
argument against reading Certara's deceleration as a Certara failure.** Three of the four
observable participants — Certara (net retention 108.4% → 105.3% → 101.5%), Schrodinger (net
dollar retention 113% → 100%), and Dassault Life Sciences (+6% → −1% → −2% cc, on a 7% fall in
study starts) — are decelerating **simultaneously**, and the fourth (Simulations Plus) is
guiding to 0–4% growth and leaving the public market. **[E3-61] is exactly on point: the row
shows position, not conduct, and a whole category moving together is a fact about the market,
not about the management.** The operator's biotech-funding prior is **CONFIRMED**, and it is
the best reason to hold [E4-17]'s *"beliefs change quite gradually"* over this verdict. **It
does not rescue Q2**, because [E3-03] criterion (2) is answered by Certara's own naming of
free substitutes and its own 101.5% price-inclusive retention number, neither of which is an
end-market fact.

---

## TESTS RUN BELOW THE CLOSED GATE — RECORDED, NOT VERDICTS

### **(c) — THE JUDGMENT, AND THE PURCHASE-ACCOUNTING TRAP IS THE LARGEST THE QUEUE HAS SEEN**

**The operator's correction 4 is confirmed and it is extreme. D&A is 42.7x total PP&E capex,
and the filed split says why.** From the FY2025 10-K, notes 6 and 7:

| FY2025 D&A of **$75,162k**, decomposed from the filed notes | $k | share |
|---|---|---|
| Depreciation of property and equipment (note 6, verbatim: *"Depreciation and amortization expense was $2,163"*) | **2,163** | 2.9% |
| Amortisation of **capitalised software development costs** (note 7: *"Amortization expense of $18,607 … was recorded in cost of revenues"*; cross-checked to the accumulated-amortisation roll, $64,739 − $46,756 = $17,983) | **18,607** | 24.8% |
| **Amortisation of ACQUIRED intangibles** — acquired software, trade names, customer relationships, non-competes, patents | **54,392** | **72.4%** |

**Gross intangibles at 2025-12-31 were $863,280k, of which $762,084k — 88% — was purchased**
(acquired software $200,818k, customer relationships $498,341k, trade names $59,998k,
non-competes $2,748k, patents $179k) and only $101,196k internally developed.

**Which case is this? Neither of the framework's two.** The corpus default is that D&A is a
fair proxy for (c) **[E3-44, E2-41]**; the exception class is the capital-intensive filer whose
own filing shows depreciation *understates* renewal **[E5-20]**. **Certara is the mirror image
of the exception: its D&A vastly OVERSTATES renewal, because nearly three-quarters of it is
purchase accounting.** The QCOM ruling applied at AVGO governs: **acquisition amortisation
renews nothing that R&D above the OCF line does not already renew.** Certara expenses
**$41.0M of R&D inside operating cash flow** and capitalises a further **$24.8M** in investing.
That $65.8M — 15.7% of revenue — is the renewal spend, and it is already fully charged.
Subtracting another $54.4M of amortisation of customer relationships bought in 2021 would be a
double count of the same renewal.

**JUDGMENT, DISCLOSED [E2-23, E3-44]: (c) = total capex = PP&E capex + capitalised software
development = $26.6M for FY2025.** Capitalised software **must** be in it — it is cash spent on
renewing the product, it sits in investing, and its amortisation is inside the D&A line, so
taking the amortisation while omitting the cash would double-count in the company's favour
(the CRWD reasoning, and here the line is $24.8M against $1.8M of PP&E).

**And I record which direction this judgment spends conservatism, because it matters
[E4-11].** Choosing $26.6M over $75.2M is **the generous choice**. It raises owner earnings by
$48.6M a year. **Windage count: ONE, and it is spent in the company's favour.** Everything
below is therefore a floor on the bear case, not a construction of it.

### **THE THIRD (c) READING THE FRAMEWORK REQUIRES ME TO PUT ON THE PAGE**

[E2-23]'s (c) is *"capitalized expenditures for plant and equipment, **etc.** that the business
requires to fully maintain its long-term competitive position and **its unit volume**."*
**On this filer there is a serious argument that the acquisitions ARE the maintenance.**
Organic growth was **2% in 2024 and 6% in 2025**; total revenue growth in the latest quarter
was **+1%** with services at **−3%**; and the company has bought 21 businesses since 2013 to
hold position. If maintaining unit volume requires buying, then acquisition spend belongs in
(c), and the five-year average is **$86.4M a year**.

| (c) construction | 5-year mean owner earnings | yield on $1,211M |
|---|---|---|
| (c) = PP&E capex + capitalised software — **the judgment used** | **$34.4M** | **2.84%** |
| (c) = total D&A — invalid here, double-counts renewal | $(8.1)M | negative |
| (c) = capex + software + acquisitions-as-maintenance | **$(52.0)M** | negative |

**Two of the three readings are negative and the one I chose is the only positive one.**
Recorded per [E4-25]: the spread *is* the range, and it is not resolved by preference.

### **OWNER EARNINGS, BY YEAR AND OVER SIX WINDOWS — EVERY WINDOW PUBLISHED [E4-38]**

*OE = OCF − SBC − (c). All figures $M, from the filed consolidated statements of cash flows:
2019–20 from the FY2021 10-K `0001558370-22-002608`; 2021–22 from the FY2022 10-K
`0001558370-23-002605`; 2023–25 from the FY2025 10-K `0001827090-26-000011`.*

| FY | OCF | SBC | OCF−SBC | total D&A | PP&E capex | cap. software | **total capex** | **OE @ (c)=capex** | OE @ (c)=D&A |
|---|---|---|---|---|---|---|---|---|---|
| 2019 | 38.0 | 1.7 | 36.3 | 41.6 | 2.1 | 7.4 | 9.5 | **26.8** | (5.2) |
| 2020 | 44.8 | 64.5 | (19.7) | 42.8 | 0.9 | 7.1 | 7.9 | **(27.6)** | (62.5) |
| 2021 | 60.4 | 29.5 | 30.9 | 45.1 | 1.1 | 7.8 | 8.9 | **22.0** | (14.2) |
| 2022 | 92.5 | 30.3 | 62.2 | 52.5 | 1.4 | 11.1 | 12.5 | **49.7** | 9.7 |
| 2023 | 82.8 | 28.3 | 54.5 | 56.1 | 1.8 | 13.5 | 15.3 | **39.1** | (1.6) |
| 2024 | 80.5 | 34.8 | 45.7 | 68.0 | 1.6 | 19.4 | 21.0 | **24.7** | (22.3) |
| 2025 | 96.3 | 33.1 | 63.2 | 75.2 | 1.8 | 24.8 | 26.6 | **36.7** | (11.9) |

*(2020's SBC of $64.5M is the December-2020 IPO's Class B unit conversion, a one-off. It is
**left in** per [E5-33] — *"to tell owners year after year, 'Don't count this' … is
misleading"* — and its effect is visible as the single negative year at the capex end.)*

| window | **OE @ (c) = total capex** | OE @ (c) = D&A |
|---|---|---|
| 3-year 2023–25 | **33.5** | (12.0) |
| 4-year 2022–25 | **37.5** | (6.5) |
| **5-year 2021–25 — the corpus default [E2-42]** | **34.4** | **(8.1)** |
| 6-year 2020–25 | **24.1** | (17.1) |
| 7-year 2019–25 | **24.5** | (15.4) |
| 5-year 2019–23 | **22.0** | (14.8) |

**THE TRUE RANGE ACROSS SIX WINDOWS AND BOTH (c) ENDS IS −$17.1M TO +$37.5M — A SPAN OF
$54.6M. The published row's span was $7M (28 to 35).** The honest width is **7.8x the
published figure**, and it cannot be expressed as a ratio because **it crosses zero**. The
operator's caveat said true width has run 2.3x–2.8x the published figure in the last seven
runs; here it is 7.8x, and the qualitative difference is that one end is negative.

**A wide spread is itself a Q4 finding [E5-11], and the distorted year is nameable:** 2020
carries the IPO's $64.5M equity-conversion charge. But removing it does not close the range —
the 5-year window that excludes 2020 entirely still spans **−$8.1M to +$34.4M.** **The width
here is not a distorted year. It is the (c) question**, and the (c) question is whether
$54.4M a year of amortisation of things bought in 2021 is a cost of staying in business.

### **STOCK COMPENSATION, SUBTRACTED IN FULL [E5-06, E3-70]**

$33.1M in FY2025, **7.9% of revenue and 34.3% of operating cash flow.** That is materially
better than the CRWD case (68.0%) and better than Schrodinger (16.8% of revenue); it is level
with SLP (8.0%). **This is a genuine point in Certara's favour and I record it as one.**
Per [E3-70] the reported charge is the floor, not the measure; Certara's awards are RSUs and
PSUs whose grant-date fair value is the share price, so the charge is close to the market
measure here. **But $8.6M of shares were issued in H1 2026 alone to settle acquisition
contingent consideration** (1,294,179 shares), which is outside the equity-award tables and
outside the SBC line, so **$33.1M is a floor.**

### **GREAT, GOOD, OR GRUESOME? [E4-20] — AND IT TURNS ON THE RETURN ON RETENTION**

> *"The worst sort of business is one that grows rapidly, requires significant capital to
> engender the growth, and then earns little or no money."* **[E4-20]**

**The arithmetic, from filed figures, 2021 through 2025:**

| | |
|---|---|
| Capital put into the business: acquisition consideration | **$577.0M** |
| Capital put into the business: capitalised software development | **$76.6M** |
| **Total retained and deployed** | **$653.6M** |
| Owner earnings, 2021 (start of window) | $22.0M |
| Owner earnings, 2025 (end of window) | $36.7M |
| **Increment** | **$14.7M** |
| **Return on capital retained and deployed** | **2.2%** |

**[E5-40] puts "quite satisfactory" at roughly 12% on retained capital. This is 2.2%.**
And the GAAP record over the same window is **cumulative net income of $(66.6)M** across
2021–2025.

- [ ] great  [ ] good  **[x] gruesome**

**Stated fairly the other way, because [E4-43] warns against over-reading this test.** The
*good* class passes and Certara is not an airline: it produces **positive operating cash flow
every year for seven years**, positive owner earnings at the chosen (c) end in six of seven,
and **the capital consumption is discretionary — acquisitions, not mandatory plant.** A
Certara that stopped acquiring would be a **good** business: roughly $35M of owner earnings on
$66M a year of genuine product spend, growing at 2–6%. **The gruesome finding is about the
consolidated record as filed, which includes the $654M and the 2.2%.** [E4-43]'s escape clause
is *"unless the cash they consume gets to earn a reasonable return"*, and the filed answer to
that clause is 2.2%, plus $47.0M of impairment and a $65.5M loss on disposal.

### **STAYING POWER — SCORE ALL THREE [E5-11]**

**(1) A large and reliable stream of earnings — PASSES AT THE CASH-FLOW LINE, FAILS AT THE
OWNER-EARNINGS LINE.** Operating cash flow has been $38M, $45M, $60M, $93M, $83M, $80M, $96M
across seven years — genuinely reliable, and the screen row's `level_shift 1.47 no step` is
correct about it. Owner earnings behind it are $22M–$50M and have no trend. **And on
continuing operations the current half-year is negative:** H1 2026 OCF from continuing
operations $15.6M, less SBC $13.4M, less continuing-operations investing $14.5M (capex $1.3M +
capitalised software $13.2M) = **−$12.3M.** *(Stated fairly: **H1 2025 on the identical
construction was also negative, at −$4.7M** — Q4 is by far the largest bookings quarter, so
the half-year is seasonally weak and the negative sign is not new. The deterioration from
−$4.7M to −$12.3M is the fact; the negative sign is not.)*

**(2) Massive liquid assets — ADEQUATE, NOT MASSIVE.** Cash $184.1M at 2026-06-30 plus a
$100.0M undrawn revolver, against $291.8M of debt. **Net debt $107.7M**, roughly 3.1x the
five-year owner-earnings mean. Not a fortress; not a problem.

**(3) No significant near-term cash requirements — THIS PASSES, AND IT IS THE ONE THAT USUALLY
KILLS.** From the filed contractual-obligations table:

| due within 1 year | $k |
|---|---|
| Principal payments of long-term debt | 2,963 |
| Interest on long-term debt | 19,300 |
| Operating leases | 4,125 |
| **Total** | **26,388** |

**$26.4M against $96.3M of operating cash flow. The term loan's $280.7M balloon is at
2031-06-26 — more than five years out — and the revolver matures 2029-06-26.** There is no
near-term wall. **[E2-54]'s coverage test:** interest of $19.7M against operating cash flow
net of ample capital expenditure ($96.3M − $26.6M = $69.7M) is **3.5x covered.** Passes
comfortably.

**Leverage, named and quantified [E4-16, E3-29] — there is no ratio ceiling in this framework
and the corpus supplies none.** Term Loan $295.5M outstanding at Term SOFR + 2.75%, maturity
2031-06-26; $100.0M revolver undrawn, maturity 2029-06-26, margin 2.75%–3.50% *"depending on
the applicable first lien leverage ratio."* **[E3-52] runs the wrong way here:** this is
covenanted bank debt with a leverage-linked margin, not the covenant-free, due-date-free
customer float the corpus praises. And **customers do not fund this business** — total
deferred revenue is **$80.0M against $418.8M of revenue**, so the CRWD-style negative operating
asset base does not exist. **Certara's operating assets are funded by shareholders and
lenders, not by customers.**

**[E2-60] — restricted earnings, and the buyback is where it bites.** Repurchases were
**$42.6M in 2025 and roughly $61.3M in H1 2026** — $103.9M over eighteen months against
owner earnings of roughly $35M a year. **The H1 2026 buyback was funded by the disposal**:
cash went $189.4M → $184.1M while receiving $69.4M of Veristat proceeds and paying out $61.3M.
That is a distribution financed by selling a business, not out of earnings. It is not the
[E2-52] issue-to-pay-dividends pattern (there is no dividend and net issuance is negative),
but it is the [E2-60] shape and it is recorded.

### **NAME THE SPECIFIC WAY THIS BUSINESS DIES [E2-27, E3-24, E4-40]**

**Model exposure, not experience [E4-40].** The benign fact is that operating cash flow has
never fallen. The exposure is different and it is on the balance sheet and in the retention
table.

**The mechanism.** Net software retention decays through 100% while the services half — 56% of
revenue before the disposal, already **−3% in the latest quarter** — keeps shrinking against
biotech customers whose R&D budgets are cash-constrained. Organic revenue turns negative. The
company's response for a decade has been to buy revenue; but the balance sheet is now **76%
goodwill and purchased intangibles with negative tangible equity of $96.8M**, there is **$292M
of covenanted bank debt**, and the equity currency has fallen roughly 80% from its post-IPO
high, so stock is an expensive acquisition currency and cash is finite. Management therefore
either levers into a decelerating market or stops buying and shows the organic rate.

**Quantified from filed figures.** The committed annual claims on operating cash flow are
**interest $19.7M + capitalised software development $24.8M** (which cannot lapse without the
product ageing) **+ stock compensation $33.1M = $77.6M against FY2025 operating cash flow of
$96.3M.** On continuing operations annualising at roughly $375M of revenue:

| revenue decline | gross profit lost at 61.5% | as % of the $34.4M owner-earnings mean |
|---|---|---|
| −5% | $11.5M | **34%** |
| −10% | $23.1M | **67%** |
| −15% | $34.6M | **100% — owner earnings reach zero** |

**Certara does not need a catastrophe. It needs the last two filed quarters to continue.** At
Q2 2026's trajectory — total revenue +1%, services −3%, net retention 101.5% and falling —
owner earnings at the generous (c) end reach zero inside three years without any new adverse
event. And the same arithmetic at the D&A end of the band is already there.

**Likelihood: [ ] likely  [x] a real possibility  [ ] a low-level possibility.**
Not *likely*: bookings are flat rather than falling, the term loan is five years out, coverage
is 3.5x, and the disposal proceeds are real cash. Not *a low-level possibility*: the
deterioration is in two filed quarters, the peer set is decelerating in the same direction
(Schrodinger's net dollar retention 113% → 100%; Simulations Plus guiding to 0–4% growth), and
the company has already destroyed $112.5M on one acquired unit inside this window.

---

## Q3 ITEMS — NO VERDICT IS WRITTEN, THE GATE IS CLOSED. **[E4-22, E4-29, E2-49, E5-08]**

**WEIGHT CASE, DECLARED AS THE TEMPLATE REQUIRES.**
- [ ] Daily execution **[E3-38]** — **not ticked.** Certara sells annual software licences and
  project-based consulting. A bad quarter is a bad quarter; it is not the [E2-70] *"their only
  products are promises"* shape.
- [ ] Control **[E1-16]** — not ticked.
- [ ] Leverage **[E3-29]** — **not ticked, and it is the closest call.** $292M of covenanted
  bank debt against negative tangible equity of $96.8M means an asset error does destroy
  equity, and one just did. But interest coverage is 3.5x, the maturity is 2031, and 20:1 this
  is not.

**None ticked → Q3 is a qualitative OVERLAY, not a gate.** Recorded findings follow; none of
them stops or starts the run, and per the guardrail none can promote the name.

**[E4-29] — THE FIFTH FLAG FIRES, AND IT FIRES IN THE PAY PLAN.** *"Trumpeting EBITDA … is a
particularly pernicious practice … That's nonsense."* EBITDA appears **9 to 11 times in every
one of the five 10-K vintages read**, and the FY2025 10-K carries a full Adjusted EBITDA and
Adjusted-EPS reconciliation. **Adjusted EBITDA is 50% of the annual bonus** (revenue 40%, KPIs
10%), and the proxy's own definition is the reason this matters:

> *"Adjusted EBITDA is defined as net income (loss), excluding interest expense, provision
> (benefit) for income taxes, depreciation and amortization expense, **amortization of
> intangible assets, equity-based compensation expense, goodwill impairment expense,
> acquisition and integration costs**, and other items not indicative of ongoing operating
> performance."* — 2026 proxy `0001104659-26-039372`

**A serial acquirer paying half its bonus on a measure that excludes stock compensation, the
amortisation of what it bought, the impairment of what it bought, and the cost of buying it.**
Under **[E4-52]** this is not three prompts but one reinforcing system: the metric that decides
the pay is the metric constructed to be blind to the acquisition programme's costs.

**THE OUTTURN, AND IT CUTS BOTH WAYS [E3-48].** The 2026 proxy discloses the 2025 targets as
numbers, in advance, which is the candid form:

| 2025 metric | threshold | target | maximum | **actual** |
|---|---|---|---|---|
| Revenue | $386.8M | **$429.8M** | $541.6M | **$418.8M — MISSED target** |
| Adjusted EBITDA (AIB) | $134.4M | **$149.3M** | $188.1M | **$152.2M — BEAT target** |

**The revenue target was set 11.6% above the prior year's actual and was missed. The Adjusted
EBITDA target was beaten.** The target-below-actual test that hit at CRWD does **not** hit
here: the revenue threshold of $386.8M was $1.7M *above* 2024's actual $385.1M, and the target
well above it. **That is a real point in management's favour and I record it as one.** The
criticism is not that the bar was low; it is that **the metric that beat is the one that
deletes the acquisition costs**, and it carries the larger weight.

**[E2-49] METRIC-SWITCHING — DOES NOT FIRE ON BALANCE, AND I RECORD WHY I DECLINED IT.** The
ACV ≥ $100k customer count disappeared after the FY2023 10-K, in the vintage its growth fell
from 24% to 5.1% — the classic dating. **But the same vintage that dropped it introduced the
bookings and net-retention tables**, which are quantified, quarterly, and carry three years of
history. On [E2-49]'s own standard — *"pre-set, long-lived and small bullseyes"* — **Certara's
disclosure got better, not worse.** This is the opposite of the CRWD finding and it deserves
to be said plainly. What is now deteriorating is the replacement metric, in public, where an
outsider can see it.

**[E4-30] FILED-FIGURE TELLS — DO NOT FIRE, AND ONE RUNS THE OTHER WAY.** Cash taxes paid were
$19.3M (2023), $14.7M (2024), $12.2M (2025) against pretax income of $(55.1)M, $(17.2)M and
$7.6M. **Cash taxes vastly EXCEED reported pretax income** — the inverse of the tell, and
consistent with real foreign profits being taxed while non-deductible purchase amortisation
suppresses the GAAP line. Reported growth is not unnaturally smooth; it is visibly lumpy.

**[E2-01] THE PRIMARY TEST — AND THE DENOMINATOR REFUSES TO WORK.** *"a high earnings rate on
equity capital employed."* Net income was $(8.9)M, $(49.4)M, $(13.3)M, $14.7M, $(55.4)M,
$(12.1)M, $(1.6)M across 2019–2025 — **negative in six of seven years, cumulative $(126.0)M**
— against equity of roughly $1.06bn. **The return on equity capital employed is approximately
zero, and negative on most cuts.** And [E2-43]'s scoping does not rescue it: **unleveraged net
tangible assets are NEGATIVE $96.8M** at 2026-06-30 (equity $966.5M less goodwill $718.1M less
intangibles $345.2M). Dividing a loss by a negative denominator returns a spurious positive.
**This run names that and refuses to print it**, as the CRWD run did.

**[E5-08] BUYBACKS — THE TWO CONDITIONS, AND THE RECORD IS GENUINELY MIXED.**
- **(1) ample funds for operations and liquidity? Yes.** $184.1M cash, $100M undrawn revolver,
  3.5x interest coverage, no maturity before 2029.
- **(2) at a material discount to conservatively calculated intrinsic value?** The record:

| | shares | cost | **average price** | vs the $7.94 quote |
|---|---|---|---|---|
| FY2025 (authorised 2025-04-11, $100M) | 3,368,374 | $42.6M | **$12.65** | **−37%** |
| H1 2026 (treasury roll, incl. tax withholding) | 9,594,850 | $61.3M | **$6.39** | **+24%** |
| Q2 2026 alone | 3,194,975 | $17.6M | **$5.50** | **+44%** |

**They bought $42.6M at $12.65 in 2025 and the stock is now $7.94; they bought $17.6M at $5.50
in Q2 2026 and the stock is now $7.94.** [E5-24] — *"what is smart at one price is dumb at
another"* — is illustrated in eighteen months by the same board. **The 2026 buying was
well-timed and is a point in the new management's favour; the 2025 buying was not.** Recorded
with the humility clause **[E4-13]**: this rests on my own value range and management knows
the business better than I do. **The flag binds position size, never the discount rate.**

**OWNERSHIP, AND THE OPERATOR'S SPONSOR-EXIT PRIOR — REFUTED.** *The prior was to check
whether the private-equity sponsor has exited.* **It has not; it rotated.** From the 2026
proxy: *"On November 3, 2022, **EQT Avatar Parent, L.P. ("EQT") entered into an agreement to
sell its shares of the Company's common stock to Arsenal Saturn Holdings LP, an affiliate of
Arsenal Capital Partners**."* As of 2026-03-20, **Arsenal Capital Partners holds 36,345,835
shares, 23.71%**, with the contractual right *"to nominate up to two directors to our Board
of Directors, with one such director appointed to the NCGC and one to the Compensation
Committee."* **Nearly a quarter of the register is a financial sponsor with board nomination
rights and a stockholders agreement.** Against that, **all executive officers and directors as
a group (17 persons) hold 1,651,429 shares — 1.08%**, and the new CEO **Jon Resnick held zero
shares** at 2026-03-20.

**THE HONESTY BINARY [E5-16] — NO DISQUALIFIER FOUND, AND THAT IS ALL IT IS.** No SEC or DOJ
inquiry, no restatement, no material weakness, no auditor change (unlike the peer, which
changed accountants in the quarter of its write-off), no related-party transaction of note
beyond the Arsenal stockholders agreement, and the 2026 proxy discloses its compensation
targets as numbers in advance. **Per [E5-17], a Q3 pass is the absence of found disqualifiers,
not a finding that the managers are honest — "sincerity and empathy can easily be faked."**
And the guardrail binds: **nothing in this Q3 is used to promote the name, and a strong Q3
cannot repair the Q2 verdict [E2-37, E2-38, E3-39].**

**[E3-40] LOSS OF FOCUS — THE ONE FINDING THAT WOULD HAVE MATTERED, AND IT IS HISTORICAL.**
*"the management of a great company gets sidetracked and neglects its wonderful base business
while purchasing other businesses that are so-so or worse."* **That is a fair description of
2021–2024**: $577M spent, a medical-writing services business bought and then written off and
sold at a combined $112.5M loss, while organic growth in the base ran at 2%. **It is also a
fair description of what the new management is undoing.** [E4-24]'s doctrine is that a loss of
focus is an exit trigger rather than an engagement plan — but here the incumbent has already
executed the exit itself, in four months, at a real price. **Recorded as a completed
correction, not a live flag.**

---

## Q5 — **COMPUTATION — NOT A CLEARANCE**

⛔ **Q1–Q4 do not each show IN. Q2 is OUT. Under operator rule 2 this question does not open,
and under operator rule 3 what follows carries no entry language and is not a verdict.**

**THE FLOOR, FIRST [E4-28, E3-13].** *"that's the figure we quit on."*

| | |
|---|---|
| Owner earnings, 5-year mean, corpus default window [E2-42], generous (c) end | **$34.4M** |
| Market capitalisation ($7.94 × 152,538,780, 2026-09-04) | **$1,211M** |
| **Yield** | **2.84%** |
| Sovereign, USD 30-year, US Treasury, 2026-09-04 | **5.24%** |
| **Points over sovereign** | **−2.40 pts** |
| **The floor [E4-28]** | **~10%** |
| **Distance below the floor** | **−7.16 pts** |

**Honest pre-tax expectancy at this price: 2.84%. The floor is roughly 10%. The name is not
ranked — it is quit on**, and per the template the ranking lines are not filled in.

**WHAT THE PRICE ALREADY ASSUMES.** To reach the 10% floor from a 2.84% starting yield
requires **7.16% perpetual growth** in owner earnings. What the business has actually done:
**organic revenue +2% (2024), +6% (2025), total revenue +1% in the latest filed quarter with
services at −3%**, and owner earnings that went from $22.0M (2021) to $36.7M (2025) on $654M
of deployed capital. **[E4-35]'s base rate governs the assumption**: fewer than 10 of the 200
most profitable companies were wagered to attain 15% EPS growth over twenty years, and a
7.16% *perpetual* rate carries the burden of proof in writing against a business decelerating
in public.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — no risk premium is added to the rate
**[E3-42]**; certainty is priced once, at the end.

| discount | no growth | 3% perpetual growth |
|---|---|---|
| At the **10% floor [E4-28]** | $344M · **$2.25/share** | $491M · **$3.20/share** |
| At the **bare sovereign 5.24%** | $656M · **$4.30/share** | $1,536M · $10.05/share |

- **conservative ≈ $2 a share · optimistic ≈ $4–5 a share · current price $7.94**
- *(The $10.05 cell is shown because [E4-38] requires every window to be published, and it is
  the only construction in which the quote is defensible. It requires discounting at the bare
  bond with **no floor at all**, which is precisely the pre-Test-D error the framework
  rewrote on 2026-08-28, plus 3% perpetual growth from a business currently growing at 1%.)*

**WHICH BAR — [x] Screamer test [E4-01].** Does the price already clear the conservative case?
**No. The price is above the whole range at the framework's floor.** Three outcomes; this is
the third: **above the whole range → no.** No margin is subtracted on top; none is needed.

**WINDAGE COUNT: ONE, and it was spent in the company's favour** — the (c) judgment took
$26.6M rather than $75.2M, which raised owner earnings by $48.6M a year. **Conservatism was
not stacked; the generous end still fails by 7.16 points.**

---

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**No position is taken, so there is nothing to sell. The pre-commitments are written anyway,
per [E1-02] — "I believe in establishing yardsticks prior to the act" — so that a future
re-open is judged against yardsticks set before it.**

- **Thesis-confirming metric (confirming the OUT):** net software retention rate, quarterly,
  from the 10-Q MD&A table. Below 100% confirms the Q2 verdict outright.
- **THESIS-BREAKING METRIC AND ITS THRESHOLD:** **net software retention at or above 110% for
  four consecutive quarters**, filed. That is 8.5 points above the latest reading and would
  falsify the [E3-03](2) finding directly, because the metric is defined as *"inclusive of
  price increases and expansion."*
- **Second breaker:** a filed cost-of-revenue disaggregation showing software gross margin at
  SLP-like levels **together** with double-digit organic software growth. The first alone is
  not enough; the pair would be.
- **Third breaker:** organic revenue growth returning to double digits **without** an
  acquisition — which the FY2026 10-K will test directly, since 2025 acquisition spend was
  zero and 2026 spend is zero to date.
- **Next catalyst date:** Q3 2026 10-Q, expected early November 2026, carrying the third
  quarterly net-retention print on the post-disposal perimeter.

**The monitoring question [E3-30, E4-17]:** *is this erosion an aberrational cycle, or has the
business slipped in a way that permanently reduces intrinsic value?* **Honestly: I do not
know, and the competitor row is the reason.** Schrodinger's net dollar retention fell 113% →
100% and Simulations Plus is guiding to 0–4% growth and leaving the public market. **The whole
category is decelerating together, which is the signature of an end-market cycle rather than a
franchise failure.** [E4-17] says beliefs about moats *"change quite gradually"*, and this one
should. **The Q2 verdict is OUT on the evidence filed today; it is not a prediction that
biosimulation is a bad industry.**

**Position size: ZERO.** No position is taken and none is contemplated at this price.

- **VERDICT: [x] OUT (about the business, at Q2) — Q6 recorded for the register.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, file closed. Q3–Q6
      recorded below the gate and explicitly marked as non-verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only
      IN and it rests on filed statements. The PROVISIONAL label attaches to the Q2 moat
      *class*, and Q2 is OUT, not IN.
- [x] Every UNRESEARCHED verdict names the artifact — none is written; the one candidate
      (Certara's software gross margin) is closed as UNKNOWABLE with the reason stated.
- [x] Every UNKNOWABLE states what cannot be known: **the software-only gross margin.** The
      separating test was asked aloud — *can I name the document?* — and the answer is no:
      Certara reports one segment, ASC 280 does not compel the split, and no 10-K, 10-Q or
      proxy filed 2021–2026 contains it. **Recorded as non-decisive because it can only cut
      one way.**
- [x] Step 0: the filing was read, with accession numbers; **two** figures cross-checked to
      the dollar against the filed statements (OCF $96,325k; D&A $75,162k).
- [x] Owner earnings on a multi-year mean; **six windows published**; capex band disclosed as
      a judgment with the filed decomposition behind it, and the third (acquisitions-as-
      maintenance) reading put on the page rather than suppressed.
- [x] Competitor row filled — **2 of the 8 competitors Certara names**, with the other six
      named and their evidence rungs recorded. **Moat class held PROVISIONAL** in consequence.
- [x] Sovereign is USD, the earnings currency, from the US Treasury (issuing authority), dated
      2026-09-04.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (screamer test), not both; **windage count 1, direction disclosed.**
- [x] Prices dated; the $7.94 quote is an aggregator figure, flagged, live quote only.
- [x] Run committed to git.

**ONE ERROR MADE AND CORRECTED INSIDE THE RUN, RECORDED PER PRIME RULE 2.** I first concluded
from a phrase-level regex sweep that Certara names net retention and bookings as key
performance indicators and never quantifies either. **That was wrong** — both are filed as
full quarterly tables, and my sweep missed them because the numbers sit in a table separated
from the defining sentence. **The correction reversed the sign of a Q3 flag** (it turned a
metric-withdrawal finding into a metric-improvement finding) **and supplied the single most
decisive number in the Q2 verdict** (101.5%). Recorded here rather than silently fixed,
because the absence-claim rule exists for exactly this failure mode: a "no instance found"
claim is only as good as the sweep behind it.

---
## REGISTER
- **Verdict: [x] OUT (about the business).**
- **One line:** Certara is a real business with a genuine and unusual moat mechanism — twenty
  drug regulators are paying licensees of its software — attached to a company that has spent
  $577M buying 21 businesses to grow 2–6% organically, carries 76% of its assets in goodwill
  and purchased intangibles, has already destroyed $112.5M on one of those purchases, and
  whose own quarterly retention metric has fallen to 101.5%; at $7.94 it yields **2.84%
  against a 5.24% sovereign and a 10% floor**, and it fails at Q2 before price is reached.
- **Not UNRESEARCHED:** the documents that would resolve Q2 have been read and they answer it.
- **The UNKNOWABLE recorded inside the file:** Certara's software-only gross margin does not
  exist in any filing and cannot be made to exist; it is non-decisive because both peers who
  do disclose it show services at 30–43%, which can only make the answer worse.

