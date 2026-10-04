# Company Run — USA Rare Earth, Inc. (USAR) — 2026-09-19

**STATUS: IN PROGRESS.** Write-early protocol (`Screens/WATCHLIST RUN QUEUE.md`): this file is
created before the fetching starts and each section is appended as it closes.

**CIK 0001970622**, found with `tools/sources.py:cik_for('USAR')` and confirmed independently below.
**WAVE 6** — one of the eleven businesses the 2026-09-01 triage dropped and the operator's
screenshots recovered on 2026-09-19; one of the five ordinary businesses in that set with no
exclusion of any kind recorded. Read as unlabelled.
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

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34 %** · date **2026-09-18** · source (issuing authority) **US Treasury daily par
  yield curve, 30-year, struck fresh for this run** (`tools/sources.py:sovereign('USD')`;
  FRED DGS30 is the fallback and was not used)
- **Currency note.** The earnings currency is mixed and the mix is a Q1 fact, not a
  formality. FY2025 revenue was 77% Germany, 11% Switzerland, 12% other (10-K Note 13,
  geographic disaggregation) — invoiced by a UK subsidiary, Less Common Metals Ltd. The
  Serra Verde business acquired on 2026-09-03 operates in Brazil and Switzerland. Every
  dollar of announced government money — $277.0M direct funding, a $1.30bn loan guarantee,
  $14.2M from Texas, up to $19.3M from the Department of Energy — is USD. **USD is used**
  because the capital, the debt and the sovereign counterparties are USD; the run records
  that revenue today is earned in EUR and GBP and will be earned in BRL, and that no
  owner-earnings number exists for the FX mix to distort.
- FX / ADR ratio: not applicable. One class of common stock, US-listed, Nasdaq: USAR.

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- **Primary document: Form 10-K for FY2025, filed 2026-03-30, accession
  `0001970622-26-000021`** (`usar-20251231.htm`), read with:
  - **Form 10-Q for the quarter ended 2026-06-30, filed 2026-08-10, accession
    `0001970622-26-000057`** (`usar-20260630.htm`) — the latest periodic report;
  - **Form 8-K of 2026-09-04 for the event of 2026-09-03, accession
    `0001213900-26-097399`** — the Serra Verde closing, items 1.01, 2.01, 2.03, 3.02, 5.02;
  - **Form 8-K of 2026-09-15, accession `0001213900-26-100190`, Exhibit 99.1** — supplemental
    risk factors filed four days before this run, the most current filed statement of the
    business;
  - **Form 8-K of 2026-08-24, accession `0001213900-26-092810`** — the Offtake Amendment and
    the capitalisation of the counterparty;
  - **Form 8-K of 2026-07-23, accession `0001213900-26-080645`** — the Carester Investment
    Agreement.
- **Figure cross-checked against the filed statement:** FY2025 **net cash used in operating
  activities of $(48,985) thousand**. Read three ways and all three agree: the MD&A Cash
  Flows table (*"Net cash used in operating activities $(48,985)"*), the MD&A narrative
  (*"net cash used in operating activities was $49.0 million"*), and the XBRL fact
  `NetCashProvidedByUsedInOperatingActivities` for CY2025 (−48,985,000, 10-K filed
  2026-03-30). Also cross-checked: **FY2025 revenue $1,643 thousand** against
  `Revenues` CY2025 = 1,643,000.

### THE CIK HOLDS A PREDECESSOR'S FIGURES, AND THE PREDECESSOR WAS A BLANK CHEQUE

`tools/sources.py:name_change_note('0001970622')` fired: *"was 'Inflection Point Acquisition
Corp. II' until 2025-03-11."* It is a real perimeter event and the run confirmed it from the
filings, as the NEGG and RGTI runs did:

- **Inflection Point Acquisition Corp. II** was *"originally incorporated on March 6, 2023 as
  a Cayman Islands exempted company for the purpose of effecting a merger, share exchange,
  asset acquisition, share purchase, reorganization or similar business combination"* — a
  SPAC (10-K FY2025, Item 1, "History of USA Rare Earth"). It domesticated into Delaware on
  **2025-03-12** and renamed itself USA Rare Earth, Inc.; the business combination with
  **USA Rare Earth, LLC** closed **2025-03-13**, and the common stock began trading on
  Nasdaq on **2025-03-14**.
- **Two 10-Ks under this CIK are the SPAC's, not the operating company's**: FY2023
  (accession `0001213900-24-029041`, `ea0202401-10k_infle2.htm`) and **FY2024 (accession
  `0001213900-25-026445`, filed 2025-03-31)**. Nine of the eleven 10-Qs on file are the
  SPAC's too.
- **The splice is visible in companyfacts as two different values for the same year**, which
  is the SOUN defect of 2026-09-19 in a second registrant. `NetCashProvidedByUsedInOperating
  Activities` for CY2024 carries **−$1,398,564 (10-K filed 2025-03-31, the SPAC's own
  figure)** and **−$12,991,000 (10-K filed 2026-03-30, USA Rare Earth LLC recast)**. Any
  screen reading the earliest vintage understates the burn by a factor of nine.
- The FY2025 10-K states the rule explicitly: *"the historical financial information included
  in this annual report … including the recast audited financial statements … are that of USA
  Rare Earth LLC prior to the consummation of the Merger."* **So the operating company has
  exactly two recast annual periods on file, FY2024 and FY2025, and FY2025 contains six weeks
  of the only revenue-producing subsidiary.**

### THE SHARE COUNT, AND WHAT WAS ISSUED AFTER THE COVER DATE (the RGTI precedent)

