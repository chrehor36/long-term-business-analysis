# AXR (AMREP Corporation) — evidence pack for the 2026-08-30 v4.1 run
Assembled 2026-08-31. Every figure below is traced to a filed document or a named
issuing authority. Aggregator data is used for live quotes only and is flagged.

---
## 1. DOCUMENTS READ

| document | filed | accession | what was read |
|---|---|---|---|
| **FY2026 Form 10-K** (FYE 2026-04-30) | 2026-07-24 | **0001104659-26-086659** | Item 1 Business, Item 2 Properties, Item 3, Item 5, **Item 7 MD&A in full**, Item 8 **statements + all 15 notes** |
| **DEF 14A** (2026 annual meeting) | 2026-08-04 | **0001104659-26-090418** | ownership table, directors, Summary Compensation Table, audit fees, 2026 Equity Plan proposal |
| 8-K (Item 2.02, FY2026 results release) | 2026-07-24 | 0001104659-26-086664 | cover only; release furnished as Ex-99.1 |
| 8-K (Item 5.02, FY2027 officer pay) | 2026-07-14 | 0001104659-26-083522 | full |
| DEF 14A (2023) | 2023-08-02 | 0001104659-23-086818 | **Karabots transaction disclosure only** |
| FY2025 / FY2023 / FY2021 / FY2019 10-Ks | various | — | **acreage and trading-volume lines only** (units series) |

**Auditor:** Rosenberg Rich Baker Berman, P.A., Somerset NJ, "auditor since 2024."
Unqualified opinion, 2026-07-24. **"We determined that there were no critical audit
matters."** No ICFR auditor attestation (smaller-reporting-company exemption).
Predecessor: Baker Tilly US, LLP (through FY2024).

**No 10-Q exists after the 10-K.** FY2027 Q1 ended 2026-07-31; the comparable prior-year
Q1 10-Q was filed 2025-09-09. Latest financial filing is therefore the FY2026 10-K.

### Figure cross-checked against the filed statement
**FY2026 net cash provided by operating activities.**
- Filed Consolidated Statements of Cash Flows: **"Net cash provided by operating
  activities ... 12,878"** (thousands)
- MD&A "Cash Flow" table: **12,878**
- SEC XBRL companyfacts, CIK 0000006207,
  `NetCashProvidedByUsedInOperatingActivities`, FY2025-05-01/2026-04-30: **12,878,000**

Three-way match. Second check: FY2025 OCF 10,242 in all three places.

---
## 2. PRICE, SHARES, MARKET CAP — verified as tasked

| item | value | source |
|---|---|---|
| Shares outstanding | **5,324,849** as of **2026-07-20** | 10-K cover page, filed |
| Shares issued at balance-sheet date | 5,305,199 at 2026-04-30 | balance sheet, filed |
| Close | **$23.08, 2026-08-28** | Yahoo chart API (**aggregator, live quote only, flagged**) |
| **Market capitalisation** | **$122,897,515 ≈ $122.9M** | 5,324,849 x $23.08 |
| Sweep figure | ~$124M on ~5.3M shares | **reproduced; gap 0.9%** |

Corroboration from the filing itself: the 10-K cover states aggregate market value held by
non-affiliates was **$82,217,793 at 2025-10-31**. Non-affiliates then were roughly
5.3M less the ~2.0M held by directors and officers, i.e. ~3.3M shares, implying ~$25/share
in October 2025. Consistent with the aggregator series.

Book value per share: $140,743,000 / 5,324,849 = **$26.43**. **Price / book = 0.87x.**

### Liquidity and spread friction for a $2,750 order [E3-67]
- $2,750 / $23.08 = **119 shares**.
- **Filed** 30-day average volume to 2026-04-30: **13,210 shares/day** (10-K Item 5).
  Prior years, same disclosure: 16,350 (FY2025), 8,540 (FY2023), 13,439 (FY2021),
  ~5,200 (FY2019).
- Observed 23 sessions 2026-07-29 to 2026-08-28 (aggregator, flagged): median **9,000**
  shares/day, **minimum 900**, maximum 53,400.
