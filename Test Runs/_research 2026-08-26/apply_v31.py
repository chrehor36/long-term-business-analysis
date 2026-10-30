import os
BASE = r"c:\Users\chreh\OneDrive\Documents\BRK"

# ---------------------------------------------------------------- CLAUDE.md
p = os.path.join(BASE, "CLAUDE.md")
s = open(p, encoding="utf-8").read()

v31 = '''## FRAMEWORK v3.1 — THE THREE BOXES. RATIFIED 2026-08-26. READ BEFORE ANY RUN.
This is the simplification. It came from reading five corpus passages in full at the
operator's instruction. Full write-up: "Framework/2026-08-26 THE FIVE PASSAGES -
Synopsis and Rulings.md" and "Framework/2026-08-26 AUDIT - What Actually Works, and
What To Cut.md".

**RULING 12 — EVERY GATE RETURNS ONE OF THREE VERDICTS: IN / OUT / TOO HARD.**
> "Charlie says, you know, 'We've got three boxes at the company: in, out, and too
> hard.' And a lot of things end up in the 'too hard' pile, and it doesn't bother us."
> -- Buffett quoting MUNGER, 2006 meeting (Annual Meetings/2006 Annual Meeting.txt:215)

- **OUT** is a judgment about the BUSINESS. It stops the run and is permanent.
- **TOO HARD** is a judgment about MY EVIDENCE. It closes the file WITHOUT PREJUDICE and
  records nothing about the business. Re-openable.
- **They must never be merged.**
- **TOO HARD IS THE DEFAULT WHEN EVIDENCE IS THIN.** A gate marked IN carrying
  "unverified", "general knowledge", "not independently confirmed" or "provisional" is a
  TOO HARD verdict wearing an IN label. This rule exists because the July 2026 Japan runs
  did exactly that and put unverified names into the portfolio.
- **THE 7-FOOT BAR RULE** (2005 meeting, Annual Meetings/2005 Annual Meeting.txt:977):
  "there's no degree of difficulty factor... we get paid, not for jumping over 7-foot
  bars, but for stepping over 1-foot bars... I'd rather have the universe be a little
  smaller than it really is, than being interpreted as larger than it is." **If a verdict
  only holds after narrowing assumptions or adjudicating a sensitivity grid, it is
  TOO HARD.**

**STRUCTURE: 8 GATES BECOME 6.**
- **GATE 8 DELETED.** Its asymmetry ratio was actually computed in 10 of 121 run files,
  and Ruling 6 already moved its useful output (the implied-growth reverse DCF) into the
  price ladder, where it now runs on every name.
- **GATE 7 MERGED into Gate 6** as "THE COMMITMENT" (size, thesis metrics, catalyst).
- Gates 1-5 unchanged in subject, changed in standard (below).

**GATE 2 — THE COMPETITOR ROW IS NOW REQUIRED** (Ruling 11, [E3-28], 1996 meeting,
Annual Meetings/1996 Annual Meeting.txt:681): "I can't be an intelligent owner of a
business unless I know what all the other businesses in that industry are doing." A moat
is a claim about RELATIVE position and cannot be evidenced from one company's numbers.
Name 2-3 closest competitors, same metric, same window, filing-sourced. Where competitor
data is unavailable, the moat class is **PROVISIONAL** and takes the wider NARROW spread.

**GATE 3 — THE HALF-OWNER TEST** replaces the vague "integrity (binary)" line [E3-28]:
does this company's reporting tell me what a 50% partner, away for a year, would have
told me? A one-time item quantified separately at every line passes; the same item buried
in an adjusted figure does not.

**GATE 4 — TWO CHANGES.**
1. **Owner earnings on a MULTI-YEAR MEAN**, never a single year, per [E2-23]'s "the
   AVERAGE ANNUAL AMOUNT": OE = mean over 3 years of (Operating Cash Flow - SBC) - mean
   maintenance capex. **Maintenance capex is a DISCLOSED JUDGMENT, not an output** --
   Buffett says (c) "must be a guess". If the band changes the verdict, TOO HARD.
2. **The stress test is COMPANY-SPECIFIC, QUANTIFIED, AND CARRIES A PROBABILITY**, per
   the 1990 Wells Fargo passage [E3-24] (Shareholder Letters/1990 Letter.txt:326-332):
   name the specific mechanism by which THIS business gets hurt, quantify it from filed
   figures, state the outcome and the likelihood ("a low-level possibility, not a
   likelihood"). The generic 50%-decline-x-2yr test is the floor, used only where no
   specific mechanism can be quantified -- and if none can be named at all, consider
   TOO HARD.

**GATE 5 — EACH INVERSION CARRIES A STATED PROBABILITY** (likely / a real possibility /
a low-level possibility). A [U] on a mandatory inversion is a TOO HARD signal, not a
caveat to carry forward.

**GATE 6 — TWO CHANGES.**
1. **RULING 9-A IS SETTLED: Book One anchors on the MOST RECENT verified tier**, on
   "Wells Fargo CURRENTLY EARNS" [E3-24]. The 5-year mean is a consistency cross-check
   only. Where the two diverge materially and the divergence cannot be explained, the
   verdict is TOO HARD, not an average.
2. **INTRINSIC VALUE IS REPORTED AS A ROUND-NUMBER RANGE**, never a point estimate. 1986
   letter, quoting Keynes approvingly: "I would rather be VAGUELY RIGHT than PRECISELY
   WRONG." A figure like "$71.84" implies a precision this method cannot support; the
   honest form is "roughly $70 to $85".

**WHAT THE EVIDENCE SAYS WORKS (2026-08-26 audit), so it is not cut:**
Gate 3 integrity (WFC fails at the 2014 and 2016 anchors on genuinely prior filed
matters, years before the Sept 2016 scandal; FITB x3, KLAC x2, BEN x2), the full
owner-earnings formula (F, CMG, AN cleared an NI screen with NEGATIVE owner earnings),
and the 10:1 leverage ceiling (Citigroup mid-2007 = 19:1, automatic). All three are
price-independent, which is why they survived the look-ahead bug.

**AND WHAT THE EVIDENCE DOES NOT SUPPORT — say this plainly whenever asked:**
the market-beating claim is **UNPROVEN**. Every backtest that beat the market ran
through a screen with a look-ahead bug and was WITHDRAWN 2026-07-25; the only
uncontaminated full-gate test (BT-11, 32 years) UNDERPERFORMED; BT-15 beat SPY at 2 of
8 anchors; BT-16 won 49.6% of 944 one-year holdings. Book One does not select. Never
present the framework as proven to beat the market.

'''