| as of | shares of common | source |
|---|---|---|
| 2025-03-28 | 81,952,420 | 10-K FY2024 cover (the SPAC's 10-K) |
| 2026-03-23 | **217,976,175** | 10-K FY2025 cover, accession `0001970622-26-000021` |
| **2026-08-04** | **244,720,099** | **10-Q cover, accession `0001970622-26-000057`** |
| 2026-09-03 | **+126,849,307** | 8-K `0001213900-26-097399`: the Serra Verde merger consideration, issued **after** the cover date |
| **pro forma** | **371,569,406** | cover count plus the closed stock issuance |

Also outstanding: **1,224,351 shares of 12% Series A Cumulative Convertible Preferred**
(10-Q cover); a **warrant held by the U.S. Department of Commerce over 17,600,584 shares at
$17.17**, exercisable from 2027-06-03 (out of the money at the price below); and public
warrants at $11.50. **A further issuance is contracted and not yet counted**: the Carester
Contribution in Kind, EUR 11,666,700 of USAR common stock priced off the close nine calendar
days before completion (8-K `0001213900-26-080645`), and the TMRC merger consideration of
**3,823,328 shares** (10-K FY2025). Neither is in the 371.6M.

**dei cover facts are missing from companyfacts for the last three periodic reports** — the
latest `EntityCommonStockSharesOutstanding` it publishes is **132,638,561 at 2025-10-31**.
This is the HBB/SOUN "no share count from dei" layer arriving on a name that was never in
that list: a screen pricing USAR today off companyfacts would divide by a count **2.80x too
small**. The count above was read off the cover of the filing itself.

**PRICE, and the aggregator is flagged.** **US$15.37, close of 2026-09-18**, from
`tools/sources.py:price('USAR')` — an **aggregator quote, used for the live price only**.
- cover-date cap: 244,720,099 x $15.37 = **US$3,761M**
- **pro forma cap including the Serra Verde shares: 371,569,406 x $15.37 = US$5,711M**

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

### What is actually filed, by leg

There are four legs and they are in four different states. The whole Q1 question is whether
the filed record lets a buyer estimate the cash any of them will produce.

**(1) Less Common Metals Ltd. (LCM), Cheshire, UK — the only leg with revenue.** Acquired
**2025-11-18** (8-K `0001970622-25-000081`; Indian Ocean Rare Metals Pte. Ltd., LCM's
parent, bought by a wholly owned subsidiary). It converts rare-earth oxides into metals and
alloys. **Every dollar of filed revenue comes from here**, and the 10-Q says so in terms:
*"All of our revenue for the three and six months ended June 30, 2026 is attributable to
Less Common Metals"* and *"Our revenues … were derived solely from our metal-making
operations following the acquisition of Less Common Metals in 2025, and we have not yet
generated revenues from our neo magnet manufacturing or mineral production."*

| filed period | revenue | cost of revenue | gross profit |
|---|---|---|---|
| FY2024 (USA Rare Earth LLC, recast) | $0 | $0 | $0 |
| FY2025 (six weeks of LCM only) | **$1,643,000** | $1,448,000 | **+$195,000** |
| Q1 2026 | $5,698,000 | $5,592,000 | +$106,000 |
| **Q2 2026** | $5,821,000 | $7,404,000 | **−$1,583,000** |
| **H1 2026** | **$11,519,000** | **$12,996,000** | **−$1,477,000** |

*(10-K FY2025 and 10-Q Q2 2026, income statements; XBRL `Revenues`, `CostOfRevenue`,
`GrossProfit`.)* **The one leg that sells anything sold it at a gross loss in the most recent
quarter.** Concentration, from 10-K Note 13: **Customer 1 = 73% and Customer 2 = 18% of
FY2025 revenue (91% in two), one vendor = 81% of raw-material purchases**, and the revenue is
77% Germany, 11% Switzerland. The 10-K itself calls the concentration non-indicative of a
trend, which is a statement that six weeks tells you nothing.

**(2) The Stillwater, Oklahoma magnet plant — no revenue, and no customer contracts.** The
10-K: *"we successfully commissioned Phase 1a of sintered NdFeB permanent magnet block
production in the first quarter of 2026, which involved running and testing the equipment to
ensure production readiness. We expect to begin fulfilling customer orders in the second
quarter of 2026."* The second quarter of 2026 is filed, and the revenue in it is LCM's. The
supplemental risk factors filed **2026-09-15** — four days before this run — still say:
*"We have commissioned and are producing under Phase 1a and are in the process of
commissioning Phase 1b … **We do not currently have any revenue or definitive off-take or
sales agreements with customers in place in our magnet business.**"* The FY2025 10-K said the
same thing about the whole company: *"We do not currently have any contractually committed
customers for the planned output and delivery of neo magnets."* **So for the leg the company
is named after, the filed record contains neither a price, nor a volume, nor a counterparty.**

**(3) The Round Top deposit, Sierra Blanca, Texas — an exploration-stage property with no
declared resource.** The 10-K states it four separate times, and the words are the filer's:
- *"**We do not have declared mineral resources as defined under Item 1300 of Regulation
  S-K** and have not yet begun to extract minerals from the Round Top Project."*
- *"It is our view that the Round Top Project is considered an 'exploration stage property'
  under Item 1300, in that the Round Top Project is **a property that has no mineral reserves
  disclosed. Mineral resources that are not mineral reserves have no demonstrated economic
  viability.**"*
- *"the Company is **not relying on the 2019 PEA** for the purpose of reporting mineral
  resources. The Company does not currently intend to update the 2019 PEA … There is no known
  significant production reported from previous operators."*
- *"**We have not yet established that the Round Top Mountain deposit contains any
  commercially exploitable quantities of proven and probable mineral reserves**, and we may
  not be able to do so."*

The timetable is filed: a **Pre-Feasibility Study** commenced in H1 2026, a **Definitive
Feasibility Study** is a government milestone targeted between December 2026 and December
2028, and the Accelerated Mining Plan *"anticipates the start of commercial production at
Round Top in late 2028."* USAR holds **81.3%** of the Round Top joint venture RTMD; TMRC
holds 18.7% and is being bought for 3,823,328 shares.

**(4) Serra Verde / SVRE Holdings — bought 16 days before this run, and it is the largest leg
by consideration.** Closed **2026-09-03** for **$300,000,000 in cash and 126,849,307 shares**
(8-K `0001213900-26-097399`), a consideration the 10-Q put at *"approximately $2.83 billion"*
when announced. The Pela Ema mine in Goiás, Brazil *"began production in January 2024 and is
currently completing an advanced-stage optimization and commissioning program, with ramp-up
expected in the third quarter of 2026"*, targeting ~4,000 tpa TREO by end-2026 and 6,400 tpa
average in stage two. **Not one Serra Verde financial statement line appears in any USAR
periodic report yet**: the acquisition closed after the 2026-06-30 balance-sheet date and
after the 2026-08-04 cover. Its debt did come across — the **Retained Finance Agreement with
the U.S. International Development Finance Corporation, up to $565,000,000** (Initial Loan up
to $465M at Term SOFR + 4.0%, fifteen years, 49 sculpted quarterly instalments, secured by a
first lien on 100% of the merger subsidiary and substantially all its assets).

### Unit economics, in my own words, without management's language

**A buyer of this share today is buying a construction programme and a government
relationship, with a small metals workshop and a ramping Brazilian mine attached.** Money is
supposed to be made in four places: dig rock in Texas and Brazil; separate the oxides;
convert oxides into metals and alloys; press the alloys into magnets and sell them to
carmakers, defence primes and MRI makers. Today the cash goes the other way. In the twelve
months to 2026-06-30 the business collected **$13.2M** of revenue (FY2025's $1,643k, all of it in the second half,
plus H1 2026's $11,519k) and **used $75.3M of operating cash in the first half of 2026 alone** (10-Q). The gap is paid by selling shares:
$303.8M of warrant exercises and $190.1M of new stock in FY2025, then **69.77 million shares
for $1.5 billion gross on 2026-01-28**, then 16,132,790 shares plus a 17,600,584-share
warrant handed to the Department of Commerce, then 126,849,307 shares handed to Serra Verde's
owners. The count went from 60,091,000 at 2024-12-31 to **371,569,406** pro forma — **6.2x in
twenty-one months.**

**The scarce input the business controls.** Two candidates, and the filings settle both.
(a) *Heavy rare earths outside China* — dysprosium, terbium, yttrium — where the 10-K says
China controls *"~99% of global HREE processing."* USAR's claim on that scarcity is the Round
Top deposit, **which has no declared resource**, and Serra Verde, which it has owned for
sixteen days. (b) *The U.S. government's willingness to pay for a non-Chinese supply chain* —
DFARS 225.7018 bars the Department of War from buying Chinese magnets from **2027-01-01**, and
the filed money follows: a $277.0M direct funding agreement, a $1.30bn loan guarantee, a
$565M DFC loan, $14.2M from Texas, up to $19.3M from the DOE, and an offtake counterparty
(**US SIIE, LLC**) into which the U.S. government has put **$750 million**. **(b) is the real
scarce input, and USAR does not control it.** That is [E2-59]'s regime, not a property of the
product.

### Will the fundamentals look broadly the same in ten years?

No, and not in the ordinary way. The company is not a stable thing being mis-measured; it is
four different businesses at four different stages, three of which have changed hands or
state in the last ten months. Between 2025-03-13 and 2026-09-03 it de-SPACed, bought a UK
metal maker, commissioned a magnet line, signed two agreements with the Department of
Commerce, agreed a French joint venture, agreed to buy out its own joint-venture partner, and
closed a $2.8bn acquisition of a company its own 10-K had named six months earlier as
*"Serra Verde Group, which produces both LREE and HREE but currently relies on processing
pathways that flow through China"* — **a competitor in the Competition section of the annual
report and a subsidiary by September.** [E3-31] asks for businesses *"relatively simple and
stable in character"*; this is the opposite end of that axis.

### THE SEPARATING TEST, ASKED ALOUD

**"Can I name the document that would resolve this?"** The question Q1 asks is whether future
cash flows can be estimated from the filed record. Taking the four legs one at a time, because
the answer differs and an honest verdict has to survive the leg where the answer is "yes":

| leg | the document that would resolve it | does it exist? |
|---|---|---|
| Round Top | the Pre-Feasibility Study, then the Definitive Feasibility Study | **No.** The PFS *"commenced"* in H1 2026 and is unfinished; the DFS is a milestone targeted Dec 2026–Dec 2028. The filer has withdrawn its only prior study from reliance. **Nothing can be fetched.** |
| Stillwater magnets | a definitive customer offtake or sales agreement | **No.** Stated as absent on 2026-09-15: *"we do not currently have any … definitive off-take or sales agreements with customers in place in our magnet business."* A document that has not been signed cannot be retrieved. |
| LCM | audited accounts and a multi-year series | **Partly.** Six weeks in FY2025 and two quarters of 2026 are filed; the pre-acquisition history of a private UK company is not. But a full LCM history would settle a business that ran a **gross loss** on $5.8M of quarterly revenue — it cannot carry the valuation of a $5.7bn quote. |
| Serra Verde | audited SVRE accounts and the Offtake Agreement with its price floors | **Yes, in part — and that part is UNRESEARCHED.** The DEFM14A of 2026-07-24 and the S-4 of 2026-05-13 carry SVRE financial statements, and the Offtake Agreement is described in 8-Ks. **But the mine is mid-commissioning** (*"ramp-up expected in the third quarter of 2026"*), the counterparty's $500M senior debt facility *"has not been documented, closed or funded"*, and the amount of the floor price is in no document this run could locate. |

**The verdict follows the two legs that carry the story and cannot be researched at all.**
This is not a case where a filing sits unfetched. For Round Top the study does not exist and
the filer says so; for the magnet plant the customer contracts do not exist and the filer says
so, as recently as four days ago. **No document that anyone can obtain would tell me what
those two legs earn, because the facts they would report have not happened.** That is the
definition of UNKNOWABLE in this framework, and it is the RGTI finding of 2026-09-13 again on
a different balance sheet.

**And the honesty runs the other way too, per [E3-47].** The closed file has a price and the
run must not reach for UNKNOWABLE as a shortcut. Three things were checked before writing it:
- *Is this simply a cheap business I am too lazy to value?* No — the arithmetic is trivial and
  is computed below at Q5. The obstacle is not effort.
- *Is there a leg whose cash flows ARE estimable, which would make the whole thing merely
  UNRESEARCHED?* Serra Verde is the candidate, and its documents exist. But buying USAR is not
  buying Serra Verde: Serra Verde is one of four legs, it was consolidated sixteen days ago,
  it is mid-commissioning, and the $2.83bn paid for it was paid mostly in paper whose value
  depends on the other three legs. **A leg that can be researched inside a company that cannot
  be does not convert the verdict.**
- *Would waiting five months help?* [E4-46] says a named filing inside an understood business
  is a work order and a business needing months of study is Q1 OUT. This is neither: it is a
  business whose determining facts are **scheduled**, not studied — late 2028 for Round Top
  production, 2027-01-01 for DFARS, December 2026 to March 2028 for ten government milestones.
  The framework has a verdict for that and it is not OUT and not UNRESEARCHED.

- **VERDICT: [ ] IN  [ ] OUT  [ ] UNRESEARCHED  [x] UNKNOWABLE → the future cash flows of the
  two legs that justify the quote cannot be estimated from any document that exists.**
  Specifically: (a) Round Top has **no declared mineral resource under Item 1300 of Regulation
  S-K**, its only study has been withdrawn from reliance, and its Pre-Feasibility Study is
  unfinished; (b) the Stillwater magnet business has **no definitive customer offtake or sales
  agreement** as of 2026-09-15 and therefore no filed price or volume; (c) the acquired
  businesses that do have revenue have been owned for six weeks (LCM, FY2025) and sixteen days
  (Serra Verde) respectively, and the one with a filed series ran a **gross loss** last
  quarter. **Close without prejudice.** This is a real company building real plant, and the
  file says nothing about whether it will work.

---
⛔ **Q1 is not IN. Under the hard sequence (operator rule 2) the file closes here.** Q2, Q3
and Q4 below are **RECORDED, NOT GOVERNING**: they were read because the queue's output
contract requires a price and a pass/fail line, and because a wrong UNKNOWABLE is the most
expensive error class in the corpus **[E3-47]** — so the work that would have overturned it
is shown. **No verdict below promotes anything.**

---
## Q2 — IS IT A FRANCHISE? **[E3-03]** — RECORDED, NOT GOVERNING

- Needed or desired [x] — DFARS 225.7018 bars the Department of War from buying Chinese
  magnets from **2027-01-01**; the product is wanted and the buyer is named.
- No close substitute [ ] — **fails.** Neodymium-iron-boron magnets are a commodity with a
  published world price. The 10-K's own Competition section names five substitutable
  suppliers and calls China *"the most prominent global competitor"*, whose companies
  *"offer REEs and magnets at subsidized prices, often undercutting other producers."*
  A magnet from Stillwater and a magnet from Ningbo do the same job; only the provenance
  differs, and the provenance is worth something because a regulation says so.
- Not price-regulated [ ] — **and this is the finding of Q2.** The price is not capped; it is
  **floored, by governments, for every Western producer including this one.** [E3-03]
  criterion 3 is about caps; [E2-59] is about floors, and it is the row that governs here.

### Must the moat be continuously rebuilt? **[E4-04]**

Yes, on the narrow reading the IBM run used and this run adopts: **the asset is replaced, not
merely defended.** A deposit is depleting by construction, and USAR does not yet have one that
qualifies as a resource. Every advantage claimed in the filings is a plant to be built, a
milestone to be hit, a feedstock contract to be signed or a company to be bought — Round Top,
Wheat Ridge, Stillwater Phase 1a/1b, Blacksburg, Lacq, LCM, Carester, TMRC, Serra Verde, all
inside eighteen months. [E5-23]'s *"working at improving your own moat … all of the time"* is
prescribed for every moat; what is excluded is the moat whose **basis** must be periodically
replaced, and a mine plus a government programme is that class. And **[E4-36]**'s four causes
of extreme success place the record squarely in the fourth, **wave-riding**: the wave is the
2025-26 Western re-shoring of rare earths, visible in the price series Lynas publishes below.
*"A surfing run is not a moat; the advantage lives in the wave, not the surfer."*

### Primary moat metric, filing-sourced, and its trend

There is no return on capital to measure: **owner earnings are negative on every construction
(Q4)**, and equity return is negative in both filed years. The honest primary metric for a
business at this stage is **gross margin on what it actually sells**, and its trend is down:

| USAR, filed | revenue | cost of revenue | gross margin |
|---|---|---|---|
| FY2025 (six weeks of LCM) | $1,643k | $1,448k | **+11.9%** |
| Q1 2026 | $5,698k | $5,592k | +1.9% |
| **Q2 2026** | $5,821k | $7,404k | **−27.2%** |
| H1 2026 | $11,519k | $12,996k | −12.8% |
| **H1 2026 pro forma with Serra Verde** | $12,107k | $18,308k | **−51.2%** |
| **FY2025 pro forma with Serra Verde** | $4,129k | $37,553k | **−809.5%** |

*(8-K `0001213900-26-097399`, Exhibit 99.3, the filed unaudited pro forma condensed combined
statements of operations.)* **Direction [E4-32] reads the wrong way on the only metric that
exists.**

### THE COMPETITOR ROW — required **[E3-28]**

Same metric, same window where windows permit, filing-sourced. **Metric: revenue, gross
margin, and cash from operations, latest completed fiscal year.**

| company | window | revenue | gross margin | cash from operations | source |
|---|---|---|---|---|---|
| **USA Rare Earth (subject)** | FY2025 (cal.) | **$1.6M** | +11.9% | **−$49.0M** | 10-K `0001970622-26-000021` |
| **USAR pro forma with Serra Verde** | FY2025 (cal.) | **$4.1M** | **−809.5%** | not presented (pro formas carry no cash-flow statement) | 8-K `0001213900-26-097399` Ex. 99.3 |
| **MP Materials Corp.** | FY2025 (cal.) | **$224.4M** | **+14.1%** *(before $89.3M of DD&A)* | **−$155.8M** | 10-K `0001801368-26-000008`, filed 2026-02-26 |
| **Energy Fuels Inc.** | FY2025 (cal.) | **$65.9M** | +20.9% | **−$89.5M** | companyfacts, CIK 0001385849, 10-K facts |
| **Lynas Rare Earths Ltd** | FY2026 (to 30 Jun 2026) | **A$977.9M** | **+40.1%** | not in the released statement; **NPAT A$222.4M, EBITDA A$386.0M** | ASX announcement 2026-08-26, `announcements.asx.com.au/asxpdf/20260826/pdf/0737tbnynjls6y.pdf` |
| Chinese producers (China Northern Rare Earth and others) | — | **no cell** | — | — | **not SEC registrants; see the limit below** |
| Noveon Magnetics Inc. | — | **no cell** | — | — | private, US |
| VACUUMSCHMELZE GmbH & Co. KG | — | **no cell** | — | — | private, Germany |
| Neo Performance Materials Inc. | — | **no cell** | — | — | Canadian; SEDAR+ rung not pulled by this run |
| KSM Metals / Australian Strategic Materials Ltd | — | **no cell** | — | — | ASX; being acquired by Energy Fuels per USAR's 10-K |

- **Peers named: 9, of whom 3 carry filled cells.** The nine are USAR's own list — the 10-K
  Competition section names MP Materials, Noveon, VACUUMSCHMELZE, KSM Metals/ASM, Lynas,
  Serra Verde (since acquired) and China; Energy Fuels enters because USAR's own filing says
  it is acquiring KSM. Buffett says eight **[E3-28]**; the industry has about nine and three
  of them file.
- **THE SOURCE RULE, stated for Lynas.** Lynas Rare Earths Ltd is **not an SEC registrant**,
  so the evidence ladder drops to the **exchange-filings rung**: the figures above are read
  from the company's own announcement to the ASX of 2026-08-26, in **Australian dollars as the
  filer reports them and not converted**, which is the same discipline the IBM run used to read
  SAP in euro. Cash from operations is not in that announcement; it is in the full financial
  report, which this run did not pull, so the cell is **left empty rather than guessed**.
- **THE LIMIT, stated for China.** The Chinese producers are the low-cost majority of this
  industry — USAR's 10-K puts China at *"an estimated 90% of global REE processing and
  approximately 99% of global HREE processing"* — and **no document on this project's citation
  shelf reports their revenue, margin or cash flow**, because they are not SEC registrants and
  the project does not read Shanghai filings. Under the four verdicts that cell is
  **UNKNOWABLE, not UNRESEARCHED**, exactly as the queue treats the seven non-SEC names.
  What the filings of the peers do say about them is usable, and it is decisive:
  MP Materials' 10-K — *"Supply of REE and magnet materials is dominated by Chinese producers.
  **The Chinese Central Government regulates production via quotas and environmental
  standards**"*; USAR's 10-K — China *"has banned the export of such technologies and
  capabilities"* since December 2023, and USAR itself is *"designated on an export control list
  by China"* (8-K `0001213900-26-097399`, Exhibit 99.1).
- Any peer unavailable → **the template's rule makes the class PROVISIONAL.** Recorded. **But
  the missing cells cannot rescue a moat, because of what they are**: two private Western
  magnet makers (competitors, whose data would narrow any advantage), a Canadian magnet maker
  (the same), an Australian metal maker being bought by a peer, and the subsidised Chinese
  majority. **Every missing cell points the same way.** So the class below is written NONE with
  PROVISIONAL recorded beside it, and neither reading promotes the name.

### What the row actually shows, and it is the whole of Q2

**[E2-58]**, 1982: *"For the great majority of companies selling 'commodity' products, a
depressing equation of business economics prevails: **persistent over-capacity without
administered prices (or costs) equals poor profitability.**"* And **[E2-59]**, the same letter:
profit troubles *"may be escaped, true, **if prices or costs are administered** in some manner
and thereby insulated at least partially from normal market forces … (a) **legally through
government intervention**"* — but the escape belongs to the regime.

The row is that paragraph, filed, in 2026:

1. **The two producing US filers both consumed cash in FY2025.** MP Materials — the only
   scaled, vertically integrated North American producer, a real mine operating since 2018,
   with a magnet plant already selling to General Motors — had **revenue of $224.4M, down
   57.5% from $527.5M in FY2022**, and **cash from operations of MINUS $155.8M**. Energy Fuels:
   revenue $65.9M, cash from operations **minus $89.5M**. Neither is a start-up excuse case;
   both are what this industry's economics look like after the plant is built.
2. **The one profitable peer says why it is profitable, and the answer is the government.**
   Lynas, FY2026: *"Rare earths market prices strengthened during the year and **Lynas secured
   floor price agreements to supply both Japanese and U.S. industry.** A record average annual
   selling price of A$80.7/kg REO was achieved … reflecting improved market prices, an
   increased mix of heavy rare earth sales, and **sales with pricing not linked to the market
   index**."* And on the price itself: *"The average China domestic price of NdPr (VAT
   excluded) increased from **US$55.0/kg in June 2025 to US$100.8/kg in June 2026. This was
   influenced by floor price agreements led by global governments**."* Lynas's own NPAT went
   from **A$8.0M in FY2025 to A$222.4M in FY2026** on that move.
3. **The floor is the same number at three different companies, and the state takes the
   upside.**
   - **Lynas / JARE (Japan), announced March 2026:** *"firm offtake for 5,000 tonnes per annum
     NdPr with a **US$110/kg NdPr floor price** and an upside sharing arrangement when prices
     exceed US$150/kg NdPr, **capped at US$10m/annum**."*
   - **MP Materials / U.S. Department of War, July 2025:** the Price Protection Agreement
     *"provides a **price floor of $110 per kilogram ("kg") for NdPr** products stockpiled,
     sold to internal affiliates, or sold to third parties. If market prices fall below this
     threshold, the Company will receive a quarterly payment from the DoW to offset the
     shortfall. Conversely … **the Company will remit a portion of the upside to the DoW, equal
     to 30% of the NdPr sales price in excess of $110 per kg.**"* The same agreements have the
     DoW *"guarantee that the 10X Facility will generate **at least $140 million of EBITDA**"*
     and give it *"the right to purchase all of the magnets produced"* there.
   - **USAR / Serra Verde, via US SIIE, LLC:** a 15-year offtake under which *"100% of Phase I
     production of the four magnetic rare earth elements is allocated on a take-or-pay basis"*,
     carrying *"**floor price protection, annual price escalation, favorable upside-sharing
     mechanics, take-or-pay volume commitments**"* — with the counterparty *"a special purpose
     vehicle capitalized by the U.S. government and private capital sources"* into which
     **the U.S. government has put $750 million** plus a $300M forward purchase commitment
     (8-K `0001213900-26-092810`).
   **This is [E2-59] with the receipts.** *"Regulation caps a franchise and floors a commodity
   business; neither creates the class."* The moat here is a line item in an appropriation.
   And the corpus names the end: *"That day is gone"* is how it finishes.
4. **[E3-62], the second step, is answered by the industry's own filings.** Who keeps the
   gains? In a commodity business *"All of the advantages from great improvements are going to
   flow through to the customers."* Here it is starker than the textile loom: **the upside
   above the floor is contractually remitted to the state** — 30% above $110/kg at MP, capped
   upside-sharing at Lynas, *"favorable upside-sharing mechanics"* at USAR. The patron who
   floors the price also takes a share of the ceiling.
5. **[E2-44]'s two-characteristic test:** can it raise prices with flat demand and idle
   capacity? No — it does not set its price at all; a published world index and a government
   floor do. Can it grow dollar volume *"with only minor additional investment of capital"*?
   No — its own 10-K names **$4.1 billion of required long-term capital expenditures**.
6. **[E2-45]'s attacker's test**, the shelf's one forward-looking moat test: with ample capital
   and skilled people, how would I compete with this? By doing what Energy Fuels, Noveon, VAC,
   ASM, Carester and Serra Verde are already doing — and by 2026 the U.S. government was
   funding several of them at once, which is competition *funded by the moat itself*.
7. **[E3-33]/[E5-28] untapped pricing power:** absent, and claiming it would be claiming near
   monopoly in a market where one country holds 90%.
8. **[E3-61]'s limit on the row, stated:** the row shows position, never conduct. It cannot
   tell me whether these five Western producers will behave like a demented Kellogg when the
   2028 capacity all arrives at once — *"I think you'd have to know the people involved."*

- Class: [ ] WIDE [ ] NARROW [x] NONE [x] PROVISIONAL *(both marked, per the rule above:
  NONE on the filled cells, PROVISIONAL because five cells are empty; the empty cells all
  point adversely)* · Direction: **narrowing** — the protection is a contract with an expiry
  and a milestone schedule, not a property of the product.
- **VERDICT (RECORDED, NOT GOVERNING): OUT on the evidence read.** This is the commodity end
  of **[E2-58]** rescued by the administered pricing of **[E2-59]**, and the corpus is explicit
  that the rescue *"belongs to the regime"*. Had Q1 returned IN, this file would have closed
  here.

---
## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL? — RECORDED, NOT GOVERNING

### STEP 1 — THE WEIGHT CASE

- [x] **Daily execution [E3-38, E3-43, E2-70]** — ticked, and it is the strongest tick in the
  file. There is no franchise to absorb error: **[E3-43]**'s *"a business, unlike a franchise,
  can be killed by poor management."* Everything here is execution — commissioning a magnet
  line, hitting ten dated government milestones, qualifying product with customers who have not
  signed, finishing a feasibility study, integrating four acquisitions in one year. And the
  people doing it keep changing: **three chief executives inside twenty-two months** — Joshua
  Ballard from 2024-12-16, Barbara Humpton from 2025-10-01, Thrasyvoulos Moraitis from
  **2026-10-01** (10-K Item 11; 8-K `0001213900-26-097399`).
- [ ] Control **[E1-16]** — not ticked; a marketable minority stake, exitable.
- [x] **Leverage [E3-29]** — ticked and quantified. Today it is modest: pro forma total
  liabilities **$2,002.2M** against pro forma equity **$4,714.5M**, including the assumed
  **DFC loan of $304.1M** ($6.1M current, $298.0M non-current at fair value) and a **royalty
  agreement liability of $226.9M**. But the direction is committed: the Loan Guarantee
  Agreement provides for **$1.30 billion** of Federal Financing Bank borrowings at Treasury
  plus 150bp, the DFC Initial Loan may run to **$465M** at Term SOFR + 4.0% secured by a first
  lien on *"100% of the shares in Merger Sub and substantially all assets of Merger Sub and its
  subsidiaries"*, and the equity that would absorb an error is itself **$602.5M of goodwill,
  $312.6M of other intangibles and $912.1M of deferred arrangement costs** — $1,827.2M, or 39%
  of pro forma equity, in assets that exist only if the plan works.

**Case declared: Q3 is a BINARY GATE, and no price compensates [E1-16, E3-29, E5-35].**

### Honesty — binary, permanent, filings-based **[E5-16]**

**No disqualifier found**, and the finding is written as the framework requires — *the absence
of found disqualifiers, not a finding that the managers are honest* **[E5-17]**.
- **Clean audit opinion.** BDO USA, P.C. (formerly HORNE LLP), Ridgeland, Mississippi, PCAOB
  ID 243: the FY2025 and FY2024 statements *"present fairly, in all material respects."* No
  going-concern paragraph. Management concluded disclosure controls and **internal control
  over financial reporting were effective as of 2025-12-31**; as a non-accelerated filer and
  an emerging growth company there is **no auditor attestation on internal control**, which is
  recorded as a limit, not a flag. Read beside **[E5-32]**: audited does not mean true.
- **Two auditor changes in seven months, and both read structural, not adversarial.**
  8-K `0001213900-25-035605` (event 2025-04-23): UHY LLP, the SPAC's auditor, exits after the
  de-SPAC, with a clean Exhibit 16.1 letter. 8-K `0001970622-25-000072` (event 2025-11-01):
  *"the partners and professional staff of Horne LLP … joined BDO USA, P.C. As a result of this
  transaction, Horne resigned"* — a firm combination. Both filings state **no disagreements**
  and no Item 304(a)(1)(v) matters, and Horne's own letter agrees. **Auditor churn that would
  fire the cockroach prompt [E4-22] does not fire here**, and saying so is part of reading the
  flag honestly.
- No restatement, no material weakness, no SEC enforcement matter found in the FY2025 10-K or
  the 2026 10-Qs. One litigation settlement, paid in shares, **$1,674k**, disclosed on the face
  of the FY2025 cash-flow statement.

### STEP 2 — THE FLAGS. Five fired. Each was read.

- [x] **Serial share issuance — [E5-15]**, *"one of the surest indicators of a promotion-minded
  management, weak accounting, a stock that is overpriced and — all too often — outright
  dishonesty."* This is the loudest fact in the file and it is not close:
  **60,091,000 shares at 2024-12-31 → 371,569,406 pro forma at 2026-09-03, a 6.2x in
  twenty-one months**, through a de-SPAC, $303.8M of warrant exercises, a $75M PIPE, a
  **$1.5 billion private placement of 69.77 million shares on 2026-01-28**, 16,132,790 shares
  plus a 17,600,584-share warrant to the Department of Commerce, 126,849,307 shares to Serra
  Verde's owners, and contracted issuances still to come to Carester and TMRC. **Read as
  [E5-15] asks:** the accounting is clean and no dishonesty was found, so what the flag is
  detecting here is the third item on its list — **that the paper is the currency**, and every
  asset in the business was bought with it.
- [x] **Trumpeted earnings projections and growth targets — [E4-22]'s third flag, with
  [E3-48]'s action.** The 10-K admits the practice in its own risk factors: *"**We have set
  certain targets for revenues; earnings before interest, taxes, depreciation and amortization
  ("EBITDA"); free cash flows; capacity; and production.** Such targets were prepared based on
  numerous variables and assumptions which are inherently uncertain … these targets may be
  inaccurate and should not be relied upon."* **[E3-48]**'s remedy is to set the company's own
  past guidance against outturn, and the run did exactly that on the one target with a filed
  date: the FY2025 10-K said *"We expect to begin fulfilling customer orders in the second
  quarter of 2026."* **Q2 2026 is filed; every dollar of its revenue is Less Common Metals';
  and on 2026-09-15 the company still had no definitive magnet sales agreement.** One
  observation is not a base rate, and it is the only one available on a company this young —
  recorded as such. **[E5-30]** is the reason it matters anyway: a guidance culture is a
  ratchet, *"do it once and you probably never stop."*
- [x] **EBITDA promotion — [E4-29]**, *"a particularly pernicious practice."* Fires, but
  **weakly, and the run says which way.** The Q2 2026 earnings release
  (8-K `0001970622-26-000056`, Exhibit 99.1) presents **no** Adjusted EBITDA: its only non-GAAP
  measures are adjusted net loss and adjusted loss per share, defined as net loss adjusted for
  preferred dividends and the fair-value swings — and, to the company's credit, **stock
  compensation is not added back**. What fires is the narrative use: the acquisition will
  *"accelerate the Company's EBITDA and cash-flow generation"*, and the 10-K confirms EBITDA is
  one of the targets set. **Read per [E5-41]:** EBITDA deletes depreciation, and depreciation
  is *"reverse float"* — the worst kind of expense, already paid. In a business whose pro forma
  balance sheet carries **$3.25 billion of plant, almost all of it development-stage**, an
  EBITDA target is the deletion of the single largest future cost.
- [x] **Incentives — [E4-27]**, *"Never, ever, think about something else when you should be
  thinking about the power of incentives."* **What the pay vests on is time, not output.**
  FY2025 Summary Compensation Table (10-K Item 11):

  | executive | year | salary | bonus | **stock awards** | total |
  |---|---|---|---|---|---|
  | Barbara Humpton, CEO (from 2025-10-01) | 2025 | $167,308 | — | **$11,536,719** | $11,704,654 |
  | Joshua Ballard, former CEO (to 2025-10-01) | 2025 | $351,346 | — | $4,637,862 | $5,516,087 |
  | William Robert Steele Jr., CFO (from 2025-03-24) | 2025 | $311,539 | $246,181 | $4,245,589 | $4,827,271 |
  | David Kronenfeld, former Chief Legal Officer | 2025 | $305,000 | $195,000 | $1,622,238 | $2,242,430 |

  **Stock awards to four named executives in FY2025: $22,042,408, against total company
  revenue of $1,643,000 — 13.4x the revenue.** The CEO's grants are set out in her employment
  agreement and they vest on **dates**: *"(a) RSUs with a grant date value of $4,000,000, which
  will vest in one-third (1/3) increments on the first three anniversaries of the grant date;
  (b) RSUs with a grant date value of $5,000,000 [same]; and (c) RSUs with a grant date value
  of $1,000,000, which will vest in one-half (1/2) increments on the first two anniversaries."*
  **Not one tonne, not one magnet, not one dollar of cash flow appears in a vesting condition
  disclosed in the 10-K.** And the deal-completion pay is disclosed in terms: the Chief Legal
  Officer received *"additional compensation of $100,000 and $100,000 in 2024 and 2025,
  respectively, related to the **successful signing of the business combination** in 2024 and
  **successful completion of the de-spac** in 2025."* Paid for doing the deal, not for the deal
  working. **[E2-49]** is the companion — *"pre-set, long-lived and small bullseyes"* is the
  standard, and a calendar is not a bullseye.
- [x] **Promotional disclosure against filed fact — [E4-22]'s spirit, and the sharpest single
  finding at Q3.** On **2026-09-04** the company's own press release described Serra Verde as
  *"the only scaled producer of all four magnetic and other critical heavy rare earth elements
  outside Asia"* whose operation *"began production in January 2024"*. **In the same filing, at
  Exhibit 99.3, the company's accountants wrote this:** *"The $3.1 billion allocated to
  property, plant and equipment, net, is related to **development stage properties**. Upon the
  closing of the Merger, **the mine will continue to be designated as a development stage
  property**, and related development costs will continue to be capitalized until the milestones
  necessary to be considered operational are achieved … **commercial operations are expected to
  commence in 2027.**"* And the numbers in the same exhibit: **SVRE revenue of $588 thousand in
  the six months to 2026-06-30 against cost of revenue of $5,312 thousand** — a cost nine times
  the revenue — and **$2,486 thousand of revenue against $36,105 thousand of cost in FY2025**.
  **Run [E2-26]'s half-owner test on that pair.** The facts ARE both filed, on the same day, in
  the same accession, which is the candour that saves this from being a misstatement. But *"the
  business facts that we would want to know if our positions were reversed"* are in Exhibit
  99.3, and the words *"scaled producer … began production"* are in Exhibit 99.1. **The reader
  who stops at the press release is misled by a document that is accurate.**
- [ ] weak accounting — **not fired.** Stock compensation is expensed and shown on the face of
  the cash-flow statement; the fair-value losses are separately quantified at every line; the
  government equity cost is disclosed at $451.4M and $430.9M with the valuation method and the
  reason for liability classification; the pro forma is fully bridged. This is unusually
  legible reporting for a company at this stage and the run says so.
- [ ] unintelligible footnotes — **not fired.** Note 13 on the CHIPS Act awards explains the
  deferred-arrangement-cost treatment, the ticking fee, the redemption right and why the
  warrant is a liability, in plain sentences.
- [ ] filed-figure tells **[E4-30]** — **not applicable.** Reported growth cannot be
  unnaturally smooth with two annual periods and no profit; cash taxes as a share of pretax
  income is meaningless against a loss.

**[E4-52] — THE CONVERGENCE, and it is the right way to read this Q3.** Four of the five fired
flags point at one outcome: **serial issuance + targets for revenue, EBITDA and free cash flow
+ EBITDA in the narrative + pay that vests on dates + a press release that outruns the same
day's accounting**. *"extreme consequences from confluences of psychological tendencies acting
in favor of a particular outcome."* The outcome they favour is **a high share price**, which is
the machine's fuel: every asset here was bought with stock, so the stock price is not a
scoreboard, it is working capital. **[E3-50]** names the premise — managers whose job they
believe *"at all times is to encourage the highest stock price possible (a premise with which
we adamantly disagree)"* — and names the next step, *"unadmirable accounting stratagems."*
**None of those has been reached.** The system is pointed that way; the accounting is clean.
Both halves belong in the record, and **[E5-38]** is why: the flag reads the accounting, the
binary **[E5-16]** judges the person, and the two stay distinct.

### STEP 3 — THE PRIMARY TEST **[E2-01]** — and why it cannot be run

*"the achievement of a high earnings rate on equity capital employed (without undue leverage,
accounting gimmickry, etc.)"*, as a multi-year series, balance sheet before income statement:

| year end | stockholders' equity | net loss | return on equity |
|---|---|---|---|
| 2024-12-31 | $34,021k | $(16,392)k | **negative** |
| 2025-12-31 | $494,286k | $(298,524)k | **negative** |
| 2026-06-30 | $2,536,972k | $(80,031)k for the half | **negative** |
| pro forma 2026-06-30 | **$4,714,493k** | pro forma $(440,697)k FY2025 | **negative** |

**Two filed years, both negative, on an equity base that grew 139x in eighteen months.** A
series like that measures issuance, not performance. **[E2-43]**'s denominator does not repair
it either: unleveraged net tangible assets are $4,714.5M less $602.5M goodwill, $312.6M other
intangibles and $912.1M deferred arrangement costs = **$2,887.3M**, of which **$3,254.5M of
plant is development-stage** — a tangible base larger than the tangible equity and not yet
earning anything.

### The institutional imperative — score all four **[E2-30]**

- [ ] resists any change in current direction — the opposite; direction changes monthly.
- [x] **projects or acquisitions materialise to soak up available funds.** The clearest score
  in the file, and the dates are the evidence: **$1.5 billion raised 2026-01-28**; Serra Verde
  agreed **2026-04-19** and Carester **2026-04-09**, eleven and twelve weeks later; Blacksburg
  selected June 2026; TMRC agreed 2026-03-04; Hooton Park bought 2026-07-02; Serra Verde closed
  2026-09-03 for $300M of that cash and 126.8M shares. **[E2-30]** is explicit that this is
  *"institutional dynamics, not venality or stupidity"*, and the run scores it that way.
