# CHUBB LIMITED (CB, CIK 0000896159) - GOVERNANCE EVIDENCE, PRIMARY FILINGS ONLY

Gathered 2026-09-19. **Evidence and verbatim quotation only. No verdict is recorded here.**
Line references are to the stripped `.txt` files in this directory, which are grep-able.

## SOURCES FETCHED AND STRIPPED

| file | form | filed | accession | primary / exhibit doc |
|---|---|---|---|---|
| `DEF14A_2026.txt` | DEF 14A | 2026-04-03 | 0001104659-26-039513 | tm2527783-7_def14a.htm |
| `DEF14A_2025.txt` | DEF 14A | 2025-04-01 | 0001104659-25-030554 | tm251658-4_def14a.htm |
| `8K_2026-07-21_body/_EX991/_EX992.txt` | 8-K items 2.02, 9.01 | 2026-07-21 | 0001193125-26-310312 | d78544d8k.htm, d78544dex991.htm, d78544dex992.htm |
| `8K_2026-04-21_body/_EX991/_EX992.txt` | 8-K items 2.02, 9.01 | 2026-04-21 | 0001193125-26-166937 | d145408d8k.htm, d145408dex991.htm, d145408dex992.htm |
| `8K_2026-02-03_body/_EX991/_EX992.txt` | 8-K items 2.02, 9.01 | 2026-02-03 | 0001193125-26-035589 | d812920d8k.htm, d812920dex991.htm, d812920dex992.htm |
| `8K_2025-10-21_body/_EX991/_EX992.txt` | 8-K items 2.02, 9.01 | 2025-10-21 | 0001193125-25-245172 | d65750d8k.htm, d65750dex991.htm, d65750dex992.htm |
| `8K_2026-05-22_annualmtg.txt` | 8-K items 5.02, 5.03, 5.07 | 2026-05-22 | 0001104659-26-065709 | tm2615328d1_8k.htm |
| `8K_2025-05-16_annualmtg.txt` | 8-K items 5.03, 5.07 | 2025-05-16 | 0001104659-25-049835 | tm2515201d1_8k.htm |
| `8K_2025-08-06_801.txt`, `8K_2026-05-20_801.txt`, `8K_2026-06-10_801.txt` | 8-K item 8.01 | 2025-08-06, 2026-05-20, 2026-06-10 | 0001104659-25-074535, 0001104659-26-064150, 0001104659-26-072113 | senior-note offerings; fetched to check for a repurchase authorisation, which is not there |

Each accession directory was listed at `https://www.sec.gov/Archives/edgar/data/896159/<accession-no-dashes>/`
and every `.htm` exhibit was fetched. Each quarterly earnings 8-K carries exactly two exhibits:
EX-99.1 (the press release) and EX-99.2 (the Financial Supplement). The 2025-Q3 8-K
(0001193125-25-245172, filed 2025-10-21) was located from `submissions.json` by item code 2.02.

---

## (a) NON-GAAP AND ADJUSTED MEASURES IN THE EARNINGS RELEASES

### EBITDA: the word does not appear

`grep -ic ebitda` returns **0** for every one of the stripped files fetched: both proxies, all four
quarterly press releases (EX-99.1), all four Financial Supplements (EX-99.2), all four 8-K bodies, and
both annual-meeting 8-Ks. **Neither "EBITDA" nor "Adjusted EBITDA" appears anywhere in any Chubb
document gathered here, in any role.**

### The headline earnings measure

The headline names GAAP net income per share **and** core operating income per share side by side.
Q2 2026, `8K_2026-07-21_EX991.txt` lines 36-42 (the headline itself):

> "Chubb Reports Second Quarter Per Share Net Income of $7.30 and
> Per Share Core Operating Income of $7.26, Up 18.2%; Consolidated
> Net Premiums Written of $14.7 Billion, Up 3.6%, with P&C and Life
> Insurance Up 3.0% and 7.5%; P&C Combined Ratio of 83.8%"

First paragraph, same file, lines 142-145:

> "ZURICH - July 21, 2026 - Chubb Limited (NYSE: CB) today reported net income for the quarter ended
> June 30, 2026 of $2.85 billion, or $7.30 per share, and core operating income of $2.84 billion, or
> $7.26 per share. Book value per share and tangible book value per share increased 12.3% and 17.1%,
> respectively, from June 30, 2025 and now stand at $195.45 and $131.93. For the last three months,
> book value was favorably impacted by after-tax net realized and unrealized gains of $388 million in
> Chubb's investment portfolio, partially offset by $254 million of foreign currency losses. Book value
> per share and tangible book value per share excluding AOCI increased 11.4% and 15.8%, from
> June 30, 2025."

So the **first paragraph puts GAAP net income first**, then core operating income, then tangible book
value per share and TBVPS excluding AOCI. The return measures are a bullet, lines 126-127:

> "Annualized return on equity (ROE) was 15.3%. Annualized core operating return on tangible equity
> (ROTE) was 21.2% and annualized core operating ROE was 14.5%."

The other three release headlines are built the same way:

- FY2025 / Q4, `8K_2026-02-03_EX991.txt` lines 35-47: "Chubb Reports Fourth Quarter Net Income of $3.21 Billion, Up 24.7%, and Core Operating Income of $2.98 Billion, Up 21.7%; Consolidated Net Premiums Written of $13.1 Billion, Up 8.9%, with P&C and Life Insurance Up 7.7% and 16.9%; Record P&C Combined Ratio of 81.2%; / Full-Year Record Net Income of $10.31 Billion, Up 11.2%, and Record Core Operating Income of $9.95 Billion, Up 8.9%; Consolidated Net Premiums Written of $54.8 Billion, Up 6.6%, with P&C and Life Insurance Up 5.4% and 15.1%; Record P&C Combined Ratio of 85.7%"
- Q1 2026, `8K_2026-04-21_EX991.txt` lines 36-46: "Chubb Reports First Quarter Per Share Net Income and Core Operating Income of $5.88 and $6.82, Respectively, Up 78.8% and 85.2%; Consolidated Net Premiums Written of $14.0 Billion, Up 10.7%, with P&C and Life Insurance Up 7.2% and 33.1%; P&C Combined Ratio of 84.0%"
- Q3 2025, `8K_2025-10-21_EX991.txt` lines 38-46: "Chubb Reports Third Quarter Net Income Per Share of $6.99, Up 22.6%, and Record Core Operating Income Per Share of $7.49, Up 30.9%; Consolidated Net Premiums Written of $14.9 Billion, Up 7.5%; Record P&C Combined Ratio of 81.8%"

### The release's own Regulation G definitions, verbatim

All from `8K_2026-07-21_EX991.txt`, the section headed "Regulation G - Non-GAAP Financial Measures"
at line 1990. The same text appears in the Financial Supplement, `8K_2026-07-21_EX992.txt` line 35700ff.

Lines 1992-1994, the preamble:

> "In presenting our results, we included and discussed certain non-GAAP measures. These non-GAAP
> measures, which may be defined differently by other companies, are important for an understanding of
> our overall results of operations and financial condition. However, they should not be viewed as a
> substitute for measures determined in accordance with generally accepted accounting principles (GAAP)."

**Constant dollar**, lines 1995-1998:

> "Throughout this document there are various measures presented on a constant-dollar basis (i.e.,
> excludes the impact of foreign exchange). We believe it is useful to evaluate the trends in our results
> exclusive of the effect of fluctuations in exchange rates between the U.S. dollar and the currencies in
> which our international business is transacted, as these exchange rates could fluctuate significantly
> between periods and distort the analysis of trends. The impact is determined by assuming constant
> foreign exchange rates between periods by translating prior period results using the same local currency
> exchange rates as the comparable current period."

**Adjusted net investment income**, lines 1999-2004:

> "Adjusted net investment income is net investment income excluding the amortization of the fair value
> adjustment on acquired invested assets from certain acquisitions of $1 million and $4 million in Q2 2026
> and Q2 2025, and including investment income of $119 million and $115 million in Q2 2026 and Q2 2025,
> from partially owned investment companies (private equity partnerships) where our ownership interest is
> in excess of 3% that are accounted for under the equity method. The amortization of the fair value
> adjustment on acquired invested assets was $3 million and $6 million for the six months ended
> June 30, 2026 and 2025, and the investment income from private equity partnerships was $246 million and
> $222 million for the six months ended June 30, 2026 and 2025. The mark-to-market movement on these
> private equity partnerships are included in adjusted net realized gains (losses) as described below.
> We believe this measure is meaningful as it highlights the underlying performance of our invested assets
> and portfolio management in support of our lines of business."

**Adjusted net realized gains (losses) and other, net of tax**, lines 2006-2012:

> "Adjusted net realized gains (losses) and other , net of tax , includes net realized gains (losses) and
> net realized gains (losses) recorded in other income (expense) related to unconsolidated subsidiaries,
> and excludes realized gains and losses on crop derivatives and realized gains and losses on underlying
> investments supporting the liabilities of certain participating policies related to the policyholders'
> share of gains and losses. The crop derivatives were purchased to provide economic benefit, in a manner
> similar to reinsurance protection, in the event that a significant decline in commodity pricing impacts
> underwriting results. We view gains and losses on these derivatives as part of the results of our
> underwriting operations, and therefore realized gains (losses) from these derivatives are reclassified
> to adjusted losses and loss expenses. The realized gains and losses on underlying investments supporting
> the liabilities of certain participating policies have been reclassified from net realized gains (losses)
> to adjusted policy benefits. We believe this better reflects the economics of the liabilities and the
> underlying investments supporting those liabilities. Other includes the amortization of fair value
> adjustment of acquired invested assets and long-term debt related to certain acquisitions."

**P&C underwriting income (loss)**, lines 2013-2016:

> "P&C underwriting income (loss ) excludes the Life Insurance segment and is calculated by subtracting
> adjusted losses and loss expenses, adjusted policy benefits, policy acquisition costs and administrative
> expenses from net premiums earned. We use underwriting income (loss) and operating ratios to monitor the
> results of our operations without the impact of certain factors, including net investment income, other
> income (expense), interest expense, amortization expense of purchased intangibles, integration expenses
> and severance, amortization of fair value of acquired invested assets and debt, income tax expense,
> adjusted net realized gains (losses), and market risk benefits gains (losses)."

**P&C current accident year underwriting income excluding catastrophe losses**, lines 2017-2020. This is
the measure that strips both catastrophes and prior period reserve development:

> "P&C current accident year underwriting income excluding catastrophe losses is P&C underwriting income
> adjusted to exclude P&C catastrophe losses and prior period development (PPD). We believe it is useful to
> exclude catastrophe losses, as they are not predictable as to timing and amount, and PPD as these
> unexpected loss developments on historical reserves are not indicative of our current underwriting
> performance. We believe the use of these measures enhances the understanding of our results of operations
> by highlighting the underlying profitability of our insurance business."

And the blanket convention, lines 2034-2035:

> "References in this release to "current accident year" or "underlying" metrics exclude catastrophe losses
> and prior period development, unless stated otherwise."

**Core operating income**, lines 2036-2044:

> "Core operating income relates only to Chubb income, which excludes noncontrolling interests. It excludes
> from Chubb net income the after-tax impact of adjusted net realized gains (losses) and other, which
> include items described in this paragraph, and market risk benefits gains (losses). We believe this
> presentation enhances the understanding of our results of operations by highlighting the underlying
> profitability of our insurance business. We exclude adjusted net realized gains (losses) and market risk
> benefits gains (losses) because the amount of these gains (losses) is heavily influenced by, and
> fluctuates in part according to, the availability of market opportunities. In addition, we exclude the
> amortization of fair value adjustments on purchased invested assets and long-term debt related to certain
> acquisitions due to the size and complexity of these acquisitions. We also exclude integration expenses,
> including legal and professional fees and all other costs directly related to acquisition integration
> activities, as well as severance expenses associated with transformation initiatives to enhance
> operational efficiency. The costs are not related to the ongoing activities of the individual segments
> and are therefore included in Corporate and excluded from our definition of segment income. We believe
> these integration expenses and severance are not indicative of our underlying profitability, and
> excluding these integration expenses and severance facilitates the comparison of our financial results to
> our historical operating results. Additionally, we exclude the amortization of the deferred tax asset
> related to the tax benefit from the Bermuda Economic Transition Adjustment, which we believe provides
> investors with a better view of our operating performance, enhances the understanding of the trends in the
> underlying business, improves comparability between periods and provides increased transparency.
> References to core operating income measures mean net of tax, whether or not noted."

**Core operating ROE and core operating ROTE**, lines 2046-2051:

> "Core operating return on equity (ROE) and Core operating return on tangible equity (ROTE) are annualized
> non-GAAP financial measures. The numerator includes core operating income (loss), net of tax. The
> denominator includes the average Chubb shareholders' equity for the period adjusted to exclude unrealized
> gains (losses) on investments, current discount rate on future policy benefits (FPB), and
> instrument-specific credit risk on market risk benefits (MRB), all net of tax and attributable to Chubb.
> For the ROTE calculation, the denominator is also adjusted to exclude Chubb goodwill and other intangible
> assets, net of tax. These measures enhance the understanding of the return on shareholders' equity by
> highlighting the underlying profitability relative to shareholders' equity and tangible equity excluding
> the effect of these items as these are heavily influenced by changes in market conditions. We believe
> ROTE is meaningful because it measures the performance of our operations without the impact of goodwill
> and other intangible assets."

**P&C combined ratio**, lines 2052-2053:

> "P&C combined ratio is the sum of the loss and loss expense ratio, acquisition cost ratio and the
> administrative expense ratio excluding the life business and including the realized gains and losses on
> the crop derivatives, as noted above."

**P&C current accident year combined ratio excluding catastrophe losses**, lines 2054-2056:

> "P&C current accident year combined ratio excluding catastrophe losses excludes the impact of P&C
> catastrophe losses and PPD from the P&C combined ratio. We believe this measure provides a useful
> evaluation of our underwriting performance and enhances the understanding of the trends in our P&C
> business that may be obscured by these items."

The fuller mechanics of that same ratio are given in the Financial Supplement, and identically in the
proxy at `DEF14A_2026.txt` line 21871:

> "Current accident year (CAY) P&C combined ratio excluding catastrophe losses excludes catastrophe losses
> (Cats) and prior period development (PPD) from the P&C combined ratio. We exclude Cats as they are not
> predictable as to timing and amount and PPD as these unexpected loss developments on historical reserves
> are not indicative of our current underwriting performance. The combined ratio numerator is adjusted to
> exclude Cats, PPD and expense adjustments on PPD, and the denominator is adjusted to exclude net premiums
> earned adjustments on PPD and reinstatement premiums on Cats and PPD. In periods where there are
> adjustments on loss sensitive policies, these adjustments are excluded from PPD and net premiums earned
> when calculating the ratios. We believe this measure provides a better evaluation of our underwriting
> performance and enhances the understanding of the trends in our P&C business that may be obscured by
> these items. This measure is commonly reported among our peer companies and allows for a better
> comparison."

**Global P&C performance metrics**, lines 2057-2061:

> "Global P&C performance metrics comprise consolidated operating results (including corporate) and exclude
> the operating results of Chubb's Life Insurance and North America Agricultural Insurance segments. The
> agriculture insurance business is a different business in that it is a public sector and private sector
> partnership in which insurance rates, premium growth, and risk-sharing is not market-driven like the
> remainder of Chubb's P&C insurance business. We believe that these measures are useful and meaningful to
> investors as they are used by management to assess Chubb's global P&C operations which are the most
> economically similar. We exclude the North America Agricultural Insurance and Life Insurance segments
> because the results of these businesses do not always correlate with the results of our global P&C
> operations."

**Tangible book value per common share**, lines 2062-2077:

> "Tangible book value per common share is Chubb shareholders' equity less Chubb goodwill and other
> intangible assets, net of tax, divided by the shares outstanding. We believe that goodwill and other
> intangible assets are not indicative of our underlying insurance results or trends and make book value
> comparisons to less acquisitive peer companies less meaningful."

**Book value per share and TBVPS excluding AOCI**, lines 2079-2080:

> "Book value per share and tangible book value per share excluding accumulated other comprehensive income
> (loss) (AOCI) , excludes AOCI from the numerator because it eliminates the effect of items that can
> fluctuate significantly from period to period, primarily based on changes in interest rates and foreign
> currency movement, to highlight underlying growth in book and tangible book value."

**Adjusted operating cash flow**, lines 2082-2086:

> "Adjusted operating cash flow is Operating cash flow excluding the operating cash flow related to the net
> investing activities of Huatai's asset management companies as it relates to the Consolidated Investment
> Products as required under consolidation accounting. Because these entities are investment companies, we
> are required to retain the investment company presentation in our consolidated results, which means we
> include the net investing activities of these entities in our operating cash flows. Chubb has elected to
> remove the impact of net investing activities of consolidated investment companies from our operating
> cash flow as they may distort a reader's analysis of our underlying operating cash flow related to the
> core insurance company operations. These net investing activities are more appropriately classified
> outside of operating cash flows, consistent with our consolidated investing activities. Accordingly, we
> believe that it is appropriate to adjust operating cash flow for the impact of consolidated investment
> products."

