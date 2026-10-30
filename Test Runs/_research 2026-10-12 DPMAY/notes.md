# DPMAY research notes (2026-10-12)
Working notes for the run file `Test Runs/2026-10-12 Run - DPMAY Diploma.md`. Downloaded documents go in `cache/` (gitignored).

## Step 0 sources (2026-10-12)
- Price DPLM.L 7,785p close 2026-10-09 (Yahoo chart API, aggregator). DPMAY $25.83.
- Shares: TVR 1 Dec 2025 = 134,317,398, no treasury; EBT 81,368 at 30 Sep 2025 (AR2025 note F). Used 134,236,030.
- Sovereign: BoE GLC nominal 30y spot 6.0481% on 2026-10-08 (latest-yield-curve-data.zip). Script boe_30y.py.
- Statements: raw pdftotext of AR2016..AR2025 statement pages; numbers in calc.py.
- Rivals: none named in AR2016..AR2025 (grep competitor/rival); used WESCO (CIK 929008), Graybar (205402), Applied Industrial (109563) SEC companyfacts, peers.py.
