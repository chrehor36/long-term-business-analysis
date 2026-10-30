# BRIEF: resume the BN run (Brookfield Corporation), overnight cycle 2026-09-13 05:35 EDT

You are resuming a company run that was KILLED BY A SESSION LIMIT, not by an error. Nobody is awake to
answer questions. Work from disk, write early, commit after every gate, and finish.

## 0. WHAT SURVIVED ON DISK (do not refetch what is here)
- **Run file:** `Test Runs/2026-09-13 Run - BN Brookfield Corporation.md` (41,567 bytes, last written
  01:39 EDT). COMPLETE in it: the priors, Step 0 (sovereign 5.35% USD dated 2026-09-11 with the
  multi-currency disclosure; 40-F `0001001085-26-000006` and Q2 6-K `0001001085-26-000021` read;
  price $38.22; count 2,297,678,581 economic common incl. 65,327,130 BWS exchangeables; cap $87,817M),
  and **Q1 IN** (committed as `bd810b8`). **Q2 onward is the blank template.** Continue from
  `## Q2 - IS IT A FRANCHISE?`. Do not rewrite Step 0 or Q1; if you find an error in them, record a
  dated correction beneath, never an edit (operator rule 6).
- **Research folder:** `Test Runs/_research 2026-09-13 BN/`. BN 40-Fs FY2022-25 (`40F_*`), the AIF,
  the FY2025 annual report 6-K/A text (`6KA_AR2025_annualreport.txt`), Q2 2026 6-K (`6K_Q2_2026.txt`),
  eleven 2026 6-K exhibits incl. the Q2 release and the combination circular
  (`6K_20260605_ex993_circular.txt`, with `circular_extract.md`), BWS 20-F FY2025 and Q2 6-K,
  `frag_step0.md`, `frag_q1.md`.
- **Three competitor-row research files written by the killed session's sub-agents. They are DRAFTS
  from a killed session: verify every figure you use against the saved filing text before it enters
  the run file.**
  - `peers_am/competitor_row_asset_managers.md` (BAM FY2021-25 fee rates and SBC, peers' 10-Ks for
    APO, ARES, BX, CG, KKR, OWL, TPG saved; the peer sections may be incomplete; check).
  - `peers_ins/competitor_row_annuity_insurers.md` (marked COMPLETE: BWS vs APO/Athene, KKR/Global
    Atlantic, CRBG, FG; spread, cost of funds, affiliated-manager share).
  - `peers_real/competitor_rows_real_assets.md` (INCOMPLETE: only the BPY subject section was written;
    BXP, SLG, SPG, VNO 10-Ks FY2023-25 are saved but not tabulated; no BIP, BEP or BBUC row at all).
- **The sibling run, finished 2026-09-13:** `Test Runs/2026-09-13 Run - BAM Brookfield Asset
  Management.md` and its COMPLETED entry. It is EVIDENCE about one of BN's components (a nine-peer
  fee-rate row, each figure checked to the peer's 10-K). It is not BN's verdict. BN owns 74% of BAM
  plus BWS, BIP, BEP, BBUC, BPG and the corporate balance sheet; the question at Q2 is asked about the
  business the BN share owns. Decide yourself how BAM's filed row bears on it and say why.
- **A lesson from the BAM resume, which had the same kind of drafts:** the killed session's drafts
  contained lines that presupposed a Q2 outcome, including a thin-evidence Q4 IN. Nothing a killed
  session wrote is a finding until you have checked it.

## 1. READ FIRST
1. `CLAUDE.md`, then `Framework/THE FRAMEWORK v4.md` in full (it governs; Q2 is lines 105-208).
2. `Framework/SECTOR METHOD - owner earnings for insurers and float-bearing holding companies.md`
   (BWS is float-bearing; BN equity-accounts it today and consolidates it after the combination).
3. `Framework/v4/THE MANAGER STANDARD - Q3.md` if you reach Q3.
4. The run file itself, top to bottom, before writing.
5. Precedent holding-company and insurer runs, for how Q2 was asked of a multi-component owner:
   `Test Runs/2026-09-02 Run - BRK Berkshire Hathaway.md`, `... L Loews Corporation.md`,
   `... GHC Graham Holdings.md`, `... HHH Howard Hughes.md`, `... WTM White Mountains.md`,
   `... MKL Markel Group.md`. Read how each built its competitor row per component and what it did
   where a component had no row.
6. `Screens/WATCHLIST RUN QUEUE.md`: the section `## THE FOLD` (six steps), `## WRITING A BRIEF`
   (the CGNX prohibition and the 8-K EX-99.1 companion rule for Q3), and the BAM COMPLETED entry as a
   model of the register fields.

## 2. STANDING INSTRUCTIONS
- **Hard sequence.** Q2, then Q3, then Q4. STOP at the first question that is not IN. UNRESEARCHED and
  UNKNOWABLE both close the file. Ask aloud on every non-IN verdict: "Can I name the document that
  would resolve this?" A gate marked IN that carries "unverified", "provisional" or "general
  knowledge" is UNRESEARCHED. Where a competitor's data is unavailable the moat class is PROVISIONAL.
- **The queue's output contract:** every run ends with A PRICE and A PASS/FAIL LINE. If the file closes
  before Q5, later questions may be RECORDED beneath an explicit "recorded, not governing" banner (as
  BAM, RGTI and CVX did), and the price is given under the heading `COMPUTATION — NOT A CLEARANCE`
  with no entry language.
