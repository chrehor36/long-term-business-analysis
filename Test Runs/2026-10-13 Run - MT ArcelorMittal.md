# Company Run — ArcelorMittal S.A. (NYSE: MT, New York Registry Shares) — 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. Filled at the fold by the dispatching session (overnight 2026-10-13, after the run was committed): not held (`PORTFOLIO.md` carries no line for MT or ArcelorMittal).

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md`, with the one departure the brief states: the lines of
evidence were derived by the analyst from the 20-F's Item 4 (business overview, segments), Item 3.D (risk factors) and
Item 5 (operating and financial review), not handed over as a list. The ones chosen: segment results and margins over the
cycle 2017 to 2025; the cost position against imports and against named producers; pricing and volume in the Europe
segment; capital spending split into maintenance and strategic growth; acquisitions and joint-venture purchases; debt,
leases and receivables sold; buybacks and the agreement with the significant shareholder; stock pay; litigation, safety
and investigations. Research folder: `Test Runs/_research 2026-10-13 MT/` (notes, scripts; raw filings in its ignored
`cache/`).

**Contamination, declared and not used.** (1) The session's opening context listed recent commit subjects of another
company's purchase run (ticker TX, a steel producer), including the wording of its Q2 close. I did not open that run file.
I left that company out of the competitor set for this reason, and Q2 below is built from ArcelorMittal's own filings and
the three rivals named in Q2. Its wording may still have shaped mine, and I say so. (2) The same context listed research-folder
names of other runs (ARCB, AYI) and memory lines about the queue and the opportunity set. None mentions this company. I did
not use any of it. (3) The brief said the company "bought Nippon Steel's 50% of AMNS Calvert on 2024-10-11". The 20-F says
control was acquired on June 18, 2025, after U.S. approval on June 13, 2025. This run uses the filing's date.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $63.47 (NYSE close 2026-10-13, New York Registry Share; Yahoo Finance chart feed via `tools/sources.py`,
  **an aggregator, flagged** per operator rule 5; used for the live quote only).
- **Shares by class:** one class of ordinary shares; the NYSE line is a New York Registry Share, one share each.
  `python Screens/cover_shares.py MT` returned "NO COVER SHARE COUNT PARSED - read the filing by hand", so the count was
  read by hand. The 20-F for FY2025 (filed 2026-03-06, accession `0001243429-26-000020`) gives 775,000,000 shares issued
  and 13,874,181 in treasury at 2025-12-31, so 761,125,819 outstanding. The figure matches the XBRL fact. 77,809,772 treasury shares were cancelled on 2025-11-20; the issued
  count fell from 852,809,772 to 775,000,000. The half-year report (6-K filed 2026-07-31, accession
  `0001243429-26-000075`, mt-20260630) shows 8,000,000 shares bought back and 915,879 delivered for share-based payments in
  the half, so **754,041,698 outstanding at 2026-06-30** (775,000,000 issued less 20,958,302 in treasury). This is the latest
  filed count. The 6-Ks filed since (2026-08-03, 08-17, 09-15 and 09-25, accessions `0001243429-26-000077`, `-000080`,
  `-000082` and `-000084`) state no new count. Buybacks under the 2025 programme continue, so the count is a ceiling. No split
  was found in the window.
- **Market cap:** $63.47 × 754.04M = **$47,859M**.
- **Sovereign for the earnings currency:** the reporting and earnings currency is the US dollar, so the rate is the US
  Treasury daily par yield curve, 30-year: **5.60%** (curve date 2026-10-09, the latest posted on the run date;
  `python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): the 20-F FY2025 (filed 2026-03-06, `0001243429-26-000020`); the half-year report
  6-K (filed 2026-07-31, `0001243429-26-000075`); the 20-Fs covering the cycle: FY2024 (filed 2025-03-10,
  `0001243429-25-000017`), FY2023 (filed 2024-02-28, `0001243429-24-000005`), FY2022 (filed 2023-03-08,
  `0001243429-23-000005`), FY2021 (filed 2022-03-11, `0001243429-22-000009`), FY2019 (filed 2020-03-03,
  `0001243429-20-000004`); the 6-Ks of 2026-07-30 (`0001243429-26-000072`) and the four after the half-year report listed
  above. As a foreign private issuer it files no proxy, and the 20-F's Item 6 and 7 sections were read in its place.
  **One figure cross-checked against the filed statement:** net cash provided by operating activities, FY2025, **$4,808M**
  in the consolidated statement of cash flows of the 20-F (with $4,852M for 2024 and $7,645M for 2023), equal to the XBRL
  fact `CashFlowsFromUsedInOperatingActivities`. Capital expenditure, FY2025, $4,337M, is the same in the cash-flow statement and in the
  segment note.
- **`python tools/run.py MT`** returned "MT: no overlapping OCF/D&A/capex annual facts. UNRESEARCHED." The company files
  IFRS tags (`ifrs-full`), and the tool reads US-GAAP tags. The arithmetic was therefore done by hand from the filed cash-flow
  statements and the IFRS company facts. The scripts are in the research folder (`facts_extract.py`, `q7_computation.py`). The table follows,
  in $M, as filed:

| FY | Cash from operations (after interest, tax, dividends from JVs) | Capex | D&A | Lease principal | Dividends to minorities | Owner cash, all spending | Owner cash, depreciation as maintenance |
|---|---|---|---|---|---|---|---|
| 2016 | 2,708 | 2,444 | 2,721 | n/s | 61 | 203 | (74) |
| 2017 | 4,563 | 2,819 | 2,768 | n/s | 141 | 1,603 | 1,654 |
| 2018 | 4,196 | 3,305 | 2,799 | n/s | 119 | 772 | 1,278 |
| 2019 | 6,017 | 3,572 | 3,067 | 320 | 129 | 1,996 | 2,501 |
| 2020 | 4,082 | 2,439 | 2,960 | 242 | 181 | 1,220 | 699 |
| 2021 | 9,905 | 3,008 | 2,523 | 199 | 260 | 6,438 | 6,923 |
| 2022 | 10,203 | 3,468 | 2,580 | 185 | 331 | 6,219 | 7,107 |
| 2023 | 7,645 | 4,613 | 2,675 | 253 | 162 | 2,617 | 4,555 |
| 2024 | 4,852 | 4,405 | 2,632 | 224 | 187 | 36 | 1,809 |
| 2025 | 4,808 | 4,337 | 2,945 | 234 | 121 | 116 | 1,508 |

  n/s: before IFRS 16 (2019), lease principal sits inside debt repayments and is not separable. The five-year average,
  2021 to 2025, is $3,085M on all spending, and $4,380M with depreciation as the maintenance guess. The ten-year average,
  2016 to 2025, is $2,122M and $2,796M. **Stock pay** is tagged at $13M (2016) and $31M (2017) and as nil
  for 2018 to 2021. Share-based payment is settled in treasury shares (915,879 delivered in the first half of 2026), so it is small against
  these sums, and the figures carry it inside operating cash as filed. **Not resolved further; stated.** **Acquisitions and
  joint-venture purchases, net of disposals** (investing lines of the 20-Fs): 2020 (98), 2021 (2,897) (the sale of the
  Cleveland-Cliffs shares received for ArcelorMittal USA), 2022 939, 2023 2,343, 2024 1,241, 2025 70. The 2025 Calvert purchase
  is presented net of $1,638M cash injected by Nippon Steel (20-F note 2.2.4). **Receivables sold without recourse:**
  $5.0bn at 2025-12-31 (20-F, liquidity section), off the balance sheet.
- **The balance sheets, ten years** (read here in Step 0 because the file closes before Q4; IFRS facts, 20-F, $M):

| 31 Dec | Total equity | Goodwill and intangibles | Equity-method investments | PP&E | Inventories | Trade receivables | Net debt (company definition) | Employee-benefit provisions | Deferred tax assets | Shares outstanding (M) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 32,325 | 5,651 | 4,297 | 34,831 | 14,734 | 2,974 | 11,059 | 8,297 | 5,837 | 1,019.5 |
| 2017 | 40,855 | 5,737 | 5,084 | 36,971 | 17,986 | 3,863 | 10,142 | 7,630 | 7,055 | 1,019.9 |
| 2018 | 44,108 | 5,728 | 4,906 | 35,638 | 20,744 | 4,432 | 10,196 | 6,982 | 8,287 | 1,013.6 |
| 2019 | 40,483 | 5,432 | 6,529 | 36,231 | 17,296 | 3,569 | 9,345 | 7,343 | 8,680 | 1,012.1 |
| 2020 | 40,237 | 4,312 | 6,817 | 30,622 | 12,328 | 3,072 | 6,380 | 4,656 | 7,866 | 1,080.7 |
| 2021 | 51,344 | 4,425 | 10,319 | 30,075 | 19,858 | 5,143 | 4,030 | 3,772 | 8,147 | 910.9 |
| 2022 | 55,590 | 4,903 | 10,765 | 30,167 | 20,087 | 3,839 | 2,236 | 2,606 | 8,554 | 805.3 |
| 2023 | 56,068 | 5,102 | 10,078 | 33,656 | 18,759 | 3,661 | 2,898 | 2,741 | 9,469 | 819.3 |
| 2024 | 51,286 | 4,453 | 11,420 | 33,311 | 16,501 | 3,375 | 5,079 | 2,338 | 8,942 | 768.5 |
| 2025 | 56,536 | 5,252 | 10,393 | 41,041 | 18,589 | 3,476 | 7,931 | 2,526 | 8,860 | 761.1 |

  What they say **[M2025-032]**. Equity rose by $24bn over the decade, nearly all retained earnings (from $16.0bn to $49.9bn), while
  goodwill and intangibles stayed near $5bn. The growth in equity is retained profit, not purchased goodwill, and most of
  it came in 2021 and 2022. Net debt fell from $11.1bn to $2.2bn by 2022 and has risen since, to $7.9bn at year-end 2025 and
  **$9.5bn at 2026-06-30** (half-year 6-K). Inventories run at 26% to 30% of sales; they were $18.6bn against sales of
  $61.4bn in 2025. Trade receivables look small, but $5.0bn of receivables had been sold without recourse at year-end 2025,
  and the filing calls this a way "to manage its working capital cycle". The balance sheet understates the working capital
  the business needs, and the debt-like funding behind it, by that amount. Equity-method investments (AMNS India, Vallourec and others) grew from $4.3bn to $10.4bn. Their profit reaches
  owner cash only as dividends received ($362M in 2025). PP&E jumped in 2025 by the consolidation of Calvert, together with a
  $1,736M bargain-purchase gain in operating income. Deferred tax assets of $8.9bn rest on Luxembourg losses of $133.4bn,
  of which $35.0bn is judged realizable; losses generated before 2017 carry forward indefinitely. Pension provisions fell
  from $8.3bn to $2.5bn. The share count fell by about a quarter, from 1,019.5M (2016) to 754.0M (mid-2026). What the
  sheets cannot say: whether the European plants earn their cost of capital at replacement cost, which is the Q2 question.

