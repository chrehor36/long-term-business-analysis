# Company Run — Telefonaktiebolaget LM Ericsson (ERIC) — 2026-09-13
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation — it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 — THE RATE, AND THE FILING

*Run written under the WRITE-EARLY protocol: this section was written before Q1 opened and every later
section is appended as it closes. The brief was read as a set of hypotheses to refute; it named no expected
verdict and none is assumed here. Every fact the brief supplied is re-derived below from Ericsson's own filings
and marked confirmed or corrected. No prior Ericsson run exists in this tree; the CALX run of 2026-09-12 (the
nearest telecom-equipment file) is context for method only, and no Ericsson figure is inherited from it.*

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 3.227% · Swedish Government Bond, 10-year benchmark (series `SEGVB10YC`) · date 2026-09-11 ·
  source: Sveriges Riksbank, SWEA open data API**
  (`https://api.riksbank.se/swea/v1/Observations/SEGVB10YC/2026-08-25/2026-09-12`, file
  `_research 2026-09-13 ERIC/sov/SEGVB10YC.json`). **Fetched by hand; nothing was added to `tools/sources.py`.**
  The same series read 3.227% on 2026-09-10 and 3.017% on 2026-08-25; the 7-year read 3.076%, the 5-year
  2.989% and the 2-year 2.706% on 2026-09-11.
- **Two limits, stated rather than smoothed.** (1) **The longest tenor the issuing authorities publish as a
  daily yield is 10 years, shorter than the 30 years used for USD, JPY and EUR.** Riksbank's SWEA list of
  government-bond series stops at `SEGVB10YC` (`sov/series.json`: 2Y, 5Y, 7Y, 10Y). Longer nominal bonds exist
  but are thin: the Swedish National Debt Office's *Sweden's Central Government Debt, 31 March 2026*
  (`riksgalden.se/contentassets/894b4829c97342c79f0311245da01114/central-government-debt-mar-2026.pdf`, file
  `sov/cgd_mar2026.txt`) lists **SGB 1053 3.5% 30 Mar 39 (SEK 45.5bn), SGB 1063 0.5% 24 Nov 45 (SEK 19.0bn) and
  SGB 1064 1.375% 23 Jun 71 (SEK 10.75bn)** against SEK 699.0bn of nominal government bonds in all; no daily
  yield for them was found on either authority's site, so none is used. (2) The SWEA series carries the field
  `"source": "Refinitiv"`: the Riksbank publishes it, a data vendor compiles it. **Cross-check at the issuer's own
  primary market:** Riksgälden's latest auction page shows **SGB 1068 2.75% 09 Feb 37 (about 10.4 years)
  auctioned 2026-09-09 at an average yield of 3.0909%**, cut-off 3.0950%, tender ratio 2.33 (page raw text saved, `sov/rg_auction.html`) — within 14 basis
  points of the 10-year benchmark the same week. **3.227% is used; 3.09% is the issuer's own confirmation.**
- **Shown for sensitivity only, from `tools/sources.py`:** USD **5.35%** (US Treasury daily par yield curve,
  30-year, 2026-09-11) · EUR **3.826%** (ECB euro area AAA curve SR_30Y, 2026-09-10).
- **Where Ericsson earns, from the filing — and it is not Sweden.** Note B1 (net sales by country of customer,
  2025): **United States SEK 96,467m of 236,681m = 40.8%**; EU SEK 34,665m (14.6%); India 12,267m (5.2%);
  Japan 8,493m (3.6%); China 8,197m (3.5%); **Sweden SEK 3,384m = 1.4%**. Note F1's currency-exposure table
  (2025): **USD sales SEK 136.9bn against USD costs SEK 95.5bn; EUR sales 38.6bn against costs 31.0bn**; the SEK
  line is not shown because it is the reporting currency. Risk factor 2.1: *"Ericsson incurs a significant portion
  of the Company's expenses in SEK"* and *"As market prices are predominantly established in US dollars or Euros,
  Ericsson presently has a net revenue exposure in foreign currencies."* Employees: 12,806 of 88,826 in Sweden
  (14.4%); non-current assets SEK 42,565m of 73,860m in Sweden (57.6%, mostly goodwill held by the parent).
  **So roughly 99% of sales are earned outside Sweden, a larger foreign share than Honda's 88% or Sony's.**
- **Why SEK anyway — argued from the corpus, not defaulted.** [E4-15] makes the rate a gravity on the value of
  the claim; the claim a Stockholm shareholder holds is **denominated, reported, paid and priced in kronor**: the
  statements are in SEK (Note F1: *"The Company reports the financial statements in SEK"*), the SEK 3.00 dividend
  is declared in SEK in two instalments (Note E1), the SEK 15bn buyback is executed in SEK on Nasdaq Stockholm
  (6-K 2026-04-16), and the quote used below is the Stockholm quote in SEK. **[E3-32] forbids a view on rates, and
  choosing the US rate because 41% of sales are American — or 58% of sales are dollar-priced — would be a view on
  which currency's rate the owner will one day be paid in.** The foreign earning base is carried as **width in the
  SEK owner-earnings figure** (reported SEK moved by currency: *"a currency impact of SEK –13.9 billion"* on 2025
  sales), not as a second rate — the MITSY, SONY, TM and HMC precedent, argued again on Ericsson's own mix, which
  is the most foreign of the four. **And the choice cannot change a verdict at Q5:** the ~10% floor [E4-28] holds
  *"whether short rates are 6 percent or whether short rates are 1 percent"* — above 3.23% SEK, 3.83% EUR and
  5.35% USD alike.
- **FX, quote vs earnings: none needed for the cap.** The cap is taken **in SEK from the Stockholm quote of the
  B share (ERIC-B.ST)**, so cap and SEK owner earnings share a currency by construction. **The USD ADR is never
  used for the cap.**
- **ADR ratio, from the filing:** 20-F cover, *"American Depositary Shares (each representing one B share)"*;
  Item 4.A, *"our American Depository Shares ("ADS"), each representing one underlying Class B share, are traded on
  NASDAQ New York"*; Exhibit 2.3 repeats it. **Derived check:** ERIC $10.31 × Riksbank USD/SEK fixing 9.69401
  (series `SEKUSDPMI`, 2026-09-11) = **SEK 99.95** against ERIC-B.ST SEK 98.66 the same day (both closes Yahoo,
  **aggregator, live quotes only, flagged**) — 1.3% apart, consistent with one B share per ADS and with the
  later New York close on a day the ADR rose 3.0%.

**THE SHARE CLASSES — read from the charter before summing (the brief's instruction, discharged).**
- Exhibit 2.3 to the 20-F (*Description of Securities*, summarising the Articles of Association): *"each Class A
  share shall carry one vote, each Class B share one tenth of one vote and each Class C share one-thousandth of one
  vote"*; *"Our Class A and Class B shareholders have the same right to dividends. Class C shareholders do not have
  any right to dividends"*; on liquidation, surplus assets *"will be equally distributed amongst our shareholders in
  proportion to the par value of the shares held by them"* — and A and B both carry **SEK 5.00** quota value (20-F
  cover; Note E1). Note E1 states it outright: *"Both classes have the same rights of participation in the net
  assets and earnings. Class A shares, however, are entitled to one vote per share while Class B shares are entitled
  to one tenth of one vote per share."* **A and B share economics equally and are summed. Class C: none
  outstanding** (cover: *"C shares (SEK 5.00 nominal value) | 0"*); the 23,100,000 C shares issued for LTV in 2025
  were *"repurchased … subsequently converted into Class B shares"* (Note E1).
- **Control, recorded for Q3 and [E3-66]:** Investor AB holds *"approximately 24.8% of the votes (9.9% of the
  shares)"*, AB Industrivärden *"approximately 15.0% of the votes (2.6% of the shares)"*, AMF *"approximately 5.1% of
  the votes (3.2% of the shares)"* (Board of Directors' Report, *Share information*). Two holding companies with
  12.5% of the capital hold about 40% of the votes.

**THE SHARE COUNT — by hand (a 20-F filer: `cover_shares.py` cannot see a 6-K, RESUME STATE §5).**
1. **The 20-F cover is ISSUED, not outstanding — a trap, recorded.** The cover's "number of outstanding shares"
   reads **B 3,109,595,752 · A 261,755,983 · C 0 = 3,371,351,735**, which equals Note E1's *"Number of shares …
   As of December 31 | 261,755,983 | 3,109,595,752 | 3,371,351,735"* — the **issued** total. The same note:
   *"At December 31, 2025, the total number of treasury shares was 38,002,276 … Class B shares."* **Outstanding at
   2025-12-31 = 3,333,349,459.** Cross-check: basic average shares 2025 *"3,333"* million (Note H2). **Confirmed.**
2. **The buyback since then.** 6-K 2026-04-16 (`0001193125-26-159055`): the Board *"resolved to utilize the
   authorization granted by the March 31, 2026 Annual General Meeting to initiate a share buyback program … up to a
   maximum consideration of SEK 15,000,000,000"*; the weekly 6-Ks from 2026-04-28 to 2026-09-08 (18 releases, all
   in `_research 2026-09-13 ERIC/6k/`, summed by `bb.py`) report **70,349,695 Class B shares repurchased for SEK
   7,299.1m, average SEK 103.75**, 2026-04-23 to 2026-09-04.
3. **Latest filed count: 6-K filed 2026-09-08 (`0001628280-26-060848`), release dated September 7, 2026:**
   *"Following the repurchases above, Ericsson's holding of treasury stock amounts to 105,668,676 Class B shares.
   There are in total 3,371,351,735 shares in Ericsson, 261,755,983 shares of Class A and 3,109,595,752 shares of
   Class B."* **Outstanding at 2026-09-04 = 3,371,351,735 − 105,668,676 = 3,265,683,059.**
