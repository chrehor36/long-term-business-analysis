# Company Run — ARM HOLDINGS PLC (ARM) — 2026-09-11 (written 2026-09-12)
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

*Run opened 2026-09-11 and killed by the session limit before the file existed; resumed
2026-09-12 with the research reads intact. Sovereign and price re-struck on resumption per
operator rule 5; the brief's 5.37% (2026-09-10) is not used. Research folder:
`Test Runs/_research 2026-09-11 ARM/` (filing dumps pattern-ignored; the FY2026 20-F dump
and the IP-peer row are reused from `Test Runs/_research 2026-09-07 SNPS/`).*

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
- **rate 5.35%** · **date 2026-09-11** · source: **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`tools/sources.py`, struck 2026-09-12 on resumption). The
  brief carried 5.37% of 2026-09-10; the rate moved −2bp overnight and the fresh figure is
  used everywhere below.
- **Earnings currency: USD.** Arm is an English plc filing on Form 20-F as a foreign private
  issuer, but it reports in US dollars and its revenue is dollar-denominated: *"Less than 2%
  of our total revenue is denominated in currencies other than U.S. dollars, and the impact
  of changes in foreign exchange rates on our revenue … was immaterial"* (FY2026 20-F, Item
  5.A). Roughly two-thirds of the cost base sits in the UK, Europe, India and Asia (Item 4.D
  facilities), so sterling and rupee wages are an **exposure**, not a repricing of the
  earnings currency; the USD sovereign is the right one and no FX conversion is needed.
- **ADS ratio 1:1** — *"American depositary shares, each of which represents the right to
  receive one ordinary share"* (20-F, forward-looking-statements preamble; restated in the
  2026-08-10 AGM 6-K: *"each representing one Ordinary Share"*). **The ordinary shares are
  not listed anywhere**: *"Our ADSs have been traded on the Nasdaq Global Select Market …
  since September 14, 2023. Our ordinary shares are not listed on any exchange"* (Item 9.A).
  The ADS quote is therefore the only quote.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Form 20-F, FY ended 2026-03-31, filed 2026-05-26, accession `0001973239-26-000097`**,
  primary document `arm-20260331.htm` — the anchor annual document. Read: Item 3.D risk
  factors (customer concentration, competition, Qualcomm litigation, production silicon,
  controlled-company risks), Item 4.B (business model, licence types, royalty mechanics,
  competition, Arm China IPLA, organisational structure), Item 5 (MD&A, cash flows,
  contractual obligations, trend information, critical estimates), Item 6.B (remuneration
  policy and the CEO's single figure), Item 7 (major shareholders, SoftBank governance
  agreement, related-party policy), the four statements and Notes 1 (policies), 4 (revenue),
  8 (PP&E), 15 (share-based compensation), 18 (commitments), 20 (related parties), 21
  (segment), 22 (subsequent events).
- **Form 20-F, FY2025, filed 2025-05-28, accession `0001973239-25-000016`** and **Form 20-F,
  FY2024, filed 2024-05-29, accession `0001973239-24-000012`** — the two prior vintages, read
  for the FY2025-vs-FY2024 MD&A comparison, the two quarterly chip-shipment counts, and the
  Qualcomm litigation as it stood before the verdict.
- **Form F-1, filed 2023-08-21, accession `0001193125-23-216983`** — the IPO prospectus, read
  for the **only filed annual chips-shipped series** (FY2021–FY2023) and the pre-IPO
  revenue split.
- **Form 6-K, quarter ended 2026-06-30, furnished 2026-07-29, accession
  `0001973239-26-000114`** — **the current perimeter document** (Q1 FY2027 condensed
  statements, MD&A, litigation update, DreamBig closing). Every level-setting balance-sheet
  figure below is taken from it.
- **Form 6-K earnings letters** (EX-99.2), six consecutive: Q4 FY2025 `0001973239-25-000010`
  · Q1 FY2026 `-25-000023` · Q2 FY2026 `-25-000042` · Q3 FY2026 `-26-000005` · Q4 FY2026
  `-26-000062` · Q1 FY2027 `-26-000113`; the **Arm Everywhere 6-K of 2026-03-24**
  (`-26-000050`, the AGI CPU launch and the long-range expectations); the AGM 6-Ks of
  2026-08-10 and 2026-09-10. *The brief's instruction to pull the release before scoring Q3
  was followed for all six letters; the finding is at Q3.*
- **Figure cross-checked against the filed statement:** *Net cash provided by (used for)
  operating activities*, FY2026 Consolidated Statements of Cash Flows, **$1,524 million** —
  agrees with the XBRL `NetCashProvidedByUsedInOperatingActivities` 1,524,000,000 and with the
  MD&A cash-flow summary table; *Share-based compensation cost* **$1,052** and *Purchases of
  property and equipment* **$(545)** likewise to the million. The Note 21 single-segment
  cost build reproduces operating income to the million: 4,920 − 1,674 − 1,052 − 160 − 881 −
  100 − 150 − 3 = **900**. Equity recomputed from A − L [E5-32]: 10,703 − 2,417 = **8,286**,
  as filed.

**Price and shares:**
- **price $264.79**, 2026-09-11 close (aggregator via `tools/run.py` — **live quote only,
  flagged** per operator rule 5). ADS = one ordinary share, so no ratio conversion.
- **shares 1,068,078,760** — the count the registrant itself uses: *"The percentage of
  ordinary shares beneficially owned as of May 21, 2026 is based on 1,068,078,760 ordinary
  shares outstanding"* (20-F Item 7.A). The Q1 FY2027 balance sheet shows **1,068 million
  issued and outstanding at 2026-06-30** (rounded), consistent. `python
  Screens/cover_shares.py ARM` returned **1,064,055,252 as of 2026-03-31** — the 20-F cover
  count; the 4.0M step to May is vested awards net of withholding. The later, precise count
  is used. **Single class; no split** in the company's history as a listed ADS.
- **Market cap $282,817M** (1,068,078,760 × $264.79). The brief's `cap_m 249861` was struck
  at ~$234.8 on the 1,064M basis; the construction is the same and the price moved.
- **What SoftBank's holding does to the float and the quote.** *"As of May 21, 2026, SoftBank
  Group beneficially owns approximately 922,733,999 or 86.4% of our total issued and
  outstanding share capital … As such, our publicly traded ADSs, representing ordinary
  shares, is 145,344,760."* The brief's "~90%" is **86.4%**, and the public float is
  **145.3M ADSs ≈ $38.5bn at $264.79 — 13.6% of the cap.** Two consequences, both filed:
  (1) *"769,029,000 of our ordinary shares that are beneficially owned by SoftBank Group,
  representing a 72.0% equity interest in us, were pledged as security under the SoftBank
  Group Facility"* — a margin loan on which *"the providers … may … exercise their rights to
  foreclose on and sell or cause the sale of our shares that may be pledged as collateral.
  The foreclosure … could cause a change of control of us."* The quoted price is set on a
  13.6% float while 72% of the company is collateral for the parent's borrowing; the
  $282.8bn cap is 7.3x the value of the shares that actually trade. (2) SoftBank holds
  pre-emptive rights on every issuance except employee plans it approves, designates seven
  director candidates, and *"[e]ach of our non-executive directors were designated by
  SoftBank Group"* (Item 6.C). Recorded here; weighed at Q3 as the control case.

---
# STAGE 0 — THE SCREEN ROW, REBUILT BY HAND, AND THE LINE THAT CONSUMES EVERYTHING

**Construction, as everywhere in this queue:** owner earnings = **OCF − SBC − capex** (one
end) and **OCF − SBC − D&A** (the other), $M, every figure the filed cash-flow statement
line (FY2024–FY2026 from the FY2026 20-F; FY2022–FY2023 from the FY2024 20-F and F-1, which
carry identical values in every later vintage — no restatements in the series). Five fiscal
years exist because the company listed in September 2023; the FY2022–FY2023 columns are
**pre-IPO** and the compensation basis differs (below).

| FY (Mar) | revenue | licence | royalty | OCF | **SBC** | employer tax on SBC (in opex, cash) | D&A | capex (PP&E) | intangibles bought + obligations paid | **OE (capex end)** | OE (D&A end) | withholding tax paid on vesting (financing) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022 | 2,703 | 1,141 | 1,562 | 458 | 26 | — | 185 | 34 | 41 + n/f | **398** | 247 | 0 |
| 2023 | 2,679 | 1,004 | 1,675 | 739 | 79 *(expense 326)* | — | 170 | 64 | 29 + n/f | **596** | 490 | 0 |
| 2024 | 3,233 | 1,431 | 1,802 | 1,090 | **1,037** | 176 | 162 | 92 | 51 + 40 | **−39** | −109 | 158 |
| 2025 | 4,007 | 1,839 | 2,168 | 397 | **820** | 224 | 183 | 219 | 20 + 59 | **−642** | −606 | 120 |
| 2026 | 4,920 | 2,307 | 2,613 | 1,524 | **1,052** | 160 | 249 | 545 | 30 + 67 | **−73** | 223 | 529 |
| **TTM to 2026-06-30** | 5,156 | 2,413 | 2,743 | **2,094** | **1,154** | 200 | 264 | 588 | 34 + 75 | **352** | 676 | 722 |

*TTM = FY2026 + Q1 FY2027 − Q1 FY2026 from the two 6-K statements; the letter's own TTM OCF
is $2,094M and TTM capex $588M, matching. "n/f" = the financing line "Payments of
intangible asset obligations" was not separately presented pre-IPO. FY2023 SBC: the cash-flow
add-back is $79M but the P&L charge was $326M (XBRL `AllocatedShareBasedCompensationExpense`),
because pre-IPO awards were **liability-classified** — *"Certain fixed monetary amount
liability-classified awards were modified to equity-classified awards at the time of IPO"*,
and $343M was reclassified into equity at listing. The add-back is the right subtraction in an
OCF-based construction (the cash-settled part already reduced OCF); `tools/run.py` subtracts
the $326M charge and gets a five-year band of −73 to 58; both are shown and neither changes a
verdict.*

## THE LINE BETWEEN OCF AND OWNER EARNINGS THAT CONSUMES EVERYTHING — cross-checked to the dollar

The brief's prior was SBC first, capitalised development second. **SBC is the line, and it is
not close; capitalised development is not a factor at all.**

