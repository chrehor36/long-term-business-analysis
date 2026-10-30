# Company Run — Edison International (NYSE: EIX) — 2026-10-22
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied 2026-10-22 before any fetch; commit f851472b.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-23, after the run was committed (6bbe1ccf): `PORTFOLIO.md` read for this one ticker; **not held**.*

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md`, with the brief's one stated departure: the
lines of evidence were derived by the analyst from the 10-K's Item 1, Item 1A and Item 7 (listed below), and the
competitor rule told the analyst to take the rivals the 10-K names. Research folder: `Test Runs/_research 2026-10-22 EIX/`
(notes, `fetch.py`, `xbrl.py`, `calc.py`, the `tools/run.py` output, the ledger rows on utilities; raw filings in its
ignored `cache/`).

**Contamination, declared.** (1) The session opened with a git status that showed the subjects of the five latest commits,
which are another company's v5 run (a utility, DUK): its box, its Q7 figures and the names of its framework notes ("net or
gross debt credit, credit inside the maintenance case, whose tax at a utility, the cap inside ten years, a monopoly's named
rivals"). I read them before starting. I did not open that run, and every choice below is argued from the framework's own
text; but the notes named choices I also faced, and the reader should know I saw them. (2) The same status listed
untracked research-folder names of two other companies (AYI, ARCB); nothing of their content was seen. (3) The memory index
loaded with the session carries one-line queue facts (counts of gate-clearers, a wave paused); none names EIX. (4) To avoid a
file-name collision I listed `Test Runs/` filtered to today's date; it returned no file. Nothing about EIX or any former
name (SCECorp) was seen in any of these.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $57.90 (2026-10-22, the quote printed by `tools/run.py`; **aggregator, live quote only, flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: **384,813,979** Edison International common shares outstanding as of
  July 23, 2026 (10-Q for the quarter ended 2026-06-30, filed 2026-07-30, accession `0000827052-26-000059`;
  `python Screens/cover_shares.py EIX`). The tool printed a second line, 434,888,104, and an "arithmetic sum, NOT a share
  count" of 819,702,083: the second line is the common stock of Southern California Edison Company, the co-registrant of
  the combined filing, all of it held by Edison International (10-Q balance sheet of SCE, "434,888,104 shares issued and
  outstanding"). It is not an EIX class and is not added. Cross-check: the 10-Q balance sheet shows 384,787,767 EIX shares
  issued and outstanding at 2026-06-30 and no treasury line (California no-par stock); the cover's July count is 26,212 higher,
  consistent with plan issuance. No 8-K or prospectus after the 10-Q bears on the count (the only filings since 2026-07-31 are
  Forms 3 and 4 and a Schedule 13G/A).
- **Market cap:** 57.90 × 384.813979M = **$22,281M**.
- **Sovereign for the earnings currency (USD):** **5.29%**, the 30-year par yield on the US Treasury daily par yield curve,
  2026-10-22 (issuing authority; printed by `tools/run.py` from `tools/sources.py`).
- **Filings read** (operator rule 4): the combined EIX/SCE **10-K for 2025** (filed 2026-02-18, accession
  `0000827052-26-000012`): Item 7 (MD&A) in full through Critical Accounting Estimates, Item 1A (Risk Factors) in full, Item 1
  (Business: the regulation, ratemaking, competition, properties and the Southern California Wildfires sections), the
  consolidated statements of income, balance sheets and cash flows, Note 1 on the Wildfire Fund; the **10-Q for Q2 2026**
  (accession `0000827052-26-000059`): Management Overview, results, the balance sheet and cash flows, the VIE and debt notes;
  the **proxy** (DEF 14A filed 2026-03-13, accession `0001104659-26-027655`), its compensation sections searched; the **10-K
  for 2021** (accession `0000827052-22-000006`), its operating-cash-flow table and footnote. The recent 8-K list (2025-01 to
  2026-07) was read by item number: earnings releases, note issues (February and April 2026), the December 2025 parent term
  loan, the April 2026 meeting results; no rename, merger, spin-off or split.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities, 2025, **$5,800M**
  on the consolidated statement of cash flows of the 10-K (accession `0000827052-26-000012`) equals the XBRL figure the tool
  printed; capital expenditures $6,515M likewise.
- `python tools/run.py EIX`, arithmetic lines only (Part VII): owner cash by the tool's two lines, 2023 to 2025: OCF less stock
  pay less capital spending −2,093, −750, −772; OCF less stock pay less depreciation 720, 2,091, 2,506 (USD millions). The
  five-year figures on the tool's other window: −2,350 (capex) and 708 (depreciation). Stock pay 46, 57, 57. The tool's "other
  capital payment" lines (117, 168, 136) are dividends on SCE's preference stock, a financing payment to a senior holder; they are
  deducted below as preferred dividends, not as capital spending. Its column d4 (`LiabilitiesOtherThanLongtermDebtNoncurrent`) is
  not debt and is not used. Nothing the tool prints as a rule, a yield verdict or a v4 id is used.

### The lines of evidence, chosen by the analyst from the 10-K (the brief's departure)
1. **The earning engine: the authorized return on a growing rate base** (Item 7, Cost of Capital Application, Capital
   Program, Rate Base; Item 1, Overview of Ratemaking Process). ROE 10.03% for 2026 to 2028 on a structure of 52% common
   equity, 43% long-term debt and 5% preferred; FERC ROE 10.3%; rate base $48.2B at year-end 2025; capital spending forecast
   $37.5B to $40.6B for 2026 to 2030.
2. **The wildfire liability and the AB 1054 / SB 254 regime** (Item 1, Southern California Wildfires; Item 1A, Operating
   Risks; Item 7, Eaton Fire and the 2017/2018 Wildfire/Mudslide Events). This is the line the rest of the file turns on.
3. **Cost recovery and disallowance** (Item 1A, Regulatory and Legislative Risks; Item 7, Regulatory Proceedings and Impact of
   2025 GRC): the share of wildfire losses the CPUC let customers bear, and the disallowances.
4. **Financing and the parent** (Item 7, Liquidity and Capital Resources; Item 1A, Risks Relating to Edison International and
   Financing Risks): debt, preferred stock, credit ratings, the parent's dependence on SCE dividends and California dividend law.
5. **Affordability and departing load** (Item 1, Competition; Item 1A, Competitive and Market Risks): CCAs, Direct Access,
   rooftop solar and net metering, and the rate pressure they and the capital plan create.

### The balance sheets first, ten year-ends (read here because the file closes before Q4) **[M2025-032]**
Transcribed by `tools/run.py` from the first-filed XBRL of each 10-K and read against the 2025 and 2021 statements. USD millions.

| year-end | assets | long-term debt (non-current) | EIX equity incl. SCE preference | SCE preference | EIX preferred | common equity | shares (M) | common book a share | retained earnings |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | 51,319 | 10,175 | 14,187 | 2,191 | 0 | 11,996 | 326 | $36.8 | 9,544 |
| 2017 | 52,580 | 11,642 | 13,866 | 2,193 | 0 | 11,673 | 326 | $35.8 | 9,188 |
| 2018 | 56,715 | 14,632 | 12,652 | 2,193 | 0 | 10,459 | 326 | $32.1 | 7,964 |
| 2019 | 64,382 | 17,864 | 15,496 | 2,193 | 0 | 13,303 | 362 | $36.7 | 8,382 |
| 2020 | 69,372 | 19,632 | 15,949 | 1,901 | 0 | 14,048 | 379 | $37.1 | 8,155 |
| 2021 | 74,745 | 24,170 | 17,789 | 1,901 | 1,977 | 13,911 | 380 | $36.6 | 7,894 |
| 2022 | 78,041 | 27,025 | 17,522 | 1,901 | 1,978 | 13,643 | 382 | $35.7 | 7,454 |
| 2023 | 81,758 | 30,316 | 17,944 | 2,443 | 1,673 | 13,828 | 384 | $36.0 | 7,499 |
| 2024 | 85,579 | 33,534 | 17,740 | 2,175 | 1,645 | 13,920 | 385 | $36.2 | 7,567 |
| 2025 | 94,026 | 36,070 | 19,259 | 1,680 | 497 | 17,082 | 385 | $44.4 | 10,714 |

(Common equity = total equity less SCE preference stock less EIX preferred stock; 2025 from the 10-K balance sheet:
preferred $497M, common stock $6,362M, AOCI $6M, retained earnings $10,714M.)

**What the figures say.** Long-term debt rose from $10.2B to $36.1B (3.5 times) while total equity rose by about a third.
Common book a share was **flat for eight years**, $36.8 at 2016 and $36.2 at 2024, although $3.3B of new common was sold in
2019 and 2020 (`ProceedsFromIssuanceOfCommonStock` 2,391 and 912) and $2.0B and $0.5B of preferred in 2021 and 2023; the 2025
jump to $44.4 is the recognition of the TKM and Woolsey wildfire cost recoveries approved that year (10-K MD&A: non-core
earnings of $1,978M at SCE). **Retained earnings fell from $9,544M (2016) to $7,454M (2022)**: over those years the common
dividend exceeded what the company earned under GAAP, and the dividend was paid while equity was raised. Regulatory assets
(non-current) went from $7.5B to $13.0B, of which $3.1B at 2025 sits in a securitization vehicle. Cash is kept near zero
($158M at 2025). The balance sheet carries a $1.7B "Wildfire Fund contributions" asset (shareholder money paid into a state
insurance fund, being amortized as an expense) and $1.3B of wildfire-claims liabilities. **What they cannot say:** the size of
the Eaton Fire liability, which the filing states it cannot estimate (Q2 below). **What the management would like them to
say:** "core earnings", the figure the 10-K leads with, which treats wildfire claims as non-core from July 2023 (10-K MD&A,
Highlights). The row asks what the figures "can’t say and what the management would like them to say" **[M2025-032]**.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own SCE's earnings if the market closed for years, "Would I
be happy buying this stock if the market closed for five years?" **[M1997-109]**, and for a regulated utility the answer turns on
what the regulator and the courts do, not on the quote. The market serves and does not instruct: a price of nine times core
earnings tells me nothing about value until the facts are read, "It just tells us prices." **[M2006-077]**. Margin of safety: if
the case needs pencil and paper "it’s too close to think about" **[M1996-084]**. No macro forecast enters: no view on rates or on
California politics is used as a forecast **[M2000-094]**; the legislative and court risk is read only as the filings state it.
**Contrary evidence, written down as found** **[M1997-127]**, looking for "what’s wrong in things" **[M2025-013]**:
(a) the 10-K's own words, "it is probable that Edison International and SCE will incur additional material losses in connection
with the Eaton Fire" and "are currently unable to reasonably estimate a range of losses"; (b) SCE "believes that it is likely
that its equipment was associated with the ignition of the Eaton Fire" (10-Q, Q2 2026); (c) a Los Angeles District Attorney
investigation "for the purpose of determining whether any criminal violations have occurred", and fines and penalties "will not
be recoverable"; (d) the AB 1054 prudency standard has never been applied by the CPUC in a final decision; (e) common book a
share flat 2016 to 2024; (f) S&P cut SCE to BBB- with a negative outlook after SB 254; (g) the dividend paid in years when owner
cash after all spending was negative (Step 0 and Q7 computation). On the other side, written down as found: AB 1054 caps
SCE's reimbursement for the Eaton Fire at about $4.3B if it kept its safety certification and is not found in conscious or
willful disregard; the Wildfire Fund reports about $21B of claims-paying capacity for the fire; and the CPUC let SCE recover
60% (TKM) and 35% (Woolsey) of the 2017/2018 losses.

## THE STANDING RULE
The buyer's conduct: a holding bought with borrowed money, or sized so that its loss would harm what the buyer needs, is ruled
out whatever the questions conclude, "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. This name carries a tail in which the
common equity is lost (Q2, the willful-disregard case), so its size in any portfolio would have to survive a zero, "anything
times zero is zero" **[M2007-050]**. Nothing here closes the file.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will look like
  in five or 10 years" **[M2012-065]**; the first step is "trying to identify the key variables in that particular business, and
  evaluating how predictable they were first" **[M1998-044]**.
- **The key variables, from the filings.** SCE earns an authorized return on its rate base: "SCE's CPUC authorized return on
  investment is established by multiplying an authorized rate of return ... by SCE's authorized CPUC rate base" (10-K, Item
  1A). Revenue is decoupled from volume: "CPUC rates decouple authorized revenue from the volume of electricity sales" (10-K,
  Item 1, Overview of Ratemaking Process), so commodity prices and departing load reach the customer's rate, not SCE's earnings
  ("exposure to commodity prices is not expected to impact earnings", Item 7, Market Risk). The variables are therefore (1) rate
  base ($48.2B at 2025; forecast $50.8B to $67.9B weighted average for 2026 to 2030), (2) the allowed return and structure
  (ROE 10.03%, 52/43/5, set to 2028 with an adjustment mechanism), (3) how much of what SCE spends the CPUC disallows, and
  (4) the wildfire liability. The first three are written down by the insiders themselves (the rate-base forecast is in the
  10-K) and are as predictable as utility economics get: "when you get an allowed return in the electric utility you’re almost
  certain of earning it, I mean, if you behave yourself" **[M2010-037]**. Do the past statements tell me the future ones **[M2008-033]**?
  For the engine, yes: authorized revenue is published by the regulator line by line (10-K, 2025 GRC table: $9,660M, of which
  authorized return $2,970M).
- **The fourth variable, and where it is judged.** The wildfire liability is important, and the filing says it cannot be
  estimated. The framework's own paragraph on the regulated utility places it: "the regulatory climate at Q2 and Q9" (Q7, The
  regulated utility). I therefore read it as the castle question, what could "destroy, or modify, or
  reduce" the business's strengths **[M2000-014]** (Q2), not as a failure to understand how SCE makes money. I understand "the economic dynamics
  of the industry" **[M2011-014]**: a franchise monopoly paid a set return for capital it is told to deploy. Whether the owners keep
  that return is the next question.
- Routing: no fast-changing technology closes this at Q1 (the grid's economics are a regulator's arithmetic; rooftop solar and
  CCAs are read at Q2). Not a bank. Not a holding company of parts with different economics: Trio, the only other business, was
  "not material to report as a separate business segment" (10-K) and was disposed of in Q2 2026 (10-Q).
- **VERDICT: IN**, on the engine's key variables, which the filings state and the regulator sets **[M1998-044]**, **[M2010-037]**;
  the wildfire variable is carried to Q2 by the framework's own placement. *(The doubt row **[M2002-092]** pulls toward closing
  here instead; the pull is recorded under "What in the framework was wrong or unclear". The box would be the same.)*

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**

- **The castle questions.** What keeps it standing is a franchise: SCE owns and runs the wires across "an approximately 50,000
  square mile area" with about 13,000 circuit-miles of transmission and 70,000 of distribution (10-K, Properties). A customer who
  leaves for a CCA or an Electric Service Provider stays on the wires: "SCE remains that customer's transmission and
  distribution provider" (10-K, Competition). The key factor is the regulatory compact, the regulator's promise of a return on
  capital the utility is told to deploy. "how permanent are they?" **[M1995-038]** is the whole question, because its terms for wildfire are being
  rewritten while this is read (SB 254 of September 2025; the state's April 2026 report, which "does not recommend or endorse
  any specific policy approach", 10-Q).
- **The attacker with money.** Nobody builds a second distribution grid in Los Angeles County; the case is the railroad's, "You
  really couldn’t create another railroad" **[M2013-054]**. One crack: FERC removed the incumbents' right of first refusal on
  certain new transmission, and "independent service providers were selected" in CAISO solicitations (10-K, Competition);
  transmission is $0.8B to $1.1B a year of a $7B to $9B capital plan.
- **Pricing power, and the agony before a rise.** SCE has none of its own: the CPUC sets every rate, and the 10-K says the
  pressure runs one way, "As customer rates increase, the CPUC may face greater pressure to approve lesser amounts" (Item 1A).
  The prayer session is held at every rate case **[M2005-020]**. The speakers name the danger for a bill people cannot give up:
  "they express their outrage at inflationary increases and said, “Let’s nationalize the whole thing.”" **[M2009-088]**. The 2025
  GRC disallowed $88M of past capital (impaired) and the 2021 GRC memorandum-account decision $65M of expenses (10-K, MD&A).
- **Unit volume and share of mind.** Volume does not reach earnings (decoupling), but departing load raises everyone else's
  rate: CCAs at about 21% and Direct Access at about 15% of total service load by end-2026, with rooftop solar required on most
  new homes since 2020 (10-K, Competition). Management projects demand to "nearly double between 2025 and 2045"; that is a
  projection and is not used.
- **The low-cost position; the low bid.** Not tests a monopoly faces from its customers; the analogue is affordability, which the
  10-K manages to a target ("bundled system average rate will rise at a compound annual growth rate equal to or below inflation
  through 2030").
- **Widening or narrowing.** Narrowing, on the filings: S&P downgraded SCE after SB 254 (BBB-, negative); the CPUC let SCE
  recover 60% of the TKM losses and 35% of the Woolsey losses, so the owners bore the rest (2017/2018 events: $9.9B of losses,
  $2.0B insurance, $3.4B rates, $3.2B after tax charged to earnings, 10-K MD&A); the $2.4B initial and $95M annual Wildfire Fund
  contributions "are not recoverable through electric rates"; under SB 254 SCE expects to exclude $2.9B of wildfire-mitigation
  capital from the equity portion of rate base, and has agreed, if triggered, to contribute $2.4B to the Continuation Account
  over 2029 to 2045 plus a $1.9B contingent share (10-K, Item 1 and Note 1). Widening: AB 1054's cap and presumption of
  prudence, the SB 254 Continuation Account (up to $18B), an approved 2026 to 2028 Wildfire Mitigation Plan and a safety
  certification valid to at least March 2027 (10-Q).
- **What could destroy, modify or reduce it** **[M2000-014]**. The Eaton Fire of January 2025: SCE "believes that it is likely
  that its equipment was associated with the ignition"; it had recorded $1.6B of settlement losses by 2026-06-30, with $917M from
  customer-funded self-insurance (now exhausted), $645M from the Wildfire Fund and $70M through FERC rates; "it is probable that
  Edison International and SCE will incur additional material losses" and they "are currently unable to reasonably estimate a range
  of losses" (10-Q). The bounds the statute sets: if the CPUC disallows costs, SCE reimburses the fund up to the Liability Cap of
  about $4.3B (about $11 a share, a fifth of the market value); if the fund administrator finds "conscious or willful disregard of
  the rights and safety of others", SCE reimburses all disallowed withdrawals, uncapped; fines and penalties are unrecoverable;
  losses beyond the fund's reported $21B capacity fall to SCE, and to rates only if prudent (10-K and 10-Q). A bellwether jury trial
  is set for January 2027; the District Attorney's investigation is open. And the next fire: SCE "has determined that approximately
  27% of its service area is in areas identified as high fire risk" (10-K, Business). The legal ground is strict liability:
  "California courts have previously found utilities to be strictly liable for property damage ... regardless of fault, by applying
  the theory of inverse condemnation" (10-K, Note 12).
- **Change, and whether it is for the better.** AB 1054 (2019) and SB 254 (2025) are offered as the change that restores the
  compact. The filing records that it has not been tested: "The CPUC has not yet issued a final decision applying the California
  Wildfire Legislation prudency framework to a wildfire cost-recovery proceeding" (10-Q). The one litigated pre-AB 1054 decision went
  against the utility: in 2017 the CPUC denied SDG&E recovery of its 2007 fire costs, and every court declined review (10-K, Item 1).
  The speakers record change for the better in a field ("the railroads were a terrible business for decades and decades and decades
  and then they got good." **[M2017-026]**), and the framework credits it only on the evidence of a full cycle **[M2005-020]**,
  **[L1995-022]**; until then the question is TOO HARD (NATURE) (Q2, Change, and what it does to a castle).

**The competitor row.** The 10-K names no rival company. Its Competition section names classes, not companies: CCAs ("governmental
entities formed by cities, counties, and certain other public agencies"; twelve in SCE's area, none named; they do not file with the
SEC, flagged), Electric Service Providers (unnamed), independent transmission developers (unnamed) and customer-owned generation. The
only other companies it names in SCE's field are PG&E and SDG&E, as the two other utilities in the Wildfire Fund. **CONVENTION of
this run:** the field for Q2 is the three California investor-owned electric utilities, the two others read from their own filings.
Rationale: they share the regulator, the liability law and the fund, so their records over the span are the field's record, while
the named classes of "competitor" are not companies that file.

| | earnings to common, USD M, by year | sum | book a common share | source |
|---|---|---|---|---|
| **EIX** | 2016 1,311 · 2017 565 · 2018 −423 · 2019 1,284 · 2020 739 · 2021 759 · 2022 612 · 2023 1,197 · 2024 1,284 · 2025 4,457 | 11,785 (2016-2025) | $36.8 (2016) → $36.2 (2024) → $44.4 (2025) | EIX 10-Ks, XBRL of each; FY2025 `0000827052-26-000012` |
| **PG&E Corp (PCG)** | 2016 1,393 · 2017 1,646 · 2018 −6,851 · 2019 −7,656 · 2020 −1,318 · 2021 −102 · 2022 1,800 · 2023 2,242 · 2024 2,475 · 2025 2,593 | **−3,778** (2016-2025) | $35.4 (2016: equity 17,940 / 507M sh) → $14.8 (2025: 32,540 / 2,198M sh) | PCG 10-K XBRL; FY2025 `0001004980-26-000009`, FY2020 `0001004980-21-000007`; in bankruptcy 2019-2020 (emerged 2020-07-01, per the EIX 10-K) |
| **SDG&E** | 2018 669 · 2019 767 · 2020 824 · 2021 819 · 2022 915 · 2023 936 · 2024 891 · 2025 563 | 6,384 (2018-2025) | shareholder's equity $7,100M (2019) → $10,933M (2025); about 11.1%, 10.3% and 10.6% on average equity in 2020 to 2022, 5.2% in 2025 after $651M of regulatory disallowances | Sempra/SDG&E combined 10-Ks: FY2025 `0001032208-26-000010`, FY2022 `0001032208-23-000008`, FY2020 `0001032208-21-000007` |

**The field's returns over the full span, judged in words.** Over 2016 to 2025 EIX earned about 8.8% a year on its average common
equity (11,785 against an average of about $13.4B of year-end common equity), counting the 2025 recoveries; its owners saw no growth in
book a share for eight years and put up $3.3B of new common through the 2017/2018 claims. PG&E's owners lost more than half of book a
share and were diluted more than four times over. SDG&E, with no catastrophe of its own in the span, earned an ordinary regulated return
and took a $651M disallowance in 2025. The return is set by a regulator, which the framework carries to Q3 as a second best rather than
closing OUT **[M2009-104]**; but the field's record shows that the set return is not what California owners have received, and that the
difference is decided by events no filing forecasts.

**The speakers on this field.** "the regulatory climate in a few states has raised the specter of zero profitability or even
bankruptcy (an actual outcome at California's largest utility and a current threat in Hawaii). In such jurisdictions, it is difficult
to project both earnings and asset values in what was once regarded as among the most stable industries in America." **[L2023-011]**;
"whether you earn X or go broke is not an equation that works" **[M2024-011]**; "A catastrophic event can render a single utility
insolvent" **[L2005-019]**. Of their own utility the speakers say the risk has outrun the return, "nor can you earn a large enough
return to take on these risks" **[M2025-040]**, and "values change and they don’t always change upward" **[M2025-045]**; those two
rows are about one company and are weighed, never deciding alone (Q2, A row about one company). The bet a utility owner makes is the
speakers' own: "the bet we are making is that regulatory authorities will treat us fairly in the future" **[M2014-087]**.

**Why TOO HARD, and why NATURE.**
- The castle against attackers stands; nobody takes the franchise. What is in doubt is whether its owners keep the return, and that
  turns on a liability the filer itself cannot size. "If something’s important but unknowable, forget it." **[M2006-076]**. The
  speakers' rule for such a threat: "at least it’s impossible for us to figure — and then we just — we don’t even think about it
  then." **[M2000-014]**; and a moat that cannot be valued is left alone, "We don’t know how to valuate that, and therefore we leave it
  alone." **[M2000-019]**.
- **Not OUT.** The castle is not shown open on the evidence: the regime did return part of the 2017/2018 losses to customers, the
  common equity survived without bankruptcy, two of three agencies affirmed the rating after SB 254, and the statute bounds the Eaton
  reimbursement at about $4.3B unless willful disregard is found. A castle shown open would need the evidence to run one way; it runs
  both ways.
- **Not WORK.** No unread filing answers it. The Eaton liability will be known only after the litigation (bellwether January 2027), the
  fund's reimbursements and a CPUC prudency proceeding that SCE will file "after it has resolved all or, if authorized by the CPUC,
  substantially all third-party damage claims" (10-Q); the next fire is weather. The insiders decline to write the number down, which is
  the test of the closed box: "They would say, “That’s too hard.”" **[M2000-105]**; "We couldn't solve this problem, moreover, even if we
  were to spend years intensely studying those industries." **[L1993-023]**.
- **The change for the better is not yet credited.** AB 1054's prudency standard has never been applied in a final CPUC decision; the
  framework credits a change for the better only on the evidence of a full cycle **[M2005-020]**, **[L1995-022]**, and until then the
  question is TOO HARD (NATURE). **CONVENTION of this run, the re-look condition:** the framework's stated condition is the first fiscal
  year in which the business's or its field's volume falls, written for a business whose test is a downturn in volume; for a regulated
  utility whose earnings are decoupled from volume and whose test is the regulator's first ruling under the new law, the condition used
  here is **the first final CPUC decision applying the AB 1054 prudency standard to a wildfire cost-recovery application by any of the
  three utilities (for SCE, the Eaton Fire application), read from the filings, together with an Eaton loss estimate the filer states as
  reasonably estimable**. Rationale: that ruling is the event that shows whether the change held, as the downturn is for a cyclical
  business; the convention's own wording does not fit a business whose volume does not reach its earnings.

**VERDICT: TOO HARD (NATURE)** **[M2006-013]**: the castle's future cannot be judged, because the deciding variable, the wildfire
liability under strict liability and an untested statute, is a forecast the insiders will not write down **[M2000-105]**, **[M2000-014]**,
**[M2006-076]**. The file closes here. Q3 to Q12 are NOT REACHED; what was already found is written under AFTER THE STOP, and the value
figures the owner asked for are under Q7 as COMPUTATION, NOT A CLEARANCE.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED (closed at Q2). Facts found are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0; facts found are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. Integrity facts found are under AFTER THE STOP and flagged in the box line.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP. (The buyback line Q6 needs from Q7 is not written back: the question was not
reached. For the record, the central COMPUTATION below puts the range at $34.08 a share, and the common repurchases found were $200M in
2024, $32M in 2025 and $30M in the first half of 2026, at prices not read.)

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED. COMPUTATION, NOT A CLEARANCE** (operator rule 3), made because the owner asks for the two reporting figures; it carries
no entry language and changes no box. Script: `Test Runs/_research 2026-10-22 EIX/calc.py`. USD millions unless a share figure.

**The basis.** SCE earns a return a regulator allows on its invested capital, and it is the whole business, so Q7's central figure is
the **equity-only** basis, owner cash after interest and after the company's tax against the market value of the shares, "leaving
aside certain exceptions, such as debt dedicated to Clayton's lending portfolio or to the fixed-asset commitments at our regulated utilities" **[L2017-012]** (Q7, The regulated utility).
The all-equity figure is shown beside it and never decides.

**The cash, after every real cost.** Owner cash (equity-only) = operating cash flow (already after interest paid, cash taxes, wildfire
claims paid net of insurance, and the Wildfire Fund contributions) less stock pay less dividends on the preferred and preference stock
(SCE's and EIX's, senior to the common) less maintenance capital spending. Wildfire losses stay in, because such losses "will
forever be paid with shareholders' money" **[L2002-002]**. **Maintenance** is taken as depreciation, a stated guess **[M2000-144]**, by
the rows' proxy **[M1998-127]**, with the rows' own warning that in "the utility business or the railroad business, it just keeps eating up more and more money, and your depreciation charges are inadequate"
**[M2015-049]**: the guess flatters, if anything.

| year | OCF | stock pay | preferred dividends | capex | D&A | M: maintenance-only | net long-term debt raised | A: all spending, debt credited to 43% of capex |
|---|---|---|---|---|---|---|---|---|
| 2017 | 3,597 | 23 | 125 | 3,844 | 2,115 | 1,334 | 948 | 553 |
| 2018 | 3,177 | 21 | 121 | 4,509 | 1,940 | 1,095 | 2,583 | 465 |
| 2019 | −307 | 29 | 121 | 4,877 | 1,803 | −2,260 | 3,614 | −3,237 |
| 2020 | 1,263 | 29 | 118 | 5,484 | 2,029 | −913 | 1,974 | −2,394 |
| 2021 | 11 | 39 | 166 | 5,505 | 2,288 | −2,482 | 4,375 | −3,332 |
| 2022 | 3,216 | 42 | 184 | 5,778 | 2,633 | 357 | 4,886 | −303 |
| 2023 | 3,401 | 46 | 225 | 5,448 | 2,635 | 495 | 2,623 | 25 |
| 2024 | 5,014 | 57 | 256 | 5,707 | 2,866 | 1,835 | 2,555 | 1,448 |
| 2025 | 5,800 | 57 | 240 | 6,515 | 3,237 | 2,266 | 3,081 | 1,789 |

Sources: each year's 10-K cash-flow statement as tagged (OCF, `PaymentsToAcquirePropertyPlantAndEquipment`,
`DepreciationDepletionAndAmortization`, `AllocatedShareBasedCompensationExpense`, `PaymentsOfDividendsMinorityInterest` for SCE's
preference dividends, `DividendsPreferredStock` for EIX's, long-term debt issued less repaid), 2023 to 2025 read on the FY2025 10-K
statement. The debt credit is the regulated-utility rule's: the long-term debt raised to fund the fixed assets, credited against the
capital spending up to the debt share the regulator allows, 43% ("52% common equity, 43% long-term debt, and 5% preferred equity",
10-K, Cost of Capital Application); the cap binds in every year but 2017 and 2020. Net long-term debt raised (issued less repaid) is used, not
gross issuance, because gross issuance includes refinancing that funds no new asset (a choice of this run, stated; the framework's
sentence does not say).

**The base: specific (a).** The first year of the literal window, 2021, is aberrational on the filer's own description: its $11M of
operating cash "include $3.9 billion settlements on 2017/2018 Wildfire/Mudslide Events claims" (10-K for 2021, accession
`0000827052-22-000006`, operating cash table, note 3). By (a) the base is the average over the last full cycle **[L2005-003]**.
**CONVENTION of this run:** the cycle is the 2017/2018 wildfire episode, from the last year before the events (2017) through the year
the CPUC decided their recovery (2025), nine years, with the two securitized recoveries of those same losses credited as owner cash
($1.6B TKM bonds, December 2025; $2.0B Woolsey bonds, July 2026, both 10-Q). Rationale: the claims were paid out of operating cash and
the regulator's partial recovery came back through a financing vehicle; a base that counts the payments and not the recoveries charges
the owners for costs the customers bore, and a base that drops 2021 drops the costliest year of a cost that recurs. The literal window
is shown beside.

**Whose tax.** Cash taxes were near nil across the span (wildfire deductions). By Q7's convention, owner cash is put at the statutory
rate (the book tax expense in place of the cash tax: −37 a year on the episode, −224 a year on the literal window) and the shelter's
present value is added at the long rate: about $3.1B of tax-effected losses and credits (10-K, MD&A, Income Taxes), used at the $554M a
year of income taxes the 2025 GRC authorizes (5.6 years, a schedule of this run's; the 10-K states none), worth **$2,624M, $6.82 a
share**. CAMT applies from 2026 (10-K); its effect on the schedule is not computed.

**Growth: specific (b).** The maintenance-only series changes sign (−2,482 in 2021, 2,266 in 2025); measured between halves it still
changes sign (episode −186 for 2017-2020 against 2,138 for 2022-2025 with the recoveries; window −1,062 against 2,850). The compound
rate is meaningless, so **the range is the no-growth case alone, said so**. Rate-base growth (6% to 7% a year in management's forecast)
is a forecast and is not credited.

**The figures (equity-only; no-growth case at 5.29%, plus the shelter):**

| case | base a year | value a share | fair price a share (at 10%) | expected return at $57.90, no growth |
|---|---|---|---|---|
| **CENTRAL: episode 2017-2025, maintenance-only, recoveries credited** | **555** | **$34.08** | **$21.24** | 2.8% |
| literal window 2021-2025, maintenance-only, the TKM recovery received in the window | 590 | $35.80 | $22.15 | 3.0% |
| literal window, both recoveries (Woolsey received after the window) | 990 | $55.45 | $32.55 | 5.0% |
| literal window, no recoveries | 270 | $20.08 | $13.84 | 1.4% |
| episode, all spending with the debt credit | −191 | not positive before the shelter (−$2.56) | not positive before the shelter | negative |
| literal window, all spending with the debt credit | 21 | $7.86 | $7.37 | 0.1% |
| **all-equity basis, beside** (maintenance-only owner cash before interest, after tax at 28% on interest: episode 1,507; window 1,978), less net debt $42,161M at 2026-06-30, the $2,000M July 2026 bonds and $1,647M of preferred and preference stock | | **not positive**: −$45.01 (episode), −$21.88 (window) | **not positive**: −$79.88, −$67.64 | |

**How Q7 would close, had it been reached.** No case earns the floor of about ten percent at the price **[M2003-149]**: the highest, the
literal window with a recovery received after it, returns about 5.0% with no growth, below the 5.29% bond. By the floor-first rule the
close would be OUT whatever the width. Every all-equity figure is not positive, as the regulated-utility paragraph foresees for a utility
at a full price **[M2009-104]**.

- **Value range (COMPUTATION):** **$34.08 a share** (the no-growth case alone; the literal-window cases beside run $20.08 to $55.45)
  against **$57.90**.
- **Fair price (COMPUTATION, a reporting figure, never a verdict):** **$21.24 a share, equity-only, central** (the regulated-utility
  basis), after the company's own tax at the statutory rate with the carryforward shelter's present value added; the debt credit enters
  only the all-spending case, which is not positive on the episode ($7.37 on the literal window); **all-equity, beside: not positive.**
  No cheap price is reported.
- **VERDICT:** NOT REACHED (the file closed at Q2).

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. (An electric utility is not among the businesses the framework names.)

---
## THE BOX
**TOO HARD (NATURE) at Q2** — the castle's future cannot be judged: the Eaton Fire liability, which the filer states it cannot estimate,
under strict liability and an AB 1054 prudency standard the CPUC has never applied in a final decision. Re-look condition (a CONVENTION of
this run, Q2): the first final CPUC decision applying the AB 1054 prudency standard to a wildfire cost-recovery application, with an
Eaton loss estimate the filer states as reasonably estimable. COMPUTATION, NOT A CLEARANCE: value $34.08 a share (no-growth case alone)
and fair price $21.24 (equity-only, central; all-equity not positive) against $57.90. **Integrity facts recorded, not judged.**

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Q3 (capital).** Rate base $48.2B at 2025-12-31; 2025 GRC authorized revenue $9,660M, of which authorized return $2,970M and
depreciation $2,729M (10-K, Impact of 2025 GRC). Capital spending $6.5B in 2025 against depreciation of $3.2B, and $37.5B to $40.6B planned
for 2026 to 2030, of which $0.8B to $1.1B a year is wildfire mitigation (10-K, Capital Program). Owner cash after all capital spending,
before any debt credit, was negative in every year 2017 to 2025 (Q7 table: OCF less stock pay, preferred dividends and capex). SB 254
requires about $2.9B of wildfire-mitigation capital approved from 2026 to be kept out of the equity portion of rate base (securitized
instead), and "Approximately $1.6 billion" of AB 1054 mitigation capital earns no equity return (10-K, Item 1). The capital-heavy business
with a regulated return is what the framework weighs as a second best at Q3.

**Q4 (the accounts).** The MD&A leads with "core earnings", a non-GAAP figure, and from July 2023 treats wildfire claims as non-core
("Edison International and SCE no longer consider wildfire-related claim losses to be representative of ongoing earnings"); non-core items
appear in every period read (2023 to Q2 2026). 2025 GAAP earnings of $4,459M include $1,978M of non-core recoveries (10-K). The Wildfire
Fund asset is amortized over a management-estimated 20-year coverage period (15 years until 2024). Regulatory assets $13.0B at 2025.
Retained earnings fell 2016 to 2022 while dividends were paid (Step 0).

**Q5 (integrity facts, recorded, not judged).** (1) The Los Angeles District Attorney's Office is investigating the Eaton Fire "for the
purpose of determining whether any criminal violations have occurred"; the CPUC's Safety and Enforcement Division is also investigating;
SCE "is not aware of any basis for felony liability" (10-K and 10-Q). (2) SCE "believes that it is likely that its equipment was
associated with the ignition of the Eaton Fire" (10-Q). (3) An agreement of October 21, 2021 between SCE and the SED "regarding the
2017/2018 Wildfire/Mudslide Events and three other 2017 wildfires", under which SCE waived recovery of $125M (TKM) and $250M (Woolsey) of
uninsured claims and owed $42M still unpaid at 2025-12-31 (10-K). (4) The board cut the 2025 annual incentive of three named executives by
about 40% "In light of the impact of wildfires on communities within SCE’s service territory" (proxy). A later run that reaches Q5 must
answer (1) to (3).

**Q6 (money and owners).** Dividend policy is a payout ratio, "target payout ratio of 45% – 55% of SCE's core earnings" (10-K); common
dividends $1,274M in 2025, paid in a year when owner cash after all capital spending was negative, so funded in effect by borrowing. Common
issued $2,391M (2019) and $912M (2020); preferred issued $1,977M (2021) and $542M (2023), and $1.66B of preferred and preference stock
repurchased or redeemed in 2025 plus $538M in the first half of 2026. Long-term incentive: 50% performance shares on relative TSR and on
core EPS, plus options and restricted stock units; peer benchmarking by a compensation consultant (proxy).

**Q8 (alternatives).** The long Treasury yields 5.29%; every equity-only case above returns less than that with no growth.

**Q9 (debt and exposures).** Total debt $42.4B at 2026-06-30 (short-term $1,521M, current long-term $3,797M, long-term $37,085M, of which
$2,979M securitization bonds of a consolidated VIE) plus $2.0B of recovery bonds issued in July 2026, against $17.4B of common equity.
Covenants: SCE debt to capitalization 0.57 against a 0.65 limit, EIX 0.64 against 0.70 (2025-12-31). Ratings, SCE Baa1/BBB/BBB- and the
parent Baa2/BBB/BBB-, S&P negative. Collateral on a fall below investment grade: $10M on power contracts, up to $115M for workers'
compensation, up to $50M for environmental obligations (10-K). Coverage, (pre-tax income + interest expense) / interest expense: 1.94
(2023), 1.84 (2024), 4.89 (2025, with the recoveries); the rows' definition is "pre-tax earnings/interest, not EBITDA/interest"
**[L2012-002]**. The parent has no operations and depends on SCE dividends and on California's dividend law (10-K, Item 1A). The little-or-no
debt criterion is stated for a whole business bought **[R1997-001]**. The Eaton tail (Q2) is the exposure that could take the common to
zero; the Continuation Account contributions ($2.4B plus $1.9B contingent) are not recoverable.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit f851472b); written question by question; committed after Q1 (089a6348) and Q2
      (60476902) and at the close (write-early).
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock in `Screens/_daily/` was present (the dispatcher's); the run
      is folded by the dispatching session (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident (the DUK commit subjects,
      two research-folder names, the memory index) is declared under Contamination and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      `Test Runs/_research 2026-10-22 EIX/check_ids.py`); every filing fact has its document and accession; no number without a filing or
      a stated convention.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance, and the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (wildfire claims, Wildfire Fund contributions, stock pay, preferred dividends, capital spending),
      never a net-income proxy (operator rule 5); the sovereign from the Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (Foundations); the facts for later questions are under AFTER THE STOP, with the integrity flag
      in the box line.
- [x] No row dated after the anchor: not a point-in-time run (the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before the closing commit.
- Honest gaps: the Eaton liability itself (no filing estimates it); the prices paid for the small buybacks; SDG&E's 2023 equity (so its 2023
  and 2024 returns are not computed); the 2025 cash tax (taken as expense less deferred, no tag); the CAMT's effect on the shelter schedule;
  the proxy was searched, not read in full (Q5 and Q6 not reached).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Where a utility's wildfire liability is judged.** Q1's test 4 ("important but unknowable" **[M2006-076]**) and the doubt row **[M2002-092]** would
close the file at Q1; the regulated-utility paragraph places "the regulatory climate at Q2 and Q9". I followed the paragraph and closed at
Q2; the box is the same either way, but two analysts could split on the question number. A sentence in Q1's routing would settle it.
(2) **The re-look condition for a change for the better** (Q2, section C) is written as a fall in volume; for a decoupled utility the test
is the regulator's first ruling under the new law, and I had to confess my own condition. (3) **The regulated-utility debt credit** does
not say gross or net issuance, nor whether it reaches the maintenance-only case that (e) makes central; I used net issuance and applied the
credit only in the all-spending case, where growth spending is charged, and said so. (4) **Specific (a) and catastrophe losses.** (a) is
written for business cycles; a catastrophe episode whose losses are paid in operating cash and recovered years later through a securitization
in financing cash is not addressed, and the choice of base moves the value from $20 to $55 a share. I took the episode as the cycle and
credited the recoveries, as a CONVENTION. (5) **Whose tax at a utility.** The shelter convention adds the carryforwards' present value
($6.82 a share here), but a utility's income taxes are set in its rates and the rows say of tax that "in the utility business, it actually does" **[M2021-035]**; whether the shelter accrues to the owner or the customer is not decided by the text. I applied the convention as written.
(6) **The competitor rule meets a monopoly.** The 10-K names classes of competitor (CCAs, Electric Service Providers, transmission developers)
and no company; the brief's rule then calls for a confessed choice, and the natural field (the other two utilities under the same regulator
and statute) is not a set of rivals at all.