- [x] **staff studies produced to justify the leader's craving** — scored on the filed fact
  that the Pre-Feasibility and Definitive Feasibility Studies for Round Top are being produced
  *while* the capital programme they are meant to justify is already being built and funded, and
  on the $96.4 million of *"investment banking fees, legal fees, issuance costs, accounting and
  audit fees, and other related advisory costs"* recognised for the Serra Verde transaction
  alone. **[E3-58]** is the companion: allocation solved *"by either having a staff that does
  it, or by hiring consultants"* is *"a terrible mistake."*
- [x] **peer behaviour mindlessly imitated** — MP Materials signed with the Department of War in
  July 2025; Lynas signed floor-price agreements with Japan and the United States; USAR signed
  a letter of intent with the Department of Commerce in January 2026 and definitive agreements
  in June 2026. Every Western producer is executing the same government-financed template at
  the same time. **That is the [E2-27] mechanism, and it is Q4's named death.**

### Capital allocation — the buyback conditions **[E5-08, E4-31]**

Not applicable and correctly so: there are no buybacks, there is no free cash, and the Direct
Funding Agreement *"contains … **restrictions on stock buybacks and dividends for a five-year
period following the Award Date**, minimum liquidity requirements, and clawback provisions."*
**No capital-allocation flag under [E5-08] and [E2-51]** — a company consuming $184M of cash a
half-year should not be buying its own stock, and it is not. Recorded.

