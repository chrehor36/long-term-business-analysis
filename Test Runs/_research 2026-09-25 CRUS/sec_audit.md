## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Step 0, Q1 IN, Q2 OUT; Q3-Q6 marked NOT REACHED and their
      material recorded beneath the close without verdicts.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 IN rests on the 10-K's own
      description, confirmed clause by clause.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives: none issued. The five unobtained peers are
      named at Q2 with their exchanges and the rung not attempted.
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: none issued; the perimeter close was
      considered at Q2 and refused in writing.
- [x] Step 0: the filing was read, with accession number; a figure was cross-checked (FY2026 operating cash $650,598K
      rebuilt from its lines; ties, and its working-capital sum ties to the MD&A's $103.4M).
- [x] Owner earnings on a multi-year mean; five windows stated; capex band disclosed as a judgment (beneath the close).
- [x] Competitor row filled: 6 of 11 named peers plus Qorvo, XBRL transcription flagged; the verdict does not rest
      on the row, and why is stated.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury par curve), dated
      09/24/2026.
- [x] Value stated as a round-number range, not a point estimate (inside a COMPUTATION block only).
- [x] One bar chosen, not both: none; Q5 not reached. Windage count stated (one).
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Run committed to git, with pathspecs, after the claim, after Q1, after Q2 and after this section.

**The brief's priors, scored:**
- *Fabless mixed-signal, fiscal year to late March/early April*: **confirmed.** Product list confirmed (amplifiers,
  codecs, smart codecs; camera controllers, haptics and sensing, battery and power ICs).
- *FY2026 10-K filed, and a 10-Q to 2026-06-27*: **confirmed**: `0000772406-26-000018` (filed 2026-05-21) and
  `0000772406-26-000037` (filed 2026-08-05).
- *One customer, believed Apple, a very large majority*: **confirmed and named by the registrant**: 91% of FY2026 and
  90% of Q1 FY2027. What it means was tested, not assumed, and it is the Q2 verdict.
- *Foundry believed GlobalFoundries, TSMC and others*: **confirmed**; terms read (capacity reservation through calendar
  2026, amended February 2025; $195M prepaid in FY2022, now down to $14.7M; a new process programme at GF's Malta,
  New York fab under the customer's American Manufacturing Program).
- *acq_note $277M inside the window*: **confirmed as Lion Semiconductor (FY2022)**, and the run found what the
  five-year window cannot: Wolfson ($444M, FY2015) behind it, both written down in part. **Nothing deal-shaped live.**
- *Share count fallen through buybacks*: **confirmed**; 63.4M basic weighted (FY2018) to 50.1M on the cover;
  $1,738M of repurchases over twelve years against $723M of SBC.
- *STEP UP flags*: **found and split** into a timing item ($180.3M of prepaid wafers returning through operating cash
  in FY2024-FY2026, stripped), an inventory release, and real operating growth that persisted.

**My own errors, caught before commit:**
1. First wrote the capex range as "$13.9-55.2M" (the low end is $14.0M, FY2026). Corrected.
2. First wrote R&D as "22-24% of sales"; the filed range is 21.7-24.2%. Corrected.
3. First wrote that the "internally develop" risk factor appeared in "every 10-K read, FY2017 to FY2026"; I had
   opened FY2017 and FY2020-FY2026, not FY2018-FY2019. Narrowed to what was opened.
4. First wrote that *"the eleven competitors the 10-K names are the ones those customers chose"*: no filing read says
   which competitor won which lost socket. Removed and replaced with what is filed.
5. First presented the risk-factor language (*"our customers"*, *"some key customers"*) as if it named Apple. It does
   not; the inference is now stated as an inference.
6. First wrote "total capex runs below D&A in eleven of twelve years"; it is ten (FY2015 and FY2018 are above).
7. First computed the no-growth value at the floor by adding cash to owner earnings that already contain the interest
   on that cash (a double count, about $0.3bn). Corrected by removing an estimated $31M of after-tax interest first.
8. First attributed *"(c) must be a guess"* to [E2-23]; the ledger row carrying those words is [E2-09]. Corrected.
9. First wrote the new revolver as "undrawn at 2026-03-28", a date before it existed; now quoted from the 10-Q at
   2026-06-27.

**Errors in the brief:** none of substance found. The brief's "WAVE 7 name 32 of 218" was counted and is right
(line 32 of `_wave7_order.txt`; 31 lines in `_wave7_done.txt` at claim). The brief's ledger count "311 rows at last
count" was counted: `csv.DictReader` returns **311** rows (312 physical lines with the header). The brief's
"newest_filing 2026-03-28 is a period end" is right; the 10-K was filed 2026-05-21.

**Tooling observations (reported, not patched):**
- `tools/run.py CRUS` did **not** miss a filed 10-K (the CLX defect did not recur here): its FY2024-FY2026 columns
  match the filed statements. It **reads capex as purchases of property, equipment and software only and omits
  "Investments in technology"** ($0.7-29.3M a year; $29.3M in FY2018), so its capex end runs slightly high. It also
  prints the three-year window as the headline yield (6.21-6.65%) with the GlobalFoundries prepayment unwind inside
  it; the stripped three-year figure is $310-333M, not $370-396M. The tool prints the divergence warning, correctly;
  it cannot see a prepayment.
- `tools/sources.cik_for()` returns a tuple (CIK, name), not a CIK string; a script passing it straight to
  `sec_facts()` builds a malformed URL. Not a defect in the tool's own callers, a trap for new scripts.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence) [ ] UNKNOWABLE (about my evidence)
- One line: **CRUS FAIL at Q2 (OUT, ON THE BUSINESS). Q1 IN. [E3-03] criterion (2) fails on filed conduct and contract
  terms: the customer that is 91% of sales caps prices by contract, takes scheduled price reductions, buys without
  minimums, can stop with "little or no penalty" and has dual-sourced since the FY2024 10-K, while customers free to
  choose have moved away (non-Apple revenue about $398M in FY2016 to about $180M in FY2026); [E2-53]: one customer, not
  the business, sets how good it will be.** Price $118.80 (2026-09-24, aggregator, flagged) x 50,117,561 shares (10-Q
  cover, `0000772406-26-000037`) = $5,954M; sovereign 5.47% (US Treasury, 09/24/2026).
- **If UNRESEARCHED:** not applicable.
- **If UNKNOWABLE:** not applicable.
