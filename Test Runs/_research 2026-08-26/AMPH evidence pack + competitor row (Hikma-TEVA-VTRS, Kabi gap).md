# AMPH evidence pack + competitor row — built 2026-08-30
Supports `Test Runs/2026-08-30 Run - AMPH (Amphastar) v4.1.md`. Transcriptions from the
named filings and documents; judgments live in the run file, not here.

## Sources (documents actually read)
| doc | date | accession / origin |
|---|---|---|
| AMPH FY2025 Form 10-K (year ended 2025-12-31; auditor E&Y, unqualified; ICFR effective) | filed 2026-02-26 | 0001297184-26-000009 |
| AMPH Q2-2026 Form 10-Q (period 2026-06-30) | filed 2026-08-06 | 0001297184-26-000047 |
| AMPH Q1-2026 Form 10-Q (period 2026-03-31) | filed 2026-05-07 | 0001297184-26-000033 |
| AMPH DEF 14A (2026 annual meeting) | filed 2026-04-13 | 0001297184-26-000023 |
| FY2025 results 8-K Ex-99.1 | filed 2026-02-26 | 0001297184-26-000007 |
| Q2-2026 results 8-K Ex-99.1 | filed 2026-08-06 | 0001297184-26-000045 |
| Warning-letter 8-K (Item 8.01, event 2026-07-02) | filed 2026-07-08 | 0001297184-26-000041 |
| Director-appointment 8-K (event 2026-07-09) | filed 2026-07-13 | 0001104659-26-082772 |
| Letop supply-agreement 8-K + employment-agreements 8-K (2026-03-03) | filed 2026-03-06 | 0001297184-26-000013 / -000015 |
| XBRL companyfacts CIK 0001297184 (screening/transcription only) | pulled 2026-08-30 | data.sec.gov |
| Hikma FY2025 results press release (audited, FY ended 2025-12-31) | 2026-02-26 | hikma.com PDF `hikma-pharmaceuticals-plc-2025-full-year-results-combined-press-release-vfinal.pdf` |
| Teva companyfacts CIK 0000818686 (10-K XBRL) | pulled 2026-08-30 | data.sec.gov |
| Viatris companyfacts CIK 0001792044 (10-K XBRL) | pulled 2026-08-30 | data.sec.gov |
| Fresenius SE FY/25 equity-story briefing deck (parent-level segment disclosure) | Mar 2026 | fresenius.com PDF |
| FRED DGS30 fredgraph.csv | pulled 2026-08-30 | fred.stlouisfed.org |
| Price quote AMPH $22.01 close 2026-08-28 | pulled 2026-08-30 | Yahoo chart API — aggregator, live quote only, FLAGGED |

## Cap verification
- Cover count 42,535,392 → rounded 42.54M shares at 2026-07-31 (Q2-2026 10-Q cover, dei tag 42.54M).
- 42.54M × $22.01 = **$936M** vs sweep ~$938M → 0.2% gap (price-date drift). VERIFIED.
- Book equity $768.2M at 2026-06-30 → $18.06/share; P/B 1.22×.

## AMPH multi-year series (10-K XBRL, cross-checked to filed statements at FY2025)
$M unless noted. Total equity incl. NCI (ANP wholly owned; NCI immaterial).

| year | revenue | NI | OCF | capex | SBC | equity (YE) | ROE (avg eq) | diluted shs (M) |
|---|---|---|---|---|---|---|---|---|
| 2016 | 255.2 | 9.8 | 38.6 | 21.4 | 15.1 | 326.5 | — | 47.5 |
| 2017 | 240.2 | 3.6 | 39.2 | 35.1 | 17.1 | 333.7 | 1.1 | 48.4 |
| 2018 | 294.7 | −5.7 | 38.2 | 46.8 | 16.7 | 364.4 | −1.6 | 46.4 |
| 2019 | 322.4 | 48.9 | 41.8 | 41.6 | 17.3 | 427.5 | 12.4 | 49.9 |
| 2020 | 349.8 | 1.4 | 57.3 | 33.9 | 20.5 | 448.7 | 0.3 | 49.1 |
| 2021 | 437.8 | 62.1 | 98.0 | 27.5 | 18.7 | 445.5 | 13.9 | 49.8 |
| 2022 | 499.0 | 91.4 | 89.2 | 24.0 | 17.9 | 528.7 | 18.8 | 52.4 |
| 2023 | 644.4 | 137.5 | 183.5 | 38.2 | 20.2 | 639.4 | 23.5 | 53.0 |
| 2024 | 732.0 | 159.5 | 213.4 | 41.0 | 24.4 | 732.3 | 23.3 | 52.1 |
| 2025 | 719.9 | 98.1 | 156.1 | 34.9 | 27.3 | 788.8 | 12.9 | 48.2 |
| TTM 6/26 | 730.0 | 78.6 | 184.6 | 31.7 | 28.9 | 768.2 (6/30) | ~10.1 | cover 42.54 |

