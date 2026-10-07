
## UPDATE 2026-09-25 - ICFI: Q2 OUT. A well-run bidder and not a franchise: the work is won task order by task order, re-competed at expiry and cancellable at will, and in 2025 the largest customer cancelled.

**ICF International, Inc. (ICFI), wave 7 name 33, register entry 165.** Run file `Test Runs/2026-09-25 Run - ICFI ICF
International.md`. Price $83.00 (close 2026-09-24, aggregator, flagged) x 17,933,884 shares (10-Q cover for
2026-06-30, `0001193125-26-338422`) = cap $1,488.5M; sovereign 5.47% (US Treasury, 30 Yr, 09/24/2026). **Q1 IN, Q2 OUT
on the business.**

### The finding
- **[E3-03] criterion (2) fails on how the service is bought.** The 10-K: *"We derive significant revenue and profit
  from contracts that are awarded through competitive bidding processes"*; under GSA Schedules and IDIQ vehicles *"we
  compete for each delivery order and task order"*; *"the need to lower our prices to overcome competition"* (the same
  sentence in FY2016, FY2019 and FY2025); contracts *"regularly become subject to re-competition"*, can be set aside for
  small businesses, and can be terminated *"at their convenience on short notice"* with *"no right to seek lost fees"*.
- **And on what the customer did.** *"Pursuant to the executive orders issued by the Administration and actions by the
  Department of Government Efficiency ("DOGE"), we received contract terminations and temporary stop-work orders
  primarily in the first and second quarters of 2025."* Federal revenue fell $279.5M in a year, federal share 54% to 43%,
  HHS 25% to 22%, total revenue -7.3%, and the severance was not reimbursed. The customer that thought the service had
  no close substitute would not have done that.
- **The substitutes are named, both ways.** Fifteen principal competitors in ICF's 10-K plus *"numerous smaller"*; Tetra
  Tech's FY2025 10-K names *"ICF International, Inc."* back and says clients weigh quality *"versus its cost to determine
  which firm offers the best value"*.
- **Criterion (3) fails in part**: the federal customer audits *"pricing practices, cost structure"* under the Truthful
  Cost or Pricing Data Act; the commercial third runs utility energy-efficiency programmes that regulators fund and
  utilities re-tender (six of the eight notable commercial wins in the Q2 2026 release were recompetes).
- **The demonstration clause fails on twelve years of margins**: operating margin 5.9-8.2% in every year FY2014-FY2025,
  in the middle of a peer row running 6.4% (AECOM) to 12.3% (Leidos).
- **Strongest evidence against, weighed at [E3-47] and recorded**: relationships spanning decades, 86% prime; the
  margin held through the 2025 fall (8.2% to 7.8%) on $26.0M of overhead cuts; book-to-bill 1.09 and a $9.3bn pipeline.
  All of it is evidence that ICF keeps winning bids; none of it shows the customer cannot choose someone else.

### For the next government-services contractor
**Read the MD&A's revenue bridge by client type, and the notes for restricted cash.** The first gives the customer's
conduct in dollars ($279.5M) in one sentence. The second found what no screen can: ICF's operating cash includes the
build-up of restricted utility-programme funds (client money), $37.2M of FY2025's $141.9M, and the company's own 2026
guide excludes it. And **count what the growth cost**: $1,141M of acquisitions FY2014-FY2025 against roughly
$0.76-0.97bn of owner earnings over the same years; goodwill now exceeds equity.

### Priors, refuted or confirmed
- *"Roughly half or more of revenue from US federal agencies"*: true FY2022-FY2024 (54-55%), **refuted for FY2025
  (43%) and Q2 2026 (39.0%)**.
- *"2025 terminations hit USAID and HHS-type programmes"*: **HHS confirmed**; USAID appears only as a cost-audit agency,
  no revenue figure found.
- *"About $500M of acquisitions inside the window"*: **confirmed ($499.5M, FY2021-FY2025)**; *"SemanticBits and ESAC in
  2022"*: **ESAC and Creative Systems closed in late 2021**; the window misses Olson ($298.2M, 2014) and ITG (about
  $253M, 2020).
- *Shape #14 THE PATRON*: fits the filed mechanism; recorded as a signature beneath the close, not an instance, because
  Q4 was not reached.

### Beneath the close, for the next reader
- Q3 prompts: pay on Adjusted EPS (50%) and gross revenue (30%) in the bonus, PSA Adjusted EPS with an rTSR modifier;
  2025 targets lowered after the terminations; **[E4-29] fires** in the furnished releases (EBITDA and Adjusted EBITDA
  margin in the headline bullets, a standing commitment to raise Adjusted EBITDA margin 10-20bp a year) and in the
  credit agreement; 2025 operating cash met its guide with restricted client cash inside, and the 2026 guide excludes it.
- Owner earnings FY2014-FY2025, SBC complete, (c) from capex to D&A, restricted build stripped: 5y $71-100M, 12y
  $63-81M, FY2025 alone $29-65M. Five-year yield 4.8-6.7% against 5.47%; $0.7-1.0bn at the ~10% floor with no growth,
  against $1.49bn. Arithmetic only.

### Tooling, REPORTED NOT PATCHED
- **`tools/run.py` subtracts TOTAL stock-based compensation, including cash-settled RSUs** whose cash already left
  through operating cash: a double count ($4.3-8.3M a year at ICF, FY2023-FY2025), in the conservative direction. Any
  filer with liability-classified awards carries it; the equity-settled cash-flow line is the right subtraction.
- **`tools/run.py` cannot see restricted client cash inside operating cash**: its three-year window (and the screen's
  $74-110M) carries $51.8M of restricted utility-programme build, in the generous direction. A reader must.
- No change to `SURVIVAL SHAPES - index.md`: #14 fits, but only a Q4 verdict enters the instances column.

**No alert, no PORTFOLIO.md row** (failed on the business). Reversal conditions in words at Q6: a 10-K showing a
material share of revenue under sole-source or platform terms the customer cannot re-bid; five years of operating margin
above about 12% on organic growth; utility programme renewals disclosed as extensions rather than recompetes.
