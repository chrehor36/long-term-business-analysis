## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. **Q1 IN, Q2 OUT**; the file closed at Q2; Q3 to Q6 recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on the filings named.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued.
- [x] Step 0: the filing was read, with accession number (10-K FY2025 `0001193125-25-248751`, 10-Q to 2026-05-31 `0001193125-26-294516`); a figure was cross-checked (FY2025 OCF 132,910 = tag; SBC and capex likewise). No FY2026 10-K exists yet on EDGAR; stated.
- [x] Owner earnings on a multi-year mean (beneath the close); every window 3 to 16 years with both ends; the D&A end taken net of acquired-intangible amortisation; SBC complete; no NCI; no discontinued operations; no net-income proxy.
- [x] Competitor row filled from the one SEC filer among the three other main pivot makers (Valmont), identical construction, figures quoted from its filed segment notes; Reinke, T-L and the infrastructure rivals named as unobtainable; the verdict stated not to rest on the row.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated (US Treasury, 30 Yr, 09/25/2026, 5.49%), struck fresh; the 34% non-dollar revenue stated.
- [x] Value stated as a round-number range, not a point estimate (in the computation only; Q5 not opened).
- [x] One bar chosen, not both; windage count stated: n/a at Q5 (not opened); the computation's windage count is one.
- [x] Prices dated; aggregator used for live quotes only and flagged (Yahoo chart endpoint, close 2026-09-25).
- [x] Run committed to git with pathspecs (claim `94e59fcf`; Step 0 and Q1 `4856efae`; Q2 `53e89eb2`; this section and the register in the next commit; the fold after).
- [x] **Every ledger id cited in this file resolved against `principle_ledger.csv`** by script before the commit.
- [x] **The strongest evidence against the verdict is recorded and answered** [E4-26]: the high returns on operating capital, the rational four-maker oligopoly, the Road Zipper, the installed base, and Lindsay's lead over Valmont in FY2022-FY2025.

**Priors from the brief, tested.** The brief carried the screen row only and no business priors. Confirmed: the fiscal year ends in August; no FY2026 10-K is on EDGAR (the fiscal year ended 2026-08-31 and last year's 10-K was filed on 2025-10-23); `deal_note` is empty because nothing is deal-shaped; no Item 4.02. **The cap flag resolved the way the brief warned it might**: neither figure is wrong; the float is struck at $132.12 on 2025-02-28, the cap at $114.25 on a count 6% smaller. The 2022 cash-flow statement is a receivables and inventory build, reversed in FY2023.

**Tooling defects, reported, not patched.**
1. **`tools/run.py` prints *"GROWTH THE PRICE ASSUMES -15.3%"*** on a 6.78-7.63% yield against a 5.49% sovereign. At that yield the no-growth rate that equates price and value is about -1.3 to -2.1 points, not -15.3%; on the five-year window (3.97-4.71%) the price assumes about +0.8 to +1.5 points. **The third consecutive run with a growth figure of the wrong size or sign** (MATX -4.2%, PPG -9.2%).
2. **`tools/run.py`'s headline window (3 years, FY2023-FY2025) and the screen's `oe_top` count FY2023's release of FY2022's inventory build without the build** ($40,954K released in FY2023 against $53,803K built in FY2022), so *"1. THE YIELD 6.78% .. 7.63%"* is the most flattering window on the record; the four-year window ($54.8-63.1M, 4.7-5.4%) contains both halves. The `wc_note` flag found the 2022 year but nothing carries it to the window choice.
3. **The screen's `cap_flag` compares a float struck at the float's own date with a cap struck at a later price and count**, and calls one of them wrong. **Second run in three days where it fired on two dates and nothing was mis-filed** (PPG, LNN). The comparison that would test it is the float against the cap at the float's own date.
4. **The D&A end in `run.py` and the screen includes acquired-intangible amortisation** ($2.0-4.7M a year here), the older open ruling (resume state 11.5, item 2); small at Lindsay, recorded.
5. `cover_shares.py` worked on this filer and agreed with the cover read by hand.

## REGISTER
- Verdict: [ ] IN [x] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **LNN FAIL at Q2 (OUT, on the business): an irrigation-equipment maker (84% of revenue) in a four-maker market where, in its own 10-K every year FY2010-FY2025, "Due to price competition [...] the Company may not be able to recoup increases in these costs through price increases", and where the market leader says "Pricing in the industry can become highly competitive, particularly during periods of low demand" ([E3-03] criterion 2); price follows steel both ways in the MD&A and slips in soft years, and irrigation margins move with Valmont's and alternate in rank ([E3-43]'s "a business"); the Road Zipper's narrow position sits in a 16% segment [E4-08]. Price $114.25 (2026-09-25) x 10,168,885 = $1,161.8M; owner earnings $29-91M over every window and both ends (2.5-7.8%), $29-50M on every window of six years or more.**
- **If UNRESEARCHED — THE WORK ORDER:** n/a
- **If UNKNOWABLE:** n/a
