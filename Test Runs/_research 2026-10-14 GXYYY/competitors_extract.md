# Macau rivals: segment extract from the filed annual reports (LVS, WYNN, MLCO)

Extracted 2026-10-14 from the text conversions in `cache/` (filing accessions as given in the dispatch). Transcription only; the one derived column is EBITDA/revenue %, which is adjusted property EBITDA divided by net revenues in the same row, rounded to one decimal place. Units: US$ millions. Wynn and Melco report in thousands and are converted here by dividing by 1,000. Sums of property lines that this file adds itself are marked (sum).

**Overlap and restatement.** The filings do not overlap: each filing contributes three years (FY2016: 2014 to 2016; FY2019: 2017 to 2019; FY2022: 2020 to 2022; FY2025: 2023 to 2025). Because no year appears in two filings, no later-filing-wins substitution was needed. There is one basis break, though. LVS and Wynn adopted ASC 606 by the full retrospective method, so their 2017 figures in the FY2019 filings are on the new basis. Their 2014 to 2016 figures come from the FY2016 filings and stay on the old basis: under that basis, net revenues were stated after promotional allowances. Melco adopted ASC 606 on 2018-01-01 by the modified retrospective method, so its 2017 figures are on the old basis (MLCO_FY2019.txt, "We adopted the New Revenue Standard on January 1, 2018 under the modified retrospective method").

---

## 1. Las Vegas Sands (LVS): "Macao" segments (Venetian, Londoner/Sands Cotai Central, Parisian, Plaza and Four Seasons, Sands Macao, Ferry Operations and Other)

**Definition (LVS_FY2025.txt, Note 19; same wording in FY2016 Note 17, FY2019 Note 18, FY2022 Note 20):** consolidated adjusted property EBITDA "is net income (loss) from continuing operations before stock-based compensation expense, corporate expense, pre-opening expense, development expense, depreciation and amortization, amortization of leasehold interests in land, gain or loss on disposal or impairment of assets, interest, other income or expense, gain or loss on modification or early retirement of debt and income taxes." **So stock-based compensation is excluded**, and so is corporate expense.

**Revenue basis.** In the FY2016, FY2019 and FY2022 filings, the Macao subtotal includes intersegment revenues. In the FY2025 filing, the "Total Macao" column shows both "Net revenues" and "Net revenues before intersegment eliminations". The before-eliminations figure is used in the main column below so that the series stays on one basis, and the net-of-intersegment figure is shown in brackets. Macao intersegment revenue was US$24 to 48m a year (2014 to 2016: 48, 46, 46; 2017 to 2019: 28, 29, 31; 2020 to 2022: 24, 27, 30; 2023 to 2025: 32, 34, 37).

| Year | Net revenues | Adj. property EBITDA | EBITDA/rev % | Capex | Total assets (long-lived) | Source file and table heading |
|---|---|---|---|---|---|---|
| 2014 | 9,609 | 3,265 | 34.0 | 946 | 11,286 (7,908) | LVS_FY2016.txt, Note 17 Segment Information: "Net Revenues", "Adjusted Property EBITDA", "Capital Expenditures", "Total Assets", "Total Long-Lived Assets"; Macao subtotal row. Old revenue basis |
| 2015 | 6,899 | 2,222 | 32.2 | 1,293 | 10,692 (8,723) | same |
| 2016 | 6,732 | 2,244 | 33.3 | 1,185 | 11,068 (9,294) | same |
| 2017 | 7,609 | 2,607 | 34.3 | 479 | 10,514 (8,840) | LVS_FY2019.txt, Note 18 Segment Information: net revenues table (Macao subtotal), "Adjusted Property EBITDA", "Capital Expenditures", "Total Assets", "Total Long-Lived Assets". ASC 606 basis |
| 2018 | 8,689 | 3,079 | 35.4 | 535 | 11,617 (8,612) | same |
| 2019 | 8,834 | 3,189 | 36.1 | 762 | 11,817 (8,937) | same |
| 2020 | 1,707 | (431) | n.m. (-25.2) | 1,058 | 10,528 (9,361) | LVS_FY2022.txt, Note 20 Segment Information: net revenues by segment (Macao subtotal), "Adjusted Property EBITDA", "Capital Expenditures", "Total Assets", "Total Long-Lived Assets" |
| 2021 | 2,897 | 338 | 11.7 | 653 | 10,073 (9,099) | same |
| 2022 | 1,627 | (324) | n.m. (-19.9) | 243 | 10,550 (8,485) | same |
| 2023 | 6,559 [6,527] | 2,224 | 33.9 | 233 | 10,224 (7,892) | LVS_FY2025.txt, Note 19 Segment Information: "Total Macao" column, rows "Net revenues before intersegment eliminations" [ "Net revenues" ] and "Segment/Consolidated adjusted property EBITDA"; "Capital Expenditures" (Macao subtotal), "Total Assets", "Total Long-Lived Assets" |
| 2024 | 7,107 [7,073] | 2,327 | 32.7 | 879 | 11,140 (8,217) | same |
| 2025 | 7,470 [7,433] | 2,310 | 30.9 | 555 | 10,546 (7,944) | same |

