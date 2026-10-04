# Company Run — SoFi Technologies, Inc. (SOFI) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**THE SECOND BANK THIS PROJECT HAS RUN**, hours after the first. CIK **0001818874**, found by
`tools/sources.py:cik_for('SOFI')`, which returns `('0001818874', 'SoFi Technologies, Inc.')`.
WAVE 6, run under the operator ruling of 2026-09-19 that the five banks are run. It is a
**financial holding company** under section 4(l) of the BHCA, owning **SoFi Bank, National
Association** (acquired 2022-02-02 with Golden Pacific Bancorp), and it came public through a
**SPAC** — Social Capital Hedosophia Holdings Corp. V, closed 2021-05-28.

**THE METHOD IS THE CCB RUN'S, AND WHERE IT IS NOT, THE FILINGS ARE THE REASON.** The operator's
brief instructs this run to follow `Test Runs/2026-09-19 Run - CCB Coastal Financial.md` unless
SoFi's filings make its construction wrong, and to say which. The four corpus rules that governed
that file govern this one:

1. **Q3 is the deciding gate, not an overlay** — **[E3-29]**: *"Because leverage of 20:1
   magnifies the effects of managerial strengths and weaknesses, we have no interest in
   purchasing shares of a poorly-managed bank at a 'cheap' price. Instead, our only interest
   is in buying into well-managed banks at fair prices."* The one place cheapness is ruled out.
2. **The named failure mode is conformity** — **[E3-02]**.
3. **Reserves are where dishonesty hides** — **[E2-50]**, *"where 'earnings' can be created by
   the stroke of a pen, the dishonest will gather."* **This is where SoFi differs from Coastal
   and the difference is the whole file.** At Coastal the pen wrote an *indemnity receivable*.
   At SoFi there is essentially **no allowance at all** on 97.3% of the loan book, because
   $46.60 billion of $47.93 billion of loans are carried at **FAIR VALUE**, and the pen writes
   the **discount rate**. The allowance for credit losses is $56.5 million on $60.9 billion of
   assets. **[E2-50] therefore lands on the valuation note, not on a reserve table.**
4. **Survival is a quantified stress, not a ratio** — **[E3-24]**, run against this bank's own
   loan book at Q4. **No leverage ceiling** (`Framework/INVENTIONS - deleted and why.md`).

**WHERE THE CCB CONSTRUCTION IS FOLLOWED AND WHERE IT IS NOT — stated up front, per the brief:**
- **FOLLOWED:** the refusal of the ordinary owner-earnings construction, for the same three
  reasons, and **the same CONVENTION for (c): Δassets × the Tier 1 leverage ratio.** It is
  declared again at Q3 and it is, if anything, sharper here.
- **FOLLOWED:** **[E2-01]** as the primary measure, run as a multi-year series of return on
  equity capital, recomputed rather than taken from the filer.
- **FOLLOWED:** the **[E3-24]** stress at 10% of loans and 30% severity, plus harder variants.
- **NOT FOLLOWED — and the filings are the reason:** the CCB run's cash-flow finding **inverts**.
  Coastal's operating cash flow was **5.4× its net income** and therefore measured growth; SoFi's
  operating cash flow is **negative in every one of the seven years it has filed**, cumulatively
  **−$27.4 billion against cumulative net income of −$265.5 million**, because personal-loan
  originations are classified held-for-sale and run through *operating* activities. The direction
  reverses; the conclusion does not. **Operating cash flow for a lender measures the balance
  sheet, not the business** — CCB found it one way round, SoFi the other, and that is now two
  independent demonstrations.
- **ADDED, because Coastal had no equivalent:** a **fair-value** section. The mark is not a
  footnote here; it is $2.03 billion of carrying value above unpaid principal, and it is the
  single most important thing in the file, exactly as the brief predicted.

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
it is UNKNOWABLE. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** · source **US Treasury daily par yield curve, 30-year
  (issuing authority)**, struck fresh for this run by `tools/sources.py:sovereign('USD')`,
  which returned `(5.34, '09/18/2026', 'US Treasury daily par yield curve')`. FRED DGS30 is the
  fallback and was not used (CLAUDE.md, corrected 2026-09-02). *It is the same rate the CCB run
  struck hours earlier; it was struck again rather than inherited, per the RESUME STATE note
  that two runs had been handed a stale rate.*
- FX: **none needed.** SoFi earns in USD, is a Delaware corporation, files 10-Ks. It has
  foreign operations in Latin America, Canada, Switzerland and Hong Kong through the Technology
  Platform segment, and Argentina is accounted for as **highly inflationary**; those cost
  $7.1 million in 2025 and are recorded at Q3, not as an FX adjustment to the sovereign.
- **Price: US$16.96, close of 2026-09-18**, from `tools/sources.py:price('SOFI')` — **AGGREGATOR,
  flagged, live quote only** per operator rule 5. **Corroborated against primary documents:**
  seven Forms 4 filed 2026-09-16 for transactions of 2026-09-14 report SoFi shares valued at
  **$17.279 and $17.32** (accessions `0002032458-26-000026`, `0001864508-26-000008`,
  `0001351119-26-000019`, `0001613438-26-000022`, `0002012135-26-000023`,
  `0001934200-26-000009`, `0002034857-26-000014`), and Forms 4 of 2026-08-19 report **$18.002**.
  The quote is corroborated by SEC-filed transaction prices two days and one month earlier.
