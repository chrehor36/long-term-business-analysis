# Company Run — Mitsubishi Corporation (TSE: 8058; OTC ADR: MTSUY) — 2026-10-12
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its source document (this name files nothing
with the SEC; each document is recorded by its exchange disclosure number and date in place of an accession); a STOP that
returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED. Copied to its dated name before any fetch.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session (overnight cycle, 2026-10-12), after the run was committed: `PORTFOLIO.md` names no Mitsubishi Corporation (8058, MTSUY); not held.*

**Dispatched run.** Dispatched by the operator's session under `Screens/_daily/_dispatch_brief.md` with stated departures
(no SEC filings; the company line and the lines of evidence left to the analyst; the dispatcher's fetches of the company
site refused). The lock in `Screens/_daily/` was present when this run started (written by the dispatching session).

**Contamination, declared and not used.** (1) The session context that opened this run carried the repository's recent commit
subjects, which include an earlier run filed under this ticker with Q7 figures and a fold note saying that run was of Mitsui &
Co. (MITSY) under the MTSUY slot by a dispatcher's ticker error, and that this ticker was still owed. I did not open that file or the fold;
its figures were seen in a commit subject only and are not used here. (2) A memory index line seen at session start speaks of
the gate-clearers in general; not used. (3) The framework's own text names a MITSY regression run and the trading-house row
**[M2023-031]**; those are the governing text and are read as such, not as a verdict on this name.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Ticker check.** The company read is Mitsubishi Corporation, 三菱商事株式会社, securities code 8058, TSE Prime,
  2-3-1 Marunouchi, Chiyoda-ku, Tokyo (cover of the FY2025 results, "FINANCIAL RESULTS FOR THE YEAR ENDED MARCH 2026",
  May 1, 2026, TDnet 140120260430515680, and the Japanese 決算短信 TDnet 140120260430515679; the buyback notice of
  2026-03-25, TDnet 140120260324588068, is signed 三菱商事株式会社, 代表取締役 社長 中西 勝也, コード 8058). Not Mitsui & Co.
  (8031), not Mitsubishi Electric, Heavy Industries or UFJ. The ADS ratio (one share per ADS) is the brief's, from the
  depositary's F-6EF of 2026-03-04 (accession 0001193805-26-000216); I did not re-read it.
- **Routes to the primary documents.** mitsubishicorp.com refused every fetch (HTTP 403, from curl and from the Windows
  HTTP stack); EDINET's API needs a key and refused; the Internet Archive was offline. The home exchange's own archive
  served the company's filings: the JPX listed-company page for code 8058 lists the company's TDnet disclosures from
  2016-11 to 2026-08 with links at `www2.jpx.co.jp/disc/80580/<TDnet id>.pdf`; the English results of FY2023 and FY2024
  came through the London Stock Exchange's RNS PDF service, where the company also files them. Each document below is
  the company's own, by its TDnet or RNS number.
- **Price:** ¥4,596 (TSE close 2026-10-09; the TSE was shut on 2026-10-12, Sports Day, and no bar exists for that date);
  ADS $29.20 (OTC close 2026-10-12). Both from Yahoo Finance's chart service, an aggregator, **flagged** (operator rule 5:
  live quotes only).
- **Shares** (one class, common): 3,710,528,742 issued less 47,834,615 treasury = **3,662,694,127** outstanding at
  2026-06-30 (Q1 FY2026 決算短信, 2026-08-03, TDnet 140120260731505791, p. 1, (3)発行済株式数). Checked against issued less
  treasury at 2026-03-31 (4,028,926,353 less 367,427,682 = 3,661,498,671; FY2025 results, TDnet 140120260430515680, 4.(3))
  and the cancellation of 318,397,611 treasury shares on 2026-04-30 (notice of 2026-03-25 with its correction of the same
  day, TDnet 140120260324588068 and 140120260325589148). No buyback or issuance notice appears in the JPX list after
  2026-03-25 except stock-option grants to executive officers (five notices of 2026-05-19, C2 to C6 plans).
  `python Screens/cover_shares.py MTSUY` returned "NOT AN SEC REGISTRANT"; the count is by hand.
