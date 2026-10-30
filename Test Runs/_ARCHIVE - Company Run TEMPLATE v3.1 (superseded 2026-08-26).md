# Company Run — [COMPANY] ([TICKER]) — [DATE]
**Framework v3.1.** Copy this file, fill it top to bottom. A section may be filled only
when every section above it carries a verdict.

---
## THE FOUR BOXES — read before filling anything
> "Charlie says, you know, **'We've got three boxes at the company: in, out, and too
> hard.'** And **a lot of things end up in the 'too hard' pile, and it doesn't bother
> us.**" — Buffett quoting Munger, 2006 annual meeting
> (`Annual Meetings/2006 Annual Meeting.txt:215`)

**Every gate returns one of FOUR verdicts (Ruling 12 as amended by Ruling 13):**

| Verdict | Meaning | Effect |
|---|---|---|
| **IN** | The evidence is here and it clears the bar. | Proceed to the next gate. |
| **OUT** | The evidence is here and the business fails. | **STOP.** Record in the Eliminated register. A permanent finding. |
| **UNRESEARCHED** | The evidence exists and I have not got it yet. | **A WORK ORDER, not a resting state.** Name the artifact and where it lives. Not reportable without one. |
| **UNKNOWABLE** | The evidence is in and the future is still indeterminate. | **CLOSE the file, without prejudice.** Buffett's actual too-hard pile. |

**THE SEPARATING TEST, asked out loud on every non-IN verdict (Ruling 13):**
### **"Can I name the document that would resolve this?"**
### **YES → UNRESEARCHED (go get it).   NO → UNKNOWABLE (close it).**

**OUT is a judgment about the BUSINESS. UNRESEARCHED is a judgment about MY DILIGENCE.
UNKNOWABLE is a judgment about MY EVIDENCE.** Never merge them.

**UNRESEARCHED IS NEVER AN ANSWER.** It is a queue entry, and it must carry the work
order. Escalation ladder: (1) SEC XBRL (screening only) → (2) SEC EDGAR primary documents
→ (3) **company IR site, English** → (4) exchange/regulator filings (TDnet, RNS, SEDAR+)
→ (5) EDINET *(blocked: needs a subscription key)* → (6) competitor filings for Gate 2.
Where a rung is blocked, name the rung and the obstacle.

**A THIN-EVIDENCE GATE IS NEVER "IN".** A gate marked IN with a caveat like "unverified,"
"general knowledge," "not independently confirmed," or "provisional" is a protocol
violation. It is **UNRESEARCHED** — and therefore it comes with a work order and someone
goes and gets the document. *(This rule exists because the July 2026 Japan runs did
exactly that and put unverified names into the portfolio. Nitori's English financial
statements were on its IR site the whole time.)*

**THE 7-FOOT BAR RULE.** > "there's **no degree of difficulty factor**... we get paid,
not for jumping over 7-foot bars, but for **stepping over 1-foot bars**... I'd rather
have the universe be a little smaller than it really is, than being interpreted as larger
than it is." — 2005 annual meeting (`Annual Meetings/2005 Annual Meeting.txt:977`)
**A conclusion that required fighting for it is worth less, not more. If a verdict only
holds after narrowing assumptions or adjudicating a sensitivity grid, the answer is
UNKNOWABLE.** (Gathering more evidence is legitimate; torturing the evidence you already
have is not. That is the line between UNRESEARCHED and UNKNOWABLE.)

---
## STEP 0 — RATE REFRESH (before anything)
- Sovereign 30-yr (earnings currency): ____ % (date: ____ , source: ____)
- Δ vs last valuation: ____ bp → >50bp? [ ] YES — revalue affected holdings [ ] NO
- FX (if non-USD): ____

## STEP 0-B — THE FILING WAS READ (Ruling 11)
> "**There are no answers in the financial statements.** There are guidelines to enable
> you to figure out the answer. And to figure out that answer, **you have to understand
> something about business.** You don't have to understand a lot about mathematics. I
> mean, **the math is not complicated.**" — 1994 meeting [E3-27]
> (`Annual Meetings/1994 Annual Meeting.txt:1233`)

- Filing read (not just tagged data): [ ] MD&A [ ] cash-flow statement incl. detail lines
  [ ] footnotes
