# -*- coding: utf-8 -*-
import io
p = "Test Runs/2026-09-21 Run - IIIN Insteel Industries.md"
t = io.open(p, encoding='utf-8').read()
i = t.index('## SELF-AUDIT')
head = t[:i]
new = '''## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT, and the file stops
      there.** Q3 to Q6 carry notes with **no verdict box ticked**, per operator rule 2.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only
      IN in this file and it rests on Item 1 of a filing read in full.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives. **There is no
      UNRESEARCHED verdict in this file.** The one place the framework would ordinarily produce
      one - an incomplete competitor row - is discussed at Q2 and does not apply, because the
      verdict is OUT on the subject's own filing and six of the seven named competitors file
      nothing anywhere, so no artifact could be named.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known. **There is no
      UNKNOWABLE verdict in this file.**
- [x] Step 0: the filing was read, with accession number; **three figures were cross-checked
      by hand against the filed statements** (FY2025 operating cash $27,163k; equity recomputed
      from A - L to $371,532k; FY2025 net sales $647,706k against the MD&A's own 22.4%).
- [x] Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.
      **Five windows published (3y, 5y, 9y, 16y, TTM), both ends of (c) on every one.**
- [x] Competitor row filled, **and its incompleteness disclosed name by name**, with the reason
      the incompleteness does not rescue the class recorded in the open.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated. **5.34%, US
      Treasury 30-year par yield, 2026-09-18, struck fresh this run. FRED not used.**
- [x] Value stated as a round-number range, not a point estimate. **No value is stated at all:
      Q5 did not open.** The only Q5-adjacent arithmetic is headed COMPUTATION - NOT A CLEARANCE.
- [x] One bar chosen, not both; windage count stated. **Neither bar was used - no valuation was
      performed. Windage count: ZERO.** Conservatism was not spent, because no margin was taken.
      The one judgment made, (c) at the D&A end, is stated once and not re-applied as a margin.
- [x] Prices dated; aggregator used for live quotes only and flagged. **$29.66, close of
      2026-09-18, Yahoo Finance chart API, raw response saved to the research folder.**
- [x] Run committed to git, **in five commits: the claim, Step 0 + Q1, Q2, the notes beneath
      the close, and the fold.**

**Extra audit item this run added for itself, because the brief made it a standing check:**
- [x] **Every screen-row field tested against the filings and the result recorded, pass or
      fail.** Twelve fields, of which one (`cap_m`) is 2.4% high, one (`wc_note`) has the right
      arithmetic and the wrong direction, four reproduce exactly, and one (`spread_caveat`)
      issued an instruction that changed the answer when obeyed.
- [x] **No net-income proxy anywhere** (operator rule 5 and PRIME RULE 3's clause of
      2026-09-20). Owner earnings run off operating cash flow in every window.
- [x] **Every quotation checked against `principle_ledger.csv`'s own `quote_verbatim` field,
      not against the framework's rendering of it.** Six were corrected on that check, and two
      source artifacts are reproduced and flagged rather than smoothed.

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line:** *The nation's largest maker of steel wire for concrete is a converter of a
  commodity it does not own, selling into a market its own 10-K calls "highly competitive based
  on price, quality and service" against six named rivals and imports, with whatever floor
  exists under its prices administered by the Department of Commerce rather than by the company
  - **[E3-03]** criterion 2 fails on the filing, **[E2-58]** supplies the class and **[E2-59]**
  supplies the regime, so Q2 is OUT and Q3 to Q6 are notes.*
- **If UNRESEARCHED - THE WORK ORDER:** not applicable; the verdict is OUT, not UNRESEARCHED.
- **If UNKNOWABLE:** not applicable.

---
## WHAT THIS RUN FOUND THAT THE SCREEN DID NOT

1. **The published owner-earnings band is 41% too generous once every filed year is read.**
   $40M-$57M from 3- and 5-year windows; **$24.0M-$24.1M across the sixteen years the filer has
   actually filed.**
2. **One year carries the band, and that year's cash was inventory, not earnings.** FY2023 is
   **59.2%** of the five-year window, and **68.6%** of FY2023's operating cash was a
   working-capital release, **$94.3M of it the inventory line alone**, unwinding FY2022's
   $118.6M build.
3. **The working-capital note's direction is inverted, for the second time in four cycles.**
   The MD&A says *"Working capital used $37.6 million of cash"*; the flagged payable was the
   offset.
4. **`WC_TAGS` cannot see inventories or receivables.** A working-capital flag built only from
   liability tags is blind to every inventory-cycle business, and on this name the line it could
   not see is the one that carries the valuation.
5. **The trailing twelve months of owner earnings are negative at both ends** (-$20.5M and
   -$13.3M to 2026-06-27), which no annual-only screen can see.
6. **`principle_ledger.csv` holds 311 rows, not the 267 that `CLAUDE.md` and every brief still
   state.** Counted from the file, as the standing instruction says to. The growth is traceable:
   267 at commit `9d38c16`, 286 at `b7e84ca`, **311 at `0eaeadd`**, both of the latter dated
   2026-09-20, with the key-files table never updated. **Reported, not edited: `CLAUDE.md` is
   the operator's document.**
7. **`Framework/THE FRAMEWORK v4.md` smooths a transcript artifact in [E4-46]**, printing
   *"the following five months"* where the ledger row reads *"the followings five months"*, and
   dropping a *"You know,"*. PRIME RULE 1 says flag artifacts and never smooth them, and PRIME
   RULE 2 says the corpus wins. **Reported, not edited.**
8. **A post-balance-sheet event that no annual screen carries:** on **2026-08-21** Insteel
   announced the closure of Upper Sandusky, Ohio, *"restructuring charges of approximately $4.6
   million"* and *"the elimination of up to 65 positions"* - **the second of the two plants the
   FY2025 acquisition bought, both now closed within twenty-two months.**
'''
io.open(p, 'w', encoding='utf-8').write(head + new)
print("ok")