- Observed mean intraday high-to-low range: **3.0%**; 8 of 23 sessions above 4%.
- The 10-K says it in its own words: **"The Company's common stock is often thinly traded.
  As a result, large transactions in the Company's common stock may be difficult to
  execute in a short time frame and may cause significant fluctuations in the price"** and
  attributes it to three shareholders owning **~52%**. **237 holders of record** at
  2026-07-20.

**Conclusion.** 119 shares is about 1.3% of a median day, so order *size* is not the
problem; on the thinnest observed day it would have been 13% of volume. The friction is
the quoted spread and price impact in a book with a 3.0% mean daily range. A round trip
plausibly costs **1% to 3% each way, i.e. $55 to $165 on $2,750**, against [E3-67]'s
stated "3 percent per annum" benchmark for management plus in-and-out costs. **Limit
orders only; a market order in this name is a donation.**

---
## 3. SOVEREIGN

**USD 30-year Treasury constant maturity: 5.19%, 2026-08-27.**
Source: FRED series **DGS30** via `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS30`
(direct route as directed; `tools/sources.py` USD bypassed). Adjacent prints: 5.17
(08-25), 5.18 (08-26), 5.19 (08-27). FRED's one-to-two-day lag noted, immaterial.
Earnings currency is USD; the 10-K states "The Company has no foreign sales."

---
## 4. THE FILED SERIES (fiscal years end April 30; $000 unless noted)

| FY | revenue | net income | OCF | SBC | P&E capex | depreciation | equity | cash+equiv | buybacks |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 18,783 | (5,903) | 765 | 113 | 9 | 537 | 84,637 | 17,502 | 0 |
| 2021 | 40,069 | 7,392 | 12,609 | 132 | 5 | 554 | 88,889 | 24,801 | 5,116 |
| 2022 | 58,926 | 15,862 | 15,476 | 217 | 1,287 | 225 | 83,162 | 15,721 | **21,904** |
| 2023 | 48,676 | 21,790 | 6,389 | 238 | 131 | 63 | 111,000 | 19,993 | 0 |
| 2024 | 51,369 | 6,690 | 10,714 | 317 | 457 | 149 | 118,050 | 29,694 | 0 |
| 2025 | 49,694 | 12,716 | 10,242 | 423 | 583 | 179 | 129,961 | 39,466 | 0 |
| 2026 | 52,847 | 10,288 | **12,878** | 447 | 102 | 312 | **140,743** | **52,327** | 0 |

Source: FY2026 10-K statements for 2025-2026; SEC XBRL companyfacts (CIK 0000006207) for
2020-2024, each figure originally tagged from that year's 10-K.

**Balance sheet, 2026-04-30 (filed):** total assets **$144,778**; total liabilities
**$4,035** (accounts payable and accrued expenses 4,017 + notes payable 18); equity
**$140,743**. Real estate inventory **$66,556** (land 54,843; homebuilding model and
completed 8,675; construction in process 3,038). Investment assets net **$16,174** (land
held for long-term investment 8,482; owned real estate leased or intended to be leased
net 7,692). Deferred income taxes net **$5,772**. Cash + restricted **$52,689**, of which
**US Government Securities $38,526**.

**Debt, in full (Note 6):** BOKF revolving line of credit, up to $6,500 committed,
**$0 drawn**, $4,438 available after reserves, 6.80% (SOFR + 3.15%), matures **August
2028**, secured on Paseo Gateway, covenants require ASW net worth at least **$32 million**
and $3.0 million of unencumbered cash to draw. Deere equipment loan **$18** at 2.35%,
matures June 2028. **Total debt $18 thousand.** Loan reserves of $1,812 support a
municipal subdivision-completion obligation.

### Return series
| FY | ROE (NI / avg equity) | ROE on avg equity **excluding cash** |
|---|---|---|
| 2021 | 8.5% | 11.3% |
| 2022 | 18.4% | 24.1% |
| 2023 | 22.4% | 27.5% |
| 2024 | 5.8% | 7.5% |
| 2025 | 10.3% | 14.2% |
| 2026 | **7.6%** | **11.5%** |
| 5-yr mean FY2022-26 | **12.9%** | 16.9% |
| 6-yr mean FY2021-26 | 12.2% | 16.0% |

