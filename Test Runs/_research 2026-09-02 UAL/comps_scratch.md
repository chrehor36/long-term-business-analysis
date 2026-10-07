# AIRLINE LOYALTY COMPARABLES - SEC PRIMARY FILINGS
Research scratch for the UAL run. Compiled 2026-09-02.
**Filed facts only. No verdict is formed here on franchise status or business quality.**

Source discipline: every figure below carries CIK, accession number, filing date, document
name and (where applicable) exhibit number. All documents fetched from www.sec.gov /
data.sec.gov with User-Agent "Chris Hrehor chrehor36@gmail.com".

---

## PART A - DELTA AIR LINES, INC. (CIK 0000027904)

### A.1 The American Express figure, three years, verbatim

| FY | Figure | Accession | Filed | Primary document |
|---|---|---|---|---|
| 2023 | $6.8 billion | 0000027904-24-000003 | 2024-02-12 | `dal-20231231.htm` |
| 2024 | $7.4 billion | 0000027904-25-000004 | 2025-02-11 | `dal-20241231.htm` |
| 2025 | $8.2 billion | 0000027904-26-000013 | 2026-02-11 | `dal-20251231.htm` |

**FY2023, Item 1. Business (Loyalty Program):**
> "Our most significant and valuable contract to sell miles relates to our co-brand credit
> card relationship with American Express. In 2023, remuneration from American Express
> totaled $6.8 billion, which we expect to increase by 10% in 2024 and grow to $10 billion
> over the long-term."

