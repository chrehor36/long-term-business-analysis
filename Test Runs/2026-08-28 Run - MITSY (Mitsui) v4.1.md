# Company Run — Mitsui & Co., Ltd. (TSE 8031 · ADR MITSY) — 2026-08-28
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this file
and that document disagree, the document governs. Q3 annex:
`Framework/v4/THE MANAGER STANDARD - Q3.md`.

**Position context.** The user HOLDS 8 MITSY ADRs @ $586 (2026-07-16), Roth IRA — the
largest framework position (~$4,950 at $618.72, 2026-08-27, +5.6%). This run therefore
carries a **Q6 HOLD READ under [E2-28] regardless of where the entry sequence stops**,
on the format precedent of `Test Runs/2026-08-28 Q6 HOLD READ - HRB.md`.

**Two method flags, declared up front (both pre-identified in `PORTFOLIO.md`):**
1. The plain OCF−capex convention goes **negative** for FY2026 (capex tripled y/y) and is
   category-wrong here: the capex line contains a one-time ¥723.8bn acquisition of mining
   rights, and the earnings are substantially equity-method associates whose dividends
   understate the economics. Owner earnings are built with the look-through increment
   **[E3-04]** and the spread carried **[E4-25]**. Worked below under a COMPUTATION header.
2. The Q3 weight case is argued from the filing, not from the "trading company" category
   label. Worked inside the hold read (the entry Q3 never opens — see Q2).

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in [E4-15, E3-32]:**
- **JPY 30-year: 4.04% · 2026-08-27 · Japan MOF official JGB curve** (`jgbcme.csv`, via
  `tools/sources.py`). Earnings currency is JPY as presented; the underlying is heavily
  USD/AUD-linked (commodity revenues), which is carried as width, not as a second rate.
- FX (quote vs earnings): ¥159.67/USD (Yahoo aggregate, 2026-08-28 — **aggregator, live
  quote only, flagged**). **ADR ratio, derived: $618.72 × 159.669 ÷ ¥4,979 = 19.84 ≈ 20
  ordinary shares per ADR.** (The 0.8% residual is the one-day close mismatch.)
- Prices: 8031.T ¥4,979 close 2026-08-28; MITSY $618.72 close 2026-08-27 (both Yahoo,
  **aggregator, live quotes only, flagged**).

**The filing was read — not tagged data [E3-27]:**
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- Document: **Annual Securities Report (Yukashoken Hokokusho), 107th fiscal year (FY ended
  2026-03-31), English translation, audited consolidated IFRS statements.** Japanese
  original issued 2026-06-12; English posted to IR 2026-08-12. Local copy:
  `Test Runs/_research 2026-08-26/Mitsui_AnnualSecuritiesReport_FY2026-03_en_107yuho.pdf`
  (324 pp). No EDGAR accession exists — Mitsui is not an SEC filer; this is the EDINET
  filing in the issuer's own English translation (Japanese original prevails).
  `tools/run.py` not usable for the same reason (no SEC XBRL companyfacts); all figures
  below are hand-transcribed from the filed statements.
- **Figure cross-checked against the filed statement:** Core Operating Cash Flow.
  Recomputed from the filed cash-flow statement detail lines: OCF 952,912 − working-capital
  change (−116,844 −72,872 +153,294 +44,831 −20,177 −123,423 = **−135,191**) − lease
  repayments 109,198 = **978,905 Mn JPY**, which equals the segment-note COCF total
  978,905 exactly (Note 6, body p. 239). Second check (work order, 2026-08-28): every
  major JPY line ÷ 160 reproduces the printed USD convenience column.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words.** Mitsui is a capital-allocation engine wearing a
trading coat. Three layers: (1) **equity positions in resource assets** — minority stakes
in Pilbara iron-ore JVs operated by Rio Tinto and BHP (equity share of production 63.8 Mt
in FY2026), oil & gas at 211 kboe/d equity share, LNG projects (ADNOC, Sakhalin II, Oman,
QatarEnergy — dividends ¥69.2bn FY2026), Collahuasi copper — earning the commodity price
minus a low cash cost, mostly through the equity-method line (share of profit ¥447.4bn
FY2026) and dividends (from equity investees ¥367.8bn); (2) **trading and midstream
businesses** across machinery, chemicals, steel, food/healthcare — thousands of margins on
flow plus investee earnings; (3) **the recycling loop**: buy or build positions, harvest,
sell (¥343bn of asset recycling in FY2026), redeploy. Profit for the year attributable to
owners: ¥834.0bn on revenue ¥13,995bn; the filing's own sensitivities make the arithmetic
legible — US$1/t of iron ore = ¥3.0bn of profit, US$1/bbl of oil = ¥0.9bn net.

