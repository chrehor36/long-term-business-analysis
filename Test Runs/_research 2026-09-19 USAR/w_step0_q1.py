# -*- coding: utf-8 -*-
import io, os
os.chdir(r"C:\Users\chreh\OneDrive\Documents\BRK")
p = "Test Runs/2026-09-19 Run - USAR USA Rare Earth.md"
s = open(p, encoding="utf-8").read()

step0 = """---
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
"""

q1 = """## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

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
months to 2026-06-30 the business collected about $16.9M of revenue and **used $75.3M of
operating cash in the first half of 2026 alone** (10-Q). The gap is paid by selling shares:
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
"""

marker = """---
## STEP 0 — THE RATE, AND THE FILING"""
start = s.index(marker)
end = s.index("## Q2 — IS IT A FRANCHISE?")
s = s[:start] + step0 + q1 + s[end:]
open(p, "w", encoding="utf-8").write(s)
print("ok", len(s))
