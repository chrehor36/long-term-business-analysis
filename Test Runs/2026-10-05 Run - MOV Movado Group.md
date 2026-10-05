# Company Run — Movado Group, Inc. (NYSE: MOV) — 2026-10-05
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** NOT CHECKED. The run was dispatched under a blind rule that forbids opening
`PORTFOLIO.md`, any holding review, the resume-state files, the register and the reading list, and forbids trying to learn
whether anyone holds or wants this name. None was opened. Whether the operator holds MOV is unknown to this analyst.

**CONTAMINATION, declared.** (1) The session's git status and recent commit subjects name other runs and their boxes
(HUBB, ATKR, ETN, all dated 2026-10-05) and two untracked run files of the same day (DBD, MBUU); none was opened, and no
figure or verdict from them is used. (2) The auto-memory index loaded with the session states general queue facts (a
count of gate-clearers, "nothing buyable"); nothing in it names MOV. (3) `tools/run.py` printed only arithmetic; its
ten-year balance-sheet table was found defective (quarter-ends mixed with year-ends, FY2016 to FY2022 missing) and was
replaced by the table below, built from the filed 10-Ks. No other Test Runs file about Movado was searched for or opened.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $33.53 (2026-10-05; printed by `tools/run.py`; **aggregator, live quote only, flagged** under operator rule 5).
  For scale, the filings record closes of $13.56 on 2025-04-11 (10-K FY2025, Item 5, 0000950170-25-054522) and $23.14 on
  2026-03-13 (10-K FY2026, Item 5, 0001193125-26-115298): the price has risen about 2.5 times in eighteen months.
- **Shares by class** from the latest filing's cover (10-Q for the quarter to 2026-07-31, filed 2026-08-26, accession
  `0001193125-26-366101`; `python Screens/cover_shares.py MOV`): Common Stock 15,956,643; Class A Common Stock 6,355,602.
  **Charter note read** (10-K FY2026, Item 5): each Class A share carries ten votes, converts at any time into one common
  share, converts automatically on transfer outside the family's "permitted transferees", has no public market, and receives
  the same quarterly dividend ("the Company declared cash dividends on its common stock and class A common stock", 10-K
  FY2026, Item 5). The classes are
  economically equivalent; voting differs. Economic share count **22,312,245**.
- **Market cap:** 22.312M x $33.53 = **$748.1M**. Cash $211.6M at 2026-07-31 and no borrowings (10-Q balance sheet and
  Note on the credit facility, 0001193125-26-366101), so enterprise value at the price is about **$536.5M**.
- **Sovereign for the earnings currency (USD):** **5.63%**, the 30-year par yield, US Treasury daily par yield curve,
  2026-10-02 (`python tools/sources.py`, issuing authority). Reporting currency USD; 56.7% of sales are international
  (10-K FY2026, Item 7), so the earnings currency is mixed and the USD rate is used as the run's single yardstick.
- **Filings read** (operator rule 4): 10-K FY2026 (fiscal year to 2026-01-31, filed 2026-03-19, `0001193125-26-115298`):
  Items 1, 1A, 5, 7, 9A, the balance sheet and the segment note; 10-Q to 2026-07-31 (`0001193125-26-366101`): MD&A,
  balance sheet, tariff and credit-facility notes; DEF 14A filed 2026-05-06 (`0001140361-26-019208`): ownership table,
  CD&A, summary compensation table; 10-K FY2025 (`0000950170-25-054522`): Note 1A, the restatement; 10-K FY2023
  (`0000950170-23-009351`), FY2021 (`0001564590-21-015296`), FY2019 (`0001564590-19-009741`), FY2016
  (`0001564590-16-015742`): segment sales by brand category, the acquisitions and the impairments; 8-K exhibits 99.1 of
  2026-03-19 (`0000950142-26-000775`) and 2026-08-26 (`0000950142-26-002427`): the earnings releases. Raw text is in
  `Test Runs/_research 2026-10-05 MOV/`.
- **One figure cross-checked against the filed statement:** cash and cash equivalents at 2026-01-31, **$230,541 thousand**
  on the face of the filed consolidated balance sheet (10-K FY2026), equal to the XBRL value `tools/run.py` printed.
  Second check: operating cash flow FY2026 **$57.9M** in the filed MD&A equals the XBRL value.
- **`tools/run.py MOV` arithmetic lines only** (Part VII): five-year owner earnings 48 to 52 ($M), three-year 29 to 32;
  FY2026 OCF 58, SBC 5, D&A 9, capex 5. Its v4 material, its "yield vs sovereign" lines and its share basis (a weighted
  average) are not used. The run's own owner-cash table is in the COMPUTATION section after the close.

