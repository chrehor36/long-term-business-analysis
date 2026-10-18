# Company Run: Japan Tobacco Inc. (TSE: 2914; US OTC ADR: JAPAY), 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file before any fetch. Every judgment cites a v5 ledger id in bold;
every filing fact carries its document and date (this name has no SEC filings, so the company's own filed documents stand
in place of accession numbers, by the brief's first departure); a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Dispatched blind run; research folder `Test Runs/_research 2026-10-12 JAPAY/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker; not held.*

**CONTAMINATION, declared before any verdict.** (1) To check that my own file name was free, I ran a directory listing of
`Test Runs/` filtered for this company's names; it printed one existing file name, `2026-07-15 Run - JAPAY (Japan
Tobacco).md`. I did not open, read or search it, and nothing in this run uses it; the listing itself was a search of
`Test Runs/` for this company and is declared as such. (2) The session context showed recent commit subjects about other
companies (FJTSY, FUJIY) and a memory index line naming queue counts; none concerns this company and none is used.
(3) Nothing else from the blind-listed files was seen.

**Lines of evidence chosen (the brief's second departure).** From the Annual Securities Report for the 41st term: "3.
Business Description" (the counterpart of Item 1), "3. Business and Other Risks" (Item 1A) and "4. Management Analysis of
Financial Position, Operating Results and Cash Flows" (Item 7), with the consolidated statements and notes 6 (segments),
7 (cash), 10 (other financial assets), 28 and 33 (financial income, net debt, exchangeability), 38 and 39 (pharmaceutical
exit), 40 (contingencies) and 41 (subsequent events); notes 14 (goodwill), 19 (debt) and 32 (share-based payment) were not
read in full, the goodwill share and the debt maturities being taken from the risk section and the management analysis; "IV. Filing Company" for shares, treasury shares and the government's holding; "4. Status of Corporate
Governance" for the board and pay (the counterpart of a proxy). Beside it: the Integrated Report 2026's eleven-year
financial table and its market-share table, the Semi-annual Securities Report for January to June 2026, the six earlier
Annual Securities Reports (FY2019 to FY2024), the FY2025 results presentation (2026-02-12), the press release of
2026-07-23 on the BREAK and Moro brands, and the rivals' filings (PMI 10-K, BAT 20-F). The 2026 Notice of Convocation
was downloaded but not read; board and pay facts come from the Annual Securities Report's governance section.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥7,230 a share, close 2026-10-09 on the Tokyo Stock Exchange Prime Market (Yahoo Finance chart feed, an
  aggregator, flagged per operator rule 5; Monday 2026-10-12 was a Japanese holiday, and the feed's next print, ¥7,245
  dated 2026-10-13 Tokyo time, is an intraday quote and is not used). **JAPAY: $22.87 a share, close 2026-10-12** (OTC
  Pink, same aggregator, flagged).
- **The ADS:** one JAPAY American Depositary Share represents one-half of one ordinary share: "One (1) American Depositary
  Share represents One-half (1/2) of one Share", The Bank of New York Mellon, form of receipt, exhibit to its Form F-6EF
  for the unsponsored programme, filed 2016-10-07, SEC accession 0001019155-16-000725. Three other depositaries filed F-6s
  for unsponsored Japan Tobacco programmes (Citibank 2017, JPMorgan 2021, ConvergEx 2014); the F-6 does not print the
  ticker, so the link of JAPAY to the one-half ratio is checked by price: $22.87 × 2 = $45.74 against $45.52 for the
  ordinary share's own US line (JAPAF, 2026-10-12, same aggregator), and ¥7,230 / $45.74 = ¥158.1 to the dollar, a
  plausible rate. So **¥7,230 a share = ¥3,615 an ADS = $22.87 an ADS** at the implied ¥158.1 (a derived rate, not a
  quoted one).
- **Shares** (Annual Securities Report, 41st term, "IV. Filing Company", (6) and (7), as of December 31, 2025): issued
  2,000,000,000 ordinary shares, one class; treasury shares 224,199,537; **outstanding 1,775,800,463**. Treasury shares
  held at the filing date: 224,198,682 (same report, "2. Acquisition of Treasury Shares", (4)). The Semi-annual
  Securities Report for January to June 2026 (posted 2026-08-21) gives 223,999,107 treasury shares at 2026-06-30, so
  1,776,000,893 outstanding; that count is used in the Q7 computation. Restricted stock disposals
  run to a few hundred thousand shares a year; immaterial to the count. `python Screens/cover_shares.py JAPAY` returned
  "NOT AN SEC REGISTRANT", as the brief expected; the count above is from the company's own report.
- **Market cap:** 1,775.8 million × ¥7,230 = **¥12,839 billion** (about $81.2 billion at the implied rate).
- **Sovereign for the earnings currency: 4.14%**, the 30-year JGB, Japan Ministry of Finance, `jgbcme.csv`, dated
  2026-10-08 (`python tools/sources.py`, run 2026-10-12; the same run printed USD 5.60%, US Treasury par curve, 2026-10-09).
  **Why the yen.** Most of the tobacco profit is earned abroad: "The Group’s overseas businesses account for more than half
  of revenue and adjusted operating profit" (Annual Securities Report, Business and Other Risks, (1) c.). But it is earned
  in many currencies and in no dominant one (the report names "Russian ruble, euro, British pound, Taiwanese dollar, US
  dollar, and Swiss franc"); the cash the owner can take out is the yen the parent reports and pays its dividend in; and
  the price is in yen. No single foreign sovereign describes that stream better than the yen's own. CONVENTION of this run:
  the yen sovereign is used for a stream earned in a basket of currencies and reported in yen; rationale: the figures
  discounted are yen figures, and choosing one foreign currency's rate for a basket would be an invention with no better
  claim. The US rate is shown beside at Q7 where it moves a figure.
- **Filings read** (operator rule 4; no accession numbers exist; each document with its date and its source):
  Annual Securities Report, 41st term (FY2025), filed with the Kanto Local Finance Bureau 2026-03-23, English translation
  posted 2026-04-13 under the Rule 12g3-2(b) page (`https://www.jti.co.jp/investors/others/12g3_2/pdf/20260413_E01.pdf`);
  Semi-annual Securities Report, January to June 2026, posted 2026-08-21 (`.../12g3_2/pdf/20260821_E01.pdf`);
  Consolidated Financial Results for the Six Months Ended June 30, 2026, 2026-07-30; Annual Securities Reports for FY2019
  to FY2024 (posted 2020-03-19, 2021-03-24, 2022-03-23, 2023-03-24, 2024-03-22, 2025-03-26); Integrated Report 2026;
  FY2025 results presentation, 2026-02-12; press release 2026-07-23, "JT Group signs agreement to acquire tobacco brands BREAK and Moro". Copies are in the research
  folder's `cache/` (ignored by git). **One figure cross-checked against the filed statement:** revenue for FY2025,
  ¥3,467,675 million, in the Consolidated Statement of Income (Annual Securities Report, p. 124) and in "Trends in
  Principal Management Benchmarks" (p. 1) and in the Integrated Report 2026's eleven-year table; the three agree.
