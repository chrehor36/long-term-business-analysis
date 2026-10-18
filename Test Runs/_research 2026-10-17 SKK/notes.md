# SKK / RNTZ run notes, 2026-10-17
- Template copied before any fetch (commit 2c482f5c).
- Raw filings are in cache/ (gitignored); fetch.py strips them to text; mas.py posts the MAS SGS form; ids.py prints ledger rows.

## Filings read (accessions)
- 20-F FY2025, 2026-04-10, 0001493152-26-016229 (auditor WWC, P.C., since 2025; reporting currency USD, functional SGD)
- 20-F FY2024, 2025-05-15, 0001641172-25-011043
- F-1, 2024-01-29, 0001493152-24-004123 (FY2021, FY2022, H1 2023)
- 6-K 2026-05-05 APA, 0001493152-26-021165 (ex10-1 APA filed as 101 page images; Schedule 1.1(a) not seen)
- 6-K 2026-06-05 EGM notice and proxy, 0001493152-26-027479 (ex99-3)
- 6-K 2026-06-24 EGM results, 0001493152-26-029899
- 6-K 2026-08-18 RDO (770,000 sh at $4.46, paid in USDT), 0001493152-26-039007
- 6-K 2026-08-19 contract awards, 0001493152-26-039241
- 6-K 2026-09-25 pro forma, 0001493152-26-044299 (ex99-1)
- 6-K 2026-10-13 closing, waiver, name change, 0001493152-26-046697
- 424B5 2026-05-18 (ATM $5.54M), 0001493152-26-024103; 424B5 2026-07-31 (ATM cut to $25,000; $201,983 sold), 0001493152-26-035691; 424B5 2026-08-14 (RDO; 2,105,332 A + 1,085,264 B outstanding), 0001493152-26-038282
- F-3 2026-05-05, 0001493152-26-021236; F-3/A 2026-05-13, 0001493152-26-022637
- S-8 2026-10-16 (6,000,000 sh, Rantizo 2026-2027 plan), 0001493152-26-047398
- 6-K 2026-04-01 (10:1 consolidation), 0001493152-26-014559; 6-K 2026-04-20 (Nasdaq delisting determination, then compliance regained), 0001493152-26-018044
- Form 4 Liao 0001493152-26-047232; Form 4 Ng 0001493152-26-047081; Form 4 Sze 0001493152-26-047072; Form 4 McInerney 0000919574-26-006971; Form 3 McInerney 0000919574-26-006969

## Share count build
- 3,190,596 (424B5 2026-08-14) + 770,000 (RDO 2026-08-17) + 51,966,591 + 2,409,300 + 2,000,000 (closing 2026-10-09) = 60,336,487
- check: pro forma's 67,930,983 = 2,448,679 + 41,917 ATM + 700,000 plan + 770,000 RDO + 58,958,998 + 2,733,485 + 2,277,904 (all at $4.39)
- pending, not counted: PIPE $10M (about 2,007,750 sh at $4.9807) and $10M capital raise, deferred to 2026-10-16; no 6-K reporting either by 2026-10-16

## Price and rates
- RNTZ $4.53 close 2026-10-16 (Yahoo chart, aggregator, live quote only; volume 8,200)
- SGS 30-year 2.41% on 2026-10-16 (MAS, SGS benchmark issues, average buying rates of SGS primary dealers)
- US Treasury 30-year 5.43% 2026-10-16 (tools/run.py, Treasury par curve)

## Owner cash, legacy business (US$000): OCF - SBC - capex + disposal proceeds - finance-lease principal
- 2021: 4,208 - 0 - 1,480 + 0 - 255 = 2,473
- 2022: 1,757 - 0 - 1,170 + 303 - 744 = 146
- 2023: 194 - 0 - 3,042 + 703 - 580 = -2,725
- 2024: 3,330 - 0 - 7,814 + 184 - 361 = -4,661
- 2025: -512 - 2,399 - 5,136 + 684 - 927 = -8,290
- average -2,611; depreciation variant (OCF - SBC - D&A) average -28; unlevered (+interest x 0.83): -2,383 and +201
