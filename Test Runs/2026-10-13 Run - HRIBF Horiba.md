# Company Run: HORIBA, Ltd. (Tokyo: 6856; US OTC: HRIBF ordinary, HRBAY unsponsored ADS), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its source document and date (Horiba files
nothing with the SEC beyond two depositaries' F-6EF registrations, so a document and date stand in place of an accession
number, as the brief directs); a STOP that returns OUT or TOO HARD closes the run and later questions are marked NOT REACHED.
Copied from the template before any fetch (write-early). Dispatched blind run under `Test Runs/_research 2026-10-13 HRIBF/_brief.md`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (HRIBF, HRBAY, Horiba, 6856); not held.*

**Contamination declared (the blind rule).** Seen without searching, and not used: the session's opening git status listed
untracked research files of other runs (folders named for AYI and ARCB, daily digest files) and the last five commit
subjects, which concern another company (GRFXY); the auto-memory index loaded into the session carries general queue lines
(counts of names, wave numbers) that name no business in this file. Nothing about Horiba under any name or ticker was seen.
No file in the blind list was opened, listed or searched.

**The business, from its own latest annual report** (Annual Securities Report, yukashoken hokokusho, for the 88th fiscal
year ended 2025-12-31, filed 2026-03-23, EDINET code E01901, read from the company's IR site; section 3, Business
description): a Kyoto maker of measuring and analysis instruments, in its own words "測定機器の製造、販売及びサービスを主たる
業務" (the manufacture, sale and service of measuring instruments), with 46 consolidated subsidiaries. Its three reporting
segments from FY2025 are Energy & Environment (engine exhaust measurement, drive-line, engine, brake and battery test
systems, vehicle development and test engineering at HORIBA MIRA in the UK, stack-gas, water and air monitors, process
instruments), Bio & Healthcare (blood cell counters, immunoassay and clinical chemistry analyzers, spectroscopy for life
science) and Materials & Semiconductor (mass flow controllers for semiconductor manufacturing equipment, chemical
concentration monitors, reticle and mask particle detectors, residual gas analyzers, scientific analyzers).
**Rename, merger, spin-off or split:** no rename, spin-off or share split in the ten years read (the price series shows
no split; shares issued were 42,532 thousand from FY2021 to FY2023 and 42,233,252 after 299,500 treasury shares were
cancelled on 2024-06-05, yuho FY2025, section 4 (4)). The one merger in the company's
history is the 1970 absorption of the operating HORIBA by a dormant shell, done to change the par value (yuho, section 2).
**Segment change:** from 2025-01-01 the five segments Automotive, Process & Environmental, Medical-Diagnostics,
Semiconductor and Scientific were replaced by the three above (yuho FY2025, section 3; FY2025 results release,
2026-02-12, note to the segment table). Acquisitions in the window: Process Instruments, Inc. (US, 2023-10),
EtaMax Co., Ltd. (Korea, 2025-04); after the window Pristine Deeptech (India) entered consolidation in H1 2026.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** ¥26,330, the Tokyo Stock Exchange close of 2026-10-09 (the last full session: 2026-10-12 was a Japanese public
  holiday, and the 2026-10-13 session was still open when fetched, last trade ¥25,665 at 13:33 JST). Source: Yahoo
  Finance chart feed for 6856.T, an aggregator, flagged per operator rule 5 (saved as
  `Test Runs/_research 2026-10-13 HRIBF/price_6856T_yahoo_10y.csv`). The OTC quote for HRIBF, $137.00, has not moved since
  at least 2026-10-05 and is a stale aggregator print, flagged and not used. The ADS ratio is not used, so the depositary's
  document is not needed. The price has risen from ¥7,973 (the 2025 low) and ¥16,325 (the 2026 low) to a 2026 high of
  ¥28,880 (same series).
- **Shares:** 42,233,252 ordinary shares issued less 211,697 treasury shares = **42,021,555 outstanding at 2026-06-30**
  (Summary of Consolidated Financial Statements for the six months ended 2026-06-30, dated 2026-08-07, notes (4); the
  semi-annual securities report filed 2026-08-10 states the same issued count and 211,600 treasury shares in its voting
  table, which counts whole units of 100). One class only. `python Screens/cover_shares.py HRIBF` returned "no periodic
  filing found (CIK 2088827)"; the count is taken by hand from the company's own filings, as the brief directs.
- **Market cap:** 42,021,555 × ¥26,330 = **¥1,106.4bn**. The company itself says its market capitalization has exceeded
  ¥1 trillion (H1 2026 release, dividend note; see Q5).
- **Sovereign for the earnings currency:** JPY 30-year **4.134%**, 2026-10-08, Japan Ministry of Finance, jgbcme.csv
  (`python tools/sources.py` prints 4.14%; the row is saved as `Test Runs/_research 2026-10-13 HRIBF/jgbcme_mof_2026-10.csv`).
