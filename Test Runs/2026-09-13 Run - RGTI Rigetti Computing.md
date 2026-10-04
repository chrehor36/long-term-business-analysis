# Company Run — Rigetti Computing, Inc. (RGTI) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Write-early protocol: this file was created before any fetch. Sections are appended as they
close. Research files: `Test Runs/_research 2026-09-13 RGTI/`.*

**PRIORS, recorded before any filing was opened [E4-26]** — to be refuted, not confirmed:
1. The operator expects an early close (Q1, Q2, or Q4 on [E5-11]). A prior, not an instruction.
2. The queue guard (share count 1.74x in two years) is ATM equity issuance, not a perimeter change.
3. The de-SPAC CIK (Supernova Partners Acquisition Co II until 2022-03-01) may hold the shell's
   pre-2022 history rather than Rigetti's. Unverified until companyfacts is read.
4. The two 8-K Item 1.01 filings since 2026-03-04 are financing, not mergers. Unverified.
5. My own prior: revenue is small and dominated by government research contracts; operating
   cash is funded by equity. Unverified.

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
protocol violation — it is UNRESEARCHED.** **No degree-of-difficulty credit [E4-18].**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.35%** · date **2026-09-11** (latest print; 09-12 and 09-13 are a weekend) · source
  **US Treasury daily par yield curve, 30-year** (issuing authority), struck fresh through
  `tools/sources.py:sovereign("USD")` on 2026-09-13. The strike agrees with the brief's figure;
  it was not inherited from it.
- Earnings currency **USD**: Delaware registrant, Berkeley CA; revenue by geography H1 2026
  US $4,911K / Europe $767K / Asia and other $3,860K (10-Q Note 11). The non-US legs (UK
  grants, C-DAC India) are small and do not change the currency the owner is paid in. No FX,
  no ADR.

**Price and share count — re-struck, not inherited:**
- Price **$15.27**, 2026-09-11 close (`sources.price("RGTI")`, Yahoo chart API — **aggregator,
  flagged, live quote only**). No split after the measurement date (`split_factor_after` = 1.0).
- **Cover count confirmed: 333,768,747 shares at 2026-08-03**, single class, 10-Q for the period
  ended 2026-06-30, filed 2026-08-06, accession `0001104659-26-091993` (the brief's pre-check
  holds; balance sheet 333,676,881 at 2026-06-30).
- **PLUS 7,739,938 shares issued to the U.S. Department of Commerce on 2026-09-08** under a
  Securities Issuance Agreement (8-K filed 2026-09-08, accession `0001104659-26-105662`, Items
  1.01/3.02, implied price $12.92). This post-dates the cover and the queue's pre-check.
- **Count used: 341,508,685.** Cap = $15.27 x 341,508,685 = **$5,214.8M** (on the cover count
  alone $5,096.6M). No ATM capacity remains (10-Q Note 8: *"there were no remaining shares
  available for sale pursuant to the Sales Agreement"*); no new ATM or shelf takedown appears in
  the submissions list through 2026-09-13.
- **Fully diluted, from the 10-Q reserve table (2026-06-30):** warrants 11,716,146 (of which
  public 8,436,597 and private 283,424 at $11.50, expiring 2027-03-02), RSUs 6,742,835, options
  6,141,388 → **~366.1M** with the DoC shares; plus 1,340,310 unvested customer warrants (10-K
  Note 13). At $15.27 the $11.50 warrants are in the money.

**The filing was read** — not tagged data **[E3-27]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **10-K FY2025**, filed 2026-03-04, accession `0001104659-26-023454` (balance sheet, operations,
  equity, cash flows, Notes 1-2, 8-9, 12-15, 19; Item 1; Item 1A; MD&A incl. liquidity).
- **10-Q Q2 2026**, filed 2026-08-06, `0001104659-26-091993` (statements; Notes 5, 8-11; MD&A).
- 10-Q Q1 2026 `0001104659-26-058641`; 10-K FY2024 `0001558370-25-002499`; 10-K FY2023
  `0001558370-24-003234`; 10-K FY2022 `0001193125-23-080486`; DEF 14A filed 2026-04-24
  `0001104659-26-048555`.
- **De-SPAC close 8-K**, filed 2022-03-07, `0001193125-22-067932`, and its **EX-99.1** (Legacy
  Rigetti audited statements, 11 months to 2021-12-31 and FY ended 2021-01-31).
- 8-K Item 4.02, filed 2022-11-14, `0001193125-22-284732` (non-reliance, Q1-Q2 2022).
- 8-K EX-99.1 earnings releases Q2 2025 through Q2 2026 (five); 8-Ks of 2026-03-20, 2026-04-21,
  2026-05-21, 2026-08-20 (two), 2026-09-08.
- **Figure cross-checked against the filed statement:** FY2025 net cash used in operating
  activities **$(58,543)K** on the 10-K cash-flow statement = companyfacts
  `NetCashProvidedByUsedInOperatingActivities` −58,543,000. FY2025 stock-based compensation
  **$17,605K** on the cash-flow statement = the equity-statement line = the Note 12 expense table
  (R&D $12,776K + SG&A $4,829K) = `ShareBasedCompensation` 17,605,000. FY2025 purchases of
  property and equipment $(18,676)K = `PaymentsToAcquirePropertyPlantAndEquipment`. H1 2026 OCF
  $(31,993)K on the 10-Q = tag.

### THE TWO PROMPTS THAT FIRED, OPENED

**`name_change_note` (Supernova Partners Acquisition Co II until 2022-03-01) — WHAT
COMPANYFACTS UNDER THIS CIK HOLDS: BOTH ENTITIES, UNDER COLLIDING PERIOD KEYS.** Read row by
row, accession on every row:
- **The SPAC shell's own figures are present** — the 10-K for FY2021 filed 2022-02-23 by
  Supernova, accession `0001564590-22-006345`: period 2020-12-22 to 2020-12-31 (net loss
  −$14,691) and **period 2021-01-01 to 2021-12-31: net loss −$23,170,100, operating loss
  −$4,904,921, operating cash −$961,975, equity −$46,476,680.** The shell's three 2021 10-Qs
  carry operating cash of −$476,570 / −$565,125 / −$653,973.
- **Rigetti's own 2021 figures are ALSO present**, as comparatives in the FY2022 10-K and the
  2022 10-Qs. Legacy Rigetti moved its year-end from January 31 to December 31, so its "fiscal
  year 2021" is **eleven months, tagged 2021-02-01 to 2021-12-31** (net loss −$38,241K, OCF
  −$29,044K) — the 10-K FY2022: *"For fiscal year 2021, this covers a period of 11 months
  starting from February 1, 2021 and ending on December 31, 2021."* Its 2021 quarterly
  comparatives sit under **the same 2021-01-01 keys as the shell's** (Q1 2021 OCF: shell
  −$476,570; Rigetti −$5,795,000).
- **Rigetti's pre-2021 operating history is NOT in companyfacts.** The FY ended 2021-01-31 lives
  only in the de-SPAC 8-K's EX-99.1: revenue $5,542,598; net loss −$26,127,496; OCF
  −$30,067,263; SBC $2,592,038; capex $4,400,432; D&A $4,299,263. The only pre-2021 Rigetti fact
  under the CIK is one balance: equity −$35,425K at 2021-01-31.
- **The trap this sets, stated so a tool can be fixed:** an annual reader that filters durations
  to 340-380 days (`sources.annual`, default `lo=340`) **drops Rigetti's 334-day FY2021 and keeps
  the shell's 365-day FY2021 — operating cash −$0.96M against Rigetti's −$29.0M, a 30x
  understatement of the burn** in any window reaching 2021. Same class as NEGG's splice, a
  different mechanism: not a different operating company, but a shell plus an eleven-month
  transition year. **This run uses no companyfacts row from accession `0001564590-22-006345`, and
  takes FY2021 and FY-Jan-2021 from the filed statements only.**
- A second, smaller tagging defect: the weighted-average basic share count in the 2023 10-Qs is
  tagged in thousands without scale (e.g. 53,692 for 53,691,948 in Q1 2022, as re-tagged in the
  Q1 2023 10-Q). Any per-share screen reading those rows is off by 1,000x.

**`deal_note` (two 8-K Item 1.01 filings since 2026-03-04, no EX-2.1) — BOTH OPENED. Neither
is an at-the-market programme, neither is a revolver, and neither is a merger:**
1. **8-K filed 2026-04-21** (`0001104659-26-045994`): a **sublease** of 12,543 rentable square
   feet of office and laboratory space at 740 Heinz Avenue, Berkeley, from Chinook Therapeutics,
   to 2029-11-30, base rent $38,111.91 a month rising to $41,645.91. Immaterial.
