## SELF-AUDIT
- [x] Questions answered in order; **Q2 is the first non-IN and it closes the file**; Q3 and Q4 are
      recorded under an explicit NOT GOVERNING banner at the brief's instruction; Q5 is headed
      COMPUTATION — NOT A CLEARANCE and carries no entry language; Q6 arms nothing
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** — Q1 IN rests on the
      filed mechanism; two general-knowledge statements found in my own drafts (the fate of the
      prior holder of the CNR ticker; Arch's bankruptcy history) were deleted before commit because
      no filing read here states them
- [x] Every UNRESEARCHED verdict names the artifact — **none used**
- [x] Every UNKNOWABLE verdict states what cannot be known — none governs; Q4 records that the
      owner-earnings range is too wide for a conclusion [E4-25], and names why (the price)
- [x] Step 0: the filing was read, with accession numbers; figures cross-checked — FY2025 OCF
      $305,752K, SBC $32,918K, D&A $621,067K, capex $(284,581)K against XBRL; Arch FY2023 OCF
      $635,374K, SBC $25,443K, capex $(176,037)K; the S-4/A pro forma revenue reproduced as the
      arithmetic sum to the thousand; three peer figures re-verified in the cached peer filings
- [x] **Merger perimeter handled explicitly**: close date and exchange ratio from the 8-K; the 8-K/A
      opened (it incorporates, it does not contain) and the S-4/A pro forma read at source; pro forma
      owner earnings built by adding two sets of audited cash-flow statements; the holes named (Arch
      Q4 2024 unfiled, the 13-day stub, synergies); no mean mixes standalone CONSOL with Core; every
      window published
- [x] Owner earnings on multi-year means; seven windows stated; (c) disclosed as a judgment with
      [E5-20] applied (D&A end invalid, twice); finance-lease principal included; SBC verified
      resolved and complete; [E4-41] normalization stated
- [x] Competitor row filled — 6 companies with filed per-ton series across three coal classes, of ~25
      named competitors; foreign and private limits stated, with the reason the class is NONE rather
      than PROVISIONAL
- [x] Sovereign is for the earnings currency, from the issuing authority (US Treasury), dated 2026-09-11
- [x] Value stated as round-number arithmetic at the floor, not a point estimate, under the
      computation heading
- [x] No bar chosen — both closed by Q2; windage count 0
- [x] Price dated (2026-09-11 close); aggregator used for the live quote only and flagged
- [x] Run committed to git with a pathspec after every section (Step 0, Q1, Q2, Q3-Q6, register)

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line: FAIL at Q2 (OUT, on the business).** Core Natural Resources is a price-taker by its own
  description — *"numerous producers selling into all markets that use coal"* — whose cost position
  is second to Warrior's in met coal, level with or behind Alliance and Peabody in thermal and the
  PRB, and whose costs ratcheted faster than its peers' through the 2022 spike and its unwind, so the
  low-cost exception of [E2-58] is neither wide ($6.23 met and $1.31 PRB margin per ton in 2025) nor
  sustainable (+40% met, +45% PAMC cash cost per ton, 2021-2025).
- **Price: $97.47** (2026-09-11) × 49,636,257 = **$4,838.0M**. COMPUTATION — NOT A CLEARANCE: yield
  **−0.5% to 18.3%** across the published windows; **2.0%** on the [E4-41]-normalized record; the ~10%
  floor is cleared only by windows containing 2022-2023.
- **Recorded, not governing:** Q3 IN (no disqualifier) with a live capital-allocation flag and
  converging presentation flags; Q4 OUT on staying power, the range too wide for a conclusion.

### PRIORS — which were refuted [E4-26]
- **Q2 OUT — NOT refuted.** The bull case was built first; its best fact (a $28.48 met margin in Q2
  2026 while Peabody's seaborne met lost $7.04) is real, and did not make one quarter "wide".
- **"The Pennsylvania Mining Complex's longwall cost position is the bull case" — REFUTED in part.**
  The PAMC's filed cash cost ($40.99, 2025) is *above* Alliance's Illinois Basin ($34.71); its margin
  premium came from export prices and fell from +$21.27 (2023) to +$1.97 (2025). **The stronger
  cost-position case in this company is the Leer Complex, and even there Warrior is lower.**
- **"Q4 is where a coal company dies" — CONFIRMED in substance, REFUTED in mechanism.** Not a debt
  death — funded debt is $447.6M, mostly long-dated tax-exempt bonds; the claims that matter are
  reclamation, black lung and retiree medical (~$1.17bn with workers' comp and the Coal Act), and the
  balance sheet that stood between them and the cycle was paid out.
- **[E5-20] "the D&A end may be INVALID" — CONFIRMED, and in the opposite direction after the close**:
  post-close D&A ($621M) overstates maintenance because of the ~$1.4bn purchase-price step-up, while
  pre-close D&A understated it in 2019-2022.
- **"Get the pension" — the pension is not the claim.** The qualified plan is overfunded by $49.6M;
  the unfunded senior claims are OPEB ($205.5M) and black lung ($285.7M).
- **"Q1: can the cash flows be predicted at all [E3-31]"** — answered from the filed volatility: the
  mechanism is simple, the level is not stable; carried to Q2 and Q4 rather than closed at Q1 (the
  OXY precedent).

### THE STRONGEST SINGLE FACT AGAINST THIS CONCLUSION
**In Q2 2026, with the Leer South longwall restored, Core's met segment earned $28.48 a ton at an
$85.65 cash cost while Peabody's seaborne met lost $7.04 and Coronado's Australian operations lost
$26.90 a tonne over the half.** That is a cost position above the marginal producer at a trough price
— exactly the shape the [E2-58] exception describes. The file's answer: it is one quarter; the full
year 2025 margin was $6.23; Warrior's was wider in every year; and the five-year cost trend runs the
wrong way. **If the next eight quarters show Q2 2026's spread held against the whole row, Q2 reopens
(Q6, condition 1).**

### TOOLING DEFECTS FOUND
1. **`tools/run.py` has no perimeter guard.** It priced CNR at a 3.44%-6.58% yield by averaging
   standalone CONSOL FY2023-FY2024 with combined Core FY2025 over the combined cap — the exact error the
   queue regeneration refused. The guard lives in one path and not the other: another two-paths split
   of the kind the resume note records (capitalised software, the share-count denominator, the
   restatement vintage, `run.py`'s vintage routing).
2. **`Screens/2026-09-01 MASTER RUN QUEUE.csv` maps CNR to "Cornerstone Building Brand · Silver
   Ores"** — a stale ticker-to-name mapping in a superseded file; the corrected queue carries no CNR
   row. Harmless now; a reader of the old file would have been told the wrong company.
3. **No tool reads finance-lease principal into (c).** Core buys mining equipment through finance
   leases ($57.7M → $127.5M in six months; $66.1M of non-cash equipment financing in H1 2025); an
   owner-earnings construction that subtracts only `PaymentsToAcquirePropertyPlantAndEquipment`
   understates maintenance on every equipment-lease-heavy miner. **A prompt, not a new number** — the
   run subtracted the filed financing line by hand.
4. **Arch's reclamation-fund contribution sits inside operating cash flow** ($116.0M in 2022) — a
   screen reading OCF sees a restricted-asset transfer as an operating cost. Displayed, not adjusted.
5. **The S-K 1300 "average cash cost per short ton" in reserve footnotes is an untapped time series**
   (Leer South $52.39 → $75.99, Arch 10-Ks FY2021 → FY2023): a qualified person's own cost assumption,
   filed yearly, and a direct [E2-58] sustainability read for every US miner. Not built; recorded.

### DEFECTS IN THE BRIEF
1. **"Arch filed its own 10-Ks through FY2023; CONSOL through FY2024"** is right, and the brief did not
   draw the consequence: **Arch's Q4 2024 cash flow was never filed by anyone**, so a pro forma FY2024
   cannot be built from filed statements alone. The run used Arch's four quarters to 2024-09-30 and
   labelled the misalignment.
2. **"Read the pro forma financial information the company itself filed (8-K/A or S-4) and reconcile
   to it"** — the filed pro forma has **no cash-flow statement**, so owner earnings cannot be reconciled
   to it directly; the reconciliation was done to revenue (exact to the thousand) and to the
   net-income bridge (identifying which adjustments are cash). The instruction assumed a line that
   does not exist.
3. **"Teck/BHP/Glencore (foreign — state the limit)"** omitted the one foreign-operations met producer
   that files US-GAAP 10-Ks: **Coronado Global Resources**, whose Australian series is the only filed
   marginal-producer comparator — and it supplied the bull case's best contrast.
4. **The six named survival shapes did not contain this one.** Core is nearest SWK (a distribution
   not funded by owner earnings) but spent an acquired balance sheet rather than selling the
   business; the file names a seventh, THE LONG TAIL ON A SHORT CYCLE.
