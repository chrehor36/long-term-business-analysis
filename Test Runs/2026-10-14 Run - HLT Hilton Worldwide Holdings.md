# Company Run — Hilton Worldwide Holdings Inc. (NYSE: HLT) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to this dated name before any fetch** (commit
`b05b1215`).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for HLT or Hilton).

**Dispatched blind run.** Analyst dispatched under `Screens/_daily/_dispatch_brief.md` with one stated departure (the
lines of evidence derived by the analyst from Items 1, 1A and 7 of the 10-K, not supplied in the brief). Working folder
`Test Runs/_research 2026-10-14 HLT/` (notes, scripts, `calc_out.txt`, `peers_out.txt`; raw filings in its ignored
`cache/`).

**CONTAMINATION, declared before any work and not used.** The session opened with the repository's recent commit
subjects in view. One of them, the fold of another company's run of the same day, quotes a figure for Hilton
("operating income 50% of tangible assets against Hilton 43%"), names a valuation of that other company and an alert.
I did not open that run or its research, did not use the figure, and computed Hilton's own return on tangible assets
from Hilton's filings (Q2, where my figure differs). Nothing else of any blind-listed file was seen.

**The lines of evidence, chosen from the 10-K (Items 1, 1A, 7) and why.** (1) The two segments and their shares of
profit (Item 1 and Note 18: management and franchise against ownership), because the parts rule needs them. (2) Fees,
units and RevPAR across the last cycle, 2019 to 2025, including the 2020 to 2021 trough (Item 7, the RevPAR tables), for
pricing through the inflation and for the castle under stress. (3) The customer advances: Hilton Honors deferred revenue,
the guest loyalty liability, and the April 2020 pre-sale of points (Item 7 and Note 4), because they move operating cash
by hundreds of millions a year. (4) Contract acquisition costs ("key money") and capital spending, which Item 7 names
as the uses of cash the segment measure leaves out. (5) Acquisitions and goodwill (Note 3: Graduate and NoMad, 2024;
goodwill and brands from the 2007 buyout). (6) Debt, leases and guarantees (Notes 10 and 19, Item 7's lease payments; Note 12 not read; the 8-Ks of 2025-07-07,
2025-12-11, 2026-03-18 and 2026-05-11). (7) Buybacks and their prices (Item 5; the Q2 2026 release). (8) Stock pay and
the pay design (Note 15; the 2026 proxy). (9) Litigation and investigations (Item 3; Note 19; a search of the 10-Ks and
the 2013 IPO prospectus). (10) The risks Item 1A puts first: competition, owners' capital, internet and AI travel
intermediaries, the loyalty program, cyclicality.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $329.59 (close 2026-10-13, from the aggregator quote `tools/run.py` prints; aggregator, live quote only, flagged
  per operator rule 5).
- **Shares by class** from the latest filing's cover: one class of common stock, **225,064,910 shares outstanding as of
  July 23, 2026** (10-Q for the quarter ended June 30, 2026, filed 2026-07-28, accession `0001585689-26-000043`).
  `python Screens/cover_shares.py HLT` parsed no cover count ("read the filing by hand"); the count above was read by hand
  from the 10-Q cover and matches the tagged dei figure `tools/run.py` prints (225.065M). Check against issued less
  treasury: the 10-Q balance sheet shows 225,696,464 outstanding and 112,124,356 treasury shares at June 30, 2026; the
  difference to the cover is July repurchases. No 8-K, prospectus or other filing after 2026-07-28 is in the EDGAR index
  fetched 2026-10-14. No other class; no charter note bearing on the count.