2. **8-K filed 2026-09-08** (`0001104659-26-105662`, Items 1.01, 3.02, 7.01): **a CHIPS Act
   "Other Transaction Agreement" with the U.S. Department of Commerce for up to $100M of R&D
   funding, paired with a Securities Issuance Agreement issuing 7,739,938 shares to the
   Department at an implied $12.92.** Tranches: $43.9M on or after the award date; $29.9M and
   $26.2M *"if the Department determines to its satisfaction in its sole discretion"* that
   milestones are met; five-year period of performance; the Department *"may demand recovery of
   the aggregate amount of payments made to Rigetti Sub … as a debt payable to the Department"*
   for failure to complete required project activity or material non-compliance; termination for
   convenience on sixty days' notice; *"march-in rights and restrictions on transfer of
   intellectual property developed using funds from the Award"*; US-ownership and domestic
   production requirements; if the Department terminates, the company may repurchase the shares
   equivalent to the undisbursed award for $1.00 in aggregate. **The terms moved between LOI and
   definitive agreement**: the 10-Q (filed 2026-08-06) described $19.9M + $22.2M + $18.5M + a
   discretionary $39.4M; the LOI 8-K (2026-05-21) said *"over a three-year period"*; the
   definitive OTA is $43.9M + $29.9M + $26.2M over five years. The LOI priced the shares at the
   lowest of three closing prices *"discounted by fifteen percent (15%)"*.
- **Also found, flagged by neither prompt:** 8-K Item 4.02, 2022-11-14 — non-reliance on the Q1
  and Q2 2022 10-Qs (the earn-out liability's volatility assumption). Carried to Q3.

### THE SHARE COUNT OVER THE FULL FILED HISTORY — AND WHAT A 2022 HOLDER STILL OWNS

| date | shares | source | driver |
|---|---|---|---|
| 2021-01-31 | 16.6M common + 57.4M preferred as converted (Legacy, ratio 0.78699) | 10-K FY2022 equity statement | private company |
| **2022-03-02 close** | **113,810,285** | de-SPAC 8-K `0001193125-22-067932` | SPAC + PIPE 34,850,706 |
| 2022-12-31 | 125,257,233 | 10-K FY2022 | RSUs 7.0M, warrants 4.8M, options 2.8M |
| 2023-12-31 | 147,066,336 | 10-K FY2023 | B. Riley equity line 13.4M ($20.5M), options 4.0M, RSUs 3.9M |
| 2024-12-31 | 283,546,871 | 10-K FY2024/FY2025 | **ATM 68.8M ($97.5M), registered direct 50.0M ($96.0M)**, B. Riley 10.1M ($12.8M), RSUs 6.4M |
| 2025-12-31 | 331,282,895 | 10-K FY2025 | **ATM 30.3M ($346.7M, weighted $11.55)**, RSUs 7.2M, warrants 4.8M ($50.0M cash), Quanta 3.0M ($35.0M), options 2.4M |
| 2026-06-30 | 333,676,881 | 10-Q Q2 2026 | RSUs, options |
| 2026-08-03 | 333,768,747 | 10-Q cover | |
| **2026-09-08** | **341,508,685** | + 8-K `0001104659-26-105662` | **DoC 7,739,938** |
| fully diluted | ~366.1M | 10-Q reserve table | warrants, RSUs, options |

- **3.00x the shares at the close in four and a half years; 2.32x since 2023-12-31; 1.79x since
  2024-08-05 (191,243,492, the queue guard's base).** **A holder of one share at the March 2022
  close now owns 33.3% of the slice of the company that share represented** (113.81 ÷ 341.51),
  **31.1% fully diluted.**
- **The queue guard's reading is CONFIRMED and was incomplete in one respect.** The perimeter did
  not change: one operating company throughout, no acquisition, no disposal. The count grew by
  selling stock through six different channels — an equity line, two ATMs, a registered direct,
  warrant exercise, a strategic placement — and now a seventh: **shares issued to a government
  counterparty as the condition of a grant.** Cash raised from equity since the close ~$659M
  (B. Riley $33.4M, ATMs $444.2M, registered direct $96.0M, Quanta $35.0M, warrants ~$50.1M) on
  top of $225.6M at the close, **against cumulative operating cash of −$283.5M and capex of
  $85.0M over FY2021(11m) to H1 2026.**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

> *"we try to stick to businesses we believe we understand. That means they must be relatively
> simple and stable in character. If a business is complex or subject to constant change, we're
> not smart enough to predict future cash flows."* **[E3-31]**

**Unit economics in my own words, no management language — the filed entity first, because it
IS writable.**

Rigetti designs superconducting quantum chips, makes them in its own small fab in Fremont, puts
them in dilution refrigerators with control electronics, and gets paid in three ways (10-K Note
14; 10-Q Note 10):

| $K | FYJan-2021 | FY2021 (11m) | FY2022 | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 | TTM 2026-06 |
|---|---|---|---|---|---|---|---|---|---|
| Revenue | 5,543 | 8,196 | 13,102 | 12,008 | 10,790 | 7,088 | 3,273 | 9,538 | 13,353 |
| — collaborative research & professional services | | | | | 8,044 | 6,676 | 3,043 | 2,251 | 5,884 |
| — quantum computers & components (point in time) | | | | | 2,390 | **0** | 0 | 7,144 | 7,144 |
| — access to quantum computing systems (cloud) | | | | | 356 | 412 | 230 | 143 | 325 |
| Government share of revenue | | 80.0% | 81.3% | | 89.4% | 90.2% | 90.7% | **22.2%** | |
| Cost of revenue + operating expenses | | 42,325 | 122,182 | 84,303 | 79,300 | 91,748 | 44,787 | 63,551 | 110,512 |
| Remaining performance obligations (year-end) | | | 9,700 | 3,000 | 2,200 | 3,800 | | 2,700 (06-30) | |

Sources: 10-K FY2022, FY2024, FY2025 statements and revenue notes; 10-Q Q2 2026; FYJan-2021 from
the de-SPAC 8-K EX-99.1; government share from Item 1A/Note 15 of each filing.

1. **Research contracts** with governments — DARPA, AFRL, DOE's SQMS centre, Innovate UK — billed
   on time-and-materials, cost-share or milestone terms. *"Currently, we generate the majority of
   our revenues from technology development contracts with various partners"* (10-K FY2025 Item
   1). This line has shrunk: $8.0M (FY2024) → $6.7M (FY2025) → $2.3M (H1 2026), and the MD&A says
   why: *"Our revenue has been negatively impacted by expiration of the National Quantum Initiative
   Act in September 2023 and its pending reauthorization in the United States Congress."*
2. **Selling small on-premises quantum computers** to universities, national labs and research
   centres — the 9-qubit Novera ($1.6M of sales in FY2024, **none in FY2025**, most of the $7.1M
   in H1 2026) and one 108-qubit system on an **~$8.4M purchase order from India's C-DAC**, due for
   deployment in H2 2026. The buyers are researchers buying an instrument to do research on.
3. **Renting time on its machines over the cloud** — directly and through Amazon Braket and
   Microsoft Azure Quantum, which the 10-K says *"operate a service in direct competition with our
   providing direct access to QCS."* $412K in FY2025; $143K in H1 2026.

**The whole of it covers about 12% of the cost of producing it** (TTM revenue $13.4M against
$110.5M of cost of revenue plus operating expense). The gap is not closed by customers. It is
closed by equity holders (~$659M of stock sold since the close, table above), by interest earned
on that equity cash (**$16.6M in FY2025 and $10.4M in H1 2026 — larger than the gross profit of
$2.1M and $3.6M in the same periods**, and inside operating cash), and now by a government grant
paid for in shares. **The company's own description of its position: *"We are still in the
technology development phase"* (10-K FY2025 Item 1A).**

**The scarce input the business controls:** Fab-1 — *"the industry's first dedicated and
integrated quantum device manufacturing facility"* (press language; the 10-K: *"Through Fab-1, we
own the means of production of our breakthrough multi-chip quantum processor technology"*) — the
chiplet-tiling patents, and 162 full-time employees, most of them *"in the areas of quantum
physics, chip and hardware engineering and software development"* (10-K FY2025, as of 2026-03-01).
**Whether any of it is scarce relative to the competitors the 10-K names — IBM, Google,
Microsoft, IonQ, D-Wave, Quantinuum, PsiQuantum, Amazon — is a Q2 question, and recorded there.**
What Q1 needs is narrower: does the company control an input that produces cash today? **No
construction of the filed record says so.** Rigetti's own gross profit was $2.1M in FY2025.

**Will the fundamentals look broadly the same in ten years? NO — by the company's own declared
program, and by the terms of its own risk factors.**
- The declared model is not the filed one: *"Our long-term business model centers on revenue
  generated from sales of quantum processing units ("QPUs") and quantum computing systems and
  providing access to quantum computing systems via the cloud in the form of Quantum Computing as a
  Service ("QCaaS")"* (10-Q Q2 2026 MD&A). **The long-term model is the two smallest lines in the
  filed record (cloud access: $325K TTM).**
- **That model is contingent on a technical event the filer says may never happen:** *"We believe
  that we will continue to incur operating and net losses each quarter until at least the time we
  begin generating significant revenue if we are able to achieve quantum advantage or LFTQC, which
  may never occur."* And: *"Commercial traction of quantum computing technology may never occur."*
  (10-Q Q2 2026, Item 1A.)
- **The roadmap has itself been constant change, in the filer's own admission:** *"We have in the
  past failed to meet publicly announced milestones and may fail to meet projected technological
  milestones in the future. In addition, we have in the past changed our technology roadmap,
  including the anticipated milestones and timing thereof"* (10-K FY2025 Item 1A). The filed record
  shows it: the FY2022 10-K carries a 2022 roadmap with *"the 336Q Lyra system, 1,000+ qubit system,
  4,000+ qubit system"*, revised in February 2023 to concentrate on an 84-qubit system; the FY2023
  10-K targets 99% on *"an anticipated Ankaa-3 84 qubit system by the end of 2024"* with Lyra
  following *"If the above target is achieved"*; Lyra never appears again; the product became a
  chiplet architecture (Cepheus, 36Q then 108Q). **The Q4 2025 release (2026-03-04) targeted *"the
  deployment of our 108-qubit system at 99.5% median two-qubit gate fidelity"*; the Q2 2026
  release (2026-08-06) reports it generally available at *"approximately 99.1%"*.** The current
  target is *"approximately 1,000 qubits … over roughly a three-year time horizon"* (Q2 2026
  release) — the class of number the 2022 roadmap put inside two years.
- **Even the revenue mix is not stable year to year**: government 90.7% of H1 2025 revenue and
  22.2% of H1 2026; quantum-computer sales $2.4M, then zero, then $7.1M; the largest customer
  (Customer F) 53% of H1 2025 revenue and not listed in H1 2026, where a different Customer A is 34%.

**THE ARGUMENT FOR IN, STATED AT FULL STRENGTH [E4-26, E4-51].** The project's own case law says
Q1 tests whether I can *state the mechanism*, not whether the business is placid. ORCL passed Q1
with a capital base compounding at ~90% a year because *"it makes the number uncertain, not the
mechanism unintelligible"*; FCN passed with five-year cash flows running 287 → 64 because *"Marking
Q1 OUT would be using the understanding gate to do the franchise gate's work."* On that reading
Rigetti is intelligible: a research-instrument maker and government R&D contractor with a small,
growing product line (H1 2026 revenue +191% on H1 2025, product sales at a higher gross margin per
the 10-Q, an $8.4M 108-qubit order, a $100M federal award), a stable and knowable cost base
(operating cash −$50.6M, −$50.6M, −$58.5M in FY2023-25), and $541.3M of cash and investments.
Every instability above could be carried to Q2 and Q4, where it would be tested on its own terms.

**Why it does not hold here — the ORCL distinction, checked rather than asserted.** Oracle's
forward engine sat **in the filed record as contracts**: $638bn of remaining performance
obligations. Rigetti's forward engine — QPU and QCaaS revenue at quantum advantage — sits in the
filed record as **$2.7M of remaining performance obligations** at 2026-06-30 (of which $1.1M beyond
twelve months), one ~$8.4M purchase order, and a $100M R&D grant that pays for research, not for
product, and can be clawed back. **The mechanism I can state is the mechanism of a laboratory
financed by its shareholders. The mechanism by which the company proposes to make money does not
yet exist in any customer's hands, at Rigetti or — on the filed evidence the 10-K itself gives —
anywhere, since the filer names quantum advantage as an event not yet reached by the industry.** A
research-instrument reading of today's business does not rescue the question either: the company
itself does not propose to live on it (*"Our long-term business model centers on…"* the other
lines), and at TTM scale it recovers 12% of its cost.

**THE ARGUMENT FOR OUT, ALSO AT FULL STRENGTH.** [E4-46] says a business that would take months of
study is outside the circle and *"no fetch repairs it"*; [E3-31] names *"subject to constant
change"* as the class the corpus cannot predict; the roadmap, the revenue mix and the funding source
all changed inside the filed window. **Why not OUT:** OUT is *"the evidence is here and the
business fails."* **The business has not failed — it has not yet happened.** A finding that the
superconducting chiplet approach will not produce a commercial product would be a finding about the
business; I have no evidence for it, and no amount of study available to this analyst supplies it.
[E4-46] converts a competence gap into OUT so that UNRESEARCHED cannot be abused; it does not
convert an indeterminate future into a verdict against the business. **[E3-47] names the cost of
getting this wrong in the other direction**, and the file stays open to the record that would
answer it.

**THE SEPARATING TEST, ASKED ALOUD: can I name the document that would resolve the ten-year shape
of this company's cash flows?**
- **Not a document that exists and I have not fetched** — that would be UNRESEARCHED. Every rung
  that could carry it has been read: the 10-K and 10-Q revenue disaggregation, RPO, customer
  concentration, the purchase commitments, the OTA's milestone schedule, the earnings releases, the
  roadmap statements across four annual reports.
- **The record that would resolve it does not yet exist**, and it can be named precisely: (1) a
  filed disaggregation showing **QPU/QCaaS revenue from customers using the systems for production
  (non-research) work**, over **two to three consecutive fiscal years**; (2) **remaining performance
  obligations** of a size that bear on a ~$110M annual cash cost; (3) a Rigetti system meeting the
  company's own named milestone — *"quantum advantage or LFTQC"* — on a filed, dated basis; (4) the
  DoC tranche-2 and tranche-3 determinations (*"in its sole discretion"*) actually made. **The same
  shape as HHH: the forward entity is, by its own declared program, not the filed entity.** HHH's
  record would exist with time; Rigetti's may exist with time or may, in the filer's own words,
  *"never occur"* — which is an argument that UNKNOWABLE is the ceiling of what the file can say,
  not an argument for more.
- **So: NO. UNKNOWABLE, closed without prejudice [E4-19].** This is not the shortcut the brief warned
  against: the verdict names four specific future records, the reading behind it is on disk, and the
  gates below are run in full as a record.

**What would re-open the file (so the closure is honest under [E3-47]):** items (1) and (2) above
together — two or more fiscal years in which product and access revenue from non-research customers
is reported separately and grows into a range that bears on the cost base, with backlog to match.
The roadmap milestones alone would not: the corpus prices cash, and a fidelity figure is not one.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE → the business the company declares
  it will be (QPU and QCaaS sales at quantum advantage) is not the business the filings record
  (grant-funded research contracts and research instruments recovering ~12% of cost, with the gap
  funded by stock); the filer says the event the model depends on *"may never occur"*; no
  document can close the gap until that record exists.**
- *The hard sequence closes the file here. **Q2-Q4 below are RECORDED, NOT GATES** (the HHH/ANF/L
  precedent), because the brief asks for them and the output contract requires a price under
  `COMPUTATION — NOT A CLEARANCE`. Nothing recorded below can reopen Q1.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]** — **RECORDED, NOT A GATE (file closed at Q1)**