- **Market cap:** ¥4,596 × 3,662.694M = **¥16,834bn** (about $105bn at the ADS price, $29.20 × 3,662.694M).
- **Sovereign for the earnings currency (yen):** JGB 30-year **4.136%**, 2026-10-08, the latest row of Japan's Ministry
  of Finance `jgbcme.csv` fetched 2026-10-12 (the 10-year is 3.089% the same day).
- **Filings read** (operator rule 4): the annual 決算短信 (IFRS, consolidated) for every fiscal year ended March 2017 to
  March 2026 from the JPX archive (TDnet 140120170509462328, 140120180507427945, 140120190508416691,
  140120200507405804, 140120210506406819, 140120220509536316, 140120230508560340, 140120240426578542,
  140120250409511808, 140120260430515679); the English results for the years ended March 2024, 2025 and 2026 (RNS
  9867M_1-2024-5-2, RNS 2381H_1-2025-5-2, TDnet 140120260430515680); the Q1 FY2026 決算短信 (TDnet 140120260731505791).
  The company's year ends 31 March; "FY2025" below means the year ended 2026-03-31, the company's own label.
  No 10-K, 20-F or proxy exists; the notice of the 2026 general meeting (English, TDnet 140120260519541439) stands for
  the proxy. **One figure cross-checked:** operating cash flow for the year ended 2026-03-31, ¥1,490,041 million, is the
  same in the English statement of cash flows (TDnet 140120260430515680, p. 22) and the Japanese
  (営業活動によるキャッシュ・フロー, TDnet 140120260430515679).
- **The business, from the company's own documents** (the FY2025 results, TDnet 140120260430515680, segment note and
  "Business Risks"; the Q1 FY2026 決算短信, TDnet 140120260731505791). A Japanese general trading company that trades
  and invests across eight reporting groups in the year ended 2026-03-31 (Environmental Energy, Materials Solution,
  Mineral Resources, Urban Development & Infrastructure, Mobility, Food Industry, Smart-Life Creation, Power Solution;
  seven from April 2026, the first being Energy & Power Solution). Its largest assets by its own list: a 50% interest in
  the BMA steelmaking coal business in Queensland through Mitsubishi Development (MDP), "the world's largest steelmaking
  coal business", PP&E ¥1,160.6bn; 20.4% of Anglo American Sur (Los Bronces, Chile; bought for US$4.51bn, carried at
  ¥216.5bn after impairments and a ¥53.2bn partial reversal in FY2025); 40% of Quellaveco (Peru; investment and loan
  ¥523.5bn); Montney shale gas and LNG Canada; 50% of Lawson (an equity-method joint venture with KDDI since 2024-08-15,
  ¥502.6bn); Eneco in Europe (goodwill ¥167.0bn). **Recent capital events, from the filings:** a three-for-one split on
  2024-01-01 (FY2023 results, RNS 9867M_1-2024-5-2, Note 3); Lawson deconsolidated after KDDI's tender offer (2024);
  sale of the Blackwater and Daunia coal mines to Whitehaven for US$1.6bn plus up to US$0.45bn contingent, closed
  2024-04-02 (subsequent-events note, FY2023 決算短信, TDnet 140120240426578542); a ¥1tn buyback, tender offer and market,
  2025-04-04 to 2026-03-24, 318,397,611 shares cancelled 2026-04-30; a tender offer for Mitsubishi Shokuhin (2025-05 to
  2025-07, notices TDnet 140120250507532233 and 140120250702507277, not read beyond their titles); the purchase of
  Aethon (Haynesville shale gas, about 2.1 Bcf a day of equity production) for US$5,200M from Ontario Teachers' Pension
  Plan, decided 2026-01-16 and completed 2026-07-14 (notices TDnet 140120260114534061 and 140120260714593288);
  Chiyoda Corporation to become an equity-method affiliate after its June 2026 meeting (notice TDnet
  140120260128539856). No rename, merger by share issue or spin-off found in the JPX list from 2016-11 to 2026-08.
