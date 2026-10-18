# LHSW run notes (2026-10-13)
Working notes for the dispatched purchase run. Raw filings go in cache/ (gitignored).

## Filings read (all from EDGAR, CIK 2004024)
- 20-F FY2026 (FYE 2026-03-31), filed 2026-08-13, 0001213900-26-089090: Items 3.D, 4, 5, 6, 7, 15, 16F; F-pages, Notes 1-23.
- 20-F FY2025, filed 2025-08-15, 0001213900-25-077169 (fetched; FY2025 figures taken from the FY2026 comparatives).
- 424B4 IPO prospectus 2025-04-04, 0001213900-25-028729: balance sheets 2024-03-31 and 2023-03-31; FY2023 OCF -1,469,694.
- F-1 2024-05-10, 0001213900-24-041530: balance sheets 2023-03-31 and 2022-03-31; FY2022 revenue 949,341; FY2022 OCF +239,201;
  FY2023 OCF -1,478,638 (differs from the later prospectus by 8,944).
- 424B4 2026-09-03, 0001213900-26-096975: unit offering, share counts, dilution, competitors named, last sale $2.88 on 2026-09-01.
- 6-K 2026-07-02 (0001213900-26-075052), Form 4 and 13D/A 2026-07-02 (0001213900-26-075053, -075054): 2,400,000 Class B at $0.165.
- 6-K 2026-07-08 (0001213900-26-076354): bid price >= $1.00 from 2026-06-22 to 2026-07-06.
- 6-K 2026-09-04 (0001213900-26-097772) with warrant form ex 4.1 and press release ex 99.1.
- 6-K press releases 2026-06-08, 06-17, 06-24, 09-22 (0001213900-26-066491, -072296, -104073).
- 13D 2025-09-10 (0001213900-25-086527), 13D 2026-04-16 (0001213900-26-044806), 6-K 2026-04-15, 6-K 2025-11-07.

## Cross-check (operator rule 4)
Accounts receivable, net, 2026-03-31: filed balance sheet $14,978,869 (F-3); tools/run.py XBRL 14,979 thousand. Match.
Net cash used in operating activities FY2026: filed $(8,966,396); run.py -9.0 million. Match.
