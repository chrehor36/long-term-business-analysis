# Company Run: Jack Henry & Associates, Inc. (Nasdaq: JKHY), 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under the canonical brief `Screens/_daily/_dispatch_brief.md` (the brief's slots filled by the
dispatcher's message of 2026-10-07; departures: none stated). Analyst: Claude (dispatched session). Working folder
`Test Runs/_research 2026-10-07 JKHY/`; raw filings in its `cache/` subfolder, which is ignored and not committed.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared as found.** (1) The `git log` printed at session start showed the subjects of the last five
commits: the ESI and HAS runs closed OUT at Q5, the GFF run TOO HARD (WORK) at Q2 and the GRMN run TOO HARD (NATURE) at Q1,
with their Q7 computation figures. Those are other companies; nothing of them is used here. (2) The dispatcher's message
says there are earlier runs on Jack Henry; none was opened, listed or searched, and their contents and boxes are unknown
to this run. (3) The project memory index loaded at session start carries lines on the queue state (counts of
gate-clearers, "nothing buyable", holding reviews owed) that name no company; nothing in it names JKHY. Not used.
(4) A directory listing of `Screens/_daily/` (to check for the dispatcher's lock) showed only `_overnight.lock`.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $146.07 (2026-10-07, live quote printed by `tools/run.py`; an aggregator, flagged per operator rule 5;
  used for the market value only).
- **Shares by class** from the latest filing's cover: one class, common stock $0.01 par, **70,112,608** shares as of
  2026-08-12 (10-K for the fiscal year ended 2026-06-30, filed 2026-08-28, accession `0000779152-26-000067`;
  `python Screens/cover_shares.py JKHY`). Cross-check: the balance sheet in the same filing shows 104,597,621 issued less
  34,526,862 in treasury = 70,070,759 at 2026-06-30; the difference to the cover is 41,849 shares issued for stock plans
  between the two dates. No 8-K filed after the 10-K changes the count (the 8-K of 2026-08-24, `0000779152-26-000060`,
  is a director appointment). No 10-Q for the quarter to 2026-09-30 is filed yet, so buybacks after 2026-06-30 are not
  known; this is said, not estimated.
- **Market cap:** 70.1126M x $146.07 = **$10,241M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, the 30-year par yield of the US Treasury daily par yield
  curve for 10/06/2026, the issuing authority (`python tools/sources.py`).
- **Filings read** (operator rule 4): the 10-K for FY2026 (filed 2026-08-28, `0000779152-26-000067`), which is later than
  the last 10-Q (quarter to 2026-03-31, filed 2026-05-07, `0000779152-26-000025`); the 10-Ks for FY2016 to FY2025
  (`0000779152-16-000142`, `-17-000040`, `-18-000060`, `-19-000048`, `-20-000064`, `-21-000073`, `-22-000076`,
  `-23-000062`, `-24-000079`, `-25-000055`); the proxy, DEF 14A filed 2026-10-02 (`0000779152-26-000088`); the 8-Ks of
  2026-03-26 (new $1.0 billion revolver, `0000779152-26-000013`), 2026-05-12 (5 million shares added to the buyback
  authority, `0000779152-26-000027`), 2026-06-04 (the chair, a former CEO, retires from the board, `0000779152-26-000036`),
  2026-08-11 (deconversion revenue for FY2026, `0000779152-26-000052`), 2026-08-18 (the FY2026 earnings release with FY2027
  guidance, `0000779152-26-000057`) and 2026-08-24 (`0000779152-26-000060`).
  **One figure cross-checked against the filed statement:** net cash from operating activities FY2026, $761,960 thousand
  on the filed cash-flow statement (10-K `0000779152-26-000067`), against $762.0M printed by `tools/run.py`. Agrees.
- `python tools/run.py JKHY` arithmetic lines only (its other output is not read, Part VII): operating cash FY2024 to
  FY2026 $568.0M, $641.5M, $762.0M; stock pay $28.9M, $28.4M, $32.5M; capital spending as the tool sums it (property and
  equipment plus software developed) $225.3M, $225.8M, $251.3M, with purchased software ($7.1M, $5.4M, $4.1M) printed as
  an alternate not in its capex; depreciation $46.3M, $43.7M, $42.1M. The tool's "D&A" column is depreciation only, and
  amortization (FY2026 $171.1M, of which computer software $154.2M) is not in it; it is not used. Owner cash is built in
  Q4 from the filed statements, not from the tool's three-year mean.
- **A fact that bears on every cash figure below, found at Step 0 and written down at once** **[M1997-127]**: FY2026
  operating cash is lifted by a tax timing item. The filer says operating cash rose 18.8% "primarily due to the change in
  deferred income taxes" (10-K FY2026, MD&A, `0000779152-26-000067`); the change in deferred income taxes was +$126.0M
  against -$3.5M and -$0.9M in the two years before; cash taxes paid were $38.9M in FY2026 against $117.6M and $107.0M
  (Note 8), after the July 2025 law restored immediate expensing of domestic research costs and let the unamortized
  balance capitalized since 2022 be deducted. FY2023 carried the opposite (deferred taxes -$48.2M as tagged in the
  filings' XBRL, sign reversed to the statement's). Q4 and Q7 treat it.

## THE FOUNDATIONS (not a gate)
*(Resumed 2026-10-10 after the session was stopped by a usage limit on 2026-10-07 during Step 0. The run keeps its date;
the price is not refreshed: every figure below is taken against the Step 0 price of $146.07 of 2026-10-07, so the run
reads as of that day. Nothing in the folder was refetched.)*

The foundation that bears hardest is the first: a share is a business, and the test is whether one would be content to own
this "if the market closed for five years" **[M1997-109]**. A bank-processing business paid monthly under six-year
contracts passes the form of that test easily; whether it passes the substance is Q2's work. The margin-of-safety foundation
is carried to Q7, where a case that needs "pencil and paper" is "too close to think about" **[M1996-084]**. Who is paid to
tell you: the company publishes annual guidance and a non-GAAP figure (the earnings release of 2026-08-18,
`0000779152-26-000057`), so its own forward numbers are not used as inputs here **[M2020-037]**. No macro view enters.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the operating-cash jump of FY2026 is mostly a tax timing
item (Step 0); (2) the filer's own risk factors say "Certain of our renewals have resulted in price compression between the
former and renegotiated contracts" (10-K FY2026, Item 1A, `0000779152-26-000067`; the phrase "price compression" is in the
FY2016, FY2017 and FY2025 10-Ks and absent from FY2018 to FY2024); (3) the filer calls its markets "characterized by
changing client and regulatory requirements and rapid technological changes" (same Item 1A); (4) the number of US banks and
credit unions each fell at about 3% a year from 2020 to 2025 (Item 1, FDIC and ACU figures), and the filer's own core bank
count fell from about 1,080 (10-K FY2017, `0000779152-17-000040`) to "over 900" (FY2026); (5) the company is building a
public cloud-native platform it describes as "a fully functional modern alternative for existing core functions" (Item 1,
FY2026), so its own cores are to be replaced by its own new product. Each is weighed where it belongs.

