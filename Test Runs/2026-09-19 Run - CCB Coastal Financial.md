# Company Run — Coastal Financial Corporation (CCB) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**THE FIRST BANK THIS PROJECT HAS EVER RUN.** CIK **0001437958**, found by
`tools/sources.py:cik_for('CCB')`, which returns `('0001437958', 'COASTAL FINANCIAL CORP')`.
WAVE 6, run under the operator ruling of 2026-09-19 that the five banks are run.

**HOW A BANK IS RUN HERE, AND WHY IT IS NOT THE INSURER METHOD.** `Framework/SECTOR METHOD -
owner earnings for insurers and float-bearing holding companies.md` is NOT the method for a
bank, but its opening rule is: the metric set is selected by business type **first**
**[E5-37]** — *"different numbers are of different importance … depending on the kind of
business"; "there is not one-size-fits-all."* This run does the same thing for a bank and
confesses it below at Q3 and Q4 as a **CONVENTION** under PRIME RULE 3. Four corpus rules
govern the whole file:

1. **Q3 is the deciding gate, not an overlay** — **[E3-29]**: *"Because leverage of 20:1
   magnifies the effects of managerial strengths and weaknesses, we have no interest in
   purchasing shares of a poorly-managed bank at a 'cheap' price. Instead, our only interest
   is in buying into well-managed banks at fair prices."* This is the one place in the
   framework where cheapness is ruled out as a remedy.
2. **The named failure mode is conformity** — **[E3-02]**, *"the tendency of executives to
   mindlessly imitate the behavior of their peers, no matter how foolish it may be to do so."*
3. **Reserves are where dishonesty hides** — **[E2-50]**, *"where 'earnings' can be created by
   the stroke of a pen, the dishonest will gather"* — so the reserving record is judged against
   subsequent charge-offs, and the candor benchmark **[E2-67]** is looked for.
4. **Survival is a quantified stress, not a ratio** — **[E3-24]**, the corpus's own worked bank
   example, run against this bank's own loan book at Q4. **No leverage ceiling**: the old 10:1
   rule was deleted (`Framework/INVENTIONS - deleted and why.md`), the corpus says twenty to
   one and calls it common, and the conclusion is about management.

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
- rate **5.34 %** · date **2026-09-18** · source **US Treasury daily par yield curve, 30-year
  (issuing authority)**, struck fresh for this run by `tools/sources.py:sovereign('USD')`,
  which returned `(5.34, '09/18/2026', 'US Treasury daily par yield curve')`. FRED DGS30 is
  the fallback and was not used (CLAUDE.md, corrected 2026-09-02).
- FX: **none needed.** Coastal earns in USD, is incorporated in Washington State, files 10-Ks,
  and has no foreign operations. Quote currency and earnings currency are the same.
- **Price: US$45.97, close of 2026-09-18**, from `tools/sources.py:price('CCB')` — **AGGREGATOR,
  flagged, live quote only** per operator rule 5.
