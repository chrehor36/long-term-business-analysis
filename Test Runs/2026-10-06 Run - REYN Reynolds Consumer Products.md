# Company Run: Reynolds Consumer Products Inc. (NASDAQ: REYN), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from the template before any fetch.

**POSITION NOTE, declared before any verdict:** not checked. This run is blind by instruction: `PORTFOLIO.md`, the
holding reviews, the resume-state file, the queue register and the prepped reading list were not opened. Whether the
operator holds REYN is unknown to the analyst.

**CONTAMINATION DECLARED.** (1) The directory listing of `Test Runs/` was printed once to confirm no earlier REYN file
existed (none did); it showed the names, not the contents, of the 2026-10-05 runs and holding reviews (for example ABG,
ADNT, CAG, CENT, BRK.B, BN, HRB, SONY, V). No such file was opened. (2) The session header showed five recent commit
subjects (BTU and PTEN runs closing OUT at Q2, two tool fixes, a session-state note) and a git status listing two
untracked 2026-10-06 run files (ASO, BCC). None concerns REYN or a REYN competitor; none was opened. (3) The analyst's
general knowledge of Reynolds, Clorox (Glad), Berry and Pactiv Evergreen predates the run; every fact used below is taken
from a filing with its accession, and general knowledge is used only to know where to look.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $22.23 (close 2026-10-05; aggregator quote through `tools/run.py`, flagged per operator rule 5: live quote only).
- **Shares by class** from the latest filing's cover: 210,790,982 common shares, one class, $0.001 par (10-Q for the
  quarter ended 2026-06-30, filed 2026-07-29, accession `0001628280-26-050419`; `python Screens/cover_shares.py REYN`).
- **Market cap:** $22.23 x 210.79M = **$4,686M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4), all fetched from EDGAR to `Test Runs/_research 2026-10-06 REYN/`:
  10-K FY2025 (filed 2026-02-04, `0001628280-26-005284`); 10-K FY2024 (`0001628280-25-003936`); FY2023
  (`0001628280-24-003623`); FY2022 (`0001628280-23-002692`); FY2021 (`0001564590-22-004307`); FY2020
  (`0001564590-21-005649`); FY2019 (`0001564590-20-009733`); the IPO prospectus 424B4 of 2020-01-31
  (`0001193125-20-021414`, the final form of the S-1 `0001193125-19-293392`, which was not read separately); the latest 10-Q (Q2 2026,
  `0001628280-26-050419`); the proxy (DEF 14A filed 2026-03-18, `0001628280-26-019380`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 **$477M**
  on the filed consolidated statement of cash flows (10-K FY2025, `0001628280-26-005284`), equal to the $477.0M
  `tools/run.py` transcribed from XBRL. Capital spending FY2025 $161M filed, $161.0M transcribed.
- `python tools/run.py REYN`, arithmetic lines only (its rule lines, ids and verdict words are not used; Part VII):

  | FY | OCF | SBC | D&A | capex | OCF-SBC-capex | OCF-SBC-D&A |
  |---|---|---|---|---|---|---|
  | 2023 | 644 | 14 | 124 | 104 | 526 | 506 |
  | 2024 | 489 | 19 | 129 | 120 | 350 | 341 |
  | 2025 | 477 | 21 | 135 | 161 | 295 | 321 |

  Five-year window (FY2021 to FY2025) per the tool: OE capex mean 284.4, OE D&A mean 292.4 ($M). The tool's balance-sheet
  table (nine year-ends) is read at Q4 against the filed statements. These are not yet owner cash: the factoring of
  receivables, the working-capital swings of 2021 to 2023 and the interest burden are read at Q4 before any figure is
  carried.

## THE FOUNDATIONS (not a gate)
Three bear on this name. **A share is a business:** the question is whether the buyer would be content to own a small
slice of a foil, trash-bag and paper-plate maker controlled 73.8% by one family holder "if the market closed for five
years" **[M1997-109]**; nothing below turns on the quotation. **Who is paid to tell you:** the only long-form account of
this business written for buyers is the 2020 prospectus, and its author was the seller. The net IPO proceeds (about
$1,161M) repaid a one-day facility "incurred as part of the Corporate Reorganization" with the seller's group, and a new
$2,475M term loan was put on the company "to settle certain related party borrowings" owed to that group (424B4
`0001193125-20-021414`, "Use of Proceeds"). "don’t ask the
barber whether you need a haircut" **[M2011-083]**: the prospectus's market-share and brand claims are read below only as
the filer's claims and set against the volume figures. **Margin of safety:** if the case needs a pencil, "it’s too close
to think about" **[M1996-084]**. The index fork: the buyer is treated as a professional doing the work, so the questions
are used **[M2008-055]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. One customer and its affiliate take **48%** of net revenue in each of 2023, 2024 and 2025 (10-K FY2025
   `0001628280-26-005284`, segment note; Customer A 31% and Customer B 17%, "affiliated entities"). The filer's own
   risk factor: "Many of our customers are large and possess significant market leverage, which results in significant
   downward pricing pressure and can constrain our ability to pass through price increases" (same 10-K, Item 1A).
   Found later in the run and written here: the earlier filings name the pair. "Walmart accounted for 28%, 27% and 26%
   and Sam’s Club accounted for 12%, 12% and 12% of our total revenue in fiscal years 2018, 2017 and 2016" (424B4
   `0001193125-20-021414`); 30% and 13% in 2019 (10-K FY2019 `0001564590-20-009733`, which also says Walmart sales are
   "concentrated more heavily in our Hefty Waste & Storage segment" and Sam's Club in tableware, the same description
   the FY2025 10-K gives of the unnamed Customers A and B). The dependence has risen, from 38% (2016) to 43% (2019) to
   48% (2023 to 2025).
2. The company was born carrying the controller's debt: $2,475M term loan at the IPO, proceeds to the seller's group
   (424B4). Net debt at 2025 year-end is still about $1,439M ($1,586M term loan less $147M cash; 10-K FY2025, Note on
   debt and balance sheet).
3. Price against volume in foil: FY2022 Reynolds Cooking & Baking price **+12%**, volume/mix **-14%** (10-K FY2022
   `0001628280-23-002692`, "Components of Change in Net Revenues"); Q2 2026 the renamed foil segment price **+19%**,
   retail volume **-8%**, non-retail **-5%** (10-Q Q2 2026 `0001628280-26-050419`).
4. Foam tableware is shrinking under "foam-related consumer behavior and regulatory pressure" (10-K FY2024
   `0001628280-25-003936`); Hefty Tableware revenue fell from $1,000M (FY2022) to $850M (FY2025) and its volume fell 11%
   in FY2025 and 14% in Q2 2026.
