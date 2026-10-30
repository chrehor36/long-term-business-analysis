# Company Run — Aehr Test Systems (AEHR) — 2026-09-18
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

Run unattended from scratch on 2026-09-18 (evening, EDT); the template was copied and committed before any fetch
(`3e3f352`). **This is a NEW NAME, not a holding, so v4 governs and not `THE HOLDINGS FRAMEWORK.md`.** WAVE 5, the
seventh and last of the "perimeter or restatement above threshold" names. Research, scripts and downloaded filings are in
`Test Runs/_research 2026-09-18 AEHR/`; the brief is `_BRIEF.md` there. Sections were written as they closed and committed
after each gate. No prior run file for AEHR exists.

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

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0: THE SKIP REASON, THE ENTITY, THE RATE, THE PRICE, THE COUNT, THE DEAL, THE PERIMETER, AND THE FILING

### The entity, in every year used
CIK 0001040470, `submissions.json` (fetched by this run): *"AEHR TEST SYSTEMS"*, SIC *"Instruments For Meas & Testing
of  Electricity & Elec Signals"*, no former names. One California corporation since 1977 (*"incorporated in California in
May 1977"*, FY2026 10-K Note 1); no reverse recapitalization, no shell, no conversion (the DJT check was run and does not
apply). `submissions.json` gives `fiscalYearEnd` **1231**, which is wrong: every 10-K in the index reports a May period
end (FY2026 ended 2026-05-29, FY2025 2025-05-30, FY2024 2024-05-31). **And the fiscal year is changing:** FY2026 10-K Note
1, *"On April 2, 2026, the Company's board of directors approved a change in the Company's fiscal year-end from the 52- or
53-week period ending on the Friday nearest May 31 to the 52- or 53-week period ending on the Friday nearest June 30. The
change will be effective beginning in fiscal year 2027, which begins on June 27, 2026 and ends on June 25, 2027."* The
four weeks from 2026-05-30 to 2026-06-26 are a transition period no filing yet covers. Every year used below is a May
fiscal year, FY2017-26.

### The skip reason, tested on the filing rather than inherited
Wave 5 row: *"perimeter or restatement above threshold: read the filing first"*; the skipped-reason list: *"revenue step
or cross-accession restatement above threshold."* **A prompt to read, never a verdict.** Reproduced by the brief-writer
against `Screens/floor_screen.py` at `a8bc84f` (`floor_screen_a8bc84f.py`) over companyfacts cut to facts filed by
2026-09-01 (`triage_repro.py`, `triage_repro_out.txt`, re-read by this run):

| guard, in order | value | fires? | what it was reacting to, on the filings |
|---|---|---|---|
| 1. `share_count_shift` | 1.098 | no | ordinary issuance: the Incal stock (552,355 shares, July 2024), ATM sales and employee plans; no split (`split_factor_after` 1.0). A dei element exists (the RIVN None check was run); single class. |
| **2. `scale_shift`** | **3.062** | **YES: THE GUARD THAT RETURNED AEHR UNPRICED** | **A REAL ORGANIC REVENUE STEP, ONE CUSTOMER'S CAPACITY BUILD. Not a perimeter and not a restatement.** FY2021 $16.6M to FY2022 $50.8M under `RevenueFromContractWithCustomerExcludingAssessedTax`, **consecutive fiscal years, same element on both sides** (the TSLA check was run: that element carries every year FY2017-26; `Revenues` carries the same totals). The FY2022 10-K MD&A (`0001654954-22-011877`): *"Net sales increased to $50.8 million for the fiscal year ended May 31, 2022 from $16.6 million for the fiscal year ended May 31, 2021, an increase of 206.2%. ... Net sales of our wafer-level products for fiscal 2022 were $48.9 million, and increased approximately $33.9 million from fiscal 2021 due to stronger demand related to silicon carbide applications."* Risk factors, same 10-K: *"During fiscal 2022, ON Semiconductor accounted for approximately 82% of the Company's net sales."* **No acquisition in FY2021-22** (no business-combination payment on either cash-flow face); the one acquisition in the window is Incal, FY2025 (below). The later steps (1.278, 1.019, 0.891, 0.848) are the same customer class peaking and falling away. |
| 3. `filed_years` | 17 | no | |
| 4. `owner_earnings` | 5y -$4.84M D&A end / -$5.44M capex end | (not reached) | OCF less SBC less (c); reproduced from the filed faces at Q4 |
| (`restatement_shift`, not a guard in that pipeline) | (1.0, FY2018) | n/a | a null, as at SMCI, SNOW, TSLA, RIVN, DJT and BX |

