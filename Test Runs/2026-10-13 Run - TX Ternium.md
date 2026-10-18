# Company Run — Ternium S.A. (NYSE: TX, ADSs only; 1 ADS = 10 ordinary shares) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
a5209c30, "TX run: template copied, research folder opened").

**Dispatched blind run.** The brief is the canonical brief with three stated departures (lines of evidence derived by the
analyst from the filing; competitors are the rivals the 20-F names; the 20-F's Items 4, 3.D and 5 stand in for the 10-K's
Items 1, 1A and 7). Working folder: `Test Runs/_research 2026-10-13 TX/` (raw filings under its gitignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled at the fold by the dispatching session (overnight 2026-10-13, after the run was committed): not held (`PORTFOLIO.md` carries no line for TX or Ternium).

**CONTAMINATION, declared as found and not used.** (1) The session's opening git status and recent commit subjects showed
another company's run (CMC, a steel producer) closed OUT at Q2 on a commodity-castle reading, with research folders of two
other names (AYI, ARCB). I read none of those files. Because CMC is a steel producer, the risk that its subject line primed my
Q2 reading is real; I declare it, and Q2 below is argued from Ternium's and its named rivals' filings only. (2) To confirm my
own file did not already exist I listed `Test Runs/` filtered for "TX" or "ternium"; that listing returned file names of
other companies' runs (TXN Texas Instruments, MATX Matson, TXRH Texas Roadhouse) and no Ternium file. A filtered listing is
a search across `Test Runs/` under the brief's rule; I declare it. No file was opened. (3) The project map and memory index
loaded with the session carry queue counts and wave names; none names Ternium, and none was used. (4) `.gitignore`, read to
place raw filings correctly, names other runs (SNPS, MGM, DELL) in its comments; not used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $58.99 per ADS = $5.899 per share (close 2026-10-13; Yahoo Finance chart API through `tools/sources.py`;
  **aggregator, flagged per operator rule 5, live quote only**). Closes of the prior week: $56.97 to $58.18.
- **Shares by class** from the latest filing's cover: 2,004,743,442 ordinary shares issued, a single class
  (`python Screens/cover_shares.py TX`: 20-F filed 2026-03-31, period 2025-12-31, accession 0001342874-26-000020).
  **Checked against issued less treasury:** the 20-F (Item 5, note (2) to the income table; Item 7.A) records 41,666,666
  treasury shares "repurchased from Usiminas on February 15, 2011", so **1,963,076,776 shares outstanding**, the figure
  the 2026 half-year statements also use as the weighted average for H1 2026 (6-K filed 2026-08-05, accession
  0001342874-26-000046). No issuance or repurchase in any 6-K read since (Item 16E: "There were no purchases ... during
  2025"). ADS-equivalent count: 196,307,678.
- **Market cap:** 1,963.08M shares × $5.899 = **$11,580M**.
- **Sovereign for the earnings currency:** Ternium reports in US dollars and its main operating subsidiaries (Ternium
  Mexico, Ternium Argentina, Ternium Brasil, Ternium Colombia, Tenigal; Usiminas from 2026-01-01) use the US dollar as
  functional currency (20-F Item 5, Overview). Owner earnings are taken in **USD**. **US Treasury daily par yield curve,
  30-year: 5.60%, dated 2026-10-09** (`python tools/sources.py`; the issuing authority; 2026-10-12 was a bond-market holiday).
- **Filings read** (operator rule 4):
  - 20-F for FY2025, filed 2026-03-31, accession **0001342874-26-000020**: Items 3.D, 4 (A, B, C), 5 (A, B, E), 6.B, 7,
    8.A, 16E, and notes 5, 25 and 32 of the financial statements, the cash flow statement (F-12).
  - 6-K, 2026 half-year consolidated condensed interim financial statements, filed 2026-08-05, accession
    **0001342874-26-000046** (balance sheet at 2026-06-30, H1 income and cash flows, notes 10, 11, 12).
  - 6-K, Q2 2026 results press release, filed 2026-08-04, accession 0001342874-26-000044 (headline figures only).
  - 6-K, revision of the 2025 dividend proposal, filed 2026-04-15, accession 0001342874-26-000025.
  - 6-Ks of 2026-07-08, accessions 0001554855-26-001509 and 0001554855-26-001510 (Sustainability Report 2025 release).
  - Prior 20-Fs for the cycle: FY2023 (accession 0001342874-24-000018; cash flow statement 2021 to 2023), FY2020
    (0001342874-21-000031; cash flow statement 2018 to 2020), FY2017 (0001342874-18-000009; selected data 2013 to 2017).
    The FY2021 20-F (0001342874-22-000023) was fetched and not read beyond what the later filings restate.
  - **Not read:** the annual-meeting documents of 2026-03-20 (accessions 0001342874-26-000011, -000013, -000015) and
    the analyst-day 6-K of 2026-10-08 (0001342874-26-000048). The file closed at Q2 before the questions they serve
    (see the box); they are listed under what I could not get.
  - **One figure cross-checked against the filed statement:** net sales 2025 $15,609M in the 20-F's Item 5 income table
    (and $15,609,094 thousand in note 5) equals the SEC XBRL fact; total assets at 2017-12-31 of $12,122,566 thousand in the
    FY2017 20-F's selected data equals the XBRL value of $12,123M used in the ten-year table. Net cash from operations
    2025 $2,313,625 thousand on the filed cash flow statement equals the XBRL value.
- `python tools/run.py TX`: prints "TX: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." (the tool reads US-GAAP
  tags; Ternium files IFRS). No line of it was used. The ten-year table below was built from the SEC company-facts IFRS
  file (`_research 2026-10-13 TX/xbrl_table.py`, output `xbrl_table.txt`) and checked line by line against the filed
  cash flow statements of the FY2025, FY2023 and FY2020 20-Fs for operating cash, capital expenditure and lease payments.

### The balance sheets, 2016 to 2025, read before the income account **[M2025-032]**
$ million at December 31 (20-F filings; XBRL ifrs-full facts as filed, 2016 from the FY2017 20-F).

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 30 Jun 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total assets | 8,323 | 12,123 | 12,548 | 12,936 | 12,856 | 17,098 | 17,492 | 24,179 | 23,129 | 23,615 | 24,552 |
| Owners' equity | 4,391 | 5,010 | 6,393 | 6,612 | 7,286 | 10,535 | 11,846 | 12,419 | 11,968 | 11,944 | 12,300 |
| Non-controlling interest | 775 | 842 | 1,091 | 1,103 | 1,157 | 1,700 | 1,922 | 4,393 | 4,163 | 4,203 | 4,439 |
| Intangibles and goodwill | 843 | 1,093 | 1,013 | 944 | 909 | 902 | 944 | 996 | 1,022 | 1,002 | 1,037 |
| Cash and equivalents | 183 | 338 | 251 | 520 | 538 | 1,277 | 1,653 | 1,846 | 1,691 | 1,531 | 1,431 |
| Other investments, current | 145 | 133 | 45 | 212 | 814 | 1,290 | 1,875 | 1,976 | 2,160 | 1,600 | 1,301 |
| Borrowings | 1,219 | 3,222 | 2,037 | 2,189 | 1,723 | 1,479 | 1,032 | 2,146 | 2,230 | 2,419 | 2,844 |
| Lease liabilities | - | - | 74 | 339 | 294 | 260 | 239 | 241 | 210 | 187 | 207 |
| Inventories | 1,648 | 2,551 | 2,690 | 2,158 | 2,002 | 3,908 | 3,470 | 4,948 | 4,751 | 4,094 | 4,395 |
| Trade receivables | n/t | 1,011 | 1,133 | 951 | 918 | 1,767 | 1,181 | 2,065 | 1,562 | 1,540 | 2,007 |
| Net sales (year) | 7,224 | 9,700 | 11,455 | 10,193 | 8,735 | 16,091 | 16,414 | 17,610 | 17,649 | 15,609 | H1: n/r |

(n/t: not tagged; n/r: not recorded here.) **What moved and why.** (1) Two steps in size, both acquisitions: 2017, Ternium
Brasil (CSA) bought for cash ($1,891M paid for control, XBRL cash-flow fact), lifting assets by $3.8B and borrowings to
$3.2B; July 2023, Usiminas consolidated after a cash purchase of control-group shares (consideration $118.7M, cash
acquired $781.1M, FY2023 20-F cash flow statement), lifting assets by $6.7B and non-controlling interest from $1.9B to
$4.4B. (2) Owners' equity rose from $4.4B to $11.9B, almost all of it in 2017 to 2022; it was **flat to down from 2023 to
2025** ($12.4B to $11.9B), the years of the Usiminas consolidation, the CSN litigation provision and the deferred-tax
write-down. (3) Goodwill and intangibles are small against equity ($1.0B, of which goodwill $662M from the Mexican
acquisitions, unchanged): the equity is mostly plant, working capital and cash. (4) The balance sheet carried **net cash**
from 2020 to 2025 (cash plus other investments above borrowings plus leases), and the 2025 capital programme ran it down
from $1.4B to $0.5B at year-end and to a net debt of $319M at 2026-06-30. (5) Inventories move with steel prices, not
with sales trend: $3.9B in the 2021 peak, run down by $0.8B in 2025 as prices fell, a working-capital release that flatters
2025 operating cash. (6) A part of the cash is not free: Ternium Argentina's cash and investments of $0.8B sit in the
Argentine financial system, "a large share of which consisted of bond holdings", and dividends out of results before 2025
need central-bank approval "which is seldom, if ever, granted" (20-F Items 3.D and 5). Cash that cannot be moved is, in the
rows' words of off-shore cash, "simply not worth as much as cash held at home" **[L2016-009]**. What the figures
cannot say: the split of profit and capital between Mexico, Brazil and Argentina (the steel segment is reported as one
integrated business; segment assets are "not disclosed as it is not reviewed by the CEO", note 5).

---
## THE FOUNDATIONS (not a gate)
The foundation that bears most here is the one on macro forecasts: Ternium's results turn on steel prices, on US and
Mexican trade measures and on Argentine and Brazilian policy, and the rows keep those forecasts out of the decision,
"macro conclusions are — just never enter into the discussion." **[M2000-094]**; the business is to be judged as a
business, as if "the market closed for five years" **[M1997-109]**. Its currency exposure (Argentine peso securities, a
Brazilian-real debt and provision) is "a bet on how government now, and in the future, will behave" **[M2011-025]**, so it
is weighed as a property of the business, not forecast. **Contrary evidence, written down as found** **[M1997-127]**:
(a) over 2016 to 2022 Ternium's margins equalled or beat those of every named rival read, including Nucor (Q2's competitor
row), which is evidence for a cost position better than the field's; (b) the computation beneath the stop (Q7, after the
box) puts the price well below its no-growth value at the long rate, which pulls toward wanting the castle to stand; I
record both because they cut against the box I reach.