- FY2025 OCF cross-checked three ways: filed consolidated statement of cash flows
  "Net cash provided by operating activities 156,115"; MD&A prose "$156.1 million";
  XBRL $156.1M. MATCH. FY2024 also matches ($213.4M).
- H1-2026: revenue 355.1 (vs 344.9), NI 36.8 (vs 56.3; Q1-2026 NI only 6.4), OCF 99.2
  (vs 70.7), capex 18.1, SBC 16.4, buybacks 74.7.
- Interest expense: 27.2 (2023) · 30.3 (2024) · 25.5 (2025); interest income 8.7 (2025).
- 2025 G&A includes a $23.1M uninsured personal-injury jury verdict (settled and PAID
  Q4-2025; Note 19). 2025 cash taxes paid $22.7M vs pretax $123.6M.
- Goodwill trivial: $3.3M. Finite-lived intangibles $615.3M at 6/30/26 (mostly BAQSIMI).

## Product revenue (FY2025 10-K Note 3 table + Q2-2026 10-Q, $K)
| product | FY2025 | FY2024 | FY2023 | H1-2026 | H1-2025 | H1 chg |
|---|---|---|---|---|---|---|
| BAQSIMI | 185,358 | 126,898 | — (TSA in other rev) | 77,937 | 85,042 | −8% |
| Primatene MIST | 108,669 | 102,012 | 89,321 | 50,767 | 51,931 | −2% |
| Epinephrine | 70,643 | 94,090 | 81,650 | 35,067 | 34,767 | +1% |
| Glucagon | 69,084 | 108,319 | 113,684 | 21,075 | 41,445 | −49% |
| Lidocaine | 56,479 | 55,854 | 58,162 | 28,499 | 28,643 | −1% |
| Ipratropium (launched Apr-26) | — | — | — | 8,411 | — | new |
| Other products | 229,654 | 225,641 | 250,421 | 133,318 | 103,114 | +29% |
| Other revenues (Lilly TSA) | — | 19,153 | 51,157 | — | — | |
| **Total** | **719,887** | **731,967** | **644,395** | **355,074** | **344,942** | +3% |

Top-5 products = 68% of FY2025 revenue; BAQSIMI alone 25.7%.

**Price/volume decomposition, filed (MD&A):**
- FY2025 epinephrine: volume −$13.4M, price −$10.0M — "increased competition for our
  multi-dose epinephrine vial product."
- FY2025 glucagon: price −$24.3M, volume −$14.9M — "competition and the continued shift
  to ready to use glucagon products such as BAQSIMI®." Filing: "We anticipate that sales
  of glucagon will continue to decline in the future due to competitive dynamics."
- FY2025 enoxaparin −$9.9M, dextrose −$9.6M "due to increased competition"; offsets:
  albuterol +$14.7M (launched 8/2024), iron sucrose +$4.4M (launched 8/2025), sodium
  bicarbonate/atropine up "due to an increase in demand caused by other supplier shortages."