**No restatement exists**: no 10-K/A, 10-Q/A or NT filing in the 1,005-row filing index (`filings_list.txt`, which runs from
2018-08-20; EDGAR full-text search finds the company's only 10-K/As for FY2005 and FY2008, outside every window); the FY2026
10-K cover leaves the error-correction box unticked (*"reflect the correction of an error to previously issued financial
statements. ☐ Yes ☒ No"*). One presentation change was found and is carried rather than smoothed: FY2022 D&A is
*"Depreciation and amortization | 307"* on the FY2022 10-K face and **356** on the FY2024 10-K face
(*"Depreciation and amortization | 657 | 450 | 356"*, FY2024/23/22), a reclassification of $49K; immaterial, and the later
face is used.

**So the label was, for AEHR: a real organic revenue step, the start of one customer's silicon-carbide capacity purchases
(onsemi, 82% of FY2022 sales), on consecutive years and one element.** The same class as SNOW's, RIVN's and DJT's
step, except that this one was **made by a single buyer**, and the buyer's share is the Q2 fact.

### The sovereign: for the currency the business EARNS in **[E4-15, E3-32]**
- **5.34%** · **09/18/2026** · **US Treasury daily par yield curve, 30 Yr, the issuing authority**, fetched directly by
  this run at 20:41 EDT (`treasury_out.txt`: *"09/18/2026,3.97,3.98,4.10,4.14,4.24,4.24,4.44,4.76,4.83,4.86,4.93,5.01,5.38,5.34"*).
  `tools/sources.sovereign("USD")` returned the cached **09/17/2026 5.29%** row half a second later (`step0_out.txt`): the
  stale-cache defect, reproduced a sixth time. The issuing-authority figure is used. FRED not used. Not inherited from BX
  (the figure agrees because it is the same day's print).
- **Earnings currency: USD.** The company reports in dollars; 59% of FY2026 sales were *"attributable to sales to
  customers for delivery outside of the United States"* (FY2026 10-K Item 1A), invoiced as reported in dollars. No FX or
  ADR conversion applies.

### The price: struck by this run, aggregator flagged (operator rule 5)
- **US$93.49, the close of 2026-09-18** (Friday). Source: Yahoo Finance chart via `sources._chart("AEHR", rng="1mo",
  max_age_h=0)` (aggregator, permitted for live quotes only, **flagged**; `step0_out.txt`): `regularMarketPrice` 93.49,
  `regularMarketTime` 1789761601 = 20:00:01 UTC = **16:00:01 EDT**, so the figure is the closing print. The day's bar had
  not finalised (open 92.02, high 93.90, low 87.15, close None; the BX run recorded the same None). `tools/sources.price()`
  returned the same 93.49 stamped 2026-09-18.
- **The quote moves violently, and the run records it rather than choosing a day:** 08-19 $107.96 · 08-28 $80.81 · 09-01
  $76.59 · 09-11 $94.69 · 09-14 $83.37 · 09-17 $90.55 · 09-18 $93.49. Insider Form 4 open-market sales in August were at **$100.70 to
  $143.77** (`form4_table.txt`); the FY2026 10-K: *"during the two-year period ended May 29, 2026, the price of our common stock has
  ranged from $6.27 to $112.00."* The screen's 2026-09-01 cap ($2,520M) was struck at about $77.
- **Primary-filing cross-check:** Form 4 `0001040470-26-000265` (Didier Wimmers, filed 2026-09-03) reports shares
  withheld for tax on **2026-09-03 at $76.27**, which is the Yahoo close for 2026-09-03 to the cent (76.27); Form 4
  `0001040470-26-000263` (Chris Siu, CFO) reports withholding on **2026-09-01 at $76.59**, the Yahoo close for 2026-09-01.
  **The aggregator's series is corroborated on two dates; no Form 4 exists for 2026-09-18.**
- **Split factor after the count's date (2026-07-20): 1.0.** `close` used, never `adjclose`.

### The share count: from the cover, with the accession
- **32,620,450 shares of common stock**, from the cover of the **FY2026 Form 10-K** (fiscal year ended 2026-05-29, filed
  **2026-07-27**, accession **`0001654954-26-006919`**): *"The number of shares of registrant's common stock, par value
  $0.01 per share, outstanding at July 20, 2026 was 32,620,450 ."* `Screens/cover_shares.py AEHR` returns the same figure
  and accession (*"(single class / undimensioned) 32,620,450"*). **This is the latest periodic filing**: no 10-Q has
  followed (the first FY2027 quarter ends in late September 2026 under the new June year).
- **Sold after the cover date:** nothing found. The April 2026 ATM was *"fully utilized"* (8-K `0001654954-26-003746`,
  2026-04-20); an automatic shelf **S-3ASR** was filed the same day as the 10-K (`0001654954-26-006922`, 2026-07-27) and **no
  prospectus supplement (424B) has been filed under it** in the index to 2026-09-10. Post-cover Form 4s are RSU vesting,
  tax withholding and open-market sales by insiders (existing shares).
- **Dilution not in the count:** 316,000 options (weighted exercise price $5.11) and 707,000 unvested RSUs and PRSUs at
  2026-05-29 (FY2026 10-K equity note), 3.1% of the cover count; 2,997,000 shares remain available under the 2023 plan. Shown
  beside the cap, not in it (the cover is the rule).

### The market cap
**$93.49 x 32,620,450 = US$3,049.7M ($3.05bn).** With the options and unvested awards: $3,145M. Split factor 1.0. Public
float on the cover: *"$ 671,378,691"* at *"the closing price of $22.97 on November 28, 2025"*; the price has quadrupled
since the float date.

### THE DEAL CHECK: none live
`sources.deal_filings("0001040470")` returned no deal forms since the annual report of 2026-07-27, and `deal_note` returned
empty (`step0_out.txt`). Read on the index: **no 425, S-4, SC TO, SC 13E-3, DEFM14A, PREM14A or SC 13D filed on this
registrant.** The 8-Ks carrying Item 1.01 in the last three years are the ATM sales agreements (2023-02-08, 2026-04-08) and
the Incal purchase (2024-07-16, with Item 3.02 for the stock consideration); Item 2.01 appears on 2024-08-01 (Incal
closing) and on 2022-07-19, where the document itself reads *"Item 2.02. Results of Operations and Financial Condition"*: an earnings release indexed as 2.01, the mistagging class the RESUME STATE records for PAY.
**The quote is not a spread and buys this company.**

### The perimeter: one acquisition inside the window, and the cash
- **Incal Technology, Inc., closed 2024-07-31** (FY2025 10-K Note 4, `0001654954-25-008553`): *"The acquisition date fair
  value of the consideration transferred for Incal was approximately $ 22.2 million"*: cash $10,631K, *"Common stock under
  transfer restriction"* $9,381K (552,355 shares), escrow $2,381K, working capital $(240)K. Assets: intangibles $12,000K
  (developed technology $9,130K over 12 years), goodwill $10,719K, inventory $2,558K. **What it added:** *"$ 18.6 million in
  revenue and $ 3.8 million in net income contributed by Incal from the date of acquisition through May 30, 2025"* (FY2026
  10-K Note 4); the package-level line it became was **$19.8M in FY2025 and $18.5M in FY2026, 34% and 37% of revenue**.
  Cash paid: $11,075K in FY2025 and $1,801K in FY2026 (*"a $1.8 million escrow release"*, FY2026 MD&A), the brief's
  `acquisition_flag` $12.9M. What it added to D&A: intangible amortization of about $1.2M a year (intangibles $10,781K to
  $9,552K in FY2026), inside the D&A line from FY2025. **Q4 carries it.**
- **The cash is new, and it was raised, not earned.** Cash $116,358K at 2026-05-29 against $24,529K a year earlier;
  *"net proceeds of $97.4 million from the issuance of common stock under the Company's ATM offering program"* (FY2026
  MD&A). The equity note: 384,380 shares at an average $25.89 (November 2025), 269,439 at $39.20 (February 2026), 476,649
  at $40.88 (March 2026), and 812,185 at $73.87 (April 2026): **1,942,653 shares for about $100.0M gross, an average of
  $51.48**. No debt: the Silicon Valley Bank facility was terminated on 2024-01-04 with nothing drawn (8-K
  `0001654954-24-000428`: *"There are no financial covenants in the Loan Agreement. No amounts were outstanding"*).

### The filing was read: not tagged data **[E3-27, E4-14]**
- [x] MD&A  [x] cash-flow statement **including its detail lines**  [x] footnotes
- **FY2026 Form 10-K**, fiscal year ended 2026-05-29, filed **2026-07-27**, accession **`0001654954-26-006919`**
  (`10K_FY2026.txt`).
- Also read: FY2019-25 10-Ks (`0001654954-19-010095`, `-20-009618`, `-21-009505`, `-22-011877`, `-23-011271`,
  `-24-009642`, `-25-008553`) for the FY2017-25 statements and customer notes; the Q3 FY2026 10-Q (`0001654954-26-003348`);
  the DEF 14A of 2026-09-09 (`0001654954-26-008222`); the 2023, 2024 and 2026 ATM prospectus supplements; the 8-K earnings
  releases (EX-99.1) of July 2022 to July 2026; the Incal and ATM 8-Ks; 156 Form 4 transactions filed since 2025-06-01
  (`form4_table.txt`).
- **Figures cross-checked against the filed statement** (FY2026 10-K consolidated statement of cash flows, $K, FY2026 /
  2025 / 2024): *"Net cash provided by (used in) operating activities | (3,310) | (7,400) | 1,756"*, *"Stock-based
  compensation expense | 6,761 | 5,162 | 2,518"*, *"Purchases of property and equipment | (2,066) | (4,992) | (749)"* and
  *"Payments for business acquisition, net of cash and cash equivalents acquired | (1,801) | (11,075) | -"* match
  companyfacts to the thousand; revenue *"$50,001 | $58,968 | $66,218"* matches. The FY2017-23 faces (FY2019, FY2020,
  FY2021, FY2022 and FY2024 10-Ks) match the tagged OCF series in the brief to the thousand.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively simple and stable in
> character. If a business is complex or subject to constant change, we're not smart enough to predict future cash
> flows."* **[E3-31]**

### What the filings show, in my own words, without management's language
Chipmakers want to find the chips that will fail early before those chips go into a car or a server. One way is to run
every chip hot and at high voltage for hours ("burn-in") and throw out the ones that fail. Aehr builds the ovens and
electronics that do this, and sells them to a handful of chipmakers and test houses. It makes money three ways, all on
the face of the revenue note ($K, FY2026 10-K `0001654954-26-006919` and FY2022-24 10-Ks):

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|---:|---:|---:|
| Systems | 7,250 | 25,224 | 38,844 | 24,169 | 21,978 | 28,669 |
| Contactors (the per-device consumable) | 5,837 | 22,647 | 21,873 | 37,560 | 30,848 | 14,887 |
| Services | 3,513 | 2,958 | 4,244 | 4,489 | 6,142 | 6,445 |
| **Revenue** | **16,600** | **50,829** | **64,961** | **66,218** | **58,968** | **50,001** |
| Gross margin | 36.3% | 46.6% | 50.4% | 49.1% | 40.6% | 35.3% |
| Five largest customers | 84% | 98% | 97% | 93% | 77% | 70% |
| Largest customer | 24% | 82% (*"ON Semiconductor"*) | 79% | 67% | 39% | 26% |
| *"EV and power semiconductor revenues"* | 23% | 82% | 85% | 92% | 41% | 17% |

1. **A system** (a FOX wafer-level machine that holds up to 18 wafers, or since the Incal purchase a Sonoma, Tahoe or
   Echo package-level machine). Capital equipment, bought when a customer adds capacity.
2. **Contactors**, the consumable: *"The WaferPak Contactors are custom designed for each device type, each of which has
   a typical lifetime of two to seven years, depending on the device life cycle. Therefore, multiple sets of WaferPak
   Contactors could be purchased over the life of a FOX system"* (FY2026 10-K Item 1; the same for DiePak Carriers). Every
   new chip design on an installed system needs a new set.
3. **Service** on the installed base.

The costs are parts bought from subcontractors (*"The Company assembles its products from components and parts
manufactured by others"*), assembly in one Fremont plant, and engineers. Nothing is capital-intensive; plant, property and
equipment is $8.9M.

**The scarce input the business controls:** the full-wafer, single-touchdown contactor and the machine built around it,
qualified inside a customer's production flow. The 10-K claims *"A single FOX-XP system with a set of WaferPak
Contactors can test up to 18 wafers at a time in the same footprint as a single-wafer wafer prober and test system
offered by Aehr's competitors,"* and holds *"125 active patents"*; but it also says *"The Company relies primarily on the
technical and creative ability of its personnel, its proprietary software, and trade secrets and copyright protection,
rather than on patents, to maintain its competitive position."* Once a customer has qualified a device on the platform,
the contactor for that device is sold only by Aehr. **What the company does not control is whether the customer keeps
adding capacity**: the table shows one buyer taking 82% of FY2022 revenue and the category that buyer bought for going
from 92% to 17% of revenue in two years.

**Will the fundamentals look broadly the same in ten years?** The mechanism (sell capacity, then consumables per device,
then service) has been the same in every 10-K on disk, FY2019-26. **The customers and the end market have not been.** In
FY2021, per the FY2022 10-K, *"Advanced Semiconductor Engineering, Inc., ON Semiconductor, Intel and Inphi accounted for
approximately 24%, 23%, 20% and 10%"*;
FY2022-24 was one silicon-carbide buyer; FY2026 is three customers at 26%, 14% and 11% in *"AI processors, silicon
photonics, and power semiconductors"* (July 2026 release), none named in the 10-K. The product line itself was half-bought
in FY2025 (package-level, 37% of FY2026 revenue, from Incal).

### THE CASE FOR UNKNOWABLE, AT FULL STRENGTH **[E4-26, E4-51]**
(1) In five years the business has been a test-lab supplier, a one-customer silicon-carbide supplier and an AI and photonics
supplier; that is *"subject to constant change"* in [E3-31]'s own words. (2) The price ($3.05bn, 61 times FY2026 revenue,
Step 0) is paying for revenue the filings do not yet show: FY2027 guidance of *"$130 million and $150 million"*, a
*"benchmark"* with *"a major supplier of AI accelerators"* whose *"potential revenue opportunity"* is unquantified, a
*"lead hyperscale customer"* whose *"second device"* is forecast, HBM *"opportunities"* (July 2026 EX-99.1). (3) The 10-K
names no customer after FY2022 and no competitor in its competition section in any year (the one rival named anywhere is
in the litigation note), so the two facts a reader most needs to judge durability are mostly withheld.

**Why it does not carry, and what is excluded.** HHH, RGTI and DJT closed at Q1 because the declared business was not the
filed one or the share's business was undecided. **Here the filed business and the declared business are the same
machines and consumables**; only the buyers change. I can state the unit economics of every dollar of FY2019-26 revenue
from the revenue note. **What is outside the circle is the forecast part**: AI wafer-level burn-in at a *"top-tier AI
processor supplier"* that has only benchmarked, HBM burn-in, the second hyperscale device. Those have no revenue line, and
[E4-46] says study will not repair that (*"if we can't make a decision in five minutes, we can't make it in five
months"*). They are recorded as outside the circle and **cannot be counted at any later gate**, including Q5. Whether the
understood business has a position that survives the constant change of its customers is a moat question: carried to Q2.

- **VERDICT: [x] IN** on the business the filings show (systems, per-device contactors and service to a few chipmakers and
  test houses, the whole of FY2019-26 revenue). **Not IN** for the AI, HBM and new-customer revenue that exists only in
  guidance and releases; outside the circle [E3-31, E4-46], never counted later.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that *"(1) is needed or desired; (2) is thought by its customers to have **no
> close substitute** and; (3) is not subject to price regulation."* **[E3-03]**, 1991 letter

### THE HYPOTHESIS TO BE REFUTED, AT FULL STRENGTH **[E4-26, E4-51]**
Aehr is the only company that burns in a whole silicon-carbide or AI wafer at once. The 10-K says its machine does in one
footprint what competitors need eighteen probers for, and that wafer-level burn-in screens out devices that would otherwise fail after packaging, *"where the yield impact
could be 10 times or even 100 times as costly."* Once qualified on a device, every contactor for that device is Aehr's, for two to
seven years, a consumable annuity. The largest silicon-carbide maker put 82% of Aehr's FY2022 revenue through it; the lead
AI customer is *"shifting their burn-in from system-level to all wafer-level"*; backlog rose from $15.2M to $80.6M in a
year (FY2026 10-K). If a tiny equipment company can have a moat, it is a sole-source consumable on a qualified process.

### THE THREE CONDITIONS **[E3-03]**
- **(1) Needed or desired: YES, by some buyers, some years.** Automotive silicon carbide and AI processors burn in because
  field failure is expensive; the FY2022-24 orders and the FY2026 backlog show it.
- **(3) Not subject to price regulation: YES.** Export-control and tariff exposure are named (Item 1A), not price
  regulation.
- **(2) No close substitute: NO, AND THE FILINGS SAY SO.**
  - **The company's own Item 1A, FY2026:** *"Some users of our systems, such as independent test labs, build their own
    burn-in systems, while others, particularly large IC manufacturers in Asia, acquire burn-in systems from captive or
    affiliated suppliers. Our WaferPak products are facing and are expected to face increasing competition. Several
    companies have developed or are developing full-wafer and single-touchdown probe cards. We expect that our DiePak
    products for burning-in and testing multiple singulated die and small modules face significant competition."*
  - **The substitute is a different place to burn in, and the 10-K describes it:** *"This can either be done at the wafer
    level, before the die are packaged, or at the package level, after the die are packaged"* (Item 1), and Aehr itself
    now sells the package-level alternative (Incal). The July 2026 release's best news is a customer *"shifting their
    burn-in from system-level to all wafer-level"*: **the customer had a substitute and used it until now.**
  - **The customers' conduct:** the largest customer's share went 82% (FY2022, onsemi), 79%, 67%, 39%, 26% (FY2026); the 10-K has
    named no customer since FY2022, so whether the silicon-carbide buyer is still among FY2026's three is not stated; contactor revenue, the "annuity", fell from $37,560K (FY2024) to $14,887K (FY2026), **-60% in two
    years**, and *"EV and power semiconductor revenues"* from 92% to 17%. The FY2025 10-K gives the reason: *"continued
    softness in the power semiconductor demand for electric vehicles"*. A consumable that the installed base stops
    buying when its owner's end market slows is not an annuity.
  - **A named rival in wafer-level burn-in, in the company's own litigation note** (FY2026 10-K Note 9): *"On October 16,
    2024, the Company filed a complaint with the China Suzhou Intermediate Court ... against Suzhou Semight Instruments
    Co., Ltd. ("Semight") ... alleging infringement of the Company's two patents related to wafer burn-in systems and
    wafer reliability test systems."* Semight petitioned to invalidate both patents; the decisions *"upholds part of the
    claims"*; and in December 2025 the first-instance court *"dismissed the Company's claims based on the court's opinion
    that there was insufficient evidence to establish infringement"* (appeal pending; a further invalidation petition
    filed 2026-01-27). **The only competitor any Aehr filing names is a Chinese maker of wafer burn-in systems whose
    product a court has so far found not to infringe.** The WaferPak's legal moat is, on the filed record, contested
    and partly narrowed.
  - **Price, in the company's own words:** *"The Company has observed price competition in the systems market,
    particularly with respect to its less advanced products"* (Item 1, every 10-K FY2022-26), and on costs: *"Should the
    Company increase its sales prices to recover the increase in costs, this could result in a decrease in the
    competitiveness of our products"* (FY2026 Item 1A). Gross margin fell from 49.1% to 35.3% in two years and the FY2026
    MD&A blames *"higher assembly and warranty costs, increased freight expenses, and higher tariffs on imported parts"*:
    **costs rose, and the price did not follow.**

**Criterion (2) fails, so the conjunction fails.**

### THE COMPETITOR ROW - required **[E3-28]** *(CONVENTION, confessed at section VI of v4; the corpus's own test is pricing conduct plus returns on capital [E3-43])*
**The company names no competitor in the competition section of any 10-K FY2019-26** (read: the FY2026 *"COMPETITION"*
section and Item 1A name none; FY2022's names only *"several regional, low-cost manufacturers"*); the one company named
as a rival anywhere is Semight, in the litigation note (above), a Chinese filer of nothing with the SEC. EDGAR full-text search for *"Aehr"* across 10-K and
20-F filings (`efts.py`, run by this run) finds **no current SEC filer that names Aehr**: FormFactor named it in its 10-Ks
for FY2008-12 only; Cohu (CIK 0000021535) and Teradyne (CIK 0000097210) return zero with the correctly padded CIK. **The
direct burn-in makers are private or foreign and file nothing with the SEC** (KES Systems, Micro Control Company, DI
Corporation, ESPEC, Chroma ATE, and Advantest, which files no US annual report); none was pulled.

So the row takes **the three SEC-filing test-equipment makers that sell the substitutes the 10-K itself names**: full-wafer
probe cards (FormFactor), back-end test handlers and contactors (Cohu), and system-level and automatic test (Teradyne).
**One specification: five filed fiscal years each, from each filer's own 10-K faces, re-read on a fresh EDGAR fetch**
(`peers/getpeers.py`, `peers/getpeers2.py`; every peer figure below was found in the filer's own text, `peers/peerfacts.py`
marks each; arithmetic `peers/calc.py`, output `peers/calc_out.txt`). **The windows differ by seven months**: AEHR's are May
years FY2022-26, the peers' December years FY2021-25.

| company | 5y revenue ($M) | gross margin, 5y (first → last year) | operating margin, 5y | revenue, first → last year | 5y OCF − SBC − capex, % of revenue | SBC / OCF, 5y | 10-K accessions read |
|---|---:|---|---:|---:|---:|---:|---|
| **AEHR (subject)** | **291.0** | **44.9% (46.6% → 35.3%)** | **3.9%** | **-1.6%** | **-9.4% (-$27.2M)** | **787%** | `0001654954-26-006919`, `-24-009642`, `-22-011877` |
| FORM | 3,729.3 | 40.1% (41.9% → 39.3%) | 9.6% | +2.0% | +1.6% | 31% | `0001039399-26-000009`, `-23-000010` |
| COHU | 3,191.1 | 45.3% (43.6% → 42.7%) | 7.2% | -48.9% | +5.7% | 26% | `0001437749-26-004339`, `-23-003782` |
| TER | 15,544.1 | 58.7% (59.6% → 58.2%) | 24.3% | -13.9% | +15.8% | 8% | `0001193125-26-059002`, `-23-044711` |

(COHU reports no gross-profit line; its margin is *"Net sales"* less *"Cost of sales"* from its own statements of
operations.)

**WHERE THE SUBJECT SITS:** the steepest gross-margin fall of the four (-11.3 points; the others moved -2.6, -0.9 and -1.4)
and the lowest last-year margin; the lowest five-year operating margin; **the only one whose operating cash after stock pay
and capex was negative over five years**, with stock pay eight times its operating cash. On revenue it sits between FORM and
TER. **Not the price leader, not the margin leader, and not the direction leader.**

- **Peers named: three filers, of an industry whose direct burn-in competitors (at least six named above) file nothing
  with the SEC.** Buffett says eight **[E3-28]**. **This does not make the class PROVISIONAL, and the reason is
  directional, as the BX run argued:** the finding rests on the subject's own record (its own words on substitutes and
  price, its own customers' conduct, its own margins and cash), which is the corpus's single-company test [E3-43]; every
  unpulled direct competitor is an additional substitute and can only strengthen it. Were Q2 heading for IN, the Advantest
  annual report and the Korean and Japanese filers would have to be read first and the class held PROVISIONAL.
- **The row's limit, stated [E3-61]:** it shows position, not conduct; the conduct is in the company's own sentence about
  price.

### THE OTHER Q2 TESTS
- **The two-characteristic test [E2-44]: fails both halves.** (a) Price rises under flat demand: **NO**; the company says a
  price rise to recover costs would cost it competitiveness, and margin fell 14 points while revenue fell. (b) Growth with
  minor added capital: **NO**; the FY2022-24 growth consumed $29.9M of inventory increase on the cash-flow faces ($6,674K, $9,469K
  and $13,732K; the balance went from $8.8M at FY2021 to $37.5M at FY2024) and was financed by $24.0M (FY2022) and
  $6.8M (FY2023) of stock sold, then $97.4M in FY2026.
- **Return on capital [E3-46]:** operating income FY2022-26 $7.8M, $13.4M, $10.1M, -$5.7M, -$14.1M, **$11.4M in five
  years on $291.0M of revenue**, against equity that grew from $11.4M (FY2021) to $219.5M (FY2026), about two-thirds of the $208M
  increase from stock sold for cash ($24.0M, $6.8M and $97.4M) or issued for Incal ($9.4M). FY2024's $33.2M net income was $12.5M pretax plus *"release of a valuation allowance of $21.9 million"* (FY2024
  MD&A). Not a high return on capital in any window longer than two years.
- **Must the moat be continuously rebuilt? [E4-04], and the four causes [E4-36]:** yes, by the filings' own shape. Each
  contactor set is custom to a device and lives *"two to seven years"*; each end market (test labs, silicon carbide, AI,
  photonics, the HBM hope) must be won with new qualification; the customer list has turned over twice in five years.
  The spending buys the next market, not the defence of one advantage. The FY2022-24 record is **wave-riding [E3-51]**: one
  customer's silicon-carbide capacity build, which ended when *"power semiconductor demand for electric vehicles"* slowed;
  a surfing run is not a moat. **The TSMC tension against [E4-04] (the 2023 meeting) is an open operator question**; v4 is
  applied as written, and the tension would not change this verdict, because criterion (2) fails independently.
- **Who holds the bargaining power:** the buyer. 70-98% of revenue from five customers in every year FY2020-26, one at 82%.
  **[E3-62]** asks who keeps the gains: the FY2022-24 capacity went to the buyer's silicon-carbide output at a 46-50% gross
  margin to Aehr, and when the buyer stopped, Aehr kept the inventory ($41.4M, 83% of FY2026 revenue).
- **[E4-37], the price-rise test:** answered in the company's own sentence above. No price increase is on file in any 10-K
  or release read.
- **Untapped pricing power [E3-33, E5-28]:** would need near-monopoly; the company's own filings list substitutes at three
  stages. None.
- **The dominance class [E2-53]:** NO.
- **The attacker's test [E2-45]:** the 10-K answers it: *"Several companies have developed or are developing full-wafer and
  single-touchdown probe cards"*, and captive suppliers serve the large Asian makers; and Semight (Note 9) is the attacker already in the field.
- **Direction [E4-32]:** narrowing. Gross margin 50.4% (FY2023) to 35.3% (FY2026); the consumable line -60% in two years.
  **[E4-55]** (units, not dollars): no unit series is disclosed; the contactor dollars are the nearest thing, and they fell.
- **Key-person dependence [E4-23], recorded here as the moat check it is:** *"Our success depends to a significant extent
  upon the continued service of Gayn Erickson, our President and Chief Executive Officer ... We do not maintain key person
  life insurance ... and none of our employees are subject to a non-competition agreement with us"* (FY2026 Item 1A). A
  standard clause, but here the business also depends on winning each new market, which is a sales-and-engineering task.
  **Recorded as a defect of the business.**

### CLASS AND VERDICT
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL.** A small equipment maker with a real technical edge in one way of
  burning in chips, selling to buyers who have other ways and use them. *(Not PROVISIONAL: the finding stands on the
  subject's own words and record [E3-43]; the unpulled direct competitors can only add substitutes.)*
- **Direction: narrowing** (gross margin 50.4% to 35.3%; contactors $37.6M to $14.9M; the customer base replaced).
- **VERDICT: [x] OUT, ON THE BUSINESS. Permanent.** Criterion (2) of **[E3-03]** fails on the company's own Item 1A (customers
  *"build their own burn-in systems"* or buy from *"captive or affiliated suppliers"*; competitors are developing
  *"full-wafer and single-touchdown probe cards"*), on its own statement that raising prices to recover costs *"could result
  in a decrease in the competitiveness of our products"* while gross margin fell from 49.1% to 35.3% **[E2-44, E4-37]**, on
  the customers' conduct (the largest customer's share 82% to 26%; the consumable -60% in two years), on a row in which the
  subject has the steepest margin fall and the only negative five-year owner cash **[E3-46]**, and on a record that is a
  wave ridden and then lost **[E4-04, E3-51, E4-36]**, with key-person dependence recorded **[E4-23]**.
  *Not UNRESEARCHED: the finding stands on the subject's own filings; the unfiled competitors can only add substitutes.
  Not UNKNOWABLE: the evidence is in and it decides.*
- **A conclusion that required fighting for it is worth less [E4-18].** This one did not: the 10-K's own risk factor names
  the substitutes and its own sentence names the price limit.

**⛔ THE FILE CLOSES HERE. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING** (the BAM, DJT, RIVN and BX precedent),
written because the brief asks for the owner-earnings rebuild and the Q3 read, and because they set the reopening
conditions at Q6. **Q5 carries the heading `COMPUTATION — NOT A CLEARANCE` and no entry language appears anywhere
below.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT, on the business). Written because the brief asked for the
> earnings releases and the proxy to be read, and because the findings belong in the reopening conditions. Nothing here
> can promote the name or repair Q2 **[E2-37, E2-38, E3-39]**.