- **Market cap:** $329.59 × 225.065M = **$74,179M**.
- **Sovereign for the earnings currency (USD):** **5.56%**, the U.S. Treasury daily par yield curve, 30-year, 10/13/2026
  (issuing authority; via `tools/run.py`'s fetch of the Treasury curve).
- **Filings read** (operator rule 4): the **10-K for FY2025**, filed 2026-02-11, accession `0001585689-26-000007` (Items 1,
  1A, 2, 3, 5, 7, 7A, 8 with Notes 3, 4, 5, 10, 13, 18, 19, 20); the **10-Q for Q2 2026**, filed 2026-07-28,
  `0001585689-26-000043`; the **2026 proxy (DEF 14A)**, filed 2026-04-02, `0001585689-26-000023`; the **8-Ks** of
  2025-07-07 (`0001193125-25-156239`), 2025-12-02 (`0001193125-25-305253`), 2025-12-11 (`0001193125-25-315917`, the 5.500%
  2034 notes, whose proceeds redeemed the 2028 notes; its 1.02 item was not read further), 2026-03-18 (`0001193125-26-113998`, revolver amendment),
  2026-05-05 (`0001193125-26-205180`, an officer's retirement), 2026-05-11 (`0001193125-26-217102`, 5.500% 2031 notes),
  2026-05-18 (`0001585689-26-000037`, annual meeting and plan amendment) and 2026-07-28 (`0001585689-26-000042`, with the
  Q2 2026 earnings release, Exhibit 99.1); for the cycle, the **10-Ks for FY2018** (`0001585689-19-000034`), **FY2019**
  (`0001585689-20-000013`), **FY2021** (`0001585689-22-000013`), **FY2022** (`0001585689-23-000036`) and **FY2024**
  (`0001585689-25-000008`); and the **IPO prospectus** (424B4, 2013-12-13, `0001193125-13-473211`), searched only.
  **One figure cross-checked against the filed statement:** net cash provided by operating activities for 2025, **$2,129
  million** on the filed consolidated statement of cash flows (10-K, page 62), equals the tagged figure `tools/run.py` prints;
  share-based compensation expense, $170 million, also agrees.
- `python tools/run.py HLT` arithmetic lines only (its output is in the research folder's `cache/`; nothing it prints as a
  rule, id or floor is used, Part VII): OCF 2023 to 2025 $1,946M, $2,013M, $2,129M; stock pay $169M, $176M, $170M; capital
  spending (property plus software) $247M, $198M, $185M; D&A $147M, $146M, $177M; finance-lease principal (financing
  section) $40M, $38M, $41M. Its owner-cash columns leave out acquisitions and finance-lease principal; the run's own owner
  cash (below, Q4 and Q7) deducts both. Stock pay is resolved and complete (one tag every year; the 15% employee purchase
  plan discount is inside it per Item 1). The full nine-year owner-cash table is in `calc_out.txt`, built from the filed
  cash-flow statements of the FY2019, FY2022 and FY2025 10-Ks.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is the share as a business: "**Would I be happy buying this stock if the market closed
for five years?**" **[M1997-109]**. Hilton is a business that owns almost no hotels and is paid a share of other people's
room revenue for its brands, its loyalty program and its booking system; a buyer of the stock buys that fee stream and
the debt the company has put in front of it. The margin of safety is the second: "if you have to actually do it on — with
pencil and paper, **it’s too close to think about**" **[M1996-084]**. The analyst's habit the brief
names governs the method: look in every business for "what’s wrong" and "what you’re missing" **[M2025-013]**, with the
research aimed "to possibly reject your original hypothesis" **[M1998-144]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the 10-K's own risk list puts internet travel intermediaries "including with the aid of AI" and the
loyalty program's possible "cessation, reduction or taxation" among the risks (Item 1A); (2) system ADR rose only from
$144.79 (2019, FY2019 10-K) to $159.89 (2025) while comparable occupancy fell from 75.7% to 71.5%, so room prices did
not keep pace with a six-year stretch the 10-K itself calls inflationary; (3) operating cash includes customer advances
(Honors deferred revenue and the loyalty liability) that rose $481M to $572M a year in 2023 to 2025 and a $1.0 billion
point pre-sale in 2020, and the company's own pay metric strips "loyalty program advanced point sales" out of free cash
flow (proxy, PSU definitions); (4) shareholders' equity went from $2,072M (2017) to a deficit of $5,388M (2025) while debt
rose from $6.7B to $12.5B, the buybacks paid for partly with borrowed money; (5) the company features Adjusted EBITDA and
an EPS "adjusted for special items", and gives quarterly and annual guidance (Q2 2026 release).

## THE STANDING RULE
Nothing in this file is financed, sized or held; a purchase of these shares for cash, unlevered, puts the buyer at no risk
of ruin: "We are **never going to risk what we have and need for what we don’t have and don’t need**" **[M2012-081]**;
"borrowed money has no place in the investor's tool kit" **[L2014-005]**. The target's own debt is a separate matter,
weighed at Q9.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the rows state it:** understanding is "a reasonable fix on about **what the earning power and competitive
  position will look like in five or 10 years**" **[M2012-065]**; "the first step" is "trying to identify the key variables
  in that particular business, and evaluating how predictable they were" **[M1998-044]**.
- **The key variables, from the filing.** Hilton's revenue that is its own (not reimbursed) was $4,954M in 2025 (10-K,
  statement of operations): franchise and licensing fees $2,780M, management fees $689M, ownership $1,233M, other $252M.
  The fees are "generally based on a percentage of the hotel’s monthly gross room revenue" (franchise royalty) and of
  gross operating revenue and operating profit (management) under contracts whose "initial terms [...] are typically 20 to
  30 years" (managed) and "approximately 20 years for new hotels" (franchised) (Item 1). So the earning power is
  (rooms in the system) × (revenue per room) × (the fee rate), plus licensing fees from the co-branded credit cards and
  HGV. Rooms: 1,351,351 at December 31, 2025, net unit growth 6.7% in 2025, a pipeline of 520,500 rooms "almost half"
  under construction, and "Nearly all of the rooms in our development pipeline will be in our management and franchise
  segment" (Item 1). Revenue per room: cyclical; "demand generally follows, on a lagged basis, key macroeconomic
  indicators" (Item 1, Cyclicality). The fee rate: contractual, with "increases of in-place rates charged to hotels"
  named as the cause of 2025's comparable franchise-fee gain (Item 7).
- **How predictable.** The contracts run two to three decades, the owners pay for the buildings, and the variables are
  rooms, room prices and a contractual percentage; the forecast is about where travellers will sleep and through whom
  they book, a forecast about customers rather than technology, the kind the rows say can be projected: "we know what we
  think we can project out in terms of consumer behavior and threats to a business" **[M2023-030]**; the Apple row draws
  the same line **[M2017-019]**. The insiders do write the forecast down: the company publishes net unit growth of 6.0% to
  7.0% and RevPAR ranges for 2026 (Q2 2026 release), so the insiders' test of TOO HARD (NATURE) **[M2000-105]** is not
  met. The past statements tell the future ones in the sense of **[M2008-033]**: the fee lines move with rooms and RevPAR,
  as the 2020 collapse and 2022 recovery show (fees $2,315M in 2019, $1,138M in 2020, $2,619M in 2022; Note 18 of the
  FY2019 and FY2022 10-Ks).
- **Contrary evidence on understanding.** Two things could move the ten-year economics in ways I cannot foresee: who owns
  the booking (the 10-K's own risk names "third-party internet and other travel intermediaries [...] including with the
  aid of AI"), and the loyalty program's economics, which the critical-accounting section says rest on actuarial
  estimates of breakage and cost per point. I can name both and read their present size; I cannot say where the
  intermediary question will stand in ten years with confidence. That is a castle question (Q2, test 11), not a reason
  the business cannot be understood: the routing sends a business to TOO HARD at Q1 where its industry changes fast, the case of "where we think the
  future technology could hurt the business as it presently exists [...] it won’t make it through the filter" **[M1998-008]**. Hotel
  branding and franchising has run in the same form for decades; the threat is a change in distribution, carried to Q2.
  Doubt about the perimeter is the stronger test: "if you have doubts about something being into your circle of
  competence, it isn’t" **[M2002-092]**. I do not doubt that the fee stream can be modelled; I doubt how wide the
  intermediary threat is, which is Q2's question.
- **Parts.** Two segments; management and franchise is 95% of segment Adjusted EBITDA in 2025 ($3,575M of $3,752M) and
  every year of the window; ownership (46 hotels, mostly leased) is small. Q1's holding-company rule reaches operating
  segments; the deciding part is understood; the ownership part is a plain leased-hotel business.
- **VERDICT: IN.** The economics are a percentage of other people's room revenue under long contracts, and the key
  variables (rooms, revenue per room, fee rate) are named and published by the filer; the open question is the castle's,
  not the circle's **[M1995-051]**, **[M2012-065]**, **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "**why is that castle still standing?** And what’s going to keep it standing or cause it not to be standing
**five, 10, 20 years from now.**" **[M1995-038]**. A moat is what "protects excellent returns on invested capital", and
competitors "will repeatedly assault" any castle that earns them **[L2007-004]**.

**The parts table** (segment profit, Note 17 of the FY2022 10-K and Note 18 of the FY2025 10-K; the measure was segment
operating income through 2022 and segment Adjusted EBITDA from 2023, and in both the management and franchise segment's
profit equals its fee revenue because "No expenses are allocated to the management and franchise segment"):

| part | 2021 to 2025 segment profit | share | castle | decides |
|---|---|---|---|---|
| management and franchise | $14,397M (1,809; 2,619; 3,055; 3,339; 3,575) | 97% | brands, loyalty program, booking system, owners under 10- to 30-year contracts | **yes** (more than half) |
| ownership (46 hotels, 40 leased) | $462M (−91; 54; 150; 172; 177) | 3% | none claimed; the 10-K lists leased real estate among its risks | no; carried at Q7 as an ordinary business inside consolidated owner cash |

The file closes on the management and franchise segment ("lumping them together [...] impedes analysis" **[L2008-005]**;
a collection can hold "a few that are marginal" **[L2021-001]**). One caution the table hides: no expenses are allocated
to the segment, so its "profit" is gross of the corporate cost of running the brands; the whole company's figures (Q3,
Q4, Q7) carry those costs.

**The castle tests, each with its filing fact.**
1. **What keeps it standing, and how permanent** **[M1995-038]**. The customer of the franchisor is the hotel owner, who
   pays a royalty on room revenue and program fees because the brand, the reservation system and Hilton Honors (243
   million members at December 31, 2025, up 15% in a year; Item 1) fill rooms. The 10-K states the mechanism: "Affiliation
   with our loyalty program encourages members to allocate more of their travel spend to our hotels", and the share of
   spend captured "increases as they move up the tiers" (Item 1). The second customer is the traveller, whose points tie
   him to the system. The reason is a network: more hotels make the program more useful, which brings more members, which
   brings more owners. It does not depend on "the genius of the lord in the castle" **[M1995-038]**: the owners run or pay
   for the buildings.
2. **The money test** **[M2011-015]**, **[M1997-103]**. Could a well-funded attacker build a rival system of 1.35 million
   rooms, 9,158 properties in 143 countries and a 243-million-member program? The owners, not the attacker, would have to
   sign 20-year contracts and pay for conversions, and they sign where the system fills rooms. The filing names the rivals
   that exist (Accor, Choice, Hyatt, IHG, Marriott, Wyndham; Item 1). The rows ask "why are there no new entrants into the
   field?" **[M2000-077]**: in the filings read, Hilton grew by brands launched or bought inside its own system (Graduate
   and NoMad bought in 2024, Note 3; Spark, LivSmart, Apartment Collection and Undergraduate launched; Item 1 and the Q2
   2026 release), and no new system of comparable size appears among the named rivals. That is the evidence I have; it is
   not a test I can run.