5. Adjusted EBITDA (the filer's figure, not an earnings figure here) has not grown: segment adjusted EBITDA $666M in
   2017, $668M in 2019, $761M in 2025 (10-K FY2019 `0001564590-20-009733` and FY2025, segment reconciliations), while
   cumulative price taken from 2020 to 2025 is about +25% (the six "Components of Change" tables compounded:
   -1%, +8%, +13%, +2%, -1%, +3%).
6. The chief executive of the IPO years left at the end of 2024; the successor had joined as CFO in October 2023 from
   SunOpta, with no operating record at the company before that (8-K `0001193125-24-246994`).
7. Found at Q5: part of what the company sells is made by another company, a former sister company now independent. It "purchased products from Pactiv, primarily
   tableware", $245M in 2025, and sells Pactiv foil and foil containers, $94M, under supply agreements that "expire over
   a variety of periods through December 31, 2027" (DEF 14A `0001628280-26-019380`, Certain Relationships). Pactiv was a
   sister company under the same controller until 2025-04-01, when it was sold "to an unrelated party" (same).

## THE STANDING RULE
The buyer's conduct, not the target's: the run assumes a cash purchase from the buyer's own funds, sized so that a 50%
fall in the quotation changes nothing the buyer needs, since "borrowed money has no place in the investor's tool kit"
**[L2014-005]** and the buyer is "never going to risk what we have and need for what we don’t have and don’t need"
**[M2012-081]**. On those terms the standing rule is satisfied; the target's own debt is weighed at Q9, not here.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding means "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" and "how the industry will develop and where the company will stand within the
  industry" **[M2012-065]**. The product is plain (aluminium foil, parchment and wax paper, disposable pans, trash and
  food-storage bags, plastic wrap, foam and paper plates and cups, cutlery, store-brand versions of most of them, and
  Fresh-Lock and Slide-Rite zip closures sold to other packers; 10-K FY2025 Item 1). What has to be foreseen is the
  economics: "I understand the economic dynamics of the industry. [...] are there competitive moats? Is there ease
  of entry?" **[M2011-014]**.
- **The key variables and how predictable they are** **[M1998-044]**: (1) unit demand in household foil, bags and
  disposable tableware, which the filer calls a "mature and highly competitive" U.S. market (10-K FY2025 Item 1,
  Competition) and which moved within a few percent a year from 2019 to 2025 except the 2020 stay-at-home spike
  (volume/mix +9%, 10-K FY2020 `0001564590-21-005649`) and its give-back; (2) the spread between the price charged and
  the cost of aluminium and resin, which the filings show squeezed in 2021 and 2022 and restored by 2023 (Q2 below);
  (3) the terms the largest retailers allow, with one group at 48% of revenue; (4) the slow regulatory decline of foam
  and some single-use plastics. Variables (1), (2) and (4) are slow and visible in the past statements, which "will tell
  me the information that’s useful to me in making a judgment about what the future financial statements are going to
  look like" **[M2008-033]**; this is the inverse of a business that changes fast **[M1999-063]**. Variable (3) is the
  one with a wide error: it is knowable in kind (the filer names it) but not in size.
- **Would the insiders write it down?** **[M2000-105]**. A category manager at a large grocer would write down where
  U.S. foil, trash-bag and paper-plate demand will be in ten years within a narrow band; the forecast is about household
  consumption and retailer terms, not technology **[M2023-030]**. No chip, no network, no patent cliff.
- **Can I name the winner, not just the industry?** **[M2012-067]**. In foil yes: the filer claims "greater than 50%
  market share in most of its categories" and "no significant branded competitor" (10-K FY2025 Item 1). In bags the
  winner is shared with Glad (Clorox) and store brands; in foam tableware the category itself is shrinking. Whether the
  winner keeps its terms against the retailer is Q2's question, not Q1's: Q1 asks whether it can be judged at all.
- **Doubt.** "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**. The
  doubt here is not about what the business is or how it makes money; it is about how much of the margin the retailer
  will leave, which is a castle question and is carried to Q2. Slow change remains change, "slow change can be much
  harder to perceive" **[M2014-038]**: foam and plastics regulation is the slow change, and it is named.
- **VERDICT: IN.** A mature household-consumables maker whose key variables are visible in eight years of filings and
  whose ten-year economics an insider would write down **[M2012-065]**, **[M2008-033]**, **[M2000-105]**. Filing facts:
  10-K FY2025 `0001628280-26-005284` Item 1 and segment note; the six "Components of Change" tables FY2020 to FY2025.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. The business is four castles of
different strength, and they are read one by one before the whole.

**The span table** (segment revenue $M / segment adjusted EBITDA $M / margin; the filer's segment measure, used here only
as a comparable operating margin across years, never as earnings; 10-K FY2019 `0001564590-20-009733` for 2017 to 2019,
FY2020 `0001564590-21-005649`, FY2021 `0001564590-22-004307`, FY2023 `0001628280-24-003623`, FY2025
`0001628280-26-005284` for the recast 2023 to 2025):

| Segment | 2017 | 2019 | 2020 | 2021 | 2022 | 2023 | 2025 |
|---|---|---|---|---|---|---|---|
| Reynolds Cooking & Baking (foil) | 1,068 / 251 / 23.5% | 1,076 / 209 / 19.4% | 1,159 / 254 / 21.9% | 1,314 / 255 / 19.4% | 1,287 / 142 / 11.0% | 1,237 / 177 / 14.3% | 1,259 / 219 / 17.4% |
| Hefty Waste & Storage (bags) | 638 / 149 / 23.4% | 709 / 190 / 26.8% | 818 / 236 / 28.9% | 884 / 173 / 19.6% | 946 / 207 / 21.9% | 960 / 265 / 27.6% | 1,011 / 279 / 27.6% |
| Hefty Tableware | 731 / 183 / 25.0% | 751 / 178 / 23.7% | 763 / 170 / 22.3% | 815 / 137 / 16.8% | 1,000 / 134 / 13.4% | 984 / 177 / 18.0% | 850 / 133 / 15.6% |
| Presto Products (store brand) | 531 / 83 / 15.6% | 511 / 91 / 17.8% | 533 / 98 / 18.4% | 564 / 69 / 12.2% | 604 / 96 / 15.9% | 594 / 112 / 18.9% | 628 / 130 / 20.7% |
| Segment total | 2,957 / 666 / 22.5% | 3,032 / 668 / 22.0% | 3,263 / 758 / 23.2% | 3,556 / 634 / 17.8% | 3,817 / 579 / 15.2% | 3,756 / 731 / 19.5% | 3,721 / 761 / 20.5% |

**Price against volume, compounded from the six "Components of Change in Net Revenues" tables FY2020 to FY2025**
(10-Ks above plus FY2022 `0001628280-23-002692` and FY2024 `0001628280-25-003936`): foil price **+27%**, volume/mix
**-6%**; bags (Hefty Waste & Storage) price **+20%**, volume/mix **+16%**; tableware price **+34%**, volume/mix **-16%**;
Presto price **+21%**, volume/mix **+1%**; the whole company price about **+25%**, volume/mix about **-4%**. Arithmetic
from the filed percentages, rounded as the filer rounds.

**The tests.**
1. **Key factors and how permanent** **[M1995-038]**. The filer names brand recognition, price, quality and innovation as
   the grounds of competition, its "category captain" role with retailers, and making both the brand and the store brand
   ("Our mix of branded and store brand products is a key competitive advantage", 10-K FY2025 Item 1). Reynolds Wrap has
   "been the top trusted brand in the consumer foil market for over 75 years" with "greater than 50% market share in most
   of its categories" and "no significant branded competitor" (same). These are the filer's claims, read against the
   numbers below.
