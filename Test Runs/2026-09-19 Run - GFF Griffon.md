# Company Run — GRIFFON CORPORATION (GFF) — 2026-09-19
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

**WAVE 6** of `Screens/WATCHLIST RUN QUEUE.md` — one of the eleven businesses the 2026-09-01
triage dropped and the operator's screenshots recovered on 2026-09-19. **No reason exists on
disk for the drop.** Read as UNLABELLED: nothing on disk says which gate would be short.

---
## THE FOUR VERDICTS — every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order — not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in.** Griffon earns overwhelmingly in USD
(see Q1 for the geographic split as filed).
- rate **5.34%** · date **2026-09-18** · source **US Treasury daily par yield curve, 30-year,
  from the issuing authority** (`python tools/sources.py`, struck 2026-09-19)
- FX: not required. The subject reports in USD and is a US domestic filer.

**CIK found independently, not taken from the brief:** `tools/sources.py:cik_for('GFF')` →
**`0000050725`, "GRIFFON CORP"**.

*(sections below filled as each closes — write-early protocol)*

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary document:** Form 10-K for the fiscal year ended **2025-09-30**, filed **2025-11-19**,
  accession **0001628280-25-053242** (`gff-20250930.htm`).
- **Second primary document, and it is the one that governs the business description:** Form 10-Q
  for the quarter ended **2026-06-30**, filed **2026-08-05**, accession **0001628280-26-053536**
  (`gff-20260630.htm`). **The 10-K describes a company that no longer exists** — see the perimeter
  note below.
- Also read: 10-K FY2024 (`0000050725-24-000152`), FY2023 (`0000050725-23-000055`), FY2022
  (`0000050725-22-000090`), FY2021 (`0000050725-21-000068`); DEF 14A filed 2026-01-09
  (`0000930413-26-000074`) and 2025-01-27 (`0000930413-25-000212`); 8-K EX-99.1 earnings releases.
- **Figures cross-checked against the filed statements (two, by hand):**
  1. **Balance-sheet identity, FY2025 10-K:** Total Assets $2,063,637 − Total Liabilities
     $1,989,665 = **$73,972**, which is the filed Total Shareholders' Equity to the dollar. Equity
     recomputed from A−L per **[E5-32]** — audited is not bedrock.
  2. **Cash-flow statement, FY2025, summed line by line:** 51,110 + 63,014 + 25,483 + 243,612 +
     566 + 4,176 − 28,485 − 8,279 + 18,850 − 18,307 − 14,166 + 17,870 + 1,996 = **$357,440**,
     the filed "Net cash provided by operating activities". The detail lines reconcile.

### THE PERIMETER — read this before any number below
**Griffon dismantled half of itself between February and July 2026, and the FY2025 10-K does not
describe the company whose shares are quoted today.** From Note 1 and Note 16 of the Q3 FY2026
10-Q:
- **2026-02-05** announced a JV with ONCAP (Onex) combining **AMES North America** with Venanpri's
  Bellota / Corona / Burgon & Ball; **closed 2026-06-09**. Griffon received **$100,000 cash**, a
  **$161,100 second-lien PIK debt receivable**, and a **43% equity interest carried at $118,600**.
  The JV is named **Veritage Brands** and is *"managed as a subsidiary of Venanpri"*; ONCAP holds
  57%. Griffon recorded a **$26,603 loss on the sale**.
- **2026-07-31** completed the sale of **AMES Australasia** to a management-led JV: **AUD 258,000
  (USD 180,910) cash**, an **AUD 69,300 (USD 48,593) PIK note**, and a **49% stake carried at AUD
  29,800 (USD 20,896)**. Estimated gain **~$123,000 ($112,000 net of tax)**, to be recorded in
  Q4 FY2026.
- **AMES U.K. ceased operations as of 2026-03-31** and is being liquidated; charges **$25,913**.
- **All AMES operations are discontinued operations in every period presented**, and **Griffon now
  reports ONE reportable segment** (10-Q Note 13: *"Subsequent to the actions discussed in Note 1,
  Griffon now conducts its operations through one reportable segment. All prior period comparative
  information has been conformed to this reporting structure."*)

**So the brief's instruction to build Q1 on "the two segments as filed (Home and Building Products;
Consumer and Professional Products)" describes the FY2025 10-K and not the company.** Recorded as a
defect in the brief; the run is built on the continuing perimeter. **The brief also names a
"2023-24 disposal" for the CNR rule; no 2023-24 disposal exists.** The disposals that bite are
Telephonics (2022) and AMES (June–July 2026).

#### PERIMETER ADDENDUM, 2026-09-19 (resuming session): the three August 2026 8-Ks, read
*The note above stops at 2026-07-31. The killed session had fetched the August 8-Ks and not opened
them. They are read here, in full, and nothing above is edited (operator rule 6).*

| 8-K | accession | what it says | changes what a share buys? |
|---|---|---|---|
| filed 2026-08-04, event 2026-07-31 | `0001628280-26-052181` | Item 2.01: AMES Australasia sale closed; *"Griffon HoldCo received AUD $258 million (USD $181 million) in cash at closing and an AUD 69.3 million (USD $48.6 million) PIK note"*, 10% a year, capitalised, maturing *"the later of six years from the date of issuance"* or 12 months after an extended senior facility, *"but in no event later than 10 years"*, subordinated, and *"Griffon has agreed not to demand or receive payment, or take enforcement action, while any amount remains outstanding under the senior debt facility."* Item 8.01: *"On July 31, 2026, we repaid the remaining balance of $285 million of Term Loan B"*. EX-99.2 is the Article 11 **pro forma** for FY2023, FY2024, FY2025 and H1 FY2026. The exhibits the brief called "projectbourne" are **EX-2.1, a side letter to the share sale agreement headed "Project Bourne"** (the deal code name), and **EX-4.1, the PIK note itself**. | **No new business.** Confirms the Australasia terms already in the perimeter note, and adds the **Term Loan B repayment**, a capital-structure fact (Q4). |
| filed 2026-08-11, event 2026-08-10 | `0001628280-26-055694` | Item 1.01: *"a Purchase Agreement ... pursuant to which the Company agreed to issue and sell to the several initial purchasers ... $800 million aggregate principal amount of the Company's 6.25% senior notes due 2034"*. EX-99.2: proceeds *"together with cash on hand and revolver borrowings"* to *"redeem all $975 million aggregate principal amount of Griffon's outstanding 5.75% Senior Notes due 2028"*. | **No.** The "purchase agreement" the brief flagged is **a note purchase agreement with the underwriters, not an acquisition.** Capital structure only. |
| filed 2026-08-19, event 2026-08-18 | `0000930413-26-002595` | Notes closed, *"net proceeds to the Company from the Notes Offering were approximately $792 million"*; mature **2034-10-01**, senior unsecured, guaranteed by Clopay, CornellCookson, Hunter Fan and others; redemption notice for all 2028 notes (*"Following completion of the redemption, none of the 2028 Notes will remain outstanding"*); revolver replaced by a **$500 million facility maturing 2031-08-18**. | **No.** It moves every debt maturity out to 2031 (revolver) and 2034 (notes). This bears on Q4 strength (3), and it is carried there. |

**What a share buys today, stated once so every later section uses it:** the Clopay door business;
Hunter Fan; 43% of Veritage and 49% of the Australasia JV (equity method); PIK receivables of
$161,100 (Veritage, 10%, due 2029-12-09, per the pro forma note 3(d)) and $48,593 (Australasia);
against debt that after 2026-08-18 is **$800,000 of 6.25% notes due 2034 plus revolver drawings**
(the revolver balance after the redemption is not yet filed; it will be in the FY2026 10-K).
**No acquisition, no new segment, no disposal beyond those in the note above.** The perimeter note
stands as written.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### Unit economics, in my own words, no management language
**Griffon today is two factories-and-trucks businesses inside one holding company, plus two
minority stakes in businesses it used to own and about $210M of paper owed to it by them.**

**1. Doors (Clopay, Ideal, Holmes, Cornell, Cookson) — nearly all of it.** Griffon buys galvanized
steel coil, hardware, aluminium and insulating foam, and stamps, forms, insulates and paints it
into sectional garage doors and rolling steel doors at four principal plants (1,625,000 sq ft at
Troy and Russia, Ohio; 279,000 at Mountain Top, PA; 163,000 at Goodyear, AZ). Doors are bulky,
easily damaged in transit, and ordered in a particular size, colour and panel style, so Griffon
pays to hold finished doors close to whoever installs them: **57 distribution centres, about
1,300,000 sq ft, across the US and Canada**. It sells to **over 3,000 independent professional
installing dealers** and to two retailers. The money is the gap between (steel + labour + freight +
the cost of carrying that inventory) and the price an installing dealer or a retailer will pay, and
what the dealer is really buying is **lead time**: the door is there this week.