4. **Reconciliation:** treasury rose 38,002,276 → 105,668,676 = +67,666,400 against 70,349,695 bought; the
   **2,683,295** difference is treasury stock delivered under LTV 2023 (6-K 2026-05-13, *"In conjunction with the
   delivery of vested shares under the long-term variable compensation program I and II 2023"*). **Reconciles.**
   The program runs *"between April 23, 2026, and March 31, 2027, at the latest"*; SEK ~7.7bn of the SEK 15bn is
   unspent, so the count will keep falling (at SEK 98.66, roughly 78M more shares, 2.4%).
5. **Shares used: 3,265,683,059** (as at 2026-09-04).
- **Split:** `split_factor_after('ERIC-B.ST','2025-12-31')` returns **1.0**; no split or reverse split is described
  in the 20-F or any 6-K read. Cap = close(2026-09-11) × shares(2026-09-04) × 1.0.
- **Price SEK 98.66** (ERIC-B.ST close 2026-09-11, Yahoo, aggregator flagged; ERIC-A.ST SEK 99.00 the same day)
  × **3,265,683,059** = **market cap SEK 322.2bn**. *(Pricing the 261.8M A shares at their own SEK 99.00 adds SEK
  0.09bn, 0.03%; not used. Pricing on the 20-F cover's 3,371M issued shares would have overstated the cap by SEK
  10.4bn, 3.2%.)*

**THE PERIMETER — the filings, with dates. Nothing here is from memory.**
- **Vonage: ACQUIRED July 2022, inside the five-year window.** Note E2 and the strategy section: *"The 2022
  acquisition of Vonage enables Ericsson to expose advanced network capabilities via network APIs"*; the National
  Security Agreement was entered *"in July 2022"* (risk factor 3.3). Consideration, cash flow and goodwill are read
  from the FY2022 20-F at Q1/Q3 (not yet on disk when this was written). **Impairments since, filed:** 2023
  *"impairment charge of goodwill attributed to the acquisition of Vonage by SEK – 31.9 billion"*; 2024
  *"impairment charges attributed to the acquisition of Vonage were made for intangibles and goodwill by SEK – 14.7
  billion"* (Note C1). Remaining goodwill in Global Communications Platform (Vonage) **SEK 9.1bn**, with headroom of
  only **SEK 2.7bn** (*"The recoverable amount of Global Communications Platform exceeds the carrying amount by SEK
  2.7 billion"*).
- **iconectiv: DIVESTED August 2025, inside the window.** Note E2: *"In August 2025, the Company divested
  iconectiv, which was an acquired US subsidiary ( 83.3 % ownership) … The transaction resulted in a capital gain of
  SEK 7.6 billion. iconectiv's consolidated contribution to Ericsson's 2024 net income was approximately SEK 1.0
  billion."* Divestment proceeds SEK 11.2bn (cash-flow statement, "Divestments of subsidiaries" 11,638).
- **Smaller moves:** IoT businesses divested March 2023; Ericom acquired April 2023 (SEK 579m); Aduna associate
  (50%) July 2025, SEK 516m; Cradlepoint (acquired before the window, goodwill SEK 8.3bn) remains. Cradlepoint's
  acquisition date and price are read at Q3 from the FY2020 filing, not asserted.
- **How this run handles it:** owner earnings are built on the consolidated statements, and the Vonage and
  iconectiv windows are named where they sit; the Vonage cash price and its operating contribution are read before
  any mean is trusted (Q4). No pro-forma is invented.

**Company name, and the 20-F/A of 2018:** registrant "ERICSSON LM TELEPHONE CO", CIK 0000717826, `formerNames`
empty (`submissions.json`); `deal_note(717826)` and `name_change_note(717826)` returned nothing — **confirmed**, and
blind to 6-K-disclosed transactions (Vonage, iconectiv), exactly as HMC found. **The 20-F/A filed 2018-04-20
(`0001193125-18-124911`) is read at Q3** for what it amended.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A (the 20-F incorporates by reference the Swedish Annual Report 2025 (adjusted version), Exhibit 15.1:
  Board of Directors' Report — financial highlights, segments, market areas, legal proceedings, share information,
  proposed disposition of earnings and buyback; CEO comment; Chair's comment; strategy and targets) — read in full
- [x] cash-flow statement incl. detail lines (consolidated statement 2023–2025; Note H3 adjustments, D&A and
  impairments by asset class, acquisitions/divestments)
- [x] footnotes (A1, A2, B1–B9, C1–C3, D1–D4, E1–E3, F1, F2, F4, G1 (part), G3, G4, H1–H6 read; risk factors
  1.1–3.7 read; Exhibit 2.3 read)
- **Primary document: Form 20-F for the fiscal year ended December 31, 2025, filed 2026-03-12, accession
  `0001193125-26-104149`** (`d948057d20f.htm`, Exhibit 15.1 `d948057dex151.htm`) — **confirmed**. Latest 6-K
  **2026-09-08, `0001628280-26-060848` — confirmed**; the Q2 2026 report 6-K 2026-07-14 (`0001628280-26-048088`)
  and every 6-K since 2025-10-01 (49 documents) are on disk. Earlier 20-Fs are read at the gate that needs them.
- **Figure cross-checked against the filed statement:** consolidated **cash flow from operating activities 2024,
  SEK 46,261m** — identical in the FY2025 20-F cash-flow statement (Exhibit 15.1, p.34), in XBRL companyfacts
  `ifrs-full:CashFlowsFromUsedInOperatingActivities` = 46,261,000,000 SEK (accessions `0001193125-25-051949` and
  `0001193125-26-104149`), and in the Board of Directors' Report text (*"Cash flow from operating activities was SEK
  33.0 (46.3) billion"*).
- **Tooling note — the brief's skip reason, TESTED, and it is neither of the two causes proposed.** (a) The triage
  said *"short XBRL history"*: **false for Ericsson** — companyfacts holds **11 annual IFRS periods, 2015–2025**, of
  operating cash flow, PP&E capex, D&A and revenue. (b) The SONY/TM/HMC finding, *companyfacts had not ingested the
  newest 20-F*: **false for Ericsson** — the FY2025 20-F (`0001193125-26-104149`) is ingested. (c) **The real cause,
  reproduced this run:** `python tools/run.py ERIC` prints *"ERIC: no overlapping OCF/D&A/capex annual facts.
  UNRESEARCHED."* because `tools/run.py`'s tag lists (`OCF`, `DA`, `CAP`, `SBC`, `NI`) contain **only US-GAAP
  element names**, while `sources.annual()` searches the `ifrs-full` namespace **with those same US-GAAP names**.
  An IFRS filer's `CashFlowsFromUsedInOperatingActivities`, `PurchaseOfPropertyPlantAndEquipment…` and
  `DepreciationAndAmortisationExpense` are never requested. **Every IFRS 20-F filer is unpriceable by construction**,
  whatever its history. Reported to the operator, not fixed here (a tool change is outside a run's brief).

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Answered per segment, as SONY, HMC and GHC were, from the filed segment note (Note B1).** 2023–2025 from the
FY2025 20-F (`0001193125-26-104149`); 2020–2022 from the FY2022 20-F (`0001193125-23-071310`), whose segment
definitions are the current ones. SEK million.

| Segment | Net sales 2020 → 2025 | EBIT margin 2020 · 21 · 22 · 23 · 24 · 25 | Gross margin 2025 | Products / services 2025 | Share of 2025 sales |
|---|---|---|---|---|---|
| **Networks** | 165,978 → 151,014 | 18.6 · 22.2 · 19.9 · 11.3 · 16.2 · **19.7%** | 49.7% | 115,488 / 35,526 | **64%** |
| **Cloud Software and Services** | 59,597 → 62,715 | (1.3) · (4.0) · (2.8) · (0.3) · (0.7) · **9.6%** | 41.7% | 24,016 / 38,699 | 26% |
| **Enterprise** | 4,792 → 21,117 | (40.4) · (47.5) · (40.5) · (148.9) · (88.8) · **15.3%** *(7.6bn iconectiv gain inside; ex-gain ≈ (20.7)%)* | 53.9% | 4,230 / 16,887 | 9% |
| **Other** (Red Bee Media, unallocated) | 2,023 → 1,835 | (15.4) · (14.2) · (164.2) · (45.5) · 53.6 · **(22.3)%** | 3.0% | — / 1,835 | 1% |
| **Group** | 232,390 → 236,681 | 12.0 · 13.7 · 10.0 · (7.7) · 1.7 · **16.3%** | 47.6% | 143,734 / 92,947 | — |

*2025 sales by commodity (Note B2): hardware SEK 88,612m, software 55,122m, services 92,947m; **IPR licensing
revenues SEK 14,506m** (13,962m in 2024, 11,101m in 2023), *"82 % … reported as part of segment Networks"* and 18% in
Cloud Software and Services. Ex-gain Enterprise margin: (3,239 − 7,600) ÷ 21,117, using the "SEK 7.6 billion" gain as
filed; the note gives no more decimals.*

- **Unit economics in my own words, no management language:**
  1. **Networks — it sells the radio half of a mobile network, one generation at a time, to a few hundred phone
     companies, and then keeps selling it capacity, software features and patents.** A mobile operator buys radios,
     antennas, baseband units and the software that runs them, plus installation, from a vendor it has chosen for a
     region; it then buys more of the same as traffic grows, software upgrades, and — once a decade — the next
     generation. Ericsson collects on the equipment and deployment (a low-margin services leg), on the software
     inside the equipment, and on **patent licences paid by handset makers** (SEK 14.5bn, most of it near-pure
     margin; the note attributes 82% to this segment). **The whole segment earned 19.7% EBIT on SEK 151bn in 2025,
     and 11.3% two years earlier.** The customers are few and large: *"Out of a customer base of more than 500
     customers … the 10 largest customers accounted for 46 % … The largest customer accounted for approximately 14 %"*
     (Note B1, 2025; 50% and 14% in 2022). What it sells has no fixed price or quantity: *"Many of these agreements do
     not contain committed purchase volumes or prices and may include commitments to future price reductions"* (risk
     factor 1.12, 2025) — and in 2013 and 2016, *"Many of these agreements are opened up on a yearly basis to
     renegotiate the price for our products and services and do not contain committed purchase volumes."*
     The spend is lumpy by country and generation: India sales SEK **31,205m (2023) → 15,194m (2024) → 12,267m
     (2025)**, *"primarily due to reduced investment levels in India"*.
  2. **Cloud Software and Services — the network's control software (core network, billing and operations
     systems) and outsourced network operation.** 62% services (*"Services accounted for 62% (64%) of net sales"*).
     It lost money five years running on the current definition and earned 9.6% in 2025 after restructuring
     (restructuring charges SEK 1,154m in 2025, 2,434m in 2024).
  3. **Enterprise — two acquired US businesses and a start-up market.** Vonage (cloud communications and
     developer APIs, *"Global Communications Platform"*) and Cradlepoint (*"Enterprise Wireless Solutions"*,
     wireless WAN routers and private 5G). **Vonage cost SEK 53,269m of consideration** (*"Purchase price paid on
     acquisition | 51,297 · Deferred consideration/Others | 1,972"*) plus *"a Vonage debt of USD -0.6 billion (SEK
     -5.9 billion) was repaid"*, and brought *"Intangible assets | 23,554"* and *"Goodwill | 41,296"* (FY2022 20-F,
     Note E2). Its own filed numbers at purchase: *"Vonage's net sales and EBIT (loss) for the 2022 financial year,
     as though the acquisition date occurred at the beginning of the annual reporting period, amounts to SEK 14.4
     billion and SEK – 3.0 billion respectively."* **Written down SEK 31.9bn (goodwill, 2023) and SEK 14.7bn
     (intangibles and goodwill, 2024)**; SEK 9.1bn of goodwill remains with SEK 2.7bn of headroom (Note C1, 2025).
     The segment made money in 2025 only by selling iconectiv (gain SEK 7.6bn).
  4. **Other** — a broadcast-services unit (Red Bee Media), 1% of sales.
- **The scarce input this business controls — and it differs in kind by leg:** **Networks: a place on a very short
  list.** For an operator outside China, the radio vendors that can deliver a national network at scale are few,
  and the filing says so indirectly: *"restrictions imposed on Chinese vendors or components in 5G networks …
  have been adopted in many countries"* (risk factor 1.1). Within that list Ericsson holds **an installed base on
  *"206 live 5G networks in 85 countries"***, a portfolio of *"more than 60,000 granted patents"* licensed on FRAND
  terms, and R&D at SEK 48.9bn a year (20.6% of sales). Its market-share figure (*"around 37% market share, outside
  China"*) is **Dell'Oro's, quoted by the company — not a filed measurement**, and is used at Q2 only as the company's
  claim. **Cloud Software and Services:** software embedded in operators' core networks — switching cost of a kind,
  tested at Q2. **Enterprise:** nothing scarce shown by the filing; Vonage competes in *"the high growth CPaaS …
  UCaaS … CCaaS markets"* and Cradlepoint in wireless WAN, both contested.
- **"On what capital?" — the segment note gives no segment assets** (unlike Honda's), so the capital question is
  answered at group level at Q2 and Q4, and the Enterprise capital is the SEK 59bn of Vonage cash plus the Cradlepoint
  price (read at Q3). What *is* filed: goodwill SEK 26.2bn in Networks, 3.3bn in CSS, 17.5bn in Enterprise (Note C1).
- **Will the fundamentals look broadly the same in ten years?** **Networks: the model, yes; the position, not
  certainly.** Operators will still buy radio networks from a few vendors and handset makers will still pay patent
  royalties; but the filing itself names the forces that change the *terms*: a *"flat RAN market"* (CEO), *"little or
  no growth in our core mobile infrastructure market"* (Chair), 6G *"expected to begin before 2030"*, Open RAN that
  *"could lower barriers to entry and enable new or alternative radio and software suppliers"* (risk factor 1.10), and
  *"customers are no longer required to purchase from one vendor"* (1.12). **CSS: yes, as a software-and-services
  attachment to the same base. Enterprise: no — its two businesses were bought in 2020 and 2022 and one is already
  mostly written off.**
- **The hunt for disconfirming evidence [E4-26], before the verdict.** [E3-31] asks for businesses *"relatively simple
  and stable in character"* and excludes those *"subject to constant change"*; Ericsson's own words are *"markets in
  which the technology and the manner in which it is being brought to market is rapidly changing"* (1.5). [E4-46] puts a
  business that needs months of study outside the circle. **But Q1 asks whether the money-making can be understood,
  not whether its future can be predicted** — the second is Q2's [E4-04] (a moat *"continuously rebuilt"*) and Q4's
  range, exactly where the TSM run (2026-09-13) put its rapid-change finding after a Q1 IN on semiconductors, and where
  CALX (2026-09-12) put it for telecom access equipment. The mechanism here is legible from the filing in a paragraph:
  who pays (operators, and handset makers for patents), for what (radio capacity, software, services, licences), in
  what pattern (generation cycles, country build-outs, annual repricing, no committed volumes), and at what margin by
  segment. **What is not stable is named above so it cannot be averaged away later.** One thing I cannot see from the
  filing — the price per unit of radio sold — is recorded as a limit, not assumed: Ericsson files no unit volumes.
- **VERDICT: [x] IN** — the money-making is understandable segment by segment from the filed 20-F: a radio-network
  vendor with a patent-licence stream, an attached core-software-and-services business, and an acquired enterprise
  leg whose cost and write-downs are filed. Understanding is the gate; durability, relative position and the capital
  each leg consumes are Q2's and Q4's. *(No "unverified" or "provisional" caveat is carried; the Dell'Oro share is not
  relied on.)*

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**Per leg, with the metric set chosen by business type first [E5-37]; the verdict must hold for what the shareholder buys
(GHC 2026-09-02, HMC 2026-09-13).** Networks is 64% of sales and, in every year 2020–2025, more than all of group EBIT; it
carries the verdict, so it is tested first and hardest. Competitor transcriptions were made by two research passes and are
on disk with accession numbers, URLs and verbatim lines: `_research 2026-09-13 ERIC/peers/NOKIA_row.md` and
`peers/OTHERS_row.md`; **every Nokia figure used below was spot-checked against the transcription's own cross-check line**
(Mobile Networks 2023 net sales EUR 9,797m, identical in Nokia's Note 2.2 and Item 5, 20-F `0000924613-24-000013`).

### 1. NETWORKS — the radio business
**[x] needed or desired · [ ] no close substitute · [~] not price-regulated (radio: no; its patent leg: FRAND terms under
antitrust review).**

**THE COMPETITOR ROW — the radio segment's operating margin, excluding restructuring on both sides, 2014–2025.**
*Ericsson: Networks segment EBIT plus that segment's restructuring charges, ÷ segment sales (Note B1/C3 of each 20-F; the
segment was redefined in 2017, so 2014–2016 are the old "Networks" and 2017–2025 the current one). Nokia: the radio
segment's own non-IFRS/segment operating profit, which *"excludes restructuring and associated charges, purchase price
accounting related charges"*, as stated in each 20-F; its segment boundary moved in 2016, 2017, 2019, 2021 and 2025, and
each row names the boundary used.*

| Year | **Ericsson Networks** (EBIT ex restructuring ÷ sales) | Nokia radio segment (segment operating profit ÷ sales) | Nokia's boundary that year | Gap, points |
|---|---|---|---|---|
| 2014 | **11.9%** (13,544 + 443 on 117,487) | 11.3% | Mobile Broadband (radio + core) | +0.6 |
| 2015 | **12.8%** (12,943 + 2,839 on 123,720) | 10.0% | Mobile Broadband | +2.8 |
| 2016 | **8.1%** (4,727 + 4,040 on 108,338) | 8.6% (9.4% restated) | Ultra Broadband Networks (radio + fixed) | (0.5) to (1.3) |
| 2017 | **11.6%** (10,455 + 4,828 on 132,285) | 8.7% | Ultra Broadband Networks | +2.9 |
| 2018 | **15.3%** (19,421 + 1,781 on 138,570) | 5.9% | Ultra Broadband Networks | +9.4 |
| 2019 | **16.0%** (24,767 + 68 on 155,009) | 3.4% | Mobile Networks (2021 recast) | +12.6 |
| 2020 | **19.0%** (30,851 + 746 on 165,978) | 7.9% | Mobile Networks (recast) | +11.1 |
| 2021 | **22.4%** (37,266 + 262 on 167,838) | 7.9% | Mobile Networks | +14.5 |
| 2022 | **20.0%** (38,512 + 146 on 193,468) | 8.8% | Mobile Networks | +11.2 |
| 2023 | **13.9%** (19,382 + 4,437 on 171,442) | 7.4% (7.6% recast) | Mobile Networks | +6.3 to +6.5 |
| 2024 | **17.4%** (25,665 + 1,899 on 158,207; filed *"adjusted EBIT margin of 17.4%"*) | 5.3% (5.5% recast) | Mobile Networks | +11.9 to +12.1 |
| 2025 | **20.4%** (29,809 + 1,006 on 151,014; filed *"20.4%"*) | 2.8% | Mobile Networks incl. Managed Services | +17.6 |

**The rest of the row — as many as the industry has, and what each filing lets me say:**
| Company | what is filed | same metric? | source |
|---|---|---|---|
| **Huawei** (not an SEC filer; audited-summary annual reports in English, KPMG Huazhen) | Carrier revenue CNY 294,012m (2018) · 296,689m (2019) · 302,621m (2020) · 281,469m (2021) · 283,978m (2022), then only "ICT Infrastructure" (adds enterprise, computing, storage); **no segment profit in any year**; group operating margin 8.1–11.0% in 2019, 2020, 2024, 2025 (19.1% and 14.8% in 2021 and 2023 with large "other income") | **No** — revenue only | huawei.com/en/annual-report, AR2018–AR2025 (URLs in `OTHERS_row.md`) |
| **ZTE** (HKEX 0763 / SZSE 000063; audited PRC-ASBE annual reports in English, Ernst & Young Hua Ming) | "Carriers' network" revenue RMB 74,018m (2020) · 75,712m · 80,041m · 82,759m · 70,327m · **62,857m (2025)**; gross margin as filed 33.79% · 42.45% · 46.22% · 49.11% · 50.90% · **48.09%**; segment results 25.6–42.6% of revenue but *"except for the exclusion of … research and development costs"*; group operating margin 5.4% · 7.6% · 7.2% · 8.3% · 7.7% · **4.8%** (2020–25). Its own words: *"a firmly set market duopoly"* (domestic, 2023) and *"domestic carriers' investment continued to decline in a period of maturity for 5G network construction"* (2025); abroad, share won at *"wireless network modernisation upgrades"* (2023) | **No** — gross margin and an ex-R&D segment result; carrier segment includes wireline, core, and (2025) servers | HKEXnews annual reports 2020–2025 (URLs in `OTHERS_row.md`) |
| **Samsung Networks** (inside Samsung Electronics, KRX; business reports and earnings decks on samsung.com/global/ir) | **Networks revenue and operating profit NOT separately disclosed in any year FY2016–FY2025**: audited segment is DX (*"TVs, monitors, refrigerators, washing machines, air conditioners, smartphones, network systems, computers, etc."*); decks combine *"MX / Networks"*. Qualitative only: *"overseas 5G sales increased, including in the US and Japan"* (4Q19); *"sales growth in North America"* (4Q25) | **No — the limit of the source, stated** | 2016–2025 Business Reports; 4Q17–4Q25 decks (paths in `OTHERS_row.md`) |
| **Ciena** (10-K) | group GAAP operating margin 9.7% · 13.8% · 13.7% · 6.1% · 8.2% · 4.1% · 4.1% (FY2019–25); **no radio business**; names Ericsson only as a *"Blue Planet Automation Software"* competitor | No — optical/transport overlap only | 10-Ks `0000936395-19-000056` … `0001628280-25-056698` |
| **Cisco** (10-K) | group GAAP operating margin 20.8–27.6% (FY2019–25); **no radio business**; **Ericsson named in none of eight 10-Ks FY2019–FY2026** | No — IP routing overlap only | 10-Ks `0000858877-19-000012` … `0000858877-26-000132` |

- **Peers named: 7 of the industry's ~5 scale radio vendors plus 2 adjacent** (Nokia, Huawei, ZTE, Samsung in radio; Ciena
  and Cisco adjacent). **Same-metric figures exist for one radio peer only — Nokia.** Huawei discloses carrier revenue and no
  carrier profit; the other limits are stated in their rows. **The moat class would therefore be PROVISIONAL on the row alone.
  It is not left there, because the verdict below does not turn on the row: it turns on criterion (2), and criterion (2) is
  answered by the customers' behaviour as filed by Ericsson and Nokia, which is complete.** [E3-61]: the row shows position,
  not conduct.

**What the row shows — position.** From even with Nokia in the late-4G years (2014–2017, a gap of −1.3 to +2.9 points) to
**6–18 points ahead in every 5G year 2018–2025.** That is a real position, and its direction is widening [E4-32]. Nokia's
own filings name the cause from the loser's side: *"certain competitors sought to take share in the early stages of 5G"*
(Nokia 20-F FY2019), *"market share loss and price erosion in North America"* (FY2020 CEO letter, and FY2021), and in 2024
*"Nokia resolved its outstanding negotiation with AT&T, who decided to proceed with an alternative RAN vendor for commercial
reasons"*. Ericsson's United States sales rose from **SEK 46,519m (2011, 20.5% of sales) to 96,467m (2025, 40.8%)** while its
China sales fell from **SEK 18,745m (2020) to 8,197m (2025)** (Note B1 of each 20-F).

**[E3-03] criterion (2) — "no close substitute" — FAILS, on both vendors' filings.** The customers' behaviour is on file:
1. **Operators dual-source.** Nokia 20-F FY2021 (`0001558370-22-002758`): *"Competitive dynamics in the CSP industry strongly
   favor the top two vendors. **Almost all CSPs dual source, giving vendors no pricing power unless they offer some technology
   advantage.**"*
2. **Installed networks are swapped, and share moves generation by generation.** Ericsson 20-F FY2013: *"The majority of the
   European network modernization projects, which put pressure on our margins in recent years, are now behind us; in line with
   our strategy we now have a strong installed base in Europe"* — an installed base **bought** in a swap cycle. Nokia 20-F
   FY2013: *"a wave of network modernization that has taken place, primarily in Europe … has continued to put pressure on
   pricing as the vendors compete for market share."* Nokia 20-F FY2019 reports its 4G-to-5G **"conversion rate … 93.5%"** —
   the generation re-bid measured, and less than all of it re-won. And a whole national network changed vendor in 2024: AT&T *"decided to proceed with an alternative RAN vendor for commercial
   reasons"* (Nokia FY2024, the vendor not named), in the same period in which Ericsson's FY2023 20-F records *"our agreement
   with AT&T to lead the commercial deployment of Open RAN in the United States"* — consistent with a swap to Ericsson, which
   neither filing states in terms, so none is asserted.
3. **The contracts do not bind the buyer.** Ericsson, 2013 and 2016: *"Many of these agreements are opened up on a yearly basis
   to renegotiate the price for our products and services and do not contain committed purchase volumes."* Ericsson, 2025:
   *"Many of these agreements do not contain committed purchase volumes or prices and may include commitments to future price
   reductions"* and *"due to open interfaces, Ericsson's customers are no longer required to purchase from one vendor"*. Nokia,
   from 2018: *"framework agreements with no fixed commitment on the overall project scope"*.
4. **Buyers hold the leverage and use it.** *"the 10 largest customers accounted for 46 %"*, the largest *"approximately 14 %"*
   (Note B1, 2025); *"customers … exercise significant buying power through the common use of a competitive bidding process"*
   (risk factor 1.5).
- **Against the lock-in hypothesis, stated at full strength [E4-51]:** a radio network is not re-bought lightly — Ericsson's own
  2016 plan was *"to leverage the installed base … grow capacity sales and leverage new spectrum"*, and the 2013 report calls
  *"The installed base of radio networks … the foundation for Ericsson's business with mobile operators."* **Within a
  generation, the incumbent sells the capacity.** The filings answer where that stops: at the next generation and at the
  annual repricing, where criteria (1)–(4) above apply.

**[E2-44], the two-characteristic test.** *(1) Price under slack demand:* **fails on the filings' own words** — *"continuous
price erosion and increased price competition"* (Ericsson, 2013 and 2016), *"continuous price pressure"* (2019 and 2025);
*"Historically, the RAN market has been largely flat over time but with cyclicality"* (FY2023) — a flat market in which the
customer extracts *"commitments to future price reductions"*. The one pricing action on file is a cost pass-through, and it is
prospective: *"we took action to mitigate component cost inflation … we will continue to pursue internal measures and pricing
actions to help offset the effect"* (Q2 2026 report). *(2) Volume with minor capital:* **yes on tangible capital** (capex
1–2% of sales; operating tangible equity about minus SEK 7bn, Q3) — **but not on total spend:** R&D rose SEK 34.8bn (2015) →
53.5bn (2024) → 48.9bn (2025) against group sales of SEK 246.9bn → 247.9bn → 236.7bn. The growth capital here is
expensed.

**[E3-62], the second step — who keeps the savings.** Ericsson's gross margin rose 38.6% (2023) → 44.1% → 47.6% (2025) on
*"cost-reduction actions and operational efficiency"*; the same years' Networks sales fell SEK 171.4bn → 151.0bn. The 2019
report states the other half of the bargain: *"When pursuing expansion of market footprint, initial margins may be
challenging, while expected to be profitable over time"*, and 2018–2019's *"negative impact from strategic contracts in
Networks"*. **Share is bought with margin at the start of a generation and recovered through cost-cutting later; the
customer keeps the first part.**

**[E4-04] — must the moat be continuously rebuilt? YES, by the filing's own description.** *"Deployments of the next
generation of mobile technology, 6G, are expected to begin before 2030"*; *"if a competitor develops, commercializes and
deploys 6G before Ericsson or subsequently captures 6G opportunities in markets of strategic importance, Ericsson's competitive
position, technology leadership, market share, pricing and future growth could be materially and adversely affected,
irrespective of the merit of Ericsson's products and technologies"* (risk factor 1.4). Capital-allocation principle (1)
commits R&D *"even during periods of increased market volatility or low visibility"*. The scope test of the framework: **does
a lapse in spending destroy the structure, or merely narrow it — and does the spending defend the same advantage, or buy its
replacement?** Here the spending buys the *next* generation's product, and a lapse loses the next tender — **the Mitsui
case, not the Coca-Cola case.** This is the excluded class: *"industries prone to rapid and continuous change"* [E4-04], a
**surfing run** [E3-51] whose wave is the generation.

**[E2-59] — whose moat is it?** The 5G-era widening coincides with governments excluding the lower-priced vendor. Ericsson:
*"restrictions imposed on Chinese vendors or components in 5G networks … have been adopted in many countries"* (risk factor
1.1). Nokia FY2013: Huawei and ZTE *"have gained market share by leveraging their low-cost advantage in tenders"*; Nokia FY2019:
*"Excluding mainland China, where local players have a dominant market share"*. **The part of the position that rests on the
exclusion belongs to the regime, and Ericsson's own risk factor describes the regime as changeable**: governments *"could support
a competitor as a national champion"* in *"the US, India and Japan"*. [E2-58]'s exception (a cost advantage *"wide and
sustainable"*) is not claimed for Ericsson in any filing; the low-cost vendor is the excluded one.

**The patent leg — the one franchise-like stream, and too small to carry the security.** IPR licensing revenues SEK 14.4bn
(2015) · 10.0bn (2016) · 8.3bn (2017) · 8.0bn (2018) · 9.6bn (2019) · 10.0bn (2020) · 8.1bn (2021) · 10.4bn (2022) · 11.1bn
(2023) · 14.0bn (2024) · 14.5bn (2025) — **6.1% of 2025 sales**, *"with margins above the Company average"* (FY2016). It is
needed (standard-essential), has no substitute for a handset maker selling 5G, and **fails criterion (3)**: licensed *"on fair,
reasonable and nondiscriminatory terms"* (20-F Item 5.C) and under antitrust investigation in China since April 2019 (SAMR), with India's Competition Commission investigations
described in the FY2024 20-F — **price-regulated in the [E3-03] sense.** Its renewals are lumpy (*"a non-recurring benefit from a
partial settlement in the prior year period"*, Q2 2026) and require litigation.

- **Key-person dependence [E4-23]:** low — the CEO leaves on 2026-09-30 and an internal successor was named; recorded in the
  business's favour.
- **Dominance [E2-53]:** no leg. **Untapped pricing power [E3-33]:** not claimed — [E5-28] would require near-monopoly, and the
  row and the customers' dual sourcing show otherwise.
- **Attacker's test [E2-45]:** a funded attacker cannot build a 5G radio portfolio, 60,000 patents and 85 countries of
  deployment quickly — **but the attacker is not hypothetical and does not need to:** Huawei and ZTE already exist at larger
  carrier revenue, Samsung is a named regional vendor (Nokia FY2016–18: *"two regional vendors, ZTE and Samsung, that operate with a below 10% market share"*), and Open RAN is designed to let *"new or alternative radio and
  software suppliers"* in (risk factor 1.10). **The attack is by regulation's permission, not capital.**

### 2. CLOUD SOFTWARE AND SERVICES — NONE
Core-network software plus managed services, 62% services; EBIT (1.3)%, (4.0)%, (2.8)%, (0.3)%, (0.7)%, 9.6% (2020–2025).
*"the increasing influence of open-source initiatives could drive a best of breed approach in Ericsson's customers, driving
prices down"*; *"For managed services … Risk of termination and reduced scope or renegotiation of existing contracts"* (risk
factor 1.13). Five loss years in six do not show a franchise's pricing [E3-43].

### 3. ENTERPRISE — NONE
Vonage competes in *"CPaaS … UCaaS … CCaaS markets"* whose *"trends have also significantly impacted the market capitalization of
Vonage's publicly traded peers"* (Chair, FY2023); SEK 46.6bn of Vonage written off; EBIT (40.4)% to (148.9)% 2020–2024.
*"Following the decision in 2024 to exit a number of areas"* (CEO, 2025).

### What the shareholder buys — the mix
| | Networks | CSS | Enterprise | Other |
|---|---|---|---|---|
| Share of 2025 sales | 64% | 26% | 9% | 1% |
| Summed segment EBIT 2020–2025 | **SEK 181.5bn** | SEK 0.6bn | **(SEK 68.3bn)** | (SEK 4.6bn) |
| Goodwill at 2025-12-31 | SEK 26.2bn | 3.3bn | 17.5bn | — |
| Classed here | narrow position, rebuilt each generation — **not a franchise** | none | none | none |

*Summed EBIT is arithmetic on the segment tables above (Networks 30,851 + 37,266 + 38,512 + 19,382 + 25,665 + 29,809; Enterprise
(1,935) + (2,965) + (6,234) + (38,336) + (22,083) + 3,239).*

### THE FAIR COUNTER-CASE, stated as its best advocate would state it [E4-51]
**Ericsson is the leading radio vendor outside China with 20% margins at the leading edge of 5G, 6–18 points ahead of its only
same-metric Western peer in every year since 2018 and widening; AT&T moved its radio business away from Nokia in the same period as its Open RAN agreement with Ericsson; it holds 60,000 patents
that every 5G handset pays for; the market has consolidated to two Western vendors (Nokia's own words: *"strongly favor the top
two vendors"*), the Chinese vendors are excluded from most of Ericsson's largest markets by governments that are not reversing,
and 6G is AI-native radio in which Ericsson's R&D lead compounds.** **What defeats it is criterion (2) and [E4-04], both from the
filings rather than from a view:** the customers dual-source, re-price every year without committed volumes, swap installed
networks at modernisation, and will re-tender at 6G; the margin lead is recent, arrived with a government exclusion, and was
bought with *"strategic contracts"* at the start of the generation. A position that must be re-won at every generation, in a
market *"largely flat over time"*, is a surfing run [E3-51], not a franchise.

- Class: **[x] NONE on the business as constituted** (Networks: a NARROW position, widening against Nokia, rebuilt each
  generation; CSS NONE; Enterprise NONE; the patent stream franchise-like but price-regulated and 6% of sales). Direction:
  **widening in Networks against the one same-metric peer; flat-to-narrowing for the enterprise.**
- **VERDICT: [x] OUT — on the business as constituted.** [E3-03] criterion (2) fails for Networks on Ericsson's and Nokia's
  own filings (dual sourcing, annual repricing without committed volumes or prices, network swaps at modernisation, a filed
  generation "conversion rate" below 100%), and [E4-04] excludes a moat whose basis must be replaced each generation, which the
  filing says it must be before 2030. **The entry run stops here. [E5-13]: most names should end here, and that is the system
  working.**

---
⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT. Everything below is **RECORDED, NOT GOVERNING**, and the price
block carries operator rule 3's header.

---

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business as constituted).
*Hard sequence (operator protocol 2): nothing below can reopen the file, and a strong Q3 could not have repaired Q2
[E2-37, E2-38, E3-39]. The record is kept because the operator's instruction asks every run for the whole file, and because the
filed legal record is the question the brief named.*

**STEP 1 — THE WEIGHT CASE. [x] Daily execution · [ ] Control · [ ] Leverage → BINARY GATE.**
- **Daily execution [E3-38, E3-43, E2-70]: yes.** The filing's own record is the evidence: a company that took
  *"45 critical and non-strategic contracts identified in 2017"* (FY2019 20-F), booked restructuring charges in **every
  one of the fourteen years 2012–2025** (SEK 3,447m · 4,453 · 1,456 · 5,040 · 7,567 · 8,501 · 8,015 · 798 · 1,306 · 549
  · 399 · 6,521 · 5,012 · 2,337m; FY2016, FY2019 and FY2025 20-Fs) and swung from a group operating margin of 8.8% (2015)
  to (16.9)% (2017) and from 13.7% (2021) to (7.7)% (2023). **[E3-43]: *"a business, unlike a franchise, can be killed
  by poor management"*** — and Q2 found no franchise to tolerate it.
- **Leverage [E3-29]: no** — net cash SEK 61.2bn at 2025-12-31 (Board of Directors' Report), SEK 59.8bn at 2026-06-30
  (Q2 2026 report). **Control [E1-16]: no** — a minority listed holding.

**Honesty — binary, filings-based [E5-16], each matter dated to when it became PUBLIC:**
1. **2019-12-06/07 — the FCPA resolution** (6-K 2019-12-09, `0001193125-19-308626`; FY2019 20-F): *"Ericsson has agreed
   to enter into a Deferred Prosecution Agreement (DPA) with the DOJ to resolve criminal charges relating to violation of
   bribery provision of the FCPA in Djibouti. The DPA also resolves criminal charges relating to violations of the
   accounting provisions of the FCPA in China, Djibouti, Indonesia, Kuwait, and Vietnam. In connection with the matter in
   Djibouti, Ericsson's Egyptian subsidiary pled guilty to bribery. As part of the resolution Ericsson paid a fine of USD
   520,650,432."* The SEC: *"financial sanction of USD 458,380,000, plus pre-judgement interest of USD 81,540,000"*, a
   consent judgment, and *"an independent compliance monitor for a period of three years"*. Charged in 2019 as SEK 10.7bn
   (*"SEK 10.1 billion in payments … a provision of SEK 0.6 billion"*). **The conduct: *"conduct in several countries
   between 2010 and 2016"*** (6-K 2023-03-03) — before the present CEO, who took office in 2017.
2. **2021-10-22 — first breach determination** (6-K `0001193125-21-304659`): *"Ericsson has received correspondence from
   the DOJ stating that it has determined that Ericsson breached its obligations under the DPA by failing to provide
   certain documents and factual information."* **Conduct during the DPA, under the management in place.**
3. **2022-02-15 and 2022-03-02 — Iraq, and the second determination** (6-K 2022-03-02, `0001193125-22-062245`): *"On
   March 1, 2022, the DOJ informed Ericsson that the disclosure made by the company prior to the DPA about its internal
   investigation into conduct in Iraq in the period 2011 until 2019 was insufficient. Furthermore, it determined that the
   company breached the DPA by failing to make subsequent disclosure related to the investigation post-DPA."* The same
   release concedes the order of events: *"we believe the situation described in the media reports on the conduct of
   Ericsson employees, vendors and suppliers in Iraq, going back to 2011 is covered by Ericsson's 2019 internal
   investigation"*, which *"found serious breaches of compliance rules and the Code of Business Ethics"*, and was disclosed
   publicly *"in our press release on February 15, 2022"*. **A 2019 report of serious breaches reached owners in February
   2022, after media reports, and reached the DOJ inadequately — both under the management in place.**
4. **2023-03-02 — the guilty plea** (6-K 2023-03-03, `0001193125-23-058894`): *"LM Ericsson will enter a guilty plea
   regarding previously deferred charges relating to conduct prior to 2017. In addition, Ericsson will pay a fine of
   $206,728,848."* The DOJ's own words, quoted by the company: *"[Ericsson] has significantly enhanced its compliance
   program … and has committed to continuing to implement and test further enhancements"* and *"has significantly enhanced
   its cooperation and information sharing efforts."* The monitorship was extended to four years and **concluded in June
   2024**: *"In June 2024, Ericsson concluded its four-year compliance Monitorship … The Monitor's certification and the
   conclusion of the Monitor team's work and term was an important milestone"* (FY2024 20-F). The Chief Legal Officer who
   signed the 2021 and 2022 releases, Xavier Dedullen, *"resigned from this role"* on 2022-03-21 (FY2021 20-F).
5. **2023 — disclosure reviews closed in the owner's favour** (FY2023 20-F): *"On May 24, 2023, Nasdaq Stockholm concluded
   its review … and dismissed the matter"*; *"the Swedish Financial Supervisory Authority also decided to formally close its
   review"*; US shareholder litigation *"was dismissed with prejudice … This shareholder suit is being appealed"*.
6. **Still open at the FY2025 20-F:** the DOJ's Iraq investigation (*"it is expected that there will not be any conclusive
   determinations on the outcome until the investigation is completed. The scope and duration of the investigation remain
   uncertain"*); three US Anti-Terrorism Act suits (filed August 2022, February 2024, November 2025) that name *"President and
   CEO Börje Ekholm"* as a defendant; 93 claimants in Solna District Court on *"alleged inadequate disclosure of the contents
   of the Company's 2019 internal Iraq investigation report"*; China SAMR's patent-licensing investigation (since April
   2019); and **the Vonage National Security Agreement** (July 2022): *"Vonage and Ericsson continue to cooperate with the
   CFIUS monitoring agencies in investigating historical and ongoing compliance with the terms of the National Security
   Agreement. The ultimate outcome of these investigations remains uncertain."* The SEC's June 2022 Iraq investigation is
   described in the FY2023 20-F; **no instance of it was found in the FY2024 or FY2025 20-F texts** (sweep: `kw.py` for
   "SEC" within 80 characters of "Iraq", both documents) — its status is not stated, and nothing is inferred.
7. **Succession:** 6-K 2026-06-16 (`0001193125-26-272235`): *"Börje Ekholm to step down on September 30, 2026"*, succeeded
   by *"Per Narvinger, currently Executive Vice President and Head of Business Area Networks"* — an internal successor.
- **The read, and the hesitation written down.** Items 1 and 4 concern conduct of 2010–2016 whose actors [E2-57] are
  largely gone. **Items 2 and 3 are the sharpest record in this file, because they are conduct of the management in place
  across an information asymmetry [E2-68]**: the company held a 2019 report of *"serious breaches"*, and the filed DOJ
  determinations say it did not put it *"face up on the table"* for the agency it had contracted to inform; owners learned
  of it after the press. [E5-22]: *"But the main problem was they didn't act when they learned about it"* — the company did act
  internally (*"several employees were exited"*, 6-K 2022-03-02) and did not act outward. Against that, the only
  authorities that have ruled on the owner-facing disclosure (Nasdaq Stockholm, the Swedish FSA, a US district court)
  ruled for the company, the DOJ credited its cooperation, and the monitor certified. **What would decide the binary is
  not on the record yet:** the DOJ's conclusion of the Iraq investigation, the ATA court's ruling on the motions to dismiss
  that name the CEO, and the CFIUS agencies' NSA findings. Those documents do not yet exist.

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E2-49, E2-57, E3-53].** *Each a prompt to read, never a verdict.*
- [x] **weak accounting — the cockroach prompt [E4-22]:** the compliance history above is the corpus's *"seldom just one
  cockroach"* in its accounting-provision form — the DPA resolved *"violations of the accounting provisions of the FCPA"* in
  five countries. Pensions: the Swedish obligation is discounted on government-bond yields; the filing itself quantifies the
  softer alternative and does not use it (*"If the discount rate had been based on Swedish covered mortgage bonds, the
  liability … would have been approximately SEK 10.9 billion, which is SEK 7.7 billion lower"*) — **a deviation toward the
  conservative, recorded in the company's favour [E2-69].** SBC is expensed.
- [ ] **unintelligible footnotes** — no: segment, goodwill-headroom (*"exceeds the carrying amount by SEK 2.7 billion"*),
  provisions and customer-finance notes are legible and quantified. **Positive pole of [E2-26].**
- [x] **trumpeted projections [E4-22, E3-48, E5-30] — the record, from the filings:** (a) *"reach an operating margin of at
  least 10% in 2020, excluding restructuring charges"* (FY2019) → **12.0% reported EBIT, met**; (b) *"The key financial
  target for 2022 is to reach an operating margin of 12–14% excluding restructuring charges"* (FY2019) → **10.1%, missed**,
  and reported as met by exclusion (item [E2-57] below); (c) *"In November 2020, we presented a long-term profitability target
  of 15–18% EBITA margin excluding restructuring charges"*, with *"our ambition is to reach the long-term target no later
  than in 2 to 3 years"* (FY2021) and *"reach the lower end of our long-term EBITA target of 15–18% by 2024"* (FY2022) →
  **8.1% in 2023, 11.0% in 2024 — missed**; 2025 *"adjusted EBITA margin of 18.1%"*, **14.9% without the iconectiv gain**,
  which the Chair calls *"tracking very close"*. One met, two missed.
- [ ] **serial share issuance [E5-15]** — no: issued shares 3,344,151,735 (2024-01-01) → 3,371,351,735, only LTV C-shares
  converted to treasury; outstanding falling under the SEK 15bn buyback.
- [x] **adjusted-earnings promotion [E4-29, E2-57, E3-53, E5-33] — fires, in the restructuring form, not the EBITDA form.**
  **"EBITDA" appears zero times** in the FY2025 annual report and in the Q4 2025, Q1 2026 and Q2 2026 reports (count by
  `grep`, the CGNX companion rule discharged); **"adjusted" appears 101, 158, 128 and 132 times.** Every headline, every
  long-term target and the LTV profitability condition exclude restructuring charges (*"Adjusted metrics are adjusted to
  exclude restructuring charges"*, Q2 2026), and restructuring has recurred in **every year for fourteen years, SEK 55.4bn in
  sum 2012–2025**, plus SEK 4.4bn in H1 2026. [E5-33]: *"to tell owners year after year, 'Don't count this' … is
  misleading."* **The except-for form fired in 2022:** *"Excluding Vonage and previously announced charges of SEK -5.5 billion
  during the year, EBIT margin was 12.9%, reaching the 2022 target of 12–14%"* — against a reported 10.0% [E2-57].
- [x] **metric-switching [E2-49] — weak.** The group yardstick moved from *operating margin* (the 2020 and 2022 targets) to
  *EBITA margin excluding restructuring* in November 2020 — **announced ahead, in the same month as the Cradlepoint
  acquisition and before Vonage**; the new yardstick excludes the group's acquired-intangible amortisation, which rose from SEK 1,164m
  (2021) to 1,991m (2022) and 3,321m (2023) after Vonage (Note H3). Announced ahead with the growth plan, not after deterioration: a weak fire, recorded.
- [ ] **filed-figure fraud tells [E4-30]** — no: taxes paid SEK 7,009m on SEK 38,302m pre-tax (18.3%) in 2025 and 6,304m on
  2,589m (a loss year after impairments) in 2024; reported growth is anything but smooth.
- [x] **the restructuring charge [E3-53]** — as above; **kept inside the owner-earnings mean at Q4**, never annualised away.

**STEP 3 — THE PRIMARY TEST [E2-01], balance sheet first.** Return on total equity, from filed net income and total equity (income statements; balance sheets, 2020–2025): **2021 23.9% · 2022 15.9% · 2023 (22.6)% · 2024 0.4% · 2025 28.3%** (28,714 on average equity of SEK 101.6bn, **the SEK 7.6bn iconectiv gain inside**). The company's own *"Return on capital employed"* (EBIT
on a capital base that includes gross cash): 2012 6.7% · 2013 10.7% · 2014 9.8% · 2015 11.6% · 2016 3.2% · 2017 (20.4)% ·
2018 0.8% · 2019 6.7% · 2020 17.0% · 2021 18.9% · 2022 13.9% · 2023 (10.8)% · 2024 2.6% · 2025 24.1% (FY2016, FY2019,
FY2022, FY2025 APM tables; definitions updated in 2025 and prior periods restated). **Fourteen years, mean about 6.8%, and
never two consecutive years above 15% except 2020–2021.** **Book equity SEK 147.4bn (2015) → 110.3bn (2025)** while SEK
72.7bn of dividends were paid 2016–2025 against cumulative net income of about SEK 27bn (SEK 27,725m on the as-first-filed 2016 figure of 1,895m; 26,842m on the restated 1,012m) (filed income statements) —
**the dividend was paid out of equity across the decade**, a point for [E2-60] at Q4.
- **[E2-43] denominator, for an acquisitive filer:** equity 110.3bn less goodwill 46.9bn and other intangibles 9.5bn =
  tangible equity **53.9bn**, less net cash 61.2bn = **operating tangible equity of about minus SEK 7bn** — the business runs
  on customer and supplier money (contract liabilities 36.9bn, trade payables 26.3bn, of which 9.6bn in a *"supplier payment
  program"* on terms to 180 days). The tangible-capital return is not a meaningful number; **the capital the business
  consumes is expensed R&D** (SEK 48.9bn in 2025, 20.6% of sales), which no balance-sheet return sees.
- **[E2-56] camouflage by segment:** Networks earned 11.3–22.2% EBIT across 2020–2025 while CSS lost money in five of six
  years and Enterprise lost SEK 71.6bn of EBIT across 2020–2024 (the 2023 and 2024 Vonage impairments inside) — the consolidated series
  averages a good radio business with a decade of poor adjacent capital allocation.

**The half-owner test [E2-26]:** mixed. The statements pass (impairments, goodwill headroom, customer-finance exposure,
supplier-finance program, the covered-bond pension alternative — all quantified). **The Iraq sequence fails it**: the owner
would have wanted to know in 2019 what the owner learned in 2022. **Candor's positive pole on acquisitions [E4-39]:** the
filings do revisit Vonage in numbers — two impairments, the CGU headroom, and the Chair's *"These trends have also
significantly impacted the market capitalization of Vonage's publicly traded peers"* (FY2023) — which is a post-mortem in
figures, if not in words.

**The institutional imperative — [E2-30], scored:**
- [ ] resists change in current direction — **not ticked**: the company exited contracts (2017–2019), exited the
  managed-services and IoT lines, sold iconectiv, cut headcount 94,236 → 88,826 in 2025 and wrote Vonage down twice.
- [x] **projects soak up available funds** — the enterprise push: Cradlepoint (*"Purchase price paid on acquisition … 9,534"*,
  2020), Vonage (SEK 53.3bn plus 5.9bn of debt repaid, 2022), Aduna, Ericom; **SEK 71.6bn of cumulative Enterprise EBIT losses
  2020–2024**, against the net cash the Networks leg generated.
- [ ] staff studies to justify a craving — not observable from the filings.
- [x] **peer behaviour imitated** — weak: the filings frame the enterprise and API push as the industry's direction
  (*"new business models are needed for the telecom industry"*, FY2025 strategy); not proven as imitation from the filing.

**Capital allocation — the buyback conditions [E5-08, E4-31, E5-24]:**
- **Scale:** SEK 15bn authorised (6-K 2026-04-16); **70,349,695 B shares bought for SEK 7,299.1m at an average SEK 103.75**,
  2026-04-23 to 2026-09-04 (weekly 6-Ks, `bb.py`). Dividends SEK 9.5bn paid in 2025, SEK 10.1bn proposed for 2026.
- **(1) ample funds:** yes on the balance sheet — net cash SEK 59.8bn at 2026-06-30.
- **(2) material discount to IV, conservatively calculated:** **not established.** At SEK 103.75 × 3,300M average shares
  the purchases paid about SEK 342bn for the company; this run's owner earnings (Q4) are SEK 15.7bn (ten-year) to 23.9bn
  (five-year) — **a 4.6–7.0% yield, below the ~10% floor [E4-28] on every window.** **CAPITAL ALLOCATION FLAG**, with the
  humility clause [E4-13]: it rests on this run's range, and management knows the business better. Binds position size,
  never the rate.
- **(3) owners supplied the information [E4-31]:** passes on the present disclosure; the Board states its principles
  (*"(4) ensure capital discipline through distributing excess cash to shareholders"*) though, unlike Berkshire's [E5-25],
  it publishes no intrinsic-value basis for the price it pays.
- **The Vonage deal against [E5-24]:** SEK 59bn paid for a business whose own pro-forma 2022 figures were *"SEK 14.4 billion
  and SEK – 3.0 billion"* of sales and EBIT; SEK 46.6bn written off within two years. *"What is smart at one price is dumb
  at another."*

**Pay and what it vests on [E4-27]** (Remuneration Report 2025; Note G3): STV for the CEO on **Economic Profit** — *"Group
EBITA excluding restructuring charges, less cost of capital on invested capital"* — 25% Group and 25% for each of three
business areas; **2025 outcome SEK 22,373,471, "183.09% against all target performance measures"** on a fixed salary of SEK
18,799,636. The Enterprise economic-profit range was a loss range (*"–6.1 | –5.1 | –4.3"* BSEK threshold/target/maximum),
paid at 200%. LTV: 45% three-year EBITA (*"Excludes restructuring charges and items not included in target performance
criterion"*), 25% absolute TSR 6–14%, 20% relative TSR, 10% ESG. **What it vests on: a capital charge (a credit), but on earnings that exclude a restructuring charge incurred every
year, and in 2025 on a year carrying a SEK 7.6bn disposal gain whose treatment in "Economic Profit" the report does not
state.** LTV 2023 vested at 91.23% (the EBITA leg at 0%); LTV 2022 at 92.72%, with both TSR legs at 0%.

**Flags that converge [E4-52]:** targets set, missed and restated + restructuring excluded from every headline and pay
metric for fourteen years + an except-for claim of a missed target + adjacent acquisitions that soaked up the radio
business's cash + a candor failure toward the DOJ on the Iraq report **all point the same way: toward presenting the
company as on plan and the costs as one-off.** A reinforcing system, not a fraud finding ([E2-30]: *"Institutional
dynamics, not venality or stupidity"*).

**THE GUARDRAIL**
- [x] Nothing in this Q3 promotes the name.
- [x] Key-person dependence: recorded at Q2.
- [x] No great-manager case is made; the CEO leaves on 2026-09-30.

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE** → **on the honesty binary.**
  *Can I name the document that would resolve it?* The documents that would decide it — the DOJ's conclusion of the Iraq
  investigation, the District of Columbia ruling on the ATA motions that name the CEO, and the CFIUS agencies' findings on the
  National Security Agreement — **do not yet exist**; every existing filing has been read. **An OUT is not written**: the
  2010–2016 bribery's actors are largely gone [E2-57], the non-criminal DPA breaches of 2021–2022 were resolved by plea with the
  DOJ crediting enhanced cooperation, and the owner-facing disclosure reviews closed for the company. **An IN is not written
  either**: the management in place held a 2019 report of *"serious breaches"* that owners received after the press and the DOJ
  found inadequately disclosed to it [E2-68], and three proceedings bearing on that conduct are open. **The rationality read,
  separately, carries a live capital-allocation flag** (Vonage at SEK 59bn, SEK 46.6bn written off; buybacks at a 4.6–7.0%
  owner-earnings yield) and converging flags [E4-52]. *[E5-17]: "Sincerity and empathy can easily be faked" — no Q3 verdict here
  is a finding that the managers are honest.*

## Q4 — WILL IT SURVIVE?

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business as constituted).
*Built in full because Q5's computation needs the number and the operator asked for the record.*

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its long-term competitive
> position and its unit volume. (… the working capital **increment also should be included in (c)**.)" … "**(c) must be
> a guess**."

**Construction, every line disclosed (CONVENTION: OCF less SBC less the (c) guess, per the framework's Section VI).**
Computation: `_research 2026-09-13 ERIC/oe.py` → `oe_out.json`; SEK million.
1. **Start: consolidated cash flow from operating activities**, as filed: FY2013 20-F (`0001193125-14-134810`) for
   2011–2013, FY2016 (`0001193125-17-139501`) for 2014–2016, FY2019 (`0001193125-20-078974`) for 2017–2019, FY2022
   (`0001193125-23-071310`) for 2020–2022, FY2025 (`0001193125-26-104149`) for 2023–2025. It nets the working-capital
   change from one audited line, so constraint 3 is met by construction. **OCF and PP&E capex for every year 2015–2025, and product development for 2019–2025, match companyfacts to the
   million** (`cf_series.json`).
2. **Less lease repayments from 2019** (*"Repayment of lease liabilities"*, SEK 2,115–2,990m a year): under IFRS 16 these
   left OCF; before 2019 they were inside it. *(CONVENTION, the HMC rule: without it the post-2019 years rise ~SEK 2.5bn.)*
3. **Less SBC, in full [E5-06] — RESOLVED and COMPLETE for all fifteen years.** Two kinds are filed. **Cash-settled**
   plans (Key Contributor, EPP; SEK 1,610m of expense in 2025) are paid in cash and accrued as provisions, so their cash
   is already inside OCF through the provisions line — subtracting them again would double-count. **Share-settled** plans
   are the non-cash add-back and are subtracted: 2011 413 · 2012 405 · 2013 388 · 2014 717 · 2015 865 · 2016 957 · 2017
   885 · 2018 678 · 2019 375 · 2020 149 · 2021 93 · 2022 89 · 2023 82 · 2024 93 · 2025 175 (Note G3/C28 of each 20-F:
   e.g. *"Total compensation costs charged during 2015: SEK 865 million, 2014: SEK 717 million"*; 2017 = legacy plans
   875.5 + ET LTV 9.9; 2018 = 644.9 + 32.6; 2019 = 317.4 + 58.0; 2020 = 65.6 + 83). **[E3-70]'s market-value measure:**
   the share-settled charge is itself grant-date fair value (*"calculated based on the fair value (FV) at grant date"*,
   Note G3) and 0.3–9.2% of OCF (the high in 2017); no option programme exists. Stated, not stretched.
4. **Less (c)**, the disclosed judgment below. **Capitalised development** (*"Product development"*, the investing line,
   SEK 817–4,483m) **is inside the capex end; its amortisation is inside the D&A end.** **Amortisation of acquired
   intangibles** (customer relationships, IPR; SEK 1,019–4,521m) **is outside both** — it is the expensing of acquisition
   prices, and the acquisitions are shown on their own line so they cannot be hidden by the choice. **Expensed R&D —
   SEK 48.9bn in 2025, 20.6% of sales — sits inside OCF in full**; that is where this business actually spends to *"fully
   maintain its long-term competitive position"*, and it is counted as a cost, never added back.

| Year | OCF | ops net assets change (inside OCF) | lease repay. | SBC (share) | capex PP&E + cap. dev. | PP&E dep. + cap.-dev. amort. | **OE, (c) = capex** | OE, (c) = D&A | acquisitions less divestments |
|---|---|---|---|---|---|---|---|---|---|
| 2011 | 9,982 | (15,200) | — | 413 | 6,509 | 4,494 | **3,060** | 5,075 | 3,128 |
| 2012 | 22,031 | 3,016 | — | 405 | 7,070 | 5,110 | **14,556** | 16,516 | 2,077 |
| 2013 | 17,389 | (4,613) | — | 388 | 5,418 | 5,634 | **11,583** | 11,367 | 2,682 |
| 2014 | 18,702 | (3,641) | — | 717 | 6,845 | 5,599 | **11,140** | 12,386 | 4,394 |
| 2015 | 20,597 | (3,687) | — | 865 | 11,640 | 6,084 | **8,092** | 13,648 | 2,200 |
| 2016 | 14,010 | 6,003 | — | 957 | 10,612 | 6,236 | **2,441** | 6,817 | 622 |
| 2017 | 9,601 | 22,710 | — | 885 | 5,321 | 6,784 | **3,395** | 1,932 | (276) |
| 2018 | 9,342 | 7,788 | — | 678 | 4,900 | 5,834 | **3,764** | 2,830 | 1,285 |
| 2019 | 16,873 | 2,807 | 2,990 | 375 | 6,663 | 5,106 | **6,845** | 8,402 | 1,505 |
| 2020 | 28,933 | (3,637) | 2,417 | 149 | 5,310 | 4,508 | **21,057** | 21,859 | 9,598 |
| 2021 | 39,065 | 4,002 | 2,368 | 93 | 4,625 | 5,017 | **31,979** | 31,587 | (59) |
| 2022 | 30,863 | 619 | 2,593 | 89 | 6,197 | 5,700 | **21,984** | 22,481 | 51,688 |
| 2023 | 7,177 | (11,999) | 2,857 | 82 | 5,470 | 5,409 | **(1,232)** | (1,171) | 2,140 |
| 2024 | 46,261 | 22,817 | 2,492 | 93 | 3,640 | 5,341 | **40,036** | 38,335 | 311 |
| 2025 | 32,954 | 378 | 2,115 | 175 | 3,768 | 5,037 | **26,896** | 25,627 | (10,539) |

*Acquisitions less divestments: cash lines "Acquisitions of subsidiaries and other operations" less "Divestments of
subsidiaries and other operations"; 2022 is Vonage (purchase price SEK 51,297m); 2025 includes iconectiv (SEK 11,200m
proceeds). Vonage's SEK 5.9bn of debt repaid sits in financing and is not in this column.*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25, E4-38]:**
| window | OE, (c) = capex | OE, (c) = D&A | lower of the two | ops-net-asset release per year inside it | lower end, release removed [E4-41] | capex ÷ D&A |
|---|---|---|---|---|---|---|
| 3-yr 2023–25 | 21,900 | 20,930 | 20,930 | +3,732 | 17,198 | 0.82 |
| **5-yr 2021–25 (default [E2-42])** | **23,933** | 23,372 | **23,372** | +3,163 | **20,208** | 0.89 |
| 10-yr 2016–25 | 15,716 | 15,870 | 15,716 | +5,149 | **10,568** | 1.03 |
| 15-yr 2011–25 | 13,706 | 14,513 | 13,706 | +1,824 | 11,882 | 1.15 |
| 5-yr 2016–20 (the last generation trough) | 7,500 | 8,368 | 7,500 | +7,134 | 366 | 1.15 |

- **Spread, conservative end:** on the lower-of-(c) figure the windows run **SEK 13.7bn (15-yr) to 23.4bn (5-yr)**, the
  conservative end **41% below** the high; with the working-capital releases removed, **SEK 10.6bn (10-yr) to 20.2bn
  (5-yr)**, 48% below.
- **Combined range (window × (c) × working-capital normalisation): SEK ~10.6bn to ~23.9bn.** The trough window 2016–20
  (SEK 7.5bn as filed, ~0.4bn without its releases) is shown and not used as an end, because it is one leg of a cycle, not a
  mean across one.
- **Is that range too wide to reach a conclusion?** **On value: no conclusion that helps a buyer — both ends capitalise below
  the floor (Q5).** On survival it is not needed: every window is positive and the balance sheet carries the worst year.
- **The distorted years, named [E5-11, E4-41]:** **2017** (an operating loss of SEK 34.7bn with SEK 22.7bn of operating net
  assets released as the company *"addressed"* the 45 contracts); **2019** (SEK 10.1bn paid to the DOJ and SEC, inside OCF,
  a real cost [E5-33] and kept); **2023–2024** (a SEK 12.0bn working-capital build then a SEK 22.8bn release — the 3-year
  window pairs them, the 5-year does not fully); **2021–2022** (the North American 5G build, Networks EBIT margin 22.2% and
  19.9%). **[E4-41] normalises down for luck:** **across 2016–2025 operating net assets released SEK 51.5bn, about SEK 5.1bn a
  year, on sales that moved between SEK 205.4bn and 271.5bn and ended the decade at 236.7bn against 222.6bn** — a release that cannot recur on flat sales.
  That is why the release-removed column governs the low end.
- **Owner earnings by year:** the table above.
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT. Which case, and why: the DEFAULT [E3-44, E2-41] applies,
  and the exception class [E5-20] does not, on Ericsson's own filing.** Capital expenditure is *"normally approximately 1–2%
  of sales"* (Board of Directors' Report); PP&E plus capitalised development ran **1.15x their depreciation and amortisation
  over fifteen years and 1.03x over ten**, and the two ends of (c) differ by **1–6% on every window**. Nothing in the filing
  says depreciation understates renewal. **One direction is recorded against the default:** capex fell to **0.82x D&A over
  2023–25** while headcount fell (94,236 → 88,826 in 2025) and the filing plans *"a proposed headcount reduction in Sweden …
  Approximately 1,600 positions"* (20-F Item 8.B, announced 2026-01-15) — a harvest signal, so the D&A end, not the capex end, is
  the honest one for the recent windows, and the table takes the lower of the two throughout. **Band used: the lower of the
  two ends per window; the working-capital release removed at the low end.**
- **The real maintenance spend is the R&D line, and it is already charged:** SEK 34.8bn (2015) → 48.9bn (2025) (Note
  B3/companyfacts `ResearchAndDevelopmentExpense`, filed income statements). *"Maintain technology leadership … through
  continued investments in R&D, even during periods of increased market volatility or low visibility"* is capital-allocation
  principle (1) — the first claim on the cash, before dividends.
- **Stock compensation subtracted in full [E5-06]:** share-settled, every year resolved; cash-settled already in OCF (item 3).
- *If the capex band changes the verdict → UNKNOWABLE:* it does not; the two ends are within 6%.
- **Look-through [E3-04]:** associates are immaterial (share of earnings SEK 54m, 2025). **Not applied.**
- **Acquisitions, displayed and not netted:** over 2016–2025 owner earnings summed **SEK 157.2bn**; dividends paid **SEK
  72.7bn**; acquisitions less divestments **SEK 56.4bn** — Cradlepoint (SEK 9.5bn) and Vonage (SEK 51.3bn plus SEK 5.9bn
  of debt repaid) — of which **SEK 46.6bn was written off** (Note C1, 2023 and 2024). SEK 157.2bn less 72.7bn less 56.4bn leaves **SEK 28.1bn** retained in cash over the decade; **the acquisitions took
  three-quarters as much as the dividends, and 81% of what Vonage cost has been written off** (SEK 46.6bn of the SEK 57.2bn paid for Vonage and its debt).

### Great, good, or gruesome? **[E4-20]**
- [ ] great
- [x] **good — for the Networks leg, in its good generations, and no better:** Networks earned 16.0–22.2% EBIT in 2019–2022
  and 2025, on almost no tangible capital (the group's operating tangible equity is **about minus SEK 7bn**: tangible equity
  SEK 53.9bn less net cash SEK 61.2bn) — but it earned **7.9% (2017) and 11.3% (2023)** in the troughs, and its generation
  race is paid for through an expensed R&D line of ~20% of sales that never stops.
- [x] **gruesome — the enterprise leg:** SEK 59bn into Vonage and SEK 9.5bn into Cradlepoint, **SEK 71.6bn of Enterprise
  EBIT losses 2020–2024**, and a segment that made money in 2025 only by selling iconectiv.
- **As constituted:** ten-year owner earnings of SEK 15.7bn on a market value of SEK 322bn, with **SEK 72.7bn of dividends paid
  over the decade against about SEK 27bn of net income and book equity down from SEK 147.4bn to 110.3bn** — [E4-43]'s *good*
  class does not rescue it at the group level, because the cash the enterprise leg consumed did not *"earn a reasonable
  return"*.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — large in good years, NOT reliable.** Owner earnings from **(SEK 1.2bn)
  (2023) to SEK 40.0bn (2024)**; group operating margin from **(16.9)% (2017) to 16.3% (2025)**; the FY2023 20-F: *"the RAN
  market has been largely flat over time but with cyclicality"*.
- **(2) massive liquid assets — yes.** Gross cash **SEK 93.9bn** at 2025-12-31 (cash 43.9bn; interest-bearing securities
  37.3bn non-current and 12.7bn current, of which *"Governments | AAA"* 15.9bn and *"Mortgage institutes | AAA"* 31.6bn, Note
  F1), against borrowings **SEK 32.7bn** → net cash **SEK 61.2bn**; SEK 59.8bn at 2026-06-30 after SEK 8.2bn of Q2 returns.
  Unused committed facilities USD 2.5bn; *"There are no financial covenants related to these programs."*
- **(3) no significant near-term cash requirements — NOT clean; covered.** Filed and dated (Note D4): debt due *"<1 year | 4.0"*
  and *"1–3 years | 18.0"* SEK bn (the EUR 750m 2027 and EUR 500m 2028 bonds); purchase obligations **SEK 22.1bn <1 year**
  (*"primarily relating to contractual commitments for supply chain resilience"*, up from 18.7bn); **commitments for customer
  finance SEK 32.9bn <1 year, 55.9bn in all** (*"Most of such financing arrangements have been transferred to banks"* — the
  exposure is the bank market's appetite, [E5-39]'s *"kindness of strangers"*); a **supplier payment program of SEK 9.6bn** on
  terms to 180 days whose *"appetite for sale and purchase of invoices by financial institutions may be affected by current
  market conditions"*; the SEK 10.1bn dividend and ~SEK 7.7bn of the buyback still to run; **the Swedish pension deficit SEK
  12.6bn** (*"There are no funding requirements for the Swedish plans"*; a business mortgage of SEK 7.4bn pledged to PRI
  Pensionsgaranti); and **unquantified legal exposure** — the DOJ Iraq investigation, three ATA suits, 93 Solna claimants,
  CFIUS NSA enforcement (*"can result in an enforcement action imposing monetary penalties … which can be material"*).
  **Scored: covered by strength (2), not absent.**
- **Leverage, named and quantified [E4-16, E3-29, E2-54]:** net cash; interest paid SEK 2,205m (2025) against five-year owner
  earnings after capex of SEK 23.9bn — **comfortably met [E2-54]**. Ratings *"BBB–, stable"* (S&P, Fitch) and *"Ba1, positive"*
  (Moody's) — **one agency rates it below investment grade.** The parent's bonds and EIB/NIB loans carry no financial
  covenants; the customer-finance and supplier-finance programs are the covenant-like exposure, set by banks' appetite.
- **Jurisdiction [E3-66]:** a Swedish company whose votes are controlled by two holding companies with 12.5% of the capital
  (Investor AB 24.8% of votes, Industrivärden 15.0%), both represented on the Nomination Committee (6-K 2026-05-29) and
  Investor's chair on the Board. **Where the public owner stands:** after R&D (*"principle (1)"*), the dividend (*"(2)
  stable to progressive"*), and *"(3) selective inorganic investments"* — distribution of *"excess cash"* is fourth. The ADS
  holder also bears *"A Swedish dividend withholding tax at a rate of 30%"*, reduced to 15% under the US treaty (Item 10.E).

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**
- **The mechanism — TM's PASS-THROUGH (the eleventh registered shape), in an expensed-R&D form, with SONY's CAMOUFLAGE (the
  tenth) in its enterprise leg. No new shape.** Not ORCL's, ARM's, BE's, BA's, SWK's, ACVA/FLNC/NEGG's, CNR's, RGTI's, BAM's
  WAREHOUSE or TSM's ADDRESS. **The company does not die; the owner's return does.** A radio vendor must re-win its customers'
  networks at each generation and each regional tender, spending ~20% of sales on R&D every year to stay on the short list,
  in a market *"largely flat over time"*, selling to buyers who hold the leverage (*"the 10 largest customers accounted for
  46 %"*; agreements that *"may include commitments to future price reductions"*; *"continuous price pressure"*) — so its
  cost savings are passed to the operators [E3-62] and its peers' investment decisions neutralise its own [E2-27]. **TM
  spends capex to hold units; Ericsson spends R&D to hold share; in both, the savings do not stay home.** And the good
  generations' cash went, in part, into a leg that must win a different race and has not (Vonage) — the consolidated series
  hides that rate [E2-56].
- **Quantified from filed figures [E3-24]:** the last trough is on the record. **2016–2020 owner earnings averaged SEK 7.5bn a
  year as filed, and about SEK 0.4bn once that window's SEK 35.7bn of working-capital releases are removed**, while the group
  took SEK 24.1bn of restructuring charges (2016–2018) and cut the cash dividend (filed dividends paid SEK 12,263m in 2016 →
  3,424m in 2017 → 3,425m in 2018). **A repeat of that window at today's price is a 2.3% yield
  as filed — below the SEK sovereign.** A tail case for the lender-like exposures, [E3-24]'s own arithmetic: if 10% of the
  SEK 55.9bn customer-finance commitments were funded onto the balance sheet and lost 30%, the loss would be **SEK 1.7bn**, 1.5%
  of equity — **survivable**; the supplier-payment program withdrawn in full would take **SEK 9.6bn** of cash, covered by gross
  cash almost ten times. Exposure, not experience [E4-40]: a legal outcome on Iraq or the NSA is the one tail the filing cannot
  size.
- **Likelihood:** insolvency — **a low-level possibility** on the filed balance sheet; **the pass-through — likely**: it is the
  filed record of 2011–2025 — a group operating margin at or above 12% in only three of fifteen years (2020 12.0%, 2021
  13.7%, 2025 16.3% with the iconectiv gain inside), and below 5% in seven (2012, 2016, 2017, 2018, 2019, 2023, 2024) — and the
  company's own statement that the RAN market is flat with cyclicality.
- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on survival** — it survives: strength (2) is ample, (3) is covered by it, and (1)
  is large in good years if unreliable. **The named death is the owner's return, not the company** — TM's PASS-THROUGH in an
  expensed-R&D form, with SONY's CAMOUFLAGE in the enterprise leg; **no new shape; the register stays at twelve.**

⛔ **Q5 does not open for entry.** Q1 IN · **Q2 OUT**. Q3 and Q4 are recorded above, not governing. Everything
below carries operator rule 3's header and no entry language.

---
## COMPUTATION — NOT A CLEARANCE

### THE PRICE AND THE PASS/FAIL LINE (the operator's instruction of 2026-09-01)
- **Price: SEK 98.66** (ERIC-B.ST close 2026-09-11, Yahoo — aggregator, live quote only, flagged; ERIC-A.ST SEK 99.00). ADR
  **$10.31** (same date, same flag), **1 ADS = 1 Class B share** (20-F cover); at the Riksbank fixing of USD/SEK 9.69401 the
  ADR is SEK 99.95.
- **Shares: 3,265,683,059** — issued 3,371,351,735 (A 261,755,983 + B 3,109,595,752) less treasury 105,668,676 B shares at
  2026-09-04 (6-K filed 2026-09-08, `0001628280-26-060848`). **A and B share economics equally** (Exhibit 2.3; Note E1) and are
  summed; the 20-F cover's 3,371,351,735 (accession `0001193125-26-104149`) is the issued count, not outstanding.
- **Market cap: SEK 322.2bn.** Sovereign: **Swedish Government Bond 10-year 3.227%, Sveriges Riksbank (SWEA `SEGVB10YC`),
  2026-09-11** — the longest tenor published as a daily yield is 10 years; the Debt Office's SGB 1068 (2037) auctioned at
  3.0909% on 2026-09-09.
- **PASS/FAIL: FAIL — the file closed at Q2, OUT on the business as constituted** (Q1 IN; Q2 OUT; Q3 UNKNOWABLE and Q4 IN
  recorded, not governing).

### What the buyer is paying for, in words
**The leading Western radio vendor at the top of a 5G margin cycle, with a patent-licence stream, SEK 61bn of net cash and a
buyback running — and a business that must re-win its customers at 6G, has spent the last decade's surplus on an enterprise
leg mostly written off, and has earned owner earnings of SEK 13.7–15.7bn a year over ten and fifteen years.** At SEK 98.66 the
market pays **13.5 times the best five-year owner earnings on record (SEK 23.9bn, 2021–25)** and **20.5 times the ten-year mean
(SEK 15.7bn)**. The price assumes that 2021–2025 — the North American 5G build, a SEK 22.8bn working-capital release in 2024, and
a Networks margin 6–18 points above Nokia's — is the level, not the crest.

### 1. THE YIELD
| Owner earnings (Q4) | ÷ cap SEK 322.2bn | per share | points over SEK 10Y 3.227% |
|---|---|---|---|
| **5-yr 2021–25, (c) = capex, as filed — the high end: SEK 23.9bn** | **7.43%** | SEK 7.33 | **+4.2** |
| 5-yr, lower of (c): SEK 23.4bn | 7.25% | SEK 7.16 | +4.0 |
| 5-yr, working-capital release removed: SEK 20.2bn | 6.27% | SEK 6.19 | +3.0 |
| 10-yr 2016–25: SEK 15.7bn | 4.88% | SEK 4.81 | +1.7 |
| 15-yr 2011–25: SEK 13.7bn | 4.25% | SEK 4.20 | +1.0 |
| **10-yr, working-capital release removed — the conservative end: SEK 10.6bn** | **3.28%** | SEK 3.24 | **+0.1** |

*Not netted, and why:* net cash SEK 61.2bn (SEK 18.74 a share) is claimed in writing by the capital-allocation order — R&D
*"even during periods of … low visibility"*, the SEK 10.1bn dividend, the ~SEK 7.7bn of buyback still to run — and sits beside a
SEK 12.6bn Swedish pension deficit, SEK 55.9bn of customer-finance commitments and unquantified legal exposure. **Netted, the
yields would be 4.1% to 9.2% — still below the floor at every end.**

### 2. WHAT THE PRICE ALREADY ASSUMES
- **Perpetual growth needed for a ~10% expectancy** (yield + growth, the engine [E3-34], casting no vote): **2.6%** on the
  best five-year figure; **5.1%** on the ten-year; **6.7%** on the ten-year with the working-capital release removed.
- **What the business has actually done:** group sales **SEK 226.9bn (2011) → 236.7bn (2025), 0.3% a year in nominal kronor**;
  Networks sales SEK 166.0bn (2020) → 151.0bn (2025); owner earnings **no usable growth rate** (SEK 3.1bn 2011, 2.4bn 2016,
  32.0bn 2021, (1.2)bn 2023, 40.0bn 2024, 26.9bn 2025). The filing's own market description: *"largely flat over time but with
  cyclicality"*.
- **[E4-35]'s base rate:** the requirement is 2.6–6.7% a year for ever, on a record of 0.3% — **[E4-44] caps value growth at
  earnings growth, and the earnings have not grown across two generations.** **What bounds the upside [E2-63]:** the 6G tender
  (*"expected to begin before 2030"*), North American operator capex, whether the Chinese-vendor restrictions hold, IPR renewals,
  and whether Enterprise stops consuming cash.

### 3. WHAT YOU ARE PAID
**+0.1 to +4.2 points over the SEK 10-year bond** on the owner-earnings range; **against the USD 30-year (5.35%), −2.1 to +2.1.**
No per-name premium was added to the rate [E3-42].

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01] — engine display, no vote
- Capitalised at the ~10% floor **with no growth**: **roughly SEK 30 to SEK 75 a share** on owner earnings (SEK 10.6–23.9bn);
  **roughly SEK 50 to SEK 90** with the net cash added.
- At the floor **with 3% perpetual growth** (a stated assumption, ten times the filed sales growth, not a finding): **roughly
  SEK 45 to SEK 105 a share**; **SEK 65 to SEK 125** with net cash.
- **Current price SEK 98.66 — above the whole no-growth range, with or without the net cash; inside the 3%-growth range only
  at its top.** The buyback's average price, SEK 103.75, sits above every no-growth construction.

### THE FLOOR, THEN THE RANKING [E4-28, E4-21]
- Honest pre-tax expectancy at this price: **~3.3% to ~7.4% before growth** on the governing constructions — **below the floor on
  every window**, and below it with the net cash netted.
- **Bar: screamer test [E4-01]** — the price is **above the conservative case** and, without growth, above the whole range:
  *"no."* **Windage count: one** — the working-capital release removed at the low end (the lower of the two (c) ends is a range
  display, not a margin; the 2019 DOJ/SEC and restructuring costs are kept as costs, not windage). No end margin is applied because
  no entry is under consideration.
- **Price at which the floor would be met, if Q2 were ever reopened** (recorded in words; **no alert armed** — a Q2 failure is a
  business failure, the QLYS ruling of 2026-09-07): **a cap of about SEK 105bn on the conservative end and SEK 240bn on the best
  five years — roughly SEK 30–75 a share before net cash, SEK 50–90 with it.**

- **VERDICT: not reached — the file closed at Q2. This block is a computation, not a clearance.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

### ⚠ RECORDED, NOT GOVERNING — nothing is owned and nothing is armed.
**Pre-committed [E1-02] — what would make Q2 worth re-running (the reversal conditions, in words):**
1. **The generation re-bid, measured.** A filed statement from Ericsson or Nokia that 6G awards went to the 5G incumbent across
   the major operators without price concessions or *"strategic contracts"* — i.e. that installed networks were **not** re-tendered
   at the generation — would weaken the [E4-04] finding. The first 6G awards are expected before 2030.
2. **Pricing under slack demand [E2-44].** Networks gross margin held or rising for three filed years in which Networks sales fell
   and no cost-reduction programme is cited as the cause — and the Q2 2026 *"pricing actions"* shown in filed margins, not in
   guidance.
3. **Contracts that bind.** A risk-factor change from *"do not contain committed purchase volumes or prices"* to committed
   multi-year volumes and prices with major customers.
4. **The enterprise leg stops consuming.** Enterprise EBIT positive for three years **without** disposal gains.
5. **Q3's open documents.** The DOJ's conclusion of the Iraq investigation; the District of Columbia ruling on the ATA motions to
   dismiss; the CFIUS agencies' NSA findings.
- **Thesis-breaking for the OUT verdict** (what would show it was wrong): Networks earning 18%+ ex-restructuring through the 6G
  transition with R&D flat as a share of sales **and** operators' filings showing single-sourced radio — both, not either.
- **Next catalysts:** Q3 2026 report (≈ mid-October 2026; the Q2 report warned of *"some pressure on Networks adjusted gross margin
  in Q3"*); CEO change **2026-09-30**; buyback completion *"March 31, 2027, at the latest"*; the FY2026 20-F (≈ March 2027).

**The sell rule [E2-28]** — not applicable; no position. **The monitoring question [E3-30, E4-17]:** is the 2021–2025 margin a new
level or the crest of the 5G wave? The 2011–2025 record — margins at or above 12% in three of fifteen years — answers most of it;
the 6G tender answers the rest. **Position size:** none. **[E5-14]** not engaged.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN** — the reopening conditions are written, dated and falsifiable; no band is armed
  and no PORTFOLIO row is added (FOLD step 4, gate-clearers only).

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, **Q2 OUT (closes)**; Q3–Q6 recorded under explicit
      "RECORDED, NOT GOVERNING" banners; the price under COMPUTATION — NOT A CLEARANCE with no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 does not rely on the Dell'Oro share. Q2's
      row has one same-metric radio peer (Nokia) and says so; the verdict turns on criterion (2) and [E4-04], answered by both
      vendors' filed statements of customer behaviour, not on the row's completeness.
- [x] Every UNRESEARCHED verdict names the artifact — none used.
- [x] Every UNKNOWABLE verdict states what cannot be known — Q3 (recorded): the DOJ Iraq conclusion, the ATA ruling, the CFIUS
      NSA findings, none yet in existence.
- [x] Step 0: the FY2025 20-F was read (the 20-F body; Exhibit 15.1 Board of Directors' Report, statements, Notes A1–H6, risk
      factors, APMs, Remuneration Report; Exhibit 2.3), accession `0001193125-26-104149`; 20-Fs FY2013, FY2016–FY2024 for segment,
      cash-flow, SBC, legal and target history; the 2018 20-F/A read for its purpose (*"Submit the Interactive Data File … Correct
      typographical errors in Item 3.A"*); 49 6-Ks since 2025-10-01 and 11 legal-milestone 6-Ks 2019–2024. **Cross-check:** 2024
      OCF SEK 46,261m = filed statement = companyfacts (two accessions) = Board of Directors' Report text.
- [x] Owner earnings on multi-year means; five windows; (c) disclosed as a judgment with the default named and the exception class
      tested and not applied (capex 1.03–1.15x D&A over ten and fifteen years); the lower of the two ends used; the working-capital
      release removed at the low end [E4-41]; **SBC resolves and is complete** (share-settled subtracted every year 2011–2025;
      cash-settled already in OCF); lease repayments restored as a cost from 2019 (CONVENTION, stated); capitalised development in
      (c), acquired-intangible amortisation outside it and acquisitions displayed on their own line; **the Vonage (2022) and iconectiv
      (2025) perimeter moves named** — the windows are consolidated, not pro-forma, and say so.
- [x] Competitor row filled: Nokia (same metric, 2014–2025, boundary named each year), Huawei, ZTE, Samsung, Ciena, Cisco with
      their limits; transcriptions in `peers/NOKIA_row.md` and `peers/OTHERS_row.md` with accession numbers and URLs.
- [x] Sovereign for the earnings currency (SEK, argued from [E4-15, E3-32] on a 99%-foreign sales base; USD and EUR shown), from the
      issuing authority (Sveriges Riksbank SWEA, cross-checked to the Debt Office's 2026-09-09 auction), dated 2026-09-11; **tenor
      10 years, shorter than 30, stated**; fetched by hand, `tools/sources.py` untouched.
- [x] Share classes read before summing (Exhibit 2.3, Note E1: equal dividend and net-asset rights, 1 vs 1/10 vote; C shares none);
      treasury excluded; the 20-F cover's issued count caught and not used; ADR ratio from the 20-F cover and derived-checked at the
      Riksbank fixing; cap in SEK from the Stockholm quote, never the USD ADR.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar (screamer); windage count stated: one.
- [x] Prices dated; aggregator used for live quotes only and flagged.
- [x] Ledger ids checked against `principle_ledger.csv` with `ids.py` on every section before splicing (none missing); quotes of
      [E5-22], [E2-68], [E5-33] and [E2-57] re-read in the ledger rows before use. [E4-27] used for pay, [E4-52] only for converging
      flags.
- [x] Run committed to git with a pathspec, section by section.

**Errors caught in this run before commit, recorded rather than hidden:** (1) Q3's first draft gave ROE as 21.5% / 14.0% / (27.0)% /
0.0% / 26.0% without computing it; recomputed on total equity as 23.9% / 15.9% / (22.6)% / 0.4% / 28.3%. (2) Q3's first draft put
Enterprise EBIT losses 2020–2024 at SEK 76bn; the arithmetic is SEK 71.6bn. (3) Q2's first draft summed CSS EBIT 2020–2025 as SEK
4.9bn; it is SEK 0.6bn. (4) Q2's first draft wrote that AT&T's radio business moved from Nokia **to Ericsson**; neither filing
names the vendor in terms, so the sentence now says only what each filing says. (5) Q4's first draft said sales "fell from SEK
222.6bn to 236.7bn" — that is a rise; corrected. (6) Q4's first draft put 2016–2018 restructuring at SEK 29.9bn; it is SEK 24.1bn,
and a per-share dividend history written from memory (SEK 3.70 → 1.00) was removed and replaced by the filed cash dividends. (7)
Q3's first draft paraphrased [E5-22] inside quotation marks; replaced with the ledger's verbatim sentence. (8) Q3's first draft
claimed the Economic Profit pay design was "the only capital-aware pay design in the recent WAVE 5 files" without checking those
files; deleted. (9) Q4's first draft put share-settled SBC at "0.2–6% of OCF"; 2017 is 9.2%.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Ericsson is the leading radio-network vendor outside China — Networks 64% of sales at a 20.4% margin ex-restructuring
  in 2025, 6–18 points ahead of Nokia in every year since 2018 — but its customers dual-source, re-price yearly without committed
  volumes or prices, swap installed networks at modernisation and will re-tender at 6G, so [E3-03] criterion (2) fails and
  [E4-04] excludes a position rebuilt each generation; Q2 OUT on the business as constituted. Price SEK 98.66 × 3,265,683,059 =
  SEK 322.2bn against owner earnings of SEK 10.6–23.9bn (3.3–7.4%), a 3.23% SEK 10-year bond and a ~10% floor; above the whole
  no-growth value range (COMPUTATION — NOT A CLEARANCE).
- **The strongest single fact against this conclusion:** the margin gap against the only same-metric Western peer has widened from
  zero in the late-4G years to 17.6 points in 2025, and Nokia's own filing says *"Competitive dynamics in the CSP industry strongly favor the top
  two vendors"* — a two-vendor Western market with the low-cost vendors excluded by governments may behave like a franchise for as long as
  the exclusion lasts. The file's answer: the exclusion belongs to the regime [E2-59], the customers still dual-source and re-tender,
  and the position must be re-won at 6G before 2030.