## THE STANDING RULE
A part-interest in a listed company, bought for cash and held unlevered, cannot by itself put the buyer at risk of ruin; the
rule binds the financing and the size of the purchase, not the target **[M2012-081]**; borrowed money to buy it is ruled out
**[L2014-005]**. Nothing here requires it. Passes, as conduct, on the buyer's side.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**What the business is, from the filing.** Jack Henry sells the system of record (deposits, loans, general ledger) to
community and regional banks (three platforms, "over 900" banks up to $55 billion of assets) and credit unions (one
platform, Symitar, "over 700"), plus complementary products and payment processing sold both to its own core clients and
to about 5,600 non-core clients (10-K FY2026, Item 1, `0000779152-26-000067`). Hosted (private and public cloud) clients
are "typically on a six-year contract" with "per account" fees and "minimum guaranteed payments"; on-premise clients pay
annual support "approximately 20% of the respective product's software license fee", and those fees "generally increase as
client assets increase" (Item 1). Revenue by type FY2026: private and public cloud $816.1M, on-premise support $336.8M,
product delivery and services $295.1M, processing $1,096.3M (Note 2). Remaining performance obligations: $8.44 billion at
2026-06-30 against $4.64 billion at 2021-06-30 (Note 2 of each, `0000779152-26-000067`, `0000779152-21-000073`), about
3.3 years of FY2026 revenue. International revenue under 1%.

**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" **[M2012-065]**; the product can stay opaque if "I understand the economic dynamics of the industry"
**[M2011-014]**. The key variables and how predictable they are **[M1998-044]**:
1. *The number of client institutions.* Banks in the filer's asset range fell from about 5,630 (10-K FY2018,
   `0000779152-18-000060`) to about 4,300 (FY2026); credit unions to about 4,400. The decline has run at about 3% a year and
   is driven by mergers. It is a slow, visible variable, and the filer is paid a deconversion fee when an acquired client
   leaves (Note 2; $42.8M in FY2026). Predictable in direction and rough rate.
2. *Jack Henry's share of those institutions.* About 1,000 core banks against 5,131 in range (10-K FY2020,
   `0000779152-20-000064`), 19.5%; "over 900" against about 4,300 (FY2026), about 21%. SilverLake, the platform for the
   larger banks, went from "over 390" banks (FY2017) to "over 500" (FY2026). Symitar from "over 640" credit unions (FY2016,
   `0000779152-16-000142`) to "over 700" (FY2026); a second credit-union platform of about 160 clients in FY2016 is no
   longer listed. Share held or rising over ten years.
3. *Revenue per client.* Rises with client assets (average core bank client assets $1.29 billion to $1.42 billion in a
   year, Item 1) and with products sold into the base. Total revenue rose in every fiscal year from FY2009 ($745.6M) to
   FY2026 ($2,544.3M) in the filed XBRL series (SEC companyfacts, transcription), through 2008 to 2010, the 2020 shutdown
   and the 2023 regional-bank failures.
4. *Margins.* GAAP operating margin between 22.1% and 26.7% in every year FY2012 to FY2026 (same series).
5. *Technology.* The filer calls its markets fast-changing and is rebuilding its core functions on a public cloud platform.

Do the past statements tell me the future ones **[M2008-033]**? For variables 1 to 4, yes over the span read: the records
of FY2016 to FY2026 are of a piece, and the forecast they support is about the conduct of conservative customers (how fast
banks merge, whether they leave a vendor at renewal), the kind of forecast the rows treat as a customer question rather
than a technology question **[M2017-019]**, **[M2023-030]**. Variable 5 is the one the filter is built to catch: "if
something comes in where there's a technological component that's of significance, or where we think the future
technology could hurt the business as it presently exists [...] it won't make it through the filter" **[M1998-008]**.

**Where variable 5 is placed.** The framework routes it: a business "whose ten-year economics cannot be foreseen because its
industry changes fast" closes here TOO HARD; a castle whose future cannot be judged closes at Q2. My reading of the filings
is that the industry does not change fast in the sense of **[L1993-023]**: the vendors named as Jack Henry's core
competitors in FY2026 (FIS, Fiserv, Finastra and the private Corelation) were the field across the decade read; cores are
replaced on a generation scale (SilverLake and Symitar are decades old and still winning clients: "a record 58 competitive
core wins" in FY2026, earnings release `0000779152-26-000057`; "51 new core wins" in FY2025, `0000779152-25-000053`); and
the move to the company's private cloud has been a move of the same clients onto the same software (cloud revenue $361.9M
in FY2017 to $816.1M in FY2026; on-premise support $307.1M to $336.8M; 10-Ks `0000779152-19-000048` and
`0000779152-26-000067`). The change is slow change, which "can be much harder to perceive" **[M2014-038]**, and it bears on
whether the castle lasts, which is Q2's question (its test 11), not on whether the economics can be pictured at all. The
insiders write the near part of the forecast down in contracts: six-year terms with minimum payments and $8.44 billion of
contracted future revenue **[M2000-105]**. Can I name the winner and not just the industry **[M2012-067]**? The question
is narrower here: will the incumbent holding about a fifth of the community-bank cores keep them; that is answerable from
the filings and is answered at Q2. How far off could I be **[M2011-084]**: narrow on volume and revenue per client, wide
only on the platform question.

**Doubt test** **[M2002-092]**. My doubt is about the castle's durability through a platform change, not about what the
business is or how it earns. Recorded, and carried to Q2.

- **VERDICT: IN.** The economics (client count, share, revenue per client, margins) are foreseeable ten years out on the
  filed record **[M2012-065]**, **[M1998-044]**; the technology threat is real and slow, and is judged as a castle question
  at Q2 **[M2014-038]**, not as an industry that cannot be foreseen **[L1993-023]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what's going to keep it standing or cause it not to be standing five,
10, 20 years from now" **[M1995-038]**; a moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table** (business of parts, CONVENTION of the framework, Q2). Segment income is revenue less cost of revenue;
research, selling and general costs and the Corporate Services loss are not allocated (Note 14). FY2022 and FY2023 from the
FY2023 10-K (`0000779152-23-000062`), FY2024 to FY2026 from the FY2026 10-K (`0000779152-26-000067`, with the filer's
reclassifications between segments); the two vintages differ by small product moves the notes describe.

