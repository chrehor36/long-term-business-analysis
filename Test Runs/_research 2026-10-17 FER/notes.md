# FER run notes 2026-10-17

## Step 0 facts (2026-10-17)
- Price: FER Nasdaq close 2026-10-16 $49.41 (Yahoo chart via tools/sources.py; AGGREGATOR, live quote only). EURUSD 1.1244 (Yahoo, aggregator) 2026-10-16. Price path: ~$68 June 2026 -> $49.41.
- Sovereign EUR 30y 3.67% 2026-10-15, ECB AAA curve SR_30Y (tools/sources.py).
- tools/run.py FER: "no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." -> arithmetic by hand.
- cover_shares: 720,626,181 outstanding at 2025-12-31 (20-F 0001628280-26-011789 cover).
  Treasury 13,129,191 at 12/31/25 -> issued 733,755,372. 2026: cancelled 4,200,000 (6-K 2026-03-11); treasury at 6/30/26 8,423,217 (H1 report 6-K 0001628280-26-050224 note 6) -> outstanding 721,132,155 at 6/30/26.
- Subsequent: I-24 SE Choice Lanes commercial close 2026-09-30 ($9.2bn construction cost, 50-yr concession, service 2034, financial close July 2027; consortium DriveTN w/ Transurban, Tikehau) 6-K 0001468522-26-000069 / 0001628280-26-064744. I-285 East selected 2026-10-15 ($8.9bn construction value, Phase 1 21 miles, w/ Tikehau) 6-K 0001468522-26-000075.
- H1 2026: ex-infra net debt EUR -1,307M (net cash); infra project net debt 7,591M (Highways 7,114). Dividends from projects H1 378M.
- q7.py: owner cash series and range arithmetic; row.py: prints ledger rows. Raw filings in cache/ (gitignored htm/pdf; txt conversions too large are not committed).
