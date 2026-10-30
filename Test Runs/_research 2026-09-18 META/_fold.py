import sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\chreh\OneDrive\Documents\BRK"

# 1. register entry at the top of COMPLETED FROM THE QUEUE
Q = ROOT + r"\Screens\WATCHLIST RUN QUEUE.md"
q = open(Q, encoding="utf-8").read()
ENTRY = """- **META (Meta Platforms), 2026-09-18 - FAIL at Q2 (OUT, ON THE BUSINESS [E3-03] criterion 2, with [E4-04], [E4-55], [E4-38], [E2-44], [E3-46], [E3-51], [E2-59], [E4-23].
  The FY2025 10-K's own Item 1A: users are *"actively engaging with other products and services similar to, or as a substitute for, our products and services"*, TikTok
  named as having *"reduced some users' engagement"*, and *"Many of our marketers spend only a relatively small portion of their overall advertising budget with us"*; the
  D.D.C. held on 2025-11-18 (*FTC v. Meta*, No. 20-3590, opinion read from the court's server), on Meta's own argument, that *"YouTube and TikTok belong in the product
  market, and they prevent Meta from holding a monopoly"*; the average price per ad compounds to 0.97 times FY2018's over seven filed years (-5%, -10%, +24%, -16%, -9%,
  +10%, +9%) while impressions grow; the company calls its business *"characterized by innovation, rapid change, and disruptive technologies"* and holds the position by
  rebuilding its basis, now at a guided $130-145bn of 2026 capital spending, $349.31bn of commitments and about $347bn of signed leases not yet commenced, no filing
  splitting defence from replacement; the EU sets the terms in 23% of revenue (DMA); founder control recorded; on a five-filer row (GOOGL with its Services segment,
  AMZN advertising, SNAP, PINS, RDDT; TikTok, X and OpenAI file nothing) Meta is the margin and owner-cash leader, and the most capital-hungry by FY2025).** Q1 IN
  (advertising by auction on four apps, 97.6% of FY2025 revenue; superintelligence, enterprise AI and Reality Labs, $96.7bn of losses since FY2019, kept outside the
  circle [E3-31, E4-46]; the case for UNKNOWABLE recorded and not taken). Q3, Q4, Q5 and Q6 RECORDED, NOT GOVERNING (Q3 a GATE case on daily execution; UNRESEARCHED
  on the binary under [E5-22]: the 2012 FTC order, the 2019 $5.0bn settlement of its violation, the 2023 proceeding to modify it, the 2026 New Mexico jury verdict of a
  $375M civil penalty; work order: that verdict record and the FTC's 2023 Order to Show Cause; prompts on two server-life extensions, a capital-spending guidance
  raised in every quarter since January 2025, and the withdrawn Facebook-app user series; capital-allocation flag on FY2025 buybacks at about $657 [E5-08, E4-13];
  pay vests on nothing the capital earns; 20 million options granted in Q2 2026 at $2,788; Q4 UNKNOWABLE: owner earnings five-year FY2021-25 **$24,655M at the capex
  end (central; finance-lease principal subtracted) and $50,431M at the D&A end, which is INVALID under [E5-20]** (server lives lengthened twice while hardware costs
  rise; capex 4.07 times D&A); twelve months to 2026-06-30 $12,736M; FY2025 about $3.1bn with stock pay at grant value [E3-70] ($40.4bn net granted in FY2025, $38.6bn
  in H1 2026, $79.79bn unrecognized); strength 3 fails [E5-11]; shape #10 THE CAMOUFLAGE with #1 and #2 as features; price headed COMPUTATION - NOT A CLEARANCE; Q6
  records the reversal condition in words and arms nothing). WAVE 5, the first of the "no share count from dei" names. **Register entry 109**, counted from this file's
  heading to `## THE WRITE-EARLY PROTOCOL` (108 line-start entries before it, no duplicate ticker, META not previously entered). `Test Runs/2026-09-18 Run - META Meta
  Platforms.md` (template `f80e17c`, Step 0 `9e4c906`, Q1-Q2 `5f8d195`, Q3-Q6 with audit and register `c21ba07`, fold in the fold commit), `check_framework.py` PASS.
  **THE PAIR.** Price **US$665.75** (2026-09-18 close, Yahoo chart `regularMarketPrice` at 16:00:02 EDT, aggregator flagged; the series corroborated by Form 4 sale
  prices inside the day's range on 2026-09-09, -14 and -15, `0000950103-26-013860`, `-014061`, `-014140`) x **2,547,506,225** (Class A 2,205,128,509 + Class B
  342,377,716) x 1.0 = cap **US$1,696.0bn** ($1,793.5bn with 146,464K unvested RSUs). **Count:** the Q2 2026 Form 10-Q cover, accession **`0001628280-26-050705`**
  (filed 2026-07-30, the latest periodic filing), both classes *"shares outstanding as of July 24, 2026"*; **A and B added one for one** on the charter's *"3.1. Equal
  Status"* clause (same rights, *"rank equally (including as to dividends and distributions, and upon any liquidation"*), ratable dividends, liquidation and merger
  consideration, and Class B convertible one for one; only the votes differ (ten to one). Nothing sold after the cover; no buyback in H1 2026; $25bn of notes sold
  2026-05-04. **Perimeter:** Scale AI minority stake ($13.80bn); the Louisiana data-centre Venture off the balance sheet (20% equity-method interest, $12.31bn of
  leases from 2029, a $28bn residual value guarantee, maximum exposure $45.95bn). **Sovereign** USD 30-year **5.34%** (US Treasury daily par yield curve,
  **09/18/2026**, fetched directly; `tools/sources.sovereign()` served the cached 09/17 row, 5.29%, a seventh time). **Computation, not a clearance:** yield 0.75%
  (twelve months) to 1.72% (three-year) at the capex end, 2.97% at the invalid D&A end, against 5.34% and a ~10% floor, which would need about $170bn a year; the price
  is 3.3 to 7 times a no-growth floor value of $250-500bn. **No band armed and no PORTFOLIO row** (a Q2 OUT is a finding about the business). **Reversal condition, in
  words:** reopen Q2 only on the price per ad rising five years running including a year of impressions growth below 5%; the D.C. Circuit reversing the finding that
  TikTok and YouTube are in Meta's market, with the 10-K's substitute sentence gone; capital spending plus finance-lease principal below 25% of revenue for three years
  with revenue growing, or a filed split of the build with a return on its new-business part; and owner cash (stock pay at grant value) positive and rising over a
  rolling five years without net borrowing.
"""
anchor = "## COMPLETED FROM THE QUEUE\n"
assert q.count(anchor) == 1 and "- **META (Meta Platforms)" not in q
q = q.replace(anchor, anchor + ENTRY, 1)

