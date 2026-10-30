# Company Run — Gulfport Energy Corporation (NYSE: GPOR) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied from the template to this dated name before any fetch** (the copy was the first action of the session; the working folder is `Test Runs/_research 2026-10-06 GPOR/`).

**POSITION NOTE, declared before any verdict:** NOT CHECKED. This is a blind run: the dispatch forbids opening
`PORTFOLIO.md`, any holding review, the resume-state file, the run queue, the prepped reading list, any other run file on
this company and other companies' 2026-10-05 and 2026-10-06 files. None was opened. Whether the operator holds GPOR is
unknown to this analyst.

**CONTAMINATION DECLARED.** (1) The session's opening context showed the five most recent commit subjects (AMN Healthcare
OUT at Q2, Innoviva OUT at Q1, Prestige Consumer Healthcare OUT at Q7, a publish-tool note, a session-state note) and a
git status listing three untracked 2026-10-05 run files by name (KTB, POOL, SBH). Their names and the three verdicts in
the subjects were seen; none of those files was opened. None concerns GPOR or a gas producer. (2) `tools/run.py` prints v4
material; only its arithmetic lines were read (Part VII). (3) I bring general knowledge that GPOR's predecessor filed
for Chapter 11 in November 2020; every fact used below is taken from the filings, not from memory.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $157.84 (close 2026-10-05; Yahoo chart via `tools/run.py`; **aggregator, live quote only, flagged** per
  operator rule 5). Closes the prior week: $152.17 (09-29) to $154.40 (10-02).
- **Shares by class** from the latest filing's cover: one class, common stock $0.0001 par, **17,683,866** shares
  (10-Q for the period ended 2026-06-30, filed 2026-08-04, accession `0001628280-26-052313`; `python Screens/cover_shares.py GPOR`).
  The preferred stock that existed from emergence was redeemed or converted in 2025 (10-K FY2025, accession
  `0001628280-26-011487`, MD&A "Recent Developments": 28,907 preferred shares converted into about 2.1 million common
  shares; the remaining 2,449 redeemed for $31.3 million on the Redemption Date), so no second class stands beside the
  common.
- **Market cap:** 17.684M x $157.84 = **$2,791M**.
- **Net debt:** principal of funded debt $797.0M at 2025-12-31 ($650.0M of 6.75% senior notes due 2029, $147.0M drawn on
  the credit facility maturing 2028-09-12), cash $1.8M (10-K FY2025, MD&A "Liquidity"). At 2026-02-19 the facility
  draw was $219.0M. Enterprise value on the year-end debt: about **$3,586M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 10/05/2026 (`python tools/sources.py`; issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-25, `0001628280-26-011487`); 10-Q Q2 2026 (filed
  2026-08-04, `0001628280-26-052313`); DEF 14A for the 2026 meeting (filed 2026-04-08, `0001213900-26-041489`); 8-K of
  2026-08-03 (`0001213900-26-084634`); the successor 10-Ks FY2021 (`0001628280-22-004445`), FY2022
  (`0001628280-23-005790`), FY2023 (`0001628280-24-007527`), FY2024 (`0001628280-25-008043`); the transition 10-K FY2020
  (`0001628280-21-004026`); the predecessor 10-Ks FY2013 (`0001445305-14-000751`), FY2014 (`0001628280-15-001182`),
  FY2015 (`0001628280-16-011417`), FY2016 (`0001628280-17-001359`), FY2017 (`0001628280-18-002041`), FY2018
  (`0001628280-19-002242`), FY2019 (`0001628280-20-002453`). Text copies and the scripts that read them are in the
  working folder.
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025 =
  **$803,193 thousand** in the 10-K's "Sources and Uses of Cash" table and the cash-flow statement
  (`0001628280-26-011487`); the XBRL fact `NetCashProvidedByUsedInOperatingActivities` for 2025 reads $803.2M. They agree.
  Additions to oil and natural gas properties FY2025: $527,569 thousand in the same table; XBRL
  `PaymentsToAcquireOilAndGasProperty` 2025: $527.6M. They agree.
- **`python tools/run.py GPOR`, arithmetic lines only.** The tool's owner-earnings window stops at FY2019 because it reads
  capital spending from `PaymentsToAcquireOtherPropertyPlantAndEquipment` ($5M to $19M a year, office equipment), not the
  drilling line; **its owner-earnings, yield and growth lines are therefore wrong for this company and are not used.**
  Its ten balance sheets are used below (COMPUTATION, part A), read against the filed statements. Owner cash is rebuilt
  from the filed cash-flow statements (COMPUTATION, part B; file `facts_table_out.txt` in the working folder transcribes every line by period with its
  accession).
- **The series break.** Fresh-start accounting at emergence on 2021-05-17 splits 2021 into a predecessor period
  (2021-01-01 to 2021-05-17) and a successor period (2021-05-18 to 2021-12-31) (10-K FY2021, `0001628280-22-004445`).
  Predecessor (2012 to 2020) and successor (2021-05-18 onward) are read separately below; the two 2021 stubs are added only
  where stated.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I would be content to own this "if the market closed for five years"
