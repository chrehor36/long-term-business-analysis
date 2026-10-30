# Company Run — Brookfield Corporation (NYSE/TSX: BN) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked. This run was dispatched under a blind rule: `PORTFOLIO.md`,
the holding reviews, the session-state file and the queue register were not opened, and no attempt was made to learn
whether the operator holds BN. The template's instruction to check `PORTFOLIO.md` was set aside for that reason (see the
last section).

**CONTAMINATION, declared.** To obey the blind rule I listed the file names in `Test Runs/` that mention Brookfield, and so
saw that two earlier runs exist, named "2026-09-13 Run - BN Brookfield Corporation.md" and "2026-09-13 Run - BAM Brookfield
Asset Management.md", with their research folders. I did not open either, and I know nothing of their verdicts. All I
learned is that BN and BAM were run on 2026-09-13 under v4.1. The session's own context carried a general memory index of
the project. It names no Brookfield entity and no holding.

**Working folder:** `Test Runs/_research 2026-10-05 BN/` (the filings as fetched, and their text conversions).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $36.68 (BN, NYSE, 2026-10-05, Yahoo Finance chart endpoint via `tools/sources.py`; **AGGREGATOR, FLAGGED**,
  live quote only, operator rule 5). For reference, from the same aggregator on the same day: BAM $44.355; BNT (the BWS
  exchangeable share) $36.92.
- **Shares by class:** 2,232,266,331 Class A Limited Voting Shares and 85,120 Class B Limited Voting Shares at
  2026-08-13 (Q2 2026 interim report, MD&A "Issued and Outstanding Shares", furnished on 6-K 2026-08-17, accession
  `0001001085-26-000021`). `python Screens/cover_shares.py BN` returned "NO COVER SHARE COUNT PARSED" (a 40-F filer
  has no 10-K cover), so the count was read by hand. **The charter note:** Class A and Class B rank equally for
  dividends and capital, but **the 85,120 Class B shares elect half the board** (Q2 2026 report, Note 12; FY2025 40-F).
  Also outstanding: 59,970,825 BWS Class A exchangeable shares (BWS 20-F FY2025, accession `0001837429-26-000008`),
  each exchangeable one-for-one into a BN Class A share and paid the same dividend, so economically a BN share. Diluted
  shares at 2025-12-31: 2,383.2 million (FY2025 annual report, MD&A Part 4, which counts options, share plans and "exchangeable
  shares of affiliate").
- **Market cap:** BN classes alone, 2,232.35M x $36.68 = **$81.9B**. With the BWS exchangeables, 2,292.3M x $36.68 =
  **$84.1B**. On the diluted count of 2025-12-31, $87.4B. (Arithmetic; price aggregator-flagged.)
- **Sovereign for the earnings currency:** the earnings currency is mainly USD (58% of common equity in USD at
  2025-12-31; the rest in GBP 13%, CAD 7%, EUR 5%, BRL 4%, AUD 4%, other 9%: FY2025 MD&A, Foreign Currency Translation).
  **US Treasury 30-year par yield 5.63%, 2026-10-02**, US Treasury daily par yield curve, issuing authority, via
  `python tools/sources.py`. (Several currencies: the sector method's CONVENTION C11, run at the reporting currency's
  sovereign with the exposure stated; it is unresolved.)
- **Filings read** (operator rule 4):
  - Form 40-F for FY2025, filed 2026-03-18, accession `0001001085-26-000006`: the annual report with MD&A and audited
    statements (`bn-20251231_d2.htm`), the 40-F body, the Annual Information Form (exhibit 99.1, fetched).
  - The FY2025 annual report as furnished on 6-K 2026-03-18, accession `0001001085-26-000008` (the same MD&A. The
    shareholder letter pages are images and were not read).
  - Q2 2026 interim report, 6-K 2026-08-17, accession `0001001085-26-000021`, including the letter of 2026-08-13.
  - The simplification transaction: release of 2026-05-26 (6-K accession `0001104659-26-066346`), the management
    information circular (6-K accession `0001104659-26-071025`, exhibit 99.3, searched, not read in full), the vote of
    2026-07-16 (6-K accession `0001104659-26-084374`). 6-Ks of 2026-09-04 (preferred redemption), 2026-09-21 (the
    $600M 5.650% notes due 2031) and 2026-09-23 (the fourteenth supplemental indenture).
  - **Brookfield Wealth Solutions Ltd. 20-F for FY2025**, filed 2026-03-26, accession `0001837429-26-000008` (balance
    sheet, fair-value hierarchy, Notes 6, 8 and 26, Item 10 on the class C shares).
  - For the ten-year balance sheets: 40-F FY2022 (accession `0001001085-23-000007`, annual report `bam-20221231_d2.htm`),
    40-F FY2020 (accession `0001001085-21-000010`, `bam-20201231.htm`), 40-F FY2018 (accession `0001001085-19-000012`,
    exhibit 99.2 annual report), and the IFRS company facts from SEC XBRL (transcription, cross-checked below).
- **One figure cross-checked against the filed statement:** corporate borrowings **$14,301M** and common equity
  **$43,796M** at 2025-12-31 on the audited Consolidated Balance Sheet (FY2025 annual report, statement lines citing
  Notes 16 and 21; auditor Deloitte LLP, unqualified opinion). These agree with the MD&A capitalization table and with the XBRL
  facts `ifrs-full:Borrowings` = 14,301,000,000 and `Equity` = 166,194,000,000 (= 4,090 + 118,308 + 43,796). Match.
- `python tools/run.py BN`: returned "BN: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The tool reads
  us-gaap tags and BN files IFRS. No arithmetic line was available from it. Nothing it printed was used.

## THE FOUNDATIONS (not a gate)
A share is a business **[M1997-109]**. Here the business is a holding company whose earnings are fees, insurance spreads and
distributions from listed and private affiliates, so the foundation that bears hardest is **who is paid to tell you**.
Brookfield earns fees on the capital it gathers, and its letters are written by the gatherer. "you do not get impartial
advice from Wall Street [...] when there’s (an) enormous amount of fees possible from one action, and no fees applicable
from another action" **[M2020-037]**. "asset gathering can become a way more important part of your income than asset
managing" **[M2010-054]**. The Q2 2026 letter's section "Private Assets are the Answer for Retirement Accounts" (6-K
`0001001085-26-000021`) is written by a firm that is paid when the answer is accepted: the people who sell a service "are
going to have to convince them that they have a problem" **[M2004-046]**. The market serves and does not instruct
**[M2006-077]**: the run reads the filings, not the quotation. The analyst's habits apply: look for "what’s wrong in
things" **[M2025-013]**, ask "What do I not know that I need to know?" **[M1999-129]**, and destroy the previous conclusion
**[M2016-054]** (the prior BN run, unopened, is not an anchor here).

