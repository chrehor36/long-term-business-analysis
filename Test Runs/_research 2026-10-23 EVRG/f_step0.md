## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $84.95 (close 2026-10-22, as printed by `python tools/run.py EVRG`; an aggregator quote, live quote only, flagged under operator rule 5).
- **Shares by class** from the latest filing's cover: Evergy, Inc. common stock, 230,567,172 shares outstanding on July 31, 2026
  (Form 10-Q for the quarter ended June 30, 2026, filed 2026-08-06, accession `0001711269-26-000100`; `python Screens/cover_shares.py EVRG`).
  The script's two further lines of 1 share each are the single shares of Evergy Metro, Inc. and Evergy Kansas Central, Inc.,
  "held by Evergy, Inc." (the 10-Q cover's own words); they are not a second class. Check against issued less treasury: the 10-Q
  balance sheet shows "230,561,238 ... shares issued" at June 30, 2026, without par, and no treasury-stock line; the cover count
  is about 6,000 shares higher a month later (stock plans), consistent. The 8-Ks filed after the 10-Q (2026-08-24,
  `0001193125-26-363625`: $600M of 6.40% junior subordinated notes due 2057 issued and the $500M term loan terminated;
  2026-09-16, `0001193125-26-393088`: $350M of Evergy Kansas Central 5.600% first mortgage bonds) issue no shares.
  **Equity claims not in the count:** (a) $1,155.9M of 4.50% convertible notes remain after the January and February 2026
  repurchases (10-Q, Note 8); the 10-K states an initial conversion rate of 16.1809 shares per $1,000, a conversion price of
  about $61.80; principal is settled in cash and only the excess in shares, so at $84.95 the excess is about 4.4 shares per
  $1,000, about 5.1M shares (arithmetic mine); at any price below about $61.80 the excess is nil. The 10-Q's diluted count was
  236.5M for the second quarter. (b) Forward sale agreements under the at-the-market program: physical settlement would have
  delivered 5.2M shares for $413.5M of cash at June 30, 2026 (10-Q). The count used below is the basic 230.567M; the
  convertible's excess is named wherever it changes a figure.
- **Market cap:** $19,586.7M (230.567172M × $84.95).
- **Sovereign for the earnings currency (USD):** 5.29%, the US Treasury daily par yield curve, 30-year, 10/22/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): Form 10-K for 2025 (combined filing of Evergy, Inc., Evergy Kansas Central and Evergy
  Metro), filed 2026-02-19, accession `0001711269-26-000017`: Item 1, Item 1A, Item 7 in full, the income-tax note, the
  balance sheet and cash-flow statement; Form 10-Q for the quarter ended 2026-06-30, `0001711269-26-000100` (balance sheet,
  income statement, Note 8, the forward sale note); proxy statement DEF 14A filed 2026-03-26, `0001140361-26-011357`;
  8-Ks of 2026-07-01 (`0001193125-26-292565`, a new $3.5B master revolving credit facility replacing the $2.5B facility of 2021 and a $1B delayed-draw term loan of May 2026), 2026-08-24 and 2026-09-16 as above; the
  XBRL company facts for 2016 to 2025 (transcription, cross-checked below). EDGAR records one former name, Monarch Energy
  Holding, Inc., 2017-07-10 to 2017-11-16; no merger, spin-off or split since the 2018 merger appears in the 8-K list from
  2025-01-01 (items 1.01, 1.02, 2.02, 2.03, 5.02, 7.01, 8.01, 9.01 only).
- **One figure cross-checked against the filed statement:** cash flows from operations of $2,045.2M (2025), $1,983.7M (2024)
  and $1,980.2M (2023) in the 10-K's MD&A, Liquidity, equal the XBRL values `tools/run.py` prints; capital expenditures of
  $2,796.9M, $2,336.6M and $2,334.0M in the same MD&A section equal the XBRL capex column.
- `python tools/run.py EVRG` arithmetic lines only (saved as `Test Runs/_research 2026-10-23 EVRG/run_py_output.txt`): owner cash
  on the capex basis (OCF less stock pay less all capital spending) of -$372M, -$368M, -$772M for 2023 to 2025, five-year
  mean -$506M; on the depreciation basis $886M, $854M, $862M, five-year mean $779M. Stock pay $15M to $21M a year, the tag
  resolved every year. Finance-lease principal $7M to $18M a year sits in financing and is shown as an alternate. The tool's
  yield, growth and "points over the sovereign" lines are not read (Part VII, the tooling).
- **The lines of evidence this name needs, derived from the 10-K's Items 1, 1A and 7** (the brief's one departure: the analyst
  chooses them): (1) the regulatory compact in two states, allowed against earned returns, rate-case outcomes, and the
  regulatory lag the filing itself names (the Kansas and Missouri plant-in-service deferrals capped at 1.5% and 2.5% a year,
  Item 1A); (2) the capital plan of $21.6B for 2026 to 2030, of which $9.3B is new generation, and how it is funded ($12.3B of
  debt and hybrid securities and $3.3B of equity to be issued, Item 7, Liquidity); (3) the large-load and data-center demand
  on which the plan rests (Item 1A's first financial risk; the large-load tariffs and 1,900 MW of service agreements, Item 7);
  (4) the coal fleet, 37% of 2026 capacity and 47% of the 2025 fuel mix, and the stranded-asset risk Item 1A names;
  (5) the 2021 cash year (Winter Storm Uri) and the fuel-recovery mechanisms; (6) the people: adjusted EPS, pay, the 2018
  merger and the buyback that followed it, the convertible repurchase of 2026; (7) the debt: $16.5B gross at June 30, 2026,
  dividend covenants, credit ratings, wildfire and nuclear exposure.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years" **[M1997-109]**,
and for a regulated utility the business is a rate base earning what two state commissions and FERC allow. The foundation that
bears hardest is who is paid to tell you: the plan on which every forward figure in the 10-K rests is the company's own
five-year capital programme, to be funded by $12.3B of debt and hybrids and $3.3B of equity sold through banks, and "You do not
want to ask an investment banker what he thinks the earnings are going to be in five years of something he's trying to sell"
**[M2011-083]**; projections are not consulted **[M1995-050]**, so this run values only what the filings show has happened. No
macro view of data-center demand enters **[M2000-094]**; the demand matters only as a filed contract term (minimum bills,
collateral). **Contrary evidence, written down as found** **[M1997-127]**: (1) diluted EPS was $3.83 in 2021 and $3.66 in 2025
(XBRL, 10-Ks `0001711269-22-000008` and `0001711269-26-000017`) while $11.6B went into plant over the five years; (2) owner
cash after all capital spending was negative in every year of the window (-$636M to -$772M a year at the ends), so the
dividend of $613M in 2025 was paid out of borrowing; (3) gross debt rose from $9.9B at the end of 2019 to $16.5B at June 30,
2026 while equity rose from $8.6B to $10.2B; (4) the company features an adjusted EPS that excludes $49M of 2025 losses on its
own non-regulated venture investments.

## THE STANDING RULE
The purchase would be a part-interest bought for cash, unlevered, sized by the buyer; owning it does not by itself expose the
buyer to a call, a collateral demand or a debt he cannot pay, so it does not touch the rule, provided no borrowed money is used
to buy it **[L2014-005]**, **[M2004-065]**. The target's own debt is weighed at Q9, not here.

---
