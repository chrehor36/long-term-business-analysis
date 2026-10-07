
---

## UPDATE 2026-09-12 — BA (The Boeing Company): Q2 OUT, and the competitor row removed the industry as the explanation

**FAIL at Q2, on the business. Price $210.45 (2026-09-11 close), 790,370,020 shares off the 10-Q
cover for the period ended 2026-06-30 (acc `0001628280-26-050038`), cap $166,333M, sovereign 5.35%
(US Treasury 30-year daily par yield, 2026-09-11, struck fresh). `check_framework.py` PASS; 104
distinct ledger ids cited, zero phantom against the 267-row ledger.**
`Test Runs/2026-09-12 Run - BA Boeing.md`

**THE QUEUE CAP WAS RIGHT, FOR THE FIRST TIME IN NINE RUNS.** $165,440M against a re-struck
$166,333M — a 0.5% price-date difference, not a count error. Eight consecutive runs had found it
wrong; this one did not, and that is worth recording because it means the `cover_shares.py` +
fresh-price discipline is now catching the cases it was built for rather than papering over a
systematic fault. **The count is still the thing to watch on this name, for a different reason:**
790.4M today against 565.4M in FY2019, with **33.5-40.2 million more contracted for 2027-10-15**
on the mandatory conversion of the 6.00% Series A preferred, whose $5,750M liquidation preference
ranks ahead of the common.

### THE ONE FACT THAT CLOSED THE FILE, AND IT CAME FROM THE PEER ROW RATHER THAN THE SUBJECT

Same year, same demand environment, same supply chain, same regulators, the same aircraft
customers:

| FY2025, commercial aircraft | Airbus | Boeing BCA |
|---|---|---|
| **aircraft delivered** | **793** | **600** |
| **commercial operating result** | **+€5,470M (10.4%)** | **−$7,079M (−17.1%)** |
| whole-company owner earnings, this framework's construction | **+€3,721M / +€4,552M** | **−$2,303M / −$1,314M** *(−$3,833M / −$2,844M corrected — see the defect)* |
| **net cash / (net debt)** | **+€12,171M** | **($25,878M)** at 2026-06-30 |
| unit backlog | **8,754 aircraft** | ~6,130 undelivered firm orders |

**A 27-point margin gap on the same product in the same twelve months, and 32% more deliveries by
the company that made money.** [E3-61] warns that the competitor row shows position and cannot show
conduct — *"I think you'd have to know the people involved"* — and that warning is precisely what
makes this decisive. **It removes the environment as the explanation for seven consecutive years of
BCA operating losses (FY2019-FY2025).** Air traffic, fuel, tariffs, the supply chain and the cycle
all hit both airframers; one printed 10.4% and €12.2bn of net cash.

**[E2-53] is then the gate that fails, and it is the strongest reading of franchise in the corpus:**
*"Once dominant, the newspaper itself, not the marketplace, determines just how good or how bad the
paper will be. **Good or bad, it will prosper.**"* Boeing did not prosper, and the marketplace was
not the reason. **[E5-18] from the other side:** *"if it won't stand a little mismanagement it's not
much of a business"* — Boeing's did not stand it, going to six consecutive year-ends of negative
book equity (−$8,617M in 2019 to −$3,908M in 2024, and −$23,552M at 2024-09-30) and then raising
$23,832M from the market in two days of October 2024. **And [E4-23] is the hinge:** *"if a business
requires a superstar to produce great results, the business itself cannot be deemed great"* — the
peer row is the proof that it does.