### STEP 1 - THE WEIGHT CASE
- [x] **Daily execution [E3-38, E3-43]:** Q2 found a business, not a franchise, whose revenue is re-won market by market
  and device by device (the customer list replaced twice in five years). *"a business, unlike a franchise, can be killed
  by poor management."*
- [ ] **Control [E1-16]:** a minority purchase of a listed share.
- [ ] **Leverage [E3-29]:** no debt; the Silicon Valley Bank facility was terminated on 2024-01-04 with nothing drawn.

**Case declared: a BINARY GATE** on daily execution. No price compensates.

### THE BINARY - honesty **[E5-16]**, each matter dated to when it became PUBLIC
1. **The guidance class action, filed 2024-12-03 (public in the FY2025 10-K of 2025-07-28 and the Q3 FY2026 10-Q).**
   *"a putative shareholder class action lawsuit captioned Lucid Alternative Fund, LP v. Aehr Test Systems, Inc. ... alleged,
   in part, that the Company and certain of its executives made materially false and misleading statements regarding the
   Company's earnings guidance and other financial projections for 2024"*, class period January 9 to March 24, 2024 (the
   weeks between the first and second cuts of FY2024 guidance, below). *"On May 16, 2025, the court-appointed lead
   plaintiff elected to dismiss the case voluntarily, with all parties to bear their own fees and costs"*; two derivative
   complaints were dismissed *"without prejudice pursuant to the parties' stipulation"* on 2025-06-09 (Q3 FY2026 10-Q,
   `0001654954-26-003348`, Note on commitments and contingencies). **No finding, no settlement paid.** Read against
   **[E5-22]** (penalty size is not seriousness, in either direction): the absence of a penalty is not a finding of
   candor; what the guidance record itself shows is scored under the flags below.
