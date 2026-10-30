# Company Run: Salesforce, Inc. (NYSE: CRM), 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every judgment
cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. The template was copied to this dated name before any fetch. Working folder:
`Test Runs/_research 2026-10-06 CRM/` (`run_py_output.txt`, `cover_shares_output.txt`, `sources_output.txt`,
`competitors_output.txt`, the scripts `fetch.py`, `competitors.py`, `row.py`, `verify_ids.py`; raw filing text under
`cache/`, gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. The dispatch forbids opening
`PORTFOLIO.md`, so whether the operator holds CRM is unknown to this analyst.

**CONTAMINATION DECLARED.** (1) The project map (`CLAUDE.md`, read first by rule) names a file
`Test Runs/2026-09-21 RE-LOOK - CRM Salesforce at the first level.md`. It was not opened. Its name alone says that an
earlier run under v4.1 produced price levels for this name and that the price reached the first of them by 2026-09-21,
which implies that an earlier analyst got as far as a value range. That is a prior, and it leans toward "the business
can be valued". It is declared so that it can be discounted; this run does not know what that file concluded. (2) The
analyst's training memory of Salesforce (a CRM vendor grown by subscription and acquisition; an activist campaign in
early 2023; the "agentic" pivot) is a prior to be replaced by the filings, not confirmed by them. (3) No queue,
resume-state, reading-list, alerts or holding-review file was opened. A directory listing of `Test Runs/` was seen
(names only, the 2026-10-05 runs), and the YELP run of 2026-10-05 was read for form only.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $229.79 (close 2026-10-05; Yahoo Finance chart endpoint via `tools/run.py`; **aggregator, live quote only,
  flagged** per operator rule 5).
- **Shares by class** from the latest filing's cover: **approximately 823 million** common shares, par $0.001, one class,
  as of 2026-08-20 (Form 10-Q for the quarter ended 2026-07-31, filed 2026-08-27, accession `0001108524-26-000190`;
  `python Screens/cover_shares.py CRM` returned 823,000,000 from the same filing). The cover rounds to the million; the
  count is 929 million at 2026-01-31 (10-K), the fall being the $25 billion accelerated repurchase of March 2026 (below).
- **Market cap:** $189,117M (823.0M x $229.79).
- **Balance sheet at 2026-07-31** (10-Q, `0001108524-26-000190`): cash and equivalents $8,310M, marketable securities
  $3,093M, strategic investments $11,324M (not counted as cash), noncurrent debt $39,288M, current debt $0: net debt
  $27,885M before the strategic investments.
- **Sovereign for the earnings currency (USD):** 5.66%, 30-year par yield, US Treasury daily par yield curve, 2026-10-05
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2026 (year ended 2026-01-31), filed 2026-03-02, `0001108524-26-000060`: Item 1 (business, competition,
    customers), Item 1A (renewal and attrition, competition, AI, consumption pricing), Item 7 (attrition, cash flows),
    the cash flow statement.
  - 10-Q Q2 FY2027 (quarter ended 2026-07-31), filed 2026-08-27, `0001108524-26-000190`: cover, balance sheet, debt table.
  - DEF 14A, filed 2026-04-16, `0001108524-26-000085`: fetched; not read past the cover, because Q5 and Q6 were not reached.
  - 8-K of 2026-08-26, `0001108524-26-000187`, Exhibit 99.1 (Q2 FY2027 results), read before any judgment of the
    filer's non-GAAP habits; 8-K of 2026-09-17, `0001108524-26-000210`, Exhibit 99.1 (Investor Day 2026 deck, as filed);
    8-Ks of 2026-03-12 (`0001193125-26-104282`, ASR agreements and five-year credit agreement), 2026-03-13
    (`0001193125-26-106356`, $25.0 billion of senior notes) and 2026-03-16 (`0001193125-26-107403`, Exhibit 99.1, the ASR
    commenced).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2026 $14,996M on
  the filed consolidated statement of cash flows (10-K, `0001108524-26-000060`) equals the tagged 14,996 that
  `tools/run.py` printed; stock-based compensation expense $3,509M and capital expenditures $594M also agree.
