# Company Run — Equifax Inc. (EFX) — 2026-09-05
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
- rate **5.24%** · date **2026-09-04** · source **US Treasury daily par yield curve, 30-yr (issuing authority), struck fresh via tools/sources.py**
- FX: not applicable — 77% of revenue is US (FY2025 10-K MD&A); quote and earnings both USD.
  International 23% of revenue earns in ARS/BRL/GBP/AUD/CAD etc.; the USD sovereign is used
  for the whole, stated as a simplification and noted at Q5 (International is 10% of segment
  operating income, so the distortion is small).

**Stage 0 by hand:**
- Price **$177.05** (2026-09-04, aggregator via run.py — live quote only, flagged).
- Shares **117,484,896** — hand-read off the Q2-2026 10-Q cover (accession
  0000033185-26-000028, filed 2026-07-21): "Common stock, $1.25 par value per share —
  117,484,896". Single class. run.py's 124.1M is the diluted weighted average (the known
  EPS-denominator defect); FY2025 10-K balance sheet shows 120.4M outstanding at 2025-12-31,
  falling through 2026 on buybacks — the cover count is the honest, most current figure.
- **Market cap ≈ $20,801M** (117,484,896 × $177.05).
- Screen row (brief): yield 2.38%, growth required 7.62%, spread 37%, "STEP UP — normalize
  down [E4-41]". Fresh run.py at $177.05: 3-yr OE 599–744, yield 2.73–3.38%; 5-yr OE
  532–634. Shape reproduced; the brief's 2.38% was struck at a higher price/stale cap. The
  step-up flag is real either way (OCF 1,116.8 → 1,324.5 → 1,615.7 in three years).

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes (Notes 3, 5, 6, 13 and
  the lease/restructuring disclosures — see Q3/Q4)
- document: **FY2025 Form 10-K, filed 2026-02-19, accession 0000033185-26-000010**; plus
  Q2-2026 Form 10-Q, filed 2026-07-21, accession 0000033185-26-000028
- figure cross-checked: **OCF FY2025 $1,615.7M, SBC $78.4M, capex $481.4M read off the filed
  Consolidated Statements of Cash Flows** — matches run.py's tagged 1,616/78/481. Segment
  revenue/operating income transcribed from filed MD&A tables by hand.
