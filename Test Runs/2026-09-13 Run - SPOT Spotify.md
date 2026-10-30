# Company Run — Spotify Technology S.A. (SPOT) — 2026-09-13
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
verdict and none is assumed here. Every fact the brief supplied is re-derived below from Spotify's own filings
and marked confirmed or corrected. **The 2026-07-15 five-pack run (framework v3.0) was read for what it found and
binds nothing**: it called the moat "NARROW, WIDENING" on three price rises "with low churn" and a 24%→31.5% gross
margin, and priced owner earnings from a net-income start (*"FY2025 NI $2.50B … OE ≈ $1.95B"*) — a net-income proxy
that operator rule 5 forbids, in dollars against a euro reporter. No figure is inherited from it.*

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- **rate 3.83% (3.8262%) · euro area AAA government yield curve, 30-year spot rate (ECB SDW series
  `YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y`) · date 2026-09-10 · source: European Central Bank** — struck fresh this
  session twice: `python tools/sources.py` printed *"EUR 3.83% 2026-09-10 ECB euro area AAA yield curve (SR_30Y)"*,
  and a direct pull of the ECB data API (`_research 2026-09-13 SPOT/sov/ecb_SR_30Y.csv`) returned 3.8262 for
  2026-09-10, 3.7839 for 09-09, 3.7546 for 09-04 — **confirmed, the brief's 3.83% holds**. No 2026-09-11 observation
  was published at the time of the pull. The 10-year point of the same curve read 3.5032% on 2026-09-10
  (`sov/ecb_SR_10Y.csv`), shown only so the tenor choice is visible.
- **Shown for sensitivity only:** USD **5.35%** (US Treasury daily par yield curve, 30-year, 2026-09-11, via
  `tools/sources.py`).
- **Where Spotify earns, from the filing — and the filing gives no currency split.** Note 23 (revenue by country):
  **United States €6,470m of €17,186m = 37.6%**; Luxembourg €13m; **"Other countries" €10,703m = 62.3%**, with
  *"There are no countries that individually make up 10% or more of total revenue included in 'Other countries.'"*
  Item 11: *"In most cases, our customers are billed in their respective local currency. Major payments, such as
  salaries, consultancy fees, and rental fees are settled in local currencies. **Royalty payments are primarily
  settled in Euros and U.S. dollars.**"* The MD&A names the currencies that moved revenue: *"the U.S. dollar, Mexican
  peso, Brazilian real, and Argentine Peso"*, and quantifies the translation: Premium revenue *"would have been
  approximately €502 million higher"* and Ad-Supported *"approximately €83 million higher"* at 2024 rates; cost of
  revenue *"approximately €419 million higher"*, operating expenses *"approximately €121 million higher"*. **So FX cut
  2025 revenue by €585m and costs by €540m: the royalty line is largely a pass-through of the same currency mix,
  and the operating-income exposure is a small fraction of the revenue exposure.** Sweep for a currency table
  (`denominated in`, `currencies other than`, `functional currency of`, Item 11, Note 22): **no instance of a
  revenue-by-currency split found**; the brief's "state the split the filing gives" is answered with the country
  split above, and the limit is stated.
- **Why EUR — argued from the corpus, not defaulted.** [E4-15] makes the rate a gravity on the value of the claim;
  what a Spotify shareholder owns is a claim **measured, reported and retained in euros**: *"The consolidated
  financial statements are presented in Euro, which is the Group's reporting currency"* (Note 2); the cash and
  short-term investments, the buyback accounting and every owner-earnings input below are euro figures; the royalty
  liability that dominates the cost base is settled *"primarily … in Euros and U.S. dollars."* **[E3-32] forbids a
  view on rates, and choosing the US rate because 37.6% of revenue is American and the shares quote in dollars
  would be a view on which currency's rate the owner will one day be paid in.** The foreign earning base is carried
  as **width in the EUR owner-earnings figure** (FX moved 2025 revenue by €585m), not as a second rate — the SONY,
  TM, HMC and ERIC precedent, argued again on Spotify's own mix. **And the choice cannot change a verdict at Q5:**
  the ~10% floor [E4-28] holds *"whether short rates are 6 percent or whether short rates are 1 percent"* — above
  3.83% EUR and 5.35% USD alike.
- **FX, quote vs earnings — CONVERTED, never mixed (the ATLKY defect guarded).** The ordinary shares quote in USD on
  the NYSE; owner earnings are in EUR. **The cap is converted to euros at the ECB euro foreign exchange reference
  rate, USD per EUR 1.1592 on 2026-09-11** (ECB SDW series `EXR.D.USD.EUR.SP00.A`, file `sov/ecb_EXR_USD.csv`; 1.1616
  on 09-10). The quote date and the reference-rate date are the same day. **Every yield below is EUR over EUR.**
- **ADR ratio: none — the ordinary shares are listed directly. Confirmed from the 20-F cover:** *"Ordinary Shares
  (par value of €0.000625 per share) | SPOT | New York Stock Exchange"*, and Item 12.D *"American Depositary Shares
  — Not applicable."* One quoted share is one ordinary share. **Derived check:** the registrar reports
  *"177,613,882 of our ordinary shares were held by 443 record holders in the United States"* (Item 7.A) — ordinary
  shares held of record directly, which is the form a direct listing takes.

**THE BENEFICIARY CERTIFICATES — read from the articles before counting (the brief's instruction, discharged).**
- **Articles of association (Exhibit 1.1 to the 20-F), Article 9.6:** *"The Beneficiary Certificates shall not
  carry any right to participate in any dividend, share premium repayment or any other kind of distributions,
  **including the distribution of any liquidation proceeds**, made by the Company."* Article 9.7: *"Each Beneficiary
  Certificate shall carry one (1) vote."* Article 9.8: non-transferable, *"automatically cancelled in case of sale or
  transfer of the share(s) to which they are linked"* (with a board discretion to except).
- Note 16 repeats it: *"The beneficiary certificates carry no economic rights and are issued to provide the holders
  of such certificates additional voting rights."* Ten per linked ordinary share, **309,932,980 outstanding at
  2025-12-31** (324,732,980 a year earlier) and **309,932,980 at 2026-06-30** (6-K Q2 2026, Note 13).
- **RULING: the beneficiary certificates carry no claim on dividends, distributions or liquidation proceeds.
  They are EXCLUDED from the cap.** They are recorded at Q3 as control: Item 7.A, *"Daniel Ek … 28,625,267 [ordinary
  shares] 13.9% | 119,932,980 [certificates] | 28.8% [of total voting power]"*; *"Martin Lorentzon … 19,050,367 9.3%
  | 190,000,000 | 40.5%"* — **23.2% of the capital, 69.3% of the votes.** Ek's 28.6M includes 16.6M ordinary shares
  held by Tencent entities over which his vehicle *"holds an irrevocable proxy"*; Tencent is listed separately with
  **16,631,969 shares, 8.1%**.
  *Correction, same run, written beside the line above rather than over it (operator rule 6): "23.2% of the capital"
  double-counts Tencent. Ek's 28,625,267 is 11,993,298 held by D.G.E. Investments **plus** the 16,631,969 Tencent shares
  he votes by proxy (11,993,298 + 16,631,969 = 28,625,267). **The founders' own economic stake is 11,993,298 + 19,050,367
  = 31,043,665 shares, 15.1% of 205,832,527**; the capital they vote, with the Tencent proxy, is 23.2%; their share of
  all votes is 69.3%.*