**Contrary evidence, written down as found** **[M1997-127]**:
1. BWS has paid BN **nothing** on BN's class C shares: "For the years ended December 31, 2025, 2024 and 2023, our company
   has not paid any distributions to the holder of class C shares" (BWS 20-F FY2025, Item 10). Yet BN's distributable
   earnings for 2025 count **$1,671M** of "Wealth Solutions distributable earnings" (FY2025 MD&A, DE table), which is
   27.8% of the $6,008M total.
2. The insurer owns its parent and its sister. BWS holds **$2.1B of BN shares**, **$3.4B of BAM shares** contributed by BN
   in June 2025, and **about $4.3B of private loans to Brookfield subsidiaries**, in all **$13.4B of related-party
   investments** (2024: $8.6B), equity-method investments not included (BWS 20-F, Note 26). BWS's total equity is
   $17.9B.
3. BWS's private loans grew from $5,204M to $8,415M in 2025. Those rated BB and below rose from $875M to **$2,918M**,
   and $2,007M carry only the company's internal rating ("Unrated", BWS 20-F, Note 6).
4. BN's distributable earnings add back equity-based compensation ($110M in 2025, $109M in 2024: FY2025 MD&A).
5. Real-estate property-specific borrowings of **$63.8B** carry an average term of **2 years**. The consolidated
   property-specific maturities due within one year are **$46.6B** ("expected to be primarily addressed through
   refinancings, repayments, and extensions": FY2025 MD&A, Contractual Obligations). Value-add and opportunistic
   real estate were written down $477M and $456M in 2025.
6. Net income attributable to common shareholders was $1,140M in 2025 on $43.8B of common equity (2.6%). Common
   equity then **fell $1.3B** in the first half of 2026, to $42,483M (Q2 2026 report).
7. The indemnifications are open-ended: "The nature of substantially all of the indemnification undertakings prevents
   the company from making a reasonable estimate of the maximum potential amount" (FY2025 MD&A, Contractual
   Obligations).
8. The letter of 2026-08-13 calls a subsidiary's moat "unassailable" (Westinghouse) and describes "one of the most
   advanced ai factories" at "$100 billion". This is the seller's language.
