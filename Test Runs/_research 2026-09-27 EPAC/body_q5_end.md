## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."* Arithmetic in `q5.py`, output `q5_out.txt`. Inputs: five-year default owner earnings **$53.0-53.7M** (capex end / depreciation end, Q4), three-year $67.1-70.0M, TTM $99.4-100.1M; cover shares **51,137,646**; price **$35.70** (NYSE close 2026-09-25, aggregator, flagged); cap **$1,825.6M**; sovereign **5.49%** (US Treasury, 30 Yr, 09/25/2026). **The pre-purchase perimeter**: the SFE Group purchase is signed and not shown closed on file; its effect is carried as a sensitivity below, not in the base.

**The growth the record supports, stated before it is spent.** Core (organic) sales in the filer's own words: +4% (FY2019), −20% (FY2020), +5%, +11% (FY2022, *"pricing actions"*), +8% (FY2023), about +2% (FY2024: IT&S +3%, product +1%), +1% (FY2025), about +1% in the nine months to 2026-05-31 (FY2026 guidance cut to *"1% to 2%"*): **compounded, about 1.1% a year FY2019-FY2025**, price included. The IT&S segment's sales were $588.2M in FY2016 and $595.8M in FY2025, flat across the exits and purchases. The old Industrial segment's sales grew **about 3.1% a year FY2007-FY2017, purchases included** (Simplex, Hayes, Larzep). Owner earnings tripled FY2022 to the TTM (about $26-30M to $99-100M), **a margin restoration (5.4% to 21.6% operating margin), not a growth rate**: margin cannot restore twice, and [E4-41] says a favourable break in the window is removed before the mean is trusted. **So about 1-3% a year is what the filed record supports.** [E4-35] is the check on anything higher, and [E4-44]'s ceiling (*"my postulation of 5% growth in GDP"*) is shown as the most generous case the corpus allows.

