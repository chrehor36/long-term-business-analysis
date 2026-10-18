# OIS run notes 2026-10-16
- template copied before any fetch.
- fetch.py: EDGAR fetch helper (submissions list, document text into cache/).
- facts.py: XBRL companyfacts annual series (first-filed value per year).
- rivals.py: operating income / total assets for OIS, NOV, BHI/BKR, Tenaris.
- q7calc.py: COMPUTATION, NOT A CLEARANCE for the value range and fair price.
- rows.py: prints v5 ledger rows by id.
- Step 0, foundations, standing rule, Q1 written; Q1 IN.
- Q2 written; OUT (ordinary returns over the cycle).
- Close: box OUT at Q2; COMPUTATION range $5.95-$13.69 all-equity vs $7.94, fair $5.58 ($4.68 equity-only); check_ids.py 0 problems; check_framework PASS.
