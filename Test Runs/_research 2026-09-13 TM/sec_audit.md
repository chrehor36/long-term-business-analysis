
---
## SELF-AUDIT (operator rule 6)
- [x] Questions answered in order; no verdict skipped. **Q1 IN → Q2 OUT → stop.** Q3 and Q4 recorded
      under explicit NOT GOVERNING banners; Q5 and Q6 headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on the
      filed segment note and the two-way statements. The PROVISIONAL label at Q2 attaches to an
      upgrade the verdict does not make.
- [x] Every UNRESEARCHED item is named with where it lives: **BYD's 2025 annual report (HKEXnews)**
      for the competitor row; **the offeror's press release** for the chairman's contribution amount;
      **Hino's own disclosure** for the US penalty amount. None bears on the Q2 verdict.
- [x] No UNKNOWABLE verdict is used.
- [x] Step 0: the filing was read, with accession numbers for ten 20-Fs (six IFRS, four US GAAP), the
      six 20-F/As of 2024-02-06, and 49 6-Ks; **consolidated operating cash ¥5,472,920M cross-checked**
      between the audited statement and the MD&A, and FY2025's ¥3,696,934M against `companyfacts`.
- [x] Owner earnings on multi-year means; **five windows published** (3, 5, 5-ex-FY2024, 7, 10
      years); (c) disclosed as a judgment with [E5-20]'s exception class applied and the D&A end ruled
      INVALID on four filed grounds; the FY2020 accounting-basis gap measured (3.5%) rather than assumed.
- [x] **SBC resolves and is complete**: filed for FY2024-FY2026, filed as zero for FY2017-FY2019,
      bounded by the shareholder-approved ¥4.0bn ceiling for FY2020-FY2023 and subtracted at the
      ceiling.
- [x] Competitor row filled: **five peers complete from SEC filings, VW and Hyundai partial from
      rung 3, BYD blocked with the obstacle named**; the metric problem (all-in vs adjusted) stated
      before the table; two peer figures re-checked by hand.
- [x] Sovereign is for the earnings currency, **from the issuing authority (Japan MOF), dated
      2026-09-10, tenor 30 years**, struck fresh twice; the choice of yen argued from the filing and
      shown not to move the floor.
- [x] Share count **read by hand** from the 20-F cover and walked through the tender result, the Q1
      FY2027 summary and the August repurchase notice; treasury and ESOP-trust shares excluded; no
      other class remains (Model AA cancelled 2021-04-03).
- [x] Value stated as a round-number range, not a point estimate.
- [x] **One bar chosen (screamer), not both. Windage count: ONE**, at the (c) judgment.
- [x] Prices dated; aggregator (Yahoo) used for the live quotes only and flagged; ADR ratio derived
      and cross-checked against the Tokyo quote; the USD cap shown for orientation only and never used
      against yen earnings.
- [x] Every judgment carries a ledger id (operator rule 8). **97 distinct ledger ids cited in this
      file, all checked against `principle_ledger.csv`: 0 phantom.**
- [x] The analyst's own incentive, checked [E4-27, E4-26]: the brief's hypothesis ("does Toyota's
      record differ?") was pursued until it produced a fact that cuts against the verdict (Toyota
      leads the volume half of the row), and that fact is stated first in the row's findings and again
      below.
- [x] `python tools/check_framework.py` **PASS** before the final commit (267 ledger rows, 0 phantom
      citations, 0 unlabelled numbers).
- [x] Run committed to git by pathspec: Step 0 `f099802`, Q1 `11bedfd`, Q2 `8203b51`, Q3-Q4 `945f675`,
      Q5-Q6 and this audit in the commit that carries this line.

## REGISTER
- **Verdict: [x] OUT (about the business).**
- **One line:** *Toyota is the best volume car company in the filed row and not a franchise: its own
  ten-year cost-reduction line nets to minus ¥645 billion, its decade of operating-income growth was the
  yen's, and the margin that leads its peers fell from 11.2% to 6.1% in two years.*
- **Work orders for any future upgrade (not for this verdict):** BYD 2025 annual report (HKEXnews,
  rung 4; the IR site returned HTTP 504); Hyundai 2021-2023 annual reports (hyundai.com, rung 3); VW
  2021-2023 absolute automotive figures (VW annual reports, rung 3).

---
# THE OUTPUT CONTRACT

## (a) THE PRICE — **COMPUTATION — NOT A CLEARANCE** (operator rule 3)
**Roughly ¥1,700 to ¥2,950 a share against the [E4-28] floor at zero growth (¥20 trillion to ¥35
trillion for the equity); roughly ¥4,250 to ¥7,350 against the bare 30-year JGB. Current price ¥3,031
(TSE close 2026-09-11; NYSE ADR $198.20 = 10 shares). Market capitalisation ¥35,807bn on 11,813,621,960
shares.** Owner earnings ¥2.0 trillion (industrial, ten-year, the bottom boundary) to ¥3.5 trillion
(five-year, with the lender's and the affiliates' retained earnings): **a 5.6% to 9.7% yield against a
4.00% sovereign.** No entry language attaches to any of this.