**Life Insurance net premiums written and deposits collected**, lines 2088-2090:

> "Life Insurance and International life insurance net premiums written and deposits collected includes
> deposits collected on universal life and investment contracts (life deposits). Life deposits are not
> reflected as revenues in our consolidated statements of operations in accordance with U.S. GAAP. However,
> we include life deposits in presenting growth in our life insurance business because life deposits are an
> important component of production and key to our efforts to grow our business."

**Where the reconciliation lives**, lines 2091-2093:

> "See the reconciliation of Non-GAAP Financial Measures on pages 27-33 in the Financial Supplement. These
> measures should not be viewed as a substitute for measures determined in accordance with GAAP, including
> premium, net income, book value, return on equity, and net investment income."

The reconciliation itself is in EX-99.2 (`8K_2026-07-21_EX992.txt`, section "Non-GAAP Financial Measures"
beginning line 35700 and running over six continuation pages, with "Reconciliation Non-GAAP" markers at
lines 35802, 38420, 40231, 42586, 44935, 47284). The net-income-to-core-operating-income bridge is also
printed on the face of the release, in the "Second Quarter Summary" table
(`8K_2026-07-21_EX991.txt` lines 240-425): net income $2,854m / $7.30; adjusted net realized (gains)
losses and other, net of tax $(47)m / $(0.13); integration expenses and severance, net of tax $6m / $0.02;
market risk benefits (gains) losses, net of tax $(4)m / $(0.01); amortization of deferred tax asset from
Bermuda law $33m / $0.08; **core operating income, net of tax $2,842m / $7.26** (lines 396-424).

**Prominence, stated plainly:** every one of the four headlines carries GAAP net income (or net income
per share) first and core operating income second. Tangible book value per share, a non-GAAP measure, is
the measure the CEO twice calls the most important one: "Our most important measure of value creation,
tangible book value per share, increased 17.1% from last year" (`8K_2026-07-21_EX991.txt` lines 935-936)
and "Per-share book and tangible book value, our most important measures of wealth creation, grew 18% and
25.7%, respectively" (`8K_2026-02-03_EX991.txt` lines 914-916).

---

## (b) FORWARD-LOOKING NUMERIC GUIDANCE OR TARGET

There is **no guidance table and no section headed guidance or outlook** in any release. A search of
`8K_2026-07-21_EX991.txt` and `8K_2026-02-03_EX991.txt` for `guidance`, `outlook`, `we expect`,
`we target`, `on track to`, `ambition`, `goal of` returns **nothing**. The forward-looking numerics that
exist are inside the CEO's quoted commentary.

**The one explicit numeric target found, Q3 2025 release**, `8K_2025-10-21_EX991.txt` lines 862-864:

> ""In sum, Chubb's fundamentals and our positioning are excellent, and our balance sheet, starting with
> our loss reserves, has never been stronger. I am confident we will maintain superior earnings growth,
> including double-digit growth in EPS, book and tangible book value, with **core operating ROE increasing
> to 14% plus over the medium term**, CATs and FX notwithstanding.""

**FY2025 release**, `8K_2026-02-03_EX991.txt` lines 921-926:

> ""While commercial insurance market conditions continue to grow incrementally more competitive, we see
> many opportunities for growth given our broad diversification by geography, product, commercial and
> consumer customer segments and distribution channel. In fact, at January 1, conditions were a bit more
> favorable than we had anticipated, and while early, we've had a good start to the year. We anticipate an
> excellent '26 with strong growth in operating earnings and double-digit growth in EPS and tangible book
> value, macro conditions notwithstanding.""

**Q1 2026 release**, `8K_2026-04-21_EX991.txt` lines 535-537:

> ""War in the Middle East raises the specter globally of higher inflation and slower economic growth,
> while adding pressure to certain financial, fiscal and economic conditions already present. Chubb's
> diversification, market-leading presence and capabilities, and operating discipline provide us with
> greater resilience. We have many sources of opportunity, and from what I see I remain confident in our
> ability to continue generating strong growth in operating earnings, and double-digit growth in EPS and
> tangible book value.""

**Q2 2026 release**, `8K_2026-07-21_EX991.txt` lines 962-964:

> ""We are an all-weather company. As long-term compounders of wealth in a cyclical business, we are
> patient and have many sources of opportunity on both the liability and asset sides of the balance sheet.
> CATs and FX aside, we are confident in our ability to continue to outperform and generate strong growth
> in operating earnings and EPS, and double-digit growth in tangible book value.""

Also Q2 2026, a directional claim about the property drag, lines 956-957:

> "and we will not underwrite knowingly at a loss. The growth penalty we are paying in property will
> dissipate going forward. In the meantime, soft market conditions are spreading to certain areas of
> casualty while financial lines also remain soft."

**In the proxies there is no forward numeric target of any kind.** `DEF14A_2026.txt` was searched for
`guidance`, `target of`, `goal of`, `by 2030`, `by 2028`, `aim to achieve`, `we expect to achieve`,
`ambition`, `multi-year`. The only hits are the word "guidance" used about a director's advisory role or
about accounting pronouncements, plus this non-numeric phrase at line 11672:

> "and the ambitious financial goals of the Company, which the Board reviews and approves each year."

The proxy measures against a plan whose numbers it never discloses. Line 10775:

> "On an absolute basis, the Company exceeded prior year performance on three of the five metrics, and
> performance beat plan on all five key metrics."

---

## (c) EXECUTIVE COMPENSATION: THE METRICS PAY VESTS ON

All quotes in this section from `DEF14A_2026.txt` (DEF 14A filed 2026-04-03, accession
0001104659-26-039513) unless stated.

### The CEO and Chairman: combined, with an independent Lead Director

Line 6776:

> "Our Chairman is CEO of our Company. Our Board believes he has both the critical skills and experience
> to best perform both roles at this time. Our Chairman works closely with our independent Lead Director,
> who is appointed by the other independent directors."

Line 5010, repeated verbatim at line 7441:

> "Moreover, the Board is structured to mitigate potential risks in combining the Chairman and CEO roles.
> Our Board has an independent Lead Director with significant and substantive powers and responsibilities,
> as further described below and in "Corporate Governance - Board Leadership Structure" in this proxy
> statement. Mr. Greenberg, in his capacity as CEO, reports to the Board. Led by the Lead Director, the
> independent directors conduct a comprehensive performance evaluation and compensation determination
> process with respect to Mr. Greenberg's performance as CEO. Further, all directors other than
> Mr. Greenberg are independent, and each of the Audit, Compensation, Nominating & Governance and Risk &
> Finance Committees of the Board are comprised entirely of independent directors. Most of our directors
> also have significant executive experience, including some as CEO, and serve individually and
> collectively as an effective independent complement to the Chairman and CEO. Regular Board refreshment
> and well-balanced tenure also ensure new independent voices and perspectives are included in Board
> discussions."

Line 7445:

> "The Board will continue to examine its leadership structure, consider shareholder feedback and will at
> all times conduct itself in the manner it determines to be in the best interests of the Company and its
> shareholders. We expect that the Company will always have either an independent Lead Director or a
> non-executive chairman."

**The independent Lead Director is Michael P. Connors.** Line 5031:

> "While Mr. Greenberg serves as Chairman, Board leadership comes also from our independent Lead Director,
> Mr. Michael P. Connors. Our Board structure provides for a strong independent Lead Director position to
> promote and foster effective director independence in deliberations and overall governance. The Lead
> Director provides a forum for independent director discussion and feedback and helps assure that all
> Board members have the means to, and do, carry out their responsibilities in accordance with their
> fiduciary duties."

Powers, lines 6782 and 6788:

> "Our Lead Director has significant and substantive powers and responsibilities, many of which are
> memorialized in the Company's Organizational Regulations and Corporate Governance Guidelines. Our Lead
> Director ensures an appropriate level of Board independence in deliberations and overall governance, and
> chairs and sets the agenda for executive sessions of the independent directors, which take place at least
> at every regular Board meeting, to discuss certain matters without the Chairman or other management
> present."

> "Our Lead Director also has the ability to convene Board meetings, establishes the regular Board agenda
> (with the Chairman), actively engages in the Board's performance assessment process, and provides input
> on the design of the Board, including composition and committee structure."

Executive Management as defined for the Swiss binding vote, line 6065:

> "Chubb's Executive Management is appointed by the Board, based on the applicable provisions of Swiss law
> and our Organizational Regulations. Chubb's Executive Management currently consists of Evan G. Greenberg,
> Chairman and Chief Executive Officer; Peter C. Enns, Chief Financial Officer; John W. Keogh, President and
> Chief Operating Officer, and Chairman, North America Insurance; and Joseph F. Wayland, General Counsel."

