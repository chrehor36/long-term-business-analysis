# RE-RUN — Nitori Holdings (NCLTY / 9843.T) under v4.1
**2026-08-28.** Purpose: replace the NI-proxy owner earnings and the stale spread with the
filed three-year IFRS record, per the standing suspension in `PORTFOLIO.md`. This is a
**re-run of Q4/Q5 inputs and the adds decision on a held position** (669 ADR sh ≈ +27%),
not a fresh entry run. Sources: Nitori's own English statements on disk (byte-verified
against the IR site), `NITORI FY2024 - work order result.md` [S1-S4 register there].

## Step 0 — rate and filings
- **JPY 30y 4.038%, 2026-08-27, Japan MOF official JGB curve** (issuing authority).
- Price **¥3,068 (9843.T, 2026-08-28**, home listing — aggregator, live quote only).
  Shares **565,057,238** (post 5:1 split 2025-10-01) → **market cap ≈ ¥1,733.6bn**.
- Filings read: FY2025 securities-report statements (carrying audited FY2024 IFRS
  comparatives) and FY2026 statements, cash-flow pages read line by line this session.
  **Premise corrections recorded:** FYE moved to March 31; FY2024 IFRS exists only as the
  FY2025 report's comparative column; the 13.4-month FY2023 transition period is excluded
  from all averaging as non-comparable.

## Q4 inputs — the filed three-year IFRS record (JPY millions)

| | FY2024 | FY2025 | FY2026 |
|---|---:|---:|---:|
| Operating cash flow | 181,164 | 144,384 | 148,911 |
| D&A (incl. right-of-use dep.) | 61,082 | 66,143 | 69,509 |
| Cash capex (PP&E + inv. property + intangibles) | 127,340 | 125,308 | 44,412 |
| Lease-liability repayments (financing CF) | 35,816 | 37,319 | 36,066 |
| Net income (owners) | 90,158 | ≈82,545 | ≈89,268 |

SBC: **nil, disclosed** (Note 33) — the old NI-proxy defect is closed with a real zero, not
an assumption. FY2025/26 NI derived from split-adjusted basic EPS (¥146.08 / ¥157.98 ×
565.06M); the wrapped P&L line is the cross-check to read on the next pass.

## Owner earnings — the (c) judgment, disclosed, with the IFRS-16 rule applied

**IFRS-16 rule (conservatism spent once):** either subtract lease repayments from OCF *or*
carry ROU depreciation inside (c) — never both. Three bases shown; the spread is carried
**[E4-25]**:

| basis | construction | FY24 | FY25 | FY26 | mean |
|---|---|---:|---:|---:|---:|
| A — leases via ROU dep. | OCF − D&A(total) | 120,082 | 78,241 | 79,402 | **92,575** |
| B — capex-conservative | OCF − leases − total capex | 18,008 | −18,243 | 68,433 | **22,733** |
| C — stated judgment | OCF − leases − owned-capex maintenance guess ≈ ¥45bn | — | — | — | **≈76,800** |

**The judgment, stated:** basis B treats every yen of capex as maintenance, which the record
itself refutes — capex collapsed from ¥125bn to ¥44bn in FY2026 while the store base held,
so a large share was discretionary growth (new stores, DCs). Basis A's FY2024 is inflated by
a working-capital swing (OCF ¥181bn vs PBT ¥125bn). **Central owner earnings ≈ ¥75–93bn**,
with basis B's ¥23bn carried as the honest far tail because **the filing does not split
maintenance from growth capex** — resolving document, named: the Japanese securities
report's capex-by-purpose disclosure (EDINET). That split is the remaining UNRESEARCHED item
on Q4's inputs. *(Retrieval attempted 2026-08-28: Nitori's IR library pages are
JS-rendered — the static HTML carries no securities-report links — and the EDINET API now
requires a registered key. Routes: a browser session on nitorihd.co.jp/ir/library/, or a
free EDINET API key, or the EDINET full-text viewer searched for 9843.)*

## Q5 — COMPUTATION, and the floor

- **Yield:** ¥75–93bn ÷ ¥1,733.6bn = **4.3–5.4%** central (tail 1.3% on basis B), against
  the **4.04% JPY sovereign** → **+0.3 .. +1.3 points** central.
- **The floor [E4-28]:** a ~10% pre-tax expectancy needs **+4.6 to +5.7 points of sustained
  growth** written down and believed. Nitori's record (long store-count and profit growth,
  but FY2025-26 profits below FY2024's) does not let me write that belief down today.
  *Open question, flagged not resolved: the floor's basis is the authors' guessed future
  opportunity cost in their (USD) set; whether a JPY name is judged against the same ~10% is
  a judgment each run must state. This run states it as: yes — the user's opportunity set is
  USD-denominated.*

## Verdicts on the re-run's scope

- **Q4 inputs: REPLACED.** NI-proxy retired; three filed IFRS years, SBC resolved at zero.
- **Q2: UNRESEARCHED, unchanged** — the competitor row (JPY furniture/home-furnishing peers,
  same metric, same window) has never been built; the moat class stays PROVISIONAL.
- **Q3: retailer → GATE [E3-38, E3-43]** on any entry; the pre-entry clean read of
  2026-07-16 governs the hold.
- **ADDS: REMAIN BARRED** — twice over: Q2 PROVISIONAL closes the entry sequence, and the
  floor gap cannot be written down. The old NARROW-spread suspension is superseded by these
  two named reasons.
- **HOLD: STANDS** under **[E2-28]** — business returns satisfactory, no manager
  disqualifier on file, and at a ~4.3–5.4% owner-earnings yield the market is not judging
  the business more valuable than the facts.

*Windage count: one — the conservative placement of the (c) guess. The 2-year basis-A mean
(¥78.8bn, excluding the WC-swollen FY2024) was used as the sanity check on the central
range, matching the prior file's ¥78–79bn exactly.*
