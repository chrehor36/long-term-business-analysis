# Company Run — NITORI HOLDINGS (NCLTY / 9843.T) — 2026-08-26
**Framework v3.1.** Supersedes the 2026-07-15 run, which was reclassified UNRESEARCHED
under Ruling 12 and is now **resolved**: every figure below comes from Nitori's own
audited IFRS statements, retrieved from its English IR site. **The July run used net
income as an owner-earnings proxy and a JPY rate that was both stale and floored.**

## STEP 0 — RATE REFRESH
- **JPY 30-yr sovereign: 4.04%** (2026-08-25, **Japan MOF official JGB curve**,
  `mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv`)
- vs the 3.76% used on 2026-07-15: **+28bp**. **The 4.00% floor no longer binds** — the
  real rate is now above it, so the hurdle is the rate itself.
- FX: **USDJPY 159.179** · **ADR ratio 0.5 ordinary shares per ADR**, derived from live
  prices: $9.47 ÷ (¥3,030 / 159.179) = 0.498 ≈ 0.5

## STEP 0-B — THE FILING WAS READ ✅ (rung 3)
- [x] consolidated statement of cash flows incl. detail lines [x] income statement
      [x] EPS note
- **Consolidated Financial Statements FY2026 (year to 2026-03-31) and FY2025**, IFRS,
  from `nitorihd.co.jp/en/ir/library/financial_statements.html`. Both PDFs committed to
  `_research 2026-08-26/`.
- **These were public in English the entire time.**

## GATE 1 — CIRCLE OF COMPETENCE
Vertically integrated furniture and homeware: designs, manufactures (largely in its own
and contracted Asian plants), imports and retails its own product. **The scarce input is
the integrated cost position** — it captures manufacturer, importer and retailer margin
on one item. Gross margin 53.9% (¥485,413M on revenue) is a manufacturer's margin earned
at retail, which is the whole thesis in one number.
**VERDICT: [x] IN**

## GATE 2 — MOAT — **UNRESEARCHED**
The vertical-integration cost advantage is plausible and the gross margin supports it,
but Ruling 11 requires the comparison and I do not have it.
- **WORK ORDER:** gross margin and operating margin for **Ryohin Keikaku (7453.T, MUJI)**
  and **IKEA Japan** (private — may force PROVISIONAL), same window, from their own
  filings. Rung 3-4.
- Until filled: **class PROVISIONAL**, carrying the NARROW spread (+4.5%).
- **VERDICT: [ ] IN [ ] OUT [x] UNRESEARCHED [ ] UNKNOWABLE**

## GATE 3 — MANAGEMENT
Carried from the banked run: succession precedent real, roles verified clean pre-entry.
- **Half-owner test:** the IFRS statements are complete and legible in English with note
  references throughout. **Passes on form.** One gap: **share-based compensation is not
  broken out on the face of the cash flow statement**, so it could not be subtracted from
  owner earnings below. Recorded as a limitation, and it makes the OE figures slightly
  generous.
- **VERDICT: [x] IN** (carried; not re-tested this run)

## GATE 4 — FINANCIAL QUALITY ✅ **RESOLVED — this is what the NI proxy was hiding**

| ¥M | FY2025 (to 2025-03-31) | FY2026 (to 2026-03-31) |
|---|---|---|
| Revenue gross profit | 473,923 | 485,413 |
| Operating profit | 117,665 | 125,526 |
| Profit before tax | 117,448 | 127,357 |
| **Profit attributable to owners** | 82,546 | **89,270** |
| EPS (basic = diluted, ¥) | 146.08 | **157.98** |
| **Operating cash flow** | **144,384** | **148,911** |
| D&A | 66,143 | 69,509 |
| Capex (PP&E + intangibles) | **125,308** | **44,412** |

**Shares: 565.1M** (¥89,270M ÷ ¥157.98). **Market cap ¥1,712.2B = $10.76B.**

### Owner earnings, and the maintenance-capex judgment (Ruling 10)
| basis | FY2025 | FY2026 | 2-yr mean |
|---|---|---|---|
| at **total capex** | **¥19,076M** | ¥104,499M | ¥61,788M |
| at **D&A** | ¥78,241M | ¥79,402M | **¥78,822M** |

**Capex swung from ¥125.3B to ¥44.4B in a single year.** At the total-capex end owner
earnings appear to move **5×**; at the D&A end they are **flat within 1.5%**.

**DISCLOSED JUDGMENT: sit near the D&A end.** The filing-cited reason is that stability
itself — a business whose true maintenance requirement moved 5× in one year while
revenue and margins barely moved is not what happened. **FY2025's capex was growth
spending** (stores and distribution capacity). This is precisely the call Buffett says
"must be a guess," and it is disclosed rather than buried.

**Owner earnings ≈ ¥78-79B/yr, and stable.** *(Generous by the unsubtracted SBC.)*

### Stress test — company-specific, quantified, with a probability
- **Mechanism:** the vertical-integration advantage is a **yen-cost** advantage. Nitori
  manufactures in Asia and sells in Japan, so a sharply weaker yen raises landed cost
  faster than it can reprice at retail. **This is the one real threat and it is
  macro, not competitive.**