1. **Stock compensation, from the filed reconciliation:** $1,037M · $820M · $1,052M for
   FY2024–FY2026 — **$2,909M against three years of OCF totalling $3,011M. Stock paid to
   employees consumed 96.6% of operating cash flow over the whole post-IPO record.** Before a
   dollar of capex, the three-year mean of OCF − SBC is **$34M a year** on a $282.8bn cap.
2. **Capitalised development does not exist on this filer.** Note 1: *"The Company has not
   historically capitalized software development costs for software to be sold, leased or
   otherwise marketed … these development costs are generally recognized as incurred in
   research and development expenses."* What is capitalised is **internal-use software**:
   $68.8M · $86.2M · $173.6M (FY2024–26), of which SBC $3.8M in FY2026 — it is inside
   "Purchases of intangible assets" ($30M) and PP&E, and it is a rounding error against
   $1,052M of stock. Recorded because the brief asked; refuted as a cause.
3. **The two series disagree because one is before the stock and one is after it [E4-25].**
   OCF rose 1,090 → 397 → 1,524 (the screen's "STEP UP 1.68" is the FY2025 trough, which was
   working capital: contract assets −$412M, receivables −$331M, and −$381M of *"other
   liabilities"* — the employment-tax payable on vested shares unwinding). Owner earnings went
   −39 → −642 → −73. The screen refused the OE ratio because the recent years crossed zero;
   the honest words are: **operating cash flow is what the customers pay; owner earnings is
   what is left after the employees are paid in shares, and on this filer that is nothing.**
4. **The cash evidence that the stock is real money, below OCF.** Since FY2026 the company
   settles employees' tax on vesting by withholding shares and paying the tax itself:
   *"Payments of withholding tax on vested shares $(529)"* in FY2026 financing, *"resulting
   from the shift to a full withhold-to-cover method"*; **$278M more in the single quarter to
   June 2026**, *"resulting from changes in share price."* The equity statement shows it as
   5M shares withheld for $585M — the company bought $585M of its own stock from its
   employees at market and retired nothing net, because it issued 11M + 1M new shares the
   same year. This line is **not** double-subtracted below (it is the cash form of part of
   the SBC already subtracted) — it is cited as [E3-70]'s market-value evidence: the accounting
   charge is the floor, and the cash the company actually paid to settle a fraction of the
   awards ran at 56% of the charge.
5. **Employer taxes on the stock are a further cash cost inside OCF**: $176M · $224M · $160M
   (Note 21), i.e. the true cost of paying in stock is the charge plus ~15–27% of it in
   payroll tax, all of which the non-GAAP measures also remove (Q3).

## SBC ÷ OCF — placed in the calibrated row

| name | SBC/OCF | file outcome |
|---|---|---|
| **ARM FY2025** | **206.5%** ($820M / $397M) | — |
| **ARM 3-year FY2024–26** | **96.6%** ($2,909M / $3,011M) | this file |
| **ARM FY2024** | **95.1%** | — |
| **ARM FY2026** | **69.0%** ($1,052M / $1,524M) | — |
| PINS | 68.6% | — |
| CRWD | 68.0% | closed the file |
| **ARM TTM to Jun-2026** | **55.1%** ($1,154M / $2,094M) — the best reading in the record, and it rests on a quarter whose OCF the letter itself says *"benefit[ed] from favorable timing of receivables collections and tax payments"* (+$389M receivables, +$370M payroll-tax payable) | — |
| QLYS | 24.9% | — |
| CRM | 23.4% | — |
| SHOP | 22.1% | — |

**Arm's best full year (69.0%) sits above the reading that closed CRWD; its three-year figure
(96.6%) is the highest this queue has recorded, and its FY2025 figure (206.5%) means the
company paid its people more than twice its operating cash flow in stock.** Per employee
(9,584 at 2026-03-31): $1,052M of stock is ~$110,000 a head on top of $1,674M of cash pay.

## THE WIDTH, rebuilt over every available window and both (c) ends — in dollars and a word

Cap **$282,817M**; sovereign 5.35%.

| window | capex end | yield | D&A end | yield | word |
|---|---|---|---|---|---|
| FY2026 alone | −73 | −0.03% | 223 | 0.08% | nothing |
| **3-yr FY2024–26 (the clean post-IPO record)** | **−251** | **−0.09%** | **−164** | **−0.06%** | **less than nothing** |
| 5-yr FY2022–26 *(corpus default [E2-42], but two pre-IPO years on a different pay basis)* | 48 | 0.02% | 49 | 0.02% | nothing |
| 5-yr, `run.py` construction (P&L SBC charge) | −73 | −0.03% | 58 | 0.02% | nothing |
| **TTM to 2026-06-30** | **352** | **0.12%** | 676 | 0.24% | a rounding error, timing-flattered |
| Company's own FCF ($882M FY2026 = OCF − PP&E − intangibles − intangible obligations) **less SBC** | **−170** | −0.06% | — | — | the company's own definition, after paying its people, is negative |

- **Width: −$642M (FY2025) to +$676M (TTM, D&A end) — $1.3bn wide, centred on zero, against
  a $282.8bn market capitalisation.** In words: **over every window this filer has filed,
  the owners' share of the cash is between minus six hundred million and plus seven hundred
  million dollars a year, and the market pays two hundred and eighty-three billion for it.**
  The screen's "n/a — negative bottom" is correct, and the reason is one line: stock.
- **Which (c) end is valid.** Depreciation is $122.6M (Note 8) inside D&A of $249M; capex was
  $545M, 2.2x D&A, *"driven by data center and office expansions and computer hardware
  purchases"*, and net PP&E doubled in a year (354 → 772) as the AGI CPU programme began.
  This is growth capacity for a business that has just entered production silicon [E5-20]'s
  exception does not literally apply (the filing does not say depreciation understates
  renewal) — but the FY2026 capex is not maintenance either. **(c) is judged at ~$400M/yr**,
  disclosed: above D&A because the R&D that defends the moat now needs data-centre compute
  the old business did not, below FY2026 capex because part of it is the silicon build-out.
  **It does not matter to the verdict: the sign is set by SBC, and even at (c) = 0 the clean
  window earns $34M.**

## [E4-41] — the level-shift, adjudicated

The OCF flag says STEP UP 1.68; the OE flag refused. Both are right about their own line. The
step in OCF is real (revenue $2.7bn → $4.9bn in four years, 23% in FY2026) and the *favourable
exogenous break* to be named and removed is the one the FY2025 and FY2026 letters name
themselves: the Armv9 and CSS mix lifting royalty per chip while units were flat (Q1) and
**$704M of licence revenue from an affiliate of the controlling shareholder** that did not
exist two years earlier (Q3). Normalised for neither, owner earnings are zero; normalised
for both, they are lower.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, without management's language.** Every processor speaks
a language — the list of instructions software can ask it to execute. Arm owns the most
widely spoken one. It does not make chips; it writes the language (the architecture) and
sells finished designs of processors that speak it (cores, GPUs, interconnect, and since
2024 pre-assembled "compute subsystems"). A chip company pays twice: **a licence fee** up
front for the right to use a design or, for a few, the right to write its own processor in
Arm's language, and then **a royalty on every chip it ships** for as long as it ships them —
a percentage of the chip's selling price or a fixed number of cents, with a contractual
floor, rising as more Arm blocks go into the chip. Because a design licensed in 2005 can
ship in a thermostat in 2026, the royalty stream has a very long tail: *"approximately 46%
of our royalty revenue for the fiscal year ended March 31, 2023 came from products released
between 1990 to 2012"* (F-1). The cost of the business is engineers: 84% of 9,584 employees
are in research and design; cost of sales is 2.5% of revenue; gross margin 97.5%. **As of
March 2026 the company added a third way to be paid: it now designs and sells a finished
data-centre chip of its own (the "Arm AGI CPU", made at TSMC), competing in the market its
licensees serve.**

Where the revenue comes from and where it goes, FY2026, as filed (Item 5.A; Note 4; Note 21):

| | $M | % |
|---|---|---|
| Royalty revenue | 2,613 | 53 |
| Licence and other revenue | 2,307 | 47 |
| **Total revenue** | **4,920** | 100 |
| of which **from related parties** (Arm China $791M; a SoftBank affiliate $704M; Ampere $4M) | **1,499** | **30** |
| of which from **external customers** | 3,421 | 70 |
| Cost of sales | 121 | 2.5 |
| Staff cash pay | 1,674 | 34 |
| **Staff stock pay + employer tax on it** | **1,212** | **25** |
| Non-staff costs, D&A, other | 1,134 | 23 |
| Operating income (GAAP) | 900 | 18.3 |
| Non-GAAP operating income (before stock, its taxes, and deal items — the number the CEO is paid on) | 2,115 | 43.0 |

**Three facts in that table govern the file.** Stock is a quarter of revenue; **thirty
percent of revenue comes from parties related to the controlling shareholder**, up from 21%
a year earlier; and the gap between the number management is paid on and the GAAP number is
the stock.

**The scarce input this business controls.** The instruction set plus the software that
speaks it — *"more than 22 million developers"*, every mobile operating system, *"greater
than 99%"* of smartphone application processors *"for many years"*. A rival architecture
needs not a better processor but a recompiled world. That is the input a competitor cannot
buy, and it is why the royalty tail runs to designs from the 1990s.

**Will the fundamentals look broadly the same in ten years?** For the **licensing and
royalty model, yes** — it is the same model as in 1998, and the tail is filed. For the
**company, the registrant says no, in its own words**: *"our expansion into production
silicon may have materially different margin profiles, revenue recognition characteristics,
and sales cycles compared to our IP licensing business"* (Item 5.D); *"Unlike our IP
licensing model, we now face exposure to risks relating to transitioning to advanced process
nodes; competing against established production silicon companies; … managing product
transitions and inventory across generations"* (Item 3.D); and *"many of our customers who
have historically licensed our IP may face direct competition from us"* (Item 4.B). The
CFO's stated forecast for that business is $15bn (Q4 FY2026 letter: *"We are on track towards
our forecast of $15 billion in this business as stated at our Arm Everywhere event"*) — three
times FY2026 revenue, from a product with $0 of filed revenue. [E3-31]: *"If a business is
complex or subject to constant change, we're not smart enough to predict future cash flows."*

**Is it "relatively simple and stable in character"?** The filed business is simple and
legible: two revenue lines, one segment, a filed related-party split, a filed geographic
split, a filed licence-type taxonomy, and — uniquely in this queue — **a filed physical unit
series and filed statements of what moved royalty per unit.** What is not stable is the
perimeter: the registrant is converting, by its own description, from a licensor into a
licensor-plus-chip-vendor, and none of the second thing's economics is filed yet. Q1 is
held IN on the filed business; the silicon entry is carried to Q2 (it competes with the
customers who are the moat) and Q4 (it is why capex doubled) rather than used to close Q1
on a prospective fact.

### [E4-55] — the unit series, and [E2-63] — units or price?

**The only filed annual chips-shipped series is in the IPO prospectus, and the registrant
stopped filing it the quarter after it turned down.**

| period | chips reported shipped | source | royalty revenue | **royalty per chip** |
|---|---|---|---|---|
| FY2021 | 25,281M | F-1 KPI table | n/f in F-1 table read | — |
| FY2022 | 29,190M | F-1 | $1,562M | **$0.054** |
| FY2023 | 30,583M | F-1: *"more than 30 billion … in the fiscal year ended March 31, 2023 alone, representing an approximately 70% increase since the fiscal year ended March 31, 2016"* | $1,675M | **$0.055** |
| Q1 FY2024 vs Q1 FY2023 | 6,844M vs 7,314M (**−6.4%**) | F-1 KPI table — the last quarter the KPI was published | — | — |
| Q4 FY2024 | *"approximately 7 billion"* | FY2024 20-F, Item 4.B | Q4 royalty ≈ $514M (Q4 FY2025 letter: $607M, "rose 18%") | **≈ $0.073** |
| Q4 FY2025 | *"approximately 7.9 billion"* | FY2025 20-F, Item 4.B | $607M | **≈ $0.077** |
| FY2026 | **not filed** — cumulative only: *"more than 350 billion … cumulatively"* | FY2026 20-F | $2,613M | not computable |

- The F-1 filed *"Number of chips shipped"* as a **key performance indicator**, with the
  reason: *"The number of chips shipped also provides insight into chip pricing and volumes
  in different end markets."* The quarterly letters since listing carry ACV, RPO and
  licence counts but **no unit count**; the 20-Fs give a single fourth-quarter figure
  (FY2024, FY2025) and then none. The yardstick was dropped at the first quarter it fell
  [E2-49] — scored at Q3.
- **Revenue growth is price, not units, and the filing says so.** FY2023 → FY2025: royalty
  +29% ($1,675M → $2,168M) while the fourth-quarter unit run-rate went 7.3bn → 7.9bn (+8%
  over two years, and Q1 FY2024 was down 6%). FY2026 royalty +21%: *"driven by an improved
  mix of products with higher royalty rates per chip, such as Armv9 technology"* — units are
  not mentioned as a driver at all in the FY2026 MD&A (FY2025's said *"higher chip shipments
  and an improved mix"*). The Q4 FY2025 letter states the instrument directly: *"analysts
  estimating that the smartphone unit shipments growing less than 2% year-on-year whereas
  Arm's royalty revenue from smartphones grew around 30% year-on-year."* **Royalty per chip
  rose from ~$0.055 to ~$0.077 in two years — +40% — on flat units.** That is the mechanism
  the brief named (v9 and CSS carry higher rates per chip; CSS *"expands both the value Arm
  delivers and the economics we capture"*) and it is [E2-44](a) evidenced from the filing —
  the strongest pricing-power instrument in the eight runs of this queue. **It is also a
  ceiling** [E2-63]: a mix shift ends when the mix is complete, and the 20-F's own royalty
  paragraph says rates *"typically reduce over time as the total volume of chips
  incorporating our products shipped increases"*, floored by a contractual minimum.

### The licence line — the other half, and who is paying it

| FY | licence & other | y/y | of which related parties | of which **external** | external y/y |
|---|---|---|---|---|---|
| 2022 | 1,141 | — | n/f | — | — |
| 2023 | 1,004 | −12% | n/f | — | — |
| 2024 | 1,431 | +43% | 380 | 1,051 | — |
| 2025 | 1,839 | +29% | 418 | 1,421 | +35% |
| **2026** | **2,307** | **+25%** | **1,009** | **1,298** | **−9%** |
| Q1 FY2027 | 574 | +23% | 264 | 310 | +22% |

**In FY2026, licence revenue from customers outside the SoftBank group fell 9%; the reported
25% growth is $591M of new licensing from a SoftBank affiliate (Note 20: $704.4M, from
$145.5M), of which $645.8M was unbilled at year-end.** The MD&A's causal sentence for the
line — *"continued strong demand for Arm IP"* — does not say this; Note 20 does. Carried to
Q3 as the candor read and to Q4 as the favourable break to remove.

- **VERDICT: [x] IN** — on the filed licensing-and-royalty business, whose mechanism, unit
  series and price series are all filed and legible. *Recorded against myself under operator
  rule 9: the brief's prior was that this would be the cleanest Q1 in the queue, and it is
  clean only for the business as it was; the registrant has told its owners in the 20-F that
  it is becoming something with "materially different margin profiles", and thirty percent
  of its revenue now comes from parties related to its 86% owner. Both facts are visible at
  Q1 and are carried forward, not softened.*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The brief's claim, framed to be refuted [E4-26]: "IN, and possibly the widest
instruction-set moat that exists." The attack the brief ordered: RISC-V, the customers' own
architecture licences, and the Qualcomm litigation. All three are run from the filings. The
verdict is IN, and the class is WIDE in the installed base — but the brief's "widest that
exists" is qualified by four filed facts, each of which is the moat's own customers acting
against it.**

### The three criteria [E3-03], from the subject's own filings

- **(1) Needed or desired — YES.** Every chip with a processor needs an architecture; the
  registrant's is in *"virtually all smartphones, a majority of tablets and digital TVs, and
  a significant proportion of all chips with embedded processors"* and *"more than 350
  billion Arm-based chips … shipped cumulatively."*
- **(2) No close substitute — YES in mobile, CONTESTED elsewhere, and the contest is filed.**
  Item 4.B, verbatim: *"We face competition primarily from other architectures like x86 and
  RISC-V in many of these markets. Furthermore, certain semiconductor companies, including
  some of our existing customers, have designed or are in the process of designing their own
  architectures in markets such as smartphone application processors, other mobile chips,
  consumer electronics, IoT and embedded computing, networking equipment, automotive, and
  cloud compute."* And: *"Some of our customers are also major supporters of the RISC-V
  architecture … in August 2023, a group of our customers and other competitors announced a
  joint venture aimed at accelerating the adoption of RISC-V, initially focused on the
  automotive sector."* The registrant names its substitutes and names its customers as their
  sponsors. In the smartphone application processor — 43% of royalty revenue — it reports
  *"market share … of greater than 99% for many years, by virtue of all key mobile operating
  systems depending on Arm processors"*: there, the substitute would need a new operating
  system, and there is none. That is near-monopoly in the [E5-28] sense, and criterion (2)
  holds there without qualification.
- **(3) Not price-regulated — passes on price; the buyer is regulated instead, and antitrust
  is an admitted exposure.** No one caps royalty rates. What is regulated is who may buy
  (BIS rules, the Entity List, the May–July 2025 EDA suspension the 20-F recounts) and, in
  the PRC, through whom: *"substantially all of our PRC-related revenue is generated through
  the IPLA with Arm China, a related party … Arm China operates independently of us."* The
  20-F also says antitrust *"could and has from time to time subjected us to investigations
  by antitrust regulators"* — the regime that once blocked the NVIDIA sale is the regime that
  would cap the royalty if it were ever used as [E3-33] describes. [E2-59]: neither creates
  nor destroys the class; both are edges.

### [E2-44], both halves, on the subject's own numbers

**(a) Can it raise prices when demand is flat? YES — the only run in this queue where the
instrument is filed, and it reads in the affirmative.** From Q1: units flat-to-down (FY2023
30.6bn; Q1 FY2024 −6.4%; Q4 run-rate 7.0bn → 7.9bn over two years) while royalty per chip
rose ~$0.055 → ~$0.077 (+40%) and total royalty rose $1,675M → $2,613M (+56%) in three
years. The letters attribute it to the v9 and CSS mix — a richer product commanding a higher
per-chip rate on the same unit — and the Q4 FY2025 letter's smartphone sentence (units
<2%, royalty ~30%) is the [E2-44](a) test stated by the registrant. **[E4-37]'s agony
metric reads the other way too:** the 20-F concedes that concentration *"has afforded
certain customers significant bargaining power, which has, in some cases, resulted in
pricing or other contractual terms that are less favorable to us"* and that new-product
royalty increases may be refused — *"customers may not value or be willing to bear the cost
of incorporating these newer products … including increases in royalty rates for such new
products."* The price rises are real and the customers are pushing back in writing.

**(b) Can it grow dollar volume with only minor additional capital? It could; it no longer
does — and the capital is people, not plant.** FY2022–24 capex was $34M–$92M on $2.7–3.2bn
of revenue: the franchise form. FY2026: capex $545M, R&D $2,776M (**56.4% of revenue, up
from 51.7%**), stock pay $1,052M, headcount +15%. Revenue grew $913M; R&D grew $705M. The
registrant's own doctrine: *"each year we increase our research and development investment
in line with the increased development needs of the next generation of products."* The
dollar volume grows; the capital added to grow it is now most of the growth.

### [E4-04] — must the moat be continuously rebuilt? The tail says no; the spending says the company is buying something else

The test: does a lapse in spending destroy the structure, or narrow it, and does the spending
defend the same advantage or buy its replacement? **The structure survives a lapse — this is
the filed fact that most supports the brief's prior**: 46% of FY2023 royalties came from
designs released 1990–2012; 350bn cumulative chips; the ecosystem does not decompile itself.
A year without a new core narrows the lead at the leading edge and leaves the tail intact.
That is [E5-23]'s continuous defence, not [E4-04]'s replaced basis. **But the FY2026 spending
is not defence of the same advantage**: the R&D step was *"primarily due to increases in
research and development expenses related to investments in next generation products, such
as the Arm AGI CPU"* — a chip, not an architecture. Munger's *competitive destruction* is
not the risk here; the risk is [E3-40]'s: the moat's owner spending the moat's cash on a
different business. Recorded at Q2 as a direction finding and at Q3 as the loss-of-focus
read.

**Key-person dependence [E4-23] — not the surgeon; the shareholder.** The moat does not go
when the CEO goes. It is exposed to the parent: seven SoftBank-designated directors, 72% of
the shares pledged, and a licensing counterparty that is *"an affiliate of SoftBank Group"*
at 14% of revenue. Recorded here as a moat defect of a different kind — the franchise's cash
is allocatable by an owner whose interests the 20-F says *"may conflict with the interests of
other holders."*

### The attack, item by item, from the filings

**1. RISC-V.** Named in Item 4.B and in Item 3.D as *"free, open-source technologies"* whose
*"major supporters"* include Arm's own customers, with a customer-founded JV in automotive
(August 2023). No RISC-V vendor files with the SEC in a form that can be rowed (SiFive
private; Andes Technology listed in Taipei; the MIPS business inside GlobalFoundries is not
segmented). **The attacker's test [E2-45] is therefore answered by the customers, not by
me:** given ample capital and skilled personnel, the way to compete with Arm is to fund an
open instruction set jointly so no one owns it — and the filing says that is exactly what
*"a group of our customers"* did. In mobile it has not moved the 99%; in IoT/automotive the
registrant reports no share figure, and that absence is the limit.

**2. The architecture licensees.** An ALA lets a customer *"develop their own highly
customized CPU designs that [are] compliant with the Arm instruction set architecture … for
a fixed architecture license fee."* The ALA customer pays for the language, not the design
— so the largest, most capable customers (the registrant does not name them; the litigation
names Qualcomm and Nuvia, and every hyperscaler building on Neoverse is designing its own
chip) contribute royalties on their own cores at rates the filing does not disclose. The
registrant admits the consequence in its concentration risk: *"certain of our contracts with
key customers contain provisions allowing such customers to obtain licenses to our latest
products as soon as they are made available to any other customer."* Most-favoured-customer
terms are the signature of a supplier that cannot price-discriminate against its biggest
buyers.

**3. Arm v. Qualcomm — the filed status, and what it did to the licensing model.**
- *Arm's suit (Delaware, filed 2022-08-31):* Arm terminated Nuvia's ALA in March 2022 when
  Qualcomm bought Nuvia without Arm's consent and sued to force destruction of the
  Nuvia-derived designs. *"The claims were tried to a jury in December 2024. The jury failed
  to reach a complete verdict on the three issues presented to it. The jury concluded that
  certain technology was licensed to Qualcomm under the Qualcomm license and that Qualcomm
  had not breached the Nuvia ALA but failed to reach a verdict on whether Nuvia breached the
  Nuvia ALA … On September 30, 2025, the Court affirmed the jury verdict on the issues on
  which it reached a conclusion and granted Qualcomm judgment as a matter of law in its favor
  to conclude that Nuvia did not breach the Nuvia ALA. We have filed an appeal with the
  United States Court of Appeals for the Third Circuit, which is currently pending."*
  (FY2026 20-F, Item 5; repeated in the Q1 FY2027 6-K.)
- *Qualcomm's suit (Delaware, filed 2024-04-18, amended three times):* breach of delivery
  obligations under the Qualcomm ALA; then *"allegations relating to an Arm notice of breach
  of the Qualcomm ALA and related tort and anti-competition claims"*; then breach of the
  Technology License Agreement; consolidated with a parallel suit against Arm Limited in
  March 2026. *"The case is expected to go to trial in the fourth calendar quarter of 2026."*
  (The FY2025 20-F had said March 9, 2026; it slipped.)
- **What the verdict did to the model, on the filed record:** an architecture licensee that
  acquires another licensee's designs may ship them under *its own* ALA. Arm's lever —
  terminate the acquired ALA and force the designs (and their royalty terms) back to the
  table — was tried before a jury and did not work, and the judge then ruled the acquired
  party had not breached either. The royalty-rate consequence is not filed and I do not
  state one. What is filed is the exposure: *"Qualcomm … accounted for 9% of our total
  revenue for the fiscal year ended March 31, 2026"* (10% in FY2025 and FY2024), Qualcomm
  is a founder of the customers' RISC-V JV, Qualcomm's counter-suit alleges Arm threatened
  its architecture licence, and Qualcomm has *"announced plans to enter the AI data center
  CPU market with its Arm-based Dragonfly C1000"* (Q1 FY2027 letter) — i.e. the litigant is
  simultaneously the second-largest smartphone-chip licensee, a substitute's sponsor, and a
  future competitor to the AGI CPU. **The litigation shows the moat's limit precisely: Arm
  can license the language but cannot, on this record, control what a licensee does with a
  compliant design it lawfully holds.**

**4. The fourth attacker is the subject itself.** *"[S]ome of our customers may face direct
competition from us in silicon production products, such as with the Arm AGI CPU"* and
customers *"could … elect[] to use alternative architectures such as x86 and RISC-V"* if
Arm's products *"may be perceived as competitive with, products sold by our customers."*
Nothing in the peer row is this: a licensor whose 20-F warns that its new product may push
its licensees to the substitute.

### Customer concentration and SoftBank-related revenue — filed

| FY | top five (incl. Arm China and SoftBank) | largest (Arm China) | >10% customers (Note 4) | Qualcomm | related-party revenue | of which SoftBank affiliate |
|---|---|---|---|---|---|---|
| 2022 | 56% | 18% | — | — | — | — |
| 2023 | 57% | 24% | — | — | — | — |
| 2024 | 54% | 21% | 3 (21/11/10 = 42%) | 10% | $724M (22%) | $4M |
| 2025 | 56% | 17% | 4 (17/11/11/10 = 49%) | 10% | $823M (21%) | $146M |
| **2026** | **57%** | **16%** | **3 (16/14/12 = 42%)** | **9%** | **$1,499M (30%)** | **$704M (14%)** |
| Q1 FY2027 | — | — | — | — | $388M (30%) | n/f in 6-K |

Three customers are 42% of revenue; the second-largest at 14% is, by arithmetic on Note 20,
the SoftBank affiliate (14.3%); Arm China at 16% is a related party that *"operates
independently of us"* under an IPLA running to 2048 that lets it *"develop its own IP"* and
sublicence at prices on which *"[t]here are no material restrictions."* **Thirty percent of
the franchise's revenue is contracted with entities the controlling shareholder controls or
part-owns.** A moat is measured against arm's-length buyers; nearly a third of this one's
revenue is not at arm's length, and its largest new licence customer of FY2026 is not
named.

### THE COMPETITOR ROW — required [E3-28]

**Identical formula for every filer (the SNPS-run convention, [E2-43] in the closest
computable form): gross margin = (revenue − cost of revenue) ÷ revenue as filed; operating
margin = filed income from operations ÷ revenue; ROUNTOA = operating income ÷ (total assets
− goodwill − intangibles − non-interest-bearing current liabilities).** Latest full fiscal
year each. IP-licensing peers reused from `_research 2026-09-07 SNPS/ROW_IP_CAE_PEERS.md`
and `ROW_CDNS_ANSS.md` (every figure filing-sourced there); the x86 and Qualcomm rows from
their own runs in this folder.

| | **ARM FY26 (Mar)** | SNPS FY25 (Oct) | CDNS FY25 | CEVA FY25 | RMBS FY25 | QCOM FY25 (Sep) | AMD FY25 | INTC FY25 |
|---|---|---|---|---|---|---|---|---|
| form · accession | 20-F `0001973239-26-000097` | 10-K `0000883241-25-000028` | 10-K `0000813672-26-000016` | 10-K `0001437749-26-006091` | 10-K `0001193125-26-057101` | 10-K `0000804328-25-000085` | 10-K `0000002488-26-000018` | 10-K FY2025 (INTC run, filed 2026-01-23) |
| what it is to Arm | subject | EDA + interface IP; sold its processor-IP line to GlobalFoundries Jun-2026 | EDA + IP; bought Arm's Artisan line Aug-2025 | DSP/NPU IP licensor — the only other filer with a unit series | interface IP + patent licensing | the litigant licensee; QTL is the pure-licensing comparator | x86 — vertically integrated, does not license | x86 — the incumbent Arm is displacing in servers |
| revenue $M | 4,920 | 7,054.2 | 5,296.8 | 109.6 | 707.6 | 44,284 (QTL 5,582) | 34,639 | 52,853 |
| **gross margin** | **97.5%** | 77.0% | 86.4% | 87.1% | 79.6% | not pulled | 49.5% | 34.8% |
| R&D % revenue | **56.4%** | 35.1% | 33.4% | 68.3% | 26.5% | 20.4% | 23.4% | 26.1% |
| SBC % revenue | **21.4%** | 12.7% | 8.6% | 18.1% | 7.7% | not pulled | not pulled | not pulled |
| **operating margin (GAAP)** | **18.3%** | 13.0% | 28.2% | (10.4%) | 36.8% | 27.9% (**QTL 72.4%**; QCT 30.4%) | 10.7% | (4.2%) |
| **ROUNTOA** | **11.5%** | 18.5% | 29.5% | (3.8%) | 23.4% | not computed on this formula | not computed | not computed |
| unit series filed | annual to FY2023, then dropped | none | none | **2.1bn devices (2025), by category** | none | MSM units, dropped after FY2017 (QCOM run) | none | none |
| royalty per unit | ~$0.055 → ~$0.077 | — | — | $0.022 | — | — | — | — |
| names Arm as competitor | — | no | no | **yes** (CPU IP, NPU, audio, vision) | no | not as a competitor; as licensor | no | no |

*ARM ROUNTOA: 900 ÷ (10,703 − 1,623 − 230 − 1,040) = 11.5% (FY2025: 13.3%). Cash of $3.6bn
sits inside the denominator as it does for every peer; ex-cash it is 21%.*

**The row's finding, and it runs against the brief's superlative in one column and for it in
another:**
1. **On gross margin Arm is alone at the top: 97.5% against the next-best 87.1%.** That is
   what a pure architecture royalty looks like, and nothing in the row resembles it. **On
   what reaches the owner it is near the bottom: 18.3% operating margin and 11.5% ROUNTOA
   against Cadence's 28.2%/29.5%, Rambus's 36.8%/23.4%, and Qualcomm's licensing segment
   at 72.4%.** The gap is R&D at 56% and stock at 21% — the highest of any profitable filer
   in the row. Same position, different conduct [E3-61]: Rambus and Qualcomm's QTL run
   licensing businesses that keep the licence money; Arm runs one that spends it.
2. **The pricing instrument exists only for two filers, and Arm's is the stronger:** Arm's
   royalty per chip is rising (+40% in two years); CEVA's is $0.022 on units growing 6%. The
   comparison also sizes the moat honestly: Arm collects about **seven cents** a chip on
   products whose selling prices run from under a dollar to over a hundred. The pricing
   power is real and the price is small — [E2-63]'s ceiling is the customers' willingness to
   bear a v9 rate on a chip whose CPU is one of a dozen blocks.
3. **Peers taken: 8 filers, against the industry's real count of roughly fourteen.** The
   row's limit, stated [E3-28]: **the substitute cannot be rowed.** RISC-V's commercial
   vendors — SiFive (private), Andes (TWSE 6533, not an SEC registrant), Tenstorrent
   (private), the MIPS line inside GlobalFoundries (a 20-F filer that does not segment it)
   — and the two largest architecture licensees as *designers* — Apple (captive; its ALA
   economics are not disclosed by either party) and Qualcomm (its Arm royalty is not a
   filed line) — sit outside the ladder. Imagination Technologies (GPU IP, private) likewise.
   Adjudicated under the ACLS/KLAC rule: an unrowable competitor can only narrow a moat,
   never widen one; the class is capped, not suspended, and the gap becomes the Q6 item.
4. **[E2-53] dominance class — claimed for the smartphone application processor only**, where
   the registrant reports >99% share "for many years" and the filing's own words make the
   position, not the execution, the cause (*"by virtue of all key mobile operating systems
   depending on Arm processors"*). **Refused for the company**: a company whose GAAP
   operating margin fell to 7.1% in the latest quarter (Q1 FY2027 letter) while revenue rose
   22% is not one where *"good or bad, it will prosper"* for its owners.
5. **[E3-33]/[E5-28] untapped pricing power — the class is CLAIMED, narrowly, and it is the
   strongest single fact for the brief's prior.** Seven cents a chip against >99% share of a
   market whose device sells for hundreds of dollars is the textbook untapped case, and the
   FY2024–26 record is the company beginning to tap it (v9, CSS). The counter-evidence is
   also filed: most-favoured-customer clauses, customers *"unwilling to pay for improved
   products,"* a 20-F admission of antitrust investigations, and the customers' RISC-V JV as
   the response to exactly this.
6. **[E4-36] — which of the four causes?** An extreme max on one variable — the installed
   software base of the instruction set — compounded by a nonlinear combination (the OS
   vendors' dependence, the developer count, the royalty tail). Ownable, and not a wave. The
   FY2024–26 *level* is partly a wave (the v9 mix shift and the AI data-centre build) and Q4
   normalises for it.

- Class: **[x] WIDE** [ ] NARROW [ ] NONE [ ] PROVISIONAL — **WIDE in the installed base
  and in mobile (near-monopoly on the registrant's filed share); NARROW at every growth
  edge the price is paying for (data centre against x86, IoT/automotive against RISC-V,
  silicon against its own licensees).** Direction: **pricing WIDENING** (royalty per chip
  +40% on flat units; CSS licences 21 across 12 companies); **structure NARROWING** — the
  customers funded the substitute in 2023, the largest licensee won at trial in 2025 and
  sues again in Q4 2026, external licence revenue fell 9% in FY2026, and the company's own
  entry into chips is the reason its 20-F now warns customers may leave for x86 or RISC-V.
- **VERDICT: [x] IN — WIDE, with the edges NARROW.** *The strongest fact against this verdict,
  stated per [E4-51] so a bear would accept it as fairly put: **the moat's own customers —
  Qualcomm and the RISC-V JV founders, Apple and the hyperscalers under architecture
  licences, and Arm China under an IPLA to 2048 that lets it build its own products — have
  each, on the filed record, acquired the means to reduce what they pay Arm per chip, and
  the largest of them has already beaten Arm before a jury on precisely that question; the
  company's response is to compete with them in silicon, which its own 20-F says may drive
  them to the substitute.** Held IN because the instruction set, the ecosystem and the
  royalty tail are the widest installed base in the row and the only one with filed evidence
  of raising price on flat units. The brief's "possibly the widest that exists" is refuted
  only in scope: widest where it already is, ordinary where the price assumes it will be.*

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**The brief's instruction — pull the 6-K release before scoring [E4-29] and [E4-22]'s third
flag, and read the SoftBank related-party note — was followed for six consecutive
shareholder letters (Q4 FY2025 through Q1 FY2027, accessions at Step 0), the Arm Everywhere
6-K, Item 6.B of the 20-F (the UK-style remuneration report), Item 7, and Note 20. "Do not
assume any gate is short" — this one is not.**

**STEP 1 — THE WEIGHT CASE, DECLARED.**
- [x] **Daily execution [E3-38]** — as of March 2026 the registrant is a fabless chip vendor
  as well as a licensor, and says so in the vocabulary of have-to-be-smart-every-day:
  *"transitioning to advanced process nodes; competing against established production
  silicon companies; coordinating multi-year roadmaps with lead development partners;
  managing product transitions and inventory across generations."* The licensing business
  alone would not tick this box; the company the price is paying for does.
- [x] **Control [E1-16]** — ticked in mirror image. The corpus's case is the owner who holds
  the whole thing and cannot exit; here the minority holder cannot exit the *controller*:
  86.4% with SoftBank, every non-executive director SoftBank-designated, pre-emptive rights,
  a consent right, and 72% of the company pledged against the parent's margin loan. The
  damage a controlling shareholder can do before a 13.6% float can react is unbounded, and
  the 20-F's own risk heading is *"risks associated with the interests of SoftBank Group …
  conflicting with the interests of other holders."* [E3-66]'s jurisdiction point applies
  by structure rather than by country: the ADS holder stands behind SoftBank in every queue.
- [ ] **Leverage [E3-29]** — none: *"We do not currently have any debt."*

**Two ticked → Q3 is a BINARY GATE and no price compensates [E1-16, E3-29, E5-35].** Case
declared: the gate is on the controller's conduct toward the minority and on the disclosure
conduct where the registrant holds the information advantage [E2-68].

**Honesty — binary, permanent, filings-based [E5-16].** *Recorded sweep of the three 20-Fs,
the F-1, the Q1 FY2027 6-K and the six letters for: restatement, material weakness, SEC
comment or enforcement, DOJ/BIS penalty, auditor change, related-party loan to an officer,
insider-trading matter, whistleblower: **no instance found.** The litigation is commercial
(Qualcomm/Nuvia, dated 2022-08-31 and 2024-04-18 when public) and a settled early-history
contract dispute with a non-top-five customer (offer $40.0M, FY2023; settled 2023-09-15
for no cash; liability reversed FY2024). The 20-F mentions antitrust investigations
*"from time to time"* without naming one — recorded, not scored, per [E5-22]: penalty size
is not seriousness and an unnamed matter cannot be read. **No personal-misconduct
disqualifier found.**

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49, E3-50].** *Each a prompt to read,
never a verdict. Six fire; they converge.*

- [ ] **weak accounting** — not found. No capitalised R&D; cost of sales $121M; equity
  investments at fair value with the losses taken ($246M on Ampere, FY2025); revenue
  recognition has a critical audit matter on related-party performance obligations (the
  auditor's own words: *"an evaluation of whether the transaction price and corresponding
  performance obligations were fairly presented for related party transactions"*) — read, not
  ticked.
- [ ] **unintelligible footnotes** — not found; the notes are the clearest part of the
  document. The **MD&A** is the unintelligible layer: it attributes FY2026 licence growth to
  *"continued strong demand for Arm IP"* when Note 20 shows the growth is one affiliate of
  the parent and external licensing fell 9%.
- [x] **trumpeted earnings projections / growth targets [E4-22 third; E3-48; E5-30].** The
  guidance record, six quarters, from the letters' own tables:

  | quarter | revenue guidance | result | non-GAAP EPS guidance | result |
  |---|---|---|---|---|
  | Q4 FY2025 | $1,175–1,275M | $1,241M (above mid) | $0.48–0.56 | $0.55 |
  | Q1 FY2026 | $1,000–1,100M | $1,053M (above mid) | $0.30–0.38 | $0.35 |
  | Q2 FY2026 | $1,010–1,110M | **$1,135M (above the top)** | $0.29–0.37 | $0.39 (letter: above the top) |
  | Q3 FY2026 | $1,225M ± 50 | $1,242M | $0.41 ± 0.04 | $0.43 |
  | Q4 FY2026 | $1,470M ± 50 | $1,490M | $0.58 ± 0.04 | $0.60 |
  | Q1 FY2027 | $1,260M ± 50 | $1,289M | $0.40 ± 0.04 | **$0.45 (above the top)** |
  | FY2025 annual | $3.94–4.04bn | $4.01bn | $1.56–1.64 | $1.63 |

  **Seven guides, seven met, five above the midpoint, two above the top of the range — the
  [E4-30] unnaturally-smooth tell in its guidance form.** [E3-48]'s remedy is to demand the
  record of the people who made the projections: this record is a management that guides
  low and beats. On top of the quarterly ratchet sit three long-range numbers with no
  reconciliation: *"$15 billion in this business"* (silicon; Q4 FY2026 letter), *"a market
  opportunity of more than $100 billion by 2030"*, and *"more than $2 billion of customer
  demand across fiscal 2027 and fiscal 2028"* for a chip launched in March — each footnoted
  *"Based on Arm internal estimates"* where footnoted at all. [E5-30]: *"once you start it,
  it's all over."*
- [x] **serial share issuance [E5-15].** Shares 1,025M (Mar 2023) → 1,040M → 1,057M → 1,064M
  → **1,068M (Jun 2026)**, +4.2% in three years — *after* the company paid $585M in FY2026
  and $278M in Q1 FY2027 to withhold shares on vesting. Every share issued went to an
  employee; none was bought back from the market; **$1,719.3M of unrecognised compensation
  remains to be charged over 1.2 years** (Note 15), and the plan reserve was increased by
  13,821,271 shares on 2026-04-01 (Note 22). The corpus's sentence: *"one of the surest
  indicators of a promotion-minded management."*
- [x] **EBITDA / adjusted-earnings promotion [E4-29] — fires at full strength, and it is
  paid on.** Every letter headlines *non-GAAP operating margin* (43.0% FY2026; 49.1% Q4;
  41.2% Q1 FY2027) beside a GAAP figure of 18.3% / 29.4% / **7.1%**; the difference is
  *"share-based compensation cost … employer taxes related to SBC … (income) loss from equity
  investments"* — $1,052M + $160M in FY2026. **The CEO's FY2026 bonus was scored on
  *"revenue and profit (EBITDA)"*** (Item 6.B); **FY2027 bonus and PSUs are scored 50/50 on
  Revenue and *Non-GAAP Operating Income*** — a metric that excludes the $1,052M cost of the
  stock the bonus is paid in. [E5-41]'s reverse-float point runs here in the other
  direction: the excluded item is not depreciation of money already spent but stock not yet
  vested, and the company's own cash-flow statement shows it costing $529M of withholding
  tax the year it vests.
- [x] **stock-price targeting [E3-50] — explicit, written into the remuneration policy, and
  put to the 2026 AGM.** *"The one-time VCP award of 425,000 PSUs will have a maximum vesting
  opportunity of 100% with the objective of achieving a $2.0 trillion market capitalization
  by March 31, 2031"* — tranches at $1.0tn (Mar 2029), $1.5tn (Mar 2030), $2.0tn (Mar 2031),
  measured on a 60-day average price, missed milestones rolling forward. The corpus's
  premise-with-which-we-adamantly-disagree — *"that their job at all times is to encourage
  the highest stock price possible"* — is here the stated performance condition: 7.1x the
  current capitalisation in five years. CEO single figure: **$70.1M (FY2024) · $24.5M
  (FY2025) · $60.6M (FY2026)**; FY2027 annual PSUs at 14x a $1.35M salary with a 200%
  maximum, raised from 125% *"conditioned on shareholder approval … at the 2026 AGM"* — an
  approval the 86.4% holder supplies.
- [x] **metric-switching [E2-49] — three instances, each following the reading turning
  unfavourable.** (i) *"Number of chips shipped"* was an F-1 KPI, justified as giving
  *"insight into chip pricing and volumes"*; the last published count, Q1 FY2024, was −6.4%
  y/y; **no letter since listing has carried it**, and the FY2026 20-F carries only the
  cumulative figure. (ii) Quarterly headcount and engineer counts dropped from Q1 FY2026
  (*"has become less relevant to our growth"*) as R&D headcount became the cost story.
  (iii) **RPO and the licence counts dropped from Q1 FY2027** (*"has become less relevant to
  our growth with the extension of our business into production silicon"*) — the quarter
  after RPO printed **−7% y/y** ($2,226M → $2,071M). *"Yardsticks seldom are discarded
  while yielding favorable readings."* The replacement yardstick is ACV, which excludes
  royalties and annualises single-use licences over an assumed three years.
- [x] **filed-figure tells [E4-30]** — cash taxes paid as a share of pretax income: FY2024
  88% ($187M / $212M) · FY2025 21% ($149M / $720M) · FY2026 19% ($223M / $1,157M). Falling
  as pretax rises, which is the tell's direction — **but the cause is filed and benign**:
  income-tax *benefits* of $94M and $72M in FY2024–25 on positive pretax income are deferred
  tax on share-based-compensation deductions (*"changes in withholding tax, unrecognized
  tax benefits and share-based compensation tax benefits"*), and the FY2026 effective rate
  normalised to 21.9%. Read; not scored as a fraud tell. Reported growth is not
  unnaturally smooth (OCF 1,090 → 397 → 1,524).
- **Related-party disclosure — the half-owner read [E2-26, E2-68].** What the 20-F tells and
  what it withholds, on the one line that made FY2026's growth:
  - Told: *"revenue from the licensing and servicing arrangements was $704.4 million and
    $145.5 million"* with *"an affiliate of SoftBank Group"* under *"the Consulting
    Agreement"*; *"current contract assets of $645.8 million … from the affiliate."*
  - Withheld: the affiliate's name, what was licensed or serviced, the term, and why 92% of
    a year's revenue from it was unbilled at year-end. The statements of work are not
    exhibits. The Audit Committee's related-party policy (Item 7.B) exempts transactions the
    committee deems arm's-length from approval; whether this one was so deemed is not
    stated.
  - Adjacent: SoftBank bought **Ampere** — Arm's equity-method investee, written down $246M
    the year before — in November 2025; Arm collected $39.3M on its Ampere convertible and
    now has an *"Ampere Development Agreement"* under which the parent's new subsidiary
    provides *"development services to the Company."* Arm China, the largest customer at
    16%, carries a $28.3M credit-loss allowance and *"operates independently of us."*
  - **Verdict on the read:** a half-owner would want to know who paid $704M and when the
    $646M arrives; the filing does not say. This is the disclosure conduct across an
    information asymmetry [E2-68], and it is a candor deficit, not a found falsehood. *Can I
    name the document that would resolve it?* The statements of work under the Consulting
    Agreement — not public; SoftBank Group's own securities reports might name the project —
    a rung outside this run. Recorded as the file's standing work order, below.

**Flags that converge [E4-52].** Non-GAAP pay + market-cap PSUs + a seven-for-seven guidance
record + serial issuance + three dropped yardsticks + an unnamed related party as the
year's growth — these are not six prompts; they are one system pointed at one outcome, the
$2.0 trillion the CEO's award names. The read treats them as such.

**STEP 3 — THE PRIMARY TEST [E2-01].** Earnings rate on equity capital employed, balance
sheet before income statement, five years, no leverage:

| FY | equity (Mar) | net income | **ROE** | net income ex interest, divestiture gain and equity-investment marks | ROE on that | ROUNTOA |
|---|---|---|---|---|---|---|
| 2022 | 3,548 | 549 | 15.5% | n/c | — | — |
| 2023 | 4,051 | 524 | 12.9% | n/c | — | — |
| 2024 | 5,295 | 306 | 5.8% | 216 | 4.1% | — |
| 2025 | 6,839 | 792 | 11.6% | 913 | 13.3% | 13.3% |
| **2026** | **8,286** | **904** | **10.9%** | 675 | 8.1% | **11.5%** |

*On unleveraged net tangible assets [E2-43] (equity − goodwill − intangibles = $6,433M),
FY2026 is 14.1%. On the operators' capital [E2-73] the hand dealt is a 97.5% gross margin
and a $2.6bn royalty annuity; **an 11% return on equity is what management's spending
turned that hand into**, and 40% of FY2026 equity growth was stock credited to APIC.
Cadence earns 29.5% on the same formula; Rambus 23.4%.*

**The half-owner test [E2-26]:** fails on the related-party licence line (above) and on the
non-GAAP framing; passes on the cash-flow statement, the withholding-tax line, the customer
concentration note, the litigation narrative and the risk factors, which are candid to the
point of self-indictment (*"we now face exposure to…"*). Authorship [E2-72]: the letters are
signed by the CEO and CFO; the 20-F's remuneration report is a UK-format committee document.

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] resists any change in current direction — no; the opposite.
- [x] projects/acquisitions materialise to soak up available funds — R&D +$705M in a year;
  capex 2.5x; DreamBig $265M (closed 2026-07-01); Raspberry Pi shares $67.9M (April 2026);
  a further $305M cloud commitment (April 2026); the AGI CPU programme.
- [x] staff studies produced to justify the leader's craving — *"more than 4x the current
  CPU capacity per GW\*"*, *"up to $10B in CAPEX savings per GW\*"*, *"more than $100 billion
  by 2030"*, all *"\*Based on Arm internal estimates."*
- [x] peer behaviour mindlessly imitated — every hyperscaler and every large licensee now
  designs chips; Arm follows them into silicon against them.

**Capital allocation — the two buyback conditions [E5-08]:**
- (1) ample funds — yes: $3,888M cash and short-term investments, no debt.
- (2) repurchases at a material discount — **no repurchases and no dividend in the listed
  history**; the only stock the company buys is from its employees on vesting, at market,
  with no value test, while issuing more. **CAPITAL ALLOCATION FLAG**, stated with the
  humility clause **[E4-13]**: management knows the AGI CPU's prospects better than I do, and
  a company that believes its stock is worth $2 trillion would rationally issue it. **Binds
  position size, never the discount rate.** The retention test [E3-54] passes on the market
  alone (book value per share $3.95 → $7.79 in three years against a price at 34x book) and
  is therefore uninformative — the corpus's own 2009 correction applies.

**THE GUARDRAIL — checked before writing the verdict.**
- [x] Confirmed: nothing in this Q3 is being used to **promote** the name.
- [x] Key-person dependence recorded at Q2 (the shareholder, not the surgeon).
- [x] Is a great manager the reason to act? No — the manager is not the plan; the *parent*
  is a plan-maker, and the corpus's exit rule for good-business-bad-allocation [E4-24] is
  the relevant one at Q6, not engagement.

- **VERDICT: [x] IN** [ ] OUT [ ] UNRESEARCHED [ ] UNKNOWABLE — *IN = no disqualifier found,
  and nothing more: no personal misconduct, no restatement, no false statement located in
  the filings. Six flags fire and converge; a capital-allocation flag is live; the control
  case makes Q3 a gate. A reader who treats the confluence — pay on a metric that excludes
  the pay, an award written against a share price, three dropped yardsticks and a fifth of
  revenue from unnamed or independent related parties — as disqualifying would close the
  file here, and the framework would not call that wrong. I do not, because the binary is
  conduct [E5-16, E5-38] and none was found; the flags bind size, and the number at Q4
  closes the file on the business regardless of how this gate is read. "Sincerity and
  empathy can easily be faked" [E5-17] applies to the letters' candour as much as to
  anything.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**

*The arithmetic is at Stage 0 and is not repeated; this section makes the judgments.*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**
- **Short-window mean** (3-yr FY2024–26, the clean post-IPO record): **−$251M (capex end) ·
  −$164M (D&A end)**
- **Long-window mean** (5-yr FY2022–26, two pre-IPO years on a liability-classified pay
  basis): **+$48M · +$49M**
- **TTM to 2026-06-30:** +$352M · +$676M — flattered by two timing items the letter itself
  names (receivables +$389M; payroll-tax payable +$370M); normalised down [E4-41] it is
  roughly zero.
- **Spread, conservative end:** not computable as a ratio (the sign changes); **in dollars,
  −$642M to +$676M across the windows and years.**
- **Combined range** (window spread × capex band): **−$0.6bn to +$0.7bn a year.**
- *Is that range too wide to reach a conclusion?* **No — it is narrow, and it is centred on
  nothing.** A range of ±$0.7bn around zero against a $282.8bn capitalisation is not
  [E4-25]'s "so wide that no useful conclusion can be reached"; it is a conclusion: **the
  owners of this business have received, and on the filed trend will receive, approximately
  none of its cash.**
- *A wide spread is also a Q4 finding: which distorted year sits in the window [E5-11]?* **All
  of them, each for a filed reason:** FY2024 carries +$495M of *"other liabilities"* inflow
  (employment tax accrued on vesting) and $212M of stock charge from pre-IPO liability
  awards; FY2025 carries the −$381M unwind of the same and −$743M of receivable/contract-asset
  build; FY2026 carries $704M of licence revenue from one SoftBank affiliate, 92% of it
  unbilled. There is no undistorted year in the listed record, and the distortions are the
  business's own working-capital mechanics plus its parent.
- **Owner earnings by year (capex end / D&A end):** FY2022 398/247 · FY2023 596/490 ·
  FY2024 −39/−109 · FY2025 −642/−606 · FY2026 −73/223 · TTM 352/676.
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT [E3-44, E2-41, E5-20].**
  Which case: **neither the 95% default nor the railroad exception fits cleanly, and the
  judgment is (c) ≈ $400M**, disclosed at Stage 0: above D&A ($249M; depreciation alone
  $122.6M) because the R&D that defends the moat now needs data-centre compute the FY2022
  business did not, below FY2026 capex ($545M) because the filing attributes the step to
  *"data center and office expansions"* for a new product line. **The judgment does not move
  the verdict: at (c) = 0 the clean window earns $34M a year.**
- Band used: OCF − SBC − [D&A $249M … capex $545M], every window shown.
- **Stock compensation subtracted in full [E5-06]:** $1,037M · $820M · $1,052M; the market-value
  measure [E3-70] would subtract more, and the $585M of withholding cash in FY2026 is the
  filed evidence that the charge is the floor.
- *If the capex band changes the verdict → UNKNOWABLE:* it does not; no construction on the
  post-IPO record produces a positive number the sovereign would notice.

**The look-through addition [E3-04]:** equity investments $387M at fair value/NAV, none
material; no undistributed investee earnings to add. Interest income of $111M on $3.6bn of
cash is inside net income but outside OCF's operating lines only as timing; it is not
owner earnings of the business and is not added.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [x] **gruesome — grows, eats capital, earns little**
- **Evidence:** *"grows rapidly"* — revenue +24%, +23%, +22% (Q1 FY2027); *"requires
  significant capital to engender the growth"* — R&D 56% of revenue and rising, stock 21%
  of revenue, capex 2.5x in a year, headcount +15%, and **the capital is the owners' shares:
  +4.2% of the company issued in three years, ~$12bn at today's price**; *"then earns little
  or no money"* — owner earnings ≈ $0 on every post-IPO window. The corpus's caveat [E4-43]
  is that the *good* class passes — capital-hungry growth earning an attractive return on the
  capital added. The test is *"unless the cash they consume gets to earn a reasonable
  return"*: **ROE 10.9% and falling, GAAP operating margin 18.3% → 7.1% in the latest
  quarter.** The paradox of the file, stated plainly: **the moat is in the great class — a
  97.5% gross-margin royalty on flat units with rising price — and the company that owns it
  is being run in the gruesome class**, because what the moat earns is spent on people paid
  in the owners' stock and on entering a business the moat's customers occupy. That is
  [E3-40] — *"neglects its wonderful base business while purchasing other businesses that
  are so-so or worse"* — with the purchase made internally, and it is why the corpus's
  answer to good-business-bad-allocation is to leave [E4-24], not to hold and hope.

### Staying power — score all three **[E5-11]**
- (1) **large and reliable stream of earnings — reliable as revenue, absent as owner
  earnings.** Royalties $2.6bn, recurring by mechanism (chips ship for years; 46% of FY2023
  royalty from designs released 1990–2012; ACV $1.7bn of committed licence fees). The
  company will not run out of revenue. It has run out of owner earnings by choice.
- (2) **massive liquid assets — yes.** $3,058M cash + $830M short-term investments at
  2026-06-30; no debt; no revolver drawn or disclosed; no commercial paper. Nothing depends
  on the kindness of strangers [E5-39].
- (3) **no significant near-term cash requirements — yes on the filed items, with one
  unfiled item named.** Filed: non-cancelable purchase obligations $1,056.5M through 2036
  plus $305M added April 2026 (cloud compute); operating and finance lease obligations
  $611M ($76M within a year); DreamBig $265M paid 2026-07-01; withholding tax on vesting
  running $529M a year and *"resulting from changes in share price"* — the one requirement
  that grows with the quote. Unfiled: the working capital of a fabless chip business —
  *"we have secured the manufacturing capacity required"* for $1–2bn of AGI CPU demand at
  TSMC 3nm, with no prepayment or inventory commitment disclosed. Against $3.9bn of cash,
  none of it is a solvency question [E2-55] under adverse conditions; it is where the
  royalty cash will go.
- **Leverage, named and quantified [E4-16, E3-29]:** none at the registrant. **The leverage
  is above it**: 769.0M of the company's shares — 72.0% — are collateral for SoftBank's
  margin facility, and *"[t]he foreclosure on our shares … could cause a change of control."*
  The coverage test [E2-54] is moot for Arm and unknowable for the parent from Arm's filings.
  Jurisdiction [E3-66]: English plc, Delaware-style governance agreement, Nasdaq ADS — the
  minority's place in the queue is set by the 86.4%, not by the law.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**

*Modelled from exposure, not experience: the last three years are the benign end of the
cycle for this filer (v9 mix, AI data-centre build, a parent-affiliate licence), and a bear
case its holders would accept must start from what the filing shows it is exposed to.*

**The mechanism, in four parts, each filed:**
1. **The licence line reverts to its external run-rate.** External licence revenue fell 9%
   in FY2026 to $1,298M; $704M came from one SoftBank affiliate under statements of work
   that can end. If FY2027 licensing returns to the external base plus Arm China (~$1.7bn)
   while royalties grow 15% (~$3.0bn), revenue is ~$4.7bn — **flat** — against an opex line
   growing 28–34% ($4.9bn on the Q1 FY2027 run-rate). **GAAP operating income goes to zero
   or below; owner earnings, already zero, go to roughly −$1bn.** *Likelihood: a real
   possibility — it is what the Q1 FY2027 quarter already shows in miniature (revenue +22%,
   GAAP operating income −20%, margin 7.1%).*
2. **A top-five licensee leaves the architecture.** Qualcomm is 9% ($443M); Arm China 16%
   ($791M) with its own IP rights to 2048. Loss of Qualcomm alone at a 97.5% gross margin
   removes ~$430M of operating income — half of FY2026's $900M. *Likelihood: a low-level
   possibility inside five years (the installed base is Arm's), a real possibility inside
   fifteen (the customer funded the alternative in 2023 and won at trial in 2025).*
3. **The silicon business earns chip-vendor economics on a licensor's valuation.** If the
   "$15bn" arrives at AMD's filed economics (49.5% gross, 10.7% operating) it contributes
   ~$1.6bn of operating income and needs several billion of working capital; if it arrives
   at the registrant's own warned risks (*"inventory write-offs"*, *"product transitions"*)
   it contributes less. Either way it dilutes a 97.5% gross margin toward the row's 50–80%
   and turns the moat's cash into inventory. *Likelihood: likely, as the direction the
   company has chosen; unquantifiable in level from any filed figure [E4-40].*
4. **The controller's leverage, not the company's.** A margin-call sale of pledged shares
   changes control without a vote; the pre-emptive rights and consent right mean the
   minority's position can be restructured around it. *Likelihood: a low-level possibility
   as an event; a certainty as a structure the minority cannot alter.*

**What survives all four: the company.** $3.9bn of cash, no debt, and a royalty annuity that
pays on designs from the last century. **What does not survive: the price.** None of the
four mechanisms threatens solvency; each threatens the owner earnings that are already
absent, and the $282.8bn that assumes they will appear.

- Likelihood, overall: **[x] likely** that the filed trajectory (rising R&D and stock, flat
  external licensing, silicon at lower margins) continues and owner earnings stay at or
  below zero; **a low-level possibility** that the business itself is impaired.
- **VERDICT: [ ] IN  [x] OUT** [ ] UNRESEARCHED [ ] UNKNOWABLE — ***OUT on the business as
  run: the gruesome class on the corpus's own definition [E4-20, E4-43], with owner earnings
  at or below zero on every post-IPO window, both (c) ends, and after a five-year, a
  three-year and a trailing-twelve-month construction.*** *This is not UNKNOWABLE: the
  evidence is in and it is not indeterminate — a business whose stock compensation equals
  97% of its operating cash flow over its whole listed life has told its owners what they
  get. It is not a finding about the moat, which is intact and pricing up; it is a finding
  about what is done with the moat's cash [E3-40]. The strongest fact against the verdict,
  per [E4-51]: the trailing twelve months are positive on both ends ($352M–$676M), Q1
  FY2027 OCF was $902M, and if the affiliate licence recurs and the payroll-tax timing is
  real, FY2027 could be the first listed year with owner earnings above zero — at which
  point the yield on the current capitalisation would be a quarter of one percent.*

---
⛔ **Q5 does not open. Q4 is OUT.** The arithmetic below is required by the operator's
standing instruction that every run end with a price and a pass/fail, and by the brief's
instruction to state what the buyer is paying for; it is headed as the framework requires.

---
## COMPUTATION — NOT A CLEARANCE

*Q1–Q3 IN, Q4 OUT. No entry language appears below; nothing here ranks the name.*

**1. THE YIELD** — owner earnings ÷ market cap $282,817M, beside the sovereign 5.35%:

| construction | owner earnings | yield | points vs sovereign |
|---|---|---|---|
| 3-yr FY2024–26, capex end | −$251M | **−0.09%** | −5.44 |
| 3-yr FY2024–26, D&A end | −$164M | −0.06% | −5.41 |
| 5-yr FY2022–26 (pre-IPO pay basis) | +$48M | +0.02% | −5.33 |
| TTM to 2026-06-30, capex end | +$352M | +0.12% | −5.23 |
| TTM, D&A end (the most generous filed reading) | +$676M | +0.24% | −5.11 |
| the company's own non-GAAP operating income, taxed at 21.9% — *i.e. pretending the stock is free* | $1,652M | 0.58% | −4.77 |

The 30-year Treasury pays **$15.1bn a year** on $282.8bn — three times Arm's entire revenue.

**2. WHAT THE PRICE ALREADY ASSUMES.** To clear the corpus's ~10% floor [E4-28] at this
capitalisation the business must deliver **~$28bn a year of owner earnings** — 5.7x FY2026
revenue. At the registrant's own non-GAAP operating margin (43%), after tax, that requires
**~$85bn of revenue, seventeen times FY2026**, with no stock compensation at all. Compounding
revenue at the post-IPO 23% gets there in **fourteen years**, if the stock stops and the
margin holds. The corpus's base rate [E4-35]: fewer than one in twenty of the most
profitable companies sustain 15% for twenty years. A DCF is refused as an engine here on
the framework's own ground — a non-positive base produces no number [E5-34] — and the
statement above is what replaces it. The upside ceiling [E2-63]: the royalty is seven cents
a chip on 30bn chips; the price assumes the chips, the cents, and a chip business, all at
once.

**3. WHAT YOU ARE PAID:** −5.1 to −5.4 points against the sovereign on any filed
construction. **Below the floor by ten points; below the bond by five.**

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01] — of the filed owner earnings, not of the
story.** Zero-growth capitalisation of the most generous filed reading (TTM D&A end, $676M):
at the sovereign **~$12bn ≈ $12 a share**; at the 10% floor **~$7 a share**. Of the
company's own non-GAAP operating income after tax, pretending the stock is free: **~$30 a
share** at the sovereign. **Conservative $0 · optimistic ~$30 · current price $264.79.**
The margin of safety is not computed; a price above the whole range is Bar 2's third
outcome, *no*.

**WHAT THE BUYER AT $264.79 IS PAYING FOR, IN WORDS.** The buyer pays **57 times revenue,
313 times GAAP earnings, 134 times the non-GAAP operating income management is paid on, 34
times book, and an unbounded multiple of owner earnings**, for four beliefs, none of which
is a filed figure: **(i)** that $1.1bn a year of stock paid to employees is not a cost of
the business — the corpus's verdict on that belief is *"even more cavalier"* [E5-06];
**(ii)** that a chip announced in March 2026 with $0 of filed revenue becomes *"$15
billion in this business"* at licensing margins, in an industry where the filed margins
of chip vendors are 50% gross and 11% operating; **(iii)** that data-centre royalties keep
*"more than doubling"* until the x86 incumbents are displaced, while the buyers of those
chips hold architecture licences and fund the open substitute; and **(iv)** that the **$2.0
trillion** market capitalisation the CEO's award is written against arrives by March 2031 —
a seven-fold rise from here. Against those beliefs the buyer receives a franchise that is
real, priced at seven cents a chip, whose owners have been paid nothing in three years and
whose 86.4% holder has pledged most of it to a bank.

- **PRICE $264.79 (2026-09-11) · FAIL — closed at Q4, on the business as run.**

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
**NOT OPENED.** Q4 is OUT. *Floor verdict, stated for the register only: honest pre-tax
expectancy at this price is negative on the clean record and below one percent on the
most generous — quit on, not ranked [E4-28]. Bar: neither — no bar is applied to a name
that did not reach Q5. Windage count: 0.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
**NOT OPENED as an entry question. Written as the reversal condition in words (the QLYS
ruling, 2026-09-07): this file failed on the business, so no price band is armed and no
PORTFOLIO row is added.**

- **What would reopen the file — the thesis-breaking metric for this verdict [E1-02]:**
  **stock compensation ÷ operating cash flow below ~25% for two consecutive fiscal years**
  (the band in which QLYS, CRM and SHOP passed the test), i.e. owner earnings durably
  positive on the framework's construction, **and** the external licence line growing without
  a related party inside it. On the FY2026 figures that means SBC below ~$400M against
  today's OCF, or OCF above ~$4bn against today's SBC.
- **What would confirm it:** the FY2027 20-F showing SBC/OCF above 50% again, external
  licence revenue flat or down, and the affiliate contract asset ($646M) still unbilled or
  written down.
- **Dated items to read [E4-17, E3-30]:** the Qualcomm trial, Q4 calendar 2026; the Third
  Circuit appeal; the FY2027 20-F (May 2027) for whether a chips-shipped count returns and
  what the silicon line's gross margin is; each quarterly letter for RPO's reappearance;
  SoftBank's pledge percentage in Item 7.
- **Moat downgrade, the slow trigger:** royalty per chip stops rising while units stay
  flat — the v9 mix completing — is the [E4-37] agony signal to watch; a filed loss of a
  >10% customer to RISC-V or an own-architecture is the fast one.
- **Position size:** none. Sized to zero by the Q4 verdict; the capital-allocation flag at
  Q3 would have sized it down regardless [E3-45 direction stated, no number fixed].
- The sell rule [E2-28] is not engaged; nothing is held.
- **VERDICT: not opened.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN · Q2 IN · Q3 IN · Q4 OUT · Q5/Q6
      not opened, reversal condition written)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q2's
      competitor row is 8 filers with the unrowable substitute named as the limit, class
      capped not suspended; Q3's IN is "no disqualifier found" with six flags recorded
- [x] Every UNRESEARCHED verdict names the artifact — none returned; the standing work order
      (the SoftBank affiliate's identity and terms) is recorded at Q3 and in the register
      without changing a verdict
- [x] Every UNKNOWABLE verdict states what cannot be known — none returned
- [x] Step 0: the filing was read, with accession number; OCF, SBC, capex, the Note 21 cost
      build and A − L cross-checked to the million
- [x] Owner earnings on a multi-year mean; three windows plus TTM; capex band disclosed as
      a judgment (~$400M) that does not move the sign
- [x] Competitor row filled (8 filers, identical formula), limit stated
- [x] Sovereign is for the earnings currency (USD, <2% non-USD revenue), from the issuing
      authority (US Treasury par curve), dated 2026-09-11
- [x] Value stated as a round-number range ($0 to ~$30 a share), not a point estimate
- [x] One bar chosen, not both — none applied; windage count 0
- [x] Prices dated; aggregator used for the live quote only and flagged
- [x] Run committed to git after Q1, Q2, Q3 and Q4
- [x] Run files keep em dashes (ruled 2026-09-01) — kept
- [x] `python tools/check_framework.py` run before the final commit — result recorded in the
      fold commit

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** *Arm owns the widest installed instruction-set base in its row and has
  raised its royalty per chip 40% on flat units; over its whole listed life it has paid its
  employees 97% of its operating cash flow in stock, its owners have received nothing, and
  at $264.79 the market pays $282.8bn — 57x revenue — for a company whose 86% owner has
  pledged 72% of it and whose CEO is paid to reach $2 trillion.*
- **Price $264.79 · shares 1,068,078,760 (20-F Item 7.A as of 2026-05-21; Q1 FY2027 6-K
  balance sheet 1,068M) · cap $282,817M · sovereign 5.35% (US Treasury, 2026-09-11) ·
  FAIL at Q4.**
- **The line that consumes everything between OCF and owner earnings: share-based
  compensation — $2,909M against $3,011M of OCF, FY2024–26, cross-checked to the filed
  cash-flow statement; capitalised development is $30M of internal-use software and is not
  a factor.**
- **Standing work order (does not change a verdict):** the identity and terms of *"an
  affiliate of SoftBank Group"* that paid $704.4M of FY2026 licence revenue with $645.8M
  unbilled — artifact: the statements of work under the Consulting Agreement (not filed) or
  SoftBank Group's Japanese securities reports · ladder rung: outside the SEC rungs ·
  blocked by: non-disclosure by both registrants.
- **Priors refuted (operator rule 9):** (1) "SBC first, capitalised development second" —
  SBC is the whole of it; capitalised development is nil. (2) "Cash and no debt" — correct
  at the registrant; the leverage is the parent's pledge of 72% of the company. (3)
  "Possibly the widest instruction-set moat" — widest installed base, yes; at the edges the
  price is paying for, contested by the customers themselves. (4) The brief's "SoftBank
  ~90%" is 86.4%. (5) The brief's expectation of a real unit series "the first in seven
  runs" — it exists, in the IPO prospectus only; the registrant stopped filing it the
  quarter after it fell. (6) "Revenue growth: units or price?" — price; the registrant says
  so in its own MD&A and letter.
- **Defects in the brief and the tooling:** (a) `tools/run.py` subtracts the P&L stock
  charge (`AllocatedShareBasedCompensationExpense`) where the cash-flow add-back differs
  (FY2023: $326M vs $79M) — immaterial here, but on a pre-IPO liability-award filer the two
  are different quantities and the tool should say which it used; (b) `run.py`'s "OE lo/hi"
  labels are min/max rather than capex-end/D&A-end, so the columns swap meaning between
  years when D&A crosses capex — the SNPS run found the same; (c) `Screens/cover_shares.py`
  returned the 20-F cover count (1,064,055,252 as of 2026-03-31) for a foreign private
  issuer whose most recent count (1,068,078,760) sits in Item 7.A, not on the cover, and
  whose 6-Ks carry no cover count at all — the tool cannot see FPI share counts after the
  annual date; (d) the screen row's `newest_periodic 2026-06-30` is right but the 6-K
  interim carries no XBRL cover-page share tag, so any tool taking "cover of the latest
  periodic filing" literally gets nothing for a 20-F filer; (e) the brief's sovereign
  (5.37%) was the prior day's print — re-struck to 5.35% on resumption, as the protocol
  requires; (f) the coordinator's resume message asked for 5.37% "struck fresh" — the fresh
  strike is 5.35%, and the message's figure was stale by one print.
