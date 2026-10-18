# Company Run — Brookfield Infrastructure Corporation (NYSE, TSX: BIPC) — 2026-10-17
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

Dispatched blind run under the canonical brief (`Screens/_daily/_dispatch_brief.md`, slots filled by the dispatcher; the
brief's stated departure: the lines of evidence are derived by the analyst from the 20-F's Items 4.B, 3.D, 5 and 7.B).
Working folder: `Test Runs/_research 2026-10-17 BIPC/` (notes, extraction scripts, the arithmetic file `q7_calc.py` and
its output; raw filings are gitignored and re-fetchable from EDGAR by the accessions below).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed (56a56bf4): `PORTFOLIO.md` read for this one ticker; the operator does not hold BIPC (no line names BIPC, BIP or Brookfield Infrastructure; the Brookfield lines there are BN, Brookfield Corporation, a different issuer).*

**Contamination declared (the blind rule).** Seen by accident, not used: (1) a directory listing of `Test Runs/` taken to
check that the dated file name was free showed the names of thirty-six other run files and research folders dated
2026-10-17 (none for BIPC, BIP or any Brookfield name; none opened); (2) the session's git status and recent commit
subjects (the BROGF run of the same day; nothing on this name); (3) the project memory index loaded with the session,
whose lines mention a count of gate-clearers and holding reviews owed without naming this company. Nothing else from a
blind-listed file was seen.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **What is bought, read before the price.** A BIPC class A exchangeable subordinate voting share. Per the 20-F for 2025
  (accession `0001788348-26-000001`, filed 2026-03-17), Item 4.A: "The exchangeable shares of our company are structured
  with the intention of being economically equivalent to the units of the partnership", by "identical dividends and
  distributions" and an exchange "at the option of the holder for one unit of the partnership at any time"; and "In making
  an investment decision relating to our securities, investors should carefully consult the documents prepared by the
  partnership." Item 10.B: the exchange is paid in one unit or its cash equivalent "the form of payment to be determined
  at the sole discretion of our group"; on a liquidation of BIPC, "If [...] the assets of our company are insufficient to
  make such payment in full, then the assets of our company will be distributed among the holders of exchangeable shares
  ratably"; the class B shares, all held by the partnership, take "the residual value in our company after payment in
  full of the amount due to holders of exchangeable shares". Item 3.D: "The Rights Agreement terminated on March 31,
  2025 [...] In the event that our company or the partnership fails to satisfy a request for exchange, a tendering holder
  is no longer entitled to rely on the secondary exchange rights." **So the business behind the share is Brookfield
  Infrastructure Partners L.P. (BIP, CIK 1406234) as a whole, read through its own filings, with BIPC's own assets as the
  legal backing of the exchange.** BIP's 20-F for 2025 (accession `0001406234-26-000002`, filed 2026-03-17) and its Q2
  2026 interim report on 6-K (accession `0001406234-26-000006`, filed 2026-08-05) were therefore read as primary filings.
- **The pending change of instrument.** Arrangement agreement among BIP Inc., BIP and BIPC dated 2026-07-21 (6-K of
  2026-07-28, accession `0001104659-26-087546`, exhibit 99.1); circular on 6-K of 2026-08-31 (accession
  `0001104659-26-103589`, exhibit 99.2). Press release of 2026-10-14 (6-K of 2026-10-15, accession
  `0001171843-26-006637`): BIP unitholders approved; BIP's conversion "is not conditional on approval by shareholders of
  [BIPC]"; the BIPC meeting is on 2026-10-29; if BIPC holders approve, each share becomes a class A share of BIP Inc.; if
  not, "the BIPC exchangeable shares will remain outstanding and will become exchangeable on a one-for-one basis for BIP
  Inc. Class A Shares". Either way the economic claim stays one unit of the same group. A signed, unclosed corporate
  change, not a deal for a business; it changes no cash stream and is written down, not valued (no figure for it).
- **Price:** $37.74 (close 2026-10-16; `tools/sources.py` price function, an aggregator quote, flagged per operator rule 5).
  BIP units closed $37.45 the same day (same source, flagged): the share trades about 0.8% above the unit it is exchangeable
  for.
- **Shares by class** from the latest filing's cover: 119,982,167 exchangeable shares and 31,909 class B shares
  (`python Screens/cover_shares.py BIPC`: 20-F filed 2026-03-17, period 2025-12-31, accession `0001788348-26-000001`). The
  tool adds the two classes; the sum is not a share count, because the class B shares are the partnership's residual claim
  and are not economically one unit each in the way the exchangeable shares are (Item 10.B). Checked against later
  filings: Item 10 of the same 20-F gives 122,406,667 exchangeable shares and 13,012,789 class A.2 exchangeable shares (of
  BIHC, held by Brookfield) at 2026-03-12; the Q2 2026 6-K (accession `0001788348-26-000005`, filed 2026-08-05), financial
  statements note: "123,005,386 exchangeable shares (2025: 119,982,167) and 13,012,789 class A.2 exchangeable shares",
  after "2,982,920 BIPC exchangeable shares" issued under the at-the-market programme in the first half of 2026. The count
  that matters for value is the group's: BIP's Q2 2026 report gives average units outstanding of 791.7 million for the
  quarter (limited partner, general partner, Redeemable Partnership, Exchange LP, BIPC Exchangeable LP units, BIPC
  exchangeable shares and class A.2 shares, all economically one unit each).
- **Market cap:** the BIPC class, 123.0 million × $37.74 = $4,642M; the group on which value is earned, 791.7 million ×
  $37.74 = $29,879M (at the BIP unit price the group is $29,649M).
- **Sovereign for the earnings currency:** 5.43%, US Treasury daily par yield curve, 30-year, 2026-10-16
  (`python tools/sources.py`, issuing authority). BIPC and BIP report in US dollars; the operating earnings are in many
  currencies (US, Canada, India, U.K., Brazil, Colombia, France and others; BIP 20-F, segment note, revenue by geography),
  and the brief and the protocol take the reporting currency's sovereign. Written down as a limit: no single sovereign
  matches a multi-currency stream.