anchor = "## PHASE 0 — INVENTORY & SPINE (exit: corpus_map.md exists)"
assert anchor in s
s = s.replace(anchor, v31 + anchor)

# operator protocol: update rule 6 and add rule 7
old6 = "6. THE PRICE LADDER IS THE DELIVERABLE (Ruling 6, 2026-08-01)."
assert old6 in s
s = s.replace(old6,
 "6. THREE BOXES, NOT TWO (Ruling 12, 2026-08-26). Every gate returns IN, OUT or\n"
 "   TOO HARD. A gate marked IN that carries an \"unverified\" or \"provisional\"\n"
 "   caveat is a protocol violation -- write TOO HARD. TOO HARD closes the file\n"
 "   without prejudice and is never reported as a pass.\n"
 "7. THE PRICE LADDER IS THE DELIVERABLE (Ruling 6, 2026-08-01).")

open(p, "w", encoding="utf-8").write(s)
print("CLAUDE.md updated with the v3.1 block and protocol rule 12")

# ------------------------------------------------- PENDING RULINGS: ratify
p2 = os.path.join(BASE, "Framework", "PENDING RULINGS.md")
r = open(p2, encoding="utf-8").read()
r = r.replace("## PROPOSED 2026-08-26, AWAITING RATIFICATION. Raised by the operator asking",
              "## \u2705 RATIFIED 2026-08-26. Raised by the operator asking")