**THE SHARE COUNT — by hand (a 20-F filer; `tools/run.py SPOT` prints *"SPOT: no overlapping OCF/D&A/capex annual
facts. UNRESEARCHED."*).**
1. **The 20-F cover is OUTSTANDING, not issued — the ERIC trap checked, and it does NOT fire here.** Cover:
   *"205,832,527 Ordinary Shares, par value €0.000625 per share."* Note 16: *"the Company had 209,485,215 … ordinary
   shares issued and fully paid"* and *"3,652,688 … ordinary shares held as treasury shares"* at 2025-12-31.
   **209,485,215 − 3,652,688 = 205,832,527 = the cover figure**, and the statement of changes in equity's column
   *"Number of ordinary shares outstanding"* closes 2025 at *"205,832,527"*. **Confirmed outstanding.** (Pricing on
   the issued count would have overstated the cap by 1.8%.)
2. **Latest filed count: 6-K for the quarter ended 2026-06-30, filed 2026-08-04, accession
   `0001628280-26-052543`**, Note 13: *"As of June 30, 2026 and December 31, 2025, the Company had 210,241,268 and
   209,485,215 ordinary shares issued and fully paid, respectively, with 4,657,063 and 3,652,688 ordinary shares held
   as treasury shares."* **Outstanding at 2026-06-30 = 210,241,268 − 4,657,063 = 205,584,205.**
3. **Reconciliation of treasury:** 3,652,688 + 750,000 issued to and repurchased from the Netherlands subsidiary
   (*"the Company issued and repurchased … 750,000 of its own ordinary shares … at par value"*) + 1,349,216 bought
   back (*"1,349,216 shares for €547 million (US$638 million) during the six months"*) − 1,094,841 reissued on option
   exercise and RSU release = **4,657,063. Reconciles exactly.** Issued rose 756,053 against 750,000 to the
   subsidiary; the 6,053 remainder is not itemised in the note (0.003%, recorded, not chased).
4. **After the quarter:** *"through close of business on August 3, 2026, the Company repurchased an additional 50,000
   shares for €21 million"* (same note), and the Board added US$1.5bn to the program on 2026-08-20 (6-K
   `0001140361-26-033885`: *"With $723 million remaining under the current repurchase program, the increase brings the
   total authorization … to approximately $2.223 billion"*). July–September reissuances on exercise are not filed,
   so the 50,000 is not netted; it is 0.02% and does not move any figure below.
5. **Dilutive instruments, stated:** at 2025-12-31 **4,665,081 options** (weighted exercise US$198.32; at most
   358,428 of them, in the US$498.99–1,084.00 bands, carry strikes that can sit above the quote) and **1,317,262 RSUs** plus 7,706 other contingently issuable shares (Note 17); **warrants:
   none** (*"As of December 31, 2025, there were no outstanding warrants"*); **Exchangeable Notes: none** — *"matured and
   were derecognized on March 15, 2026"*, repaid in cash (*"Repayment of Exchangeable Notes | (1,304)"*, 6-K Q2 2026),
   after the Group *"elected to settle all exchanges on or after December 15, 2025 in cash."* **The diluted
   weighted-average count for Q2 2026 is 208,858,469 against basic 205,788,241 (+1.5%).** The cap uses the outstanding
   count; option dilution is carried at Q3 (serial issuance) and SBC is subtracted in full at Q4 — **not counted twice.**
6. **Shares used: 205,584,205** (as at 2026-06-30).
- **Split:** `split_factor_after('SPOT','2025-12-31')` returns **1.0**; the Yahoo chart carries no split event over
  ten years; no split is described in the 20-F or any 6-K read. Cap = close(2026-09-11) × shares(2026-06-30) × 1.0.
- **Price US$525.75** (SPOT, NYSE close 2026-09-11, Yahoo, **aggregator, live quote only, flagged**; 52-week range
  US$405.00–745.00 per the same feed) × **205,584,205** = **market cap US$108,086M** ÷ **1.1592** = **market cap
  €93,242M** (price per share **€453.55**).
- **The balance sheet beside the cap (6-K Q2 2026, 2026-06-30, €M):** cash and cash equivalents 5,938 + short term
  investments 3,450 = **9,388 of liquidity**; **no borrowings** (the Exchangeable Notes are gone; lease liabilities
  404 non-current plus the current portion in Note 17); **long term investments 1,118, the majority of which is a
  listed stake in Tencent Music Entertainment** (20-F Item 11: *"The majority of our long term investments relate to
  TME"*; it was €2,181m at 2025-12-31 and the half-year OCI carries *"(1,066)"* of fair-value loss). The cap is an
  enterprise figure only after these are named; Q5 states whether they are netted.

**THE PERIMETER — the filings, with dates. Nothing here is from memory.**
- `deal_note(1639920)` and `name_change_note(1639920)` returned nothing; `formerNames` in `submissions.json` is
  empty. **Confirmed**, and blind to acquisitions disclosed only inside 20-F notes, as HMC and ERIC found. The
  acquisitions inside the window (the podcast and audiobook purchases of 2019–2022) and any impairments are read
  from the FY2019–FY2022 20-Fs at Q3; goodwill is **€1,083m** at 2025-12-31 (€1,201m in 2024; the fall is currency
  translation or impairment — read at Q3, not asserted).
- **No disposal, spin or change of reporting segment inside 2021–2025** beyond the 2025 move of video-podcast costs
  from Ad-Supported to Premium (Note 23: *"Beginning in 2025 … Podcast content costs attributable to this new
  experience for subscribers to our Premium Service are recorded in the Premium segment"*), which moves segment
  margins, not the consolidated figures.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A (Item 5 read in full: overview, how revenue is generated, components of operating results, KPIs, operating
  results by segment, FX impact, liquidity, buyback, Exchangeable Notes, cash flow, free cash flow, contractual
  obligations, trend information); Item 4.B business overview including licensing agreements and competition; Item
  11 market risk; Item 7.A major shareholders; the articles (Exhibit 1.1, Article 9)
- [x] cash-flow statement incl. detail lines (2023–2025, every line; the 6-K half-year statement for 2026)
- [x] footnotes (Notes 4, 5, 7, 8 (part), 9, 10 (part), 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27 read; the
  others read at the gate that needs them)
- **Primary document: Form 20-F for the fiscal year ended December 31, 2025, filed 2026-02-10, accession
  `0001628280-26-006874`** (`ck0001639920-20251231.htm`) — **confirmed**. Latest 6-K **2026-09-03,
  `0001140361-26-035575` — confirmed**, and it is **a board resignation** (Heidi O'Neill), not results; the latest
  results are the **Q2 2026 6-K filed 2026-08-04** (interim report `0001628280-26-052543`; shareholder update
  `0001140361-26-031044`). Nine 6-Ks from 2026-02-10 to 2026-09-03 are on disk in `_research 2026-09-13 SPOT/6k/`.
- **Figure cross-checked against the filed statement:** **net cash flows from operating activities 2025, €2,933m** —
  identical in the 20-F consolidated statement of cash flows (F-9), in the MD&A cash-flow table (*"Net cash flows
  from operating activities | 2,933 | 2,301 | 680"*), in the Q4 2025 shareholder update's twelve-month column, and
  in XBRL companyfacts `ifrs-full:CashFlowsFromUsedInOperatingActivities` = 2,933 (EUR). **Confirmed.**
- **Tooling note — the brief's skip reason, TESTED.** (a) *"short XBRL history"*: **false for Spotify** —
  companyfacts holds **ten annual IFRS periods, 2016–2025**, of operating cash flow, capex, SBC, depreciation,
  amortisation and revenue, **all in the `EUR` unit**. (b) *companyfacts lags the newest 20-F*: **false for Spotify**
  — FY2025 is ingested. (c) **The real cause is the one measured in RESUME STATE §9 on 2026-09-13, reproduced:** the
  facts exist, but in `ifrs-full` element names and in **EUR**; `floor_screen.annual()` reads only the `USD` unit and
  `tools/run.py` requests US-GAAP names, so SPOT prints *"no overlapping OCF/D&A/capex annual facts"*. **Spotify is
  the clearest case of the three causes separating: full history, current ingestion, unpriceable by construction.**
  Reported, not fixed (a tool change is outside a run's brief).

## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Answered per segment, from the filed segment note (Note 23) and the MD&A of each year's 20-F.** 2023–2025 from
the FY2025 20-F (`0001628280-26-006874`); 2020–2022 from the FY2022 20-F (`0001639920-23-000004`); 2017–2019 from
the FY2019 20-F (`0001564590-20-004357`). Subscribers, MAUs and ARPU are the December figures each 20-F reports.
€ million. *The Premium cost-of-revenue ratio is arithmetic on the filed lines (`q1` figures, no judgment).*

| Year | Premium revenue | Premium cost of revenue | **Premium CoR ÷ revenue** | Premium GM | Ad-Supported revenue | Ad GM | Group GM | Premium subscribers (M) | MAUs (M) | Premium ARPU (€/month) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 3,674 | 2,868 | **78.1%** | 22% | 416 | 10% | 21% | 71 | 160 | 5.32 |
| 2018 | 4,717 | 3,461 | **73.4%** | 27% | 542 | 18% | 26% | 96 | 207 | 4.81 |
| 2019 | 6,086 | 4,465 | **73.4%** | 27% | 678 | 15% | 25% | 124 | 271 | 4.72 |
| 2020 | 7,135 | 5,126 | **71.8%** | 28% | 745 | 1% | 26% | 155 | 345 | 4.31 |
| 2021 | 8,460 | 5,986 | **70.8%** | 29% | 1,208 | 10% | 27% | 180 | 406 | 4.29 |
| 2022 | 10,251 | 7,355 | **71.7%** | 28% | 1,476 | 2% | 25% | 205 | 489 | 4.52 |
| 2023 | 11,566 | 8,231 | **71.2%** | 29% | 1,681 | 4% | 26% | 236 | 602 | 4.39 |
| 2024 | 13,819 | 9,324 | **67.5%** | 33% | 1,854 | 12% | 30% | 263 | 675 | 4.69 |
| 2025 | 15,350 | 10,184 | **66.3%** | 34% | 1,836 | 18% | 32% | 290 | 751 | 4.63 |
| H1 2026 (6-K) | — | — | — | 35% | — | 16% | 33% | 300 (June) | — | 4.82 (H1) |

*2017 subscribers and MAUs and the 2017 ARPU are from the FY2018 20-F text (*"Premium Subscribers were 96 million as
of December 31, 2018"*; the 2017 comparatives appear in the same sentences). **Effective 2026-01-01 some Ad-Supported
activities moved to Premium** (Q2 2026 shareholder update: *"certain revenue-generating activities previously
reported within the Ad-Supported segment were transferred to the Premium segment to reflect changes in the financial
information presented to the Group's new Co-Chief Executive"*), so 2026 segment figures are not comparable with the
table; it is noted at Q3 under [E2-49].*

- **Unit economics in my own words, no management language:**
  1. **Premium (89% of 2025 revenue): it rents the world's recorded music from a handful of owners and re-rents it by
     the month to 290 million people, keeping about a third of what they pay.** A subscriber pays a local-currency
     monthly fee (family, duo and student plans pay less per head); Spotify passes most of it to the owners of the
     recordings and songs under formulas that are *"the greater of a percentage of relevant revenue and a per user
     amount"* (Item 5, Components of Operating Results), plus payment fees and streaming delivery. **What is left —
     34% gross in 2025, up from 22% in 2017 and flat at 27–29% for six years before 2024 — pays for the software,
     marketing and overhead.** The label contracts even tie the royalty *percentage* to Spotify's own performance:
     *"the percentage of revenue used in the calculation of royalties is generally dependent upon certain targets
     being met. The targets can include such measures as the number of applicable Premium Subscribers, the ratio of
     Ad-Supported Users to applicable Premium Subscribers, and/or the rates of applicable Premium Subscriber churn."*
  2. **Ad-Supported (11%): it gives a limited version away, sells audio and display advertising against the
     listening, and pays the owners a share of that too.** It is a funnel as much as a business: *"Our Ad-Supported
     Service serves as a funnel, driving a significant portion of our total gross added Premium Subscribers."*
     Gross margin has been **1% to 18%** across nine years and its revenue **fell 1% in 2025** (*"a decrease in
     fixed-CPM rates as well as a decrease in music impressions sold"*).
  3. **Podcasts, audiobooks and video are costs inside both segments, not segments.** Podcast content was all charged to
     Ad-Supported until 2025; from 2025 video-podcast payouts (the *"Spotify Partner Program"*) and audiobooks sit in
     Premium cost of revenue (Note 23). They are paid for in two ways: owned/produced content amortised over its life,
     and licensed or creator content paid per consumption. **2023 carried the podcast retreat as filed charges**:
     *"€29 million related to the write-off of content assets, €12 million of employee severance costs, €8 million of
     contract terminations"* in Ad-Supported cost of revenue (Note 23), inside a year of €212m severance (Note 5).
- **What Spotify pays the rights holders — as a share of revenue, and the filing's limit.** **The 20-F gives no
  royalty total.** Sweep: "royalt", "rights holders", "music industry", "billion" in the FY2025 20-F — **no instance of
  an annual royalty figure found**. What is filed: (a) cost of revenue *"consists predominantly of royalty and
  distribution costs"*; (b) Premium cost of revenue as a share of Premium revenue, the column in bold above,
  **78.1% (2017) → 70.8–73.4% (2018–2023) → 67.5% (2024) → 66.3% (2025)**, which includes payment processing and
  streaming delivery as well as royalties; (c) the year's royalty *increment*, *"higher royalty costs of €765 million"*
  in Premium in 2025 against a €1,531m Premium revenue increase (**50% of incremental revenue**), and *"€1,152
  million"* against €1,791m in 2022 (**64%**); (d) the balance owed, *"Accrued fees to rights holders | 1,950 |
  1,695"* (Note 20); (e) minimum guarantees of **€2.6bn** (Note 24; €2.7bn *"estimated future financial commitments
  … under license agreements"* in the risk factor). The company's own headline, in the Q4 2025 shareholder update
  (6-K `0001140361-26-004482`), not the audited statements: *"Paid out over $11 billion to the music industry in
  2025"*. **Trend, in plain words: the owners' take of each Premium euro was roughly flat at 71–73 cents for six
  years and fell to about 66 cents in the two years of Spotify's price increases — the first two years the company
  earned an operating profit.** Whether that shift is Spotify's pricing power or a negotiated, reversible window is a
  Q2 question, read from both sides' filings there.
- **Price increases and their filed effect on ARPU** (each 20-F's ARPU bridge, quoted): 2021 *"an increase in ARPU for
  the Family Plan, as a result of price increases"*; 2023 *"an increase in Premium ARPU of €0.15 as a result of price
  increases"*; **2024 *"price increases resulting in an increase in Premium ARPU of €0.49"***; 2025 *"an increase in
  Premium ARPU of €0.25 as a result of price increases"*; H1 2026 *"price increases, resulting in a €0.45 increase"*
  (6-K Q2 2026). **Reported ARPU in euros is still below 2017's €5.32 and 2018's €4.81**: mix (family plans, cheaper
  markets) and currency took back what price added in every year but 2024. Subscribers and churn around each
  increase are the [E2-44] test at Q2.
- **The scarce input this business controls: not the music.** The catalogue is licensed, non-exclusive and renewed
  every few years from owners who are concentrated: *"Universal Music Group, Sony Music Entertainment, Warner Music
  Group, and … ("Merlin"), makes up the majority of music consumed on our Service … approximately 72% of streams of
  audio content delivered by record labels"* (risk factors), and the licences *"are not automatically renewable"*
  (Item 4.B). What Spotify holds that the owners do not: **the listener relationship at scale** — 751 million MAUs,
  290 million paying accounts, *"211 billion hours of content"* streamed in 2025 — and the listening history that
  drives its recommendations. Whether that is a *controlled* scarce input or merely a large position is exactly Q2's
  question; Q1 records only that the business's one owned asset is the audience, not the product.
- **"On what capital?"** Almost none: PP&E **€188m**, capex **€61m** in 2025 (€6m in 2023); the balance sheet's
  working capital is negative because royalties and deferred subscriptions are owed before they are paid (accrued
  fees to rights holders €1,950m, deferred revenue €711m). The capital that matters is the **€2.6bn of minimum
  guarantees** and the SBC-funded payroll, both read at Q4.
- **Will the fundamentals look broadly the same in ten years?** **The model has not changed since the F-1**: rent
  the catalogue, sell access by subscription and advertising, pay the owners by formula. Eighteen years in, it is the
  same arithmetic with podcasts, audiobooks and video layered on. What is *not* stable is the price of the input,
  which is set by multi-year negotiation with concentrated suppliers and, for US mechanical rights, by the Copyright
  Royalty Board (*"Royalty rates beginning on January 1, 2028 may differ from those in effect today"*). **That
  instability is a question about durability and bargaining position — Q2 and Q4 — not about whether the money-making
  can be understood.** [E4-46] is met: the mechanism is statable in five minutes and nothing in it needs months of
  study.
- **VERDICT: [x] IN** — the money-making is understandable from the filed segment note and MD&A: Premium is a
  resold licence with a formula-set royalty and a thin, recently widened gross margin; Ad-Supported is a low-margin
  funnel. The filing does not give the royalty total, and that limit is stated rather than filled; it does not bear
  on understanding the mechanism, only on measuring the split, which Q2 takes up. **IN never promotes**: nothing
  here says the business is good.

## Q2 — IS IT A FRANCHISE? **[E3-03]**

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its customers to have **no
> close substitute** and; (3) is not subject to price regulation." — **[E3-03]**, 1991 letter

*Hypotheses to refute, stated before the evidence was read (operator rule 9): (H1) Spotify's audience and
personalisation make it the service listeners will not leave, so criterion (2) holds despite the shared catalogue;
(H2) the 2023–2026 price increases with continued subscriber growth are [E2-44]'s test passed; (H3) the royalty share
falling from 71–73% to 66% is Spotify's bargaining power over the labels, i.e. a widening moat [E4-32]. Each is tested
below against Spotify's own filings, its competitors' and its suppliers'. Evidence file:
`_research 2026-09-13 SPOT/peers/PEERS.md` (built by a sub-agent under an evidence-only brief; every quote was read
back against its source text before use here).*

- **Needed or desired [x]** — 751 million MAUs, 290 million paying accounts at 2025-12-31, 300 million at 2026-06-30.
- **Not price-regulated [x], with one regulated input.** Consumer prices are set by Spotify market by market; the US
  mechanical royalty on compositions is set by the Copyright Royalty Board (*"calendar years 2023 to 2027 in
  proceedings known as the 'Phonorecords IV'"*; *"Royalty rates beginning on January 1, 2028 may differ"*). Criterion
  (3) caps the cost side, not the price side, and it holds.
- **No close substitute [ ] — FAILS, on the evidence of all three parties.**
  1. **The supplier says the product is the same everywhere and the customer needs only one.** UMG, the largest
     licensor, Annual Report 2025 (rung 3, not an SEC filer), p.101: *"DSP providers generally make all content
     available, thus not requiring multiple subscriptions."* p.94: *"they all seek to work closely with UMG, the largest
     supplier of content to all of the digital service providers. This is because UMG's artist content is a key driver
     of customer acquisition and retention for all of these platforms."* WMG 10-K FY2025 (`0001319161-25-000034`) lists
     the same partners: *"Amazon, Apple, Deezer, KKBox, Spotify, Tencent Music Entertainment Group and YouTube."* TME's
     20-F FY2025 (`0001193125-26-160257`): *"Our licensing agreements with music labels and music copyright owners are on
     a non-exclusive basis."* **What the customer buys is the catalogue; the catalogue is the same at every door, and
     the owner of the catalogue says so.**
  2. **Spotify says its customers can and do switch, and that its rivals do not need to earn on music.** 20-F FY2025
     risk factors: *"Our current and future competitors have introduced, and may continue to introduce, new ways of
     consuming or engaging with content that cause our users, especially the younger demographic, to switch to another
     product or service"*; *"prominent, well-funded competitors like Apple, Alphabet, and Amazon have a competitive
     advantage because they can leverage the substantially broader product offerings in their ecosystem"*, able *"to
     offer competitive services at little or no profit or even at a loss"*; and devices *"for which their streaming
     service is preloaded and/or able to be used out-of-the-box."* Premium subscribers *"may cancel their subscriptions at
     any time."*
  3. **A competitor says the listener can get it elsewhere, and its own subscribers left.** SiriusXM 10-K FY2025
     (`0000908937-26-000006`): *"Our subscribers and listeners can obtain similar content for free through Spotify,
     YouTube and other internet services"*; Pandora self-pay subscribers **6,324k (2021) → 5,630k (2025)** and MAUs
     **52,275k → 41,112k**, while *"Streaming and on-demand services, including Amazon Prime, Apple Music, Spotify, TikTok
     and YouTube, compete with our SiriusXM and Pandora services."* **Listeners do move between music services; Pandora's
     loss is the filed record of it.**
  4. **The price increases were an industry's, not one firm's.** WMG 10-K FY2022: *"In 2022, Apple Music increased prices
     of its student plans … and Amazon Music Unlimited increased the prices of both its individual and family
     subscription plans"*; FY2023 (`0001319161-23-000036`, quoted in the SONY run's music file): *"in 2023 Spotify increased prices in 65
     countries … YouTube increased prices of its individual and family plan tiers on both YouTube Premium and YouTube
     Music in the United States in 2023. In 2022, Apple Music increased prices of its individual and family plans in the
     United States"*; FY2025: *"In 2025, YouTube increased the prices … In 2024, Amazon Music Unlimited increased the
     prices."* **A price rise that follows rivals' rises is evidence of parallel pricing [E3-61], not of a product
     without a close substitute.**
- **Must the moat be continuously rebuilt? Does success depend on a great manager? [E4-04]** **The basis is re-leased,
  not owned.** WMG: *"Our agreements with digital music services generally last one to three years"* and *"We currently
  enter into short-term license agreements with many digital music services and provide our music on an at-will basis
  to others"*; Spotify: label licences are *"multi-year"* and *"not automatically renewable"*, collecting-society
  licences *"generally in place for one to three years"*. Under the scope the corpus sets (a lapse that *destroys* the
  structure vs one that *narrows* it), **a lapse in any major's licence removes a large part of the product** —
  *"the music licensed to us under our agreements with Universal Music Group, Sony Music Entertainment, Warner Music
  Group, and … Merlin, makes up the majority of music consumed on our Service."* The spending on product (R&D €1,393m,
  8% of revenue) defends the audience; it cannot defend the licence. **Key-person [E4-23]: not recorded** — the founder
  handed the CEO role to two Co-CEOs on 2026-01-01 and the filings show no single-person dependence.
- **Primary moat metric, filing-sourced, and its trend:** Premium gross margin **22% (2017) → 27–29% (2018–2023) → 33%
  (2024) → 34% (2025) → 35% (H1 2026)**; Premium cost of revenue per Premium euro **78.1% → 66.3%**; subscribers growing
  **17.0% (Q2 2023) → 11.5% (Q3 2024) → 10.3% (Q4 2025) → 8.7% (Q2 2026)** year on year. **Direction [E4-32]: widening
  in margin for two and a half years, decelerating in units.** [E4-55]: units (subscribers) are still rising; the
  euro ARPU they pay is below 2017.

**THE COMPETITOR ROW — required [E3-28].** Same metrics, 2021 and 2025, filing-sourced. *Arithmetic on filed lines is
marked COMPUTED.*

| Company | paying subscribers 2021 → 2025 | subscription revenue 2021 → 2025 | gross margin 2021 → 2025 | rights-holder cost / revenue 2021 → 2025 | operating margin 2021 → 2025 | source |
|---|---|---|---|---|---|---|
| **Spotify** | 180M → 290M (Dec) | €8,460m → €15,350m (Premium) | 27% → 32% (group); Premium 29% → 34% | Premium CoR 70.8% → 66.3% (includes payment and delivery; royalty total not disclosed) | 1.0% → 12.8% (COMPUTED) | 20-F FY2022 `0001639920-23-000004`; FY2025 `0001628280-26-006874` |
| **Tencent Music** (China) | 68.6M → 125.1M (annual average) | RMB 7,333m → RMB 17,660m | 30.1% → 44.2% (one segment, incl. social entertainment) | not disclosed (service costs bundle royalties with live-streaming revenue share) | 12.2% → 40.6%; **33.4% ex the RMB 2,373m UMG gain** (COMPUTED) | 20-F FY2021 `0001193125-22-120210`; FY2025 `0001193125-26-160257` |
| **Pandora and Off-platform** (SiriusXM segment) | 6,324k → 5,630k self-pay | $530m → $526m | 35.9% → 31.3% segment (COMPUTED) | revenue share and royalties 55.0% → 61.1% of segment revenue (COMPUTED; includes podcast revenue share) | not disclosed below gross profit | 10-K FY2021 `0000908937-22-000007`; FY2025 `0000908937-26-000006` |
| **Apple Music** (Apple) | not disclosed | not disclosed | not disclosed (Services 75.4%) | not disclosed | not disclosed | 10-K FY2025 `0000320193-25-000079` |
| **YouTube Music** (Alphabet) | not in 10-K; *"125 million YouTube Music and Premium subscribers globally, including trials"* (YouTube Blog, 2025-03-05, rung 3) | not disclosed (inside "subscriptions, platforms, and devices" $48,030m) | not disclosed | not disclosed | not disclosed | 10-K FY2025 `0001652044-26-000018` |
| **Amazon Music** (Amazon) | not disclosed | not disclosed (inside "Subscription services" $49,619m) | not disclosed | *"Total video and music expense was … $ 22.4 billion"*, not split | not disclosed | 10-K FY2025 `0001018724-26-000004` |

**The supplier row — who holds the pricing power between Spotify and the labels, from both sides' filings:**

| Filer | what it says about the other side | figures |
|---|---|---|
| **Spotify** (20-F FY2025) | *"These rights holders also may attempt to take advantage of their market power (including by leveraging their publishing affiliate) to seek onerous financial or other terms from us"*; licensors can impede the business *"by withholding content, discounts and bundle approvals, and the rights to launch new service offerings"*; *"some of our license agreements require consent to undertake certain business initiatives"*; MFN clauses; royalty % *"dependent upon certain targets being met"* | majors plus Merlin **~72%** of label streams; minimum guarantees **€2.6bn** |
| **WMG** (10-K FY2021–FY2025, same sentence each year) | *"We have limited ability to increase our wholesale prices to digital music services as a small number of digital music services control much of the legitimate digital music business"*; the services *"are able to significantly influence the pricing structure"*; FY2025: *"The music industry is increasingly focused on price increases as a driver of growth … We continue to see progress in aligning our contracts with streaming services with this new paradigm"* | **Spotify = 18% (FY2021) → 20% (FY2025) of WMG revenue**; top three DSPs ~42% → ~43% |
| **UMG** (Annual Reports 2024–2025, rung 3) | *"the largest supplier of content to all of the digital service providers"*; *"In late 2024 and in 2025 we implemented Streaming 2.0 deals with Amazon, Spotify and YouTube"* that *"drive ARPU growth"* | largest customer **20% of UMG revenue** (unnamed; UMG calls Spotify *"the largest digital service provider"*) |
| **SiriusXM / Pandora** (10-K FY2025), a licensee without scale | *"The economic terms of these direct licenses are onerous … We have not been able to negotiate or obtain lower royalty rates"*; rivals *"have the ability to bear these onerous economic provisions to a much greater extent"* | royalties 55% → 61% of segment revenue |

**What the two sides together show: a bilateral oligopoly, not a franchise on either side.** Each side's filing says
the *other* holds the power — the label that *"a small number of digital music services control much of the …
business"*, Spotify that the rights holders have *"market power"*. **The filed economics say how the price gains were
split:** in 2025 Premium royalties rose **€765m** against a Premium revenue increase of **€1,531m** (50%); in 2022,
**€1,152m** against **€1,791m** (64%) (MD&A). The labels publicly *want* Spotify's price to rise (WMG's "new paradigm",
UMG's "Streaming 2.0 … drive ARPU growth") because their royalty is a percentage of it. **H3 is partly refuted:** the
royalty share did fall, and Spotify's scale (a fifth of a major's revenue) is real bargaining weight — **but the price
increases that produced it were the licensors' strategy as much as Spotify's, and every increase is shared by contract
at renewal.** Pandora, the subscale licensee, shows what the same licensors do to a service without that weight.

- **Peers named: 6** (Tencent Music, Pandora/SiriusXM, Apple Music, YouTube Music, Amazon Music; Deezer attempted — see
  `peers/PEERS.md`) **of the industry's real competitors**, plus **3 of the 3 major suppliers** (WMG, UMG, Sony's
  20-F). The three largest rivals **do not disclose music at all**; that is a limit of the documents, not an unperformed
  task, and **the failure of criterion (2) above does not rest on their numbers** — it rests on the supplier's statement
  that all services carry all content, Spotify's own switching and loss-leader disclosures, and a competitor's
  measured subscriber loss. *[E3-61]: the row shows position; it cannot show conduct.*
- **Untapped pricing power [E3-33, E5-28]?** Claiming the class is claiming near-monopoly; the row does not support it
  — three rivals with larger balance sheets sell the same catalogue, and the price moves were parallel. **[E4-37]'s
  inverse metric reads the wrong way for a franchise:** increases were staggered market by market (*"announced price
  increases are expected to have a minimal impact on Total Revenue in Q3"*, 6-K 2023-07-25), and after 2021 the filer
  stopped reporting what they did to churn (Q3).
- **[E2-44], the two-characteristic test — the strongest evidence FOR the franchise, stated in full.** (1) *"an ability
  to increase prices rather easily (even when product demand is flat and capacity is not fully utilized)"* — Spotify
  raised prices in 2021 (*"no meaningful impacts to churn or customer intake"*, 6-K 2021-02-03), in 2023 (*"Better than
  expected gross intake in markets that saw price increases"*, 6-K 2023-10-24), 2024, 2025 and 2026, and **net
  subscriber additions stayed positive in every one of the 21 quarters Q2 2021 – Q2 2026**. **H2 holds as far as the
  filings go.** Its limits, stated: demand was *not* flat (subscribers grew 9–17% a year), so the parenthesis was never
  tested; churn has been undisclosed since 2022; and the increases were matched across the industry. (2) *"grow dollar
  volume with only minor additional investment of capital"* — **passes cleanly**: revenue ×5.8 in nine years on
  PP&E of €188m.
- **[E3-43], the franchise test in its own words:** *"The existence of all three conditions will be demonstrated by a
  company's ability to regularly price its product or service aggressively and **thereby to earn high rates of return
  on capital**."* The first half is on file since 2023; **the second is not**: return on average equity **(9.0)%,
  (24.0)%, (1.4)%, (19.0)%, (21.6)%** for 2019–2023, **28.3% and 31.9%** for 2024–2025; five-year mean **3.6%**;
  cumulative net income 2016–2025 **a loss of €265m** (Q3, [E2-01]). **[E3-46]:** *"the best businesses, by definition,
  are going to be businesses that earn very high returns on capital employed over time"* — **over time**, the record is
  two years.
- **[E2-45], the attacker's test:** the attack has been running with ample capital (Apple, Alphabet, Amazon), and
  Spotify's subscribers grew from 71M (2017) to 300M (2026) through it. **That is a surfing run [E3-51] on a large
  audience, not a moat the attackers cannot cross**: the attackers did not need to win, because they sell the same
  licensed catalogue *"at little or no profit"* while the licensors take the majority of every euro from all of them.
- **[E2-53], the dominance class:** *"Good or bad, it will prosper"* — Spotify has called itself *"the world's most popular audio
  streaming subscription service"* in every 20-F since FY2021, and UMG calls it *"the largest digital service provider"*;
  **at that position it did not prosper** — operating losses in 2022 and 2023, and in seven of the eight filed years
  2016–2023; prosperity arrived with the 2023 cost cuts and the industry's price increases. Position did not set the economics; decisions did.

- **Class: [ ] WIDE [ ] NARROW [x] NONE [ ] PROVISIONAL · Direction: margins widening since 2024 on a split its
  licensors renegotiate; subscriber growth decelerating.**
- **VERDICT: [x] OUT** — permanent, on the business as constituted, on **[E3-03] criterion (2)**, evidenced from the
  supplier's own words (*"DSP providers generally make all content available, thus not requiring multiple
  subscriptions"*), Spotify's filed switching and loss-leader risks, and a competitor's measured loss of subscribers to
  the same services; with **[E4-04]** (the product's basis is re-licensed every one to three years from owners who
  license it to every rival) and **[E3-43]/[E3-46]** (the price increases have not *"thereby"* produced high returns
  on capital over time: five-year mean ROE 3.6%, ten-year cumulative net loss). **The ask aloud: can I name the
  document that would change this?** The label licence agreements themselves — **not filed, confidential by
  contract** — would show the split's durability, but no document can show listeners thinking the same catalogue has
  no substitute when its owner says it is everywhere. **OUT, not UNKNOWABLE.**

*The strongest single fact against this verdict:* **Spotify has raised prices five years running across dozens of
markets, and net subscriber additions were positive in all 21 quarters since Q2 2021, while its gross margin rose
twelve points** — the pattern [E2-44](1) describes. The reply is in the row: the rivals raised too, the licensors
asked for it and take half or more of it, and the record of *high returns on capital over time* that [E3-43] attaches
to that pattern is two years long.

*Added to the row in the same run, after the sub-agent's Deezer section closed (it did not exist when the verdict above
was committed; nothing above is changed by it):* **Deezer** (Euronext Paris, rung 3, English free translation of the
Universal Registration Documents from deezer-investors.com): subscribers **9.6M (2021) → 9.1M (2025)**; revenue **€400.0m →
€534.0m**; IFRS gross profit ÷ revenue **12.1% → 27.2%** (COMPUTED); operating income **€(120.6)m → €9.3m**. It pays labels
*"an amount equal to the label's "market share" of certain content streamed on Deezer's platform multiplied by a percentage
of all subscription revenue received"*, offers *"a full‑range catalog of high‑quality music, from essentially all labels,
distributors and aggregators across the world"*, and says of prices: *"Deezer … was the first major music streaming platform
to raise prices globally. This move resulted in minimal subscription cancellations. Since then, all other major global
platforms have followed"* (URD 2025, pdf pp.15, 19–20, 28). **A service with 3% of Spotify's subscribers raised prices with
"minimal subscription cancellations" too** — which makes price increases without churn a property of the category and its
shared catalogue, not evidence that Spotify alone has no close substitute. It strengthens the Q2 reading; it changes no
verdict. Row count, confirmed: **6 peers** (TME, Pandora, Deezer, Apple Music, YouTube Music, Amazon Music), three of them
undisclosed, plus 3 suppliers.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

⛔ **Q3, Q4 and Q5 do not open for entry.** Q1 IN · Q2 OUT. Everything below is **RECORDED, NOT GOVERNING**, and the price
at Q5 is headed **COMPUTATION — NOT A CLEARANCE** (operator rules 2 and 3).

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business as constituted).
*Hard sequence (operator protocol 2): nothing below can reopen the file, and a strong Q3 could not have repaired Q2
[E2-37, E2-38, E3-39]. The record is kept because the queue's instruction asks every run for the whole file and a price.*

**STEP 1 — DECLARE THE WEIGHT CASE. Nothing below counts until this is filled in.**
*How much damage can this manager do before I can react?*
- [x] **Daily execution** — have-to-be-smart-every-day **[E3-38]**, with the 1977 root **[E2-70]**: the product sold is
  the same catalogue every rival sells (Item 4.B: the licences *"apply worldwide"*; TME: *"on a non-exclusive basis"*),
  so what separates the services is product, pricing and negotiating conduct renewed every quarter and every licence
  cycle. And by the 1991 original **[E3-43]**, *"a business, unlike a franchise, can be killed by poor management"* —
  **Q2 found no franchise, so the gate case follows from the corpus's own rule, not from a preference.**
- [ ] **Control** — you own the whole thing and cannot exit **[E1-16]**: not ticked (a listed minority can exit), but
  recorded: the founders hold **69.3% of the votes on 15.1% of the capital**, the board they sit on may issue up to
  **1,400,000,000** further beneficiary certificates *"without reserving to our existing shareholders a preemptive
  right"*, and Ek votes Tencent's 8.1% by irrevocable proxy while Tencent votes Spotify's 9% of TME (TME 20-F FY2025,
  Item 6.E: *"Spotify has given Tencent a sole and exclusive right to vote our securities beneficially owned by
  Spotify"*). **A public owner cannot change a manager here; only exit remains.**
- [ ] **Leverage** — none: no borrowings since 2026-03-15.

**Case declared: GATE (daily execution, in a business the corpus says management can kill [E3-43]).**

**Honesty — binary, permanent, filings-based [E5-16].** Every matter dated to when it became public:
- **Ferrick et al. v. Spotify USA** (S.D.N.Y. 2016; settlement final April 2019): *"alleged that Spotify USA Inc.
  unlawfully reproduced and distributed musical compositions without obtaining licenses"* (Note 21). A copyright
  licensing failure of an operating kind at scale, settled; the 20-F records the related *Eight Mile Style* suit
  dismissed in December 2025. **Not personal misconduct.**
- **Mechanical Licensing Collective v. Spotify USA** (filed 2024-05-16; dismissed with prejudice 2025-01-29; amended
  complaint 2025-10-01): *"alleging that … Spotify USA Inc. improperly reported and underpaid royalties for its Premium
  Service as a bundle"*; worst case *"approximately € 358 million, plus potential penalties and interest"* (Note 24).
  The court held *"the Premium Service is a bundle"*. **A dispute over a regulatory classification Spotify chose and
  disclosed with its worst case quantified — the [E2-26] direction, not concealment.** Recorded, open.
- No SEC enforcement, no restatement (20-F cover: the error-correction box unticked), no auditor change found (*"Ernst & Young AB have acted as our principal accountants for the years ended December 31,
  2025 and 2024"*; internal control reported effective), no founder related-party taking found: Ek *paid* €31m for his 2021 warrants (Note 25). Sweep of Notes 21, 24,
  25 and Item 8: no other matter.
- **Finding: no integrity disqualifier found.** *Written as the corpus requires [E5-17]: the absence of found
  disqualifiers, not a finding that the managers are honest.*

**STEP 2 — THE FLAGS [E4-22, E5-15, E4-29, E4-30, E3-48, E2-49, E2-57, E3-53].** *Each a prompt to READ, never a
verdict [E5-36, E5-38].*
- [ ] **weak accounting** — not fired. SBC is expensed (€247m), the share-linked social charges are expensed and
  quantified quarterly, no pension, no capitalised development of size (capex €61m).
- [ ] **unintelligible footnotes** — not fired. The royalty mechanics, MFN clauses, minimum guarantees and the MLC
  exposure are explained in plain terms, with amounts.
- [x] **trumpeted earnings projections / growth targets — FIRES.** A quarterly guidance culture since the listing (MAUs,
  subscribers, revenue, gross margin, operating income, every quarter), and **long-term goals set at a 2022 Investor
  Day that every release from Q3 2023 to Q3 2024 refers back to** (*"well positioned to deliver on the goals outlined at
  our 2022 Investor Day"*, 6-K 2024-04-23). **The goals are not in any SEC filing** (no 6-K between 2022-04-27 and 2022-07-27), so the transcript was fetched from the
  company's IR site (rung 3; `investor_day_2022_transcript.pdf`, from the link on investors.spotify.com/investor-day-2022/) and
  **set against outturn [E3-48]**: *"our long term goals of 25-35% revenue growth and a gross margin target of 30-35%"* (the 2018
  framework, restated) — revenue grew **29%, 17%, 23%, 21%, 13%, 18%, 10%** in 2019–2025, inside the band in one of seven years (2019);
  *"Our goal continues to be to deliver 20% plus revenue growth over the long term"* — **13%, 18%, 10%** since; *"we believe 2022
  will be the peak in terms of the negative impact on Gross Margins, with podcast Gross Margin turning profitable over the next 1-2
  years"* — podcast margin is not separately filed, but Ad-Supported gross margin was **4% in 2023** and the podcast business was
  restructured that year; *"we expect our consolidated gross margin to top 30% during this timeframe"* (3–5 years) — **met: 30.1% in
  2024**; the founder's *"over the next decade, we will be a company that can generate $100 billion in revenue annually, and that we
  can achieve a 40% gross margin and a 20% operating margin"* — **€17.2bn, 32.0% and 12.8% in 2025**, needing about 26% a year to 2032 at today's
  ECB rate (COMPUTED). **[E4-35]'s base rate is the reply to the last sentence.** The quarterly record *is* on file
  and was read (the "Actuals vs. Guidance" table in every release since Q2 2022): **subscribers at or above guidance in 17 of 17 quarters, Q2 2022 – Q2 2026, by 0 to 3 million** (in-line in Q1 2024,
  Q3 2025 and Q1 2026); **MAUs below guidance in Q1 2024 (615 vs 618), Q2 2024 (626 vs 631) and Q2 2026 (777 vs 778)**;
  **operating income below guidance in Q3 2022, Q2 2023 (IFRS; the release headlined "Adjusted Operating (Loss)/Income
  … Above"), Q1 2024 (168 vs 180), Q4 2024 (477 vs 481), Q1 2025 (509 vs 548) and Q2 2025 (406 vs 539)** — every
  2024–2025 miss footnoted to *"Social Charges which were €58 million higher than forecast"*-type share-price effects or
  *"€104 million of incremental headwinds … due to unfavorable currency movements"*. A record of guidance set to be met.
- [x] **serial share issuance [E5-15] — FIRES, moderately.** Outstanding shares **167,258,400 (2017) → 180,856,081 (2018)
  → 190,212,847 (2020) → 205,832,527 (2025)**: +8.2% over the five-year default **after €530m of buybacks**, funded by
  option exercises (proceeds €1,881m 2021–2025) and RSU releases; SBC was €223–381m a year 2021–2023 and **exceeded
  operating cash flow in 2022 (€381m vs €46m)**.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29] — not current; fired historically.** The shareholder updates of
  2019 and 2020 carried *"the non-IFRS financial measures of EBITDA and Free Cash Flow"*; EBITDA was dropped in the
  2021 updates (sweep of all 24 updates on disk: zero EBITDA mentions from 2021-02-03 onward). **"Adjusted Gross
  Margin" (Q2 2022) and "Adjusted Operating Income/(Loss)" (Q2 2023 – Q4 2023) were introduced in the quarters of
  the Car Thing write-down and the restructuring, and dropped once IFRS operating income was positive (none from
  2024-04-23 on).** Today's non-IFRS set is constant-currency revenue and free cash flow only.
- [x] **[E2-49] metric-switching — FIRES as a prompt, on that same sequence.** The adjusted measures arrived *with* the
  deterioration (*"Excluding €143 million in charges associated with efficiency actions … we generated €68 million in
  Adjusted Operating Income"*, 6-K 2024-02-06) and left with it; and **effective 2026-01-01 revenue was moved from
  Ad-Supported to Premium** (*"to reflect changes in the financial information presented to the Group's new Co-Chief
  Executive"*, 6-K 2026-08-04) as Ad-Supported revenue fell 1% in 2025 and 5% in Q1 2026. The reclassification was announced
  with reasons and recast comparatives (6-K 2026-04-28: *"See Appendix for reclassified and recast segment Gross Profit
  amounts"*), which is the candor case [E2-49] carves out; the 2023 adjusted measures were not.
- [x] **[E2-57] except-for — FIRES, mildly.** Every miss is narrated around a cost the company chose: *"As a reminder,
  we do not incorporate share price movements into our forecast since they are beyond our control"* — the share-price
  sensitivity of the charge is a consequence of paying in equity. Both directions are reported (Q4 2025: *"€67 million
  below forecast"*), which limits the flag.
- [ ] **[E3-53] restructuring charge — read, not fired as a "big bath".** 2023's €212m severance and €123m real-estate
  impairment are itemised by line (Note 5, Note 23) and were not reversed later; the charges belong in the
  owner-earnings mean [E5-33], and Q4 keeps them there.
- [x] **filed-figure tells [E4-30] — cash tax fell as a share of pretax income: prompt read, explained.** Cash tax
  paid / income before tax **4.0% (2024), 3.9% (2025), 7.3% (H1 2026)**. Note 8 explains it: loss carry-forwards
  (*"United States of € 958 million"*), recognition of deferred tax assets (*"additional deferred tax benefit of
  approximately €159 million"*), and the *"acceleration of the deduction of the previously capitalized and unamortized
  domestic research and development costs in the United States"*. **Explained by the filing, and finite** — Q4
  normalises it. Subscriber beats of 0–3 million for sixteen quarters are smooth; **no filed evidence of engineering
  was found**, and the metric's definition (grace periods, family sub-accounts) is disclosed.

**STEP 3 — THE PRIMARY TEST [E2-01].** Return on average equity, net income attributable to owners over average
equity attributable to owners (20-F balance sheets):

| | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| Net income (€m) | (186) | (581) | (34) | (430) | (532) | 1,138 | 2,212 |
| Average equity (€m) | 2,066 | 2,421 | 2,462 | 2,260 | 2,462 | 4,024 | 6,927 |
| **ROE** | **(9.0)%** | **(24.0)%** | **(1.4)%** | **(19.0)%** | **(21.6)%** | **28.3%** | **31.9%** |

**Five-year mean 3.6%; cumulative net income 2016–2025 a LOSS of €265m; cumulative operating income 2016–2025 €1,416m,
€3,563m of it in 2024–2025.** *Scoped as the corpus scopes it [E2-47, E2-43]:* equity here is mostly cash (€9.4bn
liquidity against €8.4bn equity at June 2026) and the operating assets are negative (working capital is supplied by
licensors and subscribers), so a return on *unleveraged net tangible operating assets* is not meaningful — it is
infinite in the good years and undefined in the bad. **The honest reading of [E2-01] is the time series itself: eight
years of negative returns, then two strongly positive.** [E4-41]: the two positive years carry near-zero cash tax.

**The half-owner test [E2-26]:** the 20-F quantifies every one-time item at its line (Note 5 severance by function;
Note 23 segment charges; the MLC worst case in euros). **One direction runs the other way: churn.** The shareholder
updates reported the Premium churn *direction* every quarter from 2019 to Q3 2021 (*"Our average monthly Premium churn
rate for the quarter was down 23 bps Y/Y"*, 6-K 2021-07-28) and **no update from 2022 onward states it** (sweep: the
only later "churn" hits are Russia's involuntary disconnects and Ad-Supported MAU churn). The disappearance precedes
the price increases of July 2023. **It is exactly the fact a half-owner would want reversed-positions** — whether the
price increases cost subscribers — and the filer stopped volunteering it. Recorded as a candor prompt, not a finding:
the 20-F never carried a churn figure.

**The institutional imperative — score all four [E2-30].** *Not a fraud test.*
- [ ] resists change in current direction — **not fired, and the counter-evidence is filed**: in 2023 the company cut
  headcount by about 6% (January) and 17% (December), wrote off content, merged its studios (*"strategic realignment
  and reorganization plan focusing on podcast operations and rationalizing our content portfolio"*, Note 5).
- [x] **projects/acquisitions materialise to soak up funds — FIRED, 2019–2022.** The Q4 2018 update, the first after the
  listing: *"We want to acquire more, and have line-of-sight on total spend of $400-$500M on multiple acquisitions in
  2019."* Cash paid for businesses: **€331m (2019), €336m (2020), €115m (2021), €306m (2022) = €1,088m**, named in the
  notes: Anchor €136m, Gimlet €172m, Parcast €49m (2019); The Ringer €170m, Megaphone €195m (2020); Betty Labs €57m,
  Podz €45m (2021); Findaway €117m, Sonantic €93m (2022).
- [ ] staff studies to justify the leader's craving — no filed evidence either way.
- [x] **peer behaviour imitated — prompt.** Live audio (Betty Labs, *"to explore the live audio space"*), audiobooks
  (Findaway), video podcasts (the Partner Program) each follow a rival's category; **the prompt is noted, the
  judgment is not made**, because several have become Premium features rather than stand-alone bets.

**Capital allocation — the camouflage test [E2-56] and the post-mortem tell [E4-39].** The podcast programme is the
record: €1,088m of acquisitions plus content spending charged to Ad-Supported cost of revenue, **in the years
Ad-Supported gross margin was 1% (2020), 10% (2021), 2% (2022), 4% (2023)**, while Premium's 27–29% carried the
consolidated figure. **Goodwill is tested at the level of the two reporting segments** (*"Goodwill is allocated to the
Group's two operating segments, Premium and Ad-Supported"*, Note 12) and **no goodwill impairment has ever been
recognised** (20-F FY2021–FY2025: *"no impairment charges for goodwill"*) — Gimlet, Parcast and Betty Labs' live-audio
product were absorbed or closed inside a unit too large to fail a test. **That is SONY's CAMOUFLAGE in accounting
form**: the base business hides the bet. The 2023 realignment is a partial candid reversal; **no filed review of an
acquisition against its announcement case was found** [E4-39].

**Capital allocation — the two buyback conditions [E5-08, E4-31]:**
- (1) ample funds for operations and liquidity? **Yes** — €9.4bn liquidity, no debt.
- (2) repurchases at a **material discount** to conservatively calculated IV? **Price paid, from the notes:** 2018–2019
  program 4,366,427 shares for ~US$572m (**~US$131**); 2021–2022, 469,274 for €91m (**~€194**); **2025, 768,223 for
  US$510m (~US$664)**; **H1 2026, 1,349,216 for US$638m (~US$473)**; the Board added US$1.5bn on 2026-08-20. **Against
  Q5's computation below, the 2025 and 2026 purchases sit far above every conservative value this file can build
  → CAPITAL ALLOCATION FLAG on condition (2)**, stated with the humility clause **[E4-13]**: *"it is natural for CEOs
  to be optimistic about their own businesses. They also know a whole lot more about them than I do"*; and the
  purchases also offset dilution from €1.9bn of option exercises, which is not the [E5-08] purpose. **Binds position
  size, never the discount rate.**
- [E4-31]'s third condition — shareholders given what they need to estimate value: **weakened by the churn silence
  above and by the royalty terms being unfiled** (confidential licences).

**Pay and what it vests on [E4-27] — incentives.** Ek has taken *"no base salary"* since July 2017 and no bonus since
2018; his 2025 compensation is US$694,484 of security costs. The Co-CEOs (from 2026-01-01) received **US$13.9M each in
2025**, of which **US$13.4M in options and RSUs**; employees choose among *"at-the-money stock options, out-of-the-money
stock options with a closing price equal to 150% of the closing price"*, RSUs or cash, **vesting monthly over four
years *"subject to continued employment"*.** Sweep of Item 6 for "performance-based", "performance conditions",
"performance goals": **no instance found** — the equity vests on time and pays on the share price. **What the pay
rewards is the quote.** No annual cash bonuses (*"we believe they do not incentivize the long-term growth"*), but
one-time retention bonuses of US$1,664,000 to each future Co-CEO in March 2024.

**Where the flags converge — [E4-52] lollapalooza, read.** Four prompts point the same way: **pay vests on the share
price; guidance is set to be beaten and misses are narrated as share-price effects; buybacks were made at ~US$664
near the top of the range; issuance continues underneath them.** That is a system organised around the quote, which
**[E3-50]** names (*"the highest stock price possible (a premise with which we adamantly disagree)"*) — **but the filed
counterweights are real**: no EBITDA, adjusted measures dropped, one-time items quantified, the MLC worst case stated,
and a founder who takes no salary. **But the founders sold while the company bought:** between the 20-F ownership tables at
2024-12-31 and 2025-12-31, Ek's direct holding fell **480,000** shares (D.G.E. Investments 12,473,298 → 11,993,298) and
Lorentzon's **1,001,582** (20,051,949 → 19,050,367), and their beneficiary certificates fell **14,800,000** (cancelled on
transfer, ten per share) — **about 1.48 million shares out, against 768,223 bought back by the company in 2025.** Sale
prices are not in the filing (a foreign private issuer's insiders file no Section 16 reports). **The convergence is recorded as a live
capital-allocation and incentive flag, not as a venality finding [E5-38].**

**THE GUARDRAIL — check before writing the verdict.**
- [x] Confirmed: nothing in this Q3 is used to **promote** the name **[E2-37, E2-38, E3-39]**. The 2023 cost reset and
  the price increases are a manager's competence; they cannot repair Q2.
- [x] Key-person: the founder moved to Executive Chairman on 2026-01-01 and two Co-CEOs took over; **no
  single-surgeon dependence is recorded at Q2**, because the franchise question failed on the product, not the person.
- [x] Is the franchise intact and the damage excisable, or is the manager the plan **[E2-35, E2-36]**? **The manager is
  the plan**: the 2024–2025 economics came from the manager's price and cost decisions within licences the manager
  does not control.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN (no integrity disqualifier found)  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE**
  — with a **live capital-allocation flag** (2025–2026 buybacks above every value this file computes, while the founders
  sold about 1.48M shares), the **podcast camouflage** of 2019–2023, a **quarterly guidance culture** measured against its
  2018 and 2022 long-term goals (revenue growth missed; consolidated gross margin met), and **converging flags around the
  share price [E4-52]**. *IN = no disqualifier found, not a finding of honesty [E5-17]; IN never promotes.*

## Q4 — WILL IT SURVIVE?

### ⚠ RECORDED, NOT GOVERNING — the file closed at Q2 (OUT, on the business as constituted).

### Owner earnings — the one number **[E2-23]**
> "(c) **the average annual amount** … that the business **requires to fully maintain** its
> long-term competitive position and its unit volume. (… the working capital **increment
> also should be included in (c)**.)" … "**(c) must be a guess**."

**Built from the filed cash-flow statements, never from net income (operator rule 5).** Inputs by year, € million,
from the consolidated statements of cash flows of the FY2025 20-F (2023–2025), FY2022 20-F (2020–2022), FY2019 20-F
(2017–2019) and FY2018 20-F (2016), each cross-checked to XBRL companyfacts (`ifrs-full`, EUR; every vintage of
OCF, SBC, capex, depreciation and amortisation agrees with the filed statement; `vint.py`). Arithmetic in `oe.py`,
output `oe_out.json`.

| Year | OCF | SBC | (c) capex + lease principal | (c) D&A | working capital inside OCF | Δ accrued social costs (options, RSUs) | **OE, high end** | **OE, low end** |
|---|---|---|---|---|---|---|---|---|
| 2016 | 101 | 53 | 27 | 38 | +300 | — | 21 | **(290)** |
| 2017 | 179 | 65 | 36 | 54 | +420 | — | 78 | **(360)** |
| 2018 | 344 | 88 | 125 | 32 | +251 | (23) | 247 | **(120)** |
| 2019 | 573 | 122 | 152 | 87 | +451 | 0 | 364 | **(152)** |
| 2020 | 259 | 176 | 102 | 111 | +317 | +105 | **(124)** | **(345)** |
| 2021 | 361 | 223 | 120 | 127 | (36) | (85) | 103 | 47 |
| 2022 | 46 | 381 | 68 | 171 | +191 | (77) | **(326)** | **(697)** |
| 2023 | 680 | 321 | 72 | 158 | +464 | +50 | 237 | **(263)** |
| 2024 | 2,301 | 267 | 86 | 121 | +376 | +160 | 1,788 | 1,537 |
| 2025 | 2,933 | 247 | 134 | 102 | +248 | 0 | 2,584 | 2,304 |
| *H1 2026 (6-K)* | *1,652* | *142* | *61* | *55* | *+118* | *(75)* | — | — |

*High end = OCF − SBC − the lower of the two (c) guesses − the increase in the accrued social-cost liability. Low end =
OCF − SBC − the higher of the two (c) guesses − the whole working-capital inflow. Lease principal is added to capex
because IFRS 16 moved it from operating to financing cash flow in 2019 (*"Payments of lease liabilities"*: 17, 24,
35, 43, 66, 69, 73); the D&A line already includes right-of-use depreciation. Working capital is the sum of the four
filed lines (receivables, trade and other liabilities, deferred revenue, provisions).*

**MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE [E4-25].**

| Window | high end | low end | low end, cash tax normalised |
|---|---|---|---|
| **Five-year default [E2-42], 2021–2025** | **877** | **586** | 444 |
| Three-year, 2023–2025 | 1,536 | 1,193 | 956 |
| Two-year, 2024–2025 | 2,186 | 1,920 | 1,564 |
| Ten-year, 2016–2025 | 497 | 166 | 95 |

*Normalised cash tax: the 2024 and 2025 cash tax paid (€53m, €86m) replaced with the Luxembourg statutory 23.87% on
operating income (€326m, €525m), i.e. €273m and €439m subtracted; 2021–2023 had operating losses or near-zero
income and are not adjusted. The note that licenses it is Note 8: tax loss carry-forwards of **€1,163m** (*"United
States of € 958 million"*) and the Q2 2026 6-K's effective rate of **23.6%** for the half. It is [E4-41]'s instruction
applied: a favourable, finite break (losses and share-deduction shields) named and removed before the mean is
trusted.*

- **Short-window mean** (2024–2025): **€1,920m–€2,186m** (tax-normalised low €1,564m)
- **Long-window mean** (2016–2025): **€166m–€497m**; the five-year default (2021–2025): **€586m–€877m**
- **Spread, conservative end:** the two-year low end is **11.6×** the ten-year low end and **3.3×** the five-year low end.
- **Combined range** (window spread × (c) band × working capital × tax): **€95m to €2,186m.**
- *Is that range too wide to reach a conclusion?* **Yes, on the corpus's own test [E4-25]** — *"Usually, the range must
  be so wide that no useful conclusion can be reached."* The width is not the (c) guess (the two (c) constructions
  differ by at most €103m in any year); it is **the regime inside the window**. Spotify earned owner earnings above
  €400m in **two of ten years**, and both are the two most recent.
- *A wide spread is also a Q4 finding* **[E5-11]**. **Named distortions inside the window:** (1) **2023's restructuring**
  — €212m severance (Note 5), €123m real-estate impairment, €29m content write-off (cash-flow statement), the 17%
  headcount cut announced 2023-12-04, in the year before the step-change; (2) **the price increases from July 2023**
  (ARPU bridges: +€0.15, +€0.49, +€0.25, +€0.45 for 2023, 2024, 2025, H1 2026); (3) **the royalty share falling**
  (Premium CoR 71.2% → 66.3%, Q1); (4) **2022's SBC of €381m exceeding OCF of €46m** — the year the business paid its
  people in shares and the owner earned nothing; (5) **working capital supplied €2,982m of the €7,777m of OCF
  generated 2016–2025 (38%)** — the royalties owed and the subscriptions paid in advance grew with the business, and
  would reverse if it shrank.
- **Owner earnings by year:** above. **Years negative:** high end **2020, 2022**; low end **2016–2020, 2022, 2023**
  (seven of ten).
- **Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT.** **D&A default VALID [E3-44, E2-41]**: the business
  is capital-light (PP&E €188m against €17.2bn revenue; capex €6m–€135m a year), nothing in the filing says
  depreciation understates renewal, and the two constructions agree within €103m every year. **Not in the [E5-20]
  exception class.** Band used: capex plus lease principal vs D&A; **(c) does not move any verdict** — the working
  capital, the window and the tax do.
- **Stock compensation subtracted in full [E5-06]: RESOLVED and COMPLETE.** SBC resolves for **every year 2016–2025**
  from the cash-flow statement line *"Share-based compensation expense"*, matching Note 17's expense table (2025: cost of
  revenue 5 + R&D 138 + S&M 62 + G&A 42 = 247) and XBRL `AdjustmentsForSharebasedPayments`. The 2023 figure is **net of
  a €48m forfeiture credit** from the reorganisations (Note 17), left in as filed. **[E3-70]**: the IFRS 2 charge is
  the grant-date fair value (Black-Scholes for options), which is the market-value measure the corpus asks for at the
  moment of grant; **it is carried as the floor**, and the dilution it did not capture is stated at Q3: outstanding
  shares **190,212,847 (2020) → 205,832,527 (2025), +8.2%**, while €530m was spent on buybacks.
- **The social costs on share-based pay — RESOLVED, COMPLETE, and how they are treated.** Spotify books them inside
  operating expenses, not inside SBC: Note 5 *"Social costs and payroll taxes | 311 | 444 | 254"* (2025, 2024, 2023;
  85 and 85 in 2022 and 2021), of which the share-linked part is disclosed only in the shareholder updates — *"Social
  Charges are payroll taxes associated with employee salaries and benefits in select countries where we operate. Since
  a portion of these taxes is tied to the intrinsic value of share-based compensation awards, movements in our stock
  price can lead to fluctuations"* — quarter by quarter: **2024: €82m + €59m + €54m + €96m = €291m; 2025: €76m + €116m
  − €16m − €50m = €126m; Q1 2026 (€39m) credit** (6-Ks 2024-04-23 to 2026-04-28). The balance sheet carries the unpaid
  part: *"Accrued social costs for options and RSUs"* **87 (2017), 64, 64, 169, 84, 7, 57, 217, 217 (2025), 142 (June
  2026)** (Note 20 each year; 6-K Q2 2026 Note 17). **Treatment:** the charge is a real payroll tax, **already inside
  OCF as an expense and never added back**; OCF therefore reflects the *cash paid*, and the change in the accrual sits
  in working capital. **At the high end the accrual build is subtracted** (owner earnings bear the tax as *earned* at
  period-end share prices, not as paid — €160m in 2024); **at the low end it goes out with all working capital.**
  Over the five-year default the accrual rose a net **€48m** (−85, −77, +50, +160, 0), so the choice moves the
  five-year mean by under €10m a year. **Nothing here is added back as "non-cash"; nothing is counted twice.**
- **Not subtracted, and why:** *"Payments for employee taxes withheld from restricted stock unit releases"* (€241m in
  2025, financing) — the cash cost of net-settling RSUs, i.e. buying back the shares that would otherwise dilute;
  the SBC charge already expenses the award, so subtracting both would count it twice. Recorded at Q3 with the
  buybacks. Interest received (€242m in 2025) is left inside OCF; Q5 therefore sets these owner earnings against the
  **whole** cap and shows the enterprise version separately, never mixing the two.
- *If the capex band changes the verdict → **UNKNOWABLE**.* It does not.

### Great, good, or gruesome? **[E4-20]**
- [ ] great — high return, rising, little capital needed
- [ ] good — attractive return, earned also on added capital
- [ ] gruesome — grows, eats capital, earns little
- **Evidence — not gruesome, and not yet provably great.** **Capital:** growth needed none. Revenue rose **€2,952m →
  €17,186m (2016–2025)** on PP&E that is **€188m** and capex that fell to **€6m** in 2023; working capital is
  negative and *funded* growth (+€2,982m over ten years). Acquisitions were the only capital consumer — **€1,088m in
  cash 2019–2022** (Q3). So it is the opposite of the airline [E4-20]: growth did not require money. **Return:** the
  rate on that growth was **nil or negative for eight of ten years** (owner earnings, high end, averaged €75m a year
  2016–2023 on revenue averaging €7.7bn) and **€1.8bn–€2.6bn in 2024–2025**. The "great" account *"pays an
  extraordinarily high interest rate that will rise"*; Spotify's rate has risen for two years, on a split its
  licensors set (Q1, Q2). **Classified: great in capital need, unproven in rate.** The corpus's scope [E4-43] does
  not fail it; the rate is the open question, and it is a Q2 question.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — HALF.** Large now (2025 OCF €2,933m; H1 2026 €1,652m, +32%);
  **reliable, no**: two positive-owner-earnings years above €400m out of ten, and the stream is a residual after a
  royalty formula Spotify does not set.
- **(2) massive liquid assets — PASS.** **€9,388m** of cash and short-term investments at 2026-06-30 (6-K), plus the
  TME stake (€1,118m, listed); **no borrowings** since the Exchangeable Notes were repaid on 2026-03-15 (€1,304m cash).
  Against 2025 operating expenses of €3,298m it is 2.8 years of opex.
- **(3) no significant near-term cash requirements — PASS.** Within one year (2026-06-30 unless stated): **minimum
  guarantees €979m** (Note 21, 6-K Q2 2026), purchase obligations **€626m** (Dec 2025), lease payments **€98m**
  (Dec 2025), RSU tax on unvested awards **€254m over 2026–2029** (Note 17), uncertain tax positions **€100m** (6-K),
  the **MLC claim's stated worst case €358m** *"plus potential penalties and interest"* (Note 24). **Sum of every
  named item above, taking the four-year RSU tax and the MLC worst case whole, ≈ €2.4bn against €9.4bn of liquidity — about 3.9×.** The one
  liability that would come due all at once in a decline is the working-capital float — accrued fees to rights
  holders **€1,971m** and deferred revenue **€778m** (June 2026) — and it is covered 3.4× by liquidity alone.
- **Leverage, named and quantified [E4-16, E3-29]:** no debt; lease liabilities ~€466m (404 non-current + 62 current);
  **the float owed to rights holders (€1,971m) is covenant-free and paid in the ordinary course [E3-52]**, but it is
  owed to the same concentrated licensors who set the rent. [E2-54]'s coverage test: there is no interest to cover.
  **[E3-66], where shareholders stand:** a Luxembourg société anonyme with its operating company in Sweden; the
  founders hold **69.3% of the votes on 15.1% of the capital** through non-economic beneficiary certificates that the
  board may issue up to 1,400,000,000 (Step 0) — the public owner stands behind the founders on every vote, though
  equal with them on every euro.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40, E4-51]**

*Modelled from exposure, not experience: 2024–2025 are the benign end of the filed record (price increases landed,
royalty share fell, headcount down 17%, share price up, cash tax near zero). A bear case its holders would accept
starts from what the filing shows the business is exposed to.*

**The mechanism, in four parts, each filed:**
1. **The rent is reset.** The owners of *"approximately 72% of streams of audio content delivered by record labels"*
   license on *"multi-year"* terms that *"are not automatically renewable"*; the royalty *percentage* already moves with
   Spotify's subscriber, free-to-paid and churn *"targets"*; and the risk factor says they *"may attempt to take
   advantage of their market power … to seek onerous financial or other terms."* **Quantified:** Premium cost of
   revenue returning from 66.3% (2025) to its 2018–2023 mean of **72.0%** on 2025's €15,350m Premium revenue removes
   **€874m** of gross profit — **34% of 2025's €2,584m high-end owner earnings**; to 2018–2019's 73.4%, **€1,078m (42%)**.
   The first puts owner earnings back at about 2024's level, the second below it. *Likelihood: a real possibility* —
   the share fell only in the two years that followed the price increases, and the licences that set it expire and
   are renegotiated (minimum guarantees due within one year fell from €3,021m at 2024-12-31 to €1,123m a year later,
   consistent with the big renewals having just been signed; the terms are not filed).
2. **The price stops rising while mix and currency keep subtracting.** Reported ARPU in euros was **€5.32 (2017) and
   €4.63 (2025)**; mix took **−€0.14** and currency **−€0.17** in 2025 alone. Without the **+€0.25** price effect, 2025
   ARPU falls 6.6% instead of 1% — and with a percentage royalty, every lost euro of ARPU costs Spotify about 34 cents
   of gross profit, not a euro. **The binding constraint is named in the filing: *"prominent, well-funded competitors
   like Apple, Alphabet, and Amazon … offer competitive services at little or no profit or even at a loss"*,** and
   a peer that could not hold its ground is on file (Pandora: self-pay subscribers **6.3M → 5.6M** and MAUs
   **52.3M → 41.1M**, 2021–2025, with *"We have not been able to negotiate or obtain lower royalty rates"* — SIRI
   10-K FY2025). *Likelihood: a real possibility.*
3. **The people take the owner's share, as in 2022.** SBC €381m against OCF €46m in 2022; €223m against €361m in
   2021. In a year when the price is lower, share-linked social charges fall and SBC's cash weight rises (more shares
   per euro of award). *Likelihood: a low-level possibility at 2025's margins; the shape ARM registered, in the years
   Spotify did not earn.*
4. **The float runs back.** €2,749m of royalties owed and subscriptions prepaid (June 2026) is a source of cash while
   subscribers grow and a use of cash when they shrink. *Likelihood: a low-level possibility*; liquidity covers it
   3.4× (above).
- **What survives all four: the company.** €9.4bn of liquidity, no debt, covenant-free float. **What does not survive:
  the rate.** None of the four threatens solvency; each threatens the owner earnings that exist in two years of ten.

**THE SURVIVAL SHAPE — tested against the twelve on the register.** Not ORCL (contracted not to stop: the minimum
guarantees are €2.3bn against €9.4bn of liquidity, not a stop-proof obligation); ARM (earns nothing for owners after
paying its people) **fits 2016–2023 and not 2024–2025** — a past state, not the named death; not BE (ten filed years,
not too few — though only two are profitable); not BA (no cash spent undoing past work beyond 2023's €212m severance);
not SWK (no dividend); **ACVA/FLNC/NEGG (the borrowed balance sheet)** — 38% of ten years' operating cash came from
customers' prepayments and licensors' unpaid royalties, **but the balance sheet is not needed to survive** (liquidity
3.4× the float), so the shape is present and not the death; not CNR (no long tail); not RGTI (the equity is not the
revenue: option proceeds were €1.9bn 2021–2025 but operations fund themselves since 2023); not BAM (no warehouse);
**SONY's CAMOUFLAGE** is present in capital allocation (the podcast studios' goodwill tested inside two
segment-wide units — Q3) but is not how the business dies; **TM's PASS-THROUGH** is the nearest — gains passed through
to input costs — **but its mechanism is a capex race [E2-27] that Spotify does not run: nothing here is spent to keep
unit volume, and the pass-through is contractual, to named suppliers, at renewal;** not TSM's ADDRESS.
**A THIRTEENTH SHAPE, NAMED: THE TENANT.** A business whose only product is **rented, non-exclusively, from a few
landlords who rent the same product to every rival — including rivals who do not need to earn anything on it — and
who reset the rent at each renewal, with the rent contractually indexed to the tenant's own success.** It owns the
customer relationship and none of the thing the customer buys. It does not die of insolvency or of capex. **It dies
of the lease: the owner's return is whatever margin the landlords leave, and every gain in scale, price or retention
is partly written into the next rent.** Its record is the filed one: eight filed years (2016–2023) of operating losses but one, at 71–78 cents of
rent per Premium euro, and two years of profit at 66–68.
- Likelihood: [ ] likely [x] **a real possibility** (mechanism 1 and 2) [ ] a low-level possibility

- **VERDICT (RECORDED, NOT GOVERNING): [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE** → **on the owner-earnings range,
  not on survival.** *It survives*: strengths (2) and (3) pass with room (€9.4bn liquidity, no debt, every named near-term
  requirement covered about 3.9×). *But the one number cannot be stated*: **€95m to €2,186m across windows, (c), working
  capital and tax — a 23× range** — and [E4-25] says a range that wide *is* the conclusion. **Can I name the document that
  would resolve it?** The major-label licence agreements that set the split for the next renewal cycle; **they are
  confidential and not filed**, so no fetch closes it: UNKNOWABLE, not UNRESEARCHED. Named death: **THE TENANT** (proposed
  thirteenth shape), a real possibility.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** Q2 is OUT (and Q4, recorded, would be UNKNOWABLE on the range). What
follows is arithmetic the queue's output contract requires (a price and a pass/fail line from every run), headed as
operator rule 3 requires.

---
## Q5 — **COMPUTATION — NOT A CLEARANCE**

**This section contains no entry language and confers no clearance. It is arithmetic.**

**The floor first [E4-28]:** *"that's the figure we quit on ... we don't want to buy equities where our real expectancy is
below 10 percent. Now, that's true whether short rates are 6 percent or whether short rates are 1 percent."* The EUR
sovereign (3.83%, ECB, 2026-09-10) is shown beside it; **the floor governs above both, and the choice of sovereign moves
nothing below.**

**The price, in the currency of the earnings.** US$525.75 (NYSE close 2026-09-11, Yahoo, aggregator flagged) ÷ **1.1592**
(ECB reference rate, 2026-09-11) = **€453.55** × **205,584,205** shares (6-K Q2 2026, `0001628280-26-052543`) = **market cap
€93,242M** (US$108,086M). Enterprise version: − liquidity €9,388M − TME stake €1,118M + lease liabilities €466M = **€83,202M**.

**1. THE YIELD** — owner earnings (Q4, recorded) ÷ the whole cap, and ex-interest ÷ the enterprise figure (`q5.py`,
`q5_out.json`). Values per share are converted back to US dollars at the same ECB rate so they sit beside the quote.

| construction (Q4) | OE €M | yield on cap | points vs EUR 3.83% | perpetual growth needed to reach 3.83% | **perpetual growth needed to reach 10%** | value/share at 3.83%, no growth | value/share at 10%, no growth | ex-interest yield on EV |
|---|---|---|---|---|---|---|---|---|
| ten-year low | 166 | 0.18% | −3.65 | 3.6% | 9.8% | $24 | $9 | 0.12% |
| ten-year high | 497 | 0.53% | −3.30 | 3.3% | 9.4% | $73 | $28 | 0.52% |
| **five-year default, low, tax-normalised** | 444 | 0.48% | −3.35 | 3.3% | 9.5% | $65 | $25 | 0.39% |
| **five-year default, low** | 586 | 0.63% | −3.20 | 3.2% | 9.3% | $86 | $33 | 0.56% |
| **five-year default, high** | 877 | 0.94% | −2.89 | 2.9% | 9.0% | $129 | $49 | 0.91% |
| three-year low | 1,193 | 1.28% | −2.55 | 2.5% | 8.6% | $176 | $67 | 1.21% |
| three-year high | 1,536 | 1.65% | −2.18 | 2.1% | 8.2% | $226 | $87 | 1.62% |
| two-year low, tax-normalised | 1,564 | 1.68% | −2.15 | 2.1% | 8.2% | $230 | $88 | 1.60% |
| two-year low | 1,920 | 2.06% | −1.77 | 1.7% | 7.8% | $283 | $108 | 2.03% |
| two-year high | 2,186 | 2.34% | −1.49 | 1.5% | 7.5% | $322 | $123 | 2.35% |
| *twelve months to June 2026, high (not a window; shown as the most generous figure on file)* | 2,959 | 3.17% | −0.66 | 0.6% | 6.6% | $436 | $167 | 3.30% |

*Growth needed: g = (target − y) ÷ (1 + y), the one-book engine [E3-34] converting a yield into a rate; it casts no vote.
The twelve-month figure is OCF €3,337m − SBC €274m − D&A €104m, before the social-cost accrual adjustment (the June 2025
accrual is not filed).*

**2. WHAT THE PRICE ALREADY ASSUMES.** **Every construction yields below the euro sovereign**, including the most generous
twelve months on file. To reach the **10% floor**, the price needs perpetual growth of **6.6% (the best twelve months) to
9.8% (the ten-year record)**, **7.5–7.8% on the two profitable years** and **9.0–9.5% on the five-year default**. What the
business has done: revenue **+22% a year** 2016–2025 (COMPUTED from €2,952m to €17,186m); owner earnings went from nil to
€2.2bn in two years, which is a level change, not a growth rate that compounds. **[E4-35]**: *"fewer than 10 of the 200 most
profitable companies"* sustain 15% EPS growth for twenty years; the floor case here needs 7.5–9.8% **in perpetuity**, from a
base whose split is renegotiated with its suppliers. **[E4-44]**: value *"cannot over the long term grow faster than its
earnings do."* **The ceiling [E2-63]:** the gross margin is bounded by the royalty formula, and the labels' filed aim is to
share in every price rise (WMG: *"greater certainty around our economic participation"*).

**3. WHAT YOU ARE PAID.** **−0.66 to −3.65 points against the EUR sovereign**; against the floor, 6.8 to 9.8 points short.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — *computation only*:
- **at the [E4-28] floor, no growth: roughly $10 to $170 a share** (five-year default about $25–50; two profitable years
  about $90–125; the best twelve months about $170)
- at the EUR sovereign, no growth (shown only as the most generous frame): roughly $25 to $440
- **current price $525.75 — above the whole range on every construction, in both frames.**

**WHICH BAR — computed for completeness:** Bar 2, the screamer test [E4-01]: the price is **above the whole range**, the
third outcome, *"no."* No margin applied. **Windage count: two places, both at the low end and justified in writing [E4-11]:** the
working-capital inflow removed and the cash tax normalised. Neither adds caution to a realistic input; each removes a
favourable, non-recurring cash source named in the filing [E4-41] (a float that grows only while the business grows; a
shield of €1,163m of loss carry-forwards that runs out). The high end carries neither, and the price is above both ends.

- **VERDICT: not reached — the file closed at Q2. This block is a computation, not a clearance.** For the queue's output
  contract: **price US$525.75 (€453.55); FAIL — closed at Q2 (OUT), and the price would also fail the [E4-28] floor on
  every construction (yields 0.2%–3.2% against 10%).**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

### ⚠ RECORDED, NOT GOVERNING — nothing is held, nothing is armed. These are the conditions under which the file would
### be reopened, written in advance [E1-02], in words, because a price alert on a Q2 OUT is a category error (the QLYS ruling).

**What would prove the Q2 OUT wrong — the evidence that would have to appear, and where:**
1. **Criterion (2) on the customers' side:** a filed figure showing Spotify holding price **above** the rivals selling the same
   catalogue (not in parallel with them) while subscribers still grow — e.g. a price increase that Apple Music, YouTube Music and
   Amazon Music do not follow for a full year, visible in WMG's or UMG's own lists of which services raised prices, with Spotify's
   net subscriber additions positive through it. **Disconfirming today:** Deezer's and WMG's filings show the rises were parallel.
2. **The split on the suppliers' side:** Premium cost of revenue staying at or below **66%** through the **next renewal of the
   major-label licences** (the minimum-guarantee maturity table, Note 24 / 6-K Note 21, will show when the current cycle ends:
   €979m due within a year at 2026-06-30), with the labels' 10-K/annual-report language changing from *"limited ability to increase
   our wholesale prices"* to something weaker. **A rise back above 70% would confirm the OUT and THE TENANT.**
3. **Returns on capital over time [E3-43, E3-46]:** a **five-year** mean ROE and owner earnings at the 2024–2025 level — the
   first five-year window with no loss year ends with **FY2028** (20-F due about February 2029). Until then the record is short.
4. **Churn disclosed again:** a filed Premium churn figure through a price increase. Its absence since 2022 is itself recorded.

**Thesis-confirming (for the OUT) and thesis-breaking metrics, pre-committed:**
- Confirming: Premium CoR ÷ Premium revenue rising back toward 71–73%; subscriber growth below 8% a year with price increases
  continuing; Ad-Supported gross margin back below 10%; a new wave of acquisitions to *"soak up"* the €9.4bn [E2-30].
- Breaking: items 1–3 above together, not singly.
- **Next catalysts:** Q3 2026 results 6-K (about early November 2026); FY2026 20-F (about February 2027); Copyright Royalty Board
  *Phonorecords V* (rates from 2028-01-01); the MLC amended complaint.

**The sell rule [E2-28]** — not applicable; nothing is held. **HOLD conditions** would be Q2, Q3 and Q5 restated, and all three
read against the name today (no franchise; a live capital-allocation flag; the market pricing it above every construction).
**Moat-downgrade monitoring [E4-17, E3-30]:** the question for a re-run is whether 2024–2026's margin is the start of a
permanent split in Spotify's favour or an aberration of one renewal cycle; **beliefs change quite gradually**, and one cycle is
not a record.

**Do not trim winners [E5-14]. Position size: zero** — a Q2 OUT is not sized.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN** — the reopening conditions are written, dated and tied to named documents; no
  band is armed, no PORTFOLIO row.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped — Q1 IN, **Q2 OUT (closes)**; Q3–Q6 recorded under explicit
      "RECORDED, NOT GOVERNING" banners; the price under COMPUTATION — NOT A CLEARANCE with no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 states the filing's one limit (no royalty
      total) and does not rest on the $11bn headline. Q2's OUT does not rest on the three undisclosed rivals.
- [x] Every UNRESEARCHED verdict names the artifact — none used. The one test first logged as a work order (the 2022 Investor
      Day goals, [E3-48]) was performed in the same run from the company's transcript (rung 3) before commit.
- [x] Every UNKNOWABLE verdict states what cannot be known — Q4 (recorded): the terms of the next major-label licence cycle,
      which are confidential and unfiled.
- [x] Step 0: the FY2025 20-F was read (Items 3.D in part, 4, 5 in full, 6 in part, 7.A, 8, 10 in part, 11, 16C; the
      statements; Notes 4, 5, 7, 8, 9, 10, 12, 16–27; Exhibit 1.1 Article 9), accession `0001628280-26-006874`; 20-Fs FY2018–FY2024
      for cash flows, segments, subscribers, ARPU, social-cost accruals, equity, acquisitions and ownership; the Q1 and Q2 2026 6-K
      interim reports; 24 shareholder-update 6-Ks 2019–2026; the AGM, buyback-upsize and board 6-Ks. **Cross-check:** 2025 OCF
      €2,933m = filed statement = MD&A table = Q4 2025 update = companyfacts.
- [x] Owner earnings on multi-year means; **four windows** (5-year default, 3, 2, 10) plus the twelve months shown only at Q5;
      (c) disclosed as a judgment, D&A default valid and not in the [E5-20] class; lease principal restored after IFRS 16
      (CONVENTION, stated); working capital removed at the low end; cash tax normalised at the low end; **SBC resolves and is
      complete every year 2016–2025; the share-linked social costs are found in both places (Note 5 and Note 20 accruals; quarterly
      amounts in the updates), kept inside OCF, and the accrual change subtracted at the high end.** Negative years named.
- [x] Competitor row filled: Tencent Music, Pandora/SiriusXM, Deezer with figures; Apple Music, YouTube Music, Amazon Music with the
      filings read and the non-disclosure quoted; three suppliers (WMG, UMG, Sony) with both sides' pricing-power language.
- [x] Sovereign for the earnings currency (EUR, argued from [E4-15, E3-32] on a 37.6%-US, 62.3%-rest-of-world revenue base; USD
      shown), from the issuing authority (ECB SDW, SR_30Y), dated 2026-09-10, struck fresh twice. **Cap converted to euros at the
      ECB reference rate of the quote date before meeting euro earnings; nothing mixed.**
- [x] Share count by hand: cover figure proven to be OUTSTANDING (issued − treasury); latest 6-K count used; beneficiary
      certificates read in the articles (no dividend, distribution or liquidation right) and excluded; options, RSUs, warrants (none)
      and Exchangeable Notes (repaid in cash) stated; no ADR.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar (screamer), computed only; windage count stated (two, justified).
- [x] Prices dated; aggregator used for live quotes only and flagged.
- [x] Ledger ids checked against `principle_ledger.csv` before splicing (all present); the quoted fragments of [E3-43], [E3-46],
      [E2-53], [E2-44], [E3-50], [E2-30], [E4-13], [E4-28], [E4-35], [E4-44], [E2-63] matched in the ledger text. [E4-27] used for
      pay, [E4-52] only for converging flags.
- [x] Run committed to git with a pathspec, section by section.

**Errors caught in this run before commit, recorded rather than hidden:** (1) Step 0 first wrote the founders' stake as "23.2% of
the capital"; that double-counts the Tencent shares Ek votes by proxy — corrected beside the line (15.1% economic). (2) Q4's first
draft put the 2018–2023 Premium cost-of-revenue mean at 71.4%; it is 72.0%, so mechanism 1 costs €874m (34%), not €783m (30%).
(3) Q4's first draft said high-end owner earnings averaged €54m a year 2016–2023; the arithmetic is €75m. (4) Q4's first draft
gave OCF 2016–2025 as €7,757m; it is €7,777m. (5) Q4's first draft summed the near-term requirements at €2.2bn and 4.3×; with the
four-year RSU tax taken whole it is €2.4bn and 3.9×. (6) Q4's first draft said ARPU without the price effect "falls 1.3% instead
of 1%"; it falls 6.6%. (7) The Q4 working note first said the five-year social-cost accrual change netted to −€12m; it is +€48m.
(8) Q3's first draft wrote that the founder "has not sold"; the two 20-F ownership tables show the founders' holdings fell by
about 1.48M shares in 2025 — rewritten. (9) Q3's first draft said revenue growth was inside the 2018 25–35% band in three of seven
years; it is one (2019). (10) Q2's first draft attributed the "65 countries" price sentence to WMG's FY2024 10-K; it is FY2023.
(11) Q2's first draft called Spotify "the largest subscription service throughout 2016–2023" without a filed source; replaced by
the 20-F's own words and UMG's. (12) Q5's first draft gave revenue growth of 17% a year; the nine-year rate is 22%. (13) Q5's first
draft counted windage at one place and called the working-capital removal the source's instruction; it is two places, justified.

**Brief and tooling defects found:**
- **Brief:** "the issued-versus-outstanding trap ERIC found" — **checked, does not fire**: Spotify's cover count is outstanding.
- **Brief:** "the SONY run has a music competitor row with UMG and WMG" — correct and reused; but **the label side's decisive
  sentence for criterion (2) is UMG's ("DSP providers generally make all content available"), not in the SONY file's summary.**
- **Brief:** "Tencent Music (files a 20-F)" — correct, but **companyfacts has ingested TME's FY2025 20-F for one dei fact only**
  (no FY2025 financial facts): the lag cause from RESUME STATE §9 is live for TME.
- **Brief:** asked for the social costs "which Spotify books separately" — **the 20-F does not itemise the share-linked social
  charge**; only the accrual (Note 20) and the total payroll-tax line (Note 5) are audited; the quarterly amounts are in the
  furnished updates. Stated, not smoothed.
- **Tooling:** `tools/run.py SPOT` → *"no overlapping OCF/D&A/capex annual facts"* although ten EUR IFRS years exist — the USD-unit
  filter and US-GAAP tag names (RESUME STATE §9), reproduced on the cleanest case of the three causes.
- **Tooling:** `tools/sources.py` `_chart(ticker)` returns `chart.result[0]` already, so a caller indexing `['chart']` fails —
  not a defect in the tool, a trap for scripts; noted.
- **Unreconciled (from the peers file):** TME's 20-F says 8,552,440 Spotify shares went to TME Hong Kong in 2017; Spotify's 20-F
  lists 4,276,200 held there at 2025-12-31. Not material to this run's count (Spotify's outstanding count is its own).

## REGISTER
- Verdict: [ ] IN [x] **OUT (about the business)** [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Spotify rents the same non-exclusive catalogue its rivals sell — its largest supplier says every service carries
  all content and a listener needs one subscription — so criterion (2) of [E3-03] fails; the licences are renewed every one to
  three years from owners who take 50–64% of each price rise; and five years of price increases produced high returns on capital
  in two. **Q1 IN · Q2 OUT · Q3 (recorded) IN, no disqualifier, live buyback and incentive flags · Q4 (recorded) survives,
  owner earnings UNKNOWABLE on a €95m–€2,186m range, named death THE TENANT · Q5 COMPUTATION — NOT A CLEARANCE: US$525.75
  (€453.55), cap €93.2bn, yields 0.2%–3.2%, above every construction at the floor and the sovereign · Q6 (recorded) reopening
  conditions written.**
- **PASS/FAIL: FAIL — closed at Q2 (OUT, on the business as constituted).**