- **The balance sheets, eleven year-ends, March 2016 to March 2026, read before the income account** **[M2025-032]**
  (¥bn; from the 決算短信 statements of financial position named above; table in the research folder's `notes.md`):
  total assets 14,916 to 24,152; equity attributable to owners 4,593 to 9,441 (ratio 30.8% to 39.1%); bonds and
  borrowings 6,043 to 5,747, so net interest-bearing debt fell from about 4,316 (less cash 1,501 and time deposits 226)
  to 3,888 (the company's own figure, leases excluded) while equity doubled; goodwill and intangibles 291, then 1,010 on
  Lawson's consolidation (March 2017), 1,395 on Eneco (March 2020), 743 after Lawson left (March 2024), 913 (March
  2026); equity-method investments 2,870 to 5,213; inventories 1,034 to 2,077, and since March 2019 (1,214) up 71%
  against revenue up 17% (FY2018 ¥16.10tn to FY2025 ¥18.92tn; revenue before FY2017 is on the old net basis and is not
  compared), with March 2025 to March 2026 +18% against revenue +1.6%; trade receivables (current) 2,923 to 4,186;
  retained earnings 3,226 to 6,954; treasury stock ¥1,113bn at March 2026 before the cancellation. **What the figures
  cannot say:** of March 2026 equity of ¥9,441bn, ¥2,386bn is exchange differences on translating foreign operations,
  so a quarter of the yen book is the yen's fall, not retained cash; lease liabilities ran about ¥1.5tn while Lawson
  was consolidated and ¥0.76tn after. No item builds without explanation except inventories in the last year, which
  the filing ties to higher market prices and the new salmon businesses (Grieg, Cermaq) without splitting the amounts.

- `python tools/run.py MTSUY` printed "not an SEC filer ... UNRESEARCHED, not UNKNOWABLE" and no arithmetic. Every
  figure below is by hand from the filings named, in `Test Runs/_research 2026-10-12 MTSUY/`.

## THE FOUNDATIONS (not a gate)
A share is a business: would I be content to own this "if the market closed for five years" **[M1997-109]**? The
question here is what the business will earn, and its earnings move with prices no one in it sets. For a dollar holder
the ADS is also a yen holding; the rows treat "currency-related investments" as making little sense "unless we’re
getting paid extremely well for having them" **[M2011-025]**, which bears on the buyer and not the business.
**Contrary evidence, written down as found** **[M1997-127]**: (1) the speakers bought this company and four like it,
"understandable companies" whose businesses "we could understand as a group, although it didn’t mean we had deep
understanding on any" **[M2023-031]**; the 2023 letter names Mitsubishi among five that "follow shareholder-friendly
policies" and "reduced the number of its outstanding shares at attractive prices" **[L2023-008]**. These are rows about
named companies: weighed, never a verdict (Q2's CONVENTION of 2026-10-07). (2) The deciding part's competitive position
is partly readable: the company calls BMA the world's largest steelmaking coal business and Quellaveco "highly cost
competitive" (FY2025 results, Business Risks (5)), and the rows would measure a copper miner "more by cost of production
than we would by whether copper was selling for $2.00 a pound or a dollar a pound" **[M2006-004]**. (3) Mineral Resources
has earned a profit in every year since the year ended March 2016.

## THE STANDING RULE
Bought with the buyer's own money and held unlevered, a part-interest in a ¥16.8tn company does not put the buyer at
risk of ruin; "borrowed money has no place in the investor's tool kit" **[L2014-005]**. The yen exposure is the
buyer's choice of currency, a sizing matter, not ruin. The rule binds the buyer's conduct, which this run does not see.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look
like in five or 10 years" **[M2012-065]**; the analyst identifies "the key variables" and evaluates "how predictable they
were first, because that is the first step. If something is not very predictable, forget it." **[M1998-044]**. A holding
company is understood by its parts: the CONVENTION of Q1 and Q2 (2026-10-06) makes a part "matter" when it carries more
than half of five-year operating profit or, where none does, is the largest, and "a part that cannot be [understood], and
that matters, keeps the whole outside the circle" (Q1, A holding company), since "if you have doubts about something
being into your circle of competence, it isn’t" **[M2002-092]**.

**The parts table** (the filer reports profit attributable to owners by segment, not operating profit; that is the
measure used, a CONVENTION of this run, rationale: it is the only segment profit the filings give for all five years.
Segments were regrouped in April 2024 and again in April 2026; Mineral Resources (金属資源) kept its name and scope in
the restatements read; ¥bn, years ended March 2022 to March 2026, 決算短信 segment notes, TDnet 140120230508560340,
140120240426578542, 140120250409511808 and the FY2025 English results, TDnet 140120260430515680):

| Part | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | five-year | share |
|---|---|---|---|---|---|---|---|
| Mineral Resources | 420.7 | 439.3 | 295.5 | 227.8 | 204.5 | 1,587.8 | 33.9% |
| Natural Gas, then Environmental Energy | 105.1 | 170.6 | 238.8 | 198.6 | 160.9 | 874.0 | 18.6% |
| All segments | 917.9 | 1,132.2 | 975.8 | 908.8 | 752.1 | 4,686.8 | 100% |

No part carries more than half; **Mineral Resources is the largest and decides.** In the first quarter of FY2026 it was
again the largest (¥86.6bn of ¥293.8bn, Q1 決算短信, TDnet 140120260731505791, segment note).

**The deciding part's key variables, from the filer.** The company names them: steelmaking coal prices through MDP,
whose results "cannot be determined by the coal price alone" because of the Australian dollar, weather and labour; and
copper, where "a US$100 fluctuation in the price per MT of copper would have a ¥2.6 billion effect on our profit"
(FY2025 results, TDnet 140120260430515680, Business Risks (2)1)). Its investments are valued on "medium- to long-term
price forecasts", which "have a more significant impact on the valuation of our investment in AAS than short-term price
fluctuations" (same, (5)b). **How predictable they have been, in its own figures** (Mineral Resources, or Metals before
April 2019, profit to owners, ¥bn): FY2015 −360.7 (the Metals group of the time; the next year's results name the
"資源関連資産の減損損失" of that year, TDnet 140120170509462328); FY2016 147.9; FY2017 261.0; FY2018 263.6; FY2019 212.3;
FY2020 78.1; FY2021 420.7, which the filer ties to "豪州原料炭事業における市況上昇" (TDnet 140120220509536316); FY2022
439.3; FY2023 295.5; FY2024 227.8; FY2025 204.5. The part's profit rose 5.4-fold in one year and fell by half in three.
The AAS stake bought for US$4.51bn is carried at ¥216.5bn after a reversal that followed "upward revisions to medium-
to long-term price forecasts by external institutions" (FY2025 results, (5)b): the insiders do write a long-term
forecast down, and their own record is that it is rewritten with the market, in both directions. The company has itself sorted these earnings apart: its 2018 results split net income into a "Business-related
sector" and a "Market-related sector", the latter defined to include "Mineral resources in the Metals segment" and
North American shale gas and E&P (correction notice of 2018-05-17 to the results of 2018-05-08, the company's own
document, read through the www2.infomart.co.jp mirror).

