# RESUME STATE 2026-09-12 - a note for Fable, from the Opus session

**Why you are reading this.** The Fable usage cap was reached on 2026-09-12 and the operator
switched the session to Opus 5 (1M context) mid-queue. This file records every change made while
you were away, with the reason and the run that forced it, so nothing has to be inferred from the
diff. The narrative ledger in `Screens/2026-08-31 PREPPED READING LIST (operator lists).md` carries
the same material at length; this is the index to it.

**Nothing about the framework changed.** No question was added, merged or deleted; no ledger row was
written; `principle_ledger.csv` stands at 267 rows. Every change below is either a tooling fix, a
correction to one of my own errors, or a fold.

---

## 1. THE STANDING COUNT, as at the end of this session

**73 runs** *(updated 18:45 local; this section first read 71 before BA and ROKU folded)*.
Gate-clearers 26 (all failed at Q5 on price) - Q2 OUT 44 - **Q4 OUT 2 (ORCL, ARM)** - Q1 UNKNOWABLE 1
(HHH). **Thirty-three businesses have cleared every gate across the whole project and all
thirty-three failed on price.**

**Twelve runs were folded in this session**: MRVL, SNPS, CORT, PAY, INOD, ELF, PLTR, ARM, CALX, BE,
BA, ROKU. Each did its own six-step fold; I verified all six steps on each.

**In flight when this was last updated: SWK and ACMR**, launched on Opus at 22:20 GMT, both read as
unlabelled (see item 4C). **Do not trust this line - read the register.** The overnight cycles
(section 8) decide what is done by reading `## COMPLETED FROM THE QUEUE`, never by this list.

**Still unrun:** ALKT, ACVA, FLNC, NEGG, plus CNR and RGTI with their perimeters named (CNR is the
CONSOL/Arch merger, RGTI is at-the-market dilution). **Note the queue is now 331 priced, not 361** -
see item 3F. **And 23 priced names carry a live deal form** (see the ROKU fold): ACLS is party to a
real merger so its band tracks deal terms, and AVGO was read and cleared as an exchange offer.

---

## 2. THE SOVEREIGN MOVED TWICE. Do not inherit it from any brief.
5.24% through 2026-09-07, **5.37% on 09-10**, **5.35% on 09-11**. Two runs (CALX, ARM) corrected a
stale rate I had given them. Operator rule 5 means each run strikes it from the Treasury curve
itself, and the briefs now say so explicitly.

---

## 3. TOOLING CHANGES, each with the run that found it

### A. `level_shift` now refuses when the RECENT half crosses zero
Arm's row printed **`level_shift_oe -0.79` with the confident string "STEP DOWN"**. A negative ratio
is not a ratio: Arm's early owner-earnings years are positive and its recent ones are not, and every
prior guard on this function tested only the EARLY half. Refused in words like its twin. **No
negative ratio remains anywhere in the queue.** This is the fourth iteration of this one function's
guard; the pattern each time has been that the test read one side of the series and the defect lived
on the other.

### B. `working_capital_flag()` added
Built for a shape found twice in five days: **DELL's accounts payable swung $21.2bn**, which was the
entire distance between its worst owner-earnings year and its best, and **INOD's H1 2026 operating
cash of $164.4M carried a ~$116M customer prepayment** visible only in the 10-Q liquidity note, so a
trailing-twelve-month figure would have reported three times what the company earned. It fires when
a single working-capital line moves by more than 30% of a year's operating cash, names the year and
the line, and stops. **Carried into the CSV as `wc_note`; fires on 158 of 361.**

**The threshold was measured, not chosen**: 30% gives 158, 50% gives 113, 100% gives 63, 200% gives
39. Kept at 30% because the names just under 50% include **ORLY at 38%** on vendor-financed negative
working capital, which is exactly the case a reader should be sent to. **Its limit is in its
docstring: it reads ANNUAL facts, so INOD's half-year prepayment is invisible to it until the FY2026
10-K.**

### C. `newest_periodic` column added, then fixed the same day
MRVL's row read `newest_filing 2026-01-31` while **a $3.5bn acquisition, a $2bn preferred and a
59M-share customer warrant sat in two later 10-Qs and an 8-K**. `newest_filing` is the newest ANNUAL
period end; the new column carries the newest periodic one. **A later periodic filing exists beyond
the annual date on 357 of 361 rows.**

**My first version was wrong and I caught it within the hour**: it took the maximum period end
across every tag and printed **2034-03-31** for Innodata, because filers tag forward-dated
commitments. Now restricted to the operating-cash tags and to dates that have happened.

### D. `growth_required` refused on a negative bottom
MRVL's row printed 10.20% from a bottom of minus $373M. The growth needed to reach the floor from a
base below zero is not a number. Now refused in words and sorted to the end; the tier summary was
made string-safe for it. **Refused on 120 rows.**

### E. `fts_count()` added to `tools/sources.py`, with a hard guard
The CALX run reported that the EDGAR full-text-search call *"returns a well-formed zero-hit response
for every CIK."* **I tested it before recording, and the endpoint is fine - the harness was
malformed**, which is a materially narrower claim. The `ciks` parameter accepts only the bare
zero-padded ten digits:

| value sent | result |
|---|---|
| `0000926282` | 200, **20 hits** - correct |
| `CIK0000926282` | 200, **0 hits** - what the harness sent |
| `926282` unpadded | 200, **0 hits** - equally silent |

**Both malformed forms return HTTP 200 with a well-formed empty body**, and *"no competitor names
this company"* is exactly the conclusion a run draws from a zero, on a question the framework treats
as evidence because a moat is a relative claim. Primary documents show **ADTRAN, Cambium and
Clearfield all name Calix.** The new helper **refuses** a malformed CIK rather than passing it
through, because a guard that returns a plausible number on bad input is worse than no guard.

**Scope was checked rather than assumed**: the shared PLPC harness passes the correct padded form
and was unaffected; the PLTR and CALX naming claims rest on greps of downloaded 10-Ks. **The one
prior naming error already stood corrected** - the KLAC research file's claim that Applied and Lam
name nobody, which the LRCX run refuted by finding seven named companies.

### F. THE MOST CONSEQUENTIAL FIX: SBC of zero is no longer substituted silently
**This one changes the queue, so read it before using any row.** The BE run found that both
published band ends reproduced to the dollar **and both were computed with SBC set to zero.** Bloom
tags stock compensation as `AllocatedShareBasedCompensationExpense` **dimensioned by expense line**,
so an undimensioned annual fetch returns nothing after 2018, and `sbc.get(e, 0.0)` quietly
substituted zero - omitting $70-200M a year. **[E5-06] says SBC is simply an expense. Dropping it is
not conservative; it overstates owner earnings, which is the one direction that matters when the
question is whether to buy.**

Measured across the 361 priced names over their last five operating-cash years: SBC resolves for
every year on **325**, for some years on **14**, and **for no year at all on 21** - MKL, MPLX, APLE,
CTS, CVX, NEU, PM, BRK-A, EME, TDY, GENC, BE, SEB, SO, UTL, NWN, TG, C and three MBIN preferreds.

`owner_earnings()` now returns `SBC_UNRESOLVED` or `SBC_PARTIAL` and the row goes **unpriced with
the ground stated**, exactly as `CAPEX_UNRESOLVED` already did. **The queue went from 361 priced to
331.**

**No completed verdict reverses, and the reason is the direction of the error.** Four affected names
had been run - MKL (Q2 OUT), BRK-B (Q5 FAIL), COKE (Q5 FAIL) and BE itself (Q2 OUT). Omitting SBC
overstates owner earnings, so each looked **cheaper** than it is, and a failure reached on an
overstated yield holds a fortiori. MKL and BRK are priced by the insurer sector method rather than
this construction at all. **The real damage was the READING ORDER: 27 of the 30 newly unpriced names
were never run and had been ranked on an overstated yield**, including CVX, PM, SO, C, MPLX, TDY and
EME. They await a hand read.

### G. `tools/run.py` routed through the newest vintage
The DELL fix of 2026-09-07 made `vintage` a parameter with the default left at `earliest`, so
nothing anchored in the past would change by my hand - **and `run.py`, a live tool, was never
switched.** The SNPS run found it reading Synopsys's original FY2024 capex of $123.2M rather than
the restated $139.5M. All ten `annual()` calls in that file now go through `newest`. **This was the
fourth two-paths split found in five days**, after capitalised software, the share-count denominator
and the restatement vintage itself.

### H. `.gitignore` made recursive
**My own error.** A preserve commit swept **28 MB of raw filings** from the SNPS run's `cache/`
subfolder into history, because every research ignore rule matched only the folder's top level.
Removed from the tree going forward, patterns made recursive, `cache/` folders ignored outright, and
the un-hyphenated `20F` variant added after an ARM dump slipped through the same way. **The 28 MB
stays in history, recorded rather than rebased.**

---

## 4. MY OWN ERRORS, corrected on the record

