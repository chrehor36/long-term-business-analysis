# JPM 2026-10-06 — filing notes (extracts, with where they sit)

Raw filings are under `cache/` (gitignored, re-fetchable from EDGAR). Text extracts below are verbatim from the
stripped filings; line numbers refer to the stripped text dumps in `cache/` and are for re-finding only.

## Form 10-K FY2025, filed 2026-02-13, accession 0001628280-26-008131

**Item 1A, Market (dump line 471 onward):** "In addition, JPMorganChase’s investment portfolio and market-making
businesses could suffer losses due to unanticipated market events and conditions, including: [...] events or conditions
that cause previously uncorrelated market factors to become correlated (and vice versa) [...] the inability to
effectively hedge risks related to market-making and investment portfolio positions, or [...] other market risks that may
not have been adequately considered when developing, structuring or pricing a financial instrument."

**Item 1A, valuation (dump line ~522):** "Market volatility, illiquid market conditions and other fluctuations in the
financial markets could make it extremely difficult to value certain financial instruments. [...] Furthermore,
JPMorganChase’s hedging and other risk management strategies may not always be effective, and it could incur
significant losses, if extreme market events were to occur."

**Item 1A, counterparties (dump line ~526):** "The financial or operational failure of a significant market participant,
such as a major financial institution or a CCP [...] could cause substantial and cascading disruption within the
financial markets".

**Item 1A, model risk (dump line ~824):** "The models and estimations that JPMorganChase uses may not be effective in
all cases to identify, observe and mitigate risk because of factors such as: [...] inherent limitations associated with
forecasting uncertain economic and financial outcomes".

**Item 1A, legal (dump line 356):** "the extent of JPMorganChase’s exposure to legal matters is unpredictable and could,
in some cases, exceed the amount of reserves that JPMorganChase has established for those matters."

**Market Risk Management, VaR (dump line 4755):** "As VaR is based on historical data, it is an imperfect measure of
market risk exposure and potential future losses. In addition, based on their reliance on available historical data,
limited time horizons, and other factors, VaR measures are inherently limited in their ability to measure certain risks
and to predict losses, particularly those associated with market illiquidity and sudden or severe shifts in market
conditions."

**Note 5, derivative notional table:** total derivative notional $50,642B at 2025-12-31 ($47,723B at 2024-12-31):
interest rate $29,536B, credit $1,381B, foreign exchange $15,595B, equity $3,432B, commodity $698B. "While the notional
amounts disclosed above give an indication of the volume of the Firm’s derivatives activity, the notional amounts
significantly exceed, in the Firm’s view, the possible losses that could arise from such transactions."

**Fair-value table, 2025-12-31 ($M):** derivative receivables gross level 1 2,496 / level 2 594,960 / level 3 8,926;
netting (548,605); net 57,777. Total trading assets 802,873. Total assets at fair value 1,831,870, of which level 3
26,499. Total Firm assets 4,424,900.

**Deposits table (averages, $M):** total 2,506,565 at 1.80% (2025); 2,386,642 at 2.08% (2024); 2,359,067 at 1.70%
(2023). Noninterest-bearing U.S. 572,014, non-U.S. 32,169 (2025). Year-end deposits 2,559,320. Loans 1,493,429;
loans-to-deposits 58% (liquidity section).

**Income:** total net revenue 182,447 (managed 185,581); net income 57,048 (2025). Markets revenue $35.8B, up 19%
(Fixed Income $22.5B, Equity $13.3B). Stockholders' equity 362,438.

## Form 10-Q Q2 2026, filed 2026-08-06, accession 0001628280-26-054343
Total assets 5,015,069; trading assets 1,062,072; stockholders' equity 374,598 (2026-06-30). Average deposits Q2 2026
2,685,578 at 1.60%. Gross derivative receivables before netting about $690.6B (4,822 + 672,730 + 13,048), netting
(622,833), net 67,767.

## 8-K Item 2.02, filed 2026-07-14, accession 0001628280-26-048078, EX-99.1
Headline: "NET INCOME OF $21.2 BILLION ($7.70 PER SHARE), NET INCOME EXCLUDING SIGNIFICANT ITEMS OF $16.9 BILLION
($6.14 PER SHARE)". The significant items are "a $4.6 billion net gain related to Visa shares in Corporate as well as
$1.0 billion of gains on certain equity investments". Markets revenue $12.1B of $58.0B managed revenue in the quarter.

## DEF 14A, filed 2026-04-06, accession 0000019617-26-000096
Fetched; not read (Q5 not reached).

## XBRL cross-check
`us-gaap:Assets` at 2025-12-31 = 4,424,900,000,000 in accession 0001628280-26-008131; matches the balance sheet.