**The scarce input the business controls:** tier-1 resource deposits and the partner seats
that come with a century of relationships — the filing's own words: "the number of
high-quality undeveloped projects remains limited," and Mitsui just bought 40% of Rhodes
Ridge, "one of the world's largest undeveloped iron ore deposits," for ¥723.8bn.

**Ten years:** the portfolio will have churned — that is the model — but the model itself
(commodity equity positions + trading + recycling) has looked the same for fifty years and
will look the same in ten. The earnings LEVEL is a commodity-price outcome and is not
predictable; the earnings MECHANISM is.

**VERDICT: [x] IN** — with the reservation written: understanding here is understanding of
mechanism and sensitivity, not of the future price deck. That lands at Q4/Q5 as range
width, not here.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

- Needed or desired **[x]** — iron ore, energy, food: yes, elementally.
- No close substitute **[ ] FAILS.** The products are the definition of substitutability:
  one cargo of 62% Fe fines, one LNG cargo, one tonne of naphtha is as good as another.
  The filing prices its own output off world benchmarks — the sensitivity tables (US$1/t,
  US$1/bbl straight to profit) are the company's own statement that it is a **price
  taker** on every major earnings driver.
- Not price-regulated **[x]** — not regulated; just not set by Mitsui either.

**Must the moat be continuously rebuilt? [E4-04]** Yes — literally. Mines deplete; the
filing's asset-retirement note runs mine rehabilitation costs out to 2090, and the year's
defining transaction is ¥723.8bn spent buying the next deposit (Rhodes Ridge) because the
existing ones waste away. *"A moat that must be continuously rebuilt will eventually be no
moat at all."* **Does success depend on a great manager?** Yes — the same sentence of
[E4-04] eliminates it: continuous reallocation of ¥1tn+ of capital a year across seven
segments IS the business. What Mitsui owns that is genuinely scarce — Pilbara cost
position, LNG contract seats — it holds as minority partner in assets **operated by
others** (Rio Tinto, BHP, the LNG operators); the cost moat belongs to the asset, and the
asset's operator, more than to Mitsui.

**Untapped pricing power [E3-33]:** none possible. A price taker cannot raise prices.

**THE COMPETITOR ROW [E3-28]** — same metric (ROE as filed), same window (FY2022–26):

| Company | ROE % FY22→FY26 (5-yr avg) | window | source |
|---|---|---|---|
| **Mitsui & Co.** | 17.98 · 18.89 · 15.29 · 11.93 · 10.22 (**14.9**) | FY2022–26 | 107th Yukashoken Hokokusho, Selected Financial Data, body p. 1 |
| ITOCHU | 21.8 · 17.7 · 15.6 · 15.7 · 14.6 (**17.1**) | FY2022–26 | ITOCHU Financial Information Report 2026 (`FIR2026E.pdf`, itochu.co.jp, June 2026), Summary p. 4 |
| Mitsubishi Corp | — | — | **UNRESEARCHED**: FY2026-03 results PDF (`mitsubishicorp.com/jp/en/ir/library/earnings/pdf/202605e.pdf`) returns 403 to every fetcher tried from this environment |
| Sumitomo / Marubeni / Toyota Tsusho / Sojitz | — | — | **UNRESEARCHED**: each company's FY2026-03 tanshin / integrated report, on their IR sites |

- Peers named: **1 of the industry's ~6** real competitors taken; the row is context, not
  the verdict's load-bearing member. What it shows: Mitsui is not even the best-returning
  house in its own commoditized industry.
- **Class: [x] NONE** (at the product level; the asset-level cost positions are real but
  co-owned and operator-controlled) · Direction: ROE falling four consecutive years from
  the FY23 commodity peak — the return series is the commodity cycle, not a moat.