- H1-2026 BAQSIMI: price −$15.9M ("change in gross-to-net discounts due to changes in
  chargebacks and rebates and changes to the customer mix"), volume +$8.8M.
- H1-2026 glucagon: price −$13.7M, volume −$6.6M. Epinephrine: PFS +$6.1M "as a result
  of other supplier shortages", multi-dose vial −$5.8M competition.
- H1-2026 gross margin decline: "lower average selling prices for our higher margin
  products, including BAQSIMI®, glucagon, phytonadione, and epinephrine multi-dose vials"
  plus Rancho expansion costs plus IMS remediation costs.
- The class mechanism in the filing's own words (Item 1, Competition): "As competing
  generic manufacturers receive regulatory approval on the same products, market size,
  revenue and gross profit typically decline."

## Customers / suppliers (Note 6)
- McKesson 24% + Cencora 22% + Cardinal 19% = 65% of FY2025 net revenues.
- BAQSIMI is manufactured by a third-party CMO (single named dependency, Note 6 and Item 1).
- Single-source APIs for certain products; ANP (Nanjing) makes heparin starting material
  (enoxaparin), Amphadase starting material, isoproterenol, nitroprusside,
  medroxyprogesterone APIs; France (AFP) makes porcine insulin API, RHI API, AMP-028 API.

## Debt (Note 13, FY2025 10-K) — the BAQSIMI financing terms
- **2029 Convertible Notes $345.0M**, 2.0% coupon, unsecured, mature 2029-03-15;
  conversion price $62.96 (35% premium over the 2023-09-12 close); cash-settled up to
  principal; FV $319.1M at YE2025. Proceeds repaid $200M of the term loan (removing all
  amortization payments to maturity) + $50M buyback.
- **Wells Fargo Term Loan $250.0M** due June 2028, secured by substantially all assets;
  SOFR + 1.50–2.50% by consolidated net leverage; swap fixes SOFR leg at 4.04% on $250M
  notional. Consolidated net leverage covenant; "in compliance" at YE2025.
- **$200M revolver** (undrawn) same pricing; **ICBC (China) $24.6M** drawn, due Nov-2033,
  secured by ANP assets, PBoC prime −0.2%, principal biannual from May-2026; China
  Merchant Bank line ($4.1M cap) undrawn, expires Oct-2026.
- Maturity wall: 2026 $1.5M · 2027 $5.7M · **2028 $255.7M · 2029 $353.5M** · 2030 $3.3M.
- Unused revolving capacity $219.5M (MD&A).
- BAQSIMI purchase: $500M upfront (June 2023) + $125M guaranteed (paid June 2024) + $4M
  contract-assignment; **first $175M-contract-year sales milestone hit June 2026 →
  $100M payable Q3-2026** ($94.5M to intangibles, amortized over 21 remaining years).
  Total paid/payable through Q3-2026: $729M. Further sales milestones remain (originally
  up to $450M total).
- BAQSIMI product-rights intangible: $591.3M cost (now +$94.5M), 24-year weighted-average
  life, NBV $529.7M at YE2025.

## FDA status
- IMS (South El Monte, CA): FDA inspection Dec-2025 → Form 483 → response Jan-2026 →
  **"Official Action Indicated" classification Apr-2026** → **Warning Letter 2026-07-02**
  (8-K filed 2026-07-08; observations: investigation procedures, environmental monitoring
  and handling, manufacturing equipment). Does not restrict distribution; one product
  voluntarily suspended (not shortage-risk); remediation raises manufacturing expense and
  "could cause a slowdown in production" (Q2-2026 10-Q MD&A).
- Recent approvals: albuterol MDI (5/2024), iron sucrose (8/2025), teriparatide pen
  (12/2025), ipratropium HFA (2/2026). "One ANDA and one biosimilar insulin candidate
  are currently on file with the FDA" (FY2025 10-K and Q2-2026 10-Q).
- Pipeline: interchangeable insulin candidates AMP-004 (insulin aspart, on file) and
  AMP-005 (RHI); AMP-028 biosimilar (non-insulin, French API); AMP-019 intranasal
  epinephrine; AMP-105/107/109/110 early peptides; two GLP-1 APIs at ANP awaiting
  ex-US regulatory approval for meaningful third-party sales.

## Governance / Q3 facts (DEF 14A 2026-04-13 + 10-Q)
- Jack Yongfeng Zhang, **79**, CEO + President + **Chief Scientific Officer** + director
  (co-founder, 1996). Mary Ziping Luo, **76**, COO + **Chief Scientist** + **Chairman**
  (co-founder). Husband and wife. Classified three-class board.
- Ownership: Zhang/Luo jointly 12,421,688 shares = 26.7% (incl. APCL 6,827,679 = 15.3%);
  all officers+directors 29.6%; BlackRock 11.1%.
- **Pledged shares (Q2-2026 10-Q risk factor): 5.7M shares** (1.5M UBS + 1.2M East West +
  3.0M Cathay) securing credit lines up to $57M to APCL/Drs. Zhang & Luo; "UBS has an
  unlimited and unilateral right to call each of the credit lines for any reason
  whatsoever." Company pledging policy (2021, amended 2026) caps pledging at the lower of
  60% of an individual's holding or 15% of shares outstanding.
- Comp 2025 (Summary Comp Table): Zhang total $8,309,350; Luo $4,031,078 (couple
  **$12.34M = 12.6% of FY2025 NI**); Peters (CFO) $3,238,682; Zhou $2,542,634. CEO pay
  ratio 135:1 (2024 measure).
- Related-party web (10-K Note 18, Note 20; DEF 14A): Hanxin (11.5% equity-method stake;
  **majority owned by Zhang/Luo and family; son Henry Zhang is equity holder, GM and
  chairman**): contract manufacturing (Jan-2026 amendment adds GLOBAL territory for
  semaglutide API and 3/7/14mg semaglutide tablets, ex-US/Canada lidocaine and
  corticotropin), contract research (insulin/peptide research cell banks for AMP
  candidates; $0.4M paid 2025), Primatene China/Middle East/SE-Asia distribution
  (Genreach), BAQSIMI Greater-China distribution (Chengong, Oct-2025), corticotropin
  license (Jan-2026: $2M upfront + up to $14M dev + $75M sales milestones + 5% royalty
  capped $7.5M/yr and $60M cumulative). Letop (majority owned by Henry Zhang): chemical
  intermediates, cost-plus; $14K paid 2025; new 5-yr agreement Mar-2026. FY2025 revenue
  recognized from Hanxin $1.09M.
- Guidance practice: **no quantitative revenue/EPS guidance found in either earnings
  release read** (FY2025, Q2-2026); the words "guidance"/"outlook" do not appear.
  Negative product commentary is volunteered ("glucagon will continue to decline").
- Non-GAAP: "adjusted non-GAAP net income" headlined — FY2025 $156.6M vs GAAP $98.1M
  (+60%); add-backs: intangible amortization $25.0M, **share-based compensation $27.3M**,
  litigation provision $23.1M, less tax $16.9M.
- Buybacks: cumulative authorization $485M since inception ("primary goal … to offset
  dilution"); FY2025 $75.6M; H1-2026 $74.2M for 3.66M shares (avg ≈ $20.30; Q2-2026
  monthly averages $21.09/$18.78/$19.43); remaining authorization $0.4M at 2026-06-30.
  Diluted count 53.0M (2023) → cover 42.54M (7/2026), **−20% from peak**.
- Litigation: $34.1M personal-injury jury verdict Oct-2025 ($11.0M insured; $23.1M in
  2025 G&A; paid Q4-2025); three CA wage/hour/PAGA employee actions (2024-2025) open.
- Timeliness: warning letter received 2026-07-02, 8-K filed 2026-07-08 (4 business days).

## COMPETITOR ROW (same metric where computable: ROE = NI ÷ avg equity, latest FY;
## injectables-segment margin as the class read; windows as stated)
| company | FY2025 ROE | 5-yr picture | injectables-class read (filed) |
|---|---|---|---|
| **AMPH (Dec-25)** | **12.9%** | 5-yr mean ~18.5% (2021-25); TTM ~10.1% | GAAP gross margin 49% (2025), 51% (2024); op margin ~19.5% (2025) |
| Hikma (LSE:HIK, Dec-25, audited results release) | 16.3% (402 ÷ avg 2,464 net assets) | 5-yr series not pulled — WORK ORDER | Injectables rev $1,423M; **core op margin 31.0% (2024: 35.3%); 2026 guide 27-28%; medium-term margin target WITHDRAWN**; named US erosion: testosterone, calcitonin |
| Teva (NYSE:TEVA, Dec-25, 10-K XBRL) | 21.2% (1.41 ÷ avg 6.65) — one profitable year | **5-yr NI sum −$2.8B** (2021-25); revenue 16.7→17.3B flat | generics-wide price erosion; no injectables segment split — row limit |
| Viatris (NASDAQ:VTRS, Dec-25, 10-K XBRL) | **−21%** (NI ≈ −3.51 = pretax −3.665 less tax −0.15) | NI 2021-25: −1.27, +2.08, +0.05, −0.63, −3.51; revenue 17.9→14.3B | company shrinking; no injectables split — row limit |
| Fresenius Kabi (private within Fresenius SE) | **GAP — no standalone filing** | — | parent deck: FY25 revenue €8.6bn; EBIT-margin ambition 17-19% (raised from 16-18%) |
| Pfizer (hospital/sterile injectables, ex-Hospira) | not comparable at company level | — | unsegmented — GAP named |

Row limit [E3-61]: same-metric ROE is computable for only 3 of 5 named peers; the two
giants' injectable businesses are not separately filed. The filing names 16 competitors
(Pfizer, BPI Labs, Lupin, Viatris, Fresenius Kabi USA, Apotex, American Regent, Hikma USA,
Par, Cipla USA, Meitheal, Dr. Reddy's, Xeris, Medefil, Accord, Teva USA) — most private or
unsegmented. Peers taken: 4 of the ~16 named (plus Kabi scale context), and that is what
the industry's filings allow without months of work.

## Sovereign
USD 30-year (FRED DGS30, fredgraph.csv, issuing-authority series): **5.19% at 2026-08-27**
(last print in file pulled 2026-08-30; series lags 1-2 days, immaterial).
`tools/run.py AMPH` failed on the FRED fetch from this environment (read timeout, same as
the CCS/ETD/FLO runs); the series was pulled directly and dated.

## Owner-earnings arithmetic (inputs transcribed above; judgments in the run file)
- 5-yr (2021-25): OCF 148.0 − SBC 21.7 − capex 33.1 = **93.2**
- 3-yr (2023-25): 184.3 − 24.0 − 38.0 = **122.3**
- FY2025: 156.1 − 27.3 − 34.9 = **93.9**
- TTM 6/2026: 184.6 − 28.9 − 31.7 = **124.0**
- Yields on $936M cap: 93 → 9.9% · 94 → 10.0% · 122 → 13.0% · 124 → 13.2% · 70 → 7.5%
