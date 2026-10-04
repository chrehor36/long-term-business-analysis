# Framework v3.0 Test Run — Sony, Table Trac, Nintendo
**Analysis date: 2026-07-14** · Documents used: *The Analysis Workbook v3.0* (sheet flow),
*Framework v3.0* (rules), *Principles v3.0* (citations). Personal-study exercise, not advice.

**Scope of this test:** a condensed pass to exercise the machinery on live data. Owner
earnings uses **net income as first proxy** (full Sheet 5 requires the maintenance-capex +
working-capital split from each filing — flagged below where it matters). 8-quarter moat
metrics and full inversion sourcing are marked TODO where not pulled.

---

## STEP 0 — RATE REFRESH (applies to all three)

| Input | Value | Source date |
|---|---|---|
| US 30-yr Treasury | **5.10%** | 5.06–5.11% range, Jul 10–13, 2026 |
| Japan 30-yr JGB (earnings-currency anchor for SONY/NTDOY) | **3.93%** | Jul 10, 2026 |
| USD/JPY | **162.4** | Jul 13, 2026 |

⚠ JGB 30-yr is **+89bp year-over-year** — far beyond the 50bp trigger. Any existing
yen-denominated valuations are stale and must be recomputed (which this run does).

---

## 1) SONY GROUP (NYSE: SONY, ADR $20.85 · mkt cap ≈ $122.4B ≈ ¥19.9T)

**Data (FY ended 2026-03-31, continuing ops after the Oct 2025 Financial Services spin-off):**
revenue ¥12,479.6B (+3.7%) · operating income ¥1,447.5B (+13.4%) · net income ¥1,030.9B
(−3.4% vs restated prior) · ¥500B buyback announced.

- **Gate 1 (Circle):** CONDITIONAL. The financial spin-off removed the hardest-to-model
  segment, but Sony is still five businesses (Games, Music, Pictures, Sensors, ET&S).
  Per OM-5 each requires independent evaluation — the workbook's segment sheets are
  mandatory, and a real pass demands genuine familiarity with at least Games/Music/Sensors
  unit economics. "I don't know" remains available.
- **Gate 2 (Moat, franchise test [E3-03]):** Games — switching costs + network scale
  (PSN installed base, digital libraries); Music — catalog royalties, the classic
  economic-goodwill asset [E2-04]; Sensors — scale/process cost advantage but
  capital-hungry. Franchise-test pricing-power evidence strongest in Music/Games.
  Direction: TODO 8-quarter metrics (PSN MAU, music streaming revenue, sensor share).
- **Gate 3 (Management):** buyback behavior consistent with the two-condition test
  [E5-01] *only if* price < conservative IV — see Gate 6 tension below. Spin-off itself
  is OM-3-friendly (per-share focus). No integrity flags found in this pass.
- **Gate 4 (OE):** NI proxy ¥1,031B. **Flag:** Sensors capex typically runs near or above
  segment D&A (fab expansion = growth capex, but the maintenance share is material);
  content amortization in Pictures/Music needs the Sheet 5 split. True OE likely
  ¥0.85–1.0T. TODO before any full-size decision.
- **Gate 6-B — Statute (Sheet 7-B):** OE-proxy yield = 1,031 / 19,874 = **5.2%** vs JGB
  hurdle 3.93% (+0 large-cap) → **PASSES Book One** with ~1.3pp cushion (survives even
  the low end of the OE-adjustment range: 850/19,874 = 4.3%).
- **Book Two (JPY build-up: 3.93% + 5.5% ERP + 0.5% ≈ 9.9%):** crude perpetuity at g=3%:
  ¥1,031B/0.069 ≈ ¥14.9T < ¥19.9T market — **fails 20% MOS decisively.**
- **SCREAM TEST: verdicts disagree (Statute yes, Book Two no) → WHISPER.**

**VERDICT: WATCHLIST.** Statute-eligible at fair, nowhere near wonderful-at-cheap. Book
Two 20%-MOS entry needs roughly ¥11.9T market cap (≈ $73B ≈ ADR ~$12.5) on the NI proxy
— complete Sheet 5 OE work first; the real number moves this materially.

---

## 2) TABLE TRAC (OTC: TBTC, ~$4.48 · mkt cap ≈ $20.8M · 4.64M shares) ⚠ price data June 2026 — refresh quote before acting

**Data (FY2025 10-K):** revenue $11.05M (−1.0%) · net income $1.63M (EPS $0.35) · cash
$8.24M, **zero debt** · maintenance revenue $6.15M = 55.7% of sales · gross margin 73.7% ·
dividends $0.08 regular + $0.10 special.

- **Gate 1:** PASS-able. One segment, understandable product (casino management systems
  for small/tribal/cruise operators), filings small enough to read completely.
- **Gate 2 (franchise test):** Switching costs are real — accounting/compliance systems
  embedded in regulated casino operations. But: revenue FLAT (−1%), so direction is
  **STABLE, not WIDENING** [E4-02 standard]; and giant competitors (Konami, IGT,
  Light & Wonder, Aristocrat) own the mid/large-casino tier. Maintenance-revenue share
  rising + 73.7% GM = genuine pricing-power evidence in its niche. NARROW at best.