*Run in full because the brief asks for it and because a closure at Q1 that avoided the franchise
question would be the CGNX error by another route. Nothing here reopens Q1.*

- **Needed or desired [x]** — by research buyers: national labs, supercomputing centres, government
  R&D programmes (C-DAC, NQCC, AFRL, DARPA). By production users, not yet on the filed record.
- **No close substitute [ ] — FAILS, on the filer's own words and on the marketplace it sells
  through.** The 10-K lists *"IBM, Google, Microsoft, IonQ, D-Wave, Quantinuum and PsiQuantum, among
  others"* and Amazon, and says of its own cloud channel that Amazon Braket and Azure Quantum
  *"operate a service in direct competition with our providing direct access to QCS."* **The
  channel that carries Rigetti's cloud revenue also sells IonQ's and Quantinuum's machines on the
  next line of the same menu** — IonQ's 10-K: *"We currently make access to our quantum computers
  available through three major cloud platforms, Amazon Web Services', or AWS's, Braket, Microsoft's
  Azure Quantum and Google's Cloud Marketplace."* A customer switching modality changes a drop-down.
- **Not price-regulated [x] — but the price-setter is the government regime [E2-59].** Government
  was 80.0-90.7% of revenue FY2021-H1 2025; the MD&A attributes the FY2025 revenue decline to *"the
  expiration of the National Quantum Initiative Act in September 2023 and its pending
  reauthorization."* A research line whose volume follows an appropriations act belongs to the
  regime, not to the company.

**Must the moat be continuously rebuilt? [E4-04] — YES, in the excluded sense: the basis is
periodically REPLACED, not defended.** The product architecture changed three times inside the
filed window — Aspen (80Q, 2022) → Ankaa (84Q, 2023-24, a *"fourth-generation chip architecture"*,
then Ankaa-3 with *"an extensive hardware redesign"*) → Cepheus chiplets (36Q 2025, 108Q 2026) —
and the 2022 roadmap's 336Q Lyra, 1,000+ and 4,000+ qubit systems were abandoned or re-dated. **The
spending buys the replacement, not a defence of the same advantage** — the Mitsui/Rhodes Ridge side
of [E4-04]'s scope test, not the Coca-Cola side. Capex has risen to fund it ($9.1M FY2023 → $18.7M
FY2025 → $16.4M in H1 2026 alone plus $10.1M unpaid at 2026-06-30), and the filer says *"we may seek
to significantly increase our capital expenditures, including to upgrade our current Fab-1 chip
fabrication facility, and possibly invest in a new quantum chip fabrication facility."*
**Great-manager dependence [E4-23]:** no single-person dependence is named; the dependence is on 162
physicists and engineers in a market where the 10-K says competitors *"may seek to hire our
personnel."* Recorded as a moat defect: the asset walks.

**Primary moat metric, filing-sourced, and its trend.** For a pre-commercial technology company the
honest moat metric is the one that shows whether a technical lead has turned into **contracted
customer money**: revenue and remaining performance obligations (RPO), set beside the cash consumed
to produce them. Direction: **Rigetti's revenue fell 46% FY2022-FY2025 ($13.1M → $7.1M) before the
H1 2026 instrument sales; its RPO fell from $9.7M (2022) to $2.7M (2026-06-30).** [E4-32] asks for a
moat widened every year; on the only filed measures of it, this one narrowed for three years.

### THE COMPETITOR ROW — required [E3-28]