**But the allocation question that does bite is [E5-44], and it is the one the corpus wrote for
exactly this:** *"The intrinsic value of the shares you give in an acquisition **must not be
greater than the intrinsic value of the business you receive**."* Serra Verde was bought with
126,849,307 shares valued in the filed purchase-price allocation at **$17.85, the closing price
on 2026-09-02** — $2,264.3M of the $2,573.9M consideration. Sixteen days later the same paper
trades at **$15.37**, and the business received sold **$588 thousand of product in six
months** and remains a development-stage property on USAR's own books. *"a premium paid in
undervalued shares is larger than it looks"* — and its inverse is the risk here.

### THE GUARDRAIL

- [x] Confirmed: **nothing in this Q3 is used to promote the name.** A clean audit opinion and
  legible footnotes cannot repair Q2 or substitute for Q4 **[E2-37, E2-38, E3-39]**. *"a
  textile company that allocates capital brilliantly within its industry is a remarkable
  textile company — but not a remarkable business."*
- [x] **This business requires a great manager, and that is recorded at Q2 as a moat defect
  [E4-23]**, not here as a strength: *"if a business requires a superstar to produce great
  results, the business itself cannot be deemed great."* Building a mine-to-magnet chain on
  three continents against a 90%-share incumbent is superstar work, and the surgeon has changed
  twice.
