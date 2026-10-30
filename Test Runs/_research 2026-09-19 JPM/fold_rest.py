import json, re, sys

# ---------- 1. alerts.json : two bands (Q5 price failure, ACNB precedent) ----------
AP = 'tools/alerts.json'
d = json.load(open(AP, encoding='utf-8'))
ids = {a['id'] for a in d['alerts']}
n0 = len(d['alerts'])
new = [
 {"id": "JPM-floor-band", "ticker": "JPM", "currency": "USD", "op": "<=", "threshold": 230.0,
  "active": True,
  "label": ("JPM floor band: quote at/below USD 230, where the BOTTOM BOUNDARY of the owner-earnings "
            "range returns the ~10% [E4-28] floor with 3% growth (2.03x the 2026-06-30 tangible book "
            "value per share of $113.35). All four business gates cleared 2026-09-19; the run failed "
            "at Q5 on price at $349.67 with an honest pre-tax expectancy of 7.54% at the bottom "
            "boundary. A LIVE CAPITAL-ALLOCATION FLAG binds position size DOWN. RE-STRIKE THIS BAND "
            "ANNUALLY: tangible book is compounding about 10% a year. Source: Test Runs/2026-09-19 "
            "Run - JPM JPMorgan Chase.md. Review only - no action from this ping.")},
 {"id": "JPM-deep-band", "ticker": "JPM", "currency": "USD", "op": "<=", "threshold": 190.0,
  "active": True,
  "label": ("JPM deep band: quote at/below USD 190, 1.68x the 2026-06-30 tangible book value per share "
            "of $113.35 and below anything the Firm itself has paid for its own stock since 2023 "
            "($142.42 average in 2023, $276.55 in 2025). RE-STRIKE ANNUALLY. Source: Test "
            "Runs/2026-09-19 Run - JPM JPMorgan Chase.md. Review only.")},
]
for a in new:
    assert a['id'] not in ids, a['id']
    d['alerts'].append(a)
json.dump(d, open(AP, 'w', encoding='utf-8'), indent=1)
sys.stdout.write('alerts: %d -> %d\n' % (n0, len(d['alerts'])))

# ---------- 2. SURVIVAL SHAPES index : add #27 THE LICENCE ----------
SP = 'Screens/SURVIVAL SHAPES - index.md'
t = open(SP, encoding='utf-8').read()
rows_before = len(re.findall(r'^\| \d+ \|', t, re.M))
anchor = '\n\n**Open:**'
assert t.count(anchor) == 1
ROW = ("| 27 | **The licence** *(proposed, pending the operator)* | JPM (2026-09-19) | the business earns a "
 "very high return on the capital it is PERMITTED to use, and a regulator - not the owner and not the "
 "manager - decides what fraction of the equity that is; the surplus is held at a bond return inside the "
 "same company, so the reported return is a blend the owner cannot set, it is re-priced periodically by a "
 "supervisory decision with no change whatever in the business, and the better the franchise the more the "
 "idle capital costs. It does not kill the company; it caps the owner's compounding, and the cap moves. | |")
t = t.replace(anchor, '\n' + ROW + anchor)