- **Filings read** (operator rule 4; documents and dates in place of accession numbers), all from horiba.com IR library:
  - Annual Securities Report (yuho) FY2025, filed 2026-03-23; and the yuho for FY2016 (filed 2017-03), FY2017 (2018-03-26),
    FY2018 (2019-03-25), FY2019 (2020-03-30), FY2021 (2022-03-28), FY2022 (2023-03-27), FY2023 (2024-03-25) and FY2024
    (2025-03-31): the consolidated balance sheets, cash-flow statements and segment notes of FY2015 to FY2025.
  - Semi-annual securities report, H1 2026, filed 2026-08-10; H1 2026 results release (English), 2026-08-07.
  - FY2025 results release (English), 2026-02-12, and its corrected re-issue of 2026-02-17; FY2024, FY2023, FY2022,
    FY2020, FY2019 and FY2018 year-end releases.
  - Notice of the 88th ordinary general meeting (English), 2026-02-25, and the notice of resolutions, 2026-03-23.
  - FY2025 results presentation, 2026-02-25; H1 2026 presentation, 2026-08-21; HORIBA Report 2024-2025 (integrated
    report, English), published 2025-07-30. No HORIBA Report 2025-2026 is posted yet.
  - **One figure cross-checked against the filed statement:** FY2025 net cash from operating activities ¥54,383m appears
    identically in the yuho's consolidated cash-flow statement and five-year summary and in the English release of
    2026-02-12; FY2025 net sales ¥333,081m likewise. The English release's balance-sheet liability columns are misprinted
    by the text extraction, so every balance-sheet figure below is taken from the Japanese yuho.
- **`python tools/run.py HRIBF`:** failed with HTTP 404 on the SEC company-facts URL (no XBRL exists for a non-registrant).
  Every figure below is taken from the filed statements by hand (`Test Runs/_research 2026-10-13 HRIBF/scripts/owner_cash.py`).
- **Owner cash after every real cost, by hand (¥m):** net cash from operating activities, less purchases of property,
  plant and equipment and of intangibles, less finance-lease principal, less restricted stock and performance-share pay
  (shown in the statement of changes in net assets, ¥169m in 2024, ¥271m in 2025; none recorded earlier). Operating cash
  is after interest and tax paid. Acquisitions shown separately (cash paid for subsidiaries net of cash acquired).

  | FY (Dec) | sales | op. income | OCF | capex | lease | **owner cash** | acquisitions | D&A | capex/D&A |
  |---|---|---|---|---|---|---|---|---|---|
  | 2016 | 170,093 | 18,499 | 15,871 | 13,374 | 195 | **2,302** | 0 | 6,676 | 2.00 |
  | 2017 | 195,399 | 26,834 | 28,287 | 12,018 | 163 | **16,106** | 0 | 7,387 | 1.63 |
  | 2018 | 210,570 | 28,838 | 19,536 | 10,278 | 181 | **9,077** | 0 | 7,120 | 1.44 |
  | 2019 | 200,241 | 20,916 | 26,638 | 12,934 | 831 | **12,873** | 0 | 8,485 | 1.52 |
  | 2020 | 187,080 | 19,694 | 32,253 | 15,045 | 1,254 | **15,954** | 0 | 9,296 | 1.62 |
  | 2021 | 224,314 | 32,046 | 35,268 | 12,572 | 1,252 | **21,444** | 0 | 10,063 | 1.25 |
  | 2022 | 270,133 | 45,843 | 33,966 | 12,083 | 1,482 | **20,401** | 0 | 10,911 | 1.11 |
  | 2023 | 290,558 | 47,296 | 16,652 | 9,171 | 1,762 | **5,719** | 2,421 | 12,097 | 0.76 |
  | 2024 | 317,369 | 48,340 | 40,335 | 19,447 | 1,875 | **18,844** | 0 | 12,653 | 1.54 |
  | 2025 | 333,081 | 53,040 | 54,383 | 26,142 | 1,859 | **26,111** | 2,497 | 13,180 | 1.98 |

  Five-year average FY2021 to FY2025: **¥18,504m** before acquisitions, ¥17,520m after; FY2016 to FY2020: ¥11,262m.
  Owner cash has run at 1% to 10% of sales, against operating margins of 10% to 17%: capital spending has exceeded
  depreciation in nine of the ten years, and working capital absorbs cash in growth years (2023: operating cash fell to
  ¥16.7bn while operating income was ¥47.3bn, on income tax paid of ¥18.2bn and inventory build). FY2026 company forecast
  (H1 release, 2026-08-07): sales ¥382bn, operating income ¥70bn, net income ¥50bn; H1 2026 sales +20.8%.
- **Net debt at the latest filed date (2026-06-30, semi-annual report):** cash and deposits ¥169,311m plus marketable
  securities ¥1,628m = ¥170,939m; borrowings: short-term ¥8,901m, bonds ¥30,000m (¥15,000m current), long-term loans
  ¥23,984m, finance leases ¥5,490m (the FY2025 yuho schedule of borrowings, 2025-12-31; the semi-annual report does not
  restate them) = ¥68,375m. **Net cash ¥102.6bn**; less the interim dividend of ¥150 a share declared in the report and
  paid 2026-08-31 (¥6.3bn), **¥96.3bn**, about ¥2,290 a share. Investment securities (¥23.7bn, largely listed
  cross-holdings) are left out of net debt and stated beside it.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether I "would I be happy buying this stock if the market closed for five years"