No leverage and no goodwill, so book equity is already the [E2-43] unleveraged
net-tangible-asset denominator. The ex-cash column is this run's estimate of return on
capital actually employed in the business; the cash and government securities were 36% of
assets at 2026-04-30.

### Book value per share, every window published [E4-38]
| FY | shares issued | equity ($000) | BVPS |
|---|---|---|---|
| 2019 | 8,353,154 | 89,846 | $10.76 |
| 2020 | 8,358,154 | 84,637 | $10.13 |
| 2021 | 7,323,370 | 88,889 | $12.14 |
| 2022 | 5,240,309 | 83,162 | $15.87 |
| 2023 | 5,254,909 | 111,000 | $21.12 |
| 2024 | 5,271,309 | 118,050 | $22.39 |
| 2025 | 5,287,449 | 129,961 | $24.58 |
| 2026 | 5,305,199 | 140,743 | $26.53 |

CAGR to FY2026: **7y 13.8% · 5y 16.9% · 4y 13.7% · 3y 7.9% · 2y 8.8% · 1y 7.9%.**
Every window is shown because [E4-38] requires it; the five-year figure is carried by the
March-2022 buyback and the recent rate is roughly 8%.

---
## 5. THE UNITS SERIES [E4-55] — acres, not dollars

| fiscal year end | acres owned in Sandoval County (filed, Item 1) |
|---|---|
| 2019 | ~18,000 |
| 2021 | ~18,000 |
| 2023 | ~17,000 |
| 2025 | ~16,600 |
| **2026** | **~16,200** (of which ~15,300 undeveloped) |

Net depletion FY2021 to FY2026: ~1,800 acres over 5 years = **~360 acres/yr**, implying a
~45-year bank at that net rate. **Gross** acres sold were 719.0 (FY2025) and 587.5
(FY2026), implying **23 to 27 years** with no replacement purchases.

**Rio Rancho new single-family starts (filed, by the Company, its customers and other
builders): 973 in FY2025, 805 in FY2026, down 17%.**

Mineral rights: the Company owns minerals and mineral rights under approximately
**55,000 surface acres** in Sandoval County. No carrying value, lease income or production
is disclosed anywhere in the 10-K.

---
## 6. THE UNIT ECONOMICS, FROM THE FILED TABLES

**FY2026 land sales**
| | acres sold | revenue $000 | revenue/acre |
|---|---|---|---|
| Developed residential | 16.8 | 13,781 | **$820,000** |
| Developed commercial | 3.3 | 1,000 | $303,000 |
| Undeveloped | 567.4 | 5,798 | **$10,218** |
| Total | 587.5 | 20,579 | $35,000 |

**FY2025 land sales:** developed residential 28.6 acres / $21,910 / $766K per acre;
undeveloped 690.4 acres / $3,738 / **$5,414 per acre**; total 719.0 acres / $25,648.
FY2026 included a **467-acre contiguous bulk sale for $2,174, i.e. $4,655/acre**, to one
purchaser (FY2025: 549 acres for $2,502, $4,557/acre). The 10-K states these bulk sales
are **not expected to be indicative of future undeveloped land sale revenues.**

**Land sale cost of revenues, net (FY2026):** gross cost 10,504 less public improvement
district reimbursements 900, private infrastructure covenant reimbursements 434, and
payments for impact fee credits 1,041 = **8,129 net**. The reimbursement mechanisms
therefore recovered **$2,375, or 23% of gross land cost.**
**Land sale gross margin 61% (FY2026) vs 52% (FY2025).**

**Homes:** 65 sold at $441K average (FY2026) vs 50 at $425K (FY2025); **home sale gross
margin 24% vs 21%**. 75 homes in production at year end, 24 under contract representing
$12,983 of expected revenue. 28 completed homes leased to residential tenants (21 prior
year), because "Given the impact on demand as a result of affordability challenges, the
Company has opportunistically leased completed homes."

**Segments (FY2026):** Land development revenue 29,235, segment profit **10,038**;
Homebuilding revenue 23,612, segment profit **4,097**; corporate G&A (1,743); interest
income net 1,734; income before taxes **14,126**.

**Customers:** "100% of 2026 developed residential land sales having been made to three
homebuilders." One customer exceeded 10% of revenue: **$8,954** (17.0% of total revenue).
FY2025: two customers, $11,809 and $6,028.

