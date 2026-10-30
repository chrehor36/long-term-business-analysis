# Company Run — Truist Financial Corporation (TFC) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**THE FOURTH BANK THIS PROJECT HAS RUN** — after CCB (Coastal Financial, Q2 OUT), ACNB
(all four business gates IN, Q5 OUT on price) and SOFI (Q2 OUT), all on 2026-09-19. A
JPMorgan run is in flight in parallel and was not waited for. **CIK 0000092230**, found by
`tools/sources.py:cik_for('TFC')`, which returns `('0000092230', 'TRUIST FINANCIAL CORP')`.
WAVE 6, run under the operator ruling of 2026-09-19 that the five banks are run.

**And the same tool flagged the fact this whole run turns on, before a filing was opened.**
`tools/sources.py:name_change_note('0000092230')` returns: *"NAME CHANGE inside the data
window: was 'BB&T CORP' until 2019-12-06. Possibly a reverse merger, de-SPAC, spin or merger
whose predecessor's figures sit under this CIK … CHECK THAT MULTI-YEAR FIGURES ARE ONE
COMPANY [NEGG, 2026-09-13]."* It is a real perimeter event, and it is only the first of five.
The **CNR rule** therefore governs every mean in this file: **no multi-year mean crosses a
perimeter event unless it is rebuilt on one perimeter**, and the clean-year count is stated
at Q4 before any owner-earnings figure is written.

**HOW A BANK IS RUN HERE.** Five corpus rules, taken from `Screens/WATCHLIST RUN QUEUE.md`'s
**HOW A BANK IS RUN, FROM THE CORPUS** and from the construction the three prior bank runs
adopted:

1. **Q3 is the deciding gate, not an overlay** — **[E3-29]**: *"Because leverage of 20:1
   magnifies the effects of managerial strengths and weaknesses, we have no interest in
   purchasing shares of a poorly-managed bank at a 'cheap' price. Instead, our only interest
   is in buying into well-managed banks at fair prices."* The one place in the framework
   where cheapness is ruled out as a remedy.
2. **The named failure mode is conformity** — **[E3-02]**, *"the tendency of executives to
   mindlessly imitate the behavior of their peers, no matter how foolish it may be to do so."*
3. **Reserves are where dishonesty hides** — **[E2-50]**, *"where 'earnings' can be created by
   the stroke of a pen, the dishonest will gather"* — so the reserving record is judged against
   subsequent charge-offs, and the candor benchmark **[E2-67]** is looked for.
4. **Survival is a quantified stress, not a ratio** — **[E3-24]**, the corpus's own worked bank
   example, run against **this** bank's own loan book and stated beside the bank's own
   published stress result. **No leverage ceiling**: the old 10:1 rule was deleted
   (`Framework/INVENTIONS - deleted and why.md`).
5. **Owner earnings by the ordinary construction does not work for a bank.** The run states
   how it measures return on equity capital **[E2-01]** and confesses the convention
   (PRIME RULE 3). **CCB's construction — (c) = Δassets × the Tier 1 leverage ratio — is
   adopted, with ACNB's organic/acquired split**, and the SOFI fold's standing note is
   recorded: it has now passed three independent tests and should be given a ledger row or
   refused rather than re-invented a fourth time.

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
- rate **5.34 %** · date **2026-09-18** · source **US Treasury daily par yield curve,
  30-year (the issuing authority)**, struck fresh for this run by
  `tools/sources.py:sovereign('USD')`, which returned
  `(5.34, '09/18/2026', 'US Treasury daily par yield curve')`. FRED DGS30 is the fallback
  and was not used (CLAUDE.md, corrected 2026-09-02).
- **FX: none needed.** Truist is incorporated in North Carolina, files 10-Ks, earns
  substantially all of its income in USD and is quoted in USD. Quote currency and earnings
  currency are the same.
- **Price: US$48.56, close of 2026-09-18**, from `tools/sources.py:price('TFC')` —
  **AGGREGATOR, flagged, live quote only** per operator rule 5.
