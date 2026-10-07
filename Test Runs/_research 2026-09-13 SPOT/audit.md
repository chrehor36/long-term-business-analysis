---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, **Q2 OUT (closes)**; Q3–Q6 recorded under explicit
      "RECORDED, NOT GOVERNING" banners; the price under COMPUTATION — NOT A CLEARANCE with no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 states the filing's one limit (no royalty
      total) and does not rest on the $11bn headline. Q2's OUT does not rest on the three undisclosed rivals.
- [x] Every UNRESEARCHED verdict names the artifact — none used. The one test first logged as a work order (the 2022 Investor
      Day goals, [E3-48]) was performed in the same run from the company's transcript (rung 3) before commit.
- [x] Every UNKNOWABLE verdict states what cannot be known — Q4 (recorded): the terms of the next major-label licence cycle,
      which are confidential and unfiled.
- [x] Step 0: the FY2025 20-F was read (Items 3.D in part, 4, 5 in full, 6 in part, 7.A, 8, 10 in part, 11, 16C; the
      statements; Notes 4, 5, 7, 8, 9, 10, 12, 16–27; Exhibit 1.1 Article 9), accession `0001628280-26-006874`; 20-Fs FY2018–FY2024
      for cash flows, segments, subscribers, ARPU, social-cost accruals, equity, acquisitions and ownership; the Q1 and Q2 2026 6-K
      interim reports; 24 shareholder-update 6-Ks 2019–2026; the AGM, buyback-upsize and board 6-Ks. **Cross-check:** 2025 OCF
      €2,933m = filed statement = MD&A table = Q4 2025 update = companyfacts.
- [x] Owner earnings on multi-year means; **four windows** (5-year default, 3, 2, 10) plus the twelve months shown only at Q5;
      (c) disclosed as a judgment, D&A default valid and not in the [E5-20] class; lease principal restored after IFRS 16
      (CONVENTION, stated); working capital removed at the low end; cash tax normalised at the low end; **SBC resolves and is
      complete every year 2016–2025; the share-linked social costs are found in both places (Note 5 and Note 20 accruals; quarterly
      amounts in the updates), kept inside OCF, and the accrual change subtracted at the high end.** Negative years named.
- [x] Competitor row filled: Tencent Music, Pandora/SiriusXM, Deezer with figures; Apple Music, YouTube Music, Amazon Music with the
      filings read and the non-disclosure quoted; three suppliers (WMG, UMG, Sony) with both sides' pricing-power language.
- [x] Sovereign for the earnings currency (EUR, argued from [E4-15, E3-32] on a 37.6%-US, 62.3%-rest-of-world revenue base; USD
      shown), from the issuing authority (ECB SDW, SR_30Y), dated 2026-09-10, struck fresh twice. **Cap converted to euros at the
      ECB reference rate of the quote date before meeting euro earnings; nothing mixed.**
- [x] Share count by hand: cover figure proven to be OUTSTANDING (issued − treasury); latest 6-K count used; beneficiary
      certificates read in the articles (no dividend, distribution or liquidation right) and excluded; options, RSUs, warrants (none)
      and Exchangeable Notes (repaid in cash) stated; no ADR.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar (screamer), computed only; windage count stated (two, justified).
- [x] Prices dated; aggregator used for live quotes only and flagged.
- [x] Ledger ids checked against `principle_ledger.csv` before splicing (all present); the quoted fragments of [E3-43], [E3-46],
      [E2-53], [E2-44], [E3-50], [E2-30], [E4-13], [E4-28], [E4-35], [E4-44], [E2-63] matched in the ledger text. [E4-27] used for
      pay, [E4-52] only for converging flags.
- [x] Run committed to git with a pathspec, section by section.