**Employees: 52.** G&A **$9,025** = 17.1% of revenue, up 24% year over year on 6% revenue
growth (land development G&A +36%, "primarily due to an increase in property taxes").

---
## 7. TAX ATTRIBUTES (Note 12) — an [E3-71]-class advantage

- Federal NOL carryforwards **$20,620** at 2026-04-30, **no expiration**, usable against
  80% of taxable income per year.
- State NOL carryforwards **$46,843**, expiring from FY2038; a **$1,127** valuation
  allowance is carried against state attributes.
- Deferred tax asset for **"Real estate basis differences" $2,581** — the tax basis of the
  real estate **exceeds** its book basis, the residue of pre-2013 book impairments.
- Effective tax rate FY2026 **27.0%**; **cash income taxes paid net of refunds $502**, i.e.
  **3.6% of $14,126 pretax**. The gap is fully explained by the disclosed NOLs and is
  reconciled in the note. **Recorded as explained, not as an [E4-30] tell.**
- Section 382 risk is disclosed: an ownership change would limit the attributes. With three
  holders at 52% and a classified board, this is a live constraint on any control event.

---
## 8. OWNERSHIP AND THE KARABOTS CORRECTION

**The brief's premise ("Karabots control") is out of date and is corrected here.**

The 2023 DEF 14A (accession 0001104659-23-086818), under TRANSACTIONS WITH RELATED
PERSONS, discloses verbatim: **"In March 2022, the Company acquired an aggregate of
2,096,061 shares of Common Stock, representing 28.6% of the Company's then-outstanding
shares, from the Estate of Nicholas G. Karabots, Glendi Publications, Inc. and Kappa Media
Group, Inc. at a price of $10.45 per share in a privately negotiated transaction. The
total purchase price was $21,903,837.45. The closing price per share of Common Stock
reported on the New York Stock Exchange was $11.47 on the last trading day pr[ior]..."**

An EDGAR full-text search of AMREP filings for "Karabots" restricted to 2023-01-01 to
2026-08-31 returns **exactly one hit, that 2023 proxy**. There is no Karabots holding in
the current register.

**Beneficial ownership as of 2026-07-20 (DEF 14A filed 2026-08-04):**

| holder | shares | % |
|---|---|---|
| **Albert V. Russo (director)** + Clifton Russo, Lawrence Russo, Pasha Funding LLC | 1,298,275 | **24.3%** |
| **James H. Dahl and Rainey E. Lancaster** (13D/A No. 8, filed 2026-06-24) | 998,729 | **18.8%** |
| **Robert E. Robotti (director)** + Robotti & Co / Ravenswood entities | 521,764 | **9.8%** |
| Edward B. Cloues, II (chairman) | 59,032 | 1.1% |
| Christopher V. Vitale (CEO) | 125,900 | 2.4% |
| Adrienne M. Uleau (CFO) | 10,574 | * |
| Timothy S. McNaney | 1,765 | * |
| **Directors and NEOs as a group (5 persons)** | **2,017,310** | **37.4%** |

Top three = **52.9%**, matching the 10-K's "approximately 52%".

**Board (5 seats, classified into three classes):** Edward B. Cloues II (chairman,
director since 1994, age 78, ex-CEO of K-Tron, ex-chairman Penn Virginia); Christopher V.
Vitale (CEO since 2017, director since 2021, age 50, lawyer by training); Albert V. Russo
(since 1996, age 72, commercial real estate, 24.3% holder); Robert E. Robotti (since 2016,
age 73, Robotti & Co / Ravenswood, 9.8% holder); **Timothy S. McNaney (since January 2026,
age 56, co-founder and co-President of Twilight Homes of New Mexico until July 2025)**.

**Takeover structure, in the company's own words (Item 5):** Oklahoma anti-takeover
provisions "generally prohibit the Company from engaging in 'business combinations' with
an 'interested shareholder' ... unless the holders of at least two-thirds of the Company's
then outstanding common stock approve the transaction. Consequently, the concurrence of
the Company's largest shareholders would generally be needed for any 'interested
shareholder' to acquire control of the Company, **even if a change in control would be
beneficial to the Company's other shareholders.**"