*(Note: the FY2023 10-K carries the figure only in Item 1. The FY2023 MD&A "Cash Flow"
paragraph does not repeat it. Delta's phrasing that year is "remuneration", not "total cash
payments".)*

**FY2024, Item 1. Business (Loyalty Program):**
> "Our most significant and valuable contract to sell miles relates to our co-brand credit
> card relationship with American Express. In 2024, remuneration from American Express
> totaled $7.4 billion, which we expect to grow to $10 billion over the long-term."

**FY2024, Item 7. MD&A, "Cash Flow":**
> "During 2024, operating activities generated $8.0 billion, primarily from ticket sales and
> the sale of SkyMiles to our partners. Total cash sales of SkyMiles to American Express were
> $7.4 billion during 2024, an increase of approximately 8% compared to 2023."

**FY2025, Item 1. Business (Loyalty Program):**
> "Our most significant and valuable contract to sell miles relates to our co-brand credit
> card relationship with American Express. In 2025, remuneration from American Express
> totaled $8.2 billion, which we expect to grow to $10 billion over the next few years."

**FY2025, Item 7. MD&A, "Cash Flow":**
> "During 2025, operating activities generated $8.3 billion, primarily from ticket sales and
> the sale of SkyMiles to our partners. Remuneration from American Express related to the
> SkyMiles program were $8.2 billion during 2025, an increase of approximately 11% compared
> to 2024."

**FY2025, Item 7. MD&A, "Financial Condition and Liquidity - Sale of Miles to Participating
Companies":**
> "Remuneration from American Express was $8.2 billion during 2025, an increase of 11%
> compared to the prior year."

Implied growth: 2023 -> 2024 = +8.8%; 2024 -> 2025 = +10.8%. Delta's own MD&A rounds these to
"approximately 8%" and "approximately 11%".

### A.2 Delta loyalty program deferred revenue (the deferred loyalty liability)

**XBRL note (negative result, recorded):** the two endpoints specified
(`us-gaap/FrequentFlierLiabilityCurrent` and `us-gaap/FrequentFlierLiabilityNoncurrent`,
CIK 0000027904) both return data, but the series **terminate at 2018-03-31**. Last 10-K
values are 2017-12-31: current $1,822m, noncurrent $2,296m (accession 0000027904-18-000006,
filed 2018-02-23). Delta abandoned those tags on adopting ASC 606 and the line is now labelled
"Loyalty program deferred revenue". A `companyfacts` sweep of CIK 0000027904 shows **only**
`FrequentFlierLiabilityCurrent`, `FrequentFlierLiabilityNoncurrent` and
`IncreaseDecreaseInFrequentFlyerLiability` matching /loyalt|frequent/, and
`us-gaap/ContractWithCustomerLiabilityCurrent|Noncurrent` return HTTP 404 for this CIK.
**No FY2023/24/25 loyalty liability is retrievable from the specified XBRL concepts.** The
figures below are therefore read off the filed balance sheet, which is the higher-ranking
source under operator rule 4 in any case.

Consolidated Balance Sheets, $ millions (FY2025 10-K, accession 0000027904-26-000013, filed
2026-02-11; FY2023 figures from FY2023 10-K, accession 0000027904-24-000003, filed 2024-02-12):

| At Dec 31 | Current | Noncurrent | Total |
|---|---|---|---|
| 2022 | 3,434 | 4,448 | 7,882 |
| 2023 | 3,908 | 4,512 | 8,420 |
| 2024 | 4,314 | 4,512 | 8,826 |
| 2025 | 4,876 | 4,386 | 9,262 |

Loyalty program activity table, Note 2 Revenue Recognition, FY2025 10-K ($ millions):

| | 2025 | 2024 | 2023 |
|---|---|---|---|
| Balance at January 1 | 8,826 | 8,420 | 7,882 |
| Miles earned | 4,892 | 4,463 | 4,173 |
| Travel miles redeemed | (4,237) | (3,841) | (3,462) |
| Non-travel miles redeemed | (219) | (216) | (173) |
| Balance at December 31 | 9,262 | 8,826 | 8,420 |

### A.3 Delta revenue lines that touch loyalty (FY2025 10-K, Note 2), $ millions

Passenger revenue by category:

| | 2025 | 2024 | 2023 |
|---|---|---|---|
| Ticket | 45,488 | 45,096 | 43,596 |
| Loyalty travel awards | 4,237 | 3,841 | 3,462 |
| Travel-related services | 2,043 | 1,957 | 1,851 |
| **Total passenger revenue** | **51,768** | **50,894** | **48,909** |

Other revenue:

| | 2025 | 2024 | 2023 |
|---|---|---|---|
| Refinery | 5,077 | 4,642 | 3,379 |
| Loyalty program | 3,362 | 3,297 | 3,093 |
| Ancillary businesses | 937 | 772 | 840 |
| Miscellaneous | 1,320 | 1,216 | 1,104 |
| **Total other revenue** | **10,696** | **9,927** | **8,416** |

Delta describes the "Loyalty program" line in other revenue as revenue "allocated to the
remaining performance obligations, primarily brand value ... recorded as loyalty program in
other revenue as miles are delivered" (FY2025 10-K, Note 2).

Operating detail also disclosed FY2025: "In 2025, 12% of revenue miles flown on Delta were
from award travel, as program members redeemed miles in the loyalty program for approximately
35 million award tickets" (10% and ~30 million in both 2023 and 2024).

Total operating revenue for scale: 2025 $63,364m; 2024 $61,643m (FY2025 10-K MD&A).

---

## PART B - AMERICAN AIRLINES GROUP INC. (CIK 0000006201) / AMERICAN AIRLINES, INC.
## (CIK 0000004515) - THE AAdvantage FINANCING AND ITS STANDALONE FIGURES

### B.1 Answer to the question asked
**Yes.** AAG published standalone AAdvantage financial statements as a Reg FD furnishing.
They appear in **Exhibit 99.1, "Excerpts from AAdvantage Presentation", to the Form 8-K dated
March 8, 2021, accession 0000006201-21-000022, filed 2021-03-08** (co-filed by AAG CIK
0000006201 and American Airlines, Inc. CIK 0000004515; document `aainvestorpresentation.htm`).
An EDGAR full-text search of forms 8-K for "AAdvantage" over 2021-02-01 to 2021-05-31 returns
nine hits, of which the AAG ones are only accessions -000022 (2021-03-08), -000024
(2021-03-10), -000029 (2021-03-24) and -000053 (Q1 earnings, 2021-04-22). **Exhibit 99.1 to
-000022 is the sole standalone AAdvantage financial disclosure.**

The 8-K body states the purpose plainly:
> "In connection with commencing discussions with potential investors in the proposed
> AAdvantage Financing ..., American Airlines Group Inc. (the 'Company') is making available
> certain information about AAdvantage Loyalty IP Ltd., a newly formed Cayman Islands exempted
> company ..., excerpts of which are attached to this report as Exhibit 99.1."
(8-K, accession 0000006201-21-000022, Item 7.01)

**Status of the numbers:** they are **unaudited pro forma** figures of AAdvantage Holdings 1,
Ltd. (HoldCo1), prepared as if the Contribution Transactions and the Intercompany Agreement
had been consummated on January 1, 2018, and **not** giving effect to the financing itself.
Annex A to the exhibit states: "The unaudited pro forma consolidated financial information of
HoldCo1 included in the Presentation has not been prepared in accordance with the requirements
of Article 11 of Regulation S-X"; and "Neither the assumptions underlying the unaudited pro
forma adjustments, nor the resulting HoldCo1 Unaudited Pro Forma Consolidated Financial
Information have been audited or reviewed in accordance with any generally accepted auditing
standards." Also: "certain of the financial information provided herein is not required to be
included, and will not be provided, in AAG's or American's periodic and other reports filed
with the SEC."

### B.2 AAdvantage pro forma financial profile
All figures: Exhibit 99.1 to 8-K accession 0000006201-21-000022, filed 2021-03-08, slide 37
("AAdvantage Summary Pro-Forma Financial Profile"). $ millions.

| | 2018 | 2019 | 2020 |
|---|---|---|---|
| Total miles issued, % YoY | +14.1% | +2.3% | (49.5)% |
| Total miles redeemed, % YoY | +12.4% | +6.2% | (52.6)% |
| **Cash flow statement** | | | |
| Cash received from sales to American and other airlines | 1,419 | 1,513 | 529 |
| Cash received from sales to co-branded card and other non-air partners | 3,510 | 3,861 | 2,908 |
| Cash received from sales directly to AAdvantage Program members | 557 | 538 | 213 |
| **Total cash received from sales** | **5,486** | **5,912** | **3,650** |
| % growth YoY | | +7.8% | (38.3)% |
| Cash paid for redemptions | (2,677) | (2,637) | (749) |
| Cash paid for operating expenses | (125) | (130) | (84) |
| **Total cash paid for redemptions and opex** | **(2,802)** | **(2,767)** | **(833)** |
| **Net cash flows provided by operating activities** | **2,684** | **3,145** | **2,817** |
| % of total cash received from sales | 48.9% | 53.2% | 77.2% |
| **Income statement** | | | |
| Revenues, net of redemption costs | 3,183 | 3,041 | 2,173 |
| Operating expenses, excl. D&A | (125) | (130) | (84) |
| **Adjusted EBITDA** | **3,058** | **2,911** | **2,089** |
| Net income | 3,208 | 3,239 | 2,420 |
| **Balance sheet** | | | |
| Intercompany receivables | 10,884 | 14,360 | 17,511 |
| Accounts receivable | 573 | 575 | 555 |
| Other assets | 93 | 89 | 80 |
| **Total assets** | **11,550** | **15,024** | **18,146** |
| Total liabilities | 8,342 | 8,577 | 9,279 |
| Stockholder's equity | 3,208 | 6,447 | 8,867 |

Quarterly cash detail (same exhibit, slide 38): FY2019 total cash received $5,912m
(Q1 1,730 / Q2 1,389 / Q3 1,361 / Q4 1,432); FY2020 total $3,650m (Q1 1,684 / Q2 636 /
Q3 659 / Q4 671). Co-brand and non-air partner sales alone: FY2019 $3,861m
(Q1 1,206 / Q2 878 / Q3 872 / Q4 905); FY2020 $2,908m (Q1 1,265 / Q2 573 / Q3 526 / Q4 544),
i.e. **third party sales fell 25% in 2020 while American's passenger revenue fell 65%** (same
exhibit, slide 34).

