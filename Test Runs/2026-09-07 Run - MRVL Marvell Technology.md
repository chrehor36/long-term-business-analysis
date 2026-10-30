# Company Run — Marvell Technology, Inc. (MRVL) — 2026-09-07
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

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.37 %** · date **2026-09-10** · source **US Treasury daily par yield curve, 30-year,
  from home.treasury.gov (the issuing authority; not FRED)**, struck via `tools/sources.py`
  on 2026-09-11. *(The run was started 2026-09-07 against 5.24% of 2026-09-04 and killed by
  the weekly session limit; resumed 2026-09-11. The brief's 5.24% is stale by +13bp and is
  not used anywhere below.)*
- FX: none. Marvell reports and earns in USD. Delaware incorporated. No ADR ratio.

**Shares — Stage 0, BY HAND off the cover of the LATEST periodic filing (not tagged data):**
> *"The number of shares of common stock of the registrant outstanding as of **August 21,
> 2026** was **876.9 million**."*
> — **Q2 FY2027 10-Q cover page**, period 2026-08-01, filed 2026-08-28, accession
> **0001835632-26-000025**, doc `mrvl-20260801.htm`

**AND THE COVER COUNT IS NOT THE ECONOMIC COUNT — a second class exists and it was created
five months ago.** Balance sheet, same filing:
> *"Preferred stock, $0.002 par value; 8.0 shares authorized; **2.0 shares issued and
> outstanding as of August 1, 2026 of Series A Convertible Preferred Stock** (none issued
> and outstanding as of January 31, 2026)"*

> *"On **March 31, 2026**, the Company completed the issuance and sale of 2.0 million shares
> of Series A Convertible Preferred Stock … **to NVIDIA Corporation ("NVIDIA"), for an
> aggregate purchase price of $2.0 billion.** Each share … is initially convertible … at an
> initial conversion price of approximately $91.84 per share into an aggregate maximum of
> approximately **21.8 million shares of common stock**"* (21,778,000 exactly, per the risk
> factor in the same document).

Marvell's own EPS denominator is stated as **"common stock and preferred stock assuming
conversion"** — basic 897.4M for Q2 FY2027. **So the company itself treats the preferred as
economic common.** This run does the same.

| | shares | × $226.96 |
|---|---|---|
| Common on the cover, 2026-08-21 | 876,900,000 | $199,021M |
| **plus Series A preferred, as converted** | **21,778,000** | **$4,943M** |
| **= ECONOMIC SHARE COUNT** | **898,678,000** | **$203,964M** |

**MARKET CAPITALISATION = $203,964M (economic, as-converted); $199,021M on the bare common
count. Both are reported; the ranking below uses the as-converted figure because it is the
one Marvell's own EPS line uses.**

**THE BRIEF'S SCREEN ROW CARRIED `cap_m 184491`, WHICH IS $223.55 × 825.3M — a share count
that predates the Celestial share issuance, the NVIDIA preferred and the current cover.
On the same $223.55 the economic count gives $200,899M: the screen cap is 8.2% too small, so
every yield in the row is 8.9% too high.** Defect #2 of the brief's mandatory-corrections
list fires, for the fifth time in this queue.

**AND A THIRD INSTRUMENT EXISTS, DATED AFTER THE QUARTER END — a customer warrant:**
> *"Subsequent to quarter end, **we issued a warrant to a customer to purchase an aggregate
> of up to 59.0 million of our common stock at an exercise price of $206.58 per share** over
> a seven year term expiring in August 2033. The warrant is eligible for vesting from our
> third quarter of fiscal 2027 through the end of fiscal 2033, upon meeting certain revenue
> milestone conditions or time-based conditions."*

**59.0 million shares — 6.6% of the economic count — promised to a CUSTOMER, contingent on
that customer's own purchases.** It is not in the cap above: it is unvested. It is *in* the
money at $226.96 against a $206.58 strike, so the exclusion is a timing judgment, not a
value one. A second, earlier customer warrant is already vesting: the equity statement
carries *"Vestings of common stock in connection with customer warrant 10.9"* in Q1 FY2027.
**This is carried to Q2 as the sharpest available evidence on who holds the pricing power,
and to Q3 as a dilution item.**

**Price** (aggregator, flagged per operator rule 5 — live quotes only):
- **$226.96**, close of **2026-09-10**, Yahoo Finance, via `tools/sources.py`, struck
  2026-09-11. *(First struck at $223.55 on 2026-09-04 before the session was killed; the
  fresh figure is used everywhere below.)*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **FY2026 10-K · period 2026-01-31 · filed 2026-03-11 · accession 0001835632-26-000011**
  (`mrvl-20260131.htm`) — the document of record.
- Also read: **Q2 FY2027 10-Q**, acc. 0001835632-26-000025 (period 2026-08-01, filed
  2026-08-28) — **the brief's screen row says `newest_filing 2026-01-31`, which is two
  quarters stale and misses both acquisitions and both equity instruments above**;
  **FY2025 10-K** acc. 0001835632-25-000057; **FY2024 10-K** acc. 0001835632-24-000009;
  **FY2023 10-K** acc. 0001835632-23-000013; **FY2022 10-K** acc. 0001835632-22-000016 (the
  Inphi year); the **Q2 FY2027 8-K/EX-99.1** of 2026-08-27, acc. 0001835632-26-000022.
- **Figure cross-checked against the filed statement:** the XBRL
  `NetCashProvidedByUsedInOperatingActivities` of **$1,750.5M** for FY2026 was checked
  against the filed CONSOLIDATED STATEMENTS OF CASH FLOWS in `mrvl-20260131.htm` — agrees to
  the dollar. A second cross-check was run on the tag that produced the brief's flag and it
  **fails** — see the D&A section below.
- **Balance-sheet integrity check [E5-32]:** at 2026-01-31, assets $22,285.3M − liabilities
  $7,976.9M = **$14,308.4M** = the stated total stockholders' equity, exactly.

---
## THE PERIMETER — REBUILT FROM THE BUSINESS-COMBINATION NOTES, AND IT IS THE FILE

**`years_filed 7` is not a data gap. It is the age of the registrant.** Marvell Technology,
Inc. (CIK **1835632**, Delaware) was created in 2021 to be the holding company for the Inphi
merger; the prior registrant was Marvell Technology Group Ltd. (CIK 1058057, Bermuda). Seven
fiscal years is all the current entity has filed, and **the seven years contain four
different companies.**

### Acquisitions, from the filed notes and cash-flow statements

| deal | closed | consideration, filed | cash in investing |
|---|---|---|---|
| Cavium | 2018-07-06 | ~$6.0bn cash + stock (prior registrant) | before the window |
| Aquantia | 2019-09-19 | ~$0.45bn cash | FY2020 |
| Avera Semiconductor (GlobalFoundries ASIC unit) | 2019-11-05 | ~$0.65bn | FY2020: **$1,071.1M** total |
| **Inphi Corporation** | **2021-04-20** | **~$10bn cash + stock** | FY2022: **$3,555.0M** |
| Innovium | 2021-10-05 | ~$1.1bn stock | inside the same FY2022 line |
| Aquila / Terago (small) | FY2024 | — | FY2024: $112.3M |
| **automotive ethernet business SOLD to Infineon** | **2025-08-14** | **$2.5bn cash IN** | FY2026: **+$2,478.6M**, pre-tax gain **$1,830.4M** |
| **Celestial AI** | **Q1 FY2027 (Feb 2026)** | **$3.5bn total purchase consideration** | FY2027: **$1.0bn cash + 26.8M shares**, plus contingent cash and shares through fiscal 2029 |
| **XConn Technologies** | **Q1 FY2027 (Feb 2026)** | not separately stated | FY2027: **$270.2M cash** |

**THE FLAG READ THE INVESTING LINE AND UNDERSTATED THE PERIMETER FOR THE FIFTH CONSECUTIVE
RUN.** Investing-cash for Inphi+Innovium was $3,555.0M. **The filed consideration was
~$10bn, because the majority was paid in stock** — Marvell's share count went from ~669M
(FY2021) to ~845M (FY2022). The CRM shape exactly: *Tableau cost $14,845M of which the cash
was $1 million.*

