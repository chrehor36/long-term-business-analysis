
## UPDATE 2026-09-13 - BAM: Q2 OUT, and the block of 2026-09-02 was a scheduling judgment, not a measurement finding
`Test Runs/2026-09-13 Run - BAM Brookfield Asset Management.md`. **Q1 IN, Q2 OUT, file closed; Q3 recorded IN with a live
capital-allocation flag, Q4 recorded IN on survival with staying power 1 of 3, Q5 headed COMPUTATION - NOT A CLEARANCE, Q6
recorded with nothing armed.** Price **$47.26** x **1,597,251,633 economic shares** (Class A 1,597,230,353 + Class B 21,280;
10-Q cover, `0001628280-26-054933`) = cap **$75,486M**; sovereign **5.35% USD** (Treasury, 2026-09-11), struck at Step 0 and
**re-struck unchanged at the resume**. **The run was started at 01:20, killed at 01:44 and finished by a second session from the
drafts on disk.** It did its own six-step fold. **The first of the two names the queue had held BLOCKED since 2026-09-02.**

### THE BLOCK, TESTED RATHER THAN INHERITED
The queue said BAM and BN *"remain BLOCKED and are out of scope … a different perimeter problem, closer to the DKS/HON class."*
Against the filings:
- **The 2025 reorganisation is fully restated.** The ULC was the accounting acquirer, so the FY2025 10-K presents it as
  **Predecessor** and FY2023-25 are one perimeter. The DKS/HON problem - an acquisition sitting inside the owner-earnings window
  unrestated - does not arise.
- **Consolidated funds are small and separately captioned** (BSI II: $505M of investments at 2025-12-31, $3,090M at 2026-06-30),
  each with its own revenue, expense, borrowing, cash-flow and NCI lines, so they strip cleanly. **Oaktree was equity-accounted
  with its own audited statements filed as EX-99.2.**
- **What the block was right about:** **no five-year window on one perimeter exists** (three clean years plus H1 2026; FY2022 is a
  separation year with operating cash of −$374M after a $7,396M affiliate settlement), and **the perimeter moved again on
  2026-07-31** when BAM took control of Oaktree, which consolidates from Q3 2026.
**Both stale lines in the queue were left standing with a dated note beside them (operator rule 6). BN is still unrun and both
still govern it.**

### A FOURTH COMPANYFACTS SPLICE MECHANISM - AND THE FIRST THAT IS A PREDECESSOR RESTATEMENT
Under CIK 0001937926, `NetCashProvidedByUsedInOperatingActivities` holds **two different companies under the same period keys**:
BAM Ltd as the ~27% holder (FY2023 **$508M**, FY2024 **$627M**, accessions `0001937926-24-000004` and `0001937926-25-000007`) and
the ULC-as-Predecessor restatement (FY2023 **$1,439M**, FY2024 **$1,612M**, `0001628280-26-013098`). **`sources.annual()` at its
default `vintage="earliest"` returns {2023: 508, 2024: 627, 2025: 2,101} - a 3.4x step that a screen reads as growth and that is
a perimeter change.** `tools/run.py BAM` (which uses `newest`) refused in words: *"no overlapping OCF/D&A/capex annual facts.
UNRESEARCHED"* - D&A exists only in the newest filing and no capex tag resolves.
**Same class as NEGG's splice and RGTI's colliding de-SPAC keys; a different mechanism - a predecessor restatement filed by a
registrant that had been the minority holder.** The first three were a name change, a de-SPAC and a shell. **No companyfacts row
was used anywhere in this run.**

### A COVER-DEFINITION BREAK THAT READS AS A 2.5% BUYBACK
The **10-K cover** (2026-03-02) reports **1,638,147,590 Class A - the ISSUED count**, including ~29.5M treasury shares held by
escrowed-stock-plan subsidiaries. The **10-Q cover** (2026-08-10) reports **1,597,230,353 - the OUTSTANDING count.** **A screen
reading the two covers in sequence sees a 40.9M-share fall and records a buyback.** Actual H1 2026 net treasury acquisitions:
11,614,867 shares, $592M. **BN's 13D/A computes its own percentage on the issued count**, which is why the two forms coexist in
the same filer's record. Related: **BN's 1,193,021,145 shares are INSIDE the count** (74.7%), so the public float of ~404M shares
would have understated the company by 75% - the float guard earning its keep again.

### THE FINDING - Q2 OUT ON THE COMPETITOR ROW
**Nine SEC-filing peers, one specification** (FY2025 management fees / the average of YE2024 and YE2025 fee-earning capital), each
figure **checked back to that peer's own FY2025 10-K text** rather than to the transcription:

| | fee rate bp | FEAUM CAGR 23-25 | FRE margin |
|---|---|---|---|
| OWL | **145.1** | 35.2% | 56.4% |
| TPG | 117.3 | 11.5% | 45.2% |
| ARES | 108.6 | 21.1% | 41.7% |
| BX | 92.2 *(firm's own 0.86%)* | 9.9% | 58.3% |
| **BAM** | **85.8** *(ex-BWS **99.1**)* | **14.8%** | **54.6%** |
| CG | 74.8 | 4.7% | 46.8% |
| KKR | 73.5 segment | 16.4% | 69.1% |
| APO | 53.1 segment | 19.9% | 56.6% |
| TROW | 39.0 | 10.9% | 29.9% GAAP op |
| BLK | 15.0 | 18.4% | 44.1% adj op |

**Fifth of ten on price, sixth on growth, fifth of eight on margin, inside the pack on duration (87% long-dated or perpetual
against ARES 93%, KKR 92%, OWL 85%). Mid-pack on every column is what a close substitute existing looks like in filed data**, and
[E3-03] criterion (2) fails with the conjunction. BAM's own Item 1 concedes it: *"BAM competes with many other firms in every
aspect of our business."* **All nine peers describe the same discounting behaviour in their own risk factors** - which is as close
as a row can come to the conduct question [E3-61] says it cannot answer.
Three further legs: the rate falls **90.4 -> 85.0 -> 85.8 -> 82.4bp** and H1 2026 fee revenue grew **13% against 19%** growth in
the capital it is charged on [E4-32]; **56.4% of the fee base is replaced or redeemable by design** [E4-04]; and the durable 43.7%
is locked by the **74.7% controlling shareholder** rather than by the customer [E2-59].

### THE DISCONFIRMING READ THAT MADE THE VERDICT HARDER AND THEN SHARPER [E4-26]
The blended fee-rate fall is **MIX, not third-party erosion.** BWS - BN's own insurer - is **$108bn of FBC generating $234M of
fees, 23.4bp** ($92bn and $167M in FY2024). **Ex-BWS the FY2025 rate is 99.1bp and is not falling.** That **defeats** the claim
that BAM's customers are forcing its price down, and it **does not rescue criterion (2)** - 99.1bp is still fourth of ten, and
KKR's and APO's blended rates are depressed by exactly the same mechanism (Global Atlantic, Athene), so a like-for-like
ex-insurance row would lift them too. **What it does instead is sharpen the mix finding: $48.6bn of the firm's $87.3bn of H1 2026
gross inflows - 55.7%, and 70% of the entire $69.4bn increase in Fee-Bearing Capital - came from the controlling shareholder's
insurance balance sheet at a quarter of the third-party price.** The growth carrying the $1-trillion plan is, in the most recent
filed period, **majority related-party capital.**

### PRIORS REFUTED OR CONFIRMED
1. **The brief's prior, that the perimeter is answerable from BAM's 10-K - CONFIRMED.** The run reached a real verdict on the
   business, not a measurement closure.
2. **The queue's 2026-09-02 block - REFUTED as a measurement finding, upheld as a scheduling judgment.**
3. **My own prior, that BAM holds 100% of the manager only since 2025 with BN keeping most pre-2022 carry - CONFIRMED and
   sharpened:** BN takes **100% of mature-fund carry and 33.3% of new-fund carry**, and realized carry to the common holder was
   $51M / $25M / **$0** across FY2023-25.
4. **My own prior, that the cover count understates the economic count or excludes BN - REFUTED in the direction I guessed and
   confirmed in the other:** BN is *inside* the count; the 10-K cover *overstates* it by reporting issued shares.
5. **The draft session's implicit prior that a high fee margin and ~27% on tangible equity evidence a moat - REFUTED at [E3-46]:**
   every name in the row prints a high return on a capital base that is small by construction. A class characteristic shared by
   ten filers is not a relative advantage.

### THE SURVIVAL SHAPE - A NINTH: THE WAREHOUSE
**Not one of the eight.** ORCL contracted not to stop building; ARM's stock pay ate the owners' cash; RGTI sells equity as
revenue; ACVA/FLNC/NEGG borrow a balance sheet. **BAM lends one - to its own funds' deals.** *"The Company earns fees in
connection with bridge financing and **bears the risk associated with syndicating the commitment**"* (10-Q Note 15): **$3.3bn
(end-2024) -> $6.6bn (end-2025) -> $8.0bn (2026-06-30)**, plus $433M of fund guarantees, against **$3.1bn of corporate
liquidity - 2.6x**, with **no filed maturity schedule**. The commitments grew **2.4x in eighteen months in a benign market**,
which is [E4-40]'s exposure-not-experience exactly. **It carries the FIFTH shape's feature - distribution above owner earnings
[E2-60] - in a debt-funded rather than divestiture-funded form**: dividends plus buybacks were **127-179% of owner earnings in
every filed period**, funded by cash ($3,545M at end-2022 to $404M at end-2024), then $2.5bn of notes in 2025 and $1.0bn in April
2026, then $655M of related-party deposits. **The register now stands at NINE.**
**Why the business still survives its own named death:** the near-term cash requirement that fails [E5-11]'s third strength is, in
the main, **the dividend and the buyback - both discretionary.** Cutting the payout releases ~$3.2bn a year immediately while fees
keep arriving on $298bn of committed capital under 10-12 year terms. **[E2-54]**'s coverage test passes at 9-24x with no maturity
before 2030. **The mechanism breaks the distribution, not the company** - insolvency a low-level possibility, the dividend path
breaking a real possibility.

### THE STRONGEST SINGLE FACT AGAINST THE VERDICT [E4-51]
**87% of the fee base is long-dated or perpetual; a closed-end client literally cannot leave for a decade; the listed-affiliate
MSAs *"cannot be terminated without BN's consent"*; and the third-party fee rate is 99.1bp and is not eroding.** The lock is real
and it is stronger than most brands. The verdict turns on the distinction that the lock is on money *already committed*, never on
the next dollar - and nine filers compete for the next dollar, three of them growing faster at an equal or higher price.

### A RESUMED RUN - WHAT THE DRAFTS ON DISK COST AND WHAT THEY NEARLY COST
The killed session left Q3, Q4, Q5 and Q6 written but never appended, with five unresolved placeholders and **two lines that
presupposed a verdict Q2 had not reached**:
1. Q3's weight case read *"[E3-43]'s original form governs **once Q2 has found no franchise**."*
2. Q4's verdict ended *"**if this Q4 were governing**, strength (3) would need the commitment maturity schedule … before an IN
   could be written without a caveat."*
**The second is the more dangerous, and it is a protocol defect as well as a smuggled conclusion**: an IN carrying a caveat is
UNRESEARCHED by the framework's own thin-evidence rule, so the draft's Q4 was only writable as IN *because* Q2 was assumed to have
closed the file first. **Q2 was decided from the filings and the peer row before either line was read back**, and both were
rewritten with the correction recorded in place rather than repaired silently. The Q4 caveat was replaced by a **reason** - the
verdict rests on the coverage test and the contractual fee term, not on the missing schedule, and the failing cash requirement is
discretionary - with the schedule recorded at Q6 as a reopening condition instead.
**The verdict the drafts presupposed and the verdict reached agree. That they agree is not what made the rewriting unnecessary;
the rewriting was done anyway, and the CGNX prohibition is why.**

### TOOLING DEFECTS
1. **`sources.annual()` splices a predecessor restatement onto a minority holder's own history** under one CIK (the fourth
   splice mechanism; see above). The `newest` vintage avoids it here only by refusing outright.