## THE STANDING RULE
Owning a part-interest in Ternium bought with the operator's own money, unlevered, puts no claim on the buyer beyond the price
paid; the rule is breached only by borrowed money or a sizing that could force a sale, "borrowed money has no place in the
investor's tool kit" **[L2014-005]**, "never going to risk what we have and need for what we don't have and don't need"
**[M2012-081]**. Nothing in this run requires either. PASS for the buyer's conduct.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is, from the filing.** A regional flat-steel producer: the Steel segment is $15,041M of $15,609M of
  2025 net sales (96%); Mining (iron ore, mostly consumed internally) is the rest and lost money in 2024 and 2025 (note 5,
  operating income management view: Steel $968M, Mining $(141)M in 2025). Steel shipments 15.06Mt in 2025: Mexico 48% of
  steel product sales, Brazil (Usiminas, consolidated from July 2023) 25%, Southern Region (Argentina) 16%, other markets
  (southern US, Colombia, Central America) 11% (Item 4.B, Net Sales; 20-F 0001342874-26-000020).
- **The key variables and whether they are foreseeable** **[M1998-044]**. (1) The regional steel price: "The prices of our
  steel products generally reflect international market prices for similar products adjusted to reflect regional
  conditions. We adjust prices for our products periodically in response to changes in the import prices of foreign
  steel" (Item 4.B). (2) Input costs: purchased slabs, iron ore (most from Vale), coal, gas, electricity from Techgen (a
  related party). (3) Volume in Mexico, Brazil and Argentina. (4) The trade regime: US Section 232 tariffs raised to 50% in
  2025, the Section 301 investigation of Mexico opened in March 2026, Mexican and Brazilian antidumping duties (Item 3.D).
  The shape of the economics ten years out is foreseeable: a price-taking producer whose spread over imports rises and falls
  with the cycle. The level of the spread at any date is not, and the speakers do not ask for it: "We don’t think we can
  predict commodity prices." **[M2016-025]**.