### B.3 The 20% EBITDA margin - what it is and what it is not
Slide 24 ("AAdvantage Pricing and Cash Flow Mechanics") and the Annex A definition:
> "Adjustments to Cash received from sales to American and other airlines represent the gross
> cash receipts from sales by Loyalty Issuer to American that would have occurred based on the
> terms of the Intercompany Agreement, which provide for **Loyalty Issuer to earn an EBITDA
> margin of 20% only on mileage sales to American** and not on mileage sales to American
> purchased by American pursuant to other airline loyalty programs."

Repeated as a note on slides 37 and 38: "EBITDA margin of 20% applied only to sale of miles to
American and not any other cash flow." **This is a transfer price set inside the structure, not
a market margin.** Annex A also warns: "The pricing in the Intercompany Agreement may not be
the same as amounts that would have been established through agreements with unrelated
parties."

### B.4 The "margin" comparison table across the three programs
Exhibit 99.1 to 8-K 0000006201-21-000022, filed 2021-03-08, slide 26, headed "2019A Pro Forma
Financial Data". This is AAG's own compilation; the Delta and United columns are AAG's
characterisation of competitors, not those companies' filings.

| 2019A | AAdvantage | Delta SkyMiles | United MileagePlus |
|---|---|---|---|
| Date founded | 1981 | 1981 | 1981 |
| Total members | 115mm+ | 100mm+ | 100mm+ |
| Card issuer | Dual issuer (Citi / Barclays) | Sole issuer (American Express) | Sole issuer (Chase Bank) |
| Partner airlines (total / domestic) | 20+ / 5 | 25+ / 0 | 35+ / 4 |
| **Cash collections** | **$5.9bn** | **$6.1bn** | **$5.3bn** |
| **Net cash from operations** | **$3.1bn** | **$2.4bn** | **$2.3bn** |
| Third party / other share of cash flows | 74% | 68% | 71% |
| Airlines share of cash flows | 26% | 32% | 29% |
| **Margin** | **53%** | **39%** | **44%** |

