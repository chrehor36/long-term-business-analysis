# LLY 2026-10-06 — filing extracts and arithmetic (research notes)

Raw filings are under `cache/` (gitignored). Fetched from SEC EDGAR with `fetch.py` (User-Agent with contact), stripped with `strip.py`.

## Documents
| Document | Filed | Accession |
|---|---|---|
| 10-K FY2025 (lly-20251231.htm) | 2026-02-12 | 0000059478-26-000013 |
| 10-Q Q2 2026 (lly-20260630.htm) | 2026-08-05 | 0000059478-26-000081 |
| DEF 14A 2026 (lly-20260317.htm) | 2026-03-20 | 0000059478-26-000029 |
| 8-K Q2 2026 results, EX-99.1 (q226lillysalesandearningsp.htm) | 2026-08-05 | 0000059478-26-000077 |

## Step 0
- Price $1,143.12, 2026-10-05, `tools/run.py` (aggregator, live quote only).
- Shares: 941,357,065 common at 2026-08-03, 10-Q cover (accession 0000059478-26-000081); `Screens/cover_shares.py LLY` agrees.
- Market cap: 941.357M x $1,143.12 = $1,076.1B.
- Sovereign USD 30-year 5.66%, US Treasury daily par yield curve, 10/05/2026 (`tools/sources.py`).
- Cross-check: FY2025 net cash from operating activities $16,813M (run.py, XBRL) = consolidated statement of cash flows,
  10-K line "Net Cash Provided by Operating Activities | 16,813 | 8,818 | 4,240"; MD&A: "Net cash provided by operating
  activities increased to $16.8 billion in 2025, compared with $8.8 billion in 2024."
- run.py first attempt failed on SEC HTTP 429 (rate limit; parallel sessions); the retry succeeded. Its statement-lines
  block still records one accession NOT read on a 429 (0000059478-24-000065).

## Owner cash (run.py arithmetic, USD M)
| FY | OCF | SBC | D&A | capex | OCF-SBC-capex | OCF-SBC-D&A |
|---|---|---|---|---|---|---|
| 2023 | 4,240 | 629 | 1,527 | 3,448 | 163 | 2,084 |
| 2024 | 8,818 | 646 | 1,767 | 5,058 | 3,114 | 6,405 |
| 2025 | 16,813 | 626 | 1,997 | 7,841 | 8,346 | 14,190 |
Acquired IPR&D cash payments (not in capex): 2023 3,944; 2024 3,346; 2025 3,008. With them, OCF-SBC-capex-IPR&D:
2023 -3,781; 2024 -232; 2025 5,338. Five-year window (run.py): OE capex mean 4,539, OE D&A mean 6,769. Yield on price:
0.36% (capex, 3-yr) to 0.70% (D&A, 3-yr); 0.42% / 0.63% on the 5-yr window. COMPUTATION, NOT A CLEARANCE; not used,
because the run closed at Q1.

## Revenue concentration (10-K FY2025, disaggregation table; 10-Q Q2 2026; EX-99.1)
Tirzepatide = Mounjaro + Zepbound (USD M):
| Year | Mounjaro | Zepbound | Tirzepatide | Total revenue | Share |
|---|---|---|---|---|---|
| 2023 | 5,163 | 176 | 5,339 | 34,124 | 15.6% |
| 2024 | 11,540 | 4,926 | 16,466 | 45,043 | 36.6% |
| 2025 | 22,965 | 13,542 | 36,507 | 65,179 | 56.0% (filer: "56 percent") |
| H1 2026 | 18,605 | 9,088 | 27,693 | 42,773 | 64.7% (filer: "65 percent") |
Trulicity (the prior incretin), U.S.: 2023 5,433; 2024 3,694; 2025 2,914 (US compound patent and data protection 2027).
FY2026 revenue guidance $85.0B to $87.0B (EX-99.1); no guidance beyond the current year found in the release or the 10-Q
(text search for 2030, 2031, 2035, "long-term outlook", "long-range": none).

## Exclusivity (10-K FY2025, Item 1, Our Intellectual Property Portfolio)
Mounjaro/Zepbound compound patent: U.S. 2036, major European countries 2037, Japan 2040; data protection U.S. 2027.
Jardiance U.S. 2029; Trulicity U.S. 2027; Verzenio U.S. 2031; Taltz U.S. 2030.

## Filer's words used in the run
- Item 1: "Our long-term success depends on our ability to continually discover or acquire, develop, and commercialize innovative medicines."
- Item 1, Competition: "When new products, uses, or delivery systems with therapeutic, convenience, or cost advantages are introduced, including by developing new modalities, our existing products become subject to decreased sales volumes, progressive price reductions, or both."
- Item 1A: "it can be very difficult to predict revenue growth rates of, or variability in demand for, new or future products and indications"
- Item 1: "we cannot predict the extent to which our business may be affected by current or potential future legislative, regulatory, or private actor developments."
- Item 1: "The outcome of our preliminary agreements with the U.S. government and broader U.S. policy efforts to align domestic pharmaceutical pricing with international benchmarks [...] is uncertain"
- Item 1A: "in July 2025, CVS Caremark [...] stopped covering Zepbound as a preferred obesity management medicine on some insurance plans"
- Item 1, IRA: "The full impact of the IRA on our business and the pharmaceutical industry, including the implications to us of a competitor's product being selected for price setting, remains uncertain."
- 10-Q Q2 2026 MD&A: "Longer term, the durability of our cardiometabolic health product offerings and sustainability of our growth and prospects will depend on our ability to maintain or strengthen our competitive position as the therapeutic landscape evolves and to deliver further innovations"
- EX-99.1 Q2 2026: U.S. price down 3% (about 9% before rebate-estimate adjustments); outside-U.S. price down 36% (China NRDL).
