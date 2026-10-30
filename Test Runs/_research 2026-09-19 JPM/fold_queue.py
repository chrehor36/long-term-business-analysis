import re, sys
P = 'Screens/WATCHLIST RUN QUEUE.md'
t = open(P, encoding='utf-8').read()

def count(t):
    m = re.search(r'^## COMPLETED FROM THE QUEUE\s*$', t, re.M)
    s = t[m.end():]
    n = re.search(r'^## ', s, re.M)
    sl = s[:n.start()] if n else s
    return len(re.findall(r'^- \*\*', sl, re.M)), m

before, m = count(t)
sys.stdout.write('register entries BEFORE: %d\n' % before)

ENTRY = """
- **JPM (JPMorgan Chase & Co.), 2026-09-19 - ALL FOUR BUSINESS GATES IN; FAIL AT Q5 ON PRICE**, quit on at
  the ~10% [E4-28] floor. **WAVE 6**, under the operator ruling of 2026-09-19 that the five banks are run.
  **THE FOURTH BANK THIS PROJECT HAS RUN and the SECOND to clear the business gates; the largest company
  the project has ever priced.** CIK 0000019617, found by `tools/sources.py cik_for('JPM')`.
  **Honest pre-tax expectancy 7.54% at the bottom boundary [E5-34] and 9.62% centred, against a 5.34%
  sovereign - above the bond by 2.2 to 4.3 points on every construction and below the floor at the bottom
  boundary and the centre.** Value range ~$200 to ~$340 a share; 3.08x tangible book.
  **Q2 IN, class NARROW, direction MIXED, on [E2-58]'s single exception measured on the COST OF
  OPERATIONS** - a 52% overhead ratio against BAC 61.65%, C 64.7% and WFC 66%, five-year means 55.40 /
  64.66 / 67.52 / 69.20, a 9.65-point gap on a $182,447M revenue base worth about $17.6bn a year pre-tax,
  and WIDENING - **and it explicitly FAILS the test ACNB passed on: JPMorgan is THIRD of six on the cost of
  total deposits in every one of five years** (5-yr means WFC 0.927%, BAC 1.066%, JPM 1.202%, MS 1.699%,
  C 1.902%, GS 2.958%), its noninterest-bearing deposit share fell 29.1% to 24.1%, its investment-banking
  fee wallet fell 9.1% to 8.4%, and its domestic deposit share is 12bp BELOW end-2021 after absorbing First
  Republic. Five-year mean ROTCE **20.80%**, first of six in four of five years (MS 17.66, GS 14.58, BAC
  14.56, WFC 12.87, C 8.38). **[E2-59] bites on a dated event: JPM held 11.30% of US domestic insured
  deposits at 2022-12-31, so the ordinary interstate-merger route to a $200bn bank was shut and what opened
  was an FDIC receivership auction - the 2023 advantage was GRANTED BY THE REGIME, not won from customers,
  and the $2,775M bargain purchase gain is scored that way.**
  **Q3 IN at GATE weight** (daily execution and leverage both ticked; assets/common equity 14.2:1).
  The Citigroup-2007 precedent on disk pointed to OUT and the run faced it: a 2015 GUILTY PLEA to federal
  antitrust, a 2020 DOJ Deferred Prosecution Agreement over precious-metals and Treasuries spoofing, an
  EURIBOR infringement re-imposed 2023, a $31.5M Indian money-laundering fine, the $290M Epstein
  settlement, and NEW March 2024 OCC/Federal Reserve consent orders over trade-surveillance data
  completeness - the SAME failure class as the 2020 DPA, which fires [E4-22]'s cockroach rule at full
  strength. **The gate was decided by an artifact NAMED AND THEN OBTAINED from the issuing authority: the
  Federal Reserve's own enforcement-actions file (2,889 actions). Thirteen entity actions against JPMorgan
  Chase & Co. since 2003, nine of them orders, ZERO still open, five civil money penalties totalling
  $878,932,500 - the largest of the six - and the 2024-03-08 order terminated 2025-12-04, twenty-one
  months. Citigroup and Wells Fargo each still have an OPEN order on the same register at the same date.**
  That is [E5-22]'s test - did they act when they learned - answered by the supervisor's own termination
  dates, and it is why this run does not reach the Citigroup conclusion, which rested on LIVE matters.
  **[E3-02] conformity tested at 2022-12-31 from the FDIC Call Reports, before anything was public:
  JPMorgan Chase Bank NA carried HTM securities at 1.40x equity - the LOWEST of seven institutions,
  against Silicon Valley Bank's 5.91x, Bank of America's 2.81x and First Republic's 1.63x - and the lowest
  assets/equity at 10.5x.** Its own HTM unrealized loss was $36,762M, 13.9% of common equity.
  **[E2-50] reserves: cumulative provision 2019-2025 $54,408M against cumulative net charge-offs $41,302M
  - 31.7% MORE reserved than lost - and the allowance covered the next year's charge-offs at 2.72x or
  better in every year.** [E2-67] met in SUBSTANCE and NOT in form: no reserving back-test is published;
  the one in the run file was built by the reader. **Zero net common shares issued in five years** (issued
  count 4,104,933,895 identical in all six filings read) while the outstanding count fell 12.8%.
  **LIVE CAPITAL-ALLOCATION FLAG: $31,640M of buybacks in 2025 at 2.57x tangible book against $9,898M at
  1.65x in 2023 - three times the dollars at 1.6 times the price, under a programme that states it "does
  not establish specific price targets or timetables", the exact inverse of [E5-25].** [E4-27]: the CEO's
  entire equity award pays maximum at ROTCE >= 18%, and the five-year buyback programme accounts for about
  3.8 points of the reported 20%.
  **Q4 IN - GOOD, not great.** The corpus's own stress [E3-24] does not bite: 10% of $1,542,462M of loans
  at 30% severity is $46,274M against $86,807M of pre-provision profit plus a $31,531M allowance, covered
  nearly three times; break-even against one year's PPP needs 5.63% of the book, 7.6x the worst filed
  charge-off rate, and erasing tangible common equity needs 27.21%. **The bank's own published result:
  SCB 2.5%, the regulatory FLOOR, so on the Federal Reserve's severely adverse scenario the modelled CET1
  depletion is at or below 2.5 points against a 14.2% actual ratio and an 11.5% requirement.**
  Strengths 3 of 3 with (3) QUALIFIED: uninsured deposits $1,743.9bn, **64.3% of deposits - against First
  Republic's 67.7%** - covered 87% by $1.5tn of liquidity sources at a 110% LCR, "primarily wholesale
  operating deposits", and in 2023 JPMorgan's deposit share ROSE while three banks failed.
  **NAMED DEATH, proposed as survival shape #27 THE LICENCE: $120.9bn - 35.3% of common equity - earns
  about 3.7% in Corporate as the regulatory buffer while the three operating segments earn 18% (CIB, on
  $149.5bn), 32% (CCB, on $56.0bn) and 40% (AWM, on $16.0bn); each additional point of required CET1 on
  $1,981,692M of RWA moves $19,817M from the 18-40% businesses into the 3.7% one, about $2.9bn a year
  pre-tax, and the mix is a Federal Reserve decision the owner has no vote in. LIKELY, and it runs both
  ways - Corporate's allocation falls to $98.4bn on 2026-01-01.**
  **Q5 OUT ON PRICE. Q6 IN.** Owner earnings on the bank CONVENTION (declared at Q3, two modifications:
  ACNB's CNR organic/acquired split, and a SECOND new here - the convention run on BOTH total assets at
  the Tier 1 leverage ratio AND risk-weighted assets at the 11.5% CET1 requirement, agreeing within 12% in
  2025; the half-year NOT annualised because it is struck on the seasonal balance-sheet peak): combined
  range $27,924M to $49,415M, a pre-tax yield of 3.82% to 6.76%. Three distorted years NAMED and removed
  per [E4-41] - 2021's $9,256M reserve release, 2024's $7.9bn Visa gain, 2023's $2,775M bargain purchase
  gain against the $2.9bn FDIC special assessment. **Five-year organic (c) $65,334M against $251,081M of
  net income - a $172.5bn SURPLUS, where the same construction gave Coastal Financial a $111.6M shortfall
  and ACNB a $143.8M surplus. The construction is not tuned to a result.**
  **THE STRONGEST FACT AGAINST THE VERDICT, and it nearly reverses it: on the record the business has
  DELIVERED, the price clears the floor.** Diluted EPS compounded 6.85% a year 2021-2025 and tangible book
  value per share 10.30% a year 2020 to mid-2026, against the 3.24% to 5.46% of perpetual growth the quote
  needs. **The whole Q5 failure rests on one judgment: that the 82.5% rise in net interest income from
  $52,311M (2021) to $95,443M (2025), on 52.3% of the revenue, was the federal funds rate and not the
  business.** And the board bought 8.9M shares at $317.28 in December 2025, inside the top quarter of this
  run's optimistic case - the disagreement is one year of multiple expansion, not an order of magnitude.
  **Price US$349.67** (2026-09-18 close, aggregator FLAGGED, corroborated against the Q2 10-Q's own filed
  market capitalisation of $870,104M at 2026-06-30) **x 2,658,186,195 shares** (cover of the 10-Q for the
  quarter ended 2026-06-30, accession `0001628280-26-054343`; **issued 4,104,933,895 less treasury
  1,446,747,700 reconciles to the share, and the issued figure would have overstated the cap 1.544-fold**;
  the count is FALLING at 21-27M a quarter, so the cap used is overstated and every yield understated,
  which is the conservative direction) **= cap US$929,488M. Sovereign 5.34%** (US Treasury daily par yield
  curve, 30-year, 09/18/2026, issuing authority, NOT FRED). **Bands $230 and $190, to be re-struck
  annually because tangible book compounds at about 10% a year.** See
  `Test Runs/2026-09-19 Run - JPM JPMorgan Chase.md`.
"""

