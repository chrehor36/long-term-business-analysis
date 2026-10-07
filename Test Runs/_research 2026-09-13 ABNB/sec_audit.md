
---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN → **Q2 OUT, the file closed**; Q3-Q6 recorded beneath
  explicit RECORDED, NOT GOVERNING banners; Q5 headed COMPUTATION — NOT A CLEARANCE.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1's IN rests on named filings; the
  recorded Q3 and Q4 INs carry no such word. The one estimate in the file (column C's customer-funds interest) is
  labelled CONVENTION and does not sit under an IN it could promote.
- [x] Every UNRESEARCHED verdict names the artifact — none issued. The Q2 non-IN verdict was put to the separating test
  aloud (no filing measures host exclusivity; the filed record already answers criterion 2) → OUT, not UNRESEARCHED.
- [x] Every UNKNOWABLE verdict states what cannot be known — none issued.
- [x] Step 0: filing read with accession numbers (10-K `0001559720-26-000004`, 10-Q `0001559720-26-000027`, DEF 14A
  `0001193125-26-175062`, FY2020-FY2024 10-Ks, 424B4, 8-Ks); figures cross-checked (OCF FY2025 $4,646M filed =
  companyfacts; FY2020 OCF restatement found; SBC FY2025 $1,592M to the dollar across four places).
- [x] Owner earnings on multi-year means; six windows with and without 2020 and pre-IPO 2019; both (c) ends; the
  customer-funds separation done from the cash-flow statement before any figure; (c) disclosed as a judgment [E3-44].
- [x] Competitor row filled from filings (BKNG, EXPE, TCOM, MAR; IHG/HLT from the IHG run file, read only), limits
  stated [E3-61]; Vrbo unsegmented since 2019 stated.
- [x] Sovereign for the earnings currency, from the issuing authority, dated (USD 30-year 5.35%, US Treasury,
  09/11/2026, struck this session).
- [x] Value stated as a round-number range (~$35-60 conservative, ~$110-140 optimistic at 6% forever), under the
  COMPUTATION heading.
- [x] One bar (screamer), windage count one.
- [x] Prices dated; aggregator used for the quote only and flagged (US$170.19, 2026-09-11 close, Yahoo via
  `tools/sources.py:price()`).
- [x] Every ledger id cited was checked against `principle_ledger.csv` before citing (all present; the [E4-27]
  incentives row used for what pay vests on, [E4-52] only for the convergence).
- [x] Run committed to git with a pathspec at each stage (Step 0 `21f66bd`, Q1 `b782730`, Q2 `ab67084`, Q3-Q6 and
  audit in the next commit).

**Errors of mine in this run, recorded rather than smoothed:**
1. **A bash heredoc containing apostrophes killed the first Q1 append** (the brief warned of it); nothing was written
   and nothing was lost. All later sections were written to files and appended by `append.py`.
2. **I passed `fts_count()` a phrase wrapped in its own quote marks** (`'"Local Law 18"'`) and got **98** hits for
   Airbnb; the correct call returns **2**. The helper adds quotes itself and does not refuse embedded ones — recorded as
   a tooling defect below. No conclusion was drawn from the inflated count.
3. Draft figures corrected before they reached the run file: repurchase price range ($107-$134 → $107-$140), the
   revenue level at which owner earnings reach zero ($3.7bn → ~$3.5bn), the (c) band width (under 2% → under 5%, the
   incl.-2020 window being 5.2%), the 2019-25 revenue CAGR (19.5% → 16.9%), and the price multiples (33-40× → 32-33×
   TTM). A claim that repurchases were "below the bond at the time" was deleted: the historical sovereign was not struck.

**Tooling and brief defects found:**
- **`tools/sources.py:fts_count()` accepts a phrase that already contains quote marks and silently inflates the count**
  (98 against 2 for "Local Law 18", CIK 0001559720). It guards the CIK and not the phrase. Same defect class as the CALX
  harness: a malformed input returns a plausible number. Not fixed here (this run edits no tool).
- **`tools/run.py` priced ABNB on 2020-2022 only**, because `PaymentsToAcquirePropertyPlantAndEquipment` ends at FY2022:
  the filer moved capex into *"Other investing activities, net"* on the face of the statement and kept it only in the MD&A
  FCF reconciliation. **The triage's [E5-20] label ("the corpus calls [the D&A end] INVALID for this class") was wrong for
  this name** — D&A exceeds capex; the default case applies. The skip reason's generic wording attaches the railroad
  exception to every tag gap.
- **`run.py`'s share basis for ABNB was the diluted weighted average (623.0M)**, 5.7% above the economic cover count; the
  tool warned, correctly. `cover_shares.py`'s sum (598,785,682) includes **Class H, which the balance sheet shows as
  "issued and zero shares outstanding"** (held by a wholly-owned subsidiary) — a 1.6% overcount if summed. The cover calls
  those shares "outstanding"; only the balance sheet does not.
- **The brief's "possibly others" on share classes resolved to Class C (zero) and Class H (subsidiary-held, excluded).**
- **The brief's "funds payable and guest deposits are the owner-earnings trap" was true in kind and smaller in size
  than at PAY**: the host funds run through financing, not operating cash; the trap in OCF is the unearned-fee float and
  the interest on held funds.
- **The brief suggested stock compensation was "likely the centre of the file"**; measured, ABNB's SBC/OCF (49.6% since
  the IPO year, 31.7% ex-2020) sits below CRWD's 68.0% in the calibrated row. The file closed on the franchise question.
- Research dumps were renamed to the gitignored patterns (`10k_`, `10q_`, `8K_`); `s1_424b4.txt` (1.5MB) and the
  companyfacts/submissions JSON match no ignore pattern and were left uncommitted by pathspec.

---
## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line: FAIL at Q2 (OUT on [E3-03] criterion 2): close substitutes on both sides of the market — hosts and
  property managers list on Airbnb, Vrbo and Booking.com, Booking.com's homes listings nearly doubled to ~3.9 million —
  and the fee record is price defence (take rate 13.4-13.6% flat 2023-25 and below Booking's; a take-rate-neutral
  15.5% single host fee introduced so cross-listed prices compare). Q1 IN. Price US$170.19 × 589,585,682 = US$100.3bn;
  COMPUTATION — NOT A CLEARANCE: owner-earnings yield 1.1-3.1% against USD 5.35%, 6.7-8.8% perpetual growth needed for
  the 10% floor, value roughly $35-60 (conservative) to $110-140 (6% forever) a share; price above the whole range.**
- If UNRESEARCHED — not applicable. If UNKNOWABLE — not applicable.
