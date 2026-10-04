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

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The three criteria, and the second one decides the file.**

- **Needed or desired [x]** — not in question. A place to keep money, a payroll account, a
  revolving credit facility and a mortgage are all needed, and 1,927 branches in fourteen
  states and DC are used.
- **No close substitute — NO, and the filer says so in its own words, at length, and then the
  numbers say it again.** This is the finding the run turns on. **[E3-03] criterion 2 for a
  bank starts from the position that a deposit is a commodity unless the filings show
  otherwise**, and Truist's own Item 1, Competition, is the opposite of a showing:
  > *"The financial services industry is intensely competitive and constantly evolving. …
  > Truist competes actively with national, regional, and local financial services providers,
  > including banks, thrifts, credit unions, investment advisers, asset managers, securities
  > brokers and dealers, private-equity funds, hedge funds, mortgage-banking companies,
  > finance companies, limited-purpose banks, and financial technology companies. …
  > **Many of our competitors have substantial positions nationally or in the markets in which
  > we operate. Some also have greater scale, financial and operational resources, investment
  > capacity, product and service offerings, and brand recognition.** … Competition affects
  > every aspect of our business, including **product and service offerings, rates, pricing and
  > fees, credit limits, and client service.** … **We expect that competition will only intensify
  > in the future.**"* — FY2025 10-K, accession `0000092230-26-000030`

  And the market-share table is the arithmetic of the same sentence. **Truist holds the number
  one deposit share in exactly one state, Georgia, which is 21% of its deposits.** In Florida,
  its largest market at 22% of deposits, it is **fourth**. It is 12th in Pennsylvania, 18th in
  Texas, 24th in New Jersey. **[E2-53]**'s dominance class — *"Once dominant, the newspaper
  itself, not the marketplace, determines just how good or how bad the paper will be. Good or
  bad, it will prosper"* — describes a position Truist does not hold in thirteen of its
  fourteen states.
- **Not price-regulated [x] — but the tick is recorded with [E2-59] against it, exactly as the
  ACNB run did.** Deposit and loan rates are not administered. But the reason $105.1 billion of
  Truist's deposits can sit at zero interest without a run is **federal deposit insurance**, and
  **[E2-59]** is precise about what that is worth: administered pricing *"could legally price
  their way to profitability even in the face of substantial over-capacity"*, but **the moat
  belongs to the regime**, and *"That day is gone"* is how it ends. What Truist has to prove is
  that it earns **more than the regime hands every insured bank in America.** The rest of this
  section is that test, and Truist fails it.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**

**No to the first, and that is a point in Truist's favour — stated plainly because it is
true.** A branch network and a 154-year-old deposit relationship must be **defended** (personnel
expense of $6,848 million and 1,927 branches), but a lapse in that spending **narrows** the
advantage rather than replacing its basis. This is Coca-Cola's advertising, not Mitsui's Rhodes
Ridge. **[E4-04]**'s excluded class does not catch a deposit franchise. The problem at Truist is
not that the moat must be rebuilt; it is that the measurements below do not find one.

**And on [E4-23] there IS a defect, and it is unusually sharp because of its timing.** Truist's
chief executive changed **eighteen days before this run**: the 8-K of 2026-06-15 (accession
`0001193125-26-270320`) records that William H. Rogers, Jr. *"will retire as Chief Executive
Officer … effective on September 1, 2026"* and that **Michael P. Lyons** was appointed CEO and
President on that date. Every operating number in this file was produced by the previous
management. **The 8-K of 2026-09-15 then says, on the incoming CEO's fifteenth day, that a
"broader strategic review is ongoing."** Under **[E4-23]** — *"if a business requires a superstar
to produce great results, the business itself cannot be deemed great"* — the question is whether
the case for this business rests on the new man. **It does, and that is recorded HERE at Q2 as a
moat defect, not at Q3 as a strength**, because the honest statement of the bull case for Truist
in September 2026 is *"a new chief executive with a PNC record will fix the returns"*, and that
is a statement about a person.

### The primary moat metric, filing-sourced, and its trend — and it is the physical series

**[E4-55]**: where units exist, monitor units, because *"dollar revenue flattered by pricing is
how a shrinking franchise hides."* Truist has two unit series and both point the same way.

| the physical series, from the filings | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **banking offices / branches** | **2,781** | 2,517 | 2,123 | 2,001 | 1,928 | **1,927** |
| **total deposits, $M** | 381,077 | **416,488** | 413,495 | 395,865 | 390,524 | **400,398** |
| **noninterest-bearing deposits, $M** | 114,580 | **145,892** | 135,742 | — | 107,451 | **105,092** |
| noninterest-bearing share of deposits | 30.1% | **35.0%** | 32.8% | — | 27.5% | **26.2%** |
| teammates (total) | — | **52,641** | — | — | — | **38,711** |

*Sources: the "offices"/"branches" sentence in Item 1 of each of the six 10-Ks; Table 26 of the
FY2025 10-K and the equivalent deposit tables in FY2021-FY2024; Table 2/3 Teammate Summary.*

**Read it in one line: the branch count is down 30.7% in five years, total deposits are down
3.9% from the 2021 peak, and the deposits that cost nothing — the only part of a bank's funding
that is genuinely a franchise asset — are down $40.8 billion, or 28.0%.** Seventy per cent of
those deposits sit in Florida, Georgia, Virginia, North Carolina and Maryland, five of the
fastest-growing states in the United States, across a period in which nominal GDP grew by about
a quarter. **[E4-32]**, direction outranks existence: the direction is down.

**The honest qualification, because [E3-61] requires the row's limit to be stated and because
the analyst's own incentive runs the other way [E4-26].** Deposit shrinkage 2021→2025 is not
Truist-specific. From the same companyfacts data: PNC −3.6%, KeyCorp −2.5%, Regions −5.7%,
Fifth Third +1.5% — every large regional that did not buy a bank shrank or stood still, while
the three that bought one grew (M&T +26.9% with People's United, Huntington +23.3%, Citizens
+18.8% with Investors Bancorp; US Bancorp +14.5% with Union Bank). **So the deposit series is an
industry fact, not a Truist fact, and it is recorded that way.** What is a Truist fact is what
the balance sheet earns, and that is the row.

### THE COMPETITOR ROW — required **[E3-28]**, and built TWICE

**ROW A — the eight large regional banks Truist actually competes with, one basis, five years,
computed by this session from each filer's own tagged annual statement values.**

The brief names PNC, US Bancorp, Fifth Third, KeyCorp, Regions and Citizens. **M&T and
Huntington are added, making eight peers, because they are the same size class and the same
business and their exclusion would leave the row without the two banks that grew** — Buffett
says eight **[E3-28]**, and eight is what was taken.

*Specification, stated once so the row is reproducible (`Test Runs/_research 2026-09-19 TFC/peers2.py`).
**ROTCE** = net income available to common ÷ the average of opening and closing (common equity −
goodwill − other intangibles), with **no** add-back of intangible amortisation and **no**
deferred-tax adjustment; **efficiency** = noninterest expense ÷ (net interest income +
noninterest income), not taxable-equivalent, nothing excluded; **cost of deposits** = interest
expense on deposits ÷ average TOTAL deposits, so every row includes the free money; **NII ÷
average assets** stands in for net interest margin because average EARNING assets is not a
tagged concept, and it is labelled a proxy rather than a margin. **The method is validated
against the subject's own filed figure**: this specification returns **12.28%** for Truist in
2025 against the **12.7%** Truist publishes in Table 38, and the 0.42-point gap is exactly the
$290M of intangible amortisation and the $416M deferred-tax adjustment the filer adds and this
run does not. The row is therefore comparable AND tied to the filing.*

| | ROTCE 2021 | 2022 | 2023 | 2024 | 2025 | **5-yr mean** | rank |
|---|---|---|---|---|---|---|---|
| **Truist (TFC)** | 17.61 | 19.74 | **−4.80** | 12.31 | **12.28** | **11.43** | **8 of 9** |
| Regions (RF) | 22.06 | 22.68 | 21.79 | 17.66 | 18.68 | **20.57** | 1 |
| US Bancorp (USB) | 18.72 | 18.65 | 18.59 | 18.58 | 19.30 | 19.44 | 2 |
| Fifth Third (FITB) | 16.61 | 18.24 | 19.98 | 17.57 | 17.31 | 17.94 | 3 |
| Huntington (HBAN) | 11.44 | 19.92 | 17.26 | 15.43 | 15.14 | 15.84 | 4 |
| M&T (MTB) | 16.24 | 14.46 | 17.04 | 14.24 | 15.04 | 15.40 | 5 |
| PNC | 12.08 | 14.35 | 13.68 | 13.14 | 14.12 | 13.47 | 6 |
| Citizens (CFG) | 15.86 | 14.24 | 10.93 | 9.87 | 11.36 | 12.45 | 7 |
| KeyCorp (KEY) | 19.43 | 17.29 | 9.45 | **−2.74** | 12.04 | 11.09 | 9 |

| | **net income available to common ÷ average assets** 2021 | 2022 | 2023 | 2024 | 2025 | **5-yr mean** | rank |
|---|---|---|---|---|---|---|---|
| **Truist (TFC)** | 1.149 | 1.081 | **−0.266** | 0.838 | **0.922** | **0.745** | **8 of 9** |
| Regions (RF) | 1.547 | 1.349 | 1.286 | 1.146 | 1.304 | **1.326** | 1 |
| M&T (MTB) | 1.194 | 1.063 | 1.289 | 1.176 | 1.280 | 1.200 | 2 |
| Fifth Third (FITB) | 1.279 | 1.113 | 1.048 | 1.008 | 1.112 | 1.112 | 3 |
| PNC | 1.057 | 1.024 | 0.916 | 0.980 | 1.160 | 1.027 | 4 |
| US Bancorp (USB) | 1.349 | 0.882 | 0.755 | 0.881 | 1.050 | 0.983 | 5 |
| Huntington (HBAN) | 0.776 | 1.191 | 0.976 | 0.915 | 0.972 | 0.966 | 6 |
| Citizens (CFG) | 1.187 | 0.944 | 0.665 | 0.624 | 0.761 | 0.836 | 7 |
| KeyCorp (KEY) | 1.412 | 0.957 | 0.436 | **−0.162** | 0.908 | 0.710 | 9 |

| 5-year means, one basis | **cost of total deposits** | rank | **efficiency ratio** | rank | **NII ÷ avg assets** | rank |
|---|---|---|---|---|---|---|
| **Truist (TFC)** | **1.14%** | **3** | **74.38%** | **9** | **2.61%** | **5** |
| Regions (RF) | 0.81% | 1 | 58.01% | 2 | 3.05% | 2 |
| PNC | 1.11% | 2 | 63.57% | 6 | 2.37% | 9 |
| Fifth Third (FITB) | 1.21% | 4 | 58.54% | 4 | 2.63% | 4 |
| KeyCorp (KEY) | 1.21% | 4 | 71.65% | 8 | 2.25% | 8 |
| Huntington (HBAN) | 1.23% | 6 | 63.25% | 5 | 2.83% | 3 |
| Citizens (CFG) | 1.24% | 7 | 64.15% | 7 | 2.66% | 6 |
| US Bancorp (USB) | 1.27% | 8 | 62.26% | 3 | 2.41% | 7 |
| M&T (MTB) | n/d — does not tag deposit interest separately | — | 58.45% | 1 | 3.18% | 1 |

**And the row is run a SECOND time on the three years that contain neither Truist's goodwill
impairment nor its securities repositioning (2021, 2022, 2025), because the CNR rule forbids a
mean that crosses a perimeter event without being rebuilt** — and because refusing to do this
would be the cheapest possible way to make the subject look bad:

| clean window 2021 + 2022 + 2025 | ROTCE | efficiency | cost of deposits | NII / assets |
|---|---|---|---|---|
| **Truist (TFC)** | **16.54** | **62.72** | **0.70** | **2.59** |
| Regions (RF) | 21.14 | 57.30 | 0.52 | 2.90 |
| US Bancorp (USB) | 20.01 | 60.35 | 0.80 | 2.34 |
| Fifth Third (FITB) | 17.38 | 57.86 | 0.68 | 2.59 |
| Huntington (HBAN) | 15.50 | 64.12 | 0.74 | 2.84 |
| M&T (MTB) | 15.25 | 59.57 | n/d | 3.05 |
| KeyCorp (KEY) | 16.25 | 61.57 | 0.73 | 2.40 |
| Citizens (CFG) | 13.82 | 62.26 | 0.76 | 2.65 |
| PNC | 13.52 | 63.31 | 0.68 | 2.32 |

**On the clean window Truist ranks 4th of 9 on ROTCE — and that ranking is worthless, because
two of its three clean years contain the insurance brokerage it no longer owns.** Truist
Insurance Holdings earned **$3,372 million of insurance income and $580 million pre-tax in
2023** and **$3,086 million and $640 million in 2022** (FY2024 10-K, Note 2, Discontinued
Operations), on almost no balance sheet. Strip a capital-light fee business out of a bank and
the return on tangible equity falls mechanically. **So the only Truist year in this table that
is both perimeter-clean and post-disposal is 2025, and in 2025 Truist ranks 8th of 9 on ROTCE
and 7th of 9 on return on assets.**

**ROW B — the FDIC Call Report, from the issuing authority, following the standing ruling the
ACNB run left for the banks still queued.**

That ruling said the bank competitor row *"should be built from the FDIC Call Report FIRST — all
insured institutions with an office in the footprint … the only instrument that can see the
private and mutual banks an SEC row cannot."* **For Truist the ruling behaves differently and
the difference is stated rather than glossed:** ACNB competes in nine counties where 56 insured
institutions operate and most are private or mutual, so the Call Report was the only way to see
the row at all. Truist Bank has 1,927 branches in fourteen states and DC, $548 billion of
assets, and the institutions that can take a multi-state corporate treasury relationship or a
$400 billion deposit book from it are all SEC registrants. **What the Call Report adds here is
not an invisible competitor. It is a second, independent measurement of the same nine banks, on
the regulator's own uniform definitions, which no filer can choose** — and it is worth having
precisely because Row A had to be specified by this session.

*Truist Bank is **CERT 9846**, Charlotte NC, $548,346 million of assets at 2026-06-30, resolved
by exact-name filter and verified against city and state.*

| FDIC Call Report, 2021-2025 means (and 2026-06-30 beside) | **cost of funding earning assets** | **net interest margin** | **efficiency ratio** | **pre-tax ROA** | **ROE** |
|---|---|---|---|---|---|
| **Truist Bank** | **1.341** (1.782) | **3.113** (3.141) | **59.116** (52.990) | **0.991** (1.350) | **7.028** (10.000) |
| Regions Bank | 0.881 (1.296) | 3.575 (3.718) | 54.740 (55.871) | 1.875 (1.847) | 13.860 (12.860) |
| Manufacturers and Traders Trust | 1.149 (1.546) | 3.603 (3.844) | 55.651 (53.570) | 1.638 (1.826) | 10.308 (10.700) |
| Fifth Third Bank NA | 1.309 (1.656) | 3.231 (3.764) | 55.558 (66.312) | 1.682 (1.242) | 12.598 (7.890) |
| Citizens Bank NA | 1.367 (1.681) | 3.084 (3.260) | 62.341 (60.288) | 1.173 (1.270) | 8.232 (8.500) |
| PNC Bank NA | 1.382 (1.720) | 2.731 (3.153) | 62.057 (59.227) | 1.325 (1.650) | 11.772 (12.590) |
| The Huntington National Bank | 1.388 (2.026) | 3.238 (3.500) | 57.990 (59.906) | 1.418 (1.326) | 11.776 (9.470) |
| KeyBank NA | 1.459 (1.697) | 2.633 (3.113) | 59.162 (54.781) | 1.119 (1.618) | 10.376 (12.540) |
| U.S. Bank NA | 1.463 (1.949) | 2.809 (2.868) | 58.939 (54.647) | 1.429 (1.527) | 12.486 (12.380) |
| **Truist's rank, 2021-2025 mean** | **4 of 9** | **5 of 9** | **7 of 9** | **9 of 9** | **9 of 9** |