**Same metrics, same windows, filing-sourced.** $M. Owner earnings here = operating cash − SBC −
capex (the capex end), the construction used for Rigetti below. XBRL transcription, each peer
cross-checked to its filed document on one figure (noted).

| Company | modality | revenue FY2024 | revenue FY2025 | revenue H1 2026 | RPO 2026-06-30 | OCF FY2025 | SBC FY2025 | owner earnings FY2025 | source |
|---|---|---|---|---|---|---|---|---|---|
| **Rigetti (RGTI)** | superconducting gate-model | **10.8** | **7.1** | **9.5** | **2.7** | **−58.5** | **17.6** | **−94.8** | 10-K `0001104659-26-023454`; 10-Q `0001104659-26-091993` |
| IonQ (IONQ) | trapped ion (+ acquired networking, sensing, satellites) | 43.1 | **130.0** (39% from acquired id Quantique / Capella, per the auditor's scope note) | **144.7** | **485.0** | −283.2 | **312.0** | −611.6 | 10-K `0001193125-26-071562` (*"Revenue increased by $86.9 million, or 202%, to $130.0 million"* — matches tag); 10-Q `0001193125-26-341001` |
| Quantinuum (QNT, IPO June 2026) | trapped ion | 23.0 | **30.9** (incl. $16.5M hardware sales-type lease) | 13.2 | **74.2** | −160.3 | not separable pre-IPO; $447.5M H1 2026 on IPO | n/a | 424B4 `0001628280-26-041003` (FY2025 revenue table $30,931K); 10-Q `0001628280-26-056743` |
| D-Wave (QBTS) | annealing + gate-model | 8.8 | **24.6** (incl. $16.2M system sales) | 5.9 | **40.7** | −72.0 | 22.7 | −98.6 | 10-K `0001907982-26-000026` (*"Revenue increased by $15.8 million, or 179%, to $24.6 million"* — matches tag); 10-Q `0001907982-26-000129` |
| Quantum Computing Inc. (QUBT) | photonic | 0.4 | 0.7 | 9.2 | n/r | −30.3 | 8.7 | −45.7 | companyfacts only — **transcription, not cross-checked; screening grade** |
| IBM, Alphabet (Google), Microsoft, Amazon | superconducting / topological / cat qubits | — | — | — | — | — | — | — | **no quantum segment disclosed**; this project's GOOGL and MSFT runs (2026-09-06) contain no quantum line |
| PsiQuantum | photonic | — | — | — | — | — | — | — | **private; no SEC filing found** (ticker map; S-1 full-text hits are mentions in other issuers' documents) |

- **Peers named: 4 filed pure-plays with figures (IonQ, Quantinuum, D-Wave, QCi) + 4 hyperscalers
  without segment data + 1 private, of the 9 the 10-K itself names.** The hyperscaler and private
  gaps would hold a moat class PROVISIONAL **if the filed row left the question open. It does not:
  Rigetti is last or second-to-last among the filed pure-plays on every commercial metric** —
  revenue FY2025 (below D-Wave 3.5x, Quantinuum 4.4x, IonQ 18x), RPO (IonQ 180x, Quantinuum 27x,
  D-Wave 15x). A hyperscaler datum could only add a stronger competitor, never lift Rigetti above
  the pure-plays already filed. **The class does not depend on the missing rows.**
- **Brief defect found:** the brief lists Quantinuum as *"private — state the limit."* **Quantinuum
  became an SEC registrant in June 2026** (424B4 filed 2026-06-05; Nasdaq QNT; first 10-Q filed
  2026-08-13). Its filed row is above.
- **Two facts in the peer filings that bear on Rigetti's distinctions:**
  1. **The $100M CHIPS award is not a Rigetti distinction.** Quantinuum's 10-Q (Q2 2026) records a
     Letter of Intent with the Department of Commerce announced **the same day, 2026-05-21, for the
     same "up to an aggregate $100" million**, also paid for in equity at a discounted price; IonQ's
     10-Q: the Department *"announced the signing of letters of intent to provide over $2 billion in
     federal incentives under the CHIPS and Science Act to nine companies, including certain
     competitors."* **The award is the regime funding the field [E2-59], not a customer choosing
     Rigetti over the field.**
  2. **Fab-1, the named scarce input, is under direct attack [E2-45].** IonQ's 10-K announces the
     pending acquisition of **SkyWater Technology** *"which we believe will accelerate our roadmap by
     providing us with embedded access to a secure quantum foundry"*, and in 2025 acquired Oxford
     Ionics to *"leverage semiconductor production and scaling."* The attacker with ample capital —
     IonQ raised and spent at five times Rigetti's rate in FY2025 — is buying the input Rigetti
     describes as its advantage.
- **What competitors say of Rigetti, read in their filings (not a hit count):** IonQ names it once,
  as a *"startup"* using the superconducting approach alongside Google and IBM; D-Wave names it twice,
  including that gate-model systems *"developed by others, such as IonQ, Rigetti, or Quantinuum … are
  significantly smaller in scale and capability when compared to D-Wave's systems"* — a competitor's
  claim, recorded as a claim.

**Is there any filed evidence of a moat — a technical lead that shows up in contracts or revenue —
or only in press releases? [E3-03, E2-44]** **Only in press releases and the 10-K's own descriptive
language.** The technical claims (*"99.9% two-qubit gate fidelity at 28 nanosecond gate speed on a
prototype platform"*; gate speeds *"about 1,000 times faster than alternative modalities such as trapped-ion and
neutral-atom systems"* in the releases of 2026-03-04 and 2026-05-21, re-cut to *"about 10,000
times faster than trapped-ion systems and 100 times faster than neutral-atom systems"* in those of
2026-08-06 and 2026-09-08 — **the same comparison moved an order of magnitude in each direction
inside three months, with no filed measurement behind either version**) are, where the filing
repeats them, *"based on internal testing"* on the filer's own qualification. **None of them appears in a filed
contract, backlog or revenue figure that exceeds a competitor's.** The trapped-ion companies the
speed claim disparages hold 27x and 180x Rigetti's contracted backlog.
- **[E2-44] two-characteristic test:** raise prices with flat demand — no evidence of any pricing
  event; grow dollar volume with minor additional capital — **the opposite**: FY2022-FY2025 capex of
  $61.6M and operating cash of −$222.4M produced revenue that fell.
- **[E2-45] attacker's test:** with ample capital and skilled people — IBM, Google, and now IonQ with
  a foundry — the question answers itself in the row.
- **[E4-36] which cause of extreme success:** none yet; the stock's 2024-25 rise (the 10-K records
  the price at $1.07 on 2024-06-28 and $11.86 on 2025-06-30) is **a wave in the capital market, not in
  the business** — the surfing run of [E3-51], ridden by the equity rather than the revenue, and the
  company used it: $346.7M of ATM stock sold in one quarter at a weighted $11.55.
- **Untapped pricing power [E3-33]:** none. [E5-28] makes the claim a near-monopoly claim; the row
  refutes it.
- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: narrowing** (revenue −46%
  FY2022-25 before the H1 2026 instrument sales; RPO $9.7M → $2.7M; last among filed pure-plays).
- **VERDICT (recorded, not governing): would be OUT** — [E3-03] criterion (2) fails on the filer's
  own list of substitutes sold through the same cloud channels; [E4-04] excludes a basis replaced
  three times in four years; the named scarce input is being bought by a better-funded competitor;
  and no filed contract, backlog or revenue figure carries the technical claims.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — **RECORDED, NOT A GATE (file closed at Q1)**
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE.**
- [x] **Daily execution** — **[E3-43]**: *"a business, unlike a franchise, can be killed by poor
  management."* Q2 recorded no franchise; every quarter's roadmap, hiring, fab and financing choice
  moves the outcome. This is the have-to-be-smart-every-day class **[E3-38]**.
- [ ] Control — a minority holder can sell.
- [ ] Leverage — no debt since the Trinity prepayment of 2024-12-09 (10-K FY2025 MD&A).

**Case declared: Q3 would be a BINARY GATE** on daily execution, and no price compensates [E1-16,
E3-29, E5-35].

**Honesty — binary, permanent, filings-based [E5-16].** Each matter dated to when it became public:
- **2022-11-14 — Item 4.02 non-reliance** on the Q1 and Q2 2022 10-Qs: the earn-out liability's
  volatility assumption *"should be revised to include a greater weight for the volatility of the
  trading price of the Company's public warrants."* A valuation-input error on a non-cash liability,
  self-identified during the Q3 close and restated by 10-Q/A (companyfacts carries both 10-Q/A
  accessions `0001193125-22-295445` and `-295450`). Auditor BDO USA (auditor since 2021, unchanged through FY2025). **A competence error, priced; not
  misconduct.**
- **No SEC enforcement action, no auditor resignation, no Item 4.01 dispute found** in the
  submissions list or the 8-Ks read (the one Item 4.01 is the March 2022 dismissal of the SPAC's
  auditor Marcum at the close, with *"no disagreements"*).
- **Insider selling, read from the Form 4 XML (54 filings since 2025-01-01, code S, aggregated in
  `_research … RGTI/form4_2025-2026.txt`): ~$69M sold by officers and directors in 2025-26** — CEO
  Kulkarni $16.5M, COO (then CTO) Rivas $21.4M, directors Clifton $8.8M, Johnson $7.5M, Sandford
  $4.2M, Iannotti $3.6M, Bertelsen (CFO) $3.5M, Fitzgerald $2.3M, McCarthy $1.2M. Two sales read
  individually, with the plan flag and footnotes:
  - **Kulkarni, 2025-05-20, 1,000,000 shares at a weighted $12.00, `aff10b5One` = 0 (not under a
    Rule 10b5-1 plan)** — nine days before the company signed the $350M Jefferies ATM (2025-05-29),
    which then sold 30.3M shares at a weighted $11.55. No 10b5-1 adoption by Kulkarni appears in the
    Q1, Q2 or Q3 2025 10-Q Item 5 disclosures; his first is dated 2026-06-10.
  - **Rivas, 2026-05-29, 499,328 shares at a weighted $25.40, not under a plan** — eight days after
    the Department of Commerce LOI was announced (2026-05-21), during negotiation of a definitive
    agreement whose share price was to be the lowest of three closes less 15%. The LOI was public
    when he sold; the definitive terms were not.
  - **The honest reading:** discretionary open-window sales of vested awards are lawful and common,
    and nothing in the filings says either sale breached a policy. **They are not a [E5-16]
    disqualifier on this record.** They are an incentive fact under operator rule 9 and **[E4-27]**:
    the people with the best information sold at the same prices at which the company sold stock to
    the public, which says what both thought of those prices.
- **Verdict on honesty (recorded): no integrity disqualifier found.** Under [E5-17] this is the
  absence of a found disqualifier, not a finding that the managers are honest.

**STEP 2 — THE FLAGS [E4-22, E5-15].** *Each a prompt to read.*
- [x] **Serial share issuance [E5-15] — FIRES AT FULL STRENGTH.** *"one of the surest indicators of a
  promotion-minded management, weak accounting, a stock that is overpriced and — all too often —
  outright dishonesty."* **3.00x the share count in four and a half years, through seven channels**
  (Step 0 table), with the company's own liquidity language making it the plan: *"we believe we will
  meet our cash requirements and obligations primarily through our existing cash, cash equivalents
  and available-for-sale investments, potential securities financings or other capital sources"*
  (10-K FY2025). Read what the flag names, one by one: promotion-minded — see the projections flag;
  weak accounting — see below, mild; stock overpriced — **the insiders' own sales and the company's
  ATM both say so at $11.55-$25**; outright dishonesty — none found.
- [x] **Trumpeted projections [E4-22 third flag] with the [E3-48] action — FIRES; guidance against
  outturn, from the filings:**

  | stated | where, when | outturn |
  |---|---|---|
  | 2022 roadmap incl. *"the 336Q Lyra system, 1,000+ qubit system, 4,000+ qubit system"* | 10-K FY2022 (describing 2022) | revised February 2023; Lyra never delivered; no 1,000Q system as of 2026-09 |
  | *"at least 99% 2-qubit gate fidelity on an anticipated Ankaa-3 84 qubit system by the end of 2024"* | 10-K FY2023 | **met**: 99.0% median iSWAP, 99.5% fSim (10-K FY2024, internal testing) |
  | FY2025 executive bonus: 100+ qubit median 2Q fidelity ≥99.2% for 50% of target, 99.5% target | DEF 14A 2026 | **missed; *"the Executive Bonus Plan pool was not funded and no bonus amounts were awarded"*** |
  | *"deployment of our 108-qubit system at 99.5% median two-qubit gate fidelity"* | Q4 2025 release, 2026-03-04 | **99.1%** at general availability (Q2 2026 release, 2026-08-06) |
  | *"significant first-quarter year-over-year revenue growth"* from Novera orders | Q4 2025 release | **met**: Q1 2026 revenue $4.4M vs $1.5M |
  | *"approximately 1,000 qubits … over roughly a three-year time horizon"* | Q2 2026 release | open |

  The filer states the pattern itself: *"We have in the past failed to meet publicly announced
  milestones … we have in the past changed our technology roadmap."* **Two met, three missed or
  abandoned, one open.** The projections are technical, not earnings — which is why they carry the
  valuation: the price in Q5 is almost entirely a price for the roadmap.
- [x] **Adjusted-earnings promotion [E4-29] — FIRES, in the SBC form [E5-06].** Every release read
  headlines *"non-GAAP net loss"* beside GAAP in its opening bullets (Q2 2026: GAAP −$52.6M, non-GAAP
  −$16.0M; FY2025: GAAP −$216.2M, non-GAAP −$50.5M). The reconciliation removes **stock-based
  compensation** and the warrant and earn-out fair-value changes. Removing the fair-value noise is
  defensible — those swings are non-economic for the business (H1 2025 showed **GAAP net income of
  +$3.0M on an operating loss of −$41.5M**, purely from warrant marks). **Removing SBC is the named
  error: *"To say 'stock-based compensation' is not an expense is even more cavalier"* [E5-06].** And
  the non-GAAP figure keeps **interest earned on the equity raised** ($5.1M in Q2 2026), so the
  headline loss is also flattered by the financing. No EBITDA figure appears.
- [x] **Stock-price-conditioned pay [E3-50] — FIRES, historically.** 3,850,000 RSUs granted in 2023
  vested *"when the Company's Common Stock traded at or above $2.00 per share"* (50%) and at a higher
  price for the rest (10-K FY2025 Note 12); 500,000 options granted in 2022 carried a market-based
  condition satisfied in January 2025. **Current design is better**: the FY2025 cash bonus was tied to
  a pre-set technical bullseye and was **not paid when missed**; 2026 RSU counts use a 60-day average
  price.
- [ ] **Weak accounting — MILD, not the cockroach pattern.** The 4.02 above; the earn-out and warrant
  liability accounting that makes GAAP net income meaningless in both directions (a presentation
  consequence of the SPAC structure, disclosed line by line); **XBRL scale errors** in the 2023 10-Qs
  (weighted shares tagged in thousands as units). Revenue recognition (input method, milestones) is
  conventional and small.
- [ ] Unintelligible footnotes — no; the notes are plain.
- [ ] Filed-figure fraud tells [E4-30] — not computable: no pretax income, no cash taxes; revenue is
  not smooth (the opposite).
- [x] **[E2-49] metric-switching — FIRES, mildly, with the reasons announced.** The 2022 yardstick was
  qubit count (84Q → 336Q → 1,000Q → 4,000Q); in February 2023, after the 80Q Aspen-M generation and
  with a 28% workforce reduction (8-K Item 2.05, 2023-02-10), the roadmap switched to *"increasing the
  performance"* — fidelity — at a fixed 84 qubits. The switch followed deterioration, which fires the
  prompt; it was announced ahead with reasons, which is the candor half. **My [E2-49] tally: thirteen
  fires, seven failures** (after CNR's twelve and seven).
- [ ] Dividends funded by issuance [E2-52] — no dividend.

**THE LOLLAPALOOZA READ [E4-52].** Serial issuance + technical projections that carry the
valuation + a non-GAAP loss excluding stock pay + historical price-vesting pay + ~$69M of insider
selling at the prices the company issued at: **five flags pointing one way — toward selling the
equity while the market pays for the roadmap.** The countervailing facts are real and recorded: the
10-K admits failed milestones in its own words; the missed-fidelity bonus was not paid; the company
**cut 28% of staff when the stock was below $1** (two Nasdaq bid-price deficiency notices,
2023-01-25 and 2024-09-16) rather than issuing at any price; and **selling stock the market overprices
is the rational act for the remaining owners [E5-44, E5-24]** — the $346.7M raised at $11.55 bought
most of today's $541M balance.

**STEP 3 — THE PRIMARY TEST [E2-01].** Operating loss on average equity: FY2023 −55.7%, FY2024
−58.0%, FY2025 −25.2% (FY2025's improvement is the denominator — $419.6M of equity raised — not the
numerator, which worsened from −$68.5M to −$84.7M). Owner earnings on average equity FY2023-25:
−55.5%, −63.3%, −28.2%. FY2022's equity turned from −$71.5M to +$150.2M at the close, so no
meaningful ratio. **Never positive in any filed year, FYJan-2021 through H1 2026.**

**The half-owner test [E2-26]:** the 10-K passes on disclosure — failed milestones, the NQI Act
revenue hit, the 24- and 36-qubit systems' *"lower gross margin profile"*, the full share-reserve table.
The releases fail on the non-GAAP headline. **Authorship [E2-72]:** releases are CEO-quoted
boilerplate; nothing distinctive.

**The institutional imperative [E2-30]:**
- [ ] resists change — no; the roadmap and org have changed repeatedly (2023 RIF; 2026-08 COO/CTO split)
- [x] **projects materialise to soak up available funds** — after $381.7M of 2025 equity: a
  **$250M five-year investment commitment** under the Quanta collaboration (Feb 2025), a **planned
  $100M UK investment** (Q2 2026 release), a *"possibly … new quantum chip fabrication facility"*
  (10-K), and H1 2026 capex of $16.4M paid plus $10.1M unpaid, against FY2023's $9.1M full year
- [ ] staff studies — not observable
- [x] **peer imitation** — the DoC equity-for-grant structure was signed the same day by Quantinuum;
  every filed pure-play runs ATM funding and a qubit-count roadmap

**Capital allocation — the two buyback conditions [E5-08]:** no buybacks; the question inverts. The
issuance at $11.55 (2025) and $12.92 (DoC, 2026) against a business whose Q4 computation below cannot
support either price is, from the remaining owners' side, **the correct direction of the trade**
[E5-44]. The capital-allocation read is about the use of the proceeds: into a roadmap that the row in
Q2 shows trailing, and into commitments (Quanta $250M, UK $100M, a second fab) that raise the burn.
**Humility clause [E4-13]:** management knows the physics and the pipeline far better than this
analyst.

**THE GUARDRAIL.**
- [x] Nothing here promotes the name; a strong Q3 could not repair Q1 or Q2.
- [x] Key-person dependence recorded at Q2 (the 162-person team), not here.
- [x] The manager is the plan: there is no intact franchise with an excisable cancer [E2-36]; the
  business IS the execution of a roadmap.

- **VERDICT (recorded, not governing): no integrity disqualifier found [E5-16, E5-17]; as a gate it
  would read IN on honesty with FIVE CONVERGING PRESENTATION AND INCENTIVE FLAGS LIVE** ([E5-15],
  [E3-48], [E4-29]/[E5-06], [E3-50], [E2-49]) and a use-of-proceeds read that raises the burn. *IN
  never promotes.*

---
## Q4 — WILL IT SURVIVE? — **RECORDED, NOT A GATE (file closed at Q1)**

### Owner earnings — the one number **[E2-23]**

**Construction (CONVENTION, per the framework):** operating cash flow − stock-based compensation −
(c). Every figure from the filed cash-flow statements (10-K FY2022 for FY2022 and the 11-month
FY2021; 10-K FY2023, FY2024, FY2025; 10-Q Q2 2026 and Q2 2025 for the TTM; **FY ended 2021-01-31
from the de-SPAC 8-K EX-99.1** — never from the colliding companyfacts rows described in Step 0).
Script: `_research 2026-09-13 RGTI/oe.py`. $K.

| period | revenue | OCF | SBC | capex | D&A | **OE, capex end** | **OE, D&A end** | SBC ÷ revenue |
|---|---|---|---|---|---|---|---|---|
| FY ended 2021-01-31 (Legacy, 8-K EX-99.1) | 5,543 | −30,067 | 2,592 | 4,400 | 4,299 | **−37,059** | **−36,958** | 46.8% |
| FY2021 (11 months) | 8,196 | −29,044 | 1,765 | 7,008 | 4,651 | **−37,817** | **−35,460** | 21.5% |
| FY2022 | 13,102 | −62,689 | 44,812 | 22,737 | 7,017 | **−130,238** | **−114,518** | 342.0% |
| FY2023 | 12,008 | −50,579 | 12,409 | 9,059 | 7,426 | **−72,047** | **−70,414** | 103.3% |
| FY2024 | 10,790 | −50,627 | 13,069 | 11,098 | 6,906 | **−74,794** | **−70,602** | 121.1% |
| FY2025 | 7,088 | −58,543 | 17,605 | 18,676 | 8,169 | **−94,824** | **−84,317** | 248.4% |
| TTM to 2026-06-30 | 13,353 | −60,716 | 22,787 | 26,866 | 9,930 | **−110,369** | **−93,433** | 170.7% |

**Every window, both (c) ends — the spread is part of the range [E4-25, E4-38]:**

| window | OE mean, capex end | OE mean, D&A end |
|---|---|---|
| five periods FY2021(11m)-FY2025 | −81.9M | −75.1M |
| **five-year default [E2-42]: FY2022-FY2025 (four full years; the fifth is the 11-month stub)** | **−93.0M** | **−85.0M** |
| three years FY2023-FY2025 | −80.6M | −75.1M |
| two years FY2024-FY2025 | −84.8M | −77.5M |
| six periods FY-Jan-2021 to FY2025 | −74.5M | −68.7M |
| TTM | −110.4M | −93.4M |

- **Combined range: −$110.4M to −$68.7M a year. Negative on every window, both (c) ends and the TTM.
  In dollars and a word: a loss of $69-110 million a year, every year on file, and widening** — the
  TTM is the worst figure in the table. **The range is not too wide for a conclusion; it is narrow
  and entirely below zero [E4-25].**
- **Distortions named [E4-41]:** FY2022 carries $8.5M of one-time SBC catch-up on the liquidity
  condition triggered by the close (10-K FY2022 MD&A: $1.6M + $6.9M) — removing it leaves −$121.7M,
  still the worst full year. **The favourable break runs the other way and is NOT removed from OCF
  above: interest earned on the equity raised — $5.1M FY2024, $16.6M FY2025, $10.4M H1 2026 — sits
  inside operating cash.** Stripped out, the operating business consumed ~$111M (FY2025) and ~$132M
  (TTM) at the capex end. The table flatters the business by the financing.
- **Maintenance capex — the judgment [E3-44, E5-20].** D&A is the corpus default; **for this filer
  the D&A end is judged INVALID, not merely optimistic**: the capex does not maintain a unit volume,
  it buys the next architecture (Aspen → Ankaa → Cepheus, Q2), and the company's own position is
  that it cannot stand still (*"Our ability to compete successfully depends on continuous innovation
  … failure to do so could render our quantum computing systems obsolete"*). D&A ($9.9M TTM) runs at a
  third of cash capex ($26.9M TTM) with a further **$10.1M of property purchases unpaid at
  2026-06-30** (10-Q supplemental), so even the capex end understates the period's commitment. **(c)
  sits at the capex end, and the D&A column is shown only as the display of the guess.**
- **Stock compensation subtracted in full [E5-06]; RESOLVES and is COMPLETE.** The cash-flow add-back,
  the equity-statement line and the Note 12 expense table agree to the dollar every year checked
  (FY2025 $17,605K all three). Items read for incompleteness, the BA/BE lesson: the *"Vesting of
  Promote Sponsor Vesting Shares"* ($32,946K) and *"Sponsor Redemption-Based Vesting Shares"*
  ($10,433K) credits to APIC in FY2025 are **earn-out liability reclassifications for the SPAC
  sponsor, not pay for service** — correctly outside SBC; the $6,272K sell-to-cover outflow (FY2024)
  and inflow (FY2025) net to zero; the 2020 Customer Warrant (2,680,607 shares at $1.152, grant-date
  value $0.2M) is immaterial. **No stock-settled pay found under a non-SBC tag.**
- **[E3-70] — the charge is the floor.** RSUs granted in FY2025: 3,722,285 at a weighted grant-date
  fair value of $14.02 = **$52.2M of stock granted in a year whose charge was $17.6M**; unrecognized
  compensation at 2025-12-31 $49.8M (RSUs) + $2.3M (options). On a grant-date basis FY2025 owner
  earnings would be ~−$129M, not −$95M.

**SBC ÷ OPERATING CASH — THE CALIBRATED ROW, AND WHY RGTI CANNOT BE PLACED ON IT.** The row (ACVA
330.5% cumulative · ROKU 140.2% · CALX 98.4% · ARM 96.6% · CRWD 68.0%) measures **what share of
positive operating cash stock pay consumes.** Rigetti's operating cash is **negative in every filed
period**, cumulatively **−$283.5M** from FY2021(11m) to H1 2026 against SBC of $102.6M. **A ratio on
a negative denominator is not a ratio** — the same refusal this project wrote into `level_shift` —
so it is refused in words, not computed. **Where it sits: off the end of the row.** At ARM stock pay
ate the owners' share of real operating cash; at Rigetti there is no operating cash for it to eat —
**stock pay is added to a loss**, and the stock that pays it is sold to the public to fund the loss.
The substitute measure, stated so it can be compared: **SBC was 169% of cumulative revenue**
FY2021(11m)-H1 2026 ($102.6M on $60.7M), 248% in FY2025.

### Great, good, or gruesome? **[E4-20]**
- [ ] great · [ ] good · [x] **gruesome — and past the corpus's own description.** *"The worst sort
  of business is one that grows rapidly, requires significant capital to engender the growth, and
  then earns little or no money."* Rigetti requires the capital and earns none, **without the
  growth**: revenue $13.1M (FY2022) → $7.1M (FY2025) on $61.6M of capex and $222.4M of operating
  cash consumed. The H1 2026 instrument sales are the first growth in three years, off that base.
  [E4-43]'s exception — *"unless the cash they consume gets to earn a reasonable return"* — has no
  figure to apply to.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — ABSENT.** Owner earnings negative in all seven
  periods on file.
- **(2) massive liquid assets — PRESENT, and bought with stock.** Cash $27.8M + available-for-sale
  $365.9M short-term + $147.6M long-term = **$541.3M at 2026-06-30** (~$1.59 a share), no debt. Plus,
  contingently: the DoC first tranche of $43.9M (restricted to project costs, recoverable *"as a debt"*
  on default); ~$100M if the 8.72M $11.50 warrants are exercised before 2027-03-02 (in the money at
  $15.27).
- **(3) no significant near-term cash requirements — PASSES in the narrow sense.** Purchase
  commitments $35.0M, ~$21.0M of it equipment (10-Q); operating leases $7.7M; the April 2026 sublease;
  no maturities. **The larger claims are programmes, not contracts:** the Quanta collaboration's
  *"invest at least $250.0 million in the field of quantum computing … over a five-year period"*
  (satisfiable by the R&D the company would spend anyway), the planned *"up to $100 million in the
  United Kingdom over the next several years"*, and a *"possibly … new quantum chip fabrication
  facility"*. Each raises the burn the balance sheet has to cover.
- **CASH RUNWAY:** TTM cash consumed (OCF + capex) **$87.6M → 6.2 years** on $541.3M. **Ex-interest**
  (the interest disappears as the balance does) **$109.4M → 4.9 years**; with the $10.1M of unpaid
  capex settled, **~4.6 years**. The announced UK, fab and hiring plans shorten it; the DoC tranche and
  warrant cash lengthen it. **Round-number answer: roughly five years, before the next equity raise
  becomes the question.**
- **Leverage [E4-16, E3-29]:** none — debt repaid December 2024. The derivative warrant liability
  ($78.4M, current) settles in shares, not cash.
- **[E5-39] — the design principle this business inverts:** *"We will never be dependent on the
  kindness of strangers."* **Every dollar of the $541.3M came from strangers buying stock**, and the
  next five years' survival beyond it depends on them buying more.

**IS THE AT-THE-MARKET PROGRAMME THE BUSINESS MODEL? YES, on the filer's own words and record.**
Liquidity is met *"primarily through our existing cash … potential securities financings or other
capital sources"* (10-K FY2025). Since the close, equity raised (~$659M plus $225.6M at the close)
has been **2.4x the operating cash and capex consumed** (−$283.5M − $85.0M) — the surplus is today's
balance. The company has sold stock through seven channels, and **the size of each raise has tracked
the share price, not the business**: $20.5M on the B. Riley line in 2023 at ~$1.53, $346.7M in one
quarter of 2025 at $11.55.

### Name the specific way THIS business dies **[E2-27, E3-24]**

**The registered shapes, tested:** ORCL (contracted not to stop) — no contracts of size; ARM (earns
nothing for owners after paying its people) — Rigetti earns nothing *before* paying them; BE (too
little history) — five-plus years are on file, and they agree; BA (spends cash undoing past work) —
no; SWK (dividend by selling the business) — no dividend; ACVA/FLNC/NEGG (the borrowed balance sheet:
customers', vendors' money) — Rigetti's balance sheet is not borrowed, it is **sold**; CNR (the long
tail on a short cycle) — no long claims. **None fits. AN EIGHTH SHAPE: THE EQUITY IS THE REVENUE.**
A laboratory whose customers pay ~12% of its costs and whose owners pay the rest, by buying newly
issued shares at whatever price the market sets on the roadmap. It does not die when cash runs out;
it dies — for the owner — **when the price the market will pay for the roadmap falls below the price
at which the next raise covers the burn**, and each raise below that price transfers the company to
the new buyers.

**The mechanism, quantified from the company's own filed record — this has already happened once:**
- **2023:** stock below $1.00 (Nasdaq bid-price deficiency notice 2023-01-25, Item 3.01); cash and
  investments at 2023-12-31 **$99.9M** against FY2023 cash consumed of **$59.6M → 1.7 years**; a
  **28% workforce reduction** (Item 2.05, 2023-02-10) and a roadmap cut from 336/1,000/4,000 qubits to
  84; equity raised on the B. Riley line at ~$1.53. **A second deficiency notice 2024-09-16.**
- **The rescue was the market, not the business**: revenue fell in both 2024 and 2025 while the stock
  went from $1.07 (2024-06-28) to $11.86 (2025-06-30), and $541M was raised into the rise.
- **Forward case at today's filed economics:** at ~$110M a year of ex-interest cash consumption and
  rising (UK, fab, headcount), the $541.3M balance reaches the 2023 position (under two years of
  runway, ~$200M) in **about three years**. If the price the market pays for the roadmap has by then
  returned toward its 2023-24 level, a raise covering two years of burn (~$220M) at $2 a share would
  issue ~110M shares — **a third of today's company — to stay where it is.** At $1, two-thirds.
- **Exposure, not experience [E4-40]:** the H1 2026 instrument revenue and the DoC award are the
  benign recent experience. The exposure is in the filings: the competitor row (IonQ spending five
  times as much with 180x the backlog, and buying a foundry), a government revenue line that fell with
  one lapsed act, milestones the filer says it has missed before, and a roadmap that must be bought
  again every two years.
- **Likelihood, in the corpus's vocabulary [E3-24]:** **permanent impairment of a purchase at today's
  price through dilution or a lapsed roadmap — a real possibility;** insolvency inside five years with
  no raise — **a low-level possibility** ($541M, no debt).
- **The bar [E4-51] — the bull case stated so its holders would accept it:** superconducting qubits
  keep the fastest gates in the industry; chiplet tiling is a manufacturable scaling path; the US
  government has just paid $100M for a stake and Commerce framed it as national industrial policy;
  on-premises systems are selling to national centres (C-DAC $8.4M, NQCC, PSC); $541M funds the
  roadmap for years without another raise; and the one event that matters — quantum advantage — would
  make today's revenue irrelevant. **Every clause of that case is about the future; the filings
  record none of it as cash.**

- **VERDICT (recorded, not governing): would be OUT** — gruesome [E4-20] without the growth; [E5-11]
  strength (1) absent on every construction; survival conditional on continued equity sales, which is
  dependence on the kindness of strangers [E5-39]; the eighth survival shape, THE EQUITY IS THE REVENUE.

---
⛔ **Q5 does not open: Q1 is UNKNOWABLE (and Q2, Q4 are recorded OUT).** UNKNOWABLE closes the
file; it is not a pass.

---
## COMPUTATION — NOT A CLEARANCE
*Operator rule 3 and the queue's output contract: the operator gets a number; it carries no entry
language. None of the arithmetic below is a valuation of a business that cleared the gates.*

**Inputs.** Price **$15.27** (2026-09-11 close, Yahoo, aggregator flagged) × **341,508,685 shares**
(10-Q cover 333,768,747 at 2026-08-03, `0001104659-26-091993`, + 7,739,938 issued to the Department
of Commerce 2026-09-08, `0001104659-26-105662`) = **cap $5,214.8M**; ~$5.59bn on ~366.1M fully diluted
shares before exercise proceeds. Sovereign **5.35%** USD (Treasury 30-year, 2026-09-11).

**1. THE YIELD.** Owner earnings **−$110.4M to −$68.7M** ÷ $5,214.8M = **−2.1% to −1.3%**, against a
5.35% bond: **6.7 to 7.5 points BELOW the sovereign.** On the five-year default window (FY2022-25,
capex end) −$93.0M → −1.8%.

**2. WHAT THE PRICE ALREADY ASSUMES.** *The year-1 growth needed to justify the quote is not a
number*: growth from a negative base to a positive figure has no rate (the `growth_required` refusal,
2026-09-12). **In words and dollars instead:** the ~10% floor **[E4-28]** on a $5,214.8M price needs
**~$520M a year of owner earnings.** The filed record's best period produced −$68.7M. **The distance is
~$590M a year, and it has to be made up by revenue that is $13.4M today.** As an illustration only
(CONVENTION, not a forecast and not a filed margin — **no filed pure-play has a positive owner-earnings
margin**): at owner earnings of 20-40% of revenue, $520M needs **$1.3-2.6bn of annual revenue, 100-195x
the trailing twelve months**, and that is *before* discounting for the years it takes to arrive. The
base rate that governs a case of this kind **[E4-35]**: *"fewer than 10 of the 200 most profitable
companies"* sustain 15% EPS growth for twenty years; Rigetti is not among the profitable to begin with.
The second bound **[E4-44]**: value *"cannot over the long term grow faster than its earnings do"* —
and there are no earnings.

**3. WHAT YOU ARE PAID.** Nothing: the return on the current price from owner earnings is negative, **~7
points under the sovereign**, and the business consumes the cash it holds.

**WHAT THE BUYER IS PAYING FOR, IN WORDS.**
- **$1.59 a share of cash and Treasury securities** ($541.3M at 2026-06-30) — **about 10% of the
  price** — which the business is spending at roughly **$0.26-0.32 a share a year** (TTM cash consumed
  $87.6M-$109.4M ÷ 341.5M shares) and which the company's own announced plans (UK, a possible second fab,
  hiring) will spend faster.
- **$13.68 a share — about $4.67bn — for an option**: that Rigetti's superconducting chiplet roadmap
  reaches a commercially valuable machine (*"quantum advantage or LFTQC, which may never occur"*) before
  IonQ, Quantinuum, IBM, Google and the rest, and before its cash, and that the owner is still holding
  a meaningful share of the company when it does. **The company itself collects part of that option's
  premium from new buyers every time it sells stock**, which is how the $541M was raised.
- **What the shares carry that the cash does not**: a US government holder of 7.7M shares with transfer
  limits and a consent right over mergers; 11.7M warrants, 6.7M RSUs and 6.1M options ahead of the
  current holder's slice; and a Department that may *"demand recovery … as a debt"* of disbursed award
  money on default.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01].**
