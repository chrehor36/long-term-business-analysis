# Company Run — Ecolab Inc. (NYSE: ECL) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Dispatched blind run
under the canonical brief `Screens/_daily/_dispatch_brief.md` (no departure from it). Every judgment cites a v5
ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Copied from the template before any fetch (commit 29f06775).

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**Contamination, declared (the blind rule):** no file about Ecolab was opened, listed or searched. Seen by accident and not
used: (1) a listing of `Test Runs/` filtered on today's date (made to check whether today's file name was free, before I
had read the brief's rule against filtered listings; the filter was the date, not the ticker) showed the names of twelve other
runs dated 2026-10-07 (ACLS, ACNB, AMAT, ATR, AVGO, BMI, CB, CHD, CL, CMG, COKE, CSL), none about Ecolab; (2) the session
context carried the repository's git status (research folders of AYI, ARCB, BDC, CHD) and five recent commit subjects naming
the boxes and alert prices of the CL, CMG, CSL and COKE runs; (3) the session context carried a memory index line saying the
operator's queue had "57 gate-clearers, nothing buyable" and that holding reviews are owed. None of it names Ecolab; none of it
was used. Whether anyone holds or wants this name was not sought.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $279.25 (2026-10-07, live quote printed by `tools/run.py`; **aggregator, flagged** under operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock $1.00 par, **280,328,603** (10-Q for the
  quarter ended 2026-06-30, filed 2026-08-06, accession `0001628280-26-053886`; `python Screens/cover_shares.py ECL`).
  Checked against the balance sheet of the same 10-Q, which states "280.3 shares outstanding as of June 30, 2026 and 282.0
  shares outstanding as of December 31, 2025" (millions). No 8-K or prospectus after the 10-Q issues shares; the 10-Q states
  3,454,001 shares remained under the repurchase authorization, so the count can only have fallen since.
- **Market cap:** $78,282M (280.3286M x $279.25).
- **Sovereign for the earnings currency (USD):** **5.64%**, US Treasury daily par yield curve, 30-year, 2026-10-06
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K FY2025, filed 2026-02-23, `0001104659-26-018357` (Items 1, 1A, 5, 7, Notes 3, 15, 18, cash-flow and equity statements).
  - 10-Q Q2 2026, filed 2026-08-06, `0001628280-26-053886` (balance sheet, cash flow, debt note, CoolIT acquisition, subsequent events).
  - DEF 14A, filed 2026-03-20, `0001104659-26-032777` (incentive design, pay ratio, director rules, the shareholder proposal).
  - 8-K 2026-07-28, `0001628280-26-049933`, Exhibit 99.1 (second-quarter release and outlook); 8-Ks of 2026-04-15
    `0001104659-26-043821` and 2026-05-29 `0001104659-26-068276` (CoolIT financing).
  - Earlier 10-Ks for the span: FY2024 `0001558370-25-001263`, FY2023 `0001558370-24-001581`, FY2022 `0001558370-23-001969`,
    FY2021 `0001558370-22-002059`, FY2020 `0001558370-21-001916`, FY2019 `0001558370-20-001788`, FY2017 `0001558370-18-000999`,
    FY2016 `0001558370-17-000944`, FY2015 `0001558370-16-003581`, FY2013 `0001104659-14-014489`, FY2011 with its Exhibit 13
    `0001104659-12-014104`. Pre-2011 sales and operating income from the XBRL company facts (transcription; flagged as such).
- **One figure cross-checked against the filed statement:** cash provided by operating activities 2025, **$2,952.6M** in the
  consolidated statement of cash flows of `0001104659-26-018357`, against 2,953 printed by `tools/run.py`; capital expenditures
  $1,048.3M against 1,048. They agree.
- `python tools/run.py ECL` arithmetic lines only (`Test Runs/_research 2026-10-07 ECL/runpy_output.txt`): OCF less SBC less
  capex 1,542 / 1,685 / 1,768 for 2023 to 2025 ($M), five-year window 1,462; capex 775 / 994 / 1,048 against D&A 924 / 936 / 977
  (D&A there includes amortization of acquired intangibles, 304 in 2025); SBC 95 / 135 / 137, resolved and complete (the tool
  found no other stock-pay line, no securities inside operating cash, no software or intangible spending beside capex). Note: the
  tool's debt table adds `ecl:OperatingLeaseLiabilityNoncurrentExcludedFromLongTermDebt` (d3) into its "sum" for 2022 to 2025,
  although its own footnote says leases are not in it; I used the filed debt lines, not the tool's sum.

## THE FOUNDATIONS (not a gate)
The foundation that bears hardest on this name is the margin of safety: "if you have to actually do it on — with pencil and
paper, **it’s too close to think about**" **[M1996-084]**. Ecolab is the kind of business that tempts the analyst to forgive
the price because the business is good; the market's quotation of it "doesn’t tell us anything. It just tells us prices."
**[M2006-077]**, and the question is only whether the price is "out of line where the facts and reasoning lead you"
**[M2006-077]**. No macro view enters: "macro conclusions are — just never enter into the discussion." **[M2000-094]**. The share is read as a business **[M1997-109]**. Who is paid to tell me: the company's own
releases feature an adjusted figure and guidance (Q4 and Q5 below). **Contrary evidence, written down as found**
**[M1997-127]**:
1. The company exited its energy business (bought with Nalco in 2011 and Champion in 2013) in 2020 at a recorded loss on
   separation of $2,137.8M (FY2020 10-K, `0001558370-21-001916`, Note 5): a misjudged business inside the record.
2. Special (gains) and charges in every year from 2014 to 2025, under at least seven named programmes (Q4).
3. Growth has been bought: net acquisitions of $5,171M over 2021 to 2025 against $7,311M of owner cash in the same years, and
   CoolIT Systems for $4.75B in cash after the window, financed by new notes (Q6, Q7).
4. The two newest purchases (Ovivo Electronics, CoolIT Systems) are data-centre and semiconductor technology, a move toward the
   fast-changing field the framework sends to TOO HARD (Q1).
5. Receivables rose from 17.8% of sales (2016) to 20.2% (2025) (Q4).

## THE STANDING RULE
Owning a marketable part-interest in Ecolab bought with cash and sized within the buyer's own liquidity puts the buyer at no
risk of ruin; the rule forbids only the buyer's borrowing, "borrowed money has no place in the investor's tool kit"
**[L2014-005]**, and the buyer's conduct is not before this run **[M2012-081]**.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **What the business is** (FY2025 10-K, Item 1): four reportable segments since 2025-01-01: Global Water (Light & Heavy,
  Food & Beverage, Paper: water treatment, process chemicals and cleaning for industrial plants; the former Nalco business and
  the former Global Industrial segment), Global Institutional & Specialty (warewashing, laundry, sanitizers and infection
  prevention for restaurants, hotels, hospitals and food retail; healthcare moved in from 2025), Global Pest Elimination
  (commercial pest service), Global Life Sciences (contamination control and Purolite resins for pharmaceutical makers). About
  25,000 of 48,000 employees are sales and service staff; the majority of revenue is consumable product sold through a field
  force that services the customer on site; warewashing products alone were about 13% of 2025 sales; no customer is 10% of
  sales; more than 10,000 raw materials, the largest about 5% of purchases.