| Part | Five-year segment income FY2022-26 | Share of the three | Segment margin FY2018 / FY2022 / FY2026 | Revenue growth FY2018-26 a year | Castle | Decides |
|---|---|---|---|---|---|---|
| Core | $2,034.7M | 34.5% | 54.3% / 58.0% / 60.3% | 5.3% | the system of record, six-year contracts, conversion cost | yes, the largest part (none exceeds half) |
| Complementary | $1,933.9M | 32.8% | 58.5% / 58.4% / 61.9% | 8.4% | sold mostly into the core base, integrated with it | no (read below) |
| Payments | $1,922.0M | 32.6% | 51.8% / 46.3% / 48.8% | 7.9% | card, bill pay, ACH and instant payments; sold also to non-core clients | no (read below) |
| Corporate Services | loss each year (FY2026 -$274.8M) | n/a | n/a | n/a | shared costs | n/a |

The three parts are near equal, so the threshold makes Core decide by about two points. The framework's rule is applied as
written; Complementary and Payments are read as well, because they are largely sold through the same client relationships
**[L2008-005]**.

**The castle tests, each with its filing fact.**
1. *Key factors and how permanent* **[M1995-038]**. The core is the bank's system of record. Hosted clients sign six-year
   contracts with minimum payments (Item 1); the company is the client's "single point of contact" for the core and the
   products integrated with it; its hosted services are examined by the federal banking regulators under the Bank Service
   Company Act (Item 1). Early termination "most commonly occurs due to the acquisition of one of our clients by another
   financial institution" and carries a deconversion fee (Note 2). Deconversion revenue by year (MD&A of each 10-K): FY2017
   $39.5M, FY2018 $46.2M, FY2019 $30.2M, FY2020 $53.9M, FY2021 $20.6M, FY2022 $53.3M, FY2023 $31.8M, FY2024 $16.6M, FY2025
   $33.9M, FY2026 $42.8M: clients leave mainly when they cease to exist, and they pay to leave. These factors have held
   across the decade read and do not depend on one person.
2. *Without the lord.* Two chief executives in the decade read (David Foss signed the FY2016 10-K as CEO; the 8-K of
   2026-06-04, `0000779152-26-000036`, records him as CEO from 2016 to 2024 and retiring as chair; Greg Adelson since);
   operating margin stayed in a 22% to 27% band throughout, before, during and after the change. The business
   does not need a superstar **[M1995-040]**.
3. *The money test* **[M2011-015]**. The attackers with money are on the public record and their own filings show what the
   attack has cost them. Alkami (digital banking, IPO 2021): GAAP operating margin -57.8% (2019) to -12.1% (2025), negative
   every year (10-K FY2025, `0001529274-26-000009`; companyfacts). nCino (loan origination and onboarding for banks): -20.4%
   (FY ended Jan 2020) to +0.6% (FY ended Jan 2026), first positive year the last (10-K `0001902733-26-000022`). Q2 Holdings
   (digital banking): negative every year 2012 to 2024, +5.0% in 2025 (10-K `0001410384-26-000006`). None of the three sells
   a core; each sells a layer that sits on a core, and Q2's own list of digital-banking competitors does not name Jack Henry
   (Item 1, same 10-K). The cloud-native core entrants (Thought Machine, Mambu, 10x and others) and Temenos are not SEC
   filers and are flagged, not compared; Finxact, the US cloud-native core, was bought by Fiserv in 2022. No entrant in the
   filings read has taken community-bank cores at scale in ten years, while Jack Henry reports record competitive core wins
   (58 in FY2026, 51 in FY2025). Why are there no new entrants into a field this profitable **[M2000-077]**? The filings
   answer: the cost of conversion to the client and the decade of losses to the entrant.
4. *Pricing power and the agony* **[M2005-020]**. On-premise support fees "generally increase as client assets increase"
   (Item 1). Through the 2021 to 2023 inflation the Core segment margin went 56.2% (FY2021), 58.0%, 56.8%, 58.4% (FY2024)
   and 60.3% (FY2026); Complementary 57.7% to 61.9%. Against: Payments fell from 51.8% (FY2018) to 44.8% (FY2023) before
   recovering to 48.8%, and the filer says "Certain of our renewals have resulted in price compression" (Item 1A, FY2025 and
   FY2026). The price behaviour shows a business that holds its margin through inflation but bargains at renewal; not a
   business that prices without agony.
5. *Unit volume.* Core clients fell (about 1,080 banks FY2017 to over 900 FY2026) while the bank count in range fell faster
   (5,630 to 4,300), so share rose; revenue per client rose with client assets.
6. *Low-cost position.* Not claimed by the filer and not shown; not relied on.
8. *Would the customer choose it over the low bid* **[M2017-009]**. A bank changes its core rarely and at large cost; the
   evidence is that terminations come from mergers, not from price shopping (Note 2), and the contracts run six years with
   minimums. This is the Precision Castparts form, contracts "that extend over many years" where customers do not "simply
   just take the low bid" **[M2016-006]**.
9. *Ask the competitors* (from their own filings, the whole span; see the competitor row). The two large rivals' bank-core
   lines grew more slowly than Jack Henry's Core segment over the span read.
10. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Share of banks in range up from about 19.5% (FY2020) to about
   21% (FY2026); SilverLake moving up-market (390 to 500 banks, client assets to $55 billion); Core and Complementary margins
   up; Payments narrowed and partly recovered. On balance standing or widening slightly.
11. *What could destroy, modify or reduce it* **[M2000-014]**. (a) Consolidation: slow, priced by deconversion fees, but
   each lost client is lost recurring revenue; the acquirer of a Jack Henry client may run another vendor's core. (b) The
   platform change: the company is rebuilding core functions as a public cloud-native platform; if the rebuild fails or a
   rival's cloud core wins the conversions of the next generation, the castle is crossed slowly. (c) The community bank
   itself losing deposits and relevance to large banks and fintechs, which would shrink the client base faster than 3% a
   year. (d) A security or outage event at a hosted processor examined by the bank regulators. None is shown to be under way
   in the filings read; (b) is the one the rows warn of, "A moat that must be continuously rebuilt will eventually be no moat
   at all" **[L2007-005]**.

**Maintained or rebuilt?** Research and development expense plus capitalized software development was $177.6M, 13.1% of
revenue, in FY2016 ($81.2M + $96.4M) and $360.7M, 14.2%, in FY2026 ($176.4M + $184.2M) (10-Ks `0000779152-16-000142`,
`0000779152-26-000067`). The share has been steady for a decade and the margin with it, which reads as a standing cost of
keeping the castle, not an accelerating cost of rebuilding it. The rows give no test beyond this, and the judgement is mine.

**The competitor row** (same metrics from each company's own filings; transcription from SEC companyfacts and the segment
notes named; the segment margins are as each filer defines its segment and are not comparable across filers, so the common
metrics are revenue growth of the bank-technology line and company GAAP operating margin).