- Capex caption verified: ONE line, "Capital expenditures", and the MD&A attributes its
  decline to "lower capitalized software costs" — **capitalized internal-use software IS
  inside the filed capex line** (gross balance $3,098.2M on the balance sheet). The HAS
  defect does not add a missing line here; the (c) question is instead whether capex still
  understates renewal (see Q4).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **EFX sells answers to yes/no
  questions about strangers — will this person repay, do they earn what they say, are they
  employed. The raw material is contributed to it free: lenders furnish credit histories
  under an industry reciprocity convention shared with two rivals (USIS), and 4M+ employer
  organizations pipe payroll records into The Work Number because contributing outsources
  their verification burden (10-K: "we generally do not charge them to add their employment
  data"). A query costs EFX ~nothing to serve; the fee is per transaction; the party charged
  (a lender underwriting a mortgage) cannot skip the check and passes the cost to the
  borrower. So: free inputs, near-zero marginal cost, a buyer who must buy at the moment of
  decision. Revenue rides credit-decision volumes — above all US mortgage originations —
  which EFX does not control.** Largest client ~3% of revenue (10-K).
- The scarce input this business controls: **the accumulated contributed record base — 209M
  active / 813M total employment records in The Work Number at 2025-12-31, plus one of the
  three US credit files. Neither can be rebuilt quickly by an attacker because the records
  arrive only through years of contributor relationships.**
- Will the fundamentals look broadly the same in ten years? **Credit and hiring decisions
  will still require third-party data, and three bureaus have survived every technology
  cycle since the 1960s. The open question is not whether the function exists but who holds
  the payroll data exclusively — judged at Q2. Broadly yes.**
- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The segments are judged separately [E5-37], because they are different businesses.**
Segment operating-profit mix FY2025: **EWS 63.4% of segment OI ($1,141.5M of $1,799.2M) ·
USIS 26.4% ($475.2M) · International 10.1% ($182.5M)** (FY2025 10-K, Note 13 / MD&A,
hand-transcribed). The brief's "EWS is ~half of profit" understated it: EWS is nearly
two-thirds and rising (58.4% in FY2023).

**(a) EWS / The Work Number — the franchise claim.**
- Needed or desired [x] (a lender underwriting a mortgage or a government agency verifying
  benefits eligibility cannot skip income/employment verification) · no close substitute
  [x at the automated instant tier — see attacker row] · not price-regulated [x today; FHFA
  and CFPB scrutiny live — see below]
- **The physical unit series [E4-55], built from nine 10-K vintages** (verbatim quotes in
  `_research 2026-09-05 EFX/series TWN records.md`): total records **330 → 380 → 380 → 460 →
  535 → 600 → 657 → 734 → 813 million, FY2017→FY2025**; active records 168 → 188 → 209M
  (FY2023-25, the years the split is filed), +12%/+11%/yr; contributor organizations 10,600
  (2017) → "over 4 million" (2025, the jump unexplained in any vintage — payroll-processor
  ingestion changed the denominator, noted as a disclosure defect). **The physical series
  grows through the worst mortgage market since the 1990s — the honest series, not
  dollar-flattered [E4-55].**
- **The trough test the brief demanded [E4-41]: EWS operating income at trough mortgage
  volumes.** Segment series across four vintages: OI **$331.9M (2017) → $703.9M (2020) →
  $1,000.7M (2021, refi crest) → $1,006.0M (2022) → $969.3M (2023, mortgage trough) →
  $1,053.3M (2024) → $1,141.5M (2025)**. Through a ~2/3 collapse in US mortgage
  originations, EWS OI fell 3.7% peak-to-trough and re-grew past the boom peak on
  government/talent/consumer-lending verticals. Margin 41.9-49.2% across the whole cycle.
  **The mortgage boom did not create this segment's economics; it revealed them.**
- **Contributory network effect, the filer's own mechanism:** employers contribute free
  because contribution outsources their verification burden; "we have not experienced
  significant turnover in the employer contributors" (FY2025 10-K). Verifiers must come to
  whoever holds the records. The moat is defended by the same activity that runs the
  business — the [E4-04] test passes: a lapse in spending narrows it, doesn't destroy it,
  and the spending defends the same advantage.
- **Against it, the filer's own words:** "Competition in the Verification Services business
  is **highly competitive with low barriers to entry** and includes employers who manage
  verifications in-house, lenders who obtain verifications directly from employers, and
  numerous online and offline firms" (FY2025 10-K, Competition). The sentence describes the
  manual/offline tier truthfully — anyone can call an employer — but the automated instant
  tier at mortgage/government scale has one database. Recorded, not smoothed over.
- **[E5-28] check:** claiming untapped/held pricing power claims near-monopoly. The filed
  antitrust class action (E.D. Pa., 2024-05-28, purchasers of "electronic verification of
  income and employment services" since 2020) and the CFPB's three CIDs into EWS
  (2023-2024) are the adversarial evidence that others read the position the same way.
  Scrutiny is the shadow cast by the position; it is also the cap on it ([E3-03](3) is
  only conditionally satisfied).

**(b) USIS — the commodity end, on its own filed record.** Margin **42.7% (FY2017) → 21.2%
(FY2023) → 22.9% (FY2025)** — halved in eight years; operating income $539.1M (FY2017) →
$475.2M (FY2025), LOWER in dollars eight years later. FY2025 growth was "primarily due to
product pricing, partially offset by lower mortgage credit inquiry volumes" — price on
falling units, the shrinking-franchise signature [E4-55] — and the margin is squeezed by
"an increase in mortgage related royalty costs" (the FICO score royalty). **Who sets the
price in the chain [E3-03](3): FICO raised the score royalty on all three bureaus; the
bureaus passed it through and added their own increase; FHFA/public controversy attached to
the bureaus. The bureau collects the toll; the scorer sets the toll's biggest component.**
EFX's own FY2026 guidance assumes "100% of mortgage credit scores will be FICO Scores" and
projects "significant margin expansion" if customers convert to the co-owned VantageScore
(Q4-2025 ER, furnished 8-K 2026-02-04 — flagged rung). A franchise does not need to
disintermediate its own input supplier to defend its margin.
- International: 12.9% margin, never above 13.7% in this decade — a collection of
  positions, none dominant. No franchise claim made.

**Must the moat be continuously rebuilt? [E4-04]** The records refresh with every payroll
cycle automatically; the basis (contributor relationships) does not deplete. Not the
excluded class. Success does not depend on a great manager — the dominance-class test
[E2-53] arguably applies to EWS: position, not execution, sets the economics (the segment
prospered straight through the 2017-2019 breach crisis that consumed the parent).

**THE COMPETITOR ROW — required [E3-28].** Same metrics, same window, filing-sourced.
Files: `_research 2026-09-05 EFX/row TRU.md`, `row Experian.md`, `row FICO.md`,
`row attackers.md`.

| Company | Revenue FY2025 | GAAP op margin | RONTA (OI / (assets−GW−intang−cash)) | ROE | source |
|---|---|---|---|---|---|
| **EFX** | $6,074.5M | 18.0% | 31.2% ($1,095.2M / $3,511.6M) | 14.3% | FY2025 10-K, filed statements |
| TRU | $4,576.3M | 18.7% (3.4% FY2023 incl. $414M UK impairment) | 45.1% ($857.8M / $1,901.3M) | 10.5% | FY2025 10-K, accn 0001552033-26-000012 |
| Experian (FY ends March) | $8,445M statutory FY2026 | 24.2% statutory (28.6% "Benchmark" — both stated) | post-tax ROCE 17.2% (company measure; NTOA not derivable from AR summary) | — | AR 2026, experianplc.com — **IR rung, flagged**; audited IFRS statements inside |
| FICO (FY ends Sept) | $1,990.9M FY2025 | 46.5% (Scores segment 87.8%) | ~97% (assets−GW−cash $950.7M) | not meaningful — equity NEGATIVE −$1,745.8M from $7.5bn buybacks | FY2025 10-K, accn 0000814547-25-000030 |
| LexisNexis (RELX division) | not separately filed — named by TRU as competitor; unsegmented | — | — | — | row limit stated [E3-61] |

- Peers named: **4 of the industry's ~4-5 real competitors** (the third bureau Experian
  files in London; FICO is the adjacent score monopolist; LexisNexis unsegmented inside
  RELX — stated). Verification attackers (Argyle, Plaid) are private — rung-3 only, stated.
- TRU's FY2025 10-K names the chain's live threat in its own factor list: "**uncertainty
  related to Fair Isaac Corporation's ('FICO') new Mortgage Direct License Program**" —
  filed evidence that FICO can rewire the mortgage-score channel around the bureaus.
- TRU claims NO income/employment verification business in its 10-K (checked — identity
  verification only). The Work Number's filed competitor set at the automated tier is
  Experian Verify + private fintechs.
- **Untapped pricing power [E3-33]:** the opposite is closer to true at the mortgage line —
  pricing power is being SPENT (double-digit price increases through a volume trough, two
  years filed at USIS, mortgage +20-33% in Q4-2025) while FHFA scrutiny and an antitrust
  class action accumulate. [E4-37]'s inverse metric: no agony whatever in raising prices —
  which argues a wide moat TODAY and simultaneously invites the regulator/attacker response
  that caps it.
- **The attacker's test [E2-45], answered with the attackers' own records:**
  - **Experian Verify: 66 million active records** at FY2026 (AR 2026, IR rung, flagged)
    vs The Work Number's 209M active / 813M total (filed). The best-resourced conceivable
    attacker — the largest bureau, $8.4bn revenue, full data infrastructure — has reached
    ~1/3 of the incumbent's active base. The database CAN be attacked (66M is real and
    growing) and yet the distance after years of trying is the moat's width measured.
  - **FICO's Mortgage Direct License Program** (via Xactus): zero mentions in FICO's own
    10-K/10-Qs/8-Ks; first put on the SEC record by TRU (8-K exhibit 2025-10-23), described
    by FICO only in its proxy (DEF 14A 2026-01-27). It attacks the bureaus' tri-merge
    RESALE layer in mortgage — USIS exposure, not EWS.
  - **FICO's own filed series is the chain's pricing verdict: Scores segment margin
    87.8-91%, B2B scores growth "primarily attributable to a higher unit price" three
    consecutive filed 10-Ks (FY2023-25) through the mortgage trough.** The scorer, with no
    data of its own, out-earns the data owners: the toll sits with the standard, not the
    file. EFX's answer — migrate mortgage to co-owned VantageScore 4.0 (FHFA opened score
    choice July 2025, in FICO's own risk factor verbatim) — would repatriate that margin
    and is simultaneously the event that breaks FICO's grip; both bureaus' releases guide
    around FICO royalty changes. The chain is being re-fought END TO END right now.
