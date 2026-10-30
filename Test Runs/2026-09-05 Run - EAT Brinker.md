# Company Run — Brinker International (EAT) — 2026-09-05
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
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr
  (issuing authority; struck fresh this run)**
- FX: none — USD quote, USD earnings (domestic casual dining; international is franchised
  royalties, immaterial)

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **10-K FY2026, period ended 2026-06-24, filed
  2026-08-19, accession 0000703351-26-000029** (anchor); FY2026 10-Qs (Q1 accn
  0000703351-25-000046, Q2 -26-000006, Q3 -26-000015); DEF 14A filed 2025-10-03
  (accn 0001193125-25-230105); nine 10-K vintages FY2018-FY2026 via the DRI run's
  `_research 2026-09-04 DRI/peer_EAT.md` workpaper (accessions listed there)
- figure cross-checked against the filed statement: **OCF FY2026 $789.4M — filed
  consolidated statement of cash flows transcribed by hand, matches XBRL
  NetCashProvidedByUsedInOperatingActivities $789,400,000; total assets $2,815.0M
  cross-checked in the DRI-run workpaper against us-gaap:Assets**
- **Price $230.22, 2026-09-04 close (Yahoo chart API — aggregator, live quote only,
  flagged; Stooq now behind a JS wall)**
- **Shares 41,765,010, hand-read off the FY2026 10-K cover (single class, $0.10 par,
  as of 2026-08-11)** — run.py's 44.8M is its known weighted-average defect. **Cap $9,615M.**
- Stage 0 by hand: cover count above; **EAT pays no dividend — verified: "There were no
  dividends declared in fiscal 2026 or fiscal 2025" (FY2026 10-K); suspended Q4 FY2020
  under revolver covenants, never reinstated.** Screen row reproduced in shape (see
  `_research 2026-09-05 EAT/eat_oe_series.md`): by hand 3-yr 3.83-4.18% / 5-yr 2.59-2.82%
  at the cover cap; the brief's 3.2%/6.8% sits between the windows; spread 32.4%
  (5-yr vs 3-yr conservative ends), verified against my own windows.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: Brinker runs 1,163 company-owned
  sit-down restaurants — 95% of them domestic Chili's, plus 49 Maggiano's — on leased
  real estate (1,079 of 1,121 sites leased at FY2021; the estate was sold-leaseback in
  FY2019). A box takes in ~$5.0M a year (Chili's FY2026 AUV), spends ~26% on food, ~31%
  on hourly labor, ~25% on rent/utilities/advertising, and leaves ~18% before corporate
  overhead ($189M) and interest. A second, tiny stream: royalties on ~$1.14bn of
  franchisee sales (472 franchised units, nearly all international). Growth comes from
  more guests per existing box (traffic), higher menu prices, and a handful of new units
  (6 company-owned opened FY2026). Simple, stable in character, one segment that matters.
- The scarce input this business controls: honestly — none that is structural. The brand
  and 1,110 domestic Chili's sites are the assets; the thing that moved results was
  operating execution (staffing, menu simplification, a $10.99 value platform, viral
  marketing). Whether that is a moat is Q2's question, and the absence of a scarce input
  is recorded here as the hand-off.
- Will the fundamentals look broadly the same in ten years? Yes — casual dining shrinks
  or stagnates but does not vanish; cooking, serving and pricing a sit-down meal will
  look the same. The filer's own risk factor states the category fact: "The casual dining
  segment of the restaurant industry has not seen significant growth in customer traffic
  in recent years" (FY2026 10-K, Item 1A).
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] · no close substitute [ ] **FAILS — see below** · not price-regulated [x]

**THE TEN-YEAR SERIES [E4-55] — Chili's company-owned, filed every year, nothing withdrawn**
(each year's 10-K MD&A four-way decomposition; full table in
`_research 2026-09-04 DRI/peer_EAT.md`, built from nine 10-K vintages):

| FY | 17 | 18 | 19 | 20 | 21ᵇ | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Price | +1.8 | +1.3 | +1.7 | +1.3 | +0.4 | +3.3 | +9.2 | +7.4 | +4.5 | +4.4 |
| **Traffic** | **−5.8** | **−3.6** | **+2.3** | **−8.8** | **+10.5** | **+2.7** | **−6.9** | **−0.6** | **+16.0** | **+3.6** |

ᵇ FY2021 includes It's Just Wings virtual-brand delivery orders, per the filing's own footnote.
- **Cumulative ten years (arithmetic mine): price +41.0% compounded; traffic +6.9% — and
  effectively ALL of the traffic is the single year FY2025.** Six of the eight pre-boom
  years are negative; the pre-boom base is a business that could not take +1.8% price
  without shedding 5.8% of its guests (FY2017).