**VERDICT: [x] OUT.** Not a franchise under [E3-03] — the evidence is the subject's own
filed sensitivity tables, not a missing document. It is "a business" in [E3-43]'s exact
sense: one that can be killed by poor management, whose returns are set by world prices
and its managers' reallocation skill. The moat defect is structural and permanent for
entry purposes. **The entry run stops here. [E5-13]: most names should end here, and that
is the system working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT — the hard sequence closes the
file for any BUY/ADD decision. Everything below exists solely because a position is HELD,
and every valuation figure below is headed per operator rule 3.

---
## Q6 — HOLD READ ON THE EXISTING POSITION **[E2-28]**

> "We are quite content to hold any security indefinitely, **so long as the prospective
> return on equity capital of the underlying business is satisfactory, management is
> competent and honest, and the market does not overvalue the business.**" — [E2-28], 1987

Q2 OUT governs **entry**. It is not on [E2-28]'s list of sell reasons — the corpus holds
businesses it would not buy today. Price appreciation (+5.6%) and holding period are
explicitly rejected as reasons. Three conditions, condition by condition:

### Condition (1) — prospective return on equity capital: **SATISFACTORY, with a live watch item**

ROE as filed: **17.98 → 18.89 → 15.29 → 11.93 → 10.22%** (FY2022–26; 5-yr avg 14.9%),
against a 4.04% JPY sovereign, earned at 2.37× assets/equity and net DER 0.47× — no undue
leverage in [E2-01]'s sense. Core Operating Cash Flow has held ≥ ¥950bn for five straight
years (the filing: "the 1 trillion yen level for the fifth consecutive fiscal year").
Management's own MTMP2029 targets: ROE 12%, profit ¥1.1tn, COCF ¥1.2tn by FY2029.

**The watch item:** ROE has fallen four consecutive years from the FY23 peak. The [E3-30]
question — aberrational cycle or permanent slippage? The fall tracks iron ore and energy
prices off the 2022 super-spike, and 10.2% at the bottom of that slide is still 2.5× the
sovereign. Read today: cycle, not slippage. It carries the first tripwire below.

### Condition (2) — management competent and honest: **NO DISQUALIFIER FOUND**

*(This is the Q3 work the hold test requires, done to the annex's method. It is the
absence of found disqualifiers, not a finding that the managers are honest [E5-17].)*

**The weight case, argued from the filing (method flag 2).** Three determinants:
- **Leverage [E3-29]: MODERATE, not gate-level.** Assets/equity 2.37× (¥20,822bn/¥8,768bn);
  net DER 0.47×; equity ratio 42.1% and rising five years (37.6% → 42.1%); guarantees
  ¥1,147.8bn (13% of equity); no material financial covenants (stated, MD&A p. 80); ratings
  AA (R&I) / A3 / A; current debt maturities ¥557.2bn against ¥982.7bn cash plus $10.3bn
  committed lines. This is not [E3-29]'s 20:1.
- **Daily execution [E3-38]: HIGH.** The filing shows ¥1.97tn of derivative-inclusive
  other financial assets, global trading books in five segments, and a business whose
  entire engine is continuous reallocation. This is a have-to-be-smart-every-day
  business — the retailer end of [E3-38]'s spectrum, not the network-TV end.
- **Control [E1-16]:** no — listed minority position, exit at will.

**One determinant high → for any ENTRY, Q3 would be a BINARY GATE and no price would
compensate for poor management.** For the HOLD read the same standard applies as a
disqualifier scan plus the primary test:

- **Primary test [E2-01]:** the ROE series above — high multi-year earnings rate on
  equity, without undue leverage, balance sheet read first. Passes as a record.
- **The five flags [E4-22, E4-29, E5-15]:**
  - Weak accounting: none found — IFRS as issued by IASB, audited; impairments quantified
    line by line (Mainstream renewables: ¥28.1bn FY26 broken out across three named lines;
    ¥21.4bn FY25).
  - Unintelligible footnotes: no — the equity-method note discloses investee profit, OCI,
    dividends and excess value separately; the sensitivity disclosure is exemplary.
  - Trumpeted projections: **fired as a prompt, read, cleared.** MTMP2029 trumpets profit
    ¥1.1tn and a ¥1.4tn "2030 vision." The record read against it: FY2026 initial plan
    ¥770bn profit / ¥820bn COCF, delivered ¥834bn / ¥978.9bn — guidance is set low and
    beaten, the reverse of make-the-numbers. Compensation scores to ROE/profit/COCF, and
    the FY26 performance-stock payout scored itself at 90% (98/100 final score), not 120%.
  - Serial share issuance: **the reverse.** Average share count −3.2%/yr FY22→FY26
    (3,257M → 2,865M, computed from filed profit ÷ filed EPS); buybacks ¥199.6bn FY26,
    ¥399.8bn FY25; 41,075,000 treasury shares cancelled 2026-03-30.
  - EBITDA promotion: none. The promoted metric, COCF, is reconciled to the audited OCF
    line in the filing itself (cross-checked above, exact to the million) — a cash
    measure, not an earnings-before-costs measure.
  - Filed-figure tells [E4-30]: growth is visibly lumpy (no unnatural smoothness); cash
    taxes paid ¥195.7bn (+¥32.3bn refunded) vs accrual ¥222.7bn — ordinary timing for a
    resource multinational, no falling-share pattern asserted.
