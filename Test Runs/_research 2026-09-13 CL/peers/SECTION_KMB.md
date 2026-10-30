## Kimberly-Clark Corporation (KMB)

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

> As part of the 2024 Transformation Initiative and the realignment of our internal operating and management structure during the fourth quarter of 2024, we manage and report our operations through three reportable segments defined by geographic regions and product groupings: North America ("NA"), International Personal Care ("IPC") and International Family Care and Professional ("IFP").
Source: KMB_10K_FY2024_2024-12-31.txt line 417

> Segment results for the historical periods presented in these consolidated financial statements have been recast to reflect these changes.
Source: KMB_10K_FY2024_2024-12-31.txt line 417

- FY2025 10-K and 2026 10-Q: IFP is reported as discontinued operations for all periods presented; continuing operations have two segments, NA and IPC. All FY2025 10-K consolidated figures (including re-presented 2024 and 2023) are continuing operations only, so they are not on the same basis as the FY2021 to FY2024 10-K consolidated figures.

> As a result, the results of the IFP Business are reported as discontinued operations and excluded from both continuing operations and segment results for all periods presented.
Source: KMB_10K_FY2025_2025-12-31.txt line 134

> As a result of the IFP Transaction discussed above, the Company's continuing operations are now organized into two reportable segments defined by geographic region: North America ("NA") and International Personal Care ("IPC").
Source: KMB_10K_FY2025_2025-12-31.txt line 139

> On July 1, 2026, all consultation requirements and customary closing conditions set forth in the Purchase Agreement were satisfied and the IFP Transaction was completed for a cash purchase price of approximately $ 1.3 billion, subject to certain post-closing adjustments.
Source: KMB_10Q_2026-06-30.txt line 649

### 1. Organic sales decomposition

Company labels: "Volume", "Net Price", "Mix/Other" (three separate components), "Currency" (FY2021 to FY2023) or "Currency Translation" (FY2024 onward), "Acquisition/Exited Businesses" (FY2021), "Exited Business" (FY2023), "Divestitures and Business Exits" (FY2024 onward), "Total", "Organic". Signs: parentheses = negative, as filed. The column ORDER changes in FY2024: FY2021 to FY2023 order is Volume, Net Price, Mix/Other; FY2024 onward order is Volume, Mix/Other, Net Price.

**FY2021 10-K (2021 vs 2020), total company.** Extraction artefact: the net sales percent-change table and the adjusted operating profit percent-change table are printed side by side on the same lines, and several row labels are split from their values onto the previous line. The first "Percent Change" column belongs to Net Sales.

> Net Sales | Percent Change | Adjusted Operating Profit | Percent Change |
Source: KMB_10K_FY2021_2021-12-31.txt line 505

> | 2021 vs. 2020 | 2021 vs. 2020 |
Source: KMB_10K_FY2021_2021-12-31.txt line 506

> Volume | (4) | Volume | (11) |
Source: KMB_10K_FY2021_2021-12-31.txt line 507

> Net Price | 2 | Net Price | 10 |
Source: KMB_10K_FY2021_2021-12-31.txt line 508

> Mix/Other | 1 | Input Costs | (42) |
Source: KMB_10K_FY2021_2021-12-31.txt line 509

> Acquisition/Exited Businesses (e)
Source: KMB_10K_FY2021_2021-12-31.txt line 510

> | 1 | Cost Savings (c)
Source: KMB_10K_FY2021_2021-12-31.txt line 511

> Currency | 1 | Currency Translation | 2 |
Source: KMB_10K_FY2021_2021-12-31.txt line 513

> Total (a)
Source: KMB_10K_FY2021_2021-12-31.txt line 514

> | 2 | Other (d)
Source: KMB_10K_FY2021_2021-12-31.txt line 515

> Organic (b)
Source: KMB_10K_FY2021_2021-12-31.txt line 517

> | (1) | Total | (21) |
Source: KMB_10K_FY2021_2021-12-31.txt line 518

> (b) Combined impact of changes in volume, net price and mix/other.
Source: KMB_10K_FY2021_2021-12-31.txt line 520

> (e) Combined impact of the acquisition of Softex Indonesia and exited businesses in conjunction with the 2018 Global Restructuring Program.
Source: KMB_10K_FY2021_2021-12-31.txt line 523

> Net sales of $19.4 billion increased 2 percent. Organic sales decreased 1 percent. Changes in foreign currency exchange rates increased sales by 1 percent, and the net impact of the Softex Indonesia acquisition and business exits in conjunction with the 2018 Global Restructuring Program increased sales approximately 1 percent.
Source: KMB_10K_FY2021_2021-12-31.txt line 396

**FY2021 10-K, Personal Care segment** (same side-by-side layout; first percent column is Net Sales).

> Net Sales | Percent Change | Operating Profit | Percent Change |
Source: KMB_10K_FY2021_2021-12-31.txt line 539

> Volume | 2 | Volume | 1 |
Source: KMB_10K_FY2021_2021-12-31.txt line 541

> Net Price | 2 | Net Price | 10 |
Source: KMB_10K_FY2021_2021-12-31.txt line 542

> Mix/Other | 2 | Input Costs | (34) |
Source: KMB_10K_FY2021_2021-12-31.txt line 543

> Acquisition/Exited Businesses (e)
Source: KMB_10K_FY2021_2021-12-31.txt line 544

> | 3 | Cost Savings (c)
Source: KMB_10K_FY2021_2021-12-31.txt line 545

> Currency | 1 | Currency Translation | 1 |
Source: KMB_10K_FY2021_2021-12-31.txt line 547

> Total (a)
Source: KMB_10K_FY2021_2021-12-31.txt line 548

> | 10 | Other (d)
Source: KMB_10K_FY2021_2021-12-31.txt line 549

> Organic (b)
Source: KMB_10K_FY2021_2021-12-31.txt line 551

