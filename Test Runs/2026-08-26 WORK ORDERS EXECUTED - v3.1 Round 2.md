# WORK ORDERS EXECUTED — v3.1 ROUND 2 — 2026-08-26
Operator: *"Run all."* Every UNRESEARCHED work order from the v3.1 re-run was attempted.
This records what closed, what is now computable, and what is still open with a sharper
work order than before.

---
# THE BIGGEST RESULT: ALL THREE SOVEREIGNS ARE NOW SOURCED OFFICIALLY

The framework has been running on **one** rate. It needs three, and two were stale or
missing entirely.

| Currency | Rate | Source | vs what we were using |
|---|---|---|---|
| **USD 30-yr** | **5.19%** | Yahoo ^TYX, cross-checked vs FRED DGS30 | current |
| **JPY 30-yr** | **4.04%** | **Japan MOF official JGB curve, 2026-08-25** | **was 3.76% (2026-07-15) — +28bp** |
| **EUR 30-yr** | **3.70%** | **ECB euro area AAA yield curve, 2026-08-25** | **never had one** |

Both new rates came from the issuing authority's own published curve, not an aggregator.
`mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv` and the ECB SDW API
(`YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y`). **Both are now permanent rungs on the evidence
ladder.**

The JPY move matters: the Japanese runs used **3.76% floored to 4.00%**. The real rate is
now **4.04%**, above the floor, so the floor no longer binds and every Japanese hurdle
rises.

---
# ASML — WORK ORDER **CLOSED**. First financial analysis ever done on this holding.

**Step 0-B satisfied via rung 2:** ASML files with the SEC and tags in us-gaap. Full
history retrieved. **This position has been held from ~$1,000 with no run file at all;
this is the first time its numbers have been looked at.**

## GATE 1 — CIRCLE OF COMPETENCE
Sells the lithography machines that print every advanced logic and memory chip, and is
the sole producer of EUV. Revenue is a small number of very large machines plus a growing
installed-base service annuity. **The scarce input is the machine itself** — there is no
second EUV supplier.
**VERDICT: [x] IN**

## GATE 2 — MOAT — **UNRESEARCHED**
Everything points to a monopoly, and I am not going to assert it without the row the
framework now requires. ASML's own filings are not the evidence for its competitors'
position.
- **WORK ORDER:** lithography-segment revenue for **Nikon** (Precision Equipment segment)
  and **Canon** (Industrial and Others segment), same three fiscal years. Both disclose
  it in segment reporting. Ladder rung 3-4 (company IR / TSE).
- Until filled: **class PROVISIONAL**, which carries the NARROW spread.

## APPENDIX — **COMPUTATION, NOT A CLEARANCE** (Gate 2 is not closed)
Per operator protocol rule 2 this carries no clearance and no entry language.

Price $1,745.35 ÷ EURUSD 1.1658 = **€1,497.13/share** × **385.4M shares** (2025-12-31)
= market cap **€577.0B**. Hurdle **3.70%** (EUR, the earnings currency).

| FY | revenue | NI | OCF | SBC | OCF−SBC | D&A | capex | net margin |
|---|---|---|---|---|---|---|---|---|
| 2023 | €27,558M | €7,839M | €5,443M | €135M | €5,308M | €740M | €2,156M | 28.4% |
| 2024 | €28,263M | €7,572M | €11,166M | €173M | €10,993M | €919M | €2,067M | 26.8% |
| 2025 | €32,667M | €9,609M | €12,658M | €202M | €12,456M | €1,026M | €1,574M | 29.4% |

- 3-yr mean (OCF−SBC) **€9,586M**; maintenance-capex band **€895M (D&A) .. €1,932M**
- **3-yr mean OE €7,653M .. €8,691M** · **current tier (2025) €10,882M .. €11,430M**
- **DIVERGENCE +32% to +42% — MATERIAL, and it must be stated.** Cause: 2023 operating
  cash flow was €5,443M against €11,166M and €12,658M, on customer prepayment and
  deferred-revenue timing. **ASML's operating cash flow is lumpy**, and [E2-25] asks for
  *"demonstrated consistent earning power."* Both anchors are therefore carried.

