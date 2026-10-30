# Company Run — Starbucks Corporation (SBUX) — 2026-09-04
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.25%** · date **2026-09-03** · source (issuing authority) **US Treasury daily par
  yield curve, 30-yr** (`tools/sources.py`, Treasury direct — FRED not used)
- FX: earnings are consolidated in USD (China segment earns CNY inside a USD reporter;
  noted at Q2/Q4, not an ADR question). ADR ratio: n/a, US common.

**Price and count (Stage 0, by hand):**
- price **$104.47**, 2026-09-04, **aggregator — live quote only, flagged**
- shares **1,140.0 million** hand-read off the Q3 FY2026 10-Q cover ("Shares Outstanding
  as of July 23, 2026 — 1,140.0 million"), **single class**; balance sheet shows 1,139.8M
  issued and outstanding at 2026-06-28. The cover itself reports in millions — recorded as
  filed. **Cap ≈ $119.1bn** (1,140.0M × $104.47 = $119,096M).
- Screen row (2026-09-01 triage: cap $123,291M, oe_bottom $2,835M, yield 2.3%, growth
  required 7.7%, spread 30.6%): **oe_bottom $2,835M REPRODUCED TO THE MILLION** by
  `run.py` (3-yr mean of OCF−SBC−total capex: 3,372/3,010/2,124). The brief's "~3.2% /
  ~6.8%" row is the D&A end (3-yr OE hi $3,703M) at a slightly stale price; growth
  required = 10% − yield on every construction ([E4-28] arithmetic). Cap difference is
  price drift ($108 → $104.47).

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **FY2025 10-K, year ended 2025-09-28, filed 2025-11-14,
  accession 0000829224-25-000114**; also read: Q3 FY2026 10-Q (period 2026-06-28, filed
  2026-07-29, accession 0000829224-26-000130); FY2024 10-K (2024-09-29, filed 2024-11-20,
  accession 0000829224-24-000057); 8-K of 2025-11-03 (China transaction, accession
  0000829224-25-000079); DEF 14A filed 2026-01-26 (accession 0001213900-26-007780).
- figure cross-checked against the filed statement: **FY2025 OCF $4,747.5M and capex
  (additions to PP&E) $2,305.5M read off the filed consolidated statement of cash flows**
  (10-K p.46) vs the tool's 4,748/2,306 — matches to the million; cover share count above
  is the second cross-check (tool's weighted-average basis 1,139.8M vs cover 1,140.0M,
  immaterial gap, cover governs).
- **Software-capex line (the HAS fix): checked — SBUX files NO separate
  software-development line in investing; "Additions to property, plant and equipment" is
  the only capex line ($2,305.5M FY2025), investing "Other" is $62.1M. The HAS defect
  does not bite here.**

**STAGE 0(b) — dividend decomposition, the RPM test, by hand.** The Q3 FY2026 ER claims
"65 consecutive quarters of dividend payouts with CAGR of 17% over that time period."
The streak and CAGR verify arithmetically (initiated FY2010; $0.62/q now = $2.48/yr,
yield 2.37% at $104.47). **The decomposition FAILS the RPM test:** DPS FY2020→FY2025
$1.65 → $2.44 (+48%) decomposes as **payout expansion ~ALL of it** (dividends paid as %
of GAAP EPS: ~56% FY2019 → ~150% FY2025; as % of capex-end OE: 66% FY2019 → **130%
FY2025**), retirement ~+3% (share count 1,168.8M → 1,136.9M), **earnings contribution
NEGATIVE** (EPS $2.92 FY2019 → $1.63 FY2025). The PEP/TGT failure shape, worse: the
FY2025 dividend was raised through a year it exceeded conservative owner earnings.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **Starbucks sells ~$6 cups of
  customized coffee through 40,990 stores (FY2025: 21,514 company-operated, 19,476
  licensed). Two models under one trademark. (a) The big one — company-operated retail
  (83% of revenue, $30.7bn FY2025): SBUX is the OPERATOR, not the landlord — the exact
  opposite of MCD's franchisor-landlord structure from the completed MCD run. It pays the
  rent ($2.1bn fixed + $1.2bn variable lease cost/yr on a $10.5bn operating-lease
  liability, 8.6-yr WA term), the labor (store opex 56.4% of related revenue in NA,
  FY2025 — up 5 points in one year on the announced labor investment), and the beans, and
  keeps what is left: NA segment margin 19.8% (FY2024) → 11.5% (FY2025). Every
  incremental margin point must be executed daily in ~21,500 boxes [E3-38 profile].
  (b) The asset-light layer: licensed stores ($4.35bn royalty/product revenue), Channel
  Development (packaged goods through the Nestlé Global Coffee Alliance and the PepsiCo
  ready-to-drink JV; 47.3% segment margin, $885M op income), ~$222M/yr of gift-card
  breakage, a $1.75bn interest-free stored-value/loyalty float, a $5.8bn Nestlé prepaid
  royalty amortizing at $176.5M/yr over 40 years — and, since 2026-03-30, a licensing
  royalty on the 60%-sold China JV (8,009 stores) plus 40% equity-method income.**
- The scarce input this business controls: **the trademark and the habit attached to it —
  concretely, the Starbucks Rewards balance sheet: customers hand over ~$15.2bn a year in
  advance through cards/app (FY2025 deferrals), leaving a $1.75bn covenant-free float and
  $222M of annual breakage. No competitor's coffee brand extracts prepayment at this
  scale. Second input: ~40,000 corner locations, but those are leased, not owned (98 owned
  sites at DRI was a correction; here the 10-K files essentially everything leased).**
- Will the fundamentals look broadly the same in ten years? **Coffee at retail, yes — the
  product does not change [E3-31]. The corporate perimeter is NOT stable: China (a third
  of the store base) was deconsolidated mid-window (2026-03-30), 627 stores were closed in
  FY2025's restructuring, and the operating model is being rebuilt under "Back to
  Starbucks." The BUSINESS is simple and stable in character; the current FILINGS describe
  a company in transition, which is a Q4 window problem, not a Q1 understanding problem.**
- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [x] · no close substitute [x — US, at the brand-occasion level, on the
  filed price/prepayment record below; **China: FAILED and divested**] · not
  price-regulated [x]
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**
  **The spending (marketing, service labor, remodels) defends the same trademark, not a
  replacement — the Coca-Cola shape, not the surfing-run shape [E3-51]. But TWO defects
  recorded here, where the template demands them: (a) [E4-23] — the current recovery is
  named for and priced on one manager ("Back to Starbucks" is Niccol's plan; the company's
  own Q1 FY2025 ER: "we're only one quarter into our turnaround"). A business whose FY2024
  stumble cost a CEO his job and 500bp of margin to repair is a daily-execution operator
  [E3-38], not a Mayo Clinic. Recorded as a MOAT DEFECT at Q2, not as a Q3 strength.
  (b) The operator structure: SBUX is the opposite of MCD — it OPERATES 21,514 stores and
  eats its own traffic declines; there is no toll contract between the brand and the
  P&L.**

### THE PRIMARY MOAT METRIC [E4-55] — the filed transactions/ticket series, built from
### nine 10-Ks, three 10-Qs and five earnings-release exhibits (all accessions in Step 0
### and the research folder)

**North America segment (Americas pre-FY2021), company-operated comps, 10-K MD&A:**

| FY | comps | transactions | ticket | source |
|---|---|---|---|---|
| 2016 | +6 | +1 | +5 | FY2017 10-K table |
| 2017 | +3 | 0 | +4 | FY2017 10-K table |
| 2018 | +2 | −1 | +3 | FY2019 10-K table |
| 2019 | +5 | +2 | +3 | FY2019 10-K table |
| 2020 | −12 | **−21** | **+11** | FY2020 10-K table (the last year the TABLE appears) |
| 2021 | +22 | +7 | +13 | FY2021 10-K narrative |
| 2022 | +12 | +5 | +7 | FY2022 10-K narrative |
| 2023 | +9 | +3 | +6 | FY2023 10-K narrative |
| 2024 | −2 | **−5** | +4 | FY2024 10-K narrative (Q4 FY2024 alone: comps −6, **T −10**, t +4 — ER) |
| 2025 | −2 | **−4** | +2 | FY2025 10-K narrative |
| 2026 Q1/Q2/Q3 | +4 / +7.1 / +8.1 | **+3 / +4.4 / +4.5** | +1 / +2.6 / +3.5 | FY2026 10-Qs |

**US market quarterly through the turn (ERs/10-Qs):** Q1 FY2025 −4 (T −8, t +4) · Q2 −2
(T −4, t +3) · Q3 −2 (T −4, t +2) · Q4 flat (T −1, t +1; "September Turning Positive") ·
Q1 FY2026 +4 (T +3, t +1) · Q2 +7.1 (T +4.3, t +2.7) · Q3 +7.9 (T +4.2, t +3.6). The Q4
FY2025 ER headline dates the streak: *"Global Comparable Store Sales Growth for the First
Time in Seven Quarters."* **The brief's premise ("US comparable transactions negative for
multiple quarters") was true through Q4 FY2025 and was STALE at run time [E4-26] — the
three most recent filed quarters print positive transactions WITH accelerating ticket.**

**International segment:** FY2018 +1 (T −1, t +2) · FY2019 +3 (T +1, t +2) · FY2020 −19
(T −23, t +5) · FY2021 +16 (T +14, t +1) · FY2022 −9 (China −24) · FY2023 +5
("primarily driven by customer transactions") · FY2024 −4 (t −4) · FY2025 flat (T +2,
t −2; ER — **the FY2025 10-K gives International NO comps decomposition at all**) ·
FY2026 Q1 +5 (T +3, t +2) / Q2 +2.6 (T +2.1, t +0.5) / Q3 +5.7 (T +2.6, t +3.1).

**China market (the second business):** FY2021 +17 (10-K) · FY2022 **−24** (10-K, the last
China comp in any 10-K) · FY2024 **−8, ALL of it ticket (t −8)**; Q4 FY2024 −14 (t −8,
T −6) (ER) · FY2025 −1 (T +4, **t −5**); Q4 FY2025 +2 (**T +9, t −7**) (ER). **The shape
is the price war: China never recovered price after 2022 — traffic could be bought back
only at −5 to −8% ticket. That is the filed record of losing a pricing contest to Luckin.**

### DEFLATE THE TICKET [E2-44] — both halves
**(1) "Raise prices even when demand is flat":** NA ticket chained FY2019→FY2025:
1.11×1.13×1.07×1.06×1.04×1.02 = **+51% nominal**, against CPI-U ~+26% (Sep-2019→Sep-2025)
— **real price captured ≈ +20%, and the ticket line never once printed negative in the
26-year series read (even FY2020: +11%)**. The cost: US transactions chained over the same
window = 0.79×1.07×1.05×1.03×0.95×0.96 ≈ **83.4 (−17%)**, recovering to ~86-87 on FY2026
YTD. Adjudication against the two worked precedents: **COKE passed** with volume −1.3% on
+52% pricing; **DRI failed** with OG traffic −11% on real pricing ~0. SBUX sits between:
it genuinely CAPTURED real price (unlike DRI, whose deflated ticket tracked FAFH) and
genuinely PAID traffic for it (unlike COKE). The premium is real and was exercised past
its elastic limit — [E4-37]'s agony arrived at the end: FY2025-26 ticket growth is
attributed by the filer to "annualization of prior year pricing," then "higher delivery
sales and strength in customer food attach and beverage modifications" — **mix and
willingness-to-pay, not list-price increases. The recovery's ticket composition is
franchise evidence: customers paying delivery premia and adding items is the opposite of
bought traffic.**
**(2) "Grow dollar volume with only minor additional investment of capital": FAILS on the
decade record.** Revenue $21.3bn (FY2016) → $37.2bn (FY2025), +75%; consolidated
operating income $4,171.9M (FY2016) → $5,408.8M (FY2024, +3.3%/yr, incremental margin
8.3% against a 19.6% base) → **$2,900M (FY2025, BELOW FY2016)**; ~$19bn of capex over the
ten years; owner earnings flat-to-down (Q4 carries this [E3-62/E2-56] finding at full
weight — the core US box earns franchise returns; the incremental capital (China, growth
stores) earned little, and the camouflage [E2-56] broke only when the wave receded).

### [E2-49] — WHAT DISAPPEARED FROM DISCLOSURE, dated
1. **The five-year "Change in Comparable Store Sales" TABLE** (transactions/ticket by
   segment): in every 10-K through FY2020; **withdrawn in the FY2021 10-K** — the year
   after Americas printed T −21. The decomposition survives in single-year narrative and
   in ER exhibits; the multi-year tabular series never returned.
2. **China market comps in the 10-K MD&A:** FY2021 +17 named; FY2022 −24 named; **FY2023,
   FY2024, FY2025 10-Ks name NO China comp** (the years of −8 and −1). The ER "China
   Supplemental Data" table still publishes them quarterly — a venue downgrade, not a
   withdrawal.
3. **Starbucks Rewards 90-day active members:** in every ER through **Q1 FY2025**
   (2025-01-28: "34.6 million, up 1% year-over-year"); **absent from the Q2 FY2025 ER
   (2025-04-29) onward** — withdrawn in the exact quarter growth decelerated to +1%.
   Survives once a year in the proxy (2026 DEF 14A: 34.2M, +1% y/y; growth was +4% at
   Q4 FY2024). **Fires, dated.**

### CHINA — the second business, on its honest evidence rungs
- **Scale and unit economics (rung 1, filed):** 8,009 company-operated stores at FY2025
  end (569 opened IN FY2025); China revenue ~$3.1-3.3bn/yr (Q4 FY2025 supplemental:
  $831.6M/quarter; Q3 FY2026 10-Q: $776M of revenue removed in the deconsolidation
  quarter). **AUV ≈ $390-410k vs NA company-operated ≈ $2.25M — a sixth of a US box.**
- **The war record (rung 1):** the comp series above — ticket −8 (FY2024), −5 (FY2025),
  traffic recoverable only by price. The FY2024 10-K's ONLY China quantification is the
  auditor's Critical Audit Matter on China reporting-unit goodwill.
- **The exit (rung 1, 8-K 2025-11-03 + Q3 FY2026 10-Q Note 2):** agreement announced
  2025-11-03 (Boyu Capital, "up to 60%... total value expected to exceed $13 billion"
  including a decade of NPV'd licensing); **closed 2026-03-30 at a $4bn cash-free
  debt-free enterprise value — roughly 1.2-1.3x revenue and ~$500k/store** — SBUX
  received $3.1bn (including its share of debt the JV itself raised), retained 40%
  ($1.2bn equity-method carrying value), derecognized $3.4bn of net assets, recycled
  −$282.8M CTA and −$99.7M hedge losses, and booked a $536.3M pre-tax gain. SBUX keeps
  the brand and licenses it to the JV. **The $13bn November framing vs the $4bn March EV
  is the honest measure of what the retail operation was worth against a levered attacker
  once the licensing stream is stripped out.**
- **Luckin (rung 1 for the fact of filing; numbers in the competitor row):** LKNCY still
  files 20-F with the SEC (FY2025 20-F filed 2026-03-27, acc 0001104659-26-035712) even
  though the ADSs trade OTC post-fraud. Its interim 6-Ks are furnished press releases —
  one rung down, flagged where used.
- **Verdict inside the verdict: China FAILED [E3-03](2) in the filed numbers and the
  failure was crystallized by the sale.** What remains in the SBUX perimeter is a royalty
  plus 40% of the JV — capped-upside licensing economics [E2-63], no longer an operator
  claim. The franchise claim this run adjudicates is now **US + licensed international +
  CPG only.**

### THE COMPETITOR ROW [E3-28] — 7 peers taken of the industry's ~8 real ones
*(full workings with accessions: `_research 2026-09-04 SBUX/competitor_row.md`)*

| Company | Op margin (latest FY) | OI / unleveraged NTOA | Physical series, filed | Units |
|---|---|---|---|---|
| **SBUX** | **7.9%** FY2025 (15.0% FY2024) | **~37%** FY2025 (~69% FY2024); book equity −$8.1bn, ROE unusable | **Transactions/ticket split filed 26 straight years**; FY2025 T −4/t +2; FY2026 Q3 **T +4.2 / t +3.6** | 40,990; NA co-op AUV ~$2.25M |
| MCD | 46.1% | 33.4%; equity −$1.8bn | US guest counts withdrawn FY2020 10-K after 5 negative years in 6; Q2-26: "negative comparable guest counts"; US real comps 95.4 (2013=100) | 45,356 |
| CMG | 16.2% | 82.6% | T +5.0 (23) / +5.3 (24) / **−2.9 (25)** / +0.6 / +1.0 (26) | 4,042 co-op; AUV $3.10M (−3.4%) |
| BROS (attacker) | 9.8% (4.8→8.3→9.8 rising) | 22.6% | **T −4.5 (23) / −0.1 (24) / +3.2 (25) / +5.1 / +1.7 (26)**; ticket +7.3→+2.4 | 1,136 vs 671 end-2022 (+69%); AUV $2.12M |
| LKNCY (20-F; OTC) | 10.3% (12.1% FY2023) | 61.2% | No T/t split; self-op SSS: **all 4 FY2024 quarters negative** (−20.3…−3.4), FY2025 +8.1/+13.4/+14.4/**+1.2** | **31,048** vs ~8,214 end-2022 (3.8x); 9 US stores |
| QSR (TH segment) | TH 25.4% adj (segment measure, non-GAAP) | 84.4% consolidated; tangible book **−$12.3bn** | **No T/t split filed**; TH comps +3.9/+2.7 | 4,586 TH |
| DNUT | **−30.8%** (−2.4% ex-impairment) | negative | **No unit series filed**; "lower Doughnut Shop transaction volume… offset by increased pricing of approximately 2%" | 15,194 points of access, shrinking |

- Peers named: **7 of ~8** (the eighth, Dunkin', is private under Inspire Brands since
  2020-12 — **no public filings exist**; that gap is stated, not stretched over. JDE
  Peet's is a non-SEC foreign filer, out of shelf-scope.) Luckin taken at its honest rung:
  **20-F = primary SEC filing** (ADSs OTC post-fraud); its 6-K interims are furnished
  press releases, one rung down. **[E3-61] limit stated:** the row shows position, not
  conduct — identical structures produce opposite conduct, and the FY2024-25 US value war
  proves it.
- **[E2-45] the attacker's test, adjudicated on the filed record:** the DRI conviction
  required attackers compounding traffic THROUGH the incumbent's decline (TXRH +15%
  through OG's four negative years). **That does not replicate: BROS's own transactions
  were −4.5% and −0.1% in FY2023-24 — the attacker's traffic fell through the same wave —
  and turned positive only in 2025, alongside SBUX's own turn.** The traffic loss was
  category-wide (a price-wave demand response), not a share donation to a structurally
  advantaged attacker. BROS at 1,136 boxes vs ~17,000 US Starbucks points is a real,
  bounded regional attacker with 9.8% margins; Luckin's US beachhead is nine stores. The
  China theater is where [E2-45] convicts — and that business is out of the perimeter.
- **[E2-53] dominance: FAILS** — the marketplace, not the position, set SBUX's FY2024-25
  economics (a service failure cost 500bp of margin and the traffic base; dominance-class
  franchises "good or bad, will prosper"). Failing the STRONGEST franchise reading does
  not fail Q2 (the COKE precedent); it caps the class at NARROW.
- **Untapped pricing power [E3-33]: NO — the inverse.** The power was tapped +51% nominal
  FY2019→25 (real +20%) and is now consciously rested: FY2026 ticket growth is filed as
  delivery/attach/modification MIX, not list price. No near-monopoly claim is made
  [E5-28].
- **Class: [x] NARROW** (US retail + licensing; wide-class economics live only in the
  licensed/CPG layer: Channel Development 47.3% margin, breakage $222M/yr, the $1.75bn
  prepaid float) · **Direction: narrowed FY2021-25 (traffic −17% chained vs FY2019, China
  lost, NA margin 19.8→11.5); physical series positive and accelerating at run date, three
  quarters filed.**
- **VERDICT: [x] IN — decided by the filed record, against the brief's OUT prior
  [E4-26]:** (1) the two-decade price-integrity record — ticket never negative in 26
  years read, real price +20% captured FY2019-25 and HELD through a two-year traffic
  decline (the failure mode that convicted TGT and DRI — nominal price breaking — never
  appeared); (2) the prepayment franchise — $15.2bn/yr deferred through cards/app, $3.5bn
  loaded in a single quarter, #2 US gift-card brand, $1.75bn covenant-free float — no
  peer on the row has an analogue; (3) the [E2-36] classification came out
  excisable-cancer, not Pygmalion, on filed outturns: the named operational cancer was
  cut (627 stores, China control sold, service model rebuilt) and the physical series
  responded within five quarters — GEICO-1976 shape, decided on the traffic print, not on
  the manager's reputation; (4) the attacker test failed to convict (BROS's own negative
  traffic through the wave). **Recorded defects that survive into Q4/Q5: the [E2-44](2)
  capital-hunger failure, the [E4-23] key-person defect, three dated [E2-49] firings, and
  a NARROW class whose re-proven margin level is still unfiled — the FY2026 10-K is the
  pre-committed re-read.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [x] **Daily execution** — have-to-be-smart-every-day, not have-to-be-smart-once **[E3-38]**
- [ ] **Control** — whole business, no exit **[E1-16]**
- [ ] **Leverage** — small asset errors destroy equity **[E3-29]**

**Case declared: Q3 is a BINARY GATE on daily execution [E3-38/E3-43]** — 21,514
company-operated stores where the margin is executed one latte at a time, and the filed
proof of manager-sensitivity is on the record: one CEO's eighteen months (Narasimhan,
2023-03 → 2024-08) coincided with US transactions −5%, a Q4 FY2024 of T −10, and his
termination; the successor's first year moved traffic +8 points. The DRI precedent
declared the same gate for the same reason.

**Honesty — binary, permanent, filings-based [E5-16].** **No disqualifier found in the
filings read.** No restatement; Deloitte opinions clean FY2024-25; cash-tax tell [E4-30]
ACQUITS (cash taxes paid $1,294.2M / $1,373.3M / $715.6M ≈ 26% / 29% / 30% of falling
pretax income — the share RISES). Conduct file, dated: the unionization litigation wave
(NLRB complaints from 2022 onward; ~6% of US company-operated stores unionized per the
FY2025 10-K) is a labor-conduct matter read under [E5-22] — what counts is whether they
act, and the FY2025 filings describe active bargaining frameworks; recorded as watched,
not charged. Written per [E5-17]: this is an absence of found disqualifiers, not a
finding of honesty.

**STEP 2 — THE FLAGS [E4-22, E5-15].**
- [ ] weak accounting — not found; SBC expensed, no pension plan of consequence
- [ ] unintelligible footnotes — no; the China divestiture note is a model of clarity
      (every derecognized component quantified — the [E2-26] direction)
- [x] trumpeted earnings projections / growth targets — **the guidance culture is live:
      FY2026 quarterly comp guidance ("Q4 U.S. comparable store sales growth of 6.5% or
      greater") plus non-GAAP EPS $2.55-2.65, RAISED at Q3 [E5-30's ratchet]. The
      candor-direction exception on the same record: FY2025 guidance was SUSPENDED
      outright (8-K/ER 2024-10-22, "given the company's ceo transition coupled with the
      current state of the business") rather than guessed — [E2-69]-direction deviation,
      credited.**
- [ ] serial share issuance — no; count 1,455.8M (FY2016) → 1,140.0M; issuance proceeds
      $77M/yr vs dividends $2.77bn ([E2-52] does not fire)
- [ ] EBITDA promotion **[E4-29]** — **ZERO occurrences** of EBITDA in the FY2025 10-K,
      the Q3 FY2026 10-Q, all ERs read, and the 2026 proxy (the FY2024 10-K's four
      occurrences are the auditor's China-goodwill CAM describing valuation multiples —
      not management promotion). Does not fire.
- [x] **restructuring excluded from the pay metric [E5-33]:** the proxy's non-GAAP
      operating income (the bonus plan's financial base) excludes "Restructuring and
      impairment costs" as "anticipated to be completed within a finite period of time" —
      against a filed record of **restructuring provisions in 12 of the last 18 fiscal
      years, in four named waves: FY2008-10 ($266.9M + $332.4M + $53.0M — the store-closure
      wave), FY2017-19 ($153.5M + $224.4M + $135.8M — Teavana et al.), FY2020-23 ($278.7M +
      $170.4M + $46.0M + $21.8M), FY2025- ($892.0M + FY2026 YTD still running). [E4-52]
      counted honestly: not twelve consecutive years (PEP's record stands), but a
      restructuring RECURRENCE pattern whose charges the pay plan deletes every time.**
      The symmetric side, credited: the same non-GAAP also excludes a litigation
      settlement the company RECEIVED (a gain deducted — the DRI/TGT candor direction).
- [ ] filed-figure tells [E4-30] — smoothness: none (earnings fell 51% in FY2025 and were
      reported that way); cash-tax: acquits (above).

**STEP 3 — THE PRIMARY TEST [E2-01].** **Book equity is a $8.1bn DEFICIT manufactured by
buybacks — ROE is unusable (the ULTA/BBWI/MCD ruling). Denominator per [E2-43]:
unleveraged net tangible operating assets** = assets 32,019.7 − cash 3,219.8 − investments
494.1 − equity-method stakes 466.2 − goodwill 3,368.9 − intangibles 166.8 − op-lease ROU
9,315.7 − non-interest operating liabilities (AP 1,852.8 + accrued 2,359.7 + payroll
1,093.9 + stored value/deferred current 1,840.6) ≈ **$7.84bn. OI/NTOA: FY2024 ≈ 69%,
FY2025 (the crisis year, restructuring in) ≈ 37%.** The tangible core earns
franchise-class returns even stressed; the capital the returns were NOT earned on is the
$19bn of decade capex and China (the [E2-56] camouflage, charged at Q2/Q4).

**The half-owner test [E2-26]:** mixed, both directions quantified — the divestiture note
and restructuring tables are exemplary line-by-line disclosure; the three dated [E2-49]
withdrawals (Q2 section) are the other direction; net: the reader can still reconstruct
everything from ERs + proxy, at a venue cost.

**The institutional imperative [E2-30]:**
- [x] resists change in current direction — **historically**: growth capex and China
      buildout continued through FY2024's traffic collapse; broken only by replacing the
      CEO
- [x] projects/acquisitions to soak up funds — the FY2016-24 store-growth machine
      (+56% units) against flat owner earnings
- [ ] staff studies for the leader's craving — not observable in filings read
- [x] peer behaviour imitated — FY2024's "increased promotional activity" (value-menu
      chase, named in the FY2024 10-K margin walk)

**Capital allocation — the record, and the two buyback conditions [E5-08]:**
- **The decade [E2-60] finding, FY2016-FY2025: ~$49.6bn returned ($20.2bn dividends +
  $29.4bn buybacks) against ~$25.8bn of capex-end owner earnings — 1.9x — funded by the
  $7.15bn Nestlé prepayment, +$12bn of debt, and book equity driven to −$8.1bn.** The
  FY2018-19 leg alone: $17.4bn of buybacks (~248M shares ≈ $70 avg). Restricted earnings
  [E2-60] were distributed for years; the third maintenance dimension (financial
  strength) paid for it. **FIRES for the decade.** FY2025 standalone: dividends $2,771.4M
  vs conservative OE $2,124M — >100% payout in the turnaround year, dividend raised
  anyway (65 consecutive quarters paid, 17% CAGR — the ER trumpets it).
- **The reversal now on record: FY2026 YTD the China $3.1bn went to debt ($2,815.9M
  repaid, including a $1.3bn tender funded by divestiture proceeds per the 10-Q),
  buybacks stayed at ZERO for a seventh consecutive quarter, dividend held. Debt
  $16,074.8M → $13,278.6M.** [E5-25]-direction: financial strength taking precedence,
  the first such sequence in the filed decade.
- (1) ample funds: currently yes, by discipline (revolver $3.0bn undrawn, CP zero — not
  counted [E5-39]).
- (2) discount to conservative IV: not currently testable (no buybacks since FY2024).
  FY2024's $1,266.7M at ~$95 average sits above this run's zero-growth value band —
  **retrospective condition-2 FLAG, stated with [E4-13]'s humility clause; binds
  position size, never the rate.**
- **Pay-versus-performance (Item 402(v), 2026 proxy): $100 (FY2020) → $110.47 (FY2025) vs
  peer group $165.21 — trails its own chosen peer index by ~55 points over five years.**
  FY2025 pay behaved: STIP financial payout 39.7% of target (blended 54.8% with the
  100% individual factor — the uniform individual factor is the COKE-shaped soft spot);
  2023-25 PRSUs paid 30.38%. **No DG/ULTA rigging pattern. Niccol's FY2024 signing
  package: SCT $95.8M (CAP $96.4M) — the price of the manager-is-the-plan structure
  recorded at Q2; FY2025 CAP fell to $3.6M with the stock.**

**THE GUARDRAIL — checked.**
- [x] Nothing here promotes the name; Q2's verdict used the business record, not Niccol.
- [x] Key-person dependence recorded at **Q2 as a moat defect [E4-23]**, not here as a
      strength.
- [x] Manager-as-plan [E2-35/E2-36]: adjudicated at Q2 — franchise intact, cancer
      excised (China sold, 627 stores closed, service model fixed with traffic
      responding). The excisable-cancer reading is supported by filed outturns, not by
      the manager's reputation.

- **VERDICT: [x] IN (gate passed — no disqualifier found)  [ ] OUT  [ ] UNRESEARCHED
  [ ] UNKNOWABLE**
  *IN = no disqualifier found [E5-17]. IN never promotes. Flags live: guidance ratchet,
  restructuring-excluding pay metric [E5-33], decade [E2-60], retrospective buyback
  condition-2.*

## Q4 — WILL IT SURVIVE?

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**

**Owner earnings by year, OCF − SBC − (c), $M (capex end / D&A end):**
| FY | OCF | SBC | capex | D&A | OE capex-end | OE D&A-end |
|---|---|---|---|---|---|---|
| 2016 | 4,575.1 | 218.1 | 1,440.3 | 1,030.1 | 2,916.7 | 3,326.9 |
| 2017 | 4,251.8 | 176.0 | 1,519.4 | 1,067.1 | 2,556.4 | 3,008.7 |
| 2018* | 11,937.8 | 250.3 | 1,976.4 | 1,305.9 | 9,711.1 → **2,561 adj** | 10,381.6 → 3,232 adj |
| 2019 | 5,047.0 | 308.0 | 1,806.6 | 1,449.3 | 2,932.4 | 3,289.7 |
| 2020 | 1,597.8 | 248.6 | 1,483.6 | 1,503.2 | **−134.4** | −154.0 |
| 2021 (53w) | 5,989.1 | 319.1 | 1,470.0 | 1,524.1 | 4,200.0 | 4,145.9 |
| 2022 | 4,397.3 | 271.5 | 1,841.3 | 1,529.4 | 2,284.5 | 2,596.4 |
| 2023 | 6,008.7 | 302.7 | 2,333.6 | 1,450.3 | 3,372.4 | 4,255.7 |
| 2024 | 6,095.6 | 308.3 | 2,777.5 | 1,592.4 | 3,009.8 | 4,194.9 |
| 2025 | 4,747.5 | 318.3 | 2,305.5 | 1,771.5 | 2,123.7 | 2,657.7 |

*\*FY2018 [E4-41]: the $7.15bn Nestlé up-front prepayment sat in OCF via deferred revenue —
a one-time sale of 40 years of royalties, named and REMOVED before any mean is trusted.
FY2020-21 are the pandemic pair; FY2021 also has a 53rd week (+$576M revenue). FY2025 OE
is depressed by named turnaround items (restructuring cash costs; the −$408.4M coffee-
inflation inventory build, which OCF correctly nets per [E2-23] constraint 3).*

- **Short-window mean** (FY2023-25): **$2,835M** capex end (screen reproduced to the
  million) / $3,703M D&A end
- **Mid-window** (FY2021-25): $2,998M / $3,570M
- **Long-window** (FY2016-25, FY2018 adjusted): **$2,582M** / $2,890M
- **Spread, conservative end:** 2,582 → 2,835 ≈ 10% between windows; the full band
  $2,124M (FY2025 alone) to $3,703M (3-yr D&A end) is **74% wide at the extremes, with
  every distorted year NAMED** — the width does NOT close the file because the entire
  band prices below the sovereign at Q5 (the DG/UAL principle: the band cannot change the
  verdict).
- **THE PERIMETER CHANGE (the DKS/HHH class):** every year above INCLUDES China retail
  (~$3.1-3.3bn revenue, 8,009 stores); the cap prices a company that no longer operates
  it (deconsolidated 2026-03-30). The filings do not split China's OE contribution
  (International segment aggregates it) — **so a clean pro-forma is not buildable from
  filings, stated per the DKS instruction's "or state why not."** What exists: ONE
  post-perimeter quarter (Q3 FY2026: OCF $1,641.9M, capex $291.4M, SBC ~$97M → OE
  ≈ $1,254M in thirteen seasonally-strong weeks, flattered by tariff refunds and
  held-for-sale D&A stoppage). One quarter is not a year — displayed, not annualized
  [E4-41]. Directionally the swap is OE-favorable: a war-compressed operator margin out,
  a royalty at near-zero capital plus 40% equity income in.
- **OE JUDGED: ~$2,600M** (the 10-yr adjusted mean; below the 3-yr because FY2023-24
  contain the pricing wave's peak margins [E4-41 normalizes down], above FY2025 alone
  because the restructuring cash is finite). Band carried: **$2,100M-$3,700M.**
- **Maintenance capex (c) — the disclosed judgment [E3-44/E2-23], and the brief's live
  question answered from the filer's own words:** the "Back to Starbucks" remodel
  program ("coffeehouse uplifts... intended to deliver greater connection, consistency,
  and value") and the renovations line are **competitive-position defense = MAINTENANCE
  under [E2-23]'s definition** — they defend the same trademark, not growth. Therefore:
  (a) on the filed history, (c) is taken at TOTAL capex (conservative; the filer splits
  no maintenance/growth dollars in any vintage read — the TGT precedent); (b) going
  forward, the FY2026 capex collapse ($887.8M YTD, 0.73x D&A) **UNDERSTATES (c)** — if
  uplifts are maintenance, cutting them is deferred maintenance, and the D&A default
  (~$1.6bn ex-China) is the floor of any honest go-forward guess. Capex/D&A FY2025:
  1.30x. The [E5-20] exception class does not apply (no filing says depreciation
  understates renewal); the D&A end is displayed as the generous boundary, not taken.
- Stock compensation subtracted in full **[E5-06]**: yes, $318.3M FY2025, every year in
  the table. (RSU-based; reported charge taken as the measure, no material option
  program [E3-70].)
- **Gift-card float [E5-46] noted, not silently ignored (the brief's instruction):**
  $1,751.7M of stored-value/loyalty liability turns over ~8.7x/yr ($15.2bn deferred,
  $15.2bn recognized FY2025), costs nothing, has no covenants or due dates [E3-52], and
  throws off $222.4M/yr of breakage (recognized IN revenue, so already inside OE — do
  not double-count). The Nestlé $5.8bn deferred-revenue stub is the same animal at 40-yr
  duration: money received 2018, obligation ratable, $176.5M/yr recognized. **Float
  funds ~22% of tangible operating assets; it is a real funding moat, and the sector
  method's logic values it as cheap financing, not as an earnings add-on.**

### Great, good, or gruesome? **[E4-20]**
- [ ] great  [x] **good, with a gruesome decade leg, honestly split [E2-56]**  [ ] gruesome
- Evidence: the core earns great-class returns (OI/NTOA 37% in the stress year, ~69%
  normal; float-funded); **the DECADE'S incremental capital was gruesome-adjacent:
  ~$19bn of capex FY2016-25, revenue +75%, operating income FY2025 BELOW FY2016
  ($2.90bn vs $4.17bn; even FY2024's $5.41bn = only +3.3%/yr), owner earnings flat**
  — and the China leg took billions of that capital and was sold at ~1.3x revenue.
  [E4-43] governs: the good class passes Q4; the gruesome leg is priced at Q5, and the
  go-forward mix (67% licensed stores, China as royalty, capex halved) is structurally
  LIGHTER than the filed decade.

### Staying power — score all three **[E5-11]**
- (1) large and reliable stream of earnings: **pass** — OCF positive every year including
  FY2020 ($1.6bn); revenue drawdown worst case −8% (FY2020). Earnings LEVEL halved in
  FY2025 and is recovering; reliability of the stream, not its level, is what (1) asks.
- (2) massive liquid assets: **FAIL** — $3,449.8M cash + ~$250M investments against
  $13,278.6M debt and a $10.4bn lease stack. The $3.0bn revolver and $3.0bn CP program
  are refused as strength [E5-39] (both undrawn, and that is the point). Same failure
  shape as MCD.
- (3) no significant near-term cash requirements: **pass** — the FY2026-27 $3.0bn
  maturity wall was PRE-CLEARED with China proceeds ($2,815.9M repaid YTD including a
  $1.3bn tender, 10-Q verbatim: proceeds used "for debt reduction, strengthening our
  balance sheet") — the [E2-64] direction. Current portion $1,498.4M vs $3.4bn cash.
- Leverage, named and quantified **[E4-16]**: $13,278.6M funded debt (16,074.8 at FY2025
  end, coupons 2.0-4.8%, ladder ≤$1.75bn/yr through 2030) + $10.4bn operating-lease
  liability (8.6-yr WA, 3.7% discount) against **negative $8.1bn book equity** — the
  equity was repurchased away FY2018-19. Debt ≈ 5.1x judged OE; coverage [E2-54] in the
  TROUGH year: OCF−capex $2,442M / cash interest $588.3M ≈ **4.2x after capex** — zip-up
  territory is not reached even stressed.

### Name the specific way THIS business dies **[E2-27, E3-24]**
- **Mechanism 1 — solvency:** a second, deeper traffic wave against the debt+lease stack.
  Modeled from filed figures: FY2025 IS the on-record stress test — US transactions −4%,
  restructuring $892M, coffee-cost inflation, and the year still produced $4.75bn OCF,
  4.2x after-capex interest coverage, and a raised dividend. For death, op income must
  fall ~75% from FY2024's level and STAY there through the 2030s ladder. **A low-level
  possibility.**
- **Mechanism 2 — the real one, valuation death [E2-27 shape]:** the DG/MCD-shape value
  stagnation — the US habit plateaus, every remodel and labor dollar becomes defensive
  (c), licensing growth cannot outrun core stagnation, and ten more years of capex
  produce another flat OE decade. **The FY2016-25 filing IS five-plus years of this
  already on record. A real possibility.**
- **Mechanism 3 — the licensing cap [E2-63]:** China upside is now contractually a
  royalty plus 40% — if "Back to Starbucks" succeeds mostly in CHINA's JV, SBUX
  shareholders collect a capped share. Combines with 2.
- **VERDICT: [x] IN** — survival is not the live question; the value-stagnation death is,
  and it is priced at Q5.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

**THE FLOOR, before the ranking [E4-28, E3-13].** **Honest pre-tax expectancy at this
price: ~5-8%** (yield 1.8-3.1% judged ~2.2%, plus honest growth: realised OE growth
~0%/decade, op income +3.3%/yr pre-turnaround; granting the full guided margin recovery
AND mid-single-digit growth on top still lands under 8%). **Below ~10% → quit on, not
ranked.** No risk premium in the rate [E3-42]; the bare 5.25% sovereign is used
throughout.

**1. THE YIELD**
- owner earnings **$2,600M judged** ÷ market cap **$119,096M** = **2.18%** · band
  **1.78% (FY2025 alone) - 3.11% (3-yr D&A end)** · sovereign **5.25%**

**2. WHAT THE PRICE ALREADY ASSUMES**
- perpetual growth needed just to match the bare bond: **+2.14% to +3.47%, judged
  ~+3.1%** — achievable, and the strongest thing sayable for the price
- perpetual growth needed for the [E4-28] floor: **+6.9% to +8.2%** — against realised
  owner-earnings growth of ~0%/decade and [E4-35]'s base rate, the burden is not met
- what the price assumes in level terms: $119.1bn × 5.25% = **$6.25bn of owner earnings
  — 2.4x the judged figure, above even FY2024's D&A-end construction** — the quote
  prices the full margin recovery plus growth beyond it, today
- what the business has actually done: OE $2,917M (FY2016) → judged $2,600M (FY2025);
  revenue +5.9%/yr; op income +3.3%/yr to FY2024, negative through FY2025

**3. WHAT YOU ARE PAID**
- return at the current price = **−2.1 to −3.5 points UNDER the sovereign** (judged
  −3.1) — below the bond on every construction

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].** *"If you say I'm going to
stick an extra 6 percent in on the interest rate to allow for the fact — I tend to think
that's kind of nonsense. … It may look mathematical. But it's **mathematical gibberish** in my
view. You better just stick with businesses that you can understand, **use the government bond
rate**."*
- sovereign used **5.25** % — **the bare rate, no per-name premium added.**
- **Certainty is handled TWICE and neither place is the rate**: at the understanding gate
  (a business you cannot be certain about fails Q1) and in the discount to value demanded at
  the end. It is priced **once** — the end margin — and may not be stacked **[E4-11, E4-48]**.
- *Corrected 2026-09-02, found by the WTM run: this block carried "the corpus gives a floor of
  +3% over the long bond", which `THE FRAMEWORK v4.md` had explicitly REWRITTEN on 2026-08-28
  as a misreading of [E3-13]'s 10-minus-7 arithmetic. The framework governs, and the template
  is the enforcement surface, so a template contradicting it misleads every run that fills it
  in.*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — zero-growth at the 5.25% sovereign,
1,140.0M shares:
- conservative **~$35/sh** (FY2025-alone OE $2,124M) · judged **~$50/sh** ($2,600M ≈
  $49.5bn) · optimistic **~$60-65/sh** (3-yr D&A end $3,703M ≈ $70.5bn) · **at the
  [E4-28] floor: ~$19-33/sh, judged ~$23** · **current price $104.47** (2026-09-04,
  aggregator, flagged)
- the price sits **ABOVE the entire zero-growth band** — reaching it requires the
  ~+3.1% perpetual-growth belief on top of the judged OE, and reaching the floor
  requires +7-8% perpetual [E4-35]

**THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21].** *(Corrected 2026-09-03, found by the
HHH run — this block still carried v4.0's "THERE IS NO HURDLE" heading, the SEVENTH
surviving home of the rule the framework rewrote on 2026-08-28. The floor section above at
[E4-28] already governs; this block is the ranking that applies only to what clears it.)*
- floor verdict first: honest pre-tax expectancy **~5-8%** vs ~10% **[E4-28]** — **BELOW
  → QUIT ON; the ranking lines are not filled in.**

**WHICH BAR ARE YOU USING?**
- [x] **Screamer test [E4-01]** — the price ($104.47) sits **above the whole zero-growth
      range** ($35-65): **outcome three — no.** No margin was added on top; no second bar
      applied to the same number.
- **Windage count: ONE** — conservatism is spent once, in the OE judgment ($2,600M vs the
  3-yr D&A end's $3,703M), with the reasons named ([E4-41] wave-peak normalization;
  FY2026 capex understating (c)). The value band then uses the bare sovereign and no
  further margin **[E4-11, E3-42]**.

- **VERDICT: FAIL at Q5, ON PRICE, at the [E4-28] floor — quit on, not ranked. Q1 IN ·
  Q2 IN (NARROW) · Q3 IN (gate passed) · Q4 IN — the SEVENTH name to clear all four
  business gates (after ORLY, BRK-B, MCD, HAS, COKE, and TSCO, whose parallel run closed
  hours earlier), and the second restaurant.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not opened — no entry (Q5 quit on the floor). Pre-committed re-look terms recorded in
the REGISTER below [E1-02]: the FY2026 10-K (~Nov 2026) re-read, and the ~$50/sh judged
zero-growth value, recomputed at the sovereign of the day.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped (Q6 not opened — no entry)
- [x] **No question marked IN carries an "unverified" or "provisional" caveat** (the
  Dunkin' row gap is a stated absence of any existing document, not a caveat on the
  verdict; 7 of ~8 peers filed)
- [x] No UNRESEARCHED verdicts issued
- [x] No UNKNOWABLE verdicts issued
- [x] Step 0: FY2025 10-K read (MD&A, cash-flow detail lines, footnotes), accession
  0000829224-25-000114; OCF/capex cross-checked to the filed statement; cover count by
  hand
- [x] Owner earnings on multi-year means; three windows shown; capex band disclosed as a
  judgment with the (c) reasoning cited from the filing
- [x] Competitor row: 7 peers, same metrics, filing-sourced with accessions; Luckin's
  rung stated; Dunkin' absence stated
- [x] Sovereign: USD earnings, US Treasury daily par yield curve 30-yr, 5.25%, 2026-09-03
- [x] Value as a round-number range ($35-65 zero-growth; $19-33 floor)
- [x] One bar (screamer); windage count ONE, stated
- [x] Price $104.47 dated 2026-09-04, aggregator, flagged as live-quote-only
- [x] Committed after Step 0, Q1, Q2-series, Q2-verdict+Q3, Q4+Q5 (write-early protocol;
  survived one session kill with zero question loss)

## DEFECTS AND CORRECTIONS, confessed
1. **The brief's central premise was stale [E4-26], twice:** (a) "US comparable
   transactions negative for multiple quarters" was true only through Q4 FY2025 — the
   three most recent filed quarters print +3/+4.3/+4.2; (b) "the announced
   stake-sale/partnership process" had CLOSED (2026-03-30) — the perimeter itself
   changed. Both corrections are the run's decisive facts.
2. **A parallel TSCO session shares this repo**; my first commit (`ee78f50`) accidentally
   swept four uncommitted TSCO research files into the SBUX commit via a broad `git add`.
   Not destructive (their work was preserved, arguably helpfully), but the history is
   muddied; subsequent commits stage SBUX paths only.
3. **China's OE contribution is not isolable from filings** (International aggregates
   it) — the go-forward OE judgment leans on one post-perimeter quarter plus direction,
   stated as such.
4. **FY2023 China market comps** were not pinned from a document on disk (the FY2023 Q4
   ER was not fetched); the series shows the 10-K withdrawal either side of it. Gap
   named, immaterial to the verdict.
5. The 402(v) five-year TSR row reads FY2021-FY2025 with a FY2020 $100 base; the proxy's
   own footnote labels it "(3-Year)" in one header — the table's values were used as
   printed.
6. run.py share basis was the weighted average again (known queue-wide defect); cover
   count used instead.

## REGISTER
- Verdict: **FAIL at Q5, ON PRICE, at the [E4-28] floor. Business verdicts: Q1 IN · Q2 IN
  (NARROW, direction turning) · Q3 IN (gate) · Q4 IN.**
- One line: **the sixth name to clear all four business gates, and the same ending as
  MCD/HAS/COKE: a real narrow franchise, repriced by the market's own recovery trade to
  2.2% on judged owner earnings against a 5.25% bond — quit on, not ranked.**
- **PRE-COMMITTED RE-LOOK [E1-02]:** re-read at the FY2026 10-K (~Nov 2026).
  Thesis-confirming: US transactions still positive with NA op margin recovering toward
  the guided >11% consolidated non-GAAP, delivered not guided; China JV royalty
  economics quantified in the K. Thesis-breaking for the Q2 IN: transactions negative
  again while ticket is pushed, a fourth [E2-49] withdrawal (the ER comps table or China
  supplemental), or dividend raised again above conservative OE with borrowings rising
  [E2-60]. Value trigger: ~$50/sh judged zero-growth at a 5.25% sovereign — recompute at
  the rate of the day before acting on any fall.
