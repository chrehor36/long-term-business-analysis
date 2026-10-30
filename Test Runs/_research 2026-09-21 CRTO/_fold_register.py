# -*- coding: utf-8 -*-
"""Fold step 1: insert the CRTO register entry at the top of ## COMPLETED FROM THE QUEUE."""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

p = "Screens/WATCHLIST RUN QUEUE.md"
s = open(p, encoding="utf-8").read()
head = "## COMPLETED FROM THE QUEUE\n"

if "**CRTO (Criteo S.A.)" in s:
    print("ALREADY PRESENT - nothing done")
    sys.exit(0)

entry = """- **CRTO (Criteo S.A.), 2026-09-21 - FAIL at Q2 (OUT, ON THE BUSINESS).**
  Q1 IN. **WAVE 7, name 16. Register entry 148** (re-derived, not inherited: line-start `^- \\*\\*`
  counted inside the slice taken **by index** from this file's `## COMPLETED FROM THE QUEUE`
  **heading line** to `## THE WRITE-EARLY PROTOCOL`. **147 entries stood above this one**, which
  agrees with the MNRO entry directly below claiming 147 for itself and with the dispatcher's
  count. After insertion: 148. No CRTO entry existed; the only prior occurrence of the ticker in
  the slice is inside the PUBM entry, which names Criteo as a peer.)
  **Price US$16.70**, close of 2026-09-18, aggregator (Yahoo Finance chart endpoint via
  `tools/sources.py`), **flagged as an aggregator, live quote only**. **Shares 48,997,559**, from
  the **cover of the 10-Q for the quarter ended 2026-06-30, accession `0001576427-26-000092`,
  filed 2026-08-05** - *"As of July 31, 2026, the registrant had 48,997,559 ordinary shares,
  nominal value EUR 0.025 per share, outstanding."* **One class**, registered under Section 12(b)
  as *"Ordinary Shares, nominal value EUR 0.025 per share | CRTO | Nasdaq Global Select Market"*.
  **Treasury shares are OUTSIDE the cover count and they exist**: the balance sheet reads
  *"53,728,895 and 55,659,895 shares authorized and issued, and 48,550,453 and 51,151,866
  outstanding at June 30, 2026 and December 31, 2025"*, so 5,178,442 shares sat in treasury at
  2026-06-30 and the cover figure is already net of them. No split anywhere in twelve years.
  **CAP, STRUCK BY HAND: 48,997,559 x $16.70 x 1.0 = $818.3M.** The screen carried $865M, which
  is the same share count at an early-September price; its share count was right and its price was
  two weeks and 5.4% stale.
  **`cap_flag` SETTLED AS A DATE MISMATCH AND REFUTED AS AN ERROR CLAIM.** The flag said a cap of
  $865M could not sit below a filed float of $1,254M at 2025-06-30. Both numbers are correct at
  their own dates: $1,254M / $23.96 (the Nasdaq close of 2025-06-30, on which the FY2025 10-K
  cover states the float is struck) = **52.34M non-affiliate shares**, against a Q2 2025
  weighted-average count of 52,986,068 - a 99.7% non-affiliate register. Price then fell 30.3% and
  the share count fell 6.7% on buybacks (3,187,498 repurchased at a weighted average $32.80 in
  FY2025; 3,339,332 at $18.36 in H1 2026; 1,931,000 treasury shares cancelled). 0.697 x 0.933 x
  $1,254M = $815M against the hand-struck $818.3M - **the reconciliation closes to 0.4% and
  neither figure is discarded.**
  **SOVEREIGN: USD 5.34%, 2026-09-18, U.S. Treasury daily par yield curve, 30-year, from the
  issuing authority** (raw CSV saved to the research folder; FRED not used). **The earnings
  currency was argued from the filings, not assumed**, because this is the case where it bites:
  reporting currency USD, but the FY2025 10-K Item 7A says *"The functional currency of the
  Company is the euro, while our reporting currency is the U.S. dollar."* Decided **USD** on the
  revenue footnote - United States $753.3M (38.7%) is the largest single-currency block, no other
  currency reaches half of it (Japan 11.4%, Germany 10.7%, France 4.6%), EMEA's 37.4% is not a
  euro block, and every figure in the owner-earnings construction is a USD figure. The alternative
  is stated: **ECB SDW SR_30Y = 3.7502% at 2026-09-17**. Choosing USD is 159bp harder on the
  buyer. The screen's `vs_sovereign 0.0383` was discarded in full.
  **`deal_note` SETTLED ON BOTH TRACKS. NEITHER IS A CHANGE OF CONTROL; NEITHER ROKU NOR LEG
  APPLIES; THE QUOTE IS AN OWNER-EARNINGS PRICE.** Track one is the France-to-Luxembourg
  **cross-border conversion, COMPLETED 2026-07-29** on **Form 8-K12B, accession
  `0001628280-26-050326`** - *"the Company converted, without being dissolved, wound up or placed
  into liquidation, from being a public limited liability company ( societe anonyme ) governed by
  the laws of France ... to being a public limited liability company ( societe anonyme ) governed
  by the laws of the Grand Duchy of Luxembourg"*, one ordinary share for one, all ADSs mandatorily
  surrendered one-for-one and the Deposit Agreement terminated, same CIK, same file number
  001-36153, and *"The Conversion did not result in any material change to the Company's business,
  operations, assets, liabilities, obligations, directors or management."* **That filing is also
  the answer to what Criteo was before Luxembourg** - its cover carries *"32 Rue Blanche , Paris ,
  France 75009"* in the former-address box, so the whole twelve-year filed record is the French
  societe anonyme and the continuity is unbroken. Track two is the Luxembourg-to-Delaware merger
  signed 2026-08-05 (accession `0001628280-26-053414`) into **Criteo Holdings, Inc., "a Delaware
  corporation and wholly owned subsidiary of Lux Criteo"**, effective *"at 12:00:01 a.m., New York
  City time, on January 1, 2027"*, shares exchanged *"on a one-to-one basis"* with the same
  directors and officers continuing. No counterparty, no consideration and no premium on either
  track, so no spread is possible.
  **PASS/FAIL: FAIL AT Q2. `[E3-03]` criterion 2 - the customers have close substitutes and two of
  them have already used them.** Criteo's own Item 1 names **nine** competitors in one sentence -
  *"Amazon, Meta Platforms, Google, and Microsoft, pure play DSPs, such as The Trade Desk, pure
  play SSPs such as Magnite or PubMatic, and pure play retail SSPs such as Publicis' CitrusAd ...
  smaller, privately held companies such as Kevel or Koddi"* - after describing its market as
  *"complex, rapidly evolving, highly competitive, still fragmented and yet rapidly
  consolidating."* Client retention *"approximately 90%"* for three straight years; **four
  consecutive annual falls in client count on a single methodology, 18,990 (2022) to 16,786
  (2025)**, the `[E4-55]` shape, with the Q1 2023 methodology break disclosed and NOT smoothed
  (the pre-break 21,745 of 2021 is not comparable and the -22.8% that crosses the break is not
  quoted); **revenue -15.4% over seven years**, $2,300.3M (2018) to $1,944.9M (2025); and in Q2
  2026 *"a $21 million headwind from previously communicated scope changes with two specific
  Retail Media clients"* took **-21%** off the whole Retail Media segment, out of roughly 16,800
  clients. **The competitor row [E3-28], same metric and same window (FY2021-FY2025, each filer's
  own top line on its own basis):** CRTO **-13.7%**, The Trade Desk **+142.1%**, Magnite +52.4%,
  Taboola +38.7%, PubMatic +24.7%, Digital Turbine -24.4%; 6 of the 9 competitors Criteo names,
  with Amazon, Meta, Microsoft, CitrusAd, Kevel and Koddi unavailable and named as such. **Class
  NONE, direction NARROWING.** Q3-Q6 NOT OPENED.
  **The disconfirming case was put at full strength and refuted on the company's own MD&A.**
  Contribution ex-TAC rose from 52.5% to 60.4% of revenue over 2023-2025, gross profit +34.2% and
  operating cash flow reached a twelve-year high of $311.2M - but the MD&A says the gain came from
  *"lower traffic acquisition costs in Performance Media, related primarily to the decrease of the
  average CPM for inventory purchased"*, which is `[E3-62]`'s question about who keeps the saving
  and `[E3-51]`'s surfing run, not a moat. The FY2026 guidance now reverses it: *"We now expect
  Contribution ex-TAC to decrease -12% to -10% at constant currency."*
  **NO PRICE BAND ARMED AND NO `PORTFOLIO.md` ROW ADDED** - the QLYS ruling: a name that failed at
  Q2 failed on the BUSINESS and a price alert would be a category error. **THE REVERSAL CONDITION,
  IN WORDS:** re-open CRTO only if the client count rises for two consecutive years on one
  methodology, AND Contribution ex-TAC returns to growth without a fall in the average CPM of
  purchased inventory being the stated cause, AND no single pair of Retail Media clients can move a
  reporting segment by a fifth in one quarter. Price alone never re-opens it.
  **COMPUTATION - NOT A CLEARANCE** (Q1-Q4 do not all show IN, so this is arithmetic and no part
  of it is entry language): the `spread_caveat` was discharged by rebuilding owner earnings on
  **twelve filed years of operating cash flow (2014-2025)**, giving $74M to $98M on the five-year
  window and about $94M on an eight-year window, against the screen's $79M-$86M four-construction
  width; **`level_shift "no step"` and `best_year_dep "no single-year dependence"` both SURVIVE the
  longer window** (twelve-year mean $216.0M against five-year $254.1M, ratio 1.18), a screen flag
  confirmed rather than refuted. SBC resolves for all twelve years and peaks at 43.4% of operating
  cash flow, under the 50% that would force the grant table by hand `[E3-70]`. The empty `wc_note`
  was checked and is **not** clean - FY2025 carries +$246.0M on trade receivables against -$265.4M
  on trade payables, each about 80% of a year's operating cash flow, netting to only -$13.3M, and
  the annual-facts flag never saw either. **`acq_note` is the SEVENTH consecutive perimeter
  understatement**: the $156M it reports is the investing-cash line, while the FY2021 10-K states
  IPONWEB was bought *"for $380 million comprised of a mix of cash and treasury shares of the
  Company"*, with $74.0M of contingent consideration paid through the FINANCING section in
  2023-2024 and Lock-Up Shares expensed through share-based compensation;
  `BusinessCombinationConsiderationTransferred1` is ABSENT from CRTO's companyfacts, as the RESUME
  STATE records for CRM, CERT, MRVL and AVGO. **$380M is 46% of the hand-struck cap, not 18%.**
  Run file: `Test Runs/2026-09-21 Run - CRTO Criteo.md`.
"""

idx = s.index(head)
s = s[:idx + len(head)] + entry + s[idx + len(head):]
open(p, "w", encoding="utf-8").write(s)

lines = s.split("\n")
st = [i for i, l in enumerate(lines) if l.startswith("## COMPLETED FROM THE QUEUE")][0]
en = [i for i, l in enumerate(lines) if l.startswith("## THE WRITE-EARLY PROTOCOL")][0]
n = len([1 for l in lines[st:en] if re.match(r"^- \*\*", l)])
print("inserted. ENTRY COUNT NOW:", n)
