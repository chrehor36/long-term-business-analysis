## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. Inaction is the default the draft gives a file closed at Q7.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts found are under AFTER THE STOP.

---
## THE BOX
**OUT at Q7**: no case of the range earns the floor of about ten percent at US$44.17 per ADS (central growth case 4.2% at the
price); central value range US$37.59 to 91.53 per ADS (US$3.759 to 9.153 per ordinary share) at the 2.06% RMB 30-year, the price
inside it; fair price US$14.08 per ADS all-equity (US$9.87 equity-only). Q1 IN, Q2 IN narrowly, Q3 for, Q4 no STOP and against,
Q5 integrity IN and ability for, Q6 against on both parts.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box unchanged (operator rule 2) **[M1997-127]**.
- **Q8 (the bond and the alternatives).** The RMB 30-year was 2.06% on 2026-10-14 (Step 0). Owner cash before interest on the
  enterprise value of RMB 87,135 million: 1.7% on the cycle average (1,507), 4.6% on the literal five-year average (3,992), 8.1% on
  2025 alone (7,020). The company's own repurchases in 2026 were made at about US$44.4 per ADS (Q6).
- **Q9 (debt and exposures).** Borrowings RMB 4,226 million at 2026-06-30, plus the CNY 3,350 million 2.25% bonds due 2031 issued in
  September 2026 (6-K 2026-09-16, `0001104659-26-108062`); finance-lease liabilities RMB 2,993 million; cash, restricted cash and
  short-term investments RMB 15,706 million, of which RMB 1,406 million was pledged against a RMB 1,400 million one-year loan at
  2025-12-31 (20-F Item 5.A). Operating-lease liabilities RMB 27,015 million; rent RMB 4,179 million in 2025 (16.5% of revenue);
  584 leases, 68 of them expiring in 2026 (Item 4.B). In 2020 to 2021 hotel closures "may amount to an event of default under
  certain of our banking arrangements. We have managed to obtain the required waiver" (FY2021 20-F, Item 3.D): the one time the
  lenders could have called the tune, they were asked and agreed. A RMB 400 million syndicated loan carries "financial covenants
  including revenue and profit related to this facility" (Item 5.A). In 2026 the group undertook, with another shareholder of Azure
  Capital, to "provide funding support" for a repurchase of the units of a REIT of about RMB 1,239 million if the originator is
  found to have committed material violations in the issuance documents (interim report 6-K 2026-09-23, related-party note). The
  holding company depends on PRC subsidiaries' dividends; RMB 4,269 million of PRC net assets were not distributable (Item 5.B);
  the PCAOB inspection and HFCA Act risk and the PRC regulators' "authority to exert influence" are stated in Item 3.D.
- **Q12 (how the money is made).** Hotels under the group's brands; none of the businesses the rows name (casinos, tobacco,
  distributor-loading schemes, gambling dressed as investing, promotion on a borrowed reputation) was found in Item 4.B.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Declared: the
      first commit (the copy, the position note and the contamination line) was made after `tools/run.py` and
      `Screens/cover_shares.py` had run and the first filings had been fetched; the copy itself was made before any fetch. Step 0 was
      committed with Q1, and the Q6 buyback line with Q7, as the brief asks.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and named the dispatching session as holder of the
      lock; I did not write or check the lock. The run binds only once folded into the register.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Breach, declared:** to check that this
      run's file name was free I ran a listing of `Test Runs/` filtered to the date 2026-10-14, which showed the names of other runs
      of that date (CHH, H, HGV, HLT, MAR, WH and four steel names) and their research folders; none was opened or searched, and
      nothing from them is used. The commit subjects of the H (Hyatt) run seen in the session context are declared under
      contamination at the top. Marriott's and Hilton's figures were taken from their own 10-K XBRL facts on EDGAR.
- [x] Every v5 id resolves (`_research 2026-10-14 HTHT/scripts/check_cites.py`: no E-ids, every M, L and R id found in
      `principle_ledger_v5.csv`, every attached quoted fragment found in its row); every filing fact has its accession; the
      numbers without a row are filed figures or are labelled CONVENTION of this run (the 25% interest add-back rate, the euro
      earnings carried in RMB, the maintenance guess, the cycle years, segment revenue growth as organic growth).
- [x] The order was kept; Q7, the first STOP that failed, closed the run; the sensitivity under Q7 is headed COMPUTATION, NOT A
      CLEARANCE and is not a case of the range.
- [x] Owner cash after every real cost, from operating cash flow less stock pay, all capital spending, finance-lease principal
      and minority dividends, never a net-income proxy; the sovereign from the Ministry of Finance's curve as published through
      ChinaBond, its compiler, because the MOF's own page failed (Step 0); the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found (foundations, Q2, Q7 sensitivity); facts for later questions are under
      AFTER THE STOP. Q5 was reached and answered, so no integrity flag is owed in the box line.
- [x] Not a point-in-time run; no anchor-date restriction applies.
- [x] `tools/run.py` refused the name (no RMB source, currency mismatch); none of its output was used.
- [ ] `python tools/check_framework.py` PASS before the commit: see the final commit; the result is recorded in the reply.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Five things. (1) **Specific (a) with one cycle.** The window's first year is aberrational (COVID), so the base is a cycle average,
but the filings hold only one full cycle, so "the growth is measured between the averages of successive cycles" cannot be done,
and the text gives no fallback for that case; I built the growth case on the organic rate (the serial-acquirer rule required the
organic pair anyway) and said so. The cycle average also mixes a business a third of today's size (2019) with today's, after a
structural shift to franchising and a doubling of revenue; the text has no way to scale a cycle base for such a change, and the
choice swings the fair price from US$14 (cycle) to about US$38 (post-COVID sensitivity), though not the box, since every rule case
and the literal window fail the floor. (2) **"Peak to peak"** does not say whether both peak years are in the average; I used the
years after one peak through the next and showed the other reading. (3) **The serial-acquirer rule** is named for a habit but is
triggered by a single deal (Deutsche Hospitality was 83% of the window's purchases); I applied it as written. (4) **The sovereign
table and `tools/sources.py` have no RMB source**, the Ministry of Finance's own curve page was dead, and the curve was taken from
ChinaBond's MOF page; a RMB row in the protocol's table would fix the source for the next Chinese filer. At 2.06%, the range at the
sovereign sits far above every case valued at the floor, so for low-rate currencies the width test and the floor test point in
different directions; the floor-first rule decided it, as written. (5) **`tools/run.py` cannot take an ADS quoted in US dollars
for an RMB earner** (it refuses to convert and the home line is in HKD); all arithmetic was done by hand from the filings, which
the brief anticipated.
