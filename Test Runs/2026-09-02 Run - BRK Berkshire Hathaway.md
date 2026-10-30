# Company Run — Berkshire Hathaway (BRK-B) — 2026-09-02
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.
**Sector method applied:** `Framework/SECTOR METHOD - owner earnings for insurers and
float-bearing holding companies.md`, INCLUDING both 2026-09-02 amendments (WTM findings;
MKL arithmetic corrections). **This is the deliberate LAST test of that method — the name
it was derived from, run after WTM, MKL and L so the amendments arrive from outside
[E4-26]. A perfect fit here proves nothing; what proves something is whether the
amendments change the answer ON Berkshire.**

**The circularity warning, standing over the whole file:** the corpus IS this company's
management writing about itself. **[E5-19]** attributes the record to the man, the system,
luck and devotion — not the selection method. Q3 is answered from the FILINGS (10-K, proxy,
8-Ks, reserve development, post-2021 record), never by quoting the letters the framework
treats as scripture — that would be grading a self-graded exam [E2-50].

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
- rate **5.27%** · date **2026-09-01** · source **US Treasury daily par yield curve, 30-yr,
  issuing authority** (`tools/sources.py`, run 2026-09-02; FRED is the labelled fallback and
  was not needed)
- FX: none. Earnings are predominantly USD; BHE and insurance carry non-USD operations
  (see the multi-currency gap, stated at Q5 — the reporting-currency sovereign is used and
  the choice disclosed as unresolved, per the sector method's FINDING 8).

**STAGE 0(a) — THE SHARE COUNT, HAND-READ OFF THE COVER (the standing $473M-cap / 4,683%-
yield screen artifact is disposed of in `ADDENDUM 2026-09-02 (3)`):**
- 10-Q cover, filed 2026-08-10, period 2026-06-30, accession **0001193125-26-341032**,
  verified this session by `python Screens/cover_shares.py BRK-B`:
  **Class A 488,450 · Class B 1,408,035,161**
- The A converts 1:1,500 (charter; certificate of incorporation). Economic count =
  488,450 × 1,500 + 1,408,035,161 = **2,140,710,161 B-equivalent shares**
- Price **BRK-B $505.24** (2026-09-02, aggregator, live quote only, flagged). BRK-A
  $758,500 = $505.67/B-equiv — a 0.08% premium, the classes price as equivalent.
- **Market cap ≈ $1,081.6bn** (2,140,710,161 × $505.24)

**STAGE 0(b) — is this an insurer, a float-bearing holding company, or neither?**
Float-bearing holding company — the case the method was written FROM. Both ratios
(float ÷ investments AND investments ÷ equity, per the second amendment) computed at Q5
from the filed statements; the 2010 calibration reference is 41.8% and 0.45x.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- documents · dates · accession nos.: **FY2025 10-K and 2026 Q2 10-Q (0001193125-26-341032)
  — filled in as read, below**
- figure cross-checked against the filed statement (say which): **two cross-checks run.**
  (1) Prior-year reserve development: MD&A per-segment figures (GEICO +$957M favorable,
  BH Primary −$190M adverse, BHRG +$1,097M favorable) reconcile to Note 16's consolidated
  $1,854M net favorable. (2) CONVENTION 4's constructed float from the filed balance
  sheet ($174.8bn) reproduces the published ~$176bn to −0.7% — the recipe's third
  validation (MKL −1.1%).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- **Unit economics in my own words, no management language:** Berkshire is four money
  machines under one tax-efficient roof. (1) Insurance: collect premiums now, pay claims
  later; the interval funds a $176bn pool (float) that costs less than nothing when
  underwriting profits — which it has, pre-tax, in each of the last three years — and the
  pool is invested in stocks, T-bills and whole businesses. (2) A western US freight
  railroad (BNSF): near-fixed network cost, ~9.6M cars/units a year of grain, coal,
  intermodal freight; earns ~$8bn operating on ~$23bn revenue. (3) Regulated energy (BHE):
  rate-base returns on ~$185bn of rail/utility PP&E, kept inside at ~12% returns on
  retained capital rather than paid out. (4) ~70 manufacturing, service and retail
  businesses run decentralized, remitting excess cash to Omaha. The head office allocates:
  buy businesses, buy stocks, buy T-bills, buy back stock. No dividend since 1967.
- **The scarce input this business controls:** permanence of capital. Covenant-free,
  due-date-free liabilities ([E3-52]: float $176bn + deferred taxes $85.6bn) plus $369bn
  of cash and bills mean it never has to sell, never has to roll paper, and can write a
  $10bn cheque in a week when markets seize. The balance-sheet strength IS the product in
  super-cat reinsurance: cedents pay up for certainty of payment ([E2-62]).
- **Will the fundamentals look broadly the same in ten years?** Insurance, rail,
  electricity and branded consumer businesses — yes, with two stated qualifications:
  GEICO's telematics catch-up shows the auto-insurance product CAN change under it, and
  coal volumes (12.7% of BNSF units) decline secularly.
- **VERDICT: [x] IN** — the simplest very large business in the S&P: each leg is
  low-tech, stable in character, and the consolidation is disaggregated by the filer
  into leg-level P&L that reconciles ([E3-27] satisfied from the 10-K, not the letters).

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The moat claim must be stated honestly before it is tested.** Berkshire's Item 1 says of
its own core industry: *"Except for regulatory considerations, there are virtually no
barriers to entry into the insurance and reinsurance industry"* — [E2-70] restated by the
filer in the current 10-K. **The moat claimed here is therefore NOT a product moat. It is
the funding structure:** $176bn of float that has cost less than nothing (pre-tax
underwriting gains each of the last three years, and in 6 of the last 8), $85.6bn of
deferred taxes, no dividend, and a $748bn net worth that lets it retain single-event
exposures no other insurer on earth can hold. [E2-62]'s license to concentrate — **this is
the one name where the license genuinely exists**, because the loss-absorption is filed:
shareholders' equity $747.9bn (6/30/26) against Chubb, the largest P&C peer, at roughly
one-tenth that. For a cedent buying a $5-10bn cover, certainty of payment at that size has
**no close substitute** [E3-03](2), and reinsurance rates are not price-regulated (3).

- Needed or desired **[x]** · no close substitute **[x] at the structural level; [ ] at
  the product level (GEICO, standard reinsurance, freight are all substitutable)**
- not price-regulated **[x] for insurance/reinsurance/rail in the main; BHE explicitly
  fails (3) — rate-regulated by design — and is carried as [E5-40]'s ~12%-on-retention
  "good, not great" class, its regulation a floor as much as a cap [E2-59]**
- **Must the moat be continuously rebuilt? [E4-04]** No — float is replenished by writing
  ordinary insurance, and a lapse in spending narrows nothing structural. The test is
  discipline (not writing bad business), not genius. **Does success depend on a great
  manager?** The RECORD did [E5-19] — the corpus itself attributes it to the man, the
  system, luck and devotion. The man is gone from the CEO seat (Chairman since the 2025
  transition; the repurchase authority moved to the CEO by the 2025 program amendment,
  filed). **Key-person dependence is recorded HERE, at Q2, as a moat defect per [E4-23]:**
  what was personal to Buffett — inbound deal flow at favorable prices, six decades of
  allocation judgment — does not appear on any balance sheet and cannot be assumed to
  persist. What is structural — float, permanence, decentralization, the written $30bn
  liquidity floor — is filed and persists. The Mayo-Clinic test is now LIVE, not answered.

- **Primary moat metric, filing-sourced, and its trend:** float and its cost. Float
  $138bn (2020) → $147bn (2021) → $164bn (2022) → $169bn (2023) → $171bn (2024) →
  $176bn (2025) → $177.5bn (6/30/26): **+28% in five and a half years.** Cost: pre-tax
  underwriting +$1,111M (2021), −$22M (2022), +$6,913M (2023), +$11,405M (2024),
  +$9,460M (2025) → **five-year mean cost of float ≈ −3.6% a year** (a payment for
  holding the money), on ~$162bn average float. **The funding moat is WIDE and has
  WIDENED on the filed series [E4-32].**

**THE COMPETITOR ROW — required [E3-28].** A moat is a claim about *relative* position.
Berkshire has no single industry; each leg is rowed against its own peers, same metric,
same window, filing-sourced.

| Company | metric | window | figures | source |
|---|---|---|---|---|
| **GEICO** | combined-equivalent (loss%+exp%) | 2023-25 | **90.7 / 81.5 / 84.7** | BRK FY2025 10-K K-35 |
| Progressive (Personal Lines) | combined ratio | 2023-25 | **94.1 / 88.6 / 87.5** | PGR FY2025 10-K AR exhibit |
| **BNSF** | operating ratio | 2023-25 | **68.4 / 68.0 / 65.5** | BRK 10-K (opex÷revenue) |
| Union Pacific | operating ratio | 2023-25 | **62.3 / 59.9 / 59.8** | UNP FY2025 10-K |
| **BRK insurance, whole** | cost of float, 5-yr | 2021-25 | **≈ −3.6%/yr on ~$162bn** | BRK 10-Ks, [E3-69] |
| Markel | cost of float, 5-yr | 2021-25 | −2.60% on ~$4bn | this project's MKL run |
| CNA (P&C book) | cost of float, 5-yr | 2021-25 | −2.46% on ~$23bn | this project's L run |
| Loews insurance, whole | cost of float, 5-yr | 2021-25 | +4.04% | this project's L run |

- **Peers named: 5 filed rows across 3 industries, of the industries' real competitor
  sets.** Unavailable and said so: **State Farm and USAA are mutuals and file no SEC
  statements** — their positions enter through the A.M. Best market-share data Berkshire's
  own 10-K quotes (filing-sourced at one remove); Munich Re and Swiss Re are IFRS filers
  (ladder rung 4, not pulled — the reinsurance moat claim rests on scale and cost of
  float, both filed, not on a peer combined ratio). The row's limit [E3-61] stands:
  identical structures, opposite conduct.

**What the row shows, both directions, at full strength:**
1. **GEICO — the legend is DEAD and the current fact is better than the obituary.**
   Market share by successive 10-Ks quoting A.M. Best: **#2 at 13.8% (2019 data) → #3 at
   13.8% (2022 data) → #3 at 11.6% (2024 data)** — passed by Progressive, then 2.2 points
   of share lost in two years. Progressive's Personal Lines earned premium ($70.8bn 2025)
   is now 1.6x GEICO's ($44.5bn). THAT is the decade of telematics lag, in filed numbers.
   **And yet:** GEICO's combined-equivalent BEAT Progressive's in 2024 (81.5 vs 88.6) and
   2025 (84.7 vs 87.5), policies-in-force grew through 2025, and premiums written rose
   5.3%. The 2025 expense ratio jumped 9.7% → 12.4% on advertising — GEICO is buying
   growth back with underwriting profit it now actually has. A shrunken #3 earning better
   margins than the attacker is a NARROW moat, not none, direction newly positive.
2. **BNSF is the second-best of two.** Trails UNP by 6.1 / 8.1 / 5.7 points of operating
   ratio in each of the last three years. Physical series [E4-55]: cars/units **10,698k
   (2018) → 9,622k (2025), −10.1%**; ex-coal −4.5%. Deflated [E4-55/E3-62]: revenue per
   car/unit $2,150 (2018) → $2,427 (2025), **+12.9% nominal over seven years against
   ~+28% CPI — real price per unit fell ~12%** and real revenue fell ~15%. A western-rail
   duopoly position is a real asset (no close substitute for its long-haul corridors),
   run second-best, with negative real pricing. NARROW, direction flat (2025 OR improved
   7.8% while UNP's was flat — the gap closed 2.4 points in one year).
3. **The reinsurance/funding structure has no peer row because no peer exists at the
   metric that matters** — cost of float at scale: Berkshire's −3.6% on $162bn against
   the best comparable this project has measured, Markel's −2.60% on ~$4bn. [E2-53]
   dominance class: at the super-cat end, position, not execution, sets the economics.
4. **[E4-37] inverse metric — pricing conduct, filed:** BHRG walked away from $1.7bn of
   property premium in 2025 because "increased competition and lower rates"; GEICO took
   rate +7.8% in 2024 and accepted PIF decline rather than underprice. Yawn-pricing
   discipline on both sides. No prayer sessions in evidence.

**[E2-49] METRIC-SWITCHING AUDIT — the loaded test from the brief, and it does NOT fire
on the filings.** Sweep performed this session: the word "combined ratio" appears **zero
times in the FY2025 10-K — and zero times in the FY2023 and FY2020 10-Ks as well.** This
is not a withdrawal that followed deterioration; Berkshire's 10-Ks have not used the term
across the whole six-year window examined, through both the terrible GEICO year (2022,
104.8 combined-equivalent) and the record years. What IS published is unchanged in form
across all three vintages: loss ratio and expense ratio per segment to one decimal, float
level, cost-of-float statement, PIF percentage changes, BNSF cars/units by group, premium
tables. The components of the combined ratio are all there, every year, computable in
under two minutes — the [E2-26] half-owner standard met by disclosure of parts. The
letter-level BVPS-table withdrawal (2018) carried a stated economic rationale
(repurchases below IV make book per share systematically misleading) and preceded no
deterioration in the metric — the Markel-carve-out pattern, not the HD/DKS pattern.
**Reported as a negative finding at full strength because the brief loaded the test.**

- **Untapped pricing power [E3-33]:** No. BHE is rate-capped, BNSF prices below
  inflation, GEICO's market is price-elastic. The moat is cost-of-funding, not pricing.
- **The two-characteristic test [E2-44]:** (1) raise prices with flat demand — GEICO yes
  (2024, filed), BNSF no in real terms; (2) grow dollar volume with minor incremental
  capital — the float system yes ($38bn of float growth in five years on zero incremental
  equity), rail/utility emphatically no (capex $20.9bn vs D&A $13.5bn).
- **Class: [x] WIDE (the float/balance-sheet system, widening on filed series) with two
  NARROW product legs (GEICO, BNSF) and one regulated [E5-40] "good" leg (BHE).**
- **Direction: funding moat widening; GEICO share lost then stabilized with superior
  underwriting; BNSF gap to UNP closed 2.4 points in 2025 after years static.**
- **The [E4-23] defect is recorded and stands: the deal-flow-and-judgment component of
  the legend was personal and is now unevidenced either way. Q6 monitors it.**
- **VERDICT: [x] IN** — on the filed structure, not the legend. The eighteen-run streak
  does not get a vote [E4-26]; neither does the legend.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**SOURCE DISCIPLINE, STATED FIRST: everything in this Q3 is from the DEF 14A of
2026-03-13 (acc. 0001193125-26-106253), the FY2025 10-K, the 2026 Q2 10-Q, and the 2026
8-K record. The shareholder letters were NOT used — the corpus is this management writing
about itself, and quoting it here would grade a self-graded exam [E2-50, E5-19].**

**STEP 1 — DECLARE THE WEIGHT CASE.**
- [x] **Daily execution** — insurance is the corpus's own worked example: *"their only
  products are promises"* [E2-70], restated in this filer's Item 1 (virtually no barriers
  to entry). Underwriting discipline is a have-to-be-smart-every-day business.
- [ ] **Control** — no; listed, liquid.
- [ ] **Leverage** — no: equity $747.9bn against $1,263.1bn of assets (~1.7x), and the
  operating debt sits non-recourse at BNSF/BHE; parent-level leverage is trivial beside
  $365bn of cash and bills.
**Case declared: one determinant high → Q3 is a BINARY GATE. No price compensates.**

**Honesty — binary, permanent, filings-based [E5-16].** No disqualifying conduct found in
the current record. Dated matters read: the 2023-24 Pilot litigation (resolved; Berkshire
took 100%); the BHRG-affiliate Chapter 11 settlement charge of $490M (2024, disclosed
with amount and venue in the 10-K); PacifiCorp wildfire litigation (Q4 material, accruals
disclosed and quantified). Sokol (2011) stands in the corpus as the calibration case
[E5-26], not a current matter.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30].** All prompts read; none fires:
- [ ] weak accounting — none found; the auditor (Deloitte, $61.8M audit fee, disclosed)
  issued a clean ICFR opinion; pensions immaterial to the whole.
