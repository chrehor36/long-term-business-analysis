# Company Run — ACNB Corporation (ACNB) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**THIS IS A BANK, AND THE CORPUS RUNS A BANK DIFFERENTLY.** Four rules govern the file and
are declared here before any number: **Q3 is the deciding gate, not an overlay** — *"Because
leverage of 20:1 magnifies the effects of managerial strengths and weaknesses, we have no
interest in purchasing shares of a poorly-managed bank at a 'cheap' price. Instead, our only
interest is in buying into well-managed banks at fair prices"* **[E3-29]**, the one place in
the framework where cheapness is ruled out as a remedy. **The named failure mode is
conformity** **[E3-02]**. **Reserves are where dishonesty hides** **[E2-50]**, so the
allowance and provisioning record is judged against subsequent charge-offs and against the
candor benchmark **[E2-67]**. **Survival is a quantified stress, not a ratio** **[E3-24]**;
there is no leverage ceiling in this framework and the corpus supplies none. And **owner
earnings by the ordinary construction does not work for a bank** — this run states how it
measures return on equity capital employed **[E2-01]** and confesses the construction as a
**CONVENTION** under PRIME RULE 3 at Q3 and Q4 below.

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
## SUMMARY — the verdict line, before the evidence

| | |
|---|---|
| **Q1 understand** | **IN** |
| **Q2 franchise** | **IN — class NARROW, direction MIXED** |
| **Q3 honest and rational** | **IN at GATE weight (leverage and daily execution both ticked). No disqualifier found.** |
| **Q4 survive** | **IN — GOOD, not great [E4-20, E4-43]** |
| **Q5 price** | **OUT ON PRICE — quit on at the ~10% floor [E4-28]. Honest pre-tax expectancy 8.1–8.9% against a 5.34% sovereign.** |
| **Q6 falsifiers** | **IN — pre-committed below; watch-list only, nothing armed** |

**Price US$64.57** (2026-09-18 close, `tools/sources.py price()`, **aggregator FLAGGED**)
**× 10,169,930 shares** (cover of the 10-Q for the quarter ended 2026-06-30, accession
`0001628280-26-054143`: *"The number of shares of the Registrant's Common Stock outstanding
on July 30, 2026, was 10,169,930"*; **issued 11,079,210 against 10,169,930 outstanding, so
909,280 treasury shares are correctly excluded**; split factor after 2026-06-30 = 1.0;
no post-cover issuance found in the two 8-Ks filed since, and the only post-cover share
action available under the live plan is a **repurchase**, which would lower the count, so
10,169,930 is the conservative denominator) **= market capitalisation US$656.7 million.**
**Sovereign 5.34%**, USD, **US Treasury daily par yield curve, 30-year, 09/18/2026**, struck
fresh this session from the issuing authority, **not FRED**.

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34** % · date **09/18/2026** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year**, via `tools/sources.py sovereign('USD')`. ACNB earns and reports
  entirely in USD from nine counties in Pennsylvania and Maryland; there is no FX leg and no
  ADR ratio to derive. **[E3-66]** does not bite: this is a US registrant whose shareholders
  stand in the US queue.
- FX if the quote and the earnings differ in currency: **N/A** · ADR ratio, derived: **N/A**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Documents read in full this session, with dates and accession numbers:**

| document | period | filed | accession |
|---|---|---|---|
| **10-K** | FY2025 | 2026-03-12 | `0001628280-26-017229` |
| **10-K** | FY2024 | 2025-03-14 | `0000715579-25-000030` |
| **10-K** | FY2023 | 2024-03-14 | `0000715579-24-000028` |
| **10-K** | FY2022 | 2023-03-03 | `0000715579-23-000015` |
| **10-K** | FY2021 | 2022-03-14 | `0000715579-22-000018` |
| **10-Q** | Q2 2026 | 2026-08-06 | `0001628280-26-054143` |
| **8-K EX-99.1** earnings release | Q2 2026 | 2026-07-23 | `0001628280-26-049299` |
| **8-K EX-99.1** earnings release | Q1 2026 | 2026-04-23 | `0001628280-26-026708` |
| **8-K EX-99.1** earnings release | Q3 2025 | 2025-10-23 | `0001628280-25-045974` |
| **8-K EX-99.1** earnings release | Q4/FY2025 | 2026-01-22 | `0001628280-26-002992` |
| **8-K EX-99.1** + Item 2.01, Traditions closing | 2025-02-01 | 2025-02-03 | `0001104659-25-008408` |
| **DEF 14A** proxy | 2026 meeting | 2026-03-30 | `0001104659-26-036515` |

  *The **four** earnings releases were pulled deliberately, under the CGNX companion rule of
  2026-09-07: a run that reads only the annual report will score clean a company that has
  built its public narrative on a non-GAAP metric.*

- **figure cross-checked against the filed statement:** **net income FY2025 of $37,051
  thousand**, read at the **Consolidated Statements of Income** in the 10-K and matched
  against three independent places in the same filing — the MD&A summary table, the
  Consolidated Statements of Changes in Stockholders' Equity, and **Note 22 Segment and
  Related Information, where $37,805 (Banking) + $620 (Insurance) − $1,374 (holding company
  and eliminations) = $37,051.**
- **Second cross-check, the [E5-32] one — the filed statement is not bedrock, so equity was
  recomputed from A − L:** total assets $3,228,126 − total liabilities $2,808,152 =
  **$419,974**, identical to the reported stockholders' equity. **Book value per share
  recomputed independently for 2022 as $28.78 against the FY2022 10-K's own five-year table
  figure of $28.78** — an exact match on a year this session did not take from tagged data.
- *If the filing could not be obtained → **UNRESEARCHED**. Name the ladder rung that failed
  and the obstacle.* **No rung failed.** One tooling note is recorded at the self-audit:
  `tools/sources.py:_get()` defaults to `WEB_UA` and `www.sec.gov/Archives` answers that with
  HTTP 403, so every primary fetch in this run was made with `headers=SEC_UA` — the defect
  the BLK run found the same day, confirmed a second time here.