**[M1997-109]**, and the market's recent move (the price roughly tripled from the 2025 low of ¥7,973 to ¥26,330) carries
no instruction about value, "It just tells us prices" **[M2006-077]**. The margin of safety is an attitude here and an
arithmetic only at Q7 **[M1996-084]**. No macro view enters, including any view on the AI-driven semiconductor
equipment cycle that has carried the share price. Who is paid to tell me: the company's own medium-term plan (MLMAP2028)
and its forecasts are projections, read as the company's and never as evidence. **Contrary evidence, written down as found**
**[M1997-127]**: (1) owner cash is a small fraction of reported earnings in most years (¥18.5bn average against net income
of ¥33.2bn average over FY2021 to FY2025), because capital spending runs at up to twice depreciation; (2) the company's
own risk section rates semiconductor technology change and abrupt demand swings as likely and of large impact (yuho FY2025,
section 3 of Business Risks, item ③); (3) the automotive test business, once the largest earner, earned nothing or lost
money in FY2021 and FY2022 and its own risk section names electrification as a structural change (item ①); (4) Bio &
Healthcare lost money in FY2024 and FY2025; (5) the board declared a "commemorative dividend" of ¥240 a share "to mark the
milestone of the Company's market capitalization exceeding 1 trillion yen" (H1 2026 release, 2026-08-07), a management
celebrating its share price, which the speakers read as a tell: "when we see the price of a stock posted in the lobby of
the headquarters or something, you know, things like that make us nervous." **[M2004-067]**.

## THE STANDING RULE
The buyer's conduct, not the target's: a purchase of a listed part-interest for cash, with no borrowing, no collateral and
no option given away, puts nothing at risk of the kind the rule forbids, since "borrowed money has no place in the
investor's tool kit" **[L2014-005]** and the rule is "Never risk permanent loss of capital" **[L2023-005]**. Abroad, the
rows ask whether the governance and the tax are understood and, if they are, a lower price rather than a pass
**[M2000-141]**, **[M2006-021]**. Nothing here closes the file; sizing is for Q10 if reached.

---

## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test as the framework states it.** Understanding is "a reasonable fix on about what the earning power and competitive
position will look like in five or 10 years" and "some notion of how the industry will develop and where the company will
stand within the industry" **[M2012-065]**; "a reasonable probability of being able to asses where the business will be in
10 years" **[M2000-037]**. Knowing the product is not the test, "It’s the predictability of the economics of the situation
10 years out" **[M2000-104]**; the chemistry can stay opaque if "the economic dynamics of the industry" are understood
**[M2011-014]**.

**Which part decides (the business of parts: Q1's holding-company paragraph, extended to segments by Q2 section B).**
Horiba reports parts with plainly different economics. Segment operating profit from the yuho segment notes (¥m):

| FY | Automotive | Process & Env. | Medical | **Semiconductor** | Scientific | total |
|---|---|---|---|---|---|---|
| 2020 | 2,465 | 1,639 | (426) | **14,052** | 1,963 | 19,694 |
| 2021 | (13) | 1,947 | 148 | **28,006** | 1,957 | 32,046 |
| 2022 | (667) | 2,101 | (99) | **42,005** | 2,503 | 45,843 |
| 2023 | 1,209 | 2,412 | 638 | **40,580** | 2,456 | 47,296 |
| 2024 | 1,493 | 1,835 | (150) | **44,178** | 982 | 48,340 |

Under the new segments (FY2025 yuho): FY2024 Energy & Environment 4,262, Bio & Healthcare (890), **Materials &
Semiconductor 44,968**; FY2025 9,417, (894), **44,517**, total 53,040. The semiconductor business (mass flow controllers
above all: 79% of that segment's sales in the Annual Report 2011, Semiconductor segment page) earned 87% of operating profit over FY2020 to
FY2024 and 84% in FY2025 inside the wider Materials & Semiconductor segment. **It decides**: it carries more than half of
five-year operating profit. The whole is understood only if this part is.

**The key variables and how predictable they are** **[M1998-044]**:
1. *How many semiconductor manufacturing tools the customers build.* The deciding part's sales went ¥35.4bn (2015),
   38.8, 53.3, 57.8, 47.2 (2019, down 18%), 57.0, 87.0, 114.1, 112.9, 120.5 (2024); its profit went from ¥9.4bn to
   ¥44.2bn. The level of the cycle is not by itself a reason to stop here: the framework places such a level at Q7 as the
   cycle base, not at Q1 (Q2, A commodity business: "We don’t think we can predict commodity prices." **[M2016-025]**). This variable alone
   would not close the file.
2. *Whether the mass flow controller and process-monitoring position holds through the process technology of the next
   ten years.* This is the deciding variable, and the company describes it as a moving one. Its own risk section:
   "半導体及び半導体製造に関わる技術変化や半導体の急激な需要変動による半導体製造装置及び半導体メーカー等の設備投資動向は、当社グループの
   財政状態及び経営成績に影響を及ぼす可能性があります" (technological change in semiconductors and their manufacture, and abrupt
   swings in demand, may affect results), a risk the company rates as likely and of large impact (yuho FY2025, Business
   Risks (1) ③, filed 2026-03-23). Its strategy for the part is to "Expand a product lineup that addresses device
   miniaturization, 3D structures, and increasingly complex manufacturing processes" and to add new lines (wafer
   inspection, advanced materials, a synthetic-diamond acquisition in India, EtaMax for compound semiconductors) (FY2025
   results presentation, 2026-02-25); its H1 2026 presentation adds "Heightened geopolitical risks affect supply chains".
   The castle is kept by continued invention for each new generation of tools.