2. **`tools/run.py BAM` returns UNRESEARCHED on a name whose filed statements carry every figure it wants** - D&A is tagged only
   in the newest filing and no capex tag resolves, because this filer's capex is a line called "Other assets."
3. **`cover_shares.py` and any screen reading the cover cannot tell ISSUED from OUTSTANDING**, and this filer uses one form on
   the 10-K cover and the other on the 10-Q cover. **A 2.5% phantom buyback is the visible symptom; the invisible one is a cap
   2.5% too high on the annual date.**
4. **A fee rate computed as GAAP fees over the filer's own capital measure mixes perimeters.** The RMR run of 2026-08-30 printed
   BAM at 56bp that way ($3,384M GAAP fees over $602.7bn of FBC); on one perimeter it is 85.8bp, because GAAP carries Oaktree by
   the equity method while FBC counts it at 100%. **Recorded as a correction to that row, not an edit of it.**
5. **`sources.py`'s EUR leg failed on an SSL certificate verification error** on 2026-09-13. Immaterial here (the earnings
   currency is USD) and recorded, not chased.

### DEFECTS IN THE BRIEF
1. **"the 10-K FY2024 … followed an NT 10-K"** - correct, and the brief's *pre-check* had said the 10-K of 2026-03-02 was the
   first under this CIK. **It is not: the FY2024 10-K of 2025-03-17 (`0001937926-25-000007`) is.** Already recorded at Step 0 by
   the killed session; repeated here because it changes which filing carries the FY2022 Fee-Bearing Capital figure.
2. **The resume brief said the drafts contained "at least one line" phrased as though it knew Q2's verdict. There are two**, and
   the second one (Q4's) also carried a live protocol violation. A brief that says "at least one" is right; a reader who stops at
   one is not.
3. **The brief's inventory said the research folder held "no q2 draft" - correct** - and did not say that `peer_row.md` already
   contained every figure a Q2 needed. It did. **The competitor row cost re-verification, not re-fetching**, which is the
   write-early protocol paying out on the most expensive single artifact in the run.
4. **The brief said the 2026-09-02 queue paragraph and the 2026-09-13 backfill line "both go stale the moment you fold."** Only
   partly: **both still govern BN**, which is unrun. The dated notes say so rather than retiring the paragraphs.

**Count: 81 runs** - gate-clearers 26, **Q2 OUT 51**, Q4 OUT 2, Q1 UNKNOWABLE 2 (HHH, RGTI). *(Counted forward from the register
audit of 2026-09-13, which set the corrected base at 80.)*
**The operator's lists now have exactly one name without a price and a pass/fail line: BN.**