2. **Would it stand without the lord?** Yes. The chief executive changed on 2025-01-01 (8-K `0001193125-24-246994`) and
   nothing in the segment figures moved with it; the business is aisles and plants, not a person.
3. **The money test** **[M2011-015]**. Bags: the best-funded attacker in the aisle already exists. Clorox's Glad, with
   Procter & Gamble's research behind it under a venture agreement until January 2026, lost ground to Hefty: Clorox's
   Household segment volume fell 7% in its FY2019 "primarily driven by lower shipments of Glad bags and wraps, mainly due
   to wider price gaps compared to a year ago and distribution losses" (Clorox 10-K FY2020 `0000021076-20-000016`,
   annual-report section); global bags and wraps fell from 18% to 15% of Clorox's consolidated net sales between its
   FY2018 and FY2020 and stayed at 15% through FY2026, and the U.S. Bags and Wraps unit from 14% (FY2018) to 11% (FY2024
   to FY2026) (Clorox 10-K FY2026 `0000021076-26-000034`, Note 22), while Hefty Waste & Storage revenue rose
   from $696M (2018) to $1,011M (2025). The fair value of P&G's 20% of the global Glad business was estimated at $610M at
   June 2020 (Clorox 10-K FY2020, Note 8) and was bought for $476M in March 2026 (Clorox 10-K FY2026). The attacker with
   money has been losing. Foil: the filer reports no significant branded competitor; the attacker is the store brand,
   which Reynolds itself supplies in part. Tableware: the attacker is not a rival but the foam bans and the shopper.
4. **Pricing power and the agony before a rise** **[M2005-020]**, **[M2005-019]**. The company raised price about 25%
   from 2020 to 2025 while volume/mix fell about 4%, and the segment margin, crushed from 23.2% (2020) to 15.2% (2022) as
   resin and aluminium ran ahead of price, came back to 20.5% by 2025. That is the pattern the rows describe:
   "over time the businesses with strong competitive positions manage to pass through increases in raw material costs
   [...] But you get these temporary situations where, sometimes, the costs are increasing faster" **[M2005-017]**. In
   bags the stronger form holds: price +20% and volume +16% over the span, which is to "charge more for a product and
   maintain or increase market share against wellentrenched, well-known competitors" **[M2000-031]**. Foil is the weaker
   form: price +27% with volume -6% over the span, -14% volume/mix on +12% price in 2022 (including non-retail), and in
   Q2 2026 +19% price against retail volume -8% (10-Q `0001628280-26-050419`; the release blames "in part" promotional
   timing, EX-99.1 to 8-K `0001628280-26-050381`). Sales did not "fall off a cliff" **[M2005-019]**, but this is the
   warning of **[M2001-088]**: "if you establish too wide a differential between Coke and a private label product, you
   will change consumption patterns somewhat."
5. **Unit volume and share of mind** **[M1999-054]**. Whole-company volume is about flat to slightly down since 2019; the
   filer's own claims of share have narrowed year by year, which is the plainest evidence on this test:
   - revenue from products that are #1 in their category: "over 65%" (424B4 `0001193125-20-021414`; 10-Ks FY2022 and
     FY2023) to "Over 50%" (10-Ks FY2024 and FY2025);
   - Reynolds foil "greater than 50% market share in virtually all of its categories" (10-Ks FY2019 to FY2021) to "in
     most of its categories" (10-Ks FY2022 to FY2025);
   - Hefty "#1 branded market share" in outdoor trash bags and slider bags (10-K FY2021), then large black and slider
     (FY2022, FY2023), then large black only with "#2" in slider bags (FY2024) and "#2" in food storage bags (FY2025);
   - against that, the 10-Q of Q2 2026 claims the company is "the largest U.S. trash bag manufacturer by dollar share"
     (an internal estimate from Circana data), and the chief executive says it "held or gained share across the majority
     of our categories" (EX-99.1, July 2026); the same release discloses "previously communicated private label
     distribution losses" in trash bags.
6. **The low-cost position.** No filing gives unit costs against rivals; the filer says competitors "outside the United
   States [...] may have lower production costs" (10-K FY2025 Item 1A). Not found; not counted for or against.
7. **The brand in the customer's mind, and against the retailer** **[M2015-038]**, **[M2001-090]**, **[M2019-041]**. One
   customer group, named in the earlier filings as Walmart and Sam's Club (contrary evidence 1), takes 48% of revenue,
   up from 38% in 2016, and sells its own store brands; 39% of Reynolds's retail revenue is store brand
   (10-K FY2025 MD&A). The rows' warning is exact: "to the extent that people trust Costco or Walmart more than they [...]
   trust the brand, then the value of having the brand moves over to the retailer from the product itself"
   **[M2001-090]**. The evidence over six years of heavy inflation is that the retailer has not taken the margin (20.5% in
   2025 against 22.0% in 2019, with the same 48% customer), and that Reynolds is paid to make the retailer's store brand
   as well. The hedge cuts both ways: it is also proof that much of the shelf buys on price. For scale, Clorox, selling
   into the same aisles, reports its largest customer, Walmart and affiliates, at 25% to 27% of net sales (Clorox 10-Ks
   FY2020 and FY2026, segment note): Reynolds depends on one retailer about twice as heavily as the rival brand does.
8. **Would the customer still choose it over the low bid?** **[M2017-009]**. For foil and branded bags the share figures
   say yes for most buyers; for the 39% store-brand business the customer is the retailer and the product is bought on
   contract terms, "one year or multi-year agreements" (10-K FY2025 Item 1), and a contract can be lost (the trash-bag
   private-label losses of 2026; "the exit of certain low margin store branded business" in 2019, 10-K FY2019).
9. **Ask the competitors** **[M1999-130]**. Their own filings answer: Glad's owner reports lost distribution on price gaps
   and a falling fair value; Berry, a film maker that also makes institutional can liners and retail trash bags (BERY 10-K
   FY2020, Item 1), earns 11% to 14% operating margins in that segment; Pactiv Evergreen, the former sister company,
   earns 13% to 18% adjusted EBITDA in foodservice (competitor row below).
10. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Bags widening (margin 23.4% to 27.6%, revenue +58% from
    2017, Glad losing). Presto widening (15.6% to 20.7%). Foil narrowing in margin (23.5% to 17.4%) and in the filer's own
    share claim ("virtually all" to "most", 10-Ks FY2021 and FY2022). Tableware narrowing in every measure (25.0% to 15.6%, volume -16%, retail
    volume -14% in Q2 2026 and -8% excluding foam).
11. **What could destroy, modify or reduce it** **[M2000-014]**: bans on foam and some single-use plastics (already
    visible in tableware); the largest customer moving its store-brand contracts or squeezing terms; imported foil and
    bags. None of these is a technology that makes the product obsolete; foil and trash bags will be bought in 2036.

