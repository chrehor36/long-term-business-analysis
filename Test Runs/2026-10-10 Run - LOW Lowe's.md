# Company Run: Lowe's Companies, Inc. (NYSE: LOW), 2026-10-10
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Dispatch.** Run by a dispatched analyst under `Screens/_daily/_dispatch_brief.md` (the canonical brief) with the slots filled
by the dispatching session's message of 2026-10-10. Working folder `Test Runs/_research 2026-10-10 LOW/` (raw filings and XBRL
downloads under its ignored `cache/` subfolder; the fetch, transcription and check scripts beside them).

**Contamination, declared as found (the blind rule).** Seen by accident and not used: (1) the session context listed recent
commit subjects of other runs (AME, ITW, JKHY, KEYS, KLAC, with their boxes and alert prices) and untracked research-folder
names of other runs (AYI, BDC, ARCB); (2) the project's memory index, loaded into every session, carries one-line summaries of
the queue state (a count of gate-clearers, "nothing buyable", holding reviews owed) that name no company here; (3) the dispatching
message says there are earlier run files on Lowe's; none was opened, listed or searched, and their dates, boxes and contents are
unknown to this run. Nothing about Lowe's from any other run, holding review or `PORTFOLIO.md` was seen. No directory listing of
`Test Runs/` was made; the only listings were of this run's own research folder.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $186.00 (close 2026-10-09, as printed by `tools/run.py`; an aggregator quote, flagged per operator rule 5, live
  quote only).
- **Shares by class** from the latest filing's cover: one class, common stock, par $0.50: **561,054,019** shares as of
  2026-08-25 (10-Q for the quarter ended 2026-07-31, filed 2026-08-27, accession `0000060667-26-000117`;
  `Screens/cover_shares.py LOW`). Cross-check: the balance sheet of 2026-07-31 shows 561 million issued and outstanding; Lowe's
  holds no treasury stock (repurchased shares are retired, which is why "issued" equals "outstanding" in every balance sheet read),
  so issued less treasury is the same 561 million. No 8-K or prospectus after the 10-Q announces an issuance (8-Ks of 2026-08-19
  and 2026-09-02 listed; neither is an equity issuance by its item list, see Q6).
- **Market cap:** 561.054M x $186.00 = **$104,356M**.
- **Sovereign for the earnings currency (USD):** **5.60%**, the 30-year par yield on the US Treasury daily par yield curve,
  2026-10-09 (the issuing authority; fetched by `tools/sources.py` through `tools/run.py`).
- **Filings read** (operator rule 4): 10-K for fiscal 2025 (year ended 2026-01-30), filed 2026-03-23, accession
  `0000060667-26-000029`; 10-Q for the second quarter of fiscal 2026 (quarter ended 2026-07-31), filed 2026-08-27, accession
  `0000060667-26-000117`; proxy (DEF 14A) filed 2026-04-16, accession `0000060667-26-000056`. For the cycle: 10-Ks for fiscal
  2024 (`0000060667-25-000049`), 2022 (`0000060667-23-000034`), 2021 (`0000060667-22-000038`), 2019 (`0000060667-20-000036`),
  2017 (`0000060667-18-000051`), 2014 (`0000060667-15-000057`), 2011 (`0000060667-12-000096`), and the annual-report exhibits
  (EX-13) of the 10-Ks for fiscal 2009 (`0000060667-10-000059`) and fiscal 2007 (`0000060667-08-000067`).
  **One figure cross-checked against the filed statement:** net cash provided by operating activities, fiscal 2025, **$9,864M**
  in the filed Consolidated Statement of Cash Flows (10-K `0000060667-26-000029`) against $9,864M in the XBRL column of
  `tools/run.py`: equal. Capital expenditures $2,213M and share-based payment expense $247M also agree.
- `tools/run.py LOW` arithmetic lines only (USD millions; the tool's rule text, ids and verdict lines are not read, Part VII;
  saved in `runpy_output.txt`). Owner cash (operating cash less stock pay less capital spending): fiscal 2023 **5,966**;
  fiscal 2024 **7,477**; fiscal 2025 **7,404**. Its five-year line: owner cash on the capex basis averages **7,083** (fiscal
  2021 to 2025), on the D&A basis 7,049. Capex against D&A: 1,964 / 1,923; 1,927 / 1,972; 2,213 / 2,194 (fiscal 2023 to
  2025): capital spending runs at the depreciation charge. Stock pay is in the cash-flow statement as "Share-based payment
  expense" (210, 221, 247) and no other stock-pay line was found; finance-lease principal (92, 86, 85) is a further capital
  payment the tool lists as an alternate, carried at Q7. The full ten-year owner-cash series is built at Q4 from the filed
  statements.

## THE FOUNDATIONS (not a gate)
Three bear on this name. **A share is a business** **[M1997-109]**: the question is what Lowe's 1,759 stores and its new
distribution branches will put out in cash, not what the next buyer pays; the price has fallen from the levels at which the
company bought its own stock in 2023 and 2024 (Q6), and that fall carries no instruction, "It just tells us prices."
**[M2006-077]**. **Margin of safety**: if the case needs pencil and paper "it’s too close to think about" **[M1996-084]**;
held for Q7. **The analyst's habits**: look for "what’s wrong in things" **[M2025-013]**, and treat the reading of competitors'
filings as the place "to possibly reject your original hypothesis" **[M1998-144]**. No macro view enters: housing turnover and
rates appear below only as the filer's own description of its years, never as a forecast. **Contrary evidence, written down
as found** **[M1997-127]**: (1) total customer transactions fell from 1,046 million (fiscal 2020) to 780 million (fiscal 2025)
while ticket rose from $85.67 to $106.13 (10-Ks `0000060667-22-000038`, `0000060667-26-000029`); part of the fall is the
Canadian exit, but comparable transactions fell 2.8% in fiscal 2025 alone; (2) the company has shareholders' deficit of
$9,917M at 2026-01-30 and debt of $39,921M, made by buying back stock, much of it with borrowed money; (3) the 2025 purchases
(FBM $8.8B, ADG $1.3B) earned an operating profit of $3M on $1,941M of sales in the second quarter of fiscal 2026 after
amortization (10-Q `0000060667-26-000117`, segment note); (4) Lowe's has made and unwound three foreign ventures in a decade
(Australia, Mexico, Canada), the last at a loss (Q5, Q6).

## THE STANDING RULE
A part-interest in the market, bought with the buyer's own money, unlevered and sized below anything the buyer needs, puts the
buyer at no risk of ruin: "We are never going to risk what we have and need for what we don’t have and don’t need."
**[M2012-081]**; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt is not the
buyer's conduct and is weighed at Q9. Nothing here bars the run.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" and "how the industry will develop and where the company will stand within the industry" **[M2012-065]**;
the first step is "trying to identify the key variables in that particular business, and evaluating how predictable they
were" **[M1998-044]**; and the past statements must "tell me the information that’s useful to me in making a judgment about
what the future financial statements are going to look like" **[M2008-033]**.

**What the business is, from the 10-K (`0000060667-26-000029`, Item 1 and Note 18).** The world's second-largest home
improvement retailer: 1,759 stores and outlets in the United States, about 196 million square feet, fiscal 2025 net sales
$86,286M; products $82,352M, services (installation through subcontractors) $2,542M, other $1,392M. One reportable segment,
Retail Home Improvement; an "Other" group of three operating segments holds the 2025 purchases, FBM (distribution of ceilings,
wall systems, commercial doors and hardware to contractors, about 540 branches with ADG in the US and Canada) and ADG
(design, distribution and installation of interior finishes for home builders). In the second quarter of fiscal 2026 the
retail segment made $3,546M of operating income on $24,015M of sales (14.77%) and "Other" made $3M on $1,941M (10-Q
`0000060667-26-000117`, Note 13). The retail segment carries all of the operating profit; Q2 decides on it (business of
parts) and Q1 reads it first.

**The key variables** **[M1998-044]**, as the filer itself reports them each year: comparable sales, split into customer
transactions and average ticket; the operating margin against Home Depot's; and shares outstanding (the Coca-Cola pair of
"unit case sales and shares outstanding" **[M1998-040]** has its analogue here in transactions and shares). Over the whole span
the filings show (Other Metrics tables of the 10-Ks and EX-13s named in Step 0):