> | 6 | Total | (4) |
Source: KMB_10K_FY2021_2021-12-31.txt line 552

**FY2022 10-K (2022 vs 2021), total company.** Same side-by-side layout. There is no acquisition/exits column in this table.

> Net Sales | Percent Change | Adjusted Operating Profit | Percent Change |
Source: KMB_10K_FY2022_2022-12-31.txt line 523

> Volume | (3) | Volume | (9) |
Source: KMB_10K_FY2022_2022-12-31.txt line 525

> Net Price | 9 | Net Price | 59 |
Source: KMB_10K_FY2022_2022-12-31.txt line 526

> Mix/Other | 1 | Input Costs | (52) |
Source: KMB_10K_FY2022_2022-12-31.txt line 527

> Currency | (4) | Cost Savings (c)
Source: KMB_10K_FY2022_2022-12-31.txt line 528

> Total (a)
Source: KMB_10K_FY2022_2022-12-31.txt line 530

> | 4 | Currency Translation | (3) |
Source: KMB_10K_FY2022_2022-12-31.txt line 531

> Organic (b)
Source: KMB_10K_FY2022_2022-12-31.txt line 534

> | 7 | Total | (8) |
Source: KMB_10K_FY2022_2022-12-31.txt line 535

> (b) Combined impact of changes in volume, net price and mix/other.
Source: KMB_10K_FY2022_2022-12-31.txt line 537

**FY2022 10-K, Personal Care segment.**

> Personal Care
Source: KMB_10K_FY2022_2022-12-31.txt line 550

> Net Sales | Percent Change | Operating Profit | Percent Change |
Source: KMB_10K_FY2022_2022-12-31.txt line 555

> | 2022 vs. 2021 | 2022 vs. 2021 |
Source: KMB_10K_FY2022_2022-12-31.txt line 556

> Volume | (3) | Volume | (7) |
Source: KMB_10K_FY2022_2022-12-31.txt line 557

> Net Price | 8 | Net Price | 45 |
Source: KMB_10K_FY2022_2022-12-31.txt line 558

> Mix/Other | 2 | Input Costs | (34) |
Source: KMB_10K_FY2022_2022-12-31.txt line 559

> Currency | (3) | Cost Savings (c)
Source: KMB_10K_FY2022_2022-12-31.txt line 560

> Total (a)
Source: KMB_10K_FY2022_2022-12-31.txt line 562

> | 3 | Currency Translation | (3) |
Source: KMB_10K_FY2022_2022-12-31.txt line 563

> Organic (b)
Source: KMB_10K_FY2022_2022-12-31.txt line 566

> | 7 | Total | (4) |
Source: KMB_10K_FY2022_2022-12-31.txt line 567

The Personal Care table has no acquisition column, but the North America Personal Care narrative states an acquisition effect:

> The acquisition of Thinx increased sales by 1 percent. Volumes decreased 3 percent, which included the impact from a planned exit of a private label contract in 2022.
Source: KMB_10K_FY2022_2022-12-31.txt line 572

**FY2023 10-K (2023 vs 2022), total company.** Header split across three lines (extraction artefact).

> Percent Change in Net Sales 2023 vs. 2022 | Volume | Net Price | Mix/Other | Exited Business (e)
Source: KMB_10K_FY2023_2023-12-31.txt line 514

> | Currency | Total (a)
Source: KMB_10K_FY2023_2023-12-31.txt line 515

> | Organic (b)
Source: KMB_10K_FY2023_2023-12-31.txt line 516

> Consolidated | (2) | 6 | 1 | (1) | (3) | 1 | 5 |
Source: KMB_10K_FY2023_2023-12-31.txt line 518

> (b) Combined impact of changes in volume, net price and mix/other.
Source: KMB_10K_FY2023_2023-12-31.txt line 529

> (e) Impact of the sale of Brazil tissue and K-C Professional business.
Source: KMB_10K_FY2023_2023-12-31.txt line 532

**FY2023 10-K, Personal Care segment.**

> 2023 vs. 2022 | Volume | Net Price | Mix/Other | Currency | Total (a)
Source: KMB_10K_FY2023_2023-12-31.txt line 546

> | Organic (b)
Source: KMB_10K_FY2023_2023-12-31.txt line 547

> Total Personal Care | (1) | 5 | 1 | (5) | 1 | 5 |
Source: KMB_10K_FY2023_2023-12-31.txt line 549

> Net sales of $10.7 billion increased 1 percent compared to the year ago period, while organic sales increased 5 percent driven by changes in net selling prices and product mix of 5 percent and 1 percent, respectively, partially offset by lower volumes of approximately 1 percent. Changes in foreign currency exchange rates decreased sales by approximately 5 percent.
Source: KMB_10K_FY2023_2023-12-31.txt line 563

**FY2024 10-K (2024 vs 2023), total company.**

> Percent Change in Net Sales | Volume | Mix/Other | Net Price | Divestitures and Business Exits (c)
Source: KMB_10K_FY2024_2024-12-31.txt line 473

> | Currency Translation | Total (a)
Source: KMB_10K_FY2024_2024-12-31.txt line 474

> | Organic (b)
Source: KMB_10K_FY2024_2024-12-31.txt line 475

> 2024 versus 2023 | 0.8 | 0.4 | 1.9 | (1.2) | (3.8) | (1.8) | 3.2 |
Source: KMB_10K_FY2024_2024-12-31.txt line 477

> (b) Represents the change in net sales excluding the impacts of currency translation and divestitures and business exits. Organic Sales Growth is a non-GAAP financial measure. See "Summary of Non-GAAP Financial Measures" below for reconciliations of our GAAP to non-GAAP measures.
Source: KMB_10K_FY2024_2024-12-31.txt line 479

> (c) Impact of the sale of the Brazil tissue and professional business, sale of the PPE business and other exited businesses and markets in conjunction with the 2024 Transformation Initiative.
Source: KMB_10K_FY2024_2024-12-31.txt line 480