**The return the castle protects** **[M2007-023]**, **[L2007-004]**. Net tangible operating capital at 2025 year-end is
about $848M (total assets $4,936M less goodwill $1,895M, intangibles $943M and cash $147M, less non-debt liabilities of
$1,103M, being total liabilities $2,683M less the $1,580M carrying value of the term loan; 10-K FY2025 balance sheet and
Note 6). Operating profit before interest and tax in 2025 is about $479M (income before tax $393M plus net interest
$86M; 10-K FY2025 income statement). About 56% pre-tax on the tangible capital the business needs. A commodity converter does not earn that;
Berry's comparable segment earned $317M on $2,006M of segment assets in FY2020, about 16% (BERY 10-K FY2020
`0001140361-20-026326`, segment note). The castle's existence is not in doubt; its width in foil and tableware is.

**The competitor row** (same metric where the filers allow; operating margin on segment sales):

| Company, segment (accession) | Metric | Over the span |
|---|---|---|
| REYN Hefty Waste & Storage (10-K FY2025 `0001628280-26-005284`) | segment EBITDA less segment D&A, % of segment sales | 2023 25.6%, 2024 26.1%, 2025 25.6% |
| CLX Household: Glad, Kingsford, cat litter (`0000021076-20-000016`, `0000021076-23-000037`, `0000021076-26-000034`) | earnings before tax to FY2020, segment adjusted EBIT after, % of sales | FY2018 20.8%, FY2019 19.0%, FY2020 19.3%, FY2021 18.9%, FY2022 11.8%, FY2023 14.7%, FY2025 16.2%, FY2026 10.7% |
| BERY Engineered Materials, renamed Flexibles (`0001140361-20-026326`, `0001140361-24-047881`) | operating income, % of sales | FY2018 13.9%, FY2019 12.5%, FY2020 13.6%, FY2022 9.4%, FY2023 11.5%, FY2024 11.2% |
| REYN Hefty Tableware (as above) | segment adjusted EBITDA, % | 2017 25.0% falling to 2025 15.6% |
| PTVE Foodservice (`0001564590-21-008652`, `0000950170-25-026104`) | segment adjusted EBITDA, % | 2018 14.9%, 2019 15.6%, 2020 13.3%, 2023 18%, 2024 17% |
| Kirkland and other store brands | no filing breaks out the maker's margin | not obtainable from primary documents |

Clorox's segment mixes Glad with charcoal and litter and is measured after depreciation; Reynolds's Hefty figure
excludes about $94M of unallocated corporate cost. The comparison is of order, not of decimals: the branded bag maker
earns about double the film converter and well above Glad's segment across the whole span; Hefty Tableware has fallen to
the level of a foodservice converter.

**VERDICT: IN.** The castle stands where the money is: bags and the store-brand bag business (together 44% of 2025
segment revenue and 54% of segment EBITDA) show price and volume rising together against a funded rival that lost ground
**[M2000-031]**, and the whole business restored its margin after the 2021 and 2022 cost surge while keeping the same
largest customer **[M2005-017]**; it earns about 56% pre-tax on its tangible capital **[M2007-023]**. It is not shown
open on the evidence, so it is not OUT **[M2011-015]**; its future can be judged, so it is not TOO HARD **[M2000-019]**.
What the evidence shows against it is carried forward as a narrowing, not hidden **[M1999-108]**: foil margin and the
foil share claim narrowing, tableware filling in, a 48% customer, and the filer's own claims shrinking from "over 65%"
to "Over 50%" of revenue at #1 (10-Ks FY2023 and FY2024). These go into "how sure" at Q7 and into the growth input, which they hold to about
nothing. *(This is the closest call in the run. An analyst who weighted the foil and tableware narrowing above the bag
evidence would write TOO HARD here; the file says so rather than hide it.)*

## Q3: HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, **[M2011-060]**. Goodwill ($1,895M) and the trade names
  ($943M) are what the Hart group paid when it assembled the business (the prospectus names "RGHL’s acquisition of Pactiv in 2010", 424B4 `0001193125-20-021414`), not capital the business needs.
  On the tangible capital, about $848M at 2025 year-end (Q2), the business earned about $479M before interest and tax,
  about 56%. The same figure in 2020: tangible operating assets $1,439M (total assets $4,722M less goodwill $1,879M,
  intangibles $1,092M, cash $312M) less non-debt liabilities $874M (total liabilities $3,107M less debt $2,233M), about
  $565M, against operating profit before interest and tax of about $586M (income before tax $516M plus interest $70M;
  10-K FY2020 `0001564590-21-005649`, balance sheet and income statement). The return on what the business needs is
  very high in both years. Read with care **[L1994-009]**: 2020 was the stay-at-home peak, and the 2025 figure is the
  more ordinary year.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Capital spending FY2021 to FY2025 totals
  $654M against depreciation and amortization of $614M (10-K cash-flow statements; `tools/run.py` transcription checked
  at FY2025), about 1.07 times D&A and about 3.5% of sales. The filer gives no split between maintenance and growth
  spending (searched: the words maintenance and growth beside capital expenditures in the FY2025 10-K and the Q2 2026 10-Q;
  no instance found). The analyst's guess, as the rows ask **[M2000-144]**: maintenance about equal to D&A, "Every year
  we spend amounts equal to our depreciation charge simply to stay in the same economic place" **[L2000-035]**, since
  volume did not grow and the excess over D&A is small. Spending is rising: $161M in 2025 (Hefty Waste & Storage
  $48M against $11M to $19M in the two years before, segment note) and $101M in the first half of 2026 (10-Q).
- **What the added capital earned** **[M2001-019]**. Between 2020 and 2025 tangible operating capital rose by about
  $283M (from about $565M to about $848M), most of it working capital swollen by a price level 25% higher (inventory
  $419M to $584M, receivables $292M to $355M; tool table, checked against the filed 2020 and 2025 balance sheets).
  Operating profit before interest and tax fell from about $586M to about $479M. On the 2019 base, before the
  stay-at-home year, segment adjusted EBITDA was $668M against $761M in 2025, and consolidated revenue rose from $3,032M
  to $3,721M almost entirely on price. The added capital earned close to nothing in real terms: it was the cost of
  standing still in an inflation, and the rows' test is whether a business "retains its earning power in real dollars without commensurate
  investment" **[M2005-049]**: here earning power in real dollars did not keep up, though the investment was small.
- **The growth arithmetic and its caps** **[M2003-120]**, **[M1994-080]**. The business does not need capital to grow
  because it is not growing; volume is about flat since 2019 (Q2). It is the first of the speakers' grades on capital
  ("gives you more and more money every year without putting up anything to get it, or very little" **[M1998-081]**)
  only in its low need for capital; it does not give "more and more money" **[M1998-081]**. Nothing here supports carrying a growth rate
  above inflation, and the evidence of 2019 to 2025 supports less.
- **WEIGHS FOR, narrowly.** Very high return on the tangible capital the business needs and capital spending near
  depreciation **[M2010-090]**, **[M2011-060]**; against it, no reinvestment opportunity at those returns and an added
  $283M of capital that bought no added profit **[M2001-019]**, **[M2003-120]**. (The "little or no debt" criterion is
  applied at Q9.)