| fiscal | comp sales | transactions (M) | avg ticket | EBIT margin | stores |
|---|---|---|---|---|---|
| 2007 | -5.1% | 720 | $67.05 | 9.74% | 1,534 |
| 2008 | -7.2% | 740 | $65.15 | 7.85% | 1,649 |
| 2009 | -6.7% | 766 | $61.66 | 6.59% | 1,710 |
| 2010 | +1.3% | 786 | $62.07 | 7.29% | 1,749 |
| 2011 | 0.0% | 810 | $62.00 | 6.53% | 1,745 |
| 2012 | +1.4% | 804 | $62.82 | 7.05% | 1,754 |
| 2013 | +4.8% | 828 | $64.52 | 7.77% | 1,832 |
| 2014 | +4.3% | 857 | $65.61 | 8.53% | 1,840 |
| 2015 | +4.8% | 878 | $67.26 | 8.41% | 1,857 |
| 2016 | +4.2% | 945 | $68.83 | 8.99% | 2,129 |
| 2017 | +4.0% | 953 | $72.00 | 9.60% | 2,152 |
| 2018 | +2.4% | 941 | $75.79 | 5.64% | 2,015 |
| 2019 | +2.6% | 921 | $78.36 | 8.75% | 1,977 |
| 2020 | +26.1% | 1,046 | $85.67 | 10.77% | 1,974 |
| 2021 | +6.9% | 1,002 | $96.09 | 12.56% | 1,971 |
| 2022 | -0.9% | 937 | $103.64 | 10.47% | 1,738 |
| 2023 | -4.7% | 835 (827 restated) | $103.51 ($102.47) | 13.38% | 1,746 |
| 2024 | -2.7% | 809 (801) | $103.37 ($102.93) | 12.51% | 1,748 |
| 2025 | +0.2% | 780 | $106.13 | 11.77% | 1,759 |

*(EBIT margin as the filer printed it through fiscal 2017 (it called it "EBIT margin" to 2014 and "operating income" after);
fiscal 2018 to 2025 computed as operating income over net sales from the filed statements and XBRL, `facts_LOW_flow.txt`.
Store counts for 2007 and 2008 from the EX-13 tables; fiscal 2016 to 2021 include the Canadian stores bought with RONA in 2016
and sold in February 2023; fiscal 2018 and 2022 margins carry the impairments of the Orchard, Mexico and Canadian exits. The
fiscal 2023 and 2024 transaction and ticket figures were restated in the fiscal 2025 10-K; both are shown.)*

**Are they foreseeable?** In kind, yes. Through the worst housing collapse in the record (fiscal 2007 to 2009, comparable
sales down 5.1%, 7.2%, 6.7%) the business shrank its margin but never lost money; through the opposite shock (fiscal 2020, up
26.1%) it gained and then gave back. The variables moved the way a seller of goods for the existing house moves: ticket with
inflation and project size, transactions with housing activity and weather. The demand is for repair, maintenance and
improvement of a large standing stock of houses, which is not a technology forecast: the forecast is "about customers", in the
sense of **[M2017-019]** and **[M2023-030]** ("what we think we can project out in terms of consumer behavior and threats to a
business"). The industry structure has been the same two national chains (Lowe's and Home Depot, with Menards private and
regional) for the whole span read; no new national chain entered after fiscal 2007 in any filing read. The financial
statements do tell what the next ones will look like in the sense of **[M2008-033]**: sales, gross margin (33% to 35% in every
year read) and capital spending (near depreciation) move within known bands.

**Where my fix is weaker.** The rows warn by name about this field: "it’s easy to sort of think you understand retail, and then
subsequently find out you don’t" **[M2014-052]**; "In retailing, to coast is to fail." **[L1995-008]**. Those warnings bear on
the castle (Q2, test 2: whether the business needs the lord) and are carried there; they do not say the economics of a home
centre cannot be foreseen. The 2025 purchases put the company into contractor distribution (FBM) and builder installation
(ADG), businesses I can read (distribution margins, receivables, branches) but whose ten-year economics inside Lowe's are new;
they carry no profit yet and do not decide (Q2, parts). Online selling is inside the comps (about 105 basis points of fiscal
2025 comps, 10-K note 1 to Other Metrics) rather than outside them, so the online channel has not yet been a separate
attacker in the filer's own numbers; Q2 asks whether it will be.

**How far off could I be** **[M2011-084]**: on the level of demand in any one year, far (the table shows a 26% year and three
falling years in a row); on the shape of the business ten years out (a large home-centre chain selling to homeowners and small
contractors at a gross margin in the low thirties), not far. The doubt test **[M2002-092]** is applied honestly: I have no doubt
that I understand what the business does, how it makes money and what moves its figures; my doubts are about its standing
against Home Depot and about price, which are Q2 and Q7. The same row names a retailer as the example of what "You can certainly
understand" **[M2002-092]**.

**Routing.** Not a business of fast technological change **[L1993-023]**, **[M1998-008]**; not a financial institution; the
parts that matter (the retail segment) are understood. The insiders would write this forecast down; it is the forecast both
chains print in every annual report's merchandise and store tables (test 5, **[M2000-105]**, read the other way).

**VERDICT: IN.** The ten-year economics of a US home-centre chain are foreseeable in kind from twenty years of its own filings:
"a pretty good idea where it’s going to be in ten years" **[M1997-021]**, at the low precision the rows ask, "we had to have a
feel for it, and we had to know our limitations" **[M2015-086]**. Filing fact: one reportable segment carrying all operating
profit, fiscal 2025 sales $86,286M, comps and margins as tabled above. The retail warnings **[M2014-052]**, **[L1995-008]** are
carried to Q2.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now. What are the key factors? And how permanent are they? How much do they depend on the genius of the
lord in the castle?" **[M1995-038]**.

**The parts table** (business of parts, CONVENTION of the framework, section B; 10-K `0000060667-26-000029` Note 18 and 10-Q
`0000060667-26-000117` Note 13):

| part | operating income, fiscal 2021 to 2025 | share | castle | decides |
|---|---|---|---|---|
| Retail Home Improvement (the stores and online) | $54,498M (all consolidated operating income of fiscal 2021 to 2024, plus $10,223M in fiscal 2025) | above 100% | read below | **yes** |
| Other (FBM from 2025-10-09, ADG from 2025-06-02) | -$70M in fiscal 2025; -$28M in the first half of fiscal 2026 ($3,695M of sales) | below 0% | not judged: nine months of record inside Lowe's, contractor distribution and builder installation | no |

The file closes on the retail part. The Other part carries a loss after the amortization of the purchased intangibles; it is
not shown open on the evidence and not shown standing either, and it goes to Q7 on its own filed record (the price paid
deducted, the earnings it has filed credited), as the six specifics direct for a deal inside the window.

**The tests, each with its filing fact.**

1. *What keeps it standing, and how permanent* **[M1995-038]**. The 10-K names the factors itself: "Location of stores and
   branches, product assortment, product pricing, fulfillment capabilities, and customer service continue to be key
   competitive factors in our industry" (Item 1, Our Competition). A network of 1,759 large stores on owned or long-leased
   sites within reach of most American homes, stocked deep in bulky project goods (lumber, appliances, plumbing) that are
   costly to ship one at a time, is a reason the customer comes that has not changed across the span read. It is a shared
   reason: Home Depot offers it too, at greater scale (below).
2. *Would it stand without the lord?* **[L2007-006]**, **[M1996-037]**. Partly. The field stood: under the management of
   fiscal 2007 to 2017 Lowe's never lost money, and its pre-tax return on net operating tangible assets (inventory plus
   net property less accounts payable; operating leases left out for both chains; `roc.txt`) ran 11.8% at the bottom of the
   housing collapse (fiscal 2009) and 20% to 27% in fiscal 2014 to 2017. But the level of its returns has moved with its
   management: in the same years Home Depot pulled from a margin below Lowe's (fiscal 2008: 6.11% against 7.85%) to one five
   points above it (fiscal 2016: 14.19% against 8.99%), and Lowe's spent money on Australia, Mexico, Orchard and Canada that it
   later wrote off (Q5, Q6). The rows' warning is aimed at exactly this: "In retailing, to coast is to fail." **[L1995-008]**,
   and for a retailer the backward nephew "would be an express ticket to bankruptcy" **[L1995-009]**. Recorded against: this
   is a have-to-be-smart-every-day business.
3. *The money test* **[M2011-015]**, **[M1997-103]**; "why are there no new entrants into the field?" **[M2000-077]**. No new
   national home-centre chain entered in the span read. The best-funded attacker on record, Amazon (consolidated revenue
   $716,924M and operating income $79,975M in 2025, 10-K `0001018724-26-000004`), sells home goods without a home-centre
   network and reports no home-improvement figure, so its share of this field cannot be read from its filings (flagged).
   The specialist that did enter at scale, Floor & Decor (one category, flooring), grew from $784M of sales (2015) to $4,684M
   (2025, 10-K `0001628280-26-009770`) while its operating margin fell from 9.87% (2021) to 5.76% (2025). Rebuilding 196 million
   square feet of sites near rooftops, with distribution and vendor terms behind them, is not done with money alone; but the
   test is passed by the field, not by Lowe's against Home Depot, which already has the network.
