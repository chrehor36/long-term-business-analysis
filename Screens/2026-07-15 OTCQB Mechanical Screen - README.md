# OTCQB Mechanical Screen — 2026-07-15
Same method as the OTCQX screen (see that folder's README): NI (lowest of last
5 fiscal years, rough OE proxy) ÷ market cap vs. the US 30-yr hurdle. **This is a
screen, not framework output.**

## Source
User-exported `OTCQB.csv` — 120 companies, Tier=OTCQB, Country=USA, Sec
Type=Common Stock. OTCQB is the "Venture Market" tier — one step below OTCQX,
generally earlier-stage/smaller/less consistently profitable companies.

## Result: only 5 of 120 clear the bare yield check (vs. 34 of 157 on OTCQX)
The hit rate is roughly a quarter of OTCQX's — expected, given OTCQB's lower
listing bar. 114 of the 120 failures were **unprofitable on their worst of the
last 5 years** (many deeply so — biotech, mining, early-stage tech; 15 tickers
had no data coverage at all).

| Symbol | Mkt Cap ($M) | Lowest 5yr NI ($M) | Yield | Name |
|---|---|---|---|---|
| FMCC | 17,650 | 9,327 | 52.8% | **Freddie Mac** |
| FNMA | 36,330 | 12,923 | 35.6% | **Fannie Mae** |
| FBPA | 32.7 | 2.71 | 8.3% | Farmers Bank of Appomattox (VA) |
| CHBH | 123.5 | 10.06 | 8.2% | Croghan Bancshares (OH) |
| NIDB | 55.9 | 4.26 | 7.6% | Northeast Indiana Bancorp (IN) |

## Why none of these move to full gate-by-gate treatment right now

**FBPA, CHBH, NIDB are community banks** — same category the user asked to hold
per the OTCQX batch decision. Not run.

**FMCC and FNMA are not ordinary companies, and the screen result for them is
close to meaningless as stated.** Both are congressionally-chartered mortgage
GSEs that have been in federal conservatorship since 2008. The huge apparent
yields (35–53%) are an artifact of comparing market cap to CONSOLIDATED net
income — but common shareholders sit **behind** Treasury's senior preferred
stock (a liquidation preference now in the hundreds of billions combined) and
government warrants for 79.9% of common equity. Most of that reported net income
does not economically belong to common holders under the current arrangement.
Valuing GSE common stock is a specialized, politically-contingent special
situation (conservatorship release/recap timing, litigation over the historical
"net worth sweep") that the framework's ordinary-operating-company assumptions
(Gates 1, 3, 4, 6 all implicitly assume a normal capital structure) do not fit
without substantial adaptation. **Flagged, not run — a genuine scope question
for the user, not a screen failure.**

## Net result
After excluding banks (per standing instruction) and flagging the GSE anomaly,
**this batch produced zero ordinary non-financial candidates** for full
gate-by-gate treatment — a real, honest result, not a data or method failure.