**Honest pre-tax expectancy at $35.70** (yield plus growth; the yield is after corporate tax, so this errs low, and the floor is judged on it as the corpus's own examples are):
- at **g = 0**: **2.90-2.94%** (five-year); 5.44-5.48% (TTM).
- at **g = 1.1%** (core FY2019-FY2025): **3.99-4.03%** (five-year); **6.54-6.57%** (TTM).
- at **g = 3.1%** (Industrial segment sales FY2007-FY2017, purchases included): **6.05-6.09%** (five-year); **8.59-8.63%** (TTM).
- at **[E4-44]'s 5% ceiling**: 7.90-7.94% (five-year); **10.44-10.48% (TTM)**. **This is the one construction that clears the floor, and it is refused**: it needs 5% a year for ever on the best twelve months the company has ever filed, three years into a margin restoration, against a filed core record of about 1% and a segment record of about 3% with purchases; [E4-35]'s base rate puts the burden on the claimant, and nothing in the filings carries it.
- **Growth needed to reach the floor: 7.06-7.10% a year in perpetuity at the five-year ends, 4.52-4.56% on the TTM**, against 1.1-3.1% filed. The screen row's `growth_required` 0.0751 reproduces on its own `oe_bottom` (48 on its 1,923 cap: 2.50%, so 7.50%), whose bottom deducts bought-intangible amortization (Q4).
- **The SFE Group sensitivity** (not in the base; the purchase is not shown closed): on the filer's figures, SFE's *"approximately $44 million of adjusted EBITDA"* less interest on $451.4M at FY2025's cost of about 5.3% and tax at 23% leaves **at most about $15.5M** before its capital spending, stock pay and any integration cost. Added to the TTM, the yield on today's cap is **at most about 6.3%**, and the expectancy at 1.1-3.1% growth is at most about 7.4-9.4%. **Still below the floor, on an upper bound.**
- **Below roughly 10% on every construction the record supports, by 1.4 to 7.1 points. QUIT ON; the name is not ranked.** No risk premium is in any rate **[E3-42]**.

**One book. Owner earnings against the bond.** A DCF may run as an engine; it casts no vote **[E3-34]**. `tools/run.py` was not run; no figure here depends on it.

**1. THE YIELD**
- owner earnings **$53.0-53.7M** ÷ market cap **$1,825.6M** = **2.90-2.94%** · sovereign **5.49%**. Every window 1-9 years at both (c) ends: 2.08-4.83%; TTM 5.44-5.48%. **Only the TTM reaches the bond, and only to within five hundredths of a point.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- year-1 growth needed to justify the quote at the bare bond rate: **2.55-2.59% a year in perpetuity** (five-year), **0.01-0.05%** (TTM); at the ~10% floor, **7.06-7.10%** (five-year), **4.52-4.56%** (TTM).
- what the business has actually done: **core sales about 1.1% a year FY2019-FY2025**; the old Industrial segment's sales about 3.1% a year FY2007-FY2017 with purchases; owner earnings tripled FY2022-TTM on a margin restoration.

**3. WHAT YOU ARE PAID**
- the yield alone is **2.55-2.59 points BELOW the sovereign** (five-year) and **0.01-0.05 below** on the TTM; with the filed 1.1-3.1% growth the expectancy is **1.4-3.5 points under the floor on the TTM and 3.9-6.0 points under it on the five-year default.**

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- sovereign used **5.49%**, the bare rate, no per-name premium. The EUR rate struck the same run (3.74%) is lower; using it for the 28% of sales earned in Europe would lower the bond comparison, not the ~10% floor, which is rate-invariant [E4-28].
- Certainty is handled at Q1 (passed) and in the end margin, once **[E4-11, E4-48]**; no margin is needed here, because the price is above the supported value before any margin is applied.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]**, the price at which the ~10% floor is met:
- **conservative about $12** (g = 1.1%, five-year capex end: $53.0M ÷ 0.089 ÷ 51.14M = $11.63) · **optimistic about $29** (g = 3.1%, TTM depreciation end: $100.1M ÷ 0.0685 ÷ 51.14M = $28.57) · **current price $35.70**. At zero growth the floor value is about $10-20; at the bare bond with no growth, about $19 (five-year) to $36 (TTM); at [E4-44]'s refused 5% ceiling on the TTM, about $39.
- **The ceiling [E2-63, E4-44]:** the upside is bounded by owner-earnings growth; the filer's own FY2026 outlook, cut on 2026-07-07 to organic growth of *"1% to 2%"* and adjusted EBITDA of *"$151 million to $156 million"*, is below its own opening range, and the margin restoration that tripled owner earnings has, on the filer's figures, reached its 25% adjusted EBITDA target.

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].**
- floor verdict first: honest pre-tax expectancy **4.0-8.6%** with the filed 1.1-3.1% growth (2.9-5.5% at no growth; at most about 9.4% even with SFE Group's upper-bound contribution) vs ~10% **[E4-28]**: **below, so quit on, and the ranking lines are not filled in.**

**WHICH BAR ARE YOU USING?** *(never both on the same number)*
- [ ] Normal method [E4-11]: not reached: the price is above the supported value before a margin.
- [x] **Screamer test [E4-01]**: the conservative case is about $12 and the most generous filed case about $29; **the price of $35.70 is above the whole range. Outcome: no.**
- **Windage count: ONE**, the growth rate carried as 1.1-3.1% from the filed record, disclosed as a judgment. **Removing it and granting [E4-44]'s 5% ceiling on the TTM** gives about $39, **9% above the price, and an expectancy of 10.4-10.5%: the verdict DOES depend on refusing that construction**, and the refusal is argued above ([E4-35], [E4-41], a 1% core record, the best twelve months ever filed). Even there the price would sit inside the range, not below its conservative end: [E4-01]'s outcome would be *"no useful conclusion"*, never a screamer.

- **VERDICT: [ ] IN — RANKED, position ____  [x] NOT IN — QUIT ON, below the ~10% floor [E4-28]  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**
  *A price answer, not a verdict about the business: Q1-Q4 are all IN. At $35.70 the owner-earnings yield is 2.90-2.94% (five-year) and 5.44-5.48% (TTM), against a 5.49% bond; the expectancy with the filed growth is 4.0-8.6% against the ~10% floor.*

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Pre-committed before entry [E1-02]** (no entry is proposed; these are the standing tests for any re-run):
- **Thesis-confirming metric:** consolidated gross margin at or above 49% (49.3-51.1% FY2023-FY2025) with price held in a down year, and IT&S product organic growth positive; owner earnings at the capex end above $90M a year on the pre-purchase perimeter.
- **Thesis-breaking metrics and thresholds (the Q2 falsifiers):** (i) consolidated gross margin **below 46% in two consecutive fiscal years** (the FY2021-FY2022 level, before the pricing actions) without a one-time cause the filer quantifies; (ii) the filer reporting **price given back or "competitive pricing" as a cause of a margin decline** in two consecutive years; (iii) **IT&S product organic sales negative in two consecutive fiscal years**; (iv) **a write-down of SFE Group or any purchased business of $50M or more**, or a purchase exited at a loss; (v) **pre-tax return on all operating capital, goodwill and intangibles included, below 15% for two consecutive years** after the purchase (21.4-30.2% FY2023-FY2025; about 19% at most on the purchase's own figures).
- **Staying-power test, dated:** the **September 2027 maturity** of the secured facility: by the 10-Q for the quarter to 2026-11-30 (due about early January 2027) the facility must be extended or refinanced, or it is current debt; **if it is not refinanced by the 10-Q for the quarter to 2027-02-28, Q4 is re-opened on staying power (3)**, and a covenant waiver or amendment at any time re-opens it.
- **Next catalyst date:** the FY2026 fourth-quarter release and 10-K (fiscal year to 2026-08-31; FY2025's 10-K was filed 2025-10-17, so about mid-October 2026): whether SFE Group closed, on what facility, and the FY2026 outturn against the cut guidance (Q3's [E3-48] record); re-derive the owner-earnings windows and both bands on it.

**The sell rule [E2-28]**: not held; no position exists and none is proposed. For the record, were one held:
- SELL if the market judges it more valuable than the facts indicate: **at $35.70 the price is above the whole supported value range**; this trigger would be live.
- SELL if funds are needed for something more undervalued or better understood: to be judged against the ranked set at the time.
- HOLD while: return on equity capital satisfactory (22.5-23.9% FY2024-FY2025 on an equity base reduced by buybacks, yes) · management competent and honest (no disqualifier; capital-allocation flag live; the Crimea matter pending) · market does not overvalue (no, at this price).
- *Price appreciation and holding period are explicitly rejected as reasons to sell.*

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question: whether the FY2023-FY2025 margin is the product core's long-run economics restored (the Industrial segment's 27-29% of FY2012-FY2014) or a peak that the service decline, the Middle East and the SFE Group integration will erode; falsifiers (i)-(iii) separate an aberrational cycle from a permanent slip, and (iv)-(v) watch the camouflage.

**Do not trim winners [E5-14].** **Position size — a judgment, stated:** **zero**; watch-list only. If a re-run ever clears the floor, **sized DOWN** for the live capital-allocation flag (Q3: [E5-08] condition (2) not met for FY2025-FY2026; the registrant's own [E2-30] record) and for staying power (3) until the facility is extended.

**Bands (armed at the fold for a gate-clearer, each a prompt for a FULL re-run, never a purchase):** **$11.63**, the floor met at g = 1.1% (core FY2019-FY2025) on the five-year capex-end owner earnings; **$28.57**, the floor met only if 3.1% a year (the Industrial segment's FY2007-FY2017 sales growth, purchases included) is granted on the TTM depreciation end. **Both VOID if a Q2 falsifier above has fired**, both re-derived on the FY2026 10-K, and both to be re-derived on the post-purchase perimeter once SFE Group's audited statements are filed.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**: the confirming and breaking metrics are written in filed series with thresholds and dates, the staying-power test is dated; no position is held.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q1 IN, Q2 IN NARROW, Q3 IN at binary-gate weight, Q4 IN narrowly on staying power, Q5 NOT IN, quit on below the floor, Q6 IN)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (Q2's class is NARROW, not PROVISIONAL; the unrowed hydraulic-tool rivals are private or unsegmented; Q4's staying-power weakness is a filed maturity, stated as a finding with a dated test, not a caveat on unverified evidence)
- [x] Every UNRESEARCHED verdict names the artifact and where it lives (none used; the FY2026 10-K and SFE Group's audited statements do not yet exist and are dated tests at Q6, not work orders)
- [x] Every UNKNOWABLE verdict states what specifically cannot be known (none used)
- [x] Step 0: the filing was read, with accession number (10-K FY2025 `0000006955-25-000030`; 10-Q to 2026-05-31 `0000006955-26-000036`; the 8-K of 2026-07-09 `0001140361-26-027991` with EX-2.1, EX-10.1 and EX-99.1); operating cash, SBC and capex for FY2023-FY2025 cross-checked between the filed statement and companyfacts
- [x] Owner earnings on a multi-year mean; every window 1-9 years shown at both (c) ends on the continuing-operations perimeter; capex band disclosed as a judgment; acquisitions and divestitures shown beside (c); the Actuant years before FY2017 not pooled; no net-income proxy
- [x] Competitor row filled (eleven SEC filers; the class rests on the filer's own segment record and is not held PROVISIONAL)
- [x] Sovereign is for the earnings currency (USD reporting currency, 5.49%, US Treasury par curve, 30 Yr, 09/25/2026), from the issuing authority, dated; EUR 3.74% recorded as an exposure
- [x] Value stated as a round-number range, not a point estimate (about $12-29 a share at the ~10% floor)
- [x] One bar chosen, not both (the screamer test); windage count stated (one), and the one construction that would clear the floor stated and refused with its reasons
- [x] Prices dated; aggregator used for live quotes only and flagged (Yahoo chart endpoint, close 2026-09-25; the monthly series used in Q3's retention test also flagged)
- [x] Run committed to git (pathspec commits `60e4cf95`, `1c819999`, `4c46cb21`, `dda424b6`, `778e9789`, and the commit carrying this audit)

**Ledger ids.** Every id cited in this file was checked against `principle_ledger.csv` before the file was committed (`ledger_ids.txt` lists them with the first words of each row); the brief's labels were checked against the rows: [E3-03], [E3-43], [E2-44], [E2-58], [E4-23], [E4-04], [E2-23], [E2-09], [E3-44], [E4-25], [E4-01], [E4-28], [E4-22], [E4-29], [E4-27], [E4-26]. The acceptance test's phantom-id check (check 5) passed on this file at the fold.

**Brief and screen errors found (each a prompt to read; none changed a verdict):**
1. **The brief's deal hypothesis resolves to the acquirer side**: Enerpac is buying SFE Group (about $451.4M cash plus $20.6M of RSUs, signed 2026-07-07), not being bought; the quote is not a spread. The brief was right to demand the read: the `deal_note` does not say which side the filer is on.
2. **`cap_flag` is a date mismatch, not a contradiction**: the filed float ($2.49bn) was struck at $46.27 on 2025-02-28; the screen's cap about eighteen months later at about $36.
3. **`cap_m` 1,923 is stale**: today's cap is $1,825.6M, 5.1% below it (lower price and 51.1M shares after buybacks).
4. **`vs_sovereign` −0.0286 implies a 5.35% sovereign**; today's is 5.49%.
5. **`oe_bottom_m` 48 reproduces only with amortization of bought intangibles deducted as maintenance** (five-year $47.8M on the D&A line; $53.0-53.7M at the ends [E3-44] names); `oe_top_m` 67 reproduces (three-year capex end, $67.1M); `spread` 0.402 mixes window and definition.
6. **`years_filed` 17 and the `level_note` family run across the Actuant perimeter** (the name-change note was right to warn); the present company has nine continuing-operations years; the minus $3.7M in `level_note` reproduces as FY2020 at the capex end, and the note is truncated.
7. `growth_required` 0.0751 reproduces on the screen's own bottom; at the five-year ends it is 7.06-7.10%, on the TTM 4.52-4.56%.
8. `acq_note` blank while a purchase equal to about 26% of the cap is signed; `newest_periodic` 2026-05-31 is current.
9. The brief's commit trailer (*"Claude Opus 5 (1M context)"*) differs from the environment's attribution line; the brief's was used, as the prior runs did, and is recorded here.

**Tooling defects, reported not patched:** the screen's `oe_bottom` deducts bought-intangible amortization as (c) (the AIT finding, third filer after NDSN); the screen's multi-year fields pool a registrant's pre-divestiture consolidated years with its continuing-operations years (the name-change flag detects the rename, not the perimeter); capital spending for this filer is tagged `PaymentsToAcquireProductiveAssets`, so a reader limited to `PaymentsToAcquirePropertyPlantAndEquipment` returns nothing; `cap_flag` compares a cap and a float struck at different dates without stating either price; `deal_note` names the exhibit but not the filer's side of the deal; `tools/run.py` not run.

---
## REGISTER
- Verdict: **[x] IN (Q1-Q4 all IN; Q5 NOT IN, quit on below the ~10% floor, a price answer)** [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **Enerpac Tool Group, the Milwaukee seller of high-pressure hydraulic and bolting tools (the old Actuant, renamed 2020 after selling everything else), is a narrow franchise at its product core: the Industrial segment earned 22-31% on sales and 26-53% pre-tax on its assets including goodwill for thirteen years, held 23.5% through the FY2009 recession, and passed two inflations through with gross margin rising to 50.5%; but the company that owned it earned 5-10% on sales FY2018-FY2022, its present margin is three years old, a fifth of it is labour, and it has signed to buy SFE Group for about $472M on a secured facility that matures in September 2027. Q1-Q4 IN (Q2 NARROW; Q3 binary gate with [E4-29] and capital-allocation flags and the self-reported Crimea sanctions matter recorded; Q4 good, #10 THE CAMOUFLAGE with #6 as a feature, staying power (3) not met once the purchase closes); Q5 QUIT ON at $35.70 (2026-09-25) x 51,137,646 shares = $1,825.6M against a 5.49% bond (09/25/2026): owner earnings $53.0-53.7M five-year (2.90-2.94%), $99.4-100.1M TTM (5.44-5.48%), expectancy 4.0-8.6% with the filed growth; value about $12-29.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable.
- **If UNKNOWABLE:** not applicable.