- **Sovereign:** re-strike from the US Treasury daily par yield curve (`python tools/sources.py` or
  `sources.sovereign("USD")`), dated. Today is Sunday 2026-09-13, so 2026-09-11 is expected; record
  what you actually get. Do not inherit 5.35% from this brief.
- **Price:** re-strike and date it (aggregator, flagged). Check for any 6-K filed after 2026-09-04 that
  changes the count (EDGAR submissions for CIK 0001001085).
- **Owner earnings, if you reach Q4 or compute a price:** never DE, never FFO, never a net-income
  proxy. Q1 already recorded that DE adds back SBC, counts BWS DE that BN does not receive, counts
  distributions rather than owner earnings, and counted a $1,000M related-party gain. Build by
  look-through from each component's own filing, at BN's share, with (c) disclosed as a judgment and
  capital-intensive components (utilities, midstream, real estate, renewables) handled under [E5-20]
  where their own filing says depreciation understates renewal. **Verify SBC resolves and is complete
  at every component** (BE's did not resolve; Boeing's stock-settled 401(k) sat under a tag no SBC
  element contains). **Rebuild the width over every window and both (c) ends; report dollars and a word
  wherever the bottom sits near or below zero.** No five-year window on one perimeter exists (Q1
  dated the perimeter changes): say so rather than splice. Where the combined range is too wide for a
  conclusion, that is the verdict [E4-25].
- **Deal-shaped facts:** the BN/BWS combination (one-for-one exchange, shareholder-approved
  2026-07-16, closing expected by year-end subject to regulators), the Series 51/52 preference
  redemption for 2026-11-01, the Oaktree close 2026-08-03. Read what each does to the count, the
  perimeter and the quote. A live merger can make a quote a spread rather than an owner-earnings price
  (the ROKU lesson); decide whether that applies here and say why.
- **Division of labor (operator rule 8):** arithmetic by script (write scripts to the research
  folder; bash heredocs containing apostrophes fail in this environment); every judgment cites a
  ledger id from the framework.
- **Write-early:** append each section to the run file as it closes. **Commit after every gate with a
  pathspec:** write the message to a fresh file in the research folder, then
  `git commit -F "<msgfile>" -- "<path>" "<path>"`. Never `git add X && git commit` without a
  pathspec. Never `git push`, `rebase`, `reset --hard`, or force. Do not delete files you did not
  create. Trailer on every commit: `Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`.
  Stage new research files you rely on with `git add -- <path>` then commit with the same pathspec.
- **No em dashes in your own prose, commit messages or log text.** Verbatim quotes keep theirs, and the
  heading `COMPUTATION — NOT A CLEARANCE` is literal.
- Never present the framework as proven to beat the market (operator rule 7).

## 3. THE PRIORS I AM MOST LIKELY WRONG ABOUT - argue against me [E4-26]
1. **That Q2 can be asked component by component and then combined.** A holding company's franchise
   question may belong to the whole (the allocator, the GP control, the fundraising access) rather than
   to the sum of the legs, or the legs may carry it and the parent add nothing. The BRK and L runs chose
   differently. I do not know which structure the filings support for BN; decide from the evidence.
2. **That the three draft rows are the right peer sets.** Real estate peers of an unlisted, 100%-owned
   BPG with heavy fund-level debt may not be BXP, SLG, SPG and VNO. BIP, BEP and BBUC have no row yet;
   decide whether they need one, and if a component lacks one, whether that makes the class PROVISIONAL.
3. **That the BAM row transfers.** BN receives BAM's distributions and 100% of mature-fund carry, and
   is itself one of BAM's largest clients through BWS. The economics BN owns of the fee engine may not
   be BAM Ltd's economics.
4. **That the insurer is a component to be graded on spread.** [E2-70] says the only products are
   promises; the SECTOR METHOD grades cost of float. Decide which measure the corpus supports for BWS
   and use one specification across the peers.
5. **That Step 0's USD sovereign choice is harmless** (42% of common equity is non-USD). It was disclosed
   as unresolved; do not re-litigate it unless a Q5 number depends on it.

**Assume this brief contains at least one error. Every brief in this queue has. Report any you find in
the run file and in your final message.**

## 4. FINISH: THE SIX-STEP FOLD, done by you
1. Entry in `## COMPLETED FROM THE QUEUE` in `Screens/WATCHLIST RUN QUEUE.md` (insert at the TOP of the
   list, above BAM): price, share count with the document and accession it came from, cap, sovereign,
   PASS/FAIL line naming the question that closed the file, and the reversal condition in words if it
   failed on the business. Match the BAM entry's fields.
2. Strike `BN` in the MINI BERK roster (`~~BN~~` with a one-line annotation). Search the WHOLE file for
   other places that still describe BN as unrun or BLOCKED and add a dated note beside each, never an
   edit of the old text.
3. The narrative fold into `Screens/2026-08-31 PREPPED READING LIST (operator lists).md` (see how BAM was
   folded there): findings, refuted priors, tooling or brief defects.
4. `tools/alerts.json` bands and a `PORTFOLIO.md` row **only if Q1-Q4 all returned IN.** Otherwise
   touch neither.
5. `python tools/check_framework.py` must PASS before the fold commit. Fix the cause if it fails.
6. Commit with a pathspec.

Complete the SELF-AUDIT and REGISTER sections of the run file before the fold.

## 5. YOUR FINAL MESSAGE TO ME
Give: the verdict line (e.g. "Q1 IN / Q2 OUT"), price and date, the commit hashes in order, the
check_framework result, every brief error you found, and anything in the killed session's drafts you
had to correct. Keep it under 400 words.