**The tests.** (1) Where will the deciding part be in ten years? Its competitive position can be read in part (BMA's
scale, Quellaveco's cost; of two copper producers, "One is going to go broke at a buck-fifty a pound. And the other
one’s going to still be doing fine." **[M2009-059]**; also **[M2006-004]**), but its earning power cannot: it is set by the price of steelmaking coal
and copper over ten years, a variable the speakers say they cannot forecast and know no one who can: "if you are going
to try and figure out whether when to be long or short oil, or natural gas, or copper or cotton or whatever, I don’t
know of people who I feel would have an edge in trying to do that over the next 10 years" **[M2011-047]**; "We don’t
think we can predict commodity prices." **[M2016-025]**. (2) Key variables and their predictability: named, and not
predictable **[M1998-044]**. (4) "If something’s important but unknowable, forget it." **[M2006-076]**: the price is the
important variable of the part that decides, and the second part (gas and LNG, 18.6%, now enlarged by Aethon's
Haynesville gas) rests on the same kind of variable, "a investment that depends on the price of oil" **[M2020-035]** (the transcript's "a").
(8) How far off could I be? On the part's own record, by a factor of five in a year **[M2011-084]**. (9) Doubt: I have
it, and doubt means outside **[M2002-092]**. (11) Abroad, governance and tax: Japan's are readable from the filings and
the speakers' own Japanese holdings **[M2000-141]**; not the obstacle.

**Weighed against it** (written as found, **[M1997-127]**): the speakers read the five trading houses "as a group" **[M2023-031]**,
which is the reading the by-parts CONVENTION refuses and which the framework keeps OPEN against it; under the CONVENTION
the run follows the governing text. A purchase was made without knowing the price of oil, "Nobody does."
**[M2024-054]**, a row about one company, weighed and not a verdict. The answer on coal, "that doesn’t mean we’re going
to be phased out over time" **[M2021-041]**, is about Berkshire's own businesses. None makes the deciding part's ten-year earning
power foreseeable.

**Which cause.** NATURE. The deciding question is the ten-year price of steelmaking coal and copper; no filing not yet
read answers it, the company's own written forecasts move with the market, and the rows say the problem is not cured
by study: "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those
industries." **[L1993-023]**; "we’re not going to learn enough in the followings five months to make up for the fact
that we went in deficient in the first place." **[M2008-086]**. It is no judgment that the business is poor or the price
high: "It doesn’t mean it isn’t a good buy. [...] It just means that we don’t know how to evaluate it." **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**. The part that decides (Mineral Resources, 33.9% of five-year segment
  profit, the largest) earns what steelmaking coal and copper prices give it, and its profit moved from ¥78.1bn to
  ¥420.7bn in one year; its ten-year earning power cannot be foreseen. The file closes here; Q2 to Q12 are NOT REACHED.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed the file). No rival is named in the documents read (a search of the FY2023, FY2024 and FY2025
English results for "compet" finds only the company's own "highly cost competitive" and "excellent competitiveness");
no rival was read. Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN. WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The eleven balance sheets are read in Step 0; the owner-cash recast used for the computation below is in
`Test Runs/_research 2026-10-12 MTSUY/scripts/owner_cash.py`.

## Q5 — WHO RUNS IT. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED. The buyback line Q6 would take from Q7 is recorded under AFTER THE STOP.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED as a question. The two reporting figures the owner asks for are computed below.

**COMPUTATION, NOT A CLEARANCE** (the file closed at Q1; nothing here is a verdict or entry language; operator rule 3).
Built by Q7's range convention in full, each choice stated:
- **Owner cash** (yen bn, by year, from the statements of cash flows of the ten 決算短信 and the FY2025 English results):
  operating cash flow (which already counts working-capital changes, interest paid and received, tax paid, and dividends
  received from equity-method investees in place of their share of profit, the equity-method CONVENTION of Q4), less
  repayments of lease liabilities (IFRS 16 puts them in financing from FY2019; they are a real operating cost here), less
  dividends paid to non-controlling interests (the minority partners' cash), less spending on property, plant and
  equipment and investment property net of their disposals. All capital spending is deducted; the filings give no
  maintenance split, so the maintenance-only case (specific (e)) is not available. Not a net-income proxy (operator rule
  5). **All-equity basis:** interest paid added back after tax at 30.62% (CONVENTION of this run: Japan's standard
  effective statutory rate for a large company, used only to put interest after tax; rationale: the filings state the
  tax charge, not a marginal rate).

  | FY | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | owner cash before purchases, equity-only | 448 | 606 | 327 | 251 | 359 | 357 | 1,130 | 533 | 1,208 | 1,012 |
  | same, all-equity | 493 | 651 | 384 | 316 | 406 | 402 | 1,223 | 680 | 1,324 | 1,121 |
  | net purchases of businesses and investments | 96 | 207 | 121 | 230 | −50 | −214 | −305 | −137 | 3 | 166 |
  | profit to owners (for comparison only) | 440 | 560 | 591 | 535 | 173 | 938 | 1,181 | 964 | 951 | 800 |

- **Acquisitions (specific (c)).** Net purchases (equity-method investments, businesses, other investments, each net of
  sales) over the window FY2021 to FY2025 average **−¥97bn** a year: the company sold more than it bought. Deducting them
  would credit divestment proceeds as owner cash. **CONVENTION of this run:** where net purchases are negative, the
  central figure uses owner cash before purchases and shows the after-divestment figure beside; rationale: the proceeds
  of selling parts are not cash the remaining business produces, and specific (c) is written for the buyer. Lawson's
  deconsolidation (FY2024) moved Lawson's cash out of the group through two lines (−¥343.2bn in business disposals and
  +¥408.8bn released from held-for-sale) that net to +¥65.5bn; the netted figure is used.
- **The window and the cycle (specific (a)).** Five-year average, FY2021 to FY2025: **¥950.0bn** all-equity (¥847.9bn
  equity-only). Neither end year is a peak or trough of the owner-cash series (FY2021, ¥402bn, is low, its working
  capital absorbing a record profit; FY2025, ¥1,121bn, sits below FY2024), so the literal window stands. Beside it, the
  ten-year average: ¥700.1bn all-equity.
- **Growth (specifics (b), (f)).** Owner cash grew 29.3% a year from FY2021 to FY2025 (¥402bn to ¥1,121bn). Carried ten
  years that is about ¥12.4tn a year, against a highest owner-cash share of revenue in the filings of 7.1% (FY2024) on
  revenue of about ¥19tn: an absurdity **[M1999-067]**, so the growth carried is the business's own revenue growth over
  the window, ¥17,264.8bn to ¥18,916.0bn, **2.31% a year**, below the discount rate. Zero nominal growth after year ten.
- **Rate:** JGB 30-year, 4.136% (2026-10-08, Ministry of Finance).
- **Net debt (all-equity basis):** ¥3,939.8bn at 2026-06-30, the company's own "ネット有利子負債（リース負債除く）" (Q1
  決算短信, TDnet 140120260731505791, financial position table): bonds and borrowings less cash and time deposits, leases
  left out (their repayments are already deducted from owner cash). **Plus Aethon**, completed 2026-07-14, after the
  window and after the last filed balance sheet: US$5,200M at ¥158.06 (2026-10-08, aggregator, flagged) = ¥821.9bn
  added, total **¥4,761.7bn**. Aethon's own filed record (the notice of 2026-01-16) gives net income for 2022 to 2024
  averaging about US$219M a year across its two filing entities, with a loss year in each; it files no owner cash and a
  net-income proxy is barred (operator rule 5), so the deal is credited at nothing in the central figure; credited at its
  price instead, the fair price would rise by about ¥224 a share.
- **Shares:** 3,662,694,127 (2026-06-30).

**(a) VALUE RANGE (reporting figure), central, all-equity basis, owner cash before purchases:** whole business ¥22,969bn
(no growth) to ¥27,874bn (2.31% for ten years), less net debt ¥4,761.7bn: **¥4,971 to ¥6,310 a share** (ADS at one
share each: $31.45 to $39.92 at ¥158.06), width 1.27 to one, against **¥4,596 ($29.20)**. Beside it: after net
divestments ¥5,613 to ¥7,090; equity-only ¥5,597 to ¥6,792; on the ten-year base ¥3,321 to ¥4,308. The literal window
is the central figure.

**(b) FAIR PRICE (reporting figure; Part VII: each end case valued at ten percent, the two averaged; owner cash after the
company's own tax, no conversion):** **¥1,515 a share on the all-equity basis ($9.58)**; equity-only **¥2,512 ($15.89)**.
Beside: after net divestments ¥1,803 all-equity; on the ten-year base ¥774.

**What the computation says against the floor.** At ¥4,596 the market values the whole business at ¥21,595bn (equity
¥16,834bn plus net debt ¥4,761.7bn); the central owner cash earns **4.40%** on it with no growth and **5.29%** with the
capped growth (5.82% on the after-divestment figure). No case reaches the floor of about ten percent **[M2003-149]**; had
Q1 passed, Q7 would close OUT by the floor-first CONVENTION (2026-10-10), whatever the width. The range sits above the
price only because it is discounted at 4.136%; that is the arithmetic of the rate, not a margin of safety
**[M2009-005]**.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH. WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE), decided at Q1**: the deciding part (Mineral Resources, the largest, 33.9% of five-year segment
profit) earns what steelmaking coal and copper prices give it, and its ten-year earning power cannot be foreseen.
COMPUTATION only: value range ¥4,971 to ¥6,310 (at the 4.136% JGB) against ¥4,596; fair price ¥1,515 all-equity, ¥2,512
equity-only; no case earns the ten-percent floor at the price. Integrity facts recorded, not judged.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box unchanged.)*
- **Q2.** The documents read name no rival. Berkshire's 2023 letter names the five houses, "Itochu, Marubeni, Mitsubishi,
  Mitsui and Sumitomo" **[L2023-008]**; none was read, and whether each files with the SEC was not checked. Return on
  equity to owners, from the 決算短信 summaries, was 10.3% (FY2024) and 8.5% (FY2025); profit to owners averaged ¥713bn a
  year over ten years on owners' equity that rose from ¥4.6tn to ¥9.4tn. The company sold two BMA mines in 2024 and
  wrote down Japanese offshore wind in FY2024 ("国内洋上風力発電事業における減損損失等", TDnet 140120250409511808).