**A. I reported SNPS as "the first name to clear all four gates and return UNKNOWABLE at Q5." It did
not.** The run's verdict line copied KLA's form, *"[x] UNKNOWABLE is NOT used"*, and my grep read
the ticked box as the verdict. **SNPS is the twenty-fifth gate-clearer and failed at Q5 on price.**
The lesson is the one the runs keep teaching: a parser that reads a form is not a reader.

**B. I told the SNPS run the Ansys pro forma was on disk, on the strength of a filename.** The file
named `SNPS_8KA_ANSYS_PROFORMA` is a committee-appointment amendment. The real pro forma is in 10-K
Note 4 and gives no operating cash. **I trusted a name I had not opened, which is precisely what
operator rule 4 exists to prevent.**

**C. A triage label of mine had been telling five runs which gates to skim.** The tier-3 note said
of BE, NEGG and FLNC that *"these runs are the cheapest in the queue ... the file's work is Q1-Q2
plus the honest statement."* That is factually wrong for BE (rebuilt, its band **spans zero** at
minus $273.3M to plus $504.3M), it prejudges Q5 before Q1 opens, and **it is the CGNX error in a new
place** - the prohibition I wrote into that same file on 2026-09-07 says never tell a run which gate
will be boring, and I left this label standing four lines above the tier list. **A dated correction
is inserted beside the triage rather than editing it.** Still live under those labels: NEGG, FLNC,
ACMR, ALKT, ACVA and BA.

**D. I briefed a "$1 price increase" for ELF that appears in no filing.** The 10-K says *"raised
prices globally for all products sold"* with no amount. I briefed a number from memory.

**E. A commit landed under a stale message file** left at a reused scratchpad path by the ORLY run
of 2026-09-02, so `e9cc6a5` is titled *"ORLY: Q5 and Q6"* and contains the INOD fold, the
working-capital flag and the regenerated queue. Its four files are verified as exactly mine.
**History untouched; message files are now written fresh before every commit.**

**F. I checked ARM's roster strike in the wrong block** (tier 2, where every prior name had lived)
and briefly reported it missing. It was struck in tier 3. **Register checks now read the whole
file.**

---

## 5. WHAT I DID NOT FIX, and why - these are source limits, not bugs (nine)
Each was tested against the data before being recorded as a limit:

- **Stock consideration in an acquisition perimeter.** Tested `BusinessCombinationConsiderationTransferred1`
  and its equity sibling on CRM, CERT, MRVL and AVGO: **none resolves undimensioned in
  companyfacts.** Only the investing-cash line exists, which is what the flag already reads. **Six
  consecutive perimeter understatements are a limit of the source, not of the rule.**
- **Grant-date SBC.** CORT's `[E3-70]` measure puts its 2025 owner earnings at **minus $43.7M**
  against a charge-based plus $90M. No grant-date total resolves undimensioned for CORT, CRWD or
  PINS. A run on a name with SBC/OCF above 50% reads the grant table by hand.
- **`OtherDepreciationAndAmortization` as a (c) preference.** Tested on Marvell: it reads $265.9M
  against a filed $1,245.3M. **No tag rule recovers a number the filer did not tag.**
- **A renewal cost paid through financing.** Marvell pays $128-154M a year for capitalised IP
  licences under a company-extension tag no us-gaap element reaches. Every fabless designer with IP
  licence obligations will carry it.
- **Convertible preferred counted in basic EPS** is invisible to the cover element (8.2% at MRVL). A
  weighted-average-versus-cover test would over-fire on every buyback company.
- **`cover_shares.py` cannot see a foreign private issuer's post-annual count**, because 6-Ks carry
  no cover tag. For a 20-F filer the method is the 20-F Item 7.A count plus the 6-K balance sheet.
- **The SBC max-rule can double-count** SBC that was capitalised into software and already sits in
  (c) (PAY), and can pick the P&L charge where the cash-flow add-back differs (ARM FY2023, $247M
  apart). No undimensioned tag separates them.
- **The D&A end of (c) triple-counts** on filers that capitalise displays or cloud costs into other
  assets - $48M of ELF's $79M is cash already inside operating working capital - so `[E3-44]`'s
  default runs the wrong way on that class, and only a reader sees which class a filer is in.
- **8-K Item 2.01 as a closed-perimeter signal.** Tested on its own motivating case and it fails:
  **SWK announced its completed CAM sale under Item 7.01, not 2.01**, because 2.01 is required only for
  a significant disposition. It also false-positives on mistagging - **PAY's Q2 earnings release is
  tagged 2.01.** It did catch HHH's significant Vantage acquisition. **Incomplete and unclean, so not
  built.** A closed perimeter event is found by reading the 10-Q and press releases.

---

## 6. WHAT THE RUNS FOUND THAT CHANGES HOW THE REST SHOULD BE READ

- **PLTR is the dearest gate-clearer yet**: the buyer needs about **40% a year for ten years** from
  the best twelve months ever filed to reach the floor, and steady state needs $78-124bn of revenue
  against $8.15bn guided. Its Government segment looks **wider** than Commercial, which inverted my
  prior, but the 10-K says the customer negotiates *"based upon the customer's view of what our
  pricing should be"* - `[E2-59]`, the moat belongs partly to the regime.
- **ARM is the second Q4 OUT and a different shape from Oracle's.** Oracle had contracted not to
  stop; Arm carries no debt at the registrant and fails because **SBC alone consumed 96.6% of
  operating cash over its listed life**, with the leverage sitting at the parent as a pledge on 72%
  of the shares. **CALX then set a new high at 98.4% cumulative.**
- **BE named a third survival shape**: not Oracle's and not Arm's, but **the HHH shape** - too
  little filed history to judge, two quarters where HHH had twenty-six days.
- **ELF passed the tariff test on price and failed it on units**, the exact inverse of PLPC: gross
  margin recovered within three quarters while the filed volume line went negative for four.
- **My `[E2-49]` metric-withdrawal prior now stands at six fires and five failures** (fired at SHOP,
  MRVL, PAY, ARM, CALX, BE; failed at QLYS, CRM, CORT, PLTR, INOD). I retired it once as a default
  expectation and SHOP refuted the retirement the same week. **Check it; do not assume either way.**
- **The AMAT service-margin finding keeps landing.** It killed the annuity claim at AMAT (33.4%
  against 54.2%), ran by proxy at CERT, and at BE came in **worse than AMAT's own ratio** (0.51
  against 0.62) off Bloom's own slide.

---

## 7. ONE MEMORY FILE WAS UPDATED
`brk-run-agent-pattern.md` gained a third mechanism: **a model cap is not a session cap, and the
recovery differs.** A timed limit is survived by SendMessage-resume, which keeps the agent's full
context. A model usage cap is not, because the agent is pinned to that model and hits the same 429.
**The recovery is a fresh agent with an explicit model override, handed the disk state as an
inventory** - run file, byte count, what is already complete, and every research file, with an
instruction not to refetch. CALX and BE were recovered that way onto Opus; BE had every 10-K from
FY2018 to FY2025, five 10-Qs, fourteen 8-K exhibits and three proxies already on disk, so the
relaunch cost the writing rather than the fetching.

**The write-early protocol decides whether WORK survives. The kind of limit decides whether CONTEXT
survives.**

---

## 8. OVERNIGHT AUTOMATION - set up at the operator's request, and how to stop it

**The operator asked for the work to continue while they sleep, once the tokens reset.** A timer that
only pings a live session cannot do that, and nothing can re-invoke a session that is not running,
so this LAUNCHES one.

**Windows Scheduled Task `BRK-overnight`**: first run **22:35 local on 2026-09-12**, then **every hour
for twelve hours**. Each cycle runs `Screens/_daily/_overnight.ps1`, which launches a headless Claude
Code session on Opus with `Screens/_daily/_overnight_prompt.md`. **One bounded unit of work per
cycle**: resume a killed run or run the next undone name, verify the fold, run the acceptance test,
commit by file name, append a line to `Screens/_daily/OVERNIGHT LOG.md`, stop. When every name is
done it writes `Screens/_daily/QUEUE COMPLETE.md` and does nothing further.

**What was tested before it was trusted** - including the link most likely to fail at 3am:
- **Under Task Scheduler itself**, not just from a shell: a throwaway task launched the CLI as the
  operator's user, resolved the binary, AUTHENTICATED, and returned the expected reply with exit 0.
  Scheduler contexts often break auth and paths; this one did not. The test task was then removed.
- Headless print mode answered, and headless tool use under permission bypass read a repo file and
  ran git correctly.
- **The lock**: a lock holding a live PID made the cycle SKIP; a lock holding a dead PID was treated
  as stale and taken over. A single run has taken 25-40 minutes, and concurrent runs in this tree
  have crossed commits five times, so an hourly trigger must never start a second session.
- **The binary path is resolved every cycle**, because it embeds the VS Code extension version and
  an overnight auto-update would otherwise have made every cycle abort.
- **Subagents run in the foreground** (`run_in_background: false`), because a headless session ends
  when its main loop ends and would kill a background agent mid-run.
- **A run file modified in the last 45 minutes is left alone**, so an overnight cycle cannot grab a
  run another session is still writing.