- [ ] unintelligible footnotes — the retroactive-reinsurance and float mechanics are
  genuinely complex and are explained with definitions and rollforwards; the [E2-26]
  test is met by the disaggregation (see below).
- [ ] trumpeted projections — **zero guidance culture: no earnings projections anywhere
  in the 10-K, 10-Q or 8-K record [E5-30]'s ratchet never started.** The filer says the
  OPPOSITE of trumpeting: underwriting results "were exceptional compared to results over
  longer periods. However, earnings may decline in the future" — management talking its
  own record DOWN in an SEC filing, and calling its own headline investment gains
  "generally meaningless in understanding our reported periodic results."
- [ ] serial share issuance — the reverse: share count has only fallen; stock is never
  used for compensation (proxy: "Berkshire never intends to use Berkshire stock in
  compensating employees"); acquisitions are cash (OxyChem $9.4bn, Taylor Morrison
  $6.8bn — no shares issued). [E5-44] never triggered.
- [ ] EBITDA / adjusted promotion — "EBITDA" does not appear in the FY2025 10-K's
  discussion of results; no non-GAAP earnings measure is promoted anywhere in the filing.
- [ ] filed-figure tells — reported growth is the opposite of smooth (net earnings $96.2bn
  → $89.0bn → $67.0bn) and the filer refuses to smooth it; effective tax rates 18-23%,
  with the 2024 cash-tax catch-up on the equity sales visible in the cash-flow statement
  (income taxes line −$8,163M), i.e. taxes were PAID as gains were realized [E4-30] clean.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity, multi-year, gains
