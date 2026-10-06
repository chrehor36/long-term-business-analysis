# Company Run — The Ensign Group, Inc. (NASDAQ: ENSG) — 2026-10-06 — T2 TEST RE-RUN
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. **This is a test
record under `Framework/v5/tests/T2 PROTOCOL - the four re-runs of 2026-10-06.md`: it binds nothing, enters no register and
changes no verdict of record.** The two texts of `Framework/v5/tests/RULES UNDER TEST 2026-10-06 - sections D and H.md` are
applied as if they stood in Q7, and every sentence where one bears says "rule under test, section D(x)" or "section H". Fill
top to bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template before any fetch (write-early).

**POSITION NOTE, declared before any verdict:** not checked. The T2 protocol's blind rule forbids opening `PORTFOLIO.md`; the
analyst does not know and did not try to learn whether the operator holds or wants this name.

**CONTAMINATION, declared:** the shell listing that created the working folder printed the file names of the other files in
`Framework/v5/tests/` (test run files named by ticker or case letter, and their working folders). None was opened, listed
further or searched; nothing of them is used. `tools/run.py` printed v4 material (a "yield" line, a "growth the price
assumes" line, "points over the sovereign") beside its arithmetic; only the arithmetic lines (price, share counts, filed
figures, the ten-year balance-sheet table) were read, per Part VII of the framework. No run file, holding review, resume
file, register, reading list or CASE or PREREGISTRATION file was opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $173.84 (close 2026-10-06; aggregator, Yahoo Finance chart endpoint, flagged per operator rule 5; `tools/run.py`
  showed a live aggregator quote of $173.59 the same day; a second aggregator, Stooq, refused the request).
- **Shares by class:** one class. 58,282,434 shares of common stock, par $0.001, from the cover of the 10-Q for the quarter
  ended 2026-06-30 (filed 2026-07-27, accession `0001125376-26-000034`; `python Screens/cover_shares.py ENSG`, cover date
  2026-07-23). Checked against the balance sheet: 62,102 thousand issued less 3,830 thousand in treasury = 58,272 thousand at
  2026-06-30 (same 10-Q). No 8-K or prospectus after the 10-Q changes the count (8-Ks of 2026-08-20 and 2026-08-25 read:
  a credit facility and bylaws). Charter: 150,000 thousand authorised, one class (10-K balance sheet).
- **Market cap:** $10,132M (58.282M x $173.84).
- **Sovereign for the earnings currency (USD):** 5.66%, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): the 10-K for FY2025 (filed 2026-02-04, accession `0001125376-26-000007`); the 10-Q
  for Q2 2026 (filed 2026-07-27, `0001125376-26-000034`); the proxy (DEF 14A filed 2026-04-02, `0001125376-26-000014`);
  the 8-Ks of 2026-02-04, 2026-04-30 and 2026-07-27 (earnings; `0001125376-26-000008`, `0001125376-26-000023`,
  `0001125376-26-000036`, with their press-release exhibits), 2026-05-18 (annual meeting votes, `0001125376-26-000026`),
  2026-06-10 and 2026-06-15 (buyback authorisations, `0001125376-26-000029`, `0001125376-26-000031`), 2026-08-20 (credit
  facility, `0001125376-26-000038`), 2026-08-25 (bylaws, `0001125376-26-000040`), 2025-06-20 and 2025-08-26 (the executive
  chairman's retirement and package, `0001125376-25-000115`, `0001125376-25-000158`), and 2013-04-22 and 2013-10-01 (the
  DOJ settlement and the corporate integrity agreement, `0001125376-13-000053`, `0001125376-13-000086`); the 10-Ks for
  FY2014 (`0001125376-15-000019`, the CareTrust spin), FY2019 (`0001125376-20-000018`, the Pennant spin), FY2021
  (`0001125376-22-000019`), FY2023 (`0001125376-24-000018`) and FY2024 (`0001125376-25-000021`) for the span. Competitors'
  own filings: NHC 10-Ks FY2016, FY2018, FY2021, FY2023, FY2025 (`0001047335-17-000042`, `0001437749-19-002958`,
  `0001437749-22-003787`, `0001437749-24-004619`, `0001437749-26-005910`); PACS 10-K FY2025 (`0002001184-26-000005`); BKD
  10-K FY2025 (`0001332349-26-000032`); CTRE 10-K FY2025 (`0001628280-26-007664`); SBRA 10-K FY2025
  (`0001492298-26-000008`); and the XBRL companyfacts of each. **One figure cross-checked against the filed statement:**
  net cash provided by operating activities FY2025, XBRL $564.3M, filed statement of cash flows $564,270 thousand (10-K
  `0001125376-26-000007`); and the tool's year-end equity 2,232 against the filed $2,231,725 thousand.
- `python tools/run.py ENSG` arithmetic lines only: price, share counts (dei cover 58.282M; balance-sheet 58.272M; issued
  62.102M), market cap 10.12B, sovereign 5.66%, and the ten-year balance-sheet table below. **Its owner-cash window stopped at
  FY2019** (capital spending and depreciation are not tagged under the elements it reads after 2019; it printed a warning to
  read the later filings), so the owner-cash table of this run is transcribed from the filed cash-flow statements
  (FY2025 10-K for 2023 to 2025; FY2023 10-K for 2021 and 2022; FY2021 10-K for 2019 and 2020, continuing operations) in
  `_work_T2_ENSG/q7_compute.py`. USD millions:

| year | operating cash | stock pay | property and equipment | cash paid for acquisitions | depreciation and amortization | owner cash, all spending incl. acquisitions | owner cash, acquisitions left out |
|---|---|---|---|---|---|---|---|
| 2019 | 168.9 | 11.3 | 71.5 | 148.1 | 51.1 | -62.0 | 86.1 |
| 2020 | 373.4 | 14.5 | 50.3 | 25.0 | 54.6 | 283.5 | 308.5 |
| 2021 | 275.7 | 18.7 | 69.6 | 104.2 | 56.0 | 83.2 | 187.5 |
| 2022 | 272.5 | 22.7 | 87.5 | 101.1 | 62.4 | 61.1 | 162.2 |
| 2023 | 376.7 | 30.8 | 106.2 | 69.0 | 72.4 | 170.7 | 239.7 |
| 2024 | 347.2 | 36.2 | 158.2 | 156.5 | 84.1 | -3.8 | 152.7 |
| 2025 | 564.3 | 48.3 | 193.6 | 323.3 | 104.3 | -0.8 | 322.4 |
| five-year average 2021 to 2025 | | | | | | **62.1** | **212.9** |

  Stock pay is the cash-flow add-back, which the awards note confirms ($47.9M expensed in 2025 plus $0.4M under the
  Standard Bearer plan; options and restricted stock, five-year vesting; 10-K Note 14). No other stock-pay line, no
  securities inside operating cash, no finance-lease principal (debt is HUD mortgages, $144.4M at 2025-12-31, Note 13).
  "Cash paid for acquisitions" is the filer's line: in 2025 it is almost entirely real estate ($326.7M aggregate purchase
  price for the real estate of 28 operations, 10-K Note 8); in 2021 and 2022 the filer split it into business
  acquisitions ($6.0M, $16.4M) and asset acquisitions ($98.2M, $84.7M).