**Conditions it depends on, checked rather than assumed:**
- **Stay LOGGED IN** - lock the screen, do not sign out. The task is interactive; running while
  logged off would require storing a password, which was not done.
- **Stay PLUGGED IN.** Wake timers are DISABLED in the active power plan, so the task cannot wake a
  sleeping machine. On mains the sleep and hibernate timeouts are both "never", so it will not sleep;
  **on battery it sleeps after 3 minutes and the overnight work stops.** Power settings were left
  untouched.

**Where to look in the morning:** `Screens/_daily/OVERNIGHT LOG.md` (one line per cycle), the git log,
and `Screens/_daily/_overnight_logs/_scheduler_trace.log` (START / SKIP / RATE LIMITED / END for
every trigger). Full per-cycle transcripts are in the same folder and are not committed.

**To stop it:** `Disable-ScheduledTask -TaskName BRK-overnight` in PowerShell, or delete it in Task
Scheduler. The superseded note-only task `BRK-wake` was disabled rather than deleted.

## 9. ADDED 2026-09-13 ~06:30 - THE REST OF THE NIGHT, AND WHY THE WATCHLIST IS NOT FINISHED

**What ran after section 8 was written:** CNR (Q2 OUT), RGTI (Q1 UNKNOWABLE, the second after HHH), BAM (Q2
OUT) and BN (Q2 OUT). **BAM and BN had been held as "BLOCKED and out of scope" since 2026-09-02.** I ran them
because "blocked" is not one of the four verdicts and the operator's instruction covers every business. Both
runs found the perimeter measurable from the filings.

**The overnight automation worked as designed, once.** Both Brookfield runs were killed at 01:44 by the
session limit (reset 03:20). The hourly task took over after the reset: the 04:35 cycle resumed BAM from its
committed Q1, and the 05:35 cycle resumed BN. Both did their own folds, verified. The lock and the 45-minute
rule prevented any double run.

**THE REGISTER AUDIT, and two errors in the count, one of them mine.**
- **Ten completed runs had no register entry**: GM, F, OXY, AEO, KR, NKE, PLAB, CVX, HHH, GHC. All ran on
  2026-09-01 or 2026-09-02, before the FOLD rule existed. **CVX was never even struck**, so the queue showed a
  finished run as waiting. The RGTI run noticed CVX; I checked every name against the run files and found the
  other nine. All ten are now entered from their committed run files (commit e730a1e).
- **My error inside the audit:** I first wrote that HHH and GHC were already registered, because my check
  matched their Stage 0(b) roster notes, which use the same bold-ticker form. Corrected in the same commit.
- **The incremental tally was one high** ("81 runs, Q2 OUT 51" after RGTI). Counted from the register, it was
  80. **Count from the register, never carry a tally forward**; the overnight prompt now says so.
- **A second trap for anyone counting:** the phrase `## COMPLETED FROM THE QUEUE` now also appears inside
  notes above the register, so slicing from its first occurrence picks up roster notes. Slice from the heading
  line itself.

**Standing count at 06:10, from the register: 82 runs** - 26 closed at Q5 on price with all four business
gates IN, 52 at Q2, 2 at Q4 (ORCL, ARM), 2 at Q1 UNKNOWABLE (HHH, RGTI). Nothing has cleared Q5.

**WHY THE WATCHLIST IS NOT FINISHED.** I was about to write a "queue complete" note and did not, because
reconciling the triage against the register showed the tiers were only the priced slice:
- The 2026-09-01 triage took **151 businesses** from the operator's fifteen screenshots and **priced 89**. The
  tiers came from those 89. **The unpriced ones were never queued**, although the queue's own
  "SKIPPED WITH A REASON, not forgotten" section named 34 of them.
- **Four more were dropped with no reason recorded**: HBB, LCID, SOUN, BIRD, whose caps the sanity guard
  rejected as broken inputs.
- **WAVE 5** (in the queue, commit 3a91f3a) queues **35** of them. The overnight prompt now works through
  wave 5 in order and stops there, writing `Screens/_daily/WATCHLIST COMPLETE.md` at the end.
- **Three banks are NOT run and are flagged for the operator: CCB, ACNB (priced, then left out of every
  roster with no ground recorded) and SOFI (a bank holding company).** The operator's directive of
  2026-08-30 excludes banks; the later "run everything" instruction may or may not override it. **That is
  the operator's call.**
- **About 17 unpriced watchlist names cannot be identified**, because the 151-name list was transcribed from
  screenshots and never saved to disk. Only the screenshots can close that.
- **Beyond the watchlist**: `Screens/queue.py` records that the operator asked for *"every business in every
  list"*, and the three CSV lists (`_input/list_{large,mid,small}cap.csv`) feed a master queue of 331 priced
  names, most never run. **I did not start those, and the overnight prompt forbids starting them unattended.**

**Wave 5 in flight at the time of writing:** TM and SONY, launched ~06:25. The JPY sovereign read 4.00%
(Japan MOF, 2026-09-10). The EUR sovereign fetch failed on an SSL certificate error and will matter for
STLA and possibly MBGL; it has not been investigated.

**Correction, same hour:** the EUR failure was transient. Python reached the ECB endpoint with both the default and the certifi trust stores on retry, and `tools/sources.py` read **EUR 3.83% (2026-09-10)**. Nothing was changed in the tooling.

**A seventh error of mine, found by the SONY run (2026-09-13 ~06:55):** every brief I wrote for this queue
cited **[E4-52] for "what pay vests on"**. [E4-52] is the **lollapalooza** row (converging tendencies); the
incentives row is **[E4-27]**. Runs that followed the brief literally may carry the wrong id at Q3; the
acceptance test cannot catch it because the id exists. The overnight prompt now tells a cycle to check every
ledger id before sending a brief. **SONY PASSED Q1 AND FAILED Q2** (music narrow and widening, PlayStation
narrow but re-won each generation, sensors a position not a franchise); register 83.

**Wave 5 progress at 07:45 on 2026-09-13: SONY, TM, HMC and TSM all closed at Q2; register 86.** Every one
of the four found the same real cause behind the "short XBRL history" skip reason: **companyfacts had not
ingested the newest 20-F.** Nothing in the filings was short.

**AN OPEN QUESTION FOR THE OPERATOR, raised by the TSM run and not resolved by it.** TSMC passed the three
[E3-03] franchise conditions at the leading edge and failed Q2 on **[E4-04]**, the "rapid and continuous
change" exclusion. The run found in the 2023 annual meeting transcript that Berkshire bought TSMC, that
Buffett called it one of the best-managed companies with nobody in the chip industry in its league, and that
it was sold within months **on location, not on the business.** If the corpus's own purchase contradicts how
[E4-04] is applied to a leading-edge foundry, **PRIME RULE 2 says the text wins** - but changing how a gate
reads is a structural question under PRIME RULE 5 and needs a written case and the operator's approval. The
run flagged it; nobody has acted on it. UMC and GFS in wave 5 will meet the same rule.


**Automation changes at 09:40 on 2026-09-13.** (1) The overnight lock now gives an interactive holder 75 minutes instead of 180: this session sat idle at the session limit from 07:46 with a live process, and the 08:35 and 09:35 cycles skipped after the 09:30 reset. (2) **The hourly trigger was extended: it now repeats every hour for 48 hours from 10:35 on 2026-09-13**, because the original 12-hour window ended at 10:35 with 31 wave 5 names left. The prompt still stops at the end of wave 5. To stop it: `Disable-ScheduledTask -TaskName BRK-overnight`.

**WHY THE 20-F FILERS NEVER PRICED - measured at 10:05 on 2026-09-13, after ERIC (Q2 OUT, register 87).**
The runs gave two different diagnoses (SONY/TM/HMC/TSM: companyfacts lags the newest 20-F; ERIC: `run.py`
carries only US-GAAP tag names). **Both are partly right, and there is a third cause that matters more.**
Read directly from companyfacts:

| filer | namespaces | IFRS operating-cash units | newest 20-F OCF period |
|---|---|---|---|
| ERIC | ifrs-full, us-gaap | SEK (27 facts) | 2025-12-31 - current |
| TM | dei, ifrs-full, us-gaap | JPY (16) | 2025-03-31 - one year behind |
| TSM | dei, ifrs-full, srt | TWD (26), USD (9) | 2024-12-31 - one year behind |

1. **`floor_screen.annual()` reads only the `USD` unit.** A filer reporting in SEK, JPY or TWD returns
   nothing at all, whatever its tags. This alone makes every non-USD IFRS filer unpriceable.
2. **The tag lists are US-GAAP names** (`NetCashProvidedByUsedInOperatingActivities`); the IFRS element is
   `CashFlowsFromUsedInOperatingActivities`, and capex and SBC differ likewise.
3. **companyfacts does lag** for some filers (TM, TSM), not all (ERIC).

**Not fixed, deliberately.** Reading non-USD units means pricing a home-currency cap against home-currency
earnings, which is exactly where the ATLKY currency defect lived; it needs the currency guard designed in,
not a unit filter loosened at 10am on a Sunday. The wave 5 runs read the 20-F by hand, which is correct under
operator rule 4 regardless. **It should be fixed before any backtest or screen touches foreign filers.**