- `python tools/run.py JAPAY` printed "JAPAY: not an SEC filer ... This is UNRESEARCHED, not UNKNOWABLE." and no
  arithmetic. Every figure in this run is taken by hand from the company's own reports; owner cash is built under AFTER
  THE STOP, Q7 (the file closed at Q2).
- **The balance sheets, eleven of them, read before the income account** (Q4's instruction, done here because the file
  closed before Q4). Source: Integrated Report 2026, "Long-term Consolidated Financial Data" (December 2015 to December
  2025), with inventories from the Annual Securities Reports FY2020, FY2022, FY2024 and FY2025. ¥ billion:

  | Dec | Current assets / revenue | Inventories | Goodwill | Goodwill / equity attributable | Interest-bearing debt | Cash | Net debt (debt less cash) | Equity less goodwill |
  |---|---|---|---|---|---|---|---|---|
  | 2015 | 79.8% | | 1,429.3 | 58.3% | 255.3 | 526.8 | -271.5 | 1,022.3 |
  | 2016 | 74.9% | | 1,602.0 | 65.2% | 555.3 | 294.2 | 261.1 | 854.1 |
  | 2017 | 79.8% | | 1,891.2 | 68.5% | 755.8 | 285.5 | 470.3 | 870.5 |
  | 2018 | 81.7% | | 2,008.4 | 76.3% | 987.6 | 282.1 | 705.5 | 622.2 |
  | 2019 | 88.5% | 583.7 | 2,002.6 | 75.2% | 974.5 | 357.2 | 617.3 | 660.1 |
  | 2020 | 95.8% | 539.8 | 1,909.4 | 75.7% | 958.9 | 538.8 | 420.0 | 613.4 |
  | 2021 | 99.8% | 563.2 | 2,061.0 | 73.4% | 918.6 | 721.7 | 196.9 | 748.3 |
  | 2022 | 102.5% | 691.9 | 2,446.1 | 69.1% | 958.3 | 866.9 | 91.4 | 1,094.4 |
  | 2023 | 114.7% | 832.6 | 2,616.4 | 68.3% | 1,142.3 | 1,040.2 | 102.1 | 1,213.7 |
  | 2024 | 117.0% | 957.3 | 2,914.3 | 77.4% | 1,726.8 | 1,084.6 | 642.2 | 852.4 |
  | 2025 | 107.0% | 1,060.1 | 2,923.1 | 71.5% | 1,678.7 | 831.1 | 847.6 | 1,163.8 |

  What moved and why. (1) Goodwill doubled, from ¥1,429 billion to ¥2,923 billion, and has been 58% to 77% of the
  owners' equity throughout; it is 34.7% of total assets (Business and Other Risks, (1) b.). It came from paying for
  businesses: Natural American Spirit's non-US business in 2016 (about ¥591.4 billion), further acquisitions to 2019 (the FY2019
  report credits volume growth to "acquisitions in Greece, Bangladesh and Russia"; the individual prices were not read
  for this run), and Vector Group in 2024 (about ¥344.6 billion); it also moves with the yen, since it is carried in foreign
  currencies. (2) Interest-bearing debt rose from ¥255 billion to ¥1,679 billion; net debt went from net cash in 2015 to
  ¥848 billion (the company's own "net interest-bearing debt", note 33) after Vector. (3) Current assets rose from 80% to
  107% of revenue; inventories, mostly leaf (¥674.6 billion of ¥1,060.1 billion at 2025-12-31, note 9), nearly doubled from ¥563 billion (2021) to ¥1,060 billion (2025) while
  revenue rose 49%, and the cash-flow statements show ¥448.6 billion absorbed by inventory growth in 2022 to 2025; the
  report attributes leaf cost to "the rise in tobacco leaf prices" (Business Description, Procurement) and keeps stock
  for supply security (Business and Other Risks, (1) d.). (4) Cash is not all free: ¥122.2 billion at 2025-12-31 and
  ¥166.2 billion at 2026-06-30 was held by Iranian subsidiaries whose "ability to remit funds outside of Iran is
  restricted" (note 7; Semi-annual Securities Report, note 6). (5) Equity per share rose from ¥1,369 to ¥2,302, much of
  it translation: other components of equity, mostly exchange differences, were ¥526.1 billion at 2025-12-31. What the
  figures say: a business that has grown by buying, carries most of its equity as purchased goodwill, and now ties up
  more working capital per yen of sales than it did. What they cannot say: whether the leaf stock is a safety reserve
  or slower-moving product, and how much of the Russian and Iranian cash and profit an owner in Tokyo can take out.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what the business will produce, not what the next buyer pays, "Would I be happy
buying this stock if the market closed for five years?" **[M1997-109]**. The market serves and does not instruct: the
price has more than tripled since the 2021 low of ¥1,898 (Annual Securities Report, management benchmarks, lowest price
FY2021) to ¥7,230, and appreciation "is never a reason to buy it" **[L2013-007]**. No macro forecast enters: the yen's
fall against the dollar and the euro since 2021 has lifted every yen figure in this file, and the run does not forecast
the yen; it reads the business "the average profitability of the business over time and how strong its competitive mode
is" **[M2015-016]**, so the rise in yen profit is separated from the rise in the business wherever the filings allow.
Who is paid to tell you: the company features its own adjusted operating profit at constant FX (its term) and sets its targets in
it; the run uses the statutory figures and the cash, "don’t ask the barber whether you need a haircut" **[M2011-083]**.
Margin of safety: if the decision needs a pencil, it is too close **[M1996-084]**. The analyst's habits: look for "what’s
wrong" **[M2025-013]**, and write contrary evidence down at once **[M1997-127]**.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Adjusted operating profit fell in yen from ¥626.7 billion (2015) to ¥487.0 billion (2020) before rising to ¥902.2
   billion (2025); revenue was ¥2,252.9 billion in 2015 and ¥2,092.6 billion in 2020 (Integrated Report 2026, eleven-year
   table). The recent rise coincides with a weak yen.
2. JT's share of the Japanese market, its home and once a near-monopoly, was 42.4% in 2022 and 40.8% in 2025 (Integrated
   Report 2026, market share in key markets); its share of Japan's heated-tobacco segment reached 15.7% only in the fourth
   quarter of 2025 (same report, p. 15).