- **Share count: 1,221,626,188**, from the **cover of the Q2 2026 Form 10-Q, accession
  `0000092230-26-000099`, filed 2026-07-31**, verbatim: *"At June 30, 2026, 1,221,626,188
  shares of the registrant's common stock, $5 par value, were outstanding."*
  - **Issued-versus-outstanding check, run because the HBB / SOUN / BIRD notes of 2026-09-19
    made the per-class cover a standing hypothesis.** Truist has **one class** of common
    stock, $5 par value, and `dei:EntityCommonStockSharesOutstanding` is tagged **once,
    undimensioned**, so neither the HBB per-class layer nor the SOUN shell layer arises.
    **Issued equals outstanding by construction, and the filing says why:** *"In accordance
    with North Carolina law, repurchased shares cannot be held as treasury stock but revert
    to the status of authorized and unissued shares upon repurchase"* (FY2025 10-K, Share
    Repurchases). The arithmetic confirms it — the filed balance sheet carries **common
    stock, $5 par value, $6,108 million**, and $6,108M ÷ $5 = **1,221.6 million shares**,
    the cover figure. There is no treasury-stock line anywhere on the balance sheet.
    **Preferred is separate and is NOT in the count:** 196 thousand preferred shares
    outstanding of 5,000 thousand authorised, carried at **$5,411 million**, five series
    listed separately on the NYSE. The preferred is deducted before every per-common figure
    in this file.
  - **Post-cover issuance check — and here the direction of the error matters, so it is
    stated rather than ignored.** Truist is **retiring** stock, not issuing it: the 10-Q
    states *"For the six months ended June 30, 2026, the Company repurchased $2.4 billion of
    common stock, including excise tax, which represented 46.6 million shares"*, and
    *"At June 30, 2026, Truist had remaining authorization to repurchase up to $7.7 billion
    of common stock"* against a **2026 target of $5 billion** restated in the 8-K of
    2026-09-15. The count fell from 1,262,470 thousand (2025-12-31) to 1,221,626 thousand
    (2026-06-30), so **the true count on 2026-09-19 is almost certainly LOWER than the one
    used**, no Q3 2026 count has been published, and the effect of using the cover figure is
    to **overstate the market capitalisation and understate every yield** — the conservative
    direction, which is why the cover figure is used unadjusted rather than estimated
    forward. The one issuance on the record in the window is **preferred**: $495 million of
    Series S non-cumulative perpetual preferred at a stated 6.25% in H1 2026, which does not
    touch the common count and is recorded at Q3 as a capital-allocation fact.
  - `tools/sources.py:split_factor_after('TFC', '2026-06-30')` returns **1.0**, and so does
    the same call at the merger date 2019-12-06, so the house rule
    `cap = close(anchor) × shares(measurement) × splits AFTER measurement` needs no factor.
  - `tools/sources.py:deal_filings('0000092230')` returns `([], [], '2026-02-24')` — **no
    live deal form on this registrant**, so the quote is not a merger spread (the ROKU
    defect of 2026-09-12). *It does NOT mean there is no live transaction: Truist is the
    SELLER in one signed on 2026-09-15, which appears as an Item 7.01 furnished slide and
    not as a deal form. The tool reads the registrant's own merger forms; a disposal by a
    $556 billion bank of a $5.5 billion loan portfolio is not one. Recorded as a limit of
    the check, not a failure of it.*