r += '''

---
## RULING 12: THE THREE BOXES. Every gate returns IN, OUT or TOO HARD.
## ✅ RATIFIED 2026-08-26. This is the framework's primary simplification and it
## SUPERSEDES the "eight gates to six" proposal as the headline change.

Raised by reading `Annual Meetings/2006 Annual Meeting.txt:215` in full, at the
operator's instruction, after the 2026-08-26 audit.

**ATTRIBUTION, corrected under Prime Rule 1:** the line is **MUNGER'S**, quoted by
Buffett. The text reads "**Charlie says**, you know, 'We've got three boxes at the
company: in, out, and too hard.'" It was given as Buffett's in chat; corrected here.

> "There's just games that are too tough. Charlie says, you know, **'We've got three
> boxes at the company: in, out, and too hard.'** And **a lot of things end up in the
> 'too hard' pile, and it doesn't bother us.** [...] What I've learned is I know enough
> not — **to know that I don't know enough** to make an investment decision."

Munger again the same day (`:821`): "**If something is too hard to do, we look for
something that isn't too hard to do. What could be more obvious than that?**"

And 2005 (`Annual Meetings/2005 Annual Meeting.txt:977`): "there's **no degree of
difficulty factor**... we get paid, **not for jumping over 7-foot bars, but for stepping
over 1-foot bars**... **I'd rather have the universe be a little smaller than it really
is, than being interpreted as larger than it is.**"

### THE FINDING
The audit had proposed cutting eight gates to six. **Reading the passage in full shows
that was the wrong read.** The corpus does not complain about the NUMBER of tests. It
insists on a **THIRD OUTCOME**. Their filter has three boxes; ours had two, because every
gate returned PASS or FAIL.

**FAIL and TOO HARD are different findings.** FAIL says the business is bad. TOO HARD
says the business may well be excellent and I cannot tell. Collapsing the second into the
first produces false confidence in both directions: names get rejected that were merely
unexamined, and — the live failure mode — names get PASSED on thin evidence because the
only alternative on offer was a verdict the analyst did not believe.

### RULING
1. **Every gate returns IN, OUT or TOO HARD.**
   - **IN**: evidence present, clears the bar. Proceed.
   - **OUT**: evidence present, business fails. STOP. Permanent. Eliminated register.
   - **TOO HARD**: cannot tell. CLOSE the file **without prejudice**. No finding about the
     business. Re-openable if better evidence appears, and the run must record **what
     evidence would re-open it**.
2. **TOO HARD IS THE DEFAULT WHEN EVIDENCE IS THIN.** A gate marked IN carrying
   "unverified", "general knowledge", "not independently confirmed" or "provisional" is a
   TOO HARD verdict wearing an IN label. **This is now a protocol violation.**
3. **THE 7-FOOT BAR RULE.** A conclusion that required fighting for it is worth less, not
   more. If a verdict only holds after narrowing assumptions or adjudicating a
   sensitivity grid, the verdict is **TOO HARD**.
4. **TOO HARD is never reported as a pass**, never carried into a portfolio, and never
   used to authorize an order.

### THE LIVE FAILURE THIS FIXES
The July 2026 Japan runs (NCLTY, MITSY, NHNKY) each opened "No corpus/SEC sources --
general-knowledge", used **NI as an owner-earnings proxy**, and recorded **PASS** at
every gate. Two were marked BUY-ELIGIBLE and bought. **Those were TOO HARD verdicts
wearing a PASS label.** Under Ruling 12 all three close at Gate 4 (Step 0-B, filing not
read) and never reach a valuation, let alone an order.

### WHAT THIS DOES *NOT* CHANGE
The Gate 8 deletion stands on its own separate evidence (the asymmetry ratio was computed
in 10 of 121 run files; Ruling 6 already absorbed its useful output). Gate 7 merges into
Gate 6. **8 gates become 6 — but that is now the secondary change, not the headline.**
A framework with a real TOO HARD box is simpler in USE than a shorter one that forces
every name to a verdict.
'''
open(p2, "w", encoding="utf-8").write(r)
print("PENDING RULINGS: Ruling 11 ratified, Ruling 12 written and ratified")