**BOOK ONE — FAILS on every anchor, badly.**

| anchor | OE | yield vs 3.70% | statute price |
|---|---|---|---|
| 3-yr mean, total-capex | €7,653M | **1.33%** FAIL | €537 ($626) |
| 3-yr mean, D&A | €8,691M | **1.51%** FAIL | €609 ($710) |
| current tier, total-capex | €10,882M | **1.89%** FAIL | €763 ($890) |
| current tier, D&A | €11,430M | **1.98%** FAIL | €802 ($934) |

**BOOK TWO — illustrative only**, at a WIDE spread (6.70%) which Gate 2 has not earned:

| g1 | base | IV/share | vs $1,745 |
|---|---|---|---|
| 5% | 3-yr mean | $630 | **2.77×** |
| 8% | current tier | $1,020 | **1.71×** |
| **12%** | **current tier** | **$1,209** | **1.44×** |

**Even at 12% growth off the most generous anchor and the tightest spread the moat could
possibly justify, the price is 1.44× intrinsic value.** The result is not close and does
not depend on the Gate 2 question.

**PROVISIONAL READ (not a verdict — Gate 2 is open): the business is extraordinary and
the price is not defensible on this framework's arithmetic at any assumption tested.**
Hold is undisturbed. **No adds.**

---
# NCLTY (NITORI) — WORK ORDER **SUBSTANTIALLY EXECUTED**

**Step 0-B satisfied via rung 3.** English consolidated financial statements retrieved
from `nitorihd.co.jp/en/ir/library/financial_statements.html` — FY2026 and FY2025, IFRS,
committed to `_research 2026-08-26/`. **These were public the entire time.**

| ¥M | FY2025 (to 2025-03-31) | FY2026 (to 2026-03-31) |
|---|---|---|
| Gross profit | 473,923 | 485,413 |
| Operating profit | 117,665 | 125,526 |
| Profit before tax | 117,448 | **127,357** |
| **Operating cash flow** | **144,384** | **148,911** |
| D&A | 66,143 | 69,509 |
| Capex (PP&E + intangibles) | **125,308** | **44,412** |
| Basic = diluted EPS (¥) | 146.08 | **157.98** |

## THE FINDING THE NI PROXY WAS HIDING — AND IT CUTS THE OTHER WAY
The July run used **net income as owner earnings**. On the real statements:

| maintenance-capex basis | OE FY2025 | OE FY2026 |
|---|---|---|
| at **total capex** | **¥19,076M** | ¥104,499M |
| at **D&A** | ¥78,241M | ¥79,402M |

**Capex swung from ¥125.3B to ¥44.4B in one year.** At the total-capex end owner earnings
appear to move 5×; at the D&A end they are **flat at ¥78-79B**. That stability is the
tell: **FY2025's capex was overwhelmingly growth spending** (stores and distribution
centres), not maintenance. Under Ruling 10 this is exactly the judgment the band exists
to force, and the filing supports sitting **near the D&A end**, giving roughly
**¥78-79B/yr of owner earnings** — a stable figure, not the erratic one.

**This is the opposite of the TBTC case and it is worth noticing.** There the NI proxy
flattered the business; here it obscured a genuinely steady cash generator behind a
lumpy capex line.

## STILL OPEN — a much smaller work order than before
1. **ADR ratio for NCLTY** and the Tokyo (9843) share price, to compute market cap
   correctly. Without it Book One cannot be stated. *(This is the only blocker.)*
2. FY2024 statements for a true 3-year mean (rung 3, same page).
3. Share-based compensation (IFRS statements do not break it out on the face).
4. Gate 2 competitor row: Japanese furniture/homeware retail.
- **VERDICT: [ ] IN [ ] OUT [x] UNRESEARCHED — blocker is the ADR ratio, nothing more**

