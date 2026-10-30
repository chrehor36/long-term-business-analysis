---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, **Q2 OUT (closes)**; Q3–Q6 recorded under explicit
      "RECORDED, NOT GOVERNING" banners; the price under COMPUTATION — NOT A CLEARANCE with no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 does not rely on the Dell'Oro share. Q2's
      row has one same-metric radio peer (Nokia) and says so; the verdict turns on criterion (2) and [E4-04], answered by both
      vendors' filed statements of customer behaviour, not on the row's completeness.
- [x] Every UNRESEARCHED verdict names the artifact — none used.
- [x] Every UNKNOWABLE verdict states what cannot be known — Q3 (recorded): the DOJ Iraq conclusion, the ATA ruling, the CFIUS
      NSA findings, none yet in existence.
- [x] Step 0: the FY2025 20-F was read (the 20-F body; Exhibit 15.1 Board of Directors' Report, statements, Notes A1–H6, risk
      factors, APMs, Remuneration Report; Exhibit 2.3), accession `0001193125-26-104149`; 20-Fs FY2013, FY2016–FY2024 for segment,
      cash-flow, SBC, legal and target history; the 2018 20-F/A read for its purpose (*"Submit the Interactive Data File … Correct
      typographical errors in Item 3.A"*); 49 6-Ks since 2025-10-01 and 11 legal-milestone 6-Ks 2019–2024. **Cross-check:** 2024
      OCF SEK 46,261m = filed statement = companyfacts (two accessions) = Board of Directors' Report text.
- [x] Owner earnings on multi-year means; five windows; (c) disclosed as a judgment with the default named and the exception class
      tested and not applied (capex 1.03–1.15x D&A over ten and fifteen years); the lower of the two ends used; the working-capital
      release removed at the low end [E4-41]; **SBC resolves and is complete** (share-settled subtracted every year 2011–2025;
      cash-settled already in OCF); lease repayments restored as a cost from 2019 (CONVENTION, stated); capitalised development in
      (c), acquired-intangible amortisation outside it and acquisitions displayed on their own line; **the Vonage (2022) and iconectiv
      (2025) perimeter moves named** — the windows are consolidated, not pro-forma, and say so.
- [x] Competitor row filled: Nokia (same metric, 2014–2025, boundary named each year), Huawei, ZTE, Samsung, Ciena, Cisco with
      their limits; transcriptions in `peers/NOKIA_row.md` and `peers/OTHERS_row.md` with accession numbers and URLs.
- [x] Sovereign for the earnings currency (SEK, argued from [E4-15, E3-32] on a 99%-foreign sales base; USD and EUR shown), from the
      issuing authority (Sveriges Riksbank SWEA, cross-checked to the Debt Office's 2026-09-09 auction), dated 2026-09-11; **tenor
      10 years, shorter than 30, stated**; fetched by hand, `tools/sources.py` untouched.
- [x] Share classes read before summing (Exhibit 2.3, Note E1: equal dividend and net-asset rights, 1 vs 1/10 vote; C shares none);
      treasury excluded; the 20-F cover's issued count caught and not used; ADR ratio from the 20-F cover and derived-checked at the
      Riksbank fixing; cap in SEK from the Stockholm quote, never the USD ADR.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar (screamer); windage count stated: one.
- [x] Prices dated; aggregator used for live quotes only and flagged.
- [x] Ledger ids checked against `principle_ledger.csv` with `ids.py` on every section before splicing (none missing); quotes of
      [E5-22], [E2-68], [E5-33] and [E2-57] re-read in the ledger rows before use. [E4-27] used for pay, [E4-52] only for converging
      flags.
- [x] Run committed to git with a pathspec, section by section.

**Errors caught in this run before commit, recorded rather than hidden:** (1) Q3's first draft gave ROE as 21.5% / 14.0% / (27.0)% /
0.0% / 26.0% without computing it; recomputed on total equity as 23.9% / 15.9% / (22.6)% / 0.4% / 28.3%. (2) Q3's first draft put
Enterprise EBIT losses 2020–2024 at SEK 76bn; the arithmetic is SEK 71.6bn. (3) Q2's first draft summed CSS EBIT 2020–2025 as SEK
4.9bn; it is SEK 0.6bn. (4) Q2's first draft wrote that AT&T's radio business moved from Nokia **to Ericsson**; neither filing
names the vendor in terms, so the sentence now says only what each filing says. (5) Q4's first draft said sales "fell from SEK
222.6bn to 236.7bn" — that is a rise; corrected. (6) Q4's first draft put 2016–2018 restructuring at SEK 29.9bn; it is SEK 24.1bn,
and a per-share dividend history written from memory (SEK 3.70 → 1.00) was removed and replaced by the filed cash dividends. (7)
Q3's first draft paraphrased [E5-22] inside quotation marks; replaced with the ledger's verbatim sentence. (8) Q3's first draft
claimed the Economic Profit pay design was "the only capital-aware pay design in the recent WAVE 5 files" without checking those
files; deleted. (9) Q4's first draft put share-settled SBC at "0.2–6% of OCF"; 2017 is 9.2%.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Ericsson is the leading radio-network vendor outside China — Networks 64% of sales at a 20.4% margin ex-restructuring
  in 2025, 6–18 points ahead of Nokia in every year since 2018 — but its customers dual-source, re-price yearly without committed
  volumes or prices, swap installed networks at modernisation and will re-tender at 6G, so [E3-03] criterion (2) fails and
  [E4-04] excludes a position rebuilt each generation; Q2 OUT on the business as constituted. Price SEK 98.66 × 3,265,683,059 =
  SEK 322.2bn against owner earnings of SEK 10.6–23.9bn (3.3–7.4%), a 3.23% SEK 10-year bond and a ~10% floor; above the whole
  no-growth value range (COMPUTATION — NOT A CLEARANCE).
- **The strongest single fact against this conclusion:** the margin gap against the only same-metric Western peer has widened from
  zero in the late-4G years to 17.6 points in 2025, and Nokia's own filing says *"Competitive dynamics in the CSP industry strongly favor the top
  two vendors"* — a two-vendor Western market with the low-cost vendors excluded by governments may behave like a franchise for as long as
  the exclusion lasts. The file's answer: the exclusion belongs to the regime [E2-59], the customers still dual-source and re-tender,
  and the position must be re-won at 6G before 2030.
