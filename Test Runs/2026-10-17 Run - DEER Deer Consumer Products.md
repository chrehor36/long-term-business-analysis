# Company Run: Deer Consumer Products, Inc. (OTC Pink, formerly NASDAQ: DEER), 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind
run under `Screens/_daily/_dispatch_brief.md` as modified by the brief (the lines of evidence derived by the analyst from
Items 1, 1A and 7 of the 10-K; the dispatcher wrote none). Every judgment cites a v5 ledger id in bold; every filing fact
carries its accession. Research folder: `Test Runs/_research 2026-10-17 DEER/` (notes, `computation.py` and its output
`computation.txt`; raw filings in the ignored `cache/`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (cc325d84): `PORTFOLIO.md` read for this one ticker; the operator does not hold DEER (no line names DEER or Deer Consumer Products).*

**CONTAMINATION, declared.** Seen by accident and not used: the session context listed recent commit subjects of another
company's run (a Hong Kong contractor, closed OUT at Q2 on 2026-10-17), file names in other run research folders (AYI,
ARCB) in the git status, and a memory index line describing the queue (wave counts, a count of gate-clearers). None
concerns this company; nothing from them enters below. No file under `Test Runs/` other than this file, its research folder
and the two templates was opened, listed or searched.

**The lines of evidence, chosen by the analyst from the FY2011 10-K** (accession 0001185185-12-000545, filed 2012-03-29):
(1) from Item 1, what the business sells and to whom: small kitchen appliances, 68% of 2011 revenue in China under the
Deer brand through retailers and agents (Gome 38% of revenue), 32% exported as ODM/OEM; the competitors it names; how its
products are priced against theirs; the ownership of its patents and trademarks. (2) From Item 1A, the risks the filer
itself names: raw material prices, rising labour costs and new low-labour-cost rivals, licences, the purported class
action, the WFOE and Circular 75 structure, the difficulty of enforcing liabilities in China, internal control.
(3) From Item 7 and the statements, whether the reported earnings became cash: operating cash, capital spending (Wuhu land
and construction), receivables, inventory, the cash balance. (4) From the 8-Ks of 2011 to 2013 and the Form 25, what the
exchange found and what happened after the last report. (5) The rivals' own filings: none of the six named rivals files
financial statements with the SEC (below).

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $0.0002 (close 2026-10-16, OTC Markets OTCPK as reported through Yahoo Finance chart data; an aggregator,
  flagged per operator rule 5). 33 of the last 251 sessions show any volume; the volume on 2026-10-16 was 1,000 shares.
  The OTC Markets API was unavailable when tried, so the market tier (Pink, Expert Market or grey) is not confirmed from
  OTC Markets itself.
- **Shares by class** from the last filing's cover: one class of common stock, 33,592,562 shares outstanding as of
  2012-08-09 (10-Q for the quarter to 2012-06-30, filed 2012-08-09, accession 0001185185-12-001666). The FY2011 10-K
  gives the same count at 2012-03-28 and its balance sheet shows 33,592,562 shares "issued and outstanding" with no
  treasury line at 2011-12-31 (accession 0001185185-12-000545). The last filing on EDGAR, a SC 13G of 2014-08-12 by Yao
  Liangren (accession 0001591351-14-000004), computes its 9.24% on the same 33,592,562. No 8-K, prospectus or other
  issuer filing after 2013-08-13. `python Screens/cover_shares.py DEER` failed: "NOT AN SEC REGISTRANT in the live ticker
  file" (the ticker is not in the SEC's current ticker map); the count is taken from the filings above. Whether the
  company has issued or cancelled shares since 2012 cannot be known: it has filed nothing.
- **Market cap:** 33,592,562 x $0.0002 = $6,718.51 (about $0.007M).
- **Sovereign for the earnings currency (RMB):** 2.06%, the 30-year point of the China government bond yield curve of
  the PRC Ministry of Finance (财政部-中国国债收益率曲线, published on the Ministry's curve page at
  yield.chinabond.com.cn, "主办单位：中华人民共和国财政部"), dated 2026-10-16. The protocol's sovereign table has no RMB row;
  this source is the issuing authority's own published curve and is named here for that reason. `tools/sources.py` does
  not carry it and was not used.