- **`tools/run.py CRM --framework v5`, arithmetic lines only** (Part VII; nothing it prints as a rule was used; full output
  in `run_py_output.txt`). Owner cash = operating cash flow less all stock pay less capital spending, USD millions:

| FY (ends Jan) | OCF | stock pay | stock pay % of OCF | capex | owner cash (capex basis) | owner cash (D&A basis) |
|---|---|---|---|---|---|---|
| 2024 | 10,234 | 2,787 | 27.2% | 736 | 6,711 | 3,488 |
| 2025 | 13,092 | 3,183 | 24.3% | 658 | 9,251 | 6,432 |
| 2026 | 14,996 | 3,509 | 23.4% | 594 | 10,893 | 7,856 |

  Three-year mean 8,952 (capex basis), 5,925 (D&A basis); five-year mean 6,479 (capex basis), 3,549 (D&A basis), the
  window spread being -40.1% on the lower basis (`run.py`). Finance-lease principal payments ($584M in FY2026) sit in
  the financing section and are not in the capex line; with them the three-year capex-basis mean is 8,346.

- **Balance sheets, ten year-ends, read before the income account** (transcription from `tools/run.py`, XBRL, with the
  latest checked against the filed 10-K and 10-Q balance sheets), "balance sheets over an 8 or 10 year period before I
  even look at the income account" **[M2025-032]**, USD millions:

| year-end | assets | equity | cash | receivables | goodwill | intangibles | debt on the face | retained |
|---|---|---|---|---|---|---|---|---|
| 2017-01-31 | 17,585 | 7,500 | 1,607 | 3,197 | 7,264 | 1,113 | 2,008 (partial tag) | -465 |
| 2019-01-31 | 30,737 | 15,605 | 2,669 | 4,924 | 12,851 | 1,923 | 3,173 (partial tag) | 1,735 |
| 2021-01-31 | 66,301 | 41,493 | 6,195 | 7,786 | 26,318 | 4,114 | 2,673 (partial tag) | 5,933 |
| 2023-01-31 | 98,849 | 58,359 | 7,016 | 10,755 | 48,568 | 7,125 | 10,601 | 7,585 |
| 2025-01-31 | 102,928 | 61,173 | 8,848 | 11,945 | 51,283 | 4,428 | 8,433 | 16,369 |
| 2026-01-31 | 112,305 | 59,142 | 7,327 | 14,339 | 57,941 | 6,815 | 14,439 | 22,221 |
| 2026-07-31 | 109,620 | 38,378 | 8,310 | 6,320 | 59,250 | 6,142 | 39,288 | 27,107 |

  (The odd years are in `run_py_output.txt` and run between their neighbours. January receivables are seasonal: annual
  billing falls in the fourth quarter, so the July figure is not comparable with the January ones.) What the figures
  say: the business was built in large part by purchase. Goodwill rose from $7.3 billion to $59.3 billion in nine years
  and now exceeds the whole of stockholders' equity ($38.4 billion); tangible equity at 2026-07-31 is about minus $27.0
  billion. Between January and July 2026 treasury stock rose from $32.2 billion to $55.0 billion and noncurrent debt from
  $10.4 billion to $39.3 billion: the repurchase was paid for mostly with new debt. What the figures cannot say: whether
  the subscriptions behind the $59 billion of goodwill will be renewed per human user in ten years, which is the Q1
  question below.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own Salesforce "if the market closed for five
years" **[M1997-109]**, and that turns on what enterprises will pay for customer-relationship software in five and ten
years, not on the quotation, which "just tells us prices" **[M2006-077]**. Who is paid to tell you bears hard on this
name: the filer publishes a revenue target four years out ($63B+ for FY2030, Investor Day deck, `0001108524-26-000210`)
and a 190% payout of free cash flow, and the advice around a $25 billion repurchase and a $25 billion bond issue earns
fees for one answer and none for the other, "you do not get impartial advice from Wall Street" **[M2020-037]**;
projections are not consulted, and the projector's past projections are asked for **[M1995-050]**. No macro view enters
**[M2000-094]**. The analyst's habits: "I’m looking for what’s wrong in things" **[M2025-013]**; the worst anchor "is
always your previous conclusion" **[M2016-054]**, which here includes the earlier run's existence declared above.
**Contrary evidence, written down as found** **[M1997-127]**:
1. Against TOO HARD (found first, written first): Salesforce has sold the same kind of product, customer records and the
   workflow around them, for twenty-seven years; revenue grew from $6,667M (FY2016) to $41,525M (FY2026); the 10-K puts
   attrition at *"approximately eight percent"* and says the company has *"helped keep our attrition rate consistent as
   compared to the prior year"*; current remaining performance obligation is $33.5 billion, up 14% (Exhibit 99.1,
   `0001108524-26-000187`). Customers who keep coming back for decades are the thing a forecast is made from.