2. **The Semight patent litigation (from 2024-10-16):** the company as plaintiff; a business matter, recorded at Q2.
3. **No SEC order, restatement, auditor resignation or late filing** was found: BPM LLP signed every audit opinion FY2019-26;
   no 10-K/A since FY2008; no NT filing in the index. The SEC's enforcement pages were not searched (a named gap; the SEC
   litigation and administrative-proceedings indexes would resolve it).
- **Recorded (not governing): IN on the binary as filed**, written as the absence of a found disqualifier, not a finding
  that anyone is honest **[E5-17]**.

### THE INCENTIVE READ **[E4-27]**
- **What pay vests on (DEF 14A, 2026-09-09, `0001654954-26-008222`):** FY2026 cash bonus *"revenue-based and
  profit-based"* (not earned for FY2026); performance RSUs that vest *"upon the achievement of a performance condition
  related to the Company's cumulative revenue target for certain markets"* (the FY2025 tranche *"satisfied"* at 2026-05-29;
  the FY2026 tranche measured to 2027-06-25); the package-level executive's *"booking commission"* of $433,557. **Pay vests
  on revenue and bookings, not on cash, margin or return on capital.** The CEO's FY2026 Summary Compensation total was
  $3,226,098; *"Compensation Actually Paid"* $22,404,627, almost all of it the rise in the stock price on unvested awards.