- Class: **EWS WIDE on its own series · USIS NARROW-to-NONE (margin halved 42.7%→22.9% in
  eight years, price-on-falling-volume, input squeezed by FICO) · International
  NARROW-to-NONE · blended by profit mix (EWS 63.4% of segment OI): NARROW, with the wide
  asset inside** · Direction: EWS widening on units [E4-32]; USIS narrowing; blend follows
  EWS's rising profit share.
- Row limit stated [E3-61]: the row shows position; whether FHFA/CFPB/the antitrust court
  lets the position keep pricing is conduct-and-regulation, which the row cannot show.
- **VERDICT: [x] IN — class NARROW (EWS alone would be WIDE; the blend is not), direction
  mixed.** The [E3-03] triad holds at EWS: needed, no close substitute at the automated
  tier (attacker at 1/3 scale), and not price-regulated — today. The third criterion is
  the live risk, recorded at Q4 (named death) and Q6, not a present failure.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [ ] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**None ticked → Q3 is an OVERLAY — and this run has the natural experiment to prove the
classification.** The 2017 breach was the worst self-inflicted management failure in the
industry's filed history: 145.5M+ consumers, a CEO gone in 19 days, ~$1.6bn+ of gross
settlements and incident costs, lost certifications, an FY2019 consolidated operating LOSS
of $335.4M from the charge. **Through all of it, EWS operating income never stopped
growing** ($331.9M FY2017 → $391.3M FY2019 → $703.9M FY2020) and consolidated revenue
never declined. The business stood the mismanagement [E5-18] — which is the definition of
the overlay case, demonstrated rather than assumed. Leverage is 2.7x net debt/EBITDA-shape,
not a bank's 20:1; no control position. Case declared: **OVERLAY**.

**Honesty — binary, permanent, filings-based [E5-16].** Each matter dated to when it became
PUBLIC (full record: `_research 2026-09-05 EFX/breach record.md`, verbatim with accessions):
- **2017-09-07** (8-K accn 0000033185-17-000026): breach announced — intrusion mid-May-July
  2017, discovered July 29, announced September 7. **A six-week discovery-to-disclosure gap
  on the company's own filed numbers.**
- **2017-09-26** (8-K): CEO Richard Smith "retires." Forfeited: one year's cash bonus
  ($874,957) plus ~$1.3M of other-NEO bonuses by board negative discretion (2018 proxy).
  Kept: $24.9M SERP (with five GRATUITOUSLY credited service years from 2005) and ~$18.5M
  of 2017 equity-vesting value. **No clawback existed to apply — the policy acquired a
  financial/reputational-harm standard only in March 2018.** The escrowed February-2018
  share tranche's disposition was **never disclosed in any later proxy** — a candor defect
  [E2-26], recorded.
