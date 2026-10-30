## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**Construction** (`oe.py` → `oe_out.txt`): operating cash flow from the filed statements (latest-filed vintage; FY2023-FY2025 checked against the FY2025 face at Step 0), **less** stock compensation in full [E5-06] (the face line *"Share-based compensation"*, the ESPP inside it), **less** (c). **Span:** the standalone years FY2015-FY2025 (eleven); FY2013-FY2014 are shown and excluded, because they are carve-out years in which the parent paid the taxes (`IncomeTaxesPaidNet` $0M and $4M, against $40-343M a year since). **No net-income proxy anywhere** (operator rule 5).
- **(c), a disclosed judgment [E2-09, E3-44, E2-41], at two ends.** Capex end: *"Investments in property, plant and equipment"*, gross of the small government incentives. Depreciation end: the face line *"Depreciation"* (plant, equipment and buildings; FY2025 net plant $795M on $2,599M gross). **The face line *"Amortization"* (acquired intangibles, $145M in FY2025) is not a maintenance cost** ([E2-23]'s (b) adds such charges back); a depreciation-plus-amortization end is shown only because the screen used it. Capex ran 0.98-1.64 times depreciation in FY2021-FY2025 (FY2023 $197M against $120M, FY2025 $128M against $131M); the filer does not split maintenance from growth capex. **Not [E5-20]'s class:** an instrument maker whose assembly is partly contracted out, capex 2.4-3.6% of revenue, no filing read saying depreciation understates renewal. The two ends differ by less than 5% on every window of three years or more, so the capex band does not change any verdict.
- **Working capital [E2-23]:** operating cash nets it; FY2023 carried an inventory build (*"Inventory | ( 24 ) | ( 49 ) | ( 148 )"*, FY2025-FY2023) and FY2024 a $202M income-tax receivable (the discrete benefit of amended returns) that reversed by $105M in FY2025. Single years move with these; only multi-year means are owner earnings.
- **[E4-41], normalize down for luck:** FY2023 operating cash includes *"Interest rate swap agreement termination proceeds | — | — | 107"*, a gain on rates, not the business; the five-year capex-end mean without it is $945.6M against $967.0M. FY2025 carries the $105M tax-receivable collection that FY2024 lacked; across FY2024-FY2025 the two net out. **The perimeter:** no filed year contains Spirent, OSG and PowerArtist; the trailing twelve months to 2026-07-31 contain them for three quarters.

**By year ($M):**

| FY | OCF | SBC | capex | depreciation | amortization | OE, capex end | OE, depreciation end |
|---|---|---|---|---|---|---|---|
| 2013 (carve-out) | 566 | 41 | 69 | 65 | 9 | 456 | 460 |
| 2014 (carve-out) | 563 | 43 | 70 | 74 | 8 | 450 | 446 |
| 2015 | 376 | 55 | 92 | 81 | 15 | 229 | 240 |
| 2016 | 420 | 49 | 91 | 85 | 43 | 280 | 286 |
| 2017 | 328 | 56 | 72 | 92 | 131 | 200 | 180 |
| 2018 | 555 | 59 | 132 | 103 | 204 | 364 | 393 |
| 2019 | 998 | 82 | 120 | 96 | 210 | 796 | 820 |
| 2020 | 1,016 | 92 | 117 | 104 | 220 | 807 | 820 |
| 2021 | 1,322 | 103 | 174 | 117 | 174 | 1,045 | 1,102 |
| 2022 | 1,144 | 125 | 185 | 117 | 103 | 834 | 902 |
| 2023 | 1,408 | 135 | 197 | 120 | 92 | 1,076 | 1,153 |
| 2024 | 1,052 | 137 | 154 | 126 | 144 | 761 | 789 |
| 2025 | 1,409 | 162 | 128 | 131 | 145 | 1,119 | 1,116 |
| TTM to 2026-07-31 | 1,604 | 214 | 135 | 150 | 243 | 1,255 | 1,240 |

*(TTM = FY2025 + nine months to 2026-07-31 − nine months to 2025-07-31, from the 10-Qs `0001601046-26-000036` and `0001601046-25-000091`: operating cash $1,379M and $1,184M, SBC $181M and $129M, capex $97M and $90M, depreciation $116M and $97M. Amortization FY2013-FY2022 from the tag `AmortizationOfIntangibleAssets`, FY2023-FY2025 from the face line. Interest is paid inside operating cash, so these figures are after interest.)* **Positive every year at both ends; never near zero.**

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].** Every trailing window ending FY2025, on the Step 0 cap of $61,654.1M, against the 5.49% sovereign (all eleven lengths in `oe_out.txt`):