stripped (the filer's own position that they are meaningless period-to-period):
| year | operating earnings after-tax* | avg BRK equity | rate |
|---|---|---|---|
| 2023 | $37,350M | $517.3bn | 7.2% |
| 2024 | $47,437M | $605.3bn | 7.8% |
| 2025 | $44,486M | $683.4bn | 6.5% |
*(underwriting + insurance investment income + BNSF + BHE + MSR + other, after tax.)*
**A 6.5-7.8% operating return on equity, without leverage or gimmickry — LOW, and the
reason is disclosed on the face of the balance sheet: $365-373bn of the equity sits in
T-bills yielding ~4-5% pre-tax.** The number is honest and mediocre, and the mediocrity
is the cash drag. This is the arithmetic seed of the Q5 third-element question. (With
investment gains included, as reported: 18.6% / 14.7% / 9.8% — shown, not used.)

**The half-owner test [E2-26]: PASS, and it is the strongest disclosure pass this project
has recorded.** The filer publishes: per-segment underwriting with loss and expense
ratios; the float figure with its full construction; prior-year reserve development
quantified BY DIRECTION AND SEGMENT including the adverse pockets (BH Primary +$190M
adverse 2025, BHRG casualty increases named, retro +$261M) inside a favorable total;
catastrophe losses per event threshold ($150M) per year; the cost basis AND market value
of every major equity position; the impairments (KHC $5.0bn, OXY) taken to market with
the reasoning; and the KHC board-seat resignations with the accounting consequence
(one-quarter lag). [E2-67]'s published-self-restatement standard — the founder invented
it — is met by the current filing's development table with direction stated.

**The institutional imperative [E2-30] — scored:**
- [ ] resists change — no: exited airlines (2020), halted buybacks 6 quarters, resumed;
  authority structures amended and filed.
- [~] acquisitions materialize to soak up funds — **the live one to watch, honestly
  scored:** $16.2bn of acquisitions plus $4.8bn of buybacks in the new CEO's first seven
  months after 18 months of nothing. Both deals are in-perimeter (OxyChem adjacent to the
  27% OXY stake; Taylor Morrison extends Clayton/HomeServices), cash-funded, and total
  ~6% of the cash pile — not a soak-up on the filed numbers, but the cadence change is
  real and Q6 monitors it.
- [ ] staff studies for the leader's craving — no evidence; no banker-promoted process
  appears in either deal's 8-K/10-Q record.
- [ ] peer imitation — none; no peer holds $365bn of T-bills.

**Capital allocation — the buyback conditions [E5-08, E4-31, E5-25]:**
- (1) ample funds: trivially yes — the program's own filed floor is $30bn of consolidated
  cash+bills (raised from the 2011-era $20bn), against $365bn held.
- (2) material discount to conservatively-determined IV, **tested against execution, not
  words:** 2023 $9.2bn bought; H1-2024 $2.9bn; **then ZERO for six consecutive quarters
  (Q3-2024 through Q4-2025) while the stock made record highs; resumed Q1-2026 ($235M)
  and Q2-2026 ($4,527M at $476-488/B-eq)** after the post-transition decline. The
  program SPENDS LESS AS THE PRICE RISES and more as it falls — the exact inverse of the
  ORLY dollar-budget pattern this queue convicted two days ago. Execution is consistent
  with a discount discipline. Current price $505.24 sits 3.5% above the June average
  paid.
- (3) [E4-31] informed register: the two-column disclosure this method is literally built
  from, plus the development table. Pass.
- **[E2-51] refusal tell:** the 2025 zero-repurchase year coincided with record-high
  prices — a refusal AT a premium is the condition-2 discipline, not the tell.
- **Comp structure, verified from the proxy, not assumed:** Abel $22,000,000 salary, no
  bonus, no stock, $17,500 DC contribution; Jain identical; Buffett $100,000 (unchanged
  40+ years) plus $289,488 of security services; CFO $4.3M. Committee policy: "neither
  the profitability of Berkshire nor the market value of its stock are to be considered
  in the compensation of any executive officer" — [E3-50]'s stock-price-targeting flag
  is refused BY WRITTEN POLICY. **One forward item, recorded: the proxy says the
  Governance Committee "will be working with Mr. Abel during the next several months to
  evaluate what, if any, changes will be necessary" to compensation. The structure is
  Buffett's; whether it survives him is a Q6 monitoring item, not a present flag.**
- **[E4-23] succession, assessed from what is filed:** announced 2025-05-03, board voted
  unanimously 2025-05-04, effective 2026-01-01, disclosed in the proxy and 8-K record;
  the repurchase authority was re-papered to the office of CEO (not the person) "after
  consultation with the Chairman." Jain remains Vice Chairman-Insurance. The transition
  is the most-documented succession in the S&P — and its first seven months of filed
  actions (two cash acquisitions, resumed price-sensitive buybacks, yen notes rolled)
  are behaviorally continuous with the prior regime.

**THE GUARDRAIL — checked.**
- [x] Nothing here promotes the name; Q3 cannot repair the Q2 defects (GEICO share loss,
  BNSF second-best) and cannot substitute for Q4.
- [x] Key-person dependence is recorded at Q2 as a moat defect [E4-23], not here as a
  strength.
- [x] No manager is the plan; the franchise question was decided on the filed structure.

- **VERDICT: [x] IN — as the absence of found disqualifiers, under a binary gate, with
  [E5-17]'s cap: this is not a finding that the managers are honest.** The gate was
  applied to the post-2021 record and the current officers, not to the legend.

## Q4 — WILL IT SURVIVE?

### Owner earnings — SECTOR SUBSTITUTION APPLIED AND SAID SO
**For the float-bearing core there is no owner-earnings formula; the corpus values two
components and a judgment [E2-61, E3-69, E5-46-50], and the MKL run's [MF 7] ruling
holds: the capex band does not bite on a securities portfolio — what must be maintained
is reserve adequacy.** The earnings display below is therefore componentized; the full
two-component arithmetic is Q5's.

**The non-portfolio earnings stream, by year (after-tax, from the MD&A disaggregations of
the FY2023 and FY2025 10-Ks — underwriting + BNSF + BHE + MSR):**
| 2021 | 2022 | 2023 | 2024 | 2025 | H1-2026 |
|---|---|---|---|---|---|
| $21.6bn | $22.3bn | $26.2bn | $30.9bn | $30.4bn | $16.1bn |
- **Five-year mean $26.3bn · three-year mean $29.1bn · spread ~10%** — narrow, no
  distorted year inside the window, [E4-25] does not close anything.
- Insurance investment income (after-tax), shown separately because it belongs to
  component 1's portfolio at Q5: 4.8 / 6.5 / 9.6 / 13.7 / 12.5.
- **[E4-41] — the mean is normalized DOWN for two named lucks, and this is the run's ONE
  windage:** (i) the filer itself calls 2023-25 underwriting "exceptional compared to
  results over longer periods" — the 2018-2025 pre-tax underwriting mean is **$4.0bn**
  against 2023-25's $9.3bn; normalized underwriting ≈ $4bn pre-tax (≈$3.2bn after-tax),
  removing ≈**$4.7bn after-tax** from the recent-years figure; (ii) interest income rode
  the highest short rates since 2007 — already fading (−11.9% in 2025), priced at Q5 as
  the portfolio, not as a stream.
- **Maintenance capex (c), the disclosed judgment:** consolidated capex $20.9bn vs D&A
  $13.5bn (1.55x). BNSF is the corpus's NAMED [E5-20] exception — "merely spending their
  depreciation expense will not keep them in the same place" — and BHE is rate-base
  growth by design. **(c) for the rail/utility legs is judged AT total capex** (the
  after-tax segment earnings already carry ~$13.5bn of D&A; the excess ~$7.4bn is
  treated as ~half maintenance, ~half rate-base growth that earns [E5-40]'s ~12%, and
  the conservative displays below simply use reported after-tax earnings, which the
  rate-regulated structure ties to capital actually consumed). For the MSR leg capex ≈
  D&A and the [E3-44] default stands.
- Stock compensation [E5-06]: no Berkshire stock is used in compensation at all (proxy,
  written policy) — the subtraction is zero at the parent; subsidiary cash incentive
  plans are already inside operating expenses.

### Great, good, or gruesome? **[E4-20]**
- **The float system: GREAT** — funding that pays Berkshire ~3.6%/yr to hold it, grown
  $138bn → $177.5bn with no incremental equity.
- **BNSF + BHE: GOOD, by the corpus's own number** — [E5-40]'s ~12% on retained utility
  capital is "quite satisfactory"; capital-hungry but each retained dollar earns a
  regulated/duopoly return. Not gruesome: returns are earned on the added capital.
- **MSR: good** — $13.6bn after-tax on modest incremental capital.
- **The $365bn T-bill pile: the gruesome-shaped corner of a great business** — capital
  retained at ~4-5% pre-tax. It is the Q5 question, not a survival question.

### Staying power — score all three **[E5-11]**, with the [E2-61] substitution
- **(1) large and reliable earnings: PASS.** Four independent legs; worst recent year
  (2022, GEICO's 104.8 combined year) still produced $22.3bn after-tax from the
  non-portfolio legs.
- **(2) massive liquid assets — READ AS RESERVE ADEQUACY AND NET WORTH [E2-61], never
  cash: PASS on the substituted test.** Net worth $747.9bn (6/30/26), the largest of any
  company on the US register. Reserve adequacy: net FAVORABLE prior-year development
  three years running ($1.9bn / $2.3bn / $3.5bn = 1.7% / 2.2% / 3.5% of opening
  reserves), with the adverse pockets disclosed by name. **The accident-year
  decomposition — the instrument that convicted MKL and acquitted CNA — ACQUITS
  BERKSHIRE: current-accident-year combined ≈ 93.6 (2023) / 87.7 (2024) / 89.3 (2025),**
  built from Note 16's CAY incurred (58.2/57.6/59.2bn) against P&C earned premium
  (83.6/83.3/78.3bn) plus the segment expense ratios. The book written THIS year makes
  money without releases. And the literal cash is $365bn of bills with "safety over
  yield" stated in the filing.
- **(3) no significant near-term cash requirements: PASS** — no dividend since 1967, no
  guidance ratchet, float has no covenants and no due dates [E3-52], debt ladder runs
  2027-2056, and the walking-dead tell ([E2-61] redoubled writing to keep cash flowing)
  reads NEGATIVE: BHRG shrank property premium $1.7bn into softening rates.
- **Coverage [E2-54]:** consolidated interest expense ≈ $5.4bn (BNSF 1.1 + BHE 2.6 +
  manufacturing 1.2 + other) against $51.7bn pre-tax operating earnings and $25bn of
  OCF-less-capex — all interest, payable and accrued, comfortably met out of current
  cash flow net of ample capex.
- **Leverage, named and quantified [E4-16]:** notes payable $128.6bn total (I&O $43.3bn
  incl. BHFC; RUE $85.3bn, non-recourse to the parent in the main) = 0.17x equity,
  against $365bn of bills. Yen tranches (8-K 2026-04-16: ¥265bn+ across 2029-2056)
  fund yen assets — a matched book, with remeasurement gains/losses disclosed in
  "other." Float $177.5bn and deferred taxes $90.2bn are [E3-52] liabilities: no
  covenants, no due dates.
- **[E2-64] strength as an offensive asset:** the storm balance sheet is also the buying
  balance sheet — OxyChem closed January 2 with cash on hand, no financing contingency.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]** — exposure, not
experience:
- **The fast mechanisms, quantified and dismissed honestly:** (i) reserve deficiency —
  a 10% miss on $152bn of net claim liabilities (incl. retro) = **$15.2bn pre-tax ≈ 2%
  of net worth**: absorbed, *a low-level possibility* given three years of favorable
  development and profitable accident years; (ii) the stacked catastrophe — a $25bn
  single-event loss (≈5x the largest recent annual cat total) PLUS a 50% equity-market
  decline (−$160bn, non-cash) PLUS a freight recession: equity falls to ≈$550bn, float
  pays claims from $365bn of bills, nothing is force-sold, no covenant exists to trip.
  **No modeled combination of filed exposures kills it within a decade. That sentence
  is itself the [E2-62] license, written from the balance sheet.**
- **The real death is SLOW and the corpus names it [E5-45, E5-50]: the ABCs plus
  fifty-cent retention.** 387,800 employees, a founder-built compensation and
  reserving culture whose survival under new management is the open question, and
  $365bn earning bill rates. If the retained pile compounds at ~4% while the
  opportunity floor is ~10% [E4-28], the value forgone is ≈**$22bn a year — 3% of net
  worth annually, compounding** — the GM/IBM/Sears path at Berkshire scale: never a
  bankruptcy, a two-decade fade of returns toward the bond. **Likelihood: the drag is
  the CURRENT FACT (likely); its permanence is the Q5 third-element judgment.**
- Likelihood scored: catastrophic impairment [ ] likely [ ] a real possibility
  [x] **a low-level possibility** · slow-fade cash drag [x] **likely as a present
  fact**, priced at Q5 rather than closing Q4 — survival is not in question; return is.
- **VERDICT: [x] IN** — the strongest Q4 pass available on the US register, and the
  verdict explicitly does NOT carry the return question forward as settled: that
  belongs to Q5.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**Q1-Q4 all returned IN. Q5 opens legitimately — the second name in this queue ever to
open it (ORLY was the first), and the first under the sector method.**

### STAGE 0(b), BOTH RATIOS — the second amendment's requirement, against the method's
own 2010 calibration point (41.8% / 0.45x):
| | 2010 [E5-46] | BRK now (6/30/26) | MKL | L consol. | CNA | WTM |
|---|---|---|---|---|---|---|
| float ÷ investments | 41.8% | **24.6%** | 50.3% | 41.8% | 45.8% | 22.0% |
| investments ÷ equity | 0.45x | **0.96x** | 2.01x | 2.96x | 4.34x | — |
**What they imply, stated:** the portfolio has outgrown the float — float now funds only
a quarter of it, so [E5-46]'s "free funding" condition carries LESS of the valuation than
when the method was calibrated, and the T-bill pile carries more. Investments are still
smaller than equity — **Berkshire remains the only filer in the four-name panel where
counting the portfolio gross at market cannot double-count** (CONVENTION 5's rationale
holds here and only here) — but at 0.96x the license is twice as stretched as in 2010.

### COMPONENT 1 — investments at market, GROSS VS NET STATED [E5-46, MKL amendment]
All figures 6/30/26, from the filed balance sheet and Note 5 fair values ($bn):
| construction | $bn | per B-share |
|---|---|---|
| **GROSS: I&O cash 35.1 + T-bills 324.9 + fixed 17.0 + equities 323.8 + KHC/OXY/Berkadia at fair value 21.0 − unsettled bills 0.8** | **721.1** | **$337** |
| NET of float 177.5 (the L-run discipline) | 543.6 | $254 |
**Gross is used, and here is the argument, not just the choice:** [E5-46] licenses gross
on the condition that underwriting breaks even; Berkshire's underwriting made money in
each of the last three calendar years, six of the last eight, and — decisive — on the
CURRENT accident year in all three years tested at Q4. The funding condition is met in
the strongest form the panel has seen, and investments < equity means the gross count
cannot exceed what shareholders own plus what costless float funds. The net-of-float
figure is displayed because the method now requires both. RUE operating cash ($5.5bn)
excluded as working cash; noncontrolling interests $2.3bn, de minimis, not netted.

**[E3-71] — the deferred tax on unrealized gains, valued as the ADVANTAGE of an
interest-free loan, never face, never zero.** Face: **$48.4bn** DTL on "investments,
including unrealized appreciation" (Note 20, 12/31/25 — the 10-Q does not break out the
component; stated). Valued: the liability pays nothing, has no due date, and falls due
only on realization at a pace Berkshire controls; discounted at the sovereign it is
worth ~$29bn (10-yr deferral) to ~$17bn (20-yr). **Judged charge: ~$24bn (≈half of
face), a disclosed judgment.** Component 1 after charge: **$697bn ≈ $326/B-share.**
*(The $34.8bn PP&E deferred-tax item is the same animal for the rail/utility legs but
those legs enter as earnings, not assets, so it is left where it is — stated.)*

