# Company Run — Choice Hotels International, Inc. (NYSE: CHH) — 2026-10-14
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copied to its dated name before any fetch** (commit
b221b61b, 2026-10-14).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled by the dispatching session at the fold (overnight 2026-10-14), after the run was committed: not held (`PORTFOLIO.md` carries no line for CHH or Choice Hotels).

**Dispatch.** A dispatched blind run under `Screens/_daily/_dispatch_brief.md` as departed from in the brief (the analyst
derives the lines of evidence from the 10-K's Items 1, 1A and 7). The lock is held by the dispatching session (operator
rule ten (b)); this analyst did not write or touch it.

**Contamination, declared and not used.** (1) The session's opening git status listed recent commit subjects, one of which
(a fold of another company's run, HLT, dated 2026-10-14) names a ratio for "Choice" (operating income against net tangible
assets) beside Marriott and Hyatt figures. I read the subject line before I could avoid it; I did not open that run, I do
not use that figure, and the competitor metric below was chosen and computed from the filings independently (it is a
different metric, on a different capital base). (2) A directory listing of `Test Runs/` made to check that my dated file
name was free showed the file names of other runs dated 2026-10-14 (HLT, MAR and four steel companies). None was opened.
(3) The memory index loaded with the session states general queue facts (a count of gate-clearers, "nothing buyable");
nothing in it names this company and nothing of it is used.

