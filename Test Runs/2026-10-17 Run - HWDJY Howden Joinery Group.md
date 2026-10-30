# Company Run — Howden Joinery Group Plc (OTC ADS: HWDJY; London: HWDN) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its document and date (no SEC accession
exists for this name; see Step 0); a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT
REACHED. Copied to this dated name before any fetch (commit 4353c815).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (34b67bed): `PORTFOLIO.md` read for this one ticker; the operator does not hold HWDJY (no line names HWDJY, HWDN or Howden).*

**Contamination, declared.** Before any work I listed `Test Runs/` filtered to the strings "HWDJY" and "howden"; nothing
matched, so no file was seen. The git log printed at session start showed three commit subjects about another company's
run (ELUXY, OUT at Q2); the session memory index carries generic queue counts for the project. None names this company
and none was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** 788.0p an ordinary share (London close 2026-10-16, ticker HWDN.L, Yahoo Finance chart feed via
  `tools/sources.py price()`; **aggregator, live quote only, flagged** per operator rule 5). The ADS (HWDJY, four
  ordinaries each, F-6EF of 2019-11-25, accession 0001193805-19-001832, as the brief records) last traded at
  **US$40.02** (2026-10-16, same aggregator, flagged); four ordinaries at 788p are £31.52, or US$41.77 at the rate below,
  so the thinly traded ADS sat about 4% under its underlying on that day.
- **Exchange rate:** US$1.3253 to the pound, Bank of England daily spot (series XUDLUSS), 15 Oct 2026, from the Bank's
  statistical database (the issuing authority for sterling; file `boe_iadb_2026-10.csv`, kept in `cache/`). The
  aggregator showed 1.333 on 17 Oct (flagged, not used).