### STEP 2 — COST OF FLOAT, DIAGNOSTIC, NOT ADDITIVE [E3-69, first arithmetic correction]
| | 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr |
|---|---|---|---|---|---|---|
| pre-tax underwriting $bn | +1.11 | −0.02 | +6.91 | +11.41 | +9.46 | +28.87 |
| avg float $bn | 142.5 | 155.5 | 166.5 | 170.0 | 173.5 | ~161.7 |
| cost of float | −0.8% | +0.0% | −4.2% | −6.7% | −5.5% | **≈ −3.6%/yr** |
- Float ÷ premium ≈ 1.98x ([MF 13] duration context: a long-tail blend including retro).
- The 2018-2025 mean cost is ≈ −2.5% on the longer window — negative on every window.
- **The diagnostic's judgment: the float is not merely free, Berkshire is PAID ~3.6% a
  year to hold $162-177bn of other people's money, while the sovereign pays 5.27%. The
  funding advantage is worth roughly $14bn a year pre-tax against borrowing the same
  sum. Underwriting profit enters the sum ONCE, in component 2 — nothing here is added.**
- CONVENTION 4 constructed float: $174.8bn vs published ~$176bn = **−0.7%, third
  validation** (recipe retained; residual is the filer's exclusion of discount-rate AOCI
  on long-duration liabilities, which the recipe cannot see — stated).