2. Against TOO HARD again: the filer itself writes a forecast down, the FY2030 revenue target above, and the AI product it
   says threatens the category is also its own fastest-growing line (Agentforce ARR above $1.5 billion, *"up over 240%
   Y/Y"*, same exhibit). And the speakers count it as an error to stare at an understood business and do nothing
   **[M2001-006]**.
3. Against the business, found while reading Item 1: the filer describes its own market as *"highly competitive, rapidly
   evolving and fragmented, and subject to changing technology with low barriers to entry"* (10-K, Competition). Recorded
   at Q1.

## THE STANDING RULE
Owning Salesforce would not put the buyer at risk of ruin provided it is bought without borrowed money and sized so that
a total loss is bearable: "borrowed money has no place in the investor's tool kit" **[L2014-005]**; "We are never going
to risk what we have and need for what we don’t have and don’t need." **[M2012-081]**. No purchase is reached in any case.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the draft states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years", with "some notion of how the industry will develop and where the company
will stand within the industry" **[M2012-065]**; the definition is "a reasonable probability of being able to asses
where the business will be in 10 years" **[M2000-037]**. Knowing the product is not enough: "We just don’t know the
economics of it 10 years from now." **[M2000-104]**. The first step is "trying to identify the key variables in that
particular business, and evaluating how predictable they were first" **[M1998-044]**.

**What the business is, from the filing.** Salesforce sells subscriptions, typically for 12 to 36 months, to software
for customer records and the work done on them: sales, service, marketing and commerce, plus a development platform,
Slack, integration (MuleSoft, Informatica) and analytics (Tableau) (10-K FY2026, `0001108524-26-000060`, Item 1). FY2026
subscription and support revenue was $39,388M: Sales $9,028M (+8%), Service $9,818M (+8%), Platform, Slack and Other
$8,882M (+23%, of which $388M Informatica), Marketing and Commerce $5,428M (+3%), Integration and Analytics $6,232M (+8%)
(same, MD&A). The two core clouds, nearly half of the total, are priced historically per user; the newer AI and data
products are sold *"through a consumption-based business model"*, and the filer has *"limited experience with
determining optimal pricing for our consumption-based contracts"* (Item 1A).

**The key variables.** Three decide the ten-year economics:
1. **How many paid human users enterprises will have, and at what price.** The filer lists among the causes of attrition
   *"decreases in the number of users at our customers"* and *"the increased prevalence of consumption-based pricing
   models"* (10-K Item 1A; repeated in the 10-Q, `0001108524-26-000190`), and warns that *"New AI offerings may disrupt
   our service offerings or transform workforce needs and negatively impact demand for our offerings"* (same). Its own
   product pitch is *"always-on digital labor for employees and customers"* (Item 1), that is, software that does work
   now done by the people Salesforce charges for; its own Investor Day scenario for an "Agentic" customer reads *"Adopts
   Agentforce in support and core expansion, with some seat optimization"* (Exhibit 99.1, `0001108524-26-000210`).
2. **Whether the work stays inside Salesforce's applications or moves to another layer.** The filer names as current
   competitors *"AI-native companies and emerging startups that leverage generative AI and large language models as the
   core foundation of their architecture, offering highly specialized, autonomous, or automated solutions that may bypass
   traditional business process workflows or displace established user interfaces"* (Item 1, Competition). Its newest
   product answer, as the Q2 release puts it, is *"unlocking the data, workflows, business logic, actions, and governance
   inside Salesforce and making it available to every agent, model, and interface"* (Exhibit 99.1,
   `0001108524-26-000187`): the company is preparing for the interface to sit elsewhere.