- **Conservative: roughly $1 to $2 a share** — the cash balance with nothing for the technology, less
  what a wind-down or a year of continued burn would consume. This is the only end the filed record
  supports with arithmetic.
- **Optimistic: NO NUMBER.** There is no year of positive owner earnings, on any window or either (c)
  end, from which to project; an optimistic value would be a price for the roadmap, which is exactly the
  judgment Q1 found no document to support. **Stating one would be the [E5-43] error — the apparatus
  producing the wanted output.**
- **Current price: $15.27.**

**The screamer test [E4-01], stated only to show where the number sits:** price $15.27 against a
conservative case of ~$1-2 — **above the only computable range by roughly eight to fifteen times.**
Outcome: **"no."** **Floor [E4-28]: honest pre-tax expectancy from owner earnings at this price is
negative — below ~10%, quit on.** Margin used: none (no bar applies). **Windage count: zero** —
conservatism was not spent, because no valuation was reached; the D&A end was shown and judged invalid
at Q4, which is a (c) judgment, not a margin.

**What bounds the upside [E2-63]:** unbounded in principle (an option), bounded in practice by dilution —
every future raise divides the outcome, and the 2023 record shows raises happen when the price is low.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**Not opened as an entry instrument — file closed at Q1.** No thesis, no position, **no alert armed and
no PORTFOLIO row** (the QLYS ruling: a price alert on a name that failed on the business is a category
error). **What would reopen the file, pre-committed in writing [E1-02]:**