- Document + date + accession no.: ____
- **No name may reach Gate 6 on XBRL/tagged data alone.** Tags are transcription and
  screening. Any figure that drives a verdict is checked against the filed statement, and
  the check is recorded here: ____
- If the filing could not be obtained → **UNRESEARCHED. Raise the work order, name the
  ladder rung that failed, and stop here until it is executed.**

---
## GATE 1 — CIRCLE OF COMPETENCE
- Unit economics in my own words (no management language): ____
- What is the scarce input this business controls? ____
- Will the fundamentals look broadly the same in ten years? ____
- **VERDICT: [ ] IN  [ ] OUT — STOP  [ ] UNRESEARCHED — work order: ____  [ ] UNKNOWABLE — CLOSE**

## GATE 2 — MOAT (per segment)
- Franchise test [E3-03]: needed/desired [ ] · no close substitute [ ] · unregulated [ ]
  · proven by pricing power + returns on capital [ ]
- Primary moat metric + trend (filing-sourced): ____

### THE COMPETITOR ROW (required — Ruling 11)
> "**I can't be an intelligent owner of a business unless I know what all the other
> businesses in that industry are doing.**" — 1996 meeting [E3-28]
> (`Annual Meetings/1996 Annual Meeting.txt:681`)

A moat is a claim about RELATIVE position and cannot be evidenced from one company's
numbers. Name **2-3 closest competitors**; same metric, same window, filing-sourced.

| Company | Primary moat metric | Window | Source |
|---|---|---|---|
| **[subject]** | | | |
| competitor 1 | | | |
| competitor 2 | | | |

- Competitor data unavailable (private / foreign / unsegmented)? [ ] N [ ] Y → **moat
  class is PROVISIONAL**, which carries the wider NARROW spread until resolved. A
  PROVISIONAL moat is **UNRESEARCHED** until the competitor filings are pulled (rung 6).
- Direction: [ ] WIDENING [ ] STABLE [ ] NARROWING
- Class: [ ] WIDE [ ] NARROW [ ] NONE [ ] PROVISIONAL
- **VERDICT: [ ] IN  [ ] OUT — STOP  [ ] UNRESEARCHED — work order: ____  [ ] UNKNOWABLE — CLOSE**

## GATE 3 — MANAGEMENT
### Integrity (binary, permanent, filings-based)
Litigation, regulatory actions, restatements, consent orders — **dated, and dated to when
each became PUBLIC**, so the test stays point-in-time honest: ____

### The half-owner test (the candor standard — replaces "integrity (binary)")
> "I would like to have a report that would be identical to what — **if I owned half of a
> company but was away for a year, and I had a partner who owned the other half** — when
> I came back, that he would tell me about what had taken place during the past year and
> what he foresaw coming up." — 1996 meeting [E3-28]

- Does this company's reporting tell me what a 50% partner would have told me? ____
  (a one-time item quantified separately at every line passes; the same item buried in an
  adjusted figure does not)

### Capital allocation — the two-condition buyback test [E5-08], Ruling 8
- (1) ample funds for operations and liquidity? [ ] PASS [ ] FAIL [ ] UNKNOWN
- (2) repurchases at a material discount to conservatively calculated IV? [ ] PASS
  [ ] FAIL [ ] UNKNOWN
- If (2) FAILS → **CAPITAL ALLOCATION FLAG**, stated with the mandatory humility clause
  [E4-13]: the judgment rests on our own IV range, and management knows the business
  better than we do. **Binds Gate 6 SIZING, never the discount rate.**
- **VERDICT: [ ] IN  [ ] OUT — STOP (integrity failure is permanent)
  [ ] UNRESEARCHED — work order: ____  [ ] UNKNOWABLE — CLOSE**

## GATE 4 — FINANCIAL QUALITY
> "(c) **the average annual amount** of capitalized expenditures... that the business
> **requires to fully maintain** its long-term competitive position and its unit volume.
> (If the business requires additional working capital... **the increment also should be
> included in (c)**.)" ... "**(c) must be a guess** — and one sometimes very difficult to
> make." — 1986 letter [E2-23] (`Shareholder Letters/1986 Letter.txt:1650`)

### Owner earnings — MULTI-YEAR MEAN, never a single year
    OE = mean over 3 years of (Operating Cash Flow − SBC) − mean maintenance capex