**Dividend, filed verbatim: "The Company has paid no cash dividends on its common stock
since fiscal year 2008."** Eighteen years. **Current yield 0.00%.**

**Compensation (DEF 14A Summary Compensation Table, and the 8-K of 2026-07-14):**

| | FY2026 salary | bonus | stock awards | other | **total** |
|---|---|---|---|---|---|
| C. V. Vitale, CEO | 379,000 | 168,000 | 176,000 | 11,100 | **734,100** |
| A. M. Uleau, CFO | 195,000 | 61,000 | 46,000 | 11,100 | **313,100** |

FY2025: Vitale $688,800, Uleau $281,600. Two named officers, combined **$1,047,200 =
10.2% of FY2026 net income**; the CEO alone is **7.1%**. On 2026-07-13 the board awarded
Vitale a $178,000 cash bonus and 8,700 restricted shares vesting 2027/2028/2029, Uleau a
$64,000 bonus and 2,250 restricted shares, and set FY2027 salaries at $395,000 and
$205,000. Vitale also holds an option over 50,000 shares becoming exercisable 2026-11-01.
**Audit fees $120,000 (FY2026 and FY2025), no tax or other fees.**

---
## 9. THE COMPETITOR ROW [E3-28]

AXR's actual competitors for lots in Rio Rancho are unnamed in the 10-K and are private
("The Company competes with other owners and developers of land"). The row below is
therefore built from the **five listed US land-development / lot-supply comparables**,
each from its own latest audited fiscal year via SEC XBRL, with each filer's own window
stated. Prices are aggregator quotes at 2026-08-28 and are flagged.

| | **AXR** | FOR (Forestar) | JOE (St. Joe) | GRBK (Green Brick) | STRS (Stratus) | MLP (Maui Land) |
|---|---|---|---|---|---|---|
| business | NM land bank + small builder | national residential lot developer | FL legacy land, mixed use | land + homebuilding | TX land developer | HI legacy land |
| latest FY | FY2026 (Apr) | FY2025 (Sep) | FY2025 (Dec) | FY2025 (Dec) | FY2025 (Dec) | FY2025 (Dec) |
| revenue | $52.8M | $1,662.4M | $513.2M | $2,098.5M | $29.9M | n/d |
| **ROE, latest FY** | **7.6%** | 10.0% | **15.5%** | **18.0%** | 6.0% | (31.9%) |
| ROE, prior FY | 10.3% | 13.7% | 10.5% | 26.1% | 1.0% | (21.8%) |
| **gross margin** | **40.5% total; land 61%, homes 24%** | **21.9%** | 43.1% | 30.5% | n/d | n/d |
| total liabilities / equity | **0.03x** | 0.77x | 0.97x | 0.32x | 1.06x | 0.45x |
| market cap | $122.9M | $1,460.6M | $3,832.5M | $3,153.1M | $150.6M | $313.0M |
| **price / book** | **0.87x** | 0.83x | **5.00x** | 1.70x | 0.74x | **9.47x** |

Sources: SEC XBRL companyfacts, each company's own 10-K tags — FOR CIK 0001406587, JOE
0000745308, GRBK 0001373670, STRS 0000885508, MLP 0000063330. STRS ROE uses net income
available to common over average parent equity (it consolidates non-controlling
interests). MLP does not tag Revenues consistently.

**Peers named: 5.** All five are listed US land developers or legacy landholders; AXR's
*local* competitors are private and unnamed by the subject, so the row cannot show
Sandoval County share. **[E3-61]'s limit stands: the row shows position, not conduct.**
**No moat class is claimed here that would require the missing private local rows**, so
PROVISIONAL does not arise; the Q2 verdict rests on AXR's own filed concessions plus the
share arithmetic below.

**The share arithmetic that decides the substitute question.** FY2026 developed
residential land sold: **16.8 acres**. Rio Rancho lots run roughly 5 to 7 per acre at
these prices, so AXR's developed-land sales supplied on the order of **85 to 115 lots**
into a market with **805 new single-family starts** — roughly **10% to 14%**. AXR's own
homebuilder closed **65 homes = 8%** of starts. **In the town its predecessor platted,
AMREP supplies about one new lot in eight.** The lot-per-acre assumption is this run's
estimate and is labelled as such; the direction of the answer does not turn on it.