- **The test as the draft states it.** Understanding is "a reasonable fix on about **what the earning power and competitive
  position will look like in five or 10 years**" **[M2012-065]**, not knowledge of the product. The chemistry is opaque to
  me, as the petroleum-additives chemistry was to the speaker: "I never would understand the chemistry of it, but I — but
  that’s not necessarily vital. What is important is that **I understand the economic dynamics of the industry.**"
  **[M2011-014]**. The economic dynamics here can be read from the filings: a consumable used daily by plants, kitchens and
  hospitals, sold with service, whose cost is small against what it protects (the filing's claim of value is water, energy and
  operating savings); the key variables are customer retention, price against raw-material cost, and the volume of the
  customers' own activity (restaurant traffic, industrial production).
- **Are the key variables foreseeable** "trying to identify the key variables in that particular business, and evaluating how
  predictable they were first" **[M1998-044]**? Price against raw materials has a full recent test (2021 to 2025, Q2); the
  customers' activity moves with the economy but is not forecast here **[M2000-094]**; retention is asserted ("Our historical
  retention rates [...] support our expectation of consistent sales generation") but no rate is disclosed in any 10-K read
  (FY2016, FY2019, FY2022, FY2025; search "retention rate"). Would the insiders write the ten-year forecast down
  **[M2000-105]**? For warewashing, water treatment and pest service, yes in my reading; these are old fields.
- **The doubt that has to be faced, "if you have doubts about something being into your circle of competence, it isn’t."**
  **[M2002-092]**: the 2025 to 2026 purchases (Ovivo Electronics, $1.6B, ultrapure water for semiconductor plants; CoolIT
  Systems, $4.75B, data-centre liquid-cooling hardware, closed 2026-07-02, 10-Q `0001628280-26-053886`) add parts whose
  ten-year economics I cannot foresee. Under Q1's holding-company paragraph a part keeps the whole outside only if it "matters",
  defined by Q2's threshold (more than half of five-year operating profit, or else the largest part). Together the two deals
  are $6.35B against an enterprise value of about $91B, and neither has five years of operating profit inside Ecolab; neither
  decides. They are carried to Q2 and Q6, not used to close Q1.
- **VERDICT: IN.** The deciding parts (water treatment and institutional hygiene) are old consumable-and-service businesses
  whose economics, not chemistry, can be read from the filings **[M2011-014]**, **[M2012-065]**; the technology additions do
  not decide and are recorded against the business at Q2 and Q6.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "**why is that castle still standing?** And what’s going to keep it standing or cause it not to be standing
**five, 10, 20 years from now.**" **[M1995-038]**.

**The parts table** (segment operating income at the filer's fixed currency rates, $M; 2021 and 2022 from FY2022 10-K
`0001558370-23-001969` under the old segments, 2023 to 2025 from FY2025 10-K `0001104659-26-018357` recast; Global Water is
the former Global Industrial; 2021 and 2022 "Global Institutional & Specialty" excludes healthcare and "Other" is mostly Pest
Elimination, so the shares are approximate, said so):

| Part | 2021 | 2022 | 2023 | 2024 | 2025 | five-year sum | share | decides |
|---|---|---|---|---|---|---|---|---|
| Global Water | 985.7 | 977.0 | 1,042.1 | 1,207.2 | 1,263.9 | 5,475.9 | 46% | **yes, the largest part** |
| Global Institutional & Specialty | 545.7 | 634.5 | 856.5 | 1,202.2 | 1,357.8 | 4,596.7 | 39% | no (second) |
| Global Pest Elimination ("Other" 2021-22) | 184.0 | 212.8 | 200.9 | 209.7 | 237.1 | 1,044.5 | 9% | no |
| Global (Healthcare &) Life Sciences | 152.3 | 205.0 | 118.9 | 91.8 | 120.7 | 688.7 | 6% | no |

No part carries more than half; the largest, Global Water, decides (Q2, A business of parts, CONVENTION). Institutional is
read as well, because at 39% it is nearly as large and the two together are 85% of segment profit.

**Margins over the cycle, the filer's own segment tables** (operating income over sales at fixed currency, each filing's own
rates; the segment definitions moved in 2018, 2021 and 2025, so the series is read for its shape, not to a decimal):

| Year | Industrial / Water | Institutional | Energy (gone 2020) | Consolidated GAAP op. margin | gross margin (reported) |
|---|---|---|---|---|---|
| 2014 | 12.6% | 19.4% | 14.0% | 13.7% | 46.2% |
| 2015 | 14.0% | 20.8% | 13.4% | 11.5% | 46.7% |
| 2016 | 15.2% | 21.5% | 11.1% | 14.6% | 47.5% |
| 2017 | 14.7% | 20.1% | 10.1% | 14.1% | 41.7% (restated basis) |
| 2018 | 13.9% | 19.9% | 10.0% | 13.3% | 41.2% |
| 2019 | 15.3% | 19.9% | 11.4% | 13.5% | 41.5% |
| 2020 | 18.5% | 8.9% (COVID) | gone | 11.8% | 41.4% |
| 2021 | 16.2% | 14.0% | | 12.6% | 40.2% |
| 2022 | 14.1% | 14.2% | | 11.0% | 37.8% |
| 2023 | 14.3% | 14.8% | | 13.0% | 40.2% |
| 2024 | 16.1% | 20.1% | | 17.8% | 43.5% |
| 2025 | 16.5% | 22.8% | | 17.0% | 44.5% |