**The regulator's own data says it harder than the holding-company data does. On the FDIC's
uniform definitions Truist Bank has the WORST five-year mean pre-tax return on assets and the
WORST five-year mean return on equity of the nine largest regional banks in the United
States** — 0.991% pre-tax ROA against Regions' 1.875%, and 7.03% ROE against Regions' 13.86%.
Its funding is 4th cheapest of nine and its margin is 5th of nine. **The inputs are average;
the output is last.**

### Where the return actually goes — because the row has to be explained, not just recited

The two halves of the arithmetic, from the 2025 figures:

1. **Truist is NOT under-levered and NOT badly funded.** Average assets ÷ average tangible
   common equity is **13.3×**, against PNC 12.2×, M&T 11.7×, Regions 14.3×, US Bancorp 18.4×.
   Cost of total deposits 1.78% in 2025 is **essentially identical to PNC's 1.73% and better
   than US Bancorp, KeyCorp, Huntington and Citizens.** Net interest income ÷ average assets of
   2.67% is **third of nine.** The spread engine works.
2. **What does not work is the conversion of that spread into a return, and $17,125 million of
   goodwill is the reason the two rows disagree.** Truist's intangibles at 2025-12-31 were
   **$18,416 million against common equity of $60,273 million — 30.6%**; tangible common equity
   was **$42,264 million**, and **tangible book value per share was $33.48 against a book value
   of $47.74**. ROTCE (12.7%) flatters; the Call Report's ROE on the bank's actual equity
   (8.93% in 2025, 7.03% five-year mean) does not. **Both are real: the goodwill is money that
   was paid, and the corpus's instruction under [E2-43] is to report the wedge separately and
   never hide it in book equity. The wedge is $18.4 billion, and $6.1 billion of it was already
   written off in 2023.**

### Untapped pricing power **[E3-33]** — and **[E2-58]**'s one exception, tested

**No, on both, and the filings decide it rather than my judgment.**

**[E5-28]** scopes the pricing-power class: *"If you name some business that has incredible
pricing power, you're talking about a business that's a monopoly or a near monopoly."* Truist is
one of nine banks of its size and one of roughly 4,400 insured institutions; it is first in
deposit share in one state. **[E4-37]**'s inverse metric — the agony over a price increase —
cannot even be observed as agony here, because **Truist does not set the price of its main
input.** The cost of deposits went 0.04% → 0.28% → 1.59% → 2.00% → 1.78% in five years: it
followed the federal funds rate up and back down. A business whose input price is set by the
Federal Open Market Committee and whose output price is competed by eight equals has no
untapped pricing power, and none is claimed.

**[E2-58]** is the governing doctrine for this class and it is exact: *"persistent over-capacity
without administered prices (or costs) equals poor profitability"*, with **one** exception —
*"a cost advantage that is both **wide and sustainable** … By definition such exceptions are
few."* **Truist's cost of funding earning assets is 4th of 9 on the regulator's numbers and its
cost of total deposits is 3rd of 8 on the filings' numbers. That is not a wide cost advantage;
it is the middle of the pack.** The exception fails, and the equation applies.

### **[E4-36]** — which of the four causes of extreme success is Truist's record?

**None of them, because there is no extreme success in the record to explain.** That is the
short answer and it is the honest one. The five-year mean return on tangible common equity is
11.43%, 8th of nine; the five-year mean return on assets is 0.745%, 8th of nine; the bank-level
pre-tax ROA and ROE are last of nine. **[E3-46]** asks the second question about the business
as a number — *"the best businesses, by definition, are going to be businesses that earn very
high returns on capital employed over time"* — and the answer here is a below-median return on
capital employed over a full cycle. What the record does contain is **scale achieved by merger**,
which is the [E4-36] category the corpus does not list because it is not a cause of extreme
success at all.

### **[E2-44]**, the two-characteristic test — both fail

- *Can it raise prices even when product demand is flat and capacity is not fully utilised?*
  **No.** Loan yield fell 38 basis points in 2025 as rates fell, and the FY2025 10-K attributes
  it to *"the impact of variable-rate loans repricing"* — the price is indexed to something
  Truist does not control.
- *Can it grow dollar volume with only minor additional investment of capital?* **No, and for a
  bank the answer is structurally no** — every dollar of assets must be matched with regulatory
  capital, which is exactly why this run's (c) convention at Q4 exists. Truist's own 8-K of
  2026-09-15 states the mechanism in reverse: selling $5.5 billion of loans *"[c]reates $945MM
  or 22 bps of CET1 capital."* Shrinking releases capital because growing consumes it.

### **[E2-45]**, the attacker's test — the shelf's one forward-looking moat test

With ample capital and skilled people, how would I compete with Truist? **The uncomfortable
answer is that eight companies are already doing it and three of them are doing it better with
less.** Regions Bank runs $157 billion of assets in overlapping south-eastern states and earns
**1.875% pre-tax on them against Truist's 0.991%** — 89% more return per dollar of balance
sheet, with a cheaper funding cost, from a bank one-third the size. M&T earns 1.638%. Fifth
Third earns 1.682%. The attack does not require capital I do not have or a technology I cannot
build; it requires operating a regional bank at the industry's median, which Truist does not do.
**A moat that three smaller rivals are already standing inside is not a moat.**

### Class and direction

- Class: **[ ] WIDE  [ ] NARROW  [x] NONE  [ ] PROVISIONAL.**
  *Not PROVISIONAL: every peer in both rows is either an SEC registrant whose 10-K was pulled or
  an insured institution whose Call Report was pulled from the FDIC, and both rows are complete.
  The one gap is M&T's cost of deposits, which it does not tag separately before 2025 — one cell
  of one metric in a nine-bank, five-year, six-metric table, and it does not move the verdict in
  either direction.*
  The **Georgia deposit book, taken alone, would be NARROW** — first share in the state, and
  $105 billion of free deposits system-wide is a real asset. But it is not separately reported,
  it is 21% of deposits, and the company as a whole is what is for sale.
- Direction: **NARROWING**, on every series that can be measured — branches 2,781 → 1,927, free
  deposits $145.9bn → $105.1bn, noninterest-bearing share 35.0% → 26.2%, total deposits below
  the 2021 peak, and the goodwill from the merger that created the company written down by
  $6,078 million four years after it closed.

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**

**OUT means the evidence is here and the business fails this question. It is permanent, and it
is about the BUSINESS, not the price** — so no price alert and no `PORTFOLIO.md` row follows (the
QLYS ruling, 2026-09-07). **The reversal condition, recorded in words instead:** this verdict
would have to be revisited if Truist's return on average assets reached the median of this
nine-bank row and **stayed there for three consecutive years** on the FDIC's own definitions
(the median 2021-2025 mean pre-tax ROA is Huntington's 1.418%, against Truist's 0.991%), **while**
the noninterest-bearing deposit share stopped falling. H1 2026's 1.350% pre-tax ROA is the first
year of such a run, and one year is not three.

**THE STRONGEST SINGLE FACT AGAINST THIS VERDICT, stated as [E4-51] requires — the bear case's
holders would accept my statement of the bull case, so here it is.** *Truist is getting better,
quickly, and the most recent data is the best data.* On the FDIC's own numbers Truist Bank's
efficiency ratio in the first half of 2026 is **52.990%, the BEST of all nine banks**, its
pre-tax ROA has risen 0.874% → 1.248% → 1.350% in six quarters, and its ROE 8.35% → 8.93% →
10.00%. Its own reported ROTCE went 13.3% (2024) → 12.7% (2025) → 13.8% (Q1 2026) → **15.4% (Q2
2026)**, and diluted EPS rose **37% year on year** in Q2 2026. Uninsured deposits at 43.4% are
the third lowest of the nine, and CRE is 7.2% of loans against an industry that is far more
exposed. **If the trajectory of the last six quarters continues for three years, this Q2 verdict
is wrong.** What it is not is evidence of a franchise: an improvement from last place toward the
middle, delivered by a management that has just been replaced, is a statement about operating
execution, and **[E2-37]** and **[E3-39]** say exactly where operating execution belongs —
*"a good managerial record … is far more a function of what business boat you get into than it is
of how effectively you row"*, and *"averaged out, betting on the quality of a business is better
than betting on the quality of management."* **Q2 asks about the boat.**

---

⛔ **Q3, Q4 and Q5 below are RECORDED, NOT GOVERNING.** The file closed at Q2. They are written
because the operator's brief specifically required the bank method to be exercised: Q3 at gate
weight per **[E3-29]**, the reserving record against charge-offs per **[E2-50]**, the quantified
stress per **[E3-24]** beside the bank's own published result, and a below-gate computation.
Under operator rule 3 the valuation arithmetic carries the mandatory heading and **no entry
language**. Nothing below promotes the name; **[E3-29]** is explicit that for a bank cheapness
is not a remedy, and Q2 has already closed the file on the business.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? *(RECORDED, NOT GOVERNING — the file closed at Q2)*
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — THE WEIGHT CASE, and for a bank the corpus decides it in advance.**
*How much damage can this manager do before I can react?*

- [x] **Daily execution** — **[E3-38]**, its 1991 original **[E3-43]**, the 1977 root **[E2-70]**
      (*"their only products are promises"*). $556 billion of assets, $419 billion of deposits,
      1,927 branches, a $118 billion securities book whose duration is a daily decision, and a
      trading operation with a disclosed VaR. A bank is the corpus's own example of the class.
- [ ] **Control** — no; this would be a minority listed position **[E1-16]**.
- [x] **Leverage** — **[E3-29]**. **Assets $556,023M over common equity $58,684M at 2026-06-30
      is 9.5 : 1; over TANGIBLE common equity of $40,429M it is 13.8 : 1.** Below the twenty to
      one the corpus calls *"a common ratio in this industry"*, and **there is no leverage
      ceiling in this framework** — the deleted 10:1 rule does not return
      (`Framework/INVENTIONS - deleted and why.md`). But the *mechanism* [E3-29] names is fully
      present and Truist has already demonstrated it twice: *"mistakes that involve only a small
      portion of assets can destroy a major portion of equity."* A **$6,078 million goodwill
      write-off** took 11.4% of common equity in one quarter of 2023, and a **$6,651 million
      securities loss** — realised on 5.2% of assets — took another 11.5% in one quarter of 2024.

**Case declared: TWO of the three determinants are high, so Q3 is a BINARY GATE and NO PRICE
COMPENSATES [E3-29, E1-16, E5-35].** *"You can turn any investment into a bad deal by paying too
much. What you can't do is turn any investment into a good deal by paying little."*

**AND THE FACT THAT DOMINATES THIS ENTIRE SECTION, WHICH THE BRIEF DID NOT KNOW: THE MANAGER
BEING JUDGED LEFT EIGHTEEN DAYS BEFORE THIS RUN.**

8-K of 2026-06-15, accession `0001193125-26-270320`, Item 5.02, verbatim: *"After more than 40
years of exceptional leadership and service to Truist Financial Corporation … **William H.
Rogers, Jr. will retire as Chief Executive Officer ("CEO") and President … effective on
September 1, 2026** … **Michael P. Lyons will be appointed to serve as CEO and President** … Mr.
Lyons, age 55, most recently served as chief executive officer … of Fiserv, Inc. from May 2025 to
June 2026 … Before that role, he served as **president of The PNC Financial Services Group** …
from February 2024 to January 2025 after serving as executive vice president and head of
corporate and institutional banking beginning in October 2011."*

**Every operating figure in this file was produced by a management that is no longer in place,
and the manager who will produce the next ones has been in the chair since 2026-09-01.** The
furnished slide of **2026-09-15** — his fifteenth day — announces a signed disposal and says a
*"broader strategic review is ongoing."* **[E5-17]**'s cap on this whole question applies with
unusual force: *"People are not that easy to read. Sincerity and empathy can easily be faked"* —
and here there is not even a record at this company to read. The press release adds the fact that
matters most for **[E2-30]**: at PNC, Lyons *"helped lead more than $15 billion of strategic
acquisitions … and expansion of the bank's geographic footprint."*

### Honesty — binary, permanent, filings-based **[E5-16]**, each matter dated to when it became PUBLIC

**No conduct disqualifier found, and it is written in the form the corpus requires: a Q3 pass is
the absence of found disqualifiers, not a finding that the managers are honest [E5-17].** What
the record contains, dated:

- **No consent order, written agreement, memorandum of understanding or civil money penalty is
  disclosed in any of the six 10-Ks FY2020–FY2025.** Item 3 refers to Note 16, and Note 16
  describes **one** matter by name. Both Truist and Truist Bank are classified *"well-capitalized"*
  at 2025-12-31 and 2024-12-31. This is a materially cleaner supervisory record than three of the
  five sponsor banks in the CCB row carried, and it is stated as a positive.
- **The one named matter, and it is inherited: *Bickerstaff v. SunTrust Bank*, filed 2010-07-12.**
  Overdraft fees on debit-card and ATM transactions alleged to be usurious interest under Georgia
  law; class certified 2017-10-06; the class sought *"up to $452 million in paid overdraft fees
  plus prejudgment interest, which … would have been estimated at approximately $463 million as
  of December 31, 2025."* **Settled 2026-01-20, "without any admission of liability or
  wrongdoing," for "up to $240 million,"** preliminary approval 2026-01-23, final-approval
  hearing 2026-05-26. The **$130 million incremental accrual** in 2025 other expense is this
  matter. It is **SunTrust conduct from 2006–2017**, i.e. it predates the merger, and it is
  recorded as a dated fact rather than as a judgment on the present management.
- **Reasonably possible losses in excess of amounts accrued: "up to approximately $150 million in
  the aggregate as of December 31, 2025."** For a $556 billion bank that is 0.25% of common
  equity. Quantified, which is the [E2-26] behaviour.
- **Internal control: no material weakness in any year read.** PricewaterhouseCoopers LLP
  expresses *"an unqualified opinion on the effectiveness of the Company's internal control over
  financial reporting as of December 31, 2025."* **This is the sharpest contrast with CCB**, whose
  FY2025 10-K disclosed remediated material weaknesses and a restatement.
- **The CRA examination result, published in the proxy:** *"we received the highest possible
  overall rating of 'Outstanding' from the Federal Deposit Insurance Corporation for the most
  recent Community Reinvestment Act … examination period from 2020–2022."*

### STEP 2 — THE FLAGS **[E4-22, E5-15, E4-29, E4-30, E2-49, E2-57, E3-53]**. Each is a prompt to READ, never a verdict.

- [ ] **weak accounting — DOES NOT FIRE.** No material weakness, no restatement of earnings, an
  unqualified ICFR opinion, and the one restatement-like event in the window (the 2024 recast for
  discontinued operations and the 2025 line reclassification) was published in advance with full
  retrospective tables in an 8-K.
- [ ] **unintelligible footnotes — DOES NOT FIRE, and the opposite is true.** The disclosures this
  run needed most were all present and quantified: the TIH discontinued-operations income
  statement and cash flows, the exact securities sold and their book yield, the AFS→HTM transfer
  and its $3.7 billion discount, the goodwill test by reporting unit with the reasons, the ACL
  activity table by loan class, CRE by property type AND geography AND non-performing balance,
  the uninsured deposit total on the Call Report methodology, and income taxes paid by
  jurisdiction.
- [x] **TRUMPETED EARNINGS PROJECTIONS AND GROWTH TARGETS — FIRES, AT FULL STRENGTH, AND THE
  NUMBERS ARE PUBLISHED IN A SLIDE.** From the furnished EX-99.3 of 2026-07-17, accession
  `0000092230-26-000096`: the forward-looking-statements list itself includes *"Truist's ROTCE
  goals in future periods, **including achieving a 15% ROTCE in 2027**, and its confidence in
  meeting those goals"*, and slide 17, headed **"On track to achieve ROTCE targets"**, prints the
  path: **2025 12.7% → 2026 ~14% → 2027 ~15% → Long-term 16% to 18%.** The January 2026 deck's
  slide 16 carries five separate quantified guidance lines for the full year. **[E4-22]**'s third
  flag is exact: *"be suspicious of companies that trumpet earnings projections and growth
  expectations … Managers that always promise to 'make the numbers' will at some point be tempted
  to make up the numbers."* **[E4-35]** supplies the base rate and the harm: lofty targets
  *"corrode CEO behavior."* **[E5-30]** supplies the reason it is not merely this year's fact:
  *"once you start it, it's all over. You can't quit … And forecasting earnings, I can't imagine
  anything more destructive."* **A company whose five-year mean return on tangible common equity
  is 11.5% and whose bank-level return on equity is last of nine has published a long-term target
  of 16% to 18%.**