## THE FOUNDATIONS (not a gate)
The foundation that bears on this name is that no macro forecast enters: "macro conclusions are — just never enter
into the discussion." **[M2000-094]**. A steel company tempts the analyst to forecast the steel price, Chinese exports or
European tariff policy, and the run does none of that. The price level enters only at Q7, as the cycle base; the business is judged on its
position, "We don’t think we can predict commodity prices." **[M2016-025]**. Second, a share is a business: "Would I be
happy buying this stock if the market closed for five years?" **[M1997-109]**. That turns the question to what the plants
earn through a cycle, not to the next move in the quote. **Contrary evidence, written down as found** **[M1997-127]**:
(a) the filing says decarbonization "will fundamentally change the market structure of the steel industry" (20-F, Item 4,
strategy); (b) the filing names its own Europe segment as dependent on new trade measures. The European Commission's
tariff-rate quota was proposed on 2025-10-07, and the filing says "It is now imperative that this is implemented" and that
with an effective CBAM it "will provide the foundation" for the business (20-F, Item 4); (c) carbon costs have "resulted,
and in the future may result, in production cuts due to relatively higher carbon costs rendering production structurally
unprofitable" (20-F, Item 3.D); (d) three blast furnaces in Europe were idled or shut in 2025: Fos-sur-Mer #1 (idle since September 2023), Dąbrowa
Górnicza #3 (idled since July 2025 "Due to deteriorating market conditions") and Gijón B (shutdown procedures after an
incident) (20-F, Item 4, properties); (e) the Ukraine plant at Kryvyi Rih cannot be safely restarted after missile strikes
(6-K 2026-09-25, `0001243429-26-000084`).

## THE STANDING RULE
The rule concerns the buyer's own conduct. A part-interest bought for cash, without borrowing, and sized so that a large fall
harms nothing else puts the buyer at no risk of ruin: "We are never going to risk what we have and need for what we don’t
have and don’t need." **[M2012-081]**. Nothing about this name changes that. Its own exposures are Q9's, which this file
does not reach.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test, applied to the filings.** Understanding is "a reasonable fix on about what the earning power and competitive
  position will look like in five or 10 years" **[M2012-065]**. The business is a set of integrated steel producers in
  Europe, North America, Brazil and (through a joint venture) India, and iron-ore mines in Canada and Liberia. The filing
  lays out the key variables plainly. They are (1) the cost of the European plants against imported steel and against
  carbon costs; (2) capacity utilization, 65% for the European industry as reported by Eurofer and cited in the 20-F;
  (3) trade protection (safeguard, the proposed TRQ, CBAM from 2026-01-01); (4) the iron-ore cost of the mines; and
  (5) the capital needed to keep the plants and to change them to lower-carbon routes. The cash flows, segment results,
  capacities, shipments and prices are all filed, segment by segment, for a decade.
