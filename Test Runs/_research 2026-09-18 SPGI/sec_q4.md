
---
## Q4 — WILL IT SURVIVE?

### THE SKIP REASON, TESTED ON THE FILING RATHER THAN INHERITED

**The queue's wave-5 label for SPGI is "capex unresolved [E5-20]: build (c) by hand from the
filing."** Both halves were tested.

**(a) The label is a TOOLING ARTEFACT — the AMZN and CL kind, not the NVDA kind.** The XBRL tag
changed: `PaymentsToAcquirePropertyPlantAndEquipment` carries 10-K years **FY2007-FY2009 only**
(229.6 / 106.0 / 68.5) and stops; `PaymentsToAcquireProductiveAssets` carries **FY2008-FY2025**
unbroken. A reader following only the first tag sees S&P Global's capital spending end in 2009,
which is what `floor_screen.py` at `a8bc84f` did. **The union fix reaches every window — there is
NO early-year hole of the NVDA kind**, and the two tags overlap in FY2008-FY2009 rather than
leaving a gap.
**I ran it through the CURRENT `owner_earnings()` as the queue's dated notes instruct.** It
prices: `{'5y_da': 3115.0, '5y_capex': 3935.0, '3y_da': 3633.7, '3y_capex': 4644.7}` ($M). The
capex end is the *higher* one here, because capex is a small fraction of D&A — the reverse of the
usual shape, and the reason is purchase amortization.
**And the capex line never left the face of the statement:** *"Capital expenditures | ( 195 ) |
( 124 ) | ( 143 )"*, FY2025 10-K. **`da_annual()`'s defect found by the NVDA run does not bite
here**, because S&P Global reports *Depreciation* and *Amortization of intangibles* as two
separate lines and no combined total exists on the face to be replaced: 110 + 1,069 = 1,179, and
the tool returns 1,179.

**(b) THE D&A DISCONTINUITY IS THE MERGER, confirmed on the filing.** `da_discontinuity_flag()`
fires at 2022-12-31 (5.7x, $178M to $1,013M) and names three possible causes. **It is the first
one.** The filed statements show *Amortization of intangibles* at $96M (FY2021), **$905M
(FY2022)**, $1,042M, $1,077M, $1,069M, while *Depreciation* alone runs $82M / $108M / $101M /
$96M / $110M. The IHS Markit merger closed 2022-02-28 for $43.5bn, of which the FY2022 critical
audit matter identifies *"identified intangible assets of $18.6 billion"*. **Purchase accounting,
not a change of estimate and not a tag artefact.**

**(c) [E5-20] ASKED SEPARATELY, ON THE FILING, AND ANSWERED: NO.** S&P Global is not in the
capital-intensive exception class, and it is about as far from a railroad as a filer gets:
- **Total property and equipment, gross, is $1,139M** on $15,336M of revenue; **net $278M**.
  All long-lived assets *"including right of use assets, property and equipment, net and
  capitalized technology costs, net"* are **$873M**.
- **Capital expenditure has run 0.5% to 1.3% of revenue** for nine years.
- **Capex against depreciation, 2020-2025: $662M against $580M — 1.14x.** That is precisely
  **[E2-41]**'s *"capital expenditures that over time roughly approximate depreciation"* and
  **[E3-44]**'s default case. On continuing operations 2023-25 the ratio is higher, **$394M
  against $271M = 1.45x**, and both numbers are trivial.
- **[E4-47]'s inflation condition is NOT engaged** the way it was at Colgate: 61% of revenue is
  United States and *"We do not have operations in any foreign country that represent more than
  7% of our consolidated revenue"*, so there is no old-dollars depreciation problem.

**So the real (c) question here is not plant at all, and the label pointed at the wrong thing.**
The whole of the D&A band is **amortization of purchased intangibles**, and the question is
whether **buying companies** is what this business requires to fully maintain its position.
**Of the four names now run from this row: ABNB had a real presentation gap, AMZN had no gap,
NVDA had a tag gap plus a history gap, CL had a tag gap only — and SPGI has a tag gap only, with
a second question underneath it that the label does not describe.**