4. *Pricing power and the agony* **[M2005-020]**; cost pass-through **[M2005-017]**. Gross margin stayed in a band of 31.8%
   to 35.1% in all nineteen years read for Lowe's and 33.3% to 34.8% for Home Depot (XBRL, `gm.txt`), through the housing
   collapse and through the inflation of fiscal 2021 and 2022, when Lowe's average ticket rose 11.1% and 6.7% (comparable) and
   gross margin held at 33.3% and 33.2%. That is the price behaviour of a field that passes its costs through. It is not
   power over price: the two chains' gross margins are within 0.2 points of each other in fiscal 2025 (33.48% against 33.32%),
   which is what "whatever he charged for gas was my price" **[M2012-109]** looks like in a filing. Recorded against: Lowe's
   prices are set beside Home Depot's.
5. *Unit volume* **[M1999-054]**. Against. Lowe's comparable customer transactions fell 4.2% (fiscal 2021), 7.6% (2022), 3.0%
   (2024) and 2.8% (2025); Home Depot's fell 0.1% (2021), 2.9% (2023), 1.0% (2024) and 1.0% (2025) (HD 10-Ks
   `0000354950-22-000070`, `0001628280-26-019436`). Total transactions: Lowe's 921 million (fiscal 2019) to 780 million (2025),
   part of the fall being the Canadian stores sold in February 2023; Home Depot 1,616.0 million to 1,601.5 million. Lowe's
   is losing customer visits faster than its rival.
6. *The low-cost position* **[L2004-007]**, **[M2018-043]**, **[M1997-010]**. Home Depot holds it. Sales per square foot:
   Home Depot $279 against Lowe's $245 (fiscal 2009: Lowe's $47,220M over 193 million square feet); $417 against $319
   (fiscal 2017); $605 against $463 (fiscal 2021: $96,250M over 208 million) (HD 10-Ks `0001193125-10-067178`,
   `0000354950-18-000019`, `0000354950-22-000070`). Home Depot's operating margin has been above Lowe's in every year from
   fiscal 2009 to 2025. What the rows ask is cost against the competitor, not absolute **[M2001-013]**, and there Lowe's has
   moved from far behind to near parity: the gap in operating margin was 5.20 points (fiscal 2016), 8.71 (2018, Lowe's
   impairments), 5.62 (2019), then 0.83 (2023), 0.98 (2024) and 0.92 (2025) (operating income over sales, both filers).
   Recorded: Lowe's is the higher-cost of the two, by a margin that has nearly closed.
7. *The brand* **[M2001-090]**. The customer asks by name for the manufacturers' brands (both chains sell many of the same
   ones) and chooses the store by location and service; Lowe's name is a destination but not a product the customer cannot
   get next door. Neither for nor against beyond test 1.
8. *The low bid* **[M2017-009]**. A homeowner in the middle of a project and a contractor at a job site buy on what is in
   stock nearby today and on delivery; the 10-K's own list of competitive factors puts location and fulfilment beside price.
   Neither chain wins on price alone; neither is bought on the low bid alone.
9. *Ask the competitors* **[M1999-130]**. Home Depot's 10-K names as its "distinct competitive advantages" its brand,
   service, scale, real estate, supply chain "and our deep relationships with Pros" (`0001628280-26-019436`, Item 1), and it
   spent $17,644M (fiscal 2024, SRS) and $5,410M (fiscal 2025, GMS) on distributors to large contractors (XBRL, payments to
   acquire businesses). Lowe's followed with FBM and ADG ($10,088M, fiscal 2025). On the public record the leader is setting
   the direction and the follower is matching it at about half the size.
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Mixed, and recorded both ways. Narrowing on traffic (test 5).
    Widening on cost against the rival (test 6): operating margin from 8.75% (fiscal 2019) to 13.38% (2023) and 11.77% (2025),
    the retail segment alone 12.16% in fiscal 2025 and 14.77% in the second quarter of fiscal 2026 (10-Q
    `0000060667-26-000117`).