- **Q3.** Ten-year owner cash before purchases averages ¥623bn (equity-only) against profit to owners of ¥713bn;
  spending on property, plant and equipment ran ¥160bn (FY2016) to ¥521bn (FY2023); depreciation and amortization ¥201bn
  to ¥599bn (IFRS 16 added lease depreciation from FY2019).
- **Q4.** The company features a figure of its own, "Underlying operating cash flows" (operating cash flow before working
  capital, after lease repayments), used "to assess the Company's sustainable earning power" (FY2025 results, p. 5), and
  forecasts it (¥1,250bn for FY2026) beside profit (¥1,100bn). Chiyoda's Golden Pass LNG project: a provision the company
  booked itself in FY2023 under "Other" because Chiyoda's own accounts were not yet approved, reversed and re-booked in
  the segment in FY2024, then improved by a contract amendment of 2025-11-13 (segment notes, TDnet 140120250409511808 and
  140120260430515680). Two clerical corrections: the 2018 forecast page, and the 2026-03-25 cancellation count (the issued
  total printed for the cancelled number, corrected the same day).
- **Q5 (integrity facts recorded, not judged).** The company publishes an annual profit forecast every year (決算短信,
  section 3; FY2026: ¥1,100bn, +37.4%), the guidance habit the framework carries to Q5 **[L2019-006]**. Its forecast of
  ¥600.0bn for FY2018 met ¥590.7bn. The president and CEO is 中西 勝也 (Katsuya Nakanishi) on every 2025 to 2026 notice;
  two notices of a change of representative director (2026-03-19, 2026-04-17) were not read beyond their titles.
  Executive officers receive stock options (five plans granted 2026-05-19; notices not read).