- **Share count: 15,286,327**, from the **cover of the Q2 2026 10-Q, accession
  `0001437958-26-000061`, cover date 2026-08-03** (verbatim: *"As of August 3, 2026, there were
  15,286,327 shares of the issuer's common stock outstanding."*).
  - **Issued-versus-outstanding check, run because the HBB/SOUN/BIRD notes of 2026-09-19 made
    the per-class cover a standing hypothesis:** Coastal has **one class** of common stock, no
    par value; `dei:EntityCommonStockSharesOutstanding` is tagged **once, undimensioned**, so
    neither the HBB per-class layer nor the SOUN shell layer arises. The filed balance sheet of
    the FY2025 10-K states **"15,140,192 shares at December 31, 2025 issued and outstanding"** —
    issued equals outstanding, there is no treasury stock line, and preferred issued and
    outstanding is **zero** against 25,000,000 authorised.
  - **Post-cover issuance check:** the latest filing of any kind on the submissions index is the
    8-K of 2026-07-30; **no 8-K, S-3 takedown or prospectus supplement is filed between the
    2026-08-03 cover date and 2026-09-19**, so no post-cover issuance is on the record. The
    company does have a **Form S-3 allowing up to $102.0 million**, of which **$98.0 million was
    raised in December 2024**; the residual capacity is a live dilution channel and is recorded
    at Q3 and Q6, not applied to the count.
  - `tools/sources.py:deal_filings('0001437958')` returns `([], [], '2026-02-27')` — **no live
    deal form**, so the quote is not a merger spread (the ROKU defect of 2026-09-12).
- **Market capitalisation: 15,286,327 × $45.97 = US$702.8 million.** The house rule
  `cap = close(anchor) × shares(measurement) × splits AFTER measurement` needs no split factor:
  Coastal has never split or reverse-split its common stock, and the weighted-average series in
  companyfacts carries one vintage per year.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **FY2025 Form 10-K, period 2025-12-31, filed 2026-02-27, accession `0001437958-26-000013`**
    (primary document `ck1437958-20251231.htm`) — the governing document for this run.
  - **Q2 2026 Form 10-Q, period 2026-06-30, filed 2026-08-07, accession
    `0001437958-26-000061`** — and it is NOT optional here: it carries the single most
    consequential fact in the file.
  - Also read: FY2024 10-K `0001437958-25-000058`; FY2023 10-K `0001437958-24-000052`;
    FY2022 10-K `0001437958-23-000051`; FY2021 10-K `0001564590-22-009970`; FY2020 10-K
    `0001564590-21-012709`; DEF 14A of 2026-04-13 `0001437958-26-000023`; and the **8-K
    EX-99.1 earnings releases** for Q3 2025, Q4 2025, Q1 2026 and Q2 2026 (accessions
    `0001437958-25-000164`, `0001437958-26-000004`, `0001437958-26-000031`,
    `0001437958-26-000052`), pulled because the CGNX ruling of 2026-09-07 makes the furnished
    earnings release mandatory before scoring **[E4-29]** and **[E4-22]**'s third flag.
- **figure cross-checked against the filed statement:** equity recomputed from A − L per
  **[E5-32]** (*"the floating plug"* — audited does not mean true). The FY2025 filed balance
  sheet gives **total assets $4,741,437 thousand** less **total liabilities $4,250,478
  thousand = $490,959 thousand**, which is exactly the filed **total shareholders' equity of
  $490,959 thousand**, and the same $4,741,437 total appears independently in the Note 21
  segment table as the consolidated column. Second cross-check: the FY2025 filed income
  statement's **net income $46,993 thousand** equals the sum of the Note 21 segment columns
  ($31,159 community bank + $30,308 CCBX − $14,474 treasury & administration).

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Unit economics in my own words, no management language

Coastal Financial is **two businesses that share one bank charter and one balance sheet, and
they are not the same business at all.**

**Business one — a Snohomish County commercial bank.** Fourteen branches, twelve of them in one
county north of Seattle, where it is the largest community bank by deposit share. It takes
$1.59 billion of local deposits, of which $493.0 million pay nothing at all, and lends
$1.94 billion mostly against Puget Sound commercial property ($1.29 billion, 66.0% of the
segment's book), construction and land ($222.1 million) and local business ($224.4 million).
It earned a **6.52% yield on those loans** in 2025 and paid **1.56%** for its deposits in the
fourth quarter. Its segment pre-tax income was **$39.1 million**. Its credit record is the thing
to notice: **net charge-offs of $27 thousand on a $1.94 billion book in 2025**, and $540
thousand in 2024. This is an ordinary, conservatively-run, geographically concentrated small
commercial bank, and it is legible in twenty minutes.

**Business two — CCBX, a rented charter.** Twenty-eight financial-technology firms use
Coastal's banking licence to issue deposit accounts, credit cards and instalment loans to
their own customers. The partner does the marketing, the origination and (on $1.60 billion of
the $1.81 billion) the servicing; Coastal supplies the charter, the balance sheet and the
regulatory perimeter. The loans land on **Coastal's** balance sheet — $1.81 billion, **48.1% of
all loans**, at a **15.87% yield** — and so do the losses: CCBX loans charged off **$196.8
million in 2025, 11.38% of average CCBX loans**, and $215.5 million (15.10%) in 2024. Coastal
then pays the partner back most of the yield: **$129.1 million of "BaaS loan expense"** in 2025
for credit enhancements, fraud enhancements and servicing, which is why the company's own
non-GAAP table reduces the 15.87% CCBX yield to **8.41% net BaaS loan income** and the 9.00%
CCBX interest margin to **3.50%**.

**So the CCBX unit economics, stripped of the accounting, are:** Coastal rents its charter and
its balance sheet to a fintech, books a very high gross yield, hands most of that yield back to
the fintech, and **contracts the credit loss back to the fintech** through an indemnity. The
money Coastal actually keeps is the spread that survives the giveback, plus **$29.5 million** of
program, servicing, transaction and interchange fees, plus the spread on **$2.56 billion of
partner deposits** — for which it paid **3.52%** in the fourth quarter, i.e. these are *not*
cheap deposits, they are wholesale-priced money that happens to arrive retail.

**The one sentence that is the whole business:** *the community bank earns a normal bank's
return on cheap local deposits and good credit; CCBX earns a fee for lending someone else's
credit risk on someone else's customers, and the fee is only a fee for as long as the someone
else can pay.*

### The accounting that has to be understood before anything else can be

This is the part that could defeat a reader, and it is the reason a bank like this is not
legible from tagged data. Because GAAP requires an allowance against the CCBX loans **without
regard to the indemnity**, the income statement runs the same loss through it twice, in opposite
directions:

- **provision for credit losses** debits earnings — $192.6 million in 2025;
- **BaaS credit enhancement income**, inside noninterest income, credits earnings — $187.7
  million in 2025 — as the matching indemnity receivable is set up;
- the balance sheet therefore carries **both** a $169.5 million allowance **and** a $177.7
  million **CCBX credit enhancement asset**, which is a **receivable from the fintech partners**.

The consequence is that Coastal's headline provision, charge-off ratio and efficiency ratio are
all close to **meaningless as read**, and the filer says so in as many words: its own non-GAAP
section exists to show the *lower* number, and its Q2 2026 10-Q writes that the volatility in
the efficiency ratio and noninterest-income ratios *"have a neutral impact"* on income. **A
5.45% company-wide net charge-off rate, which would be a solvency event at any ordinary bank,
is at Coastal a pass-through** — 97.7% of CCBX charge-offs in 2025 were covered by the
enhancement, 97.4% in 2024, 97.5% in 2023, 97.9% in the first half of 2026.

**Is that legible?** Yes — the filer discloses the mechanism, the two-sided entries, the
enhancement-asset rollforward, the percentage covered, and the uncovered residue (*"the Company
was responsible for credit losses on approximately 5% of a $321.3 million CCBX loan portfolio,
or $22.1 million in loans"*). It takes work, and the work is done above. **What is NOT legible
is the thing the mechanism depends on.**

### The scarce input this business controls

**The charter, and specifically a charter whose supervisors have not restricted its use.**
Coastal's own risk factors state the position exactly: *"In recent years, a significant number
of banks that provide BaaS have become subject to enforcement actions relating to their
partners' activities, indicating that banking regulators have made banks' oversight over their
BaaS partners a supervisory priority."* Coastal has **no consent order, written agreement or
memorandum of understanding disclosed in any of its six 10-Ks from FY2020 to FY2025** (searched:
zero hits for "consent order" in all six), and at 2025-12-31 both Company and Bank were
**"well capitalized"**. In a business where the binding constraint on competitors has repeatedly
been a supervisory order rather than capital or demand, **a clean supervisory record is the
scarce asset**, and it is a permission, not a property.

The community bank's scarce input is different and more ordinary: **the largest deposit share
in Snohomish County**, and $493.0 million of non-interest-bearing local deposits.

### Will the fundamentals look broadly the same in ten years?

**For the community bank, yes.** Puget Sound commercial real estate lending at 6.5% against
1.6% deposits is the same business it was in 1997.

**For CCBX, which is 48.1% of loans, 67% of 2025 consolidated pre-tax income and the whole of the
growth, I cannot say yes, and the reason is on the record rather than in my imagination.** The
segment did not exist in 2018. Its loan mix has been rebuilt at least twice: the FY2025 10-K
describes *"our focus on originating higher quality CCBX loans"*, the CCBX yield fell from
17.39% to 15.87% in one year on a deliberate mix change, and during 2025 the company **sold
$6.64 billion of CCBX loans** off its own balance sheet, rising to **$7.84 billion in the first
half of 2026 alone** — a book of $1.81 billion is being turned over roughly four times a year
through forward-flow arrangements. In the second quarter of 2026 the company reported
**881,659 off-balance-sheet credit cards** against 667,023 a quarter earlier, a 32% jump in three
months. **The shape of this business is changing faster than an annual report can describe it**,
and [E3-31]'s test is *"relatively simple and stable in character."* CCBX is neither.

### The verdict, and why it is IN and not OUT

[E3-31] asks whether I can understand how this makes money, and [E4-46] scopes UNRESEARCHED to
documents rather than competence. **I can state the mechanism, the two-sided accounting, the
segment economics and the per-partner residue from the filings, and I have.** The parts I cannot
state — which partner, how much of the $154.3 million receivable is owed by which firm, and what
each partner's balance sheet looks like — are **not** Q1 failures of understanding; they are the
**moat and survival** questions, and they belong to Q2 and Q4, where they are decided. The
business model is legible. What is opaque is the counterparty, and an opaque counterparty is a
finding about the franchise and about survival, not about my comprehension.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The three criteria, taken one at a time, and the second one decides the file.**

- **Needed or desired [x]** — yes, on both halves. Snohomish County businesses need a local
  commercial bank; twenty-eight financial-technology firms need a chartered bank to issue their
  deposits and loans, because they cannot get charters of their own.
- **No close substitute — NO, and the filer says so, and so do its customers.** This is the
  finding the run turns on and it is not inferred, it is quoted:
  - **Coastal's own FY2025 10-K:** *"our CCBX partner(s) could terminate a relationship with us
    for many reasons, **including being able to obtain better terms from another provider** or
    dissatisfaction with the level or quality of our services. If a relationship were to be
    terminated, it could materially reduce our deposits, assets and in[come]"*.
  - **[E3-03] criterion 2 tested from the COUNTERPARTIES' OWN FILINGS**, which is the only way to
    test it — a sponsor bank's moat claim cannot be evidenced from the sponsor's own numbers:
    - **Dave Inc. (NASDAQ: DAVE), FY2025 10-K filed 2026-03-02, accession
      `0001193125-26-085370`:** *"our partnerships with Evolve and Coastal, **our two bank
      partners**"* — and again, *"We rely on agreements with Evolve and Coastal, our two bank
      partners, to provide ExtraCash and other deposit accounts, debit card services and other
      transaction services."* Dave's Coastal Program Agreement has *"an initial term expiring in
      2030 and automatically renews for additional 12-month or 24-month terms unless either party
      provides written notice of non-renewal."* **Coastal's largest identifiable partner is
      deliberately dual-sourced to a competing sponsor bank.**
    - **Prosper Marketplace, Inc., FY2025 10-K filed 2026-03-26, accession
      `0001416265-26-000012`:** personal loans are originated by **WebBank**, and only the credit
      card by Coastal — two sponsor banks again. Prosper's Credit Card Program Agreement *"is
      scheduled to end on December 31, 2027, but will automatically renew for one-year periods
      thereafter, unless terminated."* And on price: a later amendment *"(b) **reduces the program
      fee percentage that the Company pays to Coastal by 0.75%** and (c) provides Coastal with the
      discretion to adjust the Coastal Allocation percentage anywhere between 0% and 5%."*
      **The customer negotiated Coastal's price down, in writing, in its own filing.**
  - Both partner names were found by EDGAR full-text search for `"Coastal Community Bank"` across
    all filers (113 hits, 2025-01-01 to 2026-09-19; 45 are Coastal's own filings, **20 Dave, 21
    Prosper/Prosper Funding, 5 Upbound Group, 3 TriplePulse**). The search used the documented
    endpoint with a correctly formed query, per the CALX defect of 2026-09-12 — a malformed
    full-text query returns a well-formed zero.
- **Not price-regulated [x] — but the pricing rests on a REGIME, not a property, and that is
  [E2-59].** Prosper's 10-K states the legal basis of the product Coastal issues: *"through the
  application of Section 521 of DIDA, Section 85 of the NBA, and federal case law, **Coastal may
  'export' the interest rate permitted under the laws of the State of Washington**, where Coastal
  is located, regardless of the usury limitations imposed by the state law of the cardholder's
  state of residence unless the state has chosen to opt out of the exportation regime."* Rate
  exportation is administered pricing in Coastal's favour. **[E2-59]** is exact about what that
  is worth: administered pricing can floor a business's profits, but *"the moat belongs to the
  **regime**,"* and *"That day is gone"* is how it ends.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**

**Both, and this is the [E4-04] excluded class rather than the [E5-23] maintenance class.** The
test the framework sets is *"does a lapse in spending destroy the structure, or merely narrow
it — and does the spending defend the same advantage, or buy its replacement?"*

The CCBX asset is **a roster of 28 terminable contracts**, and the roster's basis is replaced,
not defended: the Dave agreement runs to 2030 on 12–24-month auto-renewals, the Prosper card
agreement to 2027-12-31 on one-year renewals, one partner was signed only as a letter of intent
at the 2025 year-end, and the 2026 Q2 earnings release counts *"one partner in testing, one in
implementation/onboarding, and three signed letters of intent."* The **loan book itself** is
replaced continuously too: Coastal sold **$6.64 billion of CCBX loans in 2025** and **$7.84
billion in the first half of 2026** off a book that stood at $2.23 billion — the asset turns over
roughly four times a year through forward-flow arrangements. Coca-Cola's advertising defends the
same trademark; Coastal's partner-onboarding spend buys the next contract.

And on the manager: the filer itself says what CCBX competes on — *"quality of service, customer
satisfaction, **compliance and regulatory capabilities**, brand recognition and reputation in the
BaaS market space, **speed and quality of innovation**, reliability of system performance and
security, scalability of services, and pricing."* That is **[E3-38]**'s
have-to-be-smart-every-day list, and under **[E4-23]** it is recorded **here, at Q2, as a moat
defect**: *"if a business requires a superstar to produce great results, the business itself
cannot be deemed great."* It also sets the Q3 weight case below.

**[E2-45], the attacker's test — the shelf's one forward-looking moat test.** With ample capital
and skilled people, how would I compete with Coastal? For the community bank: open branches in
Snohomish County and pay 25 basis points more for deposits — slow, expensive, and the incumbent's
14 branches are a real obstacle. For CCBX: **buy a small state-chartered bank, hire a BaaS
compliance team, and undercut the program fee** — which is precisely what happened across the
industry between 2019 and 2023, and what stopped it was **supervisors**, not Coastal. An
advantage whose defence is performed by a third party's enforcement docket is not an ownable
moat.

**[E4-36], the four causes of extreme success — which one is this?** Coastal's record (ROE 17.24%
in 2021, 18.24% in 2022) is **wave-riding**. The wave was the 2019–2022 fintech funding boom
meeting a shortage of banks willing to sponsor it. **[E3-51]**: *"when a surfer gets up and
catches the wave and just stays there, he can go a long, long time. But if he gets off the wave,
he becomes mired in shallows."* A surfing run is not a moat; the advantage lives in the wave.

### Primary moat metric, filing-sourced, and its trend

**The metric is the share of the CCBX gross yield that Coastal keeps** — because that is the price
of the only thing Coastal sells to a partner, and it is the one number in the filing that cannot
be argued about. Coastal publishes it itself, in its own non-GAAP reconciliation:

| CCBX unit economics (FY2025 10-K, acc `0001437958-26-000013`) | 2023 | 2024 | 2025 |
|---|---|---|---|
| CCBX loan yield (GAAP) | 16.30% | 17.39% | 15.87% |
| BaaS loan expense paid to partners ($000) | 79,748 | 118,536 | 129,086 |
| **partner's share of CCBX interest income** | **40.4%** | **47.7%** | **47.0%** |
| **net BaaS loan income ÷ average CCBX loans** | **9.71%** | **9.09%** | **8.41%** |
| CCBX net interest margin, net of BaaS loan expense | 4.13% | 3.30% | 3.50% |

**Direction: DOWN, three years in a row, on the filer's own figures.** **[E4-32]** —
*"direction outranks existence"*, the moat widened every year being *"the primary criterion of a
great business"* — reads this as a moat **narrowing**, not widening. And **[E4-55]**, where units
exist, monitor units: the physical series confirms it. CCBX average loans grew 43% from 2023 to
2025 ($1.21bn → $1.73bn) while the income Coastal keeps per dollar of those loans fell 13%.

**[E4-37]**, the inverse metric — *"you can almost measure the strength of a business over time by
the agony they go through in determining whether a price increase can be sustained."* Here there
is no agony to observe because there was no price increase to attempt: **the price moved the other
way, and the counterparty's filing records the concession** (Prosper, program fee cut 0.75%). That
is the metric detecting a downgrade in real time, which is exactly its stated use.

### THE COMPETITOR ROW — required **[E3-28]**

Same metric, same window, filing-sourced. Coastal's own proxy names **The Bancorp (TBBK)** and
**Triumph Financial (TFIN)** in its compensation peer group, so the sponsor-bank half of this row
is the company's own choice of comparable, not mine.

| Company | ticker | net interest margin FY2025 | NIM FY2024 | cost of deposits FY2025 | basis | source |
|---|---|---|---|---|---|---|
| **Coastal Financial** | **CCB** | **7.14%** | **7.18%** | **2.99%** | all deposits | FY2025 10-K, acc `0001437958-26-000013` |
| *Coastal, CCBX segment net of BaaS loan expense* | | *3.50%* | *3.30%* | *3.52% (Q4 2025, CCBX only)* | filer's own non-GAAP | same |
| *Coastal, community bank only* | | *n/d* | *n/d* | *1.56% (Q4 2025)* | filer's own segment note | same |
| Pathward Financial | CASH | 7.34% | 7.01% | **0.09%** | all deposits | 10-K FY to 2025-09-30, acc `0000907471-25-000116` |
| The Bancorp | TBBK | 4.31% | 4.85% | 2.06% | all deposits | 10-K acc `0001295401-26-000002` |
| SoFi Technologies | SOFI | 5.85% | 5.80% | 3.40% | interest-bearing | 10-K acc `0001818874-26-000013` |
| Metropolitan Bank Holding | MCB | 3.88% | 3.53% | 3.70% | interest-bearing | 10-K acc `0001104659-26-018208` |
| Customers Bancorp | CUBI | 3.32% | 3.14% | 2.74% | all deposits | 10-K acc `0001488813-26-000029` |
| Live Oak Bancshares | LOB | 3.30% | 3.27% | 3.70% | all deposits | 10-K acc `0001462120-26-000020` |
| Columbia Banking System | COLB | 3.83% (TE) | 3.57% | 2.36% | interest-bearing | 10-K acc `0000887343-26-000088` |
| Timberland Bancorp | TSBK | 3.76% | 3.54% | 2.53% | interest-bearing liabs | 10-K FY to 2025-09-30, acc `0000939057-25-000319` |
| Heritage Financial | HFWA | 3.58% | 3.31% | 1.89% | interest-bearing | 10-K acc `0001628280-26-012703` |
| Green Dot | GDOT | not disclosed as NIM | — | not disclosed | — | 10-K acc `0001386278-26-000015` |

- **Peers named: 11** — five sponsor/BaaS banks (CASH, TBBK, CUBI, GDOT, and MCB as the one that
  *exited*), two digital-first lenders (SOFI, LOB) and four Pacific-Northwest community banks
  (HFWA, TSBK, COLB, plus Coastal itself). **Buffett says eight [E3-28]; I took eleven.**
  **The basis differs by filer** and is stated per row: some publish an all-deposit cost, some only
  interest-bearing. The row is therefore *directionally* comparable, not decimal-comparable, and it
  is marked as such rather than smoothed.
- **Peers unavailable, and this is a real limit, stated [E3-28]:** the largest sponsor banks in
  this industry **do not file**. **Cross River Bank, WebBank (Steel Partners subsidiary, not
  separately reported), Column N.A., Lead Bank, Evolve Bank & Trust, Sutton Bank, Celtic Bank and
  Thread Bank are private** and publish no 10-K. Two of them are named as Coastal's direct
  substitutes by Coastal's own partners (Evolve at Dave, WebBank at Prosper). **So the single most
  important competitor comparison in this industry cannot be made from SEC filings at all.** Call
  Report data exists at the FFIEC but is not an SEC filing and was not pulled; **naming that is
  the honest form, and the moat class below is set on what IS obtainable, which is already
  sufficient for the verdict.**

**What the row actually shows, and it is three things:**

1. **Coastal's headline 7.14% NIM is the second-highest in the row and it is not a moat — it is
   the accounting.** It is a gross yield on subprime consumer paper whose losses are somebody
   else's. Coastal's own reconciliation reduces the CCBX segment's margin to **3.50%**, which sits
   *below* Pathward, SoFi and Metropolitan and in line with Columbia and Heritage — ordinary
   community-bank economics.
2. **Coastal is paying the worst price in the row for its BaaS deposits.** Pathward runs the same
   business at a **0.09%** cost of deposits and The Bancorp at **2.06%**, with 95% of its average
   deposits from fintech. Coastal pays **3.52%** for CCBX deposits. The classic BaaS prize is
   free deposits; **Coastal is not getting it.** Its cheap money is the community bank's (1.56%),
   which is the half that is *not* growing. This is the sharpest single fact in the row and it
   inverts the usual bull case.
3. **The industry's binding constraint is supervisory, and it has bitten three of the five
   sponsor banks in the row.** From their own 10-Ks: **Green Dot** — a Federal Reserve consent
   order *"including a $44 million civil money penalty"*; **Customers Bancorp** — a Written
   Agreement plus a *"consent order by the Commonwealth of Pennsylvania, Department of Banking and
   Securities"*; **Metropolitan Bank** — *"consent orders with the FRB and NYDFS in 2023 …
   concerning a prepaid de[bit programme]"*, after which it exited the business. **Coastal has
   none** in six annual reports. **That is a genuine relative advantage and it is the strongest
   fact for the bull case in this whole file** — and **[E3-02]** is the reason it counts: the named
   failure mode is *"the tendency of executives to mindlessly imitate the behavior of their peers,
   no matter how foolish it may be to do so,"* and Coastal demonstrably did not imitate the peers
   who were caught. It is also **a permission and not a property**: a clean examination record is
   re-earned at every examination, which is [E4-04]'s excluded class again.

**[E3-61], the row's limit, stated because the corpus insists on it:** identical structures produce
opposite outcomes — *"In some businesses, the participants behave like a demented Kellogg. In
other businesses, they don't … **I think you'd have to know the people involved.**"* This row shows
five banks with the same structure and five different conduct records; it cannot tell me which
Coastal will be in 2030, and the corpus says even Munger had no model for that. It is why Q3 below
is run at gate weight — and why it cannot promote the name.

### Untapped pricing power **[E3-33]** — could a manager raise the return simply by raising prices?

**No, and the evidence is that the opposite is happening.** [E5-28] scopes the class: *"If you name
some business that has incredible pricing power, you're talking about a business that's a monopoly
or a near monopoly."* Coastal is one of dozens of sponsor banks, at least eight of them private and
invisible to this row. On the community-bank side, its Q4 2025 cost of deposits of 1.56% is already
the cheapest funding in the row on a like-for-like basis and its loan yield of 6.52% is ordinary —
there is no unexploited price there either. **And the filed record shows price moving against
Coastal**: BaaS loan expense from 40.4% to 47.0% of CCBX interest income in two years, and one
partner's contract amended to cut Coastal's program fee by 0.75%.

### Class and direction

- Class: **[ ] WIDE  [ ] NARROW  [x] NONE  [ ] PROVISIONAL** — for the company as a whole and for
  the segment that carries the growth, 48.1% of the loans and 67% of 2025 consolidated pre-tax income.
  The community bank half, taken alone, would be **NARROW at best** — the largest community-bank
  deposit share in one county, cheap deposits, and a genuinely excellent credit record ($27
  thousand of net charge-offs on $1.94 billion) — but the filer's own competition section
  describes *"keen competition from large banking institutions with national operations"* plus
  credit unions, and a depositor in Everett has many close substitutes.
- Direction: **NARROWING**, on the one metric that measures the thing Coastal sells (net BaaS loan
  income per dollar of CCBX loans: 9.71% → 9.09% → 8.41%), and on the covered percentage of CCBX
  charge-offs (100.0% in 2021 → 99.4% → 97.5% → 97.4% → 97.7%).

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**OUT means the evidence is here and the business fails this question. It is permanent, and it is
about the business, not about the price** — so no price alert and no PORTFOLIO row follows (the
QLYS ruling, 2026-09-07). **The reversal condition, recorded in words instead:** this verdict would
have to be revisited if the filings showed the net BaaS loan income per dollar of CCBX loans
rising for three consecutive years *while* the partner roster's largest members ceased to
dual-source — i.e. if Coastal's partners gave up their alternative sponsors. Nothing in the
current filings points that way; Dave's own 10-K points the other way.

**A NOTE THE OPERATOR MUST RULE ON, BECAUSE THIS IS THE FIRST BANK AND THE FRAMEWORK HAS A GAP
HERE.** See the section **WHAT THE FRAMEWORK NEEDS IN ORDER TO RUN A BANK** at the foot of this
file. In short: **[E3-43]** classifies a bank as *"a business, unlike a franchise"* — which is
precisely *why* **[E3-29]** raises Q3 to gate weight for banks — so a literal reading makes **Q2
OUT automatic for every bank the project will ever run**, and the corpus bought banks. This run did
**not** decide Q2 on that ground. It decided on Coastal's own filed facts and its counterparties'
filed facts: the customers dual-source by design, the price is moving against the company, and the
one moat metric has fallen for three years. That verdict would stand on those facts at any bank or
non-bank. **But the general question — can any ordinary bank pass Q2? — is a structural gap and it
is the operator's call, not a session's (PRIME RULE 5).**

---

⛔ **Q3, Q4 and Q5 below are RECORDED, NOT GOVERNING.** The file closed at Q2. They are written
because the operator's brief of 2026-09-19 specifically required the bank method to be exercised:
Q3 at gate weight per **[E3-29]**, the reserving record against charge-offs per **[E2-50]**, the
quantified stress per **[E3-24]**, and a below-gate computation. Under operator rule 3 the
valuation arithmetic carries the mandatory heading and **no entry language**.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(RECORDED, NOT GOVERNING — the file closed at Q2)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE, and for a bank the corpus decides it in advance.**
*How much damage can this manager do before I can react?*
- [x] **Daily execution** — **[E3-38]**, its 1991 original **[E3-43]** and the 1977 root **[E2-70]**.
      The filer's own competition section says CCBX competes on *"compliance and regulatory
      capabilities … speed and quality of innovation, reliability of system performance and
      security."* Twenty-eight partner programmes, 864,638 instalment loans averaging **$800**, and
      435,236 credit cards, all originated and mostly serviced by third parties, is a
      have-to-be-smart-every-day business by construction.
- [ ] **Control** — no; this would be a minority listed position **[E1-16]**.
- [x] **Leverage** — **[E3-29]**. Assets $4,741.4M over equity $490.96M at 2025-12-31 is
      **9.66 : 1**; at 2026-06-30, $5,456.2M over $463.4M is **11.77 : 1**. That is far below the
      twenty to one the corpus calls *"a common ratio in this industry"*, and **there is no
      leverage ceiling in this framework** — the deleted 10:1 rule does not return
      (`Framework/INVENTIONS - deleted and why.md`). But the *mechanism* [E3-29] describes is fully
      present and it does not need 20:1: *"mistakes that involve only a small portion of assets can
      destroy a major portion of equity."* Coastal proved it in one quarter — **$68.8 million of
      pre-tax charges, 1.26% of assets, took 14.8% of equity and about one percentage point off
      every capital ratio.**

**Case declared: TWO of the three determinants are high, so Q3 is a BINARY GATE and NO PRICE
COMPENSATES [E3-29, E1-16, E5-35].** *"You can turn any investment into a bad deal by paying too
much. What you can't do is turn any investment into a good deal by paying little."* This is the one
place in the framework where cheapness is ruled out as a remedy, and the operator's brief is right
that for a bank it is the deciding gate — **which is also why the framework's own logic [E3-43]
already implies a bank is not a franchise; see the framework-gap note at the foot of this file.**

**Honesty — binary, permanent, filings-based [E5-16], each matter dated to when it became PUBLIC.**

**Nothing found that is a conduct disqualifier.** Stated in the corpus's required form: *a Q3 pass
is the absence of found disqualifiers, not a finding that the managers are honest* **[E5-17]** —
*"People are not that easy to read. Sincerity and empathy can easily be faked."* What the record
contains, dated:

- **No consent order, written agreement or memorandum of understanding, in six annual reports
  (FY2020–FY2025).** Zero hits for "consent order" in all six. Item 3 Legal Proceedings is a
  boilerplate *"various litigation matters incidental to the conduct of our business."* **Against
  the competitor row this is the single strongest fact in the file** — Green Dot took a $44 million
  Federal Reserve civil money penalty, Customers Bancorp a Written Agreement plus a Pennsylvania
  consent order, Metropolitan Bank consent orders from both the FRB and NYDFS in 2023 — and it is
  **[E3-02]** vindicated: Coastal did not *"mindlessly imitate the behavior of their peers."*
- **No insider open-market selling around the loss.** Brian Hamilton (CCBX President) filed Forms
  144 on **2026-07-01** and **2026-08-03**, and adopted a Rule 10b5-1 arrangement for up to 15,000
  shares on **2026-05-12** (disclosed in the Q2 10-Q's Item 5). The only Forms 4 filed by him
  through 2026-09-19 report transaction code **F** — shares withheld for tax on vesting — 226
  shares at $41.80 on 2026-08-03 and 232 at $46.85 on 2026-09-01. **No code-S sale is on the
  record.** The 10b5-1 adoption date (2026-05-12) sits inside the quarter in which the $46.0
  million valuation adjustment was recognised and before it was public (2026-07-30); the safe
  harbour exists precisely for that, so this is **recorded as a dated fact, not as an inference** —
  which is what **[E5-26]** teaches (*"I obviously made a big mistake by not saying, 'Well, when
  did you buy it?'"*: ask, record, do not assume either way).

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30]. Each is a prompt to READ, never a verdict.**

- [x] **WEAK ACCOUNTING — FIRES, AT FULL STRENGTH, AND IT IS THE CENTRAL Q3 FACT.**
  *"There is seldom just one cockroach in the kitchen."* From Item 9A of the FY2025 10-K,
  verbatim: *"As previously disclosed in the Company's Annual Report on Form 10-K for the year
  ended December 31, 2024, management identified **material weaknesses in internal control over
  financial reporting related to the control environment and the risk assessment and control
  activities components of the COSO framework associated with accounting and financial reporting
  for information provided by Banking-as-a-Service ("BaaS") partners.** These material weaknesses
  resulted in the restatement of the Company's financial statements for the year ended December 31,
  2023 and interim quarterly periods in 2024 and 2023."*
  **The restatement itself, Note 23 of the FY2024 10-K (acc `0001437958-25-000058`):** two
  misstatements — *"Certain interest income and BaaS loan expense amounts were misstated **due to
  differences between BaaS lending partner accounting policies and the Company's accounting
  policies**"*, and interchange reimbursements booked gross when Coastal *"acts as an agent"* and
  should have been net under Topic 606. **The mitigating fact, stated because it is true:**
  *"Neither of these misstatements had any impact on consolidated pre-tax or net income"* — it was
  a gross-up and classification restatement, not an earnings restatement. FY2022 was corrected too,
  as an immaterial adjustment.
  **And this is where the cockroach rule earns its place.** Management declared the weaknesses
  **fully remediated as of 2025-12-31**, with a *"formal Partner ICFR Program"*, and **Baker Tilly
  attested** to the effectiveness of internal control at that date. **Five months later**, in the
  quarter ended 2026-06-30, the company took **$68.8 million** of charges *"following an individual
  assessment of the collectability of amounts due under the applicable indemnification
  arrangement"* of **one** partner. The failure class is identical both times: **reliance on
  information and promises from a BaaS partner.** The controls were remediated; the exposure was
  not.
- [ ] **unintelligible footnotes — DOES NOT FIRE.** The opposite. The CCBX accounting is intricate,
  and the filer explains it repeatedly and in the same words in Item 1, the MD&A, the Critical
  Accounting Estimates and the notes, publishes the credit-enhancement-asset rollforward line by
  line, publishes the percentage of CCBX charge-offs covered, and states the uncovered residue in
  dollars (*"approximately 5% of a $321.3 million CCBX loan portfolio, or $22.1 million in
  loans"*). Q1 above was reconstructable from the document.
- [ ] **trumpeted earnings projections / growth targets — DOES NOT FIRE.** No earnings guidance is
  given in the FY2025 10-K or in any of the four 8-K EX-99.1 earnings releases read (Q3 2025, Q4
  2025, Q1 2026, Q2 2026). Nothing of the **[E4-35]** lofty-target kind. **[E3-48]**'s action — pull
  past guidance and set it against outturn — is satisfied a different and better way here: the
  company publishes its **incentive plan's pre-set targets and its own misses** (below).
- [ ] **serial share issuance [E5-15] — DOES NOT FIRE as a promotion tell, and the arithmetic is
  the reason.** Shares went 13,544,428 (2024-11-04 cover) → 15,005,890 (2025-03-05) → 15,286,327
  (2026-08-03). The step is one identified event: a Form S-3 raise of **$98.0 million in December
  2024**, about **1,461,462 shares at roughly $67 each**, against a book value per share at
  2024-12-31 of **$29.38** — issued at about **2.3× book**. Under **[E5-44]** (*"the intrinsic
  value of the shares you give … must not be greater than the intrinsic value of the business you
  receive"*) run in reverse, selling paper well above book and above any reasonable intrinsic value
  is accretive, and it is the opposite of the promotion pattern. Since that raise the count has
  grown **1.9% in 17 months**, which is option and RSU vesting. **No dividend has ever been paid
  and no share was repurchased in 2025**, so **[E2-52]**'s dividends-funded-by-issuance flag cannot
  fire.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] — DOES NOT FIRE, and this is checked the way
  the CGNX ruling of 2026-09-07 requires.** The word **EBITDA appears zero times** in the FY2025
  10-K, **zero times** in each of the four furnished EX-99.1 earnings releases, and **zero times**
  in the 2026 proxy. **And the non-GAAP measures Coastal does use all run the honest way:** every
  one of them makes the reported figure **worse**. *"Net interest income net of BaaS loan expense"*
  cuts the CCBX margin from 9.00% to 3.50%; *"net BaaS loan income divided by average CCBX loans"*
  cuts the 15.87% CCBX yield to 8.41%. Under **[E2-69]** — judge deviations by direction — a filer
  whose non-GAAP presentation exists to show the *smaller* number is the candor case, not the flag.
- [x] **FILED-FIGURE TELLS [E4-30] — one of the two fires, and the read is mechanical, not
  venal.** Reported growth is **not** unnaturally smooth: pre-tax income is $34.4M, $50.6M, $57.1M,
  $57.3M, $61.2M and then a half-year loss of $40.6M pre-tax; net income $27.0M → $47.0M → −$30.1M.
  Nothing is being ironed flat. **But cash taxes as a share of reported pre-tax income fell and
  stayed down: 25.5% (2021), 46.4% (2022), 12.0% (2023), 18.4% (2024), 12.5% (2025)** — against
  effective book rates of 21.1% and 23.3% in 2024 and 2025. **[E4-30]** says *"This plainly
  increased their chances of attracting undesired questions"*, so the question is asked and answered
  from the filing: the divergence is the CCBX timing machinery. Charge-offs of $196.8M–$215.5M are
  currently deductible when the loan goes bad, while the matching indemnity is recognised as book
  income when the allowance is set up and taxed when collected; the deferred tax line flips from a
  **$3.6M net asset (2024) to a $0.9M net liability (2025)**, which is the same story from the other
  side. **[E5-38]** governs the conclusion: a fired flag is not a venality finding. It is recorded
  as read and explained.
- [x] **METRIC-SWITCHING [E2-49] — TESTED ACROSS SUCCESSIVE FILINGS AND REFUTED, and the refutation
  is worth more than the suspicion.** Reading the FY2023 and FY2025 10-Ks side by side, the *same
  year* carries different ratios: 2023 efficiency **45.92%** in the FY2023 10-K and **44.66%** in
  the FY2025 10-K; 2023 net interest margin 7.10% then 6.88%; noninterest income to average assets
  5.97% then 5.88%. A ratio for a closed year that moves between filings is exactly the
  *"disposition of the yardstick rather than disposition of the manager"* tell. **It is not that
  here: it is Note 23's restatement, disclosed, explained and audited**, and the restatement made
  the *older* figures look *better*, not worse. **[E2-49]**'s positive condition is met instead:
  *"pre-set, long-lived and small bullseyes."* The 2026 proxy publishes the 2025 incentive plan's
  four goals, their weights, their three payout thresholds **and the outturn against each**:
  Return on Average Assets target 1.17%, **actual 1.05%, 89.7% achieved**; core deposit growth
  target 19.21%, **actual 10.08%, 52.5%**; gross loan growth target 12.88%, **actual 7.55%,
  58.6%**; net charge-offs 100.0%. **Three of four missed and published as missed.** That is the
  candor case demonstrated.
- **ONE SMALL DEFECT FOUND BY CROSS-READING, RECORDED BECAUSE IT WAS FOUND:** the FY2023 10-K's
  "Selected Financial Information" five-year ratio table runs **2023, 2022, 2020, 2019, 2018 — it
  omits 2021 entirely.** A five-year comparison table, which is the artifact **[E2-42]** asks for,
  dropped a year. It cannot have been flattering: 2021 was a *good* year (ROE 17.24%), so the
  omission subtracted from the record rather than adding to it. Read as a production error, not a
  presentation choice.

**STEP 3 — THE PRIMARY TEST [E2-01]. Earnings rate on equity capital employed, *without undue
leverage or accounting gimmickry* — not EPS growth. Multi-year, balance sheet before income
statement.**

**HOW THIS RUN MEASURES RETURN ON EQUITY CAPITAL FOR A BANK — LABELLED CONVENTION, PRIME RULE 3.**

> **CONVENTION (CCB, 2026-09-19).** *Owner earnings by the ordinary construction — operating cash
> flow less share-based compensation less a maintenance-capex guess — does not work for a bank, for
> three reasons visible in Coastal's own statements. (i) Operating cash flow is not a return: it
> was **$254.6 million in 2025 against $47.0 million of net income**, because the provision and the
> matching credit-enhancement income are both non-cash and because **$6.69 billion of loans passed
> through loans-held-for-sale**. (ii) There is no maintenance capex that matters: property
> purchases were **$8.4 million against $4.74 billion of assets**, and a loan book does not wear
> out. (iii) Deposit and loan flows are financing and investing, so the cash statement of a growing
> bank measures growth, not earnings.*
>
> ***So the metric set is selected by business type first, exactly as [E5-37] requires and exactly
> as `Framework/SECTOR METHOD …` does for an insurer — and the metric is the one the corpus itself
> names for this job, [E2-01]'s "high earnings rate on equity capital employed". Three measures,
> all from filed statements:***
> 1. ***return on average common equity***, reported by the filer and independently recomputed from
>    beginning and ending equity;
> 2. ***pre-tax return on average common equity***, because tax rates move and the 2026 loss year
>    carries a tax benefit;
> 3. ***the (c) EQUIVALENT — and this is the part that is ours.** For a bank, the expenditure that
>    the business "requires to fully maintain its long-term competitive position and its unit
>    volume" **[E2-23]** is not plant. It is **the equity that must be retained to hold the
>    regulatory capital ratio constant while the balance sheet grows**: a bank that grows assets
>    and does not retain the matching capital must either stop growing or sell shares. So
>    **(c) = Δassets × the Tier 1 leverage ratio**, and **"owner earnings" for a bank = net income
>    − (c)**. Rationale for the CONVENTION in one line: it is the only construction that makes
>    [E2-23]'s "requires to fully maintain … unit volume" mean anything for a balance-sheet
>    business, and it is the same idea as **[E2-60]**'s restricted earnings, whose third dimension
>    is explicitly **"its financial strength"**.*
>
> *Denominator scope, per **[E2-43]**: goodwill and intangibles are shown separately, never hidden
> in book equity. Coastal carries **zero goodwill** and **$4.5 million of intangibles** (from the
> GreenFi asset acquisition in Q4 2025) against $491.0 million of equity, so tangible and book
> equity are the same number to one decimal and no wedge needs reporting. Share-based compensation
> is already an expense in the reported figures and is **not** added back **[E5-06]**; it is
> tracked separately because it grew from $1.28M (2021) to **$8.60M (2025)**, 18.3% of net income.*

| year | net income | avg common equity | **ROE, recomputed** | ROE, as filed | **pre-tax / avg equity** | cash tax % of pre-tax |
|---|---|---|---|---|---|---|
| 2021 | $27.00M | $170.7M | 15.82% | 17.24% | 20.14% | 25.5% |
| 2022 | $40.62M | $222.4M | 18.27% | 18.24% | 22.77% | 46.4% |
| 2023 | $44.58M | $269.2M | 16.56% | 16.41% | 21.22% | 12.0% |
| 2024 | $45.22M | $366.8M | 12.33% | 14.11% | 15.63% | 18.4% |
| 2025 | $46.99M | $464.8M | 10.11% | 10.17% | 13.17% | 12.5% |
| H1 2026 | −$30.09M | $477.2M | **−12.61% annualised** | −12.04% | — | — |

*The recomputation matches the filer's figure within 0.15 points in four of five years. The one
gap, 2024 (12.33% mine vs 14.11% filed), is fully explained and is not a discrepancy: the $98.0
million equity raise landed in **December** 2024, so a simple beginning-and-ending average
overweights it while the filer's daily average does not. The filer's figure is the better one and
is the one used.*

**What the series says, and it is unambiguous: the primary test is failing in a straight line.**
ROE **17.24% → 18.24% → 16.41% → 14.11% → 10.17% → negative.** Pre-tax return on equity **22.77%
→ 13.17%.** Meanwhile **pre-tax income was essentially flat for three years — $57.1M, $57.3M,
$61.2M — while average equity rose 73%, from $269M to $465M.** The denominator grew and the
numerator did not. **[E2-01]** is defined *in opposition to* EPS growth for exactly this reason,
and here even EPS is not growing: diluted shares rose from 13,640,182 (2023) to 15,350,175 (2025),
so 2025 EPS was roughly $3.06 against $3.27 in 2023.

**The (c) equivalent, and it is the harshest number in the file:**

| year | Δ assets | capital required at 10.62% Tier 1 leverage | net income | **net income − (c)** |
|---|---|---|---|---|
| 2021 | $869.4M | $92.3M | $27.0M | **−$65.3M** |
| 2022 | $509.0M | $54.1M | $40.6M | **−$13.4M** |
| 2023 | $608.9M | $64.7M | $44.6M | **−$20.1M** |
| 2024 | $367.8M | $39.1M | $45.2M | **+$6.2M** |
| 2025 | $620.2M | $65.9M | $47.0M | **−$18.9M** |
| H1 2026 | $714.7M | $65.1M at 9.11% | −$30.1M | **−$95.2M** |

**Five-year total: $316.0M of capital required against $204.4M earned — a $111.6M shortfall.** And
the balance sheet confirms it independently: **equity rose $350.7M from 2020 to 2025 while
cumulative net income was $204.4M, so $146.3M of the equity increase came from issuing shares, not
from earning money.** On this construction the **five-year mean "owner earnings" is −$22.3M** and
the three-year mean is **−$10.9M**. This is **[E2-60]** in its exact terms: earnings whose payout
would cost the business *"its financial strength"* are restricted earnings, and a company that
distributes them *"is destined for oblivion."* Coastal does not distribute them — it pays no
dividend and buys back nothing, which is the **right** answer to that problem — but the corollary
is that **the shareholder's return from this business is not cash; it is book value that must be
topped up by new shareholders whenever growth outruns earnings.**

**The half-owner test [E2-26]** — *does this reporting tell me what I would want to know if the
positions were reversed?* **Largely yes, and unusually so, with one gap.**
- The things I most wanted are disclosed and quantified separately at every line: the percentage of
  CCBX charge-offs covered by the enhancement, the uncovered residue in dollars, the
  enhancement-asset rollforward, the partner-by-category maximum portfolio limits, the
  material weaknesses in plain COSO language, the restatement tables, the incentive plan's misses.
- **[E2-67]**, the positive pole — Berkshire published a table of its own reserving errors *"so you
  can … judge whether we may have some systemic bias"*. **Coastal publishes the nearest bank
  equivalent**: a three-year charge-off table split by segment, the coverage percentage series, and
  the enhancement rollforward including *"Net change in pending partner settlements."* It does
  **not** publish a reserve-development table in the insurance sense — a bank is not required to —
  so the benchmark is met in substance and not in form.
- **The gap, stated precisely rather than as an accusation.** The **cash reserve accounts** pledged
  by partners are the only collateral standing behind the credit enhancement asset, and they are
  disclosed **only annually**: **$69.3 million at 2024-12-31** and **$72.2 million at 2025-12-31**,
  against enhancement assets of $181.9M and $177.7M. **No quarterly filing discloses the balance**,
  including the Q2 2026 10-Q in which $46.0 million of the asset was written down — so at the one
  date when a reader most needed it, the number did not exist in the record. **I checked whether
  this was a new withholding and it is not:** the Q1 2026 and Q3 2025 10-Qs do not carry it either.
  It is a standing disclosure practice, and the honest finding is a **disclosure limit, not an act
  of concealment.** On the annual figures the **uncollateralised portion of the enhancement asset
  was $105.5M at 2025-12-31 and about $82.1M at 2026-06-30** using the last disclosed reserve
  balance.

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [x] **resists any change in current direction.** After the FY2024 material weaknesses and the
  restatement, and after the Q2 2026 charge, the stated course is unchanged: *"We believe this is
  an isolated issue pertaining to one partner and does not reflect a change in our view of our
  broader partner portfolio or BaaS model"*, and in the same release *"new partnership
  opportunities and product launches expected for the remainder of 2026"*, with three signed letters
  of intent. CCBX loans grew **23.1% in the six months to 2026-06-30**, to $2.23 billion, in the
  half-year that contained the loss.
- [x] **projects or acquisitions materialise to soak up available funds.** Assets grew **$714.7
  million in six months**, 15.1%, funded by CCBX deposits, in a half-year that produced a net loss
  — and **the capital ratio fell from 12.43% to 10.86% CET1**, one point of it from the charge and
  the rest from growth. This is the imperative's second behaviour in its purest balance-sheet form.
- [ ] staff studies produced to justify the leader's craving — not observable from filings.
- [ ] **peer behaviour mindlessly imitated [E3-02] — DOES NOT FIRE, and it is the company's best
  mark.** The peers that were lax were caught: Green Dot ($44M penalty), Customers Bancorp
  (Written Agreement + consent order), Metropolitan (two consent orders, then exit). Coastal has
  none in six years, and it publishes partner-by-partner **maximum portfolio limits** that it
  actually enforces — capital call lines *"limited to a maximum of $350.0 million by agreement with
  the partner"* while commitments stood at $519.1 million, and $6.64bn–$7.84bn of loans sold back
  to partners *"as part of our strategy to optimize our CCBX portfolio, manage growth, credit
  quality, portfolio and partner limits."* **Tested and found in Coastal's favour.**

**THE INCENTIVE READ [E4-27] — *"Never, ever, think about something else when you should be
thinking about the power of incentives."*** The 2025 plan's weights, from the proxy: **Return on
Average Assets 40%, core deposit growth 12.5%, gross loan growth 12.5%, net charge-offs 10%, board
discretionary 25%.** Two things follow and both matter.
1. **65% of the measured weight is growth and asset-based return.** Balance-sheet growth is the
   paid-for outcome in a business whose danger is balance-sheet growth.
2. **The credit metric excludes the entire credit exposure, and the proxy says so in a footnote:**
   *"Net charge-off goals are based on community bank data only as CCBX charge-offs are reimbursed
   by our CCBX partners, except for 5% of one CCBX partner portfolio."* The 2025 net-charge-off
   goal was scored at **100% of target** in a year of **$196.8 million of consolidated net
   charge-offs**, because the measured book charged off **$27 thousand**. The incentive plan cannot
   see the risk that produced the 2026 loss. **Board discretionary, 25% of the target, paid at
   100%** ("Strategic Objectives 100.0%").

**Capital allocation — the two buyback conditions [E5-08], plus the third [E4-31].**
- (1) **ample funds for operations and liquidity? YES** — $1.008 billion of cash and cash
  equivalents and $1.12 billion of contingent borrowing capacity at 2026-06-30, zero drawn.
- (2) **repurchases at a material discount to conservatively calculated IV?** **Not applicable, and
  correctly so.** No share was repurchased in 2025 and none is disclosed since; no dividend has
  ever been paid. **[E2-51]** warns that a manager who *consistently* turns his back on repurchases
  when they are clearly in owners' interests *"reveals more than he knows of his motivations"* —
  but that is not this case. A bank whose growth already consumes more capital than it earns
  (the (c) table above) fails condition (1) the moment it buys stock, and **[E5-25]** puts
  *"financial strength that is unquestionable"* ahead of everything. **No capital-allocation flag
  on the buyback question.**
- **The one allocation act to judge is the December 2024 raise, and it was well done:** $98.0
  million at about $67 a share against $29.38 of book. **[E5-44]** run in reverse — paper sold for
  more than the value given up — is accretive, and the residual S-3 capacity (about $4.0 million of
  the $102.0 million) is trivial. **Against that, [E3-58]'s prompt is live rather than fired:** the
  largest shareholder (11.34%) and a director is **Steven D. Hovde**, a bank mergers-and-
  acquisitions principal, with an Investment Agreement with the Company on the exhibit index since
  2011. There is no acquisition record to judge (the only one is the small GreenFi asset purchase,
  $4.5M of intangibles), so this is **recorded as a prompt, not a finding.** Note also that at the
  2026 annual meeting Mr Hovde's re-election passed with **6,374,067 for and 6,372,171 withheld** —
  **50.007%**. The register nearly removed him.

**THE GOVERNANCE FACT THAT WOULD MAKE ME ASK A QUESTION IN PERSON, and it is a sequence of dates.**
Recorded under **[E3-57]** (self-dealing and folly are *"either way, very costly to you"*) and
**[E2-30]** (institutional dynamics, not venality), and **not** as a **[E5-16]** conduct finding:
- **2026-05-12** — the CCBX President adopts a 10b5-1 plan for up to 15,000 shares.
- **quarter ended 2026-06-30** — the $22.8 million provision and the $46.0 million valuation
  adjustment are recognised.
- **2026-07-22** — the Chief Financial Officer, **Brandon Soto, hired 2025-10-01** at a $500,000
  annualised salary with 18,000 RSUs and 15,000 PSUs granted when the stock was **$110.59**,
  resigns effective 2026-08-15 **"to pursue a position as the Chief Executive Officer of a banking
  subsidiary of a privately held company in the financial technology sector"** — i.e. to a
  competing sponsor bank — after **ten months**. *"Mr. Soto's departure is not related to any
  disagreements with the Company."* He repays his $15,000 signing bonus.
  The **interim** CFO is **Joel Edwards, 65**, the predecessor who had retired in 2025.
- **2026-07-29** — **one day before** the loss is announced, the board appoints **Christopher D.
  Adams**, 46, chairman and a non-employee director since 2016, as **Executive Chair**, on a
  **five-year employment agreement with automatic annual renewal at a $750,000 base salary**. Mr
  Adams *"has been a partner at the law firm Adams & Duncan, Inc., P.S. … since 2006"* — the same
  firm to which the Company paid **$1.3 million for legal services in FY2025**, disclosed in the
  proxy's related-party section. The Company already has a chief executive (Mr Sprink, $874,000).
- **2026-07-30** — the $42.1 million quarterly loss is reported.
**Add the 2025 departures** — Curt Queyrouze (severance, resigned 2025-09-12) and Andrew Stines
(resigned 2025-10-01, $789,925 of accelerated vesting) — and the count is **five executive
changes in twenty-four months**, in a business the framework has just classed as
have-to-be-smart-every-day. **None of this is a disqualifier. All of it is the wrong direction on
the one variable [E3-29] says decides a bank.**

**And insider alignment is thin.** CEO Eric Sprink, in the job since 2010, beneficially owns
**38,972 shares** — about **0.26%**, roughly one year's total compensation at the current price.
His 2025 total compensation was $1,693,201, which is modest and not a flag; the low ownership is
not a flag either, but it is the opposite of the **[E2-48]** superstar tell.

**THE GUARDRAIL — checked before writing the verdict.**
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** Q2 is OUT and Q3 cannot
  repair it **[E2-37, E2-38, E3-39]**. The clean supervisory record is the best fact in the file and
  it **does not** promote: *"a textile company that allocates capital brilliantly within its
  industry is a remarkable textile company — but not a remarkable business."*
- [x] The business **requires** daily competence, and that is recorded at **Q2 as a moat defect
  [E4-23]**, which it was.
- [x] Is a great manager the reason to act? **No, and the question does not arise** — the franchise
  is not intact **[E2-35, E2-36]**, so there is no *"localized excisable cancer"* to excise.

- **VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [x] UNRESEARCHED**

**Why UNRESEARCHED and not IN, stated honestly.** No conduct disqualifier was found, and on an
ordinary name that would be enough for IN. But **Q3 was declared a BINARY GATE for this business**,
and at gate weight the framework's own rule bites: **a gate marked IN carrying "unverified" or
"provisional" is UNRESEARCHED.** Two things at gate weight are not on the record and **both can be
named, which is what makes this UNRESEARCHED rather than UNKNOWABLE**:
1. **THE WORK ORDER — the identity and financial condition of the counterparties.** Coastal names
   **one** partner in its filings (Aspiration Financial, LLC, exhibit 10.17, a 2019 Program
   Agreement; the FY2025 10-K also records *"Acquired GreenFi assets during the quarter ended
   December 31, 2025"*, GreenFi being Aspiration's successor name). Two more are identifiable only
   from **their** filings (Dave Inc., Prosper Marketplace). Twenty-five of twenty-eight partners are
   unnamed, and **no per-partner exposure is published at all** — not the loan balance, not the
   enhancement receivable, not the cash reserve. *The artifact that would resolve it and where it
   lives:* the Program Agreements themselves, which the Bank files only when required
   (one is on the exhibit index), and the **FFIEC Call Report** schedules for Coastal Community
   Bank (RSSD, FFIEC CDR), which carry deposit and asset detail the 10-K does not. **Ladder rung:
   below SEC EDGAR — a US bank regulatory filing outside the framework's six-rung evidence ladder.
   Not blocked; not pulled in this run.**
2. **THE WORK ORDER — the supervisory record itself.** "No consent order disclosed" is an
   **absence claim**, and the framework's own absence-claim rule (added 2026-08-28) says an absence
   may be asserted only where a recorded sweep looked for it and only as *"no instance found."*
   The sweep here was a full-text search of six 10-Ks and the SEC submissions index. **It cannot
   see a non-public supervisory action**, and bank enforcement is published by the Federal Reserve
   and the Washington DFI, not by EDGAR. *The artifact:* the **Federal Reserve's enforcement-action
   database** and the **Washington State DFI** order list for Coastal Community Bank. **Ladder
   rung: outside the ladder. Not pulled.** So the record reads **"no instance found in SEC
   filings"** and no further.

---

## Q4 — WILL IT SURVIVE? *(RECORDED, NOT GOVERNING)*

### Owner earnings — and for a bank the construction is the CONVENTION declared at Q3

The ordinary construction is not applied, for the three reasons given above; the measure used is
**net income less the capital retention the balance sheet requires**, and the numbers are in the
Q3 table. Both windows are carried, with the spread, per **[E4-25]**:

- **Short window, three years 2023–25: mean −$10.9M.**
- **Long window, five years 2021–25: mean −$22.3M.**
- **Spread:** both windows are negative, so the conservative end is the five-year figure and the
  spread does not change the sign. **Capex band: not applicable** — property purchases were $8.4M
  against $4.74bn of assets and the (c) that matters is regulatory capital, not plant, so the
  **[E3-44]/[E2-41]** D&A default and the **[E5-20]** exception class are both silent here. This
  is stated rather than forced, per **[E5-37]**.
- **A distorted year sits in the window and it is named [E5-11]: 2021**, when assets grew $869.4M
  (49.5%) in the single year CCBX scaled, making the required retention $92.3M against $27.0M
  earned. Excluding 2021 the four-year mean is −$11.5M. **It is still negative.**
- Stock compensation is subtracted in full and is inside the reported figures **[E5-06]**: $8.60M
  in 2025, 18.3% of net income, up from $1.28M in 2021. Measured at grant value rather than the
  charge **[E3-70]** the subtraction would be larger; the filings do not separate grant fair value
  from the charge, and the amount is not decision-changing here.

### Great, good, or gruesome? **[E4-20]**

- [ ] great — [ ] good — [x] **gruesome**, and **[E4-43]** is applied so as not to over-read it.
  The *good* class passes: *"nothing shabby about earning $82 million pre-tax on $400 million of net
  tangible assets"*, and ~12% on retained capital is *"quite satisfactory"* **[E5-40]**. Coastal was
  in the good class in 2021–23 on the reported ROE. **It is not now.** The three-part gruesome test:
  *grows rapidly* — assets +$714.7M, 15.1%, in six months; *requires significant capital to
  engender the growth* — the (c) table, $316.0M required against $204.4M earned over five years,
  and $146.3M of equity bought from new shareholders; *and then earns little or no money* — ROE
  10.17% in 2025 and negative in the first half of 2026, with pre-tax income flat for three years
  on 73% more equity. **[E4-20]**'s own warning applies: investors *"attracted by growth when they
  should have been repelled by it."* What would rescue it from gruesome is the clause **[E4-43]**
  supplies — *"unless the cash they consume gets to earn a reasonable return"* — and the return on
  the consumed capital has fallen every year for four years.

### Staying power — score all three **[E5-11]**

- **(1) a large and reliable stream of earnings — LARGE, NOT RELIABLE.** Net interest income is
  genuinely large and growing ($310.1M in 2025, $172.7M in the first half of 2026, a record).
  But **81.0% of 2025 noninterest income — $187.7M of $231.6M — was BaaS credit enhancement
  income, which is not a customer paying for a service; it is the recognition of a receivable from
  a counterparty**, and $46.0M of that receivable class has now been written down. Strip the
  enhancement machinery and 2025 pre-tax income of $61.2M becomes a loss.
- **(2) massive liquid assets — YES, and this is the strongest part of the file.** At 2026-06-30:
  **$1,008.4M of cash and cash equivalents** (18.5% of assets), $45.2M of securities, **zero
  FHLB advances and zero Federal Reserve discount-window borrowings** at every year-end shown, and
  **$1.12bn of additional contingent borrowing capacity**. Total borrowings are **$48.1M** — $45.0M
  of subordinated notes and $3.6M of junior subordinated debentures — against $463.4M of equity.
  **[E5-39]**: *"We will never be dependent on the kindness of strangers."* On the borrowing side,
  Coastal is not.
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — and this is where the answer changes, because
  the deposits ARE the near-term requirement.** *"Ignoring that last necessity is what usually
  leads companies to experience unexpected problems."* **$3.29 billion of the $4.86 billion of
  deposits belong to the CCBX segment** and are, in the filer's words, *"generally classified as
  interest bearing demand and money market accounts"* — legally withdrawable on demand and
  contractually tied to twenty-eight terminable programme agreements. The filer states the
  mechanism itself: *"If a relationship with a large CCBX partner terminates, the exit of those
  deposits could have an adverse impact on liquidity."* And the measure moved hard in six months:
  **estimated uninsured deposits went from $641.3M, 15.5% of deposits, to $1.35 billion, 27.7%** —
  the filer attributing it to *"the timing of new partner deposits participating in sweep and
  reciprocal deposit networks"* and warning they are *"expected to remain above historical
  levels."* A further **$4.26 billion was swept off balance sheet** at 2026-06-30 (against $843.6M
  at 2025-12-31), which is prudent for the depositor and means the on-balance-sheet figure
  understates how much partner money is in motion. **[E3-52]** is the right lens and it cuts
  against Coastal: float and deferred taxes are good liabilities because they are *"without
  covenants or due dates"*; demand deposits controlled by a third party have no covenant but they
  have the shortest due date there is. **Score: 2 of 3, and the one that fails is the one the
  corpus calls the killer.**
- **Leverage, named and quantified** — **9.66 : 1** at 2025-12-31 and **11.77 : 1** at 2026-06-30
  (assets ÷ common equity). Regulatory: CET1 **12.43% → 10.86%**, Tier 1 leverage **10.62% →
  9.11%**, total capital **14.95% → 13.30%**; Bank *"well capitalized"* at both dates. **[E2-54]**'s
  coverage test passes comfortably: interest on borrowed funds was $1.8M in the first half of 2026
  against $172.7M of net interest income. **No ratio ceiling is applied** and none is implied; the
  judgment is the one **[E3-29]** asks for and it is written above.
- **Jurisdiction [E3-66]:** US filer, Washington State charter, Federal Reserve member bank.
  Shareholders stand where US law puts them, which the corpus calls *"especially favorable to
  shareholder interests."* No adjustment.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]** — and model exposure, not experience **[E4-40]**

**[E4-40]** is the governing instruction for this section and it is exactly on point here: *"all of
us in the industry made a fundamental underwriting mistake by focusing on experience, rather than
exposure."* Coastal's **experience** is that 97.4%–100.0% of CCBX charge-offs have been reimbursed
every year since 2021. Its **exposure** is a $154.3 million receivable from twenty-eight venture-
funded financial-technology firms, collateralised by $72.2 million of their cash. A benign loss
history in a business that just produced a $46 million write-down is *"not only useless, but
actually dangerous"* as a guide.

**A. The corpus's literal test, run on the loans the bank actually owns the risk of.** Community
bank loans were **$1,982.5M** at 2026-06-30. Following **[E3-24]** *"Consider some mathematics"*
exactly:
- **10% of those loans producing losses averaging 30% of principal = $59.5 million**, against a
  year's pre-tax income of $61.2 million. **The company would roughly break even.** That is
  precisely the 1990 Wells Fargo result, on the same parameters, and Buffett's conclusion applies:
  *"A year like that — which we consider only a low-level possibility, not a likelihood — would not
  distress us."*
- Pushed harder: **15% at 40% severity = $119.0M**, $57.7M out of equity (12% of it); **20% at 50%
  = $198.3M**, $137.0M out of equity (30%). Non-owner-occupied CRE plus construction is **170.9% of
  the Bank's total risk-based capital**, against the 300% interagency attention threshold.
  **The community bank passes the corpus's own bank stress test at the corpus's own parameters.**
  **This bank does not die of loans.**

**B. The way it actually dies: the counterparty.** The mechanism, in one sentence: **Coastal holds
the loans and the losses on its own balance sheet and has sold the losses to counterparties
smaller and less capitalised than itself, so its reported credit quality is a receivable from the
borrowers' own promoters — and the promoters are venture-funded consumer-lending firms whose own
solvency is correlated with the very credit cycle that would cause the losses.** The loss is
recognised as *income* on the way in (BaaS credit enhancement income) and as *expense* on the way
out (a valuation adjustment). Quantified from filed figures:
- **If the enhancement were worth nothing for one year at FY2025 volumes:** consolidated pre-tax
  income of $61.2M becomes **−$126.4M**. Equity of $463.4M falls to **$368.6M** after tax at 25%,
  and equity/assets from 8.49% to **6.76%**. **A second such year takes it to $273.8M and 5.02%** —
  through the 5% Tier 1 leverage line (equity/assets is used as the proxy; at 2026-06-30 it was
  8.49% against a reported Tier 1 leverage ratio of 9.11%, which is struck on *average* assets, so
  the proxy is the more conservative of the two) that defines *well capitalised*, at which point the Bank
  cannot grow assets, make acquisitions or open branches without regulatory approval, and the
  holding company's obligation to fund a capital restoration plan is triggered.
- **The graded version, calibrated on the partner that has already failed.** One non-public partner
  cost **$68.8 million pre-tax**, which is **14.8% of 2026-06-30 equity**, in one quarter. Two such
  partners: 29.7%. Three: 44.5%. Five of twenty-eight: 74.2%.
- **Likelihood: [x] A REAL POSSIBILITY** — not *likely*, and explicitly not *a low-level
  possibility*, because **the single-partner case is not a model, it is the filed record of the
  most recent quarter.** What keeps it from *likely* is that partner failures are idiosyncratic,
  that 98.0% coverage still held in the June quarter, that the $4.26 billion of swept deposits and
  $6.64–7.84 billion of loan sales genuinely reduce the balance-sheet exposure, and that Coastal
  has the contractual right to *"declare the agreement in default, take over servicing and cease
  paying the partner"* and then *"retain the full yield and any fee income on the loan portfolio
  going forward"* — which converts a counterparty failure into a direct-lending business at a
  15.87% gross yield against an 11.4% charge-off rate. **That is the bear case's strongest
  rebuttal and it belongs here [E4-51]:** the loss is bounded by the enhancement asset plus the
  incremental losses on the affected portfolio, not by the whole $2.23 billion.
- **[E4-51] test — can I state the argument against my own conclusion better than its holders?**
  The bull case, fairly stated: *Coastal is the last well-run BaaS sponsor bank standing. Three of
  its five filing competitors have been disciplined by their regulators and one has left the
  business; Coastal has none disclosed in any of its six annual reports. Its community bank is genuinely
  excellent — $27 thousand of charge-offs on $1.94 billion and the cheapest deposits in its
  Washington peer group. Its balance sheet is unlevered by bank standards, holds $1.0 billion of
  cash and owes $48 million. The Q2 2026 charge was taken early, in full, on one partner, and
  disclosed in a headline; the material weaknesses were disclosed, remediated and audited. At
  1.52× book and roughly 8.7% of the market value in pre-tax income, a reader is being paid a
  fair price for a scarce charter with a clean licence, and the partners cannot easily replace a
  sponsor bank that regulators leave alone.* **I do not think that case is wrong about the
  community bank or about the balance sheet. I think it is wrong about the word "scarce": the
  filings of Coastal's own two identifiable partners name Evolve and WebBank as their other
  sponsor banks, and Coastal's own 10-K concedes a partner may leave for "better terms from
  another provider."**

**THE SURVIVAL SHAPE.** Checked against all twenty-four in `Screens/SURVIVAL SHAPES - index.md` as they stood when this file was written; the CB and BLK folds of the same day took 23 and 24, so this one is 25.
Closest existing: **#11 THE PASS-THROUGH**, which is present as a **feature** — the gains are being
passed to the partner (BaaS loan expense from 40.4% to 47.0% of CCBX interest income; Prosper's
program fee cut 0.75%) — and **#6 THE BORROWED BALANCE SHEET**, inverted, because Coastal *lends*
its balance sheet rather than borrowing one. Neither is the mechanism.

**PROPOSED, #25 — THE INDEMNITY** *(pending the operator)*: **the balance sheet holds the assets and
the legal losses, and the losses have been contracted away to counterparties smaller and
less-capitalised than the lender, so the reported credit quality is a receivable from the
borrowers' own promoters; the promise is booked as income on the way in and reversed as expense on
the way out, and it fails when one promoter cannot pay — at which point the lender owns a loan book
it did not underwrite, at a loss rate it never priced.** It is distinct from #11 (the gains are
passed to the partner *and* the loss is only apparently passed), from #6 (the direction of the
lending is reversed), from #13 THE TENANT (Coastal is the landlord; its rent is being negotiated
down) and from #7 THE LONG TAIL (the tail here is measured in months, and the buffer is a
counterparty's cash reserve, not the balance sheet).

- **VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [x] UNRESEARCHED**
  *The gruesome finding and the failure of strength (3) point to OUT; what stops the run from
  writing OUT here is the same missing artifact as at Q3 — **the per-partner exposure**. Without
  it the depth of the counterparty exposure cannot be sized, only bounded, and a gate that rests
  on an unpulled document is a work order, not an answer. The file is closed at Q2 regardless.*

---
⛔ **Q5 DID NOT OPEN. Q1 was IN; Q2 was OUT.** What follows is the below-gate arithmetic the
operator's brief required, under operator rule 3.

## COMPUTATION — NOT A CLEARANCE

*This section carries **no entry language**, no verdict, no ranking position and no margin of
safety. It exists to state, in words, what the price is and what a buyer at that price is paying
for.*

- **Price US$45.97, close of 2026-09-18** (aggregator, flagged). **Cross-checked against primary
  documents:** Brian Hamilton's Forms 4 report Coastal shares valued at **$41.80 on 2026-08-03**
  and **$46.85 on 2026-09-01** (accessions `0002005790-26-000024` and `0002005790-26-000026`), so
  the quote is corroborated by SEC-filed transaction prices two weeks either side.
- **Shares 15,286,327** (Q2 2026 10-Q cover, 2026-08-03, accession `0001437958-26-000061`).
- **Market capitalisation US$702.7 million.**
- **Book value per share at 2026-06-30: $463.447M ÷ 15,286,327 = $30.32. Price/book 1.52×.**
  Tangible book is the same to a cent ($4.5M of intangibles, no goodwill).
- **Sovereign 5.34%**, US Treasury 30-year par yield, 2026-09-18, issuing authority.

| measure, all from filed statements | amount | % of the $702.7M market cap |
|---|---|---|
| FY2025 net income | $46.99M | **6.69%** |
| FY2025 pre-tax income | $61.24M | **8.71%** |
| five-year mean net income, 2021–25 | $40.88M | 5.82% |
| five-year mean pre-tax income, 2021–25 | $52.14M | 7.42% |
| **five-year mean, retention-adjusted (the CONVENTION)** | **−$22.31M** | **−3.18%** |
| three-year mean, retention-adjusted | −$10.94M | −1.56% |
| trailing twelve months net income (H2 2025 + H1 2026) | −$3.85M | −0.55% |

- **Against the ~10% floor [E4-28]** — *"that's the figure we quit on"*, and it does not move with
  the sovereign: the honest pre-tax expectancy at this price is **8.71% on the best single year
  the company has ever had** and **7.42% on the five-year mean**. **Both are below the floor, so
  the name is not ranked.** On the construction this run actually believes is the right one for a
  bank, it is negative. For the five-year retention-adjusted mean to reach a 10% pre-tax yield at
  this price, the figure would have to move from **−$22.3M to +$70.3M**, which is not a growth
  rate — it is a different company.
- **Above the bond, below the floor** — the same configuration CLAUDE.md records for Berkshire:
  FY2025 pre-tax at 8.71% is 337 basis points over the 5.34% sovereign, and still below the ~10%
  quit-on figure. **No risk premium is added to the rate [E3-42]**; certainty is not priced here at
  all, because the file closed at Q2 and no value range is being asserted.
- **No value range is stated**, no bar is chosen, no margin is applied, and no windage is spent:
  **[E4-25]**'s three outcomes require a Q1–Q4 pass to be meaningful, and Q2 is OUT.
- **What the buyer at $45.97 is paying for, in words, which is the part of this section that
  matters.** The buyer is paying **1.52× book** for: a genuinely good $2.0 billion community bank
  in one Washington county, which earns about 6.5% on its loans, pays about 1.6% for its deposits,
  charged off $27 thousand last year and produced $39.1 million of segment pre-tax income in 2025;
  **plus** a $3.3 billion banking-as-a-service business whose reported profit is the net of a
  $193 million provision and a $188 million receivable from twenty-eight private financial-
  technology firms, of which $46 million has just been written down; **plus** a supervisory record with no order disclosed in six annual reports, in an industry where three of five filing competitors have been
  disciplined; **less** the fact that the company's growth has consumed $112 million more capital
  than it has earned in five years, and has been funded by selling shares. **In one sentence: at
  this price the buyer is paying a premium to book for a good small bank attached to a fee business
  whose fee is the assumption of a credit risk it then insures with the people who created it.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Nothing is held, so [E2-28]'s sell rule has nothing to act on and [E1-02]'s "yardsticks prior to
the act" is recorded as the reversal condition for the Q2 OUT instead.**

- **Thesis-confirming metric (would confirm the OUT):** net BaaS loan income ÷ average CCBX loans
  continuing to fall below 8.41%; the percentage of CCBX charge-offs covered by the credit
  enhancement falling below 97%; a second partner-specific valuation adjustment.
- **Thesis-breaking metric and its threshold (would force the OUT to be revisited):** net BaaS loan
  income ÷ average CCBX loans **rising for three consecutive years** *while* the largest
  identifiable partners **cease to dual-source** — Dave dropping Evolve, or Prosper moving its
  personal-loan origination from WebBank to Coastal. Both are observable in **the partners' own
  10-Ks**, which is where this run found the disconfirming evidence in the first place.
- **Next catalyst date:** the Q3 2026 10-Q, expected early November 2026 on the filing pattern
  (2025-11-07 for the prior year) — the first statement to show whether the $46.0 million
  adjustment was the whole of that partner's exposure, and the annual 10-K in late February 2027,
  which is the only filing that discloses the **cash reserve account balance**.
- **[E4-17]/[E3-30] monitoring question — aberrational cycle or permanent slippage?** The Q2 2026
  charge, read alone, is an aberration. Read with the FY2024 material weaknesses in the same
  failure class and with the three-year fall in the price Coastal keeps, it is **slippage**, and the
  operative sentence is the filer's own: a partner may leave for *"better terms from another
  provider."*
- **Position size: ZERO.** Not a judgment about sizing; the business failed Q2.
- **No band is armed in `tools/alerts.json` and no `PORTFOLIO.md` row is added.** The QLYS ruling of
  2026-09-07 governs: a name that failed on the **business** gets a reversal condition in words, not
  a price alert. The words are above.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** *(carrying Q2's verdict; nothing
  is owned and nothing is armed)*

---
## WHAT THE FRAMEWORK NEEDS IN ORDER TO RUN A BANK — written because this is the first one

Four gaps, each with the evidence that exposes it. **None is fixed here; PRIME RULE 5 requires a
written case and the operator's approval for a structural change, and PRIME RULE 6 requires the
ledger row before the rule.**

1. **Q2 HAS NO PASSABLE FORM FOR A BANK, AND THE CORPUS SAYS SO ITSELF.** **[E3-43]** classes a
   bank as *"a business, unlike a franchise"* — that is *why* **[E3-29]** raises Q3 to gate weight
   — and **[E3-03]** criterion 2 requires *"no close substitute"*, which no deposit-taking
   institution in a metropolitan market has ever had. Read literally, **every bank the project
   ever runs stops at Q2**, and the corpus bought banks (Wells Fargo 1990, at *"less than five
   times after-tax earnings"* **[E3-24]**). **This run did not use that reasoning** — it closed Q2
   on Coastal's own and its counterparties' filed facts, which would close it at any company — but
   **the next bank (ACNB, SOFI, JPM, TFC) will hit the general question immediately and it should
   not have to decide it alone.** The two candidate resolutions: (a) Q2 for a bank is a
   *local-deposit-franchise* test (cost of deposits and share against named peers, which this run
   built and which Coastal's community bank half passes); or (b) **[E3-29]** is read as the corpus
   creating an explicit exception class in which Q2 returns NARROW and the decision moves wholly to
   Q3 and Q5. **(b) has the better textual support and the worse discipline.** The operator's call.
2. **THE EVIDENCE LADDER STOPS TOO SOON FOR A REGULATED FILER.** Two of the three things this run
   most needed do not live on EDGAR: the **FFIEC Call Report** (per-bank deposit and asset detail,
   and the only public data on the private sponsor banks that are Coastal's real competitors —
   Cross River, WebBank, Evolve, Column, Lead, Sutton, Celtic, Thread) and the **Federal Reserve
   and state banking department enforcement registers** (the only place a supervisory action
   becomes public). The current ladder is *SEC XBRL → SEC EDGAR → company IR → exchange filings →
   EDINET → competitor filings*. **For a bank, a rung is missing**, and its absence turned the
   single most important competitor comparison in the industry into a stated limit and the
   supervisory record into an absence claim.
3. **OWNER EARNINGS NEEDS A DECLARED FORM FOR BALANCE-SHEET BUSINESSES, AS FLOAT GOT ONE.**
   `Framework/SECTOR METHOD - owner earnings for insurers …` exists because the operator's queue
   held nine insurers. It holds five banks. This run wrote its own CONVENTION —
   **(c) = Δassets × the regulatory leverage ratio**, i.e. the equity a bank must retain to hold its
   capital ratio while it grows — and it is the sharpest number in the file ($316.0M required
   against $204.4M earned over five years). **It is ours, it is confessed as ours, and it should
   either be adopted with a ledger row or refused.** Its strongest corpus anchor is **[E2-60]**'s
   third dimension of maintenance, *"its financial strength."*
4. **THE OPERATOR RULING SHOULD SAY WHETHER "COMPUTATION — NOT A CLEARANCE" MAY CARRY A PRICE
   VERDICT.** This run wrote the below-gate arithmetic and found that the name **also fails the
   ~10% floor** (8.71% on the best year, 7.42% on the five-year mean). That is a second,
   independent, sufficient reason not to buy, and it is useful to have on the register. But
   operator rule 3 forbids entry language, and the FAIL/PASS line in `## COMPLETED FROM THE QUEUE`
   names the question that closed the file. **This run records the floor result as a note beside
   the Q2 FAIL, not as the fail line**, and flags the convention for confirmation.

*A fifth, smaller one, and it is a tooling matter: `tools/run.py` and the screening layer build
owner earnings from operating cash flow, which for a bank is a number about growth rather than
earnings — Coastal's 2025 operating cash flow was **$254.6 million against $47.0 million of net
income**, 5.4×, because $6.69 billion of loans ran through held-for-sale. **Any screen that priced
a bank on operating-cash-flow-based owner earnings priced it at roughly five times its earnings.**
The 2026-09-01 triage dropped financials as a class, which accidentally avoided this; if financials
are ever screened, the construction must change first.*

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, **Q2 OUT — the file closed there**;
      Q3 and Q4 written and explicitly marked **RECORDED, NOT GOVERNING** at the operator's
      instruction; Q5 did not open and appears only as `COMPUTATION — NOT A CLEARANCE`.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Only Q1 is IN and
      it rests on read filings. Q3 was *not* marked IN precisely because two gate-weight items rest
      on unpulled documents.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: Q3 names the **Program
      Agreements** (SEC exhibit index, one filed) and the **FFIEC Call Report**, plus the **Federal
      Reserve and Washington DFI enforcement registers**, and states that the ladder rung is
      missing. Q4 names the **per-partner exposure**.
- [x] Every UNKNOWABLE verdict states what cannot be known — none was written.
- [x] Step 0: the filing was read, with accession numbers (FY2025 10-K `0001437958-26-000013`, Q2
      2026 10-Q `0001437958-26-000061`, five earlier 10-Ks, the 2026 proxy, four 8-K EX-99.1
      earnings releases, five other 8-Ks, and three counterparty 10-Ks). **Two figures
      cross-checked:** equity recomputed from A − L ($4,741,437 − $4,250,478 = $490,959, matching
      the filed line) and net income reconciled to the sum of the Note 21 segment columns.
- [x] Owner earnings: **the ordinary construction was refused with reasons and a CONVENTION was
      declared and labelled (PRIME RULE 3)**; two windows are reported with the spread; the capex
      band is stated as **not applicable** and why, rather than forced.
- [x] Competitor row filled — **eleven filed peers**, same metric, same window, accession per row,
      with the basis difference disclosed per row and the **private sponsor banks named as an
      explicit limit**. The moat is **NONE**, not PROVISIONAL: the deciding evidence came from the
      counterparties' own 10-Ks, not from the unavailable peers.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-18, struck fresh for this run.
- [x] No value range is stated at all — correct, because Q5 did not open.
- [x] No bar chosen and no margin applied; **windage count: zero**.
- [x] Prices dated; aggregator flagged **and corroborated against two SEC-filed Form 4
      transaction prices**.
- [x] `python tools/check_framework.py` PASSES.
- [x] Run committed to git with a pathspec, per the six-step fold.

## REGISTER
- Verdict: **[x] OUT (about the business)** — at **Q2**.
- One line: **CCB (Coastal Financial Corporation), 2026-09-19 — FAIL at Q2, OUT on the business:
  the banking-as-a-service business that is 48–53% of the loans and two-thirds of consolidated pre-tax
  income has no close substitute only in Coastal's telling; its two identifiable partners each
  name a competing sponsor bank in their own 10-Ks (Dave: Evolve; Prosper: WebBank), one of them
  amended its contract to cut Coastal's program fee by 0.75%, and the share of the CCBX yield
  Coastal keeps has fallen three years running (9.71% → 9.09% → 8.41%). Price US$45.97 (2026-09-18,
  aggregator, corroborated by Form 4 prices of $41.80 and $46.85), 15,286,327 shares from the Q2
  2026 10-Q cover of 2026-08-03 (accession `0001437958-26-000061`), cap US$702.7M, sovereign 5.34%
  (US Treasury 30-year, 2026-09-18). Below-gate note: it also fails the ~10% floor — 8.71% pre-tax
  on the best year it has ever had, 7.42% on the five-year mean, negative on the
  retention-adjusted construction.**
- **If UNRESEARCHED:** not the governing verdict. The two work orders inside Q3/Q4 are the
  **per-partner exposure** (Program Agreements; FFIEC Call Report) and the **supervisory record**
  (Federal Reserve and Washington DFI enforcement registers) — both on a **ladder rung the
  framework does not currently have**.
- **If UNKNOWABLE:** not applicable.
