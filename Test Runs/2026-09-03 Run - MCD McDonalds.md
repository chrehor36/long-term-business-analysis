# Company Run — McDonald's Corporation (MCD) — 2026-09-03
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
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.27%** · date **2026-09-02** · source (issuing authority) **US Treasury daily par
  yield curve, 30-yr** (via `tools/sources.py sovereign("USD")`)
- FX: quote and earnings both USD (MCD earns globally but reports and pays in USD; the
  sovereign for the reporting/earnings currency is the US long bond). ADR: n/a.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **10-K FY2025, filed 2026-02-24, accession
  0000063908-26-000035** (primary doc `mcd-20251231.htm`). Also read: 10-Q Q2-2026
  (filed 2026-08-07, accession 0000063908-26-000073) for the cover share count;
  DEF 14A (filed 2026-04-07, accession 0001193125-26-145548); 10-Ks FY2022
  (0000063908-23-000012), FY2019 (0000063908-20-000022), FY2016 (0000063908-17-000017),
  FY2013 (0000063908-14-000019) for the ten-year series. All saved to
  `Test Runs/_research 2026-09-03 MCD/`.
- figure cross-checked against the filed statement: **OCF series — the tool's
  10,551 / 9,447 / 9,612 matches the filed Consolidated Statement of Cash Flows line
  "Cash provided by operations 10,551 9,447 9,612" exactly.**

**PRICE AND CAP (aggregator for the live quote only, flagged):**
- price **$260.95**, 2026-09-02 close, aggregator (Stooq via `tools/sources.py`)
- shares **707,641,531** — hand-read off the 10-Q cover, "Number of shares of common stock
  outstanding as of June 30, 2026". Single class of common stock.
- **market cap $184,659M**

**SCREEN ROW — REPRODUCED before adjudicating** (`2026-09-02 MASTER RUN QUEUE
(corrected).csv`): cap 187,164 / oe_bottom 6,364 / oe_top 7,608 / spread 0.196 / yield
0.034 / growth_required 0.066 / level_shift "no step". Re-running
`floor_screen.owner_earnings` on today's companyfacts returns **5y_capex 6,363.7 /
3y_da 7,607.8 — the row's 6,364 and 7,608 to the million**; spread (7,608−6,364)/6,364 =
**19.6%** ✓; 6,364/187,164 = **3.40%** ✓; growth required 10% − 3.40% = **6.60%** ✓. The
screen's cap divides to a $264.49 price (an earlier close); at today's $260.95 the bottom
yield is 3.45%. Row reproduced.

**TOOL DEFECT NOTED (already known, fixed in floor_screen, still live in run.py):**
`tools/run.py` picked `DepreciationDepletionAndAmortization` = $457M as MCD's D&A — a
**subcomponent** (the SG&A depreciation line). The filed total is **$2,199M** (cash-flow
statement). `floor_screen.da_annual()` was corrected 2026-09-01 for exactly this name
(takes the max across candidate elements); `run.py.owner_earnings()` still takes the
first tag that resolves and printed OE hi $9,271M — overstated by ~$1.7bn/yr. run.py also
returned **shares 0.0M** (dei element absent — the META/GHC class) and yields in the
millions of percent. Everything below is computed from the filed statements, not the tags.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **McDonald's is a franchisor
  and a landlord, not a restaurant operator.** Of 45,356 restaurants at YE2025, 43,317
  (95.5%) are run by franchisees; MCD itself runs 2,039, mostly as a credibility/test
  bed. The money comes off the top line of other people's restaurants, in two streams
  stipulated in agreements that "generally have 20-year terms" (Item 1):
  **(1) rent — $10,442M in FY2025** — under the conventional-franchise structure MCD
  "generally owns or secures a long-term lease on the land and building" and charges the
  franchisee a percent of sales **with specified minimum rent payments**; and
  **(2) royalties — $6,018M** — a percent of sales for the brand and system (developmental
  licensees and affiliates, who provide their own real estate, pay royalty only). Initial
  fees are noise ($88M). The rent stream is the larger and the more distinctive one, and
  it is senior in structure: the franchisee's own equipment, décor and goodwill sit on
  MCD's land. Against the $16.5bn franchised stream MCD bears $2.6bn of occupancy cost
  (depreciation + head-lease rent), an **84% franchised margin**; the 2,039 company
  stores add $9.7bn of sales at a 15% margin; franchisees fund their own reinvestment.
  Costs below: $3.0bn SG&A, $1.6bn interest on ~$40bn of debt deliberately borrowed
  against the fee streams.
- The scarce input this business controls: **the corner real estate under ~22,570
  conventional franchised restaurants plus the trademark, tied together** — a competitor
  can copy the menu but cannot occupy the site, and a franchisee who quits the system
  walks away from a 20-year location and their sunk co-investment.
- Will the fundamentals look broadly the same in ten years? **Yes.** People will buy
  cheap, fast, consistent food; the 45,000 locations will still be where they are; the
  franchise/rent structure has been the model since the 1950s (the Sonneborn model). The
  strategy document changes ("Accelerating the Arches"); the unit economics have not.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The question is put at the right altitude first: MCD's customer is the FRANCHISEE, not
the diner.** The diner faces close substitutes on every corner; the franchisee does not.
What MCD sells is a 20-year package of brand + operating system + **the restaurant site
itself**, priced as ~4.6% royalty plus ~11% rent on sales, against which the franchisee
sinks equipment, décor and two decades of local goodwill **on land MCD keeps**. The
franchise note says it in one sentence: *"At the end of the 20-year franchise
arrangement, the Company maintains control of the underlying real estate and building
and can either enter into a new 20-year franchise arrangement with the existing
franchisee or a different franchisee, or close the restaurant."*