- **[E3-48]'s ACTION, PERFORMED: the company's own past guidance set against outturn, from the
  filings.** This is the test the corpus prescribes and it can be done exactly here, because
  Truist publishes the guide and then publishes the actual.

  | guidance issued 2025-01-17 for FY2025 (8-K `0000092230-25-000005`, EX-99.3) | guided | **actual, from the FY2025 Q4 EX-99.2** | result |
  |---|---|---|---|
  | adjusted revenue-TE, growth on $20,141M | **+3.0% to 3.5%** | **$20,534M = +1.95%** | **MISS by 1.05–1.55 pts** |
  | adjusted noninterest expense, growth on $11,675M | **+~1.5%** | **$11,790M = +0.99%** | beat |
  | net charge-off ratio | **~60 bps** | **54 bps** | beat |
  | effective tax rate | **17%** | **16.4%** | in line |
  | **the composite promise — "driving positive operating leverage"** | ~1.5–2.0 pts | **adjusted efficiency 56.3% → 56.0%, 0.3 pts** | **MISS** |
  | **and the metric the targets are set in** | toward 15% | **ROTCE 13.3% → 12.7%** | **DOWN** |

  **And the 2026 guide has already been cut, in the direction that matters.** Revenue-TE growth
  was guided *"Up 4% to 5%"* in January 2026 and *"Up 3.5% to 4%"* in July 2026, while **the share
  repurchase line was raised from ~$4 billion to ~$5 billion.** Under **[E3-48]** Buffett's stated
  remedy is to demand *"the record of the people who made the projections"*: the record is that
  the revenue half of the promise has been reduced twice in eighteen months while the buyback half
  has been raised twice — **and buybacks raise ROTCE arithmetically by shrinking the denominator,
  which is why the deck's own list of "Key drivers to our ROTCE target" includes "Increase
  buybacks" beside the operating items.** The 15% target is in part an arithmetic promise, not an
  earnings promise, and the run says so.
- [ ] **serial share issuance [E5-15] — DOES NOT FIRE, and the arithmetic runs the other way.**
  Common shares outstanding: 1,348,961k (2020) → 1,327,818k → 1,326,829k → ~1,333,940k → 1,315,936k
  → 1,262,470k → **1,221,626k (2026-06-30)**, a 9.4% reduction. **But one issuance is recorded
  because it is a capital-allocation fact rather than a promotion tell: $495 million of Series S
  non-cumulative perpetual preferred at a stated 6.25% in H1 2026**, issued in the same six months
  in which $2.4 billion of common was repurchased at roughly 12.6× forward earnings (a 7.9%
  earnings yield). Substituting permanent 6.25% non-deductible preferred for common bought at a
  7.9% yield is close to a wash before tax and worse after it; it is recorded, with [E4-13]'s
  humility clause, as a thin trade rather than a flag.
- [ ] **EBITDA / adjusted-earnings promotion — [E4-29] DOES NOT FIRE, checked the way the CGNX
  ruling of 2026-09-07 requires.** The word **EBITDA appears ZERO times** in the FY2025 10-K,
  **zero times** in the 2026 proxy, **zero times** in the Q2 2026 EX-99.1 earnings release and
  **zero times** in the EX-99.3 slide deck. A bank has no EBITDA to trumpet and Truist does not
  invent one.
- [x] **BUT [E2-57], THE "EXCEPT FOR" FLAG, FIRES HARDER THAN [E4-29] WOULD HAVE, AND IT IS THE
  SHARPEST FINDING IN THIS FILE.** *"'except for' should be excised from the lexicon. If you are
  going to play the game, **you must count the runs scored against you in all nine innings.** Any
  manager who consistently says 'except for' … may be missing the only important lesson — namely,
  that **the real mistake is not the act, but the actor.**"* **Truist adjusts out the two largest
  events in its own history, and it does so inside the pay metrics.** From Annex A of the DEF 14A
  filed 2025-03-17 (`0001193125-25-055156`), the reconciliation of adjusted net income for
  incentive-compensation purposes:

  | | FY2024 | FY2023 |
  |---|---|---|
  | net income (loss) available to common from continuing operations, as filed | **$(394)M** | **$(1,864)M** |
  | Securities (gains) losses added back | **+5,090** | — |
  | Goodwill impairment added back | — | **+6,078** |
  | Charitable contribution added back | +115 | — |
  | FDIC special assessment added back | +49 | +387 |
  | Restructuring charges added back | *(also added back)* | *(also added back)* |

  **And the award was paid.** From the DEF 14A of 2025-03-17: the 2024 AIP for William H. Rogers,
  Jr. was struck on a **$1,200,000 base salary, a 300% target and a 95.00% payout** — a
  **$3,420,000 annual bonus in a year in which continuing operations lost $394 million for common
  shareholders and the company realised a $6,651 million securities loss.** **[E5-33]** is the
  governing line: *"to tell owners year after year, 'Don't count this' … is misleading"*, and the
  charges *"borne by shareholders"* belong in the mean.
- **THE COUNTERWEIGHT, AND IT IS REAL, SO IT IS GIVEN THE SAME PROMINENCE [E4-26].** The
  **long-term** award was not adjusted into existence, and it paid **nothing**. From the DEF 14A
  of 2026-03-16 (`0001193125-26-107144`): the **2023–2025 PSU and LTIP awards** carried one metric
  — **"Relative 3-Year Average Adjusted ROCE", weighted 100%** — performance **"Below Threshold"**,
  final payment **"No awards earned."** The company adds that Rogers's *"Realized Pay was 60% of
  his Target Pay in the aggregate"* for 2022–2025, *"driven by not meeting threshold performance
  under our 2023-2025 PSU and LTIP awards."* **That is [E2-49]'s positive condition met — a
  "pre-set, long-lived and small bullseye" that was kept while it read unfavourably and published
  as a zero** — and it is a *relative* metric, which means the company's own pay committee reached
  the same conclusion this run's competitor row reached: Truist's adjusted return on capital
  employed was below its peers' for three consecutive years.
- [x] **METRIC-SWITCHING [E2-49] — FIRES TWICE, AND ONE OF THE TWO IS THE CLEANEST INSTANCE THIS
  PROJECT HAS FOUND.**
  1. **THE MERGER'S OWN YARDSTICK WAS DROPPED WITHOUT BEING REPORTED AGAINST.** The FY2020 10-K:
     *"Truist reaffirmed its commitment to achieving **$1.6 billion in net cost saves on a run rate
     basis by the fourth quarter of 2022**."* The FY2021 10-K: *"Truist achieved its fourth quarter
     2021 net cost saves target and **continues to reaffirm its commitment to achieving $1.6 billion
     in net cost saves on a run rate basis by the fourth quarter of 2022**."* **The FY2022 10-K
     contains ZERO occurrences of the words "cost save" or "saves". So does the FY2023 10-K.** The
     target's own deadline year is the year the filer stopped mentioning it, and no statement of
     achievement or shortfall was ever made. This is precisely *"disposition of the yardstick
     rather than disposition of the manager."* *(Searched: `grep -i "cost save|expense save|saves"`
     over the full text of all six 10-Ks; the phrase appears in FY2020 and FY2021 only.)*
  2. **The restructuring-charge line was deleted from the income statement.** FY2025 10-K, Table 9,
     footnote 1: *"Effective December 31, 2025, Truist **reclassified the underlying activities of
     restructuring charges, which were previously reported in a separate financial statement
     caption, to their natural expense categories** of 'Personnel,' 'Net occupancy,' 'Professional
     fees and outside processing,' and 'Other expense.' Prior period balances have been conformed
     to current period presentation."* **[E3-53]** is about dumping costs into one quarter; this is
     the inverse and it is worse for a reader — after six consecutive years of restructuring
     charges ($146M, $360M, $860M, $822M, $466M, $320M, $120M, $156M on the various bases), the
     line a reader would use to see them **no longer exists**. **Recorded two-sided, as [E2-69]
     requires:** it was announced in advance, in the 8-K of 2026-01-12 (`0000092230-26-000006`),
     with seven quarters of retrospective figures, and the non-GAAP reconciliation in the Q4 2025
     EX-99.2 still discloses restructuring of $156M for 2025 and $120M for 2024. **Disclosure was
     made; the primary statement got less legible.**
- [x] **FILED-FIGURE TELLS [E4-30] — the cash-tax tell FIRES, and the read is mechanical, not
  venal.** *Income taxes PAID*, from Note 14 (a disaggregation newly required and adopted
  retrospectively) and from the supplemental cash-flow disclosures: **$126M (2020), $792M (2021),
  $479M (2022), $780M (2023), $830M (2024), $192M (2025).** Against pre-tax income of $7,979M
  (2021), $7,669M (2022) and **$6,349M (2025)**, cash taxes were **9.9%, 6.2% and 3.0%** — against
  a 21% statutory rate and book effective rates of 19.5%, 18.3% and 16.4%. **[E4-30]**: *"This
  plainly increased their chances of attracting undesired questions."* **The question is asked and
  answered from the filing.** The FY2025 rate reconciliation names $272M of low-income-housing,
  energy and new-market tax credits and $204M of tax-exempt income — 7.5 points of the gap — and
  the 2024 securities loss generated a **$556 million tax benefit** whose cash effect lands in
  2025. **[E5-38]** governs the conclusion: a fired flag is not a venality finding. It is recorded
  as read and explained. **Reported growth is NOT unnaturally smooth** — net income available to
  common went $6,033M, $5,927M, **−$1,452M**, $4,469M, $4,974M. Nothing is being ironed flat; the
  opposite.
- [ ] **dividends funded by issuance [E2-52] — DOES NOT FIRE.** Common dividends of $2.7bn in 2025
  against $4,974M of net income available to common — a 54% payout — with the share count falling.
  No capital is being replaced to fund the distribution.
- [ ] **stock-price targeting [E3-50] — DOES NOT FIRE as stated**, but it is recorded as adjacent:
  the December 2025 authorisation of **$10.0 billion** with **no expiration date** on a
  $59.3 billion market capitalisation, and a published 2026 target of ~$5 billion of repurchases,
  is a standing commitment to buy about 8.4% of the company a year regardless of price. That is
  assessed under [E5-08] below rather than here.

### STEP 3 — THE PRIMARY TEST **[E2-01]**, and the bank CONVENTION the corpus forces us to confess