- OE tier table (all verified years, both ends of the capex band): ____
- **3-yr mean OE (the anchor):** ____   ·   5-yr mean (consistency cross-check): ____
- **MAINTENANCE CAPEX IS A DISCLOSED JUDGMENT, NOT AN OUTPUT** ("must be a guess").
  Band used: ____ (default D&A floor .. total capex ceiling). Basis for where it sits
  in the band, cited from the filing: ____
- If the band changes the verdict → **UNKNOWABLE** (the 7-foot bar rule).

### The stress test — COMPANY-SPECIFIC, QUANTIFIED, WITH A PROBABILITY
> "**Consider some mathematics:** ... If 10% of all $48 billion of the bank's loans...
> produced losses averaging 30% of principal, **the company would roughly break even.**
> A year like that — **which we consider only a low-level possibility, not a likelihood**
> — **would not distress us.**" — 1990 letter [E3-24]
> (`Shareholder Letters/1990 Letter.txt:326-332`)

- **Name the specific mechanism by which THIS business gets hurt:** ____
- **Quantify it from filed figures**, and state the resulting outcome: ____
- **Probability:** [ ] likely [ ] a real possibility [ ] a low-level possibility
- Generic floor (used only where no specific mechanism can be quantified): survives a 50%
  OE decline ×2yr? [ ] YES [ ] NO — *and if no specific mechanism can be named at all,
  consider UNKNOWABLE.*

### Fortress (two-track, FA ratified 2026-07-15)
- Financial business (bank / insurer / balance-sheet levered)? [ ] N [ ] Y
  · If N — cash + undrawn vs debt due <24mo ____ ; schedule termed out? [ ] Y [ ] N
  · If Y — **assets ____ ÷ equity ____ = ____:1 → >10:1 is an AUTOMATIC OUT, no exception**
- **VERDICT: [ ] IN  [ ] OUT — STOP  [ ] UNRESEARCHED — work order: ____  [ ] UNKNOWABLE — CLOSE**

## GATE 5 — INVERSION
- Bull-case assumptions listed: ____
- Mandatory inversions, **each with a stated probability** (1990-letter standard):

| Inversion | Scored [D/DS/P/U] | Probability |
|---|---|---|
| Moat destruction | | likely / real possibility / low-level possibility |
| Management failure | | |
| Balance sheet | | |
| Thesis-breaking metric | | |

- Any [U] on a mandatory inversion? [ ] NO [ ] YES → **a [U] is UNRESEARCHED if a document
  would settle it, UNKNOWABLE if none would. Never a caveat carried forward.** Written justification if proceeding anyway: ____
- **Thesis-breaking metric + exit threshold, pre-committed [E1-02]:** ____
  (read on the ADJUSTED figure where one-time items could mask deterioration)
- **VERDICT: [ ] IN  [ ] OUT — STOP  [ ] UNRESEARCHED — work order: ____  [ ] UNKNOWABLE — CLOSE**

---
⛔ **VALUATION LOCK — do not fill below this line unless Gates 1-5 each show IN.**
A gate marked TOO HARD closes the file. It is not a pass.

---
## GATE 6 — PRICE AND COMMITMENT
*(absorbs the old Gates 7 and 8. Gate 8's asymmetry ratio was computed in 10 of 121 runs
and Ruling 6 moved its useful output — the implied-growth reverse DCF — into the ladder
below, where it now runs on every name.)*

> **FRAMEWORK CONVENTION — Buffett does not run a DCF.** Munger, 1996: "Warren talks about
> these discounted cash flows. **I've never seen him do one.**" Under Ruling 14 the DCF is
> retained only as the ENGINE that converts growth into a comparable rate — it produces the
> equity premium and the implied growth, and casts no vote.

- **PRE-MODEL VERDICT (record BEFORE Book Two; binding):** is it obvious this will
  **WORK OUT WELL** — materially larger and still advantaged in ten years?
  [ ] OBVIOUS  [ ] NOT OBVIOUS  ·  *Tests the OUTCOME, not the price (Ruling 4-C). Do
  not smuggle price into this line.* If NOT OBVIOUS the verdict is WAIT whatever Book Two
  returns — but run and record Book Two anyway.

### ONE BOOK — THE OWNER-EARNINGS YIELD (Ruling 14)
> "we purchased our 10% interest in Wells Fargo for $290 million, **less than five times
> after-tax earnings**" — 1990 letter. Every worked valuation in the corpus is a yield or
> a multiple. There is not one DCF in it.

