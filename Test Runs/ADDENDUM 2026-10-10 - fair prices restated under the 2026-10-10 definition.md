# ADDENDUM 2026-10-10: fair prices restated under the 2026-10-10 definition

Operator rule 6: a run file is never edited. This addendum restates, for the record, a single reporting
figure for each run named below; it does not touch any run file, and it is not a new verdict, a new box, or
entry language. No framework rule changed today's definition of a hold or a buy; Q7's STOP and VERDICT in
every run file named below stand exactly as written.

**The definition applied** (`Framework/THE FRAMEWORK v5.md`, Part VII, "How the fair price is computed,"
adopted 2026-10-10): each end case of the run's value range is valued with its own cash stream discounted
at ten percent instead of the long government rate; the fair price is the average of the two, per share, on
the all-equity basis less net debt. Q7's specific (c) as amended the same day: after year ten, when growth
stops, the acquisition spending stops with it; the business is valued at no growth on owner cash before
purchases. Applied here only to a case that deducted acquisitions from B in years 1 to 10 of its own
construction; years 1 to 10 are unchanged (the run's own B and g), and only the year-11-onward perpetuity
level changes, from B after purchases to B before purchases (grown at the same g for ten years, then held
flat: the reading that reproduces Chipotle's own native construction, the one run that already carries
this exact mechanism in its own words; see the CMG row).

**What this figure replaces.** The restated fair price below replaces the alert a stale "fair price"
field would otherwise keep sending (price-alert tooling reads a single reporting figure, per
`tools/price_alerts.py`'s description in the map). It does not replace the run's own record: the run's own
stated value range, fair price (or fair-price band), cheap price and VERDICT are exactly as filed, and the
box in every run below is unchanged. Where a run's own text is quoted below it is quoted, not edited.

**The check.** For every row, the two end cases' B and g were used to rebuild the run's own value range at
the run's own long rate; the rebuilt range is compared to the run's stated range. A row whose rebuilt range
is within 3% of the run's own is restated; a row whose rebuilt range misses by more than 3%, or whose
construction does not reduce to a single pair of (B, g, r) cash streams at all, is marked NOT RESTATED with
the reason, per the instruction, rather than forcing a number.

The arithmetic is in one script, `restate_fair.py`, with every input commented to its source line in the
run file (so each row below can be checked against its source in under two minutes); its JSON output is
`restated_fair.json`.

No em dashes are used in this file.

---

## The table

Dollar figures are per share. "Deducted" states whether that end case's B deducts acquisitions in years 1
to 10 of its own construction (and therefore gets the amended-(c) tail at 10%); "n/a" means acquisitions do
not arise in that case (organic pair, maintenance-only basis, or an immaterial amount).

| Ticker | Run file | Run's fair price (old) | Low end: B, g, deducted | High end: B, g, deducted | Net debt ($M) | Shares (M) | Range check (mine vs run's, at the run's rate) | Restated fair price |
|---|---|---|---|---|---|---|---|---|
| HUBB | 2026-10-05 Run - HUBB Hubbell.md | no single figure; fair-price band $204-$259, cheap ~$129 | B=774.8 (core 639.8 + NSI 135), g=0%, no | B=774.8, g=7.2%, no | 3,000.0 (NSI financing only) | 52.83 | $203.71-$404.32 vs $204-$405 | **$137.02** |
| ETN | 2026-10-05 Run - ETN Eaton.md | no single figure; fair-price band $118-$122, cheap ~$67 | B=2,587, g=0%, no | B=2,587, g=8.7% (capped), no | 0 | 388.4 | $118.31-$235.79 vs $118-$238 | **$94.09** |
| V | 2026-10-06 Run - V Visa.md | no single figure; fair-price band $167-$242, cheap ~$114 | B=17,742, g=0%, no | B=17,742, g=10.28%, no | 0 | 1,876.0 | $167.09-$376.92 vs $167-$377 | **$143.74** |
| MWA | 2026-10-05 Run - MWA Mueller Water Products.md | $13.40 | B=94.3, g=0%, no | B=94.3, g=5.63% (capped to the rate), no | 0 | 156.13 | $10.73-$16.77 vs $10.73-$16.76 | **$7.47** |
| CSW | 2026-10-05 Run - CSW CSW Industrials.md | $85 | B=115.3, g=0%, no | B=115.3, g=5.63% (capped to the rate), no | 843.6 | 16.29 | $73.93-$144.71 vs $74-$145 | **$35.71** |
| POOL | 2026-10-05 Run - POOL Pool Corporation.md | $130 | B=472.6, g=0%, no | B=472.6, g=2.4%, no | 0 (equity-only basis) | 36.341 | $229.76-$277.85 vs $229.76-$278.38 | **$141.59** |
| REYN | 2026-10-06 Run - REYN Reynolds Consumer Products.md | $16.14 all-equity / $18.88 equity-only (a different, midpoint-growth case) | B=284.4, g=0%, no | B=284.4, g=2%, no | 0 (equity-only basis used for these two ends) | 210.79 | $23.84-$27.93 vs $23.84-$27.93 | **$14.48** |
| ABG | 2026-10-05 Run - ABG Asbury Automotive.md | $216 (whole-cycle central) | B=349 (whole-cycle), g=-5.2%, no | B=349, g=0%, no | 0 | 17.952 | $229.55-$345.31 vs $230-$345 | **$166.10** |
| PBH | 2026-10-05 Run - PBH Prestige Consumer Healthcare.md | $47.74 | B=349.6 (pro forma, after tax), g=-1.68%, no | B=349.6, g=0%, no | 2,126.5 | 47.374522 | $69.31-$85.49 vs $69.32-$85.48 | **$24.97** |
| CAT | 2026-10-06 Run - CAT Caterpillar.md | no single figure; a table of prices at which cases clear the floor under different tax readings ($394-$664 on the shown-growth case) | B=7,800 (MP&E basis), g=0%, no | B=7,800, g=12.1%, no | 0 | 459.675 | $299.80-$780.08 vs $300-$781 | **$281.63** |
| TRV | 2026-10-06 Run - TRV Travelers.md | $196 (central), $142 (mature-years variant) | n/a | n/a | n/a | n/a | n/a | **NOT RESTATED**: insurer under the sector method: value is two components (investments net of float; developed accident-year underwriting) plus a judgment, not a single B/g stream |
| SHW | 2026-10-06 Run - SHW Sherwin-Williams.md | $161 ($199 depreciation variant) | B=1,921.5, g=0%, no | B=1,921.5, g=6.0% (endpoint), no | 0 | 242.758 | $139.85-$224.98 vs $140-$225 | **$99.37** |
| AXP | 2026-10-06 Run - AXP American Express.md | $173 | B=6,884, g=0%, no | B=6,884, g=7.67% (net-income growth, capped), no | 0 | 675.31 | $180.10-$330.69 vs $180-$331 | **$137.51** |
| HD | 2026-10-06 Run - HD Home Depot.md | "fair" band $116.55-$153.50, "cheap" $140.94 | B=14,062, g=-2.84%, no | B=14,062, g=0%, no | 0 | 997.69 | $199.11-$249.02 vs $199.08-$249.02 | **$128.76** |
| MCD | 2026-10-06 Run - MCD McDonalds.md | $138.83 | B=6,577, g=0%, no | B=6,577, g=2.19% (log-trend), no | 0 | 707.65 | $164.21-$195.29 vs $164.20-$195.34 | **$100.41** |
| HON | 2026-10-06 Run - HON Honeywell.md | ~$66 (~$89 with the Quantinuum stake) | n/a | n/a | n/a | n/a | n/a | **NOT RESTATED**: a post-spin entity with three filed years, reconstructed by two methods that disagree in the sign of growth, so each end is a band of bases ($1,560M-$2,260M), not one B |
| PG | 2026-10-06 Run - PG Procter & Gamble.md | $83 ($92 at the top case) | B=14,087, g=0%, no | B=14,087, g=2.91% (shown), no | 0 | 2,391.1 | $104.09-$131.07 vs $104.09-$131.04 | **$65.38** |
| WMT | 2026-10-06 Run - WMT Walmart.md | $19.67 ($24.61 at the Q3 cap) | B=9,591, g=0%, no | B=9,591, g=2.8% (shown), no | 0 | 7,936.2 | $21.35-$26.65 vs $21.36-$26.66 | **$13.36** |
| KO | 2026-10-06 Run - KO Coca-Cola.md | $27.53 | B=10,260 (levered, recast), g=0%, no | B=10,260, g=0.38%, no | 0 (levered/equity basis; the run's separate $27,172M net debt prices a different unlevered variant) | 4,303.4 | $42.12-$43.41 vs $42.13-$43.40 | **$24.15** |
| PM | 2026-10-06 Run - PM Philip Morris International.md | $70.27 | B=9,373, g=-1.06%, no | B=9,373, g=0%, no | 0 | 1,558.613 | $97.72-$106.25 vs $97.72-$106.25 | **$58.07** |
| ADP | 2026-10-06 Run - ADP Automatic Data Processing.md | $171 | B=3,554.2, g=0%, no | B=3,554.2, g=5.66% (capped to the rate), no | 734.7 | 397.263 | $156.22-$245.69 vs $156-$246 | **$108.88** |
| GD | 2026-10-06 Run - GD General Dynamics.md | $274 | B=3,391.8, g=0%, no | B=3,391.8, g=3.67% (endpoint), no | 0 | 271.2 | $220.97-$295.52 vs $221-$296 | **$142.90** |
| COST | 2026-10-06 Run - COST Costco Wholesale.md | $173 (operating cash) / $195 (with net cash) | B=5,085 (five-year mean), g=0%, no | B=5,085, g=10.2% (endpoint), no | 0 (operating-cash basis; net-cash variant is a reported sensitivity) | 442.5 | $203.03-$455.12 vs $203-$453 | **$174.00** |
| BRK.B | 2026-10-05 Run - BRK.B Berkshire Hathaway.md | not reported in the run (component build, no single "fair price" line) | n/a | n/a | n/a | n/a | n/a | **NOT RESTATED**: conglomerate under the sector method: investments net of float plus operating earnings built up part by part (BNSF, BHE, MSR, Pilot, the insurers' underwriting) plus a judgment; no single B/g stream exists |
| TSCO | 2026-10-05 Run - TSCO Tractor Supply.md | not reported in the run (this run has a value range and THE BOX but no labelled fair/cheap price line) | B=557.4, g=0%, no | B=557.4, g=10.2% (shown), no | 0 | 521.04 | $19.00-$42.63 vs $19.00-$42.65 | **$16.20** |
| ATR | 2026-10-07 Run - ATR AptarGroup.md | $28.37 | B=318.9 (whole-cycle maintenance basis), g=0%, n/a | part-by-part (Pharma 77.1% of segment profit applied to the cash base, net of $172M growth spending, 5.0% growth, reverting after year 10) | 1,216.6 | 63.58 | best reconstruction gives $69.80-$52.08 against the run's $69.80-$76.99 (32% miss on the high end) | **NOT RESTATED**: the 77.1% figure is a segment-profit share, not a cash share, and the run does not state the Pharma-only cash figure directly; the reconstruction misses the stated high end by about 32% |
| BMI | 2026-10-07 Run - BMI Badger Meter.md | $77.15 (reported after this run's own re-look; see its file) | B=55.6 (window, acquisitions deducted), g=0%, yes (B before = 105.5) | B=55.6, g=7.2% (cut back), yes (B before = 105.5) | -83.7 (net cash) | 28.987 | $36.90-$63.08 vs $36.93-$63.29 | **$38.20** |
| CB | 2026-10-07 Run - CB Chubb.md | $115.5 (all-equity, central midpoint) | n/a | n/a | n/a | n/a | n/a | **NOT RESTATED**: insurer under the sector method: investments net of float plus developed accident-year underwriting plus a judgment; the growth case's terminal value is built component by component |
| CHD | 2026-10-07 Run - CHD Church & Dwight.md | $32.44 (the run's own midpoint-stream reading, not an average of two separately-discounted end values) | B after=581.7, g=5.06%, yes (B before=904.1) | B=992.5 (maintenance-only, already before purchases), g=0%, no | 2,001.4 | 237.204 | $56.51-$65.75 vs $56.49-$65.75 | **$34.13** |
| CL | 2026-10-07 Run - CL Colgate-Palmolive.md | $29.83 | B after=2,593, g=0%, yes (B before=2,813.4, derived) | B after=2,593, g=5.79%, yes (B before=2,813.4, derived) | 6,404.0 | 797.17 | $49.64-$83.25 vs $49.64-$83.25 | **$33.91** |
| CMG | 2026-10-07 Run - CMG Chipotle.md | $13.02 | B=1,240.6 (maintenance-only, already before purchases), g=0%, no | B after=1,003.6, g=8.1% (cut back), yes, native to the run's own construction (B before=1,240.6, grown) | -775.0 (net cash) | 1,265.4 | $18.00-$31.52 vs $18.00-$31.52 | **$13.24** |
| CSL | 2026-10-07 Run - CSL Carlisle.md | $143.72 ($183.65 equity-only) | B after=486.85 (uncredited margin, year-1 cash $494.0), g=1.48%, yes (B before=747.0) | B=931.8 (credited margin, maintenance-only, already before purchases), g=0%, no | 2,224.6 | 39.714 | $188.37-$359.99 vs $264.23-$359.99 (29% miss on the low end) | **NOT RESTATED**: the reconstructed low end misses the run's own stated bottom by about 29%; the credited/uncredited margin convention does not reduce cleanly to the B derived from the stated year-1 cash figure |
| CTAS | 2026-10-07 Run - CTAS Cintas.md | $51.72 | B=1,606.4 (maintenance-only), g=0%, n/a | B=1,377.0 (all-spending), g=11.08%, n/a | 2,196.0 | 400.17 | $65.69-$141.15 vs $65.69-$141.17 | **$51.72** |
| ECL | 2026-10-07 Run - ECL Ecolab.md | nil (default pair); $30.29 (organic pair) | B after=656.7, g=0%, yes (B before=1,690.9) | B after=656.7, g=7.71%, yes (B before=1,690.9) | 12,790.9 | 280.2 | $(4.09)-$30.92 vs $(4.09)-$30.89 | **$8.09** |
| EFX | 2026-10-07 Run - EFX Equifax.md | nil (default pair); $38.51 (organic pair) | B after=23.8, g=0%, yes (B before=767.7) | B after=23.8, g=7.09%, yes (B before=767.7) | 5,315.2 | 117.485 | $(41.65)-$(38.94) vs $(41.64)-$(39.20) | **$(6.16)** |
| EPAC | 2026-10-07 Run - EPAC Enerpac.md | $11.12 | B=55.8, g=0%, n/a (acquisitions average $1.8M/yr, immaterial) | B=55.8, g=3.9%, n/a | 69.1 | 51.138 | $18.00-$25.01 vs $18.00-$25.08 | **$11.23** |
| ITW | 2026-10-07 Run - ITW Illinois Tool Works.md | $68.04 ($92.33 equity-only) | B after=2,672 (cycle base 2018-2025), g=0%, yes (B before=2,693.5, derived from the per-year table) | B after=2,672, g=1.62%, yes (B before=2,693.5) | 8,855.0 | 284.8 | $135.26-$158.03 vs $135.29-$158.06 | **$68.50** |
| JKHY | 2026-10-07 Run - JKHY Jack Henry.md | $52.52 | B after=272.8, g=0%, yes (B before=327.2, given directly) | B after=272.8, g=8.05%, yes (B before=327.2) | 70.7 | 70.11 | $67.98-$129.58 vs $67.98-$129.58 | **$57.11** |
| AME | 2026-10-10 Run - AME AMETEK.md | $(7.18) (central); $42.53 (organic pair) | B after=294.9, g=0%, yes (B before=1,427.2, given directly) | B after=294.9, g=12.10%, yes (B before=1,427.2) | 6,540.8 (incl. Indicor's $5,000.0M) | 229.261244 | $(5.56)-$31.34 vs $(5.56)-$31.35 | **$32.18** |
| LOW | 2026-10-10 Run - LOW Lowe's.md | $92.61 ($126.20 equity-only) | B after=6,281 (cycle base 2019-2025), g=0%, yes (B before=7,932, the organic pair's base) | B after=6,281, g=7.97%, yes (B before=7,932) | 34,149.0 | 561.054 | $139.04-$315.47 vs $139.05-$315.46 | **$110.05** |
| MA | 2026-10-10 Run - MA Mastercard.md | $240.00 ($248.96 equity-only) | B after=10,465, g=0%, yes (B before=11,917, the organic pair's base) | B after=10,465, g=17.1%, yes (B before=11,917) | 14,534.0 | 875.9 (derived; the run does not restate the share count in its Q7 excerpt) | $196.76-$803.61 vs $196.74-$801.66 | **$259.13** |
| MSA | 2026-10-10 Run - MSA MSA Safety.md | $47.70 | B=236.0 (organic pair), g=0%, n/a (acquisitions left out entirely) | B=236.0, g=4.96%, n/a | 954.7 | 38.578 | $84.49-$137.22 vs $84.50-$137.29 | **$48.82** |
| NDSN | 2026-10-10 Run - NDSN Nordson.md | $77.15 | B=563.1 (no acquisitions), g=0%, no | B=563.1 grossed, g=9.42%, yes (acquisitions carried at 83.7% of the growing base through year 10, reverting to the before-acquisitions, grown level from year 11) | 1,636.3 | 55.69 (derived) | $151.18-$248.36 vs $151.16-$248.42 | **$77.13** |
| ORLY | 2026-10-10 Run - ORLY O'Reilly Automotive.md | $38.12 | B=2,667 (maintenance-only), g=0%, no | B=2,221 (all-spending), g=11.25%, no | 6,752.4 | 808.961 | $50.52-$111.20 vs $50.53-$111.16 | **$38.12** |

---

## Notes on method, for the record

1. **Where the run's own reported "fair price" already matches today's definition** (CTAS, ORLY, and very
   nearly NDSN), the restated figure equals or nearly equals the run's own figure: those runs already read
   "the midpoint of the range earns the floor" as "each end stream valued at 10%, averaged." Other runs read
   the same sentence differently (the stream at a blended midpoint growth rate: CHD; half the shown growth:
   several of the 2026-10-05/06 runs' now-superseded fair-price-band convention), and for those the restated
   figure differs, sometimes by a wide margin, from the run's own number. That difference is the point of
   today's one stated definition.
2. **Net debt.** Where a run's own value range already subtracts net debt (or its parts, debt and cash) to
   reach the per-share figures for its own two end cases, that same net debt is used here (CSW, ADP, PBH,
   CTAS, ORLY, and the whole 2026-10-07/2026-10-10 batch generally). Where a run's range is built on owner
   cash already stated after interest (an equity-only basis) and the run itself draws no further net-debt
   line through those two end cases, no net debt is subtracted here either, and the row says so; this
   matches a large group of the 2026-10-05/06 runs (HUBB, ETN, V, MWA, POOL, ABG, CAT, SHW, AXP, HD, MCD, PG,
   WMT, PM, GD, TSCO, KO, REYN) where the range itself carries no net-debt line.
3. **The amended specific (c) tail.** Confirmed against Chipotle's own native construction (the one run
   that already states, in its own words, that its growth case "revert[s] to... maintenance-only cash" after
   year ten): the reversion level is the before-purchases base grown at the same rate for ten years, then
   held flat, not the un-grown base held flat from year one. The same grown-terminal reading is used for
   every amended row (BMI, ECL, EFX, ITW, JKHY, AME, LOW, MA, CHD, CL, NDSN).
4. **ATR and CSL are NOT RESTATED** even though named for amendment, because the reconstruction from each
   run's own stated figures misses that run's own stated range by more than 3% (32% and 29% respectively);
   forcing a number past that would not be arithmetic on the run's own figures, which the operator's
   instruction says to avoid.
5. **CB, BRK.B and TRV are NOT RESTATED** because their Q7 is the sector method for insurers (and, for
   BRK.B, the conglomerate built the same way): two components plus a judgment, never a single owner-cash B
   and growth-rate g stream. **HON is NOT RESTATED** because its post-spin record is three years reconstructed
   by two methods disagreeing in the sign of growth, carrying a band of bases at each end rather than one B.

**Count: 38 restated, 6 NOT RESTATED (ATR, CSL, CB, BRK.B, TRV, HON), 44 total.**