### OWNER EARNINGS — THE ONE NUMBER **[E2-23]**

**Built by hand from the filed cash-flow statements (`_research 2026-09-18 SPGI/oe.py`); never a
net-income proxy.** Construction, and every departure from the standing CONVENTION is disclosed:

> **owner earnings = cash provided by operating activities − stock-based compensation − (c)
> − distributions to noncontrolling interest holders**

- **The working-capital increment [E2-23] constraint 3 is inside operating cash flow**, from one
  audited line, as the CONVENTION provides.
- **THE ONE ADDITION TO THE CONVENTION, and it is correctness rather than conservatism: the
  distributions to noncontrolling interest holders are deducted** — $280M / $287M / $321M in
  2023-25, off the face of the financing section. **CME Group holds 27% of S&P Dow Jones
  Indices** and took **$322M of FY2025's $1,271M of Indices operating profit**; that cash is
  inside consolidated operating cash flow and never reaches an S&P Global shareholder. **[E3-04]**
  requires the look-through *addition* of undistributed investee earnings so the yield is not
  understated; the mirror case — a consolidated subsidiary with an outside owner — requires the
  *subtraction*, or the yield is overstated. The company's own free-cash-flow definition deducts
  the same line. **The figures without this deduction are shown too** (section D below), so the
  reader can see exactly what it costs: about $296M a year, or 7.8% of the mean.

**A. THE PERIMETER BEING PRICED — continuing operations, ex-Mobility, FY2023-FY2025 ($M)**

| year | continuing OCF | SBC | continuing capex | continuing D&A | NCI distributions | **OE, (c)=capex** | OE, (c)=D&A | OE, wc movement stripped |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2023 | 3,145 | 171 | 121 | 832 | 280 | **2,573** | 1,862 | 3,033 |
| 2024 | 5,092 | 247 | 106 | 858 | 287 | **4,452** | 3,700 | 4,217 |
| 2025 | 5,030 | 236 | 167 | 862 | 321 | **4,306** | 3,611 | 4,738 |
| **3-yr mean** | | | | | | **$3,777M** | **$3,058M** | $3,996M |

*Mobility is removed using the FILED Article 11 pro forma's discontinued-operations column
(operating profit $317M / $374M / $373M, plus its own D&A of $311M / $315M / $317M, less its own
tax of $63M / $92M / $69M) and its segment capital expenditure of $22M / $18M / $28M from Note 12.
**Two disclosed approximations, stated because they matter:** (i) Mobility's own working-capital
movement is not separately given, so the split of the consolidated working-capital line is
approximate; (ii) Mobility's SBC is left inside continuing, which overstates continuing operating
cash flow by roughly $26M while the full consolidated SBC deduction over-deducts by the same
amount — **the two cancel to within a rounding error** and neither is a judgment.*

**The CL instruction applied: reported with and without the working-capital movement.** Here it
runs the opposite way to Colgate's. Stripping the movement **raises** the mean from $3,777M to
$3,996M, because working capital was a **use** of cash in two of three years (−$460M in 2023,
+$235M in 2024, −$432M in 2025). **The as-filed figure is therefore the conservative one and it is
the one used.** The component worth naming: unearned revenue rose $352M / $222M / $327M — real
customer prepayment — while **receivables absorbed $291M / $79M / $600M, and days sales
outstanding rose from 74 to 82 in 2025.** That eight-day move is a Q6 monitoring item.
**`working_capital_flag()` returns `None`** — no single line moved more than 30% of a year's
operating cash — and I checked its stated annual-facts limitation against the 10-Qs rather than
trusting the null: H1 2026 operating cash was $2,476M against $2,398M a year earlier, with no
single line above $403M.

