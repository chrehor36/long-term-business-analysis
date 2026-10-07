import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from _scratch_KMB_lib import build
A = {"K21":"KMB_10K_FY2021_2021-12-31.txt","K22":"KMB_10K_FY2022_2022-12-31.txt","K23":"KMB_10K_FY2023_2023-12-31.txt",
     "K24":"KMB_10K_FY2024_2024-12-31.txt","K25":"KMB_10K_FY2025_2025-12-31.txt","KQ":"KMB_10Q_2026-06-30.txt"}
T = r'''## Kimberly-Clark Corporation (KMB)

Transcription only. No judgment is expressed. Dollar amounts are in millions as filed unless stated. Line numbers in every "Source:" line are the 0-based line indices printed by `python g.py <file> --lines START END` (and by the g.py grep mode). Parentheses in quoted filing tables are negatives. In quoted table rows the filing uses a long dash as a nil marker; in my parsed tables that cell is written "nil".

### Documents used

| file | form | fiscal period end | filing date | accession |
|---|---|---|---|---|
| KMB_10K_FY2021_2021-12-31.txt | 10-K | 2021-12-31 | 2022-02-10 | 0000055785-22-000010 |
| KMB_10K_FY2022_2022-12-31.txt | 10-K | 2022-12-31 | 2023-02-09 | 0000055785-23-000012 |
| KMB_10K_FY2023_2023-12-31.txt | 10-K | 2023-12-31 | 2024-02-08 | 0000055785-24-000018 |
| KMB_10K_FY2024_2024-12-31.txt | 10-K | 2024-12-31 | 2025-02-13 | 0000055785-25-000013 |
| KMB_10K_FY2025_2025-12-31.txt | 10-K | 2025-12-31 | 2026-02-12 | 0001628280-26-007567 |
| KMB_10Q_2026-06-30.txt | 10-Q | 2026-06-30 | 2026-08-04 | 0001628280-26-052348 |

Source of the table above: peers\manifest_list.txt.

Aliases used in "source line" columns of parsed tables: K21 = KMB_10K_FY2021_2021-12-31.txt, K22 = KMB_10K_FY2022_2022-12-31.txt, K23 = KMB_10K_FY2023_2023-12-31.txt, K24 = KMB_10K_FY2024_2024-12-31.txt, K25 = KMB_10K_FY2025_2025-12-31.txt, KQ = KMB_10Q_2026-06-30.txt.

**Segment structures as filed (comparable scope).**

- FY2021, FY2022, FY2023 10-Ks: three segments, Personal Care, Consumer Tissue, K-C Professional. Personal Care is the comparable segment used below.
- FY2024 10-K: re-segmented in Q4 2024 into North America (NA), International Personal Care (IPC), International Family Care and Professional (IFP), with 2023 and 2022 recast. There is no longer a "Personal Care" segment; per the segment descriptions, NA includes both personal care and family care/professional products, and IPC consists of Baby & Child Care, Adult Care and Feminine Care outside North America. The segments are used as filed.

@@S K24 417 <<As part of the 2024 Transformation Initiative>> <<International Family Care and Professional ("IFP").>>@@

@@S K24 417 <<Segment results for the historical periods presented>> <<recast to reflect these changes.>>@@

- FY2025 10-K and 2026 10-Q: IFP is reported as discontinued operations for all periods presented; continuing operations have two segments, NA and IPC. All FY2025 10-K consolidated figures (including re-presented 2024 and 2023) are continuing operations only, so they are not on the same basis as the FY2021 to FY2024 10-K consolidated figures.

@@S K25 134 <<As a result, the results of the IFP Business are reported as discontinued operations>> <<for all periods presented.>>@@

@@S K25 139 <<As a result of the IFP Transaction discussed above>> <<International Personal Care ("IPC").>>@@

@@S KQ 649 <<On July 1, 2026, all consultation requirements>> <<subject to certain post-closing adjustments.>>@@

### 1. Organic sales decomposition

Company labels: "Volume", "Net Price", "Mix/Other" (three separate components), "Currency" (FY2021 to FY2023) or "Currency Translation" (FY2024 onward), "Acquisition/Exited Businesses" (FY2021), "Exited Business" (FY2023), "Divestitures and Business Exits" (FY2024 onward), "Total", "Organic". Signs: parentheses = negative, as filed. The column ORDER changes in FY2024: FY2021 to FY2023 order is Volume, Net Price, Mix/Other; FY2024 onward order is Volume, Mix/Other, Net Price.

**FY2021 10-K (2021 vs 2020), total company.** Extraction artefact: the net sales percent-change table and the adjusted operating profit percent-change table are printed side by side on the same lines, and several row labels are split from their values onto the previous line. The first "Percent Change" column belongs to Net Sales.

@@L K21 505@@

@@L K21 506@@

@@L K21 507@@

@@L K21 508@@

@@L K21 509@@

@@L K21 510@@

@@L K21 511@@

@@L K21 513@@

@@L K21 514@@

@@L K21 515@@

@@L K21 517@@

@@L K21 518@@

@@L K21 520@@

@@L K21 523@@

@@S K21 396 <<Net sales of $19.4 billion increased 2 percent.>> <<increased sales approximately 1 percent.>>@@

**FY2021 10-K, Personal Care segment** (same side-by-side layout; first percent column is Net Sales).

@@L K21 539@@

@@L K21 541@@

@@L K21 542@@

@@L K21 543@@

@@L K21 544@@

@@L K21 545@@

@@L K21 547@@

@@L K21 548@@

@@L K21 549@@

@@L K21 551@@

@@L K21 552@@

**FY2022 10-K (2022 vs 2021), total company.** Same side-by-side layout. There is no acquisition/exits column in this table.

@@L K22 523@@

@@L K22 525@@

@@L K22 526@@

@@L K22 527@@

@@L K22 528@@

@@L K22 530@@

@@L K22 531@@

@@L K22 534@@

@@L K22 535@@

@@L K22 537@@

**FY2022 10-K, Personal Care segment.**

@@L K22 550@@

@@L K22 555@@

@@L K22 556@@

@@L K22 557@@

@@L K22 558@@

@@L K22 559@@

@@L K22 560@@

@@L K22 562@@

@@L K22 563@@

@@L K22 566@@

@@L K22 567@@

The Personal Care table has no acquisition column, but the North America Personal Care narrative states an acquisition effect:

@@S K22 572 <<The acquisition of Thinx increased sales by 1 percent.>> <<in 2022.>>@@

**FY2023 10-K (2023 vs 2022), total company.** Header split across three lines (extraction artefact).

@@L K23 514@@

@@L K23 515@@

@@L K23 516@@

@@L K23 518@@

@@L K23 529@@

@@L K23 532@@

**FY2023 10-K, Personal Care segment.**

@@L K23 546@@

@@L K23 547@@

@@L K23 549@@

@@S K23 563 <<Net sales of $10.7 billion increased 1 percent>> <<decreased sales by approximately 5 percent.>>@@

**FY2024 10-K (2024 vs 2023), total company.**

@@L K24 473@@

@@L K24 474@@

@@L K24 475@@

@@L K24 477@@

@@L K24 479@@

@@L K24 480@@

@@S K24 481 <<Excluding these items, organic growth was 3.2%>> <<across all three reportable segments.>>@@

**FY2024 10-K, recast segments (2024 vs 2023, and 2023 vs 2022 recast).**

@@L K24 503@@

@@L K24 504@@

@@L K24 505@@

@@L K24 507@@

@@L K24 508@@

@@L K24 509@@

@@L K24 510@@

@@L K24 511@@

@@L K24 512@@

@@L K24 513@@

@@L K24 514@@

International Personal Care segment narrative, FY2024 10-K:

@@S K24 552 <<Organic sales benefited from higher net selling prices of 7.8%>> <<led by China.>>@@

**FY2025 10-K (2025 vs 2024), continuing operations, total company.**

@@L K25 576@@

@@L K25 577@@

@@L K25 578@@

@@L K25 580@@

@@L K25 583@@

@@L K25 584@@

**FY2025 10-K, segments (NA and IPC, continuing operations).**

@@L K25 611@@

@@L K25 612@@

@@L K25 613@@

@@L K25 615@@

@@L K25 616@@

North America segment narrative (K25 line 627 heading "North America"):

@@S K25 632 <<Organic sales increased 1.8% primarily from volume gains of 2.6%>> <<lower pricing and mix.>>@@

International Personal Care segment narrative (K25 line 637 heading "International Personal Care"):

@@S K25 642 <<Organic sales benefited from volume and mix gains of 2.3% and 1.3%>> <<partially offset by lower pricing.>>@@

**10-Q for the quarter and six months ended 2026-06-30 (continuing operations).**

@@L KQ 708@@

@@L KQ 709@@

@@L KQ 710@@

@@L KQ 712@@

@@L KQ 713@@

@@L KQ 716@@

@@L KQ 750@@

@@L KQ 754@@

@@L KQ 755@@

@@L KQ 756@@

@@L KQ 757@@

@@L KQ 758@@

@@L KQ 759@@

**Parsed table (percent change vs prior year, as filed).**

| year | scope | reported net sales growth | organic | volume ("Volume") | price ("Net Price") | mix ("Mix/Other") | FX | acq/div | other | label wording used | source line |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY2021 | Total company | +2 | (1) | (4) | +2 | +1 | +1 ("Currency") | +1 ("Acquisition/Exited Businesses") | nd | Volume / Net Price / Mix/Other / Currency | K21 lines 507-518 |
| FY2021 | Personal Care | +10 | +6 | +2 | +2 | +2 | +1 | +3 | nd | same | K21 lines 541-552 |
| FY2022 | Total company | +4 | +7 | (3) | +9 | +1 | (4) | no column | nd | same | K22 lines 525-535 |
| FY2022 | Personal Care | +3 | +7 | (3) | +8 | +2 | (3) | no column (narrative: Thinx +1 in NA Personal Care, K22 line 572) | nd | same | K22 lines 557-567 |
| FY2023 | Total company | +1 | +5 | (2) | +6 | +1 | (3) | (1) ("Exited Business") | nd | same | K23 line 518 |
| FY2023 | Personal Care | +1 | +5 | (1) | +5 | +1 | (5) | no column | nd | same | K23 line 549 |
| FY2024 | Total company | (1.8) | +3.2 | +0.8 | +1.9 | +0.4 | (3.8) ("Currency Translation") | (1.2) ("Divestitures and Business Exits") | nd | Volume / Mix/Other / Net Price (order changed) | K24 line 477 |
| FY2024 | NA | +0.2 | +1.1 | +0.5 | +0.1 | +0.5 | (0.1) | (0.8) | nd | same | K24 line 508 |
| FY2024 | IPC | (3.1) | +9.2 | +0.9 | +7.8 | +0.5 | (12.2) | (0.1) | nd | same | K24 line 509 |
| FY2024 | IFP | (5.9) | (0.2) | +1.5 | (2.0) | +0.3 | (1.2) | (4.4) | nd | same | K24 line 510 |
| FY2023 recast | NA | +4.9 | +5.0 | +0.3 | +4.3 | +0.4 | (0.3) | +0.2 | nd | same | K24 line 512 |
| FY2023 recast | IPC | (2.6) | +5.3 | (4.2) | +7.9 | +1.6 | (7.9) | nil | nd | same | K24 line 513 |
| FY2023 recast | IFP | (2.9) | +2.8 | (7.6) | +9.3 | +1.1 | (1.8) | (3.9) | nd | same | K24 line 514 |
| FY2025 (continuing ops) | Total company | (2.1) | +1.7 | +2.5 | (0.9) | +0.1 | (0.9) | (2.9) | nd | same | K25 line 580 |
| FY2025 | NA | (2.4) | +1.8 | +2.6 | (0.4) | (0.5) | (0.2) | (3.9) | nd | same | K25 line 615 |
| FY2025 | IPC | (0.9) | +1.7 | +2.3 | (2.0) | +1.3 | (2.3) | (0.2) | nd | same | K25 line 616 |
| Q2 2026 (3 months) | Total company | +0.6 | (0.1) | (0.1) | (0.5) | +0.4 | +1.1 | (0.4) | nd | same | KQ line 712 |
| H1 2026 (6 months) | Total company | +1.6 | +1.2 | +1.3 | (0.5) | +0.4 | +1.5 | (1.1) | nd | same | KQ line 713 |
| Q2 2026 | NA | (1.2) | (0.7) | (0.3) | (0.7) | +0.2 | +0.1 | (0.5) | nd | same | KQ line 755 |
| Q2 2026 | IPC | +4.0 | +1.0 | +0.3 | (0.2) | +0.9 | +3.1 | (0.1) | nd | same | KQ line 756 |
| H1 2026 | NA | (0.9) | +0.5 | +0.8 | (0.3) | nil | +0.2 | (1.6) | nd | same | KQ line 758 |
| H1 2026 | IPC | +6.5 | +2.5 | +2.2 | (0.8) | +1.2 | +4.1 | nil | nd | same | KQ line 759 |

Restatement note: the FY2023 Personal Care figures (FY2023 10-K) and the FY2023 recast NA/IPC/IFP figures (FY2024 10-K) are different segment definitions and are not substitutes for each other. The FY2024 10-K total-company figures include IFP; the FY2025 10-K figures exclude IFP (discontinued operations). The FY2025 10-K does not re-present a 2024-vs-2023 organic decomposition.

### 2. GAAP operating margin (and segment margin)

Caption used: "Operating Profit" (consolidated income statement, GAAP). Operating margin = Operating Profit / Net Sales, computed by me.

**Income statement rows as filed.**

@@L K21 747@@

@@L K21 748@@

@@L K21 749@@

@@L K21 750@@

@@L K21 753@@

@@L K22 757@@

@@L K22 758@@

@@L K22 759@@

@@L K22 760@@

@@L K22 763@@

@@L K23 733@@

@@L K23 734@@

@@L K23 735@@

@@L K23 736@@

@@L K23 740@@

@@L K24 769@@

@@L K24 770@@

@@L K24 771@@

@@L K24 772@@

@@L K24 776@@

@@L K25 843@@

@@L K25 844@@

@@L K25 845@@

@@L K25 846@@

@@L K25 850@@

@@L KQ 93@@

@@L KQ 94@@

@@L KQ 95@@

@@L KQ 96@@

@@L KQ 99@@

| year | basis | Operating Profit | Net Sales | GAAP operating margin (computed) | source line |
|---|---|---|---|---|---|
| FY2021 | total company, FY2021 10-K | 2,561 | 19,440 | 13.2% | K21 lines 748, 753 |
| FY2022 | total company, FY2022 10-K | 2,681 | 20,175 | 13.3% | K22 lines 758, 763 |
| FY2023 | total company, FY2023 10-K | 2,344 | 20,431 | 11.5% | K23 lines 734, 740 |
| FY2024 | total company, FY2024 10-K | 3,210 | 20,058 | 16.0% | K24 lines 770, 776 |
| FY2025 | continuing operations, FY2025 10-K | 2,351 | 16,447 | 14.3% | K25 lines 844, 850 |
| FY2024 re-presented | continuing operations, FY2025 10-K | 2,700 | 16,805 | 16.1% | K25 lines 844, 850 |
| FY2023 re-presented | continuing operations, FY2025 10-K | 1,928 | 17,146 | 11.2% | K25 lines 844, 850 |
| H1 2026 | continuing operations, 10-Q | 1,386 | 8,352 | 16.6% | KQ lines 94, 99 |
| H1 2025 | continuing operations, 10-Q | 1,223 | 8,217 | 14.9% | KQ lines 94, 99 |
| Q2 2026 | continuing operations, 10-Q | 633 | 4,189 | 15.1% | KQ lines 94, 99 |

Items inside GAAP Operating Profit that the filings call out (not removed from the ratios above):

@@L K23 738@@

@@S K24 484 <<Results in 2024 included a $565 million gain from the sale of our PPE business>> <<$456 million related to the 2024 Transformation Initiative>>@@

@@S K25 587 <<Operating profit of $2.4 billion decreased 12.9%>> <<$32 related to the Kenvue Acquisition.>>@@

**Segment margin.** Segment profit caption: "Operating Profit" by segment in MD&A (FY2021 to FY2023 10-Ks) and "Segment Operating Profit" in the segment note (FY2024 10-K onward). This is the segment measure reported to the chief operating decision maker, not a consolidated GAAP line: it excludes Corporate & Other and (through FY2023) Other (income) and expense, net.

@@L K21 1776@@

@@S K23 1661 <<Segment operating profit excludes>> <<ongoing operations of the business segments.>>@@

@@S K24 417 <<Further, our measure of segment profitability was changed>> <<highly inflationary accounting.>>@@

Segment rows as filed:

@@L K21 536@@

@@L K21 537@@

@@L K22 552@@

@@L K22 553@@

@@L K23 543@@

@@L K23 544@@

@@L K24 1650@@

@@L K24 1651@@

@@L K24 1652@@

@@L K24 1658@@

@@L K24 1661@@

@@L K24 1663@@

@@L K24 1669@@

@@L K24 1672@@

@@L K24 1674@@

@@L K24 1680@@

@@L K25 1849@@

@@L K25 1850@@

@@L K25 1851@@

@@L K25 1859@@

@@L K25 1862@@

@@L K25 1864@@

@@L K25 1872@@

@@L K25 1875@@

@@L K25 1877@@

@@L K25 1885@@

@@L KQ 552@@

@@L KQ 553@@

@@L KQ 554@@

@@L KQ 560@@

@@L KQ 576@@

@@L KQ 578@@

@@L KQ 584@@

| year | segment (filing) | segment operating profit | segment net sales | segment margin (computed) | source line |
|---|---|---|---|---|---|
| FY2020 | Personal Care (FY2021 10-K) | 1,933 | 9,339 | 20.7% | K21 line 537 |
| FY2021 | Personal Care (FY2021 10-K) | 1,856 | 10,267 | 18.1% | K21 line 537 |
| FY2022 | Personal Care (FY2022 10-K) | 1,787 | 10,622 | 16.8% | K22 line 553 |
| FY2023 | Personal Care (FY2023 10-K) | 1,890 | 10,691 | 17.7% | K23 line 544 |
| FY2022 recast | IPC (FY2024 10-K) | 670 | 6,054 | 11.1% | K24 lines 1674, 1680 |
| FY2022 recast | NA (FY2024 10-K) | 2,110 | 10,470 | 20.2% | K24 lines 1674, 1680 |
| FY2023 recast | IPC (FY2024 10-K) | 632 | 5,899 | 10.7% | K24 lines 1663, 1669 |
| FY2023 recast | NA (FY2024 10-K) | 2,507 | 10,988 | 22.8% | K24 lines 1663, 1669 |
| FY2024 | IPC (FY2024 10-K) | 787 | 5,715 | 13.8% | K24 lines 1652, 1658 |
| FY2024 | NA (FY2024 10-K) | 2,534 | 11,008 | 23.0% | K24 lines 1652, 1658 |
| FY2024 | IFP (FY2024 10-K) | 377 | 3,335 | 11.3% | K24 lines 1652, 1658 |
| FY2023 re-presented | IPC (FY2025 10-K) | 673 | 5,940 | 11.3% | K25 lines 1877, 1885 |
| FY2023 re-presented | NA (FY2025 10-K) | 2,514 | 10,996 | 22.9% | K25 lines 1877, 1885 |
| FY2024 re-presented | IPC (FY2025 10-K) | 826 | 5,743 | 14.4% | K25 lines 1864, 1872 |
| FY2024 re-presented | NA (FY2025 10-K) | 2,542 | 11,017 | 23.1% | K25 lines 1864, 1872 |
| FY2025 | IPC (FY2025 10-K) | 796 | 5,694 | 14.0% | K25 lines 1851, 1859 |
| FY2025 | NA (FY2025 10-K) | 2,553 | 10,753 | 23.7% | K25 lines 1851, 1859 |
| H1 2026 | IPC (10-Q) | 431 | 3,003 | 14.4% | KQ lines 554, 560 |
| H1 2026 | NA (10-Q) | 1,348 | 5,349 | 25.2% | KQ lines 554, 560 |
| H1 2025 | IPC (10-Q) | 383 | 2,819 | 13.6% | KQ lines 578, 584 |
| H1 2025 | NA (10-Q) | 1,333 | 5,398 | 24.7% | KQ lines 578, 584 |

### 3. Advertising

Two different disclosed figures exist and are kept separate: (i) "Advertising expense" in the Supplemental Income Statement Data note (all years); (ii) "Advertising and Promotion Expense" by segment in the segment note (FY2024 10-K onward, covering 2022 onward). Percentages below are computed by me (not given in the filings).

@@S K21 986 <<Advertising costs are expensed in the year>> <<traditional or digital media.>>@@

@@L K21 1815@@

@@L K21 1816@@

@@L K22 1843@@

@@L K22 1844@@

@@L K23 1727@@

@@L K23 1728@@

@@L K24 1714@@

@@L K24 1715@@

@@L K25 1927@@

@@L K25 1928@@

@@L K24 1654@@

@@L K24 1665@@

@@L K24 1676@@

@@L K25 1855@@

@@L K25 1868@@

@@L K25 1881@@

@@L KQ 556@@

@@L KQ 580@@

| year | measure | amount | net sales denominator | % of net sales (computed) | source line |
|---|---|---|---|---|---|
| FY2020 | Advertising expense (FY2021 10-K) | 956 | 19,140 | 5.0% | K21 line 1816 |
| FY2021 | Advertising expense (FY2021 10-K) | 893 | 19,440 | 4.6% | K21 line 1816 |
| FY2022 | Advertising expense (FY2022 10-K) | 901 | 20,175 | 4.5% | K22 line 1844 |
| FY2023 | Advertising expense (FY2023 10-K) | 1,075 | 20,431 | 5.3% | K23 line 1728 |
| FY2024 | Advertising expense (FY2024 10-K) | 1,184 | 20,058 | 5.9% | K24 line 1715 |
| FY2025 | Advertising expense (FY2025 10-K, continuing ops) | 1,020 | 16,447 | 6.2% | K25 line 1928 |
| FY2024 re-presented | Advertising expense (FY2025 10-K, continuing ops) | 1,122 | 16,805 | 6.7% | K25 line 1928 |
| FY2023 re-presented | Advertising expense (FY2025 10-K, continuing ops) | 1,026 | 17,146 | 6.0% | K25 line 1928 |
| FY2022 | Advertising and Promotion Expense, segment total (FY2024 10-K) | 1,009 | 20,175 | 5.0% | K24 line 1676 |
| FY2023 | same | 1,197 | 20,431 | 5.9% | K24 line 1665 |
| FY2024 | same | 1,296 | 20,058 | 6.5% | K24 line 1654 |
| FY2023 re-presented | same, continuing ops (FY2025 10-K) | 1,139 | 17,146 | 6.6% | K25 line 1881 |
| FY2024 re-presented | same, continuing ops (FY2025 10-K) | 1,222 | 16,805 | 7.3% | K25 line 1868 |
| FY2025 | same, continuing ops (FY2025 10-K) | 1,110 | 16,447 | 6.7% | K25 line 1855 |
| FY2022 recast | IPC Advertising and Promotion Expense (FY2024 10-K) | 348 | 6,054 | 5.7% | K24 line 1676 |
| FY2023 recast | IPC (FY2024 10-K) | 400 | 5,899 | 6.8% | K24 line 1665 |
| FY2024 | IPC (FY2024 10-K) | 416 | 5,715 | 7.3% | K24 line 1654 |
| FY2025 | IPC (FY2025 10-K) | 391 | 5,694 | 6.9% | K25 line 1855 |
| H1 2026 | segment total (10-Q) | 578 | 8,352 | 6.9% | KQ line 556 |
| H1 2026 | IPC (10-Q) | 212 | 3,003 | 7.1% | KQ line 556 |
| H1 2025 | segment total (10-Q) | 538 | 8,217 | 6.5% | KQ line 580 |

Denominator note: for the re-presented FY2023 and FY2024 continuing-operations rows I used total net sales (17,146 and 16,805), which include Corporate & Other net sales of 210 and 45 (K25 lines 1878, 1865). Advertising expense in the interim 10-Q outside the segment note: not disclosed (searched "advertis" in KMB_10Q_2026-06-30.txt; only segment-note rows and one MD&A phrase).

### 4. Gross margin and shipping/handling placement

Gross margin = Gross Profit / Net Sales, computed from the income statement rows quoted in section 2.

| year | basis | Gross Profit | Net Sales | gross margin (computed) | source line |
|---|---|---|---|---|---|
| FY2021 | total company | 5,988 | 19,440 | 30.8% | K21 lines 748, 750 |
| FY2022 | total company | 6,219 | 20,175 | 30.8% | K22 lines 758, 760 |
| FY2023 | total company | 7,032 | 20,431 | 34.4% | K23 lines 734, 736 |
| FY2024 | total company | 7,180 | 20,058 | 35.8% | K24 lines 770, 772 |
| FY2025 | continuing ops | 5,923 | 16,447 | 36.0% | K25 lines 844, 846 |
| FY2024 re-presented | continuing ops | 6,289 | 16,805 | 37.4% | K25 lines 844, 846 |
| FY2023 re-presented | continuing ops | 6,269 | 17,146 | 36.6% | K25 lines 844, 846 |
| H1 2026 | continuing ops | 3,137 | 8,352 | 37.6% | KQ lines 94, 96 |
| H1 2025 | continuing ops | 2,965 | 8,217 | 36.1% | KQ lines 94, 96 |
| Q2 2026 | continuing ops | 1,603 | 4,189 | 38.3% | KQ lines 94, 96 |

The company's own stated gross margins match where given:

@@S K24 483 <<Gross profit of $7.2 billion for the year ended December 31, 2024 increased 2.1%>> <<increased 140 basis points.>>@@

@@S K25 586 <<Gross profit of $5.9 billion decreased 5.8%>> <<decreased 140 basis points.>>@@

@@S KQ 722 <<Gross profit of $3.1 billion for the six months ended June 30, 2026 increased 5.8%>> <<increased 150 basis points.>>@@

**Shipping and handling placement.** The filings use the term "Distribution costs" and classify them in cost of products sold. The same sentence appears in the FY2021 and FY2025 10-Ks (quoted) under "Inventories and Distribution Costs" (also present in FY2022 line 978, FY2023 line 943, FY2024 line 974 section headings).

@@S K21 966 <<Distribution costs are classified as cost of products sold.>> <<cost of products sold.>>@@

@@S K25 1063 <<Distribution costs are classified as cost of products sold.>> <<cost of products sold.>>@@

@@S K25 1080 <<Sales are reported net of returns>> <<freight allowed.>>@@

A dollar amount for distribution or shipping and handling costs: not disclosed in any KMB 10-K or the 10-Q on disk (searched "shipping", "handling cost", "freight", "distribution cost", "transportation"). The 10-Q has no hits for these terms.

### 6. Competition and customer language

**(a) "Colgate" and "Hill".**

- "Colgate" (case-insensitive) in KMB_10K_FY2025_2025-12-31.txt: 0 hits. Across all KMB annual filings on disk (FY2021, FY2022, FY2023, FY2024, FY2025 10-Ks): 0 hits in each. Also 0 hits in KMB_10Q_2026-06-30.txt.
- "Hill" (case-insensitive) in KMB_10K_FY2025_2025-12-31.txt: 0 hits (so 0 Hill's pet brand hits and 0 unrelated hits). Across the other KMB files on disk: 1 hit, KMB_10K_FY2021_2021-12-31.txt line 304, "Hillshire Brands Company" in an executive biography (unrelated to the Hill's pet brand); 0 in FY2022 to FY2024 10-Ks and the 10-Q.
- No sentence names Colgate-Palmolive or Hill's. The Item 1 competition paragraph names no competitor:

@@L K25 167@@

**Kenvue transaction (assignment item).** "Kenvue" (case-insensitive) matches 40 lines in KMB_10K_FY2025_2025-12-31.txt. Verbatim sentences:

@@S K25 132 <<On November 2, 2025, we entered into an Agreement and Plan of Merger>> <<(the "Kenvue Acquisition").>>@@

@@S K25 132 <<In total, we expect approximately 280 million shares of common stock>> <<to be paid for the Merger Consideration.>>@@

@@S K25 132 <<The Cash Consideration is expected to be funded>> <<proceeds from the IFP Transaction (as defined below).>>@@

@@S K25 1212 <<On January 29, 2026, Kimberly-Clark and Kenvue each held a special meeting>> <<adopted by the requisite vote the Merger Agreement.>>@@

@@S K25 1212 <<Completion of the Kenvue Acquisition, which is expected to take place in the second half of 2026>> <<including the receipt of foreign regulatory approvals.>>@@

@@S K25 1212 <<The Merger Agreement also provides for certain termination rights>> <<termination fee of $ 1.1 billion.>>@@

@@S K25 506 <<During the year ended December 31, 2025, we incurred $32 of acquisition-related costs>> <<Marketing, research and general expenses.>>@@

From the 10-Q (newest filing):

@@S KQ 431 <<Completion of the Kenvue Acquisition, which is expected to take place in the second half of 2026>> <<including the receipt of foreign regulatory approvals.>>@@

@@S KQ 432 <<During the three and six months ended June 30, 2026, we incurred $ 109 and $ 157 , respectively>> <<Marketing, research and general expenses.>>@@

**(b) Private label / store brands** (FY2025 10-K; searched "private label", "store brand", "retailer brand", "value brand", "own label"; only "private label" hits, 5 lines).

@@S K25 272 <<We operate in highly competitive domestic and international markets against well-known, branded products and low-cost or private label products.>> <<low-cost or private label products.>>@@

@@S K25 272 <<Our competitors for these markets include global, regional and local manufacturers, including private label manufacturers.>> <<including private label manufacturers.>>@@

@@S K25 272 <<Alternatively, some of these competitors may have significantly lower product development and manufacturing costs>> <<allowing them to offer products at a lower price.>>@@

@@S K25 534 <<Our competitors include global, regional and local manufacturers, including private label manufacturers which offer products that are typically sold at lower prices.>> <<typically sold at lower prices.>>@@

@@S K25 534 <<In particular, we've experienced increased competitive pressures from private label manufacturers>> <<Family Care categories.>>@@

@@S K25 534 <<Increased purchases of private label products could reduce net sales>> <<negatively impact our profitability.>>@@

@@S K25 583 <<(c) Impact of the sale of the PPE business, the exit of the Company's private label diaper business in the United States>> <<2024 Transformation Initiative.>>@@

**(c) Customer concentration (Walmart), every annual filing.**

@@L K21 155@@

@@L K22 155@@

@@L K22 1775@@

@@L K23 139@@

@@L K24 139@@

@@L K24 1710@@

@@L K25 150@@

@@L K25 1923@@

Extraction artefact: K25 line 150 reads "approximatel y 16% i n 2025" (split words); the note version at K25 line 1923 reads "approximately 16 % in 2025".

| year | Walmart % of net sales | basis | filing (first report) | later filings | source line |
|---|---|---|---|---|---|
| FY2019 | 14 | consolidated | FY2021 10-K | nd | K21 line 155 |
| FY2020 | 15 | consolidated | FY2021 10-K | FY2022 10-K: 15 | K21 line 155; K22 line 155 |
| FY2021 | 14 | consolidated | FY2021 10-K | FY2022 and FY2023 10-Ks: 14 | K21 line 155; K22 line 155; K23 line 139 |
| FY2022 | 13 | consolidated | FY2022 10-K | FY2023 and FY2024 10-Ks: 13 | K22 line 155; K23 line 139; K24 line 139 |
| FY2023 | 13 | consolidated | FY2023 10-K | FY2024 10-K: 13; FY2025 10-K: 15 (continuing ops basis) | K23 line 139; K24 line 139; K25 line 1923 |
| FY2024 | 14 | consolidated | FY2024 10-K | FY2025 10-K: 16 (continuing ops basis) | K24 line 1710; K25 line 1923 |
| FY2025 | 16 | net sales from continuing operations | FY2025 10-K | nd | K25 line 1923 |
| H1 2026 | nd | | 10-Q ("Walmart" 0 hits) | | |

**(d) Pricing, promotion and trade language, FY2025 10-K and the 2026 10-Q** (searched "pric", "promot", "elastic", "trade-down", "trade down", "price investment", "rollback"; no hits for "elastic", "trade-down", "trade down", "price investment" or "rollback" in the FY2025 10-K).

@@L K25 535@@

@@S K25 534 <<This market environment has resulted in increased pressure on pricing>> <<continue in the coming year.>>@@

@@S K25 272 <<In order to stay competitive, it may be necessary for us to lower prices on our products>> <<adversely affect our financial results.>>@@

@@L K25 584@@

@@S K25 586 <<Excluding these charges, adjusted gross margin was 37.3%>> <<approximately $460.>>@@

North America segment (K25 line 627):

@@S K25 633 <<Operating profit of $2.6 billion was broadly in line with the prior year>> <<lower marketing, research and general expenses.>>@@

International Personal Care segment (K25 line 637):

@@L K25 643@@

@@S K25 1082 <<The cost of promotion activities provided to customers is classified as a reduction in sales revenue.>> <<reduction in sales revenue.>>@@

@@S K25 685 <<Trade promotion programs include introductory marketing funds>> <<to promote our products.>>@@

10-Q (quarter and six months ended 2026-06-30):

@@L KQ 719@@

@@S KQ 721 <<The increase was primarily due to one-time tariff refunds>> <<partially offset by unfavorable pricing net of cost inflation.>>@@

North America segment, 10-Q (KQ line 774 heading):

@@S KQ 779 <<Organic sales increased 0.5% driven by volume gains of 0.8%>> <<lower pricing to drive sales of new product.>>@@

@@S KQ 780 <<Operating profit for the three and six months ended June 30, 2026 of $725 and $1.3 billion>> <<incremental advertising spend.>>@@

International Personal Care segment, 10-Q (KQ line 782 heading):

@@S KQ 787 <<Organic sales growth was driven by volume and mix gains of 2.2% and 1.2%, respectively, partially offset by lower pricing.>> <<partially offset by lower pricing.>>@@

@@S KQ 788 <<The increase for the six months ended June 30, 2026 was driven by gross productivity savings>> <<supply chain related investments.>>@@

### Summary row

| FY window used | organic volume by year | price by year | GAAP operating margin by year | advertising % of sales by year | gross margin by year |
|---|---|---|---|---|---|
| FY21 to FY25 (FY21 to FY24 total company from each year's own 10-K; FY25 continuing operations excl. IFP) | FY21 -4 / FY22 -3 / FY23 -2 / FY24 +0.8 / FY25 +2.5 [Volume] | FY21 +2 / FY22 +9 / FY23 +6 / FY24 +1.9 / FY25 -0.9 [Net Price]; separately FY21 +1 / FY22 +1 / FY23 +1 / FY24 +0.4 / FY25 +0.1 [Mix/Other] | FY21 13.2 / FY22 13.3 / FY23 11.5 / FY24 16.0 / FY25 14.3 | FY21 4.6 / FY22 4.5 / FY23 5.3 / FY24 5.9 / FY25 6.2 [Advertising expense note] | FY21 30.8 / FY22 30.8 / FY23 34.4 / FY24 35.8 / FY25 36.0 |

### Gaps, extraction problems and definition differences

- Organic growth for "Personal Care" after FY2023: not disclosed, because the segment no longer exists in the FY2024 and FY2025 10-Ks or the 10-Q; IPC and NA are reported instead, as filed. FY2024 segment figures before FY2022 are not recast (FY2024 10-K recasts 2023 and 2022 only).
- FY2022 total and Personal Care decomposition tables have no acquisition/exits column; the FY2022 narrative states Thinx added 1 percent in NA Personal Care (K22 line 572). FY2023 Personal Care table has no exits column (the total-company table does, "Exited Business").
- FY2025 10-K consolidated figures are continuing operations (IFP discontinued), so FY2025 margins, advertising % and Walmart % are not on the same basis as FY2021 to FY2024. The FY2025 10-K re-presents 2024 and 2023 on the continuing basis (quoted above).
- Two advertising figures are disclosed with different scope: "Advertising expense" (supplemental note) and "Advertising and Promotion Expense" (segment note). Trade promotion is a reduction of net sales (K25 line 1082). Searched "advertis", "marketing", "brand support", "media", "A&P", "BMI": "brand support" and "A&P" have 0 hits in all KMB files; "media" hits concern Russia and social media, not spending amounts.
- Distribution/shipping cost amount: not disclosed (search terms in section 4). Distribution costs are in cost of products sold (K21 line 966, K25 line 1063). Colgate reports shipping and handling in SG&A, so KMB gross margins are not comparable to Colgate's on that basis.
- Hyperinflationary markets: KMB applies highly inflationary accounting in Argentina and Turkiye; the organic definitions quoted below do not state any exclusion of these markets, and the FY2024 10-K attributes price growth "primarily in hyperinflationary economies" (K24 lines 481, 552). Size of Argentina as filed:

@@S K25 1091 <<Net sales of K-C Argentina were approximately 1 % of our net sales>> <<2025, 2024 and 2023 .>>@@

- Extraction artefacts: FY2021 and FY2022 10-K MD&A tables print the net-sales and operating-profit percent tables side by side on one line and split row labels from values (K21 lines 505-518, K22 lines 523-535); FY2023 onward table headers are split over several lines (e.g. K23 lines 514-516, K24 lines 473-475); K25 line 150 split words ("approximatel y", "i n"); K23 line 533 "input cost s"; income statement negatives printed as "( 54 )" with internal spaces.
- Fiscal year: calendar year ending December 31 in all filings; no 52/53-week convention found (searched "53 weeks", "53-week"; 0 hits).
- Walmart % for the 2026 interim period: not disclosed in the 10-Q ("Walmart" 0 hits).
- **Definition of organic growth, as filed.** FY2021 to FY2023 10-Ks define it as the combination of volume, net price and mix/other:

@@L K21 520@@

@@S K21 366 <<In addition, we provide commentary regarding organic sales growth>> <<on net sales.>>@@

FY2024 and FY2025 10-Ks and the 10-Q define it by exclusion:

@@L K24 659@@

@@L K25 735@@

@@L KQ 813@@

- **Differences from Colgate's definition** (Colgate: net sales growth excluding foreign exchange, acquisitions and divestments; components "volume" and "net selling price"): (1) KMB reports three components, Volume, Net Price and a separate Mix/Other, where Colgate reports volume and net selling price; (2) KMB's exclusion category is "Divestitures and Business Exits" (FY2024 onward), which also removes exited businesses and markets, e.g. the exit of the US private label diaper business (K25 line 583), and in FY2021 "Acquisition/Exited Businesses"; (3) no stated exclusion of hyperinflationary markets or of price growth above any threshold; (4) calendar year ending December 31, no 53-week effect; (5) FY2025 onward is continuing operations only (IFP removed), a scope change rather than an organic adjustment.
- Shipping and handling: KMB puts distribution costs in cost of products sold; Colgate reports shipping and handling in SG&A.
'''
build(T, A, "SECTION_KMB.md")