**Contrary evidence, written down as found** **[M1997-127]**: the position has so far held and widened through technology
change. Horiba's own estimate of its global mass-flow-controller share was 47% in 2011 (Annual Report 2011, Semiconductor segment page) and 60%
for fiscal 2024 (HORIBA Report 2024-2025, market-share page); the semiconductor segment's margin was 22.7% to 29.5% in
FY2015 to FY2020 (22.7% in the down year 2019) and 32.2% to 36.8% in FY2021 to FY2024. The function, metering a gas into a
process chamber, has been the same product category for decades. Against that: the 2011 report itself forecast
"competitive pressure on sales prices" for mass flow controllers; the record is that of a supplier riding the
fastest-changing capital-goods industry; and the share figures are the company's own estimates, which no rival's filing
tests (the annual report names no competitor; see AFTER THE STOP, Q2).

**The tests, applied.**
- *Test 1, where will it be in ten years* **[M2000-037]**: I cannot print the next ten years of this part's figures; a
  decade that took its profit from ¥9.4bn to ¥44.2bn does not tell me whether 2035 is ¥20bn or ¥100bn.
- *Test 5, would the insiders write it down* **[M2000-105]**: the company writes its plan only to 2028 (MLMAP2028) and
  calls technology change in its customers' industry a likely, large risk; I found no participant in semiconductor
  equipment that publishes where its component suppliers' economics will stand in ten years.
- *Test 6, can I name the winner, not just the industry* **[M2012-067]**, **[L2009-005]**: I can see the industry
  growing; I cannot judge "what its profit margins and returns on capital will be" **[L2009-005]** for a component maker
  whose customers are a handful of equipment makers and whose newest competitors are being built inside China.
- *Test 7, customers or technology* **[M2017-019]**: the forecast is about technology, the process recipes of tools not
  yet designed, not about consumer behaviour.
- *Test 8, how far off could I be* **[M2011-084]**, **[M2012-073]**: way off, on the evidence of the last ten years.
- *Test 9, do I doubt it is inside* **[M2002-092]**: yes; "if you have doubts about something being into your circle of
  competence, it isn’t."

**Routing.** The framework fixes it (Q1, The routing, fixed): the business whose ten-year economics cannot be foreseen
because its industry changes fast closes at Q1 in TOO HARD, on "if something comes in where there’s a technological
component that’s of significance [...] it won’t make it through the filter" **[M1998-008]** and "a business that must deal
with fast-moving technology is not going to lend itself to reliable evaluations of its long-term economics"
**[L1993-023]**. The parts that do not decide neither rescue it nor need judging here: the automotive test business is in a
structural change the company itself names (electrification and AI in the automotive industry, yuho risk (1) ①) and lost
money in FY2021 and FY2022; Bio & Healthcare lost money in FY2024 and FY2025.

**Cause: NATURE, not WORK.** The deciding question is important and not knowable **[M2006-076]**: no filing I have not read
states where a semiconductor-equipment component maker's competitive position and margins will be in 2035, and the rows say
study does not cure it, "Our problem -- which we can't solve by studying up -- is that we have no insights into which
participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**; "We couldn't solve this
problem, moreover, even if we were to spend years intensely studying those industries." **[L1993-023]**. The box is no
judgment of quality: "It doesn’t mean it isn’t a good buy. [...] It just means that we don’t know how to evaluate it."
**[M2000-038]**.

- **VERDICT: TOO HARD (NATURE)** **[M2006-013]**. The deciding part, mass flow controllers and process monitors for
  semiconductor manufacturing equipment (84% to 88% of operating profit), lives on keeping pace with process technology
  that its own filing calls a likely, large risk; its ten-year economics cannot be foreseen. Q2 to Q12 are NOT REACHED;
  what follows is facts found and COMPUTATION, NOT A CLEARANCE.

---
## Q2 to Q12: NOT REACHED (the file closed at Q1).


## THE BOX
**TOO HARD (NATURE) at Q1**, the question that decided it: the deciding part (mass flow controllers and process monitors
for semiconductor manufacturing equipment, 84% to 88% of operating profit) cannot be foreseen ten years out because its
industry's process technology changes generation by generation, a risk the company's own yuho rates likely and large.
Integrity facts recorded, not judged (Q5 below: a dividend declared to celebrate the market capitalization). The
COMPUTATION below, not a clearance, puts the central range at ¥15,010 to ¥35,052 a share against ¥26,330, and no case of it
earns the floor at that price. Closed box: no research pass is opened, and a lower price does not reopen it **[M2000-038]**.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Written down as found **[M1997-127]**; no verdict; the box is unchanged (operator rule 2).*