Footnote 2 to that slide defines the margin: **"Defined as cash flow from operations divided
by total cash collections."** Total members footnote: "Total AAdvantage members defined as
total accounts in the database for the life of the program prior to removal of inactive
accounts as of YE 2020"; Delta and United member counts are "based on public statements as of
August and March 2020, respectively."

### B.5 Other AAdvantage operating disclosures in the same exhibit
- "AAdvantage launched in 1981, had ~23 million active members ... and generated ~$5.9 billion
  in pro forma cash sales in 2019" (slide 7). 2020: ~16 million active members, $3,650m pro
  forma cash sales.
- "~74% of pro forma cash flows came from 3rd parties in 2019 including Citi and Barclays,
  partners in travel, retail, lifestyle and hospitality and direct sales to program members"
  (slide 7).
- "In 2019, AAdvantage members contributed nearly 61% of American's ticket revenue" (slide 30);
  footnote: "This amount was 56% in 2020."
- 2019 average annual flight revenue per customer: AAdvantage member $1,220 vs non-member $408
  (+199%); 2019 average yield 18.9 cents vs 13.1 cents (+44%) (slide 30).
- Active members: 19mm (2017), 21mm (2018), 23mm (2019), ~16mm (2020) (slide 31).
- "American Airlines credit card spend as a % of each partner's total 2019 credit volume:
  Citi 24%, Barclays 28%, Mastercard 12%" (slide 27, sourced to "AA data, Nielsen, Accenture
  research and analysis").
- Redemption side, 2019: "$2.6bn Pro Forma Redemption and Travel Benefits Provided"; non-air
  travel redemption is "a small amount ... (3%)" (slide 25).
- Barclays "Partner with AAdvantage since 2005"; Citi a "34 year relationship with legacy
  American" (slide 27).

**No implied valuation of AAdvantage is disclosed anywhere in the exhibit.** The only
enterprise-value figure on the deck is AAG's own: "Enterprise Value $49,521" million, with
"Market Cap (as of March 3, 2021) 14,182" (slide 8, pro forma capitalization). AAdvantage
itself is never assigned a value; the closest statement is the non-numeric "Financing unlocks
value of the AAdvantage program" (slide 10).