11. *What could destroy, modify or reduce it* **[M2000-014]**. Online sellers of home goods ("a business that has millions
    and millions of happy customers can introduce them to new items" **[M2012-046]**): online sales lifted Lowe's comps by
    about 105 basis points in fiscal 2025 and are inside its own figures; Home Depot pulling away with large contractors
    through SRS and GMS; Menards, a private chain that files nothing with the SEC (flagged: no figures obtainable). None is
    shown, on the filings, to be filling the moat of the field; the first two are slow threats that "can lull you to sleep
    easier" **[M2014-038]**.

**The competitor row** (operating income over net sales, %, first-filed 10-K values; HD fiscal years end near 1 February;
TSCO, FND and AMZN calendar years; WMT fiscal years end 31 January of the next year):

| fiscal | LOW | HD | TSCO | FND | WMT | AMZN (consolidated) |
|---|---|---|---|---|---|---|
| 2008 | 7.85 | 6.11 | 5.92 | - | 5.64 | 4.39 |
| 2009 | 6.59 | 7.26 | 5.99 | - | 5.87 | 4.61 |
| 2012 | 7.05 | 10.39 | 9.37 | - | 5.93 | 1.11 |
| 2015 | 8.41 | 13.30 | 10.45 | 6.63 | 5.00 | 2.09 |
| 2017 | 9.60 | 14.55 | 9.45 | 8.52 | 4.08 | 2.31 |
| 2019 | 8.75 | 14.37 | 8.90 | 7.78 | 3.93 | 5.18 |
| 2021 | 12.56 | 15.24 | 10.27 | 9.87 | 4.53 | 5.30 |
| 2023 | 13.38 | 14.21 | 10.16 | 7.27 | 4.17 | 6.41 |
| 2025 | 11.77 | 12.68 | 9.45 | 5.76 | 4.18 | 11.16 |

Pre-tax return on net operating tangible assets (inventory plus net property less accounts payable; `roc.txt`): Lowe's
14.1% (fiscal 2008), 11.8% (2009), 13.7% (2010), 20.1% to 26.9% (2014 to 2017), 17.7% (2018), 26.1% (2019), 39.4% to 47.8%
(2020 to 2025); Home Depot 22.3% (fiscal 2011, the first year its XBRL carries all three lines) rising to 68.2% (2021) and
49.3% (2025); Tractor Supply 24.4% (2009) to 49.2% (2021) and 31.1% (2025); Floor & Decor 30.2% (2017) falling to 11.7%
(2025). Accessions: HD `0001628280-26-019436` (latest) and `0001193125-10-067178` (earliest used); TSCO `0000916365-26-000014`;
FND `0001628280-26-009770`; WMT `0000104169-26-000055`; AMZN `0001018724-26-000004`; with earlier years from each filer's
companyfacts series (first-filed 10-K values, files `facts_*.txt`). Menards: private, not an SEC filer, flagged and absent.
Amazon reports no home-improvement line; its column is the whole company and is shown only as the attacker's means.

**The field's returns over the last full cycle** (section C), judged in words: the two home-centre chains, from the worst
housing collapse in their record through the surge and the down years after it, earned pre-tax returns on the tangible
capital their stores need that were good in the trough (Lowe's 11.8%; Home Depot 15.6% on the same measure in fiscal 2009:
operating income $4,803M over inventories $10,188M plus net property $25,550M less accounts payable $4,863M, from its filed
balance sheet, 10-K `0001193125-10-067178`) and excellent in every other year. This is not a castle that protects ordinary
returns **[L2007-004]**, **[M2013-052]**.

**A change for the better, credited or not** (section C; **[M2005-020]**, **[L1995-022]**, **[M2017-026]**). Lowe's own
returns stepped up after fiscal 2019. The verdict below does not rest on the step: on its returns before it (pre-tax 20% to
27% on operating tangible assets in fiscal 2014 to 2017, 11.8% in the trough) the castle already protected returns above
ordinary. Whether the step is credited matters to Q7, whose five-year base sits on it. The cycle read: fiscal 2019 (comps
+2.6%, the last ordinary year), the surge (2020 +26.1%, 2021 +6.9%), the down years (2022 -0.9%, 2023 -4.7%, 2024 -2.7%) and
the turn (2025 +0.2%, first half of 2026 +0.4%). Through it the price behaviour held: gross margin 31.80% (2019), 33.01% to
33.48% every year after; operating margin did not fall back below 10.47% (fiscal 2022, which carries the Canadian impairment)
and was 11.77% in 2025 against 8.75% in 2019. I credit the change on that cycle, and record the limit: its down years were
far milder than fiscal 2007 to 2009 (cumulative comps about -8% against about -18%), so the improved level has not met a
collapse.

**Why the castle is still standing, in one paragraph.** Two chains have held the American home-centre field for the whole span
read, with no national entrant, gross margins that pass costs through and never break, and returns on the capital the
stores need that stay good at the bottom and excellent elsewhere. Lowe's is the second and the higher-cost of the two; it
has narrowed the cost gap to about a point and is losing customer visits faster than Home Depot. "one competitor is
frequently enough to ruin a business" **[M2012-108]** is the risk the rows name; in forty years of filings it has not ruined
this one, which has stood beside a stronger rival on price parity and still earned its returns. The moat is the field's;
Lowe's share of it depends more on its management than the rows like **[M1996-037]**.

**VERDICT: IN**, on the deciding part. The castle is not shown open on the evidence **[M2011-015]**, its future can be
judged from the field's record **[M2000-014]**, and the field's returns over the full cycle are well above ordinary
**[L2007-004]**. Carried as evidence against, to Q5 (ability) and Q7 (how sure): the higher-cost position **[M2001-013]**,
**[M1997-010]**, the faster loss of traffic **[M1999-054]**, and the dependence on staying smart every day **[L1995-008]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
**What it earns on the capital it needs** **[M1995-051]**; "the capital actually needed in the business" **[M2010-090]**,
read as tangible assets **[M2011-060]**, and not as return on equity, which buybacks can make "whatever you want"
**[M1998-017]**. Lowe's reported return on equity is meaningless here (equity has been negative since fiscal 2021) and its
own "return on invested capital" (26.1% in fiscal 2025, 10-K Other Metrics) is computed on debt plus a shrinking equity, so
neither is used. The measure used is pre-tax operating income over net operating tangible assets (inventory plus net
property less accounts payable; `roc.txt`, from the filed balance sheets):

| fiscal | 2008 | 2009 | 2010 | 2014 | 2016 | 2017 | 2018 | 2019 | 2021 | 2023 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| net operating tangible assets ($M) | 26,822 | 26,461 | 26,059 | 23,821 | 23,756 | 24,524 | 22,714 | 24,189 | 25,322 | 25,843 | 25,900 |
| operating income ($M) | 3,786 | 3,112 | 3,560 | 4,792 | 5,846 | 6,586 | 4,018 | 6,314 | 12,093 | 11,557 | 10,153 |
| pre-tax return | 14.1% | 11.8% | 13.7% | 20.1% | 24.6% | 26.9% | 17.7% | 26.1% | 47.8% | 44.7% | 39.2% |

Operating leases are left out (right-of-use assets $4,303M at 2026-01-30, rising from $3,738M); with them the fiscal 2025
figure is about 34%. The goodwill and intangibles bought in 2025 are left out here, as the rows direct for judging the
business, and counted below for judging the allocation **[M2011-060]**.

**What must go back in to stand still** **[L2000-035]**, **[L1999-024]**. Capital spending has run at the depreciation charge:
$1,964M against $1,923M (fiscal 2023), $1,927M against $1,972M (2024), $2,213M against $2,194M (2025); guidance for fiscal 2026
is about $2.5 billion (10-K MD&A). The store count barely moved (1,749 at the end of fiscal 2010, 1,759 at the end of 2025
after selling the Canadian stores), so nearly all the spending is upkeep, technology and fit-out of the existing estate. I
take maintenance as the whole of capital spending, a stated guess **[M2000-144]**: the filing does not split it and the store
count does not grow. Working capital is carried by the suppliers to a large degree: accounts payable funded 56% of inventory at
2026-01-30 ($9,762M against $17,300M) and 64% at 2017-02-03 ($6,651M against $10,458M).

**The growth arithmetic** **[M1998-081]**, **[M2001-019]**. From fiscal 2009 to fiscal 2025 net sales rose from $47,220M to
$86,286M and operating income from $3,112M to $10,153M, while net operating tangible assets stayed between $22.7 billion and
$26.8 billion in every year computed (fiscal 2011 to 2013 lack a tagged line and are not computed). The added earnings came with almost no added operating capital: that is the first of the
three businesses of **[M1998-081]**, "more and more money every year without putting up anything to get it, or very little",
for the stores. The caps: the store base is not growing, so growth comes from ticket (inflation and project size) and share;
comparable sales over the sixteen years from fiscal 2010 to 2025 compound to about 3.2% a year (from the comps table at Q1). "an abundance of funds tends
to dampen returns" **[L1996-002]**, and here the abundance has gone out in buybacks (Q6) and, in 2025, into acquisitions.

**The added capital of 2025** **[M2001-019]**, **[L2009-012]**. $10,088M paid for ADG and FBM (10-K cash-flow statement).
Their segment earned an operating loss of $70M in fiscal 2025 (part year) and $28M in the first half of fiscal 2026 on
$3,695M of sales, after amortization of the purchased intangibles; the release for the second quarter of 2026 puts that
amortization at $96M for the quarter (8-K `0000060667-26-000113`, EX-99.1). Before amortization the part earned about $99M
in that quarter, about $400M a year at that rate, or about 4% pre-tax on the price paid. The seller's own figure was $635M of
"adjusted EBITDA" for 2024 (8-K `0000060667-25-000162`, EX-99.1), before depreciation, interest and tax. Whatever the part
grows into, on its record so far the added sums earn well below the stores' return and below the long bond.

**WEIGHS FOR** for the stores, which have earned high returns on a capital base that has not grown in sixteen years
**[M1995-047]**, **[M1998-081]**; the 2025 capital, earning about 4% pre-tax before any growth, is recorded against and carried
to Q6 as an allocation question.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]**: "there are certain things it’s harder
to hide or play games with on the balance sheet than with the income statement". USD millions, fiscal year-ends, from the
ten 10-Ks named in `runpy_output.txt` (accessions `0000060667-17-000076` to `0000060667-26-000029`), checked against the
filed balance sheets of fiscal 2024 and 2025 in `0000060667-26-000029`:

| year-end | total assets | equity | cash | inventory | inventory / sales | goodwill | intangibles | debt (current + long-term) | retained (deficit) |
|---|---|---|---|---|---|---|---|---|---|
| 2017-02-03 | 34,408 | 6,434 | 558 | 10,458 | 16.1% | 1,082 | n/t | 15,699 | 6,241 |
| 2018-02-02 | 35,291 | 5,873 | 588 | 11,393 | 16.6% | 1,307 | n/t | 16,995 | 5,425 |
| 2019-02-01 | 34,508 | 3,644 | 511 | 12,561 | 17.6% | 303 | n/t | 16,223 | 3,452 |
| 2020-01-31 | 39,471 | 1,972 | 716 | 13,179 | 18.3% | 303 | n/t | 19,306 | 1,727 |
| 2021-01-29 | 46,735 | 1,437 | 4,690 | 16,193 | 18.1% | 311 | n/t | 21,780 | 1,117 |
| 2022-01-28 | 44,640 | -4,816 | 1,133 | 17,605 | 18.3% | 311 | 388 | 24,727 | -5,115 |
| 2023-02-03 | 43,708 | -14,254 | 1,348 | 18,532 | 19.1% | 311 | 169 | 33,960 | -14,862 |
| 2024-02-02 | 41,795 | -15,050 | 921 | 16,894 | 19.6% | 311 | n/t | 35,921 | -15,637 |
| 2025-01-31 | 43,102 | -14,231 | 1,761 | 17,409 | 20.8% | 311 | 277 | 35,487 | -14,799 |
| 2026-01-30 | 54,144 | -9,917 | 982 | 17,300 | 20.0% | 3,945 | 5,908 | 39,921 | -10,839 |

*(n/t: not tagged as a separate line that year, carried inside other assets; the fiscal 2025 10-K reclassified the prior
year's goodwill and intangibles out of other assets. Debt is the sum of current maturities and long-term debt, finance leases
inside it; operating lease liabilities, $4,756M at 2026-01-30, are not in it. Short-term investments of $370M at 2026-01-30
sit beside the cash.)*

What moved, and why. **Equity** went from $6,434M to a deficit of $15,050M in seven years (fiscal 2017 to 2023) while the
business earned $38.5 billion of net income: in those years the company bought back $48.8 billion of its stock and paid
$13.0 billion of dividends (cash-flow statements, `facts_LOW_flow.txt`), more than it earned, and borrowed the difference; debt rose from
$15.7 billion to $35.9 billion. In fiscal 2025 buybacks stopped ($211M paid, the programme "paused", 10-K MD&A), the deficit
shrank by $4.3 billion, and debt rose again by $4.4 billion for the acquisitions. **Goodwill** tells the deal history: $1,082M
after RONA (fiscal 2016), written down to $303M by fiscal 2018, $311M for six years, then $3,945M after FBM and ADG, with
$5,908M of purchased intangibles beside it. **Receivables** were $94M at 2025-01-31 (the store business sells for cash and
cards) and $1,090M a year later: FBM's trade credit to contractors, a new kind of asset for Lowe's. **Inventory** grew faster
than sales, from 16.1% of sales to 20.0%, while comparable transactions fell; the filer says it is investing in "inventory of
high-volume Pro products" and job-lot depth (10-K Item 1). Home Depot carried 15.7% at 2026-02-01 ($25,817M on $164,683M).
Recorded against: more inventory per dollar of sales, not suspicious on the filer's stated reason, but capital that turns
more slowly. Accounts payable fell from 64% of inventory to 56%. **Cash** has been kept low ($0.5 to $1.8 billion) except
in the pandemic year; the company runs on its revolving lines and commercial paper programme. What the figures cannot say:
whether the buybacks bought value (Q6, against Q7), and what FBM will earn (nine months of record).