**[M1997-109]**, and for a gas producer that question is mostly a question about the price of gas over those five years,
which the speakers say they cannot answer: "we are not two fellows who think we can predict the price of soybeans or
corn or oil or anything else" **[M2016-025]**; "if you are going to try and figure out whether when to be long or short
oil, or natural gas, or copper or cotton or whatever, I don’t know of people who I feel would have an edge in trying to
do that over the next 10 years" **[M2011-047]**. So no gas-price forecast enters this run (no macro forecast,
**[M2000-094]**); where the value depends on the gas price, the run says so and treats the dependence as uncertainty in
the cash, not as a view. The margin of safety is the attitude carried to Q7: "if you have to actually do it on — with
pencil and paper, it’s too close to think about" **[M1996-084]**. Who is paid to tell you: the company's own PV-10 and its
free-cash-flow language are the seller's numbers, read and not adopted. The analyst's habits: the predecessor's
bankruptcy invites a story of a clean new company; the contrary evidence is written down as it is found.
**Contrary evidence, written down as found** **[M1997-127]**: (a) the predecessor wrote off $1,440M (2015), $715M (2016),
$2,040M (2019) and $1,357M (2020) of oil and gas property in ceiling-test impairments, and the successor a further $118M
(2021 successor period) and $373M (2024) (XBRL `ImpairmentOfOilAndGasProperties` from each year's 10-K; listed with
accessions in `facts_table_out.txt`); (b) from 2012 to 2019 the predecessor paid $7,883M in cash for oil and gas property (drilling and acreage
together) against $3,650M of operating cash flow (same source), a gap filled from outside the business (long-term debt
$2,038M by the end of 2017, `tools/run.py` balance-sheet table); (c) the 10-K FY2025 says of its
own key variable: "The volatility of the energy markets makes it extremely difficult to predict future oil and natural
gas price movements with any certainty" (MD&A, "Commodity Price Risk", `0001628280-26-011487`); (d) the firm
transportation and gathering commitments still stand at $1,037.7M of future payments, $375.1M of them after 2030 (10-K
FY2025, contractual obligations table).

## THE STANDING RULE
The rule binds the buyer: a purchase would be paid in cash and sized so that no outcome for this company, including a
second bankruptcy and a total loss, touches what the buyer has and needs: "We are never going to risk what we have and
need for what we don’t have and don’t need" **[M2012-081]**; "borrowed money has no place in the investor's tool kit"
**[L2014-005]**; "always be sure you can play the next day" **[M2025-015]**. Nothing in the run requires otherwise. The
target's own debt and commitments are weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (10-K FY2025, Item 1, `0001628280-26-011487`): a natural-gas-weighted producer; 2025 net
  production 1,039 MMcfe per day, 89% natural gas by volume (927 of 1,039), 81% from the Utica and Marcellus in eastern
  Ohio and 19% from the SCOOP in Oklahoma; proved reserves 4,253 Bcfe (2,404 developed, 1,848 undeveloped); 245
  employees; all production sold at market prices "under both spot and term transactions"; derivatives cover about 52% of
  expected 2026 gas. It drills about 25 to 30 net wells a year to hold production flat (2026 guidance: $400M to $430M of
  capital for 1.030 to 1.055 Bcfe per day, against 1.039 in 2025).
- **The key variables, and how predictable they are** **[M1998-044]**: (1) the price of natural gas at the Appalachian and
  Oklahoma hubs, net of basis; (2) the company's cost per unit, cash and capital; (3) the volume and life of the
  inventory. The second and third are on the record year by year and change slowly. The first is not predictable by the
  speakers' own account: "if you are going to try and figure out whether when to be long or short oil, or natural gas,
  [...] I don’t know of people who I feel would have an edge in trying to do that over the next 10 years" **[M2011-047]**;
  "We’re not going to comment, you know, on oil or the prices of anything in terms of making any forecasts about it."
  **[M2001-103]**. The company says the same of itself: "The volatility of the energy markets makes it extremely difficult
  to predict future oil and natural gas price movements with any certainty" (10-K FY2025, MD&A).