OPEN_ADD = (" JPM proposed **#27 THE LICENCE** (2026-09-19, **the fourth bank the project has run and the "
 "second to clear the business gates**), arguing it is none of #14, #17, #26 or #10: unlike **#14 THE "
 "PATRON** it is INVERTED - no government funds JPMorganChase, one withholds permission to deploy its own "
 "capital; unlike **#17 THE PERMIT** the product is not at risk, the CAPITAL is; unlike **#26 THE MARKED "
 "BOOK** it shares the distinguishing feature (the company does not fail, the per-share compounding stops) "
 "but not the mechanism, because JPMorgan's earnings are collected in cash rather than standing as an "
 "unrealised fair-value write-up; and unlike **#10 THE CAMOUFLAGE** Corporate is not a weak leg burning a "
 "strong leg's cash - it is the same capital, undeployed. The arithmetic: $120.9bn, **35.3% of common "
 "equity**, earns about **3.7%** in Corporate because the filer's own sentence says excess capital *\"has "
 "been retained in Corporate\"*, while the three operating segments earn **18% (CIB, $149.5bn), 32% (CCB, "
 "$56.0bn) and 40% (AWM, $16.0bn)** - so the reported 17% ROE and 20% ROTCE are the average of a franchise "
 "and a Treasury bill. Each additional point of required CET1 on $1,981,692M of RWA moves $19,817M from "
 "the 18-40% businesses into the 3.7% one, about **$2.9bn a year of pre-tax income, 4.0% of 2025 pre-tax, "
 "per point** - and it runs both ways, Corporate's allocation falling to $98.4bn on 2026-01-01. **Tells "
 "checkable on any filer: a Corporate or Other segment holding a large share of equity at a return the "
 "filer itself marks \"NM\"; a capital requirement printed in the filing beside a higher actual ratio; a "
 "blended return on equity materially below EVERY operating segment's; and the filer's own sentence "
 "explaining that excess capital is retained in Corporate.** **NUMBERING: the table carried twenty-seven "
 "rows and a maximum number of 26 when this row was added (CCB and ACNB both took 25); this row is "
 "numbered 27, the next unused number, so the table now has twenty-eight rows and a maximum of 27. No "
 "prior row was renumbered. The operator's call.**")
m = re.search(r'\*\*All of the proposed shapes are listed so briefs count correctly; none is settled\.\*\*', t)
assert m, 'sentinel sentence not found'
t = t[:m.end()] + OPEN_ADD + t[m.end():]
open(SP, 'w', encoding='utf-8').write(t)
rows_after = len(re.findall(r'^\| \d+ \|', t, re.M))
sys.stdout.write('survival-shape rows: %d -> %d\n' % (rows_before, rows_after))