### B.6 The financing - amount, coupons, maturities

**Announcement.** 8-K accession 0000006201-21-000022, filed 2021-03-08, Item 8.01 and Exhibit
99.2 (press release dated March 8, 2021): proposed $2.5bn senior secured notes due 2026,
$2.5bn senior secured notes due 2029, plus a $2.5bn senior secured term loan facility.
Proceeds to repay the drawn $550m under the CARES Act / U.S. Treasury term loan facility and
for general corporate purposes.

**Pricing and upsize.** 8-K accession 0000006201-21-000024, filed 2021-03-10, Exhibit 99.1
(press release dated March 10, 2021), headline "AMERICAN AIRLINES ANNOUNCES UPSIZE OF
AADVANTAGE FINANCING TO $10.0 BILLION AND PRICING OF SENIOR SECURED NOTES":
> "An aggregate of $3.5 billion in principal amount of 5.50% senior secured notes due 2026 and
> an aggregate of $3.0 billion in principal amount of 5.75% senior secured notes due 2029 ...
> The Notes will be issued at a price to investors of 100% of their principal amount.
> Concurrent with the issuance of the Notes, American and AAdvantage Loyalty IP Ltd. expect to
> enter into a credit agreement providing for a $3.5 billion term loan facility ... In total,
> the Notes and New AAdvantage Term Loan Facility will provide gross proceeds of $10.0 billion,
> an increase of $2.5 billion from the anticipated original $7.5 billion transaction size, at a
> blended average annual coupon rate of 5.575%."

**Closing.** 8-K accession 0000006201-21-000029, filed 2021-03-24, Item 1.01. Closed
2021-03-24. $3.5bn 5.50% notes due 2026 and $3.0bn 5.75% notes due 2029 issued under an
Indenture dated March 24, 2021 with Wilmington Trust, N.A. as trustee and collateral
custodian; $3.5bn term loan fully drawn on the closing date, Barclays Bank PLC as
administrative agent. Co-issuers: American Airlines, Inc. and AAdvantage Loyalty IP Ltd.
(Cayman). Guarantors: AAG (senior **unsecured**), plus AAdvantage Holdings 1, Ltd. and
AAdvantage Holdings 2, Ltd. (senior **secured**).

Payment terms (same 8-K):
- Interest quarterly in arrears on the 20th of January, April, July and October, from
  2021-07-20.
- 2026 Notes mature 2026-04-20; principal repaid in quarterly instalments of approximately
  $291,666,667 from 2023-07-20.
- 2029 Notes mature 2029-04-20; principal repaid in quarterly instalments of $250,000,000 from
  2026-07-20.
- Term loan scheduled maturity 2028-04-20; interest at LIBOR (floor 0.75%) plus 4.75%;
  quarterly amortisation of $175.0m from July 2023.
- Redemption at 100% plus a make-whole premium.
- ~$550m of net proceeds used to prepay in full the Treasury Loan Agreement, which was
  terminated (Item 1.02).

Collateral: "a first-priority security interest in, and pledge of, various agreements with
respect to the AAdvantage program ... (including all payments thereunder) and rights under an
intercompany agreement and certain IP Licenses ..., certain deposit accounts that will receive
cash under the AAdvantage Agreements, certain reserve accounts, the equity of each of Loyalty
Issuer and the SPV Guarantors and substantially all other assets of Loyalty Issuer and the SPV
Guarantors."

