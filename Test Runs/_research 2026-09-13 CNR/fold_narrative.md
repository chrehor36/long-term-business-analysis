
## UPDATE 2026-09-13 - CNR: Q2 OUT, a price-taker whose low-cost position is neither wide nor sustainable
`Test Runs/2026-09-13 Run - CNR Core Natural Resources.md`. **Q1 IN, Q2 OUT, file closed; Q3 recorded IN with a live
capital-allocation flag, Q4 recorded OUT.** Price **$97.47** x **49,636,257 shares** (10-Q cover `0001710366-26-000054`) =
**$4,838.0M**; sovereign **5.35%** (Treasury, 2026-09-11, struck fresh). The run did its own six-step fold.

### THE PERIMETER, HANDLED RATHER THAN AVERAGED
CONSOL + Arch closed **2025-01-14 at 1.326 Arch-for-CONSOL**; 24.3M shares; a ~$1.4bn PP&E step-up. **The 8-K/A was opened:
it incorporates the S-4/A pro forma and contains nothing - and that pro forma has no cash-flow statement.** So pro forma owner
earnings were built by adding two sets of audited cash-flow statements (CONSOL FY2019-24, Arch FY2019-23 plus nine months of
2024), reconciled to the S-4/A combined revenue to the thousand. **The hole nobody flagged: Arch's Q4 2024 cash flow was never
filed** (no FY2024 10-K), so the 2024 pro forma pairs CONSOL's calendar year with Arch's four quarters to September, labelled.
**`tools/run.py` averaged standalone CONSOL FY2023-24 with combined Core FY2025 over the combined cap (3.44%-6.58%)** - the
exact mix the queue guard refused; not used.

### THE FINDING
- **Owner earnings, $M (capex + finance-lease principal):** 2019 PF 175 · 2020 PF -239 · 2021 PF 111 · **2022 PF 1,457 · 2023
  PF 1,089** · 2024 PF 467 · FY2025 -24 · TTM 227 (with ~$97M of Leer South insurance). **2022-23 are 98% of the 2019-23 total;
  the five non-spike years average $98M.** Every window published; the range is the verdict [E4-25].
- **(c) with [E5-20], twice:** pre-close D&A ran below capex in 2019-22; post-close D&A ($621M) is inflated by the step-up. **Finance-lease
  principal belongs in (c)** - the equipment is bought through leases ($57.7M → $127.5M in six months).
- **Q2, the bull case at full strength, then the row.** Leer is *"first-quartile"*; PAMC does 7.45 tons per employee hour; Q2 2026
  met margin $28.48 while Peabody seaborne met lost $7.04. **But Warrior's met margin was wider in every year 2021-25**, on a cost
  that includes freight; Core's 2025 met margin was **$6.23** and PRB **$1.31**; PAMC's cash cost ($40.99) is **above** Alliance's
  Illinois Basin ($34.71); PRB cost is above Peabody's. **Costs ratcheted through the spike and never came back** (met +40%, PAMC
  +45% 2021-25; Warrior +16%) - [E3-62] in a coal ledger. And the company's own words close criterion (2): *"numerous producers
  selling into all markets that use coal"*, its best coal sold as *"a … substitute"*.
- **Q3, the sharpest flags.** **The STIC Adjusted EBITDA was lifted by $75,774,000 of "expected, but not yet received" insurance
  to $587,840,000 - the threshold, to the dollar.** Free cash flow is defined to **include Arch's $217.6M acquired cash** (FY2025
  "$246.1M" is $28.5M without it); the "80% of FCF returned" is **~250% of owner earnings**, and net cash fell from ~$384M at the
  close to ~$26M. The program's own terms: *"funded from available cash on hand or short-term borrowings."* Synergy target raised
  twice, then retired unquantified. Guidance on volume and cost was mostly met - a point for management.