- **Filings read** (operator rule 4): the FY2011 10-K (filed 2012-03-29, accession 0001185185-12-000545); the FY2010 10-K
  (0001185185-11-000268) and its 10-K/A (0001185185-11-001580); the FY2009 10-K/A (0001144204-10-034192); the FY2008 10-K
  (0001144204-09-017240); the 10-Qs for 2012-03-31 (0001185185-12-000948) and 2012-06-30 (0001185185-12-001666); the
  DEF 14A of 2011-08-08 (0001185185-11-001146); the SEC staff correspondence of 2011-07-05, 2011-07-12 and 2011-08-24
  (0001185185-11-000962, -000992, -001433); the 8-Ks of 2011-03-14, 2011-03-22, 2011-03-28, 2011-04-26, 2011-05-04,
  2011-09-19, 2011-12-16, 2012-03-29, 2012-08-09, 2012-10-05, 2012-10-09, 2012-10-16 and 2013-08-13; the Form 25-NSE of
  2013-03-22 with its exhibit (0001354457-13-000062); the SC 13G of 2014-08-12. **One figure cross-checked against the
  filed statement:** net cash provided by operating activities for 2011, $5,968,640, in the XBRL company facts
  (us-gaap NetCashProvidedByUsedInOperatingActivities, accession 0001185185-12-000545) equals the filed consolidated
  statement of cash flows; revenue for 2011, $226,748,885, likewise. The XBRL facts carry no tag for the "Construction in
  progress" line of investing cash ($17,587,593 in 2011), so a tool reading tags alone would have missed it; the owner
  cash below is taken from the filed statements.
- **What happened after the last report, from EDGAR and the public record.** The last 10-Q is for the quarter to
  2012-06-30. NASDAQ Staff's delisting determination of 2012-10-02 (8-K of 2012-10-09, accession 0001185185-12-002172)
  rested on "the Company’s false and misleading disclosures regarding the operational status of its manufacturing
  facilities in Yangjiang, China; the Company’s failure to provide complete responses to NASDAQ Staff’s questions regarding
  the Company’s customers, suppliers and shipping providers; and the Company’s involvement in a scheme to illicitly
  transfer corporate funds to a group of stockbrokers through a bogus consulting contract." The audit committee chairman
  resigned effective 2012-10-01 after the board cut his monthly pay to $1 on 2012-09-29 (8-K of 2012-10-16, accession
  0001185185-12-002238). A Hearing Panel denied continued listing on 2013-01-09, trading was suspended 2013-01-11, the
  determination became final 2013-02-25 and the Form 25-NSE removed the stock effective 2013-04-01 (0001354457-13-000062).
  An 8-K of 2013-08-13 (0001185185-13-001692) reported the final approval on 2013-08-09 of a class-action settlement "which
  represents about 4% of plaintiffs’ claimed damages", the company continuing to deny the allegations. No 10-K for FY2012
  or any later period, no Form 15 and no 12(j) revocation order appear in the EDGAR filing index of CIK 0001388855 (read
  2026-10-17); an EDGAR full-text search for "Deer Consumer Products" from 2013 finds only third parties' 13F listings
  (one bank listed the name through 2024) and fund reports. A law firm's release of 2017-03-21 (seidenlaw.com) announced a
  shareholder group seeking a receivership and said the company "stopped reporting to the Securities & Exchange
  Commission"; no record that a receiver was appointed was found. **Not found:** whether the PRC subsidiaries still
  operate; any accounts after 2012-06-30; whether the SEC has revoked the registration; any act of the company since
  2013-08-13.
- `python tools/run.py DEER` failed: "DEER: not an SEC filer" (the live ticker map lacks it). Owner cash was computed by
  hand from the filed cash-flow statements in `computation.py` (output in `computation.txt`), arithmetic only:

| FY | operating cash | all capital spending (PP&E, land use rights, construction, land deposits, net) | owner cash | D&A | net income | revenue |
|---|---|---|---|---|---|---|
| 2007 | 0.433 | 2.242 | -1.809 | 0.814 | 3.422 | 33.476 |
| 2008 | 3.038 | 4.196 | -1.158 | 1.218 | 3.357 | 43.785 |
| 2009 | 0.384 | 4.304 | -3.920 | 1.449 | 12.369 | 81.343 |
| 2010 | 11.076 | 56.109 | -45.033 | 1.641 | 30.349 | 175.847 |
| 2011 | 5.969 | 23.496 | -17.527 | 2.966 | 39.806 | 226.749 |
| H1 2012 | -2.405 | 0.089 | -2.494 | 2.114 | 13.552 | 94.875 |

  USD millions as filed (the filer translates from RMB). Five-year sums: net income $89.3M, operating cash $20.9M, owner
  cash -$69.4M; five-year average owner cash **-$13.889M**. Stock pay is inside operating cash (added back by the filer;
  $0.33M in 2009, $0.28M in 2010, $0.10M in 2011), so it is charged here as a real cost by not adding it back again; it
  is small. No finance leases, no interest-bearing debt at 2012-06-30 (notes payable nil). Sources: 2009 to 2011 from the
  FY2011 10-K; 2008 from the FY2009 10-K/A; 2007 from the FY2008 10-K; H1 2012 from the 10-Q (accessions above).