### COMPONENT 2 — pre-tax earnings of everything else, dividends and interest removed
[E5-48], WITH THE ASU 2016-01 JUDGMENT DISCLOSED [MF 15]
Exact construction from the segment note: total operating businesses EBT less insurance
pre-tax investment income:
| | 2023 | 2024 | 2025 | 3-yr mean |
|---|---|---|---|---|
| operating EBT | 43.6 | 53.9 | 51.7 | |
| less insurance inv. income | −11.6 | −16.7 | −15.3 | |
| **component 2, pre-tax** | **32.1** | **37.2** | **36.5** | **35.2** |
- Corporate/eliminations (+$1.3bn 2025) EXCLUDED — it contains the parent's T-bill
  interest, which belongs to component 1; leaving it out avoids the double-count in the
  direction that hurts the seller of this thesis.
- **The ASU 2016-01 problem, and the finding: at Berkshire it is worth ZERO.** The row
  names only "dividends and interest"; at WTM the unnamed unrealized marks were worth
  27% of component 2 and at Loews 175%. Berkshire segregates ALL equity marks in a
  separate "Investment gains (losses)" line that never touches either component — the
  one filer in the panel where the 2015 row still fits the 2026 accounting. Both
  constructions are therefore IDENTICAL here; shown by construction, not assumption.