### Bears on Q2 (the castle)
- **Competitors named:** none. Neither the FY2025 yuho nor the HORIBA Report 2024-2025 nor the FY2025 and H1 2026
  presentations names a rival (text search for the usual names and for 競合 found one generic mention, "競合他社の動向",
  in the Bio & Healthcare risk paragraph). No SEC-filing rival was read, so no competitor row exists; this is recorded as a
  gap, not filled from memory. The rivals a later run would have to read are its own choice under the brief's rule.
- **Share, by the company's own estimate:** mass flow controllers 47% of the world market (Annual Report 2011, Semiconductor segment page) and
  60% (HORIBA Report 2024-2025, estimates as of fiscal 2024); engine emission measurement systems 80% global; Raman
  spectrometers 30% global; pH meters 50% in Japan (same page).
- **Margins of the old segments over FY2015 to FY2024** (segment profit / external sales, yuho segment notes): Semiconductor
  26.7%, 24.9%, 29.3%, 29.5%, 22.7%, 24.7%, 32.2%, 36.8%, 36.0%, 36.7%; Automotive 7.9%, 5.7%, 10.5%, 9.7%, 8.0%, 3.9%,
  0.0%, (1.0%), 1.5%, 1.6%; Medical 9.2%, 10.6%, 7.6%, 7.0%, 5.1%, (2.0%), 0.6%, (0.3%), 2.0%, (0.4%); Process &
  Environmental 10.5%, 9.2%, 6.3%, 10.5%, 8.7%, 8.9%, 9.6%, 9.3%, 9.7%, 6.5%; Scientific 4.5%, 3.7%, 1.9%, 0.8%, 2.7%,
  7.3%, 6.5%, 6.9%, 6.2%, 2.4%. FY2025 (new segments): Materials & Semiconductor 28.4%, Energy & Environment 7.0%, Bio &
  Healthcare (2.1%).
- **Pricing:** the 2011 report forecast "competitive pressure on sales prices" for mass flow controllers. The FY2025
  presentation says of the medical business "Competition in the IVD market is intensified in Europe, U.S. and China" and
  that it "Initiated structural reforms in regions where profitability has declined due to intensifying competition"; it
  signed an MoU toward an alliance with Medconn, a Chinese diagnostics company.
- **Change in the automotive part:** the yuho names electrification and AI as structural change for the automotive test
  business (risk (1) ①); the FY2025 presentation reports that development of hybrids and engines on next-generation fuels
  "is reaccelerating due to the moderated EV shifts in several countries", and that investment in automotive fuel cells is
  slowing. The CFO page of the HORIBA Report 2024-2025 says "Although our hydrogen energy business earned less" (the sentence is
  cut by the page layout).
- **Customers:** semiconductor equipment makers and device makers (2011 report, segment page); no customer is named and no
  share of sales by customer is disclosed in the yuho. Two subsidiaries exceed 10% of consolidated sales each: HORIBA
  Instruments Inc. (US) and HORIBA (China) Trading (yuho FY2025, section 4, note 23). Asia was 41.7% of FY2025 sales,
  Materials & Semiconductor Asia ¥100.4bn of ¥156.5bn (FY2025 release, sales by destination).
- **Capacity:** the new Fukuchiyama factory raises domestic mass-flow-controller capacity "up to three times", with output
  "expanded step-by-step in line with semiconductor market conditions" (FY2025 presentation); the Aso factory, which makes
  new mass-flow-controller products, stopped after the 2026 Kumamoto earthquake and resumed on 2026-07-31 (H1 2026
  presentation).

### Bears on Q3 (capital)
- Capital spending exceeded depreciation in nine of ten years (ratio 0.76 to 2.00; FY2025 ¥26.1bn against ¥13.2bn);
  company forecast FY2026 capital spending ¥20.0bn against depreciation ¥15.5bn (FY2025 release, section 4).
- Operating capital (receivables, inventories and net PP&E, less trade payables and advances or contract liabilities) was
  ¥125.8bn at FY2016 and ¥265.8bn at FY2025; operating income ¥18.5bn and ¥53.0bn: 14.7% and 20.0% pre-tax on that
  capital, and ¥34.5bn of added operating income on ¥140.0bn of added capital (24.6% pre-tax) over nine years. Owner cash
  in FY2025 was 9.8% of the FY2025 operating capital.
- Acquisitions over FY2021 to FY2025 were ¥4.9bn in cash (Process Instruments 2023 ¥2.4bn; EtaMax 2025 ¥2.5bn), 5% of
  owner cash before purchases: not a serial acquirer under Q7(c). Goodwill ¥2.0bn at FY2025. The earlier large purchase
  was MIRA (UK vehicle engineering and proving ground), ¥13.6bn in FY2015 (business transfer line, FY2016 yuho).

### Bears on Q4 (the accounts): the balance sheets, FY2015 to FY2025 **[M2025-032]**
Japanese GAAP, consolidated, ¥bn, from the yuho of each year (the prior-year column of the next yuho where the year's own
filing was not downloaded):

