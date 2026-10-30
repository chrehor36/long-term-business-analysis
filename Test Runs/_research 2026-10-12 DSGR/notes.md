# DSGR run notes (2026-10-12)

Working notes for the run of record. Template copied before any fetch.

## Files in this folder
- fetch.py: fetch an EDGAR document into cache/f (gitignored) with a wrapped text copy.
- grab.py: print windows around regex matches in a cached text file.
- rows.py: print v5 ledger rows by id.
- peers.py: peer revenue and operating income from SEC companyfacts (FAST, MSM, GWW), cached in cache/peers.
- q7_computation.py and q7_output.txt: the Q7 arithmetic, COMPUTATION, NOT A CLEARANCE.
- check_run.py: the citation check (no E-ids; every id in the ledger; every quoted fragment beside an id in that row).

## Working facts
- Reverse acquisition 2022: TestEquity + Gexpro Services the accounting acquirer; Lawson from 2022-04-01 only.
- Gexpro Services decides under the business-of-parts convention: five-year segment operating income 144.7 of 276.8
  on the combined basis (52.3%), 57.3% on the as-reported basis.