- **[E4-41] normalization (the run's ONE windage, declared):** the filer itself calls
  2023-25 underwriting exceptional; substituting the 2018-2025 mean ($4.0bn) for the
  3-yr mean ($9.3bn) gives **normalized component 2 ≈ $30bn pre-tax.**

### THE SUM, AS A ROUND-NUMBER RANGE [E4-01]
| construction | $bn | per B-share |
|---|---|---|
| conservative: C1 697 + normalized C2 at the 10% floor rate (300) | 997 | **≈ $470** |
| central: C1 697 + normalized C2 at the sovereign (569) | 1,266 | **≈ $590** |
| generous: C1 697 + 3-yr C2 at the sovereign (668) | 1,365 | **≈ $640** |
> ### **PRICE: $505.24** (BRK-B, 2026-09-02, aggregator, flagged) · cap **$1,081.6bn**
> ### **VALUE, ROUND NUMBERS: ≈ $470 / $590 / $640 per B-share**
> ### Book value per B-share **$349**; price/book **1.45x**

**1. THE YIELD** — look-through pre-tax income (component 2 + portfolio cash income +
[E3-04] look-through retained investee earnings ≈ $61-66bn) ÷ cap:
**5.6% (normalized) to 6.1% (3-yr mean) · sovereign 5.27%**
**→ +0.4 to +0.9 points OVER the sovereign — the first name in this queue's history
above the bond on EVERY construction at the full market cap.** (The operating businesses
alone, at the $385bn residual price after component 1: **7.8-9.2% pre-tax yield.**)

**2. WHAT THE PRICE ALREADY ASSUMES** — to justify $505 at the sovereign needs the
normalized construction plus ~nothing: the central sum ($590) sits 17% ABOVE the price.
To clear the [E4-28] floor needs ≈ **4.4%/yr perpetual growth** on the whole; realized:
component-2 after-tax per-share grew **≈ +8.9%/yr** (2021-25), book per B-share
**+11.6%/yr** (2021-26H1). The needed rate is well below the realized rate — this is
the closest any name has come to the floor, and [E4-35]'s base-rate burden (a caution
against needing 15%) does not bite at 4.4%.

