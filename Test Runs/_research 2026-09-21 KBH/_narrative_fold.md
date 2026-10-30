
## UPDATE 2026-09-21 — KBH (KB Home): Q1 IN, Q2 OUT on the business. Wave 7, name 14; register entry 146.

`Test Runs/2026-09-21 Run - KBH KB Home.md`. **Price $47.12 (close 2026-09-18, Yahoo chart
endpoint, flagged as an aggregator, raw JSON on disk). Shares 61,309,728 from the cover of the
10-Q for the quarter ended 2026-05-31, accession `0000795266-26-000063`. Cap struck by hand
$2,888.9M. Sovereign 5.34%, 2026-09-18, US Treasury daily par yield curve, 30-year, downloaded
in this run.** Acceptance test PASS before the commit.

### Why the gate closed, and it closed on the filer's own sentences

**[E3-03] criterion 2 fails in the FY2025 10-K's own Competition paragraph.** KB Home names
four substitute categories for its product: *"We **also compete for homebuyers against housing
alternatives to new homes, including resale homes, apartments, single-family rentals and other
rental housing**."* And it does not merely concede them, it prices against one of them as
stated strategy: the 2025 selling plan offers *"a compelling value **competitive with area
resale home prices**."* In the same paragraph, **selling price is named first** among the
factors that decide a sale. A business whose disclosed method of selling is to price
competitively against the second-hand version of its own product is not *"thought by its
customers to have no close substitute."*

That reduces the whole Q2 case to the single exception **[E2-58]** allows a commodity
business: *"a cost advantage that is both wide and sustainable … By definition such exceptions
are few."* **The competitor row was built to test exactly that, and it refuted it.**

### The competitor row — eight peers, ten fiscal years, and the subject is last of nine twice

D.R. Horton, Lennar, PulteGroup, NVR, Toll Brothers, Meritage, M/I Homes, Century Communities.
Fiscal calendars stated and aligned (KBH and LEN end 30 Nov, DHI 30 Sep, TOL 31 Oct, the rest
31 Dec). Every figure from the filers' own 10-K company-facts.

| 10-year mean | NVR | PHM | DHI | MHO | MTH | TOL | CCS | LEN | **KBH** |
|---|---|---|---|---|---|---|---|---|---|
| return on equity | 39.9 | 22.1 | 20.7 | 17.6 | 16.5 | 15.8 | 15.1 | 14.9 | **13.6** |
| **return on assets** | 23.1 | 12.5 | 13.2 | 9.1 | 10.2 | 7.8 | 7.4 | 8.5 | **6.8** |

**KB Home is last of nine on both, and last or joint-last on ROA in every one of the ten
individual years.** The obvious defence — that a lower ROE just means less leverage — was run
**before** the verdict was written **[E4-26]** and it fails twice. First, ROA is the
leverage-neutral measure and KBH is last there too. Second, the direction is backwards: KB
Home's *"ratio of debt to capital, was **30.3%** at November 30, 2025"*, rising to 34.1% by
2026-05-31, against DHI 19.8%, LEN 21.1%, TOL 17.4%. **It earns the lowest return in the group
on one of the more leveraged balance sheets in it.**

