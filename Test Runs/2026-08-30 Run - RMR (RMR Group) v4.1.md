# Company Run — The RMR Group Inc. (Nasdaq: RMR) — 2026-08-30
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`. Evidence: `Test Runs/_research 2026-08-26/`
(`RMR_*` and `RMRpeer_*` files).

**Position context: NONE HELD. Fresh entry run.** Surfaced by the sourcing sweep (cap
~$292M, 6.02% statute yield) and the dividend lens (9.24% dividend yield). **Bias declared
per operator rule 9:** roughly $2,750 of taxable capital seeks a dividend payer that
compounds, so the analyst's incentive is to clear this name. The iron prescription
**[E4-51]** is applied and disconfirming evidence is hunted hardest **[E4-26]**. **A "no"
verdict is a fully successful run.**

---

# ⚠ CAP VERIFICATION FIRST — THE SWEEP'S CAP IS WRONG BY 2.14×, AND THE YIELD SURVIVED BY ACCIDENT

**The sweep's cap of ~$292M is an artifact.** It used **15,000,000 shares**, which is
exactly the Class B-2 count, and the FY2025 10-K describes that class in one sentence:
Class B-2 shares "**are paired with the 15,000,000 RMR LLC Class A Units and have no
independent economic interest in RMR Inc.**" The sweep therefore priced the company on the
one class that, standing alone, is worth nothing.

**The true economic count, from the filed cover pages (live EDGAR, pulled 2026-08-31):**

| class | count | source | economic claim |
|---|---|---|---|
| Class A common | **16,080,226** | Q3-FY2026 10-Q cover, as of **2026-07-31** | 1 RMR LLC unit each |
| Class B-1 common | **1,000,000** | same cover | 1 RMR LLC unit each; 10 votes |
| Class B-2 common | **15,000,000** | same cover | paired 1:1 with ABP Trust's redeemable RMR LLC Class A Units; 10 votes |
| **total economic units** | **32,080,226** | | = 100% of RMR LLC |

Note 1 of the same 10-Q closes it: RMR Inc. owns 16,092,402 + 1,000,000 RMR LLC units =
**53.3% of the economic interest of RMR LLC**; ABP Trust's subsidiary owns 15,000,000
redeemable Class A Units = **46.7%**. 17.09M ÷ 0.533 = 32.09M units. The two counts agree.

- **TRUE ECONOMIC MARKET CAP = 32,080,226 × $19.46 = $624.3M** (close 2026-08-28, Nasdaq,
  Yahoo aggregator, live quote only, flagged).
- Class A + B-1 only: 17,080,226 × $19.46 = **$332.4M**.
- Sweep's figure: 15,000,000 × $19.46 = **$291.9M**. **The true cap is 2.14× the sweep's.**
- **Filed corroboration:** RMR's own Q3-FY2026 supplemental (8-K 2026-08-05, Ex. 99.2, p.12)
  computes Distributable Earnings per share on "**32,093** shares outstanding as of the
  record date." The company uses the same denominator this run uses.

**But the 6.02% "statute yield" was NOT materially wrong, and saying otherwise would be the
easy, wrong answer.** The sweep's numerator was `us-gaap:NetIncomeLoss` = **$17.596M**,
which is net income attributable to RMR **Inc. only** (45.5% of the $38.679M consolidated
figure), set against a cap that was 46.8% of the true cap. **Two errors of nearly equal
size, in opposite directions.**

| basis | numerator | denominator | yield |
|---|---|---|---|
| **the sweep, as run** | parent-only NI $17.596M | $291.9M (Class B-2 count) | **6.03%** |
| like-for-like, parent | parent-only NI $17.596M | $332.4M (Class A + B-1) | **5.29%** |
| like-for-like, consolidated | consolidated NI $38.679M | $624.3M (all units) | **6.20%** |

**So: the CAP is an artifact; the YIELD is not.** And the honest correction runs *toward*
the name, not away from it: on owner earnings rather than net income, the yield on the true
cap is **8.6% to 10.9%** (Q4 below), because RMR's reported net income is depressed by
$9.4M/yr of non-cash amortization charged against revenue and by real-estate depreciation.
**RMR is cheaper on cash earnings than the sweep said, not dearer.** Recording that is
[E4-26]'s requirement, not a concession.

**The dividend lens's 9.24% is also real, with one material qualification.** $0.45/quarter
= $1.80/yr on $19.46 = **9.25%**, paid on Class A and Class B-1. But RMR **LLC** distributes
only **$1.28 per unit per year** to all 32.08M units; RMR **Inc.** tops its own shareholders
up to $1.80 out of a corporate cash balance. The FY2025 10-K states it plainly: "**The
remainder of the dividends noted above were funded with cash accumulated at RMR Inc.**"
FY2025: dividends $30,347k against $21,580k received from RMR LLC, a **$8,767k gap**. That
balance was $19,478k at 2025-09-30 and $15,386k at 2026-06-30, and the company's own
supplemental says it supports "dividends at current levels for **more than two years**."
**Roughly 29% of the 9.25% yield has a disclosed and dated runway.** See Q4.

*(All dollar figures below in $ thousands unless marked, matching the filings.)*

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **USD 30-year: 5.19% · observation date 2026-08-27 · FRED DGS30** via `fredgraph.csv`
  direct (operator-directed route), series file
  `Test Runs/_research 2026-08-26/DGS30_2026-08-31.csv`, pulled 2026-08-31. *Honest note:
  four re-fetch attempts during this run failed (fredgraph.csv timed out or closed the
  connection; transient outage, not a blocked rung); the same-day cached pull of the same
  series by the same route was used, last observation 2026-08-27. FRED's 1-2 day lag noted,
  immaterial.* Revenues are 100% domestic: "During the three and nine months ended June 30,
  2026 and 2025, **all of our income before taxes was derived solely from domestic
  operations**" (Q3-FY2026 10-Q, Note 9). No FX.
- Price: **$19.46, Nasdaq close 2026-08-28** (Yahoo, aggregator, live quote only, flagged).
- **Market cap: $624.3M** (verification above). Book: total equity $398,562 at 2026-06-30
  → **$12.42 per economic unit; price/book 1.57×**. Total shareholders' equity attributable
  to RMR Inc. $224,186 on 17.09M shares = $13.12/share; price/book 1.48× on that basis.

**The filing was read — not tagged data [E3-27]:**
1. **FY2025 Form 10-K, filed 2025-11-12, accession 0001644378-25-000043** (year ended
   2025-09-30; auditor **Deloitte & Touche LLP**, PCAOB ID 34; unqualified opinion; ICFR
   attestation) — [x] MD&A [x] cash-flow statement incl. detail lines [x] footnotes
   (Item 1 Business incl. the full management-agreement terms; Item 1A risk factors incl.
   conflicts, controlled-company and dual-class; Item 3; Item 5; Note 1 Organization,
   Note 2 significant accounting policies/revenue, Note 11 Shareholders' Equity incl. the
   dividend and RMR LLC distribution tables).
2. **Q3-FY2026 Form 10-Q, filed 2026-08-05, accession 0001644378-26-000020** (period
   2026-06-30) — full read: Note 3 Related Person Transactions, Note 4 Revenue Recognition,
   Note 6 Indebtedness, Note 8 Investments, Note 9 Income Taxes, Note 13, Note 14, MD&A.
3. Q2-FY2026 10-Q, accession 0001644378-26-000014; Q1-FY2026 10-Q, accession
   0001644378-26-000007 — series and incentive-fee timing only.
4. FY2024 10-K, accession 0001644378-24-000042; FY2022 10-K, accession 0001644378-22-000047;
   FY2021 10-K, accession 0001644378-21-000041; FY2023 10-K, accession 0001644378-23-000051
   — for the FY2021-FY2023 cash-flow and AUM series.
5. **DEF 14A filed 2026-01-15, accession 0001104659-26-004085** — Compensation Discussion
   and Analysis, Summary Compensation Table, Pay Versus Performance, Annex A Certain
   Related Person Transactions, audit fees.
6. Earnings 8-Ks: **2026-08-05, accession 0001644378-26-000019** (Ex. 99.1 release and
   Ex. 99.2 supplemental) and **2025-11-12, accession 0001644378-25-000042**.
7. Competitor filings: see the row at Q2 (accessions listed there).

- **Figure cross-checked against the filed statement:** FY2025 net cash provided by
  operating activities. Filed consolidated statement of cash flows reads "**Net cash
  provided by operating activities 75,746**"; Item 1 Business prose reads "net cash from
  operating activities of **$75.7 million**"; SEC XBRL companyfacts (CIK 0001644378)
  `NetCashProvidedByUsedInOperatingActivities` FY2025 = **75,746,000**. Three-way match.
  **Second check:** 9M-FY2026 OCF "**82,937**" in the 10-Q statement, against the MD&A's
  "The **$22,819** increase in net cash flows provided by operating activities for the nine
  months ended June 30, 2026" on a prior-period base of 60,118. 60,118 + 22,819 = 82,937.
  Match.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

- **Unit economics in my own words, without management's language.** RMR is a fee pipe
  bolted onto four listed real-estate vehicles and a tail of private ones. It employs
  roughly 800 people; those people are also the entire officer corps of every client, and
  the clients have no employees at all. Three fee lines, all formula-driven:
  1. **Base business management fee** on each listed REIT: the **lesser** of a cost-based
     tier (0.5% of transferred assets + 0.7% of average invested capital to $250,000 +
     0.5% above) and a **market-capitalization** tier (0.7% to $250,000 + 0.5% above).
     "Average market capitalization" is defined in the agreements as common equity **plus
     preferred liquidation preference plus the principal amount of consolidated
     indebtedness** — that is, enterprise value. As of 2026-06-30 the market-cap measure
     was the binding one for DHC, ILPT and SVC. FY2025: **$80,030** from the four REITs.
  2. **Property management (3.0% of gross rents collected) and construction supervision
     (5.0% of construction cost, 3% on some projects).** FY2025: $36,748 + $6,991.
  3. **Incentive business management fee**: 12.0% of the client's equity market cap
     multiplied by its three-year total-return outperformance of a named MSCI sub-index,
     capped at the value of 1.5% of its shares, nil if total return is negative or if the
     shortfall to the index exceeds 500bp/yr. **This line is either zero or enormous.**
  Plus fees from Sonesta (0.6% of revenues), RMR Residential (2.5-3.5% of collected rents,
  5% construction), other private vehicles, and Tremont's 1.5%-of-equity advisory fee from
  SEVN. Costs are people: FY2025 compensation and benefits $161,728 + equity comp $9,664 +
  separation $7,078 + G&A $42,497.
- **The reported "Total revenues" of $700,284 means nothing** and the run refuses to use
  it. $506,861 of it (72%) is **reimbursable costs** grossed up on both sides of the income
  statement. The number that matters is **total management, incentive and advisory services
  revenue: $182,703 (FY2025)**.
- **The scarce input this business controls:** not skill, and not the properties. It is
  **the contract, plus the fact that the person who signs on the client's side and the
  person who signs on the manager's side are the same person.** Adam Portnoy is Chair and
  a managing trustee of every Managed Equity REIT and of SEVN, sole director of AlerisLife,
  a director and controlling shareholder of Sonesta, and RMR's own CEO, Chair, 50.7%
  economic owner and holder of **91.0% of RMR's voting power** (10-K risk factors; DEF 14A
  Annex A). That is the scarce input, stated plainly.
- **Ten years:** the fee formulas will look the same. **The client list will not** — TA
  left in 2023, AlerisLife wound down in 2026, OPI went through Chapter 11 in 2025-26 and
  emerged with a five-year agreement in place of a twenty-year one. That is a Q2 problem,
  not a Q1 one.
- **VERDICT: [x] IN.** The economics are legible from the filings, client by client and fee
  line by fee line, in a document that discloses its conflicts at length. Nothing here is
  too hard to understand. *(The reimbursable gross-up is a presentational trap, not an
  intelligibility failure; it is disclosed and reversible in one subtraction.)*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- **Needed or desired [~]** — needed, plainly: the clients have no employees. **Desired** is
  the word that fails; see the OPI test below.
- **No close substitute [ ] — FAILS.** The substitute is **internalization**, and the
  industry exercises it routinely.
- **Not price-regulated [x]** — correct.

### The claimed moat, stated at its strongest, then tested

The 10-K's own claim: "Our agreements with the Managed Equity REITs are **20 year term
evergreen contracts with significant termination fees payable in certain circumstances**."
The mechanics are genuinely formidable: the agreements "**automatically extend on December
31st of each year and have terms thereafter that end on the 20th anniversary of the date of
each extension**" — a term that never runs down — and termination for convenience obliges
the REIT to pay "**a termination fee equal to the sum of the present values of the monthly
future fees … for the remaining term**." On SVC's ~$40M/yr of fees that is a nine-figure
number against a client whose entire equity is worth about $1.0 billion. **[E2-45]'s
attacker's test:** with ample capital and skilled personnel I could not take DHC, ILPT or
SVC away from RMR. The lock is real and it is not attackable from outside.

**Four tests it fails anyway, all on the subject's own filings.**

**1. The contract is written to die with one man [E4-23].** "A Managed Equity REIT is **not
required to pay any termination fee** if it terminates its business or property management
agreements for cause, or **as a result of a manager change of control**." The termination
fee — the entire moat — evaporates on a change of control of RMR LLC. Buffett wrote
[E4-23] inside the durability criterion: "**if a business requires a superstar to produce
great results, the business itself cannot be deemed great … The partnership's moat will go
when the surgeon goes.**" Here the moat does not merely go when the surgeon goes; **the
contract says so in writing.** This is recorded at Q2 as a moat defect, per the guardrail,
and not at Q3 as a compliment to the person.

**2. The one arm's-length repricing in the record cut the term by 75%.** OPI filed Chapter
11 on 2025-10-30 and emerged 2026-06-17. At that moment OPI's creditors, not a board
chaired by RMR's owner, held the pen. The new agreements: "**each with initial terms of
five years and terminable without payment of a termination fee after the first two
years**," with any pre-two-year fee capped at "$28 million less the business management fee
actually paid." **The twenty-year evergreen with a PV-of-twenty-years termination fee was
replaced, at the only genuinely negotiated repricing on the record, with a two-year tail.**
RMR wrote off **$19,066** of the capitalised OPI relationship in the same quarter. That is
the market's price for this contract when a counterparty can actually negotiate, and it is
the single most decisive fact in this run.

**3. The base is depleting and the manager is buying replacements with cash [E4-04].**
[E4-04] excludes the moat whose **basis must be periodically replaced**. RMR's basis is
fee-earning AUM, and it is shrinking:

| as of | AUM | source |
|---|---|---|
| 2021-09-30 | **$32.7B** | FY2021 10-K |
| 2022-09-30 | $37.3B | FY2022 10-K |
| 2023-09-30 | $35.9B | FY2023 10-K |
| 2024-09-30 | $40.9B *(includes ~$5.5B bought with the MPC acquisition)* | FY2024 10-K |
| 2025-09-30 | $39.0B | FY2025 10-K |
| 2026-06-30 | **$37.5B** | Q3-FY2026 supplemental |

Ex the $5.5B bought for cash, organic AUM in 2024 was roughly $35.4B against $37.3B in
2022. **Properties managed [E4-55], the physical series:** "more than 2,100" (FY2021) →
"2,100" (FY2022) → "over 2,000" (FY2024) → "**approximately 1,900**" (FY2025). Headcount:
~600 (FY2021 and FY2022) → "over 1,000" (FY2024, post-MPC) → "nearly 900" (FY2025) → "over
800" (2026-08-05 release). **Fee revenue: $199,980 (FY2022) → $182,703 (FY2025), and
$190,882 in FY2023 once the one-time TA termination fee is stripped.** The MPC acquisition
cost **$78,771 net of cash** plus a $14,547 earnout and contributed $17,524 of FY2025 fees;
without it, organic fee revenue is roughly $165M against FY2022's $200M. **The spending
buys a replacement basis, not a defence of the same one.** That is Mitsui's Rhodes Ridge,
not Coca-Cola's advertising.

**4. The two-characteristic test [E2-44]: 0 of 2.**
- *Raise prices when demand is flat?* **No, and structurally cannot.** The rate is fixed by
  contract and the base falls automatically with the clients' enterprise values. The 10-K:
  base business management revenue fell $4,152 in FY2025 "**due to declines in their
  respective enterprise values**." The one rate increase in the record (OPI's flat $14.0M
  against an $11,412 FY2025 base fee) was bought by surrendering fifteen years of term.
  **[E4-37]'s inverse metric is at its extreme: RMR cannot hold a prayer session about
  raising prices, because it has no price to raise.**
- *Grow dollar volume with only minor additional capital?* **No, not any more.** In
  September 2021 RMR paid a **$7.00/share special dividend ($219,851)** out of a
  debt-free balance sheet holding $341,612 in money market funds. Since then: MPC
  $78,771 + $14,547 earnout; rental property acquisitions **$70,509 (FY2024) + $166,008
  (FY2025)**; loans $64,733 (since sold to SEVN); **$50,000 into SVC shares (April 2026)**;
  $24,824 into SEVN's rights offering; $17,576 into JVs; $93,200 + $46,500 of mortgage
  debt taken on and $25,000 drawn on the revolver. Cash: **$267,989 (FY2023) → $141,599 →
  $62,297 → $58,203 (2026-06-30)**. Property and equipment: nil → **$225,762**.
  Investments: $31,900 → **$136,200**. Debt: nil → **$163,807**. **Fee revenue is lower
  than it was before any of it.**

**Untapped pricing power [E3-33, E5-28]:** claiming that class claims near-monopoly. RMR
holds a contractual monopoly over four named vehicles and no pricing power over any of
them. Not the class.

**Direction [E4-32]:** negative on every filed axis — AUM, fee-earning AUM, fee revenue,
properties, headcount, client count, and contract term at the one client that was repriced.

### THE COMPETITOR ROW [E3-28] — same metric, same window, filing-sourced

Peer set chosen two ways: **RMR's own self-constructed peer group** (DEF 14A 2026, Pay
Versus Performance and CD&A: Brookfield Corporation, Cohen & Steers, Kennedy-Wilson,
RITHM Capital, and Bridge Investment Group until it stopped trading 2025-09-02), plus the
two largest listed alternative managers for the fee-rate and flows comparison, plus
**Ashford Inc.**, the closest governance analogue in the market.

| same metric, same window | **RMR FY2025** | BRDG FY2024 | CNS FY2025 | KW FY2025 | OWL FY2025 | ARES FY2025 | BAM FY2025 | AINC FY2024 |
|---|---|---|---|---|---|---|---|---|
| 10-K accession | 0001644378-25-000043 | 0001854401-25-000062 | 0001284812-26-000011 | 0001408100-26-000072 | 0001823945-26-000009 | 0001628280-26-011413 | 0001628280-26-013098 | 0001604738-25-000004 |
| management/fee revenue | **$182.7M** | $245.8M | $524.8M | $115.2M | $2,521.9M | $3,680.5M | $3,384M | $48.5M |
| AUM | **$39.0B** | $49.8B | $90.5B | $36.4B | $307.4B | $622.5B | n/d (uses FBC) | not disclosed |
| fee-earning AUM | $27.2B *(6/30/26)* | $22.3B | $90.5B | $11.0B | $187.7B | $384.9B | $602.7B | not disclosed |
| **fee rate on fee-earning AUM** *(computed)* | **67 bp** | 110 bp | 58 bp | 105 bp | 134 bp | 96 bp | 56 bp | n/a |
| net income, consolidated | $38.7M | $16.7M | $157.4M | $23.8M | $305.5M | $834.5M | $2,398M | **($4.0M)** |
| net income to parent | $17.6M | $8.0M | $153.2M | **($38.8M)** | $78.8M | $527.4M | $2,029M | ($3.3M) |
| total equity incl. NCI | $402.0M | $505.9M | $611.0M | $1,573.4M | $6,054.2M | $8,676.1M | $8,912M | **($346.5M)** |
| **ROE, parent** *(computed)* | **7.6%** | 10.1% | **28.5%** | (2.5)% | 3.6% | 13.5% | ~26.6% | n/m |
| fee-related / adj. EBITDA margin | ~41% *(company's own)* | 42.3% *(computed)* | 32.0% op *(disclosed)* | n/d | **58.3%** *(disclosed)* | 48.2% *(computed)* | 54.6% *(computed)* | n/d |
| **AUM direction, 3-4 yrs** *(computed CAGR)* | **+0.1%/yr, now falling** | +11.1%/yr | +4.0%/yr | +21.8%/yr | +36.2%/yr | +28.5%/yr | +14.8%/yr | n/a |
| permanent/perpetual capital | $18.3B of $27.2B FEAUM | n/d | 13.3% closed-end | n/d | **85% of mgmt fees** | **93% of mgmt fees** | 39.9% of FBC | n/d |

Closest structural comparator inside the set: **BAM's Real Estate segment** — fee-bearing
capital $101.7B / $93.6B / $93.4B over 2025/24/23 with fee revenue $1,090M / $968M / $920M
= **107bp, growing 4.3%/yr**, against RMR's 67bp on a shrinking base.

- **Peers named: 8 of the industry's real competitors, plus the 9 internalization
  precedents below.** Buffett says eight [E3-28]; eight were taken, four of them RMR's own
  choice of peer. **Ashford Inc. discloses no AUM and stopped filing** (Form 15-15D
  2025-01-17), so its fee rate is not computable — named as unavailable, per the rule.
  **No moat class is being claimed that requires the missing rows**; the verdict rests on
  the subject's own filings plus the row as filled, so PROVISIONAL does not arise.
- **The row's limit [E3-61] is stated:** structure is shown; conduct is not derivable from
  it. RMR could behave better or worse than the structure suggests, and the row cannot say.

### THE SUBSTITUTE, PRICED: nine REIT internalizations, 2015-2024

| REIT | manager | closed | consideration paid | source |
|---|---|---|---|---|
| Global Net Lease | AR Global | 2023-09-12 | 29,614,825 GNL shares (with Necessity Retail) | 8-K 2023-09-12 |
| BrightSpire (ex-CLNC) | Colony Capital | 2021-04-30 | **$102.3M cash termination fee** | 8-K 2021-05-03 |
| Preferred Apartment | internal mgmt cos. | 2020-02 | $154M + up to $25M earnout | 8-K 2020-02-03 |
| Steadfast Apartment | STAR Advisor | 2020-09-03 | $125.0M cash + Class B OP units | 8-K 2020-09-03 |
| National Healthcare Props (ex-HTI) | AR Global | 2024-09-30 | $75.0M cash | 8-K 2024-09-30 |
| Independence Realty | RAIT Financial | 2016-12 | $43.0M | 8-K 2016-12-22 |
| Bluerock Residential | Bluerock manager | 2017-11-06 | ~$41.2M | 8-K 2017-11-06 |
| Sila Realty (ex-CV MC REIT II) | CV Manager Sub | 2020-09-30 | $40.0M cash | 8-K 2020-09-30 |
| Braemar | **Ashford Inc.** | letter agmt 2025-08-26 | Sec. 12.5(b) calculation fixed; amount not in the 8-K body | 8-K 2025-08-26 |

**The cluster is $40M-$155M — a low single-digit multiple of annual fees, not the present
value of twenty years.** External management gets bought out routinely, and cheaply. RMR's
termination-fee provision has **never been tested**; the one time a counterparty could
actually negotiate, it was negotiated away.

### The calibration case: Ashford Inc.

The closest governance analogue in the market — an externally-managed manager of captive
REITs controlled by one family — carried an **even harsher** termination fee (1.1× the
greater of 12× trailing advisory net earnings or its own EV/EBITDA multiple applied to net
earnings, **plus a 40% tax gross-up**). It ended at **negative $346.5M of equity**,
delisted (Form 25-NSE 2024-07-29) and deregistered (Form 15-12G 2024-08-08). **A punitive
termination fee did not protect the manager's economics, because the fee base was the
clients and the clients failed.** That is the mechanism this run is testing at RMR, and the
market has already run the experiment once.

### The scoreboard the company keeps on itself

RMR's own Pay Versus Performance table (DEF 14A 2026), $100 invested 2020-09-30:

| FY | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|
| **RMR TSR** | $150.68 | $112.28 | $123.65 | $137.33 | **$93.92** |
| **RMR's own peer group TSR** | $162.57 | $125.39 | $125.50 | $203.42 | **$249.97** |

**Five years, a total return of minus 6%, against a peer group RMR selected itself
returning plus 150%.** [E3-59]'s first yardstick — how well they run the business, judged
against the hand they were dealt and against competitors' reports — reads badly, and it
reads badly on the company's own chosen comparison.

- **Class: [x] NONE as a franchise; the honest label is a CONTRACTUAL LOCK ON A DEPLETING
  BASE.** Direction: **narrowing**, on every filed axis.
- **VERDICT: [x] OUT.** Under [E3-03] a franchise's customers must think it has no close
  substitute; the substitute here is internalization, it is exercised across the industry
  at $40M-$155M a time, and the only party who ever negotiated at arm's length with RMR
  (OPI's creditors, in bankruptcy) shortened the twenty-year evergreen to five years
  terminable without penalty after two. The termination-fee moat is written to vanish on a
  change of control of the manager, which is [E4-23]'s defect stated in the contract
  itself. The basis must be replaced rather than defended, which is [E4-04]'s excluded
  class, and RMR has been replacing it with cash and mortgage debt while fee revenue fell
  from $200.0M to $182.7M. The two-characteristic test scores 0 of 2, and the company's own
  peer-group scoreboard shows minus 6% against plus 150% over five years. **The entry run
  stops here. [E5-13]: most names should end here, and that is the system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT — the hard sequence closes the
file for any BUY decision. No position exists, so no [E2-28] hold read is required.
Everything below is **FOR THE RECORD**, because the operator tasked this run with the Q3
agency read, the OPI-at-zero bottom boundary, the quantified deaths, and Q6 regardless.
**All valuation arithmetic below sits under operator rule 3's header. Nothing below is
entry language.**

---
## Q3 — FOR THE RECORD: ARE THEY HONEST, AND ARE THEY RATIONAL?
*Standard applied: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Q2 OUT stands regardless;
Q3 can stop a run, never start one.*

**STEP 1 — THE WEIGHT CASE.** *How much damage can this manager do before I can react?*
- [x] **Daily execution HIGH [E3-38].** RMR's own employees are the entire officer corps of
  every client. The fee base is the clients' enterprise value, which has to be defended
  every day at roughly 1,900 properties, and the incentive fee turns on three-year relative
  total shareholder return. OPI proved the consequence: a client that fails takes the
  contract with it. This is the retailer, not the network TV station.
- [ ] **Control [E1-16]** — not applicable; a minority holder can exit. Recorded for the
  record: the inverse asymmetry is extreme. Adam Portnoy holds **91.0% of the voting power**
  and RMR is a Nasdaq "**controlled company**" entitled to skip the majority-independent-board
  and independent-committee requirements (currently not availed of, per the 10-K).
- [ ] **Leverage [E3-29]** — not at RMR: debt $163,807 against $398,562 of equity, of which
  $141,493 is interest-only property mortgage. LOW. **But note the transmission:** the base
  fee is levied on the clients' **debt-inclusive** enterprise value, so client leverage
  magnifies RMR's revenue in both directions.
- **One determinant high → Q3 is a BINARY GATE and no price compensates [E3-38, E5-35].**
  **And [E2-50] scopes the whole question:** "*Where 'earnings' can be created by the
  stroke of a pen, the dishonest will gather.*" RMR's revenue is created by contracts
  between entities whose boards are chaired by the same man who owns the manager. **This is
  the sector where the conduct record, not the ratio, carries the Q3 weight.** It is
  [E3-57]'s agency structure inverted: the manager *is* the counterparty.

**Honesty — the binary [E5-16]. No integrity disqualifier found; written as the absence of
found disqualifiers, never as a clearance [E5-17].** The sweep, named: Item 3 Legal
Proceedings states "*we are currently not a party to any litigation which we expect to have
a material adverse effect*"; no restatement; no error-correction or clawback check-boxes
ticked on the 10-K cover; unqualified Deloitte opinions with ICFR attestation; audit fees
$878,620 against $135,424 of all other fees, a clean ratio. **And the disclosure conduct is
the opposite of concealment:** the conflicts occupy pages of Item 1A and the whole of DEF
14A Annex A, naming every overlapping directorship, every cross-holding, the tax receivable
agreement, the related-party leases, and the fact that agreements with related parties "**may
not be on terms as favorable to us as they would have been if they had been negotiated among
unrelated parties**." [E2-68]'s test — conduct where the informed party holds the advantage
— is passed on disclosure. Worded per the absence-claim rule: no instance found, not "none
exists."

**STEP 2 — THE FLAGS [E4-22, E4-29, E5-15, E4-30, E2-49, E2-52, E2-51].**

- [x] **Metric-switching [E2-49] — FIRED, and it is the sharpest finding in the file.**
  "Effective January 1, 2026, RMR LLC and SVC amended their business management agreement
  to **replace the benchmark index used in the calculation of incentive business management
  fees** … the MSCI U.S. REIT **Diversified** Index will be used … for periods ending prior
  to January 1, 2026, the MSCI U.S. REIT/**Hotel & Resort** REIT Index will continue to be
  used." [E2-49] verbatim: "*Yardsticks seldom are discarded while yielding favorable
  readings. But when results deteriorate, most managers favor disposition of the yardstick
  rather than disposition of the manager*" — the remedy demanded is "*pre-set, long-lived
  and small bullseyes*." **A benchmark that the beneficiary of the fee can amend by
  agreement with a board he chairs is not a pre-set bullseye.** *Stated fairly [E4-51]: SVC
  has sold roughly $1 billion of hotels and is repositioning toward net-lease retail, so a
  diversified index is arguably the more apt comparison; and the amendment is prospective
  only, which is the honest form, and it is disclosed in both the proxy and the 10-Q. What
  the filings do not contain is any stated reason.*
- [x] **Adjusted-earnings promotion [E4-29] — FIRED.** Three non-GAAP measures are
  headlined: Adjusted Net Income, Adjusted EBITDA, and Distributable Earnings. Q3-FY2026:
  GAAP net income attributable to RMR Inc. **$0.18/share**, Adjusted Net Income
  **$0.15/share**, **Distributable Earnings $0.48/share** — a 2.7× uplift over GAAP, and it
  is the $0.48 that sits on the page headed "**Well-Covered Dividend**" beside the $0.45
  dividend. The two per-share figures use different denominators in the same document
  (16,791 weighted average shares for GAAP, 32,093 for Distributable Earnings). **[E4-29]
  and [E5-41] apply directly:** depreciation and the $19,066 OPI impairment are real costs
  already paid, and the adjusted measures delete them. *Fairly stated: the Distributable
  Earnings arithmetic is internally consistent at the whole-company level ($15,401 of DE
  against $12,492 of total distributions), and the same page discloses in its own footnote
  that $0.13 of the $0.45 comes from RMR Inc.'s cash balance. The disclosure passes [E2-26];
  the headline does not.*
- [x] **Trumpeted projections [E4-22] — FIRED, with the [E3-48] record run.** The CEO, in
  the 2026-08-05 release: "*the Managed Equity REITs are collectively **on pace to generate
  over $40 million of incentive fees** for RMR this calendar year*." **The record of the
  people who made the projection:** the FY2025 10-K's own risk factor states that in FY2019
  incentive fees were **39.9% of total management and advisory services revenues**, and
  "**through fiscal 2025 we have not subsequently earned any incentive business management
  fees from the Managed Equity REITs**." **Six consecutive years of zero, then $23,584 in
  the December 2025 quarter.** The forecast is, in substance, a forecast of four REIT share
  prices over the remaining four months of a calendar year. [E5-30]'s ratchet is noted; a
  single instance is not yet a guidance culture, and RMR issues no formal earnings guidance.
- [x] **Restricted earnings / the dividend's funding [E2-60, and the spirit of E2-52] —
  FIRED.** RMR LLC distributes **$1.28 per unit per year**; RMR Inc. pays **$1.80 per
  share**; the FY2025 gap of **$8,767** was "funded with cash accumulated at RMR Inc."
  (10-K Note 11, verbatim). RMR Inc.'s cash: $19,478 → **$15,386** over nine months. The
  company's own footnote: that balance "provides ample capacity … to continue dividends at
  current levels **for more than two years**." Meanwhile consolidated distributions ran
  **$49,547 (FY2025 common) + $11,841 (tax distributions to ABP)**, or roughly 90-107% of
  owner earnings, while cash fell from $267,989 to $58,203 and $163,807 of debt appeared.
  [E2-60]: maintenance has a third dimension, **financial strength**, and "*a company that
  consistently distributes restricted earnings is destined for oblivion*." The payout is not
  reckless and it is fully disclosed; it is nonetheless being maintained while the balance
  sheet that supported it is spent.
- [ ] **Serial share issuance [E5-15] — NOT fired, the reverse.** Class A: 15,846,025
  (2024-09-30) → 16,063,495 (2025-09-30) → 16,080,226 (2026-07-31). About **1.4%/yr**, all
  employee and director awards, with 53,201 shares withheld and repurchased in FY2025 for
  tax. **No capital has been raised from shareholders since the 2015 IPO.**
- [ ] **Filed-figure tells [E4-30] — NOT fired.** Cash taxes ÷ pre-tax income: 10.7%
  (FY2021) · 10.5% (FY2022) · 14.2% (FY2023) · 14.2% (FY2024) · 12.4% (FY2025). Stable, no
  downward drift; the low level is structural (46.8% of RMR LLC's income passes through to
  ABP Trust untaxed at the entity). Reported growth is visibly lumpy (net income $127,771 →
  $53,129 → $38,679), not unnaturally smooth.
- [ ] **Unintelligible footnotes — NOT fired.** The Up-C structure is complex; the notes
  explaining it are not. Note 1, Note 3 and Note 11 lay out the unit counts, the economic
  percentages, the tax receivable agreement and the distribution mechanics in plain
  arithmetic that this run was able to reproduce.
- **Convergence [E4-52] — the finding.** The amended SVC benchmark, the Distributable
  Earnings headline attached to the dividend, and the $40M incentive-fee projection all
  push in one direction: **present the fee stream as larger and safer than the GAAP
  statements show.** They are not a sum of prompts; they are one system, and it sits exactly
  where a binary-gate Q3 looks.

**STEP 3 — THE PRIMARY TEST [E2-01], scoped by [E2-43, E2-47].** Balance sheet first
[E5-27]. Total equity: $540,902 (FY2020) → **$347,715 (FY2021, after the $219,851 special
dividend)** → $369,739 → $423,663 → $419,417 → **$402,013 (FY2025)** → $398,562 (2026-06-30).
Debt: nil throughout FY2020-FY2023, then $92,764 (FY2024), $180,754 (FY2025), $163,807 now.
Goodwill $71,761 and intangibles $20,329 arrived with MPC, so [E2-43]'s **unleveraged net
tangible** denominator is roughly $306M today, with the goodwill wedge reported separately
rather than hidden.

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| net income, consolidated | 81,013 | 77,468 | 127,771 | 53,129 | 38,679 |
| return on average **total** equity *(computed)* | 22.9% | 21.6% | 32.2% | 12.6% | **9.4%** |
| return on average total equity, **ex the $45,282 TA termination fee** *(computed)* | 22.9% | 21.6% | ~23.7% | 12.6% | **9.4%** |
| fee revenue | 175,678 | 199,980 | 236,164 | 193,920 | 182,703 |

**The trend is the finding, and it is the [E3-38]/[E2-01] pattern reversed:** a business
that earned 22-32% on equity with **no debt and no fixed assets** now earns 9.4% on an
equity base swollen by goodwill, real estate and investments. **The deterioration is not
operating; it is allocation.** The cash was there and it was spent. And the primary test
must be read alongside [E2-73]: judged on the underlying assets the *manager* actually has
to work with, the fee business itself still earns extraordinarily — the 9.4% is what
happens after $410M of principal investments were bolted onto it.

**The half-owner test [E2-26]:** **passes, and passes well.** The FY2025 10-K discloses fee
revenue client by client and fee line by fee line; the proxy's Annex A names every conflict;
Note 11 publishes the RMR LLC distribution table that lets an outsider compute the dividend
funding gap; the supplemental publishes the funding gap itself. **A reader who reads gets
told.** *(The one thing an outsider would want and does not get: a stated reason for the SVC
benchmark change, and any quantification of what it is worth.)*

**Institutional imperative [E2-30], scored — "*institutional dynamics, not venality or
stupidity*":**
- (1) **Resists change** — *partially fired.* The 20-year evergreen architecture is
  unchanged since 2015 and is defended rather than re-examined, even as the vehicles inside
  it shrink.
- (2) **Acquisitions/projects soak up available funds** — **FIRED, hard.** $267,989 of cash
  at FY2023 became MPC, four wholly-owned properties, three JV stakes, $50,000 of SVC
  shares, a $24,824 SEVN backstop, and $163,807 of debt. Fee revenue fell. **[E3-40]'s loss
  of focus is the exact diagnosis:** "*gets sidetracked and neglects its wonderful base
  business while purchasing other businesses that are so-so or worse.*"
- (3) **Staff studies for the leader's craving** — not observable from the filings.
- (4) **Peer behaviour mindlessly imitated** — *fired, mildly.* The rebranding to "a leading
  U.S. alternative asset management company," the promote/carried-interest programs, the
  fund-seeding and the balance-sheet co-investment are the Blackstone/Bridge playbook
  adopted by a company whose fee rate (67bp) and AUM growth (+0.1%/yr) do not resemble those
  managers'.

**Capital allocation — the buyback conditions [E5-08, E4-31, E5-31, E2-51]:**
- **(1) Ample funds for operations and liquidity? No, not now.** $58,203 of cash, $75,000 of
  undrawn revolver, a dividend costing $49,968/yr at the LLC and RMR Inc. levels combined,
  and an RMR Inc. cash balance with a stated two-year runway.
- **(2) Repurchases at a material discount to conservatively-calculated IV?** **There is no
  repurchase program at all.** Item 5's table shows "N/A" under both program columns; the
  only purchases in FY2025 were 53,201 shares of tax withholding at an average $16.98. On
  this run's numbers the shares at $19.46 offer a bottom-boundary owner-earnings yield of
  8.6-9.2%. **[E2-51]:** "*A manager who consistently turns his back on repurchases, when
  these clearly are in the interests of owners, reveals more than he knows of his
  motivations.*" *Stated with the humility clause [E4-13]: condition (1) genuinely fails
  today, which is a complete and legitimate answer, and management knows the liquidity
  position better than this run does. The flag binds position size only, and no position is
  held.*
- **What was bought instead, and this is the [E5-31] comparison that matters:** $50,000 of
  **SVC** shares in SVC's own underwritten offering at $1.20, and $24,824 into **SEVN's**
  rights offering (of which $17,436 was a backstop of shares nobody else wanted), taking
  Tremont to **20.2% of SEVN**. Both are equity in vehicles RMR manages. **SEVN's rights
  offering raised roughly $65,200 of new equity, and Tremont's advisory fee is 1.5% of
  SEVN's equity: RMR funded 38% of a capital raise that enlarged its own fee base by roughly
  $978 a year.** Nothing here is concealed and nothing here is alleged to be improper. It
  is simply the structure working as designed: **the manager's principal investments and the
  manager's fee base point the same way, and no disinterested party stands between them.**

**Compensation and the vote.** Adam Portnoy's FY2025 Summary Compensation Table total is
**$4,817,047**, against **$17,596** of net income attributable to RMR Inc. — **27% of the
public company's attributable earnings for one officer.** The three highest-paid officers
total $13,651,839, or **78%** of that figure. *(The stock-award component includes shares
granted by the managed REITs, so the burden is shared with the clients' shareholders; the
proxy says so.)* Ms. Clark's retirement agreement guaranteed a FY2025 cash bonus of "**the
greater of the cash bonus paid to Mr. Portnoy … and $2,880,000**" plus a recommendation to
accelerate her unvested shares. The proxy states: "**We do not use any financial performance
measures to link compensation actually paid to our NEOs by us to the Company's
performance.**" Say-on-pay approval was "**approximately 99%**" — **a figure that carries
almost no information, because the controlling shareholder holds 91.0% of the votes.**

**THE GUARDRAIL — checked before the verdict:**
- [x] Nothing in this Q3 is being used to **promote** the name. Q2 OUT stands; a capable
  operator cannot repair a depleting fee base **[E2-37, E2-38, E3-39]**.
- [x] **Key-person dependence is recorded at Q2 as a moat defect [E4-23]**, where the
  contracts themselves put it, and not here as a compliment.
- [x] Is the franchise intact with a localised excisable cancer, or **is the manager the
  plan [E2-35, E2-36]**? **The manager is the plan**, and more than that: the manager is
  simultaneously the counterparty, the clients' chairman, the fee-setter, the benchmark
  amender and the 91% voter. That is [E2-36]'s unbuyable class, not GEICO's.

- **Q3 FOR-THE-RECORD READ: no honesty disqualifier found, and the disclosure record is
  genuinely good. The gate would still not clear.** In a business where earnings are
  created by the stroke of a pen between related parties **[E2-50]**, with daily execution
  high **[E3-38]**, the amended incentive benchmark **[E2-49]**, the adjusted-measure
  headline attached to a dividend the company itself discloses is partly funded from a
  depleting balance **[E4-29, E2-60]**, the incentive-fee projection against a six-year
  record of zero **[E4-22, E3-48]**, and the conversion of a debt-free fee business into a
  levered principal investor while fee revenue fell **[E3-40, E2-30(2)]** converge
  **[E4-52]** exactly where a binary gate looks. Set against them, fairly: full and
  voluminous disclosure, a clean audit and litigation record, no share issuance, 50.7%
  owner-operator economics, and a fee formula that automatically *reduces* the manager's
  pay as the clients' values fall. *A pass here would be the absence of found
  disqualifiers, never a clearance **[E5-17]**; and IN never promotes.*

## Q4 — FOR THE RECORD: WILL IT SURVIVE?

### Owner earnings — **COMPUTATION — NOT A CLEARANCE** [E2-23]

Convention: multi-year mean of (OCF − SBC) − (c). Both windows shown **[E2-42, E4-25]**;
the spread carried, not resolved by preference.

**The SBC subtraction, corrected against the filing.** The income-statement line "Equity
based compensation $9,664" is **not** RMR's dilution. It is $2,782 of RMR's own 2016-Plan
awards plus **$6,882 of shares granted by the clients to RMR employees**, which appears
dollar-for-dollar as "Reimbursable equity based compensation" revenue. The cash-flow
statement's own add-back, "**Operating expenses paid in The RMR Group Inc. common shares**,"
is the honest measure: **$3,798 (FY2025)**. Cross-checked against [E3-70]'s market-value
standard: RMR awarded 272,872 Class A shares in FY2025 at a weighted-average award-date fair
value of $16.84 ($4,595 gross), with 53,201 withheld; net new shares issued were 217,470,
worth $3,662. The $3,798 add-back sits between the two. **Using the XBRL
`ShareBasedCompensation` tag of $9,664 would over-subtract by $5,866 and would be wrong.**

**The (c) judgment, disclosed [E2-23, E3-44, E2-41, E5-20].** This is **not** the
capital-intensive exception class at the manager level: the fee business consumes IT and
leasehold improvements and nothing else, and capex ran $1,142 / $1,121 / $3,983 / $3,865 /
$3,650 over FY2021-25 on fee revenue near $200M. But RMR now owns $225,762 of real estate
and $20,329 of MPC intangibles, so **D&A ($11,551 FY2025, $17,289 TTM) now runs well above
capex** and is the **conservative** end. **(c) is therefore taken as a band from actual
capex to D&A, D&A being the conservative end, and the band is disclosed as a guess, not
computed.** The working-capital increment is inside OCF by the convention; over FY2021-25
the five working-capital changes sum to **−$2,620**, essentially neutral, which is why the
multi-year mean is the right instrument here.

| FY | OCF | − SBC | = cash | (c)=capex | **OE @ capex** | (c)=D&A | **OE @ D&A** |
|---|---|---|---|---|---|---|---|
| 2021 | 71,794 | 4,122 | 67,672 | 1,142 | 66,530 | 973 | 66,699 |
| 2022 | 101,270 | 3,774 | 97,496 | 1,121 | 96,375 | 993 | 96,503 |
| 2023 | 109,215 | 3,608 | 105,607 | 3,983 | 101,624 | 1,102 | 104,505 |
| 2024 | 61,375 | 3,937 | 57,438 | 3,865 | 53,573 | 4,713 | 52,725 |
| 2025 | 75,746 | 3,798 | 71,948 | 3,650 | 68,298 | 11,551 | 60,397 |
| TTM to 2026-06-30 | 98,565 | 4,149 | 94,416 | 5,912 | 88,504 | 17,289 | 77,127 |

**Two distortions are named and removed [E4-41], because both are favourable exogenous
breaks and the corpus requires normalizing the mean DOWN:**
1. **FY2023 contains a $45,282 one-time termination fee** paid by TravelCenters of America
   when BP bought it. That is a **death benefit on a lost client**, not recurring income.
2. **The TTM contains $23,715 of incentive fees** for the calendar-2025 measurement period
   (DHC $17,905, ILPT $5,679, SEVN $131) — the first such fees in **six years**. Carried as
   optionality, refused as a base.

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E2-42]:**
- **Long window, 5-yr FY2021-25**, mean(OCF−SBC) $80,032 less $9,056/yr of TA fee = $70,976;
  mean capex $2,752, mean D&A $3,866 → **OE $67,109 to $68,224**.
- **Short window, 3-yr FY2023-25**, mean(OCF−SBC) $78,331 less $15,094/yr = $63,237; mean
  capex $3,833, mean D&A $5,789 → **OE $57,448 to $59,404**.
- **Spread, conservative end: the 3-year mean is 14.4% below the 5-year mean.**
- **Combined range (window spread × capex band): roughly $55M to $70M.**
- **Is the range too wide to conclude [E4-25]? No** — 55 to 70 is a 27% band, workable. But
  **the spread is itself a Q4 finding [E5-11]:** the distortion in the window is named
  (FY2022's $96.5M reflects a fee base near its peak with zero balance-sheet drag; FY2024's
  $52.7M reflects the trough plus the MPC integration), and **[E3-55] does not rescue it** —
  this is uncertainty about the *level* of a shrinking fee base, not the noise of a certain
  mechanism.
- **Bottom boundary as filed [E5-34]: OE ≈ $53M to $57M** (TTM ex-incentive at D&A, and the
  3-year mean at D&A). **Bottom-boundary yield 8.6% to 9.2% on the true $624.3M cap.**

### THE BOTTOM BOUNDARY WITH OPI-CLASS FEES AT ZERO — the arithmetic, shown

*OPI is the live test case: delisted to OTC 2025-10-06, Chapter 11 2025-10-30, emerged
2026-06-17 into a five-year agreement terminable without penalty after two, having failed
the performance measure for three consecutive calendar years (the 10-K: "OPI may have had a
right to terminate its management agreements with us after December 31, 2025 due to our
failure to satisfy the applicable measure for calendar year 2025").*

| step | | $000 |
|---|---|---|
| A | 3-yr mean (FY2023-25) OCF − SBC, ex the TA termination fee | **63,237** |
| B | less (c) at D&A, the conservative end of the capex band | (5,789) |
| **C** | **= bottom-boundary owner earnings as filed** | **57,448** → 9.20% on $624.3M |
| D | **less the entire OPI fee stream** (9M-FY2026 $17,380 × 4/3) | **(23,173)** |
| E1 | no cost relief, no tax relief (harshest) | **34,275** → **5.49%**, +0.30 pts over sovereign |
| E2 | tax relief only (RMR Inc.'s 53.3% share × ~18% effective rate) | **36,498** → **5.85%**, +0.66 pts |
| E3 | 50% cost drop-through as RMR sheds staff for OPI's 124 properties, plus tax relief | **46,973** → **7.52%**, +2.33 pts |

**And the harsher case the structure invites — OPI *and* DHC's non-incentive fees at zero**
(DHC ex-incentive run-rate $23,979): **OE $10,296 to $14,820, or 1.65% to 2.37%, which is
2.8 to 3.5 points BELOW the sovereign.**

**Read that table plainly.** OPI is 13.2% of FY2025 fee revenue. Removing one of four public
clients takes the bottom-boundary owner-earnings yield from 9.2% to between 5.5% and 7.5%,
which is to say from comfortably above the long bond to roughly level with it. **The
business has no cushion for a second client failure, and it has already had one.**

### Great, good, or gruesome? **[E4-20]**

**Two businesses inside one filer, and the answer differs.**
- **The fee business standing alone was GREAT**, in the corpus's exact sense: FY2022 owner
  earnings of $96,503 on essentially **zero net tangible capital**, no debt, and a savings
  account paying an extraordinarily high rate. That is why this name is worth reading at all.
- **The consolidated company as it now exists is GOOD at best, and drifting.** [E4-43] says
  the good class passes and there is nothing shabby about it — but the filed direction is
  the wrong one: return on average total equity has gone 22.9% → 21.6% → 32.2% → 12.6% →
  **9.4%**, below the ~12% [E5-40] calls "quite satisfactory," because roughly $410M of
  cash and new debt was moved out of a no-capital fee business into real estate,
  fund seeds and client equity that have not yet earned it back. **The migration is from
  great toward good, and it was chosen, not imposed.**

### Staying power — score all three **[E5-11]**

1. **A large and reliable stream of earnings — PARTIAL.** Contractual and formula-driven,
   which is real. But **68.0% of FY2025 management and advisory revenue came from four
   clients** whose combined equity market value is roughly $3.8 billion, one of which has
   just been through bankruptcy. Concentration is the defect, not volatility.
2. **Massive liquid assets — FAIL as the corpus means it, and deteriorating.** Cash
   **$58,203** (of which $15,386 sits at RMR Inc. and is earmarked for the dividend gap),
   plus $75,000 of undrawn revolver — which is [E5-39]'s **kindness of strangers**, not
   liquidity — plus $116,472 of listed client equity (SEVN $38,591, SVC $70,417, OPI
   $7,464) that cannot be sold quietly by a 20.2% holder who is also the manager. Against
   $267,989 of cash and zero debt three years ago.
3. **No significant near-term cash requirements — PARTIAL FAIL.** The revolver matures
   **2028-01-22** with $25,000 drawn; $141,493 of interest-only property mortgages sit
   behind interest-rate caps struck at 3.00% expiring August and October 2028; the tax
   receivable agreement liability is $18,478 with $2,552 current. **The binding near-term
   requirement is the dividend itself**: $49,968/yr all-in, with roughly $8,900/yr of it
   drawn from a $15,386 balance the company dates at "more than two years."
- **Leverage, named and quantified [E4-16, E3-29]** — *no ratio ceiling exists in this
  framework and none is applied*: total debt **$163,807** ($141,493 property mortgage,
  interest-only, capped; $25,000 revolver at SOFR + 225bp) against $398,562 of equity.
  **[E2-54]'s coverage test:** TTM interest paid ≈ $9,036 against pre-interest operating
  cash of roughly $107,600 net of $5,912 of capex — **coverage above 11×. Comfortably met.**
  This is not a leverage story.

### Name the specific ways THIS business dies **[E2-27, E3-24]** — exposure, not experience **[E4-40]**

1. **A second client failure cascades into the fee base (the OPI mechanism, repeated).**
   Quantified above: OPI at zero takes bottom-boundary OE from $57,448 to $34,275-$46,973
   and the yield to 5.5-7.5%; OPI and DHC together take it to $10,296-$14,820, below the
   sovereign. Exposure, not experience: SVC carries roughly $4.8 billion of debt against
   $1.0 billion of equity and raised $575 million of new equity this year at $1.20 a share.
   **Likelihood: a real possibility.** One of four has already happened.
2. **Manager change of control voids the moat with no fee (the key-person death).**
   Contractual and filed: no termination fee is payable "as a result of a manager change of
   control." Quantified: the four Managed Equity REITs are a **$124M/yr** fee run-rate and
   68% of fee revenue; on that event they become terminable at will. **Likelihood: a
   low-level possibility in any given year; approaching certain over a multi-decade holding
   period, which is the horizon this framework buys on.**
3. **Success at the client kills the fee (the alignment death, already running).** The base
   fee is the *lesser* of cost and enterprise value, and enterprise value **includes debt**.
   Every deleveraging and every asset sale RMR executes for a client shrinks RMR's own fee.
   Filed and quantified: SVC's fee-earning base fell $6,224,431 → $5,817,828 in twelve
   months (−6.5%) and SVC base business management fees fell $21,317 → $19,873 over the
   same nine months. **Likelihood: likely — it is happening, and it is what good
   stewardship of the clients requires.** *This is the cleanest statement of the agency
   structure in the whole file: doing right by the client's balance sheet reduces the
   manager's pay.*
4. **Internalization or non-renewal.** Nine confirmed precedents 2015-2024 at $40M-$155M,
   a low-single-digit multiple of annual fees. RMR's PV-of-twenty-years provision has never
   been tested; the one negotiated repricing produced a two-year tail.
   **Likelihood: a real possibility over a decade.**
5. **The dividend's funding gap closes (the death of the reason this name was screened).**
   $1.80 paid against $1.28 distributed by the LLC; the $8,767/yr difference draws a $15,386
   balance with a company-stated runway of "more than two years." Either RMR LLC raises its
   distribution (which requires the fee base to grow, which it is not doing) or the RMR Inc.
   dividend falls toward $1.28, which at $19.46 is a **6.6% yield**, not 9.25%.
   **Likelihood: likely within roughly three years absent a rise in LLC distributions.**
6. **Impairment of the remaining contract asset.** "Other assets, net" of **$61,857** is the
   unamortized 2015 consideration attached to the DHC, ILPT and SVC agreements, amortizing
   against revenue to June 2035. OPI's share of it was written off for $19,066 in one
   quarter when its agreement was replaced. **Likelihood: a real possibility, and it is
   non-cash — the cash version is death 1.**

- **Q4 FOR-THE-RECORD READ: it survives the current regime comfortably on the balance sheet
  — coverage above 11×, no maturity before 2028, modest and property-secured debt.** It
  does **not** meet [E2-55]'s standard of *certain under extraordinarily adverse
  conditions*: leg 2 of [E5-11] fails and is deteriorating, leg 3 fails at the dividend, and
  the OPI-at-zero arithmetic shows the earnings power has no cushion for a second client
  failure. **Were the gate live it would read IN on current-regime survival with legs 2 and
  3 failed and written.**

---
## Q5 — FOR THE RECORD — **COMPUTATION — NOT A CLEARANCE**
*(Q1-Q4 did not close IN; operator rule 3's header governs; no entry language.)*

**THE FLOOR [E4-28] — "that's the figure we quit on."**

**1. THE YIELD** — owner earnings ÷ **$624.3M** (the verified economic cap), against the
**5.19%** sovereign (FRED DGS30, 2026-08-27):

| OE basis | OE | yield | points over sovereign |
|---|---|---|---|
| TTM as reported *(refused as a base [E4-41]; shown)* | $77,127 | 12.35% | +7.16 |
| 5-yr mean FY2021-25, ex TA fee | $67,109-$68,224 | 10.75-10.93% | +5.56 to +5.74 |
| FY2025 alone | $60,397-$68,298 | 9.67-10.94% | +4.48 to +5.75 |
| 3-yr mean FY2023-25, ex TA fee | $57,448-$59,404 | 9.20-9.52% | +4.01 to +4.33 |
| **Bottom boundary as filed [E5-34]** | **$53,412-$57,448** | **8.56-9.20%** | **+3.37 to +4.01** |
| **Bottom boundary, OPI fees at ZERO** | **$34,275-$46,973** | **5.49-7.52%** | **+0.30 to +2.33** |
| Bottom boundary, OPI **and** DHC at zero | $10,296-$14,820 | 1.65-2.37% | −3.54 to −2.82 |

*A note on the tax character of these yields: RMR LLC is a partnership and 46.8% of its
income passes through untaxed at the entity level, so consolidated cash taxes ran only
12.4% of pre-tax income in FY2025. The owner-earnings yields above are therefore much
closer to pre-tax expectancy than a normal C-corp's would be, which is the comparison
[E4-28]'s floor asks for.*

**2. WHAT THE PRICE ALREADY ASSUMES.** $624.3M × the 10% floor = **$62,428 of owner
earnings required with no growth at all.** That sits **above** the 3-year mean ($57,448),
**above** the bottom boundary ($53,412-$57,448), and **1.7× to 1.8× the OPI-at-zero case**.
It is met only by the 5-year mean, which leans on FY2021 and FY2022 — the years before the
balance sheet was spent and before the client base began shrinking. **The price assumes the
fee base stops shrinking.** Against that, [E4-35]'s base rate and [E4-44]'s bound both
apply: the value of the asset cannot over the long term grow faster than its earnings, and
this asset's earnings are contractually a percentage of a declining number. **[E2-63]'s
ceiling, stated:** the upside is bounded by the clients' enterprise values, which RMR does
not control and is contractually paid to shrink.

**3. WHAT YOU ARE PAID.** **+3.4 to +4.0 points over the sovereign at the bottom boundary
as filed**, falling to **+0.3 to +2.3 points** if one of four public clients goes the way
OPI went. That is thin compensation for equity in a business whose Q2 verdict is OUT and
whose Q3 weight case is a binary gate.

**THE FLOOR VERDICT, stated plainly.** Honest pre-tax expectancy at $19.46 is **8.6% to
9.2%** at the bottom boundary, **9.2% to 10.9%** across the Q4 range, and **5.5% to 7.5%**
with OPI's fees at zero. **[E5-34] prices against the bottom boundary, and at the bottom
boundary the 10% floor does not clear.** It clears only on the five-year mean, which is a
window ending in a year the business no longer resembles.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01], for the record only:**
- At the 10% quit rate on the OPI-at-zero bottom boundary: **roughly $340M-$470M**, or
  **$11 to $15 a share**.
- At the 10% quit rate on the bottom boundary as filed: **roughly $530M-$575M**, or **$17 to
  $18 a share**.
- At the 10% quit rate on the 5-year mean ex the TA fee: **roughly $670M-$680M**, or **$21
  a share**.
- Treated as a perpetuity at the bare sovereign with no growth and no client loss:
  **roughly $1.0B-$1.3B**, or **$32 to $41 a share** — shown once and refused as a basis,
  because a fee stream contractually tied to a shrinking base is not a perpetuity.

**The $624.3M cap sits inside the range.** Bar chosen: **[x] the screamer test [E4-01]**,
never both bars. Three outcomes, and this is the middle one: **price inside the range → no
useful conclusion, move on.** That is a finished answer and the usual one.
**Windage count: one** — the (c) taken at the D&A end inside the bottom boundary. The
removal of the TA termination fee and the refusal of the incentive-fee spike are [E4-41]'s
required normalizations, and pricing against the bottom boundary is [E5-34]'s own move;
neither is windage. The OPI-at-zero table is shown as a **scenario**, separately, and is not
folded into the central case.

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists; these are pre-committed yardsticks for the WATCH LIST, set prior to
any act **[E1-02]**. **Alert thresholds LISTED ONLY** — no shared file edited.)*

**Q2 REOPEN CONDITIONS — the only route back to entry. BOTH required.**
1. **Evidence, not price.** Q2 failed on **class**, so the bar is structural, and price
   alone reopens nothing:
   - **Fee-earning AUM rising for two consecutive fiscal years on an organic basis**, that
     is, excluding anything bought for cash. RMR's own fee-earning AUM series (published
     quarterly in the supplemental) is the metric; $27.18B at 2026-06-30 is the marker.
   - **Third-party private capital raised from investors who are not RMR clients**, in size,
     with the CEO's own "challenging fundraising environment" language withdrawn.
   - **The manager-change-of-control termination carve-out removed or fee-protected** in the
     DHC, ILPT and SVC agreements. This is the [E4-23] defect and it is fixable only by
     contract amendment, which would be visible in an 8-K.
   - **A durable term restored at OPI** past the two-year no-fee cliff (June 2028), on terms
     disclosed.
2. **Price [E4-28].** The bottom boundary pays the 10% floor with zero credit for any of the
   above at **roughly $340M-$575M, or $11 to $18 a share**. Below **~$14** this file gets
   re-read for the record; entry still requires condition 1, which today does not exist.

**Watch-list metrics and thresholds (review triggers, not auto-executions):**
- **The dividend funding gap — the single most decidable line.** Track RMR LLC's per-unit
  distribution (currently **$0.32/quarter**) against RMR Inc.'s dividend (**$0.45**) and
  RMR Inc.'s standalone cash balance (**$15,386** at 2026-06-30, published every quarter on
  the "Well-Covered Dividend" page). **RMR Inc. cash below ~$10,000, or two consecutive
  quarters of decline with the LLC distribution unchanged, means the $1.80 is on a clock.**
  A cut to $1.28 is a 29% reduction and takes the yield from 9.25% to 6.6% at this price.
- **Incentive fees against the projection [E3-48]:** the CEO's "over $40 million … this
  calendar year" is measured at 2026-12-31 and recognised in the December quarter, reported
  in the Q1-FY2027 10-Q (~February 2027). **Outturn materially below $40M with the
  projection unwithdrawn is the guidance ledger's first entry.** A clean beat is the first
  contrary datum.
- **Client health, quarterly, from the clients' own filings:** SVC's leverage and hotel
  disposition proceeds; DHC's senior-living transition to third-party operators; ILPT's
  Mountain JV; OPI's post-emergence property count against the $14.0M flat fee. **Any second
  client entering a restructuring support agreement re-runs the death-1 arithmetic
  immediately.**
- **Fee-earning AUM and the property count [E4-55]:** two consecutive quarters of decline in
  fee-earning AUM, or the property count falling below ~1,750, is death 3 compounding.
- **The benchmark line [E2-49]:** any further amendment of an incentive-fee benchmark index,
  at any client, without a stated reason. One is a prompt; two is a pattern.
- **Balance-sheet drift [E3-40]:** further principal investment in client securities, or
  wholly-owned real estate above the current $225,762, funded by revolver draws. Revolver
  drawn above $50,000 against the $100,000 facility, or any new corporate (non-mortgage)
  debt, is the loss-of-focus vector accelerating.
- **The change-of-control clause:** any 8-K touching ABP Trust's holdings, any change in
  Adam Portnoy's role at RMR or at the clients, any amendment to the manager-change-of-
  control carve-out. **This is the one event that reprices the whole file in a day.**
- **A repurchase program, if one is ever authorised [E2-51, E5-08]:** its price discipline
  against this run's $11-$21 range would be the sharpest single read on capital allocation
  available.
- **Price alert (list only):** RMR below **$14** → re-run both reopen conditions.
- **Next catalysts:** FY2026 10-K and Q4 results ~mid-November 2026 (the first full year
  with the new OPI agreement, and the FY2026 AUM mark) · DEF 14A ~mid-January 2027 · the
  calendar-2026 incentive fee in the Q1-FY2027 10-Q ~early February 2027 · OPI's two-year
  no-fee termination cliff **June 2028** · revolver maturity **2028-01-22**.

**The taxable never-switch test, answered for the operator's mandate [E2-46, E3-64].** The
earmarked account wants a dividend payer that compounds, taxed once at the end. **RMR is a
high-current-yield holding, not a compounder, and the filings say so.** The 9.25% is real
cash today; roughly 29% of it is drawn from a balance the company itself dates at "more than
two years"; the LLC's own distribution rate has been **$1.28 flat since at least FY2023**;
the fee base that funds it has shrunk for three years; and the equity has returned minus 6%
over five years against a self-selected peer group's plus 150%. **A holding whose thesis is
"collect the yield and watch the funding gap" is a sell-discipline position, not a
hold-forever one**, and the switching arithmetic [E2-46, E3-64] penalises exactly that.
**The brief's bias warning is confirmed rather than resisted: the wished-for profile is not
in this filing.**

- **VERDICT: [x] IN** — what would prove this run wrong is written, dated and
  document-named on both sides: four structural reopen conditions and a price, plus seven
  monitored lines for the class thesis, each tied to a specific filed disclosure that
  recurs on a known schedule.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (Q2 OUT); Q3-Q5 written for
      the record only, with Q4/Q5 arithmetic under operator rule 3's **COMPUTATION — NOT A
      CLEARANCE** header
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] **Market cap verified as tasked from live EDGAR cover pages, class by class**
      (16,080,226 + 1,000,000 + 15,000,000 = 32,080,226 at 2026-07-31); the stale
      15,000,000 constant identified as the Class B-2 count that the 10-K says has "no
      independent economic interest"; the 2.14× error stated at the top; **and the sweep's
      6.02% yield honestly reported as approximately correct by offsetting errors rather
      than dismissed** [E4-26]
- [x] Step 0: filings read with accession numbers; **FY2025 OCF cross-checked three ways**
      ($75,746 statement = $75.7M MD&A prose = XBRL companyfacts); 9M-FY2026 OCF
      cross-checked against the MD&A's own increment ($60,118 + $22,819 = $82,937)
- [x] Owner earnings on multi-year means, both windows shown with the spread carried; the
      TA termination fee and the incentive-fee spike named and removed IN WRITING [E4-41];
      (c) disclosed as a judgment with the corpus default and the exception class tested
      [E3-44, E2-41, E5-20]; **SBC corrected off the XBRL tag to the filed cash-flow
      add-back and cross-checked against [E3-70]'s market-value standard**
- [x] **Bottom boundary [E5-34] computed with OPI-class fees at zero, arithmetic shown step
      by step, in three cost-relief cases plus an OPI+DHC stress**
- [x] Competitor row filled: 8 peers, 4 of them RMR's own self-selected group, all
      filing-sourced with accessions; every ratio labelled computed; Ashford's missing AUM
      named as unavailable with the reason; no moat class claimed that needs a missing row
- [x] Management-agreement terms read in full (duration, auto-extension, termination fee
      construction, change-of-control carve-out, incentive-fee formula and cap); related-
      person-transactions section read in both the 10-K and DEF 14A Annex A; the managed
      REITs' governance history recorded from the filings
- [x] Deaths quantified from filed figures with the likelihood vocabulary [E3-24, E4-40]
- [x] Sovereign for the earnings currency (USD, 100% domestic per the 10-Q) from the
      issuing-authority series, dated 2026-08-27; the failed re-fetch disclosed
- [x] Value stated as round-number ranges; floor verdict stated plainly; one bar (screamer,
      for the record); windage count: one, justified in writing
- [x] Prices dated; aggregators used for live quotes only and flagged
- [x] Q6 written regardless; alerts LISTED ONLY; taxable never-switch test answered; **no
      shared file edited** — this run created only this file and evidence under
      `Test Runs/_research 2026-08-26/`
- [x] The market-beating claim not made anywhere; every judgment carries a ledger id or is
      labelled a judgment or an estimate
- [x] Run committed to git

## REGISTER
- **Verdict: [x] OUT (about the business, at Q2 — for entry).** No position held. Q1 IN.
  Q3 for the record: **no honesty disqualifier found and the disclosure record is genuinely
  good**, but the weight case is a binary gate and the flags converge; the manager is the
  plan, the counterparty, the clients' chairman and the 91% voter. Q4 for the record:
  survives the current regime comfortably; [E5-11] legs 2 and 3 fail; no cushion for a
  second client failure. Q5 computation: the 10% floor does not clear at the bottom
  boundary (8.6-9.2%), and the price sits inside the honest value range, which is the
  screamer test's middle box.
- **One line:** *an externally-managed manager whose twenty-year evergreen contracts were
  cut to five years terminable-after-two the one time a counterparty could actually
  negotiate, whose termination fee is written to vanish if its controlling shareholder ever
  ceases to control it, whose fee is a percentage of its clients' debt-inclusive enterprise
  value and therefore shrinks every time it does right by them, whose AUM, fee revenue,
  property count and headcount have all fallen while $410M of cash and new mortgage debt
  went into buying replacement AUM, and whose five-year total return is minus 6% against a
  peer group it chose itself returning plus 150% — priced at a genuine 8.6-9.2%
  bottom-boundary owner-earnings yield, which is the honest reason the file was worth
  opening and is not enough to open the gate.*
- **Work orders (UNRESEARCHED, none blocking Q2):**
  1. **The clients' own filings, read as the fee base rather than as companies** — DHC
     (CIK 1075415), ILPT (1717307), SVC (945394), SEVN (1452477), OPI (1456772) most recent
     10-Qs, all filed and free on EDGAR, ordinary retrieval. Wanted: each client's debt
     maturity wall and covenant headroom, which is what death 1's likelihood actually turns
     on. *Not obtained in this run for reasons of scope; Q2 is decided without them.*
  2. **The business and property management agreements themselves**, filed as exhibits to
     RMR's 10-K (Exhibits 10.5 onward), rather than the 10-K's summary. Wanted: the precise
     definition of "manager change of control" and of the "performance reason" measure.
     Ordinary retrieval; the summary was read and is unambiguous on the fee consequence.
  3. **Sonesta's and ABP Trust's economics** — private, no filings. Likely **UNKNOWABLE**
     beyond what RMR discloses ($9,314 of FY2025 fees, 0.6% of revenues).
  4. **The Braemar/Ashford Section 12.5(b) termination amount** — the 2025-08-26 8-K
     references the calculation without a dollar figure; the exhibit letter agreement would
     resolve it. Would sharpen the internalization price table, not change it.
  5. **FY2026 10-K (~November 2026)** — first full year of the new OPI agreement, the FY2026
     AUM mark, and the next [E3-48] data point on the $40M incentive-fee projection.
- **The single biggest concern:** not any one of the flags, but **the direction of the
  whole structure**. This was, five years ago, a debt-free, asset-free, $341M-cash toll
  booth earning 22-32% on equity and paying a $7.00 special dividend because it had more
  cash than it could use. It is now a levered principal investor earning 9.4% on equity,
  with $58M of cash, a dividend part-funded from a balance the company itself dates at two
  years, a client base one member smaller and shrinking, and a moat whose central provision
  is written to disappear on a change of control of one man. **None of that is dishonest;
  all of it is disclosed; and all of it is what [E3-40] means by loss of focus and what
  [E2-60] means by distributing restricted earnings.** The 9.25% dividend yield that put
  this name on the list is the most attractive number in the file and the one most likely
  to be wrong within three years.

*This file is a judgment by the AI running the framework; the underlying facts are the
FY2025 10-K (acc. 0001644378-25-000043), the Q3-FY2026 10-Q (acc. 0001644378-26-000020) and
the two earlier FY2026 10-Qs, the FY2024/FY2023/FY2022/FY2021 10-Ks, the 2026 DEF 14A
(acc. 0001104659-26-004085), the earnings 8-Ks of 2026-08-05 and 2025-11-12, SEC XBRL
companyfacts (CIK 0001644378), the eight peer 10-Ks and nine internalization 8-Ks listed at
Q2, FRED DGS30, and flagged aggregator quotes for price. Where a number is a judgment or an
estimate — the (c) band, the bottom-boundary band, the cost-drop-through cases, the
return-on-capital series, the clients' equity market values, the reopen band — it is
labelled as one.*