**3. WHAT YOU ARE PAID** — **+0.4 to +0.9 points over the sovereign** at the current
look-through yield, before any credit for growth or allocation skill.

**THE THIRD ELEMENT [E5-50] — the whole question on this name, measured, not opined
[E3-54]:** $1 of market value per $1 retained, five-year rolling, run on the CURRENT
five years, not the legend:
- Retained 2021-2025 (no dividends): $763.2bn − $444.6bn = **$318.6bn**
- Market value added: cap $537bn (end-2020: 2,315.94M B-eq × $231.87) → $1,081bn
  (end-2025, ~2,150M × $502.65) = **+$544bn**
- **→ $1.71 of market value per $1 retained. PASSES.** Through H1-2026: $1.54. Adding
  back the $47bn spent on buybacks: $1.85. *(Historical closes from the aggregator,
  flagged — the only non-filing figures in this section.)*
- The 2009 self-corrected form, reported at full strength BOTH ways: book/share grew
  11.6%/yr over the window, which **TRAILS** the S&P total return (~14%/yr, 2021-2025)
  — the book-vs-index leg FAILS while the market-value leg passes. And the cash pile:
  $365bn at bill rates is a live drag of roughly $22bn/yr against the 10% floor
  (≈3% of net worth annually); deployment resumed under the new CEO ($21bn in seven
  months, price-disciplined per Q3) but the pile did not shrink. **Judgment, stated:
  NEUTRAL — no fifty-cent-dollar evidence exists in the filed record (retention test
  passes, no overpriced deal, no scrip), and no premium for future allocation skill is
  granted: the sum above values the bills at face and the operating earnings with zero
  credit for redeployment. The Buffett premium is priced at zero; so is the Buffett
  discount.**

**THE FLOOR, before the ranking [E4-28].** Honest pre-tax expectancy at $505.24:
blend of the portfolio leg (2/3 of cap at ~4.5-7% expected pre-tax) and the operating
leg (1/3 of cap at 7.8-9.2% yield + mid-single growth ≈ 11-15%):
**≈ 6.7% conservative / 8.0% central / 9.7% generous.**
*"that's the figure we quit on … whether short rates are 6 percent or 1 percent."*
**Every construction sits below roughly 10%. Berkshire is not ranked. It is quit on —
and the file records plainly that under v4.0's deleted "there is no hurdle — it ranks"
this name would have ranked #1 in the queue at +0.4 to +0.9 over the sovereign. The
restored floor is exactly the rule that closes this file.**

**WHERE CERTAINTY IS PRICED [E3-42]:** sovereign used **5.27%, bare** — no per-name
premium anywhere. Certainty was spent once, at the end margin (see Bar below).

**WHICH BAR: [x] Bar 2, the screamer test [E4-01].** Price $505.24 against the range
$470-$640: **INSIDE the range — the middle outcome: no useful conclusion, move on.**
No margin added on top. It is not startlingly low; a 7% move down would put it under
the conservative case, which is precisely what "inside the range" means.
- **Windage count: ONE** — the [E4-41] normalization of underwriting to its 8-year
  mean. The conservative row of the range is the range's own bottom boundary [E5-34],
  not a second spend; [E3-71]'s deferred-tax charge is a realistic input by rule, not a
  conservatism.

- **VERDICT: NOT IN — closed at Q5, on price. [x] the [E4-28] floor (expectancy
  ≈6.7-9.7% vs ~10%) and [x] Bar 2's middle outcome (price inside $470-$640) agree.
  Ranking position: unranked (quit on), while noting it pays more over its sovereign
  than anything else this queue has produced.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(DID NOT OPEN — Q5 closed the file on price. Watchlist re-read triggers, recorded per
[E1-02] so the re-read is pre-committed rather than improvised:)*
- **Price trigger:** below ≈ **$470/B** the price crosses the conservative sum and Bar 2's
  bottom row goes live; re-run Q5 arithmetic only (one session, the components are on
  disk).