**B. THE [E2-42] FIVE-YEAR DEFAULT, FY2021-FY2025, consolidated AS FILED ($M)** — *published
because [E4-38] requires every window, and labelled because it measures a company that no longer
exists: it crosses the 2022-02-28 merger and it contains Mobility throughout.*

| 2021 | 2022 | 2023 | 2024 | 2025 | **5-yr mean** |
|---:|---:|---:|---:|---:|---:|
| 3,214 | 2,030 | 3,116 | 5,031 | 4,899 | **$3,658M**, (c) = capex |
| 3,071 | 1,106 | 2,116 | 3,982 | 3,915 | **$2,838M**, (c) = D&A |

**C. THE PRE-MERGER REFERENCE, FY2017-FY2021, legacy S&P Global on ONE perimeter ($M)**

| 2017 | 2018 | 2019 | 2020 | 2021 | **5-yr mean** |
|---:|---:|---:|---:|---:|---:|
| 1,683 | 1,703 | 2,440 | 3,207 | 3,214 | **$2,449M**, (c) = capex |

**D. WITHOUT the NCI deduction** (the bare CONVENTION), continuing 2023-25: 2,853 / 4,739 / 4,627,
mean **$4,073M**. The deduction costs $296M a year.

**E. TRAILING TWELVE MONTHS to 2026-06-30, continuing** (10-Q `0000064040-26-000045`):
consolidated OCF $5,729M, capex $156M, SBC $239M, NCI distributions $315M; Mobility removed at
$610M and $28M. **OE = $4,437M.** *A single twelve months, not a mean; it is an upper reference,
never the number.*

### (c) — THE DISCLOSED JUDGMENT, because Buffett says it must be a guess

**(c) is set at TOTAL CAPITAL EXPENDITURE.** Three grounds, all from the filing:
1. **Capex here is not just plant.** The MD&A's own definition: *"Capital expenditures include
   purchases of property and equipment **and additions to technology projects**."* The capitalised
   product development is already inside the number, which is what **[E2-23]**'s *"plant and
   equipment, **etc.**"* reaches for in a business like this one.
2. **Capex exceeds depreciation** (1.14x over 2020-25 consolidated, 1.45x over 2023-25
   continuing), so taking capex rather than depreciation is the conservative end on the plant.
3. **The D&A end is invalid in the opposite direction from the usual one.** Continuing D&A of
   $862M is $96M of depreciation and **$766M of amortization of intangibles bought in 2022**.
   Deducting it as (c) asserts that the whole purchased intangible base must be repurchased
   every eleven years to stand still. That is an assertion about acquisitions, not about plant,
   and it deserves to be tested rather than assumed.

**SO THE REAL QUESTION IS TESTED SEPARATELY: IS BUYING COMPANIES A MAINTENANCE REQUIREMENT?**

*Evidence that it is NOT (and this is where I land):*
- **The company's own organic disclosure.** FY2026 guidance: *"Organic, Constant Currency Revenue
  growth | 6.0% to 8.0%"* against reported revenue growth of *"5.9% to 7.9%"*. **Organic growth is
  guided at or above reported growth** — the position is not being held by purchase.
- **84% of continuing profit is earned by segments that buy essentially nothing.** FY2025
  amortization of intangibles from acquisitions by segment: **Ratings $6M, Indices $37M, Energy
  $130M** — $173M of the $766M. The remaining ~$593M sits in Market Intelligence.
- **The reference assets are not purchased and do not amortize.** The letter, the index and the
  assessment were built, not bought, and carry no intangible balance.

*Evidence that it IS, for the Market Intelligence leg, and it is real:*
- **$2,023M of acquisitions in FY2025** against $195M of capital expenditure, and Market
  Intelligence's revenue growth is repeatedly attributed to purchases — *"favorably impacted by
  the acquisition of Visible Alpha in May of 2024 and With Intelligence in November of 2025"*.

**THE RANGE, WHICH IS WHAT [E4-25] ASKS FOR RATHER THAN A RESOLUTION.** If the Market
Intelligence acquisition programme is maintenance rather than growth, (c) rises by the
acquisition run-rate and owner earnings fall:

| construction of (c) | 3-yr mean owner earnings |
|---|---:|
| total capital expenditure **(the judgment used)** | **$3,777M** |
| capex + the 2023-24 acquisition rate (~$300M/yr) | $3,477M |
| capex + the 3-yr mean acquisition spend (296 + 305 + 2,023)/3 = $875M/yr | **$2,902M** |
| continuing D&A (the mechanical D&A end) | **$3,058M** |

**Two independent routes to the low end land within $156M of each other — $2,902M and $3,058M —
which is the useful fact.** The combined range carried to Q5 is therefore **roughly $3,050M to
$3,800M**, with the trailing twelve months at $4,437M as an upper reference and the five-year
as-filed window at $3,658M sitting inside it on a different perimeter.

**Is that range too wide to reach a conclusion [E4-25]?** **No** — and it is worth saying why,
because the honest answer could have been yes. Top to bottom the range is 24%, and **every point
in it produces the same Q5 answer** (see Q5: the widest and narrowest constructions are 2.6% and
3.7% against a 5.29% sovereign). The range would only matter if it straddled the verdict, and it
does not.

**Stock compensation subtracted in full [E5-06]**: $171M / $247M / $236M, from the filed non-cash
block. **THE BA SBC CHECKLIST, RUN LINE BY LINE ON THE FILED BLOCK** — *"Depreciation",
"Amortization of intangibles", "Provision for losses on accounts receivable", "Deferred income
taxes", "Stock-based compensation", "(Gain) loss on dispositions, net", "Restructuring, lease
impairment charges and other"* — **there is no second equity-settled line.** The 401(k) and
retirement contributions are inside *"Accrued compensation and contributions to retirement
plans"* on the balance sheet and are cash; the pension is a $254M **asset**, overfunded, with
$178M of other post-retirement liability. **[E3-70]'s market-value measure is not applied and the
reason is stated:** SBC is **4.2% to 4.6% of operating cash flow** across 2023-25, so the gap between the charge and a grant-date market value cannot move any verdict here; the
reported charge is used as the floor it is. *(SBC ÷ consolidated operating cash flow: 4.6% in
2023, 4.3% in 2024, 4.2% in 2025.)*

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

**[x] GREAT — at the segment level, and the corporate-level qualification is stated rather than
buried.**

*Why great:* net tangible **operating** assets are **negative** (about −$2.2bn; see Q3), so growth
requires no incremental capital in the operations at all. FY2025 continuing owner earnings of
$4,306M were produced on $167M of capital expenditure and gross plant of $1,139M. It is
**[E2-44](b)** — *"grow dollar volume with only minor additional investment of capital"* — in its
purest available form, and **[E5-41]**'s inversion runs the right way: customers prepay $4,088M
of unearned revenue, so this is float rather than reverse float.

*The qualification, and it is [E2-56] again:* at the **corporate** level the growth was bought.
Owner earnings per diluted share, on comparable perimeters:

| | FY2017 | FY2019 | FY2021 *(legacy, no Mobility, no IHS Markit)* | FY2023 | FY2024 | FY2025 *(continuing, no Mobility)* |
|---|---:|---:|---:|---:|---:|---:|
| owner earnings, $M | 1,683 | 2,440 | **3,214** | 2,573 | 4,452 | **4,306** |
| diluted shares, M | 258.9 | 246.9 | **241.8** | 318.9 | 311.9 | **305.1** |
| **OE per diluted share** | $6.50 | $9.88 | **$13.29** | $8.07 | $14.27 | **$14.11** |