Long-lived assets are "property and equipment, net of accumulated depreciation and amortization, and leasehold interests in land, net of accumulated amortization" (footnote to the long-lived assets table in each filing). Against the net-of-intersegment revenue, the 2023 to 2025 EBITDA/rev % is 34.1, 32.9 and 31.1.

## 2. Wynn Resorts (WYNN): "Macau Operations" (Wynn Palace plus Wynn Macau; assets also include "Other Macau", the Macau holding company and ancillary entities)

**Definition.** The measure was named "Adjusted Property EBITDA" up to the FY2019 filing and "Adjusted Property EBITDAR" from FY2022, when the triple-net rent at Encore Boston Harbor began. The R adds back only that US rent, so the Macau figures are not affected. In WYNN_FY2025.txt, Note 20 footnote (4), the measure "is net income before interest, income taxes, depreciation and amortization, pre-opening expenses, impairment of goodwill and intangible assets, property charges and other expenses, triple-net operating lease rent expense related to Encore Boston Harbor, management and license fees, corporate expenses and other expenses ..., stock-based compensation, change in derivatives fair value, loss on debt financing transactions, and other non-operating income and expenses." **Stock-based compensation is excluded**, and so are management and license fees, which are intercompany fees to the parent. The FY2016 definition (Note 18 (1)) also excludes stock-based compensation and "includes equity in income from unconsolidated affiliates".

| Year | Net / operating revenues | Adj. property EBITDA(R) | EBITDA/rev % | Capex | Total assets (long-lived, "Macau") | Source file and table heading |
|---|---|---|---|---|---|---|
| 2014 | 3,796.8 | 1,258.1 | 33.1 | 1,075.0 | 4,333.9 (2,799.8) | WYNN_FY2016.txt, Note 18 Segment Information: "Net revenues", "Adjusted Property EBITDA", "Capital expenditures", "Assets" (Total Macau Operations), "Long-lived assets" (Macau). Old revenue basis; Wynn Macau only (Palace opened 2016-08-22) |
| 2015 | 2,463.1 | 708.6 | 28.8 | 1,634.8 | 5,341.3 (4,324.7) | same |
| 2016 | 2,847.4 | 784.5 | 27.6 | 881.8 | 5,508.1 (4,973.9) | same |
| 2017 | 4,367.2 | 1,288.3 | 29.5 | 150.9 | 5,463.8 (4,614.0) | WYNN_FY2019.txt, Note 19 Segment Information: "Operating revenues" and "Adjusted Property EBITDA" (Total Macau Operations), "Capital expenditures", "Assets", "Long-lived assets". ASC 606 basis |
| 2018 | 5,052.1 | 1,577.1 | 31.2 | 152.2 | 5,831.3 (4,387.1) | same |
| 2019 | 4,613.7 | 1,378.4 | 29.9 | 208.7 | 6,414.2 (4,322.0) | same |
| 2020 | 980.1 | (236.8) | n.m. (-24.2) | 96.6 | 6,622.6 (3,989.8) | WYNN_FY2022.txt, Note 19 Segment Information: "Operating revenues" and "Adjusted Property EBITDAR (2)" (Total Macau Operations), "Capital expenditures", "Assets", "Long-lived assets" |
| 2021 | 1,509.0 | 95.9 | 6.4 | 62.4 | 5,328.9 (3,678.2) | same |
| 2022 | 721.5 | (220.6) | n.m. (-30.6) | 44.9 | 4,582.1 (3,382.3) | same |
| 2023 | 3,100.4 (sum) | 953.9 (sum) | 30.8 | 91.9 | 5,686.7 (3,191.1) | WYNN_FY2025.txt, Note 20 Segment Information: "Total segment operating revenues" and "Segment Adjusted Property EBITDAR (4)", Wynn Palace plus Wynn Macau columns (sum); "Capital expenditures" and "Assets", Total Macau Operations; "Long-lived assets", Macau |
| 2024 | 3,682.3 (sum) | 1,175.6 (sum) | 31.9 | 165.1 | 5,004.9 (3,095.4) | same. The revenue sum agrees with MD&A "Total Macau Operations 3,682,317" (line 606) |
| 2025 | 3,718.0 (sum) | 1,085.0 (sum) | 29.2 | 240.0 | 5,161.0 (3,040.6) | same. The revenue sum agrees with MD&A "Total Macau Operations 3,718,017" (line 606) |