# 2. strike META in the wave 5 row and add a dated note after the AEHR note
old_row = "| no share count from dei: read the cover | META, DASH, PATH, PUBM, BZFD |"
assert q.count(old_row) == 1
q = q.replace(old_row, "| no share count from dei: read the cover | ~~META~~, DASH, PATH, PUBM, BZFD |")
NOTE = """
*Dated note, 2026-09-18 (the META run), left beside the table rather than editing its row (operator rule 6): **for META the "no share count from dei" label was a TAGGING CONVENTION FOR A TWO-CLASS COVER, not a missing or stale count.** companyfacts carries one dei element for Meta, `EntityPublicFloat`, so `share_count_shift` returned None (the RIVN reading: not measured, not stable). **The inline XBRL of the latest 10-Q (`0001628280-26-050705`, cover as of 2026-07-24) does tag `dei:EntityCommonStockSharesOutstanding`, twice: 2,205,128,509 in a context dimensioned `us-gaap:StatementClassOfStockAxis` = `CommonClassAMember`, and 342,377,716 dimensioned `CommonClassBMember`. companyfacts publishes only undimensioned facts, so a per-class cover never reaches it.** `Screens/cover_shares.py` reads both and correctly refuses to add them; the addition is a judgment, made from the charter (*"3.1. Equal Status"*: the classes *"rank equally (including as to dividends and distributions, and upon any liquidation"* and are *"identical in all respects"*, Class B converting one for one; only the votes differ), so the count is the sum, 2,547,506,225. The other `a8bc84f` guards did not fire (`scale_shift` 1.372; `restatement_shift` 1.0, a null); no restatement exists. **The file closed at Q2 on the business, not on the label.** **The row's tally opens with this note: of one name run so far, META's label was a dimensioned two-class cover.** DASH, PATH, PUBM and BZFD should have their latest cover read in the inline XBRL first (for dimensioned per-class facts) before the label is read as a missing count, and any multi-class cover's classes should be added only on the charter's economic terms.*
"""
aehr_anchor = "before it is read as a business step.*\n"
assert q.count(aehr_anchor) == 1
q = q.replace(aehr_anchor, aehr_anchor + NOTE, 1)
open(Q, "w", encoding="utf-8").write(q)
print("queue ok")