| FY | cash + securities | receivables | inventories | net PP&E | goodwill + intang. | total assets | borrowings + bonds | net assets | retained earnings | sales |
|---|---|---|---|---|---|---|---|---|---|---|
| 2015 | 50.8 | 50.1 | 40.2 | 57.0 | 10.3 | 232.1 | 44.7 | 127.2 | 93.2 | 171.9 |
| 2016 | 53.5 | 53.7 | 40.3 | 62.0 | 7.9 | 239.7 | 46.7 | 133.2 | 103.1 | 170.1 |
| 2017 | 60.9 | 60.2 | 45.6 | 68.7 | 4.4 | 265.9 | 42.1 | 150.9 | 115.3 | 195.4 |
| 2018 | 66.0 | 59.1 | 55.1 | 68.7 | 4.9 | 278.1 | 44.1 | 162.0 | 132.3 | 210.6 |
| 2019 | 98.7 | 59.1 | 51.6 | 75.9 | 5.5 | 315.1 | 55.4 | 171.6 | 141.7 | 200.2 |
| 2020 | 116.5 | 50.9 | 49.3 | 82.1 | 4.6 | 328.1 | 77.1 | 178.7 | 150.2 | 187.1 |
| 2021 | 137.0 | 59.9 | 53.1 | 88.3 | 4.4 | 371.6 | 80.2 | 204.5 | 166.9 | 224.3 |
| 2022 | 141.4 | 69.8 | 75.3 | 95.7 | 3.6 | 416.7 | 67.2 | 240.9 | 194.0 | 270.1 |
| 2023 | 134.8 | 71.5 | 99.5 | 100.8 | 5.0 | 449.0 | 60.4 | 283.7 | 223.3 | 290.6 |
| 2024 | 146.3 | 82.6 | 97.7 | 113.0 | 5.5 | 481.6 | 64.4 | 314.7 | 241.8 | 317.4 |
| 2025 | 164.6 | 82.2 | 94.7 | 132.1 | 6.4 | 518.3 | 66.5 | 348.6 | 267.5 | 333.1 |

What moved, and why, as the filings show it: equity grew from ¥127bn to ¥349bn almost wholly through retained earnings
(¥93bn to ¥267bn), with no large write-off; goodwill and intangibles are small and fell as the MIRA intangibles amortized,
so equity is nearly all tangible. Cash rose from ¥51bn to ¥165bn while borrowings stayed between ¥42bn and ¥80bn: the
company moved from about ¥6bn net cash to about ¥98bn. Receivables held at 25% to 29% of sales throughout. Inventories are
the one line that moved against sales: 23% to 26% of sales in FY2015 to FY2021, then 28% (FY2022) and 34% (FY2023) as the
company built stock through the semiconductor boom and supply shortages (inventory increases of ¥18.8bn in FY2022 and
¥20.1bn in FY2023 in the cash-flow statements), easing to 28% in FY2025 as ¥11.8bn was released over FY2024 and FY2025.
That build is why FY2023 owner cash was ¥5.7bn on operating income of ¥47.3bn. What the figures do not say: the margin and
order book of the semiconductor part at a turn of the cycle, which no balance sheet shows.
- Real costs: depreciation is charged and below capital spending; stock pay is small (restricted stock and performance
  share units, ¥271m in FY2025) and expensed; restructuring charges appear in FY2025 (¥1.3bn business restructuring,
  ¥0.6bn environmental) and impairments in FY2024 and FY2025 (¥1.3bn, ¥1.0bn), as extraordinary losses below ordinary
  income. EBITDA appears in none of the documents read (text search).
- Guidance: the company publishes full-year and half-year forecasts and revises them (FY2026 operating income forecast
  ¥56.0bn in February 2026, raised to ¥70.0bn in August 2026). No adjusted earnings figure is featured in place of the
  Japanese GAAP figures in the releases read.

### Bears on Q5 (the people): **integrity facts recorded, not judged**
- **The commemorative dividend.** The H1 2026 release (2026-08-07) raised the FY2026 year-end dividend forecast to ¥640 a
  share, of which "commemorative dividend of 240 yen to mark the milestone of the Company’s market capitalization
  exceeding 1 trillion yen". A dividend declared to mark the share price is a fact the speakers read under the tell of a
  management fixed on its stock price, "when we see the price of a stock posted in the lobby of the headquarters [...]
  things like that make us nervous" **[M2004-067]**. Recorded for any later run that reaches Q5, which must answer it
  **[M2013-088]**.
- **Who runs it.** Atsushi Horiba, Chairman & Group CEO and chair of the board, born 1948, joined 1972, director since June
  1982, President from 1992, Chairman of HORIBA STEC (the mass-flow-controller subsidiary) until 2026-03-27; he holds
  1,097,072 shares, 2.61%, the sixth-largest holding (notice of the 88th general meeting, 2026-02-25; yuho FY2025,
  principal shareholders and officers). The company was founded by 堀場雅夫 (Masao Horiba) (yuho section 2). Director Dan
  Horiba is a relative within the second degree of the Chairman (yuho FY2025, officers, note 4); he was President of
  HORIBA STEC until 2026-03-27, then its chairman, and head of group strategy from 2026-04-01. The board after the 2026
  meeting: nine directors, three non-executive and independent (notice of meeting).