Two more failures on the registrant's own words, both in one 10-K: **[E2-44]** — *"This market
environment has resulted in **intense pressures on pricing** and other competitive factors, and we
expect these pressures to **continue or intensify** in the coming years"*, said about BCA and again
about BGS, with the substitute conceded in the same MD&A (*"they offer competitive products and have
access to most of the same customers and suppliers"*). And **[E2-59] / [E3-03](3)** — *"Since the
737-9 door plug accident in January 2024, the 737 program **may only increase production rates
and/or implement new production lines with the concurrence of the FAA**."* Prices are not regulated;
**output is.** Regulation caps a franchise and floors a commodity business; neither creates the
class, and here it caps.

### TWO TOOLING DEFECTS, AND THE SECOND IS A NEW CLASS

**(1) The published spread is a WINDOW artifact and is nineteen times too narrow — the INTC finding
replicating on the same sub-class, five days later.** `oe_bottom -4,429 / oe_top -3,392` reproduce
to within $4M and **both ends sit at the capex end** (5y_capex −3,388 max, 3y_capex −4,426 min; the
two D&A constructions are interior at −3,563 and −4,076). The advertised $1,037M "spread" measures a
three-year-versus-five-year window difference and says nothing about the (c) judgment it is read as.
**Rebuilt over eleven windows × both ends: −$10,076M to +$9,324M, a $19,399M width.** Both members
of the STEP DOWN sub-class have now been run and both found this. The triage's *"a tight spread here
is not safety"* was right in substance and wrong about the spread, twice.

**(2) THE 401(k)-IN-STOCK DEFECT. SBC THAT RESOLVES CAN STILL BE INCOMPLETE, AND NO XBRL-SIDE GUARD
CAN DETECT THAT.** This is the BE SBC-of-zero finding in a place the BE fix cannot reach, and it is
worse in one respect: the BE case failed loudly once guarded, and this one cannot be made to fail at
all from tagged data. Boeing's consolidated cash-flow statement carries **two** equity-settled
compensation add-backs:

> **Share-based plans expense** — 426 / 407 / 690
> **Treasury shares issued for 401(k) contribution** — **1,530 / 1,601 / 1,515**
> *(FY2025 / FY2024 / FY2023, FY2025 10-K, Consolidated Statements of Cash Flows)*

The second is the employee retirement match **paid in shares instead of cash**, added back to
operating cash flow exactly as SBC is. `StockIssuedDuringPeriodValueEmployeeBenefitPlan` resolves
for **FY2010-12 and FY2020 only**; from FY2021 the number exists **solely in the filed statement**.
The filed series: **$195M (FY2020) · $1,233M · $1,215M · $1,515M · $1,601M · $1,530M (FY2025) ·
$855M (H1 2026)**. [E5-06] is unambiguous and [E3-70] is stricter still, so **total equity-settled
compensation was $1,956M in FY2025 against $1,065M of operating cash flow — 184%** — and the screen
subtracted $426M of it. The correction moves FY2025 owner earnings from −$1,314M/−$2,303M to
−$2,844M/−$3,833M and flips FY2022 from positive to roughly zero.

**No code change was made, and that is the finding rather than a shortfall.** The BE fix works
because a tag returning *nothing* is detectable; a tag returning *part of the truth* is not. A
refusal rule keyed on "capex exceeds SBC by more than X" would produce false negatives across the
whole queue. **What went into `Screens/floor_screen.py` is a documented note naming the class, the
Boeing instance, and the only remedy there is: read the cash-flow statement's non-cash block, every
line of it, and do not assume `ShareBasedCompensation` is the whole of equity-settled pay.** The
same exposure exists wherever a filer pays benefits in stock — Boeing also settled **pension**
contributions in shares ($3,000M / $2,048M / $952M in FY2020/21/22), which this run left out as a
conservatism against its own conclusion.

### THE YEARS CHOSEN, AND WHY THIS RANGE IS NARROW IN THE ONLY SENSE THAT MATTERS

The brief warned there was *"no stable multi-year owner-earnings figure here at all"*: **true of the
full history, and refuted for the business that exists now.** FY2019 is a **dated structural break**
rather than a matter of taste — the worldwide 737 MAX grounding of 2019-03-13 — and across that line
seven things changed and none changed back: BCA went from profit every year to loss every year; the
FAA acquired a veto over the 737 rate; debt went $13,847M → $54,098M; interest $475M → $2,771M;
weighted-average shares 579.2M → 759.8M; and the 401(k) match went from cash to stock. **Every
window is published per [E4-38]; the mean is not taken across the break.**

| the business that exists now | capex end | D&A end |
|---|---|---|
| FY2019-2025 (7y, the whole post-grounding era) | **−$6,955M** | −$7,277M |
| FY2021-2025 (5y, the corpus default window) | **−$4,807M** | −$4,981M |
| FY2022-2025 (4y) | **−$4,393M** | −$4,320M |
| FY2024-2025 (2y, post-door-plug) | **−$10,076M** | −$9,384M |
| **TTM to 2026-06-30** | **−$2,238M** | −$585M |
| *pre-break, a different company: FY2014-2018* | *+$9,129M* | *+$9,324M* |

**Range for the business that exists now: −$10,076M to −$4,320M — negative on every window, both
(c) ends, and the trailing twelve months.** [E4-25]'s *"too wide to reach a conclusion"* applies to
the full range and **not** to the post-break one, which is the entire value of dating the break.
**The D&A end is INVALID under [E5-20] for a reason more specific than capital intensity:** capex is
1.51× depreciation in FY2025 and 1.72× in H1 2026, and Boeing's real renewal spending is not on the
capex line at all — it runs through R&D ($3,180M) and through ~$31.2bn of capitalised deferred
production costs and tooling sitting in inventory. **The $1,953M depreciation charge contains nothing
for the eventual replacement of the 737.** Windage count: one.

### THE ANSWER TO THE QUESTION THE BRIEF ASKED: YES, THE CUSTOMERS ARE FUNDING THE OPERATING CASH

| $M | FY2023 | FY2024 | FY2025 | **H1 2026** |
|---|---|---|---|---|
| operating cash flow | 5,960 | (12,080) | 1,065 | **+1,185** |
| change in advances and progress billings | +3,365 | +4,069 | (723) | **+4,660** |
| change in accounts payable | +1,672 | (793) | +724 | **+1,381** |
| **OCF EXCLUDING BOTH LINES** | **+923** | **(15,356)** | **+1,064** | **(4,856)** |

**In the six months to 2026-06-30 Boeing reported +$1,185M of operating cash flow while taking
$6,041M of additional money from its customers and suppliers. Excluding those two lines the business
consumed $4,856M of cash in half a year.** Advances stand at **$64,059M**. The queue's `wc_note` is
confirmed exactly: accounts payable moved −$3,783M in FY2021 against operating cash flow of
−$3,416M, **111%**.

**[E3-52] read in both directions is the real finding.** Float and deferred taxes are *"liabilities
without covenants or due dates attached … the benefit of debt … but saddle us with none of its
drawbacks."* Customer advances share that covenant-free, long-dated **form** and differ in the one
way that matters: **they are discharged by building aircraft, and on the loss-making programmes the
cost of building exceeds the cash received. That is what a reach-forward loss IS. This is the inverse
of float** — money already spent, against an obligation costing more than the cash.

### A FOURTH SURVIVAL SHAPE, ADDED TO THE ORCL / ARM / BE SET

Boeing carries **both** of the first two and is also a fourth thing.

- **The ORCL feature (contracted not to stop) is present:** $15,229M of airplane financing
  commitments of which **$11,904M is to customers Boeing itself believes are below investment
  grade**, $6,711M of accrued *"Forward loss recognition"*, and $64,059M of advances discharged at a
  negative margin.
- **The ARM feature (earns nothing after paying its people) is present and WORSE than ARM's.** ARM's
  finding was stock compensation equal to 97% of operating cash flow over its whole listed life.
  **Boeing's equity-settled compensation was 184% of FY2025 operating cash flow — the highest ratio
  this queue has recorded.** Boeing pays its retirement match in stock.
- **The BE feature (too little filed history) is absent:** 18 years of filed annual history, nothing
  UNKNOWABLE for want of evidence.
- **THE FOURTH: THE CASH IS SPENT UNDOING PAST WORK.** ORCL's cash bought datacentre assets that
  might yet earn; ARM's went to the engineers who build the next architecture; BE's bought a factory
  with too little history to judge. **Boeing's goes to its own defects:** $14,891M of cumulative 777X
  reach-forward losses (launched 2013, first delivery now 2027, zero delivered), $964M on the 767,
  ~$5,000M of BDS fixed-price development losses in FY2024 alone, **$10,882M of adverse cumulative
  catch-up adjustments in three years**, $1,300M of abnormal production costs, $1,500M of cash
  concessions to 737 MAX customers, $443M of 737-9 customer considerations, $689M to the DOJ and the
  families, and $1,696M still accrued as concessions owed. **None of it builds anything.** The
  framework had no category for a business whose principal use of capital is remediation; it has one
  now.

### THE FLOOR STATEMENT, WHICH IS THE CLEANEST IN THE QUEUE

A negative numerator has no growth rate, so the question inverts into dollars. **Boeing must earn
$8,899M of owner earnings to yield the 5.35% sovereign at $210.45, and $16,633M to clear the ~10%
[E4-28] floor. The most it has EVER earned in eighteen filed years is $13,398M — FY2018, on 806
deliveries, 579M shares and $13,847M of debt. Repeat the best year in Boeing's history exactly and
the buyer today receives 8.05% — below the figure the corpus quits on; 7.79% on the full equity
claim including the preferred. The floor requires 24% more than the best year ever, on 31% more
shares.** A round-number value range was **refused rather than invented**, because there is no
positive owner-earnings value to state. Neither bar applies: the normal method needs a value and the
screamer test needs a conservative case, and the price sits above the whole range — [E4-01]'s third
outcome.

### THE TAIL-TRIAGE CORRECTION EARNED ITS KEEP ON THE FIRST RUN AFTER IT WAS WRITTEN

BA sat under **STEP DOWN** with *"a tight spread there is not safety"*. The brief passed that along
as *"a statement about the arithmetic"* and — correctly, per the correction inserted the same day —
told the run that **every gate was open**. That mattered: the brief's own expectation was that the
file would close at **Q4**, and it closed at **Q2**. The material that closed it — the peer row, the
FAA concurrence sentence, the registrant's own pricing-pressure language, the delivery series — all
sits in Q1 and Q2. **A brief or a label that had aimed the effort at Q4 would have produced a
correct verdict on the wrong gate, and the hard sequence would have been broken to get there.**

### PRIORS REFUTED

1. **"IN NARROW on the duopoly, and I want it attacked" — refuted, and by the peer row rather than
   by Boeing's numbers.** The duopoly IS a franchise; Airbus is the one holding it. That is a
   stronger and less comfortable finding than "the moat never existed."
2. **"Q4 is where I expect this to close" — refuted on location, confirmed on substance.** Q4 is
   indeed OUT (gruesome on [E4-20]'s literal words; [E2-54] coverage negative in three of four
   recent periods; [E5-11] strengths 1 and 3 failed), but Q2 fails first and the hard sequence puts
   the verdict there.
3. **"There is no stable multi-year owner-earnings figure here at all" — true of the full history,
   refuted for the business that exists now.**
4. **The queue cap being wrong for a ninth time — refuted.** It was right.

### THE STRONGEST SINGLE FACT AGAINST THE VERDICT **[E4-51]**

**Airframe manufacturing is a thin-margin leg for everyone.** Lockheed Aeronautics **6.9%** (down
from 10.3% in FY2023, carrying a $950M classified reach-forward loss in FY2025), Northrop
Aeronautics Systems **6.3%** (a $477M B-21 LRIP loss provision), Pratt & Whitney **7.9%**, Embraer
Commercial Aviation **2.7%**. Where the peers earn 10%+ at company level they earn it on aftermarket
and electronics — RTX Collins 16.3%, HEICO Flight Support 24.1%, TransDigm 47.2%, Embraer Services
& Support 15.5% — **exactly the leg Boeing sold $10.55bn of in October 2025.** So the whole industry
takes reach-forward losses on new airframe programmes, and Boeing's are partly a genre feature
rather than purely a moat failure. **The verdict rests on the gap between a thin positive and a deep
negative: nobody else's airframe leg is at −17.1%, and the one direct comparable is at +10.4% on 32%
more deliveries in the same twelve months.** That reading is also why the file carries eight written
reversal conditions instead of being forgotten.

### DEFECTS IN THE BRIEF

Two, both small, and one is arguably a virtue. **(1) The brief asserted the run should "check that
SBC resolves for every year you use" — it does, for all 18 years, and the check passed while the
subtraction was still wrong by $1.5bn a year.** A resolution check is not a completeness check, and
the brief inherited that conflation from the BE fix. **(2) The brief said "Boeing has issued a great
many shares recently; the count is the first thing to get right," implying the queue's cap would be
wrong again.** It was right. Framing a prior as a near-certainty is the mirror of telling a run which
gate is boring — it invites the run to find what it was told to find. The brief's own instruction to
re-strike and verify is what caught it, so the protocol worked and only the framing was loaded.

**Count: 72 runs** — gate-clearers 26, Q2 OUT **43**, Q4 OUT 2, Q1 UNKNOWABLE 1.