- [x] Is the franchise intact and the damage excisable, or **is the manager the plan**
  **[E2-35, E2-36]**? **The manager is the plan.** There is no franchise to have local damage.

- **VERDICT (RECORDED, NOT GOVERNING): IN — no disqualifier found.** Not a finding that the
  managers are honest **[E5-17]**. Five flags fired and converge **[E4-52]**; three of the four
  institutional-imperative behaviours score; the accounting itself came back clean and that is
  recorded as plainly as the flags. **IN never promotes.**

---
## Q4 — WILL IT SURVIVE? — RECORDED, NOT GOVERNING

### Owner earnings — the one number **[E2-23]**

**MORE THAN ONE WINDOW — and the corpus's default window does not exist here.** **[E2-42]**
recommends *"not less than a five-year test"*; **the operating company has exactly two recast
annual periods on file (FY2024, FY2025)**, because everything before is the SPAC's. That
absence is itself the finding **[E4-25, E5-11]**.

House convention: operating cash flow less share-based compensation less the (c) guess.

| | FY2024 | FY2025 | TTM to 2026-06-30 |
|---|---|---|---|
| cash from operations | $(12,991)k | $(48,985)k | **$(106,071)k** |
| less SBC **[E5-06]** | 1,738 | 8,760 | 18,481 |
| (c) at the **D&A end** | 389 | 1,586 | 5,834 |
| (c) at the **total-capex end** | 3,107 | 37,359 | **139,450** |
| **owner earnings, D&A end** | **$(15,118)k** | **$(59,331)k** | **$(130,386)k** |
| **owner earnings, capex end** | **$(17,836)k** | **$(95,104)k** | **$(264,002)k** |

*(FY2024/FY2025 from the 10-K consolidated statement of cash flows; TTM built as FY2025 less
H1 2025 plus H1 2026 from the 10-Q. D&A at the D&A end is the sum of the statement's own lines:
depreciation, amortisation of other intangibles, amortisation of right-of-use assets.)*

- **Short-window mean** (window: FY2025 alone): **$(59,331)k to $(95,104)k**
- **Long-window mean** (window: FY2024-FY2025, the longest that exists): **$(37,225)k to
  $(56,470)k**
- **TTM sensitivity:** $(130,386)k to $(264,002)k — **worse than either annual window, and
  worsening**
- **Combined range (window spread x capex band): minus $15.1M to minus $264.0M.**
  **Every construction on every window is negative**, which is the FLNC case of 2026-09-12
  rather than the BE case: there is no sign change to date and no positive end to the band.
- **Is that range too wide to reach a conclusion [E4-25]?** It is wide — 17x from end to end —
  **but the conclusion does not depend on the width, because the sign never changes.** The
  honest statement is not *"no useful conclusion"*; it is *"there are no owner earnings, on any
  window, at either end of the capex band."*
- **A wide spread is also a Q4 finding [E5-11]. Name the distortion:** FY2025 contains a
  **de-SPAC (2025-03-13)**, a **$244.6M non-cash fair-value loss** on the May 2025 $75M
  financing, and **six weeks of an acquired subsidiary (from 2025-11-18)**; H1 2026 contains a
  **$1.5 billion equity raise**, **$51.0M of securities issuance costs**, **$27.7M of deferred
  government loan costs** and **$882.3M of stock and warrants issued to a government**. There
  is no undistorted period in the record.
- **Maintenance capex — the disclosed judgment [E2-23]'s constraint 4, *"(c) must be a
  guess."*** **The D&A end is INVALID here and the run says so, per [E5-20] and [E2-41].**
  D&A of $1.6M in FY2025 against capex of $37.4M, and $5.8M TTM against $139.5M, is not
  maintenance of anything — it is the depreciation of plant that is not yet built. **The
  judgment: (c) belongs at the total-capex end and above it**, because the business's own filed
  statement of what it needs is *"our estimated **$4.1 billion of required long-term capital
  expenditures**"*. Where the capex band would normally change a verdict, here it only changes
  how negative the answer is. **[E4-47]** reinforces it: replacement capex in current dollars
  outruns depreciation charged in old dollars, and here there is nothing to replace yet.
- **Stock compensation subtracted in full [E5-06]**, and measured beyond the charge **[E3-70]**:
  the FY2025 charge was **$8,760k** and H1 2026 **$11,003k**; the FY2025 Summary Compensation
  Table's grant-date fair values for four executives alone were **$22,042,408**, which is the
  [E3-70] direction — *the reported charge is the floor of the subtraction, not the measure.*
- **SBC AGAINST OPERATING CASH — THE CALIBRATED ROW, AND THE RATIO IS REFUSED IN WORDS.**
  The house row is ACVA 330.5% cumulative, ROKU 140.2%, CALX 98.4%, ARM 96.6%, CRWD 68.0%.
  **USAR cannot take a place in it.** Operating cash is negative in every filed period, so
  SBC-over-operating-cash is a negative number that reads as small when the truth is that
  **there is no operating cash for the pay to consume** — the same refusal the RGTI run of
  2026-09-13 wrote down. The honest denominators instead:
  **SBC was 533.2% of FY2025 revenue ($8,760k against $1,643k) and 95.5% of H1 2026 revenue
  ($11,003k against $11,519k)**; over FY2024-H1 2026 cumulative SBC of $21,501k exceeds
  cumulative revenue of $13,162k by 63%. **The company pays its people more in stock than it
  collects from customers.** Shape #2 is therefore a **feature**, not the mechanism.

### Great, good, or gruesome? **[E4-20]**

- [ ] great  [ ] good  [x] **gruesome** — *"grows rapidly, requires significant capital to
  engender the growth, and then earns little or no money."* Revenue grew from $0 to $11.5M in a
  half-year; the pro forma gross margin on it is **minus 51.2%**; the capital required is
  **$4.1 billion by the company's own statement**; and the cash earned is **minus $130M to
  minus $264M** a year. **[E4-43]**'s protection for the *good* class does not reach: there is
  no *"$82 million pre-tax on $400 million of net tangible assets"* here, there is a loss.
  *"attracted by growth when they should have been repelled by it."*

### Staying power — score all three **[E5-11]**

1. **A large and reliable stream of earnings: ABSENT.** Two annual periods, both losses; TTM
   revenue of **$13.2M** against a TTM operating cash outflow of $106.1M. Two customers were 91%
   of FY2025 revenue and one vendor 81% of raw-material purchases.
2. **Massive liquid assets: PRESENT, and this is the leg that passes.** Pro forma cash and cash
   equivalents of **$1,392,007k** at 2026-06-30 (10-Q cash of $1,530,147k, plus $162,413k of
   SVRE cash acquired, less the $300,000k cash consideration and $553k of interest
   settlement — 8-K `0001213900-26-097399` Ex. 99.3). That is **$3.75 per pro forma share**
   against a $15.37 quote.
3. **No significant near-term cash requirements: FAILS, and [E5-11] says this is the one that
   usually kills.** The filed list of near-term requirements:
   - **$4.1 billion of stated required long-term capital expenditures**;
   - a contractual obligation to *"**raise at least $600 million of additional equity by
     December 31, 2027**"* and to *"establish a **$250 million revolving credit facility by
     December 31, 2026**"* — both are **milestones for the government money itself**;
   - a **2.0% upfront loan commitment fee of $26.0 million** and *"a 2.0% annual ticking fee,
     paid quarterly, based on the unutilized LGA commitment amount"* — up to about **$26M a
     year for not drawing**;
   - the assumed **DFC loan, repayable in up to 49 sculpted quarterly instalments**, with
     financial maintenance covenants and a first lien on the Brazilian business;
   - Blacksburg, Lacq, Stillwater Phase 1b and the Round Top mine, none of which is built.

   **Burn and runway, from filed figures.** H1 2026 used **$75,324k** in operations and
   **$108,388k** in capital expenditure and equipment deposits: **$183,712k in six months, a
   $367M annual rate.** Against pro forma cash of $1,392,007k that is **about 3.8 years at the
   most recent observed rate** — and materially less at the planned rate, since the $4.1bn
   programme is **about 2.9x the cash on hand** and the company's own milestone schedule runs to March
   2028. **[E5-39]**: *"We will never be dependent on the kindness of strangers."* This company
   is designed to be: its funding plan names the strangers — the Department of Commerce, the
   Federal Financing Bank, the DFC, the State of Texas, the Department of Energy, the
   Government of France, InfraVia, and the equity market for $600M more.
