# MSFT — BALANCE-SHEET / PERIMETER LEG
**Company:** Microsoft Corporation · **CIK** 0000789019
**Sources:** SEC filings only. No press, no news, no analyst estimates, no memory.
**Compiled:** 2026-09-06

## SOURCE REGISTER (operator rule 4 — the filing gets read)

| FY | Form | Period | Filed | Accession | Primary document |
|---|---|---|---|---|---|
| FY2021 | 10-K | 2021-06-30 | 2021-07-29 | 0001564590-21-039151 | msft-10k_20210630.htm |
| FY2022 | 10-K | 2022-06-30 | 2022-07-28 | 0001564590-22-026876 | msft-10k_20220630.htm |
| FY2023 | 10-K | 2023-06-30 | 2023-07-27 | 0000950170-23-035122 | msft-20230630.htm |
| FY2024 | 10-K | 2024-06-30 | 2024-07-30 | 0000950170-24-087843 | msft-20240630.htm |
| FY2025 | 10-K | 2025-06-30 | 2025-07-30 | 0000950170-25-100235 | msft-20250630.htm |
| FY2026 | 10-K | 2026-06-30 | 2026-07-29 | 0001193125-26-323660 | msft-20260630.htm |
| Q1 FY2026 | 10-Q | 2025-09-30 | 2025-10-29 | 0001193125-25-256321 | msft-20250930.htm |
| Q2 FY2026 | 10-Q | 2025-12-31 | 2026-01-28 | 0001193125-26-027207 | msft-20251231.htm |
| Q3 FY2026 | 10-Q | 2026-03-31 | 2026-04-29 | 0001193125-26-191507 | msft-20260331.htm |

Accessions verified against `https://data.sec.gov/submissions/CIK0000789019.json`.
Fiscal year ends June 30. FY2026 = year ended 2026-06-30.

**Cross-check (operator rule 4):** FY2026 total revenue of $331,839m, net income $133,749m and total assets $758,376m were read off the filed income statement and balance sheet, and tie to the MD&A summary-results table and the Note 3 / Note 4 / Note 6 footnote detail used throughout. Operating cash flow of $182,935m ties across the FY2026 and FY2025 cash-flow statements. The lease reconciliation in section 2.7 ties the Note 13 maturity table to the MD&A contractual-obligations table exactly, in three separate years.

---

# ASSIGNMENT 1 — THE OPENAI RELATIONSHIP, FROM THE FILINGS ONLY

## 1.1 Is OpenAI named? Occurrence count per vintage

| Vintage | Occurrences of "OpenAI" | Where |
|---|---|---|
| FY2021 | **0** | not named at all |
| FY2022 | **0** | not named at all |
| FY2023 | **7** | Item 1 business description (2), Item 1A risk factors (2). No financial-statement mention. |
| FY2024 | **9** | Item 1 business (2), Item 1 competition (2), Item 1A risk factors (2). **No financial-statement mention.** |
| FY2025 | **13** | XBRL tag `msft:OpenAIGlobalLlcMember` (1), Item 1A (2), Item 7 MD&A (2), **Note 1 accounting policy (1)**, **Note 3 Other income (1)** |
| FY2026 | **30** | XBRL tags (4), Item 1A (1), Item 7 MD&A (8), non-GAAP reconciliation (3), **Note 1 (7)**, **Note 3 (2)** |

**The finding in the count:** OpenAI first enters the **financial statements** in **FY2025**, not FY2023 or FY2024, despite the investment dating from the 2019 partnership and the "third phase" announced January 2023. FY2023 and FY2024 name OpenAI only in the business description and risk factors. FY2024's $1.5 billion of net losses from OpenAI was **not separately disclosed in the FY2024 10-K itself**; it appears retrospectively in the FY2026 non-GAAP table and the FY2026 Note 3.

### FY2023 / FY2024 — the whole of it (business + risk factor only)

> "We have a long-term partnership with OpenAI, a leading AI research and deployment company. We deploy OpenAI's models across our consumer and enterprise products. As OpenAI's exclusive cloud provider, Azure powers all of OpenAI's workloads. We have also increased our investments in the development and deployment of specialized supercomputing systems to accelerate OpenAI's research."
> — FY2023 10-K, Item 1; **identical in FY2024 10-K, Item 1**

> "In January 2023 we announced the third phase of our OpenAI strategic partnership."
> — FY2023 and FY2024 10-Ks, Item 1A (acquisitions/JV risk factor)

> "This AI may be developed by Microsoft or others, including our strategic partner, OpenAI."
> — FY2023, FY2024 and FY2025 10-Ks, Item 1A

FY2024 also names OpenAI as a **competitor**, twice:
> "Our AI offerings compete with AI products from hyperscalers such as Amazon and Google, as well as products from other emerging competitors, including Anthropic, OpenAI, Meta, and other open source offerings, many of which are also current or potential partners."
> — FY2024 10-K, Item 1, Competition (Azure)

> "Our Search and news advertising business competes with Google, OpenAI, and a wide array of websites…"
> — FY2024 10-K, Item 1, Competition

## 1.2 How is the investment accounted for?

### FY2025 — first appearance of the accounting policy (Note 1)

> "Investments that are considered variable interest entities ("VIEs") are evaluated to determine whether we are the primary beneficiary of the VIE, in which case we would be required to consolidate the entity… **We have determined we are not the primary beneficiary of any of our VIE investments. Therefore, our VIE investments are not consolidated and the majority are accounted for under the equity method of accounting. We have an investment in OpenAI Global, LLC ("OpenAI") and have made total funding commitments of $13 billion. The investment is accounted for under the equity method of accounting.**"
> — FY2025 10-K, Note 1, Investments

### FY2026 — expanded (Note 1)

> "We have determined we are not the primary beneficiary of any of our VIE investments. Therefore, our VIE investments are not consolidated and the majority are accounted for under the equity method of accounting or the measurement alternative.
> **We have a long-term strategic partnership with OpenAI. In October 2025, we signed a new definitive agreement with OpenAI that extends this partnership. We have an investment accounted for under the equity method that represents an approximate 25% interest on an as-converted basis.** As an equity method investee, OpenAI is a related party as defined in Accounting Standards Codification Topic 850, Related Party Disclosures ("ASC 850")…
> **We calculate our equity method income or loss using the hypothetical liquidation at book value ("HLBV") method because our liquidation rights and priorities differ from our underlying ownership interest. Under the HLBV method, we recognize income or loss based on the change in the amount we would receive if the net assets of the investee were distributed at book value.**"
> — FY2026 10-K, Note 1, Investments

**Verdict: NOT consolidated. Equity method. VIE, but Microsoft is not the primary beneficiary.** Income/loss is computed by HLBV, not by pro-rata share — an explicit statement that Microsoft's economics differ from its 25% nominal stake.

## 1.3 CARRYING VALUE of the OpenAI investment

**NOT FOUND IN FILINGS.** No 10-K discloses a standalone carrying value for the OpenAI investment in any year FY2023-FY2026.

The only related figure is the **aggregate** equity-method line in Note 4:

> "As of June 30, 2026 and 2025, equity investments without readily determinable fair values measured at cost with adjustments for observable changes in price or impairments were $12.4 billion and $2.9 billion, respectively, and **equity investments measured using the equity method were $12.0 billion and $6.0 billion**, respectively."
> — FY2026 10-K, Note 4, Investments

That $12.0bn is *all* equity-method investees, not OpenAI alone. Balance-sheet context, Note 4 FY2026:
- Total investments, recorded basis: **$113,191 million**, of which Cash & equivalents $20,935m, Short-term investments $55,908m, **Equity and other investments $36,348m**.
- Total equity investments recorded basis: **$27,240m** (FY2026) vs **$12,673m** (FY2025), of which "Other" (non-fair-value: cost/equity-method/NAV) $24,567m vs $9,141m.