## Q4: DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, nine year-ends, before the income account** **[M2025-032]** ($M; 2017 and 2018 from the
  prospectus, 424B4 `0001193125-20-021414`; 2019 and 2020 from 10-K FY2020 `0001564590-21-005649`; 2021 to 2025 from
  each year's 10-K, the `tools/run.py` table checked against the filed 2020 and 2025 statements):

  | Year-end | Total assets | Equity | Cash | Receivables | Inventory | Goodwill | Intangibles | Debt (external / related party) | Retained earnings |
  |---|---|---|---|---|---|---|---|---|---|
  | 2017 | 5,911 | -1,298 | n/r | n/r | n/r | n/r | n/r | 2,049 / 3,927 (+367 accrued interest) | parent deficit |
  | 2018 | 6,421 | -1,027 | n/r | n/r | n/r | 1,879 | n/r | 2,030 / 3,950 (+576 accrued interest) | parent deficit |
  | 2019 | 4,160 | -818 | 102 | 13 | 418 | 1,879 | 1,123 | 2,011 / 2,214 (+18) | parent deficit |
  | 2020 | 4,722 | 1,615 | 312 | 292 | 419 | 1,879 | 1,092 | 2,233 / 0 | 233 |
  | 2021 | 4,812 | 1,756 | 164 | 316 | 583 | 1,879 | 1,061 | 2,112 / 0 | 365 |
  | 2022 | 4,929 | 1,868 | 38 | 348 | 722 | 1,879 | 1,031 | 2,091 / 0 | 431 |
  | 2023 | 4,780 | 1,983 | 115 | 347 | 524 | 1,895 | 1,001 | 1,832 / 0 | 537 |
  | 2024 | 4,873 | 2,142 | 137 | 337 | 567 | 1,895 | 972 | 1,695 principal / 0 | 694 |
  | 2025 | 4,936 | 2,253 | 147 | 355 | 584 | 1,895 | 943 | 1,586 principal / 0 | 802 |

  (n/r: not read; the prospectus balance-sheet extract read for this run gives liabilities and equity for 2017 and 2018,
  not every asset line.)

  **What moved and why.** (1) Before the IPO the business was a carve-out carrying its parent group's debt: about $6.0B
  of external and related-party borrowings plus accrued related-party interest against total assets of $5.9B to $6.4B,
  so equity was negative. The pre-IPO income statements therefore carry related-party interest ($280M in 2018, $209M in
  2019, XBRL transcription) and their net income is not comparable with later years. (2) The IPO of February 2020 turned
  the related-party debt into paid-in capital ($1,381M) and a new external term loan; external debt has since fallen from
  $2,233M to $1,586M. (3) Goodwill and trade names are flat or amortizing slowly ($1,123M to $943M of intangibles); no
  write-down in any year read, and a $6M acquisition in 2023 is the only purchase (XBRL
  PaymentsToAcquireBusinessesNetOfCashAcquired). (4) Receivables were $13M in 2019 because before the IPO they were sold
  to a parent-group special-purpose entity (10-K FY2021, accounting policies); rebuilding them to $292M in 2020 absorbed
  operating cash once. Since then receivables have stayed at 8.9% to 9.5% of sales. (5) Inventory went from 12.8% of
  sales (2020) to 16.4% (2021) and 18.9% (2022), then back to 14.0% (2023) and 15.7% (2025): a build in the cost surge and
  a release after it, still above the 2019 and 2020 level. "inventories look out of line, you know, with sales" is a tell
  the rows name **[M1995-064]**; here the swing is explained by the filer (material costs, then destocking) and has
  reversed, so it is read as the cost cycle, not as a tell. (6) Accounts payable rose from $185M plus $41M related-party
  payables (2020) to $387M (2025), about 9.9% to 13.8% of cost of sales; the supply-chain-finance programme behind some of
  it is small ($9M confirmed at 2025 year-end, 10-K FY2025 Liquidity). Payables supplied about $160M of the five years'
  operating cash; that is a one-time source, not a repeating one. (7) Retained earnings rose $569M from 2020 to 2025
  while $960M of dividends were paid out of $1,533M of net income. What the balance sheets say: a plain business with a
  shrinking debt and no hidden asset build. What they cannot say: how much of the $1,895M goodwill is still earned, a
  question the trade-name and goodwill tests pass each year (10-K critical accounting estimates).
- **The real costs** **[L2015-004]**, **[L2021-003]**. Depreciation and amortization $109M to $135M a year is matched by
  capital spending (Q3). Stock pay is small and rising ($4M in 2021 to $21M in 2025) and is deducted below. The
  "one-time" items: IPO and separation costs of $31M (2020), $14M (2021), $12M (2022), none in 2023 and 2024, then $53M in
  2025 (debt refinancing $13M, "costs to execute strategic initiatives" $25M, chief-executive transition $15M) (10-K
  FY2022 and FY2025 reconciliations). Over six years they average about $18M a year, small against pre-tax income of
  $393M to $516M; they recur in kind, so they are left in the cash figure, which operating cash already does. Amortization
  of trade names (about $30M a year) is a charge the rows allow to be added back where the asset does not deplete
  **[L2015-004]**; the brands are not visibly depleting, so the D&A basis of owner cash below leaves it as a margin.
- **EBITDA in the filer's own mouth.** The segment measure is "Adjusted EBITDA", the release headlines "Adjusted EBITDA"
  and "Adjusted EPS" beside GAAP net income and EPS, and guidance gives net income, EPS and adjusted EBITDA (EX-99.1 to
  8-K `0001628280-26-050381`). The rows call the figure "utter nonsense" **[M1998-086]** and count the purchases where
  "people are talking about EBITDA" as "about zero" **[M2002-026]**. Against that, in this filer's mouth: GAAP net income
  is printed first, 2026 guidance shows adjusted net income equal to net income, depreciation is deducted in the bonus
  measure (adjusted EBIT) and the share awards run on adjusted EPS and adjusted free cash flow (DEF 14A
  `0001628280-26-019380`, Compensation Discussion). A management "preoccupied with accounting considerations" is "a
  negative" but not "a total exclusionary factor" **[M1994-018]**; adjusted per-share figures featured "makes us
  nervous" **[L2016-006]**. No make-the-numbers habit was found (2021 and 2022 earnings fell openly with the reasons
  stated), so the two-tell line of the framework's Q4 convention is not reached.
- **Owner cash after every real cost, recast** (operating cash, which is already after cash interest and cash tax and
  after the "one-time" items, less stock pay, less capital spending; filed cash-flow statements, never net income):

  | FY | Operating cash | Stock pay | Capex | Owner cash (capex basis) | D&A | Owner cash (D&A basis) |
  |---|---|---|---|---|---|---|
  | 2020 | 319 | 5 | 143 | 171 | 99 | 215 |
  | 2021 | 310 | 4 | 141 | 165 | 109 | 197 |
  | 2022 | 219 | 5 | 128 | 86 | 117 | 97 |
  | 2023 | 644 | 14 | 104 | 526 | 124 | 506 |
  | 2024 | 489 | 19 | 120 | 350 | 129 | 341 |
  | 2025 | 477 | 21 | 161 | 295 | 135 | 321 |
  | **Five-year mean 2021 to 2025** | | | | **284.4** | | **292.4** |

  The five-year window holds both the inventory build of 2021 and 2022 and its release in 2023, so it is internally
  balanced; a three-year window (2023 to 2025, mean $390M) would take the release without the build and is not used
  **[L2005-003]**. The window does hold one abnormal stretch, the 2021 and 2022 cost squeeze, when price lagged resin
  and aluminium; whether that is abnormal or simply this business's cycle is itself a finding (it is the third squeeze
  the filings describe, after 2018's cost rise and before 2026's aluminium rise), so a whole-cycle variant is carried
  to Q7 rather than a cleaned figure. Payables supplied about $32M a year of the mean (point 6 above).
