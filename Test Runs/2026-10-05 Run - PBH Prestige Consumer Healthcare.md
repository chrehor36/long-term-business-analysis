# Company Run: Prestige Consumer Healthcare Inc. (NYSE: PBH), 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run surface copied from
`Test Runs/_TEMPLATE - Company Run.md` before any fetch. Working folder: `Test Runs/_research 2026-10-05 PBH/` (filings as
fetched, text conversions, `fetch.py`, `totext.py`, `ledger.py`, `owner_cash.py`, `q7_calc.py` and its output
`q7_calc_output.txt`, `run_py_output.txt`, `cover_shares.txt`, peers in `peers/`, earnings releases in `pr/`).
Every judgment cites a v5 ledger id in bold; every filing fact carries its accession. A STOP that returns OUT or TOO HARD
closes the run and later questions are marked NOT REACHED. No em dashes are used in this file's own prose; where the
protocol's heading "COMPUTATION, NOT A CLEARANCE" appears it is written with a comma for that reason.

**POSITION NOTE, declared before any verdict:** not checked. `PORTFOLIO.md` is on this run's blind list, so whether the
operator holds PBH is unknown to the analyst.

**CONTAMINATION DECLARED.** (1) The session's opening context showed recent commit subjects for other companies' v5 runs
(TDS, CENT, OGN, PENN) and a session-state commit, and the git status listed untracked 2026-10-05 run files for CALY, PRKS
and SKYW and research files for AYI; none was opened, and none concerns PBH or its industry except that CENT (pet and garden
brands sold through large retailers) is a branded-consumer name: its subject line said it closed OUT at Q2 on retailer
concentration and store brands. I read that line before this run began. It bears on the same question asked here (brands
against retailers), so it is declared as a possible anchor and the Q2 reading below was made from PBH's and its
competitors' own filings only. (2) A text search of `Framework/v5/` for the row M2002-026, made to see how the framework
treats EBITDA talk, printed the file name of the barred, not-adopted CASE file on small-cap gaps (not opened) and an excerpt
of `Framework/v5/tests/A HRB - analyst 2.md` that names a gap between Q4's "rules OUT" list and Q4's STOP; that excerpt
shaped how the gap is described at Q4 and in the last section. (3) No other `Test Runs/` file about PBH was opened; a
directory listing for "PBH" and "Prestige" before the copy returned nothing.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $45.61 (2026-10-05; `tools/run.py`, Yahoo chart endpoint; **aggregator, live quote only, flagged** under
  operator rule 5; the date is today and the quote may be intraday).
- **Shares by class** from the latest filing's cover: one class, common stock, **47,374,522** (10-Q for the quarter ended
  2026-06-30, filed 2026-08-06, accession `0001295947-26-000042`; dei count as of 2026-07-31; `python Screens/cover_shares.py PBH`,
  output in `cover_shares.txt`). No other class; preferred authorized 5,000 thousand, none issued (10-K FY2026 balance sheet).