**And [E2-58]'s exception was found — in a competitor.** NVR's FY2025 10-K: *"We expect,
however, to continue to acquire **substantially all of our finished lot inventory using LPAs
with forfeitable deposits**."* NVR turns homebuilding inventory about **6.0x**; KB Home turns
it **1.11x**, owns about 62% of 59,106 lots, and put **$2.61bn** into land in FY2025 against
$6.21bn of revenue. One builder rents its land position with a capped downside; the other buys
it. **That is the wide and sustainable cost advantage, and the subject is on the wrong side of
it.** Management's own moat claim — Built to Order gives *"a meaningful and distinct
competitive advantage"* — is not dismissed in the run; it is given its strongest reading
(#1 customer-ranked builder, most ENERGY STAR homes, 73% of Q2 orders) and then **refuted by
ten years of returns in which it never once appears**.

**[E4-55] on the physical series, and all three point the same way:** deliveries 14,169
(FY2024) → 12,902 (FY2025) → **10,500–11,000 guided** (FY2026); ASP $486,900 → $481,400 →
$457,000 actual for the half-year; housing gross margin 21.0% → 18.6% → **16.1–16.5% guided**.
**[E4-37]**'s inverse metric reads at the far end: KB Home did not agonise over a price
increase; it *"**reduced selling prices** relative to applicable market conditions"* as policy.

**The [E4-04] perimeter close was available and deliberately not taken.** Under the ruling of
2026-09-20, UNKNOWABLE-at-Q2 is reserved for a name that **passes** [E3-03] and whose
durability cannot be judged from filings. KB Home does not pass [E3-03]. **OUT on the
business.**

### The refuted priors

1. **The `cap_flag`, for the sixth consecutive run, said *"one of the two is wrong"* and was
   wrong itself — and this time it was closed with arithmetic.** The filed float
   **$3,510,028,491** is dated **2025-05-31**; shares outstanding that day were **68,050,184**;
   the 2025-05-30 close was **$51.58**; and **68,050,184 × $51.58 = $3,510,028,491, to the
   dollar.** The filed "float" is **every outstanding share at the May-2025 close** — the whole
   market capitalisation on a date fifteen months before the screen's cap, not a subset of any
   later one. Nothing is wrong. What the flag actually detects is a **17.7% fall in market
   value**, 9.9 points of it price and the rest 6.74 million shares retired. **Fix: compare
   the float against a cap struck on the float's own as-of date; three of the four inputs are
   already on the cover page the tool parses.** *(BRBR, FC and APOG each reached "the two dates
   differ"; this is the first run to close it by reconstructing the float exactly.)*
2. **The brief's ASC 842 candidate for the `da_note` is REFUTED by the filing.** FY2019 10-K
   Note 1: *"**We will adopt** ASU 2016-02 … **beginning December 1, 2019**"* — the year AFTER
   the step — at *"approximately **$31.0 million**"* of right-of-use assets, with *"**no
   material impact** on our consolidated statements of operations or cash flows."* The real
   cause is **ASC 606**, Note 10: *"a change in the classification of certain community sales
   office and other marketing- and model home-related costs … **from inventories to property
   and equipment, net** due to our adoption of ASC 606 effective December 1, 2018"* — the
   "Model furnishings and sales office improvements" line going from **$0** to **$82,117
   thousand** in one year, with depreciation *"$27.2 million in 2019, $2.5 million in 2018."*
   **This outlives the name: for any homebuilder that adopted ASC 606 this way, the pre-2019
   and post-2019 operating-cash-flow series are not like-for-like**, because roughly $30–45M a
   year of model-home spend left OCF for investing activities.
3. **The v3.0 prior's competition quote SURVIVED, word for word.** `Test Runs/2026-07-16 Run -
   Homebuilders 6-pack …` rendered it as *"compete... against numerous homebuilders... some of
   which are larger and have greater financial resources than us."* The FY2025 10-K reads *"We
   compete for homebuyers, construction resources and desirable land against numerous
   homebuilders, ranging from regional and national firms, some of which are larger and have
   greater financial resources than us, to small local enterprises."* Every quoted word is
   present, in order, and both ellipses cover exactly what they should. **This project has
   struck a prior's recollection more than once; this time the prior was right, and it is
   recorded as plainly as an error would be.** Its **method** is not inherited: the v3.0 rule
   *"generic competition text eliminates"* is a verdict on prose and appears nowhere in v4 or
   the corpus. Same answer here, reached on [E3-03] and a ten-year nine-name row.

### A PRIOR IN THIS VERY FILE THAT THE BRIEF DID NOT MENTION, AND IT WAS RIGHT

The brief named one prior (the 2026-07-16 v3.0 six-pack) and said to check it. **There is a
second, and it is in this document, at the head of `## TIER 2 - triaged and NOT sent`:**

> *"**KBH (KB Home)** - the 0.39% growth-required figure is an artifact. **2023 owner earnings
> of $1,013M against a 2017-2022 mean of $192M.** That is not an earnings boom, it is a
> homebuilder's inventory unwinding into cash: land and work-in-progress released during a
> slowdown reads as operating cash flow. Recent-3 mean $514M vs earlier $192M. **Normalize
> down; the yield does not survive it.**"*

**That sweep of 2026-08-31 got the mechanism right, independently, before any filing was
opened, and this run confirms it from the cash-flow statement itself.** Its arithmetic
reconciles: its $1,013M for FY2023 against this run's $1,011.7M (OCF $1,082.7M less SBC $34.6M
less D&A $36.4M), its recent-3 mean of $514M against this run's $518.3M, and its 2017–2022
mean of $192M against this run's $198.7M — the small gaps are different (c) constructions, not
disagreements. **Three things this run adds that the triage could not:** the mechanism is now
quantified from the filed inventory line (FY2023 inventory **−$409.5M**, and −0.58 correlation
across eighteen years); the window goes back to **2008**, not 2017, and the eighteen-year
figure is **$120.7M**, not $192M; and **the name failed at Q2 on the business**, so the yield
question never arose at all. **Note also that KBH sits under "triaged and NOT sent" here and
was nevertheless dispatched as wave 7, name 14** — the two lists are different (this one is
the 2026-08-31 operator lists; wave 7 runs the 2026-09-02 master run queue CSV), but a reader
of this file should know the name appears in both and that the earlier one said to hold it.

### The wider window, which the screen could not see and which changed the number by 4.3x

`years_filed` is 18. Rebuilt, in a block headed **COMPUTATION — NOT A CLEARANCE** (operator
rule 3), because Q2 had already closed the file:

| window | owner earnings (OCF − SBC − (c)) | yield on the $2,888.9M cap |
|---|---|---|
| three years 2023–25, D&A end — the screen's top | **$518.3M** | 17.9% |
| five years 2021–25, total-capex end — the screen's bottom | **$309.1M** | 10.7% |
| **eighteen years 2008–25** | **$120.7M** | **4.2%**, below the 5.34% sovereign |
| the decade 2011–2020 | $6.9M | 0.2% |

**Operating cash flow was NEGATIVE in five of the eighteen filed years** (2010, 2011, 2013,
2014, 2021). **The screen's band is now reproducible to the dollar** — `oe_top_m 518` is the
3-year OCF mean less SBC less D&A; `oe_bottom_m 309` is the 5-year mean less SBC less total
capex — which is what the `spread_caveat`'s *"4-construction width only (3y/5y × two capex
ends)"* was saying, and this run puts a size on it: **the band sits 4.3x above the
eighteen-year figure.** **[E4-38]** names the disease (*"a calculated selection of either
initial or terminal dates"*) and its remedy is to publish every window, which the table does.

**The `wc_note` is wrong in both of its claims, and the second one is the interesting one.**
*"ONE LINE MADE THE CASH"* — FY2021 operating activities **consumed $37.3M**; there was no
cash to make, and the 487% is |+181.6| ÷ |−37.3|, a ratio to a near-zero **negative**
denominator. **Tooling defect class: a percentage published without a guard on the sign or
magnitude of its denominator.** And it names the wrong line: the **inventories** line moved
**−$897.8M** that same year, **4.9x** the accounts-payable move, and over all eighteen years
OCF correlates **−0.58** with it. **For a homebuilder, land and homes under construction ARE
the working capital of [E2-23]'s parenthetical**, so operating cash goes negative when the
builder buys land (FY2014: inventory +$919.8M, OCF −$630.7M) and positive when it liquidates
(FY2023: inventory **−$409.5M**, OCF **+$1,082.7M**). **The largest operating-cash year in KB
Home's filed record is the year it shrank its land position.** So: cycle or business? **Both,
and the window decides** — a 3- or 5-year mean anchored on FY2023 measures the liquidation
phase of a land cycle and reports it as earnings; only the eighteen-year window contains both
ends of **[E2-58]**'s *"ratio of supply-tight to supply-ample years."* And the increment is not
buying unit volume: inventory +2.6% over two years while deliveries fall about 24% to the
FY2026 guidance midpoint.

### Beneath the close, seen and not scored

- The **8-K EX-99.1 of 2026-06-23** was pulled before the decision, per the CGNX standing
  instruction. It carries a **full quarterly and full-year guidance table** and the Executive
  Chairman's *"met or exceeded the mid-point of our key guidance ranges."* That is **[E4-22]**'s
  third flag and **[E5-30]**'s ratchet, and it is **left unscored, not scored clean.**
- A non-GAAP *"Adjusted housing gross profit margin"* exists (19.1% vs GAAP 18.6% in FY2025),
  adding back impairments and abandonments — **[E5-33]** territory, also unscored.
- **The word "EBITDA" does not appear in the FY2025 10-K or the 2026-06-23 EX-99.1** — an
  observation about two documents read, not an absence claim about the company.
- The **DEF 14A of 2026-03-13 was downloaded and NOT read**; a named, deliberate gap behind a
  closed gate, not a work order.
- **No survival shape counted.** The file closed at Q2 and Q4 was never reached as a gate, so
  on the PAGP/MGPI/FC/APOG precedents this is the signature without the verdict.
- **No price band and no `PORTFOLIO.md` row** (the QLYS ruling). **Reversal condition in
  words:** KB Home would have to move to a **land-light structure** of the kind NVR discloses —
  owned lots falling well below the current ~62% of 59,106 and turns rising toward the peer top
  quartile — **and** the ROA ranking changing for reasons other than the cycle. **[E4-17]**:
  *"those beliefs change quite gradually."*

### Tooling defects found

1. **`cap_flag`** — compares a float to a cap struck on a different date and calls the
   difference an error. Sixth consecutive false firing; first time closed by exact
   reconstruction.
2. **`wc_note`** — no guard on the sign or magnitude of the OCF denominator, so a
   cash-consuming year is reported as one in which a line *"MADE THE CASH"*; and it names
   accounts payable where, for this filer class, inventories is the governing line.
3. **`newest_filing` is a REPORT date, not a filing date** — the APOG finding, confirmed on a
   second name. True newest filing 2026-08-07 (a Form 4); no Q3 filing exists yet.
4. **The band's construction is now known** (3y/D&A top, 5y/total-capex bottom) and sized
   against the long window for the first time: **4.3x**.
5. **Nothing in `Framework/`, `CLAUDE.md` or `principle_ledger.csv` was edited by this run, and
   no tool was changed.** The four defects are recorded, not patched.

### Acceptance test, the id check, and the verbatim audit

`python tools/check_framework.py` **PASS before the commit** — 0 phantom citations across
1,099 run files and 25,081 id citations, 0 unlabelled numbers in all five governed documents,
310 of 311 ledger rows verbatim against their cited sources (E5-07 is the declared negative
finding). **Every id cited was then checked directly against `principle_ledger.csv`: 46
distinct ids in the run file and 10 in the register entry, PHANTOM COUNT 0 in both**, and
twenty-seven rows were opened and read against the file's own text.

**That audit found four of my own errors and they were corrected in place before the final
commit, with the prior text left standing in git at `2625053` and the corrections named in the
run file's self-audit.** The two that matter: I had rendered **[E3-51]**'s *"the advantage
lives in the wave, not the surfer"* and **[E2-59]**'s *"neither creates the class"* as
**corpus quotations, and both are `THE FRAMEWORK v4.md`'s own commentary**. Replaced with the
ledger's actual words ([E3-51]'s surfer passage, [E4-36]'s *"Catching and riding some sort of
big wave"*, [E2-59]'s administered-prices sentence). The other two: I had **smoothed
[E4-55]'s OCR artifacts** (`""bounce back'' e'ect`), which PRIME RULE 1 forbids, and set an em
dash inside **[E2-37]** where the ledger holds a hyphen. **This is the same defect the APOG
fold corrected on [E4-36] the day before — quoting the framework's summary of a row instead of
the row. Two runs in two days, same cause: reading the corpus through the framework rather
than through the ledger.**

**`CLAUDE.md` still says the ledger is 267 rows; the file and `tools/check_framework.py` both
report 311 rows and 311 unique ids** (E1 18, E2 78, E3 79, E4 74, E5 62; no duplicates, no
empty quote cells). **ELEVENTH consecutive wave-7 fold to record that stale pointer**, which
remains the operator's call and not a run's.