9. A structural change is under way. BN and BWS are to be combined under a new Bermuda parent, Brookfield Corporation
   Ltd. Shareholders approved it on 2026-07-16 and closing is expected by year-end (6-Ks `0001104659-26-066346`,
   `0001104659-26-084374`). After closing, the annuity writer sits inside the parent outright.

## THE STANDING RULE
Owning this share outright, unlevered and sized within the buyer's means, puts no demand for cash on the buyer. The rule is
about the buyer's conduct: "We are never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**, and "Never risk permanent loss of capital" **[L2023-005]**. Nothing here licenses borrowing to buy it
**[M2004-065]**. The rule's row on cash-out life contracts **[L2014-024]** bears on the target, not the buyer, and is
noted at Q9 (not reached).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** "can I understand it?" **[M1995-051]**, where understanding is "a reasonable probability of being able to
asses where the business will be in 10 years" **[M2000-037]**, and "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years" **[M2012-065]**. **A holding company is understood by its parts**
(CONVENTION, Q1 of the framework, "A holding company"): a part that cannot be understood, and that matters, keeps the
whole outside the circle. The row behind it: "if you have doubts about something being into your circle of competence,
it isn’t" **[M2002-092]**. **[M2023-031]**, the trading houses understood "as a group", stays OPEN against it.

**Stage zero of the sector method: split first** **[L2008-005]**, **[L1998-002]**. The parts, by the filer's segment
common equity at 2025-12-31 (FY2025 MD&A, Summary of Results by Operating Segment; total common equity $43,796M after
Corporate Activities of -$18,659M; percentages of the $62,455M sum of the positive segments, my arithmetic):