3. One Russian distributor, the Megapolis Group, bought ¥497.5 billion, 14.3% of consolidated revenue, in 2025 (Annual
   Securities Report, note 6 (4)); the company says of Russia that it continues "to evaluate various options, including
   the potential transfer of ownership of our Russian tobacco business" and "is unable to reasonably estimate the outlook
   and the impact on financial results" (Business and Other Risks, (1) f.).
4. A Canadian smoking-and-health settlement cost a ¥375.6 billion provision in 2024 (note 6, adjustment items).
5. The JT Act obliges the company to buy all Japanese leaf grown under contract at about three times the foreign price
   (Business and Other Risks, (3) b.), and the government must hold more than one-third of the shares (same, (3) a.).

## THE STANDING RULE
The buyer would hold a marketable part-interest bought with cash, with no borrowing and no collateral; nothing in the
holding can make "sudden demands for large sums" of the buyer **[L2014-024]**. The holding is a yen asset held by a
dollar holder through an unsponsored ADS, and a currency holding is "a bet on how government now, and in the future, will
behave" **[M2011-025]**; that is a weight on the size of the position, not a ruin, provided it is not bought with borrowed
money, since "borrowed money has no place in the investor's tool kit" **[L2014-005]**. Ruin to the buyer: none on the facts.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The parts.** Two reportable segments, Tobacco and Processed Food; the pharmaceutical business was sold to Shionogi in
2025 and is a discontinued operation (Annual Securities Report FY2025, note 6 (1) and note 38). Tobacco carried 99% of
segment adjusted operating profit over 2021 to 2025 (¥3,884.6 billion of ¥3,915.6 billion; Integrated Report 2026,
financial data by business; 2021 is International plus Domestic Tobacco) and 99% of segment operating profit (¥3,136.5
billion of ¥3,167.2 billion). Tobacco decides; Processed Food (¥159.5 billion revenue, ¥8.6 billion adjusted operating
profit in 2025) does not, and is read here only as a part that does not matter to the earnings.

**The test as the framework states it, applied.** Understanding is "a reasonable fix on about what the earning power and
competitive position will look like in five or 10 years", with "some notion of how the industry will develop and where the
company will stand within the industry" **[M2012-065]**. The key variables and how predictable each is **[M1998-044]**:
1. *Combustible industry volume.* Falls slowly and steadily: "Combustibles volume increased within an industry volume
   declining by 2.7%" in 2025 (FY2025 results presentation, 2026-02-12, slide 18, over 70+ markets); PMI's own 10-K for
   2025 (SEC accession 0001628280-26-005939) gives "a 1.1% decrease for cigarettes" internationally and expects "a total
   international industry volume decline of around 2% for cigarettes and HTUs" in 2026. In Japan the fall was fast:
   cigarette industry volume -6.3% (2019), -8.2% (2020), combustibles -8.4% (2021) (Annual Securities Reports FY2019,
   FY2020, FY2021, Domestic Tobacco segment results). Predictable in direction and roughly in rate outside Japan.
2. *Price.* Tobacco price/mix added 7.0%, 6.2%, 8.0% and 10.8% of core revenue growth at constant FX in 2022 to 2025
   (FY2025 results presentation, slide 19). Predictable as long as excise policy and the consumer's tolerance allow; the
   report says retail price changes "most often occur in case of tax increase" (Business Description, Retail prices).
3. *JT's share of combustibles.* Rising internationally for a decade: market share rose "in all main markets" in 2021
   (Annual Securities Report FY2021, International Tobacco), grew in "approximately 50 markets" in 2025 (FY2025 report,
   segment results). Readable.
4. *The move to non-combustible formats and JT's place in them.* Not predictable from the filings (see Q2).
5. *Russia.* The company itself "is unable to reasonably estimate the outlook and the impact on financial results"
   (Business and Other Risks, (1) f.). Not predictable.
6. *The yen value of profit earned in roubles, lira, euro, sterling and others.* A macro variable; not forecast here
   (the foundations).

**Do the past statements tell me the future ones** **[M2008-033]**? For the combustible core, yes in shape: price over
volume, with share. The eleven-year table shows how much the yen moves the reported figure (adjusted operating profit
¥626.7 billion in 2015, ¥487.0 billion in 2020, ¥902.2 billion in 2025), but the company's own constant-currency series
and the USD series it printed until 2021 (International Tobacco adjusted operating profit $3,493 million in 2018, $3,126
million in 2019, $3,181 million in 2020, $4,157 million in 2021; Annual Securities Reports FY2019 and FY2021) let the
business be read apart from the currency.

**Abroad: governance and tax** **[M2000-141]**. Readable from the report: the JT Act obliges the government to hold more
than one-third of the issued shares (it held 33.34% of issued shares on 2025-12-31, 37.55% of shares outstanding), gives
it a veto on special resolutions, and makes new businesses outside the approved scope subject to the Minister of
Finance's approval; the Tobacco Business Act obliges JT to buy all domestic leaf grown under contract (Business and Other
Risks, (3) a. and b.; "IV. Filing Company", (6)). The excise system in Japan is stated in full (same section, (3) c.).

**The routing.** The industry's ten-year economics can be foreseen: all three global filers read in this run (JT, PMI,
BAT) earn high margins on a product whose volume falls slowly and whose price rises; the speakers' own reading of a
tobacco business was "probably one of the best businesses I’ve ever seen, in terms of the economics of it" **[M2005-097]**
(a row about one business at one date, weighed as evidence of the test, not as a verdict, by Q2's paragraph on a row
about one company). The product is not a technology business in its core; the economics turn on "consumer behavior and
threats to a business" **[M2023-030]**. What cannot be foreseen (variables 4 and 5) is JT's castle within the industry,
and the framework gives rapid change and the castle's future to Q2 (Q1, What understanding means: rapid change is owned by Q2). Doubt is recorded
honestly: "if you have doubts about something being into your circle of competence, it isn’t" **[M2002-092]**; my doubt
is about the castle's future, not about how the business makes its money, and it is put to Q2's tests rather than
settled here.

**VERDICT: IN.** The deciding part (Tobacco, 99% of five-year segment profit) is a business whose economics can be read
from its filings and whose combustible core, about 96% of tobacco core revenue (RRP-related revenue ¥122.5 billion of
¥3,184.4 billion core revenue in 2025; Annual Securities Report, segment results), has key variables that are known and,
outside Japan and Russia, slow-moving **[M2012-065]**, **[M1998-044]**, **[M2000-037]**. The two variables that are not
predictable go to Q2.

