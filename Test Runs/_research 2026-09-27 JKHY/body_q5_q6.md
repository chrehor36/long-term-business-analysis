## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on ... we don't want to buy equities where our real expectancy is below 10 percent."* Arithmetic in `q5.py`, output `q5_out.txt`. Inputs: owner earnings from Q4 (three-year **$387.6M capex end, $436.2M D&A end**; with fiscal 2026's tax catch-up removed $345.6M-$394.2M; five-year $319.4M-$362.8M; the tax-neutral four-year $327.2M-$372.4M), cover shares **70,112,608**, price **$147.79** (Nasdaq close 2026-09-25, aggregator, flagged), cap **$10,361.9M**, sovereign **5.49%** (US Treasury, 30 Yr, 09/25/2026).

**The growth the record supports, stated before it is spent.**
- **Revenue: 7.5% a year** (fiscal 2009-2026, $745.6M to $2,544.3M), 6.5% (2016-2026), 7.7% (2021-2026); fiscal 2027 guidance *"$2,684 | $2,709"*, 5.5-6.5%. Part of it is bought (iPay, Goldleaf, Banno, Ensenta, Geezeo, Payrailz, Victor), and the cost of the buying sits below the owner-earnings line.
- **Owner earnings, aggregate, capex end, five-year mean to five-year mean:** 2011-15 $199.0M to 2016-20 $240.7M (3.9% a year); 2016-20 to 2021-25 $281.3M, **3.2% a year**; 2012-16 to 2017-21, 5.1%; over sixteen years (2005-09 $107.9M to 2021-25 $281.3M) **6.2% a year**. The D&A end: 2.3% (2016-20 to 2021-25) and 6.2% (sixteen years). **Owner earnings have grown more slowly than revenue for a decade**, because capitalized software grew faster than both (Q2, Q4); that is the pass-through the Q4 death names, already in the record.
- **Per share:** basic shares fell from 77.9M (fiscal 2017) to 71.9M (2026), about 0.9% a year, on $1.47bn of repurchases.
- **The corpus's ceiling on perpetual growth [E4-44]:** *"I come back to my postulation of 5% growth in GDP and remind you that it is a limiting factor in the returns you're going to get"*; and the base rate against sustained high growth **[E4-35]**: *"a growth rate of that magnitude can only be maintained by a very small percentage of large businesses"*.