3. **What the replacement revenue will earn.** Agentforce ARR above $1.5 billion, Agentforce and Data 360 ARR nearly $3.9
   billion (same exhibit), against subscription revenue of $39.4 billion; priced by consumption, with the margins of a
   business that buys model capacity from others (the filer lists among its risks its reliance on *"third-party
   infrastructure providers, including hardware, software, energy and platform providers"*, 8-K of 2026-03-12,
   `0001193125-26-104282`, forward-looking statements).

**Are the key variables predictable?** The customer's habit of keeping one system of record for its customers is the
kind of thing a reader can follow, and the eight percent attrition is evidence of it. But the economics do not run on
the habit; they run on the unit the habit is billed in. Whether a bank in 2036 pays Salesforce for ten thousand service
seats, for three thousand seats and a meter of agent work, or for a data layer read by an agent sold by Microsoft,
OpenAI or a start-up, is a forecast of how fast AI agents replace clerical and sales labour, how vendors will price
them, and who will own the layer the user talks to. Every one of those is a technology forecast about others' products.

**The tests, one by one.**
- *Where will it be in ten years?* "You’re trying to print the next 10 years of Value Line in your head." **[M1999-132]**.
  I cannot print seats, price per seat or the consumption mix for FY2036 within a range I would defend. An analyst in
  2016 could have printed seat growth for 2026 roughly; the variable that now decides it, agents doing the work of the
  users, was not in the FY2016 picture at all.
- *Do the past statements tell me the future ones?* "the financial statements will tell me the information that’s useful
  to me in making a judgment about what the future financial statements are going to look like" **[M2008-033]**. Not
  here. The decade of statements records revenue compounding at about 20% a year, much of it bought (goodwill $7.3
  billion to $59.3 billion), on a per-user model whose base the filer now says AI may *"transform"*. Core growth has
  already slowed to 8% (Sales, Service) and 3% (Marketing and Commerce) in FY2026; the statements cannot say whether that
  is a cycle or the first years of a smaller user base.
- *Is it important and knowable?* "If something’s important but unknowable, forget it." **[M2006-076]**. The deciding
  variable, the number of paid human users in an economy deploying agents, is the most important one in the business and
  is not knowable from here.
- *Would the insiders write it down?* The rows' test: insiders "would not want to put down on paper their predictions
  about where 10 companies you would choose in the tech field would be in 10 years, in terms of their economics"
  **[M2000-105]**. Salesforce writes down a four-year revenue target (contrary evidence 2 above) but describes its market
  as *"rapidly evolving"* with *"low barriers to entry"* and says AI may *"disrupt our service offerings"* (10-K). HubSpot,
  the nearest CRM rival in its own words: competitors using *"evolving AI technologies"* may *"render our existing or
  future products less competitive, or obsolete"*, and it *"may need to decrease the prices"* (10-K FY2025,
  `0001193125-26-046646`). ServiceNow: *"A failure to innovate and adapt how we offer our products in response to rapidly
  evolving technological changes and in the midst of an intensely competitive market may harm our competitive position"*
  (10-K FY2025, `0001373715-26-000007`). Microsoft, which sells Dynamics against Salesforce: its AI investments depend on
  *"evolving customer demand, technological developments, competitive dynamics"* and *"the pace of adoption of AI"* (10-K
  FY2026, `0001193125-26-323660`). None of the four writes the ten-year forecast down; the one forecast written is the
  seller's four-year target, and "don’t ask the barber whether you need a haircut" **[M2011-083]**.
- *Can I name the winner, not just the industry?* Enterprise software spending will grow (the filer cites Gartner for it),
  but "we don’t have the faintest idea who the winners will be" **[M2012-067]**, and seeing growth in an industry "does
  not mean we can judge what its profit margins and returns on capital will be as a host of competitors battle for
  supremacy" **[L2009-005]**.
- *Is the forecast about customers or about technology?* The rows separate them in the case nearest this one: Apple "much
  more of a consumer products business", read through what "their prospective customers will do in the future, as
  opposed to, say, IBM’s customers, it’s a different sort of analysis", and the same speaker adds "I was wrong on the
  first one" **[M2017-019]**. An enterprise software vendor's customers are IBM's kind, and the speaker's one recorded
  attempt to read them he calls wrong. The IBM purchase was made by a man who had read the annual report "for more than
  50 years" **[L2011-010]** and who still said "I do not understand the moat around an IBM as well as I understand the
  mode around a Coca-Cola" **[M2013-074]**.
