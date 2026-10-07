## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on ... we don't want to buy equities where our real expectancy is below 10 percent."* Arithmetic in `q5.py`, output `q5_out.txt`. Inputs: owner earnings from Q4 (three-year **$5,266.3M capex end, $6,030.3M filer-split, $6,489.0M depreciation limit**; five-year $5,490.0M-$6,644.0M; TTM $6,373M-$7,619M), cover shares **594,075,498**, price **$273.79** (NYSE close 2026-09-25, aggregator, flagged), cap **$162,651.9M**, sovereign **5.49%** (US Treasury, 30 Yr, 09/25/2026). **Both perimeters are priced**, per the rule stated at Step 0; the verdict below does not turn on which.

**The growth the record supports, stated before it is spent.**
- **Volume: none.** Revenue carloads **8,453,000 (1997) and 8,447,000 (2025)**: flat over 28 years (9,852,000 at the 2006 peak).
- **Nominal freight revenue: 3.2% a year 1997-2025** ($9,712M to $23,220M), 3.0% a year 2005-2025; real revenue per car (fuel included) +19% over the 28 years, made in 2003-2014 (+52%) and partly given back since (-14%).
- **Owner earnings, aggregate, capex end:** five-year mean 2016-20 $4,716.6M to 2021-25 $5,490.0M, **3.1% a year**. Over 2010-14 to 2021-25 it was 7.3% a year, **made by the operating ratio falling from about 67% to 60%**, which cannot fall that far again.
- **Owner earnings per share, capex end:** five-year mean $6.34 (2016-20) to $8.87 (2021-25), **6.9% a year, of which more than half is the share count falling 3.9% a year (five-year mean diluted shares 755.3M to 618.8M) on $43.3bn of repurchases, about $17bn of them borrowed** (Q3). Buybacks are *"paused"*, and the merger adds about 225M shares.
- **The corpus's ceiling on perpetual growth [E4-44]:** *"I come back to my postulation of 5% growth in GDP and remind you that it is a limiting factor in the returns you're going to get."*