**The income account, recast.** Owner cash after every real cost (operating cash less stock pay less capital spending;
USD millions; from the filed cash-flow statements):

| fiscal | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| operating cash | 5,617 | 5,065 | 6,193 | 4,296 | 11,049 | 10,113 | 8,589 | 8,140 | 9,625 | 9,864 |
| stock pay | 90 | 99 | 74 | 98 | 155 | 230 | 223 | 210 | 221 | 247 |
| capital spending | 1,167 | 1,123 | 1,174 | 1,484 | 1,791 | 1,853 | 1,829 | 1,964 | 1,927 | 2,213 |
| owner cash | 4,360 | 3,843 | 4,945 | 2,714 | 9,103 | 8,030 | 6,537 | 5,966 | 7,477 | 7,404 |
| net earnings | 3,091 | 3,447 | 2,314 | 4,281 | 5,835 | 8,442 | 6,437 | 7,726 | 6,957 | 6,654 |

Owner cash and net earnings part company in the working-capital years: fiscal 2019 (inventory and payables moving against
the cash) and fiscal 2020 (payables up $3.2 billion in the surge), which offset each other (their average, $5,909M, sits near
the earnings). Finance-lease principal ($85M to $92M a year) is a further capital payment, an alternate carried at Q7.

**The real costs.** *Depreciation* ($2,194M in fiscal 2025) is matched by capital spending every year read and is a true cost
**[R1996-023]**; no shortfall to subtract. *Stock pay* ($247M, 0.29% of sales) is expensed and is deducted above **[L2015-003]**;
the share count fell from 1,468 million (diluted, fiscal 2008) to 560 million (2025), so the dilution has been bought back
many times over (at what price is Q6). *The recurring "one-time"*: an item excluded from "adjusted" results in nearly every year
read: Australian joint-venture impairments (fiscal 2015 and 2016), the exit of Orchard Supply, Mexico and Canadian stores
(2018, 2019), $2.5 billion of pre-tax costs on selling the Canadian business (2022: impairment, loss on sale, closing costs;
10-K `0000060667-23-000034`), gains of $79M and $177M on that sale's deferred consideration (2023, 2024), $321M of acquisition
costs and amortization (2025). These are the costs of capital decisions and they are real: "we do not ask you to forget about
those costs" **[M1999-023]**; telling owners year after year to ignore them "is misleading" **[L2016-007]**. Owner cash above
carries all of them except the non-cash impairments, which are the write-off of money already spent in earlier years' capital
and acquisition lines. *Amortization of the purchased intangibles* (customer relationships over twenty years, trademarks over
fifteen) is not a cash cost and is not deducted in owner cash; whether it is real is the question **[L2012-003]** puts, and
the row itself names the case: "Charges against other intangibles such as the amortization of customer
relationships, however, arise through purchase-accounting rules and are clearly not real expenses." **[L2012-003]**. It is not
deducted; the trademarks are treated the same way.

**EBITDA in the filer's own mouth** **[M2002-026]**, **[M1998-086]**: the largest purchase in the company's history was
announced and priced on it: "Lowe’s will acquire FBM for $8.8 billion in cash, which reflects an adjusted EBITDA multiple of
13.4x" (8-K `0000060667-25-000162`, EX-99.1, 2025-08-20), and justified as "expected to be accretive to adjusted diluted
earnings per share in the first full year". Recorded against, carried to Q5 and Q6.

**The featured adjusted figure** **[L2016-006]**: every earnings release read heads with it ("Diluted EPS of $4.27; Adjusted
Diluted EPS of $4.40", 8-K `0000060667-26-000113`), and the overview of every 10-K from fiscal 2019 to 2025 reports "adjusted
diluted earnings per common share" beside the GAAP figure. **Guidance** **[L2019-006]**: the company publishes a yearly outlook
for sales, comparable sales, operating margin, adjusted operating margin, interest, tax rate and EPS (8-K
`0000060667-26-000113`: fiscal 2026 sales "$92.0 billion (previously $92.0 to 94.0 billion)", comparable sales "flat
(previously flat to up 2%)"), and its 10-Ks record the outlook given back to fiscal 2011 (10-K `0000060667-12-000096`: "we
expected total sales in 2012 to increase 1% to 2%"). The release of August 2026 lowered the outlook: the habit of guidance
is shown; a habit of always making it is not (no instance found in the releases read of a target met to the penny; the sweep
was the four releases of fiscal 2025 and 2026 fetched). These weigh against here and are carried to Q5.

**Confusion or suspicion?** None found. The accounts are plain retail accounts with one segment until 2025; the Canadian
loss, the impairments and the acquisitions are each explained in the notes with their amounts. The tells that live in the
accounts **[M1995-064]** were looked for: other current assets $1,213M at 2026-01-30 (1.4% of sales, up from $722M, of which $123M came
with the acquired businesses and the rest is not broken out in the notes read); inventory higher against sales but
explained and visible; no reserve that moves with a stock sale; no profit booked on both sides of a contract.

**VERDICT on the accounts: IN** (no confusion, no suspicion **[M1995-063]**, **[M1995-065]**); **WEIGHS AGAINST** on the
habits: the adjusted figure featured, yearly guidance, and the largest deal priced on adjusted EBITDA **[L2016-006]**,
**[L2019-006]**, **[M2002-026]**, carried to Q5 **[M2004-067]**. The recast earnings for Q7: owner cash as tabled, with interest
added back after tax for the all-equity basis (interest, net: $885M, $1,123M, $1,382M, $1,313M, $1,406M in fiscal 2021 to 2025;
effective tax rates 24.7%, 28.8%, 24.1%, 24.0%, 23.9%).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**Who.** Marvin R. Ellison, 61, President and Chief Executive Officer since July 2018 and also Chairman since May 2021 (10-K
`0000060667-26-000029`, executive officers); before Lowe's, chairman and chief executive of J. C. Penney. A marketable stake is
read, not met: "most of those were companies I never met the management, never talked to them. We read a lot."
**[M2007-081]**.

**The first yardstick, the record against the hand dealt** **[M1994-008]**. The hand in 2018: a chain whose operating margin
trailed Home Depot's by about five points for four years (Q2, test 6), with loss-making ventures in Australia (exited before
him), Mexico, Orchard Supply and Canada. What he did: closed Orchard and Mexico (fiscal 2018 and 2019), sold the Canadian
business in February 2023 and took the $2.5 billion pre-tax cost in fiscal 2022, which is acting on bad news rather than
nursing it **[M2017-007]**, **[M2017-005]**; took the operating margin from 8.75% (fiscal 2019) to 13.38% (2023) and 11.77%
(2025) and the gap to Home Depot from 5.6 points to under one (Q2); disclosed the figures that matter every year
(comparable transactions, ticket, store counts, segment margins), which is telling owners "about the things that we would want
to know about if we owned a hundred percent of the company" **[M1998-036]**. Against: comparable transactions fell four years
in five and faster than Home Depot's (Q2, test 5); the largest capital decision of his tenure, FBM, has so far earned about 4%
pre-tax on its price (Q3); the buybacks of fiscal 2021 to 2024 were made at $198 to $245 a share (Q6). "Buying a retailer
without good management is like buying the Eiffel Tower without an elevator." **[L1995-006]**; the record says this one has
an elevator for operations.

**The second yardstick, how they treat the owners** **[M1994-008]**, from the proxy (DEF 14A `0000060667-26-000056`):
- Pay. Mr. Ellison's reported total compensation: $18,162,272 (fiscal 2023), $20,164,912 (2024), $21,581,889 (2025), of
  which salary $1,544,231 in 2025 and the rest stock, options and cash incentive. The annual cash incentive pays on company
  sales (40%), operating income (40%), inventory turnover (10%) and Pro sales growth (10%), with the targets "aligned with our
  financial guidance provided to investors at the beginning of the 2025 fiscal year"; the performance shares pay on a
  three-year average of the company's ROIC with a relative total-return modifier. Two things weigh for: the committee
  excluded the acquired businesses' results from the 2025 sales and operating-income achievement (no pay for bought sales),
  and the 2023 to 2025 performance shares "did not pay out" because ROIC missed its threshold. Things weigh against: in the
  same year the committee raised the cash-incentive threshold payout from 25% to 50% of target, kept an 85% payout for
  "performance that does not achieve target", raised the performance-share maximum from 150% to 200%, and adjusted out $105
  million of acquisition costs, "modestly increasing the achievement result for operating income performance": "ratchet,
  ratchet, and bingo" **[M2012-095]**, and the proxy gives "market practice" as the reason twice, which is the committees' reliance on "comparative data"
  **[L2005-015]**. The ROIC
  used for pay divides by "debt and shareholders’ (deficit)/equity", a base that buybacks can shrink: "if you keep the equity low enough by buying shares back, why, you could make return on equity
  whatever you want" **[M1998-017]**.
- The board. The chief executive is also Chairman, with a lead independent director **[L2014-026]**. Directors' holdings are
  small: of the eleven non-employee directors listed, most hold under 20,000 shares, and the footnotes show much of it is
  deferred stock units granted by the company, not the "purchasing shares with their savings" of **[L2019-008]** (also **[L2002-033]**).
  Mr. Ellison's 806,743 beneficially owned shares include 575,700 under exercisable options, leaving about 231,000 held,
  roughly $43M at $186.
- The record with regulators: an EPA consent decree on lead-safe renovation practices by its installers (2014); deviations
  identified by the EPA in fiscal 2023; on 2025-11-25 the company, without admitting liability, agreed a civil penalty of
  $12,500,000 and a second consent decree (10-K Item 3). Disclosed plainly; a compliance failure repeated under a decree,
  in work done in pre-1978 homes. Carried to Q12.

**The habits carried from Q4** **[M2004-067]**: the adjusted figure featured in every release and 10-K overview
**[L2016-006]**; yearly guidance, to which the cash incentive is tied by the proxy's own words, the arrangement the 2019 letter
calls "the scourge of earnings "guidance" and the desire of CEOs to "hit the number."" **[L2019-006]**; the largest deal sold
on an adjusted EBITDA multiple and on accretion to adjusted EPS (8-K `0000060667-25-000162`). Read with the rest of the record:
the company lowered its own outlook in August 2026 rather than reach for it, takes its losses openly and in full, and
explains every adjustment with its amount. No instance found, in the 10-Ks, proxy and releases read, of a figure changed, a
reserve moved to make a quarter, or a misleading statement about the business; no instance found of the words "mistake" or
"wrong" about the company's own decisions in the 10-K, proxy or the four releases read (the sweep: a text search of those
documents), which is the taboo **[L2024-003]** describes, though a 10-K is not the place the rows expect such words.