**Owner earnings is THE number. Three outputs, one model. The DCF is an ENGINE, not a
voter — it computes 2 and 3 and issues no verdict of its own.**

**1. THE YIELD**
- anchor OE (current tier, Ruling 9-A) ____ ÷ market cap ____ = **____ %**
- sovereign (earnings currency) ____ % + size premium ____ % = hurdle **____ %**

**2. WHAT THE PRICE ALREADY ASSUMES**
- implied year-1 OE growth needed to justify the quote: **____ %**
- what the business has actually done (3-yr OE growth): ____ %

**3. WHAT YOU ACTUALLY GET — THE DECISION NUMBER**
- IRR at the current price on base-case growth: ____ %
- **= ____ POINTS OF EQUITY PREMIUM over the sovereign**
- rate for the fair-value calc = sovereign + Aesop moat spread (Ruling 4-A) = ____ %
- *A wide range around this is a PASS, not a puzzle to solve [E4-01]. If the verdict
  turns on narrowing it, the answer is UNKNOWABLE (7-foot bar rule).*

### THE PRICE LADDER — ROUND NUMBERS
> "I would rather be **vaguely right than precisely wrong**." — Keynes via the 1986 letter

  · **CHEAP**   roughly $____   = IV × (1 − MOS)  — buy with a cushion, full size
  · **FAIR**    roughly $____   = IV — pay value, earn exactly the discount rate, starter
  · **CURRENT** $____ = ____× fair value

- **MOS per the Ruling 5-A ladder** (applied ONCE, at the end — Ruling 7): 10% base
  (WIDE, 4/4 inversions resolved, fortress with room) · +10 NARROW or PROVISIONAL · +10
  per unresolved inversion · +10 tight fortress · floor 50% permanent-loss risk · cap 60%.
  **MOS used: ____ % — derivation: ____**

### TWO VERDICTS, STATED SEPARATELY AND NEVER MERGED
- **BUSINESS:** ____
- **PRICE:** ____

### THE COMMITMENT (was Gate 7 — filled before any order)
- Thesis-confirming metric: ____ · Thesis-breaking metric: ____ · Next catalyst: ____
- **Size** (conviction × MOS; illiquidity cap if OTC; **sized DOWN if a Gate 3 capital
  allocation flag is live**): ____
- **VERDICT: [ ] BUY-ELIGIBLE (price ≤ CHEAP, full size) [ ] STARTER (price ≤ FAIR)
  [ ] WAIT — standing order at the ladder
  [ ] UNRESEARCHED — work order: ____  [ ] UNKNOWABLE — CLOSE**

---
## SELF-AUDIT (the run is incomplete until every box is checked)
- [ ] Sections completed in order; no verdict line skipped
- [ ] **Every gate returned IN, OUT, UNRESEARCHED or UNKNOWABLE — no gate marked IN
      carries an "unverified" or "provisional" caveat**
- [ ] **Every UNRESEARCHED verdict carries a work order naming the artifact and rung**
- [ ] **Every UNKNOWABLE verdict states what specifically cannot be known**
- [ ] Step 0-B filled: the filing was read, with document and accession number
- [ ] Owner earnings on a MULTI-YEAR MEAN; maintenance-capex band disclosed as a judgment
- [ ] Stress test names a specific mechanism, quantified, with a probability
- [ ] Gate 2 competitor row filled, or the moat class marked PROVISIONAL
- [ ] Book One anchored to the CURRENT tier; cross-check stated
- [ ] Year-1 growth ≤ lower of recent OE growth / guidance
- [ ] IV stated as a round-number RANGE, not a point estimate
- [ ] MOS derived from the Ruling 5-A ladder and shown
- [ ] Prices/market cap dated; aggregator used for live quotes only and flagged
- [ ] Step 0 rates dated; >50bp rule checked
- [ ] Run committed to git

## ELIMINATED / CLOSED REGISTER
- Verdict: [ ] OUT (about the business) [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- Reason, in one line: ____
- **If UNRESEARCHED — THE WORK ORDER (required):** artifact ____ · where it lives ____
  · ladder rung ____ · blocked by ____
- **If UNKNOWABLE:** what specifically cannot be known, in the 2006 form? ____