- **The test as the draft states it.** Understanding means "a reasonable fix on about what the earning power and
  competitive position will look like in five or 10 years" **[M2012-065]**; the product may stay opaque if "I understand
  the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?" **[M2011-014]**.
  Ten years of IFRS statements in US dollars are on file, the cash flows are plain, and the decision can be made "off the
  figures" **[M2008-069]**. By the framework's commodity paragraph, a dependence on a commodity price "is never by itself a
  STOP at Q1 or Q2"; Q1 asks whether the business can be understood from its figures, and it can.
- **Abroad** (test 11). The rows ask whether "we think we understand the nuances of the corporate governance system and
  taxation" **[M2000-141]**, and for an understood business in a less familiar country they ask a lower price rather than a
  pass: "Brazil would not be off limits at all [...] We would want it to be cheaper than if it were in the United States.
  We wouldn’t understand the tax laws as well, the nuances of governance" **[M2006-021]**. The nuances here are named in
  the filing and knowable: a Luxembourg holding company controlled by San Faustin (76.5% with Tenaris), Argentine exchange
  controls on dividends, a Brazilian court that reversed itself on the CSN claim after eleven years. They raise the margin
  asked (carried to Q7); they do not put the economics out of sight.
- **Routing.** Not a fast-changing technology; not a financial institution; not a holding company of unlike parts (the
  Steel segment carries 96% of sales and more than the whole of 2023 to 2025 operating profit, management view, $4,919M of
  $4,621M, the Mining segment netting a loss; the earlier two years are not read by segment; so Steel decides, Q2's
  business-of-parts paragraph).
  Doubt about the circle **[M2002-092]**: I have doubts about the castle, not about what the business is or how it earns;
  those belong to Q2.
- **VERDICT: IN.** The economics of a regional flat-steel price-taker can be foreseen in shape from its figures
  **[M2012-065]**, **[M2008-069]**; the foreign nuances ask a lower price **[M2006-021]**, carried to Q7.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The lines of evidence, and why these** (the brief's departure (1)). From Item 4.B (Net Sales, Marketing, Competition,
Capital Expenditure Program), Item 3.D and Item 5 of the FY2025 20-F I chose: (i) how the filer says its prices are set,
because in a commodity field the castle question becomes the cost question (the framework's commodity paragraph); (ii)
what the filer says of its cost position, by a search of the whole 20-F; (iii) margins and returns over the whole span
against the rivals the 20-F names that file with the SEC, because "The figures are available." **[M2009-059]**; (iv) imports
and trade measures in each home market, because the filer names them as what sets its price and share; (v) the parts the
filer reports, to find which part decides.

- **Pricing power and the agony before a rise** **[M2005-020]**. The filer sets its price off the import price: "We adjust
  prices for our products periodically in response to changes in the import prices of foreign steel, export prices, and
  supply and demand" (Item 4.B). On costs: "we may be unable to recover, in whole or in part, increased costs of raw
  materials and energy through increased selling prices on steel products, or it may take considerable time to do so"
  (Item 3.D). The rows' test is that "over time the businesses with strong competitive positions manage to pass through
  increases in raw material costs" **[M2005-017]**; the filer does not claim it. The rival sets the price: "whatever he
  charged for gas was my price." **[M2012-109]**.
- **The low bid** **[L2004-003]**. "The global market for such steel products is highly competitive, with the primary
  competitive factors being price, cost, product quality and customer service" (Item 5, Overview); in rebar and wire rod,
  "competition is largely based on price" (Item 4.B). The filer's differentiation (service centres, just-in-time delivery,
  automotive grades, the "Ternium Activo" platform) is real but is described as an aim, "We strive to differentiate
  ourselves" (Item 4, Overview); no figure in the filing shows a price premium kept against imports.