**AND THE PERIMETER MOVED AGAIN AFTER THE 10-K THE SCREEN READ.** Celestial AI closed in
**February 2026**, three weeks after the FY2026 year end, for **$3.5 billion**, and XConn
with it. Every owner-earnings figure below is computed on a company that **no longer
exists in that form**: the numerator is Marvell-without-Celestial and the denominator is a
market cap that includes it. **The brief's warning — "the numerator and denominator may be
different companies" — is literally true here, and it is true twice: the automotive business
is in the numerator's early years and gone from its last, and Celestial is in the
denominator and absent from the numerator entirely.**

### Were pro formas filed? Asked, and the answer is a partial no

- **Inphi/Innovium (FY2022 10-K, acc. 0001835632-22-000016):** a pro-forma table **is** filed.
- **Celestial/XConn (Q2 FY2027 10-Q):** the acquisitions are disclosed with preliminary
  purchase-price allocations. Pro-forma revenue and earnings are **not** given as of Q2
  FY2027 — the 10-Q states the allocations are preliminary.
- **The Infineon disposal was NOT treated as discontinued operations.** It runs through
  continuing operations and the $1,830.4M gain sits in *"Interest income and other, net"* —
  which is why FY2026 net income of $2,670.1M is not a business number and why [E2-23]
  refuses the net-income proxy.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Marvell designs chips it does not
manufacture and sells them into other companies' data centres. It has three ways of getting
paid and they are not the same business:

**One — custom silicon.** A hyperscaler decides it wants its own accelerator or its own
switch rather than buying a merchant part. Marvell's engineers co-design that chip with the
customer's engineers, TSMC builds it, and Marvell sells the finished part back to the
customer for the life of the program. The customer pays the non-recurring engineering and
then a per-unit price. Marvell books the revenue; the *architecture* belongs substantially to
the customer.

**Two — merchant connectivity.** Optical DSPs (the Inphi business), retimers, PCIe/CXL
switches, Ethernet switch silicon. These are catalogue parts sold to module makers, switch
vendors and the same hyperscalers. Here Marvell owns the design and competes part-for-part.

**Three — the legacy tail.** Carrier and enterprise networking, and until August 2025
automotive ethernet, which was sold to Infineon for $2.5bn.

**So how does Marvell make money?** It spends **$2,075.2M a year of R&D on 8,194.6M of
revenue — 25.3% of sales, the highest ratio in the competitor row below** — to win sockets
inside data-centre hardware, and then collects a per-unit price for as long as that hardware
ships. The scarce input is **engineering headcount that can tape out a leading-node
mixed-signal SoC**, and Marvell has bought it four times rather than grown it: Cavium,
Avera, Inphi, Celestial.

**The scarce input this business controls:** the design win, and only for the life of the
program. Marvell does not control a fab, a process node, an instruction set, a brand or a
standard. It controls the incumbency of a specific chip in a specific box, and that
incumbency has a stated end date — the next program.