- **Gate 3:** founder-led, dividend-paying, debt-free, special dividends over empire
  building — OM-2/OM-8 friendly posture. TODO: proxy read for comp structure/options.
- **Gate 4 (OE):** asset-light; NI ≈ OE is a fair first proxy. Fortress balance sheet:
  cash = 40% of market cap; survives the 50%×2yr drill trivially.
- **Gate 5 (mandatory inversions):** key-person (founder-engineer) — **[U]** until
  succession is addressed on the record; customer concentration — TODO from 10-K;
  technology shift (cashless/mobile gaming) — partially addressed via product upgrades.
  An unanswered mandatory inversion requires written justification to proceed.
- **Gate 6-B — Statute:** OE yield = 1.63 / 20.75 = **7.9%** vs hurdle 5.10% + **2.0%
  (micro/illiquid)** = 7.10% → **PASSES Book One** with 0.8pp cushion. (Ex-cash: OE/EV =
  1.63/12.5 = 13.0% — noted, but the Statute tests the price you actually pay.)
- **Book Two (12.6% WACC):** perpetuity at g=2%: 1.63/0.106 ≈ $15.4M + $8.2M cash ≈
  $23.6M vs $20.8M → only ~14% upside — **20% MOS not met.**
- **SCREAM TEST:** Statute yes, Book Two no → **WHISPER.**

**VERDICT: STARTER SIZE PERMITTED (Statute), FULL SIZE NOT AVAILABLE.** The dual-book
regime working as designed: wonderful-at-fair yes, wonderful-at-cheap no. Illiquidity
sizing cap applies regardless (Gate 7). Entry for full size needs ≈ $16.5M market cap
(~$3.55/sh) or a verified OE step-up. Resolve the [U] key-person inversion first.

---

## 3) NINTENDO (OTC: NTDOY $10.97 · mkt cap ≈ $50.8–56.3B → ≈ ¥8.25–9.15T; using ¥8.4T)

**Data (FY ended 2026-03-31 — Switch 2 launch year):** sales ¥2,313B (+98.6%) · operating
income ¥360.1B · net income ¥424.1B (+52.1%) · Switch 2: 19.86M units yr-1 · guidance
FY3/27: sales ¥2,500B, NI ¥310B. Stock −48% off its 52-week high ($24.92 → $10.97).

- **Gate 1:** PASS-able. One business, readable economics — but requires accepting
  console-cycle lumpiness as the unit of analysis.
- **Gate 2 (franchise test):** IP portfolio (Mario/Zelda/Pokémon co-ownership) = the
  no-close-substitute condition in its purest form; pricing power proven (first-party
  software margins, hardware sold profitably unlike competitors). Cycle risk is the
  moat-durability question: the moat is the IP, not any console [E4-04's
  no-continuous-rebuild criterion cuts BOTH ways here — hardware must be rebuilt each
  cycle; the IP does not].
- **Gate 4 (OE + RANGE ANCHORING, P47):** verified tiers: FY3/26 NI ¥424B (launch-year,
  includes non-operating FX/interest income — OI was only ¥360B); **FY3/25 NI ¥278.8B =
  the lowest recent VERIFIED tier** (pre-launch trough). The field amendment exists for
  exactly this cyclical shape: buy prices anchor to ¥278.8B, not the launch-year number.
  Note guidance itself (¥310B) sits near the anchor, corroborating it.
- **Gate 6-B — Statute (anchored tier):** 278.8 / 8,400 = **3.3%** vs 3.93% hurdle →
  **FAILS Book One on the anchor** (current-year tier would pass at 5.0% — the amendment
  forbids using it). Anchored pass requires ≈ ¥7.1T market cap ≈ $43.7B ≈ **NTDOY ~$9.30**
  (~15% below current).
- **Book Two:** not reached (Statute failed on anchor) — Gate 6 stops the analysis for
  entry purposes.

**VERDICT: WATCHLIST with a computed trigger.** The −48% drawdown has carried it *near*
Statute range but not into it on anchored earnings. Watch: NTDOY ≈ $9.30 (or a published
filing that raises the verified floor above ¥278.8B — e.g., FY3/27 actuals ≥ guidance).
Cash-rich balance sheet (historically ¥2T+ net cash) means an EV-adjusted view would be
considerably more generous — a legitimate Sheet 5 refinement before the next pass.

---

## Test-run observations (framework mechanics)

1. **The dual-book regime discriminated all three cases differently** — Sony (fair, not
   cheap), TBTC (starter permitted, full blocked), Nintendo (anchor-blocked with a price
   trigger). No verdict required judgment overrides.
2. **Range anchoring earned its keep on Nintendo** — without it, launch-year earnings
   would have shown a comfortable Statute pass at exactly the wrong point in the cycle.
3. **The Scream Test rejected both marginal cases** (Sony, TBTC full-size) — behaving as
   the whisper-filter it was designed to be.