- *Is there a technological component of significance?* Yes: "where we think the future technology could hurt the
  business as it presently exists", "it won’t make it through the filter" **[M1998-008]**; "a business that must deal
  with fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics"
  **[L1993-023]**; "whenever we look at a business and we see lots of change coming, 9 times out of 10, we’re going to
  pass on that" **[M1999-063]**. The speakers put the software business by name outside their circle: "the software
  business is not within my circle of competence" **[M1999-074]**; "I don’t know what that world will look like in 10
  years" **[M1998-050]**; "it’s much easier to predict the relative strength that Coke will enjoy in the soft drink world
  than the strength" Microsoft "will possess in the software world" **[M1999-072]**.
- *How far off could I be?* "some model in our mind of how far off we can be" **[M2011-084]**. Here the range runs from
  Salesforce as the governed data and workflow layer every agent must call, charging more per customer than today (the
  filer's own *"Agentic Enterprise"* scenario of a 3x-4x+ ARR uplift, Investor Day deck), to Salesforce as a database with fewer paying users and agent work priced by
  vendors with their own models, the case the rows narrate when a leader's technology base shifts: "Companies get left
  behind" and "here are a bunch of people that should know a lot about that business but they couldn’t see the future
  either" **[M1997-023]**; "Leadership alone provides no certainties" **[L1996-031]**.
- *Do I doubt it is inside?* I do. "if you have doubts about something being into your circle of competence, it isn’t"
  **[M2002-092]**.

**Answering the contrary evidence.** Item 1 (twenty-seven years, eight percent attrition, cRPO up 14%) is real and is
written down above. It shows the habit of the customer, which is not in doubt; it does not show the unit the habit will
be paid in, and slow change "can lull you to sleep easier" **[M2014-038]**: the per-user base can shrink inside renewals
that still look consistent, since the filer itself names fewer users as a cause of attrition. Item 2 (the filer's own
forecast and its fast-growing AI line) cuts both ways: a four-year revenue target from the seller is the projection the
rows do not consult **[M1995-050]**, and an AI line growing 240% from a small base is evidence that the change is under
way, not that its economics can be seen. The omission row counts only misses "within our circle of
competence" and names "a software company" as a miss that "is not an error" **[M2001-006]**. Outside the circle, "there is no penalty in
investing if you don’t swing at a ball that’s in the strike zone" **[M2018-087]**.

**Routing.** A business whose ten-year economics cannot be foreseen because its industry changes fast closes here, in
"too hard" among the "three boxes at the company: in, out, and too hard" **[M2006-013]**, not OUT on the business: "It
doesn’t mean it isn’t a good buy." **[M2000-038]**. The castle questions (switching costs, the low-cost position, the
competitor row) belong to Q2, which is reached only by a business Q1 has passed (framework, Q1, The routing, fixed); the
competitor figures gathered are recorded below the box as evidence only.

**Which cause: WORK or NATURE.** NATURE. The deciding question (how many human users enterprises will pay for, and who
will own the agent layer and its pricing, over ten years) is a forecast the industry's insiders do not write down
**[M2000-105]**: Salesforce, HubSpot, ServiceNow and Microsoft each call the field rapidly evolving in their latest
10-Ks, and the one written forecast is a four-year sales target. It is the roadblock "the nature of the industry would
be" **[L1993-023]**, not the reader's want of work, which is the cause in "I haven’t done the work and I’m not sure if I
did the work I would understand them" **[M1994-026]**: more reading of Salesforce's filings would not reveal how fast
OpenAI, Microsoft and the start-ups will make the clerk's seat unnecessary, a problem "which we can't solve by studying
up" **[L1999-018]**. "if we can’t make a decision in five minutes, we can’t make it in five months" **[M2008-086]**. A
lower price does not reopen the box **[M2000-038]**.