**UMC closed at Q2 at 10:15 on 2026-09-13 (register 88), and raised a second question for the operator.**
Its Q3, recorded beneath the close, would be OUT on a **corporate** criminal record: UMC pleaded guilty in the
US in 2020 to possessing a stolen trade secret (US$60M fine), and a Taiwan court convicted the company in 2022
together with two of its then-current employees, with no filing found saying they were dismissed. **Every
earlier Q3 in this queue rested on named people's conduct; this is the first resting on the company's plea.**
Whether a corporate plea without identified individual accountability meets the honesty test is a reading of
the framework, and the run asked for a written ruling rather than setting the precedent itself. It did not
govern the verdict. **Also from UMC:** the Taipei Exchange endpoint the TSM run recorded returns 404; the
working path is `/www/en-us/bond/govDaily2`, now recorded in the UMC run file and fold.

**Open operator questions, collected:** (1) whether banks on the watchlist are run (CCB, ACNB, SOFI); (2) the
~17 unidentifiable unpriced watchlist names; (3) the TSMC corpus tension against [E4-04]; (4) the corporate-plea
reading of Q3 from UMC; (5) whether to start the three CSV lists after wave 5.

## 10. ADDED 2026-09-20 ~12:00 - THE WATCHLIST IS FINISHED, THE AUDIT IS FOLDED, TWO RULINGS WAIT ON THE OPERATOR

**The watchlist and Mini Berk closed at 20:37 on 2026-09-19: 132 businesses in the register**, every one
with a price and a pass/fail line - 33 cleared all four business gates and failed on price, 92 at Q2, 2 at Q4,
5 at Q1 UNKNOWABLE. Eleven names the triage had dropped were recovered from the operator's screenshots
(151 of 151 now reconciled), the five banks were run on the operator's ruling, and OTTR was run because
its "pre-run" exclusion had no file behind it.

**Then the unattended cycles audited the project itself for nine hours** (branch C of the prompt, with no
name to run) and the operator said "Fix". The disposition of all 26 decisions is the CLOSURE block at the
end of `Screens/_daily/WATCHLIST COMPLETE.md`. What matters most for the next session:
- **The ledger is 286 rows and every row is now checked against its source on every run** (check 4).
  Six rows were re-cut; E4-19's `(Laughter)` is back, including in the v4 epigraph. Two shelf files have
  holes (Talk 02, Talk 09) that need the operator's own Almanack.
- **Check 5 sweeps every run file for phantom ids.** Zero today.
- **PRIME RULE 3 has a clause: a CONVENTION label may confess an invention, never license what a rule
  forbids.** Seven July runs did exactly that; addendum on file; six of them sit in no current list.
- **`Test Runs/README - which run files are in force.md`** says which 141 files bind and which 158 do not.
- **The corpus was asked two Q2 questions and answered both** (nineteen new rows, E2-75..E5-56):
  [E4-04] is a perimeter limit, not a franchise finding, and a bank passes Q2 only through [E2-58]'s
  low-cost door in its two filed forms. **Both are written as a PRIME RULE 5 case for the operator**
  (`Framework/v4/RULING CASE 2026-09-20 ...`). Under Case 1 only TSM's verdict of record would move.
- **The overnight lock now honours an interactive holder by freshness**, because the PID it wrote was
  never alive and three cycles walked through it; two agents ran AIG as a result, the second refusing to
  overwrite and leaving a replication in the research folder.

**Still open, in order:** the operator's two rulings; the tooling fixes the operator queued on 2026-09-18
(foreign-currency screen, non-SEC path, the three older rulings); TJX re-run; the first holding reviews
(NCLTY, HRB, MITSY, V, TBTC); ten proposed survival shapes; and the three CSV lists, about 265 businesses,
which the operator said to run at one an hour once the watchlist was done - **not started, on the standing
instruction not to start them unattended.**

**Update 2026-09-20 ~14:00 - the operator ruled that the corpus answers all five open items, and it did.** Case 1 and Case 2 are APPLIED in Q2 (commit 2931a61), TSM re-read to Q2 UNKNOWABLE by addendum; Talk 02 restored from two July captures, Talk 09 left as found; the eighteen proposed survival shapes are RULED from the corpus (13 kept, 3 merged, 2 dropped to features; 25 distinct shapes; `Screens/SURVIVAL SHAPES - index.md`, every ruled line naming its rows); the ledger is **311 rows, 310 verified verbatim** (25 rows added for the shapes on top of the 19 for the two Q2 rulings); and **WAVE 7 is running** - 218 names from the three CSV lists at one an hour, 45 financials held out under the 2026-08-30 directive, first cycle 13:46. Nothing in section 10 above is still owed to the operator except the Almanack copy for Talk 09.

## 11. ADDED 2026-09-25 ~19:10 - THE SESSION CLOSES. READ THIS SECTION FIRST IN A NEW CHAT.

The operator is opening a new chat and asked that everything learned be kept. This section is the state of
the project at the moment the old chat ended, written so a session with no memory of it can continue
without asking. Sections 1 to 10 above are history and still true where they are not corrected here.

### 11.1 What the operator has standing instructions on (their words, in order given)
- 2026-09-01: *"We need to use the lists I provided. Check for pre run buisnesses. Exclude ETFs. And run
  everything through the frame work. Each should end with a price and whether it did or did not pass the
  framework."* Token cost is not a concern to the operator.
- *"Finish the mini berk and watch list in the next 24hrs or sooner. Then we can run one company an hour
  from the much larger lists"* - done for the first half (section 10); the second half is WAVE 7, running.
- *"Change to doing one an hour instead of one of 30mins"* - the cadence is one name an hour.
- *"the current framework is for new purchases. we also need a holdings framework and this will be it
  once its built"* - built: `Framework/ARCHIVE - v4.x (superseded 2026-10-05)/THE HOLDINGS FRAMEWORK.md`, governing since 2026-09-13.
- *"The corpus is the law. All answers are in the corpus"* and *"Your job is to audit and fix"* - every
  judgment cites a ledger id or it is an opinion (operator rule 8); when a question is open, search the
  shelf before asking the operator.
- Run locally, never in cloud agents. Never store the operator's Windows password in a scheduled task.
- No em dashes in prose written to the operator; restructure the sentence. Run files keep what they
  quote (PRIME RULE 1).
- The five watchlist banks were run on the operator's ruling; the 2026-08-30 directive still keeps
  financials out of the unattended CSV queue (45 names held out of WAVE 7). Only the operator lifts it.

### 11.2 Where every queue stands
| | |
|---|---|
| Register (`Screens/WATCHLIST RUN QUEUE.md`, count it from the file) | **172 entries** |
| Watchlist + Mini Berk | complete, 132 entries (section 10) |
| WAVE 7 (three CSV lists, `Screens/_daily/_wave7_order.txt`) | **40 of 218 done**; done file `_wave7_done.txt`; 45 financials held out; next HUBG, whose partial run (Q1 IN, committed dd28674) resumes from its own file |
| Gate-clearers (Q1-Q4 IN, failed on price) | **34**, PG the thirty-fourth (2026-09-25); **none passes Q5** |
| Names passing the whole framework at their price | **zero**, as at 2026-09-25 |
| Ledger | 311 rows, 310 verbatim, checks 1-5 PASS |
| Overnight task `BRK-overnight` | Ready, running hourly (a cycle starts at :46 or :55 and takes 30-300 minutes); trigger was set on 2026-09-20 to repeat for 14 days - **check it has not lapsed after 2026-10-04** |

The operator's last question was *"is there anything worth buying?"* The answer given, and still true:
nothing. Thirty-four businesses passed every business question and the framework passed on all
thirty-four at their prices. CRM fired its first level on 2026-09-21 and the pre-committed re-look quit at
the floor a second time (5.5-9.3% against ~10%); its levels are now $210 (full re-run) and $150 (ranks).
PG's bands are $107.25 (re-run) and $84.16 (floor). Alerts live in `tools/alerts.json`; a first level is
the top of the value range and means re-look, a second level is the ~10% floor price and means it ranks.
Neither is a buy.

### 11.3 What changed in the framework since section 10, all committed
- Q2 carries the two rulings of 2026-09-20 as text: [E4-04] is a competence limit (UNKNOWABLE at Q2
  when durability cannot be judged; rebuilt-from-zero fails, a maintained lead does not); a bank passes
  only through [E2-58]'s low-cost door, in the funding form [E4-60] or the operating form [E3-76], and
  its Q2 IN is NARROW so Q3 decides. `Framework/v4/RULING CASE 2026-09-20 ...` is the written case.
- Survival shapes: 30 numbered, 25 distinct after the rulings, every ruled line naming its ledger rows
  (`Screens/SURVIVAL SHAPES - index.md`). Runs name the shape.
- PRIME RULE 3 clause (a CONVENTION may not license what a rule forbids); PRIME RULE 4 eighth class
  (`Special Letters`).
