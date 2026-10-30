# Company Run — Corcept Therapeutics Incorporated (CORT) — 2026-09-11
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

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## THE SCREEN ROW THAT PROMPTED THIS RUN — a prompt to read, never a score (operator rule 8)

```
cap_m 12386 | oe_bottom_m 90 | oe_top_m 94 | spread 0.051 ($90M to $94M)   <-- 5.1%, the TIGHTEST in the queue
yield_bottom 0.72% | vs_sovereign -4.65 pts | growth_required 9.28%
level_shift 1.24 "no step" | level_shift_oe 0.96 "no step"
level_shift_full n/a (17 years filed) — the FULL series REFUSES: early half straddles zero
window_disagree: FIRES — 9yr and 17yr give different KINDS of answer
best_year_dep 0.058 / best_year_dep_oe 0.057 — no single-year dependence
newest_filing 2025-12-31
```

**The 5.1% width is the first thing this run distrusts, and the queue's own wording for the
shape is the right one: "a tight spread here is arithmetic, not knowledge."** It is rebuilt
over eleven windows and both (c) ends at Q4, and on the two SBC measures the framework
requires **[E5-06, E3-70]**. The result of that rebuild is stated there; the short version is
that the row's two ends are the same number twice, because D&A and capex are both roughly
one-tenth of one percent of revenue in this business, so the (c) band has no width to offer
and the published spread is the *window* spread alone.

---
## STEP 0 — THE RATE, THE COVER, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.37 %** · date **2026-09-10** (the latest published close at the time of this run;
  the Treasury posts the curve after the close, and the 2026-09-11 reading was not yet up) ·
  source **US Treasury daily par yield curve, 30-year, read directly from the Treasury CSV
  (the issuing authority; FRED DGS30 is the fallback and was not used)**. The week's path,
  same source: 5.24 (09-04) · 5.25 (09-08) · 5.28 (09-09) · **5.37 (09-10)** — +13bp on the
  week, not the +9bp the daily fetch of 09-10 carried, because the 09-04 base was 5.24.
- FX: none. Corcept reports in USD and, per the FY2025 10-K, sells its Products only in the
  United States (*"We sell Korlym and a generic version of Korlym in the United States"*).
  Foreign pre-tax income was $3.6M of $66.5M in 2025 (Note 9). The earnings currency is USD.

**THE COVER COUNT, BY HAND.** `python Screens/cover_shares.py CORT`:
```
CORT  CORCEPT THERAPEUTICS INC
   10-Q filed 2026-07-29, period 2026-06-30, accession 0001628280-26-050613
   Common Stock, $0.001 par value                      108,098,397
```
- **ONE class** (Common, $0.001 par; 10.0M preferred authorised, none issued — Note 7, FY2025
  10-K). Cover as-of date **2026-07-22**. No split in the filing history.
- **The count is RISING.** Balance-sheet outstanding: 105,113k (2024-12-31) → 105,966k
  (2025-12-31) → 108,098,397 (2026-07-22 cover), *despite* $172.9M of open-market repurchases
  in 2025. **In H1 2026 there were no repurchases at all** (10-Q cash-flow statement:
  *"Repurchases of common stock in connection with Stock Repurchase Program — | (130,451)"*,
  the second figure being H1 2025), and the count still rose 2.1M in six months on option
  exercises net of withholding. This is the first fact recorded against the company and it is
  dealt with at Q3 under **[E5-08]** and at Q4 under **[E5-06, E3-70]**.
- **price $114.92 · 2026-09-10 close · aggregator (Yahoo Finance chart endpoint via
  `tools/sources.py`), FLAGGED, live quote only** (operator rule 5).
- **MARKET CAP = 108,098,397 × $114.92 = $12,422.7M.** The queue's `cap_m 12386` back-solves
  to $114.58 on the same count — the row is 0.3% stale on price and correct on the count.
  Immaterial; re-struck here as the brief instructed.
- *For the record, from the FY2025 10-K's own risk factor: "During the 52-week period ended
  February 17, 2026 … the intra-day sales prices per share of our common stock on the Nasdaq
  Capital Market ranged from $32.99 to $117.33."* The quote has roughly 3.5x'd inside twelve
  months. Recorded here as a fact about the price, not the business.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary: 10-K FY2025, FYE 2025-12-31, filed 2026-02-24, accession
  `0001628280-26-011091`.**
- **10-Q Q2 2026**, period 2026-06-30, filed 2026-07-29, accession `0001628280-26-050613`;
  10-Q Q1 2026 `0001628280-26-028902`; 10-Q Q3 2025 `0001628280-25-048841`; Q2 2025
  `0001628280-25-037005`; Q1 2025 `0001628280-25-022173`; Q3 2024 (comparative).
- **8-K EX-99.1 earnings releases, read for [E4-29] and [E3-48] — all 37 8-Ks filed since
  2023-01-01 were fetched with their 99.1 exhibits.** The latest is the Q2 2026 release,
  furnished 2026-07-29, accession `0001628280-26-050607`. The regulatory 8-Ks that decide
  this file: CRL for relacorilant in hypercortisolism, `8-K 2025-12-31`; FDA approval of
  Lifyorli (relacorilant) in platinum-resistant ovarian cancer, `8-K 2026-03-25`; NDA
  acceptance with PDUFA dates, `8-K 2025-03-03` and `8-K 2025-09-10`.
- **DEF 14A** filed 2026-04-17, accession `0001628280-26-025735`; also 2025-04-25
  `0001628280-25-019942` and 2024-04-10 `0001628280-24-015633`.
- **Eighteen consecutive 10-K vintages were fetched, FY2008 through FY2025**, because the
  screen's 17-year series refuses the ratio and the run has to decide which years describe
  the business that exists now **[E4-41]**. Accessions: FY2024 `0001628280-25-008167` ·
  FY2023 `0001628280-24-005055` · FY2022 `0001628280-23-005581` · FY2021
  `0001628280-22-002714` · FY2020 `0001628280-21-002861` · FY2019 `0001628280-20-002122` ·
  FY2018 `0001628280-19-001879` · FY2017 `0001564590-18-003840` · FY2016
  `0001564590-17-003493` · FY2015 `0001088856-16-000011` · FY2014 `0001562762-15-000080` ·
  FY2013 `0001193125-14-100313` · FY2012 `0001193125-13-110085` · FY2011
  `0001193125-12-112317` · FY2010 `0001193125-11-067361` · FY2009 `0001193125-10-068719` ·
  FY2008 (period 2008-12-31).
- **Figures cross-checked against the filed statement (Consolidated Statements of Cash
  Flows, 10-K FY2025, page F-7):**

| line | XBRL (`run.py`) | filed statement | agree |
|---|---|---|---|
| Net cash provided by operating activities 2025 | 142.0 | **$141,996** | yes |
| Stock-based compensation 2025 | 84.5 | **$84,500** | yes |
| Depreciation and amortization 2025 | 1.15 | **$1,149** | yes |
| Purchases of property and equipment 2025 | 0.21 | **$(211)** | yes |
| Income taxes paid 2025 | 12.97 | **$12,969** | yes |
| Product revenue, net 2025 (income statement) | 761.41 | **$761,407** | yes |

  Every figure that drives a verdict below ties to the dollar. *(One immaterial discrepancy,
  found by the competitor-row pull: the FY2025 10-K's comparative columns carry 2024 OCF as
  $198,295k and 2023 as $126,681k, where the as-filed FY2024 and FY2023 statements — and the
  XBRL series — carry $198,067k and $127,039k. Reclassifications under $0.4M; the latest
  filed statement is what the grid uses.)* **No tooling defect in the
  tagged series was found for this filer** — a change from the CGNX and QLYS runs, and worth
  saying plainly because the absence was checked, not assumed: the filed cash-flow statement
  carries one D&A line and one capex line, and `run.py`'s D&A and capex both resolve to them.

**What the tagged data could not have told me, and the filing did — the four facts that
shape everything below.** Recorded here so that no later section can pretend to discover
them:
1. **Corcept sold one molecule until 2026-04-01.** FY2025 product revenue of $761.4M is
   *"Korlym and an authorized generic version of Korlym (collectively, our 'Products')"* — 100%
   mifepristone. Lifyorli (relacorilant) began selling on 2026-04-01 and booked $47.6M in its
   first quarter (Q2 2026 10-Q, revenue-by-product table).