> **CONVENTION (TFC, 2026-09-19), under PRIME RULE 3, adopting CCB's construction of
> 2026-09-19 with ACNB's split and one refinement Truist's own filings make necessary.**
>
> *Owner earnings by the ordinary construction — operating cash flow less share-based
> compensation less a maintenance-capex guess — does not work for a bank, for the three reasons
> the CCB run of 2026-09-19 set out and which hold here at 250× the size: operating cash flow is
> not a return (Truist's includes the whole provision and the securities loss as non-cash
> reversals); there is no maintenance capex that matters (premises and equipment are **$3,177
> million against $556,023 million of assets**, and a loan book does not wear out); and deposit
> and loan flows are financing and investing, so the cash statement of a bank measures growth,
> not earnings.*
>
> ***So the metric set is selected by business type first, exactly as [E5-37] requires, and the
> metric is the one the corpus itself names for this job — [E2-01]'s "high earnings rate on
> equity capital employed … without undue leverage, accounting gimmickry, etc." Three measures,
> every figure from a filed statement:***
> 1. ***return on average common equity*** and ***return on average TANGIBLE common equity***,
>    recomputed from opening and closing balances and reported beside the filer's own figure;
> 2. ***return on average assets***, because it is leverage-independent and is what the FDIC
>    publishes for every bank in the country;
> 3. ***the (c) EQUIVALENT, and this is the part that is ours.*** *For a bank the expenditure the
>    business "requires to fully maintain its long-term competitive position and its unit volume"
>    **[E2-23]** is not plant; it is **the equity that must be retained to hold the regulatory
>    capital ratio constant while the balance sheet grows.** CCB's form was **(c) = Δassets ×
>    the Tier 1 leverage ratio**, and ACNB ruled that Δassets must be **split into organic and
>    acquired** or (c) reports a stock issuance as a loss of earning power.*
>
> ***THE REFINEMENT TRUIST FORCES, AND THE BRIEF ASKED FOR EXACTLY THIS ("follow their
> construction unless Truist's filings make it wrong, and say which"): for Truist, Δtotal assets
> is the wrong measure of growth and the filings say why.*** *Truist's total assets fell $19,906
> million in 2023 and $4,173 million in 2024, and neither was a contraction of the business:
> $7,655 million of it was the Insurance Holdings segment leaving the balance sheet on
> 2024-05-06, and most of the rest was a deliberate securities repositioning. Total assets also
> swing $20 billion on a decision about how much cash to hold at the Federal Reserve, which
> consumes almost no capital. **So a third construction is computed: (c) = Δ(risk-weighted
> assets) × the CET1 ratio** — which is the binding constraint, is what the regulator measures,
> and is the one the company itself uses in public: the 8-K of 2026-09-15 values the disposal of
> $5.5 billion of loans as *"$945MM or 22 bps of CET1 capital."* **All three are reported below.
> The RWA/CET1 version is the one this run treats as the measure, and the reason is named.***
>
> *Denominator scope, per **[E2-43]**: goodwill and intangibles are shown separately and never
> hidden in book equity. Truist carries **$17,125 million of goodwill and $1,130 million of other
> intangibles at 2026-06-30 against $58,684 million of common equity — the wedge is 31.1% of the
> common equity, and $6,078 million of it was already written off in 2023.** Share-based
> compensation is already an expense in the reported figures and is **not** added back **[E5-06]**.*

**The primary test, recomputed (`Test Runs/_research 2026-09-19 TFC/arith.py`):**

| year | NI avail. common $M | avg common equity $M | **ROE %** | avg tangible common equity $M | **ROTCE %** | filer's own ROTCE | avg assets $M | **ROA %** |
|---|---|---|---|---|---|---|---|---|
| 2020 | 4,184 | 62,160 | 6.73 | 34,796 | 12.02 | n/d | 491,153 | 0.852 |
| 2021 | 6,033 | 62,731 | 9.62 | 34,262 | **17.61** | n/d | 525,234 | 1.149 |
| 2022 | 5,927 | 58,231 | 10.18 | 30,026 | **19.74** | n/d | 548,248 | 1.081 |
| 2023 | **(1,452)** | 53,222 | **(2.73)** | 30,237 | **(4.80)** | 18.9 *(adjusted)* | 545,302 | **(0.266)** |
| 2024 | 4,469 | 55,176 | 8.10 | 36,306 | 12.31 | 13.3 | 533,262 | 0.838 |
| 2025 | 4,974 | 59,022 | 8.43 | 40,494 | **12.28** | **12.7** | 539,357 | **0.922** |
| H1 2026 annualised | 5,800 | 59,478 | 9.75 | 41,160 | **14.09** | 13.8 / **15.4** by quarter | 551,780 | 1.051 |

**Two things have to be said about this table before it is used.**

**First, the method is validated and the gap is explained.** This run's 2025 ROTCE of 12.28%
against the filer's published 12.7% is the $290 million of intangible amortisation and the $416
million deferred-tax adjustment that Truist adds and this run does not. **Second, the filer's own
2023 ROTCE of 18.9% is the [E2-57] flag in its purest form:** it is computed on "tangible net
income" with the **$6,078 million goodwill impairment added back**, so a year in which common
shareholders lost $1,452 million is published as an 18.9% return on their capital. **Both numbers
are in the same table in the FY2025 10-K (Table 38), which is why this is a disclosure finding and
not a concealment finding — but a reader who takes the 18.9% is reading a number that describes a
year that did not happen.**

**THE CORRECTION THIS SECTION OWES Q2, recorded as an addendum rather than by editing the
committed table (operator rule 6).** Q2's ROTCE row for Truist was computed from companyfacts'
**latest-vintage** goodwill, and for Truist the latest vintage is the **post-recast, ex-Insurance
figure**: companyfacts carries **$23,233 million** of goodwill at 2022-12-31, while the FY2022
10-K's own balance sheet carries **$27,013 million** at the same date — a $3,780 million
difference, which is the Insurance Holdings goodwill later moved to discontinued operations.
Recomputed on the **as-filed** tangible common equity published in each year's own capital table
($36,130M / $33,826M / $23,933M / $29,122M / $39,498M / $42,264M), Truist's ROTCE is **17.25
(2021), 20.52 (2022), −5.47 (2023), 13.02 (2024), 12.17 (2025)** and the five-year mean is
**11.50% instead of 11.43%. Truist's rank of 8 of 9 does not change, on either the five-year mean
or 2025 alone.** *This is the CNR rule biting the analyst rather than the filer, and it is exactly
the trap `sources.py:name_change_note` warned about at the top of this file.*

**What the series says.** Return on average assets: **1.149 → 1.081 → −0.266 → 0.838 → 0.922 →
1.051 annualised.** Five full years averaging **0.745%**, against the same nine-bank row's median
of 1.027% and Regions' 1.326%. **[E3-46]** asks the second question about the business as a
number, and the number is below median through a full cycle. **[E2-47]**'s carve-outs are checked
and neither rescues it: leverage is mid-pack at 13.3× tangible, and the asset values are not
mis-stated — the one large mis-statement of asset value in the record, $6,078 million of goodwill,
was **written off**, which is the honest treatment.

### The (c) equivalent — three constructions, and the bank's "owner earnings"

| year | Δ total assets $M | Tier 1 lev. % | **(i) CCB: Δassets × lev** | organic Δ $M | **(ii) ACNB split** | Δ RWA $M | CET1 % | **(iii) ΔRWA × CET1** | net income $M |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | +32,013 | 8.7 | 2,785 | +28,713 | 2,498 | +11,733 | 9.6 | **1,126** | 6,406 |
| 2022 | +14,014 | 8.5 | 1,191 | +14,014 | 1,191 | +43,527 | 9.0 | **3,917** | 6,267 |
| 2023 | −19,906 | 9.3 | (1,851) | −16,506 | (1,535) | −10,708 | 10.1 | **(1,082)** | (1,047) |
| 2024 | −4,173 | 10.5 | (438) | **+3,482** | **366** | −9,996 | 11.5 | **(617)** | 4,840 |
| 2025 | +16,362 | 10.0 | 1,636 | +16,362 | 1,636 | +24,920 | 10.8 | **2,691** | 5,307 |
| H1 2026 ann. | +8,485 | 10.1 | 857 | +8,485 | 857 | −8,458 | 10.9 | **(922)** | 6,060 |
| **2021-25 total** | | | **3,323** | | **4,156** | | | **6,036** | **21,773** |

**"Owner earnings" for a bank = net income − (c):**

| year | net income | (i) CCB | (ii) ACNB split | **(iii) RWA × CET1 — the measure used** |
|---|---|---|---|---|
| 2021 | 6,406 | 3,621 | 3,908 | **5,280** |
| 2022 | 6,267 | 5,076 | 5,076 | **2,350** |
| 2023 | (1,047) | 804 | 488 | **35** |
| 2024 | 4,840 | 5,278 | 4,474 | **5,457** |
| 2025 | 5,307 | 3,671 | 3,671 | **2,616** |
| **five-year mean** | **4,355** | **3,690** | **3,523** | **3,147** |
| **three-year mean 2023-25** | 3,033 | | | **2,702** |
| **2025 alone** | 5,307 | | | **2,616** |

**The construction matters and the spread is the finding.** On the (iii) basis, **Truist earned
$21,773 million over five years and had to retain $6,036 million of it simply to hold its CET1
ratio while its risk-weighted assets grew from $379.2 billion to $443.3 billion** — 27.7% of
cumulative earnings went to standing still. On the (i) basis it was 15.3%, and the difference is
entirely the 2023 and 2024 asset shrinkage, which flatters the CCB form because a disposal reads
as released capital. **This is why the brief's instruction to say where Truist's filings make the
prior construction wrong matters: on CCB's form, the year Truist sold its best business and
realised a $6.7 billion loss (2024) prints the HIGHEST owner earnings of the six ($5,278M),
which is absurd, and the RWA form prints $5,457M for the same reason — both are wrong in the same
direction, because releasing regulatory capital is not earning it.** The honest reading is that
**2022 and 2025, the two years of real balance-sheet growth, are the years that show what growth
costs this bank: $3,917 million and $2,691 million of retained capital against $6,267 million and
$5,307 million of net income.** A bank growing risk-weighted assets 5-6% a year at a 10.8% CET1
ratio must retain roughly half its earnings to do it.

**And the equity account confirms it independently, which is the check ACNB's ruling asks for.**
Common equity went **$62,864 million (2020-12-31) → $60,273 million (2025-12-31), a DECLINE of
$2,591 million**, while cumulative net income available to common over the five years was
**$19,951 million**. The reconciliation: **−$13,500 million of common dividends, −$5,350 million
of buybacks, and −$3,692 million of AOCI and other.** No shares were issued to fund it; **the
shareholder's return from this business over five years was the cash it paid out plus a fall in
its own book equity.**

### **[E3-54]**, the corpus's own scored retention test — and it fails

*At least $1 of market value per $1 retained, five years rolling.* Per share, which is the only
honest basis when the count is changing: diluted EPS summed 2021-2025 = **$4.51 + $4.43 − $1.09 +
$3.36 + $3.82 = $15.03**; dividends declared per share = **$1.86 + $2.00 + $2.08 + $2.08 + $2.08 =
$10.10**; **retained per share = $4.93.** The share price went **$47.93 (2020-12-31) → $49.21
(2025-12-31), +$1.28** *(closes from `tools/sources.py`, aggregator, flagged, used only for the
market-value leg)*. **$0.26 of market value per $1 retained.** The test's own 2009 self-correction
allows a book-value-plus-premium reading, and it gives the same answer: **tangible book value per
share went $26.78 → $33.48, +25.0% over five years, or 4.6% a year.**

**And the filer publishes the comparison itself, which is the [E2-26] and [E2-69] behaviour.**
FY2025 10-K, Table 5, Cumulative Total Shareholder Return, $100 invested at 2020-12-31:

| | 2021 | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|---|
| **Truist Financial Corporation** | 126.07 | 96.43 | 88.21 | 109.13 | **129.86** |
| S&P 500 Index | 128.68 | 105.36 | 133.03 | 166.28 | **195.98** |
| KBW Nasdaq Bank Index | 138.34 | 108.74 | 107.77 | 147.87 | **196.02** |

**Truist returned 29.9% over five years against 96.0% for its own industry index — 66 points
behind the banks, not the market.** It cannot be explained by rates or by the sector; the sector
is in the table. **Truist publishing it is the candor case; the content is the capital-allocation
verdict.**

### The half-owner test **[E2-26]** — and the reserving candor benchmark **[E2-67]**

*Does this reporting tell me what I would want to know if the positions were reversed?* **Yes,
substantially, and in two places it exceeds what the sector does.**

- **[E2-50]** puts the Q3 weight on reserves in an estimate-driven business — *"where 'earnings'
  can be created by the stroke of a pen, the dishonest will gather"* — and **[E2-67]** names the
  positive pole: a filer that publishes its own reserving errors, *"so you can … judge whether we
  may have some systemic bias."* **A bank has no reserve-development triangle. Truist publishes
  the nearest equivalent that exists, every year, with a number:** *"Under the range of scenarios
  considered as of December 31, 2025, use of the Company's **pessimistic scenario would have
  resulted in an increase to the modeled allowance results of approximately $2.4 billion**."* The
  same sentence, with its own figure, appears in all five 10-Ks: **$2.1bn (2021), $2.2bn (2022),
  $2.2bn (2023), $2.2bn (2024), $2.4bn (2025)**. That is the company stating, on the record and
  in dollars, how wrong its central reserve could be — and the direction. **On a $5,347 million
  allowance, the disclosed pessimistic add is 45%.**
- **THE RESERVING RECORD AGAINST SUBSEQUENT CHARGE-OFFS, which is what [E2-50] actually asks
  for.** Every figure from the ACL activity tables of the five 10-Ks:

  | $M | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|
  | ACL, beginning | 1,651 | 1,889 | 6,199 | 4,695 | 4,649 | 5,093 | 5,161 |
  | CECL adoption | — | +3,140 | — | — | — | — | — |
  | **provision for credit losses** | 615 | 2,335 | **(813)** | 777 | 2,109 | 1,870 | 1,894 |
  | **net charge-offs** | 634 | 1,119 | 697 | 823 | 1,595 | 1,803 | 1,705 |
  | ACL, ending | 1,889 | 6,199 | 4,695 | 4,649 | 5,093 | 5,347 | 5,347 |
  | ALLL ratio | — | — | 1.53% | 1.34% | 1.54% | 1.59% | 1.53% |
  | ALLL ÷ net charge-offs | — | 5.2× | 6.4× | 5.3× | 3.0× | 2.7× | **3.0×** |

  **The test, run forward as [E2-50] requires — was each year's reserve adequate for the losses
  that actually followed?**
  - ACL at 2021-12-31 of **$4,695M** against the next two years' net charge-offs of **$2,418M** —
    **1.94× covered.**
  - ACL at 2022-12-31 of **$4,649M** against 2023+2024 charge-offs of **$3,398M** — **1.37×.**
  - ACL at 2023-12-31 of **$5,093M** against 2024+2025 charge-offs of **$3,508M** — **1.45×.**
  - **The reserve was never caught short**, the ALLL ratio has moved in a 25-basis-point band
    through a full credit cycle (1.34%–1.59%), and the provision has exceeded net charge-offs in
    every year since 2022. **No evidence of reserve manipulation in either direction is found.**
  - **The one prompt, and it is the industry's, not Truist's: the $813 million NEGATIVE provision
    in 2021.** It added roughly $620 million after tax to a year that reported $6,033 million —
    about 10% of the earnings — and it was released into a loss cycle that then rose for four
    consecutive years (0.24% → 0.27% → 0.50% → 0.59% → 0.54% of average loans). **[E3-02]** is the
    lens the corpus supplies: *"the tendency of executives to mindlessly imitate the behavior of
    their peers"* — every large US bank released COVID reserves in 2021, and Truist did what the
    peers did. **It is recorded as a conformity prompt, not a reserving failure, because the
    reserve that remained proved 1.94× the following two years' losses.**
- **The gap in the candor record, stated because it is the one thing a half-owner would want and
  does not get:** Truist publishes its **modelled** allowance sensitivity but does **not** publish
  a backtest of its own ACL model against realised losses by vintage, and no accounting standard
  requires one. This is the same structural gap the SOFI fold recorded on 2026-09-19 from the
  other direction — a fair-value lender has no reserve table at all — and it is worth carrying:
  **[E2-67]**'s artifact exists for insurers and has no mandated equivalent for banks.
- **Authorship [E2-72]:** Truist files no annual shareholder letter in its 10-K; the Executive
  Overview is unsigned corporate prose (*"we focused on delivering strong, purpose-driven
  performance"*). **[E2-72]** — *"owners are entitled to hear directly from the CEO … A once-a-year
  report of stewardship should not be turned over to a staff specialist or public relations
  consultant"* — is **not met**, and the CEO's only signed communication to owners in the record
  is the quarterly earnings-release quote. Recorded as a tell, not a disqualifier.

### The institutional imperative — score all four **[E2-30]**. *Not a fraud test: "institutional dynamics, not venality or stupidity."*

- [ ] **resists any change in current direction — DOES NOT FIRE, and the opposite behaviour is the
      finding.** Truist has changed direction repeatedly and publicly: sold 20% of insurance
      (2023-04-03), sold the student loan portfolio (Q2 2023), sold the rest of insurance
      (2024-05-06), sold Sterling Capital Management (July 2024), discontinued Marine/RV lending,
      agreed to sell Regional Acceptance (2026-09-15), and has a *"broader strategic review …
      ongoing."* **Serial reshaping is not the imperative behaviour [E2-30] describes; it is the
      [E3-40] concern — capital and attention moving away from the base business — read from the
      disposal side rather than the acquisition side.**
- [x] **projects or acquisitions materialise to soak up available funds — FIRES, with dates and
      prices.** **$2.0 billion of cash for Service Finance, LLC on 2021-12-06**, producing $1.2
      billion of goodwill and $647 million of intangibles; **Constellation Affiliated Partners on
      2021-07-01** ($582 million of goodwill) and **Kensington Vanguard National Land Services**
      announced early 2022 — **both bought to expand the Insurance Holdings segment that was sold
      in its entirety twenty-eight months later.** **[E5-24]**: *"what is smart at one price is
      dumb at another"* — and the same management bought into a business at one price and exited
      the whole of it at another, inside three years.
- [x] **staff studies produced to justify the leader's craving — FIRES, and the filing prices
      it.** FY2022 10-K, explaining 2021 expenses: the prior year included *"**a $30 million
      professional fee to develop an ongoing program to identify, prioritize, and roadmap teammate
      generated revenue growth and expense savings opportunities beyond the Merger**."* **[E3-58]**
      is exact that solving capital allocation *"by either having a staff that does it, or by
      hiring consultants"* is *"a terrible mistake."* Thirty million dollars for a roadmap is the
      behaviour, disclosed to the dollar.
- [x] **peer behaviour mindlessly imitated — FIRES, AND THIS IS [E3-02], THE CORPUS'S NAMED BANK
      FAILURE MODE.** The brief's instruction is *"test what this bank did while its peers were
      lax."* The answer is on the balance sheet:
      **AFS securities at fair value: $74,727M (2019) → $120,788M (2020) → $153,123M (2021).**
      Truist **doubled** its securities book in the two years of the lowest interest rates in
      American history. Then, **in the first quarter of 2022, it "transferred $59.4 billion of AFS
      securities to HTM as the Company continues to execute upon its asset-liability management
      strategies"** — a transfer that, in the filer's own words, froze *"the difference between the
      par value and the fair value of these securities, which was recorded as a loss in AOCI,
      [resulting] in a net discount of $3.7 billion"* to be amortised back through interest
      income, and **which stops further marks from reaching the reported balance sheet.** Then, in
      the second quarter of 2024, it sold **$27.7 billion** of what remained in AFS at a **$6,651
      million pre-tax loss**. *"The tendency of executives to mindlessly imitate the behavior of
      their peers, no matter how foolish it may be to do so"* **[E3-02]** is the whole sequence,
      and **Truist did not do better than the peers; it did the same thing on a larger base.**

**Three of four fire. [E2-30]'s last clause governs: this is not a fraud test.**

### Capital allocation — the two buyback conditions **[E5-08]**, and the third **[E4-31]**

- **(1) ample funds for operations and liquidity? YES.** $207.7 billion of selected liquidity
  sources at 2025-12-31 against $177.6 billion of uninsured deposits; available secured borrowing
  capacity *"approximately 4.8 times the amount of wholesale funding maturities in one year or
  less"*; CET1 10.8% against a 4.5% minimum plus a 2.5% stress capital buffer; parent-company cash
  managed *"to exceed a minimum of 12 months of projected cash outflows."* Condition one is met
  comfortably and it is the strongest part of the Q3 record.
- **(2) repurchases at a MATERIAL DISCOUNT to conservatively calculated intrinsic value? NO — AND
  THIS IS A LIVE CAPITAL ALLOCATION FLAG.** The facts: **$0 in 2023, $1.0 billion in 2024, $2.5
  billion in 2025, $2.4 billion in the first half of 2026 (46.6 million shares, ~$51.5 a share
  including excise tax)**, a **$10.0 billion authorisation with no expiration date** adopted in
  December 2025, **$7.7 billion still available at 2026-06-30**, and a guided **~$5 billion for
  2026** — about **8.4% of the market capitalisation in one year.** Against this run's own Q5
  computation below, the honest pre-tax expectancy at $48.56 is **about 8%**, below the ~10%
  **[E4-28]** floor. **Buying at $51.5 when the conservative value is at or below the quote is not
  a material discount.** The mechanical consequence is on the record: **tangible book value per
  share FELL from $33.48 at 2025-12-31 to $33.40 at 2026-06-30 while the company earned $3.0
  billion**, and buying 46.6 million shares at ~$51.5 against a $33.4 tangible book cost roughly
  **$845 million of tangible book value in six months** — about $0.69 per remaining share.
  **Stated with the humility clause [E4-13] and [E5-08]'s own:** *"it is natural for CEOs to be
  optimistic about their own businesses. They also know a whole lot more about them than I do,"*
  and *"many CEOs never stop believing their stock is cheap."* This flag rests on **our** value
  range and **binds position size, never the discount rate.** It is also not the worst case the
  corpus describes: Truist is buying at roughly 1.0× book and 12.6× forward earnings, not at three
  times book.
- **(3) [E4-31]'s forgotten third condition — "Shareholders should have been supplied all the
  information they need for estimating that value." MET.** Truist publishes tangible book value
  per share, the full securities portfolio with fair values, the ACL sensitivity, CRE by property
  type and geography, uninsured deposits on the Call Report methodology, and the disposals with
  their proceeds. A reader can build a value, which is what this file has done.
- **[E5-25]'s standard — did they publish both conditions as NUMBERS in advance, the way
  Berkshire did? NO.** There is no stated price limit, no book-value ceiling, and no liquidity
  floor attached to the repurchase authority; the FY2025 10-K lists *"the trading price of
  Truist's common stock"* among many *"various factors"* management *"determines to be advisable."*
  A $10 billion open-ended authorisation with a published annual target and no price discipline is
  the **opposite** of the 110%-of-book limit and the $20 billion liquidity floor **[E5-25]**
  names — and the ROTCE target the buyback serves is itself published.

### THE INSURANCE SALE — the sharpest capital-allocation fact on file, tested against **[E5-08]** and **[E2-60]**

**What was received.** Two transactions, both dated from the filings:
- **2023-04-03:** 20% of the common equity of Truist Insurance Holdings sold to an investor group
  led by Stone Point Capital for **$1.9 billion**, *"with the proceeds, net of tax, recognized as
  an increase to shareholders' equity"* — **$1,922 million of net cash** in the cash-flow
  statement. The buyer also received *"profits interest representing 3.75% coverage on TIH's fully
  diluted equity value"* and consent and exit rights, and was allocated *"approximately 23% of TIH
  pretax net income."*
- **2024-02-20 agreed, 2024-05-06 completed:** the remaining stake sold to a group led by Stone
  Point and Clayton, Dubilier & Rice *"for a purchase price that implied an **enterprise value for
  TIH of $15.5 billion**."* **Gain on sale $6,939 million pre-tax, $4,841 million after tax, $3.64
  a share; after-tax cash proceeds to Truist of approximately $10.1 billion.**

**What was sold.** The discontinued-operations note prices the business precisely: TIH earned
**insurance income of $3,372 million and pre-tax income of $580 million in 2023**, and **$3,086
million and $640 million in 2022**, on almost no balance sheet ($7,655 million of total assets at
2023-12-31, most of it goodwill and receivables). **$10.1 billion of after-tax cash for a business
earning roughly $480 million of net income is between 21 and 27 times earnings**, against a bank
that has traded between 7 and 13 times its own. **The sale itself was a good sale, and this run
says so without qualification: it converted a capital-light fee business trading at a bank's
multiple inside a bank into cash at an insurance broker's multiple. It is the single best capital
allocation decision in the file.**

**What was done with the money, and this is where [E5-08] and [E2-60] bite.** From the FY2024
10-K, verbatim: *"Following the sale of TIH, which resulted in after-tax cash proceeds to Truist
of approximately $10.1 billion, Truist executed a strategic balance sheet repositioning of a
portion of its AFS investment securities portfolio by **selling $27.7 billion of lower-yielding
investment securities, resulting in an after-tax loss of $5.1 billion in the second quarter of
2024**. The investment securities that were sold had a book value of $34.4 billion and a
**weighted average book yield of 2.80%** … Including the tax benefit, the repositioning generated
$29.3 billion available for reinvestment … Truist invested approximately $18.7 billion of the
$39.4 billion available … **in shorter duration investment securities yielding 5.27%**. The
remaining $20.7 billion was invested in cash."*

**THE HONEST READING, AND IT CUTS AGAINST THE OBVIOUS CRITICISM, SO IT IS GIVEN FIRST [E4-51].**
The $6,651 million pre-tax loss **did not destroy tangible book value, because the loss was
already there.** AFS securities are marked through AOCI, so the decline had already been deducted
from common equity: the 2024 comprehensive-income statement shows **+$4,205 million of after-tax
"net change in AFS securities" in OCI**, which is the same loss travelling out of AOCI as it
travelled into retained earnings. The net equity effect of the realisation is approximately zero,
and the **tax benefit was real cash** — *"including the tax benefit, the repositioning generated
$29.3 billion"* against $27.7 billion of proceeds. Reinvesting a 2.80% book at 5.27% adds roughly
**$680 million a year of pre-tax interest income** on $27.7 billion. **Taken on its own, the
repositioning was a sensible trade and a competent execution, and any reading that calls it "$5
billion destroyed" is wrong.**

**THE CRITICISM THAT SURVIVES, AND IT IS THE ONE THAT MATTERS.** The repositioning was **the
remedy, and the disease was the decision that created it** — buying $78.4 billion of additional
securities in 2020 and 2021 at yields that produced a 2.80% book, then moving $59.4 billion of the
result into held-to-maturity in the first quarter of 2022 so the marks would stop appearing.
**[E2-60]** is the test the brief names and it is the right one: restricted earnings are those
whose payout costs the business *"its ability to maintain its unit volume of sales, its long-term
competitive position, **its financial strength**."* Truist did not distribute the insurance
proceeds — **it used them to repair a balance sheet its own earlier decisions had damaged**, which
is the correct use and also an admission of what the earlier decisions cost. **The measure of the
cost is the securities book's own arithmetic: $27.7 billion had to be sold at 81 cents in the
dollar to get out of a position entered at par, and $46.4 billion of held-to-maturity securities
still carry a fair value of $38.1 billion at 2026-06-30 — an $8.2 billion unrealised loss, 14.0%
of common equity, which no repositioning has touched.** That is the residue of the same decision
and it is priced at Q4.

**And the pattern is about to repeat, on the record, four days before this run.** The furnished
slide of 2026-09-15 says the Regional Acceptance disposal *"Generates $5.2B of net proceeds and a
$535MM loan loss reserve recapture … Creates $945MM or 22 bps of CET1 capital"* — and then, under
*"Illustrative liquidity and capital deployment actions"*: *"Repay wholesale borrowings with
proceeds from loan sale"* and **"Reposition certain AFS securities to fully offset capital created
from RAC sale."** **The stated plan is to spend the entire capital benefit of selling a business
on realising more securities losses**, with the **"2026 share repurchase target unchanged at
$5B."** It is the same trade as 2024, announced in advance, and it is recorded here as the
capital-allocation pattern rather than as a criticism of the trade's economics.

### THE GUARDRAIL — checked before the verdict

- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** **[E2-37]** — *"a
      textile company that allocates capital brilliantly within its industry is a remarkable
      textile company — but not a remarkable business"* — and **[E3-39]** — *"averaged out, betting
      on the quality of a business is better than betting on the quality of management."* Q2 has
      already found no franchise, and nothing here repairs it.
- [x] **The requires-a-great-manager finding is recorded at Q2 as a moat defect [E4-23]**, not
      here as a strength. The bull case for Truist in September 2026 is a new chief executive.
- [x] **[E2-35] and [E2-36], the one exception and its boundary, tested and failed.** Is the
      franchise already intact with a *"localized excisable cancer"*, or **is the manager the
      plan**? **The manager is the plan.** The franchise was found absent at Q2 on nine-bank
      filings and Call Reports; the damage is not local (it is the return on every dollar of the
      balance sheet); and the fix on offer is *"a broader strategic review"* by a chief executive
      of eighteen days' standing with a published 16–18% long-term target. **[E2-36]**: *"the true
      'turnaround' situation in which the managers expect — and need — to pull off a corporate
      Pygmalion"* is the class, and it is not buyable. **[E2-38]** is the same point in one line:
      *"Good jockeys will do well on good horses, but not on broken-down nags."*

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** *(RECORDED, NOT GOVERNING — the
  file closed at Q2)*

**And the ground is stated precisely, because the two grounds are not interchangeable [E5-16].
THIS IS NOT AN INTEGRITY FINDING.** No conduct disqualifier was found: no consent order, no
material weakness, an unqualified internal-control opinion, an "Outstanding" CRA rating, a
long-term award that paid zero and was published as zero, a five-year ACL sensitivity disclosed in
dollars, and the company's own five-year underperformance against its own industry index printed in
its own 10-K. **The verdict is OUT on [E3-29]'s standard, which is the only place in the framework
where cheapness is ruled out as a remedy:** *"we have no interest in purchasing shares of a
poorly-managed bank at a 'cheap' price. Instead, our only interest is in buying into well-managed
banks at fair prices."* On the regulator's own uniform definitions Truist Bank has the **worst
five-year mean pre-tax return on assets and the worst five-year mean return on equity of the nine
largest regional banks in the United States**; the goodwill of the merger that created the company
was written down by $6,078 million four years after it closed; $27.7 billion of securities were
sold at a $6,651 million loss; the merger's own $1.6 billion cost-save yardstick was dropped
without a report; three of the four institutional-imperative behaviours fire; and the shareholder
who bought at the start of the window has 29.9% against his own industry index's 96.0%. **That is
the record of a bank that was not well managed, and Q3 at gate weight says no price fixes it.**

**THE STRONGEST FACT AGAINST THIS VERDICT [E4-51], and it is the same one that argues against
Q2's.** *The management that produced this record is gone.* Michael Lyons has been chief executive
since 2026-09-01; Bill Rogers's own long-term award paid nothing, which means the board's
pre-registered metric reached the same conclusion this run did and acted on it; the adjusted
efficiency ratio in H1 2026 is the best of the nine banks on the FDIC's numbers; ROTCE has gone
12.7% → 13.8% → 15.4% in three quarters; and the first capital action of the new regime is to sell
the worst-returning loan book in the company. **A reader who believes the framework should judge
the forward manager rather than the backward record would write UNKNOWABLE here rather than OUT,
and the argument for it is stated above rather than buried.** This run writes OUT because
**[E1-02]** requires yardsticks *"prior to the act"* and there is no record to measure the new man
against at this company, and because **[E2-36]** puts "the manager is the plan" outside the
buyable class. **The operator may rule otherwise; the evidence for both readings is on this page.**

## Q4 — WILL IT SURVIVE? *(RECORDED, NOT GOVERNING — the file closed at Q2)*

### THE PERIMETER, AND THE CLEAN-YEAR COUNT — the brief's question, answered first

**The CNR rule governs every mean below: no multi-year mean crosses a perimeter event unless it
is rebuilt on one perimeter.** Twelve events are established from the filings, with dates:

| # | event | date | source |
|---|---|---|---|
| 1 | **BB&T and SunTrust merge**; registrant renamed Truist Financial Corporation | **2019-12-06** | the CIK's own former-name record; `sources.py:name_change_note` |
| 2 | **Securities book doubled**: AFS $74,727M → $120,788M → **$153,123M** | FY**2020**–**2021** | FY2020 and FY2021 10-K balance sheets |
| 3 | **Service Finance, LLC acquired for $2.0bn cash** ($1.2bn goodwill, $647M intangibles); **Constellation Affiliated Partners** acquired for the insurance segment | **2021-12-06** and **2021-07-01** | FY2021 10-K, Note 2 |
| 4 | **$59.4 billion of AFS securities transferred to HTM**, freezing a $3.7bn discount in AOCI | **Q1 2022** | FY2022 10-K, Note 3 |
| 5 | **20% of Truist Insurance Holdings sold for $1.9bn**, net proceeds taken to equity; **student loan portfolio sold** | **2023-04-03**; Q2 **2023** | FY2024 10-K Note 2; FY2023 10-K MD&A |
| 6 | **Goodwill impairment $6,078M** (CB&W and C&CB reporting units, 2023-10-01 test date) | **Q4 2023** | FY2023 10-K, Note 7 |
| 7 | **Remaining TIH stake sold** at an implied enterprise value of **$15.5bn**; the whole Insurance Holdings segment becomes discontinued operations and **every prior period is recast** | agreed **2024-02-20**, completed **2024-05-06**, recast published **2024-05-10** | 8-K `0000092230-24-000029` |
| 8 | **$27.7 billion of AFS securities sold at a $6,651M pre-tax / $5.1bn after-tax loss** | **Q2 2024** | FY2024 10-K MD&A |
| 9 | **Sterling Capital Management LLC sold** | **July 2024** | FY2024 10-K MD&A |
| 10 | **Marine and RV lending discontinued** | 2024–2025 | 8-K of 2026-09-15, EX-99.1 |
| 11 | **Income-statement line presentation changed and seven quarters recast**: restructuring charges dissolved into natural categories, card/deposit revenue lines renamed and regrouped, operating-lease income and depreciation moved | effective **2025-12-31**, published **2026-01-12** | 8-K `0000092230-26-000006` |
| 12 | **Regional Acceptance Corporation — $5.5 billion of auto loans, substantially all its assets — agreed to be sold**, with a stated plan to *"[r]eposition certain AFS securities to fully offset capital created from RAC sale"* | signed and furnished **2026-09-15**, four days before this run | 8-K `0000092230-26-000105` |

**HOW MANY CLEAN YEARS EXIST: ONE.**
- **2020** — first full post-merger year, CECL adoption ($3,140M added to the allowance), COVID
  provisioning of $2,335M. Not clean.
- **2021** — an $813M **negative** provision, the insurance segment still consolidated, two
  acquisitions closed. Not clean.
- **2022** — the $59.4bn AFS→HTM transfer, insurance still consolidated, a third insurance
  acquisition announced. Not clean.
- **2023** — the $6,078M goodwill impairment, the 20% insurance sale straight to equity, the
  student-loan sale, a $507M FDIC special assessment. Not clean.
- **2024** — the insurance disposal, a $6,939M gain in discontinued operations, a $6,651M
  securities loss, Sterling sold, and every prior period recast beneath it. Not clean.
- **2025** — **the only year on the post-disposal perimeter.** It carries a $130M legal accrual and
  a line-presentation change at 31 December, both disclosed and quantified. **Clean enough to
  read.**
- **H1 2026** — clean, but half a year, and the RAC disposal will move it again.

**The corpus's default window is FIVE YEARS [E2-42, E1-03], and Truist has ONE.** That is not a
reason to pick a different window and defend it — **[E4-38]** forbids exactly that — it is a
finding about the reliability of every figure in this file, and it is carried into Q5's range as
width rather than resolved by preference.

### Owner earnings — the bank CONVENTION, carried from Q3, with the window spread

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**

- **Five-year mean (2021-2025), all three constructions:** (i) CCB Δassets×leverage **$3,690M** ·
  (ii) ACNB organic split **$3,523M** · (iii) ΔRWA×CET1 **$3,147M**
- **Three-year mean (2023-2025), construction (iii):** **$2,702M**
- **The single clean year, 2025, construction (iii):** **$2,616M**
- **Spread, conservative end to optimistic end: $2,616M to $3,690M — a 41% range.**
- **Combined range used: $2.6 billion to $3.7 billion of bank owner earnings a year.**
- **Is that range too wide to reach a conclusion [E4-25]?** For a **yield** computation, no — the
  conservative end is usable and Q5 below uses it. For a **growth** claim, yes, and no growth claim
  is made. **The width's cause is named: it is the perimeter, not the business.** Every dollar of
  the $1.07 billion spread is traceable to whether a disposal that released regulatory capital is
  treated as earnings.
- **[E4-41], normalise the mean DOWN for luck:** the favourable exogenous breaks in the window are
  named and removed. The **$813M negative provision in 2021** (about $620M after tax) is a
  cycle release, not earnings, and it sits in the five-year mean; removing it takes the five-year
  (iii) mean to about **$3,023M**. The 2024 tax benefit of $556M from the securities loss is
  one-time and sits in 2025's cash taxes, not its book earnings. **The conservative end of the
  range, $2.6 billion, already excludes both, which is why it is the end Q5 uses.**
- **Maintenance capex — the DISCLOSED JUDGMENT.** **[E3-44]** and **[E2-41]** make D&A the default
  proxy for (c), and **[E5-20]** invalidates the D&A end for capital-intensive filers. **Neither
  applies to a bank and the run says so rather than pretending:** premises and equipment are
  **$3,177 million against $556,023 million of assets — 0.57%** — and a loan book does not wear
  out. The binding "maintenance" requirement is **regulatory capital**, which is what the (c)
  convention above measures, and the band displayed is the band across the three constructions
  rather than a D&A-to-capex band.
- **Stock compensation subtracted in full [E5-06]:** it already is. Share-based compensation is
  inside the $6,848 million personnel expense line; nothing is added back. **[E3-70]**'s
  grant-value test cannot be run at the margin here because Truist does not disclose a grant-date
  fair value of equity awards separately from total personnel expense in the 10-K; the proxy gives
  the named-executive figures only (the CEO's 2026 LTI target is $12.0 million against $6,848
  million of total personnel expense). **On any reading it is immaterial to a $5.3 billion earnings
  figure, and that is stated rather than implied.**

### Great, good, or gruesome? **[E4-20]**

- [ ] great — [x] **good, at best, and the incremental return cannot be established** — [ ] gruesome

**It is not gruesome. [E4-43] is the reason the distinction matters:** the good class *passes* —
*"nothing shabby about earning $82 million pre-tax on $400 million of net tangible assets."*
Truist earns money every year except the year it wrote off goodwill, requires capital to grow but
is not a bottomless pit, and returns more cash to owners than it retains.

**The return on RETAINED capital, which is the [E4-20] and [E5-40] test, straddles the boundary and
the honest answer is a range:**
- **Measured 2020 → 2025:** net income $4,581M → $5,307M, **+$726M**, against **$6,036M** of
  capital retained to hold the CET1 ratio (construction iii). **A 12.0% return on retention** —
  which **[E5-40]** calls *"quite satisfactory"* for retained capital in a regulated business.
- **Measured 2022 → 2025 on continuing operations:** net income from continuing operations
  $5,779M → $5,307M, **−$472M**, against $8,844M of risk-weighted-asset growth requiring roughly
  $940M of retained capital. **A NEGATIVE return on retention.**
- **The two answers disagree because the base year decides, which is precisely [E4-38]'s named
  disease** — *"growth-rate presentations can be significantly distorted by a calculated selection
  of either initial or terminal dates"* — and its remedy is to publish both, which is done here.
  **With one clean year on the perimeter, the incremental return on retained capital at Truist is
  not establishable from the filings, and that is recorded as the answer rather than resolved.**

**And the per-share series, which is the only one the owner actually holds:**
**diluted EPS from continuing operations $4.07 (2022) → $(1.40) (2023) → $(0.30) (2024) → $3.82
(2025)**, on a share count that fell 4.9% over the same period. **Tangible book value per share
$26.78 (2020) → $25.47 → $18.04 → $21.83 → $30.01 → $33.48 (2025) → $33.40 (2026-06-30)** — a
**4.6% a year** compound over five years, and **flat to down in the most recent half-year while
$3.0 billion was earned.**

### Staying power — score all three **[E5-11]**, and this is where Truist is genuinely strong

**(1) A large and reliable stream of earnings — MET, and it is the strongest part of the file.**
$14,423 million of net interest income in 2025, which is a spread on $400 billion of deposits and
does not depend on a product cycle, a customer concentration or a commodity price. Revenue has
been between $19.97bn and $20.52bn in every year since 2022 on the continuing perimeter. The one
loss year in the record, 2023, was a **non-cash** goodwill write-off; pre-provision net revenue was
positive in every quarter of the window, including the quarter of the $6,651 million securities
loss. Q2 2026 PPNR was **$2.26 billion**, about **$9.0 billion annualised**.

**(2) Massive liquid assets — MET.** From Table 33 of the FY2025 10-K:

| selected liquidity sources, 2025-12-31 | $M |
|---|---|
| unused borrowing capacity, Federal Reserve | 84,160 |
| unused borrowing capacity, FHLB | 23,464 |
| available investment securities (at fair value) | 70,150 |
| **available secured borrowing capacity** | **177,774** |
| eligible cash at the Federal Reserve | 29,973 |
| **total** | **207,747** |

*"At December 31, 2025, Truist Bank's available secured borrowing capacity represented
approximately **4.8 times** the amount of wholesale funding maturities in one year or less."* And
**[E5-39]**'s test — *"We will never be dependent on the kindness of strangers"* — is the one place
this must be read carefully: **$177.8 billion of the $207.7 billion is borrowing CAPACITY, not
cash.** It is the capacity to pledge securities to the Federal Reserve and the FHLB. Cash at the
Fed is **$29,973 million.** The corpus counts *"no bank lines … nothing depended on"*; a bank's
liquidity is constitutionally the opposite, and **the honest statement is that Truist's liquidity
is excellent by banking standards and does not meet [E5-39]'s standard, because no bank can.**
**[E2-61]**'s sector scope is the governing instruction: read the metric set the business type
selects.

**(3) No significant near-term cash requirements — MET, and this is the one that usually kills.**
Long-term debt $42,976M against $207.7bn of liquidity; short-term borrowings $26,885M of which
$17.6bn is FHLB advances, fully collateralised; time deposits over $250,000 maturing within three
months are **$8,140 million** and within twelve months **$10,589 million** of an $11,005 million
total — small against the liquidity. Parent-company cash is managed *"to exceed a minimum of 12
months of projected cash outflows."* **[E2-54]**'s coverage test is met with enormous margin:
total interest expense of $2,567 million a quarter against $3,620 million of net interest income
after paying it. **[E3-52]**'s terms test is the favourable reading: **$409 billion of deposits are
liabilities without covenants or due dates**, which is the float-like structure the corpus praises
— and the unfavourable reading is at the death below, because deposits have no due date and can
leave on any morning.

**Leverage, named and quantified [E4-16, E3-29] — there is no ratio ceiling in this framework and
the corpus supplies none.** Assets/common equity **9.5 : 1**; assets/tangible common equity
**13.8 : 1**; CET1 **10.9%** at 2026-06-30 against a **4.5% minimum plus a 2.5% stress capital
buffer = 7.0%**; total capital 13.8%; Tier 1 leverage 10.0%; supplementary leverage 8.3%. Both
Truist and Truist Bank are *"well-capitalized."* **Against [E3-29]'s "leverage of 20:1 … a common
ratio in this industry", Truist is at roughly half that, and the framework's conclusion is about
management, not the ratio — which is what Q3 did.**

### The loan book, the deposit book, and the securities book — the three Q4 exposures the brief names

**THE LOAN BOOK, and the concentration is not where the market looks.**

| 2025-12-31, $M | balance | % of loans HFI | 2025 net charge-off $M | implied NCO rate |
|---|---|---|---|---|
| **Commercial and industrial** | **167,808** | **51.0%** | 363 | **0.22%** |
| CRE | 23,720 | 7.2% | 129 | 0.55% |
| Commercial construction | 7,783 | 2.4% | (2) | n/m |
| Residential mortgage | 56,807 | 17.3% | 1 | 0.00% |
| Home equity | 9,719 | 3.0% | (6) | n/m |
| Indirect auto | 25,659 | 7.8% | 489 | 1.94% |
| Other consumer | 32,181 | 9.8% | 513 | 1.62% |
| Credit card | 4,918 | 1.5% | 218 | 4.43% |
| **total loans and leases HFI** | **328,595** | 100% | **1,705** | **0.54%** |

**COMMERCIAL REAL ESTATE MEASURED AGAINST THE REGULATORY GUIDANCE THRESHOLDS — and Truist passes
both by a very wide margin, which is a genuine and under-appreciated strength.** The interagency
CRE concentration guidance uses two screens against **total risk-based capital**, which for Truist
at 2025-12-31 is **13.8% × $443,257M = $61,169 million**:

| screen | threshold | **Truist** | |
|---|---|---|---|
| construction and land development ÷ total risk-based capital | **≥ 100%** | **$7,783M ÷ $61,169M = 12.7%** | passes with 87 points to spare |
| total CRE (including construction) ÷ total risk-based capital | **≥ 300%** | **$31,503M ÷ $61,169M = 51.5%** | passes with 249 points to spare |

**And the office exposure, which is the sector's live wound, is trivial here: CRE office is $2,435
million — 10.3% of CRE and 0.74% of total loans — down from $3,459 million a year earlier, with
non-performing office loans down from $228 million to $36 million.** Construction office is a
further $392 million. Multifamily is the largest CRE category at $8,055 million (34.0%). **CRE
non-performing loans fell from $298 million to $47 million in one year.** *The filer's own January
2025 slide put it in one line: CRE including construction was **9.4% of total loans**, weighted
average loan-to-value **63%**, and **75%** of it inside the south-eastern and mid-Atlantic
footprint.* **[E4-40]** warns against reading a benign loss history as safety — but this is
**exposure**, not experience: the balance is small, and a small balance cannot produce a large
loss.

**THE DEPOSIT BOOK AND THE UNINSURED SHARE.** Total deposits **$400,398M** at 2025-12-31 and
**$419,212M** at 2026-06-30 on the Call Report. The filer states it plainly: *"Approximately **62%
of deposits were insured or collateralized** at both December 31, 2025 and December 31, 2024. …
**The amount of deposits above the FDIC's insurance limit of $250,000 was $177.6 billion and
$170.7 billion** as of December 31, 2025 and 2024, respectively, calculated using the same
methodology as the Call Report for Truist Bank."* **$177.6 billion is 44.4% of deposits and 3.02×
common equity.** On the FDIC's own return, Truist Bank's uninsured share was **43.4% (2025-12-31)**
and **44.9% (2026-06-30)**, which is **third lowest of the nine** — Huntington 31.5%, Regions 39.6%,
**Truist 43.4%**, Fifth Third 44.5%, PNC 46.4%, Citizens 46.6%, M&T 49.7%, KeyBank 51.4%, U.S.
Bank 51.6%. Noninterest-bearing deposits are **25.8%** of the book and core deposits **90.6%** —
the latter the **second lowest** of the nine, after U.S. Bank's 90.0%.

**THE SECURITIES BOOK, INCLUDING HELD-TO-MATURITY — and this is the number that is not in the
equity account.**

| 2026-06-30, $M | amortised cost | fair value | **unrealised loss** | where it sits |
|---|---|---|---|---|
| AFS securities | 72,223 | 67,651 | **4,572** | in AOCI, and therefore in common equity and in CET1 |
| **HTM securities** | **46,351** | **38,145** | **8,206** | **nowhere — not in equity, not in CET1** |
| **total** | **118,574** | **105,796** | **12,778** | **21.8% of common equity** |

**The $8,206 million HTM loss is 14.0% of common equity and 20.3% of tangible common equity, and
it is invisible on the balance sheet.** It is the direct residue of perimeter events 2 and 4 — the
doubling of the securities book in 2020-2021 and the $59.4 billion transfer to held-to-maturity in
Q1 2022 that stopped the marks reaching the reported figures.

**AND HERE [E3-02]'S TEST — "test what this bank did while its peers were lax" — GIVES A HARD
NUMBER, BECAUSE TWO OF THE NINE DID NOT DO IT.** HTM unrealised loss as a percentage of common
equity at 2025-12-31, each figure from the filer's own securities note or its tagged data:

| | HTM amortised cost $M | HTM fair value $M | **unrealised loss $M** | **% of common equity** |
|---|---|---|---|---|
| U.S. Bancorp | 76,170 | 67,079 | **9,091** | **15.6%** |
| **Truist** | **47,186** | **39,130** | **8,056** | **13.4%** |
| Huntington | 15,258 | 13,636 | 1,622 | 7.5% |
| PNC | 70,105 | 67,979 | 2,126 | 3.5% |
| Citizens | 7,933 | 7,150 | 783 | 3.2% |
| M&T | 12,430 | 11,715 | 715 | 2.7% |
| KeyCorp | 8,622 | 8,313 | 309 | 1.7% |
| Regions | 5,606 | 5,584 | 22 | **0.1%** |
| Fifth Third | 11,368 | 11,404 | **(36) — a gain** | **(0.2)%** |

**Truist is the second worst of nine. Regions and Fifth Third have essentially no problem at all,
and Regions is the bank that earns 1.875% pre-tax on assets to Truist's 0.991%.** That is the
single tightest link between Q2's return finding and Q3's conformity finding: **the bank that did
not chase the 2020-2021 securities trade is the bank that earns the best return in the row**, and
**[E3-02]** is the corpus line that predicts it. *(PNC discloses the same mechanism and its size —
*"The amortized cost of held-to-maturity securities included net unrealized losses of $2.7 billion
at December 31, 2025, related to securities transferred, which are offset in AOCI"* — so the
transfer trick is not Truist's alone; the magnitude is.)*

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]**

**FIRST, THE CORPUS'S OWN WORKED BANK SCENARIO, RUN ON TRUIST'S OWN BOOK.** **[E3-24]**, 1990:
*"Consider some mathematics: … If 10% of all $48 billion of the bank's loans … produced losses
averaging 30% of principal, the company would roughly break even. A year like that — which we
consider only a low-level possibility, not a likelihood — would not distress us."*

| the [E3-24] scenario, applied to Truist at 2026-06-30 | $M |
|---|---|
| loans and leases held for investment | **329,796** |
| 10% of loans | 32,980 |
| × 30% severity = **net charge-offs in one year** | **9,894** |
| *for scale: Truist's worst actual year since the merger was 2024 at* | *1,803* |
| pre-provision net revenue, Q2 2026 annualised | **9,040** |
| allowance for loan and lease losses already held | 4,983 |
| **pre-tax result if the allowance is consumed and not rebuilt** | **+4,129** |
| **pre-tax result if the allowance is fully rebuilt in the same year** | **(854)** |

**The answer is the same one Buffett got: the company would roughly break even.** A $854 million
pre-tax loss is about $660 million after tax, or **1.4% of the $47,393 million of CET1 capital** —
CET1 falls from 10.9% to roughly 10.7% before any relief from shrinking risk-weighted assets.
**Likelihood: [x] a low-level possibility.** The scenario is **3.0% of loans charged off in one
year, 5.5× the worst year in this bank's post-merger history and 5.6× the 2025 rate.**

**SECOND, A HARDER SCENARIO BUILT FROM TRUIST'S OWN EXPOSURES RATHER THAN ITS EXPERIENCE
[E4-40], BECAUSE THE FIRST ONE DOES NOT THREATEN IT.** The three exposures that matter are the
51.0% commercial-and-industrial concentration, the $8.2 billion unrecognised HTM loss, and the
44.9% uninsured deposit share. Combine all three in one year:

| the compound scenario | $M |
|---|---|
| C&I losses at 3.0% of the book (13.6× the 2025 rate) | 5,034 |
| consumer losses (auto, other consumer, card) at 2× 2025 rates | 2,440 |
| CRE and construction at 3.0% (5.5× the 2025 rate) | 945 |
| residential and home equity at 0.5% | 333 |
| **total net charge-offs** | **8,752** |
| allowance rebuilt to 1.51% of a shrinking book | 4,983 |
| **provision required** | **~8,750** |
| PPNR down 20% on a deposit-cost squeeze and weaker fee income | **7,232** |
| **pre-tax operating result** | **(1,518)** |
| **plus: the HTM loss realised because uninsured deposits leave and securities must be SOLD rather than pledged** | **(8,206)** |
| **total pre-tax** | **(9,724)** |
| **after tax at 21%** | **(7,682)** |
| CET1 capital before | 47,393 |
| **CET1 capital after** | **39,711** |
| CET1 ratio on a risk-weighted-asset base shrunk to $400,000M | **9.9%** |
| **regulatory minimum plus the 2.5% stress capital buffer** | **7.0%** |
| tangible common equity before / after | 40,429 / **32,747** |
| **tangible book value per share before / after** | **$33.09 / $26.81** |

**AND THE CONCLUSION IS THE ONE THAT MATTERS, AND IT IS THE SAME SHAPE OF ANSWER THE SOFI RUN
REACHED BY A DIFFERENT ROUTE: TRUIST DOES NOT FAIL.** In a scenario that puts charge-offs at 2.7%
of loans — **five times the worst year in its history** — forces the entire held-to-maturity loss
into the open, and cuts pre-provision earnings by a fifth, **Truist still carries a 9.9% CET1 ratio
against a 7.0% requirement**, still has $207 billion of liquidity sources, and loses about **19% of
its tangible book value per share.** **Every leg of the scenario is pessimistic on purpose, and the
company survives every one of them.** The **[E3-24]** vocabulary for the compound scenario is **a
low-level possibility**, and the corpus's own conclusion about a bank in that position applies:
*"would not distress us."*

**Two refinements that make the scenario weaker still, stated because [E4-51] requires the bear
case to be one its holders would accept as fairly stated.** First, **the $177.8 billion of
"liquidity" is mostly the ability to PLEDGE securities to the Federal Reserve and the FHLB at par,
not to sell them** — which means a deposit run does **not** automatically crystallise the HTM loss,
and the 2023 regional-bank episode established that the Federal Reserve will lend against exactly
these securities. The HTM leg of the scenario therefore requires a liquidity event severe enough to
exhaust $177.8 billion of pledging capacity, which is a different and much rarer animal. Second,
**the FRB's own published stress result is better than my scenario:** *"The FRB has assigned Truist
an **SCB of 2.5%**, which was effective from October 1, 2025 to September 30, 2026"* — **2.5% is the
regulatory FLOOR**, which means the 2025 supervisory severely-adverse scenario produced a
peak-to-trough CET1 decline plus four quarters of planned dividends of **no more than 2.5% of
risk-weighted assets**, i.e. **about $11 billion**, against the $47.4 billion Truist holds. *(The
2.5% is a 2025-vintage result carried forward: on **2026-02-04** the FRB notified Truist that it
was extending the deadline for the 2026 SCB to **2027-10-01** because its October 2025 model
proposals were unresolved, so the next independent supervisory read is two years away. That is a
limit of the comparator and it is stated.)* **Truist's own published stress result and this run's
independent stress both say the same thing: the balance sheet holds.**

**SO WHAT IS THE DEATH? IT IS NOT INSOLVENCY. IT IS A PERMANENT STOP IN PER-SHARE COMPOUNDING, AND
THE MECHANISM IS THE PUBLISHED RETURN TARGET ITSELF.**

**[E2-27]** is the right lens — *"Viewed individually, each company's capital investment decision
appeared cost-effective and rational; viewed collectively, the decisions neutralized each other and
were irrational"* — but here the decisions are **disposals**, not investments, and what they
neutralise is the owner's claim. The mechanism, entirely from filed and furnished documents:

1. Truist has published a **15% ROTCE target for 2027** and a **16% to 18% long-term** target
   against a five-year mean of **11.5%** and a bank-level return on equity that is **last of nine**.
2. The published route includes *"Increase buybacks"* and *"Continue to optimize balance sheet and
   return significant capital to shareholders."* **ROTCE rises arithmetically when tangible common
   equity falls**, and tangible common equity falls when stock is retired.
3. The buyback is being funded, at the margin, by **selling businesses**: the insurance segment
   ($10.1 billion after tax, 2024), Sterling Capital (2024), the student-loan portfolio (2023),
   Marine/RV, and now **Regional Acceptance — $5.2 billion of net proceeds and $945 million of
   created CET1** — with the 2026 repurchase target **raised** from ~$4 billion to ~$5 billion in
   the same six months in which the revenue-growth guide was **cut** from +4-5% to +3.5-4%.
4. The arithmetic of the last five years is the proof that this is not a forecast: **common equity
   fell from $62,864 million to $60,273 million** while **$19,951 million was earned** and
   **$18,850 million was paid out**; **risk-weighted assets are $434,799 million at 2026-06-30,
   BELOW the $443,257 million of six months earlier**; the share count is down 9.4% from 2020; and
   **diluted earnings per share from continuing operations went $4.07 (2022) to $3.82 (2025)** on
   that smaller count. **Tangible book value per share compounded at 4.6% a year over five years and
   fell in the most recent half-year.**
5. **The end state is a smaller bank with a higher published ratio and an owner whose claim has not
   grown.** There is no quarter in which anything breaks, no covenant, no run, no regulator. The
   company is one of the ten largest banks in the United States and will be in 2036.

**Likelihood: [x] likely — because it is not a forecast about the future; it is a description of
the last five filed years, restated as the next five.** The falsifier is stated at Q6.

### THE SURVIVAL SHAPE — against `Screens/SURVIVAL SHAPES - index.md`

**PROPOSED, #27: THE BOUGHT RATIO.** *The published return target is reached by retiring and
selling the capital the return is measured against, rather than by earning more on it; each
disposal raises the ratio and lowers the business; nothing ever breaks, and the owner's claim
compounds at the rate of the share count rather than the rate of the bank.*

**Why it is not one of the twenty-six already in the index, argued against the three nearest:**
- **Not #5 THE SELF-LIQUIDATING DISTRIBUTION** (SWK, 2026-09-12, *"the dividend is paid by selling
  the business"* **[E2-60]**). Two differences. The payout here is **a buyback, not a dividend**,
  which is what makes it accretive to the published metric rather than merely distributive; and the
  assets sold are **deliberately the worst ones** — Regional Acceptance's *"pre-tax earnings were
  approximately breakeven through the six months ended June 30, 2026"* on its own furnished slide,
  and the disposal *"[r]educes NPLs by >10 bps … and NCOs by ~10 bps annually."* **Each disposal
  genuinely improves the bank that remains.** #5 describes a business being consumed; #27 describes
  a business being **improved into a smaller one whose ratio is better and whose earnings are not.**
- **Not #24 THE BOUGHT AVERAGE** (BLK, 2026-09-19). #24 is the inverse: BlackRock **buys** higher-
  priced businesses with its own shares so a falling unit price reads flat, and the owner pays in
  dilution. Truist **sells** businesses and retires shares so a flat earnings stream reads as a
  rising ratio, and the owner pays in scale. **In #24 the share count rises; in #27 it falls, and
  that is the mechanism rather than a mitigant.**
- **Not #26 THE MARKED BOOK** (SOFI, 2026-09-19). The two share their conclusion — *"what stops is
  the per-share compounding"* — and nothing else. SoFi's earnings are a valuation that has not been
  collected and it funds growth by **issuing** equity; Truist's earnings are cash, collected, and it
  **retires** equity. **They are opposite ends of the same finding, which is worth recording as the
  project's second instance of a bank that does not fail and does not compound.**

**Its tells are checkable on any filer, which is the test the index sets:** a published forward
return-on-equity target materially above the filer's own trailing multi-year mean, with buybacks or
disposals named among the drivers; risk-weighted assets flat or falling while the share count
falls; common equity lower at the end of a five-year window than at the start despite cumulative
profits; earnings per share flat or down on a reduced share count; and disposal proceeds and
capital "created" by disposals being cited in the same document as the repurchase target.

**The mechanism that could actually kill Truist, recorded beside the shape rather than instead of
it,** is the ordinary one: **#11 THE PASS-THROUGH** as a feature — the deposit franchise is a
commodity the bank prices against eight equals, its noninterest-bearing share has fallen from 35.0%
to 25.8%, and the spread is re-competed every time rates move. That is a compression, not a death.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE** *(RECORDED, NOT GOVERNING)*

**Q4 is IN and the run says so without hedging: this business survives.** Three strengths met,
CET1 at 10.9% against a 7.0% requirement, $207.7 billion of liquidity sources, CRE at 51.5% of
total capital against a 300% threshold, office at 0.74% of loans, an allowance that covered the
following two years' charge-offs 1.37× to 1.94× in every test, a published pessimistic-scenario
reserve sensitivity, and both my stress and the regulator's leaving it comfortably capitalised.
**What Q4 cannot establish, and says so, is the LEVEL of owner earnings on a five-year mean, because
only one clean year exists on the current perimeter [E2-42, E4-25].** The range is carried into Q5
as width.

---

# COMPUTATION — NOT A CLEARANCE

**Operator rule 3.** ⛔ **Q5 did not open.** Q1 is IN; **Q2 is OUT on the business** and Q3 is OUT
at gate weight; the file is closed. What follows is arithmetic produced only because the brief
required a below-gate computation for a bank, it carries the mandatory heading, and **it carries no
entry language of any kind.** No price alert is armed and no `PORTFOLIO.md` row is written, because
a name that failed at Q2 failed on the **business** and a price alert on it would be a category
error (the QLYS ruling, 2026-09-07).

**The inputs, all restated from above:** price **US$48.56** (close of 2026-09-18, aggregator,
flagged); shares **1,221,626,188** (cover of the Q2 2026 10-Q, accession `0000092230-26-000099`);
market capitalisation **US$59,322.2 million**; sovereign **5.34%** (US Treasury daily par yield
curve, 30-year, 2026-09-18, issuing authority).

**1. THE YIELD — bank owner earnings against the bond**

| construction | owner earnings $M | ÷ market cap | **yield** | sovereign | **points over** |
|---|---|---|---|---|---|
| **(iii) ΔRWA × CET1, single clean year 2025 — the conservative end** | **2,616** | 59,322 | **4.41%** | 5.34% | **−0.93** |
| (iii) three-year mean 2023-2025 | 2,702 | 59,322 | 4.56% | 5.34% | −0.78 |
| (iii) five-year mean 2021-2025 | 3,147 | 59,322 | 5.31% | 5.34% | −0.03 |
| (ii) ACNB organic split, five-year mean | 3,523 | 59,322 | 5.94% | 5.34% | +0.60 |
| **(i) CCB Δassets × leverage, five-year mean — the optimistic end** | **3,690** | 59,322 | **6.22%** | 5.34% | **+0.88** |
| *for reference only: net income available to common, 2025, with NO charge for retained regulatory capital* | *4,974* | *59,322* | *8.39%* | *5.34%* | *+3.05* |
| *for reference only: the same, H1 2026 annualised* | *5,800* | *59,322* | *9.78%* | *5.34%* | *+4.44* |

**The whole result sits in the gap between the two reference rows and the five rows above them, and
the gap IS the (c) convention.** On a plain earnings yield Truist looks like an 8-10% asset against
a 5.34% bond. **Charge the business for the regulatory capital it must retain to keep its capital
ratio constant while it grows — which is what [E2-23]'s "requires to fully maintain … its unit
volume" means for a balance-sheet business — and the yield falls to between 4.41% and 6.22%,
straddling the bond.** The convention is confessed at Q3 and it is doing the work here; a reader who
rejects it gets the reference rows instead, and the run says so rather than hiding it.

**2. WHAT THE PRICE ALREADY ASSUMES**

Solving $59,322M = owner earnings ÷ (10% − g) for the perpetual growth the quote requires at the
**[E4-28]** floor rate:

| | owner earnings $M | **perpetual growth required to justify $48.56 at a 10% discount rate** |
|---|---|---|
| conservative end | 2,616 | **5.59% a year, for ever** |
| five-year mean (iii) | 3,147 | 4.69% |
| optimistic end | 3,690 | **3.78% a year** |

**What the business has actually done, measured three ways over the perimeter-complete window:**
tangible book value per share **+4.6% a year** (2020-2025, and **negative** in H1 2026); **diluted
EPS from continuing operations $4.07 (2022) → $3.82 (2025), −2.1% a year**; risk-weighted assets
**+3.2% a year** (2020-2025) and **falling** in H1 2026. **The conservative end needs 5.59% for
ever from a business whose per-share earnings have gone backwards for three years and whose
risk-weighted assets shrank in the most recent half-year. [E4-44]** is the bound: *"the value of an
asset, whatever its character, cannot over the long term grow faster than its earnings do."*
**[E4-35]** supplies the base rate for anything better: *"fewer than 10 of the 200 most profitable
companies in 2000 will attain 15% annual growth in earnings-per-share over the next 20 years."*
Truist is not claiming 15%; it is claiming **16-18% ROTCE**, which is a different number, and the
route it publishes to get there is partly the buyback.

**3. WHAT YOU ARE PAID** — **−0.93 to +0.88 points over the sovereign** on the owner-earnings
construction; **+3.05 to +4.44 points** if the regulatory-capital charge is refused. **On the
conservative construction the buyer is paid LESS than the thirty-year Treasury.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** Sovereign used **5.34%, the bare
rate, no per-name premium added.** Certainty is handled twice and neither place is the rate: at the
understanding gate (Q1, which passed) and in the discount to value demanded at the end. It is priced
**once** **[E4-11, E4-48]**. **Windage count: ONE** — the choice of the conservative end of the
owner-earnings range. No additional end margin is applied, because the bar used below is the
screamer test, which adds none.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — at the **[E4-28]** floor rate of 10%, which is the
rate the corpus says it quits on:

| | $M | **per share** |
|---|---|---|
| **conservative** (2025 owner earnings on construction iii, capitalised at 10%) | 26,160 | **roughly $20 to $25** |
| **middle** (five-year mean, construction iii) | 31,470 | roughly $25 to $30 |
| **optimistic** (five-year mean, construction i, the loosest defensible charge for capital) | 36,900 | **roughly $30 a share** |
| *if the regulatory-capital charge is refused entirely and 2025 net income is capitalised at 10%* | *53,070* | *roughly $40 to $45* |
| *the same on H1 2026 annualised earnings* | *60,600* | *roughly $50* |
| **current price, 2026-09-18** | **59,322** | **$48.56** |

**THE RANGE IS $20 TO $50 A SHARE, AND THAT IS THE HONEST OUTPUT [E4-25].** *"Usually, the range
must be so wide that no useful conclusion can be reached."* **Here it is, and the cause is named
rather than averaged away: it is whether a bank's retained regulatory capital is an expense or an
investment, compounded by the fact that ONE clean year exists on the current perimeter.** Under
**[E4-25]** the verdict on the arithmetic is that **no useful conclusion can be reached about the
value**, and the price sits at the top of the widest defensible band.

**THE FLOOR, BEFORE ANY RANKING [E4-28, E3-13].** *"that's the figure we quit on."* **Honest pre-tax
expectancy at $48.56: about 6% at the conservative end (4.41% yield plus about 2% of achievable
growth) and about 9% at the optimistic end (6.22% plus about 3%). Call it about 8%. Below roughly
10% on every construction, so the name is not ranked — it is quit on**, whatever the sovereign is,
and the ranking lines are not filled in. **This is the same answer the Chubb, Coca-Cola, Griffon and
ACNB runs of 2026-09-19 reached from four different businesses, and the third time today that a name
clearing or nearly clearing the bond has failed the floor.**

**WHICH BAR — [x] the screamer test [E4-01].** Does the price already clear the **conservative**
case? **No: $48.56 against a conservative case of roughly $20 to $25.** Three outcomes, and this is
the third: **above the whole conservative range → no.** *"it ought to just kind of scream at you"*
**[E3-25]** — nothing here does.

**COMPUTATION VERDICT: the floor is failed and the bond is failed at the conservative end. No
clearance of any kind is implied or given.**

---

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? *(there is no position; this is the reversal record)*

**Pre-committed before entry [E1-02]** — and since the file closed at Q2 on the business, these are
**the conditions under which the Q2 verdict would have to be revisited**, not exit triggers. The
QLYS ruling of 2026-09-07 requires them in words rather than as armed price bands, and no band is
armed.

**THESIS-CONFIRMING METRICS (each would confirm Q2 OUT):**
- Return on average assets stays below the nine-bank median on the **FDIC's own** definitions.
  *(2021-2025 mean: Truist 0.991% pre-tax, median Huntington 1.418%, best Regions 1.875%.)*
- The noninterest-bearing deposit share keeps falling from **25.8%**.
- Risk-weighted assets flat or falling while the share count falls — the **#27 THE BOUGHT RATIO**
  tell. *(RWA $443,257M → $434,799M and shares 1,262,470k → 1,221,626k in H1 2026: both fell.)*
- Diluted EPS from continuing operations fails to exceed **$4.07**, its 2022 level, in any year
  through 2028.

**THE THESIS-BREAKING METRIC AND ITS THRESHOLD — the one that would force a re-run:**
> **Truist Bank's pre-tax return on average assets, on the FDIC Call Report, reaches the
> nine-bank median (about 1.42%) and stays at or above it for THREE consecutive full years, while
> the noninterest-bearing deposit share stops falling.** H1 2026's **1.350%** is the first
> half-year of such a run and it is already close. **One year is not three**, and the reason the
> threshold is three is **[E4-17]**: *"those beliefs change quite gradually."*

**The second breaker, and it is about the man rather than the numbers, which is why it is written
separately:** if Michael Lyons's *"broader strategic review"* produces **a large acquisition paid
for in Truist stock**, the Q2 verdict does not need revisiting — it is confirmed, and **[E5-44]** is
the reason: *"the intrinsic value of the shares you give in an acquisition must not be greater than
the intrinsic value of the business you receive."* At a quote above this run's whole conservative
value range, Truist paper is not cheap currency. His public record is *"more than $15 billion of
strategic acquisitions"* at PNC. **This is a named, dated, falsifiable prediction about the next two
years and it is on the record before the fact [E1-02].**

**NEXT CATALYST DATES:** Q3 2026 results, expected mid-October 2026 (the pattern is the 17th–21st),
which will carry the first quarter under the new chief executive and the closing of the Regional
Acceptance sale *"in late 3Q26 or early 4Q26"*; the FY2026 10-K in late February 2027; and the
**2027 supervisory stress test**, which is the next independent read on the capital position after
the FRB's 2026-02-04 extension.

**THE SELL RULE [E2-28]** — not applicable, no position. **[E4-24]** is recorded instead, because it
is the corpus's answer to exactly this situation: *"if you really think you're in with people that
have got a good business, but they're going to keep doing dumb things with your money, you'll
probably do better to get out"* — with **[E4-49]**'s base rate on engagement, *"Worse than poor."*

**Position size: ZERO.** No entry. The capital-allocation flag at Q3 would have bound size downward
even if the gates had cleared.

- **VERDICT: [x] IN** *(the reversal conditions are written, dated and falsifiable, which is what
  this question asks for)*

---
## WHAT THIS RUN LEAVES BEHIND FOR THE FRAMEWORK, AND FOR JPM

**Five items, in the order a later session will need them.**

1. **THE BANK (c) CONVENTION HAS NOW PASSED THREE INDEPENDENT TESTS AND FAILED A FOURTH, AND THE
   FAILURE IS SPECIFIC.** CCB adopted **(c) = Δassets × the Tier 1 leverage ratio**; ACNB added the
   organic/acquired split; SOFI's fold recorded that it reproduced itself from the equity account
   and should be *"adopted with a ledger row or refused rather than re-invented a third time."*
   **Truist breaks the Δ-total-assets form**, and the way it breaks is instructive rather than
   fatal: in 2024 Truist's total assets **fell** $4,173 million because a disposed segment left the
   balance sheet, so the CCB form prints **$5,278 million** of owner earnings — **the highest of the
   six years — in the year the company realised a $6,651 million securities loss.** The fix used
   here is **(c) = Δ(risk-weighted assets) × the CET1 ratio**, which the company itself uses in
   public (*"Creates $945MM or 22 bps of CET1 capital"*). **Recommendation for the operator: adopt
   the convention with a ledger row, in the RWA/CET1 form, with the Δassets form kept as the
   fallback for filers that do not publish risk-weighted assets.** Both are computed in
   `Test Runs/_research 2026-09-19 TFC/arith.py` and both are reported above.
2. **THE VINTAGE TRAP IS REAL AND IT CAUGHT THIS RUN'S OWN Q2 TABLE.** `companyfacts` returns the
   **latest** vintage of a restated balance-sheet date. Truist's goodwill at 2022-12-31 is
   **$23,233 million** in companyfacts and **$27,013 million** on the FY2022 10-K's own balance
   sheet — a $3,780 million difference that is the Insurance Holdings goodwill later moved to
   discontinued operations. **Any ROTCE or tangible-book computation for a filer with a
   discontinued-operations recast must use the as-filed capital table, not the tagged data.** The
   correction is recorded in full at Q3; the ranking did not change. **For JPM this matters less
   (no comparable recast), but the check costs one grep.**
3. **AN FDIC API DEFECT, FOUND AND FIXED HERE.** `banks.data.fdic.gov/api/institutions` with
   `search=NAME:"..."` is a **full-text** match, not an exact one. A first pass that searched
   `"TRUIST BANK"` and took the largest match by assets returned **JPMorgan Chase Bank, CERT 628**;
   `"CITIZENS BANK"` returned **Wells Fargo Bank, CERT 3511**; and `"KEYBANK"` and
   `"MANUFACTURERS AND TRADERS TRUST"` returned **nothing at all**. A row built that way is wrong
   and looks entirely plausible. **The correct call is `filters=NAME:"<exact legal name>" AND
   ACTIVE:1`, verified against city and state**, and the nine CERTs are recorded in
   `fdic_certs.json` for reuse: Truist 9846, PNC 6384, U.S. Bank 6548, Fifth Third 6672, KeyBank
   17534, Regions 12368, Citizens 57957, M&T 588, Huntington 6560. **JPMorgan Chase Bank NA is CERT
   628, established here by accident.**
4. **THE ACNB "CALL REPORT FIRST" RULING NEEDS A SIZE SCOPE.** For ACNB the Call Report was the only
   instrument that could see 56 competing institutions, most of them private or mutual. For a
   $556 billion bank the competitor set is nine SEC registrants and the Call Report adds a *second
   uniform measurement* rather than a hidden competitor — which turned out to be worth more, because
   **it moved Truist from 8th of 9 to LAST of 9 on both return measures.** Proposed refinement:
   *build the Call Report row always; treat it as the primary row where the footprint contains
   material non-filers, and as the confirming row where it does not.*
5. **[E2-67] HAS NO MANDATED BANK EQUIVALENT, AND THIS RUN FOUND THE BEST AVAILABLE SUBSTITUTE.**
   The SOFI fold recorded that a fair-value lender has no reserve table at all. Truist supplies the
   other end of the range: **a published, annually repeated, dollar-quantified statement of what a
   pessimistic macroeconomic scenario would add to the modelled allowance — $2.1bn, $2.2bn, $2.2bn,
   $2.2bn, $2.4bn for 2021 through 2025.** It is not a reserve-development triangle and it is not a
   model backtest, but it is the filer stating in dollars how wrong its central estimate could be,
   with the direction named. **Proposed: treat the ACL scenario sensitivity as the bank analogue of
   [E2-67]'s table, and record its absence as a candor gap where a bank does not publish one.**

---
## SELF-AUDIT

- [x] **Questions answered in order; no verdict skipped.** Q1 IN → **Q2 OUT (the file closes)** →
      Q3, Q4 recorded and explicitly marked NOT GOVERNING at the head of each → Q5 did not open and
      appears only under `COMPUTATION — NOT A CLEARANCE` → Q6 recorded as the reversal record.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN and Q4 IN
      (recorded) rest entirely on filed documents named with accession numbers. The moat class at Q2
      is **NONE, not PROVISIONAL**, and the one gap in the competitor row (M&T's cost of deposits
      before 2025, which it does not tag separately) is stated in the row and does not bear on the
      verdict in either direction.
- [x] **Every UNRESEARCHED verdict names the artifact.** There are none.
- [x] **Every UNKNOWABLE verdict states what cannot be known.** There are none. **Two places where
      UNKNOWABLE was considered and rejected are stated in the open**: Q3, where a reader who judges
      the eighteen-day-old chief executive rather than the record would write UNKNOWABLE (the
      argument is printed in full beside the OUT), and Q4's incremental return on retained capital,
      which is recorded as **not establishable** inside an IN verdict on survival rather than used to
      fail the gate.
- [x] **Step 0: the filing was read, with accession numbers; a figure was cross-checked.** Six
      10-Ks, two 10-Qs, three proxies and eight 8-K exhibit sets, all listed with accessions. Equity
      recomputed from **A − L** per **[E5-32]**: $556,023M − $491,928M = **$64,095M**, exactly the
      filed total. Second cross-check on the figure that drives Q3: average common equity
      recomputed from period-end balances gives **$59,023M** against the filer's daily average of
      **$58,902M**, a 0.2% agreement.
- [x] **Owner earnings on a multi-year mean; window stated; the capex band disclosed as a
      judgment.** Three constructions, three windows (one year / three years / five years), the
      **41% spread reported as the range**, and the reason for the width named (the perimeter, not
      the business). The (c) guess is confessed as a **CONVENTION** under PRIME RULE 3 at Q3, with
      the departure from CCB's form stated and justified from Truist's own filings, as the brief
      required.
- [x] **Competitor row filled.** **TWO rows, nine banks, five years**: one computed on a single
      specification from tagged annual statement values and validated against the subject's own
      filed ROTCE (12.28% computed vs 12.7% published, gap explained); one from the **FDIC Call
      Report**, from the issuing authority, with every CERT verified by exact name.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** 5.34%, USD,
      US Treasury daily par yield curve 30-year, 2026-09-18. FRED not used.
- [x] **Value stated as a round-number range, not a point estimate.** Roughly $20 to $50 a share
      across the defensible constructions, and **[E4-25]**'s conclusion drawn from the width.
- [x] **One bar chosen, not both; windage count stated.** Screamer test **[E4-01]**; windage count
      **ONE** (the conservative end of the owner-earnings range); no end margin added.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $48.56 close of
      2026-09-18 from `tools/sources.py:price`, flagged; year-end closes used only for the
      **[E3-54]** market-value leg, flagged there too.
- [x] **Run committed to git** — five commits, each with a pathspec, under the write-early protocol:
      the claim, Step 0+Q1, Q2, Q3, Q4, and this closing section.
- [x] **The CGNX ruling of 2026-09-07 honoured:** the furnished 8-K EX-99.1 earnings releases were
      pulled and read **before** scoring **[E4-29]** and **[E4-22]**'s third flag — and it mattered.
      **[E4-29]** reads clean (EBITDA: zero occurrences in the 10-K, the proxy, the release and the
      deck), but **[E4-22]**'s third flag fires **only in the furnished material**: the 15% ROTCE
      target for 2027 and the 16-18% long-term target exist in the EX-99.3 slide deck and in the
      forward-looking-statements paragraph, and **nowhere in the 10-K.** A run that read only the
      annual report would have scored the projections flag clean.
- [x] **`python tools/check_framework.py` PASSES** — see the line below this block.

## REGISTER

- **Verdict: [ ] IN  [x] OUT (about the BUSINESS)  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
- **One line:** *Truist Financial (TFC) — **FAIL AT Q2, OUT ON THE BUSINESS**: on the FDIC's own
  uniform definitions Truist Bank has the **worst five-year mean pre-tax return on assets (0.991%
  against Regions' 1.875%) and the worst five-year mean return on equity (7.03% against 13.86%) of
  the nine largest regional banks in the United States**, from mid-pack funding costs (4th of 9),
  a mid-pack margin (5th of 9) and mid-pack leverage (13.3× tangible), with number-one deposit share
  in exactly one of its fourteen states, free deposits down 28% and branches down 31% in five years,
  and its own 10-K saying *"We expect that competition will only intensify in the future."*
  **Q3 recorded OUT at gate weight on [E3-29]** (the merger's $1.6bn cost-save yardstick reaffirmed
  twice and then never reported against; pay metrics that add back the $5,090M securities loss and
  the $6,078M goodwill impairment while the 2024 bonus paid 95% of target; three of four
  institutional-imperative behaviours; a published 16-18% long-term ROTCE target against an 11.5%
  five-year record) **— with the fact that decides how much weight to give it: the chief executive
  changed on 2026-09-01, eighteen days before this run.** **Q4 recorded IN on survival** — CET1
  10.9% against a 7.0% requirement, CRE at 51.5% of total capital against a 300% threshold, office
  at 0.74% of loans, and a stress five times the worst year in its history still leaving CET1 at
  9.9%. **Twelve perimeter events; ONE clean year.** Price **US$48.56** (2026-09-18), shares
  **1,221,626,188** (Q2 2026 10-Q cover, `0000092230-26-000099`), cap **US$59,322.2M**, sovereign
  **5.34%**. Below-gate computation fails the ~10% **[E4-28]** floor **and the bond** at the
  conservative end (yield 4.41%, −0.93 points). **Proposed survival shape #27, THE BOUGHT RATIO.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable. *(The two places UNKNOWABLE was weighed are named in the
  self-audit above.)*
- **Alerts and PORTFOLIO row: NONE, and deliberately.** The name failed at Q2 on the business, so
  the QLYS ruling of 2026-09-07 applies: no band in `tools/alerts.json`, no `PORTFOLIO.md` row, and
  the reversal condition recorded in words at Q2 and Q6 instead.
- **The strongest single fact AGAINST this run's conclusion, repeated here so the register carries
  it [E4-51]:** *on the FDIC's own numbers Truist Bank's efficiency ratio in the first half of 2026
  is **52.990%, the best of all nine banks**; its pre-tax return on assets has gone 0.874% → 1.248%
  → 1.350% in six quarters; its own reported ROTCE has gone 13.3% → 12.7% → 13.8% → **15.4%**; and
  the management that produced the five-year record left on 2026-09-01 having earned **nothing** on
  its 2023-2025 long-term award. If the last six quarters continue for three years, the Q2 verdict
  is wrong.* The threshold that would prove it is written at Q6 and it is three years, not one.

---
## ADDENDUM, 2026-09-19, WRITTEN AT THE FOLD — two corrections to this file, made here and NOT by editing it (operator rule 6)

**1. THIS IS THE FIFTH BANK THE PROJECT HAS RUN, NOT THE FOURTH. The header of this file says
"THE FOURTH BANK", and that is wrong.** The brief said fourth, and at dispatch it was defensible —
CCB, ACNB and SOFI were folded earlier in the day and JPM's run file said RUN IN PROGRESS. **By
the time this file was folded, JPM had been folded as register entry 130 and its own entry claims
"the FOURTH bank this project has run", which is correct.** The order is **CCB (first, Q2 OUT) →
ACNB (second, all four gates IN, Q5 OUT on price) → SOFI (third, Q2 OUT) → JPM (fourth, all four
gates IN, Q5 OUT on price) → TFC (fifth, Q2 OUT)**. Counted from the register rather than from the
brief, exactly as the SOFI fold required after the same mistake — **the third consecutive bank run
whose brief mis-stated the count.**

**2. THE PROPOSED SURVIVAL SHAPE IS #29, NOT #27.** Q4 of this file proposes **THE BOUGHT RATIO**
as #27. Between dispatch and fold, **JPM took #27 (THE LICENCE) and OTTR took #28 (THE CONVERTED
WINDFALL)**, both on 2026-09-19. `Screens/SURVIVAL SHAPES - index.md` now carries 29 rows with a
maximum number of 28, so **THE BOUGHT RATIO is entered in the index as #29**, and the collision is
recorded rather than resolved by renumbering anyone (the same treatment OTTR gave its own
collision with JPM in the same hour). **The index is the authority on the number; this file is the
authority on the mechanism.**

**Neither correction changes a verdict.** Q1 IN, **Q2 OUT on the business**, Q3 OUT recorded at gate
weight, Q4 IN recorded on survival, the below-gate computation failing the ~10% **[E4-28]** floor and
the bond at the conservative end, and Q6's reversal conditions all stand exactly as written.

**AND ONE FINDING OWED BACK TO THE JPM RUN, WHICH FINISHED WHILE THIS ONE WAS WRITTEN, BECAUSE THE
TWO ANSWER EACH OTHER.** JPM's fold records that **JPMorgan's HTM securities stood at 1.40× equity
at 2022-12-31, the LOWEST of the seven institutions it tested, against SVB's 5.91×** — its
**[E3-02]** conformity test, passed. **This file's equivalent test, on the nine largest regional
banks at 2025-12-31, gives the other end of the same distribution: Truist's unrecognised
held-to-maturity loss is $8,056 million, 13.4% of common equity, second worst of nine — and
Regions, which has essentially none (0.1%), earns the best return in the row (1.875% pre-tax on
assets against Truist's 0.991%).** Taken together the two runs establish the same thing from
opposite directions: **among American banks in 2020-2022, the securities decision separates the
returns, and [E3-02] is the line that predicts it.** That is worth more than either run's own
finding and it is recorded in both folds.