- **Q1 (the governing closure):** two or more consecutive fiscal years in which the revenue note
  separates **QPU/QCaaS revenue from non-research commercial customers**, growing into a range that bears
  on a ~$110M annual cash cost, **with remaining performance obligations to match** (today $2.7M); and a
  filed, dated statement that a Rigetti system has reached the company's own named milestone. Fidelity
  figures alone do not reopen it.
- **Q2 (recorded OUT):** Rigetti's revenue or backlog overtaking a filed pure-play competitor (D-Wave's
  $40.7M RPO is the nearest) for four consecutive quarters; a multi-year contract on which a customer
  chose Rigetti's modality over a named alternative, in the filing rather than a release.
- **Q4 (recorded OUT):** operating cash **excluding interest income** positive for four consecutive
  quarters; or a year in which the share count does not grow by more than the vesting of employee
  awards.
- **Q3 (live flags):** a release series that drops SBC from its non-GAAP exclusions; the 1,000-qubit /
  99.9% / three-year target met or missed on the date it was set against (≈ mid-2029).
- **Next dated catalysts:** C-DAC 108-qubit deployment (H2 2026); public warrant expiry **2027-03-02**
  (~$100M of cash and ~8.7M shares if exercised); DoC tranche-2 milestone determination; the FY2026 10-K
  (≈ March 2027).