- **What insiders did (Form 4s filed 2025-06-01 to 2026-09-03, `form4_table.txt`, parsed by this run):** about **735,000
  shares sold in the open market for about $61M**, by 13 directors and officers, the CEO about $16.0M of it (152,824 shares
  at $70.58 on 2026-04-10 and 40,000 at about $131 on 2026-08-12); **no open-market purchase** in the period. The April 2026
  selling began on 2026-04-09, the day after the company's own $60M ATM prospectus supplement (2026-04-08), whose 812,185
  shares were sold in April at an average $73.87. Directors and officers as a group hold 1,488,042 shares, 4.6% (DEF 14A,
  as of 2026-08-27). Whether the sales were under Rule 10b5-1 plans was not checked (the
  parser did not read the footnotes). Recorded as the incentive fact it is: the people paid on revenue sold alongside the company when the
  price was high; no inference about conduct is drawn from it.

### STEP 2 - THE FLAGS. *Each is a prompt to READ, never a verdict.*
- [ ] **Weak accounting:** SBC expensed; the FY2024 *"release of a valuation allowance of $21.9 million"* is disclosed on
  its own line and explained (pretax $12,458K against net income $33,156K); the auditor's critical audit matter is
  inventory reserves. Not ticked.
- [ ] **Unintelligible footnotes:** no. But the 10-K has named **no customer since FY2022** while one customer was 67-79% of
  revenue; recorded under candor.
- [x] **Trumpeted projections [E4-22], scored against outturn as [E3-48] requires:**

  | guidance, as given in the 8-K EX-99.1 | when | outturn (10-K) |
  |---|---|---|
  | FY2023: *"at least $60 million to $70 million"* | 2022-07-19 | $65.0M: met |
  | FY2024: *"at least $100 million ... and GAAP net income of at least $28 million"* | 2023-07-13, reiterated 2023-10-05 | revised 2024-01-09 to *"between $75 million and $85 million"*, then in March to *"greater than $65 million in total revenue and net income of at least $11 million"*; actual **$66.2M, 34% below the first figure**; net income $33.2M only through the $21.9M tax release |
  | FY2025: *"at least $70 million and net profit before taxes of at least 10% of revenue"* | 2024-07-16, reiterated 2024-10-10 and 2025-01-13 | *"temporarily withdrawing our guidance"* 2025-04-08; actual **$59.0M**, pretax loss $4.3M |
  | H2 FY2026: *"revenue between $25 million and $30 million"* | 2026-01-08 | $10.3M + $18.8M = $29.1M: met |
  | FY2027: *"between $130 million and $150 million ... non-GAAP net income to be 18% to 22% of total revenue"* | 2026-07-14 | open |

  Two of four closed guidances met, two missed by 16-34%, and the July 2022 release promised demand that *"increases
  exponentially throughout the decade"*. **[E5-30]**: guidance is a ratchet, withdrawn in April 2025 and **reinstated
  within nine months**. Ticked.
- [x] **Serial share issuance [E5-15]:** 13,331,965 shares (2016 cover) to 21,417,011 (2017) to 32,620,450 (2026), **2.4
  times in ten years**; a 2017 public offering, ATM programmes of $25M (2021), $25M (2023), $40M (2024) and $60M (2026), and
  552,355 shares for Incal. Ticked.
- [x] **Adjusted-earnings promotion [E4-29, E5-06]:** the July 2026 release's headline measure after revenue is *"Non-GAAP net
  income, which excludes stock-based compensation"*: **$0.9M for FY2026 against a GAAP loss of $7.1M**, and FY2027 guidance
  is given only as *"non-GAAP net income"*. Not EBITDA; the same deletion of the expense [E5-06] says is simply an expense.
  Ticked.
- [x] **Metric-switching [E2-49]:** the FY2025 target was *"net profit before taxes of at least 10% of revenue"* in July and
  October 2024 and became *"non-GAAP net profit before taxes of at least 10% of revenue"* on 2025-01-13, as results fell; the
  FY2024 target had been *"GAAP net income"*. **A switch that follows deterioration fires.** Ticked.
- [ ] **Filed-figure tells [E4-30]:** cash taxes of $4K-$100K a year against pretax income of $9.5-14.6M in FY2022-24 are
  loss carryforwards (the valuation allowance note), not a tell. Not ticked.
- **Flags that converge [E4-52]:** four ticks (projections, issuance, adjusted earnings, the switched yardstick), each
  pointing the same way: the public narrative is carried by forward revenue and pre-SBC profit while the filed cash is
  negative. Recorded as one system, not four prompts; a reading of the accounting, never of the person **[E5-38]**.
- **The auditor's-eye test [E4-34]:** the fourth question (period-shifting) bears on a lumpy equipment seller whose
  quarterly revenue is shipment-timed; no bill-and-hold or channel note was found in the revenue-recognition policy read.
  Not answered beyond that.

### STEP 3 - THE PRIMARY TEST **[E2-01]**
Net income on average equity: FY2022 30%, FY2023 23%, FY2024 35% (13% on pretax income, the rest the tax release), FY2025
-3.3%, FY2026 -4.2%. Five-year net income $46.1M, of which $21.9M is the tax release; **about 5% a year on the average
equity excluding it**, and equity itself was raised, not retained (Q2).

### CANDOR - THE HALF-OWNER TEST **[E2-26]**
Two deductions. (1) **The customers are withheld**: from FY2023 the 10-K gives *"two customers accounted for approximately
79% and 10%"* with no names, while the FY2022 10-K had named *"ON Semiconductor"*; a half-owner would want to know whose
capacity plan is 79% of the business. (2) **The headline measure deletes stock pay** and guidance switched to it as results
fell (above). One credit: the 10-K discloses the EV share of revenue every year (92% to 17%), which is the fact that
decided Q2.