| Company (accession) | Bank-technology line and its growth over the span read | Segment margin as filed | Company GAAP operating margin |
|---|---|---|---|
| Jack Henry (`0000779152-26-000067`, `-23-000062`) | Core segment $509.8M FY2018 to $768.5M FY2026, 5.3% a year; whole company 6.5% a year FY2016-26 | Core segment 54.3% to 60.3% (before R&D and SG&A) | 22.1% to 26.7% every year FY2012-26 |
| Fiserv (FISV; `0000798354-17-000006`, `-23-000004`, `-26-000009`) | Financial segment revenue +1% in 2016, +3% in 2015; Fintech segment $2,901M (2020) to $3,170M (2022); Banking line $2,435M (2023), $2,496M (2024), $2,435M (2025), flat | Financial 32.6% to 33.8% (2014-16); Fintech 34.2% to 36.5% (2020-22); Financial Solutions 45.9%, 47.3%, 45.3% (2023-25, after allocations) | 26.2% (2016); 12.5% to 15.8% (2019-21, after First Data); 27.5% (2025) |
| FIS (`0001136893-20-000032`, `-26-000013`) | Banking Solutions $5,552M (2017) to $5,873M (2019) to $7,285M (2025), about 3.5% a year with acquisitions and recasts | adjusted EBITDA margin 37.8% (2017) to 43.4% (2025), an EBITDA measure | 14.7% (2016) to 16.3% (2025), -111% in 2022 on a $17.6 billion goodwill impairment |
| Alkami (`0001529274-26-000009`) | digital banking, not core; revenue $74M (2019) to $444M (2025) | n/a | negative every year, -57.8% to -12.1% |
| nCino (`0001902733-26-000022`) | lending and onboarding, not core; $138M to $595M | n/a | negative every year to FY Jan-2025, +0.6% in FY Jan-2026 |
| Q2 Holdings (`0001410384-26-000006`) | digital banking, not core; $41M (2012) to $795M (2025) | n/a | negative 2012-2024, +5.0% in 2025 |
| Temenos, Finastra, Corelation, Thought Machine, Mambu | flagged: not SEC filers, not compared | | |

**The field's returns over the last full cycle, judged in words** (section C). Jack Henry's after-tax operating income
against equity plus debt less cash: about 27% in FY2017 ($367.7M at the 33% effective rate against $917M), about 23% in
FY2021 ($398.7M at 21.7% against $1,368M), about 24% in FY2026 ($635.0M at 23.0% against $2,080M); on that capital less
goodwill and acquired intangibles, about 41% in FY2026. These are excellent returns, held through 2020 and 2023. The two
large rivals' company returns are buried under acquisition goodwill (FIS wrote off $17.6 billion in 2022), so their filings
show the cost of buying into the field, not ordinary returns on its castles; their bank-technology segment margins are high
and steady. The entrants show the cost of attacking it. The field is not one of standing castles protecting ordinary
returns; the OUT of section C does not apply **[L2007-004]**.

**Complementary and Payments, read for the record.** Complementary's castle is the core's (integration, single point of
contact), plus core-agnostic products sold to some 5,600 non-core clients; its margin rose. Payments competes with card
processors and bill-pay and instant-payment providers that are not bound to the core; its margin fell seven points over five
years and recovered four; it stands, but it is the narrowest of the three. Neither is open on the evidence.

**What the castle does not have.** The customer does not ask for Jack Henry by name the way a consumer asks for a brand; the
moat is switching cost and trust with regulated institutions, which "one competitor is frequently enough to ruin" only if
that competitor makes switching cheap **[M2012-108]**. The cloud-native core is the attempt to make it cheap. It has not
succeeded in the filings read; it is the thing to watch.

- **VERDICT: IN.** The deciding part, Core, has a castle that has held for the decade read: share of a shrinking field up,
  margins up, terminations mainly by merger and paid for, entrants losing money and rivals' core lines growing more slowly
  **[M1995-038]**, **[M2011-015]**, **[M2016-006]**. Its threat is a slow platform change that the company is meeting with a
  steady, not rising, share of revenue spent on development **[L2007-005]**, **[M2000-014]**. The returns it protects are
  excellent, not ordinary **[L2007-004]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
The measure is the capital "actually needed in the business" **[M2010-090]**, read as "return on tangible assets", with
goodwill forgotten for the business and counted for the allocation **[M2011-060]**.