- **VERDICT on confusion: IN.** The accounts are plain and the costs are counted; the carve-out history is explained in
  the filings themselves **[M2025-032]**. **WEIGHS AGAINST, mildly**: EBITDA and adjusted EPS featured in the releases and
  guidance **[M2002-026]**, **[L2016-006]**, and an operating cash series that needs a five-year window to be read at all.

## Q5: WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The two yardsticks** **[M1994-008]**. How well they run it, against the hand dealt: the hand of 2021 and 2022 was
  the largest material-cost rise in the filings' span ($391M in 2021 and $333M in 2022, 10-Ks FY2021 and FY2022); management lost 8 points of segment margin and
  recovered most of it in 2023 by price, keeping volume within a few percent (Q2). Against the competitor's hand in the
  same aisle, Clorox's Household segment fell about as far (19.3% to 11.8%) and by FY2026 stood lower, at 10.7%
  (competitor row, Q2). How they treat owners:
  read from the proxy, "see how they treat themselves versus how they treat the shareholders" **[M1994-009]** (below).
- **Who runs it.** The chief executive since 2025-01-01 joined as CFO in October 2023, after CFO roles at SunOpta and
  Claire's Stores and treasury roles at Sears Holdings (8-K `0001193125-24-246994`); the CFO since 2025 is an internal
  finance promotion; the chief legal officer left under a separation agreement of May 2025 (10-K FY2025 exhibit 10.32)
  and three of the five named officers of 2025 joined that year (DEF 14A, Summary Compensation Table notes). The operating
  record of the present team at this company is about eighteen months. Ability: not yet shown here, neither for nor
  against; the business's own record belongs to the predecessor.
- **The controller.** Graeme Hart's PFL owns 73.8% (155,455,000 shares; DEF 14A, beneficial ownership) and under the
  stockholders agreement nominates every director while it holds 50%; four of nine directors are Rank officers or family
  (Cole, Golding, Hugli, and Hawkesby, Hart's son-in-law). The company is a Nasdaq "controlled company" and has "elected
  not to comply" with the majority-independent board and independent compensation committee rules (DEF 14A, Corporate
  Governance). The record of the controller's dealings with the company: (a) it took the IPO proceeds and put a $2,475M
  term loan on the company to settle borrowings owed to its own group (424B4); (b) until 2025-04-01 the company bought
  $399M, $381M and $332M a year of goods from Pactiv Evergreen, then controlled by the same holder, and paid it $54M,
  $37M and $28M of freight (10-K FY2024 `0001628280-25-003936`, Note 17), on terms "negotiated on what we believe to be
  an arm’s-length basis" (DEF 14A, Certain Relationships); (c) it receives $143M a year of dividends (10-K FY2024, Note
  17). All of it is disclosed, in the filings, in numbers.
- **The tells of dishonesty** (Q5's list). Too good to be true: the filer has narrowed its own share claims year by
  year rather than inflate them (Q2, test 5), which is the opposite tell. Reports that dance: no restatement in the
  years read, legal proceedings "not significant" (10-K FY2025 Item 3). Mistakes named in the reports: 2022's
  foil margin is put down to "equipment reliability and related inefficiencies" (10-K FY2022), plainly. Stock price
  fixation: no buyback and no split; a guidance-beating record was not searched for beyond the years read. "everybody mouths the integrity, even when it’s lacking"
  **[M2010-069]** is a warning, not a finding; no instance of a misleading figure was found in the documents read.
- **The rule on doubt.** "If you’ve got doubts, forget it." **[M2013-088]**; "trustworthiness is more important than the
  brains" **[M2015-047]**. The doubt that the record supports is about whose interest a controlled board serves, which is
  Q6, Part B, not about honesty: no false statement, concealment or self-dealing outside the disclosed contracts was found.
  For a marketable stake the reading is from documents, not meetings **[M2007-081]**, and the documents read straight.
- **VERDICT on integrity: IN** **[M2013-088]**, **[M2015-047]**, on the documents read. **Ability: UNDECIDED**, a new
  team with an eighteen-month record **[M1994-008]**, running a business that "doesn’t require good management" more
  than most **[M1996-037]**.

## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
- **Part A, the retention test** **[R1995-009]**, **[M1998-110]**. From 2021 to 2025 the company earned $1,533M of net
  income, paid $960M of dividends (the same $0.23 a quarter throughout, 10-Ks and the July 2026 release) and kept $573M,
  which, with cash drawn down from $312M to $147M, repaid $647M of the IPO term loan. Nothing was retained for growth;
  the retained dollars bought down debt at the loan's rate, which creates about a dollar of value per dollar, not more.
  Market leg: the shares were sold at $26.00 in the IPO (424B4 cover) and trade at $22.23; the retention has not shown up
  in the quotation, though dividends of about $5.65 a share were paid from 2020 to mid-2026 (XBRL PaymentsOfDividends
  over 210M shares, arithmetic). The forward question, "Can you keep using all of the capital you generate" **[M2010-097]**:
  no; the business throws off more than it can use, and "a company that expects to regularly earn more than it can
  profitably employ in its business, should be paying out dividends" **[M2004-089]**, which it does, at a fixed rate,
  "clear, consistent and rational" **[L2012-015]**. The new chief executive's stated aim is a structure to "facilitate
  entry into adjacent categories" (10-Q Q2 2026, Note 9): a retention that will need watching, since "almost any
  management that wants to retain money is going to rationalize it" **[M1998-110]**.
- **Buybacks:** none since the IPO (no repurchase line in any cash-flow statement read); shares outstanding 209.7M (2020)
  to 210.8M (2026), a 0.5% creep from stock pay. **Issuance and deals:** none beyond the IPO and a $6M purchase in 2023;
  no all-stock deal, so the one STOP in Part A is not engaged **[L2009-019]**.
- **Part B, the pay, the board and the owners** **[L1993-020]**, **[M1994-009]**. Chief executive pay 2025 $6.7M, of which
  $4.5M stock (including a one-time promotion grant) (DEF 14A, Summary Compensation Table), about 2.2% of 2025 net income.
  The bonus: 60% on adjusted EBIT growth over the prior year, 15% on revenue growth, 25% on "strategic initiatives", the
  last paid at 200% of target in 2025 while the EBIT and revenue legs paid 50% and 65% (DEF 14A, 2025 AIP). Share awards:
  one-year adjusted EPS growth and adjusted free cash flow. Pay tied to "what is actually under the reasonable control of
  the person that’s being measured" **[M2003-019]**: partly; revenue growth in a price-pass-through business rewards
  aluminium prices, and the discretionary leg paid the most. "you get what you reward for" **[M2016-083]**. No capital
  charge, though the business needs little capital. The board: the controller's nominees, a compensation committee that
  is not independent, directors' holdings small except Hawkesby (334,092 shares through his company; whether bought
  with his own money is not stated) **[L2002-033]**. The owners as partners: the controller's interest and the minority's
  run together on dividends (each gets the same $0.92 a share), and apart on the IPO debt, the related-party supply terms
  and any future sale or take-private, where 26% of the owners have no vote that counts. "Owning stock in a corporation
  where you know that if shareholders or somebody else has to suffer, the choice is likely to be that somebody else will
  be chosen" **[M1998-121]** is the reading the controller's record asks for, and the record (Q5) shows the minority
  sold a company carrying the controller's debt.