3. **Pricing power, and the agony before a rise** **[M2005-020]**. Two prices matter. (a) The fee rate charged to owners:
   2025's comparable franchise-fee gain was "largely attributable to increases of in-place rates charged to hotels,
   partially offset by a decrease in fees due to a decrease in RevPAR" (Item 7): Hilton raised its take in a year its
   franchisees' comparable RevPAR fell 0.8%. (b) The room rate: system ADR $144.79 (2019) to $159.89 (2025), +10.4% in six
   years; system RevPAR $109.65 to $114.39, +4.3%; occupancy 75.7% to 71.5% (FY2019 and FY2025 10-Ks, each year's comparable
   set). Across a stretch the 10-K itself calls one of "elevated levels of inflation", room prices rose slowly in nominal
   terms: the hotels' power over the traveller looks weak. Fee revenue per management-and-franchise room: $2,457 (2019),
   $2,389 (2022), $2,676 (2025), +8.9% in six years; the franchisor's take per room kept just ahead of room prices, and its
   growth is units, not price. "over time the businesses with strong competitive positions manage to pass through increases"
   **[M2005-017]**: the owners' fee rate passed through; the room rate, on these figures, largely did not.
4. **Unit volume and share of mind** **[M1997-099]**. Rooms in the management and franchise segment: 942,307 (2019),
   1,096,115 (2022), 1,336,064 (2025), 6.0% a year; net unit growth 6.7% in 2025 and 6.1% in the year to June 2026; pipeline
   541,300 rooms at June 30, 2026, up 6% in a year (Q2 2026 release). Owners kept choosing the system in volume through a
   downturn and through the rate rise the 10-K says delayed openings (Item 7, System Growth).
5. **The brand in the mind, and against the intermediary** **[M2015-038]**. The rows' warning is exact: "to the extent that
   people trust Costco or Walmart more than they [...] trust the brand, then the value of having the brand moves over to the
   retailer" **[M2001-090]**; "the brand is our protection against the intermediaries making all the money" **[M2019-041]**.
   Here the intermediaries are the online travel agencies and, newly, AI agents; the 10-K says shifting customer loyalties
   "divert bookings away from our websites, which increases costs to hotels in our system" (Item 1A). The filing gives no
   share of bookings by channel, so I cannot measure the shift. The loyalty program is the defence the filing names, and
   its growth (members +15% in 2025) is the only number I have on it.
6. **Would the customer still choose it over the low bid** **[M2017-009]**. The owner: yes, on 6% unit growth a year while
   paying rising fee rates. The traveller: partly; room nights are shopped on price through the intermediaries, and system
   occupancy fell 4.2 points from 2019 to 2025.
7. **Widening or narrowing** **[M1999-108]**, **[L2005-010]**. Widening in units and members (tests 4 and 5); flat to
   narrowing in price per room against inflation (test 3). On the field's returns below, the castle earns at least what its
   largest rival earns.
8. **What could destroy it, five to fifteen years out** **[M2000-014]**. (a) Distribution captured by intermediaries or AI
   agents, turning the brand into a supplier to the platform (test 5); (b) the owners' economics: hotel costs "tend to be
   more fixed than variable" (Item 1) and owners finance construction at rates the 10-K says have delayed openings; if
   owners' returns fall, unit growth slows, and Hilton's growth is the owners' capital; (c) the loyalty program's
   "cessation, reduction or taxation" (Item 1A). "If the technology had not changed, they’d still be impregnable
   franchises. But the technology did change." **[M2006-065]** is the failing case to keep in view for (a).
9. **The castle under stress, a full cycle.** Management and franchise fees fell 51% in 2020 ($2,315M to $1,138M), were
   above 2019 by 2022 ($2,619M) and 54% above it by 2025 ($3,575M); rooms grew through the trough (942,307 in 2019 to
   1,096,115 in 2022). The asset-light shape dates from the January 2017 spin-offs of Park Hotels & Resorts and Hilton Grand
   Vacations (the Distribution Agreement, exhibit 2.1 of the 10-K), so the change for the better has been through one full
   cycle with the price behaviour held: the filings read show no cut in the fee rate to keep owners, and the system grew
   **[M2005-020]**, **[L1995-022]**.

**The competitor row** (operating income over net tangible assets, assets less goodwill and intangibles; each company's
own 10-K figures as tagged in XBRL, transcription, flagged; `scripts/peers.py`, `peers_out.txt`):

| company (source) | 2019 | 2020 | 2022 | 2025 | mean 2017 to 2025 |
|---|---|---|---|---|---|
| Hilton (its 10-Ks; intangibles from its balance sheets) | 45% | −7% | 46% | 54% | 39% |
| Marriott (MAR, CIK 1048286, its 10-K facts) | 24% | 1% | 48% | 50% | 36% |
| Choice Hotels (CHH, CIK 1046311, its 10-K facts) | 34% | 11% | 42% | 29% | 32% |
| Hyatt (H, CIK 1468174, its 10-K facts; operating income untagged, so pre-tax income plus interest, which carries asset-sale gains) | 14% | −10% | 7% | 5% | 8% |

Named rivals not read: **Accor** is not in the SEC's company-ticker file (no SEC filer found); **IHG** and **Wyndham** file
with the SEC and were not read, the brief's limit being three. Hilton's figure includes its leased hotels and the net
program costs it spends above reimbursements ($465M in 2025; Q4), which lower it; it is still the highest of the four over
the span. Choice held up best in the 2020 trough; Hilton alone of the three asset-light filers had an operating loss that
year (it carries $258M of impairments and $397M of net program costs; FY2022 10-K, Note 17).

**The field's returns over the last full cycle, in words.** The franchisors that own few hotels (Hilton, Marriott, Choice)
earned operating returns on tangible capital in the thirties to fifties across 2017 to 2025, through a trough in which
revenue halved; the one that owned many hotels (Hyatt) earned single digits. A durable castle that protects only ordinary
returns closes OUT; this field's asset-light players do not earn ordinary returns, and Hilton earns as much as the best of
them **[L2007-004]**, judged in words, since the moat has "no formula" that measures it **[M1999-108]**.

**Why not TOO HARD.** The tenuous moat goes to TOO HARD because "We don’t know how to valuate that" **[M2000-019]**. The
intermediary threat is real and unmeasured in the filing, but the castle has a decade of filed evidence including a full
downturn, and the threat bears on growth and the fee rate, which Q7 can bracket; it does not leave the cash stream
unpicturable.