- **The crystallized-view trigger [E2-40]** does not arise: nothing is held.

- **VERDICT: not opened — file closed at Q1.**

---
## THE OUTPUT CONTRACT — PRICE AND PASS/FAIL
- **PRICE: $15.27** (2026-09-11 close, aggregator flagged) · **341,508,685 shares** · **cap $5,214.8M** ·
  sovereign **5.35%** · owner-earnings yield **−2.1% to −1.3%** (COMPUTATION — NOT A CLEARANCE) ·
  conservative value **~$1-2 a share**, optimistic **not computable**.
- **PASS/FAIL: FAIL at Q1 — UNKNOWABLE, closed without prejudice.** The business the company declares it
  will be is not the business its filings record, and the event the declared model depends on is one the
  filer says *"may never occur."* Q2 (would be OUT), Q3 (no disqualifier; five converging flags) and Q4
  (would be OUT) are recorded, not governing.

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 UNKNOWABLE closes the file; Q2-Q4 recorded
      under explicit NOT A GATE banners; Q5 not opened, its arithmetic headed COMPUTATION — NOT A
      CLEARANCE; Q6 not opened.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** No gate is marked IN.
      The recorded Q3 honesty read is worded as absence of found disqualifiers [E5-17].
- [x] Every UNRESEARCHED verdict names the artifact — none issued. Two places came close and were
      resolved by fetching rather than labelling: Quantinuum's figures (brief said private; it filed a
      424B4 and a 10-Q) and whether the insider sales were under 10b5-1 plans (Form 4 XML flag read).
