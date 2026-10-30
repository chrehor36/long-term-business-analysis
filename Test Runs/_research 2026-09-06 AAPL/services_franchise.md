# AAPL — SERVICES: THE FRANCHISE INSIDE THE FRANCHISE
Research file for the AAPL v4.1 run. Compiled 2026-09-06. CIK 0000320193.

**Primary documents (all read as filed HTML from SEC EDGAR Archives, 2026-09-06)**

| Doc | Accession | Primary file | Covers |
|---|---|---|---|
| FY2025 10-K (filed 2025-10-31) | 0000320193-25-000079 | `aapl-20250927.htm` | FY2025/24/23 |
| FY2023 10-K (filed 2023-11-03) | 0000320193-23-000106 | `aapl-20230930.htm` | FY2023/22/21 |
| FY2020 10-K (filed 2020-10-30) | 0000320193-20-000096 | `aapl-20200926.htm` | FY2020/19/18 |
| Q3 FY2026 10-Q (qtr ended 2026-06-27) | 0000320193-26-000020 | `aapl-20260627.htm` | Q3 FY2026 |

Cross-check per operator rule 4: FY2025 total gross margin of **$195,201M** was verified in two
independent places in the filed document — the MD&A gross-margin table and the Consolidated
Statements of Operations (`Total cost of sales 220,960` → `Gross margin 195,201`). They agree.

> **DATA-HYGIENE INCIDENT (recorded, per operator rule 6).** During this run a scratch file named
> `k20.txt` in a shared temp directory proved to contain **General Motors'** 10-K (`gm-20201231`),
> left over from the 2026-09-01 GM run, and a concurrently-running sub-agent overwrote a shared
> parsing script mid-task. Both were caught before any number was transcribed, by sentinel-checking
> that each stripped file contained "Apple Inc". **No GM figure entered this file.** All Apple work
> was then redone in an isolated directory. Flagging because a filename collision of this kind is
> exactly how a wrong number enters a run silently.

---

## 1. THE TABLE THE RUN NEEDS — PRODUCTS vs SERVICES, FY2018-FY2025

All figures **$ millions**, transcribed verbatim from the MD&A "Gross Margin" tables and the
revenue/cost-of-sales disaggregation in the three 10-Ks above.

### 1.1 Net sales

| FY | Products | Services | **Total net sales** | Services % of sales |
|---|---|---|---|---|
| 2018 | 225,847 | **39,748** | 265,595 | 15.0% |
| 2019 | 213,883 | **46,291** | 260,174 | 17.8% |
| 2020 | 220,747 | **53,768** | 274,515 | 19.6% |
| 2021 | 297,392 | **68,425** | 365,817 | 18.7% |
| 2022 | 316,199 | **78,129** | 394,328 | 19.8% |
| 2023 | 298,085 | **85,200** | 383,285 | 22.2% |
| 2024 | 294,866 | **96,169** | 391,035 | 24.6% |
| 2025 | 307,003 | **109,158** | 416,161 | **26.2%** |

*All Products and Services net sales figures above are **VERBATIM from the Consolidated Statements of
Operations** in the three 10-Ks (FY2025 10-K for 2025/24/23; FY2023 10-K for 2023/22/21; FY2020 10-K
for 2020/19/18). Nothing in this table is derived. The FY2023 overlap between the FY2025 and FY2023
10-Ks agrees exactly ($298,085M Products / $85,200M Services), which cross-checks the transcription.*

### 1.2 Cost of sales

| FY | Products COGS | Services COGS |
|---|---|---|
| 2018 | 148,164 | 15,592 |
| 2019 | 144,996 | 16,786 |
| 2020 | 151,286 | 18,273 |
| 2021 | 192,266 | 20,715 |
| 2022 | 201,471 | 22,075 |
| 2023 | 189,282 | 24,855 |
| 2024 | 185,233 | 25,119 |
| 2025 | 194,116 | 26,844 |

*All cost-of-sales figures above are **VERBATIM from the Consolidated Statements of Operations**, not
derived. Verified: Products COGS + Services COGS = Total cost of sales in every year (e.g. FY2025:
194,116 + 26,844 = 220,960 ✓), and net sales less cost of sales reproduces the MD&A gross margin
table exactly (e.g. FY2025 Services: 109,158 - 26,844 = 82,314 ✓). This is the operator-rule-4
cross-check: the MD&A table and the audited statements agree in all eight years.*

### 1.3 GROSS MARGIN — dollars and percent (all VERBATIM from MD&A)

