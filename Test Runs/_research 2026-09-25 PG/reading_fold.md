
## UPDATE 2026-09-25 - PG: all four business gates IN, quit on at the floor. Procter & Gamble is a narrow franchise priced at a 4.0-4.2% owner-earnings yield against a 5.47% bond.

**The Procter & Gamble Company (PG), wave 7 name 40.** Run file `Test Runs/2026-09-25 Run - PG Procter & Gamble.md`. CIK
0000080424. Price $145.68 (NYSE close 2026-09-24, aggregator, flagged) x 2,391.1M shares as converted (2,324,433,060 common
from the FY2026 10-K cover, `0000080424-26-000103`, plus 66.6M ESOP preferred convertible one-for-one) = cap $348.3bn;
sovereign 5.47% (US Treasury, 30 Yr, 09/24/2026). **Q1 IN, Q2 IN (NARROW), Q3 IN (overlay), Q4 IN, Q5 QUIT ON.** Earlier
notes in this file carry PG only as a peer in the CL and CLX rows; this is its first run as a subject.

### The finding
- **The franchise is real and narrow.** In FY2022-24 P&G took seventeen points of price and still made net share gains in all
  five segments; pre-tax returns on net tangible operating assets ran 78-92% for six years; its five-year GAAP operating margin
  (22.7%) is the highest in a fourteen-company row that includes Unilever, Colgate, Kimberly-Clark, Henkel, Essity and L'Oréal.
- **But the direction is not a moat widening every year.** The company's own segment-share sentences, read for fourteen
  years, show six years of losses everywhere (FY2013-18, including the razor price war and an $8.3bn write-down), six years of
  recovery, and slippage again in three segments in FY2025-26, with "competitive activity" named nine times in the latest 10-K.
  Units were flat for five years; the growth was price.
- **Some of the celebrated return is supplier credit**: payables went from 14.3% to 18.7% of sales, $6.2bn of it in
  supply-chain finance. The return was 40-50% before the stretch, still very high.
- **Owner earnings are $14.1-14.7bn on the default window** ($12.0-15.6bn across every window), SBC complete, (c) near total
  capex because capex has exceeded D&A in 17 of 18 years.
- **The price**: 4.0-4.2% yield, 1.2-1.4 points under the bond; with the filed 3-4.25% growth the expectancy is 7.0-8.5%;
  value at the floor about $85-110.

### What the reading list should carry forward
- **Two bands armed, $84.16 and $107.25**, each a prompt for a full re-run, void if a Q2 falsifier fires first. The FY2027 10-K
  (about August 2027) is the test of whether FY2025-26 is a cycle or a slip [E3-30].
- **The named death is #19 the shelf, the same shape the CL run named for Colgate**: PG and Colgate, both gate-clearers, share
  it, which suggests the shape belongs to branded staples sold through concentrated retailers rather than to either company.
- **The growth algorithm**: "mid-to-high single digits" Core EPS printed every year, 4.0% delivered. Watch whether the new CEO
  (Jejurikar, Chairman from 2026-08-01) keeps printing it; FY2027 was guided below it, the candid direction.

### Priors refuted or confirmed
- `oe_bottom_m` / `oe_top_m`: confirmed to the dollar. `spread_caveat`: acted on; the older windows are lower, not higher.
- `cap_m`: stale; and the cover count omits the convertible preferred (2.9% of the economic count).
- Empty `deal_note`: half right. No spread, but a $3.8bn Thorne purchase agreed 2026-08-04 sits only in the 10-K.
- `growth_required` 5.78%: confirmed. `vs_sovereign`: confirmed in sign, refuted in level at the re-struck 5.47%.

### Tooling defects (reported, not patched)
- `deal_note()` cannot see an acquisition that files no 8-K item (below the significance test): the fourth deal blind spot
  this week, the first on the buy side.
- `cover_shares.py` cannot see one-for-one convertible preferred that draws the common dividend.
- `peer_metrics.py` reads a non-total `Revenues` tag for PG FY2012-2014 (28,400; 29,200; 29,400); the run used
  `SalesRevenueNet`.
- `run.py` prices an intraday quote against the prior day's sovereign.