---
## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now" **[M1995-038]**.

**The parts table** (section B; segment profit from the Integrated Report 2026, financial data by business; FY2021 to
FY2025, continuing businesses):

| Part | Share of five-year segment adjusted operating profit | Castle | Decides |
|---|---|---|---|
| Tobacco | 99.2% (¥3,884.6 bn of ¥3,915.6 bn) | below | **yes** (more than half) |
| Processed Food | 0.8% (¥31.0 bn) | not judged: frozen noodles, cooked rice and seasonings against "Umios, Nichirei Foods, Ajinomoto Frozen Foods and Nissui" and private brands (Business and Other Risks, (1) h.), adjusted operating margin 5.4% in 2025 | no |

Beside it, the three clusters the Tobacco segment reports to the board (note 6 (2); 2022 and 2023 from the Integrated
Report 2026 composition ratios applied to the segment total): adjusted operating profit FY2022 to FY2025, ¥ billion:
Asia 267.7, 245.9, 219.6, 224.6; Western Europe 219.4, 231.7, 257.1, 277.6; EMA 266.9, 272.2, 315.0, 450.0. EMA, which
holds Russia, Turkey, Romania, the US and the Middle East, is the largest (40% of the four-year sum) and below half. The
clusters are one product in different markets, so the castle is read for Tobacco as a whole, cluster by cluster.

**The castle tests, each with its filing fact.**
1. *Key factors and their permanence* **[M1995-038]**. Brands (Winston and Camel, "global #2 & #3" brands, FY2025
   presentation slide 18), nicotine dependence, a distribution network in over 130 markets, and regulation that bans
   most advertising and so freezes shares. The last cuts both ways: the same regulators raise excise, ban flavours and
   menthol, require plain packs, and in October 2025 Japan set up "a Special Committee on Preventive Measures Against
   Passive Smoking" to consider amending the Health Promotion Act (Business and Other Risks, (2) c.). "The regulatory
   environment for tobacco is getting stricter year by year" (same, (2) c.).
2. *Without the lord.* Passes; no superstar is needed to sell Winston.
3. *The attacker with money* **[M2011-015]**. In combustibles no new entrant has displaced the four multinationals. In
   JT's home market the attacker came with money and a new format and succeeded: JT's share of Japan's cigarette market
   was 61.4% in 2018 (derived: 60.4% in 2019 after a fall of 1.0 point) and 60.4% in 2019; counting heated products, its share of the whole market was 48.7% in 2019 (46.9%
   in 2020 after a fall of 1.8 points), 44.4% in 2021, 42.4% in 2022, 42.8% in 2023, 41.2% in 2024 and 40.8% in 2025
   (Annual Securities Reports FY2019, FY2020, FY2021, Domestic Tobacco; Integrated Report 2026, market share in key
   markets). Heated products were "about 23%" of the domestic market in 2019 and "30%" in 2021; JT's share of that
   category was "about 9%", "about 10%" and 10.3% in 2019 to 2021 (same reports), and its Ploom share of heated products
   reached 15.7% only in the fourth quarter of 2025 (FY2025 presentation, slide 16). PMI's own filing dates the attack:
   "IQOS was first introduced in Nagoya, Japan, in 2014" (PMI 10-K FY2025, SEC accession 0001628280-26-005939). The
   failing answer applies to the home castle, "one competitor is frequently enough to ruin a business" **[M2012-108]**;
   it has not ruined it, but it has taken a fifth of the market from it.
4. *Pricing power and the agony before a rise* **[M2005-020]**. The strongest evidence for the castle. Tobacco price/mix
   added 7.0%, 6.2%, 8.0% and 10.8% to core revenue at constant FX in 2022 to 2025, through the inflation, while JT's
   combustible volume rose in an industry falling 2.7% (2025) and its share rose 1.3 points (FY2025 presentation, slides
   18 and 19; the Annual Securities Report FY2025 has share expanding in approximately 50 markets). That is the
   positive form exactly: "Anytime you can charge more for a product and maintain or increase market share against
   wellentrenched, well-known competitors, you have something very special in people’s minds." **[M2000-031]**. Against
   it, the company's own words on mature markets: "down-trading is prevalent in these markets" (Management Policy, (6)).
5. *Unit volume and share of mind.* Total shipments 527.3, 540.1, 552.9 and 577.8 billion units in 2022 to 2025, with
   Vector Group added from October 2024; by cluster Asia 127.4 to 128.0, Western Europe 108.9 to 97.1, EMA 290.9 to 352.7
   (Integrated Report 2026, Tobacco Business Data). Winston rose from 185.4 to 219.5 billion and Camel from 85.7 to 113.3,
   while MEVIUS, the home brand, fell from 44.7 to 40.9 and LD from 46.6 to 42.2 (same table).
6. *The low-cost position.* No filing shows JT as the low-cost producer; in Japan it carries a statutory cost
   disadvantage, domestic leaf at "approximately three times" the foreign price, which "may adversely impact the Group’s
   relative competitiveness because other global tobacco companies use foreign-grown leaf tobacco only" (Business and
   Other Risks, (3) b.). Not decisive: this is a branded business, not a commodity.
7. *Ask the competitors* **[M1999-130]**. PMI's 10-K FY2025 names "Japan Tobacco Inc." among its competitors and reports
   international industry volume "broadly stable, with a 1.1% decrease for cigarettes, largely offset by 10.2% growth of
   HTUs"; PMI's own shipments were 607.4 billion cigarettes and 179.1 billion smoke-free units, smoke-free 22.8% of the
   total. BAT, the other rival JT's report names, wrote its acquired US combustible brands down by £23.0 billion in 2023:
   "the acquired U.S. combustibles brands of Newport, Camel, Natural American Spirit and Pall Mall which are now
   considered to have a useful economic life not exceeding 30 years" (BAT 20-F FY2023, SEC accession
   0001303523-24-000024); of the new formats it says "it cannot be predicted whether regulations will permit the
   marketing (freely or with certain restrictions)" of them (BAT 20-F FY2025, accession 0001303523-26-000017). An
   insider has written a finite life on combustible brands.
8. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Two answers. Outside Japan, widening: share up in all main
   markets in 2021 and in about 50 to 60 markets in 2025; combustible profit margin up 0.5, 0.6, 1.2 and 3.4 points in
   2022 to 2025 at constant FX (FY2025 presentation, slide 20, "internal unaudited performance"). In Japan, narrowing a
   notch a year: Domestic Tobacco adjusted operating profit ¥209.0 billion (2018), ¥187.2 billion (2019), ¥168.1
   billion (2020), ¥182.4 billion (2021) (Annual Securities Reports FY2019 and FY2021), and the Asia cluster, which Japan
   dominates, ¥267.7 billion in 2022 and ¥224.6 billion in 2025.
9. *What could destroy, modify or reduce it, five to fifteen years out* **[M2000-014]**. (a) The move from combustibles
   to heated, oral and vapour formats, where JT follows the leader: the plan is to "reach mid-teens Heated Products SoS in
   key Heated Products markets and achieve break-even across the RRP business at brand contribution level" by the end of
   2028, after investing "approx. JPY 800 Bn over the three-year period from 2026 to 2028" (FY2025 presentation, slide
   12), so today the RRP business loses money at brand contribution; RRP-related revenue was ¥122.5 billion of ¥3,184.4
   billion core revenue in 2025. (b) Regulation, above. (c) Russia: the Megapolis Group, a Russian distributor, took
   ¥497.5 billion, 14.3% of consolidated revenue, in 2025 (note 6 (4)); JT holds 36.9% of the Russian market (Integrated
   Report 2026); it is evaluating "the potential transfer of ownership of our Russian tobacco business" and "is unable to
   reasonably estimate the outlook and the impact on financial results" (Business and Other Risks, (1) f.; repeated in
   the Semi-annual Securities Report for January to June 2026). PMI, with Russia at "around 6% of our total net
   revenues", calls the implications "impossible to predict at this time" (PMI 10-K FY2025). (d) Litigation: the Canadian
   settlement provision of ¥375.6 billion in 2024 (note 6). The substitute test, "If the technology had not changed,
   they’d still be impregnable franchises. But the technology did change." **[M2006-065]**, describes the Japanese record
   of 2014 to 2025.

**The competitor row** (operating profit over revenue, each from its own filings, 2016 to 2025; the revenue definitions
differ, JT's including a distribution business and, to 2023, pharmaceuticals; JT from the Integrated Report 2026
eleven-year table; PMI from its 10-K XBRL facts, OperatingIncomeLoss over
RevenueFromContractWithCustomerExcludingAssessedTax; BAT from its 20-F XBRL facts, ProfitLossFromOperatingActivities over
Revenue; aggregate = ten-year sum of profit over ten-year sum of revenue):

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | ten-year aggregate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| JT | 27.7% | 26.2% | 25.5% | 23.1% | 22.4% | 21.5% | 24.6% | 23.7% | 10.3% | 25.0% | 22.7% |
| PMI | 40.9% | 40.3% | 38.4% | 35.3% | 40.7% | 41.3% | 38.6% | 32.9% | 35.4% | 36.6% | 37.8% |
| BAT | 32.9% | 32.8% | 38.0% | 34.8% | 38.6% | 39.8% | 38.1% | -57.7% | 10.6% | 39.0% | 23.6% |

JT 2024 carries the Canadian provision; BAT 2023 carries the £27.3 billion impairment and BAT 2024 its Canadian charge
("the net impact of charges in respect of the provision recognised in relation to the Canadian settlement", BAT 20-F
FY2025). JT runs at roughly two-thirds of PMI's margin in every year. Named rivals that do not file with the SEC: none
named individually in JT's report beyond "strong firms operating in localized markets" and China National Tobacco
Corporation, which JT excludes from its ranking (Business Description).

**The field's returns over the last full cycle.** Excellent, not ordinary: the three earn operating margins from the 20s
to the 40s on revenue net of excise in every normal year of the span, and JT's adjusted operating profit of ¥902.2
billion in 2025 sits on tangible equity of about ¥768 billion (equity attributable ¥4,086.9 billion less goodwill
¥2,923.1 billion and intangibles ¥395.7 billion; statement of financial position, 2025-12-31). The castle does not
protect only ordinary returns; section C's OUT does not apply.

**The verdict, written against my own lean.** The strongest case for IN: pricing power through the inflation with
rising share is the test the speakers call "something very special" **[M2000-031]**; the field's returns are excellent;
JT's international share has risen for a decade; the speakers judged a tobacco business's economics among the best they
had seen **[M2005-097]**. The case against: the castle's future over ten to twenty years turns on three things no filing
lets me judge and the insiders themselves decline to forecast: how fast nicotine moves to new formats in each market,
and whether JT, a loss-making follower there, wins a place in them (its own target stops at 2028 and at break-even);
what regulators will permit (BAT: "it cannot be predicted"); and Russia, a seventh of revenue through one distributor,
which JT "is unable to reasonably estimate" and PMI calls "impossible to predict". The one market where the new format
arrived in force, Japan, is the market where JT's castle lost a fifth of the market and part of its profit. "We view
change as more of a threat into the investment process than an opportunity" and "whenever we look at a business and we
see lots of change coming, 9 times out of 10, we’re going to pass on that" **[M1999-063]**; "slow change can be much
harder to perceive, and can lull you to sleep easier" **[M2014-038]**; "when we see a moat that’s tenuous in any way
[...] it’s just too risky. We don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**. The moat
is not shown on the evidence to be filling in (internationally it is widening), so the box is not OUT; its future cannot
be judged, so the box is TOO HARD **[M2006-013]**.

**Which cause.** NATURE. The deciding question, what the tobacco castle earns in 2036 to 2046 once the format shift and
the regulators have run, is a forecast the industry's insiders do not write down: JT's plan is "a three-year plan that
is renewed each year on a rolling basis" because of "increasing uncertainties" (Management Policy, (5) i.), and of the
RRP categories it says only that growth rates "will be influenced by factors such as product innovation, consumer
preferences, and regulations and taxation related to RRP" (Management Policy, (6) i.); BAT and PMI say the same of
regulation and Russia in their own filings. The test is the speakers' "They would say, “That’s too hard.”"
**[M2000-105]**, and the cure is not study: "We couldn't solve this problem, moreover, even if we were to spend years
intensely studying those industries." **[L1993-023]**. A filing not yet read would not answer it, so no research pass is
opened, and a lower price does not reopen the box **[M2000-038]**.

**VERDICT: TOO HARD (NATURE).** The file closes here. Q3 to Q12 are NOT REACHED; the facts already found are recorded
below under AFTER THE STOP, and Q7's two figures are given there as COMPUTATION, NOT A CLEARANCE, as the operator asked.