**Read the two bold columns together.** Both are the company without Mobility. **Four years and
$43.5 billion of stock after the merger, owner earnings per share is $14.11 against $13.29 — a
total gain of 6.2%, or about 1.5% a year.** Dollars of owner earnings rose 34%; the share count
rose 26%.
**The fair caveats, stated because the comparison is doing a lot of work:** FY2021 capital
expenditure was abnormally low at $35M (normalising it to $100M gives $13.02 a share, which does
not change the conclusion); and FY2021 was a strong issuance year while FY2023 was a weak one.
**The cleaner rate, mid-cycle to boom, is FY2019 to FY2025 continuing: $9.88 to $14.11, +6.1% a
year** — and because it runs from a mid-cycle year *to* a boom year, the underlying rate is
**below** 6.1%. That is the growth number Q5 uses, and it is used at face value rather than
shaded, so that the windage stays spent once.

### STAYING POWER — score all three **[E5-11]**

**(1) A large and reliable stream of earnings — PASS, comfortably.** Operating cash flow has not
been below **$2,016M** in nine filed years and never negative; **79% of FY2025 revenue was
recognised over time** ($12,192M of $15,336M); unearned revenue of $4,088M is next year's revenue
already collected. Even in FY2022, the worst year in the window — merger costs, divestiture taxes
and a bond-market shutdown together — operating cash flow was $2,603M.

**(2) MASSIVE LIQUID ASSETS — FAIL, and it is recorded rather than argued around.** Cash was
**$1,745M at 2025-12-31** against **$13,088M of total debt**; the pro forma post-spin balance
sheet shows **$3,663M** at 2026-03-31 after the $1.974bn Mobility distribution, and the company
has announced it will spend *"more than $7 billion"* on repurchases in 2026. The filing points at
a facility rather than at cash: *"We have the ability to borrow a total of $2.0 billion through
our commercial paper program, **which is supported by our $2.0 billion five-year credit
agreement**"*, with **$825 million of commercial paper outstanding at 2026-06-30**. Commercial
paper is exactly **[E5-39]**'s *kindness of strangers* — it is the funding that disappears in the
week you need it. **Scored FAIL, on the same reading the CL run gave Colgate.**

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — PASS, with one named exception the filing
itself declines to schedule.** Debt matures **$3M in 2026, $1.7bn in 2027, $784M in 2028, $2.7bn
in 2029, $596M in 2030 and $6.5bn thereafter**, against $5.1bn of annual free cash flow; the fair
value of the debt is **$11.3bn against $13.1bn of book**, so the fixed coupons are worth less than
par at today's rates. The AWS commitment is *"a purchase obligation of $1.0 billion … over a
five-year period"*. **The exception:**
> *"after December 31, 2017, **CME Group and CME Group Index Services LLC ('CGIS') has the right
> at any time to sell, and we are obligated to buy, at least 20% of their share in S&P Dow Jones
> Indices LLC**. **We have excluded this amount from our contractual obligations table** because
> we are uncertain as to the timing and the ultimate amount of the potential payment we may be
> required to make."*

**A $4,914M put, exercisable at the counterparty's option at any time, deliberately left out of
the obligations table.** That is [E5-11]'s third strength in its literal form — *"Ignoring that
last necessity is what usually leads companies to experience unexpected problems"* — and the
filing says, in terms, that it is ignoring it. It is **affordable** (one year's free cash flow,
and the minimum tranche is nearer $1.0bn), which is why this is a pass rather than a fail; but it
is exercisable in exactly the market where S&P's own cash flow would be weakest, and **[E2-55]**
says score the worst case.

**[E5-11] SCORES 2 OF 3.**

**[E2-54] the coverage test:** interest paid in FY2025 was **$390M** against operating cash flow
of $5,651M **net of ample capital expenditure** ($195M) — **14.0x**. Accrued interest is not
material beyond the paid figure. **Leverage, named and quantified [E4-16, E3-29]:** total debt
$13,088M, 2.5x free cash flow; net debt post-spin about $9.7bn; the single financial covenant is
*"indebtedness to cash flow … not greater than 4 to 1, and this ratio has never been exceeded."*
**[E3-52]'s question — read the terms, not the quantity:** $4,088M of unearned revenue is
covenant-free, due-date-free, customer-prepaid funding; $13.1bn of senior notes are long-dated
and unsecured with no maintenance covenants named beyond the facility's.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**Not insolvency. The mechanism is the withdrawal of the requirement to hold the letter.**