- Needed or desired [x] — $139.4bn of 2025 systemwide sales; the filed Euromonitor
  benchmark (last given in the FY2019 10-K) put MCD at **8.2% of a $1.2 trillion IEO
  category** — the largest single share of the most fragmented consumer category there is.
- no close substitute [x, at the franchisee level] — no other QSR franchise system
  offers the site + brand package at MCD's per-store volumes (peer AUV row below); for
  the diner the substitute exists, which is why the class judgment (below) is NARROW,
  not WIDE.
- not price-regulated [x] — menu prices are set by franchisees, not by MCD or any
  regulator (the FY2016 Item 1: franchisees *"maintain control over all
  employment-related matters, marketing and pricing decisions"*); MCD's own prices —
  the royalty and the rent — are private contract terms.

**THE AATC/QCOM PRECEDENT — the term structure runs the OTHER way.** AATC closed at Q2
because its licence had a term (2031) and a three-year notice clause held by the
counterparty; QCOM's licences expire 2027-2031 and its three largest customers build
the substitute. MCD's agreements also have a term — 20 years — but **at expiry the
asset reverts to MCD, not to the counterparty**. The franchisee cannot "design out"
the franchisor: quitting means surrendering the location and the sunk co-investment.
The schedule is filed: **$31,451M of contracted future minimum rent** due to MCD under
existing conventional arrangements ($15.8bn on owned sites, $15.6bn on head-leased),
with minimum rents that *"parallel the Company's underlying … escalations."* No renewal
rate is disclosed in any 10-K read (FY2013-FY2025) — stated as an absence, per the
absence-claim rule — but the conventional estate itself is the renewal record: 21,366
(2017) → 22,570 (2025) restaurants, never shrinking through COVID. This is not a QTL
(dated contracts held by counterparties who can leave); it is closer to Boardwalk's
rights-of-way, except FERC set Boardwalk's rates and nobody sets MCD's.

**[E3-03] criterion 3, put as the brief put it — who sets the price? The take-rate
series (fifteen years, filed, `mcd_series.md`):**

| | 2011 | 2015 | 2019 | 2022 | 2025 |
|---|---|---|---|---|---|
| Franchised revenues ÷ franchised sales | 12.88% | 13.48% | 12.84% | 12.89% | **12.76%** |
| Royalties ÷ franchised sales | 4.33% | 4.50% | 4.53% | 4.57% | **4.64%** |
| Rents ÷ conventional franchised sales | n/a | n/a | 11.29% | 11.30% | **11.14%** |
| Total revenues ÷ systemwide sales | 31.4% | 30.7% | 21.3% | 19.6% | **19.3%** |

**The take-rate is FLAT — and that is not the erosion case the brief feared, for a
reason the table itself supplies.** The 31%→19% headline fall is refranchising mix
(company-store dollars swapped for fee dollars), not erosion: the franchised take has
held a 12.6-13.5% band for fifteen years and royalty take has crept UP 31bp (mix toward
~5% developmental-licence royalties). The toll RATE never moved; the toll REVENUE
compounded with nominal systemwide sales — $8.7bn (2011) → $16.5bn (2025) of franchised
revenues, +4.7%/yr — because a percent-of-sales toll with contractual minimum-rent
escalators is **automatically inflation-indexed** [E4-47]. Pricing power here is not
the demonstrated ability to raise the rate; it is that the rate never needed raising
for the stream to double. Whether the flat rate is restraint or inability cannot be
decided from the filings; what the filings do show is that per-store franchisee sales
roughly doubled while the rate held — the landlord grew with the tenant, and [E3-33]
untapped power, if claimed, would rest on the franchisees' improved unit economics
bearing a higher take. That claim is NOT made here (it would require the near-monopoly
reading [E5-28]); the moat claim rests on the structure, not on unexercised increases.

**[E4-55] THE PHYSICAL SERIES — the honest one, and it convicts the U.S. lane.**
Filed U.S. guest counts: **−4.1% (2014), −3.0% (2015), −2.1% (2016), +1.0% (2017),
−2.2% (2018), −1.9% (2019)** — negative five of six last-disclosed years. Numeric
disclosure then STOPS (below). Deflated by CPI food-away-from-home, U.S. comparable
sales index 2013=100 stands at **95.4 in 2025** — twelve years of U.S. same-store
volume growth is negative; the entire nominal +50% is price. The current filing
concedes the sign: Q2-2026 10-Q — U.S. comps *"primarily driven by positive check
growth … partly offset by negative comparable guest counts."* This is Precision Steel:
dollar revenue flattered by pricing while the physical series shrinks. **The
counterweight, from the same filings:** the highway is global — systemwide sales
$85.9bn → $139.4bn (+62%), units 33,510 → 45,356 (+35%), 2025 comps positive in every
segment (US +2.1, IOM +3.2, IDL +4.6), and the licensee channel adds ~1,800 units a
year with zero MCD capital. The U.S. franchise collects a rising toll off fewer,
larger transactions; the growth engine is abroad and royalty-only.

**[E2-49] — two yardsticks withdrawn, dated:**
1. **Comparable guest counts**: numeric by-segment table in every 10-K through FY2019
   (filed 2020-02-26). FY2020 10-K: table gone, one qualitative line (*"negative
   across all segments"*) in the worst year. FY2021 on: even the definition bullet
   gone. Withdrawn AFTER five negative U.S. years in six — the yardstick was disposed
   of, not the trend. **Fires.**
2. **The Euromonitor IEO share figure**: 8% (2012 data) → 7.0% (2015) → 8.2% (2018),
   then absent from FY2022 and FY2025 10-Ks. Its own last reading was RISING, so this
   withdrawal does not follow deterioration; noted, not charged.

**[E2-45] the attacker's test.** With ample capital and skilled people, how to attack
McDonald's? Not head-on: the corner real-estate network under 45,356 restaurants
cannot be assembled at any price (the sites are occupied), the brand cannot be bought,
and per-store volumes give MCD a unit-cost and rent-coverage advantage no entrant
matches. The attacks that exist in the record are (a) the fast-casual tier (CMG) taking
the higher check — real, decade-long, and in a different price tier; (b) delivery
platforms inserting themselves — MCD co-opted them (delivery from ~41,000 restaurants,
~90% of the estate); (c) the value war with peer QSRs — margin-denting, share-neutral.
The filed share record while all three ran: IEO share 7.0% → 8.2% (2015→2018), and
franchised sales +86% over the decade. The category is savagely attacked; the record
shows the attacks landing on the CATEGORY's margins, not on MCD's share.

- Must the moat be continuously rebuilt? **Defended, not rebuilt [E4-04].** The basis
  (trademark + land + network) is not periodically replaced; advertising and remodels
  defend the same advantage, and franchisees fund most of both (franchisees are
  *"responsible for reinvesting capital in their businesses over time"* — Item 1). A
  spending lapse narrows the moat; it does not destroy the structure. Of the four
  causes [E4-36], this is extreme performance over many factors (sites + brand + scale
  + franchisee selection) compounded for 70 years — ownable, not wave-riding.
- Does success depend on a great manager? **No [E4-23]** — the Mayo test passes
  literally: the moat survived every CEO turnover including the 2019 for-cause
  termination (Q3), and [E2-53] applies: the estate, not the marketplace, sets whether
  the toll is collected.
- Primary moat metric, filing-sourced, and its trend: **return on unleveraged net
  tangible operating assets 32.7% (FY2019) → 25.0% (COVID FY2020) → 33.4% (FY2025)** —
  recovered above pre-pandemic; with the revenue-bearing head-lease ROU asset left IN
  the denominator (the honest variant for a landlord), 24.0% (FY2025). Secondary:
  franchised margin 84.2% of franchised revenues (FY2025), 84.0% (FY2023).

**THE COMPETITOR ROW — required [E3-28].** Full workpaper:
`_research 2026-09-03 MCD/competitor_row.md` (accessions there; YUM/QSR built from the
filed statements, WEN/CMG/DRI from SEC XBRL with the caveats noted). Same metric —
return on unleveraged net tangible operating assets, ORLY formula — same window (latest
FY vs five years earlier):

| Company | OI÷NTOA latest | 5 yrs earlier | Op margin | Book equity $M | Rent from franchisees | Systemwide $/unit |
|---|---|---|---|---|---|---|
| **MCD** | **33.4%** (24.0% ROU-in) | 32.7% (FY2019; COVID FY2020 25.0%) | **46.1%** | **−1,791** | **$10,442M** | **$3.07M** |
| YUM | 85.1% | 68.1% | 31.3% | −7,325 | ~$103M | $1.08M |
| QSR | 92.8% | 62.6% | 23.3% | +5,159 | $832M | $1.42M |
| WEN | 19.1% | 16.9% | 15.8% | +117 | ~$235M (last tagged FY2022) | n.p. |
| CMG | 75.2% (~26% ROU-in) | 17.9% (COVID) | 16.2% | +2,831 | none (0% franchised) | n/a |
| DRI | 29.0% (understated — trademarks untagged) | 22.1% | 12.0% | +2,208 | none | n/a |

- Peers named: **5** of an industry that has more filers than eight (SBUX, DPZ, JACK,
  PZZA, EAT sit outside this row); five were taken as the brief named them and the count
  is stated. No named peer unavailable — no PROVISIONAL.
- **The row must be read with [E3-61]'s limit, and here the limit bites the METRIC:
  YUM's 85% and QSR's 93% do not out-moat MCD — they measure NOT OWNING the moat
  asset.** The asset-light franchisors carry the brand on the balance sheet as acquired
  intangibles (QSR: $11.2bn, subtracted by the formula) and own almost no restaurants
  (YUM: ~400 owned/leased-out sites of 63,285); MCD deliberately holds $28.2bn of net
  P&E — the land under the toll booth — inside the denominator. The like-for-like reads
  are the **operating margin row (MCD 46.1% — first by 15 points)**, the **per-unit
  volume row (MCD $3.07M — 2.2-2.8x the franchised peers, [E2-53] dominance made
  physical)**, and the **rent row: no peer's franchisee-rent stream is within a factor
  of TWELVE of MCD's $10.4bn.** The structure the brief asked about — royalty PLUS rent
  on owned land with 20-year sunk-cost tenants — exists nowhere else in the field.
- **What the negative equity does to the metric (the ULTA/BBWI ruling, applied):**
  MCD's −$1,791M and YUM's −$7,325M are buyback artifacts; NTOA does not touch equity
  or debt, so the returns above are not leverage-inflated — demonstrated inside the row
  by YUM carrying 4x MCD's equity deficit on the same structure. The goodwill wedge
  (MCD $3,354M, 5.6% of assets) is reported, not hidden.
- **Untapped pricing power [E3-33]:** not claimed. The take-rate series is flat by
  fifteen years of record; claiming the franchisees could bear a higher toll would
  require the near-monopoly reading [E5-28] and is not needed for the verdict.
- Class: **[x] WIDE — as a franchisor** (the business being valued: contracted rent +
  royalty on owned corners, tenant switching costs structural, no peer analogue) ·
  **with the consumer-level erosion channel NAMED: the U.S. physical series** (real
  comps 95.4 on 2013=100; guest counts negative in every disclosed year since 2017,
  disclosure withdrawn FY2020, negative again by the filer's words in H1-2026).
  · Direction [E4-32]: **widening internationally** (units +35% in nine years, licensee
  capital, loyalty scale), **narrowing in U.S. physical terms** — the Q6 monitoring
  metric is exactly this series.
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *The brief's [E4-26] framing answered: IN, and WIDE rather than NARROW — but WIDE
  about the franchisor structure, not the burger. The "toll road on a shrinking
  highway" case fails on the filed record because the highway is global and growing
  (+62% nominal systemwide, +35% units) and the toll is inflation-indexed by contract;
  what IS shrinking, in real terms, is same-store volume in the largest market, and
  that is recorded as the moat's erosion channel, not its refutation.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is a qualitative OVERLAY.** This is the [E3-43] franchise case
exactly: a percent-of-sales toll collected from 43,317 restaurants run by other people
tolerates mismanagement; the business ran through a for-cause CEO termination (below)
without a ripple in the fee stream. On leverage: book equity is **−$1,791M** and total
debt ~$40bn, but this is not the [E3-29] case — that gate is for balance sheets (banks,
20:1) where small ASSET errors destroy the firm. MCD's negative equity is an artifact
of $79.3bn of treasury stock bought against a $185bn market value; interest is covered
7.8x by operating income and the asset side is land, buildings and contracted
receivables. Leverage is weighed at Q4, where it belongs. **Case declared: OVERLAY.**

**Honesty — binary, permanent, filings-based [E5-16].** Dated to when public:
- **2019-11-04 (8-K):** CEO Easterbrook terminated over a relationship violating
  company policy; separation agreement dated 2019-10-31, treated as "without cause."
- **2020-08:** after a July 2020 internal investigation found undisclosed further
  misconduct, the company SUED its former CEO to recover the severance.
- **2021-12:** Easterbrook returned the compensation (separation value the SEC puts at
  "more than $40 million"; the returned equity and cash were reported at ~$105M).
- **2023-01-09 (SEC order):** Easterbrook charged with fraud — $400,000 penalty and a
  five-year officer/director bar. **McDonald's itself was charged under Section 14(a)
  and Rule 14a-3** for not disclosing the discretion it exercised in treating the
  termination as without cause; the SEC imposed **no penalty "in light of the
  substantial cooperation"** including voluntary disclosure beyond what was requested.
- Reading under [E5-22] (penalty size is not seriousness; the failure that counts is
  *"they didn't act when they learned"*): the board acted when it learned (fired him),
  acted harder when it learned more (sued, recovered), and self-disclosed. The 2019
  disclosure failure is the company's own conduct matter on the record — a proxy
  disclosure violation, remediated, no restatement, no earnings contamination. The
  binary judges today's management (Kempczinski, CEO since 2019) on conduct since:
  **no disqualifier found.**

**STEP 2 — THE FLAGS [E4-22, E5-15].** *Each a prompt to read, never a verdict.*
- [ ] weak accounting — none found: SBC expensed, pension exposure immaterial, revenue
  recognition plain (cash-basis sales, %-of-sales fees).
- [ ] unintelligible footnotes — the opposite; the franchise and lease notes are models
  (contracted rent schedule published to the dollar).
- [x] trumpeted growth targets — **partial**: no EPS guidance culture [E5-30 does not
  fire], but the 10-K carries operational targets ("50,000 restaurants by the end of
  2027... the fastest period of restaurant unit growth in Company history"; 250M loyalty
  users; $45bn loyalty sales by 2027). These are unit/system targets, not earnings
  numbers "to make"; noted, not charged.
- [ ] serial share issuance — none: shares issued fixed at 1,660.6M since at least 2022;
  count falls every year (treasury 950.0M).
- [ ] **EBITDA [E4-29]: ZERO occurrences in the FY2025 10-K and ZERO in the DEF 14A.**
  Does not fire — rare in this queue. The non-GAAP measures used (constant currency,
  free cash flow, ROIC) are reconciled and long-standing [E2-49 does not fire on the
  headline metrics: comparable sales, systemwide sales, ROIC, FCF conversion are the
  same measures across every vintage read back to FY2013].
- [x] filed-figure tells [E4-30]: income taxes paid, net, **$2,688M FY2025** (incl.
  $429M of purchased Federal transferable energy credits) vs provision $2,334M, and
  "$3.0 billion" paid in each of 2024 and 2023 vs provisions of $2,121M/$2,053M — cash
  taxes AT or ABOVE the book provision every year; no falling-cash-tax tell. Reported net income moves with real events
  (−3% in 2024). Does not fire. *(The one [E2-49]-adjacent item is at Q2: guest-count
  disclosure withdrawn FY2020; charged there.)*
- Restructuring [E3-53]: "Accelerating the Organization" charges three years running
  ($250M/$221M/$226M, $697M total, ~$250M more guided for 2026, completion 2027) —
  a rolling multi-year program under a growth-strategy name. Disclosed and quantified
  every year, every line [E2-26 pass]; **but the STIP excludes restructuring from the
  operating-income metric it pays on — management is paid as if the recurring
  transformation cost were not real [E5-33]. FLAG, the one genuine pay flag found.**
  Treatment: the charges stay in the owner-earnings mean at Q4; the flag reads on
  candor, not honesty.

**STEP 3 — THE PRIMARY TEST [E2-01].** Equity capital employed is **negative (−$1,791M)**
— the literal ratio is meaningless, and [E2-43] directs the unleveraged net tangible
denominator (the ULTA/BBWI ruling; the goodwill wedge $3,354M reported separately, not
hidden). Return on unleveraged net tangible operating assets: **32.7% (FY2019) → 25.0%
(FY2020) → 33.4% (FY2025)**; with the revenue-bearing head-lease ROU asset kept in the
denominator, 24.0% (FY2025). Operating income series (filed): 7,745 (2016, charge year)
→ 9,553 → 8,823 → 9,070 → 7,324 (COVID) → 10,356 → 9,371 → 11,647 → 11,712 → **12,393
(2025)**. High, stable, recovered above pre-pandemic on a smaller equity base each year.
Balance sheet before income statement: the equity deficit is a FINANCING choice (below),
not an operating fact.

**The half-owner test [E2-26]:** passes with one exception. Charges and gains are
quantified separately at every line, restated GAAP-first (2025: $229M net charges shown
against both GAAP and non-GAAP EPS); segment detail down to occupancy cost per segment;
the contracted rent schedule published. The exception is the STIP restructuring
exclusion above — and the guest-count withdrawal charged at Q2.

**The institutional imperative — score all four [E2-30].**
- [ ] resists change — no: refranchised ~4,000 stores 2015-2018 (company-op 6,738 →
  2,039), sold Russia (2022) and South Korea (2024), bought Israel back (2024) —
  the perimeter moves when the case moves.
- [ ] projects to soak up funds — capex is rising ($2.4bn → $3.4bn → guided $3.7-3.9bn
  and another +$300-500M in 2027) but into named unit growth with licensees funding
  1,800 of 2,600 openings; not soak-up-shaped. Watched, not scored.
- [ ] staff studies for the leader's craving — none visible.
- [ ] peer imitation — no: the owned-real-estate model is the OPPOSITE of the sector's
  asset-light refranchising orthodoxy (peer row), and MCD kept it through a decade
  when "REIT spin-off" was the activist demand on this exact stock.
- **Score: 0 of 4.**

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds for operations and liquidity? Yes on flow ($10.6bn OCF vs $3.4bn
  capex), thin on stock ($774M cash — Q4).
- (2) material discount to conservatively calculated IV? **The 2025 average repurchase
  price was ~$301/share ($2,016M for 6.7M shares) against this run's judged
  zero-growth value of ~$230-300 (Q5): repurchases ran AT or ABOVE the conservative
  case, not at a material discount. CAPITAL-ALLOCATION FLAG**, stated with [E4-13]'s
  humility clause: this rests on our own IV range and management knows the business
  better. Two mitigants on the record: the pace CUT as the price rose ($5.2bn 2018 →
  $2.1bn 2025 — the opposite of the ORLY dollar-budget pattern), and dividends (raised
  every year; $7.44/sh annualized, ~2.85% yield) took the larger share. **The flag
  binds position size, never the discount rate.** [E2-60] (payouts vs owner earnings
  vs new debt) is computed at Q4 and FIRES for the 2014-2019 program; 2020-2025
  payouts ran roughly WITHIN owner earnings.

**THE GUARDRAIL — checked.**
- [x] Nothing here promotes the name; Q2 stands on the structure, Q4/Q5 on the numbers.
- [x] No great-manager requirement — recorded at Q2 that the moat survives any CEO
  [E4-23, E2-53].
- [x] No excisable-cancer case is being made; the manager is not the plan.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *IN = no disqualifier found [E5-17], with two recorded flags: the STIP restructuring
  exclusion, and buyback condition-2 (binds position size). The 2019-2021 Easterbrook
  matter was the PREDECESSOR's misconduct, refused and recovered by the board; the
  company's own 14(a) charge (2023, no penalty, cooperation) is on the record. IN never
  promotes.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** All four windows,
both capex ends, from the verified filed series (`mcd_series.md` §6; OE = OCF − SBC − (c)):

| Window | mean(OCF−SBC) | (c)=capex | (c)=D&A | OE range | Yield on $184,659M |
|---|---|---|---|---|---|
| 3-yr 2023-25 | 9,699 | 2,832 | 2,091 | **6,867 – 7,608** | 3.72% – 4.12% |
| 5-yr 2021-25 | 9,064 | 2,487 | 2,003 | **6,577 – 7,062** | 3.56% – 3.82% |
| 7-yr 2019-25 | 8,501 | 2,353 | 1,912 | **6,148 – 6,589** | 3.33% – 3.57% |
| 10-yr 2016-25 | 7,771 | 2,289 | 1,774 | **5,482 – 5,997** | 2.97% – 3.25% |

- **Combined range: $5,482M to $7,608M** (38.8% width off the bottom); **spread,
  conservative end (10-yr vs 5-yr capex construction): −16.6%.**
- *Too wide to conclude?* **No — every construction lands on the same side of the
  sovereign (all below 5.27%), so the width cannot change the Q5 outcome** (the ORLY
  precedent).
- *The distorted years, named [E5-11]:* the 10-yr window mixes in the refranchising-era
  perimeter (5,669 company stores in 2016 vs 2,039 today — OCF structurally lower then)
  and the 2020 pandemic year; both bias the long window DOWN. The representative
  business is the 3-to-5-yr fee-stream company. [E4-41] the other way: no favourable
  exogenous break inflates the recent mean — 2025's working-capital benefit was +$106M
  net, and ~$225M/yr of restructuring cash cost sits IN the mean, guided to continue
  through 2027 [E5-33].
- Owner earnings by year (capex end): 4,108 · 3,580 · 4,100 · 5,618 · 4,532 · 6,962 ·
  5,321 · 7,080 · 6,500 · 7,021 (2016→2025).
- **Maintenance capex — the (c) judgment [E2-23]: D&A default VALID; judged (c) ≈
  $2.0-2.2bn.** This is NOT the [E5-20] exception class: nothing in the filing says
  depreciation understates renewal; capex/D&A is 1.53x because capex is *"mainly
  allocated to new restaurant openings"* (FY2025 MD&A — ~2,300 openings; the FY2022
  vintage split its $1.9bn *"approximately 50% to each"* of existing vs new, the
  DG-style measured split), and the franchisees bear site maintenance (*"Franchisees
  generally pay related occupancy costs including property taxes, insurance and site
  maintenance"*) and *"are responsible for reinvesting capital in their businesses over
  time."* D&A on MCD's rent-earning buildings is a real renewal cost of the rent
  stream; existing-restaurant capex when disclosed ran BELOW D&A. **Judged OE:
  ~$7,000M** (5-yr window at the D&A end 7,062; 3-yr 7,608; 7-yr 6,589).
- **ASC 842 tested hardest, as instructed — and for the FIRST time in eight runs it is
  NOT immaterial:** finance-lease ROU **$2,168M**, liability **$2,352M**, wavg
  remaining term **28 years**; 2025 lease-financed additions **$468M finance + $765M
  operating ROU** obtained — capital deployed OUTSIDE the capex line (≈14% of capex on
  the finance side alone), with only ~$68M/yr of principal repayment visible in
  financing. These are head-lease sites that then EARN franchise rent (leased-site
  minimum rents receivable $15.6bn vs total lease payments owed $20.6bn) — growth
  assets, lease-financed. Treatment: (c) is not raised (the additions are new-unit
  growth), but leverage below counts the $14.8bn lease stack in full.
- Stock compensation subtracted in full every year **[E5-06]** ($165M in 2025); SBC is
  RSU/option-based and the reported charge is taken as the floor [E3-70] — at 1.6% of
  OE it cannot move a verdict.
- Look-through [E3-04]: China (48%) and Japan (35%) equity earnings $190M sit in
  operating income but only their dividends sit in OCF; the undistributed increment
  (≤$190M) is NOT added — conservatism spent once, stated. **Windage count: 1.**
- *Capex band changes the verdict?* No — see Q5: every end of every window is below
  the sovereign.

### Great, good, or gruesome? **[E4-20]**
- [x] great on the franchised stream — a percent-of-sales toll, inflation-indexed,
  84% margins, licensees fund ~70% of new units with their own capital
- [x] good on the owned-unit growth program — MCD's own $3.4bn (guided $3.7-3.9bn)
  of capex earns the ~33% NTOA return also on added deposits [E4-43: nothing shabby]
- Evidence: operating income $7.7bn → $12.4bn on net P&E $21.3bn → $28.2bn over nine
  years; returns held ~33% while capital was added. Not gruesome on any reading.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings — **PASS, the strongest in this queue's
  history**: $31,451M of CONTRACTED minimum rent receivable, royalties on $139bn of
  systemwide sales from ~5,000 franchisees/licensees across 100+ countries; COVID
  trough OCF was still $6.27bn and the dividend was raised through it.
- (2) massive liquid assets — **FAIL**: $774M of cash against $4,361M of current
  liabilities; the liquidity backstop is a revolver, and $1.5bn of commercial paper is
  classified long-term only because it is *"supported by a long-term line of credit
  agreement expiring in June 2028"* — **[E5-39] refuses to count bank lines.** A
  deliberate lean-treasury policy on a fee stream, but the test is the test.
- (3) no significant near-term cash requirements — **PASS on the filed schedule**:
  long-term debt maturities **2026: $0**; 2027: $3,201M; 2028: $5,166M — against
  ~$7.2bn of free cash flow; the sole near-term call is the $1.5bn CP (flagged at (2)).
  Distinguished from UAL's contractual $18.3bn wall.
- Leverage, named and quantified **[E4-16]**: total debt **$39,973M** + lease
  liabilities **$14,840M** (op 12,488 + fin 2,352) against equity of **−$1,791M**;
  interest paid $1,555M covered **7.8x by operating income and 4.6x by OCF−capex —
  [E2-54]'s coverage test passes with the capex taken out first.** Fixed-rate ~95%,
  multi-currency ($15.6bn foreign-denominated as net-investment hedge). The corpus
  supplies no ratio and none is invented; the judgment: this stack is carried by the
  most contracted revenue stream in the queue, and it was built to buy in shares, not
  to run restaurants — which is where [E2-60] bites:
- **[E2-60] — restricted earnings, computed:** ten years 2016-2025: buybacks
  **$39,603M** + dividends **$39,343M** = **$78,946M paid out against $54,822M of
  owner earnings (capex end)** — an excess of **$24.1bn**, funded by **+$13,973M of
  debt** (26,000 → 39,973) plus refranchising/disposal proceeds. **FIRES for the
  decade: the equity deficit is the payout program made visible, and (c)'s third
  dimension (financial strength) was spent.** Last five years: payouts $35,280M vs OE
  $32,884M, debt +~$2.5bn — the program now runs roughly AT owner earnings, mildly
  over. Recorded at Q3 as the condition-2 flag; binds position size.
- Stage 0 by hand (brief items): cover count **707,641,531** ✓; dividend streak
  decomposition (RPM/ITW test): DPS $3.61 (2016) → $7.17 declared (2025), +7.9%/yr,
  decomposes as **net-income growth +6.9%/yr + share retirement ~1.5%/yr − payout-ratio
  drift (65.2% → 59.7%)** — the streak is EARNINGS-funded with retirement assistance,
  not payout-ratio expansion. Clean.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: **the toll road's cars — a real-traffic decline that goes global and
  permanent while the leverage stays.** The U.S. lane already shows it (real comps
  95.4 on 2013=100; guest counts negative in every disclosed year but 2017). If check
  growth stops covering traffic decline system-wide, a %-of-sales toll shrinks in real
  terms against $40bn of fixed-rate debt and a $5bn+ dividend constituency. The
  second exposure [E4-40], from the filer's own risk factor: a single brand on 100% of
  the system — *"food safety events … have occurred within … our System from time to
  time"* — one contamination catastrophe hits every restaurant at once, executed
  day-to-day by ~5,000 independent operators MCD does not control.
- Quantified from filed figures: model five years of ZERO nominal systemwide growth
  with 3% cost inflation — franchised revenues flat $16.5bn; SG&A +$480M; company-op
  margin −200bp (−$190M); refinancing the ~$11.8bn maturing through 2029 at +150bp
  (+$180M): operating income falls to ~$11.5bn, interest ~$1.76bn, **coverage still
  6.5x; the dividend ($5.1bn) still covered ~1.4x by conservative owner earnings.**
  The 2020 stress test is on the record: OCF fell to $6.27bn, capex was cut to
  $1.64bn, the buyback to ~$0.9bn, the dividend was PAID AND RAISED, and debt rose
  ~$3.3bn — absorbed without strain. A repeat **"would not distress us"** [E3-24].
  Death requires a DECADE of global real decline met with unchanged payouts — visible
  years out in the systemwide series.
- Likelihood: [ ] likely [ ] a real possibility [x] **a low-level possibility** (the
  U.S. real-traffic decline itself is FACT; its going global and outrunning the
  check+units engine is the low-level possibility).
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: **7.6% – 9.2%** (owner-earnings yield 3.56-4.12% on the
representative windows, judged 3.79%, plus realised growth of 3.8%/yr [OE, capex end,
2019-25] to 5.3%/yr [operating income, either the 6-yr or 9-yr base]). **Below the ~10%
floor on every construction: the name is quit on, not ranked** — whatever the sovereign
is. Even the most generous pairing (3-yr D&A-end yield 4.12% + 5.4% growth) reaches
9.5%.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings **$7,000M judged** ($5,482M-$7,608M across four windows and the capex
  band) ÷ market cap **$184,659M** = **3.79%** (range 2.97%-4.12%) · sovereign **5.27%**

**2. WHAT THE PRICE ALREADY ASSUMES**
- year-1 growth needed to justify the quote against the bare bond: **+1.48%** perpetual
  (range +1.15% to +2.30%) — *achievable, and the strongest thing that can be said for
  this price*
- growth needed to clear the [E4-28] floor: **+6.2%** perpetual (range +5.9% to +7.0%;
  the screen's 6.60% reproduced and adjudicated)
- what the business has actually done: **+3.8%/yr** (owner earnings, capex end,
  2019→2025) to **+5.3%/yr** (operating income, 2016→2025 and 2019→2025 alike);
  systemwide sales +4.8%/yr (2019→2025)

**3. WHAT YOU ARE PAID**
- return at the current price = **−1.48 points UNDER the sovereign** (−1.15 to −2.30
  across constructions) before any growth; with realised growth credited, 7.6-9.2%
  against a 5.27% bond — paid over the bond only by growth that must persist for
  decades [E4-44], and still under the floor

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.27%** — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero-growth capitalisation of owner
earnings at the bare sovereign (the growing-perpetuity form is refused here: with
realised growth 3.8-5.3% against a 5.27% rate the denominator goes degenerate — the
Tinker Bell trap [E4-44]; the convergent cross-check is the floor rate with mid growth,
7,000×1.045/(0.10−0.045) ≈ $133bn, which lands INSIDE the sovereign zero-growth range):
- conservative **~$150-175/sh** (7-yr and 5-yr capex-end constructions at 5.27%) ·
  judged **~$185-190/sh** ($7,000M ÷ 5.27% = $132.8bn ÷ 707.64M sh) · optimistic
  **~$205-215/sh** (3-yr D&A end, look-through increment) · at the [E4-28] floor rate:
  **~$95-110/sh** · **current price $260.95** (2026-09-02 close)
- **The price sits ABOVE the whole range** — ~1.4x the judged value, ~1.2x the top.

**THE FLOOR, THEN THE RANKING [E4-28, E3-45].**
- honest pre-tax expectancy: **7.6-9.2% — below the ~10% floor: QUIT ON, NOT RANKED.**
- points over sovereign, this name: **−1.48 on the yield**; +2.3 to +3.9 with growth
  credited — for the record only, since the floor closes the file.
- against the rest of the opportunity set: had the floor not governed, this would rank
  alongside BRK-B (6.7-9.7%) and above ORLY (7.1-8.7%) — **the best business economics
  yet to reach Q5 in this queue, failing on price exactly as they did.**

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [x] **Screamer test [E4-01]** — does the price already clear the conservative case?
      **Price $260.95 is above the WHOLE range ($95-215) → the third outcome: no.**
      No margin added on top.
- **Windage count: 1** — the look-through increment (≤$190M) excluded from judged OE;
  (c) sits at the corpus DEFAULT (D&A), not the conservative end, and the judged
  window is the representative 5-yr, so conservatism is spent exactly once. **[E4-11]**

- **VERDICT: [ ] IN — **FAIL AT Q5, ON PRICE** · [ ] UNRESEARCHED · [ ] UNKNOWABLE ·
  ranking position: **not ranked — quit on at the [E4-28] floor.** All four business
  gates returned IN; the price alone closes the file.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

*No position exists or is opened — the file closed at Q5. Q6 is filled as the
pre-committed re-entry and monitoring card [E1-02], because this is the rare name whose
four business gates all returned IN.*

**Pre-committed before any entry [E1-02]:**
- Thesis-confirming metric: systemwide sales growth ≥ ~4%/yr nominal with unit growth
  ~2%+; franchised take-rate holding ≥12.5% of franchised sales.
- **Thesis-breaking metric and its threshold:** the Q2 erosion channel going global —
  total-company comparable sales below FAFH-class inflation (real comps negative) for
  two consecutive years OUTSIDE the U.S. as well as inside it; or the franchised
  take-rate slipping below ~12% (toll cut to defend the base).
- **Re-entry price, pre-committed:** the judged value band **~$185-190/sh** at today's
  5.27% sovereign (recompute against the sovereign of the day; the OE base moves with
  each 10-K). At ~$185 the honest expectancy is ~9.5-11%, at/over the floor.
- Next catalyst date: FY2026 10-K (~2027-02) — watch: capex step-up to $3.7-3.9bn +
  guided 2027 increase vs whether OE grows through it; the 50,000-unit 2027 target;
  any return of numeric guest-count disclosure [E2-49 reversal would be a candor
  upgrade].

**The sell rule [E2-28]** — n/a (no holding). The two Q3 flags carry forward: STIP
restructuring exclusion; buyback condition-2 (repurchases at ~$301 average in 2025,
above the judged value — sized-down rule would apply to any future position).

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring
question, put concretely for MCD: is the U.S. real-traffic decline an aberrational
cycle of price-led inflation recovery, or has the consumer franchise slipped in a way
that permanently reduces intrinsic value? The filed record says it is at least a
decade old and disclosure was withdrawn rather than the trend arrested — slow to
conclude, but the conclusion direction is already visible; fast once concluded [E2-40].

- **VERDICT: [x] IN** *(as a monitoring card; no position)*

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN → Q2 IN → Q3 IN → Q4 IN →
  Q5 FAIL on price → Q6 filled as monitoring card)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The
  known gaps are stated as gaps, none load-bearing: WEN systemwide sales not pulled
  (row note); DRI trademark intangibles untagged (understates DRI, direction
  unaffected); no renewal-rate disclosure exists (absence claim from a recorded sweep
  of seven 10-K vintages).
- [x] No UNRESEARCHED verdicts issued
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: 10-K FY2025 read (MD&A, cash-flow incl. detail lines, footnotes),
  accession 0000063908-26-000035; OCF series cross-checked to the filed statement
- [x] Owner earnings on multi-year means; FOUR windows displayed; capex band disclosed
  as a judgment with the filing-cited reason ((c)=D&A default valid; franchisees bear
  site maintenance; capex is mainly new units)
- [x] Competitor row filled (5 peers; YUM/QSR from filed statements, WEN/CMG/DRI from
  SEC XBRL with caveats stated in the workpaper)
- [x] Sovereign 5.27%, USD, US Treasury daily par yield curve (issuing authority),
  2026-09-02
- [x] Value stated as a round-number range ($150-175 / ~$185-190 / $205-215; floor
  ~$95-110)
- [x] One bar (screamer test); windage count 1, stated
- [x] Price $260.95 dated 2026-09-02, aggregator, flagged as live-quote-only
- [x] Run committed to git after every question (write-early protocol followed;
  session killed twice, zero questions lost)

**Tool defects found this run (operator rule 6):**
1. `tools/run.py` D&A tag-pick takes the FIRST resolving element; on MCD that is a
   $457M subcomponent vs the $2,199M filed total — already fixed in
   `floor_screen.da_annual()` (2026-09-01) but STILL LIVE in run.py, which also
   returned shares 0.0M (dei absent) and yields in the millions of percent.
2. The ASC 842 "immaterial" streak (seven runs) ended here exactly as the brief
   predicted: $2.35bn of finance-lease liabilities, $468M of 2025 lease-financed
   additions outside the capex line. Any tooling that reads only
   `PaymentsToAcquirePropertyPlantAndEquipment` understates MCD's capital deployment
   by ~14%.

## REGISTER
- Verdict: [x] **FAIL AT Q5, ON PRICE** (about the price, not the business: Q1-Q4 all
  IN — the third name in queue history to clear all four gates, after ORLY and BRK-B)
- One line: **A genuine franchise — the only rent-plus-royalty structure in its field,
  $31.5bn of contracted minimums on land it keeps at every expiry — priced at 1.4x its
  judged value: honest expectancy 7.6-9.2% against the ~10% floor; quit on, not
  ranked.**