| FY | Products GM $ | Services GM $ | **Total GM $** | Products GM % | Services GM % | Total GM % | **SERVICES % OF TOTAL GROSS PROFIT** |
|---|---|---|---|---|---|---|---|
| 2018 | 77,683 | 24,156 | 101,839 | 34.4% | 60.8% | 38.3% | **23.7%** |
| 2019 | 68,887 | 29,505 | 98,392 | 32.2% | 63.7% | 37.8% | **30.0%** |
| 2020 | 69,461 | 35,495 | 104,956 | 31.5% | 66.0% | 38.2% | **33.8%** |
| 2021 | 105,126 | 47,710 | 152,836 | 35.3% | 69.7% | 41.8% | **31.2%** |
| 2022 | 114,728 | 56,054 | 170,782 | 36.3% | 71.7% | 43.3% | **32.8%** |
| 2023 | 108,803 | 60,345 | 169,148 | 36.5% | 70.8% | 44.1% | **35.7%** |
| 2024 | 109,633 | 71,050 | 180,683 | 37.2% | 73.9% | 46.2% | **39.3%** |
| 2025 | 112,887 | 82,314 | 195,201 | 36.8% | **75.4%** | 46.9% | **42.2%** |

**The finding in one line: Services is 26% of Apple's revenue and 42% of its gross profit, and the
share has risen every year but one since FY2018.** Products gross margin has been essentially flat
in the mid-30s for eight years (34.4% → 36.8%); every point of consolidated margin expansion from
38.3% to 46.9% is mix-shift into Services.

Apple's own MD&A attributes the FY2025 Services increase, VERBATIM:

> "Services net sales increased during 2025 compared to 2024 primarily due to higher net sales from
> advertising, the App Store and cloud services."

Note the ordering: **advertising is named first**, and advertising is where the Google licensing
revenue sits (see §2).

---

## 2. THE COMPOSITION SWEEP — APPLE DISCLOSES **NO** SUB-LINE DOLLARS

**Recorded sweep. Searched the FY2025 10-K and Q3 FY2026 10-Q for a dollar figure attached to any
Services sub-line. Result: ZERO. Apple discloses Services as a single number.**

What Apple gives is a *narrative* description in Item 1, with **five named sub-categories and not
one dollar attached to any of them**. VERBATIM, in full:

> **"Advertising**
> The Company's advertising services include third-party licensing arrangements and the Company's
> own advertising platforms.
> **AppleCare**
> The Company offers a portfolio of fee-based service and support products under the AppleCare®
> brand. ...
> **Cloud Services**
> The Company's cloud services store and keep customers' content up-to-date and available across
> multiple Apple devices and Windows personal computers.
> **Digital Content**
> The Company operates various platforms, including the App Store®, that allow customers to
> discover and download applications and digital content, such as books, music, video, games and
> podcasts. ...
> **Payment Services**
> The Company offers payment services, including Apple Card®, a co-branded credit card, and Apple
> Pay®, a cashless payment service."

**The load-bearing sentence for this run is the first one.** Apple places "third-party licensing
arrangements" — the Google search-default payment — inside **Advertising**, which is inside
**Services**. It is disclosed only as a category descriptor. There is no dollar amount, no
percentage, and no separate line anywhere in the financial statements.

| Sub-line | Named by Apple? | Dollar size disclosed? |
|---|---|---|
| Advertising (incl. third-party licensing / Google) | Yes | **NO** |
| AppleCare | Yes | **NO** |
| Cloud Services | Yes | **NO** |
| Digital Content (incl. App Store) | Yes | **NO** |
| Payment Services | Yes | **NO** |

**Consequence for the framework:** the run **cannot** compute what share of Services gross profit
is Google money, or App Store money, from filed data. The disclosure does not exist. This is an
**UNKNOWABLE** as to composition, from filings alone.

The only quantified sub-disclosure Apple makes about Services is a footnote on the revenue line,
VERBATIM:

> "(1)Services net sales include amortization of the deferred value of services bundled in the sales
> price of certain products."

---

## 3. CUSTOMER / REVENUE CONCENTRATION — WHAT IS AND IS NOT DISCLOSED

**Apple names NO customer at >10% of revenue. There is no revenue-concentration disclosure at all.**

The only concentration disclosures are **receivables** (credit risk), VERBATIM from Note 3:

> "As of September 27, 2025, the Company had one customer that represented 10% or more of total
> trade receivables, which accounted for 12%. The Company's third-party cellular network carriers
> accounted for 34% and 38% of total trade receivables as of September 27, 2025 and September 28,
> 2024, respectively. The Company requires third-party credit support or collateral from certain
> customers to limit credit risk."

> "As of September 27, 2025, the Company had two vendors that individually represented 10% or more
> of total vendor non-trade receivables, which accounted for 46% and 23%. As of September 28, 2024,
> the Company had two vendors that individually represented 10% or more of total vendor non-trade
> receivables, which accounted for 44% and 23%."

**Do not read the "one customer at 12%" as Google.** It is a *trade* receivable, i.e. product
distribution, and Apple's own framing ties the category to cellular carriers and resellers. The
Google payment is not identifiable in any concentration table.

