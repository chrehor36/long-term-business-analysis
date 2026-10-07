---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`*

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].

*Resumed 2026-09-13 by a fresh session after the first was killed at a session limit; Step 0, Q1 and Q2 are the killed session's, read whole and not re-derived. Working: `q3calc.py` / `q3calc_out.txt`; the SEC order `SEC_order_33-11060.txt` (`sec_order.py`); the FY2023 guidance record `8K_2022-*` and `8K_2023-02-22` (`fetch_fy23.py`), all in the research folder.*

**What the killed session's last three fetches were for (opened, not assumed).** `SEC_press_2022-79.txt` is the SEC's release of 2022-05-06 charging NVIDIA over its FY2018 cryptomining disclosures (the honesty matter below). `10Q_FY23Q1.txt` (quarter ended 2022-05-01, `0001045810-22-000079`) carries the company's own disclosure of that settlement. `10Q_FY26Q2.txt` (quarter ended 2025-07-27, `0001045810-25-000209`) carries the H1 FY2026 comparatives and the only interim cash-tax line on disk (*"Cash paid for income taxes, net | $ | 8,451"*), which the Q2 FY2027 10-Q does not print; that is the most likely purpose, and it is the use made of it here. The killed session left no note saying so.

**STEP 1: DECLARE THE WEIGHT CASE.** *How much damage can this manager do before I can react?*
- [x] **Daily execution [E3-38]**, through its 1991 original: *"a business, unlike a franchise, can be killed by poor management"* **[E3-43]**. Q2 found a
  dominant position in a race, not a franchise, so the original governs. The decisions that decide a year are made every quarter: supply and capacity
  commitments raised **from $119bn to $279bn in one quarter** (10-Q Note 10), what to build for which architecture, whom to finance, and which export
  regime a product will meet. The filed cost of one such decision going wrong is on record: $2.17bn of provisions in FY2023 and the $4.5bn H20 charge
  in Q1 FY2026.
- [ ] **Control [E1-16]: not ticked.** A listed minority position; single class (Step 0); Mr. Huang holds **3.58%** (DEF 14A 2026, `0001045810-26-000036`,
  as of 2026-03-23).
- [ ] **Leverage [E3-29]: not ticked, argued both ways.** *For ticking:* the contingent layer is large and new. Commitments of **$366bn** (Note 10 first
  table), additional commitments of **$56bn** (AI cloud agreements and third-party leases) and guarantees capped at **$108.5bn** sum to **$530.5bn, 2.3x
  shareholders' equity of $228,984M**; and **43.2% of that equity is the carrying value of stakes** in companies that are also customers (`q3calc_out.txt`).
  One demand pause would hit the commitments, the stakes, the receivables ($63.1bn on terms *"up to one year"*) and the guarantees together, so the
  errors are correlated, which is what makes leverage dangerous. *Against:* [E3-29]'s mechanism is a balance sheet on which *"small asset errors destroy
  equity"*, and its example is 20:1. Recognised liabilities are **$91,288M against equity of $228,984M (0.4:1)**; debt of $33,366M sits beside cash and
  debt securities of $56,586M; most of the $279bn is a purchase of inventory that the 10-Q says is *"in certain instances ... cancelable, rescheduled, or
  adjustable"*, and the guarantees are not yet effective (first SB Energy phase expected FY2029). A FY2023-sized error at today's exposure is quantified at
  Q4 (~$58bn) and is about a quarter of equity, not all of it. **Not ticked; recorded as the determinant most likely to tick if the commitments keep
  growing at this quarter's rate.** The weight case does not turn on it, because daily execution already makes Q3 a gate.
- **Case declared: Q3 is a BINARY GATE, on daily execution.** *(Recorded, not governing.)*

**Honesty: binary, permanent, filings-based [E5-16].** *Each matter dated to when it became public.*
1. **The SEC cease-and-desist order, public 2022-05-06** (Securities Act Release No. 11060, Exchange Act Release No. 94859, File No. 3-20844; order text
   `SEC_order_33-11060.txt`, fetched from sec.gov at the resume). **The conduct:** the Forms 10-Q for Q2 and Q3 FY2018, *"filed ... on August 23, 2017 and
   November 21, 2017"*. **The finding:** *"NVIDIA had information indicating that cryptomining was a significant factor in the year-over-year growth in
   revenue from the sale of GPUs that NVIDIA designed and marketed for gaming. The company, however, did not disclose this"*; Gaming revenue rose *"by 52%,
   year over year for the second fiscal quarter 2018, and by 25% ... for the third"*; the omission, beside disclosure of crypto sales in OEM, *"gave the
   misimpression ... that the year-over-year growth in the company's Gaming revenue was not meaningfully impacted by cryptomining"*; and *"NVIDIA's senior
   management internally expressed a desire to capture the cryptomining demand"*. **Its legal basis and limits, in the order's words:** Sections 17(a)(2)
   and (3), *"A violation of these provisions does not require scienter and may rest on a finding of negligence"*; plus disclosure controls under Rule
   13a-15(a); *"without admitting or denying the findings"*; a **$5,500,000** penalty; **the respondent is the company and no individual is charged.** **The
   correction:** *"The company's periodic reports did not identify cryptomining as a significant factor in year-over-year growth in Gaming revenue until ...
   its Form 10-K for fiscal year 2018 (filed on February 28, 2018)"*, one quarter after the second omission. The company's own disclosure of the settlement:
   10-Q Q1 FY2023 (`0001045810-22-000079`): *"NVIDIA entered into a settlement with the SEC relating to MD&A disclosures in our Forms 10-Q for the second and
   third quarters of fiscal year 2018 concerning the impact of cryptocurrency mining"*. **The same CEO (founder, CEO since 1993) and CFO (Ms. Kress, since
   2013, 10-K FY2019) signed then and sign now.**
   **Read against the corpus.** [E5-22]: *penalty size is not seriousness*, so $5.5M is not read as small; the test is whether they acted when they learned,
   and the filed record is that the next annual report named cryptomining as a significant factor, and that in the second crypto wave the FY2022 10-K
   reported *"CMP revenue was $550 million for the fiscal year"* separately and shipped LHR cards, while still saying *"we have limited visibility into how
   much this impacts our overall GPU demand"*. [E2-68]: disclosure where the company holds the information advantage is the sharpest read, **and in 2017 this
   company failed it**: the SEC's finding is exactly that the company knew more than the 10-Q said. [E5-16] refuses **personal misconduct**; the order finds a
   corporate disclosure failure on a standard that needs no intent, names no person, and was corrected within a quarter. **Not a disqualifier on the record
   read. It is the most serious candour fact in this file and is carried at [E2-26] below, dated 2017 (conduct) and 2022 (public).**
2. **The securities class action, In re NVIDIA Corporation Securities Litigation, 4:18-cv-07669-HSG, filed 2018-12-21** (10-Q Q2 FY2027 Note 10): alleged
   *"materially false or misleading statements related to channel inventory and the impact of cryptocurrency mining on GPU demand between May 10, 2017 and
   November 14, 2018"*, a longer window than the SEC's; dismissed 2021-03-02; reversed in part by the Ninth Circuit 2023-08-25; the Supreme Court dismissed
   NVIDIA's writ *"as improvidently granted on December 11, 2024"*; **on March 25, 2026 the district court certified a class** of purchasers from
   2017-08-10 to 2018-11-15. Four derivative suits on the same facts are stayed. *"there are no accrued contingent liabilities ... liabilities, while
   reasonably possible, are not probable"*. **Open allegations of knowing falsity against executives; not a finding. A judgment of scienter against a named
   officer would be a [E5-16] matter, and is written into Q6.**
3. **China's antitrust regulator, preliminary finding published 2025-09-15** (10-Q Part II Item 1A): that compliance *"with applicable U.S. export controls
   ... violated the terms of China's approval of our Mellanox acquisition"*. A dispute over obeying the home government's export law; not dishonesty toward
   owners. **Open; recorded at Q2 as a regime reach [E2-59] and at Q4 as an exposure.**
4. **Competition inquiries** (EU, US, UK, China, South Korea requests for information; the French Competition Authority on whether gaming and data-center
   GPUs are separate categories): inquiries, no finding. **Open.**
5. **Related parties** (DEF 14A 2026): *"The total compensation for Fiscal 2026 of the daughter and son of Mr. Huang was approximately $1,232,000 and
   $1,320,000"*, set *"without the involvement of Mr. Huang"*. Disclosed with amounts; not a flag. Hedging and pledging of NVIDIA stock are prohibited.
- **No finding of personal misconduct by a named officer or director in any document read** (10-Ks FY2017, FY2019, FY2021-FY2026; 10-Qs FY23Q1, FY26Q1-Q3,
  FY27Q1-Q2; DEF 14A 2026; thirteen releases; the SEC order). Written as the absence of found disqualifiers, not a finding that the managers are honest
  **[E5-17]**, and the 2017 matter shows why: the filing read at the time looked clean.

**STEP 2: THE FLAGS [E4-22, E5-15, E4-29, E4-30].** *Each is a prompt to READ, never a verdict. Thirteen EX-99.1 releases were read before scoring (six
from 2025-05-28 to 2026-08-26 on disk from the killed session; six from the FY2023 down-year, fetched at the resume; and the SB Energy release).*
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]: NOT FIRED, and the direction since FY2027 is the inverse.** "EBITDA" appears **0 times** in every
  release on disk. Non-GAAP measures are in every release, presented in a GAAP table first and a non-GAAP table second. **Until FY2026 the non-GAAP
  measures excluded stock-based compensation** ([E5-06]: *"even more cavalier"*); **the Q4 FY2026 release announced the end of that a quarter ahead, with a
  reason**: *"Beginning in the first quarter of fiscal year 2027, NVIDIA will include stock-based compensation expense in non-GAAP financial measures.
  Stock-based compensation is a foundational component of NVIDIA's compensation program"*, and recast history. Today's non-GAAP net income is **below**
  GAAP because it strips the equity marks: **$45,548M against $58,321M (Q1 FY2027) and $53,954M against $59,688M (Q2 FY2027)**. A switch made at record
  results, announced ahead, toward the stricter number is [E2-69]'s direction toward candour, and the reverse of [E2-49]'s form.
- [x] **The except-for prompt [E2-57] and the restructuring charge [E3-53, E5-33]: FIRES as a prompt; read; passes on disclosure, fails on frequency.**
  Q1 FY2026: *"Excluding the $4.5 billion charge, first quarter non-GAAP gross margin would have been 71.3%"*, with an "as adjusted" EPS line. **Against the
  flag:** GAAP is stated first; the favourable reversal the next quarter was stripped too (*"Excluding the $180 million release, non-GAAP gross margin for
  the quarter would have been 72.3%"*), so both innings were counted. **For it:** provisions for inventory and purchase obligations are filed every year,
  **$354M (FY2022), $2.17bn (FY2023), $2.2bn (FY2024), $3.7bn (FY2025), $7.2bn (FY2026), $2.1bn (H1 FY2027)** (MD&A of each 10-K and the 10-Q), including
  $0.4bn more on H200. A charge that recurs with every architecture and regime change is the cost of this business, and an "excluding" figure invites
  treating it as one-time. **Kept inside the owner-earnings mean** (the cash is inside OCF; Q4).
- [x] **Trumpeted projections [E4-22, third]: FIRES as a prompt; the record is checked [E3-48], across a down-year and a boom.** NVIDIA guides one quarter
  ahead, revenue *"plus or minus 2%"*:
  | quarter | revenue outlook | outturn | GAAP gross margin outlook | outturn | source |
  |---|---|---|---|---|---|
  | Q1 FY2023 | $8.10bn | **$8.29bn** (above the top) | 65.2% | 65.5% (inside) | EX-99.1 2022-02-16, 2022-05-25 |
  | **Q2 FY2023** | **$8.10bn** | **$6.70bn (17% below; pre-announced 2022-08-08)** | 65.1% | **43.5%** | EX-99.1 2022-05-25, 2022-08-08, 2022-08-24 |
  | Q3 FY2023 | $5.90bn | $5.93bn (inside) | 62.4% | **53.6% (8.8 points below)** | EX-99.1 2022-08-24, 2022-11-16 |
  | Q4 FY2023 | $6.00bn | $6.05bn (inside) | 63.2% | 63.3% (inside) | EX-99.1 2022-11-16, 2023-02-22 |
  | Q2 FY2026 | $45.0bn | **$46.7bn** (above) | 71.8% | 72.4% (above; includes a $180M release) | EX-99.1 2025-05-28, 2025-08-27 |
  | Q3 FY2026 | $54.0bn | **$57.0bn** (above) | 73.3% | 73.4% (inside) | 2025-08-27, 2025-11-19 |
  | Q4 FY2026 | $65.0bn | **$68.1bn** (above) | 74.8% | 75.0% (inside) | 2025-11-19, 2026-02-25 |
  | Q1 FY2027 | $78.0bn | **$81.6bn** (above) | 74.9% | 74.9% (inside) | 2026-02-25, 2026-05-20 |
  | Q2 FY2027 | $91.0bn | **$96.2bn** (above) | 74.9% | 75.0% (inside) | 2026-05-20, 2026-08-26 |
  **Revenue met or beaten 8 of 9, above the top of the range 6 of 9; one miss of 17% in the down-year, when gross margin came in 21.6 points under the
  outlook, and gross margin missed again the next quarter by 8.8 points. Gross margin met or beaten 7 of 9.** The miss was **pre-announced eight days after the quarter closed**, with the cause and the price action named: *"the company implemented pricing
  programs with channel partners to reflect challenging market conditions"* (2022-08-08). That is the candour case [E2-26] handled well. The ratchet
  [E5-30] is live (a quarterly outlook for at least four years). The promotional register is in the CEO quotations (*"the largest infrastructure expansion
  in human history"*, 2026-05-20; *"Now, compute is revenue"*, 2026-08-26) and the *"over $500 billion"* financing platforms announced *"subject to
  definitive agreements"*, not in multi-year numeric targets. **Recorded as a live behaviour whose one test in a soft year was a large miss disclosed
  promptly.**
- [ ] **Serial share issuance [E5-15]: prompt run, NOT FIRED as issuance.** Split-adjusted shares (cover pages; 4-for-1 2021 and 10-for-1 2024 verified at
  Step 0): **21,664M (2016-03) → 23,544M (2017-02) → 25,100M (2022-03 peak) → 24,147M (2026-07-26)**: +11.5% in ten years, +2.6% since February 2017, and
  **-3.8% from the 2022 peak**. The 2016-17 step is convertible-note conversions (FY2017 cash-flow *"Loss on early debt conversions"*); the rest is employee
  stock. **What it cost to hold the count:** repurchases of $135,635M and RSU tax withholding of $28,884M FY2017-H1 FY2027; since FY2023, **$156,075M bought
  a net reduction of 953M shares, about $164 per share retired** (`q3calc_out.txt`). No issuance for cash in the decade.
- [ ] **Dividends funded by issuance [E2-52]: not fired.** The quarterly dividend rose from $0.01 to $0.25 a share from June 2026 (release 2026-05-20), about
  $24bn a year on 24.1bn shares, with no share issuance for cash. *(But see condition (1) below: H1 FY2027's distributions exceeded cash left after
  investment, and the half raised $24.9bn of debt.)*
- [ ] **Filed-figure tells [E4-30]: NOT FIRED.** Cash taxes as a share of pre-tax income: **0.7-5.9% (FY2017-FY2022) → 33.6% (FY2023, on a small
  pre-tax) → 19.4% → 18.0% → 14.3% (FY2024-FY2026)**; 15.3% in FY2026 excluding the $8,918M of non-cash equity gains; cash tax $20,288M against book tax
  expense $21,383M in FY2026. **Rising across the decade, not falling.** Reported growth is not unnaturally smooth (FY2020 revenue fell 6.8%; FY2023 operating
  income fell 58%). *Presentation note:* the Q2 FY2027 10-Q cash-flow statement prints no cash-tax line (the Q2 FY2026 10-Q did), so a trailing figure is not
  computable from the filing; recorded, not a flag.
- [x] **Weak accounting: a PROMPT on useful lives, read, not a cockroach.** *"In February 2023, we assessed the useful lives of our property, plant, and
  equipment. Based on advances in technology and usage rate, we increased the estimated useful life of a majority of the server, storage, and network
  equipment from three years to a range of four to five years, and assembly and test equipment from five years to seven years ... an increase in operating
  income of $135 million"* (10-K FY2024). **Lengthening lives lowers depreciation**, the direction Amazon reversed in the same era; at 0.4% of FY2024
  operating income it is immaterial, and from the FY2025 10-K the stated range is *"two to seven years"*, so some assets now carry shorter lives. Carried to
  Q4's [E5-20] question. SBC has been expensed throughout.
- [x] **Metric-switching [E2-49]: two switches, neither fires on the rule's form; one soft note.** (1) SBC into non-GAAP, above. (2) From Q1 FY2027 the
  market platforms changed (*"NVIDIA will have two market platforms — Data Center and Edge Computing"* (the dash is the release's), Hyperscale and ACIE within Data Center; Gaming no
  longer reported alone), comparatives recast, announced at record results. **The soft note:** the Q1 FY2027 release bridged the old split once (*"Data
  Center compute revenue was a record $60.4 billion, up 77% ... networking revenue was a record $14.8 billion, up 199%"*), and the compute line, the one
  growing more slowly than the total, is absent from the Q2 FY2027 release and 10-Q. My [E2-49] prior (six fires, five failures as of 2026-09-12) is checked,
  not assumed: **not a fire; recorded for the next filing to test.**
- [ ] **Stock-price targeting [E3-50]: not fired.** One of three pay elements vests on *"3-Year Relative TSR"*; that ties pay to the price, not to the premise
  *"that their job at all times is to encourage the highest stock price possible"*; no stratagem found.
- [ ] Unintelligible footnotes: not fired. The commitments and guarantees notes name counterparties, triggers, caps and timing.

**Where the flags converge [E4-52]?** The fired prompts are a recurring charge treated as "excluding", a live guidance habit, and a useful-life extension;
the older facts are a 2017 candour failure and a decade of SBC excluded from the headline. **Since 2022 they point the same way, toward more disclosure**
(the pre-announcement, SBC put back, the commitments and guarantee tables). **No confluence toward one outcome is found.**

**STEP 3: THE PRIMARY TEST [E2-01]**, balance sheet first **[E5-27]** (`q3calc_out.txt`; FY2016-FY2024 balance sheets are companyfacts screening
values, the FY2025, FY2026 and 2026-07-26 balance sheets re-read on the filed faces):
| FY | equity | NI ÷ avg equity | operating capital (equity − cash − debt securities − stakes + debt) | after-tax operating income ÷ avg operating capital | same, ex goodwill and intangibles [E2-43] |
|---|---|---|---|---|---|
| FY2017 | 5,762 | 32.6% | 1,743 | 127% | 304% |
| FY2018 | 7,471 | 46.1% | 2,363 | 133% | 201% |
| FY2019 | 9,342 | 49.3% | 3,908 | 103% | 131% |
| FY2020 | 12,204 | 26.0% | 3,298 | 67% | 82% |
| FY2021 (Mellanox) | 16,893 | 29.8% | 12,295 | 49% | 96% |
| FY2022 | 26,612 | 44.8% | 16,350 | 60% | 114% |
| **FY2023** | 22,101 | **17.9%** | 19,470 | **20%** | 31% |
| FY2024 | 42,978 | 91.5% | 25,382 | 129% | 174% |
| FY2025 | 79,327 | 119.2% | 41,193 | 212% | 257% |
| FY2026 | 157,293 | 101.5% | 76,114 | 189% | 254% |
| TTM to 2026-07-26 | 228,984 | 99.9% (Jan/Jul average) | 106,867 | 181% | 246% |

*(CONVENTION, confessed: after-tax operating income uses the filed effective rate for FY2024 onward and 15% where the rate was not extracted, FY2017-FY2023;
"stakes" are non-marketable and publicly-held equity securities, which were immaterial before FY2023.)*
- **Primary test: passed at a level no run in this queue has shown, and not steady.** The one soft year (FY2023) fell to 17.9% on equity and 20% on operating
  capital; the series is a wave, which is Q2's finding read through the owners' capital.
- **What the $99bn of stakes and H1 FY2027's $24,140M of other income do to it.** Stakes are **43.2% of equity at 2026-07-26** (25.4% at 2026-01-25). TTM
  net income of $192,880M includes **$32,164M of other income**; net income without it (taxed at the TTM rate of 16.0%) over average equity **without the
  stakes** is **134.1%**, against 99.9% reported. **The stakes lower the reported return, not raise it:** they add a large denominator and marks that are
  small beside operating income. The primary test is carried by the chip business; the capital now going to stakes earns marks, not cash, and its return is
  not computable from the filings.
- **[E2-56], judged incrementally:** operating capital rose from $19,470M (FY2023) to $106,867M (2026-07-26) while after-tax operating income rose by about
  $162bn: **the increment earns far above any hurdle.** The capital outside operating capital (stakes $99bn, commitments $25bn more) has no cash return on
  file; the consolidated series cannot camouflage it because it is not yet in the series.
- **[E3-54] retention:** passes by orders of magnitude (retained earnings $219,157M against a cap of $5,270.9bn), which measures the wave as much as the
  allocation.

**The half-owner test [E2-26].** The filings tell the owner the commitments by type and year, the guarantee caps with counterparty (*"an affiliate of
OpenAI Group PBC"*), triggers and timing, the stakes in total with measurement, every provision with its product, customer concentration by percentage,
the AI cloud mechanics (*"which the AI clouds can unilaterally stop providing to us and sell to third-party customers at more advantageous rates"*), and the
FY2023 miss eight days after quarter-end. **They do not tell the owner:** the $99bn itemised by investee (only Intel $5bn and Anthropic up to $10bn are named,
in the Q3 FY2026 10-Q); **how much revenue comes from customers NVIDIA has invested in, financed or guaranteed** (the 10-K says only *"These investments include
AI model makers that purchase our products directly or through CSPs"*); the revenue recognised on sales to AI clouds that carry NVIDIA's buy-back commitment;
the price paid per share for any stake; or who the 22% and 14% customers are. **Mixed: candid in the notes where the numbers are large and new; silent on the
one number that sizes the round trip. And in 2017, by the regulator's finding, it failed the test outright.**

**The institutional imperative: score all four [E2-30].** *Not a fraud test.*
- [ ] resists change: not ticked (a new reporting framework, SBC put back into non-GAAP, a new AI cloud business model in Q2 FY2027).
- [x] **projects soak up funds (prompt):** $17.5bn into private companies and infrastructure funds in FY2026; **$42,404M of equity purchases in H1 FY2027**
  and $25bn more committed; ~$17bn for the Groq licence and hires; $11.9bn plus up to $1.0bn of retention equity for Hugging Face; guarantees capped at
  $105bn; *"more than $500 billion"* of financing platforms in memorandum form. The cash is large and the projects have materialised as fast as it has.
- [ ] staff studies to justify a craving: no evidence either way in a filing.
- [x] **peers imitated (prompt):** Broadcom backstops its custom-accelerator customers ($29bn, Q2 row), Amazon funds OpenAI and Anthropic (AMZN run), and
  NVIDIA funds and guarantees the same laboratories; **[E2-27]**'s picture, each rational alone.

**Capital allocation: buybacks [E5-08, E4-31, E5-24, E4-50].**
- **(1) Ample funds for operations and liquidity: met on liquidity, with a borrowed half-year.** Cash and debt securities $56,586M, OCF $134,360M TTM. But in
  H1 FY2027 OCF of $74,421M less capex $4,434M, net equity purchases $35,163M, Groq $2,944M, repurchases $39,044M, dividends $6,290M and withholding $4,531M
  leaves **-$17,985M** before the smaller lines, and the half raised **$24,896M of notes**. Against **$120bn of commitments due in the rest of FY2027**, distributions were in effect
  partly borrowed. [E4-50] licenses borrowing to buy back **only at a true discount**; that is condition (2)'s question. Prompt, and [E2-60]'s "financial
  strength" dimension is carried to Q4.
- **(2) A material discount to intrinsic value conservatively calculated: FAILS on this run's computation. CAPITAL ALLOCATION FLAG.** Average prices paid
  (split-adjusted, from the 10-K equity notes and the 10-Q): **$15.94 (FY2023), $46.19 (FY2024), $109.68 (FY2025), $143.26 (FY2026), $196.06 (H1 FY2027),
  $209.57 (Q2 FY2027)**. Q5's computation (below) values the business at the 10% floor at roughly **$50 a share with no growth, ~$105 at 5% a year forever
  and ~$175 at 7% forever, all from the best twelve months on file.** The FY2026 and FY2027 purchases sit at the 6-7%-forever end of that range, which is
  no discount. The stated reason was never value: *"Our share repurchase program aims to offset dilution from shares issued to employees"* (10-Ks FY2024,
  FY2025); the FY2026 10-K drops the sentence and gives none; "intrinsic value" appears 0 times in the FY2026 10-K, the Q2 FY2027 10-Q, the DEF 14A and the Q1 FY2027 CFO commentary. **[E4-31]'s
  third condition (owners supplied the information to estimate value) is therefore not addressed at all.** With the humility clause **[E4-13]**: *"They also
  know a whole lot more about them than I do"*; and **[E5-08]**: *"infractions, even serious ones, are innocent; many CEOs never stop believing their stock is
  cheap"*. **Binds position size, never the discount rate. The FY2023 purchases ($10.04bn at ~$16) were, in hindsight, the cheapest capital this company ever
  retired; hindsight is not the test, and the FY2023 10-K stated no rationale for them either (0 hits for "offset dilution").**
- **The refusal test [E2-51]:** not applicable (repurchasing heavily).
- **Groq [E5-24, E4-39]:** ~$17bn for *"a non-exclusive license agreement ... and hired certain Groq employees"*, booked as $14.4bn of goodwill *"primarily
  attributable to the workforce and future development of the licensed technology"*; *"NVIDIA Groq 3 LPX ... is now in full production"* two quarters later.
  No return case and no post-mortem supplied. At Q2 it was evidence of a substitute; here it is a price paid for position without a value case.
- **Hugging Face [E5-44]:** *"approximately $11.9 billion purchase price payable to Hugging Face stockholders ... and an equity-based retention program of up
  to approximately $1.0 billion"*; paid in cash, so [E5-44]'s share-for-share test applies only to the retention equity; no value case filed.
- **The equity in customers [E3-40]:** $99bn plus $25bn committed, including companies that *"purchase our products directly or through CSPs"*. This is not
  [E3-40]'s manager wandering off the base business into so-so businesses: **it is the base business's demand being financed by the seller**, the Q2 finding
  seen as allocation. Recorded as a prompt, and as the channel through which a demand pause becomes a capital loss (Q4).
- **Tenure [E3-58]:** the same CEO since 1993 and CFO since 2013 allocated all of it; allocation is not visibly outsourced to bankers or consultants.

**Pay and what it vests on [E4-27]** (DEF 14A 2026): three elements: *"variable cash awards based on annual revenue"*; *"PSUs based on annual Non-GAAP Operating Income performance with a single-year
performance metric, vesting over four years"*, where Non-GAAP Operating Income is *"GAAP operating income ... excluding stock-based compensation expense, acquisition-related and other costs, and other"*,
and multi-year PSUs on *"3-Year Relative TSR"*. The FY2026 stretch goals *"would automatically be reduced to $160.0 billion and $96.0 billion"* if H20 controls came
in the first half, a rule set *"at the time it set the Fiscal 2026 performance goals"* (pre-set, which [E2-49] asks for), and irrelevant to the outcome: revenue
of $215.9bn beat even the original $190.0bn. **The incentive to note:** cash pay rewards revenue whether or not NVIDIA financed the buyer, and equity pay
rewards an operating profit that excludes the executives' own stock pay and ignores capital committed to stakes, guarantees and buy-backs. **A prompt, not a
flag**; it points at the same round trip as the half-owner gap.

**THE GUARDRAIL: checked before the verdict.**
- [x] Nothing in this Q3 is used to **promote** the name **[E2-37, E2-38, E3-39]**; the extraordinary returns above are the wave's, and Q2 has ruled on that.
- [x] **Key-person dependence [E4-23]:** none filed (recorded at Q2).
- [x] Is a great manager the reason to act? **No; the file is closed on the business.** [E2-35, E2-36] do not arise.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN on the binary**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *No personal-misconduct disqualifier found (the absence of found disqualifiers, not a finding of honesty [E5-17]). Carried, heaviest first: the SEC's 2022
  finding that the company's 2017 10-Qs omitted what it knew about cryptomining, on a negligence standard with no individual charged, corrected in the next
  10-K, by the same CEO and CFO who run it now [E2-26, E2-68]; the certified class action on the same facts, open, which would become a [E5-16] matter on a
  scienter finding against a named officer; a capital-allocation flag on buyback condition (2), no value rationale ever stated [E5-08, E4-31], and H1 FY2027
  distributions partly borrowed [E4-50]; recurring provisions presented "excluding" [E2-57]; pay on revenue and on an operating profit that excluded SBC
  [E4-27]. IN never promotes.*

---
