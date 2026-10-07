# ABNB COMPETITOR ROW - filing-sourced (2026-09-13)

Fetch and compute only. No conclusion about any moat is drawn here (operator rule 8).
Sources: SEC EDGAR primary filings (10-K, 10-Q, 20-F; plus 8-K EX-99.1 and 6-K exhibits where a 10-K gives no absolute figure, flagged), accession numbers given per figure block.
Arithmetic ratios are computed from the filed figures and labelled as computed. Trip.com is in RMB; nothing is converted.

Status: COMPLETE (see Section 7 for gaps). Raw filings saved alongside as `10k_*.txt`, `10q_*.txt`, `20F_*.txt`; table-flattened copies as `flat_*.txt`.

### Summary (COMPUTATION from the tables below)
| | Booking (USD) | Expedia (USD) | Trip.com (RMB) |
|---|---|---|---|
| Take rate, total rev / GB: 2019, 2021, 2022, 2023, 2024, 2025 | 15.62%, 14.31%, 14.09%, 14.18%, 14.34%, 14.46% | 11.19%, 11.87%, 12.27%, 12.34%, 12.34%, 12.32% | not computable (GMV not disclosed) |
| Take rate ex advertising line, 2025 | 13.82% | 11.24% | n/c |
| Take rate 2020 (timing-distorted) | 19.20% | 14.13% | n/c |
| Units 2019 / 2020 / 2025 | room nights 845m / 355m / 1,235m | stayed 389.0m / 173.4m; booked 2025 415.4m (basis differs; releases, not 10-K) | not disclosed |
| Operating margin 2019 / 2025 | 35.5% / 32.8% | 7.5% / 12.7% | 14.1% / 25.3% |
| SBC/OCF cumulative 2021-2025 | 7.3% | 12.2% | 14.7% |
| Capex / revenue 2025 | 1.2% | 5.2% | 1.3% |
| (OCF-SBC-capex) / revenue 2025 | 31.5% | 18.4% | 18.1% |
| Marketing / revenue 2019 / 2025 | 33.0% / 30.4% (marketing expenses) | 50.8% / 55.6% (total S&M); direct 41.8% / 49.9% | 26.1% / 23.9% (S&M) |
| 2020 vs 2019: GB / units / revenue | -63.3% / -58.0% / -54.9% | -65.9% / -55.4% / -56.9% | GMV quarterly -51/-72/-51/-45% / n/d / -48.6% |
| First year above 2019 (GB, units, revenue) | 2022, 2022, 2022 | 2024, not determinable, 2023 | GMV 2023 (core OTA incl. Qunar), n/d, 2023 |
| Merchant/customer float inside OCF | yes | yes | yes |

---
## 1. BOOKING HOLDINGS (BKNG, CIK 0001075531) - USD millions

### Source documents (all read as primary filing text, converted from the filed .htm)
| Tag | Document | Filed | Accession |
|---|---|---|---|
| K19 | 10-K FY2019 (bkng1231201910k.htm) | 2020-02-26 | 0001075531-20-000011 |
| K20 | 10-K FY2020 (bkng-20201231.htm) | 2021-02-24 | 0001075531-21-000019 |
| K21 | 10-K FY2021 (bkng-20211231.htm) | 2022-02-23 | 0001075531-22-000008 |
| K22 | 10-K FY2022 (bkng-20221231.htm) | 2023-02-23 | 0001075531-23-000016 |
| K23 | 10-K FY2023 (bkng-20231231.htm) | 2024-02-22 | 0001075531-24-000014 |
| K24 | 10-K FY2024 (bkng-20241231.htm) | 2025-02-20 | 0001075531-25-000010 |
| K25 | 10-K FY2025 (bkng-20251231.htm) | 2026-02-18 | 0001075531-26-000009 |
| Q226 | 10-Q Q2 2026 (bkng-20260630.htm), six months to 2026-06-30 | 2026-08-04 | 0001075531-26-000037 |

Each year's figure is taken from that year's own 10-K (the tag in the Src column). H1 figures from Q226.

Gross bookings definition, verbatim (K21 and K22 MD&A): *"Gross bookings is an operating and statistical metric that captures the total dollar value, generally inclusive of taxes and fees, of all travel services booked through our OTC brands by our customers, net of cancellations, and is widely used in the travel business."*

### Reported figures
| Year | Src | Agency rev | Merchant rev | Advertising & other rev | Total revenue | Agency GB | Merchant GB | Total gross bookings | Room nights (m) | Operating income | Marketing expenses | OCF | SBC (CF add-back) | Additions to P&E | CF line "Deferred merchant bookings and other current liabilities" | DMB balance (year end) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | K19 | 10,117 | 3,830 | 1,119 | 15,066 | 70,651 | 25,791 | 96,443 | 845 | 5,345 | 4,967 (performance 4,419 + brand 548) | 4,865 | 325 | 368 | 480 (K19 label: "Accounts payable, accrued expenses and other current liabilities"; relabelled in K20) | 1,561 |
| 2020 | K20 | 4,314 | 2,117 | 365 | 6,796 | 24,475 | 10,920 | 35,395 | 355 | (631) | 2,179 | 85 | 255 | 286 | (2,266) | 323 |
| 2021 | K21 | 6,663 | 3,696 | 599 | 10,958 | 50,741 | 25,845 | 76,586 | 591 | 2,496 | 3,801 | 2,820 | 376 | 304 | 1,539 | 906 |
| 2022 | K22 | 9,003 | 7,193 | 894 | 17,090 | 67,379 | 53,873 | 121,253 | 896 | 5,102 | 5,993 | 6,554 | 404 | 368 | 3,718 | 2,223 |
| 2023 | K23 | 9,414 | 10,936 | 1,015 | 21,365 | 68,906 | 81,721 | 150,627 | 1,049 | 5,835 | 6,773 | 7,344 | 530 | 345 | 2,742 | 3,254 |
| 2024 | K24 | 8,524 | 14,142 | 1,073 | 23,739 | 61,398 | 104,182 | 165,580 | 1,144 | 7,555 | 7,278 | 8,323 | 599 | 429 | 1,361 | 4,031 |
| 2025 | K25 | 7,968 | 17,755 | 1,194 | 26,917 | 56,082 | 130,025 | 186,107 | 1,235 | 8,825 | 8,186 | 9,409 | 617 | 322 | 796 | 5,270 |
| H1 2025 | Q226 | 3,608 | 7,375 | 577 | 11,560 | 29,931 | 63,474 | 93,406 | 627 | 3,312 | 3,916 | 6,484 | 297 | 185 | 3,796 | n/r |
| H1 2026 | Q226 | 3,431 | 8,825 | 628 | 12,884 | 28,984 | 75,732 | 104,716 | 662 | 3,771 | 4,439 | 6,934 | 281 | 183 | 4,207 | n/r |