Also relevant, VERBATIM from Item 1 (channel mix):

> "During 2025, the Company's net sales through its direct and indirect distribution channels
> accounted for 40% and 60%, respectively, of total net sales."

And the single-product-category concentration Apple *does* concede, VERBATIM from Item 1A:

> "Further, the Company generates a significant portion of its net sales from a single product
> category and a decline in demand for that product could significantly impact net sales and gross
> margins."

(iPhone was **$209,586M of $416,161M = 50.4%** of FY2025 net sales.)

---

## 4. GEOGRAPHIC SEGMENTS FY2023-FY2025 (VERBATIM, Note 13, $ millions)

| Segment | FY2025 net sales | FY2024 | FY2023 | FY2025 op. income | FY2024 | FY2023 |
|---|---|---|---|---|---|---|
| Americas | 178,353 | 167,045 | 162,560 | 72,480 | 67,656 | 60,508 |
| Europe | 111,032 | 101,328 | 94,294 | 47,739 | 41,790 | 36,098 |
| Greater China | 64,377 | 66,952 | 72,559 | 26,917 | 27,082 | 30,328 |
| Japan | 28,703 | 25,052 | 24,257 | 13,955 | 12,454 | 11,888 |
| Rest of Asia Pacific | 33,696 | 30,658 | 29,615 | 14,586 | 13,062 | 12,066 |
| Corporate | — | — | — | (42,627) | (38,828) | (36,587) |
| **Total** | **416,161** | **391,035** | **383,285** | **133,050** | **123,216** | **114,301** |

Country detail (10%-or-more countries), VERBATIM:

| | FY2025 | FY2024 | FY2023 |
|---|---|---|---|
| U.S. net sales | 151,790 | 142,196 | 138,573 |
| China net sales *(incl. Hong Kong and Taiwan)* | 64,377 | 66,952 | 72,559 |
| Other countries | 199,994 | 181,887 | 172,153 |

Long-lived assets: U.S. $40,274M vs China $3,617M (FY2025). **Greater China is the only segment
shrinking** — down 11.3% from FY2023 to FY2025.

Note Apple's segment definition caveat, VERBATIM: *"Europe includes European countries, as well as
India, the Middle East and Africa."* Europe's growth therefore blends the EU (where the DMA bites)
with India (where Apple is growing hardest). The filing does not let the run separate them.

---

## 5. ALPHABET CROSS-CHECK — THE OTHER SIDE IS ALSO SILENT

Alphabet Inc., CIK 0001652044, FY2025 10-K, **accession 0001652044-26-000018**, filed 2026-02-05,
`goog-20251231.htm`. FY2023 figure from the prior 10-K, accession 0001652044-25-000014.

**Total traffic acquisition costs (TAC), $ millions:**

| FY2023 | FY2024 | FY2025 |
|---|---|---|
| 50,886 | 54,900 | **59,926** |

TAC definition, VERBATIM (appears identically in MD&A and Note 1):

> "Cost of revenues is comprised of TAC and other costs of revenues.
> • TAC includes:
> ◦ amounts paid to our distribution partners who make available our search access points and other
> ad-supported services. Our distribution partners include browser providers, mobile carriers,
> original equipment manufacturers, and software developers; and
> ◦ amounts paid to Google Network partners primarily for ads displayed on their properties."

**RECORDED ABSENCE: the word "Apple" appears ZERO times in Alphabet's FY2025 10-K** (0 in stripped
text and 0 in raw HTML; also 0 in the FY2024 10-K). Alphabet quantifies no payment to any single
distribution partner. Hit counts: `Apple` **0**, `distribution partner` 10, `browser` 5, `default` 4,
`search access point` 2, `one distribution partner` **0**, `TAC` 21.

**So neither counterparty discloses the number.** Apple names Google but not the amount; Alphabet
discloses the amount only as a $59.9bn aggregate that also contains every other OEM, carrier and
network partner. The ~$20bn figure is therefore **not derivable from either filing** — it is a
court-record figure. See `google_tac.md` §3 for the rung.

---

## 6. VERDICT INPUTS FOR Q2

1. **Services is 42.2% of gross profit** and is the entire source of margin expansion since FY2018.
   The franchise question is now mostly a Services question.
2. **Apple discloses no Services sub-line dollars.** Composition is **UNKNOWABLE** from filings.
3. The most profitable identifiable plank — the Google licensing arrangement — is **court-supervised
   and unquantified by both parties.**
4. Apple's own Item 1A concedes the arrangement could be prohibited outright on appeal, with a
   "materially adverse" effect.

Against **[E3-03] criterion 3 ("is not subject to price regulation")** the Services segment cannot
be cleared on filed evidence, because the analyst cannot even size the regulated portion. The honest
verdict is not "fails" but **"cannot be established IN"** — and under the four-verdict rule an
UNKNOWABLE closes the file just as an OUT does.