- **Q6.** The ¥1tn buyback of 2025-04-04 to 2026-03-24 bought 318,397,611 shares for ¥999,999,552,401, an average of
  **¥3,141 a share**, below the bottom of the computed range (¥4,971) and above the computed fair price (¥1,515
  all-equity, ¥2,512 equity-only); the board's resolution named a total and a share cap, not a price (notice TDnet
  140120260324588068, reference section). Dividends rose from ¥70 (FY2023, split-adjusted) to ¥110 (FY2025), forecast
  ¥125. A tender offer was made for the listed subsidiary Mitsubishi Shokuhin (2025). Aethon was bought for cash from a
  pension fund for US$5.2bn; one of its two filing entities reported a loss in its last year.
- **Q9.** Gross interest-bearing liabilities ¥5,746.9bn at 2026-03-31, "almost all" at floating rates (FY2025 results,
  Business Risks (2)4)); net ¥3,939.8bn at 2026-06-30 before Aethon; lease liabilities ¥760.9bn at 2026-03-31;
  marketable securities ¥1,440.6bn at market with ¥348.6bn of unrealised gains.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (Step 0; Q1 and the
      sections before it; the computation and the close).
- [x] Dispatched: the brief allowed per-question pathspec commits; the lock in `Screens/_daily/` was present at the
      start (the dispatching session's, not mine); the fold is the dispatcher's.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched. Seen by accident and declared at
      the top: commit subjects of an earlier run filed under this ticker (of Mitsui & Co.), and a memory index line. Not
      used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      `scripts/check_ids.py` in the research folder); every filing fact carries its TDnet or RNS number; no number without
      a filing or a CONVENTION label.
