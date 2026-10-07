
## UPDATE 2026-09-26 - USPH: Q2 OUT. U.S. Physical Therapy sells a visit at a price Medicare and the insurers set, and the price was $105.92 in 2010 and $105.76 in 2025; it is the best operator of the three SEC filers in its field.

**U.S. Physical Therapy, Inc. (USPH), wave 7 name 42, register entry 174.** Run file `Test Runs/2026-09-26 Run - USPH U.S. Physical Therapy.md`.
CIK 0000885978. Price $84.84 (NYSE close 2026-09-25, aggregator, flagged) x 14,922,698 shares (10-Q cover for 2026-06-30,
`0001140361-26-031825`) = cap $1,266.0M; sovereign 5.49% (US Treasury, 30 Yr, 09/25/2026). **Q1 IN, Q2 OUT on the
business.** No earlier note in this file mentions USPH; this is its first run.

### The finding
- **The price is not the company's.** 35.8% of FY2025 patient revenue is Medicare or Medicaid on the government's fee
  schedule, cut in each year 2021-2025; the rest is paid at rates *"stipulated in the payor contracts"*. The registrant
  calls its field *"highly competitive"* and *"highly fragmented with no company having a significant market share
  nationally"*, and names hospital departments, private clinics, physician-owned clinics and chiropractors as competitors.
  [E3-03] criteria (2) and (3) fail on the filing itself.
- **The physical series is the verdict [E4-55].** Net patient revenue per visit, from each 10-K's own table: $96.49
  (2005), $105.92 (2010), $105.83 (2013), $105.18 (2016), $105.90 (2019), $102.80 (2023), $105.76 (2025). Fifteen years
  without a nominal price increase, while salaries per visit rose $57.54 to $62.04 and the clinics were made to see 32.2
  patients a day instead of 20.5. Operating margin 15.7% to 11.1%.
- **The roll-up in the denominator**: goodwill and intangibles $158.4M (2013) to $865.3M (2025); the pretax return on
  capital including them fell 21.1% to 16.4% to 9.6%, while the return on the tangible capital a clinic needs stayed at
  150-215%. The operators do very well on what they run; the owner earns less and less on what he paid.
- **[E4-23] is the business model**: each clinic's partner-therapist holds the physician referrals, under a non-compete
  of up to two years, and is bought out on a put *"at a predetermined multiple of earnings performance"*. 45 owned clinics
  closed in 2024 and 23 in 2025.
- **Peers**: Select Medical's outpatient segment ($100-104 a visit, 7.0-14.5% segment Adjusted EBITDA margin) and ATI
  ($106-113 a visit, operating margin -3.9% and +0.3% in 2023-24). Both have since left the SEC (ATI's Form 15 in March
  2025, Select Medical's in July 2026 after a going-private). USPH beat both in every year shown; recorded as the strongest
  evidence against, and answered by [E3-43]'s "a business" and [E2-37]'s remarkable textile company.

### Beneath the close
- **Owner earnings for a USPH shareholder come after the partners.** Consolidated operating cash is 100% of every clinic;
  the partners took $14.7-19.3M a year in distributions 2018-2025 (31.8% of 2025 net income). After them, and with SBC
  (complete) and the (c) band: **$31.7-38.5M on the five-year window FY2021-25 (2.50-3.04% of the cap)**, $34.7-38.9M over
  ten years; after net buyouts of partners, shown apart, $17.3-24.1M. At the ~10% floor with no growth about $21-26 a
  share, at the sovereign about $39-47, against $84.84 (computation only).
- **Incentives [E4-27]**: the CEO's objective bonus and restricted stock vested on Adjusted EBITDA of $88-95M; the proxy
  reports $95,010,000, $10,000 over the top. Guidance is in Adjusted EBITDA ([E4-29] fires). A 2017 restatement of the
  partner-interest accounting (2012-2015) with a material weakness. No finding of personal misconduct.

### What the reading list should carry forward
- **A partnership roll-up has to be read net of the partners before any yield is printed.** The screen's $49-59M and
  `run.py`'s $51-59M are consolidated. This will recur at every name with material non-controlling interests.
- **Search stripped filings with whitespace normalised.** A plain grep for "per visit" in the 2026 10-Q returned nothing
  because the phrase was broken across lines; the metric had been renamed and widened, not dropped. The near-miss would
  have been a false [E2-49] finding.
- **Next dates**: CMS's final 2027 Medicare fee schedule (customarily November); the FY2026 10-K with the first full year
  of hospital-affiliated clinics under the widened revenue-per-visit definition. Neither can move the price-setter.

### Priors refuted or confirmed
- `deal_note`: half confirmed; one credit agreement and one CFO employment agreement, not an offering; no deal.
- `acq_note` ($322M in the window): confirmed, $322.0M over 2021-2025, growth bought while the owned base was flat.
- `spread_caveat`: acted on; 3, 5, 10 and 18-year windows rebuilt; the spread across recent windows is narrow.
- `level_shift` (no step): consistent; 2020-21 Relief Funds removed.

### Tooling defects (reported, not patched)
- **The screen and `run.py` never subtract non-controlling partners' cash** (distributions to non-controlling interests);
  for USPH that overstates owner earnings by a quarter to two-fifths.
- **The screen's `acq_note` omits purchases of partner interests** ($8.4-29.5M a year 2019-2025).
- **Multi-word greps on `fetch.py` output miss line-broken phrases**; normalise whitespace first.