- **The attacker with money** **[M2011-015]**. Mexico: "foreign steel producers cover approximately half of the flat steel
  demand in the country" (Item 4.B, Strategy); finished flat imports 8.9, 10.3 and 10.2Mt in 2025, 2024 and 2023 against
  Ternium's 7.4Mt of Mexican shipments in 2025; rivals have built inside Mexico (POSCO's and NUCOR-JFE's galvanizing lines,
  ArcelorMittal's hot-rolling mill, Item 4.B, Competition); and "U.S. tariff measures on Mexico's steel exports have led to
  the diversion of products once destined for the U.S. market into the domestic market, thereby intensifying competitive
  pressures within the country." Brazil: flat imports "surged approximately 40% in 2023, 10% in 2024 and 30% in 2025,
  mainly due to the import of low-priced Chinese steel products" (Item 3.D). Argentina: "Its main competition in the
  Argentine flat steel market are imports, particularly from Brazil", and in 2024 import streamlining "resulted in an
  increase of unfairly traded imports" (Items 4.B, 3.D). The money test is answered yes in the filer's own words: the
  castle is entered by anyone who can ship flat steel into the market, and the barriers the filer names are trade remedies
  and freight, not anything of its own **[M2012-106]**.
- **The low-cost position** **[M1997-010]**, **[L2000-017]**, **[M2006-004]**. **No instance found** in the FY2025 20-F of a
  statement that Ternium is a low-cost producer: a search for "low-cost", "lowest cost", "low cost", "cost position",
  "cost-competitive", "cost competitive" and "competitive cost" returns one hit, a risk that "BRL-denominated costs (mainly
  labor-related costs) may increase, thereby affecting cost-competitiveness" (Item 3.D). The filer's own reading of 2025:
  "Usiminas advanced several projects aimed at improving the cost structure", "the influx of low-priced Chinese steel
  products continued to pressure Usiminas' profitability", and a $405M write-down of Usiminas' deferred tax assets
  "following a recoverability assessment" (Item 5), which is the filer saying it does not expect Usiminas to earn the
  taxable profit to use them. The Mexican unit buys a large part of its slabs and is not yet integrated: the new DRI-EAF
  slab shop was "expected to be completed in the fourth quarter of 2026" (Item 3.D) and is "expected to begin operations in
  early 2027" in the release of 2026-07-08 (accession 0001554855-26-001509). The cost position is therefore read from the
  margins in the competitor row below, as the rows direct: "It’s like comparing a copper producer whose costs are $2.50 a
  pound with a copper producer whose costs are $1 a pound. Those are two different kinds of businesses." **[M2009-059]**.
