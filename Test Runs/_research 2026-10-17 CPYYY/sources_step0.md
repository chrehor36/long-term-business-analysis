# Step 0 source extracts (CPYYY run, 2026-10-17)

## Sovereign (GBP), Bank of England
- BoE yield curve archive `latest-yield-curve-data.zip`, file "GLC Nominal daily data current month.xlsx", sheet "4. spot curve", 30-year nominal spot (zero-coupon) yield:
  2026-10-13 5.951; 2026-10-14 5.950; 2026-10-15 5.864 (latest published at fetch, 2026-10-17).
- BoE IADB series IUDLNPY (20-year nominal par yield): 2026-10-14 5.7225. IUDMNPY (10-year): 2026-10-14 5.383.
- UK DMO gilt reference prices (D10B export) refused the fetch with a captcha page (2026-10-17).

## FX, Bank of England IADB XUDLUSS (USD per GBP, spot)
- 2026-10-14 1.3160; 2026-10-15 1.3253 (latest published at fetch).

## Prices (aggregator, Yahoo Finance chart API, flagged per operator rule 5)
- CNA.L close 2026-10-16: 150.50p (2026-10-15 148.30p).
- CPYYY close 2026-10-16: $8.04 (2026-10-15 $7.90).
- Check: 4 x 150.50p x 1.3253 = $7.98, against the ADS close $8.04.

## Shares
- RNS "Total Voting Rights", 1 October 2026 (Investegate copy of the RNS): as at 30 September 2026 issued capital 5,064,902,964 ordinary shares of 6 14/81p, of which 445,410,114 in treasury, leaving 4,619,492,850 with voting rights.
- AR2025 note 26: 5,064,902,964 shares at 31 December 2025; 454,315,003 in treasury; 90.4m own shares in employee trusts.
- H1 2026 note: weighted average 4,536m for EPS (excludes trust and treasury shares).

## Tools
- `python tools/run.py CPYYY`: "CPYYY: not an SEC filer. Use the evidence ladder ... This is UNRESEARCHED, not UNKNOWABLE."
- `python Screens/cover_shares.py CPYYY`: "CPYYY NOT AN SEC REGISTRANT in the live ticker file".