**Honest pre-tax expectancy at $147.79** (yield plus growth; the yield is after corporate tax, so this errs low, as the corpus's own examples are judged):
- at **g = 0**: **3.74-4.21%** (three-year, capex end to D&A end); 3.34-3.80% with the tax catch-up removed.
- at **g = 3.2%** (the latest five-year-to-five-year owner-earnings rate): **6.94-7.41%**.
- at **g = 5.0%** ([E4-44]'s own ceiling for American business as a whole): **8.74-9.21%**.
- **Growth needed to reach the floor, in perpetuity: 6.26% (three-year capex end), 5.79% (three-year D&A end), 6.66% (capex end, catch-up removed), 6.50-6.92% (five-year)**: above the latest five-year owner-earnings rate on every construction and above [E4-44]'s ceiling on every one.
- **Below roughly 10% on every construction that spends a growth rate the owner earnings have delivered in the last decade, or the corpus's ceiling. QUIT ON; the name is not ranked.** No risk premium is in any rate **[E3-42]**.

**THE ONE CONSTRUCTION THAT CROSSES, stated at full strength [E4-51] and answered.** Spend the sixteen-year owner-earnings rate, 6.2% a year, in perpetuity: 3.74% + 6.2% = **9.94%** at the capex end and **10.41%** at the D&A end. Answered: (i) a perpetual 6.2% exceeds [E4-44]'s 5% ceiling, and the corpus says the value of an asset *"cannot over the long term grow faster than its earnings do"*, which is the operative limit once revenue growth slows to the guided 5.5-6.5%; (ii) the sixteen-year rate includes growth bought with $925M of acquisitions whose price is not in the owner-earnings mean, and the rate with the acquisitions deducted is lower; (iii) the most recent five-year-to-five-year rate is 3.2% at the capex end and 2.3% at the D&A end, and the Q4 death (#11, renewals compressing price) points the same way. **It is not spendable; no other construction reaches the floor.**

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no vote **[E3-34]**. The engine, run once as a cross-check (`q5.py`): three-year owner earnings growing at **7.5% a year (the revenue rate) for ten years, then 3%**, discounted at the 10% floor, gives **$113.5 (capex end) to $127.7 (D&A end) a share**, below the price even on the revenue rate that owner earnings have not matched. `tools/run.py` was not run; no figure here depends on it.

**1. THE YIELD**
- owner earnings **$387.6M-$436.2M** (three-year) ÷ market cap **$10,361.9M** = **3.74-4.21%** · sovereign **5.49%**. Every window: 1y 4.57-5.15% (a tax catch-up year), 5y 3.08-3.50%, 10y 2.79-3.14%, 27y 1.74-1.99%; with acquisitions counted 1.28-4.17%. **No window and no (c) end yields as much as the bond.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- at the bare bond rate, perpetual growth of **1.3-1.8% a year** (5.49% less the three-year yield; 1.7-2.2% with the catch-up removed); at the ~10% floor, **5.8-6.3% a year** for ever.
- what the business has actually done: revenue **7.5%**; owner earnings **3.2%** (latest five-year-to-five-year, capex end) to **6.2%** (sixteen years).

**3. WHAT YOU ARE PAID**
- the yield alone is **1.28-1.75 points BELOW the sovereign**; with the latest 3.2% owner-earnings growth the expectancy is **1.5-1.9 points over the sovereign and 2.6-3.1 points under the floor.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- sovereign used **5.49%**, the bare rate, no per-name premium.
- Certainty is handled at Q1 (passed) and in the end margin, once **[E4-11, E4-48]**; no margin is applied here, because the price is above the value before any margin.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**, the price at which the ~10% floor is met:
- **conservative about $80** (three-year capex end at g = 3.2%: $387.6M ÷ 0.068 ÷ 70.11M = **$81.30**; $72.50 with the catch-up removed) · **optimistic about $125** (three-year D&A end at [E4-44]'s 5%: $436.2M ÷ 0.050 ÷ 70.11M = **$124.43**) · **current price $147.79**. The two-stage engine at the revenue rate gives $114-$128. At zero growth the floor value is about $55-62.
- **The ceiling [E2-63, E4-44]:** the upside is bounded by owner-earnings growth, which has trailed revenue for a decade, and by a client market that shrinks about 3% a year in number.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **6.9-9.2%** (3.7-4.2% at no growth) vs ~10% **[E4-28]**: **below, so quit on, and the ranking lines are not filled in.**

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] Normal method [E4-11]: not reached; the price is above the value before a margin.
- [x] **Screamer test [E4-01]**: the conservative case is about $80 and the most generous floor case on a spendable growth rate about $125 (about $128 on the two-stage engine); **the price of $147.79 is above the whole range. Outcome: no.**
- **Windage count: ONE**, the capex end of (c) at the conservative figure (disclosed at Q4 as the judgment, not a stacked discount); the tax catch-up removal is displayed ($72.50) and not used in the range. **Removing the one** (the D&A end at the same 3.2%: $436.2M ÷ 0.068 ÷ 70.11M = $91.49) leaves the price 38% above it, and the optimistic figure ($124.43) is **16% below the price**; the verdict does not depend on it.

**The buyback condition from Q3, scored here [E5-08, E4-13].** Fiscal 2026 repurchases were made at *"an average price of $152 per share"*, the fourth quarter's at *"$140"*: **both above the whole value range ($80-$125) and above the two-stage engine ($114-$128). The second condition fails on this run's range: CAPITAL ALLOCATION FLAG.** Stated with the humility clause: *"it is natural for CEOs to be optimistic about their own businesses. They also know a whole lot more about them than I do"* **[E4-13]**, and *"many CEOs never stop believing their stock is cheap"* **[E5-08]**; the range is this run's, from filed figures only. **The flag binds position size, never the discount rate** (a CONVENTION, section VI of the framework).

- **VERDICT: [ ] IN — RANKED  [x] NOT IN — QUIT ON, below the ~10% floor [E4-28]  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  *A price answer, not a verdict about the business: Q1-Q4 are all IN. At $147.79 the owner-earnings yield is 3.74-4.21% (three-year), below the 5.49% bond on every window and both (c) ends, and the expectancy with the latest owner-earnings growth is 6.9-7.4% (9.2% at the corpus's 5% ceiling) against the ~10% floor.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]**: for a name not bought, these are the conditions under which the file is re-opened, and the falsifiers that close it at Q2 if they fire first. *"I believe in establishing yardsticks prior to the act."*
- **Thesis-confirming metric:** the core share of the filer's own market count rising (banks above the FY2025 ~21.4%, credit unions above ~15.9%) **in a year when the client-incentive balance falls as a share of revenue** and no 10-K repeats *"Certain of our renewals have resulted in price compression"*: [E2-44]'s first characteristic appearing where the filings now show its absence.
- **Thesis-breaking metrics and thresholds (each closes the file at Q2 on the business):**
  1. **Renewals are bought [E2-44, E3-43]:** contract assets (the *"upfront incentive payments or credits"*) above **8% of revenue** at a fiscal year-end (7.0% at 2026-06-30, from 5.2% in 2023), or rising faster than revenue in **both fiscal 2027 and 2028**.
  2. **The units turn [E4-55, E4-32]:** core banks as a share of the filer's own market count below **20%**, or core credit unions below **15%**, in any 10-K; or both shares falling in **two consecutive 10-Ks**.
  3. **The return converges on the rivals' [E3-46, E3-28]:** pre-tax return on operating capital ex goodwill below **30%** (the Q2 construction; low 33.8% in fiscal 2024) for **two consecutive years**, or the return including goodwill within **5 points** of Fiserv's (same construction, its own 10-K) for two years.
  4. **Price is given back openly [E4-37]:** an MD&A that attributes a revenue decline in the Core or Payments segment to renewal pricing, or GAAP operating margin below **21%** (below every year 2009-2026).
- **Next catalyst dates:** the proxy for the 2026 annual meeting (the last was filed 2025-10-02); the 10-Q for the quarter to 2026-09-30 (the last two first-quarter 10-Qs were filed 2024-11-08 and 2025-11-07); the fiscal 2027 10-K (the last three were filed 2024-08-26, 2025-08-25 and 2026-08-28), which carries the contract-asset balance and the core counts that decide conditions 1 and 2.

**Price bands (the QLYS ruling: a gate-clearer failed on price carries bands; each a prompt for a FULL v4.1 re-run, never a purchase):**
- **$81.30**: the ~10% floor met at g = 3.2% (the latest five-year-to-five-year owner-earnings rate, capex end) on the three-year capex-end owner earnings ($387.6M ÷ 0.068 ÷ 70.112608M).
- **$124.43**: the floor met only if [E4-44]'s 5% ceiling is granted in perpetuity on the three-year D&A-end owner earnings ($436.2M ÷ 0.050 ÷ 70.112608M); re-test the growth and the (c) end before spending either.
- Both bands are per the current share count and **VOID if any Q2 falsifier above has fired**; re-derive both on the fiscal 2027 10-K.

**The sell rule [E2-28]**: not engaged; no position is held or proposed.
- SELL if the market judges it more valuable than the facts indicate: n/a
- SELL if funds are needed for something more undervalued or better understood: n/a
- HOLD while: n/a (not held)
- *Price appreciation and holding period are **explicitly rejected** as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question, asked of fiscal 2025-2026: is the first *"price compression"* sentence and the faster growth of client incentives *"just part of an aberrational cycle"* (a wave of renewals of contracts signed in 2019-2020, in a year of bank mergers) *"or whether the business has slipped in a way that permanently reduces intrinsic business values"*? The margins, which widened in both years, argue aberrational; the incentive balance and the fiscal 2026 bank count argue slippage. Conditions 1 and 2 decide it on the next two 10-Ks.

**Do not trim winners [E5-14].** **Position size** — a judgment, stated: none now; if the name ever clears the floor, **sized DOWN** while the capital-allocation flag (fiscal 2026 buybacks above this run's value range) is live **[E3-45]**.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____** — the conditions are pre-committed, dated and filed-sourced; no position.