**This is the perimeter hole.** A ~25% as-converted interest in the counterparty that generated $24.1bn of Microsoft's revenue has no separately stated book value in the filing.

## 1.4 EQUITY-METHOD GAINS AND LOSSES RECOGNISED — the dollar figures

### Note 3 — Other income (expense), net, FY2026 10-K (In millions)

| Component | 2026 | 2025 | 2024 |
|---|---|---|---|
| Interest and dividends income | 3,301 | 2,647 | 3,157 |
| Interest expense | (3,051) | (2,385) | (2,935) |
| Net recognized gains (losses) on investments | 4,385 | (349) | (118) |
| Net gains (losses) on derivatives | 1,867 | (260) | (187) |
| Net gains (losses) on FX remeasurements | (527) | 171 | (244) |
| **Other, net** | **4,722** | **(4,725)** | **(1,319)** |
| **Total** | **10,697** | **(4,901)** | **(1,646)** |

> "**Other income (expense), net included $6.5 billion of net gains, $4.8 billion of net losses, and $1.5 billion of net losses for fiscal years 2026, 2025, and 2024, respectively, from investments in OpenAI, primarily net recognized gains (losses) on our equity method investment reflected in Other, net. The net gains recorded for fiscal year 2026 primarily relate to the dilution gain from the OpenAI Recapitalization.**"
> — FY2026 10-K, Note 3

The FY2025 10-K said far less about the same $4.8bn:
> "Other, net primarily reflects net recognized losses on equity method investments, including OpenAI."
> — FY2025 10-K, Note 3 (and Item 7 MD&A, identical sentence)

FY2025's Note 3 gave **no dollar figure at all** for OpenAI. The three-year series only became visible in FY2026.

### The precise figures, from the FY2026 non-GAAP reconciliation

> "Adjusted other income (expense), net, adjusted net income, and adjusted diluted EPS are non-GAAP financial measures which exclude net (gains) losses from investments in OpenAI."

| (In millions, except per share) | 2026 | 2025 | 2024 |
|---|---|---|---|
| Other income (expense), net | 10,697 | (4,901) | (1,646) |
| **Net (gains) losses from investments in OpenAI** | **(6,530)** | **4,763** | **1,482** |
| Adjusted other income (expense), net (non-GAAP) | 4,167 | (138) | (164) |
| Net income | 133,749 | 101,832 | 88,136 |
| Net (gains) losses from investments in OpenAI, net of tax of $1,567, $(1,143), and $(356) | (4,963) | 3,620 | 1,126 |
| **Adjusted net income (non-GAAP)** | **128,786** | **105,452** | **89,262** |
| Diluted EPS | 17.95 | 13.64 | 11.80 |
| Net (gains) losses from investments in OpenAI | (0.67) | 0.49 | 0.15 |
| **Adjusted diluted EPS (non-GAAP)** | **17.28** | **14.13** | **11.95** |

**Pre-tax OpenAI P&L by year: FY2024 −$1,482m · FY2025 −$4,763m · FY2026 +$6,530m.**
After tax: FY2024 −$1,126m · FY2025 −$3,620m · FY2026 +$4,963m.

> "Current year net income and diluted EPS were positively impacted by net gains from investments in OpenAI, which resulted in an increase in net income and diluted EPS of $5.0 billion and $0.67, respectively. Prior year net income and diluted EPS were negatively impacted by net losses from investments in OpenAI, which resulted in a decrease in net income and diluted EPS of $3.6 billion and $0.49, respectively."
> — FY2026 10-K, Item 7

**Analyst note (not from filings, arithmetic only):** the FY2026 +$6,530m is *not* operating economics. The filing says it "primarily relate[s] to the dilution gain from the OpenAI Recapitalization" — a non-cash mark arising because Microsoft's ownership percentage **fell**. Cumulative pre-tax OpenAI P&L FY2024-FY2026 = **+$285m**, i.e. roughly nil, and the positive sign is carried entirely by a dilution gain. Microsoft itself excludes this line from its own headline non-GAAP measure.

## 1.5 FUNDING COMMITMENTS

> "**We have an investment in OpenAI Global, LLC ("OpenAI") and have made total funding commitments of $13 billion.**"
> — FY2025 10-K, Note 1

> "**We have made total funding commitments of $13.0 billion related to our investment, of which $11.9 billion has been funded as of June 30, 2026.**"
> — FY2026 10-K, Note 1

| | FY2025 | FY2026 |
|---|---|---|
| Total funding commitment | $13 billion | $13.0 billion |
| Funded | **not disclosed** | $11.9 billion |
| Remaining unfunded | **not disclosed** | **$1.1 billion** (arithmetic) |

**FY2025 did not disclose how much of the $13bn had been funded.** FY2026 is the first year the funded portion appears. Remaining commitment is small: $1.1bn.

## 1.6 RESTRUCTURING OF THE RELATIONSHIP — the FY2026 disclosure, verbatim

> "**In October 2025, OpenAI formed a public benefit corporation and completed a recapitalization ("OpenAI Recapitalization"). During fiscal year 2026, our proportionate ownership of OpenAI decreased due to the OpenAI Recapitalization and other funding activity, and we recorded dilution gains in other income (expense), net.**"
> — FY2026 10-K, Note 1

> "We have a long-term strategic partnership with OpenAI which was originally established in 2019. **In October 2025 and April 2026, we extended this partnership** and continue to build on our shared vision to advance artificial intelligence responsibly and make its benefits broadly accessible. Microsoft is a major investor in OpenAI and will continue to receive revenue-sharing payments. We hold rights to OpenAI's intellectual property, including models and infrastructure, for integration into our products."
> — FY2026 10-K, Item 7, Industry Trends and Opportunities

> "In October 2025, we signed a new definitive agreement with OpenAI that extends this partnership. We have an investment accounted for under the equity method that represents an approximate 25% interest on an as-converted basis."
> — FY2026 10-K, Note 1

### What was DELETED between FY2025 and FY2026 — the negative finding

FY2025 Item 7 said:

> "Microsoft and OpenAI maintain a long-term strategic partnership originally established in 2019. Microsoft is a major investor in OpenAI, and the companies have reciprocal revenue-sharing arrangements. We hold rights to OpenAI's intellectual property, including models and infrastructure, for integration into our products. **The OpenAI API is exclusive to Azure, runs on Azure, and is available through the Azure OpenAI Service. We also have a right of first refusal on OpenAI's new capacity needs.**"
> — FY2025 10-K, Item 7

The FY2026 equivalent paragraph **drops** all of the following:
- **"The OpenAI API is exclusive to Azure, runs on Azure"** — gone.
- **"We also have a right of first refusal on OpenAI's new capacity needs"** — gone.
- "reciprocal revenue-sharing arrangements" becomes the one-directional "will continue to receive revenue-sharing payments".

And the FY2023/FY2024 Item 1 sentence **"As OpenAI's exclusive cloud provider, Azure powers all of OpenAI's workloads"** does not appear in FY2026.

**The exclusivity language and the right of first refusal were removed from the filing.** The 10-K does not say they were terminated, and does not say what replaced them. That is the disclosure gap.

## 1.7 Related-party vs concentration

**Related party: YES, from FY2026 only.**

> "**As an equity method investee, OpenAI is a related party as defined in Accounting Standards Codification Topic 850, Related Party Disclosures ("ASC 850"). In accordance with ASC 850, we are disclosing revenue and accounts receivable balances from transactions with OpenAI. For fiscal year 2026, we recorded revenue from commercial arrangements with OpenAI, inclusive of revenue-sharing payments, of $24.1 billion, and accounts receivable from OpenAI as of June 30, 2026 was $6.0 billion.**"
> — FY2026 10-K, Note 1

