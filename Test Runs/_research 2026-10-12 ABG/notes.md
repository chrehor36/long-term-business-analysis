# ABG research notes
Opened 2026-10-12. Template copied before any fetch.

## Step 0 facts (2026-10-12)
- Price 165.28 USD, 2026-10-12, aggregator live quote via tools/run.py (flagged).
- Shares 17,951,917 cover of 10-Q filed 2026-07-31, acc 0001144980-26-000094 (cover_shares.py). BS 6/30/2026 issued count 40.099M incl treasury.
- Sovereign USD 30y par 5.60%, 10/09/2026, US Treasury (tools/sources.py).
- 10-K FY2025 acc 0001144980-26-000051 (filed 2026-02-20); 10-Q Q2 2026 acc 0001144980-26-000094; DEF 14A acc 0001144980-26-000070; 8-Ks since 10-Q: 0001144980-26-000096 (CHRO exit), -000098 (new CHRO), -000100 (consulting agreement).
- Cross-check: OCF 2023 313.0 run.py = filed cash-flow statement 313.0 (10-K FY2025).
- Lines of evidence chosen: Item 1 (business, competition, franchise laws, acquisitions/divestitures), Item 1A (manufacturer dependence, EV/autonomy, debt, FTC, impairments), Item 7 (results, floor plan cash-flow classification and adjusted CFO, capex, buybacks, impairments).
- Rivals named by the 10-K: Item 5 peer index AutoNation, Sonic, Group 1, Penske, Lithia; Item 1A names Carvana. Chosen: AN, GPI, LAD.
## Field returns: see field_returns.py output (XBRL transcription; pre-tax EBIT after floor plan interest over net tangible capital).
## Adjusted CFO (filer non-GAAP, reconciled in each 10-K): 2014 193.2, 2015 118.9, 2016 260.3, 2017 195.6, 2018 181.6, 2019 155.1 old def / 282.3 new def, 2020 442.6, 2021 632.1, 2022 987.0, 2023 705.3, 2024 688.4, 2025 651.4.

## Close (2026-10-12)
- Box: OUT at Q7 (no case earns the floor at $165.28). Range central $7.39 (default pair, no-growth alone); organic $332.50 beside; fair price $102.33 (organic pair, labelled); equity-only $244.70.
- tools/check_framework.py: PASS (run before the closing commit).
- check_quotes.py on the run file: ids 99, adjacent fragments 33, failures 0, no E-ids.
- Em dashes: only in the template's headings and title line; none in the analyst's prose.