SBC line label: K19-K22 "Stock-based compensation expense and other stock-based payments"; K23 onward "Stock-based compensation expense". Capex: "Additions to property and equipment" (Booking's property and equipment note lists "Capitalized software" as a P&E class, so the line includes capitalized software). Marketing split: K19 discloses performance and brand marketing as separate income-statement lines; from K20 the income statement carries one "Marketing expenses" line (K22 MD&A: *"Our total marketing expenses, which are comprised of performance and brand marketing expenses that are substantially variable in nature, were $6.0 billion in 2022"*); no numeric split after 2019 was found in the 10-K text.

### Computed ratios (COMPUTATION, arithmetic on the figures above)
| Year | Take rate = total rev / GB | Take rate ex advertising = (agency+merchant rev) / GB | Operating margin | SBC/OCF | Capex/rev | (OCF-SBC-capex)/rev | Marketing/rev |
|---|---|---|---|---|---|---|---|
| 2019 | 15.62% | 14.46% | 35.5% | 6.7% | 2.4% | 27.7% | 33.0% |
| 2020 | 19.20% | 18.17% | -9.3% | 300% (OCF 85) n/m | 4.2% | -6.7% | 32.1% |
| 2021 | 14.31% | 13.53% | 22.8% | 13.3% | 2.8% | 19.5% | 34.7% |
| 2022 | 14.09% | 13.36% | 29.9% | 6.2% | 2.2% | 33.8% | 35.1% |
| 2023 | 14.18% | 13.51% | 27.3% | 7.2% | 1.6% | 30.3% | 31.7% |
| 2024 | 14.34% | 13.69% | 31.8% | 7.2% | 1.8% | 30.7% | 30.7% |
| 2025 | 14.46% | 13.82% | 32.8% | 6.6% | 1.2% | 31.5% | 30.4% |
| TTM to 2026-06-30 (FY25 + H1 26 - H1 25) | 14.31% | n/c | 32.9% | 6.1% | 1.1% | 31.6% | 30.8% |

- SBC/OCF cumulative 2021-2025: 2,526 / 34,450 = **7.3%**.
- 2020 take rate is distorted: revenue is recognised at check-in, gross bookings at booking, net of cancellations (K21: *"our gross bookings (recognized at the time of booking) and our revenues (recognized at the time of check-in)"*). Half-year take rates are seasonally low for the same reason.
- Merchant/agency mix shift: merchant revenue went from 25% of total (2019) to 66% (2025) (computed). Merchant revenue per K22 includes *"travel reservation commissions and transaction net revenues (i.e., the amount charged to travelers, including the impact of merchandising, less the amount owed to travel service providers) in connection with our merchant reservation services; revenues from facilitating payments, such as credit card processing rebates and customer processing fees; and ancillary fees, including travel-related insurance revenues."* On that definition merchant revenue is a net figure (amount charged less amount owed to providers), not a gross-up of room value, but it also contains payment-facilitation and insurance revenue that has no counterpart in a pure service-fee line.

### The 2020 collapse (computed from K20)
| Metric | 2019 | 2020 | Change | First year filer's own figure exceeded 2019 |
|---|---|---|---|---|
| Gross bookings | 96,443 | 35,395 | -63.3% | 2022 (121,253, K22) |
| Room nights (m) | 845 | 355 | -58.0% (K20 prints (58.0)%) | 2022 (896, K22) |
| Revenue | 15,066 | 6,796 | -54.9% | 2022 (17,090, K22) |

### Customer-deposit float in OCF
Booking's OCF **includes** the merchant-model float. Definition, K25 Note: *"Cash payments received from travelers in advance of the Company completing its performance obligations are included in "Deferred merchant bookings" in the Company's Consolidated Balance Sheets and are comprised principally of amounts estimated to be payable to travel service providers as well as the Company's estimated future revenues for its commission or margin and fees. The amounts are mostly subject to refunds for cancellations."* The working-capital change sits in operating activities. Presentation change: in K19 the operating line was "Accounts payable, accrued expenses and other current liabilities" (2019: 480); from K20 it is "Deferred merchant bookings and other current liabilities", with 2019 re-presented at the same 480 and 2019 long-term items re-combined ("Long-term assets and liabilities" (435) in K20 vs (36) + (399) in K19). The CF line bundles other current liabilities; the DMB-only swing computed from balance sheets is: 2020 -1,238; 2021 +583; 2022 +1,317; 2023 +1,031; 2024 +777; 2025 +1,239 (balance changes, include FX, COMPUTATION).

---
## 2. EXPEDIA GROUP (EXPE, CIK 0001324424) - USD millions

### Source documents
| Tag | Document | Filed | Accession |
|---|---|---|---|
| K19 | 10-K FY2019 (q42019-10k.htm) | 2020-02-14 | 0001324424-20-000009 |
| K20 | 10-K FY2020 (expe-20201231.htm) | 2021-02-12 | 0001324424-21-000015 |
| K21 | 10-K FY2021 (expe-20211231.htm) | 2022-02-11 | 0001324424-22-000009 |
| K22 | 10-K FY2022 (expe-20221231.htm) | 2023-02-10 | 0001324424-23-000007 |
| K23 | 10-K FY2023 (expe-20231231.htm) | 2024-02-09 | 0001324424-24-000007 |
| K24 | 10-K FY2024 (expe-20241231.htm) | 2025-02-07 | 0001324424-25-000008 |
| K25 | 10-K FY2025 (expe-20251231.htm) | 2026-02-13 | 0001324424-26-000008 |
| Q226 | 10-Q Q2 2026 (expe-20260630.htm), six months to 2026-06-30 | 2026-08-06 | 0001324424-26-000053 |
| R19 | 8-K EX-99.1 earnings release Q4 2019 (earningsrelease-q42019.htm) | 2020-02-13 | 0001324424-20-000006 |
| R20 | 8-K EX-99.1 earnings release Q4 2020 (earningsrelease-q42020.htm) | 2021-02-11 | 0001324424-21-000013 |
| R25 | 8-K EX-99.1 earnings release Q4 2025 (earningsrelease-q42025.htm) | 2026-02-12 | 0001324424-26-000005 |
| R226 | 8-K EX-99.1 earnings release Q2 2026 (earningsrelease-q22026.htm) | 2026-08-05 | 0001324424-26-000051 |

Room nights are **not** disclosed as absolute numbers in any Expedia 10-K read (growth rates only). The absolute figures below come from the earnings-release exhibits (R tags), which are furnished under Item 2.02, not filed financial statements.

Gross bookings definition, verbatim (K25 MD&A; same wording in K20): *"Gross bookings generally represent the total retail value of transactions booked for agency and merchant transactions, recorded at the time of booking reflecting the total price due for travel by travelers, including taxes, fees and other charges, and are reduced for cancellations and refunds. Revenue margin is defined as revenue as a percentage of gross bookings."* The K19 wording named Vrbo explicitly: *"Gross bookings generally represent the total retail value of transactions booked for agency, merchant and Vrbo transactions..."*

### Reported figures (each year from its own 10-K; restatements listed below the table)
| Year | Src | Merchant rev | Agency rev | Advertising, media (and other) rev | Vrbo rev (K19 only) | Total revenue | Gross bookings | Room nights (m) | Operating income | S&M direct | S&M indirect | S&M total | OCF | SBC (CF: "Amortization of stock-based compensation") | Capex (CF: "Capital expenditures, including internal-use software and website development") | CF: Deferred merchant bookings | CF: Accounts payable, merchant | DMB balance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | K19 | 6,459 | 3,165 | 1,103 | 1,340 | 12,067 | 107,873 | 389.0 stayed (R19) | 903 | 5,043 | 1,092 | 6,135 | 2,767 | 241 | 1,160 | 1,342 | 224 | 5,679 |
| 2020 | K20 | 3,261 | 1,267 | 671 | - | 5,199 | 36,796 | 173.4 stayed (R20) | (2,719) | 1,747 | 799 | 2,546 | (3,834) | 205 | 797 | (2,576) | (1,320) | 3,107 |
| 2021 | K21 | 5,537 | 2,307 | 754 | - | 8,598 | 72,425 | n/d (stayed +35%, K21) | 186 | 3,499 | 722 | 4,221 | 3,748 | 418 | 673 | 2,642 | 777 | 5,688 |
| 2022 | K22 | 7,762 | 2,994 | 911 | - | 11,667 | 95,049 | n/d (stayed +29%, K22) | 1,085 | 5,428 | 672 | 6,100 | 3,440 | 374 | 662 | 1,464 | 375 | 7,151 |
| 2023 | K23 | 8,818 | 3,075 | 946 | - | 12,839 | 104,079 | n/d (booked +12%, K23) | 1,033 | 6,107 | 756 | 6,863 | 2,690 | 413 | 846 | 572 | 332 | 7,723 |
| 2024 | K24 | 9,439 | 3,169 | 1,083 | - | 13,691 | 110,921 | 383.9 booked (R25) | 1,319 | 6,846 | 781 | 7,627 | 3,085 | 458 | 756 | 794 | (10) | 8,517 |
| 2025 | K25 | 10,256 | 3,183 | 1,294 | - | 14,733 | 119,590 (B2C 83,867; B2B 35,723) | 415.4 booked (R25) | 1,871 | 7,349 | 836 | 8,185 | 3,880 | 398 | 770 | 1,858 | 155 | 10,428 |
| H1 2025 | Q226 | 4,670 | 1,504 | 600 | - | 6,774 | 61,860 | 213.2 booked (R226, Q1 107.7 + Q2 105.5) | 415 | 3,677 | 412 | 4,089 | 4,073 | 203 | 396 | 4,898 | 119 | n/r |
| H1 2026 | Q226 | 5,466 | 1,547 | 728 | - | 7,741 | 69,458 | 225.4 booked (R226, Q1 113.9 + Q2 111.5) | 1,051 | 3,975 | 419 | 4,394 | 5,409 | 217 | 383 | 4,998 | 283 | 15,426 (at 2026-06-30) |

Restatements and basis changes (recorded as found, not smoothed):
- K19 revenue by business model carried Vrbo as its own line (merchant 6,459 / agency 3,165 / advertising and media 1,103 / Vrbo 1,340). K20 re-presented 2019 as merchant 6,763 / agency 3,882 / "advertising, media and other" 1,422, with Vrbo folded into the three models.
- K20 re-presented 2019 S&M as 6,078 (direct 5,043, indirect 1,035) against 6,135 in K19. K21 shows 2019 at 6,060 (direct 5,025) and 2020 at 2,527 (direct 1,728) against 2,546 in K20. Each row above uses the year's own first filing.
- Room-night basis changed. R19 and R20 report **stayed** room nights (R19 definition: *"Room nights represent stayed hotel room nights for our Core OTA and Egencia reportable segments and property nights for our Vrbo reportable segment."*). R25 and R226 report **booked** room nights (R25: *"Represents booked hotel room nights and property nights for our B2C reportable segment and booked hotel room nights for our B2B reportable segment."*). The two series are different measures.
- Segment basis: K19 Core OTA / trivago / Vrbo / Egencia; K20-K22 Retail / B2B / trivago; K23 onward B2C / B2B / trivago. Egencia left the group in 2021 (K23: *"Prior to its sale on November 1, 2021, our B2B segment also included Egencia"*).

### Vrbo-specific disclosure
- 2019 is the last year Vrbo was a reportable segment (K19): Vrbo gross bookings 11,933; Vrbo revenue 1,340; Vrbo revenue margin 11.2%; Vrbo Adjusted EBITDA 281; Vrbo segment operating income 180 (K19 segment note). Same year: Core OTA revenue margin 10.8%, Egencia 7.5%, total 11.2%.
- K19: *"Vrbo revenue increased 14% in 2019 compared to 2018 due to growth in transactional revenue of approximately 20% primarily driven by a benefit from the traveler service fee, partially offset by subscription revenue decreasing approximately 10%."*
- K19: *"Vrbo has been undergoing a transition from a listings-based classified advertising model to an online transactional model that optimizes for both travelers and homeowner and property manager partners, with a goal of increasing monetization and driving growth through investments in marketing as well as in product and technology. Vrbo offers hosts subscription-based listing or pay-per-booking service models. It also generates revenue from a traveler service fee for bookings. As of December 31, 2019, there are over 2.1 million online bookable listings available on Vrbo."*
- K20: *"Revenue per room night in 2020 benefited from an increase in the percentage of room nights contributed by Vrbo, which has a higher revenue per room night than the rest of our lodging business, and transaction revenue related to Vrbo's transition to merchant of record."*
- K19 deferred revenue note: *"Deferred revenue primarily consists of Vrbo's traveler service fees received on bookings where we are not merchant of record due to the use of a third party payment processor, unearned subscription revenue as well as deferred advertising revenue."*
- K20 legal proceedings: a 2016 putative class action against HomeAway.com, Inc. *"related to its implementation of a service fee. The putative class was comprised of homeowners that list their properties on HomeAway's websites for rent."*
- K25 revenue note: *"Vrbo also charges a traveler service fee at the time of booking. The service fee charged to travelers provides compensation for Vrbo's services, including but not limited to the use of Vrbo's website and VrboCare TM providing travelers with protection and support to travelers who book on Vrbo."* K25 MD&A: *"Vrbo primarily offers pay-per-booking service model and generates revenue from a traveler service fee for bookings, as well as insurance products."*
- Vrbo listing counts: K19 "over 2.1 million online bookable listings"; K20 "over 2 million online bookable alternative accommodations listings" (within "over 2.9 million lodging properties"); K22 and K23 "over 2 million online bookable alternative accommodations listings through Vrbo"; K24 "over 2.5 million online bookable alternative accommodations listings through Vrbo"; K25 *"approximately 2.4 million online bookable alternative accommodations through Vrbo"*.
- **Not disclosed** in any 10-K read: Vrbo gross bookings, revenue, nights or take rate after 2019; the traveler service fee rate, or any change in it, 2019-2021. The 10-Ks establish only that the fee exists and that it lifted 2019 revenue.

### Computed ratios (COMPUTATION)
| Year | Take rate = total rev / GB (the filer's "revenue margin") | Take rate ex the advertising/media line | Operating margin | SBC/OCF | Capex/rev | (OCF-SBC-capex)/rev | S&M total/rev | S&M direct/rev |
|---|---|---|---|---|---|---|---|---|
| 2019 | 11.19% (K19 prints 11.2%) | 10.16% | 7.5% | 8.7% | 9.6% | 11.3% | 50.8% | 41.8% |
| 2020 | 14.13% | 12.31% | -52.3% | n/m (OCF negative) | 15.3% | -93.0% | 49.0% | 33.6% |
| 2021 | 11.87% | 10.83% | 2.2% | 11.2% | 7.8% | 30.9% | 49.1% | 40.7% |
| 2022 | 12.27% | 11.32% | 9.3% | 10.9% | 5.7% | 20.6% | 52.3% | 46.5% |
| 2023 | 12.34% | 11.43% | 8.0% | 15.4% | 6.6% | 11.1% | 53.5% | 47.6% |
| 2024 | 12.34% | 11.37% | 9.6% | 14.8% | 5.5% | 13.7% | 55.7% | 50.0% |
| 2025 | 12.32% | 11.24% | 12.7% | 10.3% | 5.2% | 18.4% | 55.6% | 49.9% |
| TTM to 2026-06-30 (FY25 + H1 26 - H1 25) | 12.34% | 11.23% | 16.0% | 7.9% | 4.8% | 25.8% | 54.1% | n/c |

- SBC/OCF cumulative 2021-2025: 2,061 / 16,843 = **12.2%**.
- K25 segment revenue margins: B2C 11.3% (2025), 11.4% (2024), 11.5% (2023); B2B 13.6%, 13.8%, 13.8%.

### The 2020 collapse (computed)
| Metric | 2019 | 2020 | Change | First year filer's own figure exceeded 2019 |
|---|---|---|---|---|
| Gross bookings | 107,873 | 36,796 | -65.9% (K20 prints (66)%) | 2024 (110,921, K24) |
| Room nights (stayed, releases) | 389.0 | 173.4 | -55.4% (K20: "room nights declined 55% in 2020") | Not determinable like-for-like: stayed series not published after 2020 in the documents read; booked 2024 383.9 is below 2019 stayed 389.0 and booked 2025 415.4 is above it, but the bases differ |
| Revenue | 12,067 | 5,199 | -56.9% (K20 prints (57)%) | 2023 (12,839, K23) |

### Customer-deposit float in OCF
Expedia's OCF **includes** the merchant float through two operating lines, "Deferred merchant bookings" and "Accounts payable, merchant". K25 MD&A: *"Under the merchant model, we receive cash from travelers at the time of booking and we record these amounts on our consolidated balance sheets as deferred merchant bookings. We pay our airline suppliers related to these merchant model bookings generally within a few weeks after completing the transaction. For most other merchant bookings, which is primarily our merchant lodging business, we generally pay after the travelers' use and, in some cases, subsequent billing from the hotel suppliers. Therefore, generally we receive cash from the traveler prior to paying our supplier, and this operating cycle represents a working capital source of cash to us."* K25 risk factor: *"our merchant hotel business, which has historically provided a meaningful portion of our operating cash flow"*.

Combined swing from the two operating lines (COMPUTATION): 2019 +1,566; 2020 -3,896; 2021 +3,419; 2022 +1,839; 2023 +904; 2024 +784; 2025 +2,013; H1 2025 +5,017; H1 2026 +5,281. K25 also places the One Key loyalty liability inside deferred merchant bookings (K25 auditor critical audit matter: *"The Company defers the relative standalone selling price of earned rewards, net of rewards not expected to be redeemed (known as "breakage"), as deferred loyalty rewards within deferred merchant bookings on the consolidated balance sheet."*). No change to the caption of either cash-flow line was found across K19-K25.

### Like-for-like limits against Airbnb's net take rate
- Merchant hotel revenue is recorded net (K25 note: *"We record the payment in deferred merchant bookings until the stayed night occurs, at which point we recognize the revenue, net of amounts paid to suppliers, as this is when our performance obligation is satisfied."*). There is no hotel gross-up.
- B2B partner commissions are expensed in selling and marketing rather than netted from revenue (K25: *"Selling and marketing - direct increased $503 million during 2025 compared to 2024 primarily driven by an increase in B2B partner commissions to support strong growth."*). B2B revenue and the total take rate are therefore gross of what distribution partners receive.
- Revenue includes advertising (trivago, EG Advertising) that has no associated gross bookings, and agency gross bookings are mostly air (K25: *"The majority of our agency gross bookings relate to air bookings."*). Airbnb has neither.

---
## 3. TRIP.COM GROUP (TCOM, CIK 0001269238) - **RMB millions** (no currency conversion performed; the filer's own US$ convenience column is not used)

### Source documents
| Tag | Document | Filed | Accession |
|---|---|---|---|
| F19 | 20-F FY2019 (d860693d20f.htm) | 2020-04-09 | 0001193125-20-102627 |
| F20 | 20-F FY2020 (d73725d20f.htm) | 2021-03-15 | 0001193125-21-081372 |
| F21 | 20-F FY2021 (d270872d20f.htm) | 2022-04-27 | 0001193125-22-123585 |
| F22 | 20-F FY2022 (d442074d20f.htm) | 2023-03-27 | 0001193125-23-080422 |
| F23 | 20-F FY2023 (d630811d20f.htm) | 2024-04-29 | 0001193125-24-122196 |
| F24 | 20-F FY2024 (d779353d20f.htm) | 2025-04-11 | 0001193125-25-078429 |
| F25 | 20-F FY2025 (d27369d20f.htm) | 2026-04-28 | 0001193125-26-183379 |
| Q126 | 6-K EX-99.1 "Unaudited First Quarter of 2026 Financial Results" (d163607dex991.htm) | 2026-06-25 | 0001193125-26-281805 |
| N26 | 6-K EX-99.2 announcing Q2 and H1 2026 results for 2026-09-15 US time (d431415dex992.htm) | 2026-09-02 | 0001193125-26-379443 |

Latest interim: Q1 2026 (Q126). Q2/H1 2026 results are not yet published: N26 says they will be announced *"on Tuesday, September 15, 2026, U.S. Time, after the market closes."* Trip.com is a foreign private issuer and files no 10-Q.

### Reported figures
| Year | Src | Accommodation reservation rev | Transportation ticketing rev | Packaged tours rev | Corporate travel rev | Other rev | Total revenues | Net revenues (after sales tax and surcharges) | Income (loss) from operations | Sales and marketing | OCF | SBC (CF add-back) | Purchase of property, equipment and software | CF: Increase/(decrease) in accounts payable | CF: Increase/(decrease) in advances from customers | Advances from customers balance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 | F19 | 13,514 | 13,952 | 4,534 | 1,255 | 2,461 | 35,716 | 35,666 | 5,040 | 9,295 | 7,333 | 1,714 | 823 | 540 | 2,211 | 11,675 |
| 2020 | F20 | 7,132 | 7,146 | 1,241 | 877 | 1,931 | 18,327 | 18,316 | (1,423) | 4,405 | (3,823) | 1,873 | 532 | (7,762) | (4,073) | 7,605 |
| 2021 | F21 | 8,148 | 6,905 | 1,105 | 1,347 | 2,524 | 20,029 | 20,023 | (1,411) | 4,922 | 2,475 | 1,681 | 570 | 1,513 | (69) | 7,535 |
| 2022 | F22 | 7,400 | 8,253 | 797 | 1,079 | 2,526 | 20,055 | 20,039 | 88 | 4,250 | 2,641 | 1,188 | 497 | 1,309 | 708 | 8,278 |
| 2023 | F23 | 17,257 | 18,443 | 3,140 | 2,254 | 3,468 | 44,562 | 44,510 | 11,324 | 9,202 | 22,004 | 1,834 | 606 | 8,977 | 5,129 | 13,380 |
| 2024 | F24 | 21,612 | 20,301 | 4,336 | 2,502 | 4,626 | 53,377 | 53,294 | 14,177 | 11,902 | 19,625 | 2,042 | 591 | (203) | 3,869 | 18,029 |
| 2025 | F25 | 26,100 | 22,489 | 4,688 | 2,829 | 6,404 | 62,510 | 62,409 | 15,773 | 14,904 | 14,379 | 2,270 | 797 | 2,136 | 4 | 18,185 |
| Q1 2025 | Q126 | 5,541 (net) | 5,418 (net) | 947 | 573 | 1,351 | n/p | 13,830 | 3,563 | 2,999 | n/p | 480 (sum of expense lines) | n/p | n/p | n/p | n/p |
| Q1 2026 | Q126 | 6,510 (net) | 6,050 (net) | 1,130 | 690 | 1,828 | n/p | 16,208 | 3,945 | 3,747 | n/p | 691 (sum of expense lines) | n/p | n/p | n/p | n/p |

n/p = not presented in the quarterly release. Q126 presents revenue lines as "Net Revenues" by type, not gross.

**Gross bookings / GMV: not disclosed as an RMB amount in any 20-F read.** The filer gives only growth rates. **Units (room nights, tickets): not disclosed** at group level in any 20-F read (F25 gives a room-night growth figure only for a sub-brand: *"In 2025, Country Retreats recorded a 21% year-over-year increase in room nights"*). A take rate (revenue / GMV) therefore **cannot be computed** from the filings.

GMV statements found, verbatim:
- F20: *"Our GMV decreased by 51%, 72%, 51%, and 45% in the first, second, third, and fourth quarter of 2020, each comparing to the respective periods in 2019."*
- F21: *"This was in line with the 25% increase in accommodation reservation GMV..."* and *"Transportation GMV increased by 22% in 2021..."*
- F22: *"This was in line with the 18% decrease in accommodation reservation GMV, primarily due to the surges of COVID-19 infections in certain regions of China."*
- F23: *"In 2023, our core online travel agency business (including Qunar) reached a record high, achieving a year-over-year increase in GMV of nearly 130% and a growth of about 30% compared to 2019."* Accommodation GMV +170%, transportation GMV +120% (2023).
- F24: accommodation reservation GMV +19%, transportation ticketing GMV +8% (2024). F25: accommodation reservation GMV +17%, transportation ticketing GMV +6% (2025).
- F25, on take rates: *"Our products and services have different, sometimes contrasting, GMV contributions and take rates. In addition, GMVs, take rates, and terms of travel products and services may vary depending on the specific ecosystem partners providing them."*

Revenue basis, verbatim (F25 MD&A): *"Under most circumstances, we do not take ownership of the products and services being sold. Instead, we act as an agent in substantially all of our transactions. Our risk of loss due to obligations for canceled hotel and airline ticket reservations is thus relatively remote. Accordingly, we recognize revenues primarily based on commissions earned rather than transaction value."* F25 note: *"The Company presents revenues from such transactions on a net basis ... The amounts of accommodation reservation service revenues recognized on a gross basis were immaterial..."* F25 cost of revenues includes *"direct costs of principal travel tour services"*.

### Computed ratios (COMPUTATION; denominators are net revenues)
| Year | Take rate | Operating margin | SBC/OCF | Capex/net rev | (OCF-SBC-capex)/net rev | S&M/net rev |
|---|---|---|---|---|---|---|
| 2019 | not computable (GMV n/d) | 14.1% | 23.4% | 2.3% | 13.4% | 26.1% |
| 2020 | n/c | -7.8% | n/m (OCF negative) | 2.9% | -34.0% | 24.1% |
| 2021 | n/c | -7.0% | 67.9% | 2.8% | 1.1% | 24.6% |
| 2022 | n/c | 0.4% | 45.0% | 2.5% | 4.8% | 21.2% |
| 2023 | n/c | 25.4% | 8.3% | 1.4% | 44.0% | 20.7% |
| 2024 | n/c | 26.6% | 10.4% | 1.1% | 31.9% | 22.3% |
| 2025 | n/c | 25.3% | 15.8% | 1.3% | 18.1% | 23.9% |
| Q1 2025 / Q1 2026 | n/c | 25.8% / 24.3% | n/p | n/p | n/p | 21.7% / 23.1% |
| TTM to 2026-03-31 (FY25 + Q1 26 - Q1 25) | n/c | 24.9% (16,155 / 64,787) | n/p | n/p | n/p | 24.2% |

- SBC/OCF cumulative 2021-2025: 9,015 / 61,124 = **14.7%**.
- The 2020 collapse: net revenues 35,666 -> 18,316 = **-48.6%** (computed); GMV by quarter -51% / -72% / -51% / -45% (F20); room nights n/d. First year above 2019: net revenues 2023 (44,510, F23); GMV 2023 for the core OTA business including Qunar (F23 "about 30% compared to 2019"); units n/d.
- 2025 OCF fell to 14,379 from 19,625 while operating income rose; the advances-from-customers line added 4 against 3,869 in 2024 (F25 CF). F25 net income of 33,386 includes a 15,409 "Gain from acquirement of business or disposal of long-term investments", removed in the CF reconciliation. Recorded, not interpreted.

### Customer-deposit float in OCF
Trip.com's OCF **includes** customer advances and supplier payables. F25 note: *"Cash payments received from travelers in advance of the Company completing its performance obligations are included in "Advances from customers" in the Company's consolidated balance sheets and are mainly comprised of amounts estimated to be payable to travel suppliers as well as the Company's estimated future revenues for its commissions."* Combined swing of the two operating lines (COMPUTATION): 2019 +2,751; 2020 -11,835; 2021 +1,444; 2022 +2,017; 2023 +14,106; 2024 +3,666; 2025 +2,140. No change in the caption of either line across F19-F25 beyond wording ("Increase in" / "Increase/(decrease) in"). F25 also carries a separate "Increase in accrued liability for rewards program" line (648 / 1,408 / 810 for 2023-2025).

### Like-for-like limits against Airbnb
- No GMV amount, so no take rate. No units.
- Revenue mix: transportation ticketing (air and rail) is 36% of 2025 total revenues (F25); Airbnb has none.
- Mostly China and outbound Chinese travel. The group is under an SAMR anti-monopoly investigation (F25: *"in January 2026, we received notice that the SAMR commenced an investigation into whether we have abused or are abusing a dominant market position to engage in monopolistic conduct pursuant to the PRC Anti-Monopoly Law."*).

---
## 4. HOTELS AS A SUBSTITUTE: MARRIOTT INTERNATIONAL (MAR, CIK 0001048286) - USD

### Source documents
| Tag | Document | Filed | Accession |
|---|---|---|---|
| M19 | 10-K FY2019 (mar-q42019x10k.htm) | 2020-02-27 | 0001628280-20-002376 |
| M20 | 10-K FY2020 (mar-20201231.htm) | 2021-02-18 | 0001628280-21-002433 |
| M21 | 10-K FY2021 (mar-20211231.htm) | 2022-02-15 | 0001628280-22-002666 |
| M25 | 10-K FY2025 (mar-20251231.htm) | 2026-02-10 | 0001048286-26-000007 |

The brief asked for 2019-2021 from the FY2025 10-K. **M25 presents RevPAR only for 2025 against 2024 and fee revenues only for 2023-2025**, so 2019, 2020 and 2021 were taken from M19, M20 and M21. The rung was not blocked; the figures simply are not in M25.

RevPAR definition, verbatim.
- M25: *"We believe Revenue per Available Room ("RevPAR"), which we calculate by dividing property level room revenue by total rooms available for the period, is a meaningful indicator of our performance because it measures the period-over-period change in room revenues. ... Unless otherwise stated, RevPAR, occupancy, and ADR statistics are on a systemwide basis for comparable properties, and all changes refer to year-over-year changes for the comparable period. Comparisons to prior periods are on a constant U.S. dollar basis..."* Comparable properties: *"hotels in our system that were open and operating under one of our brands since the beginning of the last full calendar year (since January 1, 2024 for the current period) and have not, in either the current or previous year: (1) undergone significant room or public space renovations or expansions, (2) been converted between company-operated and franchised, or (3) sustained substantial property damage or business interruption."*
- M20 differs: *"which we calculate by dividing room sales for comparable properties by room nights available for the period"*, and comparable properties include *"properties closed or otherwise experiencing interruptions related to COVID-19, which we continue to classify as comparable."* The occupancy denominator includes *"rooms in hotels temporarily closed due to issues related to COVID-19"*.

| Year | Src | Worldwide comparable systemwide RevPAR | Change as filed | Gross fee revenues ($M) | of which: base mgmt / franchise / incentive | Net fee revenues ($M, after contract investment amortization) |
|---|---|---|---|---|---|---|
| 2019 | M19 | $117.30 | +1.3% vs 2018 | 3,823 | 1,180 / 2,006 / 637 | 3,761 (M20) |
| 2020 | M20 | $46.28 | (60.2)% vs 2019 | 1,683 | 443 / 1,153 / 87 | 1,551 |
| 2021 | M21 | $74.66 | +60.4% vs 2020; M21 text: *"Comparable systemwide constant dollar RevPAR in 2021 compared to pre-pandemic 2019 levels declined ... 36.5 percent worldwide"* | 2,694 | 669 / 1,790 / 235 | 2,619 |
| 2025 | M25 | $128.80 | +2.0% vs 2024 | 5,438 | 1,322 / 3,325 / 791 | 5,303 |

Also in M25: gross fee revenues 2024 5,170 and 2023 4,824. M20 quarterly: *"Worldwide comparable systemwide constant dollar RevPAR declined 23 percent in the 2020 first quarter, 84 percent in the 2020 second quarter, 66 percent in the 2020 third quarter, and 64 percent in the 2020 fourth quarter, compared to the same periods in 2019."*

COMPUTATION: gross fee revenues 2020/2019 = 0.440; 2025/2019 = 1.422. The RevPAR dollar levels come from different comparable-property sets and different exchange-rate bases each year, so the dollar figures are not a consistent series. Only each filing's own percentage change is like-for-like.

### IHG figures recorded in `Test Runs/2026-09-13 Run - IHG InterContinental Hotels.md` (read only, not edited; sources as that file states them)
- Fee business revenue $M: 2019 1,510; 2020 823; 2021 1,153; 2022 1,434; 2023 1,672; 2024 1,774; 2025 1,897. The run file cites the fee margin reconciliations in the 20-F FY2021 (2017-2021; 2021 re-presented to $1,144M for IFRS 17 in FY2023) and FY2023/FY2025 (2022-2025).
- Global RevPAR change: 2019 -0.3%; 2020 -52.5%; 2021 +46.0%; 2023 +16.1%; 2024 +3.0%; 2025 +1.5%. The run file cites the KPI pages of each 20-F.
- System gross revenue $bn: 2019 27.9; 2020 13.5; 2025 35.2 (20-F KPI pages; 20-F FY2020 quoted as *"$ 13.5 bn 2019: $27.9bn"*).
- The run file's competitor row also records Marriott RevPAR 2020 vs 2019 at -60.2% and fee revenue 2020/2019 at 0.440. Both agree with M20 above.

---
## 5. VERBATIM PASSAGES: Airbnb named, alternative accommodations, multi-listing, supplier direct

EDGAR full-text search, run only through `tools/sources.py fts_count` with bare 10-digit CIKs, 2026-09-13. These are hit counts across all forms and years; they are prompts, not evidence. BKNG "Airbnb" 52 (10-K only: 12; one earlier attempt returned HTTP 500, and the retry returned 12); EXPE "Airbnb" 60 (10-K: 12); TCOM "Airbnb" 0 (20-F: 0, on retry after HTTP 500); EXPE "in addition to listing on" 18; BKNG "in addition to listing on" 0; TCOM 0 (on retry after HTTP 500); "multi-list" and "cross-list": 0 for all three; "list on multiple": 0 for all three; BKNG "multiple platforms" 10, all 2012-2014 KAYAK-merger documents and 10-Qs/10-K from 2013-2014, outside the window and not opened for quotation; EXPE "supplier direct" 50; TCOM "homestay" 1 (F25). Every quotation below comes from the primary document on disk.

### (a) Airbnb named as a competitor
**Booking Holdings**
- K19 (0001075531-20-000011), competition risk factor, list of competitors: *"online accommodation search and/or reservation services that are currently focused primarily on alternative accommodations, including individually owned properties such as homes and apartments, such as Airbnb, Vrbo (which is owned by Expedia Group), Tujia (in which Trip.com Group and Expedia Group hold investments) and Xiaozhu;"* Same bullet in K20 (0001075531-21-000019).
- K19: *"For example, companies such as Airbnb and Expedia Group offer services providing alternative accommodation property owners, particularly individuals, an online place to list their accommodations where travelers can search and book such properties and compete directly with our alternative accommodation services. In addition, Airbnb, which owns HotelTonight, offers some hotel reservations through its online platforms."*
- K22 (0001075531-23-000016): *"Companies such as Airbnb and Expedia Group, primarily through Vrbo, offer services providing alternative accommodation property owners an online place to list their accommodations where travelers can search and book such properties and compete directly with our alternative accommodation services. In addition, companies such as Airbnb that have in the past exclusively provided alternative accommodations have expanded into traditional accommodation offerings."*
- K25 (0001075531-26-000009): *"The market for accommodations covers a wide range of property types including alternative accommodations and companies like Airbnb and Vrbo (owned by Expedia) compete directly with our accommodations businesses."* Near-identical sentences appear in K23 and K24.

**Expedia Group**
- K20 (0001324424-21-000015): *"In particular, we face increasing competition from other OTAs and alternative accommodations in many regions, such as Booking Holdings and its subsidiaries Booking.com and Agoda.com; Trip.com, which in some cases may have more favorable offerings for travelers or suppliers, including pricing and supply breadth; and Airbnb. ... Airbnb, Booking Holdings and other providers of alternative accommodations provide an alternative to hotel rooms and compete with alternative accommodation properties available through Expedia Group brands, including Vrbo. The continued growth of alternative accommodation providers could affect overall travel patterns generally and the demand for our services specifically in facilitating reservations at hotels and alternative accommodations. Furthermore, Airbnb and similar providers could increasingly look to add other travel services, such as tours, activities, hotel and flight bookings, any of which could further extend their reach into the travel market as they seek to compete with the traditional OTAs."*
- K24 (0001324424-25-000008): *"In particular, we face intense competition from other OTAs and alternative accommodation providers in many regions, such as Booking Holdings (through its Booking.com, Priceline.com and Agoda.com brands), Airbnb, and Trip.com, any of which may have more favorable offerings for travelers or suppliers, including pricing and supply breadth. Airbnb, Booking Holdings and other providers of alternative accommodations provide an alternative to hotel rooms and compete with alternative accommodation properties available through Expedia Group brands, including Vrbo."*
- K25 (0001324424-26-000008): *"OTAs such as Booking.com, alternative accommodation providers such as Airbnb, and travel metasearch services;"* and *"In recent years, Airbnb has expanded into tours, activities, and hotel bookings, and discussed expansion into flight bookings, and Booking.com has expanded its flight booking services."*
- K19 through K25, industry overview: *"In addition, the increasing popularity of the "sharing economy," accelerated by online penetration, has had a direct impact on the travel and lodging industry. Businesses such as Airbnb, Vrbo and Booking.com have emerged as the leaders, bringing incremental alternative accommodation inventory to the market."* This is the K25 wording. K19-K21 add "(previously HomeAway, which Expedia Group acquired in December 2015)" after Vrbo and "(owned by Booking Holdings)" after Booking.com, and K19-K24 read "alternative accommodation and vacation rental inventory".

**Trip.com Group:** no passage naming Airbnb in any of F19-F25 (local text search of all seven 20-Fs, and the EDGAR full-text count of 0).

### (b) Alternative accommodations / listing counts
**Booking.com** alternative accommodation property counts and room-night mix (10-K text):
| Year-end | Total properties | Hotels, motels, resorts | Homes, apartments and other unique places to stay | Alt-accom share of Booking.com room nights | Src |
|---|---|---|---|---|---|
| 2019 | ~2,580,000 | ~460,000 | ~2,120,000 | n/f in K19 (K21 says 2021 "about 29%, which was about the same as the share of room nights in 2019") | K19 |
| 2020 | ~2,373,000 | ~434,000 | ~1,939,000 | n/f (K21: 2021 "down slightly from 2020") | K20 |
| 2021 | ~2.4 million | over 400,000 | over 1.9 million | about 29% | K21 |
| 2022 | over 2.7 million | over 400,000 | ~2.3 million | ~30% | K22 |
| 2023 | ~3.4 million | over 475,000 | over 2.9 million | ~33% | K23 |
| 2024 | ~4.0 million | ~500,000 | ~3.5 million | ~35% | K24 |
| 2025 | ~4.4 million | ~500,000 | ~3.9 million | ~36% | K25 |

- K25 verbatim: *"The mix of Booking.com's room nights booked for alternative accommodation properties in 2025 was approximately 36%, up versus approximately 35% in 2024. We have observed a longer-term trend of an increasing mix of room nights booked for alternative accommodation properties as consumer demand for these types of properties has grown, and as we have increased the number and variety of these properties on Booking.com. We may experience lower profit margins due to additional costs from offering alternative accommodations, such as increased customer service or certain partner related costs. As our alternative accommodation business grows, these different characteristics may negatively impact our profit margins."*
- K25 risk factor: *"Alternative accommodations typically consist of single units or a small collection of independent units, and may result in additional costs for us, which can result in more limited booking opportunities and lower profit margins than hotels, motels, and resorts. Further, alternative accommodations may be unavailable during peak periods due to seasonality or owner use. To the extent alternative accommodations represent an increasing percentage of the properties we add to our platforms, we expect that our room-night growth rate and property growth rate will continue to diverge over time, and the number of reservations per property will likely continue to decrease."*

**Expedia/Vrbo** listing counts are in Section 2 (Vrbo-specific disclosure).

**Trip.com:** F20-F25 customer description: *"We have a broad base of customers, which primarily consist of our ecosystem partners, including airlines and other air ticket partners, hotel and alternative accommodation partners, and various value-added travel products and services partners, such as insurance companies."* (F25 reads "consists"). F21 describes Tujia as *"a leading alternative accommodation platform in China"* among its investments. F25: *"it has been publicly reported that in December 2025, the Yunnan Provincial Tourism Homestay Industry Association announced a decision to initiate an anti-monopoly effort against certain online travel agency platforms, alleging that these platforms leveraged their dominant market position to engage in unfair competition practices. We were specifically named in that decision."* No listing count is disclosed.

### (c) Hosts or properties on multiple platforms / suppliers shifting inventory
- **Expedia K22 (0001324424-23-000007):** *"Other competitors have arisen, including vacation rental property managers such as Vacasa, who operate their own booking sites in addition to listing on Airbnb, Vrbo, and Booking.com, and are expected to continue to grow as a percentage of the global accommodation market."*
- **Expedia K23 (0001324424-24-000007):** *"Other competitors have arisen, including vacation rental property managers, who operate their own booking sites in addition to listing on Airbnb, Vrbo, and Booking.com, and are expected to continue to grow as a percentage of the global accommodations market."*
- **Expedia K24 (0001324424-25-000008):** *"Other competitors have arisen, including vacation rental property managers, who operate their own booking sites in addition to listing on Airbnb, Vrbo, and Booking.com."*
- **Expedia K25 (0001324424-26-000008):** *"Other competitors have arisen, including alternative accommodation property managers, who operate their own booking sites in addition to listing on Airbnb, Vrbo, and Booking.com."*
- Expedia K21 (0001324424-22-000009) and later, on bookings leaving the platform: *"We have also experienced instances where properties listed on our sites are copied and travelers booking these properties outside of our websites are the subject of fraudulent requests for payment. In other cases, travelers have been asked to pay for their booking of properties listed on our website directly to the alternative accommodation operator and outside of our website, resulting in loss of revenue for us and increased risk of fraud for the traveler."*
- Expedia K25, suppliers who are also competitors: *"We face competition from airlines, hotels, alternative accommodation websites, rental car companies, cruise operators and other travel service providers, whether working individually or collectively, some of which are suppliers to our websites."*
- **Booking K24 (0001075531-25-000010) and K25:** *"If occupancy rates increase, accommodation providers often limit their offerings to OTCs."* K23 (0001075531-24-000014): *"If occupancy rates increase, accommodation providers often limit the amount of business that flows through certain distribution channels."*
- Booking K25, parity: *"For example, Booking.com has implemented changes to address the DMA prohibition on parity arrangements in the European Economic Area and the requirements regarding the usage of data across services, which could adversely impact our business."*
- Booking K19, on alternative accommodation owners listing elsewhere: see the (a) quote, *"companies such as Airbnb and Expedia Group offer services providing alternative accommodation property owners, particularly individuals, an online place to list their accommodations"*.
- **Trip.com F25 (0001193125-26-183379)**, on suppliers: *"The hotel partners may reduce the commission rates on bookings made through us."* and, on airlines, *"although we currently have supply relationships with these airlines, they also compete with us for ticket bookings and have entered into similar arrangements with many of our competitors and may continue to do so in the future."*
- No passage using "multi-list", "cross-list" or "also listed" was found in any of the 21 annual filings read.

### (d) Direct booking by hotels and loyalty programs as competition
- **Expedia K25:** *"We face increasing competition from travel supplier direct websites. In some cases, supplier direct channels offer advantages to travelers, such as their own specific loyalty programs, complimentary services such as Wi-Fi, and better pricing."* Also: *"Further, airlines and lodging companies are aggressively pursuing direct online distribution of their products and services."* K19-K24 carry the same supplier-direct language.
- **Booking K19:** *"travel service providers such as accommodation providers, rental car companies and airlines, many of which have their own branded online platforms to which they drive business, including large hotel chains such as Marriott International, Hilton and Intercontinental Hotel Group and emerging hotel chains such as OYO Rooms, as well as joint efforts by travel service providers such as Room Key, an online hotel reservation service owned by several major hotel companies;"*
- **Booking K25:** *"Barriers to entry are low, and we compete with online travel companies ("OTCs"), travel service providers offering direct booking (such as airlines, hotels, and rental car companies), traditional travel agencies and operators..."* and *"Travel service providers may offer lower prices through direct or AI-enabled channels ... Consolidation among travel service providers or AI-enabled alternative travel offerings could result in lower OTC commission rates, increased discounting, and greater incentives for consumers to join closed-user groups."*
- **Trip.com F25:** *"We may also face increasing competition from hotels and airlines as they increase their direct selling efforts or engage in alliances with other travel service providers, as well as content platforms and social networks entering into the travel industry."*

---
## 6. CROSS-CHECKS (XBRL companyfacts against the filed statement text)
| Company | Figure | Filed text (document) | XBRL fact (accession) | Match |
|---|---|---|---|---|
| BKNG | Revenue FY2025 | 26,917 (K25 income statement) | Revenues 26,917,000,000 (0001075531-26-000009) | yes |
| BKNG | OCF FY2019 | 4,865 (K19 cash flow statement) | NetCashProvidedByUsedInOperatingActivities 4,865,000,000 (0001075531-20-000011) | yes |
| EXPE | SBC FY2025 | 398 (K25 CF "Amortization of stock-based compensation") | ShareBasedCompensation 398,000,000 (0001324424-26-000008) | yes |
| EXPE | Operating income FY2019 | 903 (K19) | OperatingIncomeLoss 903,000,000 (0001324424-20-000009) | yes |
| TCOM | Net revenues FY2025 | RMB 62,409 (F25) | Revenues CNY 62,409,000,000 (0001193125-26-183379); the tag carries net revenues | yes |
| TCOM | OCF FY2019 | RMB 7,333 (F19) | NetCashProvidedByUsedInOperatingActivities CNY 7,333,000,000 (0001193125-20-102627) | yes |

All other figures in this file were read from the filed document text (HTML converted to text), not from XBRL.

---
## 7. COVERAGE, GAPS AND LIKE-FOR-LIKE LIMITS

**Coverage.** Three competitors (Booking Holdings, Expedia Group, Trip.com Group) plus one hotel substitute (Marriott, RevPAR and fees only), with a read-only note of the IHG run file. 21 annual filings (7 x 10-K BKNG, 7 x 10-K EXPE, 7 x 20-F TCOM), two 10-Qs (BKNG, EXPE Q2 2026), four MAR 10-Ks, four EXPE earnings-release exhibits, and two TCOM 6-Ks.

**Unavailable figures and why.**
| Figure | Status | Reason |
|---|---|---|
| Expedia room nights, absolute, in any 10-K | not disclosed | 10-Ks give growth rates only. Absolute figures were taken from 8-K EX-99.1 releases, which are furnished rather than filed, and the basis switches from stayed (2019-2020) to booked (2024-2026). 2021-2023 absolute figures were not collected; the releases for those years were not fetched. |
| Expedia room nights, first year above 2019 | not determinable like-for-like | Basis change (stayed vs booked) |
| Vrbo gross bookings, revenue, nights, take rate after 2019 | not disclosed | Vrbo stopped being a reportable segment from K20 |
| Vrbo traveler service fee rate and any 2019-2021 change | not disclosed | 10-Ks disclose only that the fee exists and that it lifted 2019 revenue |
| Booking performance vs brand marketing split after 2019 | not disclosed numerically | One "Marketing expenses" line from K20 onward |
| Trip.com GMV (RMB amount) | not disclosed | Growth rates only, in F20-F25 |
| Trip.com take rate | not computable | No GMV amount |
| Trip.com units (room nights, tickets) | not disclosed at group level | Only a sub-brand room-night growth rate in F25 |
| Trip.com H1 2026 | not yet published | Results due 2026-09-15 US time (N26); Q1 2026 used instead, with no cash-flow statement in the release |
| Marriott 2019-2021 RevPAR and fees in the FY2025 10-K | not in that document | Taken from M19, M20 and M21 instead |
| Booking deferred-merchant-bookings-only CF swing | not presented separately | The CF line bundles "other current liabilities"; the balance-sheet change was used as a proxy and includes FX |
| Blocked rungs | none | Every EDGAR document fetch succeeded. EDGAR full-text search returned HTTP 500 on four queries; each was retried and returned a count, and no error was treated as a zero. |

**Where a like-for-like comparison with Airbnb's net take rate is not possible or needs adjustment.**
1. **Trip.com:** no gross bookings figure, so no take rate at all.
2. **Booking:** total revenue includes advertising and other revenue (KAYAK, OpenTable) with no gross bookings behind it. The ex-advertising ratio (13.82% for 2025) removes that. Merchant revenue includes *"revenues from facilitating payments, such as credit card processing rebates and customer processing fees"* and travel insurance. Discounts are netted in revenue (K25: *"Some of these initiatives, such as discounts, may result in lower ADRs and lower revenues as a percentage of gross bookings as they can reduce the daily room rate and are recognized as contra-revenue."*). Gross bookings include rental cars, flights and attractions as well as accommodations, and roughly 64% of Booking.com room nights in 2025 were at properties other than alternative accommodations (computed as 100% minus the ~36% alternative-accommodation mix in K25).
3. **Expedia:** revenue includes advertising (trivago, EG Advertising); B2B partner commissions sit in selling and marketing rather than netted against revenue; agency gross bookings are mostly air, with air revenue recognized at booking. The ex-advertising ratio (11.24% for 2025) removes only the first of these.
4. **Timing, all three:** gross bookings are recorded at booking and revenue at stay. 2020 ratios and half-year ratios are distorted by this (e.g. Booking 2020 19.20%, H1 2026 12.30%).
5. **Operating cash flow:** Booking, Expedia and Trip.com all carry customer prepayments and supplier payables inside operating cash flow, per the quotations above. SBC/OCF and (OCF-SBC-capex)/revenue therefore include working-capital float for all three. Any Airbnb comparison must use the same treatment of Airbnb's own funds payable and restricted cash, as the main run defines it.
6. **Marketing:** Expedia's "selling and marketing" includes indirect personnel costs and B2B partner commissions. Booking's "marketing expenses" is performance plus brand only (sales and personnel are separate lines). Trip.com's "sales and marketing" is a single line. These captions do not measure the same thing.

No conclusion about any company's moat is drawn in this file.

Status: COMPLETE (2026-09-13).