- **2018-03-14 / 2018-06-28**: SEC charges two individuals (a business-unit CIO and a
  manager) with insider trading ahead of the announcement (SEC press releases 2018-40,
  2018-115; title of 2018-40 verified directly at sec.gov). Both were terminated;
  **the SEC and the board's special committee brought no charges against the senior
  officers who traded in early August 2017**. Personal misconduct was found at employee
  level, prosecuted, and not found at officer level.
- **2019-07-22** (8-K accn 0001193125-19-198584): global settlement filed — $380.5M
  consumer fund (+$125M contingent), $180.5M to 48 states+DC+PR, $100M CFPB penalty, $10M
  NYDFS; $802.2M paid through 2024; $13.5M UK FCA penalty (2023). **Consent-order business
  practice commitments remain operative in the FY2025 risk factors** ("extensive and
  require a significant amount of attention from management").
- **2022-08** (public), FCRA class: a three-week coding issue mis-calculated credit scores
  sent to lenders; settlement in principle June 2026 (Q2-2026 10-Q).
- **2023-07 → 2024-08**: three CFPB CIDs into EWS data accuracy and dispute handling —
  live, outcome unpredictable (filer's words).
- **2024-05-28**: antitrust class action, E.D. Pa. — purchasers of EWS verification
  services since 2020. Live.
- **2026-01**: $30.0M accrual, four related class actions re credit-file inquiry disputes.
**The read [E5-22]:** penalty size is not seriousness in either direction. On the breach,
the failure class was competence and institutional neglect, and **they acted when they
learned** — disclosure in ~40 days, CEO out in 19, full settlement, a five-year $1.5bn+
rebuild. The TJX-precedent reading (industry-wide security failure ≠ integrity finding)
applies, and the current CEO (Begor, April 2018) post-dates the failure entirely. **The
brief's harder question — does breach + mortgage-price extraction + antitrust + CFPB read
as one pattern [E4-52]?** The flags do converge on one description: a company that
monetizes a captive position to the edge of what regulators tolerate. That is recorded as
the convergence it is — but [E5-16]'s binary is PERSONAL misconduct, and no disqualifying
personal misconduct by current management is on the filed record. **No integrity OUT.**

**STEP 2 — THE FLAGS [E4-22, E5-15].** *Accounting and disclosure, not litigation. Each
is a prompt to READ, never a verdict.*
- [ ] weak accounting — not found in the filed statements themselves (clean EY opinions;
  no restatement in the vintages swept)
- [ ] unintelligible footnotes — no; footnotes are legible and detailed
- [x] **trumpeted earnings projections / growth targets** — quarterly AND full-year
  guidance with adjusted EPS; Q4-2025 ER leads with "$30 million above the midpoint of
  guidance"; a named "Long Term Financial Framework"; "EFX2028 Strategic Priorities"; a
  "Vitality Index" KPI with a "10% long-term goal." The [E5-30] ratchet in full operation.
- [ ] serial share issuance — no: issued shares flat at 189.3M; but note SBC crept the
  count UP +3.4M over 2017-2024 while buybacks were suspended (holder diluted through the
  freeze), and ~$271M of the BVS price was paid in Equifax do Brasil shares/BDRs (2023).
- [x] **EBITDA / adjusted-earnings promotion [E4-29]** — adjusted EBITDA margin reported
  BY SEGMENT in every earnings release; the proxy's 402(v) "most important financial
  performance measure" is **Adjusted EBITDA**; FY2026 guidance given in Adjusted EBITDA.
  **GAAP EPS $5.32 vs adjusted EPS $7.65 — a 44% gap**, exclusions including acquisition
  amortization ($250.2M), "realignment of resources" (the restructuring line, excluded in
  each of FY2023/24/25: $37.6M/$48.0M/$49.9M — a three-year filed streak, all in SG&A,
  all excluded from adjusted EPS; pre-2023 vintages not swept, stated), legal accruals,
  pension mark-to-market, and more.
- [ ] filed-figure tells [E4-30]: growth NOT unnaturally smooth (3/8/7%; FY2019 loss
  filed as a loss). Cash-tax share of pretax fell 33% → 22.4% in FY2025 — traced to the
  OBBBA deferred-tax swing (+$30.2M deferred vs −$66.9M), an economy-wide 2025 artifact,
  not the [E4-30] tell; it is instead an OCF quality item for Q4 [E4-41].
- [x] **[E2-49]-adjacent disclosure conduct, three instances, dated:** (1) the Canadian
  breach class actions present in FY2024 Item 3 **disappeared silently** from FY2025
  Item 3 — the disappearance is the disclosure; (2) the TWN contributor-organization
  count jumped "tens of thousands" → "over one million" (FY2019→FY2020 vintages) with
  the denominator change never explained; (3) Smith's escrowed-share disposition never
  disclosed in any later proxy. None follows a deteriorating metric (the [E2-49] core
  case), but all three run the same direction: quiet on the unflattering detail.
- [x] **The loudest disclosure choice: the FY2025 10-K — filed 2026-02-19, seven months
  after FHFA opened mortgage-score choice and four months after FICO's direct-license
  launch — contains ZERO mentions of FHFA, VantageScore, score choice, or the FICO
  program** (full-text checked), while FICO devotes a risk factor to it and TRU names it
  in its factor list, and while EFX's own earnings release builds 2026 guidance on a
  "100% FICO" assumption and promises "significant margin expansion" from VantageScore
  conversion. The half-owner test [E2-26] fails on exactly this line: what I would most
  want to know — the economics of the mortgage-score chain being re-fought — is in the
  press release's happy case and absent from the filed risk disclosure.

**STEP 3 — THE PRIMARY TEST [E2-01].** Multi-year, balance sheet before income statement:
- ROE (NI attributable / year-end equity): FY2023 ~11.6% · FY2024 12.6% · FY2025 14.3%.
- **[E2-43] scoping, required for this acquisitive filer:** goodwill $6,745.7M +
  intangibles $1,426.1M against equity of $4,604.3M — **net tangible equity is NEGATIVE
  (≈ −$3.6bn)**, so ROE measures the acquisition history, not the operations. On
  unleveraged net tangible operating assets: consolidated OI $1,095.2M / (assets − GW −
  intangibles − cash = $3,511.6M) = **31.2% pre-tax RONTA**; the goodwill wedge ($8.2bn,
  built by ~$6.1bn of acquisitions 2016-2025: Veda $1.79bn, Appriss $1.825bn, Kount
  $640M, BVS $869.6M consideration...) is reported separately, as [E2-43] requires. The
  operations are franchise-grade; the capital that bought them was not cheap.
- **The filed 402(v) series is the shareholder's answer: $100 (2020-12-31) → $116.66
  (2025-12-31) vs peer group $169.26** — five years, +3.1%/yr with dividends, trailing
  the company's own chosen peer index by 52.6 points. The [E3-54] retention test fails
  on this filed series: ~$2.25bn retained over the five years (NI ~$3.25bn less
  dividends ~$1.0bn) against a market value that DECLINED (cap ~$23.5bn end-2020 at the
  402(v) base → $20.8bn today, aggregator price flagged).

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] resists change — no; if anything the opposite (cloud rebuild executed)
- [x] **projects/acquisitions materialise to soak up available funds** — the 10-K says it
  in its own voice: "A critical lever of our strategy is inorganic growth through
  accretive and strategic acquisitions..." ~$6.1bn spent 2016-2025 across ~25+ deals;
  the moment FCF ran free of the cloud build (2025), a $3bn buyback authorization
  materialized the same board meeting as the dividend raise.
- [ ] staff studies for the leader's craving — not observable from filings
- [x] peer behaviour imitated — all three bureaus run the same play (TRU: Neustar/Sontiq;
  Experian FY2026: $792M of acquisitions; EFX: the list above), and all three co-own and
  now push VantageScore.

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds? Marginal: FY2025 buybacks $927.5M + dividends $232.8M = $1,160.3M
  against FCF $1,134.3M, with net short-term (CP) borrowings +$474.7M in the same year —
  the return program leaned on the CP window in its first year back.
- (2) material discount to conservative IV? **FAILS. FY2025 average repurchase price
  $231.48 (4,006,173 shares for $927.4M); H1-2026 ~$182 average ($565.0M); the
  zero-growth value band computed at Q5 is ~$80-145/share, judged ~$115.** The company
  bought back stock at roughly twice the judged zero-growth value, at prices up to 31%
  above even today's $177.05 quote — and the FY2025 tranche is already 24% underwater.
  **CAPITAL ALLOCATION FLAG, stated with [E4-13]'s humility** (management knows the
  business better than I do; many CEOs never stop believing their stock is cheap
  [E5-08]). **Binds position size, never the discount rate.**