**Integrity, on doubt alone** **[M2013-088]**, **[M2015-047]**. I have looked for a reason to doubt that these managers deal
honestly with their owners, and have not found one: the habits are the common habits of large American companies, which the
rows condemn and which weigh against here, but none of them, in this record, hides a cost or misstates a result; every
adjustment is reconciled to GAAP in the same document. The doubts I hold are about judgment with capital (Q6), not about
honesty. The lead-paint decree is a doubt about the control of contractors in customers' homes, weighed at Q12.

**VERDICT on integrity: IN**, with the habits recorded against **[L2016-006]**, **[L2019-006]**, **[M2012-095]**. **Ability
WEIGHS FOR** on running the stores (the margin gap closed, the foreign mistakes exited promptly **[M2017-007]**) and is carried
to Q6 as **AGAINST** on capital (FBM's return so far, the buyback prices). "the number one risk factor is that this business
gets the wrong management" **[M2021-042]**: for a business whose castle depends this much on staying smart (Q2), ability enters
"the degree of certainty that we attribute to the stream of income" **[M1999-104]** at Q7.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
"the biggest judgment you have to make is how well capital will be deployed in the future" **[M2001-111]**.

### Part A: the money

**The retention test** **[R1995-009]**, **[M1994-061]**, **[M1998-110]**. Lowe's has retained nothing, net, for a decade: it has
paid out more than it earned and borrowed the rest. Fiscal 2021 to 2025: net earnings $36,216M; dividends $12,087M; buybacks
$37,538M; paid out $49,625M, 137% of earnings, while debt rose from $21,780M (2021-01-29) to $39,921M (2026-01-30). The test
of a dollar kept does not apply; what applies is the price at which the dollars went back.

**Buybacks, with their prices** (10-K share-repurchase tables; average price per share, settlement basis):

| fiscal | 2010 | 2011 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| paid ($M) | 2,618 | 2,937 | 3,710 | 3,905 | 3,925 | 3,595 | 3,192 | 3,037 | 4,313 | 4,971 | 13,012 | 14,124 | 6,138 | 4,053 | 211 |
| average price | $23.28 | $24.51 | $43.10 | $52.57 | $71.21 | $74.89 | $80.01 | $96.18 | $104.68 | $144.08 | $207.32 | $198.39 | $210.07 | $244.63 | $243.48 |

*(Paid: cash-flow statement line "Repurchases of common stock". Average prices: as printed in the 10-Ks for fiscal 2015 to 2025;
for fiscal 2010, 2011, 2013 and 2014 computed from the programme shares and cost the 10-Ks print (111.7M for $2,600M; 118.3M
for $2,900M; 86.6M for $3,732M; 73.8M for $3,880M). Fiscal 2012 ($4,393M paid) has no price in the 10-Ks fetched. Fiscal 2025: the table's $116M for 0.5 million shares; the
cash-flow line, $211M, includes settlements the table excludes.)*

The programme names no price: each 10-K states a sum ("For 2022, we expect to repurchase shares totaling approximately $12.0
billion, subject to market conditions", 10-K `0000060667-22-000038`), never a value above which buying stops **[L2016-002]**.
By the framework's test (a programme with no stated price weighs against unless the prices paid sit at or below the bottom of
the Q7 range), read against today's range (Q7: bottom $139.05 a share on the all-equity basis, $170.14 equity-only): the
$40.6 billion paid in fiscal 2010 to 2020 at $23 to $144 sits at or about the bottom (fiscal 2020's $144.08 just above it);
the $37.3 billion paid in fiscal 2021 to 2024 at an average of about $208 (179.8 million shares) sits well above it and inside
the range, below its midpoint of $227.26. Today's range is a measure for today's business, larger than the business of 2010,
so the early purchases look cheaper against it than they were against their own day's value; the test is applied as written.
The largest purchases were made at the top of the surge with borrowed money, the opposite of buying with "available funds
-- cash plus sensible borrowing capacity -- beyond the near-term needs of the business" at a price "below its intrinsic value,
conservatively-calculated" **[L1999-023]**. "what is smart at one price is dumb at another" **[L2011-003]**. In fiscal 2025 the
company stopped buying to pay for FBM, which is the order the rows give (the business's needs first **[L2016-003]**, here
read as the company's chosen use).

**Deals: value given against value got** **[M1995-001]**, **[L1994-015]**. All in cash, none in stock, so the one STOP of Part A
(an all-stock deal by an undervalued acquirer **[L2009-019]**) does not arise.
- *FBM and ADG, 2025.* $10,088M paid, net of cash acquired (FBM $8.8 billion, ADG $1.3 billion). Financed by $5.0 billion of
  notes and a $2.0 billion term loan "designated to finance, in part, our acquisition of FBM" (10-K MD&A). Sold by ASP Flag
  Holdings LP, an American Securities vehicle (8-K `0000060667-25-000162`, EX-2.1): a private-equity seller, the "financial
  owner" whose business the rows warn "has been dressed up for sale" **[L2000-008]**. Priced on "an adjusted EBITDA multiple
  of 13.4x" and sold to owners as "accretive to adjusted diluted earnings per share in the first full year": "even a
  high-priced deal will usually boost per-share earnings if it is debt-financed" **[L2017-004]**. Value got, on the part's own
  filed record: operating income before amortization of about $164M in the first half of fiscal 2026, about $250M a year
  after tax at that rate, worth about $4.5 billion at the long bond with no growth (FBM grew revenue about 25% a year in
  2019 to 2024 "organically and inorganically", by the seller's own release, and keeps buying: $49M of further purchases since
  closing, 10-K Note 2). Value given: $10.1 billion. On the record so far the owners gave more than they got; the growth that
  would close the gap is the seller's history, not yet Lowe's.
- *RONA, 2016 (before this management).* $2,356M paid (fiscal 2016 cash flow); the Canadian business was sold in February 2023
  after $2.5 billion of pre-tax costs on the sale (Q4). Australia (a joint venture, impaired in fiscal 2015 and 2016 and sold),
  Mexico and Orchard (exited fiscal 2018 and 2019) complete the record of the decade's capital outside the US home centre:
  each ended in a write-off. "Post mortems of acquisitions [...] should instead be standard practice" **[L2014-013]**; no instance
  found in the 10-Ks read of one published for any of them (the sweep: the MD&A of each 10-K fetched).

**Dividends.** $4.75 a share declared in fiscal 2025, raised every year in the 10-Ks read; about 40% of net earnings. Neither
for nor against beyond the payout arithmetic above.

### Part B: the pay, the board and the owners
Read at Q5 from the proxy. For: the committee kept the acquired businesses out of the 2025 incentive results; the 2023 to 2025
performance shares paid nothing; the performance shares pay on a return on capital, in the spirit of "charge managers a high rate for
incremental capital they employ" **[L1994-019]** (the FBM debt raises the denominator). Against: cash incentive targets
set at the guidance given to investors **[L2019-006]**; payout floors and caps raised in the same year, the proxy says, to match market practice
**[L2005-015]**, **[M2012-095]**; a pay plan whose return measure divides by debt plus a deficit that buybacks shrink
**[M1998-017]**; the chief executive also chairs **[L2014-026]**; directors' holdings mostly granted, not bought
**[L2019-008]**; yearly guidance: "We don’t give out earnings guidance. We think it’s silly." **[M2016-002]**, and hitting targets
"becomes a catechism" **[M2022-054]**.

**Part A WEIGHS AGAINST**: the largest buybacks were made with borrowed money at prices inside today's value range and above its
bottom, with no stated price **[L2016-002]**, **[L2011-003]**, and the largest acquisition so far returns less than half its
price on its own record, bought from a financial owner on an EBITDA multiple **[M1995-001]**, **[L2017-004]**. **Part B WEIGHS
AGAINST**, mildly: the plan has teeth (no payout when ROIC missed) but ratchets and is tied to guidance **[M2012-095]**,
**[L2019-006]**.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is the
risk-free interest rate" **[L2000-021]**; value is "the discounted value of the cash that can be taken out of a business during
its remaining life" **[R1996-018]**, held as "a range of possibilities" **[L2000-024]**, and the price must "scream at you"
**[M2009-005]**. All arithmetic is in `q7.py`, its output in `q7_output.txt` and `q7b_output.txt`.

**The inputs.** Owner cash after every real cost, as recast at Q4 (operating cash less stock pay less all capital spending;
maintenance taken as all capital spending, the stated guess of Q3, so the maintenance-only case and the all-spending case
coincide). Working capital is counted (it is inside operating cash). All-equity basis: interest, net, added back after the
company's own effective tax (23.9% to 28.8% in fiscal 2019 to 2025; no carryforward or credit that runs out inside ten years
was found, so no shelter is priced). Rate: **5.60%** (Step 0). Floor: about 10% (CONVENTION of the framework). Net debt at the
latest filed balance sheet (10-Q `0000060667-26-000117`, 2026-07-31): debt $37,556M (current $2,352M, long-term $35,204M,
finance leases inside) less cash $3,172M and short-term investments $235M = **$34,149M**; operating lease liabilities ($4,467M)
left out, long-term investments ($179M) not deducted, said so; the filing states no subsequent event that changes it (the 8-K
of 2026-09-02 is officer appointments). At the fiscal year-end the same figure was $38,569M; July's is lower because the
selling season fills the cash and the payables, and the convention takes the latest date.

| fiscal | owner cash | interest, net | tax rate | before interest | net acquisitions | before interest, acquisitions deducted |
|---|---|---|---|---|---|---|
| 2012 | 2,451 | 425 | 37.6% | 2,716 | 0 | 2,716 |
| 2013 | 3,071 | 477 | 37.8% | 3,368 | 203 | 3,165 |
| 2014 | 3,930 | 516 | 36.9% | 4,256 | 0 | 4,256 |
| 2015 | 3,470 | 552 | 42.4% | 3,788 | 0 | 3,788 |
| 2016 | 4,360 | 645 | 40.5% | 4,744 | 2,356 | 2,388 |
| 2017 | 3,843 | 1,097 | 37.2% | 4,532 | 509 | 4,023 |
| 2018 | 4,945 | 624 | 31.8% | 5,370 | 0 | 5,370 |
| 2019 | 2,714 | 691 | 23.9% | 3,240 | 0 | 3,240 |
| 2020 | 9,103 | 1,908 | 24.6% | 10,542 | 0 | 10,542 |
| 2021 | 8,030 | 885 | 24.7% | 8,697 | 0 | 8,697 |
| 2022 | 6,537 | 1,123 | 28.8% | 7,337 | 0 | 7,337 |
| 2023 | 5,966 | 1,382 | 24.1% | 7,015 | -100 | 7,115 |
| 2024 | 7,477 | 1,313 | 24.0% | 8,475 | -177 | 8,652 |
| 2025 | 7,404 | 1,406 | 23.9% | 8,474 | 10,088 | -1,614 |

*(Interest, net = operating income less pre-tax earnings; fiscal 2012 and 2013 operating income from the EBIT margins the 10-Ks
print. Fiscal 2017's interest includes the cost of retiring notes early. Net acquisitions: "Acquisition of businesses - net"
less "Proceeds from sale of business". Fiscal 2020's operating cash carries a $3.2 billion rise in payables in the surge and
fiscal 2019's a working-capital outflow; they offset across the cycle.)*

**The window and the cycle (specific (a)).** The literal window is fiscal 2021 to 2025. Its first year is aberrational on the
filer's own description: "The COVID-19 pandemic had a significant effect on us in 2020 and 2021, affecting [...] demand for our
products and services" (10-K `0000060667-22-000038`); fiscal 2021's sales ($96,250M) and operating income ($12,093M) remain the
record. So the base is the average over the last full cycle. *CONVENTION of this run: the cycle is taken as fiscal 2019 to 2025*
(the last ordinary year before the surge, the surge, the three falling years and the turn), the same cycle on which Q2 credited
the change for the better; the previous seven years, fiscal 2012 to 2018 (recovery and expansion), give the earlier average.
Rationale: the filings show one housing boom and bust in the window and no clean peak-to-peak pair; the rows ask for the cycle
**[M2011-101]**, **[M2011-102]** and give no rule for marking it. The literal window is shown beside.

**Acquisitions (specific (c)).** The default pair deducts net acquisitions and credits the total growth; the organic pair leaves
acquisitions out, credits only the comparable-sales growth the filer reports (fiscal 2019 to 2025 compounding to 3.51% a year),
and adds the acquired part on its own filed record (Other segment, first half of fiscal 2026: operating income before
amortization about $164M, annualized and after tax about $250M, at no growth). The FBM debt is in today's net debt in both.

**The growth and the cap (specifics (b), (f)).** Default pair: cycle averages $3,672M (fiscal 2012 to 2018) and $6,281M (2019 to
2025), seven years apart: **7.97%** a year in aggregate, not per share. Its sources are visible and partly once-only: the
company tax rate fell from about 37% to about 24% with the 2017 tax law, and the operating margin stepped from about 8.5% to
about 12%. Is carrying it ten years an absurdity **[M1999-067]**? It would lift owner cash before interest from 7.2% of sales to
about 9.2% of sales by year ten at the cycles' sales growth (5.36%); Home Depot reached 9.0% in fiscal 2021 (operating cash
$16,571M less stock pay $399M less capital spending $2,566M, on $151,157M). Within the field's own record, so not cut back; the
shown rate is the cap inside the ten years, and zero nominal growth after **[M1997-095]**.

**The ranges** (per share on 561.054 million shares; all-equity figures net of $34,149M):

| case | base | growth | value range a share | width | midpoint |
|---|---|---|---|---|---|
| **central: cycle base, acquisitions deducted, total growth (default pair), all-equity** | $6,281M | 7.97% | **$139.05 to $315.46** | 2.27x | $227.26 |
| organic pair, all-equity (acquisitions left out, comps growth, FBM/ADG on record) | $7,932M | 3.51% | $191.60 to $272.83 | 1.42x | $232.22 |
| literal window fiscal 2021 to 2025, all-equity, acquisitions left out | $8,000M | -0.65% | $181.02 to $193.74 | 1.07x | $187.38 |
| literal window, acquisitions deducted | $6,037M | -0.65% | $121.69 to $131.29 | 1.08x | $126.49 |
| equity-only beside the central (owner cash after interest, acquisitions deducted) | $5,346M | 7.20% | $170.14 to $301.32 | 1.77x | $235.73 |

**Value range (central, all-equity): $139.05 to $315.46 a share against $186.00.** The range is narrower than about three to
one (2.27x), so it does not close TOO HARD **[L2000-025]**. The price sits inside it, in its lower half and below its midpoint,
not below its bottom: the case is not a screamer and would need the pencil this whole section has needed **[M2009-005]**,
**[M1996-084]**. The floor: at $186 the expected return on the midpoint stream (the stream whose value at 5.60% is the midpoint,
owner cash growing 4.60% a year for ten years then flat) is **6.47%** a year on the all-equity basis (6.99% equity-only); on the
top stream, the full 7.97% for ten years, 8.13%; on no growth, 4.53%. Every case is below the floor of about ten percent: "a point
at which we drop out of the game" **[M2003-149]**. The literal window's ranges straddle or sit below the price and close the
same way.

**Fair price (a reporting figure, never a verdict; Part VII): $92.61 a share** on the all-equity basis: the price at which the
midpoint stream earns 10% a year after the company's own tax (its value at 10%, $86,107M for the whole business, less net debt
of $34,149M, over 561.054 million shares). Equity-only beside it: **$126.20**. The organic pair gives $99.80 (all-equity) and
the equity-only organic pair $141.72. No cheap price is reported.

**How sure** **[M1999-104]**: the castle is the field's and Lowe's place in it depends on staying smart (Q2), the improved margin
has met a mild downturn and not a collapse (Q2), and the newest capital earns about 4% (Q3). Those widen the margin the rows
would ask **[M1997-080]**; they do not need to be priced, because the price fails the floor on the most generous case.

**VERDICT: OUT.** Valued, and the price does not clear the floor on any case built **[M2003-149]**; it sits inside a range
narrower than three to one, so the case would need a pencil **[M2009-005]**. "You can turn any investment into a bad deal by
paying too much." **[M2019-015]**

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
**NOT REACHED.** Q7 closed the file OUT (operator rule 2). Facts found are under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
**NOT REACHED.** Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
**NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
**NOT REACHED.** Facts under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7 on price.** Value range (central, all-equity, cycle base fiscal 2019 to 2025, acquisitions deducted, total growth
7.97% for ten years then none, at 5.60%): **$139.05 to $315.46 a share against $186.00**; the price sits inside a range narrower
than three to one and its expected return on every case built (6.47% on the midpoint stream, 8.13% on the top stream) is below
the floor of about ten percent. Q1 IN, Q2 IN (the retail part, with the higher-cost position and the faster loss of traffic
recorded against), Q3 weighs FOR, Q4 IN on the accounts (habits weigh against), Q5 integrity IN (habits recorded against;
ability for on operations, against on capital), Q6 weighs AGAINST. Reporting figures: fair price $92.61 (all-equity), $126.20
(equity-only).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.

**Bears on Q8 (the alternatives).** At $186 the expected return on the midpoint stream is 6.47% a year (all-equity) and on the
no-growth stream 4.53%, against the 30-year Treasury at 5.60% (Step 0); the comparison the rows make first is "to compare it
with a bond" **[M1997-089]**. Source: `q7b_output.txt`.

**Bears on Q9 (debt and exposures).** Debt $39,921M at 2026-01-30 (notes in seven maturity bands at average rates from 3.29% to
5.74%, a $1,999M term loan at 4.88% due October 2028, finance leases $391M) and $37,556M at 2026-07-31; principal maturities
$2,350M (fiscal 2026), $3,018M (2027), $5,005M (2028), $1,811M (2029), $2,500M (2030), $25,135M after (10-K
`0000060667-26-000029`, debt note). Interest coverage on the rows' definition, "pre-tax earnings/interest, not EBITDA/interest"
**[L2012-002]**: fiscal 2025 pre-tax earnings $8,747M against interest, net, $1,406M, 6.2 times (7.2 times on earnings before
interest). Cash $982M at the year-end and $3,172M at 2026-07-31, with undrawn revolving facilities of $2.0 billion to September
2030, $2.0 billion to September 2028 and $1.0 billion of 364-day credit to September 2026, backing a commercial-paper programme
with nothing outstanding at the year-end; the 10-K says its access to markets "depends on our strong credit ratings". Operating
lease liabilities $4,756M (2026-01-30). Shareholders' deficit $7,437M at 2026-07-31. Receivables, mostly contractors' trade
credit with FBM, $1,238M at 2026-07-31. The "little or no debt" criterion **[R1997-001]** is stated for whole businesses; the
company would not meet it.

**Bears on Q10.** Nothing beyond Q7's figures.

**Bears on Q12 (how the money is made).** The EPA lead-safe renovation matter (10-K Item 3): a 2014 consent decree, possible
deviations identified by the EPA in fiscal 2023, and on 2025-11-25 a $12,500,000 civil penalty and a second consent decree,
without admission of liability, over installations in homes built before 1978. The newspaper test is **[M2008-011]**. The
business (home-improvement goods and installation) is not among the businesses the rows name.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (the copy was the first file written, before any EDGAR call); written question
      by question. **Committed after each question: partly.** Step 0 to Q1 and Q2 were committed separately; Q3 to Q7 went in one
      commit (`d2304b79`) because `.git/index.lock` was held from 10:35:25 to about 10:42 and again from 10:42:37 to about 10:50
      with no live git process behind it (process 29756 not running); my retries, by hand and by `commit.py`, about thirty
      seconds apart, found it each time, and it was never deleted. Each of Q3 to Q7 was written and closed before the next was
      started.
- [x] Dispatched: the brief allowed the per-question pathspec commits; whether the dispatching session holds the lock in
      `Screens/_daily/` was not checked by me. The fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. **Contamination, added during the
      run** (not used): commit subjects of other runs seen in `git log` output while checking my own commits ("LOPE run: step 0
      ...", "LRCX run: Step 0 (price ...", "LSTR run: Q2 to the close, committed by the dispatch...", "LOPE run: Q1 IN, Q2 IN, Q3 weighs for, Q4 IN (habits weigh against), Q5 OUT on integrity (doubt) ...", "LSTR run:
      template copied ...", "LSTR run: Step 0 ... Q1 IN"), and the research-folder names of the LSTR and LRCX runs in a process
      listing made to find who held the git lock. None concerns Lowe's or its competitors.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`check_quotes.py`, output
      `check_quotes.txt`); every filing fact carries its accession or names its 10-K; every number is from a filing or from the
      stated arithmetic files.
- [x] The order was kept; Q7, the first STOP that failed, closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost (operating cash less stock pay less all capital spending), never a net-income proxy;
      the sovereign from the US Treasury par yield curve; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (the foundations' list; Q2 tests 2, 5 and 6; Q4's inventory and habits; Q6);
      facts for later questions under AFTER THE STOP.
- [x] No point-in-time anchor: a current run.
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py`: result in `check_framework.txt` before the final commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7, specific (a), gives no rule for marking the cycle.** The literal window's first year (fiscal 2021) is aberrational on
the filer's own words, but the text says only "peak to peak or trough to trough" and the filings show one housing boom and bust
with no clean pair of either; I confessed a convention of this run (fiscal 2019 to 2025 against 2012 to 2018), and the growth
it yields (7.97%) depends on that choice (the literal window shows -0.65%). (2) **Specific (c) and a debt-financed deal inside
the window.** The default pair deducts the $10.1 billion paid for FBM and ADG from owner cash, while the all-equity basis also
subtracts today's net debt, which holds the $7.0 billion borrowed for the deal; the sentence on a deal financed by debt does not
say whether the deduction still applies, so the same purchase is charged once as a recurring spending rate and once as a
liability. I applied the text as written and showed the organic pair beside; the box is the same either way. (3) **"the price at
which the midpoint of the range earns the floor"** does not say which cash stream is the midpoint; I used the stream whose
value at the sovereign equals the range's midpoint (owner cash growing 4.60% for ten years, then flat) and valued it at 10%.
(4) **Q6's buyback test reads prices paid years ago against today's range**, which flatters early purchases (the business, and
its value a share, were smaller then); I applied it as written and said so. (5) **The cap's "absurdity" has no test**; I used
the field's own filed record (Home Depot's owner cash reached 9.0% of sales) as the bound, which another analyst might set
elsewhere. (6) **Q2's credit for a change for the better "on a full cycle"** meets the same cycle problem as (1); I credited it on
fiscal 2019 to 2025 and recorded that its down years were milder than 2007 to 2009.

## THE BRIEF'S ERRORS (asked for by the dispatching message)
(1) **The hard sequence in the brief contradicts the template and operator rule 2.** The brief says that if no STOP among Q1 to
Q6 closes the file the analyst should "do Q7 to Q10", which read literally has Q8 to Q10 worked even after Q7, itself a STOP,
closes the file; the template says a STOP that returns OUT or TOO HARD "closes the run and later questions are marked NOT
REACHED". I followed the template. (2) **The lock rule has no end state.** "wait thirty seconds and retry, up to ten times" and
"never delete a lock file" do not say what the analyst does after the tenth failure, nor how the dispatcher learns that a lock
is stale; today a lock with no live owner held at least four analysts' commits for minutes at a time. (3) **The trailer
instruction is misplaced**: "(end the message with the project's trailer line)" now follows the lock paragraph added on
2026-10-10 instead of the commit command it qualifies. In the dispatching message's slots: Amazon and Walmart file no
home-improvement figures, so their "own filings" cannot give the same metric as the home-centre chains; they appear in the
competitor row as whole companies, flagged.