t = t[:m.end()] + ENTRY.rstrip('\n') + t[m.end():]
after, _ = count(t)
sys.stdout.write('register entries AFTER: %d (delta %d)\n' % (after, after - before))
assert after == before + 1, 'EXACTLY ONE ENTRY MUST BE ADDED'

old_row = '| JPM | JPMorgan Chase & Co. | bank | **RUN** - see the operator ruling below |'
assert t.count(old_row) == 1, t.count(old_row)
new_row = (
 '| ~~JPM~~ | JPMorgan Chase & Co. | bank | **RUN 2026-09-19 - struck. ALL FOUR BUSINESS GATES IN; '
 'FAIL at Q5 on PRICE** (quit on at the ~10% [E4-28] floor; honest pre-tax expectancy 7.54% at the bottom '
 'boundary and 9.62% centred, above the 5.34% bond on every construction). **THE FOURTH BANK THIS PROJECT '
 'HAS RUN and the SECOND to clear the business gates; the largest company the project has ever priced.** '
 'Q2 passes on [E2-58]’s cost-advantage exception measured on the COST OF OPERATIONS (52% overhead '
 'against BAC 61.65 / C 64.7 / WFC 66, widening) and explicitly FAILS the cost-of-funds test ACNB passed '
 'on, being third of six every year. Q3 IN at GATE weight, decided by the Federal Reserve’s own '
 'enforcement register: thirteen entity actions since 2003, ZERO orders open, $878.9M of penalties, while '
 'Citigroup and Wells Fargo each still have one open. [E3-02] conformity tested at 2022-12-31 from the '
 'FDIC Call Reports: HTM at 1.40x equity, the lowest of seven institutions against SVB’s 5.91x. '
 'Named death **#27 THE LICENCE** (proposed). Price US$349.67, cap US$929,488M. Bands $230 and $190. '
 'Register entry 130. See COMPLETED. |')