- **The balance sheets, read in Step 0 because the file closes before Q4** (the template's instruction). Only six dates
  exist after the reverse merger of 2008: year-ends 2007 to 2011 (FY2008 10-K, FY2009 10-K/A, FY2011 10-K) and
  2012-06-30 (10-Q); eight to ten years cannot be had. What moved: equity rose from $14.0M (2007) to $185.4M (2011),
  carried by a 2009 offering ($93.6M gross, $12.4M of costs) and retained earnings of $65.7M; cash rose to $79.3M at the
  end of 2009 on the offering, then fell to $34.0M (2010), $14.0M (2011) and $9.4M (2012-06-30) in a span when reported
  net income was $83.7M (2010, 2011 and H1 2012). The cash went into land use rights in Wuhu ($36.4M in 2010; intangible
  assets $35.9M at 2011), construction in progress ($21.1M at 2011, which then barely moved: $26,620 spent in H1 2012
  though the 10-K planned workshops and a warehouse "in 2012"), property and equipment ($11.3M in 2009 to $36.1M in 2011)
  and inventory ($18.1M in 2009 to $61.0M in 2011, $79.4M at 2012-03-31). Receivables swung from $52.7M (2010) to
  $20.6M (2011) to $6.4M (2012-03-31) to $38.0M (2012-06-30). No borrowings; liabilities $12.7M at 2012-06-30. Two
  inconsistencies found: total assets at 2009-12-31 are $133,491,680 in the FY2009 10-K/A and $136,008,298 in the FY2011
  10-K's selected data, with no restatement note found in the pages read; and the 2008 share count is 22,600,000 on the
  FY2008 balance sheet and 19,652,226 after the share exchange in the 10-K narrative. What the figures cannot say: what
  any of these assets is worth or where it is now, fourteen years after the last balance sheet.

## THE FOUNDATIONS (not a gate)
A share is a business: "Would I be happy buying this stock if the market closed for five years?" **[M1997-109]**. Here
the market has in effect closed for thirteen years and the company has said nothing in that time, which is the test made
real: the buyer would own a claim on a Nevada shell whose only assets are Chinese subsidiaries it has not reported on
since 2012. The market “doesn’t tell us anything. It just tells us prices.” **[M2006-077]**: a quote of $0.0002 tells nothing of value. On who is
paid to tell you, “you do not get impartial advice” **[M2020-037]** where fees ride on one answer: the company's own press releases of 2011 attacked short sellers and "affirmed" guidance
while operating cash fell short of net income; the law firm's release of 2017 was written to gather clients. The analyst's
habits: the evidence against was hunted first and written down as found. **Contrary evidence, written down as found** (“write it down in the first 30 minutes”
**[M1997-127]**): (1) for the business: the filer reports gross margins near 30% for 2009 to 2011, no debt, in-house
motors, ODM customers who own tooling with it, and a domestic brand placed in about 4,000 stores; (2) against: in five
years the reported net income of $89.3M produced $20.9M of operating cash and owner cash of -$69.4M; NASDAQ alleged false
disclosure of the Yangjiang plant's status and a bogus consulting contract; a comparable Guangdong small-appliance ODM
that files with the SEC left the business in 2012 because it could not compete (Q2 below).

## THE STANDING RULE
Does owning this put the buyer at risk of ruin? Not by itself: the price is $0.0002 and a position would be bought for
cash, not borrowed money, so nothing puts the buyer “in a position, obviously, where the other fellow can call your tune” **[M2006-079]**; “borrowed money has no place in the investor's tool kit” **[L2014-005]**.
The rule's other edge is the one that applies: "Never risk permanent loss of capital." **[L2023-005]**, and the money
spent here could be lost entirely with no recourse (the 10-K's own risk factor: "It will be extremely difficult to acquire
jurisdiction and enforce liabilities against our officers, directors and assets based in China"). Recorded; it decides
nothing about the business.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years. So I’ve got some notion of how the industry will develop and where the company will stand
  within the industry." **[M2012-065]**. The business is a maker of blenders, juicers, soy milk makers and similar small
  kitchen appliances, sold through Chinese appliance chains and as ODM/OEM goods for foreign brands (10-K Item 1,
  accession 0001185185-12-000545). The key variables are the customer's choice at the shelf, the retailer's terms, the cost
  of plastics, copper, steel and labour, and the export customer's choice of supplier. These are questions about
  consumer and customer behaviour, the kind the rows say can be projected: "we know what we think we can project out in
  terms of consumer behavior and threats to a business." **[M2023-030]**. There is no fast-moving technology at the
  centre (the filer spent $188,658 on research and development in 2011 on $226.7M of revenue). The industry's economics
  can be foreseen in kind: many makers, standard products, powerful retail chains; that is a foreseeable position, and
  Q2 judges what it shows.
- **Where the company will stand, and the doubt.** "The first question is, can I understand it?" **[M1995-051]**. Two
  tests do not pass cleanly. Test 3, "do I understand enough about this business so that the financial statements will
  tell me the information that’s useful to me in making a judgment about what the future financial statements are going to
  look like" **[M2008-033]**: there are no statements after 2012-06-30, and the last ones are the subject of the exchange's
  allegations. Test 11, abroad, "where we think we understand the nuances of the corporate governance system and taxation"
  **[M2000-141]**: a Nevada holding company over a BVI company over PRC WFOEs, with Circular 75, MOFCOM approval of the
  2008 transfer of Winder and a possible transfer-pricing challenge all named by the filer as unresolved (Item 1A; 10-Q
  note, 0001185185-12-001666). The rows answer a less familiar country by asking a lower price, not a pass: "We wanted to
  get paid more for going into China, and we did, because we don’t know the game as well there." **[M2006-021]**. The
  absence of figures is a question of whether the business's condition can be known from its numbers, which is the
  wording of Q4's heading ("can its condition be known from them"), so it is carried to Q4 and not decided here. My
  reading, stated as mine: "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]** is a doubt about the reader's competence in the economics, and the economics of a small-appliance
  maker are inside it; the doubts above are about this company's figures and governance, which later questions own.
- **VERDICT: IN**, on the economics of the business as the 10-K describes them; test 3 and test 11 recorded and carried
  (to Q4 and Q5).

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20
years from now. What are the key factors? And how permanent are they?" **[M1995-038]**. All filing facts below are from
the FY2011 10-K (accession 0001185185-12-000545) unless another accession is given. These are the filer's statements
about itself; they do not depend on the figures NASDAQ disputed.
- **The key factors the filer itself offers** (Item 1, Competition): "Reputation as a High-Quality Producer", "Varied
  Product Menu", "Experience", "Limitation of Foreign Brands" in China; "ODM capabilities", "Experience", "Vertical
  Integration", "Customer Service" in export. None names a reason the customer cannot buy the same thing elsewhere; each
  describes a competent maker. Permanence: none is shown.
- **The attacker with money.** "if I had a hundred million dollars and I wanted to go in and take on See’s Candy, could I
  do it? [...] If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. The filer is its own evidence that
  the answer is yes: it "introduced the Deer brand (德尔) of appliances to the China domestic market in April 2008" and, on
  its own figures, took sales through traditional channels "to $122.6 million in 2011 from $58.7 million in 2010 and $11.5
  million in 2009" by placing promoters in Gome and SuNing stores and advertising "in subways, taxi stations, commercial
  building elevators". If that is true, a newcomer crossed the field in three years with money and promoters, and the road
  is open to the next one: "usually if something can gain competitive advantage very quickly, you have to worry about them
  losing it quickly, too." **[M2002-050]**.
- **Pricing power and the agony before a rise.** "you can almost measure the strength of a business over time by the
  agony they go through in determining whether a price increase can be sustained." **[M2005-020]**. The filer prices under
  its rivals by its own account: "our products retail for significantly less than the price of imports of comparable
  quality and at slight discount to the products of other domestic brands". In export it meets customers "at their price
  points", and in 2011 it "turned away certain orders [...] that did not meet our profit margin requirements". No instance
  found, in the filings read, of a price rise held.
- **Share of mind; the brand.** "you’re probably going to get better gross of margins if they ask for you by name. [...]
  And if you’re just another cola, and there have been hundreds of them, and even if you have distribution through
  something like Walmart, who has Sam’s Cola, it just doesn’t, it’s not the same." **[M2023-073]**. The Deer brand was four
  years old at the last filing; beside it the filer sells under ten other brand names "for which we own or have user
  rights" and makes "one store brand for a retailer’s private label program". The patents and trademarks are licensed from
  the Chairman and CEO, his brother and two Shenzhen companies; the transfer was never registered and the filer does not
  intend to register it; of the seven trademarks, "three expire in 2013".
- **The retailer.** "to the extent that people trust Costco or Walmart more than they [...] trust the brand, then the value
  of having the brand moves over to the retailer from the product itself." **[M2001-090]**. Gome alone took 38% of 2011
  revenue, Reed Sea 13% and Suyi 11%; agents buy the goods and hold the inventory for the stores.
- **Would the customer still choose it over the low bid?** "it wouldn’t be a question of people buying candy for the low
  bid." **[M2017-009]**; against it, "most insureds don't care from whom they buy." **[L2004-003]**. OEM customers have the
  filer produce "based on their custom specifications and designs"; export customers "look for high quality and stylish
  products from a reliable manufacturer which can meet their specifications on time and at their price points"; "we
  generally do not enter into fixed agreements as to sales quantities". The one stickiness the filer names is real and
  small: ODM customers who paid for tooling "tend to be less likely to switch suppliers relative to customers that purchase
  OEM products".
- **The low-cost position.** "commodity businesses have risk unless you’re the low-cost producer" **[M1997-010]**; "when a
  company is selling a product with commodity-like economic characteristics, being the low-cost producer is all-important."
  **[L2000-017]**. The filer claims a cost edge from in-house motors and vertical integration. Its reported gross margin
  was 21.6% (2007), 22.1% (2008), 24.8% (2009), 28.8% (2010) and 30.5% (2011); the same 10-K cites "average gross profit
  margins for small household electric appliances" of "approximately 30%". On its own figures it earned the industry
  average it cites and no more; no figure in the filings read shows its costs below a named rival's.
- **High labour content, a product easily shipped in.** "we do not want to buy into a business that has a very high labor
  content and that has a product that can be shipped in from abroad very easily." **[M2007-116]**. For its export
  customers this filer is the shipped-in product, and Item 1 says the next one is arriving: "we have experienced increased
  competition from other ODM and OEM manufacturers operating in regions with low labor costs such as Eastern Europe and
  other Southeast Asian countries"; Item 1A names rising Chinese labour costs under the Labor Contract Law.
- **Ask the competitors.** The named rivals were not reachable. The nearest public answer from inside the field is a
  comparable maker's own filing (below): a vertically integrated Guangdong small-appliance ODM, on the model the filer
  claims, wrote that it was "ultimately unable to remain competitive in the small kitchen electronics category as
  competitors offered increasingly less expensive products and mass market retailers drove down retail prices".
- **Widening or narrowing.** "whether it’s likely to widen further or shrink on you." **[M1999-108]**. Export fell from
  82% of revenue (2009) to 32% (2011) amid "an overall decrease in customer orders"; the domestic rise that replaced it is
  the part of the record NASDAQ's allegations touch. Narrowing in the part that can be read.
- **What could destroy it.** "one competitor is frequently enough to ruin a business." **[M2012-108]**. The filer names
  six, several far larger than it.

**The competitor row.** The 10-K names Midea, Hisense, Galanz, Supor, Elec-Tech and Tsann Kuen (Taiwan). **None files
financial statements with the SEC** (EDGAR company search, 2026-10-17: Midea's only EDGAR entities are an F-6EF depositary
registration, CIK 0002039784, and a SC 13D filer, CIK 0002012517; no registrant found for Hisense, Galanz, Supor,
Elec-Tech or Tsann Kuen). All six are flagged as named rivals that do not file; their exchange filings in Shenzhen, Hong
Kong and Taiwan were not read. **Comparator of this run's own choosing, not named by the 10-K:** Global-Tech Advanced
Innovations Inc. (formerly Global-Tech Appliances Inc., CIK 0001057708), a Dongguan ODM of small household appliances for
US and European brands, 20-F for the year to 2012-03-31 (accession 0001193125-12-311223), covering the same five years:

| Metric, five years | Deer (FY2007 to FY2011) | Global-Tech (years to March 2008 to 2012) |
|---|---|---|
| Gross margin as filed | 21.6%, 22.1%, 24.8%, 28.8%, 30.5% | 9.9%, 4.1%, 17.3%, 12.3%, 15.3% (continuing operations, after home appliances were reclassified as discontinued) |
| Home-appliance result | not reported by part (one segment) | discontinued home appliances, net of tax ($M): +2.0, -0.1, +3.1, -1.8, +1.4; exit approved 2011-06-03, production ceased 2012-01-15 |
| What the filer says of the field | "slight discount to the products of other domestic brands" | "Customer pricing demands no longer reflected actual production costs"; "the business becoming increasingly commoditized" |
| Operating cash against net income, five years | $20.9M against $89.3M | not compared (the 20-F's cash statement mixes in the discontinued segment) |

**The parts table.** The filer reports one segment and no profit by part. Revenue in 2011: China domestic 68%, export
32% (Item 1). CONVENTION of this run: with no profit by part filed, the deciding part is the larger by revenue; rationale:
Q2's business-of-parts convention decides by five-year operating profit, which this filer never disclosed by part.

| Part | share of 2011 revenue | castle | decides |
|---|---|---|---|
| China domestic (Deer brand, private label, agents to Gome, SuNing and others) | 68% | open: priced under rivals, entered in three years by the filer itself, 38% of revenue through one retailer, brand rights licensed from the CEO | yes |
| Export ODM/OEM | 32% | open: customers' specifications and price points, lower-labour-cost rivals arriving, orders falling | no |

**The field's returns over the last full cycle.** From the filer: reported operating income of $48.2M on equity of $185.4M
in 2011, but owner cash negative in every year from 2007 to 2011, and five years of net income turning into a quarter as
much operating cash; the reported returns never appeared as cash an owner could take. From the only SEC-filing maker in
the field found: thin or negative results in home appliances and an exit. Judged in words, as the convention asks: the
field visible in SEC filings shows ordinary or worse returns, and the filer's own high returns are not shown by its cash.

- **Why not TOO HARD.** The tenuous moat goes to TOO HARD because "We don’t know how to valuate that" **[M2000-019]**. Here
  the castle is not tenuous but shown open, on statements the filer makes about itself: a price under its rivals,
  customers who buy to their own specifications and price points, a brand it does not own, an entry it made itself in
  three years. "A truly great business must have an enduring "moat" that protects excellent returns on invested capital."
  **[L2007-004]**; "there are some industries that are just never going to have barriers to entry." **[M2012-106]**.
- **VERDICT: OUT.** Asked whether money could take the castle, the answer from the filer's own record is yes, and “If the answer had been yes, we wouldn’t have done it.” **[M2011-015]**; of the “three boxes at the company: in, out, and too hard” **[M2006-013]**, this is out. The deciding part,
  the domestic brand business, shows no castle the filings can name; the export part is a low-bid business losing orders
  to lower-cost makers. Q3 to Q10 and Q12 are NOT REACHED.

## Q3 to Q10, Q12: NOT REACHED (Q2 closed the file OUT).

---
## THE BOX
**OUT at Q2** (the castle shown open on the filer's own statements: prices under its rivals, customers who buy to their
own specifications and price points, a brand licensed from the CEO, 38% of revenue through one retailer); **integrity facts
recorded, not judged.** Q7 not reached; the COMPUTATION below is a reporting figure only.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down as found (“write it down in the first 30 minutes” **[M1997-127]**); no verdict; the box unchanged (operator rule 2).
- **Q3 (capital).** From 2009 to 2011 the filer put $36.4M into Wuhu land use rights, $25.4M into construction in progress
  and $22.0M into property and equipment (FY2011 10-K cash-flow statement, 0001185185-12-000545); the Wuhu plant had
  fencing, utilities and levelled land at the end of 2011 and $26,620 of construction spending in H1 2012 (10-Q,
  0001185185-12-001666). The 10-K also says the Yangjiang plant "currently does not operate at full capacity".
- **Q4 (the accounts).** Five years' net income $89.3M, operating cash $20.9M, owner cash -$69.4M (table in Step 0).
  Receivables of $52.7M at 2010 (30% of that year's revenue), $20.6M at 2011, $6.4M at 2012-03-31, $38.0M at 2012-06-30;
  inventory $18.1M (2009), $61.0M (2011), $79.4M (2012-03-31). Total assets at 2009-12-31 stated two ways ($133.5M in the
  FY2009 10-K/A, 0001144204-10-034192; $136.0M in the FY2011 10-K's selected data). Management reported a material weakness
  at 2011-12-31: "We lack technical accounting expertise among our financial staff regarding the requirements of U.S.
  GAAP". Auditor: Goldman Kurland & Mohidin, LLP. Guidance was affirmed in press releases of 2011-12-16, 2012-03-29 and
  2012-08-09 (8-Ks 0001185185-11-002239, 0001185185-12-000543, 0001185185-12-001665). No statements exist after 2012-06-30.
- **Q5 (integrity).** NASDAQ Staff's grounds of 2012-10-02 (quoted in Step 0, 8-K 0001185185-12-002172): false and
  misleading disclosure of the Yangjiang plant's operating status, incomplete answers on customers, suppliers and shippers,
  and "a scheme to illicitly transfer corporate funds to a group of stockbrokers through a bogus consulting contract". The
  board cut the audit committee chairman's monthly pay to $1 on 2012-09-29; he resigned on 2012-10-01 (8-K
  0001185185-12-002238). The company stopped filing after the 10-Q for 2012-06-30, and its NASDAQ appeal failed (Form 25,
  0001354457-13-000062). The class action alleging false statements on 2009 and 2010 was settled for about 4% of claimed
  damages, the company denying the allegations (8-K 0001185185-13-001692). In 2011 the company sued the short seller
  "Alfred Little" and Seeking Alpha and announced it would "Seek Sanctions against the Rosen Law Firm" (8-Ks of 2011-03-28
  and 2011-05-04); a press release title of 2011-12-16 read "Unaware of Any Negative Corporate Development". The SEC
  staff's comment letters of 2011 asked the company to support its industry statistics and to explain its sales growth;
  the company agreed to remove three of the statistics (CORRESP 0001185185-11-001433). The patents and trademarks used by
  the business are licensed from the Chairman and CEO and his brother, the 2008 transfer never registered. The CEO held
  25.45% through Achieve On Limited; the Manager of Purchasing held 5.02% through Sino Unity Limited (10-K Item 12).
- **Q6 (the money and the owners).** The 2009 offering raised $93.6M gross with $12.4M of costs; $6.9M of stock was bought
  back in 2010 while warrants brought in $7.0M; quarterly dividends of $0.05 were paid from April 2011 ($5.0M in 2011,
  $1.7M in H1 2012). None was tested against a Q7 range (Q7 not reached).
- **Q9 (debt and exposures).** No borrowings at 2012-06-30 (notes payable nil); cash held in PRC banks, uninsured (Item
  1A); a shareholder outside China has no practical way to enforce a claim (Item 1A).

## COMPUTATION NOT A CLEARANCE: the two reporting figures (a reporting convention, not a rule; no entry language)
Inputs: owner cash after the company's own tax (operating cash is after taxes paid), USD as filed, window FY2007 to
FY2011 (the last five fiscal years ever filed; FY2012 was never reported); discount rate the RMB sovereign 2.06%
(Ministry of Finance curve, 2026-10-16); 33,592,562 shares; net cash $9.876M at 2012-06-30 (cash $9.402M plus a $0.474M
certificate of deposit, no borrowings), the latest filed balance sheet, fourteen years old. The all-equity basis and the
equity-only figure coincide: there is no debt and no interest expense to separate them. The 15% PRC high-technology rate
the filer used is a preferential rate, not a carryforward or credit, so the section E adjustment was not applied; it would
only lower the figures. Arithmetic in `computation.py`, output `computation.txt`.
- **The all-spending series** (the cash input the convention requires): -1.809, -1.158, -3.920, -45.033, -17.527 ($M);
  average -$13.889M. (a) No cycle base: no end year is described by the filer as a peak or trough; 2010 carries the Wuhu
  land, which the filer describes as expansion, so it is handled under (e). (b) The series is negative in every year: the
  compound rate between the ends is meaningless, and so is the rate between the halves (2007 to 2008 average -1.48, 2010
  to 2011 average -31.28); by (b) this series gives the no-growth case alone: **-$19.78 a share** at 2.06%, -$3.84 at 10%.
  (c) No acquisitions. (d) Working capital is inside operating cash.
- **(e) The maintenance guess.** The filer states no maintenance spending; the depreciation proxy ("not inappropriate in
  most companies to use as a proxy for required capital expenditures" **[M1998-127]**) gives operating cash less D&A of
  -0.381, 1.819, -1.065, 9.435, 3.003 ($M), average $2.562M: **$4.00 a share** at no growth and 2.06%, $1.06 at 10%. The
  growth spending (Wuhu and the rest above depreciation, about $82M over the five years) bought no output that reached the
  cash statement, so the growth bought is worth less than its cost: by (e) the maintenance-only no-growth case is the top
  of the range and the all-spending case the bottom; "growth can destroy value" **[L2000-023]**. (f) Not needed for the
  ends; a growth case on the maintenance series capped at the discount rate would give $4.76 at 2.06% and $1.17 at 10%,
  shown for completeness only.
- **(a) VALUE RANGE (COMPUTATION): -$19.78 to $4.00 a share, against $0.0002.** The literal window is the same window.
  The floor test: the top case earns far more than ten percent at $0.0002 and the bottom case earns nothing at any price;
  the width is unbounded (one end negative). No verdict follows: Q7 was not reached.
- **(b) FAIR PRICE (COMPUTATION): no positive fair price.** Each end valued at ten percent and averaged (Part VII):
  (-$3.84 + $1.06) / 2 = **-$1.39 a share**, all-equity basis, equity-only identical. Beside it, and not the central
  figure: if the depreciation proxy were taken as the filing's maintenance guess with its own capped growth case as the
  other end, the pair would be $4.00 to $4.76 and the fair price $1.11; that reading credits as owner cash an operating
  cash figure that is itself the subject of the exchange's allegations and that no owner has received since 2012.

## RESEARCH PASS
None: the box is OUT, not TOO HARD (WORK).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 8b6fd623); written question by question; committed after Step 0
      and Q1 (b2da084e), after Q2 (89381865), and at the close.
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock is the dispatching session's; the fold is the
      dispatcher's (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident
      (commit subjects of another company's run, research-folder names in git status, a memory index line) is declared
      above and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      `check_ids.py` in the research folder); every filing fact carries its accession; numbers are from filings or the
      computation script.
- [x] The order was kept; Q2 closed the file; nothing after it is a clearance; the figures after it are headed COMPUTATION.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign from the issuing authority (PRC Ministry of Finance curve, dated); the price is an aggregator quote,
      flagged.
- [x] Contrary evidence written down as found (Foundations); the facts for later questions are under AFTER THE STOP and
      the integrity flag is in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] `tools/run.py` and `Screens/cover_shares.py` failed on the ticker and printed nothing used; no v4 material entered.
- [x] `python tools/check_framework.py` PASS before the closing commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A company that has stopped reporting.** No question says where fourteen years without any statement belongs. Q1's
test 3 ("the financial statements will tell me") and Q4's heading ("can its condition be known from them") both reach it,
and a verdict for a document not yet read is recorded as absent; this run read the economics at Q1 and carried the
silence to Q4, and a second analyst could fairly close at Q1 TOO HARD instead. A sentence saying which question owns a
non-reporting issuer would make the two runs agree. (2) **No RMB row** in the protocol's sovereign table; the Ministry of
Finance curve was used and named. (3) **The parts convention decides by operating profit by part**, which a one-segment
filer never discloses; this run confessed a revenue rule. (4) **Rivals that do not file with the SEC.** The brief limits
the competitor row to SEC filers; for a Chinese filer whose six named rivals file only in Shenzhen, Hong Kong or Taiwan the
row is empty, and an unnamed SEC-filing comparator was used and labelled. Whether the rivals' own exchange filings should
be read is not said. (5) **Q7 (b) and (e) together.** With an all-negative all-spending series and a positive
depreciation-proxy series, (b) says the range is the no-growth case alone, while (e) makes the maintenance case the top of
the range once the growth bought is worth less than its cost; whether the filing "allows the maintenance guess" when it
states no maintenance figure decides whether the fair price is negative or $1.11. The text should say whether the
depreciation proxy counts as the filing allowing the guess. (6) **(f)'s "never above the discount rate"** at a 2.06%
sovereign makes the growth cap equal to the rate; whether that cap binds inside the ten years is unclear. (7) **The
template's eight to ten years of balance sheets** cannot be had for a reverse-merger company with six dates. (8) The tools
fail on a ticker no longer in the SEC's live map; the CIK route (company facts) worked and could be offered.
