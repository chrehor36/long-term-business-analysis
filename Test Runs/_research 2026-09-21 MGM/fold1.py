# -*- coding: utf-8 -*-
"""FOLD STEP 1: the register entry, written BY LINE, never by string.replace
(the dated note of 2026-09-21 beside fold step 1)."""
import io, os, re
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Q = os.path.join(BASE, "Screens", "WATCHLIST RUN QUEUE.md")
raw = io.open(Q, encoding="utf-8").read()
lines = raw.split("\n")

HEAD = "## COMPLETED FROM THE QUEUE"
TAIL = "## THE WRITE-EARLY PROTOCOL"
heads = [i for i, l in enumerate(lines) if l.strip() == HEAD]
tails = [i for i, l in enumerate(lines) if l.strip().startswith(TAIL)]
assert len(heads) == 1, "heading not unique: %r" % ([i + 1 for i in heads],)
assert len(tails) == 1, "tail not unique"
h, tl = heads[0], tails[0]
before = [l for l in lines[h:tl] if re.match(r"^- \*\*", l)]
print("entries before insert:", len(before))
assert len(before) == 156, "expected 156 existing entries, saw %d" % len(before)

ENTRY = u'''- **MGM (MGM Resorts International), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. `Test Runs/2026-09-21 Run - MGM MGM Resorts International.md`. Price **$38.59**
  (2026-09-21, aggregator, flagged, intraday) x **251,592,756 shares** of common stock, **one
  class** ($0.01 par, the only line on the balance sheet), from the **10-Q cover for the quarter
  ended 2026-06-30, filed 2026-07-29, accession `0000789570-26-000076`** = cap **$9,709M**.
  Sovereign **5.34% USD** (US Treasury daily par yield curve, 30 Yr, 09/18/2026, issuing
  authority; FRED not used). Filing read: **10-K FY2025, filed 2026-02-11, accession
  `0000789570-26-000018`**, plus that 10-Q, the **8-K EX-99.1 of 2026-07-29
  (`0000789570-26-000075`)**, the **8-K Item 1.01 of 2026-04-07 (`0000789570-26-000029`)**, the
  **8-K Item 1.01 of 2026-05-14 (`0001193125-26-224106`)**, the **DEF 14A
  (`0001193125-26-129074`)**, the **Schedule 13D/A of 2026-06-01 (`0001104659-26-068674`)**, the
  FY2021/FY2022/FY2023/FY2024 10-Ks, and **VICI Properties' FY2025 10-K
  (`0001705696-26-000034`)** from the other side of the lease. Cross-checked against the filed
  statements, not the tags: FY2025 operating cash flow **$2,529,378**; Note 11 cash rent
  **$1,867,130** against Note 17 rent expense **$2,258,405**; Note 11 total future minimum
  operating lease payments **$54,679,646** against a **$25,068,747** present value; and FY2022
  D&A **$3,482,050** with its **$2.7 billion** intangible-amortisation component read off the
  FY2022 10-K income statement and Note 7.

  **Q2 OUT. [E3-03] clause (2) fails on the registrant's own words**, in Item 1 under "Customers
  and Competition": *"We compete against gaming companies, as well as other hospitality companies
  in the markets in which we operate, neighboring markets, and in other parts of the world,
  including non-gaming resort destinations such as Hawaii"*, and *"Our Las Vegas Strip Resorts
  also compete, in part, with each other."* **The competitor row: SEVEN comparators** (LVS, WYNN,
  CZR, BYD, PENN, MLCO and the landlord VICI), same metric, same five-year window, each from its
  own 10-K or 20-F. FY2025 operating margin **MGM 5.7%** against LVS 21.6%, BYD 18.3%, CZR 16.2%,
  WYNN 15.7%, MLCO 11.6%. Built so an owner and a tenant sit on one scale - (operating income +
  operating lease cost) over (PP&E net + operating ROU asset) - **MGM 11.2%** against BYD 25.8%
  and LVS 24.2%. **MGM has the group's largest revenue and its lowest return.** Galaxy and SJM,
  two of the six Macau concessionaires, are not SEC registrants and are named as absent.

  **THE FINDING, and it is the guarantor table.** The Rule 13-01 summarized financial information
  in the 10-K MD&A shows that MGM plus its wholly owned **domestic** guarantor subsidiaries - all
  nine Las Vegas Strip resorts, excluding MGM China, LeoVegas, BetMGM, Detroit, National Harbor
  and Springfield - earned **operating income of $78.5M on net revenues of $10,580.2M in FY2025**,
  against **$733.7M** in FY2024 and **$1,324.6M** in FY2023 on 1.9% more revenue. Even assigning
  every consolidated one-off to that group the series reads about **$954M to $815M to $483M**.
  Note 10 says it in one line: **domestic pre-tax income $1,214.9M (2023), $256.9M (2024),
  MINUS $237.1M (2025)**, with all FY2025 pre-tax income foreign. **The registrant sold the only
  scarce input in its business - the land - and leased it back** on 25-to-30-year triple net
  master leases with 2% escalators: $25,068,747 thousand of operating lease liability,
  **$54,679,646 thousand undiscounted**, against $6,305,614 thousand of property and equipment.
  VICI's own 10-K: MGM and Caesars are *"our two largest tenants representing 39% and 35%,
  respectively, of our annualized rent"* - the same landlord rents the same class of building to
  MGM's nearest rival, with the MGM leases parent-guaranteed and cross-defaulted.

  **[E4-37] and [E4-55]:** no agony over a price increase because there was none - Las Vegas ADR
  $260 to $249 and RevPAR $245 to $229 in FY2025 with occupancy down to 92%, and both down a
  further 4% in Q2 2026. Q2 2026 Las Vegas casino revenue rose **17%** while table games drop fell
  **2%** and slot handle was flat: the whole of it is hold, 29.6% against 22.9%, which the 10-K
  itself calls *"not fully controllable by us."*

  **RECORDED BENEATH THE CLOSE (no box ticked).** Q3: **[E4-29] fires at full strength** - the
  headline profit measure is Segment Adjusted EBITDAR, struck before **$2,258.4M of rent** and
  **$1,017.8M of D&A**, and 75% of the CEO's bonus turns on "Compensation Adjusted EBITDAR" whose
  target the proxy says was the budget *"as further increased by the Company's rental payments"*;
  2025 outturn $4,304,248,000 and ~100% of target paid in the year the guarantor group's operating
  income fell 89%. **[E2-49] fires**: Absolute TSR PSUs removed and the Relative TSR index moved
  from the S&P 500 to the S&P 1500 Hotels index in one year, both announced ahead with reasons and
  a negative-TSR funding cap retained. **[E4-30] recorded and it fires**: cash taxes 23.4%, 23.9%,
  then **minus 12.3%** of pre-tax - explained by the domestic loss and a $283.7M valuation-allowance
  release, not by manipulation. **[E3-54] fails**: $0.68 of market value per $1 retained over
  2021-2025. Projections flag does NOT fire (no numeric guidance). Serial issuance does NOT fire
  (43% of the shares retired since 2021, $9,406.8M spent).
  Q4: **SBC resolves and is COMPLETE for all 18 filed years.** Owner earnings rebuilt over
  **eleven windows and three (c) ends**: **about $40M (2020-2025, c=D&A) to $1,679M (2023-2025,
  c=depreciation only)**, five-year default $607M to $1,259M, eighteen-year record $175M to $543M.
  The screen's $607M-$1,558M band reproduces exactly as the 5y and 3y means at the c=D&A end; the
  true width is about 42x wider at the bottom. **Gruesome [E4-20].** Death named: **shape #13 THE
  TENANT**, with **#1 CONTRACTED NOT TO STOP** as its feature; no new shape proposed. Likelihood:
  **a real possibility**.
  Q5: **DID NOT OPEN.** Computation only: 0.4% to 17.3% yield, 3.0% to 14.1% after the
  noncontrolling interests' $315.0M claim, against a **5.34%** sovereign and the ~10% floor
  [E4-28]. The band straddles the floor; under **[E4-25]** the width IS the conclusion.
  **AND THE PRICE IS NOT A CLEAN PRICE: a live, unresolved go-private proposal at $48.30 cash**
  from People Incorporated (f/k/a IAC), filed 2026-06-01 as an exhibit to a **Schedule 13D/A**,
  from the holder of more than 25.73% of the votes, whose chairman sits on MGM's board.
  **`deal_note()` did not see it, because SC 13D/A is not in `DEAL_FORMS`** - the fourth live-deal
  miss after CTAS, ACLS and ROKU, and a new class: the bidder-disclosed proposal.
  **NO ALERT BAND AND NO PORTFOLIO ROW** (fold step 4, the QLYS ruling): the file closed at Q2, on
  the business. The reversal condition is written in words at Q6 of the run file.
'''

new = lines[:h + 1] + ENTRY.rstrip("\n").split("\n") + lines[h + 1:]
io.open(Q, "w", encoding="utf-8").write("\n".join(new))

# VERIFY by re-reading from disk and counting back
lines2 = io.open(Q, encoding="utf-8").read().split("\n")
h2 = [i for i, l in enumerate(lines2) if l.strip() == HEAD]
t2 = [i for i, l in enumerate(lines2) if l.strip().startswith(TAIL)]
assert len(h2) == 1 and len(t2) == 1
after = [l for l in lines2[h2[0]:t2[0]] if re.match(r"^- \*\*", l)]
print("entries after insert:", len(after))
print("FIRST entry is now:", after[0][:80])
assert len(after) == 157, "expected 157, saw %d" % len(after)
assert after[0].startswith("- **MGM (MGM Resorts International)"), "MGM is not first"
print("VERIFIED: MGM is register entry 157 and is first in the register.")