**Errors caught in this run before commit, recorded rather than hidden:** (1) Step 0 first wrote the founders' stake as "23.2% of
the capital"; that double-counts the Tencent shares Ek votes by proxy — corrected beside the line (15.1% economic). (2) Q4's first
draft put the 2018–2023 Premium cost-of-revenue mean at 71.4%; it is 72.0%, so mechanism 1 costs €874m (34%), not €783m (30%).
(3) Q4's first draft said high-end owner earnings averaged €54m a year 2016–2023; the arithmetic is €75m. (4) Q4's first draft
gave OCF 2016–2025 as €7,757m; it is €7,777m. (5) Q4's first draft summed the near-term requirements at €2.2bn and 4.3×; with the
four-year RSU tax taken whole it is €2.4bn and 3.9×. (6) Q4's first draft said ARPU without the price effect "falls 1.3% instead
of 1%"; it falls 6.6%. (7) The Q4 working note first said the five-year social-cost accrual change netted to −€12m; it is +€48m.
(8) Q3's first draft wrote that the founder "has not sold"; the two 20-F ownership tables show the founders' holdings fell by
about 1.48M shares in 2025 — rewritten. (9) Q3's first draft said revenue growth was inside the 2018 25–35% band in three of seven
years; it is one (2019). (10) Q2's first draft attributed the "65 countries" price sentence to WMG's FY2024 10-K; it is FY2023.
(11) Q2's first draft called Spotify "the largest subscription service throughout 2016–2023" without a filed source; replaced by
the 20-F's own words and UMG's. (12) Q5's first draft gave revenue growth of 17% a year; the nine-year rate is 22%. (13) Q5's first
draft counted windage at one place and called the working-capital removal the source's instruction; it is two places, justified.

**Brief and tooling defects found:**
- **Brief:** "the issued-versus-outstanding trap ERIC found" — **checked, does not fire**: Spotify's cover count is outstanding.
- **Brief:** "the SONY run has a music competitor row with UMG and WMG" — correct and reused; but **the label side's decisive
  sentence for criterion (2) is UMG's ("DSP providers generally make all content available"), not in the SONY file's summary.**
- **Brief:** "Tencent Music (files a 20-F)" — correct, but **companyfacts has ingested TME's FY2025 20-F for one dei fact only**
  (no FY2025 financial facts): the lag cause from RESUME STATE §9 is live for TME.
- **Brief:** asked for the social costs "which Spotify books separately" — **the 20-F does not itemise the share-linked social
  charge**; only the accrual (Note 20) and the total payroll-tax line (Note 5) are audited; the quarterly amounts are in the
  furnished updates. Stated, not smoothed.
- **Tooling:** `tools/run.py SPOT` → *"no overlapping OCF/D&A/capex annual facts"* although ten EUR IFRS years exist — the USD-unit
  filter and US-GAAP tag names (RESUME STATE §9), reproduced on the cleanest case of the three causes.
- **Tooling:** `tools/sources.py` `_chart(ticker)` returns `chart.result[0]` already, so a caller indexing `['chart']` fails —
  not a defect in the tool, a trap for scripts; noted.
- **Unreconciled (from the peers file):** TME's 20-F says 8,552,440 Spotify shares went to TME Hong Kong in 2017; Spotify's 20-F
  lists 4,276,200 held there at 2025-12-31. Not material to this run's count (Spotify's outstanding count is its own).

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Spotify rents the same non-exclusive catalogue its rivals sell — its largest supplier says every service carries
  all content and a listener needs one subscription — so criterion (2) of [E3-03] fails; the licences are renewed every one to
  three years from owners who take 50–64% of each price rise; and five years of price increases produced high returns on capital
  in two. **Q1 IN · Q2 OUT · Q3 (recorded) IN, no disqualifier, live buyback and incentive flags · Q4 (recorded) survives,
  owner earnings UNKNOWABLE on a €95m–€2,186m range, named death THE TENANT · Q5 COMPUTATION — NOT A CLEARANCE: US$525.75
  (€453.55), cap €93.2bn, yields 0.2%–3.2%, above every construction at the floor and the sovereign · Q6 (recorded) reopening
  conditions written.**
- **PASS/FAIL: FAIL — closed at Q2 (OUT, on the business as constituted).**
