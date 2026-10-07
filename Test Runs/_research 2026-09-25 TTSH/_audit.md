## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 OUT; Q3-Q6 not scored, per the hard sequence)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q1 rests on the 10-K's own Item 1 and MD&A)
- [x] Every UNRESEARCHED verdict names the artifact: none issued
- [x] Every UNKNOWABLE verdict states what cannot be known: none issued; the [E4-04] perimeter close was considered at Q2
      and refused, with the reason given there
- [x] Step 0: the filing was read, with accession number (10-K FY2025 `0001552800-26-000006`); figures cross-checked
      (FY2025 OCF 5,792; SBC 1,282; 2022 payables (8,057) against OCF 2,715; FY2017-2019 OCF and capex against the 10-K
      FY2019; Floor & Decor's FY2025 operating income 270,070 against its 10-K)
- [x] Owner earnings on a multi-year mean; four windows stated; capex band disclosed as a judgment (beneath the close, not
      scored)
- [x] Competitor row filled: 5 filers of about 10; Floor & Decor's figure read from its 10-K, the other three flagged XBRL;
      the unavailable peers named (Daltile inside Mohawk, unsegmented; MSI, Arizona Tile, Bedrosians, Porcelanosa private)
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (US Treasury 30 Yr 5.47%, 09/24/2026; FRED
      not used)
- [x] Value stated as a round-number range, not a point estimate (computation only, not a clearance)
- [x] One bar: none chosen, because Q5 was not opened; windage count stated for the computation (one)
- [x] Prices dated; aggregator used for the live quote only and flagged (Yahoo chart endpoint, OTC Markets OTCPK, raw
      response saved)
- [x] Run committed to git with pathspecs (commits listed in the register)

**Ledger ids.** The run file cites 47 distinct ids; every one resolved against `principle_ledger.csv` (311 rows by
`csv.DictReader`) before the fold. Verbatim quotations of [E3-03], [E3-43], [E3-74], [E4-37], [E4-55], [E2-44], [E2-45],
[E3-46], [E4-32], [E3-61] and [E3-28] were read from the ledger's `quote_verbatim` column before use. No new ledger row, no
edit under `Framework/`.

**The brief's priors, each tested:**
- **`cap_flag` (cap below filed float, "one of the two is wrong"): REFUTED as to error, EXPLAINED as to cause.** Both
  figures were right at their own dates; the float was struck at $6.36 on Nasdaq on 2025-06-30, the cap at about $2.52 on
  OTC Pink on 2026-09-02, with a delisting and an 11% share reduction between them. **Status confirmed**: no longer
  exchange-listed, no longer SEC-reporting; the price is a thin OTC Pink Limited print on a dark issuer.
- **`wc_note` (payables moved 297% of 2022 OCF): arithmetic CONFIRMED, inference REFUTED.** Payables were a $8.1M use, and
  the four current working-capital lines together a $34.7M use; the third instance of this flag firing against a total
  working-capital use (after CAH and DMC).
- **`best_year_note` ("two years jointly carry the window"): CONFIRMED and named**: 2020 and 2023, two inventory
  liquidations, 41.8% of the nine-year OCF sum.
- **`level_note_oe` ("early half straddles zero"): CONFIRMED** (2013 and 2018 negative at the capex end; 2018 is the
  screen's -$19.8M exactly). **`flags_disagree`: EXPLAINED** (OCF positive every year, owner earnings not).
- **`deal_note` and `name_change_note` empty: the blind spot CONFIRMED.** A Rule 13e-3 going-private transaction (SC 13E-3,
  Form 25, Form 15) closed in December 2025 and the screen's deal column did not see it. No deal is live; the quote is not a
  spread.
- **SBC: RESOLVES 14 of 14 years (2012-2025) and COMPLETE** (cash-flow add-back equals the restricted-stock expense in
  Note 9).
- **"A controlling holder" and "a history of deregistration/relisting questions": CONFIRMED** (the 2019 attempt, the
  Chancery action and settlement, the 2021 relisting; insiders and affiliates at about 73% after the 2025 cash-out).
- **Brief errors: none verdict-bearing.** Its commit trailer (`Claude Opus 5 (1M context)`) differs from the session's
  attribution instruction (`Claude Opus 5.5`); I followed the brief for consistency with the DMC fold and record the
  difference here, as DMC did.

**Tooling defects found (not patched; no tool may add a number, and fixing is the operator's call):**
1. **`cap_flag` cannot see a delisting between the float date and the cap date.** It compared a current OTC cap with a
   float struck at a prior Nasdaq half-year price and called one of them wrong.
2. **`deal_note()` / `deal_filings()` missed a completed Rule 13e-3 transaction** (SC 13E-3 and amendments, Form 25, Form
   15-12G), the third blind spot after WS and DMC. A screen row for a company that has filed Form 15 should say so.
3. **`working_capital_flag()` fired against a total working-capital use** for the third time (CAH, DMC, TTSH): it reads the
   size of one line against OCF and not the line's sign relative to the total.
4. **`run.py` priced on the 2026-09-25 intraday print** (1,158 shares) and carried a 3-year yield without any note that the
   issuer has stopped reporting; the cover count it used (2026-02-23) is the last one that will ever be filed.

**My own errors (four caught before commit; the fourth partly reached commit `0800dac` and is recorded, not rewritten):**
1. I first summed dividends and repurchases since 2017 as about $117M; the filed lines sum to **$134.1M**. Corrected.
2. I first wrote that the 10-K's five-year table "leads with" Adjusted EBITDA; it carries it among other rows. Corrected.
3. Two phrases in the Q2 counter-case drew on general knowledge (a housing market "weakest ... in decades", a pandemic
   remodelling wave "that lifted every peer"); both were replaced with the filing's own words and the row's own figures
   before the Q2 commit.
4. The Step 0 text listed footnotes and the FY2019 10-K as read before I had read them. I read Notes 5, 6, 13 and 14 and
   the FY2019 cash-flow statement before commit `0800dac`, **but the list's "equity" item went into that commit unread**:
   the equity statements were read at Q2 and Note 9 beneath the close, both later in this run. The claim is true now and
   was not true when first committed; recorded here rather than by editing the committed text (operator rule 6).
5. A sentence in the beneath-the-close header said the template's Q3-Q6 boxes were left below after I had replaced them;
   corrected in the audit commit. One line of my own prose carried em dashes; restructured.

**The honest record (operator rule 7).** Nothing in this run bears on whether the framework beats the market; that claim
remains UNPROVEN.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line: FAIL at Q2 (OUT, on the business). A specialty tile retailer whose own 10-K says "The barriers of entry into
  the retail tile industry are relatively low", with operating margin 2015-2025 mean 4.5% falling to -1.7%, return on
  equity mean 7.0%, and below Floor & Decor every year since 2017. It went dark in December 2025 (reverse split cash-out
  at $6.60, $32.2M paid; Form 25, Form 15; OTC Pink Limited); the FY2025 10-K is its last report. Price $2.01 (close
  2026-09-24, OTC, aggregator, flagged) x 39,821,741 shares (10-K cover, `0001552800-26-000006`) = cap $80.0M; sovereign
  5.47% (US Treasury 30 Yr, 09/24/2026).**
- Work order: none. Unknowable: none.