- `tools/check_framework.py` has five checks; check 4 reads every ledger row against its source and
  check 5 sweeps every run file for phantom ids. It must PASS before any commit that touches a
  framework document, the ledger or a run file.
- `Test Runs/README - which run files are in force.md` says which files bind.

### 11.4 How to run the queue without losing work (learned the hard way, 2026-09-02 to 2026-09-25)
1. **Write early.** Run file from the template before any fetch; each question written as it closes;
   commit after each question; research to `Test Runs\_research <date> <TICKER>\`.
2. **Claim the name at dispatch.** The run file exists within minutes of the agent starting; a cycle that
   finds a fresh file for the next name skips it. Two agents ran AIG before this rule.
3. **Resume, do not respawn**, after a timed session limit (SendMessage to the same agent keeps its
   context). After a MODEL cap, spawn fresh on another model with a disk inventory (section 4 of the
   memory file `brk-run-agent-pattern`).
4. **No helper agents.** Four parallel runs each spawning helpers exhausted the limit at 10:45 on
   2026-09-19 and the weekly cap from 2026-09-21 to 2026-09-24 stopped everything. One name an hour, one
   agent, no helpers.
5. **Count from the file, never from a brief.** The register heading text appears inside notes; anchor
   the regex at line start and slice to the write-early heading. Briefs say "count it".
6. **Commit with a pathspec**: `git commit -F <msgfile> -- <paths>`. Trailer
   `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
7. **Bash heredocs that carry apostrophes in PowerShell-hosted shells fail**; write the script to the
   scratchpad or the research folder and run it.
8. **The lock**: an interactive session's lock is honoured by freshness (under 75 minutes); a headless
   lock needs a live PID under 180 minutes; a cycle releases only the lock it wrote.
9. **Six-step FOLD** after every run: register entry, roster strike, narrative fold, alerts and
   PORTFOLIO only for gate-clearers, check_framework PASS, pathspec commit. The OVERNIGHT LOG line
   carries the price and the pass/fail, which is the operator's required output.
10. **Every brief has contained an error.** Briefs end with "assume this one does too". Errors of record:
    [E4-52] cited for pay (it is lollapalooza; incentives is [E4-27]); Sekisui House category;
    PARA resolves to Banzai; stale counts in briefs; [E3-43] said of media, cited as if of banks.

### 11.5 Open, in the order the operator gave them
1. **WAVE 7 to completion** (178 remain at one an hour; branch C of the prompt writes
   `Screens/_daily/LISTS COMPLETE.md` when the order file is exhausted).
2. **The 2026-09-18 tooling fixes, items 11-13, not started**: `floor_screen.annual()` reads only USD
   units and US-GAAP tag names, so foreign filers cannot be priced by the screen (currency guard,
   unit filter); no automated path for documents outside SEC EDGAR; three older rulings (acquired-intangible
   amortisation inside (c), EX-5.1, Item 2.01). Deferred behind the queue by the operator's ordering.
3. **First holding reviews owed** under the holdings framework: NCLTY (its Q2 franchise test of
   2026-09-18 is OUT, footfall down and price per customer up, so H1 is already answered against it),
   HRB (bought under v3.1; H1 is the sharp question), MITSY (bought on the net-income proxy), V, TBTC.
   TJX needs a fresh purchase run; its in-force run is pre-v4.1.
4. Six void July names in no list: MTSUY, ITOCY, MARUY, SSUMY, NPNYY, FUJIY.
5. Talk 09 of the Almanack has a hole that needs the operator's own copy.
6. A pre-registered forward test of the gate-clearers against the index from 2026-09-11 was offered and
   not written. If written, it must be pre-registered before any return is looked at (operator rule 9).
7. The Gmail, Calendar and Drive connectors are unauthorised in this environment.

### 11.6 The honest record, restated for the new session
The market-beating claim is UNPROVEN (operator rule 7). The Roth's three framework-era buys were up 19.4%
in two months against the index's 1.6% when the operator asked why; the answer given was that two months
of three names is noise, that Nitori rose 34% while its franchise test failed, and that the corpus
attributes the record to the man, the system, luck and devotion [E5-19]. Do not let the run of good
prices become an argument for the method.