Property detail (US$m, Palace / Macau). Revenues: 2023 1,886.8 / 1,213.5; 2024 2,217.7 / 1,464.6; 2025 2,307.4 / 1,410.6. EBITDAR: 2023 615.8 / 338.1; 2024 733.7 / 441.9; 2025 682.9 / 402.1.

## 3. Melco Resorts & Entertainment (MLCO): Macau = City of Dreams, Studio City, Altira Macau, Mocha (Clubs) and Other

Macau is separable in every filing. The FY2019 and FY2022 notes print a "Macau: ... Sub-total" row. The FY2025 note has no subtotal, but its geographic table gives "Operating Revenues: Macau", which equals the sum of the four Macau segments, and "Long-lived Assets: Macau". The figures below **exclude** City of Dreams Manila (the Philippines), Cyprus Operations / City of Dreams Mediterranean, Sri Lanka ("Other Operations", 2024 and 2025) and Corporate and Other.

**Definition.** MLCO_FY2025.txt, Note 22: "Adjusted property EBITDA is net income (loss) before interest, taxes, depreciation, amortization, pre-opening costs, development costs, property charges and other, share-based compensation, payments to the Philippine Parties, integrated resort and casino rent, Corporate and Other expenses, and other non-operating income and expenses." **Share-based compensation is excluded.** The FY2019 and FY2022 wording is the same, with "land rent to Belle" in place of "integrated resort and casino rent". Amortization of the gaming subconcession is below the line through 2022.

| Year | Net / operating revenues | Adj. property EBITDA | EBITDA/rev % | Capex | Total assets (long-lived, "Macau") | Source file and table heading |
|---|---|---|---|---|---|---|
| 2014 to 2016 | not covered | | | | | no FY2016 filing supplied |
| 2017 | 4,597.1 | 1,187.8 | 25.8 | 515.4 | 7,478.1 (6,389.8) | MLCO_FY2019.txt, Note 24 Segment Information: "NET REVENUES", "ADJUSTED PROPERTY EBITDA", "Capital Expenditures", "Total Assets" (Macau Sub-total rows), "Long-lived Assets" (Macau). Old revenue basis |
| 2018 | 4,496.8 | 1,208.7 | 26.9 | 418.1 | 7,512.8 (6,287.3) | same |
| 2019 | 4,988.3 | 1,412.6 | 28.3 | 248.2 | 7,191.1 (6,207.7) | same |
| 2020 | 1,426.3 | (135.5) | n.m. (-9.5) | 348.6 | 7,135.9 (6,054.0) | MLCO_FY2022.txt, Note 25 Segment Information: "Operating revenues", "Adjusted property EBITDA (1)", "Capital Expenditures", "Total Assets" (Macau Sub-total rows), "Long-lived Assets" (Macau) |
| 2021 | 1,660.4 | 144.5 | 8.7 | 565.8 | 6,998.1 (6,080.6) | same. Grand Dragon Casino revenue of US$24.2m sat in Corporate and Other in 2021 (US$18.3m in 2020) and is not in the Macau subtotal |
| 2022 | 844.7 | (170.1) | n.m. (-20.1) | 456.1 | 6,928.2 (6,068.5) | same |
| 2023 | 3,117.4 | 809.1 (sum) | 26.0 | 104.2 (sum) | 6,638.8 (sum) (5,752.8) | MLCO_FY2025.txt, Note 22 Segment Information: geographic "Operating Revenues" (Macau) and "Long-lived Assets" (Macau); "Adjusted property EBITDA", "Capital Expenditures" and "Total Assets" summed across the City of Dreams, Studio City, Altira Macau and Mocha and Other columns |
| 2024 | 3,920.3 | 987.9 (sum) | 25.2 | 182.2 (sum) | 6,321.3 (sum) (5,522.8) | same |
| 2025 | 4,429.2 | 1,234.0 (sum) | 27.9 | 246.8 (sum) | 5,960.2 (sum) (5,224.2) | same |