- **The five-year pair the operator flagged, established precisely:** FY2022-26 price
  +32.2% compounded WITH traffic +14.2% — the best [E2-44](1) print in this queue
  (COKE passed at volume −1.3% on +52% price). But leave-ONE-out [E4-41]: drop FY2025
  and the same five-year window reads **price +26.6% / traffic −1.6%.** The entire
  positive half of the rarest-combination claim lives inside one viral year.
- **The normalization series the brief asked for (filed 10-Qs, FY2026 quarterly Chili's
  traffic): +13.1 → +2.7 → −1.2 → ~+1.2 implied** (Q4 = 4×3.6 − 3×4.4, arithmetic mine).
  Q1 still lapped a pre-viral base; the three lapped quarters average ~+0.9%. **The wave
  is over as growth; the LEVEL held** — guests did not give back the +16%, and FY2026
  took another +4.4% price on top. Recorded as the strongest fact against this verdict.
- **[E4-55] deflated:** Chili's revenue per meal $15.50 (FY2021) → $23.12 (FY2026), +49%
  in five years, vs CPI-U food-away-from-home ~+19-20% over the comparable window (BLS,
  from the DRI run) — the check outran category inflation while traffic rose in the two
  surge years. Genuinely rare, and genuinely two years old.

**Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04, E4-23]**
Yes, twice, and this decides the question:
1. **[E2-53] dominance FAILS on the filed record.** "Once dominant... good or bad, it will
   prosper" — Chili's had the same brand, the same ~1,100 domestic boxes, and the same
   value platform ("3 for $10" is in the FY2021 10-K, Item 1) through FY2017-FY2024, and
   printed six negative-traffic years in eight with a 6.0% operating margin (FY2021).
   Position did not carry it; the marketplace set the outcome until the execution changed
   (Hochman, CEO June 2022: staffing up, menu cut, TikTok). The turnaround manager vs the
   business's decade [E2-37]: the decade is the business; the two years are the manager
   and the wave.
2. **The Maggiano's natural experiment, judged separately as the brief asked** (segment
   note discloses it): same corporate hand, same playbook window — traffic negative five
   straight years, FY2026 **−9.3%** with +5.0% price; segment OI **$60.1M → $16.5M** in
   FY2026 alone. The corporate claim reduces to one brand's two-year run. Franchise mix:
   immaterial as a stream (Franchise revenues $56.5M, 1.0% of total revenues, FY2026
   income statement) — judged inside the segments, no separate verdict needed.