**Lines of evidence, derived from the FY2025 10-K (Items 1, 1A and 7) and why** (the brief's one departure):
1. *The fee stream and its drivers* (Item 1, "the primary factors that affect the Company's results": rooms, mix,
   occupancy and rate, royalty rate). Read: the U.S. system table 2016 to 2025 from the FY2020 and FY2025 10-Ks (rooms,
   RevPAR, royalty rate, royalty fees), the international table, the pipeline.
2. *What it costs to win and keep a franchisee* (Item 1A, "competition may require us to ... make greater use of
   financial incentives, including franchise agreement acquisition costs, loans and guaranties"). Read: franchise agreement
   acquisition cost payments in operating cash flow, 2016 to H1 2026, and the capitalized balance (Note 6).
3. *The capital the "asset-light" model now consumes* (Item 1A, "may result in exposure to losses and be disruptive to our
   asset-light business model"; Item 7, $667.2 million in Cambria and Everhome support). Read: owned hotel, affiliate and
   note spending 2016 to H1 2026; the acquisitions (WoodSpring 2018, Radisson Hotels Americas 2022, Choice Hotels Canada
   2025) and the failed Wyndham pursuit 2023 to 2024.
4. *Distribution* (Item 1A, internet intermediaries and AI booking). Read as a Q2 threat; no figure for the channel mix is
   filed (no instance found in the FY2025 10-K of a share of bookings by channel).
5. *Franchisee health* (Item 1A, deterioration of franchisees; Item 7, provisions for credit losses). Read: receivables,
   allowance and write-offs, 2024 to H1 2026; the reimbursable deficit 2023 to 2025.
6. *Debt and its terms* (Item 1A, indebtedness; Item 7, the notes, the revolver, the 2026 term loan 8-K).
7. *Control and the people* (Item 1A, concentration of ownership; the 2026 proxy; the 2026 8-Ks on the CEO change).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $103.88 (close 2026-10-13; printed by `tools/run.py` from an aggregator, flagged per operator rule 5, live
  quote only).
- **Shares by class** from the latest filing's cover: 45,008,622 common shares, par $0.01, one class (10-Q for the period
  ended 2026-06-30, filed 2026-08-05, accession `0001046311-26-000025`; `python Screens/cover_shares.py CHH`). Checked:
  issued 95,065,638 less treasury 49,886,198 = 45,179,440 at 2026-06-30 on the 10-Q balance sheet, which agrees with the
  balance-sheet count; the cover count (as of 2026-07-29) is lower by the buyback since. No 8-K or prospectus after the 10-Q
  changes the count (8-Ks of 2026-08-28, 2026-08-31 and 2026-10-01 are a term loan and two officer matters; the S-3ASR of
  2026-08-05 is a shelf, no issuance found). The cover count is used.
- **Market cap:** $103.88 x 45.009M = **$4,675.5M**.
- **Sovereign for the earnings currency (USD):** **5.56%**, US Treasury daily par yield curve, 30-year, 2026-10-13
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-19, `0001046311-26-000008`): Items 1, 1A, 3, 7, 7A,
  the statements and Notes 1, 4, 5, 6, 16 in part; 10-Q Q2 2026 (filed 2026-08-05, `0001046311-26-000025`): statements,
  Notes 3, 7, 11, MD&A in part; DEF 14A 2026 (filed 2026-04-22, `0001046311-26-000013`): ownership, CD&A, related-party
  section; 8-Ks `0001193125-26-232581` (2026-05-20, CEO steps down), `0001628280-26-046377` (2026-07-01, director),
  `0001193125-26-374377` (2026-08-28, $500M term loan), `0001193125-26-375580` (2026-08-31, new CEO), `0001193125-26-409974`
  (2026-10-01, CHRO transition), and the earnings release exhibit 99.1 of `0001046311-26-000006` (2026-02-19). For the span:
  10-Ks FY2024 `0001046311-25-000007`, FY2023 `0001046311-24-000010`, FY2022 `0001046311-23-000008`, FY2021
  `0001046311-22-000009`, FY2020 `0001046311-21-000014`, FY2019 `0001046311-20-000011`, FY2018 `0001046311-19-000011`
  (cash-flow statements, system tables, MD&A capital lines).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $270,447
  thousand on the filed statement of cash flows (10-K FY2025), equal to the $270.4M `tools/run.py` transcribed from XBRL.
  Also checked: the stock-pay figure. `tools/run.py` prints an "SBC+other" alternate that adds the OCF add-back line
  "Non-cash share-based compensation and other charges" ($38.3M in 2025) to the share-based compensation expense ($38.3M);
  the two are the same cost counted twice, so the alternate is not used. Stock pay is taken from the filed table of
  share-based compensation expense (Note on share-based compensation: $38.3M 2025, $38.4M 2024, $40.5M 2023, $40.5M 2022,
  $23.4M 2021).
- `python tools/run.py CHH`, arithmetic lines only (output kept in `Test Runs/_research 2026-10-14 CHH/run_py_output.txt`):
  OCF $296.6M, $319.4M, $270.4M (2023 to 2025); capex as tagged $47.7M, $39.1M, $38.9M is only "other property and
  equipment" and leaves out the owned-hotel spending ($68.6M, $106.8M, $106.9M), which this run adds back in (Q4, Q7).
  The ten-year balance-sheet table is used at Q4. Nothing it prints as a rule, a yield verdict or a v4 id is used (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I would be content to own this fee stream "if the market closed for five
years" **[M1997-109]**, and the answer turns on the franchise contracts and the brands, not on the quotation. The market
serves: the price is $103.88 and "it just tells us prices" **[M2006-077]**; the decision follows "where the facts and
reasoning lead". Margin of safety: "if you have to actually do it on — with pencil and paper, it’s too close to think
about" **[M1996-084]**. No macro: the run does not forecast RevPAR or the lodging cycle **[M2000-094]**; it reads the cycle
the filings show. Who is paid to tell you: the company's own featured figure is "Adjusted EBITDA reached a company record
$625.6 million" (earnings release, 2026-02-19), against GAAP operating income of $448.4M; the run works from the cash-flow
statement. The analyst's habits: "I’m looking for what’s wrong in things because that’s part of investing" **[M2025-013]**;
"What do I not know that I need to know?" **[M1999-129]**. **Contrary evidence, written down as found** **[M1997-127]**:
(i) U.S. rooms fell 2.9% in 2025 and U.S. royalty fees fell in 2024 and 2025 (10-K FY2025, Item 7); (ii) franchise
agreement acquisition payments rose from $17.4M (2016) to $112.2M (2024) and $72.2M in H1 2026 alone against $41.5M in
H1 2025 (cash-flow statements); (iii) the pipeline fell from 1,135 hotels (2019, 10-K FY2019) to 825 (2025); (iv) the
allowance for credit losses on receivables rose from $45.6M (2024) to $51.2M (2025) to $71.1M (2026-06-30), and
receivables from $176.7M to $279.8M (10-Q Q2 2026); (v) the chief executive of nine years stepped down on 2026-05-20 with
no reason given in the 8-K; (vi) the company bought back stock at about $126 (2025) and about $109 (H1 2026) a share,
above today's $103.88.

## THE STANDING RULE
Owning a part-interest bought with cash puts the buyer at no risk of ruin from this name's own conduct; the rule binds the
buyer's financing and sizing, "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and "We are never
going to risk what we have and need for what we don’t have and don’t need" **[M2012-081]**. Nothing here requires
borrowing or a position that could call. The target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as stated.** Understanding is "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, "where the business will be in 10 years" **[M2000-037]**.
- **The business, from Item 1.** "We are primarily a hotel franchisor": 7,575 hotels, 656,825 rooms at 2025-12-31; 6,187
  U.S. hotels with 496,979 rooms produce most of the money (U.S. royalty fees $439.8M of franchise and management fees of
  $673.2M in 2025). The fee is "an initial fee, a percentage-of-revenue royalty fee, and a marketing & reservation fee";
  royalty fees "typically range from 5% to 6% of gross room revenues", marketing and reservation fees "3% to 4%", on
  contracts of "10 to 30 years" with termination rights at "designated anniversaries" and liquidated damages. The
  marketing and reservation fees are a pass-through fund that is meant to break even over time. Seventeen owned hotels and
  a $667.2M programme of investment, loans and guaranties support two newer brands (Cambria, Everhome).
- **The key variables and whether they are foreseeable** **[M1998-044]**: (1) rooms in the system, (2) RevPAR, (3) the
  royalty rate net of what is paid to get it (franchise agreement acquisition costs), (4) the capital put into owned
  hotels, ventures and acquisitions. The first three are filed every year for ten years and move slowly: U.S. rooms
  404,498 (2016) to 462,973 (2019) to 496,979 (2025); U.S. RevPAR $46.01, $47.18, $52.85; royalty rate 4.41%, 4.86%,
  5.14% (10-Ks FY2020 and FY2025). The fourth is a management choice, read at Q3 and Q6. The economic dynamics are plain
  **[M2011-014]**: an owner pays for the brand, the reservation system and the loyalty programme as long as they deliver
  more guests than they cost; the franchisor's costs barely rise with rooms.
- **Do the past statements tell me the future ones** **[M2008-033]**: the fee lines do; the reimbursable fund, the
  capitalized acquisition costs and the owned-hotel programme take reading (Q4) but are disclosed.
- **Is the forecast about customers or technology** **[M2017-019]**: about hotel owners and travellers. Technology enters
  through distribution (online travel agents, AI booking, Item 1A), which is a threat to the castle and belongs to Q2.
- **Would the insiders write it down** **[M2000-105]**: they do: the 2026 outlook gives "Global net system rooms growth
  ~1%" and U.S. RevPAR "-2% to 1%" (earnings release, 2026-02-19). A ten-year forecast is less sure; the industry is old
  and slow-changing, with a franchise model in place since before 1980 in this company.
- **Doubt** **[M2002-092]**: I have no doubt that I understand how the money is made. Where the earning power will be in
  ten years depends on whether the brands keep their owners against richer rivals, which is a castle question (Q2), not a
  question of understanding. A franchisor of roadside and suburban hotels, with ten years of filed system data, is inside
  the perimeter; the risk is "if I think I understand a business and I don’t" **[M1997-024]**, which the Q2 and Q4 reading
  is meant to test.
- **VERDICT: IN.** The economics are knowable and the key variables are filed **[M2012-065]**, **[M1998-044]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now. What are the key factors? And how permanent are they?" **[M1995-038]**.

**The parts table** (business of parts, CONVENTION in the framework). Segment operating income (10-K FY2025, Note 15):

| part | operating income 2023 / 2024 / 2025 ($M) | share of three-year total | castle | decides |
|---|---|---|---|---|
| Hotel Franchising & Management (22 brands, 13 managed hotels) | 508.5 / 584.3 / 603.1 | above 100% | the brand system, below | yes |
| Corporate & Other (17 owned hotels, corporate costs) | (133.5) / (120.5) / (154.7) | a loss | none claimed; a support programme for two brands | no |

Only three years of segment figures are in the FY2025 10-K; the franchising part carries more than all of the operating
income in each, so it decides on any five-year span. The owned-hotel part is carried to Q3 and Q7 as capital spending,
not as a business of its own.

**What the castle is, in the filer's words.** "We believe that hotel operators choose a franchisor based primarily on the
value and quality of each franchisor’s brand(s) and services and the extent to which affiliation with that franchisor may
increase the franchisee’s reservations and profits" (Item 1, Competition). The parts: brand recognition with walk-in and
roadside travellers, a central reservation system and website, a loyalty programme of "more than 74 million worldwide
members", procurement scale, and contracts of 10 to 30 years with liquidated damages. The customer who decides is the hotel
owner; the traveller decides for the owner.

**The castle tests, each with its filing fact.**
1. *Key factors and permanence* **[M1995-038]**. The fee stream has stood through two severe downturns: operating income
   $174.6M (2008), $148.1M (2009), $318.5M (2019), $121.7M (2020, still a profit), $448.4M (2025) (XBRL from the 10-Ks;
   2025 checked against the filed statement). Wyndham and Hilton reported operating losses in 2020 (Wyndham -$46M, Hilton
   -$418M, XBRL). The franchise model does not depend on the genius of the lord: the core brands are decades old.
2. *The attacker with money* **[M2011-015]**, **[M2012-106]**. The attackers are named in Choice's own brand pages: Comfort
   competes with "Hampton by Hilton, Holiday Inn Express, and Fairfield by Marriott"; Everhome and MainStay with "StudioRes"
   and "LivSmart"; WoodSpring with "Extended Stay America, MyPlace, Studio 6, Echo Suites, and LivAway" (Item 1). The two
   largest rivals have far more money and are building brands in Choice's chain scales. The money test is being run against
   Choice now; the answer so far is that Choice has kept its U.S. room count roughly level (below) but pays more to do it.
3. *Pricing power and the agony* **[M2005-020]**. The posted price rose: the U.S. average royalty rate went from 4.41%
   (2016) to 4.86% (2019) to 5.14% (2025) and 5.22% (H1 2026). What Choice pays owners to sign rose faster: franchise
   agreement acquisition payments (cash-flow statements, net of reimbursements) $17.4M (2016), $38.9M (2019), $98.3M
   (2023), $112.2M (2024), $83.4M (2025), and $72.2M in H1 2026 against $41.5M in H1 2025. As a share of U.S. royalty fees
   (a ratio of this run; the payments are global and the fees U.S., so it overstates the U.S. share somewhat): 5.8% (2016),
   10.5% (2019), 21.5% (2023), 24.7% (2024), 19.0% (2025), 33.9% (H1 2026, a seasonal half). The royalty rate net of that
   ratio: about 4.15% (2016), 4.35% (2019), 3.81% (2024), 4.16% (2025). **The price owners pay, net of what Choice pays them,
   has not risen in nine years.** The filer says why: "competition may require us to reduce or change fee structures, make
   greater use of financial incentives, including franchise agreement acquisition costs, loans and guaranties to acquire
   franchisees" (Item 1A). The agony before a price rise is here paid in cash after it.
4. *Unit volume and share of mind* **[M1997-099]**. U.S. rooms 462,973 (2019) to 496,979 (2025), but about 44,000 of the
   2025 rooms are in brands bought with Radisson Hotels Americas in 2022 (Country Inn & Suites 32,333, Radisson 10,090, Park
   Inn 1,294; Item 1 table). The legacy system was therefore about 453,000 rooms in 2025 against 462,973 in 2019, a fall of
   about 2% in six years (this run's subtraction). In 2025 the U.S. system lost 141 hotels and 14,760 rooms (-2.9%): Econo
   Lodge -7.6% of rooms, Quality -4.3%, Comfort -2.0%, Clarion -6.9%, while WoodSpring +10.8% and Everhome grew from 7 to 25
   hotels (Item 7). The pipeline fell from 1,135 hotels (2019, 10-K FY2019) to 825 (2025). In H1 2026 U.S. rooms were
   499,226 against 500,562 a year earlier (-0.3%, 10-Q).
5. *The low-cost position*: not the castle claimed; the filer competes on brand and delivery, not on cost.
6. *The brand in the customer's mind* **[M2008-075]**, **[M2023-073]**. For the roadside traveller the promise is real and
   old: "a significant portion of hotel room nights are sold to guests who either walk-in or contact the hotel directly"
   (Item 1). Against it, "A significant, and increasing, percentage of hotel rooms are booked through internet travel
   intermediaries", and AI booking tools may shift "loyalties from our brands to their travel services" (Item 1A). Where the
   intermediary is trusted as much as the brand, "the value of having the brand moves over to the retailer from the product
   itself" **[M2001-090]**. No instance found in the FY2025 10-K of a filed share of bookings by channel.
7. *Would the customer still choose it over the low bid* **[M2017-009]**. The owner's low bid is a cheaper flag or no flag.
   Liquidated damages from early terminations rose in both 2024 and 2025 ("an increase in liquidated damages resulting from
   the early termination of franchise agreements", Item 7), and owners are paid more each year to sign (test 3). The owner
   does not choose Choice regardless of price.
8. *Ask the competitors* **[M1999-130]**. The company's own act is on the record: Choice tried to buy Wyndham, its closest
   rival, in 2023 and 2024, and terminated the pursuit on 2024-03-08, at a cost of $55.8M (2023) and $17.2M (2024) of
   "business combination, diligence and transition costs" (most of it the pursuit, with Radisson integration in 2023) and an
   $8.3M loss on the Wyndham shares it had bought (Item 7). The silver bullet it chose was to buy its rival.
9. *Widening or narrowing* **[M1999-108]**, **[L2005-010]**. Narrowing in the legacy economy and midscale brands (tests 3,
   4, 7); widening in extended stay (WoodSpring, Everhome) and abroad (international rooms 121,716 in 2021 to 159,846 in
   2025, partly the Canada purchase). The net is a castle that keeps its returns on its old base by spending more each year
   to hold its size.
10. *What could destroy or reduce it* **[M2000-014]**: the owners' economics (U.S. RevPAR fell three years running, $55.19
    in 2023 to $52.85 in 2025; franchisee credit losses rose, Q4); distribution captured by intermediaries; the larger
    chains' new brands in Choice's scales. None is sudden; each is slow.

**The competitor row**, same metrics from the competitors' own filings. The 10-K names competitor *brands*, not companies;
they map to three SEC filers used here: Wyndham Hotels & Resorts (Days Inn, Super 8, La Quinta, Baymont, Ramada, Wingate;
the closest rival by chain scale), Hilton Worldwide (Hampton, LivSmart), Marriott International (Fairfield, StudioRes).
**Flagged, not SEC filers or not used:** Best Western (a membership association, no SEC filings found), Red Roof, Motel 6
and Studio 6, Extended Stay America, InTown Suites, Sonesta (private); IHG (Holiday Inn Express) files a 20-F as a foreign
issuer and was not read; Hyatt (Hyatt Place) is a fourth filer, left out under the brief's limit of three. Metric of this
run: operating income against total assets less cash, goodwill and indefinite-lived brands and trademarks (capitalized key
money and other finite intangibles left in, since they are cash the business put up). It is not a return on net tangible
assets and is not comparable to one.

| company (FY2025 10-K; FY2019 10-K) | system rooms 2019 → 2025 | U.S. rooms 2019 → 2025 | U.S. RevPAR 2019 → 2025 | operating income 2019 → 2025 ($M) | OI / that capital 2019 → 2025 |
|---|---|---|---|---|---|
| Choice (`0001046311-26-000008`; `0001046311-20-000011`) | 590,897 → 656,825 (+11%, Radisson bought 2022) | 462,973 → 496,979 (legacy about -2%) | $47.18 → $52.85 (+12%, mix from Radisson upscale) | 318.5 → 448.4 | 27.2% → 19.4% |
| Wyndham (`0001722684-26-000007`; `0001722684-20-000007`) | 831,025 → 868,900 (+5%) | 510,200 → 505,100 (-1%) | $46.39 → $48.44 (+4%) | 307 → 402 | 20.4% → 29.0% |
| Hilton (`0001585689-26-000007`; `0001585689-20-000013`) | 971,780 → 1,351,351 (+39%) | not compared | not compared | 1,657 → 2,693 | 37.8% → 46.8% |
| Marriott (`0001048286-26-000007`; `0001628280-20-002376`) | 1,380,921 → 1,779,936 (+29%) | not compared | not compared | 1,800 → 4,141 | 18.2% → 34.1% |

Inputs: XBRL Assets, cash, Goodwill, indefinite-lived intangibles (Marriott: total intangibles less finite-lived), Wyndham
trademarks from its balance sheet text ($1,395M 2019, $1,208M 2025); Choice 2019 cash as tagged includes restricted cash
($34M). Two endpoints, not a full series: 2020 and 2021 are pandemic years for all four, so the comparison is between the
last pre-pandemic peak and the latest year. Wyndham's 2025 operating income carries $86M of impairments and $74M of charges
tied to a failed franchisee group (its own reconciliation), so its 2025 figure is depressed, not flattered.

**The field's returns over the last full cycle, in words.** All four earn on the capital this metric counts what a
commodity field does not; the field's returns are high, not ordinary, at both ends of a cycle that included a year in
which two of the four lost money. Choice is the only one of the four whose return on this capital fell from 2019 to 2025,
because its capital grew faster than its income: $1,171M to $2,314M of capital (Radisson, Canada, the owned-hotel and
venture programme, $485.4M of capitalized acquisition payments at 2025) for $129.9M more operating income. The castle
protects excellent returns on the old base; the added capital earns much less (Q3).

**Verdict reasoning.** The castle is standing: the brands and contracts held a high return through 2009 and 2020, the
field's returns are not ordinary **[L2007-004]**, and the deciding part earns all of the profit. It is narrowing in its
largest brands: the net price owners pay has not risen in nine years, the legacy room count is slightly lower than in
2019, the pipeline is more than a quarter smaller, and the incentives that hold the system together are rising faster than
the fees. This is the pattern of an industry that "retains its excellent economics, but has lost still another notch"
**[L1995-023]**, and close to "A moat that must be continuously rebuilt will eventually be no moat at all" **[L2007-005]**,
though the evidence shows the rebuilding holding so far, not failing. On the rows, a castle shown to be filling in closes
OUT **[M2011-015]** and a moat "tenuous in any way" is left alone because "We don’t know how to valuate that" **[M2000-019]**.
I judge that this castle's future can be judged: a fine fee business that holds its size by paying for it, with no real
growth in its legacy brands. That judgment is carried to Q7 as no growth credited beyond what the filings show and as a
wide margin demanded. **Contrary evidence written down** **[M1997-127]**: a stricter reading of "If we can think of very
much that can go wrong with them, we just forget it" **[M2000-016]** would close this file here TOO HARD (NATURE) on the
narrowing; the box at the end does not turn on which reading is taken (Q7).

- **VERDICT: IN**, narrowly, on the deciding part (franchising), with the narrowing carried forward **[M1995-038]**,
  **[L2007-004]**, **[L1995-023]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **The base business.** Franchising needs almost no capital of its own: the filer says "our business has not historically
  required significant reinvestment of capital" (Item 7), and the franchising segment earned $603.1M of operating income in
  2025 on a business whose own property spending ("investments in other property and equipment": leasehold improvements,
  office equipment, capitalized software) was $47.7M, $39.1M and $38.9M in 2023 to 2025. On the capital it needs, this is
  the first kind of business, "more and more money every year without putting up anything to get it, or very little"
  **[M1998-081]**, judged "in terms of the capital actually needed in the business" **[M2010-090]**.
- **What the company now puts in besides.** Four streams, all from the filed cash-flow statements:
  1. *Payments to sign franchisees* (franchise agreement acquisition costs, inside operating cash flow): $38.9M (2019),
     $38.2M (2021), $54.5M (2022), $98.3M (2023), $112.2M (2024), $83.4M (2025), $72.2M (H1 2026). Capitalized net balance
     $419.6M (2024) and $485.4M (2025), gross $645.0M (Note 6).
  2. *Owned hotels, ventures and loans* to support Cambria and Everhome: owned-hotel spending $68.6M, $106.8M, $106.9M
     (2023 to 2025); contributions to affiliates $38.9M, $52.8M, $93.7M less distributions $0.9M, $15.9M, $44.6M; notes
     issued less collected. The programme stood at $667.2M at 2025-12-31 against an authorization of up to $1.2 billion
     (Item 7); the filer expects net outlays to fall to "$20 million to $45 million in 2026" (earnings release).
  3. *Acquisitions*: WoodSpring (2018, $231.3M), an asset acquisition of $169.0M (2019), Radisson Hotels Americas (2022,
     $673.9M purchase price, $550.4M net of cash, plus $56.0M of acquired mortgage repaid), Choice Hotels Canada (2025,
     $114.5M, $73.4M net of cash).
  4. *Buybacks* (Q6).
- **What the added capital earned.** The measure is "what it can earn on incremental invested assets" **[M2000-065]**.
  From 2019 to 2025 the capital counted in the Q2 metric rose from $1,171M to $2,314M, and goodwill and indefinite-lived
  brands from $182M to $559M: about $1.52 billion more, for operating income up from $318.5M to $448.4M, $129.9M. That is
  about 8.5% before tax on the added capital, and less than that if any of the rise came from price inflation on the old
  base, which it did (U.S. RevPAR +12% nominal over the span). The pieces read the same way: (a) the seventeen owned hotels
  earned owned-hotel revenue less owned-hotel expenses of $29.7M in 2025 ($121.4M less $91.7M, Item 7), before depreciation,
  on property and equipment of $649.3M; equity in the ventures lost $14.3M in 2025; (b) the brands bought with Radisson are
  shrinking in the U.S.: Radisson rooms 15,206 (2023), 13,390 (2024), 10,090 (2025); Country Inn & Suites 34,122, 33,771,
  32,333; Park Inn 2,926 to 1,294 in 2025 (Item 7 tables); (c) the payments to sign franchisees bought a U.S. room count that
  is roughly level (Q2, test 4). "We’re not earning a higher rate of return on capital than we were when we started. We just
  put way more capital into the business" **[M2023-081]** is the shape of 2019 to 2025 here, with the return on the added
  capital lower than the old.
- **Reinvestment to stand still and to grow** **[L1999-024]**, **[M2000-144]**. The filer gives no maintenance figure. My
  guess, stated as a guess: maintenance is the "other property and equipment" line (about $39M to $48M a year) plus the part
  of the franchise acquisition payments spent on keeping existing owners, which the filer does not split from the part spent
  on new ones; owned hotels, ventures and acquisitions are growth outlays. On the evidence of Q2, much of the "growth"
  spending is in fact spending to stand still: the system has not grown organically since 2019.
- **The growth arithmetic and its cap.** Return on equity is not a measure here: equity was negative in six of the ten
  year-ends 2016 to 2025 because of buybacks, which is how "you could make return on equity whatever you want"
  **[M1998-017]**. No growth rate above the discount rate is in question; the shown organic growth is about zero (Q7).
- **WEIGHS AGAINST.** The base needs little capital and earns a very high return on it, but since 2019 the company has put
  about $1.5 billion more into the business, in owned hotels, ventures, acquisitions and payments to owners, for about 8.5%
  before tax, with the system no larger organically: the second account of **[L2007-010]** at best for the added money,
  and close to the third where the spending only holds the size.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten year-ends** **[M2025-032]** (`tools/run.py` table, first-filed XBRL, read against the
  filed balance sheets of FY2025 and the 10-Q; $M):

| year-end | assets | equity | cash | receivables | goodwill | intangibles | long-term debt | retained earnings |
|---|---|---|---|---|---|---|---|---|
| 2016 | 852 | (311) | 202 | 107 | 79 | 16 | n/t | 608 |
| 2018 | 1,138 | (184) | 27 | 138 | 169 | 271 | n/t | 795 |
| 2020 | 1,587 | (6) | 235 | 150 | 159 | 304 | 1,059 | 1,024 |
| 2021 | 1,932 | 266 | 512 | 153 | 159 | 312 | 844 (+216 current) | 1,275 |
| 2022 | 2,102 | 155 | 42 | 217 | 219 | 742 | 1,201 | 1,556 |
| 2023 | 2,395 | 36 | 27 | 196 | 220 | 811 | 1,069 (+499 current) | 1,756 |
| 2024 | 2,531 | (45) | 40 | 177 | 220 | 884 | 1,769 | 2,001 |
| 2025 | 2,918 | 181 | 45 | 207 | 306 | 1,082 | 1,906 | 2,318 |
| 2026-06-30 | 2,989 | 142 | 43 | 280 | 303 | 1,106 | 2,002 | 2,377 |

  (n/t: not tagged under the element that year; 2017 and 2019 omitted for width, equity (212) and (24).) **What moved and
  why.** (1) *Equity* is near zero or negative throughout although retained earnings rose from $608M to $2,377M: treasury
  stock at cost reached $2,635.5M at 2026-06-30, so the earnings were paid out in buybacks and dividends and the business
  runs on borrowed money. (2) *Goodwill and intangibles* rose from $95M to $1,388M (2025): the WoodSpring, Radisson and Canada
  purchases (franchise rights $262.7M, trademarks $252.8M, reacquired rights $75.0M, goodwill $305.8M) and the capitalized
  payments to franchisees ($485.4M net). (3) *Debt* rose from about $1.06 billion (2020, 2021) to $2.00 billion (2026-06-30)
  while operating income rose from $428.9M (2021) to $448.4M (2025). (4) *Receivables* rose from $176.7M (2024) to $207.5M
  (2025) to $279.8M (2026-06-30); the allowance for credit losses from $45.6M to $51.2M to $71.1M; write-offs net of
  recoveries $14.4M (2024) and $29.6M (2025); provisions in SG&A $11.0M (2024), $20.2M (2025), $18.1M in H1 2026 alone
  (10-K Note 3, 10-Q Note 3). Part of June's balance is seasonal; the allowance and the provisions are not. "What the figures
  are saying": the owners in the system are paying more slowly and more of them are not paying at all. "What they can't
  say": whether the capitalized payments to owners ($485.4M) will be earned back, since an owner who leaves owes the
  unamortized balance and an owner in distress may not pay it.
- **The real costs.**
  1. *Depreciation and capital spending.* D&A $59.7M (2025) against "other property and equipment" spending of $38.9M; the
     D&A includes amortization of purchased franchise rights and the owned hotels' depreciation, so the maintenance spending
     is the better guide to the cost of standing still in the base, as **[L2015-004]** asks for the cost actually needed.
  2. *Stock pay*, $38.3M (2025), is a real cost **[L2015-003]** and is deducted in owner cash; the company's adjusted EBITDA
     adds it back.
  3. *Payments to franchisees.* GAAP spreads them over 10 to 30 years as a reduction of revenue ($32.0M of amortization in
     2025 against $83.4M of cash paid; $28.7M against $112.2M in 2024), so GAAP operating income ran ahead of cash economics
     by $51M to $84M in those years. Adjusted EBITDA removes even the amortization ("franchisee agreement acquisition cost
     amortization and charges" are excluded, earnings release definition). Owner cash below is built from the cash-flow
     statement, where the payments are charged when made.
  4. *The marketing and reservation fund* ran deficits of $32.8M, $18.2M and $47.1M (2023 to 2025). The filer says the fund
     should break even over time and franchisees must reimburse deficits; three deficits in a row are cash the company has
     spent. Adjusted EBITDA excludes them; owner cash includes them, as the cash flow does.
  5. *Restructuring and deal costs* recur: "business combination, diligence and transition costs" $55.8M (2023), $17.2M
     (2024), $4.7M (2025); "we do not ask you to forget about those costs" **[M1999-023]**, and they stay in.
  6. *Tax.* Effective rate 19.0% (2025, lowered by the non-taxable $100.0M gain on remeasuring the Canada stake) and 24.3%
     (2024); cash income taxes paid $84.7M (2025, federal net of purchased transferable credits, plus state and foreign). The
     company has committed to buy about $179M of transferable solar tax credits through 2036 (10-Q Note 11): it pays cash for
     a discount on its tax; the payments are in operating cash flow, so owner cash already carries both sides.
  7. *Non-recurring items in GAAP net income* that owner cash ignores: the $100.0M gain of 2025 (non-cash), a $67.4M
     WoodSpring contract termination receipt in 2022.
- **EBITDA in the filer's own mouth.** "Adjusted EBITDA reached a company record $625.6 million for full-year 2025"
  (earnings release, 2026-02-19), defined to exclude share-based compensation, the amortization of payments to franchisees
  and the fund's deficits, against GAAP operating income of $448.4M and owner cash after all spending far lower (Q7). The
  rows: "bullshit earnings" **[M2003-109]**; "a figure calculated after interest, taxes, depreciation, amortization and all
  forms of compensation" **[L2021-003]**. The release also gives guidance for 2026 (net income, adjusted EBITDA, adjusted EPS,
  RevPAR, rooms). Both habits weigh against here and are carried to Q5 **[L2016-006]**, **[L2019-006]**.
- **The tells in the accounts** **[M1995-064]**: a deferred asset building (the capitalized payments, $485.4M and rising)
  and receivables and their allowance rising faster than revenue. Both are disclosed, with their policies and their cash
  plainly on the cash-flow statement; the accounts do not confuse me and do not hide the cost, they report it over time. I
  read them as the tells of a business paying more to hold its owners and carrying more owners who struggle to pay, not as
  accounts dressed up. "We regard it is a negative when we find a management that’s preoccupied with accounting
  considerations. But, we find it so frequent that we can’t afford to use it as a total exclusionary factor" **[M1994-018]**.
- **The recast earnings for Q7.** Owner cash = operating cash flow (which already charges the payments to franchisees, the
  fund's deficits, working capital and cash taxes) less stock pay less capital spending, in two cases: maintenance only
  (other property and equipment and intangibles), and all spending (adding owned hotels, ventures net of distributions,
  notes net of collections, and, in the default pair, acquisitions net of sale proceeds). Table at Q7.
- **VERDICT on the accounts: WEIGHS AGAINST** (no STOP; neither confusion **[M1995-063]** nor suspicion of the statements
  **[M1995-065]** found). GAAP earnings overstate the cash the owners can take out, the company features an adjusted figure
  that leaves out three real costs, and the receivables show stress; all of it is readable from the filings.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** The Bainum family and trusts own "approximately 43% of outstanding shares" (DEF 14A 2026); Stewart W. Bainum Jr.,
  79, has chaired the board since 1987 (with a gap in 1996 to 1997) and is paid $500,000 a year, $350,000 of it in stock;
  his nephew Brian B. Bainum is a director. The chief executive since 2017, Patrick Pacious, "will step down" effective
  2026-05-20 (8-K `0001193125-26-232581`), with no reason stated, and left the board on 2026-08-31; Dominic Dragisich,
  CFO from 2017 to 2023 and since then head of operations, brands and strategy, was made interim and then permanent CEO
  (8-K `0001193125-26-375580`). The CFO since 2023 has been at the company since 2002.
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt*: the hand was a franchise system of
  forty years' standing in a field whose returns are high (Q2). Against the closest rival dealt a similar hand, Wyndham's
  operating income rose from $307M to $402M (2019 to 2025) with no large acquisition after 2018; Choice's rose from $318.5M
  to $448.4M after about $1.5 billion more capital (Q3). The added capital was allocated poorly: owned hotels and ventures
  earning little, a $673.9M purchase whose U.S. brands are shrinking, a failed attempt to buy Wyndham that cost about $81M in
  deal costs and a share loss, and buybacks at prices above value (Q6). *How they treat owners*: dividends steady ($1.15 a
  share), buybacks large, disclosure full and in places candid (Item 1A states plainly that competition forces more
  incentives and that owned hotels may be "disruptive to our asset-light business model").
- **The proxy: how they treat themselves against the owners** **[M1994-009]**. Chief executive pay $8,074,700 for 2025, 81
  times the median employee. A "$30 million one-time Strategic Leadership Alignment Grant" to the chief executive in 2022,
  vesting 10%, 20% and 70% in years three to five. The annual bonus is paid on operating income "adjusted by the Committee
  based on approved exceptions" ($519.0M for bonus purposes against GAAP operating income of $448.4M; the exceptions include
  the fund's results, restructuring and severance, and "M&A due diligence and transition costs in excess of budget") and on
  revenue; it paid 95.6% of target in a year when U.S. royalty fees and GAAP operating income fell. Stock awards vest on
  three-year cumulative EPS, which buybacks raise, with a relative TSR modifier; no element is tied to the capital employed
  or the return on it, contrary to "tying performance to what is actually under the reasonable control of the person"
  **[M2003-019]** in its capital half. The departing chief executive receives 200% of salary and target bonus, two more years
  of vesting, health payments to 2032 and a hotel-stay benefit of $25,000 a year to 2037 (8-K). Related-party dealings are
  small and disclosed: Sunburst, controlled by the Bainums, pays about $1.8M of fees on eight hotels and received $512,500 of
  franchise incentives in 2025, on legacy terms; aircraft leases to family members at cost, with no family flight hours in
  2025; the chairman's office space $112,500.
- **The letters and the reports.** The 10-K's business and risk sections tell an owner what an owner would want to know,
  including the weaknesses. The earnings release leads with "record" adjusted EBITDA (Q4) and gives guidance.
- **The habits carried from Q4**, read with the integrity record. Adjusted EBITDA featured over GAAP, defined to leave out
  stock pay, the payments to franchisees and the fund's deficits; adjusted EPS; annual guidance; a bonus measured on an
  adjusted operating income. "A management that regularly attempts to wave away very real costs by highlighting "adjusted
  per-share earnings" makes us nervous" **[L2016-006]**; guidance is "the scourge" that encourages managers "who wish to game
  numbers" **[L2019-006]**; these are among "things that they do in public in relation to their investors and the promises
  they make" **[M2004-067]**. Against them: every adjusted figure is reconciled to GAAP in the release; the cash-flow
  statement shows each excluded cost in full; no restatement, no material litigation (Item 3), and no sign in the filings
  read of reserves moved, of figures that dance, or of a target always met (the 2025 bonus paid below target, 95.6%). I do
  not find dishonesty; I find a management that presents its business in the industry's adjusted language and pays itself
  on that language. Doubt, in the sense of **[M2013-088]**, is about trust in the people; the record read gives me no ground
  to distrust their honesty, and I do not invent one. The habits are weighed against the people's judgment, not their
  integrity.
- **Love of the business, and after the sale.** A family that has owned and chaired the company for four decades and never
  sold (the Bainums' 43% is the record) loves the business on the evidence of conduct; the managers are long-tenured
  insiders. Not a whole-business purchase, so the after-the-sale test does not apply **[M2007-081]**.
- **Contrary evidence written down** **[M1997-127]**: the sudden departure of the chief executive with no reason given is
  unexplained in the filings; a reader may treat it as a fact owed an explanation. It is recorded, not weighed as integrity
  evidence, since the filings give no fact about its cause.
- **VERDICT on integrity: IN** **[M2015-047]**, **[M1994-009]**; **ability WEIGHS AGAINST**: operations competent, capital
  allocated poorly since 2019 and pay tied to adjusted and per-share measures rather than to the capital employed
  **[M1994-008]**, **[M2003-019]**, **[L2016-006]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**. Over 2021 to 2025 net income totalled $1,549M; the company paid out
  $1,330M in buybacks and $243M in dividends, $1,573M, more than it earned, while debt rose from about $1.06 billion
  (2021-12-31) to $1.91 billion (2025-12-31) and $2.00 billion (2026-06-30), and the owned-hotel programme, the payments to
  franchisees and two acquisitions took the rest of the cash. The test is therefore not whether earnings kept became more
  than a dollar, but whether the borrowed and reinvested money did. Shares outstanding fell from 55,535,554 (2020-12-31,
  10-K FY2020) to 45,008,622, about 19% fewer, bought at about $117 to $124 a share; today's price is $103.88, below every
  year's average price paid, and owner cash before interest has not grown with the capital put in (Q3, Q7). On the market
  leg and on the business leg the money kept and borrowed since 2021 has not yet shown up as more than a dollar of value
  per dollar. "Almost any management that wants to retain money is going to rationalize it" **[M1998-110]**.
- *Buybacks* **[L1999-023]**, **[L2011-003]**. Average prices paid, from the filed statements of equity: about $119 (2021,
  0.11M shares), $117 (2022, 3.70M), $120 (2023, 3.04M), $122 (2024, 3.11M), $124 (2025, 1.09M including employee
  redemptions), about $109 (H1 2026, 0.9M, 10-Q). The programme is an authorization of a number of shares (5 million added
  on 2024-03-11), with no price named above which it stops **[L2016-002]**, and it was partly paid for with borrowed money in
  2022 to 2025. **Buyback price test (written back from Q7):** every year's average price paid (about $109 to $124) sits
  above the bottom of the Q7 range ($23.63 a share, central, all-equity) and above its top ($60.29); on the equity-only
  basis too (top $88.03). The purchases are therefore read by the rule for a buyback with no stated price, and weigh
  against: "Continuing shareholders are hurt unless shares are purchased below intrinsic value" **[L2011-003]**.
- *Issuance and deals* **[L2014-012]**, **[M2007-123]**. No shares issued in a deal. The 2023 exchange offer for Wyndham
  proposed "$49.50 in cash and 0.324 shares of Choice common stock per Wyndham share", the share part valued at "$40.50" on
  Choice's then price (about $125 a share), at "a 14.9x multiple of Wyndham’s consensus 2023 adjusted EBITDA estimate"
  (8-K exhibit 99.2, `0001193125-23-293430`). It did not close, so the STOP for an all-stock deal in undervalued stock does
  not arise **[L2009-019]**; it is recorded as the board's view of value given against value got. Radisson ($673.9M) and
  Canada ($114.5M) were paid in cash, borrowed in part; Radisson's U.S. brands have shrunk since (Q3). Stock pay dilution is
  small (option exercises and vesting, about 0.1M to 0.4M shares a year, against 0.1M to 3.7M bought).
- *Dividends and cash.* A steady $1.15 a share; cash is kept near $40M to $60M and the revolver is the reserve.

**Part B: the pay, the board and the owners.**
- *Pay* (Q5): the annual bonus on an adjusted operating income and on revenue; stock awards on three-year cumulative EPS,
  which the buybacks raise; a one-time $30M grant to the chief executive in 2022; nothing tied to the capital employed or
  to the return on the added capital **[M2003-019]**. A pay plan that rewards per-share earnings while the share count is
  bought down with borrowed money pays whatever happens to the return on capital, close to "heads I win, tails you lose"
  **[L1994-020]** in effect if not in design.
- *The board* **[M2007-120]**: twelve directors, a majority independent; the controlling family holds true, long-held
  ownership **[L2002-033]**, the best partnership fact in the file. The board backed a hostile bid for the closest rival at a
  price it described as a multiple of an adjusted figure, and approved buybacks at prices above value (below).
- *Owners as partners*: full GAAP reconciliation and candid risk factors; against them, guidance and adjusted figures each
  quarter (Q4, Q5).

- **Part A: WEIGHS AGAINST**: about $1.6 billion paid out in five years, more than was earned, partly on borrowed money and
  largely in buybacks with no stated price at prices above the value range, while the reinvested and borrowed money raised
  operating income little **[L2011-003]**, **[L2016-002]**, **[M1998-110]**.
- **Part B: WEIGHS AGAINST**, with the family's ownership for it: pay rewards adjusted and per-share figures, not the return
  on the capital the company keeps adding **[M2003-019]**, **[L1994-020]**, **[L2002-033]**.

## Q7 — WHAT IS IT WORTH? STOP.
"How certain are you that there are indeed birds in the bush? When will they emerge and how many will there be? What is
the risk-free interest rate" **[L2000-021]**; value is "the discounted value of the cash that can be taken out of a
business during its remaining life" **[R1996-018]**, at the long government rate, 5.56% **[M1996-025]**.

**Owner cash by year** ($M; script `Test Runs/_research 2026-10-14 CHH/oc.py`, every input from the filed cash-flow
statements and the share-based compensation notes of the 10-Ks listed at Step 0). OCF already charges cash taxes, working
capital, the payments to franchisees and the fund's deficits. *Maintenance* = other property and equipment plus
intangibles where the filer splits them (2023 to 2025: $49.7M, $39.1M, $38.9M); before 2023 the filer gives one property
line that includes hotel development, and the maintenance guess is the 2023 to 2025 average, $42.6M (**CONVENTION of this
run**: the filer gives no split before 2023, and the three split years are the only filed measure of the base's own
spending). *Programme* = the rest of property spending plus contributions to affiliates less distributions plus notes
issued less collected. *Acquisitions* = businesses and assets bought net of cash, including the $56.0M Radisson mortgage
repaid in 2022, less sale proceeds. Interest is added back at 76% of interest paid for the all-equity basis (**CONVENTION
of this run**: a 24% shield, between the filed effective rates of 19.0% and 24.3%).

| year | OCF | stock pay | maintenance | programme | acquisitions net of sales | owner cash, maintenance only | after programme | after programme and acquisitions |
|---|---|---|---|---|---|---|---|---|
| 2016 | 152.0 | 14.6 | 42.6 | 37.7 | 18.4 | 94.8 | 57.1 | 38.7 |
| 2017 | 257.4 | 24.9 | 42.6 | 48.3 | (1.0) | 189.9 | 141.6 | 142.6 |
| 2018 | 242.9 | 15.0 | 42.6 | 46.1 | 231.4 | 185.3 | 139.2 | (92.2) |
| 2019 | 270.6 | 16.6 | 42.6 | 36.5 | 169.1 | 211.4 | 174.9 | 5.8 |
| 2020 | 110.1 | 7.2 | 42.6 | (9.6) | (9.2) | 60.3 | 69.9 | 79.1 |
| 2021 | 383.7 | 23.4 | 42.6 | 42.1 | (6.1) | 317.7 | 275.6 | 281.7 |
| 2022 | 367.1 | 40.5 | 42.6 | 58.7 | 396.0 | 284.0 | 225.3 | (170.7) |
| 2023 | 296.6 | 40.5 | 49.7 | 100.0 | 0.0 | 206.4 | 106.4 | 106.4 |
| 2024 | 319.4 | 38.4 | 39.1 | 149.6 | 0.0 | 241.9 | 92.3 | 92.3 |
| 2025 | 270.4 | 38.3 | 38.9 | 155.5 | 21.4 | 193.2 | 37.7 | 16.3 |

(2022 sale proceeds of $211.3M are three Cambria hotels, land, an international market conversion and the $44.7M basis of
terminated WoodSpring contracts; the 2019 line includes a $169.0M asset acquisition and a $10.8M disposition payment.
In 2020 total property spending ($35.0M) fell below the maintenance guess, so the programme shows negative that year.
Depreciation variant beside: D&A averaged $42.4M over 2021 to 2025 against the $42.6M maintenance guess, so the variant
changes nothing material.)

**The specifics, applied.**
- *(a) Cycles.* The literal window is 2021 to 2025. Both end years are aberrational on the filer's own words: 2020 spending
  was "Eliminated, reduced or deferred" during the pandemic (10-K FY2020) and 2021's operating cash rose on "an increase in
  operating income ... and timing of working capital items" (10-K FY2021), with payments to franchisees at $38.2M against
  $98.3M to $112.2M two years later; 2025's operating cash fell on "the timing of working capital items, the final
  installment payment made in 2025 for the one-time transition tax ... and the cash paid for the purchase of transferrable
  tax credits" (10-K FY2025), a single year's draw tied to named events (specific (d)). The cycle is read on owner cash
  (maintenance only), the series the specific names: $211.4M (2019, the last pre-pandemic high), $60.3M (2020, the trough),
  then $317.7M, $284.0M, $206.4M, $241.9M (2021 to 2024, 2024 the latest high before the 2025 draw). The base is the last
  full cycle peak to peak, **2019 to 2024**, with the literal window shown beside.
- *(c) Acquisitions; the serial acquirer.* Net purchases over the window, $680.7M (Radisson with its mortgage, Canada),
  exceed half of owner cash before purchases ($1,243M maintenance-only, half $621.5M): the central figure is the organic
  pair, purchases left out and organic growth only. The default pair (purchases deducted, total growth credited) is beside.
- *(b) Decline.* Organic growth as the filer reports it: U.S. royalty fees, with no U.S. acquisition after 2022, were
  $458.1M (2023), $454.7M (2024), $439.8M (2025), **-2.0% a year**; global net rooms grew 1.2% in 2025 and are guided "~1%"
  for 2026, with U.S. RevPAR guided "-2% to 1%" (earnings release). The negative rate is carried as the bottom.
- *(e) Growth spending.* The filing allows the maintenance guess, so the top of the range is owner cash after maintenance
  only, at no growth; the programme's spending is charged in the bottom case, against the growth it bought, which on the
  filed evidence is none. The inversion is the finding **[L2000-023]**.
- *(f) The cap.* No rate above the discount rate is carried; nothing needs cutting.
- *(d) Working capital* is inside operating cash flow every year.
- **Net debt** (all-equity basis): long-term debt $2,002.3M less cash $42.8M at 2026-06-30 (10-Q) = **$1,959.5M**;
  operating lease liabilities (about $104M non-current) left out; the employee-plan investments ($54.8M) held against
  deferred compensation of $61.1M left out. The 10-Q states no subsequent event; the $500M term loan of 2026-08-28 (8-K)
  is for "general corporate purposes, including working capital, debt repayment", so net debt is taken as unchanged by it.
  Shares 45.009M. Price $103.88: market value $4,675.5M, market value plus net debt $6,635.0M.

**The range** (per share, all-equity basis, 5.56%, ten years then zero nominal growth; script `val.py`):

| case | base owner cash before interest ($M) | growth | value / share | equity-only beside | return at $103.88 (all-equity) |
|---|---|---|---|---|---|
| **TOP**: maintenance only, no growth, cycle 2019-2024 | 259.8 | 0% | **$60.29** | $88.03 | 3.9% |
| **BOTTOM**: after programme, organic decline, cycle | 196.9 | -2.0% | **$23.63** | $53.69 | 2.5% |
| beside: maintenance only, organic decline, cycle | 259.8 | -2.0% | $45.08 | $75.14 | 3.3% |
| beside: literal window 2021-2025, top | 295.6 | 0% | $74.60 | $99.36 | 4.5% |
| beside: literal window, bottom | 194.4 | -2.0% | $22.79 | $50.30 | 2.4% |
| beside: default pair (acquisitions deducted), total growth between halves +10.4% | 105.3 | +10.4% | $52.53 | $60.00 | 3.8% |
| beside: guided ~1% rooms growth on the top case | 259.8 | +1.0% | $68.87 | $95.30 | 4.3% |

**The floor, tested first** (CONVENTION, Q7). Every case above earns between about 2.4% and 4.5% on the price on the
all-equity basis, and between about 2.6% and 5.3% on the equity alone; **no case earns the floor of about ten percent**.
"We don’t want to buy equities where our real expectancy is below 10 percent" **[M2003-149]**: the file closes OUT whatever
the width. (Default-pair growth: owner cash after acquisitions changes sign, so growth is measured between the halves 2016-2020
and 2021-2025, $68.4M to $112.2M before interest, +10.4% a year; the base shown is the cycle average.) (Width for the record: top over bottom 2.6 to 1 on the cycle base, 3.3 to 1 on the literal window.) The price
is above the top of the range on every case, all-equity and equity-only alike, so it would also close OUT under the
range convention's own rule for a price above the top.

**Value range: $23.63 to $60.29 a share** (central, all-equity, cycle base 2019-2024) **against $103.88. Closes: OUT** (no case earns
the floor; the price is above the top).

**Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and averaged, after the
company's own tax, less net debt (the bottom case is worth less than the net debt at ten percent, -$5.28 a share, and
is averaged as it stands): **$4.46 a share on the all-equity basis (the central figure)**; **$39.76 a share on the
equity-only basis** (owner cash after interest against market value) beside it. The gap between the two is the debt: the
lenders are paid about 4.5% after tax, so on the equity-only figure the owner keeps the spread between the floor and the
cost of the borrowing, which the all-equity basis refuses to credit **[L2017-004]**. On the literal window the two figures
would be $8.19 and $41.95. No cheap price is reported.

- **VERDICT: OUT** **[M2003-149]**, **[L2000-021]**: at $103.88 the business would have to grow its owner cash at rates its
  own filings do not show to earn the floor, while its organic fee stream in the U.S. is shrinking. "You can turn any
  investment into a bad deal by paying too much" **[M2019-015]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT). Facts under AFTER THE STOP.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts under AFTER THE STOP.

---
## THE BOX
**OUT, at Q7**: no case of the range earns the floor at the price; value range **$23.63 to $60.29 a share** (central,
all-equity, cycle 2019-2024; equity-only top $88.03) **against $103.88**. Fair price $4.46 all-equity (central), $39.76
equity-only. Q1 IN; Q2 IN narrowly (the castle stands and narrows; a stricter reading would have closed it TOO HARD
(NATURE) there, with the same practical result); Q3, Q4, Q6 weigh against; Q5 integrity IN, ability against. A research
pass is not written: no case of the range earns the floor at the price (Part VII, when a research pass is run).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2), each with its source **[M1997-127]**.)*
- **Q8, the bond.** The 30-year Treasury yields 5.56% (2026-10-13, Treasury par curve); every case of Q7 returns 2.4% to
  4.5% on the price, all-equity, and 2.6% to 5.3% on the equity alone.
- **Q9, debt and exposures.** Long-term debt $2,002.3M at 2026-06-30 (10-Q): senior notes $400M at 3.70% due 2029-12-01,
  $450M at 3.70% due 2031-01-15, $600M at 5.85% due 2034-08-01; revolver of $1 billion to 2029-06-28 ($469.8M drawn at
  2025-12-31, more in 2026); a $500M term loan entered 2026-08-28 maturing 2029-08-28 (8-K). Covenants: leverage not above
  4.5 to 1 (5.5 after material acquisitions); leverage reported 2.86x at 2025-12-31 on the credit agreement's own measure.
  Interest expense $91.1M against operating income of $448.4M (2025), and against income before taxes of $456.9M which
  includes a $100.0M non-cash gain. Variable-rate debt $472.6M at 5.22% (Item 7A). Guaranties: up to $40.4M of venture debt
  and an $18.2M owner's-priority guarantee on seven managed hotels (10-Q Note 11); a commitment to buy about $179M of solar
  tax credits through 2036. Franchisee credit: allowance $71.1M at 2026-06-30. About seven-tenths of the debt (the 2029 notes, the revolver
  and the 2031 notes) falls due in 2029 to 2031, before the term loan is counted, and the company "expects to refinance its fixed and variable long-term debt obligations prior to their scheduled
  maturities" (Item 7A).
- **Q12.** The business is hotel franchising; none of the businesses the rows name. Item 1A lists "human trafficking" among
  the areas in which franchisees' conduct can damage the brands; no instance found in the filings read of a case against the
  company.
- **Q5 facts after the verdict** (already judged at Q5, recorded for a later run): the chief executive's departure on
  2026-05-20 is unexplained in the 8-K; the CHRO leaves at the end of 2026 (8-K 2026-10-01).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit b221b61b); written question by question; committed after each
      (Step 0 and Q1, Q2, Q3, Q4, Q5, Q6, Q7 with the Q6 line written back, the close).
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (seen present
      in `Screens/_daily/`, not touched). Folding into the register is the dispatcher's step; until then the run binds
      nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed by intent or searched. Seen by accident and
      declared above: a commit subject naming a ratio for Choice inside another company's fold, and the names of other runs
      dated today in a directory listing. Neither was used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check
      script `Test Runs/_research 2026-10-14 CHH/check_ids.py`); every filing fact carries its document and accession at
      Step 0 or where it is used; no E-ids.