**VERDICT: TOO HARD (NATURE).** Salesforce's ten-year economics turn on how many paid human users its customers will
keep once AI agents do part of their work, and on who will own and price the agent layer; the filer itself names both
as risks, calls its market rapidly evolving with low barriers to entry, and neither it nor its rivals write the
ten-year forecast down. The file closes here. No research pass is opened (a NATURE close takes none, framework section I).

---
## Q2 — WHY IS THE CASTLE STILL STANDING? STOP. **NOT REACHED** (closed at Q1).
The competitor figures gathered for this question are recorded below the box as evidence only, not as a Q2 verdict.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING. **NOT REACHED.**

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion. **NOT REACHED.** (The balance sheets were read in Step 0.)

## Q5 — WHO RUNS IT? STOP on integrity. **NOT REACHED.**

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING. **NOT REACHED.** (The repurchase and debt facts are recorded below as evidence only.)

## Q7 — WHAT IS IT WORTH? STOP. **NOT REACHED.** No value range was computed.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP. **NOT REACHED.**

## Q9 — COULD IT RUIN US? WEIGHING. **NOT REACHED.**

## Q10 — IS IT THE FAT PITCH? WEIGHING. **NOT REACHED.**

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE? **NOT ASKED.**

---
## THE BOX
**TOO HARD (NATURE), decided at Q1.** Salesforce's ten-year economics depend on how many paid human users its customers
keep once AI agents do part of their work, and on who owns and prices the agent layer; the filer calls its own market
*"rapidly evolving"* with *"low barriers to entry"*, and no insider (Salesforce, HubSpot, ServiceNow, Microsoft) writes
the ten-year forecast down. Q7 was not reached and no value range was computed. Price $229.79 (aggregator, flagged).

---
## EVIDENCE RECORDED BEYOND THE CLOSE (record only; not a Q2, Q4, Q6 or Q9 verdict)

**The competitor row, from the competitors' own filings** (XBRL company facts, annual values as tagged in 10-K filings,
USD millions; operating margin = GAAP operating income over revenue; `competitors.py`, `competitors_output.txt`):

| company | revenue, start of span | revenue, latest year | op. margin start | op. margin latest | own words on AI (latest 10-K) | latest 10-K accession |
|---|---|---|---|---|---|---|
| Salesforce (FY ends Jan) | 6,667 (FY2016) | 41,525 (FY2026) | 1.7% | 20.1% | market *"rapidly evolving"*, *"low barriers to entry"*; AI may *"transform workforce needs"* | `0001108524-26-000060` |
| Microsoft (FY ends Jun; Dynamics not broken out in dollars) | 91,154 (FY2016) | 331,839 (FY2026) | 22.1% | 46.8% | *"Dynamics 365 revenue increased 18%"*; *"Dynamics competes with cloud-based and on-premises business solution providers"* | `0001193125-26-323660` |
| ServiceNow | 1,005 (2015) | 13,278 (2025) | -16.5% | 13.7% | *"rapidly evolving technological changes"*, *"intensely competitive market"* | `0001373715-26-000007` |
| HubSpot | 182 (2015) | 3,131 (2025) | -25.5% | 0.2% | AI could make products *"less competitive, or obsolete"*; *"may need to decrease the prices"* | `0001193125-26-046646` |
| Oracle (FY ends May) | 37,047 (FY2016) | 67,357 (FY2026) | 34.0% | 30.6% | not read for AI language | `0001193125-26-277521` |

Read across: the one rival that discloses a CRM-like line, Microsoft's Dynamics 365, grew 18% in its FY2026 against 8%
for Salesforce's Sales and Service clouds in FY2026; Salesforce's GAAP operating margin of 20.1% compares with Microsoft's
46.8% for the whole company. HubSpot, the CRM rival for smaller firms, reached break-even only in 2025. None of this is a
Q2 finding; Q2 was not reached.

**Stock pay, the repurchase and the debt** (record only, Q4, Q6 and Q9 NOT REACHED):
- Stock pay was $3,509M in FY2026, 23.4% of operating cash flow (27.2% in FY2024). The Q2 FY2027 release headlines
  non-GAAP operating margin (34.1%) and non-GAAP EPS ($5.90, *"up 103% Y/Y"*), both of which exclude stock pay
  (Exhibit 99.1, `0001108524-26-000187`; the Investor Day reconciliation adds back $3,480M of stock pay for FY2026).