**Concentration: NO. The word "concentration" does not appear in the FY2025 or FY2026 10-K at all** (0 occurrences, both files). There is no customer-concentration footnote, no "no single customer accounted for more than 10%" statement, no credit-risk concentration disclosure. The $24.1bn is disclosed **because ASC 850 requires related-party disclosure**, not because of any concentration rule.

## 1.8 Azure revenue attributable to OpenAI / OpenAI as a customer

**Partially disclosed, FY2026 only, and only in aggregate.**

- **$24.1 billion** of FY2026 revenue "from commercial arrangements with OpenAI, **inclusive of revenue-sharing payments**".
- **$6.0 billion** accounts receivable from OpenAI at 2026-06-30.

**NOT FOUND IN FILINGS:**
- The split of the $24.1bn between **Azure compute sold to OpenAI** and **revenue-sharing payments received from OpenAI**. These are economically opposite items (one is a sale to a customer; one is a royalty on the investee's revenue) and they are combined into one number.
- Which **segment** the $24.1bn lands in.
- Any FY2025 or FY2024 comparative for the $24.1bn. **It is a single-year, no-comparative disclosure.**
- Any disclosure of amounts Microsoft **pays** OpenAI, or of the reciprocal side of the revenue share.
- Whether the $6.0bn receivable is current, its ageing, or any credit allowance against it.

### Scale check (arithmetic on filed figures)
- $24.1bn ÷ $331,839m total FY2026 revenue = **7.3% of Microsoft's consolidated revenue**.
- $24.1bn ÷ $137,791m Intelligent Cloud revenue = **17.5% of Intelligent Cloud**, if it all sits there.
- FY2026 Intelligent Cloud revenue rose $31,526m; $24.1bn is **76% of that increase**, if all of it is Intelligent Cloud and all of it is incremental. The filing does not permit either assumption to be tested.
- $6.0bn receivable ÷ $24.1bn revenue = **91 days of receivable** against this one counterparty.

## 1.9 SUMMARY — what the filings do NOT disclose about OpenAI

1. **Carrying value of the OpenAI investment.** Not in any year. Only an all-investee equity-method aggregate ($12.0bn FY2026).
2. **Any comparative for the $24.1bn related-party revenue.** One year, no prior-year figure.
3. **The split of $24.1bn** between Azure sales and revenue-share receipts.
4. **What Microsoft pays OpenAI**, or the terms of the revenue share (rate, duration, caps).
5. **What happened to Azure exclusivity and the right of first refusal.** The language was removed; no explanation given.
6. **The terms of the October 2025 definitive agreement or the April 2026 extension.** No IP-rights expiry date, no AGI clause, no termination provision, no compute-purchase commitment to or from OpenAI is described.
7. **Any OpenAI-specific commitment** in the commitments footnote. The $13.0bn equity commitment is in Note 1, not the commitments note; no separate OpenAI-related purchase or capacity obligation is identified anywhere.
8. **Whether any part of the $112.2bn "other purchase commitments"** (see Assignment 3) relates to OpenAI. Not stated.
9. **OpenAI's own financial statements or summarised financial information.** No ASC 323-30-50 summarised financial data for the investee is provided, despite the investee being material enough to swing net income by $5.0bn and to generate 7.3% of revenue.
10. **Ownership percentage before the recapitalization.** Only "approximate 25% interest on an as-converted basis" as of FY2026, and "our proportionate ownership… decreased". The prior percentage is never stated in any 10-K. *(The FY2026 10-Qs partially fill this: 27% at both 2025-12-31 and 2026-03-31, falling to 25% at 2026-06-30. Still nothing pre-October-2025. See Addendum.)*
11. **The size of the dilution gain separately** from the rest of the $6,530m. "Primarily relate[s] to" is as far as it goes.

---

# ASSIGNMENT 2 — FINANCE LEASES AND ASC 842

Source: Note 14 (FY2021-FY2024) / Note 13 (FY2025-FY2026), LEASES, of each 10-K.

## 2.1 The scope sentence, and how it changed

> "We have operating and finance leases for datacenters, corporate offices, research and development facilities, Microsoft Experience Centers, and certain equipment."
> — FY2021 through FY2025 10-Ks

> "We have operating and finance leases for **datacenters, corporate offices, research and development facilities, and certain equipment**."
> — FY2026 10-K, Note 13

And in Item 7:
> "We have operating and finance leases for **datacenters and related infrastructure, servers and network equipment**, corporate offices, and research and development facilities."
> — FY2026 10-K, Item 7, Other Planned Uses of Capital

**"Servers and network equipment" is added to the leased-asset description in FY2026.** Microsoft is now leasing the short-lived compute itself, not only the buildings.

## 2.2 OPERATING LEASES — balance sheet and terms

| (In millions) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Operating lease ROU assets | 11,088 | 13,148 | 14,346 | 18,961 | 24,823 | **24,177** |
| Other current liabilities (current portion) | 1,962 | 2,228 | 2,409 | 3,580 | 5,424 | 5,393 |
| Operating lease liabilities (non-current) | 9,629 | 11,489 | 12,728 | 15,497 | 17,437 | 16,532 |
| **Total operating lease liabilities** | **11,591** | **13,717** | **15,137** | **19,077** | **22,861** | **21,925** |
| Weighted-avg remaining term | 8 yrs | 8 yrs | 8 yrs | 7 yrs | 6 yrs | 6 yrs |
| Weighted-avg discount rate | 2.2% | 2.1% | 2.9% | 3.3% | 3.5% | 3.7% |
| **Operating lease cost** | **2,127** | **2,461** | **2,875** | **3,555** | **5,524** | **6,968** |

Operating leases have gone **flat to shrinking** since FY2025. The whole growth story is in finance leases.

## 2.3 FINANCE LEASES — balance sheet, terms, and cost components (separately, by year)

| (In millions) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Property and equipment, at cost | 14,107 | 17,388 | 20,538 | 32,248 | 53,876 | **82,712** |
| Accumulated depreciation | (2,306) | (3,285) | (4,647) | (6,386) | (9,861) | (15,431) |
| **Property and equipment, net (finance lease ROU)** | **11,801** | **14,103** | **15,891** | **25,862** | **44,015** | **67,281** |
| Other current liabilities (current portion) | 791 | 1,060 | 1,197 | 2,349 | 3,172 | 4,290 |
| Other long-term liabilities | 11,750 | 13,842 | 15,870 | 24,796 | 43,000 | 62,304 |
| **Total finance lease liabilities** | **12,541** | **14,902** | **17,067** | **27,145** | **46,172** | **66,594** |
| Weighted-avg remaining term | 12 yrs | 12 yrs | 11 yrs | 12 yrs | 13 yrs | 13 yrs |
| Weighted-avg discount rate | 3.4% | 3.1% | 3.4% | 3.9% | 4.2% | **4.5%** |

### Components of finance lease cost, SEPARATELY, by year

| (In millions) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| **Amortization of right-of-use assets** | **921** | **980** | **1,352** | **1,800** | **3,408** | **5,403** |
| **Interest on lease liabilities** | **386** | **429** | **501** | **734** | **1,417** | **2,547** |
| **Total finance lease cost** | **1,307** | **1,409** | **1,853** | **2,534** | **4,825** | **7,950** |

Verbatim, FY2026:
> "The components of lease expense were as follows: … Operating lease cost $6,968 $5,524 $3,555 … Finance lease cost: Amortization of right-of-use assets $5,403 $3,408 $1,800; Interest on lease liabilities 2,547 1,417 734; Total finance lease cost $7,950 $4,825 $2,534"
> — FY2026 10-K, Note 13

**Total lease cost FY2026 = $6,968m operating + $7,950m finance = $14,918m**, up from $3,434m in FY2021. A 4.3x increase in five years.

**Finance lease liabilities of $66,594m now EXCEED total long-term debt face value of $46,136m.** Microsoft's largest single interest-bearing obligation is not its bonds; it is its leases.

## 2.4 CRITICAL — ROU ASSETS OBTAINED IN EXCHANGE FOR LEASE OBLIGATIONS

This is the non-cash capital spending that does **not** appear in "Additions to property and equipment".

| (In millions) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| **Operating leases** | 4,380 | 5,268 | 3,514 | 6,703 | 7,826 | 4,555 |
| **Finance leases** | **3,290** | **4,234** | **3,128** | **11,633** | **20,511** | **24,608** |
| Combined | 7,670 | 9,502 | 6,642 | 18,336 | 28,337 | 29,163 |

Verbatim, FY2026:
> "Right-of-use assets obtained in exchange for lease obligations: Operating leases 4,555 7,826 6,703; Finance leases 24,608 20,511 11,633"
> — FY2026 10-K, Note 13, supplemental cash flow information

**Cumulative finance-lease ROU additions FY2024-FY2026 = $56,752 million.** None of it is in the capex line.

### Cash paid for lease obligations (for the owner-earnings bridge)

| (In millions) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Operating cash flows from operating leases | 2,052 | 2,368 | 2,706 | 3,550 | 4,931 | 6,443 |
| Operating cash flows from finance leases (interest) | 386 | 429 | 501 | 734 | 1,372 | 2,547 |
| **Financing cash flows from finance leases (principal)** | **648** | **896** | **1,056** | **1,286** | **2,283** | **3,101** |

**Note the mismatch.** FY2026 finance-lease ROU additions were $24,608m; cash principal repaid was $3,101m. The obligation is being added roughly **8x faster than it is being paid down**. And the principal repayment sits in **financing** activities, so it never touches free cash flow as conventionally computed from operations minus capex.

## 2.5 LEASES NOT YET COMMENCED — the forward datacentre commitment

| As of | Operating | Finance | **Total** | Commencement window | Terms |
|---|---|---|---|---|---|
| June 30, 2021 | $5.4bn | $7.3bn | **$12.7bn** | FY2022-FY2026 | 1-15 yrs |
| June 30, 2022 | $7.2bn | $8.8bn | **$16.0bn** | FY2023-FY2028 | 1-18 yrs |
| June 30, 2023 | $7.7bn | **$34.4bn** | **$42.1bn** | FY2024-FY2030 | 1-18 yrs |
| June 30, 2024 | $8.6bn | **$108.4bn** | **$117.0bn** | FY2025-FY2030 | 1-20 yrs |
| June 30, 2025 | *not split* | *not split* | **$92.7bn** | FY2026-FY2031 | 1-20 yrs |
| June 30, 2026 | *not split* | *not split* | **$329.1bn** | FY2027-FY2033 | 1-20 yrs |

Verbatim:

> "As of June 30, 2023, we have additional operating and finance leases, primarily for datacenters, that have not yet commenced of **$7.7 billion and $34.4 billion**, respectively. These operating and finance leases will commence between fiscal year 2024 and fiscal year 2030 with lease terms of 1 year to 18 years."

> "As of June 30, 2024, we had additional operating and finance leases, primarily for datacenters, that had not yet commenced of **$8.6 billion and $108.4 billion**, respectively. These operating and finance leases will commence between fiscal year 2025 and fiscal year 2030 with lease terms of 1 year to 20 years."

> "As of June 30, 2025, we had additional leases, primarily for datacenters, that had not yet commenced of **$92.7 billion**. These leases will commence between fiscal year 2026 and fiscal year 2031 with lease terms of 1 year to 20 years."

> "As of June 30, 2026, we had additional leases, primarily for datacenters, that had not yet commenced of **$329.1 billion**, **with some arrangements subject to certain contractual conditions being met**. These leases will commence between fiscal year 2027 and fiscal year 2033 with lease terms of 1 year to 20 years."
> — FY2026 10-K, Note 13

### Three findings here

1. **$329.1 billion.** That is **99% of FY2026 total revenue ($331,839m)**. It is 4.9x the on-balance-sheet finance lease liability of $66,594m. It is committed, off-balance-sheet, and will land on the balance sheet between FY2027 and FY2033.
2. **The operating/finance split was DISCONTINUED in FY2025.** FY2021-FY2024 disclosed both legs separately. FY2025 and FY2026 give one combined number. Given operating-lease liabilities are flat and shrinking, essentially all of the $329.1bn is presumptively finance, but **the filing no longer lets you verify it**. This is a reduction in disclosure quality exactly as the number became enormous.
3. **FY2026 added a hedge that was not there before:** "with some arrangements subject to certain contractual conditions being met". No amount is attached to the conditional portion. The filing does not say how much of $329.1bn is conditional, what the conditions are, or who controls them.

Also note the **FY2025 decline**: $117.0bn (FY2024) fell to $92.7bn (FY2025), because $20.5bn of finance ROU commenced during FY2025 and moved onto the balance sheet. Then FY2026 added a gross ~$261bn of new signings. The stock is being refilled far faster than it is drawn down.

## 2.6 MATURITY TABLE OF LEASE LIABILITIES, most recent year

As of June 30, 2026 (Note 13):

| Year Ending June 30 | Operating Leases | Finance Leases |
|---|---|---|
| 2027 | $6,082 | $7,121 |
| 2028 | 4,334 | 7,294 |
| 2029 | 3,146 | 6,668 |
| 2030 | 2,612 | 6,570 |
| 2031 | 2,316 | 6,543 |
| Thereafter | 6,216 | **55,490** |
| **Total lease payments** | **24,706** | **89,686** |
| Less imputed interest | (2,781) | **(23,092)** |
| **Total** | **$21,925** | **$66,594** |

**$23,092m of imputed interest** on the finance leases, 26% of total undiscounted payments. Note that this table covers **only the commenced leases**; the $329.1bn of not-yet-commenced leases is not in it.

## 2.7 RECONCILIATION — proving what the contractual obligations table contains

The MD&A "Contractual Obligations" table shows "Operating and finance leases, including imputed interest" of **$443,506m** at FY2026. The Note 13 maturity table totals only $24,706 + $89,686 = **$114,392m**.

**$443,506m − $114,392m = $329,114m = the $329.1 billion of not-yet-commenced leases.** Exact.

The same check holds in prior years:
- FY2025: $178,701m − ($25,481 + $60,506) = $92,714m ≈ $92.7bn (verified)
- FY2024: $172,725m − ($21,570 + $34,149) = $117,006m = $8.6bn + $108.4bn (verified)

**So the MD&A contractual-obligations lease line already includes the off-balance-sheet leases.** The correct total lease obligation is **$443.5 billion undiscounted**.

---

# ASSIGNMENT 3 — STAYING POWER [three strengths]

## 3.1 Cash, cash equivalents and short-term investments

| (In millions) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Cash and cash equivalents | 13,931 | 34,704 | 18,315 | 30,242 | **20,935** |
| Short-term investments | 90,826 | 76,558 | 57,228 | 64,323 | **55,908** |
| **Total cash, equivalents and ST investments** | **104,757** | **111,262** | **75,543** | **94,565** | **76,843** |
| Equity and other investments | 6,891 | 9,879 | 14,600 | 15,405 | **36,348** |

> "Cash, cash equivalents, and short-term investments totaled $76.8 billion and $94.6 billion as of June 30, 2026 and 2025, respectively. Equity and other investments were $36.3 billion and $15.4 billion as of June 30, 2026 and 2025, respectively."
> — FY2026 10-K, Item 7

**Liquidity has FALLEN 31% from the FY2023 peak of $111.3bn while total assets went from $412.0bn to $758.4bn.** Cash is being consumed by capex, not accumulated.

### Composition of the portfolio (Note 4, June 30, 2026, recorded basis, $m)

| | Total | Cash & equiv | ST investments | Equity & other |
|---|---|---|---|---|
| Commercial paper | 2,987 | 2,373 | 614 | 0 |
| Certificates of deposit | 1,745 | 1,701 | 44 | 0 |
| **U.S. government securities** | **48,562** | 399 | **40,675** | 7,488 |
| U.S. agency securities | 3,133 | 1,787 | 1,346 | 0 |
| Foreign government bonds | 226 | 0 | 226 | 0 |
| Mortgage- and asset-backed securities | 1,795 | 0 | 1,795 | 0 |
| Corporate notes and bonds (L2) | 10,660 | 0 | 10,660 | 0 |
| Corporate notes and bonds (L3) | 1,738 | 0 | 118 | 1,620 |
| Municipal securities | 238 | 0 | 238 | 0 |
| **Total debt investments** | **71,084** | 6,260 | 55,716 | 9,108 |
| Total equity investments | 27,240 | 0 | 0 | 27,240 |
| Cash | 13,059 | 13,059 | 0 | 0 |
| Derivatives, net | 192 | 0 | 192 | 0 |
| **Total** | **113,191** | **20,935** | **55,908** | **36,348** |

> "Our short-term investments are primarily intended to facilitate liquidity and capital preservation. They consist predominantly of highly liquid investment-grade fixed-income securities, diversified among industries and individual issuers."
> — FY2026 10-K, Item 7

**The portfolio is genuinely liquid:** 73% of debt investments are U.S. government/agency. There is an unrealized loss of **$1,154m on U.S. government securities** ($1,054m of it 12-months-or-greater), which is a rates mark, not a credit issue.

## 3.2 Total debt and the maturity schedule

| (In millions) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Short-term debt (commercial paper) | 0 | 0 | 6,693 | 0 | **0** |
| Current portion of long-term debt | 2,749 | 5,247 | 2,249 | 2,999 | **9,227** |
| Long-term debt | 47,032 | 41,990 | 42,688 | 40,152 | **31,067** |
| **Total bonded debt** | **49,781** | **47,237** | **51,630** | **43,151** | **40,294** |
| Total finance lease liabilities | 14,902 | 17,067 | 27,145 | 46,172 | **66,594** |
| **Debt + finance leases** | **64,683** | **64,304** | **78,775** | **89,323** | **106,888** |

Note 10 detail, FY2026: total face value **$46,136m**, less unamortized discount and issuance costs $(1,081)m, hedge fair value adjustments $(11)m, premium on debt exchange $(4,750)m, giving total debt **$40,294m**.

> "Debt in the table above is comprised of **senior unsecured obligations and ranks equally with our other outstanding obligations**. Interest is paid semi-annually, except for the Euro-denominated debt, which is paid annually. Cash paid for interest on our debt for fiscal years 2026, 2025, and 2024 was $1.5 billion, $1.6 billion, and $1.7 billion, respectively."
> — FY2026 10-K, Note 10

> "As of June 30, 2026 and 2025, the estimated fair value of long-term debt, including the current portion, was $36.5 billion and $40.4 billion, respectively."
> — FY2026 10-K, Note 10

Fair value $36.5bn against $46.1bn face: the legacy low-coupon debt trades at ~79 cents. A $9.6bn unrecognised gain to the borrower.

### DEBT MATURITY SCHEDULE, next five years (FY2026 10-K, Note 10)

| Year Ending June 30 | (In millions) |
|---|---|
| **2027** | **$9,250** |
| **2028** | **$0** |
| **2029** | **$2,001** |
| **2030** | **$0** |
| **2031** | **$500** |
| Thereafter | 34,385 |
| **Total** | **$46,136** |

**Five-year total bond maturities: $11,751 million.** Against $76.8bn of cash and short-term investments and $182.9bn of annual operating cash flow, the bond maturity wall is trivial. **This is the strongest single fact in the staying-power test.**

Bonded debt is **shrinking**: no debt issued in FY2026 or FY2025 (cash-flow line "Proceeds from issuance of debt" = 0, 0, 24,395 for FY2026/FY2025/FY2024), with $3,000m repaid in FY2026.

## 3.3 Commercial paper program

> "**Short-term Debt** As of June 30, 2025, we had **no commercial paper issued or outstanding**. As of June 30, 2024, we had **$6.7 billion of commercial paper issued and outstanding, with a weighted average interest rate of 5.4% and maturities ranging from 28 days to 152 days**. The estimated fair value of this commercial paper approximates its carrying value."
> — FY2025 10-K, Note 10

**The FY2026 10-K has no "Short-term Debt" section at all.** The phrase "short-term debt" appears zero times in the FY2026 10-K, and Note 10 opens directly with long-term debt. **No commercial paper was outstanding at June 30, 2026.**

**NOT FOUND IN FILINGS:** the authorised size of the commercial paper program. No 10-K states a program limit in any year.

## 3.4 Credit facility / revolver / covenants

**NOT FOUND IN FILINGS.** The terms "credit facility", "revolving", "line of credit" and "covenant" each appear **zero times** in the FY2024, FY2025 and FY2026 10-Ks.

**There is no disclosed revolver, no disclosed backstop facility, and no financial covenant of any kind.** For the staying-power test this cuts both ways: there is nothing that can be tripped, but there is also no committed external liquidity line disclosed. Microsoft's stated liquidity plan is:

> "We expect existing cash, cash equivalents, short-term investments, cash flows from operations, and **access to capital markets** to continue to be sufficient to fund our operating activities and cash commitments for investing and financing activities, such as dividends, share repurchases, debt maturities, and material capital expenditures, for at least the next 12 months and thereafter for the foreseeable future."
> — FY2026 10-K, Item 7

That sentence rests partly on **"access to capital markets"**, which is an assumption, not a resource on the balance sheet. The FY2026 risk factors concede the same point: "Our ability to fund these investments depends on our ability to generate sufficient cash flows and obtain financing on acceptable terms."

## 3.5 Interest expense and interest income by year (Note 3)

| (In millions) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| Interest and dividends income | 2,131 | 2,094 | 2,994 | 3,157 | 2,647 | **3,301** |
| Interest expense | (2,346) | (2,063) | (1,968) | (2,935) | (2,385) | **(3,051)** |
| **Net** | (215) | 31 | 1,026 | 222 | 262 | **250** |

**Composition warning.** Reported FY2026 interest expense of $3,051m is (a) **net of capitalised interest** and (b) **dominated by finance leases**. Finance-lease interest alone was $2,547m, or **83% of reported interest expense**, while cash interest paid on actual debt was only $1.5bn. The MD&A confirms both effects:

> "Interest expense increased primarily due to **higher finance lease interest expense**, offset in part by **higher capitalization of debt interest expense**."
> — FY2026 10-K, Item 7

**NOT FOUND IN FILINGS: the amount of interest capitalised into property and equipment.** No 10-K discloses it. That gap matters: capitalised interest inflates the asset base and understates the income-statement cost of the build.

## 3.6 OTHER PURCHASE COMMITMENTS — the single most important number

### Contractual Obligations table (MD&A, "Material Cash Requirements and Other Obligations")

| (In millions) | FY2022 | FY2023 | FY2024 | FY2025 | **FY2026** |
|---|---|---|---|---|---|
| LT debt principal | 55,511 | 52,866 | 51,221 | 49,206 | **46,136** |
| LT debt interest | 22,607 | 21,125 | 28,659 | 27,036 | **25,553** |
| **Construction commitments** | 8,518 | 13,455 | 35,391 | 32,149 | **34,566** |
| **Operating and finance leases, incl. imputed interest** | 48,654 | 79,840 | 172,725 | 178,701 | **443,506** |
| **Purchase commitments** | 45,654 | 67,818 | 72,022 | 109,953 | **194,060** |
| **TOTAL** | **180,944** | **235,104** | **360,018** | **397,045** | **743,821** |

### FY2026 timing breakdown, verbatim

> "The following table summarizes the payments due by fiscal year for our outstanding contractual obligations as of June 30, 2026: (In millions) **2027 / Thereafter / Total** — Long-term debt: Principal payments $9,250 / $36,886 / $46,136; Interest payments 1,405 / 24,148 / 25,553; **Construction commitments 29,848 / 4,718 / 34,566**; **Operating and finance leases, including imputed interest 32,411 / 411,095 / 443,506**; **Purchase commitments 169,008 / 25,052 / 194,060**; **Total $241,922 / $501,899 / $743,821**"
> — FY2026 10-K, Item 7

> "(d) **Purchase commitments primarily relate to datacenters and include open purchase orders and take-or-pay contracts that are not presented as construction commitments above.**"
> — FY2026 10-K, Item 7, footnote (d)

Prior-year timing:
- **FY2025:** purchase commitments **$103,940m due in FY2026**, $6,013m thereafter (total $109,953m); construction commitments $26,859m / $5,290m (total $32,149m). Total due within 12 months: **$148,106m**.
- **FY2024:** purchase commitments **$68,280m due in FY2025**, $3,742m thereafter (total $72,022m); construction commitments $29,892m / $5,499m (total $35,391m). Total due within 12 months: **$114,290m**.

### Construction commitments, verbatim from Note 6/7

> "As of June 30, 2026, we have committed **$34.6 billion** for the construction of new buildings, building improvements, and leasehold improvements, primarily related to datacenters." — FY2026 Note 6
> "As of June 30, 2025, we have committed **$32.1 billion**…" — FY2025 Note 6
> "As of June 30, 2024, we have committed **$35.4 billion**…" — FY2024 Note 7
> "As of June 30, 2023, we have committed **$13.5 billion**…" — FY2023 Note 7

### The near-term cash requirement test

**$241,922 million is contractually due within fiscal year 2027**, of which **$169,008m is purchase commitments** ("primarily relate to datacenters… open purchase orders and take-or-pay contracts").

Against that: cash + short-term investments **$76,843m**, plus FY2026 operating cash flow **$182,935m** = $259.8bn of resources against $241.9bn of one-year obligations, **before** dividends ($27.0bn declared in FY2026) and **before** buybacks ($16.7bn in FY2026).

$241.9bn (due FY2027) − $182.9bn (FY2026 OCF) = **$59.0bn** to be met from the $76.8bn liquidity stack, leaving roughly $17.8bn against $43.7bn of dividends and buybacks. The arithmetic does not break, but **the "no significant near-term cash requirements" characterisation does not survive contact with this table.** The one-year commitment total has run $59.4bn → $89.6bn → $114.3bn → $148.1bn → **$241.9bn** in five years, a 4.1x increase, while liquidity fell 31%.

Scale: **$743.8bn total obligations is 2.24x FY2026 revenue and 98% of total assets ($758.4bn).** In FY2022 the same total was 0.91x revenue.

## 3.7 Unearned / deferred revenue — covenant-free customer funding

| (In millions) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Short-term unearned revenue | 45,538 | 50,901 | 57,582 | 64,555 | **72,965** |
| Long-term unearned revenue | 2,870 | 2,912 | 2,602 | 2,710 | **2,747** |
| **Total unearned revenue** | **48,408** | **53,813** | **60,184** | **67,265** | **75,712** |

Note 12, FY2026, by segment: Productivity and Business Processes $57,936m; Intelligent Cloud $14,942m; More Personal Computing $2,834m.

> "Balance, beginning of period $67,265; Deferral of revenue 194,184; Recognition of unearned revenue (185,737); Balance, end of period $75,712"
> — FY2026 10-K, Note 12

Cash-flow contribution: unearned revenue added **+$9,361m** to operating cash flow in FY2026 (+$5,438m FY2025, +$5,348m FY2024).

**And the backlog behind it:**
> "**Revenue allocated to remaining performance obligations**, which includes unearned revenue and amounts expected to be invoiced and recognized as revenue in future periods, was **$684 billion** as of June 30, 2026. Revenue allocated to remaining performance obligations related to the commercial portion of revenue was **$678 billion** as of June 30, 2026, with a **weighted average duration of approximately 2.3 years**. We expect to recognize approximately **30%** of both our total company remaining performance obligation revenue and commercial remaining performance obligation revenue over the next 12 months and the remainder thereafter."
> — FY2026 10-K, Note 12

**$684bn of contracted future revenue against $743.8bn of contractual obligations.** These are the two numbers to hold against each other. About 30% of RPO (~$205bn) converts within 12 months, against $241.9bn of obligations due in the same window.

## 3.8 Accounts payable and working capital

| (In millions) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Accounts payable | 19,000 | 18,095 | 21,996 | 27,724 | **42,416** |
| Accounts receivable, net | 44,261 | 48,688 | 56,924 | 69,905 | **80,876** |
| Total current assets | 169,684 | 184,257 | 159,734 | 191,131 | **207,710** |
| Total current liabilities | 95,082 | 104,149 | 125,286 | 141,218 | **168,825** |
| **Working capital** | **74,602** | **80,108** | **34,448** | **49,913** | **38,885** |
| **Current ratio** | 1.78 | 1.77 | 1.28 | 1.35 | **1.23** |

**Working capital has halved since FY2023 and the current ratio is at a six-year low of 1.23.**

### The accounts-payable finding — accrued capex

> "As of June 30, 2026, 2025, and 2024, **purchases of property and equipment remaining in accounts payable were $26.7 billion, $6.9 billion, and $4.3 billion**, respectively."
> — FY2026 10-K, Note 6

(FY2023: **$3.8 billion**, per FY2025 Note 6.)

**$26.7 billion of the $42.4 billion accounts payable balance is unpaid capex — 63% of AP.** AP rose $14.7bn in FY2026 while accrued capex inside it rose $19.8bn, meaning **trade payables excluding capex actually fell**. The AP increase contributed **+$5,268m to operating cash flow** in FY2026 while representing equipment already received and not yet paid for. This is capex financed by the supply chain, sitting inside operating cash flow.

**Adjusted:** cash capex $115,948m + accrued-capex increase ~$19,800m = **~$135.7bn of capex incurred** in FY2026 versus $115.9bn reported as cash outflow.

---

# ASSIGNMENT 4 — THE CAPEX COMPOSITION

## 4.1 "Additions to property and equipment" (the capex line)

| (In millions) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|
| **Additions to property and equipment** | **20,622** | **23,886** | **28,107** | **44,477** | **64,551** | **115,948** |
| Net cash from operations | 76,740 | 89,035 | 87,582 | 118,548 | 136,162 | **182,935** |
| Capex as % of OCF | 27% | 27% | 32% | 38% | 47% | **63%** |
| Net cash used in investing | (27,577) | (30,311) | (22,680) | (96,970) | (72,599) | **(139,500)** |

## 4.2 The TRUE capital formation, adding the items outside the capex line

| (In millions) | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Additions to property and equipment (cash) | 44,477 | 64,551 | **115,948** |
| **+ Finance lease ROU assets obtained** | 11,633 | 20,511 | **24,608** |
| **+ Operating lease ROU assets obtained** | 6,703 | 7,826 | 4,555 |
| **+ Increase in capex accrued in accounts payable** | ~500 | ~2,600 | **~19,800** |
| **≈ Total capital formation** | **~63,300** | **~95,500** | **~164,900** |
| Reported capex as % of true total | 70% | 68% | **70%** |

**The capex line understates FY2026 capital formation by roughly $49 billion, or 30%.** For the owner-earnings calculation this is the load-bearing adjustment: finance-lease ROU additions are capital spending funded by a 13-year, 4.5% obligation, and they appear nowhere in investing cash flow. Label the accrued-capex row **CONVENTION — derived from the two disclosed year-end accrual figures.**

## 4.3 Does MD&A break capex into categories?

**NO. NOT FOUND IN FILINGS.**

The only forward-looking capex language in any of the six 10-Ks is the boilerplate in "Other Planned Uses of Capital":

> "We will continue to invest in sales, marketing, product support infrastructure, and existing and advanced areas of technology, as well as acquisitions that align with our business strategy. **Additions to property and equipment will continue, including new facilities, datacenters, and computer systems for research and development, sales and marketing, support, and administrative staff. We will continue to invest in capital expenditures to support growth in our cloud offerings and our investments in AI training and other infrastructure.**"
> — FY2026 10-K, Item 7

Compare FY2024 and FY2025: "We **expect** capital expenditures to **increase** in coming years to support growth in our cloud offerings and our investments in AI infrastructure and training." **FY2026 dropped both "expect" and "increase"**, replacing them with "We will continue to invest in capital expenditures". That is the only change in forward capex language across the six years, and it points toward moderation, not acceleration.

### Specifically, on the long-lived / short-lived split

**NOT FOUND IN FILINGS.** The phrase "short-lived" appears **zero times** in the FY2025 and FY2026 10-Ks. "Long-lived" appears once, in an unrelated impairment-policy context. "Shell" appears once, in the cover-page "shell company" checkbox. **No 10-K in FY2021-FY2026 discloses any split of capital expenditure between land/buildings/shell and servers/GPUs/network equipment.** Management has described such a split in public remarks; **it is not in a filing**, and under a filings-only standard it does not exist.

### What the filing DOES give — balance-sheet composition (Note 6, not a capex split)

| (In millions) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Land | 4,734 | 5,683 | 8,163 | 9,338 | **10,546** |
| Buildings and improvements | 55,014 | 68,465 | 93,943 | 137,921 | **182,749** |
| Leasehold improvements | 7,819 | 8,537 | 9,594 | 12,117 | **16,348** |
| Computer equipment and software / **Servers, network equipment, and software** | 60,631 | 74,961 | 93,780 | 132,836 | **215,874** |
| Furniture and equipment | 5,860 | 6,246 | 6,532 | 6,407 | **6,250** |
| **Total, at cost** | **134,058** | **163,892** | **212,012** | **298,619** | **431,767** |
| Accumulated depreciation | (59,660) | (68,251) | (76,421) | (93,653) | **(118,691)** |
| **Total, net** | **74,398** | **95,641** | **135,591** | **204,966** | **313,076** |
| Depreciation expense | 12.6bn | 11.0bn | 15.2bn | 22.0bn | **34.3bn** |

**FY2026 renamed the line "Computer equipment and software" to "Servers, network equipment, and software"** — the first time servers are named on the face of the footnote.

Derived gross additions at cost (year-on-year change in total at cost), the closest the filing comes to a capex split:

| (In millions) | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Land | +2,480 | +1,175 | **+1,208** |
| Buildings and improvements | +25,478 | +43,978 | **+44,828** |
| Leasehold improvements | +1,057 | +2,523 | **+4,231** |
| **Servers, network equipment, and software** | **+18,819** | **+39,056** | **+83,038** |
| Furniture and equipment | +306 | (125) | (157) |
| **Total change at cost** | **+48,140** | **+86,607** | **+133,148** |

**Servers and network equipment were 62% of FY2026 gross PP&E additions, up from 39% in FY2024.** The mix has shifted decisively toward the short-lived asset. This is a derivation from two balance-sheet dates, not a disclosed split, and it is contaminated by finance-lease ROU assets (which sit inside PP&E) and by disposals. Label it: **CONVENTION — derived, not disclosed.**

## 4.4 Useful lives, and the FY2023 extension

> "The estimated useful lives of our property and equipment are generally as follows: **software developed or acquired for internal use, three years; servers and network equipment, two to six years**; buildings and improvements, five to 15 years; leasehold improvements, three to 15 years; and furniture and equipment, one to 10 years. Land is not depreciated."
> — FY2026 10-K, Note 1

The series:
- **FY2022:** "computer equipment, **two to four years**"; leasehold improvements three to **20** years
- **FY2023:** "computer equipment, **two to six years**"; leasehold improvements three to 20 years
- **FY2024:** unchanged from FY2023
- **FY2025:** leasehold improvements shortened to three to **15** years
- **FY2026:** "computer equipment" renamed "**servers and network equipment**", two to six years

> "Depreciation expense **declined** in fiscal year 2023 due to the change in estimated useful lives of our server and network equipment."
> — FY2023 10-K, Note 7

**The server life was extended from four years to six in FY2023**, which reduced FY2023 depreciation (from $12.6bn to $11.0bn on a rising asset base). The filing discloses the change and its direction but **not the dollar benefit**. It has not been extended again through FY2026. Note the mismatch: **$215.9bn of servers and network equipment at cost is depreciated over up to six years, while the finance leases funding much of the infrastructure run 13 years.**

## 4.5 Any statement about expected FUTURE capex

The only forward statements in any filing:
1. **FY2022:** "We **expect capital expenditures to increase** in coming years to support growth in our cloud offerings."
2. **FY2024 and FY2025:** "We **expect capital expenditures to increase** in coming years to support growth in our cloud offerings and our investments in AI infrastructure and training."
3. **FY2026:** "We **will continue to invest in capital expenditures** to support growth in our cloud offerings and our investments in AI training and other infrastructure."

**No dollar amount, no range, no percentage, and no time horizon for future capex is given in any 10-K FY2021-FY2026.** The quantified forward commitment lives entirely in the contractual-obligations table ($241.9bn due FY2027) and the not-yet-commenced lease disclosure ($329.1bn, FY2027-FY2033), not in any capex guidance.

## 4.6 The FY2026 risk factor that quantifies nothing but says the most

> "We have made and are continuing to make significant capital and operational investments to develop, train, deploy, and support AI models and related cloud-based services, including building and expanding datacenters, acquiring necessary components, and securing energy resources. **These investments are being made at significant scale and on an accelerated timeline, require substantial and increasing capital expenditures and continued access to capital, and are in advance of fully developed revenue streams. The associated revenue may not be realized in the expected timeframes or at expected levels.** … **Our ability to fund these investments depends on our ability to generate sufficient cash flows and obtain financing on acceptable terms.** Adverse changes in interest rates, credit markets, investor sentiment, our credit ratings, or other factors affecting capital availability could increase our cost of capital or limit our ability to execute our infrastructure strategy."
> — FY2026 10-K, Item 1A (**new** risk factor; no equivalent in FY2025)

This is management's own written statement that the spending runs ahead of the revenue and depends on continued capital access.

## 4.7 Property and equipment, net, and total assets

| (In millions) | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Property and equipment, net | 74,398 | 95,641 | 135,591 | 204,966 | **313,076** |
| Operating lease ROU assets | 13,148 | 14,346 | 18,961 | 24,823 | **24,177** |
| **Total assets** | **364,840** | **411,976** | **512,163** | **619,003** | **758,376** |
| PP&E net as % of total assets | 20% | 23% | 26% | 33% | **41%** |
| Total stockholders' equity | 166,542 | 206,223 | 268,477 | 343,479 | **442,387** |
| Total revenue | 198,270 | 211,915 | 245,122 | 281,724 | **331,839** |

PP&E, net **includes** finance-lease ROU assets of $67,281m at FY2026 (Note 13). Owned PP&E net is therefore ~$245.8bn; leased is ~$67.3bn, or **21% of net PP&E**.

**Microsoft has been converted from a software company into a fixed-asset company in four years.** PP&E net has roughly quadrupled since FY2022 and now represents 41% of total assets. Depreciation of $34.3bn in FY2026 is 10.3% of revenue, up from 5.2% in FY2023.

---

# WHAT THE FILINGS DO NOT DISCLOSE — consolidated list

1. **Carrying value of the OpenAI investment** (any year). Only an all-investee equity-method aggregate.
2. **Split of the $24.1bn OpenAI revenue** between Azure compute sales and revenue-share receipts; no prior-year comparative; no segment attribution.
3. **Terms of the October 2025 / April 2026 OpenAI agreements**; what replaced Azure exclusivity and the right of first refusal (both deleted from the FY2026 filing without comment).
4. **Summarised financial information for OpenAI** as an equity-method investee.
5. **Ownership percentage before the October 2025 recapitalization.** No 10-K or 10-Q before Q2 FY2026 states any percentage. (The 10-Qs do supply the post-recapitalization path: 27% at Dec 2025 and Mar 2026, 25% at Jun 2026 — see Addendum.) The dilution gain is still never isolated from the rest of the line in the 10-K; the Q2 FY2026 10-Q's $10.0bn quarterly figure is the closest the filings come.
6. **Operating/finance split of the $329.1bn not-yet-commenced leases** (discontinued after FY2024) and the amount subject to "certain contractual conditions".
7. **Interest capitalised into property and equipment** (any year).
8. **Any capex split between long-lived and short-lived assets.** Not in any filing.
9. **Any dollar guidance for future capex.** Not in any filing.
10. **Dollar benefit of the FY2023 server useful-life extension.**
11. **Commercial paper program authorised size.**
12. **Any credit facility, revolver, or financial covenant.** None exists in the filings.
13. **Any customer-concentration disclosure.** The word "concentration" appears zero times in FY2025 and FY2026.

---

# ADDENDUM — THE FY2026 10-Qs, WHICH BREAK THE OPENAI GAIN APART

The three FY2026 10-Qs disclose the OpenAI P&L quarterly. The 10-K gives only the annual total. **The quarterly series changes the interpretation completely.**

| Filing | Accession | Period | OpenAI net gain (loss) in other income (expense), net |
|---|---|---|---|
| 10-Q Q1 FY2026 | 0001193125-25-256321 | 3 mo to 2025-09-30 | **−$4.1 billion** |
| 10-Q Q2 FY2026 | 0001193125-26-027207 | 3 mo to 2025-12-31 | **+$10.0 billion** |
| 10-Q Q2 FY2026 | 0001193125-26-027207 | 6 mo to 2025-12-31 | **+$5.9 billion** |
| 10-K FY2026 | 0001193125-26-323660 | 12 mo to 2026-06-30 | **+$6.5 billion** |
| **Derived: H2 FY2026 (Jan-Jun 2026)** | | 6 mo to 2026-06-30 | **+$0.6 billion** |

Verbatim:

> "For the three months ended September 30, 2025 and 2024, other income (expense), net included **$4.1 billion** and $688 million, respectively, **of net losses from investments in OpenAI**, primarily net recognized losses on our equity method investment reflected in other, net."
> — 10-Q for the quarter ended 2025-09-30, Note 3

> "Other income (expense), net included **$10.0 billion and $5.9 billion of net gains for the three and six months ended December 31, 2025**, respectively, and $1.2 billion and $1.9 billion of net losses for the three and six months ended December 31, 2024, respectively, from investments in OpenAI, primarily net recognized gains (losses) on our equity method investment reflected in Other, net. **The net gains recorded for the three and six months ended December 31, 2025 primarily relate to the dilution gain from the OpenAI Recapitalization.**"
> — 10-Q for the quarter ended 2025-12-31, Note 3

**What this proves.** The entire FY2026 gain of $6.5bn is a **single-quarter, non-cash dilution gain of about $10.0 billion** booked in the December 2025 quarter, against roughly **$3.5 billion of ongoing equity-method losses** in the other three quarters ($4.1bn loss in Q1, and +$0.6bn net across H2 which itself nets a further modest loss against any residual dilution effects).

The 10-K's annual presentation of "+$6.5 billion of net gains" conceals this. **The recurring economics of the OpenAI stake remained loss-making throughout FY2026.** Microsoft's own non-GAAP measure strips the whole line out, which is the correct treatment.

## The ownership percentage fell again in the fourth quarter

| Date | Ownership disclosed | Source |
|---|---|---|
| 2025-09-30 | **not disclosed** | 10-Q Q1 FY2026, Note 1 |
| 2025-12-31 | **"approximately 27 percent … on an as-converted basis"** | 10-Q Q2 FY2026, Note 1 |
| 2026-03-31 | **"approximately 27 percent … on an as-converted basis"** | 10-Q Q3 FY2026, Note 1 |
| 2026-06-30 | **"approximate 25% interest on an as-converted basis"** | 10-K FY2026, Note 1 |

**Ownership fell from 27% to 25% during the June 2026 quarter**, after the recapitalization, and no filing explains why or discloses any accompanying gain or loss. The FY2026 10-K attributes the dilution to "the OpenAI Recapitalization **and other funding activity**" without quantifying the second.

**The pre-recapitalization ownership percentage is still NOT FOUND IN FILINGS.** The Q1 FY2026 10-Q (as of 2025-09-30, before the October 2025 recapitalization) states the equity method and the funding commitment but gives **no percentage at all**. No 10-K or 10-Q before Q2 FY2026 ever states a Microsoft ownership percentage in OpenAI.

## The funding progression, quarter by quarter

> "We have made total funding commitments of $13 billion, of which **$11.6 billion** has been funded as of September 30, 2025." — 10-Q Q1 FY2026
> "…of which **$11.7 billion** has been funded as of December 31, 2025." — 10-Q Q2 FY2026
> "…of which **$11.8 billion** has been funded as of March 31, 2026." — 10-Q Q3 FY2026
> "…of which **$11.9 billion** has been funded as of June 30, 2026." — 10-K FY2026

About $100 million per quarter. **The $13bn commitment is effectively complete**; $1.1bn remains. No filing discloses any *new* funding commitment to OpenAI arising from the October 2025 definitive agreement or the April 2026 extension.

## An accounting-description change coincident with the recapitalization

Q1 FY2026 (before):
> "The investment is accounted for under the equity method of accounting, **with our share of OpenAI's income or loss recognized in other income (expense), net**."

Q2 FY2026 onward (after):
> "**We calculate our equity method income or loss using the hypothetical liquidation at book value ("HLBV") method because our liquidation rights and priorities differ from our underlying ownership interest.**"

The HLBV disclosure **first appears in the Q2 FY2026 10-Q**. It is not in any earlier 10-Q or 10-K. Whether this is a change in method or the first disclosure of a method already in use is **not stated in any filing**.