# ---------- 3. narrative fold into the reading list ----------
RL = 'Screens/2026-08-31 PREPPED READING LIST (operator lists).md'
t = open(RL, encoding='utf-8').read()
FOLD = """

---
## JPM (JPMorgan Chase & Co.) - RUN 2026-09-19. ALL FOUR BUSINESS GATES IN; FAIL AT Q5 ON PRICE.
*The narrative fold. The register entry with the price, the share count, the cap, the sovereign and the
PASS/FAIL line is in `Screens/WATCHLIST RUN QUEUE.md`, entry 130. Run file:
`Test Runs/2026-09-19 Run - JPM JPMorgan Chase.md`.*

**THE FOURTH BANK THIS PROJECT HAS RUN, the SECOND to clear the business gates, and the largest company it
has ever priced** ($929,488M). WAVE 6, under the operator ruling of 2026-09-19 that the five banks are run.

**THE FINDINGS, in the order they mattered.**

**1. The first thing the run tested about the franchise, it refuted.** A bank's franchise is the price of
its money, and ACNB - the only bank to have passed Q2 before this run - passed on exactly that: a cost of
funds 64 basis points below the median of its own 56-bank market over five years. **JPMorganChase FAILS
that test. On one uniform specification across all six holding companies, from their own tagged annual
data, it is THIRD of six on the cost of total deposits in every one of five years** (five-year means:
Wells Fargo 0.927%, Bank of America 1.066%, **JPMorgan 1.202%**, Morgan Stanley 1.699%, Citigroup 1.902%,
Goldman Sachs 2.958%). The FDIC Call Reports confirm it independently at six dates: JPMorgan Chase Bank NA
is third of the four universal banks on cost of funding earning assets at every date, 21bp behind Bank of
America and 42bp behind Wells Fargo at 2025-12-31, and only **23.2% of its deposits pay nothing** against
27.5% at Bank of America and 27.3% at Wells Fargo. **The largest deposit franchise in America is not the
cheapest one.**

**2. So where the pass came from is a DIFFERENT form of [E2-58]'s single exception, and naming which form
is the general result.** *"a cost advantage that is both wide and sustainable … By definition such
exceptions are few."* JPMorgan's is on the **expense line**: a 52% overhead ratio against Bank of
America's 61.65%, Citigroup's 64.7% and Wells Fargo's 66%; five-year means 55.40 / 64.66 / 67.52 / 69.20;
**a 9.65-point gap on a $182,447M revenue base, about $17.6 billion a year of pre-tax income, and
WIDENING** (JPMorgan 59 to 52 while Bank of America went 67.03 to 61.65). Five-year mean ROTCE **20.80%,
first of six in four of five years**, with a worst year (18%) above every peer's best year but Morgan
Stanley's. **After four banks the usable rule is: [E3-03] criterion 2 is passable for a bank ONLY through
[E2-58]'s exception, and the exception has at least two independent forms - the price of the liability
(ACNB) and the cost of the platform (JPM). A bank with neither is OUT.**

**3. [E2-59] bites on a dated, quantified event and it is the 2023 acquisition.** JPMorgan Chase Bank NA
held **11.30% of all United States domestic insured deposits at 2022-12-31** on the FDIC's own numbers, so
the ordinary interstate-merger route to a $200bn bank was closed; what opened was an FDIC receivership
auction, and Note 34 records it: *"acquired certain assets and assumed certain liabilities of First
Republic Bank … from the Federal Deposit Insurance Corporation ('FDIC'), **as receiver**."* The
**$2,775 million after-tax bargain purchase gain was granted by the regime, not won from customers**, and
is scored that way rather than as moat evidence. The regime sent the bill too: a **$2.9 billion FDIC
special assessment** in 2023 expense.

**4. The refuted prior on deposit share, and it is the sharpest [E4-32] finding.** The run expected the
largest bank in America to be gaining share. **It is not. Domestic deposit share went 11.77% (2021), 11.30%,
11.68%, 11.44%, 11.67%, 11.65% (2026-06-30) - twelve basis points BELOW end-2021 after absorbing a
$92 billion deposit base.** Bank of America's fell 71bp over the same window, so JPMorgan won relatively;
but the franchise did not widen on the measure that matters most to it. Investment-banking fee wallet share
fell 9.1% to 8.4% and the loan-syndication rank slipped #1 to #2 globally and in the U.S.

**5. Q3 was the gate and the closest precedent on disk was AGAINST the company.**
`Framework/v4/VERIFICATION - the two cases that decide the deletions.md` rejects Citigroup at mid-2007 at
Q3 on its filed Legal Proceedings. JPMorganChase's record is long and bad in absolute terms: a **2015
GUILTY PLEA to federal antitrust**, a **2020 DOJ Deferred Prosecution Agreement** over precious-metals and
Treasuries spoofing, an EURIBOR infringement re-imposed in December 2023, a **$31.5M Indian
money-laundering fine**, the **$290M Epstein settlement**, and **NEW March 2024 OCC and Federal Reserve
consent orders over the completeness of trade-surveillance data - the SAME failure class as the 2020 DPA,
three and a half years later, which fires [E4-22]'s cockroach rule at full strength.**
**The gate was decided by an artifact the run NAMED and then WENT AND GOT from the issuing authority
rather than recalling: the Federal Reserve's own enforcement-actions file, all 2,889 actions.** Thirteen
entity actions against JPMorgan Chase & Co. since 2003, nine of them orders, **ZERO still open**, five
civil money penalties totalling **$878,932,500 - the largest of the six** - and the 2024-03-08 order
**terminated 2025-12-04, twenty-one months**. Run across the row: **Citigroup and Wells Fargo each still
have an OPEN order at the same date.** That is [E5-22]'s operative test - *"the failure that counts is they
didn't act when they learned"* - answered by the supervisor's own termination dates, and it is why this run
does not reach the Citigroup conclusion, which rested on LIVE matters. **A reader who scores $879 million
of central-bank penalties and a criminal antitrust plea as a disqualifier has a defensible reading and the
run file says so.**

**6. [E3-02] conformity, tested at the one moment in twenty years when it could be tested against a
control group that actually died.** At **2022-12-31**, before anything was public, from the FDIC Call
Reports of all seven institutions: **JPMorgan Chase Bank NA carried held-to-maturity securities at 1.40x
equity - the LOWEST of the seven - against Silicon Valley Bank's 5.91x, Bank of America's 2.81x, Wells
Fargo's 1.84x, First Republic's 1.63x and Citibank's 1.60x** - and the lowest assets-to-equity at 10.5x.
Its own filings put the HTM unrealized loss at $36,762M, **13.9% of common equity**; the same mark at
Silicon Valley Bank was of the order of its whole equity. **It did not imitate, and the peer it most
conspicuously did not imitate is Bank of America, whose ROTCE has since run 6.2 points below it.**

**7. [E2-50] reserves, and the answer is conservative by a wide margin.** Cumulative provision 2019-2025
**$54,408M against cumulative net charge-offs of $41,302M - 31.7% MORE reserved than lost** - with the
allowance covering the following year's charge-offs at **2.72x or better in every single year** and 10.76x
in 2020. **[E2-67] is met in SUBSTANCE and NOT in form: JPMorganChase publishes no reserving back-test,
and the one in the run file was built by the reader from the published series.** The one honest criticism
is the CB run's #23 THE CUSHION applied here: the **-$9,256M provision of 2021** is 15.5% of that year's
pre-tax income and the reason 2021 shows the window's best ROTCE of 23%.

**8. The segment answer to the brief's question, and it is the named death.** On the filer's own capital
allocation: **AWM 40% on $16.0bn, CCB 32% on $56.0bn, CIB 18% on $149.5bn - and Corporate about 3.7% on
$120.9bn, 35.3% of the common equity.** The filer says why in one sentence: *"Any capital that the Firm has
accumulated in excess of these current requirements … has been retained in Corporate."* **All three
operating segments earn far above any plausible cost of their allocated capital; a third of the equity
earns a bond return because the Federal Reserve requires 11.5% of $1,981,692M of RWA and the Firm holds
$288,469M, an excess of $60,574M.** That is **PROPOSED SHAPE #27 THE LICENCE**: each additional point of
required CET1 moves $19,817M from the 18-40% businesses into the 3.7% one, about $2.9bn a year pre-tax,
and the owner has no vote. Likelihood **LIKELY**, and it runs both ways - Corporate's allocation falls to
$98.4bn on 2026-01-01.

**9. Why it failed at Q5, and the one judgment the failure rests on.** Honest pre-tax expectancy
**7.54% at the bottom boundary [E5-34], 9.62% centred, 11.06% at the top**, against a 5.34% sovereign -
**above the bond by 2.2 to 4.3 points and below the ~10% floor**, the fifth name on this track to land in
that configuration after KO, CB, GFF and ACNB. Value range **~$200 to ~$340 a share against a $349.67
quote**; 3.08x tangible book; the **Screamer test [E4-01]** returns the third outcome, narrowly - above the
whole range. **THE STRONGEST FACT AGAINST THE VERDICT: on the record the business has DELIVERED, the price
clears the floor.** Diluted EPS compounded 6.85% a year 2021-2025 and tangible book per share 10.30% a
year 2020 to mid-2026, against the 3.24% to 5.46% of perpetual growth the quote requires. **The entire Q5
failure rests on one judgment - that the 82.5% rise in net interest income from $52,311M (2021) to
$95,443M (2025), on 52.3% of the revenue, was the federal funds rate and not the business, and cannot
happen again from the same starting point.** [E4-41] requires that break to be named and removed; the run
names it. **And the board bought 8.9 million shares at $317.28 in December 2025, inside the top quarter of
this run's optimistic case: the disagreement is one year of multiple expansion, not an order of
magnitude.**

**10. The LIVE CAPITAL-ALLOCATION FLAG, which binds position size and not the discount rate [E4-13].**
**$31,640M of buybacks in 2025 at 2.57x tangible book against $9,898M at 1.65x in 2023 - three times the
dollars at 1.6 times the price** - under a programme that states it *"does not establish specific price
targets or timetables"*, the exact inverse of **[E5-25]**'s standard of publishing both conditions as
numbers in advance. **[E5-24]**'s first law inverted: *"what is smart at one price is dumb at another."*
The counter-argument is strong and is stated in full at Q3: the alternative use is Corporate at 3.7%, and
a share bought at 2.57x tangible book in a 20%-ROTCE business returns about 7.8% on the cash - better than
3.7% and better than the bond. **The run's answer is that [E5-08] asks for a material DISCOUNT, and 7.8%
on cash spent is a fair price, not a discount.**
**And [E4-27]: the CEO's entire equity award is in PSUs paying maximum at ROTCE >= 18% and zero below 6%,
and the five-year buyback programme accounts for roughly 3.8 points of the reported 20% ROTCE.** Recorded
under **[E5-38]** as a fired flag and explicitly NOT as a venality finding.

**11. Two facts that belong in any future bank run because they are unusual.** **Zero net common shares
issued in five years** - the issued count is 4,104,933,895 in all six filings read, identical to the share,
while the outstanding count fell 12.8% and the $192 billion First Republic acquisition was paid in cash and
a note. And **[E3-48] answered in the company's favour**: the 2025 outlook printed in the FY2024 10-K
guided NII to ~$94.0bn, NII ex-Markets to ~$90.0bn, adjusted expense to ~$95.0bn and the Card charge-off
rate to ~3.60%; the outturn was **$95,443M, $92,591M, $95,640M and 3.31% - guided conservatively and beaten
on three of three measurable items.** The projections flag fires on the practice ([E5-30]: a guidance
culture is a ratchet, and two of the three metrics are non-GAAP) and is answered on the record.

**12. A METRIC-SWITCHING finding the reader loses by [E2-56].** JPMorganChase went from **FOUR reportable
segments to THREE** with effect from January 2024: **Commercial Banking - which the brief asked about as a
segment with its own filed return on equity - no longer exists as a reporting unit**, folded into a
$149.5bn CIB reporting a blended 18%. The switch was announced ahead with restated comparatives and a
named management change, and did not follow deterioration, so it is [E2-49]'s candor case - **but the
separate series a reader needed is gone.**

**TOOLING DEFECTS AND BRIEF DEFECTS FOUND.**
- **`tools/sources.py:_get()` still defaults to `WEB_UA` and `www.sec.gov/Archives` answers HTTP 403 -
  the THIRD confirmation in one day** (BLK, ACNB, JPM). Every primary fetch in this run passed
  `headers=SEC_UA`. It is a one-line fix: default to `SEC_UA` for any `sec.gov` host.
- **`tools/sources.py` has no helper for the two regulator endpoints that decided two gates today.**
  ACNB and JPM both hand-rolled them. Two functions - `call_report(cert, dates)` and
  `enforcement_actions(name)` - would get the same numbers sooner without adding a step, which is the test
  CLAUDE.md sets for tooling.
- **The evidence-ladder gap CCB reported is CLOSED for two of its three rungs.** The FDIC Call Report API
  and the Federal Reserve enforcement file are both one HTTP request from the issuing authority and both
  decided gates. **RECOMMENDATION: add one rung between "SEC EDGAR primary documents" and "company IR
  site" - *the prudential regulator's own published data for the sector*.** The rung still genuinely
  missing is the **OCC** register (`apps.occ.gov` returned HTTP 404 twice) and **NCUA Form 5300**.
- **BRIEF DEFECT 1: the brief says JPM is "the third bank this project has run." It is the FOURTH** - CCB,
  ACNB and SOFI all ran 2026-09-19. The count matters because the deliverable asked whether the banks now
  run have settled the Q2 question.
- **BRIEF DEFECT 2: the brief says "two banks have already met [E3-03] criterion 2 differently." Only ONE
  had** - ACNB. CCB's Q2 was OUT and SOFI's Q2 was OUT. JPMorgan is the second.
- **BRIEF DEFECT 3: the brief says "JPM is not in the WAVE 6 table" and instructs a strike "in the
  operator-ruling sentence and the excluded subsection." Both halves are wrong: JPM IS a row in the WAVE 6
  table (unlike CCB and ACNB), and it is NOT in the excluded subsection, which names only CCB, ACNB and
  SOFI.** The fold struck the table row itself and recorded the discrepancy beside the ruling rather than
  editing it out.
- **ONE ERROR OF MY OWN, corrected in an addendum rather than by editing history (operator rule 6):** Q1
  states Level 3 ASSETS are $76,139M and 21.5% of common equity. **That is the Level 3 LIABILITIES figure;
  Level 3 ASSETS are $33,732M, 9.5% of common equity.** The Q1 sentence is left visible, the correction is
  at the head of Q4, and every subsequent calculation uses the corrected figures.
"""
t = t.rstrip('\n') + FOLD
open(RL, 'w', encoding='utf-8').write(t)
sys.stdout.write('reading-list fold appended: %s\n' % ('## JPM (JPMorgan Chase & Co.) - RUN 2026-09-19' in t))