- **Share count: 1,291,570,324**, from the **cover of the Q2 2026 10-Q, accession
  `0001818874-26-000054`, cover date 2026-07-31** (verbatim: *"The number of shares of the
  registrant's common stock, par value $0.0001 per share, outstanding as of July 31, 2026 was
  1,291,570,324 shares."*).
  - **Issued-versus-outstanding check, run because the HBB/SOUN/BIRD notes of 2026-09-19 made
    the per-class cover a standing hypothesis:** the Q2 2026 filed balance sheet states
    **"1,290,312,404 and 1,270,568,878 shares issued and outstanding, as of June 30, 2026 and
    December 31, 2025"** — **issued equals outstanding**, there is no treasury stock line, and
    footnote (1) records **100,000,000 non-voting common shares authorised and NONE issued or
    outstanding** at either date. `dei:EntityCommonStockSharesOutstanding` is tagged once,
    undimensioned. The **Series 1 Redeemable Preferred Stock was redeemed in May 2024** for
    $323.4 million and none is outstanding. So the HBB per-class layer does not arise, but the
    **non-voting class exists and is authorised**, which is recorded as a live channel, not
    applied to the count.
  - **POST-COVER ISSUANCE CHECK — and this company does issue shares constantly, so it was run
    three ways.** (i) **No block issuance is on the record between the 2026-07-31 cover and
    2026-09-19:** the only filings by the registrant in that window are the 8-K of 2026-07-29
    (Item 2.02, the earnings release) and a 5.07 8-K of 2026-06-17; **no 424B, no S-3 takedown,
    no 8-K Item 3.02.** (ii) **Insider Forms 4 through 2026-09-16 were read individually**: ten
    were filed after 2026-08-01, and every transaction is code **M** (option/RSU settlement) or
    **F** (shares withheld for tax), except **one code-S sale — Kelli Keough, 11,286 shares at
    $18.0032 on 2026-08-24**. The gross of the code-M settlements filed on 2026-09-16 is
    roughly **0.6 million shares**, net of withholding, which is inside the rounding of a
    1.29 billion count. (iii) **Seven Form 144 notices** were filed (five on 2026-09-15, two on
    2026-08-18) — notices of *proposed* sale by affiliates, which do not change the count.
    **The count is used as filed.**
  - **THE LIVE DILUTION CHANNELS ARE NOT IN THE COUNT AND ARE NOT SMALL.** From Note 10 of the
    Q2 2026 10-Q: **total common stock reserved for future issuance 253,630,801 shares at
    2026-06-30**, which is **19.7% of shares outstanding** — 63,363,353 of outstanding
    options/RSUs/PSUs and **190,267,448 of "possible future issuance under stock plans"**, the
    latter growing by an **evergreen provision of up to 5% of shares outstanding every
    1 January through 2030**. Plus **$428.0 million of 2026 convertible notes maturing
    2026-10-15**, 26 days after this run, settleable in cash to par and shares above it — the
    filer states that at 2026-06-30 *"we did not anticipate any incremental spread, as our
    common stock price was below the conversion price"* — and $862.5 million of 2029
    convertible notes whose **fair value was $1.7 billion** at 2026-06-30 on Level 1 quotes.
    All of this is recorded at Q3 under **[E5-15]** and at Q6, not applied to the count.
  - `tools/sources.py:deal_filings('0001818874')` returns `([], [], '2026-02-17')` — **no live
    deal form**, so the quote is not a merger spread (the ROKU defect of 2026-09-12).
- **Market capitalisation: 1,291,570,324 × $16.96 = US$21,905.0 million.** The house rule
  `cap = close(anchor) × shares(measurement) × splits AFTER measurement` needs no split factor:
  `tools/sources.py:split_factor_after('SOFI','2021-05-28')` returns **1.0** — SoFi has never
  split since it began trading. `market_cap()` independently returns **$21,905,032,695**.

### DOES THIS CIK HOLD A PREDECESSOR'S FIGURES? **YES — AND IT IS WORSE THAN THE RGTI/USAR CASE**

`tools/sources.py:name_change_note('0001818874')` fires: *"NAME CHANGE inside the data window:
was 'Social Capital Hedosophia Holdings Corp. V' until 2021-05-28."* The check was then run to
the bottom, because the RGTI run of 2026-09-13 and the USAR run of 2026-09-19 both closed on
recast perimeters.

**What the filings say.** The FY2021 10-K, Note 2 (accession `0001818874-22-000031`), verbatim:
*"The Business Combination was accounted for as a **reverse recapitalization** whereby SCH was
determined to be the **accounting acquiree** and Social Finance to be the **accounting
acquirer**. This accounting treatment was the equivalent of Social Finance issuing stock for the
net assets of SCH, accompanied by a recapitalization whereby no goodwill or other intangible
assets were recorded. **Operations prior to the Business Combination are those of Social
Finance.**"* Prior-period share counts were *"retroactively converted by application of the
exchange ratio of 1.7428."*

**So the operating history under this CIK from FY2019 onward is Social Finance, Inc.'s own, and
it is a real eleven-year-old lender's record, not a shell's.** That is better than RGTI's and
USAR's position. **But the CIK carries BOTH companies' figures at the SAME period end**, and
this is the trap in its purest form yet found:

| tag, period end 2020-12-31 | value | accession | whose company |
|---|---|---|---|
| `us-gaap:Assets` | **$806,077,995** | `0001104659-21-037483` (FY2020 10-K) | **the SPAC's trust account** |
| `us-gaap:Assets` | **$8,563,499,000** | `0001818874-22-000031` (FY2021 10-K) | **Social Finance, recast** |
| `us-gaap:StockholdersEquity` | **$5,000,001** | `0001104659-21-037483` | the SPAC's founder shares |
| `us-gaap:StockholdersEquity` | **−$120,115,000** | `0001818874-22-000031` | Social Finance, recast |

`us-gaap:StockholdersEquity` is also tagged **$0 at 2020-07-09**, the SPAC's inception.
**A screen taking the earliest vintage at 2020-12-31 gets a $806 million blank-cheque
company; one taking the newest gets an $8.56 billion lender. Both are audited, both are
filed under this CIK, and they are different companies.** This run uses the FY2021 10-K
vintage throughout and says so. *(This is the same class of defect as the DELL/SNPS
`vintage` split recorded in `Screens/RESUME STATE 2026-09-12 …` item 3G; here the two
vintages are not a restatement, they are two registrants.)*

**And a third inheritance, which is a Q3 item, not a bookkeeping one.** FY2021 10-K, verbatim:
*"on April 22, 2021, SCH concluded that it was appropriate to **restate** its previously issued
audited financial statements as of and for the period ended December 31, 2020, and as part of
such process, SCH **identified a material weakness in its internal control over financial
reporting. As the accounting acquirer in the Business Combination, we inherited this material
weakness and the warrants.**"* The 8-K of 2021-04-22 carries **Item 4.02 — non-reliance.**
The FY2021 **10-K/A of 2022-05-02** (`0001818874-22-000058`) was checked and is benign: its
explanatory note says it was filed *"for the sole purpose of including the information required
by Part III"*. **No restatement of SoFi's own financial statements is on the record.**

**THE ACQUISITION LEDGER, from the filings, with dates** — because a nine-acquisition history
in five years is a perimeter question **[E5-44]**:

| date | target | consideration | where it sits now |
|---|---|---|---|
| 2020 | 8 Limited (Hong Kong) | not separately disclosed | SoFi Holdings (Hong Kong), investing |
| 2020-05 | **Galileo Financial Technologies** | ~$1.2bn, mostly stock | Technology Platform |
| **2022-02-02** | **Golden Pacific Bancorp** — *the charter* | ~$22.3m cash | **SoFi Bank, N.A.** |
| 2022-03-03 | **Technisys S.A.** | **$913.8 million** | Technology Platform (Cyberbank) |
| 2023-04 | Wyndham Capital Mortgage | $72.3m net of cash acquired | Lending (home loans) |
| 2026-Q2 | **Peach Finance Inc.** | part of $70.1m aggregate cash | Technology Platform |
| 2026-Q2 | **Composer** | part of the same $70.1m | Financial Services |

**Goodwill and intangibles at 2026-06-30: $1,425.0m + $226.5m = $1,651.5m, which is 14.9% of
$11,076.2m of book equity.** Of it, **$247.174 million of goodwill was impaired in 2023** —
against the Technology Platform reporting unit — which is the only acquisition post-mortem the
filings contain and is read at Q3 under **[E4-39]**.

**HOW MANY CLEAN YEARS EXIST AS A BANK? FOUR AND A HALF.** SoFi Bank opened 2022-02-02.
FY2022 is a stub bank year (eleven months, $7.6bn of quarterly adjusted average bank assets);
FY2023, FY2024, FY2025 and H1 2026 are full. **The five-year window [E2-42] therefore contains
one pre-bank year (2021) and one part-year (2022), and both are named as distorted at Q4.**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **FY2025 Form 10-K, period 2025-12-31, filed 2026-02-17, accession `0001818874-26-000013`**
    (primary document `sofi-20251231.htm`, 6.77 MB) — the governing document.
  - **Q2 2026 Form 10-Q, period 2026-06-30, filed 2026-08-06, accession
    `0001818874-26-000054`** — and it is not optional: it carries the Technology Platform
    collapse and the current fair-value assumptions.
  - Also read: FY2024 10-K `0001818874-25-000016`; FY2023 10-K `0001818874-24-000026`; FY2022
    10-K `0001818874-23-000018`; FY2021 10-K `0001818874-22-000031`; FY2021 10-K/A
    `0001818874-22-000058`; **DEF 14A of 2026-04-30 `0001818874-26-000032`**; and the **four
    8-K EX-99.1 earnings releases** for Q3 2025, Q4 2025, Q1 2026 and Q2 2026 (accessions
    `0001818874-25-000204`, `0001818874-26-000008`, `0001818874-26-000020`,
    `0001818874-26-000050`), pulled because the CGNX ruling of 2026-09-07 makes the furnished
    earnings release mandatory before scoring **[E4-29]** and **[E4-22]**'s third flag. **On
    this company that ruling earns its keep twice over.**
  - **Counterparty and competitor filings read** (the CCB method, and it decided Q2 here as
    well): **Chime Financial, Inc.** FY2025 10-K `0001795586-26-000013`; **Dave Inc.** FY2025
    10-K `0001193125-26-085370`; **Ally Financial** `0000040729-26-000005`; **Capital One**
    `0000927628-26-000024`; **Synchrony** `0001601712-26-000006`; **LendingClub (now filing as
    "Happen, Inc.")** `0001409970-26-000018`; **Upstart** `0001647639-26-000027`.
- **figures cross-checked against the filed statements — three of them:**
  1. **Equity recomputed from A − L per [E5-32]** (*"the floating plug"* — audited does not
     mean true). Q2 2026: **$60,947,548 − $49,871,321 = $11,076,227 thousand**, which is
     exactly the filed total equity line. FY2025: **$50,660,478 − $40,170,983 = $10,489,495**,
     likewise exact.
  2. **Net income reconciled across statements:** the FY2025 income statement's **$481,320**
     is the opening line of the FY2025 cash-flow statement, and the Q2 2026 statement of
     changes in equity rolls $10,489,495 → $11,076,227 with $323,323 of net income.
  3. **The fair-value components add:** unpaid principal $44,303,296 + accumulated interest
     $271,655 + cumulative fair value adjustments $2,027,061 = **$46,602,012**, the filed total
     fair value of loans at 2026-06-30; and $26,101,759 + $16,134,415 + $2,067,122 =
     $44,303,296 across the three products.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Unit economics in my own words, no management language

SoFi does **three** things, and only one of them is a bank.

**One — it is an unsecured consumer lender that funds itself with deposits.** It takes
**$45.54 billion of deposits**, of which **$45.42 billion (99.72%) pay interest**, at an average
cost of **3.40%** in 2025. It lends the money at **12.89%** on personal loans (weighted average
coupon at 2026-06-30) and **5.89%** on student-loan refinancings, and it earns the spread. The
loan book at 2026-06-30 is **$47.93 billion**, of which **$27.51 billion (57.4%) is unsecured
personal loans**, $16.92 billion student loans, $2.18 billion home loans, and $1.28 billion of
everything else (secured loans, credit card, a small commercial book). Net interest income was
**$2,218.9 million** in 2025 on a **5.85%** net interest margin. That is an ordinary, if
unusually concentrated, consumer bank, and it is legible in an hour.

**Two — it originates loans it does not keep, for a fee.** In 2025 SoFi originated **$11.0
billion of personal loans on behalf of third parties** and collected **$575.9 million of "loan
platform fees"** — up from $141.6 million in 2024 and $33.6 million in 2023. It refers
pre-qualified borrowers to partners, or originates and immediately sells. **This line went from
1.6% to 15.9% of total net revenue in two years and is the whole of the growth in the
Financial Services segment**, whose contribution profit went from −$0.3 million (2023) to
$307.0 million (2024) to **$792.9 million (2025)**. Read plainly: SoFi is renting out its
origination funnel, and taking cash today for credit risk somebody else carries.

**Three — it sells banking software.** **Galileo** (bought 2020) is a card-and-payments
processor; **Technisys** (bought 2022, $913.8m) is a core banking platform. Together they are
the **Technology Platform** segment: $450.2 million of segment net revenue in 2025 and $144.4
million of contribution profit. **This is the leg that is supposed to make SoFi something other
than a bank, and it is shrinking. See Q2.**

**The one sentence that is the whole business:** *SoFi buys consumer relationships with
advertising, funds them with deposits it pays full market price for, lends at 12.9% to prime
borrowers who can refinance elsewhere at a keystroke, and books the difference between what it
paid for the loan and what it thinks someone would pay for the loan as revenue on the day it is
written.*

### The accounting that has to be understood before anything else can be

**Of $60.95 billion of assets at 2026-06-30, $46.60 billion — 76.5% — is loans carried at FAIR
VALUE under the fair value option, and $36.20 billion of the FY2025 figure was LEVEL 3**, i.e.
valued with *"significant unobservable inputs"* by discounted cash flow. Level 3 assets at
2025-12-31 were **$36,648,051 thousand against $10,489,495 thousand of book equity — 3.49
times equity.**

Three consequences, all from the filings:

1. **There is almost no allowance for credit losses, and that is not prudence, it is
   classification.** The allowance is **$56,459 thousand** at 2026-06-30, against $47.93 billion
   of loans, because it applies only to the $1.28 billion held at amortized cost. Credit losses
   on the other $46.60 billion are inside the fair-value mark. **So the provision line —
   $30.3 million in 2025, $22.7 million in H1 2026 — tells a reader nothing about the credit
   risk of 97% of the book.** This is why **[E2-50]** has to be re-pointed for this company.
2. **The mark is above par, and by a lot.** Note 4 of the Q2 2026 10-Q:

| loans at fair value, 2026-06-30 ($000) | Personal | Student | Home | **Total** |
|---|---|---|---|---|
| Unpaid principal balance | 26,101,759 | 16,134,415 | 2,067,122 | **44,303,296** |
| Accumulated interest | 180,704 | 81,501 | 9,450 | 271,655 |
| **Cumulative fair value adjustments** | **1,222,827** | **704,648** | **99,586** | **2,027,061** |
| Total fair value of loans | 27,505,290 | 16,920,564 | 2,176,158 | **46,602,012** |

  **$2,027.1 million of carrying value is a cumulative unrealised write-up above unpaid
  principal and accrued interest.** It was **$1,937.1 million** at 2025-12-31 and **$1,153.6
  million** at 2024-12-31. It is **18.3% of book equity** and **23.6% of net tangible equity**
  at 2026-06-30. **Cumulative net income since FY2019 is MINUS $265.5 million.** The write-up
  on the balance sheet is therefore not a fraction of the earnings record; **it is larger, in
  absolute terms, than the entire earnings record, which is negative.**
3. **Recognition is immediate and revenue-side.** From Note 1: *"We record the initial fair
   value measurement and subsequent measurement changes in fair value in the period in which
   the changes occur within **noninterest income**—loan origination, sales, securitizations and
   servicing."* A loan written today at an above-par mark produces revenue today.

**The inputs are disclosed, and they are the thing to read.** Personal loans at 2026-06-30:
coupon **12.89%**, assumed annual default rate **4.77%**, conditional prepayment **25.77%**,
**discount rate 4.97%**. At 2025-12-31 the personal-loan discount rate was **4.5%** (down from
5.3% a year earlier) and the assumed default rate 4.5%. **The discount rate applied to a
$26 billion book of unsecured consumer paper was, at the last year end, BELOW the 5.34%
thirty-year Treasury**, and it is 37 basis points below it now. It is not my place at Q1 to
call that wrong — the filer's stated basis is *"the volume and terms of recent whole loan sales
and securitization market pricing factors"* — but it is exactly the number **[E2-50]** points at,
and Q3 and Q4 test it.

**Is the business legible? Yes, and the filer does its part.** The fair-value option is
explained in Item 1A, the MD&A, the Critical Accounting Estimates, Item 7A and Notes 1, 4 and
15; the Level 3 rollforward is published; the significant inputs are published with ranges and
weighted averages **quarter by quarter**; the interest-rate and credit sensitivities are
published; the auditor names *"fair value of loans"* as a Critical Audit Matter. **What takes
work is not concealed. It is merely hard.**

### The scarce input this business controls

**Honestly: I cannot name one, and the filer does not claim one.** Test the candidates against
the filings:
- **The charter?** SoFi bought it for about $22 million in 2022. It is not scarce; every peer in
  the Q2 row has one, and the ones that do not (Upstart, and Chime through partner banks)
  compete without one.
- **The deposits?** They cost **3.40%** and **99.72% of them pay interest**. Non-interest-bearing
  deposits are **$126.9 million of $45,543.2 million — 0.28%.** There is no float here.
- **The technology?** Its largest customer replaced it with software the customer built itself
  (Q2).
- **The brand?** It is bought: **sales and marketing was $1,095.4 million in 2025, 30.3% of
  total net revenue**, plus lead-generation inside the segment tables. SoFi's own competition
  section concedes *"many other banks are larger, have been in business longer and often have
  **greater brand awareness** than us."*
- **The member base?** 13.6 million "members" — but see Q2 on how that number is defined.

**The nearest thing to a scarce input is the cost of acquiring a prime borrower who will buy a
second product**, which is what the company calls the Financial Services Productivity Loop.
That is a real operating advantage if it works. **It is not a property; it is a spending
programme, and it is re-bought every year.** Recorded here, decided at Q2.

### Will the fundamentals look broadly the same in ten years?

**The lending half, yes.** Lending prime consumers at a spread over deposits is the same
business it was in 1980.

**The rest, no, and the record rather than my imagination says so.** In five years this company
has: bought a bank charter (2022); bought a core banking platform for $913.8 million (2022) and
written off $247.2 million of Technology Platform goodwill (2023); bought a mortgage lender
(2023); built a $575.9 million third-party origination fee business from $33.6 million in two
years (2023–25); **launched crypto trading in Q4 2025 and booked $255.9 million of gross crypto
transaction revenue in H1 2026 against $253.8 million of cost — a net $2.0 million**; launched a
**stablecoin liability** ($52.5 million at 2026-06-30); and bought two more companies in Q2
2026. **[E3-31]** asks for *"relatively simple and stable in character."* The lending engine is
simple. The company is not stable in character.

### The verdict, and why it is IN and not OUT

I can state the mechanism, the funding, the segment economics, the fair-value machinery and
where the money actually comes from, and I have. **[E4-46]** scopes UNRESEARCHED to documents
rather than competence, and nothing at Q1 rests on an unpulled document. The parts that are
uncertain — whether the marks are right, whether the technology leg has a franchise, whether
the third-party origination fee survives a credit cycle — are **Q2, Q3 and Q4 questions, and
they are decided there.** A business whose character keeps changing is a finding about the
franchise and about survival, not about my comprehension.

- **VERDICT: [x] IN**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The three criteria, taken one at a time, and the second one closes the file — on all three
legs of the business, and on two of them from the counterparties' own filings.**

- **Needed or desired [x]** — yes, plainly. Prime consumers want cheap credit and a place to
  keep money; fintechs need card processing and a core ledger.
- **No close substitute — NO. This is the finding the run turns on, and it is quoted, not
  inferred.** Taken leg by leg.

### Leg one: the Technology Platform. The largest client replaced SoFi with software it built itself.

**SoFi's own Q2 2026 10-Q, verbatim:** *"Technology Platform total enabled client accounts were
135 million, down from 160 million in the prior year period. These results reflected **the exit
of a large client that fully transitioned off our platform prior to December 31, 2025**."* And
in the segment discussion: *"The decrease was primarily attributable to a decline in technology
services fees of **$76.3 million** … reflected the exit of a large client who fully transitioned
off our platform in 2025. This was partially offset by an increase in **intercompany revenue of
$18.2 million**."*

**Who the client was, from ITS OWN 10-K — this is the CCB method and it works here too.
Chime Financial, Inc., FY2025 Form 10-K, filed 2026-03-06, accession `0001795586-26-000013`,
verbatim:**

> *"**Historically, transactions have been processed by Galileo Financial Technologies, LLC
> ("Galileo"), a third-party payment processor. However, as of the end of 2025, we have
> transitioned our members' transactions to being processed by ChimeCore.**"*

And Chime's stated reason, from the same document:

> *"We have invested substantially over several years in our cloud-native technology platform,
> including ChimeCore, to be able to efficiently develop products and process and record
> financial transactions in-house. By operating our technology platform in-house, we are able
> to focus a greater portion of our technology spend on product innovation, avoid costly
> maintenance of legacy systems, and **reduce or eliminate reliance on third-party vendors in
> areas such as transaction processing, financial ledgering, technology and product
> development, and technical operations.**"*

> *"As of November 2025, ChimeCore processes **all** of the payments, transfers, deposits,
> withdrawals, and other financial transactions that are conducted through our platform."*

**Three things follow and each is worse than the one before.**
1. **The substitute was not a rival vendor. It was the customer.** Under **[E3-03]** criterion
   2, a service a customer can build for itself does not lack a close substitute; it has an
   identical one. Chime had 9.5 million Active Members at 2025-12-31 and revenue of
   $2,186.8 million; it is large enough to in-house, and it did.
2. **That customer is also SoFi's most direct competitor in digital consumer banking.** SoFi's
   technology leg was selling the rails to the firm it competes with for the same deposit and
   the same debit interchange. When the customer left, it kept the capability.
3. **What is left is being propped by internal transfers.** Note 17 of the Q2 2026 10-Q:
   *"Within the Technology Platform segment, intercompany fees were **$27,805** and $52,542 for
   the three and six months ended June 30, 2026 … and **$18,182** and $34,377 for the three and
   six months ended June 30, 2025."* Strip the intercompany and the segment's **external**
   revenue fell from **$91.7 million to $56.7 million in one quarter, 38.1%.** The
   accounts-metric footnote concedes the construction: *"We **include intercompany accounts** on
   the Galileo platform as a service in our total accounts metric to better align with the
   Technology Platform segment revenue reported in Note 17 … **which includes intercompany
   revenue.**"*

**The segment's numbers, from the filings:**

| Technology Platform | FY2023 | FY2024 | FY2025 | Q2 2025 | Q2 2026 |
|---|---|---|---|---|---|
| segment net revenue ($000) | 352,340 | 395,178 | 450,211 | 109,833 | **84,505** |
| contribution profit ($000) | 94,786 | 126,955 | 144,413 | 33,195 | **11,772** |
| contribution margin | 26.9% | 32.1% | 32.1% | 30.2% | **13.9%** |
| total enabled client accounts (m) | | | | 160.0 | **134.8** |

**Revenue −23%, contribution profit −65%, accounts −16%, in one year, on a leg that already
carried a $247.174 million goodwill impairment in 2023.** **[E4-55]** — where units exist,
monitor units — and this is the **only** non-cumulative unit series SoFi publishes for this
segment. The physical series is the honest one, and it is down 25.2 million accounts.

**And a second counterparty priced SoFi down in writing. Dave Inc., FY2025 Form 10-K, filed
2026-03-02, accession `0001193125-26-085370`, verbatim:** *"In January 2023, we executed an
amended agreement with Galileo that **significantly reduced processing fees**. The amended
agreement expires on the fifth anniversary of its effective date and thereafter renews for
successive one-year periods unless either party provides four months' written notice of
non-renewal."* That is the identical finding the CCB run made on Prosper's contract with
Coastal, in a different industry, from a different filer, on the same day. **[E4-37]** — the
inverse metric: there is no agony over a price increase to observe, because the price moved the
other way and the customer wrote it down.

**Who else names Galileo in a 10-K, from EDGAR full-text search (2025-06-01 to 2026-09-19,
forms=10-K, 7 hits):** Dave Inc., **Chime Financial**, H&R Block, EVERTEC, Q2 Holdings, and
SoFi itself. Four identifiable customers or rivals; one of them has left; one has cut the price.
*(The search harness needed a fix first — see the tooling defect at the foot of this file.)*

### Leg two: lending. SoFi's founding product IS the frictionless substitution of a rival's loan.

**[E3-03]** criterion 2 asks whether the customer has a close substitute. **SoFi was founded in
2011 to refinance other lenders' student loans**, and the FY2025 10-K explains 2025's 46%
student-loan growth as *"borrowers looked to **refinance at a lower rate**."* A company whose
core product is the keystroke by which a borrower leaves another lender cannot then claim that
its own borrowers cannot leave. **The prepayment assumption is the measurement of exactly that:
conditional prepayment rate 25.77% on personal loans and 10.99% on student loans at
2026-06-30** — a quarter of the personal-loan book is assumed to walk out every year, and the
company's own valuation model says so.

**And the filer concedes the market structure in its own words:** *"The prime lending market is
**highly fragmented and competitive**. We face competition from a diverse landscape of consumer
lenders, including other banks, credit unions and specialty finance lenders, as well as
alternative technology-enabled lenders."* Unsecured prime consumer credit is a price; the rate
is posted; the comparison sites are free. **This is [E2-58]'s commodity end**: *"persistent
over-capacity without administered prices (or costs) equals poor profitability,"* whose **one
exception** is *"a cost advantage that is both wide and sustainable."* SoFi does not have one —
see the row.

### Leg three: deposits. There is no deposit franchise, and the number is 0.28%.

| SoFi deposits, filed | 2026-06-30 |
|---|---|
| interest-bearing deposits | **$45,416,257** thousand |
| noninterest-bearing deposits | **$126,903** thousand — **0.28% of the total** |
| average cost of interest-bearing deposits, FY2025 | **3.40%** |

A deposit franchise in the corpus's sense is money that stays put and costs little. SoFi's
deposits are **99.72% interest-bearing** and priced at market. The filer's own risk factor:
*"heightened market volatility or concerns about the financial sector could increase member
sensitivity to interest rates, safety perceptions, and liquidity needs, **intensifying
competition for deposits and increasing our funding costs**,"* and *"many other banks are
larger, have been in business longer and often have **greater brand awareness** than us."*
**The framework's own worked bank case, Wells Fargo 1990 [E3-24], was bought for a deposit
base; there is no analogue here.**

- **Not price-regulated [x] — but a real part of the economics belongs to a REGIME, and that is
  [E2-59].** SoFi Bank is a national bank and exports its home-state rate under the National
  Bank Act, which is what lets a 12.89% weighted-average coupon exist in states with lower
  usury ceilings; and the student-loan business depends on federal policy — the filer names the
  **One Big Beautiful Bill Act of July 2025**, which *"included provisions to eliminate federal
  Grad PLUS loans, impose lower borrowing limits and restrictions on Parent PLUS loans, starting
  in July 2026"*, and says *"We expect these changes could lead to changes in demand for SoFi's
  student loan products. All such outcomes are **highly uncertain**."* **[E2-59]** is exact
  about what that is worth: administered pricing can floor a business's profits, but *"the moat
  belongs to the **regime**,"* and *"That day is gone"* is how it ends. Since January 2024 SoFi
  Bank and its affiliates are also under **CFPB supervision**, a body with UDAAP authority over
  pricing conduct.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**

**Rebuilt, on the filer's own expense line.** The test the framework sets is *"does a lapse in
spending destroy the structure, or merely narrow it — and does the spending defend the same
advantage, or buy its replacement?"*

| ($000) | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| **sales and marketing** | 719,400 | 796,293 | **1,095,412** | **727,936** (+45% y/y) |
| % of total net revenue | 33.9% | 29.8% | 30.3% | 31.4% |

**Thirty cents of every revenue dollar buys the next customer**, and the asset bought prepays at
25.77% a year. Coca-Cola's advertising defends the same trademark; SoFi's buys the next cohort
of a book that is contractually walking out the door. Inside the segment tables the detail is
starker still: in Q2 2026 the Lending segment spent **$119.8 million of direct advertising and
$89.0 million of lead generation** on $724.8 million of segment revenue, and Financial Services
another $55.4 million of lead generation and $31.4 million of member incentives.

**And on the manager: the business is have-to-be-smart-every-day by construction.** A
$46.6 billion Level-3 book remarked monthly, credit decisioning on unsecured paper, a bank
charter under OCC and Federal Reserve examination, a crypto business launched in Q4 2025 and a
stablecoin liability launched in 2026. Under **[E4-23]** this is recorded **here, at Q2, as a
moat defect** — *"if a business requires a superstar to produce great results, the business
itself cannot be deemed great"* — and it sets the Q3 weight case.

### The metric that cannot fall, and the one that can

**[E2-26]**'s half-owner test bites at Q2 as well as Q3, because the headline metric is the
franchise claim. SoFi's two most-quoted numbers are defined, verbatim, as follows:

> *"**Total products** refers to the aggregate number of lending and financial services products
> that our members have selected on our platform **since our inception through the reporting
> date, whether or not the members are still registered for such products.**"*
> … in Lending, *"the number of personal loans, student loans and home loans that have been
> originated through our platform through the reporting date … **whether or not such loans have
> been paid off.**"*
> … and *"**Since our inception** through December 31, 2025, we have served approximately 13.6
> million members who have used approximately 20.2 million products."*

**Members and products are cumulative-ever counts. They cannot decline.** "Member growth up 35%
to a record 13.7 million members" is the first line of every earnings release and **New Members**
carries 15% of the annual bonus weight. The comparison is not idle: **Chime, in the same
industry, reports 9.5 million *Active* Members.** SoFi does publish two series that *can* fall —
**Technology Platform total accounts, which fell 160.0m → 134.8m**, and **Lending "loans with a
balance", 1,257,965 → 1,744,115, up 39%.** The honest series that is growing is the loan count;
the honest series that is falling is the technology leg. **The flattering series is the one in
the headline.** Recorded under **[E4-55]** and again at Q3 under **[E2-49]**.

### **[E2-44]** — the two-characteristic test, and the second half fails on arithmetic

- *Can it raise prices "even when product demand is flat and capacity is not fully utilized"?*
  **No.** The price is an interest rate set against a posted, comparison-shopped market, and
  the discount rate in SoFi's own valuation model moves with *"benchmark interest rates"* and
  *"credit spreads … indicated by asset-backed security and secondary markets."*
- *Can it grow dollar volume "with only minor additional investment of capital"?* **No, and this
  is the cleanest failure in the file.** It is a balance-sheet business: every dollar of asset
  growth requires equity at the leverage ratio. The (c) table computed at Q3 shows **$7,096
  million of capital required against $359 million earned, 2022–2025**, and **89.8% of the
  $6,699 million of equity added since 2021 came from selling shares, not from earning money.**

### **[E3-46]** — "the second question about the business is a number"

*"the best businesses, by definition, are going to be businesses that earn very high returns on
capital employed over time."* SoFi's recomputed return on average equity capital, from the
filed statements: **−22.73% (2021), −6.69% (2022), −5.76% (2023), +8.48% (2024, of which the
whole of the beat is a $265.3 million deferred-tax valuation-allowance release), +5.66%
(2025).** On the filer's own daily-average permanent equity, FY2025 is **6.27% after tax and
6.85% pre-tax.** That is not a high return on capital employed; it is below the sovereign.

### **[E4-36]** — which of the four causes of extreme success is this?

**Wave-riding.** The record — deposits from zero to $45.5 billion in four and a half years,
"members" from 1.9 million (2020) to 13.6 million (2025) — is the 2022–2026 wave of (i) a bank
charter acquired near the bottom of the rate cycle, (ii) a deposit market in which a
top-of-table online savings rate gathered $11.2 billion a year, and (iii) the de-SPAC funding
window that supplied the equity. **[E3-51]**: *"when a surfer gets up and catches the wave and
just stays there, he can go a long, long time. But if he gets off the wave, he becomes mired in
shallows."* **A surfing run is not a moat; the advantage lives in the wave.**

### **[E2-45]** — the attacker's test, the shelf's one forward-looking moat test

*"how I would like, assuming I had ample capital and skilled personnel, to compete with it."*
**Buy a small bank charter for about $20 million** — SoFi paid roughly $22 million for Golden
Pacific in 2022 — **post 25 basis points more on savings, licence a core ledger, and spend
$1 billion a year on advertising.** That is not a thought experiment: it is the list of firms
that did it between 2019 and 2026 (Ally, Marcus, Chime through partner banks, Varo, Current,
Robinhood, LendingClub via Radius, Upgrade, Figure). And on the technology leg, **the filer
writes the attacker's plan itself**: *"We face competition from larger institutions that could
make investments into an integrated platform as a service solution or to a cloud-native digital
and core banking solution, and also **undercut our pricing, preventing our current clients from
renewing**, while also impeding our attempts to acquire new clients."*

### THE COMPETITOR ROW — required **[E3-28]**

Same metric, same window, filing-sourced, accession per row. The metric set is chosen for a
bank per **[E5-37]**: **cost of interest-bearing deposits** (the funding advantage, which is
where a deposit franchise shows up), **net interest margin**, and **return on equity** as the
filer states it.

| Company | ticker | cost of interest-bearing deposits FY2025 | FY2024 | net interest margin FY2025 | ROE FY2025, as filed | source |
|---|---|---|---|---|---|---|
| **SoFi Technologies** | **SOFI** | **3.40%** | **4.11%** | **5.85%** | **6.27% recomputed on the filer's own average permanent equity; the 2026 proxy reports 9.2% "return on tangible equity"** | FY2025 10-K, acc `0001818874-26-000013`; DEF 14A `0001818874-26-000032` |
| Pathward Financial | CASH | **0.09%** (all deposits) | 0.10% | 7.34% | not taken in this row | 10-K FY to 2025-09-30, acc `0000907471-25-000116` *(as read by the CCB run, 2026-09-19)* |
| The Bancorp | TBBK | 2.06% (all deposits) | — | 4.31% | not taken | 10-K acc `0001295401-26-000002` *(same)* |
| Coastal Financial | CCB | 2.99% (all deposits); **community bank 1.56% Q4 2025** | — | 7.14% | 10.17% | 10-K acc `0001437958-26-000013` *(the CCB run, today)* |
| Capital One | COF | **3.21%** | 3.54% | 7.84% | 2.03% *(Discover merger year; 8.08% FY2024)* | 10-K acc `0000927628-26-000024` |
| Ally Financial | ALLY | 3.56% | 4.18% | 3.43% | 5.77% | 10-K acc `0000040729-26-000005` |
| LendingClub *(now files as **Happen, Inc.**)* | LC | 3.83% | 4.65% | not disclosed as NIM | 9.6% | 10-K acc `0001409970-26-000018` |
| Synchrony Financial | SYF | 4.10% | 4.63% | **15.24%** | **21.1%** | 10-K acc `0001601712-26-000006` |
| Chime Financial | CHYM | **no deposits — bank partners hold them** | — | n/a | net **loss** $1,009.9m on $2,186.8m of revenue | 10-K acc `0001795586-26-000013` |
| Upstart Holdings | UPST | **no bank, no deposits** | — | n/a | +$53.6m net income on $1,043.9m revenue, $798.8m equity | 10-K acc `0001647639-26-000027` |

- **Peers named: nine, plus the subject.** Five are banks with directly comparable deposit
  costs (COF, ALLY, LC, SYF, CCB); three more are the sponsor/BaaS class (CASH, TBBK, and
  Coastal again); two (CHYM, UPST) are the non-bank competitors that matter for the technology
  and origination legs. **Buffett says eight [E3-28]; I took nine.** **The basis differs by
  filer and is stated per row** — some publish an all-deposit cost, some interest-bearing only —
  so the row is directionally comparable, not decimal-comparable, and it is marked as such
  rather than smoothed. Three rows (CASH, TBBK, CCB) are carried across from the CCB run of the
  same day with its accessions, and are attributed rather than re-pulled.
- **Peer unavailability, stated:** Marcus (inside Goldman Sachs), Discover (merged into Capital
  One, May 2025, no longer separately reported), Varo, Current, Chime's partner banks at the
  programme level, and every private core-banking vendor that competes with Technisys (Thought
  Machine, Mambu, 10x) publish nothing comparable. The **FFIEC Call Report** would give SoFi
  Bank's own standalone deposit detail; it is **not on the framework's evidence ladder** — the
  same missing rung the CCB run named hours ago.

**What the row actually shows, and it is three things.**

1. **SoFi's 3.40% cost of deposits is mid-pack among branchless lenders and hopeless against
   anyone with an operating-deposit franchise.** Pathward pays **0.09%**. The Bancorp pays
   2.06%. Coastal's community bank pays 1.56%. **SoFi pays 3.40%, and 99.72% of its deposits
   pay something.** **[E2-58]**'s one exception to the commodity-end doctrine is *"a cost
   advantage that is both **wide and sustainable** … By definition such exceptions are few."*
   **SoFi's cost of funds is not an advantage in the direction that matters: 30 basis points
   better than Ally's, 331 basis points worse than Pathward's.**
2. **The 5.85% net interest margin is not a franchise; it is the asset mix.** It sits between
   Ally (3.43%, auto) and Synchrony (15.24%, private-label cards), exactly where a
   57%-unsecured-consumer, 35%-student book belongs. Synchrony earns **21.1% on equity** at a
   **4.10%** cost of deposits, because it has retailer partnerships and near-monopoly card
   economics inside them; SoFi earns **6.27%** at 3.40%. **The peer with the worse funding cost
   earns three times the return on capital.** That is what it looks like when the margin is mix
   and not moat.
3. **Two of the row's members compete with SoFi without a charter at all** — Chime (9.5 million
   Active Members through partner banks) and Upstart (originating through bank partners, and
   *profitable* in FY2025 while Chime is not). **A perimeter that can be competed against from
   outside the perimeter is not a perimeter.**