- **Pay.** FY2025 directors' pay (excluding outside directors, seven persons) ¥1,153m: base ¥214m, performance-linked
  ¥820m, long-term stock ¥118m. Atsushi Horiba ¥458m in total, of which ¥319m performance-linked (yuho FY2025, officer pay
  tables). The performance-linked pool is (consolidated ROE ÷ 0.375%, rounded down) × ¥30m, capped at ¥1,200m, split by
  title points (Chairman 3.5 of 10); no charge for capital and no step-up beyond ROE (yuho FY2025, remuneration policy).
  Directors of HORIBA STEC are paid a bonus pool of 1% of the semiconductor segment's profit (the Materials &
  Semiconductor segment from FY2025), capped at ¥70m (yuho FY2022 and FY2024 remuneration notes).
- No litigation, investigation or restatement was found in the documents read (the yuho risk section lists none; the
  FY2025 release states no retrospective restatement).

### Bears on Q6 (the money and the owners)
- **Policy:** dividends targeted at 30% of consolidated net income, with special dividends and buybacks "機動的に"
  (flexibly) (yuho FY2025, dividend policy). Paid: FY2024 ¥270 a share (payout 33.8%); FY2025 ¥450 including a ¥160
  special (50.9%); FY2026 forecast ¥790 including special ¥190 and commemorative ¥240.
- **Buyback:** one programme in the decade: board resolution of 2024-02-14, up to 530,000 shares or ¥5.0bn, bought
  2024-02-15 to 2024-04-30 on the market: 334,500 shares for ¥4,998m, an average of **¥14,942 a share**; 299,500 treasury
  shares were cancelled on 2024-06-05 (yuho FY2024, section 2; yuho FY2025, section 4). The resolution states a sum and a
  share count, no price ceiling. **The line Q6 would have needed from Q7**: the bottom of the COMPUTATION's central range
  is ¥15,010; the average price paid, ¥14,942, sits at that bottom, on today's computation (Q6 not reached; not weighed).
- **Retention:** from end-FY2015 to end-FY2025 retained earnings rose ¥174bn while cash and securities rose ¥114bn; market value rose from about
  ¥230bn (¥5,410 at end-2016 on about 42.2m shares) to ¥1,106bn. Cross-shareholdings (investment securities) ¥23.7bn at
  2026-06-30.

### Bears on Q9 (could it ruin us)
- Net cash ¥102.6bn at 2026-06-30 (Step 0). Borrowings ¥68.4bn including ¥30.0bn of bonds (¥15.0bn due within a year)
  and long-term loans at 0.9% average (yuho FY2025, schedule of borrowings). Equity ratio 67.1%. One subsidiary (HORIBA
  FuelCon, Germany) had negative net assets of ¥3.1bn at 2025-12-31 (yuho section 4, note 9). The proving ground and
  engineering business in the UK carries "多額の固定資産" (large fixed assets) whose utilization depends on automakers'
  development spending (yuho risk (1) ①).

### Bears on Q7: COMPUTATION, NOT A CLEARANCE
*Reporting figures at the owner's request (Part VII, The owner's price); no entry language; Q7 was not reached.*
- **Base, window FY2021 to FY2025** (the literal window; no end year is described by the filer as aberrational: FY2025 is a
  "record" year but H1 2026 runs above it, and the trough year FY2023 sits inside the window), on the all-equity basis
  (net interest removed at the statutory 30.5%; the effective rate of 27.3% reflects recurring R&D credits, not a
  carryforward, so no shelter is priced):
  - maintenance-only owner cash (operating cash less depreciation as the maintenance guess, leases and stock pay),
    **¥22,096m**, the central base under specific (e); depreciation is the guess because the company's capital spending
    carries named growth projects (the Fukuchiyama factory), and the rows allow it: "the depreciation charge is not
    inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]** (the guess is
    mine);
  - all-spending owner cash after acquisitions **¥17,010m** (shown beside); growth spending = ¥5,086m a year.
- **Growth shown (aggregate):** maintenance-only owner cash 12.09% a year FY2021 to FY2025 (all-equity); all-spending
  1.17%. Sales grew 10.39% a year. The cap (f): the growth case reaches owner cash of 8.4% of year-ten sales at the
  sales growth shown, below the highest share of sales in the filings read (11.7%, FY2025), so no cut. After year ten,
  zero nominal growth, and the growth spending stops with the growth.
- **Value range at the JGB 30-year 4.134%, per share, all-equity basis (net cash ¥96.3bn added): ¥15,010 (no growth) to
  ¥35,052 (shown growth, growth spending charged for ten years)**; width 2.34 to one per share (2.58 to one on the
  business before net cash), under three. Price ¥26,330
  sits inside the range.
- **The floor, tested first:** at ten percent the same two cases give ¥7,549 and ¥13,133 a share; **no case earns the floor
  at ¥26,330**. The central growth case would need owner cash to grow 23.1% a year for ten years to earn ten percent at the
  price. Had Q7 been reached, it would have closed OUT on the floor **[M2003-149]**, whatever the width.
