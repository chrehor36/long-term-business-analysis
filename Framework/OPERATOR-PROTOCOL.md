# THE OPERATOR PROTOCOL AND THE PRIME RULES
# Binding on every session that touches this project. Audited by `tools/check_framework.py`.

*This file was lifted from `CLAUDE.md` on 2026-09-25, when `CLAUDE.md` became the map of the
project. The text below is the text that stood in `CLAUDE.md` that day, unchanged, with its dated
correction notes; the rule numbers are unchanged, so every "operator rule 5" and "PRIME RULE 3" in
the run files still points where it did. Two presentation changes only: the tools and the sovereign
series are set as tables, and two file names are written in full. Where this file and the governing
documents (`THE FRAMEWORK v4.md`, `THE HOLDINGS FRAMEWORK.md`) disagree, the corpus wins (PRIME RULE 2).*

---
## OPERATOR PROTOCOL — binds any session applying the framework to a company

1. **RUN FILE FIRST.** Copy `Test Runs/_TEMPLATE - Company Run.md` to a dated file and fill
   it top to bottom. The template is the enforcement surface.
2. **HARD SEQUENCE.** No Q5 output may be reported unless Q1-Q4 each show IN. UNRESEARCHED
   and UNKNOWABLE both close the file; neither is a pass.
3. **COMPUTATION IS NOT CLEARANCE.** Any valuation math produced before Q1-Q4 close must be
   headed **"COMPUTATION — NOT A CLEARANCE"** and may carry no entry language.
4. **THE FILING GETS READ.** Tagged data is transcription and screening. No name reaches Q5
   on XBRL alone. Record the document, date and accession number, and cross-check one
   figure against the filed statement.
5. **STRICT INPUTS.** Owner earnings never via a net-income proxy. Sovereign for the
   **earnings currency**, from the issuing authority, dated. Primary filings over
   aggregators; aggregators for live quotes only, flagged.
6. **THE AUDIT IS PART OF THE RUN.** A run is incomplete until its self-audit is checked.
   Violations found later are corrected in an addendum, never by editing history.
7. **STATE THE HONEST RECORD WHEN ASKED.** The market-beating claim is **UNPROVEN**. Every
   backtest that beat the market ran through a screen with a look-ahead bug and was
   withdrawn 2026-07-25; the only uncontaminated full-gate test underperformed over 32
   years; the corrected basket beat the index at 2 of 8 anchors; the mechanical layer wins
   49.6% of 944 one-year holdings. The loss leg passes thinly (Test E, pre-registered;
   replicated by BT-17, 2026-08-28, in both a 13-anchor S&P panel and a two-anchor
   micro-cap panel — thin, survivorship-conditioned, return leg still trailing).
   The corpus itself attributes the record to the man, the system, luck and devotion
   **[E5-19]** — not to the selection method alone. **Never present the framework as
   proven to beat the market.**
8. **THE DIVISION OF LABOR** *(operator directive, 2026-08-28)*. **Arithmetic is
   automated; judgment is made by the AI running the framework; every judgment is
   justified from the corpus by ledger id, or it is not a judgment — it is an opinion.**
   Tools fetch and compute and are forbidden to conclude; every flag is a prompt to read,
   never a score.
9. **THE ANALYST IS ALSO A SUBJECT OF THE PSYCHOLOGY.** The misjudgment catalogue reads
   you, not just the management: *"Never, ever, think about something else when you should
   be thinking about the power of incentives"* **[E4-27]** — and the analyst holding a
   position has an incentive to clear it; the builder of a framework has an incentive to
   validate it. The antidotes are the corpus's own: hunt disconfirming evidence hardest
   for your favourite hypothesis **[E4-26]**, and *"you must not fool yourself, and you're
   the easiest person to fool"* **[E3-41]**. In practice: pre-register before computing,
   frame tests to refute, and let the acceptance test fail the build.

---
## TOOLS — efficiency only, never a new model

| Command | What it does |
|---|---|
| `python tools/check_framework.py` | the acceptance test: no phantom cites, no unlabelled numbers, every ledger row verbatim against its cited source, no phantom id in any run file, every path in a pointer file on disk |
| `python tools/ledger_verbatim.py` | the verbatim check on its own, row by row (adopted 2026-09-20) |
| `python tools/sources.py` | the three sovereigns, from the issuing authority |
| `python tools/run.py TICKER [--write]` | pre-fill a run file with the arithmetic |

**The test on any tooling: does it get the same number sooner, or does it add a number?**
The second is forbidden. No tool may add a step, only remove friction from one.

