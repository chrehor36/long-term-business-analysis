# v5 PASSERS - every business that cleared the business questions under v5, and its alert
*Started 2026-10-07 at the operator's instruction: "we need to keep a list of the companies that passed so we can have alerts on them." A name is listed when a v5 purchase run in the register closes OUT at Q7 on price (every STOP before Q7 IN) or IN. It is added at the FOLD (step 4 in `Screens/WATCHLIST RUN QUEUE.md`), with its alert in `tools/alerts.json` at the run's own fair price; a later run of the same name replaces the row and the alert. No name has closed IN. Count the rows from the file.*

**What the alert means.** A fair price is the price at which the midpoint of the run's value range earns the floor of about ten percent (Part VII, The owner's price; after the company's own tax and on the all-equity basis for runs dated after 2026-10-06). A price at or below it is a prompt to re-run Q7 on fresh filings, never a buy: Q7 still asks for a price so far below value that no pencil is needed **[M2009-005]**. Runs of 2026-10-05 and 2026-10-06 computed their fair prices before sections E and H entered Q7, so those figures are higher than a run under today's text would set.

| ticker | company | run of record | active alert(s) |
|---|---|---|---|
| ABG | Asbury Automotive Group, Inc. | `Test Runs/2026-10-12 Run - ABG Asbury Automotive.md` | `ABG-v5-fair` $102.33 |
| ADP | Automatic Data Processing, Inc. | `Test Runs/2026-10-06 Run - ADP Automatic Data Processing.md` | `ADP-v5-fair` $108.88 |
| ADRZY | Andritz AG | `Test Runs/2026-10-12 Run - ADRZY Andritz.md` | `ADRZY-v5-fair` EUR35.02 |
| AME | AMETEK, Inc. | `Test Runs/2026-10-10 Run - AME AMETEK.md` | `AME-v5-fair` $32.18 |
| ATR | AptarGroup, Inc. | `Test Runs/2026-10-07 Run - ATR AptarGroup.md` | `ATR-v5-fair` $28.37 |
| AXP | American Express Company | `Test Runs/2026-10-06 Run - AXP American Express.md` | `AXP-v5-fair` $137.51 |
| BMI | Badger Meter, Inc. | `Test Runs/2026-10-07 Run - BMI Badger Meter.md` | `BMI-v5-fair` $38.2 |
| BRK.B | Berkshire Hathaway Inc. | `Test Runs/2026-10-05 Run - BRK.B Berkshire Hathaway.md` | `BRK.B-v5-range-bottom` $316 |
| CAT | Caterpillar Inc. | `Test Runs/2026-10-06 Run - CAT Caterpillar.md` | `CAT-v5-fair` $281.63 |
| CB | Chubb Limited | `Test Runs/2026-10-07 Run - CB Chubb.md` | `CB-v5-fair` $115.5 |
| CHD | Church & Dwight Co., Inc. | `Test Runs/2026-10-07 Run - CHD Church & Dwight.md` | `CHD-v5-fair` $34.13 |
| CL | Colgate-Palmolive Company | `Test Runs/2026-10-07 Run - CL Colgate-Palmolive.md` | `CL-v5-fair` $33.91 |
| CMG | Chipotle Mexican Grill, Inc. | `Test Runs/2026-10-07 Run - CMG Chipotle.md` | `CMG-v5-fair` $13.24 |
| COST | Costco Wholesale Corporation | `Test Runs/2026-10-06 Run - COST Costco Wholesale.md` | `COST-v5-fair` $174.0 |
| CSL | Carlisle Companies Incorporated | `Test Runs/2026-10-07 Run - CSL Carlisle.md` | `CSL-v5-fair` $143.72 |
| CSW | CSW Industrials, Inc. | `Test Runs/2026-10-05 Run - CSW CSW Industrials.md` | `CSW-v5-fair` $35.71 |
| CTAS | Cintas Corporation | `Test Runs/2026-10-07 Run - CTAS Cintas.md` | `CTAS-v5-fair` $51.72 |
| DPMAY | Diploma PLC | `Test Runs/2026-10-12 Run - DPMAY Diploma.md` | `DPMAY-v5-fair` GBp453.0 |
| ECL | Ecolab Inc. | `Test Runs/2026-10-07 Run - ECL Ecolab.md` | `ECL-v5-fair` $8.09 |
| EFX | Equifax Inc. | `Test Runs/2026-10-07 Run - EFX Equifax.md` | `EFX-v5-fair` $40.36 |
| EPAC | Enerpac Tool Group Corp. | `Test Runs/2026-10-07 Run - EPAC Enerpac.md` | `EPAC-v5-fair` $11.23 |
| ETN | Eaton Corporation plc | `Test Runs/2026-10-05 Run - ETN Eaton.md` | `ETN-v5-fair` $94.09 |
| FAST | Fastenal Company | `Test Runs/2026-10-12 Run - FAST Fastenal.md` | `FAST-v5-fair` $11.29 |
| GD | General Dynamics Corporation | `Test Runs/2026-10-06 Run - GD General Dynamics.md` | `GD-v5-fair` $142.9 |
| HD | The Home Depot, Inc. | `Test Runs/2026-10-06 Run - HD Home Depot.md` | `HD-v5-fair` $128.76 |
| HON | Honeywell International Inc. | `Test Runs/2026-10-06 Run - HON Honeywell.md` | `HON-v5-fair` $89 |
| HUBB | Hubbell Incorporated | `Test Runs/2026-10-05 Run - HUBB Hubbell.md` | `HUBB-v5-fair` $137.02 |
| ITOCY | ITOCHU Corporation | `Test Runs/2026-10-12 Run - ITOCY ITOCHU Corporation.md` | `ITOCY-v5-fair` $1.82 |
| ITW | Illinois Tool Works Inc. | `Test Runs/2026-10-07 Run - ITW Illinois Tool Works.md` | `ITW-v5-fair` $68.5 |
| JKHY | Jack Henry & Associates, Inc. | `Test Runs/2026-10-07 Run - JKHY Jack Henry.md` | `JKHY-v5-fair` $57.11 |
| KO | The Coca-Cola Company | `Test Runs/2026-10-06 Run - KO Coca-Cola.md` | `KO-v5-fair` $24.15 |
| LOW | Lowe's Companies, Inc. | `Test Runs/2026-10-10 Run - LOW Lowe's.md` | `LOW-v5-fair` $110.05 |
| MA | Mastercard Incorporated | `Test Runs/2026-10-10 Run - MA Mastercard.md` | `MA-v5-fair` $259.13 |
| MCD | McDonald's Corporation | `Test Runs/2026-10-06 Run - MCD McDonalds.md` | `MCD-v5-fair` $100.41 |
| MITSY | Mitsui & Co., Ltd. | `Test Runs/2026-10-12 Run - MITSY Mitsui and Co.md` | `MITSY-v5-fair` $65 |
| MSA | MSA Safety Incorporated | `Test Runs/2026-10-10 Run - MSA MSA Safety.md` | `MSA-v5-fair` $48.82 |
| MWA | Mueller Water Products, Inc. | `Test Runs/2026-10-05 Run - MWA Mueller Water Products.md` | `MWA-v5-fair` $7.47 |
| NDSN | Nordson Corporation | `Test Runs/2026-10-10 Run - NDSN Nordson.md` | `NDSN-v5-fair` $77.13 |
| ORLY | O'Reilly Automotive, Inc. | `Test Runs/2026-10-10 Run - ORLY O'Reilly Automotive.md` | `ORLY-v5-fair` $38.12 |
| OTIS | Otis Worldwide Corporation | `Test Runs/2026-10-10 Run - OTIS Otis Worldwide.md` | `OTIS-v5-fair` $15.2 |
| PBH | Prestige Consumer Healthcare Inc. | `Test Runs/2026-10-05 Run - PBH Prestige Consumer Healthcare.md` | `PBH-v5-fair` $24.97 |
| PG | The Procter & Gamble Company | `Test Runs/2026-10-06 Run - PG Procter & Gamble.md` | `PG-v5-fair` $65.38 |
| PM | Philip Morris International Inc. | `Test Runs/2026-10-06 Run - PM Philip Morris International.md` | `PM-v5-fair` $58.07 |
| PNR | Pentair plc | `Test Runs/2026-10-10 Run - PNR Pentair.md` | `PNR-v5-fair` $13.43 |
| POOL | Pool Corporation | `Test Runs/2026-10-05 Run - POOL Pool Corporation.md` | `POOL-v5-fair` $141.59 |
| REYN | Reynolds Consumer Products Inc. | `Test Runs/2026-10-06 Run - REYN Reynolds Consumer Products.md` | `REYN-v5-fair` $14.48 |
| SBUX | Starbucks Corporation | `Test Runs/2026-10-10 Run - SBUX Starbucks.md` | `SBUX-v5-fair` $33.48 |
| SHW | The Sherwin-Williams Company | `Test Runs/2026-10-06 Run - SHW Sherwin-Williams.md` | `SHW-v5-fair` $99.37 |
| TECH | Bio-Techne Corporation | `Test Runs/2026-10-11 Run - TECH Bio-Techne.md` | `TECH-v5-fair` $13.96 |
| TRV | The Travelers Companies, Inc. | `Test Runs/2026-10-06 Run - TRV Travelers.md` | `TRV-v5-fair` $156 |
| TSCO | Tractor Supply Company | `Test Runs/2026-10-05 Run - TSCO Tractor Supply.md` | `TSCO-v5-fair` $16.2 |
| TXN | Texas Instruments Incorporated | `Test Runs/2026-10-11 Run - TXN Texas Instruments.md` | `TXN-v5-fair` $74.1 |
| UNP | Union Pacific Corporation | `Test Runs/2026-10-11 Run - UNP Union Pacific.md` | `UNP-v5-fair` $59.3 |
| V | Visa Inc. | `Test Runs/2026-10-06 Run - V Visa.md` | `V-v5-add` $300; `V-v5-fair` $143.74 |
| WMT | Walmart Inc. | `Test Runs/2026-10-06 Run - WMT Walmart.md` | `WMT-v5-fair` $13.36 |

## The v4.1 gate-clearers awaiting a v5 run
*Names that cleared Q1 to Q4 under the archived v4.1 and have not yet been run under v5. Their v4.1 bands stay active until the v5 run replaces them; each leaves this list when its v5 run is folded (and enters the table above if it passes). The order is `Screens/_daily/_v5_rerun_order.txt`.*

.