- **Market capitalisation: 1,221,626,188 × $48.56 = US$59,322.2 million.**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.:
  - **FY2025 Form 10-K, period 2025-12-31, filed 2026-02-24, accession
    `0000092230-26-000030`** (primary document `tfc-20251231.htm`) — the governing document.
  - **Q2 2026 Form 10-Q, period 2026-06-30, filed 2026-07-31, accession
    `0000092230-26-000099`** — the current balance sheet and capital position.
  - Also read in full: FY2024 10-K `0000092230-25-000020`; FY2023 10-K
    `0000092230-24-000010`; FY2022 10-K `0000092230-23-000034`; FY2021 10-K
    `0000092230-22-000008`; FY2020 10-K `0000092230-21-000032`; Q1 2026 10-Q
    `0000092230-26-000062`; DEF 14A of 2026-03-16 `0001193125-26-107144`; DEF 14A of
    2025-03-17 `0001193125-25-055156`; DEF 14A of 2021-03-15 `0001193125-21-081387` (the
    first full merger year's pay record).
  - **And the furnished 8-K exhibits, which the CGNX ruling of 2026-09-07 makes mandatory
    before scoring [E4-29] and [E4-22]'s third flag** — here they carry three facts the
    annual report does not: the Q2 2026, Q1 2026 and Q4 2025 EX-99.1 earnings releases with
    their EX-99.2 Quarterly Performance Summaries and EX-99.3 slide decks (accessions
    `0000092230-26-000096`, `0000092230-26-000039`, `0000092230-26-000023`); the **8-K of
    2026-09-15, accession `0000092230-26-000105`**, whose single furnished slide announces a
    **signed sale of substantially all of Regional Acceptance Corporation, $5.5 billion of
    auto loans**; the **8-K of 2026-06-15, accession `0001193125-26-270320`**, which changes
    the chief executive; the **8-K of 2026-01-12, accession `0000092230-26-000006`**, whose
    EX-99.1 retrospectively recasts seven quarters of the income statement onto a new line
    presentation; and the **8-K of 2024-05-10, accession `0000092230-24-000029`**, which
    recast the FY2023 10-K for the insurance disposal.
- **figure cross-checked against the filed statement:** equity recomputed from **A − L** per
  **[E5-32]** (*"the floating plug"* — audited does not mean true). The Q2 2026 filed
  balance sheet gives **total assets $556,023 million** less **total liabilities $491,928
  million = $64,095 million**, which is exactly the filed **total shareholders' equity of
  $64,095 million**. Second cross-check, on the figure that actually drives this run's Q3:
  the FY2025 10-K's Table 38 builds ROTCE from **average common shareholders' equity of
  $58,902 million** less average intangibles; the filed period-end common equity
  ($65,189M total equity − $4,916M preferred = **$60,273M**) and the prior period-end
  ($63,679M − $5,907M = **$57,772M**) average to **$59,023M**, within 0.2% of the filer's
  daily average, so the denominator is confirmed independently of the filer's arithmetic.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Unit economics in my own words, no management language

Truist is **the sixth-largest bank in the United States by assets, and it is a spread
business with a fee business bolted to the side of it.** Strip the language out and there
are exactly two engines.

**Engine one, and it is nine-tenths of the machine: borrow at 1.78% and lend at 5.96%.**
Truist holds **$400.4 billion of deposits** (2025-12-31), of which **$105.1 billion pay
nothing at all** — a quarter of the funding is free — and the whole book cost **1.78%** on
average in 2025. Against that it holds **$328.6 billion of loans** yielding **5.96%** and
**$112.2 billion of securities** yielding **3.13%**. The difference, after the
taxable-equivalent adjustment, is **$14,619 million of net interest income**, a **3.03% net
interest margin** on average earning assets. That one line is **71% of revenue**.

**Engine two: sell services to the same customers for a fee.** $5,896 million of
noninterest income in 2025 — investment banking and trading, wealth management, card and
treasury management, mortgage, service charges. It uses almost no balance sheet and it is
the half that is growing.

**Then subtract the two costs that make a bank a bank.** Credit: **$1,894 million of
provision** in 2025 against **$1,705 million of actual net charge-offs, 0.54% of average
loans**. And people and premises: **$12,076 million of noninterest expense**, of which
**$6,506 million is personnel** — 1,927 branches and roughly 37,000 people. What is left is
**$6,349 million of pre-tax income**, **$5,307 million of net income**, **$4,974 million
after the preferred dividend**, **$3.82 a diluted share**.

**The whole business in one sentence:** *Truist is paid the difference between what money
costs it and what money earns for it, on a balance sheet levered about 8.7 times against
common equity, and it keeps roughly 31 cents of every revenue dollar after credit losses
and the cost of 1,927 branches.*

### Where the money actually comes from, by segment — and the answer is not the branches

| segment (FY2025, net income from continuing operations) | $M | share |
|---|---|---|
| **Wholesale Banking** | **4,102** | **77.3%** |
| **Consumer and Small Business Banking** | **2,529** | **47.7%** |
| Other, Treasury & Corporate | (1,324) | (24.9%) |
| **Truist Financial Corporation** | **5,307** | 100% |

*FY2025 10-K, Table 10, accession `0000092230-26-000030`.* The two operating segments
together earn $6,631 million and the corporate centre loses $1,324 million of it. **The
larger earner is the commercial and corporate bank, not the branch network** — and this
matters at Q2, because a branch deposit franchise and a corporate lending book are not the
same competitive animal.

### The scarce input this business controls

**A deposit base that is geographically concentrated in the fastest-growing states in the
country, and 26% of which is free.** The filer publishes the position itself:

| state | % of Truist's deposits | deposit market share rank | branches |
|---|---|---|---|
| Florida | 22% | **4th** | 441 |
| Georgia | 21% | **1st** | 202 |
| Virginia | 14% | 3rd | 259 |
| North Carolina | 13% | 2nd | 276 |
| Maryland | 7% | 3rd | 138 |
| Tennessee | 5% | 5th | 98 |

*FY2025 10-K, Table 1; FDIC data as of 2025-06-30.* **Seventy per cent of the deposits sit
in five south-eastern states, and Truist is number one in exactly one of them.** That is
the scarce input and it is also the Q2 problem, and it is dealt with there rather than
here.

The second scarce input is regulatory and it is real: **a Category III bank holding company
charter with a $556 billion balance sheet**. It cannot be replicated by entry — the last
bank to reach this size did it by merging two large banks, which is precisely what Truist
is. But a scarce *permission* is not the same thing as a scarce *property*, and the CCB run
of this morning made that distinction on the same ground.

### Will the fundamentals look broadly the same in ten years?

**Yes for the machine, and that is the honest answer to [E3-31]'s test of "relatively simple
and stable in character."** Taking deposits in Charlotte and Atlanta and lending against
commercial and industrial credit, houses and cars is the same business BB&T ran in 1872 and
the same business it will run in 2036. Rates will move; the spread structure will not.

**No for the perimeter, and the filings say so in five separate events.** These are
established with dates at Q4 and drive the clean-year count, but they belong in the Q1
comprehension test too, because a reader who takes any five-year series off this registrant
at face value is reading five different companies:

| # | event | date, from the filings |
|---|---|---|
| 1 | **BB&T and SunTrust merge**; registrant renamed | merger closed **2019-12-06** (the CIK's own former-name record: *"BB&T CORP … to 2019-12-06"*) |
| 2 | **20% of Truist Insurance Holdings sold** to a Stone Point group for **$1.9 billion**, proceeds net of tax taken straight to equity | **2023-04-03** |
| 3 | **Goodwill impairment of $6,078 million** | Q4 **2023** |
| 4 | **The remaining stake in TIH sold** at an implied enterprise value of **$15.5 billion**; the whole Insurance Holdings segment becomes discontinued operations and **every prior period is recast** | agreement **2024-02-20**, completed **2024-05-06**, recast published in the 8-K of **2024-05-10** |
| 5 | **$27.7 billion of AFS securities sold** at a **$6,651 million pre-tax / $5.1 billion after-tax loss** | Q2 **2024** |
| 6 | **Income-statement line presentation changed and seven quarters recast** | effective **2025-12-31**, published 8-K of **2026-01-12** |
| 7 | **Regional Acceptance Corporation — $5.5 billion of auto loans, substantially all of its assets — agreed to be sold**, with an explicit plan to *"[r]eposition certain AFS securities to fully offset capital created from RAC sale"* | signed and furnished **2026-09-15**, four days before this run; closing *"anticipated in late 3Q26 or early 4Q26"* |

Seven, not five. **The brief asked for every perimeter event with dates, and there are
seven.** The clean-year count is at Q4.

### The verdict, and why it is IN

**[E3-31]** asks whether the mechanism is legible and whether it is simple and stable.
The mechanism is a spread on deposits plus fees, it is stated above from the filed
statements without using the filer's own framing, and it is arithmetically checkable at
every line. Nothing in it requires me to model a technology, a commodity price or a
counterparty's balance sheet — which is what closed Q1 or Q2 on ACVA, BIRD and CCB.

What is *not* stable is the **perimeter**, and that is a Q4 finding about the reliability of
multi-year figures rather than a Q1 failure of comprehension. **[E4-46]** scopes UNRESEARCHED
to documents rather than competence, and here every document exists and has been read: the
recast 8-K, the discontinued-operations note, the goodwill-impairment note, the securities
loss, the new CEO's offer letter and the RAC slide. **I can state how this makes money, and
I can state what has been done to the company since 2019. Both are on the record.**

- **VERDICT: [x] IN**