- **Litigation note (Note 25):** boilerplate only — "appropriate provision has been
  recorded… any additional liabilities will not materially affect" — no named material
  action. No integrity matter found in this filing.
- **Candor / half-owner test [E2-26]:** the report tells an owner what moves the result —
  per-unit price sensitivities, equity share of production, segment COCF, the Rhodes
  Ridge price, the Mainstream write-downs, dividend-vs-retention arithmetic. Passes.
- **Institutional imperative [E2-30], scored:** (1) resists change — no; portfolio churn
  is the model; (2) projects materialize to soak up funds — **the standing risk of the
  species**: FY26 investments ¥1,380bn vs COCF ¥979bn, cash flow after shareholder
  returns **−¥588bn**, debt +¥813bn. Judged against discipline evidence: returns 50%+ of
  COCF to shareholders by stated policy, recycled ¥343bn out, and the big outlay is a
  tier-1 deposit at a negotiated price, not a diversifying trophy. Scored: present as
  appetite, not yet as pathology. (3) staff studies for the leader's craving — not
  observable from the filing. (4) peer imitation — all five shosha expanded returns and
  bought resources together; noted, not scored against Mitsui alone.
- **Buyback conditions [E5-08]:** (1) ample funds — yes (liquidity shown above). (2)
  material discount to conservative IV — at the FY26 average repurchase levels the stock
  traded well inside the OE-yield range computed below; ¥199.6bn was bought back in a year
  when the price ran from ¥2,365 to ¥6,674. Neither condition visibly violated; no
  capital-allocation flag raised, with [E4-13]'s humility clause standing.

**CEO:** Kenichi Hori, President & CEO (seat since 2021 — a full MTMP cycle of record).
**Conclusion: no disqualifier found.** Not a clearance [E5-17].

### Condition (3) — the market does not overvalue: **PASSES, with thin headroom**

**COMPUTATION — NOT A CLEARANCE** *(operator rule 3: Q1–Q4 did not close IN; nothing here
carries entry language).*

**Owner earnings, look-through basis (method flag 1) [E2-23, E3-04].** The plain
convention fails here by category: FY26 OCF ¥952.9bn − total capex ¥1,109.6bn < 0, but
the capex line contains the ¥723.8bn Rhodes Ridge **acquisition of mining rights**
(commitments note, body p. 264: recognized as mining rights; FY26 forward commitments
"immaterial") — the purchase of a new deposit, not maintenance of unit volume. And OCF
excludes ¥79.6–126.6bn/yr of investee earnings retained beyond dividends.