| window | capex end | depreciation end |
|---|---|---|
| 1y FY2025 | $1,119.0M (1.81%) | $1,116.0M (1.81%) |
| 3y FY2023-25 | $985.3M (1.60%) | $1,019.3M (1.65%) |
| **5y FY2021-25 (the corpus's default window [E2-42])** | **$967.0M (1.57%)** | **$1,012.4M (1.64%)** |
| 7y FY2019-25 | $919.7M (1.49%) | $957.4M (1.55%) |
| 11y FY2015-25 (every standalone year) | $682.8M (1.11%) | $709.2M (1.15%) |
| TTM to 2026-07-31 (the first figure with Spirent and OSG) | $1,255M (2.04%) | $1,240M (2.01%) |

- **Short-window mean** (window: five years FY2021-FY2025): **$967.0-1,012.4M**
- **Long-window mean** (window: eleven years FY2015-FY2025): **$682.8-709.2M**
- **Spread, conservative end:** the eleven-year capex end is 29.4% below the five-year capex end.
- **Combined range** (every window 1-11 years × both ends): **$682.8M to $1,119.0M (1.11% to 1.81% of the cap)**; the TTM $1,240-1,255M (2.01-2.04%). **Every rolling five-year window [E4-38]:** from $373.8M (FY2015-19, capex end, 0.61%) rising in every step but one (FY2020-24, $904.6-953.2M, slightly below FY2019-23's $911.6-959.4M) to $1,012.4M (FY2021-25, depreciation end, 1.64%).
- *Is that range too wide to reach a conclusion?* **No, for Q4's purpose:** the width is growth (organic and bought), not a cycle that returns to zero; every window and both ends are positive, and the longer the window the lower the figure. For Q5 the whole range, and the TTM, sit below the bond, so the width changes no verdict there either.
- *The distorted years, named [E5-11]:* FY2017-FY2018 (Ixia's purchase and a *"northern California wildfire"*, the FY2018 goodwill impairment non-cash), FY2023 (the swap proceeds), FY2024 (the tax receivable and a 9% revenue fall). None turns a window negative.
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** D&A is the default proxy [E3-44, E2-41]; this is not the capital-intensive class; the depreciation end is admissible and the capex end is shown beside it. **Band used: capex end to depreciation end; the conservative figure in any Q5 arithmetic is the lower of the two in each window.**
- **Stock compensation subtracted in full [E5-06]:** $162M in FY2025, $214M in the TTM, the face line. **[E3-70]'s market-value measure:** the grant-date value of awards granted is not separately taken here; the charge is the floor of the subtraction, stated as such.
- **The screen's `oe_bottom_m` 879 reproduces within 0.2% as the five-year depreciation-plus-amortization end ($880.8M)**, the end this run does not use; `oe_top_m` 978 reproduces at no end exactly (nearest the three-year capex end, $985.3M).

### Great, good, or gruesome? **[E4-20]**
- [ ] great
- [x] **good** — attractive return, earned also on added capital, but less on the added than on the base
- [ ] gruesome
- Evidence: the instrument business earns 46-77% pre-tax on its own net tangible capital (FY2019-FY2025, Q2) and needs capex of 2.4-3.6% of revenue: the base account is close to [E4-20]'s great one. But the company's growth since FY2015 was bought with about $6.2bn of acquisition cash (including the ESI minority), about 82% of the period's owner earnings ($7,511M at the capex end), and the return on all capital including the purchases is 13.4-16.3% in FY2024-FY2025. Deposits added earn an attractive rate, below the base; that is the good account [E4-43], and it passes.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **yes.** Owner earnings positive in every year FY2013-FY2025 at both ends, never below $180M, $1.1-1.3bn in FY2025 and the TTM; the one filed collapse (FY2002-FY2003, Q2) predates the spin.
- (2) massive liquid assets: **yes.** Cash and equivalents $2,605M at 2026-07-31; the $750M revolver to April 2031 is undrawn and is not counted [E5-39].
- (3) **no significant near-term cash requirements:** **met.** The **$700M of 4.60% senior notes due April 6, 2027** fall due in seven months, and the cash on hand is 3.7 times them; next, $500M of 3.00% notes in October 2029, $750M of 5.35% notes in July 2030 and $600M of 4.95% notes in October 2034. No covenant bites while the revolver is undrawn (*"a requirement to maintain compliance with specified financial ratios"* applies to it). Standby letters of credit and bonds $54M.
- Leverage, named and quantified **[E4-16, E3-29]**: senior notes $2,550M par against cash $2,605M, net cash about $55M; equity $6,571M. **[E2-54]'s coverage:** TTM interest expense $108M ($96M FY2025 + $80M − $68M for the nine-month periods) against TTM owner earnings of $1,240-1,255M that are already after interest: covered more than eleven times out of cash flow net of capex.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- The mechanism: **#10 THE CAMOUFLAGE** (`Screens/SURVIVAL SHAPES - index.md`), with **#20 THE WAVE** as a feature. The instrument franchise's cash is recycled into purchases of network-test and design-software businesses that must re-win their races each product cycle (Ixia, Eggplant, ESI Group, Spirent, OSG), so the company lives and grows while the owner's return on what has been paid falls toward the purchases' return. The wave: the FY2019-FY2023 margin rise and the FY2026 revenue jump ride the 5G build and AI data-centre spending; when a wave ebbs (FY2024: revenue −9%, operating margin 24.9% to 16.7%) the fixed R&D and sales cost stays.
- Quantified from filed figures, and the resulting outcome: purchases about $6.2bn FY2015-FY2025 against $7,511M of owner earnings; **Ixia, $1,622M, written down by $709M (44% of its price) within eighteen months**; goodwill and other intangibles **$4,575M at 2026-07-31 (*"Goodwill | 3,462"*, *"Other intangible assets, net | 1,113"*)**, about 2.4 times the business's own net tangible capital ($1,908M at 2026-07-31: equity $6,571M plus notes $2,517M less cash $2,605M, goodwill and intangibles); pre-tax return on all capital 13.4% in FY2025 against 56% on the tangible base. **The depression case, modelled [E3-24]:** a repeat of FY2002 (revenue −43%, operating margin −27%) on TTM revenue of $6,582M would be an operating loss of about $1.0bn in a year; cash of $2,605M covers that year and the April 2027 notes together, so it is distress, not death. **Exposure, not experience [E4-40]:** about 41% of revenue is billed in the Americas and 41% in Asia Pacific (*"We have experienced forced reductions in sales and been prevented from selling large orders to certain key customers due to trade restrictions"*, FY2025 10-K), and tariffs cut FY2025's gross margin; export controls on sales into China are an exposure the filings name without a figure.
- Likelihood: [ ] likely **[x] a real possibility** (the camouflage: the owner's return compressed toward the purchases' 13% while the base keeps earning) · [x] a low-level possibility (the depression case as distress)
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____** — **IN, GOOD.** Owner earnings positive in every filed year and rising across the rolling five-year windows ($373.8M to $1,012.4M, one small dip), $967.0-1,012.4M on the default window and $1,240-1,255M on the TTM; net cash; the April 2027 notes covered 3.7 times by cash; interest covered more than eleven times. Named death #10 THE CAMOUFLAGE with #20 THE WAVE as a feature, a real possibility for the owner's return, not for survival.
