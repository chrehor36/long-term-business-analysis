# S&P 500 Mechanical Screen — 2026-07-15
Same NI/mkt-cap-vs-hurdle method as the other screens, applied to the full
S&P 500 (not the OTC/foreign universe the rest of this project has focused
on) — a different exercise: checking whether any current S&P 500 members
screen statistically cheap against a bond-yield hurdle, not "undiscovered
small caps."

## Source correction
The user's first export (`sp500_constituents.csv`, 49 rows) turned out to be
a "recently added to the index" subset (Date First Added spanning 2023-10-18
to 2026-06-29), not the full ~500-company roster. Replaced by pulling
Wikipedia's "List of S&P 500 companies" table directly (503 rows — a few
tickers carry dual share classes) and reformatting to the same column schema
so the existing script needed no changes.

## Data-source saga (why this took 3 attempts)
1. **First attempt** (stockanalysis.com alone, 0.6s pacing): corrupted by a
   concurrent ad-hoc test request I made against the same site while the
   background job was running — the collision tripped a block partway
   through (ticker ~26 of 503 onward, 100% failure).
2. **Second attempt** (same method, no concurrent collision this time):
   failed again, in the same way, starting even earlier (~ticker 10). This
   ruled out "collision" as the sole cause: stockanalysis.com's `/stocks/`
   path (regular exchange-listed tickers) has materially tighter bot
   protection than its `/quote/otc/` path, which had handled 500+ OTC
   tickers cleanly earlier in this same session at the same pacing.
3. **Third attempt (this one)**: rather than keep guessing at the right
   pacing for one site, the list was **split into three segments, each
   routed through a completely separate data source** so no single site
   absorbs the full request volume:
   - **Segment A** (167 tickers): SEC EDGAR's XBRL companyfacts API (NI,
     authoritative filed 10-K data, no bot-wall) + Finviz.com (market cap)
   - **Segment B** (167 tickers): Zacks.com (both NI and market cap)
   - **Segment C** (169 tickers): Barchart.com (both NI and market cap)

   All three ran concurrently without incident (different domains = no
   shared rate-limit risk). Result: **503/503 market caps (100%), 499/503
   Net Income histories (99.2%)** — a dramatic improvement over either single
   -source attempt, both of which failed outright.

## Result: 47 of 503 pass the bare yield check (9.3%)

| Symbol | Name | Sector | Mkt Cap ($M) | Yield |
|---|---|---|---|---|
| CHTR | Charter Communications | Communication Services | 18,180 | 25.07% |
| HPQ | HP Inc. | Information Technology | 22,520 | 11.23% |
| CTSH | Cognizant | Information Technology | 20,460 | 10.39% |
| LEN | Lennar | Consumer Discretionary | 20,170 | 10.30% |
| SYF | Synchrony Financial | Financials | 24,784 | 9.03% |
| DHI | D.R. Horton | Consumer Discretionary | 42,980 | 8.34% |
| PHM | PulteGroup | Consumer Discretionary | 23,727 | 8.20% |
| IT | Gartner | Information Technology | 8,900 | 8.19% |
| UHS | Universal Health Services | Health Care | 8,731 | 7.74% |
| NVR | NVR, Inc. | Consumer Discretionary | 17,218 | 7.18% |
| RF | Regions Financial | Financials | 26,387 | 7.17% |
| ACN | Accenture | Information Technology | 83,850 | 7.04% |
| HON | Honeywell | Industrials | 70,550 | 6.70% |
| APA | APA Corporation | Energy | 12,110 | 6.64% |
| ZTS | Zoetis | Health Care | 31,052 | 6.56% |
| VZ | Verizon | Communication Services | 177,336 | 6.55% |
| HCA | HCA Healthcare | Health Care | 80,660 | 6.50% |
| CMCSA | Comcast | Communication Services | 83,910 | 6.40% |
| EOG | EOG Resources | Energy | 73,510 | 6.34% |
| TROW | T. Rowe Price | Financials | 24,870 | 6.26% |
| TSCO | Tractor Supply | Consumer Discretionary | 16,022 | 6.22% |
| BF.B | Brown-Forman | Consumer Staples | 11,610 | 6.16% |
| LULU | Lululemon | Consumer Discretionary | 13,920 | 6.14% |
| ELV | Elevance Health | Health Care | 92,680 | 6.11% |
| BAC | Bank of America | Financials | 437,080 | 6.02% |
| AFL | Aflac | Financials | 61,590 | 5.92% |
| CDW | CDW Corporation | Information Technology | 16,720 | 5.91% |
| COP | ConocoPhillips | Energy | 135,790 | 5.88% |
| FOX | Fox Corp (Class B) | Communication Services | 20,800 | 5.79% |
| PYPL | PayPal | Financials | 41,785 | 5.79% |
| UPS | United Parcel Service | Industrials | 96,620 | 5.77% |
| REGN | Regeneron | Health Care | 69,365 | 5.70% |
| USB | U.S. Bancorp | Financials | 96,387 | 5.63% |
| SWKS | Skyworks Solutions | Information Technology | 8,510 | 5.61% |
| GEHC | GE HealthCare | Health Care | 28,050 | 5.59% |
| LOW | Lowe's | Consumer Discretionary | 116,450 | 5.53% |
| PNC | PNC Financial Services | Financials | 101,146 | 5.51% |
| AMP | Ameriprise Financial | Financials | 47,400 | 5.39% |
| DVN | Devon Energy | Energy | 49,520 | 5.34% |
| ADBE | Adobe | Information Technology | 89,260 | 5.33% |
| BLDR | Builders FirstSource | Industrials | 8,180 | 5.32% |
| GL | Globe Life | Financials | 13,900 | 5.32% |
| MTB | M&T Bank | Financials | 35,420 | 5.25% |
| WFC | Wells Fargo | Financials | 261,004 | 5.24% |
| FOXA | Fox Corp (Class A) | Communication Services | 23,060 | 5.23% |
| BBY | Best Buy | Consumer Discretionary | 17,990 | 5.15% |
| FDX | FedEx | Industrials | 74,840 | 5.11% |

CHTR's 25.07% is an outlier worth a sanity flag before anyone acts on it —
plausibly a real distressed-cable-sector read (heavy debt load, market cap
compressed) but worth confirming the NI figure isn't distorted by a one-time
item before trusting it at face value; not investigated further here since
this is a mechanical screen, not framework output.

## What this screen does NOT tell us
This is a **bare NI/mkt-cap yield check only** — no circle-of-competence,
moat, management, or Fortress Test review of any kind. Financial-sector names
here (SYF, RF, BAC, AFL, USB, PNC, WFC, MTB, GL, TROW, AMP) would need the
Ruling 2 hard leverage ceiling (10:1 assets/equity) applied before any of
them could even reach Gate 6 — none of that work is done here.

## Net result
47 passes across a real cross-section of sectors, several already
well-covered/analyzed mega-caps (Bank of America, Wells Fargo, Verizon,
Comcast) rather than obscure names — a different flavor of result than the
OTC/Japan screens, reflecting a fundamentally different, far-more-efficiently
-priced universe. None of these 47 have been run gate-by-gate.