- **Commodity dependence is not a Q1 stop.** The framework places a commodity business's question at Q2, the cost
  position read from the filings ("if you can’t make a decision on something like PetroChina off the figures, forget about
  going further" **[M2008-069]**; "We don’t think we can predict commodity prices." **[M2016-025]**). The figures here are
  sufficient to read the cost position, at least against imports and the named producers, so the question can be put.
- **Against IN, written down.** "We view change as more of a threat into the investment process than an opportunity." **[M1999-063]**. The filing itself expects
  decarbonization to change the industry's structure, and its European results now turn on a policy decision (the TRQ)
  that was not yet in force at the filing date. If either variable were the deciding question, Q1 would be closer to TOO
  HARD (NATURE) **[M2000-105]**. I read it otherwise. Neither variable has to be forecast to answer the question that
  decides, which is whether the business is the low-cost producer in its main part. The filings answer that from the past
  decade. "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**; I record that the doubt here is about the industry's future, not about
  what the business is or how it earns.
- **VERDICT: IN**. The economics can be read from the figures **[M2012-065]**, **[M2008-069]**; the deciding question moves
  to Q2 under the commodity-business paragraph. (Alternative reading recorded: TOO HARD (NATURE) at Q1 on the
  decarbonization change **[M1999-063]**; not taken, for the reason above.)

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
**The parts table first** (the framework's business-of-parts paragraph; "lumping them together [...] impedes analysis"
**[L2008-005]**). Segment profit for 2021 to 2025, $M, from the segment notes of the 20-Fs FY2023 (`0001243429-24-000005`)
and FY2025 (`0001243429-26-000020`). The segments were recast from 2024, so the old Europe segment (which held what is now
Sustainable Solutions) is matched by Europe plus Sustainable Solutions in 2023 to 2025 (the 2023 figures reconcile: 879 +
225 = 1,104). The India and JVs part is equity-method income, which is below operating income.

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year | Share of the positive parts | Castle | Decides? |
|---|---|---|---|---|---|---|---|---|---|
| Europe (with Sustainable Solutions) | 5,672 | 4,292 | 1,104 | 443 | 664 | 12,175 | 26% | commodity flat and long steel behind trade measures; see below | **yes, the largest part** |
| North America | 2,800 | 2,818 | 1,917 | 1,310 | 2,205 | 11,050 (9,192 without the 2025 Calvert gain of 1,858) | 24% | not judged (does not decide) | no |
| Brazil | 3,798 | 2,775 | 1,461 | 1,399 | 608 | 10,041 | 22% | not judged | no |
| Mining (Canada, Liberia) | 2,371 | 1,483 | 1,144 | 770 | 789 | 6,557 | 14% | the filing claims "a steeper cost curve" and "low-cost iron ore"; not judged | no |
| India and JVs (equity income, all associates and JVs) | 2,204 | 1,317 | 1,184 | 779 | 806 | 6,290 | 14% | not judged; counted as dividends received at Q7 | no |
| ACIS, then Others (Ukraine, South Africa, Kazakhstan to 2023, corporate) | 2,705 | (930) | (3,021) | (642) | (633) | (2,521) | n/a | loss-making | no |

No part carries more than half. The largest part decides, and that is Europe, whether or not the Calvert bargain-purchase
gain is counted in North America. The file closes on Europe's castle. The other parts are carried to Q7 as ordinary
businesses at no growth, if Q7 is reached.

**The castle tests, on the deciding part.** "why is that castle still standing? And what’s going to keep it standing or
cause it not to be standing five, 10, 20 years from now." **[M1995-038]**
- **What keeps it standing, and how permanent.** The filing's "enduring competitive strengths" are scale (74.6 Mt of
  capacity group-wide), a "world-class mining business" (72% iron-ore self-sufficiency in 2025), a "leading market share
  (approximately 16% of the worldwide market) in automotive" with engineers embedded at carmakers, and a broad product range
  (20-F, Item 4). In Europe the filing names one more thing that keeps it standing, and that one is not the company's own:
  trade protection. "the new TRQ mechanism and an effective CBAM will provide the foundation" (20-F, Item 4). A castle whose
  foundation is a regulation proposed by a government is not shown to be permanent **[M1995-038]**.
- **The money test, and the attacker.** The attackers are already inside the walls. "Periods of weak global steel demand
  heighten the risk of increased volumes of unfairly traded imports into ArcelorMittal’s key markets—Europe, North America
  and Brazil—placing downward pressure on prices and demand for its products" (20-F, Item 3.D). Eurofer puts European
  capacity utilization at 65%, against the "healthy levels of 80–85%" the TRQ aims at (20-F, Item 4).
- **Pricing power.** Europe's average steel selling price ran $986 a tonne (2021), $1,191 (2022), $1,039 (2023, old
  segment), then $910 (2024) and $894 (2025) on the new segment. Profit moved with the spread: 2025 operating income rose
  "primarily due to a positive price-cost effect" while the price fell 1.8% (20-F FY2025, Europe). The company takes the
  market's price. The strength of a business shows in "the agony they go through in determining whether a price increase
  can be sustained" **[M2005-020]**, and here no price is set by the company to be agonized over.
- **Unit volume.** Europe crude steel production was 43.9 Mt in 2019 (with part of the Italian plants), 36.8 Mt in 2021,
  31.9 Mt in 2022, 28.8 Mt in 2023 and 29.2 Mt in 2025. Shipments fell from 33.2 Mt (2021) to 28.4 Mt (2025) (20-Fs FY2021,
  FY2023, FY2025). In 2025 three European blast furnaces were idle or being shut (Fos-sur-Mer #1, Dąbrowa Górnicza #3,
  Gijón B).