> Excluding these items, organic growth was 3.2% driven by a 1.9% increase in price, primarily in hyperinflationary economies, coupled with volume and mix gains across all three reportable segments.
Source: KMB_10K_FY2024_2024-12-31.txt line 481

**FY2024 10-K, recast segments (2024 vs 2023, and 2023 vs 2022 recast).**

> Percent Change in Segment Net Sales | Volume | Mix/Other | Net Price | Divestitures and Business Exits (c)
Source: KMB_10K_FY2024_2024-12-31.txt line 503

> | Currency Translation | Total (a)
Source: KMB_10K_FY2024_2024-12-31.txt line 504

> | Organic (b)
Source: KMB_10K_FY2024_2024-12-31.txt line 505

> 2024 versus 2023 |
Source: KMB_10K_FY2024_2024-12-31.txt line 507

> NA | 0.5 | 0.5 | 0.1 | (0.8) | (0.1) | 0.2 | 1.1 |
Source: KMB_10K_FY2024_2024-12-31.txt line 508

> IPC | 0.9 | 0.5 | 7.8 | (0.1) | (12.2) | (3.1) | 9.2 |
Source: KMB_10K_FY2024_2024-12-31.txt line 509

> IFP | 1.5 | 0.3 | (2.0) | (4.4) | (1.2) | (5.9) | (0.2) |
Source: KMB_10K_FY2024_2024-12-31.txt line 510

> 2023 versus 2022 |
Source: KMB_10K_FY2024_2024-12-31.txt line 511

> NA | 0.3 | 0.4 | 4.3 | 0.2 | (0.3) | 4.9 | 5.0 |
Source: KMB_10K_FY2024_2024-12-31.txt line 512

> IPC | (4.2) | 1.6 | 7.9 | — | (7.9) | (2.6) | 5.3 |
Source: KMB_10K_FY2024_2024-12-31.txt line 513

> IFP | (7.6) | 1.1 | 9.3 | (3.9) | (1.8) | (2.9) | 2.8 |
Source: KMB_10K_FY2024_2024-12-31.txt line 514

International Personal Care segment narrative, FY2024 10-K:

> Organic sales benefited from higher net selling prices of 7.8%, primarily from hyperinflationary economies, and volume growth of 0.9%, led by China.
Source: KMB_10K_FY2024_2024-12-31.txt line 552

**FY2025 10-K (2025 vs 2024), continuing operations, total company.**

> Percent Change in Net Sales | Volume | Mix/Other | Net Price | Divestitures and Business Exits (c)
Source: KMB_10K_FY2025_2025-12-31.txt line 576

> | Currency Translation | Total (a)
Source: KMB_10K_FY2025_2025-12-31.txt line 577

> | Organic (b)
Source: KMB_10K_FY2025_2025-12-31.txt line 578

> 2025 versus 2024 | 2.5 | 0.1 | (0.9) | (2.9) | (0.9) | (2.1) | 1.7 |
Source: KMB_10K_FY2025_2025-12-31.txt line 580

> (c) Impact of the sale of the PPE business, the exit of the Company's private label diaper business in the United States, and other exited businesses and markets in conjunction with the 2024 Transformation Initiative.
Source: KMB_10K_FY2025_2025-12-31.txt line 583

> Net sales of $16.4 billion declined 2.1%, primarily from divestitures and business exits and unfavorable currency impacts, partially offset by organic sales growth. Organic sales increased 1.7% driven by volume gains of 2.5%, partially offset by lower pricing.
Source: KMB_10K_FY2025_2025-12-31.txt line 584

**FY2025 10-K, segments (NA and IPC, continuing operations).**

> Percent Change in Segment Net Sales | Volume | Mix/Other | Net Price | Divestitures and Business Exits (c)
Source: KMB_10K_FY2025_2025-12-31.txt line 611

> | Currency Translation | Total (a)
Source: KMB_10K_FY2025_2025-12-31.txt line 612

> | Organic (b)
Source: KMB_10K_FY2025_2025-12-31.txt line 613

> NA | 2.6 | (0.5) | (0.4) | (3.9) | (0.2) | (2.4) | 1.8 |
Source: KMB_10K_FY2025_2025-12-31.txt line 615

> IPC | 2.3 | 1.3 | (2.0) | (0.2) | (2.3) | (0.9) | 1.7 |
Source: KMB_10K_FY2025_2025-12-31.txt line 616

North America segment narrative (K25 line 627 heading "North America"):

> Organic sales increased 1.8% primarily from volume gains of 2.6%, with all categories growing volume, partially offset by lower pricing and mix.
Source: KMB_10K_FY2025_2025-12-31.txt line 632

International Personal Care segment narrative (K25 line 637 heading "International Personal Care"):

> Organic sales benefited from volume and mix gains of 2.3% and 1.3%, respectively, driven by China, Indonesia, Australia and South Korea, partially offset by lower pricing.
Source: KMB_10K_FY2025_2025-12-31.txt line 642

**10-Q for the quarter and six months ended 2026-06-30 (continuing operations).**

> Percent Change in Net Sales | Volume | Mix/Other | Net Price | Divestitures and Business Exits (c)
Source: KMB_10Q_2026-06-30.txt line 708

> | Currency Translation | Total (a)
Source: KMB_10Q_2026-06-30.txt line 709

> | Organic (b)
Source: KMB_10Q_2026-06-30.txt line 710

> Three Months Ended | (0.1) | 0.4 | (0.5) | (0.4) | 1.1 | 0.6 | (0.1) |
Source: KMB_10Q_2026-06-30.txt line 712

> Six Months Ended | 1.3 | 0.4 | (0.5) | (1.1) | 1.5 | 1.6 | 1.2 |
Source: KMB_10Q_2026-06-30.txt line 713