# 3. narrative fold
RL = ROOT + r"\Screens\2026-08-31 PREPPED READING LIST (operator lists).md"
r = open(RL, encoding="utf-8").read()
FOLD = """
## UPDATE 2026-09-18 - META: Q2 OUT, the largest audience in the world, and a court found its substitutes at Meta's own request
`Test Runs/2026-09-18 Run - META Meta Platforms.md`. **Q1 IN; Q2 OUT on the business, file closed; Q3 recorded (a GATE case on daily execution; UNRESEARCHED on the
binary); Q4 recorded (UNKNOWABLE on the (c) width); Q5 headed COMPUTATION - NOT A CLEARANCE; Q6 recorded with nothing armed.** Price **US$665.75** (2026-09-18 close,
aggregator flagged, three Form 4 sale prices inside the day's range) x **2,547,506,225** (Class A 2,205,128,509 + Class B 342,377,716, the Q2 2026 10-Q cover,
`0001628280-26-050705`, added one for one on the charter's equal-status clause) = cap **US$1,696.0bn**; sovereign **USD 30-year 5.34%** (US Treasury, 09/18/2026).
**The first of wave 5's "no share count from dei" names. Register count at the fold, read from the register: 109 runs** (META adds one Q2 OUT).

### WHY Q2 CLOSED, ON THREE INDEPENDENT RECORDS
- **The company's own words** (FY2025 10-K Item 1A): users *"actively engaging with other products and services similar to, or as a substitute for, our products and
  services"*; TikTok named as having *"reduced some users' engagement"*; marketers spend *"only a relatively small portion of their overall advertising budget with us"*;
  and the business is *"characterized by innovation, rapid change, and disruptive technologies"* ([E3-03](2), [E4-04]).
- **The court, at Meta's urging**: *FTC v. Meta*, D.D.C., 2025-11-18 (89-page opinion fetched from the court's own server): *"YouTube and TikTok belong in the product
  market, and they prevent Meta from holding a monopoly"*; *"Meta holds no monopoly in the relevant market."* The FTC appealed on 2026-01-20. The GOOGL file's Q2 IN
  leaned on a court finding Alphabet a monopolist; this file is its mirror.
- **The price series across the whole window** [E4-55, E4-38]: average price per ad -5%, -10%, +24%, -16%, -9%, +10%, +9% (FY2019-25), 0.97 times FY2018's by FY2025,
  while impressions grew; the three rising periods (FY2024 to H1 2026) are attributed by the filer to better ad targeting, i.e. to the spending.
- **The capital**: capex/revenue 15.8% (FY2021) to 34.7% (FY2025), a 2026 guide of $130-145bn raised in every quarter since January 2025, $349.31bn of commitments and
  about $347bn of signed leases not yet commenced at mid-2026; no filing splits defence of the ad business from the superintelligence build [E2-44](2), [E3-46].
- **The row** (GOOGL with Services, AMZN advertising, SNAP, PINS, RDDT, re-fetched; TikTok, X and OpenAI file nothing): Meta is the margin leader (37.4% five-year) and the
  owner-cash leader (16.8% of revenue), and the most capital-hungry by FY2025. Position is not in doubt; the franchise definition is.

### THE SKIP REASON, FROM THE FILED RECORD
- **A dimensioned two-class cover**: the count is tagged per class of stock, and companyfacts drops dimensioned facts. The dated note under the wave 5 table opens the
  row's tally and tells DASH, PATH, PUBM and BZFD to read the inline XBRL cover first.

### Q3 FINDINGS WORTH KEEPING (recorded, not governing)
- **[E5-22] pattern on the conduct record**: the 2012 FTC order, the 2019 $5.0bn settlement of its violation, the 2023 proceeding to modify it again (stayed), the New
  Mexico jury's $375M civil penalty (2026-03-24), $2.4bn of legal charges in Q2 2026, a $190M derivative settlement paid by insurers with all wrongdoing denied. Recorded
  UNRESEARCHED: the verdict record and the FTC Order to Show Cause are the work order.
- **Guidance**: next-quarter revenue guidance met or beaten five quarters running; capital-spending guidance raised every quarter since January 2025 [E3-48, E5-30].
- **Accounting prompts**: server lives lengthened in 2022 and to 5.5 years in 2025 ($2.92bn less depreciation in FY2025) while hardware costs rise; Facebook-app user
  series withdrawn from 2024. No EBITDA or adjusted earnings in any release.
- **Allocation**: FY2025 buybacks of $26.3bn at about $657 against owner earnings yielding 1.5-3.0% at that price (flag, with [E4-13]); dividends paid in 2026 while
  borrowing; pay vests on nothing the capital earns; 20 million options granted in Q2 2026 at a $2,788 exercise price.

### Q4 AND (c)
- **(c) is in the [E5-20] exception class** (net plant $225.7bn on twelve-month revenue of $228.2bn; capex 4.07 times D&A; lives lengthened while costs rise); the D&A
  end ($50.4bn five-year) is INVALID and shown as display. **Capex end, finance-lease principal subtracted: $24.7bn five-year, $29.2bn three-year, $12.7bn for the twelve
  months to June 2026, -$0.5bn for H1 2026.** With stock pay at grant value [E3-70] FY2025 falls from $23.2bn to about $3.1bn.
- **Off the balance sheet and not in any year yet**: about $347bn of signed leases (roughly $17-19bn a year when commenced) and the Louisiana Venture's $45.95bn maximum
  exposure. Strength 3 fails [E5-11]; Q2 2026 free cash flow covered twelve-month interest obligations about 0.7 times on an annualised quarter [E2-54].
- **Shape #10 THE CAMOUFLAGE**, with #1 and #2 as features; no new shape (later instances added to `Screens/SURVIVAL SHAPES - index.md`).

### REVERSAL CONDITION, IN WORDS (fold step 4; nothing armed, no PORTFOLIO row)
Reopen Q2 only on: the price per ad rising five years running including a year of impressions growth below 5%; the D.C. Circuit reversing the substitute finding, with
the 10-K's substitute sentence gone; capital spending plus finance-lease principal below 25% of revenue for three years with revenue growing, or a filed split of the
build with a return on its new-business part; and owner cash, stock pay at grant value, positive and rising over a rolling five years without net borrowing.

### FOR THE OPERATOR
- **The v4 evidence ladder has no court-record rung**; this run (like GOOGL) read a court opinion from the court's own server for a Q2 finding. Recorded as a judgment,
  not a rule change.
- **The screen's capex end subtracts finance-lease right-of-use additions, not principal paid** ($613M against $2,524M for Meta in FY2025): a tooling proposal that
  would change a number, so not made.
- **`tools/sources.sovereign()` served a stale cached row a seventh time** (09/17 5.29%; the Treasury's 09/18 figure is 5.34%).

### ONE THING TO KEEP
**Read the company's own litigating position.** A company that has proved in court that it has close substitutes has answered [E3-03]'s second criterion.
"""
r = r.rstrip("\n") + "\n" + FOLD
open(RL, "w", encoding="utf-8").write(r)
print("reading list ok")