- **Test 4 against the speakers' practice.** "If something’s important but unknowable, forget it." **[M2006-076]** would
  close the file here if the gas price had to be forecast. The rows show the speakers did not treat a producer that way:
  they bought producers without a price view ("if we were in an oil stock, it’s because we think it offers a lot of
  value at this price, but it does not mean that we think the price of oil is going up" **[M2007-129]**), valued them on
  their own figures ("it was bought simply because it was very, very cheap in relation to earnings, in relation to
  reserves, in relation to daily oil production" **[M2004-082]**), and named the industry's economics as graspable ("a big
  integrated oil company, it’s fairly easy to get your mind around the economic characteristics that will exist in the
  business" **[M2004-081]**; "we think we understand something like the oil business in China reasonably well"
  **[M2003-118]**). What understanding asks is "a reasonable fix on about what the earning power and competitive position
  will look like in five or 10 years. So I’ve got some notion of how the industry will develop and where the company will
  stand within the industry." **[M2012-065]**, and for a business whose product is opaque "What is important is that I
  understand the economic dynamics of the industry. Is there — are there competitive moats? Is there ease of entry?"
  **[M2011-014]**. The economic dynamics here are plain from the filings: a price-taker selling an undifferentiated
  product, whose result "is going to depend on the price of oil to a great extent" **[M2020-035]** (gas, here), whose
  value is "the discounted value of the oil that’s going to come out. And then you have to make an estimate as to volume
  and as to price." **[M2002-079]**, and whose wells decline fast, the case Munger describes: "in a year, year and a half,
  it becomes partly nothing. It’s a different business in effect." **[M2023-082]**.
- **Where it will stand in ten years** (tests 1 and 6): a small Appalachian and Oklahoma gas producer, still a price
  taker, still drilling about $400M a year to stay flat, on an inventory whose proved part is 4,253 Bcfe against 379 Bcfe
  a year produced (11.2 years; developed reserves 6.3 years). That is foreseeable. Its earning power in dollars is not,
  because it is a multiple of the gas price; that unknowable is carried to Q2 (whether a commodity seller has any castle
  against it) and Q7 (how wide the range is), which is where the rows put it for a commodity producer.
- **Routing.** No fast-moving technology governs the economics (drilling technique moves cost, the product does not
  change); the business is not a financial institution; it is not a holding company (the 24.5% Grizzly oil-sands stake has
  been suspended since 2015 and is not funded, 10-K FY2025, Item 1).
- **VERDICT: IN**, narrowly: the economic dynamics and the competitive position are understood from the filings
  **[M2012-065]**, **[M2011-014]**, on the speakers' own treatment of producers **[M2007-129]**, **[M2004-081]**; the gas
  price, the one important unknowable, is carried to Q2 and Q7 rather than ruled on here (see "What in the framework was
  wrong or unclear", item 1, for why this routing is a choice).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**.

**Is it a commodity business?** Yes, on the filing's facts. The product is natural gas, NGL and oil, sold at hub prices
"under both spot and term transactions"; no customer asks for Gulfport's gas by name; the largest purchaser took 14% of
2025 sales (10-K FY2025, Item 1, "Major Customers"); the company competes "with many other companies that have greater
resources than we have" (Item 1, "Competition"). The rows' marks of a commodity apply: "most insureds don't care from whom
they buy" **[L2004-003]** (here, buyers of gas at a hub); and the rival, here the market, sets the price: "whatever he
charged for gas was my price. (Laughs) I didn’t have much choice. You don’t like to be in a business like that."
**[M2012-109]**; "he determined our profit, because we looked at his price every day" **[M2023-079]**. Gulfport's realized
price before hedges was $6.49, $2.73, $2.41 and $3.49 per Mcfe in 2022, 2023, 2024 and 2025 (10-K FY2022
`0001628280-23-005790`; 10-K FY2025), moving in step with every competitor in the row below; nothing the company did set it.

**The castle tests, each with its filing fact.**
1. *The castle questions* **[M1995-038]**: the filing names no lasting key factor other than acreage, cost and hedging; the
   company's own statement of strategy is to generate sustainable free cash flow (10-K FY2025, Item 1), not to hold an
   advantage.
2. *Would it stand without the lord?* Not reached as a castle question: there is no castle for a lord to keep.
3. *The money test* **[M2011-015]**: "if I had a hundred million dollars and I wanted to go in and take on See’s Candy,
   could I do it? And I came to the conclusion, no, so we bought See’s Candy. If the answer had been yes, we wouldn’t have
   done it." Here the answer is yes, shown by the company's own conduct: the predecessor bought its SCOOP position from
   Vitruvian (10-K FY2016 `0001628280-17-001359`, Item 1: purchase agreement dated December 13, 2016), and the successor buys
   acreage every year ($95.6M of leasehold paid in 2025, of which $62.9M incurred on "discretionary acreage acquisitions",
   10-K FY2025, MD&A). Acreage and wells are for sale to anyone with money: "there are some industries that are just never
   going to have barriers to entry" **[M2012-106]**.
4. *Pricing power* **[M2005-020]**: none; the price is the hub's. The company hedges because it cannot set price (10-K
   FY2025, Item 7A).
5. *Unit volume*: falling, not rising: 1,375 MMcfe per day in 2019 (10-K FY2019 `0001628280-20-002453`), 983 in 2022, 1,054
   in 2023 and 2024, 1,039 in 2025, 963 in the second quarter of 2026 (10-Q `0001628280-26-052313`), below the 1,030 to
   1,055 guided for the year. Share of mind does not apply to a hub molecule.
6. *The low-cost position*: tested in the competitor row below. The rows' exception for a commodity seller is to be the
   low-cost producer: "when a company is selling a product with commodity-like economic characteristics, being the
   low-cost producer is all-important" **[L2000-017]**; "commodity businesses have risk unless you’re the low-cost producer,
   because the low-cost producer can put you out of business" **[M1997-010]**; cost is read against the competitor: "if
   your costs are on parity or less — labor costs — than your other major competitors, that is much more important to you
   than the absolute level" **[M2001-013]**; "It’s like comparing a copper producer whose costs are $2.50 a pound with a
   copper producer whose costs are $1 a pound. Those are two different kinds of businesses." **[M2009-059]**. In this
   industry the speakers name the figure that decides it: "finding cost per McF or per barrel of oil [...] That’s the most
   important figure in an oil and gas company over a period of years" **[M2007-082]**; "a person who finds oil and develops
   reserves at $6 a barrel is worth a lot more than somebody that finds and develops them at $10 a barrel" **[M2007-009]**.
7. *Brand*: none.
8. *Would the customer still choose it over the low bid?* No: gas is bought on price at the hub.
9. *Ask the competitors* **[M1999-130]**: not answerable from the public record. A search for "Gulfport" in the five
   competitors' 10-K FY2025 texts found one mention: CNX lists it in the peer group of its stock-performance graph, beside
   Antero, Expand, EQT and Range (which supports this run's choice of peers, and says nothing of the castle). Recorded and
   set aside.
10. *Widening or narrowing* **[M1999-108]**: narrowing in scale. Gulfport produced 1,375 MMcfe per day in 2019 and about
    1,000 since emergence; the competitors consolidated: EQT 6,527 MMcfe per day in 2025 (EQT 10-K FY2025
    `0000033213-26-000018`), Expand Energy (Chesapeake and Southwestern) 7,183 (EXE 10-K FY2025 `0000895126-26-000011`),
    Antero 3,442 (AR 10-K FY2025 `0001104659-26-013386`), Range 2,236 (RRC 10-K FY2025 `0001193125-26-067292`), CNX 629.0
    Bcfe for the year, about 1,723 per day (CNX 10-K FY2025 `0001070412-26-000038`). Gulfport is the smallest of the six.
11. *What could destroy it, five to fifteen years out* **[M2000-014]**: a long spell of low gas prices against fixed
    transport and gathering commitments ($1,037.7M still owed, $375.1M of it after 2030, 10-K FY2025 contractual
    obligations) and debt. That is what happened once. The predecessor's firm transportation commitments stood at
    $3,560.5M at the end of 2019 (10-K FY2019, contractual obligations); it filed for Chapter 11 on November 13, 2020; the
    restructuring agreement required it to "permanently reduce its future demand reservation fees owed over the life of all
    of its firm transportation agreements, taken as a whole, by at least 50 %" (10-K FY2020 `0001628280-21-004026`, notes);
    its old common stock was cancelled and the noteholders took the new equity (10-K FY2021 `0001628280-22-004445`, notes:
    160.9M predecessor shares and $4.22bn of paid-in capital cancelled; noteholders received 19.7M new shares, the new
    preferred and $550M of new notes; old equity received nothing). The speakers name this error in a credit tied to gas:
    "the assumption there was that gas prices would stay roughly as high as they were or go higher, and instead they went
    a whole lot lower." **[M2014-037]**.

**The competitor row** (each company's own 10-K; per Mcfe; *cash margin* = realized price before derivative settlements
less lease operating expense, production and ad valorem taxes, and gathering, processing and transportation; *capital* =
cash capital spending divided by production). Sources: Gulfport 10-Ks FY2019, FY2020, FY2022, FY2025 (accessions in Step 0;
2018 and 2019 as restated gross of firm transport in the 10-K FY2020, which moved the same dollars out of revenue and into
cost, leaving the margin unchanged: 2019 first-filed $2.27 less $0.81 = $1.46, restated $2.70 less $1.22 = $1.48); EQT
10-Ks FY2019 `0000033213-20-000008`, FY2022 `0000033213-23-000008`, FY2025; Antero 10-Ks FY2019 `0001558370-20-000726`,
FY2022 `0001558370-23-001378`, FY2025; Range 10-Ks FY2019 `0001564590-20-007459`, FY2022 `0000950170-23-004687`, FY2025;
CNX 10-Ks FY2019 `0001070412-20-000011`, FY2022 `0001070412-23-000015`, FY2025; Expand 10-K FY2025. Texts in
`Test Runs/_research 2026-10-06 GPOR/peers/`.

| cash margin $/Mcfe | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| **GPOR** | 2.16 | 1.48 | 0.69 | 2.83 (both stubs) | 5.15 | 1.56 | 1.24 | 2.24 |
| EQT | 1.88 | 1.24 | 0.53 | 2.50 | 5.00 | not read | 0.86 (a) | 1.91 (a) |
| AR (b) | 1.39 | 0.72 | 0.14 | 2.43 | 4.42 | 1.03 | 0.82 | 1.43 |
| RRC | 1.93 | 1.06 | not read | 2.48 | 4.58 | 1.41 | 1.15 | 1.78 |
| CNX | 2.02 | 1.40 | not read | 2.98 | 5.46 | not read | 1.22 | 2.25 |
| EXE | (c) | (c) | (c) | (c) | (c) | not read | 1.11 | 2.01 |

| capital $/Mcfe produced | 2018 | 2019 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| **GPOR** (all oil and gas property spending) | 1.81 | 1.44 | 1.28 | 1.40 | 1.18 | 1.39 (drilling only 1.07) |
| RRC | 1.20 | 0.82 | not read | 0.73 | 0.72 | 0.71 |
| AR (drilling and unproved leasehold) | not read | not read | not read | 0.90 | 0.56 | 0.65 |
| CNX (all capital) | not read | not read | not read | not read | 0.98 | 0.79 |
| EQT (all capital, pipelines included from the 2024 merger) | not read | not read | not read | about 1.00 | 1.01 | 0.96 |
| EXE (all capital) | (c) | (c) | (c) | not read | 1.13 | 1.04 |

(a) EQT's 2024 and 2025 costs include "transportation and processing to affiliate", eliminated in consolidation after the
Equitrans merger, so its consolidated cash margin is higher than shown. (b) Antero's price carries a large NGL uplift and
its cost a matching processing charge; its margin is comparable in total, not line by line. (c) Chesapeake was oil-weighted
until 2021 and is not comparable before the Southwestern merger. "Not read": the filing for that year was not fetched; the
gap is recorded, not filled.

**What the row says, the evidence for the company written down first** **[M1997-127]**: on *cash* margin Gulfport is not
the high-cost producer. It is first or second of the six in most years read, level with CNX and ahead of EQT, Range and
Antero. That is real and it counts in its favour. On *capital* per unit, the cost the speakers call "the most important
figure in an oil and gas company over a period of years" **[M2007-082]**, it is the highest of the six in every year read:
about $1.2 to $1.4 per Mcfe produced to stand still, against about $0.7 at Range and $0.6 to $0.9 at Antero. The
predecessor's record shows where that leads over a cycle: operating cash flow less stock pay less capital spending was
negative in every year from 2014 to 2020, **-$3,372M** in total (XBRL facts from each year's 10-K, `owner_cash_out.txt`);
ceiling-test impairments took $5,552M of capitalized cost in 2015, 2016, 2019 and 2020; proved reserves were revised down
by 1,725 Bcfe in 2020 (10-K FY2022, supplemental reserve roll-forward); and the owners were wiped out. Of the six, two filed
for Chapter 11 in 2020, Gulfport and Chesapeake (now Expand); EQT, Antero, Range and CNX did not. The low-cost title, "the
low-cost producer (GEICO, Costco)" **[L2007-004]**, does not belong on this evidence to the smallest and most
capital-hungry member of the field; and "In an unregulated commodity business, a company must lower its costs to
competitive levels or face extinction." **[L1994-035]**, which the predecessor did not do and faced.

**The other route through a commodity field.** **[L2004-007]** opens "Another way to prosper in a commodity-type business
is to be the low-cost operator", and names NICO's "ebb-and-flow business model"; section VI carries the second route open.
Gulfport's model is the opposite of ebb and flow: a flat drilling program run through every price, production held at
about 1,040 MMcfe per day through the 2024 trough (10-K FY2025). No second route was found in the filings.

- **VERDICT: OUT.** A commodity seller whose price the market sets **[M2012-109]**, **[M2023-079]**, whose buyers do not
  care from whom they buy **[L2004-003]**, whose field anyone with money can enter by buying acreage **[M2011-015]**,
  **[M2012-106]**, and which is not the low-cost producer on the measure the speakers name for this industry
  **[M2007-082]**, **[M1997-010]**, **[L2000-017]**: a castle shown open on the evidence. "We’re going to be investors in
  businesses, not commodities, by and large." **[M2007-131]**. The box is OUT, not TOO HARD: the castle's future is not
  unjudgeable, there is no castle; and a lower price does not reopen it: "What you can’t do is turn any investment into a
  good deal by paying little" **[M2019-015]**.

**The file closes here.** Q3 to Q12 are NOT REACHED. Everything below is COMPUTATION — NOT A CLEARANCE, written at the
owner's request and for the record; it carries no entry language.

---
## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED as a verdict; the balance sheets are read below as the template asks when the file closes before Q4.
## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 — WHAT IS IT WORTH. NOT REACHED as a verdict; the owner's figures are below as COMPUTATION.
## Q8, Q9, Q10, Q12. NOT REACHED.

---
## COMPUTATION — NOT A CLEARANCE
*Written after the file closed OUT at Q2, at the owner's request (value range, a whole-cycle variant, a fair price and a
cheap price) and for the record. Nothing here reopens Q2; none of it is entry language. Arithmetic in
`Test Runs/_research 2026-10-06 GPOR/owner_cash.py`, output in `owner_cash_out.txt`.*

### A. The balance sheets, ten year-ends, before the income account
(USD millions; `tools/run.py` transcription of the first-filed XBRL, checked against the filed statements of equity in the
10-Ks FY2022 and FY2025 for 2020 to 2025: equity -$300.5M at 2020, $639.7M at emergence, $549.5M, $828.8M, $2,161.7M,
$1,711.4M, $1,834.7M, all agreeing.)

| year-end | assets | liabilities | equity | cash | receivables | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|
| 2017 | 5,808 | 2,706 | 3,102 | 100 | 182 | 2,038 | -1,276 |
| 2018 | 6,051 | 2,723 | 3,328 | 52 | 210 | 2,087 | -845 |
| 2019 | 3,883 | 2,568 | 1,315 | 6 | 121 | 1,978 | -2,848 |
| 2020 | 2,540 | 2,840 | -300 | 90 | 120 | 0 (in liabilities subject to compromise) | -4,473 |
| 2021-05-17 (fresh start) | 2,253 | 1,558 | 640 | 2 | 181 | 793 | 0 |
| 2021 | 2,168 | 1,561 | 549 | 3 | 233 | 713 | -113 |
| 2022 | 2,534 | 1,653 | 829 | 7 | 278 | 694 | 382 |
| 2023 | 3,268 | 1,062 | 2,162 | 2 | 122 | 667 | 1,848 |
| 2024 | 2,866 | 1,117 | 1,711 | 1 | 156 | 703 | 1,582 |
| 2025 | 3,030 | 1,195 | 1,835 | 2 | 185 | 788 | 1,835 |

What the figures say. (1) The predecessor's equity went from $3,328M (2018) to -$300M (2020) in two years, by the
$2,040M and $1,357M ceiling-test write-downs, while its debt stayed at about $2.0bn: the assets shrank and the claims did
not. (2) There is no goodwill or intangible in any year; the assets are wells and acreage carried under the full-cost
method, written down to a ceiling set by twelve-month average prices (10-K FY2025, critical accounting policies), so the
book value moves with the gas price. (3) Cash is near zero in every successor year; the company runs on its revolving
credit facility, whose borrowing base is redetermined twice a year "based primarily on projected future cash flows"
(10-K FY2025, MD&A): the lender's switch, held by the lender. (4) The successor's equity jump in 2023 (+$1,333M) is mostly
not cash: net income of $1,471M that year included a $525.2M income tax benefit from releasing the valuation allowance
on the deferred tax asset and $740.3M of derivative gains (XBRL `IncomeTaxExpenseBenefit`,
`GainLossOnDerivativeInstrumentsNetPretax`, 10-K FY2025), of which settlements were only about $154M ($0.40 per Mcfe on
384.8 Bcfe, 10-K FY2025 production table). At the end of 2025 the deferred tax asset is $465.7M of the
$3,030M of assets, resting on a $1.5bn federal net operating loss (10-K FY2025, income-tax note): "what the figures
are saying and what they don’t say and what they can’t say" **[M2025-032]**: they cannot say whether that asset is
realized, which depends on future gas prices. (5) Long-term debt has stayed at $0.67bn to $0.79bn since emergence and rose
to $922.3M at 2026-06-30 (10-Q `0001628280-26-052313`) while the company bought back stock: the buybacks are partly
borrowed. (6) Receivables follow the gas price ($278M at the 2022 peak, $122M in 2023), not sales effort.

### B. Owner cash after every real cost (successor; USD millions)
Operating cash flow less stock pay, less all cash capital spending on oil and gas property (drilling, leasehold and
other), less preferred dividends paid, less the cash paid to settle performance stock units in 2025 (stock pay paid in
cash outside operating cash flow, 10-K FY2025, sources and uses of cash). Interest is inside operating cash flow; cash
income taxes were nil to $1.2M a year (XBRL `IncomeTaxPaidFederalAfterRefundReceived`, `IncomeTaxesPaidNet`), so owner
cash here is effectively pre-tax.

| year | OCF | stock pay | capital | preferred dividends | cash-settled PSUs | **owner cash** | per Mcfe | D&A variant |
|---|---|---|---|---|---|---|---|---|
| 2021 (both stubs) | 465.2 | 3.2 | 309.4 | 1.5 | 0 | **151.1** | 0.41 | 236.8 |
| 2022 | 739.1 | 5.7 | 460.8 | 5.4 | 0 | **267.2** | 0.74 | 460.2 |
| 2023 | 723.2 | 9.5 | 537.4 | 4.8 | 0 | **171.5** | 0.45 | 389.2 |
| 2024 | 650.0 | 11.0 | 454.1 | 4.2 | 0 | **180.7** | 0.47 | 309.1 |
| 2025 | 803.2 | 12.2 | 527.6 | 1.7 | 12.3 | **249.4** | 0.66 | 472.8 |
| five-year mean | | | | | | **204.0** | | 373.6 |

Sources: XBRL facts by period (`facts_table_out.txt`) from the 10-Ks FY2021 to FY2025; preferred dividends from the
cash-flow statements (10-K FY2022 and FY2023: $5.4M, $4.8M; 10-K FY2025: $4.2M, $1.7M; 2021 successor $1.5M); the 2021
figure joins the predecessor stub to the successor stub (any bankruptcy cash costs sit inside the predecessor stub's
operating cash flow) and is flagged. **The maintenance judgment:** production was 1,054,
1,054 and 1,039 MMcfe per day in 2023, 2024 and 2025 (10-K FY2025), so all of the capital in those years was spent to stand
still, and the D&A variant (D&A of $304M to $326M on the fresh-start written-down base) understates the true cost; the
2026 guidance of $400M to $430M for flat production says the same. The all-capital figure is the one used.
The predecessor, same arithmetic (OCF less stock pay less capital): 2014 -928.3, 2015 -1,265.5, 2016 -394.5, 2017 -391.2,
2018 -119.6, 2019 -1.0, 2020 -272.0; **-3,372.1 in total**.

The 2022 gas spike is in the window but barely in the owner cash: realized hedge losses of $2.94 per Mcfe that year (10-K
FY2022) took the realized price including derivatives to $3.55, against $3.13 to $3.64 in the other successor years. The
window's mean realized price including derivatives, $3.34 per Mcfe, sits $0.24 above the 2015 to 2025 mean of $3.10
(own 10-Ks; the 2015 to 2017 prices were reported net of some transport and so understate the gross price).

### C. The value range (Q7 CONVENTION construction), with variants
Sovereign 5.66%; 17.684M shares; price $157.84; market cap $2,791M; net debt $795.2M (year-end 2025).
- **Growth shown and its cap.** Owner cash rose from $151.1M (2021) to $249.4M (2025), 13.3% a year, but the rise is the
  gas price and the emergence-year costs, not the business: production went from 983 to 1,039 MMcfe per day from 2022 to
  2025, 1.86% a year, and fell to 963 in the second quarter of 2026. The high end is capped at the production growth shown
  (CONVENTION of this run: the framework caps growth "by the growth arithmetic of Q3", and Q3 was not reached; a
  price-driven rate cannot be the business's growth). The 13.3% case is shown and not used.
- **The range by the convention** (five-year mean, ten years, then no growth, at 5.66%): **$204 a share (no growth) to
  $236 (1.86%)**, against $157.84. Ratio 1.16 to 1. On the four successor full years (mean $217.2M): $217 to $251.
- **Variant 1, a depleting asset** (CONVENTION of this run: the perpetuity assumes the inventory never runs out; proved
  reserves are 11.2 years of production): the same cash for 11 years then nothing, $93 a share; for 15 years, $115; for 20
  years, $136.
- **Variant 2, whole cycle** (the owner's request): the 2025 cost structure (cash costs $1.25, G&A $0.11, interest $0.14 per
  Mcfe, maintenance capital $1.09 per Mcfe from the 2026 guidance midpoint) at 2025 volume, with the realized price
  including hedges set at the 2015 to 2025 mean of $3.10: owner cash about $193M a year, $193 a share as a perpetuity.
- **Variant 3, the price as the input.** Each $0.10 per Mcfe of realized price is about $38M a year of owner cash and about
  $38 a share of perpetuity value. At the realized prices the company has actually had in its own filings since 2015
  ($2.53 in 2020 to $3.64 in 2025, hedges included), the same arithmetic runs from about **$4 a share at $2.60 to $398 at
  $3.64**: far wider than three to one. Had Q7 been reached, this, not the narrow convention range, is the honest width:
  "Usually, the range must be so wide that no useful conclusion can be reached." **[L2000-025]**; and a wide range is not
  cured by a bigger discount: "we don’t really try to compensate for that sort of thing by having some extra large margin
  of safety" **[M2007-022]**.

### D. The fair price and the cheap price (the owner's request)
- **Expected return at $157.84 on the central case:** owner cash $204.0M on $2,791M = 7.3% pre-tax with no growth, 9.2%
  with the 1.86% production growth. Both below the CONVENTION floor of about ten percent pre-tax ("we don’t want to buy
  equities where our real expectancy is below 10 percent" **[M2003-149]**).
- **FAIR PRICE: about $115 a share** (range $101 to $144). Rule: the price at which the central case (five-year mean owner
  cash, $204.0M, no growth) yields 10% pre-tax on the equity, i.e. after interest: $204.0M / 10% = $2,040M = $115.35 a share.
  Tax: owner cash is after cash taxes, which were nil, so it is pre-tax in practice; the $1.5bn net operating loss shields
  income for some years and is given no extra credit. On equity plus net debt the same floor gives $101 ((204.0 + 54.3
  interest) / 10% - 795.2 net debt); on the four successor full years, $123; with the 1.86% growth as a perpetuity at a 10%
  required return, $144.
- **CHEAP PRICE: about $85 a share.** Rule (CONVENTION of this run): the price below which the buyer gets the wells already
  drilled for less than their value net of all debt and the undeveloped inventory free: the PV-10 of proved developed
  reserves at year-end 2025, $2,291M (10-K FY2025, Item 1, at SEC prices of $3.39 per MMBtu Henry Hub and $66.01 WTI,
  discounted at 10%), less net debt $795.2M, = $1,496M = $84.59 a share. Cross-check: the central owner cash for 11 years
  only (the proved reserve life) at 10% is $1,325M = $75 a share. Below about $75 to $85 no pencil would be needed on
  these figures; at $157.84 the price is 87% above the cheap price and 37% above the fair price.
- None of these figures is an entry signal: the file is closed OUT at Q2, and a lower price does not reopen a castle that
  is not there **[M2019-015]**.

### E. Facts gathered for the questions not reached (record only)
- **Buybacks since emergence** (10-Ks FY2022 to FY2025; 10-Q Q2 2026): 2.9M shares for $250.8M in 2022 (average $86.47);
  1.5M for $148.9M in 2023, $40.4M of it bought from a related party; 1.2M for $184.5M in 2024 ($153.35); 1.8M for $336.3M in
  2025 ($188.65); 8.6M shares for about $1.2bn at an average $135.09 from the start of the program to 2026-06-30, including
  84,416 shares bought from Silver Point Capital on 2026-03-02 for about $17.2M (10-Q, related-party note; a Silver Point
  partner sits on the board, DEF 14A 2026). The program names no price. Shares outstanding: about 21.5M issued at
  emergence (19.8M plus 1.7M to the disputed-claims reserve), 17.68M at 2026-07-28; the preferred converted into at least
  3.6M common shares from 2023 to 2025 (statements of equity, 10-Ks FY2023 and FY2025).
- **Stock pay:** expense $12.2M in 2025, plus $12.3M of 2022 performance units settled in cash; the chief executive's 2025
  total in the summary compensation table $7,323,707 (DEF 14A 2026, `0001213900-26-041489`); the annual incentive scorecard
  includes LOE per Mcfe and "Adjusted Free Cash Flow" targets.
- **Hedging:** about 52% of expected 2026 gas hedged at an average floor of $3.74 per Mcf (10-K FY2025, MD&A); settled
  derivatives added $0.73 per Mcfe in 2024 and took away $2.94 in 2022.
- **Debt and commitments:** $650.0M of 6.75% notes due 2029; revolver $147.0M drawn at year-end 2025, $219.0M at 2026-02-19;
  long-term debt $922.3M at 2026-06-30; firm transportation and gathering $1,037.7M; letters of credit $48.7M and surety bonds
  $45.3M posted "primarily for certain firm transportation agreements" (10-K FY2025).

---
## THE BOX
**OUT, at Q2** (the castle shown open: a commodity seller whose price the market sets, which is not the low-cost producer
on the capital measure the speakers name for this industry; cash margin competitive, capital per unit the highest of six,
the predecessor bankrupt with old equity cancelled). Q7 not reached; for the record only (COMPUTATION): value range by the
convention $204 to $236 a share, honest width with the gas price as the input far wider than three to one; fair about $115;
cheap about $85; price $157.84.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question. Not committed: the dispatch forbids commits,
      so the write-early rule was kept by writing each part to the file as it closed, not by a commit after each.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (checked by script, see below); every filing fact carries its
      accession or names its filing; no number without a row, a filing or a CONVENTION label.
- [x] The order was kept; Q2 closed the file OUT; nothing after it is a clearance, and the computations are headed so.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy (operator rule 5); the
      sovereign from the US Treasury; the price quote flagged as an aggregator's.
- [x] Contrary evidence was written down as it was found **[M1997-127]**: in the foundations (impairments, cash burn,
      the company's own words on price, transport commitments), and in Q2 the evidence for the company (its cash margin
      among the best of six) written down before the evidence against it.
- [x] No row dated after the anchor: not a point-in-time run; the run is dated 2026-10-06 and every row is earlier.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings lines were rejected as reading the wrong
      capital-spending tag (Step 0).
- [x] `python tools/check_framework.py` PASS before closing the file (see the note at the end).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **Where a commodity price goes: Q1 or Q2.** Q1's test 4 ("If something’s important but unknowable, forget it."
   **[M2006-076]**) and test 2 ("If something is not very predictable, forget it." **[M1998-044]**) would close every
   commodity producer at Q1, TOO HARD (NATURE), because the price is the key variable and the speakers say no one can
   forecast it **[M2011-047]**. But Q2 has a full section on the commodity business and its exception, which assumes
   commodity businesses reach Q2, and the speakers bought producers without a price view **[M2007-129]**, **[M2004-082]**.
   The framework does not say which governs. I passed Q1 and decided at Q2; a second analyst could close the same name at
   Q1 TOO HARD (NATURE) with equal textual support, and the box would differ (OUT against TOO HARD). A one-line routing rule
   is wanted: whether an unforecastable output price is a Q1 matter or is carried to Q2 and Q7.
2. **The low-cost exception has no stated measure.** Q2 names the low-cost position as the exception but not what cost:
   cash operating cost, cost including capital, or finding cost. Here the answer turns on it: Gulfport is first or second of
   six on cash margin and last on capital per unit. I used the speakers' own industry-specific figure, finding cost
   **[M2007-082]**, through the capital-per-unit proxy, because the full-cost method's DD&A on a fresh-start base does not
   show finding cost. The framework should say which cost the exception means, or that it means all-in cost.
3. **The Q7 convention's perpetuity misfits a depleting asset.** "Ten years then no real growth" assumes the cash never
   ends; for a producer with 11 years of proved reserves the convention gives $204 a share and the reserve-life variant $93.
   The convention also lets the five-year mean of a commodity price stand in for the future; the range it produces (1.16 to
   1) looks narrow only because the price is held fixed. The three-to-one width test cannot fire unless the analyst varies
   the price, which the convention does not ask for.
4. **The growth cap points to a question that was not reached.** The convention caps growth "by the growth arithmetic of
   Q3"; when a file closes before Q3 and the owner still wants a range, nothing says what cap to use. I capped at the
   production growth shown and said so.
5. **The template's write-early rule assumes commits.** This dispatch forbade commits; the self-audit's first box cannot be
   ticked as written. Recorded rather than ticked silently.

---
**Checks run on this file, 2026-10-06.** `python tools/check_framework.py`: PASS (test runs: phantom ids in 0 files; v5
scope: 0 citations outside the v5 sources). `Test Runs/_research 2026-10-06 GPOR/quote_check.py`: no E-ids; 47 distinct
M/L/R ids, all present in `principle_ledger_v5.csv`; every quotation set directly beside an id (43 pairs, fragments split
at `[...]`) found in that row's text, 0 failures. Nothing committed (dispatch instruction).