Sources: FY2016 10-K `0001558370-17-000944` (2014-16), FY2019 10-K `0001558370-20-001788` (2017-19), FY2022 10-K (2020-22),
FY2025 10-K (2023-25); gross margins from each MD&A; consolidated margins are reported operating income over net sales. In
the 2008-09 recession, before Nalco, the consolidated operating margin was 11.6% (2008) and 11.5% (2009) against 12.2% (2007)
and 13.3% (2010) (XBRL company facts, transcription, flagged).

**Pricing through the last inflation, the filer's sales bridge** (MD&A, "components of the year-over-year sales change"):

| Year | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Volume | 0% | (1)% | 3% | 4% | 0% | (9)% | 3% | 2% | 0% | 2% | 1% |
| Price | 0 | 0 | 1 | 2 | 2 | 2 | 2 | 10 | 8 | 2 | 2 |

The FY2022 MD&A: "accelerating pricing covering substantially higher delivered product costs"; the FY2023 MD&A: "Our gross
profit increased as our strong pricing exceeded substantial delivered product cost inflation." Gross margin fell from 41.4%
(2020) to 37.8% (2022) and rose to 44.5% (2025), three points above where the inflation found it. The 2026 second-quarter
release (`0001628280-26-049933`) reports "strong pricing offset rising commodity costs" again.

