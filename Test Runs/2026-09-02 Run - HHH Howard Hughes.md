# Company Run — Howard Hughes Holdings (HHH) — 2026-09-03
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs. **Sector method applies to PART
of this company** per the Stage 0(b) ruling of 2026-09-02 (run queue): the insurance leg
only, under `Framework/SECTOR METHOD - …` with both amendments. The two-business method
(CONVENTION 3, the HOG/L precedent) governs the whole.

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
- rate **5.27%** · date **2026-09-01** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority, via `tools/sources.py`)**
- FX: none needed for the quote — USD quote, USD functional currency. **But note the
  sector-method Finding-8 exposure in miniature:** the 10-Q states "The U.S. dollar is the
  functional currency of the Company and its subsidiaries. Vantage occasionally transacts
  business in foreign currencies" — Vantage's Bermuda subsidiary writes worldwide, so some
  premium is non-USD before translation. Stated per the amendment; USD sovereign used; the
  choice is the reporting currency's and is disclosed as unresolved method-wide.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- documents · dates · accession nos.:
  - **10-Q Q2-2026** (period 2026-06-30), filed 2026-08-05, **0001628280-26-053324** — read
    in full: balance sheet, operations, equity, cash flows, Notes 1-19
  - **10-K FY2025** (period 2025-12-31), filed 2026-02-19, **0001628280-26-009710**
  - **8-K** (closing), event 2026-06-04, filed 2026-06-05, **0001104659-26-071029**
  - **8-K/A** (Vantage audited financials + pro formas), filed 2026-07-15,
    **0001104659-26-083909** — ex-23.1 auditor consent, ex-99.1/99.2/99.3
  - **DEF 14A**, filed 2026-08-19, **0001104659-26-098808**
- figure cross-checked against the filed statement: **total consideration for Vantage
  $2,099,992k per Note 2 of the 10-Q ties to the closing 8-K's "$2.1 billion" and to
  "Acquisition of business, net of cash acquired $(1,639,220)k" on the filed cash-flow
  statement ($2,100.0M less $376.3M cash and $84.5M restricted cash acquired = $1,639.2M —
  ties exactly).** Series A preferred proceeds $997,353k (cash-flow statement) ties to
  $1.0bn gross less $4.2M issuance costs (Note 3), balance-sheet carrying $995,764k.

---
## STAGE 0 — THE ARTIFACT CHECK (sector method, both amendments)

**(a) Share count BY HAND off the cover.** The 10-Q cover (2026-08-05): *"The number of
shares of common stock, $0.01 par value, outstanding as of July 29, 2026, was
59,721,036."* Single class of common. `cover_shares.py HHH` returns the same 59,721,036 —
tool and hand agree. Balance sheet: 66,253,546 issued less 6,596,484 treasury =
59,657,062 at 6/30; the cover count is later and governs.
**Instruments issued around the Vantage deal — all three found, none in the common count:**
1. **Series A Non-voting Exchangeable Perpetual Preferred, $1.0bn** (140,000 shares at
   $7,142.86), issued 2026-06-04 to Pershing Square Holdings, Ltd. — **mezzanine equity**,
   $995.8M carrying. Exchangeable from FY2032 year-end into up to **49% of Vantage Units**
   (the insurance subsidiary's common equity), NOT into HHH common. Company call each year
   from FY2026 at the **greater of** cost + 4% compounded **or 1.5x Vantage book value
   excluding acquisition goodwill/intangibles**, times the as-exchanged ownership.
   Dividends discretionary, noncumulative, capped at what Vantage passes up.
2. **Warrants to a director**: April 2026, Marc Grandisson (board member) bought warrants
   on **1,131,273 common shares, strike $100**, for $10.0M; exercisable April 2030, expire
   April 2031 (10-Q Note 14). ~1.9% potential dilution, out of the money at today's price.
3. **May 2025: 9,000,000 new common shares to Pershing Square Holdco at $100/share**
   ($900M gross, $862.9M net booked) — in the count already. Pershing Square beneficial
   ownership: **~46.7% of common** at 6/30/2026 (10-Q Note 3).

**(b) Is it an insurer, a float-bearing holding company, or neither?** — the 2026-09-02
queue ruling **VERIFIED against the filings**: HHH is **float-bearing as of 2026-06-04**.
10-Q Note 2: Howard Hughes Insurance Holdings, LLC completed the acquisition of 100% of
Vantage Group Holdings, Ltd. for **$2,099,992k cash** on **June 4, 2026** (Purchase and
Sale Agreement dated 2025-12-17; sellers Carlyle and Hellman & Friedman vehicles).
**26 days of filed insurance history under HHH** (June 4-30). The 10-Q describes the whole:
*"HHH … is a holding company that owns subsidiaries engaged in various diverse business
activities"* — a real-estate development subsidiary (MPCs, strategic developments,
operating assets) **plus** *"a specialty insurance and reinsurance subsidiary."*

**Both Stage 0(b) ratios, as the amendments require:**
- **Constructed float (CONVENTION 4), at the acquisition date** from the Note 2 PPA:
  reserves for claims $2,090.2M + unearned premiums $1,384.4M − reinsurance recoverable
  $599.1M − premiums receivable (acquired AR) $788.7M − DAC $0 (reset in acquisition
  accounting) = **$2,086.8M**; netting also the acquired prepaid reinsurance premiums
  (ceded unearned, inside acquired other assets; $435.2M at 6/30 on the consolidated
  sheet) gives **~$1,652M**. Both stated; the construction is shown, not cited.
- **Float ÷ investments**: acquired investments at 6/4 = fixed maturities $2,608.3M +
  short-term $32.8M + cash $376.3M + restricted $84.5M = $3,101.9M →
  **float/investments ≈ 53-67%** (by prepaid-reinsurance treatment) — **ABOVE Berkshire's
  41.8% calibration.** Unlike WTM (22%), the insurance leg is genuinely float-funded;
  step 2 is NOT a minor term for the leg. For the CONSOLIDATED company, insurance
  investments ($1.35bn securities at 6/30 after the repositioning, plus insurance cash)
  sit inside a $15.9bn balance sheet — the leg is ~40% of total segment assets ($6.3bn).