### The balance sheets first, eight to ten years of them (read here because the file closes before Q4) **[M2025-032]**
From the first-filed XBRL vintages (tool table, accessions `0001125376-18-000028` to `0001125376-26-000007`) and the filed
statements of 2023 to 2025 (10-K `0001125376-26-000007`) and 2026-06-30 (10-Q `0001125376-26-000034`); USD millions.

| year-end | assets | liabilities | equity | cash | receivables | goodwill + intangibles | PP&E net | right-of-use assets | lease liabilities | debt | self-insurance liabilities | retained earnings |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2014 | 494 | 236 | 259 | 50 | n/a | 30 | 150 | (pre-ASC 842) | | 68 | | 146 |
| 2016 | 1,001 | 541 | 456 | 58 | n/a | 46 | 485 | | | 284 | | 235 |
| 2017 | 1,102 | 602 | 492 | 42 | 265 | 114 | 537 | | | 316 | | 265 |
| 2018 | 1,182 | 580 | 591 | 31 | 276 | 111 | 608 | | | 246 | | 345 |
| 2019 | 2,362 | 1,706 | 654 | 59 | 309 | 57 | 768 | 1,047 | 1,019 | 330 | | 392 |
| 2020 | 2,546 | 1,727 | 818 | 237 | 305 | 57 | 778 | 1,026 | 999 | 118 | | 551 |
| 2021 | 2,851 | 1,829 | 1,021 | 262 | 329 | 63 | 888 | 1,139 | 1,109 | 160 | | 734 |
| 2022 | 3,452 | 2,203 | 1,247 | 316 | 408 | 83 | 992 | 1,451 | 1,421 | 156 | | 946 |
| 2023 | 4,178 | 2,680 | 1,492 | 510 | 485 | 84 | 1,091 | 1,756 | 1,722 | 152 | 166 | 1,143 |
| 2024 | 4,669 | 2,829 | 1,837 | 465 | 570 | 105 | 1,291 | 1,861 | 1,829 | 148 | 212 | 1,427 |
| 2025 | 5,463 | 3,228 | 2,232 | 504 | 637 | 104 | 1,697 | 2,098 | 2,064 | 144 | 246 | 1,756 |
| 2026-06-30 | 5,749 | 3,304 | 2,442 | 262 | 669 | 104 | 2,097 | 2,144 | 2,111 | 140 | 296 | 1,948 |