- **Market cap:** 47.3745M x $45.61 = **$2,160.8M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 10/05/2026
  (`tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for FY ended 2026-03-31, filed 2026-05-14, accession `0001295947-26-000016` (Items 1, 1A in part, 3, 5, 7, the
    balance sheet, cash-flow statement, equity statement, tax note, receivables note).
  - 10-Q for the quarter ended 2026-06-30, filed 2026-08-06, accession `0001295947-26-000042` (Notes 2 and 8, MD&A, subsequent events).
  - DEF 14A filed 2026-06-29, accession `0001295947-26-000021` (CD&A, ownership table, pay versus performance).
  - 8-Ks: 2026-03-20 `0001104659-26-032332` (Breathe Right purchase agreement, $1.045B, with its Ex 99.1 presentation);
    2026-05-13 `0001295947-26-000013` (FY2026 results, LaCorium agreement; Ex 99.1); 2026-06-16 `0001104659-26-074259`
    (Breathe Right closed; $1.045B term loan; ABL amended); 2026-07-06 `0001295947-26-000029` (LaCorium closed, $95M added
    term loan); 2026-07-15 `0001104659-26-083872` ($400M 6.250% notes due 2034); 2026-08-06 `0001295947-26-000040`
    (Q1 FY2027 results, Ex 99.1); 2026-08-14 `0001295947-26-000049` (SVP Operations retires).
  - 10-Ks FY2011 to FY2025 (accessions `0001295947-11-000011`, `-12-000029`, `-13-000018`, `-14-000015`, `-15-000015`,
    `-16-000051`, `-17-000018`, `-18-000013`, `-19-000015`, `-20-000018`, `-21-000021`, `-22-000015`, `-23-000017`,
    `-24-000017`, `-25-000017`), read for market positions, customer and supplier concentration, impairments, acquisition
    prices and product-group revenue; and the Q4 earnings releases FY2013 to FY2026 (Ex 99.1 of the May 8-Ks, accessions
    in `pr/`) for the filer's organic revenue figures.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2026 **$257,627
  thousand** on the filed cash-flow statement (10-K `0001295947-26-000016`) = `tools/run.py` 257.6. Also total
  stockholders' equity $1,887,516 thousand and goodwill $581,109 thousand on the filed balance sheet = run.py 1,888 and 581.
- **`python tools/run.py PBH`, arithmetic lines only** (output in `run_py_output.txt`; its v4 material ignored, Part VII):

| FY (Mar) | OCF | SBC | capex | D&A | owner cash, capex basis | owner cash, D&A basis |
|---|---|---|---|---|---|---|
| 2022 | 259.9 | 9.0 | 9.6 | 32.1 | 241.2 | 218.8 |
| 2023 | 229.7 | 12.4 | 7.8 | 32.6 | 209.5 | 184.7 |
| 2024 | 248.9 | 14.0 | 9.6 | 30.7 | 225.4 | 204.2 |
| 2025 | 251.5 | 11.2 | 8.2 | 30.2 | 232.1 | 210.2 |
| 2026 | 257.6 | 10.8 | 11.2 | 31.3 | 235.6 | 215.5 |
| 5-yr mean | | | | | **228.8** | 206.7 |

  USD millions, as filed (XBRL, first-filed vintage; FY2022 and FY2023 from `owner_cash.py` on the same company facts;
  SBC for FY2018 to FY2022 from the tag `StockIssuedDuringPeriodValueShareBasedCompensation`, since the cash-flow SBC tag is
  missing those years). Alternates printed by run.py: finance-lease principal (2.8, 4.5, 2.5 in FY2024 to FY2026) would
  lower the capex-basis figure by those amounts; shown, not chosen. SBC is resolved and complete (one SBC line a year, no
  other stock-pay lines). Owner cash above is **after interest and after cash taxes**; it includes a deferred-tax
  add-back of $23.1M, $14.4M and $22.7M in FY2024 to FY2026 (cash-flow statement, "Deferred and other income taxes"),
  which is mostly the tax amortization of purchased brands (deferred tax liability on intangibles $477.0M at 2026-03-31,
  tax note). It is real cash while it lasts; each purchase's shield ends fifteen years after it.

- **Owner cash before and after acquisitions, FY2012 to FY2026** (`owner_cash.py`; acquisitions net of cash acquired from
  the cash-flow statements, Fleet's $803.8M from the FY2017 10-K text because the XBRL tag reads zero that year):

| FY | owner cash (capex basis) | acquisitions | divestiture proceeds | buybacks | owner cash after acquisitions |
|---|---|---|---|---|---|
| 2012 | 63.8 | 662.8 (GSK brands) | 0 | 0 | -599.0 |
| 2013 | 123.6 | 0 | 21.7 | 0 | 145.3 |
| 2014 | 103.7 | 55.2 (Care, Australia) | 0 | 0 | 48.5 |
| 2015 | 143.2 | 749.7 (Insight, Hydralyte) | 10.0 | 0 | -596.5 |
| 2016 | 160.8 | 227.0 (DenTek) | 0 | 0 | -66.2 |
| 2017 | 136.6 | 803.8 (C.B. Fleet) | 110.7 | 0 | -556.5 |
| 2018 | 188.7 | 0 | 0 | 0 | 188.7 |
| 2019 | 171.4 | 0 | 65.9 (Household Cleaning) | 50.0 | 237.3 |
| 2020 | 194.9 | 2.8 | 0 | 56.7 | 192.1 |
| 2021 | 204.8 | 0 | 0 | 11.9 | 204.8 |
| 2022 | 241.2 | 247.0 (Akorn eye care, TheraTears) | 0 | 0 | -5.8 |
| 2023 | 209.5 | 0 | 0 | 50.0 | 209.5 |
| 2024 | 225.4 | 10.6 | 0 | 25.0 | 214.8 |
| 2025 | 232.1 | 8.2 | 0 | 51.5 | 223.9 |
| 2026 | 235.6 | 123.7 (Pillar5, Clear Eyes supplier) | 0 | 156.3 | 111.9 |
| **sum** | **2,635.3** | **2,891.0** | **208.3** | **401.4** | **-47.4** |

  After the fiscal year: Breathe Right and other brands $1,045.0M (closed 2026-06-12, all term-loan debt) and LaCorium
  Health about $150.0M (closed 2026-07-01, $95.0M term loan plus cash) (10-Q `0001295947-26-000042`, Notes 2 and 18).
  Over fifteen years every dollar of owner cash, and a little more, went into brands; the debt paydown and the buybacks
  were paid from the dollars the acquisitions borrowed and then returned.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would hold PBH "Would I be happy buying this stock if the market closed for
five years?" **[M1997-109]**, and the answer turns on the brands' cash and the debt now ahead of the equity, not on the
quote. The market serves and does not instruct: the stock fell from $85.97 (March 2025 monthly close, aggregator) to
$45.61; "It just tells us prices." **[M2006-077]**, and the fall is read here only as a price. Who is paid to tell you:
the Breathe Right figures ("~$200 million of revenue and ~$95 million of EBITDA", Ex 99.1 to `0001104659-26-032332`) are a
seller's twelve months repeated by a buyer whose pay rises with acquired sales and EBITDA (Q6), and five banks arranged
the loan for fees (8-K `0001104659-26-074259`): "you do not get impartial advice from Wall Street" **[M2020-037]**;
"don’t ask the barber whether you need a haircut" **[M2011-083]**. The analyst's habits: the hunt is for "what you’re
missing" **[M2025-013]**, written down at once **[M1997-127]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Organic revenue fell 4.5% in FY2026 and Eye & Ear Care fell 20.6% on "a limited ability to supply demand for Clear
   Eyes" (10-K FY2026, MD&A); Clear Eyes went from #1 in redness relief (FY2021 10-K) to #2 (FY2023) to #3 (FY2026).
2. One privately owned supplier makes about 21% of gross revenue (10-K FY2026, Item 1); the company wrote off a $10.3M
   loan to a supplier in FY2026 (10-K FY2026, receivables note and MD&A).
3. Walmart 20% and Amazon 15% of gross revenue in FY2026 (10-K FY2026, Item 1); Walmart was 15.9% to 23.8% in every year
   from FY2011 to FY2026 (each year's 10-K).
4. About $716M of brand and goodwill impairments in FY2018 to FY2025 against about $2.9B of acquisitions since FY2012
   (XBRL impairment tags; FY2018 Beano and Comet $99.3M; FY2019 Fleet, DenTek, Efferdent $155.0M plus $33.5M Oral Care
   goodwill; FY2023 Summer's Eve, DenTek, TheraTears $298.7M plus $22.7M finite-lived plus $48.8M goodwill; FY2025
   $12.5M). TheraTears was bought in July 2021 for $228.9M and impaired in February 2023.
5. Monistat, the largest brand by carrying value, is the one indefinite-lived asset whose fair value exceeds carrying
   value by less than 10%; a 50-basis-point rise in the discount rate would have cost $16.6M (10-K FY2026, critical
   estimates). Women's Health revenue fell from $252.5M (FY2021) to $205.1M (FY2026) and fell 5.1% again in Q1 FY2027.
6. Store brands: Perrigo reports "accelerating store brand volume share gains" in soft OTC consumption in 2025 (Perrigo
   10-K 2025, `0001585364-26-000009`).
7. Debt doubled after the year end: $1.0B at 2026-03-31 to $2.045B at 2026-06-30 and about $2.14B after LaCorium;
   the company's own pro forma "bank-defined net leverage of ~4" times EBITDA (Ex 99.1 to `0001104659-26-032332`).
8. Management pay is on Net Sales (50%) and Adjusted EBITDA (50%) for the annual plan and the same two measures for the
   performance units (DEF 14A `0001295947-26-000021`), so a debt-financed purchase raises both.
9. Gross margin fell from 56.2% to 51.3% in Q1 FY2027 (Pillar5 plant costs and inventory step-up; 10-Q MD&A).

## THE STANDING RULE
Owning PBH shares bought with the buyer's own money and sized so that a total loss is survivable does not put the buyer at
risk of ruin; bought on margin it would: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "We are
never going to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. The target's own debt
is weighed at Q9, not here.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What it is, from the 10-K:** about 890 employees selling over-the-counter health brands, most bought from larger
  owners who had found them "non-strategic" (10-K FY2026, MD&A General), made mostly by 95 contract manufacturers
  (18 under long-term contracts, about 60% of gross sales) plus three owned plants making about 21% (Item 1). Revenue
  $1,088.7M FY2026; North America 83.9%, International (mainly Australia) 16.1%. Twelve of the seventeen major brands
  in the filer's table are #1 in a narrow segment it defines from IRI data, the other five #3 or #4; brands with a #1
  position were 63.7% of revenue.
- **The key variables** **[M1998-044]**: (a) consumer demand in each small ailment category (wart removal, motion sickness,
  vaginal anti-fungal, ear wax, adult enemas, sore throat, eye redness); (b) each brand's share and price against the
  store brand at Walmart, Amazon and the drug chains; (c) supply continuity from outsourced makers; (d) what the company
  pays for the next brand and how it finances it. (a) and (b) are about customers, not technology: "laying out what their
  prospective customers will do in the future" **[M2017-019]**; "what we think we can project out in terms of consumer
  behavior and threats to a business" **[M2023-030]**. The categories in the 2012 10-K (Chloraseptic, Dramamine, Compound W,
  Luden's, Debrox, BC/Goody's) are the same ailments and mostly the same brands in 2026. (c) is knowable from the filings
  and is bad (contrary evidence 1 and 2). (d) is a capital-allocation question and belongs to Q6, where it is weighed.
- **Tests:** where will it be in ten years **[M2000-037]**: selling the same remedies, with the category and store-brand
  pressures of the last fifteen years, its size set mainly by purchases; how the industry will develop and "where the
  company will stand within the industry" **[M2012-065]**: a niche leader in many small aisles, not a scale leader; do the
  past statements tell the future ones **[M2008-033]**: yes for the base business (fifteen years of gross margin 50.8% to
  58.0% and organic growth of minus 4.5% to plus 10.1% a year), less so for a roll-up whose next purchases are unknown;
  would insiders write it down: the filer itself writes a long-term organic expectation of "2% to 3%" (Ex 99.1 FY2022,
  `0001295947-22-000012`), so this is not the forecast insiders "would not want to put down on paper" **[M2000-105]**; doubt about the perimeter
  **[M2002-092]**: the brands are understood; the price of the next brand is not, and that doubt is carried to Q6, not here.
- **Routing:** not a fast-changing industry; not a bank; not a holding company in the Q1 sense (one business, many brands).
- **VERDICT: IN.** The economics of the existing portfolio can be pictured ten years out from the filings: small
  ailment categories, branded at about 55% gross margin, sold through a few large retailers, made by others. The first
  question, "can I understand it?" **[M1995-051]**, is answered yes for the business. The unknown future purchases are a judgment on people
  and capital (Q5, Q6), not on understanding.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing?" **[M1995-038]**. Each test with its filing fact:

1. **The attacker with money** **[M2011-015]**. Most PBH categories are small: the filer put the U.S. motion-sickness
   category at $95.5M, Dramamine's share at 48.0% (10-K FY2016, `0001295947-16-000051`). A rich branded attacker gains
   little from a $100M aisle; the rows name this castle: "very small markets that aren’t really too attractive to anybody
   with any sense to enter" **[M2011-017]**. The attacker that does come is the store brand, which needs no advertising
   and sits on the same shelf; and "one competitor is frequently enough to ruin a business" **[M2012-108]**.
2. **Pricing power and the agony before a rise** **[M2005-020]**. The filer gives no price and volume split in any 10-K
   or release read (search for "pricing", "price increase", "volume" in the FY2026 10-K and the FY2013 to FY2026
   releases; the FY2022 release says growth will be "driven by ... pricing actions"). Indirect evidence: gross margin held
   through the 2021 to 2024 cost inflation, 58.0% (FY2021), 57.1%, 55.4%, 55.5%, 55.8%, 54.7% (FY2026), a fall of about
   three points; "the businesses with strong competitive positions manage to pass through increases in raw material
   costs" **[M2005-017]** is met in part, not in full. The rows' warning runs the other way too: "if you establish too wide
   a differential between Coke and a private label product, you will change consumption patterns somewhat" **[M2001-088]**.
3. **Unit volume and share of mind.** Not disclosed. Organic revenue, which includes price, grew at a geometric mean of
   about 1.3% a year over FY2016 to FY2026 (the filer's eleven figures: 2.8, 1.0, 1.7 pro forma, 0.1, 1.3, -2.4, 10.1,
   3.5, 0.2, 1.2, -4.5; Q4 releases in `pr/`). If any of that is price, volume grew by less. The competitors that do split
   it show volume falling across U.S. branded OTC in 2025: Kenvue Self Care organic -3.0%, volume -3.4%, price +0.4%
   (Kenvue 10-K 2025, `0001944048-26-000030`); Haleon North America organic -0.4%, price +1.0%, volume/mix -1.4% (Haleon
   20-F 2025, `0001104659-26-027443`).
4. **The low-cost position.** Not PBH's castle: it buys finished goods from contract makers whose prices "are subject to
   change due to fluctuations in input costs" (10-K FY2026, Item 1) and calls itself a "low-cost operating model" only in
   overhead.
5. **The brand in the customer's mind, and against the retailer.** "you’re probably going to get better gross of margins if
   they ask for you by name" **[M2023-073]**. The margin test over the whole span, below, says customers do ask for these
   names at a price above the store brand. Against the retailer: Walmart 15.9% to 23.8% of gross revenue in each of FY2011
   to FY2026 and Amazon now 15%; "the value of having the brand moves over to the retailer from the product itself"
   **[M2001-090]** is the standing threat, and the narrated mistake is a brand house that underestimated "what the retailer
   is" **[M2019-041]**. The retailer "is going to use all the pressure they’ve got" **[M2015-038]**. Fifteen years of
   stable margins say the pressure has been met, not removed.
6. **Would the customer still choose it over the low bid** **[M2017-009]**. For a remedy bought when ill (an enema, a
   yeast-infection treatment, a wart freezer, a motion-sickness tablet before a trip), the filings show the branded leader
   holding #1 for fifteen years: Chloraseptic #1 (42.8% share 2012, 48.4% 2016, #1 2026); Dramamine #1 (37.4%, 48.0%, #1);
   Compound W #2 (35.9%) then #1 (37.8%, #1); Debrox #1 (53.3% 2016, #1 2026); Monistat #1 (55.1% 2016, #1 2026)
   (10-Ks FY2012, FY2016, FY2026). Shares stopped being disclosed after FY2016.
7. **Ask the competitors.** Perrigo, the store-brand maker, says retailers earn "a greater percentage and dollar profit"
   on store brands and that store brands gained volume share in 2025 (Perrigo 10-K 2025). The silver bullet is aimed
   at the national brand on every shelf PBH occupies.
8. **Widening or narrowing** **[M1999-108]**. Mixed by brand. Narrowing: Clear Eyes #1 to #3 in five years on supply
   failure; Women's Health down 19% from FY2021 to FY2026 with Summer's Eve impaired (FY2023) and Monistat at the edge
   (FY2026); Luden's #3 to #4; DenTek #3 to #4; impairments on Beano, Comet, Fleet, DenTek, Efferdent, Summer's Eve and
   TheraTears. Holding or widening: Gastrointestinal (Fleet, Dramamine, Gaviscon, Hydralyte) $130.1M FY2020 to $179.3M
   FY2026; the #1-brand share of revenue 58.6% (FY2024) to 63.7% (FY2026). "for every Inevitable, there are dozens of
   Impostors" **[L1996-031]**; here there are several of each inside one company.
9. **What could destroy, modify or reduce it** **[M2000-014]**: store-brand share in a weak consumer year; Amazon's rank
   algorithms replacing shelf space (the filer names "loss of shelf space/digital rank" from shortages, 10-K FY2026 Item
   1A); single-source supply; and slow decline, which "can lull you to sleep easier" **[M2014-038]**.

**The competitor row, same metric from the competitors' own filings** (gross margin, XBRL transcription of each filer's
annual statements; `peers/gm.py`; HLN in GBP under IFRS):

| Company | role | gross margin over the span | other | accession (latest) |
|---|---|---|---|---|
| PBH | branded niche OTC | FY2010 52.4%, FY2013 55.7%, FY2016 57.9%, FY2021 58.0%, FY2024 55.5%, FY2026 54.7% | organic about 1.3%/yr FY2016-FY2026 | `0001295947-26-000016` |
| Perrigo (PRGO) | store-brand OTC maker | FY Jun 2012 34.5%, 2015 37.2%, 2017 40.0%, 2020 35.9%, 2022 32.7%, 2025 35.1% | store brand volume share gains 2025 | `0001585364-26-000009` |
| Church & Dwight (CHD) | brands, household and OTC | 2011 44.2%, 2017 45.8%, 2022 41.9%, 2025 44.7% | (organic figures not extracted) | `0001193125-26-048139` |
| Kenvue (KVUE) | large OTC brands | FY2021 55.9%, 2023 56.0%, 2025 58.1% | Self Care 2025 volume -3.4% | `0001944048-26-000030` |
| Haleon (HLN) | large OTC brands | 2020 59.7%, 2022 60.6%, 2025 64.2% | N. America 2025 price +1.0%, vol/mix -1.4% | `0001104659-26-027443` |

Read over the whole span, not one year: PBH's gross margin has run about 17 to 22 points above the store-brand maker's
in every year both report, from 2012 to 2025, and about level with Kenvue's and a few points below Haleon's, firms many
times its size with far larger advertising budgets. The brand premium has held against the store brand for fifteen
years. That is the castle. Its width is not visible: no share or volume data after FY2016, and the three-point margin
slide since FY2021 runs the wrong way.

- **Would it stand without the lord?** Yes for the brands: Dramamine and Fleet need no genius; "How much do they depend
  on the genius of the lord in the castle?" **[M1995-038]** is answered "little". The roll-up depends on management's
  buying, which is Q6.
- **The judgment.** The castle is not shown open on the evidence: margins over the whole span and fifteen years of #1
  positions in most niches say the customer still pays for the name. Parts of it are filling in, on the filer's own
  evidence (Clear Eyes, Women's Health, the impaired brands), and the moat is narrow and kept by advertising of about
  14% of revenue (FY2013 14.5%, FY2026 13.7%). "when we see a moat that’s tenuous in any way" **[M2000-019]** is the
  closest call of the run; I read the moat as narrow and partly eroding rather than tenuous as a whole, because the
  erosion is concentrated in named brands while the majority holds, and the margin record is long. The partial erosion
  is carried into Q7 as a lower growth input and a shown-decline case, not ignored.
- **VERDICT: IN**, narrow. The deciding brand tests (share against the store brand, price against volume) are answered
  only indirectly, by the margin comparison; that gap is recorded in the last section.

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **The capital the business needs** **[M2010-090]**: "we’re defining it in terms of the capital actually needed in the
  business. Whether it’s a good investment for us depends on how much we pay for that in the end." At 2026-03-31 the
  operating assets net of operating liabilities were about $400M (receivables 191.9, inventories 159.1, prepaid 16.6,
  PP&E 121.7, lease assets 49.6, other 10.9, less payables 22.8, other accrued 73.0, lease liabilities 48.6, other 5.6;
  10-K FY2026 balance sheet). Against FY2026 operating income of $309.4M that is a pre-tax return above 70% on the
  tangible capital: the brands themselves need almost nothing. Capital spending ran $7.8M to $22.2M a year over FY2017 to
  FY2026 (about 1% of revenue), roughly equal to depreciation (D&A $31.3M less amortization $17.9M = $13.4M in FY2026).
  The filer gives no maintenance figure; the shareholders "are entitled to my best guess" **[M2000-144]** and mine, from
  these figures, is that capital spending about equal to depreciation keeps the plants and the brands in place, with
  advertising (13.7% of revenue in FY2026) expensed in the income account.
- **The capital the owner paid** **[M2011-060]**: "In terms of evaluating the job we’re doing in allocating capital, you
  have to include goodwill, because we paid for it." Equity plus debt less cash at 2026-03-31 was $2,817.6M; pre-tax
  unlevered owner cash FY2026 (owner cash + interest paid + income taxes paid = 235.6 + 43.8 + 45.9) was $325.3M, 11.5%
  pre-tax on the book capital; adding back the ~$716M of brand capital written off since FY2018 (paid, then impaired)
  the capital paid is about $3.5B and the return about 9.2% pre-tax, 7.6% after tax (unlevered after-tax owner cash $268.4M).
- **What the added capital earned** **[M2001-019]**: "whether that’s good or bad depends on what we earn on that
  incremental $130 million over time". From FY2011 to FY2026 pre-tax unlevered owner cash rose from $111.8M to $325.3M
  (+$213.5M) while net acquisitions took $2,682.7M (Step 0 table): **about 8.0% pre-tax, 6.4% after tax**, and that is an
  upper bound, since fifteen years of organic growth on the FY2011 base are inside the increase. The capital is not
  compulsory to stand still (organic revenue has grown about 1.3% a year without it); it is the "optional outlays, aimed
  at business growth, that management expects will produce more than a dollar of value for each dollar spent"
  **[L1999-024]**. At 6.4% after tax against a 5.66% long bond, it about pays its way and no more. The 2026 purchases are
  priced the same way: Breathe Right $1,045M for "~$95 million of EBITDA" (9.1% pre-tax before any capital need, on the
  seller's figure) and LaCorium about $150M for "approximately $12 million in EBITDA including the benefits from
  anticipated synergies" (8.0%).
- **The growth arithmetic.** Earnings have grown because capital was added, not because the return on it rose: "We just
  put way more capital into the business" **[M2023-081]**. The rows' summary fits PBH's own brands exactly: "Most of the
  great businesses generate lots of money. They do not generate lots of opportunities to earn high returns on incremental
  capital." **[M2003-120]**; PBH's answer has been to buy other people's brands at full prices.
- **WEIGHS AGAINST.** The brands are a capital-light business; the company that owns them reinvests every dollar in
  purchases earning about 8% pre-tax, short of "decent returns on the incremental sums they invest" **[L2009-012]** by the
  measure the floor of this framework sets, and the record of impairments says some purchases earned far less.

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends** **[M2025-032]** ("balance sheets over an 8 or 10 year period before I even
  look at the income account"), from `tools/run.py` (first-filed XBRL) checked against the FY2026 filed balance sheet;
  six of the ten year-ends shown, all ten in `run_py_output.txt`; USD millions:

| Mar 31 | assets | goodwill | intangibles | LT debt | equity | retained | cash | receivables | inventory |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | 3,911 | 615 | 2,904 | 2,194 | 823 | 397 | 42 | 137 | 116 |
| 2019 | 3,441 | 579 | 2,507 | 1,799 | 1,096 | 702 | 28 | 149 | 120 |
| 2021 | 3,429 | 578 | 2,476 | 1,480 | 1,358 | 1,009 | 32 | 115 | 115 |
| 2023 | 3,354 | 528 | 2,342 | 1,346 | 1,447 | 1,132 | 58 | 167 | 162 |
| 2025 | 3,402 | 527 | 2,295 | 992 | 1,835 | 1,556 | 98 | 194 | 148 |
| 2026 | 3,494 | 581 | 2,300 | 994 | 1,888 | 1,746 | 64 | 192 | 159 |

  What moved and why: (1) goodwill and intangibles were 90% of assets in FY2017 and 82% in FY2026; tangible equity was
  negative throughout (FY2017 -$2,696M, FY2026 -$993M), so book value is purchase prices less write-downs, nothing more.
  (2) Intangibles fell $604M over nine years although the Akorn eye-care brands and other rights were bought in that
  time: impairments (FY2018, FY2019, FY2023), amortization and divestitures took more than was added. (3) Debt fell from $2,194M to $994M,
  about $1.2B repaid from owner cash in nine years; then $1,045M was borrowed again in June 2026 and $95M in July (10-Q).
  (4) Retained earnings rose $1,349M; $232M of it is the FY2018 non-cash deferred-tax remeasurement (income tax benefit
  of $232.5M in FY2018), and it is after about $716M of impairments. (5) Receivables rose from 15.5% to 17.6% of revenue
  and inventory from 13.2% to 14.6%; the FY2026 MD&A attributes part of the G&A increase to "an increase in our allowance
  for doubtful accounts pertaining to one specific customer", and a $10.3M supplier loan was written off. Neither is out
  of line enough to read as the tell of **[M1995-064]**, "inventories look out of line, you know, with sales". (6) The
  deferred tax liability grew to $447.4M: the tax amortization of brands that are not amortized in the books. What the
  figures cannot say: what the brands are worth. The impairment tests use management's own projections and discount rates
  (critical estimates), and the FY2023 write-downs were attributed "primarily" to a higher discount rate rather than to sales.
- **The real costs.** Stock pay of $10.8M to $14.0M a year is deducted (owner cash is after it): the earnings the rows
  accept are "a figure calculated after interest, taxes, depreciation, amortization and all forms of compensation"
  **[L2021-003]**. Amortization ($17.9M FY2026) is of brands and customer relationships; "Some truly deplete over time
  while others never lose value." **[L2012-003]**; the capex basis is used, so the question does not change the figure.
  Impairments and deal costs: to tell owners year after year to ignore charges "when management is simply making business
  adjustments that are necessary, is misleading" **[L2016-007]**. PBH's Adjusted EBITDA and Adjusted EPS exclude "trade name
  impairment" and "integration, transition, purchase accounting, legal and various other costs associated with
  acquisitions and divestitures" (DEF 14A definition), in a company whose strategy is acquisitions. These costs recur.
- **EBITDA in the filer's own mouth.** The Breathe Right purchase was presented on "~$95 million of EBITDA" and a "45%+
  EBITDA Margin" (Ex 99.1, `0001104659-26-032332`); LaCorium on "$12 million in EBITDA including the benefits from
  anticipated synergies" (Ex 99.1, `0001295947-26-000013`); leverage and covenants are stated on EBITDA; annual and
  long-term pay is half on Adjusted EBITDA. The rows: "where people are talking about EBITDA, is going to be about zero"
  **[M2002-026]**; "I’m talking about regular pretax earnings." and "But it works for the people that sell businesses."
  **[M2012-034]**; "we do not think so-called EBITDA (earnings before interest, taxes, depreciation and amortization) is a
  meaningful measure of performance" **[R1996-023]**. PBH's EBITDA does little harm to the arithmetic of the business itself
  (capex is about 1% of revenue), but it is the measure on which the company buys, borrows and pays itself.
- **The make-the-numbers habit and the tells.** Adjusted EPS heads every release read (FY2013 to Q1 FY2027): "a management
  that regularly attempts to wave away very real costs by highlighting" **[L2016-006]** adjusted earnings is one tell. A
  habit of making declared targets is not shown: the initial organic outlooks were 1% to 2% for FY2024 (actual 0.2%),
  about 1% for FY2025 (actual 1.2%) and about 2% for FY2026 (actual -4.5%) (Q4 releases `0001295947-23-000014`,
  `-24-000015`, `-25-000014`, `-26-000013`); the rows' worry is the manager who will "consistently reach their declared
  targets" **[L2002-041]**, and PBH does not. So there is one tell, not two, and under the framework's two-tell line (Q4,
  a CONVENTION) this is a weighing, not suspicion.
- **Confusion?** No. The accounts are plain: finished goods bought and sold, brands carried at cost less write-downs,
  fixed-rate notes and a term loan, and each year's change explained in the filer's own words. Its preoccupation with
  adjusted measures is a negative, but "we can’t afford to use it as a total exclusionary factor" **[M1994-018]**.
- **VERDICT on confusion: IN. WEIGHS AGAINST** otherwise: EBITDA as the language of buying and pay, adjusted earnings
  that exclude the recurring costs of the strategy, and owner cash that includes a tax shield ($14M to $23M a year) that
  lasts only as long as purchases keep coming. The recast figure carried to Q7 is owner cash after interest, taxes, stock
  pay and capital spending, with the interest added back (after tax at 25%) to put every year on an all-equity basis.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Ronald M. Lombardi, 62, CEO since 2015 (CFO before), Chair of the Board since May 2017; CFO and COO Christine
  Sacco (DEF 14A `0001295947-26-000021`). This is a marketable stock, so the reading is of documents, not of people met:
  "We read annual reports." **[M2007-081]**.
- **The two yardsticks** **[M1994-008]**. Running the business against "the hand they were dealt": the hand was a set of
  brands bought from owners who neglected them; under this management organic growth averaged about 1.3% a year, gross
  margin held between 54.7% and 58.0%, debt was halved, and the eye-care supply failed for three years (FY2024 to FY2026)
  before the company bought the supplier (Pillar5, December 2025). Its own purchases were impaired: Fleet (bought FY2017,
  written down FY2019), TheraTears (bought FY2022, written down FY2023). Treatment of owners, read in the proxy, "see how
  they treat themselves versus how they treat the shareholders" **[M1994-009]**: CEO pay $5.76M, $6.19M and $6.00M for
  FY2024 to FY2026 (Summary Compensation Table), salary $1.0M; performance units paid at 70% of target for FY2024 to FY2026
  although both measures missed (95% of the sales target, 92% of the EBITDA target); compensation actually paid to the
  CEO in FY2026 $0.83M as the stock fell. The CEO owns 376,501 shares (about $17M at the price); all directors and
  officers 1.5%. Corporate housing $35,274. Nothing here is self-dealing.
- **Integrity, applied on doubt** **[M2013-088]**. Tells searched: restatements (none found in the 10-Ks read); legal
  proceedings (Item 3 routine; a discontinued talc product named in "a small number of lawsuits", most dismissed);
  related-party transactions (none disclosed); reports that dance around the key figure, against the test of
  "whether the management is telling us about the things that we would want to know about if we owned a hundred percent of
  the company" **[M1998-036]**: the 10-K discloses the Monistat impairment margin, the Clear Eyes shortage, the supplier
  concentration and the loan write-off plainly. One absence: the words "mistake", "we were wrong" and "error in judgment"
  appear in none of the FY2013 to Q1 FY2027 releases, the FY2026 10-K or the proxy (text search); impairments are
  explained by discount rates and by "reassessment of the long-term sales projections". "That taboo, implying managerial
  perfection, always made me nervous" **[L2024-003]** weighs a little; it is not a tell of dishonesty. No doubt about
  honesty is found, so "we wouldn’t hire anybody, no matter how able, if we didn’t trust them" **[M2015-047]** is not engaged.
- **Love of the business.** Not readable from documents beyond the CEO's own shareholding; "do they love the business or
  do they love the money?" **[M2000-098]** is left unknown, and the pay design (Q6) points toward the deal.
- **Ability.** The rows rank the business first, "And we still look to the underlying business, though." **[M1996-037]**,
  and name the danger: "the number one risk factor is that this business gets the wrong management" **[M2021-042]**. For a
  roll-up the manager's skill is the buying. The fifteen-year record of purchases earned about 8% pre-tax with several
  large write-downs (Q3), and the largest purchase in the company's history was agreed at the end of a three-year
  stretch of supply failure in its own eye-care line.
- **VERDICT on integrity: IN** (no tell found, on doubt). **Ability WEIGHS AGAINST**, narrowly: an honest, competent
  operator of brands whose capital record, which is the job in this company, is ordinary.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
"What do we do with the money, as it comes in?" **[M2001-111]**. PBH has never paid a dividend (10-K FY2026, Item 5), so
every dollar is retained and deployed into purchases, debt repayment and buybacks.

**Part A, the money.**
- **The retention test** **[R1995-009]**, "at least $1 of market value for each $1 retained", on five-year windows
  (March closes from the aggregator, monthly bars, flagged; shares from each 10-K cover: 50,284,147 (FY2011), 52,759,363
  (FY2016), 49,910,894 (FY2021), 47,374,522 today; buybacks added back as cash returned; retained = net income, there
  being no dividends):

| window | market value, start to end | change + buybacks | net income retained | per $1 retained |
|---|---|---|---|---|
| FY2012-FY2016 | $578M to $2,817M | +$2,239M | $354M | **$6.33** |
| FY2017-FY2021 | $2,817M to $2,200M | -$498M | $680M | **-$0.73** |
| FY2022-FY2026, to March 2026 | $2,200M to $2,805M | +$888M | $737M | **$1.20** |
| FY2022-FY2026, to today | $2,200M to $2,161M | +$244M | $737M | **$0.33** |
| FY2012 to today | $578M to $2,161M | +$1,984M | $1,771M | **$1.12** |

  The early window carries the GSK and Insight purchases and a rerating; the middle window, the Fleet purchase, fails;
  the last passes or fails with the quote. Over fifteen years the market has given back about $1.12 per dollar kept,
  while the company ended the span (after June 2026) with about $2.1B of net debt. "if after three or four years,
  you’ve found that the dollars we’ve retained hasn’t created more of that in value, then the presumption becomes very
  strong" **[M1998-110]**: the presumption is neither strong nor cleared here. The form of the test that compares book
  value with the S&P and asks whether "every $1 of retained earnings was always worth more than $1" **[R2009-002]** was not
  run (no S&P series from a primary source in this folder).
- **Buybacks.** An authorization of up to $300.0M (May 2024) names no price: "repurchase announcements almost never
  refer to a price above which repurchases will be eschewed" **[L2016-002]**. FY2026: treasury stock rose 2,391 thousand
  shares for $162.1M, about $67.80 a share including shares withheld for tax (equity statement); March 2026 purchases at
  $60.49 (Item 5). Read by the framework's convention against the Q7 range: the range bottom at the long rate is $69.32
  a share (Q7), so the FY2026 buying sat at or just below that bottom and is read by what it did; against the floor, the
  fair price is $47.74 (Q7), and the same buying was about 40% above it. In the same months the board signed a $1.045B
  purchase financed wholly with new debt. A buyback needs "funds -- cash plus sensible borrowing capacity -- beyond the
  near-term needs of the business" and a price "below its intrinsic value, conservatively-calculated" **[L1999-023]**;
  buying stock in March 2026 and borrowing $1.045B in June meets the first condition only because the debt was available.
- **Deals.** All cash and debt; no stock issued, so the one STOP of Part A (an all-stock deal by an undervalued acquirer)
  does not arise. Value given against value got: "If we give 200 million of cash for a business that’s worth a 150
  million, we are worse off." **[M1995-001]**. The record: about $2.9B paid since FY2012, about $716M written off, an
  incremental return of about 8% pre-tax (Q3). The new purchases are at about 11 and 12.5 times the stated EBITDA, the
  smaller one "including the benefits from anticipated synergies": "we never count on synergies when we acquire
  companies" **[L2016-008]**. The March 2026 release calls the Breathe Right purchase "immediately accretive", and "even a
  high-priced deal will usually boost per-share earnings if it is debt-financed" **[L2017-004]**. No post mortem against
  the original projections is published: "Post mortems of acquisitions, in which reality is honestly compared to the
  original projections, are rare in American boardrooms." **[L2014-013]**.
- **Part A WEIGHS AGAINST**: a retention record that passes over fifteen years only narrowly and fails in two of its
  windows at today's price, a price-blind buyback programme run in the same months as the largest debt-financed purchase
  in the company's history, and deals priced on EBITDA and synergies.

**Part B, the pay, the board and the owners.**
- **Pay tied to what the person controls, and to the capital used.** The annual plan pays on Net Sales (50%) and
  Adjusted AIP EBITDA (50%); performance units (75% of the CEO's long-term award) on three-year Net Sales and Adjusted
  EBITDA (DEF 14A). Neither measure charges for capital, and both rise when a brand is bought with borrowed money. The
  rows "charge managers a high rate for incremental capital they employ" **[L1994-019]**, because "a batting average that
  does not include a cost of capital is a phony batting average" **[M1995-010]**, and "you get what you reward for"
  **[M2016-083]**. This is the strongest single fact of the run against the owners' interest: the plan pays for the
  Breathe Right purchase whatever it earns on $1.045B.
- **Peer data and the ratchet.** Salaries for FY2027 were raised "to move each closer to the median of the peer group"
  (DEF 14A): "comp committees have become slaves to comparative data" **[L2005-015]**; "there’s a ratcheting effect that
  takes place" **[M2004-017]**.
- **The board.** Six of seven directors independent and a lead independent director, but the CEO has also been Chair
  since 2017: "how hard it is to replace a mediocre CEO if that person is also Chairman" **[L2014-026]**.
- **The owners as partners.** Annual guidance on revenue, organic growth, adjusted EPS and free cash flow, restated each
  quarter (every release read): "forecasting earnings, I can’t imagine anything more destructive" **[M2022-054]**; "the
  scourge of earnings" **[L2019-006]** guidance. The proxy's pay discussion runs about thirty pages, short of the hundred
  that would mark "something is wrong" **[M2009-087]**.
- **Part B WEIGHS AGAINST**: pay on sales and EBITDA with no capital charge in a company whose growth is bought, peer
  benchmarking, a combined Chair and CEO, and guidance.

**Q6 WEIGHS AGAINST** in both parts.

## Q7: WHAT IS IT WORTH? STOP.
The three questions, "How certain are you that there are indeed birds in the bush? When will they emerge and how many
will there be? What is the risk-free interest rate (which we consider to be the yield on long-term U.S. bonds)?"
**[L2000-021]**, answered as a range: "working with a range of possibilities is the better approach" **[L2000-024]**.
Arithmetic in `q7_calc.py`, output in `q7_calc_output.txt`.

- **The cash input** (the framework's CONVENTION: five-year average of owner cash after every real cost). Because the
  capital structure changed after the window (net debt from about $0.9B at 2026-03-31 to about $2.1B in July 2026), each
  year's owner cash is put on an all-equity basis by adding back interest paid after tax at 25%, and the net debt is
  subtracted at the end. **CONVENTION of this run**, rationale: the five-year average of after-interest owner cash would
  carry the old, smaller interest bill against the new, larger debt; the rows value a purchase "on an all-equity basis"
  **[L2017-004]**. Unlevered after-tax owner cash: FY2022 287.2, FY2023 250.2, FY2024 272.8, FY2025 267.9, FY2026 268.4;
  **average $269.3M**. Pre-tax (owner cash + interest paid + income taxes paid): 349.2, 304.4, 348.2, 332.0, 325.3;
  average $331.8M.
- **The purchases after the window.** Added at the stated EBITDA less tax at 25% and no capital spending: Breathe Right
  $95M (the seller's twelve months to December 2025, from the deal presentation, not an audited figure) and LaCorium
  $12M ("including the benefits from anticipated synergies"), together $80.3M after tax, $107.0M pre-tax. **CONVENTION of
  this run**, rationale: the businesses are owned and their debt is counted, so leaving them out would value the debt
  and not the asset; their figures are the seller's and management's, so two stress variants are shown below. No capital
  spending is assumed because the acquired brands come with contract-manufacturing agreements and no plants (10-Q Note 2).
  **Pro forma base: $349.6M after tax, $438.8M pre-tax, unlevered.**
- **Net debt:** face debt $2,045.0M at 2026-06-30 plus $95.0M borrowed 2026-07-01 = $2,140.0M; cash $89.1M less about
  $55.0M paid for LaCorium from cash = $34.1M; finance-lease liabilities $20.6M (2026-03-31); **net $2,126.5M** (10-Q
  `0001295947-26-000042`; the July note exchange of $400M for $400M is neutral). Shares 47,374,522.
- **The growth input.** Shown on aggregate unlevered owner cash, FY2022 to FY2026: **-1.68% a year**. The window begins on
  a year the filer calls a recovery from COVID-depressed categories (organic +10.1%, FY2022) and ends on a year cut by
  the Clear Eyes shortage (organic -4.5%, FY2026), so a **whole-cycle variant** is shown with the top end at the filer's
  own organic revenue growth over FY2016 to FY2026, **+1.30% a year** (geometric mean of the eleven figures at Q2; a
  CONVENTION of this run, rationale: both ends of the five-year window are abnormal years named as such by the filer, and
  organic revenue is the longest record of the brands' own growth). No case is carried above the growth shown in the
  record, and none past the discount rate **[M1997-095]**.
- **The range at the long government rate, 5.66%** (ten years at the growth input, then zero nominal growth, discounted
  throughout; equity = value less net debt; per share):

| case | growth | enterprise value | equity | per share |
|---|---|---|---|---|
| shown decline (bottom) | -1.68% | $5,410M | $3,284M | **$69.32** |
| no growth (top of the five-year range) | 0.00% | $6,176M | $4,050M | **$85.48** |
| whole-cycle variant (top) | +1.30% | $6,848M | $4,721M | **$99.65** |
| stress: purchased brands worth nothing, their debt counted | -1.68% to +1.30% | | | $43.10 to $66.47 |
| stress: purchased brands worth exactly what was paid | -1.68% to +1.30% | | | $68.32 to $91.70 |

  Width: top over bottom 1.23 (five-year) and 1.44 (whole-cycle), far inside the framework's three-to-one line, so the
  range is narrow enough to decide on, not TOO HARD.
- **The floor** (the framework's CONVENTION: about ten percent pre-tax on the price paid, as the speakers stated and
  qualified it: "we don’t want to buy equities where our real expectancy is below 10 percent" and "And it’s arbitrary."
  **[M2003-149]**; "at least 10% pre-tax returns" **[L2002-020]**; a figure "we are guessing at our future opportunity cost"
  **[M2003-151]** and that cheap money moves "a little" **[M2016-078]**). Applied on the all-equity basis, the price paid
  being the market value plus the net debt the buyer of the whole would assume ($2,160.8M + $2,126.5M = **$4,287.3M**):

| case | expected pre-tax return at $45.61, all-equity basis |
|---|---|
| shown decline | **9.11%** |
| no growth | **10.24%** |
| whole-cycle variant | **11.15%** |

- **Reading the two together.** The price, $45.61, is 34% below the bottom of the per-share range, but the per-share
  discount is magnified by $2.1B of debt standing ahead of the equity; on the whole business the price is 21% below the
  bottom of the range and 31% below its no-growth value. The rows ask for "a big discount from that present value
  calculated using the risk-free interest rate" **[M1997-126]**, and a larger one as the business is less certain: "the
  more volatile the business is [...] the larger the margin of safety" **[M1997-080]**. Here the moat is narrow and partly
  eroding (Q2), the purchases have earned about 8% (Q3), and supply and retailer concentration are live (contrary
  evidence 1 to 3). The floor states the same thing in one number: at this price the business is expected to earn about
  10% pre-tax in the central case, 9% if the five-year decline continues, 11% if the long organic record resumes. That is
  a calculation to tenths of a percent, the case the rows tell us to leave: "forget about the whole exercise"
  **[M2009-005]**; "it’s too close to think about" **[M1996-084]**. On the levered basis the equity's expected return is higher, but only because the lenders stand
  first; the rows evaluate "on an all-equity basis" **[L2017-004]**.
- **VERDICT: OUT.** Valued, narrow range, price well below the range at the long rate, but the expected return on the
  whole business at the price sits on the ten-percent floor in the central case and below it in the shown-decline case:
  not a screamer, a pencil case, quit on under the framework's floor **[M2003-149]**, **[M2009-005]**.

**Reporting at the owner's request (not a rule change). COMPUTATION, NOT A CLEARANCE** (the file closed OUT at Q7):
- **(a) VALUE RANGE:** **$69.32 to $85.48 a share** (five-year convention, shown decline to no growth, at 5.66%);
  **whole-cycle variant $69.32 to $99.65** (top end at the FY2016 to FY2026 organic rate, because both ends of the
  five-year window are abnormal years). Against the price of $45.61.
- **(b) FAIR PRICE: $47.74 a share.** The price at or below which the central case (no growth, pro forma pre-tax
  unlevered owner cash of $438.8M) earns 10% pre-tax on the whole business (enterprise value $4,388M less net debt
  $2,126.5M). Tax treatment: "pre-tax" means before income tax and before interest (owner cash plus interest paid plus
  income taxes paid, as in the five-year table), measured on market value plus net debt; at a 25% tax rate the
  after-tax equivalent is about 7.5%. The same test in the shown-decline case gives $37.87; in the whole-cycle case $56.32.
  The price is about 4% below the central fair price.
- **(c) CHEAP PRICE: $16.86 a share.** Rule (CONVENTION of this run): the price at which the central case earns 15% pre-tax
  on the whole business, one and a half times the floor, so that owner cash could fall by a third and the purchase would
  still clear the floor; that is the margin at which no pencil is needed. In the shown-decline case the same rule gives
  $11.21. The cheap price is so far below the fair price because $2.1B of debt takes the first $2.1B of any value: a
  margin of a third on the business is a margin of about two thirds on this equity.

## Q8: IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (closed OUT at Q7).

## Q9: COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED as a question (closed OUT at Q7). The debt facts are recorded because the balance-sheet reading needs them.
**COMPUTATION, NOT A CLEARANCE.** After the June and July 2026 borrowings: $600M 3.750% notes due April 2031; a $1,140M
term loan at Term SOFR plus 2.00% due June 2033, floating, secured by "substantially all" of the borrower's and guarantors'
assets, amortizing 0.25% a quarter, with an excess-cash-flow sweep from FY2028 if first-lien net leverage exceeds 2.75
times; $400M 6.250% notes due July 2034 (replacing the 5.125% notes due January 2028); a $225M asset-based revolver to
June 2031, undrawn, $193.5M available at June 30 (8-Ks `0001104659-26-074259`, `0001295947-26-000029`,
`0001104659-26-083872`; 10-Q Note 8). Net debt $2,126.5M is 4.8 times the pro forma pre-tax unlevered owner cash of
$438.8M; the company's own figure is "~4" times bank-defined EBITDA. No maturity of size before 2031, so "no significant
near-term cash requirements" **[L2014-023]** is met for five years; the 2031 to 2034 maturities assume refinancing, and
"maturities must actually be met by payment" **[L2010-020]** in a bad market. As a whole business offered for purchase it
would fail the "little or no debt" criterion **[R1997-001]**; that STOP is stated for whole businesses and is not applied
to a market purchase here. The debt is what turns a narrow-moat business into a thin equity: risk "from the capital
structure when somebody sticks a ton of debt into some business" **[M1997-009]**.

## Q10: IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED (closed OUT at Q7).

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (closed OUT at Q7). For the record only: remedies for minor ailments sold under their own names; none of the
named businesses of Q12.

---
## THE BOX
**OUT, at Q7.** The castle stands, narrowly (Q2 IN), the accounts are plain (Q4 IN) and no integrity tell was found (Q5
IN); the capital record, the pay design and the uses of cash all weigh against (Q3, Q6). Valued on an all-equity basis
the business is expected to earn about 10% pre-tax at the price in the central case and 9% if its five-year decline
continues: a pencil case on the floor, not a screamer. **Value range $69.32 to $85.48 a share (whole-cycle variant to
$99.65), fair price $47.74, cheap price $16.86, against a price of $45.61.** Not TOO HARD: no research pass is opened.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy and the research folder were made before `tools/run.py` ran).
      **Not met in full:** the file was written in three stages (Step 0 to Q2, Q3 to Q6, Q7 to the end) rather than
      question by question, and nothing was committed, because this session's instruction forbids commits.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, below); every filing fact carries its
      accession or names the filing; numbers not from a row or a filing are labelled CONVENTION (the framework's or this
      run's) or flagged as aggregator data (the price, the March closes used in the retention test).
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8, Q10 and Q12 are NOT REACHED and the
      Q9 facts are headed as computation; the fair and cheap prices are headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost (OCF less stock pay less capital spending, as filed), never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury; aggregator quotes flagged. Net income is used once, as the
      measure of earnings retained in the retention test, which is what that test retains.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the nine items under the foundations).
- [x] No row dated after the anchor is cited in a point-in-time run: not a point-in-time run (today's run).
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its owner-earnings mean (3-year) was not used; the
      five-year table here is recomputed from the filed figures.
- [x] `python tools/check_framework.py` PASS before finishing (result recorded in the reply; no commit made).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q4 and EBITDA talk.** Q4's "What it rules OUT" lists "EBITDA as earnings and managements that talk it" and the text
under "Why confusion is a STOP" says "On EBITDA talk the stop is stated as a count", citing the row on EBITDA talk; yet Q4's heading
confines the STOP to confusion or suspicion and the two-tell convention makes suspicion need two tells. PBH talks EBITDA
when it buys, borrows and pays itself, but its accounts are not confusing; I treated the EBITDA talk as a heavy weighing,
not a STOP. Had it been read as a STOP the file would have closed OUT at Q4 instead of Q7. (2) **Q7 and a capital
structure that changed after the window.** The range convention averages five years of owner cash, which is after
interest; PBH doubled its debt for a $1,045M purchase ten weeks after the window closed. The convention says nothing on
this; I put every year on an all-equity basis, added the purchased businesses at their stated EBITDA and subtracted the
net debt, and showed two stress variants. Two analysts could easily do it differently. (3) **The floor's basis.** The
floor is "about ten percent pre-tax on the price paid", but the framework does not say whether the price paid is the
equity's or the enterprise's. On the equity at $45.61 the expected return is well above 10% because of the leverage; on
the enterprise it is about 10%. I used the enterprise, following **[L2017-004]** and Q9's test 2, and the verdict depends
on that choice. (4) **The range and the floor can disagree.** The template says Q7 closes IN "only if the price is so far
below [the range] that no pencil is needed", and a price 34% below the bottom of a range discounted at 5.66% sounds like
that; yet the same price meets the 10% pre-tax floor only to a tenth of a point. The range at the long rate and the floor
are two different hurdles; the framework should say which governs when they conflict (here I let the floor govern,
because the framework's own convention says a candidate at or below the floor is quit on). The same conflict reaches Q6:
the buyback convention reads repurchases against the bottom of the Q7 range, which here sits above the floor's fair
price, so PBH's FY2026 buybacks pass one test and fail the other. (5) **Q2's brand tests with no data.** Share against
the store brand and price against volume are the deciding brand tests, and the filer stopped disclosing shares after
FY2016 and never splits price from volume. The framework sends an unknowable castle to TOO HARD and an unresearched one
to the research pass, but gives no rule for a castle answered only indirectly (here, by fifteen years of gross margins
against the store-brand maker's). I closed Q2 IN on the indirect evidence and said so; another analyst could reasonably
have closed it TOO HARD (WORK). (6) **The roll-up.** Q1's "understood by its parts" is written for holding companies; a
brand roll-up's future depends on purchases not yet made, which no question owns except Q6's weighing. The framework
could say whether expected future deals are part of what must be understood at Q1. (7) The contamination note: the
blind list does not cover commit subjects of other companies' runs visible in the session context, one of which concerned
a branded-consumer name closed at Q2 on retailer power, the very test this run turned on.