- **Fair price (Part VII; each end valued at ten percent, the two averaged), after the company's own tax: ¥10,341 a share
  on the all-equity basis (central); ¥8,640 on the equity-only basis** (owner cash after interest, ¥22,606m maintenance /
  ¥17,520m all-spending, 13.01% growth, no net cash added), beside it.
- **Beside, not central:** the all-spending literal case alone gives ¥12,082 to ¥13,088 at the JGB rate (fair price
  ¥6,506); the ten-year average owner cash FY2016 to FY2025 was ¥14,883m (equity basis, before acquisitions), against
  ¥18,504m for the window. At the price, the enterprise value (¥1,010bn) yields 2.19% on central owner cash and 1.68% on
  all-spending owner cash. Investment securities (¥23.7bn) are excluded from net cash; adding them raises every per-share
  figure by about ¥560.
- Script and output: `Test Runs/_research 2026-10-13 HRIBF/scripts/q7_compute.py`, `Test Runs/_research 2026-10-13 HRIBF/q7_compute_output.txt`.


## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (Step 0 with the
      foundations and standing rule; Q1; the facts after the stop, the computation and this audit), pathspec of the run
      file and the research folder only.
- [x] Dispatched to an analyst: the brief allowed the per-question commits. The lock is the dispatching session's (operator
      rule 10 (b)); the analyst did not write or check it. The fold into the register is the dispatcher's; until then this
      run binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; no file under `Test Runs/` was
      searched or listed except this run's own folder. What was seen by accident (the opening git status and commit
      subjects, the memory index) is declared under contamination at the top and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (checked by
      `Test Runs/_research 2026-10-13 HRIBF/scripts/check_ids.py`); no E-id is cited. Every filing fact carries its
      document and date (no accession numbers exist: Horiba is not an SEC registrant).
- [x] The order was kept; Q1 failed and closed the run; nothing after it is a clearance, and the Q7 figures are headed
      COMPUTATION, NOT A CLEARANCE.
- [x] Owner cash after every real cost from the filed cash-flow statements, never a net-income proxy (operator rule 5);
      the sovereign is the JPY 30-year from the Ministry of Finance's jgbcme.csv, dated; the Tokyo price is an aggregator
      quote and is flagged; the stale OTC quote is flagged and unused.
- [x] Contrary evidence was written down as found (foundations; Q1's paragraph on the widening share and margins); the
      facts for later questions are under AFTER THE STOP, with the integrity flag in the box line.
- [x] No row dated after the anchor: not a point-in-time run; the anchor is today.
- [x] `tools/run.py` produced no output for this name (HTTP 404 at the SEC); none of its lines was used. All arithmetic is
      by hand from the filings, in `Test Runs/_research 2026-10-13 HRIBF/scripts/owner_cash.py` and `scripts/q7_compute.py`.
- [x] `python tools/check_framework.py` PASS before the final commit (result recorded in the notes file).
- Honest limits: the semiconductor segment's figures for the 2008-2009 downturn could not be read cleanly from the 2011
  annual report's charts and are not used; no rival's filing was read, because the company names none and the file closed
  before Q2; the H1 2026 lease balance was not restated in the semi-annual report and the year-end figure is used.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7 specific (e) against the PG specific on growth.** The central case is maintenance-only owner cash "with the
growth spending charged against the growth it buys", and the growth shown "is measured on the aggregate owner cash". For
Horiba the two aggregate series grow at 12.1% (maintenance-only) and 1.2% (all spending, after acquisitions) over the same
window, and the choice moves the top of the range from about ¥13,100 to ¥35,100 a share. I measured growth on the central
(maintenance-only) series and deducted the growth spending, growing with it, for the ten years, stopping it after year ten
as specific (c) stops acquisition spending; the all-spending case is shown beside. The text does not say which series
carries the growth when (e) applies; it should. The box did not depend on it: no case earns the floor at the price.
(2) **The all-equity basis and interest income.** "Owner cash before interest" does not say whether interest earned on the
cash that is credited in net debt is removed. For a net-cash company it matters in the opposite direction from a borrower.
I removed net interest after tax at the statutory rate (¥0.5bn a year on average). (3) **The brief's competitor rule when
the annual report names no rival.** Horiba's yuho and integrated report name none; the brief has no instruction for that
case. The file closed at Q1, so no rival was chosen; a run reaching Q2 would need a rule. (4) **Q1 for a component maker
inside a fast-changing industry.** The routing sentence and its rows speak of businesses that "must deal with fast-moving
technology"; Horiba's product function has not changed in decades and its share and margins widened through ten years of
process change. Nothing in Q1's tests separates "the function is stable" from "the economics are foreseeable"; the box was
decided by test 9 (doubt) together with the company's own risk rating. A sentence saying whether a stable function inside
a changing industry is inside or outside the routing would make the call reproducible. (5) **Subsequent events.** The
net-debt convention adds "the subsequent events that filing itself states"; the interim dividend declared in the H1 report
and paid after its balance-sheet date was deducted as one. (6) **Non-registrants.** The template's accession fields and
`tools/run.py` assume an SEC filer; the brief's departure covered it, and the template could say so.