### RATIONALITY IS CAPITAL ALLOCATION
- **Buybacks [E5-08]:** none (only withholding on vesting). **The reverse is the live question:** the company sold
  1,942,653 shares for $100.0M in FY2026 at an average $51.48, at 20-60 times revenue. Selling stock the market prices far
  above any value the filings support is, for the remaining holders, the right direction of the [E5-24] law (*"what is
  smart at one price is dumb at another"*); recorded as consistent with it, not as a flag.
- **The acquisition [E3-40, E2-30]:** Incal, $22.2M, now 37% of revenue, earning *"$ 3.8 million in net income"* in its first ten
  months; it bought the package-level substitute the Q2 finding names. Not a loss-of-focus case on the filings.
- **The institutional imperative [E2-30]:** (4) *"peer behaviour mindlessly imitated"*: the FY2026 10-K and releases chase the
  AI, photonics and HBM narratives every equipment maker chases; a prompt, recorded.
- **VERDICT (RECORDED, NOT GOVERNING): IN on the binary as filed**, with four flags ticked that converge on forward-revenue
  promotion **[E4-22, E5-15, E4-29, E2-49, E4-52]** and a pay plan that vests on revenue. Not an OUT on the filings read.

### THE GUARDRAIL
- [x] Nothing in this Q3 promotes the name; Q2 is closed on the business **[E2-37, E2-38, E3-39]**.
- [x] Key-person dependence recorded at Q2 as a defect **[E4-23]**.
- [x] No great-manager exception is claimed.

## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The brief asked for the owner-earnings rebuild over every window the filed statements
> support, both (c) ends and the acquisition's treatment; it is done here and it governs nothing.

### Owner earnings — the one number **[E2-23]**
**Windows: every one the filed faces support.** FY2017-26 are all on 10-K faces read by this run (FY2019, FY2020, FY2021,
FY2022, FY2024 and FY2026 10-Ks). **Five years FY2022-26 is the default [E2-42]**; also three years FY2024-26, ten years
FY2017-26 (a full cycle, before, during and after the silicon-carbide wave), and the two sub-windows the brief's question
needs: **the wave FY2022-24** and **before the wave FY2017-21**. No window before FY2017 was built (the FY2016 and earlier
10-Ks were not fetched; nothing in them would reach the default). `oe.py`, `oe_out.txt`, $K, every input from the faces:

| FY | OCF | SBC | D&A | capex | acquisition | **OE, D&A end** | **OE, capex end** | OE, capex + acquisition | working-capital lines (of which inventory) | OE before working capital, D&A end |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2017 | -4,495 | 999 | 271 | 477 | | -5,765 | -5,971 | -5,971 | -313 (430) | -5,452 |
| 2018 | -1,351 | 996 | 417 | 572 | | -2,764 | -2,919 | -2,919 | -3,234 (-2,073) | 470 |
| 2019 | -5,637 | 905 | 431 | 173 | | -6,973 | -6,715 | -6,715 | -1,735 (-112) | -5,238 |
| 2020 | -2,024 | 910 | 384 | 163 | | -3,318 | -3,097 | -3,097 | -561 (1,164) | -2,757 |
| 2021 | -2,701 | 1,101 | 310 | 227 | | -4,112 | -4,029 | -4,029 | 316 (-972) | -4,428 |
| 2022 | 1,508 | 3,006 | 356 | 416 | | -1,854 | -1,914 | -1,914 | -10,295 (-6,674) | 8,441 |
| 2023 | 10,011 | 2,748 | 450 | 1,362 | | **6,813** | **5,901** | 5,901 | -7,841 (-9,469) | 14,654 |
| 2024 | 1,756 | 2,518 | 657 | 749 | | -1,419 | -1,511 | -1,511 | -14,378 (-13,732) | 12,959 |
| 2025 | -7,400 | 5,162 | 2,312 | 4,992 | 11,075 | -14,874 | -17,554 | -28,629 | -12,203 (-2,441) | -2,671 |
| 2026 | -3,310 | 6,761 | 2,799 | 2,066 | 1,801 | -12,870 | -12,137 | -13,938 | -1,760 (11) | -11,110 |
| **5y FY2022-26** | | | | | | **-4,841** | **-5,443** | **-8,018** | | 4,455 |
| 3y FY2024-26 | | | | | | -9,721 | -10,401 | -14,693 | | -274 |
| 10y FY2017-26 | | | | | | -4,714 | -4,995 | -6,282 | | 487 |
| the wave FY2022-24 | | | | | | 1,180 | 825 | 825 | | 12,018 |
| before the wave FY2017-21 | | | | | | -4,586 | -4,546 | -4,546 | | -3,481 |

- **The screen is reproduced**: five-year capex end -$5,443K exactly; D&A end -$4,841K against `a8bc84f`'s -$4,839.6K (the
  FY2022 D&A vintage, 307 against 356).
- **Is there any window in which owner earnings are positive? One year and one sub-window.** FY2023 alone ($5.9-6.8M), and
  the wave FY2022-24 at **$0.8-1.2M a year**, which is **about zero** on a $3.05bn price. Every window the filings support
  that includes a year outside the wave is negative. Before working capital, the wave earned $12.0M a year; the five-year
  default $4.5M; ten years $0.5M.
