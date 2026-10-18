==============================================================================
Solaris Energy Infrastructure, Inc.  (SEI)   —  ARITHMETIC ONLY, NOT A VERDICT
==============================================================================
  sovereign USD   5.43%   10/15/2026   US Treasury daily par yield curve
  earnings currency: USD (the XBRL unit of the cash-flow series)
  price     65.16 USD   2026-10-15   (aggregator — live quote only)
  shares    0.0M      market cap 0.00B USD
  share basis: STALE (2846 days old; the newest filed) WeightedAverageNumberOfDilutedSharesOutstanding + WeightedAverageNumberOfSharesOutstandingBasic for the year to 2018-12-31 - a WEIGHTED AVERAGE, not a cover-page count
  ** A weighted average is an EPS denominator, not a share count.
     For a multi-class filer it is denominated in ONE class. Verify:
     python Screens/cover_shares.py SEI **

  OWNER EARNINGS   mean of 3 years of (OCF − SBC) − maintenance capex   (USD millions)
  OCF tag: NetCashProvidedByUsedInOperatingActivities

        FY end        OCF      SBC       D&A      capex    OE capex      OE D&A
    2023-12-31       89.4      7.7      36.2       64.4        17.2        45.4
    2024-12-31       59.4     10.6      47.2      188.4      -139.7         1.5
    2025-12-31      209.1     23.4      84.3      646.8      -461.1       101.4
          mean                                               -194.5        49.5
  OE capex = OCF − SBC − capital spending;  OE D&A = OCF − SBC − depreciation and amortization.
  lower of the two each year: capex basis in 2023, 2024, 2025
  mean of the year-by-year lower: -194.5;  of the higher: 49.5  (lines 2 and 3 below use these)
  SBC tag by year: 2023 ShareBasedCompensation; 2024 AllocatedShareBasedCompensationExpense; 2025 AllocatedShareBasedCompensationExpense
  capex tag by year: 2023 PaymentsToAcquirePropertyPlantAndEquipment; 2024 PaymentsToAcquirePropertyPlantAndEquipment; 2025 PaymentsToAcquirePropertyPlantAndEquipment

  STATEMENT LINES FROM THE FILINGS (calculation linkbase; transcription; USD millions)
  read: 0001628280-26-012501, 0001697500-25-000013, 0001697500-24-000023
    2023-12-31  other capital payment (not in capex)  us-gaap:FinanceLeasePrincipalPayments (financing section)  2.5
    2024-12-31  other capital payment (not in capex)  us-gaap:FinanceLeasePrincipalPayments (financing section)  3.0
    2025-12-31  other capital payment (not in capex)  us-gaap:FinanceLeasePrincipalPayments (financing section)  3.2

        FY end  OCF filed OCF ex-sec  SBC+other    capex  capex alt  OE capex alt  OE D&A alt
    2023-12-31       89.4       89.4        7.7     64.4       66.9          14.7        45.4
    2024-12-31       59.4       59.4       10.6    188.4      191.4        -142.6         1.5
    2025-12-31      209.1      209.1       23.4    646.8      650.0        -464.3       101.4
          mean                                                             -197.4        49.5
  OCF ex-sec = OCF as filed less the securities lines' and PIK interest's effect; SBC+other = the SBC column plus
  the other stock-pay lines; capex alt = capex plus the other capital payments. The columns
  above are AS FILED; these are the ALTERNATES. Neither is chosen here.

  THE OTHER WINDOW (5-yr, 5 yrs of data)   OE capex -122.3  OE D&A 32.8   yield -7265.08% (capex) 1947.74% (D&A)
  DIVERGENCE vs the 3-yr window: +36.4% on the lower of the two bases
  ** The spread between the windows is part of the range, not a tiebreak;
     do not pick a window and defend it. **

  1. THE YIELD                 capex basis -11556.25%   D&A basis 2938.77%   vs sovereign 5.43%
  2. GROWTH THE PRICE ASSUMES  REFUSED - the lower owner-earnings mean
     is at or below zero. A DCF on a non-positive base produces no
     number; the negative bottom boundary IS the statement.
  3. POINTS OVER THE SOVEREIGN REFUSED on the same ground at the lower mean; higher mean +94.57

  BALANCE SHEETS, 10 fiscal year-ends (USD millions; first-filed XBRL vintage, transcription only; read the filed statements)
    year-end          assets liabilities      equity        cash receivables   inventory    goodwill intangibles     lt debt    retained
    2018-09-30             -           -         321           -           -           -           -           -           -           -
    2018-12-31           425         118         169          25          40          10          17           5           -          43
    2019-11-30             -           -           -           -           2           -           -           -           -           -
    2019-12-31           505          95         264          67          39           7          17           4           -          74
    2020-12-31           412          96         201          60          18           1          13           3           -          21
    2021-12-31           406         108         203          36          33           2          13           2           -           6
    2022-12-31           463         145         216           9          65           5          13           1           -          13
    2023-12-31           468         153         206           6           -           7          13           1          30          17
    2024-12-31         1,123         456         356         114          72          11         104          72         308          18
    2025-12-31         2,143       1,316         564         353         103          14         105          60         180          26
    accessions: 0001558370-23-003344, 0001628280-26-012501, 0001697500-19-000009, 0001697500-19-000042, 0001697500-20-000006, 0001697500-21-000019, 0001697500-22-000011, 0001697500-24-000023, 0001697500-25-000013
    equity: StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest (2018); StockholdersEquity (2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025)
    lt debt: LongTermDebtNoncurrent (2023, 2024, 2025)

    DEBT ON THE FACE OF THE BALANCE SHEET (USD millions; the lines the filings' calculation linkbase puts under liabilities)
    year-end            d1        d2        d3        d4        d5        d6        sum
    2018-12-31           -         -         -         -        13         -         13*
    2022-12-31           -         -         -         -         8         -          8*
    2023-12-31           -        30         -         -        30         -         60*
    2024-12-31           8       308         0         -         -         -        316*
    2025-12-31           4       180       880         -         -         -      1,064*
    d1 = us-gaap:LongTermDebtCurrent
    d2 = us-gaap:LongTermDebtNoncurrent
    d3 = us-gaap:ConvertibleDebt
    d4 = us-gaap:NotesPayableCurrent
    d5 = us-gaap:LongTermLineOfCredit
    d6 = us-gaap:LongTermNotesPayable
    sum = the lines tagged that year-end; '-' = not tagged under that element that year (read the statement);
    * = a partial sum, some line untagged that year-end. Leases are not in it.

  STILL OWED BEFORE THE VALUE QUESTION OPENS:
    - read the balance sheets over the years above BEFORE the income account (v5 Q4)
    - read the filing: MD&A, cash-flow detail lines, footnotes; record accession no.
    - cross-check one figure above against the filed statement
    - say where in the capex band maintenance sits, and why, citing the filing
    - fill the competitor row from the competitors' own filings