- **Thesis-watch metrics (from this file's own defects):** GEICO market share in the next
  10-K's A.M. Best sentence (11.6% and stabilizing, or resuming decline); the
  compensation-structure decision the proxy promises "over the next several months"
  (whether the no-stock, no-metric structure survives Abel); deployment cadence vs the
  T-bill pile (bills $324.9bn at 6/30/26 — does it shrink); accident-year combined ratio
  staying under 100; the [E5-45] ABC tells aging in.
- **Next catalyst dates:** Q3 10-Q ~2025-11-02-pattern (early Nov 2026); FY2026 10-K
  ~late Feb 2027 with the first full-year Abel record.

---
## WHERE THE AMENDED METHOD STILL FAILED TO FIT — reported above the verdict, as
instructed, because it outranks it

**[BRK-MF 1] The method's center of gravity has moved off its own calibration case.**
Stage 0(b): float funds 24.6% of the portfolio today against the 41.8% the method was
calibrated on. Berkshire 2026 is less a float-levered portfolio than an operating
conglomerate with a T-bill warehouse; step 2's cost-of-float diagnostic, the method's
crown jewel, now bears on about a sixth of the market cap. The method still runs — but
on its OWN filer, sixteen years on, the answer lives mostly in steps 1 and 3, exactly
the relocation the first amendment described at WTM.

**[BRK-MF 2] "Dividends and interest removed" needs a corporate-line rule.** The parent
holds ~$160bn of bills OUTSIDE the insurance segment (the end-2024 capital
distributions); its interest income sits in "corporate, eliminations and other," which
[E5-48] never mentions. This run excluded the whole corporate line and said so. The
method document should name that rule; today it is a per-run improvisation.

**[BRK-MF 3] [E3-71] gives a treatment but no discount horizon.** Valuing the $48.4bn
DTL as an interest-free loan requires a deferral-duration guess (10-20 years spans
$17-29bn of PV). The judged ~$24bn charge is disclosed, but the method supplies no rule
for the horizon and Munger's Wesco worked example does not state his. Open.

**[BRK-MF 4] The floor and the ranking now disagree on the same name, and the method
has no vocabulary for it.** Above the sovereign on every construction (+0.4 to +0.9)
yet below the ~10% expectancy floor on every construction. v4.1 resolves it (the floor
wins; quit), but the method document — written under v4.0's "there is no hurdle" — still
says "rank against the sovereign; there is no hurdle; it ranks" in its step-4 table.
**That line contradicts the governing framework and should be amended.**

**[BRK-MF 5] Retention-test denominators are regime-mixed.** [E3-54] measured 2021-2025
retention, but 2021-2025 retained earnings were allocated almost entirely by the
founder; the CEO whose "what-will-they-do-with-the-money" is being priced has seven
months of record ($21bn deployed). The corpus's five-year window cannot yet see the
person it is supposed to grade. Not fixable by method; fixable only by time. Stated.

**And one thing that fit perfectly, reported because negatives were:** the ASU 2016-01
ambiguity that was worth 27% at WTM and 175% at L is worth ZERO at Berkshire — the
filer's presentation still matches the 2015 row it invented. The two-column method fits
its author. **A perfect fit here proves nothing [E4-26] — which is why the four
misfits above are the actual product of this run.**

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN verdict (Q5, on price)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat**
- [x] No UNRESEARCHED verdicts issued; no UNKNOWABLE verdicts issued
- [x] Step 0: FY2025 10-K (acc. 0001193125-26-083899) and 2026 Q2 10-Q (acc.
      0001193125-26-341032) read — MD&A, cash-flow detail, footnotes; two figures
      cross-checked (reserve development reconciliation; CONVENTION 4 float −0.7%)
- [x] Sector substitution for owner earnings applied and disclosed; windows stated
      (3-yr exact, 5-yr after-tax, 8-yr underwriting); (c) treated per [E5-20] for
      rail/utility and declared inapplicable to the float core per [MF 7]
- [x] Competitor row filled (5 filed rows, 3 industries); unavailable peers (State
      Farm, USAA — mutuals; Munich/Swiss Re — IFRS rung 4) named with the reason, and
      the moat class rests on filed metrics, not on the missing rows
- [x] Sovereign 5.27%, USD, US Treasury daily par curve (issuing authority), 2026-09-01;
      multi-currency exposure stated, treatment disclosed as unresolved per FINDING 8
- [x] Value as a round-number range (~$470/$590/$640); price dated; aggregator used for
      live quote and historical closes only, both flagged
- [x] One bar (Bar 2); windage count ONE, stated
- [x] Share count hand-read off the cover and tool-verified; A/B equivalence taken from
      the charter conversion ratio, priced at 0.08% parity
- [x] Q3 sourced from proxy/10-K/10-Q/8-K only; no letter quoted for any Q3 finding
- [x] Run committed to git after every question (5 commits before this one)

## REGISTER
- **Verdict: OUT at Q5, ON PRICE (about the price, not the business). Q1-Q4 all IN —
  the first name in the eighteen-run history of this queue to clear every business
  gate.** Bar 2 middle outcome + [E4-28] floor, agreeing.
- **One line:** Berkshire at $505 is a $721bn portfolio plus $30-35bn of pre-tax
  operating earnings bought at a fair-to-slightly-cheap price that pays 0.4-0.9 points
  over the bond and roughly 8% expectancy — below the figure the corpus quits on, with
  the strongest balance sheet on the register, a passing retention test, and a
  seven-month-old CEO whose allocation record is too short to grade.
- **PRICE: $505.24 (BRK-B, 2026-09-02). VALUE: ≈ $470-$640/B-share (central ≈ $590).**
- **PASS/FAIL: FAIL — closed at Q5 (price/floor). Q1 IN · Q2 IN · Q3 IN · Q4 IN.**