- **The low-cost position** (the commodity-business paragraph's question: "we would measure it, probably, more by cost of
  production than we would by whether copper was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**). No filing
  read states that the European plants are low-cost. The filing claims a cost advantage only for the mines ("a steeper cost
  curve", "low-cost iron ore reserves"). For Europe it states the opposite against the producers that ship in: "ArcelorMittal
  may be at a competitive disadvantage relative to steelmakers having more or all of their production in developing
  countries. [...] this competitive disadvantage could be severe and has resulted, and in the future may result, in
  production cuts due to relatively higher carbon costs rendering production structurally unprofitable" (20-F, Item 3.D).
  "commodity businesses have risk unless you’re the low-cost producer, because the low-cost producer can put you out of
  business." **[M1997-010]**; "In an unregulated commodity business, a company must lower its costs to competitive levels or
  face extinction." **[L1994-035]**; "the guy with the lower cost comes in and kills you." **[M2001-013]**.
- **The brand, and the low bid.** The automotive engineering ties are the best evidence for the castle. Carmakers co-design
  with the company years before launch, and some of that steel is not bought on the low bid. But the filing itself says
  "Commodity steel markets will inevitably remain an important part of ArcelorMittal’s steel portfolio", and its stated aim
  there is that "a lean cost structure should limit the downside in weak markets" (20-F, Item 4, strategy). That is the
  commodity producer's aim, not the franchise's. No filing read gives the automotive share of European volume, so the
  automotive franchise cannot be shown to carry the part.
- **Ask the competitors.** No competitor's view of this company was found in the filings read. Not available on the public
  record used here.
- **Widening or narrowing.** The part is narrowing on the filed record. Europe's operating margin (operating income over
  segment sales) was 6.5% (2017), 4.0% (2018), -2.9% (2019), -5.1% (2020), 13.1% (2021), 9.1% (2022), 2.9% (2023), 1.1%
  (2024) and 1.7% (2025). Volume is falling and plants are idled, and the filing calls the trade measure "imperative".
  "whether it’s likely to widen further or shrink on you" **[M1999-108]**: on these figures, it shrinks.
- **What could destroy it.** The carbon cost (EU ETS, with free allowances withdrawn as CBAM phases in), Chinese exports
  (the filing expects them "at or above current peak" if Chinese demand falls without closures), and substitute materials
  (20-F, Item 3.D). Each is named by the filer. The product "can be shipped in from abroad very easily" **[M2007-116]**.

**The competitor row.** The 20-F names no competitors as such. Nippon Steel, Cleveland-Cliffs, U.S. Steel, voestalpine,
POSCO and Ternium appear only as partners, counterparties or co-owners. **CONVENTION of this run:** the rivals are chosen,
not named by the filer. They are **Nucor** (10-K FY2025, `0001193125-26-071575`; the U.S. mini-mill, the field's
benchmark for cost), **Cleveland-Cliffs** (10-K FY2025, `0000764065-26-000025`; an integrated U.S. producer that bought
ArcelorMittal USA in 2020) and **POSCO Holdings** (20-F FY2024, `0001193125-25-104983`; an integrated producer of comparable
breadth; FY2025 figures not found in its tagged data, so the span ends at 2024). Rationale: three SEC filers that make steel
by the integrated or the scrap route in the company's markets or at its scale. Ternium was left out for the contamination
stated at the top. **Named European and Asian rivals that do not file with the SEC, flagged:** thyssenkrupp, Tata Steel
(Netherlands and UK), voestalpine, Salzgitter, SSAB, Nippon Steel, China Baowu and the other Chinese exporters. The
European rivals, who would decide the cost comparison for the deciding part, are not on the SEC record. The figures below
are the companies' tagged XBRL figures, transcription flagged per operator rule 4 and not checked line by line against
each rival's statements.

| Company | Metric | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Span average |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ArcelorMittal, group | operating margin | 7.9% | 8.6% | -0.9% | 4.0% | 22.2% | 12.9% | 3.4% | 5.3% | 2.9% (5.9% with the Calvert gain) | 7.4% |
| ArcelorMittal, Europe | operating margin | 6.5% | 4.0% | -2.9% | -5.1% | 13.1% | 9.1% | 2.9% | 1.1% | 1.7% | 3.4% |
| Nucor | pre-tax margin (no operating line is tagged) | 8.6% | 12.9% | 7.9% | 4.1% | 25.2% | 24.7% | 18.1% | 9.4% | 7.9% | 13.2% |
| Cleveland-Cliffs (a steelmaker from 2020) | operating margin | n/a | n/a | n/a | -2.7% | 19.6% | 8.4% | 3.0% | -4.0% | -8.5% | 2.6% (2020-2025) |
| POSCO Holdings | operating margin | 7.0% | 6.2% | 5.0% | 3.6% | 11.5% | 5.1% | 3.6% | 2.0% | n/f | 5.5% (2017-2024) |

The returns on capital over the same span, pre-tax, on equity plus net debt: ArcelorMittal 11.5% a year on average for
2016 to 2025 (operating income over equity plus net debt less equity-method investments; 2025 without the Calvert gain).
Two boom years carry most of that: 37.7% in 2021 and 21.8% in 2022, against -1.4% to 13.2% in the other years and 3.3% in
2025. Nucor averaged 22.3%, Cleveland-Cliffs 6.6% (2020 to 2025) and POSCO 5.3% (2016 to 2024). (Scripts: `rivals.py`,
`q7_computation.py` in the research folder.)

