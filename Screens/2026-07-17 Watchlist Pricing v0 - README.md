# Global Watchlist Pricing Pass v0 — 2026-07-17 — PARTIAL, flagged
First automated pricing of the 40-name Global Quality Watchlist.
**Result: 6/40 priced, 34 no-data, 1 artifact — infrastructure gaps, not
verdicts.**

## What the 5 real reads say (and they say a lot)
| Ticker | True read | Meaning |
|---|---|---|
| HESAY Hermès | 1.2% vs 4.0% | Tier-1 quality at ~3x too expensive — as expected |
| LRLCY L'Oréal | 2.0% vs 4.0% | Same |
| LNSTY LSEG | 1.0% vs 5.45% | Same |
| IDEXY Inditex | 0.95% vs 4.0% | Same |
| RBGLY Reckitt | −0.12% | Negative worst-year — auto-fail range anchoring |
The watchlist's job is to WAIT — these confirm the waiting is real.

## Known bad / gaps
- **ATLKY "19.05%" is a currency artifact** (SEK financials vs USD ADR
  cap ≈ 10x inflation; true ≈ 1.8%) — same bug class the FTSE screen's
  currency check caught on ULVR/DGE. DO NOT act on it.
- 34 no-data: the 'us'-venue names (NVO/ASML/TSM/DEO/UL/RELX/RACE/MELI/
  FMX) had no NI fetcher path, and many unsponsored-ADR pages lack
  financials tables on the OTC source.

## Fix plan (for the continuation timer / next session)
1. Currency-normalize every row (the ULVR/DGE verification method,
   scripted): NI currency vs cap currency, convert before dividing.
2. NI for US-listed names via SEC XBRL where they file 20-Fs (NVO, ASML,
   TSM, UL, RELX, DEO, MELI, FMX all file with the SEC — companyfacts
   works!) — the reliable path, same as the S&P batches.
3. Re-run; then distance-to-line radar goes global for real.

## v1 UPDATE (same day): 15/40 priced, radar operational
Fix executed: XBRL (us-gaap+ifrs-full merged) for the 9 SEC 20-F filers +
Zacks caps + currency normalization everywhere. Full table in
`2026-07-17 Watchlist Pricing v1.csv`. Distance-to-line, nearest first:
**UL −6%** · NVO −24% · DEO −29% · RELX −43% · LRLCY −46% · ATLKY −55%
(artifact corrected) · HESAY −67% · IDEXY −74% · RACE −75% · LNSTY −77% ·
ASML −78% · TSM −81% · FMX −95% · MELI −99% · RBGLY −103% (neg. worst yr).
Remaining 25: unsponsored ADRs with no free financials tables — a
structural data gap (macrotrends per-name backoff is the known slow path).
Radar conclusion: **Unilever is the global quality name to watch weekly;
Novo and Diageo quarterly; the rest are doing what quality does — being
expensive.**