- In February 2026 the board authorized $50 billion of repurchases; on 2026-03-11 the company entered $25 billion of
  accelerated repurchase agreements with five banks, with an initial delivery of about 103 million shares, *"approximately
  80% of the total shares anticipated"* at the 2026-03-11 close, which implies a close of about $194 (8-Ks
  `0001193125-26-104282`, `0001193125-26-107403`). It was paid for with $25.0 billion of senior notes issued 2026-03-13 in
  eight series from 4.500% due 2028 to 6.700% due 2066 (8-K `0001193125-26-106356`). The Investor Day deck states a
  *"$182 expected average share price"* for the ASR and *"190% of Free Cash Flow returned in FY27"* (`0001108524-26-000210`).
  The program names no price above which it stops. Noncurrent debt rose from $10,439M to $39,288M and stockholders' equity
  fell from $59,142M to $38,378M between 2026-01-31 and 2026-07-31 (10-Q). Whether the prices paid sit below a
  conservatively calculated value **[L1999-023]** cannot be said, because no value range was computed (Q7 NOT REACHED).
- Acquisitions keep coming: Informatica (closed Q4 FY2026), Regrello ($818M, October 2025), and Contentful and Fin (agreed
  June 2026, expected to close in Q3 FY2027) (10-K; Exhibit 99.1, `0001108524-26-000187`).

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question (Step 0 to the standing rule, then Q1);
      committed after each with a pathspec (`6cb7be8`, `cd15404`, then this close). The overnight lock was not written:
      the dispatch forbids editing any file other than the run file and research folder.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` (`verify_ids.py`: every bold id found; every quoted fragment
      that precedes an id found in that row); every filing fact carries its accession; every number is from a filing, a
      row or `run.py`/`competitors.py` arithmetic.
- [x] The order was kept; Q1 closed the run; nothing after it is a clearance, and no valuation was computed.
- [x] Owner cash after every real cost (all stock pay, capital spending; the finance-lease variant shown), never a
      net-income proxy; the sovereign from the US Treasury; the price quote flagged as an aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]**, the case against TOO HARD first.
- [x] No row dated after the anchor is cited (not a point-in-time run; today is the anchor).
- [x] Only the arithmetic lines of `tools/run.py` were used.
- [x] `python tools/check_framework.py` PASS before each commit.
- [ ] Not done: the DEF 14A was fetched but not read (Q5 and Q6 not reached); Oracle's AI language not read; Microsoft
      does not give Dynamics revenue in dollars; SAP (a 20-F filer) not fetched.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Test 7 of Q1, customers or technology,** is stated for consumer businesses **[M2017-019]**, **[M2023-030]** and says
nothing of a business whose customers are stable but whose billing unit (the human user) is what the technology attacks.
Salesforce's customers are as sticky as any; the doubt is in the unit. I read **[M2017-019]**'s IBM contrast as placing
enterprise vendors on the technology side, which is a reading, not a rule. (2) **Q1 test 5, "would the insiders write it
down?"**, does not say what to do when the filer writes a short forecast (a four-year revenue target) but not the
ten-year one; I treated the seller's target as a projection not consulted **[M1995-050]**, **[M2011-083]**, and looked to
the rivals' own risk language instead. A rule on which insiders count (the filer, its rivals, or both) would make two
analysts agree. (3) **The routing leaves strong Q4 and Q6 evidence unweighed.** A $25 billion repurchase paid for with
$25 billion of new debt and no stated price, goodwill above equity, and stock pay near a quarter of operating cash are
facts the framework would weigh heavily at Q4, Q6 and Q9, but a Q1 TOO HARD sends the file to the box before them; I
recorded them below the box. The framework might say whether a NATURE close may carry a line that later questions would
also have weighed against. (4) **The template's position note** asks the analyst to check `PORTFOLIO.md`, which the
dispatch's blind rule forbids; the blind rule was followed. (5) **The project map names an earlier CRM file** whose title
discloses that a v4.1 run produced price levels; a blind dispatch cannot keep that out, and the framework's contamination
practice has no rule for a prior carried in a file name.