| Part | What it is | Common equity | Share | 2025 DE / FFO / NOI (filer's measure) | Cash it sent the Corporation |
|---|---|---|---|---|---|
| Asset Management | 73% of BAM (fees on $603B fee-bearing capital), plus $10.9B of direct LP stakes, mostly BAM real-estate funds | $15,511M | 24.8% | DE $3,327M | BAM and direct-investment distributions in DE $2,767M; realized carry $560M |
| Wealth Solutions | equity-accounted BWS: annuities, life, P&C; insurance assets $143B | $12,742M | 20.4% | DE $1,671M | **$0** (class C, 2023 to 2025) |
| Renewable Power and Transition | 45% of BEP | $4,860M | 7.8% | FFO $584M | distributions $454M |
| Infrastructure | 26% of BIP | $2,311M | 3.7% | FFO $757M | distributions $356M |
| Private Equity | 43% of BBU direct (68% with BWS) | $1,890M | 3.0% | FFO $455M | distributions $24M |
| Real Estate | 100% of Brookfield Property Group: super core, core plus, value add, opportunistic, NA residential | $25,141M | 40.3% | NOI $3,144M | in "Distributions from Operating Businesses" (BPG's distributions not separately reconciled) |

The sector method's own scope test (stage zero, step 4; CONVENTION C10) puts **both of the two financial parts outside
the method**. BAM is "an asset manager whose earnings are fees". BWS is overwhelmingly a life and annuity book:
policyholders' account balances of $92,992M and future policy benefits of $16,249M, against P&C policy and contract claims
of $7,277M (BWS 20-F, balance sheet). The life and annuity book has surrender features: the 20-F's revenue note counts
"surrender charges" as annuity revenue, and its lapse assumptions are "the expected rate of full surrenders". The rows set
that book apart: "property-casualty insurance differs in an important way from certain forms of life insurance"
**[L2013-003]**. "Many life insurance products contain redemption features that make them susceptible to a "run" in
times of extreme panic" **[L2014-024]**. **What I did where the method does not reach:** I applied the framework's own
Q1 rules for a financial institution, the exclusion and the door left open for a bank, by their form. Can both sides of
the balance sheet be read from the filings **[M2002-022]**, **[M2011-022]**? I then applied the holding-company convention
to the result. I did not stretch the float method over an annuity book (C10). Stage zero's two ratios, stated for the
record and not as a test (C2): investments to equity at BWS are $110,044M / $17,917M = **6.1x**. Liabilities to equity are
$139,264M / $17,917M = 7.8x.

**The decisive part: Wealth Solutions. Can its asset side be read from outside?** The BWS 20-F FY2025 (accession
`0001837429-26-000008`) shows:
- Total investments **$110,044M**. Of these, five lines are carried at amortized cost, cost or equity method: mortgage
  loans $11,231M, investment funds $8,962M, private loans $8,415M, real estate partnerships $4,241M, investment real
  estate $3,000M. Together $35,849M (my sum). Separately, $10,617M of fair-valued assets sit in **Level 3**, partly
  overlapping those lines. The filer defines Level 3 inputs as ones that "reflect the Company’s own assumptions"
  (F-41/F-42). Of the Level 3 total, $4,710M is fixed-maturity and equity securities not counted above.
- **Private loans:** $8,415M, of which BB and below $2,918M and "Unrated" $2,007M. The unrated loans carry "internal risk
  ratings, based on its investment selection and monitoring process" (Note 6).
- **Related parties:** $13.4B of investments in related parties, excluding equity-method investments. These include
  $2.1B of BN's own shares, $3.4B of BAM shares contributed by BN, and about $4.3B of private loans issued to subsidiaries
  of Brookfield (Note 26). The consolidated investment VIEs hold $23,575M of assets (Note 8).
- **Who chooses the assets:** "BAM has discretionary authority to manage the investment and reinvestment of the funds
  [...] including investments in Brookfield Accounts" (Item 7.B). BN's MD&A adds that BWS's investments "could be made in
  the open market or from the Corporation and its related party affiliate entities". In 2025 BWS deployed $13B "into
  Brookfield-managed strategies [...] at an average yield of 8.5%" (FY2025 MD&A, Wealth Solutions).
- **The liability side:** fixed index and fixed rate annuities with surrender charges, pension risk transfer, and
  **funding agreements, including a funding agreement-backed notes programme** (Item 4). That last is wholesale money,
  which "can run pretty fast" **[M2012-012]**. The reported gross spread is 2.25%: a net investment yield of 5.01% plus
  0.69% of realized and unrealized real-asset gains, against a 3.45% cost of funds (FY2025 MD&A). Nearly a third of the
  spread (0.69 of 2.25) is gains on real-asset strategies.

The rows decide this. "with financial institutions, it’s much tougher [...] no one probably knows [...] or even within
a reasonable range — the exact condition" **[M2005-068]**. "the only thing we understand is that we don't understand how
much risk the institution is running" **[L2002-018]**. "You spot troubles in financial institutions late. It’s just the
nature of the beast." **[M2001-066]**. The door is open only for a book whose asset side can be read, with "very little
risk on the asset side" **[M2002-022]**, and "It’s always on the asset side" **[M2011-022]**. Here the asset side holds
some $40.6B of loans, funds, partnerships and Level 3 securities ($35,849M plus $4,710M, my sum, about 37% of investments)
carried at amortized cost, at cost, under the equity method, or at the company's own assumptions. $13.4B of it is lent to or invested in the issuer's own group, chosen by a sister company paid fees on it
($243M of investment management fees to Brookfield in 2025, Note 26). Understanding each piece is not understanding the
whole: "even though I could understand every individual transaction they did, I don’t regard the whole enterprise, or the
operation of it, necessarily as being within my circle of competence" **[M2002-094]**. The same row asks "whether I can
continually fund it [...] independent from using Berkshire’s credit". That is exactly the question the BN and BWS circle
raises. BN contributed $3.5B of BAM shares to BWS in 2025 and $1.1B in 2024 (BWS 20-F, Note 26). BWS bought a $1B
economic interest in BBU from BN in Q4 2024 (FY2025 MD&A). BWS holds BN's shares and lends to BN's subsidiaries. The
framework's settled rule for a mixed institution (Q1, "The door against the exclusion, settled") applies by its form: the
readable half of a book does not make the unreadable half readable, which is the reading it draws from the row just
quoted. BWS's $59.7B of Level 2 corporate and
government bonds are readable. The privately valued, related-party half is not.

**Does the part matter?** Yes, on every measure the filings give. It is 29.1% of BN's common equity ($12,742M of $43,796M)
and 27.8% of BN's own headline DE. It holds 4% of BAM and 25% of BBU on the group's behalf. And on closing of the
simplification transaction it becomes part of the parent outright (6-K `0001104659-26-066346`: BN and BWS shares
"exchanged on a one-for-one basis for new shares of the Company"). It is also the part the filer names as growing: "As our
wealth solutions business continues to grow, it is becoming an increasingly important source of long-duration capital"
(letter of 2026-08-13).

**The other parts, briefly, for the record** (none is needed for the verdict):
- **BAM.** The most legible part: contractual base fees of $4,896M, a fee-related-earnings margin of 58%, and committed
  capital "typically committed for 10 years". Its ten-year key variable is whether clients keep committing capital to
  alternatives, which is a forecast of fund-raising, not of a moat **[M1998-044]**. Not decided here.
- **Real Estate (40% of the positive segment equity, more with the LP stakes held in Asset Management).** Values are
  internal (196 external appraisals of $49B of assets "within 3% of management’s valuations"). The debt is short-dated.
  US office and retail are the source of the 2024 and 2025 write-downs. "We view change as more of a threat into the
  investment process than an opportunity" **[M1999-063]**. This part adds doubt but does not decide the run.
- **BEP, BIP, BBU.** Separate listed issuers with their own filings. BBU is itself a private-equity conglomerate. Not
  read part by part here.

**Test 3, do the past statements tell me the future ones?** **[M2008-033]**. They do not, at the level of the whole.
Consolidated revenue fell from $95.9B (2023) to $75.1B (2025) because businesses were sold and deconsolidated, not because
the business shrank. Net income moves with fair-value changes. The filer's own measure (DE) counts insurance earnings that
were never paid to it. **Test 8, how far off could I be?** **[M2011-084]**: for the BWS asset book, I cannot bound it from
outside, which is the point of **[M2013-089]**: "we still wouldn’t have known what was going on [...] But nobody can."

**The cause of the box: NATURE.** The deciding question is the true condition, over a credit cycle, of a privately valued
asset book that the group itself originates, manages and marks, inside a 6x-levered annuity writer. More reading does not
answer it. Every further document returns the same marks, made on the company's "own assumptions". The rows say this
kind of condition is not known from outside however long one studies: "We couldn't solve this problem, moreover, even if
we were to spend years intensely studying those industries. [...] in other cases the nature of the industry would be the
roadblock" **[L1993-023]**. Also "nobody can" **[M2013-089]**, and "It’s just the nature of the beast" **[M2001-066]**.
It is "important but unknowable" **[M2006-076]**. A pass would end where the rows say it ends: "if we can’t make a decision
in five minutes, we can’t make it in five months" **[M2008-086]**. This is no judgment that anything is wrong: "It’s no
judgment that there’s anything bad" **[M2007-052]**, and "It doesn’t mean it isn’t a good buy [...] It just means that we
don’t know how to evaluate it" **[M2000-038]**. (A reader could argue WORK: BWS's US insurance subsidiaries file statutory
statements listing each holding, and I did not read them. I judge that they would list the same privately marked assets
without pricing them independently, so the work would not change the box. Recorded in the last section.)

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**. The decisive part is the annuity writer's asset side: $13.4B of
  related-party investments, $10.6B of Level 3 assets and $8.4B of private loans ($2.0B internally rated), in a book
  levered 6.1x, managed with discretion by an affiliate (BWS 20-F, accession `0001837429-26-000008`). It is 29% of BN's
  common equity and is being folded into the parent. Its condition cannot be read from the filings **[L2002-018]**,
  **[M2005-068]**, **[M2002-094]**, and doubt keeps the holding company outside **[M2002-092]**. The file closes here.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED as a verdict. The ten-year balance sheets were read anyway, because the dispatch asked for them and the reading
informed Q1. They are set out under COMPUTATION below, and they clear nothing.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range is written.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a verdict. The corporate and consolidated debt are read under COMPUTATION below.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing with this name **[M1995-018]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## COMPUTATION — NOT A CLEARANCE
*Everything below was computed after Q1 closed the file. It carries no entry language and clears nothing (operator rule 3).
It is recorded because the dispatch asked for the balance-sheet reading, the debt reading and the owner cash, and because
it is evidence for the next reader.*

### C1. Ten years of balance sheets, before the income account **[M2025-032]**
USD millions, at 31 December, as first reported in each annual report (2016 to 2018 from the FY2018 annual report, 2019 and
2020 from FY2020, 2021 and 2022 from FY2022, 2023 to 2025 from FY2025; 2022 is before the IFRS 17 restatement). The
equity-accounted line and goodwill are from the XBRL IFRS facts and agree with the reports where both were read.

| Year | Total assets | Common equity | Preferred | Non-controlling interests | Corporate (recourse) borrowings | Non-recourse borrowings | Goodwill + intangibles | Equity-accounted investments |
|---|---|---|---|---|---|---|---|---|
| 2016 | 159,826 | 22,499 | 3,954 | 43,235 | 4,500 | 60,391 | 9,856 | 24,977 |
| 2017 | 192,720 | 24,052 | 4,192 | 51,628 | 5,659 | 72,730 | 19,559 | 31,994 |
| 2018 | 256,281 | 25,647 | 4,168 | 67,335 | 6,409 | 111,809 | 27,577 | 33,647 |
| 2019 | 323,969 | 30,868 | 4,145 | 81,833 | 7,083 | 136,292 | 42,260 | 40,698 |
| 2020 | 343,696 | 31,693 | 4,145 | 86,804 | 9,077 | 139,324 | 39,372 | 41,327 |
| 2021 | 391,003 | 42,210 | 4,145 | 88,386 | 10,875 | 165,057 | 50,836 | 46,100 |
| 2022 | 441,284 | 39,608 | 4,145 | 98,138 | 11,390 | 202,684 | 67,073 | 47,094 |
| 2023 | 490,095 | 41,674 | 4,103 | 122,465 | 12,160 | 221,550 | 73,905 | 59,124 |
| 2024 | 490,424 | 41,874 | 4,103 | 119,406 | 14,232 | 220,560 | 71,802 | 68,310 |
| 2025 | 518,971 | 43,796 | 4,090 | 118,308 | 14,301 | 245,311 | 81,851 | 79,881 |
| Jun 2026 | 525,515 | 42,483 | 4,088 | 120,065 | 14,711 | 250,271 | 79,084 | 87,682 |

Common equity per share, on weighted-average shares adjusted for the 3-for-2 splits of 2020 and 2025 (XBRL
`WeightedAverageShares` times 2.25 for 2017 and 2018 and times 1.5 for 2019 to 2023; my arithmetic): 2017 $11.15; 2018
$11.90; 2019 $14.16; 2020 $13.98; 2021 $18.31; 2022 $16.85 (after the December 2022 distribution of 25% of the asset
manager to shareholders); 2023 $17.83; 2024 $18.47; 2025 $19.49 (year-end shares 2,244.7M: $19.51). That is 7.2% a year
compounded from 2017 to 2025, before dividends. Shares rose from about 2,157M to 2,247M over the same years despite
buybacks.

**What moved, and what the figures say and do not say** **[M2025-032]**:
- **Common equity roughly doubled ($22.5B to $43.8B). Non-recourse debt quadrupled ($60.4B to $245.3B). Goodwill and
  intangibles rose eightfold ($9.9B to $81.9B).** Most of the consolidated goodwill and debt sit in entities owned largely
  by others (non-controlling interests rose from $43.2B to $118.3B), so the consolidated sheet is a picture of what the
  group controls, not of what the shareholder owns. The filer says so itself: "we control entities in which we hold only a
  minority economic interest" (FY2025 MD&A).
- **Book growth leaned on revaluation, not earnings.** Net income attributable to common shareholders summed
  $14,002M over 2018 to 2025 (XBRL `ProfitLossAttributableToOrdinaryEquityHoldersOfParentEntity`), and common equity rose
  $19,744M over the same years. Dividends, the 2022 distribution of BAM shares and buybacks all went out of equity, so the
  balance came in through other comprehensive income, chiefly revaluation surplus on power and infrastructure property
  (2025: OCI to common shareholders $1,833M against net income of $1,307M; FY2025 MD&A, Common Equity). Those revaluations
  rest on the company's own discounted-cash-flow models (FY2025 MD&A, Part 5).
- **Corporate leverage rose faster than common equity.** Corporate borrowings went from 20% of common equity (2016) to 33%
  (2025). With the perpetual preferred, from 38% to 42%.
- **The equity-accounted line more than tripled ($25.0B to $79.9B, then $87.7B by June 2026).** It includes BWS. Under the
  framework's CONVENTION, equity-method income counts at Q3, Q4 and Q7 only as cash received **[L1994-024]**,
  **[L1996-038]**, **[M2018-045]**, and BWS sent none.
- **What the balance sheet cannot say:** the value of the private marks inside BWS and inside the real-estate book. Both
  are management's estimates, under audit, but not prices.

### C2. The corporate (recourse) debt read separately from the consolidated debt
- **Recourse to the Corporation** (FY2025 MD&A Part 4; Q2 2026 report): corporate borrowings **$14,301M** at 2025-12-31
  (**$14,711M** at 2026-06-30, plus **$600M of 5.650% notes due 2031** issued 2026-09-23 and guaranteed by BN). All
  fixed rate, average 4.8%, average term 15 years, maturities from 2026 to 2080. Due within one year $496M; in years 2-3
  $1,413M; in years 4-5 $1,736M; after 5 years $10,656M. No commercial paper outstanding at year-end. The revolver
  matures June 2030. **Perpetual preferred** $4,090M (5.0% average; rate-reset on the Canadian 5-year yield). The
  Series 51 and 52 are being redeemed on 2026-11-01. Recourse obligations due within a year: $3.8B (2024: $2.1B),
  including payables. **Core liquidity** $5.9B: $2.7B of cash and financial assets, of which $1.2B is the Corporation's
  share of BAM's cash, plus $3.2B of undrawn facilities. **Unfunded commitments** to flagship BAM funds: $10,796M
  committed, $6,846M funded, so $3,950M unfunded (my arithmetic).
- **Coverage, on the filer's own cash figures** (arithmetic, not a test): interest on corporate borrowings $742M (2025),
  against the cash the Corporation reported receiving from its parts and realized carry, $4,929M (C3 below). That is
  about 6.6 times, or about 5.4 times counting preferred dividends of $177M with the interest. "you can’t talk about debt levels without
  relating it to the ability to pay debt" **[M1995-104]**. Whether those receipts hold "under harsh economic
  conditions" **[L2003-016]** is the question Q1 could not answer for the insurer.
- **Non-recourse, consolidated:** subsidiary borrowings $16,897M (the listed affiliates' own recourse debt) and
  property-specific borrowings $228,414M. Of the latter, real estate $63,754M (2-year average term, 6.2%), of which
  $40.7B is in the real-estate LP investments of the Asset Management segment, and infrastructure $78,586M (7-year term).
  Consolidated debt to capitalization is 50% (2024: 47%). Consolidated interest expense was $17,100M, of which $16.4B is
  non-recourse. 2026 non-recourse maturities are about $48B. "Companies with large debts often assume that these
  obligations can be refinanced as they mature. That assumption is usually valid. Occasionally, though [...] maturities
  must actually be met by payment" **[L2010-020]**.
- **What can and cannot be seen.** The filings separate recourse from non-recourse cleanly, and the recourse debt is long,
  fixed and modest against the Corporation's receipts. What cannot be seen:
  1. Whether the Corporation would let a non-recourse entity fail. Its own words are that Corporate Activities provide
     "capital throughout the organization, when needed", and that "Certain guarantees are or may be provided on the
     financial obligations of perpetual affiliates and managed funds" (FY2025 MD&A). The indemnifications have no
     estimable maximum. The rows themselves pull both ways: "we’re going to pay everything we owe, no matter where it is"
     **[M2002-066]** against debt that "is not now, nor will it be, an obligation of Berkshire" **[L2003-016]**,
     **[R2009-001]**. The framework carries that pull OPEN (section VI, the standing rule and Q9).
  2. What the BWS liabilities become after the combination. BWS's $139.3B of liabilities include $93.0B of policyholder
     account balances with surrender features and a funding-agreement notes programme. These are the "sudden demands for
     large sums" and the cash-out rights of **[L2014-024]**, and a regulated insurer's obligations stand ahead of the new
     parent's equity. The circular was searched, not read in full, for the pro forma; I record that I did not reach it.
  3. The real estate refinancing at 2-year terms, which the filer expects to "address" but cannot promise.

### C3. Owner cash: the holding company read by its parts, equity-method income counted as cash received
The cash input is the cash the Corporation actually received, after its own costs, interest, preferred dividends and all
forms of compensation **[L2021-003]**, **[L2015-003]**, with equity-accounted BWS counted at the dividends it paid (the
CONVENTION at Q4, **[R1996-018]**). Every line is the filer's own DE line except where marked (FY2025 MD&A, DE table):

| USD millions | 2024 | 2025 |
|---|---|---|
| BAM and direct-investment distributions (DE from Asset Management) | 2,645 | 2,767 |
| Distributions from Operating Businesses | 1,626 | 1,602 |
| **Wealth Solutions: cash received on class C (BWS 20-F, Item 10)** | **0** | **0** |
| Realized carried interest, net (lumpy) | 403 | 560 |
| Leverage and corporate costs | (683) | (587) |
| Preferred share dividends | (176) | (177) |
| **Owner cash** | **3,815** | **4,165** |
| ...of which excluding realized carry | 3,412 | 3,605 |
| *Filer's DE, for comparison* | *6,274* | *6,008* |
| *Difference: BWS earnings never paid / SBC add-back / disposition gains* | *1,350 / 109 / 1,000* | *1,671 / 110 / 62* |

- Per diluted share (2,403.5M in 2024; 2,383.2M in 2025): **$1.59 (2024) and $1.75 (2025)**. Excluding realized
  carry, $1.42 and $1.51.
- Against the market value at $36.68 (aggregator), including the BWS exchangeables ($84.1B), 2025 owner cash is 4.95% of the
  price (4.29% without carry). The Treasury 30-year rate is 5.63%. Even if the $1,671M of BWS earnings had been paid, the
  figure would be 6.9%. **This is arithmetic only.** Q7 and Q8 were not reached, and no comparison here is a test.
- Only two years are shown. The framework's five-year average (CONVENTION, Q7) was not built because Q7 was not reached,
  and DE components for 2021 to 2023 were not read.
- The filer's DE is a number someone is paid to present **[M1994-079]**. It counts BWS earnings that never reached the
  Corporation and adds back stock compensation, which "is the most egregious example" of real costs owners are told to
  ignore **[L2015-003]**. A management "that regularly attempts to wave away very real costs by highlighting "adjusted
  per-share earnings" makes us nervous" **[L2016-006]**. This is recorded as a reading, not as a Q4 verdict (Q4 not
  reached), and it is one tell, not two.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**. Brookfield is a holding company understood by its parts. One part that matters
cannot be understood from outside: Brookfield Wealth Solutions, an annuity writer levered 6.1x (investments to equity)
whose asset side holds $13.4B of related-party investments (including $2.1B of BN's own shares and $3.4B of BAM's), $10.6B
of Level 3 assets and $8.4B of private loans ($2.0B internally rated), chosen by an affiliate paid to manage them. It is 29%
of BN's common equity, has paid BN nothing in three years while BN counts its earnings, and is being folded into the new
parent by year-end **[L2002-018]**, **[M2005-068]**, **[M2002-094]**, **[M2002-092]**. The cause is NATURE: the condition
of a privately marked, self-originated asset book is not knowable from the filings however long one studies
**[L1993-023]**, **[M2013-089]**. Q7 was not reached, so no range is set against the $36.68 price. A lower price does not
reopen the box **[M2000-038]**.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch.
- [ ] Written question by question and committed after each (write-early). **Not done:** the file was copied first, but
      the body was written in one pass after the reading, and no commit was made because the dispatch forbade commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, see below). Every filing fact has its
      accession. Numbers are the filer's or are marked as my arithmetic.
- [x] The order was kept: Q1 closed the run, and everything after it is NOT REACHED or under COMPUTATION — NOT A
      CLEARANCE, with no entry language.
- [x] Owner cash after every real cost (stock pay not added back, preferred deducted), never a net-income proxy (operator
      rule 5). The sovereign is from the issuing authority (US Treasury), dated. The aggregator quote is flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the nine items under the foundations).