> (c) Impact of the exit of the Company's private label diaper business in the United States and other exited businesses and markets in conjunction with the 2024 Transformation Initiative.
Source: KMB_10Q_2026-06-30.txt line 716

> Percent Change in Segment Net Sales | Volume | Mix/Other | Net Price | Divestitures and Business Exits (c)
Source: KMB_10Q_2026-06-30.txt line 750

> Three Months Ended |
Source: KMB_10Q_2026-06-30.txt line 754

> NA | (0.3) | 0.2 | (0.7) | (0.5) | 0.1 | (1.2) | (0.7) |
Source: KMB_10Q_2026-06-30.txt line 755

> IPC | 0.3 | 0.9 | (0.2) | (0.1) | 3.1 | 4.0 | 1.0 |
Source: KMB_10Q_2026-06-30.txt line 756

> Six Months Ended |
Source: KMB_10Q_2026-06-30.txt line 757

> NA | 0.8 | — | (0.3) | (1.6) | 0.2 | (0.9) | 0.5 |
Source: KMB_10Q_2026-06-30.txt line 758

> IPC | 2.2 | 1.2 | (0.8) | — | 4.1 | 6.5 | 2.5 |
Source: KMB_10Q_2026-06-30.txt line 759

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

> (Millions of dollars, except per share amounts) | 2021 | 2020 | 2019 |
Source: KMB_10K_FY2021_2021-12-31.txt line 747

> Net Sales | $ | 19,440 | $ | 19,140 | $ | 18,450 |
Source: KMB_10K_FY2021_2021-12-31.txt line 748

> Cost of products sold | 13,452 | 12,318 | 12,415 |
Source: KMB_10K_FY2021_2021-12-31.txt line 749

> Gross Profit | 5,988 | 6,822 | 6,035 |
Source: KMB_10K_FY2021_2021-12-31.txt line 750

> Operating Profit | 2,561 | 3,244 | 2,991 |
Source: KMB_10K_FY2021_2021-12-31.txt line 753

> (Millions of dollars, except per share amounts) | 2022 | 2021 | 2020 |
Source: KMB_10K_FY2022_2022-12-31.txt line 757

> Net Sales | $ | 20,175 | $ | 19,440 | $ | 19,140 |
Source: KMB_10K_FY2022_2022-12-31.txt line 758

> Cost of products sold | 13,956 | 13,452 | 12,318 |
Source: KMB_10K_FY2022_2022-12-31.txt line 759

> Gross Profit | 6,219 | 5,988 | 6,822 |
Source: KMB_10K_FY2022_2022-12-31.txt line 760

> Operating Profit | 2,681 | 2,561 | 3,244 |
Source: KMB_10K_FY2022_2022-12-31.txt line 763

> (Millions of dollars, except per share amounts) | 2023 | 2022 | 2021 |
Source: KMB_10K_FY2023_2023-12-31.txt line 733

> Net Sales | $ | 20,431 | $ | 20,175 | $ | 19,440 |
Source: KMB_10K_FY2023_2023-12-31.txt line 734

> Cost of products sold | 13,399 | 13,956 | 13,452 |
Source: KMB_10K_FY2023_2023-12-31.txt line 735

> Gross Profit | 7,032 | 6,219 | 5,988 |
Source: KMB_10K_FY2023_2023-12-31.txt line 736

> Operating Profit | 2,344 | 2,681 | 2,561 |
Source: KMB_10K_FY2023_2023-12-31.txt line 740

> (In millions, except per share amounts) | 2024 | 2023 | 2022 |
Source: KMB_10K_FY2024_2024-12-31.txt line 769

> Net Sales | $ | 20,058 | $ | 20,431 | $ | 20,175 |
Source: KMB_10K_FY2024_2024-12-31.txt line 770

> Cost of products sold | 12,878 | 13,399 | 13,956 |
Source: KMB_10K_FY2024_2024-12-31.txt line 771

> Gross Profit | 7,180 | 7,032 | 6,219 |
Source: KMB_10K_FY2024_2024-12-31.txt line 772

> Operating Profit | 3,210 | 2,344 | 2,681 |
Source: KMB_10K_FY2024_2024-12-31.txt line 776

> (In millions, except per share amounts) | 2025 | 2024 | 2023 |
Source: KMB_10K_FY2025_2025-12-31.txt line 843

> Net Sales | $ | 16,447 | $ | 16,805 | $ | 17,146 |
Source: KMB_10K_FY2025_2025-12-31.txt line 844

> Cost of products sold | 10,524 | 10,516 | 10,877 |
Source: KMB_10K_FY2025_2025-12-31.txt line 845

> Gross Profit | 5,923 | 6,289 | 6,269 |
Source: KMB_10K_FY2025_2025-12-31.txt line 846

> Operating Profit | 2,351 | 2,700 | 1,928 |
Source: KMB_10K_FY2025_2025-12-31.txt line 850

> (In millions, except per share amounts) | 2026 | 2025 | 2026 | 2025 |
Source: KMB_10Q_2026-06-30.txt line 93

> Net Sales | $ | 4,189 | $ | 4,163 | $ | 8,352 | $ | 8,217 |
Source: KMB_10Q_2026-06-30.txt line 94

> Cost of products sold | 2,586 | 2,707 | 5,215 | 5,252 |
Source: KMB_10Q_2026-06-30.txt line 95

> Gross Profit | 1,603 | 1,456 | 3,137 | 2,965 |
Source: KMB_10Q_2026-06-30.txt line 96

> Operating Profit | 633 | 592 | 1,386 | 1,223 |
Source: KMB_10Q_2026-06-30.txt line 99

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

> Impairment of intangible assets | 658 | — | — |
Source: KMB_10K_FY2023_2023-12-31.txt line 738

> Results in 2024 included a $565 million gain from the sale of our PPE business, offset by charges of $456 million related to the 2024 Transformation Initiative
Source: KMB_10K_FY2024_2024-12-31.txt line 484

