# -*- coding: utf-8 -*-
import io, re

P = "Screens/WATCHLIST RUN QUEUE.md"
t = io.open(P, encoding='utf-8').read().split('\n')
h = [n for n, l in enumerate(t) if l.startswith('## COMPLETED FROM THE QUEUE')][0]
e = [n for n, l in enumerate(t) if l.startswith('## THE WRITE-EARLY PROTOCOL')][0]
before = [n for n in range(h + 1, e) if re.match(r'^- \*\*', t[n])]
assert not any('IIIN' in l for l in t), "IIIN already present"
print("register entries before:", len(before), " heading line", h + 1, " end heading line", e + 1)

entry = '''- **IIIN (Insteel Industries Inc.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 20 of 218. Register entry 152** (re-derived, not inherited: line-start
  `^- \\*\\*` counted **by index** in the slice from this file's `## COMPLETED FROM THE QUEUE`
  heading (found by grep at line 502) to `## THE WRITE-EARLY PROTOCOL` (found by grep at line
  12273 - the heading moved again, and the ADM entry directly below cites 12096).
  **151 entries stood above this one, no duplicate ticker, and IIIN appeared NOWHERE in the
  file.** After insertion: 152.)
  **Price US$29.66**, close of **2026-09-18**, aggregator (Yahoo Finance chart endpoint),
  **flagged as an aggregator, live quote only**; raw JSON saved to
  `Test Runs/_research 2026-09-21 IIIN/price_raw_aggregator.json`.
  **Shares 19,358,247, a SINGLE class of "Common Stock (No Par Value)"**, read off the cover of
  the **10-Q for the quarterly period ended 2026-06-27, accession `0001437749-26-023682`,
  filed 2026-07-16**, as-of date 2026-07-15. No split after the measurement date
  (`split_factor_after` = 1.0); no second class (the FY2025 balance sheet reads *"Preferred
  stock, no par value Authorized shares: 1,000 None Issued"*); no convertible preferred.
  **CAP, STRUCK BY HAND: 19,358,247 x $29.66 = $574.2M.** The screen carried **$588M**.
  **-2.4%, and it is a price-date difference, not a count error - the screen's cap survives the
  re-strike as arithmetic**, the way ADM's did and unlike BELFB's (6.29x) and FC's (18%).
  Insteel is the single-class, current-cover shape; checked rather than assumed.
  **Sovereign US$ 30-year 5.34% at 09/18/2026**, struck fresh for this run from the **US
  Treasury daily par yield curve** (issuing authority; FRED DGS30 not used, and the rate was not
  inherited from the brief). Earnings currency USD, no FX.
  **FY2026 HAS NOT CLOSED AND NO 10-K FOR IT EXISTS** - the year ends 2026-10-03 (Saturday
  nearest 30 September), twelve days after this run, so `newest_periodic 2026-06-27` is Q3 FY2026
  and both screen dates are correct.
  **Anchor filing read: 10-K FY2025, period ended 2025-09-27, accession `0001437749-25-031597`,
  filed 2025-10-23.** Three hand cross-checks: FY2025 *"Net cash provided by operating activities
  27,163"* on the filed cash-flow statement, equal to the tagged fact; equity recomputed from
  A - L ($462,650 - $66,009 - $25,109) = **$371,532**, the filed Total shareholders' equity to
  the dollar; and FY2025 net sales **$647,706** against the MD&A's own *"increased 22.4% to
  $647.7 million"*. Also read: the Q3 FY2026 10-Q (`0001437749-26-023682`), the DEF 14A of
  2026-01-02 (`0001308179-26-000001`), four quarterly 8-K EX-99.1 earnings releases, and the
  8-K EX-99.1 of **2026-08-21** announcing the Upper Sandusky closure (`0001437749-26-028729`).
  **PASS/FAIL: FAIL AT Q2 - OUT ON THE BUSINESS, at [E3-03] criterion 2 (no close substitute),
  on the registrant's own Item 1.** *"Our markets are highly competitive based on price, quality
  and service."* Six named direct rivals plus imports, and its flagship engineered structural
  mesh is sold as *"a lower cost reinforcing solution than hot-rolled rebar"*, so the product is
  itself in a substitution relationship. **[E2-58]** supplies the class - the one exception, *"a
  cost advantage that is both wide and sustainable"*, is refuted by the same Item 1, which says
  the largest rivals *"are vertically integrated companies that produce both wire rod and
  concrete reinforcing products"* while wire rod is **85.6% of Insteel's cost of sales**.
  **[E2-59]** supplies the regime: the 10-K says four times that anti-dumping and countervailing
  duties *"had the effect of limiting the participation of these countries in the domestic
  market"*, and the risk factors concede *"Trade law enforcement is critical to our ability to
  maintain our competitive position"*. **[E4-04]**'s UNKNOWABLE perimeter branch was checked and
  rejected with reasons: that branch is for names that PASS [E3-03].
  **THE COMPETITOR ROW [E3-28]: 7 named by the subject, 1 obtainable and unsegmented.** Wire
  Mesh Corporation, Concrete Reinforcements, National Wire Products, Davis Wire, Oklahoma Steel
  & Wire and Sumiden Wire all return *"No matching companies"* on EDGAR company search and are
  disclosed UNOBTAINABLE. Net income on year-end equity, FY2010-FY2025 (16 years, identical
  construction, each filer's own 10-K facts): **STLD 17.7% / NUE 14.6% / IIIN 9.9% / CMC 8.9%**.
  **Insteel earns the lowest of the four while carrying NO DEBT AT ALL**, so the row is run in
  the subject's favour and still refutes the cost-advantage claim. Row cross-checked against
  Nucor's own FY2025 MD&A (*"Return on average stockholders' equity was 8.5% and 9.8% in 2025
  and 2024"*) against my 8.3% and 10.0%: average-equity versus year-end-equity, nothing else.
  **THE PHYSICAL SERIES [E4-55] IS THE PRECISION STEEL SHAPE.** FY2022 net sales **+40.0%** on
  shipments **-7.8%**; FY2021 to FY2024 shipments -0.6%, -7.8%, -5.3%, flat; the only growth
  year, FY2025 (+14.8%), is bought - *"primarily due to incremental volume generated from our
  acquisitions"* ($72.1M, 12.6% of the hand cap).
  **THE OWNER-EARNINGS REBUILD, THE FINDING THAT MATTERS FOR THE QUEUE.** The screen's
  **$40M-$57M** reproduces exactly (3y/5y x two ends = 39.7 / 42.7 / 53.5 / 57.2) and is the
  wrong answer: **sixteen filed years give $24.0M-$24.1M**, and the **TTM to 2026-06-27 is
  NEGATIVE at both ends (-$20.5M dep / -$13.3M capex)**. FY2023 alone is **59.2%** of the
  five-year window, and **68.6% of FY2023's operating cash was a working-capital release,
  $94.3M of it the inventory line**, unwinding FY2022's $118.6M build. Combined range
  **-$20.5M to $57.2M**, which is **[E4-25]**'s too-wide-to-conclude on its own.
  **THE `wc_note` DIRECTION IS INVERTED, THE SECOND TIME IN FOUR CYCLES (after BELFB).**
  Arithmetic right (19,260 / 27,163 = **70.9%**), direction wrong: the MD&A says *"Working
  capital used $37.6 million of cash"* and the flagged payable was the **offset** to a net
  **-131%-of-OCF** drain. **Two further tooling defects reported, not patched: `WC_TAGS` holds
  only liability tags, so the flag cannot see inventories or receivables at all** (Insteel tags
  both, every year, and the inventory line it could not see is the one that carries the band);
  **and the flag prints only the single largest line**, which here was the offset.
  **TWO DOCUMENTATION FINDINGS, reported and not edited.** `principle_ledger.csv` holds **311
  rows**, not the **267** `CLAUDE.md` and every brief still state (267 at `9d38c16`, 286 at
  `b7e84ca`, 311 at `0eaeadd`, the last two both 2026-09-20). And `THE FRAMEWORK v4.md` smooths
  a transcript artifact in **[E4-46]**, printing *"the following five months"* where the ledger
  row reads *"the followings five months"*.
  **Q3 and Q4 notes beneath the close, no verdicts:** **[E4-29] is CLEAN and was checked in the
  8-K earnings releases, not just the 10-K** - *"EBITDA"*, *"non-GAAP"* and *"adjusted earnings"*
  appear **zero times** in the 10-K, the 10-Q, the proxy and all six 8-K exhibits, and **no
  numeric earnings guidance exists in any release**. My **[E2-49]** metric-withdrawal prior was
  tested and **did not fire - the count stays at six fires and six failures**: return on capital
  has been the sole annual-incentive metric for at least fifteen years and the proxy publishes
  the whole series including **0.0% payouts in 2011, 2012 and 2019 and 29.0% in 2024**, which is
  the **[E2-67]** positive pole. Zero debt at every date read. The named death is quantified by
  the filer itself: *"a 10% increase in the price of wire rod would have resulted in a $33.1
  million decrease in our pre-tax earnings"*, against **nine-month pre-tax earnings of $28.1M** -
  **118% of them**.
  **NO PRICE ALERT AND NO PORTFOLIO ROW (the QLYS ruling):** the name failed on the BUSINESS, so
  the reversal condition is recorded in words, price excluded **[E5-35]** - a structural removal
  of industry over-capacity, a flat-demand year in which prices rise **[E2-44]**, three years of
  organic tonnage growth separated from acquired tonnage **[E4-55]**, or backward integration
  into wire rod.
  Run file: `Test Runs/2026-09-21 Run - IIIN Insteel Industries.md`.'''

t.insert(h + 1, entry)
io.open(P, 'w', encoding='utf-8').write('\n'.join(t))

t2 = io.open(P, encoding='utf-8').read().split('\n')
h2 = [n for n, l in enumerate(t2) if l.startswith('## COMPLETED FROM THE QUEUE')][0]
e2 = [n for n, l in enumerate(t2) if l.startswith('## THE WRITE-EARLY PROTOCOL')][0]
after = [n for n in range(h2 + 1, e2) if re.match(r'^- \*\*', t2[n])]
print("register entries after:", len(after))
print("IIIN lines now:", sum(1 for l in t2 if 'IIIN' in l))