- **Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this
  framework and the corpus supplies none.* Today: liabilities $2,002.2M against equity
  $4,714.5M pro forma, of which the hard money is the **$304.1M DFC loan** and a **$226.9M
  royalty liability**; committed but undrawn: **$1.30bn** under the LGA and up to **$465M**
  more under the DFC Initial Loan. **Read the terms, not just the quantity [E3-52]:** none of
  this is covenant-free customer float. It is secured, covenanted, milestone-gated, dated debt,
  and **[E2-54]**'s coverage test cannot be met from operations at all — *"all interest, both
  payable and accrued, to be comfortably met out of current cash flow net of ample capital
  expenditures"*: current cash flow is minus $106M and capital expenditure is $139M. **Zip up
  your wallet** is the corpus's instruction on that reading, and the only thing standing
  between it and this balance sheet is the $1.39bn of equity-funded cash.
- **Jurisdiction [E3-66]:** pro forma, the largest single asset is a Brazilian mine held through
  British Virgin Islands and Swiss entities, financed by a US development agency with a first
  lien over it, selling to a Swiss-contracted US government special purpose vehicle. The run
  records that a US shareholder's claim runs through four jurisdictions and behind a secured
  sovereign lender.

### NAME THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24]**

**Mechanism — and it is [E2-27] verbatim, happening on a published schedule.** *"Viewed
individually, each company's capital investment decision appeared cost-effective and rational;
viewed collectively, the decisions neutralized each other and were irrational … After each
round of investment, all the players had more money in the game and returns remained anemic."*
Between 2025 and 2028 the United States, Japan, France, Australia, Brazil and the European
Union are each funding a non-Chinese rare-earth chain, and the filings name the participants:
MP Materials' 10X Facility with a **guaranteed $140M of EBITDA** and a **$110/kg floor**;
Lynas's Mt Weld, Kalgoorlie and Malaysia expansions with a **US$110/kg JARE floor to 2038**;
Energy Fuels buying KSM Metals; Noveon and VAC already producing in the US; Carester and
InfraVia building Lacq with French state support — and **USAR building Stillwater, Blacksburg
and Lacq while targeting 10,000 tpa of domestic magnet capacity**. Every one of those decisions
is individually rational because a government is paying for it. **Collectively they are one
capacity build aimed at the same protected demand, and the protection is a contract with a
term.**

**Quantified from filed figures, and the arithmetic is the corpus's own form [E3-24]:**
- USAR's target is **10,000 tpa of NdFeB magnets and 10,000 tpa of heavy strip-cast, metal and
  alloy** (Q2 2026 earnings release), for **$4.1 billion of stated capital expenditure** —
  about **$410,000 of capital per annual tonne of magnet capacity** if the whole programme is
  ascribed to magnets, and more once Round Top and Blacksburg are separated out.
- The protected price is knowable: **US$110/kg is the floor three separate governments have
  written**, and the market moved from **US$55.0/kg to US$100.8/kg in twelve months** on those
  agreements (Lynas, ASX 2026-08-26). **So the floor sits roughly where the free market price
  now is, and above where it was fifteen months ago.**
- **The test: what happens if the floor is not renewed, or the appropriation is not made?**
  MP Materials took **minus $155.8M of operating cash in FY2025** and Energy Fuels **minus
  $89.5M** — both with plant already running — in a year when NdPr nearly doubled. Strip the
  administered price out of this industry and the filed evidence is that nobody in it earns
  cash. USAR would then own $3.25bn of development-stage plant, $602.5M of goodwill and
  **$912.1M of deferred arrangement costs whose only realisation is milestone-gated government
  funding** — and the terms say the government keeps the equity regardless: *"the government
  will retain 100% of such equity securities **whether or not the Expected U.S. Government
  Transaction is funded in full or at all**, if all or part … is not funded for any reason, or
  **if the funding is received but subsequently clawed back.**"*
- **And the second, faster mechanism, quantified.** Before any of that, the owner can be
  diluted out. The count went **60.1M → 371.6M in twenty-one months**; the company must raise
  **$600M more equity by 2027-12-31** as a condition of the funding; the DOC warrant adds
  17.6M shares at $17.17; Carester and TMRC add more. **At the current $15.37, $600M is another
  39.0 million shares, 10.5% of the pro forma count** — and that is the *contractual minimum*
  against a $4.1bn programme.

**Likelihood:** [ ] likely  [x] **a real possibility**  [ ] a low-level possibility — for the
over-build mechanism inside a decade. **The dilution mechanism is not a possibility; it is
filed, dated and contractual.**

**[E4-51], the iron prescription — the argument AGAINST this section, stated as its holders
would:** the DFARS ban is law from 2027-01-01; China has export controls and has named USAR on
a control list, which is proof the position matters; three governments have committed cash, a
price floor and a take-or-pay; Serra Verde is the only non-Asian source of all four magnetic
heavy rare earths and its Phase 1 output is 100% sold on take-or-pay; USAR holds $1.39bn of
cash and no meaningful net debt; and the world price doubled in a year. **A holder would say the
patron is not a risk but the thesis, and that this is the one commodity where the West has
decided price will not be set by the low-cost producer.** That case is coherent and it is why
the name trades at $5.7bn. **[E4-40]** is the answer the framework gives: *model exposure, not
experience.* The favourable experience is fifteen months old and was created by the same policy
that can be withdrawn; the exposure is $4.1bn of spending against a contract.

**THE SURVIVAL SHAPE — measured against `Screens/SURVIVAL SHAPES - index.md`.**
- **Mechanism: #8, THE EQUITY IS THE REVENUE** (RGTI, 2026-09-13) — *customers pay a small part
  of the costs and new shareholders pay the rest.* TTM revenue of **$13.2M** against
  TTM operating and capital cash outflows of **$245.5M** ($106.1M operating plus $139.5M capital); the gap filled by a $1.5bn
  placement, $303.8M of warrant exercises and 126.8M shares handed to a seller. Fourth instance
  after RIVN, LCID and SOUN, and the most extreme by ratio.
- **Feature: #14, THE PATRON** (GFS, 2026-09-13, proposed) — *the government that funds the
  plant sets the terms and can change them.* **And this run proposes one addition to #14 rather
  than a new shape, because the index warns against proliferation: THE PATRON WHO FLOORS THE
  PRICE ALSO CAPS IT, AND CHARGES AN ENTRY FEE IN EQUITY.** Filed in three companies at once:
  30% of the upside above $110/kg remitted to the DoW (MP), upside sharing capped at
  US$10m/annum (Lynas/JARE), *"favorable upside-sharing mechanics"* (USAR/US SIIE) — and at
  USAR **$882.3 million of stock and warrants paid as a condition precedent for $277.0M of
  funding not yet received, retained by the government whether the funding arrives or not.**
  That last clause is not in any existing shape.
- **Features also present:** #2 (earns nothing for owners after paying its people — SBC 533% of
  FY2025 revenue; the ratio to operating cash refused above); #3 (too little filed history —
  two recast annual periods, and the corpus's five-year window cannot be run); #1 (contracted
  not to stop — the milestone schedule and the ticking fee oblige spending).

- **VERDICT (RECORDED, NOT GOVERNING): OUT on the evidence read** — gruesome under **[E4-20]**,
  the third staying-power strength fails **[E5-11]**, and owner earnings are negative on every
  window at both ends of the capex band. The file had already closed at Q1.

---
⛔ **Q5 does not open: Q1 is UNKNOWABLE and Q2 and Q4 would each have closed the file.** What
follows carries the mandatory heading and no entry language.

---
## COMPUTATION — NOT A CLEARANCE
*(operator rule 3, and the queue's output contract: every run ends with a price and a
pass/fail line. **This is arithmetic, not a valuation, and it carries no entry language.**)*

**THE PRICE.** **US$15.37, close of 2026-09-18** (`tools/sources.py:price('USAR')`,
**aggregator, flagged, live quote only**).
**THE SHARE COUNT.** **371,569,406** = 244,720,099 off the 10-Q cover of 2026-08-04 plus
126,849,307 issued on 2026-09-03. **THE CAP: US$5,711M.** (On the cover count alone,
US$3,761M — the post-cover issuance moves the cap by **52%**, which is why the RGTI precedent
is in the brief.)
**THE SOVEREIGN.** **USD 5.34%**, 30-year, US Treasury, 2026-09-18.

**1. THE YIELD — negative on every construction.**

| owner-earnings construction | figure | yield on $5,711M |
|---|---|---|
| FY2024-FY2025 mean, D&A end *(invalid end, shown for completeness)* | $(37.2)M | **−0.65%** |
| FY2024-FY2025 mean, capex end | $(56.5)M | **−0.99%** |
| TTM to 2026-06-30, D&A end | $(130.4)M | **−2.28%** |
| **TTM to 2026-06-30, capex end — the honest one** | **$(264.0)M** | **−4.62%** |

Against a sovereign of **5.34%** the gap is not a spread to be argued about; it is the wrong
sign. **[E5-34]** is the applicable instruction and it was already obeyed at Q1: *"We first
have to decide whether we can sensibly estimate an earnings range for five years out, or
more … If, however, we lack the ability to estimate future earnings — which is usually the
case — we simply move on."*