- **Return on the capital needed.** After-tax operating income (operating income at the year's effective tax rate) against
  equity plus debt less cash, less goodwill and acquired intangibles (customer relationships, other intangibles), all from
  the filed balance sheets: FY2021 $312.2M on $573M (54%) (10-K `0000779152-21-000073`: equity $1,319.3M, debt $100.1M, cash
  $51.0M, goodwill $687.5M, intangibles $108.0M); FY2026 $489.0M (at the 23.0% effective rate) on $1,192M (41%) (10-K `0000779152-26-000067`). With
  goodwill counted, about 23% to 24% in both years (Q2). The capitalized software ($656.3M net) and the capitalized contract
  costs and client incentives (below) are kept in the capital, because they are cash already spent to earn the revenue.
- **Capital needed per dollar of revenue is rising.** The same tangible capital was about 33% of revenue in FY2021 and about
  47% in FY2026. The causes are on the face of the filings: capitalized contract costs (commissions and conversion work)
  $314.8M (FY2021, Note 2) to $599.5M (FY2026: $301.5M to obtain, $298.0M to fulfil); contract assets, chiefly upfront
  incentive payments or credits to clients, $75.8M (FY2021) to $178.5M (FY2026); computer software net $368.1M to $656.3M.
  The incremental return, FY2021 to FY2026, is the added after-tax operating income ($176.8M) on the added tangible capital
  ($619M): about 29%. Rising earnings bought with rising capital is the thing the rows say to read twice **[M2023-081]**;
  here the added capital still earns well above the rate.
- **Reinvestment to stand still and to grow** **[M2000-144]**, **[L1999-024]**. The filer gives no split between maintenance
  and growth spending. FY2026 capital spending: property and equipment $67.1M, software developed $184.2M, software
  purchased $4.1M, together $255.5M, against depreciation $42.1M and software amortization $154.2M ($196.3M); the excess,
  about $59M, plus the yearly growth in contract costs and incentives (the cash-flow line "prepaid expenses, deferred costs
  and other": -$57.1M FY2021, -$82.6M, -$112.3M, -$115.6M, -$50.9M, -$85.5M FY2026), is what growth costs. Revenue grew 7.7%
  a year FY2021 to FY2026 on that spending; whether the excess is "good or bad depends on what we earn on that incremental
  $130 million over time" **[M2001-019]**, and on the filed figures it earns about 29%.
- **The growth arithmetic and its caps.** Revenue growth of 6% to 9% a year (organic, as the filer reports it: 9%, 8%, 7.4%,
  6.5%, 7.3% for FY2022 to FY2026, MD&A of each 10-K) against a client base that shrinks about 3% a year means revenue per
  client must rise about 10% a year to hold that rate; it has, through prices tied to client assets and through cross-sales.
  This is the second-best business of the 1998 ranking, the one that "takes more money, but the rate at which you invest
  [...] the money to get that growth is a very satisfactory rate" **[M1998-081]**, not the first.
- **WEIGHS FOR.** High returns on the capital actually needed and about 29% on the capital added **[M2010-090]**,
  **[M2011-060]**, **[M2001-019]**; carried against it, a capital need per dollar of revenue that has risen by half in five
  years **[M2023-081]**. (The "little or no debt" criterion is applied at Q9.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
**The balance sheets first, ten of them** **[M2025-032]** (`tools/run.py` table, first-filed XBRL vintage, transcription; the
filed statements of FY2017, FY2021 and FY2026 read behind it, accessions in Step 0). USD millions, June year-ends.

| FY | Assets | Liabilities | Equity | Cash | Receivables | Goodwill | Debt | Retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2017 | 1,909 | 877 | 1,032 | 115 | 277 | 552 | 0 | 1,585 |
| 2018 | 2,050 | 783 | 1,267 | 31 | 292 | 650 | 0 | 1,857 |
| 2019 | 2,185 | 756 | 1,429 | 94 | 310 | 667 | 0 | 2,066 |
| 2020 | 2,428 | 879 | 1,550 | 213 | 301 | 686 | 0 | 2,235 |
| 2021 | 2,336 | 1,017 | 1,319 | 51 | 307 | 687 | 100 | 2,412 |
| 2022 | 2,456 | 1,074 | 1,382 | 49 | 348 | 687 | 115 | 2,636 |
| 2023 | 2,774 | 1,165 | 1,609 | 12 | 361 | 805 | 275 | 2,856 |
| 2024 | 2,924 | 1,082 | 1,842 | 38 | 333 | 805 | 60 (plus 90 current) | 3,082 |
| 2025 | 3,044 | 913 | 2,131 | 102 | 318 | 805 | 0 | 3,373 |
| 2026 | 3,146 | 1,094 | 2,052 | 12 | 349 | 828 | 40 | 3,705 |

What moved and why. *Equity against goodwill*: goodwill rose $276M in ten years, in four steps that match the acquisitions
(Ensenta FY2018, $137.6M paid; Geezeo FY2020, $30.4M; Payrailz FY2023, $229.6M; Victor FY2026, $42.4M, goodwill $22.9M),
no impairment in the span; equity rose less than retained earnings because $2.34 billion of shares were bought into treasury
(Q6). *Cash* is kept near zero and the revolver used as the till (borrowings and repayments of $350M to $600M a year). *Debt*
peaked at $275M after Payrailz and is $40M. *Receivables against sales*: 19.4% (FY2017), 17.4% (FY2021), 13.7% (FY2026),
falling, which is the right direction. *Retained earnings* rose every year. *Deferred tax liability*: $261M (FY2021), $240M
(FY2025), $366M (FY2026), the R&D expensing of Step 0. *The accounts that build*: prepaid expenses and other $66.9M (FY2017)
to $193.5M (FY2026); non-current deferred costs $96.8M to $226.9M; other non-current assets $82.5M to $504.9M. Part of the
step is the revenue standard adopted in FY2019, which brought capitalized commissions and contract assets onto the balance
sheet; from FY2021 to FY2026, on a like basis, contract assets (mostly upfront client incentives) went from $75.8M to
$178.5M, 4.3% to 7.0% of revenue, and capitalized contract costs from $314.8M to $599.5M. "if some prepaid expense, deferred
asset accounts start building up suspiciously high [...] you want to look twice" **[M1995-064]**. Looked at twice: each is
named and measured in the notes, amortized against revenue ($195.7M of contract-cost amortization in FY2026, no impairments),
and every dollar of it passed through operating cash when spent, so owner cash below bears it in full. What it says is not
that the accounts mislead but that winning and keeping clients costs more up front each year: incentives growing faster than
revenue are a price paid for the contract, the same fact as the "price compression" the filer admits (Q2). What the figures
do not say: the split of capital spending between maintenance and growth, and revenue or margin by client cohort.

**The real costs.**
- *Depreciation* $42.1M against property spending $67.1M in FY2026; depreciation is a real cost **[R1996-023]**.
- *Software amortization* $154.2M against $188.4M of software developed and purchased; "With software, for example,
  amortization charges are very real expenses" **[L2012-003]**. Owner cash deducts the cash spent, not the amortization.
  Amortization of customer relationships and other acquired intangibles ($17M in FY2026) is the purchase-accounting kind.
- *Stock pay* $32.5M (1.3% of revenue), deducted; "Stock-based compensation" is "the most egregious example" of a real cost
  waved away **[L2015-003]**. The company's non-GAAP figures do not add it back (earnings release `0000779152-26-000057`,
  reconciliation tables: the adjustments are deconversions, acquisition costs, a contract change and an asset gain).
- *The recurring "one-time"*: deconversion revenue in every year of the decade ($16.6M to $53.9M) is excluded from the
  non-GAAP figures; excluding a revenue lowers the adjusted figure, so it does not flatter; the voluntary early departure
  programme cost $16.4M in FY2024. Small.
- *EBITDA in the filer's own mouth* **[M1998-086]**, **[M2003-108]**: the FY2026 earnings release carries a table
  "reconciling net income to non-GAAP EBITDA" (`0000779152-26-000057`). The 10-K does not feature it.
- *The make-the-numbers habit, guidance and a featured adjusted figure*: the earnings release leads with "Non-GAAP adjusted
  revenue" and "non-GAAP adjusted operating income" and gives full-year FY2027 guidance; the company files a separate 8-K
  each quarter announcing deconversion revenue, explained by reference to "how guidance is developed" (8-K of 2026-08-11,
  `0000779152-26-000052`). Recorded here as a WEIGHING against **[M1994-018]** and carried to Q5 **[L2019-006]**,
  **[L2016-006]**.

**Owner cash after every real cost** (operator rule 5; never net income), from the filed cash-flow statements of the 10-Ks
for FY2023 (`0000779152-23-000062`) and FY2026 (`0000779152-26-000067`); computed in `owner_cash.py` in the working folder.
Operating cash less stock pay, property and equipment, software developed and software purchased:

| FY | Operating cash | Owner cash, equity-only | Owner cash, all-equity (after-tax interest expense added back at 78%, a CONVENTION of this run: one minus an effective rate of about 22%) | Change in deferred taxes in operating cash | All-equity at the book tax charge (timing removed) | Acquisitions paid |
|---|---|---|---|---|---|---|
| 2022 | 504.6 | 288.5 | 290.3 | +31.9 | 258.4 | 0 |
| 2023 | 381.6 | 146.0 | 157.7 | -48.2 | 205.9 | 229.6 |
| 2024 | 568.0 | 306.7 | 319.5 | -0.9 | 320.4 | 0 |
| 2025 | 641.5 | 381.9 | 390.1 | -3.5 | 393.6 | 0 |
| 2026 | 762.0 | 474.0 | 478.2 | +126.0 | 352.2 | 42.4 |
| Average | 571.5 | 319.4 | 327.2 | +21.1 | 306.1 | 54.4 |

The tax timing: under the 2017 law, domestic research costs were capitalized for tax from FY2023, raising cash taxes in
FY2023 to FY2025; the July 2025 law restored expensing and let the unamortized balance be deducted, so FY2026 cash tax fell
to $38.9M (Note 8). Over the five-year window the deferred-tax line sums to +$105.3M, about $21M a year, which is close to
the deferral the company ran before 2022 by expensing software development for tax while capitalizing it for books (the
same line was between +$7.6M and +$37.5M in every year FY2012 to FY2022 except FY2018, when the 2017 law remeasured the
balance, as tagged in the filings' XBRL). So the five-year average as filed is
a fair base, while the end years are not: FY2026 is aberrational on the filer's own description and FY2022 to FY2026
end-to-end growth on the as-filed series (13.3% a year) is the "breathtaking, but meaningless" kind **[L2005-003]**. The
growth used at Q7 is measured on the series at the book tax charge: 8.05% a year end to end.

The interest income line ($23.1M in FY2026) is left in operating cash: the filer earns it on "balances" in the course of its
payments business, not on a cash hoard (year-end cash is $12.1M). Said, not adjusted.

- **VERDICT on the accounts: WEIGHS FOR, with three items against.** The statements are clear, the costs that are real are
  carried, stock pay is not added back, and no figure confuses **[M1995-063]**, **[M1995-065]**. Against: the building
  contract assets read twice and found to be a growing price of winning clients, not a reserve game **[M1995-064]**; EBITDA
  in the release **[M1998-086]**; guidance and a featured adjusted figure, carried to Q5 **[L2019-006]**, **[L2016-006]**.
  The recast owner cash (all-equity five-year average $327.2M; $272.8M after acquisitions) feeds Q7.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
The two yardsticks: "how well they run the business", read against "the hand they were dealt", and "how well that they treat
their owners" **[M1994-008]**. For a marketable stock the speakers read rather than meet **[M2007-081]**.

**The record against the hand dealt.** Same industry, same decade, same shrinking customer base as Fiserv's and FIS's
bank-technology lines (Q2): Jack Henry's revenue rose in every year, its operating margin held in a 22% to 27% band, its
share of community-bank cores rose, and it did not make the large acquisitions that cost FIS a $17.6 billion goodwill
write-off. Under two chief executives (Foss 2016 to 2024, Adelson since). Ability **WEIGHS FOR** **[M1994-008]**.

**The integrity record, from the filings.** No restatement and no material weakness in the decade read (Item 9A of each
10-K; the FY2026 auditor's report on internal control, `0000779152-26-000067`); legal proceedings "routine" (Item 3); no
reportable related-party transaction (proxy, `0000779152-26-000088`); hedging and pledging of company stock prohibited for
directors and officers; a clawback policy; an independent board chair (Matthew Flanigan, a director since 2007); 91% support
on the last say-on-pay vote (proxy). The filer volunteers unfavourable facts in its own risk factors (renewal price
compression; consolidation; "we have experienced cybersecurity incidents in the past"), and files a separate 8-K each quarter
giving its deconversion revenue before results (8-K of 2026-08-11, `0000779152-26-000052`).

**The habits carried from Q4, read with that record** **[M2004-067]**. (1) *Guidance.* Annual guidance for GAAP revenue,
margin and EPS, given in each fourth-quarter release (8-K exhibits `0000779152-22-000071`, `-23-000057`, `-24-000076`,
`-25-000053`, `-26-000057`). Against the filed results: FY2023 guided revenue $2,080M to $2,087M, actual $2,077.7M (below),
EPS $5.05 to $5.09 against $366.6M of net income on 73.1M diluted shares, about $5.02 (below); FY2024 revenue $2,208M to
$2,229M, actual $2,215.5M (inside); FY2025 $2,369M to $2,391M, actual $2,375.3M (inside); FY2026 $2,475M to $2,504M, actual
$2,544.3M (above). Not a record of always landing on the number; FY2023 missed both. The rows grow "incredulous if they
consistently reach their declared targets" **[L2002-041]**; this record does not do that. (2) *The featured adjusted figure.*
The release leads with non-GAAP adjusted revenue and operating income; the adjustments remove deconversion revenue (which
lowers the adjusted figure), acquisition costs, an asset gain and a one-time contract change; stock pay and software
amortization are not removed. The "wave away very real costs" of **[L2016-006]** is not what these adjustments do. (3)
*EBITDA* in a release table (Q4). (4) *Pay set to a budget number* (Q6, Part B): 75% of the annual bonus on adjusted
operating income against the board-approved budget ($579.5M for FY2026), the incentive the rows warn turns into the desire
"to "hit the number."" **[L2019-006]**.

**Do they leave doubt?** Read together, the habits are those of an ordinary large listed company: guidance given, sometimes
missed; adjusted figures that do not strip real costs; no reserve movements, no restatements, no promotion of the stock price.
I find no doubt about honesty on this record. The rule is "If you've got doubts, forget it." **[M2013-088]**; the habits
weigh against the people's owner-orientation and are carried to Q6, Part B, not to the integrity STOP. Love of the business
cannot be read from the filings beyond the record itself and the absence of large personal holdings (all directors and
executive officers own 291,665 shares, 0.4% of the company; the chief executive 30,128 shares, about $4.4M at the Step 0
price; proxy). Trustworthiness "is more important than the brains" **[M2015-047]**; nothing in the filings read speaks against
it.

- **VERDICT on integrity: IN** (no doubt found on the filed record; the habits recorded and weighed) **[M2013-088]**,
  **[L2002-041]**. **Ability: WEIGHS FOR** **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *The retention test* **[R1995-009]**, read in market value and against intrinsic value **[R2009-002]**. FY2022 to FY2026:
  net income $2,069.8M, dividends $777.2M, retained $1,292.6M, of which $730.4M went into buybacks. The proxy's pay-versus-
  performance table: $100 invested on 2021-06-30 was worth $89.76 on 2026-06-30 with dividends reinvested, against $125.48 for
  the company's peer group (`0000779152-26-000088`). The market leg fails over five years. The intrinsic leg passes: owner
  cash at the book tax charge grew about 8% a year and revenue 7.7% a year over the same years (Q4, Q3), so the business per
  share grew while the price fell from a high multiple. The rows warn that the market leg alone misleads when prices fall
  **[R2009-002]**; the forward question, can it keep using what it retains, is answered at Q3: yes, at about 29%. Mixed, and
  the money kept in the business itself has been well used.
- *Buybacks.* The programme "does not include specific price targets or timetables" (10-K FY2026, Item 5). Average price paid
  (cash spent over shares bought, cash-flow statements and treasury-share counts): FY2014 $57.8, FY2016 $74.3, FY2018 $109.4,
  FY2019 $137.2, FY2020 $147.4, FY2021 $154.1 (2.80M shares, $431.5M), FY2022 $155.1, FY2023 $165.6, FY2024 $156.7, FY2025
  $169.3, FY2026 $152.1 (2.95M shares, $448.2M; fourth quarter $140.42, June 2026 $131.06, Item 5). Against the Q7 range
  computed below (default pair $67.98 to $129.58 a share; organic pair $81.74 to $146.59), every year's average since FY2016
  sits above the bottom of the default pair and every year's since FY2019 above its top. A buyback with no stated
  price weighs against unless the prices paid sit at or below the bottom of the range (framework, Q6) **[L2016-002]**,
  **[L1999-023]**: it weighs against. The two large years (FY2021, FY2026) were financed partly with the revolver, which the
  rows allow ("cash plus sensible borrowing capacity") **[L1999-023]**.
- *Deals.* Ensenta ($137.6M, FY2018), Geezeo ($30.4M, FY2020), Payrailz ($229.6M, FY2023), Victor ($42.4M, FY2026), all for
  cash, none for stock: the all-stock STOP does not arise. Payrailz, the largest, brought $8.5M of revenue and $22.5M of
  expenses in its first year (MD&A FY2023); no later figure for it is disclosed, and no post-mortem against the original case
  is published **[L2014-013]**. Goodwill unimpaired.
- *Dividends.* $2.38 a share in FY2026, raised each year; about a third of net income.
- **Part A WEIGHS AGAINST, narrowly**: retained money well used inside the business, but buybacks at prices above the range
  the business supports today and no stated price **[L2016-002]**, **[R2009-002]**.

**Part B: the pay, the board and the owners.** Annual bonus 75% on adjusted operating income against the budget, 25% on
strategic goals; long-term pay 60% performance shares vesting on relative total shareholder return against the S&P 900
(one third), organic revenue growth and adjusted operating margin expansion, the rest restricted stock (proxy, CD&A). No
measure charges for the capital used, though Q3 shows the capital per dollar of revenue rising by half in five years: the
rows charge managers "a high rate for incremental capital they employ" **[L1994-019]**. One third of the performance shares
ride on the share price relative to an index, which the person does not control **[M2003-019]**. Chief executive pay $8.4M in
FY2026 (summary compensation table); targeted at about the median of a peer group (CD&A). Independent chair, ownership
guidelines (6x salary for the CEO), anti-hedging, clawback (proxy). Directors and officers own 0.4%. No guidance-free,
owner-letter practice; the communication is the standard release and call. **Part B WEIGHS AGAINST, mildly**: pay on budget
numbers and relative stock price with no capital charge **[L1994-019]**, **[M2003-019]**, **[L2019-006]**.

## Q7 — WHAT IS IT WORTH? STOP.
How much cash, how sure, how soon, at the long government rate **[L2000-021]**, **[M1996-025]**, as a range **[L2000-024]**,
built by the framework's CONVENTION construction and six specifics; arithmetic in `value.py` and `owner_cash.py` in the
working folder.

**Inputs.** Owner cash after every real cost, all-equity (before interest expense, after the company's own tax), five-year
average FY2022 to FY2026: **$327.2M** (Q4 table). Acquisitions paid in the window average **$54.4M** a year. Growth shown,
measured on the aggregate series at the book tax charge because both end years carry tax timing (specific (a), the last year
aberrational on the filer's own words, **[L2005-003]**): **8.05%** a year; the literal window's end-to-end rate on the as-filed
series is 13.3% and is shown, not used. Organic growth as the filer reports it (non-GAAP adjusted revenue excluding
deconversions and acquisitions): 8%, 7.4%, 6.5%, 7.3% for FY2023 to FY2026, about **7.3%** (MD&A of each 10-K). Sovereign
**5.64%**. Ten years at the growth shown, then zero nominal growth (framework, Q7). Net debt **$70.7M**: debt $40.0M less cash
$12.1M at 2026-06-30, plus the $0.61 dividend declared on 2026-08-21 (Note 15, the filing's own subsequent event; $42.8M on
70.11M shares); operating leases ($37.8M) left out, as the basis says. Specifics: (a) applied as above; (b) growth positive,
not applied; (c) the default pair deducts acquisitions and credits the total growth, the organic pair leaves them out and
credits organic growth; (d) working capital, including the contract costs and client incentives, is inside operating cash;
(e) the filing gives no maintenance split, so the all-spending case is central and no maintenance-only case is computed; the
depreciation variant, for the record, would replace $255.5M of FY2026 capital spending with $196.3M of depreciation and
software amortization; (f) 8.05% is the shown rate and is carried only for ten years.

| Case | Owner cash | Growth | Whole-business value | Per share (less net debt, 70.11M shares) | Top / bottom |
|---|---|---|---|---|---|
| Default pair, all-equity (central) | $272.8M (after acquisitions) | 0% / 8.05% | $4,837M / $9,156M | **$67.98 / $129.58** | 1.89x |
| Organic pair, all-equity | $327.2M | 0% / 7.3% | $5,801M / $10,349M | $81.74 / $146.59 | 1.78x |
| Default pair at the book tax charge throughout (beside) | $251.7M | 0% / 8.05% | $4,463M / $8,447M | $62.64 / $119.48 | 1.89x |
| Literal window, as-filed growth (shown, not used) | $272.8M | 0% / 13.3% | $4,837M / $13,820M | $67.98 / $196.11 | 2.86x |
| Equity-only beside the central (owner cash after interest, no net debt) | $265.0M | 0% / 8.05% | | $67.01 / $126.85 | |

**Value range:** **$67.98 to $129.58 a share** (all-equity default pair) against **$146.07**; the organic pair $81.74 to
$146.59 beside. The price is 13% above the top of the central range and at the top of the organic pair. At the Step 0 price
the enterprise is valued at $10,312M; for the default base to be worth that at the long government rate, owner cash would have
to grow about 9.6% a year for ten years, and to earn the floor of about 10%, about 19% a year; on the organic base, about
16% a year to earn the floor (`value.py`). Neither has been shown.

**Closes.** The range is narrower than three to one (1.89x), so it is not TOO HARD on width **[L2000-025]**. The price sits
above the top of the central range, which closes OUT by the floor convention: the expected return at the price is below the
minimum, "a point at which we drop out of the game" **[M2003-149]**; on the organic pair it sits inside the range, at its top,
which closes OUT as a case that would need a pencil and does not scream **[M2009-005]**, **[M1996-084]**. The margin the rows
ask grows as certainty falls **[M1997-080]**, and here there is no margin at all.

**Fair price (a reporting figure, never a verdict; Part VII):** the reading used, a CONVENTION of this run because the text
does not say how a range midpoint becomes a stream: the cash stream whose value at the sovereign equals the midpoint of the
range (for the default pair, $272.8M growing 4.65% a year for ten years, then flat) is valued at the floor of 10% after the
company's tax, less net debt. **$52.52 a share** on the all-equity basis (central); **$52.00** on the equity-only basis beside
it. Organic pair, for the record: $61.08 all-equity, $60.61 equity-only. No cheap price is reported.

- **VERDICT: OUT.** The price ($146.07) is above the top of the central range ($129.58) and at the top of the organic range;
  the expected return at the price is below the floor **[M2003-149]**, and nothing here needs no pencil **[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7** (Q1 IN, Q2 IN, Q3 weighs for, Q4 weighs for, Q5 IN, Q6 weighs against): value range $67.98 to $129.58 a share
(all-equity default pair; organic pair $81.74 to $146.59) against $146.07 on 2026-10-07; fair price $52.52 all-equity, $52.00
equity-only (reporting figures, not verdicts). Integrity was judged at Q5 (IN), so no integrity flag is carried.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
Written down, not weighed; the box unchanged (operator rule 2) **[M1997-127]**.
- *Q8, the bond:* all-equity owner cash of $327.2M (five-year average) against an enterprise value of $10,312M at the Step 0
  price is 3.2% before any growth, against a 30-year Treasury at 5.64% (Step 0).
- *Q9, debt and exposures:* debt $40.0M at 2026-06-30, all on a new $1.0 billion five-year unsecured revolver of 2026-03-25
  (8-K `0000779152-26-000013`) with a minimum EBITDA-to-interest covenant, variable rate ("a 1% increase in our borrowing rate
  would increase our annual interest expense by $400" thousand, Item 7A); operating lease liabilities $37.8M (Note 4); cash
  kept near zero and the revolver used for buybacks (Q4). The filer states it has "experienced cybersecurity incidents in the
  past" (Item 1A) and that its hosted services are examined by the federal banking regulators (Item 1). Unrecognized tax
  benefits $23.6M (Note 8).
- *Q10:* nothing beyond Q7.
- *Q12:* the money is made processing the accounts and payments of community banks and credit unions; no named business of
  Q12 is involved.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Departures,
      stated: the session stopped at a usage limit on 2026-10-07 during Step 0 and resumed 2026-10-10; Q1's own commit was
      blocked by another session's git index lock and went in with Q2 (commit 166b922e says so); Q3 and Q4 went in one commit;
      Q5, Q6 and Q7 to the end went in one commit after the lock contention of 2026-10-10. Once, on 2026-10-10 about 10:11, a
      `.git/index.lock` five minutes old with no git process running was removed so that the waiting commits of several
      sessions could proceed; it may have been left by a commit process of this session that the shell killed.
- [x] If dispatched to an analyst: the brief allowed the per-question commits; a lock file was present in `Screens/_daily/`
      throughout (the dispatcher's); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared: commit
      subjects of the ESI, HAS, GFF and GRMN runs (session start) and of the KLAC, ITW and AME runs (in `git log` while
      committing on 2026-10-10), and the command lines of another session's commit script naming the ITW run (in a process
      listing). Not used.
- [x] Every v5 id resolves (`check_ids.py` in the working folder); every filing fact has its accession; no number without a row
      or a filing, except the CONVENTIONS of this run named below.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy; stock pay, all software
      spending and property spending deducted; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations; Q2; Q4); facts for later questions under AFTER THE STOP.
- [x] No row dated after the anchor is cited (the run is not point-in-time; the anchor is today).
- [x] Only the arithmetic lines of `tools/run.py` were used; its "D&A" column (depreciation only) was not used.
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in the commit message).

**CONVENTIONS of this run, confessed:** (1) the after-tax factor of 78% on interest expense for the all-equity basis (one minus
an effective rate of about 22%); (2) growth measured on owner cash at the book tax charge, the base kept as filed, because the
tax-law timing of FY2023 to FY2026 makes the end years aberrational while the five-year sum washes out (rationale: the
specific for aberrational years speaks of cycles and does not name a tax-law timing item); (3) the fair price read as the
sovereign-midpoint stream valued at the floor; (4) interest income on operating balances left in owner cash.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) *The fair price.* "The price at which the midpoint of the range earns the floor" does not say what cash stream the midpoint
is: the midpoint is a value, and a value earns 10% only once a stream is chosen. I used the stream whose value at the sovereign
equals the midpoint (growth solved for), valued at 10%; another analyst could value the midpoint's no-growth equivalent or
scale the midpoint by the ratio of the two rates, and get a different figure. (2) *Aberrational years that are not cyclical.*
Specific (a) defines the cycle base for "a cyclical peak or trough, or otherwise aberrational" year, but its remedy (the average
over the last full cycle, growth between cycle averages) assumes a business cycle. Here the aberration is a tax-law timing item
that depresses FY2023 and lifts FY2026 inside the window; there is no cycle to average over. Confessed as convention (2).
(3) *The parts threshold with near-equal parts.* Three parts at 34.5%, 32.8% and 32.6% of five-year segment income: "the
largest part decides" hands the file to Core by two points, while the other two parts are sold through the same client
relationships. I read all three; the rule should say what to do when the largest part's lead is within a few points.
(4) *Segment income before shared costs.* The parts threshold is computed on segment income that excludes research, selling,
general and corporate costs (here a $275M loss); the framework does not say whether shares are taken before or after shared
costs.

**Errors in the brief** (the dispatcher's message; every brief so far has carried one): (a) Fiserv is named "(FI)"; its EDGAR
record lists it as FISV on Nasdaq (submissions file for CIK 0000798354), though its FY2025 10-K documents still carry the "fi-"
prefix; the stale ticker would send a fetch to the wrong symbol. (b) nCino (NCNO) is listed with Temenos and the private cores as
"flagged", the brief's word for a rival that is not an SEC filer; nCino files 10-Ks (`0001902733-26-000022`) and is compared
here from its own filing. (c) "(Q2, Alkami ALKT for digital banking)" reads either as the framework's Q2 or as Q2 Holdings; both
were taken: the digital-banking rivals Alkami and Q2 Holdings (QTWO) are compared. (d) The canonical brief says `tools/run.py`
prints a "warning where only intangible amortization was found for depreciation"; for this filer it printed depreciation only in
its "D&A" column, omitting $171.1M of amortization, without a warning.