**[E3-61], the row's limit, stated because the corpus insists on it:** identical structures
produce opposite outcomes — *"In some businesses, the participants behave like a demented
Kellogg. In other businesses, they don't … **I think you'd have to know the people
involved.**"* This row shows ten firms with overlapping structures and returns from a
billion-dollar loss to +21.1% on equity; it cannot tell me which SoFi will be in 2030, and the
corpus says even Munger had no model for that. It is why Q3 is run at gate weight — **and why
it cannot promote the name.**

### Untapped pricing power **[E3-33]** — could a manager raise the return simply by raising prices?

**No, and every observable price move is in the other direction.** **[E5-28]** scopes the
class: *"If you name some business that has incredible pricing power, you're talking about a
business that's **a monopoly or a near monopoly**."* SoFi is one of a dozen digital lenders and
one of several core-banking vendors. On the filed record: the **technology fee was cut in
writing at a customer's request** (Dave, January 2023); the **largest technology customer left
altogether** (Chime, 2025); the **Lending contribution margin fell from 60.1% to 60.0% to
55.0%** across FY2023–25 while origination volume grew 57%; and the **deposit rate is set by
what Ally and Marcus post this morning.** **[E4-37]**'s agony test has nothing to measure
because no price increase was attempted.

### Class and direction

- Class: **[ ] WIDE  [ ] NARROW  [x] NONE  [ ] PROVISIONAL** — for all three legs. It is NONE
  and not PROVISIONAL because the deciding evidence came from **Chime's and Dave's own 10-Ks**
  and from SoFi's own segment disclosures and balance sheet, not from the peers that could not
  be obtained.