**2. WHAT THE PRICE ALREADY ASSUMES.** No growth rate can be solved for from a negative base,
so the arithmetic is run the other way — **what must exist for $5,711M to be worth paying**.
Take the corpus's own floor **[E4-28]**, a 10% pre-tax expectancy, and it requires roughly
**$571M a year of owner earnings.** The business's own targets are 10,000 tpa of NdFeB magnets
and 10,000 tpa of metal and alloy. **$571M on 10,000 tonnes of magnets is about $57,000 of
owner earnings per tonne** — against a market where MP Materials sold $224M of product and
consumed $156M of cash, and where Lynas's record year produced A$222.4M of profit on 12,122
tonnes of REO with two governments underwriting the price. **What the business has actually
done: $13.2M of TTM revenue, a negative gross margin, and $245.5M of cash consumed in the last
twelve months.**
**[E4-35]**'s base rate belongs here: *"fewer than 10 of the 200 most profitable companies …
will attain 15% annual growth in earnings-per-share over the next 20 years."*

**3. WHAT YOU ARE PAID.** **Minus 4.62% against plus 5.34%: about 10 points BELOW the
sovereign** on the TTM capex-end construction. On the most generous construction in the table,
about 6 points below.

**WHAT THE BUYER IS PAYING FOR, IN WORDS.** At $15.37 a share, per pro forma share:

| | per share | share of the price |
|---|---|---|
| pro forma cash and equivalents ($1,392.0M) | **$3.75** | 24.4% |
| deferred arrangement costs ($912.1M) — the stock and warrants already given to the Department of Commerce, an asset only if milestones are met | **$2.46** | 16.0% |
| goodwill and other intangibles ($915.1M), incl. $246.7M for an offtake under which *"delivery … has not started"* | **$2.46** | 16.0% |
| property, plant, equipment and mineral interests ($3,287.0M), **almost all development-stage** | **$8.85** | 57.6% |
| other assets (receivables $6.3M, inventories $74.8M, prepaid $12.3M, other current $77.9M, equipment deposits $46.9M, right-of-use $2.2M, other non-current $0.5M = $220.9M) | **$0.59** | 3.8% |
| less total liabilities ($2,002.2M) | **$(5.39)** | (35.1)% |
| less mezzanine equity, the 12% preferred ($10.3M) | **$(0.03)** | (0.2)% |
| **= pro forma book value attributable to common ($4,714.5M)** | **$12.69** | 82.6% |
| **quoted price** | **$15.37** | 100% |

So: **a quarter of the price is cash, and essentially all the rest is plant that does not yet
produce, goodwill on a mine that does not yet produce, and a receipt for equity handed to a
government.** The business attached to it sold **$5.8 million** of metal last quarter at a gross
loss, and the largest acquisition sold **$588 thousand** in six months. **A buyer at $15.37 is
paying $5.7 billion for a construction schedule and a government's continued intention.** That
sentence is the whole computation.

**THE FLOOR [E4-28], for the record and not as a ranking:** honest pre-tax expectancy at this
price is **negative**, against roughly 10%. **The name is not ranked; it is quit on** — and it
was closed one gate earlier than that, at Q1.

---
## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL? — RECORDED, NOT GOVERNING

Nothing is bought, so there is nothing to sell. **[E1-02]** *"I believe in establishing
yardsticks prior to the act"* applies instead to the yardstick for **re-opening the file**,
which is the useful output of a Q1 UNKNOWABLE. The HHH and RGTI runs set the precedent.

**THE RE-OPEN CONDITION — three documents, each of which the company itself has dated.** When
they exist, the verdict changes from UNKNOWABLE to researchable, and a fresh v4 run is owed:
1. **The Round Top Definitive Feasibility Study.** Management's filed schedule: *"on track for
   **Q4 2026 completion and Q1 2027 publication**"* (Q2 2026 earnings release). The Company has
   no declared mineral resource until something like it exists.
2. **A definitive magnet offtake or sales agreement with a price and a volume**, replacing
   *"we do not currently have any … definitive off-take or sales agreements with customers in
   place in our magnet business"* (2026-09-15).
3. **Serra Verde reclassified from development-stage to operational** on USAR's own books —
   the company's estimate is **2027** — which is the event that turns $3.1bn of capitalised
   cost into a measurable business.

**THE THESIS-BREAKING METRIC, pre-committed, if the file ever re-opens:** **owner earnings per
share, not owner earnings.** The count is the variable management controls and has used six
times in twenty-one months; a plant that works while the count triples is not a win for the
holder. Threshold: any construction of owner earnings per pro forma diluted share that is still
negative at the point the Blacksburg and Round Top milestones are declared complete (management
schedule: March 2028) closes the file again.

**THE MONITORING QUESTION [E3-30, E4-17]:** the erosion to watch is not a cycle in the NdPr
price, it is **the durability of the administered price.** Is a change in the floor *"just part
of an aberrational cycle … or [has] the business slipped in a way that permanently reduces
intrinsic business values"*? The corpus already answered for the 1970s insurers whose regulated
pricing ended: *"That day is gone"* **[E2-59]**.

**Position size: NIL.** Not a judgment about the company; a consequence of a closed file. No
alert band is armed and no `PORTFOLIO.md` row is written, per the fold's rule 4 and the QLYS
ruling of 2026-09-07: **a name that did not clear the business gates gets a reversal condition
in words, not a price trigger.** The reversal condition is the three documents above.

- **VERDICT (RECORDED, NOT GOVERNING): UNKNOWABLE** — the exit yardstick cannot be
  pre-committed for a business whose cash flows cannot be estimated.

---
## SELF-AUDIT

- [x] Questions answered in order; no verdict skipped. Q1 closed the file; Q2, Q3, Q4 and Q6
  are each headed **RECORDED, NOT GOVERNING**, and the Q5 arithmetic carries the mandatory
  `COMPUTATION — NOT A CLEARANCE` heading with no entry language.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** The only
  gate marked IN is Q3, and it is marked RECORDED, NOT GOVERNING and stated as *no disqualifier
  found* per **[E5-17]**. Q2's class carries PROVISIONAL and Q2 is **not** marked IN.
- [x] Every UNRESEARCHED verdict names the artifact — **no gate closed as UNRESEARCHED.** Two
  *cells* are UNRESEARCHED and both are named with their rung: Lynas's cash from operations
  (ASX full financial report, not pulled) and Neo Performance Materials (SEDAR+, not pulled).
- [x] Every UNKNOWABLE verdict states what specifically cannot be known: Q1 names the
  Pre-Feasibility Study, the Definitive Feasibility Study and the absent customer contracts;
  the China competitor cell names the absence of any document on this project's shelf.
- [x] Step 0: the filing was read, with accession numbers for six documents; **FY2025 operating
  cash of $(48,985)k cross-checked three ways** and FY2025 revenue of $1,643k cross-checked
  against XBRL.
- [x] Owner earnings on a multi-year mean, **and the run states that the corpus's five-year
  window [E2-42] does not exist for this registrant**; both windows shown, capex band disclosed
  as a judgment with the D&A end declared INVALID per **[E5-20]**.
- [x] Competitor row filled: **9 peers named, 3 cells filled**, class NONE with PROVISIONAL
  recorded, the non-SEC limit stated for China and the source rule stated for Lynas.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated; the mixed
  earnings currency is disclosed at Step 0.
- [x] Value stated as a range of constructions, not a point estimate; the per-share table is
  the filed balance sheet, not a valuation.
- [x] One bar chosen — **neither**, because no bar applies below the gate. No margin of safety
  was computed and none may be. **Windage count: 0.** Conservatism was not spent, because no
  valuation was reached.
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] `python tools/check_framework.py` PASSES.
- [x] Run committed to git with a pathspec.

## REGISTER

- Verdict: [ ] IN  [ ] OUT (about the business)  [ ] UNRESEARCHED (about my diligence)
  [x] **UNKNOWABLE (about my evidence)** — at **Q1**.
- **One line:** **FAIL at Q1, UNKNOWABLE.** USA Rare Earth is a de-SPAC with two recast annual
  periods on file whose Texas deposit has **no declared mineral resource under Item 1300 of
  Regulation S-K**, whose magnet plant had **no definitive customer offtake or sales agreement
  as of 2026-09-15**, whose only revenue-producing subsidiary ran a **gross loss last quarter**,
  and whose $2.83bn Brazilian acquisition remains a **development-stage property on its own
  books** having sold **$588 thousand of product in six months**; **price US$15.37 (2026-09-18),
  pro forma cap US$5,711M** on 371,569,406 shares.
- **If UNKNOWABLE — what specifically cannot be known:** the future cash flows of the two legs
  that carry the quote. **(a)** Round Top: no declared mineral resource, the 2019 PEA withdrawn
  from reliance by the filer, the Pre-Feasibility Study unfinished and the Definitive
  Feasibility Study scheduled for Q1 2027 publication — **no document exists to be fetched.**
  **(b)** The Stillwater magnet business: no definitive customer offtake or sales agreement, so
  no filed price, volume or counterparty — **a contract that has not been signed cannot be
  retrieved.** **(c)** Serra Verde's steady-state economics: a development-stage property by
  USAR's own purchase accounting, with commercial operations expected in 2027 and an offtake
  under which *"delivery … has not started."*
- **The re-open work order (not an UNRESEARCHED verdict — these artifacts do not yet exist):**
  the Round Top DFS (management: Q1 2027), a definitive magnet sales agreement, and Serra
  Verde's reclassification to operational (management: 2027).