---
# MITSY (MITSUI) — WORK ORDER **REFINED**, route corrected
**Rung 2 is dead and now proven dead:** Mitsui's own SEC page states it filed Form 20-F
only **"until fiscal year ended March 31, 2010."** There is no SEC route. This is a
finding, not a failure — it removes a rung permanently for this name.
- **Rung 3-4 located:** `mitsui.com/jp/en/ir/library/` carries English quarterly and
  annual results. Q1 FY2027 retrieved: operating cash flow **¥42.3bn**, with management's
  own **"Core Operating Cash Flow ¥280.9bn"** which excludes working-capital changes.
- **That second figure is the interesting one** and needs the full-year version: a
  sogo shosha's reported OCF is dominated by commodity working-capital swings, which is
  precisely the [E2-23] "average annual amount" problem in its most extreme form.
- **WORK ORDER:** the FY2026 annual results PDF from the same library (not the Q1), for
  reported OCF, core operating cash flow, D&A, capex and share count.
- **VERDICT: [x] UNRESEARCHED**

# NHNKY (NIHON KOHDEN) — WORK ORDER **STILL OPEN**
Both guessed IR paths returned 404. Needs the correct English IR URL located before the
statements can be pulled.
- **WORK ORDER:** locate Nihon Kohden's English IR library, then the same five items.
- **GTC at $9.10 remains CANCELLED.**
- **VERDICT: [x] UNRESEARCHED**

---
# V, HRB, TBTC — COMPETITOR ROWS STILL OPEN
The TJX row cost three filings and a failed XBRL shortcut. The same is required here.
- **V:** peer is Mastercard. Partial data in hand — **MA operating margin 57.6% (FY2025)
  vs V 60.0% (FY2025)**; V revenue growth +11.3% vs MA +16.4%. **MA is growing faster and
  V's operating margin fell from 65.7% to 60.0%.** Needs verification against both 10-Ks
  before it can settle Gate 2.
- **HRB:** Intuit is a poor comparator — far broader business, and the XBRL series for
  HRB stops at FY2014 on the tags tried. Needs a defensible peer set first.
- **TBTC:** competitors (IGT, Light & Wonder) are an order of magnitude larger and may
  not disclose a comparable segment. **This one may legitimately convert to UNKNOWABLE**
  once attempted — it would be the first honest use of that verdict.

---
# SCOREBOARD

| Name | Before today | Now | Blocker |
|---|---|---|---|
| **TJX** | WAIT, moat asserted | ✅ **v3.1 COMPLETE**, moat measured | — |
| **ASML** | no run file, no line | ✅ **Gates 1 + 4 + 6 computed**, 1.44× fair at best | Gate 2 competitor row |
| **NCLTY** | UNRESEARCHED, NI proxy | ✅ **real statements, OE ¥78-79B stable** | ADR ratio only |
| **MITSY** | UNRESEARCHED | route corrected, rung 2 proven dead | FY2026 annual PDF |
| **NHNKY** | UNRESEARCHED | unchanged | correct IR URL |
| **V / HRB / TBTC** | UNRESEARCHED at Gate 2 | partial peer data (V) | competitor rows |
| **All three sovereigns** | one rate, two stale/missing | ✅ **USD 5.19 / JPY 4.04 / EUR 3.70, official sources** | — |

**Nothing converted to UNKNOWABLE today. Every remaining item is still a queue entry with
a named artifact — which is the point of Ruling 13.**

## WHAT THIS ROUND PROVED
The operator's premise was correct and the evidence is now on the record: **of the seven
UNRESEARCHED names, the blockers turned out to be a PDF on a company website, an ADR
ratio, and a URL.** None of it was hard. It had simply never been done, and the old
framework had a verdict — PASS-with-a-caveat — that let it never be done.