> Operating profit of $2.4 billion decreased 12.9%, inclusive of charges of $348 related to the 2024 Transformation Initiative and $32 related to the Kenvue Acquisition.
Source: KMB_10K_FY2025_2025-12-31.txt line 587

**Segment margin.** Segment profit caption: "Operating Profit" by segment in MD&A (FY2021 to FY2023 10-Ks) and "Segment Operating Profit" in the segment note (FY2024 10-K onward). This is the segment measure reported to the chief operating decision maker, not a consolidated GAAP line: it excludes Corporate & Other and (through FY2023) Other (income) and expense, net.

> (b) Segment operating profit excludes Other (income) and expense, net and income and expenses not associated with the business segments.
Source: KMB_10K_FY2021_2021-12-31.txt line 1776

> Segment operating profit excludes Other (income) and expense, net and income and expense not associated with ongoing operations of the business segments.
Source: KMB_10K_FY2023_2023-12-31.txt line 1661

> Further, our measure of segment profitability was changed to include the effects of changes in exchange rates on monetary assets and liabilities for subsidiaries where we have adopted highly inflationary accounting.
Source: KMB_10K_FY2024_2024-12-31.txt line 417

Segment rows as filed:

> | 2021 | 2020 | 2021 | 2020 |
Source: KMB_10K_FY2021_2021-12-31.txt line 536

> Net Sales | $ | 10,267 | $ | 9,339 | Operating Profit | $ | 1,856 | $ | 1,933 |
Source: KMB_10K_FY2021_2021-12-31.txt line 537

> | 2022 | 2021 | 2022 | 2021 |
Source: KMB_10K_FY2022_2022-12-31.txt line 552

> Net Sales | $ | 10,622 | $ | 10,267 | Operating Profit | $ | 1,787 | $ | 1,856 |
Source: KMB_10K_FY2022_2022-12-31.txt line 553

> 2023 | 2022 | 2023 | 2022 |
Source: KMB_10K_FY2023_2023-12-31.txt line 543

> Net Sales | $ | 10,691 | $ | 10,622 | Operating Profit | $ | 1,890 | $ | 1,787 |
Source: KMB_10K_FY2023_2023-12-31.txt line 544

> Year Ended December 31, 2024 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1650

> NA | IPC | IFP | Total |
Source: KMB_10K_FY2024_2024-12-31.txt line 1651

> Net Sales | $ | 11,008 | $ | 5,715 | $ | 3,335 | $ | 20,058 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1652

> Segment Operating Profit | $ | 2,534 | $ | 787 | $ | 377 | $ | 3,698 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1658

> Year Ended December 31, 2023 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1661

> Net Sales | $ | 10,988 | $ | 5,899 | $ | 3,544 | $ | 20,431 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1663

> Segment Operating Profit | $ | 2,507 | $ | 632 | $ | 287 | $ | 3,426 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1669

> Year Ended December 31, 2022 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1672

> Net Sales | $ | 10,470 | $ | 6,054 | $ | 3,651 | $ | 20,175 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1674

> Segment Operating Profit | $ | 2,110 | $ | 670 | $ | 256 | $ | 3,036 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1680

> Year Ended December 31, 2025 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1849

> NA | IPC | Total |
Source: KMB_10K_FY2025_2025-12-31.txt line 1850

> Segment Net Sales | $ | 10,753 | $ | 5,694 | $ | 16,447 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1851

> Segment Operating Profit | $ | 2,553 | $ | 796 | $ | 3,349 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1859

> Year Ended December 31, 2024 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1862

> Segment Net Sales | $ | 11,017 | $ | 5,743 | $ | 16,760 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1864

> Segment Operating Profit | $ | 2,542 | $ | 826 | $ | 3,368 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1872

> Year Ended December 31, 2023 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1875

> Segment Net Sales | $ | 10,996 | $ | 5,940 | $ | 16,936 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1877

> Segment Operating Profit | $ | 2,514 | $ | 673 | $ | 3,187 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1885

> Six Months Ended June 30, 2026 |
Source: KMB_10Q_2026-06-30.txt line 552

> NA | IPC | Total |
Source: KMB_10Q_2026-06-30.txt line 553

> Net Sales | $ | 5,349 | $ | 3,003 | $ | 8,352 |
Source: KMB_10Q_2026-06-30.txt line 554

> Segment Operating Profit | $ | 1,348 | $ | 431 | $ | 1,779 |
Source: KMB_10Q_2026-06-30.txt line 560

> Six Months Ended June 30, 2025 |
Source: KMB_10Q_2026-06-30.txt line 576

> Net Sales | $ | 5,398 | $ | 2,819 | $ | 8,217 |
Source: KMB_10Q_2026-06-30.txt line 578

> Segment Operating Profit | $ | 1,333 | $ | 383 | $ | 1,716 |
Source: KMB_10Q_2026-06-30.txt line 584

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

> Advertising costs are expensed in the year the related advertisement or campaign is first presented through traditional or digital media.
Source: KMB_10K_FY2021_2021-12-31.txt line 986

> | 2021 | 2020 | 2019 |
Source: KMB_10K_FY2021_2021-12-31.txt line 1815

> Advertising expense | $ | 893 | $ | 956 | $ | 757 |
Source: KMB_10K_FY2021_2021-12-31.txt line 1816

> | 2022 | 2021 | 2020 |
Source: KMB_10K_FY2022_2022-12-31.txt line 1843

> Advertising expense | $ | 901 | $ | 893 | $ | 956 |
Source: KMB_10K_FY2022_2022-12-31.txt line 1844

> 2023 | 2022 | 2021 |
Source: KMB_10K_FY2023_2023-12-31.txt line 1727

> Advertising expense | $ | 1,075 | $ | 901 | $ | 893 |
Source: KMB_10K_FY2023_2023-12-31.txt line 1728

> 2024 | 2023 | 2022 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1714