**The bear case, stated as well as its holders would state it [E4-51].** S&P Global Ratings does
not sell information; information about credit is free and getting freer. It sells **admission**.
An issuer buys the letter because other people's documents demand it — a pension fund's mandate,
a bank's capital calculation, an insurer's reserve rules, an index's eligibility screen. **None of
those documents is written by S&P Global, and the largest author of them is the state.** The
FY2025 10-K concedes the exposure in its own words: legislators continue to consider *"provisions
seeking to **reduce regulatory and investor reliance on credit ratings**"*, *"provisions regarding
**remuneration** and rotation of credit rating agencies"*, and governments *"may from time to time
establish **official rating agencies**"*. **[E2-59]** is exact about what class that puts the
business in: a regime can floor a business's profits, *"but that day is gone"* is how such
arrangements end, and the moat belongs to the regime rather than to the firm. Meanwhile the
borrowing itself is migrating: the fastest-growing part of corporate credit is private and
bilateral, where the lender does its own work and buys no letter at all — the 10-K lists *"private
market opportunities"* as a Ratings *growth* initiative, which is the company conceding that the
public-issuance base is not where the growth is.

**Quantified from filed figures.** Ratings is **$3,013M of $6,218M** of continuing segment
operating profit, on **$4,724M of revenue** of which **$2,470M is transaction** (tied to new
issuance) and **$2,254M non-transaction** (tied to the stock of ratings outstanding). The
incremental margin on rating fees is close to 100% — the segment's assets are $1,137M and its
capital expenditure is $64M — so revenue lost is profit lost almost dollar for dollar.
- **Scenario 1, fee compression from mandated remuneration rules or a third rating becoming
  standard: −20% of Ratings revenue = −$945M of operating profit, −15.2% of continuing segment
  profit.** Owner earnings fall from about $3,777M to about $3,050M, and the yield at today's
  price from 3.17% to 2.56%.
- **Scenario 2, the deeper one — a 30% reduction in the *stock* of rated debt over a decade as
  reliance is withdrawn and private credit takes share: −30% of both revenue legs = −$1,417M**,
  **−22.8% of continuing segment profit**; owner earnings fall to about **$2,690M** and the yield
  to **2.26%**.
- **Scenario 3, the one the balance sheet feels: Market Intelligence's data products are
  commoditised by general-purpose AI.** That segment carries **$31,234M of total assets** earning
  **$991M**. A write-down to the value of its cash earnings would be a non-cash charge in the
  order of **$20-26bn — 17% to 22% of today's market capitalisation** — alongside the loss of 16%
  of continuing profit. The 10-K names this exposure five separate times in its own risk factors.

**LIKELIHOOD: [x] a real possibility** for Scenario 1 within five years (it is already drafted
legislation in the European Union and the United Kingdom), **[ ] a low-level possibility** for
Scenario 2 within a decade, **[x] a real possibility** for Scenario 3 within a decade. **None of
them is insolvency**, and that is the point: this business does not die of a balance sheet. It
dies, if it dies, of somebody else deleting a sentence from a document.

**[E4-40] — exposure, not experience.** The temptation here is to read the 2015 stress test as
proof of immortality: the franchise took a $1.5bn hit for the worst ratings failure imaginable and
came back stronger. **That is experience.** The *exposure* is different in kind — 2015 was a
reputational failure in a regime that still required the letter. None of the three scenarios above
is a reputational failure; all three are the removal of the requirement. **A benign history of
surviving reputational disasters is "not only useless, but actually dangerous" as a guide to
surviving a regulatory one.**

**VERDICT: [x] IN** — the business survives. It has nine years of never-negative operating cash
flow, negative operating capital requirements, 14x interest coverage and no maturity wall. What
it does not have is massive liquid assets, and what it carries is a $4.9bn put it has excluded
from its own obligations table.