- **Filings read** (operator rule 4): BIPC 20-F for 2025 (`0001788348-26-000001`, 2026-03-17), Items 3.D, 4, 5, 7.B, 10
  and 18; BIPC 20-Fs for 2020 to 2024 (`0001628280-21-002159`, `0001628280-22-005591`, `0001628280-23-008524`,
  `0001628280-24-011578`, `0001628280-25-014377`) for the balance sheets; the BIPC prospectus of 2020-03-13 (424B3,
  `0001193125-20-071782`), fetched, used only for the history of the special distribution; BIPC Q2 2026 6-K
  (`0001788348-26-000005`); BIP 20-Fs for 2016, 2018, 2020, 2021, 2022, 2023, 2024, 2025 (`0001047469-17-001344`,
  `0001628280-19-002303`, `0001628280-21-005114`, `0001628280-22-005592`, `0001628280-23-008523`,
  `0001628280-24-011576`, `0001628280-25-014380`, `0001406234-26-000002`); BIP Q2 2026 interim report
  (`0001406234-26-000006`); the arrangement agreement, the circular and the press releases of 2026-07-21, 2026-07-30,
  2026-10-09 and 2026-10-14 (6-Ks `0001171843-26-004805`, `0001171843-26-005054`, `0001171843-26-006569`,
  `0001171843-26-006637`). A foreign private issuer files no proxy; the board and fee arrangements are read from Items 6
  and 7 of the two 20-Fs. Triton International Ltd (CIK 1660734), a BIPC subsidiary that still files with the SEC, was read
  through its XBRL company facts only (10-K data 2014 to 2021, tagged, not cross-checked; flagged as transcription).
  **One figure cross-checked against the filed statement:** BIP's 2025 FFO of $2,627 million in the MD&A key-measures
  table equals the FFO total of the audited segment note (F-33 of the same 20-F); and the cover count 119,982,167 read by
  `cover_shares.py` from tagged data equals the comparative figure printed in the Q2 2026 6-K's share note.
- `python tools/run.py BIPC` arithmetic lines only: **the tool failed on this 20-F filer** ("no overlapping OCF/D&A/capex
  annual facts. UNRESEARCHED"; output in `run_py.txt`). Every figure below is taken from the filed statements and the
  filer's own MD&A tables, by the extraction scripts in the research folder. **Owner cash** (built at Q4 and Q7, the group's
  share, US$ millions, from BIP's own tables: FFO less maintenance capital spending less the general partner's incentive
  distributions, with interest added back for the all-equity basis):

| Year | FFO | Maint. capex | AFFO | Growth capex | Interest (BIP share) | IDR | Owner cash, equity basis (AFFO less IDR less pref.) | Owner cash before interest (AFFO + interest less IDR) | D&A, BIP share |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 1,733 | 321 | 1,412 | 1,153 | 755 | 206 | 1,139 | 1,961 | 1,144 |
| 2022 | 2,087 | 386 | 1,701 | 1,613 | 991 | 240 | 1,395 | 2,452 | 1,282 |
| 2023 | 2,288 | 450 | 1,838 | 1,746 | 1,340 | 266 | 1,509 | 2,912 | 1,429 |
| 2024 | 2,468 | 606 | 1,862 | 2,166 | 1,650 | 295 | 1,499 | 3,217 | 1,681 |
| 2025 | 2,627 | 663 | 1,964 | 3,308 | 1,709 | 320 | 1,582 | 3,353 | 1,736 |
| 5-yr avg | | | | 1,997 | | | 1,425 | 2,779 | |

  Sources: FFO, maintenance and AFFO, BIP 20-F 2022 MD&A (2021, 2022) and 20-F 2025 MD&A (2023 to 2025); growth capex,
  same tables by segment; interest, the "Total attributable to Brookfield Infrastructure" columns of the audited segment
  notes; incentive distributions, Item 7.B ("the Holding LP paid incentive distributions of $320 million (2024: $295
  million, 2023: $266 million)") and the 2022 20-F's related-party note ($240, $206); preferred and perpetual-note
  distributions, the distributions note (2021 $67, 2022 $66, 2023 $63, 2024 $68, 2025 $62); D&A attributable, the segment
  notes. Stock pay: none found at the partnership (no employees; the manager is paid a fee, which is inside FFO as
  general and administrative cost: $414M in 2025, Item 7.B). Resolved and complete for the lines named.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest is **who is paid to tell you**: the manager is paid "1.25% of our partnership’s market
value plus preferred units outstanding and net recourse debt" (BIP 20-F 2025, Item 5) and an incentive share of every
distribution above a threshold, so the filer's featured measures (FFO, AFFO, a 12% to 15% return target, a 5% to 9%
distribution-growth target) come from a party with an "enormous amount of fees possible from one action" **[M2020-037]**;
the projection of the seller is not asked for **[M2011-083]**. **A share is a business**: the share here is a contractual
claim on another entity's unit, so the business is BIP, and the test "Would I be happy buying this stock if the market
closed for five years?" **[M1997-109]** is put to BIP's portfolio, not to BIPC's three subsidiaries. No macro view enters
**[M2000-094]**. **Contrary evidence, written down as found** **[M1997-127]**: (1) the Rights Agreement that backed the
exchange ended on 2025-03-31, so a holder's claim to one unit rests on BIPC's articles and BIPC's own assets (BIPC 20-F
2025, Item 3.D); (2) BIPC's own balance sheet at 2025-12-31 shows "Shares classified as financial liability" of $5,129M
against equity attributable to the partnership of $(1,299)M, so BIPC's net assets before that liability and before
non-controlling interests are about $3,830M at book, about three quarters of the exchange claim at market (BIPC 20-F
2025, F-6; arithmetic $5,129M less $1,299M); (3) BIPC "guarantee[s] certain debt obligations of Brookfield
Infrastructure" (Item 3.D heading); (4) the 20-F states that none of the arrangements "impose on Brookfield any fiduciary
duties to act in the best interests of our shareholders" (Item 3.D heading).