- [x] The order was kept; Q1 closed the file; everything after it is NOT REACHED or headed COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost, from the cash-flow statements, never net income (operator rule 5); the sovereign
      from Japan's Ministry of Finance; aggregator quotes (price, ADS, USD/JPY) flagged.
- [x] Contrary evidence written down as found (Foundations; Q1, Weighed against it); facts for later questions under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] No point-in-time anchor; rows of every year are admissible.
- [x] `tools/run.py` and `Screens/cover_shares.py` returned nothing for a non-SEC name; every figure is by hand.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Not done: the integrated report and the annual securities report (yuho) were not read (company site refused, EDINET's
  API needs a key); the Japanese 決算短信 stand in for them, with the English results of the last three years. The
  notice of the 2026 general meeting was located (TDnet 140120260519541439) and not read, since Q5 was not reached.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) The by-parts CONVENTION measures a part by "five-year operating profit", but a Japanese trading house reports
segment profit attributable to owners, after tax and equity-method income, and regroups its segments (April 2024 and
April 2026); I used the reported measure and the restated series and said so. With no part above half, the largest part
decides at 33.9%, so a third of the earnings closes the whole; the text intends this, but it means the five-house row, which reads the whole "as a group" **[M2023-031]**, can never govern a trading house; the framework flags it OPEN and
does not resolve it. (2) Q1's routing names fast change as the TOO HARD case; it does not say whether a business whose
earning power is set by a commodity price nobody forecasts belongs at Q1 (an unknowable key variable) or at Q7 (the
cycle specific). I closed at Q1 because the price decides the part's ten-year earning power, not only its cycle, and the
part's own written forecasts move with the market; a reader could send it to Q2 or Q7 instead. (3) Specific (c) says
nothing of a business that is a net seller over the window: deducting net purchases then credits divestment proceeds as
owner cash. I confessed a CONVENTION (central figure before purchases) and showed the other beside. (4) Specific (c)
values a deal closed after the window "on its own filed record", which for an unlisted target is a notice with net income
and no cash flow; operator rule 5 then credits it at nothing, which is harsh for a producing asset; I showed the at-cost
figure beside. (5) The all-equity basis adds back interest after tax at a rate the filings do not state; I confessed
30.62%.
