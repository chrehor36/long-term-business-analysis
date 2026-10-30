# OTCID Mechanical Screen — 2026-07-15
Same method as the OTCQX/OTCQB screens (see those folders' READMEs): NI (lowest
of last 5 fiscal years, rough OE proxy) ÷ market cap vs. the US 30-yr hurdle
(5.10% + 2% micro-cap add-on where market cap < $300M). **This is a screen, not
framework output.**

## Source
User-exported `OTCID.csv` — 264 companies, Tier=OTCID, Country=USA, Sec
Type=Common Stock. OTCID ("Pink Current Information") sits one tier below
OTCQB — issuers report current information but don't meet OTCQB's bid-price/
financial-standard requirements for listing there.

## Result: 25 of 264 clear the bare yield check — and every single one is a bank
Higher hit rate than OTCQB (9.5% vs 4.2%) but lower than OTCQX (21.7%) — and the
composition answers its own question: OTCID is where hundreds of tiny community
bank and savings/thrift holding companies sit because they see no reason to
uplist. Of 264 tickers, roughly half the ticker list by name alone is some
variant of "…Bancorp / …Bancshares / …Financial Corp / Bank of…" — small-town
single-charter holding companies, often family- or community-controlled, that
trade a handful of shares a week.

| Symbol | Mkt Cap ($M) | Lowest 5yr NI ($M) | Yield | Name |
|---|---|---|---|---|
| WTBFB | 993.2 | 55.80 | 5.6% | WTB Financial Corp (Class B) — WA |
| RCBC | 624.8 | 44.48 | 7.1% | River City Bank (CA) |
| OXBC | 109.0 | 8.82 | 8.1% | Oxford Bank Corp (MI) |
| MFGI | 319.5 | 18.54 | 5.8% | Merchants Financial Group (MN) |
| MLGF | 213.4 | 19.60 | 9.2% | Malaga Financial Corp (CA) |
| HFBK | 69.1 | 5.13 | 7.4% | Harford Bank, Aberdeen (MD) |
| FFWC | 56.4 | 4.09 | 7.2% | FFW Corp (IN) |
| CEFC | 59.2 | 5.86 | 9.9% | Commercial National Financial Corp (MI) |
| CRZY | 17.0 | 1.28 | 7.5% | Crazy Woman Creek Bancorp (WY) |
| SEBC | 96.0 | 7.50 | 7.8% | Southern Banking Corp (GA) |
| PCLB | 38.6 | 4.07 | 10.6% | Pinnacle Bancshares (AL) |
| ANDC | 39.6 | 3.16 | 8.0% | Andover Bancorp (OH) |
| ORPB | 81.1 | 7.14 | 8.8% | Oregon Pacific Bancorp |
| LSFG | 66.9 | 4.88 | 7.3% | LifeStore Financial Group (NC) |
| MSBC | 307.9 | 18.72 | 6.1% | Mission Bancorp (CA) |
| MDVT | 39.9 | 3.15 | 7.9% | Middlebury National Corp (VT) |
| CNBZ | 32.7 | 3.00 | 9.2% | CNB Corp (MI) |
| JFWV | 31.4 | 3.04 | 9.7% | JSB Financial Inc (WV) |
| SFDL | 125.3 | 9.81 | 7.8% | Security Federal Corp (SC) |
| CYVF | 100.4 | 10.14 | 10.1% | Crystal Valley Financial Corp (IN) |
| BCSO | 80.9 | 6.74 | 8.3% | Bancorp Southern Indiana |
| PVBK | 48.7 | 3.59 | 7.4% | Pacific Valley Bancorp (CA) |
| SLRK | 86.0 | 11.09 | 12.9% | Solera National Bancorp (CO) |
| DENI | 51.4 | 4.43 | 8.6% | Denali Bancorp (AK) |
| CITZ | 84.4 | 10.26 | 12.2% | Citizens Bancshares Corp (SC) |

## Why none of these move to full gate-by-gate treatment right now
**All 25 are banks or thrift holding companies** — same category the user asked
to hold, applied consistently across all three screens to date (31 of 34 OTCQX
passers, 3 of 5 OTCQB passers, now 25 of 25 OTCID passers). No GSE-style or
other special-situation anomaly surfaced in this batch — the non-passing rows
were dominated by ordinary unprofitable-on-a-bad-year small caps (biotech,
mining, early-stage tech, a few shells), not another Fannie/Freddie-type case.

144 of 264 tickers had at least one data gap (mostly "financials page fetch
failed" — very thinly-traded OTCID names that stockanalysis.com doesn't carry
financials pages for). This is the highest no-data rate of the three screens,
consistent with OTCID being the thinnest-coverage tier.

## Net result
**Zero ordinary non-financial candidates** for full gate-by-gate treatment —
the cleanest (and starkest) version of the same result as OTCQB. Across all
three tiers screened so far (157 + 120 + 264 = 541 companies), the mechanical
screen plus the standing "hold banks" instruction has produced exactly two
non-bank, non-GSE survivors total: **Unit Corp (UNTC)** and **Gamco Investors
(GAMI)** — both already run gate-by-gate (UNTC: starter-size-at-most verdict;
GAMI: PASS/does-not-qualify per user override on accumulated red flags).