**The cost advantage, measured.** AXR's **61% land gross margin against Forestar's 21.9%
company gross margin** is the [E2-58] exception tested in numbers: the advantage is real
and it is wide. JOE, the other legacy-basis landholder, runs 43.1%. What the row also
shows is that the wide margin does **not** convert into a superior return on capital:
AXR earns 7.6% on equity where GRBK earns 18.0% and JOE 15.5%.

**And the price/book column carries its own warning.** JOE at 5.0x book and MLP at 9.5x
book are the market paying up for stale-basis land in Florida and Maui. AXR at 0.87x is
not getting that treatment, and the honest reason is location: high-desert Sandoval
County is not beachfront. The premium is location-specific, not generic to legacy land.

---
## 10. ARITHMETIC USED IN THE RUN

**Owner earnings**, convention: multi-year mean of (OCF less SBC) less (c). $000.

| window | OCF mean | SBC mean | OCF-SBC | (c) = $2,000 | (c) = $4,000 |
|---|---|---|---|---|---|
| 5-yr FY2022-26 (corpus default [E2-42]) | 11,140 | 328 | 10,811 | **8,811** | **6,811** |
| 7-yr FY2020-26 | 9,868 | 270 | 9,598 | 7,598 | 5,598 |
| 3-yr FY2024-26 | 11,278 | 396 | 10,882 | 8,882 | 6,882 |

**Combined range $5.6M to $8.9M, round $5.5M to $9M.** Bottom boundary [E5-34] ~$5.5M-6.5M.
Yield on the $122.9M cap: **4.6% to 7.2%**, against the 5.19% sovereign.

**Enterprise framing** (cash and equivalents $52,327 deducted; debt $18 ignored):
EV = $70.6M. Interest income net $1,734 pretax, ~$1,266 after tax at the 27.0% effective
rate. Operating owner earnings = $4.33M to $7.63M. **EV yield 6.1% to 10.8%.**

**Asset basis** ([E3-71], liquidating value plus advantages):
- Book equity $140,743 = **$26.43/share**; price/book 0.87x.
- Cash + restricted $52,689 = **$9.89/share**, against total liabilities of $4,035.
- All land-carrying lines combined: land inventory 54,843 + land held for long-term
  investment 8,482 = **$63,325**, covering 217 developed residential lots, 68 developed
  commercial/industrial acres, 358 acres under development **and** ~16,500 undeveloped acres.
- Maximally conservative markup on the 15,300 undeveloped acres, assuming the **entire**
  $63,325 land book belongs to them (it does not; the developed lots then count at zero):
  - at the FY2026 bulk-sale price $4,655/acre: $71.2M, markup **+$7.9M**, adjusted equity
    **$148.6M = $27.91/share**
  - at the FY2026 blended realised price $10,218/acre: $156.3M, markup **+$93.0M**,
    adjusted equity **$233.7M = $43.89/share**
- Counted at zero: mineral rights under ~55,000 surface acres; the developed lots and 68
  developed commercial acres that fetched $735K-$820K per developed acre in FY2026; the
  $1,127 valuation allowance on state NOLs.
- Charged against it: a 23-to-45-year monetisation timetable and ~$9.0M/yr of G&A carried
  through it.

**Retention test [E3-54].** Retained earnings 2022-04-30 $54,828 to 2026-04-30 $106,312 =
**$51,484 retained**. Market cap 2022-04-30: 5,240,309 x $12.86 = $67.4M (aggregator,
flagged). At 2026-08-28: $122.9M. **Change +$55.5M on $51.5M retained = $1.08 per $1.**
Measured to the April 2026 peak ($27.55, cap $146.2M) instead: $1.53 per $1. Both endpoints
published per [E4-38]; **the test passes, thinly, and the endpoint matters.**

**Floor arithmetic [E4-28].** $122.9M x 10% = **$12.3M of owner earnings required**. Filed
range $5.5M-$9.0M; the best single year in the record (FY2022: OCF 15,476 less SBC 217
less (c) 2,000 = $13.3M) clears it, the mean does not. On the enterprise basis:
$70.6M x 10% = **$7.06M of operating owner earnings required** against $4.33M-$7.63M
filed; the top of the band clears, the mean does not.