- [x] **The UNKNOWABLE verdict states what specifically cannot be known**: four named future records
      (production-customer QPU/QCaaS revenue over 2-3 years; RPO bearing on the cost base; a filed dated
      milestone; the DoC tranche determinations), and why none can exist today.
- [x] **Step 0: the filing was read, with accession numbers; figures cross-checked** (FY2025 OCF, SBC and
      capex to the dollar on the cash-flow statement; H1 2026 OCF).
- [x] Owner earnings on multi-year means; **every window and both (c) ends published**; the D&A end judged
      invalid and shown only as the display of the guess; SBC resolves and complete; the de-SPAC
      splice excluded by accession.
- [x] Competitor row filled from four filed pure-plays, each cross-checked to its document on one figure
      except QCi (labelled screening grade); the hyperscaler and PsiQuantum limits stated, with the reason
      they do not change the class.
- [x] Sovereign for the earnings currency, from the issuing authority, dated.
- [x] Value stated as a round-number range, with the optimistic end refused in words.
- [x] One bar only named (screamer, to locate the number); windage count stated as zero.
- [x] Price dated; aggregator used for the live quote only and flagged.
- [x] **Run committed to git with a pathspec after every section** (52bf986 Step 0, 47792ee Q1, fcba565 Q2,
      c28d46e Q3, 5854c7c Q4).
- **Priors, scored [E4-26]:**
  1. *Operator: an early close at Q1, Q2 or Q4.* **CONFIRMED at Q1** — and the run built the case for Q1 IN
     at full strength first (the ORCL/FCN precedent), and the case for Q1 OUT, before choosing
     UNKNOWABLE on the HHH test. **Q2 and Q4 would each have closed it independently.**
  2. *Queue guard: ATM dilution, not a perimeter change.* **CONFIRMED and extended** — seven issuance
     channels, the seventh (shares to the government for a grant) post-dating the guard.
  3. *De-SPAC CIK may hold the shell's history.* **CONFIRMED, and worse than either alternative the brief
     posed: it holds BOTH**, under colliding keys, and an annual filter keeps the shell's year.
  4. *The two Item 1.01 filings are financing.* **HALF REFUTED**: one is a sublease; the other is a
     government R&D grant paid for in equity — financing in substance, not an ATM or a revolver.
  5. *My own: revenue small and government-dominated, operating cash funded by equity.* **Confirmed on
     equity; refuted on the government share for H1 2026 (22.2%, down from 90.7%).**
- **Strongest single fact AGAINST the conclusion [E4-51]:** **H1 2026 revenue of $9.5M was 191% above H1
  2025, driven by on-premises system sales at a higher gross margin than the research contracts they
  replace, with an $8.4M 108-qubit order behind it and $541M of cash and no debt behind that** — the
  first sign in the filed record of a product business separable from grant research. It does not reopen
  Q1: the TTM still recovers ~12% of cost, the RPO is $2.7M, and the buyers are research institutions
  buying instruments, not production users; but it is the shape the Q1 reopening condition would start
  from.
- **Defects in the brief:** (1) *"Quantinuum and PsiQuantum (private — state the limit)"* — **Quantinuum
  listed in June 2026** and files a 10-Q; its row is in Q2. (2) The deal_note framing *"most likely
  financing or an at-the-market programme"* missed the **CHIPS award with shares to the Department of
  Commerce**, which changes the share count used for the cap by 7.7M. (3) *"Compute SBC/OCF cross-checked
  to the dollar and place it in the calibrated row"* — **the ratio does not exist for this filer**
  (operating cash negative in every period); refused in words, placed off the end of the row, and a
  substitute (SBC ÷ revenue) stated. (4) *"This is the last name in the operator's watchlist queue"* —
  it is the last of the overnight list, but **CVX (tier 2) remains unstruck in its roster and absent from
  COMPLETED though a run file exists** (`Test Runs/2026-09-02 Run - CVX Chevron.md`, Q2 OUT, folded into
  the reading list only), and **BRK-A, HHH, GHC, BAM, BN remain unstruck in the MINI BERK roster** (HHH
  and GHC are registered in COMPLETED; BAM and BN are blocked). Not edited here — recorded for the
  operator.
- **Tooling defects:** (1) **`sources.annual()`'s 340-day floor selects the SPAC shell's 365-day FY2021
  over Rigetti's 334-day transition year** — OCF −$0.96M instead of −$29.0M; any de-SPAC with a
  fiscal-year change will do the same. (2) `sources.sec_facts("1838359")` **404s on an unpadded CIK**
  while `fts_count` refuses one — the two helpers disagree on input form. (3) **`deal_note` cannot tell a
  grant-for-equity from a financing** (Item 3.02 on the same 8-K is the tell it does not read). (4)
  `name_change_note` correctly fired; its 60% precision held here (a real de-SPAC). (5) Weighted-average
  share counts tagged in thousands as units in Rigetti's 2023 10-Qs — a 1,000x per-share hazard for any
  screen reading them.

## REGISTER
- Verdict: [ ] IN [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [x] **UNKNOWABLE (about my evidence)** — at Q1.
- **One line:** a superconducting quantum-computing laboratory that recovers ~12% of its costs from
  research customers and funds the rest by selling stock (3.0x the shares since 2022); the business it
  declares it will be depends on an event its own filings say *"may never occur"*, and no document can
  resolve that until the record exists — closed without prejudice at Q1, with Q2 and Q4 each recorded
  OUT beneath it; price $15.27 against ~$1.59 a share of cash.
- **If UNKNOWABLE:** what cannot be known is **whether Rigetti's roadmap produces a product that
  non-research customers pay for at a scale that bears on its costs, before its cash and its
  shareholders' patience run out** — the four named records in Q1 are the evidence that would decide it,
  and none of them yet exists at Rigetti.