**The field's returns over the last full cycle, judged in words.** Over 2017 to 2025, which runs from the 2019 to 2020 trough
through the 2021 to 2022 peak to the 2024 to 2025 trough, the group sits in the middle of the named field. It is below the
scrap-based low-cost producer, Nucor, and above Cleveland-Cliffs and POSCO. Its deciding part, Europe, sits near the bottom
of the field, at a few percent of sales on average and about one to two percent in the last two years. Once the one boom is
averaged in, the field's returns are ordinary, and the deciding part's are below ordinary. "A truly great business must have an
enduring "moat" that protects excellent returns on invested capital." **[L2007-004]**; "you can have only two competitors
and they’re still terrible businesses, they beat each other’s brains out." **[M2013-052]**. The price is set by the import
offer ("whatever he charged for gas was my price." **[M2012-109]**). The cost advantage is held by others ("being the
low-cost producer is all-important" **[L2000-017]**).

**A change for the better?** The TRQ proposed on 2025-10-07 and CBAM's financial phase from 2026-01-01 could raise
European prices and utilization. The filing describes them as protection to come, not as a change already shown in the
figures. Crediting them would be a forecast of policy, which the foundations exclude ("macro conclusions are — just never
enter into the discussion." **[M2000-094]**). The framework's Q2 convention credits a change for the better only on a full cycle, and none has begun. Recorded as the alternative reading, not taken: an analyst who reads the TRQ as a
change for the better already under way would close TOO HARD (NATURE). The re-look would be the first fiscal year in which
European steel volume falls with the TRQ in force.

- **VERDICT: OUT.** The deciding part is a commodity producer whose own filing states a cost disadvantage against the
  producers that ship in **[M1997-010]**, **[L1994-035]**, whose price is set by the import offer **[M2012-109]**, **[M2007-116]**,
  whose volume and margin are narrowing **[M1999-108]**, and whose field earns ordinary returns over the full cycle
  **[L2007-004]**, **[M2013-052]**. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**. (Alternative recorded:
  TOO HARD (NATURE), on the reading that no filing places the European plants on a cost curve against other European
  producers, who are not SEC filers, **[M2000-019]**; not taken, because the filing states the cost disadvantage against
  the imports that set the price.)

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED (closed at Q2; the ten balance sheets are read in Step 0).
## Q5 — WHO RUNS IT. NOT REACHED (closed at Q2; integrity facts found are under AFTER THE STOP).
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED (closed at Q2).
## Q7 — WHAT IS IT WORTH. NOT REACHED as a question; computed below under COMPUTATION, NOT A CLEARANCE, at the owner's request.
## Q8 — IS IT BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED (facts under AFTER THE STOP).
## Q10 — IS IT THE FAT PITCH. NOT REACHED.
## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## COMPUTATION, NOT A CLEARANCE (the file closed at Q2; Q7's construction applied at the owner's request; no entry language)
Built by Q7's range convention and its specifics, in $M unless per share. Script and output:
`q7_computation.py`, `q7_computation_output.txt`.
- **Cash input.** Owner cash is cash from operations as filed, which comes after interest paid and received, income tax
  paid, pension contributions and working-capital movements (specific (d), counted as filed), and takes in dividends received from
  associates and joint ventures (the equity-method convention). From that are deducted capital spending, lease principal and
  dividends paid to minority partners. **Tax:** the company's own tax as paid. The Luxembourg losses carry forward
  indefinitely (20-F, note on income tax), so the convention on shelters that run out inside ten years does not apply.
- **(e) Maintenance case central.** The filing allows the guess. For 2026 the company guides $2.8bn to $3.1bn of
  "maintenance and other ongoing capital expenditures", $1.4bn to $1.6bn of strategic growth and $0.3bn of decarbonization
  (20-F, capital expenditures). The midpoint, $2.95bn, matches 2025 depreciation of $2.945bn. The maintenance guess for
  each year is therefore that year's depreciation, and the all-spending case is shown beside.
- **(a) Cycle base.** The first window year, 2021, is the peak: the filer describes steel prices at "the highest levels"
  that year (20-F FY2021), and owner cash ran $6.4bn to $7.1bn in 2021 and 2022 against $36M to $1.8bn in 2024 and 2025.
  The base is therefore the last full cycle, trough to trough on owner cash, from 2020 (a local trough between 2019 and 2021)
  to the 2024 to 2025 trough: **2020 to 2025**. Averages: maintenance case $3,767M, all spending $2,774M.
- **(c) Acquisitions.** Net purchases of businesses and joint-venture stakes, after disposals, averaged $266M a year over
  2020 to 2025 ($1,598M in all, about a tenth of owner cash before purchases, so not a serial acquirer). They are deducted
  from both ends, with total growth credited (the default pair). The organic pair (purchases left out) is shown beside. The
  filer reports no organic growth rate, so sales growth stands in there. Calvert (closed 2025-06-18, inside the window) is in
  the figures from that date.
- **All-equity add-back.** Net interest paid ((interest paid less interest received) × (1 − 23.87%), the Luxembourg statutory
  rate in the 20-F; **CONVENTION of this run:** the statutory rate is used for the interest shield because the group's cash tax
  is a blend across countries and no blended marginal rate is filed) averaged $304M over 2020 to 2025.
- **Growth and (f) the cap.** Shown growth between the averages of successive cycles (2016 to 2020, then 2020 to 2025) is
  28.7% a year on the maintenance case and 21.4% on all spending. Carried ten years, 28.7% would put owner cash at about 70%
  of sales, against a highest share in the filings read of 9.0% (2021). That is absurd, so the rate is cut to the business's
  own sales growth between the same cycles: **0.64% a year**. There is zero nominal growth after year ten.
- **(e) The inversion.** Growth spending (capex above depreciation, $0.5bn to $1.9bn a year since 2021) buys only the 0.64%
  growth. The all-spending growth case is therefore worth less than the maintenance-only no-growth case. The maintenance
  no-growth case is the **top** and the all-spending growth case the **bottom**: "growth can destroy value", the inversion
  the text names as the finding.
- **Net debt** at the latest filed date, 2026-06-30: **$9.5bn** (half-year 6-K: debt $14.4bn less cash $4.9bn). The company's
  definition includes its lease liabilities in debt. Not counted, and stated: $5.0bn of receivables sold without recourse
  (year-end 2025), the €7.0bn damages claim of the Italian commissioners (contested), and minorities' claims beyond the
  dividends paid to them.
- **Rate:** 5.60%, US Treasury 30-year par, 2026-10-09. **Shares:** 754.04M. **Price:** $63.47.

**The value range (central figure, all-equity basis):** whole business $52,815M to $67,945M, so **$57.44 to $77.51 a
share** against **$63.47**. Width 1.29 to 1. **Equity-only beside it:** $62.46 to $82.90 a share.

**The floor, tested first** (the Q7 convention of about ten percent; "we don’t want to buy equities where our real
expectancy is below 10 percent" **[M2003-149]**). The expected return at the price is 5.16% (the bottom
case) to 6.63% (the top case) on the all-equity basis, and 5.51% to 7.31% on the equity-only basis. **No case of the range
earns the floor at the price**, so Q7, had it been reached, would close OUT on the floor whatever the width.

**The fair price** (Part VII: each end valued at ten percent, the two averaged, after the company's own tax):
**$32.10 a share on the all-equity basis (the central figure)**; **$40.57 a share on the equity-only basis (beside it).**

Shown beside, never deciding:

| Case (all-equity unless said) | Range per share at 5.60% | Width | Fair price | Return at $63.47, the two ends |
|---|---|---|---|---|
| Central: cycle 2020-2025, maintenance central, purchases deducted | $57.44 to $77.51 | 1.29 | $32.10 | 5.16% to 6.63% |
| Equity-only, same | $62.46 to $82.90 | 1.33 | $40.57 | 5.51% to 7.31% |
| Organic pair (purchases left out, sales growth standing in) | $64.08 to $83.82 | 1.26 | $35.71 | 5.64% to 7.10% |
| Literal window 2021-2025, purchases deducted, sales growth | $62.86 to $89.83 | 1.36 | $37.05 | 5.56% to 7.54% |
| Literal window, its own decline (-31.7% a year) carried as the bottom | $(0.91) to $89.83 | 8.8 | $20.99 | 0.19% to 7.54% |
| Ten-year 2016-2025 (purchases before 2020 not deducted) | $48.39 to $61.35 | 1.21 | $25.06 | 4.50% to 5.44% |
| All spending at both ends (the PG specific, depreciation variant set aside) | $54.00 to $57.44 | 1.05 | $25.52 | 4.90% to 5.16% |

The best case of any construction, the literal window's peak-weighted top, returns 7.54% at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down, not weighed; no verdict; the box unchanged (operator rule 2) **[M1997-127]**.)*
- **Q3 (capital).** Capital spending has run above depreciation every year since 2021, by $0.5bn to $1.9bn. Guidance for 2026
  is $4.5bn to $5.0bn against 2025 depreciation of $2.9bn, with $0.3bn on decarbonization (20-F). Pre-tax return on
  operating capital averaged 11.5% over 2016 to 2025, and was 3.3% in 2025 (Q2 table).
- **Q4 (accounts).** The 2025 operating income of $3,628M includes a $1,736M bargain-purchase gain and a $122M gain on
  pre-existing relationships from Calvert (20-F note 2.2.4). Without them it is $1,770M. The Executive Chairman's and CEO's
  annual bonus weights "EBITDA targets at Group level: 40%", and other executives' bonuses use "EBITDA targets at Group,
  segment or Business unit level" (20-F, compensation). $5.0bn of receivables sold without recourse
  keep trade receivables off the balance sheet. The 2025 Calvert cash outflow is shown net of $1,638M cash injected by
  Nippon Steel. Large impairments recur: $1,927M (2019), $1,026M (2022), $1,038M (2023), plus a $1,405M impairment of
  equity-method investments (2023).
- **Q5 (integrity; the box line carries the flag).** (1) On 2026-01-26 the Extraordinary Commissioners of Acciaierie
  d'Italia (the former Ilva plants, which the company co-controlled with the Italian state's Invitalia from 2021) served a
  writ before the Court of Milan. The claim alleges "that ADI was mismanaged and that value was intentionally transferred from
  ADI to ArcelorMittal (causing ADI to become insolvent)", and it "seeks damages valued at €7.0 billion, with an alternative
  valuation of €3.65 billion". The company "categorically rejects any and all allegations" and has itself brought an
  arbitration against Italy claiming more than €1.8bn (20-F FY2025). (2) Safety: 46 deaths in the Kostenko coal-mine
  explosion in Kazakhstan on 2023-10-28, after earlier accidents at Abayskaya (2021), Temirtau (2022) and Lenina (2022)
  (20-F FY2023). The Kazakh business was sold to a state fund in December 2023. Six deaths in five events in 2025 (20-F
  FY2025). The Executive Chairman and the CEO "voluntarily renounced their 2023 and 2022 Performance Bonus" "due to the high
  number of fatalities" (20-F, compensation). (3) Control: the Significant Shareholder (the Mittal family interests) held 44.55% at 2026-06-30. It sells
  shares back to the company alongside each buyback so as to keep its voting share below the 45% standstill of the 2006
  memorandum (half-year 6-K). The CEO is Aditya Mittal; the Executive Chairman is Lakshmi N. Mittal.
- **Q6 (money and owners).** Buybacks of $5,170M (2021), $2,937M (2022), $1,208M (2023), $1,300M (2024), $262M (2025) and
  about $0.5bn in the first half of 2026. The share count fell from 1,019.5M (2016) to 754.0M (mid-2026). No stated price or
  value test for the buybacks was found in the filings read. The base dividend was raised to $0.55 a share for 2025.
  Purchases in the window include CSP in Brazil (2023), a 28.4% stake in Vallourec (2024; part sold in 2026 for $0.7bn) and
  Calvert (2025).
- **Q9 (ruin).** Net debt rose from $2.2bn (2022) to $9.5bn (2026-06-30). Receivables sold $5.0bn. $5.5bn of undrawn
  credit lines (20-F). The Ukraine plant cannot be restarted (6-K 2026-09-25). The ADI claim is above.

---
## THE BOX
**OUT at Q2** (the castle): the deciding part, Europe, is a commodity steel producer whose own filing states a cost
disadvantage against the imports that set its price, with volume and margin narrowing and ordinary returns for the field over
2017 to 2025. **Integrity facts recorded, not judged** (the ADI writ alleging value intentionally transferred, €7.0bn;
the Kazakhstan fatalities; the controlling holder's buyback parity agreement). COMPUTATION, NOT A CLEARANCE, beneath the
stop: range $57.44 to $77.51 a share against $63.47, no case earning the floor (best 7.54%); fair price $32.10 all-equity,
$40.57 equity-only. Alternative readings recorded, not taken: TOO HARD (NATURE) at Q1 (decarbonization) and at Q2 (no
European cost curve on the SEC record; the TRQ as a change for the better).

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `ab858d91`); written question by question; committed after Step 0
      to Q1 (`42ae90b3`), after Q2 (`2194f7e2`), and at the close.
- [ ] If dispatched to an analyst: the brief allowed the per-question commits (yes). The lock and the fold are the
      dispatching session's (operator rule ten), and I did not see them. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. What was seen by accident (the
      commit subjects of another steel company's run, other research-folder names, memory lines) is declared under
      contamination at the top and not used. That company was left out of the competitor set for that reason.
- [x] Every v5 id resolves (checked by `check_ids.py` in the research folder). Every filing fact has its accession. The
      rivals' figures are tagged XBRL, flagged.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; everything after it is headed COMPUTATION or
      written as facts, not weighed.
- [x] Owner cash after every real cost, from the filed cash-flow statements, never a net-income proxy (operator rule 5).
      The sovereign is from the US Treasury. The price is an aggregator quote, flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q1, Q2). Facts for later questions
      are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor is cited (not a point-in-time run; the anchor is today).
- [x] `tools/run.py` produced no arithmetic for this filer (US-GAAP tags only). Nothing it prints was used. The
      arithmetic was done by hand and the scripts are kept.
- [x] `python tools/check_framework.py` PASS before the closing commit (recorded below).
- Shortfalls, stated honestly: the rivals' figures were not checked against their filed statements line by line. The
  European rivals that decide the cost comparison file nowhere I could read. Share-based pay was not resolved to a cash
  figure. Pre-2019 lease principal could not be separated. Net purchases before 2020 were not deducted in the ten-year case.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. First, the commodity-business paragraph sends a file to TOO HARD (NATURE) "where no filing states" the cost
position, and to OUT for "a high-cost producer". Here the filer states its European cost disadvantage against imports
(carbon cost, "structurally unprofitable"), but no SEC filing places it against the European producers that are its
direct rivals. The text does not say whether a disadvantage stated against one set of rivals (imports) is enough to call a
producer high-cost when its position against the others is unknown. I took the filer's own statement against the
price-setting imports as sufficient for OUT and recorded TOO HARD (NATURE) as the alternative. Second, the change-for-the-better
convention (credited only on a full cycle, TOO HARD (NATURE) until then) does not say whether a protection that is proposed
but not yet in force, here the EU tariff-rate quota, counts as a "change" at all. I read it as a policy forecast, which the
foundations exclude, and so not a change. Third, specific (a) defines the cycle by owner cash but gives no rule for choosing
between overlapping trough-to-trough spans when the series has several local troughs (2016, 2018, 2020, 2024). I chose the
latest full span ending at the latest trough (2020 to 2025) and showed the literal window and the ten-year average beside
it. The floor test gave OUT on every one of them, so the choice did not decide anything here, but it could elsewhere. And a
tooling note: `tools/run.py` and `Screens/cover_shares.py` both fail silently on IFRS filers (no `us-gaap` tags, no parsed
cover count), so every IFRS 20-F name is done by hand.