### The balance sheets, ten year-ends, read before the income account (USD $M; XBRL latest-filed vintage, FY2024 as restated; face statements read for FY2026 and FY2024)
*(The rule sits at Q4, which this run does not reach. They were read here, before Q1, because Q2's castle tests use the
income account and **[M2025-032]** asks for "balance sheets over an 8 or 10 year period before I even look at the income
account".)*

| FYE Jan | assets | liabilities | equity | cash | receivables | inventory | goodwill | other intangibles | retained earnings | treasury stock |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 607.8 | 133.8 | 474.0 | 256.3 | 66.8 | 153.2 | 0 | 1.6 | 415.9 | 204.4 |
| 2018 | 645.4 | 175.0 | 470.3 | 214.8 | 83.1 | 151.7 | 60.3 | 23.1 | 388.7 | 208.9 |
| 2019 | 759.7 | 259.3 | 496.7 | 189.9 | 84.0 | 165.3 | 136.0 | 48.2 | 431.2 | 217.2 |
| 2020 | 847.3 | 316.9 | 526.5 | 185.9 | 78.4 | 171.4 | 136.4 | 42.4 | 455.5 | 222.8 |
| 2021 | 719.3 | 289.3 | 425.3 | 223.8 | 76.9 | 152.6 | 0 | 17.1 | 341.6 | 223.3 |
| 2022 | 761.2 | 284.1 | 472.8 | 277.1 | 91.6 | 160.3 | 0 | 13.5 | 413.6 | 249.0 |
| 2023 | 787.7 | 277.2 | 507.6 | 251.6 | 94.3 | 186.2 | 0 | 9.6 | 476.8 | 281.6 |
| 2024 (restated) | 756.5 | 248.4 | 505.9 | 262.1 | 86.0 | 153.9 | 0 | 7.5 | 459.4 | 285.3 |
| 2025 | 729.2 | 245.7 | 481.3 | 208.5 | 93.4 | 156.7 | 0 | 5.5 | 446.7 | 289.1 |
| 2026 | 742.6 | 232.4 | 508.8 | 230.5 | 102.0 | 158.3 | 0 | 4.2 | 442.2 | 293.4 |

**What the figures say.** (1) **Equity stood still for a decade**: $474.0M to $508.8M while the company earned a cumulative
$281.0M of net income FY2017 to FY2026 (10-K income statements as filed, FY2018 carrying a $57.4M tax charge and FY2021 the
impairments). Retained earnings rose $26.3M in ten years. Everything earned was paid out (dividends $229.4M and open-market
repurchases $82.7M over the same ten years, XBRL cash-flow tags) or written off. (2) **Goodwill came and went**: $60.3M
(Olivia Burton, July 2017, $79.0M cash) and then $136.0M (MVMT, October 2018, $97.9M cash plus an earn-out of up to $100M),
then a $133.7M goodwill impairment and a $22.2M MVMT trade-name and customer-relationship impairment in the first quarter of
FY2021 (10-K FY2021, 0001564590-21-015296). The MVMT earn-out liability was remeasured to zero by 2020-01-31 "Based on
updated revenue and EBITDA ... performance expectations", a $15.4M non-cash gain (same 10-K): the acquired brand missed
its seller's targets within fifteen months. (3) **No debt in any year**: the revolver was drawn for the MVMT purchase and
repaid; weighted average borrowings were zero in FY2025 and FY2026 (10-K FY2026, Item 7). Liabilities grew from FY2020 on
because operating leases came onto the balance sheet ($78.7M lease liability at FY2026), which is an accounting change, not
borrowing. (4) **Inventory is heavy and slow**: $151.7M to $186.2M against sales of $507M to $744M, about a quarter of a
year's sales held as watches and parts; FY2023's $186.2M was followed by FY2024's cut to $153.9M. (5) **Receivables were
overstated**: the FY2024 restatement took $18.4M off trade receivables (from $104.5M to $86.0M) and $10.9M off retained
earnings (10-K FY2025, Note 1A, 0000950170-25-054522). (6) **Cash is large and partly abroad**: $230.5M at FY2026, of which
$136.2M at foreign subsidiaries (10-K FY2026, Item 7). (7) **Other non-current assets rose from $42.4M (FY2017) to $90.3M
(FY2026)**, which include minority stakes in "early-stage growth companies and venture capital funds", some investing "in
digital assets": $21.5M committed since FY2022, $17.5M funded, two impairments recorded (10-K FY2026, Items 1A and 7).

**What the figures do not say and cannot say** **[M2025-032]**: which licensed brand earns what, and on what royalty; how
much of "owned brands" is Movado itself as against Ebel, Concord, Olivia Burton and MVMT; how much of the Company Stores
segment's margin is discounted owned-brand product. The filings give category totals only.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this "if the market closed for five years?"
**[M1997-109]**, and the price, which has risen about two and a half times since April 2025, "just tells us prices."
**[M2006-077]**; neither the rise nor the fall before it is evidence about the business. No macro view enters: the tariff
episode (IEEPA duties of $12.7M incurred in FY2026, ruled unlawful, $3.2M refunded in the quarter to July 2026; 10-K FY2026
Item 7 and the 10-Q) is read only for what it shows of the company's pricing, at Q2. The analyst's habits: this is a
cheap-looking, debt-free, dividend-paying small cap, the kind of file an analyst is tempted to clear, so the hunt for the
case against it was made first. **Contrary evidence, written down as found** **[M1997-127]** ("write it down in the first 30
minutes"): (a) the company has stayed solvent, debt-free and dividend-paying through the smartwatch decade, a pandemic and a
fraud in its Dubai branch, while its largest U.S. peer lost most of its revenue; (b) its licensors have renewed for decades
(Coach since 1999, Tommy Hilfiger 2001, Hugo Boss 2006, Lacoste 2007) and it won a new licence, Kate Spade New York, for
watches from spring 2027 (the 10-K dates the signing "July 2025" on page 2 and "July 1, 2026", a date after its own filing,
on page 8; a drafting error in the filing, recorded as found);
(c) licensed-brand sales grew 7.2% in FY2026 and 9.0% in the quarter to July 2026; (d) the owned outlet chain earned $14.8M
in FY2026, the company's most profitable segment; (e) the first half of FY2027 shows operating income of $21.9M against
$4.3M a year earlier (10-Q). Each is weighed at Q2.

## THE STANDING RULE
A purchase of this common stock for cash puts no buyer at risk of ruin by the buyer's own conduct; the rule would be broken
only by financing it with borrowed money, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, or by a
size that cost the buyer the ability to "play the next day." **[M2025-015]**. Nothing in this file asks for either.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test applied.** Understanding means a fix on "what the earning power and competitive position will look like in five
  or 10 years." **[M2012-065]**. The business is plain: Movado designs, sources from independent makers in Switzerland and
  China, markets and distributes watches and some jewelry; it manufactures nothing (10-K FY2026, Item 1: "The Company does
  not manufacture any of the products it sells."). It sells through department stores, jewelry chains, online
  marketplaces, distributors and 57 own outlet stores.
- **The key variables, and whether they are foreseeable** (**[M1998-044]**: "trying to identify the key variables in that
  particular business"): (1) whether the five licensors renew, and on what royalty (licensed brands were 58.3% of FY2026
  net sales; Hugo Boss and Calvin Klein run to 2026-12-31, Coach to 2028-06-30, Tommy Hilfiger to 2029-12-31, Lacoste to
  2031-12-31; 10-K FY2026, Item 1); (2) consumer demand for analog fashion watches in a world of smartwatches; (3) owned-brand
  demand, chiefly Movado; (4) the department-store door count; (5) gross margin against tariffs, the Swiss franc and the
  marketing spend needed to hold share (19.5% to 22.4% of sales, FY2024 to FY2026). These are consumer and contract
  questions, not technology questions the company must win: the forecast is of "consumer behavior and threats to a
  business" **[M2023-030]**. Ten years of statements (FY2016 to FY2026) show what the variables have done, so the past
  statements do say something about the future ones **[M2008-033]**.
- **Where it will be in ten years**: a mid-sized distributor whose sales have moved sideways in nominal dollars (FY2016
  $594.9M; FY2026 $671.3M, with two acquired brands inside the later figure), whose owned brands shrink and whose licensed
  share rises, and whose operating margin has run between 3% and 16% with a falling trend. That is a forecast I can write
  down, and it is a forecast about the castle, which Q2 owns.
- **The doubt, written down.** "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**, and of retail, "it’s easy to sort of think you understand retail, and then subsequently find out you
  don’t" **[M2014-052]**. "Fashion trends and consumer demands and tastes often shift quickly." (10-K FY2026, Item 1A). I do
  not doubt that I understand how this business makes and loses money; what I cannot do is promise that it will make more,
  which is a finding about the castle, not about my perimeter.
- **VERDICT: IN.** The economics and the competitive position can be foreseen in outline from the filings **[M2000-037]**,
  **[M2012-065]**; whether they are good is Q2's question.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
"why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five, 10, 20 years
from now." **[M1995-038]**. The castle tests, each with its filing fact:

- **The attacker with money** ("If the answer had been yes, we wouldn’t have done it." **[M2011-015]**). Could a well-funded
  rival take this business? For 58.3% of sales the answer is in the contracts: the brand belongs to the licensor, the licence
  runs for a fixed term, and "after the term of any license agreement has concluded, the licensor may decide not to renew
  with the Company" (10-K FY2026, Item 1A). The attacker need not build a brand; it need only outbid Movado's royalty and
  minimums at renewal. Licences do move between licensees: Kate Spade New York watches move to Movado from spring 2027, and
  Fossil's FY2025 10-K (`0000883569-26-000017`) lists its licensed brands as Armani Exchange, Diesel, Emporio Armani, Michael
  Kors, Skechers and Tory Burch, with no Kate Spade. What one licensee can win, another can take. **Answer: yes.**
- **Pricing power and the agony before a rise** ("a prayer session before you raise your prices a penny" **[M2005-020]**).
  The company says it in so many words: "All of the Company’s brands compete with a number of other brands not only on
  styling but also on wholesale and retail price. The Company’s ability to improve margins through price increases is
  therefore, to some extent, constrained by competitors’ actions." (10-K FY2026, Item 7). Facing the 2025 tariffs it wrote
  that it "may seek to raise prices, which could reduce demand and result in loss of customers" (Item 1A). In FY2026 tariffs
  cost about 150 basis points of gross margin (Item 7); the margin was held by mix and by cutting marketing $14.1M, not by
  price. The opposite of "Anytime you can charge more for a product and maintain or increase market share" **[M2000-031]**.
- **Unit volume and share of mind** **[M1997-099]**. Owned-brand net sales, which carry the higher gross margin (Item 7):
  FY2016 $219.0M (then called the luxury brands category: Movado, Ebel, Concord, ESQ; 10-K FY2016); FY2022 $249.9M (now including Olivia Burton and MVMT); FY2023
  $230.3M; FY2024 $198.6M; FY2025 $183.6M; FY2026 $172.5M (10-K FY2016, FY2023, FY2025 and FY2026 segment notes). Down 31%
  in four years, and in FY2026 below the FY2016 figure although two brands bought for $177M of cash sit inside it. The only
  owned growth in the decade was bought, and the bought growth was written off.
- **The low-cost position.** None claimed and none shown: the company outsources all manufacture to independent assemblers
  without "long-term supply commitments" (Item 1A) and competes with Swatch Group, "a large Swiss-based competitor" with
  "greater financial, distribution, marketing and advertising resources" (Item 1). No filing fact supports a cost advantage.
- **The brand in the customer's mind** ("you’re probably going to get better gross of margins if they ask for you by
  name." **[M2023-073]**; "the brand has to stand for something in the consumer’s mind." **[M2015-038]**). The names the
  customer asks for in 58.3% of sales are Coach, Tommy Hilfiger, Hugo Boss, Lacoste and Calvin Klein, which are the
  licensors' assets; the company "has little or no control over the brand management efforts of its licensors" (Item 1A).
  Between a distributor and the brand owner, "the value of having the brand moves over" to whoever the customer trusts
  **[M2001-090]**; here that is the licensor, who takes it as a royalty. For the owned Movado brand, the company runs 57
  outlet stores to "sell current and discontinued models" (Item 1), $103.0M of sales in FY2026: the Movado brand is sold at
  a discount by its own owner as a regular channel, the thing a strong watch brand does not want, "any more than Rolex wants
  somebody discounting their watches." **[M2002-129]**.
- **Would the customer still choose it over the low bid?** **[M2017-009]**. The 10-K's own words: the products "compete on
  the basis of price, features, brand image, design, perceived desirability and reliability", and the company faces
  smartwatch makers with "significantly greater financial, distribution, advertising and marketing resources" (Item 1A). A
  watch whose job a phone or a smartwatch now does is not chosen for necessity; it is chosen for fashion, and fashion is "a
  product that has a whole bunch of competitors" **[M2023-074]**.
- **The intermediaries.** "the brand is our protection against the intermediaries making all the money." **[M2019-041]**.
  Movado sits between two stronger parties: licensors who own the brands and department stores and jewelry chains who own
  the shelf ("Future reorganizations, changes of ownership and consolidations could further reduce the number of retail
  doors", Item 1A). The co-operative advertising and "retail media network programs" it pays wholesale customers (Item 1)
  are rent paid to the shelf; "the struggle between the manufacturers of brands and retailers will go on and on and on and
  become more intensified." **[M2006-091]**.
- **Ask the competitors** **[M1999-130]**. Not done by interview. The competitor's own filing speaks for it: Fossil names
  Movado among its traditional-watch competitors and says that it "exited" the smartwatch category to refocus on traditional
  watches (FOSL 10-K FY2025, `0000883569-26-000017`).
- **Widening or narrowing** ("whether it’s likely to widen further or shrink on you" **[M1999-108]**). Narrowing, on every
  measure the filings give. Operating margin: FY2015 12.2%, FY2016 11.8%, FY2017 9.8%, FY2018 7.6%, FY2019 9.2%, FY2020 6.1%,
  FY2021 2.7% before impairments, FY2022 16.0% and FY2023 15.5% (the post-pandemic restocking), FY2024 7.3%, FY2025 3.1%,
  FY2026 4.4% (10-K income statements; FY2023 and FY2024 as restated). Pre-tax return on tangible capital employed (operating
  income against assets less cash, goodwill, intangibles and current liabilities; COMPUTATION from the filed balance sheets):
  23.5% and 25.3% in FY2015 and FY2016, 7.5% in FY2026 (9.1% leaving out the operating-lease assets booked from FY2020, so
  the comparison is not an artifact of the lease rule). The notch is lost and lost again **[L1995-023]**.
- **What could destroy, modify or reduce it** **[M2000-014]**: the loss of a licence (Hugo Boss and Calvin Klein both
  expire 2026-12-31; the 10-K says of Calvin Klein only that "preparations are underway for an extension", and of Hugo Boss
  that the company has rights to extend "upon satisfaction of specified conditions"); one more step in the substitution of
  the smartwatch for the fashion watch, in the decade in which Fossil, which Movado's 10-K names among its moderate and
  fashion competitors, lost 71% of its revenue: "If the technology had not changed, they’d still be impregnable franchises. But the technology did change."
  **[M2006-065]**.

**The competitor row** (same metrics, competitors' own filings):

| | revenue, first year | revenue, last year | operating income, first year | operating income, last year | source |
|---|---|---|---|---|---|
| Movado (FY to Jan) | $587.0M (FY2015) | $671.3M (FY2026) | $71.5M (12.2%) | $29.8M (4.4%) | 10-K XBRL; FY2026 `0001193125-26-115298` |
| Fossil (FY to Dec/Jan) | $3,509.7M (FY2014) | $1,004.4M (FY2025) | $566.5M (16.1%) | -$19.1M (-1.9%) | FOSL 10-K `0001047469-15-000992`; `0000883569-26-000017` |
| Swatch Group | not obtained | | | | non-SEC (SIX Swiss Exchange); **flagged, not read** |
| Citizen Watch | not obtained | | | | non-SEC (Tokyo); **flagged, not read** |
| Seiko Group | not obtained | | | | non-SEC (Tokyo); **flagged, not read** |

Fossil's traditional watches were $814.6M in FY2025, 81.1% of its sales; its smartwatches $11.8M (FOSL 10-K FY2025). The
U.S.-listed fashion-watch house Movado names as a competitor lost 71% of its revenue and all of its operating income in
eleven years. Movado lost less,
by buying two brands, adding Calvin Klein in 2022 and keeping its outlets, and still lost more than half of its operating
margin. The industry's insiders do write this down: Fossil's filing records the exit from smartwatches and the retreat to
"core businesses" (FOSL 10-K FY2025).

**The contrary evidence, weighed.** (a) Survival is not a castle: the speakers' failing answer is the business that leads
now and has no reason that lasts, "Roman Candles" **[L2007-004]**; surviving a decline by paying out all earnings and holding
cash is the shape of a business keeping its capital in "a declining operation", not of a moat. (b) The long licensor
relationships are evidence of execution, which is real, but it is a moat the company must win again at each renewal, and "A
moat that must be continuously rebuilt will eventually be no moat at all." **[L2007-005]**; the 19.5% to 22.4% of sales spent
on marketing each year is the cost of the rebuilding. (c) Licensed growth in FY2026 and the first half of FY2027 is the
licensors' brands growing in Movado's hands, partly as a weaker licensee retreats; it is share won in a shrinking category,
and Movado's own figures show it did not stop the owned-brand decline. (d) A small, unattractive market served with
"fanaticism in service" **[M2011-017]** can be a moat, but no filing fact shows Movado's customers paying for service, and
the department-store and marketplace channels it sells through are not small or unattractive to rivals. (e) A battery-like
"unit declines over a period of time, but I think we’ll do fine" **[M2015-066]** was said of a business that owned its brand;
here 58% of the brand value is rented. (f) The first-half rebound could be "a cyclical problem, not a secular one"
**[L1995-022]**; but the ten-year margin and owned-brand series run through two cycles, and the one rebound in them (FY2022
to FY2023) was followed by the lowest margins of the decade.

**Mistake the speakers narrate that this resembles.** Dexter: "We had a good brand name. We had great workmanship. And we
found out that it just plain wouldn’t work" **[M2008-013]**, and "we assumed that the future would be as good as the past"
**[M2003-077]**; and the speakers' own reading of their errors, "it’s where I misgauged the competitive position of the
business." **[M2012-031]**.

- **VERDICT: OUT.** The castle is shown on the evidence to be filling in, not merely uncertain: the owned brands shrank 31%
  in four years and below their FY2016 level despite $177M of acquisitions, $155.9M of which was written off; the majority
  of sales rides on fixed-term rented brands that a richer licensee can bid away **[M2011-015]**; the company records that
  its prices are set by competitors' actions **[M2005-020]**; the margin has fallen from 12% to 4% and the return on tangible
  capital from about 24% to under 8% **[M1999-108]**; and Fossil, the fashion-watch competitor Movado's 10-K names, lost 71% of its revenue in the decade both companies' filings
  name the smartwatch as a competitor **[M2006-065]**, **[M2007-117]** ("you do not want to have something whose competitive position is going
  to erode over time."). A castle shown open on the evidence closes OUT **[M2011-015]**, **[M2006-013]**, and price does not
  reopen it: "What you can’t do is turn any investment into a good deal by paying little" **[M2019-015]**; "If you really
  think a business is declining, most of the time you should avoid it." **[M2012-062]**; "marginal businesses purchased at
  cheap prices may be attractive as short-term investments" **[L2014-009]**, which is not this framework's question.
- **Why OUT and not TOO HARD.** The framework sends to TOO HARD the castle whose future cannot be judged (Q2, What it rules
  OUT), on the row "it’s just too risky. We don’t know how to valuate that, and therefore we leave it alone." **[M2000-019]**. This
  castle's future was judged from ten years of its own filings and its largest peer's: the direction is down. What cannot be
  judged is the speed, and the speed does not change the box.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**NOT REACHED** (Q2 closed the file OUT). The capital figures are in the COMPUTATION section below and are not a weighing.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**NOT REACHED.** Recorded as facts only, not judged: the FY2023 and FY2024 statements were restated for a five-year fraud by
the Dubai branch's former managing director (overstated sales, premature recognition, unreported credit notes, a third-party
warehouse "unknown to the Company’s management", falsified documents; FY2024 net sales cut $8.2M, FY2023 $7.7M, receivables
$18.4M, retained earnings $10.9M; 10-K FY2025 Note 1A); a material weakness was reported at FY2025 and declared remediated at
FY2026, PwC opining that controls were effective (10-K FY2026, Item 9A); the company "has received and responded to
information requests from the SEC" (Item 1A). The earnings releases feature "Adjusted operating income" ($34.x M against GAAP
$29.8M for FY2026; 8-K 0000950142-26-000775), and adjusted operating income is the bonus measure (proxy, CD&A). Had Q4 been
reached, these are the items it would have opened with **[M1995-064]**, **[L2002-039]**, **[L2016-006]**.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**NOT REACHED.**
Facts recorded, not judged: Efraim Grinberg, Chair since 2009 and with the company since 1980, holds 66.81% of the voting
power through 5,353,718 Class A and 502,952 common shares, about 26% of the economic shares (proxy, beneficial ownership
table; Grinberg Partners L.P. holds 3,055,640 of the Class A shares); his brother Alex Grinberg is a director; the two are
the only non-independent directors.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**NOT REACHED.**
Facts recorded, not judged: dividends of $31.1M in each of FY2025 and FY2026 against net income of $18.4M and $26.6M; a
$50M repurchase programme with no stated price, under which 208,000 shares were bought in FY2026 at an average $18.75 and
61,000 in the first half of FY2027 at $25.26 (10-K, Item 5; 10-Q); the FY2026 annual bonus was made discretionary ("it would
be impracticable to establish meaningful pre-set financial performance metrics") and paid at 90% of target; the chief
executive's FY2026 total compensation was $5,228,254 against operating income of $29.8M (proxy, summary compensation
table); the company sponsors The Movado Group Foundation and raised donations to it by $0.9M in FY2026 (10-K Item 7);
the company pays the premiums on life insurance whose cash surrender value belongs to the chief executive (proxy).

## Q7 — WHAT IS IT WORTH? STOP.
**NOT REACHED.** See the COMPUTATION section; it is not a clearance.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.**

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** (Fact: no debt; a $75M secured revolver to 2031, undrawn; 10-Q.)

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT ASKED** (the file closed at Q2).

---
## COMPUTATION — NOT A CLEARANCE
*(Made after the closing STOP, at the owner's request for a value range, a fair-price band and a cheap price. It carries no
entry language and does not reopen Q2: "What you can’t do is turn any investment into a good deal by paying little"
**[M2019-015]**. Script and output: `Test Runs/_research 2026-10-05 MOV/computation.py` and `computation_output.txt`.)*

**Owner cash after every real cost** (operating cash flow less stock pay less all capital spending; the depreciation variant
beside it; XBRL cash-flow tags from the 10-Ks, never net income; USD $M):

| FY (Jan) | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| OCF | 58.2 | 54.7 | 86.2 | 32.1 | 68.4 | 130.8 | 54.3 | 76.8 | -1.5 | 57.9 |
| owner cash, all capex | 45.0 | 44.0 | 69.6 | 13.0 | 60.3 | 120.1 | 41.5 | 61.2 | -13.6 | 48.2 |
| owner cash, D&A variant | 39.4 | 36.3 | 66.0 | 9.3 | 49.2 | 113.3 | 37.8 | 59.8 | -14.9 | 43.3 |

Capex runs $3.0M to $12.7M a year against D&A of $9.3M to $16.4M; the company calls its spending "primarily for projects in
the ordinary course of business" and "has the ability to manage its capital expenditures on discretionary projects" (10-K
FY2026, Item 7), so the all-capex figure is taken as the maintenance figure. Not deducted, and named: the $177M spent on
Olivia Burton and MVMT (FY2018 to FY2019), which was spent to hold the owned-brand line and is the strongest evidence that
standing still has cost more than capex. The cash swings are working-capital swings (inventory built in FY2023, released in
FY2024 and FY2026; FY2025's negative figure was tax payments and receivables).

- **Base (CONVENTION, Part VI):** five-year average FY2022 to FY2026 **$51.5M** (D&A variant $47.9M; ten-year average $48.9M),
  less an after-tax estimate of the interest on the cash pile ($2.7M: other income of $6.0M, $7.1M and $5.0M in FY2024 to
  FY2026, "primarily due to interest income", taxed at 25%, averaged over five years), leaving **$48.8M** of operating owner
  cash; the cash is then added at its July 2026 balance, $211.6M, with the note that $136.2M of the January balance sat
  abroad and "off-shore cash is simply not worth as much as cash held at home" **[L2016-009]**.
- **Growth shown** (aggregate owner cash, FY2016 $60.4M to FY2026 $48.2M): **-2.2% a year**. The five-year endpoints
  (FY2022 $120.1M, a post-pandemic restocking year) would show -20% a year, a base-year artifact **[L2005-003]**, so the
  ten-year span is used.
- **Value range at the sovereign 5.63%** (ten years at the growth shown, then no nominal growth; ends = no growth and shown
  growth): **$42.04 to $48.30 a share** against **$33.53**. Width 1.15 to one. Sensitivity, not the range: without the FY2022
  year (four-year base $31.6M) the range is $30.59 to $34.65; on the ten-year base ($46.2M), $40.33 to $46.27.
- **FAIR-PRICE BAND (COMPUTATION):** the prices at which the expected return is at or above the floor of about ten percent
  pre-tax (CONVENTION, Q7; **[L2002-020]**, **[M2003-149]**). Conversion: owner cash is after tax; the effective tax rate
  was 21.8% in FY2026 and 27.9% in FY2025 (10-K FY2026, Item 7), so 25% is used and ten percent pre-tax is taken as **7.5%
  after tax** (pre-tax = after-tax / 0.75). Discounting the same cash at 7.5%: **at or below $34.22** (shown decline) to
  **$38.63** (no growth); at 22% and 28% tax the band's top runs $33.32 to $39.84. **No price inside the value range
  ($42.04 to $48.30) reaches the floor**: the whole range sits above the floor prices, because the range is discounted at
  5.63% and the floor asks 7.5% after tax. The fair-price band therefore lies below the range, at about **$34 to $39**, and
  the price of $33.53 sits at its bottom edge: at $33.53 the no-growth case yields 9.1% after tax on enterprise value
  (about 12.1% pre-tax) and the shown-decline case about 6.7% after tax (about 8.9% pre-tax), straddling the floor.
- **CHEAP PRICE (COMPUTATION):** **about $21**, half the bottom of the range. CONVENTION, ours: the rows give no number for
  the price that needs no pencil; the nearest is "I didn’t need to know whether it was worth 97 billion or 103 billion if I
  was buying it at 35 billion." **[M2008-068]**, a price about a third of value; half is the less demanding reading. At
  $33.53 the case plainly needs a pencil: this section is the pencil, and "It should scream at you." **[M2009-005]**.
- **What the computation assumes that Q2 denies.** Every figure above assumes the five-year cash persists or shrinks 2.2% a
  year. Q2 found that 58% of sales sits on licences two of which expire on 2026-12-31 and that the owned brands shrank 31%
  in four years; a lost licence or another leg of the category's decline would put the cash below the four-year sensitivity
  case ($30.59), which is below the price. That is why the box is decided at Q2 and not here.

---
## THE BOX
**OUT**, decided at **Q2** (the castle shown filling in on the evidence). Not reached Q7; COMPUTATION only: value range
$42.04 to $48.30 against $33.53, fair-price band about $34 to $39 (below the range), cheap about $21.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch. [ ] Written question by question and committed after each: **not
      committed**, because this dispatch forbade commits; the file was written once, after the reading, in question order.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv`, every quoted fragment matched inside its
      row); every filing fact has its accession; no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q2 failed and closed the run; Q3 to Q12 are NOT REACHED and the facts recorded under them are not
      judged; the valuation is headed COMPUTATION — NOT A CLEARANCE and carries no entry language.
- [x] Owner cash from operating cash flow less stock pay less capex, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the price is an aggregator quote and is flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, items a to e; weighed at Q2).
- [x] No point-in-time anchor; not applicable.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its balance-sheet table was replaced, see the
      contamination note.
- [x] `python tools/check_framework.py` PASS (run after writing; result recorded in the session report).
- [ ] Not done: Swatch Group, Citizen and Seiko filings (non-SEC) were not read; the competitor row carries Fossil only.
      Scuttlebutt (licensors, department-store buyers) was not done; the castle was judged from filings alone **[M1998-144]**.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **The balance-sheet-first rule sits at Q4, but Q2 needs the income account.** Q2's tests (pricing power, widening or
narrowing, the return on capital the moat protects) cannot be run without margins, and the template reaches the balance
sheets only at Q4; a run that closes at Q2 would never read them. This run read them in Step 0, before Q1; the template
could say so. (2) **A licensee's castle is not addressed.** The brand rows (**[M2001-090]**, **[M2019-041]**, **[M2015-038]**)
are about the brand owner against the retailer; the rows found say nothing direct about a business whose brands are rented
on fixed terms. The nearest rows are a licence that "became a royalty stream" for its holder **[M2006-052]** and the
retailer battle. This run treated the licensor as the party holding the moat and the licensee as a contractor rebuilding its
position at every renewal **[L2007-005]**; that is the analyst's reading, not a speaker's, and another analyst could read the
twenty-year renewals as a moat in execution. (3) **The fair-price band and the range use two rates.** The range is
discounted at the sovereign (Q7) and the floor at about ten percent pre-tax (the CONVENTION). Whenever the after-tax floor
exceeds the sovereign, every price inside the range fails the floor, so the owner's "fair-price band inside the range" is
empty by construction for any business valued this way; the band was reported below the range instead and the reason
stated. The convention should say which rate builds the range the band is read against, and how pre-tax is converted (this
run used the company's own tax rate, 25%). (4) **The cheap price has no rule.** The owner asks for it and the framework gives
no number; this run used half the bottom of the range and confessed it. (5) **TOO HARD (WORK) against OUT at Q2.** The line
between "a castle whose future cannot be judged" and "a castle shown open on the evidence" is drawn by the analyst; here the
direction was judged from filings and the speed was not, and the run treated an unknown speed as not changing the box. The
framework does not say whether an unknown speed of decline is a cause of TOO HARD.