2. **The generic has been on the market for two and a half years, and Corcept lost the
   patent case.** *"Teva launched its generic product in January 2024. … On February 19,
   2026, the appellate court affirmed the District Court's ruling, finding no infringement of
   either the '214 or the '800 patent."* (Item 3.) Korlym's composition-of-matter patent
   *"has expired"* (Item 1).
3. **Relacorilant was refused for Cushing's and approved for ovarian cancer, ten weeks
   apart.** CRL 2025-12-30 (*"the FDA stated that additional evidence of efficacy would be
   required for approval"*); NDA resubmitted June 2026 with a PDUFA date of **2026-12-17**;
   Lifyorli approved in platinum-resistant ovarian cancer **March 2026**, ahead of its
   2026-07-11 PDUFA date.
4. **2025 operating income fell 67% on a 60% SG&A increase, and the year's net income
   includes a $33.2M tax BENEFIT on $66.5M of pre-tax income.** Operating income $137.0M →
   $44.8M; SG&A $280.3M → $448.7M; income tax benefit $33.2M *"primarily due to increased
   stock compensation deductions and decreased pretax income."* Cash taxes paid fell $60.3M →
   $13.0M. The [E4-30] tell fires on its face and is read at Q3.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language.** Until 2026-04-01
Corcept sold one pill. Mifepristone, 300 mg, one or more tablets a day, to adults whose
bodies make too much cortisol because of a tumour and who, as a result, have diabetes or
cannot control their blood sugar — the label indication. The molecule is sixty years old
and is the same active ingredient as the abortion pill; Corcept's contribution was to run
the trial that got it approved for this use in 2012 and to hold the orphan exclusivity that
came with it. **That exclusivity ended in February 2019, the composition-of-matter patent
has expired, and the method-of-use patents were held not infringed by Teva's generic in
December 2023, affirmed on appeal 2026-02-19, rehearing denied 2026-07-10.** Since January
2024 a Teva generic of the same tablet has been on sale, and since June 2024 Corcept has sold
its own unbranded copy alongside the brand.

The money is made in three steps, none of which is the tablet. **First, find the patient.**
Most people with hypercortisolism are undiagnosed; Corcept funds screening studies (CATALYST
found hypercortisolism in 23.8% of 1,057 difficult-to-control diabetics; MOMENTUM enrolled
over 1,000 resistant hypertensives) and fields the sales representatives and medical liaisons
who turn those findings into prescriptions. **Second, get it paid for.** *"Confirmation of
coverage by private or government insurance or by a third-party charity is a prerequisite for
selling our Products to a patient."* Corcept staff handle the prior authorisation; where the
insurer will not pay, Corcept's own assistance programme or a charity Corcept funds does, and
*"no patient with hypercortisolism will be denied access to our Products for financial
reasons."* **Third, ship it direct.** Every prescription is dispensed by a single contracted
specialty pharmacy that ships to the patient's home — Optime from 2017, Curant from Q4 2025 —
and the specialty distributor channel is *"less than one percent of our net revenue."* Revenue
is recognised on delivery, net of government rebates (a $84.7M provision on 2025 sales, about
10% of gross), trivial chargebacks, co-pay assistance and returns.

Where the money goes, FY2025, and the shape is the whole story:

| FY2025 | $M | % of revenue |
|---|---|---|
| Net product revenue (100% mifepristone) | 761.4 | 100% |
| Cost of sales | 13.0 | **1.7%** |
| Research and development | 254.9 | **33.5%** |
| Selling, general and administrative | 448.7 | **58.9%** |
| **Operating income** | **44.8** | **5.9%** |
| Interest and other income | 21.7 | |
| Income tax **benefit** | +33.2 | |
| Net income | 99.7 | 13.1% |
| Operating cash flow | 142.0 | 18.6% |
| Stock-based compensation | 84.5 | 11.1% |
| Capital expenditure | **0.2** | 0.03% |
| Depreciation | 1.1 | 0.15% |

**The tablet costs 1.7 cents on the revenue dollar to make and there is nothing to
depreciate.** The other 92.4 cents are people and programmes: 730 employees at year end, a
sales and patient-support apparatus that grew SG&A 60% in one year (*"to support
commercialization of our existing and potential future products"*), and a clinical programme
that spends a third of revenue building the next molecule. This is a business whose entire
cost base is discretionary operating expense, which is why the owner-earnings arithmetic at
Q4 turns not on (c) — there is no (c) to speak of — but on what R&D is *for* **[E4-04]**, and
on stock compensation.

**Is revenue units or price [E2-63]?** Corcept files the decomposition every year, which is
the disclosure a pharma company either makes or does not **[E4-55]**, and it makes it:

| year | net revenue $M | growth | share of growth from **price** | share from **volume** | price action named in the MD&A |
|---|---|---|---|---|---|
| 2017 | 159.2 | +96% | 16.6% | 83.4% | — |
| 2018 | 251.2 | +58% | 14.3% | 85.7% | — |
| 2019 | 306.5 | +22% | **41.6%** | 58.4% | Medicaid mix; statutory govt price; increase 2019-08-01 |
| 2020 | 353.9 | +15% | **68.1%** | 31.9% | increases 2019-08-01 and 2020-01-01 |
| 2021 | 366.0 | +3% | **79.3%** | 20.7% | increase 2021-03-01 |
| 2022 | 401.9 | +10% | *see Q2* | | |
| 2023 | 482.4 | +20% | 42.6% | 57.4% | increase 2023-01-01 |
| 2024 | 675.0 | +40% | 20.6% | 79.4% | increase 2024-01-01 — **the month Teva launched** |
| 2025 | 761.4 | +13% | **price −17.7%** | **volume +37.0%** | AG mix; increase 2025-08-01 |
| H1 2026 (Korlym+AG) | 373.5 | +6% | price −2.1% | volume | AG mix; Aug-2025 increase; better payor rates at Curant |

*(FY2019, FY2020, FY2021, FY2023, FY2024 and FY2025 10-Ks, MD&A "Net Product Revenue"; Q2
2026 10-Q. The 2025 physical figure is also stated in the FY2025 release, 8-K 2026-02-24:
"a 37 percent increase in the number of tablets sold compared to the prior year.")* From
2019 to 2021 most of the growth was price; from 2023 to 2025 most of it was volume, and in
2025 the price went *down* because the company's own generic took share of its own volume.
That series is the Q2 evidence and is adjudicated there.

**The scarce input this business controls.** Not the molecule — that is in the public
domain, generically available, and the patent case is lost. Not manufacturing — *"We rely
on contract manufacturers."* Not distribution infrastructure — one contracted pharmacy.
What Corcept controls is **the funnel from undiagnosed patient to delivered prescription**:
the screening science it paid for, the prescriber relationships its field force built, and the
single dispensing channel through which every Korlym and AG script flows with its
prior-authorisation and co-pay apparatus attached. Recorded here because it decides Q2 and
Q3: **each of the three is the subject of a live legal matter.** The dispensing channel is
what Teva's antitrust complaint and the Aetna/HCSC/Humana/Molina complaint attack; the
prescriber relationships and prior-authorisation practices are what the NJ US Attorney's
Office has been investigating under a records subpoena since **November 2021**; and the
funnel's next stage — relacorilant in the same indication — is what the securities class
action filed 2026-02-20 concerns. The scarce input is real, and it is contested in three
courts.

**Will the fundamentals look broadly the same in ten years?** For the mechanism —
specialty endocrinology, patient found by screening, paid for by prior authorisation, shipped
direct — probably yes. **For the product, no, and the company says so.** By 2036 Korlym will
be a twenty-four-year-old generic molecule, and the filing's own plan is that revenue will
come from relacorilant (approved in ovarian cancer March 2026; refused in Cushing's December
2025; resubmitted, decision due 2026-12-17), miricorilant (MASH, Phase 2b), dazucorilant
(ALS, Phase 3 planned) and nenocorilant (oncology, Phase 1b). **[E3-31]**'s constant-change
clause — *"If a business is complex or subject to constant change, we're not smart enough to
predict future cash flows"* — is live for a company whose stated strategy is to replace its
only product, and it is recorded here and decided at Q2 under **[E4-04]**, exactly as the
QLYS and CGNX runs carried the same clause.

**[E4-46] check** — *"if we can't make a decision in five minutes, we can't make it in five
months."* One product, one segment, one country, one share class, no debt, no acquisitions,
no goodwill, no float, no percentage-of-completion, no capitalised development, a
three-line cost structure. The business took five minutes. Whatever closes this file, it will
not be that the business is unintelligible.

- **VERDICT: [x] IN** — *on understanding. Recorded and carried forward, not waived: the
  generic, the contested channel, and the replacement-molecule strategy, all decided at Q2.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**MY PRIOR, AND THE BRIEF'S, WRITTEN BEFORE THE EVIDENCE SO IT CAN BE READ AGAINST ME
[E4-26]:** OUT, on the generic. **The prior survives, but not for the reason the brief gave,
and two of its factual premises were wrong.** The brief expected the generic to have taken
Korlym's volume; it has not — tablets sold rose 37% in the generic's second year. The brief
expected relacorilant's status to be one of approved, under review or refused; it is all
three at once, in two indications. What fails this gate is not the generic's *effect* but what
Corcept had to do to hold the volume against it, and what the R&D that is a third of revenue
is *for*.

### THE GENERIC — established from the filings, as the brief asked

| date | event | source |
|---|---|---|
| Feb 2012 | Korlym approved; orphan exclusivity to **Feb 2019** | FY2024 10-K |
| Feb 2018 | Teva Paragraph IV notice; Corcept sues (D.N.J.) | Item 3, every vintage since |
| Aug 2020 | **FDA final approval of Teva's ANDA** | Item 3 |
| Nov 2020 | PTAB upholds the '214 patent; Fed. Cir. affirms | Item 3 |
| Dec 29, 2023 | District court: Teva's product **does not infringe** '214 or '800 | Item 3 |
| **Jan 2024** | **Teva launches** | Item 3, FY2023 and later |
| Jan 1, 2024 | **Corcept raises Korlym's price** | FY2024 10-K MD&A |
| **Jun 2024** | **Corcept launches its own authorized generic** | Item 1 |
| Jun 13, 2024 | **Teva sues Corcept and Optime for antitrust** (N.D. Cal.) | Item 3 |
| Feb 10, 2025 | **Aetna, HCSC, Humana, Molina sue Corcept**, "substantially similar" allegations | Item 3 |
| Aug 2025 | Corcept raises price again | FY2025 10-K MD&A |
| Feb 19, 2026 | **Fed. Cir. affirms non-infringement**; en banc denied Jul 10, 2026 | Q2 2026 10-Q |
| May 5, 2026 | Antitrust motions partly denied, *"allowing the case to proceed"*; **trial March 2027** | Q2 2026 10-Q |

**At what price did the generic launch?** Not filed by either party. **What has it done to
Korlym's volume?** Corcept's own tablets sold rose **37.0% in 2025** and volume rose in every
quarter since (Q3 2025 +42.5%, Q1 2026 +12.4%, Q2 2026 "76.1 percent of the increase"). **What
has it done to Korlym's price?** Average realised price fell **17.7% in 2025** (20.2% in Q3
2025, 6.7% in Q1 2026, 2.1% in H1 2026), and the filing gives one cause every time: *"due to
higher sales volume from our authorized generic version of Korlym."* **The generic did not
take the volume. It took eighteen points of price, through Corcept's own unbranded copy.** And
the mechanism by which Teva's copy was kept off the scripts — an exclusive specialty pharmacy
that dispensed only Corcept's brand and Corcept's generic — is the thing Teva and four
national payors say is illegal, with a trial date.

### [E3-03] — the three criteria, against the company's own words

**(1) Needed or desired — YES.** Hypercortisolism *"can be lethal if not treated"*; surgery
fails in half of patients. Nothing in the file argues otherwise.

**(2) "Thought by its customers to have no close substitute" — NO, and it fails three ways on
the filer's own disclosure.** First, **a chemically identical tablet has been on sale for two
and a half years**, approved by the FDA as therapeutically equivalent, and Corcept sells one
itself. There is no closer substitute than the same molecule. Second, the FY2025 competition
section names **six** alternatives: *"Signifor® (pasireotide) … Isturisa® (osilodrostat) and
Recorlev® … drugs used 'off-label,' such as ketoconazole … and metyrapone … Since January
2024, our Products also compete with a generic version of Korlym sold by Teva."* Third, the
risk factor that governs: *"The availability of generic Korlym could cause our revenue to
decline … by reducing the number of tablets we sell or lowering their price or both."* The
filed outcome, two years on, is the second of the two: price.

**(3) "Not subject to price regulation" — PARTLY FAILS, and the company says the regulation
will bite from 2026.** Medicaid *"reimburses Korlym at a significantly lower price"*
(statutory rebates; the 2025 government-rebate provision was $84.7M, about a tenth of gross).
The IRA caps Medicare price increases at inflation and, from 2025, imposes manufacturer
liability in Part D; the FY2025 10-K: *"We anticipate this provision will limit the revenue we
receive from Medicare patients and may materially reduce our profits in 2026 and beyond."*
**[E2-59]** governs — regulation *caps* a franchise — and here the cap is filed as material.

### [E2-44] — the two-characteristic test SPLITS, and the split is the whole company

**Half two — grow dollar volume "with only minor additional investment of capital"? YES, as
emphatically as any name in this queue.** Capex $211k on $761M of revenue; net PP&E $1.9M;
inventory $24M; receivables $60M; operating capital employed is negative once the $532M of
cash and $168M deferred tax asset are removed from an $837M balance sheet. Revenue doubled
2021-2025 on no capital at all.

**Half one — raise prices "even when product demand is flat and capacity is not fully
utilized" without loss of volume? The filed series says the opposite, and it says it in the
exact year the test specifies.** The decomposition Corcept files every year:

| year | share of revenue growth from price | share from volume | list-price action |
|---|---|---|---|
| 2019 | 41.6% | 58.4% | +Aug 2019 |
| 2020 | 68.1% | 31.9% | +Jan 2020 |
| 2021 | **79.3%** | 20.7% | +Mar 2021 |
| 2022 | 45.4% | 54.6% | +Jan 2022 |
| 2023 | 42.6% | 57.4% | +Jan 2023 |
| 2024 | 20.6% | 79.4% | +Jan 2024 |
| **2025** | **price −17.7%** | **volume +37.0%** | +Aug 2025, *and* the AG |
| Q1 2026 | price −6.7% | volume +12.4% | |
| H1 2026 | price −2.1% | volume (rest) | |

From 2019 to 2023 Corcept was the [E3-33] business — a monopoly on a lethal disease taking a
list-price increase every year, with price supplying 42% to 79% of each year's growth. **The
moment the substitute arrived, realised price fell by a fifth and has kept falling.** That is
half one failing in the corpus's own terms: the price could be raised only while there was
*"no close substitute"* **[E3-03]**, and **[E5-28]**'s scope rule — pricing power of that kind
*"is a monopoly or a near monopoly"* — reads the series exactly: the pricing power was the
orphan exclusivity and the patents, both now gone. **[E4-37]**'s inverse metric cuts both ways
and both are recorded: Corcept raised the *brand's* list price in the very month Teva launched
and again nineteen months later — no prayer session — and the *realised* price fell 18%
anyway, because the customer took the unbranded tablet. The list price is what management
controls; the realised price is what the customer decides, and the customer decided.

### [E4-04] — must the moat be REBUILT, or merely DEFENDED? This is where the file turns.

*The test: does a lapse in spending destroy the structure, or merely narrow it — and does the
spending defend the same advantage, or buy its replacement?*

**The brief asked the corpus to be checked for patent expiry, and the sweep is recorded:** all
268 rows of `principle_ledger.csv` searched for *patent*, *generic*, *pharmaceutical*, *drug*,
*FDA*. Three rows match — **[E2-27]** (textile capex), **[E5-11]** (staying power) and
**[E2-70]**, which names patents only as an advantage insurers *lack*. **No instance found of
the corpus addressing pharmaceutical patent expiry directly.** The applicable doctrine is
therefore [E4-04]'s own scope statement — what "enduring" excludes is *"the moat whose basis
must be periodically replaced — rapid-change industries, depleting assets"* — and
**[E3-51]**'s competitive destruction. A drug's exclusivity is a depleting asset with a
statutory date on it, and this file has watched it deplete: orphan exclusivity to 2019,
composition patent expired, method patents held not infringed, generic on sale.

**Corcept's two spending lines answer the test separately, and both fail it.**

- **R&D — $254.9M, 33.5% of revenue — buys the replacement.** The FY2025 development table
  allocates **$93.1M to Cushing's syndrome**, and that programme is relacorilant: the same
  indication, the same prescribers, the same channel, a new molecule with composition patents
  to 2040 and a fresh seven-year orphan term *"provided we obtain approval."* That is Mitsui's
  Rhodes Ridge, not Coca-Cola's advertising: money spent to buy the next deposit because the
  current one is running out. It does not defend Korlym; nothing can. And the successor
  **was refused** on 2025-12-30 (*"additional evidence of efficacy would be required"*),
  is resubmitted, and is due a decision on 2026-12-17.
- **SG&A — $448.7M, 58.9% of revenue, up 60% in a year — buys each year's patients.** The
  filing's own sentence: *"increased sales and marketing activities and employee compensation
  expenses to support commercialization of our existing and potential future products."* The
  funnel described at Q1 has to be run every day; a lapse does not narrow it, it hands the
  scripts to the pharmacy's generic. And the funnel's generic-blocking function is on trial in
  March 2027.

**Where the moat would have to live for IN, stated fairly [E4-51]:** in the funnel itself —
the screening science Corcept paid for, the prescriber base, the patient-support apparatus —
as a durable structure into which any molecule can be placed. If that were the moat, R&D would
be buying a new tenant for a building Corcept owns, and the building would be the Coke
trademark. **The filed numbers refuse that reading.** A building does not cost 59% of the rent
to keep standing; operating margin has fallen in **every one of the last six years** — 36.4%
(2019) → 36.2% → 34.0% → 28.0% → 22.2% → 20.3% → **5.9% (2025)** → **(2.0)% in H1 2026** —
while revenue rose 2.5x. **[E4-32]** — direction outranks existence — reads that series one
way. And the corpus's test for a franchise is what happens to the *price* under attack
**[E3-43]**: *"a company's ability to regularly price its product or service aggressively"*;
the price fell.

### THE COMPETITOR ROW — REQUIRED **[E3-28]**

*Full working with accession numbers, URLs and verbatim quotes:
`Test Runs/_research 2026-09-11 CORT/COMPETITOR_ROW.md`.* **Peers named: 3 of the 3 branded
same-indication competitors Corcept itself names (Recordati's Isturisa and Signifor; Xeris's
Recorlev), plus Teva.** Of these, **only Xeris files with the SEC**; Recordati is a Borsa
Italiana registrant read at the company-IR-site rung; Teva files with the SEC but reports no
product line for generic mifepristone. **The row is therefore partly PROVISIONAL, and that is
stated. It does not carry the verdict: the verdict rests on Corcept's own filed price series,
its own development table and its own competition section, and the row corroborates.** *(The
verdict below was written before the peer pull completed, because it does not depend on it;
the row was inserted afterwards and it corroborates, and adds one fact.)*

| same-indication product (Cushing's) | FY2023 | FY2024 | FY2025 | H1 2026 | FY2025 growth | source |
|---|---|---|---|---|---|---|
| **Korlym + AG (CORT)** | $482.4M | $675.0M | **$761.4M** | $373.5M | **+12.8%** | 10-K `0001628280-26-011091`; 10-Q `0001628280-26-050613` |
| Recorlev (Xeris, XERS) | $29.5M | $64.3M | **$139.3M** | $106.5M | **+117%** | 10-Ks `0001867096-24-000031` / `-25-000039` / `-26-000016`; 10-Q `-26-000065` |
| Isturisa (Recordati) | €139.5M | €203.6M | **€262.8M** | €178.8M | **+29%** | recordati.com results releases — non-SEC, **euro**, company-IR-site rung |
| Signifor / Signifor LAR (Recordati) | €102.9M | €118.0M | €131.3M | €68.8M | +11% | same |
| Teva generic mifepristone | — | — | — | — | — | **no revenue instance found**, 10-Ks `0001193125-25-020826` and `0001193125-26-034532` |

Company level, CORT against the one SEC-filing peer, FY2025: gross margin **98.3%** vs 85.4%;
GAAP operating margin **5.9%** vs 8.5%; OCF $142.0M vs $28.6M; SBC ÷ OCF 59.5% vs 78.1%;
cash $532M and **no debt** vs $111M against $220M of term debt at 11.4% effective; shares
outstanding +0.8% vs +11.2%. Xeris names *"Korlym"*, *"Corcept"*, the Teva generic and
relacorilant in every 10-K in the window.

**Four things the row adds, all corroborating:**
1. **The incumbent is the slowest-growing branded product in its own indication** — +12.8%
   against +29% (Isturisa) and +117% (Recorlev) — and both challengers name Korlym in their
   own filings. That is criterion (2) read from the substitutes' side.
2. **Isturisa's US label was widened from Cushing's disease to Cushing's syndrome on
   2025-04-15** — onto Korlym's ground — and Recordati's US net active patients went from
   *"over 1,000"* to *"approximately 1,400"* during 2025.
3. **Teva's own launch table locates the moat.** Both Teva 10-Ks carry the row *"Mifepristone
   Tablets | Korlym | January | $2"* under *"Total Annual U.S. Branded Sales at Time of Launch
   (U.S. $ in millions (IQVIA))"*. **IQVIA saw $2M of Korlym sales; Corcept reported ~$480M.**
   The 240x gap is the exclusive specialty pharmacy that IQVIA cannot see — the attacker's
   filing says, in a number, that the moat is the channel and not the molecule. The channel is
   what is on trial.
4. **Neither branded product held price in 2025.** Xeris reports Recorlev's net price down
   7.2%; Corcept's realised price fell 17.7%. **[E2-58]**'s equation — over-capacity without
   administered prices — has begun to describe an orphan indication with three branded
   products and a generic.

*Limit of the row, in addition to [E3-61]:* Korlym's patient share, Teva's volume and Korlym's
realised net price after the AG are invisible from the competitors' side; Recordati is a
revenue-only column in euro; AbbVie's Elahere ($690M in FY2025, FRα-gated) is a ceiling
reference for Lifyorli's market, not a peer.

**The row's limit, stated [E3-61].** The row can show that Corcept's realised price fell
while its volume rose, and that its branded competitors are small; it cannot show what
share of the 37% tablet growth Teva also captured, because **Teva does not file it and
Corcept does not file the brand/AG split**. The unit series the framework wants **[E4-55]** is
filed as a growth percentage for one year and as adjectives (*"a record number of new
prescriptions"*) in every quarter; **no level series of tablets, patients or prescribers has
been filed in any vintage read** (recorded sweep, 18 10-Ks and 37 8-Ks).

### THE REMAINING Q2 TESTS, run and recorded

- **[E3-33] / [E5-28] untapped pricing power — NO; the class existed 2019-2023 and was
  exhausted by the generic.** Claiming it now means claiming near-monopoly against an
  identical tablet on sale from Teva.
- **[E2-53] the dominance class — NO.** Korlym's economics have been set by a district judge
  (Dec 2023), an appellate panel (Feb 2026), the FDA (Dec 2025) and a pharmacy contract
  (2025), not by the company.
- **[E3-46] the number — high on capital, collapsing on margin.** Operating income on
  negative operating capital is a ratio this run declines to print; operating margin 5.9%.
- **[E2-45] the attacker's test — already answered by the attacker.** Teva took the cheapest
  possible route (an ANDA on a sixty-year-old molecule), won in court, and is now attacking
  the channel. The company's response was to become its own generic.
- **[E4-36] which cause of extreme success?** A **surfing run [E3-51]** on a statutory
  exclusivity, then a second wave — the screening surge the company itself generated with
  CATALYST — and the wave is real: 37% tablet growth. *"The advantage lives in the wave, not
  the surfer."*
- **[E4-23] key-person — recorded here, not at Q3.** Dr Belanoff has been CEO since founding
  and is the CODM; the proxy says the 25.8M options *"are primarily held by our executive
  management, with an average holding period of seven years."* No defect scored; the funnel is
  institutional.

### THE Q2 VERDICT

- Needed or desired **[x]** · no close substitute **[ ] FAILS** · not price-regulated
  **[ ] PARTLY FAILS, filed as material from 2026**
- Must the moat be continuously rebuilt? **YES — R&D buys the replacement molecule, SG&A buys
  each year's patients, and the exclusivity the price was built on has already expired
  [E4-04].**
- Primary moat metric: **realised price under generic competition — down 17.7% in 2025 and
  still falling; operating margin down six consecutive years to 5.9%.**
- Class: **NONE for Korlym; PROVISIONAL-on-paper for Lifyorli (one quarter of sales).** ·
  Direction: **narrowing on price and margin; widening on units.**
- **VERDICT: [x] OUT — on [E3-03] criterion (2), on [E2-44] half one, and on [E4-04]'s
  replacement test; criterion (3) and [E4-32] corroborating.**

**THE CASE FOR IN, STATED AS WELL AS I CAN STATE IT [E4-51], because a holder should accept it
as fair.**

> Corcept met the generic head-on and **grew tablets 37% in its second year on the market**,
> which almost no branded drug has ever done; the proxy says so in one line — *"despite the
> presence of generic alternatives."* It did that by selling its own generic, keeping the
> patient, and raising the brand's price twice. It has no debt, $545M of cash, a business that
> needs no capital, a diagnosis funnel it built with its own science that is still widening
> (record new prescriptions every quarter), and a successor molecule with composition patents
> to 2040 that is **already approved and selling in oncology** — $47.6M in its first quarter,
> 1,300 patients started, an NCCN preferred regimen — and that in Cushing's would remove
> Korlym's worst side effect (44% hypokalemia) with a fresh seven-year orphan term. The 2025
> margin collapse is launch spending, disclosed as such, and H1 2026 already shows Q2
> operating margin back at 16%. If the funnel is the asset, this is a franchise between
> tenants.

**Why it still does not carry the gate, and each reason is a filed fact:**

1. **The price fell.** [E3-03] and [E3-43] make the franchise test a price test, and the one
   thing a franchise does under attack is hold price. Realised price is down 18% and the
   company attributes it, every quarter, to its own generic.
2. **The substitute is the same molecule, and the company sells it.** Criterion (2) cannot be
   read any other way.
3. **The funnel's generic-blocking mechanism is on trial, and four payors have joined.** A
   moat whose operation is the subject of *Teva v. Corcept* (trial March 2027) and *Aetna et
   al. v. Corcept* is not one whose existence this run can grade IN; if the plaintiffs are
   right, the 37% is the *evidence* against the company.
4. **[E4-04] excludes a moat whose basis must be replaced, and this one has been replaced
   once (exclusivity → patents), lost, and is being replaced again (Korlym → relacorilant) at
   a third of revenue, with the replacement refused once already.**
5. **The successor's own moat is not yet in the numbers.** Lifyorli has one quarter of
   sales and no earnings; relacorilant in Cushing's has a December decision date. The
   framework values what exists **[E5-34]**: *"If … we lack the ability to estimate future
   earnings — which is usually the case — we simply move on."*

**WHAT WOULD FLIP THIS VERDICT, NAMED IN ADVANCE SO IT IS FALSIFIABLE.** Any one of:
**(a)** realised average price for the hypercortisolism products filed as *rising* for four
consecutive quarters with the AG mix stable — half one of [E2-44] becoming answerable;
**(b)** relacorilant **approved in Cushing's** (decision due 2026-12-17) *and* two full years
of filed relacorilant revenue in that indication, so that the successor's franchise can be
evidenced rather than assumed — this is the [E4-04] rebuilt-moat test run on the replacement,
and it is a document I can name; **(c)** the Teva antitrust and Aetna matters resolved without
a finding or settlement that changes the dispensing arrangement, so that the funnel's
generic-blocking function is lawful on the record; or **(d)** a filed unit series (tablets,
patients on therapy, or brand/AG split) making [E4-55] runnable. **Each is a document I can
name, which is why this is OUT and not UNRESEARCHED: every document that exists has been
read, and they answer the question as it stands today.**

**Q2 CLOSES THE FILE. Everything below this line is recorded because the operator's brief
asked for it and because a closed file still owes the register its findings. None of it is a
verdict, and per operator rule 2 none of it can promote the name.**

## Q3 ITEMS — RECORDED, NOT A VERDICT. **[E2-01, E2-26, E2-49, E2-57, E3-48, E4-22, E4-29, E4-30, E4-31, E5-08, E5-15, E5-30]**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE, DECLARED.**
- **Daily execution [E3-38, E2-70] — [x] TICKED.** The product is a promise renewed daily:
  find the patient, win the authorisation, ship the tablet, keep the patient on therapy
  through 44% hypokalemia. The FY2025 revenue miss was caused by the company's own single
  vendor being *"unable to fully meet demand"* — one operational failure at one contractor
  cost the guidance. **Q3 is a BINARY GATE for this business, and no price compensates
  [E1-16, E3-29, E5-35].**
- Control **[ ]** — not ticked; marketable minority position.
- Leverage **[ ]** — not ticked; **no debt of any kind.**

**HONESTY BINARY [E5-16] — RECORDED SWEEP: no adjudicated misconduct; THREE OPEN MATTERS,
each dated to when it became public.**
1. **NJ US Attorney's Office records subpoena, public November 2021, STILL OPEN** — *"seeking
   information relating to the sale and promotion of Korlym, our relationships with and
   payments to health care professionals who can prescribe or recommend Korlym and prior
   authorizations and reimbursement for Korlym. The NJ USAO has informed us that it is
   investigating whether any criminal or civil violations by us occurred."* Four years and
   ten months without resolution, and its subject is the funnel that Q1 named as the scarce
   input.
2. **Teva antitrust (public 2024-06-13) and Aetna/HCSC/Humana/Molina (public 2025-02-10)** —
   the exclusive-pharmacy arrangement; motions partly denied 2026-05-05; **trial March
   2027**. Not an integrity finding; a prompt to read, and read at Q2.
3. **Securities class action, public 2026-02-20**, class period 2024-10-31 to 2025-12-30,
   concerning statements about the relacorilant NDA. The statements are on the record: 8-K
   2025-11-04, eight weeks before the CRL — *"We believe both deadlines will be met."*
Closed: the Melucci securities action (2019-2024; $14.0M settlement, insurer-reimbursed in
full); the Williams/Jeweltex and Ritchie derivative suits (dismissed 2025). **Under [E5-17]
this is the absence of found disqualifiers, not a finding that the managers are honest**, and
under **[E5-22]** the size of any eventual penalty is not the measure; *"they didn't act when
they learned"* is. Auditor **Ernst & Young LLP since 2001**, with a critical audit matter on
government rebates.

**STEP 2 — THE FLAGS. Each a prompt to READ [E5-36, E5-38].**
- **weak accounting [ ]** — does not fire. Options expensed since the tables begin; no
  pension; the rebate reserve is rolled forward in full every year. No restatement in any
  vintage read.
- **unintelligible footnotes [ ]** — does not fire. The notes are short and plain; the CRL is
  stated in one sentence.
- **trumpeted earnings projections / growth targets [x] FIRES — see [E3-48] below.**
- **serial share issuance [x] FIRES, in the form the corpus did not anticipate: issuance
  hidden behind buybacks [E5-15].** Cover count: 112.9M (Feb 2016) → 108.1M (Jul 2026), **−4.3%
  in ten years, after $966.6M of treasury stock at cost** (36.55M shares bought, including
  a $145.4M tender at $22.00 in 2023 and $172.9M at $66.71 in 2025). The proxy states the
  overhang itself: **25.8M options outstanding, 2.2M restricted shares, 3.9M available and
  8.0M newly requested — "total basic dilution of 38.4 percent"** — and *"we purchased
  approximately 56 percent of the shares issued in connection with option exercises."*
  Shareholders noticed: the plan amendment passed **53.2M for / 23.9M against (31% opposed)**
  on 2026-05-28, against 94% for say-on-pay.
- **EBITDA / adjusted-earnings promotion [ ] DOES NOT FIRE [E4-29].** Recorded sweep of
  **all 37 8-Ks filed since 2023-01-01, with exhibits**, for *non-GAAP*, *EBITDA*, *adjusted
  net income / EPS / operating*: **zero hits.** Every release leads on GAAP revenue, GAAP net
  income and cash. This is the CGNX lesson run and passed: the flag was checked in the
  furnished releases, not the 10-K, and it is clean.
- **filed-figure tells [E4-30]** — *smoothness:* does not fire (operating income 137 → 45;
  net income 141 → 100). *Cash tax % of pre-tax:*

| FY | pre-tax income | cash taxes paid | cash tax % |
|---|---|---|---|
| 2021 | $125.0M | $9.1M | 7.3% |
| 2022 | $116.2M | $39.8M | 34.2% |
| 2023 | $124.6M | $47.6M | 38.2% |
| 2024 | $161.5M | $60.3M | 37.3% |
| **2025** | **$66.5M** | **$13.0M** | **19.5%** |

  **Fires as a prompt; reading resolves it into two named, dated causes, one of which is a
  Q4 finding.** (i) OBBBA, enacted 2025-07-04: *"our election to expense domestic research
  costs for tax purposes starting in 2025"* generated a **$397.8M federal NOL in one year**.
  (ii) *"increased stock compensation deductions"* — the rate reconciliation shows a
  **$41.1M tax effect from stock-based compensation (61.9 points of the rate)**, which at 21%
  is roughly **$196M of deductions**, and the equity note supplies the source: *"The total
  intrinsic value of options exercised during the year ended December 31, 2025 … was
  $227.5 million."* **Employees realised $227.5M from options in 2025 against an $84.5M
  accounting charge.** That is not a fraud tell; it is the [E3-70] measure showing up in the
  tax line, and it is carried to Q4.

**[E3-48] THE PROJECTIONS FLAG — FIRES, AND THE RECORD IS THE ONE THE CORPUS ASKS FOR.**
*"demand the record of the people who made the projections."* Corcept guides revenue every
quarter; the full series from the furnished releases:

| year | first guidance | last guidance | actual | outturn vs first midpoint |
|---|---|---|---|---|
| 2023 | $430–450M (Feb) | $470–480M (Nov) | **$482.4M** | +9.6% |
| 2024 | $600–630M (Jan) | $675–700M (Oct) | **$675.0M** | +9.8%; bottom of the final range |
| **2025** | **$900–950M (Feb)** | **$800–850M (Nov, after $850–900M in Jul)** | **$761.4M** | **−17.7%; $38.6M BELOW the bottom of the twice-cut range** |
| 2026 | $900–1,000M (Feb) | $1,100–1,200M (Jul) | — | — |

Two years of sandbagged beats, then a miss of every range published, attributed to the
vendor. **[E2-57] fires on the attribution:** *"We should have achieved higher growth but were
not able to fully meet demand because of capacity constraints at our previous specialty
pharmacy vendor"* — the vendor Corcept chose, alone, in 2017. *"The real mistake is not the
act, but the actor."* **[E2-49] fires mildly on the yardstick:** the first-ever filed unit
figure (*"37 percent increase in the number of tablets sold"*) appears in the release for the
year revenue missed — a favourable yardstick introduced as the standing one deteriorated.
**And the regulatory projections:** *"We believe both deadlines will be met"* (2025-11-04) →
CRL (2025-12-30) → *"confident that the ultimate outcome will be approval"* (2026-02-24). One
of the two was met, early. **[E5-30]**: a guidance culture is a ratchet, and this one has run
since at least 2023.

**[E4-52] — do the flags converge?** Three fire toward one thing — guidance, dilution behind
buybacks, an except-for — and they point at **a management paid in options, guiding the
stock, and re-buying its own issuance.** That is a confluence and it is read as one system.
What it is not is the CRWD lollapalooza: GAAP is complete, no non-GAAP exists, the price
series is filed every year, and nothing has been restated.

**STEP 3 — THE PRIMARY TEST [E2-01].** Net income on average equity:

| FY | net income | avg equity | ROE | operating margin |
|---|---|---|---|---|
| 2019 | $94.2M | $323.6M | 29.1% | 36.4% |
| 2020 | $106.0M | $447.3M | 23.7% | 36.2% |
| 2021 | $112.5M | $449.6M | 25.0% | 34.0% |
| 2022 | $101.4M | $438.8M | 23.1% | 28.0% |
| 2023 | $106.1M | $504.3M | 21.0% | 22.2% |
| 2024 | $141.2M | $593.2M | 23.8% | 20.3% |
| **2025** | **$99.7M** | **$663.7M** | **15.0%** *(≈10% before the $33.2M tax benefit)* | **5.9%** |

ROE is flattered by $966.6M of treasury stock inside equity and by a $168.2M deferred tax
asset; operating capital employed is **negative** (assets $836.7M less cash and securities
$532.4M less DTA $168.2M = $136.1M, against $188.8M of liabilities), so **[E3-46]**'s number
is *"very high"* on capital and falling fast on margin. Both are true.

**THE HALF-OWNER TEST [E2-26] — MIXED, AND THE POSITIVE HALF IS RARE.** Corcept files, every
year, the split of revenue growth between price and volume, an R&D table by programme, and a
full rebate-reserve rollforward — three disclosures most pharma filers omit, and the first of
them produced the sharpest finding *against* the company at Q2. Against that: **no brand/AG
split, no patient count, no unit level, no Teva share**, and the guidance record above.

**THE INSTITUTIONAL IMPERATIVE [E2-30].** *Not a fraud test.*
- **[ ] resists change** — no; the company is replacing its product.
- **[x] projects materialise to soak up funds** — fires as a prompt: nine named trials across
  five indications (BELLA A/B/C, STELLA, TRIDENT, SYNERGY, MONARCH, DAZALS Phase 3, MOMENTUM)
  on $44.8M of operating income; R&D guided *"higher in 2026."*
- **[ ] staff studies** — no instance found.
- **[ ] peer imitation** — no.

**CAPITAL ALLOCATION — THE BUYBACK, ALL THREE CONDITIONS [E5-08, E4-31, E5-24].**

| period | cash | shares | price |
|---|---|---|---|
| 2018 / 2019 / 2020 open market | $23.7M / $31.0M / $10.0M | — | — |
| **Dec 2021 tender** | **$207.5M** | **10.0M** | **$20.75** |
| Apr 2023 tender | $145.4M | 6.6M | **$22.00** |
| 2024 | $15.7M | — | — |
| 2025 (mostly H1) | $172.9M | 2.6M | **$66.71** |
| H1 2026 | **$0** | — | (price $60–115) |
| net-exercise withholding purchases 2023 / 2024 / 2025 / H1 2026 | $9.1M / $22.3M / $72.9M / $17.2M | | at market |

- **(1) ample funds — YES.** $544.6M cash and securities, no debt, API commitment $10.7M,
  leases $7.4M.
- **(2) material discount to conservatively calculated IV — FAILS on this run's range.** The
  computation at Q5 puts the floor-based value at roughly **$6 to $37 a share** across every
  base and growth case up to 30%; the 2025 purchases were struck at $66.71. The 2023 tender
  at $22.00 is the closest to defensible and is inside the range only at 15%+ growth.
  **CAPITAL-ALLOCATION FLAG, with the humility clause [E4-13]:** this rests on my range; they
  know the business better. And **[E5-24]** cuts the other way and is credited: **they stopped
  buying entirely in H1 2026** as the price ran from $60 to $115. *What is smart at one price
  is dumb at another* — the refusal is the rational half of the record.
- **(3) the register supplied all the information needed to estimate value [E4-31] — FAILS.**
  A buyback executed while the register is not told the brand/AG split, the patient count, or
  Teva's share, and while the leading indicator the company itself uses (tablets) is filed
  once, does not meet the earliest statement of the rule.
- **And the buybacks did not reduce the count.** 36.55M shares bought since 2018; the cover
  count is down 4.8M. The buyback is a settlement mechanism for option exercises, and the
  proxy says so: *"we purchased approximately 56 percent of the shares issued in connection
  with option exercises."*

**THE GUARDRAIL.** [x] Nothing here promotes the name. [x] Key-person recorded at Q2. [x] No
manager-as-plan case is made; the file is closed at Q2.

- **Q3, had it been reached: IN (no disqualifier found) with three flags and an open
  federal investigation — recorded, not a verdict.** *"Sincerity and empathy can easily be
  faked" [E5-17].*

## Q4 ITEMS — RECORDED, NOT A VERDICT. **[E2-23, E3-44, E3-70, E4-25, E4-41, E4-20, E5-11, E3-24]**

### Owner earnings — the one number, rebuilt as the brief instructed
*Script and output: `Test Runs/_research 2026-09-11 CORT/owner_earnings_grid.py` and
`OWNER_EARNINGS_OUTPUT.txt`. Every input is a filed cash-flow line (18 vintages) or a filed
grant table.*

**THE PUBLISHED 5.1% WIDTH IS THE FIFTEENTH CONSECUTIVE UNDERSTATEMENT, AND THIS ONE HAS A
SPECIFIC CAUSE.** `oe_bottom 90 / oe_top 94` are the 3-year and 5-year means of (OCF − SBC
charge − (c)), and since D&A and capex are both about $1M a year, the (c) band has **no
width**: the row's two ends are one SBC measure across two windows. The framework requires
two more dimensions the row cannot see — **[E3-70]**'s market-value SBC measure and **[E4-41]**'s
decision about which years describe the business — and both are where the width is.

| window | years | OE, SBC at the **charge** | OE, SBC at **grant-date value [E3-70]** | yield (charge) |
|---|---|---|---|---|
| 3-yr | 2023–25 | $89.3M | **$44.8M** | 0.72% |
| 5-yr | 2021–25 | $93.8M | $58.5M | 0.75% |
| 7-yr | 2019–25 | $98.8M | n/a | 0.80% |
| 10-yr | 2016–25 | $84.2M | n/a | 0.68% |
| 17-yr | 2009–25 | $38.1M | n/a | 0.31% |
| **generic era only, 2024–25** | | **$95.6M** | **$33.9M** | |
| **TTM to 2026-06-30** | | **$10.6M** | | **0.09%** |
| **H1 2026 alone** | | **−$38.4M** | | |

*(Conservative (c) end throughout — the larger of D&A and capex — and the generous end is
within $1M of it in every window: $89.3M vs $90.3M at 3 years.)*

**Owner earnings by year, charge basis, conservative (c) ($M):** 2016 11.1 · 2017 47.2 · 2018
91.6 · 2019 105.7 · 2020 117.2 · 2021 123.9 · 2022 77.1 · 2023 76.7 · 2024 134.8 · **2025
56.4** · H1 2026 **−38.4**. On the grant-date SBC measure: 2020 111.3 · 2021 84.6 · 2022 73.7
· 2023 66.4 · 2024 111.6 · **2025 −43.7**.

**WHICH YEARS DESCRIBE THE BUSINESS THAT EXISTS NOW [E4-41] — decided, stated, justified.**
The 17-year series refuses the ratio because **2009–2015 are a development-stage company
burning $18–42M a year**; they are shown and excluded from the level, and the screen's refusal
was the correct output. **2016–2023 are the pre-generic monopoly**, in which price supplied 42%
to 79% of each year's growth; that price regime ended in January 2024 and does not describe
the business now. **Only 2024, 2025 and H1 2026 describe the business that exists** — a
generic-exposed product with an authorized generic and a launch — **and they disagree with
each other by $78M on the charge basis and $155M on the grant basis.** The honest statement of
the level is therefore **dollars and a word: "$34M to $96M on the two SBC measures across the
generic era, roughly nothing in the last twelve months, and negative in the last six."**

**The rebuilt width:** across windows that contain only profitable years and both SBC
measures, **$44.8M to $98.8M — 2.2x against the published 1.05x.** Including the generic-era
grant-basis figure, $33.9M to $98.8M — 2.9x.

- **Maintenance capex — the corpus default holds, and it is irrelevant [E3-44, E2-41].** This
  is not the capital-intensive exception **[E5-20]**; it is the opposite case. Net PP&E is
  $1.9M on $837M of assets; the filing's investing section carries one capital line of $211k.
  D&A ($1.15M) is the guess for (c), it is the larger of the two ends, and the band
  contributes nothing to the range. **Working-capital increment:** receivables +$5.8M and
  inventory +$7.5M in 2025 are inside OCF already.
- **Stock compensation subtracted in full [E5-06], on both measures, and the second is the
  one the corpus specifies.** The charge: **$84.5M in 2025, 59.5% of OCF**; **H1 2026 $52.5M
  against $16.8M of OCF — 313%.** The market-value measure **[E3-70]** — *"what the company
  could have realized by publicly selling options of like quantity and structure"* — taken as
  the grant-date fair value of the year's grants (2,866k options × $36.08 + 1,192k restricted
  shares × $68.07) is **$184.5M in 2025, 2.18x the charge and 130% of OCF.** The charge is the
  floor of the subtraction, not the measure; and the tax note independently confirms the
  scale: **$227.5M of intrinsic value realised on option exercises in 2025.**
- **[E4-41] — normalise DOWN for luck.** Favourable break named: 2025 cash taxes of $13.0M
  against $60.3M in 2024, of which the OBBBA research-expensing election (enacted 2025-07-04;
  $397.8M federal NOL generated) is legislative and exogenous. At the 2022–24 cash-tax rate
  (~36% of pre-tax) 2025 cash taxes would have been ~$24M, so 2025 OCF is normalised down
  by roughly **$11M**. The unfavourable break — the vendor's capacity shortfall — is *not*
  added back; the framework normalises only for luck. **And $21.7M of 2025 OCF is interest on
  the cash pile**, which the market cap already contains: ex-interest, 2025 owner earnings on
  the charge basis are roughly **$35M**.
- *Is the range too wide to reach a conclusion? **Yes** — and that would have been the Q4
  verdict [E4-25] had Q2 not already closed the file.* The distorted years are named: 2025
  (launch SG&A +$168M, vendor shortfall, SBC doubling) and H1 2026 (Lifyorli launch, no
  revenue offset until Q2). **A wide spread is a Q4 finding about reliability [E5-11]**, and
  here the newest year is the outlier in the direction the "no step" flag cannot see.

### Great, good, or gruesome? **[E4-20]**
- [x] **great — for Korlym alone, 2017–2023:** no capital, 34–36% operating margins, price
  rising every year. The savings account paid an extraordinary rate.
- [ ] good / [ ] gruesome — **cannot be assigned for the company as constituted, and that is
  a finding.** The great account's interest is now being deposited into a second account —
  $254.9M of R&D and a $168M SG&A step — and **[E4-43]**'s test for whether that is *good* or
  *gruesome* is *"unless the cash they consume gets to earn a reasonable return."* Lifyorli
  has one quarter of revenue and no earnings; relacorilant in Cushing's has a decision date.
  The class is **UNKNOWABLE until the successor earns**, which is the same fact that closed
  Q2 from the other side.

### Staying power — score all three **[E5-11]**
- **(1) large and reliable stream of earnings — FAILS on "reliable."** Owner earnings on the
  charge basis: $135M → $56M → negative in H1 2026; guided revenue was missed by 15% in the
  latest full year. Large, historically; reliable, no.
- **(2) massive liquid assets — PASSES.** $544.6M of cash and securities at 2026-06-30
  (maturities under three years, duration under two), **no debt of any kind**, no bank lines
  relied on **[E5-39]**.
- **(3) no significant near-term cash requirements — PASSES.** API purchase commitment
  $10.7M; leases $7.4M through 2030; no maturities; the buyback was halted. The operating
  spend is large but discretionary — R&D can be cut in a quarter. This is the strength the
  corpus says usually kills, and it does not kill here.
- **Leverage, named and quantified: none.** No interest to cover; **[E2-54]** passes
  trivially. The balance sheet is built for the storm **[E2-64]** — and is being spent on the
  pipeline rather than kept for it.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]** — exposure, not experience
- **Mechanism A — the funnel is found unlawful and the generic substitutes at the
  pharmacy.** Teva's antitrust case, joined in substance by Aetna, HCSC, Humana and Molina,
  goes to trial in **March 2027**; a finding or settlement that opens dispensing to Teva's
  tablet removes the arrangement by which Corcept kept the volume. *Quantified from filed
  figures:* the filing does not give the AG share, so the arithmetic is illustrative and
  labelled — if half of the $761M hypercortisolism revenue is already at AG prices and Teva
  takes half of that, revenue falls **~$190M at a 98% gross margin, and operating income goes
  from +$45M to roughly −$140M.** Likelihood: **a real possibility** — the motions to dismiss
  were partly denied and the trial is set.
- **Mechanism B — relacorilant is refused again on 2026-12-17.** The Cushing's programme
  ($93.1M of 2025 R&D) then has no product, Korlym runs off as a generic, and the successor in
  the indication that generates all of today's earnings is gone. *Quantified:* the 2025
  Cushing's R&D alone exceeds 2025 operating income twice over. Likelihood: **a real
  possibility** — the FDA refused once on *"additional evidence of effectiveness"*, and the
  filings say only that the NDA was *"resubmitted"* six months later; what was added is
  **UNRESEARCHED** (the document is the resubmission's cover letter, which is not public).
- **Mechanism C — the NJ USAO investigation resolves against the funnel's practices** (HCP
  payments, prior authorisations). Open since November 2021; **no accrual** (*"No such amounts
  are accrued"*); unquantifiable from filed figures. Likelihood: **a low-level possibility to a
  real possibility** — four years and ten months is long for a matter that ends in nothing.
- **Mechanism D — the IRA**, filed by the company as *"may materially reduce our profits in
  2026 and beyond."* Likelihood, on the company's own word: **likely**, magnitude unfiled.
- **Q4, had it been reached: UNKNOWABLE [E4-25] — the range is too wide, the class cannot be
  assigned until the successor earns, and strength (1) fails. Recorded, not a verdict.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## COMPUTATION — NOT A CLEARANCE
*Q1–Q4 do not each show IN (Q2 is OUT). Under operator rule 3 this block is arithmetic only,
carries no entry language, and exists because the brief asked what the price is pricing.
Engine: the `run.py` ten-year fade to 2.5%, run by hand in
`Test Runs/_research 2026-09-11 CORT/OWNER_EARNINGS_OUTPUT.txt`.*

**THE FLOOR [E4-28].** Honest pre-tax expectancy at $114.92: **0.1% to 0.8%** on owner
earnings of $11M (TTM) to $99M (7-year charge basis) against a $12,422.7M cap. **Below the
floor by nine points; quit on, not ranked.** No risk premium was added to any rate **[E3-42]**.

**1. THE YIELD**
- owner earnings **$44.8M .. $98.8M** ÷ market cap **$12,422.7M** = **0.36% .. 0.80%** ·
  sovereign **5.37%** · (TTM $10.6M = **0.09%**)

**2. WHAT THE PRICE ALREADY ASSUMES**
- year-1 growth needed to justify the quote at the 10% floor, fading to 2.5% over ten years:
  **63% to 89%** across the bases; at the bare sovereign, **32% to 54%**.
- what the business has actually done: owner earnings (charge basis) **$105.7M (2019) →
  $56.4M (2025)**, a compound decline of ~10% a year across the window that contains the
  generic; revenue +20% a year over the same six years.
- **[E4-35]**'s base rate: *"fewer than 10 of the 200 most profitable companies"* sustain 15%
  a year for twenty years. This price needs four to six times that in year one.
- **What the price is actually pricing, in the company's own numbers:** 2026 guided revenue
  of $1.1–1.2B. At the **best operating margin Corcept ever earned (36.4%, 2019)** on $1.15B,
  operating income would be ~$420M and after-tax earnings ~$330M — **a 2.7% yield at this
  price, still below the floor with every dollar of R&D and launch cost gone.** The quote is
  not pricing Korlym, and it is not pricing guided 2026 at peak margin; it is pricing
  relacorilant in Cushing's, the oncology programme, MASH and ALS — the pipeline the framework
  values at what exists, which for four of the five is nothing yet **[E5-34]**.

**3. WHAT YOU ARE PAID**
- return at the current price = **roughly −2.1 to −2.6 points against the sovereign** on the
  `run.py` engine at 3% growth; on TTM owner earnings the engine refuses (base near zero).

**THE KORLYM RUN-OFF, LABELLED AS THE ILLUSTRATION IT IS.** If every dollar of R&D stopped
and Korlym were milked as a generic-exposed product: OCF $142.0M + R&D $254.9M × (1 − 21%)
− SBC $84.5M ≈ **$259M**, a **2.1% yield**; capitalised at the floor with no growth, roughly
**$2.6B, or ~$24 a share** — a fifth of the price, for a product whose realised price is
falling and whose channel is on trial. The pipeline is not entering Q5 through the back
door: it is not entering at all, and without it the price has no support.

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used ____ % — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this
method cannot support:
- at the 10% floor, bases $45M–$99M, year-1 growth 5%–30% fading to 2.5%: **conservative
  ~$6 · optimistic ~$35 a share**; at 50% year-1 growth, $34–$74 · **current price $114.92,
  above the whole range at every base and every growth case computed.** *(Computation, not a
  clearance; no entry language attaches to any of these figures.)*

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- floor verdict first: honest pre-tax expectancy **0.1%–0.8%** vs ~10% **[E4-28]** — **below →
  quit on, and the lines below are not filled in**
- points over sovereign, this name: *not ranked*
- against the rest of the opportunity set: *not ranked*
- *Take the best available, or nothing.*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — realistic inputs, one margin at the end.
      Margin used ____ %, and which corpus illustration it sits nearest:
      bridge ~35% **[E3-25]** · Grand Canyon 60%, the stated ceiling **[E3-26]** ·
      "closer to a dollar on the dollar" for a business you understand **[E4-12]** ·
      "dollar bills for 80 cents" **[E5-09]**
- [ ] **Screamer test [E4-01]** — does the price already clear the **conservative** case?
      No margin is added on top. Three outcomes: below the conservative case → act ·
      **inside the range → no useful conclusion, move on** · above the whole range → no.
- **Windage count** — conservatism applied at how many places? **Zero.** No margin was
  applied because no computed value approaches the price; the bar question does not arise.
  **[E4-11]**

- **Q5 did not open. No verdict; no ranking position. The file closed at Q2.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**No entry, so no sell rule applies. What is pre-committed instead is the REVERSAL
SPECIFICATION [E1-02] — in words, not price bands, because this name failed on the business
and a price alert on it would be a category error (the QLYS ruling, 2026-09-07).**

- **Re-open Q2 only if one of the four conditions named at Q2 is met:** (a) realised price
  for the hypercortisolism products filed as rising for four consecutive quarters with the
  AG mix stable; (b) relacorilant approved in Cushing's **and** two full years of filed
  revenue in that indication; (c) *Teva v. Corcept* and *Aetna et al. v. Corcept* resolved
  without a change to the dispensing arrangement; (d) a filed unit or brand/AG series.
- **Thesis-confirming metric (for the OUT):** the average-price line in each 10-Q's revenue
  paragraph — filed every quarter — continuing to read "decrease … due to higher sales
  volume from our authorized generic."
- **Thesis-breaking metric:** condition (b) — it is the only one that would make the moat
  evidenceable rather than promised, and it has a date.
- **Next catalyst dates:** relacorilant Cushing's PDUFA **2026-12-17**; EMA decision on
  Lifyorli and BELLA Part A and MONARCH results, all *"by the end of this year"*; Q3 2026 10-Q
  (~early November) for the price series and SBC; **Teva antitrust trial March 2027**.
- **Position size: none.** The capital-allocation flag at Q3 would have bound size had the
  file reached Q5; it did not.
- **[E4-17] / [E3-30]:** the moat downgrade here was not slow — it had a court date and a
  launch date — and the belief that the successor's moat exists should form slowly, on
  filed earnings, not on a PDUFA letter.

- **Q6: no verdict; no position. Watch specification recorded above.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 OUT, file closed; Q3–Q6
      recorded and labelled as not verdicts
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1 IN is on
      understanding, from the filed statements
- [x] Every UNRESEARCHED item names the artifact: the relacorilant resubmission's contents
      (not public); the brand/AG split and Teva's share (not filed by either party)
- [x] Every UNKNOWABLE item states what cannot be known: the successor's earnings, and
      therefore the [E4-20] class, until relacorilant earns
- [x] Step 0: the filing was read, with accession numbers; six figures cross-checked to the
      dollar
- [x] Owner earnings on multi-year means across eleven windows; both SBC measures; (c)
      disclosed as the corpus default and shown to be immaterial
- [x] Competitor row: 3 of 3 named branded competitors plus Teva; **partly PROVISIONAL**
      (Recordati non-SEC; Teva files no product line) and stated as such; the verdict rests on
      the subject's own filings and the row corroborates. Research file:
      `Test Runs/_research 2026-09-11 CORT/COMPETITOR_ROW.md`
- [x] Sovereign for USD, US Treasury daily par yield curve (issuing authority), 2026-09-10
- [x] Value stated as a round-number range, labelled COMPUTATION — NOT A CLEARANCE
- [x] No bar chosen because Q5 did not open; windage count zero, stated
- [x] Price $114.92 dated 2026-09-10, aggregator, flagged as live quote only
- [x] Run committed to git after Step 0/Q1, after Q2, and at close

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **A sixty-year-old molecule whose exclusivity has expired, whose identical generic
  Corcept now sells itself at an 18% lower realised price, whose channel is on trial in March
  2027, and whose replacement was refused once and is due a second decision on 2026-12-17 — at
  $12.4bn against $11M to $99M of owner earnings.**
- **The strongest fact against this verdict:** tablets sold rose 37% in the generic's second
  year, Lifyorli booked $47.6M in its first quarter with 1,300 patients started, and
  relacorilant's composition patents run to 2040. If the funnel is the asset and relacorilant
  is approved in December, this is a franchise between tenants and the OUT was written one
  decision too early. The reversal conditions at Q2 and Q6 exist for exactly that case.