**Will the fundamentals look broadly the same in ten years?** Three facts, stated as they
are:
- The **connectivity** franchise (Inphi's optical DSPs) has a real technical lead and a
  product cadence measured in years. Ten years is plausible for the *category*.
- The **custom silicon** line, which is where all the growth is, is a program business. Every
  program is re-competed. The customer owns the architecture and can move it.
- The **company** has bought a business every two years for eight years and changed its
  registrant, its country of incorporation, its segment structure and its perimeter inside
  the window. Predicting Marvell-in-2036 requires predicting what it buys next.

**I can nonetheless describe how each dollar of today's revenue is earned from the filed
statements, without needing to know what it buys next**, and that is what [E3-31] asks. It
is not the ATLKY class and it is not [E4-46]'s five-months-of-study class. **The business is
simple. Its perimeter is not, and that is a Q2/Q4 problem, not a Q1 one.**

- **VERDICT: [x] IN**

---
## COMPUTATION — NOT A CLEARANCE
*(operator rule 3: this arithmetic is produced before Q2–Q4 have closed. It carries no
entry language and it is not a Q5 output.)*

### THE D&A FLAG — READ FROM THE CASH-FLOW STATEMENT, AND IT IS THE CERT DEFECT AGAIN

The brief's `da_note` says *"D&A steps 5.5x at 2022-01-29."* **Marvell's filed cash-flow
statement carries two separate lines, in every vintage**, and the flag spliced them:

| $M, filed cash-flow statement | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|---|---|
| "Depreciation and amortization" (PP&E, licences, ROU) | 124.0 | 156.7 | 197.9 | 265.9 | 304.9 | 299.8 | 304.3 | 348.6 |
| "Amortization of acquired intangible assets" | 183.3 | 368.1 | 443.6 | 979.4 | 1,087.4 | 1,097.9 | 1,052.6 | 942.0 |
| **Total D&A, filed** | **307.3** | **524.8** | **641.5** | **1,245.3** | **1,392.3** | **1,397.7** | **1,356.9** | **1,290.6** |
| step, year on year | | 1.71× | 1.22× | **1.94×** | 1.12× | 1.00× | 0.97× | 0.95× |

*(FY2019–FY2021 from the prior registrant's FY2021 10-K, CIK 1058057, acc.
0001058057-21-000009; FY2022 onward from the current registrant's 10-Ks named at Step 0.)*

**The real step at FY2022 is 1.94×, not 5.5×.** The screen's 5.5× is arithmetic on two
different tag definitions: FY2021 read from the XBRL `DepreciationAndAmortization` tag
(**197.9** — the PP&E line only, which in Marvell's taxonomy *excludes* acquired-intangible
amortisation), and FY2022 read from `Depreciation` + `AmortizationOfIntangibleAssets`
(113.5 + 979.4 = **1,092.9**). 1,092.9 ÷ 197.9 = 5.52. **Two definitions spliced at the
year the Inphi amortisation arrived — exactly the CERT shape the flag was written after.**
And the spliced FY2022 figure is itself wrong by $152M against the filed total of 1,245.3,
because `Depreciation` (113.5) is not the "Depreciation and amortization" line (265.9).

**What the 1.94× real step IS: Inphi.** *"The Company completed the acquisitions of Inphi
Corporation for $9.9 billion on April 20, 2021, and Innovium, Inc. for $1.0 billion on
October 5, 2021 … including intangible assets of $4.4 billion for Inphi and $433 million for
Innovium"* (FY2022 10-K, Critical Audit Matter). $4.8bn of finite-lived intangibles on
five-to-eight-year lives is ~$700M a year of new amortisation, and that is the step. **The
brief's prior on the cause is CONFIRMED; the brief's magnitude was a tooling artefact.**

**Cash-flow cross-check on the flag's own tag [E5-32]:** XBRL `OtherDepreciationAndAmortization`
FY2026 = 348.6 = the filed "Depreciation and amortization" line; `AmortizationOfIntangibleAssets`
FY2026 = 942.0 = the filed acquired-intangible line. Sum 1,290.6. **The filed total is
reproducible from XBRL only by summing two tags neither of which is `DepreciationDepletionAndAmortization`
— which is why the brief's fix-note ("(c) prefers a filed D&A total and sums components only
when none exists") does not rescue this row: no total tag exists, and the component sum it
falls back to uses the wrong depreciation tag.** Recorded as a defect against the tool.

### THE SCREEN ROW — REPRODUCED, AND BOTH ENDS ARE DIFFERENT WINDOWS

Screen row: `oe_bottom_m -373 | oe_top_m 676 | spread: n/a`.

**Owner earnings by year, from the filed cash-flow statements (all $M):**

| FY | OCF | SBC | capex | tech-licence cash *(financing + investing)* | **OE, capex end** | total D&A | **OE, D&A end** | **OE, capex+licence end** |
|---|---|---|---|---|---|---|---|---|
| 2019 | 596.7 | 184.1 | 75.9 | 80.7 | 336.7 | 307.3 | 105.3 | 256.0 |
| 2020 | 360.3 | 242.2 | 81.9 | 77.0 | 36.2 | 524.8 | −406.7 | −40.8 |
| 2021 | 817.3 | 241.5 | 106.8 | 112.7 | 469.0 | 641.5 | −65.7 | 356.3 |
| 2022 | 819.4 | 460.7 | 169.3 | 152.1 | 189.4 | 1,245.3 | −886.6 | 37.3 |
| 2023 | 1,288.8 | 552.4 | 206.2 | 153.6 | 530.2 | 1,392.3 | −656.0 | 376.6 |
| 2024 | 1,370.5 | 609.8 | 336.3 | 164.2 | 424.4 | 1,397.7 | −637.0 | 260.2 |
| 2025 | 1,681.2 | 597.4 | 284.6 | 160.6 | 799.2 | 1,356.9 | −273.1 | 638.6 |
| **2026** | **1,750.5** | **590.8** | **354.1** | **132.8** | **805.6** | **1,290.6** | **−130.9** | **672.8** |
| H1 FY2026 | 794.5 | 295.7 | 166.3 | 56.5 | 332.5 | 657.7 | −158.9 | 276.0 |
| H1 FY2027 | 1,244.3 | 533.8 | 282.4 | 61.6 | 428.1 | 628.6 | 81.9 | 366.5 |

- screen `oe_top` **676** = the **3-year FY2024–26 mean at the capex end**: my figure
  **676.4**. Reproduces.
- screen `oe_bottom` **−373** = the **5-year FY2022–26 mean at the SPLICED D&A end**: my
  figure on the spliced tags is **−369.5**; on the **filed** D&A totals it is **−516.7**.
  The row reproduces to $4M on the tool's own construction and **understates the true D&A
  end by $147M**, because the splice used `Depreciation` in place of the filed line.
- **So the two published "ends" are two different windows AND two different (c)
  definitions, one of them wrong.** The INTC shape.

**Rebuilt over my own windows [E4-25], all three ends, in DOLLARS:**

| construction | window | $M | yield on $203,964M |
|---|---|---|---|
| capex end, 3-yr (FY2024–26) | 3 | **676.4** | 0.33% |
| capex end, 5-yr (FY2022–26) — **corpus default [E2-42]** | 5 | **549.8** | 0.27% |
| capex end, 7-yr (FY2020–26) — the registrant's full history | 7 | **464.9** | 0.23% |
| capex end, 8-yr (FY2019–26) — adds the Cavium year | 8 | **448.8** | 0.22% |
| capex + technology-licence end, 3-yr | 3 | **523.9** | 0.26% |
| capex + technology-licence end, 5-yr | 5 | **397.1** | 0.19% |
| capex + technology-licence end, 8-yr | 8 | **319.6** | 0.16% |
| D&A end (filed totals), 3-yr | 3 | **−347.0** | negative |
| D&A end (filed totals), 5-yr | 5 | **−516.7** | negative |
| D&A end (filed totals), 8-yr | 8 | **−368.8** | negative |
| FY2026 alone, capex end (best full year ever filed) | 1 | **805.6** | 0.39% |
| **TTM to 2026-08-01, capex end** | 1 | **901.2** | **0.44%** |
| TTM to 2026-08-01, capex + licence end | 1 | **763.3** | 0.37% |
| TTM to 2026-08-01, D&A end — *the first positive D&A-end figure in the company's filed history* | 1 | **109.9** | 0.05% |

**THE WIDTH, IN DOLLARS AND A WORD: from MINUS $517M to PLUS $901M — a $1.4 BILLION range
on a business whose best year is $806M. The range crosses zero on every multi-year window
and the word is DISAGREEMENT: the constructions disagree about whether Marvell has ever
earned anything for its owners.** [E4-25]'s *"the range must be so wide that no useful
conclusion can be reached"* is the description, and the section below establishes **why**
they disagree before either end is used.

**And the honest note on every row above: the numerator is Marvell-before-Celestial and
the denominator includes it** (Step 0). No pro forma exists to fix that yet.

**A wide spread is a Q4 finding [E5-11], and the distorted years are named:**
- **FY2020 is DEPRESSED** (OCF $360M on $2.7bn revenue): the Avera/Aquantia year, plus a
  $1,122M gain on the Wi-Fi disposal that sits in net income and not in OCF.
- **FY2022 is DEPRESSED**: the Inphi/Innovium year — SBC nearly doubled ($241.5M →
  $460.7M, assumed awards), $194M of inventory step-up amortised, restructuring, and $7.2bn
  of stock issued.
- **FY2025 is DEPRESSED in the income statement and not in OCF**: a **~$715M Q3 FY2025
  restructuring** — $358.3M in operating expenses and roughly $400M inside cost of goods
  sold (Q3 FY2025 COGS $1,166.7M on $1,516.1M of revenue against $685.3M the prior
  quarter; GAAP gross margin **23.0%** that quarter). Mostly *"impairment and write-off of
  purchased technology licenses and property and equipment, as well as recognition of
  future contractual obligations"* — non-cash, so OCF is undisturbed; the **cash** for those
  licences had already left through the financing line in earlier years.
- **FY2026 is ELEVATED in net income and not in OCF**: the $1,830.4M Infineon gain is
  deducted in the reconciliation. It is why net income of $2,670.1M is a disposal, not a
  business.
- **[E4-41] normalisation DOWN for luck:** the FY2026–27 AI-capex surge is the favourable
  exogenous break [E4-41] says to strip before trusting a mean. It is not stripped; it is
  named, and the ranking below runs on the *unstripped, most generous* figure so the
  conclusion cannot be accused of it.

### THE (c) JUDGMENT — THE AVGO RULING, DECIDED HERE, AND IT LANDS IN THE SAME PLACE BY A DIFFERENT ROUTE

**Direction first, so no reader inverts it: at Marvell the D&A end is the CONSERVATIVE end
and the capex end is the GENEROUS end** — the reverse of an ordinary filer. FY2026 total
D&A of $1,290.6M is **3.6× capital expenditure** of $354.1M, and $942.0M of it is
amortisation of intangibles bought with cash and stock that left in FY2019–FY2022.

**Decided from the filed split of depreciation versus amortisation [E3-44], in three parts:**

1. **The physical half — and here Marvell is NOT Broadcom.** Broadcom's depreciation ran
   1.09× its capex, steady state. Marvell's "Depreciation and amortization" line (348.6)
   is *below* capex (354.1) and far below capex-plus-licence cash (486.9); capex has grown
   **4.3× in seven years** (81.9 → 354.1) against 3.0× revenue, runs **4.3% of revenue**
   (Broadcom 0.98%), and H1 FY2027 capex of $282.4M annualises to ~$565M. **On the physical
   side the capex end is already the binding one** — spending depreciation would not keep
   the company in place [E5-20], and the filing's own words are that R&D spend rose for
   *"advanced IP development and customer design win activity."* This is why the
   capex-plus-licence column exists: **Marvell pays $128–154M a year for capitalised IP
   licences through the FINANCING line** (*"Payments on technology license obligations"*),
   a renewal cost that neither OCF nor investing capex captures, and which the FY2025
   restructuring then wrote off when the product lines were abandoned. Under [E2-23]'s
   *"capitalized expenditures for plant and equipment, etc. that the business requires to
   fully maintain its long-term competitive position"*, it belongs in (c). **$666.3M of
   such licence commitments are outstanding at 2026-08-01.**
2. **The acquired-intangible half renews nothing that R&D does not already renew.** The
   QCOM ruling, applied at AVGO and CRM: what keeps Inphi's DSP designs current is the
   **$2,075.2M of R&D expensed above the OCF line — 25.3% of revenue, the highest ratio in
   the competitor row.** Deducting $942M of amortisation as well charges the renewal twice.
   The judgment is the same as AVGO's and it is recorded as such.
3. **But the [E2-23]/[E2-60] objection is STRONGER here than at AVGO, and it must be
   written down.** Broadcom bought a mature franchise and harvested it. **Marvell bought its
   growth line itself**: optical interconnect — *"roughly half of our data center
   revenue"* (2026 proxy) — is Inphi; the custom-ASIC capability is Avera; the next-generation
   interconnect is Celestial, bought three weeks after the year end for $3.5bn plus an
   earnout now marked at **$749.5M** (up from $315.8M at close, because the earnout is
   payable partly in Marvell shares and the shares rose). **Cumulative acquisition
   consideration since FY2019 is roughly $22bn — Cavium ~$6bn, Aquantia/Avera ~$1.1bn,
   Inphi $9.9bn, Innovium $1.0bn, Celestial $3.5bn plus earnout — against cumulative
   capex-end owner earnings of $3.6bn over the same eight years.** If maintaining *"its
   long-term competitive position and its unit volume"* requires buying the next
   technology every two years, then acquisition spend IS (c), and owner earnings are
   deeply negative on every window. **That reading is not priced into (c). It is carried
   to Q2 as the moat-class finding it is — [E4-04]'s continuously-rebuilt moat in its
   purest form — and to Q4 as the named way this business dies.**

**(c) JUDGED — a disclosed judgment, per [E2-23] "must be a guess": (c) = total capital
expenditure PLUS technology-licence cash, ~$487M in FY2026 and ~$450M on the five-year
mean** — above the bare capex end because the physical spend is rising and the licence
payments are real renewal cash hidden in financing; below the D&A end because acquisition
amortisation is a sunk purchase price whose renewal is already inside OCF as R&D. **The D&A
end is carried in the table as the pessimistic bound. The acquisition-as-maintenance
reading is carried to Q2 and Q4, not to (c).**

**Stock compensation subtracted in full [E5-06]: $590.8M, 7.2% of FY2026 revenue — and it
is accelerating: H1 FY2027 SBC of $533.8M is 1.8× the prior-year half ($295.7M), on
Celestial replacement awards and new grants.** **[E3-70] recorded and NOT stacked:** the
market-value measure would be higher; the reported charge is the floor of the subtraction.
A further $365.2M of cash left in H1 FY2027 alone for tax withholding on vesting. Windage
is not spent here.

### THE PRICE — the number the queue's output contract requires

- **Price $226.96** (2026-09-10, Yahoo, aggregator, flagged) · **cap $203,964M** (economic,
  as-converted; $199,021M on the bare cover count)
- **Owner-earnings yield: NEGATIVE to 0.44%** across every construction that exists,
  including the trailing twelve months at the most generous (c).
- **Sovereign 5.37%.** **Every construction, on every window, at every (c), including the
  best twelve months in the company's history, is between 4.9 and 5.9 points BELOW a
  government bond.** For the yield to reach the bond, owner earnings would have to be
  **$10.95bn — 12× the trailing figure and 2.6× FY2026's entire gross profit.**

*Nothing in this block is a clearance. Q2, Q3 and Q4 follow.*

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

### THE BULL CASE, BUILT AT FULL STRENGTH FIRST [E4-26, E4-51]

The brief's prior is OUT, held weakly. Before testing it, the case for the franchise as its
holders would state it:

1. **Custom silicon is designed in for the life of a program.** A hyperscaler that
   co-designs an accelerator or a NIC with Marvell cannot swap the supplier mid-program
   without a redesign cycle; the switching cost is real and multi-year. The 2026 proxy:
   *"Our custom silicon business has scaled rapidly from effectively zero to approximately
   25% of our data center revenue."* Q2 FY2026 release: *"Our custom AI design activity is
   at an all-time high, with the Marvell team now engaged in over 50 new opportunities
   across more than 10 customers."*
2. **The optical-DSP franchise (Inphi) has a demonstrated technical lead and a product
   cadence measured in years.** Proxy: *"Optical interconnect has grown at an approximately
   50% compound annual growth rate (CAGR) for five straight years and represents roughly
   half of our data center revenue."* Every AI cluster needs optical links between racks;
   Marvell's DSP sits in a large share of the world's 800G/1.6T modules.
3. **The record is real and filed:** data-center revenue $1,040.8M (FY2021) → $6,100.3M
   (FY2026), a 5.9× in five years; consolidated revenue +42.1% in FY2026 and +37% in Q2
   FY2027; eight consecutive quarterly guidance beats.
4. **Two of the industry's principals have just bought into it with their own money:**
   NVIDIA paid $2.0bn for convertible preferred at $91.84 (2026-03-31) and Google signed a
   seven-year custom-products agreement (2026-07-29).

That is a genuine case and it is stated before it is tested.

### [E3-03], CRITERION BY CRITERION

**(1) Needed or desired — yes.** AI data centres are being built; the interconnect and
custom compute inside them are not optional.

**(3) Not price-regulated — yes.** No regulator sets Marvell's prices.

**(2) "Thought by its customers to have no close substitute" — and this is where the file
turns.** Three filed facts, none of them from a competitor:

**First, the customers are the substitute, in Marvell's own words** (FY2026 10-K, Competition):
> *"In addition, **some of our customers have chosen to develop certain semiconductor
> products internally and this trend may continue to proliferate.**"*

And the same section names the merchant competitors by company: *"Advanced Micro Devices,
Inc., Alchip Technologies, Astera Labs, Inc., Ayar Labs, Inc., Broadcom Inc., Cisco
Systems, Inc., Credo Technology Group Holding Ltd, Intel Corporation, Global Unichip
Corporation, Lightmatter, Inc., MACOM Technology Solutions Holdings, Inc., MediaTek Inc.,
Microchip…"* — **fifteen-plus named competitors, two of which (Alchip, GUC) are the
Taiwanese custom-ASIC houses that do exactly what Marvell's custom business does, at
foundry-affiliated cost.** Broadcom, by contrast, names zero competitors (AVGO run).

**Second, the customer-concentration series across vintages — the brief's specific
instruction — and it is the sharpest series in this file:**

| FY | ten largest customers, % of revenue | Distributor A | Customer A | receivables, top customers |
|---|---|---|---|---|
| FY2020 | — | 12% | * | — |
| FY2021 | — | 13% | * | four = 53% |
| FY2022 | **56%** | 15% | * | six = 52% |
| FY2023 | **63%** | 20% | * | five = 55% |
| FY2024 | **72%** | 24% | * | three = 67% |
| FY2025 | **81%** | 34% | 13% | four = 72% |
| FY2026 | **82%** | 37% | 14% | four = 73% |
| **Q2 FY2027** (three months) | — | **44%** | **16%** | five = 72% |

*(FY2022–FY2026 10-Ks; Q2 FY2027 10-Q. "*" = under 10%. Marvell has never named
Distributor A or Customer A in any vintage.)*

**Ten customers were 56% of revenue in the year Inphi closed and are 82% now. Two
customers — one of them an unnamed distributor — were 61% of revenue in the latest quarter.**
The AI business did not diversify Marvell's customer base; it concentrated it, and the
counterparty holding the most of it is a distributor, which means Marvell does not itself
file who the end customer is.

**Third — and this is the fact that settles criterion (2) — Marvell pays its largest custom
customer, in equity, to buy from it.** 8-K of 2026-08-19, Item 1.01, verbatim:
> *"On July 29, 2026, Marvell Technology, Inc. (the "Company") and **Google LLC** ("Google")
> entered into a commercial agreement relating to the Company's development of custom
> semiconductor products to Google … In connection with this collaboration, on August 18,
> 2026, the Company issued to Google a warrant … to purchase up to an aggregate of
> **58,970,907 shares** of common stock of the Company … at an exercise price of $206.58
> per share. … The remaining Warrant Shares vest based on discretionary purchases … **in
> 240 equal tranches, with one tranche vesting for each $500 million in Custom Products
> revenue.**"*

**240 tranches × $500M = $120 billion of custom revenue over seven years is the vesting
schedule, and the price of it is 6.6% of the company.** A business whose product had *no
close substitute* would not need to pay its customer to buy it. **This is [E4-37]'s
agony-of-pricing metric read at its extreme: the customer does not merely resist a price
increase — the supplier pays for the volume.** The word "discretionary" in the vesting
clause is the customer's, and it is filed. A second, earlier customer warrant was already
vesting in Q1–Q2 FY2027 (*"Vestings of common stock in connection with customer warrant"*,
$10.9M and $11.3M in the equity statement). **Criterion (2) FAILS on the custom half, in
the company's own filing, and the bull case's strongest leg — design-in for the life of the
program — is the leg on which the customer extracted equity.**

**On the optical half, criterion (2) is closer and is stated fairly.** Inphi's DSP position
is real; but the competitor row below shows **Credo at a 33.3% operating margin and Astera
at a 75.7% gross margin in adjacent connectivity sockets**, both growing faster than
Marvell, and both founded inside the last twelve years — the socket admits entrants.
Marvell's response to the threat was to buy Celestial for $3.5bn.

### [E4-04] — MUST THE MOAT BE CONTINUOUSLY REBUILT? YES, AND IT IS REBUILT BY PURCHASE

*"does a lapse in spending destroy the structure, or merely narrow it — and does the
spending defend the same advantage, or buy its replacement?"* At Marvell the spending
**buys the replacement, by acquisition, on a two-year cadence**: Cavium (2018), Aquantia
and Avera (2019), Inphi and Innovium (2021), Celestial and XConn (2026). Each is a *new*
technology position, not a defence of the prior one; the prior ones were, in the case of
Wi-Fi and automotive ethernet, sold. **This is not [E5-23]'s defend-the-same-moat class;
it is Munger's competitive destruction with the destruction pre-empted by cheque.** And the
custom-silicon line, where the growth is, re-competes every program from zero — the moat's
basis is replaced each generation by definition. **[E3-51] is the honest description: a
surfing run.** The wave is hyperscaler AI capex; Marvell is a good surfer; the advantage
lives in the wave.

**[E4-36] — which cause of extreme success?** The five-year revenue record comes from
**wave-riding plus an acquisition** (Inphi supplied the product that caught the wave).
Neither cause is ownable.

**Does success depend on a great manager [E4-23]?** Matt Murphy has run it since 2016 and
the acquisition sequence is his. A business whose moat is rebuilt by M&A every two years
depends on the acquirer's judgment every two years. **Recorded here as a moat defect, per
[E4-23]** — the surgeon is the plan.

### [E2-44] — THE TWO CHARACTERISTICS

- **(1) Raise prices with flat volume?** No filed evidence, and the Google warrant is
  evidence of the opposite. Non-GAAP gross margin — the company's own measure — has gone
  **60.5% (Q3 FY2025) → 58.9% (Q2 FY2027) → guided 57.5–58.5% (Q3 FY2027)** as revenue
  doubled. Fails.
- **(2) Grow dollar volume with minor additional capital?** Capex 4.3% of revenue and
  rising, **plus ~$22bn of acquisitions to reach $8.2bn of revenue.** Fails.

**[E3-33] untapped pricing power — not claimable.** [E5-28] says the class is *"a monopoly
or a near monopoly"*; a company issuing warrants to its customer is not one.

**[E3-46] — the second question about the business is a number.** Return on capital:
GAAP operating margin **16.1%** in the best year ever filed, **negative in five of the
seven** (see the primary test at Q3). Not *"very high returns on capital employed over
time."*

### [E2-63] — DOES THE AI REVENUE ARRIVE WITH MARGIN? Tested, and the answer is "yes, at a lower rate, and falling"

The DELL run found 95¢ of every incremental AI dollar at a 5.37% gross margin. Marvell's
filed gross margins:

| | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|---|
| Revenue $M | 2,699.2 | 2,968.9 | 4,462.4 | 5,919.6 | 5,507.7 | 5,767.3 | 8,194.6 |
| **GAAP gross margin** | 50.3% | 50.1% | 46.3% | 50.5% | 41.6% | 41.3% | **51.0%** |
| data-center share of revenue | — | 35% | 40% | 41% | 40% | 72% | **74%** |

GAAP gross margin is polluted by acquired-intangible amortisation in COGS and by the FY2025
restructuring, so the company's own non-GAAP series (furnished 8-K releases) is the cleaner
test, and it runs against the AI mix:

| quarter | revenue $M | GAAP GM | non-GAAP GM |
|---|---|---|---|
| Q3 FY2025 | 1,516.1 | 23.0% (restructuring) | **60.5%** |
| Q4 FY2025 | 1,817 | 50.5% | 60.1% |
| Q1 FY2026 | 1,895 | 50.3% | 59.8% |
| Q2 FY2026 | 2,006 | 50.4% | 59.4% |
| Q3 FY2026 | 2,075 | 51.6% | 59.7% |
| Q4 FY2026 | 2,219 | 51.7% | 59.0% |
| Q1 FY2027 | 2,418 | 52.1% | 58.9% |
| **Q2 FY2027** | **2,739.3** | **53.1%** | **58.9%** |
| Q3 FY2027 guide | 3,150 ± 5% | 52.9–53.9% | **57.5–58.5%** |

**Decomposed:** from Q3 FY2025 to Q2 FY2027, revenue rose $1,223M and non-GAAP gross
profit rose ~$696M — **an incremental non-GAAP gross margin of ~57%**, against a 60.5%
base. From Q2 FY2027 to the Q3 FY2027 guide midpoint, the incremental margin is **~52%**
— and management's own words for that quarter are *"a significant acceleration in our
Custom business beginning in the second half of fiscal 2027."* **So: AI revenue arrives
with margin — it is not the DELL shape — but each incremental tranche is arriving at a
lower gross margin than the last, and the custom line that is taking over the mix is the
lowest-margin line.** GAAP gross margin rises only because a fixed $942M of amortisation
is spread over more revenue; the underlying product margin is going the other way.

### [E2-49] — METRIC-SWITCHING, DATED, AND IT FIRES

FY2026 10-K, Note 3: *"Beginning in the fourth quarter of fiscal 2026, the Company
consolidated revenue previously reported separately as enterprise networking, carrier
infrastructure, consumer and automotive/industrial end markets into a new communications
and other end market."* What those four lines showed before they were merged:

| $M | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Enterprise networking | 636.0 | 907.7 | 1,369.2 | 1,228.4 | 626.4 | — |
| Carrier infrastructure | 599.4 | 820.4 | 1,084.0 | 1,051.9 | 338.2 | — |
| Consumer | 574.7 | 700.0 | 701.1 | 622.4 | 316.1 | — |
| Automotive/industrial | 118.0 | 249.6 | 356.5 | 388.3 | 322.4 | *sold 2025-08* |
| **the four together** | 1,928.1 | 2,677.7 | 3,510.8 | 3,291.0 | **1,603.1** | *2,094.3 as one line* |

**The four lines fell 51% in FY2025 — $3,291M to $1,603M — and were merged into one line
the following year.** *"Yardsticks seldom are discarded while yielding favorable readings"*
[E2-49]. The honest counter is recorded: the automotive piece was sold in August 2025, which
is a legitimate reason to re-cut, and the merged line rose 31% in FY2026. But no reason
beyond "consolidated" is filed, and the merge removes the reader's ability to see whether
carrier and consumer — 47% of FY2021 revenue — ever recovered.

**[E4-55] recorded sweep — no physical series is filed.** "units shipped", "unit volume",
"ports", "lanes", "modules": zero hits as a metric in the FY2026 10-K. The Precision Steel
test cannot be run.

### THE COMPETITOR ROW — required **[E3-28]**

Same metric, same window, filing-sourced, most recent full fiscal year of each via SEC
XBRL. The AVGO and AMD runs built the semiconductor half; it is reused and the
connectivity/networking leg is added.

| Company | operating margin | gross margin | revenue $M | R&D % rev | SBC % rev | goodwill+intangibles % assets | period |
|---|---|---|---|---|---|---|---|
| **MRVL (subject)** | **16.1%** | **51.0%** | 8,194.6 | **25.3%** | 7.2% | **57.5%** | FY to 2026-01-31 |
| NVIDIA | **60.4%** | 71.1% | 215,938 | 8.6% | 3.0% | 11.7% | FY to 2026-01-25 |
| Broadcom — semiconductor segment | 57.6% | — | 36,858 | 9.2% | n/a | — | FY2025 |
| Broadcom — consolidated | 39.9% | 67.8% | 63,887 | 17.2% | 11.8% | 76.0% | FY2025 |
| Arista Networks | 42.8% | 64.1% | 9,005.7 | 13.7% | 4.9% | 3.6% | CY2025 |
| Texas Instruments | 34.1% | 57.0% | 17,682 | 11.8% | 2.4% | 12.5% | CY2025 |
| **Credo** *(connectivity, direct competitor)* | **33.3%** | 68.0% | 1,335.1 | 20.9% | 13.7% | 5.3% | FY to 2026-05-02 |
| Qualcomm — consolidated | 27.9% | — | 44,284 | 20.4% | 6.3% | 24.9% | FY2025 |
| Cisco | 24.3% | 64.5% | 63,325 | 15.1% | 6.0% | 51.7% | FY to 2026-07-25 |
| **Astera Labs** *(connectivity, direct competitor)* | 20.3% | **75.7%** | 852.5 | 35.7% | 18.8% | 0.0% | CY2025 |
| AMD | 10.7% | 49.5% | 34,639 | 23.4% | 4.7% | 54.4% | CY2025 |

**Peers: 10 obtained on the same metric, of the fifteen-plus Marvell names. The private
ones (Alchip, GUC are listed in Taiwan; Ayar, Lightmatter are private) are unobtainable
from the shelf and are named as such.** The row does not hold the class PROVISIONAL — the
verdict below rests on Marvell's own filings, not on the row.

**What the row shows, including the parts that cut against my prior [E4-26]:**

1. **Marvell is the second-lowest-margin business in its own competitor row.** 16.1% in
   its best year against NVIDIA 60.4%, Broadcom's chip segment 57.6%, Arista 42.8%, Credo
   33.3%. Only AMD is lower, and AMD's number is depressed by Xilinx amortisation exactly
   as Marvell's is by Inphi's.
2. **The direct connectivity competitors out-earn it at a fraction of the scale.** Credo
   earns 33.3% on $1.3bn; Astera earns a 75.7% gross margin on $853M with zero goodwill.
   Both were founded after Inphi's IPO. **The socket Marvell paid $9.9bn for admits
   entrants who reach higher margins without buying anyone.**
3. **The refuted prior, stated because [E4-26] requires it:** I expected the R&D ratio to
   be the tell of a business buying its way to relevance. It is — 25.3% is the highest in
   the row — but **Astera spends 35.7%** and earns a higher margin. High R&D is not the
   defect; low return on it is.
4. **[E2-45]'s attacker test answers itself:** the attacker already exists. Broadcom does
   custom silicon for the same hyperscalers at 57.6%; NVIDIA is the merchant incumbent the
   custom programs are built to escape and it just bought $2bn of Marvell's preferred;
   Google is the customer and holds a warrant on 6.6% of the company. **The three most
   powerful counterparties in Marvell's row hold equity or optionality in Marvell, and
   Marvell holds none in them.**
5. **[E3-61]'s limit, stated:** the row shows position, not conduct. It cannot show what
   Google, Amazon, Microsoft or Meta's silicon teams do in 2028. Those customers are not in
   the row at all, and one of them has just been granted the warrant.

### CLASS AND DIRECTION

- Needed or desired [x] · no close substitute [ ] **FAILS on the custom half (Google
  warrant; customers named as competitors); close and admits entrants on the optical half**
  · not price-regulated [x]
- Must the moat be continuously rebuilt? **Yes — by acquisition, every two years [E4-04].**
  Does success depend on a great manager? **Yes — the acquirer is the plan [E4-23].**
- Primary moat metric, filing-sourced, and its trend: **non-GAAP gross margin, 60.5% →
  58.9% → guided 57.5–58.5% while revenue doubled; and the ten-largest-customer share, 56%
  → 82%.** Both run the wrong way for a franchise.
- Class: [ ] WIDE  [ ] NARROW  **[x] NONE**  [ ] PROVISIONAL
- **Direction: narrowing** — the company is paying equity for volume, its product margin
  is declining as the custom mix rises, and its response to entrants is to buy the next
  technology.
- **VERDICT: [x] OUT.** The prior was OUT held weakly; the evidence is OUT held firmly, and
  the decisive document was not a competitor's filing but Marvell's own 8-K of 2026-08-19.
  **A business that issues a warrant on 6.6% of itself to its customer, vesting per $500M
  of that customer's discretionary purchases, has told the register who holds the pricing
  power.** [E3-03] criterion (2) is not met. The optical franchise is real and it is
  narrower than its owners' language, and it is not enough to carry a $204bn valuation on
  its own. This is the business failing, not the diligence: every document that would
  resolve it has been read.

---
⛔ **Q2 is OUT. Q3 and Q4 do not open as gates.** Per the queue's output contract and the
brief, the findings gathered for them are recorded below as **RECORD — NOT A GATE**, so the
file carries what was read; none of it can promote the name or reopen Q2.

---
## RECORD — NOT A GATE. What was read for Q3 and Q4 before Q2 closed the file.
*(The framework stops at the first non-IN verdict. The brief asked for specific documents
at Q3 and Q4 — the 8-K EX-99.1, the debt, the seven-year share count — and they were read
before Q2 was written. They are recorded so the file carries the evidence; nothing here is a
verdict, and nothing here can reopen Q2 [E2-37, E3-39].)*

### Q3 — what the filings show about honesty and rationality

**Weight case, declared for the record:** daily execution — refused (design wins are
multi-year, $8.5bn of foundry commitments are contracted); control — refused; leverage —
**argued and refused**: total debt $4,999.9M face against $3,932.8M of cash at 2026-08-01,
assets-to-equity 1.5×, and **[E2-54]'s coverage test passes at 7.1×** (FY2026 OCF $1,750.5M
less capex $354.1M less licence cash $132.8M = $1,263.6M, against cash interest paid of
$177.7M). Tangible equity is $2,311M against $16,220M of goodwill and intangibles — a
goodwill impairment would erase book equity and would not be a cash or covenant event.
**Overlay, not gate.**

**The flags [E4-22, E4-29, E5-15], each read, dated:**

| flag | 10-K (filed) | 8-K EX-99.1 (furnished) | reading |
|---|---|---|---|
| **EBITDA / non-GAAP promotion [E4-29]** | EBITDA **0**, non-GAAP **0** in the FY2026 10-K | **Every release leads with non-GAAP.** Q2 FY2027 headline: *"$0.33 GAAP diluted income per share / $0.94 non-GAAP"* — a **2.85× wedge**. Non-GAAP excludes SBC ($534M in H1), acquired-intangible amortisation ($440M in H1), restructuring, and the Celestial earnout remeasurement. | **FIRES at full strength in the furnished documents and is invisible in the filed ones** — the CGNX shape exactly. **And the wedge is paid on:** *"The fiscal 2026 AIP was based on three corporate financial metrics: revenue (50%), non-GAAP gross margin … (15%), and non-GAAP operating income margin … (35%)"* (2026 proxy). The release itself says non-GAAP is used for *"Management's determination of the achievement and measurement of certain types of compensation including Marvell's annual incentive plan."* **Corporate achievement 144.84% of target.** |
| **Trumpeted projections [E4-22 third; E5-30]** | — | Guides every quarter in dollars; raised *"our revenue outlook for both fiscal 2027 and fiscal 2028"* in the Q2 FY2027 release; Investor Day 2026-10-06 promised for *"long-term strategy."* | **Fires.** The ratchet [E5-30]. |
| **Serial share issuance [E5-15]** | Diluted weighted shares **668.8M (FY2021) → 869.7M (FY2026)**; Q3 FY2027 guided **921M**. **+37.7% in six years, AFTER $3,419.6M of buybacks (FY2020–26) and $2,040.1M in FY2026 alone.** Stock issued for Inphi/Innovium ($7,231.8M non-cash consideration, FY2022), Celestial (24.5M shares + earnout in shares), NVIDIA preferred (21.8M as-converted), Google warrant (59.0M), and SBC of $590.8M a year. | Q3 FY2027 guide adds another 21M diluted shares in one quarter. | **Fires, and it is the loudest flag in the file after the warrant.** The buyback has not reduced the count; it has slowed its growth. |
| **Dividend funded by issuance [E2-52]** | Dividend $205.1M; proceeds from employee stock plans $78.7M; **SBC $590.8M.** | — | Cash dividend is 2.6× stock-plan proceeds, so the narrow test does not fire; but the dividend is one-third of the SBC dilution it sits beside. Recorded. |
| **Restructuring as a recurring "one-time" [E3-53]** | $55.3M (FY2020), $170.8M, $32.4M, $21.6M, $131.1M, **$353.9M + ~$400M in COGS (FY2025)**, $15.5M (FY2026). Legal settlements $36.0M (FY2022), $100.0M (FY2023). | Excluded from every non-GAAP figure. | **Fires.** Seven years, seven charges. [E5-33] governs: they are real costs and they are inside every OCF-based figure in this run. |
| **Metric-switching [E2-49]** | Four end markets merged into one in Q4 FY2026 after a 51% fall (Q2 above). | — | **Fires**, dated to the FY2026 10-K. |
| **Filed-figure tells [E4-30]** | Cash taxes paid $117.5M / 14.2 / 7.9 / 95.9 / 120.6 / 40.1 / 92.1 against pre-tax income that was negative in four of seven years. | — | Cannot be run as a ratio on losses; reported growth is not smooth (operating income −243 / −258 / −348 / +238 / −568 / −720 / +1,323). Does not fire. |
| **Except-for [E2-57]** | 3 hits, incidental | non-GAAP definition runs to a paragraph | Does not fire on the words; the non-GAAP definition IS the except-for list. |

**[E4-52] — the flags converge.** Non-GAAP pay metrics + quarterly guidance + serial
issuance + a customer warrant + a director-to-CFO appointment are not five prompts; they are
one system, and it is the system [E4-52] describes.

**[E3-48] — the guidance record, demanded and produced:**

| guided in | for | guide (midpoint) | actual | beat |
|---|---|---|---|---|
| Q3 FY2025 release, 2024-12-03 | Q4 FY2025 | $1,800M | $1,817M | +0.9% |
| Q4 FY2025, 2025-03-05 | Q1 FY2026 | $1,875M | $1,895M | +1.1% |
| Q1 FY2026, 2025-05-29 | Q2 FY2026 | $2,000M | $2,006M | +0.3% |
| Q2 FY2026, 2025-08-28 | Q3 FY2026 | $2,060M | $2,075M | +0.7% |
| Q3 FY2026, 2025-12-02 | Q4 FY2026 | $2,200M | $2,219M | +0.9% |
| Q4 FY2026, 2026-03-05 | Q1 FY2027 | $2,400M | $2,418M | +0.8% |
| Q1 FY2027, 2026-05-27 | Q2 FY2027 | $2,700M | $2,739M | +1.4% |
| Q2 FY2027, 2026-08-27 | Q3 FY2027 | $3,150M ± 5% | pending 2026-12 | — |

**Seven for seven, every beat between 0.3% and 1.4%, on a business growing 37–63%.** The
same shape as Broadcom's three-for-three. Not the [E4-30] fraud shape (results are lumpy);
unambiguously the [E5-30] ratchet.

**The primary test [E2-01], and why its denominator is refused [E2-47, E2-43]:**

| FY | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|
| Equity $M | 8,678.6 | 8,435.8 | 15,702.1 | 15,637.2 | 14,831.4 | 13,427.0 | 14,308.4 |
| Net income $M | 1,584.4 | −277.3 | −421.0 | −163.5 | −933.4 | −885.0 | 2,670.1 |
| **ROE** | 18.3%* | −3.3% | −2.7% | −1.0% | −6.3% | −6.6% | 18.7%* |

*\*Both positive years are disposals: FY2020 carries a $1,122M Wi-Fi gain and a $786M tax
benefit; FY2026 carries the $1,830M Infineon gain. **On the business, ROE has been negative
in every one of the five clean years.*** Equity nearly doubled in FY2022 by stock issuance
for Inphi, which is [E2-47]'s carve-out. **[E2-43] run on FY2026:** tangible assets $9,468M
less non-interest-bearing current liabilities $2,721M = **$6,748M net tangible operating
assets** (ex-cash $4,109M); pre-tax operating income $1,322.9M = **19.6%** (32.2% ex-cash).
**And the wedge, reported separately as [E2-43] demands:** goodwill plus intangibles of
$12,817M — on what was *paid* (~$19.6bn of tangible plus purchased), the return is **6.8%**.
[E2-73]'s two denominators give two different verdicts: the engineers earn a decent return
on the assets they work with; the acquirer has earned 6.8% on what he paid for them.

**Capital allocation [E5-08, E4-31] — recorded, not scored:**
- (1) ample funds — yes, on cash and the undrawn $1.5bn revolver.
- (2) material discount — **$2,040.1M repurchased in FY2026 and $400M in H1 FY2027**
  against a conservative value below $20 a share (computed below). The FY2026 average
  repurchase price cannot be read from the cash-flow statement alone; the count fell from
  866.1M to 848.1M between March and November 2025 while $2.0bn was spent, implying a
  price in the $70–80 range — still several times the conservative case. **Stated with the
  humility clause [E4-13]:** the register at $227 has since proved the board right on the
  quote and this run wrong on the quote; the run's claim is about value, not price.
- **(3) [E4-31] — an informed register?** The AIP pays on non-GAAP gross margin and
  non-GAAP operating margin; the release reconciles them for the current quarter only and
  refuses reconciliation for forward periods (*"cannot be provided without unreasonable
  effort"*). The register can compute the metric after the fact and cannot compute the
  guided one. Partial.
- **[E2-30] institutional imperative:** (2) *"projects or acquisitions will materialize to
  soak up available funds"* — $2.5bn from Infineon (Aug 2025) and $2.0bn from NVIDIA (Mar
  2026) arrived; $3.5bn went to Celestial (Feb 2026) and $270M to XConn. **Fires.** (4)
  peer imitation — the custom-XPU model is Broadcom's, and the "AI revenue" narrative is
  Broadcom's. Recorded.
- **[E3-58] — delegation:** four acquisitions in eight years, all banker-led. Recorded.
- **The people, dated:** CEO Matthew Murphy since 2016, FY2026 total $25.1M, pay ratio 158:1.
  **Sandeep Bharathi, President of the Data Center Group, was paid $48.4M in FY2026**
  ($46.2M in stock) — nearly twice the CEO. **CFO Willem Meintjes resigned 2026-06-10
  (8-K 2026-06-11), effective five days later, and was replaced the same day by Daniel
  Durn, who resigned from the Board and from the chair of the Audit Committee to take the
  job.** The 8-K says the resignation *"is not the result of any disagreement."* An
  audit-chair-to-CFO move at a company with a 2.85× GAAP/non-GAAP wedge is recorded as a
  prompt to read, never a verdict [E5-38]. **An Executive Retirement Program was adopted
  2025-05-28** with continued PSU vesting after retirement. **Integrity: no disqualifier
  found.** Nothing in this section promotes the name.

### Q4 — what the filings show about survival

**Owner earnings — see the computation block.** The five-year default window at the judged
(c) is **$397M**; the range across windows and (c) ends is **−$517M to +$901M**. **The range
crosses zero on every multi-year window, and [E4-25]'s rule is that this IS the finding:**
the constructions disagree about whether the business has ever earned anything, and the
disagreement is the $942M–$1,098M a year of amortisation on $22bn of purchased technology.

**Great, good, or gruesome [E4-20]?** *"grows rapidly, requires significant capital to
engender the growth, and then earns little or no money."* Revenue 3.0× in seven years; $22bn
of acquisitions plus rising capex to get there; GAAP operating loss in five of seven years
and a 16.1% margin in the seventh. **[E4-43]'s caveat is applied:** the *good* class passes,
and the TTM figure of $901M on $6.7bn of net tangible operating assets would be good — if
the $22bn were not the capital that engendered it. **On what was paid, this is the gruesome
account.** On the underlying assets, it is good. The framework's own instruction [E2-73] is
to pick the denominator by the question, and the question at Q4 is the owner's: **gruesome.**

**Staying power [E5-11] — all three, scored on the worst case [E2-55]:**
- **(1) a large and reliable stream of earnings — FAILS on "reliable."** GAAP operating
  income was negative in five of seven years; two customers are 61% of revenue.
- **(2) massive liquid assets — passes narrowly.** Cash $3,932.8M against $4,999.9M of
  senior notes; net debt ~$1.07bn; $1.5bn revolver undrawn; no financial covenants on the
  notes. Marvell **factors receivables** (*"higher factoring fees for the sales of
  receivables"*, FY2025 MD&A) — recorded because the cash figure is partly borrowed from
  tomorrow's receipts.
- **(3) no significant near-term cash requirements — FAILS.** At 2026-08-01: **$8,518.9M of
  unconditional purchase commitments to foundries and test partners** ($1,829.3M in the
  rest of FY2027, $2,125.4M in FY2028, $2,178.3M in FY2029, $2,201.8M in FY2030), plus
  **$666.3M of technology-licence fees**, **$351.6M of capex commitments**, a **Celestial
  earnout marked at $749.5M** payable in cash and shares through FY2029, and **$1,249.9M of
  notes due in 2028**. Against OCF of ~$2.2bn trailing. The foundry commitments are
  cancellable only *"with payment of all costs and expenses incurred through the date of
  cancellation … loss of amounts paid in advance, or loss of priority to reserved capacity."*
  **This is [E5-39]'s kindness-of-strangers structure: the capacity is reserved against
  revenue that two customers have not yet ordered.**
- **Leverage, named and quantified [E4-16, E3-29]:** debt 2.9× FY2026 OCF; 2.2× tangible
  equity; the notes are covenant-free and laddered 2028–2036 at 2.45–5.95%. Not the
  Russian-roulette class. The leverage that matters is **operational** — the $8.5bn of
  committed wafers.
- **Jurisdiction:** 36% of FY2026 revenue shipped to China, 20% to Taiwan; the 10-K names
  export licences and customers' *"ability … to develop their own solutions"* as the
  linked risk.

**The named way this business dies [E2-27, E3-24, E4-51] — the bear case as its holders
would state it:**
- **The mechanism:** the two customers that are 61% of revenue in-source, second-source,
  or re-bid the custom programs at the next generation — the outcome the 10-K itself
  forecasts (*"some of our customers have chosen to develop certain semiconductor products
  internally and this trend may continue to proliferate"*) — while the foundry commitments
  written against those programs come due. Broadcom, Alchip and GUC bid the same sockets;
  the customer owns the architecture.
- **Quantified from filed figures:** Distributor A was **44% of Q2 FY2027 revenue ≈
  $1,205M a quarter**. Lose half of that channel over a program transition — **~$2.4bn a
  year at a ~55% gross margin = ~$1.3bn of gross profit** — and the loss exceeds FY2026's
  entire operating income of $1,322.9M; the company is back to a GAAP operating loss with
  $2.1bn of committed wafers falling due in the same year. **The Google warrant makes the
  exposure legible: Marvell has priced the retention of its custom customer at 6.6% of
  itself, and the vesting is at the customer's discretion.**
- **Likelihood:** **a real possibility** — not a low-level one. The company's own
  Competition section says the trend *"may continue to proliferate"*; two customers hold
  61%; every program is re-competed; the merchant incumbent (NVIDIA) and the strongest
  custom competitor (Broadcom) both out-earn Marvell by 40 margin points. **[E4-40] —
  exposure, not experience:** the seven-for-seven guidance record is the benign loss history
  late in a good cycle; the exposure is the concentration table.

**The seven-year share count, as the brief asked:** diluted weighted shares **676.1M
(FY2020) → 869.7M (FY2026), +28.6%**; from the pre-Inphi base **668.8M (FY2021) → 921M
guided for Q3 FY2027, +37.7%** — after **$3,419.6M of repurchases**. Every dollar of buyback
bought back a share that had already been issued for an acquisition, an award, or a
customer.

---
## COMPUTATION — NOT A CLEARANCE: THE VALUE BAND
*(operator rule 3. The queue's output contract requires a price and a band either way. Q2 is
OUT; this carries no entry language and no ranking.)*

**One book. Owner earnings against the bond [E4-01, E3-42] — the bare sovereign, 5.37%, no
per-name premium.**

| owner-earnings construction | $M | ÷ 5.37% = zero-growth value | per economic share (898.7M) | ÷ 10% floor [E4-28] | per share |
|---|---|---|---|---|---|
| capex + licence end, 5-yr (the judged (c), corpus default window) | 397 | $7.4bn | **~$8** | $4.0bn | ~$4.40 |
| capex end, 5-yr | 550 | $10.2bn | ~$11 | $5.5bn | ~$6 |
| capex end, 3-yr (the screen's `oe_top`) | 676 | $12.6bn | ~$14 | $6.8bn | ~$7.50 |
| **TTM capex end (the most generous figure that exists)** | **901** | **$16.8bn** | **~$19** | **$9.0bn** | **~$10** |
| D&A end, any multi-year window | negative | — | — | — | — |

Net debt of ~$1.07bn (cash $3,932.8M less notes $4,999.9M) is ~$1.20 a share and is not
netted above; netting it lowers every figure.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]: roughly $8 to $19 a share at the bare
sovereign with zero growth; roughly $4 to $10 at the ~10% floor. Current price $226.96.
The price is 12× to 28× the range.**

**What the price already assumes [E4-35, E4-44] — the expectancy test, so the growth belief
is faced in writing:** a buyer at $203,964M who receives the most generous trailing figure
($901M) and sees it compound at **30% a year for ten years** (to $12.4bn), then sells at the
sovereign's 18.6× with all interim cash collected, earns roughly **3% a year**. At **40% a
year for ten years** (to $26.1bn) the return reaches roughly **10–11%** — the floor. **The
[E4-28] floor at this price requires forty per cent compound growth in owner earnings for a
decade, from a base that has been negative on the conservative construction in every year
the company has filed.** [E4-35]'s base rate — fewer than one in twenty of the best
businesses sustain 15% for twenty years — is the answer.

**The ceiling [E2-63]:** bounded by hyperscaler capex and by the customers' own silicon
teams; Marvell's product margin is already falling as the custom mix rises.

**No bar is applied and no margin is stated**, because Q2 is OUT and Bar 1/Bar 2 are Q5
apparatus. **Windage count: zero** — every figure above is the unstripped, most generous
construction, and the conclusion does not need conservatism to hold.

---
## Q5, Q6 — NOT OPENED. Q2 is OUT.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, Q2 OUT, file closed; Q3/Q4
      material recorded below the gate and headed as such
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1 rests on
      the FY2026 10-K and Q2 FY2027 10-Q
- [x] Every UNRESEARCHED verdict names the artifact — none issued
- [x] Every UNKNOWABLE verdict states what cannot be known — none issued
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026
      OCF $1,750.5M against the filed cash-flow statement; the D&A tag cross-check FAILED and
      is recorded)
- [x] Owner earnings on a multi-year mean; windows stated (3/5/7/8-yr and TTM); (c) disclosed
      as a judgment with direction stated
- [x] Competitor row filled — 10 of 15+ named; private/Taiwan-listed peers named as unobtained
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-10
- [x] Value stated as a round-number range, headed COMPUTATION — NOT A CLEARANCE
- [x] One bar chosen — none applied, stated why; windage count stated (zero)
- [x] Prices dated; aggregator used for live quotes only and flagged
- [x] Run committed to git, by file name, after each gate
- **Operator rule 6 addendum:** the run was started 2026-09-07 at $223.55 / 5.24% and
  completed 2026-09-11 at $226.96 / 5.37% after two session kills; Step 0 records both
  strikes and every figure below Step 0 uses the fresh pair.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- One line: **Marvell is a serial acquirer of chip-design teams that has bought ~$22bn of
  technology to reach $8.2bn of revenue, has never earned a positive owner-earnings figure
  on the conservative construction, has concentrated 82% of its revenue in ten customers
  and 61% in two, and in August 2026 issued a warrant on 6.6% of itself to its largest
  custom customer, vesting per $500M of that customer's discretionary purchases — the
  filing's own statement of who holds the pricing power. Q2 OUT; price $226.96 against a
  computed band of roughly $8–$19.**
- **The reversal condition, in words (the QLYS ruling — no price alert on a business
  failure):** Q2 reopens only on filed evidence that the custom-silicon customers regard
  Marvell as having no close substitute — concretely, (a) a filed multi-year supply
  agreement with take-or-pay terms running *toward* Marvell rather than a warrant running
  toward the customer; (b) the ten-largest-customer share falling below 60% with revenue
  still growing; and (c) non-GAAP gross margin rising, not falling, through the custom
  ramp. Any one is a document; all three are needed.
- **The strongest fact against this verdict, stated because [E4-51] requires it:** the
  optical-DSP franchise is real, has compounded at ~50% for five years, is half of
  data-centre revenue, and its two visible merchant competitors (Credo, Astera) are a
  tenth of Marvell's size. NVIDIA and Google, who could each build or buy what Marvell
  sells, chose instead to put $2bn of preferred and a seven-year commercial agreement into
  it. If the custom business is a low-margin door-opener for a high-margin interconnect
  franchise that the hyperscalers have decided not to build themselves, the concentration
  is a feature of the customer base, not a defect of the product, and Q2 is NARROW rather
  than NONE. **The run's answer:** the same documents show the product margin falling as
  that door opens, and the counterparties took equity rather than paying price — but it is
  the closest thing in the file to a case for the other side, and it is on record.