---
## Q3: HOW MUCH CAPITAL MUST GO IN. NOT REACHED (the file closed at Q2).
## Q4: DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (the eleven balance sheets are read in Step 0).
## Q5: WHO RUNS IT. NOT REACHED.
## Q6: WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7: WHAT IS IT WORTH. NOT REACHED as a verdict; the operator's two figures are computed under AFTER THE STOP.
## Q8: BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9: COULD IT RUIN US. NOT REACHED.
## Q10: THE FAT PITCH. NOT REACHED.
## Q12: WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED. The framework's own text names tobacco among the
businesses refused when the whole is to be bought and run, and makes the question a WEIGHING for a marketable stake
(Q12, STOP or WEIGHING); the facts that bear on it are recorded below and not weighed.

---
## THE BOX
**TOO HARD (NATURE), decided at Q2** (the castle's future over ten to twenty years cannot be judged: the move to
non-combustible formats where JT is a loss-making follower, tightening regulation, and Russia, a seventh of revenue,
which the company says it cannot estimate). **Integrity facts recorded, not judged.** COMPUTATION, NOT A CLEARANCE:
value range ¥4,713 to ¥5,149 a share (all-equity, at the 30-year JGB) against ¥7,230; fair price ¥1,690 (all-equity),
¥2,352 (equity-only). No research pass: the cause is NATURE, and no case of the range earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts already found that bear on later questions, each with its source, written down and not weighed; no verdict; the
box unchanged (operator rule 2; Part VII, Facts for a later question)* **[M1997-127]**.

### Q3 (capital)
- Cash capital spending (property, plant and equipment plus intangibles) was ¥102.9, ¥99.4, ¥116.6, ¥150.4 and ¥162.4
  billion in 2021 to 2025, against depreciation and amortization excluding leases of ¥167.1, ¥176.9, ¥153.3, ¥148.4 and
  ¥165.3 billion (cash-flow statements; Integrated Report 2026 table). The amortization includes acquired intangibles,
  ¥55.7 billion (2024) and ¥70.5 billion (2025) (note 6 reconciliation).
- Working capital absorbed cash: inventories rose by ¥93.9, ¥136.2, ¥96.6 and ¥121.9 billion in 2022 to 2025, and
  prepaid tobacco excise taxes by ¥107.0 billion in 2023 and ¥78.9 billion in 2025 (cash-flow statements). Adjusted
  operating profit rose from ¥610.4 billion (2021) to ¥902.2 billion (2025) while equity owner cash (below) was ¥473.6
  billion in 2021 and ¥324.2 billion in 2025 as reported (¥551.0 billion with the Canadian payment added back).
- Return on the capital actually needed is high: 2025 adjusted operating profit ¥902.2 billion against tangible equity
  of about ¥768 billion plus net debt; on the capital paid for, equity attributable ¥4,086.9 billion plus net
  interest-bearing debt ¥847.6 billion (note 33), it is about 18% before tax.
- RRP: "approx. JPY 800 Bn" to be invested in 2026 to 2028, to reach break-even at brand contribution by the end of 2028
  (FY2025 presentation, slide 12).

### Q4 (the accounts)
- The company features "adjusted operating profit" and "AOP at constant FX", sets its group target in them ("mid to high
  single digit annual average growth rate over the mid- to long-term"), and from 2026 excludes from both adjusted
  operating profit and core revenue "the Canada adjustment (Annual contribution)", which is "revenue and profit
  corresponding to each annual payment related to the settlement of the litigation" in Canada (Semi-annual Securities
  Report January to June 2026, non-GAAP measures; ¥8.2 billion in the first half of 2026). The annual Canadian payments
  are thereby kept out of the featured profit figure.
- Adjusted operating profit adds back the amortization of acquired intangibles (¥70.5 billion in 2025) and "adjustment
  items" (restructuring, impairment, the Canadian provision of ¥375.6 billion in 2024, the ¥27.1 billion loss on
  liquidating the Sudanese subsidiary in 2025).
- The constant-FX figure "excludes the increase in revenue or profit caused by inflation in some markets calculated
  using certain methods"; hyperinflation accounting (IAS 29) applies to some subsidiaries (MD&A, non-GAAP notes).
- Inventories grew faster than sales (Step 0 table). Iranian cash is restricted (note 7).
- Stock pay is small: share-based payments ¥1.0 billion in 2025 (statement of changes in equity).
- Revenue ¥3,467,675 million was cross-checked in three places (Step 0).

### Q5 (the people; integrity facts recorded, not judged)
- 2025 executive-bonus targets and results (Annual Securities Report, remuneration): core revenue at constant FX target
  ¥3,160.0 billion, result ¥3,347.8 billion; adjusted operating profit at constant FX ¥825.0 billion against ¥926.6
  billion; adjusted operating profit ¥746.0 billion against ¥901.3 billion; profit ¥449.0 billion against ¥487.7
  billion. Bonus weights: 15% core revenue at constant FX, 35% AOP at constant FX, 25% AOP, 25% profit.
- The redefinition of the featured profit measure in 2026 to exclude the Canadian annual payments (Q4 above).
- The company operates in countries under sanctions: "the Group conducts business in countries that are subject to
  economic sanctions"; in Russia it is "fully committed to complying with all applicable sanctions" (Business and Other
  Risks, (1) f.); its Iranian subsidiaries hold restricted cash (note 7).
- Litigation: 142 smoking-and-health cases pending at 2025-12-31, 123 individual cases against subsidiaries in the
  United States, where the Group's business is Vector Group, whose Liggett Group is named in the one US class action
  (note 40); the 18 Canadian cases discharged under the CCAA plans implemented on
  2025-08-29 (same note).
- The Chairman of the Board from March 2026, Shigeaki Okamoto, entered the Ministry of Finance in 1983 and was its
  Administrative Vice Minister from July 2018; he holds 1,900 shares (Annual Securities Report, officers). A standing
  Audit & Supervisory Board member also came from the Ministry of Finance (same).

### Q6 (the money and the owners)
- No buyback programme in 2021 to 2025: treasury-share purchases were ¥1 million to ¥1.6 billion a year, odd lots
  (cash-flow statements; "IV. Filing Company", 2. Acquisition of Treasury Shares: "No items to report" under board
  resolution). The buyback test against the bottom of the Q7 range therefore has nothing to read. Policy: "Consider
  implementing a share buy-back program, mainly taking into account the Company’s financial outlook of the respective
  year and mid-term capital needs" (Management Policy, (4)).
- Dividend policy: "Target a dividend payout ratio of about 75%", ±5%; payout 85.0% in 2025 on the company's adjusted
  profit basis (Integrated Report 2026 table). Dividends to owners paid: ¥251.9, ¥266.2, ¥367.3, ¥349.6 and ¥356.9
  billion in 2021 to 2025, 78% of the five-year equity owner cash as reported.