Sovereign sources, **issuing authority first** *(corrected 2026-09-02)*:

| Currency | Source | Series or file |
|---|---|---|
| USD | **US Treasury daily par yield curve** | the 30-year par yield |
| JPY | Japan Ministry of Finance | *jgbcme.csv* |
| EUR | ECB Statistical Data Warehouse | *YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y* |
| USD fallback | FRED *DGS30* | **the FALLBACK, not the source.** FRED lags a day or two behind the intraday quote; immaterial, but know it |

*Why this changed: operator rule 5 requires the sovereign "from the **issuing authority**",
and FRED is a Federal Reserve Bank of St. Louis redistribution of a Treasury series, not the
Treasury. This line had contradicted the protocol above it since v4 was written. `tools/daily_fetch.py`
had already moved to the Treasury curve with FRED as fallback; the PLAB run of 2026-09-02 hit
five consecutive FRED connection refusals and went to the Treasury directly, which is UP the
evidence ladder, not a workaround. The document is now made to match both the protocol and the
practice.*

**Market cap is split-invariant** — the fix for the look-ahead bug that voided four
backtests: `cap = close(anchor) × shares(measurement) × splits AFTER measurement`. Use
`close`, never `adjclose`.

---
## PRIME RULES — apply to every piece of work
1. **VERBATIM ONLY.** The ledger takes exact quotes with year and source file. Paraphrase
   is never recorded as quotation. Flag OCR and transcript artifacts; never smooth them.
2. **THE TEXT WINS.** Where the framework and the corpus disagree, the corpus wins. Audit
   the framework; do not defend it.
3. **CONFESS INVENTIONS.** Anything useful but unsourced is labelled **CONVENTION** with a
   one-line rationale, or it is deleted. **A CONVENTION label may confess an invention; it may
   never license conduct a rule forbids.** *(Clause added 2026-09-20 at the operator's "Fix", decision
   15: seven run files of 2026-07-15 labelled a net-income proxy for owner earnings a "FRAMEWORK
   CONVENTION" and their self-audits ticked the box, while operator rule 5 forbids the proxy
   outright. The corpus already ruled: the owner-earnings figure is chosen over the GAAP figure by
   name and "(c) must be a guess" [E2-09], so an unobtainable input obliges a disclosed guess
   [E3-44], never a substitute number. The worked case is
   `Test Runs/ADDENDUM 2026-09-20 - the net-income proxy seven, and why a CONVENTION label cannot license operator rule 5.md`.)*
4. **CITATION SHELF.** Partnership letters, Berkshire letters, Wesco letters, meeting
   transcripts, Poor Charlie's Almanack, An Owner's Manual, Buffett's Fortune essays, the
   `Special Letters`, the 2014 fiftieth-anniversary pair published inside that year's
   Berkshire annual report *(eighth class named 2026-09-20: the 07:32 sweep found the ledger
   drawing on eight folders and this rule naming seven; **[E5-19]** is from this class and
   operator rule 7 cites it, so the honesty rule depended on a source the shelf did not list)*.
   Graham is off the shelf *(2026-07-13)*: his concepts are cited through Buffett's and
   Munger's own articulations, and he may be named only as they name him. **Ninth class, named
   2026-10-04: the signed chairman's sections of each Berkshire annual report** (Owner-Related
   Business Principles as printed that year, Acquisition Criteria, Intrinsic Value, The Managing of
   Berkshire), cited to the report file with a line span; the financial statements, notes and
   Management's Discussion in the same file stay off the shelf as context. *(The case is
   `Framework/v5/CASE 2026-10-03 - v5 from the meetings, for the operator's approval.md`, CASE 2,
   approved in principle by the operator on 2026-10-03. The first rows of the class were written by the
   v5 read on 2026-10-03 (the 1996 AM unit, principle_ledger_v5.csv, ids R1995-001 onward), and this
   sentence was added the next morning: PRIME RULE 6, the row before the rule. The sections exist by
   those headings in the FY1995 to FY2017 reports only.)*
5. **ASK BEFORE STRUCTURAL CHANGE.** Adding, merging or deleting a question requires a
   written case with quotes, presented for approval first.
6. **NOTHING IS WRITTEN UNTIL ITS EVIDENCE EXISTS.** A rule enters the framework only after
   its ledger row does.

## THE STANDARD
Another analyst must be able to verify any rule against its cited source in **under two
minutes**. `tools/check_framework.py` enforces the machine-checkable half of that.