> Advertising expense | $ | 1,184 | $ | 1,075 | $ | 901 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1715

> 2025 | 2024 | 2023 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1927

> Advertising expense | $ | 1,020 | $ | 1,122 | $ | 1,026 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1928

> Advertising and Promotion Expense | 806 | 416 | 74 | 1,296 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1654

> Advertising and Promotion Expense | 739 | 400 | 58 | 1,197 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1665

> Advertising and Promotion Expense | 608 | 348 | 53 | 1,009 |
Source: KMB_10K_FY2024_2024-12-31.txt line 1676

> Advertising and Promotion Expense | 719 | 391 | 1,110 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1855

> Advertising and Promotion Expense | 806 | 416 | 1,222 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1868

> Advertising and Promotion Expense | 739 | 400 | 1,139 |
Source: KMB_10K_FY2025_2025-12-31.txt line 1881

> Advertising and Promotion Expense | 366 | 212 | 578 |
Source: KMB_10Q_2026-06-30.txt line 556

> Advertising and Promotion Expense | 335 | 203 | 538 |
Source: KMB_10Q_2026-06-30.txt line 580

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

> Gross profit of $7.2 billion for the year ended December 31, 2024 increased 2.1%, while gross margin of 35.8% increased 140 basis points.
Source: KMB_10K_FY2024_2024-12-31.txt line 483

> Gross profit of $5.9 billion decreased 5.8%, while gross margin of 36.0% decreased 140 basis points.
Source: KMB_10K_FY2025_2025-12-31.txt line 586

> Gross profit of $3.1 billion for the six months ended June 30, 2026 increased 5.8%, while gross margin of 37.6% increased 150 basis points.
Source: KMB_10Q_2026-06-30.txt line 722

**Shipping and handling placement.** The filings use the term "Distribution costs" and classify them in cost of products sold. The same sentence appears in the FY2021 and FY2025 10-Ks (quoted) under "Inventories and Distribution Costs" (also present in FY2022 line 978, FY2023 line 943, FY2024 line 974 section headings).

> Distribution costs are classified as cost of products sold.
Source: KMB_10K_FY2021_2021-12-31.txt line 966

> Distribution costs are classified as cost of products sold.
Source: KMB_10K_FY2025_2025-12-31.txt line 1063

> Sales are reported net of returns, consumer and trade promotions, rebates and freight allowed.
Source: KMB_10K_FY2025_2025-12-31.txt line 1080

A dollar amount for distribution or shipping and handling costs: not disclosed in any KMB 10-K or the 10-Q on disk (searched "shipping", "handling cost", "freight", "distribution cost", "transportation"). The 10-Q has no hits for these terms.

### 6. Competition and customer language

**(a) "Colgate" and "Hill".**

- "Colgate" (case-insensitive) in KMB_10K_FY2025_2025-12-31.txt: 0 hits. Across all KMB annual filings on disk (FY2021, FY2022, FY2023, FY2024, FY2025 10-Ks): 0 hits in each. Also 0 hits in KMB_10Q_2026-06-30.txt.
- "Hill" (case-insensitive) in KMB_10K_FY2025_2025-12-31.txt: 0 hits (so 0 Hill's pet brand hits and 0 unrelated hits). Across the other KMB files on disk: 1 hit, KMB_10K_FY2021_2021-12-31.txt line 304, "Hillshire Brands Company" in an executive biography (unrelated to the Hill's pet brand); 0 in FY2022 to FY2024 10-Ks and the 10-Q.
- No sentence names Colgate-Palmolive or Hill's. The Item 1 competition paragraph names no competitor:

> We have several major competitors in most of our markets, some of which are larger and more diversified than us. The principal methods and elements of competition include brand recognition and loyalty, product innovation, quality and performance, price, and marketing and distribution capabilities. For additional discussion of the competitive environment in which we conduct our business, see Item 1A, "Risk Factors."
Source: KMB_10K_FY2025_2025-12-31.txt line 167

**Kenvue transaction (assignment item).** "Kenvue" (case-insensitive) matches 40 lines in KMB_10K_FY2025_2025-12-31.txt. Verbatim sentences:

> On November 2, 2025, we entered into an Agreement and Plan of Merger (the "Merger Agreement") to acquire the outstanding equity interests of Kenvue, Inc. ("Kenvue"), a global consumer health leader, for stock and cash consideration (the "Kenvue Acquisition").
Source: KMB_10K_FY2025_2025-12-31.txt line 132

> In total, we expect approximately 280 million shares of common stock to be issued and approximately $6.7 billion to be paid for the Merger Consideration.
Source: KMB_10K_FY2025_2025-12-31.txt line 132

> The Cash Consideration is expected to be funded through a combination of cash on hand, proceeds from new debt issuance, and proceeds from the IFP Transaction (as defined below).
Source: KMB_10K_FY2025_2025-12-31.txt line 132

> On January 29, 2026, Kimberly-Clark and Kenvue each held a special meeting of their respective stockholders. During the respective meetings, Kimberly-Clark stockholders approved by requisite vote the issuance of Kimberly-Clark common stock as consideration to holders of Kenvue common stock, and Kenvue stockholders adopted by the requisite vote the Merger Agreement.
Source: KMB_10K_FY2025_2025-12-31.txt line 1212

> Completion of the Kenvue Acquisition, which is expected to take place in the second half of 2026, remains subject to the satisfaction of other customary closing conditions, as described in the Merger Agreement, including the receipt of foreign regulatory approvals.
Source: KMB_10K_FY2025_2025-12-31.txt line 1212

> The Merger Agreement also provides for certain termination rights, and under certain specified circumstances, both Kimberly-Clark and Kenvue may be required to pay the other a termination fee of $ 1.1 billion.
Source: KMB_10K_FY2025_2025-12-31.txt line 1212