- **The competitor row** (the rivals the 20-F names, up to three that file with the SEC; same metrics from each filer's own
  SEC XBRL facts as filed; `_research 2026-10-13 TX/compare.py`, output `compare.txt`). Named as Ternium's "largest foreign
  competitors in the flat products market" or as domestic rivals: **Nucor** (10-K FY2025, accession 0001193125-26-071575),
  **ArcelorMittal** (20-F FY2025, 0001243429-26-000020; named in Mexico and Brazil), **Gerdau** (20-F FY2025,
  0001104659-26-027678; named in Brazil, and Gerdau Corsa in Mexican rebar; reports in BRL, so ratios only). Named rivals
  that file with the SEC and were not used: Steel Dynamics, Cleveland-Cliffs, POSCO, CSN (the litigation adversary), and US
  Steel (whether it still files was not checked). **Named rivals that do not file with the SEC, flagged:** Galvasid (Grupo
  LM), Zincacero (Grupo Villacero), TYASA, GASA, Deacero, Prolamsa, Nippon Steel (and the NUCOR-JFE and ArcelorMittal-NSC
  joint ventures as such), Acerías Paz del Río, Diaco, Acerías de Colombia, Siderúrgica Nacional, Siderúrgica del Occidente;
  Grupo Simec's filing status was not checked.

  | Pretax margin, % of sales | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2016-25 avg | 2019-25 avg |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | Ternium | 15.5 | 14.0 | 17.7 | 8.1 | 13.3 | 35.8 | 16.2 | 7.5 | 4.1 | 4.2 | 13.6 | 12.7 |
  | Nucor | 8.0 | 8.6 | 12.9 | 7.9 | 4.2 | 25.2 | 24.7 | 18.1 | 9.4 | 7.9 | 12.7 | 13.9 |
  | ArcelorMittal | 4.8 | 7.3 | 6.6 | -2.7 | 2.0 | 23.5 | 14.1 | 1.8 | 4.7 | 5.9 | 6.8 | 7.0 |
  | Gerdau | -6.9 | -0.1 | 4.7 | 4.2 | 8.0 | 25.9 | 19.2 | 13.6 | 8.2 | 3.6 | 8.0 | 11.8 |

  | Return on owners' equity, % | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2016-25 avg | 2019-25 avg |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|
  | Ternium | 14.2 | 18.8 | 26.4 | 8.7 | 11.2 | 42.9 | 15.8 | 5.6 | -0.4 | 3.6 | 14.7 | 12.5 |
  | Nucor | 10.4 | 15.9 | 25.5 | 12.6 | 6.8 | 55.0 | 46.9 | 23.0 | 9.8 | 8.5 | 21.4 | 23.2 |
  | ArcelorMittal | 6.2 | 13.3 | 12.7 | -6.1 | -1.9 | 34.2 | 18.2 | 1.7 | 2.6 | 6.1 | 8.7 | 7.8 |
  | Gerdau (BRL) | -10.3 | -1.5 | 9.3 | 4.6 | 8.2 | 42.2 | 25.8 | 15.8 | 8.5 | 2.5 | 10.5 | 15.4 |

  (Net income to owners over average owners' equity; the 2016 opening equity for ArcelorMittal and Gerdau is their 2015
  total equity, the owners' figure not being tagged. Ternium's equity carries $2.9B to $4.0B of cash and investments in
  2021 to 2025, which lowers its ROE against an operating-capital measure; its pretax margin is unaffected by that. The
  peers' figures are their XBRL facts; their filed statements were not read, which is flagged.)
  **Reading, whole span.** From 2016 to 2018 Ternium out-earned every rival read; over the decade its pretax margin (13.6%
  average) sits at Nucor's (12.7%) and above ArcelorMittal's and Gerdau's. That is the strongest evidence for a castle, and
  it is written down here as found **[M1997-127]**. Over the last full cycle, trough to trough 2019 to 2025 (Ternium's
  operating income bottomed at $865M in 2019 and $705M in 2025), it is middle of the field: second of four on pretax margin,
  third of four on return on equity. In the latest down-leg its pretax margin was the lowest of the four in 2024 (4.1%,
  against ArcelorMittal 4.7%, Gerdau 8.2%, Nucor 9.4%) and the second lowest in 2025 (4.2%, against Gerdau 3.6%,
  ArcelorMittal 5.9%, Nucor 7.9%). A low-cost operator is the one that does well when the market is hard, "a company holding a
  low-cost advantage must pursue an unrelenting foot-to-the-floor strategy" **[L2004-007]**; Ternium was at the bottom of the
  field when the import price fell. *(Corrected before close, same session: this sentence first said Ternium was "the
  weakest of the four but ArcelorMittal" and that its margin "fell furthest"; both were wrong on the table above. From 2022
  to 2025 Nucor's and Gerdau's margins fell further in points; Ternium's level was the lowest or second lowest.)*
- **The parts table** (the filer reports two operating segments; note 5, operating income, management view, $M).

  | Part | 2023 | 2024 | 2025 | Share of three-year total | Castle | Decides |
  |---|---|---|---|---|---|---|
  | Steel | 2,391 | 1,560 | 968 | 106% | the subject of this question | **yes, more than half** |
  | Mining | 16 | (166) | (141) | -6% | iron ore, mostly internal | no |

  The steel segment is itself three markets that the CEO "allocates resources and assesses performance" for as "an
  integrated business" (note 5); no operating profit by country is reported, so the castle is read for the segment as a
  whole, with Usiminas (about a quarter of steel sales since 2024) the part the filer itself describes as under price
  pressure **[L2008-005]**. Only three years of segment profit are read; the earlier two would not change which part decides.
- **The field's returns over the last full cycle, judged in words.** The durable players of the field read here earned, over
  2019 to 2025, average returns on equity of 7.8% (ArcelorMittal), 12.5% (Ternium), 15.4% in a currency with Brazilian
  inflation (Gerdau) and 23.2% (Nucor, in a market behind a 25% then 50% US tariff). Ternium's own 12.5% rests on one year:
  without 2021 (42.9%) its six other years average 7.4%, and 2023 to 2025 average 2.9%, below the long government rate of
  5.60%. Judged in words, as the convention asks: a castle that protects ordinary returns, in a field where "you can have only
  two competitors and they’re still terrible businesses, they beat each other’s brains out" **[M2013-052]**; nothing in the
  span shows the "excellent returns on invested capital" a moat protects **[L2007-004]**.
- **Widening or narrowing** **[M1999-108]**. Narrowing in the filer's words in each home market over 2023 to 2025: Brazilian
  imports up in each of the three years, Mexican demand down about 10% in 2025 with diverted US-bound steel added, Argentine
  imports liberalised in 2024 (Item 3.D). The change for the better the filer is investing in (the Pesquería downstream lines
  started in Q1 2026, the DRI-EAF slab shop now due in early 2027) has not been through a downturn, and a change for the
  better is credited only on a full cycle (Q2, Change) **[M2017-026]**; it is not credited.
- **What could destroy it** **[M2000-014]**. The filer names it: a failure of the US and Mexico "to reach a new trade agreement
  on reasonable terms", the Section 301 investigation of Mexico, and Chinese exports "exerting downward pressure on sales and
  margins of steel companies operating in other markets" (Item 3.D). A product "that can be shipped in from abroad very
  easily" is the rows' named risk **[M2007-116]**; the protection the filer has is mostly the government's (antidumping duties
  in Mexico, Brazil, Argentina and Colombia, Item 4.B, Trade regulations), which is not a castle the business owns.
- **Ask the competitors** **[M1999-130]**: not done; public-record scuttlebutt beyond the filings was not in this run.
- **VERDICT: OUT.** A commodity business **[M2007-131]** whose price is set by the import offer **[M2012-109]**,
  **[M2023-079]**, with no filing that states a low-cost position and a margin record that puts it in the middle of the named
  field over the last full cycle and at or near the bottom in the current down-leg **[M1997-010]**, **[M2009-059]**, and whose own
  returns over that cycle are ordinary on the filer's and the rivals' filings: the standing castle that protects only ordinary
  returns is OUT, not TOO HARD (Q2, What it rules OUT) **[L2007-004]**, **[M2013-052]**. The money test is answered yes by the
  filer's own import figures **[M2011-015]**. *Alternative reading, recorded and not adopted:* TOO HARD (NATURE), on the
  commodity paragraph's "where no filing states it", since no filing states Ternium's cost position and the next decade turns
  on US and Mexican trade policy, a forecast no insider would write down **[M2000-105]**. I did not adopt it because the rule
  that applies when the returns are known sends the file OUT, and the returns over the full cycle are known; the tenuous-moat
  row sends a castle to TOO HARD only because "We don’t know how to valuate that" **[M2000-019]**. Price does not reopen
  it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict (closed at Q2); the balance sheets were read in Step 0.
## Q5 — WHO RUNS IT. NOT REACHED (closed at Q2).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (closed at Q2).
## Q7 — WHAT IS IT WORTH. NOT REACHED as a verdict; the computation for the owner's reporting figures is below, under its heading.
## Q8, Q9, Q10, Q12. NOT REACHED (closed at Q2).

---
## THE BOX
**OUT at Q2** (commodity flat steel priced off the import offer; no filing states a low-cost position; middle of the named
field over the 2019 to 2025 cycle and at or near its bottom in 2024 and 2025; ordinary returns over the full cycle);
TOO HARD (NATURE) recorded as the alternative reading. **Integrity facts recorded, not judged** (the Brazilian court ruling on
the 2012 Usiminas tag-along, the related-party flows to San Faustin companies, the dividend proposal cut two months after it
was announced; see below). COMPUTATION beneath the stop, not a clearance: value range **$100.60 to $214.81 per ADS ($10.06
to $21.48 per share)** against **$58.99 per ADS ($5.899 per share)**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down, not weighed; no verdict; the box unchanged (operator rule 2)* **[M1997-127]**.

**Bearing on Q3 (capital).** Capital expenditure (cash line, "Capital expenditures and advances to suppliers for PP&E") was
$524M, $581M, $1,461M, $1,865M and $2,501M in 2021 to 2025 against depreciation and amortization of $592M to $788M (cash
flow statements, 20-Fs 0001342874-24-000018 and -26-000020); 2025's $2.5B was "the peak of the current investment cycle,
with the bulk allocated to the continuing expansion of the industrial center in Pesquería" (Item 5); Mexico's 2025 capex
was $2.0B, Brazil's $322M, Argentina's $126M, mining $156M (Item 4.B), so spending outside the Mexican expansion was near
the depreciation charge. 2026 guidance: $1.9B to $2.1B (Item 4.B). Owners' equity was $11.8B at the end of 2022 and $12.3B
at 2026-06-30 after about $5.8B of capex in 2023 to 2025. The Usiminas investment: control-group shares bought in January
2012; write-downs of the investment of $739.8M in 2014 and $191.9M in 2015 (FY2017 20-F, selected data note (1)); on
consolidation in 2023 a loss of $171M and a recycling of other comprehensive income of $(935)M (Item 5 income table); a
further 153.1M ordinary shares bought for $315.2M in cash, closed 2026-02-10 (note 32).

**Bearing on Q4 (the accounts).** The company features "Adjusted EBITDA" as the headline of its results release ("ADJUSTED
EBITDA $717 MILLION", 6-K 0001342874-26-000044) and cited "a sequential increase in adjusted EBITDA" when it cut the
dividend proposal (6-K 0001342874-26-000025); the rows on the figure are **[M1998-086]** and **[L2016-006]**, recorded here
for Q4 and Q5, not weighed. Deferred tax results swing with local currencies against the dollar (a $222M gain in 2025,
Item 5). Dividends "paid in kind to non-controlling interest" of $112.3M (2022), $233.5M (2023) and $112.3M (2025) appear
only among the non-cash transactions (cash flow statements). The CSN litigation provision is charged below operating income
($410M in 2024, $117M in 2025, $71.5M in H1 2026).

**Bearing on Q5 (integrity: recorded, not judged; a later run that reaches Q5 must answer these** **[M2013-088]**).
(1) Brazil's Superior Court of Justice in June 2024 reversed its own 2023 ruling and held that Ternium Investments, Ternium
Argentina and Tenaris's Confab must pay CSN an indemnification over the 2012 Usiminas purchase, on CSN's claim that the
buyers owed the non-controlling Usiminas holders a tag-along tender offer; the court confirmed the obligation in December
2024 and Ternium's further appeals were denied leave in September and November 2025, one appeal still pending at the Supreme
Federal Tribunal; Ternium "continues to believe that all of CSN's claims and allegations are unsupported and without merit",
citing the securities regulator's decisions of 2012 and 2016 (note 25(i)(a)). Provision $599.1M at 2026-06-30 (6-K
0001342874-26-000046). The rows on treatment of other shareholders are **[M1998-121]**. (2) Related-party flows with
companies controlled by San Faustin, the controlling shareholder, rose with the Pesquería project: engineering, construction
and labour services $406M in 2025 (from $178.1M), plant equipment, spare parts and technical assistance from Tenova and
others $429.6M (from $27.6M), electricity from Techgen (48% Ternium, 30% Tecpetrol, 22% Tenaris) $316.6M; "Material related
party transactions are subject to the review of the audit committee" (Item 7.B). (3) Control: San Faustin holds 65.03% and
Tenaris 11.46%; RP STAK controls San Faustin; the articles let the board waive pre-emptive rights (Item 3.D). The chairman,
Paolo Rocca, is also chairman and CEO of Tenaris and president of San Faustin; directors and senior management as a group own
1,570 shares (Item 7.A). (4) The board proposed a $2.70 per ADS dividend on 2026-02-17 and cut it to $2.20 on 2026-04-15
"in response to global uncertainty" (6-K 0001342874-26-000025). (5) Pay: directors receive fixed fees ($115,000 each, the
chairman $295,000 more); aggregate cash pay to directors and senior management $31.1M in 2025 plus retention units of
$7.03M (Item 6.B). No guidance or "make the numbers" habit was looked for; none recorded.

**Bearing on Q6 (the money and the owners).** No repurchases in 2025 (Item 16E); a five-year authority to buy up to 10% at
75% to 125% of the five-day average price is proposed, with no price related to value. "Ternium S.A. does not have, and has no
current plans to establish, a formal dividend policy" (Item 8.A); dividends paid $569M (2023), $609M (2024), $530M (2025),
$255M (May 2026). The Feb 2026 purchase of Usiminas shares was paid in cash, not stock; no all-stock deal found. No buyback
prices exist to set against the bottom of the Q7 range.

**Bearing on Q9 (could it ruin us).** Net debt at 2026-06-30 $319M (borrowings $2,843.8M plus leases $206.9M, less cash
$1,430.7M and other investments $1,300.9M); at 2025-12-31 the filer reports net cash of $712M. Borrowings at year-end 2025:
25% current; Usiminas debentures in BRL at 16.17%; covenants met (Item 5.B). Beside them: the CSN provision of $599.1M, a
guarantee of up to $57.2M of Techgen obligations and $28.8M of GIMSA's (note 25(ii)). About $0.8B of the cash and investments
is Ternium Argentina's, inside the Argentine system **[L2016-009]**.

**Bearing on Q12.** No named business of the rows; nothing recorded.

## Q7 COMPUTATION, NOT A CLEARANCE (the owner's two reporting figures; no entry language; operator rule 3)
Script `_research 2026-10-13 TX/q7.py` (output `q7_output.txt`) and `q7_literal.py` (output `q7_literal_output.txt`).
- **Owner cash** (USD, the reporting and functional currency; after the company's own tax, which is inside operating cash
  as taxes paid). Central, by specific (e): **maintenance-only** = net cash from operating activities less depreciation and
  amortization as the maintenance guess (the filer's own capex split puts non-expansion spending near the charge, Q3 facts
  above; depreciation as "a proxy for required capital expenditures" **[M1998-127]**), less cash paid for businesses and
  minority stakes. All-equity basis: before net interest (interest paid added back, interest received taken out; 2015 to 2019
  interest received is the filed interest income, the cash line not being tagged). Beside it: **all-spending** = operating
  cash less the capex cash line and lease payments.
  Maintenance-only, equity-only, $M: 2015 889; 2016 693; 2017 (1,981) (Ternium Brasil bought for $1,891M); 2018 1,150;
  2019 981; 2020 1,113; 2021 2,084; 2022 2,133; 2023 1,724; 2024 1,163; 2025 1,526.
- **The base, specific (a).** The window's first year, 2021, is a peak year on the filer's own account (operating income up
  388%; "Investors should not rely on the results of a single period, particularly a period of peak prices", Item 5) and
  2025 is a down year (operating income down 44%), so the base is the last full cycle, trough to trough by operating income,
  2019 to 2025: **$1,523M** all-equity ($1,532M equity-only). The prior cycle, 2015 to 2019: $428M all-equity, after the
  $1,891M paid for Ternium Brasil, specific (c).
- **Growth, specifics (c) and (f).** Acquisitions deducted, total growth credited (the default pair; net purchases in the
  window, $124M, are far below half of owner cash, so not a serial acquirer). The growth shown between the cycle averages,
  28.9% a year, carried ten years would need owner cash far above its highest share of sales (13% in 2022), so it is cut to
  the business's own sales growth between the same cycles: **9.5% a year** (cycle sales averages $9,290M and $14,614M). The
  sales growth is itself mostly bought: Ternium Brasil (2017) and the Usiminas consolidation (2023, about $4B of yearly sales
  for $118.7M of cash in the window). Zero nominal growth after year ten; discount at **5.60%**.
- **Minority shareholders.** **CONVENTION of this run** (the framework's all-equity basis does not address it): the
  consolidated value less net debt is shared with the subsidiaries' minority holders at their book share of total equity at
  the latest filed date, 26.5% (owners' $12,299.6M of $16,739.0M, 2026-06-30), so the owners' share is 73.5%. Rationale: the
  minorities own a quarter of the consolidated cash flows (Usiminas' 76.7% minority, Ternium Argentina's 37.4%, Tenigal's
  49%) and book equity is the only filed measure of the split; the 2021 to 2025 profit split (owners 83.8%) is shown beside.
- **Net debt** at 2026-06-30, which includes the February 2026 Usiminas purchase: **$319M**. The CSN provision of $599.1M is
  shown beside, not in net debt (it is not a borrowing).
- **VALUE RANGE (central: maintenance-only, all-equity, cycle base, owners' book share): $10.06 to $21.48 per share, $100.60
  to $214.81 per ADS**, against $5.899 per share, $58.99 per ADS. Width 2.12 to 1. The ends are the no-growth case and the
  9.5% case.
- **FAIR PRICE (Part VII; each end valued at 10%, the two averaged; after the company's own tax, no conversion):**
  **all-equity (central) $8.23 per share, $82.28 per ADS**; **equity-only $8.40 per share, $83.98 per ADS**.
- **The floor, tested first.** At the price, the 9.5% case valued at 10% is $108.75 per ADS, above the price, so some case
  earns the floor; the no-growth case valued at 10% is $55.81 per ADS, just below the price, so the no-growth case earns a
  little under 10%. The width is under three to one.
- **Beside the central figure:**
  - With the CSN provision deducted: fair $80.04 per ADS.
  - Owners' share at the 2021 to 2025 profit split (83.8%): range $114.76 to $245.04 per ADS, fair $93.86.
  - The literal 2021 to 2025 window: average $1,697M, end-to-end change -7.1% a year, so by specific (b) the decline is the
    bottom and no growth the top: range $64.09 to $112.26 per ADS, fair $50.56 per ADS.
  - All-spending, cycle base: range $60.34 to $129.38 per ADS, fair $49.27 per ADS; all-spending, literal window: the series
    changes sign (negative in 2024 and 2025) and the halves are meaningless, so the no-growth case alone, $61.26 per ADS
    ($33.78 at 10%).
- What the computation rests on and the box does not: a cycle base that contains the 2021 and 2022 peak years, a growth rate
  made mostly by acquisitions, the maintenance guess, a split with the minorities that the filings do not state, and $0.8B
  of Argentine cash that cannot be freely moved. None of it reopens Q2 **[M2019-015]**.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit a5209c30); written question by question; committed after each
      (5e051685 Step 0 to Q1; 76b70db7 Q2; this commit the close).
- [x] Dispatched: the brief allowed the per-question commits; the lock is the dispatching session's (I saw a lock file in
      `Screens/_daily/` at the start and did not touch it); the fold is the dispatcher's. A run not in the register binds nothing.
- [ ] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched: **not fully kept.** No such file was
      opened, but one filtered listing of `Test Runs/` was made (contamination note (2)); declared, not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv`; every quoted fragment beside an id is checked against its row by
      `_research 2026-10-13 TX/check_ids.py`; every filing fact carries its document and accession; the peers' figures are
      their XBRL facts, flagged as not read against their filed statements.
- [x] The order was kept; Q2's STOP closed the run; nothing after it is a clearance; the Q7 figures are headed COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5): operating cash less the maintenance guess
      or all spending, after tax; the sovereign from the US Treasury, dated; the price an aggregator quote, flagged.
- [x] Contrary evidence was written down as found **[M1997-127]** (the 2016 to 2022 margin record; the computation's range
      against the price); facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited (not a point-in-time run; today's rows only).
- [x] Only the arithmetic lines of `tools/run.py` were used (it printed none).
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the reply).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Two Q2 rules point different ways for a commodity producer.** The commodity paragraph (2026-10-12) says "where no filing
states it, TOO HARD (NATURE)" of the cost position, while the ordinary-returns item says a field earning ordinary returns over
a full cycle "is OUT, not TOO HARD". For Ternium no filing states the cost position and the returns are known. I applied the
ordinary-returns item and recorded TOO HARD (NATURE) as the alternative reading; the text does not say which governs, and two
analysts could split here. (2) **Minority interests are not addressed** by the all-equity basis (Q7, On what the floor is
earned): for a group with a 76.7% minority in one subsidiary and 37.4% in another, the owners' share of the value is a
judgment worth about 14% of the figure (book share 73.5% against the profit split 83.8%). I confessed a CONVENTION of this run.
(3) **Specific (c) does not fit a step acquisition paid mostly before the window.** Usiminas was bought into in 2012 to 2016,
written down, and consolidated in 2023 for $118.7M of window cash while adding about $4B of yearly sales; the default pair then
credits the acquired sales growth as the business's own, and specific (f)'s cut to sales growth carries it forward. The text
offers no organic measure where the filer reports none. (4) **Which series defines the cycle.** Specific (a) says owner cash
defines the cycle, but Ternium's owner cash has no clean troughs (2017 holds an acquisition, 2024 and 2025 hold an expansion
programme); I dated the cycle by operating income and said so. (5) **The template asks for Q4's balance sheets "in Step 0 if
the file closes before Q4"**, which I did; it does not say whether the reading should carry a verdict there (I gave none).
(6) **The canonical brief asked me to read the annual-meeting documents**, which serve Q5 and Q6; after a Q2 STOP they bear only
on facts recorded and not weighed, so I left them unread and say so.
