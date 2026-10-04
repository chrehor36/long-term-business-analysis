# -*- coding: utf-8 -*-
"""Generate: The Analysis Workbook v3.0 (July 2026).
Fillable sheets, one set per company. Field amendments integrated in flow:
Step 0 (rate refresh) opens Sheet 7; Sheet 7-B is the Buffett Statute;
Scream Test closes the valuation block; range anchoring governs Sheets 7/9.
Checkbox glyphs use DejaVuSans."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, Spacer, Table, TableStyle

from v3_style import (CHECK, GOLD_PALE, GRAY, MOTTO, NAVY, NumberedDoc, PALE,
                      S, callout, rule_card, source_class_box)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "The Analysis Workbook v3.0.pdf")
P, SP = Paragraph, Spacer
el = []

def line(label, w1=1.9, w2=4.8):
    t = Table([[P(f"<b>{label}</b>", S["formlabel"]), P("", S["formline"])]],
              colWidths=[w1 * inch, w2 * inch])
    t.setStyle(TableStyle([("LINEBELOW", (1, 0), (1, 0), 0.6, GRAY),
                           ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                           ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    return t

def lines2(l1, l2, w=3.35):
    t = Table([[line(l1, 1.5, w - 1.6), line(l2, 1.5, w - 1.6)]],
              colWidths=[w * inch, w * inch])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    return t

def checks(prompt, options):
    opts = "&nbsp;&nbsp;&nbsp;".join(f"{CHECK} {o}" for o in options)
    return P(f"<b>{prompt}</b>&nbsp;&nbsp; {opts}", S["formline"])

def bigbox(label, h=0.55):
    t = Table([[P(f"<b>{label}</b>", S["formlabel"])], [SP(1, h * inch)]],
              colWidths=[6.7 * inch])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.6, GRAY),
                           ("LEFTPADDING", (0, 0), (-1, -1), 6),
                           ("TOPPADDING", (0, 0), (-1, -1), 4)]))
    return t

def gate_result(g, extra="FAIL — stop"):
    return callout([P(f"<b>GATE {g}:</b>&nbsp;&nbsp;{CHECK} PASS&nbsp;&nbsp;&nbsp;{CHECK} {extra}",
                      S["formline"])])

def grid(headers, nrows, widths):
    data = [[P(f"<b>{h}</b>", S["formlabel"]) for h in headers]]
    for _ in range(nrows):
        data.append(["" for _ in headers])
    t = Table(data, colWidths=[w * inch for w in widths],
              rowHeights=[16] + [20] * nrows)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, GRAY),
                           ("BACKGROUND", (0, 0), (-1, 0), PALE),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 4)]))
    return t

# ---------- cover ----------
el += [SP(1, 70), P("THE ANALYSIS WORKBOOK", S["title"]), SP(1, 8),
 P("Fillable Application Sheets — One Set Per Company Under Analysis<br/>"
   "Companion to: A Framework for Long-Term Business Analysis", S["subtitle"]),
 SP(1, 6), P("VERSION 3.0 — JULY 2026", S["edition"]), SP(1, 20),
 P("“I believe in establishing yardsticks prior to the act; retrospectively, almost anything can "
   "be made to look good in relation to something or other.”", S["epigraph"]),
 P("— Buffett, 1961 partnership letter [E1-02]", S["epigraphsrc"]), SP(1, 22),
 P("Print Sheets 1–8 fresh for every new company. Sheet 9 every quarter held. Sheet 10 once per "
   "year. Rules: (1) complete sheets in sequence — a FAIL at any gate stops the analysis; "
   "(2) every figure from primary filings (10-K, 10-Q, 20-F, 6-K, earnings-call transcripts); "
   "(3) no analyst estimates, adjusted metrics, or data aggregators; (4) definitions and all "
   "source citations are in the Framework document.", S["small"]), PageBreak()]

# ---------- sheet 1 ----------
el += [P("SHEET 1 — COMPANY OVERVIEW AND GATE TRACKER", S["h1"]),
 lines2("Company:", "Ticker:"), lines2("Exchange:", "Sector:"),
 lines2("Market cap:", "Currency:"), lines2("Current price:", "Analysis date:"),
 SP(1, 4),
 bigbox("Business description — your own words, no quoting management", 0.5),
 bigbox("How does it make money at the unit-economics level?", 0.5),
 bigbox("My informational edge (required — none means reconsider Gate 1)", 0.4),
 SP(1, 6), P("Gate tracker", S["h2"]),
 grid(["Gate", "Title", "Result", "Date"], 8, [0.6, 3.1, 1.8, 1.2]),
 SP(1, 4),
 checks("Final decision:", ["ENTER POSITION", "WATCHLIST — WAIT FOR PRICE", "DOES NOT QUALIFY"]),
 lines2("Statute hurdle (Sheet 7-B):", "Max buy price (Sheet 7):"), PageBreak()]

# ---------- sheet 2 ----------
el += [P("SHEET 2 — CIRCLE OF COMPETENCE | GATE 1", S["h1"]),
 rule_card("GATE QUESTION", [P("Can I independently verify the moat claim without relying on "
   "management’s description? “If you don’t feel comfortable making a rough estimate of the "
   "asset’s future earnings, just forget it and move on.” [E5-02]", S["cardbody"])]), SP(1, 6),
 checks("Q1. Unit economics understood?", ["YES", "NO"]),
 checks("Q2. Primary cost drivers identifiable without the annual report?", ["YES", "NO"]),
 checks("Q3. Informational edge (vs public narrative)?", ["YES — describe below", "NO"]),
 checks("Q4. Multi-segment: each segment evaluable independently?", ["YES", "NO", "N/A"]),
 SP(1, 4), P("Failure-mode check (any YES = reconsider)", S["h3"]),
 checks("Familiarity mistaken for understanding?", ["YES", "NO"]),
 checks("Assuming domain expertise transfers?", ["YES", "NO"]),
 checks("Thesis built on narrative, not numbers?", ["YES", "NO"]),
 SP(1, 4), bigbox("Moat mechanism in my own words (from memory — no quoting management)", 0.9),
 SP(1, 6), gate_result(1), PageBreak()]

# ---------- sheet 3 ----------
el += [P("SHEET 3 — MOAT IDENTIFICATION | GATE 2", S["h1"]),
 P("Evaluate each segment independently — never a conglomerate as a single moat (OM-5). Run the "
   "FRANCHISE TEST first [E3-03], then classify.", S["small"])]
for seg in (1, 2):
    el += [P(f"SEGMENT {seg}" + ("" if seg == 1 else "  (N/A if single segment)"), S["h2"]),
     line("Segment name:"),
     P("Franchise test [E3-03]:", S["h3"]),
     checks("Needed or desired?", ["YES", "NO"]),
     checks("No close substitute in customers’ minds?", ["YES", "NO"]),
     checks("Free of price regulation?", ["YES", "NO"]),
     checks("Proven by aggressive pricing + high returns on capital?", ["YES", "NO"]),
     checks("Moat type (convention P42):",
            ["SWITCHING COST", "NETWORK EFFECT", "INTANGIBLE", "COST ADV.", "NONE"]),
     line("Primary moat metric:"),
     grid(["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"], 1,
          [0.83] * 8),
     checks("Direction [E4-02]:", ["WIDENING", "STABLE", "NARROWING"]),
     checks("Classification:", ["WIDE (20+ yrs)", "NARROW (10–20)", "NONE"]),
     bigbox("Single scenario that destroys this moat", 0.35), SP(1, 4)]
el += [gate_result(2), PageBreak()]

# ---------- sheet 4 ----------
el += [P("SHEET 4 — MANAGEMENT INTEGRITY | GATE 3", S["h1"]),
 lines2("CEO / tenure:", "CFO / tenure:"),
 P("Dimension 1 — INTEGRITY (binary; candor standard = OM-12)", S["h2"]),
 checks("Unflattering info volunteered (not only when required)?", ["YES", "NO"]),
 checks("Deteriorating metrics led with, not buried?", ["YES", "NO"]),
 checks("No selective-disclosure pattern?", ["YES", "NO"]),
 checks("No restatements / SEC letters / disclosure failures?", ["YES", "NO"]),
 line("Evidence (filing + date):"),
 callout([P(f"<b>Integrity verdict:</b>&nbsp; {CHECK} PASS &nbsp;&nbsp; {CHECK} FAIL — "
            "DISQUALIFIED — one deliberate deception ends the analysis", S["formline"])]),
 P("Dimension 2 — COMPETENCE (OM-3, OM-9, [E5-01])", S["h2"]),
 checks("Returns above cost of capital over a full cycle?", ["YES", "NO", "INSUFF. DATA"]),
 checks("$1 retained → ≥ $1 market value (OM-9, corrected form)?", ["YES", "NO", "N/A"]),
 checks("Buybacks only under the two 2011 conditions?", ["YES", "NO", "N/A"]),
 checks("Says no to bad acquisitions (OM-8)?", ["YES", "NO", "N/A"]),
 P("Dimension 3 — ALIGNMENT (OM-2)", S["h2"]),
 checks("Wealth in shares held (not options)?", ["YES", "NO"]),
 checks("Compensation on owner-economics (not adjusted metrics)?", ["YES", "NO", "UNCLEAR"]),
 checks("Shareholders addressed as partners (OM-1)?", ["PARTNERS", "MANAGED"]),
 SP(1, 6), gate_result(3), PageBreak()]

# ---------- sheet 5 ----------
el += [P("SHEET 5 — OWNER EARNINGS | GATE 4", S["h1"]),
 rule_card("THE COMPLETE 1986 FORMULA [E2-08]", [
   P("OE = Net income + D&amp;A/non-cash charges − Maintenance capex − Required working-capital "
     "increment", S["cardbody"])]), SP(1, 6),
 lines2("Filing type / date:", "Fiscal year:"),
 line("Net income (attributable):"),
 line("One-time items stripped (justify each):"),
 lines2("D&A:", "Total capex:"),
 P("Maintenance capex", S["h2"]),
 checks("Management discloses split in MD&A? (overrides bands)", ["YES — use it", "NO"]),
 checks("Business type (convention P44):",
        ["CAP-INTENSIVE (65–70%)", "ASSET-LIGHT (20–30%)", "MIXED (50%)"]),
 lines2("Maintenance capex:", "Growth capex:"),
 line("Working-capital increment (cash-flow stmt):"),
 callout([P("<b>OWNER EARNINGS = ______________</b>  (SBC check: if SBC &gt; 15% of OE — "
            "convention P44 — deduct: adjusted OE = ______________)", S["formline"])]),
 P("Historical OE tiers — range anchoring (FA, P47)", S["h2"]),
 grid(["FY", "Net inc.", "D&A", "Maint. capex", "WC", "OE", "Verified?"], 4,
      [0.7, 1.0, 0.9, 1.15, 0.8, 1.0, 1.05]),
 P("LOWEST VERIFIED OE TIER (buy prices anchor here): ______________", S["formlabel"]),
 P("Balance sheet — the Fortress Test, two tracks (FA, ratified 2026-07-15)", S["h2"]),
 lines2("Net cash / (debt):", "Credit rating (if any):"),
 checks("Is this a FINANCIAL business (bank/insurer/balance-sheet levered)?", ["YES", "NO"]),
 source_class_box("amendment", [
   P("<b>If NO (non-financial) — SURVIVAL TRACK.</b> Credit rating: ______  Undrawn revolver + "
     "cash: ______  vs. debt due within 24 months: ______  Debt schedule termed-out (no cliff "
     "concentration)? " + CHECK + " Y " + CHECK + " N.  Survives a 50% OE decline sustained for "
     "2 consecutive years without existential risk? " + CHECK + " YES " + CHECK + " NO. Ordinary "
     "investment-grade leverage is NOT itself a disqualifier.", S["formline"]),
   P("<b>If YES (financial) — LEVERAGE CEILING (mechanical, no exception).</b> Total assets: "
     "______  Total equity: ______  Assets ÷ equity = ______ : 1.  &gt;10:1 = AUTOMATIC FAIL "
     "regardless of survival-track judgment. [E3-02 context: 1990 letter on 20:1 bank leverage; "
     "validated by Citigroup 2007 at 19:1 — see Backtests.]", S["formline"]),
 ]),
 SP(1, 4), gate_result(4), PageBreak()]

# ---------- sheet 6 ----------
el += [P("SHEET 6 — INVERSION | GATE 5", S["h1"]),
 P("Destroy the thesis before pricing it [E2-20, E2-21, E3-22]. Score: [D] Direct / [DS] "
   "Structural / [P] Partial / [U] Unanswered (convention P42 notation).", S["small"]),
 bigbox("STEP A — every assumption the bull case requires (no list = no thesis)", 0.8)]
for name in ("MOAT DESTRUCTION [E4-04]", "MANAGEMENT FAILURE — inst. imperative [E2-18]",
             "BALANCE-SHEET STRESS (50%×2yr drill)", "ADDITIONAL INVERSION"):
    el += [P(f"MANDATORY — {name}" if "ADDITIONAL" not in name else name, S["h3"]),
           bigbox("Failure scenario", 0.32),
           line("Mgmt response (filing + date):"),
           checks("Score:", ["D", "DS", "P", "U"])]
el += [SP(1, 4),
 rule_card("THESIS-BREAKING METRIC — PRE-COMMITTED [E1-02]", [
   P("Metric: ____________________  Current: __________  Exit threshold (2 consecutive quarters "
     "at/below): __________  Next checkpoint: __________", S["formline"])]),
 SP(1, 6), gate_result(5), PageBreak()]

# ---------- sheet 7 ----------
el += [P("SHEET 7 — VALUATION | GATE 6", S["h1"]),
 source_class_box("amendment", [
   P("<b>STEP 0 — RATE REFRESH.</b> Sovereign 30-yr yield TODAY: ________  Date: ________  "
     "Yield at last valuation: ________  Δ &gt; 50bp? " + CHECK + " YES — revalue holdings  " +
     CHECK + " NO", S["formline"])]), SP(1, 8),
 P("SHEET 7-B — BOOK ONE: THE BUFFETT STATUTE (starter size)", S["h2"]),
 source_class_box("amendment", [
   P("Lowest verified OE tier (Sheet 5): ____________  ÷ Market cap: ____________  = "
     "<b>OE yield: ________%</b>", S["formline"]),
   P("Hurdle: sovereign 30-yr ________% + size premium (" + CHECK + " +1% small/mid  " + CHECK +
     " +2% micro/illiquid  " + CHECK + " +0%) = ________%   Floor 4% applied? " + CHECK +
     " YES  " + CHECK + " N/A", S["formline"]),
   P("Coca-Cola clause (generational moat, Gate 2 = WIDE with [E3-03] all-yes): hurdle × 0.70 = "
     "________%  " + CHECK + " invoked (justify): ______________________", S["formline"]),
   P("<b>STATUTE VERDICT:</b>  " + CHECK + " OE yield ≥ hurdle — wonderful-at-fair, starter size "
     "permitted  " + CHECK + " below hurdle — Book Two price or pass", S["formline"]),
   P("Authorities: Aesop’s three questions [E4-01]; the yardstick rate [E3-23]; certainty-adjusted "
     "discounting [E3-13]. The yardstick is a comparison standard — never a perpetuity input.",
     S["small"])]), SP(1, 8),
 P("BOOK TWO — BUILD-UP DCF (full size) — convention P43", S["h2"]),
 lines2("OE base (lowest verified tier):", "Diluted shares:"),
 lines2("WACC = sov. + ERP + specific:", "Moat class / fade:"),
 grid(["Scenario", "Yr1-10 growth", "Fade", "TGR", "IV/share", "×0.80 (0.70 no-moat)"], 3,
      [0.95, 1.35, 0.8, 0.6, 1.3, 1.6]),
 P("Sensitivity — thesis must hold across the majority of the grid [E3-12]", S["h3"]),
 grid(["WACC \\ TGR", "2.0%", "2.5%", "3.0%", "3.5%", "4.0%"], 5,
      [1.35, 1.07, 1.07, 1.07, 1.07, 1.07]),
 SP(1, 6),
 source_class_box("amendment", [
   P("<b>THE SCREAM TEST (P46).</b> Verdict at bare yardstick rate: " + CHECK + " BUY " + CHECK +
     " WAIT   Verdict at Book Two WACC: " + CHECK + " BUY " + CHECK + " WAIT   Agree? " + CHECK +
     " YES — proceed   " + CHECK + " NO — whisper, PASS", S["formline"])]),
 SP(1, 6), gate_result(6, "FAIL — wait for price"), PageBreak()]

# ---------- sheet 8 ----------
el += [P("SHEET 8 — REVERSE DCF | GATE 8", S["h1"]),
 P("The pari-mutuel check [E3-20]: what must the crowd believe for today’s price to be fair?",
   S["small"]),
 lines2("Current price:", "WACC used:"),
 P("Q1 — implied OE base (growth held fixed)", S["h2"]),
 grid(["Benchmark", "Value", "Implied as %", "Verdict"], 3, [1.9, 1.3, 1.5, 2.0]),
 checks("Overall:", ["BELOW TROUGH", "BELOW CURRENT", "AT CURRENT", "ABOVE PEAK — do not enter"]),
 P("Q2 — implied year-1 growth (OE held fixed)", S["h2"]),
 grid(["Decel profile", "Implied yr-1 growth", "vs 5-yr CAGR", "Verdict (A/S/H)"], 4,
      [1.6, 1.7, 1.6, 1.8]),
 P("Asymmetry ratio (convention P44)", S["h2"]),
 P("Upside (Base IV − price): ________   Downside (price − Bear IV): ________   "
   "Ratio: ______ : 1    " + CHECK + " >3:1  " + CHECK + " 2–3:1  " + CHECK + " <2:1 — wait",
   S["formline"]),
 SP(1, 6), gate_result(8, "FAIL — wait"), PageBreak()]

# ---------- sheet 9 ----------
el += [P("SHEET 9 — QUARTERLY MONITORING | GATE 7", S["h1"]),
 P("“Charlie and I let our marketable equities tell us by their operating results — not by their "
   "daily, or even yearly, price quotations — whether our investments are successful.” [E2-13]",
   S["small"]),
 lines2("Company / ticker:", "Quarter / date:"),
 lines2("Avg cost:", "Current price:"),
 P("Thesis-confirming metric", S["h2"]),
 lines2("Prior value:", "This quarter:"),
 checks("Direction:", ["IMPROVING", "FLAT", "DETERIORATING"]),
 P("Thesis-breaking metric", S["h2"]),
 lines2("This quarter:", "Consecutive qtrs deteriorating:"),
 checks("EXIT TRIGGERED (2 consecutive)?", ["YES — EXIT", "NO — HOLD"]),
 P("Integrity check (OM-12)", S["h2"]),
 checks("Previously disclosed metric now omitted?", ["Y", "N"]),
 checks("New SEC correspondence / restatement?", ["Y", "N"]),
 checks("Status:", ["INTACT", "YELLOW FLAG", "DISQUALIFIED — EXIT"]),
 P("Owner earnings + range anchoring (P47)", S["h2"]),
 lines2("Trailing OE:", "vs DCF base (Δ%):"),
 checks("OE moved >10% vs base (convention)?", ["YES — rerun Gates 4–6", "NO"]),
 checks("New filing raises lowest VERIFIED tier?", ["YES — raise thresholds", "NO"]),
 P("Sell decision tree", S["h2"]),
 checks("Price > 120% of conservative IV (OM-14 + convention)?", ["YES — REDUCE", "NO"]),
 checks("Quarterly decision:", ["HOLD", "ADD", "REDUCE", "EXIT", "RERUN"]),
 SP(1, 4),
 callout([P("“Inactivity strikes us as intelligent behavior.” [E3-15] — the default action is no "
            "action.", S["cardbody"])]), PageBreak()]

# ---------- sheet 10 ----------
el += [P("SHEET 10 — POSITION LOG, WATCHLIST, ELIMINATED REGISTER", S["h1"]),
 P("Transaction log (print yearly)", S["h2"]),
 grid(["Date", "Ticker", "Buy/Sell", "Shares", "Price", "Total", "Account"], 8,
      [0.95, 0.85, 0.85, 0.8, 0.9, 1.05, 1.3]),
 P("Current holdings", S["h2"]),
 grid(["Ticker", "Shares", "Avg cost", "Price", "Base IV", "MOS %", "Reviewed"], 5,
      [0.85, 0.85, 0.95, 0.9, 0.95, 0.85, 1.35]),
 P("Watchlist (passed Gates 1–5; waiting for price)", S["h2"]),
 grid(["Ticker", "Statute hurdle", "Book Two max buy", "Current", "Gap %", "Next catalyst"], 4,
      [0.85, 1.25, 1.4, 0.9, 0.75, 1.55]),
 P("Eliminated (failed a gate — no revisits without new primary evidence; integrity failures are "
   "permanent)", S["h2"]),
 grid(["Ticker", "Gate failed", "Primary reason", "Date"], 5, [0.9, 1.0, 3.4, 1.4]),
 SP(1, 10),
 P("OM-15 self-benchmark: portfolio result vs index, 3-year minimum window [E1-03] — "
   "“Otherwise, why do our investors need us?”", S["small"]),
 SP(1, 10), P(f"“{MOTTO}”", S["epigraph"]),
 P("The Analysis Workbook — v3.0 — July 2026", S["epigraphsrc"])]

doc = NumberedDoc(os.path.abspath(OUT), "The Analysis Workbook")
doc.build(el)
print("built:", os.path.abspath(OUT))