3. **[E3-51] the wave, named:** the traffic arrived through value pricing ($10.99
   "3 for Me") plus viral relevance ("the social-media-famous Triple Dipper®" — the
   10-K's own words). Value price points and TikTok are non-excludable weapons; every
   scaled casual-diner can and does copy them ("competitors employing our same
   strategies or discounting their offerings" — FY2026 forward-looking-statements list).
   [E4-36]: extreme performance on one variable (value-for-money perception), i.e.
   wave-riding. The AUV-led cost position ($5.0M/box funding value at 18.5% segment
   residual margin) is real TODAY but is the wave's RESULT — Chili's AUV was $2.9M in
   FY2021, mid-pack — so the "cost advantage" [E2-58 exception] is not shown to be
   sustainable: it is two years old and made of the traffic it is supposed to defend.
4. **[E2-58] the category equation:** persistent over-capacity without administered
   prices = poor profitability. The filer's own risk factor: "The casual dining segment
   ... has not seen significant growth in customer traffic in recent years... our
   ability to grow customer traffic ... will depend on our ability to increase our
   market share." A share-shift game in a flat, over-capacitied category, said plainly
   by the subject itself.

- Primary moat metric, filing-sourced, and its trend: same-restaurant traffic (above) —
  direction currently POSITIVE at ~+1%/qtr lapped, on a base that was negative for most
  of a decade; and return on unleveraged NTOA 34.3% (FY2021) → **82.1%** (FY2026), top of
  the cohort — a level that is itself the wave's print.

**THE COMPETITOR ROW — required [E3-28].** Same formulas as the DRI run (OI/NTOA
ex-goodwill, ex-cash, ROU-out; traffic = filed physical series), filing-sourced, from
`_research 2026-09-04 DRI/` workpapers built 2026-09-04:

| Company | Return on NTOA (window) | Physical series, price cycle | source |
|---|---|---|---|
| **EAT (Chili's)** | **82.1%** FY2026 (33.6% ROU-in; 64.3% incl gw); 34.3% FY2021 | Chili's traffic +14.2% FY2022-26 cum (−1.6% ex-FY2025); Maggiano's −9.3% FY2026 | 10-K FY2026 accn 0000703351-26-000029 |
| DRI (completed run) | 38.5% FY2026 (22.2% incl gw) | OG guests 89.1 on FY2019=100; LH **121.1** | DRI 10-K FY2026 accn 0000940944-26-000025 |
| TXRH | 34.0% FY2025 (21.1% ROU-in) | traffic positive **11 of 12 years**; +15.3% FY2022-25 cum; AUV $8.7M; zero debt | TXRH FY2025 10-K |
| CAKE | 23.2% FY2025 (9.0% ROU-in) | orders **−21.5%** FY2017-25 on ~+30% pricing | CAKE FY2025 10-K |
| BLMN | 4.5% FY2025 (2.6% incl gw) | Outback traffic **−15.1%** FY2022-25, check +19.3% | BLMN FY2025 10-K |

- Peers named: **4 of the ~6-8 real chained casual-dining competitors** (plus the subject).
  Applebee's (Dine Brands, franchisor P&L — not same-formula comparable) and the private
  regionals are the row's stated limit [E3-61]; fiscal year-ends differ by up to 13 months
  across the row, stated. The row does NOT convict EAT of weak economics — it convicts the
  CATEGORY of substitute-density: the losing half (CAKE, BLMN, OG, Maggiano's) lost the
  exact guests the winning half (Chili's, LongHorn, TXRH) gained, at the same time, on
  value. **Share moves this fast in both directions only where substitutes are close
  [E3-03](2).** And the cohort's DURABLE physical series belongs to TXRH (11 of 12 years)
  and LongHorn (121.1 index), not to Chili's one viral year.
- **Untapped pricing power [E3-33/E5-28]:** claiming it claims near-monopoly; not
  claimable for a value player in casual dining whose own strategy is the $10.99 platform. No.
- Class: [x] **NONE** (a two-year execution/wave advantage on a decade-long no-moat base)
  · Direction: the wave's numbers still widening; the basis non-ownable [E4-04]
- **VERDICT: [x] OUT** — [E3-03](2) fails: the customers' own filed behavior (a decade of
  substitution away, then a surge in through the value door) is the direct evidence of
  close substitutes; the surge is [E3-51] surfing (value + virality), the pre-boom base
  [E4-41] is the honest level of the BUSINESS as distinct from the wave; [E2-53]
  dominance fails on the decade and on Maggiano's; key-person dependence recorded here
  as a moat defect [E4-23] — the moat goes when the surgeon goes. **OUT is about the
  business, permanent, and closes the file before Q5.**

*[E4-26] discipline — the disconfirming case, stated at full strength: FY2026 is a lapped
year and still printed +3.6% traffic / +4.4% price; the five-year both-halves pair is the
best in the queue; the AUV-margin flywheel could PROVE structural if it survives the
virality's decay. The pre-committed reopen test: if the FY2027 10-K (due ~Aug 2027) files
a THIRD consecutive positive-traffic year with price ≥ FAFH inflation — three lapped
years, five-year window then clean of the viral base — the wave classification is wrong
and this Q2 is re-run. That is a work order with a date, not a hedge on the verdict.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

*File already closed at Q2 (OUT). Q3-Q4 recorded as findings per the DRI precedent and the
queue's output contract; nothing below reopens the file.*

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution** — have-to-be-smart-every-day **[E3-38]** — a casual-dining
  operator with no franchise (Q2's finding) is exactly the class the 1991 original names:
  *"a business, unlike a franchise, can be killed by poor management"* **[E3-43]**. The
  FY2017-24 record IS the demonstration: the same assets under ordinary execution earned
  a 6.0% margin.
- [ ] Control — no. - [ ] Leverage — no longer (post-deleveraging; see Q4).
**Case declared: GATE.**

**Honesty — binary [E5-16]:** no disqualifier found. No restatement found in the vintages
read (FY2018-FY2026 10-Ks via the DRI workpaper + this run); KPMG auditor **since 1984**,
unqualified opinions; no personal-misconduct matter surfaced in the proxy or 10-K read.
Written as [E5-17] requires: an absence of found disqualifiers, not a finding of honesty.

**STEP 2 — THE FLAGS.**
- [ ] weak accounting — not found. The 10-K is GAAP-clean: **zero occurrences of EBITDA in
  the FY2026 10-K (counted)**; single capex line; no capitalized-software line (the HAS
  defect does not bite); footnotes legible.
- [x] **trumpeted projections / promotion [E4-22]** — a live guidance culture **[E5-30]**:
  annual revenue/EPS/capex guidance in both Q4 releases read (FY2026 guided 2025-08-13;
  FY2027 guided 2026-08-12: revenue $6.15-6.27bn, adj EPS $12.60-13.40). ER language is
  promotional: *"Chili's is officially back, baby back!"* (FY2025 Q4 ER) and — quoted
  because a moat claim is this run's exact question — *"Our strong brand relevance,
  industry-leading value proposition, streamlined operations, and significant restaurant
  investments have created a competitive moat"* (FY2026 Q4 ER, CEO). **[E3-48] record:**
  FY2026 guidance beaten on revenue ($5,807.4M vs $5.60-5.70bn guided) and EPS, **missed
  on capex — guided $270-290M, spent $231.9M**, an under-spend of the filer's own
  investment guide by ~15-20% in the year margins were celebrated (recorded; feeds the
  (c) judgment at Q4).
- [x] **EBITDA / adjusted promotion [E4-29]** — fires, scoped to pay design and ERs:
  adjusted EBITDA in both earnings releases (6 mentions each); **every pay metric is
  adjusted non-GAAP** — STIP on "Adjusted PBT" + revenue, performance shares on
  "Adjusted EBITDA," all excluding the "Other (gains) and charges" caption **[E5-33]**
  (the caption ran $86.6M in FY2025 per the ER reconciliations; exclusions recurring
  by design).
- [ ] serial share issuance [E5-15] — no: shares 45.0M (June 2024) → 41.77M (Aug 2026).
- [x] **filed-figure tells [E4-30]** — cash-tax share of pretax FALLING: 15.8% (FY2024) →
  14.0% → **11.4%** (FY2026: $66.0M paid on $580.9M pretax). Read, as the flag demands:
  the mechanism is on the face of the cash-flow statement (deferred income taxes +$32.2M
  FY2026, +$12.6M FY2025 — book provision 16.2% effective, held down by FICA tip credits,
  with the deferred piece disclosed line-by-line). Not period-shifting; noted and
  acquitted with the mechanism named. Growth is NOT unnaturally smooth (NI 24.4 → 131.6
  → 117.6 → 102.6 → 155.3 → 383.1 → 487.0) — no smoothing tell.
- **The pay-windfall finding (recorded, not a rigging flag):** FY2025 STIP paid **200% of
  target on both components** (Adjusted PBT target $244.4M — set ~48% ABOVE FY2024's
  $164.9M pretax actual, the committee's memo even assumed continued industry traffic
  declines — actual $536.4M); the FY2023-25 PSP paid **200%** (target $405M set FY2023,
  max $506.25M, actual $788.5M); and the FY2025-27 PSP (target $541.8M, max $623.1M, set
  early FY2025 off FY2024's $443.6M) was **already beyond its own MAXIMUM before the
  proxy printed** (FY2025 actual $788.5M). Targets were set above prior actuals — the
  DG/ULTA rigging pattern does NOT replicate — but the committee did not reset after the
  wave, so three years of LTI are effectively guaranteed at max unless EBITDA falls
  ~30%. Management's pay rides the same wave the valuation does [E4-41]. Hochman FY2025
  SCT $30.5M, CAP $122.3M; 402(v): TSR $100 → **$750.83** vs peer index $182.05 — pay
  tracked the stock, the stock tracked the wave.
- [E2-49] metric-switching: not found in the proxy read (STIP/LTI metrics stable FY2023-25;
  scoped to the FY2025 proxy plus plan descriptions therein).
- [E4-52] convergence: the flags do NOT converge into one system — the filed accounting is
  clean and conservative-side; the promotion lives in releases and pay design. No
  lollapalooza.

**STEP 3 — THE PRIMARY TEST [E2-01]** — run on unleveraged NTOA [E2-43] (equity is
meaningless here: a $911.6M treasury block took book equity negative FY2019-FY2023):
OI/NTOA ex-goodwill **34.3% (FY2021) → 82.1% (FY2026)**; ROU-in 13.4% → 33.6% (the honest
cross-company form for an all-leased estate — 1,079 of 1,121 sites leased). The series is
the wave's print; the FY2021 figure is the hand the manager was dealt [E2-73].

**The half-owner test [E2-26]:** passes in the filings — the four-way comp decomposition
(price/mix/traffic) is filed every year INCLUDING the six negative-traffic years, nothing
withdrawn in ten vintages ([E2-49] clean on the metric that matters — the ORLY/TSCO
pattern); segment OI discloses Maggiano's deterioration plainly. The ER layer is worse
than the filing layer (adjusted measures, moat talk) — stated.

**The institutional imperative [E2-30]:** (1) no — the turnaround was itself a change;
(2) watch the re-image program (60-80 remodels FY2027, then ~10% of the fleet annually —
disclosed, plausible maintenance); (3) not observable; (4) inverted — staffing UP while
peers cut labor was the anti-imitation move. No box fired hard.

**Capital allocation — the record, both halves:**
- **The FY2015-19 vintage is the [E2-60] case study, filed:** ~$1.53bn of buybacks +
  ~$330M of dividends over FY2015-19 against ~$660M of OE (FY2016-19 sum), funded by
  debt and the FY2019 **$455.7M sale-leaseback of 141 restaurants**; equity driven to a
  deficit; then FY2020 filed the proof that restricted earnings had been distributed:
  the amended revolver **"prohibited [us] from making dividends, stock repurchases and
  investments"** (FY2021 10-K, verbatim) and the dividend — $1.52/sh in FY2019 — was
  suspended Q4 FY2020 and **has never been reinstated** ("There were no dividends
  declared in fiscal 2026 or fiscal 2025"). Distribution of restricted earnings, proven
  by the covenant that stopped it.
- **The FY2021-26 half runs the other way [E2-69]:** deleveraged $1,225.0M (FY2020) →
  $448.0M (FY2026) total debt incl. finance leases; the 5.000% notes repaid at maturity
  FY2025; the 8.25% COVID notes redeemed 2026-07-15 at 104.125 ($378.9M, refinanced onto
  a 4.90% revolver — a rational 8.25%→4.90% swap with ~1.2-year premium payback);
  revolver $0 drawn at year-end; $969.9M available.
- **Buybacks [E5-08]:** condition (1) passes today. Condition (2): FY2026's $400.0M at
  ~$138 avg sits inside my conservative zero-growth band (~$114-184 judged ~$160 — Q5
  computation); the post-year-end tranche ($75.0M at ~$187.50) and the **2026-08-10
  authorization increase to $750.0M with the stock at ~$210-230** sit ABOVE it →
  **condition-2 CAPITAL-ALLOCATION FLAG on the current vintage**, stated with [E4-13]
  humility (my band, their knowledge), binding position size only — moot here, the file
  is closed. The stated program purpose includes *"to minimize the dilution to our
  shares outstanding that results from equity compensation grants"* (10-K, verbatim) —
  a dollar-budget rationale, not a discount rationale; the anti-[E5-08] wording is
  itself a tell.

**THE GUARDRAIL.**
- [x] Nothing here promotes the name; Q2 stays OUT.
- [x] The great-manager dependence is recorded at Q2 as the moat defect [E4-23] — the
  two-year record is Hochman's, and *"the moat will go when the surgeon goes."*
- [x] Manager-as-the-plan check [E2-36]: this is the true turnaround (corporate
  Pygmalion), not an excisable cancer on an intact franchise — there was no intact
  franchise (Q2). Not buyable on the manager.

- **VERDICT (recorded): IN — no disqualifier found**, under a GATE-weight declaration,
  with two live flags (guidance/promotion culture; condition-2 buyback vintage) and the
  pay-windfall noted. *An absence of found disqualifiers, not a finding of honesty
  [E5-17]. IN never promotes; the file remains closed at Q2.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

*File already closed at Q2; recorded as findings. Full series and arithmetic:
`_research 2026-09-05 EAT/eat_oe_series.md` (OCF − SBC − capex, hand-built from as-filed
vintages, cross-checked to the FY2026 filed cash-flow statement).*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
- **Short-window mean** (3-yr FY2024-26): **$368.2M** capex end / $401.6M D&A end
- **Long-window mean** (5-yr FY2022-26): **$249.0M** capex end / $270.7M D&A end
- Also displayed: 10-yr $202.3M · leave-two-out FY2020-26 (drop the two best, the ANF
  fix) **$144.5M** · pre-boom FY2016-22 **$161.2M** (the operator's asked-for base) ·
  best year ever (FY2026) $525.3M
- **Spread, conservative ends (3-yr vs 5-yr): 32.4%**
- **Combined range: ~$145M to ~$540M** — wide, and that width IS a finding: every window
  averages two different businesses (pre-wave and wave — the ACMR/ALKT
  two-businesses-in-one-mean shape, inverted upward). Named distortions: the FY2025-26
  viral surge inside every short window [E4-41]; the FY2022-23 inflation-squeeze years
  inside the 5-yr; the FY2019 sale-leaseback ($455.7M, 141 restaurants) making
  pre-FY2019 years a DIFFERENT LEASE STRUCTURE (their $170-270M OE carried owned real
  estate; today's boxes pay $192.3M/yr of rent).
- Owner earnings by year (capex end): 266.7 / 195.7 / 169.0 / 28.7 / 125.7 / 259.3 /
  83.3 / 57.0 / 197.1 / 382.3 / 525.3 (FY2016→FY2026)
- **Maintenance capex — the (c) judgment, disclosed:** the [E3-44] D&A default and total
  capex nearly COINCIDE at the current level (FY2026 capex $231.9M vs D&A $218.7M) —
  the anti-railroad. **(c) is judged at TOTAL capex PLUS finance-lease ROU additions**
  (~$25M/yr; $53.7/17.9/24.5M FY2024-26 — they are restaurant assets acquired outside
  the capex caption, the DRI-run treatment), so judged (c) ≈ $255-260M at the current
  fleet, because: (i) the filer's own program says maintenance of competitive position
  requires reinvestment — "modern Greenville" re-images, 60-80 remodels in FY2027 then
  ~10% of the fleet annually (Item 1); (ii) guided capex $265-285M (FY2027) sits ABOVE
  D&A; (iii) FY2026 actually UNDER-spent its own capex guidance ($231.9M vs $270-290M
  guided) — the filed level may understate the required level, direction [E3-44]
  conservative. 3-yr mean with finance-lease additions: ~$336M.
- Stock compensation subtracted in full [E5-06]: yes, every year ($32.2M FY2026); the
  reported charge as floor [E3-70] noted — options are a small share of grants (PSUs/RSUs
  dominate), no material repricing found.
- Working-capital increment: inside OCF from the audited line (gift-card liability,
  payables detail transcribed) — the [E2-23] carve-out applied by construction.
- **JUDGED OE: ~$340M** — a [E4-41] wave normalization, stated as the judgment it is:
  ~35% below the FY2026 print ($501M with finance-lease (c)), a bit below the 3-yr mean,
  2.1x the pre-boom base. Basis: the level HELD through four lapped quarters (the filed
  fact that forbids full reversion to $145-160M today), while the virality that built it
  is exogenous, decaying, and non-ownable (the finding that forbids capitalizing $500M).
  Flow-through check (arithmetic mine): each −5% of Chili's traffic ≈ −$265M company
  sales ≈ −$65-80M of OI at the filed ~25-30% incremental margin; judged OE equals the
  FY2026 level less roughly a 10-12% traffic give-back.

### Great, good, or gruesome? **[E4-20]**
- [x] **good** (with the wave caveat): attractive return earned also on added capital —
  remodel/re-image dollars currently earn against a $5.0M-AUV base, and even the bad
  years held NTOA returns >30% because the estate is leased (capital-light by
  structure). Not GREAT: the return's durability is the Q2 failure — the high rate is
  the wave's print, not a franchise's. Not gruesome: it does not eat capital.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream: **MARGINAL** — large today ($789M OCF), but the stream
  doubled in two years on a viral surge; "reliable" is exactly what the pre-boom decade
  says it is not.
- (2) massive liquid assets: **FAIL** — $110.0M cash against $448M debt at FY2026
  (post-year-end: $378.9M revolver draw + $98M finance leases after the 8.25% redemption);
  liquidity is a $1.0bn revolver, which [E5-39] refuses to count. The MCD/SBUX/TSCO shape.
- (3) no significant near-term cash requirements: **PASS** — after the July 2026
  redemption there are NO notes outstanding at all; the revolver matures 2030-05-01;
  finance-lease payments ~$30M/yr; no dividend. Coverage [E2-54]: interest paid $38.7M
  vs OCF-less-capex $557.5M ≈ **14x after capex** (FY2026); even at the pre-boom OE base
  ($161M) coverage ≈ 5x. Accrued interest included via the paid-net line.
- Leverage, named and quantified: funded debt ~$379M (revolver, 4.90% at FY2026 rate
  structure) + finance leases $98.0M + operating lease PV **$1,311.2M** (10.8-yr WAT,
  6.2%) — lease-adjusted obligations ~$1.79bn against judged OE $340M (~5.3x; ~2.9x at
  the FY2026 print). The fixity is the exposure [E4-40]: $192.7M of FY2027 operating
  rent is contractual against a guest count that is not.

### Name the specific way THIS business dies **[E2-27, E3-24]**
1. **The wave ends — a valuation death, and its first quarter is already filed:** Chili's
   traffic printed −1.2% in Q3 FY2026 (the first negative lapped quarter). Mechanism:
   virality decays; the value war resumes (the 10-K's own risk list: "competitors
   employing our same strategies or discounting their offerings"); traffic gives back
   10-20 of the +20.2 surge points. Quantified: −15% traffic ≈ −$800M sales ≈ −$200-240M
   OI → OE reverts toward ~$250-300M; at −20% with price stuck, toward the pre-boom base
   ~$160-200M. **A real possibility** — it is what the whole pre-2023 filed record looks
   like.
2. **[E2-27] the capacity/discount spiral:** every casual-diner re-arms on value
   simultaneously (Applebee's, DRI's OG "back to basics", BLMN's turnaround), the
   share-shift nets to zero and margins carry the discounts — the category's own
   2016-2019 history. A real possibility, slower.
3. **Solvency — a low-level possibility, with a named path:** the business cannot die of
   its current balance sheet (no notes, 2030 revolver, 14x coverage). The path is the
   one ALREADY FILED ONCE: re-lever to buy back the wave at the top (the $750M
   authorization of 2026-08-10 against $107M then remaining + revolver capacity, at
   ~$210-230/sh), then the wave ends and a FY2020-class shock arrives — the FY2015-19
   sequence ($1.53bn buybacks + SLB + debt → covenant prohibition → dividend dead) was
   the dress rehearsal. Modelled: $750M drawn at ~6% adds ~$45M interest; at pre-boom OE
   $161M coverage falls to ~2.3x — survivable, but the kindness of strangers [E5-39]
   would be back in the room.
- **VERDICT (recorded): IN** — it survives; what the wave leaves of the earnings LEVEL is
  the priced question, and the width of the honest range is itself the Q4 finding
  [E4-25, E5-11].

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

# ⛔ COMPUTATION — NOT A CLEARANCE
*The file closed at Q2 (OUT). Q1-Q4 do not all show IN; under operator rule 3 this
arithmetic is reported for the queue's output contract and carries no entry language.*

**THE FLOOR, before the ranking [E4-28].** Honest pre-tax expectancy at $230.22:
**~5-8%** (judged yield 3.54% plus honest growth of ~+2-4%/yr — price-led, traffic flat,
in the filer's own flat-traffic category). Below roughly 10%: **quit on, not ranked** —
independent of the Q2 verdict.

**1. THE YIELD** (cap $9,615M = 41,765,010 × $230.22; sovereign 5.24%)
| construction | OE $M | yield |
|---|---|---|
| leave-two-out FY2020-26 | 144.5 | 1.50% |
| pre-boom FY2016-22 | 161.2 | 1.68% |
| 10-yr | 202.3 | 2.10% |
| 5-yr capex end | 249.0 | 2.59% |
| 3-yr, (c) incl. finance leases | 336.2 | 3.50% |
| **judged [E4-41]** | **340** | **3.54%** |
| 3-yr capex end / D&A end | 368.2 / 401.6 | 3.83% / 4.18% |
| FY2026, best year ever | 525.3 | 5.46% |

**Every multi-year construction yields below the bond; the single best year in company
history clears it by 0.22 points.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- growth to match the bare bond: **+1.7%/yr perpetual on judged OE** (range +1.1 to +3.7
  across constructions) — the strongest thing sayable for the price
- growth to clear the ~10% floor: **+6.5%/yr on judged** (range +5.8 to +8.5 — the
  screen's ~6.8% reproduced from my own windows)
- what the business has actually done: pre-boom OE was FLAT-to-declining for seven years;
  the two wave years did +94% and +37%; the lapped run-rate (FY2026 quarterly traffic
  ~+1%, price +4.4%) supports low-single-digit nominal growth IF the level holds — and
  the [E4-35] base rate stands against the floor case.

**3. WHAT YOU ARE PAID**
- at judged OE: **−1.70 points under the sovereign** (3.54% vs 5.24%)

**WHERE CERTAINTY IS PRICED [E3-42]:** sovereign used **5.24%** — the bare rate, no
per-name premium. Certainty was already exercised once, at the judged-OE normalization;
no second margin is stacked on the computation below.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero-growth at the sovereign
(OE ÷ 0.0524 ÷ 41.765M shares):
- conservative (leave-two-out / pre-boom): **~$65-75 per share**
- 5-yr window: **~$115** · **judged: ~$155** · 3-yr window: **~$155-185**
- generous (FY2026 print annuitized): **~$240**
- **current price $230.22** — ABOVE the entire multi-year zero-growth band; the market is
  paying for the best year ever as the permanent level, plus a little.
- At the ~10% floor: **~$35-95 per share, judged ~$80.**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict: honest pre-tax expectancy **~5-8% vs ~10% → quit on**; the ranking lines
  are not filled in. (For the record the name would also rank below the bond itself.)

**WHICH BAR?**
- [x] **Screamer test [E4-01]** — price vs the conservative case: $230.22 is above the
  WHOLE zero-growth range (outcome three: no). No margin added on top.
- **Windage count: 1** — the [E4-41] judged-OE normalization. The finance-lease addition
  to (c) is a construction (DRI-run consistency), not windage; the conservative END of
  the displayed range is a display, not a second margin.

- **VERDICT: none — Q5 never opened.** The file closed at Q2. This section is arithmetic
  under operator rule 3, reported because the queue's contract requires a price.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened — the file closed at Q2.** One pre-commitment is recorded anyway, because
the Q2 verdict itself carries a dated reopen test [E1-02]:
- **Reopen test (written at Q2):** if the FY2027 10-K (due ~Aug 2027) files a THIRD
  consecutive positive Chili's traffic year with price at or above FAFH inflation —
  three lapped years, the five-year window then clean of the viral base — the wave
  classification is wrong and Q2 is re-run. Secondary watch: the FY2027 quarterly
  traffic prints (10-Qs from ~Oct 2026) and whether the buyback re-levers the balance
  sheet above ~$1bn while the stock sits above the judged band (the named solvency path).

---
## SELF-AUDIT
- [x] Questions answered in order; run stopped at Q2 (OUT); Q3-Q4 recorded as findings
  per the DRI precedent, Q5 headed COMPUTATION — NOT A CLEARANCE, Q6 not opened
- [x] No question marked IN carries an "unverified" or "provisional" caveat (Q3's
  metric-switching and no-restatement claims are SCOPED to the documents read, stated
  as such, and sit inside a recorded-finding section, not a gate)
- [x] No UNRESEARCHED verdicts issued; the Q2 reopen test is a dated work order attached
  to a CLOSED verdict, not a hedge
- [x] Step 0: FY2026 10-K read (MD&A, cash-flow detail lines, footnotes), accession
  0000703351-26-000029; OCF $789.4M cross-checked filed-statement-to-XBRL
- [x] Owner earnings on multi-year means; five windows displayed; (c) disclosed as a
  judgment (total capex + finance-lease ROU additions), with the [E3-44] default noted
  as nearly coincident
- [x] Competitor row filled from filing-sourced workpapers (EAT + DRI/TXRH/CAKE/BLMN);
  limits stated (Applebee's franchisor P&L; differing fiscal year-ends; [E3-61])
- [x] Sovereign 5.24%, USD, US Treasury daily par yield curve (issuing authority),
  2026-09-04, struck fresh
- [x] Value as round-number ranges; one bar (screamer); windage count 1
- [x] Price $230.22 dated 2026-09-04, aggregator (Yahoo chart API), flagged — Stooq now
  behind a JS challenge wall (gotcha for future runs)
- [x] Committed after Step0/Q1, Q2, Q3; Q4 survived a session kill inside the
  coordinator's preserve commit; Q5/close committed below

**DEFECTS CONFESSED:**
1. The brief said "H1 FY2026 filed data decides" — the FULL FY2026 10-K existed and
   decided better (four lapped quarters, not two). Stale brief, favorable direction.
2. run.py share basis again (44.8M weighted vs 41.77M cover) — cap overstated 7% by the
   tool; corrected by hand. Queue-wide defect, previously logged.
3. Q4's preservation commit (27eabfb, by the coordinator at the session kill) was broad
   and swept parallel-EFX files — the SBUX/ACLS broad-add defect repeated structurally.
4. Older-year D&A (FY2016-23) taken from the XBRL Depreciation tag, not re-transcribed
   from each filed cash-flow statement (FY2024-26 transcribed); affects only the display
   of the 5-yr D&A end, no verdict.
5. Chili's-only OE is not filed (segment note gives OI, not cash flow) — the judged OE
   treats the company blended; Maggiano's decline (~$16.5M segment OI) is inside it.
6. FY2027 Q1 (Sept 2026) not yet filed at run date; the reopen test therefore dates to
   the first FY2027 10-Q, ~Oct 2026.

## REGISTER
- Verdict: [x] **OUT (about the business)** — at Q2
- One line: **The attacker's two-year traffic miracle is real, filed, and made of a wave
  — value pricing plus virality on a brand whose own prior decade (six negative-traffic
  years in eight, a 6.0% margin) proves the marketplace, not the position, sets the
  outcome; and the price pays for the best year ever as if it were permanent.**