t = t.replace(old_row, new_row)

old_s = '**So ~~CCB~~, ~~ACNB~~, ~~SOFI~~, JPM and TFC are run**'
assert t.count(old_s) == 1, t.count(old_s)
t = t.replace(old_s, '**So ~~CCB~~, ~~ACNB~~, ~~SOFI~~, ~~JPM~~ and TFC are run**')

anchor = 'as the record of why they were held.'
assert t.count(anchor) == 1
NOTE = anchor + """

*Dated note, 2026-09-19 (the JPM run), left beside the ruling rather than editing anything above it
(operator rule 6): **JPM is RUN and STRUCK - ALL FOUR BUSINESS GATES IN and a FAIL at Q5 on PRICE, quit on
at the ~10% [E4-28] floor. It is struck in the WAVE 6 table ITSELF, because - unlike CCB and ACNB - JPM IS
a row in that table, and it is NOT in the `#### EXCLUDED UNDER THE OPERATOR'S BANK DIRECTIVE` subsection
below, which names only CCB, ACNB and SOFI.** The brief for this run said the opposite on both counts
("JPM is not in the WAVE 6 table: strike it in the operator-ruling sentence and the excluded subsection");
the table contains it and the subsection does not, and the discrepancy is recorded rather than resolved by
editing. **Three rulings this run leaves behind for the one bank still queued (TFC):**
**(1) The missing evidence rung is NOT missing and it costs one HTTP request.** CCB said the ladder stopped
too soon for a regulated filer. Both rungs it named have now decided gates: ACNB used the FDIC Call Report
over 56 institutions, and this run used it over **4,411 institutions at six dates** for the deposit-share
and 2023-conformity tests and used the **Federal Reserve's own enforcement-actions file**
(`federalreserve.gov/supervisionreg/files/enforcementactions.csv`, 2,889 actions) **to decide Q3 - the gate
the Citigroup-2007 precedent says decides a bank.** The OCC's own register (`apps.occ.gov`) returned HTTP
404 to two attempts and is the one rung still genuinely absent.
**(2) [E3-03] criterion 2 IS passable for a bank, ONLY through [E2-58]'s single exception, and the
exception has at least TWO independent forms.** After four banks: CCB OUT at Q2, SOFI OUT at Q2, **ACNB IN
on the COST OF FUNDS** (a low deposit beta, 64bp below its market's median over five years), **JPM IN on
the COST OF OPERATIONS** (a 9.65-point overhead advantage, widening) **while FAILING ACNB's test
outright**. A bank with neither form is OUT. What the four runs do NOT settle is whether [E2-58]'s
exception is the right doorway at all, or whether [E3-29]'s purchase of a bank at 20:1 leverage means the
corpus intended an exception class in which Q2 returns NARROW by construction and the decision moves
wholly to Q3 and Q5. **Both readings remain open and it is the operator's call under PRIME RULE 5.**
**(3) The bank owner-earnings CONVENTION has now been tested across a factor of 1,300 in size and has not
broken** - a $111.6M shortfall at Coastal, a $143.8M surplus at ACNB, a $172.5bn surplus at JPMorganChase -
**and this run adds a SECOND modification beside ACNB's CNR split: for a bank with a $1.06 trillion trading
book, run (c) on BOTH total assets at the Tier 1 leverage ratio AND risk-weighted assets at the CET1
requirement, and never annualise a half-year struck on the seasonal balance-sheet peak.** They agreed
within 12% in 2025. **The run also records the one place the CONVENTION changes a verdict, which is what a
confessed convention is for: without it JPMorganChase's pre-tax yield is 7.81% and clears the floor with
3% growth; with it the bottom boundary is 7.54% and it does not.** See COMPLETED, and
`Test Runs/2026-09-19 Run - JPM JPMorgan Chase.md`.*"""
t = t.replace(anchor, NOTE)

open(P, 'w', encoding='utf-8').write(t)
final, _ = count(t)
sys.stdout.write('FINAL register entries: %d\n' % final)
sys.stdout.write('JPM struck in table: %s\n' % ('~~JPM~~ | JPMorgan Chase' in t))
sys.stdout.write('JPM struck in ruling: %s\n' % ('~~SOFI~~, ~~JPM~~ and TFC' in t))
sys.stdout.write('dated note present: %s\n' % ('Dated note, 2026-09-19 (the JPM run)' in t))