- **What the working-capital increment is made of, and whether it reversed [E2-23]:** FY2022 receivables $7.8M and
  inventory $6.7M (the first onsemi shipments); FY2023 inventory $9.5M, partly carried by payables +$5.0M; **FY2024
  inventory $13.7M built *"due to anticipated customer demand"*** (FY2024 MD&A) while payables were paid down $3.9M (the
  `working_capital_flag`'s 222%: payables of -$3,891K against OCF of $1,756K) and receivables released $6.8M; FY2025
  prepaid and other $5.0M (unbilled receivables and prepayments) and receivables $3.0M; FY2026 receivables $3.3M and
  prepaid $2.8M against customer deposits +$3.2M (deferred revenue $1,981K to $5,192K). **It did not reverse**: inventory
  was $37.5M at FY2024 and $41.4M at FY2026 on revenue a quarter lower. The build made for the wave is still on the
  balance sheet, and [E2-23] counts the increment where the business requires it: a seller whose next wave needs its own
  device-specific inventory requires it.
- **Maintenance capex, a DISCLOSED JUDGMENT:** plant is $8.9M; capex was $0.2-0.6M a year before FY2022 and $0.4-5.0M
  since (FY2025's $5.0M *"primarily related to office renovation"*). **The D&A default [E3-44, E2-41] is valid; the [E5-20]
  exception class does not apply.** The two ends differ by $0.6M a year; the band is not what matters here.
- **The acquisition, and how (c) treats it:** Incal cost $12.9M of cash in the window (plus $9.4M of stock). The D&A end
  charges it only through intangible amortization (about $1.2M a year from FY2025); the capex end not at all. **The honest
  treatment is to charge it**, because it bought the package-level line that is 37% of FY2026 revenue and without which
  FY2025-26 revenue would have been about $39M and $31M: the growth in the window was bought, not built. Shown as its own
  column (five-year **-$8.0M**). The $9.4M of stock is not in any column; counting it would lower the figures further.
- **SBC, resolved and complete on the face in every year used:** *"Stock-based compensation expense"* 999 to 6,761 ($K),
  matching companyfacts; no capitalised SBC disclosed. **SBC exceeded operating cash in two of the three positive-OCF years**
  (199% FY2022, 143% FY2024) and OCF was negative in the other seven. **[E3-70] asks for the market measure:** the FY2026
  grants were 533,000 RSUs and PRSUs at a weighted *"$15.39"* grant-date value, $8.2M against a $6.8M charge (the grant
  table, read by hand: FY2026 10-K equity note); the same grants are worth $49.8M at today's $93.49. The charge is the
  floor of the subtraction, as [E3-70] requires.
- **[E4-41], normalize down for luck:** the wave was one customer's capacity build; FY2023 is its peak and the only
  positive year. Nothing in the window is normalized up. The FY2026 figure also contains interest earned on raised cash
  ($1.4M), which is not operating.
- **Short-window mean (3y FY2024-26): -$9.7M to -$14.7M.** **Long-window mean (5y FY2022-26, the default): -$4.8M to
  -$8.0M.** Ten years: -$4.7M to -$6.3M. **Combined range, five-year default: about minus $5M to minus $8M a year: negative
  at every end.** **Is the range too wide to conclude?** No; it is narrow and entirely below zero, which is a conclusion.

### Great, good, or gruesome? **[E4-20, E4-43]**
- [ ] great · [ ] good · [x] **gruesome, on the filed record.** *"grows rapidly, requires significant capital to engender
  the growth, and then earns little or no money"*: revenue quadrupled FY2021-24 and required $29.9M of inventory (FY2022-24) and $30.8M of
  stock sold (FY2022-23) to do it; over ten years the business consumed about $50M of owner earnings and was financed by
  about $149M of stock sold for cash (FY2017's public offering and private placement, $21.1M, then $24.0M, $6.8M and
  $97.4M). **[E4-43]'s exception**
  (*"unless the cash they consume gets to earn a reasonable return"*) is not met in any window the filings support.

### Staying power — score all three **[E5-11]**
- **(1) Large and reliable stream:** **no.** Operating cash positive in three of ten years; the five largest customers
  70-98% of revenue.
- **(2) Massive liquid assets:** **yes, bought.** $116.4M of cash at 2026-05-29 against a burn of $5-15M a year, all of it
  from the FY2026 ATM.
- **(3) No significant near-term cash requirements:** **none found beyond working capital.** No debt; *"unconditional purchase obligations, which have a remaining term in excess of 12
  months, are not material"* (FY2026 10-K; shorter purchase commitments are not quantified there); the FY2027 guidance ($130-150M from $50M) would require inventory and receivables
  in proportion, the one requirement that matters, now funded.
- **Leverage [E4-16, E3-29, E2-54]:** none. The [E2-54] coverage test is moot without interest.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**
- **The mechanism, stated as its holders would accept it:** Aehr does not run out of money; it runs out of wave. A customer
  in a new market (silicon carbide in 2021, AI processors and photonics now) qualifies Aehr's machines and buys capacity
  and device-specific contactors for a few years; the company builds inventory ahead of the ramp and sells stock to fund it;
  when that customer's end market slows or it moves burn-in to another stage or supplier, systems and contactors stop
  together, the inventory stays, and the next wave has to be found and funded again. The FY2022-26 record is one full
  turn: revenue $16.6M to $66.2M to $50.0M, EV share 23% to 92% to 17%, contactors $37.6M to $14.9M, owner earnings
  positive in one year. **A new shape is proposed: #20 THE WAVE** (below), **with #8, THE EQUITY IS THE REVENUE, as a
  feature**: over ten years the owners' new money, not the customers, funded the working capital.
- **The exposure, quantified [E4-40]:** FY2027 guidance of $130-150M against $50.0M, with *"effective backlog of
  approximately $100 million"*; a repeat of FY2024-26 (the lead customer's share 67% to 26%, revenue -24% in two years) from
  the guided level would leave inventory built for $140M of revenue behind, against $116.4M of cash. The company survives
  that; the owner's return does not.
- **Likelihood:** the wave ending, **a real possibility** (it has happened once in the filed window); insolvency, **a
  low-level possibility** while the ATM cash lasts.
- **VERDICT (RECORDED, NOT GOVERNING): would be OUT.** Gruesome on the filed record **[E4-20]**: owner earnings negative at
  every end of the five-year default and in every window but the wave itself; survival bought with stock, not earned
  **[E5-11]**.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT. The block below is arithmetic only.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

### COMPUTATION — NOT A CLEARANCE
Cap **$3,049.7M** ($93.49 x 32,620,450); sovereign **5.34%** (US Treasury 30 Yr, 09/18/2026).

| owner earnings case | $M a year | yield on the cap | vs 5.34% |
|---|---:|---:|---:|
| 5y FY2022-26, D&A end | -4.8 | -0.16% | -5.50 |
| 5y FY2022-26, capex end | -5.4 | -0.18% | -5.52 |
| 5y FY2022-26, capex plus the acquisition | -8.0 | -0.26% | -5.60 |
| 10y FY2017-26, D&A end | -4.7 | -0.15% | -5.49 |
| the wave FY2022-24, capex to D&A end (the most generous window) | 0.8 to 1.2 | 0.03% to 0.04% | about -5.3 |
| the wave FY2022-24, before working capital (more generous than [E2-23] allows) | 12.0 | 0.39% | -4.95 |

- **The growth the price needs is not a number**: from a negative base no growth rate reaches the floor (the refusal rule of
  2026-09-12, tooling change D). In dollars: **a 10% pre-tax return [E4-28] on $3,050M needs about $305M a year of owner
  earnings**, six times FY2026 revenue. **[E4-35]** and **[E4-44]** bind, and a Q2 OUT on a narrowing margin does not carry
  that burden.
- **Shown once and not counted (Q1 put it outside the circle):** the company's own FY2027 guidance, *"non-GAAP net income to
  be 18% to 22% of total revenue"* on $130-150M, is $23-33M **before stock pay**, 0.8-1.1% of the cap. Granting management's
  forecast and its measure leaves the yield below a fifth of the bond. It changes nothing.

### THE VALUE, AS A ROUND-NUMBER RANGE **[E4-01]**
**No earning-power value on the filed record**: owner earnings are negative at every end of every window but one
sub-window, where they round to zero. What the share holds is the balance sheet: equity $219.5M, **tangible equity about
$200M ($6 a share)**, of which $116.4M is cash and $41.4M inventory. **Price $93.49 is about fifteen times that.** Bar 2, the
screamer test **[E4-01]**: the answer would be *no*; the price is above the whole range. **Windage count: zero** (no
normalization lowered anything; the acquisition column is a treatment, shown beside the unadjusted ends).

- **VERDICT: none. Q5 did not open (Q2 OUT).** Had every gate been IN, the computation shows a yield of about -0.2% against
  a 5.34% bond and a ~10% floor, at a price about fifteen times tangible book.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

> **RECORDED, NOT GOVERNING.** Nothing is owned and nothing is armed (a Q2 OUT is a finding about the business, and a
> price alert on it would be a category error, the QLYS ruling). These are the conditions on which the file would be
> reopened, written before any reopening **[E1-02]**.

**What would reverse Q2 (the governing gate), in words:**
1. **Pricing shows up**: gross margin back above 50% and held for three years **while costs rise** (tariffs, freight), with a
   price increase disclosed in a 10-K or release [E2-44, E4-37].
2. **The consumable becomes an annuity**: contactor revenue rising for three consecutive years across **more than one**
   end market, with no single customer above 30% of revenue, so that the installed base, not one buyer's capacity plan,
   carries it [E4-04, E3-51].
3. **The substitutes fail on the record**: the Semight appeal won and the patents upheld in full; a 10-K that names its
   competitors and shows share taken from package-level and system-level burn-in.
4. **Owner cash**: operating cash less stock pay less capex positive over a rolling five-year window, without equity raised
   in it.

**What would close it harder:** another guidance withdrawal or a miss of the FY2027 range; a further ATM; the FY2026
inventory written down; the largest customer again above 60%.

**Next catalyst date:** the first 10-Q of the June fiscal year (quarter ending about 2026-09-25), and whatever covers the
2026-05-30 to 2026-06-26 transition weeks.

**The sell rule [E2-28]** does not apply (nothing held). **Position size:** none.
**VERDICT (RECORDED, NOT GOVERNING): not applicable; the file closed at Q2 and Q6 arms nothing.**

---
## SELF-AUDIT
- [x] Questions answered in order; the gate stopped at Q2 (OUT, on the business); Q3-Q6 recorded beneath explicit
  RECORDED, NOT GOVERNING banners, with Q5 headed COMPUTATION — NOT A CLEARANCE and carrying no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the filed revenue note
  FY2021-26 and the unit economics stated from it; the forecast revenue is excluded by name. Q3's IN is recorded and not
  governing.
- [x] No UNRESEARCHED or UNKNOWABLE verdict was returned; the case for UNKNOWABLE at Q1 is recorded at full strength and
  not taken, with the reason.
- [x] Step 0: the skip reason reproduced and explained on the FY2022 10-K (an organic step on consecutive years and one
  element, 82% from onsemi); the entity checked (one corporation; the fiscal-year change of 2026-04-02 recorded); the
  filing read with accession numbers; OCF, SBC, capex, acquisition cash and revenue cross-checked to the FY2026 10-K face and
  FY2017-25 to the earlier faces.
- [x] Owner earnings on the five-year default and on three-year, ten-year, wave and pre-wave windows, both (c) ends and an
  acquisition-inclusive column; the working-capital increment itemized by year and shown not to have reversed; the windows
  that were not built (before FY2017) named with the reason.
- [x] Competitor row filled from three SEC filers' own 10-Ks (FORM, COHU, TER), each re-fetched and each figure found in the
  filer's text; the direct burn-in competitors named and shown to file nothing with the SEC; the class not PROVISIONAL,
  with the directional reason.
- [x] Sovereign for the earnings currency (USD), from the issuing authority, dated 09/18/2026, fetched directly; the cached
  09/17 row from `sources.sovereign()` recorded and not used.
- [x] Value stated as a range under COMPUTATION — NOT A CLEARANCE (no earning-power value; tangible equity about $6 a share).
- [x] One bar (the screamer test); windage count zero, stated.
- [x] Price dated as the 2026-09-18 close, aggregator flagged, the series corroborated by two Form 4 withholding prices
  (2026-09-01 and 2026-09-03) that equal the aggregator's closes.
- [x] Share count from the FY2026 10-K cover with its accession, the latest periodic filing; nothing sold after the cover
  date found; dilution shown beside the cap.
- [x] Deal check run on EDGAR: none live.
- [x] Run committed after Step 0, after Q1-Q2, and after Q3-Q6, each with a pathspec.
- [x] Every ledger id cited was looked up in `principle_ledger.csv` (`led.py`) before it was written.
- [x] No em dashes in anything this session wrote (the template's headings and the required `COMPUTATION — NOT A
  CLEARANCE` heading carry them).
- [x] Never presented as proven to beat the market; nothing here claims it.
- [x] No image files committed; the downloaded 10-K, 10-Q, 8-K, proxy and prospectus texts, the peers' 10-Ks and
  companyfacts, and `companyfacts.json` were left out of every commit.

### THINGS THIS RUN GOT WRONG OR HAD TO CORRECT, on the record
1. **Q2 was committed (`17882a0`) saying the company names no competitor anywhere.** Reading the litigation note for Q3
   found Suzhou Semight Instruments, a Chinese maker of wafer burn-in systems against which Aehr's infringement claims were
   dismissed at first instance in December 2025. Q2 was amended in the Q3-Q6 commit to add it (a named rival, the patents
   *"upholds part of the claims"*, the attacker already in the field); the verdict did not change, and the amendment
   strengthens it. History kept.
2. **Step 0, corrected before its commit:** a stray draft fragment in the D&A reclassification sentence; the August insider
   sale range (first written as $127.50 to $143.77; the parsed Form 4s give $100.70 to $143.77).
3. **Step 0, corrected in the Q1-Q2 commit:** "no 10-K/A in the 1,005-row index" did not say the index begins 2018-08-20;
   EDGAR full-text search finds 10-K/As for FY2005 and FY2008 only, and the sentence now says so.
4. **Q1-Q2, corrected before commit:** the FY2021 customer names were first attributed to the FY2021 10-K (they are quoted
   from the FY2022 10-K); the inventory build was first written as $36.5M (the faces give $29.9M for FY2022-24); a draft
   said the 82% buyer had left the 10% list, which the filings do not show, because the 10-K names no customer after FY2022.
5. **Q4, corrected before commit:** stock sold for cash over ten years was first $144M (the FY2017 private placement of
   $5.3M was missing; $149M); *"SBC exceeded operating cash in every positive year but one"* (two of three); revenue
   without Incal $40M (it is $39M).
6. **Tooling friction, not an error:** re-running the flattener on already-flattened files made `.flat.flat.txt` copies;
   deleted, never committed.

### DEFECTS FOUND IN THE BRIEF I WAS GIVEN
1. **"settle on the 10-K competition section, which names them" (section 3): it names nobody.** No Aehr 10-K FY2019-26 names
   a competitor in its competition section; the only rival named anywhere is Semight, in the litigation note. Advantest,
   Teradyne, FormFactor and Cohu are named in no Aehr filing read; EDGAR full-text search shows FormFactor named Aehr in its
   FY2008-12 10-Ks only, and Cohu and Teradyne never.
2. **"Fiscal year ends on the last Friday of May" (section 1)** is the Friday *nearest* May 31 (52- or 53-week year), and **it
   is changing**: from FY2027 the year ends on the Friday nearest June 30 (board approval 2026-04-02; FY2027 runs 2026-06-27
   to 2027-06-25), leaving a four-week transition period no filing yet covers. `submissions.json` also gives
   `fiscalYearEnd` 1231, which no filing supports.
3. **Tagged D&A "0.31 (FY2022)" (section 2)** is the earliest vintage; the FY2024 10-K face restates FY2022 D&A to $356K.
   The screen's `da_annual` also gives FY2024 $700K against the face's $657K (its source element was not traced).
4. **The memory-sourced beliefs (section 3), settled:** SiC for EVs made FY2022-24 with onsemi the large customer: **held**
   (named at 82% for FY2022; 79% and 67% unnamed for FY2023-24; EV and power 92% at the peak). Incal bought in FY2025,
   package-level: **held** ($22.2M, closed 2024-07-31, $18.6M revenue in its first ten months). FY2024 valuation-allowance
   release: **held** ($21.9M; pretax $12.5M against net income $33.2M). New markets AI, HDD, GaN, silicon photonics:
   **held in the releases and business section**; package-level revenue (Sonoma, Tahoe, Echo) is 37% of FY2026
   revenue and the July 2026 release ties Sonoma orders to a hyperscale AI customer; the rest is forecast and was kept
   outside the circle. Erickson CEO: **held** (since January 2012). ATM
   programmes: **held**, four of them ($25M 2021, $25M 2023, $40M 2024, $60M 2026) plus a 2017 offering. Competitors
   Advantest, Teradyne, FormFactor, Cohu: **not named by Aehr** (defect 1).
5. **The brief did not know** about the December 2024 guidance class action (voluntarily dismissed 2025-05-16), the
   metric switch in FY2025 guidance from "net profit before taxes" to "non-GAAP net profit before taxes", the Semight
   litigation, or the fiscal-year change; each is in the file.

### TOOLING NOTES, recorded and not fixed (no tool may add a number; these would only remove friction)
- **`tools/sources.sovereign()` served the cached 09/17 row** at 20:41 EDT while the Treasury had published 09/18: the
  SNOW, TSLA, RIVN, DJT and BX note, reproduced a sixth time.
- **`sources._chart()` returned `close None` for the day's bar** after the close, as at BX; `regularMarketPrice` with its
  `regularMarketTime` carried the closing print.
- **`submissions.json` `fiscalYearEnd` can be wrong** (1231 for a May filer); any tool that reads it to align years would
  misplace AEHR's.
- **`scale_shift` cannot tell a one-customer capacity build from a business step.** Only the customer-concentration note
  shows that the FY2022 step was 82% one buyer; a screen could read `ConcentrationRiskPercentage1` where tagged; not built.

### ONE THING THE PROJECT SHOULD KEEP FROM THIS RUN
**A consumable is only an annuity if the installed base keeps producing.** Aehr's per-device contactors looked like the
razor-blade half of a franchise; the filed record shows them falling 60% in two years when one customer's end market
slowed. Read the consumable line through a customer's cycle before calling it recurring.

---
## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)**, at Q2. [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** AEHR CLOSES AT Q2 (OUT, ON THE BUSINESS, [E3-03] criterion 2, with [E2-44], [E4-37], [E3-46], [E4-04],
  [E3-51], [E4-23]): the FY2026 10-K says customers *"build their own burn-in systems"* or buy from *"captive or affiliated
  suppliers"* and that competitors are developing *"full-wafer and single-touchdown probe cards"*; it says a price rise to
  recover costs *"could result in a decrease in the competitiveness of our products"* while gross margin fell from 49.1% to
  35.3% (FY2024-26); the only rival it names, Semight, had Aehr's infringement claims dismissed at first instance (December 2025); the
  consumable contactor line fell 60% in two years as EV and power revenue went from 92% to 17%; the largest customer went
  from 82% (onsemi, FY2022) to 26%; on a three-filer row (FORM, COHU, TER) re-read from each 10-K, the subject has the
  steepest margin fall and the only negative five-year owner cash. Q1 IN (systems, per-device contactors and service; the AI
  and HBM forecast revenue outside the circle). Q3 recorded IN on the binary (the guidance class action voluntarily
  dismissed) with four converging flags: guidance missed by 34% (FY2024) and withdrawn (FY2025), serial issuance (2.4 times
  in ten years), non-GAAP net income before stock pay as the headline, and the FY2025 target switched to non-GAAP as results
  fell; pay vests on revenue; insiders sold about $61M in fifteen months. Q4 recorded OUT (gruesome: owner earnings
  five-year FY2022-26 **-$4.8M to -$8.0M** a year, positive only in FY2023; survival bought with $97.4M of FY2026 stock
  sales; proposed shape #20 THE WAVE with #8's feature); price $93.49 x 32,620,450 = $3,049.7M, headed COMPUTATION — NOT A
  CLEARANCE: yield about -0.2% against 5.34% and a ~10% floor, price about fifteen times tangible equity; Q6 records the
  reversal condition in words and arms nothing.
- **The skip reason, as it turned out:** a real organic revenue step (FY2021 $16.6M to FY2022 $50.8M, consecutive years,
  one element), made by one customer's silicon-carbide capacity build (onsemi 82%); not a perimeter change and not a
  restatement.