# survival shapes: later instances
S = ROOT + r"\Screens\SURVIVAL SHAPES - index.md"
s = open(S, encoding="utf-8").read()
a10 = "| HMC (declared in its own 20-F), ERIC (enterprise leg) |"
a1 = "| BA (a feature), AMZN (beside #18), NVDA ($279bn of supply commitments, beside #18) |"
a2 = "| BA 184% of FY2025 OCF, ACVA 330.5%, ROKU, CALX |"
for a in (a10, a1, a2):
    assert s.count(a) == 1, a
s = s.replace(a10, "| HMC (declared in its own 20-F), ERIC (enterprise leg), META (2026-09-18: advertising cash recycled into Reality Labs, $96.7bn lost since FY2019, and the superintelligence build; #1 and #2 as features) |")
s = s.replace(a1, "| BA (a feature), AMZN (beside #18), NVDA ($279bn of supply commitments, beside #18), META ($349.31bn of commitments and about $347bn of signed leases, a feature of #10) |")
s = s.replace(a2, "| BA 184% of FY2025 OCF, ACVA 330.5%, ROKU, CALX, META (at the [E3-70] grant-value measure only: $40.4bn net granted in FY2025, $38.6bn in H1 2026) |")
open(S, "w", encoding="utf-8").write(s)
print("shapes ok")