**The competitor row** (operating income over sales, from the rivals' own filings):

| Rival | field | years | operating margin | source |
|---|---|---|---|---|
| JohnsonDiversey / Diversey Holdings, Inc. | institutional and food hygiene | 2006-2010 | (4.4)%, 2.2%, 4.0%, 6.4%, 8.2% | 10-K FY2010, CIK 1262768, `0001193125-11-069837`, selected financial data |
| Diversey Holdings, Ltd. | institutional and food hygiene | 2019-2022 | 2.6%, 2.3%, (0.4)%, (4.1)%; net losses every year | XBRL company facts CIK 1831617 (10-Ks `0001628280-22-005909`, `0001628280-23-008499`); bought by Solenis in 2023 |
| Ecolab, same years | | 2007-2010 / 2019-2022 | 12.2%, 11.6%, 11.5%, 13.3% / 13.5%, 11.8%, 12.6%, 11.0% | above |
| Veralto, Water Quality segment (Hach, Trojan, ChemTreat) | water treatment and analytics | 2021-2025 | 21.9%, 23.1%, 24.0%, 24.5%, 25.4% | 10-K FY2023 `0001967680-24-000033`, 10-K FY2025 `0001967680-26-000011`, segment note |
| Rollins (Orkin) | pest | 2019-2025 | 15.7%, 17.4%, 18.5%, 18.3%, 19.0%, 19.4%, 19.3% | XBRL company facts CIK 84839 (10-K FY2025 `0000084839-26-000008`) |
| Ecolab Pest Elimination | pest | 2023-2025 | 19.2%, 18.4%, 19.4% | FY2025 10-K segment note |

Flagged, not SEC filers, no comparison made: Kurita Water Industries (Japan), Solenis (private; owner of Diversey since 2023),
Veolia Water Technologies (France; holds the former GE Water and Suez water-treatment business), and ChemTreat, which Veralto
does not report apart from its Water Quality segment, so the closest water-chemicals rival's own margin is not on the record.
Diversey was a filer under two registrants (2003 to 2011 and 2021 to 2023), not only 2021 to 2023 as the brief has it.
Rentokil Initial files a 20-F (CIK 930157) and was not read. Nalco's own 10-Ks before 2011 were not read.

**The field's returns over the last full cycle, judged in words** (section C). The cycle read is 2019 to 2025: a pandemic trough
(2020), a raw-material inflation (2021 to 2023) and a recovery. Ecolab's return on the tangible capital the business needs is
very high and held across a decade: in 2025, operating income before acquired-intangible amortization of $3,041M against about
$4.4B of tangible capital (equity $9,771M plus debt $8,236M less cash $646M, goodwill $9,227M and intangibles $3,688M); in 2016,
about $2.2B against about $3.1B on the same arithmetic (FY2016 and FY2025 balance sheets). On everything paid, goodwill
included, about 17% pre-tax in both years. The hygiene rival with its own filings earned little or nothing on sales across two
separate spans; the water rival with its own filings earns more on sales in a mix led by instruments; the pest rival earns
about what Ecolab's pest unit earns. This is not a standing castle that protects ordinary returns; "you can have only two
competitors and they’re still terrible businesses" **[M2013-052]** describes Diversey's side of the field, not Ecolab's.

**The castle tests, each with its filing fact.**
1. *Pricing power and the agony before a rise* **[M2005-020]**. The full inflation is the test: "over time the businesses with
   strong competitive positions manage to pass through increases in raw material costs" **[M2005-017]**. Price +10% and +8% in
   2022 and 2023 with volume +2% and flat, and gross margin back above its pre-inflation level by 2024, is the positive form:
   "Anytime you can charge more for a product and maintain or increase market share against wellentrenched, well-known
   competitors, you have something very special" **[M2000-031]** (share itself is not disclosed; volume held). Against: the
   risk factor that "multi-year contracts with some of our customers include terms affecting our pricing flexibility", and the
   lag of 2021 to 2022 before price caught cost, which is some agony.
2. *Would the customer still choose it over the low bid* **[M2017-009]**? Ecolab says it competes on "demonstrated value,
   technical expertise" (Water) and "superior value, premium customer support, training, service" (Institutional and Pest), and
   that customer-relationship intangibles from Nalco, Anios, CID Lines, Purolite and Ovivo have shown retention "aligned with our
   acquisition assumptions", with no impairment of goodwill or of the Nalco trade name since 2011. The product is cheap against
   what it protects (a boiler, a cooling tower, a health inspection); I read that as the low bid not being the buying test, but
   the filings give no price comparison against rivals. Partly answered.
3. *The money test* **[M2011-015]**: could a well-funded attacker displace it? The barrier the filing describes is the 25,000
   sales-and-service staff in about 170 countries and the installed dispensing and monitoring equipment (3D TRASAR). Diversey,
   with a private-equity owner's money, did not earn a profit on sales in 2021 or 2022 and was sold: a failed attack on the
   institutional side, on the record. On the water side the attackers (Veolia, Kurita, Solenis, ChemTreat) are not on the SEC
   record; I cannot say what they earn.
4. *The low-cost position*: no cost comparison is filed. The rows' form, "being a low-cost producer of something that’s
   essential to people, it’s going to be a very good business usually." **[M2004-091]**, cannot be shown from the filings;
   not credited.
5. *Unit volume*: volume positive in 2024 and 2025 after the price; sales did not "fall off a cliff" **[M2005-019]**.
6. *Widening or narrowing* **[M1999-108]**: Institutional fell to 8.9% in 2020 and recovered to 22.8%, above its 2014-19 band,
   "a cyclical problem, not a secular one" **[L1995-022]**; Water is inside its 13% to 18% band. Not narrowing on the evidence.
7. *What could destroy it* **[M2000-014]**: customer consolidation (risk factor), the regulatory push on ingredients (PFAS; the
   REACH revision expected in 2026), and management's own move into data-centre cooling and semiconductor water, fields where
   change is fast; and "one competitor is frequently enough to ruin a business." **[M2012-108]**. No filing fact shows any of
   these biting yet.
8. *Ask the competitors*: not done (no access); recorded as not done.

**Tenuous, or judged** **[M2000-019]**? The deciding part's castle is shown standing on a full cycle of price against cost, on
returns on tangible capital held for a decade, and against the one hygiene rival with filings. The water side's rivals' own
returns are not on the record, the weakest leg; it lowers certainty (Q7) rather than showing the castle open or unjudgeable.

- **VERDICT: IN.** Deciding part Global Water, castle standing; Institutional also standing; Pest at its filing rival's level;
  Life Sciences not judged and not deciding. "A truly great business must have an **enduring "moat"** that protects excellent
  returns on invested capital." **[L2007-004]**: the excellent returns are on the record and held through the inflation
  **[M2005-017]**.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
- **Return on the capital actually needed** "we’re defining it in terms of the capital actually needed in the business"
  **[M2010-090]**: about 68% pre-tax on tangible capital in 2025 and about 72% in 2016 (Q2 arithmetic); the measure is "return
  on tangible assets" **[M2011-060]**. Purchased goodwill is forgotten when judging the business and included when judging the
  allocation, "because we paid for it" **[M2011-060]**: on that basis about 17% pre-tax in 2016 and 2025.
- **Reinvestment to stand still and to grow.** Capital spending against depreciation (cash-flow statements of the 10-Ks above,
  $M): 2016 757 / 561; 2019 801 / 654; 2021 643 / 604; 2022 713 / 619; 2023 775 / 617; 2024 994 / 635; 2025 1,048 / 673; and
  $589M in the first half of 2026 against $455M a year earlier (10-Q). Capex was 5.0% of sales in 2021 and 6.5% in 2025.
  The filing names what it is for: customer-placed dispensing and monitoring equipment ("Investments in Equipment", Item 1) and
  "supply chain investments to secure supply and add new capacity in our Life Sciences business" (Item 1A), but gives no split
  between keeping the place and growth; the owner is entitled to the manager's best guess of the first **[M2000-144]** and the
  filing does not give it. The working-capital need is real: receivables, inventory and other assets absorbed $1.0B in 2022
  alone (cash-flow statement, FY2022 10-K) and released part of it in 2023.
- **The growth arithmetic.** Operating income before acquired-intangible amortization rose from $1,838M (2021) to $3,041M
  (2025), +65%, while capital employed (equity plus debt less cash) rose from about $15.6B to about $17.4B; but the growth was
  partly bought (Purolite $3.7B in 2021, Ovivo $1.6B in 2025; the surgical business sold for $0.89B in 2024) and partly
  price in an inflation. "we’re not earning a higher rate of return on capital than we were when we started. We just put way
  more capital into the business" **[M2023-081]** is the test; here the return on the whole capital paid held at about 17%
  pre-tax over a decade, so the added capital, purchases included, earned about what the old capital earned. The first half
  of 2026 adds CoolIT for $4.75B with no filed earnings yet.
- **WEIGHS FOR.** A business that "gives you more and more money" while the reinvestment earns "a **very satisfactory rate**"
  **[M1998-081]**, the second-best kind, nearer the best on tangible capital; the purchased growth is weighed at Q6.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
- **The balance sheets first, ten of them** **[M2025-032]** ($M, year-end; `tools/run.py` first-filed XBRL, read against the filed
  statements of the 10-Ks listed in Step 0; the 2020 drop is the ChampionX split-off):

| year | assets | equity | goodwill | intangibles | cash | receivables | inventory | debt (filed lines) | retained earnings | receivables / sales |
|---|---|---|---|---|---|---|---|---|---|---|
| 2016 | 18,330 | 6,901 | 6,383 | 3,818 | 327 | 2,341 | 1,319 | 6,687 | 6,975 | 17.8% |
| 2017 | 19,962 | 7,618 | 7,167 | 4,018 | 211 | 2,574 | 1,446 | 7,323 | 8,045 | 18.6% |
| 2018 | 20,074 | 8,003 | 7,078 | 3,798 | 115 | 2,662 | 1,546 | 7,045 | 8,910 | 18.1% |
| 2019 | 20,869 | 8,685 | 7,252 | 3,672 | 186 | 2,796 | 1,506 | 6,354 | 9,994 | 18.8% |
| 2020 | 18,126 | 6,166 | 6,007 | 2,977 | 1,260 | 2,274 | 1,285 | 6,687 | 8,243 | 19.3% |
| 2021 | 21,206 | 7,224 | 8,064 | 4,224 | 360 | 2,478 | 1,492 | 8,758 | 8,814 | 19.5% |
| 2022 | 21,464 | 7,236 | 8,013 | 3,681 | 599 | 2,698 | 1,793 | 8,580 | 9,319 | 19.0% |
| 2023 | 21,847 | 8,045 | 8,148 | 3,494 | 920 | 2,834 | 1,497 | 8,181 | 10,075 | 18.5% |
| 2024 | 22,388 | 8,757 | 7,907 | 3,309 | 1,257 | 2,865 | 1,465 | 7,565 | 11,517 | 18.2% |
| 2025 | 24,696 | 9,771 | 9,227 | 3,688 | 646 | 3,249 | 1,490 | 8,236 | 12,834 | 20.2% |
| 2026-06-30 | 29,927 | 10,084 | 9,419 | n/r | 5,135 | 3,453 | 1,644 | 13,176 | n/r | n/r |

  What moved and why. Goodwill and intangibles together exceed equity in every year (about $12.9B against $9.8B in 2025): the
  equity is the residue of purchases (Nalco, Champion, Purolite, Ovivo) and of $9.1B of treasury stock bought back (equity
  statement, FY2025 10-K). Retained earnings rose every year except the split-off year. Debt held between $6.4B and $8.8B for
  ten years and then rose to $13.2B by June 2026 to pay for CoolIT (the $5.1B of cash at June 30 was spent on 2026-07-02).
  Inventory is steady at 9% to 11% of sales; receivables drift up from 17.8% to 20.2% of sales, a reading to watch, not yet a
  tell (the 2025 rise came with the December Ovivo purchase and new business wins as the filer describes them). "what the
  figures are saying and what they don’t say and what they can’t say" **[M2025-032]**: they say a stable, cash-generative
  business whose balance sheet has been used repeatedly for purchases; they do not say what the customer contracts look like.
- **The real costs.** Depreciation 673 against capex 1,048 (2025): capex is the charge used, as depreciation falls short of it
  **[L2015-004]**. Stock pay $137M in 2025, deducted in owner cash ("the most egregious example" of costs owners are asked to
  ignore **[L2015-003]**). Restructurings: special (gains) and charges in every year read, $M pre-tax: 2014 83.1, 2015 482.6
  (Venezuela 289.3 within), 2016 105.5, 2017 62.2, 2018 136.3, 2019 259.8, 2020 312.0, 2021 266.8, 2022 261.0, 2023 133.9,
  2024 (183.6) net gain after the $382M gain on the surgical sale, 2025 162.6 (the "Total special (gains) and charges" lines of
  the FY2016, FY2019, FY2022 and FY2025 10-Ks), under named plans: the Nalco merger plan (2012-13), the Energy Restructuring
  Plan (2013-16), the Combined Restructuring Plan (2015-16), the 2017 actions, Accelerate 2020 (from 2018), the Institutional
  Advancement Program (2020), the Europe Program (2021), the Combined Program (2022-24) and One Ecolab (2024 on). They recur;
  they are costs: "we do not ask you to forget about those costs" **[M1999-023]**; telling owners year after year to ignore
  them "is misleading" **[L2016-007]**. Owner cash below is built from operating cash flow, which already carries their cash.
  Amortization of acquired intangibles ($304M in 2025) is non-cash and not deducted; customer relationships are the bulk, and
  the filing reports retention in line with the acquisition assumptions.
- **Pensions.** The expected return on U.S. plan assets was raised to 8.25% for 2025 (8.00% for 2024, 7.75% for 2023; FY2025
  10-K, critical accounting estimates) while the discount rate fell to 5.28%. The rows warn: "if its pension assumptions are
  fanciful, watch out." **[L2002-039]**; "The real lollapalooza is pension fund accounting" **[M2003-110]**. The expense effect
  is small (net pension and postretirement expense $15.0M in 2025; a quarter point of return is $4.4M), so it weighs against
  as a tell of attitude, not as a number.
- **EBITDA in the filer's own mouth:** not featured in the releases read; the featured figure is adjusted diluted EPS. The
  FY2025 10-K headline: "Adjusted diluted EPS [...] increased 13% to $7.53"; the 2026-07-28 release headline: "ADJUSTED DILUTED
  EPS $2.09, +11%" with "RAISES 2026 ADJUSTED DILUTED EPS OUTLOOK", quarterly and annual guidance, and amortization of the CoolIT
  intangibles called "non-cash" and taken out. The habits recorded here and carried to Q5 (section A of the gaps case): a
  featured adjusted figure **[L2016-006]**, earnings guidance **[L2019-006]**, and the annual bonus paid on "our
  pre-established adjusted EPS goal" (proxy), a declared target that was beaten (137% of target in 2025).
- **Confusion or suspicion?** The accounts are not confusing: segment, special-charge and organic reconciliations are full,
  the cash-flow statement ties to the income account, goodwill has never been impaired and the filer says why. No tell that
  lives in the accounts (prepaid or deferred accounts building, inventory out of line, reserves that move) was found in the
  balance sheets read. A management "preoccupied with accounting considerations" is "a negative", but "we can’t afford to use it as a
  total exclusionary factor" **[M1994-018]**.
- **VERDICT on the accounts: WEIGHS AGAINST** (no STOP): restructuring every year, a featured adjusted figure with guidance,
  and a raised pension return assumption, against accounts that are clear and cash that ties. **The recast earnings feed Q7**:
  owner cash after every real cost = operating cash flow less stock pay less all capital spending, with acquisitions treated
  under Q7's specific (c).

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
- **The people** (FY2025 10-K, executive officers; proxy `0001104659-26-032777`): Christophe Beck, chief executive since January
  2021 and chairman since May 2022 (combined roles; the proxy carries a stockholder proposal for an independent chair and names
  a Lead Director); Darrell Brown, president and chief operating officer; Scott Kirkland, CFO since 2022. All are long-serving
  Ecolab managers. For a marketable stock the speakers read rather than meet **[M2007-081]**.
- **The two yardsticks** **[M1994-008]**. *How well they run it, against the hand dealt:* the hand was the inflation of 2021 to
  2023 and the pandemic; the record is price +10% and +8% with volume held, gross margin from 37.8% to 44.5%, Institutional from
  8.9% to 22.8% (Q2). Against the one rival with filings (Diversey), the record is far better. *How they treat the owners:* read
  in the proxy, "how they treat themselves versus how they treat the shareholders" **[M1994-009]**: chief executive pay $17.4M
  for 2025 (pay-ratio disclosure); annual bonus on "our pre-established adjusted EPS goal", paid at 137% of target; long-term
  units on organic ROIC (adjusted ROIC before 2023) with a relative-TSR modifier and a 200% maximum; annual stock options at a
  fixed price (option tables, FY2020 and FY2025 10-Ks); no hedging or pledging, no single-trigger change-in-control benefits,
  no tax gross-ups; directors to hold five times the retainer.
- **The tells of dishonesty the rows name, searched for:** reports that dance **[M1995-111]**: not found; the special charges,
  organic measures and segment recasts are reconciled line by line in each 10-K. Numbers obscured **[M2003-029]**: not found.
  Stock price posted in the lobby **[M2004-067]**: the releases lead with records and adjusted growth, not the stock price.
  Serial issuance **[L2014-015]**: no; the share count fell from about 299M diluted (2012) to 285M (2025) (XBRL, transcription),
  with one large stock issue (Nalco, 2011). Government investigation or restatement: none found in Note 15 of the FY2025 10-K
  (litigation note read; the TPC Group explosion suits against Nalco are product-liability claims, not conduct of the company's
  managers) or in the risk factors. How they talk of mistakes **[L2024-003]**: the energy exit (a $2.1B loss on separation,
  FY2020 10-K Note 5) is described as a "strategic shift", not as an error; no letter acknowledging a mistake was read.
- **The habits carried from Q4**, read with the record: a featured adjusted figure **[L2016-006]**, quarterly and annual
  guidance **[L2019-006]**, and a declared target beaten **[L2002-041]**. They are "things that they do in public in relation to
  their investors and the promises they make" **[M2004-067]**. Read with the rest: the adjusted figure is reconciled to GAAP in
  every release, the charges it removes are disclosed by plan and by year, and nothing in the accounts raised suspicion at Q4.
  The habit is the common one, and the rows that condemn it condemn the culture it breeds **[L2016-006]**; I record it as the
  strongest thing against the people. Does it leave me in doubt about their honesty **[M2013-088]**? It leaves me doubting their
  candour about what the business earns (restructuring is presented as outside normal earnings every year for twelve years), not
  their honesty in what they report. On the evidence read, no doubt about integrity.
- **Love of the business:** not readable from outside beyond the record; the managers are career Ecolab people (10-K officer
  table), which is weak evidence for the business over the money.
- **VERDICT on integrity: IN** (no tell of dishonesty found; the habits weigh against and are carried into Q6 Part B).
  **Ability WEIGHS FOR**: the inflation record against the hand dealt **[M1994-008]**.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
**Part A, the money.**
- *The retention test* **[R1995-009]**, five years 2021 to 2025: net income $7,782M (XBRL, 10-K values), dividends paid $3,204M,
  buybacks $2,409M (cash-flow statements). Market value at 2020-12-31 about $61.8B (285.75M shares, the FY2020 10-K share table:
  362,553,443 issued less 76,801,025 in treasury, at $216.36) and at 2025-12-31 about $74.0B (282.0M at $262.52); closes from the
  aggregator, flagged. Market value rose about $12.2B against about $4.6B of earnings kept after dividends: the market leg
  passes. The intrinsic leg (Q7) does not support it: owner cash grew 7.7% a year while the multiple of it the market pays rose,
  so most of the market gain is the price of the stock, not the value per dollar kept **[R2009-002]**.
- *Buybacks* **[L1999-023]**: the authorization of November 2022 is 10,000,000 shares "Subject to market conditions", with "no
  expiration date", and names no price (FY2025 10-K, Item 5); "repurchase announcements almost never refer to a price above which
  repurchases will be eschewed" **[L2016-002]**. Prices paid: October to December 2025, 1,514,808 shares at an average of $263.91
  (Item 5); 2024 $986M, 2025 $784M, first half 2026 $669M (cash-flow statements), at year-end prices of $234 to $263. The
  framework's test reads the prices paid against the bottom of the Q7 range: every construction's bottom (Q7: $61.32 a share at
  most) and every top ($158.97 at most) sits far below the prices paid. **Weighs against**: "If you’re repurchasing shares above a
  rationally calculated intrinsic value, you are harming your shareholders" **[M1996-013]**.
- *Issuance and deals, value given against value got* **[M1995-001]**, **[L2014-012]**:
  - Nalco, 2011-12-01: total consideration $5,495.0M, each Nalco share converted at the holder's election into 0.7005 Ecolab
    shares or $38.80 cash, about 70% in stock, plus $2,858.4M of Nalco long-term debt assumed (FY2011 annual report, Exhibit 13 of
    `0001104659-12-014104`). The water part of Nalco is now the deciding part and its returns hold (Q2). Whether Ecolab's stock was
    below its value when it was given is not knowable from what I read; the all-stock STOP **[L2009-019]** does not apply to a deal
    30% in cash and is not tested.
  - The energy business (Nalco's energy services, and Champion, bought 2013): split off 2020-06-03; Ecolab gave net assets of
    $3,486.7M and received 4,955,552 of its own shares (fair value $1,051.4M) and $527.4M in cash, a recorded loss on separation
    of $2,137.8M (FY2020 10-K, Note 5). A large part of what was paid for energy was given away again. The rows ask for the honest
    post mortem **[L2014-013]**; none was found in the filings read.
  - Purolite, 2021-12-01: $3.7B in cash, net of cash acquired (FY2022 10-K); Life Sciences operating income (recast) was $118.9M,
    $91.8M and $120.7M in 2023 to 2025 against $147.2M and $160.8M as first reported for the old Healthcare & Life Sciences
    segment in 2024 and 2023; on the recast segment the return on the $3.7B is thin so far.
  - Surgical solutions business sold 2024-08-01 for $889.7M net (cash-flow statement), a $381.7M gain.
  - Ovivo Electronics, 2025-12-16, $1.6B cash; CoolIT Systems, 2026-07-02, $4.75B cash, funded by $5.0B of new notes (10-Q). Both
    are data-centre and semiconductor businesses, outside the castle read at Q2; CoolIT has no filed earnings in Ecolab's hands.
  - Weighs against: the record contains one large deal that worked (Nalco water), one that was reversed at a $2.1B loss (energy),
    one whose return is thin so far (Purolite), and $6.35B committed in nine months to a field of fast change.
- *Dividends*: paid every year for 89 years, raised 34 years in a row (Item 5); $754M in 2025, about 36% of net income. A steady
  dividend is consistent with the rows **[L2012-015]**.

**Part B, the pay, the board and the owners.**
- Pay tied to what the person controls **[M2003-019]**: the bonus metric (adjusted EPS) excludes the restructuring charges the
  managers choose to take every year; the long-term metric (organic ROIC) is a capital measure, which the rows favour
  **[L1994-019]**, but organic and adjusted. The fixed-price ten-year option has no step-up for retained earnings, "a royalty on
  money that you left with me" **[M1997-043]**. **Weighs against.**
- The board: chief executive also chairman **[L2014-026]**, a lead director, a stockholder proposal for an independent chair;
  directors paid about $324,000 to $328,000 each in 2025 (director compensation table), half in stock; whether any bought shares
  with their own savings **[L2019-008]** was not found. **Undecided.**
- Owners as partners: guidance given **[L2019-006]**; the adjusted figure leads. **Weighs against.**
- **Part A WEIGHS AGAINST; Part B WEIGHS AGAINST.**

## Q7 — WHAT IS IT WORTH? STOP.
Value is "the **discounted value of the cash that can be taken out of a business during its remaining life**" **[R1996-018]**,
at the long government rate **[L2000-021]**, held as a range **[L2000-024]**. Arithmetic in
`Test Runs/_research 2026-10-07 ECL/q7_calc.py` (inputs transcribed from the filed cash-flow statements; output reproduced here).

- **Owner cash after every real cost** (Q4), $M: operating cash flow less stock pay less all capital spending, 2021 to 2025:
  1,329.4 / 987.8 / 1,541.9 / 1,684.6 / 1,767.7, average **1,462.3** (equity-only, after interest). On the all-equity basis
  (Q7, On what the floor is earned) net interest paid is added back after the company's own tax rate of each year (provision over
  pre-tax income, 17% to 21%): 1,498.2 / 1,171.4 / 1,799.7 / 1,968.7 / 2,016.3, average **1,690.9**. Tax is the company's own; no
  carryforward shelter that runs out inside ten years was found, so no statutory recomputation (Whose tax).
- **The window and the specifics.** (a) Cycles: the window 2021 to 2025 contains the inflation trough (2022, working capital
  absorbed $1.0B) but neither end year is described by the filer as aberrational; the literal window is the base. (c)
  Acquisitions: net acquisitions $3,923.7 / 7.2 / 180.4 / (576.8) / 1,636.2, average **1,034.1** (acquisitions less divestitures,
  cash-flow statements). Default pair: acquisitions deducted, total growth credited (all-equity owner cash grew 7.71% a year,
  2021 to 2025). Beside it: acquisitions left out, organic growth credited; the filer reports organic sales growth (5%, 13%, 9%,
  4%, 3%; compound 6.74%), not organic owner cash, so the organic sales rate is used: **CONVENTION of this run**, rationale: it is
  the only organic rate the filer reports, and it flatters the case because two of the five years are inflation pricing. (d)
  Working capital: inside operating cash flow, counted. (e) Growth spending: the filing gives no maintenance figure (Q3), so the
  central case charges all capital spending; the depreciation-only case is shown beside as a guess, depreciation being "not
  inappropriate in most companies to use as a proxy for required capital expenditures" **[M1998-127]**. (f) Cap: 7.71% and 6.74%
  are above the 5.64% rate but are carried for ten years only, then zero nominal growth; nothing traces to an absurdity. The
  deal after the window: CoolIT ($4,750M cash, 2026-07-02) is valued on its own filed record, of which there is none in Ecolab's
  hands, so it is credited at nothing and its price is added to net debt.
- **Net debt** (10-Q 2026-06-30): short-term debt $1,271.1M plus long-term debt $11,905.1M less cash $5,135.3M, plus CoolIT
  $4,750.0M paid on 2026-07-02 (the 10-Q's own subsequent event) = **$12,790.9M**; operating leases ($576.7M non-current) left
  out, said so. Enterprise value at the price: $78,282M + $12,791M = **$91,073M**.

| construction (all-equity, at 5.64%) | base $M | growth | whole business $M | per share | top / bottom |
|---|---|---|---|---|---|
| **default: acquisitions deducted, total growth** | 656.7 | 7.71% | 11,644 to 21,450 | **$(4.09) to $30.89** | 1.84 |
| beside: acquisitions left out, organic growth | 1,690.9 | 6.74% | 29,980 to 51,146 | $61.32 to $136.82 | 1.71 |
| beside: depreciation for capex (a guess), organic | 1,896.1 | 6.74% | 33,620 to 57,355 | $74.30 to $158.97 | 1.71 |

  The literal window is shown (2021 to 2025); no cycle base replaced it. Purolite ($3.9B, December 2021) dominates the default
  pair's deduction; the organic pair shows the case without it.
- **The price against the range.** $279.25 a share against a top of $30.89 (default) and $158.97 (the most generous
  construction, which leaves out $5.2B of purchases and charges only depreciation). The owner cash yield at the price is 1.86%
  (all-equity owner cash $1,690.9M against an enterprise value of $91,073M), against a floor of about ten percent and a long bond
  at 5.64%. The ranges are narrower than three to one, so the close is not TOO HARD; a price above the top of the range "closes
  OUT however wide the range, by the floor convention" (Q7, specific f), "a point at which we drop out of the game" **[M2003-149]**.
- **Fair price (a reporting figure, never a verdict; Part VII; the brief's reporting convention).** Reading used here: the price
  at which the range's midpoint case (half the shown growth for ten years, then none) returns ten percent, on the company's own
  tax. **All-equity (central): no positive price** on the default pair (the computation gives $(15.14) a share: the midpoint
  case at ten percent is worth $8,548M against $12,791M of net debt); **$30.29** a share on the organic pair; $39.51 on the
  depreciation guess. **Equity-only, beside:** $19.66 (default) and $65.66 (organic pair), owner cash after interest against the
  market value alone. No cheap price is reported.
- **VERDICT: OUT.** Valued; the price is far above every construction of the range and the expected return at the price is far
  below the floor **[M2003-149]**, **[M1994-004]**. Not a close call: "It should scream at you." **[M2009-005]** runs the other way.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED (Q7 closed the file OUT).

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. Facts under AFTER THE STOP.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED. Facts under AFTER THE STOP.

---
## THE BOX
**OUT at Q7**, by the floor: value range **$(4.09) to $30.89** a share on the default all-equity construction (organic pair
$61.32 to $136.82; depreciation guess $74.30 to $158.97; window 2021 to 2025) against **$279.25**. Q1 IN, Q2 IN (Global Water
deciding, castle standing), Q3 WEIGHS FOR, Q4 WEIGHS AGAINST, Q5 integrity IN and ability WEIGHS FOR, Q6 WEIGHS AGAINST in both
parts. Q11 belongs to the holding review.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Q7 closed the file; written down, not weighed **[M1997-127]**; the box unchanged.)*
- **Q8:** the long bond at 5.64% against an owner-cash yield of 1.86% at the price (Q7 arithmetic).
- **Q9:** debt $13,176.2M at 2026-06-30, of which $1,265.7M current maturities; notes due 2026 ($750M), 2027 ($500M and $500M),
  2028 ($500M and $500M), 2029 ($1,200M) and later (10-Q debt note); a $2.0B revolving credit facility; about $1.5B of floating
  rate debt at 2025-12-31; ratings A-/A3/A- (FY2025 10-K). Coverage on 2025 figures, pre-tax income plus interest over interest
  ($2,548M + $306M) / $306M, about 9.3 times **[L2012-002]**, before the CoolIT notes. Indemnities to and from ChampionX, and the
  tax-free status of the 2020 split-off rests on counsel's opinion, not an IRS ruling (risk factors). Product-liability suits from
  the 2019 TPC Group explosion against Nalco (Note 15); TPC's own estimate of its liability to individuals was $152M to $520M.
  Pension: expected return 8.25% (Q4).
- **Q10:** nothing beyond Q7.
- **Q12:** cleaning, water treatment, pest and contamination-control products; none of the businesses the rows name.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 29f06775); written question by question; committed after each with a
      pathspec of the run file and the research folder (Q3 and Q4, Q5 and Q6 each in their own commit). Departure declared: the
      first session was stopped by a time limit after the template commit; the questions were written after the restart from
      the research already in the folder.
- [x] Dispatched: the brief allowed per-question commits; the lock is the dispatching session's; the run binds nothing until
      folded into the register.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened or searched. One listing of `Test Runs/` filtered on
      today's date was made before the blind rule was read; what it and the session context showed is declared under
      contamination above and was not used.
- [x] Every v5 id checked against `principle_ledger_v5.csv` by `Test Runs/_research 2026-10-07 ECL/check_ids.py`; every filing
      fact carries its accession; numbers from the XBRL company facts are labelled as transcription.
- [x] The order was kept; the first STOP that failed (Q7) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost from operating cash flow less stock pay less capital spending, never net income; the
      sovereign from the Treasury; aggregator quotes (today's price and the year-end closes in Q6) flagged.
- [x] Contrary evidence written down as found (foundations list; Q2 test 7; Q4; Q6); facts for later questions are under AFTER
      THE STOP; no integrity facts against the people were found, so no flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` used; its debt "sum" was not used (Step 0).
- [x] `python tools/check_framework.py` run before the closing commit (result recorded in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
1. **The fair price is negative on the default pair**, and the text does not say what to report when the midpoint case at ten
   percent is worth less than net debt. I reported "no positive price" with the computed figure beside it. The same specific (c)
   that sets the default pair (acquisitions deducted, total growth credited) lets one purchase at the window's first year
   (Purolite, $3.9B in December 2021, earning in the following four years) drive the base to a third of the business's own
   owner cash; the text has a cycle rule for aberrational earnings years but none for a lumpy acquisition year, which is the same
   problem in the deduction. I showed the organic pair beside; the box does not depend on it.
2. **"Organic growth, as the filer reports it"** (specific c) assumes the filer reports organic growth of the quantity being
   valued. Ecolab reports organic sales, not organic owner cash or organic operating income for every year (2024 is "not
   meaningful" in the FY2025 10-K); I used organic sales growth and confessed it as a CONVENTION of this run.
3. **"Fair price ... the price at which the midpoint of the range earns the floor"** does not say whether "midpoint" is the middle
   value of the range or the middle growth case; at a different discount rate these differ. I used the middle growth case
   discounted at ten percent and said so.
4. **Q5's "doubt closes"** with Q4's habits carried in: the text does not separate doubt about candour (the adjusted figure that
   leaves out twelve straight years of restructuring) from doubt about honesty. I judged the first a weight and the second the
   STOP, and wrote the reasoning down; another analyst could read the same facts as doubt.
5. **The brief** names the segments as "Global Industrial, Global Institutional & Specialty, Global Healthcare & Life Sciences,
   Global Pest Elimination"; since 2025-01-01 they are Global Water, Global Institutional & Specialty, Global Pest Elimination and
   Global Life Sciences, with healthcare moved into Institutional (FY2025 10-K, Note 18). It says Diversey "was a filer 2021 to
   2023"; it was also a filer from 2003 to 2011 as Diversey Holdings, Inc. (CIK 1262768), which gave the comparison its second
   span. It does not mention CoolIT Systems ($4.75B, closed 2026-07-02), the largest event in the name's recent record.
6. **`tools/run.py`** adds a non-current operating-lease line into its debt "sum" for 2022 to 2025 while its footnote says leases
   are not in it.