- **WEIGHS: Part A UNDECIDED** (all cash paid out or used to repay the controller's IPO debt; nothing compounding; a new
  push into adjacent categories to watch) **[M2004-089]**, **[M1998-110]**. **Part B AGAINST** (a controlled board without
  an independent compensation committee, pay partly on revenue and on a discretionary leg paid at the maximum, and a
  controller whose dealings with the company have so far run in its own favour, all disclosed) **[M2003-019]**,
  **[M1998-121]**.

## Q7: WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**; value is "the discounted value of the
cash that can be taken out of a business during its remaining life" **[R1996-018]**, net of what must be put back
**[M2014-068]**; held as a range **[L2000-024]**. Arithmetic in `Test Runs/_research 2026-10-06 REYN/q7.py`.

- **The cash.** Owner cash after every real cost, five-year mean FY2021 to FY2025 (Q4): **$284.4M** on the capex basis,
  $292.4M on the D&A basis. It is cash to the equity: operating cash is already after cash interest ($80.6M a year on
  average) and cash tax ($87.4M a year on average) (10-K cash-flow supplements, XBRL InterestPaidNet and
  IncomeTaxesPaidNet, FY2021 to FY2025).
- **How sure.** The castle stands but narrows in foil and tableware, and one customer group takes 48% (Q2); the moat and
  the people enter as the certainty of the stream **[M1999-104]**, and here they argue for the lower end of the range.
- **The growth input, capped by Q3.** The convention asks for the growth shown in aggregate owner cash over the five
  years, never above it. Measured end to end that is $165M (2021) to $295M (2025), about 16% a year, from a trough base
  year, which is the "breathtaking, but meaningless" rate of **[L2005-003]**; and Q3 found volume flat and real earning
  power falling. **CONVENTION of this run (ours, confessed):** the shown-growth end is set at **2% nominal a year for ten
  years**, the growth of segment adjusted EBITDA from 2019 ($668M) to 2025 ($761M), about 2.2% a year rounded down, as the
  longest span free of the trough; then zero nominal growth, as the framework's convention says. Rationale: the
  aggregate-cash rate is a base-year artifact the rows themselves reject, and the operating-profit rate over the span
  with no abnormal end is the only shown growth that survives Q3's cap.
- **The rate:** the U.S. 30-year par yield, 5.66% (Step 0) **[L2000-021]**, **[M1996-025]**.

**VALUE RANGE** (the framework's Q7 convention: five-year mean, no-growth and shown-growth ends, ten years then zero
nominal growth, at the sovereign; 210.79M shares):

| Case | No growth | 2% for ten years | Width |
|---|---|---|---|
| Five-year mean, capex basis ($284.4M) | $5,025M, **$23.84** | $5,887M, **$27.93** | 1.17 to 1 |
| Five-year mean, D&A basis ($292.4M) | $5,166M, $24.51 | $6,052M, $28.71 | 1.17 to 1 |
| Whole-cycle variant, FY2020 to FY2025 ($312.0M) | $5,512M, $26.15 | $6,458M, $30.64 | 1.17 to 1 |
| Whole-cycle, without the separation adjustment ($265.5M) | $4,691M, $22.25 | $5,495M, $26.07 | 1.17 to 1 |

The whole-cycle variant (requested by the owner because the five-year window holds the 2021 and 2022 cost squeeze) takes
the six years 2020 to 2025, one full cost cycle: the stay-at-home peak of 2020, the squeeze, and the recovery. Its 2020
owner cash ($171M) is adjusted by adding back $279M, the one-time rebuild of receivables that before the IPO had been sold
to a parent-group entity (receivables $13M at 2019 year-end, $292M at 2020 year-end; Q4, point 4); the unadjusted line is
shown beside it. **Value range: $23.84 to $27.93 a share against $22.23**, whole-cycle $26.15 to $30.64.

**The floor** (the framework's CONVENTION, about ten percent pre-tax: **[M1994-004]**, **[L2002-020]**, **[M2003-149]**,
qualified by **[M2003-151]** and **[M2016-078]**). Pre-tax owner cash to the equity is $284.4M plus $87.4M of cash tax,
$371.8M: **7.93%** of the $4,686M market value. With growth of 0%, 1% and 2% for ten years the expected pre-tax return at
$22.23 is **7.9%, 8.5% and 9.1%**. On the all-equity basis the rows use for a whole purchase, "we evaluate acquisitions on
an all-equity basis" **[L2017-004]**, adding back cash interest ($452.4M pre-tax, pre-interest) against the enterprise
($4,686M plus net debt of $1,439M, $6,125M) it is **7.4%, 7.9% and 8.5%**. Below about ten percent on every basis.

**FAIR PRICE** (the price at or below which the central case clears the ~10% pre-tax floor). Central case: five-year
mean, 1% growth for ten years (the midpoint of the two ends), then zero. Tax treatment: the cash is grossed up by cash
taxes actually paid (five-year mean), so the floor is applied to pre-tax cash, as the rows state it ("10% pre-tax
returns (which translate to 6 [...] 7% after corporate tax)", **[L2002-020]**). On **equity plus net debt** (all-equity
basis, net debt at 2025 year-end $1,439M): **$16.14**. On equity alone, with the company's own interest deducted:
$18.88. The run names **$16.14** as the fair price, the all-equity basis being the one Q9's test 2 of the framework asks for, and the row's own words are "we evaluate
acquisitions on an all-equity basis" **[L2017-004]**; the equity-only figure is higher only because the term loan costs about 5%
against a 10% floor. Whole-cycle variant, equity alone: $20.28.

**CHEAP PRICE** (below which no pencil is needed). **CONVENTION of this run (ours):** the lower of (a) the price at which
the **no-growth** case on the all-equity basis clears ten percent pre-tax ($452.4M / 10% = $4,524M, less $1,439M net
debt: **$14.64**) and (b) two-thirds of the bottom of the value range (2/3 of $23.84: $15.89). **Cheap: $14.64.**
Rationale: at that price the purchase clears the floor with no growth credited and sits more than a third below the
conservative value, which is the distance at which "it ought to just kind of scream at you" **[M1996-084]**; a business
whose castle is narrowing in two of its four segments asks the wider margin **[M1997-080]**.

**The close.** The range is narrow (1.17 to 1), so the case is valued and not TOO HARD. The price, $22.23, sits about 7%
below the bottom of the central range, about 15% below the bottom of the whole-cycle range, and level with the bottom
of the unadjusted whole-cycle range. Against the central range that is just below its bottom, in the words of the framework's convention: not a screamer,
and it needs a pencil **[M2009-005]**, **[M1995-115]**; and the expected pre-tax return at the price is 7.4% to 9.1%
on every basis, below the floor, "a point at which we drop out of the game" **[M2003-149]**. The price must be "a
reasonable price in relation to the bottom boundary of our estimate" **[L2013-012]**: it is, but not by the margin the
rows ask.