- [E2-52] dividends-by-issuance: does not fire (dividend $232.8M, small against OCF).
- Buyback third condition [E4-31] (informed register): the FY2025 10-K's silence on the
  FHFA/FICO chain re-fight (above) means the register was buying alongside a filer whose
  risk section lagged its own press release — noted against condition three.

**THE GUARDRAIL — check before writing the verdict.**
- [x] Confirmed: nothing in this Q3 promotes the name. Q2's class and Q4's numbers stand
      on their own **[E2-37, E2-38, E3-39]**.
- [x] The business does NOT require a great manager — the breach experiment proved the
      position carries mediocre-to-failed management [E2-53, E5-18]; recorded at Q2.
- [x] No manager-as-plan reasoning anywhere in this file **[E2-35, E2-36]**.

- **VERDICT: [x] IN — as OVERLAY, no integrity disqualifier found.** *NOT a finding that
  the managers are honest [E5-17]. IN never promotes.* Live flags carried to Q5/Q6:
  guidance ratchet [E5-30]; adjusted-measures promotion [E4-29]; the FY2025 10-K's
  FHFA/FICO silence [E2-26]; three quiet-disclosure instances [E2-49]-adjacent;
  buyback condition-2 flag (binds position size); acquisition soak-up [E2-30](2); the
  [E4-52] convergence reading (breach + captive-chain pricing + antitrust + CFPB) as one
  reinforcing description of conduct toward the customer chain — none of it personal
  misconduct, all of it monitoring load.

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
Full decade transcribed by caption from four 10-K vintages
(`_research 2026-09-05 EFX/series cashflow.md`). OE = OCF − SBC − capex (cash-flow line;
the caption VERIFIED to contain capitalized internal-use software in every vintage
2016-2025 — the brief's live (c) question answers itself: the software spend is already
inside the charged line, $3,098.2M gross on the balance sheet; the accrual-basis series
differs by <$25M/yr, both bases recorded):
- **Owner earnings by year ($M): 2016 612.4 · 2017 559.5 · 2018 307.8 · 2019 −135.5 ·
  2020 470.2 · 2021 810.9 · 2022 70.0 · 2023 443.7 · 2024 731.4 · 2025 1,055.9**