**Update 2026-09-26 ~07:00 - CLAUDE.md is now the map of the repository, and the rules moved.** At the
operator's request on 2026-09-25 ("structure CLAUDE.md as a guide to all other files in this project"),
`CLAUDE.md` was rewritten as a pointer map: a read-first order, one status word per file (GOVERNING means
in the acceptance test's DOCS list and nothing else), one table per area, five recipes for how work moves,
and its own rules (no counts in it, full paths, every path must exist). The operator protocol, the prime
rules, the tooling test, the sovereign sources and the standard moved verbatim, rule numbers unchanged, to
`Framework/OPERATOR-PROTOCOL.md`, which `CLAUDE.md` imports on every session (verified in a fresh headless
session: the file loads, nine rules) and which the acceptance test now reads; the "ONE SCREEN" summary was
deleted because it had drifted from v4 twice. `tools/check_framework.py` has a sixth check: every backticked
path in `CLAUDE.md`, the protocol, `Framework/README.md` and `README.md` must exist on disk. The sweep the
mapping found: root `README.md` had described the v3.0 eight gates since July and is rewritten for v4.1 with
its honest-record section kept word for word plus a dated addendum; dated notes on `PORTFOLIO.md` (pre-Test-D
header wording), `corpus_map.md`, `owners_manual_map.md` and the Test Runs in-force README (its lists stop at
2026-09-20; the register decides); the E5-08 ledger note's coursework path; three tool docstrings. Commits
043dae43, bcad0533. The overnight prompt's reading order names the protocol; the cycles that ran after the
change (LNN, SYY and on) folded normally. Still open from the mapping, not done: adding
`Framework/v4/THE MANAGER STANDARD - Q3.md` to DOCS (a governance change); a "no net-income proxy" line in the
company template's self-audit; `Backtests/gate_timelines/` was never written up.

**Update 2026-09-26 ~09:30 - the seven root files audited and organized; ten gate-clearers found unentered.** At
the operator's "organize and audit all of these" (the seven files then at the root), each was checked against the
files it describes; the record is `Framework/2026-09-26 AUDIT - the seven root files.md`. The finding that matters:
**ten v4.1 runs of 2026-08-31 and 2026-09-01 (CSL, HD, ITW, LOPE, LOW, LSTR, OTIS, PNR, RPM, SHW) cleared all four
business gates, quit on at the floor and armed alerts, and were never entered in the register or in PORTFOLIO's
opportunity table**; the 2026-09-13 backfill caught the failed runs of those days, not these. Both are backfilled
now (register section dated 2026-09-26, PORTFOLIO rows marked), so **the gate-clearer count in section 11.2 above
("34") was understated by at least these ten; count from the register, never from this note.** Organized: the
three history files left the root for the archives they describe (`claims_audit.csv` to the May 2026 archive,
`corpus_map.md` and `owners_manual_map.md` to the v3.x archive), every pointer repointed, `PORTFOLIO.md` joined the
pointer check. Audit results in one line each: every VERIFIED row of the claims audit re-verifies against the shelf;
the corpus map's file rows match the disk exactly and only its v3 framework rows are gone; all 33 Owner's Manual
quotes verify by segment; PORTFOLIO cites no phantom id and one shorthand path was written in full; the ledger's
era column matches every id, its five duplicate openings are the five declared alias pairs, ids E2-34 and E3-36
were never used, and 50 rows are cited by no document and no run (listed in the audit file, left as evidence).

**Update 2026-09-26 ~10:00 - the Talk 09 hole is identified, not yet repaired.** Two independent transcripts of the 2003 UC Santa Barbara lecture (Whitney Tilson's transcript, tilsonfunds.com/MungerUCSBspeech.pdf, 25 pages; and Farnam Street's reproduction, fs.blog/great-talks/academic-economics-charlie-munger/) both read *"as a teenager, I'd been to the racetrack in Omaha where they had the parimutuel system."* So the two words missing after "where they had the" in `Munger Talks (PCA)/Talk 09 - Academic Economics - Strengths and Faults (UC Santa Barbara, 2003-10-03).txt` are "pari-mutuel system" (the Almanack's hyphenated spelling, used in its own next sentence; the transcripts write "parimutuel"). **Not written into the file**: both sources are transcripts of the speech, not captures of the Almanack edition, a step below the bar the Talk 02 repair met on 2026-09-20 (two captures of the same Almanack passage). The operator was told and asked whether to restore the words with a dated shelf note naming both sources and the spelling choice; no answer yet. No ledger row cites the sentence; `tools/shelf_damage.csv` stays empty; nothing in the framework waits on it.

## 12. ADDED 2026-10-02 - THE QUEUE IS PAUSED. READ THIS SECTION FIRST IN A NEW CHAT.

**The operator paused the queue on 2026-10-02.** The Windows task `BRK-overnight` is **disabled**, not deleted. Nothing runs until it is re-enabled.

**Where it stopped.** Wave 7 is done through name 111 of 218, PAYO (Payoneer Global, FAIL at Q2). **The next name is BWXT**, line 112 of `Screens/_daily/_wave7_order.txt`. The done file ends at PAYO and matches the first 111 lines of the order file. The register in `Screens/WATCHLIST RUN QUEUE.md` holds 253 entries, counted from the file on 2026-10-02. No run is half-done: PAYO's cycle of 2026-09-29 stopped after the register entry and before the reading-list fold, the survival-shapes note and the log line, and those were finished from the committed run file on 2026-10-02 (commit b0a8a722).

**Why the cycles had already stopped.** Every cycle on 2026-10-01 failed on the weekly usage limit; the two after it failed with "Can't reach the API server" (ENOTFOUND). Both are in `Screens/_daily/_overnight_logs/_scheduler_trace.log`.

**Results so far, from the register on 2026-10-02.**

| Where the run closed | Names |
|---|---|
| Q1 (could not understand the business) | 5 |
| Step 0 (no gate run) | 1 |
| Q2 (not a franchise) | 188 |
| Q4 (would not survive) | 2 |
| Q5 (cleared Q1-Q4, failed on price) | 57 |
| Passed Q5 | 0 |

Wave 7 alone produced 14 of the 57 gate-clearers (PG, CHD, UNP, JKHY, NDSN, EPAC, ATR, CAT, MSA, ECL, KEYS, ESI, MA, TECH).

**To resume.** Re-enable the task (`Enable-ScheduledTask -TaskName 'BRK-overnight'`). Its trigger was set on 2026-09-20 to repeat for 14 days, so renew the trigger as well after 2026-10-04. The next cycle reads the order and done files and starts at BWXT. Open items from section 11 are unchanged.

**Open item added 2026-10-02 at the operator's instruction: "check a framework only using annual meetings."**
8. **Check the framework against the annual-meeting transcripts alone** (`Annual Meetings/`, 1994 to 2025).
   Recorded in the operator's words; the scope and method are to be settled with the operator before any work
   starts. If it becomes a test of v4.1 (does a framework built only from the meetings agree with it, and where
   does it not), it is pre-registered before any reading or computing, as Test D and Test E were (operator rule 9),
   and any change it proposes to the framework goes through a written case first (PRIME RULE 5). Not started.

**Open item added 2026-10-02 at the operator's instruction: "run japanese businesses through v4.1."** The operator
also confirmed the same day that v4.1 is the default for everything.
9. **Run the Japanese businesses through v4.1.** Counted from `Test Runs/` on 2026-10-02:
   - **Already under v4.1, not to be re-run:** SONY and TM (2026-09-13, both Q2 OUT, in the register); MITSY
     (`Test Runs/2026-08-28 Run - MITSY (Mitsui) v4.1.md`); NCLTY (`Test Runs/2026-08-28 RERUN - NCLTY (Nitori) under v4.1.md`
     and the Q2 OUT of 2026-09-18). MITSY and NCLTY are held, so what they owe is the first holding review
     (item 3), not a purchase run.
   - **NHNKY (Nihon Kohden) first.** A Roth GTC buy at $9.10 x 165 stands on a price derived from deleted v3 rules;
     the v4.1 run should come before it can fill, or the operator cancels the order.
   - **Then the names that have only a v3.0 run of 2026-07-14/15:** MTSUY, ITOCY, MARUY, SSUMY, NPNYY, FUJIY (the
     six void names of item 4, folded in here), FJTSY, JAPAY, and NTDOY (a condensed test pass only).
   - **Not included unless the operator says so:** the rest of the 295-row
     `Screens/2026-07-15 JPN ADR Mechanical Screen - full results.csv`.
   - **What these runs need:** the documents are not on SEC EDGAR, so the route is the company's own securities
     report (有価証券報告書) from its IR site, as the NCLTY Q2 test did; the JPY sovereign from the Ministry of Finance
     (*jgbcme.csv*); the ADR ratio from the depositary; and item 2's tooling fix (the screen reads only USD and
     US-GAAP tags) if the arithmetic is to be pre-filled. Not started.

## 13. ADDED 2026-10-03 - THE v5 BLIND READ IS RUNNING. WAVE 7 STAYS PAUSED.

**What was decided.** The operator's theory, 2026-10-03: the annual meetings are the conglomeration of every
lesson learned. The operator chose, in answer to seven questions put that day: sources are the 32 transcripts
plus the signed sections of the report each meeting answers (Buffett's and Munger's own text only; the rest of
the report stays OFF-SHELF); v5 is an intended replacement for v4.1; a blind fresh read; a headless hourly
cycle; both the purchase and the holdings framework in scope; wave 7 paused while it reads; adoption decided by
the operator on a written comparison. The operator then approved the plan ("yes go and use auto mode"). Open
item 8 of section 12 is resolved into this.

**What governs it.** `Framework/v5/CASE 2026-10-03 - v5 from the meetings, for the operator's approval.md`
(PRIME RULE 5 and PRIME RULE 4) and `Framework/v5/PREREGISTRATION - v5 blind read and comparison.md` (the
design, the five kinds of lesson, the blind rule and its declared contamination, the calibration metric, the
reconciliation classes, the five tests before adoption). **v4.1 governs every run and review until a ruling
case the operator approves.** Nothing in `principle_ledger.csv` or any governing document changed.

**The machinery.** `principle_ledger_v5.csv` (twelve columns, ids M/L/R<year>-<nnn>, rows only through
`tools/v5_ledger.py`, which matches every quote against its source before appending and refuses a failing
batch); `tools/ledger_verbatim.py` gained `match_quote()` and a ledger-path parameter; `tools/check_framework.py`
knows the new id class, verifies the second ledger with checks 3 and 4, and takes `--also <path>` to check a
draft without making it governing; `Screens/_daily/_v5_read.ps1` and `_v5_read_prompt.md` (a copy of the
overnight cycle sharing `_overnight.lock`); `Screens/_daily/_v5_order.txt` (64 units: one meeting session each,
the AM unit carrying the FY(Y-1) letter and, for FY1995 to FY2017, the report with its signed sections);
`_v5_done.txt`; `Screens/_daily/V5 READ LOG.md`; `Framework/v5/READING REGISTER.md` and `Framework/v5/notes/`.
Windows task `BRK-v5-read`, hourly, indefinite trigger, no stored password.

**Owed as the read proceeds.**
- **PRIME RULE 4 and the `CLAUDE.md` row for `Annual Reports/` are amended when the first R-row exists**
  (PRIME RULE 6: the row before the rule). The first unit that can write one is 1996 AM.
- The operator reads the register and the log between cycles and re-queues any unit with zero rows whose note
  does not justify it.
- When `Screens/_daily/V5 READ COMPLETE.md` appears: synthesis (interactive), then the reconciliation and the
  five pre-registered tests, then the ruling case. The steps are in the pre-registration.
- Wave 7 resumes after the read: re-enable `BRK-overnight` and renew its trigger; stagger it from the v5
  task if both are ever to run.

**To stop the read:** `Disable-ScheduledTask -TaskName 'BRK-v5-read'`. A cycle in flight finishes its unit or
dies at the 3-hour task limit; the next cycle of either task takes over a dead-PID lock.

**Update 2026-10-03 19:55 - first unit closed by hand, one machinery defect found and fixed, task enabled.** The
hand-run cycle read 1994 AM in eight minutes: 91 rows (L 32, M 59), all 91 verbatim, four pathspec commits, note,
register entry, done and log lines, lock released, acceptance test PASS. Its own error report found that the
prompt had reached the session cut off at section 3: PowerShell 5.1 does not escape double quotes inside a native
argument, so the Windows command line ended the prompt at its first `"`. The session recovered by reading the
prompt file. `_v5_read.ps1` and `_overnight.ps1` now escape embedded quotes before the call; the overnight
cycles since the BAM/BN paragraph was written had been receiving sections 1 to 3 only and worked because those
sections send the session to the files. The prompt now names its own file on the whitelist and fixes the
letter-heading convention the unit set. `BRK-v5-read` enabled 2026-10-03 19:56, hourly at :15; next unit 1994 PM.

**Update 2026-10-04 08:07 - the headless v5 read is stopped.** The operator: "let's not do this headless."
`BRK-v5-read` disabled after 13 of 64 units (1994 AM through 2000 AM; next unit 2000 PM), 1,159 rows all
verifying, every cycle on the hour. This morning, before the stop: PRIME RULE 4 gained its ninth class (the
signed report sections, R-rows existing since 1996 AM) and the `CLAUDE.md` row for `Annual Reports/` was
corrected with a dated note; the brief and helper were amended from the units' own error reports (staging a new
note, an `erratum` command, locator form, `=====` section marks, reprint and damaged-span rules, speaker
conventions); three errata applied. All recorded in the pre-registration's INTERIM LOG 1. **How the read
continues is the operator's decision**: interactive sessions unit by unit under the same design (the prompt
file is the protocol an interactive session follows), or a stop. `BRK-v5-alert` still watches for the
completion file and is harmless; `BRK-overnight` stays disabled.