- **VERDICT: IN**, on the deciding part: a network of owners, members and booking channels that owners keep joining at 6% a
  year while paying rising fee rates, tested through a 51% fee collapse and recovered within two years, and earning returns
  on tangible capital at the top of its field **[M1995-038]**, **[L2007-004]**, **[M2011-015]**. Carried against it: room
  prices lagged the inflation (test 3), the intermediaries' share is unmeasured (test 5), and growth rests on the owners'
  capital (test 8).

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, measured on tangible assets **[M2011-060]**. Hilton's operating
  income on net tangible assets was 45% (2019), 46% (2022), 54% (2025), a mean of 39% over 2017 to 2025 with the 2020 loss
  inside it (Q2's competitor row). The tangible base is small and mostly not Hilton's money: of $16.8B of assets at
  December 31, 2025, goodwill ($5.1B) and brands ($5.0B) are the 2007 buyout's purchase accounting, and the largest
  tangible items, receivables ($1.7B) and cash ($0.9B), are matched by payables ($2.3B) and by customer advances (deferred
  revenues and the loyalty liability, $5.4B). Read with care before credit **[L1994-009]**: not a cyclical peak (the mean
  spans a trough), not leverage on the operating return (operating income is before interest), and the return on equity is
  meaningless here because equity is negative from buybacks, the case the rows name, "if you keep the equity low enough by
  buying shares back, why, you could make return on equity whatever you want" **[M1998-017]**.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. Hilton's own spending, 2019 to 2025:
  property $549M, capitalised software $559M, contract acquisition costs ("key money", paid to owners to sign or renew,
  inside operating cash) $990M, acquisitions (Graduate, NoMad) $240M; $2,338M in seven years, about $334M a year against
  owner cash before interest of $1.27B (2019) rising to $2.24B (2025). The filing does not split maintenance from growth;
  it says the pipeline "will require minimal capital investment from us" (Item 1) and guides 2026 "Contract acquisition
  costs and capital expenditures, excluding amounts reimbursed by third parties" at about $300M (Q2 2026 release). The
  owners pay for the hotels: "the capital required to build, renovate and maintain hotels is typically provided by the
  third-party owners" (Item 7). This is the business that throws off cash rather than leaving "your profit sitting in the
  yard" **[M2008-036]**.
- **What the added capital earned.** Owner cash before interest rose by $974M a year from 2019 to 2025 against $2,338M of
  Hilton's own spending in the same years, about 42 cents of added annual cash per dollar spent. Most of the added cash was
  bought with the owners' capital (6% more rooms a year), not Hilton's, which is the point of the model; the rows' best
  business is one "that gives you more and more money every year without putting up anything to get it, or very little"
  **[M1998-081]**, and growth is "wonderful" where "it requires relatively little incremental investment" **[M2001-019]**.
- **The growth arithmetic and its caps** **[M2003-120]**, **[M1999-067]**. The rate is capped by rooms, room prices and the
  fee rate: rooms grew 6.0% a year 2019 to 2025, fee revenue per room 1.4% a year, management and franchise fees 7.5% a
  year, Hilton's own sales (revenue before reimbursements) 4.7% a year (ownership shrank as leases ended). A rate of owner
  cash above those cannot be carried long; Q7 applies the cap.
- **Against.** (1) Key money is rising: $231M in 2025 against $90M in 2019, and the 10-K names "increases in cash paid for
  contract acquisition costs of $126 million" in 2025 (Item 7): the price of each new contract is going up. (2) Hilton's
  growth is the owners' capital; when owners' financing tightens, openings slow (Item 7), and Hilton cannot substitute its
  own money without becoming a capital-heavy business. (3) The leased hotels need capital "to deliver properties back to
  lessors in a particular state of repair" (Item 1A).
- **WEIGHS FOR.** A business that earns 40% to 50% on tangible capital and grows mainly on other people's capital is the
  rows' first grade, "more and more money every year without putting up anything to get it, or very little"
  **[M1998-081]**, **[L2007-008]**; the rising price of key money is carried as the weight against.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them, before the income account** **[M2025-032]** (USD millions, year-end; `tools/run.py`'s
first-filed tagged table, read against the filed balance sheets of the FY2018, FY2019, FY2021, FY2022, FY2024 and FY2025
10-Ks, which agree where read; brands and contracts from those statements):

| year-end | assets | goodwill | brands + contracts + other intangibles | cash | receivables | debt (incl. finance leases) | equity (Hilton) | accumulated deficit |
|---|---|---|---|---|---|---|---|---|
| 2016 (before the spin-offs) | 26,211 | 5,822 | n/a | 1,418 | 1,005 | 10,118 | 5,899 | −3,323 |
| 2017 | 14,308 | 5,190 | 6,276 | 570 | 998 | 6,602 | 2,072 | −6,596 |
| 2018 | 13,995 | 5,160 | 6,156 | 403 | 1,150 | 7,282 | 551 | −6,417 |
| 2019 | 14,957 | 5,159 | 6,078 | 538 | 1,261 | 7,993 | −482 | −5,965 |
| 2020 | 16,755 | 5,095 | 5,823 | 3,218 | 771 | 10,487 | −1,490 | −6,732 |
| 2021 | 15,441 | 5,071 | 5,835 | 1,427 | 1,068 | 8,766 | −821 | −6,322 |
| 2022 | 15,512 | 5,032 | 5,888 | 1,209 | 1,327 | 8,747 | −1,102 | −5,190 |
| 2023 | 15,401 | 5,052 | 6,083 | 800 | 1,487 | 9,196 | −2,360 | −4,207 |
| 2024 | 16,522 | 5,035 | 6,419 | 1,301 | 1,583 | 11,151 | −3,727 | −2,822 |
| 2025 | 16,774 | 5,081 | 6,700 | 918 | 1,690 | 12,363 | −5,388 | −1,508 |

What moved and why. (1) **The 2017 spin-offs** of Park Hotels & Resorts (the owned hotels) and Hilton Grand Vacations
(timeshare) took assets from $26.2B to $14.3B and charged the accumulated deficit; 2016 is a different company and is not
used anywhere in this run. (2) **Goodwill and brands** have sat at about $5.1B and $4.9B to $5.0B for nine years: they are
the 2007 buyout's purchase accounting ("the Merger", Item 7), never written down and never grown except by the 2024
Graduate and NoMad brands. They are 60% of assets and say nothing about what the business earns: "in evaluating the businesses we own [...]
forget about goodwill", but in judging the capital allocation "you have to include goodwill, because we paid for it"
**[M2011-060]**. (3)
**Receivables** rose from $998M to $1,690M (+69%) while management and franchise fees rose from $1,927M to $3,575M (+86%):
collection held up as the fee base grew; the allowance for credit losses was $163M against $145M a year earlier. (4)
**Cash** spiked in 2020 ($3.2B: the revolver drawn, notes issued, $1.0B of points pre-sold to American Express; FY2021
10-K) and has otherwise been kept below $1.5B. (5) **Debt** rose from $6.6B (2017) to $12.4B (2025) and $13.4B at June 30,
2026 (10-Q), while (6) **equity** fell from +$2.1B to −$5.4B: the accumulated deficit improved by $5.1B as earnings were
kept, and treasury stock grew to $14.4B (2025) and $16.2B (June 2026). Buybacks of $14.4B in 2017 to 2025 exceeded the
$8.8B of owner cash (after interest, all spending) those years produced; the difference was borrowed. (7) **Customer
advances**: Hilton Honors deferred revenue and the guest loyalty liability totalled $5,419M at the end of 2025 (current and
non-current deferred revenues $858M and $1,648M; loyalty liability $1,289M and $1,624M), up $481M in the year; operating
cash took in $2,576M from their growth over 2019 to 2025, of which the April 2020 pre-sale of points to American Express
for $1.0B (FY2021 10-K) was used up by mid-2022 (FY2022 10-K). What the figures say: the company is financed by its lenders
and its customers, its own tangible capital is small, and its equity is a residue of buybacks. What they do not say:
whether the brands are worth more or less than their 2007 carrying value. What they cannot say: what the advances will do
if the system stops growing.

**The real costs.**
- **Stock pay**, $170M (2025), $176M, $169M: a real cost **[L2015-003]**, deducted in owner cash. The PSU, RSU and option
  grants are expensed (Note 15).
- **Depreciation and software.** D&A was $177M in 2025, "primarily related to software placed in service" (Item 7);
  software amortization is a real expense **[L2012-003]**; owner cash deducts the cash spent on property and software
  instead.
- **Key money.** Contract acquisition costs are paid in cash (inside operating cash, $231M in 2025) and amortized as a
  reduction of fee revenue ($57M); Adjusted EBITDA adds the amortization back.
- **FF&E replacement reserves**, $73M in 2025, a cash cost of the leased hotels, added back in Adjusted EBITDA.
- **The reimbursed programs.** Reimbursed expenses exceeded cost reimbursement revenues by $337M (2023), $557M (2024) and
  $465M (2025) (statement of operations). The company excludes both from Adjusted EBITDA on the ground that "over the life
  of the operation of these programs, the expenses incurred related to the indirect reimbursements are designed to equal
  the revenues earned [...] such that, in the long term, the programs will not earn a profit or generate a loss" (Item 7).
  Part of the gap is cash received and deferred (the advances above), so operating cash, which this run uses, counts the
  programs on a cash basis. But on the income account the gap has run one way three years running, and "to tell owners
  year after year, "Don't count this," [...] is misleading" **[L2016-007]**.
- **Recurring "other" items**: other adjustments $80M (2025), $34M (2024), $28M (2023); losses on debt guarantees $50M
  (2024) and $77M paid; the 2023 $92M loss on an unconsolidated fund; a list of one-off items that recurs every year,
  costs "that should properly be attributed to a number of years" **[L1998-031]**; "we do not ask you to forget about
  those costs" **[M1999-023]**.
- **Interest and tax.** Interest paid $648M (2025) on $12.5B of debt; income tax paid $523M. The 2024 net income carries a
  $270M tax benefit "for increased foreign tax basis for certain brand assets" (Item 7), a deferred item that left cash
  taxes unchanged. Loss carryforwards are almost all non-expiring ($461M of $493M of deferred tax assets; $32M expire 2026 to
  2045; Note 13), so no shelter is priced separately (Q7, Whose tax). Pensions are frozen (1996 domestic, 2013 U.K.; Note 14).

**EBITDA in the filer's own mouth, and the habits.** The 10-K defines Adjusted EBITDA, lists its limitations fairly
("should not be considered as discretionary cash available to us"), and uses it as the measure of both segments and of
pay. The earnings releases lead with GAAP diluted EPS and net income, then "diluted EPS, adjusted for special items" and
Adjusted EBITDA, and give quarterly and annual guidance for each (Q2 2026 release: full-year 2026 Adjusted EBITDA
"between $4,040 million and $4,080 million"). 2025 Adjusted EBITDA of $3,725M was "slightly above 100% of the target goal"
(proxy). Adjusted EBITDA ($3,725M) against operating income ($2,693M) against owner cash before interest ($2,241M), 2025:
the featured figure is 66% above the cash the owner could take out. The rows: "The one figure we regard as utter nonsense
is the so-called EBITDA" **[M1998-086]**; "the number of times we’re going to buy into a company [...] where people are
talking about EBITDA, is going to be about zero" **[M2002-026]**; "the scourge of earnings "guidance"" **[L2019-006]**; a
management that features adjusted earnings "makes us nervous" **[L2016-006]**. Under the convention of section A (2026-10-06)
these are recorded here as a WEIGHING against and carried to Q5; the STOP falls on the accounts themselves.

**The accounts themselves: confusion or suspicion?** Not confusing: operating cash reconciles to net income line by line,
the reimbursement netting is explained, the pre-sale is disclosed with its amount and its use. No tell of suspicion found
in the statements read: receivables grew slower than fees; prepaid expenses ($219M against $193M) and other current assets
are small and steady; no reserve release found; no gain-on-sale income in the cash figures used. A plus: the 10-K lists in
plain terms what Adjusted EBITDA leaves out, a management that "does explain to you in clear terms what’s going on"
**[M1994-018]**.

- **VERDICT on the accounts: no STOP (neither confusion nor suspicion); WEIGHS AGAINST** on the featured Adjusted EBITDA
  and adjusted EPS, the guidance, a pay target met at "slightly above 100%" (proxy), and the reimbursed-program gap excluded
  year after year **[M1998-086]**, **[L2019-006]**, **[L2016-007]**; carried to Q5. **The recast earnings for Q7**: owner cash =
  operating cash − stock pay − property and software spending − finance-lease principal − acquisitions; before interest it
  adds back cash interest paid at (1 − 21%). Cycle 2019 to 2025: $1,033M a year after interest, $1,398M before (Q7).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
**The people** (2026 proxy): Christopher J. Nassetta, 63, President and Chief Executive Officer since December 2007,
before that chief executive of Host Hotels and Resorts (2000 to 2007); he beneficially owns 4,664,062 shares (2.0%; about
$1.5B at $329.59), most in a revocable trust and a family LLC. Kevin J. Jacobs, CFO, with Hilton since 2008. The board is
led by a non-executive chair, Jonathan D. Gray (President and COO of Blackstone, chair since the 2007 buyout, 740,105
shares), and a lead independent director, Douglas M. Steenland; the chair and chief executive roles are separate.

**The two yardsticks** **[M1994-008]**. (1) *How well they run the business, against the hand dealt*: the team took a
leveraged, hotel-owning company from the 2007 buyout through the 2013 IPO and the 2017 spin-offs to a fee business with
the highest return on tangible capital of the three asset-light rivals read (Q2), grew rooms 6% a year through a pandemic
that cut fees by half, and raised liquidity in 2020 without issuing equity (notes, the revolver, the $1.0B point pre-sale;
FY2021 10-K). (2) *How they treat the owners*: read in the proxy, "how they treat themselves versus how they treat the
shareholders" **[M1994-009]**: the CEO's 2025 pay was $27.7M (salary $1.3M, stock $17.3M, options $5.8M, cash incentive
$3.0M; summary compensation table), against $1,457M of net income; the CEO owns about 55 years of that pay in stock.