- [x] The order was kept; the first failing STOP (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy (operator rule 5); stock
      pay deducted; the sovereign from the US Treasury; the price an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations, Q2, Q5); facts for later questions under AFTER THE STOP. No
      integrity flag is needed in the box line: Q5 was reached and judged.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its "SBC+other" alternate was rejected as double counting and
      its capex line was found to omit owned-hotel spending (Step 0).
- [x] `python tools/check_framework.py` PASS before the final commit (result at the foot of the file).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q2 has no rule for a castle that is standing and narrowing at once.** The rows give OUT for a castle shown to be
filling in **[M2011-015]** and the box of the unvaluable for a moat "tenuous in any way" **[M2000-019]**, and they also
record a franchise that "retains its excellent economics, but has lost still another notch" **[L1995-023]**, which Buffett
kept. Choice's net price after incentives is flat for nine years, its legacy room count slightly down and its returns
still high; I judged IN and carried the narrowing to Q7, and said where a stricter reader would close TOO HARD. The text
should say which of the three readings governs a narrowing castle whose returns remain high. (2) **Payments to win
customers inside operating cash flow.** Franchise agreement acquisition costs are part growth spending (new owners) and
part maintenance (keeping owners), but they sit in operating cash, so specific (e)'s maintenance-only case charges them in
full and cannot separate them; the framework's specifics speak only of capital spending. I charged them in every case and
said so. (3) **Specific (a) defines the cycle on owner cash, which here has a pandemic trough and a rebound inside six
years;** "peak to peak" on that series gave 2019 to 2024 by my reading, but 2021 is also a local peak, so the choice of
peaks is a judgment the text does not fix. I showed the literal window beside. (4) **The serial-acquirer threshold
compares purchases with owner cash "before purchases" without saying which owner cash** (maintenance-only or after all
spending); the test passed on both here, but on another name the choice would decide the central pair. (5) **The fair price
on the all-equity basis can be near zero for a leveraged franchisor** ($4.46 here against $39.76 equity-only) because the
bottom case is worth less than the net debt at ten percent; Part VII averages the two ends as they stand, which I followed,
but the text does not say whether a negative end is averaged or floored at zero. (6) **The brief's competitor rule** ("the
rivals the 10-K itself names") meets a 10-K that names competitor brands, not companies; I mapped brands to their SEC filers
and said so.

---
*Checks at the close, 2026-10-14: `python tools/check_framework.py` PASS; `check_ids.py` (no E-ids; 81 distinct v5 ids, all in `principle_ledger_v5.csv`; quoted fragments beside ids found in their rows, 18 by the strict pattern and 23 more by hand-listed spot check in `spot.py`, 0 problems).*