### THE ANNUAL CASH BONUS: NO STATED METRIC WEIGHTS

The bonus is discretionary against three criteria, with no weighting disclosed. Lines 11552-11587:

> "Cash bonus
> Determined in early 2026 based on 2025 performance, as measured against:
> - Company Performance Criteria;
> - Individual Performance Criteria; and
> - the performance of the operating unit(s) or functions directly managed by the NEO.
> Based on performance for each NEO, and targeted to deliver total compensation in a range that typically
> approximates market median to the 75th percentile.
> Ties NEO pay to annual Company and individual performance.
> Allows the Compensation Committee to adjust annual compensation to reflect overall Company financial
> performance during the prior fiscal year and the actual performance of each NEO."

The Company Performance Criteria are five key metrics plus TSR. Line 10773:

> "The Compensation Committee evaluates our absolute and relative financial performance across the five key
> metrics detailed in the table below, as well as TSR."

The five, from "Key Metrics Against Prior Year, Plan and Peers" (headings at lines 10781, 10800, 10817,
10834, 10851, and TSR at 10868). **Four of the five are non-GAAP "core operating" figures**, and the
fifth, the P&C combined ratio, is also non-GAAP as Chubb defines it (see (a) above).

1. **Core operating income** (non-GAAP). Line 10791: "Core operating income was a record for 2025, exceeding both prior year and plan. Core operating income growth was at the 6th percentile of the Financial Performance Peer Group. Contributing to our relative rank were significant improvements by two of our peers in operating income growth compared to prior year, each by 90% or more, with results reflecting recovery from substantial underperformance in prior years." And line 10793: "In evaluating this metric, the Compensation Committee further considered the Company's stable, consistent core operating income growth against more volatile peer performance over the past five years. Chubb's core operating income growth over the prior year, three-year and five-year periods was 8.9%, 54.8% and 200.6%, respectively."
2. **P&C combined ratio** (non-GAAP). Line 10810: "P&C combined ratio was a record low for 2025, evidencing world-class underwriting performance despite full-year catastrophe losses that were modestly higher than prior year. Absolute performance beat both plan and prior year, and relative performance was at the 97th percentile of the Financial Performance Peer Group."
3. **Core operating return on equity (ROE)** (non-GAAP). Line 10827: "Core operating ROE exceeded plan and was 0.1 percentage point below prior year. Relative performance was at the 30th percentile of the Financial Performance Peer Group. Our relative performance rank was impacted by the Company's strategic decision to maintain higher levels of capital relative to peers for both future risk and opportunity, as well as the Company being more acquisitive than peers and pursuing transactions we believe are in the best interests of the Company and shareholders over the long-term, resulting in a larger portion of equity comprising goodwill and other intangible assets."
4. **Core operating return on tangible equity (ROTE)** (non-GAAP). Line 10844: "Core operating ROTE exceeded plan and was 1.0 percentage point below prior year. Relative performance was at the 46th percentile of the Financial Performance Peer Group, which was impacted by the Company maintaining higher levels of capital relative to peers for both future risk and opportunity."
5. **Tangible book value per share growth** (non-GAAP). Line 10861: "Tangible book value per share growth performance substantially exceeded both prior year growth (by 11.6 percentage points) and plan. Relative performance was at the 51st percentile of the Financial Performance Peer Group on a reported basis, and at the 63rd percentile on an adjusted basis excluding from Chubb and peers any accretion or dilution to tangible book value resulting from extraordinary transactions such as acquisitions, dispositions, extraordinary investments and extraordinary share purchases."
6. **Total shareholder return.** Line 10882: "Our 1-year and 3-year annualized TSR were at the 32nd (4.4 percentage points from median) and 24th (3.5 percentage points from median) percentiles, respectively, of our Financial Performance Peer Group. Our cumulative 3-year TSR was 47.7%."

A candour note the proxy volunteers about itself, line 10777:

> "2025 performance further reflected the Company's consistent growth and outstanding results over the
> short-, medium- and long-term, underscoring the Company's discipline, financial strength and delivery of
> value to shareholders. While absolute performance was exceptional, our percentile ranks against peers on
> our key metrics were in some cases below median. Further information on each of the metrics and factors
> considered by the Compensation Committee are below."

**The catastrophe adjustment inside the bonus judgment**, line 10273, repeated at line 3186:

> "In the first quarter of 2026, the Compensation Committee reviewed the Company's 2025 results on an
> absolute basis against prior year and plan and relative to the Financial Performance Peer Group, as well
> as underlying core performance including and excluding catastrophe losses. The Committee also assessed
> performance against non-financial operating and strategic goals."

**No metric is weighted and none is designated most important**, line 18913:

> "In determining NEO compensation for a particular year, the Compensation Committee conducts a holistic
> review of overall performance and considers the Company's results on key financial metrics on an absolute
> basis and relative to its Financial Performance Peer Group. The Committee also considers achievement of
> operational and strategic goals. Our compensation practices are designed to reward both Company and
> individual performance across a number of measures and criteria. The Committee does not focus on only one
> performance measure or consider one measure the "most important"; rather, the Committee's review
> encompasses a holistic analysis of Company performance across different measures that capture various
> elements of the Company's performance, including operating income, underwriting performance, balance sheet
> strength, shareholder value creation, and achievement of strategic and operational objectives. The
> Committee believes this approach provides a more measured, consistent and appropriate basis on which to
> base compensation decisions. While the Committee does not consider one measure as the "most important",
> the Committee determined that, for purposes of the SEC's pay versus performance disclosure this year,
> core operating income should be considered the Company-Selected Measure because it most fully
> encapsulates amongst the key metrics the profitability of the full range of the Company's business."

### THE LONG-TERM INCENTIVE VEHICLE MIX: 100% PERFORMANCE-BASED EQUITY

Line 2967, repeated at line 10075:

> "Performance-based equity awards (granted in the form of performance stock units (PSUs) and performance
> shares (PSAs)) cliff-vest after the end of a three-year period if certain performance criteria are
> satisfied. **These awards comprise 100% of the annual long-term equity award for each of our NEOs.**
> See "How We Determine Total Direct Compensation Pay Mix - Equity Compensation" beginning on page 83 for
> details on our equity award criteria and vesting conditions."

Line 11691:

> "The annual equity awards granted to NEOs in 2026 (for 2025 performance) and 2025 (for 2024 performance)
> consisted entirely of performance-based equity awards (PSUs and PSAs). Prior to February 2025, one or
> more NEOs were also granted time-based restricted stock awards (RSUs and RSAs, which vest ratably over a
> 4-year period from the grant date) and stock options (which vest ratably over a 3-year period from the
> grant date, with a 10-year exercise period)."

Line 11693:

> "PSUs and RSUs carry the same vesting criteria and schedule as PSAs and RSAs. Shares are not issued for
> PSUs or RSUs until vesting (unless settlement is further deferred at the executive's election), while
> PSAs and RSAs are issued shares at grant but subject to forfeiture if the awards do not vest."

Size relative to the bonus, line 2965 (repeated at 10073) and line 11639:

> "When determining the final mix of pay for the CEO and other NEOs, the overall compensation package is
> weighted towards variable rather than fixed compensation, and towards long-term rather than short-term
> awards, in order to better link pay and performance and to align executive awards with the creation of
> long-term shareholder value. In line with this approach, long-term equity compensation of our CEO and
> other NEOs is typically 1.5 to 2.5 times the short-term annual cash bonus award."

> "Based on performance for each NEO, typically 1.5 to 2.5 times the annual cash bonus to emphasize
> long-term performance tied to shareholder value, and targeted to deliver total compensation in a range
> that typically approximates market median to the 75th percentile."

### PERFORMANCE-SHARE METRICS AND WEIGHTS: 70% TBVPS GROWTH, 30% P&C COMBINED RATIO, BOTH RELATIVE

Line 11697, the load-bearing sentence:

> "PSUs and PSAs cliff vest at the end of a three-year performance period if established performance
> criteria are met. To determine whether PSUs and PSAs vest, we compare our performance on a relative basis
> to our Financial Performance Peer Group. Our performance criteria tie the three-year cliff vesting of
> these awards to specified relative performance targets, namely our **tangible book value per share growth
> (70% weighting) and P&C combined ratio (30% weighting)**. If performance exceeds the 75th percentile,
> relative TSR is then measured to determine an additional number of Premium Awards that will vest."

Both are **non-GAAP** measures as Chubb defines them. Line 11699, on the choice and on how the annual and
the three-year use of the same two metrics differ:

> "We selected tangible book value per share growth and P&C combined ratio as metrics for our
> performance-based equity award plan because they are strong indicators of growth in shareholder value and
> underwriting profitability for a commercial property and casualty insurer and common financial
> performance measures for companies in our industry. While tangible book value per share growth and P&C
> combined ratio are also included among the key financial metrics used to determine annual variable
> compensation (in the form of an annual cash bonus and long-term equity awards), these two measures are
> evaluated differently for performance-based equity vesting purposes. For the determination of annual
> variable compensation, these metrics are considered along with other metrics, as well as TSR, on an
> annual basis against prior year, plan and peers. For the determination of PSU and PSA vesting, the two
> metrics are evaluated only on a relative basis against peers over a three-year time horizon."

Line 11703:

> "PSUs and PSAs each have two components: Target Awards and Premium Awards. The performance measurement
> and vesting requirements for each component as granted to our NEOs are summarized below."

(The summary table itself is rendered as a graphic in the filed document and carries no extractable text.
The percentile thresholds are recoverable from the vesting disclosure at lines 13404 and 17207, quoted
below: cumulative performance above the 75th percentile earns Premium Awards, with a three-year TSR
modifier tested at the 55th percentile.)

**Reserve-relevant point: on the catastrophe and prior-development question.** The PSU/PSA metric is the
**P&C combined ratio** itself, not the current accident year combined ratio excluding catastrophe losses.
The proxy's PSU/PSA criteria language contains no catastrophe exclusion and no prior-period-development
exclusion. The catastrophe adjustment appears only as a discretionary lens in the annual bonus review
(line 10273 above). The one formal adjustment written into the equity metric is for extraordinary
transactions, line 11734:

> "The Compensation Committee lacks discretion to increase the vesting of any performance-based equity
> award other than what was achieved based on actual performance. The Committee's analysis of performance
> metrics for all performance-based equity awards may take into account the effect of any extraordinary
> transaction (including acquisitions, dispositions, extraordinary investments and extraordinary share
> purchases) on tangible book value and the combined ratio of the Company and peer companies during the
> applicable performance measurement period. This permits the Committee to ensure that executives are not
> unduly penalized or enriched for taking actions that it determines are in the best interests of the
> Company."

**Independent verification of the calculation**, lines 11722-11724:

> "We have retained Ernst & Young Ltd. (EY), an independent public accounting firm, to verify the
> calculations of our performance criteria for the vesting of performance-based equity awards and to prepare
> a report on its findings."

> "Our Compensation Committee reviews the report prepared by EY and, based on that report, formally
> confirms whether, and to what extent, the performance criteria were met for the particular vesting period
> and how many, if any, awards vested as a result."

Line 16360, on the certification timing:

> "Column reports the target number of shares for performance-based equity awards. Awards cliff-vest
> following the end of a three-year performance period, subject to the achievement of specified performance
> criteria. The actual number of shares that may vest, including the extent of any premium awards, may be
> higher or lower than the target number. Vesting is determined in May following completion of the
> three-year performance period when the Compensation Committee, based on a report prepared by an
> independent accounting firm, formally confirms whether, and to what extent, the performance criteria were
> met for the particular vesting period and how many, if any, awards vested as a result."

**Actual vesting outcomes disclosed**, line 13404:

> "The PSA Target Awards granted in 2022 met relevant performance criteria and cliff-vested in 2025 as
> scheduled. Performance share awards granted to NEOs in 2022 earned a Premium Award of 77% (50% of the
> Target Awards granted) based on Cumulative Performance exceeding the 75th percentile and three-year TSR
> not meeting or exceeding the 55th percentile. The table below shows the value realized on vesting of those
> Premium Awards at the vesting dates for the 2022, 2021 and 2020 grants. The Target Awards granted to NEOs
> in 2021 and 2020 earned a Premium Award of 100% (65% of the Target Award)."

And line 17207, with the share counts:

> "Of Common Shares acquired on vesting, the following numbers were respectively acquired due to vesting of
> performance share Target Awards on May 15, 2025: Mr. Greenberg (58,409 shares), Mr. Enns (6,783 shares),
> Mr. Keogh (26,378 shares), Mr. Lupica (18,842 shares) and Mr. Ortega (5,936 shares). These amounts consist
> of performance share awards granted in 2022, which cliff-vested following the end of the three-year
> performance period. Of shares acquired on vesting, the following numbers were respectively acquired due to
> vesting of performance share Premium Awards granted in 2022: Mr. Greenberg (29,205 shares), Mr. Enns
> (3,392 shares), Mr. Keogh (13,189 shares), Mr. Lupica (9,421 shares) and Mr. Ortega (2,968 shares). The
> Target Awards granted to NEOs in 2022 earned a Premium Award of 77% (50% of the Target Award) based on
> cumulative performance exceeding the 75th percentile and three-year TSR not meeting or exceeding the 55th
> percentile."

Line 11726:

> "In May 2025, the Compensation Committee certified that Target Awards granted in 2022 earned a Premium
> Award of 50% of the Target Award following completion of the three-year cumulative performance period."

**The Financial Performance Peer Group**, lines 10302-10354: The Allstate Corporation; American
International Group, Inc.; CNA Financial Corporation; The Hartford Financial Services Group, Inc.;
Liberty Mutual Holding Company Inc.*; The Travelers Companies, Inc.; Zurich Insurance Group**.
Line 18890 names the TSR-comparison subset:

> "These companies for each period presented are The Allstate Corporation, American International Group,
> Inc., CNA Financial Corporation, The Hartford Financial Services Group, Inc., The Travelers Companies,
> Inc. and Zurich Insurance Group. The TSR of each company in the peer group has been weighted according to
> its respective stock market capitalization at the beginning of each period for which a TSR is provided.
> Calculations for both the Company and peer group include reinvested dividends."

**The compensation consultant**, line 11754:

> "Farient Advisors LLC has been retained directly by the Compensation Committee as its independent
> compensation consultant. Farient also provides director compensation-related market data and analysis to
> the Compensation Committee."

### CEO PAY TOTALS

**Summary Compensation Table**, `DEF14A_2026.txt` line 12518ff, Evan G. Greenberg, Chairman and Chief
Executive Officer (lines 12578-12708):

| year | Salary | Bonus | Stock Awards | Option Awards | All Other Comp | Total |
|---|---|---|---|---|---|---|
| 2025 | $1,600,000 | $11,000,000 | $18,850,128 | none | $1,730,454 | **$33,180,582** |
| 2024 | $1,600,000 | $9,500,000 | $17,350,017 | none | $1,688,077 | **$30,138,094** |
| 2023 | $1,550,000 | $9,000,000 | $15,650,006 | none | $1,461,311 | **$27,661,317** |

The timing caveat the proxy attaches, line 12270:

> "The total direct compensation for 2025 and its components for each of our NEOs are summarized in the
> table below. This table presents compensation more in alignment with how our Compensation Committee
> considered and made compensation decisions for performance in 2025 than the Summary Compensation table on
> the following page, because pursuant to SEC rules, the Summary Compensation Table reflects equity grants
> awarded during the prior calendar year (2025), even if corresponding to the year before's performance
> (2024). Our Compensation Committee and the Board of Directors approves NEO cash bonus and long-term
> equity awards each February corresponding to the prior year's performance; for example, cash bonus and
> equity awards for 2025 performance are approved in February 2026 and reflected in the table below."

**The Committee's own "total direct compensation" for 2025 performance**, lines 12307-12337:
Evan G. Greenberg, Chairman and Chief Executive Officer: Salary $1,600,000; Cash Bonus $11,000,000;
Long-Term Equity Award $21,400,000; **Total Direct Compensation $34,000,000**.
Lines 12345-12397: Peter C. Enns, Chief Financial Officer: $976,923 / $2,142,000 / $3,700,000 /
$6,818,923. John W. Keogh, President and Chief Operating Officer; Chairman, North America Insurance:
$1,200,000 / $4,161,000 / (equity and total continue past line 12397).

The decision itself, line 11850:

> "The Committee also further reinforced the alignment of compensation for Mr. Greenberg with Company
> performance by delivering 100% of the annual equity award in the form of performance-based equity awards.
> The Committee determined to increase Mr. Greenberg's total direct compensation by 13.5% compared to 2024.
> In doing so, the long-term equity award was increased by 13.5% to $21.4 million, and his annual cash bonus
> was increased by 15.8% to $11.0 million. The Committee also determined to keep Mr. Greenberg's base salary
> unchanged for 2026."

### CEO PAY RATIO

`DEF14A_2026.txt` line 18997:

> "The 2025 total annual compensation of our CEO calculated for purposes of disclosure in the Summary
> Compensation Table of this proxy statement was $33,180,582, which was approximately **512 times** the
> compensation of the median employee ($64,842) calculated in the same manner. The median employee is an
> accounts specialist based in the United States, and is the same employee used in the pay ratio calculation
> disclosed in our 2024 and 2025 proxy statements. We believe it is reasonable to continue to use the same
> employee for purposes of this calculation because there has been no change in our employee population or
> employee compensation arrangements that we believe would significantly impact the pay ratio disclosure."

Prior year, `DEF14A_2025.txt` line 19381:

> "The 2024 total annual compensation of our CEO calculated for purposes of disclosure in the Summary
> Compensation Table of this proxy statement was $30,138,094, which was approximately **477 times** the
> compensation of the median employee ($63,197) calculated in the same manner."

The identification date of that median employee, `DEF14A_2026.txt` line 18999:

> "We identified the median employee by examining compensation information derived from our global human
> resources information systems for all employees as of **December 31, 2023**, excluding the CEO."

### THE SWISS BINDING MAXIMUM COMPENSATION VOTE

`DEF14A_2026.txt` line 6067:

> "Swiss law and our Articles of Association require our shareholders to ratify, on an annual basis and in
> a separate binding vote, the maximum aggregate amount of compensation that can be paid, granted or
> promised to the members of Executive Management for the subsequent calendar year."

Line 6071:

> "The proposal of  $98 million in maximum aggregate compensation for Executive Management for the 2027
> calendar year is an increase from the $78 million for the 2026 calendar year approved at last year's
> annual general meeting."

Line 6077, on the cushion:

> "The degree of cushion built into the recommended amount considers market competitiveness, increased
> competition for talent, and the lengthy period of time between when this recommended amount is set and
> when variable compensation awards are actually determined approximately two years later."

Line 6075:

> "The recommended amount takes into account 2025 compensation decisions for Executive Management that
> reflect alignment with the Company's excellent financial and operational performance for the year, and
> allows for year-over-year increases in compensation for both 2026 and 2027 assuming Company performance
> meets or substantially exceeds performance thresholds established by the Board and Compensation
> Committee."

### A NOTE ON WHICH YEAR THE EQUITY BELONGS TO

`DEF14A_2026.txt` line 6261, about the Swiss Compensation Report table:

> "Third, the equity awards disclosed in the Swiss Compensation Report table represent grants for
> performance for that particular year (i.e., the equity awards that were granted in February 2026 for
> performance in 2025 are included in 2025 compensation). This is consistent with how our Compensation
> Committee views compensation for 2025 as described in the Compensation Discussion & Analysis. Due to SEC
> requirements, the Summary Compensation Table shows 2025 equity awards granted in 2025, which were intended
> to serve as compensation for 2024."

---

## (d) WHAT THE PROXY SAYS ABOUT SHARE REPURCHASES

**No repurchase authorisation size is disclosed in either proxy**, and no proxy passage states a policy
or a condition governing when the company repurchases. A search of `DEF14A_2026.txt` and
`DEF14A_2025.txt` for `repurchas` returns only the following.

`DEF14A_2026.txt` line 3564:

> "Our Board of Directors continues to believe that it is in the best interests of the Company and its
> shareholders to retain our earnings for future investment in the growth of our business, for share
> repurchases, for the possible acquisition of other companies or lines of business, and for dividends out
> of legal reserves as described in this proxy statement. The Company's statutory auditor,
> PricewaterhouseCoopers AG, has confirmed, in its audit report on the standalone Swiss statutory financial
> statements of the Company for the year ended December 31, 2025, that the proposed appropriation of
> available earnings complies with Swiss law and the Company's Articles of Association."

Line 7000, the only reference to the programme as such:

> "Chubb itself may also from time to time engage in transactions in Chubb securities, such as in connection
> with its **Board-authorized share repurchase program**. In doing so, Chubb is committed to adhering to
> applicable securities laws and requirements."

The Swiss capital-band mechanism that lets repurchased shares be cancelled, line 5242:

> "The share capital reduction component of the proposed capital band would also enable us to continue to
> cancel shares earmarked for cancellation that are acquired under our share repurchase program, ensuring we
> maintain capital management flexibility and continue to return capital to shareholders through share
> repurchases in accordance with Swiss requirements."

Line 5333:

> "In case of a capital reduction, the Board of Directors shall, to the extent necessary, determine the
> number of cancelled shares and the use of the reduction amount. The acquisition and holding of shares
> repurchased for purposes of cancellation under the capital band are, to the extent permitted by law, not
> subject to the 10% threshold for own shares within the meaning of Art. 659 para. 2 CO."

Line 5368, the stated consequence if the capital band fails:

> "If shareholders do not approve this proposal, we may be restricted in our ability to issue shares at
> times our Board deems necessary or advisable and in the best interests of the Company, or to cancel
> shares, which may impede our ability to return capital to shareholders through our share repurchase
> program."

**Amount, as the proxy states it.** `DEF14A_2026.txt` line 10616:

> "$4.91 billion returned to shareholders through dividends and share repurchases, a 41.1% increase from
> 2024, while continuing to invest in our business for the future."

`DEF14A_2025.txt` line 3072, repeated at 10654:

> "$3.48 billion returned to shareholders through dividends and share repurchases, while continuing to
> invest in our business for the future"

**The releases are more specific than the proxy.**

`8K_2026-07-21_EX991.txt` lines 1305-1307:

> "Total capital returned to shareholders in the quarter was $1.37 billion, comprising share repurchases of
> $979 million at an average purchase price of $327.18 per share and dividends of $395 million. Total
> capital returned to shareholders for the six months was $2.90 billion, comprising share repurchases of
> $2.12 billion at an average purchase price of $326.03 per share and dividends of $775 million."

`8K_2026-02-03_EX991.txt` lines 1288-1290 (Q4 2025):

> "Total capital returned to shareholders was $1.48 billion, comprising share repurchases of $1.10 billion
> at an average purchase price of $282.96 per share and dividends of $381 million."

`8K_2026-02-03_EX991.txt` lines 1638-1640 (FY2025):

> "Total capital returned to shareholders was $4.91 billion, comprising share repurchases of $3.39 billion
> at an average purchase price of $282.57 per share and dividends of $1.52 billion."

**The only stated condition governing repurchase found in any document gathered** is in the CEO's Q3 2025
commentary, not in a proxy. `8K_2025-10-21_EX991.txt` lines 860-861:

> ""In the quarter, we increased share buybacks since our stock is trading well below intrinsic value.
> Given our earning power, increased buyback activity will continue, while at the same time we build
> additional capital and our invested asset base."

`grep -i "intrinsic value\|buyback"` across all four EX-99.1 releases hits only those two lines. The three
item 8.01 8-Ks of 2025-08-06, 2026-05-20 and 2026-06-10 were fetched and are all senior-note offerings
(see `8K_2025-08-06_801.txt`, `8K_2026-05-20_801.txt`, `8K_2026-06-10_801.txt`). **No
repurchase-authorisation announcement was located among the filings gathered.**

Share count for reference, `DEF14A_2026.txt` line 5443:

> "As of March 6, 2026, there were 390,229,029 Common Shares outstanding. At that date, there were a total
> of 5,746,388 Common Shares that remained available for future issuance under the Current LTIP. The number
> of Common Shares to be issued upon exercise of outstanding options, warrants, and rights, was 9,222,037,
> with a weighted-average exercise price of outstanding options, warrants, and rights of  $213.93 and a
> weighted average remaining contractual term of 6.084 years."

---

## (e) SAY-ON-PAY RESULTS, SHAREHOLDER PROPOSALS, GOVERNANCE DISPUTE

### 2026 AGM, held May 21, 2026 (8-K filed 2026-05-22, accession 0001104659-26-065709, item 5.07)

`8K_2026-05-22_annualmtg.txt` lines 232-234:

> "The Company convened its AGM on May 21, 2026, pursuant to notice duly given. **Agenda Items 1-13
> submitted by the Company were approved in accordance with the Board's recommendations.** The matters
> voted upon at the AGM and the results of such voting are set forth below."

**No shareholder proposal was on the 2026 ballot.** All thirteen agenda items are company items, and
`DEF14A_2026.txt` contains no shareholder-proposal agenda item.

Votes, as For / Against / Abstain / Broker non-votes, from `8K_2026-05-22_annualmtg.txt`:

- **Item 12, Advisory vote to approve executive compensation under U.S. securities law requirements (the SEC say-on-pay)**, lines 628-638: **299,771,583 / 13,120,560 / 362,087 / 25,878,713**.
- **Item 11.3, Advisory vote to approve the Swiss compensation report**, lines 616-626: **301,088,681 / 11,808,686 / 356,863 / 25,878,713**.
- **Item 11.2, Maximum compensation of Executive Management for the 2027 calendar year** (the binding $98 million), lines 604-614: **305,650,550 / 6,781,846 / 821,834 / 25,878,713**.
- Item 11.1, Maximum compensation of the Board of Directors until the next annual general meeting, lines 590-600: 311,662,438 / 763,851 / 827,941 / 25,878,713.
- **Item 6, Election of Evan G. Greenberg as Chairman of the Board of Directors until the Company's next annual general meeting**, lines 486-497: **257,446,673 / 55,185,489 / 725,717 / 25,775,064**. This is the largest Against vote at the meeting.
- Item 5.1, Election of Evan G. Greenberg as director, lines 328-338: 303,590,041 / 9,406,375 / 257,814 / 25,878,713.
- **Item 5.11, Election of David H. Sidwell as director**, lines 450-460: **261,240,340 / 51,733,009 / 280,881 / 25,878,713**.
- **Item 7.3, Election of David H. Sidwell as Compensation Committee member**, lines 527-538: **273,873,190 / 39,077,356 / 303,684 / 25,878,713**.
- Item 5.2, Election of Michael P. Connors (the Lead Director) as director, lines 340-350: 291,139,799 / 21,825,091 / 289,340 / 25,878,713.
- Item 7.1, Connors as Compensation Committee member, lines 501-512: 301,696,049 / 11,251,161 / 307,020 / 25,878,713.
- Item 7.2, Michael L. Corbat as Compensation Committee member, lines 514-525: 306,466,577 / 6,485,713 / 301,940 / 25,878,713.
- Item 7.4, Frances F. Townsend as Compensation Committee member, lines 540-551: 302,777,363 / 10,183,621 / 293,246 / 25,878,713.
- Item 3, Discharge of the Board of Directors, lines 278-288: 309,919,814 / 2,225,460 / 1,030,519 / 25,878,713.
- Item 4.1, Election of PricewaterhouseCoopers AG (Zurich) as statutory auditor for FY2026, lines 290-301: 324,338,889 / 14,438,605 / 355,449 / 0.
- Item 4.2, Ratification of PricewaterhouseCoopers LLP (United States) for U.S. reporting for FY2026, lines 303-314: 320,826,057 / 17,953,280 / 353,606 / 0.
- Item 4.3, Election of BDO AG (Zurich) as special audit firm, lines 316-326: 338,030,366 / 684,245 / 418,332 / 0.
- Item 9, Renewal of a capital band for authorized share capital increases and reductions, lines 566-576: 330,556,940 / 8,133,261 / 442,742 / 0.
- Item 10, Approval of the Chubb Limited 2016 Long-Term Incentive Plan, as amended and restated, lines 578-588: 306,008,978 / 6,936,721 / 308,531 / 25,878,713.
- Item 13, Approval of the Sustainability Report for the year ended December 31, 2025, lines 640-650: 336,424,257 / 1,811,895 / 896,791 / 0.

The capital band, same 8-K lines 219-222:

> "At the AGM, the Company's shareholders approved an amendment of Article 6 of the Articles of Association
> to renew the Company's capital band, which authorizes the Board of Directors to increase or decrease the
> Company's share capital by up to 20% for a 1-year period ending on May 21, 2027, and in connection
> therewith, limit or withdraw the shareholders' pre-emptive rights in specified and limited circumstances,
> all as further described in the Proxy Statement under the heading "Agenda Item 9: Renewal of a Capital
> Band for Authorized Share Capital Increases and Reductions,"."

### 2025 AGM (8-K filed 2025-05-16, accession 0001104659-25-049835, item 5.07)

From `8K_2025-05-16_annualmtg.txt`:

- **Item 11, Advisory vote to approve executive compensation under U.S. securities law requirements**, lines 624-634: **315,166,639 / 15,403,826 / 371,244 / 27,048,017**.
- **Item 6, Election of Evan G. Greenberg as Chairman of the Board of Directors**, lines 494-505: **255,656,290 / 74,664,555 / 620,864 / 27,048,017**. The dissent on the chairmanship was larger in 2025 than in 2026.
- **Item 13, Shareholder proposal on Scope 3 greenhouse gas emissions reporting**, lines 648-658: **45,779,040 For / 282,479,933 Against / 2,682,736 Abstain / 27,048,017 broker non-votes**. Defeated.

### The 2025 proxy's statement in opposition to that shareholder proposal

`DEF14A_2025.txt` line 502 lists "Agenda Item 13: Shareholder Proposal on Scope 3 Greenhouse Gas
Emissions Reporting"; line 261 and line 1573 list it as "Shareholder proposal on Scope 3 greenhouse gas
emissions reporting, if properly presented". The Board's case against it, line 6257:

> "We share the Proponent's objective to address the realities of climate change. However, the Proponent's
> repeated demand for greenhouse gas (GHG) emissions disclosure relating to our underwriting, insuring and
> investment activities (i.e., Scope 3 emissions) serves no useful purpose and is duplicative and wasteful
> of Company and shareholder resources in light of: (i) our existing climate strategy and initiatives;
> (ii) our extensive climate disclosures; and (iii) the inescapable problems ignored by the Proponent in
> the feasibility of measuring the Scope 3 emissions requested and the lack of a connection between such
> data and assessing Chubb's climate readiness and transition efforts."

Line 6360:

> "There is no evidence that insurers' disclosure of Scope 3 emissions will lead to reductions in emissions
> across the global economy. In fact, initial evaluations of the impacts of net-zero alliances conclude
> that the process of Scope 3 accounting and goal setting by financial institutions and asset managers has
> had limited measurable impact on real-world emissions. As the Institutional Investor Group on Climate
> Change (IIGCC) noted in a 2024 discussion paper, "Scope 3 accounting and target-setting at portfolio or
> fund level may not lead to real-world outcomes that help to reduce climate change.""

Line 6350:

> "Unlike estimating Scope 3 emissions, our underwriting criteria and risk engineering expertise directly
> promote responsible risk behavior by clients, directly relate to our business and risks, and are more
> likely to reduce GHG emissions in the real economy, all within the annual policy renewal process."

### Engagement with proponents

`DEF14A_2026.txt` line 6902:

> "Our 2025-2026 engagement program targeted our top 50 shareholders, and also included proponents who
> submitted proposals for our 2025 and 2026 annual general meetings."

Line 7065:

> "In 2025, we solicited our 50 largest shareholders, representing nearly 65% of our outstanding Common
> Shares. The primary topics discussed during engagement are below. During the engagement cycle we also
> engaged with the shareholder proponents who submitted proposals for this year's and last year's annual
> general meetings."

Note the tension for a reader to resolve from the record: lines 6902 and 7065 refer to a proposal
submitted for the 2026 annual general meeting, yet no shareholder proposal appears on the 2026 ballot in
the item 5.07 8-K and none appears as an agenda item in the 2026 proxy.

### The non-binding nature of say-on-pay, and the two-layer structure

`DEF14A_2026.txt` line 6321:

> "This proposal, commonly known as the SEC's "say-on-pay" proposal, gives our shareholders the opportunity
> to express their views on our NEOs' compensation for the fiscal year ended December 31, 2025. This vote
> is not intended to address any specific item of compensation, but rather the overall compensation of our
> NEOs and the philosophy, policies and practices described in this proxy statement."

Line 6323:

> "This SEC say-on-pay vote is advisory, and not binding on the Company, the Compensation Committee or the
> Board of Directors. However, the Board of Directors and the Compensation Committee value the opinions of
> our shareholders and will continue to consider the outcome of this vote each year when making
> compensation decisions for our CEO and other NEOs."

Line 6181:

> "This non-binding retrospective vote on the compensation paid to the Board of Directors and Executive
> Management is in addition to the binding forward-looking votes on the maximum compensation of the Board
> of Directors and Executive Management described in the other sub-items in this Agenda Item 11, and the
> separate non-binding retrospective U.S. say-on-pay vote for compensation paid to our SEC named executive
> officers described in Agenda Item 12."

Line 6183:

> "This additional Swiss say-on-pay advisory vote provides our shareholders with a direct retrospective
> voice on director and executive compensation by providing a look-back on the use of prior-approved Swiss
> maximum compensation amounts."

Line 6201:

> "While we historically have had an advisory say-on-pay vote on the compensation paid to our named
> executive officers, that vote is required by SEC rules. The vote in this Agenda Item 11.3 is required
> pursuant to Swiss law. Consequently, both votes are required at the Annual General Meeting."

Line 6014, what happens if the binding Swiss maximum is rejected:

> "If shareholders do not ratify the maximum aggregate compensation amount proposed by the Board, our
> Articles of Association require the Board to consider the results of the vote, other shareholder feedback
> and other matters in its discretion. Then the Board may submit a new proposal for approval of the maximum
> aggregate amount at next year's annual general meeting or at an extraordinary general meeting of the
> shareholders. The Company may continue to pay compensation to the Board subject to the subsequent
> approval."

### Shareholder proposal mechanics for 2027

`DEF14A_2026.txt` line 19484:

> "Proposed shareholder proposal agenda items must be received no later than 5:00 p.m. Central European
> Time on December 8, 2026 and otherwise comply with the SEC requirements under Rule 14a-8 of the Exchange
> Act to be eligible for inclusion in the Company's 2027 annual general meeting proxy statement."

Line 19490:

> "In addition to the SEC rules for inclusion of shareholder proposals in a company's proxy material, under
> Swiss law, one or more shareholders of record owning registered shares of at least 0.5% of the Company's
> share capital (2,000,604 shares as of March 27, 2026) can ask that an item be put on the agenda of a
> shareholders' meeting. The request must be made at least 90 days prior to the anniversary date of the
> prior year's annual general meeting."

---

## (f) LOSS-RESERVE SETTING, RESERVE ADEQUACY, THE ACTUARIAL FUNCTION, AUDIT COMMITTEE OVERSIGHT

### Reserve setting is named in the Audit Committee's charge

`DEF14A_2026.txt` line 8043, and identically at `DEF14A_2025.txt` line 8148:

> "The Audit Committee is responsible for oversight of the Company's financial statements, financial
> reporting and internal controls, including Sarbanes Oxley (SOX) and financial model risk; **the process
> for establishing insurance reserves**; the Company's cybersecurity program and related exposures and
> risks; and legal, regulatory and compliance matters. The Audit Committee receives regular updates on these
> topics from various members of management, including the Chief Financial Officer, Chief Accounting
> Officer, Chief Auditor, **Chief Actuary**, Chief Information Security Officer, General Counsel, Head of
> Global Tax, and Chief Compliance Officer (who reports to the General Counsel), among others."

### What the Audit Committee Report says it actually did about reserves

`DEF14A_2026.txt` line 19030:

> "The Committee met 14 times in 2025, plus one in-depth session covering various matters. At the four
> regularly scheduled quarterly meetings, the Audit Committee met with members of management and PwC to
> review Company matters, including internal and independent audits; **loss reserve estimates and
> developments**; compliance-related activities; the Company's cybersecurity program and related exposures
> and risks; and other financial reporting and accounting, legal, tax and internal policy matters."

Line 19036, the annual independent reserve assessment:

> "In **January 2026, the Audit Committee met with the Chief Actuary to review, among other things, the
> external independent actuaries' review and their annual independent assessment of the Company's loss
> reserves.** Also, at a February 2026 meeting, the Audit Committee reviewed and discussed the 2025 annual
> financial statements, including Management's Discussion and Analysis of Financial Condition and Results of
> Operations (MD&A) in our 2025 Form 10-K, with management and PwC prior to their filing with the SEC."

Line 19034, the executive-session access:

> "Management participants at Audit Committee meetings include the Chief Financial Officer, Chief Accounting
> Officer, Chief Compliance Officer, Chief Auditor, Chief Actuary, Head of Global Tax, legal counsel and
> others as requested. Also at the quarterly meetings, the Audit Committee meets in executive session
> (without management present), which may also include meetings with representatives of PwC and with the
> Company's Chief Auditor, in each case to discuss the results of their examinations and their evaluations
> of the Company's internal controls and overall financial reporting, as well as with the Company's Chief
> Financial Officer, General Counsel and Chief Compliance Officer, as needed."

Line 19079, one of the enumerated matters the Committee discusses:

> "the effect of significant accounting policies in controversial or emerging areas for which there is a
> lack of authoritative guidance or consensus;"

### The same language a year earlier, plus an extra joint-committee reserve session

`DEF14A_2025.txt` line 19418:

> "The Committee met 14 times in 2024, plus one in-depth session covering various matters. At the four
> regularly scheduled quarterly meetings, the Audit Committee met with members of management and PwC to
> review Company matters, including internal and independent audits; loss reserve estimates and
> developments; compliance-related activities; the Company's cybersecurity program and related exposures and
> risks; and other financial reporting and accounting, legal, tax and internal policy matters."

`DEF14A_2025.txt` line 19445:

> "In January 2025, the Audit Committee met with the Chief Actuary to review, among other things, the
> external independent actuaries' review and their annual independent assessment of the Company's loss
> reserves. Also, at a February 2025 meeting, the Audit Committee reviewed and discussed the 2024 annual
> financial statements, including Management's Discussion and Analysis of Financial Condition and Results of
> Operations (MD&A) in our Annual Report on Form 10-K, with management and PwC prior to their filing with
> the SEC."

`DEF14A_2025.txt` line 19420:

> "Additionally, at its February 2024 and February 2025 meetings, the Audit Committee met in joint session
> with the Risk & Finance Committee to review and discuss the Company's enterprise risk management strategy,
> including risk priorities, risk perspectives and risk governance. **The February 2025 joint session also
> included a presentation on the Company's loss reserves from its external independent actuaries.**"

### Where the actuarial function reports

`DEF14A_2026.txt` line 11894, on the CFO:

> "Mr. Enns has executive responsibility for managing all aspects of Chubb's financial organization.
> Corporate units under his management include accounting and financial reporting, investment management,
> treasury, **actuarial** and tax."

Line 12179, on the head of North America general insurance:

> "Mr. Ortega has executive operating responsibility for all Chubb general insurance business in North
> America, including commercial P&C, personal lines, agriculture, and accident and health insurance.
> Mr. Ortega's scope of responsibility includes all products, underwriting, marketing and sales, claims,
> **actuarial** and support functions related to these business lines."

### The Risk & Finance Committee's remit, as the proxy states it

`DEF14A_2026.txt` line 7919:

> "The goal of the Risk & Finance Committee is to oversee that the Company's risk management process
> identifies and assesses relevant risks, has a reasonable and sound set of policies for setting parameters
> on risk, and, for specific material risks, has prepared itself to avoid or to mitigate outcomes that could
> adversely affect or threaten the viability of the Company."

### Reserve adequacy as management asserts it in a release

`8K_2025-10-21_EX991.txt` lines 862-864:

> ""In sum, Chubb's fundamentals and our positioning are excellent, and **our balance sheet, starting with
> our loss reserves, has never been stronger.** I am confident we will maintain superior earnings growth,
> including double-digit growth in EPS, book and tangible book value, with core operating ROE increasing to
> 14% plus over the medium term, CATs and FX notwithstanding.""

### Prior period development is disclosed as a separate headline bullet each quarter

`8K_2026-07-21_EX991.txt` lines 106-109:

> "Total pre-tax favorable prior period development was $283 million compared with $249 million in the
> prior year."

Lines 102-103, alongside it:

> "Total pre-tax net catastrophe losses were $475 million compared with $630 million in the prior year."

FY2025 release, `8K_2026-02-03_EX991.txt` lines 877-880:

> "P&C underwriting income was up 40% to $2.2 billion with a record combined ratio of 81.2%, supported by
> low CATs, **strong prior period reserve development** and a record low current accident year combined
> ratio of 80.4%, reflecting the strength of our businesses from around the globe."

The Financial Supplement carries the PPD line in the reconciliation itself (`8K_2026-07-21_EX992.txt`
line 22055 area of `DEF14A_2026.txt` equivalent: "Less: prior period development" at `DEF14A_2026.txt`
line 22055, and "Less: catastrophe losses" at line 22021; "Favorable prior period development (PPD) -
pre-tax" at `DEF14A_2026.txt` line 23278).

### How PPD is characterised in the non-GAAP definitions

`8K_2026-07-21_EX991.txt` lines 2017-2020, quoted in full under (a), contains the operative phrase:

> "and PPD as these unexpected loss developments on historical reserves are not indicative of our current
> underwriting performance."

And the mechanical treatment, `DEF14A_2026.txt` line 21871:

> "The combined ratio numerator is adjusted to exclude Cats, PPD and expense adjustments on PPD, and the
> denominator is adjusted to exclude net premiums earned adjustments on PPD and reinstatement premiums on
> Cats and PPD. In periods where there are adjustments on loss sensitive policies, these adjustments are
> excluded from PPD and net premiums earned when calculating the ratios."

### Where the release points a reader for reserve detail

`8K_2026-07-21_EX991.txt` line 1957:

> "investors.chubb.com , in the Financials section for more detailed information on individual segment
> performance, together with additional disclosure on reinsurance recoverable, **loss reserves**, investment
> portfolio, and debt and capital."