**Honest pre-tax expectancy at $273.79** (yield plus growth; the yield is after corporate tax, so this errs low, as the corpus's own examples are judged):
- at **g = 0**: **3.24-3.99%** (three-year, capex end to depreciation limit); 4.68% at the TTM depreciation limit.
- at **g = 3.1%** (the filed revenue and aggregate owner-earnings rate): **6.34-7.09%**; 6.81% on the filer-split construction.
- at **g = 5.0%** ([E4-44]'s own ceiling for American business as a whole): **8.24-8.99%**; 9.68% at the TTM depreciation limit, the most generous standalone construction on the record.
- **Growth needed to reach the floor, in perpetuity: 6.8% (three-year capex end), 6.3% (filer-split), 6.0% (depreciation limit), 5.3% (TTM depreciation limit)**: above the 28-year filed rate on every construction and above [E4-44]'s ceiling on all but the TTM limit.
- **Combined perimeter** (225M new shares, $20bn of new debt at 5.10-5.60%; Q4): yield **2.65% (capex end, no synergies) to 3.62% (depreciation limit, no synergies)**; **3.61% to 4.58% with every dollar of the claimed $2.75bn synergies**; growth needed to reach the floor **5.4% to 7.4%**. **Worse on every construction than standalone before synergies, and no better than standalone with all of them.**
- **Below roughly 10% on every construction that spends a growth rate the business has earned, on both perimeters. QUIT ON; the name is not ranked.** No risk premium is in any rate **[E3-42]**.

**THE ONE CONSTRUCTION THAT CROSSES, stated at full strength [E4-51] and answered.** Spend the per-share record, 6.9% a year, in perpetuity: 3.24% + 6.9% = **10.1%** at the capex end, 10.9% at the depreciation limit. That rate is the operating-ratio programme plus debt-funded repurchases: the ratio sits at 59.8% against 87.4% in 1997 and cannot repeat the move; the repurchases are paused and the merger reverses the share count; and a perpetual 6.9% exceeds [E4-44]'s 5% ceiling. [E2-01] excludes returns earned through *"undue leverage"*, and a growth rate bought with leverage is the same thing seen per share. **It is not spendable, and no other construction reaches the floor.**

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no vote **[E3-34]**. `tools/run.py` was run for the cross-check only; no figure here depends on its embedded growth assumptions.

**1. THE YIELD**
- owner earnings **$5,266.3M-$6,489.0M** (three-year) ÷ market cap **$162,651.9M** = **3.24-3.99%** · sovereign **5.49%**. Every window: 1y 3.29-4.11%, 5y 3.38-4.08%, 10y 3.14-3.85%, 23y 1.90-2.70%, TTM 3.92-4.68%. **No window and no (c) end yields as much as the bond.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- at the bare bond rate, perpetual growth of **1.5-2.3% a year** (5.49% less the yield); at the ~10% floor, **6.0-6.8% a year**.
- what the business has actually done: **3.1-3.2% a year** in aggregate (revenue 28 years, owner earnings 5y-to-5y); 6.9% per share with leverage.

**3. WHAT YOU ARE PAID**
- the yield alone is **1.50-2.25 points BELOW the sovereign**; with the filed 3.1% growth the expectancy is **0.9-1.6 points over the sovereign and 2.9-3.7 points under the floor.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- sovereign used **5.49%**, the bare rate, no per-name premium.
- Certainty is handled at Q1 (passed) and in the end margin, once **[E4-11, E4-48]**; no margin is applied here, because the price is above the value before any margin.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**, the price at which the ~10% floor is met:
- **conservative about $130** (three-year capex end at g = 3.1%: $5,266.3M ÷ 0.069 ÷ 594.1M = $128.47) · **optimistic about $220** (three-year depreciation limit at [E4-44]'s 5%: $6,489.0M ÷ 0.050 ÷ 594.1M = $218.46) · **current price $273.79**. The filer-split construction gives $147 (3.1%) to $203 (5%). At zero growth the floor value is about $89-109.
- **Combined perimeter, per Union Pacific share after closing:** about **$105** (capex end, no synergies, 3.1%) to **$251** (depreciation limit, every synergy dollar, 5%: the most generous construction in this file). **The price is above that too.**
- **The ceiling [E2-63, E4-44]:** the upside is bounded by owner-earnings growth, and the physical series has not grown in 28 years.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **6.3-9.0%** (3.2-4.0% at no growth) vs ~10% **[E4-28]**: **below, so quit on, and the ranking lines are not filled in.**

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] Normal method [E4-11]: not reached; the price is above the value before a margin.
- [x] **Screamer test [E4-01]**: the conservative case is about $130 and the most generous standalone case about $220 (about $251 on the most generous combined construction); **the price of $273.79 is above the whole range. Outcome: no.**
- **Windage count: ONE**, the capex end carried as the conservative figure (disclosed at Q4 as the corpus's default for this business, not a stacked discount). **Removing it** (the depreciation limit, which the filings say is never reached, at the 5% ceiling) gives about $218, still **20% below the price**; the verdict does not depend on it.

- **VERDICT: [ ] IN — RANKED  [x] NOT IN — QUIT ON, below the ~10% floor [E4-28]  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *A price answer, not a verdict about the business: Q1-Q4 are all IN. At $273.79 the owner-earnings yield is 3.24-3.99% (three-year), below the 5.49% bond on every window and both (c) ends, and the expectancy with the filed growth is 6.3-7.1% (9.0% at the corpus's 5% ceiling) against the ~10% floor. The combined perimeter is worse before synergies and no better with all of them.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]**: for a name not bought, these are the conditions under which the file is re-opened, and the falsifiers that close it at Q2 if they fire first.
- **Thesis-confirming metric:** real freight revenue per carload excluding fuel surcharge (CPI-U deflated, the Q2 construction) **rising in a year when carloads are flat or falling** [E2-44], with the operating ratio at or below 60%.
- **Thesis-breaking metrics and thresholds (each closes the file at Q2 on the business):**
  1. **The regime binds [E2-59]:** the STB adopts a rate standard built on revenue adequacy, or a reciprocal-switching rule reaching Union Pacific's traffic generally, or approves the merger on conditions that open Union Pacific's corridors to another carrier's trains (trackage rights or switching beyond the specific markets named in the application).
  2. **The price slide continues [E4-55, E4-32]:** real freight revenue per carload excluding fuel surcharge below the prior year's in **2026 and 2027** (a third and fourth year after 2019-2025's -12%), from the 10-K MD&A and BLS CPI-U.
  3. **The western lead goes [E3-28]:** Union Pacific's operating ratio within **3 points** of BNSF's (BNSF LLC's own 10-K, same construction) for **two consecutive years**.
  4. **The return falls to the regulated level [E5-40]:** the filer's return on invested capital as adjusted below **12%** for **two consecutive years**, the merger's goodwill included.
- **Next catalyst dates:** the STB's procedural schedule after the supplemental information (the 10-Q: first portion provided 2026-07-07, the rest due by 2026-07-27); the Q3 2026 10-Q (late October 2026); the FY2026 10-K (February 2027); the STB decision (the companies expect completion *"in 2027"*); the agreement's End Date **2028-01-28**.

**Price bands (the QLYS ruling: a gate-clearer failed on price carries bands; each a prompt for a FULL v4.1 re-run, never a purchase):**
- **$128.47**: the ~10% floor met at g = 3.1% (the filed revenue and aggregate owner-earnings rate) on the three-year capex-end owner earnings ($5,266.3M ÷ 0.069 ÷ 594.1M).
- **$218.46**: the floor met only if [E4-44]'s 5% ceiling is granted in perpetuity on the three-year depreciation limit ($6,489.0M ÷ 0.050 ÷ 594.1M); re-test the growth and the (c) end before spending either.
- **Both bands are standalone and per the current share count. On the merger's closing they are VOID and must be re-derived on the combined perimeter** (about $105 to $251 a share on this file's constructions), because the share count rises about 38% and $20bn of debt is added; if the STB refuses, re-derive after the $2.5bn fee.

**The sell rule [E2-28]**: not engaged; no position is held or proposed.
- SELL if the market judges it more valuable than the facts indicate: n/a
- SELL if funds are needed for something more undervalued or better understood: n/a
- HOLD while: n/a (not held)
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question, asked of 2019-2025: is the 12% real price fall *"just part of an aberrational cycle - to be fully made up in the next upturn - or whether the business has slipped in a way that permanently reduces intrinsic business values"*? The 2014-2019 flat real price and the CPI surge of 2021-2023 argue aberrational; the 28-year flat volume and the fall in every commodity line argue slippage. Condition 2 decides it on the next two 10-Ks.

**Do not trim winners [E5-14].** **Position size** — a judgment, stated: none now; if the name ever clears the floor, **sized DOWN** while the capital-allocation flag on the merger is live.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____** — the conditions are pre-committed, dated and filed-sourced; no position.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Step 0; Q1 IN; Q2 IN NARROW; Q3 IN as a binary gate; Q4 IN; Q5 NOT IN, QUIT ON; Q6 written). Valuation arithmetic before Q4 closed was not reported; the combined-perimeter owner earnings at Q4 are headed as computation.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q2's one undisclosed figure (the regulated share of traffic) is named with the document that would hold it and does not carry the verdict, which rests on the filed outcome.
- [x] Every UNRESEARCHED verdict names the artifact (none issued). Every UNKNOWABLE verdict states what cannot be known (none issued; **the [E4-04] competence branch was considered and refused in writing**, and **the perimeter branch at Q5 was tested and did not arise**: both perimeters give the same answer).
- [x] Step 0: the filing was read, with accession numbers (10-K FY2025 `0000100885-26-000037`, 10-Q `0000100885-26-000250`, 8-K `0000100885-26-000249` with EX-99.1, DEF 14A `0000100885-26-000098`, the merger 8-Ks `0001193125-25-168150` and `0001193125-25-167154`, the vote 8-K `0000100885-25-000332`, every 10-K FY2000-FY2024; Norfolk Southern's 10-Ks `0001628280-26-006268` and `0000702165-25-000008` and 10-Q `0001628280-26-049326`); FY2025 operating cash, capex, depreciation and SBC cross-checked to the filed statement and note.
- [x] **The deal check was done from the filings, not the row**: a live merger found where the row's `deal_note` was blank; terms, votes, the STB timetable, fees, financing and the perimeter rule written before any gate.
- [x] **One share class; nothing summed**; the cover count's as-of date (2026-07-17) stated.
- [x] **SBC resolves and is complete** (not on the face; the note table by plan; the tag split across two elements recorded).
- [x] Owner earnings on a multi-year mean; **every trailing window 1-23 years and every rolling five-year window, both (c) ends plus the filer-split middle and a capital-lease construction**; the (c) hypothesis tested against the filings in both directions [E5-20]; no net-income proxy.
- [x] Competitor row filled (all five other North American Class I railroads, two metrics, same construction, filing-sourced); **class not PROVISIONAL**.
- [x] **The strongest evidence against each open verdict was stated and answered** (Q2 five items; Q5 the one crossing construction) and the analyst's incentives stated (operator rule 9, [E4-27], [E4-26]).
- [x] Sovereign for the earnings currency, from the issuing authority, dated (USD 5.49%, US Treasury par curve, 09/25/2026, struck fresh). CPI from the issuing authority (BLS).
- [x] Value stated as a round-number range, not a point estimate (about $130 to $220 standalone; about $105 to $251 combined).
- [x] One bar chosen, not both (screamer); windage count ONE, stated, and removing it does not change the answer.
- [x] Prices dated; aggregator used for live quotes only and flagged (UNP $273.79, NYSE close 2026-09-25, Yahoo chart endpoint).
- [x] Run committed to git (commits `72dcab0f` claim, `e4555f79` Step 0 and Q1, `5ea2b6db` Q2, `5fe05b95` Q3, `146462a6` Q4, then this section and the fold).

## REGISTER
- Verdict: [ ] IN [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence) — **Q1-Q4 IN; Q5 NOT IN, QUIT ON at the ~10% floor (a price answer).**
- One line: **ALL FOUR BUSINESS GATES IN; FAIL AT Q5 ON PRICE.** One of the two western railroad networks, with the lowest operating ratio (59.9% mean 2021-2025) and the highest return on its plant (16.9%) of all six North American Class I railroads, and a filed repricing era (real revenue per car +35% in 2003-2014); **NARROW**, because the STB's rate jurisdiction is live [E2-59], capital must run at 1.72x depreciation [E2-44, E5-20], and real revenue per car at fixed mix has fallen 12.4% since 2018 in every commodity line on carloads flat for 28 years [E4-55, E4-32]. Q3 IN as a binary gate for the merger's integration years, with a capital-allocation flag: **a live acquisition of Norfolk Southern (1 share + $88.82 per NSC share; about 225M shares and $20bn of new debt; STB decision expected 2027; $2.5bn fee) that pays about $81.6bn for 1.85-3.02% owner earnings, 5.2-5.7% with every claimed synergy, and cuts owner earnings per share about 18% at closing before synergies.** Owner earnings $5,266.3M-$6,489.0M (three-year), **3.24-3.99% against a 5.49% bond**; expectancy 6.3-9.0% against the ~10% floor on both perimeters; value about $130 to $220 a share against $273.79.
- **Brief and screen errors found (every brief has had one):**
  1. **`deal_note` BLANK, and a merger is live**: 8-K Item 1.01 of 2025-07-29, S-4 of 2025-09-16 (effective 2025-09-30), 87 Form 425s, both votes on 2025-11-14, the STB application of 2025-12-19. **The row priced a quote that is not an owner-earnings price for today's company.** Cause found, a tooling defect (below).
  2. **`cap_m` $182,803M** was struck at an older price; today's cap is **$162,651.9M (-11.0%)**. `yield_bottom` 2.88% and `vs_sovereign` -2.47% follow from it and an older sovereign (5.35% implied); today's are 3.24% and -2.25 points. `growth_required` 7.12% (10% less the stale yield) is **6.76%** today.
  3. **`oe_bottom_m` $5,266M and `oe_top_m` $6,644M reproduce to the dollar** ($5,266.3M three-year capex end, $6,644.0M five-year depreciation end), **but the top is a (c) end the filings say is never reached** [E5-20]: the filer's own capital table puts maintenance-type capex above depreciation in every year.
  4. **`spread_caveat` said the 4-construction width "CANNOT see variation older than the 5-year window"**: it could not, and what is there is lower ($3,086.9M, 1.90%, over 23 years), **but it is not a hidden cycle; it is an older, worse-run railroad** (operating ratio 81.5% in 2003); the recent windows are the normal and every window is below the bond either way.
  5. **`years_filed` 19** is the XBRL depth; the record read here runs 1997-2025 (traffic) and FY2003-FY2025 (cash flows).
  6. **The brief's operating-ratio gap "BNSF trails by 5.7-8.1 points"** is Berkshire's segment basis (the BRK run); on BNSF LLC's own 10-K the gap is 6.7, 6.7, 8.2 and 5.8 points for 2022-2025. Both filed; the difference is the source, recorded.
  7. **The brief's memory of the deal was right in outline** (Union Pacific buying Norfolk Southern for stock and cash, subject to the STB) and carried no terms; every term above is from the filings.
  8. **The brief's question "is UNP different from BNSF's real price fall?" is answered: no** (-12.4% at fixed mix 2018-2025 against about -12% for BNSF).
  9. **The brief's commit trailer** (`Claude Opus 5 (1M context)`) differs from the attribution this session's environment supplies (`Claude Opus 5.5`); the brief's line was used, as the dispatcher's written instruction, and the difference is recorded (the NUE, BUKS, BR, MRK and NGVC precedent).
- **Tooling, reported, not patched:** (a) **`tools/sources.py` `deal_filings()` only looks at filings made after the latest annual report** (`since` = the newest 10-K date), so **a deal signed before the last 10-K and still pending is invisible**: for UNP it returns zero hard and zero soft hits today (since 2026-02-06), with a signed merger, an effective S-4 and 87 Form 425s on file; the same blind spot would hide any long regulatory review; (b) companyfacts carries no `NetCashProvidedByUsedInOperatingActivities` for UNP FY2013-FY2016 (only the `...ContinuingOperations` tag); (c) UNP's SBC is under `ShareBasedCompensation` only to FY2023 and under `AllocatedShareBasedCompensationExpense` for FY2024-25 (resolved by `tools/run.py`; a one-tag reader would subtract zero); (d) UNP's `PropertyPlantAndEquipmentNet` stops after FY2023; (e) **BNSF LLC's `Revenues` tag carries about $100M a year from FY2021** (another revenue line), so a peer row that takes `Revenues` first shows an operating ratio of about -8,000%; (f) CN's annual facts sit under **6-K** forms (a 40-F filer), so a filter on 10-K/40-F/20-F returns nothing. `tools/run.py` was run and its FY2023-25 figures agree with the filed statement.
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