**The integrity record.**
- *Searched*: Item 3 and Note 19 of the FY2025 10-K ("various claims and lawsuits arising in the ordinary course of
  business", including "antitrust claims, consumer protection claims"; none described as material); the FY2019, FY2022 and
  FY2025 10-Ks for "Department of Justice", "subpoena" and "investigation" (the only governmental matter found is an ADA
  settlement with the Department of Justice described in the 2013 IPO prospectus, a compliance matter); the 2013 IPO
  prospectus for "Starwood", "trade secret", "indict" and "grand jury". **No instance found** in these filings of fraud,
  restatement, an SEC action or a criminal matter involving the company or its officers.
- *Not verified, and not used*: I recall from outside the filings a 2009 lawsuit by Starwood alleging that executives it
  had lost to Hilton took confidential documents, settled in 2010, early in this chief executive's tenure. The IPO
  prospectus searched carries no mention of it, and I read no court record; it is recorded here as an open item for a
  later reader, not as a fact, and it is given no weight. A doubt resting on my memory alone is not evidence; a later run
  that reaches Q5 should read the docket.
- *The habits carried from Q4*: Adjusted EBITDA and adjusted EPS featured in every release, quarterly and annual guidance
  given, the annual pay target on Adjusted EBITDA met at "slightly above 100%" in 2025 (101% payout), the reimbursed-program
  gap excluded three years running. Read with the record above. The rows' alarm is a habit of hitting declared numbers:
  "we become downright incredulous if they consistently reach their declared targets" **[L2002-041]**, because forecasts
  push "really decent people" to "deliver certain numbers" **[M2015-033]**. What I have is one year's annual target met
  closely, PSU payouts of 117% (2023 grant) with the RevPAR-index leg at 60%, and a guidance practice; no restatement, no
  reserve movement, no accounting tell (Q4). That is a weight on the people, not a doubt about their honesty.
- *Reporting that tells the owner what he would want to know* **[M1998-036]**: the 10-K discloses the pre-sale with its
  amount and its unwinding, the reimbursement gap, the key money paid, and Adjusted EBITDA's limitations in plain words;
  the releases put GAAP figures first. Against it, the reports are standardised and do not discuss mistakes; "if it’s
  clearly the product of some investor relations department [...] that tells you something about the individual"
  **[M2007-083]**; no letter from the chief executive to owners was found among the filings, so the test of how they talk
  about mistakes **[L2024-003]** cannot be run from the record read.
- *Love of the business*: eighteen years in the job and a stake of about $1.5B held through trusts rather than sold; that
  is evidence of the owner's posture the rows ask about, read as the rows ask, from "some evidence of behavior in front of us" **[M1998-166]**, not proof of it.

- **VERDICT on integrity: IN** on the record read; no fact found that raises doubt about honesty, and the doubt rule
  **[M2013-088]** is applied to evidence, not to an unverified recollection, which is recorded above for a later reader.
  **Ability WEIGHS FOR** (the record against the hand dealt **[M1994-008]**), with the Q4 habits (guidance, adjusted
  figures) **WEIGHING AGAINST** the people **[L2019-006]**, **[M2015-033]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- **The retention test** **[M1994-061]**, **[R1995-009]**. Hilton keeps almost nothing. Over 2017 to 2025 it bought back
  $14,449M of stock and paid $1,164M of dividends (cash-flow statements), $15.6B against $8.8B of owner cash after interest
  and all spending; the rest was borrowed (debt from $6.6B to $12.4B; Q4). So the question is not whether a dollar kept
  became more than a dollar, since few were kept, but whether the dollars paid out and borrowed to buy stock were spent at
  a price below value. The forward question, "Can you keep using all of the capital you generate, effectively, for a very
  long time?" **[M2010-097]**, the company answers no in its own words: the pipeline needs "minimal capital investment from
  us" (Item 1), so the cash is returned. That is the right answer for a business that cannot use its earnings
  **[M2008-104]**; it puts the whole weight of Part A on the buyback price.
- **Buybacks** **[L1999-023]**, **[L2011-003]**. The programme names a dollar total, not a price: "allows for the
  repurchase of up to a total of $14.5 billion", raised by $3.5 billion in January 2026, "through open market purchases
  [...] including through Rule 10b5-1 trading plans", with "no expiration date" (10-K, Item 5); 2026 "Capital return is
  projected to be approximately $3.5 billion" (Q2 2026 release), a sum fixed in advance. "repurchase announcements almost
  never refer to a price above which repurchases will be eschewed" **[L2016-002]**; a buyback is advisable only when the
  stock sells "below its intrinsic value, conservatively-calculated" **[L1999-023]**. Prices paid: about $256 a share in
  2025 ($3.2B for 12.5M shares, excluding excise tax; Item 7), $272.40 in the fourth quarter of 2025 (Item 5), $314.62 in
  the first half of 2026 and $326.99 in the second quarter (Q2 2026 release). The buybacks were funded in part by new debt
  (notes of $1.0B each in March 2024, September 2024, July 2025, December 2025 and May 2026).
  **The buyback with no stated price, tested against the bottom of the Q7 range** (written back at Q7, committed with
  it): the bottom of the range is $56.50 a share all-equity ($82.56 equity-only) and the top $147.79; the prices paid,
  about $256 (2025), $272.40 (Q4 2025), $314.62 (H1 2026) and $326.99 (Q2 2026), sit not only above the bottom but
  above the top. The purchases are read by what they did **[L2013-012]**: shares bought at well over twice the top of a
  conservatively calculated value, much of it with borrowed money. "If you’re repurchasing shares above a rationally
  calculated intrinsic value, you are harming your shareholders" **[M1996-013]**. The no-stated-price buyback **weighs
  against** on its prices.
- **Issuance and deals** **[M1995-001]**, **[L2009-019]**. No deal paid in stock found in the filings read; the STOP for an
  all-stock deal in undervalued stock does not arise. The 2024 deals were cash and small: the Graduate brand for $210M and
  a controlling interest in the Sydell Group (NoMad), with put options to the minority from 2030 at "a multiple of the
  Sydell Group's earnings" (Note 3). Diluted shares fell from 327M (2017) to 238M (2025); stock pay is bought back rather
  than allowed to dilute, which the rows do not count as a reason to buy back: "dilution by itself is a negative and buying
  back your stock at too high a price is another negative. So it has to be related to valuation." **[M2016-049]**.
- **Dividends**: $0.60 a share a year, about $143M in 2025, small against the buybacks.

**Part B: the pay, the board and the owners.**
- **Pay tied to what the person controls** **[M2003-019]**. The annual cash incentive's "primary financial performance
  objective" for every named officer is annual Adjusted EBITDA (proxy), the measure Q4 found 66% above owner cash and
  leaving out stock pay, key-money amortization, FF&E reserves and the reimbursed-program gap; the long-term award is 50%
  PSUs on four equal legs (Adjusted EBITDA, free cash flow per share, net unit growth, RevPAR-index growth), 25% RSUs and
  25% options. For: net unit growth and RevPAR index are under management's control, and the free-cash-flow leg strips out
  "loyalty program advanced point sales" (proxy, PSU definitions). Against: a per-share cash measure rises with buybacks
  funded by borrowing, which the rows refuse in principle ("we evaluate acquisitions on an all-equity basis"
  **[L2017-004]**); the options carry no step-up for retained earnings **[L1994-021]**.
- **The board.** A non-executive chair separate from the chief executive, and a lead independent director (proxy); the
  rows warn of the chief executive "also Chairman" **[L2014-026]**, and that is not the case here. The chair is a
  Blackstone executive who has chaired since the 2007 buyout.
- **The owners as partners.** The chief executive's stake (4.66M shares) is large against his pay, and the proxy prohibits
  pledging and hedging; directors' holdings are mostly DSUs granted, not shares bought "with their savings" **[L2019-008]**.

- **Part A: WEIGHS AGAINST** (the price test, written back at Q7, confirms it): everything is paid out and more, through a
  fixed-sum buyback with no price named, partly on borrowed money **[L2016-002]**, **[L1999-023]**.
  **Part B: UNDECIDED**: the chief executive's large stake and a separate chair weigh for; a primary pay metric that leaves
  out real costs, a per-share metric rewarded by borrowed buybacks, and options without a step-up weigh against
  **[M2003-019]**, **[L1994-021]**; "any compensation sins are generally of minor importance compared to the sin of having
  somebody that’s mediocre running a huge company" **[M2007-006]**, and the manager is not mediocre (Q5).

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**; value is "the discounted value of the cash that can be taken out of a
business during its remaining life" **[R1996-018]**, with the business credited only "for whatever net cash is left
every year" **[M1998-080]**. The rate is the long Treasury, 5.56% **[M1996-025]**. All arithmetic is in
`scripts/calc.py` and `calc_out.txt`.

**The cash (Q4's recast).** Owner cash = operating cash − stock pay − property − capitalised software − finance-lease
principal − acquisitions (USD millions; filed cash-flow statements):

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| owner cash after interest (equity-only) | 983 | 493 | −203 | 1,375 | 1,490 | 1,365 | 1,729 |
| owner cash before interest (all-equity; interest paid × 0.79 added back) | 1,267 | 835 | 81 | 1,678 | 1,879 | 1,809 | 2,241 |
| of which customer advances (deferred revenue + loyalty liability) | 174 | 825 | −233 | 205 | 552 | 572 | 481 |

**CONVENTION of this run (after-tax interest):** interest paid is added back at (1 − 21%), the U.S. federal statutory rate;
rationale: the company's own tax is inside operating cash already, and the all-equity basis needs the interest after the
tax it saved; the filer's effective rate (about 29% in 2025) would add back less and lower every figure.

**The six specifics.**
- **(a) Cycle.** The literal five-year window is 2021 to 2025; its first year is aberrational on the filer's own account
  ("As a result of the COVID-19 pandemic, the operations of certain of our hotels were suspended", FY2022 10-K, Note 17;
  owner cash −$203M) **[L2005-003]**,
  **[L2003-004]**. The base is therefore the last full cycle **[M2011-101]**, **[M2011-102]**: **2019 to 2025**, the
  pre-pandemic peak to the latest year, which is above it. **CONVENTION of this run:** the cycle runs peak to latest year
  because the company in its present form exists only from the 2017 spin-offs, so no earlier trough or second peak of the
  same business is on file; rationale: the 2016 and earlier figures are a hotel owner and timeshare seller, not this
  business. The April 2020 point pre-sale ($1.0B in) and its use by mid-2022 both fall inside the cycle and net out in its
  average. **Base: $1,398M a year all-equity; $1,033M equity-only.** The literal window is shown beside: $1,537M and $1,151M.
- **(b) Growth, and (f) the cap.** The series changes sign (2021), so growth is measured between the halves of the cycle:
  2019 to 2021 averages $728M before interest, 2023 to 2025 average $1,976M, **28.4% a year**. Carried ten years it would
  put owner cash at several times its highest share of sales in the filings read (36.8% of revenue before reimbursements,
  2022), so by (f) it is cut to the business's own sales growth **[M1999-067]**. **CONVENTION of this run (which sales):**
  the top case uses the management and franchise segment's fee revenue, 2019 to 2025, **7.5% a year**, because that part
  decides (Q2) and the consolidated figure is pulled down by leases deliberately exited; the consolidated revenue before
  reimbursements, **4.7% a year**, is shown beside, and so is the consolidated sales growth between the same halves,
  15.9%, which carries the 2020 to 2021 trough. No rate above the discount rate is carried after year ten
  **[M1997-095]**: years eleven on are at zero growth.
- **(c) Acquisitions.** $240M over the cycle (Graduate, NoMad), deducted, total growth credited. Not a serial acquirer
  (purchases are about 3% of owner cash before purchases). No deal signed and unclosed; none closed after the window.
- **(d) Working capital** is counted as filed. The customer advances added $368M a year on average to the base; they
  grow with the system and the co-branded cards and would not grow in a business that has stopped growing. They are left
  in, which flatters the no-growth case; taking them out lowers every figure below.
- **(e) Maintenance.** The filing does not split maintenance from growth spending (Q3). The central case charges all
  spending; beside it, the case that treats every dollar of key money as growth (base $1,540M), an upper bound.
- **Net debt** at the latest filed date (10-Q, June 30, 2026): debt and finance leases at face $13,444M less cash
  $1,009M = **$12,435M**; restricted cash ($55M) and operating leases ($680M non-current liability) left out, said so; no
  subsequent event in the 10-Q changes it. Enterprise value at the price: $74,179M + $12,435M = $86,614M.

**The floor, tested first** **[M2003-149]**, **[M1994-004]**, **[L2002-020]**: the expected return at $329.59 on each case
(the rate at which the case's cash, ten years at its growth then flat, equals the price paid; all-equity against
enterprise value, equity-only against market value):

| case | value per share at 5.56% (all-equity) | expected return at the price (all-equity) | equity-only value / return |
|---|---|---|---|
| no growth | **$56.50** | 1.6% | $82.56 / 1.4% |
| consolidated sales growth, 4.7% | $106.83 | 2.5% | $119.74 / 2.1% |
| **fee growth of the deciding part, 7.5% (top)** | **$147.79** | 3.1% | $150.00 / 2.7% |
| beside: sales growth between halves, 15.9% | $337.91 | 5.7% | $290.46 / 5.0% |
| beside: key money as growth, 7.5% | $168.32 | 3.4% | |
| beside: literal window, 7.5% | $167.95 | 3.4% | |
| beside: 2025 alone (not the convention), 7.5% | | 4.8% | |
| forbidden by (f): the uncut 28.4% halves rate | $947.80 | 11.2% | $741.02 / 10.1% |

**No case the method allows earns the floor of about ten percent at the price.** The best allowed case returns about 5.7%,
the central top 3.1%, the no-growth case 1.6%, against a 5.56% Treasury. Only the 28.4% rate that (f) forbids, a rate
carried ten years from a pandemic trough, clears it. "there’s just a point at which we drop out of the game" **[M2003-149]**.

**Value range:** **$56.50 to $147.79 a share (all-equity, central) against $329.59**; equity-only $82.56 to $150.00;
literal window beside, $67.60 to $167.95. Width 2.6 to 1. The price is more than twice the top of the range; the market
price implies owner cash growing well above the 7.5% the fee base has shown, for ten years, or a rate below the Treasury.
"You can turn any investment into a bad deal by paying too much" **[M2019-015]**.

**Closes: OUT**, by the floor tested first (2026-10-10): no case in the range earns the floor at the price, and the price
sits above the top of the range, which closes OUT however the width reads **[M2003-149]**, **[M2009-005]**.

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent, averaged:
all-equity ends $6.89 (no growth) and $49.08 (7.5%), **fair price $27.98 a share (central, all-equity, after the
company's own tax)**; **equity-only $61.49** ($45.90 and $77.08). Beside them, with key money treated as growth, $36.40
all-equity. The all-equity figure sits below the equity-only one because at ten percent the no-growth business is worth
little more than its $12.4B of net debt. No cheap price is reported.

- **VERDICT: OUT.** Valued, and the price does not clear the floor on any case the method allows **[M2003-149]**; the
  castle is good (Q2) and the price is the problem, "it makes more sense [...] to buy a wonderful business at a fair price,
  than a fair business at a wonderful price" **[M2003-040]**, and this is neither at $329.59.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. One fact found is under AFTER THE STOP.

---
## THE BOX
**OUT at Q7** (the floor, tested first): Q1 IN, Q2 IN (management and franchise decides at 97% of five-year segment profit;
a network of owners, members and booking channels tested through a full cycle; operating return on net tangible assets at
the top of its field), Q3 WEIGHS FOR, Q4 no STOP and WEIGHS AGAINST (Adjusted EBITDA featured and guided), Q5 integrity IN
on the record read with the habits weighing against, Q6 Part A WEIGHS AGAINST (buybacks with no stated price at $256 to
$327, above the top of the range, partly borrowed), Part B UNDECIDED. **Value range $56.50 to $147.79 a share (all-equity,
central; equity-only $82.56 to $150.00) against $329.59** at the 5.56% Treasury; no case the method allows earns the floor
at the price (best 5.7%, central top 3.1%). Fair price $27.98 all-equity, $61.49 equity-only (reporting figures, not
verdicts). Integrity facts recorded, not judged: one unverified recollection (Q5), given no weight.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed, each with its source **[M1997-127]**; the box is unchanged (operator rule 2).
- **Q8.** The ten-year comparison is the 5.56% thirty-year Treasury (10/13/2026) against expected returns at the price of
  1.6% to 5.7% on the cases Q7 allows (`calc_out.txt`). "one opportunity cost of buying the stock is to compare it with a
  bond" **[M1997-089]**.
- **Q9.** Debt and finance leases $13,444M at face at June 30, 2026 (10-Q, Note 4), weighted average rate 5.03% (Q2 2026
  release); senior secured term loans $3,119M due 2030; maturities at December 31, 2025: $25M (2026), $619M (2027), $12M
  (2028), $1,360M (2029), $4,124M (2030), $6,319M after (10-K, Note 10), plus $1.0B of 5.500% notes due 2031 issued in May
  2026; the release says "no material indebtedness that matures until April 2029, other than $600 million of outstanding
  Senior Notes due April 2027". Revolver undrawn, $1,894M available, extended to about March 2031 with a first-lien net
  leverage grid (8-K 2026-03-18). Pre-tax earnings over interest **[L2012-002]**: 4.6x (2023), 4.1x (2024), 4.3x (2025).
  Debt guarantees and loan commitments to owners $61M, performance guarantees $22M (Note 19); $77M paid on debt guarantees
  in 2024. Guest loyalty liability $2,913M and deferred revenues $2,506M at December 31, 2025, obligations to reimburse
  hotels for redemptions and to deliver services already paid for. Operating lease liabilities $730M (non-current) and
  minimum operating lease payments of $156M in 2026 (Item 7). Equity is a deficit of $5.4B. The "little or no debt"
  criterion **[R1997-001]** is stated for whole businesses; this name carries net debt of about 5.5 times its 2025 owner cash
  before interest ($12.4B against $2.2B).
- **Q12.** "We also manage hotels with casino gaming operations as part of or adjacent to the hotels" and, where Hilton
  operates the casino, it holds the gaming license (10-K, Item 1, Government Regulation). The rows name casinos among the
  businesses refused to be owned and run **[M2007-018]**. No figure for the size of this activity was found in the filings
  read.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `b05b1215`); written question by question; committed after each
      (Step 0 to Q1 `f48fa9d4`, Q2 `85e0a844`, Q3 `99793c97`, Q4 `9d77fe32`, Q5 `7457a24b`, Q6 `fa2a425b`, Q7 with the Q6
      write-back `049c56d7`, this close in the next commit).
- [x] Dispatched to an analyst: the brief allowed per-question pathspec commits of the run file and research folder only,
      and states that the lock is held by the dispatching session; the fold into the register is the dispatcher's and is
      not done here. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared at
      the top: the subject line of another company's fold commit in the git log shown at session start, which quotes a
      Hilton return figure. Not used; this run's own figure (Q2) was computed from Hilton's filings. The repository's
      `.gitignore` was read for the research-folder rules; it names no company.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `scripts/check_citations.py`, result in `check_out.txt`); no E-ids; every filing fact has its accession in Step 0 or
      beside it; numbers are filed figures, sums of them, or CONVENTIONs named in the text.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; nothing after it is a clearance; Q8 to
      Q12 are NOT REACHED and their facts are under AFTER THE STOP.
- [x] Owner cash after every real cost from operating cash, never a net-income proxy (operator rule 5); stock pay, all
      capital spending, finance-lease principal and acquisitions deducted; the sovereign from the Treasury; the price an
      aggregator quote, flagged.
- [x] Contrary evidence written down as found **[M1997-127]** (the foundations' list; Q2 tests 3, 5, 6, 8; Q3's key money;
      Q4's balance sheet).
- [x] No point-in-time anchor applies; the run is dated today and cites rows as the ledger holds them.
- [x] Only the arithmetic lines of `tools/run.py` were used; its owner-earnings windows were not adopted (they leave out
      acquisitions and finance-lease principal and use three or five years where Q7's cycle rule governs).
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in `check_out.txt`).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q4 says two things about EBITDA.** Its "What it rules OUT" list names EBITDA as earnings and the managements that talk it, citing
the row that says the count of such purchases "is going to be about zero" **[M2002-026]**; the section A convention of
2026-10-06 records a featured adjusted figure at Q4 as a weighing and carries it to Q5. Hilton defines Adjusted EBITDA in
its 10-K, pays its officers on it and guides it quarterly; under the list it could close at Q4, under the convention it
weighs. I followed the convention, which is the later and more specific text, and say so; the list should say whether
"talk it" means using it as the measure or substituting it for earnings. (2) **Cycle rule (a) assumes successive cycles of
the same business.** A company re-formed by a spin-off in 2017 has one peak and one trough on file; the rule says
"peak to peak or trough to trough" and neither exists. I ran peak to latest year and confessed it. (3) **Rule (b) and cap
(f) together leave a choice of sales measure.** Growth between halves through a pandemic trough is 28.4%; (f) cuts it to
"the business's own sales growth over the same window (or between the same cycles)", which here is 4.7% end to end, 15.9%
between the halves (still carrying the trough), or 7.5% on the deciding part's fees. The text does not say consolidated or
deciding part, nor end points or halves. I took 7.5% as the top and showed the others; the box does not depend on the
choice (all fail the floor), but a closer case would. (4) **Customer advances inside operating cash.** Loyalty-program
deferred revenue added $368M a year to the cycle base; specific (d) counts working capital, but says nothing of float-like
advances that grow only while the system grows, and the framework's float treatment lives in the insurer method. The
company's own pay metric strips point pre-sales. I left them in (generous) and said so; a rule is wanted. (5) **The tax
rate on the interest added back for the all-equity basis** is not stated; I used the 21% federal statutory rate as a
CONVENTION of this run. (6) **Integrity on doubt alone, and the analyst's own memory.** Q5 applies "If you’ve got doubts,
forget it" **[M2013-088]** but does not say whether a doubt the analyst carries from outside the filings, unverified, counts;
I recorded it and gave it no weight, which a stricter reader could call the wrong side of the doubt rule. (7) **The template's
Q6 line** asks for the bottom of the Q7 range; here the prices paid were above the top as well, and the convention's words
("at or below the bottom") give no further grade; none was needed.