- Deals: RJR Nabisco's non-US business (1999, about ¥944.0 billion), Gallaher (2007, about ¥1,720.0 billion), Katokichi
  (2008, about ¥109.0 billion), Natural American Spirit non-US (2016, about ¥591.4 billion), Vector Group (2024, about
  ¥344.6 billion), all for cash (Business and Other Risks, (1) b.); BREAK and Moro trademarks signed 2026-07-22 for EUR
  176 million (about ¥32.6 billion), unclosed, "funded by JT Group's existing cash" (press release 2026-07-23). No
  all-stock deal found in the window.
- Pay: board pay ¥2,169 million in 2025, the largest individual ¥1,007 million; restricted stock restricted for 30 years
  or until retirement; performance share units on profit plus ESG and RRP indices (Annual Securities Report,
  remuneration). The government holds 37.55% of shares outstanding and a veto on special resolutions by statute.

### Q7 (COMPUTATION, NOT A CLEARANCE)
*Computed because the operator asked for the two reporting figures; not a clearance; no entry language (operator rule 3).
Arithmetic in `Test Runs/_research 2026-10-12 JAPAY/q7_compute.py`, output in `q7_output.txt`; ¥ billion unless stated.*

**Owner cash after every real cost, by year** (operating cash flow, which is after interest paid, interest and dividends
received and income taxes paid, less purchases of property, plant and equipment and of intangibles, lease principal
repayments and dividends to minority owners; Annual Securities Reports FY2022 for 2021 and 2022, FY2024 for 2023 and
2024, FY2025 for 2025):

| | 2021 | 2022 | 2023 | 2024 | 2025 | average |
|---|---|---|---|---|---|---|
| Operating cash flow | 598.9 | 483.8 | 566.3 | 630.0 | 514.1 | |
| Equity owner cash (after interest) | 473.6 | 361.8 | 423.5 | 450.7 | 324.2 | 406.8 |
| All-equity owner cash (interest paid added back, interest and dividends received taken out) | 473.5 | 360.0 | 408.7 | 419.4 | 277.0 | 387.7 |
| Same, 2025 Canadian settlement cash added back (177.2 + 49.6) | 473.5 | 360.0 | 408.7 | 419.4 | 503.8 | 433.1 |
| Acquisitions net of disposals (Vector 265.7 in 2024; 68.3 subsequent payment, 24.8 associates, less 42.8 pharmaceutical proceeds and 2.3 sales in 2025) | -2.6 | -3.0 | -1.4 | 265.3 | 47.9 | 61.2 |
| **Central series: all-equity, Canada adjusted, acquisitions deducted** | 476.0 | 363.1 | 410.0 | 154.1 | 455.9 | **371.8** |

Treatments, each named: the company's own tax, as paid (Whose tax); 2025 is aberrational on the filer's own description
of the Canadian settlement as "a one-time loss of 375.6 billion yen on litigation" (Integrated Report 2026, note 6 to the
eleven-year table), so its cash payment is added back and the unpaid settlement liability,
¥161.3 billion at 2026-06-30 (Semi-annual Securities Report, note 14), is added to net debt instead, so the cost is
charged once (specific (a)); acquisitions are deducted and the total growth credited, the default pair; net purchases
are 14% of owner cash before purchases, so the serial-acquirer rule does not apply (specific (c)); working capital is
counted, inside operating cash flow (specific (d)); the filing does not separate maintenance from growth spending (the
RRP device and stick capacity is inside capital spending), so the all-spending case is central and the depreciation
variant is shown beside (specific (e)); the pharmaceutical business, sold in 2025, is inside the 2021 to 2025 cash flows
(its operating cash flow was ¥9.7 billion in 2024 and ¥11.0 billion in 2025, note 38), a small overstatement left in.
Unlevering adds back gross interest paid without its tax shield; net interest was close to zero or a receipt in every
year, so the error is small and runs against the business.

**Growth shown.** Central series 2021 to 2025, end-year compound rate **-1.07% a year** (both ends positive, so the rate
is meaningful; specific (b)): a decline, carried as the bottom of the range, with the no-growth case as the top. Beside:
before acquisitions +1.57% a year; equity basis +1.38%. The cap (specific (f)) is not reached. After year ten the
purchases stop and the terminal value is on owner cash before purchases (+¥61.2 billion; specific (c), section E).

**Net debt** (all-equity basis, latest filed balance sheet, 2026-06-30, Semi-annual Securities Report): bonds and
borrowings ¥1,676.8 billion (117.1 current, 1,559.7 non-current) less cash ¥827.9 billion less time deposits and debt
securities ¥187.3 billion (¥191.6 billion at 2025-12-31, note 10, less the first-half net withdrawal of ¥4.3 billion),
plus the Canadian settlement liability ¥161.3 billion = **¥822.9 billion**. Lease liabilities are left out because their
principal is already charged in owner cash. Beside: with the Iranian cash (¥166.2 billion) not counted as cash, ¥989.1
billion. Retirement benefit liabilities of ¥250.0 billion are left out (not borrowings), said so. Shares 1,776.0 million
(2,000,000,000 issued less 223,999,107 treasury at 2026-06-30). Market value at ¥7,230: ¥12,840 billion; with net debt,
¥13,663 billion.