- **Q4, the claims a cash-flow screen never sees:** ARO $534.7M, black lung $285.7M, OPEB $205.5M, workers' comp $87.8M, Coal
  Act ~$29.9M, surety bonds $1.07bn - **~$1.17bn recognized, ~$98M a year of cash, each roughly doubled by the merger.** The
  pension is overfunded.

### PRIORS REFUTED OR CONFIRMED
1. **"Q2 OUT via [E2-58]" - confirmed**, after the bull case was built first; its best fact is one quarter.
2. **"PAMC's longwall cost position is the bull case" - refuted in part:** PAMC's premium was the export price; the Leer Complex is
   the better cost case, and Warrior is lower still.
3. **"Q4 is where a coal company dies" - confirmed in substance, refuted in mechanism:** not debt ($447.6M, tax-exempt, 2035), but
   decades of reclamation, black lung and retiree medical against a years-long cycle, with the buffer paid out.
4. **"[E5-20]: the D&A end may be invalid" - confirmed, and inverted after the close.**
5. **"[E2-49]" - FIRED: twelve fires, seven failures.**

### THE SURVIVAL SHAPE - A SEVENTH: THE LONG TAIL ON A SHORT CYCLE
**Not one of the six.** Nothing is contracted not to stop (ORCL); SBC is not the cash (ARM); seven filed years exist (BE); no cash
undoes past work (BA); nobody lends the balance sheet (ACVA/FLNC). **Nearest SWK** - the distribution was not funded by owner
earnings - **but SWK sold the business and Core spent the balance sheet it acquired**; that part is recorded as SWK's shape in an
acquired-balance-sheet form. **The new element is the tail**: senior claims fixed in dollars and measured in decades (reclamation,
black lung, retiree medical), set against earnings set by a commodity cycle measured in years; survival depends on the average
price across the tail, and the balance sheet is the only buffer between the two clocks. **The register now stands at SEVEN.**

### THE STRONGEST SINGLE FACT AGAINST THE VERDICT [E4-51]
**Q2 2026: met cash margin $28.48 at an $85.65 cash cost, while Peabody seaborne met lost $7.04 and Coronado Australia lost
$26.90 over the half** - a producer above the marginal cost at a trough price. One quarter; Warrior wider every year; the
five-year cost trend the wrong way. Eight more quarters of that spread against the whole row would reopen Q2.

### TOOLING DEFECTS
1. **`tools/run.py` has no perimeter guard** - the guard lives in the queue regeneration only; another two-paths split.
2. **`Screens/2026-09-01 MASTER RUN QUEUE.csv` names CNR "Cornerstone Building Brand · Silver Ores"** - a stale mapping in a
   superseded file.
3. **No construction reads finance-lease principal into (c)**; equipment-lease-heavy miners understate maintenance.
4. **Arch's reclamation-fund contribution ($116.0M in 2022) sits inside operating cash** - a restricted-asset transfer read as cost.
5. **Untapped: S-K 1300 reserve footnotes file a qualified person's "average cash cost per short ton" every year** (Leer South
   $52.39 → $75.99) - a direct [E2-58] sustainability series for every US miner. Not built.

### DEFECTS IN THE BRIEF
1. The pro forma it asked to reconcile to has **no cash-flow statement**; reconciled to revenue and the net-income bridge instead.
2. It did not draw the consequence of Arch's last 10-K being FY2023: **Arch's Q4 2024 was never filed.**
3. "[E2-63] can be decomposed directly" beside units - **E2-63 is the capped-upside row; the units test is [E4-55]** (the NEGG
   run found the same line in its brief).
4. The foreign-peer instruction omitted **Coronado**, the one Australian met producer filing US-GAAP 10-Ks - which supplied the
   bull case's best contrast.
5. "Six named survival shapes" - this is a seventh.

**Count: 80 runs** - gate-clearers 26, **Q2 OUT 51**, Q4 OUT 2, Q1 UNKNOWABLE 1. **Tier 3 still live: RGTI.**