- Direction, **[E4-32]** (*the moat widened every year* is *"the primary criterion of a great
  business"*): **narrowing on both legs where a moat was claimed.** Technology Platform accounts
  −16%, revenue −23%, contribution profit −65%, with intercompany revenue rising to cover part
  of it. Lending contribution margin 60.1% → 55.0% while origination volume grew 57%. The leg
  that is growing — third-party loan origination, $33.6m → $141.6m → $575.9m of fees — grows
  because SoFi is **selling the credit risk it used to keep**: a fee for a service, not a
  widening moat, and untested through a downturn.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**Why OUT and not UNRESEARCHED.** Nothing here rests on a document I could not get. The three
findings that decide it are all on the record: **Chime's own 10-K says it replaced Galileo with
its own ledger**; **Dave's own 10-K says it negotiated Galileo's fee down**; and **SoFi's own
balance sheet says 99.72% of its deposits pay interest at 3.40%**, against a peer at 0.09%.
**[E3-03]** criterion 2 fails on every leg, **[E2-44]**'s second characteristic fails on
arithmetic, **[E3-46]**'s number is 6.27%, and the direction is down. **The file closes here.**

---
⛔ **Q3 and Q4 are written below because the operator's brief asked for them, and they are
marked RECORDED, NOT GOVERNING. Q5 does not open: it appears only as
`COMPUTATION — NOT A CLEARANCE` under operator rule 3.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(RECORDED, NOT GOVERNING — the file closed at Q2)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*

- [x] **Daily execution** — **[E3-38]**, its 1991 original **[E3-43]** and the 1977 root **[E2-70]**:
      an undifferentiated product magnifies the manager. *(Scope stated, PRIME RULE 1: [E2-70]'s
      subject is INSURERS — "Insurance companies offer standardized policies which can be copied
      by anyone. **Their only products are promises.** It is not difficult to be licensed, and
      rates are an open book." The generalisation to any undifferentiated product is the
      FRAMEWORK's, in its own Q3 weight table; it is applied here and not extended.)*
      SoFi originated **$36.42 billion of loans in 2025**, decides credit on
      unsecured paper at a $25,810 average balance, **remarks a $46.6 billion Level-3 book
      monthly** with *"third-party valuation specialists … with quarterly oversight by a
      Valuation Committee"*, runs a national bank under OCC and Federal Reserve examination and
      CFPB supervision, and launched a crypto exchange and a **stablecoin liability** in the
      last four quarters. This is have-to-be-smart-every-day by construction.
- [ ] **Control** — no; this would be a minority listed position **[E1-16]**.
- [x] **Leverage** — **[E3-29]**. Assets $60,947.5m over equity $11,076.2m at 2026-06-30 is
      **5.50 : 1**, and **6.47 : 1** on net tangible equity of $9,424.7m. That is **far** below
      the twenty to one the corpus calls *"a common ratio in this industry"*, and **there is no
      leverage ceiling in this framework** — the deleted 10:1 rule does not return
      (`Framework/INVENTIONS - deleted and why.md`). **But the mechanism [E3-29] describes does
      not need 20:1 and it is present in an unusual form here:** *"mistakes that involve only a
      small portion of assets can destroy a major portion of equity."* SoFi's cumulative
      fair-value write-up alone — **$2,027.1m, 3.3% of assets — is 18.3% of equity and 21.5% of
      tangible equity**, and it is an estimate. A 200-basis-point move in benchmark rates costs
      **$1,563.4m of fair value on the filer's own sensitivity table, 14.9% of equity**, from
      1.5% of assets *(the ratio is struck on the 2025-12-31 figures because that is the date
      the table is published for)*.

**Case declared: TWO of the three determinants are high, so Q3 is a BINARY GATE and NO PRICE
COMPENSATES [E3-29, E1-16, E5-35].** *"You can turn any investment into a bad deal by paying too
much. What you can't do is turn any investment into a good deal by paying little."*

**Honesty — binary, permanent, filings-based [E5-16], each matter dated to when it became PUBLIC.**

**Nothing found that is a conduct disqualifier.** Stated in the corpus's required form: *a Q3
pass is the absence of found disqualifiers, not a finding that the managers are honest*
**[E5-17]** — *"People are not that easy to read. Sincerity and empathy can easily be faked."*
What the record contains, dated:

- **2019 — an FTC consent order, still in force**, disclosed in the FY2025 10-K in these words:
  *"in 2019, we were subject to a consent order from the FTC (the "FTC Consent Order"), which
  resolved allegations that we **misrepresented how much money student loan borrowers have saved
  or would save from financing their loans with us**, in violation of the Federal Trade
  Commission Act. Under the FTC Consent Order, we are prohibited from misrepresenting to
  consumers how much money they would save by using our products, unless the claims are backed
  up by reliable evidence."* **This is a marketing-claims order, seven years old, no monetary
  penalty disclosed, and it predates the current CFO and the public company.** It is recorded
  because **[E5-22]** says penalty size is not seriousness in either direction, and because the
  subject matter — overstating a customer's benefit in advertising — sits in the same domain as
  the metric definitions read at Q2. It is **not** scored as a [E5-16] disqualifier.
- **2022-04-18 — a settled putative class action** alleging *"unlawful lending discrimination …
  by making applicants who are conditional permanent residents or DACA holders ineligible for
  loans or eligible only with a co-signer."* *"We made an aggregate payment to the class and the
  class counsel in an **immaterial amount**."*
- **2021-04-22 — the inherited SPAC material weakness and Item 4.02 non-reliance**, described at
  Step 0. **It was the predecessor shell's, not SoFi's**, and no restatement of SoFi's own
  statements is on the record.
- **No consent order, written agreement or memorandum of understanding with the OCC, the Federal
  Reserve, the FDIC or the CFPB is disclosed in any of the five 10-Ks from FY2021 to FY2025.**
  Stated as the absence-claim rule requires: **no instance found in SEC filings.** The sweep was
  a full-text search of five 10-Ks and the submissions index. It cannot see a non-public
  supervisory action; **bank enforcement is published by the OCC and the Federal Reserve, not by
  EDGAR, and that register is outside the framework's evidence ladder** — the same missing rung
  the CCB run named this morning.
- **Item 9A of the FY2025 10-K: internal control over financial reporting concluded EFFECTIVE,
  with a Deloitte & Touche LLP attestation.** No material weakness at any date since FY2021.
  That is a materially better internal-control record than Coastal's.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30]. Each is a prompt to READ, never a verdict.**

- [x] **EBITDA / ADJUSTED-EARNINGS PROMOTION [E4-29] — FIRES AT FULL STRENGTH, AND IT IS THE
  CENTRAL Q3 FACT.** *"Trumpeting EBITDA … is a particularly pernicious practice. Doing so
  implies that depreciation is not truly an expense, given that it is a 'non-cash' charge.
  That's nonsense."* — twelve-plus corpus restatements, ending at *"a banned measurement."*
  **A bank holding company reports Adjusted EBITDA as its primary earnings measure.** From the
  FY2025 10-K's own reconciliation:

| FY2025 ($000) | |
|---|---|
| Net income (GAAP) | **481,320** |
| add back: interest expense — corporate borrowings | 45,723 |
| add back: income tax expense | 44,537 |
| add back: **depreciation and amortization** | **234,151** |
| add back: **share-based expense** | **262,058** |
| add back: restructuring, FX of highly inflationary subsidiaries, servicing-rights and residual FV changes | −13,891 |
| **Adjusted EBITDA (non-GAAP)** | **1,053,898** |

  **The adjusted figure is 119% above the GAAP figure**, and the two largest add-backs are the
  two the corpus refuses outright: **$234.2 million of depreciation and amortization** —
  **[E5-41]**'s *"reverse float … you spend the money first … and record the expense later"*, the
  worst kind of expense because it is already paid — and **$262.1 million of share-based
  expense**, of which **[E5-06]** says *"To say 'stock-based compensation' is not an expense is
  even more cavalier."* The measure appears **13 times** in the FY2025 10-K and is the headline
  of every earnings release read. The filer also runs **Adjusted net revenue**, **Adjusted net
  income**, **Adjusted EPS**, **adjusted EBITDA margin** and **incremental adjusted EBITDA
  margin**. *(The CGNX ruling of 2026-09-07 exists for exactly this and earned its keep again:
  the earnings releases are worse than the 10-K.)*
- [x] **TRUMPETED EARNINGS PROJECTIONS / GROWTH TARGETS [E4-22] — FIRES, AND IT IS A RATCHET
  [E5-30].** The Q2 2026 earnings release headline, verbatim: *"**Increases 2026 Adjusted Net
  Revenue Guidance to $4.75 billion to $4.85 billion**."* Five forward figures are guided every
  quarter — adjusted net revenue, adjusted EBITDA, adjusted net income, adjusted EPS and new
  members — and **none is reconciled**: *"Management has not reconciled forward-looking non-GAAP
  measures to their most directly comparable GAAP measures."* **[E5-30]**: *"once you start it,
  it's all over. You can't quit … And forecasting earnings, I can't imagine anything more
  destructive."*
  **And the medium-term target is the [E4-35] case in its purest form.** From the Q4 2025
  release, 2026-01-30, verbatim: *"Over the medium term, management expects to deliver
  **compounded annual growth in adjusted net revenue of at least 30% from 2025 to 2028**.
  Additionally, management expects to deliver **compounded annual growth in adjusted earnings
  per share of 38% to 42% from 2025 to 2028**."* **[E4-35]** sets the base rate against which
  that must be read: *"I would wager you a very significant sum that **fewer than 10 of the 200
  most profitable companies** in 2000 will attain **15% annual growth in earnings-per-share over
  the next 20 years**"* — and names the cost of the promise, *"lofty targets corrode CEO
  behavior."* **38–42% compound EPS growth, published as a target, is two and a half times the
  rate the corpus says fewer than one in twenty of the best businesses achieves.**
- **THE [E3-48] ACTION WAS RUN, AND IT COMES OUT IN MANAGEMENT'S FAVOUR. This is recorded in
  full because the rule requires the record, not the suspicion.** Pull the company's own past
  guidance and set it against outturn:

| 2025 guidance, by date | adjusted net revenue | adjusted EBITDA | adjusted net income | adjusted EPS |
|---|---|---|---|---|
| Q2 2025 release (prior) | $3.375bn | $960m | $370m | $0.31 |
| Q3 2025 release, 2025-10-28 (raised) | ~$3.54bn | ~$1.035bn | ~$455m | ~$0.37 |
| **FY2025 actual, per the 10-K** | **$3.591bn** | **$1.054bn** | — | — |

  **Guidance was raised and then beaten on both measures.** The proxy publishes the bonus-plan
  outturn against pre-set goals as well: adjusted net revenue target $3,396m, **actual $3,591m,
  106%**; adjusted EBITDA target $993m, **actual $1,054m, 106%**; return on tangible equity
  target 6.8%, **actual 9.2%, 135%**; new members target 3.1m, **actual ~3.6m, 115%**; formulaic
  payout 123%, *"the Compensation Committee exercised **downward discretion** to reduce the
  funding level to 120%."* **A company that publishes pre-set targets, beats them, and then
  trims its own payout is doing the [E2-49] thing right.** **[E3-48]** earns them the weight and
  it is given. **What it does not do is make the 2028 EPS target reasonable, because [E4-35]'s
  base rate is about the next three years and not the last one.**
- [x] **SERIAL SHARE ISSUANCE [E5-15] — FIRES, AND THE ARITHMETIC IS THE WHOLE OF IT.**
  *"one of the surest indicators of a promotion-minded management, weak accounting, a stock that
  is overpriced and — all too often — outright dishonesty."* **The flag is scored as fired and
  then scoped, because on this company [E5-15]'s *reasons* do not all apply and the honest read
  says so.**

| weighted average basic shares (000) | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| | 945,024 | 1,050,219 | 1,150,140 | **1,280,338** |
| year-on-year | | **+11.1%** | **+9.5%** | **+16.1%** |

  **The count is up 35.5% in two and a half years.** What did it:
  - **$3,185.6 million of cash raised in 2025 in two underwritten offerings** — 82,733,817 shares
    at **$20.85** on 2025-07-31 ($1.7bn net) and 54,545,454 at **$27.50** on 2025-12-08 plus
    3.2m more in January 2026 ($1.6bn net). **Roughly 140.5 million shares, 11% of the company,
    sold in five months.** *Against a book value per share of about $8.26 at 2025-12-31, they
    were sold at 2.5× and 3.3× book.* Under **[E5-44]** run in reverse — *"the intrinsic value
    of the shares you give … must not be greater than the intrinsic value of the business you
    receive"* — **selling paper above intrinsic value is accretive, and this was the right act at
    the right price.** *(The stock is now $16.96, 19% and 38% below those prices. That is bad for
    the buyers of the offerings and good for the company, and it is the same verdict the CCB run
    reached on Coastal's December 2024 raise.)*
  - **$772.0 million of the 2026 convertible notes retired by issuing 92,703,674 shares** across
    December 2023 (9,490,000 shares for $88.0m), March 2024 (72,621,879 for $600.0m) and August
    2024 (10,591,795 for $84.0m), with **$677,147 thousand of it recorded as a non-cash
    "Extinguishment of convertible notes by issuance of common stock"** in the 2024 cash-flow
    statement. **Debt discharged in stock.**
  - **Share-based compensation**, below.
  - **And the reserved overhang: 253,630,801 shares, 19.7% of the count**, including an
    **evergreen provision of up to 5% of shares outstanding added every 1 January through 2030**.
  **Why the flag fires but the promotion reading does not stick:** the issuance was disclosed,
  underwritten, priced above book, and the proceeds are visibly in the capital ratios (Tier 1
  leverage 13.4% → 18.8%). The filer says so: *"This increase was primarily driven by the
  issuance of $3.2 billion of common stock during the third and fourth quarters of 2025."*
  **[E5-38]** governs: a fired flag is not a venality finding. **But the flag's economic content
  is real and it is the Q4 finding: 89.8% of the $6,699 million by which equity grew between
  2021-12-31 and 2026-06-30 came from selling shares, not from earning money.**
- [x] **SHARE-BASED COMPENSATION — measured at [E3-70]'s standard, not the charge, and the gap
  is 60%.** *"subtract an amount equal to what the company could have realized by publicly
  selling options of like quantity and structure"* — *"Where SBC is material, the reported charge
  is the floor of the subtraction, not the measure."* Three measures, all filed:

| FY2025 share-based compensation | $m | as % of FY2025 net income $481.3m |
|---|---|---|
| **P&L charge** (income statement, cash-flow add-back) | **262.1** | 54.5% |
| **credited to additional paid-in capital** (statement of changes in equity) — the difference of $51.1m was **capitalised into internally-developed software** | **313.2** | 65.1% |
| **[E3-70] grant value**: 24,784,993 RSUs at $15.91 + 1,820,753 PSUs at $13.42 | **418.8** | **87.0%** |

  Plus **$478.4 million of unrecognized compensation cost** on unvested RSUs at 2025-12-31, to be
  recognised over 2.2 years. **On the corpus's own measure, 87 cents of every dollar of reported
  net income was granted to employees in shares.** *(The usual ratio this project reports —
  SBC ÷ operating cash flow — **cannot be computed**, because operating cash flow is negative in
  every year. That is itself a finding and it is recorded at Q4.)*
- [x] **FILED-FIGURE TELLS [E4-30] — one of the two fires, and the read is mechanical, not
  venal.** Reported growth is **not** unnaturally smooth: pre-tax income runs −$481.2m, −$318.7m,
  −$301.2m, +$233.3m, +$525.9m and net income −$483.9m, −$320.4m, −$300.7m, **+$498.7m**,
  +$481.3m. **Note the 2024 inversion: net income EXCEEDED pre-tax income by $265.3 million**,
  because of *"the release in the fourth quarter of a **$258 million valuation allowance** against
  certain deferred tax assets."* **The whole of 2024's reported profitability is a deferred-tax
  release**, and the filer says so plainly, which is the candour case rather than the flag.
  **But cash taxes are the tell and they fire:** income taxes paid, net, were **$14.3m (2023),
  $26.9m (2024), $28.9m (2025)** against pre-tax income of −$301.2m, +$233.3m and +$525.9m —
  **11.5% and 5.5% of pre-tax income in the two profitable years**, against book effective rates
  of −113.7% (a benefit) and +8.5%. **[E4-30]**: *"This plainly increased their chances of
  attracting undesired questions"*, so the question is asked and answered from the filing: the
  divergence is **net operating loss carryforwards from eleven years of losses, plus the fact
  that fair-value write-ups are book income and not taxable income until realised.** It is
  recorded as read and explained. **[E5-38]** governs the conclusion.
- [x] **WEAK ACCOUNTING [E4-22] — FIRES, on two specific items, and neither is a restatement.**
  *"There is seldom just one cockroach in the kitchen."*
  1. **The discount rate.** The weighted-average discount rate on the personal-loan book was
     **4.5% at 2025-12-31**, down from 5.3% a year earlier, and **4.97% at 2026-06-30**, on
     unsecured consumer paper with a 12.89% coupon and a 4.77% assumed default rate. **The
     30-year Treasury is 5.34%.** At 2025-12-31 the company discounted $20.2 billion of unsecured
     consumer principal at **84 basis points below the long sovereign**, and the year's reduction
     in that rate was itself a source of income. The filer's stated basis is *"the volume and
     terms of recent whole loan sales and securitization market pricing factors, as applicable,
     as indicators of loan fair values"* — **and the observable fact is that there were no
     personal-loan whole-loan cash sales at all in the six months to 2026-06-30** (against
     $1,313.3 million in H1 2025), and **no securitization transfers qualified for sale
     accounting in FY2025, FY2024 H1 or FY2026 H1** other than Loan Platform Business ones.
     **The exit price is being estimated for a $27.5 billion book in a channel the company has
     not transacted in for two quarters.** This is not an accusation; it is the fact pattern
     **[E2-50]** points at, and it is the reason Q4's stress is run on the mark.
  2. **The goodwill test on the shrinking segment.** **$1,364,452 thousand of the group's
     $1,425,015 thousand of goodwill — 95.7% — sits in the Technology Platform segment**, whose
     Q2 2026 contribution profit was **$11.8 million** (annualised $47m) and whose largest client
     left in 2025. The last **quantitative** test was at **2025-09-01**, with a **12.9% discount
     rate for Galileo and 19.3% for Technisys** and a 4.0% terminal growth rate, and the filer's
     own sensitivity says *"if the discount rate … was increased or decreased by 50 basis points,
     the fair value of the Galileo and Technisys reporting units would decrease or increase by
     approximately 4% and 3%."* The **annual test at 2025-10-01 was qualitative ("step zero")**,
     and so was the **Q2 2026 test**: *"we performed a **qualitative assessment** … we concluded
     that it was not more-likely-than-not that the fair value of any of our reporting units was
     below its respective carrying value as of June 30, 2026."* **A reporting unit that lost its
     largest customer, 16% of its accounts, 23% of its revenue and 65% of its contribution
     profit, carrying $1.36 billion of goodwill — 12.3% of book equity — was tested
     qualitatively.** Read as a prompt, and it is a strong one: the unit was impaired by
     $247.174 million once before, in 2023, for the same kind of reason.
- [ ] **unintelligible footnotes — DOES NOT FIRE.** The opposite, and it should be said. The
  fair-value option, the Level 3 hierarchy, the Level 3 rollforward, the significant inputs with
  ranges AND weighted averages **quarter by quarter**, the interest-rate sensitivity at ±100 and
  ±200 basis points, the credit-loss sensitivity, the unpaid-principal-to-fair-value bridge, the
  segment intercompany revenue, the goodwill discount rates and their sensitivities, the
  delinquent-loan-sale tables and the repurchase-obligation exposure ($15.7 billion of loans
  sold subject to reps and warranties) are all published. **Everything this run needed to be
  sceptical about was disclosed by the company.** Q1 and Q4 were reconstructable from the
  document. **[E2-69]** — judge deviations by direction: the crypto business is presented
  **gross and net** ($255.9m revenue, $253.8m cost, **$2.0m net** for H1 2026), disaggregated as
  soon as it became material; that is the honest direction.
- [ ] **dividends funded by issuance [E2-52] — cannot fire.** No dividend has ever been paid on
  the common stock. The only dividends in the record are the Series 1 preferred's, $16.5m in
  2024 and $40.4m in 2023, and that stock was redeemed in May 2024.
- [x] **METRIC-SWITCHING [E2-49] — TESTED ACROSS SUCCESSIVE FILINGS. It half-fires, and the
  half that fires is a definition, not a switch.** The reported ratios for closed years are
  **stable** across the FY2021–FY2025 10-Ks; no yardstick was withdrawn after deteriorating, and
  the bonus plan kept *"the same corporate performance metrics, weightings, and performance
  achievement and payout framework … as in the prior year."* **[E2-49]**'s positive condition —
  *"pre-set, long-lived and small bullseyes"* — is met on the cash-bonus plan. **What fires is
  the definition of the two metrics quoted first in every release**: members and products are
  **cumulative since inception**, *"whether or not the members are still registered for such
  products"* and *"whether or not such loans have been paid off."* A metric that cannot decline
  is not a yardstick; it is a ratchet. It was read at Q2 and it is recorded here too, because
  **New Members carries 15% of the annual bonus weight.**

**STEP 3 — THE PRIMARY TEST [E2-01]. Earnings rate on equity capital employed, *without undue
leverage or accounting gimmickry* — not EPS growth. Multi-year, balance sheet before income
statement.**

**HOW THIS RUN MEASURES RETURN ON EQUITY CAPITAL FOR A BANK — THE CCB CONVENTION, ADOPTED AND
RE-LABELLED, PRIME RULE 3.**

> **CONVENTION (adopted from the CCB run of 2026-09-19; re-stated here because PRIME RULE 3
> requires the label at the point of use, and re-justified on SoFi's own figures because the
> three reasons are DIFFERENT numbers on this company.)** *Owner earnings by the ordinary
> construction — operating cash flow less share-based compensation less a maintenance-capex
> guess — does not work for SoFi, for three reasons visible in its own statements.*
> 1. ***Operating cash flow is not a return: it is NEGATIVE IN EVERY FILED YEAR.*** *−$54.7m
>    (2019), −$479.3m (2020), −$1,350.2m (2021), −$7,255.9m (2022), −$7,227.1m (2023),
>    −$1,119.8m (2024), −$3,742.5m (2025), **−$6,205.4m in H1 2026 alone** —
>    **cumulatively −$27,435.0 million** — because personal-loan originations are classified
>    held-for-sale and therefore run through **operating** activities (*"Changes in loans held
>    for sale, net"*, −$7,000.5m in H1 2026 alone). **Cumulative net income over the same span is
>    −$265.5 million.** The ordinary construction would report owner earnings of about
>    **minus four billion dollars a year** for a company reporting $481 million of net income,
>    which is not conservatism; it is a category error.*
> 2. ***There is no maintenance capex that matters.*** *Purchases of property, equipment and
>    software were $242.4m plus $8.7m of capitalised software in 2025, against $50.7 billion of
>    assets. A loan book does not wear out. The **[E3-44]/[E2-41]** D&A default and the
>    **[E5-20]** capital-intensive exception class are both **silent** here, and that is stated
>    rather than forced, per **[E5-37]**.*
> 3. ***Deposit and loan flows are financing and investing.*** *Net change in deposits was
>    +$11,248.5m in 2025 and +$8,002.9m in H1 2026, inside **financing**; "other changes in loans
>    held for investment" was −$4,199.3m, inside **investing**. The cash statement of a growing
>    bank measures the balance sheet.*
>
> ***So the metric set is selected by business type first, exactly as [E5-37] requires, and the
> metric is the one the corpus itself names for this job — [E2-01]'s "high earnings rate on
> equity capital employed". Three measures, all from filed statements:*** *(i) return on average
> common equity, recomputed; (ii) pre-tax return on average common equity, because 2024's whole
> profit is a tax item; and (iii) **the (c) EQUIVALENT, which is the part that is ours:
> (c) = Δassets × the Tier 1 leverage ratio**, i.e. the equity a bank must retain to hold its
> regulatory capital ratio constant while the balance sheet grows, so that
> **"owner earnings" for a bank = net income − (c)**. Its rationale in one line: it is the only
> construction that makes **[E2-23]**'s "requires to fully maintain … unit volume" mean anything
> for a balance-sheet business, and it is the same idea as **[E2-60]**'s restricted earnings,
> whose third dimension is explicitly **"its financial strength."***
>
> ***Denominator scope, per [E2-43]:** goodwill and intangibles are shown separately, never
> hidden in book equity. SoFi carries **$1,425.0m of goodwill and $226.5m of intangibles** at
> 2026-06-30 — **14.9% of book equity** — so the wedge is real and is reported: book equity
> $11,076.2m, **net tangible equity $9,424.7m**. Share-based compensation is already an expense
> in the reported figures and is not added back **[E5-06]**; it is tracked separately above
> because the **[E3-70]** grant-value measure is 60% larger than the charge.*

| year | net income $m | avg common equity $m *(filer's daily average where published)* | **ROE, recomputed** | **pre-tax / avg equity** | cash tax % of pre-tax |
|---|---|---|---|---|---|
| 2021 | −483.9 | 2,128.6 *(simple)* | **−22.73%** | −22.61% | n/a (loss) |
| 2022 | −320.4 | 4,792.7 *(simple)* | **−6.69%** | −6.65% | n/a (loss) |
| 2023 | −300.7 | **5,225.8** *(filer)* | **−5.75%** | −5.76% | n/a (loss) |
| 2024 | +498.7 | **5,994.6** *(filer)* | **+8.32%** | **+3.89%** | 11.5% |
| 2025 | +481.3 | **7,672.5** *(filer)* | **+6.27%** | **+6.85%** | 5.5% |
| H1 2026 | +323.3 | 10,782.9 *(simple)* | **+6.00% annualised** | +7.49% annualised | — |

**What the series says.** **Five of the six periods are below the 5.34% sovereign on a pre-tax
basis, and the one that clears it — 2024 on an after-tax basis — clears it only because of a
$258 million deferred-tax valuation-allowance release.** The best year the company has ever
had, FY2025, earned **6.85% pre-tax on average equity capital.** **[E2-01]** is the primary test
of managerial economic performance and it is being failed against the government bond, not
against a peer.

**THE (c) EQUIVALENT, and it is the harshest number in the file.** Tier 1 leverage ratio,
SoFi Technologies consolidated, as filed: **21.8% (2022), 12.8% (2023), 13.4% (2024), 18.8%
(2025), 16.5% (2026-06-30)**. SoFi Bank's own: 15.3%, 15.0%, 14.4%, 13.5%, 13.3%.

| year | Δ assets $m | (c) at the holdco's own Tier 1 leverage $m | *(cross-check: at the Bank's)* | net income $m | **net income − (c) $m** |
|---|---|---|---|---|---|
| 2022 | 9,831.3 | 2,143.2 | *1,504.2* | −320.4 | **−2,463.6** |
| 2023 | 11,067.2 | 1,416.6 | *1,660.1* | −300.7 | **−1,717.3** |
| 2024 | 6,176.1 | 827.6 | *889.4* | +498.7 | **−328.9** |
| 2025 | 14,409.5 | 2,709.0 | *1,945.3* | +481.3 | **−2,227.7** |
| H1 2026 | 10,287.1 | 1,697.4 *(at 16.5%)* | *1,368.2* | +323.3 | **−1,374.1** |

**Four-year total 2022–2025: $7,096.4 million of capital required against $358.8 million earned
— a shortfall of $6,737.6 million.** Four-year mean "owner earnings" on this construction
**−$1,684.4 million**; three-year mean (2023–25) **−$1,424.6 million**.

**And the balance sheet confirms it independently, which is the point of the construction:
equity rose from $4,377.3 million at 2021-12-31 to $11,076.2 million at 2026-06-30, +$6,698.9
million, while cumulative net income over exactly that span was +$682.2 million. $6,016.7
million — 89.8% — of the equity increase came from issuing shares.** **[E2-60]** in its exact
terms: earnings whose payout would cost the business *"its financial strength"* are restricted
earnings. **SoFi does not distribute them — no dividend, no buyback — which is the RIGHT answer
to that problem. The corollary is that the shareholder's return from this business is not cash;
it is a book value that has to be topped up by new shareholders whenever growth outruns
earnings, and it has outrun earnings in four of the last four years.**

*A risk-weighted cross-check, because for a consumer lender RWA binds before leverage does:
risk-weighted assets went $15,695.2m (2022) → $22,883.2m (2023) → $27,859.6m (2024) →
$37,234.0m (2025) → **$48,682.4m (2026-06-30)**. ΔRWA × the Tier 1 risk-based ratio gives
$1,078.2m (2023), $796.2m (2024), $2,137.4m (2025) and **$2,141.6m in the first half of 2026
alone** — the same answer by a different route.*

**The half-owner test [E2-26]** — *does this reporting tell me what I would want to know if the
positions were reversed?* **Yes on the hard things; no on the easy one, and that inversion is
itself the finding.**
- **Yes, and unusually so, on everything a sceptic needs**: the Level 3 inputs quarter by
  quarter with ranges; the movement in the discount rate explained to the basis point (*"benchmark
  interest rates declining by 8 bps, along with credit spreads tightening by 1 basis point"*);
  the assumed default rate set **beside** the realised charge-off rate in the same paragraph
  (*"Annualized net charge-off rates on personal loans in the fourth quarter of 2025 were 2.80%,
  which remained lower than the assumed weighted average default rates in our fair value model
  of 4.46%"*); the fact that the charge-off rate was flattered by **$359.9 million of delinquent
  loan sales**; the goodwill discount rates and their sensitivities; the segment intercompany
  revenue that props the technology leg.
- **No on the headline.** The two metrics in the first line of every release — members and
  products — are cumulative-since-inception counts that cannot fall, while the peer in the same
  business (Chime) reports **Active** members. **The hardest disclosures are candid and the
  easiest one is not**, which is the opposite of the usual pattern and worth recording as such.
- **[E2-67]**, the positive pole — Berkshire published a table of its own reserving errors *"so
  you can … judge whether we may have some systemic bias"*, naming the direction. **The nearest
  bank analogue for a fair-value lender would be a backtest of the model: realised losses and
  realised sale prices against the assumptions used, by vintage.** SoFi publishes the
  **single-quarter** comparison (2.80% realised against 4.46% assumed) but **no multi-year,
  by-vintage record of model error and no realised-versus-modelled sale-price series.** So the
  benchmark is met **in part and not in form**, and this is a genuine disclosure gap rather than
  an accusation. It is the one artifact a reader most needs and does not have.

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [x] **resists any change in current direction.** After the largest technology client left, the
  stated course is unchanged: *"We continue to leverage investments made to integrate our
  services and offerings to position the Technology Platform segment for **diversified durable
  growth**,"* and the response was to **buy another technology company** (Peach, Q2 2026) and to
  raise the group revenue guidance.
- [x] **projects or acquisitions materialise to soak up available funds.** $3.19 billion was
  raised in the second half of 2025; **assets then grew $10,287.1 million (20.3%) in the
  following six months** and risk-weighted assets $11,448.4 million (30.7%), taking Tier 1
  leverage back from 18.8% to 16.5% and Tier 1 risk-based from 22.8% to 18.7%. Two acquisitions
  were made in the same half. **This is the imperative's second behaviour in its purest
  balance-sheet form.**
- [ ] staff studies produced to justify the leader's craving — not observable from filings.
- [x] **peer behaviour mindlessly imitated [E3-02] — FIRES, and this is where SoFi differs from
  Coastal, which passed this test.** The named failure mode for a bank is *"the tendency of
  executives to mindlessly imitate the behavior of their peers, no matter how foolish it may be
  to do so."* In the four quarters to 2026-06-30 SoFi launched **crypto trading** (Q4 2025) and a
  **stablecoin liability** (2026), in the exact quarter the whole sector did, and the economics
  are disclosed: **$255.9 million of gross crypto transaction revenue in H1 2026 against
  $253.8 million of cost — a net margin of $2.0 million, 0.8%.** A bank holding company added
  digital-asset custody obligations (*"we may be liable to our users for losses arising from our
  failure to secure these assets from theft or loss"*) and a payment-token liability for
  **eight-tenths of one per cent** on the gross. **Tested, and found against.**

**THE INCENTIVE READ [E4-27] — *"Never, ever, think about something else when you should be
thinking about the power of incentives."* This is the sharpest Q3 finding after [E4-29].**
From the 2026 proxy (accession `0001818874-26-000032`), the 2025 Annual Cash Bonus Plan:

| performance metric | weight | threshold | **target** | maximum |
|---|---|---|---|---|
| **Adjusted Net Revenue** | **35%** | $1,698m | $3,396m | $5,094m |
| **Adjusted EBITDA** | **35%** | $497m | $993m | $1,490m |
| Return on Tangible Equity | 15% | 3.4% | **6.8%** | 10.2% |
| New Members | 15% | 1,550k | 3,100k | 4,650k |

**Four things follow and each is on the face of the document.**
1. **Seventy per cent of the measured weight is on the two non-GAAP measures [E4-29] calls
   nonsense** — adjusted net revenue and adjusted EBITDA, the latter defined to exclude
   depreciation, share-based compensation and corporate interest. **The management is paid on the
   number that deletes its own largest expenses.**
2. **The nearest thing to [E2-01]'s primary test carries 15% of the weight and its TARGET is
   6.8%** — with 3.4% paying out at threshold and 10.2% the maximum. A bank holding company set
   **3.4% return on tangible equity** as the level below which nothing is paid. Against a 5.34%
   sovereign, the threshold is a real loss and the target is roughly a wash.
3. **There is NO credit or asset-quality metric at all.** No charge-off rate, no delinquency, no
   provision, no reserve coverage, and — most striking for this company — **nothing about the
   fair-value assumptions.** A management paid 70% on revenue and EBITDA, with **no** metric that
   moves against it when the discount rate falls, is being paid to originate. *(Coastal's plan at
   least had a charge-off metric, even though it was mis-scoped to exclude the risk that later
   produced its loss. SoFi's has none.)* The only risk control is a **cap** on the individual
   multiplier: *"If an executive does not receive a satisfactory risk rating under the Risk
   Management Effectiveness Assessment Program, the executive's individual performance multiplier
   **may** be capped at 90% or 70% of target."* **All NEOs received satisfactory ratings in
   2025.**
4. **Target payout was earned at 80% of target performance, and shareholders had to ask for that
   to change.** The proxy's own words: *"Stockholders questioned our practice of aligning **80%
   of target achievement with a target (100%) payout** … Previously, 100% payout under our Annual
   Cash Bonus Plan corresponded to 80% of target performance, with target performance based on
   stretch goals. **In response to stockholder feedback**, the Compensation Committee approved
   changes to the design of the **2026** Annual Cash Bonus Plan that align achievement of target
   performance with the target payout, **strengthening the rigor of our goal-setting**."* And on
   the PSU plan: *"Feedback indicated that the relative total stockholder return ("TSR")
   performance metric in our PSU program should target **above-median** performance. In response
   … target performance for the relative TSR metric requires outperformance at the 55th
   percentile."* **Until 2026, the long-term plan paid target for median shareholder returns and
   the annual plan paid target for missing target by a fifth. Both were fixed only after the
   register objected.** **[E2-49]** asks for *"pre-set, long-lived and small bullseyes"*; these
   were pre-set and long-lived, and until this year they were not small.

**Pay, stated plainly.** CEO Anthony Noto's 2025 total compensation was **$30,275,733**
($1,000,000 salary, $25,308,941 of stock awards, $2,760,000 cash bonus, $1,206,792 of other,
which includes **$743,968 of personal aircraft use**, $54,824 of tax equalisation on it and
$408,000 of personal security). The **CEO pay ratio is 248 : 1** on a median employee at
$122,109. Against FY2025 net income of $481.3 million, the CEO's package is **6.3%**. Separately,
*"For Mr. Noto and Mr. Lapointe, these amounts include the value realized upon the vesting of
the first tranche of the 2021 PSUs in the fourth quarter of 2025, which was **$64,435,770** and
$8,328,277, respectively."* **This is recorded as a fact, not as a disqualifier.** What it is
not is modest, and **[E4-27]** requires it to be read beside the metrics above: the money is
paid for adjusted revenue, adjusted EBITDA and new members.

**Insider alignment, from the 2026 proxy's beneficial-ownership table (record date 2026-04-20,
1,282,735,158 shares):** Noto **23,970,768 shares, 1.9%**; all directors and executive officers
as a group, 16 people, **31,614,529 shares, 2.5%**. The largest holders are index funds —
Vanguard 6.4% plus a further 5.3% through Vanguard Capital Management, BlackRock 5.1%. **There
is no controlling holder and no founder block.** Noto's 1.9% is roughly 24× his annual pay at
the current price, which is better alignment than the CCB run found at Coastal (0.26%).

**Capital allocation — the two buyback conditions [E5-08], plus the third [E4-31].**
- (1) **ample funds for operations and liquidity? YES**, and this is the strongest part of the
  file. $3,126.2m of cash, $4,225.7m of investment securities, Tier 1 leverage 16.5% at the
  holding company and 13.3% at the Bank against a 5.0% well-capitalised minimum.
- (2) **repurchases at a material discount to conservatively calculated IV?** **Not applicable —
  no share has been repurchased and no dividend has ever been paid.** **[E2-51]** warns that a
  manager who *consistently* turns his back on repurchases when they are clearly in owners'
  interests *"reveals more than he knows of his motivations"* — **but that is not this case.** A
  bank whose growth already consumes more capital than it earns (the (c) table) fails condition
  (1) the moment it buys stock, and **[E5-25]** puts *"financial strength that is
  unquestionable"* ahead of everything. **No capital-allocation flag on the buyback question.**
- **The allocation acts that CAN be judged, and they split.**
  - **The 2025 equity raises were well done**: $3.19 billion sold at $20.85 and $27.50 against
    about $8.26 of book. **[E5-44]** run in reverse.
  - **The acquisition record is the other way.** $913.8 million was paid for **Technisys** in
    March 2022 in stock; **$247.174 million of Technology Platform goodwill was written off in
    2023**, eighteen months later; and the segment that holds the remaining **$1,364.5 million**
    of goodwill has just lost its largest customer and 65% of its contribution profit.
    **[E4-39]** asks for the rare-positive tell — a candid acquisition post-mortem is *"almost
    never witnessed"*, and the Washington Post reviewed every deal three years after. **SoFi
    publishes no post-mortem on Technisys or Galileo against the announcement case**; the 2023
    impairment is described in the non-GAAP reconciliation as *"not indicative of our core
    operating performance"*, which is precisely the **[E3-53]** treatment the corpus refuses —
    *"to tell owners year after year, 'Don't count this' … is misleading"* **[E5-33]** — and the
    **[E2-57]** except-for flag: *"the real mistake is not the act, but the actor."*
  - **[E3-58]'s prompt is live rather than fired.** Two more acquisitions were made in Q2 2026
    ($70.1 million cash for Peach and Composer, $31.5 million of it goodwill) in the same half in
    which the segment they are meant to reinforce shrank 23%. There is no banker-led serial-M&A
    pattern and no consultant-driven programme visible in the filings, so this is **recorded as
    a prompt, not a finding.**

**THE GUARDRAIL — checked before writing the verdict.**
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** Q2 is OUT and Q3
  cannot repair it **[E2-37, E2-38, E3-39]**. The clean internal-control record, the 1.9% CEO
  stake, the beaten guidance and the accretive equity raises are all real and none of them
  promotes: *"a textile company that allocates capital brilliantly within its industry is a
  remarkable textile company — but not a remarkable business."*
- [x] The business **requires** daily competence, and that is recorded at **Q2 as a moat defect
  [E4-23]**, which it was.
- [x] Is a great manager the reason to act? **No, and the question does not arise** — the
  franchise is not intact **[E2-35, E2-36]**, so there is no *"localized excisable cancer"* to
  excise. This would be the *"corporate Pygmalion"* case, not the excisable-cancer case.

- **VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [x] UNRESEARCHED**

**Why UNRESEARCHED and not IN, stated honestly.** **No conduct disqualifier was found**, and on
an ordinary name that would be enough for IN. But **Q3 was declared a BINARY GATE for this
business**, and at gate weight the framework's own rule bites: *a gate marked IN carrying
"unverified" or "provisional" is UNRESEARCHED*. Two things at gate weight are not on the
record, and **both can be named, which is what makes this UNRESEARCHED rather than UNKNOWABLE**:
1. **THE WORK ORDER — the model backtest.** The whole of this company's reported profitability
   rests on the fair-value assumptions for a $46.6 billion Level-3 book, and there is **no
   by-vintage record of modelled versus realised loss, and no realised-versus-modelled sale-price
   series**, in any filing. *The artifacts that would resolve it and where they live:* the
   **ABS deal documents and monthly servicer reports** for SoFi's own personal-loan and
   student-loan securitization shelves (SoFi Consumer Loan Program and SoFi Professional Loan
   Program trusts), filed on EDGAR by the trusts themselves as **Form 10-D and ABS-EE**, which
   carry loan-level performance against origination vintage. **Ladder rung: SEC EDGAR primary
   documents, a DIFFERENT registrant. Not blocked; not pulled in this run.**
2. **THE WORK ORDER — the supervisory record.** "No consent order disclosed" is an absence
   claim, and the framework's own absence-claim rule says an absence may be asserted only where
   a recorded sweep looked for it and only as *"no instance found."* The sweep here was a
   full-text search of five 10-Ks and the submissions index. It cannot see a non-public
   supervisory action. *The artifacts:* the **OCC enforcement-action database** and the
   **Federal Reserve's enforcement register** for SoFi Bank, N.A. and SoFi Technologies, Inc.
   **Ladder rung: outside the ladder. Not pulled** — the same gap the CCB run recorded this
   morning, now confirmed on a second bank.

---

## Q4 — WILL IT SURVIVE? *(RECORDED, NOT GOVERNING)*

### Owner earnings — the construction is the CONVENTION declared at Q3

The ordinary construction is refused for the three reasons given above; the measure is **net
income less the capital retention the balance sheet requires**, and the numbers are in the Q3
table. Both windows are carried, with the spread, per **[E4-25]**:

- **Short window, three years 2023–25: mean −$1,424.6 million.**
- **Long window, four years 2022–25: mean −$1,684.4 million.** *(A five-year window is not
  available on this construction: 2021 precedes the bank charter, so there is no Tier 1 leverage
  ratio to apply and Δassets that year is +$612.8 million against a recast pre-bank balance
  sheet. **The corpus's default window [E2-42] cannot be honoured, and that is stated rather
  than faked.**)*
- **Spread:** both windows are deeply negative and the spread does not change the sign. **The
  capex band is NOT APPLICABLE and that is stated rather than forced** — property and software
  purchases were $251.1 million against $50.7 billion of assets, and the (c) that matters is
  regulatory capital, not plant, so the **[E3-44]/[E2-41]** D&A default and the **[E5-20]**
  exception class are both silent, per **[E5-37]**.
- **Distorted years sit in the window and they are named [E5-11]: TWO of them.** **2024**, whose
  entire reported profitability is a **$258 million deferred-tax valuation-allowance release**
  (pre-tax income was $233.3m and net income $498.7m); and **2025**, in which $3.19 billion of
  equity was raised in the second half, so the year-end Tier 1 leverage ratio of 18.8% used in
  the (c) column is itself elevated by the raise. Running 2025's (c) at the Bank's 13.5% instead
  gives $1,945.3m rather than $2,709.0m — **still $1,464.0 million more than the year earned.**
- **Stock compensation is subtracted in full and is inside the reported figures [E5-06]:**
  $262.1 million charged, $313.2 million credited to paid-in capital, **$418.8 million at the
  [E3-70] grant-value measure — 87.0% of reported net income.** The usual SBC ÷ operating-cash
  ratio is not computable because operating cash flow is negative in every year.

### CUMULATIVE NET INCOME AGAINST CUMULATIVE OPERATING CASH FLOW, AND WHAT THE MARKS CONTRIBUTED

The brief asks for this directly and it is the arithmetic that most changes how the company reads.

| FY | net income $m | operating cash flow $m | cumulative fair value adjustment on loans, at year end $m |
|---|---|---|---|
| 2019 | −239.7 | −54.7 | n/d |
| 2020 | −224.1 | −479.3 | n/d |
| 2021 | −483.9 | −1,350.2 | n/d |
| 2022 | −320.4 | −7,255.9 | n/d |
| 2023 | −300.7 | −7,227.1 | n/d |
| 2024 | +498.7 | −1,119.8 | **1,153.6** |
| 2025 | +481.3 | −3,742.5 | **1,937.1** |
| H1 2026 | +323.3 | −6,205.4 | **2,027.1** |
| **cumulative** | **−265.5** | **−27,435.0** | **+2,027.1 carried on the balance sheet** |

**Three readings, and all three are the same fact from different sides.**
1. **Cumulative operating cash flow is −$27.4 billion against cumulative net income of −$265.5
   million.** The $27.2 billion gap is almost entirely *"Changes in loans held for sale, net"* —
   −$5,270.9m in 2025 and −$7,000.5m in H1 2026 — i.e. **loans originated and kept.** Funded by
   +$11,248.5m and +$8,002.9m of net deposit inflow inside *financing*. **Operating cash flow
   here measures the balance sheet, and the CCB run's finding is confirmed from the opposite
   direction.**
2. **What the fair-value marks contributed.** The balance-sheet stock is **$2,027.1 million of
   carrying value above unpaid principal and accrued interest** at 2026-06-30, up from $1,153.6
   million at 2024-12-31. **It grew $783.6 million during 2025 and a further $89.9 million in
   H1 2026.** The income-statement flow can be read three ways from the filings and all three
   are large relative to the earnings: *"Fair value changes in loans held for investment"* in
   the cash-flow reconciliation were **$351.2m (2025), $158.2m (2024), $44.0m (2023)** — that
   line alone is **73% of FY2025 net income** and it is explicitly non-cash; the Level 3
   rollforward's net *"Impact on Earnings"* was **+$121.5m (2025)** and **−$471.8m (2024)** —
   though that figure mixes in interest income and charge-offs and so is not a clean measure of
   the mark; and the filer's own instrument-specific-credit-risk estimate was **+$106.1m (2025),
   +$73.3m (2024), −$26.6m (2023)**.
   **The cleanest honest statement: the cumulative unrealised write-up now standing on the
   balance sheet, $2,027.1 million, is LARGER IN ABSOLUTE TERMS THAN THE ENTIRE CUMULATIVE
   EARNINGS RECORD OF THE COMPANY, which is negative $265.5 million.** That is not a charge of
   impropriety — the marks may prove right, the loans may pay, and the realised charge-off rate
   of 2.62% is *below* the 4.77% assumed. **It is the plainest possible statement of where the
   reported profit lives: on the balance sheet, as an estimate, not in the bank.**
3. **And the revenue recognition is at origination.** *"We record the initial fair value
   measurement and subsequent measurement changes in fair value in the period in which the
   changes occur within noninterest income."* A loan written today at an above-par mark is
   revenue today. **[E4-34]**'s fourth auditor's-eye question — is there any action with *"the
   purpose and effect of moving revenues or expenses from one reporting period to another"* — is
   answered by the accounting policy itself: **GAAP-permitted, elected, disclosed, and it moves
   revenue forward.** The policy is legitimate; the reader has to know it is there.

### Great, good, or gruesome? **[E4-20]**

- [ ] great — [ ] good — [x] **gruesome**, and **[E4-43]** is applied so as not to over-read it.
  The *good* class **passes**: *"nothing shabby about earning $82 million pre-tax on $400 million
  of net tangible assets"*, and ~12% on retained capital is *"quite satisfactory"* **[E5-40]**.
  **SoFi is not in the good class and the three-part test says why.** *Grows rapidly* — assets
  +$10,287.1m, 20.3%, in six months; origination volume +57% in 2025. *Requires significant
  capital to engender the growth* — the (c) table: **$7,096 million required against $359 million
  earned over four years**, with **$6,017 million of equity bought from new shareholders**.
  *And then earns little or no money* — **6.85% pre-tax on average equity capital in the best
  year it has ever had, against a 5.34% sovereign**, and negative in three of the five years
  before. **[E4-20]**'s own warning applies exactly: investors *"attracted by growth when they
  should have been repelled by it."* What would rescue it is **[E4-43]**'s clause — *"unless the
  cash they consume gets to earn a reasonable return"* — and 6.85% pre-tax is not one.

### Staying power — score all three **[E5-11]**

- **(1) a large and reliable stream of earnings — LARGE, AND MORE RELIABLE THAN COASTAL'S, BUT
  ESTIMATE-DEPENDENT.** Net interest income is genuinely large and growing: $2,218.9m in 2025,
  $1,481.2m in H1 2026 (+45.7%). **That part is cash.** But of $1,394.4m of FY2025 noninterest
  income, **$575.9m is loan platform fees** (a new, three-year-old line growing 4× a year and
  never tested through a downturn) and **$242.9m is "loan origination, sales, securitizations and
  servicing"**, which is where the fair-value marks and servicing-rights revaluations live. And
  the reported return is below the bond. **Score: large, growing, and dependent on a valuation.**
- **(2) massive liquid assets — YES, and this is unambiguously the strongest thing in the file.**
  At 2026-06-30: **$3,126.2m of cash and cash equivalents**, $439.3m restricted, **$4,225.7m of
  investment securities** (of which $3,993.3m available-for-sale, marked, with an amortized cost
  of $3,993.3m — i.e. **no material unrealised AFS loss**, which is exactly what killed three
  banks in 2023). Borrowings are **$3,300.5m** — $645.0m drawn revolver, $428.0m of 2026
  converts, $862.5m of 2029 converts, the rest warehouse — against **$11,076.2m of equity**.
  **Tier 1 leverage 16.5% at the holding company and 13.3% at the Bank, against a 5.0%
  well-capitalised minimum; total risk-based 18.8% and 15.3% against 10.0%.** **[E5-39]**:
  *"We will never be dependent on the kindness of strangers."* On solvency, SoFi is not.
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — and here it is BETTER than Coastal, which
  failed this test, and the number that decides it is 97%.**
  - **Uninsured deposits were $1.0 billion at 2025-12-31 against $37.5 billion of total
    deposits, and the filer states: "approximately 97% of our total deposits were insured."**
    Coastal's uninsured share had gone to 27.7%. **This is a real and material difference and it
    belongs in the bull case.** The mechanism is the **Insured Deposit Program**, a reciprocal
    network giving *"expanded FDIC insurance coverage of up to $3 million."* **Its condition is
    disclosed and is the thing to watch:** *"while SoFi Bank met the definition of
    "well-capitalized" as of December 31, 2025 and currently has no restrictions regarding
    acceptance of **brokered deposits** or setting of interest rates, there can be no assurance
    that we will continue to meet this definition"* — **the FDIA's brokered-deposit provisions
    would bite if capital fell, and the coverage that makes the deposits sticky depends on the
    network.**
  - **Time deposits due in less than one year: $1.2 billion.** Small.
  - **The one real near-term item: $428.0 million of 2026 convertible notes mature on
    2026-10-15 — twenty-six days after this run** — against $3,126.2m of cash. Trivially
    covered, and the filer notes the stock is below the conversion price so no share settlement
    above par arises.
  - **$848.3 million of sponsorship, advertising and cloud commitments** over 1 to 14 years,
    $126.4 million due in 2026 and $325.3 million *"thereafter"*.
  - **$15.7 billion of loans sold subject to representation-and-warranty repurchase
    obligations** at 2025-12-31, against an $18.4 million accrual. That is the contingent tail
    and it is disclosed.
  - **Score: 3 of 3 on solvency, with the qualification that the deposit stickiness is a
    function of a reciprocal insurance network whose availability is conditioned on capital.**
    **This is the single most important respect in which SoFi is a stronger business than
    Coastal, and it is recorded plainly.**
- **Leverage, named and quantified** — **5.50 : 1** on book equity and **6.47 : 1** on net
  tangible equity at 2026-06-30. **No ratio ceiling is applied and none is implied**;
  **[E2-54]**'s coverage test passes comfortably (corporate borrowing interest $21.3 million in
  H1 2026 against $1,481.2 million of net interest income). **[E3-52]** — read the terms, not the
  quantity: SoFi's deposits have **no covenants and the shortest due date there is**, which is
  the same read Coastal got; its warehouse facilities **do** have covenants — *"maintaining:
  (i) a certain minimum tangible net worth, (ii) minimum unrestricted cash and cash equivalents,
  (iii) a maximum leverage ratio of total debt to tangible net worth, and (iv) minimum risk-based
  capital and leverage ratios"* — and the company *"was in compliance with all financial
  covenants."* **The covenants are struck on tangible net worth, which the $1,651.5 million of
  goodwill and intangibles reduces, and which a reversal of the fair-value write-up would reduce
  further.** That linkage is the mechanism at the foot of this section.
- **Jurisdiction [E3-66]:** US filer, Delaware corporation, national bank. Shareholders stand
  where US law puts them, which the corpus calls *"especially favorable to shareholder
  interests."* No adjustment. *(The Argentine operations are highly inflationary and cost
  $7.1 million in 2025 — material to the technology segment, immaterial to the group.)*

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]** — and model exposure, not experience **[E4-40]**

**[E4-40]** is the governing instruction and it bites here: *"all of us in the industry made a
fundamental underwriting mistake by focusing on **experience, rather than exposure**."* SoFi's
**experience** is a personal-loan annualised charge-off rate that **fell** to 2.62% in Q2 2026
from 3.03% in Q1, *"including the impact of asset sales, new originations and **delinquency
sales** in the quarter"* — and the company sold **$359.9 million of delinquent unpaid principal**
during 2025, which removes loans from the book **before** they charge off. Its **exposure** is
$26.1 billion of unsecured consumer principal at a 12.89% coupon, marked at a 4.97% discount
rate, in a channel it has not sold into for two quarters. A benign and actively-managed loss
history is *"not only useless, but actually dangerous"* as a guide.

**A. THE CORPUS'S LITERAL TEST, run three ways on the loans the bank actually owns the risk of.**
Following **[E3-24]** *"Consider some mathematics"* exactly — 10% of the loans producing losses
averaging 30% of principal, set against a year's pre-tax income:

| base | amount $m | 10% × 30% loss $m | vs FY2025 pre-tax $525.9m | vs annualised H1 2026 pre-tax $807.7m | after tax, as % of equity |
|---|---|---|---|---|---|
| all loans, carrying value | 47,933.4 | **1,438.0** | −$912.1m | −$630.3m | **10.1%** |
| loans at fair value, unpaid principal | 44,303.3 | 1,329.1 | −$803.2m | −$521.4m | 9.4% |
| **personal loans only, unpaid principal** | 26,101.8 | **783.1** | −$257.2m | **+$24.7m** | **5.5%** |

**The Wells Fargo parity is exact on the personal-loan book and fails on the whole book.** On
the unsecured book alone — the part a consumer recession actually hits — **SoFi roughly breaks
even, which is precisely the 1990 result, and Buffett's conclusion would apply:** *"A year like
that — which we consider only a low-level possibility, not a likelihood — would not distress
us."* On the **whole** book, SoFi does not break even: it loses about $630 million pre-tax
against its best run-rate, which is 10.1% of equity after tax, and survives easily.

**Pushed harder, on personal loans:** 15% at 40% severity = $1,566.1m, 11.0% of equity;
**20% at 50% = $2,610.2m, 18.4% of equity**, equity falls to $9,040.3m and equity/assets from
18.2% to 14.8%; 30% at 50% = $3,915.3m, 27.6% of equity. **At a $4 billion pre-tax loss — five
times the company's best annual earnings — Tier 1 risk-based capital is still 12.31% and Tier 1
leverage 10.84%, both far above every regulatory minimum.** **THIS BANK DOES NOT DIE OF CREDIT,
and the $3.19 billion raised in 2025 is exactly why.**

**B. THE MARK, which is the other candidate, and it does not kill the company either.**
- **Reverse the entire cumulative fair-value write-up**: $2,027.1m pre-tax, **$1,581.1m after
  tax, 14.3% of equity.** Equity falls to $9,495.1m, still 15.6% of assets.
- **The filer's own rate sensitivity**: +200 basis points costs **$1,563.4m of fair value**,
  **14.9% of 2025 equity**, from a book of $36.4 billion — an implied effective duration of about
  **2.15 years**. +100bp costs $766.1m, 7.3%.
- **The filer's own credit sensitivity**: a **10%** increase in credit loss rates costs
  $149.9 million of fair value, 1.4% of equity. Scaled linearly, doubling the assumed loss rate
  (4.77% → 9.5%) would cost roughly **$1.5 billion**, 14% of equity.
- **Combined — write-up reversed AND the [E3-24] literal test on personal loans:** $2,191.9m
  after tax, **19.8% of equity**, equity to $8,884.3m and 14.6% of assets. **Still comfortably
  well-capitalised.**

**C. SO WHAT ACTUALLY HAPPENS. The mechanism, in one sentence.** **SoFi does not die; the
owner's per-share claim does.** The business earns **6.85% pre-tax on equity capital** while its
growth requires equity equal to **15–19% of every dollar of new assets**, so growth cannot be
funded from earnings and must be bought from new shareholders — which it has been, to the tune
of **$6,017 million of the $6,699 million by which equity has grown since 2021, 89.8%**.
Meanwhile the reported profit that makes the shares saleable is, to the extent of **$2,027
million on the balance sheet**, an unrealised write-up on assets the company keeps and funds,
with **cumulative operating cash flow of minus $27.4 billion**. **The loop closes only while the
market will keep buying the paper.** When it stops — because the growth rate falls below the
guided 30%, or because the mark reverses, or because tangible net worth tightens the warehouse
covenants — the company continues, well capitalised and profitable on the income statement, and
simply stops compounding per share.

**Quantified from filed figures.** Diluted shares went **945.0m (2023) → 1,101.4m (2024) →
1,251.8m (2025) → 1,365.0m (H1 2026)**, up **44.4%**, while book value per share went from about
$5.54 (2023: $5,234.6m ÷ 945.0m weighted) to **$8.58** at 2026-06-30 — real progress, but bought.
**To hold Tier 1 leverage at 16.5% while growing assets 30% a year, as guided through 2028, SoFi
must add roughly $3.0 billion of capital a year against $0.65–0.80 billion of annual earnings.
The gap is about $2.2 billion a year, and at $16.96 that is 130 million shares a year — 10% of
the company, annually.** *(This is the framework's arithmetic on the company's own guidance, not
a company projection.)*

- **Likelihood: [x] A REAL POSSIBILITY** — and note carefully what the likelihood attaches to.
  **Insolvency is a low-level possibility at best**: the capital, the liquidity, the 97% insured
  deposit base and the absence of AFS losses make it so, and that is the honest finding. **What
  is a real possibility, on the company's own guidance and its own capital ratios, is that the
  per-share compounding does not happen** — that the shareholder funds 30% asset growth out of a
  6.85% pre-tax return on equity and receives the difference in dilution.

- **[E4-51] test — can I state the argument against my own conclusion better than its holders?**
  *The bull case, fairly stated:* **SoFi is the only digital-first consumer bank in the United
  States that has reached scale, profitability and a national charter simultaneously.** It has
  13.6 million members, $45.5 billion of deposits gathered in four and a half years at a cost
  below Ally's, 97% of them FDIC-insured, and a securities portfolio with no unrealised loss. It
  has raised $3.19 billion of equity above three times book, retired convertible debt with
  shares issued at high prices, and now runs Tier 1 leverage of 16.5% — **more capital than any
  peer in the row and more than it needs**, which means the next several years of growth can be
  funded internally at a lower rate than the last. It has been profitable for eight consecutive
  quarters, beaten raised guidance in 2025, published pre-set incentive targets and cut its own
  payout, reports effective internal control with a Big Four attestation, has no consent order
  in five annual reports, and discloses its Level 3 assumptions quarter by quarter beside the
  realised charge-off rates — which is more than most banks do about their reserves. Its
  realised personal-loan charge-off rate of **2.62% is 215 basis points BELOW its own assumed
  4.77%**, so if anything the marks are conservative. The third-party origination business —
  $575.9 million of fees in its second full year — converts the same customer acquisition into
  **capital-free** revenue, which is the answer to the capital problem the bear case rests on.
  And the fair-value option is not an artifice: it is the same election the corpus's own
  Berkshire makes on equities, and it puts the loss in the income statement **earlier** than
  CECL would, not later.
  **I do not think that case is wrong about the capital, the liquidity, the deposit insurance or
  the disclosure. I think it is wrong about the word "only": Chime has 9.5 million active
  members without a charter and built SoFi's own technology in-house; Ally has $148.8 billion of
  interest-bearing deposits at 3.56%; and Synchrony earns 21.1% on equity while paying 4.10% for
  its money. Scale reached is not scale defended, and 6.85% pre-tax on equity is the number that
  says which one this is.**

**THE SURVIVAL SHAPE.** Checked against every shape in `Screens/SURVIVAL SHAPES - index.md` as
it stood when this file was written. *(The index's own instruction is to count the table and
never the summary sentence; the number is assigned at fold time from the table as it then
stands, because concurrent runs are adding shapes today.)*
Closest existing: **#2 EARNS NOTHING FOR OWNERS AFTER PAYING ITS PEOPLE**, present as a
**feature** — SBC grant value $418.8m is **87.0% of FY2025 net income**, and the usual
SBC ÷ operating-cash ratio cannot even be computed because operating cash flow is negative;
**#11 THE PASS-THROUGH**, also a **feature** — 3.40% of the loan yield is passed to depositors
on a 99.72%-interest-bearing book, Galileo's fee was cut at a customer's written request, and
the Lending contribution margin fell 60.1% → 55.0% while volume grew 57%; and
**#8 THE EQUITY IS THE REVENUE**, which is **not** right, because SoFi's customers do pay for
the service and the company is GAAP-profitable. None is the mechanism.

**PROPOSED — THE MARKED BOOK** *(pending the operator)*: **earnings are recognised at
origination as an unrealised write-up on an asset the lender keeps rather than sells, so the
reported profit is a valuation and not a receipt; the cash never arrives, because the asset is
retained and funded with deposits, leaving operating cash flow permanently and heavily negative;
growth consumes regulatory capital at ten to twenty times the rate the valuation earns it; and
the gap is closed by issuing shares, which the market supplies for as long as the reported
growth holds. The company does not fail — it survives very large credit and rate shocks, because
the equity it raised to grow is also the equity that absorbs them — but the owner funds the
growth twice, once in the dilution and once in the return foregone, and the per-share claim
stops compounding without anything visibly breaking.**

It is distinct from **#8 THE EQUITY IS THE REVENUE** (there, customers pay a small part of the
costs; here they pay all of them and the company is profitable); from **#2** (there, employees
take the operating cash; here the cash never exists and the employees' share is a symptom);
from **#11 THE PASS-THROUGH** (there, the gains go to customers or suppliers; here the *gain is
an estimate that has not yet been collected from anyone*); from **#24 THE BOUGHT AVERAGE**
(there, a falling unit price is concealed by purchased mix; here the unit price is fine and it
is the *cash conversion* that is absent); and from **#25 THE INDEMNITY** (there, the loss is
contracted away to a counterparty and booked as income; here there is no counterparty at all —
the loss is retained and the *income* is the lender's own discount rate). **Its tells are
checkable on any filer:** cumulative operating cash flow far more negative than cumulative net
income with the gap in one held-for-sale line; a cumulative fair-value write-up larger than
cumulative earnings; asset growth times the regulatory capital ratio exceeding net income for
several consecutive years; and equity growth exceeding retained earnings by an order of
magnitude.

- **VERDICT (recorded, not governing): [ ] IN  [ ] OUT  [x] UNRESEARCHED**
  *The gruesome finding under [E4-20] and the (c) table point to OUT. What stops this run from
  writing OUT here is the same missing artifact as at Q3 — **the by-vintage model backtest**,
  which lives in the securitization trusts' own 10-D and ABS-EE filings. Without it the marks
  can be stress-tested (above) but not audited, and a gate that rests on an unpulled document is
  a work order, not an answer. The file is closed at Q2 regardless.*

---
⛔ **Q5 DID NOT OPEN. Q1 was IN; Q2 was OUT.** What follows is the below-gate arithmetic the
operator's brief required, under operator rule 3.

## COMPUTATION — NOT A CLEARANCE

*This section carries **no entry language**, no verdict, no ranking position, no value range and
no margin of safety. It exists to state, in words, what the price is and what a buyer at that
price is paying for.*

- **Price US$16.96, close of 2026-09-18** (aggregator, flagged). **Corroborated against primary
  documents:** seven Forms 4 filed 2026-09-16 report SoFi shares at **$17.279–$17.32** for
  transactions of 2026-09-14, and Forms 4 of 2026-08-19 at **$18.002**.
- **Shares 1,291,570,324** (Q2 2026 10-Q cover, 2026-07-31, accession `0001818874-26-000054`).
- **Market capitalisation US$21,905.0 million.**
- **Book value per share at 2026-06-30: $11,076.227m ÷ 1,290,312,404 = $8.58. Price/book 1.98×.
  Tangible book value per share $7.30 (goodwill $1,425.0m + intangibles $226.5m removed);
  price/tangible book 2.32×.**
- **Sovereign 5.34%**, US Treasury 30-year par yield, 2026-09-18, issuing authority.

| measure, all from filed statements unless marked | amount $m | % of the $21,905.0m market cap | points vs the 5.34% sovereign |
|---|---|---|---|
| FY2025 net income | 481.3 | **2.20%** | −3.14 |
| FY2025 pre-tax income | 525.9 | **2.40%** | −2.94 |
| trailing twelve months net income (H2 2025 + H1 2026) | 636.3 | 2.90% | −2.44 |
| annualised H1 2026 net income | 646.6 | 2.95% | −2.39 |
| **annualised H1 2026 pre-tax income — the most favourable honest figure in the file** | **807.7** | **3.69%** | **−1.65** |
| four-year mean net income, 2022–25 | 89.7 | 0.41% | −4.93 |
| four-year mean pre-tax income, 2022–25 | 34.8 | 0.16% | −5.18 |
| **four-year mean, retention-adjusted (the CONVENTION)** | **−1,684.4** | **−7.69%** | −13.03 |
| three-year mean, retention-adjusted | −1,424.6 | −6.50% | −11.84 |
| *(for reference only, and it is not an earnings measure)* FY2025 **Adjusted EBITDA**, the company's own primary measure | *1,053.9* | *4.81%* | *−0.53* |

- **Against the ~10% floor [E4-28]** — *"that's the figure we quit on"*, and it does not move with
  the sovereign: the honest pre-tax expectancy at this price is **3.69% on the best run-rate the
  company has ever produced** and **0.16% on the four-year mean.** **Both are far below the
  floor, so the name is not ranked.** On the construction this run believes is right for a bank
  it is **minus 7.69%**.
- **AND IT IS BELOW THE BOND TOO, WHICH IS WHERE IT DIFFERS FROM COASTAL.** The CCB run recorded
  *"above the bond, below the floor"* — Coastal's FY2025 pre-tax yield of 8.71% was 337 basis
  points over the sovereign. **SoFi is 165 basis points BELOW the sovereign on its very best
  figure**, and 294 below it on FY2025 pre-tax. **Even the company's own Adjusted EBITDA — a
  measure that adds back depreciation and share-based pay and which [E4-29] calls nonsense —
  yields 4.81%, still 53 basis points below a riskless thirty-year Treasury.** **No risk premium
  is added to the rate [E3-42]**; certainty is not priced here at all, because the file closed at
  Q2 and no value range is being asserted.
- **What the price already assumes, and this is the most useful line in the section.** To reach
  the ~10% floor from the annualised H1 2026 pre-tax run-rate, pre-tax income must go from
  **$807.7m to $2,190.5m** — **+171% in one year, or 39.5% a year compounded for three years, or
  22.1% a year for five.** **The company's own published medium-term target is 38–42% compound
  growth in adjusted earnings per share from 2025 to 2028.** So: **at $16.96 the buyer is paying
  a price at which, IF management delivers the 38–42% compound target it has published — a rate
  [E4-35] says fewer than one in twenty of the 200 most profitable companies in America achieves
  over any long run — the buyer would merely ARRIVE at the ~10% floor in 2029, having been paid
  nothing for the three years of risk.** On the retention-adjusted construction the figure has
  to travel from −$1,684m to +$2,191m, which is not a growth rate; it is a different company.
- **The ceiling, per [E2-63]:** the WPPSS analysis capped its own upside at face value, and
  *"the great majority of operating businesses have a limited upside potential also **unless more
  capital is continuously invested** in them. That is so because most businesses are unable to
  significantly improve their average returns on equity."* **SoFi's average ROE is 6.27% and more
  capital IS being
  continuously invested — from new shareholders.** The upside is bounded by the return on
  equity capital, and that is the bound.
- **What the same figures imply about price, stated only as arithmetic and NOT as a value
  range** *(no value range is asserted; Q5 did not open)*: capitalising the annualised H1 2026
  pre-tax figure **at the ~10% floor** gives $8,077m, **$6.25 a share**; **at the bare sovereign
  of 5.34%** it gives $15,126m, **$11.71 a share**. **Book value is $8.58 and tangible book
  $7.30.** The quote is $16.96.
- **No bar is chosen, no margin is applied, and no windage is spent: [E4-25]**'s three outcomes
  require a Q1–Q4 pass to be meaningful, and Q2 is OUT. **Windage count: zero.**
- **What the buyer at $16.96 is paying for, in words, which is the part of this section that
  matters.** The buyer is paying **1.98× book and 2.32× tangible book, and 28.3× the company's
  own guided 2026 adjusted EPS of about 60 cents**, for: a genuinely large and growing digital
  consumer bank with **$45.5 billion of deposits gathered in four and a half years, 97% of them
  FDIC-insured**, an investment portfolio with **no unrealised loss**, Tier 1 leverage of 16.5%
  and $3.1 billion of cash — **the strongest balance sheet in its peer group, and the single
  best thing about the company**; **plus** a $26.1 billion book of unsecured consumer principal
  yielding 12.89% and carried at a **4.97% discount rate**, 37 basis points below the long
  sovereign, in a channel the company has not sold into for two quarters, with **$2,027 million
  of cumulative unrealised write-up above par** standing on the balance sheet against a
  **cumulative earnings record of minus $265 million** and **cumulative operating cash flow of
  minus $27.4 billion**; **plus** a banking-software business whose largest customer replaced it
  with software the customer wrote, taking 16% of the accounts and 65% of the segment's
  contribution profit, and which still carries **$1,364 million of goodwill tested only
  qualitatively**; **less** the fact that growth of the kind guided requires roughly
  **$3 billion of new equity a year against $0.65–0.80 billion of earnings**, which at this price
  is about **130 million shares a year — ten per cent of the company, annually**. **In one
  sentence: at this price the buyer is paying twice tangible book for a well-capitalised lender
  that earns 6.85% pre-tax on its equity, books the profit before the cash arrives, and must
  sell him more shares every year to grow.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Nothing is held, so [E2-28]'s sell rule has nothing to act on, and [E1-02]'s "yardsticks prior
to the act" is recorded as the REVERSAL CONDITION for the Q2 OUT instead.**

- **Thesis-confirming metrics (would confirm the OUT):**
  1. **Technology Platform total enabled client accounts** falling further from 134.8 million, or
     **external** (ex-intercompany) Technology Platform revenue falling below $56.7 million a
     quarter. Both are computable from the segment note and footnote (1) each quarter.
  2. **Cumulative fair value adjustments on loans** continuing to rise as a share of equity above
     18.3%, or the **personal-loan weighted-average discount rate** falling again below 4.97%
     while the coupon falls.
  3. **Weighted average diluted shares** rising more than 8% a year, or a further underwritten
     offering.
  4. **Return on average equity capital** staying below the 5.34% sovereign on a pre-tax basis.
  5. **A goodwill impairment in the Technology Platform segment** — $1,364.5 million is at risk
     and the last quantitative test was 2025-09-01.
- **Thesis-breaking metric and its threshold (would force the Q2 OUT to be revisited):**
  **the deposit cost and the non-interest-bearing share, together.** The OUT rests on the finding
  that SoFi has no deposit franchise and no substitute-proof product. **It would be broken if
  noninterest-bearing deposits rose from 0.28% of total deposits to above 10%, AND the cost of
  interest-bearing deposits fell more than 100 basis points below Ally's in the same year** —
  i.e. if the "primary banking relationship" claim started to show up in the funding cost the way
  it does at Pathward and at Coastal's community bank. Both numbers are in the average-balance
  table of every 10-K. **A second, independent breaker: the Technology Platform winning back a
  client of Chime's scale, visible in the accounts metric returning above 160 million.**
- **Next catalyst dates:** the **2026 convertible notes mature 2026-10-15** (26 days); the
  **Q3 2026 10-Q**, expected early November 2026 on the filing pattern (2025-11-06 for the prior
  year), which will show the next quarter of Technology Platform accounts and the next
  fair-value assumption set; and the **FY2026 10-K in mid-February 2027**, the only filing that
  carries the annual goodwill test, the uninsured-deposit percentage and the full-year capital
  ratios.
- **[E4-17]/[E3-30] monitoring question — aberrational cycle or permanent slippage?** The
  Technology Platform decline, read alone, could be one large customer and therefore an
  aberration. **Read with Dave's written fee cut, with the filer's own statement that competitors
  could *"undercut our pricing, preventing our current clients from renewing"*, and with the fact
  that the substitute was built by the customer rather than bought from a rival, it is
  slippage** — the capability is replicable by the people who buy it. On the lending side the
  operative sentence is the company's own valuation assumption: **a 25.77% conditional prepayment
  rate is the company's own estimate of how fast its customers leave.**
- **Position size: ZERO.** Not a judgment about sizing; the business failed Q2.
- **No band is armed in `tools/alerts.json` and no `PORTFOLIO.md` row is added.** The QLYS ruling
  of 2026-09-07 governs: a name that failed on the **business** gets a reversal condition in
  words, not a price alert. The words are above.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** *(carrying Q2's verdict;
  nothing is owned and nothing is armed)*

---
## WHAT THE FRAMEWORK STILL LACKS FOR BANKS — the second bank, and three of the four gaps are CONFIRMED

The CCB run of this morning named four structural gaps. This run hit three of them and found a
**fifth that only a fair-value lender exposes**. **None is fixed here; PRIME RULE 5 requires a
written case and the operator's approval for a structural change, and PRIME RULE 6 requires the
ledger row before the rule.**

1. **Q2 HAS NO PASSABLE FORM FOR A BANK — and this run is the WRONG evidence for that claim,
   which is itself worth recording.** CCB warned that **[E3-43]** classes a bank as *"a business,
   unlike a franchise"*, which read literally makes **Q2 OUT automatic for every bank**, and asked
   the operator to decide. **This run did not need the general question**: it closed Q2 on
   Chime's own 10-K, Dave's own 10-K, a 0.28% noninterest-bearing deposit share and a 65% fall in
   a segment's contribution profit — findings that would close Q2 at a software company or a
   cement company. **So after two banks the score is 2–0 for "the general question did not have
   to be decided", and the operator should be told that the question is less urgent than CCB
   feared** — but also that **neither bank has yet tested it**, because neither had a deposit
   franchise to defend. **ACNB is the one that will test it** (a Pennsylvania community bank with
   real branch deposits), and **JPM and TFC after it.** The two candidate resolutions stand as
   CCB stated them: (a) Q2 for a bank is a *local-deposit-franchise* test — cost of deposits and
   share against named peers; or (b) **[E3-29]** creates an explicit exception class in which Q2
   returns NARROW and the decision moves to Q3 and Q5. **(a) now has the better evidence**,
   because the metric that decided both bank runs was **the cost of deposits against named
   peers**, which is exactly test (a), built twice independently.
2. **THE EVIDENCE LADDER STOPS TOO SOON FOR A REGULATED FILER — CONFIRMED, SAME TWO RUNGS.**
   Two of the things this run most needed are not on EDGAR under the subject's own CIK: the
   **OCC and Federal Reserve enforcement registers** (the only place a supervisory action against
   SoFi Bank, N.A. becomes public — EDGAR cannot see one, so *"no consent order disclosed"* has to
   be written as *"no instance found in SEC filings"*) and the **FFIEC Call Report** (SoFi Bank's
   standalone deposit and asset detail, and the only public data on private competitors).
   **This is now two banks out of two.** **A third rung is exposed by this run specifically and
   it IS on EDGAR, just under a different registrant: the securitization trusts' own Form 10-D
   and ABS-EE filings**, which carry loan-level performance by origination vintage — the only
   public artifact that could audit a fair-value lender's marks. The current ladder is
   *SEC XBRL → SEC EDGAR primary documents → company IR → exchange filings → EDINET → competitor
   filings*. **It has no rung for "the subject's own off-balance-sheet or affiliated registrants"
   and no rung for a prudential regulator's public register.**
3. **OWNER EARNINGS NEEDS A DECLARED FORM FOR BALANCE-SHEET BUSINESSES — and the CCB CONVENTION
   NOW HAS A SECOND INDEPENDENT TEST, WHICH IT PASSES.** `(c) = Δassets × the regulatory leverage
   ratio` was written this morning for Coastal, where it produced a $111.6 million five-year
   shortfall on a $703 million company. **Applied unchanged to SoFi it produces a $6,738 million
   four-year shortfall on a $21,905 million company, and the balance sheet confirms it by a
   completely independent route** — equity up $6,699 million on cumulative earnings of $682
   million, so $6,017 million came from issuing shares. **A convention that reproduces itself from
   the equity account on two very different banks is worth adopting.** Its strongest corpus anchor
   remains **[E2-60]**'s third dimension of maintenance, *"its financial strength."* **It should
   either be adopted with a ledger row or refused; it should not be re-invented a third time.**
   *One refinement this run adds: for a consumer lender, risk-weighted assets bind before total
   assets, and the RWA-based cross-check (ΔRWA × the Tier 1 risk-based ratio) gave the same
   answer to within 1% on FY2025. Either denominator works; the run should state which.*
4. **"COMPUTATION — NOT A CLEARANCE" AND THE PRICE VERDICT — the same question, with a sharper
   fact.** CCB asked whether the below-gate section may carry a price verdict, having found that
   Coastal *also* failed the ~10% floor. **SoFi fails harder and differently: it is below the
   BOND on every construction, including the company's own Adjusted EBITDA.** That is a second,
   independent, sufficient reason not to buy. **This run records the floor result as a note
   beside the Q2 FAIL, not as the fail line**, as CCB did, and flags the convention for
   confirmation. **Two runs have now made the same choice, so it is becoming practice by
   accretion rather than by ruling, which is exactly how the framework's confirmed errors were
   made.**
5. **NEW, AND ONLY A FAIR-VALUE LENDER EXPOSES IT: the framework has no test for an
   ESTIMATE-DERIVED EQUITY, and [E2-50] as written points at the wrong document.** The corpus's
   instrument for *"earnings created by the stroke of a pen"* is **the reserve-development
   table** and **[E2-67]**'s candour benchmark — a filer publishing its own reserving errors so a
   reader can *"judge whether we may have some systemic bias."* **For a lender that elects the
   fair value option there is no allowance, no reserve and no development table**: SoFi's
   allowance is $56.5 million against $47.9 billion of loans, and 76.5% of the balance sheet is
   marked. The equivalent artifact — **the model backtest: assumed default, prepayment and
   discount rates against realised losses, prepayments and sale prices, by origination vintage,
   over years** — **does not exist in any SoFi filing**, and no accounting standard requires it.
   **So [E2-50]'s instruction is live and its instrument is missing.** Two things follow that the
   operator may wish to rule on:
   - **Where the run should look instead** — the securitization trusts' 10-D/ABS-EE filings
     (item 2 above), and the **filer's own quarter-by-quarter juxtaposition of assumed against
     realised** (SoFi does publish this for one quarter at a time: *"Annualized net charge-off
     rates on personal loans in the fourth quarter of 2025 were 2.80%, which remained lower than
     the assumed weighted average default rates in our fair value model of 4.46%"*). **Stitching
     those single-quarter statements into a multi-year series across ten 10-Qs and five 10-Ks is
     the nearest available substitute, and it is a real piece of work that this run did not do.**
   - **A candour test that would work on this class**, offered as a candidate rather than a rule:
     **does the filer publish its own model error over time, and in which direction?**
     **[E2-67]**'s Berkshire table named the direction (*"always presented a better underwriting
     picture than was truly the case"*). **A fair-value lender that published the same thing would
     be doing the corpus's own test; one that publishes only the current quarter's comparison —
     which is all SoFi does — has met it in substance for one period and not in form for any.**

*And a tooling matter, which is item 5 of the CCB list confirmed and extended:* `tools/run.py`
and the screening layer build owner earnings from operating cash flow. **For Coastal that was
5.4× too high; for SoFi it is NEGATIVE $3.7 billion on a company reporting $481 million of net
income.** Any screen that priced SoFi on operating-cash-flow-based owner earnings would have
rejected it as bottomlessly loss-making, and any screen that priced Coastal the same way would
have priced it at five times its earnings. **The construction is not merely imprecise for banks;
it has no sign.** The 2026-09-01 triage dropped financials as a class, which accidentally avoided
both; **if financials are ever screened, the construction must change first.**

---
## THE TOOLING DEFECT FOUND AND FIXED IN THIS RUN

**`tools/sources.py:fts_count()` returned a well-formed ZERO for every query that passed `forms`
as a Python list — which is the natural idiom and which the signature invites.** This is the
**identical silent-false-negative class** the function's own docstring was written to prevent in
the parameter next to it (the CALX defect of 2026-09-12), and it could defeat that guard.
Measured on the phrase `"Calix"` this afternoon, before the fix:

| call | result |
|---|---|
| `fts_count('Calix', forms=['10-K'])` | **200, 0 hits** — the natural Python idiom |
| `forms='10-K'` | 200, **306 hits** — correct |
| `forms='10-K,10-Q'` | 200, **622 hits** — correct (306 + 316) |
| `fts_count('Calix', cik='0000926282', forms=['10-K'])` | **200, 0 hits** — where the no-forms call returns 40 |

The list urlencodes to `forms=%5B%2710-K%27%5D` — a Python repr — and EDGAR answers **HTTP 200
with an empty body and no warning.** This run hit it first and reported *"0 hits in 10-Ks"* for
`"SoFi"`, `"SoFi Technologies"`, `"Galileo Financial Technologies"` and `"SoFi Bank"` — **four
false negatives on the question the framework treats as evidence, because a moat is a relative
claim [E3-03]**. It was caught only because the unrestricted query returned 10,000 and the
contradiction was checked. **The fix coerces a list, tuple or set to the comma-joined string the
endpoint expects; a bad FORM NAME still fails loudly with HTTP 500, so no further guard is
needed.** Verified after the fix: `forms=['10-K']` → 306, `forms=('10-K','10-Q')` → 622, and
`cik='0000926282', forms=['10-K']` → **20**, which is exactly the figure the docstring records as
correct. **`python tools/check_framework.py` PASSES.**

*This is the fifth consecutive session in which the defect found was **a guard that read one side
of its own input** (`level_shift` four times, the `cik` half of `fts_count` once, and now the
`forms` half of the same function). The pattern is worth naming: **when a guard is added to one
parameter, test the parameters beside it.***

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT — the file closed there**;
      Q3 and Q4 written and explicitly marked **RECORDED, NOT GOVERNING** at the operator's
      instruction; Q5 did not open and appears only as `COMPUTATION — NOT A CLEARANCE`.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Only Q1 is IN and
      it rests on read filings. Q3 was *not* marked IN precisely because two gate-weight items
      rest on unpulled documents.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: Q3 names the
      **securitization trusts' Form 10-D and ABS-EE filings** (SoFi Consumer Loan Program and
      SoFi Professional Loan Program shelves, on EDGAR under the trusts' own CIKs) and the
      **OCC and Federal Reserve enforcement registers** (outside the ladder); Q4 names the same
      by-vintage backtest.
- [x] Every UNKNOWABLE verdict states what cannot be known — **none was written.**
- [x] Step 0: the filing was read, with accession numbers (FY2025 10-K `0001818874-26-000013`,
      Q2 2026 10-Q `0001818874-26-000054`, four earlier 10-Ks, the FY2021 10-K/A, the 2026 proxy,
      four 8-K EX-99.1 earnings releases, ten Forms 4 read individually, and seven competitor or
      counterparty 10-Ks). **Three figures cross-checked:** equity recomputed from A − L at both
      dates; net income reconciled across the income statement, the cash-flow statement and the
      statement of changes in equity; and the fair-value component bridge added in both
      directions.
- [x] **The predecessor question was answered from the filings, both ways:** the operating history
      is Social Finance's (reverse recapitalization, SCH the accounting acquiree), **and the CIK
      nonetheless carries the SPAC's own audited figures at the same period end** — the trap is
      recorded with both tagged values and both accessions.
- [x] Owner earnings: **the ordinary construction was refused with reasons and the CCB CONVENTION
      was adopted, re-labelled and re-justified on this company's own figures (PRIME RULE 3)**;
      two windows are reported with the spread; the **five-year default [E2-42] is stated as
      unavailable and why**, rather than faked; the capex band is stated **not applicable** and
      why, rather than forced.
- [x] Competitor row filled — **nine filed peers plus the subject**, same metric, same window,
      accession per row, with the basis difference disclosed per row, the three rows carried from
      the CCB run attributed, and the private and merged competitors named as an explicit limit.
      The moat is **NONE**, not PROVISIONAL: the deciding evidence came from **Chime's and Dave's
      own 10-Ks**, not from the unavailable peers.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-18, **struck fresh for this run** rather than inherited.
- [x] **No value range is stated at all** — correct, because Q5 did not open. Two capitalisation
      arithmetics are shown and both are explicitly labelled as arithmetic, not as a range.
- [x] No bar chosen and no margin applied; **windage count: zero.**
- [x] Prices dated; aggregator flagged **and corroborated against nine SEC-filed Form 4
      transaction prices**.
- [x] **Share count from the latest cover, with the issued-versus-outstanding check, the
      per-class check, and a three-way post-cover issuance check** (no block issuance on the
      record; ten Forms 4 read individually; seven Form 144s identified as notices, not sales).
      **The 253,630,801-share reserve and the 5%-a-year evergreen are recorded as live channels
      and are NOT in the count.**
- [x] `python tools/check_framework.py` **PASSES**, after the `fts_count` fix.
- [x] Run committed to git **with a pathspec**, per the six-step fold, at each question.

## REGISTER
- Verdict: **[x] OUT (about the business)** — at **Q2**.
- One line: **SOFI (SoFi Technologies, Inc.), 2026-09-19 — FAIL at Q2, OUT on the business. The
  technology leg's largest client replaced Galileo with software it wrote itself: Chime
  Financial's own FY2025 10-K (acc `0001795586-26-000013`) says *"as of the end of 2025, we have
  transitioned our members' transactions to being processed by ChimeCore"*, and SoFi's Q2 2026
  10-Q records *"the exit of a large client"* with accounts 160.0m → 134.8m, segment revenue
  −23%, contribution profit −65%, and intercompany revenue rising from $18.2m to $27.8m to cover
  part of it; Dave Inc.'s own 10-K adds that in January 2023 it *"executed an amended agreement
  with Galileo that significantly reduced processing fees"*. There is no deposit franchise
  either: 99.72% of $45.54bn of deposits are interest-bearing at 3.40%, against Pathward at 0.09%
  and Coastal's community bank at 1.56%, while Synchrony earns 21.1% on equity paying a WORSE
  4.10%. [E2-01]'s primary test is 6.85% pre-tax on average equity capital in the best year the
  company has had. Price US$16.96 (2026-09-18, aggregator, corroborated by Form 4 prices of
  $17.28–$18.00), 1,291,570,324 shares from the Q2 2026 10-Q cover of 2026-07-31 (accession
  `0001818874-26-000054`), cap US$21,905.0M, P/B 1.98×, P/TB 2.32×, sovereign 5.34% (US Treasury
  30-year, 2026-09-18). Below-gate note: it also fails the ~10% floor AND the bond — 3.69% pre-tax
  on the best run-rate it has ever produced, 2.40% on FY2025, 0.16% on the four-year mean, and
  minus 7.69% on the retention-adjusted construction; even the company's own Adjusted EBITDA
  yields 4.81% against a 5.34% sovereign. The CIK carries the SPAC predecessor's own audited
  figures at the same period end ($806,077,995 of assets at 2020-12-31 under acc
  `0001104659-21-037483` against $8,563,499,000 under acc `0001818874-22-000031`). Cumulative net
  income since FY2019 is MINUS $265.5M against cumulative operating cash flow of MINUS
  $27,435.0M and a cumulative fair-value write-up of PLUS $2,027.1M standing on the balance
  sheet. Proposed survival shape: THE MARKED BOOK.**
- **If UNRESEARCHED:** not the governing verdict. The two work orders inside Q3/Q4 are the
  **by-vintage model backtest** (the securitization trusts' own Form 10-D and ABS-EE filings) and
  the **supervisory record** (OCC and Federal Reserve enforcement registers) — the second on a
  **ladder rung the framework does not currently have**, now confirmed on two banks out of two.
- **If UNKNOWABLE:** not applicable.

---
# ADDENDUM, 2026-09-19 19:40 EDT — THE FDIC CALL REPORT ROW, THE CNR SPLIT, AND A CORRECTION TO THIS FILE'S OWN COUNT

*Written as an addendum and not by editing the text above, per operator rule 6. **Nothing below
changes any verdict.** Two of the three items strengthen the Q2 OUT; the third is the single
strongest fact against it found anywhere in this run, and it is stated first.*

## 1. CORRECTION: THIS IS THE THIRD BANK, NOT THE SECOND

**This file's own heading says "THE SECOND BANK THIS PROJECT HAS RUN" and that is wrong.**
`Test Runs/2026-09-19 Run - ACNB ACNB Corporation.md` was written and folded the same afternoon —
register entry 128, overnight-log line 16:31 EDT — and it is described there as *"the SECOND bank
this project has run and the FIRST to clear the business gates."* **SoFi is the THIRD.** The
coordinator's message that dispatched this fold also said "second". **The heading is left standing
and corrected here, because that is what operator rule 6 requires and because the queue's own
standing instruction is the relevant one: do not trust any count quoted in a brief — count the
register.** *(Counted for this fold with a line-start regex: 118 bullets in the
`## COMPLETED FROM THE QUEUE` slice proper, plus the 10 in the `### REGISTER BACKFILL 2026-09-13`
subsection that follows it, which is how a reader reaches 128.)*

**ACNB left two explicit rulings for the three banks still queued — "SOFI, JPM and TFC" by name.
Both are applied below.**

## 2. ACNB'S RULING ONE, APPLIED: THE CNR SPLIT OF Δ ASSETS INTO ORGANIC AND ACQUIRED

ACNB's ruling: *"the bank CONVENTION for return on equity capital **needs the CNR split of
Δassets into organic and acquired** whenever the filer has bought anything inside the window, or
(c) reports a stock issuance as a loss of earning power."* SoFi bought **four** things inside the
window, so the ruling bites and the split is done. Acquired assets, from the filings and from the
issuing authority:

- **Golden Pacific Bank, N.A., closed 2022-02-02: $174,662 thousand of total assets** at
  2021-12-31 — **from the FDIC Call Report, CERT 26881** (the charter SoFi bought is the same
  CERT SoFi Bank files under today, so the FDIC carries the predecessor's own balance sheet).
  The 10-K discloses only the $11.2 million of goodwill and says the acquisition was *"not
  determined to be a significant acquisition."*
- **Technisys S.A., closed 2022-03-03: total identifiable assets acquired $281,563 thousand**
  (FY2022 10-K, of which $239,000 thousand was intangibles), on $913,764 thousand of
  consideration.
- **Wyndham Capital Mortgage, 2023: $72,301 thousand** net of cash acquired (cash-flow statement).
- **Peach Finance and Composer, Q2 2026: $70,100 thousand** of cash consideration in aggregate.

| year | Δ assets $m | **acquired $m** | **organic $m** | (c) unsplit $m | **(c) ORGANIC $m** | net income $m | **NI − (c) organic $m** |
|---|---|---|---|---|---|---|---|
| 2022 | 9,831.3 | 456.2 *(4.6%)* | 9,375.1 *(95.4%)* | 2,143.2 | **2,043.8** | −320.4 | **−2,364.2** |
| 2023 | 11,067.2 | 72.3 *(0.7%)* | 10,994.9 *(99.3%)* | 1,416.6 | **1,407.3** | −300.7 | **−1,708.1** |
| 2024 | 6,176.1 | 0.0 | 6,176.1 *(100%)* | 827.6 | **827.6** | +498.7 | **−328.9** |
| 2025 | 14,409.5 | 0.0 | 14,409.5 *(100%)* | 2,709.0 | **2,709.0** | +481.3 | **−2,227.7** |
| H1 2026 | 10,287.1 | 70.1 *(0.7%)* | 10,217.0 *(99.3%)* | 1,697.4 | **1,685.8** | +323.3 | **−1,362.5** |

**THE RULING IS APPLIED AND IT DOES NOT MOVE THE NUMBER, WHICH IS ITSELF THE FINDING.** Four-year
(c) falls from **$7,096.4m to $6,987.7m — a difference of $108.7m, 1.53%** — and the shortfall
against $358.8m of cumulative earnings goes from $6,737.6m to **$6,628.9m**. The four-year mean
"owner earnings" moves from **−$1,684.4m to −$1,657.2m**; the three-year mean from −$1,424.6m to
**−$1,421.6m**. **SoFi's balance-sheet growth is 95–100% ORGANIC in every year of the window,
which is the exact opposite of ACNB's case, where $877,450 thousand arrived on a single day and
was paid for with $83,649 thousand of issued stock.** ACNB's ruling was written to stop (c)
reporting a stock-funded purchase as a loss of earning power; **at SoFi there is no purchase to
strip, so the $6.6 billion shortfall is what it appears to be: capital consumed by growing the
lending business itself.** *(This is the useful outcome of a ruling — applied, tested, and found
not to bind. It should be adopted for banks generally on ACNB's evidence, not on this run's.)*

## 3. ACNB'S RULING TWO, APPLIED: THE FDIC CALL REPORT ROW — AND IT REACHES THE PRIVATE BANKS THE CCB RUN SAID IT COULD NOT

ACNB's ruling: *"the competitor row for a bank should be built from the FDIC Call Report FIRST …
which is the only instrument that can see the private and mutual banks an SEC row cannot."*
**It was not built before this addendum, and that was a real defect in this run.** It is built
now, from the issuing authority — `banks.data.fdic.gov/api/financials`, REPDTE **2026-06-30**,
pulled 2026-09-19 — and saved to
`Test Runs/_research 2026-09-19 SOFI/fdic_row.txt`. **SoFi Bank, National Association is FDIC
CERT 26881, Salt Lake City, Utah.**

| bank (FDIC CERT) | assets $k | equity $k | NIM % | interest expense ÷ earning assets % | efficiency % | **ROE %** | pre-tax ROA % | net charge-offs % | **noninterest-bearing deposits %** | uninsured deposits % |
|---|---|---|---|---|---|---|---|---|---|---|
| **SoFi Bank, N.A. (26881)** | **56,821,411** | **7,277,956** | **6.07** | **2.64** | **67.20** | **15.41** | **2.66** | **0.08** | **0.30** | **5.01** |
| Ally Bank (57803) | 188,184,000 | 15,542,000 | 4.14 | 3.17 | 48.96 | 14.53 | 1.55 | 1.15 | 0.15 | 10.37 |
| Synchrony Bank (27314) | 115,217,000 | 14,860,000 | 12.91 | 3.35 | **36.71** | **22.07** | 3.75 | 5.39 | 0.52 | 11.92 |
| Pathward, N.A. (30776) | 7,313,151 | 882,564 | 7.41 | **0.17** | 57.97 | 23.28 | 3.27 | 0.86 | **95.87** | 12.74 |
| Coastal Community Bank (34403) | 5,452,231 | 467,455 | 7.02 | 2.30 | 68.22 | **−11.91** | −1.49 | 4.96 | 12.51 | 27.45 |
| ACNB Bank (7506) | 3,303,705 | 407,393 | 4.55 | 1.27 | 50.54 | 14.53 | 2.27 | 0.01 | 23.54 | 22.40 |
| **WebBank (34404) — PRIVATE** | 2,861,274 | 478,586 | **15.79** | 2.93 | 63.14 | **28.37** | **6.33** | 0.43 | 6.31 | 13.87 |
| **Column N.A. (58224) — PRIVATE** | 1,768,904 | 174,821 | 8.63 | 3.29 | 38.91 | **73.35** | **11.62** | −0.29 | 28.03 | 86.09 |

**FOUR THINGS, AND THE FIRST IS THE STRONGEST FACT AGAINST THIS RUN'S VERDICT.**

**(a) SoFi BANK is a good bank, and the consolidated shareholder does not get its return.**
The bank's own ROE series from the issuing authority is **10.47% (2022) / 15.36% (2023) / 12.14%
(2024) / 14.17% (2025) / 15.41% (H1 2026 annualised)**, with pre-tax ROA of 2.35–2.73% throughout
— **better than Ally (14.53%, 1.55%) and better than ACNB (14.53%, 2.27%)**, and this run's own
Q2 and Q3 sections said nothing about it because they measured the **holding company**, which is
the right unit for a shareholder and the wrong unit for judging the bank. **The arithmetic of the
gap, which is the honest way to hold both facts at once: SoFi Bank holds $7,277,956 thousand of
equity against the group's $11,076,227 thousand, so $3,798,271 thousand — 34.3% of the
shareholder's capital — sits OUTSIDE the bank. The bank's 15.41% on its own equity is about
$1,122 million a year; the group reported $646.6 million annualised in H1 2026. The difference,
roughly $475 million a year, is the non-bank perimeter (Galileo, Technisys, the brokerage, crypto)
plus the capital parked at the holding company earning less than the bank does.** **[E2-56]** is
the governing rule and it runs in the direction this run had not tested: *"Their marvelous core
businesses … **camouflage repeated failures in capital allocation elsewhere**"* — the Pro-Am
effect. **Here the camouflage runs the other way: the consolidated number HIDES a good bank
rather than a bad one, and [E2-56]'s instruction — judge retention segment by segment, never on
the blended return — cuts both ways and is applied in both directions here.** A reader who wants
to buy SoFi Bank and not SoFi Technologies has a case, and it cannot be bought.

**(b) THE DEPOSIT FRANCHISE SoFi BOUGHT WAS DESTROYED BY THE GROWTH, and the FDIC series says it
in one column.** This is the finding the SEC filings could not produce, because the FDIC carries
the predecessor's own balance sheet under the same CERT:

| REPDTE | name on the charter | assets $k | **noninterest-bearing deposits, % of deposits** | efficiency % |
|---|---|---|---|---|
| 2021-12-31 | **GOLDEN PACIFIC BANK NA** | 174,662 | **47.01%** | 83.03 |
| 2022-03-31 | SOFI BANK NATIONAL ASSN | 2,038,881 | 14.01% | 101.38 |
| 2022-12-31 | SOFI BANK NATIONAL ASSN | 9,123,708 | 1.26% | 81.13 |
| 2023-12-31 | SOFI BANK NATIONAL ASSN | 24,063,364 | 0.31% | 68.46 |
| 2024-12-31 | SOFI BANK NATIONAL ASSN | 31,087,762 | 0.48% | 68.63 |
| 2025-12-31 | SOFI BANK NATIONAL ASSN | 46,568,135 | 0.34% | 68.09 |
| 2026-06-30 | SOFI BANK NATIONAL ASSN | 56,821,411 | **0.30%** | 67.20 |

**SoFi paid about $22 million for a charter whose deposits were 47% free, and grew the balance
sheet 325-fold in four and a half years while diluting the free money to three-tenths of one per
cent.** **[E4-32]** — *direction outranks existence*, the moat widened every year being *"the
primary criterion of a great business"* — is answered here by a six-point series from the issuing
authority rather than by a single snapshot, and **the direction is down for every one of the four
and a half years.** The Q2 verdict above rested on the 0.28% figure from the 10-Q; **the FDIC
independently confirms it at 0.30% at the bank level and adds the history that makes it a trend
rather than a fact.** *(And note the second column: the efficiency ratio has sat at 67–69% for
four years while assets grew six-fold. There are no scale economies in the series, which is the
"Financial Services Productivity Loop" claim tested at the bank level and not found.)*

**(c) THE PRIVATE SPONSOR BANKS THE CCB RUN RECORDED AS UNREACHABLE ARE REACHABLE.** That run,
hours earlier, wrote: *"the largest sponsor banks in this industry **do not file** … Cross River
Bank, WebBank …, Column N.A., Lead Bank, Evolve Bank & Trust, Sutton Bank, Celtic Bank and Thread
Bank are private and publish no 10-K … **So the single most important competitor comparison in
this industry cannot be made from SEC filings at all.** Call Report data exists at the FFIEC but
is not an SEC filing and was not pulled." **It can be made, just not from SEC filings.**
**WebBank — named in Prosper's 10-K as Coastal's competing sponsor — earns a 28.37% ROE on a
15.79% net interest margin with a 6.33% pre-tax ROA. Column N.A. earns 73.35% on equity with
86.09% of its deposits uninsured.** Both are in the table above, from the issuing authority, at
2026-06-30. **This is a finding owed back to the CCB file and it is recorded here rather than
written into that run's history:** its Q2 verdict does not change — it rested on Dave's and
Prosper's own filings, not on the missing peers — but its stated *limit* was too strong, and the
correct form is *"cannot be made from SEC filings; can be made from the FDIC."* **ACNB found the
instrument three hours after CCB declared it out of reach. Two of the eight names CCB listed are
now in a row.** *(Cross River, Lead, Evolve, Sutton, Celtic and Thread were not pulled here and
remain available on the same endpoint by name search; that is a work order, not a limit.)*

**(d) ONE NUMBER IN THIS TABLE IS A TRAP AND MUST BE FLAGGED, BECAUSE THE ROW INVITES THE ERROR.**
**SoFi Bank's FDIC net charge-off rate is 0.08%, against Synchrony's 5.39% and Coastal's 4.96%.
That comparison is meaningless and must not be made.** SoFi elects the fair value option on
$46.60 billion of its $47.93 billion of loans, so credit losses are recognised inside the mark
and never appear as a charge-off; the Call Report's charge-off line therefore measures only the
$1.28 billion carried at amortized cost. The company's own MD&A gives the real figure —
**a personal-loan annualised charge-off rate of 2.62% in Q2 2026** — and even that is flattered by
**$359.9 million of delinquent-loan sales during 2025**, which remove loans from the book before
they charge off. **A reader who ranked this row on the NCO column would conclude that SoFi runs
the cleanest consumer book in America. It is the accounting election, not the credit.** Recorded
because the FDIC row is now a standing instrument for this project and this is the first trap it
sets.

## 4. WHAT THIS ADDS TO THE FRAMEWORK GAPS ABOVE

- **Gap 2 (the evidence ladder) is now specific and fixable rather than a complaint.** The
  missing rung is **the prudential regulator's own public data**, and for a US bank it has a
  concrete address: `banks.data.fdic.gov/api` for the Call Report (bank-level, covers private and
  mutual institutions, and carries the *predecessor's* balance sheet under a retained CERT), plus
  the OCC and Federal Reserve **enforcement** registers for the supervisory record, which remain
  unpulled. **Three banks have now hit it. ACNB built the Call Report harness; this run reused it
  in twenty minutes; it belongs in `tools/`.** *(A minimal helper would take a bank name or CERT
  and return the row above. It computes nothing the filer does not publish and it removes a real
  step, so it is inside operator rule 8's test.)*
- **A NEW gap, and it is the sharpest thing in this addendum: the framework has no rule for a
  BANK HELD INSIDE A HOLDING COMPANY THAT ALSO OWNS SOMETHING ELSE.** **[E2-56]** says judge
  retention segment by segment and never on the blended return, and **[E2-43]** says pick the
  denominator by the question asked. **Neither tells a run whether to judge a bank holding
  company on the BANK's return on the bank's equity or the GROUP's return on the shareholder's
  equity, and at SoFi those numbers are 15.41% and 6.27% — more than two to one.** Both are
  right; they answer different questions; and a run that reports only one of them is
  incomplete. **The candidate rule, offered and not adopted: report BOTH, name the capital that
  sits outside the bank in dollars and as a percentage of consolidated equity, and let the
  difference be the finding.** SoFi's is **$3,798,271 thousand, 34.3%**. *(This would have
  changed nothing at Coastal, whose holding company is essentially the bank, and nothing at
  ACNB for the same reason. It bites on SoFi, and it will bite hard on JPM and TFC.)*
- **Gap 5 stands unchanged and the FDIC row confirms why:** the Call Report's charge-off column
  cannot see a fair-value lender's losses either, so the **by-vintage model backtest** remains
  the missing artifact and the securitization trusts' Form 10-D and ABS-EE remain the place to
  find it.

## 5. WHAT DOES NOT CHANGE

**Q1 stays IN. Q2 stays OUT. Q3 and Q4 stay UNRESEARCHED and not governing. Q5 did not open.**
The FDIC row **strengthens** the Q2 verdict on the deposit leg (a four-and-a-half-year series
replacing a snapshot, and the destruction of a 47%-free deposit base) and leaves the two legs that
actually decided it — Chime's in-housing of Galileo and Dave's written fee cut — untouched. The
bank-level ROE of 15.41% is recorded as **the strongest single fact against the verdict found
anywhere in this run, stronger than the balance-sheet case stated at Q4**, and it does not reverse
it: **[E5-42]** keeps the two judgments separate — business quality is *"the capital actually
needed in the business"*, and what the buyer gets *"depends on how much we pay for that in the
end"*. **The buyer at $16.96 cannot buy SoFi Bank. He buys a holding company that earns 6.27% on
his money while a third of it sits outside the bank, and the Q5 computation above — 3.69% pre-tax
on the best run-rate, below the 5.34% sovereign — prices exactly that.**