**2. Ceiling fans (Hunter, Casablanca, Jan Fan).** Griffon designs fans, has most of them made by
third parties in Asia (*"The percentage of HBP and CPP worldwide sourced finished goods as a percent
of revenue approximated 6% and 38%"*, FY2025 10-K), and sells them to home centres, e-commerce
platforms and industrial/commercial installers. The money is the gap between a landed unit cost and
a shelf price, and the asset is a name stamped on a box.

**3. Two minority stakes and two IOUs.** 43% of Veritage and 49% of AMES Australasia, equity method,
**recorded on a three-month lag and carrying no recognised earnings in any period presented**; plus
PIK notes of $161,100 and $48,593, which pay no cash until maturity.

**The filed arithmetic, continuing operations, nine months to 2026-06-30:** revenue **$1,357,490**;
gross profit **$626,776 (46.2%)**; SG&A $324,515; operating income **$302,261 (22.3%)**; interest
expense $64,254; income before tax $232,669. Revenue by end market: residential repair and remodel
**$723,727 (53.3%)**, commercial **$536,714 (39.5%)**, residential new construction **$97,049
(7.1%)**. **96% of revenue is US** (10-Q Note 13), so the sovereign is USD without qualification.

**For reference, the segments as last filed separately (FY2025 10-K Note 19) — the last honest
picture of the two halves:**

| | revenue FY2025 | Segment Adj. EBITDA FY2025 | margin | revenue FY2023 | Adj. EBITDA FY2023 |
|---|---|---|---|---|---|
| Home and Building Products | $1,584,182 | $494,576 | **31.2%** | $1,588,505 | $510,876 (32.2%) |
| Consumer and Professional Products | $935,744 | $85,545 | **9.1%** | $1,096,678 | $50,343 (4.6%) |

**One half earned three times the margin of the other, and the low-margin half is the half now
gone.** Note the measure: the company's own CODM measure was **segment adjusted EBITDA**, struck
before $63,014 of D&A, $57,828 of unallocated corporate cost, $93,857 of net interest and every
impairment and restructuring charge. It is not earnings, and this run never treats it as such
(see Q3, **[E4-29]**).

### The scarce input this business controls
**Not steel** — the filing says raw materials *"are generally available from a number of sources."*
The scarce input is **presence at the moment a door is chosen**, and it has three physical parts:
(1) the 57-depot network holding made-to-order inventory within a day of the installer;
(2) **the exclusive shelf**: *"Clopay is currently the exclusive supplier of residential and
commercial garage doors to Home Depot and Menards locations throughout North America, and has
maintained long-standing relationships with Home Depot for 40 years and with Menards for over 30
years"*; and (3) the 3,000-dealer relationship, mediated by software the dealers quote and order
through (MyClopay, MyDoor, Commercial Door Quoter). A new entrant can buy a press; it cannot
quickly buy 57 buildings, 3,000 dealers and forty years at Home Depot.
**For fans there is no scarce input I can name** — the product is sourced, and the filing itself
says the principal competitors are *"retailer house brands such as Hampton Bay in The Home Depot
and Harbor Breeze in Lowe's."* That belongs at Q2.

### Customer concentration — first, from the 10-K, as the brief requires
- **Home Depot = 10% of FY2025 consolidated revenue, 9% of HBP revenue, 12% of CPP revenue.**
  *"No other customer accounted for 10% or more of consolidated revenue."*
- Home Depot is also **9% of consolidated net accounts receivable** (6% of HBP's, 14% of CPP's).
- **Named significant customers:** HBP — Home Depot and Menards (exclusive on doors). CPP — Home
  Depot, Lowe's, Bunnings. *"The loss of either of these customers would have a material adverse
  effect on Clopay and Griffon."*
- **On the continuing perimeter the concentration is LOWER than the headline suggests, not higher:**
  Home Depot was 9% of HBP, HBP is now nearly the whole company, and the retail channel is only part
  of it — **over 3,000 independent installing dealers** carry the rest. The 12%-of-CPP half of the
  concentration left with AMES. This is the opposite of what the brief's framing implies and is the
  single most important Q1 correction.

### Will the fundamentals look broadly the same in ten years?
**For doors, yes.** A garage door is a stamped steel panel on a track; the FY2025 filing's own
demand drivers are the age of the housing stock, existing-home sales, and the age of
non-residential buildings. 53% of continuing revenue is repair and remodel of doors that already
exist. Nothing in the filing describes a technology that replaces a door.
**For fans, less so** — a sourced consumer good sold against the retailer's own label, whose
five-year record inside Griffon is a write-off (Q3).

**Can I name the document that would resolve anything left open?** Nothing is left open at Q1. The
business is two product lines, one currency, one country, presented as one segment with the end
markets disaggregated.

- **VERDICT: [x] IN**  ·  *It is relatively simple and stable in character, and the unit economics
  can be written without the company's words.* **[E3-31]**

## Q2 — IS IT A FRANCHISE? **[E3-03]**

*Read on the perimeter that exists: Clopay (doors, ~88% of continuing revenue) and Hunter Fan
(~12%, derived below). The two are tested separately, because they answer differently.*

- **Needed or desired [x]** — a garage door is not optional on a house that has one, and **53.3%
  of continuing revenue is repair and remodel** of doors already installed.
- **No close substitute — PARTIAL, and this is where the file turns.** The filing's own
  competition section says: *"The sectional garage door and commercial rolling steel door industry
  includes several large national manufacturers and many smaller, regional and local
  manufacturers. Clopay competes on the basis of service, quality, brand awareness, product design
  and price."* **A filer that says it competes on price is not asserting the absence of a close
  substitute.** In the retail channel the substitute is absent by contract — *"Clopay is currently
  the exclusive supplier of residential and commercial garage doors to Home Depot and Menards"* —
  but that absence is the retailer's to grant and to withdraw. **For fans, criterion 2 fails on the
  filing's own words:** *"CPP's principal competitors in the consumer ceiling fan market are
  retailer house brands such as Hampton Bay in The Home Depot and Harbor Breeze in Lowe's, followed
  by Minka Air."* The customer is the substitute.
- **Not price-regulated [x]** — no rate regulation of garage doors is disclosed anywhere in the
  filing.

### Must the moat be continuously REBUILT, or only defended? **[E4-04]**
**Defended, not rebuilt.** A sectional garage door is a stamped, insulated steel panel on a track;
nothing in five 10-Ks describes a technology change that obsoletes the product, the plant or the
57 depots. Capex has run **$31.4M (FY2023), $50.3M (FY2024), $41.7M (FY2025)** on the continuing
perimeter against D&A of $35.5M / $35.9M / $38.5M — maintenance-scale spending that **defends the
same advantage** rather than buying its replacement, which is the test the corpus sets
(*"certainly should be working at improving your own moat and defending your own moat all of the
time"* **[E5-23]**; the canonical franchise treated maintenance as *"a permanent obsession"*
**[E3-49]**). Of the **four causes of extreme success [E4-36]**, this record is not wave-riding:
the wave (the 2021-22 remodel boom) has been over since FY2023 and the margin did not go with it.
**No key-person dependence recorded as a moat defect [E4-23]:** the door business ran through the
2017-2026 reorganisations and three CEO-level strategic reversals without the margin moving.

### The primary moat metric, filing-sourced, and its trend — THE TWO-CHARACTERISTIC TEST **[E2-44]**
*"can it raise prices even when product demand is flat and capacity is not fully utilized, and grow
dollar volume with only minor additional investment of capital?"* — both halves, from the filed
MD&As, FY2020 to FY2025 (HBP as separately reported; revenue for FY2020-22 from the FY2022 10-K
segment note, FY2023-25 from the FY2025 10-K segment note):

| FY | HBP revenue | price & mix, as filed | volume, as filed | HBP segment adj. EBITDA | margin |
|---|---|---|---|---|---|
| 2020 | $927,313 | — | +4% | $153,631 | 16.6% |
| 2021 | $1,041,108 | **+8%** | +4% | $181,015 | 17.4% |
| 2022 | $1,506,882 | **+47%** | **−2%** | $412,738 | 27.4% |
| 2023 | $1,588,505 | **+8%** | **−3%** | $510,876 | **32.2%** |
| 2024 | $1,588,625 | (resi volume up, commercial down) | — | $501,001 | 31.5% |
| 2025 | $1,584,182 | **+2%** | **−2%** | $494,576 | 31.2% |

**Half one: passed, and not marginally.** In FY2022 Clopay took **47% of price with volume down
2%** — the literal wording of [E2-44]. In FY2023 it took **8% more while volume fell another 3%**,
and the FY2023 10-K says adjusted EBITDA *"benefited from the increased revenue noted above and
reduced material costs"* — **the steel cost came out and the price stayed in.** That is the part of
the test a cost pass-through cannot fake, and it is the reason this is not shape 11, the
pass-through. The margin has now held between **31.2% and 32.2% for three consecutive years**, and
the current quarter is still taking price: the Q3 FY2026 release (2026-08-05) reports revenue
*"a 7% increase … due to favorable price and mix of 6% … and increased volume of 1%."*
**On [E4-37]'s inverse metric there is no sign of agony** — no filing describes a price increase as
contested, delayed or withdrawn; the FY2021 10-K records the opposite problem, *"the lag in
realization of price increases"*, which is a timing complaint, not a pricing-power complaint.

**Half two: passed.** Dollar revenue rose **70.8%** from FY2020 to FY2025 on capex of 1.7-2.8% of
revenue and no acquisition in the segment since CornellCookson in 2018.

**And the honest counter-reading, which the corpus requires me to state at full strength
[E4-51, E4-55]:** *"you can almost measure the strength of a business over time by the agony they go
through"* has a twin — **[E4-55]**, where units fell 69M to 46M pounds while price rises held dollar
revenue level, and Buffett called it *"a serious reverse, not likely to disappear in some 'bounce
back' effect."* **Griffon's physical volume is flat-to-down across all six years** (+4, +4, −2, −3,
mixed, −2) while dollar revenue rose 71%. **Griffon discloses no unit series anywhere** — not doors
shipped, not square feet, not dealers gained or lost — so I cannot separate a cyclical remodel bust
from share loss from the filings. That is a judgment, not a work order: **no document exists on this
project's shelf that would resolve it**, because the company does not publish units and no
competitor publishes a market-share series (see the row's limits). The judgment I make is that the
volume weakness is cyclical, on three filed grounds: commercial revenue held ($700.1M FY2023 →
$676.6M FY2025 → running $536.7M in nine months of FY2026, up 3.2%), the FY2024 outlook cites
*"residential and commercial market share gains"*, and **the nearest listed competitor's volume fell
harder over the same window** (below). It is a judgment and it is written down.

### The second question about the business, and it is a number **[E3-46, E2-43]**
Return on **unleveraged net tangible assets** — the denominator the corpus prescribes for an
acquisitive, leveraged filer (*"the best guide to the economic attractiveness of the operation"*
**[E2-43]**), with the goodwill wedge reported separately and never hidden in book equity:

- **At 2025-09-30, continuing perimeter** (recast balance sheet in the Q3 FY2026 10-Q): continuing
  assets $2,076,034 − $735,816 held for sale = **$1,340,218**; less goodwill $191,253 and
  intangibles $363,955 = tangible assets **$785,010**; less non-debt liabilities ($2,002,062 total
  − $250,390 discontinued − $1,412,309 debt) = **$339,363** → **unleveraged net tangible assets
  $445,647**.
- Continuing operating income FY2025 before the impairment = $173,866 + $243,612 = **$417,478**.
- **Return on unleveraged net tangible assets: 93.7% pre-tax** (≈67% after tax at the guided 28%).
- **At 2026-06-30**, on the same construction and excluding the two JV stakes and the two PIK notes
  from the asset base: unleveraged net tangible operating assets **$460,432** against annualised
  nine-month operating income of **$403,015** → **87.5% pre-tax**.
- **The goodwill wedge, stated separately and not netted:** goodwill $191,253 (all of it HBP, and
  none of it impaired in any of FY2022-25) plus intangibles $346,815 at 2026-06-30. **Book equity is
  $129,156 against $538,068 of goodwill and intangibles — net tangible equity is about
  −$409M.** That belongs at Q4, and it is stated here so the 93.7% is read for what it is: a return
  on the *operating* assets, not a claim about the balance sheet.

**A pre-tax return near 90% on the tangible capital the operators actually work with is the
[E3-46] answer, and it is what a franchise looks like from the inside.**

### AUDIT OF THE DRAFT ABOVE, 2026-09-19 (resuming session). Dated corrections; the draft is not edited.
*The Q2 text above was written by a session killed at ~10:38 EDT. Every figure in it was re-read
against the filed document on disk and every ledger id against `principle_ledger.csv`. What held and
what did not:*

**Figures that reproduce to the dollar:** the HBP revenue and segment adjusted EBITDA series
FY2020-FY2025 (FY2021 10-K MD&A: *"HBP Adjusted EBITDA in 2021 increased $27,384, or 18% to $181,015
compared to $153,631 in 2020"*; FY2022 revenue = FY2021 $1,041,108 + the filed increase $465,774 =
$1,506,882); the price and volume percentages for FY2021, FY2022, FY2023 and FY2025; the continuing
capex and D&A (recast FY2025 10-K cash-flow statement, `0001628280-26-054906`: capex $41,692 /
$50,279 / $31,445, D&A $38,473 / $35,949 / $35,506); the unleveraged net tangible assets at both
dates ($445,647 and $460,432); the returns (93.7% and 87.5%); commercial revenue $700,112 /
$676,626 and the nine-month +3.2% ($536,714 against $519,893); book equity $129,156 against
$538,068 of goodwill and intangibles. All five quoted passages checked verbatim in the FY2025 10-K.

**Correction 1: FY2022 is NOT "the literal wording of [E2-44]", and it is withdrawn as evidence.**
[E2-44] asks for price taken *"even when product demand is flat and capacity is not fully
utilized"*. The FY2022 10-K gives the reason volume fell, and it is the opposite condition:
*"Total volume decreased 2%, primarily due to labor and supply chain disruptions impacting
residential deliveries"*. Demand was not flat and capacity was not idle; supply was short. A 47%
price rise into a supply shortage is what [E3-43] calls the other route to exceptional profit,
*"if supply of its product or service is tight. Tightness in supply usually does not last long."*
**The test years that DO fit the wording are FY2023** (*"pricing and mix of 8%, partially offset
by a decline in volume of 3%. The volume decrease was primarily driven by residential"*, with
*"reduced material costs"*) **and FY2025** (*"favorable price and mix of 2%, offset by decreased
volume of 2% primarily driven by residential volume"*). Half one of [E2-44] still passes on those
two years; it passes more narrowly than the draft said.

**Correction 2: the draft's maintenance-scale capex reading was flattered by amortisation.** It set
continuing capex ($31.4M / $50.3M / $41.7M) against continuing D&A ($35.5M / $35.9M / $38.5M). That
D&A includes amortisation of acquired intangibles, mostly Hunter's: the Q3 FY2026 release guides
*"depreciation of $27 million and amortization of $15 million"* against *"capital expenditures of
$50 million"*. **For the door business alone the filed segment note gives HBP capex $24,065 /
$41,765 / $30,200 against HBP D&A $15,066 / $15,349 / $17,592 (FY2023-FY2025), so doors spend 1.6x
to 2.7x their depreciation.** FY2023 includes *"approximately $6,000 in connection with the
purchase of HBP's Mason headquarters"*. The [E4-04] conclusion (defended, not rebuilt) survives,
because capex is still 1.5-2.6% of HBP revenue and segment assets barely moved (below). **The (c)
consequence is carried to Q4: the D&A default [E3-44] must be read on depreciation, not on D&A.**

**Correction 3: "the door business ran through ... three CEO-level strategic reversals without the
margin moving" is withdrawn.** No filing on disk counts three reversals, so the phrase is unsourced
(PRIME RULE 3), and the margin DID move: HBP segment adjusted EBITDA margin went 16.6% (FY2020) to
32.2% (FY2023). The [E4-23] finding that survives is narrower and sourced: the three parts of the
scarce input named at Q1 (57 depots, the Home Depot and Menards exclusive, 3,000 dealers) are
structures, not a person, and no filing ties Clopay's results to a named executive.

**Correction 4: the [E4-36] sentence needs its counter-reading.** The draft says the record is
not wave-riding because the margin outlived the 2021-22 wave. True as far as it goes; but **the
LEVEL of the margin was set during the wave, industry-wide**: Sanwa's Overhead Door (ODC) went from
a 6.0% segment margin (year to 2022-03) to 13.3% (year to 2023-03), and Sanwa's own words are
*"Sales increased substantially as the increase in raw material and other costs was passed through
to selling prices."* So part of today's level is an industry regime after an inflation reset, and
not Clopay's alone. **What is Clopay's alone is the gap to the next competitor, and the row below
shows the gap predates the wave.**

**Correction 5: "Hunter Fan (~12%, derived below)" was never derived. Derived now:** continuing
revenue (recast / pro forma) less the filed HBP revenue gives Hunter **$282,723 (FY2023), $267,360
(FY2024), $211,202 (FY2025), 15.1% / 14.4% / 11.8%**, down 25% in two years. Hunter's segment
EBITDA is not filed on the new basis; **by subtraction** (continuing adjusted EBITDA $461,820 less
HBP $494,576 plus the FY2025 unallocated corporate $57,828) it is roughly **$25,000, about 5% of
segment EBITDA**, labelled a derivation because the recast's unallocated line may not equal the old
one.

**Correction 6, a small one:** the "FY2024 outlook" citing *"residential and commercial market share
gains"* is in the **FY2023 Q4 earnings release (EX-99.1, November 2023)**, not a 10-K; it is
management's forecast, not a filed outcome, and it is weighted as such.

**Ledger ids cited in the draft, checked:** [E3-03], [E4-04], [E5-23], [E3-49], [E4-36], [E4-23],
[E2-44], [E4-37], [E4-51], [E4-55], [E3-46], [E2-43] each say what they are cited for. [E4-55] is
cited correctly as the twin of [E4-37] in the framework's own text. No phantom id.

### THE DOOR SERIES REBUILT ON AN OPERATING LINE, FY2020-FY2025
*Segment adjusted EBITDA is the company's CODM measure; the row needs an operating line, so HBP
D&A (filed, segment note) is taken off. Unallocated corporate cost is NOT allocated, which flatters
Clopay against a peer that carries its own overhead; the size of that flattery is stated below.*

| FY | HBP revenue | adj. EBITDA | HBP D&A | segment operating income | margin | HBP capex | HBP segment assets (year end) | pre-tax return on segment assets |
|---|---|---|---|---|---|---|---|---|
| 2020 | $927,313 | $153,631 | $18,361 | $135,270 | 14.6% | $17,499 | n/a | n/a |
| 2021 | $1,041,108 | $181,015 | $17,370 | $163,645 | 15.7% | $8,648 | $666,422 | 24.6% |
| 2022 | $1,506,882 | $412,738 | $16,539 | $396,199 | 26.3% | $11,029 | $737,860 | 53.7% |
| 2023 | $1,588,505 | $510,876 | $15,066 | $495,810 | 31.2% | $24,065 | $703,661 | 70.5% |
| 2024 | $1,588,625 | $501,001 | $15,349 | $485,652 | 30.6% | $41,765 | $737,992 | 65.8% |
| 2025 | $1,584,182 | $494,576 | $17,592 | $476,984 | 30.1% | $30,200 | $770,072 | 61.9% |

Sources: FY2022 10-K (`0000050725-22-000090`) segment note for FY2020-22 D&A, capex and assets;
FY2023 10-K (`0000050725-23-000055`) and FY2024 10-K (`0000050725-24-000152`) for FY2023 assets;
FY2025 10-K (`0001628280-25-053242`) segment note for FY2023-25. Segment assets include the $191,253
of goodwill, so the return column is struck on a denominator the corpus would call too large
[E2-43], which is conservative. **If ALL of the FY2025 unallocated corporate cost ($57,828) is
charged to doors, the FY2025 margin is 26.5%.** That is the floor of the flattery.

**[E2-44] half two, on the segment's own assets: revenue +52% from FY2021 to FY2025 on segment
assets +16% ($666,422 to $770,072), and capex never above 2.6% of revenue.** That is *"large
dollar volume increases ... with only minor additional investment of capital"*, and the dollar
growth came from price (volume is flat to down in every year), which is the case the passage
itself names: *"often produced more by inflation than by real growth"*.

### THE COMPETITOR ROW, required **[E3-28]**
**Metric: segment operating income ÷ segment revenue, and segment operating income ÷ segment
assets, each filer's own three latest fiscal years, from the filer's own document.** Windows do
not align (Griffon Sept, Sanwa March, ASSA and Janus December/January) and are stated per row;
forcing calendar alignment would be my arithmetic, not theirs.

| Company | window | segment op. margin, 3 yrs | Δ over window | segment income ÷ segment assets | price vs volume, as filed | source |
|---|---|---|---|---|---|---|
| **Clopay (GFF HBP)** | FY Sep 2023 → Sep 2025 | **31.2% / 30.6% / 30.1%** | **−1.1 pts** | **70.5% / 65.8% / 61.9%** | price +8 / 0 / +2; volume −3 / flat / −2; Q3 FY2026 price +6, volume +1 | FY2025 10-K `0001628280-25-053242`, segment note |
| **Overhead Door (Sanwa, North America segment)**: the #2, same products, same size | FYE Mar 2024 → Mar 2026 | **15.7% / 16.9% / 15.6%** | −0.1 pts | **20.8% / 20.5% / 17.5%** | *"Efforts to stem the decline in selling prices"* (FYE 3/2024); *"struggling to secure volume in the door business"* (FYE 3/2026); residential USD sales **−5.0%** (FYE 3/2026) | Sanwa tanshin segment tables, FYE 3/2024-3/2026, IR distribution PDFs (URLs in `peers/FOREIGN_sanwa_assa.md`); IR rung, not SEC |
| ASSA ABLOY Entrance Systems (owns Amarr): a whole division, residential 20% of it | CY2023 → CY2025 | 16.4% / 17.2% / 16.9% (reported EBIT) | +0.5 pts | not filed by division (ES ROCE 19.0%, Q2 2026, a different line) | residential *"declined"* 2023 and 2024, *"stable"* 2025; no price disclosure | ASSA year-end reports 2023-2025; IR rung, not SEC |
| Janus International (JBI): rolling steel doors, competes with CornellCookson | FY Dec 2023 → Jan 2026 | 23.0% / 15.2% / 12.6% (consolidated operating income; no segment income filed) | **−10.4 pts** | 8.5% on total assets (FY2025 only on disk) | *"75% attributed to the overall decline in volume with the residual 25% decline being attributed to price"*; *"a decline in sales price"* | JBI 10-K FY2025 `0001839839-26-000006`, FY2024 `0001839839-25-000032` |
| C.H.I. Overhead Doors (Nucor) | n/a | **not filed** | n/a | not filed | n/a | Nucor FY2022 10-K: *"Pro-forma results of operations ... would not be materially different ... therefore, this information is not presented."* |
| Amarr (inside ASSA ABLOY) | n/a | **not filed** | n/a | not filed | n/a | Amarr named in none of six ASSA reports read |

**Adjusted-EBITDA cross-check, the one metric both Griffon and Janus publish:** Clopay 32.2% /
31.5% / 31.2%; Janus 26.8% / 21.6% / 19.0%.

**Before the wave, the gap already existed:** Clopay FY2021 segment operating margin **15.7%**
against ODC (year to 2022-03) **6.0%**; after it, **30.1%** against **15.6%**. The ratio went from
2.6x to 1.9x; the gap in points widened from 9.7 to 14.5. **Clopay was first on the metric
before the regime changed and is first after it.**

**Peers named: 4 rowed with numbers (Clopay, ODC, ASSA Entrance Systems, Janus) of the six real
competitors the filings and the peer research name in North American garage and rolling doors;
two (CHI, Amarr) exist only inside unsegmented parents, and the private tail (the peer file names
none I could verify on a primary document) is not rowed.** Buffett says eight; the industry's
reportable set is smaller than that.

**The separating test on the two empty rows: "Can I name the document that would resolve this?"
No.** Nucor states in its own 10-K that it does not present CHI's results, and ASSA ABLOY does not
name Amarr in any report read. There is no filing to fetch, so this is not a work order. Under the
ARM precedent in this queue (*"The substitute cannot be rowed ... class capped, not suspended"*),
**the gap caps the class; it does not suspend the gate.** The row that can be built contains the
competitor that matters most: ODC is the one peer of the same size (USD 1,615M against Clopay's
USD 1,584M), in the same products, through the same two channels, and Sanwa itself ranks ODC
*"North America No. 2"* for garage doors (Integrated Report 2025; a layout read, flagged in the
peer file).

**What the row shows, in one sentence: on the same line, over overlapping windows, the largest
North American door maker earns about twice the margin and about three times the return on
segment assets of the second, held its price when ODC and Janus were losing theirs, and lost less
volume.** On direction [E4-32], Clopay is flat to slightly narrowing (−1.1 pts in two years,
segment EBITDA down in FY2024 and FY2025, the nine-month FY2026 continuing margin lower on
*"increased material and selling, general and administrative costs"*); ODC is flat; Janus is
collapsing. **The relative position is widening against Janus and steady against ODC; the absolute
level is not widening.**

**[E3-61], the row's stated limit:** the row shows position, not conduct. Three large door makers
all took price in 2022 and none has given it back in full; whether that is a franchise's pricing
or an oligopoly's manners, *"I think you'd have to know the people involved."* The honest
statement is that part of the level is the industry's, and the row cannot say how much.

### THE REMAINING Q2 TESTS, run rather than recited
- **The attacker's test [E2-45]:** *"how I would like, assuming I had ample capital and skilled
  personnel, to compete with it."* The filed record contains the answer from an attacker that had
  both. **Nucor, with ample capital, did not build a door business; it bought CHI for "approximately
  $3.00 billion", of which PP&E was $117,392 thousand and goodwill plus intangibles $3,426,353
  thousand** (FY2022 10-K, Note 25), then added Rytec for ~$565 million in 2024. Plant was
  3.7% of the $3,195,937 thousand of net assets acquired; the rest was paid for a position. A well-funded attacker paid for an
  incumbent's position rather than attempt to build one, which is the attacker's test answered by
  conduct. (Nucor's FY2025 10-K also says *"the performance of certain businesses that comprise our
  reporting units requires continued improvement"*, with a critical audit matter on an unnamed
  steel-products reporting unit; whether that is CHI is not filed, and it is not used.)
- **Untapped pricing power [E3-33, E5-28]:** **not claimed.** [E5-28] says claiming the class is
  claiming *"a monopoly or a near monopoly"*, and a filer that names *"several large national
  manufacturers"* and competes on price does not support that.
- **The agony metric [E4-37]:** no filing describes a Clopay price increase as contested, delayed
  or withdrawn. The FY2021 *"lag in realization of price increases"* is timing. The current
  quarter's +6% price is a pass-through of material cost (the release says so), and ODC says the
  same of its own (*"Cost increase resulting from tariff impacts in 2025 have already been
  addressed through price pass-through"*). Pass-through that sticks is not agony; it is also not
  proof of untapped power.
- **Units [E4-55]:** Griffon files no unit series, so the Precision Steel test cannot be run on
  doors directly. The filed volume percentages are flat to down in every year, and the row shows
  the peers' volume fell harder (Janus volume was 75% of an 8.3% decline; ODC residential USD sales
  −5.0%). **Judgment, written down: cyclical, not share loss**, on the row, not on management's
  word. No document would settle it more finely, because no filer publishes door units.
- **The dominance class [E2-53]:** not claimed. Clopay's economics are position plus execution;
  the ODC comparison is the evidence that execution matters (same industry, same regime, half the
  margin).
- **Which cause of extreme success [E4-36]:** the nearest is *"an extreme of good performance over
  many factors"* (depot density, retail exclusivity, dealer software, commercial breadth). Not one
  ownable variable, which is why the class is not WIDE.
- **Key-person dependence [E4-23]:** none found (Correction 3 above).
- **Commodity end [E2-58]:** differentiation here IS meaningful to the installer (lead time,
  availability) and the gap to peers is wide and has lasted through a regime change, which is the
  exception the passage allows (*"a cost advantage that is both wide and sustainable"*). Whether
  the gap is a cost advantage or a price advantage the filings do not say; either way it is the
  relative position [E3-03] asks the returns to demonstrate.

### HUNTER FAN, the other ~12%: class NONE, and why it does not decide the gate
Criterion 2 of **[E3-03]** fails on the filing's own words (*"retailer house brands such as Hampton
Bay in The Home Depot and Harbor Breeze in Lowe's"*): the customer is the substitute. Revenue
fell 25% in two years (Correction 5), and the reporting unit took **$80,000 of impairment in FY2023
and $243,612 in FY2025** (recast cash-flow statement; the FY2025 charge *"driven by a decrease in
year-to-date and forecasted sales and operating results primarily due to ongoing weak consumer
demand coupled with the impact of increased tariffs"*). **It is roughly 12% of revenue and roughly
5% of segment EBITDA.** Unlike DIS and IBM today, where the franchise was the minority of the
capital, here the franchise is the large majority of the profit and of the operating capital
[E2-73]; Hunter's book carrying value is mostly purchase price. Hunter is a capital-allocation
record (Q3), not the business the share mostly buys.

- **Untapped pricing power [E3-33]:** not claimed (above).
- **Class: [x] NARROW** for the company, set by Clopay; the class is **capped** by the two
  unrowable competitors and by criterion 2 being met only partly (the substitute exists at the
  dealer; the retail exclusive is the retailer's to grant). Hunter Fan: NONE.
  **Direction: absolute level flat to slightly narrowing; relative position steady against ODC
  and widening against Janus [E4-32].**
- **VERDICT: [x] IN**

**Why IN, stated against the strongest case for OUT [E4-51].** The case for OUT: the filer says it
competes on price; three competitors exist; the retail exclusive can be withdrawn by Home Depot; the
level of profit was set during an inflation wave the whole industry rode; the margin and the
segment EBITDA have edged down three years running; and the fan business beside it is a write-off.
Every one of those is true and recorded. **Against it, the evidence the corpus names as the
demonstration of a franchise is present in the filings:** *"The existence of all three conditions
will be demonstrated by a company's ability to regularly price its product or service aggressively
and thereby to earn high rates of return on capital"* **[E3-03]**. Clopay took price in five of the
last six years, including two years of falling residential demand; it earns 62-70% pre-tax on
segment assets that include goodwill; and it is first on the metric against the one peer of its
size, by about twice the margin, before the wave and after it. **This is the NARROW class, the same
class ORLY, BMI and CTAS were admitted in, and it is written as narrow.** No narrowing assumption
was needed to reach it [E4-18]: the row is filed, the corrections above all cut against the draft,
and the verdict holds on the years that fit [E2-44]'s wording without the one that does not.

**What IN does not carry forward:** the absolute level of the margin. Whether the post-2022 level
is the business or the regime is a Q4 and Q5 question (the window, [E4-41]'s normalisation), and
it is carried there, not settled here.

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?
*Full standard: `Framework/v4/THE MANAGER STANDARD - Q3.md`. Standing rule followed: the latest 8-K
EX-99.1 releases were read before scoring [E4-29] and [E4-22]'s third flag (Q3 FY2026,
`0001628280-26-052927`; Q2 FY2026, `0001628280-26-031705`; Q1 FY2026, 8-K `0001628280-26-005611`;
FY2025 Q4, 8-K `0000050725-25-000079`; and the FY2023 Q4, FY2024 Q4 and FY2025 Q3 releases on disk),
with the 2026 and 2025 proxies (`0000930413-26-000074`, `0000930413-25-000212`).*

**STEP 1 — DECLARE THE WEIGHT CASE.**
- **[x] Daily execution [E3-38]**: ticked, on a filed fact and not on a view of these managers.
  Q2 found the class NARROW, and the evidence that capped it is the row: **Overhead Door works the
  same product, the same two channels and the same inflation regime at half Clopay's margin**, and
  Janus lost 10.4 points of margin in two years. Where an equivalent competitor earns half as much,
  execution is doing part of the work, which is [E3-43]'s *"a business, unlike a franchise, can be
  killed by poor management"* in its milder form. The differentiation Q1 named (a door in the depot
  this week) is delivered every day through 57 buildings.
- [ ] **Control [E1-16]**: not ticked; a marketable security, exit at will.
- [ ] **Leverage [E3-29]**: not ticked, and quantified rather than screened. Book equity of
  **$129,156** against debt of **$1,267,635** (2026-06-30) looks like 10:1, but it is a buyback
  artifact: treasury stock at cost is **$1,147,112**. The filer's own covenant computation is
  **2.2x net debt to EBITDA** (Q3 FY2026 release), and the [E3-29] condition is errors in *assets*
  destroying equity at 20:1 gearing, which is not an operating company's balance sheet. The ORLY
  precedent (negative book equity from buybacks, not ticked) is followed.

**CASE DECLARED: Q3 IS A BINARY GATE on daily execution, and no price compensates.**

### Honesty — binary, permanent, filings-based **[E5-16]**, each matter dated to when it became public
- **No disqualifying matter found.** FY2025 10-K Item 3 refers to *"litigation, investigations and
  claims arising out of the normal conduct of business"* and to Note 16. Note 16 carries two
  environmental matters: the Peekskill Site (Lightron and ISCP, no operations *"in over three
  decades"*, added to the National Priorities List on 2019-05-15, *"Griffon does not acknowledge any
  responsibility to perform any investigation or remediation"*, defended by an insurer under a
  reservation of rights) and a Hunter site the EPA may list. Both are legacy environmental
  exposure, disclosed in the footnotes; neither is conduct.
- **No restatement, no clawback.** Both FY2025 10-K cover checkboxes (error correction; incentive
  recovery analysis) are **unchecked**. Auditor Grant Thornton; its one critical audit matter is the
  **Hunter Fan trademark interim impairment test**, which is the right matter to be critical.
- **A Q3 pass is the absence of found disqualifiers [E5-17]**, and it is written that way.

### STEP 2 — THE FLAGS. Each is a prompt to read, never a verdict **[E5-36]**
- **[x] EBITDA / adjusted-earnings promotion [E4-29]: FIRES, and it is PAID ON.** Every release
  headlines *"Adjusted EBITDA"*; the old CODM segment measure was segment adjusted EBITDA; leverage
  is stated as *"net debt to EBITDA"*. **The 2026 proxy sets the fiscal 2025 short-term cash plan at
  "EBITDA (80%)" and "Working Capital (20%)"**, so four fifths of the annual bonus is earned on the
  line [E4-29] calls *"a particularly pernicious practice."* The long-term cash plan (Core EPS 75%,
  free cash flow 25%) and the equity awards (ROIC 60%, relative TSR 40%) are better lines. One
  presentation choice went the right way: the February 2026 outlook headlined *"Adjusted EBITDA to
  be $520 million, excluding unallocated costs of $62 million"*; the May release restated the same
  guidance as *"Adjusted EBITDA, presented to reflect Griffon's new reporting structure, is expected
  to be $458 million"*, corporate cost inside it. That switch is toward candor [E2-69].
- **[x] Trumpeted projections [E4-22, third flag]: FIRES; the [E3-48] record is decent.** Griffon
  guides revenue, adjusted EBITDA, capex, D&A, interest and tax every November and updates it every
  quarter. Guidance against outturn, from the releases on disk:

  | guided in | for | guidance | outturn |
  |---|---|---|---|
  | Nov 2023 | FY2024 | revenue $2.6bn; adj. EBITDA $525M ex-unallocated; HBP revenue −3% to −5%; HBP margin *"in excess of 30%"* | revenue $2,623.5M; segment adj. EBITDA $573.6M; HBP revenue flat; HBP 31.5%: **beaten** |
  | Nov 2024 | FY2025 | revenue $2.6bn; adj. EBITDA $575M-$600M ex-unallocated; CPP margin *"in excess of 9%"* | revenue guidance cut in Aug 2025 to $2.5bn, outturn $2,519.9M; segment adj. EBITDA $580.1M (inside the range, low half); CPP 9.1%: **met; revenue missed on the fans and tools side** |
  | Nov 2025, then Feb 2026 | FY2026 | $2.5bn and $580M-$600M, then after the disposals $1.8bn and $458M | not yet filed (year ends 2026-09-30) |

  The door business's guidance was met or beaten every time; the misses were in the business Griffon
  has now mostly sold. **[E5-30] still applies**: a guidance culture is a ratchet, and it is live.
- **[x] The except-for flag [E2-57]: FIRES, in the proxy.** The 2026 proxy: *"the Company had an
  outstanding year in fiscal 2025, achieving all-time highs in EPS and adjusted EBITDA; and had
  outstanding years in fiscal 2024, 2023, 2022 and 2021 as well."* FY2025 is the year Griffon wrote
  off **$243,612** of the Hunter purchase and reported net income of **$51,110** against $209,897
  the year before; FY2022, one of the "outstanding years", carries a filed **net loss of $191,558**
  (FY2022 10-K income statement). *"you must count the runs scored against you in all nine
  innings"*: this passage, in the document that sets the executives' pay, does not.
- **[x] Stock-price targeting [E3-50]: FIRED HISTORICALLY, since replaced.** The 2026 proxy: *"For
  the years 2016 through 2021, the Committee selected stock price growth as the performance measure
  for the equity grants awarded to the CEO and COO. Vesting of these grants required that the
  Company's stock close at a price at least 20% above the price on the date of grant for thirty
  consecutive trading days"*. From FY2022 the grants moved to ROIC and relative TSR. Public in every
  proxy for those years; replaced from the FY2022 grants.
- **[x] Weak accounting: one small cockroach, stated as a prompt [E4-22].** The recast FY2025
  annual report (8-K `0001628280-26-054906`, MD&A results table) prints adjusted EBITDA margins of
  **25.7% / 23.8% / 23.6%** for FY2025 / FY2024 / FY2023 beside dollar figures of $461,820 /
  $482,292 / $505,364 on revenue of $1,795,384 / $1,855,985 / $1,871,228. **The dollars give
  25.7% / 26.0% / 27.0%.** Two of three printed margins do not reconcile to the printed dollars, in
  a document recast specifically to show the new perimeter, and the misprint reverses the trend
  (the true series falls 1.3 points; the printed one rises 2.1). I do not know the cause and do not
  guess it. It is a prompt, not a finding of intent [E5-38].
- [ ] Unintelligible footnotes: not found. The disposal notes, the pro forma and the PIK terms are
  plain.
- [ ] Serial share issuance [E5-15]: not fired. One public offering in 2020 (*"total net proceeds
  of $163,830"* at $21.50 a share, plus a 700,000-share overallotment); the count otherwise fell.
- [ ] Dividends funded by issuance [E2-52]: not fired.
- [ ] Filed-figure tells [E4-30]: not fired. Cash taxes paid $70,937 / $102,978 / $96,244
  (FY2023-25, recast cash-flow statement) against continuing pre-tax income before impairments of
  $347,325 / $332,093 / $326,856: **20.4% / 31.0% / 29.4%**, rising, not falling (cash taxes include
  discontinued operations, which is noise in both directions). Reported growth is not smooth.
- [ ] Restructuring charge [E3-53]: the $92,468 (FY2023) and $41,309 (FY2024) charges and three
  years of *"strategic review - retention and other"* costs were excluded from adjusted figures, but
  they sat in AMES and the review; on the recast they are outside continuing operations except the
  retention line ($15,929 / $9,117 / $2,568), which is **kept inside the owner-earnings mean [E5-33]**
  because the recast cash-flow statement already carries it.

### STEP 3 — THE PRIMARY TEST **[E2-01]**, read segment by segment **[E2-56]**
Return on equity is not usable: book equity fell from $807.2M (FY2021) to $74.0M (FY2025) because
**$664.1M of stock was bought back from April 2023 to June 2026** (Q3 FY2026 release) and two $2
special dividends were paid (declared 2022-06-27 and 2023-04-19), not because the business shrank.
The corpus's substitute for a leveraged, acquisitive filer is **unleveraged net tangible assets
[E2-43]**, and [E2-56] requires it **segment by segment**, because *"Their marvelous core businesses
... camouflage repeated failures in capital allocation elsewhere"*:

| FY | HBP segment op. income ÷ HBP segment assets | CPP segment adj. EBITDA ÷ CPP segment assets (before D&A, so flattering to CPP) | CPP segment assets |
|---|---|---|---|
| 2022 | 53.7% | not computed | $1,914,529 |
| 2023 | 70.5% | **3.2%** ($50,343) | $1,579,588 |
| 2024 | 65.8% | **4.9%** ($72,632) | $1,495,489 |
| 2025 | 61.9% | **7.3%** ($85,545) | $1,164,957 |

**This is the Pro-Am effect in its textbook form.** The door business earned 62-70% pre-tax on its
segment assets while the other half of the company, **$1.2-1.9bn of assets**, earned 3-7% before
depreciation. The consolidated figure blended them and the proxy called every year outstanding.
The continuing company earns **87.5-93.7% pre-tax on unleveraged net tangible operating assets**
(Q2): for the first time in the window, Griffon's consolidated return is mostly the franchise's.

### Capital allocation — the record, the institutional imperative, and the buybacks
**The record, from the filings:**
- **Hunter Fan**, bought 2022-01-24 *"for a contractual purchase price of $845,000"*, financed with
  *"a new $800,000 seven-year Term Loan B facility"* (FY2022 10-K). Impaired **$80,000 (FY2023) and
  $243,612 (FY2025)**, 38% of the price inside four years; revenue down 25% in two years. The Term
  Loan B that bought it was repaid in full on 2026-07-31 with AMES proceeds.
- **AMES**, the tools and outdoor business built by a decade of bolt-ons (Hills 2016, La Hacienda
  2017, Tuscan Path 2017, Kelkay 2018, Apta 2019, per the FY2021 10-K). AMES North America,
  carrying value **$391,312**, went to a 43%-owned JV for **$379,700 of consideration of which
  $100,000 was cash**, at a **$25,885 loss**; AMES U.K. was closed (**$25,913** of charges); AMES
  Australasia was sold at a gain of about **$118,559** (pro forma note 2). A decade of capital
  returned largely as paper: PIK notes and minority stakes.
- **The good decisions are on the record too**: CornellCookson (2018, *"approximately $170,000"*)
  inside the door business; the Telephonics sale (2022, $330,000); the specialty plastics sale to
  Berry (2018, *"approximately $465,000"*); and the 2026 disposals, which end the Pro-Am.
- **The 2022-23 strategic review** (announced 2022-05-16, concluded 2023-04-20 with no transaction)
  cost **$20,225 / $10,594 / $3,883** of *"strategic review - retention and other"* (FY2023-25
  segment note) and **$2,685** of *"proxy expenses"* (FY2023).

**The institutional imperative [E2-30], scored:**
- [x] **projects or acquisitions materialise to soak up available funds**: Hunter, January 2022,
  debt-funded at the peak of the consumer-durables boom, while the door business was producing the
  best cash in its history. This is [E3-40]'s named vector: *"gets sidetracked and neglects its
  wonderful base business while purchasing other businesses that are so-so or worse"*.
- [ ] resists any change in current direction: **not ticked**; a management that sells most of the
  Pro-Am leg has changed direction, and the 2026 filings are the evidence.
- [ ] staff studies to justify the leader's craving: not evidenced in any filing.
- [ ] peer behaviour mindlessly imitated: not evidenced.

**Delegation [E3-58]:** the 2026 transactions ran through Goldman Sachs and Houlihan Lokey (8-K
2026-08-04). Banker-led disposal of a failed leg is ordinary; recorded, not fired.

**Buybacks, the two conditions [E5-08] and the third [E4-31]:**
- (1) **Ample funds?** Yes on the filed record: buybacks of $164.0M / $309.9M / $183.3M (FY2023-25)
  and $119.1M in nine months of FY2026 were paid while long-term debt fell from $1,561.0M (FY2022)
  to $1,259.6M (2026-06-30) and covenant leverage fell to 2.2x. Not borrowed to buy.
- (2) **At a material discount to intrinsic value, conservatively calculated?** The average price
  paid from April 2023 to June 2026 was **$54.86**, and **$85.00** in the latest quarter. Tested
  against the Q4 range, not assumed here (see the addendum to this section after Q5).
- (3) **[E4-31], owners supplied the information to estimate value?** Largely yes on the continuing
  perimeter: the recast, the pro forma, the PIK terms and the JV carrying values are all filed. The
  gap: the JVs are on a three-month lag and their own accounts are not filed.
- **The one issuance was at the wrong end [E5-24]:** about 8.7M shares sold in August 2020 at
  **$21.50**; 12.1M bought back from 2023 at an average **$54.86**. *"what is smart at one price is
  dumb at another."* The humility clause applies with force: the price rose because the business
  did, and 2020 was a pandemic balance-sheet decision [E4-13]. Recorded, not scored as misconduct.

**CAPITAL-ALLOCATION FLAG: LIVE.** A textbook [E2-56] Pro-Am, a debt-funded acquisition written
down by 38% inside four years, and a proxy that calls each of those years outstanding. It **binds
position size, never the discount rate**, and it is carried to Q6 as a named trigger: **any new
acquisition outside doors reopens this file at Q3.** The humility clause **[E4-13]**: *"They also
know a whole lot more about them than I do."*

### Candor **[E2-26]**
Mixed, and both halves are filed. For: the Hunter impairment is quantified at every line and is the
auditor's critical audit matter; the disposals come with a pro forma, carrying values, PIK terms and
costs to sell; the May 2026 guidance moved corporate cost into the headline. Against: the proxy's
"outstanding year" passage [E2-57], the EBITDA-first release architecture [E4-29], and the recast
margin misprints. **The half-owner test is passed by the financial statements and failed by the
proxy prose.**

### Converging flags **[E4-52]**
EBITDA promotion, bonus paid on EBITDA, annual projections and except-for prose converge on one
outcome: a headline that reads better than the GAAP record. They are read as one reinforcing system.
**What they do not converge on is a disqualifier**: no restatement, no misconduct, no issuance to
pay dividends, cash taxes rising with profit, and guidance on the franchise met or beaten.

### THE GUARDRAIL — checked before the verdict
- [x] Nothing in this Q3 is used to promote the name **[E2-37, E2-38, E3-39]**. The 2026 refocus is
  recorded as evidence the institutional imperative is not frozen, not as a reason to buy.
- [x] Key-person dependence recorded at Q2 as absent **[E4-23]**.
- [x] Is a great manager the reason to act? **No.** The franchise is intact and the damage (CPP) was
  the excisable kind **[E2-36]**; the sellers have mostly excised it themselves.

- **VERDICT: [x] IN** (Q3 is a gate on daily execution; no disqualifier found). One live
  **capital-allocation flag** (binds position size) and live [E4-29], [E4-22]-third and [E2-57]
  flags, each quantified above. *IN = no disqualifier found, not a finding that the managers are
  honest [E5-17]. IN never promotes.*

## Q4 — WILL IT SURVIVE?
*Arithmetic in `Test Runs/_research 2026-09-19 GFF/q45.py`, output `q45_out.txt`. Inputs
hand-transcribed from the recast continuing cash-flow statement (8-K `0001628280-26-054906`) and the
Q3 FY2026 10-Q (`0001628280-26-053536`). $ thousands unless stated.*

### Owner earnings — the one number **[E2-23]**

**THE WINDOW, and why the five-year default cannot be run on this perimeter [E2-42].** The share
buys the continuing perimeter (Step 0's perimeter note and addendum). Griffon has filed that
perimeter's cash-flow statement for **three fiscal years only** (FY2023-25, in the August 2026
recast) plus the nine-month 10-Q. A five-year window exists only on the consolidated perimeter,
which included AMES, and that is a company the share no longer buys. **So the windows here are the
three-year filed mean and the trailing twelve months, and the missing five-year window is stated,
not manufactured.**

**A tooling finding, recorded for the operator:** `python tools/run.py GFF` printed owner earnings
of **297-318 (three-year) and 170-190 (five-year)**, a yield of 7.04-7.54%. **Both windows are the
pre-disposal consolidated perimeter**: its FY2025 operating cash of 357 is the original 10-K's
consolidated $357,440 (Step 0 cross-check 2), not the recast continuing $307,794. The recast was
filed on an **8-K**, and the tool's `annual()` reads 10-K and 20-F facts, so any filer that recasts a
disposal through an 8-K is read by the tool on the perimeter it has sold. **Here that overstates the
three-year owner earnings by roughly $50M a year and the yield by about a point.** Not fixed in
this run (tools may not conclude, and a fix is the operator's to approve); the numbers below are
hand-built from the recast.

**Owner earnings by year, OCF − SBC − (c), continuing perimeter:**

| FY | OCF (continuing) | SBC | capex | depreciation | OE, capex end | OE, depreciation end | capex ÷ depreciation |
|---|---|---|---|---|---|---|---|
| 2023 | 332,826 | 39,178 | 31,445 | 20,925 | **262,203** | 272,723 | 1.50 |
| 2024 | 307,370 | 25,570 | 50,279 | 21,607 | **231,521** | 260,193 | 2.33 |
| 2025 | 307,794 | 24,191 | 41,692 | 23,892 | **241,911** | 259,711 | 1.75 |
| TTM to 2026-06-30 | 291,222 | 27,945 | 32,930 | n/a | **230,347** | n/a | n/a |

- **Three-year mean: $245,212 (capex end) to $264,209 (depreciation end).** TTM $230,347.
- **Spread, conservative end:** TTM against the three-year mean, **−6.1%**; capex band **7.7%**.
  **Combined range roughly $230M to $264M before the pro forma adjustment.** Narrow enough to
  conclude [E4-25].
- **Pro forma interest, a disclosed judgment:** the historical cash flow carries interest on debt
  that AMES proceeds have since repaid ($100,000 in June, $180,910 in July, at the Term Loan B rate of
  5.66%), less the extra cost of the August refinancing ($800,000 at 6.25% plus the ~$182,775
  remainder on the revolver at 5.51%, against $974,775 at 5.75%: **+$4,021 a year pre-tax**). Net,
  after the company's guided 28% tax rate: **+$8,552 on the three-year means, +$4,477 on the TTM**
  (the June money was already working inside the TTM).
- **A distorted year in the window?** FY2023 carries a working-capital release (inventories
  −$31,627) and the largest SBC ($39,178); FY2024 carries the largest capex ($50,279, *"the opening
  of new warehouses"*). Neither is large enough to widen the range materially; both are named.
- **(c): which case, and why [E3-44, E2-41, E5-20].** Not the capital-intensive exception class:
  capex is 1.7-2.8% of revenue. **But the default must be read on DEPRECIATION, not D&A** (Q2
  correction 2: D&A carries ~$15M a year of acquired-intangible amortisation, which renews nothing).
  Door capex has exceeded depreciation in every filed year (1.5x-2.3x), and the company guides
  FY2026 capex of $50 million against depreciation of $27 million. Part of that is growth
  (warehouses) and the filing does not separate it. **Judged at the capex end, the conservative end
  of the band. Windage place #1.**
- **SBC subtracted in full [E5-06]**, the cash-flow statement's own add-back, which resolves in
  every year. SBC is 7.9-11.8% of OCF, not the class where [E3-70]'s grant-value measure changes
  the answer.
- **[E3-04] look-through:** the pro forma gives the two JV stakes' share of earnings as **−$39,484 /
  −$796 / +$20,530** pre-tax (FY2023-25), a three-year mean of **about −$6,600**. Not added to
  owner earnings. **The JV stakes and PIK notes are valued as assets instead (Q5)**, because their
  earnings history is negative on average and the PIK interest is capitalised, not paid.
- **Owner earnings, judged: about $254M (three-year mean, capex end, plus pro forma interest);
  range $235M-$273M across the constructions.**

**[E4-41], normalise down for luck: the 2022 regime, named.** The one favourable exogenous break in
the record is the industry-wide repricing of 2022 (Q2 correction 4). **It is not removed from the
mean**, because it has now held for three and a half years through two years of falling residential
volume, and the competitor that rode the same wave (ODC) has also held its level. **It is
quantified instead, so the reader can see what the answer depends on:** if the door margin reverted
**half** way to its FY2021 level (30.1% to 22.9%), owner earnings fall by about **$82M** after tax
to about **$172M**; **all** the way (to 15.7%), by about **$164M** to about **$90M**. Carried into
the named death below and into Q5's reading.

### Great, good, or gruesome? **[E4-20]**
- [x] **great**, on the two things the passage measures that can be measured: the door business
  earns 62-70% pre-tax on segment assets that include goodwill, and grew dollar revenue 52% on
  segment assets up 16% (FY2021-25). **Qualified on the third:** the rate has not *"risen as the
  years pass"* since FY2023; it has edged down (70.5% → 65.8% → 61.9%). A great account paying a
  flat-to-falling rate is still the great account; it is not the rising one.
- [ ] good · [ ] gruesome. **Hunter Fan, on its own, is nearer the gruesome account**: $845,000 in,
  $323,612 written off, revenue down 25% in two years. It is 12% of revenue and does not set the
  class of the company.

### Staying power — score all three **[E5-11]**, in the worst case **[E2-55]**
- **(1) A large and reliable stream of earnings: YES, qualified.** Continuing operating cash of
  $307-333M in each filed year, through a residential downturn; owner earnings $230-262M. Qualified
  because the level dates from 2022 (above), and the business is housing-cyclical.
- **(2) Massive liquid assets: NO.** Cash **$110,350** at 2026-06-30, against debt of about $1.1bn
  after the August transactions. The $472,348 of undrawn revolver is a bank line, and [E5-39]
  counts no bank lines (*"We will never be dependent on the kindness of strangers"*). The $209,693 of
  PIK notes are subordinated and cannot be called while the JVs' senior debt is outstanding (8-K
  2026-08-04). **Fails, stated plainly.**
- **(3) No significant near-term cash requirements: YES, and this is the one that usually
  kills.** After 2026-08-18 there is **no debt maturity before the revolver in August 2031 and the
  notes in October 2034**; the 2028 notes are called (*"none of the 2028 Notes will remain
  outstanding"*); the Term Loan B is gone; current debt at 2026-06-30 was $8,011 and that was Term
  Loan B amortisation. The notes are senior unsecured with incurrence covenants, not maintenance
  covenants; the revolver has maintenance tests (*"a maximum total leverage ratio, a maximum senior
  secured leverage ratio and a minimum interest coverage ratio"*). The dividend is about $40M a year
  and buybacks are discretionary.
- **Score: 2 of 3.** The same score CL and SPGI carried through Q4 in this queue.

**Leverage, named and quantified [E4-16, E3-29]; the corpus supplies no ceiling ratio.** Debt at
2026-06-30 **$1,274,786** face; after the July and August transactions, **about $1.1bn** by my
arithmetic ($800,000 of notes plus roughly $300,000 of revolver: the TLB's $285,000 less the $180,910
of Australasia cash, plus the ~$182,775 by which the redemption exceeded the $792,000 of net note
proceeds). **This is an estimate from filed transactions, not a filed balance; the FY2026 10-K will
file it.** Covenant leverage **2.2x** at 2026-06-30 (company computation). **The coverage test
[E2-54]:** cash available for interest after capex (OCF + interest paid − capex) against interest
paid was **4.02x / 3.55x / 3.86x** (FY2023-25); on the pro forma interest bill (the company guides
$80 million for FY2026, net of PIK income) it is higher. *"comfortably met out of current cash flow
net of ample capital expenditures"*: yes. **The terms [E3-52]:** unsecured notes, eight years
out, incurrence covenants: long-dated and covenant-light, the better kind of borrowed money.

### Name the specific way THIS business dies **[E2-27, E3-24]**, modelled on exposure **[E4-40]**
**1. The oligopoly stops behaving: a price war, or the retail exclusive lost, returns the door
margin to where it was before 2022.** Mechanism: [E3-61]'s *"demented Kellogg"*: three large makers
(Clopay, ODC, Amarr) plus CHI inside Nucor, an owner with a steel mill to fill; or Home Depot
(9% of HBP revenue, and the shelf where the homeowner sees one brand) re-tenders the exclusive.
**Quantified:** full reversion of the FY2025 door margin (30.1%) to FY2021's 15.7% takes **$228,122
pre-tax** out; continuing operating income before impairments falls from **$417,478 to about
$189,356**, which still covers a ~$70-80M interest bill **about 2.4-2.7 times**. The company
survives; the owner loses most of the equity value, because the price is set on today's margin.
**Likelihood: half-way reversion is a real possibility; full reversion is a low-level possibility**,
on the evidence that the level has held for three and a half years and through ODC's and Janus's
price declines.
**2. A housing depression.** Exposure: 96% US; residential repair and remodel 53%, commercial 40%,
new construction 7% of continuing revenue. **Quantified:** revenue −25% with the lost revenue
carrying the FY2025 continuing gross margin of 47.2% takes **$211,855** out; operating income falls
to about **$205,623**, coverage near 2.6-2.9x. **Survives. A low-level possibility at that
depth.**
**3. The owner's death, not the company's: a relapse into debt-funded diversification.** The
record is the mechanism (Hunter, $845,000, debt-funded, 38% written off; AMES, a decade of
bolt-ons returned as paper). A new acquisition of that size today would be funded on the revolver
and the accordion, and would re-create the Pro-Am. **A real possibility**, and it is Q6's first
trigger.

**The bear case, stated so its holders would accept it [E4-51]:** a leveraged holding company whose
one good business earns an inflation-era margin that has already started to slip, run by a
management that spent the franchise's cash on a fan company and a tools business, is priced as if
the margin and the management's new focus are both permanent. **I accept the first half of that as
the reason Q5 must be read with the reversion case beside it, and the second half as the reason the
capital-allocation flag is live.** Neither is a way the company fails to survive.

- **VERDICT: [x] IN.** Owner earnings about **$254M** (range $235M-$273M on the filed three-year
  and TTM windows with the pro forma interest); great by return and capital need, flat in direction;
  staying power 2 of 3 (no near-term maturities to 2031, cash thin); three named deaths quantified,
  none a failure to survive.

---
**Q1-Q4 each show IN. Q5 opens.**

## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?
*Arithmetic in `q45.py` / `q45_out.txt`, the same file as Q4.*

### THE PAIR, struck by this run
- **Sovereign 5.34%**, 30-year, **US Treasury daily par yield curve, dated 09/18/2026**, re-struck
  by `python tools/sources.py` on 2026-09-19 (the issuing authority, not FRED, not inherited).
- **Price US$93.22**, 2026-09-18 close, Yahoo Finance chart via `tools/sources.py:price`,
  **aggregator, flagged** (operator rule 5). Corroborated by the issuer's own purchases: *"an
  average of $85.00 per share"* in the quarter to 2026-06-30 (Q3 FY2026 release).
- **Shares 45,294,716**, the Q3 FY2026 10-Q cover (*"The number of shares of common stock
  outstanding at July 31, 2026 was 45,294,716"*), accession **`0001628280-26-053536`**. One class,
  $0.25 par. `split_factor_after('GFF','2026-07-31')` = **1.0**. Cross-check: issued 84,746 less
  treasury 39,269 thousand = 45,477 thousand at 2026-06-30, and July buybacks explain the gap.
- **Cap = US$93.22 × 45,294,716 × 1.0 = US$4,222.4M.**
- **Non-operating assets, valued separately:** equity-method stakes $118,600 + $20,896 and PIK
  principal $161,100 + $48,593 = **$349,189 carrying**. Taken at **50% (conservative), 75%
  (default), 100% (generous)**, a disclosed judgment: subordinated paper that cannot be enforced
  while the JVs' senior debt is outstanding, and minority stakes in businesses whose three-year
  share of earnings averages about −$6,600 (Q4). **Windage place #2, justified below.**

**THE FLOOR, before the ranking [E4-28, E3-13].** *"that's the figure we quit on."*

### 1. THE YIELD (owner earnings ÷ the cap net of the non-operating assets)

| construction | owner earnings | operating cap | yield | points against 5.34% |
|---|---|---|---|---|
| conservative: TTM, capex end, JV/PIK at 50% | $234.8M | $4,047.8M | **5.80%** | +0.46 |
| **default: three-year mean, capex end, JV/PIK at 75%** | **$253.8M** | **$3,960.5M** | **6.41%** | **+1.07** |
| generous: three-year mean, depreciation end, JV/PIK at 100% | $272.8M | $3,873.2M | **7.04%** | +1.70 |
| *sensitivity, not a construction: half-way margin reversion (Q4 [E4-41])* | *~$172M* | *$3,960.5M* | *~4.3%* | *−1.0* |

**Above the long bond on every filed construction; below it on the reversion case.** This is the
Berkshire shape that CLAUDE.md names: above the bond, and the floor still decides.

### 2. WHAT THE PRICE ALREADY ASSUMES
Growth in perpetuity from year one at which owner earnings discounted at the rate equal the price
(a DCF used as an engine only; it casts no vote [E3-34]):
- to match the **bond**: **negative on every construction** (−0.44% to −1.59%). The price does not
  need growth to beat 5.34%.
- to reach the **~10% floor**: **3.97% (conservative), 3.38% (default), 2.76% (generous)**, forever.
- **What the business has actually done, on the filed record:** continuing owner earnings **$262.2M
  (FY2023) to $230.3M (TTM), about −4.6% a year**; continuing adjusted EBITDA $505,364 to $461,820
  (FY2023-25), **−4.4% a year**, with FY2026 guided at $458 million; door segment operating income
  **−1.9% a year** (FY2023-25). The only positive growth in the longer record is the door business's
  2022 repricing (HBP revenue +11.3% a year FY2020-25), which [E4-41] forbids extrapolating: it was
  a level shift, and the three years since it are flat to down. Door price ex-2022 has averaged
  about +4% a year and has not reached owner earnings, because costs rose alongside.
- **[E4-35] and [E4-44] put the burden on the believer:** a perpetual 3.4% on a business whose
  owner earnings have fallen three years running, whose units are flat, and whose last big gain was
  a one-time repricing, is a growth belief the filings do not carry. **Granted here: 0% to 3%,
  default 2.5%, a stated judgment (roughly price pass-through with flat units).**

### 3. WHAT YOU ARE PAID
**+1.07 points over the sovereign** on the default static yield (+0.46 to +1.70 across the
constructions). **As an expectancy** (yield plus the 0-3% granted): **about 5.8% (conservative, no
growth) to 10.0% (generous, 3%), default about 8.9%.** The floor is touched only at the most generous
corner, with the depreciation end of (c), the JV paper at full carrying value and a 3% growth rate
the last three filed years do not show.

**THE FLOOR VERDICT FIRST [E4-28]: honest expectancy about 6-9%, default 8.9%, against ~10%. QUIT
ON; not ranked, however it compares with the bond of the day.** It is above the bond by about a
point, which is exactly the case the floor exists for (*"that's true whether short rates are 6
percent or whether short rates are 1 percent"*).

**WHERE CERTAINTY IS PRICED [E3-42]:** the bare 5.34% is the only rate used; no per-name premium.
The reversion risk is shown as a sensitivity row, not added to the rate.

### THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]
At the ~10% floor, owner earnings $235M-$273M growing 0-3.5%, plus the non-operating assets at
50-100%: **roughly $2.5bn to $4.7bn, about $55 to $105 a share; the default (6.41%, 2.5%, 75%)
about $80.** At the floor with **zero** growth on the default: about **$62**. **Current price
$93.22: inside the range, in its upper half, and above the default.** Bar 2 [E4-01] would read the
middle outcome, *no useful conclusion, move on*; the floor already said no.
**What bounds the upside [E2-63]:** flat units, price pass-through, and cash returned by buybacks
rather than reinvested; the business needs little capital and has nowhere large to put it inside
doors. The ceiling is the housing stock.

### THE FLOOR FIRST, THEN THE RANKING [E4-28, E4-21]
- floor verdict: honest expectancy **~6-9% (default 8.9%)** vs ~10% **[E4-28]: below; quit on. The
  ranking lines are not filled in.**

**WHICH BAR?** Neither is applied; the floor closes the question before a margin is needed. For the
record, **Bar 2 reads "inside the range: no useful conclusion"**. **Windage count: two**, and the
second is justified: (1) the capex end of (c) at Q4; (2) the haircut on the JV stakes and PIK notes
at the conservative and default constructions. The second is not a second layer of conservatism on
the business; it values a different asset (subordinated, unenforceable-for-now paper from
businesses with a negative three-year earnings mean), and the generous construction removes it. The
reversion case is shown, never deducted.

- **VERDICT: QUIT ON at the [E4-28] floor. FAIL ON PRICE. Ranking position: not ranked.** Not
  UNKNOWABLE: the range is narrow enough to conclude, and on every construction but the most
  generous it concludes *no*.

### Q3 ADDENDUM: the buyback condition (2) [E5-08], now testable against the range
The latest quarter's purchases at **$85.00** sit **above** the default value at the floor (~$80) and
inside the range: **not at a material discount to intrinsic value conservatively calculated.
Condition (2) fails for the recent purchases.** The April 2023 to June 2026 average of **$54.86**
sits at the bottom of today's range, on an owner-earnings base that was about the same in FY2023
($262.2M), so the earlier buying passes on this arithmetic. The capital-allocation flag at Q3 is
therefore live on two counts, the Pro-Am record and the recent buyback price, and is stated with the
humility clause: this rests on my range, and *"They also know a whole lot more about them than I
do"* [E4-13]. **It binds position size, never the discount rate.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
*(No position exists or is opened. This section pre-commits the re-look, as the queue does for
floor-fail gate-clearers.)*

**Pre-committed before any entry [E1-02]:**
- **Thesis-confirming metrics:** price/mix positive in the MD&A in years of flat or falling
  volume (the [E2-44] years); continuing gross margin at or above FY2025's 47.2%; owner earnings
  back above the FY2023 $262M on the new perimeter; the Home Depot and Menards exclusive still in
  the 10-K's business description.
- **Thesis-breaking metrics and thresholds (the Q2 falsifiers, each a judgment written now):**
  (i) **price/mix negative in a fiscal year in which Griffon's MD&A reports lower material cost**
  (the pass-through reversing: the oligopoly has stopped holding price); (ii) **continuing gross
  margin below 42% in two consecutive fiscal years** (about a third of the way back to the pre-2022
  economics; FY2025 47.2%, nine months FY2026 46.2%); (iii) **the Home Depot or Menards
  exclusivity sentence removed or qualified in a 10-K**; (iv) [E2-49]: **withdrawal of the
  price/mix and volume percentages from the MD&A or of the end-market revenue table**.
- **The Q3 trigger (the capital-allocation flag):** **any acquisition outside doors, or any
  debt-funded acquisition, reopens this file at Q3** before any price is looked at [E3-40, E4-24].
- **Re-look prices, recomputed at the rate of the day:** **at or below about $82** (the ~10% floor
  met on the default owner earnings of $253.8M with 2.5% perpetual growth granted, growth the last
  three filed years do not show): a prompt for a full v4.1 re-run in which that growth is re-tested
  before it is spent. **At or below about $62** (the floor met on the default owner earnings with
  zero growth, the filed record): the price at which the name would clear the floor without a growth
  belief. **Neither is a buy signal; each is a prompt to re-run the gates, and both are VOID if a Q2
  falsifier above has fired.**
- **Next catalyst dates:** the **FY2026 10-K (expected mid-November 2026)**: the first annual report
  on the continuing perimeter, the post-refinancing debt balance, the first equity-method earnings
  from the two JVs, and the first full-year owner earnings on this perimeter, which re-strikes the
  three-year window and both bands; the Q4 FY2026 release (same week) for FY2027 guidance.

**The sell rule [E2-28]**, for a future holder: hold while the return on the capital that earns the
operating income stays high (62-94% pre-tax on the measures at Q2), no integrity event occurs and the
except-for gap between the proxy's "record" language and GAAP does not widen, and the market does not
overvalue the business. **At $93.22 the third condition would be in question for a holder**
(above the default value at the floor), recorded, not acted on, since there is no position.

**The real trigger is a moat downgrade, and it is slow [E4-17, E3-30].** The monitoring question
here: is a year of lower margin the tariff pass-through lag (aberrational), or the oligopoly giving
back the 2022 level (permanent)? The price/mix line in a year of falling steel cost decides it.

**Do not trim winners [E5-14]. Position size:** none; no entry. **Pre-committed: SIZED DOWN if it
ever clears**, because the capital-allocation flag is live on two counts.

- **VERDICT: [x] IN as a monitoring plan; no position.**

---
## SELF-AUDIT
- [x] Questions answered in order; Q1-Q4 each IN; Q5 opened only after all four; the file closes at
  Q5 on price.
- [x] No question marked IN carries an "unverified" or "provisional" caveat. Q2's class is NARROW
  and capped by two unrowable competitors (CHI, Amarr); the separating test was asked aloud and no
  document exists that would fill them, so the gap caps the class and does not suspend the gate (the
  ARM precedent). The one competitor that could be rowed at the same size (ODC) is rowed.
- [x] No UNRESEARCHED or UNKNOWABLE verdict issued.
- [x] Step 0: the filings read with accession numbers; two figures cross-checked to the dollar
  (balance-sheet identity; the FY2025 cash-flow detail lines). The August 8-Ks read and folded into a
  dated perimeter addendum.
- [x] Owner earnings on multi-year means (the three filed years of the perimeter, plus the TTM);
  the missing five-year window stated, not manufactured; (c) disclosed as a judgment on
  depreciation, not D&A; SBC resolves in every year and is subtracted in full.
- [x] Competitor row filled from filed documents: Griffon, Sanwa (IR rung), ASSA ABLOY (IR rung),
  Janus (SEC), with CHI and Amarr named as unfilled and why.
- [x] Sovereign for the earnings currency (96% US), from the US Treasury, dated 09/18/2026.
- [x] Value stated as a round range ($55-105 a share, default ~$80); windage count two, the second
  justified; no bar applied because the floor closed the question.
- [x] Price dated and flagged; corroborated by the issuer's own repurchase price.
- [x] Committed: the killed session's preserve `9716031`; perimeter and Q2 `175ecb1`; Q3 `ad55770`;
  Q4 `911764f`; Q5, Q6, this audit and the register in the next commit; the fold after.
- [x] Ledger ids: every id cited in the sections written by this session was checked against
  `principle_ledger.csv`; the draft's ids were checked too (Q2 audit).

**Errors found in the killed session's draft (all corrected by dated note at Q2, none silently):**
1. FY2022 presented as *"the literal wording of [E2-44]"*; the 10-K gives supply disruption, not
   flat demand, as the reason volume fell. Withdrawn as evidence.
2. Capex set against D&A including acquired-intangible amortisation, flattering the maintenance
   reading; re-read against depreciation, and carried into (c) at Q4.
3. An unsourced "three CEO-level strategic reversals ... without the margin moving"; withdrawn, and
   the margin did move.
4. The [E4-36] "not wave-riding" sentence without its counter-reading (the level was set by an
   industry-wide wave); counter-reading added.
5. "Hunter Fan (~12%, derived below)" never derived; derived.
6. The "FY2024 outlook" quotation sourced to the wrong document class (an earnings release, not a
   filing of outcome).

**Errors found in the brief (recorded for the operator):**
1. **"Exhibits named projectbourne"** are not a new transaction: EX-2.1 is a side letter to the AMES
   Australasia share sale agreement (*"Project Bourne - Side letter to share sale agreement"*) and
   EX-4.1 is the PIK note. **"2026-08-11 with a purchase agreement"** is a **note purchase
   agreement** with the initial purchasers of the $800M 2034 notes, not an acquisition. Nothing in
   August changes what a share buys; it changes the debt.
2. **The Q1 section recorded two further brief defects** in the killed session's own words (the
   two-segment instruction describing a company that no longer exists, and a "2023-24 disposal"
   that does not exist). They stand as written; this session did not re-verify the brief's original
   wording, which is not on disk.
3. **"the draft refers to [peer evidence] as '(below)'"**: correct, and the peer file on disk also
   refers to a `FOREIGN_fiskars_fans.md` that **does not exist** in `peers/`. The fans comparison
   was therefore built from Griffon's own filing (the named house brands), which is sufficient for
   criterion 2 and is the only source used.
4. **The tooling finding at Q4** (run.py on an 8-K recast) is not a brief error but is recorded here
   so the operator sees it in one place.

## REGISTER
- Verdict: **[x] IN on the business (Q1-Q4), quit on at the Q5 floor: FAIL ON PRICE.** [ ] OUT
  [ ] UNRESEARCHED [ ] UNKNOWABLE
- **One line:** Griffon is now, after the 2026 disposals, the largest North American garage-door
  maker (about 88% of revenue) plus a shrinking fan brand and two minority stakes; the door business
  took price in two years of falling residential demand, earns about 30% on sales and 62-70% pre-tax
  on segment assets against Overhead Door's 16% and 18-21%, and has held that level since the 2022
  repricing, though it is edging down. Owner earnings on the perimeter the share buys are about $254M
  (three filed years, capex end, pro forma interest; range $235-273M). **At $93.22 (2026-09-18) x
  45,294,716 shares (cover of 10-Q `0001628280-26-053536`) = $4,222.4M, the yield is 6.41% against a
  5.34% bond, above the bond, but the price needs 3.4% perpetual growth to reach the ~10% floor
  against owner earnings that fell about 4.6% a year over the filed perimeter's three years. Value at
  the floor about $55-105 a share, default ~$80. FAIL at Q5.** Capital-allocation flag live (the
  Hunter/AMES Pro-Am; recent buybacks above value).