- **Investments ÷ equity (CONVENTION 5)**: insurance securities $1,352M ÷ total HHH
  stockholders' equity $3,960M = **0.34x consolidated** (vs BRK 0.45x, MKL 2.01x) — but
  against the insurance sub's own capital (net assets acquired $1,820M + the $1bn
  preferred injection) it is ~**1.1x at the acquisition-date portfolio ($3.1bn)**. The
  gross-counting condition [E5-46] — "free as long as underwriting breaks even" — rests
  here on **26 days** of HHH-filed underwriting history.

**Perimeter statement (the reason this run is careful):** every perimeter class at once —
the acquisition sits inside any owner-earnings window; the filed history (FY2016-FY2025)
describes an MPC developer the cap no longer prices alone; the insurance leg has 26 days
of filed history under HHH against [E3-69]'s "period of years," so its cost of float can
come only from **Vantage's own pre-acquisition audited statements** (8-K/A of 2026-07-15,
ex-99.1/99.2) — obtained, see Q4 — or the leg is UNRESEARCHED.

**Post-acquisition fact recorded at Stage 0 because it recolors everything downstream:**
in the 26 days after closing, the company **sold $2,335.8M of Vantage's $2,608.3M
fixed-maturity book** (Note 4: *"the Company intends to reposition Vantage's investment
portfolio to include cash, short-term U.S. Treasury securities, and publicly traded equity
securities"*) and bought **$1,113.5M of equity securities**, managed by Pershing Square
under investment management agreements signed at closing. The insurer's asset side is
being converted from an insurer's bond book into a Pershing-managed equity portfolio.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language — the parts first, because the
parts ARE writable:**

*The land business.* HHH owns roughly 98,000 gross acres across five master planned
communities (Summerlin/Las Vegas, The Woodlands + Bridgeland + Woodlands Hills/Houston,
Teravalis/Phoenix), nearly all entitled, carried at a basis set years to decades ago
($2.65bn of MPC assets on the books against 19,808 remaining saleable residential acres
the company itself prices at $391k-$1,719k/acre and 12,984 commercial acres). Each year it
spends on roads, sewers, and utilities to convert raw acres into finished superpads and
lots, sells them to homebuilders (FY2025: 620.5 residential acres at an average $890k),
and books projected cash margins of 81-96% because the land cost is historic. The rooftops
it creates generate demand for its own commercial parcels; it builds offices, retail, and
apartments on them (9.3M sq ft + 5,855 units generating ~$270M/yr of NOI), and in Hawai'i
it builds condo towers that are 96-99% pre-sold before completion, with buyer deposits
carrying much of the construction. The cycle repeats until each community sells out —
filed sell-out dates run from 2031 (Woodlands) to **2086 (Teravalis)**. This paragraph was
easy to write. **The brief's prior — that Q1 might fail on the difficulty of understanding
the land model — is WRONG, and is recorded as a brief defect: the MPC engine is one of the
most transparent long-duration models in the filing population.**

*The insurance business.* Vantage is a 2020-vintage Bermuda/US specialty insurer and
reinsurer: $1.6bn gross premiums written, ~$1.2bn net, writing casualty, property,
professional lines and property-cat retro, at a combined ratio of ~102% (FY2024) to ~95%
(FY2025) — roughly break-even underwriting funding a float we construct at ~$1.4bn. Its
reserves are five accident years old and two-thirds unpaid; its earnings are mostly
investment income on a portfolio the new owner is converting from bonds to equities.

*The holding company.* Pershing Square (46.7% of common) advises under a ten-year
self-renewing Services Agreement; the declared program is to keep buying operating
companies with real-estate cash flow and insurance float.

**The scarce input the business controls:** for the land leg, genuinely scarce and
genuinely controlled — entitled contiguous acreage inside supply-constrained growth
corridors, with the entitlement processes "substantially completed" (the 10-K's words).
For the insurance leg, [E2-70] answers: *"Their only products are promises… There are no
important advantages from trademarks, patents, location…"* — nothing scarce. For the
holding company: Pershing Square's judgment, which is a person, not an input the company
controls.

**Will the fundamentals look broadly the same in ten years?** For the MPC subsidiary —
yes, decisively; the filings project the same activity to 2086. **For the company the
common share actually buys — NO, by management's own declaration.** The FY2025 10-K:
*"the Company began executing a long-term strategy to transition from a pure-play real
estate company to a diversified holding company… we expect to acquire controlling stakes
in high-quality, durable growth public and private operating companies."* The future
acquisitions are, by nature, unnamed. And the one acquisition made so far changed
character within 26 days of closing: $2,335.8M of the insurer's $2,608.3M bond book was
sold and $1,113.5M of equities bought, so **the only filed record of the insurance leg
(Vantage's two audited years) describes an asset side that no longer exists.** Between
February and August 2026 the company's own stated yardstick moved: the FY2025 10-K MD&A
opens *"We are primarily focused on creating stockholder value by increasing our per-share
net asset value"*; the Q2-2026 10-Q deletes that sentence and opens with the diversified
holding company description.

**The argument FOR IN, built at full strength [E4-26]:** Berkshire, Loews, WTM and Markel
all passed Q1 in this project's runs as holding companies whose composition changes. The
businesses inside HHH are individually stable and simple. The declared model — real-estate
cash into float into operating companies — is the most studied model on this project's own
shelf. If the acquirer's *method* is stable, composition change is not [E3-31] change.
**Why it still fails:** in every name above, the method had a long filed record under the
same discipline (Berkshire 60 years, Loews decades, WTM ~20). HHH's method is **15 months
old**; its first and only large deployment closed 26 days before the latest balance
sheet; its second is promised but unidentified; the insurer's asset policy, the company's
self-description, and the headline yardstick all changed within the last two filings.
[E3-31] is not about lumpy industries — it is about whether *"we're smart enough to
predict future cash flows,"* and the future cash flows of HHH belong mostly to decisions
not yet made, by an allocator whose record at THIS company is one deal, 26 days old. The
corpus's own attribution [E5-19] refuses the shortcut of underwriting the man: Berkshire's
record is credited to "constructive peculiarities," luck and devotion — not to a
transferable method an analyst can assume forward.

**The separating test, asked aloud:** can I name the document that would resolve the
ten-year shape of this company? **No such document exists** — the acquisitions are not yet
chosen, the repositioned insurance portfolio has no filed history, and the first
under-HHH underwriting year has not completed. Not UNRESEARCHED — there is nothing to go
and get. **UNKNOWABLE, closed without prejudice** [E4-19].

**What would re-open the file (stated so the closure is honest under [E3-47]):** two to
three completed fiscal years of Vantage under HHH ownership (underwriting result, reserve
development, and the equity-portfolio policy through one drawdown), plus the second and
third capital deployments actually named and priced. The land business alone, were it ever
separable again, would pass Q1 on this record.

- **VERDICT: [x] UNKNOWABLE → the forward entity is, by its own declared program, not the
  filed entity; no document can close the gap until the record exists.**
- *The hard sequence closes the file here. Q2-Q4 below are RECORDED, NOT GATES (the ANF/L
  precedent), because the brief ordered the tests run and the output contract requires the
  price under `COMPUTATION — NOT A CLEARANCE`.*

## Q2 — IS IT A FRANCHISE? **[E3-03]** — **RECORDED, NOT A GATE (file closed at Q1)**
*Two legs, two rows — a blended franchise claim across an MPC developer and a Bermuda
reinsurer would be meaningless (CONVENTION 3).*

### The insurance leg — [E3-03] fails on criterion (2), by the filer's own numbers
- Needed or desired [x] · **no close substitute [ ] — FAILS**: [E2-70] verbatim —
  *"Insurance companies offer standardized policies which can be copied by anyone. Their
  only products are promises."* Vantage's distribution is rented (acquired intangibles
  assign $227M to relationships with insurance/reinsurance BROKERS — a purchased
  relationship with Marsh/Aon is intermediation, not a moat) · not price-regulated [x] —
  E&S and Bermuda, but [E2-59] reads rate freedom as the removal of a floor, not a moat.

**THE COMPETITOR ROW — insurance [E3-28].** Same metric (GAAP combined ratio), same window
(FY2024-FY2025, the only two audited Vantage years), all filing-sourced (peer FY2025
10-Ks; accessions in `peers/EXTRACT - insurance peer combined ratios FY2024-25.md`):

| Company | FY2025 combined | FY2024 combined | FY2025 GWP |
|---|---|---|---|
| KNSL | 75.9% | 76.4% | $1,977M |
| ACGL (consol.) | 82.8% | 82.5% | $22,878M |
| RLI | 83.6% | 86.2% | $2,027M |
| AXS | 89.8% | 92.3% | $9,645M |
| WRB | 90.7% | 90.3% | $15,105M |
| **Vantage (subject)** | **95.3%** | **102.1%** | **$1,625M** |

**Vantage is LAST of six in both audited years** — and on the current-accident-year basis
(97.1% / 101.1%) the gap is wider still, since FY2025's reported 95.3% includes $18.8M of
favorable releases from a book only five accident years old and 33% paid. *(Fairness
footnote from the extract: ACGL's consolidated ratio includes its mortgage segment; on
ACGL's insurance segment alone — 95.2% / 94.8% — Vantage's FY2025 is a tie, not a loss.
FY2024 is last of the row on every construction. The row's limit [E3-61] stands: it shows
position, not conduct.)* Kinsale writes
comparable specialty risk ~20 points better with near-identical premium volume. Five peers
named of a large industry; the row is sufficient to place the subject at its bottom.
[E4-37]'s agony metric cannot be run — **Vantage's audited statements disclose no rate-change
series at all** ([E4-55]-absence, insurance side: no policy counts, no renewal retention,
no rate change — the MKL absence pattern, replicated in a smaller filer).
- Class: **NONE**. A 2020-vintage underwriter, last of its row both years, breakeven-at-best
  on current-year underwriting, in the business the corpus calls near-commodity.

### The real-estate leg — a REAL but WASTING locational advantage
- Needed or desired [x] · no close substitute **[partial]** — within its submarkets the
  position approaches [E2-53] dominance: Summerlin is the scale supplier of new
  master-planned residential land in west Las Vegas (BLM-ringed), Bridgeland/Woodlands in
  their Houston corridors; a builder wanting finished superpads at scale there has few
  alternatives. But every lot competes with every other lot in the metro at the margin ·
  not price-regulated [x].
- **[E4-04] — the decisive test, and it CONVICTS the structure**: does the spending defend
  the same advantage, or buy its replacement? An MPC is a **depleting asset**: the filer's
  own sell-out dates are Woodlands 2031, Bridgeland 2032, Summerlin 2043. Continuing the
  business past those dates required **buying the next deposit** — Teravalis (37,000 gross
  acres, Phoenix, acquired 2021, sell-out 2086) — the Rhodes-Ridge shape, not the
  Coca-Cola shape. The moat is real while the land lasts and is consumed by the act of
  monetizing it.
- Primary moat metric, filing-sourced, and its trend — **the filer's own chosen national
  metric, RCLCO top-selling MPC rank, traced through five 10-Ks**: Summerlin **3rd (2018)
  → 3rd (2020) → 9th (2022) → 5th (2024) → 10th (2025)**; Bridgeland 18th → 9th → 20th →
  7th → 11th. Volume-based and partly pace-of-release-driven, but the direction on the
  metric management itself cites is **down**. Demand indicator the filer publishes: net
  new home sales FY2025 **Bridgeland −13.4%, Summerlin −8.6%**; superpad realization fell
  from $1,345k/acre (FY2024) to $970k/acre (FY2025) on mix while volume nearly doubled.
- **Untapped pricing power [E3-33]**: the model's core claim — and partially evidenced:
  custom lots realized $7.5M/acre (FY2025) vs $6.0M (FY2024); Summerlin superpad prices
  roughly tripled over the decade (see the [E4-55] series below). Claiming the full class
  claims near-monopoly [E5-28]; the submarket row supports it only inside Summerlin.
- **Key-person dependence is recorded HERE as a moat defect, as [E4-23] instructs**: the
  forward capital allocation of the whole company — which land gets developed, what gets
  bought next, how the insurer's float is invested — is contractually Pershing Square's
  advisory domain. *"The moat will go when the surgeon goes"* — and the surgeon is also
  the counterparty (Q3).
- MPC peer row: no public filer reports the same acres/price-per-acre metrics for
  comparable MPCs (St. Joe, Five Point, Tejon, Forestar differ in model and disclosure) —
  peer row for the land leg is therefore **PROVISIONAL by unavailability**, stated per the
  template; the within-market dominance evidence above is the filer's own.

### [E4-55] — THE PHYSICAL SERIES, ten years, nominal AND deflated
*(full table with sources: `_research 2026-09-02 HHH/EXTRACT - MPC residential land sales
2016-2025 [E4-55].md`; totals tie across overlapping 10-Ks)*

| | 2016 | 2018 | 2020 | 2022 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| residential acres sold | 351.2 | 456.2 | 376.6 | 322.7 | 445.4 | 620.5 |
| $/acre, nominal ($k) | ~464 | ~515 | ~573 | 768 | 990 | 890 |
| $/acre, real 2025$ ($k) | ~622 | ~659 | ~712 | ~843 | ~1,015 | 890 |

**The instrument ACQUITS the land leg — its sixth acquittal**: physical volume **+77%**
over ten years while REAL price per acre rose **~+43%** (~4.1%/yr above CPI-U). This is
the opposite of the Precision Steel shape: units and real prices rising together. Wobbles
named: 2020 pandemic, 2022 rate-shock trough (322.7 acres), 2025 nominal $/acre −10% on
Summerlin superpad mix while volume rose 39%. For the INSURANCE leg the same test returns
an absence: two years of GWP ($1,397M → $1,625M, +16%) is a growth fact, not a series, and
no rate-change, policy-count, or retention figures are published at all.

- Consolidated class: **land leg NARROW and wasting · insurance leg NONE** → the company
  as bought is not a franchise; the declared future company is unknowable (Q1).
- **VERDICT (recorded): would be OUT** — the principal new platform fails [E3-03](2) at
  the bottom of its own row, and the leg with the real advantage is depleting by design,
  with continuation dependent on replacement purchases and on the manager [E4-23].

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT A GATE (file closed at Q1)**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Sources: DEF 14A filed
2026-08-19 (0001104659-26-098808), 10-Q Note 3, closing 8-K, earnings releases (filed as
8-K exhibits 0001628280-26-009701 and -053303).*

**STEP 1 — THE WEIGHT CASE: ALL THREE DETERMINANTS FIRE → Q3 would be a BINARY GATE.**
- [x] **Daily execution** — an insurance underwriter is now a principal platform; *"their
  only products are promises"* **[E2-70]** magnifies the manager
- [x] **Control** — Pershing Square holds 46.7% of common, the Executive Chairman seat, the
  CIO office, three board designees (uncapped votes for their own election against a 40%
  cap for everything else), the investment management of the insurer's portfolio, and a
  Services Agreement that a minority holder cannot practically terminate: non-renewal
  needs a UNANIMOUS disinterested-director vote PLUS 70% of the non-Pershing shares, and a
  change-of-control termination pays Pershing the present value of ALL remaining fees
- [x] **Leverage** — $5.46bn of consolidated debt plus $2.1bn of claim reserves and $1.4bn
  of unearned premiums; small asset errors move equity

**Honesty — binary [E5-16]:** no personal-misconduct disqualifier found in the filings
read. The 2020 and 2025 Pershing transactions were approved by disinterested-director
committees and are disclosed at unusual length. Recorded as the absence of found
disqualifiers, per [E5-17] — not as a finding of honesty.

**THE RELATED-PARTY LEDGER — both sides, at full strength [E4-26]:**
*Against the arrangement:*
1. **The fee runs on the stock price.** Services Agreement (proxy, verbatim mechanics):
   base fee $3,750,000/quarter + variable fee **0.375% per quarter of (quarter-end price −
   $66.1453) × 59,393,938 shares** — i.e., **~1.5%/yr of all market-cap appreciation above
   the reference**, crystallizing quarterly, PCE-indexed, ten-year term, ten-year
   auto-renewals. **[E3-50]'s "highest stock price possible" premise is here a contracted
   revenue stream of the controlling shareholder.** H1-2026 fees paid: $7.6M.
2. **The preferred gives Pershing the upside of the insurance leg specifically**: $1.0bn of
   non-voting preferred exchangeable from FY2032 into ~32% (cap 49%) of Vantage Units;
   HHH's annual call costs the GREATER of cost+4% or **1.5x Vantage book ex-goodwill** ×
   the as-exchanged stake; plus a right of first refusal and preemptive rights over any
   Vantage equity issuance. If the insurer compounds, Pershing exchanges into it or is
   bought out at 1.5x book; if it fails, Pershing holds a pari passu $1bn claim. Common
   holders keep the development-cycle risk of the real-estate leg either way.
3. **Three roles, one side of the table**: the controlling shareholder is simultaneously
   (i) the advisor paid on the stock price, (ii) the investment manager of the insurer's
   general account (no additional fee), and (iii) the holder of the option on the
   insurer's equity. The new **Insurance Committee consists entirely of the three Pershing
   designees** (Ackman, Israel, Grandisson — Grandisson chairs), with its charter *"under
   development"* at proxy date [E2-30 — whether minority holders are the operative concern].
4. Pershing may *"cause or permit the appointment, removal or replacement of the Chief
   Investment Officer"* while the Services Agreement is in effect (proxy).
*For the arrangement:*
1. **Pershing paid $100/share** in May 2025 — a ~51% premium to the $66.1453 reference set
   the same day — for 9,000,000 new shares; minority holders were diluted UPWARD in
   per-share terms.
2. **Ackman waived all compensation** as director and Executive Chairman; the base fee is
   modest against a $4bn cap; the variable fee is currently ~nil (price ≈ the reference).
3. The preferred pays **no cash coupon** unless Vantage passes dividends up — against
   HHH's own 6.125% 2034 notes, $1bn of zero-current-cost, covenant-free capital
   [E3-52-shaped], non-cumulative.
4. **A director put personal cash in at a premium strike**: Marc Grandisson paid $10.0M
   for warrants on 1,131,273 shares struck at $100 (April 2026) — ~48% out of the money.
5. Both Pershing transactions ran through committees of disinterested directors under a
   Standstill with a 40% voting cap.

**STEP 2 — THE FLAGS:**
- [x] **Metric-switching [E2-49] — FIRES, fully dated, the run's cleanest Q3 finding:**
  (i) FY2025 10-K MD&A (2026-02-19): *"We are primarily focused on creating stockholder
  value by increasing our per-share net asset value."* (ii) Q4-2025 earnings release (same
  date): headline metric **"Adjusted Operating Cash Flow"** — defined, reconciled, given
  per-share ($446M / $7.97 vs $535M / $10.71 prior year — **introduced in the year the
  reading FELL 17%**), and **guided for 2026 at $415-465M**. (iii) Q2-2026 earnings
  release (2026-08-05): **zero occurrences of "Adjusted Operating Cash Flow," the 2026
  guidance gone mid-guidance-year**, replaced by "two principal operating platforms" and a
  stub-period combined ratio; the 10-Q MD&A simultaneously deletes the NAV sentence.
  *"Yardsticks seldom are discarded while yielding favorable readings"* — this is two
  yardstick disposals in six months, the second while its own guidance year was live.
  (A defense is available and stated: consolidation of Vantage genuinely breaks the AOCF
  composite. But its components — MPC EBT, NOI — are still published, and the composite
  could have been reported against the live $415-465M guidance. It was not.)
- [x] **Serial share issuance [E5-15] — fires WEAKLY, direction unusual**: 9M common
  (+16%) at a premium to one buyer; $1.0bn preferred to the same buyer; $10M of warrants
  to a director. No broad-market dilution; every instrument went to insiders — the flag's
  usual mechanism (promotion to the public) is absent, the concentration mechanism is not.
- [ ] EBITDA promotion [E4-29]: **does not fire.** No EBITDA anywhere; AOCF *includes* net
  interest expense; NOI is reconciled. One adjusted-presentation noted: *"Without the
  impact of the net investment loss, Vantage generated pre-tax net income of $17.5
  million"* (10-Q MD&A) — strips the mark-to-market cost of the company's own portfolio
  choice; disclosed transparently beside the GAAP figure.
- [ ] Weak accounting / unintelligible footnotes: not found — the Vantage PPA, preferred
  bifurcation, and reserve notes are unusually legible; SBC expensed; pensions immaterial.
- [x] **Trumpeted projections [E3-48] — partial**: first-ever composite guidance (AOCF
  $415-465M) introduced February 2026, unfalsifiable by August (metric dropped). The
  record of the people who made the projection cannot now be scored against it — which is
  itself the finding.
- [ ] Filed-figure tells [E4-30]: no smoothing (income swings −$551.5M → +$285.2M →
  +$123.8M); cash taxes paid trivially small vs pretax income (MPC deferrals, condo
  percentage-of-completion tax timing) — structural, not the fraud tell shape.

**STEP 3 — THE PRIMARY TEST [E2-01], hand-dealt caveat attached:** net income (loss)
attributable, continuing ops: FY2023 +$83.4M, FY2024 +$285.2M, FY2025 +$123.8M on average
equity ~$2.8-3.8bn → **~3% / ~10% / ~3.5% — below the 5.27% sovereign in two of three
years**, and H1-2026 +$166.6M (annualizing ~8.5%) only with a record condo-delivery
half. The caveat stated per [E2-73]: GAAP understates an MPC's economics because land
appreciation surfaces only at sale; the same caveat cannot rescue the Operating Assets
segment (segment EBT ~breakeven to negative in FY2024-25 with a FY2025 property-level
**covenant breach** on debt-service coverage, filed in the 10-K).

**Institutional imperative [E2-30], scored:** (1) resists change — no, the opposite; (2)
**projects/acquisitions materialize to soak up available funds — literally the declared
program**: *"we expect to acquire controlling stakes…"*; (3) staff studies to support the
leader's craving — the Services Agreement makes the controlling shareholder the permanent
author of the studies; (4) peer imitation — the model imitated is Berkshire, mindfully
rather than mindlessly, but [E5-19] is the corpus's own warning that the model's freight
was carried by non-transferable peculiarities. *"Institutional dynamics, not venality."*

**Buyback conditions [E5-08]:** no active repurchase program; treasury stock is stale
(2021-22 vintage, 6.6M shares at ~$95 average) while new equity was issued at $100 and
the stock trades ~$67. The company sold shares above today's price and bought none below
it — condition-2 conduct is therefore UNTESTED in the current window; no flag, stated.
**MUD-receivable sales recorded here**: $180M of proceeds in each of FY2024/FY2025 at
$48.2M/$48.7M booked losses — receivables monetized at ~21% discounts to carrying value;
a rational duration trade only if the cash's next use clears the discount rate given up;
the next use was Vantage.

**THE GUARDRAIL:** nothing above promotes. And the [E2-36] question answers itself here:
**the manager IS the plan** — the entire diversified-holding-company thesis is an
underwriting of Pershing Square's future judgment. That is the branch the corpus refuses
to buy: not an intact franchise with an excisable cancer, but a declared Pygmalion.

- **VERDICT (recorded): no integrity disqualifier found [E5-16/E5-17]; rationality
  unresolved — the capital-allocation record under the new program is one deal, 26 days
  old, and the yardstick against which management asks to be measured changed twice in
  six months [E2-49]. Had the file been open, the weight case (all three determinants) plus
  [E2-49] firing would have made Q3 a live gate, not a formality.**

## Q4 — WILL IT SURVIVE? — **RECORDED, NOT A GATE (file closed at Q1)**

### The two-business method governs (CONVENTION 3, the HOG/L precedent)
A blended yield across an MPC developer and a Bermuda reinsurer is meaningless. The legs
are computed separately below; the insurance leg uses the sector method as amended (step 2
diagnostic, not additive; [E5-48] with the ASU 2016-01 judgment disclosed).

### LEG 1 — real estate: owner earnings, and the (c) problem stated honestly
**The brief was right here: this is NOT [E5-20].** An MPC's "capex" is land-development
spending that CREATES the inventory it sells — it already runs through OPERATING cash flow
($477.9M of MPC development expenditures and $511.0M of condominium development inside
FY2025 OCF), so the classic OCF-minus-capex construction double-counts nothing but also
cannot separate maintenance from growth: **the spending that maintains unit volume IS the
spending that builds the next phase.** (c) below OCF is judged as the maintenance of the
income-producing portfolio only: operating property improvements + P&E ≈ **$50M** (FY2025
actual $48.3M), with the D&A end ($183M) shown as the generous-overstatement bound — real
estate D&A overstates economic maintenance here (the L/Boardwalk inversion), because the
filer's own improvements spending has run at ~27% of D&A for three years.

**The windows [E4-25] — and the perimeter breaks that limit them.** Continuing-operations
OCF (FY2025 10-K, filed statement): **FY2023 −$215.2M · FY2024 +$447.8M · FY2025
+$462.4M**; H1-2026 +$277.1M (contains a record condo-delivery half and 26 days of
Vantage — not annualizable [E4-41]). Years before 2023 are a DIFFERENT PERIMETER (Seaport
consolidated until the July 2024 spinoff), and 2026 forward is a different perimeter again
(Vantage) — **the ten-year series contains three different companies**, which is itself
the Q1 finding restated.
- Short window (FY2024-25 harvest years): mean OCF $455.1M − SBC $19.8M − (c) $50M ≈
  **$385M**
- Three-year window (FY2023-25, one condo-consumption year in): mean OCF $231.7M − SBC −
  (c) ≈ **$162M**
- **Spread: 58% off the high end. [E4-25]: a range this wide supports no point conclusion
  — that IS the finding.** The distorted-year mechanism is named: condominium development
  consumes cash for 2-3 years and returns it in delivery quarters (FY2023 the trough,
  H1-2026 the crest), and MPC land closings are builder-scheduled, not annual.
- The filer's own composite (Adjusted Operating Cash Flow: FY2025 $446M, FY2024 $535M) is
  recorded for cross-check only — it is a non-GAAP management measure [E4-29-adjacent],
  since dropped (Q3).

### LEG 2 — insurance: the sector method, as amended
- **Step 1, investments at market**: acquired portfolio at close $3,101.9M (fixed
  maturities $2,608.3 + short-term $32.8 + cash $376.3 + restricted $84.5), plus the $1.0bn
  preferred proceeds injected. At 6/30: securities $1,351.9M + insurance cash (inside the
  consolidated $2.65bn; not separately filed) — mid-repositioning into equities.
- **Step 2, cost of float — DIAGNOSTIC [E3-69], and the structural ruling holds**: from
  **Vantage's own pre-acquisition audited statements** (8-K/A ex-99.1, PwC opinion):
  CONVENTION 4 float **$1,036.3M (FY2024) → $1,440.8M (FY2025)**; underwriting result
  (filer's own segment measure) **−$17.0M (FY2024), +$48.9M (FY2025)** → cost of float
  ≈ **+1.6% then −3.9%; two-year net ≈ −1.3%/yr (a small benefit)**. **The window is TWO
  YEARS against [E3-69]'s "a period of years," and the 2021-2023 audited statements are
  not public** → the cost-of-float leg beyond FY2024 is **UNRESEARCHED — artifact:
  Vantage FY2021-23 audited statements / BMA Financial Condition Reports; ladder rung:
  company disclosure (rung 3), blocked by private-company status pre-2024.** 26 days of
  HHH-era history is not evidence [E3-69]. The reserve-candor substitution [E2-67]: the
  development tables exist BUT are marked *unaudited supplementary information* (PwC
  explicitly does not opine on the 2021-2024 columns), the book is 33% paid, and the
  accident-year decomposition shows adverse pockets: insurance AY2023 **+13.8%** and
  AY2024 upward; reinsurance AY2022 **+10.6%** (the Russia-Ukraine strengthening) —
  against net favorable headlines. Neither a conviction nor an acquittal: **five accident
  years cannot convict or acquit a long-tail reserving culture** — the honest verdict on
  this sub-test is UNKNOWABLE with the artifact that would resolve it not yet in
  existence (time).
- **Step 3, ex-portfolio pre-tax earnings [E5-48]**: FY2025 underwriting +$48.9M + net
  fee income +$12.5M ≈ **$61M**; FY2024 ≈ **−$17M + fees**. The ASU 2016-01 judgment
  disclosed: post-repositioning, the largest income-statement item of this leg will be
  **unrealized equity marks** (already −$38.3M in 26 days); step 3 excludes them, step 1
  carries the portfolio at market — no double-count, but the leg's reported GAAP earnings
  will be noise from here on.

### Great, good, or gruesome? [E4-20]
- MPC leg: **good-to-great while the deposit lasts** — 81-96% projected cash margins on
  land carried at historic basis; the caveat is [E4-04]: continuation requires buying the
  next Teravalis. - Operating assets: good-to-mediocre (claimed 8.8% yield-on-cost
  against a 5.27% sovereign; FY2025 covenant breach on coverage ratios at property level).
- Insurance leg: **so far gruesome-shaped by the filed numbers**: five years, $1.24bn of
  paid-in capital grown to $1.40bn of equity, cumulative underwriting ≈ +$32M over the two
  audited years and last of its row both years; it grows fast, consumes capital, and
  earns its keep from investment leverage on float — the account's rate so far is the
  bond's, not a franchise's.

### Staying power — score all three [E5-11], insurance leg per [E2-61]
1. **Large and RELIABLE earnings stream — FAILS the reliability half**: OCF swung −$215M →
   +$462M in three years by the filer's own timing mechanisms; the insurance leg adds
   accident-year volatility plus equity-mark volatility BY POLICY.
2. **Massive liquid assets — split verdict**: $2.65bn cash + $1.35bn securities is real;
   but [E2-61] governs the insurance leg — its test is reserve adequacy and net worth,
   and the reserves are young, IBNR-heavy (71-91% on recent AYs), and were fair-value
   reset at acquisition; the RE leg's $717M of restricted cash includes covenant-trapped
   property cash (FY2025 10-K: *"not in compliance with certain property-level debt
   covenants… excess net cash flow after debt service from the underlying properties
   became restricted"*). Undrawn facilities ($515M Bridgeland + $970M construction
   commitments) are NOT counted, per [E5-39].
3. **No significant near-term cash requirements — the load-bearing test**: consolidated
   maturities $663M (2026) / $508M (2027) / $923M (2028) / $1,076M (2029) against ~$260M/yr
   of interest; the Feb-2026 refinancing ($1.0bn of 2032/2034 notes replacing the $750M
   2028s at 5.875%/6.125% vs 5.375%) bought time at a price. Condo completion obligations
   (Kalae 2028, Ritz-Carlton 2027) are deposit- and construction-loan-funded. The
   **[E2-54] coverage test at the conservative end fails**: accrued interest ~$260M+
   (plus $76M capitalized) against owner earnings of $162M (three-year construction) —
   *"zip up your wallet"*; at the harvest-window construction ($385M) it passes at ~1.1-1.5x.
   Two structural items sit outside the schedule: the preferred's **contingent repurchase
   + 10% defaulted dividend + distribution stopper**, and the Services Agreement
   **make-whole (PV of all remaining fees)** on a change of control — both payable
   precisely in the scenarios where cash is scarce.

### [E2-62] — the license question, inverted, as the brief ordered
Berkshire's concentration *"makes sense only because"* of exceptional financial strength.
**HHH's filed balance sheet implies the OPPOSITE of the license**: an insurer converting
its bond book to equities (target allocation: cash, T-bills, public equities; $1.11bn
bought in the first 26 days; manager: the controlling shareholder) sits inside a parent
carrying $5.46bn of debt, a property-level covenant breach in its latest 10-K, an OCF
series that was negative two fiscal years ago, and a $1bn mezzanine claim held by the same
manager choosing the equities. *"For almost all other insurers, a comparable degree of
concentration… would be totally inappropriate."* HHH is the almost-all-other case, by
construction.

### Name the specific way THIS business dies [E2-27, E3-24]
**Mechanism — the correlated triple, plus the structure that monetizes it**: a housing
trough in Vegas/Houston (the filer's own leading indicator already negative: net new home
sales −8.6% Summerlin, −13.4% Bridgeland in FY2025) cuts MPC EBT while condo starts stall;
the 2028-2029 maturity wall (**$2.0bn**) reprices or closes; the insurer's equity
portfolio draws down 30% (**≈ −$400M+ of capital**) in the same macro event while one
outsized cat or casualty-development year hits an IBNR-heavy five-year-old book (insurance
AY2023 already +13.8%; the book includes property-cat reinsurance — [E4-40]: two benign
cat years in a young book are *"not only useless, but actually dangerous"* as a guide).
In that state the recapitalizer of last resort is the controlling shareholder, whose
existing instruments (10% defaulted-repurchase dividend, distribution stopper, exchange
into up to 49% of the insurance subsidiary, fee make-whole) price the rescue. Quantified
from filed figures: half of MPC EBT ≈ −$225M/yr; equity-book drawdown ≈ −$400M; one
adverse-development year at the AY2023 rate on $1.55bn net reserves ≈ −$200M; against
$2.65bn of cash and $2.0bn of 2028-29 maturities. **Each element alone: a real
possibility. The conjunction: a low-level possibility — but [E5-12]'s test is not the odds,
it is who holds the gun, and here the gun is held by the counterparty across the table.**

- **VERDICT (recorded): would be UNKNOWABLE-to-OUT at the conservative construction — the
  [E4-25] spread (58%) plus the [E2-54] coverage failure at the conservative end plus a
  reserve base too young to audit. Survival is likely in the median case; the framework
  scores the worst case [E2-55], and the worst case is structurally concentrated, not
  absorbed.**
*(Constraints applied above: multi-window with the spread carried [E4-25]; (c) a disclosed
judgment — this is neither the [E5-20] exception nor the plain D&A default, it is the MPC
case where development spend sits inside OCF and (c) below the line is the operating-
portfolio maintenance only; SBC subtracted in full [E5-06]; the distorted years named.)*

---
⛔ **Q5 does not open unless Q1-Q4 each show IN. Q1 returned UNKNOWABLE — the file is
closed. What follows is the run-queue output contract, not a clearance.**

---
## COMPUTATION — NOT A CLEARANCE
*(Operator rule 3. No entry language. The arithmetic the queue contract requires.)*

**Price and cap (quote from web aggregators, flagged as such, 2026-09-03):** HHH ≈
**$67-68/share** (sources quoted $66.60-$67.79 intraday; 52-wk range $61.01-$91.07). Cap
at $67.5 × 59,721,036 = **≈ $4,031M common**, plus $995.8M mezzanine preferred. Pershing
Square paid $100.00 in May 2025 for 16% of the count; the quote is 32% below that print.

**Construction A — whole-company owner-earnings yield (the strict framework construction):**
- Owner earnings $162M (3-yr window) to $385M (harvest window) ÷ $4,031M common cap =
  **4.0% to 9.6%**, against the 5.27% sovereign. The capex band ($50M judged → $183M D&A
  end) moves the range a further ~$130M down at the D&A end.
- Zero-growth value at the sovereign: $162-385M ÷ 5.27% = $3.1bn-$7.3bn ≈ **roughly $50 to
  $120 per share** — the price sits INSIDE the range: **Bar 2's middle outcome, "no useful
  conclusion can be reached" [E4-25]** — which is the honest whole-company answer.
- At the ~10% floor [E4-28]: $1.6bn-$3.9bn ≈ **roughly $27 to $65 per share** — the price
  sits at or above the top of the floor range on every construction: **below the floor,
  quit on, not ranked.**
- What the price already assumes: at the judged midpoint (~$275M), the $4.03bn cap needs
  **~2% perpetual growth to match the bond** and **~7% to clear the floor** — against a
  filed record whose three-year OCF mean includes a negative year, and net new home sales
  currently falling in both flagship communities.

**Construction B — sum of the parts (two-business method), stated for the spread it adds:**
- Insurance leg to common: post-injection capital ≈ $2.8bn; at 1.0x (the row supports no
  franchise premium) with the preferred's as-exchanged ~32% carved out ≈ **$1.9bn**; at
  the 1.5x just paid at arm's length, common's share ≈ **$2.9bn**.
- RE leg at the sovereign on its own windows: $3.1bn-$7.3bn (same arithmetic as above —
  the FY2023-25 OCF is entirely pre-Vantage).
- Sum to common: **≈ $5.0bn-$10.2bn ≈ $84-171/share** — ABOVE the quote on every
  construction, and the spread (2x) is exactly why [E4-25] refuses the sum: the answer is
  a window choice wearing a valuation. Recorded, not relied on. *(The NAV bridge every
  bull cites — 19,808 residential acres at the filer's own $391k-$1,719k estimates ≈
  $17bn+ undiscounted — is [E2-01]/[E4-29] material: sell-out dates run to 2086, and 2086
  dollars at any honest rate are pennies. It is not used.)*

**THE PRICE, as the output contract requires, in round numbers:**
- **Value roughly $50-120/share at the sovereign (judged, at the framework's conservative
  end, roughly $60-85); roughly $27-65/share at the [E4-28] floor. Current price ≈ $67.50.**
- The price sits inside the sovereign-rate range (no useful conclusion) and above the
  floor range (quit on at the floor). **Under v4.1 the name would close at Q5 on the floor
  even if Q1-Q4 had cleared — honest pre-tax expectancy at this price is ~4.0-9.6%,
  below the ~10% "figure we quit on" on every construction but the single most generous
  window-and-capex pairing.**
- Windage count: conservatism spent ONCE (conservative end of the window/capex range);
  no risk premium in the rate [E3-42]; no margin stacked on Bar 2 [E4-01].

**TEMPLATE DEFECT, recorded for the maintainer (the ORLY run's finding, still only half
fixed):** the template's Q5 block still carries **"THERE IS NO HURDLE. THERE IS A RANKING
[E4-21]"** — the pre-Test-D v4.0 wording that `THE FRAMEWORK v4.md` REWROTE on 2026-08-28
into "the floor, then the ranking" [E4-28], and that the 2026-09-02 correction (found by
the BRK run) removed from the sector method's step 4. The framework governs; this run used
the floor. The template line should be rewritten before the next run fills it in.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not applicable — the file closed at Q1 and no position exists to monitor.** The
re-opening conditions were pre-committed at Q1 per [E1-02]: (i) two to three completed
fiscal years of Vantage under HHH (underwriting result, reserve development, the equity
portfolio through one drawdown); (ii) the second and third capital deployments named and
priced; (iii) a stable headline yardstick surviving two consecutive annual filings
[E2-49]. The watch-item if ever re-opened: net new home sales in Summerlin and Bridgeland
(the filer's own leading indicator), and the RCLCO rank direction.

- **VERDICT: not opened — file closed at Q1.**

---
## THE OUTPUT CONTRACT — PRICE AND PASS/FAIL

**PRICE: value roughly $50-120 per share at the 5.27% sovereign (judged conservative band
roughly $60-85); roughly $27-65 per share at the [E4-28] ~10% floor. Quote ≈ $67.50
(aggregator, 2026-09-03, flagged). All of it under `COMPUTATION — NOT A CLEARANCE`.**

**FAIL. The file closes at Q1 — UNKNOWABLE.** The company the common share buys is, by its
own declared program, not the company in the filings: a 15-month-old diversified-holding
transformation, one 26-day-old $2.1bn insurance acquisition whose asset side was rebuilt
within those 26 days, and future deployments that are promised but unnamed. No document
exists that closes the gap; time will. Without prejudice: the MPC subsidiary alone, on
this record, would have passed Q1. Had the gates been open, the recorded findings say Q2
would have failed on the insurance row (last of six both audited years) and Q5 would have
quit on the floor (honest expectancy ~4.0-9.6%).

---
## SELF-AUDIT
- [x] Questions answered in order; file closed at the first non-IN verdict (Q1); Q2-Q4
      explicitly RECORDED, NOT GATES per the ANF/L precedent and the queue contract
- [x] No question marked IN carries an "unverified" or "provisional" caveat (no question
      was marked IN)
- [x] Every UNRESEARCHED sub-item names the artifact (Vantage FY2021-23 audited
      statements / BMA Financial Condition Reports — rung 3, blocked by pre-2024 private
      status; MPC peer same-metric row — no public filer publishes it)
- [x] UNKNOWABLE states what cannot be known: the ten-year composition and cash flows of a
      declared, continuing transformation with unnamed future acquisitions
- [x] Step 0: filings read with accession numbers; consideration/cash-flow cross-check tied
- [x] Owner earnings multi-year, windows stated, capex band a disclosed judgment, SBC
      subtracted, spread carried [E4-25]
- [x] Competitor row: insurance row filled (5 peers, same metric, same window,
      filing-sourced); land-leg row PROVISIONAL by unavailability, stated
- [x] Sovereign: USD earnings, US Treasury daily par yield curve 30-yr, 5.27%, 2026-09-01
- [x] Value stated as round-number ranges; price dated and flagged as aggregator
- [x] Bar 2 only (price inside range → no useful conclusion); windage count: once
- [x] Run committed to git after every question
- **Protocol note:** this run was resumed across multiple sessions under the WRITE-EARLY
  PROTOCOL; each question was committed as it closed and no work was lost.

## REGISTER
- Verdict: [x] **UNKNOWABLE** (about my evidence — and about anyone's: the evidence does
  not yet exist)
- One line: **a transparent, durable land business wrapped inside a 15-month-old
  transformation vehicle whose forward shape is a declared unknown; the wrapper, not the
  land, closes the file.**
- **The work orders that would feed a re-opened file:** Vantage FY2021-2023 audited
  statements or BMA Financial Condition Reports (rung 3) · FY2026 and FY2027 10-Ks with
  full-year Vantage segments · the first post-Vantage proxy scoring the Services
  Agreement fees against outturn.
- **What specifically cannot be known today:** the underwriting quality of a five-accident-
  year book that is 33% paid; the behavior of an insurer's equity-heavy portfolio policy
  through a drawdown; the identity, price, and quality of the acquisitions the declared
  program will make; which yardstick management will report against next year.