What moved and why, "what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**:
(1) Equity grew from $259M to $2,442M in twelve years almost wholly from retained earnings ($146M to $1,948M); paid-in
capital rose from stock-pay credits and option exercises ($615M APIC at 2025, net of $139M treasury), not from a share
sale since 2015. Goodwill and intangibles are small ($104M, 2% of assets): the buying is of real estate and leased
operations, not of businesses with goodwill, and the filer says so (10-K Note 2, acquisition accounting). (2) The 2019
step in assets and liabilities (+$1.2B each) is the lease standard: 253 of 373 facilities are leased, and the right-of-use
asset and lease liability ($2.1B each) are the present value of $3.08B of rent at 6.2% over 13.9 years (Note 15). The
leases are the business's real capital and they sit outside the equity. (3) PP&E rose from $150M to $2,097M as Standard
Bearer bought the buildings of operations it then runs ($155M of real estate in 2024, $327M in 2025, $375M in the first
half of 2026); the owned estate is now about a third of the facilities. (4) Receivables track sales: 46 days of service
revenue at 2025 (637/5,032), 49 in 2024, 46 in 2021; the allowance is small and steady ($7.8M). No build-up. (5) Cash rose
to $504M by 2025 and fell to $262M by June 2026 as the acquisitions outran operating cash; debt is $140M of HUD mortgages at
3.1% to 4.2% fixed with 25- to 35-year terms (Note 13); the $600M revolver (raised to $800M and extended to 2031 on
2026-08-19, 8-K `0001125376-26-000038`) is undrawn except $8.4M of letters of credit. (6) Self-insurance liabilities
(general and professional liability, workers' compensation) grew from $166M to $296M in thirty months, faster than revenue
(a 78% rise against a 36% rise in revenue), with provisions of $245M in 2025 against $210M paid (Note 17); the captive's
investments ($167M to $210M) are designated to those liabilities and are not free cash. (7) Accrued wages jumped $82.8M in
2025 (against $20.0M in 2024 and $48.0M in 2023) and reversed $39.4M in the first half of 2026: payroll timing, which
flattered 2025 operating cash. What the figures cannot say: the return on the landlords' capital, the value of the 253
leaseholds, and the cost of the pending government investigation (no accrual).

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is "who is paid to tell you": every quarterly release leads with an adjusted
earnings figure, a raised guidance range and a record, and the chief executive's words in the FY2025 release are a sales
pitch for organic growth ("we are actually excited that it's as low as it is", of 83% occupancy), so the reading must be
from the filings and the competitors' filings, not the release, since there is no "impartial advice" where there is an
"enormous amount of fees possible from one action, and no fees applicable from another action" **[M2020-037]**, and "don’t
ask the barber whether you need a haircut" **[M2011-083]**. A share is a business: the question is what the 373 facilities
will earn on the government's rates over ten years, held as if "the market closed for five years" **[M1997-109]**, and the
quotation "just tells us prices" **[M2006-077]**. No macro forecast enters: the ageing population in the 10-K's industry
section is not a reason, the economics of the business are. Margin of safety: a decision that needs "pencil and paper" is
"too close to think about" **[M1996-084]**. The analyst's habit here is the hardest: a ten-year record of rising earnings
is the cherished belief that the mind will defend. **Contrary evidence, written down as found** **[M1997-127]**: (a) three
Department of Justice matters in twelve years, each about billing (a $48M settlement with a five-year corporate integrity
agreement in 2013; a $48.0M qui tam settlement in 2024 on medical-director relationships; a civil investigative demand of
January 2024 on Medicare and Texas Medicaid claims from 2016 to the present, pending); (b) owner cash after acquisitions has
averaged $62M a year for five years against a $10.1B market value, so the owners have received nearly nothing in cash;
(c) the rival that copied the model (PACS, founded 2013) reached $5.3B of revenue in twelve years and then two DOJ demands,
a subpoena and an SEC investigation; (d) the long-lived incumbent (NHC, 89.7% occupancy) earns ordinary returns; (e) the
price is set by Medicaid in 17 states and by CMS, and the filer's own words are that it "cannot predict the ultimate
content, timing or impact" of reform; (f) the chief executive became chairman in September 2025 and a derivative suit of
July 2026 alleges insider stock sales and related-party transactions; (g) 2025 operating cash was flattered by $40M to
$60M of payroll timing.

## THE STANDING RULE
Owning this stake with the buyer's own money, unlevered and sized within what he can see fall by half, risks nothing the
buyer has and needs: "Never risk permanent loss of capital." **[L2023-005]**; "borrowed money has no place in the
investor's tool kit" **[L2014-005]**; the holder must be able to see it "go down 50 percent — or more — and be comfortable
with it" **[M2020-022]**, which for a name under an open government investigation is a real test of the buyer's conduct.
The target's own debt and exposures are Q9's.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**What it is, from the filings.** A holding company whose independent subsidiaries run 373 facilities in 17 states: 357
skilled nursing operations with 37,911 operational beds and 47 senior living operations with 3,402 units; 253 facilities
leased (104 from CareTrust under eight master leases, the rest under 19 other master leases and single leases) and 158
owned, 152 of them inside the captive REIT Standard Bearer, which also leases 38 to third parties (10-K FY2025,
`0001125376-26-000007`, Item 1 and Note 6). Skilled nursing is 95.6% of revenue. Service revenue by payer in 2025: Medicaid
39.8% plus Medicaid-skilled 6.0%, Medicare 23.7%, managed care 18.8%, private and other 11.7% (Note 3). Skilled nursing
days: Medicaid 59.0%, Medicare 11.6%, managed care 13.5%, other skilled 5.6%, private 10.3%; average daily rates: Medicare
$800.94, managed care $583.47, Medicaid $308.27, private $308.27; so 30.7% of the days (the "skilled mix") bring 49.4% of
the skilled revenue (MD&A, FY2025). Payroll is 60.0% of total expenses (46,000 full-time equivalents); rent 4.7% of revenue
($239.3M). The business, in one sentence: fill the beds (occupancy 82.2% in 2025, 72.8% in 2021, 79.2% in 2019), tilt the
days toward Medicare and managed care, and keep wages and rent below the rates that the government and the insurers set,
while buying more facilities each year (145 in 2021 to 2025) from operators who could not.

**The test: foreseeing the economics, not knowing the product** **[M2000-037]**, "a reasonable fix on about what the earning
power and competitive position will look like in five or 10 years" **[M2012-065]**. The product is plain. The economics
turn on six variables (test 2, **[M1998-044]**), judged for predictability:
1. *Medicaid rates*, 59% of days, set annually by seventeen legislatures: the 10-K says the rates are "subject to a state’s
   annual budgetary requirements and funding", that the July 2025 federal law (OBBB) changes provider taxes and eligibility
   (six-monthly redeterminations from 2027, retroactive eligibility cut), that California projects a two-year shortfall and
   Colorado proposed stagnant provider pay for 2025 to 2026 (Item 1, Revenue sources). Direction foreseeable: over the span
   the rates have risen with costs (the filer's Medicaid per diem +4.6% in 2025; NHC's +8.6% in 2024 and +3.5% in 2025, NHC
   10-Ks `0001437749-25-005690` as quoted in `0001437749-26-005910`). Level in 2036: not foreseeable, and the filer says so:
   "we cannot predict the ultimate content, timing or impact on us of any healthcare reform legislation" (Item 1A).
2. *Medicare's rate*, set by CMS each October (+4.2% in 2024, +3.2% in 2025): foreseeable in shape, political in level.
3. *The shift from Medicare to Medicare Advantage*: managed care pays $583 a day against Medicare's $801, a 27% discount,
   and Medicare fell from 26.6% of service revenue in 2023 to 23.7% in 2025 while managed care rose from 18.0% to 18.8%
   (Note 3). Foreseeable in direction; its pace and the operator's offset through mix are not.
4. *Labor*, 60% of expenses: wages rise at times "in excess of general inflation or in excess of increases in reimbursement
   rates we receive" (Item 1, Employees); the CMS minimum-staffing rule of April 2024 was repealed on 2025-12-02 (Item 1).
5. *The acquisition supply*: growth has come from distressed operators selling or landlords re-tenanting (CareTrust moved
   two Eduro facilities to Ensign in 2024; CTRE 10-K `0001628280-26-007664`, Note 4); whether the supply continues is a
   guess about other people's failures.
6. *Enforcement*: Medicare recoupment reviews at 25 subsidiaries, a pending DOJ civil investigative demand, and the False
   Claims Act (Item 3). A recurring cost of unknown size.

Do the statements tell me "what the future financial statements are going to look like" **[M2008-033]**? Ten years of
filed statements show revenue $1.65B to
$5.06B and net income $50M to $344M (XBRL, FY2016 to FY2025), with two dips (2017, when operating income fell to $43M from
$92M; 2023, with $60.8M of litigation charges, 10-K `0001125376-24-000018` MD&A). They show what the model does with
facilities bought at one and two stars (the filer: "At the time of acquisition, the majority of our facilities typically
hold 1 and 2-Star ratings", Item 1); they do not show what Medicaid pays in 2036. The rows ask for "some model in our mind
of how far off we can be" **[M2011-084]**. The spread is thin: skilled services segment income is 12.7% of its revenue ($616.4M on $4,837.8M, Note 7) and consolidated
pre-tax income 9.0% of revenue; a five percent cut in Medicaid rates with no cost relief is about $115M, a quarter of
pre-tax income. "important and knowable" **[M2006-076]**: the rate path is important; its level is not knowable, only its
habit of tracking costs. Would the insiders "put down on paper their predictions" **[M2000-105]**? The company guides one
year at a time.

**Routing.** No fast technological change: the threats are payers and wages, a forecast of "what their prospective
customers will do in the future" rather than of technology **[M2017-019]**; not a bank; a holding company of independent subsidiaries understood by its parts, and the
deciding part is skilled services (segment income $616.4M against $37.6M for Standard Bearer and a $197.3M loss for all
other, Note 7), so the parts rule of section B is met by the one part. **The perimeter.** The nearest narrated error is
retail: "it’s easy to sort of think you understand retail, and then subsequently find out you don’t" **[M2014-052]**; a
nursing operator is retail-like, local, labor-heavy, a business where "you have to stay smart" **[M1995-040]**. Written
down as contrary evidence. Against it: the economics are "right there in black and white" in ten years of reports
**[M2005-015]**, the drivers are few and the filer discloses each of them by cohort, payer and per diem every year.

**VERDICT: IN**, at the low precision the rows ask, "we had to have a feel for it, and we had to know our limitations"
**[M2015-086]**: the ten-year shape of the economics can be foreseen (more beds, a Medicaid majority, a thin spread on
government rates that has tracked costs over the span, growth by buying others' failures); the level of the rates cannot,
and that is carried to Q2 as what could destroy the castle and to Q9 as an exposure. The doubt row **[M2002-092]** was
weighed: the doubt here is about the payer's future conduct, which Q2's eleventh test owns, not about how the business
makes its money. Filing facts: Note 3 payer table and the MD&A per-diem table, 10-K `0001125376-26-000007`.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The question** **[M1995-038]**: "why is that castle still standing? And what’s going to keep it standing or cause it not
to be standing five, 10, 20 years from now. What are the key factors? And how permanent are they? How much do they depend on
the genius of the lord in the castle?" The filer's own answer (10-K `0001125376-26-000007`, Item 1): "We believe our success
is largely driven by our proven ability to build strong relationships with key stakeholders in local healthcare
communities", local leaders empowered to make each facility "the “operation of choice” in their community", a training
system (Ensign University, the New Market CEO programme since 2006) and "an established track record of successful
acquisitions" of "under-performing and performing post-acute care operations". That is an answer about the lord and his
lieutenants, not about the castle.

**The castle tests, each with its filing fact.**
1. *The attacker with money* **[M2011-015]**. The answer is yes, and it has been done. PACS Group, founded 2013, has
   "successfully acquired and integrated over 300 facilities", $5.29B of revenue in 2025 against Ensign's $5.06B, with the
   same playbook ("acquiring underperforming custodial care focused facilities and converting them into higher-value
   short-term transitional care focused facilities"), the same decentralised "locally led, centrally supported model", and
   the same landlord: CareTrust names Ensign, Pennant and PACS as its SEC-reporting tenants (PACS 10-K
   `0002001184-26-000005`, Item 1; CTRE 10-K `0001628280-26-007664`, Item 1). "there are going to be marauders. And they’ll
   never go away." **[M2017-012]**. What the marauder has not copied is survival: PACS did not file four periodic reports on
   time, reports material weaknesses, and carries two DOJ civil investigative demands, a DOJ subpoena and an SEC
   investigation (PACS 10-K, Items 1A and 3). The model is copyable; the discipline, so far, has not been.
2. *Pricing power and the agony before a rise* **[M2005-020]**. None. Medicaid rates are "established by each state";
   Medicare pays "a predetermined amount per patient, per day" under PPS; managed care rates are negotiated at a 27%
   discount to Medicare ($583 against $801). Private payers, 10.3% of days, pay $308.27, the same as Medicaid's $308.27
   (MD&A per-diem table): even the customer who could pay more does not. It is the gas station where "whatever he charged
   for gas was my price" **[M2012-109]**, with the state in the role of the rival.
3. *Unit volume and share of mind* **[M1999-054]**. The volume evidence is the strongest thing in the file: consolidated
   occupancy 72.8% (2021), 75.3%, 78.5%, 80.5%, 82.2% (2025); same-facility 82.9% and transitioning 84.2% in 2025;
   skilled days up 6.8% at same facilities; skilled mix by revenue 49.4%; 153 of 357 skilled facilities rated four or five
   stars against 114 in 2021; the overall CMS rating 6.8% above the national average with a portfolio bought at one and two
   stars (10-K Items 1 and 7; FY2021 and FY2023 10-Ks `0001125376-22-000019`, `0001125376-24-000018`). The referral source
   (the hospital, the managed-care plan) does choose this operator more each year. But it still fills fewer beds than the
   incumbents: NHC 89.7%, PACS 89% (below).
4. *The low-cost position* **[L1996-015]**. Not shown. Cost of services is 79.5% of skilled revenue in both 2024 and 2025;
   payroll is 60% of expenses, paid at local market wages under state staffing minimums; rent is 4.7% of revenue. NHC's
   salaries, wages and benefits are 60.7% of revenue (NHC 10-K `0001437749-26-005910`, MD&A). No filer discloses cost per
   patient day, so parity cannot be shown either way **[M2001-013]**.
5. *The brand* **[M2008-075]**. None in the customer's mind; the facilities keep local names, and the filer's "brand
   strategy" is the local operation's reputation (Item 1).
6. *Would the customer still choose it over the low bid* **[M2017-009]**? There is no bid; the price is the payer's. The
   choice is made on bed availability, star rating, location and the discharge planner's relationship, which test 3 shows
   Ensign winning at the margin and test 1 shows PACS winning as well.
7. *Ask the competitors* **[M1999-130]**, **[M2022-021]**. The landlord's answer is in its filing: CareTrust calls Ensign its
   "Financially Secure Primary Tenant" (23% of its rent, $92.1M a year on 113 properties and 12,218 beds), guarantees eight
   Pennant properties on Ensign's name, and when its other tenants fail it moves the facilities to Ensign (two Eduro
   facilities in Colorado in March 2024; one Kansas facility in September 2024; seven facilities added to an Ensign master
   lease for $10.0M of rent in 2025; CTRE 10-K Note 4). The landlord would trade its other operators for Ensign.
8. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Widening on the operating metrics (test 3) and on the owned
   estate (158 properties, $2.1B of PP&E, a third of the facilities); narrowing on the enforcement side (a 2024 DOJ demand
   pending; self-insurance liabilities up 78% in thirty months against a 36% rise in revenue; a derivative suit of July
   2026).
9. *What could destroy, modify or reduce it* **[M2000-014]**. (a) The payer: 59% of days at Medicaid rates set by
   seventeen legislatures under the July 2025 federal law's provider-tax and eligibility changes; the filer's own
   sensitivity is a quarter of pre-tax income for a five percent Medicaid cut (Q1). The nearest row is the utility
   lesson: "the regulatory climate in a few states has raised the specter of zero profitability" and "it is difficult to
   project both earnings and asset values" **[L2023-011]**. (b) The Medicare Advantage shift, which moves days from $801 to
   $583. (c) Exclusion: "In the event of an uncured material breach of the CIA, the Company could be excluded from
   participation in Federal healthcare programs" (8-K `0001125376-13-000086`); the same remedy sits behind the pending
   CID. (d) The supply of distressed facilities drying up, which ends the growth half of the model.

**The competitor row** (same metric, each from its own filings).

| name | occupancy, operational beds | operating margin (operating income / revenue, XBRL) | return on year-end equity (net income / equity) | source |
|---|---|---|---|---|
| ENSG | 2017 75.4, 2018 77.4, 2019 79.2, 2020 73.5, 2021 72.8, 2022 75.3, 2023 78.5, 2024 80.5, 2025 82.2 | 2016 5.5%, 2017 2.7%, 2018 4.8%, 2019 6.3%, 2020 9.3%, 2021 9.9%, 2022 9.8%, 2023 6.8%, 2024 8.4%, 2025 8.4% (after rent) | 2016 11%, 2017 8%, 2018 16%, 2019 17%, 2020 21%, 2021 19%, 2022 18%, 2023 14%, 2024 16%, 2025 15% | 10-Ks FY2019 `0001125376-20-000018`, FY2021, FY2023, FY2025; companyfacts |
| NHC (National HealthCare, operating since 1971, owns most of its buildings) | 2014 88.9, 2015 90.0, 2016 89.5, 2017 90.2, 2018 89.8, 2019 90.3, 2020 83.6, 2021 80.6, 2022 83.8, 2023 87.9, 2024 88.6, 2025 89.7 | 2016 6.6%, 2017 5.6%, 2018 5.7%, 2019 4.9%, 2020 4.7%, 2021 4.7%, 2022 2.9%, 2023 5.0%, 2024 6.9%, 2025 8.5% (owner-operator, no rent on owned) | 2016 7.5%, 2017 8.0%, 2018 8.0%, 2019 8.8%, 2020 5.3%, 2021 15.3% (securities gains), 2022 2.6%, 2023 7.4%, 2024 10.4%, 2025 11.2% | 10-Ks `0001047335-17-000042`, `0001437749-19-002958`, `0001437749-22-003787`, `0001437749-24-004619`, `0001437749-26-005910`; companyfacts |
| PACS (founded 2013, IPO 2024) | 2025: portfolio 89%, mature 95%, ramping 86%, new 81% | 2022 9.5%, 2023 6.7%, 2024 3.0%, 2025 5.9% | 2024 8%, 2025 20% (on post-IPO equity) | 10-K `0002001184-26-000005`; companyfacts |
| BKD (Brookdale, senior living, 93.9% private pay; not a skilled-nursing comparator) | not comparable | operating losses in 10 of 13 years 2013 to 2025 | net loss every year 2013 to 2025 except 2020; equity negative at 2025 | 10-K `0001332349-26-000032`; companyfacts |
| CTRE (landlord) | rent from Ensign $92.1M a year, 23% of CTRE's rent; new sale-leasebacks written at an 11.0% initial cash yield; the 2025 Ensign amendment added $10.0M of rent for seven facilities | | | 10-K `0001628280-26-007664`, Notes 3 and 4 |
| SBRA (landlord) | no Ensign lease: the FY2025 10-K does not mention Ensign | | | 10-K `0001492298-26-000008` |

**The parts table** (section B). The filer reports two segments since 2022 and an "all other" category; segment income is
income before tax (Note 7). Three years are reported on this basis (2023 to 2025), said so.

| part | segment income 2023 to 2025 (USD M) | share of the positive total | castle | decides |
|---|---|---|---|---|
| skilled services (357 operations) | 464.9 + 518.5 + 616.4 = 1,599.8 | 94% | the operating culture and the referral relationships, tested above | yes, more than half |
| Standard Bearer (152 properties, 116 leased to Ensign's own subsidiaries) | 29.1 + 29.3 + 37.6 = 96.0 | 6% | a landlord to itself: $107.6M of its $126.9M rent is intercompany; its economics are a lease yield | no |
| all other (senior living, ancillaries, the Service Center) | (151.9) + (159.4) + (197.3) | loss | none | no |

The file closes on skilled services.

**The field's returns over the last full cycle** (section C), peak 2019 to trough 2021 to the new peak 2025, judged in
words from the filings. The durable owner-operator of the field, NHC, earned ordinary returns across the cycle: an
operating margin of three to nine percent and a return on equity near eight percent on average, with two bad years in
six, and it owns its real estate, so its return is the whole return on the capital the business needs. Ensign earned
fifteen to twenty-one percent on its equity in every year since 2018, through the trough, the $60.8M of litigation
charges of 2023 and a chief-executive handover in 2019; but its equity excludes the $2.1B present value of the leases on
253 facilities, whose owners earn their own ordinary return (CareTrust writes new leases at about eleven percent cash
yield), and once the landlords' capital is counted the whole business earns something nearer the incumbent's figure than
the operator's. PACS, the copy, shows four years of falling then recovering margin and no full cycle. So: the castle of
the field protects ordinary returns; the excess that Ensign shows belongs to the operating skill applied to each bought
facility, which must be applied again to the next one. The returns held, so the castle is not "shown on the evidence to be
filling in"; the ordinary-returns rule of section C does not fit cleanly either, because the filer's own filings show
returns that are not ordinary, and the rule is written for a field whose durable players earn ordinary returns. A change
for the better (occupancy and mix rising since 2021) is credited only on a full cycle; the cycle since the trough is four
years and the pre-COVID peak occupancy of 79.2% was passed only in 2024.

**Why it closes here, and in which box.** What keeps the castle standing is the lord: a culture that turns one-star
facilities into four-star ones, and a stream of such facilities to buy. The rows' second test asks exactly this: "if a
business requires a superstar to produce great results, the business itself cannot be deemed great" **[L2007-006]**; "The
really great business is one that doesn’t require good management" **[M1996-037]**; "A moat that must be continuously
rebuilt will eventually be no moat at all." **[L2007-005]**. Against that, a culture can be a moat, "a culture and a
business model, which people are going to find very, very difficult to copy, even semi-copy" **[M2009-038]**, and this one
has lasted twenty-six years, two chief executives and a corporate integrity agreement. The price-setter sits above both:
the spread between the government's rates and local wages is thin (Q1) and the state can take it, as the utility lesson
shows **[L2023-011]**. Whether this culture holds at five hundred facilities, whether the supply of failed operators
continues, and what seventeen legislatures pay in 2036 are forecasts the industry's insiders would not write down: the
filer guides one year and says, in its own risk factor, that it cannot predict reform. That is the tenuous moat of
**[M2000-019]**: "when we see a
moat that’s tenuous in any way [...] it’s just too risky. We don’t know how to valuate that, and therefore we leave it
alone." The nearest alternative reading, OUT under section C, was weighed and not taken, because the evidence does not
show the castle filling in; it shows a castle whose keeper is the point, and "the number one risk factor is that this
business gets the wrong management" **[M2021-042]**. "there are many businesses — industries where it’s very hard to
evaluate moats" **[M2001-069]**.

**VERDICT: TOO HARD (NATURE).** The castle's future cannot be judged from where the analyst stands: it rests on the lord
**[M1995-038]**, **[L2007-006]**, on a moat rebuilt at each acquisition **[L2007-005]**, and on a payer that sets the price
**[M2012-109]**, **[L2023-011]**; the box is "too hard" **[M2006-013]**, by nature and not by work, since no filing not yet
read holds the forecast **[M2000-105]**, and a lower price does not reopen it **[M2000-038]**. The file closes here.
Integrity facts found on the way are recorded under AFTER THE STOP, not judged.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED.** The file closed at Q2. Facts found that bear here are under AFTER THE STOP.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** The balance sheets were read in Step 0 as the template asks when the file closes before Q4. Facts found
that bear here (the featured adjusted figures, the guidance, the litigation adjustments) are under AFTER THE STOP.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.** Integrity facts recorded under AFTER THE STOP, not judged; the box line carries the flag.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
# COMPUTATION, NOT A CLEARANCE
*The file closed at Q2. Everything below is arithmetic required by the T2 protocol so that the rules under test can be seen
to bear; it carries no entry language and changes no box (operator rule 3). Script: `_work_T2_ENSG/q7_compute.py`.*

**The cash input.** Owner cash after every real cost: operating cash as filed (after the company's own income taxes paid,
$116.2M in 2025, and after interest), less stock pay (the cash-flow add-back, treated as cash), less purchases of property
and equipment, and, under the default pair of rule under test, section D(c), less cash paid for acquisitions; five-year
average 2021 to 2025, from the table in Step 0. Depreciation as filed is the alternative shown beside (the PG specific).
No net-income proxy anywhere **[L2021-003]**, **[L2015-004]**. Tax treatment: owner cash is after the company's own
income tax, no conversion; the effective rate was 24.4% in 2025 and the 10-K attributes the gap to the statutory rate to
excess tax benefits of stock pay (Note 12), not to a carryforward that runs out, so section E's shelter does not arise.

**Rule under test, section D(c)**, acquisitions. Cash paid for businesses, net of businesses sold (none sold in the
window), is capital spending for the range. The default pair, acquisitions deducted and total growth credited, gives the
all-spending series of Step 0: 83.2, 61.1, 170.7, -3.8, -0.8, five-year average **$62.1M**. Under rule under test,
section D(b), that series changes sign, so growth is measured between the halves of the window: 72.2 (2021 to 2022)
against -2.3 (2024 to 2025), a change of sign again, so the range on this pair is the no-growth case alone, said so.
The second pair, acquisitions left out and only organic growth credited as the filer reports it: the series 187.5,
162.2, 239.7, 152.7, 322.4, average **$212.9M**; the filer reports organic growth as same-facility revenue growth, 4.2%
(2021), 7.9% (2023), 6.9% (2024), 6.5% (2025; 2022 not read), average **6.4%** (10-Ks `0001125376-22-000019`,
`0001125376-24-000018`, `0001125376-25-000021`, `0001125376-26-000007`, MD&A); the literal compound rate of this series,
14.5% a year, is not credited, because under section D(c) total growth may never be credited with acquisitions left out.
No deal in the window was financed by debt (the revolver is undrawn; acquisitions were paid from cash), so section
D(c)'s debt sentence bears only in form: the value is on unlevered owner cash less today's net debt, which is net cash.

**Rule under test, section D(a)**, cycles. The first year of the window, 2021, is the COVID trough (occupancy 72.8%, the
lowest in the span; $24.2M of deferred 2020 payroll tax repaid that year and again in 2022, FY2021 10-K Note 3), and the
year before it, 2020, was aberrational the other way ($48.3M of payroll tax deferred, sequestration suspended, state
relief funds). The last full cycle, peak to peak, runs from the pre-COVID occupancy peak of 2019 (79.2%) to the new peak
of 2025 (82.2%); the base over it is shown beside the literal window: all-spending average 2019 to 2025 **$76.0M**;
acquisitions-left-out average **$208.4M**. The two bases differ little from the five-year ones, so the cycle adjustment
does not move the result.

**Rule under test, section D(d)**, working capital. Operating cash as filed already nets the change in working capital,
so the increase is deducted. One item is a single year's swing: accrued wages rose $82.8M in 2025 against $20.0M in 2024
and $48.0M in 2023 and reversed $39.4M in the first half of 2026 (10-K cash-flow statement; 10-Q `0001125376-26-000034`);
the filer ties it to nothing, so it is not an aberrational year by section D(a), but the range at the business's
working-capital intensity before the swing is shown beside: the excess over the two prior years' average ($48.8M) is
removed from 2025, base **$203.1M** on the second pair.

**Rule under test, section D(e)**, growth spending. The filing does not allow the maintenance guess: it reports one line
for property and equipment ($193.6M in 2025, $158.2M in 2024), says the money goes "to improve the quality of care at our
existing operations" and that "approximately $190.0 million" is budgeted "for renovation projects in 2026" (10-K
Liquidity), and gives no split; depreciation ($104.3M) is a floor, not a guess, because the tenant maintains 253 leased
buildings whose depreciation sits on the landlords' books. So the central case is the all-spending case and the
depreciation variant is shown beside (average 2021 to 2025, acquisitions left out: **$260.1M**); nothing is charged twice.

**Rule under test, section H**, the basis. The central figure is built on the all-equity basis: owner cash before
interest and after the company's tax, against the market value of the shares plus net debt. Net debt at 2026-06-30
(10-Q): borrowings $139.7M (HUD mortgages, no finance leases) less cash $262.3M less current investments $58.5M =
**net cash $181.1M**; the captive insurer's deposits and investments ($210.1M) are designated to its liabilities and are
left out, said so; operating leases ($2,111M present value, $3.08B undiscounted) are left out and said so. Equity plus
net debt = $10,132M less $181M = **$9,951M**. The interest adjustment is small and runs the wrong way for a net-cash
company: adding back after-tax interest paid ($5.2M) and removing after-tax interest income ($18.5M) lowers owner cash by
$13.3M (second-pair base $199.6M); the as-filed figures are the equity-only case, shown beside and never deciding alone.

**Rule under test, section D(f)**, the cap. The shown organic rate, 6.4%, is above the discount rate and is carried for
ten years only, then zero nominal growth; no result traces to an absurdity; a price above the top of the range closes OUT
however wide the range, by the floor convention.

**The range** (ten years at the shown rate then no growth, discounted at 5.66% throughout; per share after adding net
cash; price $173.84):

| basis | base (USD M) | growth | whole business, no-growth to shown-growth (USD M) | per share, all-equity (H) | per share, equity-only (beside) | fair price, all-equity | fair price, equity-only |
|---|---|---|---|---|---|---|---|
| **Pair 1, the default (D(c)): acquisitions deducted; no-growth alone (D(b))** | 62.1 | none | 1,097 (a point) | **$21.92** | $18.82 | **$13.76** | $10.65 |
| Pair 1 on the 2019 to 2025 cycle base (D(a)) | 76.0 | none | 1,342 | $26.14 | $23.03 | $16.14 | $13.03 |
| Pair 2 (D(c), beside): acquisitions left out; organic 6.4% | 212.9 | 6.4% | 3,762 to 6,234 (ratio 1.66) | **$67.65 to $110.07** | $64.54 to $106.96 | **$49.70** | $46.59 |
| Pair 2, owner cash before interest (H) | 199.6 | 6.4% | 3,526 to 5,844 | $63.61 to $103.38 | | $46.79 | |
| Pair 2 on the cycle base (D(a)) | 208.4 | 6.4% | 3,683 to 6,103 | $66.30 to $107.83 | | $48.72 | |
| Pair 2, 2025 wage swing removed (D(d)) | 203.1 | 6.4% | 3,589 to 5,948 | $64.69 to $105.17 | | $47.56 | |
| Depreciation variant (the PG specific), acquisitions left out | 260.1 | 6.4% | 4,595 to 7,615 | $81.95 to $133.77 | | $60.02 | |

**Fair price** (a reporting figure, never a verdict; Part VII): the price at which the midpoint of the range earns the
floor of about ten percent **[M2003-149]**, **[L2002-020]**, applied to owner cash after the company's own tax
**[M1994-004]**. CONVENTION of this run, confessed: the midpoint is the average of the no-growth and shown-growth cash
streams, and the fair price is that stream's present value at the floor rate, per share, less net debt on the all-equity
basis (section H) and without the adjustment on the equity-only basis. Default pair: **$13.76** all-equity, $10.65
equity-only. Second pair: **$49.70** all-equity, $46.59 equity-only. No cheap price is reported.

**The reading, as a computation only.** On every basis the price, $173.84, sits above the top of the range: 7.9 times the
default pair's point value and 1.6 times the top of the second pair's range. The expected return at the price is 0.6% on
the default pair and 2.1% on the second, against a floor of about ten percent, so the name would be quit on, "there’s just
a point at which we drop out of the game" **[M2003-149]**, and rule under test, section D(f), closes it OUT by the floor
convention however wide the range. Were Q7 reached, the second pair's range is narrower than three to one (1.66) and the
price is above it: OUT, not TOO HARD. The widest reading, the depreciation variant, tops at $133.77. The arithmetic says
what Step 0's table said in words: the owners have received almost no cash in five years because every dollar went into
buying facilities, and the market is paying for the facilities not yet bought. None of this is a clearance.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts under AFTER THE STOP.

---
## THE BOX
**TOO HARD (NATURE)**, decided at Q2: the castle's future cannot be judged, because what keeps it standing is the lord and
a moat rebuilt at each acquisition under a payer that sets the price **[M1995-038]**, **[L2007-006]**, **[L2007-005]**,
**[M2000-019]**, **[M2006-013]**; the forecast is one the insiders would not write down, so the cause is nature, not work
**[M2000-105]**, **[L1993-023]**. Q7 was computed, not reached: on the default pair the value is a point near $22 a share
and on the second pair $68 to $110, against $173.84; the fair price is $14 (default) or $50 (second pair), all-equity.
**Integrity facts recorded, not judged.** A test record under the T2 protocol: it binds nothing and enters no register.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on a later question, each with its source **[M1997-127]**; written down, not weighed; no
verdict; the box unchanged (operator rule 2).*

**Q3 (capital).** Net income on year-end equity 15% to 21% every year since 2018 (companyfacts; 10-K statements). The
capital the business needs includes the leased buildings: lease liabilities $2.06B at 2025 (present value at 6.2%),
undiscounted rent $3.08B, 13.9 years (10-K Note 15). Standard Bearer paid $326.7M for the real estate of 28 operations in
2025, about $11.7M each (Note 8), and $375.3M in the first half of 2026 (10-Q). Purchases of property and equipment ran
at 1.9 times depreciation in 2025 ($193.6M against $104.3M). Dividends were $14.4M on $344M of net income; everything else
was retained and spent on facilities. Standard Bearer's segment income was $37.6M on $126.9M of rent, of which $107.6M is
paid by Ensign's own subsidiaries (Note 7).

**Q4 (the accounts).** The accounts are clear and consistent across the span; receivables and allowances steady;
goodwill small; no restatement. Every quarterly release leads with adjusted figures: "Adjusted EBT, Adjusted net income,
Adjusted earnings per share, EBITDA, Adjusted EBITDA, Adjusted EBITDAR, and Funds from Operations" (8-K
`0001125376-26-000036`); adjusted EPS of $6.57 against GAAP $5.84 for 2025 (press release, 8-K `0001125376-26-000008`),
the difference being mainly stock pay ($48.3M), litigation ($12.0M) and system costs; "Litigation" was adjusted out at
$60.8M in 2023 and $4.6M in 2022 (FY2023 10-K `0001125376-24-000018`, MD&A) and $12.0M in 2025, described each time as
"specific proceedings and adjustments arising outside of the ordinary course of business". Annual earnings and revenue
guidance is issued and was raised in each of the first two quarters of 2026 ("Raises 2026 Annual Earnings and Revenue
Guidance", press releases of 2026-04-30 and 2026-07-27), with "record" in the chairman's quotations. The 10-K itself says
of Adjusted EBITDAR that it "excludes rent expense, which is a normal and recurring operating expense" and presents it
"only for the current period". Self-insurance provisions $245.0M in 2025 against $209.8M paid (Note 17). Accrued wages
+$82.8M in 2025, reversed in part in 2026.

**Q5 (the people).** The record: a founder-led company (Christopher Christensen, president from 1999, chief executive 2006
to 2019, executive chairman to 2025-09-01; Barry Port chief executive since May 2019 and chairman since September 2025,
combining the roles with a lead independent director; 8-K `0001125376-25-000115`; proxy `0001125376-26-000014`). The
integrity record, as filed: (1) a federal civil investigation of billing "since 2006", settled in October 2013 for a $48M
lump sum with a five-year corporate integrity agreement under which "the Company could be excluded from participation in
Federal healthcare programs" on an uncured breach (8-Ks `0001125376-13-000053`, `0001125376-13-000086`); (2) a May 2018
civil investigative demand on False Claims Act and Anti-Kickback Statute exposure in medical-director relationships, on
which the DOJ declined to intervene in April 2020, the relator proceeded, and the company "agreed to settle the civil case
for $48.0 million" in 2024, without admission (10-K FY2025 Item 3); (3) a January 2024 civil investigative demand
"to determine whether claims have been submitted to Medicare and Texas Medicaid for services which were unnecessary or
otherwise not consistent with existing reimbursement requirements", covering 2016 to the present, pending (Item 3; 10-Q
`0001125376-26-000034` Part II); (4) a derivative complaint filed 2026-07-16 (Thompson v. Keetch) alleging breach of
fiduciary duty "relating to the our healthcare regulatory compliance, staffing, executive compensation, stock sales by
certain of the individual defendants, and related-party transactions" (10-Q Part II); (5) a California cost-and-market
subpoena (OHCA) that the company has petitioned a court to void as unconstitutional (Item 3); (6) a $12.0M settlement of
California wage-and-hour class claims for six years to December 2025 (Note 18); (7) 25 subsidiaries under multi-claim
Medicare reviews at year-end, 18 at June 2026. Pay: the 2025 bonus pool of $49.9M was set by a formula on adjusted EBT
(a non-GAAP figure), though the committee deducted stock pay and the litigation charge, so the pool ran on GAAP pre-tax
income; the chief executive received $10.3M in cash bonus and $2.9M in vested stock on a $549K salary, total $13.8M;
$6.0M of the pool "would be awarded to charities and certain employees", including $2.1M to the retiring executive
chairman, at management's recommendation (proxy, Compensation Discussion). The retiring chairman also received
accelerated vesting, a $150K health-premium subsidy and a one-year consultancy (8-K `0001125376-25-000158`). Four
relatives of officers and a director are employed, the co-founder's brother as Chief Human Capital Officer at $1.46M
(proxy, Certain Relationships). Say-on-pay passed with 94.6% of votes cast for (8-K `0001125376-26-000026`). The proxy's
bonus-tier table contains a mis-set figure ("$1444.0 million"). Insider Form 4 filings numbered 56 to 79 a year from 2020
to 2026 (EDGAR index count; not read). Ability: the operating record of Q2's third test.

**Q6 (the money and the owners).** Retention: all but $14.4M of $344M retained in 2025; retained earnings $551M (2020) to
$1,948M (June 2026). Buybacks: $20.0M in 2025 and $40.0M in the first half of 2026 under authorisations of $40M (May 2026)
and a further $60M (June 2026), with no stated price (8-Ks `0001125376-26-000029`, `0001125376-26-000031`; 10-Q). Issuance:
no share sale since 2015; 4.07M options outstanding at a $96.87 average strike (7% of the shares) and 0.44M unvested
restricted shares; stock pay $48.3M, 14% of net income; options exercised in 2025 at a $50.39 average strike for $29.0M
(Note 14). The Standard Bearer equity plan grants executives stock in the captive REIT, valued quarterly by a third party
and callable by the company (proxy; the retiring chairman's 19,726 shares were bought back for $286K). Pay is tied to
pre-tax profit, not to capital employed; equity vests on service alone over five years; the chief executive recommends the
other executives' grants; a compensation consultant (Willis Towers Watson) validates the plan (proxy). The owners are
given annual guidance and quarterly adjusted figures (Q4 above).

**Q9 (ruin).** Debt $139.7M, HUD mortgages at fixed 2.4% to 3.3% coupons, 25- to 35-year terms, $4.2M due in 2026 (Note
13); an $800M revolver to 2031, undrawn, with a 3.75x net-debt-to-EBITDA covenant (8-K `0001125376-26-000038`). Rent
$238M a year on $3.08B of undiscounted lease commitments; "a default at a single facility could subject one or more of the
other facilities covered by the same master lease to the same default risk", and "Failure to comply with Medicare and
Medicaid provider requirements is an event of default under several of the Company’s leases, master lease agreements and
debt financing instruments" (Note 15). Self-insured professional liability, $296M of reserves at June 2026, with punitive
damages uninsurable in some states (Item 3). The aggregation: 59% of days on Medicaid in 17 states; exclusion from federal
programmes is the remedy behind the pending demand. Cash $262M at June 2026 after $376M of purchases in six months.

**Q12 (how the money is made).** No named business. The newspaper test's material is above: three government billing
matters in twelve years; a 2023 Arizona jury verdict for medical negligence, reversed on appeal in July 2026 (10-Q Part II);
the industry's custom of adjusted figures. Recorded, not judged.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). The
      session hit a timed limit after the reading and before any section was written; the run resumed from the files on
      disk, and the sections were then written and committed one at a time.
- [x] If dispatched to an analyst: this is a T2 test re-run, which binds nothing and enters no register; the per-question
      commits were made with the protocol's message form and trailer. **Departure, declared:** the protocol's pathspec names
      the working folder, but `Framework/v5/tests/_work_*/` is ignored by the repository's own rule (`.gitignore`, line 117),
      so git refused the folder pathspec and each commit named the run file alone; the working folder's scripts
      (`fetch.py`, `q7_compute.py`, `check_ids.py`) and transcribed filings stay on disk, uncommitted, as the ignore rule
      intends.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched (the blind rule). Seen by accident
      and declared under contamination at the head of this file: the file names in `Framework/v5/tests/` from the listing
      that created the working folder, and one commit subject of another test run in the git log line printed after a
      commit here; neither was opened or used. The position note is unfilled for the same reason.
- [x] Every v5 id resolves (`_work_T2_ENSG/check_ids.py`: every M, L and R id in `principle_ledger_v5.csv`, no E-ids,
      every quoted fragment beside an id found in that row); every filing fact has its accession; no number without a
      row, a filing or a confessed CONVENTION.
- [x] The order was kept; Q2 was the first STOP that failed and closed the run; Q7 is headed COMPUTATION, NOT A CLEARANCE
      and nothing after Q2 is a clearance.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the US Treasury; the price from an aggregator, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations paragraph); the facts for later questions
      are under AFTER THE STOP; the integrity flag is in the box line.
- [x] No point-in-time anchor: the run is dated today and every row cited is in the ledger as it stands.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 lines were declared and ignored; its owner-cash window
      stopped at 2019 and the table was rebuilt from the filings.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Eight things. (1) Rule under test, section D(c): its default pair, "acquisitions deducted, total growth credited", cannot
be executed for a serial acquirer that spends all its cash on facilities. Owner cash after acquisitions is near zero or
negative, so the series carries no growth to credit, section D(b) sends it to the no-growth case alone, and the "default"
range becomes a point that values a $10B company at $1.1B; the arithmetic is right and the figure is useless, and the
second pair carried all the weight. The rule should say what the "total growth" is measured on when the deducted series is
meaningless, or say that the second pair becomes the central case then. (2) Section D(c)'s "organic growth, as the filer
reports it": filers report organic revenue, not organic owner cash; this run accepted the same-facility revenue rate and
assumed the margin held, and said so; the rule should say whether that is allowed. (3) Section H's "cash and securities"
does not say whether a captive insurer's investments designated to its liabilities count; this run left them out and said
so. (4) The fair price, "the price at which the midpoint of the range earns the floor", names no computation; this run
averaged the two end streams and discounted them at the floor rate, as a CONVENTION of the run. (5) Section C of the gaps
case, "a field whose durable players earn ordinary returns over a full cycle", does not say what to do when the filer is
itself a durable player with excellent returns while the incumbent earns ordinary ones; this run read the difference as
the lord's and went to TOO HARD, and says the OUT reading was the nearest alternative. (6) The T2 protocol's commit
pathspec names a folder the repository ignores (self-audit). (7) The brief named Sabra as a landlord to Ensign for the
lease economics; Sabra's FY2025 10-K does not mention Ensign; and it named Brookdale, a private-pay senior living operator
with no skilled nursing, as a competitor for a company that is 95.6% skilled nursing; both were read and set aside with
the reason. (8) The template's position note requires a check of `PORTFOLIO.md` that the protocol's blind rule forbids;
the note is left as "not checked".