> During the year ended December 31, 2025, we incurred $32 of acquisition-related costs in connection with the Kenvue Acquisition, which are included in Marketing, research and general expenses.
Source: KMB_10K_FY2025_2025-12-31.txt line 506

From the 10-Q (newest filing):

> Completion of the Kenvue Acquisition, which is expected to take place in the second half of 2026, remains subject to the satisfaction of other customary closing conditions, as described in the Merger Agreement, including the receipt of foreign regulatory approvals.
Source: KMB_10Q_2026-06-30.txt line 431

> During the three and six months ended June 30, 2026, we incurred $ 109 and $ 157 , respectively, of acquisition-related costs in connection with the Kenvue Acquisition, which are included in Marketing, research and general expenses.
Source: KMB_10Q_2026-06-30.txt line 432

**(b) Private label / store brands** (FY2025 10-K; searched "private label", "store brand", "retailer brand", "value brand", "own label"; only "private label" hits, 5 lines).

> We operate in highly competitive domestic and international markets against well-known, branded products and low-cost or private label products.
Source: KMB_10K_FY2025_2025-12-31.txt line 272

> Our competitors for these markets include global, regional and local manufacturers, including private label manufacturers.
Source: KMB_10K_FY2025_2025-12-31.txt line 272

> Alternatively, some of these competitors may have significantly lower product development and manufacturing costs, particularly with respect to private label products, allowing them to offer products at a lower price.
Source: KMB_10K_FY2025_2025-12-31.txt line 272

> Our competitors include global, regional and local manufacturers, including private label manufacturers which offer products that are typically sold at lower prices.
Source: KMB_10K_FY2025_2025-12-31.txt line 534

> In particular, we've experienced increased competitive pressures from private label manufacturers in the Baby and Child Care and Family Care categories.
Source: KMB_10K_FY2025_2025-12-31.txt line 534

> Increased purchases of private label products could reduce net sales of our higher-margin products which would negatively impact our profitability.
Source: KMB_10K_FY2025_2025-12-31.txt line 534

> (c) Impact of the sale of the PPE business, the exit of the Company's private label diaper business in the United States, and other exited businesses and markets in conjunction with the 2024 Transformation Initiative.
Source: KMB_10K_FY2025_2025-12-31.txt line 583

**(c) Customer concentration (Walmart), every annual filing.**

> Net sales to Walmart Inc. as a percent of our consolidated net sales were approximately 14 percent in 2021, 15 percent in 2020 and 14 percent in 2019. Net sales to Walmart Inc. were primarily in the Personal Care and Consumer Tissue segments.
Source: KMB_10K_FY2021_2021-12-31.txt line 155

> Our largest customer, Walmart Inc., represented approximately 13 percent in 2022, 14 percent in 2021 and 15 percent in 2020 of our consolidated net sales. Net sales to Walmart Inc. were primarily in the Personal Care and Consumer Tissue segments.
Source: KMB_10K_FY2022_2022-12-31.txt line 155

> Net sales to Walmart Inc. as a percent of our consolidated net sales were approximately 13 percent in 2022, 14 percent in 2021 and 15 percent in 2020. Net sales to Walmart Inc. were primarily in the Personal Care and Consumer Tissue segments.
Source: KMB_10K_FY2022_2022-12-31.txt line 1775

> Our largest customer, Walmart Inc., represented approximately 13 percent in 2023 and 2022 and 14 percent in 2021 of our consolidated net sales. Net sales to Walmart Inc. were primarily in the Personal Care and Consumer Tissue segments.
Source: KMB_10K_FY2023_2023-12-31.txt line 139

> Our largest customer, Walmart Inc., represented approximately 14 % in 2024 and 13 % in 2023 and 2022 of our consolidated net sales. Net sales to Walmart Inc. were primarily in the NA segment.
Source: KMB_10K_FY2024_2024-12-31.txt line 139

> Net sales to Walmart Inc. as a percent of our consolidated net sales were approximately 14 % in 2024 and 13 % in 2023 and 2022. Net sales to Walmart Inc. were primarily in the NA segment.
Source: KMB_10K_FY2024_2024-12-31.txt line 1710

> Our largest customer, Walmart Inc., represented approximatel y 16% i n 2025 and 2024 and 15% in 2023 of our net sales from continuing operations. Net sales to Walmart Inc. were primarily in the NA segment.
Source: KMB_10K_FY2025_2025-12-31.txt line 150

> Net sales to Walmart Inc. as a percent of our net sales from continuing operations were approximately 16 % in 2025 and 2024 and 15 % in 2023. Net sales to Walmart Inc. were primarily in the NA segment.
Source: KMB_10K_FY2025_2025-12-31.txt line 1923

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

> Pricing - Our net sales growth and profitability may be affected as we adjust prices to address market conditions. We adjust our product prices based on a number of variables including demand, the competitive environment, technological improvements, product innovations and changes in our raw material, distribution, energy and other input costs. Price changes may affect net sales, earnings and market share in the near term as the market adjusts to new pricing and other market conditions.
Source: KMB_10K_FY2025_2025-12-31.txt line 535

> This market environment has resulted in increased pressure on pricing and other competitive factors, and we expect these pressures to continue in the coming year.
Source: KMB_10K_FY2025_2025-12-31.txt line 534

> In order to stay competitive, it may be necessary for us to lower prices on our products and increase spending on advertising and promotions, which could adversely affect our financial results.
Source: KMB_10K_FY2025_2025-12-31.txt line 272

> Net sales of $16.4 billion declined 2.1%, primarily from divestitures and business exits and unfavorable currency impacts, partially offset by organic sales growth. Organic sales increased 1.7% driven by volume gains of 2.5%, partially offset by lower pricing.
Source: KMB_10K_FY2025_2025-12-31.txt line 584

> Excluding these charges, adjusted gross margin was 37.3%, a decrease of 100 basis points primarily due to unfavorable pricing net of cost inflation, including tariff impacts, and supply chain related investments, partially offset by gross productivity savings from integrated margin management of approximately $460.
Source: KMB_10K_FY2025_2025-12-31.txt line 586