| component | figure (Mn JPY) | basis |
|---|---|---|
| OCF, 5-yr mean FY22–26 | **937,856** | filed: 806,896 · 1,047,537 · 864,419 · 1,017,518 · 952,912 |
| OCF, 3-yr mean FY24–26 | 944,950 | window spread **+0.76% — not material [E4-25]** |
| less SBC in full [E5-06] | −14,011 | FY26 share-based payment, changes-in-equity statement |
| less (c), the guess — band | −333,248 to −385,786 | low = FY26 D&A, the corpus default [E3-44, E2-41] — supported by the filing's own FY25 shape (total capital additions 347.7 ≈ D&A 313.7); high = FY26 total capex ex-Rhodes acquisition (1,109,586 − 723,800), which still contains named growth capex (oil & gas ¥127.1bn, power ¥42.5bn) and is therefore a generous ceiling. Depletion sits inside D&A; the filing nowhere says depreciation understates renewal, so the [E5-20] exception is not invoked — but the band top covers it if it should have been. |
| plus look-through increment [E3-04] | +75,625 to +120,235 | share of investee profit − dividends received from investees: FY26 447,442 − 367,837 = 79,605; FY25 494,076 − 367,513 = 126,563; less a **5% tax allowance (disclosed judgment** — Japan's foreign-dividend exemption leaves distribution tax small; [E3-04] requires the allowance). Only two years of this pair are in the filing on disk; the FY22–24 pairs are named in the work order below. |
| **OWNER EARNINGS, the range [E4-25]** | **≈ ¥615bn to ¥720bn** (613,684 – 717,926) | ≈ ¥215–252 per share |

**The yield:** OE ÷ market cap (¥4,979 × 2,847,628,411 net-of-treasury shares =
¥14,178bn) = **4.3% – 5.1%**, against the **4.04%** JPY sovereign: **+0.3 to +1.0 points
over.** For calibration only: the FY27 dividend alone (¥140 declared minimum) is a 2.8%
cash yield on ¥4,979.

**Overvaluation test:** the [E2-28] trigger is the market judging the business *more
valuable than the facts indicate* — the OE yield falling materially through the sovereign.
At ¥4,979 the conservative-end yield still sits above the bond. **The market is not
overvaluing on today's facts. It is also paying almost nothing over the bond** — the
headroom is +0.3 points at the conservative end, against HRB's +3.4 at the same test.

**The floor, for the record [E4-28]:** honest pre-tax expectancy at this price is the
4.3–5.1% yield plus believable growth; reaching ~10% needs **+4.9 to +5.7 points of
sustained growth**. Filed record: EPS +0.9%/yr FY22→FY26; profit has FALLEN from the FY23
peak (¥1,131bn → ¥834bn). Management's ¥1.1tn FY2029 target would be +9.7%/yr — their
target, not a belief this run will write. **Below the floor at today's price; an add
could not be written even if Q2 had cleared.**

### VERDICT: **HOLD. All three [E2-28] conditions pass. ADDS REMAIN BARRED** — an add is
an entry, the hard sequence applies, Q2 is OUT, and the price independently sits below
the [E4-28] floor. Position size: 8 ADRs (~$4,950) stands as the existing judgment; no
capital-allocation flag is live to force it down; **[E5-14] — do not trim the winner.**

### Pre-committed tripwires — set now, prior to any act **[E1-02]**

**SELL triggers ([E2-28]'s two):**
1. **Overvaluation — COMPUTATION, NOT A CLEARANCE:** the price at which the conservative
   OE end (¥615bn) yields the 4.04% sovereign is **≈ ¥5,300/share TSE (≈ $670/ADR at
   ¥159.7/$)**; the optimistic end gives ≈ ¥6,200 (≈ $780/ADR). A TSE quote through
   ¥5,300–6,200 with no offsetting OE growth makes trigger 1 live — *reviewed then, not
   auto-executed*. The ADR figures move with FX; the TSE band is the reference.
2. **Funds required for a still more undervalued or better-understood name** — standing;
   the set ranks in `PORTFOLIO.md`. At +0.3 to +1.0 points over the sovereign, MITSY
   ranks below HRB (+6.3 to +7.0) on the only scale Q5 keeps; a funded buy candidate
   clearing its own gates outranks this hold almost automatically.

**Condition-(1) tripwire (the ROE slide):** filed ROE below **8%** in two consecutive
annual reports, or COCF below **¥700bn** twice consecutively — either reading says the
erosion is no longer the commodity cycle [E3-30]. One bad year proves nothing [E4-17];
once the view crystallizes, delay is the graver error [E2-40].

**Condition-(2) tripwires:** (a) the progressive-dividend promise broken — a cut below
the declared ¥140 floor without a solvency reason is a candor event, not a business
event; (b) leverage regime change — net DER sustained above ~0.8× (from 0.47×) while
investments keep outrunning COCF, i.e. imperative behaviour (2) turning from appetite to
pathology [E2-30]; (c) an integrity matter naming the company or officers — [E5-16] zero
tolerance, permanent.

**Monitoring, not triggers:** Sakhalin II / Russia dividend stream inside the ¥69.2bn LNG
dividends (named in the filing; a seizure is an earnings event to re-read, sized ~1–2% of
OE); Rhodes Ridge FID and development capex (expected determination by 2029 — the next
multi-hundred-billion-yen call on capital); the 108th Yukashoken Hokokusho (~June 2027)
re-runs this file.

**Q2 REOPEN (adds side):** none plausible — the price-taker finding cannot change while
the products are commodities. The only route back to an add is [E4-28]: a price at which
the honest expectancy clears ~10% with the growth belief written down, PLUS a reasoned
case that v4.1's Q2 should read a co-owned cost position as a moat class — a structural
question for the framework owner [PRIME RULE 5], not for this run.

---
## SELF-AUDIT
- [x] Questions answered in order; stopped at the first non-IN (Q2 OUT); no verdict skipped
- [x] No question marked IN carries an "unverified" or "provisional" caveat
- [x] Every UNRESEARCHED item names the artifact and where it lives (competitor row: 5
      peers' FY2026-03 filings on their IR sites; Mitsubishi's exact URL 403-blocked from
      this environment — ladder rung "competitor filings", obstacle WAF; OE inputs: the
      FY22–24 share-of-profit/dividends-received pairs live in the 104th–106th Yukashoken
      Hokokusho English translations, `mitsui.com/jp/en/ir/library/securities/`)
- [x] Q2 OUT states what specifically fails and on which filed evidence
- [x] Step 0: filing read, document and dates recorded, COCF cross-checked to the million
- [x] Owner earnings on a multi-year mean; both windows shown (spread +0.76%, not
      material); capex band disclosed as a judgment with the [E3-44] default and the
      reason the [E5-20] exception is not invoked; SBC subtracted in full; look-through
      increment [E3-04] with a disclosed 5% tax allowance
- [x] Competitor row attempted from filings; 1 of ~6 obtained; shortfall recorded as
      UNRESEARCHED (row is context — the OUT rests on the subject's own filing)
- [x] Sovereign for the earnings currency from the issuing authority, dated (MOF,
      2026-08-27)
- [x] Value stated as a round-number range (¥615–720bn OE; ¥5,300–6,200 review band)
- [x] One bar: none applied — no entry math ran; the hold read uses [E2-28]'s own tests.
      **Windage count: one** — the conservative OE end in tripwire 1
- [x] Prices dated; aggregator used for live quotes only and flagged (Yahoo: 8031.T,
      MITSY, JPY=X)
- [ ] Run committed to git — pending

## REGISTER
- Verdict: **[x] OUT (about the business, at Q2 — for entry)** · **HOLD (about the
  position, under [E2-28] — all three conditions pass)**
- One line: **a price-taking capital-reallocation engine with honest, disciplined
  managers and no franchise — not buyable under this framework at any price it has shown,
  holdable while returns stay satisfactory, the managers stay clean, and the market keeps
  paying less than the facts.**
- **Work orders (UNRESEARCHED items):** (1) Mitsubishi Corp FY2026-03 results —
  `mitsubishicorp.com/jp/en/ir/library/earnings/pdf/202605e.pdf`, rung: competitor
  filings, blocked by WAF/403 from this environment (a browser session retrieves it).
  *2026-08-28 addendum: a Wayback snapshot EXISTS
  (`web.archive.org/web/20260514065544/…/202605e.pdf`) but archive.org rate-limited
  this client persistently (six 429s across two spaced retry cycles); the snapshot
  opens in a normal browser;*
  (2) Sumitomo, Marubeni, Toyota Tsusho, Sojitz FY2026-03 tanshin — respective IR
  libraries; (3) the FY2022–24 equity-method profit/dividend pairs — 104th–106th
  Yukashoken Hokokusho English, Mitsui IR securities-report library (would tighten the
  look-through increment from a 2-year to a 5-year base).
- **The single biggest concern:** FY2026 investments ran ¥1,380bn against ¥979bn of COCF
  — cash flow after shareholder returns was **−¥588bn**, funded by +¥813bn of new debt in
  the year the stock and the dividend both made records. Discipline has held (net DER
  0.47×, ratings stable, returns policy honored); the imperative's behaviour (2) is the
  named way this species of business goes wrong, and the leverage tripwire above is
  pointed at exactly that.

*This file is a judgment by the AI running the framework; underlying facts are the 107th
Annual Securities Report (audited IFRS, issued 2026-06-12), the ITOCHU FIR2026, the MOF
JGB curve, and the flagged live quotes. Facts and sources are cited inline; where a
number is a judgment (the (c) band, the 5% tax allowance, the tripwire thresholds), it is
labelled as one.*
