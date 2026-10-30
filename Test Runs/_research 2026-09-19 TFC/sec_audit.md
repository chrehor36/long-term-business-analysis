
---
## SELF-AUDIT

- [x] **Questions answered in order; no verdict skipped.** Q1 IN → **Q2 OUT (the file closes)** →
      Q3, Q4 recorded and explicitly marked NOT GOVERNING at the head of each → Q5 did not open and
      appears only under `COMPUTATION — NOT A CLEARANCE` → Q6 recorded as the reversal record.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN and Q4 IN
      (recorded) rest entirely on filed documents named with accession numbers. The moat class at Q2
      is **NONE, not PROVISIONAL**, and the one gap in the competitor row (M&T's cost of deposits
      before 2025, which it does not tag separately) is stated in the row and does not bear on the
      verdict in either direction.
- [x] **Every UNRESEARCHED verdict names the artifact.** There are none.
- [x] **Every UNKNOWABLE verdict states what cannot be known.** There are none. **Two places where
      UNKNOWABLE was considered and rejected are stated in the open**: Q3, where a reader who judges
      the eighteen-day-old chief executive rather than the record would write UNKNOWABLE (the
      argument is printed in full beside the OUT), and Q4's incremental return on retained capital,
      which is recorded as **not establishable** inside an IN verdict on survival rather than used to
      fail the gate.
- [x] **Step 0: the filing was read, with accession numbers; a figure was cross-checked.** Six
      10-Ks, two 10-Qs, three proxies and eight 8-K exhibit sets, all listed with accessions. Equity
      recomputed from **A − L** per **[E5-32]**: $556,023M − $491,928M = **$64,095M**, exactly the
      filed total. Second cross-check on the figure that drives Q3: average common equity
      recomputed from period-end balances gives **$59,023M** against the filer's daily average of
      **$58,902M**, a 0.2% agreement.
- [x] **Owner earnings on a multi-year mean; window stated; the capex band disclosed as a
      judgment.** Three constructions, three windows (one year / three years / five years), the
      **41% spread reported as the range**, and the reason for the width named (the perimeter, not
      the business). The (c) guess is confessed as a **CONVENTION** under PRIME RULE 3 at Q3, with
      the departure from CCB's form stated and justified from Truist's own filings, as the brief
      required.
- [x] **Competitor row filled.** **TWO rows, nine banks, five years**: one computed on a single
      specification from tagged annual statement values and validated against the subject's own
      filed ROTCE (12.28% computed vs 12.7% published, gap explained); one from the **FDIC Call
      Report**, from the issuing authority, with every CERT verified by exact name.
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** 5.34%, USD,
      US Treasury daily par yield curve 30-year, 2026-09-18. FRED not used.
- [x] **Value stated as a round-number range, not a point estimate.** Roughly $20 to $50 a share
      across the defensible constructions, and **[E4-25]**'s conclusion drawn from the width.
- [x] **One bar chosen, not both; windage count stated.** Screamer test **[E4-01]**; windage count
      **ONE** (the conservative end of the owner-earnings range); no end margin added.
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $48.56 close of
      2026-09-18 from `tools/sources.py:price`, flagged; year-end closes used only for the
      **[E3-54]** market-value leg, flagged there too.
- [x] **Run committed to git** — five commits, each with a pathspec, under the write-early protocol:
      the claim, Step 0+Q1, Q2, Q3, Q4, and this closing section.
- [x] **The CGNX ruling of 2026-09-07 honoured:** the furnished 8-K EX-99.1 earnings releases were
      pulled and read **before** scoring **[E4-29]** and **[E4-22]**'s third flag — and it mattered.
      **[E4-29]** reads clean (EBITDA: zero occurrences in the 10-K, the proxy, the release and the
      deck), but **[E4-22]**'s third flag fires **only in the furnished material**: the 15% ROTCE
      target for 2027 and the 16-18% long-term target exist in the EX-99.3 slide deck and in the
      forward-looking-statements paragraph, and **nowhere in the 10-K.** A run that read only the
      annual report would have scored the projections flag clean.
- [x] **`python tools/check_framework.py` PASSES** — see the line below this block.

## REGISTER

- **Verdict: [ ] IN  [x] OUT (about the BUSINESS)  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
- **One line:** *Truist Financial (TFC) — **FAIL AT Q2, OUT ON THE BUSINESS**: on the FDIC's own
  uniform definitions Truist Bank has the **worst five-year mean pre-tax return on assets (0.991%
  against Regions' 1.875%) and the worst five-year mean return on equity (7.03% against 13.86%) of
  the nine largest regional banks in the United States**, from mid-pack funding costs (4th of 9),
  a mid-pack margin (5th of 9) and mid-pack leverage (13.3× tangible), with number-one deposit share
  in exactly one of its fourteen states, free deposits down 28% and branches down 31% in five years,
  and its own 10-K saying *"We expect that competition will only intensify in the future."*
  **Q3 recorded OUT at gate weight on [E3-29]** (the merger's $1.6bn cost-save yardstick reaffirmed
  twice and then never reported against; pay metrics that add back the $5,090M securities loss and
  the $6,078M goodwill impairment while the 2024 bonus paid 95% of target; three of four
  institutional-imperative behaviours; a published 16-18% long-term ROTCE target against an 11.5%
  five-year record) **— with the fact that decides how much weight to give it: the chief executive
  changed on 2026-09-01, eighteen days before this run.** **Q4 recorded IN on survival** — CET1
  10.9% against a 7.0% requirement, CRE at 51.5% of total capital against a 300% threshold, office
  at 0.74% of loans, and a stress five times the worst year in its history still leaving CET1 at
  9.9%. **Twelve perimeter events; ONE clean year.** Price **US$48.56** (2026-09-18), shares
  **1,221,626,188** (Q2 2026 10-Q cover, `0000092230-26-000099`), cap **US$59,322.2M**, sovereign
  **5.34%**. Below-gate computation fails the ~10% **[E4-28]** floor **and the bond** at the
  conservative end (yield 4.41%, −0.93 points). **Proposed survival shape #27, THE BOUGHT RATIO.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable. *(The two places UNKNOWABLE was weighed are named in the
  self-audit above.)*
- **Alerts and PORTFOLIO row: NONE, and deliberately.** The name failed at Q2 on the business, so
  the QLYS ruling of 2026-09-07 applies: no band in `tools/alerts.json`, no `PORTFOLIO.md` row, and
  the reversal condition recorded in words at Q2 and Q6 instead.
- **The strongest single fact AGAINST this run's conclusion, repeated here so the register carries
  it [E4-51]:** *on the FDIC's own numbers Truist Bank's efficiency ratio in the first half of 2026
  is **52.990%, the best of all nine banks**; its pre-tax return on assets has gone 0.874% → 1.248%
  → 1.350% in six quarters; its own reported ROTCE has gone 13.3% → 12.7% → 13.8% → **15.4%**; and
  the management that produced the five-year record left on 2026-09-01 having earned **nothing** on
  its 2023-2025 long-term award. If the last six quarters continue for three years, the Q2 verdict
  is wrong.* The threshold that would prove it is written at Q6 and it is three years, not one.