North America segment (K25 line 627):

> Operating profit of $2.6 billion was broadly in line with the prior year, as impacts from divestitures and business exits (approximately 330 basis points), unfavorable pricing net of cost inflation and supply chain related investments were offset by gross productivity savings and lower marketing, research and general expenses.
Source: KMB_10K_FY2025_2025-12-31.txt line 633

International Personal Care segment (K25 line 637):

> Operating profit of $796 decreased 3.6% primarily due to unfavorable pricing net of cost inflation, supply chain related investments and currency impacts, partially offset by gross productivity savings, lower marketing, research and general expenses and volume and mix gains.
Source: KMB_10K_FY2025_2025-12-31.txt line 643

> The cost of promotion activities provided to customers is classified as a reduction in sales revenue.
Source: KMB_10K_FY2025_2025-12-31.txt line 1082

> Trade promotion programs include introductory marketing funds such as slotting fees, cooperative marketing programs, temporary price reductions and other activities conducted by our customers to promote our products.
Source: KMB_10K_FY2025_2025-12-31.txt line 685

10-Q (quarter and six months ended 2026-06-30):

> Net sales of $8.4 billion for the six months ended June 30, 2026 increased 1.6% primarily driven by organic sales growth and favorable currency impacts, partially offset by divestitures and business exits. Organic sales increased 1.2% primarily from volume gains of 1.3%.
Source: KMB_10Q_2026-06-30.txt line 719

> The increase was primarily due to one-time tariff refunds and gross productivity savings from integrated margin management of approximately $120, partially offset by unfavorable pricing net of cost inflation.
Source: KMB_10Q_2026-06-30.txt line 721

North America segment, 10-Q (KQ line 774 heading):

> Organic sales increased 0.5% driven by volume gains of 0.8%, primarily in Consumer Tissue and Professional categories, partially offset by lower pricing to drive sales of new product.
Source: KMB_10Q_2026-06-30.txt line 779

> Operating profit for the three and six months ended June 30, 2026 of $725 and $1.3 billion increased 10.7% and 1.1%, respectively, driven by one-time tariff refunds and gross productivity savings, partially offset by impacts from business exits of 110 basis points and 310 basis points for the three and six months ended June 30, 2026, respectively, and incremental advertising spend.
Source: KMB_10Q_2026-06-30.txt line 780

International Personal Care segment, 10-Q (KQ line 782 heading):

> Organic sales growth was driven by volume and mix gains of 2.2% and 1.2%, respectively, partially offset by lower pricing.
Source: KMB_10Q_2026-06-30.txt line 787

> The increase for the six months ended June 30, 2026 was driven by gross productivity savings, favorable currency impacts and volume and mix led net sales growth, partially offset by unfavorable pricing net of cost inflation and supply chain related investments.
Source: KMB_10Q_2026-06-30.txt line 788

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

> Net sales of K-C Argentina were approximately 1 % of our net sales in 2025, 2024 and 2023 .
Source: KMB_10K_FY2025_2025-12-31.txt line 1091

- Extraction artefacts: FY2021 and FY2022 10-K MD&A tables print the net-sales and operating-profit percent tables side by side on one line and split row labels from values (K21 lines 505-518, K22 lines 523-535); FY2023 onward table headers are split over several lines (e.g. K23 lines 514-516, K24 lines 473-475); K25 line 150 split words ("approximatel y", "i n"); K23 line 533 "input cost s"; income statement negatives printed as "( 54 )" with internal spaces.
- Fiscal year: calendar year ending December 31 in all filings; no 52/53-week convention found (searched "53 weeks", "53-week"; 0 hits).
- Walmart % for the 2026 interim period: not disclosed in the 10-Q ("Walmart" 0 hits).
- **Definition of organic growth, as filed.** FY2021 to FY2023 10-Ks define it as the combination of volume, net price and mix/other:

> (b) Combined impact of changes in volume, net price and mix/other.
Source: KMB_10K_FY2021_2021-12-31.txt line 520

> In addition, we provide commentary regarding organic sales growth, which describes the impact of changes in volume, product mix and net selling prices on net sales.
Source: KMB_10K_FY2021_2021-12-31.txt line 366

FY2024 and FY2025 10-Ks and the 10-Q define it by exclusion:

> • Organic Sales Growth is defined as the change in consolidated Net Sales, as determined in accordance with U.S. GAAP, excluding the impacts of currency translation and divestitures and business exits.
Source: KMB_10K_FY2024_2024-12-31.txt line 659

> • Organic Sales Growth is defined as the change in Net Sales, as determined in accordance with U.S. GAAP, excluding the impacts of currency translation and divestitures and business exits.
Source: KMB_10K_FY2025_2025-12-31.txt line 735

> • Organic Sales Growth is defined as the change in Net Sales, as determined in accordance with GAAP, excluding the impacts of currency translation and divestitures and business exits.
Source: KMB_10Q_2026-06-30.txt line 813

- **Differences from Colgate's definition** (Colgate: net sales growth excluding foreign exchange, acquisitions and divestments; components "volume" and "net selling price"): (1) KMB reports three components, Volume, Net Price and a separate Mix/Other, where Colgate reports volume and net selling price; (2) KMB's exclusion category is "Divestitures and Business Exits" (FY2024 onward), which also removes exited businesses and markets, e.g. the exit of the US private label diaper business (K25 line 583), and in FY2021 "Acquisition/Exited Businesses"; (3) no stated exclusion of hyperinflationary markets or of price growth above any threshold; (4) calendar year ending December 31, no 53-week effect; (5) FY2025 onward is continuing operations only (IFP removed), a scope change rather than an organic adjustment.
- Shipping and handling: KMB puts distribution costs in cost of products sold; Colgate reports shipping and handling in SG&A.