- **Short-window mean** (3-yr, FY2023-25): **$743.7M**
- **Mid-window** (5-yr, FY2021-25): **$622.4M**
- **Long-window mean** (10-yr, FY2016-25): **$492.6M**
- Leave-two-out (drop best 1,055.9 and worst −135.5): **$500.7M**
- **Spread, conservative end: 33.8%** (10-yr vs 3-yr) — the screen's 37% row reproduced in
  shape by hand.
- **Distorted years, named [E5-11, E4-41]:** DOWNWARD — 2019 (breach settlements; $341.5M
  paid, OCF $313.8M) and 2022 (final $345.0M Consumer Restitution deposit January 2022 +
  the $624.5M capex peak; OE $70.0M). UPWARD — 2025 (OBBBA cash-tax timing: current tax
  fell to 22.4% of pretax from ~33%, deferred swung +$97M; incentive-accrual build inside
  OCF; and the mortgage-PRICE wave — USIS mortgage +20-33% in Q4-2025 on "product
  pricing" while volumes fell, riding FHFA tolerance that is publicly fraying). **The
  window carries both signs; the [E4-41] normalization nets them rather than cherry-
  picking either.**
- **Maintenance capex — the disclosed judgment.** This is neither the [E5-20] railroad
  case nor a clean [E3-44] default case; it is the convergence case: **D&A ex-deal-
  amortization ($726.9M − $250.2M purchased-intangible amortization = $476.7M) ≈ the
  capex line ($481.4M)** — the two honest bases agree at ~$480-500M/yr. Purchased-
  intangible amortization is an acquisition artifact, not renewal spend, and is excluded
  from (c) with that reason stated. **(c) judged at $500M/yr** — slightly above the
  current declining line, because a data company's capitalized software development IS
  its product renewal (the QCOM/ACLS R&D shape, capitalized here), and the filer's
  "post-Cloud" capex decline is taken as guidance, not fact.
- Stock compensation subtracted in full [E5-06]: $78.4M FY2025 (reported charge = the
  floor of the subtraction [E3-70]; series 37.1 → 81.6 doubled over the decade).
- **JUDGED OE: $700M** — construction: 2024-25 capex-end average $893.7M, minus ~$95M
  OBBBA tax-timing, minus ~$90M judged non-durable mortgage-price capture (about half of
  the 2024-25 USIS mortgage price gains, the half exposed to FHFA/antitrust reversal);
  cross-anchored between the 5-yr mean ($622M, which carries the 2022 restitution year
  at full weight) and the 3-yr mean ($744M). **Range carried: $500-900M** (leave-two-out
  floor to the un-normalized recent average). The single best year ever ($1,055.9M) is
  displayed and refused as a mean.
- The range is wide but not conclusion-destroying [E4-25]: every point in it prices the
  same verdict at Q5 (see below), so the file can close honestly on the range itself.

### Great, good, or gruesome? **[E4-20]**
- [x] **good** — consolidated: 31.2% pre-tax RONTA, but growth has been bought (~$6.1bn
  of acquisitions 2016-2025) and OE grew only ~1.5%/yr across the decade (612 → judged
  700) against revenue +7.6%/yr. The added capital earned; it earned modestly.
- Inside it, **EWS alone is great** — 44.2% margin, segment capex 3.7% of revenue,
  $1.14bn OI on a contributed-free database ([E2-44](2) passes loudly).
- Not gruesome: nothing here eats capital at poor returns.

### Staying power — score all three **[E5-11]**
- (1) large and reliable earnings stream: **PASS** — revenue rose every year of the filed
  decade including the breach years; OCF positive in all ten years including 2019.
- (2) massive liquid assets: **FAIL** — $170.1M cash (June 30, 2026) against $5,485.3M
  total debt; liquidity is a $2.0bn Revolver (upsized from $1.5bn in 2026) with only
  $0.6bn available because ~$1.4bn of CP is outstanding against it. **[E5-39]: the CP
  program is dependence on the kindness of strangers as a standing funding tool — it
  grew $762M → ~$1.4bn in six months while $565M went to buybacks.**
- (3) no significant near-term cash requirements: **MARGINAL** — the June-2026 notes
  ($275M) are already repaid (with CP); next walls $750.3M (Dec 2027) and $825.3M
  (2028, incl. the 6.9% debentures) against ~$1.1bn/yr FCF; the covenant is
  EBITDA-based (3.75x max; ~2.9x at Jun-2026 on the FY2025 EBITDA shape) [E2-54 note:
  an EBITDA covenant is exactly the construction the corpus distrusts].
- Coverage [E2-54]: FY2025 (OCF − capex) / cash interest = (1,615.7−481.4)/209.7 =
  **5.4x**; but the worst filed year, 2022, was **0.6x** on the same construction —
  named: the final restitution deposit plus peak transformation capex. The structure
  survived its own worst year with CP and term issuance, which is the fact both ways.
- Leverage, named and quantified [E4-16, E3-29]: $5,485.3M total debt, ~$5.3bn net;
  ~2.9x net debt / (OI + D&A); 85% fixed-rate at FY-end. Investment-grade dependent —
  a downgrade "could preclude our ability to issue CP" (filer's words).

### Name the specific way THIS business dies **[E2-27, E3-24]**
1. **The chain-pricing reversal (valuation death, not solvency).** Mechanism: FHFA score
   choice + FICO-direct-via-Xactus + the CFPB/antitrust matters + VantageScore's own
   lower price compress the mortgage-chain pricing that produced most of 2024-25's
   growth ("product pricing" is the filed driver both years). Quantified: reversing the
   two-year USIS mortgage price capture (~$250-300M revenue at high incremental margin)
   plus EWS mortgage price exposure ≈ OE falls toward **$450-500M → zero-growth value
   ~$73-82/share at the sovereign**. Likelihood: **a real possibility** — it is the
   scenario the filer's own 2026 guidance hedges with the VantageScore migration plan.
2. **The database opened (the slow death).** Mechanism: consumer-permissioned
   verification architecture (the model EFX's own 10-K describes without naming:
   "third parties may also seek to obtain verifications directly from employees...by
   seeking employee credentials") plus Experian Verify's 66M records plus any
   access-remedy outcome from the antitrust/CFPB matters. Quantified: EWS margin
   migrating to USIS's 22.9% would cut segment OI $1,141.5M → ~$590M; OE toward
   $150-250M — the [E2-27] shape. Likelihood: **a low-level possibility** on the filed
   evidence (the best attacker is at 1/3 scale after years, and the architecture trades
   certainty for cost), rising if a court or the CFPB forces access.
3. **Solvency.** Mechanism: a second breach-class event (or consent-order enforcement)
   simultaneous with a CP freeze and the 2027-28 walls. Quantified from the filed
   precedent [E3-24-style]: the 2017 event cost ~$1.6bn gross over three years and the
   company carried it with positive OCF every year and MORE relative leverage than
   today; a repeat would force the revolver, cut the buyback, and survive. Likelihood:
   **a low-level possibility** — modeled on exposure, not benign recent experience
   [E4-40]: the exposure (5,000+ data sources, 15,000 employees, state actors) is
   permanent.
- **VERDICT: [x] IN** — with [E5-11] scored pass/FAIL/marginal and the CP dependence
  named as the structure's soft spot.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Honest
pre-tax expectancy at this price: **~5.5-7.5%** (yield 2.4-3.6% plus durable growth
honestly creditable at +2 to +4%/yr — the filed decade produced +1.5%/yr OE growth; the
+10% guidance is revenue, price-wave-assisted, and guidance [E3-48]). **Below roughly 10%:
the name is QUIT ON, not ranked.** Growth needed to clear the floor from the judged yield:
**+6.6%/yr perpetual** (range +6.4 to +7.6 — the screen's 7.62% reproduced), against
+1.5%/yr realised — a [E4-35] base-rate burden this file cannot carry in writing.
**No risk premium in the discount rate [E3-42].**

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no
vote **[E3-34]**.

**1. THE YIELD**
- owner earnings **$700M judged ($500-900M carried; windows 492.6 / 622.4 / 743.7)** ÷
  market cap **$20,801M** (117,484,896 sh × $177.05) = **3.37% judged; 2.37-3.58% across
  windows** · sovereign **5.24%** (US Treasury 30-yr, 2026-09-04)
- **The loudest single fact in the file: the best owner-earnings year in the filed decade
  — FY2025's $1,055.9M, itself carrying OBBBA tax timing and a mortgage-price wave —
  yields 5.08% at this price. Below the bond. Every construction, including the one
  [E4-41] forbids, pays less than the 30-year Treasury.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- growth needed to justify the quote at the bare bond: **+1.9%/yr perpetual** on judged OE
  (+1.7 to +2.9 across the range)
- what the business has actually done: **OE +~1.5%/yr over the filed decade** (612.4 →
  judged 700); revenue +7.6%/yr, but ~$6.1bn of acquisitions bought that line
- so the quote is roughly fair against the bond ONLY if the recent level is durable and
  grows ~2%/yr forever; it is nowhere near the ~10% floor

**3. WHAT YOU ARE PAID**
- return at the current price = **−1.9 points UNDER the sovereign** (judged; −2.9 to −1.7
  across windows; even the best-year-ever construction is −0.2)

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.24%** — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero-growth perpetuity of OE at the bare
sovereign (5.24%), per share on 117,484,896:
- conservative **~$80** ($500M) · judged **~$115** ($700M) · optimistic **~$145** ($900M)
  · best-year-ever, displayed and refused as a mean: ~$170 ($1,055.9M)
- at the ~10% floor: **~$43-77, judged ~$60**
- **current price $177.05** (2026-09-04, aggregator, flagged) — **above the ENTIRE
  zero-growth band, including the refused best-year construction**

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **~5.5-7.5%** vs ~10% **[E4-28]** —
  **below → QUIT ON, and the ranking lines are not filled in.**
- *(For the record, not the ranking: at −1.9 points under the sovereign this name would
  rank below every completed name in the queue's history; BMI judged 2.06-4.18%, SBUX
  2.18%, EFX 3.37% judged — all quit on.)*

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [x] **Screamer test [E4-01]** — price $177.05 vs the conservative case ~$80 and the
      whole range $80-145: **above the whole range → outcome three → no.** No margin
      added on top.
- **Windage count: ONE** — conservatism was spent once, in the judged-OE normalization
  ($893.7M recent average → $700M, reasons named); the value band then uses realistic
  perpetuity arithmetic at the bare rate with no second margin **[E4-11, E4-48]**.

- **VERDICT: [x] Q5 FAIL — ON PRICE, at the [E4-28] floor. Not ranked; quit on.**

**Pre-committed re-look (Q6 not opened; the file closes at Q5):**
- Re-price at the rate of the day against **~$115/share judged zero-growth** (struck at a
  5.24% sovereign); the file reopens for a full re-read, not a re-price, if price enters
  the $80-115 band.
- Reopen triggers (any one): (a) the FY2026 10-K's first FHFA/VantageScore/score-choice
  risk-factor language — and whether the promised "significant margin expansion" from
  VantageScore conversion prints in USIS margin; (b) TWN active-record growth below
  +5%/yr, or withdrawal of the record-count disclosure [E2-49, E4-55]; (c) class
  certification or CFPB action in the EWS matters (the access-remedy scenario is named
  death #2); (d) buybacks continuing above the judged band while CP grows [E5-08(2),
  E2-60]; (e) a filed mortgage-revenue decomposition showing the price wave reversing.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened — no position exists or is licensed; the file closed at Q5 on price.** The
pre-committed re-look triggers above stand in for Q6's yardsticks-prior-to-the-act
[E1-02]. Were the price question ever to reopen: the thesis-confirming metric is the TWN
active-record series (+11%/yr filed); the thesis-breaking metric is an EWS Verification
margin below ~35% or an access remedy in the antitrust/CFPB matters; and the
capital-allocation flag (condition-2 buybacks) would bind position size from day one.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q6 not opened, stated with reason)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Experian
  row is IR-rung and flagged as such; it is corroborative, not load-bearing for any IN)
- [x] No UNRESEARCHED verdicts issued
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: FY2025 10-K read (MD&A, cash-flow detail lines, footnotes), accession
  0000033185-26-000010; OCF/SBC/capex cross-checked against the filed statements
- [x] Owner earnings on multi-year means; 3/5/10-yr + leave-two-out windows all displayed;
  (c) disclosed as a judgment ($500M) with the convergence reasoning stated
- [x] Competitor row filled: TRU + FICO filed; Experian at its honest rung, flagged;
  LexisNexis named as unsegmented (row limit stated [E3-61])
- [x] Sovereign 5.24%, USD (the earnings currency for 77% of revenue; simplification for
  International stated), US Treasury (issuing authority), 2026-09-04
- [x] Value as a round-number range ($80 / $115 / $145 zero-growth; $43-77 floor)
- [x] One bar (Screamer); windage count ONE, stated
- [x] Prices dated; aggregator for live quote only, flagged
- [x] Run committed to git after every question (write-early protocol; survived one
  session kill with zero question loss)

**Defects confessed:**
- The brief's screen row (2.38% / 7.62% / 37%) was struck at a stale cap; reproduced in
  shape (2.37% = the 10-yr window yield at today's cap; 37% ≈ 33.8% spread by hand;
  7.62% ≈ my 6.6-7.6% floor-growth range). Not exact to the million, unlike prior runs —
  the price moved between strike and run.
- run.py's share basis (124.1M weighted average vs 117.48M cover) and its 3-yr-only
  default window both corrected by hand; its OE lo/hi labels invert for EFX because D&A
  exceeds capex here (noted for the tool file).
- Mortgage % of revenue is stated nowhere in any 10-K vintage (checked FY2017-25);
  quantified mortgage exposure rests on segment-level filed statements plus the furnished
  ER's growth rates — the exact mortgage revenue share is a stated gap, not a number in
  this file.
- Insider-trading citations: SEC press release 2018-40 title verified directly;
  2018-115 (Bonthu) cited by release number from the agent's sweep without a direct
  fetch of the page in this session.
- Experian FY2026 AR figures are IR-rung (audited statements inside, but not a filed
  document); all Argyle/Plaid material is rung-3 and so labeled; the Argyle survey is
  treated as marketing.
- 2019/2022 breach-year OCF distortions are inside every window mean; the judged $700M
  nets them against 2025's tailwinds — a judgment, disclosed as one.
- EWS-level owner earnings cannot be isolated (capex by segment is filed but corporate
  capex/SBC/tax are not allocated); the segment franchise case rests on segment OI and
  capex, stated.

## REGISTER
- Verdict: **Q5 FAIL — ON PRICE, at the [E4-28] floor. About the price, not the business:
  Q1 IN · Q2 IN (NARROW; EWS WIDE inside) · Q3 IN (overlay, no disqualifier) · Q4 IN.**
- One line: **A genuinely wide contributory-database franchise (records 330M→813M filed,
  attacker at 1/3 scale, trough-proof segment economics) wrapped in a narrowing bureau, a
  guidance-and-adjusted-EBITDA culture, a CP-funded buyback at twice judged value — and
  priced so that even its best year ever yields less than the 30-year Treasury.**

---
# OUTPUT CONTRACT (queue rules 1 and 2)
**PRICE: $177.05 (2026-09-04, aggregator, flagged). Zero-growth value at the 5.24%
sovereign: ~$80-145/share, judged ~$115. At the ~10% floor: ~$43-77, judged ~$60.**
**PASS/FAIL: FAIL — at Q5, on price, at the [E4-28] floor. All four business gates (Q1-Q4)
returned IN; honest pre-tax expectancy ~5.5-7.5% vs the ~10% quit-on floor; price sits
above the entire zero-growth value band on every owner-earnings construction in the filed
decade.**
