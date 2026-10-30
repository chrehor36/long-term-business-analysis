# RCON research notes (2026-10-16)
Started: template copied before any fetch (commit 59629c95).

## Sources fetched (SEC EDGAR, User-Agent Chris Hrehor chrehor36@gmail.com); raw text under cache/ (gitignored)
- 20-F FY2026 (period 2026-06-30), filed 2026-09-30, acc 0001104659-26-112415
- 20-F FY2025 acc 0001104659-25-099502; FY2024 acc 0001410578-24-001721; FY2023 acc 0001410578-23-002152;
  FY2022 acc 0001410578-22-002904; FY2021 acc 0001104659-21-139057; FY2020 acc 0001104659-20-113968; FY2019 acc 0001144204-19-046766
- 6-K 2026-04-16 (PIPE) acc 0001104659-26-044442; 6-K 2026-05-06 (Nasdaq notice) acc 0001104659-26-056297;
  424B5 2026-07-29 acc 0001104659-26-088067; 6-K 2026-07-31 (ATM sales agreement) acc 0001104659-26-089038;
  6-K 2026-08-13 (1-for-200 consolidation) acc 0001104659-26-096022; 6-K 2026-09-18 (Nasdaq compliance) acc 0001104659-26-108775
- XBRL companyfacts CIK 1442620 (transcription; one figure cross-checked: FY2026 operating cash flow -58,801,965 RMB, XBRL = filed statement)
- Rivals named in the 20-F (Item 3.D): Honeywell (CIK 773840), Emerson (CIK 32604), Rockwell Automation (CIK 1024478) XBRL; Schneider Electric and Siemens do not file with the SEC.
- Sovereign: MoF PRC China government bond yield curve (财政部-中国国债收益率曲线, hosted at yield.chinabond.com.cn/cbweb-czb-web, 主办单位 中华人民共和国财政部), 30-year 2.07% on 2026-10-15 (sov.txt)
- Price: Yahoo chart (aggregator, live quote only): close 1.05 USD 2026-10-15 (price_tail.txt)

## Tools
- tools/run.py RCON refused: earnings CNY, quote USD; no CNY sovereign configured. Figures taken by hand from the 20-Fs.
- Screens/cover_shares.py RCON: 353,154 A + 20,000,000 B at 2026-06-30 (20-F cover). Class B converts 1/3,600 of a Class A and carries dividend rights at that ratio (Note 2, EPS policy).

## Scripts here
fetch.py, facts.py, bs.py, rivals.py, owner_cash.py (outputs *_out.txt), row.py (ledger lookup), check_cites.py (citation check).