**Update 2026-10-04 16:57 - THE v5 READ IS COMPLETE.** 64 units, 4279 rows all verifying, both ledgers PASS. Units 14 to 64 ran
interactively after the operator's "let's do this normally instead of headless"; `BRK-v5-read` stays disabled and
`BRK-v5-alert` fires on `Screens/_daily/V5 READ COMPLETE.md`, written now. **Next step: synthesis with the operator
present**, from `principle_ledger_v5.csv` only, then the pre-registered comparison and tests, then the ruling case
(`Framework/v5/PREREGISTRATION - v5 blind read and comparison.md`, "The tests a candidate must pass"). v4.1 governs
until then. Open for the operator: the signed memos to the managers (FY2001, FY2010 files), read and not rowed.
Wave 7 stays paused until the operator says otherwise.

**Update 2026-10-04 night - v5 SYNTHESIS AND RECONCILIATION DONE; the public repository is live.**
- **Synthesis:** four theme maps, one merged map, the operator's structure decision (preamble, standing rule, Q1 to
  Q11, Q12 optional, closing note), thirteen section drafts, and two assembled drafts that pass the acceptance test
  with `--also`: `Framework/THE FRAMEWORK v5.md` (1,384 ids) and `Framework/v5/DRAFT - THE HOLDINGS
  FRAMEWORK v5.md` (183 ids, six hold questions). Calibration metric 72 of 78.
- **Reconciliation** (`Framework/v5/RECONCILIATION - v5 against v4.1.md` and three parts in `Framework/v5/synthesis/`):
  215 v4.1 rules, 130 reproduced, 52 partly, 28 absent, 5 contradicted; 87 new in v5. **Operator's rulings:** E4-13
  counts, so the hypothesis FAILS narrowly on one load-bearing rule (suspicion about accounting is a reason to stop in
  the meetings, only a prompt to read in v4.1); PARTLY recorded, not counted; three v4.1 defects corrected by
  `Framework/v4/ADDENDUM 2026-10-04 - three defects in v4.1 found by the v5 reconciliation.md` (ledger row E5-63
  added first; the ledger is 312 rows); the PERMANENT designation's 2016 withdrawal is owed a PRIME RULE 5 case.
- **Public repository:** https://github.com/chrehor36/long-term-business-analysis, an export by
  `tools/publish_public.py` into `C:\Users\chreh\BRK-public`; `NOTICE.md`, `HOW TO TRY IT.md`, `LICENSE`,
  `LICENSE-DOCS.md` are in both copies. Re-export and push after public-worthy commits; never push from this repo.
- **Owed, in order:** (1) Tests A' and B' and the regression under the v5 drafts (about fifteen runs; the operator
  said tomorrow); (2) the holdings draft's reconciliation against `THE HOLDINGS FRAMEWORK.md`; (3) the PRIME RULE 5
  case on PERMANENT; (4) the ruling case for v5's adoption, carrying the five test results and the six load-bearing
  PARTLY rules; (5) a seventh acceptance check (inline quotation against its row) is proposed in the addendum, not
  implemented. v4.1 governs until the ruling case. Wave 7 stays paused.

**Update 2026-10-05 early - THE FIVE TESTS ARE DONE; TWO CASES WAIT FOR THE OPERATOR.** Fifteen runs under the v5 drafts
(`Framework/v5/tests/`, protocol in the same folder; results in `Framework/v5/TESTS - A prime, B prime and the regression -
results.md`): acceptance PASS on both drafts; Test A' PASS on every STOP and both boxes (HRB Q2 TOO HARD, TJX Q7 OUT, both
analysts), two TJX weighings diverged; Test B' PASS, zero false passes on the five sealed cases; the regression on seven
names explained every difference (one real change, ASML: v4.1 understood and sold on price, v5 Q1 TOO HARD); calibration
72 of 78. The holdings reconciliation is part 4 (77 rules; PERMANENT contradicted; five findings against the holdings
framework). Ledger rows E5-64 (the 2016 withdrawal of the permanent class for marketable securities) and E5-65 (the 2009
correction of the retention test) were added, 314 rows. **Waiting on the operator:** `Framework/v5/RULING CASE 2026-10-05 -
adopt v5, for the operator's approval.md` (options A adopt now, B adopt after one correction pass [recommended], C keep
v4.1 and import, D refuse; and which absences to carry as CONVENTIONS) and `Framework/v5/CASE 2026-10-05 - the PERMANENT
designation and the retention test, for the operator's approval.md` (two rule changes to v4.1 and the holdings framework,
three addenda). v4.1 governs until the rulings. The public copy is current. Wave 7 still paused.

**Update 2026-10-05 - V5 ADOPTED.** The operator ruled on both cases: option B (adopt after one correction pass), both
largest absences kept as CONVENTIONS (the pre-committed falsifier; "about ten percent"), the PERMANENT withdrawal and the
retention-test correction approved with their three addenda (E5-66, E5-67 added; `principle_ledger.csv` is 316 rows). The
correction pass was made (section 5 of the ruling case, a to j), both drafts passed, and the PG reproducibility pair
agreed at every STOP and on the box. Section 8 then ran: `Framework/THE FRAMEWORK v5.md` and `Framework/THE HOLDINGS
FRAMEWORK v5.md` govern from 2026-10-05; v4.1 is in `Framework/ARCHIVE - v4.x (superseded 2026-10-05)/`; the v5 templates
carry the canonical template names and the v4.1 templates are archived beside the v3 ones; `DOCS` repointed; acceptance
PASS; `principle_ledger_v5.csv` (4,279 rows) published; `tools/run.py` defaults to v5. Every pointer file carries a dated
note. Runs dated 2026-08-28 to 2026-10-05 bind under the archived v4.1; later runs under v5.
- **Owed, in order:** (1) the first holding reviews under v5 for HRB, MITSY, NCLTY, V and TBTC (`Test Runs/_TEMPLATE -
  Holding Review.md`, six questions, four words); (2) the Japanese businesses through v5 (to-do item 9); (3) the
  wave 7 resumption decision, which is the operator's; the headless prompt `Screens/_daily/_overnight_prompt.md` still
  describes a v4.1 run and must be rewritten for the v5 template before `BRK-overnight` is re-enabled; (4) the seventh
  acceptance check (inline quotation against its row), proposed in the 2026-10-04 addendum, not implemented;
  (5) `tools/price_alerts.py` and `tools/alerts.json` still read first and second levels from v4.1 run files; under v5 the
  value question is Q7 and its range is a CONVENTION, so the alert bands of any v5 run need a reading rule before the
  first v5 run writes one. `BRK-v5-read` stays disabled; `BRK-overnight` stays disabled; wave 7 stays paused.
- *2026-10-05, after adoption:* the map's v5 automation rows now say the read is finished and both v5 tasks are
  disabled (`BRK-v5-alert` had fired on 2026-10-04 but never disabled itself; disabled by hand); the holding-review
  recipe in `CLAUDE.md` names the six questions and four words; `Screens/_daily/_overnight_prompt.md` carries a dated
  halt note (it still describes a v4.1 run and halts any cycle that reads it until rewritten for v5); the register's
  working rules carry a dated v5 note instead of an edit. Commits fb744da5, cb7ef9a0; public 20d3284 and the follow-up.
- *2026-10-05, owed item (1) begun:* **HRB reviewed under v5: WATCH, with NO ADD**
  (`Test Runs/2026-10-05 Holding Review - HRB H&R Block.md`; PORTFOLIO note the same day). Q2 graded MAJOR on the AI risk
  factor with assisted volume flat; purchase falsifier not tripped; new falsifier and a re-derived silly-price band
  (about $85.60 to $91.90 at 5.63%) written. Reviews still owed: MITSY, NCLTY, V, TBTC. The review's closing paragraph
  asks the operator one question: whether a held name may sit in WATCH indefinitely when a single unanswerable Q2 both
  holds it under watch and bars every add.
- *2026-10-05, the research-pass case approved and piloted:* the operator approved
  `Framework/v5/CASE 2026-10-05 - deeper research on the too-hard names, for the operator's approval.md` (A, B, C; HRB pilot;
  blind second analyst kept); v5 amended (section I, Q1, Part VII, VI; holdings II A; template box line). **HRB pilot: both
  analysts closed TOO HARD (NATURE) at Q2**, every K-finding agreeing (`Test Runs/2026-10-05 RESEARCH PASS - HRB H&R Block, the two
  closes compared.md`). Found: the paid category held about 52% of returns 2012 to 2025; HRB's share of it fell by a third or
  more; Direct File took about 0.1%; no AI effect yet; TurboTax Live growing fast, cause of HRB's loss not established. WATCH
  and NO ADD stand on a closed question. **Waiting on the operator:** four refinements to the research pass's form (single-fact
  OUT answers; spans fixed in advance; unknowable K-answers; blind copy without the position note). Next pass candidates per the
  case: TBTC, MITSY, then ASML. Holding reviews still owed: MITSY, NCLTY, V, TBTC.