- **Quantified:** gross margin is 53.9%. A 500bp gross-margin compression on FY2026
  revenue costs roughly **¥45B of operating profit**, taking operating profit from
  ¥125.5B to ~¥80B and owner earnings to roughly **¥45-50B**. Still positive, still
  covering maintenance capex.
- **Probability: [x] a real possibility** — the yen has already moved to 159/USD.
- **VERDICT: [x] IN**

## GATE 5 — INVERSION (carried, with probabilities added)
| Inversion | Score | Probability |
|---|---|---|
| Moat destruction | [P] | a low-level possibility |
| Management failure | [DS] | a low-level possibility |
| Balance sheet | [DS] | a low-level possibility |
| Thesis-breaking metric | [D] | — |
| **Yen-cost compression** | **[P]** | **a real possibility** |
- Thesis-breaking metric: **gross margin below 50% for two consecutive halves.**
  Currently 53.9%.
- **VERDICT: [x] IN**

---
⛔ VALUATION LOCK — Gate 2 is UNRESEARCHED, so what follows is
**COMPUTATION, NOT A CLEARANCE** (operator protocol rule 2). No entry language.
---

## GATE 6 — PRICE (computation)

### BOOK ONE — hurdle 4.04%
| anchor | OE | yield | verdict | statute price (ADR) |
|---|---|---|---|---|
| 2-yr mean @ total capex | ¥61,788M | **3.61%** | FAIL | $8.50 |
| **2-yr mean @ D&A** | **¥78,822M** | **4.60%** | **PASS** | **$10.85** |
| current tier @ D&A | ¥79,402M | 4.64% | PASS | $10.93 |
| current tier @ total capex | ¥104,499M | 6.10% | PASS | $14.38 |

**Passes on three of four anchors, including the disclosed judgment. Statute price ≈
$10.85-10.93 against $9.47 today — Book One passes with roughly 13% of room.**

### BOOK TWO — rate 4.04% + 4.5% (NARROW; moat PROVISIONAL) = **8.54%** · MOS 20%
Observed OE growth **+1.5%**.

| g1 | IV ¥/share | IV per ADR | CHEAP per ADR |
|---|---|---|---|
| 1.5% | ¥2,269 | **$7.13** | $5.70 |
| 3.0% | ¥2,418 | $7.59 | $6.08 |
| 5.0% | ¥2,629 | $8.26 | $6.61 |

**Book Two says the ADR is above fair value at every growth setting.**

### SCREAM TEST — **THE BOOKS DISAGREE → WHISPER → PASS**
- Book One: **PASS** (4.60% vs 4.04%)
- Book Two: **FAIL** ($9.47 vs a $7.13-8.26 fair range)
- **→ WHISPER.** The framework's standing rule is to classify as whisper and pass rather
  than pick the book that says what you want to hear.

### TWO VERDICTS
- **BUSINESS: good, and better documented than it has ever been.** Owner earnings are a
  stable ¥78-79B, gross margin 53.9%, cash generation real rather than a net-income
  assertion. Moat unproven for want of a competitor row.
- **PRICE: fair-to-full, not cheap.** Below the Statute line, above the Book Two range.

### **VERDICT: [ ] BUY-ELIGIBLE [ ] STATUTE-ONLY [x] WAIT (whisper) [ ] UNRESEARCHED-close**
**Position held at a ¥ basis equivalent to ~$7.435 is undisturbed and is up ~27%.
NO ADDS.** The July "BUY-ELIGIBLE both books" verdict does not survive.

### WHAT CHANGED, AND WHY
| | 2026-07-15 | 2026-08-26 |
|---|---|---|
| Owner earnings | **NI proxy** ¥545 (units unclear in that run) | **¥78.8B, from the cash flow statement** |
| JPY sovereign | 3.76%, floored to 4.00% | **4.04%, floor no longer binds** |
| Moat spread | **+2.5%** | **+4.5%** (Ruling 4-A, never back-applied; moat now PROVISIONAL) |
| Discount rate | 6.26% | **8.54% (+228bp)** |
| Verdict | **BUY-ELIGIBLE both books** | **WHISPER — WAIT** |

**Almost the entire change is the discount rate**, and almost all of that is Ruling 4-A
having been ratified on 2026-08-01 and never applied to the Japanese names.

## SELF-AUDIT
- [x] Gates returned IN / UNRESEARCHED; none marked IN with an "unverified" caveat
- [x] Step 0-B: audited statements read, source named, committed to `_research`
- [x] Owner earnings from the cash-flow statement, not a proxy; capex band disclosed with
      a filing-cited reason for where it sits
- [x] SBC limitation stated (not broken out; OE therefore slightly generous)
- [x] Stress test specific, quantified, with a probability
- [x] Gate 2 competitor row **outstanding** — work order recorded, class PROVISIONAL
- [x] Sovereign from the issuing authority, dated
- [x] ADR ratio derived and shown, not assumed
- [x] Valuation labelled COMPUTATION — NOT A CLEARANCE, since Gate 2 is open
