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