- **Shares.** No cover page exists (not an SEC filer; `python Screens/cover_shares.py HWDJY` returns "NOT AN SEC
  REGISTRANT"). Count built from the company's own documents:
  - Annual Report and Accounts 2025 (approved 25 Feb 2026), note 16: 541,517,203 shares in issue at 27 Dec 2025 after
    12,074,517 bought back and cancelled for £100.2m in 2025; 2,479,691 in treasury; employee share trusts held 0.19% of
    issued capital (shareholder information page, about 1.03m shares).
  - RNS "Admission of New Ordinary Shares" (22/23 June 2026): 12,725,469 new shares issued to the seller of DIY Kitchens;
    554,242,672 in issue, 3,326,336 in treasury, 550,916,336 voting.
  - RNS "Total Voting Rights" (1 Oct 2026): 548,552,116 issued, 4,871,987 in treasury at 30 Sep 2026.
  - RNS "Transaction in Own Shares" (12 Oct 2026): 500,000 more bought and cancelled 5 to 9 Oct at 748.58p to 764.89p
    (daily weighted averages); **542,980,129 shares in issue excluding treasury** after those purchases.
  - The RNS texts were read through Investegate, a distributor of the RNS feed (the company's own regulatory-news page
    sits behind a bot wall); the texts are the company's own announcements.
  - **Count used: 541.95m shares** = 542,980,129 less about 1.03m held by the employee benefit trust (the trust waives
    dividends and abstains; its holding is taken at the 27 Dec 2025 percentage, the latest stated). Per ADS: four shares.
- **Market cap:** 541.95m x 788p = **£4,271m** (US$5,660m at 1.3253).
- **Sovereign for the earnings currency (sterling):** **5.7225%**, the Bank of England's 20-year nominal par gilt yield
  (database series IUDLNPY), 14 Oct 2026, the latest dated value in the file fetched 17 Oct. **CONVENTION of this run:**
  the protocol's table names no sterling series; the Bank of England is sterling's issuing authority for published yield
  curves, its longest daily par-yield series in the statistical database is the 20-year, and its 30-year spot curve file
  for the current month was empty when fetched (`yc/GLC Nominal daily data current month.xlsx`, every value "#VALUE!").
  Rationale: the rows ask for the long government rate **[L2000-021]**; the 20-year is the longest the issuing authority
  publishes as a daily par yield.
- **Filings read** (operator rule 4; no SEC annual filing exists, so each document is named and dated in place of an
  accession): Annual Reports and Accounts for FY2015 to FY2025 (company investor site, `/docs/librariesprovider25/
  archives/annual-reports/`; FY2015, FY2016, FY2018, FY2020, FY2022, FY2024 and FY2025 read for the primary statements,
  the others for specific notes); 2026 Half Year results announcement (23 July 2026); "Howdens agrees to acquire DIY
  Kitchens" (3 June 2026); acquisition presentation (3 June 2026); trading update (28 April 2026); 2025 preliminary
  results; "Introduction to Howdens" investor presentation (Feb 2025); the RNS items above, and the share buyback RNS of
  3 June and 10 August 2026. The directors' remuneration report is read inside the 2025 Annual Report.
- **One figure cross-checked against the filed statement:** FY2025 revenue £2,418.0m in the audited consolidated income
  statement (AR2025 p.157) equals the five-year record (AR2025 p.205) and the "£2.4 billion" of the 2026 half-year
  announcement's notes to editors. FY2024 operating profit £339.2m agrees between AR2024's income statement and AR2025's
  comparative column.
- **`python tools/run.py HWDJY`:** "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE". No arithmetic lines exist; all
  arithmetic below is by hand from the reports, in `data_filed.csv` and `scripts/calc.py` in the research folder.

**Owner cash after every real cost, by year (£m; from the audited cash flow statements).** Owner cash before interest
= net cash from operating activities, less capital spending (property, plant, equipment and intangibles) net of disposal
receipts, less lease principal and all interest paid (the group has no borrowings until June 2026, so interest paid is
lease interest and facility fees; from 2020 IFRS 16 moves rent out of operating cash, and before 2020 the rent sits inside
it, so deducting lease cash keeps the series on one footing), less the share-based payment charge (added back inside
operating cash; a real cost **[L2015-003]**). Interest received on cash is left out (the cash is netted at Q7).

| FY | Revenue | Op. profit | Op. margin | Capex net | Lease cash | Tax paid | Tax charge, current-year basis | Owner cash, as filed (cash tax) | Owner cash, tax-charge basis |
|---|---|---|---|---|---|---|---|---|---|
| 2015 | 1,220.2 | 221.9 | 18.2% | 45.9 | in rent | 35.3 | 44.2 | 104.9 | 96.0 |
| 2016 | 1,307.3 | 237.2 | 18.1% | 63.3 | in rent | 28.8 | 51.4 | 139.9 | 117.3 |
| 2017 (53 wks) | 1,403.8 | 234.4 | 16.7% | 48.5 | in rent | 41.8 | 47.2 | 124.2 | 118.8 |
| 2018 | 1,511.3 | 240.1 | 15.9% | 44.2 | in rent | 45.4 | 48.1 | 114.7 | 112.0 |
| 2019 | 1,583.6 | 260.0 | 16.4% | 60.8 | in rent | 46.2 | 51.7 | 155.7 | 150.2 |
| 2020 | 1,547.5 | 195.7 | 12.6% | 69.7 | 87.6 | 32.2 | 37.7 | 168.3 | 162.8 |
| 2021 | 2,093.7 | 401.7 | 19.2% | 85.8 | 85.8 | 73.1 | 78.0 | 255.7 | 250.8 |
| 2022 | 2,319.0 | 415.2 | 17.9% | 140.1 | 79.2 | 101.5 | 79.9 | 168.7 | 190.3 |
| 2023 (53 wks) | 2,310.9 | 340.2 | 14.7% | 118.9 | 121.8 | 63.5 | 80.3 | 125.6 | 108.8 |
| 2024 | 2,322.1 | 339.2 | 14.6% | 121.9 | 113.4 | 39.2 | 81.7 | 155.2 | 112.7 |
| 2025 | 2,418.0 | 355.3 | 14.7% | 156.4 | 123.9 | 25.7 | 81.1 | 195.0 | 139.6 |

Notes to the table: 2016's tax paid is net of a £12.7m refund; 2022 includes £14.6m paid for a subsidiary (net of cash),
shown separately at Q7, not in the capex column. The "tax-charge basis" replaces cash tax with the year's tax charge less
the adjustments in respect of previous periods (tax notes of AR2022, AR2023, AR2024, AR2025), because the filer says cash
tax in 2022 to 2025 carries prior-year patent-box credits (AR2025 financial review: "Corporation tax payments were lower
at £25.7m (2024: £39.2m) as a result of prior year tax credits due to the patent box claim"; AR2022 note 7: a prior-year
current tax credit of £36.1m for 2017 to 2021). Pension: operating cash includes deficit-repair contributions above the
pension charge of 39.1, 30.6, 21.2, 16.3, 26.9, 22.2, 18.5 and 16.9 (2015 to 2021 and 2023); none is currently payable
(H1 2026 announcement, Pensions). Capital spending 2025 includes the "one-off freehold purchase of the Runcorn
manufacturing facility for £31m" (AR2025 financial review). Five-year averages (2021 to 2025): £180.0m as filed, £160.4m
on the tax-charge basis. Q4 recasts and Q7 builds the range from this table.

**Lines of evidence chosen, and from which sections** (the brief asks the run to derive them). From the Strategic Report's
"Howdens at a glance", "Our purpose ... our business model" and CEO review (the business-model part of a 10-K's Item 1):
the trade-only, in-stock, depot model; depot count; UK and International revenue (note 3, one operating segment). From
"Risk management and principal risks" (Item 1A): the nine principal risks (cyber security; market conditions; people;
health and safety; supply chain; maximising growth; business model and culture; product; business continuity). From the
Financial Review (Item 7) and the primary statements: margins over the cycle FY2015 to FY2025; gross margin through the
2021 to 2023 inflation; capital spending and leases (IFRS 16 from FY2020); tax and the patent-box credits; buybacks and their
prices (equity notes); the Sheridan purchase (2022) and DIY Kitchens (2026); the pension scheme; share-based pay and the
directors' remuneration report; litigation and investigations (sweep below at Q4).

---
## THE FOUNDATIONS (not a gate)
The foundation that bears hardest here is the margin of safety: a business this well known in its home market, priced at
about 22 times its cycle-average owner cash, will only clear if the arithmetic is so plain "it ought to just kind of scream
at you" **[M1996-084]**. The share-as-business test is easy to put: the question is whether one "Would I be happy buying
this stock if the market closed for five years?" **[M1997-109]**, which for a UK kitchen supplier turns on UK
repair-and-improvement spending, a variable the run does not forecast. Who is paid to tell: the company publishes an
"Analyst Consensus" page and sets its executive bonus by "a combination of analyst consensus estimates, internal forecasts"
(AR2025 remuneration report), so the figures it is judged by are partly ones it helps shape; carried to Q4 and Q5.
**Contrary evidence, written down as found [M1997-127]:** (1) owner cash as a share of sales fell from 8% to 13% in
FY2015 to FY2021 to 5% to 6% in FY2023 to FY2025 on the tax-charge basis, while capital spending roughly doubled; (2) the
UK headline tax rate rose from 19% to 25% in 2023, so the FY2021 to FY2022 years overstate future after-tax cash; (3) the
2025 bonus targets sat below the prior year's actual profit (Q6); (4) the company bought DIY Kitchens, an online seller
direct to consumers, at about 8.5 times EBITDA, partly in new shares, while buying back shares at similar prices (Q6).

## THE STANDING RULE
A part-interest in a business with no borrowings until June 2026 (a £240m term loan, net cash still stated by the company)
puts no buyer at risk of ruin, provided the buyer does not borrow to own it: "Never risk permanent loss of capital."
**[L2023-005]**; borrowing is "the one thing that ends — or can prevent you from playing out your hand" **[M2004-065]**.
No sizing or financing is set here (Q10).

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The business, from the filings.** Howdens sells kitchens and joinery to trade customers (local builders) only, from
  975 depots at 13 June 2026 (893 UK, 82 France, Belgium and Ireland), always in stock, with confidential local pricing and
  trade credit; about 38% of cost of goods is made in its own factories at Runcorn and Howden (AR2025 "at a glance": "c.38%
  volume of products manufactured as % of cost of goods sold"). One operating segment (AR2025 note 3); UK revenue £2,333.2m
  of £2,418.0m in FY2025. Revenue "typically ... more than 95%" from goods (note 2). From 23 June 2026 it also owns DIY
  Kitchens, an online seller to non-trade consumers (2025 revenue £136m, EBIT £37m, about a tenth of group EBIT).
- **Key variables and how predictable they are** **[M1998-044]**: (1) UK kitchen and joinery demand, mostly residential
  repair, maintenance and improvement (AR2025 p.4 chart of "% Howdens' revenue": residential against non-residential and
  RMI against new construction, the shares printed as 90%/10% and 95%/5%; the extraction does not let me pair each figure
  with its label, so I record only that both splits are lopsided toward residential RMI), cyclical but not fast-changing;
  (2) the depot count (scope "around 1,000" UK depots, H1 2026) and same-depot sales; (3) gross margin, 60.1% to 64.3% in
  every year FY2015 to FY2025; (4) the cost of the depot estate (lease cash £87.6m to £123.9m a year since FY2020). The
  product is a kitchen cabinet, a door, a worktop: "I understand the economic dynamics of the industry. Is there — are
  there competitive moats? Is there ease of entry?" **[M2011-014]** is the right form of the question, and the filings
  answer it with eleven years of margins.
- **Ten years out.** The forecast is about builders and households, not technology: "we know what we think we can project
  out in terms of consumer behavior and threats to a business" **[M2023-030]**. A reasonable fix on "what the earning power
  and competitive position will look like in five or 10 years" **[M2012-065]** exists: the business has been run on the same
  model through 2008, 2020 and the 2023 to 2025 market decline (the company's own peer chart, "Introduction to Howdens"
  Feb 2025, shows positive revenue growth in most of those years).
- **The doubt I carry.** Retail-like businesses are where the speakers found "it’s easy to sort of think you understand
  retail, and then subsequently find out you don’t" **[M2014-052]**; and the purchase of an online direct-to-consumer
  kitchen seller is the company telling me the channel may move. These go to the castle (Q2), not to whether the economics
  can be pictured; Howdens is a trade distributor and manufacturer whose figures tell me what its future figures look like.
- **VERDICT: IN.** The economics can be pictured ten years out on the filings: a UK trade distributor-manufacturer of
  kitchens with eleven years of readable statements, one segment, no derivatives book, no financial institution inside it
  **[M2000-037]**, **[M2012-065]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**Competitors, from the filings.** The annual reports FY2015 to FY2025 name no competitor (sweep: the words "competitor",
"Wren", "Magnet", "Benchmarx", "Wickes", "Travis", "B&Q", "Screwfix", "Jewson", "Selco", "Nobia", "Toolstation" across all
eleven reports; the hits are directors' past employers and the unnamed "four key competitors" whose web traffic the 2023
report says Howdens exceeded). The company's own investor presentation "Introduction to Howdens" (Feb 2025, p.10) names its
peer set: "Building Product Merchants: Grafton, SIG, Travis Perkins, Wickes, Kingfisherand Nobia." (the extraction's
spacing). **None of the six files with the SEC** (all London or Stockholm listed). **CONVENTION of this run:** the rivals' own
primary reports are read in place of SEC filings, and the three chosen from that list are the ones that sell kitchens in the
UK: Travis Perkins (its merchant arm has "a kitchen design and supply offer, branded as Benchmarx", AR2025 p.6), Wickes
(kitchens and bathrooms, retail and installed) and Nobia (Magnet). Rationale: the brief allows primary reports where no rival
files with the SEC; the rows ask that the competitors be asked **[M1999-130]**, and their own accounts are the nearest public
answer. Grafton, SIG and Kingfisher are flagged as named and not read.

| Company (source) | Metric | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| Howdens (ARs FY2016 to FY2025, income statements) | operating margin | 16.7% | 15.9% | 16.4% | 12.6% | 19.2% | 17.9% | 14.7% | 14.6% | 14.7% |
| Travis Perkins (AR2021 and AR2025 five-year summaries, statutory operating profit over revenue) | operating margin | 5.1% | (0.3)% | 3.3% | 0.7% | 7.6% | 5.7% | 3.3% | 0.0% | (2.1)% |
| Wickes Group (AR2022, AR2023, AR2025 income statements) | operating margin | n/a | n/a | n/a | n/a | 6.3% | 4.3% | 4.0% | 3.1% | 4.3% |
| Nobia (year-end report 2025, Cision distribution of the company's report) | group adjusted operating margin | | | | | | | | 2.8% | 5.3% |

Travis Perkins 2017 to 2019 include Wickes and are not re-presented (its footnote); 2020 is re-presented. Nobia has agreed
to sell its UK region (Magnet), reported as discontinued, describing its Nordic core as having "structurally higher margins"
(year-end report 2025); no Magnet margin series is published, so the UK kitchen rival nearest the Howdens model is shown only
by its owner's decision to leave the UK. Wickes carried £719.8m of lease liabilities against equity of £130.9m at 27 Dec
2025 (AR2025 balance sheet). Howdens' own return: operating profit £355.3m in FY2025 on capital employed (equity less cash,
plus lease liabilities and the pension deficit) of about £1,559m, about 23% pre-tax with leases capitalised; the company's
own ROCE for its 2023 share award was 36% (AR2025 remuneration report, on its own definition).

- **The castle tests, each with its filing fact.**
  - *Key factors and permanence* **[M1995-038]**: trade-only (no retail customers; the builder's price is confidential and
    local), in stock (AR2025: "99.9% availability from primary distribution to depots"), the depot near the builder ("88% of
    customers are less than 5 miles from a Howdens depot"), trade credit, and own manufacturing of about 38% of cost of
    goods. The model has run unchanged through 2008, 2020 and the 2023 to 2025 market fall.
  - *The attacker with money* **[M2011-015]**: to copy it an entrant needs about 900 depots, a credit book of local
    builders, two factories and the stock; the rivals that already have branches (Travis Perkins with 1,426, Wickes with its
    stores) have not taken the margin away in ten years. The custom-frame row fits: "you cannot figure out a way to call on
    those 18,000 people that are in that business and figure out a way to divert their business to you" **[M2002-032]**.
    Against it: "one competitor is frequently enough to ruin a business" **[M2012-108]**, and the reports name no kitchen
    specialist rival, so the largest private UK kitchen seller is not examined here (no filing of it read).
  - *Pricing power and the agony before a rise* **[M2005-020]**: prices were raised at the start of 2022, 2023 and 2026
    (AR2022 CEO statement: "We also increased prices, which helped us defray most of the significant rises in input costs";
    H1 2026: "the benefit of the price increase at the start of the year"), and gross margin stayed between 60.8% and 62.8%
    from FY2021 to H1 2026, against 64.3% in FY2015. The phrase "balancing pricing and volumes" recurs each year, a mild
    prayer session, but the pass-through held: "over time the businesses with strong competitive positions manage to pass
    through increases in raw material costs" **[M2005-017]**.
  - *Would the customer still choose it over the low bid* **[M2017-009]**: the builder buys on availability, credit and the
    depot relationship; the filings show a record number of customer accounts at the end of 2022 and 2023 and revenue held
    level in 2023 while "market volumes fell significantly" (AR2023 CEO Q&A).
  - *The low-cost position* **[M2018-043]**: not shown on cost per unit (no rival publishes one), but on margin the gap is
    three times and more the rivals' in every year of the table.
  - *Widening or narrowing* **[M1999-108]**: **contrary evidence**. Operating margin averaged 16.6% FY2015 to FY2019 (rent
    inside it) and 14.7% FY2023 to FY2025 (lease depreciation inside, lease interest of about 0.9% of sales below it), so
    about two to three points lower like for like; operating costs rose from 45.9% of sales (FY2019) to 48.0% (FY2025);
    owner cash fell from about 10% of sales to about 5% to 6% (Step 0 table). The company says it gained share in a
    contracting market ("Howdens' estimates based on proprietary data"), which no independent figure in the reports confirms.
    Capital spending of £119m to £157m a year since FY2022, against £44m to £70m before, may be the work of "widening the
    moat" **[L2005-010]** or the sign that "A moat that must be continuously rebuilt will eventually be no moat at all."
    **[L2007-005]**; the filings cannot yet separate the two.
  - *What could destroy it* **[M2000-014]**: the consumer planning and buying a kitchen online and having any builder fit
    it, the model Howdens has just bought (DIY Kitchens: "revenue growth of over 17% per annum over the past five years");
    a shrinking builder base; imports of a product with labour content (**[M2007-116]**; Howdens sources from "+300 global
    suppliers" and makes about 38% itself).
- **The parts table.** One reported segment; UK 96% of FY2025 revenue; International (France, Belgium, Ireland) carries
  unrecognised tax losses (AR2025 tax note: "Tax losses not recognised 6.3") and is small; DIY Kitchens joined after the
  window with 2025 EBIT of £37m against the group's £355m. The UK depot business decides (more than half of five-year
  operating profit; v5 Q2, a business of parts, "lumping them together [...] impedes analysis" **[L2008-005]**).
- **The field's returns over the last full cycle**, judged in words: the merchants and sheds that sell kitchens earn a few
  percent on sales, some years nothing; Howdens earns three times and more that margin in every year from 2017 to 2025,
  through COVID and the 2023 to 2025 market fall. This is not a standing castle that protects only ordinary returns.
- **VERDICT: IN.** The castle stands on ten years of margins set against named rivals' own accounts, and it is a moat that
  "protects excellent returns on invested capital" **[L2007-004]**; the narrowing since FY2021 is written down and carried
  to Q3 and Q7, where it is priced, not decided here.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**. Capital on one footing across the IFRS 16 change: equity less
  cash, plus the pension deficit, plus lease liabilities in excess of right-of-use assets (so that leases count as rent,
  as they do in owner cash). FY2019: 615.2 − 267.4 + 56.6 = **£404m**, against operating profit (rent inside) of £260.0m,
  about **64% pre-tax**. FY2025: 1,190.9 − 344.5 + 7.8 + (704.9 − 665.2) = **£895m**, against operating profit less lease
  interest of about £334m, about **37% pre-tax**; owner cash on the tax-charge basis of £139.6m is about 16% of it after
  tax. The level is high; goodwill is negligible (intangibles £62.6m, mostly software), so this is return on tangible
  capital **[M2011-060]**.
- **What the added capital earned.** Between FY2019 and FY2025 the capital rose by about £490m (two-thirds of it fixed
  assets: PPE £212m to £576m; inventories £232m to £409m; receivables £193m to £279m) while revenue rose £834m. Operating
  profit after rent rose about £74m, about **15% pre-tax on the increment**; owner cash after every cost (tax-charge basis)
  went from £150.2m to £139.6m, **no increase at all**, partly because the tax rate rose from 19% to 25%. The pattern is the
  one the rows warn of: "we’re not earning a higher rate of return on capital than we were when we started. We just put way
  more capital into the business" **[M2023-081]**, and "whether that’s good or bad depends on what we earn on that
  incremental $130 million over time" **[M2001-019]**. The increment is not yet proved: much of it (reformats, Runcorn
  capacity and the £31m freehold, the "XDC" facility named in AR2022, digital) is said by the filer to be for future growth.
- **To stand still and to grow** **[L1999-024]**, **[M2000-144]**: the filings give no maintenance figure. Owned
  depreciation (£68.6m in FY2025; £39.1m a year over FY2018 to FY2023) is used as the maintenance guess, "not
  inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**; capital spending
  above it, £47.7m a year over FY2018 to FY2023 and about £88m in FY2025, is growth spending. The H1 2026 going-concern
  note speaks of capital spending "reduced to a 'maintenance' level" in its stress case without a figure.
- **Growth arithmetic and its caps.** Sales grew 8.5% a year between the halves of the eleven-year record (FY2015 to FY2019
  against FY2021 to FY2025); owner cash grew 2.8% a year on the same halves (Q7). Growth here has needed capital at a
  return well below the business's average, which is the second-best business at best **[M1998-081]**.
- **WEIGHS: UNDECIDED.** For: a high return on the capital the business needs, little goodwill, no debt before 2026.
  Against: the last six years added about £490m of capital and £834m of sales and no more owner cash a year **[M2023-081]**.
  The debt half of the acquisition criterion is applied at Q9.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eleven of them** **[M2025-032]** (£m, audited year-end balance sheets in the reports named in
  Step 0; cash includes short-term investments in FY2015 to FY2017):

| FY | Equity | Cash | Inventories (% sales) | Receivables (% sales) | Trade payables | PPE | Intangibles | Lease liabilities | Pension |
|---|---|---|---|---|---|---|---|---|---|
| 2015 | 421.7 | 226.1 | 177.1 (14.5%) | 129.5 (10.6%) | 197.7 | 129.2 | 4.6 | off balance sheet | (49.2) |
| 2016 | 397.0 | 226.6 | 183.7 (14.1%) | 135.9 (10.4%) | 214.2 | 167.9 | 7.3 | off | (106.0) |
| 2017 | 454.2 | 241.1 | 208.3 (14.8%) | 137.8 (9.8%) | 212.1 | 180.0 | 15.4 | off | (109.3) |
| 2018 | 567.1 | 231.3 | 226.3 (15.0%) | 186.0 (12.3%) | 232.9 | 187.1 | 23.1 | off | (36.0) |
| 2019 | 615.2 | 267.4 | 231.8 (14.6%) | 193.1 (12.2%) | 241.4 | 212.4 | 24.9 | off | (56.6) |
| 2020 | 720.8 | 430.7 | 255.0 (16.5%) | 166.6 (10.8%) | 300.4 | 248.8 | 24.3 | 580.5 | (47.7) |
| 2021 | 991.5 | 515.3 | 301.6 (14.4%) | 205.8 (9.8%) | 384.7 | 295.8 | 22.6 | 591.2 | 140.8 |
| 2022 | 871.7 | 308.0 | 373.3 (16.1%) | 233.3 (10.1%) | 433.9 | 398.7 | 35.9 | 665.3 | (41.5) |
| 2023 | 978.4 | 282.8 | 382.8 (16.6%) | 194.5 (8.4%) | 373.2 | 456.9 | 43.5 | 684.5 | (12.6) |
| 2024 | 1,128.7 | 343.6 | 390.7 (16.8%) | 264.6 (11.4%) | 386.8 | 500.6 | 58.1 | 681.0 | (2.1) |
| 2025 | 1,190.9 | 344.5 | 409.2 (16.9%) | 278.8 (11.5%) | 384.0 | 576.1 | 62.6 | 704.9 | (7.8) |

  What moved and why. **No borrowings in any of the eleven years** (an undrawn facility only; the £240m term loan of June
  2026 is the first debt). **Equity** nearly tripled while about £1.7bn went out in dividends (£928m) and buybacks (£751m) over FY2015 to FY2025; goodwill is nil and
  intangibles small, so equity is tangible. **Fixed assets** went from £129m to £576m (PPE), the investment of Q3, including
  the Runcorn freehold bought in 2025. **Inventories** rose from about 14.5% to about 16.9% of sales: the filer explains it
  by depot openings, new ranges and safety stock (AR2025: "stock £18.5m higher as a result of depot openings and new product
  introductions"; H1 2026: "higher safety stock levels due to the conflict in the Middle East"); the trend is upward and
  the inventory allowance is the filer's stated estimation uncertainty (AR2025 note 1), so it is watched, not suspected
  **[M1995-064]**. **Receivables** move with trade credit (8% to 12% of sales), no drift. **Pension**: the deficit of £106m to
  £109m in FY2016 to FY2017 was paid down by about £190m of contributions above the charge over FY2015 to FY2023 and is now
  small; the scheme is closed to accrual. **Leases**: about £0.7bn of depot leases since IFRS 16, an operating cost carried
  in owner cash. "What the figures are saying and what they don’t say" **[M2025-032]**: they say a debt-free, tangible,
  cash-generating distributor whose capital base has grown faster than its owner cash since FY2019; they do not say how much
  of the new capital is maintenance.
- **The real costs.** Depreciation charged and treated as a cost; share-based pay of £3.6m to £10.3m a year deducted in
  owner cash; no recurring restructuring charges in FY2015 to FY2025 (the only "underlying" adjustment found is the £6.4m of
  DIY Kitchens acquisition costs in H1 2026); pension deficit cash shown in Step 0. Tax: the 2022 charge (7.8% effective)
  and the 2024 and 2025 cash tax carried prior-year patent-box credits (£36.1m prior-year current-tax credit in FY2022 for
  2017 to 2021); the recast uses the year's own charge. **EBITDA in the filer's own mouth:** only in the bank covenants
  ("net debt to EBITDA ... less than 3:1", AR2025 note 19), the 2021 capital policy ("leverage of approximately 0.7x EBITDA
  after taking into account lease liabilities") and the DIY Kitchens price ("approximately 8.5x LTM EBITDA"); not as a
  featured earnings figure.
- **Litigation and investigations** (sweep of AR2021 to AR2025 for "contingent liabilities", "legal proceedings",
  "litigation", "investigation", "Competition and Markets", "tribunal"): no instance found of a proceeding against the
  group; "litigation" appears only as "We charge interest at appropriate market rates on balances which are in
  litigation" (trade debtors), and "Competition and Markets Authority Order" is the audit-tender order every large UK
  company reports compliance with. The CMA approved the DIY Kitchens purchase (H1 2026 note 14).
- **Habits weighed here and carried to Q5.** The company publishes an "Analyst Consensus" page on its investor site,
  gives "Technical guidance" each half (capex, tax, interest, cost headwinds), says each update that it is "on track with
  the outlook", and sets its executives' profit targets "with reference to a combination of analyst consensus estimates,
  internal forecasts and long-term strategic goals" (AR2025 remuneration report). This is the guidance habit **[L2019-006]**,
  not yet a habit of beating declared numbers (no EPS guidance was found); weighed against **[M1994-018]** and carried.
  New "underlying" figures in H1 2026 exclude only the deal costs and are reconciled (note 12); not the waving away of
  "very real costs" **[L2016-006]**, but noted.
- **VERDICT on the accounts: WEIGHS FOR.** The statements are plain, debt-free, consistently presented, cash-backed and
  reconciled; nothing confuses **[M1995-063]** and nothing in the accounts raises suspicion. The recast earnings (owner cash
  on the tax-charge basis, Step 0 table) feed Q7. Against: the guidance and consensus habit, carried to Q5.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Andrew Livingston, chief executive since April 2018 ("He was previously the CEO of Screwfix", AR2025 board biography); Jackie
  Callaway, finance director since 2 June 2025 (Paul Hayes retired May 2025); Peter Ventress, chairman. The depot managers
  run local profit and loss accounts and are paid on them (AR2025 business model; "Depots motivated to deliver incremental
  sales (local P&L charged for revamp costs)", Introduction to Howdens 2025).
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* from FY2018 to FY2025 revenue rose
  from £1,511m to £2,418m and operating profit from £240m to £355m, through COVID and a UK kitchen market the company
  describes as contracting in 2023, 2024 and 2025; over the same years Travis Perkins went from a 7.6% margin (2021) to an
  operating loss and Nobia decided to leave the UK (Q2 table). The record is better than the field's. The capital half of
  the yardstick (Q3, Q6) is weaker: owner cash a year has not grown since FY2019 on £490m of added capital. *How they treat
  the owners:* read in the remuneration report **[M1994-009]**, Q6 Part B.
- **Tells of dishonesty sought.** Reports that dance: none found; the annual reports describe each year's market fall
  plainly ("the kitchen market contracting more than had been forecast", AR2025), reconcile every adjusted measure, and
  explain the tax credits. Mistakes: a sweep of AR2023 to AR2025 for "mistake", "disappoint" and "lessons" finds no
  admitted business mistake; the one "Disappointingly" (AR2023) reports that a deferred bonus for senior staff lapsed
  "due to challenging market conditions". A report that never names a mistake is a mild version of the taboo the rows
  distrust **[L2024-003]**; it is weighed, not judged as dishonesty. Stock-price emphasis: the company runs a share-price
  page and an analyst-consensus page, ordinary for a FTSE 100 company; no price posted as a target was found. Serial issuance:
  12.7m shares issued once, for DIY Kitchens, against continuing buybacks (Q6).
- **Habits carried from Q4.** Half-yearly "technical guidance", "on track with outlook" statements, and profit targets for
  pay set with reference to analyst consensus. Read with the integrity record: no habit of declared earnings targets met to
  the penny was found, and FY2023 profit fell (PBT £327.6m against £405.8m) and was reported as it fell. The rows'
  suspicion is of those who "consistently reach their declared targets" **[L2002-041]**; the record here is of reported
  falls, so no doubt arises on this ground.
- **Love of the business, and after the cheque.** The chief executive holds 677,357 shares outright, 656% of salary (AR2025
  shareholdings table), against a 300% requirement; most came through awards, not savings. He came from running Screwfix, a trade
  retailer, and has stayed eight years. No sale of shares by him was found in the 2026 RNS list read (the PDMR notices
  listed are share-plan items; not all were opened).
- **The pay record that bears on integrity, judged here and weighed at Q6.** The 2025 bonus paid the maximum, 200% of
  salary, on a profit range whose top ("Outperformance £325.5m") sat below the prior year's actual £328.1m; the 2023 share
  award vested at 98.4% on an "adjusted PBT" of £495.9m against a statutory FY2025 profit before tax of £344.9m, the
  committee having excluded "specific expenditure", "costs which were outside of management's control" and "the
  expenditure that was invested in driving future growth" (AR2025 pp.105 and 115 to 116). Both are disclosed in full, with
  the committee's reasons, by the non-executive directors; they show a board generous to management, not a management
  hiding numbers from owners. On the evidence they do not create doubt about honesty in the sense of **[M2013-088]**; they
  weigh heavily against at Q6 Part B.
- **VERDICT on integrity: IN** (no tell of dishonesty found in the reports, the accounts or the announcements read).
  **Ability: WEIGHS FOR** on the operating record against the field; the capital record is weighed at Q6. The business
  itself carries more of the result than the lord: "we still look to the underlying business, though" **[M1996-037]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
### Part A: the money
- **The stated policy.** "where year end cash is in excess of £250m we expect to return surplus cash to shareholders"
  (AR2021 CEO statement), restated in 2026 as returning surplus capital "while maintaining a net cash position" (H1 2026).
  Priorities in order: organic investment, a "progressive" dividend, then buybacks (buyback RNS of 3 June 2026). The
  buyback is a fixed sum set by a cash threshold; no programme names a price above which it stops **[L2016-002]**.
- **Buybacks and their prices** (equity notes of each report; cost over shares cancelled):

| Year | Spent (£m) | Shares cancelled | Average price |
|---|---|---|---|
| 2016 | 80.0 (56.3 cancelled, 23.7 to treasury) | 12,467,000 + 5.0m to treasury | about 458p |
| 2017 | 47.9 | 11,171,060 | about 429p |
| 2018 | 62.2 | 12,756,448 | about 488p |
| 2019 | 55.2 | 10,772,446 | about 512p |
| 2020 | 9.8 | 1,800,000 | about 544p |
| 2021 | 50.0 | 5,290,034 | about 945p |
| 2022 | 250.5 | 36,657,778 | about 683p |
| 2023 | 50.0 | 7,324,329 | about 683p |
| 2025 | 100.2 | 12,074,517 | about 830p |
| 2026 to 9 Oct | about 66 (estimate, Step 0 and Q7) | about 8.65m net, cancelled or to treasury | 739p to 768.5p in the latest week |

  **The no-stated-price test against the bottom of the Q7 range (written back from Q7, committed with it; the bottom is 780p):** the prices paid in 2016 to 2020 (about 429p to
  544p), 2022 and 2023 (about 683p) and 2026 (739p to 768.5p in the latest week) sit at or below the bottom of the range,
  so those purchases are read by what they did; the £50.0m of 2021 (about 945p) and the £100.2m of 2025 (about 830p) sit
  above it and weigh against, as a buyback with no stated price **[L2016-002]**. Against the all-spending bottom (640p),
  2022 and 2023 sit above it too. Every purchase since 2021 was made above the fair price of 499p.
- **Issuance and the deal.** DIY Kitchens: enterprise value £390m, "£292.5m in cash and £97.5m in Howdens' shares" at
  766p (3 June announcement), 12,725,469 new shares, valued at £101.2m at completion (about 795p). Paid mostly in cash, so
  an acquisition, not a merger under v5 Q7(c), and Q6's all-stock STOP does not apply. The stock leg was issued while the
  company was buying back its own shares at about the same price under a £100m programme it kept unchanged ("no change to
  the previously announced £100m share buyback"); the rows' own lesson on a mixed deal is "I could’ve always gone to the
  market and repurchased a bunch of stocks subsequently" **[M2014-030]**, which here happened in the same months. Value got
  against value given **[M1995-001]**: £390m for EBIT of £37m (9.5% pre-tax, about 7.1% after 25% tax) in a business
  growing revenue "over 17% per annum over the past five years", with "freehold property assets (valued at around £55m)";
  the price is about 8.5 times the seller's EBITDA. On the seller's own figures the deal is priced near the floor before
  growth; whether it earns more depends on growth the run cannot check (no DIY Kitchens accounts were read; Companies House
  filings for Ultima Furniture Systems Limited not fetched). The earlier deal, Sheridan (worktops), cost £14.6m net in 2022.
- **The retention test** **[R1995-009]**. FY2021 to FY2025: profit after tax £1,460m; returned £1,046m (dividends £595m,
  buybacks £451m); about £414m retained, and cash on hand fell a further £171m (from £515m to £345m), all of it put into
  fixed assets, stock and debtors. Market value per share: 689.6p at end-2020 (aggregator close, flagged), 788p now, about
  98p gained, against about 73p a share retained (£414m over about 570m average shares). The market leg is met, by about
  1.3 to 1; on the business leg owner cash a year has not risen (Q3), so the market leg rests on the price paid today.
- **Part A: WEIGHS AGAINST.** A cash-threshold buyback with no price, a share issue at the same time as buybacks at the
  same price, and five years of retention that bought sales but not owner cash; offset by an all-cash-funded balance sheet
  that never borrowed to buy back.

### Part B: the pay, the board and the owners
- **The bonus.** Maximum 200% of salary. FY2025 range: threshold £279m, target £310m, "Outperformance £325.5m" of PBT,
  all below FY2024's actual £328.1m; actual £344.9m paid the maximum (£1,710k to the chief executive). The committee says
  the range was set "with reference to a combination of analyst consensus estimates, internal forecasts and long-term
  strategic goals and was a change from the automatic use of the prior year PBT figure". A bar below last year's result is
  the hurdle the rows mock: "you get paid for showing up" **[M2004-097]**.
- **The share award.** The 2023 PSP (60% on PBT, £400m threshold to £484m maximum for FY2025) vested 98.4%. Statutory
  FY2025 PBT was £344.9m, below the threshold; the committee excluded "specific expenditure", "costs which were outside of
  management's control" and "the expenditure that was invested in driving future growth and profitability rather than
  into 2025 PBT", producing an "Actual Outcome: £495.9m". An award that pays in full when the measured figure falls 15%
  over the period is "heads I win, tails you lose" **[L1994-020]**, and an adjusted profit is a thing that can be "easily
  faked" **[M1996-089]**. Against the plan's defenders: pay is tied to profit and cash, which the managers control
  **[M2003-019]**; 30% of bonus is deferred into shares; a senior-staff award lapsed in 2023.
- **Totals.** Chief executive single figure £5,051k in FY2025 against £2,837k in FY2024; salary £726k to £855k (+18%) in
  2025 and £898k from April 2026. Compensation sins rank below the sin of the wrong manager **[M2007-006]**, and the
  manager here is able (Q5); the plan still transfers value on terms the owners did not get.
- **The board.** Chairman (Peter Ventress, £340k fee) separate from the chief executive, so the hardest case of
  **[L2014-026]** does not arise; non-executive fees £71k; directors' own purchases with savings not checked.
- **Part B: WEIGHS AGAINST.** Owners are told everything (the report is candid about the adjustments), but the plan's
  bar sits below last year's result and its adjusted profit rescues an award the reported profit would have failed.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business" **[R1996-018]**, held as a range
**[L2000-024]**. All arithmetic is in `scripts/value.py` (inputs `data_filed.csv`); figures in £m unless stated.

**The cash input.** Owner cash after every real cost, recast at Q4: Step 0's "tax-charge basis" column, with the pension
deficit-repair cash added back after tax because the deficit is treated as debt-like (the £16.9m deficit at 13 June 2026
is in net debt below; no contributions are now payable). **CONVENTION of this run**, rationale: deficit repair is the
paying-down of a past liability, not a cost of running the business forward, and counting both the payments and the
deficit would charge it twice. The series (FY2015 to FY2025): 127.2, 141.8, 135.9, 125.2, 172.0, 180.8, 265.8, 190.3,
121.7, 112.7, 139.6.

**The specifics, in order.**
- **(a) Cycles.** The first window year, FY2021, is aberrational **[L2005-003]** on the filer's own description: "the Company achieved
  exceptional financial results through satisfying unprecedented demand" and "a period of exceptional trading conditions"
  (AR2021). The base is the last full cycle of the series, trough FY2018 to trough FY2024, averaged over
  FY2018 to FY2023: **£176.0m**, less acquisitions in those years (£14.6m, 2022) spread over six years: **£173.5m**. The
  earlier cycle is not complete in the reports read (FY2015 is the first year), so growth is measured between the two
  halves of the eleven-year record, FY2015 to FY2019 (avg £140.4m) and FY2021 to FY2025 (avg £166.0m), six years apart:
  **2.83% a year** (the halves method of specific (b), used here because no earlier cycle can be closed; **CONVENTION of
  this run**, rationale: it is the text's own fallback where an end-to-end rate misleads). **The literal window, shown
  beside:** FY2021 to FY2025 average £166.0m, less acquisitions £163.1m; end-to-end FY2021 to FY2025 growth −14.9% a year.
- **(b) Decline.** The literal window's decline is shown beside as its bottom (below); it is not the central case because
  (a) governs an aberrational first year.
- **(c) Acquisitions.** Sheridan (£14.6m) deducted from the base as above; organic growth is not reported separately
  ("same depot" sales only), so the default pair stands. Net purchases are far below half of owner cash: not a serial
  acquirer. **DIY Kitchens, closed 23 June 2026, after the window and before the price date, is valued on its own filed
  record** (announcement of 3 June 2026: 2025 revenue £136m, EBIT £37m, revenue growth over 17% a year for five years) with
  its financing in net debt. No owner-cash figure is filed for it; **a disclosed guess, not a substitute number:** owner cash
  = EBIT after 25% UK tax, £27.75m, assuming capital spending equal to depreciation and no working-capital draw (the
  announcement cites "customer prepayment"). Its two ends: no growth, and 17% for ten years then none.
- **(d) Working capital** is inside owner cash (operating cash after working-capital movements).
- **(e) The maintenance case.** Owned depreciation is the maintenance guess (Q3, **[M1998-127]**): over FY2018 to FY2023
  capital spending averaged £86.8m and owned depreciation £39.1m, so maintenance-only owner cash is **£221.2m**. Valued at
  the sovereign, maintenance-only with no growth (£3,866m) is worth more than all spending with the 2.83% growth it bought
  (£3,793m): **the growth bought is worth less than its cost**, so by (e) the maintenance no-growth case is the top of the
  Howdens range and the growth case its bottom; "growth can destroy value" **[L2000-023]** is the finding, not an error.
  The all-spending no-growth case (£3,032m) is shown beside.
- **(f) The cap.** 2.83% is below the discount rate and needs no more than the share of sales already earned (owner cash
  was 12.7% of sales in FY2021; the growth case reaches about 9.5% of FY2025 sales by year ten even at no sales growth). DIY
  Kitchens at 17% for ten years needs no rise in its share of sales but carries its revenue from £136m to about £654m;
  that is optimistic and is kept only because the box does not turn on it (see the floor test).
- **The rate:** 5.7225% (Step 0), zero nominal growth after year ten.
- **Net debt (all-equity basis)**, at the latest filed balance sheet (13 June 2026) with the subsequent events that filing
  states: cash £332.8m, less the DIY Kitchens cash outflow of "c.£300m", plus the £240m term loan drawn, less buybacks after
  13 June estimated at about £66m (8.65m fewer voting shares between the June figures and 9 October at about 765p;
  **CONVENTION of this run**, rationale: the share count is taken at 9 October, so the cash that bought those shares must
  leave the balance on the same date); borrowings £240m; net debt **£33.4m**, plus the pension deficit £16.9m: **£50.3m**.
  Lease liabilities (£712.9m at 13 June 2026) are left out because rent is charged inside owner cash; said so.
- **Shares:** 541.95m (Step 0), including the 12.7m issued for DIY Kitchens.

**The value range (at the sovereign, all-equity basis, less net debt):**

| Case | Howdens | DIY Kitchens | Whole less net debt | Per share | Per ADS (US$, at 1.3253) |
|---|---|---|---|---|---|
| Bottom: all spending, 2.83% growth; DIY no growth | 3,793 | 485 | 4,228 | **780p** | **$41.35** |
| Top: maintenance only, no growth; DIY 17% | 3,866 | 1,842 | 5,657 | **1,044p** | **$55.33** |
| Beside: all spending, no growth; DIY no growth | 3,032 | 485 | 3,467 | 640p | $33.91 |
| Beside: literal window £163.1m, no growth / decline −14.9% (DIY no growth) | | | | 606p / 251p | |

Width 1.34 to 1 (well inside three to one). Price **788p** (ADS **US$40.02**, aggregator, flagged): inside the range, just
above its bottom.

**The floor, tested first** **[M2003-149]**. Each case valued at ten percent instead of the sovereign: bottom 430p, top
**567p**; the beside cases 362p (all spending, no growth) to 547p (all spending with growth and DIY at 17%). **No case of
the range earns ten percent at 788p.** Sensitivities written down so the close does not rest on one choice: the literal
window base with the halves growth, 524p; the as-filed cash-tax series without the pension add-back, 522p; the
all-spending base carried at the business's own sales growth of 8.5% a year (the most generous growth in the record) with
DIY at 17%, **735p**; none reaches 788p. The price would need the business to grow owner cash faster than it has grown
sales over eleven years.

**Reporting figures (a reporting convention, not a verdict or entry language; Part VII):**
- **(a) VALUE RANGE:** **780p to 1,044p** a share (**US$41.35 to US$55.33** an ADS), all-equity basis, company's own tax
  (tax charge excluding prior-year credits), against 788p (US$40.02 an ADS, aggregator, flagged).
- **(b) FAIR PRICE:** each end valued at ten percent and averaged, all-equity basis: **499p a share, US$26.43 an ADS**
  (central figure). **Equity-only, beside:** 503p, US$26.66 (owner cash after net interest: interest received on cash,
  after tax, less about £9m a year of term-loan interest the H1 2026 guidance names; no net debt deducted). The price is
  about 58% above the fair price.

**Q6's buyback test** is written back into Q6 (bottom of the range: 780p).

**VERDICT: OUT.** No case in the range earns the floor of about ten percent at 788p: "there’s just a point at which we
drop out of the game" **[M2003-149]**. Nor would it be a screamer if it did: the price sits just above the bottom of a
narrow range, the case that needs a pencil **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7** (the floor): no case of the value range earns about ten percent at 788p. Range 780p to 1,044p a share
(US$41.35 to US$55.33 an ADS) against 788p (US$40.02 an ADS); fair price 499p (US$26.43 an ADS), equity-only 503p
(US$26.66). Q1 IN, Q2 IN, Q3 UNDECIDED, Q4 WEIGHS FOR, Q5 integrity IN and ability FOR, Q6 Parts A and B WEIGH AGAINST.
Re-look is a price question, not a business one: the top of the range valued at ten percent is 567p.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down **[M1997-127]**, not weighed; the box is unchanged (operator rule 2).
- **Q8.** UK 20-year gilt 5.7225% (Bank of England, 14 Oct 2026); the fair price at ten percent is 499p.
- **Q9.** First borrowing in the eleven years read: a £240m term loan drawn 23 June 2026, maturing 31 August 2029,
  "restricted in use for the acquisition", covenants "in line with those within the RCF" (H1 2026); the RCF of £150m,
  undrawn, expiring September 2029, with covenants of net debt to EBITDA below 3:1 and EBITDA to net finance charges above
  4:1 (AR2025 note 19). The company "expects to remain in a net cash position" and states cash "greater than the amount of
  the loan" after the deal (H1 2026 going concern). Lease liabilities £712.9m at 13 June 2026, mostly depot leases. Pension
  deficit £16.9m, triennial valuation as at 31 March 2026 under way, funding arrangement to 31 May 2027. The company's own
  stress case is "the worst 12-month year-on-year fall that the Group has ever experienced". About £40m of cost headwinds
  in H2 2026 from "ongoing disruption in the Middle East" (H1 2026 technical guidance); supply from "+300 global suppliers".
- **Q10, Q12.** None found that bears; no named business of Q12's list.
- **No integrity facts are carried** (Q5 was answered IN).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 4353c815); written question by question; committed after each
      (Step 0 5f761db6; Q1 7eeb002b; Q2 0c8ab89c; Q3 225f8477; Q4 4ed1abc4; Q5 4426eae6; Q6 2f921e14; Q7 c1072a2e).
      The first Write of Step 0 replaced the template's later headings in the file; each section was then rewritten in the
      template's order and wording as it closed.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's (not checked by
      me); folding is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. One filtered listing of
      `Test Runs/` for "HWDJY" and "howden" returned nothing (declared at the top); the git log and memory lines seen are
      declared under contamination and were not used.
- [x] Every v5 id resolves (checked by `scripts/check_cites.py`); every filing fact names its document and date (no SEC
      accession exists; the ADS F-6EF accession is the brief's); every number has a filing or a CONVENTION.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy, for Howdens. **Exception, disclosed:** DIY Kitchens has
      no filed cash figure; its owner cash is a disclosed guess from its filed EBIT (Q7(c)), and the box does not turn on it
      (without DIY growth the top at ten percent is lower still). The sovereign is from the issuing authority (Bank of
      England), its series a CONVENTION of this run; aggregator quotes (price, ADS, the 2020 year-end close) are flagged.
- [x] Contrary evidence written down as found (foundations list; Q2 narrowing; Q3 increment; Q6 pay).
- [x] Not a point-in-time run; no anchor bar applies.
- [x] `tools/run.py` and `cover_shares.py` returned nothing for this name; no v4 material was used.
- [x] `python tools/check_framework.py` PASS before the final commit (run 2026-10-17); `scripts/check_cites.py` in the
      research folder: no E-ids, 65 v5 ids all in the ledger, 29 quoted fragments beside ids all found in their rows,
      0 problems; a looser pass over every id's preceding 160 characters found one id placed after a filing quote
      (L2005-003 at Q7(a)), moved to the principle it supports.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Sterling has no sovereign series in the protocol's table**, and the issuing authority's daily par yields stop at 20
years; I used the 20-year and called it a CONVENTION. A 30-year from the Bank's spot-curve archive would be a few basis
points different; the box does not turn on it. (2) **Q7(a) assumes two full cycles are visible.** With eleven years of
reports and an aberrational first window year, only one trough-to-trough cycle (FY2018 to FY2024) can be closed; the text
says growth is "measured between the averages of successive cycles" and gives no fallback when the earlier cycle is
incomplete. I borrowed (b)'s halves method and said so. A cycle-to-partial-cycle rate (FY2015 to FY2017 against FY2018 to
FY2022) would have given about 8.5% a year and a top case at ten percent of 734p, still below 788p, so the choice is
material to how the range is built though not to the box here. (3) **Cash tax
distorted by prior-year credits.** The template asks for owner cash "after the company's own tax" and does not say whether
cash tax or the charge governs when the filer says cash tax carries refunds of earlier years; I used the year's own charge
and showed the cash basis beside. (4) **A deal closed after the window "valued on its own filed record"** does not say what
to do when the record is a press-release EBIT with no cash flow; the protocol forbids a net-income proxy, so I labelled the
EBIT-after-tax figure a disclosed guess. A rule is needed. (5) **The maintenance case (e) can invert the range so that the
bottom rises** (here from 640p to 780p), which narrows the range and moves Q6's buyback test against fewer purchases; the
text treats the inversion as the finding, but the buyback test then reads against a higher bottom than the all-spending
pair would give. Both are shown. (6) **Pension deficit repair** is neither listed as a real cost nor as debt in Q7's net
debt definition; I treated it as debt-like and added the cash back, a CONVENTION of this run. (7) The template's v5 header
still points to `Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`, a test-record file; I did not open it.