**CIK, found this session as instructed and with the history checked:**
`tools/sources.py cik_for('ACNB')` returns **CIK 0000715579, "ACNB CORP"**. `formerNames` is
**empty** and the `companyfacts` history is **continuous from 2009 to 2025 on 585 us-gaap
tags** — so the BLK trap (a CIK whose history does not span the window) does **not** apply
here, and the check was performed rather than assumed.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** ACNB Corporation is the holding
company for one bank and one insurance agency. At 2026-06-30 it holds **$3,318,863 thousand
of assets**. It gathers **$2,535,676 thousand of deposits** from **33 community banking
offices and two loan offices** in six Pennsylvania counties (Adams, Berks, Cumberland,
Franklin, Lancaster, York) and three Maryland counties (Baltimore, Carroll, Frederick), and
in the six months to 2026-06-30 it paid those depositors **1.04% a year, counting the
noninterest-bearing money that costs nothing** (interest of $13,001 thousand on average
interest-bearing deposits of $1,933,033 thousand plus average noninterest-bearing demand of
$569,102 thousand; the 10-Q's own average-balance table). It lends that money out at
**6.40%** on a **$2,398,104 thousand** loan book of which **54.6% is commercial real estate**,
holds **$529,774 thousand of securities** yielding 3.68%, and keeps the difference: an
**FTE net interest margin of 4.56% in the quarter** and **$34,002 thousand of net interest
income**, which is **79.4% of the quarter's revenue**.

The other **20.6%** is fees: an insurance agency (commissions, $9,482 thousand of revenue in
2025), trust and brokerage, service charges on deposits, debit-card interchange, and gains on
selling residential mortgages it originates. Against all of that it spent **$23,125 thousand**
of operating cost in the quarter — an **efficiency ratio of 51.60%** on the filer's own
definition — and provisioned **$447 thousand** for credit losses. What is left, after a 21%
federal rate and Maryland state tax, is **$15,214 thousand of net income, $1.49 a diluted
share, a 1.85% return on average assets and a 14.54% return on average equity.**

Stripped of all of that: **ACNB borrows short-dated money from small-town depositors at
roughly one per cent and lends it against local commercial property at roughly six and a
half, on nine dollars of assets for every dollar of tangible equity.** Everything else is
detail.

**The scarce input this business controls.** It is **not** the loan. ACNB's total
earning-asset yield in 2025 was **5.61%**, below Orrstown Bank's **6.13%** on the same
instrument in the same year — ACNB is not a better-paid lender. The scarce input is **the
deposit that does not ask for interest.** At 2026-06-30, **$600,711 thousand — 23.7% of all
deposits — paid nothing**, and that balance **grew 4.3% in the quarter and 5.7% over the
year**; savings deposits of **$336,504 thousand paid 0.03%** while the 30-year Treasury paid
**5.34%**. The filer names what it is competing against in its own words: *"local government
investment trusts, credit unions and larger regional banks"*. Those substitutes are a phone
call away, charge nothing to switch to, and pay four to five per cent. The money stays
anyway. **That gap — between what the money is worth and what its owner asks for it — is the
whole business**, and it is the only thing here that is scarce.

**Will the fundamentals look broadly the same in ten years?** Yes, and the record is 168
years long: the bank was founded in 1857 as Adams County National Bank and the holding
company was formed in 1982. The three revenue mechanisms — spread, insurance commission, fee
— have not changed in any filing this session read back to FY2021, and the balance sheet's
shape has not changed either: loans/deposits 92.8% to 95.1% across five years, securities
16% of assets, no trading book, no derivatives book beyond $260 thousand of posted collateral
on customer swaps and one cash-flow hedge, no foreign exposure, **no off-balance-sheet
vehicle other than $566,839 thousand of undrawn loan commitments and $24,394 thousand of
standby letters of credit, both disclosed and both ordinary.** This is **[E3-31]**'s
*"relatively simple and stable in character"* in the plainest case this queue has run.

**[E4-46] checked and it does not bite.** Nothing here needed five months to learn. Every
number above came out of two filings in one session.

- **VERDICT: [x] IN**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired [x] — a place to keep money and a loan against a building; the demand is
  not in question.
- no close substitute [x] — **but only on the narrow ground the corpus itself names, and the
  argument is below**, because deposits and loans are commodities until the filings prove
  otherwise.
- not price-regulated [x] — deposit and loan rates are not administered. **But [E2-59] is
  recorded against this tick and not waved through:** the deposit franchise is **floored by a
  regime** — federal deposit insurance, which is why $1,953,357 thousand of ACNB Bank's
  deposits can sit at 0.03% without a run. *"administered pricing ... could legally price
  their way to profitability even in the face of substantial over-capacity ... That day is
  gone"* is how a regime-based moat ends, and the moat belongs to the regime, not the bank.
  What ACNB has to prove is that it earns **more** than the regime hands everybody.

**Must the moat be continuously rebuilt? Does success depend on a great manager?**
**[E4-04]** No to both, on the scope test the framework sets. A branch network and a
168-year-old depositor relationship must be **defended** — branch operating cost, and
$23,125 thousand a quarter of it — but a lapse in that spending **narrows** the advantage; it
does not destroy the basis of it and replace it. This is Coca-Cola's advertising, not Mitsui's
Rhodes Ridge. And **[E4-23]** is answered explicitly: **the advantage is not the CEO.** ACNB
has had three bank acquisitions under two chief executives and the funding advantage sits in
the same counties across all of them. **No key-person moat defect is recorded at Q2.**

**Primary moat metric, filing-sourced, and its trend. The metric is the cost of the money,
because the cost of the money is the business.**

| ACNB, cost of **total** deposits (interest on deposits ÷ average total deposits incl. noninterest-bearing), from the filer's own daily-average tables | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 ann. |
|---|---|---|---|---|---|---|
| **cost of total deposits** | **0.215%** | **0.110%** | **0.184%** | **0.613%** | **1.087%** | **1.039%** |
| FTE net interest margin, as filed | 2.82% | 3.33% | 4.07% | 3.79% | **4.23%** | **4.51%** |
| noninterest-bearing share of average deposits | 25.5% | 26.1% | 27.1% | 26.2% | 23.1% | 22.7% |

**And the honest deduction from it, before the row:** of 2025's 4.23% margin, **$7,719
thousand — 26 basis points — is accretion of acquisition accounting adjustments** on the
Traditions loans and deposits, disclosed by the filer, and it runs off ($2.2M in Q2 2025,
$1.9M in Q1 2026, **$1.8M in Q2 2026** — a declining series on the filer's own numbers). Ex
accretion the 2025 margin is roughly **3.97%** and the Q2 2026 margin roughly **4.32%**.
**[E4-41] applied: the favourable exogenous break is named and removed before the number is
trusted.** The margin still leads the row after the removal.

### THE COMPETITOR ROW — required [E3-28]. A moat is a claim about *relative* position.

**TWO rows were built, because one of them could not close the private and mutual banks and
the other could.**

#### ROW A — the ten SEC-registrant community bank holding companies with footprint or
adjacent-market overlap. Five years, one specification, every figure computed by this session
from each filer's **own** tagged annual data and then read back against the filing text.

*Specification, stated once so the row is reproducible: **ROE** = net income ÷ the simple
average of opening and closing common equity; **cost of total deposits** = interest expense
on deposits ÷ the simple average of opening and closing total deposits (so every filer is on
the same footing, including the subject — ACNB's figure on this uniform basis is 1.259% for
2025 against 1.087% on its own daily averages, and **the uniform figure is the one used in
the row**); **net interest income ÷ average assets** stands in for NIM across five years
because peers do not all tag earning assets, and each filer's **own published FTE NIM** is
given beside it for 2025; **efficiency** = noninterest expense ÷ (net interest income +
noninterest income), unadjusted, so merger costs and intangible amortisation are left in for
everybody.*

| holding company | HQ / overlap | **cost of total deposits, 2025** | 2024 | 2023 | 2022 | 2021 | **own FTE NIM 2025** | **5-yr mean ROE** | **5-yr mean ROA** | source |
|---|---|---|---|---|---|---|---|---|---|---|
| **ACNB Corporation** | **Gettysburg PA — the subject** | **1.26%** | **0.61%** | **0.18%** | **0.11%** | **0.22%** | **4.23%** | **11.53%** | **1.26%** | 10-K `0001628280-26-017229` + four prior 10-Ks |
| Citizens & Northern | Wellsboro PA | 1.69% | 1.91% | 1.21% | 0.34% | 0.24% | 3.61% | 9.30% | 1.05% | 10-K `0001104659-26-024613` |
| Peoples Financial Services | Scranton PA | 1.84% | 2.29% | 1.85% | 0.42% | 0.27% | 3.58% | 9.46% | 0.91% | 10-K `0001104659-26-028106` |
| Franklin Financial Services | **Chambersburg PA — Franklin Cty** | 1.90% | 1.84% | 1.22% | 0.24% | 0.13% | 3.25% | 11.26% | 0.87% | 10-K `0000723646-26-000016` |
| Fulton Financial | **Lancaster PA — direct** | 1.95% | 2.19% | 1.39% | 0.21% | 0.14% | 3.51% | 10.65% | 1.08% | 10-K `0000700564-26-000006` |
| Shore Bancshares | Easton MD | 1.97% | 2.11% | 1.64% | 0.33% | 0.19% | 3.36% | 7.16% | 0.68% | 10-K `0001035092-26-000014` |
| Citizens Financial Services | Mansfield PA | 1.98% | 2.22% | 1.52% | 0.40% | 0.34% | 3.50% | 11.38% | 1.11% | 10-K `0001140361-26-009103` |
| Orrstown Financial Services | **Shippensburg/Harrisburg PA — direct** | 2.02% | 2.35% | 1.49% | 0.26% | 0.17% | 4.04% | 11.24% | 1.03% | 10-K `0001628280-26-017278` |
| Norwood Financial | Honesdale PA | 2.22% | — | — | — | — | 3.49% | 9.98% | 0.93% | 10-K `0001013272-26-000003` |
| Mid Penn Bancorp | **Harrisburg PA — direct** | 2.46% | — | — | — | — | 3.56% | 8.36% | 0.92% | 10-K `0000879635-26-000026` |
| First Keystone | Berwick PA | 2.52% | 2.49% | 1.73% | 0.51% | 0.31% | 2.66% | 3.82% | 0.43% | 10-K `0000737875-26-000009` |

*Norwood and Mid Penn do not tag interest expense on deposits separately in the years before
2025, so their pre-2025 cells are left empty rather than filled from a different definition;
their 2025 figures are computed from the interest-expense-on-deposits line in their own
average-balance tables. Every "own FTE NIM 2025" figure was read in the filing text, not
inferred: ORRF 4.04% (its Analysis of Net Interest Income table), CZNC 3.61%, MPB 3.56%,
FULT 3.51% (FTE table), CZFS 3.50%, NWFL 3.49%, PFIS 3.58% (its Net interest margin
(non-GAAP) line, cross-checked as $165,962k of net interest income over $4,708,036k of average
earning assets = 3.53% before the FTE adjustment), SHBI 3.36%, FRAF 3.25%, FKYS 2.66%.*

**What Row A says, and it is not ambiguous. ACNB is first of eleven on four measures at once:
the lowest cost of total deposits in four of the five years, the highest published FTE net
interest margin in 2025, the highest five-year mean return on equity, and the highest
five-year mean return on assets — and the most stable ROA of the eleven (1.04 / 1.35 / 1.28 /
1.32 / 1.32, a 31-basis-point range against Orrstown's 95, Peoples' 120 and First Keystone's
211).**

**And what Row A says against it, which is the part that decides the class. The deposit-cost
gap is closing fast.** Against the second-cheapest funder in the row, ACNB's advantage ran
**13bp (2021) → 13bp (2022) → 104bp (2023) → 123bp (2024) → 43bp (2025)**. The advantage is
**real, measured, and three-fifths gone in one year.** Part of that is acquisition mix — the
filer says the money-market attrition it is running off is *"higher cost money market deposits
from the Acquisition"* — and the H1 2026 figure has turned down (1.039% annualised against
1.087%). But the direction of the single metric on which the franchise rests was **adverse in
the most recent full year**, and this run will not write that as a footnote.

#### ROW B — and this is the row that closes the private and mutual banks, from the issuing
authority rather than from the SEC.

Row A is a row of **listed** holding companies. ACNB's own filing names **credit unions** and
**local government investment trusts** among the competitors it prices deposits against, and
neither files with the SEC — so on Row A alone the moat class would be **PROVISIONAL and
therefore UNRESEARCHED**. **It is not left there.** Every FDIC-insured institution that
operates a banking office in ACNB's nine counties files a **quarterly Call Report with the
FDIC**, which publishes the ratios directly. This session pulled the FDIC `locations`
endpoint for all nine counties (712 offices), reduced it to **56 distinct insured
institutions with at least one office in ACNB's market**, and pulled each one's
**2025-12-31 Call Report financials** — the same four metrics the brief asks for, at the same
date, from the regulator that collects them. **ACNB Bank is CERT 7506.**

**ACNB Bank at 2025-12-31, FDIC Call Report:** net interest margin **4.476%** · **cost of
funding earning assets 1.412%** · efficiency ratio **59.685%** · ROE **10.39%** · pre-tax ROA
**1.545%** · uninsured deposits **$522,925k on $2,475,524k = 21.1%** · core deposits **94.1%
of deposits** · loans/deposits 94.3%.

**The two decisive rankings out of 56, and neither needs a footnote:**

| | ACNB Bank | where it ranks among the 56 institutions with an office in its nine counties |
|---|---|---|
| **cost of funding earning assets** | **1.412%** | **6th lowest of 56.** The five below it are Wilmington Trust NA (0.05%, a trust bank with almost no deposits), Fleetwood Bank ($402M), Woodsboro Bank ($456M), Harbor Bank of Maryland ($380M) and Community State Bank of Orbisonia ($459M). **Among the 25 institutions in this market with more than $1 billion of assets, only BayVanguard Bank ($903M, 1.38%) and Woodforest National Bank (a Texas in-store retail bank, 1.28%) fund more cheaply. Of the PA- and MD-headquartered commercial banks above $1bn that compete here, ACNB is FIRST.** |
| **net interest margin** | **4.476%** | **4th highest of 56**, behind Capital One NA (8.35%, a credit-card bank), Wilmington Trust NA (8.04%, a trust bank) and Eastern Savings Bank FSB (5.69%, $367M). **Among the $1bn-plus institutions it is second only to Woodforest (4.58%), and it beats every direct footprint rival: Orrstown 4.14%, Mid Penn 3.64%, Fulton Bank 3.60%, Farmers & Merchants of Chambersburg 3.44%, Ephrata National 3.35%, Citizens & Northern 3.75%, Bank of Bird-in-Hand 2.86%.** |

**And Row B runs five years too, which is what turns a snapshot into the [E2-58] test.** The
same 56 institutions' Call Reports were pulled at six dates. *Cost of funding earning assets
is the Call Report's own ratio; the market figure is the **median of the 56**, not an average
of the largest.*

| FDIC Call Report, ACNB Bank (CERT 7506) vs the 56 institutions in its market | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-06-30 |
|---|---|---|---|---|---|---|
| **ACNB cost of funding earning assets** | 0.231% | 0.109% | 0.334% | 1.048% | 1.412% | **1.274%** |
| **market median, 56 institutions** | 0.232% | 0.383% | 1.599% | 2.174% | 1.928% | 1.685% |
| **ACNB advantage, points** | **0.00** | **0.27** | **1.27** | **1.13** | **0.52** | **0.41** |
| **ACNB rank, lowest cost, of 56** | **28th** | **3rd** | **2nd** | **3rd** | **9th** | **8th** |
| **ACNB net interest margin** | 2.894% | 3.438% | 4.106% | 3.889% | 4.476% | **4.553%** |
| market median NIM | 2.996% | 3.316% | 3.330% | 3.212% | 3.556% | 3.746% |
| **ACNB NIM advantage, points** | **−0.10** | **+0.12** | **+0.78** | **+0.68** | **+0.92** | **+0.81** |
| ACNB efficiency ratio | 59.11% | 53.12% | 54.90% | 60.39% | 59.69% | **50.54%** |
| ACNB return on equity | 10.73% | 14.62% | 13.35% | 12.16% | 10.39% | **14.53%** |

**This is the most important table in the file, and it corrects the story the 2025 snapshot
tells.** In 2021, with the risk-free rate at zero, **ACNB Bank was the 28th cheapest funder of
56 — exactly the median — and its net interest margin was BELOW the market median.** There was
no visible advantage at all. What the record actually shows is **not a permanent cost advantage
but a LOW DEPOSIT BETA**: when the market's cost of funds rose 194 basis points from 2021 to
2024, ACNB's rose **82**; as the market's came back down 49 basis points, ACNB's has come down
**14**. A lag is worth most exactly when rates are high, which is when it matters for margin —
and a lag also **compresses on the way down**, which is what 2025 and 2026 are showing.
**Across the full five years ACNB's mean cost of funding was 0.627% against the market median's
1.263% — a 64-basis-point cycle-average advantage on roughly $2.1 billion of average deposits,
about $13 million a year pre-tax, near a fifth of pre-tax income.** That is wide, it is
cycle-average rather than snapshot, and it is the honest size of the thing. **The composite —
net interest margin — points the other way and is still widening: from 10 basis points BELOW
the market median in 2021 to 81 above it in mid-2026.**

**At 2026-06-30, against the eleven banks that actually compete for the same deposits and
buildings, ACNB Bank is first on four of six measures:**

| bank (FDIC, 2026-06-30) | assets $m | NIM | cost of funding | efficiency | ROE | ROA | uninsured dep. | noninterest-bearing dep. | net charge-offs |
|---|---|---|---|---|---|---|---|---|---|
| **ACNB Bank** | **3,304** | **4.55%** | **1.27%** | **50.54%** | 14.53% | **1.80%** | 22.4% | 23.5% | **0.012%** |
| Citizens & Northern Bank | 3,143 | 4.10% | 1.64% | 57.94% | 8.61% | 0.96% | 31.4% | 21.6% | 0.880% |
| Orrstown Bank | 5,612 | 3.99% | 1.88% | 52.48% | 14.99% | 1.69% | 29.1% | 20.0% | 0.104% |
| First United Bank & Trust | 2,055 | 3.96% | 1.53% | 60.95% | 12.02% | 1.25% | 22.7% | 25.3% | 0.038% |
| Mid Penn Bank | 7,039 | 3.90% | 1.94% | 57.43% | 9.89% | 1.24% | 20.0% | 16.5% | 0.040% |
| Middletown Valley Bank | 1,194 | 3.78% | 1.68% | 61.01% | 5.06% | 0.45% | 23.2% | 25.9% | 0.018% |
| Ephrata National Bank | 2,390 | 3.76% | 1.40% | 70.94% | 11.18% | 1.01% | 12.1% | 35.3% | 0.036% |
| Fulton Bank NA | 32,561 | 3.64% | 1.69% | 57.38% | 11.84% | 1.30% | 40.5% | 19.6% | 0.304% |
| Farmers & Merchants Trust, Chambersburg | 2,336 | 3.64% | 1.70% | 60.14% | **15.37%** | 1.27% | 22.7% | 17.8% | 0.075% |
| Bank of Bird-in-Hand | 1,908 | 3.28% | 2.75% | 52.60% | 12.20% | 1.17% | 24.6% | 8.7% | 0.001% |
| Woodsboro Bank | 483 | 4.23% | 0.88% | 62.55% | **15.86%** | 1.11% | 24.1% | 34.7% | −0.016% |

**First of eleven on net interest margin, on cost of funding among everything above $1bn, on
efficiency ratio, and on return on assets; second-lowest on charge-offs; and Citizens &
Northern — the same size, the same state, the same business — is charging off 73 times as much
of its book.** The two banks that beat ACNB on ROE do it at $483 million and $2.3 billion with
worse margins and worse efficiency, on more leverage.

**The combination is the finding.** Of 56 institutions competing in these counties, exactly
**six** carry a net interest margin above 4.0% together with a cost of funding below 1.50%:
Wilmington Trust NA, Harbor Bank of Maryland ($380M), Woodsboro Bank ($456M), BayVanguard
Bank ($903M), Woodforest National Bank (Texas), and **ACNB Bank**. **ACNB is the only
Pennsylvania- or Maryland-headquartered community bank above one billion dollars in this
market that does both, and the private and mutual banks — the ones Row A could not see —
do not do it either.** Bank of Bird-in-Hand, the fast-growing Lancaster County private bank,
funds at **3.10%**, more than twice ACNB's cost. **Farmers & Merchants Trust of Chambersburg,
ACNB's closest non-listed neighbour, funds at 2.03% and earns a 3.44% margin.** The advantage
is not an artefact of comparing ACNB only with other listed companies.

- **Peers named: 10 of 10 available SEC-registrant holding companies with footprint or
  adjacent-market overlap (Row A), plus all 56 FDIC-insured institutions with a banking
  office in ACNB's nine counties (Row B).** Buffett says eight **[E3-28]**; this row took
  ten and then took the whole market.
- **Any peer unavailable?** **One class, and it is named with its artifact rather than
  waved at: credit unions.** ACNB's own 10-K names them as a deposit competitor; they file
  **NCUA Form 5300 call reports and quarterly Financial Performance Reports**, which are
  public, and this session did not pull them. **That rung is UNRESEARCHED, and the direction
  of the missing evidence is stated so the reader can price it: credit unions are federally
  tax-exempt and therefore structurally cheaper funders, so the missing rung can only push
  the measured advantage DOWN, never up.** The uncertainty is spent in the **class** —
  **NARROW, not WIDE** — rather than left as an open question about whether the advantage
  exists, because the advantage is already measured against 56 filing institutions at 43 to
  123 basis points. *That is a judgment, it is disclosed here, and a reader who thinks the
  template's PROVISIONAL rule should have closed the file instead can see exactly what was
  traded.*
- **Untapped pricing power — could a manager raise the return simply by raising prices, and
  has not? [E3-33]** **No, and the inverse test [E4-37] is the useful one here.** ACNB cannot
  raise the price of a commercial mortgage in York County; its earning-asset yield is *below*
  Orrstown's. What it can do is keep *not* raising the price it pays, and the filed evidence
  is that it does so **without agony**: noninterest-bearing deposits grew 22.7% in 2025 and
  4.3% in the June 2026 quarter alone, at a price of zero, and savings deposits held at
  **0.03%** across the entire rate cycle (0.03% in 2023, 0.04% in 2024, 0.03% in 2025, 0.03%
  in H1 2026 — the filer's own rate tables). **A bank that can hold 0.03% on $336 million
  through a cycle in which the risk-free rate went to five per cent is not having a prayer
  session before it prices.** **[E5-28] is respected and the claim is kept small: this is not
  near-monopoly pricing power. It is one-directional pricing power on the liability side
  only.**
- **[E2-58] — the commodity doctrine, which is the criterion-2 test for any bank.** The
  equation says persistent over-capacity without administered prices equals poor
  profitability, and it names **one** exception: *"a cost advantage that is both **wide and
  sustainable** … By definition such exceptions are few."* **Wide: a 64-basis-point
  cycle-average advantage over the median of its own 56-bank market across 2021–2025, peaking
  at 127 basis points in 2023 and running at 41 in mid-2026 — roughly $13 million a year
  pre-tax, about a fifth of pre-tax income. Sustainable in the sense that matters and NOT in
  the sense the phrase first suggests: it is a property of the depositor base — a low deposit
  beta — rather than a pricing decision, and so it persists; but it was INVISIBLE in 2021
  (28th of 56, exactly the median), because at a zero risk-free rate there is nothing for a
  low beta to be low against.** That is the exception, met on filed figures and stated with
  its shape rather than with its best year — and it is also the *whole* of the franchise,
  which is why the class is NARROW.
- **[E3-62]'s second step, and it must be asked because this is a commodity business.** How
  much of the funding gain stays home and how much flows to the customer? **It stays home,
  and the number says so:** ACNB Bank earns a 4.476% margin on 1.412% money while the market
  median funds at roughly 1.93% — the gap is retained as margin, not competed away into loan
  pricing, because ACNB does *not* undercut on loans (its asset yield is mid-pack). **But
  Row A's closing gap is this same question answered in the other direction over time**, and
  it is the reason the direction is MIXED.
- **[E4-36] — which of the four causes of extreme success is this?** Not wave-riding
  **[E3-51]**: the rate cycle is a wave and ACNB rode it (margin 2.82% → 4.23%), but the
  *relative* position — cheapest funder in a 56-bank market — is not a wave, because every
  one of those 56 sat in the same rate cycle. It is **the extreme max/min of one variable**:
  cost of funds. **One variable is a narrow moat by construction, and the corpus's own
  language for it is [E2-53]'s opposite — position here does not carry the business "good or
  bad"; it carries exactly one line of the income statement.**
- **[E3-46] — the second question about the business is a number.** Return on tangible equity
  capital employed, the **[E2-43]** denominator with the goodwill wedge reported separately:
  **13.30 / 17.83 / 15.83 / 13.81 / 13.84 per cent for 2021–2025, a five-year mean of
  14.92%, and 18.21% annualised in H1 2026.** The wedge is stated and not hidden: goodwill
  and intangibles were **$86,884k at 2025-12-31 and $84,800k at 2026-06-30, 20.7% and 20.0%
  of book equity.**
- **[E2-44]'s two-characteristic test.** Can it raise prices when demand is flat and capacity
  is not fully used? **On the liability side, yes — it holds price when everyone else raises
  it, which is the same thing.** Can it grow dollar volume with only minor additional capital?
  **Answered at Q4's (c): organically it needed $20.4 million of retained capital in five
  years against $164.2 million earned. Yes.**
- **[E2-45]'s attacker's test — with ample capital and skilled people, how would I compete
  with this?** Not by opening branches in Adams County; the incumbent has 168 years and the
  deposits cost it nothing. **I would compete the way the substitute already competes: by
  offering the same depositor 4% on a federally insured money market account with no branch at
  all, which is precisely what a credit union, a Treasury fund and an online bank already do
  — and the answer is that this attack is already fully deployed, has been for three years at
  a 400-basis-point price advantage, and ACNB's noninterest-bearing deposits still grew.**
  That is the strongest thing that can be said for the moat, and it is also the exact shape of
  the way it dies, named at Q4.
- **[E3-61]'s limit is recorded:** the row shows position, not conduct. Eleven banks with
  near-identical structures produced five-year mean ROEs from 3.82% to 11.53%, and no row
  predicts which will imitate the next lax underwriting cycle. That is Q3's question, and
  Q3 is a gate here.
- Class: [ ] WIDE [x] **NARROW** [ ] NONE [ ] PROVISIONAL · Direction: **MIXED, and the two
  limbs point opposite ways on purpose.** The composite — net interest margin against the
  median of its own 56-bank market — went from **10 basis points BELOW** in 2021 to **81
  above** in mid-2026, and is still widening. The single variable the franchise rests on —
  cost of funds — peaked at a **127-basis-point** advantage in 2023 and is now **41**, because
  what ACNB owns is a **low deposit beta** and a lag compresses on the way down as it expanded
  on the way up. **[E4-32] is satisfied on existence and is claimed for the composite only;
  it is explicitly NOT claimed for the funding gap, which is narrowing.**
- **VERDICT: [x] IN — class NARROW**

*Why this is IN and not UNRESEARCHED. The gate asks whether this is a franchise. Fifty-six
institutions' Call Reports at one date and ten holding companies' filings over five years say
that one line of ACNB's income statement is first or near-first in its market and has been for
five years, on the one exception [E2-58] names. The class is NARROW because it is one line;
the direction is MIXED and written as MIXED; the credit-union rung is named as a work order
with its direction stated. **No "unverified", "general knowledge" or "provisional" caveat is
carried into the verdict** — what is carried is a class and a direction, both of which are
findings.*

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [x] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]** — not ticked; this is a marketable
      minority position in a NASDAQ-listed company and the exit is a phone call
- [x] **Leverage** — small asset errors destroy equity **[E3-29]**

**Case declared: Q3 IS A BINARY GATE AND NO PRICE COMPENSATES.** Two of three ticked, and the
corpus names this exact business when it says so. **Leverage:** total assets of $3,318,863
thousand on book equity of $423,279 thousand is **7.8 to 1**, and on tangible common equity of
$338,479 thousand against tangible assets of $3,234,063 thousand it is **9.6 to 1** — so a
loss of **10.5% of assets** erases the tangible equity, and the whole of the equity sits inside
one credit decision repeated a few thousand times. [E3-29] was written about twenty to one and
concluded about management rather than about a threshold; nine and a half to one does not change
the conclusion, it only moves the arithmetic. **Daily execution [E3-38, E3-43, E2-70]:** the
1977 root is exact for this business — *"their only products are promises"*. A loan is a
promise underwritten one at a time by people the shareholder never meets, and there is no
franchise here that will carry a bad underwriting year; the [E2-53] dominance reading was
refused at Q2 for precisely this reason. **So the one place in the framework where cheapness is
ruled out as a remedy is in force [E1-16, E3-29, E5-35]:** *"You can turn any investment into a
bad deal by paying too much. What you can't do is turn any investment into a good deal by
paying little."*

**Honesty — binary, permanent, filings-based [E5-16].** Each matter dated to when it became
PUBLIC:
- **No conduct matter was found.** Item 3 of the FY2025 10-K: *"there were no material pending
  legal proceedings, other than ordinary routine litigation incidental to and in the ordinary
  course of the business"* — the same language in all five 10-Ks read. No regulatory
  enforcement action, consent order, written agreement, BSA/AML matter, CRA downgrade or
  restatement appears in any of the five 10-Ks, the four earnings releases, or the proxy.
- **The auditor is Crowe LLP** (Franklin, TN, PCAOB Firm ID 173). Unqualified opinion on the
  FY2025, FY2024 and FY2023 financial statements **and** an unqualified attestation on internal
  control over financial reporting at 2025-12-31. **No material weakness, no significant
  deficiency, no disagreement:** Item 9 reads *"None."* **Two critical audit matters, and both
  are the right ones:** the allowance for credit losses (*"the extent of auditor judgment
  applied and significant audit effort to evaluate the significant subjective and complex
  judgments made by management, including segmentation, the economic forecast"*) and **the fair
  value of acquired loans** (*"especially subjective auditor judgment … including the need for
  professionals with specialized skill or knowledge"*). The auditor put its flag on exactly the
  two places this run's own reading found the judgment — the reserve and the purchase
  accounting. **[E5-32]'s cap is nevertheless carried in full: Salomon's floating plug was
  signed by the largest audit firm in the country for twelve years. Audited does not mean
  true**, which is why equity was recomputed from A − L at Step 0 and why the reserve is tested
  against subsequent charge-offs below rather than against the auditor's opinion.
- **Related-party dealing is minimal and policed:** *"The Corporation does not regularly engage
  in business transactions with directors and executive officers outside of its business of
  banking. Generally, any other significant transactions with directors or executive officers
  are reviewed and approved"* (2026 proxy). No Compensation Committee interlocks.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30]. Accounting and disclosure, not litigation.
Each is a prompt to READ, never a verdict — and the list is open, not closed [E3-68].**

- [ ] **weak accounting** — does not fire. Restricted stock is expensed in full ($1,411 /
      $1,263 / $1,004 thousand for 2025/2024/2023); there is no defined-benefit pension return
      assumption doing work (the nonqualified plan liability is $6.5 million, funded with
      bank-owned life insurance, and the annual charge is disclosed at $886 thousand); no
      capitalised software games; no off-balance-sheet vehicle beyond disclosed loan
      commitments.
- [ ] **unintelligible footnotes** — does not fire, and the opposite is true: the 10-K opens
      with a **two-page defined-abbreviation table** and the notes are numbered and plain. The
      business-combination note gives the full purchase-price allocation line by line, book
      value beside fair value beside the adjustment.
- [ ] **trumpeted earnings projections / growth targets** — does not fire on the filings. **The
      four earnings releases were pulled specifically to test this (the CGNX companion rule)
      and none of them contains an EPS, revenue, margin or NIM forecast, a target, or a
      multi-year plan.** The language is promotional — *"RECORD 2026 SECOND QUARTER FINANCIAL
      RESULTS"*, and the CEO quote runs to *"the resilience of our franchise"* and
      *"disciplined growth, prudent risk management, and delivering sustainable long-term
      shareholder value"* — but **promotional adjectives about the quarter that has already
      happened are not [E3-48]'s projections, and [E5-30]'s ratchet has not been started: there
      is no guidance culture to quit.** Recorded as noise, not as a flag.
- [ ] **serial share issuance [E5-15]** — **does not fire, and the reason is specific.** Shares
      outstanding went **6,064,138 (2016) → 10,372,251 (2025), +71.0%**, which on its face is
      the tell. But **every share of that increase is acquisition consideration paid to selling
      shareholders** (938,360 for New Windsor in 2017, 1,590,547 for Frederick County in 2020,
      2,035,246 for Traditions in 2025) and **not one dollar was raised for cash from the
      market**: *"There have been no unregistered sales of stock in 2025, 2024 or 2023"*, and
      the only cash issuance is the Dividend Reinvestment Plan, which issued **15,419 shares in
      2025 and 13,115 in H1 2026 — 0.15% and 0.13% of the count.** [E5-15]'s target is the
      promotion-minded manager selling paper into a market; the dilution here is a
      capital-allocation question and it is scored there, under [E5-44].
- [x] **EBITDA / adjusted-earnings promotion [E4-29]** — **READS CLEAN, and the count is
      given** because the CGNX ruling requires the 8-Ks to be pulled before this is scored:
      **`grep -c -i ebitda` = 0 in the FY2025 10-K, 0 in the Q2 2026 10-Q, 0 in ALL FOUR 8-K
      EX-99.1 earnings releases, and 0 in the 2026 proxy.** The word does not appear anywhere in
      ACNB's filed record read this session. "Adjusted earnings", "adjusted EPS" and "adjusted
      net income" return **0** in the 10-K, the 10-Q and all four releases. The box is ticked
      only because the test was run, and the finding is a pass. **The four non-GAAP measures
      ACNB does present — tangible book value per share, tangible common equity to tangible
      assets, the efficiency ratio, and FTE net interest margin — are each reconciled line by
      line on a dedicated "Non-GAAP Reconciliation" page of every release, with the subtractions
      named (goodwill and intangibles; intangible amortisation; merger-related expense;
      securities gains; life-insurance gains). That is the [E2-26] form: the item is quantified
      separately at every line, not buried inside an adjusted figure.**
- [x] **filed-figure tells: cash taxes falling as a share of pretax income [E4-30]** — **FIRES
      as a prompt, and reading it resolves it benign. The prompt was real and the resolution is
      on the face of the filing.** Cash paid for income taxes: **$10,030 thousand (2023, 25.2%
      of pre-tax) → $6,628 (2024, 16.4%) → $5,328 (2025, 11.5%).** That is exactly the direction
      [E4-30] names. **What the filing says:** the **book** effective rate is flat at **20.5% /
      21.2% / 20.2%**, and Note 15 splits the 2025 charge into **current $5,777 and deferred
      $3,626** — the gap between cash tax and book tax is a **deferred tax expense recognised in
      the same statements**, i.e. book income ahead of taxable income, which is what
      purchase-accounting accretion and a December securities loss do. The FY2025 rate
      reconciliation is itemised with **no line above 1.5%** (state 1.5%, tax-exempt loan and
      securities income −0.9%, bank-owned life insurance −1.2%, life-insurance gain −0.1%,
      non-deductible merger costs **+0.3%**, excess compensation +0.1%, other −0.5%). **A
      company hiding earnings quality does not print a rate reconciliation whose largest
      adjustment is one and a half points.** Flag read, not scored.
- [ ] **unnaturally smooth reported growth [E4-30]** — does not fire; the opposite. Diluted EPS
      ran **$4.15 (2022) → $3.71 → $3.73 → $3.60 (2025)**, and net income $35.8m → $31.7m →
      $31.8m → $37.1m. **Reported earnings went DOWN for three consecutive years and the
      company did not smooth them.**
- [x] **metric-switching [E2-49] — fires once, weakly, and is disclosed.** In Q1 2025 ACNB
      changed the measurement of loans held for sale from lower-of-cost-or-market to **fair
      value**, *"to more appropriately reflect the performance of its entire mortgage banking
      activities"*, with the prior-period impact *"deemed to be immaterial"*. The change
      **preceded** a year in which gain on mortgage loans held for sale rose $5.0 million — so
      it is a policy change in the direction of the growing line. Against it: it was announced
      in the accounting-policy note, the direction of the change is the standard one for a
      mortgage-banking operation, and the amount is small. **Every headline metric definition —
      the efficiency ratio, tangible book value per share, FTE NIM — is identical across the
      FY2025 10-K, the Q2 2026 10-Q and all four releases.**
- [x] **the except-for flag [E2-57], and the restructuring-charge variant [E3-53, E5-33] —
      FIRES, at the place it does the most damage: the pay formula.** The 2026 proxy discloses
      that, for the 2024 variable-compensation awards, *"the Compensation Committee determined
      that it was appropriate to add the after-tax amount of these discrete merger expenses,
      **$1,582,358**, to the net income and ROAE for purposes of calculating the … performance
      awards."* **The metric that determines executive pay excludes the cost of the acquisitions
      the executives decide to make** — and [E4-27] is the governing line: *"Never, ever, think
      about something else when you should be thinking about the power of incentives."* [E3-53]
      and [E5-33] both say those charges are real costs and belong in the mean, and this run
      keeps them there: the $10.7 million of 2025 merger costs and the $2.0 million of 2024
      merger costs stay inside every figure below.
      **What is recorded ON THE OTHER SIDE, because it is the candor case demonstrated and it is
      unusual:** the same passage discloses a **second** adjustment running the other way — the
      2023 awards were adjusted for an after-tax securities loss of **$3,479,192**, against the
      executives — and states the **net** effect of both: *"a net increase to 2024 net income for
      purposes of determining Plan performance awards of $146,790."* A committee that wanted to
      flatter would not have disclosed the offsetting adjustment or netted to $146,790 in
      public. **The flag fires on the principle and the disclosure is exemplary; both are
      written down.**
      **And [E2-49]'s positive pole is met in the same document:** the plan publishes
      **pre-set threshold / target / maximum** levels for each financial metric **in advance**
      and reports the outturn against them — for 2024, net interest margin 2.70 / 3.00 / 3.60
      against an actual **3.37%**, and ROAE 9.75 / 10.83 / 13.00 against an actual **10.99%
      non-GAAP and 10.94% GAAP, both printed.** *"Pre-set, long-lived and small bullseyes"* is
      what that is, and the minimum triggers are published too (non-performing assets below
      1.5% before the plan activates at all).
- [x] **the reserve flag [E2-50] — this is a bank, so this is the flag that matters, and it
      fires once.** *"Where 'earnings' can be created by the stroke of a pen, the dishonest will
      gather."* **In 2024 the pen created $2,763 thousand of pre-tax income**: a $2,437 thousand
      reversal of the provision for credit losses plus a $326 thousand reversal on unfunded
      commitments — **6.8% of that year's $40,419 thousand of pre-tax income**, in the one year
      when reported EPS would otherwise have **fallen** from $3.71 to roughly $3.53 rather than
      risen to $3.73. **And the allowance ratio fell from 1.23% of loans to 1.03% in the same
      year that nonaccrual loans rose from $3,011 thousand to $5,871 thousand — reserve down
      while the bad loans went up.** The stated cause is *"updated estimates utilized as input
      assumptions within the CECL model calculation … based on more current information available
      during 2024"*, with a third party engaged to validate the model. **A model-assumption
      change that releases reserves in the year the metric needed help is the [E2-50] event, and
      it is recorded as fired.**
      **What answers it, and it is the strongest answer available — the reserving record against
      subsequent charge-offs, which is a bank's only substitute for [E2-67]'s table:**

| allowance at year end | against net charge-offs actually taken in the next three years | coverage |
|---|---|---|
| 2018: $13,964k | 2019–2021: $4,566k | **3.1x** |
| 2019: $13,835k | 2020–2022: $4,975k | **2.8x** |
| 2020: $20,226k | 2021–2023: $2,785k | **7.3x** |
| 2021: $19,033k | 2022–2024: $1,794k | **10.6x** |
| 2022: $17,861k | 2023–2025: $956k | **18.7x** |

  **Net charge-offs to average loans, eight consecutive filed years: 0.13% / 0.06% / 0.16% /
  0.08% / 0.08% / 0.02% / 0.02% / 0.01%, and 0.012% annualised at 2026-06-30 on the Call
  Report.** The allowance has been **between 2.8 and 18.7 times** the losses that actually
  followed it, in every window the filings allow to be tested. **[E2-50]'s risk is
  UNDER-reserving, and eight years of filed data say the error has run the other way every
  time.** So the 2024 release is read as **a late correction of a demonstrably over-large
  reserve, taken in a convenient year** — not as a reserve built in order to be released. The
  direction of the error is the thing [E2-67] says to look for (*"so you can … judge whether we
  may have some systemic bias"*), and the direction here is conservative. **Allowance coverage
  of nonaccrual loans is 221% (2025) and 244% (Q2 2026), against 463% in 2022 and 207% in 2018
  — thinner than the peak and thicker than the pre-COVID base.**
- [x] **[E2-67]'s exact artifact does not exist, and the absence is stated honestly rather than
      scored.** Berkshire published a table of its own reserving errors. **A bank has no
      equivalent disclosure requirement and ACNB publishes none** — there is no loss-development
      triangle in a bank 10-K. What ACNB does publish, and this run used all of it: the
      three-year allowance roll-forward with charge-offs and recoveries **by loan class**, the
      allowance allocation by class with each class's share of the book, nonaccrual loans **by
      origination vintage** (the 2025 table runs 2006–2024 year by year), collateral-dependent
      loans by collateral type, and the internally risk-rated total with its own allowance
      (*"Total internally risk rated loans were $1.80 billion as of December 31, 2025 with a
      related ACL of $19.0 million"*). **That is the most a bank filer gives, and ACNB gives all
      of it.**
- [ ] **dividends funded by issuance [E2-52]** — does not fire. 2025 dividends of $14,382
      thousand against net income of $37,051 thousand (38.8%) and buybacks of $11,164 thousand
      on top, while cash issuance was the $15,419-share DRIP. **Cash returned exceeded cash
      raised by roughly forty to one.**
- [ ] **stock-price targeting [E3-50]** — **does not fire, and this was tested rather than
      assumed.** The incentive plan's financial metrics are **net interest margin** and **return
      on average equity**, with strategic and individual goals. **Total shareholder return
      appears in the 2026 proxy in exactly two places, both inside the SEC-mandated Pay Versus
      Performance disclosure under Item 402(v), and nowhere in the incentive formula.** There is
      no stock-price, P/E-multiple or TSR performance measure in ACNB's pay design. *(The
      contrast is recorded because this queue has it one day old: the BLK run of 2026-09-19
      found "Next 12-Month P/E Multiple (including relative premium)" scored as a
      financial-performance measure. ACNB does not do that.)*
- **[E4-52]'s lollapalooza test — do the fired flags converge on one outcome?** The three that
  fired are the pay add-back of merger costs, the 2024 reserve release, and the
  loans-held-for-sale policy change. **They do converge, weakly, on one direction: each makes a
  year look better than the GAAP line, and two of the three are tied to the acquisition
  programme.** But they are small ($1.6m, $2.8m, immaterial), each is disclosed and quantified in
  the filing that contains it, and **the reported bottom line fell for three consecutive years
  anyway** — a reinforcing system produces smooth rising numbers, and these did not. **Not
  scored as a lollapalooza.**

**STEP 3 — THE PRIMARY TEST [E2-01].** *"The primary test of managerial economic performance is
the achievement of a high earnings rate on equity capital employed (without undue leverage,
accounting gimmickry, etc.) and not the achievement of consistent gains in earnings per
share."*

### HOW THIS RUN MEASURES RETURN ON EQUITY CAPITAL FOR A BANK — LABELLED CONVENTION, PRIME RULE 3

> **CONVENTION (ACNB, 2026-09-19).** *The same construction the CCB run wrote the same day,
> adopted here because ACNB's filings do not make it wrong, with **one modification that they
> force**. Owner earnings by the ordinary construction — operating cash flow less share-based
> compensation less a maintenance-capex guess — does not work for a bank, and ACNB's own
> statements show why in three lines. **(i) Operating cash flow is not a return:** it was
> **$53,643 thousand in 2025 against $37,051 thousand of net income**, and the reconciliation
> says why — $184,652 thousand of proceeds from selling originated mortgages and $7,719 thousand
> of non-cash purchase-accounting accretion both sit in operating, while the provision is
> non-cash. **(ii) There is no maintenance capex that matters:** purchases of premises and
> equipment were **$1,076 thousand against $3,228,126 thousand of assets** — 0.03% — and a loan
> book does not wear out. **(iii) Deposit and loan flows are financing and investing**, so the
> cash statement of a bank measures the direction of its balance sheet, not its earnings.*
>
> ***The metric set is therefore selected by business type first, exactly as [E5-37] requires
> (*"different numbers are of different importance … depending on the kind of business"; "there
> is not one-size-fits-all"*) and exactly as `Framework/SECTOR METHOD …` does for an insurer.
> The metric is the one the corpus itself names for this job — [E2-01]'s "high earnings rate on
> equity capital employed". Four measures, all from filed statements:***
> 1. ***return on average common equity**, as the filer reports it and independently
>    recomputed;*
> 2. ***return on average TANGIBLE common equity**, because [E2-43] says that for an acquisitive
>    filer the denominator is unleveraged net tangible assets — **"the best guide to the economic
>    attractiveness of the operation"** — with the goodwill wedge reported separately and never
>    hidden inside book equity. ACNB has made five acquisitions, so this is the **governing**
>    denominator here, not an optional extra;*
> 3. ***return on average assets**, because it is the one bank ratio immune to the leverage
>    choice and therefore to [E2-47]'s carve-out for unusual debt-equity ratios;*
> 4. ***the (c) EQUIVALENT, which is the part that is ours.** For a bank, the expenditure that
>    the business "requires to fully maintain its long-term competitive position and its unit
>    volume" **[E2-23]** is not plant. It is **the equity that must be retained to hold the
>    regulatory capital ratio constant while the balance sheet grows** — a bank that grows assets
>    and does not retain the matching capital must stop growing or sell shares. So **(c) =
>    Δassets × the Bank's Tier 1 leverage ratio**, and **"owner earnings" for a bank = net income
>    − (c)**. Rationale for the CONVENTION in one line: it is the only construction that makes
>    [E2-23]'s "requires to fully maintain … unit volume" mean anything for a balance-sheet
>    business, and it is the same idea as **[E2-60]**'s restricted earnings, whose third
>    dimension is explicitly **"its financial strength"**.*
>
> ***THE MODIFICATION ACNB'S FILINGS FORCE, and it is the CNR rule — no mean crosses a merger
> unless it is rebuilt on one perimeter: Δassets must be SPLIT into organic and acquired.***
> *Coastal Financial grew organically, so one Δassets served. ACNB's 2025 asset increase of
> $833,296 thousand contains **$877,450 thousand of assets that arrived on 2025-02-01 in the
> Traditions acquisition and were paid for with $83,649 thousand of newly issued stock, not with
> retained earnings.** Charging the acquired perimeter's capital requirement against the year's
> earnings gives (c) of $90,996 thousand and "owner earnings" of **minus $53,945 thousand**,
> which is arithmetic about a stock issuance dressed up as arithmetic about earning power. **So
> (c) is computed on the ORGANIC perimeter — Δassets less assets acquired — and the
> acquisition's capital cost is stated separately, in full, on its own line.** Both numbers are
> below and neither is hidden.*
>
> *Share-based compensation is already an expense in every reported figure and is **not** added
> back **[E5-06]**; it is tracked separately and it is immaterial — $1,411 thousand in 2025,
> **3.8% of net income and 2.6% of operating cash flow** — so the [E3-70] grant-value question
> cannot change a verdict here and no grant-value estimate is constructed. Restricted stock
> grants net of forfeitures and shares withheld for taxes were **24,598 shares** in 2025, 0.24%
> of the count.*

**The series. Balance sheet before income statement, as [E2-01] requires.**

| | 2021 | 2022 | 2023 | 2024 | 2025 | H1 2026 ann. |
|---|---|---|---|---|---|---|
| net income, $k | 27,834 | 35,752 | 31,688 | 31,846 | 37,051 | **57,834** |
| **ROE, recomputed (simple average equity)** | **10.50%** | **13.83%** | **12.13%** | **10.97%** | **10.25%** | **13.71%** |
| ROE, as the filer reports it | 10.52% | 14.35% | 12.23% | 10.94% | 9.44% | **13.76%** |
| **ROTCE — the [E2-43] denominator** | **13.30%** | **17.83%** | **15.83%** | **13.81%** | **13.84%** | **18.21%** |
| **ROA** | 1.04% | 1.35% | 1.28% | 1.32% | 1.32% | **1.78%** |
| tangible common equity, $k | 223,905 | 190,525 | 224,194 | 251,250 | 333,090 | 338,479 |
| **tangible book value per share** | **$25.80** | **$22.37** | **$26.34** | **$29.37** | **$32.11** | **$33.42** |
| goodwill + intangibles, $k — the wedge, reported separately | 48,209 | 54,517 | 53,267 | 52,023 | 86,884 | 84,800 |
| diluted EPS | $3.19 | **$4.15** | $3.71 | $3.73 | $3.60 | **$5.66** |
| cash tax as % of pre-tax income | — | — | 25.2% | 16.4% | 11.5% | — |

*The recomputation tracks the filer within 0.10 points in three of five years. The two gaps are
both explained and neither is a discrepancy: **2022** (13.83% mine against 14.35% filed) and
**2025** (10.25% mine against 9.44% filed) are simple-average artefacts — in 2025 the $83,649
thousand equity issuance landed on **1 February**, so a beginning-and-ending average
underweights it while the filer's daily average does not. **The filer's figure is the better one
in both years and the filer's is the one carried into Q5.** ROTCE adds back intangible
amortisation at the 20.2% book effective rate; the wedge is shown on its own line so that it is
never inside the denominator. **Five-year means: ROE 11.53%, ROTCE 14.92%, ROA 1.26%.**
**Tangible book value per share compounded from $23.95 at 2020-12-31 to $33.42 at 2026-06-30,
+39.5%, through three acquisitions, a 2022 AOCI drawdown of $33 million and a 45% payout ratio.**
The 2022 dip from $25.80 to $22.37 is the available-for-sale securities mark, not acquisition
dilution, and it has been fully recovered.*

**WHAT THE SERIES SAYS, AND IT SAYS TWO OPPOSITE THINGS THAT BOTH HAVE TO BE WRITTEN DOWN.**

**Against management.** Reported **ROE fell for three consecutive years, 14.35% → 12.23% →
10.94% → 9.44%**, and **diluted EPS is 13.3% BELOW its 2022 level four years later** ($3.60
against $4.15) — after three bank acquisitions, a 71% larger share count and a balance sheet 30%
larger than 2021's. **[E2-01] is defined in opposition to EPS growth precisely so that a manager
cannot be credited for a bigger company; here not even EPS grew.** The five-year mean ROE of
**11.53%** is the highest of the eleven-name row at Q2 — which says the industry was hard, not
that this was good — and it sits barely above the **~10% floor [E4-28]** that governs the price
at Q5.

**For management, and it is the larger half.** The three-year decline is **fully accounted for by
disclosed items and a denominator, not by deterioration:** $10.7 million of merger costs in 2025
and $2.0 million in 2024; a $3.5 million after-tax securities repositioning loss in 2023 and a
$2.8 million one in 2025; and **average equity that rose 51%, from $259.1 million (2023) to
$392.4 million (2025)**, because $83.6 million of it was issued on 1 February 2025 and had
eleven months in the denominator. **The moment the merger year is behind it, the series inverts:
H1 2026 shows ROE 13.76%, ROTCE 18.21%, ROA 1.78%, EPS annualising at $5.66 — 36% above 2022's
peak — and an efficiency ratio of 50.54% on the Call Report, the best of the eleven banks that
compete with it.** And **ROTCE, the [E2-43] denominator the corpus actually specifies for an
acquisitive filer, never fell below 13.30% in any of the five years and averaged 14.92%.** The
ROE series was depressed by the goodwill the acquisitions created; the return on the capital the
managers actually have to work with — **[E2-73]**'s question, *"the managers of the units should
be judged by the returns they achieve on the underlying assets"* — did not fall.

**[E3-59]'s two yardsticks, run explicitly.** *One is how well they run the business*, judged
against the hand they were dealt and read against competitors' reports: **the Q2 rows are that
reading, and at 2026-06-30 ACNB is first of eleven on margin, on funding cost among everything
above a billion, on efficiency and on return on assets, with net charge-offs of 0.012% against
Citizens & Northern's 0.880% on a same-sized book in the same state.** *The second is how well
they treat their owners*: the regular dividend was raised 23.5% year on year to $0.42 a quarter,
a **special dividend of $0.50** was paid in Q2 2026, and **179,407 shares were repurchased that
quarter at a weighted average of $50.79** — together **$25.7 million returned against $28.9
million of first-half earnings, 89%.** The correlation [E3-59] notes — that poor operators are
usually also the ones who do not think much about shareholders — points the same way here, in the
good direction.
**[E4-41] is applied to the hand as well as to the mean: the 2023–2025 margin expansion is a
rate cycle ACNB did not create, and it is named and removed at Q2 (26 basis points of accretion,
plus the low-beta lag) and again at Q4.**

**The half-owner test [E2-26]** — *does this reporting tell me what I would want to know if the
positions were reversed?* **Yes, and unusually so for a company this size, with one gap.**
- Everything this run most wanted was disclosed and quantified **separately at every line**: the
  merger costs ($10.7m, $2.0m), the securities losses ($2.8m after tax in 2025, $3.5m in 2023,
  each announced in its own 8-K **before** the 10-K), the purchase-accounting accretion ($7,719k
  for the year **and $1.8m / $1.9m / $2.2m by quarter, so the reader can watch it decay**), the
  full Traditions allocation with book value beside fair value beside the adjustment, the day-one
  non-PCD provision ($5.5m) separated from the PCD gross-up ($1.5m), **the CRE concentration as a
  percentage of the Bank's total risk-based capital at both dates**, the uninsured-deposit share,
  the twenty-largest-depositor concentration ($177.2m, 7.2% of Bank deposits), and the liquidity
  coverage of uninsured deposits (342.7% and 329.7%).
- **[E2-69]'s direction test passes:** the December 2025 securities sale was a **deliberately
  realised loss**, announced in an 8-K dated 2025-12-05 with the $2.8 million after-tax cost
  named, in order to reinvest at a higher yield. A management optimising the reported number does
  not volunteer a loss in December and file an 8-K about it. **A deviation toward candor is not
  the weak-accounting flag.**
- **The gap, and it is a real one: [E2-72] cannot be tested from the filings.** *"owners are
  entitled to hear directly from the CEO … A once-a-year report of stewardship should not be
  turned over to a staff specialist or public relations consultant."* **ACNB's 10-K contains no
  shareholder letter**; a CEO letter, if one exists, lives in a glossy annual report that is not
  an SEC filing and was not obtained. **Recorded as untestable rather than scored either way, and
  named as the one [E2-72] artifact this run did not get** (it would live on investor.acnb.com).

**The institutional imperative — score all four [E2-30].** *Not a fraud test: "institutional
dynamics, not venality or stupidity."*
- [ ] **resists any change in current direction** — does not fire. The 2025 securities
      repositioning, the 2026 subordinated-debt refinancing (issued $15.0m of 5.875% notes due
      2036 on 2026-03-12, redeemed $15.0m of 4.00% notes on 2026-03-31), the $40.0m FHLB
      paydown, the special dividend and the accelerated buyback are all changes of direction
      taken without prompting.
- [x] **projects/acquisitions materialise to soak up available funds** — **FIRES, and the
      sharpest instance is not the banks.** **$7,800,000 in cash, February 2022, for the business
      and assets of Hockley & O'Donnell Insurance Agency, LLC** — $2,077 thousand of goodwill and
      $5,723 thousand of customer-list and non-compete intangibles, all cash, no contingent
      payment. **The insurance segment's pre-tax income four years later is BELOW where it was
      before the purchase: $920 thousand (2021) → $1,312 (2022) → $1,701 (2023) → $1,528 (2024)
      → $853 (2025).** Segment revenue did rise, $5,928 thousand to $9,482 thousand, so the
      agency was bought and the revenue arrived — **and the earnings went backwards anyway.** The
      segment now produces **$853 thousand of pre-tax income, 1.8% of the consolidated total, on
      $8,385 thousand of goodwill and $19,652 thousand of assets.** This is a small number inside
      a $657 million company, and it is the clearest read available on how this management spends
      discretionary cash, which is why it is written out in full rather than summarised.
- [x] **staff studies produced to justify the leader's craving** — **fires weakly and is
      discounted on its face.** *"ACNB used an independent valuation specialist to assist with
      the determination of fair values"*; *"with the assistance of an independent valuation
      specialist, completed a core deposit intangible asset valuation"*; *"The Bank engages a
      third-party to assist with validation of the CECL model"*. **[E3-58]** says solving capital
      allocation *"by either having a staff that does it, or by hiring consultants"* is *"a
      terrible mistake"* — but **a purchase-price allocation under ASC 805 and a CECL model
      validation are GAAP and supervisory requirements, not outsourced judgment**, and nothing in
      the filings shows a banker-led deal pipeline or a consultant-written strategy. Scored as
      fired-and-discounted, with the reason given.
- [x] **peer behaviour mindlessly imitated** — **FIRES, and this is the [E3-02] test the
      operator's bank method demands: what did this bank do while its peers were doing the
      foolish thing?** On **acquisitions ACNB did exactly what its peers did, in the same
      eighteen months**: Orrstown bought Codorus Valley (2024-07-01), Citizens & Northern bought
      Susquehanna (2025), Peoples Financial bought FNCB (2024), ACNB bought Traditions
      (2025-02-01). **Four of the eleven names in the Q2 row did the same thing at the same time.
      That is the imperative's fourth behaviour and it fires.**
      **But [E3-02]'s question is about the LAX behaviour, not the busy behaviour, and on that
      the answer is the opposite — and it is the most important finding in this Q3. There are
      four filed proofs.**
      **(1) Credit.** Net charge-offs of **0.13 / 0.06 / 0.16 / 0.08 / 0.08 / 0.02 / 0.02 / 0.01
      per cent** of average loans across eight years including the pandemic. Citizens & Northern,
      the same size and the same state, charged off **0.880%** in the twelve months to
      2026-06-30 — **73 times ACNB's 0.012%.** Fulton 0.304%, Orrstown 0.104%.
      **(2) The securities portfolio, which is where this entire industry was lax in 2020–2021
      and where three banks died for it in 2023.** ACNB's held-to-maturity book — the one that is
      *not* marked — is **$63,288 thousand of amortised cost against $56,576 thousand of fair
      value at 2026-06-30. The unrecognised loss is $6,712 thousand, 1.98% of tangible common
      equity.** Mark the **entire** securities portfolio to market and ACNB's tangible equity
      falls from $338,479 thousand to $331,767 thousand. **The bank that did what its peers did
      in 2021 put the duration into held-to-maturity and hid the hole; ACNB kept 88% of the
      portfolio in available-for-sale where the loss is already inside equity — and then in
      December 2025 crystallised $2.8 million of it on purpose.** The filing also states what it
      did not buy: *"The Corporation does not own investments consisting of pools of Alt-A or
      subprime mortgages, private label mortgage-backed securities, or trust preferred
      investments."*
      **(3) Commercial real estate concentration, measured against the regulatory guidance
      thresholds and disclosed by the filer itself in both filings read.**
      **Non-owner-occupied commercial real estate, construction and multi-family was 239.0% of
      the Bank's total risk-based capital at 2025-12-31 and 231.6% at 2026-06-30** — inside the
      **300%** level of the 2006 interagency guidance's second criterion — and **construction and
      land development alone, at $116,680 thousand against total Bank risk-based capital of about
      $397 million, is roughly 29%**, far inside the **100%** level of the first criterion. The
      second criterion's other limb (growth of 50% or more in the prior thirty-six months) **is**
      met, because the Traditions deal added $648.5 million of loans in one day — but the
      guidance requires **both** limbs, and the level limb is not met. **The number is falling,
      and ACNB reports it against the regulatory yardstick voluntarily; nothing requires that
      sentence to be in a 10-K.**
      **(4) Deposits.** Uninsured and non-collateralised deposits were **17.7% of Bank deposits
      at 2025-12-31 and 18.1% at 2026-06-30** (21.1% on the FDIC's broader definition), against
      **40–50% at the four largest banks operating in the same counties** (JPMorgan 47.2%, Bank
      of America 41.0%, Wells Fargo 48.1%, PNC 46.4%), with liquidity covering **329.7%** of
      them and the twenty largest depositors only **7.2%** of the book.
      **So the fourth behaviour fires on deal-making and is refuted on underwriting, on duration,
      on concentration and on funding. That is [E3-02] answered from the filings, and it answers
      in ACNB's favour on everything except the deals.**

**Capital allocation — the two buyback conditions [E5-08], plus [E4-31]'s third.**
- **(1) ample funds for operations and liquidity?** **Yes.** Bank Tier 1 leverage 11.25%, CET1
  14.30%, total risk-based 15.28% at 2026-06-30, each roughly double the well-capitalised
  minimum; FHLB capacity $1.29 billion of which $1.01 billion undrawn; $192.0 million of undrawn
  Fed Funds lines; $57.0 million of Discount Window capacity, fully available.
- **(2) repurchases at a material discount to conservatively calculated IV?** **Yes, on this
  run's own range, and the filed prices are the evidence.** **Q4 2025: 38,203 shares at $42.73
  and 17,140 at $46.36** (the Item 5 table) against a tangible book value per share of $32.22 and
  2025 EPS of $3.60 — **1.33x and 1.44x tangible book, roughly 12x earnings.** **Q2 2026: 179,407
  shares at a weighted average of $50.79** against tangible book of $33.42 and an annualising
  $5.66 — **1.52x tangible book and 9.0x earnings.** **Every share ACNB bought back in the last
  four quarters was bought below $51, and the stock closed at $64.57 on 2026-09-18.** Against the
  conservative end of this run's Q5 range ($52) the Q4 2025 purchases sit inside it and the Q2
  2026 purchases sit at it. **The condition is met, and management's execution on it is better
  than this run's own valuation would have been.**
- **(3) [E4-31]'s third condition — were shareholders supplied all the information they need to
  estimate value?** **Yes: tangible book value per share is reconciled on a dedicated page of
  every quarterly release, five quarters at a time.**
- **CAPITAL-ALLOCATION FLAG: LIVE — and it is about acquisitions, not buybacks.** **[E5-44]** is
  the governing rule for a stock deal — *"The intrinsic value of the shares you give in an
  acquisition must not be greater than the intrinsic value of the business you receive"* — and
  the arithmetic runs the wrong way. ACNB issued **2,035,246 shares at $41.10, $83,649 thousand
  of value**, when its own tangible book value per share was **$29.37**, i.e. it paid with paper
  at **1.40x its own tangible book**, to receive **$63,542 thousand of identifiable net assets of
  which $18,854 thousand was a core deposit intangible — $44,688 thousand of tangible net assets,
  so 1.88x tangible.** **ACNB paid 1.88x tangible book using paper worth 1.40x tangible book, and
  tangible book value per share was diluted by roughly $15 million, about 6% of pre-deal tangible
  equity.** The same shape is in 2020 ($57.9 million, 1,590,547 shares, $22,528 thousand of
  goodwill, $3,560 thousand of core deposit intangible) and 2017 ($33.3 million, 938,360 shares
  plus $4.5 million of cash, $13,272 thousand of goodwill, $2,418 thousand of core deposit
  intangible). **Cumulatively goodwill and intangibles are $84,800 thousand, 20.0% of book
  equity, and every dollar of it is premium over tangible assets that the selling banks' owners
  kept.**
  **Stated with the humility clause [E4-13]:** *"it is natural for CEOs to be optimistic about
  their own businesses. They also know a whole lot more about them than I do."* And the deal **is
  earning**: Traditions contributed $13.2 million of pre-tax income in eleven months, pro-forma
  2025 net income was $48,943 thousand against $37,051 thousand reported, and **H1 2026's ROTCE
  of 18.21% is the highest figure in the five-year series.** A tangible-book-dilutive deal that
  raises the return on the remaining tangible capital is not obviously wrong; it is a trade, and
  this is the trade being made repeatedly. **The flag BINDS POSITION SIZE, never the discount
  rate.**
- **[E2-51]'s inverse is checked and passes:** this is not a manager who turns his back on
  repurchases. 464,336 shares bought across 2025 and H1 2026, every one below $51.
- **[E2-48]'s superstar tell, recorded as present and deliberately not over-read:** *"these
  champs have made very few deals in recent years, and often have found repurchase of their own
  shares to be the most sensible employment of corporate capital."* **ACNB is doing both at
  once** — the largest acquisition in its history in February 2025 and the largest buyback in its
  history in the four quarters after. The buyback half is the [E2-48] behaviour; the acquisition
  half is not, and **no superstar claim is made** (there is a reason the corpus names only four
  in a generation).
- **[E2-60] checked against the dividend, because that is where restricted earnings hide.**
  Five-year dividends of $52,882 thousand and buybacks of $21,639 thousand against cumulative net
  income of $164,171 thousand — a 45% total payout — while book equity rose $162,002 thousand and
  **tangible book value per share rose 39.5%.** The payout did **not** cost the business its
  financial strength: Bank Tier 1 leverage went 8.81% → 11.25% across the same window. **These are
  not restricted earnings.**

**THE GUARDRAIL — checked before writing the verdict.**
- [x] Confirmed: **nothing in this Q3 is being used to promote the name.** Q2 was decided on the
      competitor rows before this section was written, the class was set at NARROW there, and
      **Q3 IN does not move it. [E2-37, E2-38, E3-39] govern: a bank that allocates capital well
      within its industry is a remarkable bank, not a remarkable business.** The five-year mean
      ROE of 11.53% is the top of an eleven-name row whose own mean is about 9.5% — *"a good
      managerial record … is far more a function of what business boat you get into than it is of
      how effectively you row"*, and this boat's whole row averages under ten per cent.
- [x] **This business does not require a great manager**, and no key-person moat defect is
      recorded at Q2 **[E4-23]**: the funding advantage is a property of nine counties and 168
      years, not of the chief executive.
- [x] **Is a great manager the reason to act? No.** No excisable-cancer case **[E2-35, E2-36]** is
      being made; there is no cancer and no corporate Pygmalion. The reason to consider acting, if
      any, is the funding position at Q2 and the price at Q5.
- **[E5-45]'s ABCs recorded as a Q6 monitoring item, not a Q3 finding:** arrogance, bureaucracy
  and complacency have no filed tell here yet, and the place to watch for them is the
  press-release language, which is already running to *"the resilience of our franchise"*.

- **VERDICT: [x] IN — at GATE weight.**
  *IN = **no disqualifier found**. This is NOT a finding that the managers are honest —
  "sincerity and empathy can easily be faked" **[E5-17]**, and Munger's own screen missed a
  reserve fraud at Royal Dutch; **[E5-26]**'s Sokol calibration is carried too, because a decade
  of strong record preceded that failure. **IN never promotes.** Three flags fired — the
  merger-cost add-back inside the pay metric [E2-57], the 2024 reserve release [E2-50], and a
  loans-held-for-sale policy change [E2-49] — each small, each disclosed and quantified in the
  filing that contained it, each read rather than scored. **One capital-allocation flag is LIVE
  and binds position size: three bank deals and one insurance-agency deal, done with paper at
  1.40x tangible book for assets at 1.88x tangible book, and the agency's pre-tax income is now
  below its pre-purchase level.*

---
## Q4 — WILL IT SURVIVE?

### Owner earnings — and for a bank the construction is the CONVENTION declared at Q3

The CONVENTION is stated in full at Q3 STEP 3 and is not restated here. Its two operative
parts: **"owner earnings" for a bank = net income − (c)**, and **(c) = the equity that must be
retained to hold the regulatory capital ratio constant while the balance sheet grows**, computed
on the **organic** perimeter because the CNR rule forbids a mean that crosses a merger unless it
is rebuilt on one perimeter.

**THE (c) RECORD, ORGANIC PERIMETER — and it is the opposite of Coastal Financial's, which is
why the same CONVENTION produces the opposite finding.**

| year | Δ assets | less assets acquired | **organic Δ assets** | Bank Tier 1 leverage, as filed | **(c)** | net income | **net income − (c)** |
|---|---|---|---|---|---|---|---|
| 2021 | +$231,625k | — | **+$231,625k** | 8.81% | **$20,406k** | $27,834k | **+$7,428k** |
| 2022 | −$261,480k | — | **−$261,480k** | 9.50% | **$0** | $35,752k | **+$35,752k** |
| 2023 | −$106,660k | — | **−$106,660k** | 11.12% | **$0** | $31,688k | **+$31,688k** |
| 2024 | −$24,017k | — | **−$24,017k** | 12.03% | **$0** | $31,846k | **+$31,846k** |
| 2025 | +$833,296k | $877,450k (Traditions, 2025-02-01) | **−$44,154k** | 10.92% | **$0** | $37,051k | **+$37,051k** |

**Five-year organic (c) total: $20,406 thousand, against cumulative net income of $164,171
thousand — a surplus of $143,765 thousand.** The balance sheet **shrank** in four of the five
years, so the existing business needed almost no retained capital to hold its unit volume. **The
same CONVENTION applied to Coastal Financial the same day produced $316.0 million of required
capital against $204.4 million earned, a $111.6 million shortfall; applied to ACNB it produces a
$143.8 million surplus. The construction is not tuned to a result.**

**And the balance sheet confirms it independently, which is the point of building it this way:**
book equity rose **$162,002 thousand** from 2020 to 2025 while cumulative net income was
**$164,171 thousand**, dividends **$52,882 thousand** and buybacks **$21,639 thousand** — and
**$83,649 thousand of stock was issued to buy Traditions.** Net of that issuance and of a
roughly $11 million AOCI drawdown, **retained earnings alone funded the dividend, the buyback
and the entire organic balance sheet, and no capital was raised from the market for operations
in any of the five years.** **[E2-60] passes on its own terms:** these are not restricted
earnings; the payout did not cost the business its financial strength, and Bank Tier 1 leverage
went **8.81% → 11.25%** across the same window.

**The acquisition's capital cost, stated separately in full and not netted into the above:** the
$877,450 thousand of assets acquired on 2025-02-01 required **$95,818 thousand** of Tier 1
capital at the Bank's 10.92% leverage ratio. **$83,649 thousand of that was supplied by issuing
2,035,246 shares and $12,169 thousand came out of retained earnings.** The acquisition programme
is capitalised almost exactly, in paper. **That is the honest shape of this company's growth: it
does not retain earnings to grow; it issues shares to buy growth and pays the earnings out.**

### MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38]

*"Using precise numbers is, in fact, foolish; working with a range of possibilities is the better
approach."* And [E4-38]'s remedy for date-selection distortion is to publish **every** window,
not to defend one. **Four are published. The spread between them is not noise — it is the
merger, and the CNR rule is why it must be shown rather than averaged away.**

| window | net income | perimeter | ex-accretion **[E4-41]** | less (c) | **owner earnings** | yield on $656,672k cap |
|---|---|---|---|---|---|---|
| **five-year mean, 2021–2025** | $32,834k | **the OLD company, $2.4–2.8bn of assets** | $32,834k | $4,081k | **$28,753k** | **4.38%** |
| three-year mean, 2023–2025 | $33,528k | mixed | $31,978k | $2,072k | **$29,906k** | **4.55%** |
| **FY2025 pro-forma, the filer's own (Note 2, as if Traditions had been owned from 2024-01-01)** | **$48,943k** | **TODAY's company** | **$42,783k** | $9,334k | **$33,449k** | **5.09%** |
| **H1 2026 annualised** | **$57,834k** | **TODAY's company** | **$52,134k** | $9,334k | **$42,800k** | **6.52%** |
| *(and FY2024 pro-forma, the filer's own)* | *$41,224k* | *today's company, prior year* | *~$35,000k* | *$9,334k* | *~$25,700k* | *3.91%* |

- **Short-window mean** (window: **H1 2026 annualised, the only period whose perimeter matches
  the company that exists**): **$42,800k**
- **Long-window mean** (window: **2021–2025**): **$28,753k**
- **Spread, conservative end:** the long window is **32.8% below** the short one.
- **Combined range** (window spread × the (c) band): **$25,700k to $42,800k**, a yield of
  **3.91% to 6.52%**.
- **Is that range too wide to reach a conclusion? NO, and the reason is specific, so this is a
  judgment and not a convenience.** The width is **entirely** the merger: the low end is a
  company with $2.4 billion of assets and 8.6 million shares, the high end is a company with
  $3.3 billion of assets and 10.2 million shares, and they are not the same business. **The CNR
  rule resolves it rather than the analyst's preference: only the post-2025-02-01 perimeter is
  the thing being bought, so the two pro-forma windows and H1 2026 are the live estimates and the
  five-year mean is carried as history.** Within the live perimeter the range is **$25,700k to
  $42,800k** — still wide, and the width is then honestly about **how much of the accretion and
  the low-beta funding lag persists**, which is the Q6 falsifier. **[E4-25]'s "too wide" verdict
  is NOT invoked, and the reason it is not is written here so a reader can disagree with it.**
- **Owner earnings by year, the CONVENTION:** 2021 **$7,428k** · 2022 **$35,752k** · 2023
  **$31,688k** · 2024 **$31,846k** · 2025 **$37,051k** · H1 2026 annualised **$37,418k** at the
  observed 5.6% growth rate of assets, **$48,500k** at nominal-maintenance growth only.
- **Maintenance capex — a DISCLOSED JUDGMENT, and for a bank it is not capex at all.** The
  corpus default (D&A as the proxy for (c), **[E3-44, E2-41]**) is **inapplicable and is not
  used**: ACNB's D&A was $6,737 thousand in 2025 of which **$4,257 thousand is amortisation of
  acquired core deposit intangibles** — the write-off of a purchase price already paid in shares
  already in the denominator — and its actual premises-and-equipment spend was **$1,076
  thousand, 0.03% of assets.** Neither number has anything to do with what this business must
  reinvest to hold its unit volume. **[E5-20]'s exception class is likewise inapplicable: nothing
  in ACNB's filings says depreciation understates renewal, because there is nothing to renew.**
  **So (c) is the CONVENTION's regulatory-capital construction, and the judgment inside it is
  the growth rate charged as maintenance. The band used is disclosed:**
  - **(c) LOW = $9,334 thousand** — 2.5% nominal asset growth (roughly inflation, so that real
    unit volume is held) at the 11.25% Bank Tier 1 leverage ratio. **This is the end used for
    the live-perimeter estimates**, because [E2-23]'s words are *"requires to fully **maintain**
    … its unit volume"*, and growth beyond inflation is discretionary expansion, not maintenance.
  - **(c) HIGH = $20,416 thousand** — the observed H1 2026 annualised asset growth of 5.6% at the
    same ratio, i.e. treating all of the growth actually being pursued as required.
  - **Where in the band it sits, with the reason cited from the filing:** at the LOW end, because
    the five-year record shows the company shrinking its balance sheet in four of five years
    while its FTE net interest margin rose from 2.82% to 4.23% — **this business demonstrably
    does not need asset growth to hold its competitive position**, and the filer says so in
    substance when it describes running off *"higher cost money market deposits from the
    Acquisition"* while noninterest-bearing deposits grow.
- **Stock compensation subtracted in full [E5-06]:** yes, and it needs no adjustment.
  **$1,411 thousand in 2025, 3.8% of net income and 2.6% of operating cash flow**, already an
  expense in every figure above. **[E3-70]'s grant-value measure is not constructed because it
  cannot change a verdict at this size** — the whole charge is under four per cent of earnings,
  and net restricted-stock issuance was **24,598 shares, 0.24% of the count.**
- *If the capex band changes the verdict → **UNKNOWABLE**.* **It does not.** At the (c) HIGH end
  the owner-earnings yield on the live perimeter is 5.70% instead of 6.52% and the Q5 verdict is
  the same one — below the floor. **The band moves the number and not the answer, which is the
  only condition under which a band is allowed to stand.**

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [x] **good** — attractive return, earned also on capital that is added
- [ ] gruesome — grows, eats capital, earns little

**Evidence, and the boundary call is argued rather than asserted.** It is not gruesome: the
return on the capital employed is **13.30% to 18.21% on tangible equity across five years and a
half, averaging 14.92%**, and the business consumed **$20.4 million of retained capital in five
years while earning $164.2 million** — the exact inverse of *"grows rapidly, requires
significant capital to engender the growth, and then earns little or no money."* It is **not
great either**, and two filed facts say so: **the rate did not rise as the years passed** —
reported ROE fell 14.35% → 9.44% across three consecutive years and diluted EPS is still 13.3%
below 2022 — and **incremental earnings are not free.** To grow the balance sheet 5% ($166
million of assets) ACNB must retain about **$18.7 million** of capital, roughly a third of a
year's earnings. That is precisely [E4-20]'s **good** account: *"an attractive rate of interest
that will be earned also on deposits that are added."* **[E4-43] is applied and the good class
passes** — *"nothing shabby"* — and **[E5-40]**'s benchmark is the right calibration: ~12% on
retained capital is *"quite satisfactory"*, and ACNB earns 13.8–18.2% on its tangible capital.
**Good ranks below great at Q5, and that is all the finding does.**
**Expressed as a yield, as [E4-20] requires so that it carries into Q5: 5.09% to 6.52% of the
current price, growing with the nominal size of nine counties.**

### Staying power — score all three **[E5-11]**, and the metric set is selected by business type first **[E5-37]**

- **(1) a large and reliable stream of earnings — PASS, and the reliability is the stronger
  half.** Net income was positive in every one of the seventeen filed years available (2009
  through 2025, $7.2 million to $37.1 million) — **including 2020, when a $9,140 thousand
  pandemic provision still left $18,394 thousand of profit.** Return on assets ran **1.04 / 1.35
  / 1.28 / 1.32 / 1.32 per cent** across five years, the tightest 31-basis-point band of the
  eleven-name row. **And the filer's own interest-rate simulation says the stream is
  rate-insensitive: a ±200 basis point twelve-month ramp changes net interest income by between
  −0.3% and −1.1%, against policy limits of 5% and 10%.** That is a genuinely unusual disclosure
  to be able to quote, and it is the reason the named death below is **not** a rate scenario.
- **(2) massive liquid assets — PASS on the sector-scoped reading, and the scoping is declared.**
  **[E2-61]** scopes strength 2 for float businesses; a bank needs its own scoping, because cash
  on hand is never the measure for a deposit-taker. The measures that are: **cash and cash
  equivalents $81,835 thousand; investment securities $529,774 thousand of which 88% is
  available-for-sale and therefore already marked; $1.01 billion of undrawn FHLB capacity
  against $1.85 billion of pledged loan collateral; $192.0 million of undrawn Fed Funds lines;
  $57.0 million of Discount Window capacity, fully available. Together, cash plus unencumbered
  securities plus collateralised borrowing capacity was 342.7% of uninsured and non-collateralised
  Bank deposits at 2025-12-31 and 329.7% at 2026-06-30.** Capital: **Bank Tier 1 leverage 11.25%,
  CET1 14.30%, total risk-based 15.28%**, each roughly double the well-capitalised minimum, and
  the holding company higher still at 11.55 / 14.49 / 16.25.
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — and this is the one that usually kills, so
  it is scored hardest. PASS at the holding company, QUALIFIED at the bank, and the
  qualification is structural rather than specific to ACNB.**
  **At the holding company there is essentially nothing to fund:** total holding-company debt is
  **$20.4 million** — $15.0 million of 5.875% subordinated notes issued 2026-03-12 and **not
  callable until 2031, due 2036**, plus $5.376 million of trust-preferred debentures assumed in
  the 2020 acquisition. Annual interest on both is about **$1.2 million against $26.9 million of
  dividends the Bank paid up to the parent in 2025 — 22 times covered.** **[E2-54]**'s test,
  run properly: *all* interest, payable and accrued, met out of current cash flow **net of ample
  capital expenditures** — borrowings interest of **$12,798 thousand annualised against $73,738
  thousand of pre-tax pre-provision earnings and $1,076 thousand of capex, 6.8 times covered**,
  and that is before treating deposit interest as what it is, the cost of goods rather than a
  capital-structure obligation.
  **At the bank, $480,895 thousand of time deposits (19.0% of deposits, including $75.0 million
  brokered) and $80 million of 2026 FHLB advances reprice or mature inside a year** — and that is
  ordinary for the business, matched by a loan book of which **$189,919 thousand matures within a
  year and $1,818,413 thousand carries variable or floating rates.**
  **[E3-52] is applied to the terms and not only to the quantity, and it is the reason this
  passes:** ACNB's $2.54 billion of deposits are *"liabilities without covenants or due dates
  attached"* in the [E3-52] sense for 81% of the balance — demand and savings money with no
  maturity, no covenant and no acceleration clause — while the covenanted, dated liabilities are
  the **$214.9 million of FHLB advances and $20.4 million of holding-company notes, together
  6.9% of the funding.** That is a materially different animal from a bank funded by brokered
  money and repo.
  **[E5-39]'s test is the one a bank structurally cannot pass on Berkshire's terms, and this run
  says so rather than pretending:** *"We will never be dependent on the kindness of strangers …
  cash is a lot like oxygen."* **ACNB's stated liquidity plan explicitly names the FHLB, the
  Discount Window, Fed Funds lines and the ability to raise brokered deposits — it depends on
  the kindness of strangers by construction, as every deposit-taker does.** What it can show,
  and does, is that the strangers are not needed: **the FHLB is $280 million drawn against $1.29
  billion of capacity, the Fed Funds lines and the Discount Window are entirely undrawn, and
  81.0% of the funding has no due date at all.** Scored as a pass with the structural limit
  named.
- **Leverage, named and quantified [E4-16, E3-29] — there is no ratio ceiling in this framework
  and the corpus supplies none:** **7.8 to 1 on book equity, 9.6 to 1 on tangible common
  equity.** The corpus's own bank comment is that twenty to one is *"a common ratio in this
  industry"* and it then **bought** a bank at that leverage; ACNB runs at less than half of it.
  **[E1-18]'s 25%-of-net-worth borrowing limit is the operator's own and is not a screen for
  companies; it is not applied here.** **[E5-29]** governs the reading: risk here means
  impairment, not price movement — the question is whether 9.6 to 1 can be broken, and that is
  the next section.

### Name the specific way THIS business dies **[E2-27, E3-24]** — modelled from EXPOSURE, not experience **[E4-40]**

**The corpus's own bank arithmetic, run on ACNB's own book first, because it is the benchmark
the framework supplies [E3-24]:** *"If 10% of all $48 billion of the bank's loans … produced
losses averaging 30% of principal, the company would roughly break even. A year like that —
which we consider only a low-level possibility, not a likelihood — would not distress us."*
**On ACNB at 2026-06-30: 10% of $2,398,104 thousand of loans losing 30% of principal is $71,943
thousand, against $73,738 thousand of annualised pre-tax pre-provision earnings. The company
would roughly break even — the 1990 sentence reproduces itself on this book to within 2.5%.**
And the allowance of **$24,006 thousand** absorbs the first third of it before earnings are
touched at all.

**But that is the generic test, and [E4-40] says the death list comes from what the filing shows
the business is EXPOSED to, never from what has recently happened** — *"all of us in the
industry made a fundamental underwriting mistake by focusing on experience, rather than
exposure."* ACNB's experience is a benign 0.01% charge-off rate late in a long expansion, which
[E4-40] calls *"not only useless, but actually dangerous"* as a guide. **So three mechanisms are
named and quantified from the balance sheet, and the third is the one that actually kills the
owner's return.**

**MECHANISM 1 — the commercial-property cycle. A real possibility; survivable with room.**
The exposure, from the filer's own tables: **commercial real estate $1,273,813 thousand (54.6%
of gross loans), of which 65.4% — $833,074 thousand — is non-owner-occupied**, the largest
sectors being *"retail and mixed-use commercial rental units, office complexes, apartment
complexes and hotels, motels and bed and breakfast entities"*, plus **$116,680 thousand of real
estate construction** and **$221,100 thousand of commercial investment-property loans sitting
inside the residential-mortgage line.**
- **Stress A, the office-and-hospitality slice:** 20% of the non-owner-occupied book impaired at
  a 25% loss severity = **$41,654 thousand**, against $73,738 thousand of pre-tax pre-provision
  earnings and a $24,006 thousand allowance. **One year's earnings absorbs it with $32 million
  to spare and the equity is untouched.**
- **Stress B, the break-even point:** **25.9% of the entire non-owner-occupied plus construction
  basket would have to default at a 30% severity to consume a full year's pre-tax pre-provision
  earnings.**
- **Stress C, the equity:** to erase the **$338,479 thousand** of tangible common equity the
  **whole $2.4 billion loan book** must lose **14.11% of principal** — **88 times ACNB's worst
  filed net charge-off year (0.16%, 2020)** and roughly 29 times the ~0.48% it charged off at the
  worst of 2010–2011.
- **Against the regulatory yardstick, which is where a supervisor would look first:** the basket
  is **231.6% of the Bank's total risk-based capital at 2026-06-30** (239.0% at 2025-12-31),
  **inside the 300% level of the 2006 interagency guidance's second criterion**, and
  construction alone is roughly **29% against the 100% level of the first.** **Neither threshold
  is crossed, the number is falling, and the filer volunteers it.**
- **Likelihood: a real possibility. Consequence: a poor year, not an impairment.**

**MECHANISM 2 — the deposit run, which is how three banks died in 2023. A low-level possibility,
and the filed numbers make it the weakest of the three.**
**Uninsured and non-collateralised deposits were 18.1% of Bank deposits at 2026-06-30** (21.1%
on the FDIC's broader definition), against **40–50% at the four largest banks operating in the
same nine counties.** The twenty largest depositors are **7.2%** of the book. Liquidity covers
**329.7%** of the uninsured money. **And the securities hole that killed the 2023 failures does
not exist here: held-to-maturity securities are $63,288 thousand of amortised cost against
$56,576 thousand of fair value, so the unrecognised loss is $6,712 thousand — 1.98% of tangible
common equity. Mark the entire portfolio to market and tangible equity falls from $338,479
thousand to $331,767 thousand.** To exhaust the liquidity a depositor flight would have to take
**more than 59% of all deposits, not 18%.** **Likelihood: a low-level possibility.**

**MECHANISM 3 — THE ONE THAT ACTUALLY KILLS THE OWNER'S RETURN, and the filer's own model cannot
see it. Likely, and already under way.**
Q2 established that the entire franchise is one variable: a cost of funds that is 41 basis
points below the median of its own 56-bank market today and averaged 64 below it across five
years. **The exposure is not an interest-rate move. It is the $600,711 thousand of deposits
paying zero and the $336,504 thousand of savings paying 0.03% while the 30-year Treasury pays
5.34%.** Nothing has to happen in the rate market for that to reprice; **the depositor simply
has to notice.**
**Quantified from exposure:** if the noninterest-bearing balances repriced to **3.0%** and the
savings balances with them, the annual cost is **0.030 × $600,711k + 0.0297 × $336,504k =
$28,015 thousand pre-tax — 38.0% of annualised pre-tax pre-provision earnings — with market
interest rates completely unchanged.** A milder version, simple convergence of the total cost of
deposits to the market median, costs **$10,259 thousand at today's 41-basis-point gap and
$16,014 thousand at the 64-basis-point five-year average gap — 13.9% and 21.7% of pre-tax
pre-provision earnings**, which takes ROE from 13.76% to roughly 11.5% and 10.4%.
**Combine Mechanism 3's mild form with Mechanism 1's Stress A and a year's earnings goes to
approximately zero:** $16,014 + $41,654 = $57,668 thousand against $73,738 thousand, before
tax, leaving the company solvent, well capitalised, and earning nothing.
**[E4-40] is the whole point of writing it this way, and the filing proves the point on itself.**
ACNB's own twelve-month earnings-at-risk simulation says a **±200 basis point ramp moves net
interest income by at most 1.1%.** That model is built on **experience** — the bank's own
historical deposit betas — and it is the correct model for a rate shock. **It cannot model a
behavioural repricing at unchanged rates, which is exactly the exposure the balance sheet
carries.** The evidence that the exposure is live and not theoretical is in the same filings from
the other direction: ACNB's cost of funding rose 82 basis points from 2021 to 2024 while the
market's rose 194 — **the lag is the asset — and its advantage over the market median has already
fallen from 127 basis points in 2023 to 41 in mid-2026 while the bank was doing nothing wrong.**

**THE SURVIVAL SHAPE. #11 THE PASS-THROUGH is the mechanism, and a new shape is PROPOSED,
argued and numbered: #25 THE SLEEPING DEPOSITOR.**
#11 fits the destination — the gain is competed away and the owner's return compresses while the
company survives — and it is recorded as the mechanism so the index stays honest if the proposal
is refused. **But the recipient and the trigger are both different from every instance of #11 in
the index.** In #11 (Toyota, Honda, UMC, Amazon Web Services, DoorDash, PubMatic, BlackRock) the
gain flows to the **customer or the supplier** because a **rival bids it away**. Here the gain
flows to the **supplier of the raw material** — the depositor — and **no rival has to do
anything at all**: the substitute is already on the table at a 400-basis-point advantage and has
been for three years. The counterparty only has to read its own statement. It is not #19 THE
SHELF (no concentrated intermediary takes the margin — the twenty largest depositors are 7.2% of
the book), and it is not #22 THE HABIT (Coca-Cola's habit is a purchase the customer enjoys and
pays a premium for; this habit **costs** the counterparty money every single day it persists).
**Its tells are checkable on any deposit-taking filer: a large noninterest-bearing balance whose
price is set at zero by inattention rather than by contract; a disclosed cost of funds far below
the market median with no contractual reason for it; a rate table in the filer's own MD&A
showing savings at 0.03% while the sovereign pays five per cent; and an interest-rate
sensitivity model built on historical betas that therefore cannot see the risk.** **The
distinguishing feature, and the reason it deserves a number: there is no observable event. #11
narrows when a competitor cuts price and you can watch it; #25 narrows one account at a time,
silently, and the only place it shows up is the funding-cost line two quarters later.**
- **Likelihood: [ ] likely — as a slow grind, ALREADY UNDER WAY and measured (127bp → 41bp of
  advantage in three years); [x] a real possibility as a fast repricing inside two years;
  [ ] a low-level possibility** for the combined credit-plus-funding year that takes earnings to
  zero.
- **[E4-51]'s iron prescription — the bear case stated better than its holders would state it,
  because that is the test of whether I am entitled to an opinion.** *A short seller would say:
  you are paying 1.93 times tangible book and 11.4 times two annualised record quarters for a
  $3.3 billion bank whose entire advantage is that its depositors have not yet asked for market
  rates; whose reported earnings per share are still below 2022's after three acquisitions and a
  71% larger share count; whose measured funding advantage has fallen by two thirds in three
  years; 26 basis points of whose margin is purchase-accounting accretion that is disclosed to be
  decaying quarter by quarter; and which has just bought a $7.8 million insurance agency whose
  segment earnings are lower than before it was purchased. Fifty-four per cent of the loan book
  is commercial real estate, two thirds of that non-owner-occupied, in office, retail and
  hospitality, at 232% of regulatory capital, and the 0.01% charge-off rate that reassures you
  is the late-cycle number [E4-40] calls dangerous. The management is good and the price already
  says so.* **That case is fairly stated and this run's Q5 agrees with the last sentence of it.**
- **VERDICT: [x] IN — GOOD, not great.**

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**Q1, Q2, Q3 and Q4 each show IN, so Q5 opens. This is the fourth name in this queue and the
first bank to get here.**

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*

**Honest pre-tax expectancy at this price: 8.4%** at the conservative end that **[E5-34]**
requires (*"we will buy the stock … if it sells at a reasonable price in relation to **the bottom
boundary of our estimate**"*), **10.7%** at the optimistic end, **centred about 9.3%.**
Construction, so it can be checked: pre-tax owner earnings of **$42.2 million to $53.5 million**
(after-tax owner earnings of $33.4–42.8 million grossed up at ACNB's own 20.2% book effective
rate) on a market capitalisation of **$656.7 million** is a pre-tax owner-earnings yield of
**6.43% to 8.15%**, plus sustainable growth in owner earnings per share of **2.0% to 2.5%** —
nominal growth in the deposits and buildings of nine Pennsylvania and Maryland counties, plus
about a point from buying back stock, **less** the funding-convergence headwind quantified at
Q4's Mechanism 3.

**BELOW ROUGHLY 10%, THE NAME IS NOT RANKED — IT IS QUIT ON, whatever the sovereign is. The
bottom boundary is 8.4% and the centre is 9.3%. ACNB is quit on at the floor.**

**And the floor's own basis is respected [E4-28]:** the 10% is *"true whether short rates are 6
percent or whether short rates are 1 percent"*, because its basis is guessed future opportunity
cost, not today's rate. **So the fact that 8.4% comfortably beats the 5.34% sovereign does not
save it.** This is the same disagreement the operator protocol names in the Berkshire case:
**above the bond, below the floor.** It is also where CB and GFF landed the same day.

**The growth belief is tested against the corpus's base rate [E4-35] and bounded [E4-44, E2-63].**
Nothing here needs 15% growth and none is claimed: the case rests on 2.0–2.5%, and **[E4-35]**'s
*"fewer than 10 of the 200 most profitable companies"* wager is therefore not engaged. But
**[E4-44]** is: *"the value of an asset … cannot over the long term grow faster than its earnings
do"*, and ACNB's earnings per share have grown at **minus 3.5% a year since 2022** on the
reported line. The 2.0–2.5% assumption is a forecast that the merger-year distortion reverses and
then nominal growth resumes — which H1 2026 supports and four prior years do not. **And the
ceiling is stated [E2-63]:** the upside is bounded by the nominal growth of nine counties and by
a return on tangible equity that the eleven-name row says tops out around 15–18% in a good year.
**There is no optionality here. A community bank cannot surprise on the upside by an order of
magnitude; that is what makes it understandable and it is also what caps it.**

**One book. Owner earnings against the bond. A DCF may run as an engine; it casts no vote
[E3-34].** No DCF was run. The numbers below are a yield, a multiple and a required-return
capitalisation — the corpus's practice **[E3-24, E4-21]**.

**1. THE YIELD**
- owner earnings **$33.4M to $42.8M** ÷ market cap **$656.7M** = **5.09% to 6.52%** ·
  sovereign **5.34%**
- *(and the unadjusted earnings yield, for the reader who rejects the CONVENTION's (c)
  altogether: $42.8M to $52.1M of ex-accretion net income on $656.7M = **6.52% to 7.94%**.)*

**2. WHAT THE PRICE ALREADY ASSUMES**
- **growth needed to justify the quote, at the [E4-28] floor:** for a 10% pre-tax expectancy at
  $64.57 the business must grow pre-tax owner earnings per share at **1.85% to 3.57% a year for
  ever** (10% less the 6.43–8.15% pre-tax yield). **That is not a heroic assumption — it is a
  plausible one — which is exactly why this is a price failure of 1.6 points and not of ten.**
- **what the business has actually done:** **diluted EPS −3.5% a year compounded, 2022 to 2025**
  ($4.15 to $3.60); **tangible book value per share +6.9% a year, 2020 to mid-2026** ($23.95 to
  $33.42); **net interest income +14.6% a year over the same span, almost all of it bought.**
  **The honest reading is that the record supports the assumption on tangible book and refutes it
  on earnings per share, and the difference between the two is the acquisitions.**

**3. WHAT YOU ARE PAID**
- return at the current price = **minus 0.25 to plus 1.18 points over the sovereign** on the
  owner-earnings yield (5.09–6.52% against 5.34%), or **plus 1.18 to plus 2.60 points** on the
  ex-accretion earnings yield before (c). **The owner of ACNB at $64.57 is paid, in the best
  construction this run can honestly build, about two and a half points over a thirty-year
  Treasury to own nine and a half times leverage against Pennsylvania and Maryland commercial
  property.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- sovereign used **5.34%** — **the bare rate, no per-name premium added.** *"It may look
  mathematical. But it's mathematical gibberish."*
- **Certainty is handled TWICE and neither place is the rate [E3-42, E4-11, E4-48]:** at the
  understanding gate (Q1 passed on a business whose three revenue mechanisms have not changed in
  168 years), and in the discount to value demanded at the end. It is priced **once** — the end
  margin — and is not stacked. **[E3-60]** grades that margin by understanding, and this is a
  creek-crossing rather than a Grand Canyon: simple business, plain accounting, 9.6 to 1
  leverage against real estate.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — a point estimate claims precision this method
cannot support:
- **conservative ≈ $45 a share** · **optimistic ≈ $65 a share** · **current price $64.57**
  *(construction: pre-tax owner earnings of $42.2M–$53.5M required to return the [E4-28] floor of
  10% pre-tax gives $422M–$535M, or $41–$53 a share, with no growth; allowing 2% perpetual growth
  and therefore an 8% required return gives $528M–$669M, or $52–$66 a share. Rounded to $45 and
  $65. **Cross-check that this run did not set the range to suit itself: management bought its own
  stock at $42.73 and $46.36 in Q4 2025 and at a weighted average $50.79 in Q2 2026 — all three
  inside the conservative half of this band, and all three well below today's quote.**)*

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- **floor verdict first: honest pre-tax expectancy 8.4% (bottom boundary) to 10.7% (top),
  centred 9.3%, against ~10% [E4-28] — BELOW, so the name is QUIT ON and the ranking lines
  below are not filled in.**
- points over sovereign, this name: *(not filled in — the floor was not cleared)*
- against the rest of the opportunity set: *(not filled in — the floor was not cleared)*
- *Take the best available, or nothing.* **[E2-74]**'s parking place is the answer for the money:
  *"our major parking place for money is medium-term tax-exempt bonds"* — liquid and waiting,
  because *"Mr. Market will offer us opportunities."* **The box exists so cash pressure never
  bends the standard, and a 1.6-point shortfall is exactly the size of gap that cash pressure
  bends.**

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — not used.
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case? **No.
      $64.57 is 43% above the conservative case of ~$45 and sits at the very top of the
      optimistic case of ~$65.** Three outcomes, and this is the third and then the second: the
      price is **above the whole conservative range** and **inside the full range** — either way
      the answer is *"no useful conclusion — move on."* **No margin is added on top;
      "startlingly low" is what you observe, not what you subtract, and nothing here screams.**
      **[E3-65]** is the calibration that settles it: the Washington Post was bought at *"about
      20 percent of the value to a private owner."* ACNB is available at **100 to 143 per cent**
      of this run's own value range.
- **Windage count: ONE.** Applied once, at Q4, in taking the **ex-accretion** pro-forma earnings
  as the bottom boundary of earning power and the **LOW** end of (c) at the same time — which
  are the same act of conservatism on one number, the earning power. **No margin is added at
  Q5, no premium is added to the rate, and no haircut is taken to the growth rate.** **[E4-48]**
  satisfied: realistic inputs, errors on the conservative side, and the conservatism spent once.
- **[E3-17]'s long-horizon qualifier, recorded because it cuts both ways and is the best argument
  for the other verdict:** *"If the business earns 6 percent on capital over 40 years … you're
  not going to make much different than a 6 percent return, even if you originally buy it at a
  huge discount"* — and the inverse is that **a business earning 14.9% on tangible capital
  delivers most of that to a patient owner over decades almost regardless of a 40% entry
  premium.** **The entry discount dominates short horizons and business quality dominates long
  ones, and both tests bind; neither excuses the other.** This run applies the entry test because
  Q5 is the entry question, and the floor is the entry standard.

- **VERDICT: [ ] IN — [x] OUT ON PRICE. Quit on at the ~10% floor [E4-28]. Ranking position: not
  ranked.**

*This is a failure on the PRICE, not on the business. All four business gates cleared. The
distinction matters operationally and the QLYS ruling of 2026-09-07 is the precedent for which
way it cuts: a Q2 failure is a failure on the business and a price alert on it would be a
category error, but **a Q5 failure is exactly the case where a price band is the right artifact**
— and it is armed at the fold.*

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]** — *"I believe in establishing yardsticks prior to the
act."* **Every threshold below is stated now, against a filed series, with the filing that will
report it.**

**THESIS-CONFIRMING metrics — what must keep being true for the Q2 class to hold:**
1. **Cost of funding earning assets below the median of the 56 institutions with an office in
   ACNB's nine counties**, FDIC Call Report, quarterly. Base: **1.274% against a 1.685% median at
   2026-06-30, an advantage of 41 basis points.**
2. **Noninterest-bearing deposits at or above 22% of total deposits.** Base: **$600,711
   thousand, 23.7% at 2026-06-30.**
3. **FTE net interest margin above 4.00%** ex-accretion. Base: **4.56% reported, roughly 4.32%
   ex-accretion, Q2 2026.**
4. **Return on average tangible common equity above 13%.** Base: **18.21% annualised, H1 2026;
   never below 13.30% in five years.**

**THESIS-BREAKING metrics AND THEIR THRESHOLDS — any one of these, and the Q2 class falls to
NONE or Q3 falls:**
1. **FUNDING — the primary falsifier, because Q2 rests on one variable.** *The advantage over
   the 56-bank market median cost of funding falls below **20 basis points for two consecutive
   quarters**, or ACNB's rank among the 56 falls outside the lowest fifteen.* Base 41bp and 8th.
   *(This is the metric that has already moved from 127bp to 41bp and is the reason the class is
   NARROW.)*
2. **THE NOTICE EVENT — Q4's Mechanism 3 becoming visible.** *Noninterest-bearing deposits fall
   below **20% of total deposits**, or the cost of interest-bearing deposits rises more than
   **40 basis points in any two consecutive quarters while the 30-year Treasury does not rise**.*
   Base: 23.7%, and 1.36% on interest-bearing.
3. **CREDIT — the [E3-02] answer reversing.** *Net charge-offs above **0.30% of average loans**
   in any twelve months, or nonaccrual loans above **1.00% of loans**, or the non-owner-occupied
   CRE plus construction plus multi-family concentration above **300% of the Bank's total
   risk-based capital**, which is the guidance level itself.* Base: 0.012%, 0.41%, and 231.6%.
4. **RESERVING — the [E2-50] flag recurring.** *A second year in which a reversal of the
   provision contributes more than **5% of pre-tax income** while nonaccrual loans rise.* Base:
   2024 was the first, at 6.8%.
5. **CAPITAL ALLOCATION — the live flag becoming a verdict.** *Another acquisition at more than
   **1.75x tangible book** paid in shares trading below **1.60x** ACNB's own tangible book, or
   any acquisition outside banking and insurance in the existing footprint, or **tangible book
   value per share falling year-on-year for a reason other than the AOCI mark**.* Base:
   Traditions at 1.88x paid with paper at 1.40x, and TBVPS +$1.31 in the last two quarters.
6. **DURATION — the thing this bank got right in 2021 and could get wrong next time.** *The
   held-to-maturity portfolio's unrecognised loss exceeding **5% of tangible common equity**, or
   the held-to-maturity share of securities rising above **25%**.* Base: 1.98% and 11.9%.
7. **THE ABCs [E5-45], as a qualitative watch and not a threshold:** guidance, a multi-year
   target, or an "adjusted EPS" appearing in an earnings release. **All three read zero today
   and the counts are in the file.**

**Next catalyst date:** Q3 2026 earnings release, expected in the second half of **October 2026**
(the Q3 2025 release was filed 2025-10-23 and the Q4 release 2026-01-22). **The 10-Q for
2026-09-30 will carry the cost-of-funds line and the CRE concentration sentence; the FDIC Call
Report for 2026-09-30 will carry the 56-bank market median.**

**The sell rule [E2-28]** — two triggers, three hold conditions. **Recorded for completeness and
expressly not operative, because nothing is owned: this is a Q5 price failure, there is no
position, and `Framework/THE HOLDINGS FRAMEWORK.md` governs if one is ever taken.**
- SELL if the market judges it more valuable than the facts indicate — **the trigger is
  pre-committed at above roughly $70 a share on today's earning power**, which is where even the
  optimistic case is exceeded by more than the margin.
- SELL if funds are needed for something more undervalued or better understood — standing.
- HOLD while: return on equity capital satisfactory (**ROTCE above 13%**) · management competent
  and honest (**the six falsifiers above**) · market does not overvalue.
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question,
in ACNB's own terms: **is a narrowing funding advantage an aberrational cycle — a low-beta bank's
lag compressing as rates fall, which reverses when they rise again — or has the depositor base
slipped in a way that permanently reduces intrinsic value?** *"And those beliefs change quite
gradually."* **The discriminating observation is stated in advance so the answer cannot be
back-fitted: if the advantage narrows while the sovereign FALLS, it is the lag and it is
aberrational; if it narrows while the sovereign is FLAT or RISING, the depositors have noticed
and it is permanent.** From 2025 to mid-2026 the 30-year Treasury was roughly flat and the
advantage fell 11 basis points — **the early reading is mildly adverse and is not yet
decisive.** **[E2-40]** is carried against my own gradualism: slow to conclude, and fast once
concluded.

**Do not trim winners [E5-14]. Position size — a judgment, stated: ZERO, because the floor was
not cleared.** Had it cleared, the size would have been **small** and the reason is written
rather than felt: **[E3-45]** says capital goes to rank #1 and this name would not have been
rank #1 at 8.4% to 10.7%; the **live capital-allocation flag binds position size** **[E5-08,
E4-13]**; **[E2-62]**'s licence condition is not met by a name whose entire moat is one line of
the income statement; and **[E2-53]**'s dominance reading was refused at Q2, so there is nothing
here that *"good or bad, will prosper."*

- **VERDICT: [x] IN** *(the falsifiers are pre-committed and each is a filed series with a
  threshold and a document; nothing is armed in the portfolio because nothing is owned)*

---
## SELF-AUDIT
- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 IN → Q3 IN → Q4 IN → Q5
      OUT ON PRICE → Q6 IN. Q5 opened only because the four business gates each showed IN, and
      the Q5 section says so in its first line.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The one place
      this was at risk is Q2, where the template's rule would hold the moat class PROVISIONAL
      because credit unions were not pulled. **The run did not carry a caveat into the verdict:
      it spent the uncertainty in the CLASS (NARROW, not WIDE), named the missing rung and its
      artifact, stated the direction of the missing evidence (adverse, because credit unions are
      tax-exempt and therefore cheaper funders), and closed the private and mutual banks properly
      by going to the FDIC Call Report for all 56 institutions in the footprint. The trade is
      disclosed in the file so a reader can reject it.**
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** No gate is
      UNRESEARCHED. **Two named sub-artifacts were not obtained and both are stated in place:**
      (1) **credit-union deposit pricing in ACNB's nine counties — NCUA Form 5300 call reports
      and quarterly Financial Performance Reports, public, at ncua.gov**; (2) **any ACNB CEO
      letter to shareholders, for the [E2-72] authorship test — it would live in the glossy
      annual report at investor.acnb.com and is not an SEC filing.**
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known.** None was written.
- [x] **Step 0: the filing was read, with accession numbers; a figure was cross-checked.** Twelve
      documents listed with dates and accessions. FY2025 net income of $37,051k matched across
      four independent places in the same filing; equity recomputed from A − L; 2022 book value
      per share recomputed to the cent against the filer's own five-year table.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.**
      Four windows published per [E4-38], the spread quantified at 32.8%, the reason for the
      spread named as the merger, and the CNR rule used to decide which windows are live rather
      than the analyst's preference. **The (c) band ($9,334k–$20,416k) is disclosed as a
      judgment, the end used is named, and the file states that the band moves the number and not
      the verdict.** The corpus's D&A default for (c) is explicitly **refused with reasons** for
      this business type, not silently skipped.
- [x] **Competitor row filled.** **Row A: ten SEC-registrant holding companies, five years, one
      specification. Row B: all 56 FDIC-insured institutions with a banking office in ACNB's nine
      counties, six dates, from the Call Report.** No peer figure was inherited from a prior run
      in this repository; every one was computed or read this session.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** 5.34%, USD,
      **US Treasury** 30-year par yield, 09/18/2026. **Not FRED.**
- [x] **Value stated as a round-number range, not a point estimate.** ~$45 to ~$65.
- [x] **One bar chosen, not both; windage count stated.** Bar 2, the screamer test. Windage ONE,
      applied at Q4.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $64.57, 2026-09-18
      close, `tools/sources.py price()`, **aggregator FLAGGED**, order-of-magnitude cross-checked
      against the $50.79 weighted-average repurchase price in the Q2 2026 release and the $42.73
      and $46.36 in the 10-K's Item 5 table.
- [x] **A bank was run on the corpus's bank method, and the four required elements are each
      present:** Q3 declared at **gate** weight with the case argued [E3-29]; the **[E3-02]**
      conformity test run against the bank's own filings and answered four ways; the reserving
      record judged against **subsequent** charge-offs [E2-50] with the [E2-67] benchmark's
      absence stated honestly; the survival test built as a **quantified named scenario**
      [E3-24] and not as a ratio; no leverage ceiling applied; and the return on equity capital
      **[E2-01]** measured under a construction **labelled CONVENTION with its rationale**
      [PRIME RULE 3].
- [x] **`python tools/check_framework.py` PASS** — recorded at the fold with its output.
- [x] **Run committed to git**, incrementally, under the write-early protocol: the empty template
      first, then Step 0 + Q1 + Q2, then Q3, then Q4 through the register. **Every commit carried
      a pathspec.**
- **ONE THING THIS RUN WOULD DO DIFFERENTLY, recorded because operator rule 6 asks for it:** the
  FDIC Call Report layer should have been built **first**, before the SEC peer row. It is a
  better instrument for a bank on every count — it is the issuing authority, it covers private
  and mutual banks, it is bank-level rather than holding-company-level, and it publishes the four
  ratios directly instead of requiring them to be computed. **The SEC row took most of this run's
  peer effort and the FDIC row decided the question.** That belongs in the tooling note.

## REGISTER
- Verdict: [ ] IN [x] **OUT — but on the PRICE, at Q5, not on the business** [ ] UNRESEARCHED
  [ ] UNKNOWABLE
- **One line:** **All four business gates IN — the first bank in this queue to clear them — and a
  FAIL at Q5 on price: ACNB Bank funds itself 41 basis points below the median of all 56
  FDIC-insured institutions in its own nine counties and 64 below it on a five-year average,
  carries the highest net interest margin, the best efficiency ratio and the highest return on
  assets of the eleven banks that compete with it, and charges off 0.012% of its book against
  Citizens & Northern's 0.880% — but at $64.57, 1.93x tangible book, the honest pre-tax
  expectancy is 8.4% at the bottom boundary and 9.3% at the centre, below the ~10% floor
  [E4-28], and above the 5.34% sovereign on every construction.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable; no gate is UNRESEARCHED. The two named
  sub-artifacts are the NCUA 5300 credit-union call reports (ncua.gov) and any ACNB CEO
  shareholder letter (investor.acnb.com, not an SEC filing).
- **If UNKNOWABLE:** not applicable.
- **THE STRONGEST SINGLE FACT AGAINST THIS CONCLUSION [E4-26, E4-51], and it is a fact about my
  own arithmetic rather than about the company: ACNB's two most recent quarters earned $13.7
  million and $15.2 million, and if those are the run rate rather than a peak, the company is
  earning $57.8 million and is priced at 11.4 times earnings and 1.93 times a tangible book value
  that is compounding at 6.9% a year — and my 8.4% bottom boundary is built on the FY2025
  pro-forma, a year that contained $10.7 million of merger costs and a securities loss. On the
  H1 2026 numbers alone the pre-tax expectancy is 10.7% and this file says BUY.** The reason it
  does not is **[E5-34]**'s instruction to price against the bottom boundary and **[E4-18]**'s
  prohibition on narrowing until the answer appears — but two record quarters is thin evidence
  for a peak and thin evidence for a run rate alike, **and a reader who prefers the newer
  perimeter reaches the opposite verdict from the same file.** That is the honest state of it.


---
## ADDENDUM 2026-09-20 - the shape this run numbered #25 is #30 in the index
*Operator rule 6: corrected here, not by editing the text above.* This file proposed THE SLEEPING DEPOSITOR as shape **#25**. The CCB fold took #25 for THE INDEMNITY in the same hour, and `Screens/SURVIVAL SHAPES - index.md` carried two rows numbered 25 until the 2026-09-20 audit. **THE SLEEPING DEPOSITOR is now #30 in the index**; the argument above is unchanged, and every reference to "#25" in this file means that shape.