### B.7 The debt service coverage ratio covenant - the actual numbers
The 8-Ks and the 10-Ks describe this only qualitatively ("a minimum debt service coverage
ratio at specified determination dates" / "a peak debt service coverage ratio, pursuant to
which failure to comply with a certain threshold may result in early repayment"). **The
numeric schedule is in the indenture itself:**

Indenture dated as of March 24, 2021, **filed as Exhibit 4.3 to AAG's Form 10-Q for the
quarter ended March 31, 2021, accession 0000006201-21-000054, filed 2021-04-22**, document
`ex43q121aadvantagexindentu.htm` (and incorporated by reference as Exhibit 4.197 to AAG's
FY2021 Form 10-K, accession 0000006201-22-000026, filed 2022-02-22):

> "'Peak Debt Service Coverage Ratio' shall mean, with respect to any Determination Date, the
> ratio obtained by dividing (i) the sum (without duplication) of (x) the aggregate amount of
> Collections deposited to the Collection Account during the Related Quarterly Reporting Period
> and (y) Cure Amounts deposited to the Collection Account on or prior to such Determination
> Date ... by (ii) the Maximum Quarterly Debt Service for such Determination Date ..."

> "'Peak Debt Service Coverage Ratio Test' shall be satisfied as of any Determination Date if
> the Peak Debt Service Coverage Ratio is not less than (i) for the Determination Dates in July
> 2021, October 2021 and January 2022, **0.75 to 1.00**; (ii) for the Determination Dates in
> April 2022, July 2022 and October 2022, **1.00 to 1.00**; (iii) for the Determination Dates
> in January 2023 and April 2023, **1.50 to 1.00**; and (iv) for any Determination Date
> thereafter, **2.00 to 1.00**."

Cure mechanic (Section 4.33): the issuers may deposit Cure Amounts into the Collection Account
to satisfy the test, but "no more than five (5) times in the aggregate prior to the final
maturity date of the 2029 Notes and no more than two times in any twelve (12) month period."

Failing the test triggers an Early Amortization Event, not an event of default; the Early
Amortization Payment is "50% of the excess" of the notes' pro rata share of quarterly
Collections over the amounts due in the waterfall (Indenture, definition of "Early
Amortization Payment"). This matches slide 10 of Exhibit 99.1: "Robust de-leveraging mechanism
based on peak DSCR test offers additional protection in case of a prolonged downturn" and "50%
excess CF sweep based on predefined triggers."

Other covenants of note (8-K 0000006201-21-000029, Item 1.01):
- At least 90% of quarterly AAdvantage cash receipts must be directed into the collection
  account.
- AAG must maintain minimum liquidity of at least **$2.0 billion** (unrestricted cash plus
  undrawn revolver availability) at the close of any business day.
- American and Loyalty Issuer are "prohibited from substantially reducing the AAdvantage
  program business or modifying the terms of the AAdvantage program in a manner that would
  reasonably be expected to materially impair repayment" (a "Payment Material Adverse Effect"),
  and AAG and subsidiaries are "prohibited from ... operating a competing loyalty program."
- Cap on pre-paid mile sales: mandatory prepayment on net proceeds from pre-paid AAdvantage
  mile purchases exceeding $500.0m (required only above $505.0m in aggregate); covenant limit
  on selling pre-paid miles "in excess of $550.0 million in the aggregate."
- "A bankruptcy event of American is not itself an event of default; following an American
  bankruptcy, an event of default would only occur if American failed to satisfy certain
  enumerated bankruptcy case milestones, including an assumption of the AAdvantage Financing
  by a certain date."
- IP License termination on default "would trigger a liquidated damages payment in an amount
  that is greater than the initial principal amount of the Notes and the Loans."

### B.8 Status of the AAdvantage financing at FY2025 - NOT repaid
AAG FY2025 Form 10-K, **accession 0000006201-26-000014, filed 2026-02-18**, document
`aal-20251231.htm`, Note 4 (Debt), section (c) "AAdvantage Financing", and the long-term debt
table. Principal outstanding, $ millions:

| Instrument | 12/31/2025 | 12/31/2024 |
|---|---|---|
| 5.50% senior secured notes, instalments until due April 2026 | 583 | 1,750 |
| 5.75% senior secured notes, instalments beginning July 2026 until due April 2029 | 3,000 | 3,000 |
| 2021 AAdvantage Term Loan Facility, variable rate 6.13%, due April 2028 | 2,264 | 2,450 |
| 2025 AAdvantage Term Loan Facility, variable rate 7.13%, due May 2032 | 995 | -- |
| **Total AAdvantage Financing** | **6,842** | **7,200** |

AAG total long-term debt 12/31/2025 was $28,594m before discounts (of which secured $24,219m).

Amendments disclosed in the same note:
- **Second Amendment, 2025-03-24**: term loans outstanding of approximately $2.3 billion
  "were replaced with new term loans in the same principal amount", now bearing SOFR (0.00%
  floor) + 2.25% (or base rate + 1.25%); quarterly amortisation cut to 0.25% of principal
  outstanding at 2025-03-24 (approximately $6 million per quarter) from July 2025, balance due
  at maturity April 2028.
- **Third Amendment, 2025-05-28**: $1.0 billion of **incremental** term loans (the "2025
  AAdvantage Term Loan Facility") due 2032-05-28, at SOFR + 3.25% (or base + 2.25%), quarterly
  amortisation approximately $3 million from July 2025. "The net proceeds from the 2025
  AAdvantage Term Loan Facility were used, in part, to repay the Convertible Notes."

So: the 2026 notes have amortised down to $583m and mature 2026-04-20; the 2029 notes are
untouched at $3.0bn; the term loan leg has been repriced, extended and **increased**. The
AAdvantage collateral package remains in place and AAG states "As of the most recent applicable
measurement dates, we were in compliance with each of the foregoing covenants."

### B.9 AAG disclosed loyalty figures, FY2023-FY2025
Same FY2025 10-K (accession 0000006201-26-000014, filed 2026-02-18).

**Co-brand cash payments (the AAG analogue of Delta's Amex number), Item 1 Business and MD&A:**
> "Starting in 2026, Citibank N.A. (Citi) became the exclusive issuer of the AAdvantage
> co-branded credit card portfolio in the U.S. Cash payments from co-branded credit card and
> other partners were $6.2 billion and $6.1 billion during 2025 and 2024, respectively. Cash
> remuneration in 2024 included a one-time cash payment related to the new co-branded credit
> card agreement announced in December 2024."

FY2024 10-K (accession 0000006201-25-000010, filed 2025-02-19), Item 1 and MD&A:
> "During 2024 and 2023, cash payments from co-branded credit card and other partners were
> $6.1 billion and $5.2 billion, respectively, an increase of 17% year-over-year. Cash
> remuneration in 2024 included a one-time cash payment related to the new co-branded credit
> card agreement announced in December 2024."

| Year | AAG co-brand and other partner cash payments |
|---|---|
| 2023 | $5.2 billion |
| 2024 | $6.1 billion (includes an undisclosed one-time payment from Citi) |
| 2025 | $6.2 billion |

**Caution on comparability with Delta:** AAG's figure is "co-branded credit card **and other
partners**", i.e. broader than Delta's single-counterparty Amex number; and the 2024 figure is
inflated by an unquantified one-time signing payment that "will be amortized over the life of
the new agreement beginning in 2026."

**Revenue, $ millions (FY2025 10-K, Note 1(m)):**

| | 2025 | 2024 | 2023 |
|---|---|---|---|
| Passenger travel | 45,607 | 45,743 | 44,914 |
| Loyalty revenue - travel | 4,036 | 3,843 | 3,598 |
| **Total passenger revenue** | **49,643** | **49,586** | **48,512** |
| Cargo | 839 | 804 | 812 |
| Loyalty revenue - marketing services | 3,511 | 3,257 | 2,929 |
| Other revenue | 640 | 564 | 535 |
| **Total operating revenues** | **54,633** | **54,211** | **52,788** |

**Loyalty program liability (contract liability), $ millions:**

| At Dec 31 | Current | Noncurrent | Total |
|---|---|---|---|
| 2023 | 3,453 | 5,874 | 9,327 |
| 2024 | 3,556 | 6,498 | 10,054 |
| 2025 | 3,725 | 6,839 | 10,564 |

Roll-forward for 2025: opening $10,054m, deferral of revenue $4,445m, recognition of revenue
$(3,935)m, closing $10,564m. The balance "includes a one-time cash payment related to the new
co-branded credit card agreement announced in December 2024, which will be amortized over the
life of the new agreement beginning in 2026."

Other FY2025 operating disclosures: "During 2025, our members redeemed approximately 18 million
awards"; mileage credit contracts with partners have "remaining terms generally from one to 10
years as of December 31, 2025"; in July 2025 AAG extended Mastercard as exclusive payment
network under a new 10-year contract.

---

## DOCUMENT INDEX (everything cited above)

| # | CIK | Accession | Filed | Form | Document / exhibit |
|---|---|---|---|---|---|
| 1 | 0000027904 | 0000027904-24-000003 | 2024-02-12 | 10-K FY2023 | `dal-20231231.htm` |
| 2 | 0000027904 | 0000027904-25-000004 | 2025-02-11 | 10-K FY2024 | `dal-20241231.htm` |
| 3 | 0000027904 | 0000027904-26-000013 | 2026-02-11 | 10-K FY2025 | `dal-20251231.htm` |
| 4 | 0000027904 | 0000027904-18-000006 | 2018-02-23 | 10-K FY2017 | last 10-K using `FrequentFlierLiability*` tags |
| 5 | 0000006201 / 0000004515 | 0000006201-21-000022 | 2021-03-08 | 8-K | body `aal-20210308.htm`; **Ex. 99.1** `aainvestorpresentation.htm`; **Ex. 99.2** `aex992securednotespressrel.htm` |
| 6 | 0000006201 / 0000004515 | 0000006201-21-000024 | 2021-03-10 | 8-K | body `aal-20210310.htm`; **Ex. 99.1** `aex991securednotespricingp.htm` |
| 7 | 0000006201 / 0000004515 | 0000006201-21-000029 | 2021-03-24 | 8-K | `aal-20210324.htm` (closing, Items 1.01 / 1.02 / 2.03) |
| 8 | 0000006201 | 0000006201-21-000054 | 2021-04-22 | 10-Q Q1 2021 | **Ex. 4.3** `ex43q121aadvantagexindentu.htm` (Indenture); Ex. 10.4 `ex104q121aadvantagexcredit.htm` (term loan credit agreement) |
| 9 | 0000006201 | 0000006201-22-000026 | 2022-02-22 | 10-K FY2021 | `aal-20211231.htm` (covenant description; Ex. 4.197 incorporation by reference) |
| 10 | 0000006201 | 0000006201-25-000010 | 2025-02-19 | 10-K FY2024 | `aal-20241231.htm` |
| 11 | 0000006201 | 0000006201-26-000014 | 2026-02-18 | 10-K FY2025 | `aal-20251231.htm` |

XBRL endpoints queried (Delta): `companyconcept/CIK0000027904/us-gaap/FrequentFlierLiabilityCurrent.json`,
`.../FrequentFlierLiabilityNoncurrent.json` (both terminate 2018-03-31);
`.../ContractWithCustomerLiabilityCurrent.json` and `...Noncurrent.json` (HTTP 404);
`companyfacts/CIK0000027904.json` (no post-2017 loyalty liability concept exists).

## NOTHING WAS BLOCKED
Every document sought was obtained. The one negative result is recorded above in A.2: the
FY2023/24/25 Delta loyalty liability is **not** available from the two XBRL concepts specified
in the brief, because Delta stopped using those tags after adopting ASC 606; the figures were
taken from the filed balance sheet instead.

## STANDING CAUTIONS ON THESE COMPARABLES
1. Every AAdvantage figure in B.2 through B.5 is **unaudited pro forma**, prepared by AAG for a
   144A marketing exercise, resting on an intercompany transfer price (the 20% EBITDA margin)
   that AAG itself says "may not be the same as amounts that would have been established
   through agreements with unrelated parties."
2. The 2019 three-way comparison in B.4 is AAG's compilation of its own competitors. The Delta
   and United columns are not sourced to Delta's or United's filings.
3. AAG's co-brand cash payments line covers all co-brand and non-air partners; Delta's covers
   American Express alone. They are not like for like.
4. AAG's 2024 co-brand cash figure contains an unquantified one-time Citi signing payment.