Property detail, 2025 (US$m): City of Dreams revenue 2,736.8, EBITDA 822.1; Studio City 1,478.4, 393.8; Altira (4.1) EBITDA on 107.0; Mocha and Other 22.2 on 107.1. The FY2025 note says City of Dreams charged Studio City intersegment revenue of US$55.0m (2025), US$44.9m (2024) and US$2.4m (2023). It is inside the Macau segment revenue figures.

Melco's non-Macau parts, for reference (US$m, revenue / adj. property EBITDA). City of Dreams Manila: 2017 649.3 / 235.0; 2019 602.5 / 247.1; 2022 396.4 / 146.9; 2025 411.1 / 132.8. Cyprus: 2019 94.7 / 29.8; 2022 91.3 / 23.7; 2025 300.2 / 68.2.

---

## 4. Concession statements

| Rival | Filing, section | Statement |
|---|---|---|
| LVS | LVS_FY2016.txt, Item 1 Business ("Regulation and Licensing - Macao Concession and Our Subconcession", line 542; risk factor line 1037) | LVS operated under a **subconcession granted through Galaxy's concession** (December 2002). "Our subconcession agreement expires on June 26, 2022. Unless our subconcession is extended, all of VML's casino premises and gaming-related equipment will be transferred automatically to the Macao government on that date without compensation to us." Redeemable from 2017-12-26 on one year's notice with fair compensation. |
| LVS | LVS_FY2019.txt, Item 1 (line 3993) and Item 1A (line 4311) | Same 2022-06-26 expiry and reversion language. Corporate income tax exemption on gaming profits through 2022-06-26, with an annual payment in lieu of dividend tax of 38 million patacas. |
| LVS | LVS_FY2022.txt, Item 1 "Regulation and Licensing - Macao Concession" (lines 211, 316, 344) | New 10-year concession from 2023-01-01, "expires in December 2032". The prior subconcession, as amended, ran to 2022-12-31. On expiry, "all casino premises and gaming-related equipment, which use was temporarily transferred by the Macao government to VML, will be transferred back to the Macao government ... together with any gaming-related equipment we acquire during our Concession, without any compensation to us." Investment commitment: 30.24 billion patacas (about US$3.77bn), including 27.80 billion patacas (about US$3.46bn) non-gaming, through 2032 (line 303). |
| LVS | LVS_FY2025.txt, Item 1 "Regulation and Licensing - Macao Concession" (lines 295, 318, 348) | Commitment now **35.84 billion patacas (about US$4.47bn)**, of which 33.39 billion patacas (about US$4.17bn) is non-gaming, "by December 2032". On 2022-12-30, VML committed to transfer the Gaming Assets back to the government "without compensation" and then received the right to operate them for the term. At expiry the Gaming Assets are returned without compensation, and "any new casinos, gaming areas and respective supporting areas that VML is authorized to operate during the Concession will revert to the Macao government without compensation to us." |
| WYNN | WYNN_FY2016.txt, Item 1 "Concession Agreement" (line 385) and Item 1A (line 923) | Original concession: Wynn had to invest at least 4 billion patacas (about US$500m) by June 2009, which was satisfied in 2006. The concession "expires in June 2022. Unless our concession is extended, in June 2022, all of our gaming operations and related equipment in Macau will be automatically transferred to the Macau government without compensation to us." Redeemable from June 2017 on one year's notice with fair compensation. |
| WYNN | WYNN_FY2019.txt, Item 1A (line 497) | The term "ends on June 26, 2022". The same automatic transfer without compensation applies. |
| WYNN | WYNN_FY2022.txt, Item 1 (line 225), Item 7 contractual commitments (line 963), Note 5 "Property Transfer Agreements" (line 1520) | 10-year concession from 2023-01-01, "expiring on December 31, 2032". Casino areas and gaming equipment were "transferred ... to the Macau government without compensation on December 31, 2022" and transferred back for use from 2023-01-01, for an annual payment. Investment commitment: MOP17.73bn (about US$2.21bn), of which MOP16.50bn (about US$2.05bn) is non-gaming, with a 20% non-gaming uplift if market GGR reaches MOP180bn. |
| WYNN | WYNN_FY2025.txt, Item 7 (line 922) and Note 5 "Macau Operations Property Transfer Agreements" (lines 1496 to 1497) | Commitment now **MOP21.03bn (about US$2.62bn)**, of which MOP19.80bn (about US$2.47bn) is non-gaming. Property transfer payment: MOP53.1m in 2023, price-indexed for 2024 and 2025, then MOP177.0m (about US$22.1m) a year from 2026, indexed. Bank guarantee of MOP1.0bn to the government (line 210). |
| MLCO | MLCO_FY2019.txt, Item 3.D Risk Factors (lines 3159 to 3162) | Melco operated under a **subconcession from Wynn Macau** (line 3022). "The Subconcession Contract expires on June 26, 2022. Unless it is extended ... all of our casino premises and gaming-related equipment under Melco Resorts Macau's subconcession will automatically revert to the Macau government without compensation." Redeemable from 2017, with compensation based on City of Dreams gross revenues. |
| MLCO | MLCO_FY2022.txt, Item 3.D (line 2692) and Item 4 (line 3318) | New concession; subconcessions are now prohibited (line 3932). Commitment: MOP11,823.7m overall (about US$1.5bn), plus a MOP2,003.0m (about US$249m) non-gaming increment if GGR reaches MOP180bn. Studio City's gaming and gaming support area of 28,784.3 square meters "is owned by the Macau SAR" and has been transferred to Melco for use during the concession from 2023-01-01. |
| MLCO | MLCO_FY2025.txt, defined terms (lines 818 and 990) and Item 3.D (lines 2211 and 2679) | The Concession Contract dated 2022-12-16, "as amended on February 10, 2026", "expires on December 31, 2032". The increment was triggered in 2023, so commitment is MOP11,823.7m (about US$1.48bn) plus MOP2,003.0m. On termination, "any casino premises and gaming equipment at that time will revert or be transferred to the Macau government without compensation to us." |

## 5. Not found or not covered

- **Melco 2014 to 2016**: no Melco filing before FY2019 was supplied, so there is nothing for those years.
- **LVS and Wynn 2014 to 2016** are on the pre-ASC 606 basis and are not restated in any supplied filing. They are not strictly comparable with 2017 onward.
- **Wynn 2023 to 2025 Macau revenue and EBITDAR**, and **Melco 2023 to 2025 Macau EBITDA, capex and total assets**, are sums of property columns made by this extract. The FY2025 notes print no Macau subtotal for these items. Melco's Macau revenue and long-lived assets are printed directly.
- **Segment capex is accrual-based property capex** as each note presents it. No note splits maintenance capex from growth capex.
- **No segment figure is net of corporate expense or stock-based compensation.** All three filers exclude both from the property measure, and none allocates them to Macau.
- I did not locate an MLCO_FY2025 sentence on reversion **at ordinary expiry**. The statement found covers reversion on termination (line 2211) plus the government-owned Studio City gaming area (line 3245). For the expiry clause, the LVS and Wynn texts above describe the same 2022 Macau gaming law regime.