## THE STANDING RULE
Owning this, bought for cash, puts the buyer at no risk of ruin: the share carries no call for further money and no
margin, and the rule binds the buyer's financing and sizing, "never going to risk what we have and need for what we
don’t have and don’t need" **[M2012-081]**; "You never get in a position, obviously, where the other fellow can call your
tune." **[M2006-079]**. The target's own debt is weighed at Q9, not here.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it.** "can I understand it?" **[M1995-051]**, meaning "a reasonable fix on about what the
  earning power and competitive position will look like in five or 10 years" **[M2012-065]**. The instrument is understood
  first (Step 0): one BIPC share is one BIP unit's economics, so the question is put to BIP, a holding company of
  part-interests (most of them 10% to 40%, alongside Brookfield's private funds) in four segments. **A holding company is
  understood by its parts**; a part matters when it decides, more than half of five-year operating profit or else the
  largest part (the framework's Q1 holding-company paragraph and Q2's business-of-parts paragraph).
- **The parts table** (BIP's share, US$ millions; FFO from the audited segment notes of the 2022 and 2025 20-Fs; Adjusted
  EBITDA from the segment MD&A tables of the same filings). **CONVENTION of this run:** the filer reports no "operating
  profit" by segment; its audited segment measure is FFO (after interest, before depreciation), with Adjusted EBITDA
  beside; both are used and give the same deciding part. Rationale: the filer's own audited segment measure is the least
  invented proxy, and showing the second measure tests that the choice does not decide.

| Segment | FFO 2021 | 2022 | 2023 | 2024 | 2025 | 5-yr FFO | Share | 5-yr Adj. EBITDA | Share |
|---|---|---|---|---|---|---|---|---|---|
| Utilities | 705 | 739 | 879 | 760 | 786 | 3,869 | 28.8% | 5,950 | 30.5% |
| Transport | 701 | 794 | 888 | 1,224 | 1,144 | 4,751 | 35.4% | 6,494 | 33.3% |
| Midstream | 492 | 743 | 684 | 625 | 668 | 3,212 | 23.9% | 4,534 | 23.3% |
| Data | 238 | 239 | 275 | 333 | 502 | 1,587 | 11.8% | 2,510 | 12.9% |
| (Corporate) | (403) | (428) | (438) | (474) | (473) | (2,216) | | | |

  No segment carries more than half; **Transport is the largest and decides** on both measures. Inside it, BIP reports
  three businesses (2025 FFO): diversified terminals $603M (the world's largest intermodal container lessor, Triton,
  consolidated at BIPC with a 27% ownership interest, plus port and terminal interests), rail $366M (a Brazilian rail and
  port logistics network at about 21%, Australian and North American rail), toll roads $175M (Brazil and Peru). The
  portfolio changes by policy: "As the business matures and cash flows have been de-risked, we seek to recycle capital and
  re-invest" (BIPC 20-F 2025, Item 4.A); the framework reads such a company "on the parts it owns, with the policy weighed
  at Q6".
- **Key variables and whether they are foreseeable** **[M1998-044]**: for rail and toll roads, regulated or contracted
  tariffs indexed to inflation and traffic or freight volumes (iron ore, grain, general freight); for containers, global
  trade volume, utilisation, lease rates and the price of new boxes; for the whole, the cost and availability of the
  asset-level debt that finances it (BIP's share of debt $35,652M at 2026-06-30). These are old, slow-changing businesses
  whose economics are "important and knowable" **[M2006-076]**; I understand "the economic dynamics of the industry"
  **[M2011-014]** for rail, roads and container leasing, and the figures needed are in the filings. Abroad, the
  governance (a Bermuda partnership managed by Brookfield; a British Columbia corporation) and the tax are set out in the
  20-Fs **[M2000-141]**.
- **Routing.** Not a business of fast-changing technology in its deciding part. The Data segment (AI-related data centres,
  semiconductor foundries; 12% of five-year FFO, 19% of 2025's) is the part I would not claim to foresee, and it does not
  decide. Doubt about the deciding part would keep the whole outside **[M2002-092]**; I record none that the filings
  cannot answer. **[M2023-031]** stays open against the by-parts reading, as the framework says.
- **Contrary evidence** **[M1997-127]**: the five-year window itself changed the deciding part (Triton bought 2023;
  Australian export terminal, Australian container terminal and part of the U.K. ports sold in 2025; BIP 20-F 2025, Item
  4.A), so the Transport of 2035 will not be the Transport of 2025; the instrument is mid-change (the vote of 2026-10-29).
- **VERDICT: IN.** The share is understood as one BIP unit; BIP is understood by its deciding part, Transport, whose
  ten-year economics rest on knowable tariffs, volumes and leases **[M1995-051]**, **[M2012-065]**, **[M2006-076]**.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing
five, 10, 20 years from now." **[M1995-038]**. Asked of the deciding part, Transport (Q1's parts table); the other three
segments are written down under "the parts" below and do not decide.

**Lines of evidence chosen, and from which item** (the brief's departure: derived by the analyst). From BIPC's 20-F 2025:
Item 4.B (the three BIPC businesses: Brazilian gas transmission "fully contracted under long-term ship-or-pay" until the
first contract expired on 2026-01-01, "transitioning to a RAB-based regulatory regime, in which tariffs reset every five
years"; U.K. last-mile connections on regulated tariffs with "a cap and floor"; the container lessor serving "the
world’s top shipping lines"), Item 3.D (the sole-customer risk at the Brazilian pipeline; competition for acquisitions;
commodity demand; regulation and nationalisation; the Brookfield relationship), Item 5 (results and cash flows), Item
7.B (the Master Services Agreement, the fees, the ATM programme, the related-party loans). From BIP's 20-F 2025: Item 4.A
(every acquisition and disposition 2023 to 2025), Item 4.B and Item 5 (segment and business results, maintenance and
growth spending, debt by segment and maturity), Item 7.B (base fee and incentive distributions). Litigation: "not,
during the past 12 months, been and is not currently subject to any material governmental, legal or arbitration
proceedings" (BIPC 20-F 2025, Item 4.B); no instance of material litigation found in the BIP Item 4.B read.

**The castle tests, on the deciding part.**
- *The money test* **[M2011-015]**: a rival with money cannot build a second Brazilian rail and port network, a second set
  of Brazilian and Peruvian toll-road concessions, or a second Australian freight railway; the speakers name the rail case
  directly, "You really couldn’t create another railroad" **[M2013-054]**. Containers are the exception inside the
  segment: money buys boxes, and the 2025 purchase of a half-million-TEU fleet from Global Container International "fully
  funded through debt" (BIP 20-F 2025, Item 4.A) shows fleets change hands for money.
- *Pricing power and the agony* **[M2005-020]**: rail and toll tariffs move by contract and indexation, "inflationary
  tariff increases of 7%" at rail in 2024 and "average rate increases of 7% across our rail networks and 6% across our
  toll road portfolio" (BIP 20-F 2025, Item 5, 2024 vs 2023); the price is set by a contract or a regulator, not won from a
  customer, so it shows protection, not the "something very special in people’s minds" kind. Container lease rates are
  market rates.
- *The low-cost position* **[L2004-007]**, *and would the customer take the low bid* **[L2004-003]**: shipping lines lease
  or own boxes on price, a commodity product. The leader's returns run above its rival's in every overlapping year (the
  competitor row below), which is the sign the low-cost row describes; no cost-per-TEU comparison was read, so the claim
  rests on returns, not on costs.
- *Widening or narrowing* **[M1999-108]**: Transport FFO rose from $701M (2021) to $1,144M (2025), most of it bought (Triton,
  September 2023; an added 10% of the Brazilian rail business, April 2024) and some of it sold again (2025); the window
  shows a portfolio rotated, not a moat visibly widened.
- *What could destroy, modify or reduce it* **[M2000-014]**: concession expiry and renegotiation (Brazil, Peru);
  dependence of the Australian railway on iron ore (BIP 20-F 2025, Item 3.D: "our Australian rail operation relies on
  demand for iron ore for steel production"); a fall in container trade or a glut of new boxes; and the regulatory compact
  breaking, which the speakers record as their own error with utilities **[L2023-011]**.
- *Would it stand without the lord* **[L2007-006]**: the railways and roads would; what would not stand without
  Brookfield is the rotation itself, the buying and selling that changes what the unit owns. That is weighed at Q6.

**The competitor row** (container leasing, the largest business inside Transport; the 20-F names no operating rival,
Item 3.D naming only "investment funds, operating companies acting as strategic buyers" as competitors for acquisitions).
**CONVENTION of this run:** the comparators are chosen by me: Triton (the BIPC subsidiary itself, which still files) and
Textainer, the one other container lessor found filing with the SEC; no rail or toll-road rival was read. Rationale: the
brief asks for rivals from their own filings, the filer names none, and the container business is where the castle is
weakest, so it is the one to test. Metric: pre-tax profit plus interest, over year-end total assets (an unlevered return,
after depreciation), from XBRL company facts (tagged data, transcription, not cross-checked to the statements):

| Year | Triton (CIK 1660734; 10-K to FY2023, 20-F for FY2024 `0001660734-25-000004` and FY2025 `0001660734-26-000005`) | Textainer (CIK 1413159; 20-F, last `0001564590-22-010813` and the FY2022 facts) |
|---|---|---|
| 2016 | 2.0% | 0.6% |
| 2017 | 6.6% (net income used; pre-tax not tagged) | 3.2% |
| 2018 | 6.6% (same) | 4.1% |
| 2019 | 7.2% | 4.1% |
| 2020 | 6.4% | 3.4% |
| 2021 | 6.4% | 5.6% |
| 2022 | 8.6% | 6.2% |
| 2023 | 6.9% | (taken private; no filing read) |
| 2024 | 7.4% | |
| 2025 | 8.3% | |
| Span average | 6.6% (2016 to 2025) | 3.9% (2016 to 2022) |

Named rivals that do not file: none named. Unnamed lessors (state-owned and private) were not read.

**The field's returns over the last full cycle, judged in words.** Container leasing, trough (2016) to boom (2022) and back:
the leader earns a modest unlevered return, roughly the level of a corporate bond, and its rival less; the equity returns
Triton reports (net income of $747M in 2022 on equity near $3 billion) are made by gearing assets about four times equity,
which the rows say to strip out ("leverage" among the three things to rule out, **[L1994-009]**). The Transport segment as
a whole, BIP's share: Adjusted EBITDA less maintenance spending over BIP's share of segment assets was 9.5% (2021), 10.9%
(2022), 8.9% (2023), 11.2% (2024), 10.3% (2025), before any depreciation beyond the filer's maintenance estimate and on
assets carried at revalued amounts (BIP segment notes and MD&A; arithmetic in `notes.md`). The rail and road half earns
returns set by concession or regulator, which Q2's list excepts from the ordinary-returns OUT and sends to Q3: "there’s no
way we get rich on our utility investments" **[M2009-104]**; such businesses are entered on "decent returns on the
incremental sums they invest" **[L2009-012]**. The container half earns ordinary returns in a commodity field, held up by being the largest and, on the
returns, the lower-cost operator **[L2004-007]**.

**The parts** (business-of-parts paragraph): Utilities (regulated transmission and distribution, 29% of five-year FFO),
Midstream (Canadian and U.S. pipelines, processing and a petrochemical complex, 24%), Data (towers, fibre, data centres,
semiconductor foundry interests, 12%) do not decide. Read at the finer level of the businesses BIP reports inside its
segments, Midstream would be the largest single business over five years ($3,212M of FFO against diversified terminals'
$1,638M over 2023 to 2025 alone, the earlier years not split); the segment level is used because it is the level of the
audited segment note. Written down as an unclear point (last section).

- **VERDICT: IN**, weighed and narrow. The deciding part's castles stand: networks and concessions that money cannot
  duplicate **[M2011-015]**, **[M2013-054]**, earning returns a contract or a regulator sets, which Q2's list sends to Q3
  rather than OUT ("there’s no way we get rich on our utility investments" **[M2009-104]**); the container half is a commodity held by its largest and
  better-returning operator **[L2004-007]**. Carried forward: the container half's returns are ordinary, the whole is
  bought and sold by policy, and the price power is indexation, not agony.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** **[M2010-090]**, the group's share. Capital employed (invested capital plus net
  debt attributable to the partnership, BIP's own non-IFRS measures): $23,698M at 2020-12-31 (9,213 + 14,485), $29,697M at
  2021-12-31 (12,195 + 17,502), $46,579M at 2025-12-31 (12,806 + 33,773) (BIP 20-Fs 2020, 2022, 2025, MD&A). Owner cash
  before interest (maintenance basis, Step 0 table) $1,961M (2021) and $3,353M (2025): 6.6% and 7.2% of capital employed,
  pre-tax and with interest added back in full. On the depreciation basis (FFO plus interest less D&A attributable less
  incentive distributions: $1,138M in 2021, $2,280M in 2025) the figures are 3.8% and 4.9%. The filer's own "return on
  Invested Capital of 14%" is AFFO over equity contributed, after asset-level debt that is nearly three times that equity:
  a geared figure of the kind the rows say to rule out as evidence ("leverage", **[L1994-009]**; return on equity made
  "almost any number you want if we just used enough leverage" **[M2001-054]**).
- **What the added capital earned.** From 2021 to 2025 capital employed rose $16,882M and owner cash before interest rose
  $1,392M (maintenance basis), 8.2% pre-tax on the increment; $1,142M on the depreciation basis, 6.8%. "whether that’s good
  or bad depends on what we earn on that incremental $130 million over time" **[M2001-019]**: here the increment earns
  about what the asset-level debt costs (the corporate notes issued in 2024 and 2025 carried coupons of 3.700% to 7.250%,
  BIP 20-F 2025, Item 4.A), so the growth adds little per unit; per unit, owner cash on the equity basis went from $1.59 (1,139 / 714.8M
  units) to $2.00 (1,582 / 790.5M), 5.9% a year, while capital employed per unit rose faster.
- **Reinvestment to stand still.** The filer's maintenance spending ($663M in 2025; estimate for 2026 "$615-$670 million")
  is 38% of its D&A attributable ($1,736M); it argues the revaluation model inflates depreciation (BIP 20-F 2025, Item 5,
  "Depreciation, amortization and return of capital estimates"). The rows hold depreciation to be the price of standing
  still: "Every year we spend amounts equal to our depreciation charge simply to stay in the same economic place"
  **[L2000-035]**; the gap is carried to Q4 and Q7 as the depreciation variant. The filer itself adds back "an estimate of
  the portion of earnings that represent a return of capital on concession-based businesses" ($128M in 2025) when it
  computes its return, an admission that concessions run off.
- **Growth arithmetic and its caps.** Growth spending rose from $1,153M (2021) to $3,308M (2025), the 2025 step "from our
  construction progress at our semiconductor manufacturing foundries in the United States" (Data, not the deciding part);
  the growth projects are underwritten at "our partnership’s target after-tax equity return threshold of 12-15%+", a geared
  target. The regulated and concession half earns a set return: "there’s no way we get rich on our utility investments"
  **[M2009-104]**; the second best "still a good choice" **[M2018-055]** only where the added sums earn "decent returns"
  **[L2009-012]**.
- **WEIGHS AGAINST**: a capital-heavy second best whose added capital, over the five years, earned about the cost of the
  debt that financed it, and whose maintenance spending runs far below its depreciation **[M2001-019]**, **[L2009-012]**,
  **[L2000-035]**.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, eight to ten years of them** **[M2025-032]**. BIP, consolidated (US$ millions; BIP 20-Fs for
  2016, 2018, 2020, 2022, 2024, 2025, statements of financial position or the summary key-metrics table where the older
  statements did not extract):

| Dec 31 | Total assets | Borrowings (corporate + non-recourse) | Goodwill | Limited partners' capital | Interest of others in operating subsidiaries | Cash | Proportionate net debt |
|---|---|---|---|---|---|---|---|
| 2015 | 17,735 | 7,232 | n.r. | 3,838 | n.r. | 199 | n.r. |
| 2016 | 21,275 | 8,326 | n.r. | 4,611 | n.r. | 786 | n.r. |
| 2017 | 29,477 | 10,164 | n.r. | n.r. | n.r. | 374 | n.r. |
| 2018 | 36,580 | 15,106 | n.r. | n.r. | n.r. | 540 | n.r. |
| 2019 | 56,308 | 21,019 | 6,553 | 5,048 | 14,113 | 827 | 12,121 |
| 2020 | 61,331 | 23,178 | 6,634 | 4,233 | 13,954 | 867 | 14,485 |
| 2021 | 73,961 | 29,253 | 8,979 | 5,702 | 15,658 | 1,406 | 17,502 |
| 2022 | 72,969 | 30,233 | 8,789 | 5,372 | 15,320 | 1,279 | 19,188 |
| 2023 | 100,784 | 45,815 | 14,488 | 5,321 | 23,661 | 1,857 | n.r. |
| 2024 | 104,590 | 51,094 | 14,101 | 4,704 | 20,568 | 2,071 | 28,842 |
| 2025 | 128,150 | 64,498 | 19,210 | 4,889 | 26,086 | 3,201 | 33,773 |

  (n.r.: not read in the extraction; the 2015 to 2018 borrowings are the key-metrics table's corporate plus non-recourse
  lines.) **What moved and why.** Assets rose about seven times and borrowings about nine times in ten years, while the
  limited partners' capital stayed between $3.8 billion and $5.7 billion: the growth was paid for by asset-level debt and by
  the money of Brookfield's private-fund partners, who own the "interest of others" ($26.1 billion in 2025). Goodwill
  roughly tripled from 2019 to 2025, the mark of acquisitions bought above book. The partnership carries an accumulated
  deficit ($6,094M at 2025, $4,419M at 2023, in the invested-capital reconciliation): distributions have run ahead of IFRS
  net income for years, and the gap is financed. Cash is small against the debt. What the figures do not say: the
  partnership's share of each asset's debt is a management measure ("Debt attributable to the partnership"), not a
  statement line; "what the figures are saying and what they don’t say and what they can’t say" **[M2025-032]**.
  BIPC's own balance sheets (BIPC 20-Fs 2020 to 2025): total assets $9,853M (2019), $9,344M (2020), $10,086M (2021),
  $10,178M (2022), $23,909M (2023, Triton consolidated), $23,587M (2024), $24,025M (2025); the exchangeable shares are a
  liability at the unit price ($2,221M in 2020, $4,466M in 2021, $3,426M in 2022, $4,153M in 2023, $4,644M in 2024,
  $5,129M in 2025), and the equity left to the partnership's class B shares after it has been negative at every year-end
  since the 2020 spin-off ($(1,722)M, $(2,127)M, $(1,119)M, $(399)M, $(1,253)M, $(1,299)M; total equity less
  non-controlling interests). BIPC's own net assets before the exchange liability covered that liability by about 22%
  (2020), 52%, 67%, 90%, 73% and 75% (2025) at book (arithmetic: liability plus the negative residual, over the liability).
  The share's value rests on the partnership's units, not on BIPC's assets, and since the Rights Agreement ended
  (2025-03-31) the partnership's delivery of units is an election, not an obligation (Step 0).
- **The real costs.** Depreciation: FFO adds back all of it, and the filer argues its revaluation model inflates the charge;
  the maintenance spending it deducts instead ($663M in 2025) is 38% of D&A attributable ($1,736M). The rows: "almost
  always true costs" **[L2015-004]**; depreciation "not inappropriate in most companies to use as a proxy for required
  capital expenditures" **[M1998-127]**; so both are carried to Q7, the maintenance case central under the framework's (e)
  and the depreciation variant beside it. Stock pay: none at the partnership; the manager's base fee ($414M) is inside FFO
  as general and administrative cost, the incentive distributions ($320M) are not and are deducted in Step 0's owner cash.
  Restructurings: none recurring found; "other income (expenses)" excluded from FFO ($344M of expense consolidated in
  2025) is a filer's choice of what is "not related to normal revenue earning activities". Concessions: the filer's own
  return-of-capital estimate ($128M) is noted at Q3.
- **EBITDA in the filer's own mouth; the habits.** The key-measures table leads with FFO, AFFO, Adjusted EBITDA and a
  "Return on invested capital"; IFRS net income attributable to the partnership ($1,091M in 2025, $391M in 2024, $432M in
  2023) sits beside a featured FFO more than twice as large. "The one figure we regard as utter nonsense is the so-called
  EBITDA" **[M1998-086]**; a management "highlighting "adjusted per-share earnings" makes us nervous" **[L2016-006]**. Targets
  declared and met: a 5% to 9% annual distribution increase, met in each recent year (6% in 2026; "a compound annual growth
  rate of 9% over the last 15 years"), and a 60% to 70% FFO payout, met (66% in 2025). These are weighed against here and
  carried to Q5 **[L2002-041]**. Clear speech counts the other way: every non-IFRS measure is reconciled line by line to
  IFRS in the audited segment note (F-33), and the depreciation argument is stated, not hidden **[M1994-018]**.
- **Confusion or suspicion?** The accounts are long and layered (consolidation at 27% ownership through a voting agreement
  with a Brookfield affiliate, as with Triton; deconsolidation by ending one, as with the Peruvian toll roads in June 2024;
  the exchangeable shares carried as liabilities at market so that BIPC's net income swings with the unit price), but each
  item is explained in the filings and was understood on reading. No tell from the accounts list was found (no building
  prepaid or deferred accounts, no reserve releases found, no restatement found in the filings read). Not a STOP
  **[M1995-063]**.
- **VERDICT on the accounts: WEIGHS AGAINST** (not a STOP): featured FFO and Adjusted EBITDA over IFRS earnings, maintenance
  set far below depreciation, growth financed off the partnership's own capital **[M1998-086]**, **[L2016-006]**,
  **[L2015-004]**. The recast earnings fed to Q7 are owner cash after maintenance (central) and after depreciation
  (beside), after incentive distributions, as in Step 0.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **Who.** Neither BIPC nor BIP's general partner employs the managers; Brookfield's Service Providers run both under the
  Master Services Agreement, led by Sam Pollock, "a Managing Partner of BAM and Chief Executive Officer of the Service
  Providers" who "Since 2006 [...] has led Brookfield’s expansion into the infrastructure sector" (BIP 20-F 2025, Item 6.A).
  BIPC's board of nine overlaps the general partner's board except for one director, who "assist[s] us with [...] resolving
  any conflicts of interest" (BIPC 20-F 2025, Item 6.A).
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* FFO per unit rose from $2.08
  (2020) to $3.32 (2025), and distributions at "a compound annual growth rate of 9% over the last 15 years" (BIP 20-Fs 2022
  and 2025); the per-unit record was made with assets growing about seven times on debt and partners' money (Q4), so it
  shows skill at buying, financing and selling more than at running one business better. *How they treat the owners:* in
  2025 Brookfield received a base fee of $414M and incentive distributions of $320M, $734M together, against $793M of
  distributions to the public limited partners (BIP 20-F 2025, Items 7.B and note 30); "read the proxy statements, see what
  they think of — see how they treat themselves versus how they treat the shareholders" **[M1994-009]**. The terms were
  "effectively determined by Brookfield" and none of the arrangements "impose on Brookfield any fiduciary duties"
  (BIPC 20-F 2025, Item 3.D).
- **The tells of dishonesty** **[M1995-111]**, looked for in what was read: reports that dance around the key figure (not
  found: the debt attributable, the fees, the incentive distributions and the conflicts are set out at length and the
  non-IFRS figures reconciled); a stock price featured (not found in the filings read); serial issuance (units from 680.2M
  to 790.5M on average, 2020 to 2025, about 16%, mostly as consideration for acquisitions, weighed at Q6 under
  **[L2014-015]**). Related-party dealing, stated in the filings: BIPC "sold its interest in its Australian regulated
  utility operation to an affiliate of Brookfield for net proceeds of approximately $435 million" (BIPC 20-F 2023); loans
  from Brookfield Wealth Solutions, refinanced on 2026-05-07 "at arm’s length on market terms" at 6.33% (BIP Q2 2026,
  related-party note); control of the Peruvian toll roads "revert[ed] [...] to Brookfield" by ending a voting agreement
  (BIP 20-F 2025, Item 4.A). Each is disclosed; none is shown to be dishonest.
- **The habits carried from Q4**: featured FFO and Adjusted EBITDA, declared distribution-growth and payout targets met
  year after year **[L2002-041]**, read with the record above: the met target is a distribution the board declares, not a
  reported earnings figure, and the earnings measures are reconciled in an audited note; "things that they do in public in
  relation to their investors and the promises they make" **[M2004-067]** show a promoter's habit of targets, not a
  falsehood found.
- **Doubt, stated.** What doubt I hold is about whose interest wins when Brookfield's and the unitholders' differ, which the
  filings themselves say may be "resolved in a manner that is not in the best interests of our company"; the rows read that
  as a culture to weigh, "if shareholders or somebody else has to suffer, the choice is likely to be that somebody else
  will be chosen" **[M1998-121]**, and the framework weighs pay and alignment at Q6 Part B. It is not a doubt about the
  truth of what is reported, which is what the STOP asks **[M2013-088]**.
- **VERDICT on integrity: IN** (no instance of dishonesty found in the filings read; the conflicts are stated, not hidden)
  **[M1995-111]**, **[M2013-088]**. **Ability WEIGHS FOR** on the record of buying, financing and running a large portfolio
  **[M1994-008]**; the second yardstick, the treatment of owners, **WEIGHS AGAINST** and is carried to Q6 **[M1994-009]**,
  **[M1998-121]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A: the money.**
- *The retention test* **[R1995-009]**, **[M1998-110]**: little is retained. Distributions (including the incentive and
  preferred distributions) took 97%, 89%, 83%, 82%, 88% and 89% of AFFO in 2020 to 2025 (BIP 20-Fs 2022 and 2025, the
  "AFFO payout ratio"); AFFO less distributions over 2021 to 2025 was about $1.2 billion in all (Step 0 figures). The growth
  is financed from outside: net debt attributable up $19.3 billion and invested capital up $3.6 billion from 2020 to 2025
  (Q3), plus the proceeds of selling "mature, de-risked businesses" (BIP 20-F 2025, Item 4.B, "Capital Recycling
  Strategy"). So the question the test asks is put to the external money and the rotation: per unit, owner cash on the
  equity basis rose 5.9% a year (Q3), with the added capital earning about its debt cost.
- *Buybacks* **[L1999-023]**, **[L2016-002]**: the normal course issuer bid authorises up to 23,062,017 units with no price
  named; 1.9 million units were bought in 2025 for $58 million, about $30.5 a unit (BIP 20-F 2025, Item 5 and Item 16.E);
  in the first half of 2026 BIPC issued 2,982,920 exchangeable shares under its at-the-market programme while the
  partnership bought back "an equivalent number of partnership units" (BIPC Q2 2026 6-K), which sells the dearer of the two
  twin securities and buys the cheaper and adds nothing to value per unit beyond the premium captured. *Read against the
  bottom of the Q7 range* (written back at Q7): the 2025 purchases at about $30.5 a unit sit above the bottom of the
  range, $20.45 a share on the all-equity basis, so the unpriced programme weighs against **[L2016-002]**, **[L2013-012]**.
- *Issuance and deals* **[M1995-001]**, **[L2014-015]**: units rose about 16% from 2020 to 2025 (Q5), mostly as deal
  currency; the Triton purchase of September 2023 was paid "$1.2 billion [...] consideration paid included $751 million of
  BIPC exchangeable shares issued and $55 million of pre-existing interest" (BIP 20-F 2025, Item 4.A), so more than half in
  shares: a merger by the framework's definition, valued on the combined figures (BIPC's 2023 and later statements consolidate
  Triton). Q6's one STOP falls on an acquisition paid "wholly" in undervalued stock **[L2009-019]**: this one was not wholly
  in stock, so the STOP's condition is not met; whether the shares went out below value was not tested (the issue price
  per share was not found in the filings read); weighed, not a STOP. The policy of continual buying and selling is the use of money the framework sends here: in
  2025 alone about $2.9 billion of sales (Mexican pipelines, the U.S. gas pipeline, the Australian export and container
  terminals, a third of the U.K. ports, part of the gas storage IPO and others) against purchases of Colonial ($900M),
  Hotwire ($800M) and others (BIP 20-F 2025, Item 4.A).
- *Part A* **WEIGHS AGAINST**: growth bought with outside money at about its cost, shares issued as deal currency, and a
  buyback with no stated price **[M1998-110]**, **[L2016-002]**, **[L2014-015]**.

**Part B: the pay, the board and the owners.**
- *Pay tied to what the person controls* **[M2003-019]**: the base fee is "1.25% of our partnership’s market value plus
  preferred units outstanding and net recourse debt" (BIP 20-F 2025, Item 5), so it rises with the unit price, with new
  units issued and with recourse debt, none of which measures what the manager did for value per unit. The incentive
  distribution right takes 15% of distributions above $0.1218 a unit a quarter and 25% above $0.1320, against a
  distribution of $0.455 now (BIP 20-F 2025, Item 7.B): about a quarter of every marginal dollar distributed, whether the
  dollar came from earnings or from new capital. It is "a royalty on money that you left with me" **[M1997-043]** in kind,
  and both legs pay in a bad year, which the rows call "heads I win, tails you lose" **[L1994-020]**. In 2025 the two came
  to $734M, 28% of FFO.
- *The board*: BIPC's directors, but one, are the general partner's; the overlapping directors were paid "an annual
  retainer of $15,000" by BIPC and the one non-overlapping director $165,000; directors are expected to hold shares or units
  costing "at least two times their annual retainer" (BIPC 20-F 2025, Item 6.B), a small stake beside "huge and true
  ownership interests" **[L2002-033]**. "Our company is not entitled to terminate the Master Services Agreement" (Item 3.D).
  Holders of the exchangeable shares cast 25% of the votes and the partnership 75%.
- *The owners as partners*: the alignment the filings offer is Brookfield's own economic interest, "approximately 26.5% on a
  fully exchanged basis" (BIPC 20-F 2025, Item 4.C), held beside fees that do not depend on per-unit results.
- *Part B* **WEIGHS AGAINST** **[M2003-019]**, **[L1994-020]**, **[M1997-043]**; the rows rank the person above the plan
  **[M2007-006]**, and the person here was found able at Q5.

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the discounted value of the cash that can be taken out of a business during its remaining life" **[R1996-018]**,
at "the yield on long-term U.S. bonds" **[L2000-021]**, held as a range **[L2000-024]**. All arithmetic is in
`q7_calc.py`, output in `q7_output.txt` (research folder); inputs are the Step 0 table and the debt figures below.

**The construction, by Q7's range convention and its specifics.**
- *The cash.* Owner cash after every real cost the filer reports, the group's share: FFO less maintenance spending less the
  incentive distributions (Step 0), on the all-equity basis with the group's share of interest added back. The interest is
  added back in full, without taking away its tax shield; this overstates unlevered owner cash and can only favour the
  business, so a conclusion against the price survives it. FFO is after current tax and before deferred tax, which is the
  company's own tax (Q7, Whose tax); no expiring carryforward was identified. Five-year average 2021 to 2025: **$2,779M**
  before interest (equity basis $1,425M). Depreciation variant beside: $1,810M.
- *(c) Acquisitions, and the serial acquirer.* BIP does not report its share of purchases and sales as one figure; derived
  from its filed measures: capital employed grew $22,881M from 2020 to 2025 (net debt attributable +$19,288M, invested
  capital +$3,593M), plus $1,199M of AFFO not distributed, less $9,986M of growth capital spending, leaves **about $14,094M
  of net purchases** over 2021 to 2025 (including currency effects on the debt, which the derivation cannot separate;
  labelled as derived, not filed). That is more than half of owner cash before purchases ($6,948M before interest; $3,562M
  on the equity basis), so **the serial-acquirer rule applies: the central figure is the organic pair**, purchases left out
  and organic growth as the filer reports it. The filer reports group organic growth of 10% (2022), 8% (2023), 7% (2024)
  and 8% (2025) (BIP 20-Fs, the payout-ratio factors); 2021 is not stated as a group figure (only "11% organic growth" for
  transport). **CONVENTION of this run:** the growth carried is the average of the four stated years, **8.25%**. Rationale:
  the rule asks for organic growth "as the filer reports it", and four of the five window years are reported. *The default
  pair beside:* owner cash after maintenance, growth spending and the derived net purchases averages **$(2,037)M** a year,
  negative, so its total-growth case has no meaning by (b) and its value is below zero at any rate; written down, not used.
- *(e) Growth spending.* The filing allows the maintenance guess (the filer states it and an engineering review of it), so
  the central cases are after maintenance only, with the growth spending ($1,997M a year, the five-year average) charged
  against the growth it buys in the growth case. **CONVENTION of this run:** after year ten, when growth stops, the growth
  spending stops with it, as (c) says of purchases. Rationale: (e) charges growth spending to the growth it buys and is
  silent on the years after growth stops; (c)'s reasoning ("a business that buys no growth spends nothing to buy it")
  applies to building as to buying.
- *(a) Cycles:* neither end year is described by the filer as aberrational; the literal five-year window is the base.
  *(b) Decline:* none; the series grew every year. *(d) Working capital:* AFFO excludes working-capital changes and the filer
  reports no proportionate working-capital figure; not counted, said so (a gap, last section). *(f) The cap:* the shown
  organic rate is carried for ten years only; at year ten owner cash would be $6,140M against revenue of $19,672M grown at
  the window's revenue growth (10.97% a year, $5,281M in 2021 to $8,009M in 2025, BIP's share): 31%, below the highest
  share earned in the window (41.9%, 2025), so no cut. After year ten, zero nominal growth.
- *The bridge from the business to the share* (Q7, On what the floor is earned): net debt attributable to the partnership
  **$33,969M** at 2026-06-30, the latest filed date (BIP Q2 2026 interim report, MD&A, "Net debt"; operating leases not
  included in it, said so); preferred units $729M and perpetual subordinated notes $293M, together **$1,022M**; **791.7
  million** unit-equivalents (Step 0). No subsequent event in that filing changes net debt by a stated amount (the
  Mantiqueira sale for about $150 million, signed in November 2025, is left out; it is small and its closing is not
  confirmed in the filings read).

**The range** (per BIPC share, the long government rate 5.43%):

| Case | All-equity basis (central) | Equity-only basis (beside) |
|---|---|---|
| No growth, owner cash after maintenance | **$20.45** (EV $51,179M) | $33.14 |
| Growth 8.25% for ten years, growth spending charged | **$61.60** (EV $83,758M) | $44.94 |
| Depreciation variant, no growth | $(2.10) | |
| Default pair (acquisitions deducted) | below zero | below zero |

- **Value range: $20.45 to $61.60 a share against $37.74.** Width 3.01 to 1.
- **The floor, tested first** **[M2003-149]**: each case valued at ten percent. All-equity: $(9.10) no growth, $2.37 growth.
  Equity-only: $18.00 no growth, $16.32 growth (the growth bought is worth less than its cost at ten percent on this basis,
  the inversion (e) names). Even the generous test that charges no growth spending at all gives $17.88 (all-equity) and
  $31.82 (equity-only). **No case earns the floor at $37.74.** In yields: owner cash before interest is 4.3% (five-year
  average) and 5.2% (2025) of the enterprise value at the price ($64,870M); on the equity basis, 4.8% and 5.3% of the market
  value. Both sit below the 30-year Treasury at 5.43%, before any growth is credited.
- **Fair price (a reporting figure, never a verdict; Part VII):** each end case valued at ten percent and the two averaged,
  after the company's own tax: on the all-equity basis **below zero, $(3.36) a share** (at ten percent the two ends are worth
  less than the net debt and the preferred capital ahead of the units); on the equity-only basis **$17.16 a share**. No
  cheap price is reported. (Q6's buyback line was written back from this range.)
- **The signed, unclosed change:** the Simplification exchanges each share for one BIP Inc. class A share (or leaves it
  exchangeable into one); no cash stream changes, so the range is the same either way. Closed after the window: the Wells
  Fargo Rail joint venture (2026-01-01, about $300 million of equity) is inside the 2026-06-30 net debt and is credited with
  nothing, no earnings of it being filed in the window.
- **VERDICT: OUT.** No case in the range earns the floor of about ten percent at the price, on either basis **[M2003-149]**;
  the price also sits inside a range of about three to one, the close call that would need a pencil **[M2009-005]**,
  **[M1996-084]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED (Q7 closed the file OUT; operator rule 2).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts found are under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**OUT at Q7**: no case in the value range earns the floor at the price; **range $20.45 to $61.60 a share (all-equity
basis, organic pair, at the 30-year Treasury of 5.43%) against $37.74**. Fair price (reporting figure): below zero,
$(3.36), on the all-equity basis; $17.16 on the equity-only basis. Q1 IN (the share is one BIP unit; BIP read by its
deciding part, Transport), Q2 IN narrow, Q3 weighs against, Q4 weighs against, Q5 integrity IN, Q6 weighs against on both
parts. No integrity facts left unjudged (Q5 was answered).

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Facts found before or during Q7 that bear on questions not reached; written down, not weighed; the box unchanged,
operator rule 2.)* **[M1997-127]**
- **Q8 (the bond):** the 30-year Treasury is 5.43% (2026-10-16); owner cash before interest is 4.3% (five-year average)
  and 5.2% (2025) of the enterprise value at the price, and owner cash on the equity basis 4.8% and 5.3% of the market value
  (Q7).
- **Q9 (debt and exposures):** debt attributable to the partnership $35,652M and net debt $33,969M at 2026-06-30, about
  1.1 times the market value of the units at the price; the partnership's share of scheduled principal: $508M (rest of
  2026), $1,652M (2027), $4,854M (2028), $3,968M (2029), $4,880M (2030), $18,651M beyond, average term seven years;
  corporate (recourse) borrowings $4,124M with an average term of 14 years; group-wide liquidity $5,535M (BIP Q2 2026
  interim report, MD&A). Consolidated debt $62,465M, most of it non-recourse to the partnership. A BIPC subsidiary "has
  agreed to guarantee certain commercial paper, unsecured debt securities and preferred securities issued by Brookfield
  Infrastructure" (BIPC 20-F 2025, Item 3.D). The Brazilian pipeline "is dependent on a sole customer for the majority of its
  revenues" and moved from ship-or-pay contracts to five-yearly tariff resets from 2026-01-01 (Items 3.D, 4.B). Draws on
  "Brookfield's private funds credit facility used to bridge acquisitions over year-end" are carried among the
  non-controlling borrowings (BIP 20-F 2025, Item 5). BIPC's own net assets covered 75% of the exchange claim at 2025-12-31
  at book, and the Rights Agreement that backed the exchange ended on 2025-03-31 (Step 0, Q4).
- **Q10:** nothing found.
- **Q12:** the businesses named by the rows (casinos, tobacco, distributor-loading schemes) are not among the group's; the
  group owns refined-products and gas pipelines, a petrochemical complex in its Canadian midstream business, residential
  service contracts (HomeServe), data centres and semiconductor-foundry interests (BIP 20-F 2025, Item 4). The newspaper
  test was not applied.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early): Step 0
      to Q1, Q2, Q3, Q4, Q5, Q6, Q7 (with the Q6 write-back), the close, each a pathspec commit of the two paths.
- [x] If dispatched to an analyst: the brief allowed the per-question commits and the lock was held by the dispatching
      session (the lock file was present at the start, written 2026-10-17T20:46:01); the run is folded into the register by
      the dispatcher (operator rule ten). A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; the one directory listing of
      `Test Runs/` (to check the file name was free) is declared under contamination, with what it showed; nothing in it
      concerned this company.
- [x] Every v5 id resolves (checked by `check_citations.py` in the research folder); every filing fact has its accession
      in Step 0 or beside it; derived figures (net purchases, coverage ratios, returns on assets) are labelled as arithmetic
      on filed figures. Triton and Textainer figures are XBRL company facts, flagged as tagged data, not cross-checked.
- [x] The order was kept; Q7 was the first STOP that failed and closed the run; Q8 to Q12 are NOT REACHED and nothing
      after Q7 is a clearance.
- [x] Owner cash after every real cost the filer reports (FFO less maintenance less incentive distributions; depreciation
      variant beside), never a net-income proxy (operator rule 5); the sovereign from the US Treasury; the price is an
      aggregator quote, flagged. Limits stated: interest added back without its tax shield (favours the business);
      working capital not counted (not reported on the partnership's share).
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q1, Q2, Q4); facts for the questions
      not reached are under AFTER THE STOP.
- [x] Not a point-in-time run; no anchor-date rule applies.
- [x] Only the arithmetic lines of `tools/run.py` could have been used; the tool failed on this 20-F filer and nothing it
      printed was used.
- [x] `python tools/check_framework.py` PASS before the closing commit (result recorded in `notes.md`).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **A share that is another entity's unit.** The framework has no rule for a twin security whose economics are
contractually another issuer's (here one BIP unit) while its legal backing is the issuer's own assets (BIPC's net assets,
75% of the exchange claim at book, with the backstop agreement ended). I valued the unit's business (BIP) and wrote the
backing down as a fact at Step 0, Q4 and under Q9; the framework does not say where the gap between the economic claim
and the legal backing is judged (Q1, Q4 or Q9). (2) **Which "parts" decide.** The business-of-parts paragraph does not say
whether the parts are the audited operating segments or the businesses the filer reports inside them; at the segment
level Transport decides, at the business level Midstream would. I used the audited segments and said so. (3) **A deciding
part that is half regulated and half commodity.** Q2's list sends a field earning ordinary returns to OUT, with a
regulator's return excepted; it does not say how to close a deciding part whose regulated half and commodity half point
different ways. I closed it IN, narrow, and carried the doubt. (4) **The serial-acquirer test needs a purchases figure the
filer does not report.** BIP gives no single figure for its share of purchases net of sales; I derived it from the change
in its own capital measures, which mixes in currency effects. (5) **Growth spending after year ten.** (e) charges growth
spending to the growth it buys but does not say whether it stops when growth stops; I applied (c)'s purchases rule by
analogy, a CONVENTION of this run. (6) **"Owner cash before interest and after the company's tax"** does not say whether
interest is added back net of its tax shield; I added it back gross, which favours the business, and the OUT holds either
way. (7) **An incentive distribution right** is neither a cost nor a security in the framework's terms; I deducted the
amounts paid from owner cash, which understates the claim as distributions rise (the right takes 25% at the margin).
(8) **A multi-currency earnings stream** has no single earnings-currency sovereign; I used the reporting currency's, as the
brief says. (9) **Working capital** under (d) cannot be counted where the filer reports cash only on its share and before
working capital. (10) `tools/run.py` fails on a 20-F filer reporting under IFRS; every figure was taken from the filings
by extraction scripts.
