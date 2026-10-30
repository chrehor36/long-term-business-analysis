# Japan ADR/Common Mechanical Screen — 2026-07-15
Same NI/mkt-cap method as the domestic screens, with adjustments made by
explicit user decision before running (see chat record):
1. **Scope**: Japan-domiciled companies trading OTC in the US were brought
   into scope even though the original mandate was "US companies" — the user
   added this file deliberately and chose to screen it.
2. **Hurdle**: uses the **Japan 30-yr JGB yield (3.76%, 2026-07-15) floored at
   4%** per the Statute's floor rule, not the US 30-yr Treasury — on the
   reasoning that a Japan-domiciled business's true sovereign comparison is
   its home government's bond, not the market where its ADR happens to trade.
   (Independently corroborated by a 2026-07-14 test run in this same project
   that used the JGB rate for SONY/NTDOY — this wasn't a new departure.)
3. **Currency fix**: stockanalysis.com quotes market cap in USD but Net
   Income in millions of home-currency (confirmed JPY). The script detects
   the currency caption per ticker and converts NI to USD at spot (162.20
   JPY/USD, 2026-07-14) before computing yield.

## Source
User-exported `JPN ADR and Common.csv` — 295 rows, Country=Japan. 278 ADRs +
17 direct common-stock ordinaries. 292 of 295 are **Pink Limited** tier.

## Two-pass data collection
**Pass 1 (stockanalysis.com)**: only 4 of 295 tickers had a financials page —
a genuine coverage gap, not a bug (confirmed via direct 404s).

**Pass 2 (macrotrends.net follow-up)**: resolved **107 more** tickers (6s
pacing + a one-time 45s backoff-and-retry on Cloudflare challenges — this is
respectful rate-limiting, not fingerprint spoofing or challenge-solving).
Macrotrends reports NI already converted to USD, so no currency conversion
was needed for this batch.

**Combined coverage: 111 of 295 (37.6%)** — up from 4 of 295 (1.4%) in the
first pass. The remaining 184 simply aren't carried by either site (mostly
thinner-volume unsponsored ADRs and direct Japanese ordinaries) — flagged as
a residual gap, not reported as failures.

## Result: 32 of 295 pass the bare yield check (vs. 2 in the first pass)

| Symbol | Name | Mkt Cap ($M) | Lowest 5yr NI ($M) | Yield |
|---|---|---|---|---|
| NPNYY | Nippon Yusen KK | 13,400 | 1,398 | 10.43% |
| SKHSY | Sekisui House | 13,940 | 1,401 | 10.05% |
| ISUZY | Isuzu Motors | 9,830 | 887 | 9.02% |
| DIFTY | Daito Trust Construction | 6,710 | 527 | 7.85% |
| DNPLY | Dai Nippon Printing | 8,320 | 640 | 7.69% |
| HTCMY | Hitachi Construction Machinery | 7,080 | 483 | 6.82% |
| ITOCY | **Itochu Corp** | 91,840 | 5,295 | 5.77% |
| SGIOY | Shionogi & Co | 15,200 | 1,016 | 6.68% |
| NCLTY | Nitori Holdings | 8,270 | 545 | 6.59% |
| MARUY | **Marubeni Corp** | 49,800 | 3,116 | 6.26% |
| BRDCY | Bridgestone Corp | 30,120 | 1,881 | 6.25% |
| KDDIY | KDDI Corp | 69,370 | 4,401 | 6.34% |
| KUBTY | Kubota Corp | 19,000 | 1,203 | 6.33% |
| OTSKY | Otsuka Holdings | 36,670 | 2,265 | 6.18% |
| MITSY | **Mitsui & Co** | 81,180 | 5,504 | 6.78% |
| SSUMY | **Sumitomo Corp** | 45,940 | 2,559 | 5.57% |
| SZKMY | Suzuki Motor Corp | 24,190 | 1,427 | 5.90% |
| NHNKY | Nihon Kohden | 1,590 | 93 | 5.85% |
| SUGBY | Suruga Bank | 1,380 | 71 | 5.14% |
| FUJHY | Subaru Corp | 10,890 | 600 | 5.51% |
| MZDAY | Mazda Motor Corp | 4,230 | 232 | 5.48% |
| RICOY | Ricoh Co | 5,280 | 270 | 5.11% |
| JAPAY | Japan Tobacco | 67,180 | 3,058 | 4.55% |
| FUJIY | Fujifilm Holdings | 26,490 | 1,302 | 4.91% |
| NDEKY | Nitto Denko Corp | 13,450 | 660 | 4.91% |
| MAURY | Marui Group | 3,310 | 158 | 4.77% |
| MTSUY | **Mitsubishi Corp** | 103,660 | 4,935 | 4.76% |
| CAJPY | Canon Inc | 23,420 | 1,056 | 4.51% |
| UNICY | Unicharm Corp | 10,160 | 437 | 4.30% |
| FJTSY | Fujitsu Ltd | 35,770 | 1,451 | 4.06% |
| IPXHY | Inpex Corp | 25,860 | 1,939 | 7.50% |
| SOMLY | Secom Co | 16,470 | 703 | 4.27% |

## Headline finding: all five of Berkshire's sogo shosha holdings pass
Buffett has publicly built stakes in five Japanese general trading companies
since 2020: **Mitsubishi Corp, Mitsui & Co, Itochu, Marubeni, and Sumitomo
Corp**. All five appear in this file, and **all five clear the bare yield
check** against the JGB-floor hurdle (4.76%–6.78% vs. 4.00%) — a genuinely
relevant confirmation, not an arbitrary hit, though a bare mechanical pass is
not a framework verdict; none of these have been run gate-by-gate.

## What this screen does NOT tell us
For 184 of 295 companies there was no data from either source — not a "fail,"
an unscreened gap. Coverage skews toward larger/more liquid names (all five
sogo shosha, most auto/electronics majors); many mid-tier Pink Limited names
remain unresolved.

## Net result
32 mechanical passes, headlined by the sogo shosha basket. **Mitsubishi Corp
already flagged for deeper research** in `Screens/SURVIVORS - Non-Bank
Candidates Awaiting Full Gate Run.md`; the other four sogo shosha plus the
remaining 27 passes are unreviewed pending user direction.