**VERDICT: OUT** **[M2009-005]**, **[M2003-149]**. Value $23.84 to $27.93 (whole-cycle $26.15 to $30.64) against $22.23;
fair price $16.14 (all-equity basis; $18.88 on equity alone); cheap price $14.64. Q6's buyback test needs no entry: there
were no buybacks.

---
*Q8 to Q12 are NOT REACHED: the STOP at Q7 closed the file. The owner asked that Q7 to Q10 be done if Q1 to Q6 passed;
Q7 was done and closed the file, so Q8 to Q10 below record facts only, headed as the protocol requires, and are not
clearances.*

## Q8: IS IT BETTER THAN THE ALTERNATIVES? NOT REACHED.
**COMPUTATION - NOT A CLEARANCE.** The bond: the 30-year Treasury pays 5.66% (Step 0); the shares at $22.23 offer about
7.9% pre-tax and 6.1% after corporate tax on owner cash, with growth near zero. The rows want "a significantly higher
return [...] than we are from a government bond" **[M2007-095]**; two to three points pre-tax, from a business narrowing
in half its segments, is not that. The ranking against the best thing already held was not done: the holder's list was
not opened (blind rule).

## Q9: COULD IT RUIN US: the target's debt and exposures. NOT REACHED.
**COMPUTATION - NOT A CLEARANCE.** Facts recorded for whoever reopens the file: term loan $1,586M maturing March 2032,
no scheduled amortization until December 2028; $700M revolver undrawn to October 2029; $1,000M of the loan swapped to
fixed at 2025 year-end, and $900M of forward-start swaps beginning February 2026 and maturing between March 2028 and
March 2031 at a 5.12% weighted average effective rate; a 100
basis point move on the unhedged part changes interest by $6M (10-K FY2025, Note 6 and Item 7A). Pre-tax earnings over
interest about 5.6 times in 2025 ($479M against $86M), to be read as the rows read debt, "even under harsh economic
conditions" **[L2003-016]**; in the 2022 trough, operating cash covered capital spending by only $91M before dividends of $192M. The
whole-business criterion "little or no debt" **[R1997-001]** is not met; it is stated for whole businesses only. Other
exposures: one customer group at 48% (Q2); tableware supply bought from Pactiv, now unrelated, under contracts to
2027-12-31 (contrary evidence 7); a receivables factoring line of up to $95M used intra-year ($38M at 2026-06-30, 10-Q).

## Q10: IS IT THE FAT PITCH? NOT REACHED.
**COMPUTATION - NOT A CLEARANCE.** Inaction is the default **[M2003-070]**. The draft would have the buyer do nothing at
$22.23; the file reopens only on a price at or below the fair price, or on new evidence that changes Q2.

## Q12 (optional): WOULD WE BE PROUD OF HOW THE MONEY IS MADE? NOT REACHED.
Not asked. Recorded only: the products are household disposables, including foam tableware the filer itself says is
under "regulatory pressure"; none is among the businesses the rows name.

---
## THE BOX
**OUT at Q7** (the price does not clear the floor and is not a screamer) **[M2003-149]**, **[M2009-005]**. Value range
$23.84 to $27.93 a share (whole-cycle variant $26.15 to $30.64) against $22.23 (2026-10-05); expected pre-tax return at the
price 7.4% to 9.1% on every basis; fair price $16.14 on the all-equity basis ($18.88 on equity alone); cheap price $14.64.
Q1 IN, Q2 IN (the closest call: bags widening, foil and tableware narrowing, 48% from one customer group), Q3 weighs for
narrowly, Q4 IN and weighs against mildly, Q5 IN on integrity with ability undecided, Q6 Part A undecided and Part B
against. Not a TOO HARD: the deciding question was answerable and answered.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. *Not committed after each: the
      instruction for this run forbids commits; the file was written section by section to disk instead.*
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, with every quoted fragment beside an id
      matched inside that row); every filing fact has its accession; no number without a row or a filing, except the
      two CONVENTIONs of this run (Q7 growth input; cheap-price rule) and the owner's requested fair and cheap prices.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; Q8 to Q10 are headed COMPUTATION - NOT A
      CLEARANCE (a hyphen in place of the protocol's dash, under the no-em-dash instruction) and carry no entry language.
- [x] Owner cash after every real cost from operating cash less stock pay less capital spending, never a net-income
      proxy (operator rule 5); the sovereign from the U.S. Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (seven items; items 1 and 7 were extended or
      added mid-run and say so).
- [x] No row dated after the anchor is cited: the run is dated today, not point-in-time.
- [x] Only the arithmetic lines of `tools/run.py` were used; its v4 lines, ids and verdict words were ignored.
- [x] `python tools/check_framework.py` PASS (run after the file was complete; result in the working folder,
      `check_framework_out.txt`).
- Honest gaps: the 2017 and 2018 asset lines were not all read (the prospectus extract gave liabilities and equity);
  Kirkland and other store-brand makers file nothing usable; Clorox's segment mixes Glad with charcoal and litter; the
  filer gives no maintenance capital figure; no scuttlebutt beyond the competitors' filings.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The Q7 growth input.** The convention says growth is measured on aggregate owner cash over the five years and never
above it. For a business whose five-year window opens in a cost trough, that rule yields about 16% a year, a base-year
artifact the rows themselves condemn **[L2005-003]**; the convention gives no instruction for this case. This run replaced
it with operating-profit growth over the longest span free of an abnormal end (2019 to 2025, 2%), confessed as a
CONVENTION of the run; a framework rule is needed (for example: measure from the window's average, or from the longest
span whose ends are not the extremes). (2) **The range and the floor measure different things.** The range is discounted
at the 30-year Treasury (5.66% today), the floor is about 10% pre-tax. With long rates where they are, a price just below
the range's bottom implies only 6% to 8% after tax, so the floor, not the range, decided this file; the framework's Q7
close reads as if the range alone decides OUT or IN, and should say which governs when they disagree. (3) **EBITDA in the
filer's mouth.** Q4 lists EBITDA and the managements that talk it under what it rules OUT, on the row that counts the purchases
"where people are talking about EBITDA" as "about zero" **[M2002-026]**, while the STOP is on confusion or suspicion. A filer whose segment measure must by accounting rule be the measure its chief
operating decision maker uses, and who prints GAAP net income first, is talking EBITDA only in a weaker sense; the framework
does not say whether that closes Q4. This run weighed it against and did not close. (4) **Fair price, equity or
enterprise.** The framework gives the floor without saying whether it applies to the price of the shares or to the
shares plus net debt; for a leveraged company the two differ by about $2.70 a share here ($18.88 against $16.14). The run
chose the all-equity basis from Q9's test 2 **[L2017-004]**; the framework should say so at Q7. (5) **A business of mixed
castles.** Q2 has no instruction for a company whose segments point different ways (bags widening, tableware filling in);
the run judged the whole by where the earnings are, which is a reading of ours, not a rule.