- [x] No row dated after the anchor is cited: not a point-in-time run, so not applicable.
- [x] `tools/run.py` was run. It produced no arithmetic for an IFRS filer, and nothing it printed was used.
- [x] `python tools/check_framework.py` run after writing: PASS (2026-10-05). A separate script confirmed that all 55
      cited ids exist in `principle_ledger_v5.csv`, that no v4 (E-) id appears, and that every quoted fragment set
      beside an id is a verbatim substring of that row. No commit was made (dispatch instruction).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **WORK or NATURE for an opaque financial institution.** Section I defines NATURE by the insiders' unwillingness to
   write a forecast down **[M2000-105]**, a test made for technology. The financial-institution rows give a different
   reason, that the condition "nobody can" know from outside **[M2013-089]**, **[L2002-018]**. The framework does not say
   which test governs. Nor does it say whether the existence of further primary documents (here the statutory statements
   of BWS's US insurers, unread) makes the box WORK even when those documents would only repeat management's marks. I
   chose NATURE and said why. A second analyst could choose WORK on the same facts, and the framework would not tell us
   which of us is right.
2. **"A part that matters" has no measure.** The holding-company CONVENTION at Q1 does not say how large a part must be to
   keep the whole outside. I used share of common equity (29%), share of the filer's DE (28%), and the pending
   combination. A smaller opaque part (BBU at 3%) would have raised the same question with no rule to answer it.
3. **No Q1 door for an annuity writer.** The sector method's C8 door reads reserves, which fits a P&C book. An annuity
   writer's risk sits mainly on the asset side, and C10 puts it outside the method altogether. I applied the bank door by
   its form (are both sides readable?). The framework should say whether that is the intended route.
4. **A company in the middle of a reorganization.** BWS is equity-accounted today, so the equity-method CONVENTION counts
   its contribution at zero cash. After the approved combination closes it will be consolidated, and the same business
   would be counted differently. The framework gives no rule for a run made between approval and closing.
5. **The template's position note** tells the analyst to check `PORTFOLIO.md`, which a blind dispatch forbids. I left
   it unchecked and said so. The template could carry a blind-run variant.
6. **Related-party and circular holdings** (an insurer owning its parent's shares and lending to its sister companies)
   have no named test at Q1, Q4 or Q9. **[M2002-094]** carried the weight. A row on related-party dealing, if the ledger
   holds one, was not found by this run, which did not search for it.