- *2026-10-05, later:* **the v5 scope directive** ("any rules in v5 should come frome ONLY the v5 scope"): written into v5's
  standard; acceptance check 7 enforces it; the falsifier CONVENTION removed (its basis lay outside scope); the ten-year
  balance-sheet table added to `tools/run.py` and template Q4 [M2025-032]. **SECTOR METHOD v5 adopted** after a blind MKL test,
  an amendment (net of float by default; float net of ceded; accident-year development; after tax; the operating-income
  step) and a blind repeat that passed; the v4 method archived. Ten open items in the method's header. The public copy no
  longer carries any MBA path (placeholder removed, folder ignored). **Waiting on the operator:** the four research-pass
  refinements; whether to scrub the MBA placeholder from the public repo's history; the holding template's balance-sheet line.
- *2026-10-05:* the owner's screenshots add BN, BRK.B, CCB, SONY (one account) and NHNKY (filled) to the holdings; all are to be reviewed. PORTFOLIO note added; quantities and bases owed.
- *2026-10-05:* NCLTY sold (SELL review); NHNKY sold (v5 run OUT at Q2, blind analyst); V KEEP/NO ADD (owner may add); MITSY, TBTC, HRB WATCH/NO ADD. Reviews still owed: BN, BRK.B, CCB, SONY; QQQM a note.
- *2026-10-05:* BN v5 run TOO HARD (NATURE) at Q1 (the BWS insurer); the owner deferred a research pass (statutory statements, possible WORK) and BN's holding review until the list is finished. Order now: BRK.B, CCB, SONY, QQQM note, then BN research pass and review.
- *2026-10-05:* the owner added a TBTC research pass to the end-of-list queue (its v5 TOO HARD at Q2 called NATURE, with knowable parts: customer retention, wins and losses against named rivals, replacement pricing). End-of-list queue: BN research pass and review; TBTC research pass.
- *2026-10-05:* the owner added TSCO (Tractor Supply) to the reviews; whether it is held is to be confirmed. Prior runs: 2026-07-15 (v3) and 2026-09-04 (v4.1). Queue: BRK.B (running), CCB, SONY, TSCO, QQQM note; then BN and TBTC research passes.
- *2026-10-05:* TSCO confirmed not held; a v5 purchase run only (a possible buy). Blind run started.
- *2026-10-05:* SONY reviewed (WATCH, NO ADD); added to the deeper-analysis pool (research passes owed: BN, TBTC, SONY). CCB review: SELL recommended. Remaining: QQQM note; the three research passes; tools/run.py fixes for non-US filers (Sony: US rate, pre-split shares).
- *2026-10-05:* research passes done: BN (OUT, sold), TBTC (Q2 IN by ruling; Q5 integrity check running), SONY (OUT on a flawed K2; ruled corrected, stays WATCH). Lessons: name whose licence; never set after-depreciation income against gross capex; keep holding facts out of files the blind analysts are told to read.
- *2026-10-05:* the owner asked for v5 purchase runs (blind, not held) of the electrical-trades list, top down: LINC, UTI, PWR, EME, FIX, IESC, MYRG, PRIM, MTZ, DY, LMB, WCC, HUBB, NVT, ATKR, ETN. Run in batches of three; each a run of record in Test Runs/.
- *2026-10-05:* tools/run.py defects found by the runs: share count stale after a split (SONY, IESC: paired post-split price with pre-split shares); US rate for non-USD earners (SONY); OCF including securities purchases (IESC); stock pay printed as 0 (EME); equity tag missing (V). To fix.
- *2026-10-05:* small-cap screen (Screens/2026-10-05 smallcap screen (v5 triage).csv) and its top ten run blind under v5, all committed. OUT at Q7 on price only: MWA (alerts set at the range top, fair and cheap prices). OUT at Q2: RES, DBD, MOV, HNI. TOO HARD (WORK) at Q2, research-pass steps 1-2 written in each run and not run: CTS, MBUU (price below its cheap level), IOSP, SXI. TOO HARD (NATURE) at Q1: EXTR. Framework gaps the analysts logged repeatedly: Q2 has no by-parts rule; the Q7 range has no rule for negative shown growth, a boom year or acquisition-bought growth; no cheap-price convention; which tax rate turns the 10% pre-tax floor into after-tax. tools/run.py also leaves directors' stock pay out and shows only non-current debt.
- *2026-10-05:* small-cap screen ranks 11-16 run blind under v5, all committed: OUT at Q2 OSIS, AROC, GENC; OUT at Q4 ENSG (the two-tell convention, guidance beaten plus adjusted EPS featured; the operator may want a case on whether it should STOP or weigh); TOO HARD (WORK) at Q2 BOOT (above its cheap price, no pass run); TOO HARD (NATURE) at Q1 MTRN. MBUU research pass done (both analysts OUT at Q2 literally, TOO HARD (NATURE) on purpose; literal close stands by default, operator not yet ruled). tools/run.py: mine-development payments omitted (MTRN). Screen exhausted: of 16 ranked names only MWA passes the business questions (alerts set).
- *2026-10-05:* operator ruled MBUU keep OUT. The six unmapped small caps: the screen's SEC ticker cache was stale; CSGS was acquired and deregistered (May 2026); the rest run blind under v5 and committed: OUT at Q7 on price only CSW (alerts set at 145/85/45); OUT at Q2 SHOE (was SCVL), RYZ (was RYI), HOS (Helix merged into Hornbeck 2026-09-01), KLXE. tools/run.py fixed (nine defects plus finance leases and PIK interest; see tools/RUN_PY_FIXES 2026-10-05.md); tools/screen.py share count now split-aware. Still open in run.py: penny warrants and post-10-Q share issuance (8-K, S-3) are not read; SONY IFRS cash flows. Framework/v5/CASE 2026-10-05 - gaps found by the small-cap runs, for the operator's approval.md waits for the operator (sections A to G).
- *2026-10-05:* operator asked for more small caps. Screens/2026-10-05 SP600 smallcap screen (v5 triage).csv: 362 never-run S&P 600 names (financials, real estate, utilities left out), 233 ranked. Top ten run blind under v5, all committed: OUT at Q7 on price only ABG (cheap alert at 163; price below fair 216); TOO HARD (WORK) at Q2 WSC (research steps written; priced between cheap and fair, pass not run, operator asked); TOO HARD (NATURE) at Q1 EFOR (was ASGN); OUT at Q2 GIII, CAG, AHCO, WEN, ADNT, MBC, AMR. Lesson: the highest screen yields are mostly declining or cyclical businesses priced for it. run.py now also shows rental-fleet purchases and minority-partner dividends. Public export still held: holding reviews carry the operator's cost basis; operator to decide whether to withhold them.
- *2026-10-05:* S&P 600 screen ranks 11-20 run blind under v5, all committed: OUT at Q2 KSS, SCSC, LKQ, SLVM, ANDE, LCII (pending all-stock sale to Patrick), ENR, PENN; TOO HARD (WORK) at Q2 ROCK (research steps written, priced above fair, not run); TOO HARD (NATURE) at Q1 YELP. Of the screen's top twenty only ABG passed the business questions. Public export: holding reviews, notes, hold reads and research passes now withheld (operator said yes); re-exported and pushed (3dd726a in BRK-public). The HRB review with basis and share count remains in BRK-public history; operator asked whether to scrub. Gaps case scope-checked: 101 ids, all v5 scope; operator's decision on sections A-G still owed.
- *2026-10-05:* S&P 600 ranks 21-30 (nine companies; CENT and CENTA are one) run blind under v5, all committed: OUT at Q7 on price only PBH (cheap alert 16.86); OUT at Q2 CENT, PRKS, TDS, CALY, SKYW; OUT at Q1 OGN (pending $14 cash sale to Sun Pharma), INVA; TOO HARD (NATURE) at Q1 RHI. Of the screen's top thirty only ABG and PBH passed the business questions. run.py also shows aircraft purchases now. Public history scrubbed of the HRB holding files and force-pushed (be0a764). Operator made an 'experimental' branch on GitHub (unsourced rules from older versions) and asked for a 'ben graham' branch; a local timer fires 2026-10-06 01:11 EDT to set both up with their own working paths, rules kept off master (memory: brk-experimental-branch). Gaps case sections A-G explained; operator's decisions still owed.
- *2026-10-06:* S&P 600 ranks 31-40 run blind under v5, all committed: OUT at Q7 on price only POOL (alerts fair 130, cheap 91); OUT at Q2 AMN, SBH, GPOR, ADT, NSIT, PTEN, BTU; TOO HARD (NATURE) KTB (Q2), HRMY (Q1). Of the screen's top forty only ABG, PBH and POOL passed the business questions. Tools: run.py shows subscriber-account spending and flags amortization-only D&A; cover_shares.py no longer reads the CIK as a share count. Branches experimental and ben-graham set up in their own worktrees at the timer (memory: brk-experimental-branch). Another Claude session pushed claude/hopeful-ptolemy-5kwiln to GitHub with 2026-10-06 runs (GD, MO, XOM ...) and run.py/alerts.json edits, not in this repo; operator told. An EFX v4 alert fired (142.6 under 145): re-run prompt. Gaps case A-G still awaits the operator.
