# S&P 400 + 600 Mechanical Screen — 2026-07-16
Small/mid-cap expedition: the same NI/mkt-cap-vs-hurdle method as the
prior screens, applied to the S&P MidCap 400 + SmallCap 600 (1,003 names
from Wikipedia's constituent lists). **Hurdle = 6.10%** (5.10% US 30-yr +
the Statute's +1% small/mid size premium — a full point stiffer than the
S&P 500 screen faced).

## Method
- NI: SEC EDGAR XBRL companyfacts (authoritative filed data), lowest of
  the last 5 annual 10-K figures — range anchoring.
- Market caps: 3-way source split (Finviz / Zacks / Barchart), threaded.
- Banks excluded upfront per the standing rule (107 names, saved in
  `2026-07-16 SP400-600 - Banks Excluded.csv`).
- **Units bug caught post-run**: market caps came back in millions and
  were divided by 1e6 again, inflating yields ×1e6 ("509 passes"). Values
  were recovered exactly from the stored yield ratios and rescored
  (ManpowerGroup sanity-checked at $1.81B cap ✓). The saved CSV is the
  corrected version.

## Result: 49 of 881 with data pass (5.6%) · 15 no-data · 370 negative worst-year NI
The negative-NI count is the small-cap story in one number: 42% of this
universe couldn't show five straight profitable years — the screen's
range-anchoring discipline auto-rejects them.

Top passes (full list in the CSV): MAN 23.1%, WU 19.9%, VSNT 18.3%*,
BBWI 15.2%, ASO 12.9%, KBH 12.1%, HOG 12.0%, RDN 11.6%, ESNT 11.2%,
SBH 10.9%, ABG 10.6%, HRB 10.4%, LAD 10.3%, MTG 10.3%...

*VSNT (Versant) is the Comcast cable-networks spinoff (Jan 2026) — its
"5-yr history" is carve-out accounting, flag before trusting. EFOR
(16.0%) unrecognized/possible data artifact — verify before use.

## Cluster read (pre-gate impression, NOT framework output)
- **Homebuilders (6)**: KBH, MHO, TMHC, MTH, DFH, CCS — same cycle trough
  as the DHI/LEN/PHM/NVR batch; expect most to fail Gate 2 like LEN/PHM
  unless a specific structural claim exists.
- **Auto dealers (5)**: ABG, LAD, AN, GPI, PAG — scale/franchise-network
  economics, genuinely worth a gate-by-gate look.
- **Mortgage insurers/financials (RDN, ESNT, MTG, NMIH, RITM, SLM, AFG)**:
  Ruling 2 mechanical ceiling applies to all; RITM is a mortgage REIT
  (likely ceiling-fail territory).
- **Possible quality sleepers**: HRB (brand + recurring tax prep),
  BKE (high-ROE apparel, heavy insider ownership), AMSF (niche workers'
  comp), BBWI (real brand), CPB (Campbell's — brand staple at 8.7%),
  LZB/CRI (brands), G/EPAM (IT services — same AI bucket as ACN/CTSH).
- **E&P (4)**: MTDR, CRC, OVV, MGY — the APA/EOG/COP/DVN Gate 2 precedent
  says commodity price-takers fail the franchise test.

None of these 49 are framework output — this is a pre-filter. Gate-by-gate
runs to follow on whatever subset survives an initial quality triage.
