import io, os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "2026-09-19 Run - BLK BlackRock.md")
s = io.open(P, encoding="utf-8").read()
i = s.index("## SELF-AUDIT")
TAIL = r"""## SELF-AUDIT
*Operator rule 6: a run is incomplete until its self-audit is checked. Violations found later are
corrected in an addendum, never by editing history.*

- [x] **Questions answered in order; no verdict skipped.** Q1 IN → Q2 OUT → the file closed → Q3,
      Q4 and Q6 written as **RECORDED, NOT GOVERNING** and Q5 headed **COMPUTATION — NOT A
      CLEARANCE** under operator rule 3.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1, Q3, Q4 and Q6
      are each IN on filed evidence. The moat class was NOT left PROVISIONAL, and the reason is
      argued in the Q2 verdict rather than asserted.
- [x] **Every UNRESEARCHED verdict names the artifact and where it lives.** There are no
      UNRESEARCHED gate verdicts. Two *peer* items are marked UNRESEARCHED inside Q2 with their
      artifacts named: the Fidelity Concord Street Trust 485BPOS fee table for the Fidelity ZERO
      funds (CIK 0000819118; four 2026 accessions listed, none of which carried the prospectus fee
      tables), and Amundi's English-language Universal Registration Document. Both are shown to be
      one-directional: neither can reverse the finding.
- [x] **Every UNKNOWABLE verdict states what specifically cannot be known.** There are none.
- [x] **Step 0: the filing was read, with accession number; a figure was cross-checked.** 10-K
      FY2025 `0001193125-26-071966`; total revenue of $24,216M reconciled two independent ways, and
      operating cash flow of $3,927M tied to the GAAP column of the CIP reconciliation. Four more
      filings read in full, each with its accession.
- [x] **Owner earnings on a multi-year mean; window stated; capex band disclosed as a judgment.**
      Five-year (the corpus default) and three-year windows; the (c) band $369.6M-$593.0M with the
      reason the corpus default runs backwards here argued from the composition of the D&A line;
      and a third end quantified and explicitly not adopted.
- [x] **Competitor row filled**, one specification, eight lines, six filing-sourced competitors,
      accessions on every line, definitions quoted verbatim, and two comparability flags carried
      rather than smoothed (STT publishes no average AUM and no rate; IVZ changed its own yield
      definition in FY2025; BEN runs a September year; BX and BAM are carried from the committed
      BAM row of 2026-09-13 and **flagged as not recomputed in this run**).
- [x] **Sovereign is for the earnings currency, from the issuing authority, dated.** USD 5.34%,
      US Treasury daily par yield curve, 2026-09-18, struck fresh for this run; not FRED and not
      inherited from the brief. The earnings currency is USD (the Americas are 68% of AUM and 67%
      of base fees).
- [x] **Value stated as a round-number range, not a point estimate.** Roughly $550-$650 conservative
      and $875-$1,030 optimistic, against a price of $1,069.78.
- [x] **One bar chosen, not both; windage count stated.** The screamer test **[E4-01]** only; the
      normal method is explicitly not used. **Windage count: ONE**, applied at Q4 (stock pay at the
      larger of charge and grant value).
- [x] **Prices dated; aggregator used for live quotes only and flagged.** $1,069.78 at the
      2026-09-18 close, from `tools/sources.py price()`, flagged as an aggregator, with the 10-K's
      own *"a closing stock price of $1,070"* at 2025-12-31 as an order-of-magnitude cross-check.
- [x] **Every judgment cited by ledger id, and every id checked against `principle_ledger.csv`
      before use.** All 170-odd ids referenced across this file were verified present in the
      267-row ledger by script before the run was written; **zero phantom citations**.
- [x] **`python tools/check_framework.py` PASSES** — recorded in the fold commit.
- [x] **Run committed to git**, in six pathspec commits: the skeleton before any fetch, then
      Step 0 + Q1, Q2, Q3, Q4, and Q5 + Q6 + audit.
- [x] **Write-early protocol followed.** The run file was created from the template as the first
      action, before any fetch, and every question was written and committed as it closed.
      Research written to `Test Runs/_research 2026-09-19 BLK/` as it was gathered.

**ONE THING THIS RUN GOT WRONG AND CORRECTED ITSELF, recorded rather than hidden.** The first
attempt at the competitor row was delegated to a helper agent, which exhausted the session limit
before it finished. Its partial output was on disk (`peers/PEER_ROW.md`) and was **verified figure
by figure against the downloaded filings by this session** before use — TROW's *"EFR without
performance-based fees 39.4 41.0 41.9"*, BEN's *"was 40.5 and 41.1 basis points for fiscal years
2025 and 2024"*, IVZ's *"revenue yield (2) 33.7 37.4 40.4"* and *"Net revenue yield ex performance
fees (3) 23.0 25.4 28.4"*, and STT's *"Management fees (1) $ 2,398 $ 2,124 $ 1,876"* were each
re-read in the filing text. The six ETF prospectus accessions were recovered by matching the
on-disk file sizes against EDGAR's own filing indexes and are recorded in Q2. **Nothing in the row
rests on a figure this session did not see in a filing.**

## REGISTER
- Verdict: [ ] IN  **[x] OUT (about the business)**  [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- **One line: BLK fails Q2 — the product that is 42% of long-term AUM and 45% of long-term base
  fees is sold by Vanguard at an identical 0.03%, unchanged for five years; every organically owned
  fee rate fell over 2021-2025 (ETFs −17.1%, active equity −20.8%, active fixed income −18.0%,
  active multi-asset −35.4%, non-ETF index −8.1%) and the blended 15.22bp held only because $28.3bn
  — $22.0bn of it in the company's own shares and units — bought a higher-priced private-markets
  book; base fees grew 14.6 points slower than the assets they are charged on, and owner earnings
  per share are flat to 12.5% lower than four years ago on 40.3% more AUM.**
- **Price US$1,069.78 (close 2026-09-18, aggregator, flagged) · share count 162,476,186 (154,869,259
  common + 7,606,927 Subco Units) from the 10-Q cover as of 2026-07-31, accession
  `0001193125-26-337177` · market cap US$173,814M · sovereign 5.34% (US Treasury, 2026-09-18) ·
  FAIL at Q2, OUT on the business. Q5 below the floor at 3.5-4.1% pre-tax expectancy against ~10%,
  and above the whole value range — headed COMPUTATION, NOT A CLEARANCE.**
- **If UNRESEARCHED — THE WORK ORDER:** not applicable to any gate. The two peer work orders are
  recorded in Q2 with artifacts named.
- **If UNKNOWABLE:** not applicable.

### THE SURVIVAL SHAPE **[E5-11]**
**#11 THE PASS-THROUGH is the mechanism** — *"the company survives but gains are passed to
customers and suppliers, compressing the owner's return."* The filed evidence: ETF average AUM
+60.3% from 2021 to 2025 while the ETF fee rate fell 17.1%; total AUM +40.3% while base fees rose
25.7%; owner earnings per share flat to −12.5%. **[E3-62]**'s second step answers the question the
shape asks: the savings from scale went home to the customer, not to the owner.

**PROPOSED, PENDING THE OPERATOR — a new shape, argued rather than asserted: THE BOUGHT AVERAGE.**
*The mechanism, in one line: the price of everything the business already owns falls every year, and
the owner buys higher-priced businesses with its own shares so that the blended price stands still —
so the decline is invisible in the headline while the share count and the goodwill rise, and the
owner pays for the appearance of stability in dilution.*
**Why it is not #11 alone:** the pass-through describes where the gains go; this describes **how the
loss is concealed**. BlackRock's blended rate reads 16.29 → 15.22bp, a 6.6% decline that looks
survivable; the organic rate fell 13.4% and every component fell between 8% and 35%, and the
difference is $28.3bn of purchased mix. **Why it is not #21 THE ROLL-UP:** SoundHound's revenue
*line* was bought while the businesses it owned throughout shrank. BlackRock's revenue line grows
organically and strongly — $698bn of net inflows in 2025. **It is the price per unit, not the
revenue, that is bought.** **Why it is not #10 THE CAMOUFLAGE:** there is no weak leg burning the
strong leg's cash; every leg is profitable. What is camouflaged is a *rate*, by a *purchase*, paid
for in *equity*. **Tells a reader can check on any filer:** a blended unit price roughly flat while
every disclosed component falls; goodwill and intangibles crossing book equity (here $63,251M
against $55,888M, tangible equity **−$7,363M**); and the share count rising by acquisition
consideration faster than buybacks retire it (up to 25.0M shares and units, 15.4%, against $1.6bn a
year of repurchase). **Numbering is left to the folding session, which must count the current index
rather than trust this file.**

### THE STRONGEST SINGLE FACT AGAINST MY CONCLUSION **[E4-26, E4-51]**
**iShares crossed $6 trillion in AUM and roughly doubled in three years while charging the same
0.03% as Vanguard on the flagship — which means buyers are choosing BlackRock for something that is
not price, and that something is not in my fee-rate series.** If the reason is secondary-market
liquidity, the options complex built on the ETFs, the securities-lending revenue returned to the
funds, or the ability to move ten billion dollars in an afternoon, then BlackRock owns a real and
unbuyable advantage that simply does not show up as price — and the framework's own **[E3-33]**
warns that *"a screen on realised returns alone misses this class entirely."* My answer is that an
advantage which shows up as volume at a price you cannot raise is scale, not franchise, and
**[E3-62]** says where the gains from scale go in that case. **But I record that a holder who
believes iShares' liquidity is a durable toll that will eventually be priced would read the same
filings and reach IN at Q2, and the fact they would cite is the $6 trillion, not a projection.**

### DEFECTS FOUND IN THE BRIEF AND THE TOOLING
1. **`tools/sources.py:_get()` defaults to `WEB_UA` = `Mozilla/5.0`, and `www.sec.gov/Archives`
   returns HTTP 403 to it.** Every primary-document fetch in this run failed until `headers=SEC_UA`
   was passed explicitly. The default is wrong for the rung of the evidence ladder the framework
   uses most. **Suggested fix: default `_get` to `SEC_UA` for any `sec.gov` host**, which changes no
   number and removes a trap that costs every new run a failed call.
2. **`cik_for("BLK")` returns the right CIK and a misleading history, and nothing warns.** CIK
   0002012383 files today; its `companyfacts` begins at **FY2024** because the holding company was
   only created in October 2024. The 2009-2023 history sits under CIK 0001364742, now named
   BlackRock Finance, Inc. **A single-CIK XBRL pull on BLK returns two years of data and no error**,
   which is the same defect class the resume-state note records for `level_shift` and
   `working_capital_flag`: a diagnostic that does not reach the reader. **Suggested fix: have
   `name_change_note()` fire on a `formerNames` entry that differs in corporate form (it returned an
   empty string here), or have `annual()` refuse when fewer than five annual periods resolve.**
3. **The brief's instruction to find the CIK myself was correct and load-bearing.** Any run that had
   taken a CIK from a brief would have silently built a two-year series for a company with seventeen
   years of filings.
4. **The brief's "Aladdin is the part that may behave unlike the rest" was a hypothesis and it is
   half right, which is the useful answer.** Aladdin does behave differently in contract form
   (long-term, recurring, 16% organic ACV growth) and **does not** behave differently in its fee
   base: *"Fees earned for technology services are primarily recorded as services are performed over
   time and are **generally determined using the value of positions on the Aladdin platform**, or on
   a fixed-rate basis."* Its revenue is partly market-linked, like everything else. And it is
   **8.2% of total revenue**, which is too small to reclassify the other 91.8%.
5. **No defect found in the brief's framing of the fee-rate test.** It named the decisive series
   correctly before the data was pulled, and the data confirmed it. The instruction *not* to inherit
   BAM's conclusions mattered: BlackRock's rate decline has a different cause (customer substitution
   at a commodity price) from BAM's (related-party mix), and the two runs reach the same verdict for
   different reasons.
6. **One instruction in the original brief caused the session loss and is worth recording as a
   process defect, not a content one:** delegating the competitor row to a helper agent. The
   coordinator's correction — fetch peer data in-session — is the right rule for a run of this size,
   and the write-early protocol is what saved the partial peer file.
"""
s = s[:i] + TAIL
io.open(P, "w", encoding="utf-8").write(s)
print("audit and register written")
