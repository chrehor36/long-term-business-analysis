# v5 PASSERS - every business that cleared the business questions under v5, and its alert
*Started 2026-10-07 at the operator's instruction: "we need to keep a list of the companies that passed so we can have alerts on them." A name is listed when a v5 purchase run in the register closes OUT at Q7 on price (every STOP before Q7 IN) or IN. It is added at the FOLD (step 4 in `Screens/WATCHLIST RUN QUEUE.md`), with its alert in `tools/alerts.json` at the run's own fair price; a later run of the same name replaces the row and the alert. No name has closed IN. Count the rows from the file.*

**What the alert means.** A fair price is the price at which the midpoint of the run's value range earns the floor of about ten percent (Part VII, The owner's price; after the company's own tax and on the all-equity basis for runs dated after 2026-10-06). A price at or below it is a prompt to re-run Q7 on fresh filings, never a buy: Q7 still asks for a price so far below value that no pencil is needed **[M2009-005]**. Runs of 2026-10-05 and 2026-10-06 computed their fair prices before sections E and H entered Q7, so those figures are higher than a run under today's text would set.

| ticker | company | run of record | active alert(s) |
|---|---|---|---|
| ABG | Asbury Automotive Group, Inc. | `Test Runs/2026-10-12 Run - ABG Asbury Automotive.md` | `ABG-v5-fair` $102.33 |
| ADP | Automatic Data Processing, Inc. | `Test Runs/2026-10-06 Run - ADP Automatic Data Processing.md` | `ADP-v5-fair` $108.88 |
| ADRZY | Andritz AG | `Test Runs/2026-10-12 Run - ADRZY Andritz.md` | `ADRZY-v5-fair` EUR35.02 |
| AEE | Ameren Corporation; NYSE AEE, SEC CIK 0001002910, Missouri, 10-K filer; a public utility holding company in St. Louis whose subsidiaries are Ameren Missouri (rate-regulated electric generation, transmission and distribution and gas distribution), Ameren Illinois (rate-regulated electric transmission and distribution and gas distribution) and ATXI (FERC-regulated transmission in the MISO), four segments; no rename, merger, spin-off or split in the 8-Ks since December 2025; the 10-K names no SEC-filing rival, Evergy, WEC Energy and Xcel Energy chosen as a CONVENTION of the run | `Test Runs/2026-10-18 Run - AEE Ameren.md` | `AEE-v5-fair` $31.39 |
| ALFVY | Alfa Laval AB; Nasdaq Stockholm ALFA, OTC ADR ALFVY, SEC CIKs 0000863344 and 0000713064 with ADR forms only, read from its own annual reports; heat transfer, separation and fluid handling in Energy, Food & Water and Marine; Fives Cryogenics and NRG Marine 2025 | `Test Runs/2026-10-17 Run - ALFVY Alfa Laval.md` | `ALFVY-v5-fair` SEK187.17 |
| AME | AMETEK, Inc. | `Test Runs/2026-10-10 Run - AME AMETEK.md` | `AME-v5-fair` $32.18 |
| AQN | Algonquin Power & Utilities Corp.; NYSE and TSX AQN, SEC CIK 0001174169, Ontario, 40-F filer reporting in US dollars under US GAAP, formerly Algonquin Power Income Fund; the Regulated Services Group (electric, water and wastewater, gas utilities and transmission in the US, Canada, Bermuda and Chile) and the Hydro Group; renewables other than hydro sold to LS Power 2025-01-08, the Atlantica interest sold 2024, the Suralis stake sale signed 2026-08-28 and open; the filing names no rival, Evergy, American Water Works and Atmos Energy chosen as a CONVENTION of the run | `Test Runs/2026-10-18 Run - AQN Algonquin Power & Utilities.md` | NONE: arm one at the fold |
| ATO | Atmos Energy Corporation; NYSE ATO, SEC CIK 0000731802, Texas and Virginia, fiscal year to September 30; a natural-gas-only regulated distributor to about 3.4 million customers in eight states, with one of the largest intrastate pipelines in Texas; $700 million of 6.000% notes due 2036 closed about 2026-10-09 | `Test Runs/2026-10-17 Run - ATO Atmos Energy.md` | `ATO-v5-fair` $33.59 |
| ATR | AptarGroup, Inc. | `Test Runs/2026-10-07 Run - ATR AptarGroup.md` | `ATR-v5-fair` $28.37 |
| AVA | Avista Corporation; NYSE AVA, SEC CIK 0000104918, Washington, 10-K filer, formerly Washington Water Power Co. until 1998; regulated electric and natural gas utility, two segments (Avista Utilities in Washington, Idaho, Oregon and Montana; AEL&P in Juneau, Alaska) plus Avista Capital investments; its 15 percent of Colstrip Units 3 and 4 transferred to NorthWestern 2026-01-01; Spokane-area wildfires from 2026-08-01 damaged its West Spokane transmission and distribution; no rename, merger, spin-off or split in the 8-Ks since the 10-K; the 10-K names no SEC-filing rival, IDACORP, Portland General and NorthWestern chosen as a CONVENTION of the run | `Test Runs/2026-10-18 Run - AVA Avista.md` | `AVA-v5-fair` $3.21 |
| AXIAY | AXIA Energia S.A.; OTC ADS AXIAY (common) and AXICY (class C preferred), one share per ADS, B3 AXIA3 and AXIA7, SEC CIK 0001439124, Rio de Janeiro, 20-F filer under IFRS in reais until the Form 15F of 2026-08-07, formerly Centrais Eletricas Brasileiras S.A. - Eletrobras, renamed 2026-04-15; Brazil's largest generator (43,872.3 MW, 17% of national capacity) and largest transmission company; class B preferred exchanged 2025-12-22, class B1 preferred exchanged into common 2026-06-10 on the Novo Mercado migration, ADSs delisted from the NYSE (Form 25 of 2026-07-27); the IE Madeira and IE Garanhuns swap with ISA Energia signed March 2026; the 20-F names no rival, CEMIG and COPEL chosen as a CONVENTION of the run | `Test Runs/2026-10-18 Run - AXIAY AXIA Energia.md` | `AXIAY-v5-fair` $1.13 |
| AXP | American Express Company | `Test Runs/2026-10-06 Run - AXP American Express.md` | `AXP-v5-fair` $137.51 |
| BCKIY | Babcock International Group PLC; London BAB, OTC ADR BCKIY one to one, SEC CIK 0001516323 with ADR forms only, read from its own annual reports; UK defence in Marine, Nuclear, Land and Aviation, Nuclear deciding | `Test Runs/2026-10-17 Run - BCKIY Babcock International Group.md` | `BCKIY-v5-fair` GBp427.0 |
| BIPC | Brookfield Infrastructure Corporation; NYSE and TSX BIPC, SEC CIK 0001788348, British Columbia, 20-F filer; exchangeable shares built to be economically one Brookfield Infrastructure Partners unit; combination into BIP Inc. signed 2026-07-21 | `Test Runs/2026-10-17 Run - BIPC Brookfield Infrastructure Corp.md` | NONE: arm one at the fold |
| BMI | Badger Meter, Inc. | `Test Runs/2026-10-07 Run - BMI Badger Meter.md` | `BMI-v5-fair` $38.2 |
| BRK.B | Berkshire Hathaway Inc. | `Test Runs/2026-10-05 Run - BRK.B Berkshire Hathaway.md` | `BRK.B-v5-range-bottom` $316 |
| CAT | Caterpillar Inc. | `Test Runs/2026-10-06 Run - CAT Caterpillar.md` | `CAT-v5-fair` $281.63 |
| CB | Chubb Limited | `Test Runs/2026-10-07 Run - CB Chubb.md` | `CB-v5-fair` $115.5 |
| CHD | Church & Dwight Co., Inc. | `Test Runs/2026-10-07 Run - CHD Church & Dwight.md` | `CHD-v5-fair` $34.13 |
| CHH | Choice Hotels International, Inc.; NYSE CHH; primarily a hotel franchisor of 7,575 hotels, the Radisson Americas brands among them, owning a few Cambria, Everhome and Radisson hotels; no rename, merger, spin-off or split in the 8-Ks since 2025-06, a $500M term loan 2026-08-28; Wyndham, Hilton and Marriott read, Best Western and other private rivals flagged | `Test Runs/2026-10-14 Run - CHH Choice Hotels International.md` | `CHH-v5-fair` $4.46 |
| CL | Colgate-Palmolive Company | `Test Runs/2026-10-07 Run - CL Colgate-Palmolive.md` | `CL-v5-fair` $33.91 |
| CMG | Chipotle Mexican Grill, Inc. | `Test Runs/2026-10-07 Run - CMG Chipotle.md` | `CMG-v5-fair` $13.24 |
| COST | Costco Wholesale Corporation | `Test Runs/2026-10-06 Run - COST Costco Wholesale.md` | `COST-v5-fair` $174.0 |
| CPK | Chesapeake Utilities Corporation; NYSE CPK, SEC CIK 0000019745, Delaware; regulated natural gas and electric distribution and gas transmission with propane and other unregulated energy, Mid-Atlantic, the Carolinas, Florida and Ohio; Florida City Gas bought 2023-11-30 | `Test Runs/2026-10-17 Run - CPK Chesapeake Utilities.md` | `CPK-v5-fair` $42.39 |
| CSL | Carlisle Companies Incorporated | `Test Runs/2026-10-07 Run - CSL Carlisle.md` | `CSL-v5-fair` $143.72 |
| CSW | CSW Industrials, Inc. | `Test Runs/2026-10-05 Run - CSW CSW Industrials.md` | `CSW-v5-fair` $35.71 |
| CTAS | Cintas Corporation | `Test Runs/2026-10-07 Run - CTAS Cintas.md` | `CTAS-v5-fair` $51.72 |
| DPMAY | Diploma PLC | `Test Runs/2026-10-12 Run - DPMAY Diploma.md` | `DPMAY-v5-fair` GBp453.0 |
| ECL | Ecolab Inc. | `Test Runs/2026-10-07 Run - ECL Ecolab.md` | `ECL-v5-fair` $8.09 |
| EFX | Equifax Inc. | `Test Runs/2026-10-07 Run - EFX Equifax.md` | `EFX-v5-fair` $40.36 |
| ENGGY | Enagas, S.A.; OTC ADS ENGGY at two ADSs per ordinary share, Madrid ENG, no SEC annual report, read from its own annual reports in EUR; the Spanish gas TSO | `Test Runs/2026-10-17 Run - ENGGY Enagas.md` | `ENGGY-v5-fair` $4.75 |
| EPAC | Enerpac Tool Group Corp. | `Test Runs/2026-10-07 Run - EPAC Enerpac.md` | `EPAC-v5-fair` $11.23 |
| ETN | Eaton Corporation plc | `Test Runs/2026-10-05 Run - ETN Eaton.md` | `ETN-v5-fair` $94.09 |
| FAST | Fastenal Company | `Test Runs/2026-10-12 Run - FAST Fastenal.md` | `FAST-v5-fair` $11.29 |
| GD | General Dynamics Corporation | `Test Runs/2026-10-06 Run - GD General Dynamics.md` | `GD-v5-fair` $142.9 |
| H | Hyatt Hotels Corporation; NYSE H; a global hotel manager, franchisor and owner with all-inclusive resorts and a distribution arm; Playa bought 2025; Marriott and Hilton read | `Test Runs/2026-10-14 Run - H Hyatt Hotels.md` | `H-v5-fair` $30.28 |
| HD | The Home Depot, Inc. | `Test Runs/2026-10-06 Run - HD Home Depot.md` | `HD-v5-fair` $128.76 |
| HGV | Hilton Grand Vacations Inc.; NYSE HGV; a timeshare developer, seller, lender and manager; spun off from Hilton in 2017; Diamond bought 2021, Bluegreen 2024; Marriott Vacations and Travel + Leisure read | `Test Runs/2026-10-14 Run - HGV Hilton Grand Vacations.md` | `HGV-v5-fair` $25.77 |
| HLT | Hilton Worldwide Holdings Inc.; NYSE HLT; a global hospitality company of 9,158 properties, management and franchise plus a small ownership segment; Park Hotels & Resorts and Hilton Grand Vacations spun off in 2017; no merger, spin-off or split item in the 8-Ks since 2025-06; Marriott, Choice and Hyatt read, Accor flagged | `Test Runs/2026-10-14 Run - HLT Hilton Worldwide Holdings.md` | `HLT-v5-fair` $27.98 |
| HOKCY | The Hong Kong and China Gas Company Limited; OTC ADS HOKCY at one ordinary per ADS, Hong Kong 0003, no SEC annual report, read from its own annual reports in HKD; Hong Kong town gas and mainland city gas | `Test Runs/2026-10-18 Run - HOKCY Hong Kong and China Gas.md` | `HOKCY-v5-fair` $0.037 |
| HON | Honeywell International Inc. | `Test Runs/2026-10-06 Run - HON Honeywell.md` | `HON-v5-fair` $89 |
| HTHT | H World Group Limited; Nasdaq HTHT ADSs and HKEX 1179; a multi-brand hotel franchisor, manager and lessee mostly in China with Deutsche Hospitality in Europe; formerly China Lodging and Huazhu; Hilton, Marriott and Atour read | `Test Runs/2026-10-14 Run - HTHT H World Group.md` | `HTHT-v5-fair` $14.08 |
| HUBB | Hubbell Incorporated | `Test Runs/2026-10-05 Run - HUBB Hubbell.md` | `HUBB-v5-fair` $137.02 |
| HWDJY | Howden Joinery Group Plc; London HWDN, OTC ADS HWDJY at four ordinaries, SEC CIK 0001563177 with F-6 filings only, GBP under IFRS; UK trade-only kitchens and joinery from 975 depots; DIY Kitchens bought 2026-06-23 | `Test Runs/2026-10-17 Run - HWDJY Howden Joinery Group.md` | `HWDJY-v5-fair` GBp499.0 |
| ITOCY | ITOCHU Corporation | `Test Runs/2026-10-12 Run - ITOCY ITOCHU Corporation.md` | `ITOCY-v5-fair` $1.82 |
| ITW | Illinois Tool Works Inc. | `Test Runs/2026-10-07 Run - ITW Illinois Tool Works.md` | `ITW-v5-fair` $68.5 |
| JKHY | Jack Henry & Associates, Inc. | `Test Runs/2026-10-07 Run - JKHY Jack Henry.md` | `JKHY-v5-fair` $57.11 |
| KAI | Kadant Inc.; NYSE KAI, formerly Thermo Fibertek to 2001; engineered systems, parts and consumables for paper, packaging, wood products, mining and recycling, in Flow Control, Industrial Processing and Material Handling; Babbini 2025, Kadant Profil 2026; no rival named in the 10-K, Albany International and Xerium read as a CONVENTION of the run | `Test Runs/2026-10-16 Run - KAI Kadant.md` | `KAI-v5-fair` $88.0 |
| KO | The Coca-Cola Company | `Test Runs/2026-10-06 Run - KO Coca-Cola.md` | `KO-v5-fair` $24.15 |
| LNT | Alliant Energy Corporation; Nasdaq LNT, SEC CIK 0000352541, 10-K filer; a regulated utility holding company in Madison, Wisconsin, electric and gas service to about 1,010,000 electric and 435,000 gas customers through IPL (Iowa) and WPL (Wisconsin), with a 16% interest in ATC under AEF; IPL left its steam business after 2025-12-31; no rename, merger, spin-off or split in the 8-Ks since June 2025; the 10-K names no SEC-filing rival, WEC Energy, MGE Energy and Xcel Energy chosen as a CONVENTION of the run | `Test Runs/2026-10-18 Run - LNT Alliant Energy.md` | `LNT-v5-fair` $17.1 |
| LOW | Lowe's Companies, Inc. | `Test Runs/2026-10-10 Run - LOW Lowe's.md` | `LOW-v5-fair` $110.05 |
| MA | Mastercard Incorporated | `Test Runs/2026-10-10 Run - MA Mastercard.md` | `MA-v5-fair` $259.13 |
| MAR | Marriott International, Inc.; Nasdaq MAR; a worldwide lodging franchisor, operator and licensor owning or leasing under 1% of its system; no rename, merger, spin-off or split in the 8-Ks since 2025-06; Hilton, IHG and Hyatt read, Accor and Best Western flagged | `Test Runs/2026-10-14 Run - MAR Marriott International.md` | `MAR-v5-fair` $45.91 |
| MCD | McDonald's Corporation | `Test Runs/2026-10-06 Run - MCD McDonalds.md` | `MCD-v5-fair` $100.41 |
| MDU | MDU Resources Group, Inc.; NYSE MDU, SEC CIK 0000067716, Delaware; regulated electric in North Dakota, Montana, South Dakota and Wyoming, natural gas distribution in eight states and the WBI interstate pipeline; Knife River separated 2023-05-31, Everus 2024-10-31 | `Test Runs/2026-10-18 Run - MDU MDU Resources Group.md` | `MDU-v5-fair` $3.86 |
| MITSY | Mitsui & Co., Ltd. | `Test Runs/2026-10-12 Run - MITSY Mitsui and Co.md` | `MITSY-v5-fair` $65 |
| MSA | MSA Safety Incorporated | `Test Runs/2026-10-10 Run - MSA MSA Safety.md` | `MSA-v5-fair` $48.82 |
| MWA | Mueller Water Products, Inc. | `Test Runs/2026-10-05 Run - MWA Mueller Water Products.md` | `MWA-v5-fair` $7.47 |
| NDSN | Nordson Corporation | `Test Runs/2026-10-10 Run - NDSN Nordson.md` | `NDSN-v5-fair` $77.13 |
| NJR | New Jersey Resources Corporation; NYSE NJR, SEC CIK 0000356309, New Jersey, fiscal year to September 30; New Jersey Natural Gas, Clean Energy Ventures, Energy Services, and Storage and Transportation (Leaf River, Adelphia, half of Steckman Ridge); residential solar portfolio sold 2024-11-25 | `Test Runs/2026-10-18 Run - NJR New Jersey Resources.md` | `NJR-v5-fair` $8.03 |
| OGS | ONE Gas, Inc.; NYSE and NYSE Texas OGS, SEC CIK 0001587732, Oklahoma; Oklahoma Natural Gas, Kansas Gas Service and Texas Gas Service, about 2.3 million customers; separated from ONEOK 2014-01-31 | `Test Runs/2026-10-18 Run - OGS ONE Gas.md` | NONE: arm one at the fold |
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
| SIEGY | Siemens AG | `Test Runs/2026-10-13 Run - SIEGY Siemens AG.md` | `SIEGY-v5-fair` $59.14 |
| SR | Spire Inc.; NYSE SR, SEC CIK 0001126956, formerly Laclede Group; regulated gas distribution through Spire Missouri, Spire Alabama, Spire Gulf and, from 2026-03-31, Spire Tennessee; Spire Marketing sold 2026-04-30, Spire Storage sold 2026-06-30 | `Test Runs/2026-10-18 Run - SR Spire.md` | NONE: arm one at the fold |
| STLD | Steel Dynamics, Inc.; no rename, spin-off or split in the 8-Ks since 2025-06; the remaining 55% of New Process Steel bought for cash 2025-12-01 | `Test Runs/2026-10-13 Run - STLD Steel Dynamics.md` | `STLD-v5-fair` $120.05 |
| SWX | Southwest Gas Holdings, Inc.; NYSE SWX, SEC CIK 0001692115, Delaware; Southwest Gas Corporation, regulated gas distribution to about 2.28 million customers in Arizona, Nevada and California; MountainWest sold 2023-02-14, Centuri deconsolidated August 2025 | `Test Runs/2026-10-18 Run - SWX Southwest Gas Holdings.md` | NONE: arm one at the fold |
| TECH | Bio-Techne Corporation | `Test Runs/2026-10-11 Run - TECH Bio-Techne.md` | `TECH-v5-fair` $13.96 |
| TRV | The Travelers Companies, Inc. | `Test Runs/2026-10-06 Run - TRV Travelers.md` | `TRV-v5-fair` $156 |
| TSCO | Tractor Supply Company | `Test Runs/2026-10-05 Run - TSCO Tractor Supply.md` | `TSCO-v5-fair` $16.2 |
| TXN | Texas Instruments Incorporated | `Test Runs/2026-10-11 Run - TXN Texas Instruments.md` | `TXN-v5-fair` $74.1 |
| UGI | UGI Corporation; NYSE UGI, SEC CIK 0000884614, fiscal year to September 30; Utilities, Midstream & Marketing, UGI International and AmeriGas; portfolio sales FY2024 to FY2026, the Electric Utility sale signed April 2026 | `Test Runs/2026-10-18 Run - UGI UGI Corporation.md` | `UGI-v5-fair` $16.2 |
| UNP | Union Pacific Corporation | `Test Runs/2026-10-11 Run - UNP Union Pacific.md` | `UNP-v5-fair` $59.3 |
| V | Visa Inc. | `Test Runs/2026-10-06 Run - V Visa.md` | `V-v5-add` $300; `V-v5-fair` $143.74 |
| WAB | Westinghouse Air Brake Technologies Corporation, d/b/a Wabtec; NYSE WAB; locomotives, rail and transit equipment, systems and services, segments Freight and Transit; Faiveley 2017, GE Transportation 2019, Inspection Technologies, Frauscher and Dellner 2025 to 2026; Caterpillar the one filing rival the 10-K names | `Test Runs/2026-10-16 Run - WAB Wabtec.md` | `WAB-v5-fair` $72.2 |
| WH | Wyndham Hotels & Resorts, Inc.; NYSE WH; the world's largest hotel franchisor by number of franchised properties, over 8,300 hotels under 25 brands; spun off from Wyndham Worldwide, now Travel + Leisure, in 2018; La Quinta bought 2018; no rival named in the 10-K, Choice, Hilton and Marriott chosen by the analyst | `Test Runs/2026-10-14 Run - WH Wyndham Hotels & Resorts.md` | `WH-v5-fair` $5.96 |
| WMT | Walmart Inc. | `Test Runs/2026-10-06 Run - WMT Walmart.md` | `WMT-v5-fair` $13.36 |
| XNGSY | ENN Energy Holdings Limited; OTC ADS XNGSY at four ordinaries per ADS, Hong Kong 2688, no SEC annual report, read from its own annual reports in RMB; a Chinese city-gas distributor | `Test Runs/2026-10-18 Run - XNGSY ENN Energy Holdings.md` | `XNGSY-v5-fair` $12.11 |

## The v4.1 gate-clearers awaiting a v5 run
*Names that cleared Q1 to Q4 under the archived v4.1 and have not yet been run under v5. Their v4.1 bands stay active until the v5 run replaces them; each leaves this list when its v5 run is folded (and enters the table above if it passes). The order is `Screens/_daily/_v5_rerun_order.txt`.*

.
