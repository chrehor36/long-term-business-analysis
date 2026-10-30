# -*- coding: utf-8 -*-
import io
P = "Screens/2026-08-31 PREPPED READING LIST (operator lists).md"
t = io.open(P, encoding='utf-8').read()
assert 'IIIN' not in t or 'Insteel' not in t
body = '''
## UPDATE 2026-09-21 - IIIN (Insteel Industries Inc.): Q1 IN, Q2 OUT on the business. Wave 7, name 20; register entry 152.

**Run file:** `Test Runs/2026-09-21 Run - IIIN Insteel Industries.md` (1,027 lines).
**Research:** `Test Runs/_research 2026-09-21 IIIN/` (the FY2025 10-K and six earlier 10-Ks -
FY2024, FY2023, FY2022, FY2021, FY2019, FY2016 - the Q3 FY2026 10-Q, the 2026 proxy, six 8-K
EX-99.1 exhibits, the companyfacts file, three peer companyfacts files, Nucor's FY2025 10-K
text, and the raw price JSON).
**Step 0.** Sovereign **USD 30-year 5.34% at 09/18/2026**, struck fresh from the **US Treasury
daily par yield curve** (issuing authority; FRED DGS30 not used, and the brief withheld a rate
deliberately). Price **$29.66**, close of 2026-09-18, Yahoo chart endpoint, flagged aggregator,
raw response saved. Shares **19,358,247, a single class of "Common Stock (No Par Value)"**,
cover of the 10-Q for the quarterly period ended 2026-06-27, accession
**`0001437749-26-023682`**, as of 2026-07-15; `split_factor_after` 1.0. **Cap, hand-struck:
$574.2M** against the screen's **$588M** - **-2.4%, a price-date difference, and the screen's
cap survives.** Anchor filing **10-K FY2025, `0001437749-25-031597`**, filed 2025-10-23; three
hand cross-checks (FY2025 operating cash **$27,163k**, equity recomputed from A-L at
**$371,532k**, FY2025 net sales **$647,706k** against the MD&A's own 22.4%).
**FY2026 had not closed** - the year ends 2026-10-03 - so no FY2026 10-K exists and both screen
dates are right.

## THE FINDING OF THE RUN: the five-year window is 59% one year, and that year's cash was inventory

The screen published **$40M-$57M** of owner earnings. **It reproduces exactly** - the 3- and
5-year means at the two ends of (c) are $39.7M, $42.7M, $53.5M and $57.2M - and it is the wrong
answer. Rebuilt by hand over **every filed year the data supports, FY2010 to FY2025**, owner
earnings average **$24.1M at the D&A end and $24.0M at the capex end**. The published band's
midpoint is **more than twice** the sixteen-year mean.

The mechanism is one year. **FY2023 alone is 59.2% of the five-year window's owner earnings**,
and **FY2023's cash was not earnings**: the filed cash-flow statement shows working capital
*providing* **$97.6M of the year's $142.2M** of operating cash, **68.6%**, of which **$94.3M was
the inventory line alone**, unwinding the **$118.6M** build of FY2022 as steel prices fell. Strip
the swing and FY2023's owner earnings are about **$29M, not $126M**.

And the trailing twelve months to 2026-06-27 - FY2025 less nine months of FY2025 plus nine months
of FY2026 - are **negative at both ends: -$20.5M and -$13.3M.** No annual-only screen can see it.
**The combined range is -$20.5M to $57.2M, which is [E4-25]'s too-wide-to-conclude on its own,
independently of the Q2 verdict.**

## What the run found

**Q1 IN.** One arithmetic line: tons shipped x (price per ton less rod cost per ton), less
conversion cost and freight. The filing writes the same equation. **The scarce input is not
owned** - the rod is bought, 27% of it imported in FY2025 - and what Insteel holds is freight
geometry, eleven owned plants near the customers.

**Q2 OUT, at [E3-03] criterion 2, on the registrant's own Item 1.** *"Our markets are highly
competitive based on price, quality and service."* Six named direct rivals plus import
competition, and the flagship engineered structural mesh is sold as *"a lower cost reinforcing
solution than hot-rolled rebar"* - the product is itself the substitute for something else, and
substitution runs both ways.

**[E2-58] supplies the class and its one exception is refuted by the same page.** Strategy states
*"operating as the lowest cost producer in our industry"*; Item 1 states that the largest rivals
*"are vertically integrated companies that produce both wire rod and concrete reinforcing
products"*. **Wire rod is not a component of the cost, it is 85.6% of it** (FY2025 cost of sales
$554,268k on net sales $647,706k). The rivals own the input; Insteel buys it.

**[E2-59] supplies the regime, and this is the sharpest thing in the file.** The 10-K says four
times, once after each trade petition, that duties *"had the effect of limiting the participation
of these countries in the domestic market"*, and the risk factors concede *"Trade law enforcement
is critical to our ability to maintain our competitive position against foreign PC strand and
SWWR producers"*. Whatever floor exists under PC strand and standard welded wire pricing is
**administered by the Department of Commerce**. **And the regime leaks**: with duties in force
against five countries since 2003, China since 2010 and fifteen more since 2021, **FY2024's price
decline is attributed in the MD&A to "the impact of low-priced PC strand" imports**, and FY2019's
shipments fell because of *"an increase in low-priced import competition spurred by the Section
232 tariff on imported steel"* - a measure meant to help the industry raised Insteel's rod cost
and let finished imports in underneath it.

**The competitor row: 7 named by the subject, 1 obtainable and unsegmented.** Wire Mesh
Corporation, Concrete Reinforcements, National Wire Products, Davis Wire, Oklahoma Steel & Wire
and Sumiden Wire all return *"No matching companies"* on EDGAR company search; all disclosed
UNOBTAINABLE rather than smoothed. Net income on year-end equity, FY2010-FY2025, identical
construction from each filer's own 10-K facts: **STLD 17.7% / NUE 14.6% / IIIN 9.9% / CMC 8.9%.**
**Insteel earns the lowest of the four while carrying no debt at all** - the row is run in the
subject's favour and still refutes the cost-advantage claim. Cross-checked against Nucor's own
FY2025 MD&A statement (*"Return on average stockholders' equity was 8.5% and 9.8% in 2025 and
2024"*) against the row's 8.3% and 10.0%: average-equity versus year-end-equity, nothing else.

**And the company publishes its own commodity record.** The 2026 proxy prints fifteen years of
return on capital under its incentive plan: 5.1, 1.4, 7.7, 10.4, 11.1, 23.1, 12.5, 16.6, 1.8,
9.7, **36.9, 47.6**, 9.1, 6.3, 14.1 per cent. **Mean 14.2%; strip the two steel-spike years and
the other thirteen average 9.9%, with three under 2%.** That is [E2-58]'s *"ratio of supply-tight
to supply-ample years"* rendered as a table by the compensation committee.

## Priors refuted, in both directions

- **REFUTED - the `wc_note`'s DIRECTION, for the second time in four cycles.** The arithmetic is
  right (19,260 / 27,163 = **70.9%**). The direction is inverted: the MD&A says *"**Working
  capital used $37.6 million of cash** due to a $36.5 million increase in inventories and a $20.4
  million increase in accounts receivable **partially offset by** a $19.3 million increase in
  accounts payable and accrued expenses."* **The payable did not make the cash; it softened the
  loss of it.** Net working-capital block FY2025: **-$35.7M, -131% of operating cash.** This is
  the BELFB failure repeated on a different filer, so it is no longer a one-off.
- **CONFIRMED and worse than stated - `spread_caveat` and `window_disagree`.** The instruction to
  rebuild was right, and obeying it moved the answer from $40-57M to $24M.
- **CONFIRMED - `level_note` STEP UP, ratio 2.13, and the year is identified.** Recent 3 =
  $75.9M, earlier 6 = $35.5M on the 9-year operating-cash series, which reproduces 2.13 exactly.
  The step is **[E3-51]**'s surfing wave: the 2021-22 steel price spike, which lifted selling
  prices 25.7% and then 51.9% **while tons fell 0.6% and then 7.8%**.
- **CONFIRMED but understated - `best_year_dep` 0.238.** Correct on the 9-year operating-cash
  series. On the series the framework actually values, **FY2023 is 59.2% of the five-year
  window**, not 23.8%.
- **EXPLAINED - `flags_disagree`.** The operating-cash series' early half has a positive mean so
  the guard waves it through at 2.13; the owner-earnings series' early half straddles zero
  (FY2022 at **-$12.66M**, which is the note's *"$-12.7M"* exactly) so the guard refuses.
  **The refusing series is the right one.** Operating cash hides the sign changes that netting
  capex reveals.
- **CONFIRMED - `acq_note`, and the perimeter is worse than the note implies.** $72.1M, **12.6%**
  of the hand cap: EWP $67.0M (2024-10-21) and OWP $5.1M (2024-11-26), both all cash. The 10-K
  says *"the presentation of EWP's earnings is impracticable for 2025"*, so the only quantification
  that exists is the pro forma - and it says the acquisition would have **reduced FY2024 net
  earnings by $1.8M on $93.3M of extra sales**. $25.9M of the price became goodwill.
- **REFUTED - my own [E2-49] metric-withdrawal prior. The count stays at six fires and six
  failures.** Return on capital has been the sole annual-incentive metric for at least fifteen
  years, the proxy publishes the entire series including **0.0% payouts in 2011, 2012 and 2019 and
  29.0% in 2024**, and states *"we do not apply subjective factors to adjust compensation during
  periods where our failure to meet our return on capital targets may be due to factors outside
  the control of our executive officers."* The CEO's non-equity incentive went **$654,500 (2023)
  -> $204,673 (2024) -> $1,500,000 (2025)**. **Publishing your own worst readings is the
  [E2-67] positive pole.**
- **REFUTED - the [E4-29] EBITDA prior, and it was tested in the right place.** Following the
  CGNX rule, the four quarterly 8-K EX-99.1 releases were pulled before scoring. *"EBITDA"*,
  *"non-GAAP"* and *"adjusted earnings"* appear **zero times** in the 10-K, the 10-Q, the proxy
  and **all six 8-K exhibits**, and **no numeric earnings, EPS, margin or growth guidance exists
  in any release**. The only forward number is capital spending. On a capital-intensive filer
  that is the honest choice at the point of maximum temptation **[E5-41]**.
- **NEW, and not in the screen row at all: a post-balance-sheet event.** On **2026-08-21**
  Insteel announced the closure of **Upper Sandusky, Ohio**, *"restructuring charges of
  approximately $4.6 million"*, *"the elimination of up to 65 positions"*, and - the line that
  matters for [E2-58] - that the remaining plants *"have ample open capacity to accommodate
  additional volumes"*. **Upper Sandusky and Warren were the two plants the FY2025 acquisition
  bought. Both are now closed within twenty-two months.** The logic is coherent consolidation;
  it is also the subject's own testimony to industry over-capacity.

## Tooling defects found - reported, not patched (three, plus two documentation findings)

1. **`WC_TAGS` contains no inventory tag and no receivables tag.** All four entries are liability
   lines. **A working-capital flag that cannot see inventories is blind to every inventory-cycle
   business there is.** Insteel tags `IncreaseDecreaseInInventories` and
   `IncreaseDecreaseInAccountsReceivable` in every filed year, so the data was present and the
   test did not ask for it. On this name **the line it cannot see is the one that carries the
   entire published band.** Same defect class as the four prior iterations of `level_shift`'s
   guard: the test reads one side of the series and the defect lives on the other.
2. **`working_capital_flag()` reports only the single largest line and stops.** FY2025's payable
   at 70.9% outranked FY2023's inventory release at 66.3%, so only the payable printed - **and
   the payable was an offset while the inventory release was the substance.** Reporting the
   maximum is not reporting the material one.
3. **The direction defect is now confirmed twice.** The note's sentence *"ONE LINE MADE THE CASH"*
   asserts a direction the function never computes: it takes `abs(v)/abs(o)` and then prints a
   directional claim. BELFB found it; IIIN reproduces it on a different filer and a different
   line. **Two runs, two inversions.**
4. **Documentation: `principle_ledger.csv` holds 311 rows, not 267.** `CLAUDE.md`'s key-files
   table and every brief still say 267. Traced: **267** at `9d38c16`, **286** at `b7e84ca`,
   **311** at `0eaeadd`, the last two both dated 2026-09-20, with the pointer never updated.
   **Counted from the file, as the standing instruction says to. Reported, not edited: `CLAUDE.md`
   is the operator's document.**
5. **Documentation: `Framework/THE FRAMEWORK v4.md` smooths a transcript artifact in [E4-46].**
   The framework prints *"we're not going to learn enough in the **following** five months"*; the
   ledger row reads *"the **followings** five months"*, and the framework also drops a
   *"You know,"*. **PRIME RULE 1 says flag artifacts and never smooth them; PRIME RULE 2 says the
   corpus wins.** The run file quotes the row and flags the artifact. **Reported, not edited: a
   governing document is not amended to match a run.**

## The (c) judgment, and why both ends agree here

**(c) is a disclosed guess [E2-09], and the guess is $15-18M a year, the D&A end.** The reason is
measured rather than asserted: **over FY2010-FY2025, D&A averaged $12.39M and capital expenditure
averaged $12.48M, a ratio of 1.01.** Sixteen years of the two lines matching to one per cent puts
Insteel visibly inside **[E2-41]**'s *"95% of American businesses"*, and it is why the two
owner-earnings ends converge on the long window ($24.1M vs $24.0M) and diverge only on short ones.
**[E5-20]**'s exception class was argued and rejected with reasons: the risk factors do say *"Our
operations are capital intensive and require substantial recurring expenditures for the routine
maintenance"*, but the MD&A says the spending is *"focused on cost and productivity improvement
initiatives in addition to recurring maintenance requirements"* and, decisively, *"Our investing
activities are largely discretionary"*, which is the opposite of a railroad's position.

## No price band, and the reversal condition in words

**Q2 OUT is a finding about the business, so no alert is armed and no `PORTFOLIO.md` row is
added** - the QLYS ruling, and **[E5-35]**: *"You can turn any investment into a bad deal by
paying too much. What you can't do is turn any investment into a good deal by paying little."*
The file reopens only on filed evidence of: **(1)** a structural, not cyclical, removal of
industry over-capacity, such that *"ample open capacity"* stops being true industry-wide;
**(2)** a fiscal year of flat or falling shipments in which **average selling prices rise**,
which is **[E2-44]**'s test and which FY2024 filed the counter-example to; **(3)** three
consecutive years of organic tonnage growth with the MD&A separating organic from acquired tons
**[E4-55]**; or **(4)** backward integration into wire rod, the only visible route to
**[E2-58]**'s *"cost advantage that is both wide and sustainable"* - and itself a new business
needing its own run. **None of these is a price.**

## The uncomfortable part, written down rather than hedged

**This is a well-run company and the run says so.** Zero debt at every date read, thirty-five
years of one CEO, a formulaic incentive on return on capital that pays nothing in bad years and
publishes those years, no EBITDA anywhere, no earnings guidance anywhere, restructuring costs
quantified line by line, and a pro forma published that makes its own acquisition look worse.
**The retention test [E3-54] even passes on the corpus's own five-year window** - **$3.89 of
market value per $1 retained** to the FY2025 close, **$2.12** to 2026-09-18. **Both other windows
were published too, because [E4-38] forbids choosing one: on FY2017-FY2025 the same test returns
$0.46 and -$0.88.** The five-year window starts at the October 2020 trough and the nine-year one
at a 2016 peak, which is exactly the artifact [E4-38] names, and the honest reading is that the
test measures the steel cycle here rather than the allocator.

**None of that is a franchise, and [E2-37] is the sentence that governs:** *"a textile company
that allocates capital brilliantly within its industry is a remarkable textile company - but not
a remarkable business."* **A good jockey does not repair the horse [E2-38, E3-39].** The Q2
verdict is about the business and it is permanent; it is not a judgment about the people, and the
run says so in those terms.

**The one thing a reader should not take from this file:** the file does **not** say Insteel is
in danger. It has no debt, discretionary capex, and a seventeen-year record with no loss year
after 2009. The named death mechanism - quantified by the filer itself, *"a 10% increase in the
price of wire rod would have resulted in a $33.1 million decrease in our pre-tax earnings"*
against nine-month pre-tax earnings of **$28.1M**, which is **118% of them** - produces **bad
years, not death**. **This business is very hard to kill and quite easy to make worthless as a
compounder**, which is the Q2 finding arriving at Q4 by another road.

## Acceptance test
`python tools/check_framework.py` **PASS** before the fold commit (phantom citations 0 across
**1,121** test-run files; unlabelled numbers 0 in all five governing documents; ledger verbatim
OK). `tools/ledger_verbatim.py` not run separately: the ledger was not touched, and check 4 of
the acceptance test covers it. **Six quotations in the run file were corrected before the commit
on a check against `principle_ledger.csv`'s own `quote_verbatim` field rather than the
framework's rendering of it** - [E2-59], [E4-41], [E2-67], [E4-46], [E4-55] and [E3-03] - and
**two source artifacts are reproduced and flagged rather than smoothed**: the ledger's OCR damage
in [E4-55] (*doubled quote marks, a replacement character in "e?ect"*) and the spacing artifact
*"extra- legally"* in [E2-59]. **PRIME RULE 1: the framework's own compression of a quote is not
a licence to repeat it as a quote.**
'''
io.open(P, 'a', encoding='utf-8').write(body)
print("appended", len(body.split('\n')), "lines")