4. **Honest TODOs for a real (non-test) run:** Sheet 5 maintenance-capex/WC splits from
   the 20-F/10-K; 8-quarter moat metrics; Gate 5 sourcing from transcripts; TBTC current
   quote; Nintendo net-cash adjustment.

---

## ADDENDUM (same date) — Book Two intrinsic values and MOS entry prices

Full Sheet 7 mechanics (10-yr explicit, moat-class fade, TV at TGR<WACC), OE bases and
WACCs as above; per-ADR figures scaled from market cap (ADR-ratio-proof). NI-as-OE proxy
caveats apply; Nintendo uses the anchored tier (P47) + ¥2.0T net-cash estimate (verify).

| | Bear IV | **Base IV** | Bull IV | Current | **Max buy (IV×0.80)** | Statute price (Book One) |
|---|---|---|---|---|---|---|
| **SONY** | $12.87 | **$16.82** | $19.53 | $20.85 | **$13.46** | $27.52 |
| **SONY (conserv. OE ¥900B)** | $11.23 | **$14.69** | $17.05 | $20.85 | **$11.75** | — |
| **TBTC** | $4.79 | **$5.33** | $6.02 | $4.48 | **$4.27** | $4.96 |
| **NTDOY** | $6.94 | **$8.28** | $9.49 | $10.97 | **$6.62** | $9.26 |

Readings:
- **SONY**: price ABOVE Base IV on both OE readings — no MOS exists at $20.85. Statute
  ($27.52) permits starter size at fair; Book Two full-size entry waits for ~$13.50
  (or ~$11.75 on conservative OE). Scream-test whisper confirmed numerically.
- **TBTC**: the interesting one. Price sits BELOW Bear IV ($4.48 < $4.79) — the cash
  pile floors the downside; model asymmetry is effectively unbounded. But MOS available
  is 16.0% vs the 20% floor: max buy $4.27, price $4.48 → **WAIT (gap ~5%)**. Statute
  already satisfied ($4.96 ceiling) → starter size permitted now, full size at ≤$4.27.
- **NTDOY**: price above Base IV even crediting ¥2T net cash. Anchored full-size entry
  $6.62; Statute starter trigger $9.26. Both below market — **WATCHLIST stands**. A
  published FY3/27 result ≥ guidance (¥310B) would lift the anchor ~11% and move both
  triggers up accordingly.

---

## ADDENDUM 2 — FULL OWNER EARNINGS (Sheet 5 done properly)

The first pass used NI as OE proxy. Filing data now pulled; OE = NI + D&A − maintenance
capex − required WC increment [E2-08], maintenance bands per convention P44 where the
split is undisclosed.

**SONY (FY3/26 continuing ops):** NI ¥1,031B + D&A ¥664.6B − maint capex (50–70% of
~¥600B/yr, from the ¥1.8T three-year budget) − WC ≈ 0 (OCF ¥1,945.6B corroborates)
→ **OE band ¥1,175–1,396B, mid ¥1,285B.** The NI proxy was TOO HARSH: continuing-ops
D&A exceeds capex. Caveat: if the D&A line excludes content amortization, content
spend/amortization roughly offset at steady state — 20-F check remains open.

**TBTC (FY2025):** OCF $1.81M − maint capex ~$0.1M → **OE ≈ $1.7M.** Correction to pass
one: the cash jump to $8.24M was maturing CDs reclassified, not a WC release. New datum
for Gate 5: one customer = 19.2% of revenue and 34.7% of receivables — the customer-
concentration inversion is now DOCUMENTED, scores [P] at best.

**NTDOY (anchored tier FY3/25):** NI ¥278.8B + D&A ¥12.1B − maint capex (¥35–72B; FY3/25
capex ¥287.9B was launch-inflated growth spend; asset-light band applied) → **OE band
¥219–256B, mid ¥237B.** The NI proxy FLATTERED Nintendo — tiny D&A gives no add-back
while real maintenance capex still subtracts.

### Corrected table (Base scenario, mid-band OE)

| | Full-OE Base IV/sh | Current | Max buy (×0.80) | Statute price | Verdict |
|---|---|---|---|---|---|
| **SONY** | **$20.97** (band 19.17–22.78) | $20.85 | **$16.78** | $34.30 | Price ≈ IV. Statute starter available; full size at ~$16.78. Scream: whisper (unchanged). |
| **TBTC** | **$5.49** (5.27–5.71) | $4.48 | **$4.39** | $5.17 | Gap to full-size entry now ~2%. Starter permitted; resolve [U] key-person + refresh quote. |
| **NTDOY** | **$7.43** (7.06–7.81) | $10.97 | **$5.94** | $7.88 | Anchored Statute trigger DROPS to $7.88 (was $9.26 on proxy). Watchlist; floor rises on FY3/27 filing. |

**Lesson recorded:** the proxy erred in BOTH directions — 25% too low on Sony, 15% too
generous on Nintendo. Gate 4's insistence on the full formula [E2-08] is not pedantry;
it is where the verdicts moved.