## (b) PASS / FAIL
# **FAIL — the file was closed by QUESTION 2.**
**Q1 IN · Q2 OUT · Q3 and Q4 recorded, not governing · Q5 and Q6 computation, not clearance.**

**The strongest single fact against this file's conclusion [E4-51]:** on an all-charges-in basis
**Toyota's automotive margin is the highest in the filed competitor row in each of the last three
fiscal years, and its five-year pooled 8.22% is above every volume manufacturer's comparable figure**
(GM 5.39% with its lender inside, VW about 5.6%, Ford 1.46%, Honda automobile −0.62%), while Honda,
Ford, Stellantis and GM wrote off their EV programmes. **GM and Ford failed Q2 at the bottom of this
row; Toyota is at the top of it.** The file's answer is that the lead is inside the charges the peers
exclude and behind GM and Stellantis on their own measures, that it halved in two years, and that
Toyota's own cost line shows the savings did not stay home. But the fact is filed, it is favourable,
and it is recorded without hedging.

### TOOLING AND DOCUMENT DEFECTS FOUND
1. **The triage's skip reason was right in effect and wrong in cause.** TM's `companyfacts` holds
   `ifrs-full` annual facts for **FY2020-FY2025 only**, because Toyota switched from US GAAP to IFRS
   with the FY2021 20-F (the US GAAP history sits under `us-gaap`, a different namespace and basis), and
   **the FY2026 20-F filed 2026-06-10 had not been ingested by `companyfacts` on 2026-09-13**, three
   months later. **The SONY run found the same ingestion lag for its FY3/26 20-F.** Two Japanese March
   filers, same gap: any screen that trusts `companyfacts` for a Japanese 20-F filer is a year stale.
2. **A basis change inside a filer's own history is invisible to a namespace-bound reader.**
   `annual()` accepting `ifrs-full` (the 2026-09-01 fix) is necessary and not sufficient: a ten-year
   window on a filer that changed GAAP needs both namespaces and a measured basis gap. The gap here
   was 3.5% of free cash in the overlap year; it will not always be small.
3. **The two-way statements moved from the audited notes (FY2021-FY2025 20-Fs) to Item 5 MD&A (FY2026
   20-F).** A parser keyed on *"NOTES TO CONSOLIDATED FINANCIAL STATEMENTS ... (iii) Consolidated
   Statement of Cash Flows on Non-Financial Services"* finds nothing in the FY2026 filing.
4. **`tools/sources.py` EUR leg failed** (`SSL: CERTIFICATE_VERIFY_FAILED` against the ECB data API);
   USD and JPY struck normally. Not needed here; the next euro filer (STLA is in WAVE 5) will hit it.
5. **Toyota does not furnish the monthly "Share Buyback Report" 6-K the SONY run recommended for
   Japanese ADRs**; it furnishes *"Notice Concerning the Status of the Repurchase of Shares"*, which
   gives the month's purchases but not the treasury balance. The treasury balance came from the
   quarterly financial summary. **The SONY method does not generalise to every Japanese filer.**
6. **`fts_count()` was not used**; every competitor naming and quote came from downloaded filings.

### DEFECTS IN THE BRIEF
1. **"The register holds 82 entries before this wave"** — the concurrent SONY run folded first, so the
   register held **83** when this run folded, and the check is 83 → 84.
2. **"the registered survival shapes (the RGTI and CNR runs list them)"** — those lists stop at eight;
   BAM added the ninth (the warehouse) and SONY the tenth (the camouflage). **And the name this run first
   drafted, "the treadmill", was already registered by the FLNC fold** for a variant of the sixth; the
   shape here is recorded as the eleventh, **THE PASS-THROUGH**.
3. **"pay [E4-52]"** — [E4-52] is the lollapalooza row; the incentives row is [E4-27] (the SONY run found
   the same defect in its brief).
4. **"ARM Arm Holdings run of 2026-09-12"** — the file is `2026-09-11 Run - ARM Arm Holdings.md` (the run
   was started 2026-09-11 and closed 2026-09-12).
5. **"a 20-F/A filed 2024-02-06 (0001193125-24-024814): open it and state what it amended"** — it is one
   of **six** 20-F/As filed that day (FY2016, FY2017, FY2019, FY2020, FY2021, FY2023), all amending only
   the Iran Section 13(r) disclosure. The pointer was accurate and incomplete.
6. **The competitor list names three non-SEC registrants (VW, Hyundai, BYD).** The F precedent treated
   them as UNKNOWABLE; the framework's evidence ladder has a rung 3 (company IR site, English), and VW
   and Hyundai were readable on it. **"Not an SEC registrant" is a rung, not a verdict.**
7. **The priors, framed to be refuted:** "GM and F failed on excess-capacity language; test whether
   Toyota's record differs" — **it differs, and still fails**: Toyota leads the volume half of the row;
   the lead is neither wide nor sustainable. "Q3: establish whether any take-private of a group company
   is live" — **not live; completed 2026-06-15**, at a net ¥3.2 trillion cash cost to TMC. **The [E2-49]
   metric-withdrawal prior: did not fire** (the FY2020 depreciation change was announced with its
   quantified effect).