**The value range (Q7's range convention in full), discounted at the 30-year JGB, 4.14%:**
- No-growth case (top): ¥9,967 billion for the business; **¥5,149 a share**.
- Decline case at -1.07% a year for ten years, then flat (bottom): ¥9,194 billion; **¥4,713 a share**.
- **Range ¥4,713 to ¥5,149 a share** (¥2,357 to ¥2,575 an ADS; $14.90 to $16.28 an ADS at the implied ¥158.1) against
  **¥7,230 (JAPAY $22.87)**. Top over bottom 1.09, far inside three to one.
- **The floor, tested first:** the expected return at the price is 3.05% on the no-growth case and 2.81% on the decline
  case; no case earns about ten percent at ¥7,230. Earning ten percent at the price would need owner cash to grow 18.4%
  a year for ten years. Had Q7 been reached, the price above the top of the range would close it OUT by the floor
  convention.
- Beside, each named: the literal window (2025 with the Canadian payment in, growth -16.7% a year): ¥1,314 to ¥4,623;
  the depreciation variant (D&A in place of capital spending, ¥35.9 billion a year lower): ¥4,267 to ¥4,661; Iranian
  cash not counted as cash: ¥4,620 to ¥5,055; the US 30-year rate, 5.60%, in place of the JGB: ¥3,328 to ¥3,632; no
  purchases at all, no growth: ¥5,427.
- The signed, unclosed BREAK and Moro purchase (¥32.6 billion, cash, no earnings filed for the brands) would add ¥32.6
  billion to net debt, about ¥18 a share off every figure, credited at nothing; left out of the central figure.

**The two reporting figures (a reporting convention, not a rule; not a verdict; Part VII, The owner's price and How the
fair price is computed):**
- **(a) VALUE RANGE: ¥4,713 to ¥5,149 a share** ($14.90 to $16.28 an ADS), all-equity basis, at 4.14%, against ¥7,230
  ($22.87 an ADS).
- **(b) FAIR PRICE: ¥1,690 a share** (¥845 an ADS, about $5.34), the all-equity central figure: each end case valued at
  ten percent (¥3,954 billion no-growth, ¥3,695 billion decline), averaged, less net debt ¥822.9 billion, over 1,776.0
  million shares; owner cash after the company's own tax, no conversion. **Equity-only beside: ¥2,352 a share** (¥1,176
  an ADS, about $7.44): equity owner cash ¥390.9 billion a year, growth +1.38%, valued at ten percent and less the
  Canadian liability, against the market value of the shares. Literal window beside: ¥1,005. Iranian cash not counted:
  ¥1,597.

### Q8 (alternatives)
- The 30-year JGB yields 4.14% (MOF, 2026-10-08); owner cash at the price yields about 2.7% on the business's value
  (¥371.8 billion against ¥13,663 billion).

### Q9 (ruin)
- Debt maturities at 2025-12-31: ¥79.6 billion within one year, ¥20.2 billion, ¥230.3 billion, ¥82.8 billion and ¥200.6
  billion in years two to five, ¥1,080.6 billion after five (MD&A (8) b.). Ratings A2 (Moody's), A+ negative (S&P), AA
  (R&I), AA+ (JCR). Unused committed lines ¥683.9 billion. Bondholders have "statutory preferential rights to the
  property of the Company" under the JT Act (same).
- Operating profit ¥867.0 billion against interest expense ¥76.2 billion in 2025 (statement of income; cash-flow
  statement).
- Exposures: Russia through one distributor (14.3% of revenue); Iranian cash restricted; sanctions risk stated by the
  company; US smoking-and-health litigation through Liggett (note 40).

### Q12 (how the money is made)
- The business is the manufacture and sale of tobacco products in over 130 markets (Business Description), 99% of
  segment profit. A buyer of JAPAY would hold a marketable part-interest, not the whole business.
- It sells in Russia and holds subsidiaries in Iran, and states that "simply operating in the countries subject to the
  sanctions may have a detrimental effect on the public image of the Group" (Business and Other Risks, (1) f.).
- Combustibles are about 96% of tobacco core revenue (2025).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the template was copied before the first download); written question
      by question; committed after Step 0, Q1, Q2, and with this closing section (write-early).
- [x] Dispatched to an analyst: the brief allowed the per-question pathspec commits; the lock is the dispatching
      session's; the fold into the register is the dispatcher's (operator rule ten). Not checked by me: whether the lock
      is held (I did not open `Screens/`, by the blind rule's spirit).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened. One breach to declare: a directory listing of
      `Test Runs/` filtered for this company's names, made to check my file name was free, printed the name of an
      earlier run file for this company; it was not opened (CONTAMINATION, top of file).
- [x] Every v5 id resolves (check script in the research folder, `check_ids.py`: ids present in
      `principle_ledger_v5.csv`, no E-ids, every quoted fragment beside an id found in that row). Every filing fact
      carries its document and date; there are no accession numbers for JT's own filings because it files none with the
      SEC (the brief's first departure); the rivals' and the depositary's SEC accessions are given.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is facts or COMPUTATION,
      NOT A CLEARANCE.
- [x] Owner cash after every real cost, from the filed cash-flow statements, never a net-income proxy (operator rule
      5); the sovereign from the issuing authority (MOF `jgbcme.csv`, dated); aggregator quotes flagged (Yahoo Finance).
- [x] Contrary evidence written down as found (the foundations' list), and the facts for later questions are under
      AFTER THE STOP with the integrity flag in the box line.
- [x] No row dated after the anchor is cited: this is a live run, not a point-in-time test.
- [x] `tools/run.py` and `Screens/cover_shares.py` returned nothing usable (not an SEC filer); no line of theirs was used.
- [x] `python tools/check_framework.py` run before the final commit (result in the reply and the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q1 against Q2 for an incumbent facing a format shift.** Q1's routing sends "a business whose ten-year economics
cannot be foreseen because its industry changes fast" to Q1 TOO HARD, and Q1's test 6 ("Can I name the winner") sends
industries whose winners cannot be named there too; Q2 owns "a castle whose future cannot be judged" and says rapid change
is owned by Q2. For Japan Tobacco the industry's economics can be read and its combustible core is a named winner, while
its castle's future turns on a format race it is losing in its home market. I put the close at Q2; an analyst who read
the RRP race as "winners cannot be named" would close at Q1 with the same box, and one who weighted the pricing evidence
more would pass Q2 and close OUT at Q7 on price. The text does not say which of the three the facts of a mature
incumbent under substitution call for. (2) **Parts inside one segment.** The parts convention speaks of "parts with
different economics" the filer reports; JT reports three geographic clusters to its board inside one Tobacco segment, and
EMA, which holds Russia, is the largest. Whether clusters are parts is not stated; had I treated them as parts, EMA would
decide as "the largest part". (3) **A part whose future cannot be judged and does not decide** (Russia, inside EMA) has
no stated treatment; the convention covers only a non-deciding part that is open. (4) **Net debt under IFRS 16.** The
all-equity convention adds "finance leases" and leaves out "operating leases"; IFRS 16 has no such split, and lease
principal is already charged in owner cash, so I left all leases out and said so. The text also has no rule for cash the
filer says cannot be remitted (¥166.2 billion in Iran) or for a settlement liability carried as a financial liability
(the Canadian one); I counted the second as debt and showed the first both ways. (5) **The earnings currency for a
multi-currency earner** reporting in yen has no rule; I confessed a CONVENTION of this run. (6) **"Purchases stop after
year ten"** (section E) is written for the growth case; I applied it to both ends of the range, since the no-growth case
also buys no growth after year ten, and the text could be read either way. (7) **The template** asks Q4's balance sheets
to be read "in Step 0" when the file closes earlier but gives Step 0 no slot for them; I added one. Its self-audit line
"every filing fact has its accession" cannot be met literally by a non-SEC filer.
