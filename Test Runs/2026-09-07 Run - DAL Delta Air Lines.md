# Company Run — Delta Air Lines, Inc. (DAL) — 2026-09-07
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
## PRE-REGISTRATION — written before any filing was opened (operator rule 9)

The brief states its own prior: *"Q2 is where I expect this to die."* The UAL run of
2026-09-02 reached Q2 OUT on the same industry and its findings are on the shelf. **Both
facts are incentives to reach the same answer cheaply**, which is exactly what **[E4-27]**
and **[E4-26]** forbid. So, pre-registered:

1. **The prior is Q2 OUT.** It is recorded here so that it cannot be presented later as a
   discovery.
2. **The named refutation route.** Delta differs from United on one filed, quantified fact
   the UAL run itself surfaced: **Delta discloses a dollar figure for American Express
   remuneration and United has never disclosed a Chase number.** If the two-business case
   can be made anywhere in this industry it is here, and it must be built at full strength
   before it is tested **[E4-51]**.
3. **The disconfirming evidence to hunt hardest [E4-26]:** every metric on which Delta is
   the *best* carrier in the panel, stated first and in its own words, not buried.
4. **Nothing from the UAL run is inherited as a conclusion.** Peer figures are reused as
   arithmetic (they are the same filings); every Delta-specific finding is built from
   Delta's own filings. The brief's two known errors in the UAL instruction — that audited
   standalone loyalty financial statements exist, and a lease element — are treated as
   **live hypotheses to be tested on Delta, not as settled facts.**

---
## STEP 0 — THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** — the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.24** % · date **2026-09-04** · source **US Treasury daily par yield curve,
  30-year constant maturity, from the issuing authority** (`home.treasury.gov/.../daily-treasury-rates.csv/2026/all`).
  2026-09-04 is the latest published business day as of this run.
- FX: none. Delta earns in USD and quotes in USD. No ADR ratio.
- *(The `tools/sources.py` FRED-vs-Treasury defect logged by the UAL run on 2026-09-02 has
  been fixed: `SOVEREIGN_SOURCES["USD"]` now names the Treasury curve with FRED as an
  explicitly labelled fallback. Verified in this run; the Treasury path was the one used.)*

**Price** — aggregator, live quote only, flagged: **$80.17**, 2026-09-04 (Stooq via
`tools/sources.py:price`).

**Share count — read off the cover of the LATEST periodic filing, not the 10-K**
(brief correction 4): **657,623,030 shares of common stock outstanding as of 2026-06-30**,
cover page of the Form 10-Q for the quarter ended 2026-06-30, filed **2026-07-10**,
accession **0000027904-26-000031**.
**Market capitalisation = 657,623,030 × $80.17 = $52,722M.**

**The filing was read** — not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Delta Air Lines, Inc. Form 10-K for fiscal year ended
  2025-12-31, filed 2026-02-11, accession 0000027904-26-000013**, primary document
  `dal-20251231.htm`.
- **figure cross-checked against the filed statement — the whole FY2025 balance sheet was
  reconstructed line by line and it closes exactly.** Current liabilities: current debt and
  finance leases 1,605 + current operating leases 809 + air traffic liability 7,157 +
  accounts payable 5,226 + accrued salaries 4,906 + loyalty program deferred revenue 4,876 +
  fuel card obligation 1,100 + other accrued 1,945 = **27,624**, the filed total.
  Noncurrent: debt and finance leases 12,507 + noncurrent operating leases 5,353 + pension
  and postretirement 3,156 + noncurrent loyalty deferred revenue 4,386 + deferred taxes
  3,444 + other 3,994 = **32,840**, the filed total. Assets 81,317 − 27,624 − 32,840 =
  **20,853 = total stockholders' equity as filed.** Second cross-check: capital expenditures
  on the face of the cash-flow statement, flight equipment $(3,521)M + ground property and
  equipment $(978)M = **$(4,499)M**, matches the `PaymentsToAcquireProductiveAssets` XBRL
  fact used in the owner-earnings arithmetic and the MD&A's "$4.5 billion".
  Third cross-check: MD&A liquidity "$7.4 billion in cash, cash equivalents, short-term
  investments and aggregate principal amount committed and available to be drawn under our
  revolving credit facilities" = balance-sheet cash **$4,310M** + undrawn revolvers
  **$3.1bn** (Note 6). Agrees — **and the composition is a Q4 finding, recorded there.**

**Also read:** Delta 10-K for FY2019 (accession 0000027904-20-000004), FY2021
(0000027904-22-000003) and FY2023 (0000027904-24-000003) for the operating-statistics series;
the Form 10-Q for the quarter ended 2026-06-30 (0000027904-26-000031) for the share count;
and the Form 8-K of **2020-09-14, accession 0001193125-20-244688**, Exhibits 99.1 and 99.2,
for the SkyMiles financing — the only standalone SkyMiles figures that exist anywhere on
EDGAR. Working papers: `Test Runs/_research 2026-09-07 DAL/`.

---
## Q1 — CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**

**Unit economics in my own words, no management language.** Delta buys aeroplanes, hires
pilots and flight attendants, buys jet fuel, and rents counters and gates. It then
manufactures a product that is destroyed at the moment of departure — a seat on a particular
aircraft at a particular time — and must sell it before the door closes or it is worth
nothing, permanently. In 2025 it manufactured **298,045 million available seat miles** and
sold **249,578 million** of them (an **84%** load factor) at **17.37 cents** of passenger
revenue per available seat mile against **19.31 cents** of total operating cost per available
seat mile. Those two numbers are not directly comparable, because Delta owns an oil refinery
whose third-party sales sit in revenue and whose costs sit in expense; on Delta's own
refinery-adjusted basis, revenue per seat mile was **19.56 cents**. Either way the whole of
the business is the **1.95 cents per seat mile** ($5,822M ÷ 298,045m ASMs) that separates
them, which is **9.2% of revenue**.

Three revenue streams, all filed (Note 2): **passenger $51,768M** (of which tickets $45,488M,
loyalty travel awards $4,237M, travel-related services $2,043M), **cargo $900M**, and
**other $10,696M** (refinery sales to third parties $5,077M, loyalty program $3,362M,
ancillary businesses including the MRO shop $937M, miscellaneous $1,320M). Three costs
dominate and Delta controls none of them: **labour** ($17,520M of salaries plus $1,337M of
profit sharing, 29.7% of revenue, ~103,000 full-time equivalents, all major workgroups except
flight attendants under Railway Labor Act contracts), **fuel** (4,269 million gallons at
$2.30, $9,819M — and 4,269 × $2.30 = $9,819M exactly, which is the fourth cross-check), and
**airport and government charges** ($3,564M of landing fees and rents).

**A second business is consolidated inside the first and it must be named at Q1 rather than
discovered at Q2.** Delta sells its loyalty currency for cash to third parties: **total cash
sales from marketing agreements were $8.0 billion in 2025**, and **remuneration from American
Express totalled $8.2 billion**, which Delta expects "to grow to $10 billion over the next
few years." That is 12.9% of total revenue arriving from one investment-grade counterparty.
The accounting splits it: the part attributed to future award travel is deferred (the
loyalty-program deferred revenue balance is **$9,262M** and rose $436M in 2025) and emerges
in *passenger* revenue when the member flies; only the part attributed to brand and other
non-travel obligations — **$3,362M** — is recognised as loyalty revenue outside passenger
revenue. Whether this is one business or two is the whole of Q2 and it is settled there,
not here.

**The scarce input this business controls.** Not aircraft: Airbus and Boeing sell to anyone
with money, and Delta's own order book is 256 airframes deep. The genuinely scarce, controlled
inputs are (a) **slots, gates and route authorities at capacity-constrained airports** —
Delta's balance sheet carries **$5.9 billion of indefinite-lived intangibles** which are
exactly "routes, slots, the Delta tradename and assets related to alliances," the two named
sub-buckets being Pacific route authorities plus Heathrow slots, and LaGuardia plus Reagan
National domestic slots; the FAA slot-controls only three US airports and Delta is the
largest operator at two of them — and (b) the **SkyMiles member base and the American Express
contract**, which is pledged: $4,010M of Delta's debt is secured on the SkyMiles programme at
2025-12-31 and the financing agreements "restrict our ability to … change the policies and
procedures of the SkyMiles program."

**Will the fundamentals look broadly the same in ten years?** Yes, and **[E3-31]** asks for
"relatively simple and stable in character," which this is on both counts. Capacity is added
in indivisible 200-seat lumps with a 25-year life and a five-to-nine-year order lead time;
the product is perishable; the cost base is 30% labour and 17% fuel. That mechanism has not
changed in fifty years and nothing in the filing suggests it will. **The corpus's hostility
to airlines is a statement about the returns the mechanism produces, not about whether the
mechanism is legible.** That belongs at Q2 and Q4 and is not permitted to pre-empt Q1
**[E4-26]**.

**VERDICT: [x] IN**

*One caution recorded against my own verdict, per **[E4-51]**: understanding the mechanism is
not the same as being able to estimate the earnings five years out, which is what **[E5-34]**
actually asks for. Fuel price and the demand cycle are exogenous and neither is forecastable.
That distinction is carried forward and settled at Q4 and Q5, not dissolved here.*

---

## Q2 — IS IT A FRANCHISE? **[E3-03]**

**The prior was pre-registered at the head of this file: Q2 OUT. Everything below is filed.
Where a finding runs AGAINST that prior it is stated first and at full strength [E4-26], and
the case for the name is built before it is tested [E4-51].**

### THE STRONGEST CASE FOR THE NAME, STATED FIRST AND AT FULL STRENGTH **[E4-51]**

**1. Delta is the best operator in this industry on every filed metric, in every year, by a
wide margin.** From the six-carrier row built for the UAL run of 2026-09-02 and reused here
because it is the same filings, same window, same tags
(`Test Runs/_research 2026-09-02 UAL/competitor_row.md`):

| Return on **unleveraged net tangible operating assets**, % | 2017 | 2018 | 2019 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|
| **DAL** | **30.3** | **18.9** | **22.4** | **17.6** | **18.3** | **16.1** |
| UAL | 18.6 | 12.6 | 15.7 | 13.1 | 15.4 | 13.1 |
| AAL | 14.8 | 7.3 | 8.5 | 9.4 | 8.5 | 4.9 |
| LUV | 24.4 | 23.1 | 23.1 | 1.9 | 2.4 | 3.0 |
| ALK | 25.9 | 12.5 | 15.8 | 5.8 | 6.9 | 3.4 |
| JBLU | 13.6 | 3.3 | 9.8 | (2.6) | (7.2) | (3.5) |

**Delta is first of six in every single year in the window.** On return on total invested
capital including what was paid for it (operating income ÷ (all debt and leases + equity)) it
is also first in every year: **20.3% in 2019 and 14.2% in 2025**, against UAL's 13.4% and
10.2%. **[E3-46]** asks the second question about the business as a number — *"the best
businesses, by definition, are going to be businesses that earn very high returns on capital
employed over time"* — and 16.1% pre-tax on unleveraged net tangible operating assets sits
above **[E5-40]**'s ~12% "quite satisfactory" mark and inside the range **[E4-43]** uses to
say the *good* class **passes**. A persistent decade-long return gap of 3 to 12 points over
carriers flying the same aircraft on the same routes is not noise.

**2. The loyalty stream is real, large, disclosed in dollars, contracted, and it compounded
through the worst shock the industry has ever had.** Filed, from Note 2 of successive 10-Ks
and from the SkyMiles investor presentation:

| | 2017 | 2018 | 2019 | **2020** | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Total cash sales from marketing agreements ($bn) | 3.2 | 3.5 | 4.2 | **2.9** | 4.1 | 5.7 | 6.9 | 7.4 | **8.0** |
| Remuneration from American Express ($bn) | | | **4.1** | | | | 6.8 | 7.4 | **8.2** |

**In 2020, Delta's passenger revenue fell 70% and loyalty cash sales fell 31%.** Delta expects
Amex remuneration "to grow to $10 billion over the next few years." Amex remuneration was
**$2.0 billion in 2014** (SkyMiles presentation, Ex. 99.1 to the 8-K of 2020-09-14): the
stream has quadrupled in eleven years, a nominal CAGR of **13.6%**, under a co-brand contract
*"extend[ed] to 2029"* signed in 2019. The loyalty deferred-revenue balance is **$9,262M** and
rose again in 2025 — customer-prepaid, non-interest-bearing, undated money, which is precisely
the *"benefit of debt … with none of its drawbacks"* class of **[E3-52]**.

**3. And Delta discloses it, which United does not.** **[E2-26]** asks what I would want to
know if the positions were reversed. Delta prints the Amex dollar figure in Item 1, in the
MD&A and in the notes, every year. United has never disclosed a Chase dollar amount in any
filing. On this one disclosure Delta is the best filer in the industry.

**That case is serious and none of it is withdrawn below. It fails anyway, and here is why —
from the same documents.**

### THE TWO-BUSINESS TEST, RUN AS INSTRUCTED, AND IT RETURNS ONE BUSINESS

**(a) THE BRIEF'S PREMISE WAS TESTED RATHER THAN INHERITED, AND IT HOLDS FOR DELTA TOO: NO
AUDITED STANDALONE LOYALTY FINANCIAL STATEMENTS EXIST.** The instruction was *"do not assume
Delta is different; verify."* Verified, three ways:
- The only standalone SkyMiles figures anywhere on EDGAR are in **Exhibit 99.1 to the Form
  8-K of 2020-09-14, accession 0001193125-20-244688** — an investor presentation for a Rule
  144A offering. Its own disclaimer reads: *"**Pro forma financial information included in
  this Presentation is provided for informational purposes only, has not been prepared in
  accordance with the standards for such information established by the U.S. Securities and
  Exchange Commission** and may not be an indication of the financial condition or results of
  operations of Sky Miles IP Ltd. in the future."* The summary financial page is footnoted
  *"Amounts represent SMHL **Unaudited** Pro Forma Consolidated Financial Information."*
- The structure being described **did not exist when the numbers were struck**. The cash-flow
  mechanics page is labelled *"To be created"*, and every cash-sales figure is *"pro forma for
  sale of miles to Delta that would have occurred **had the structure been in place** in
  2019."*
- **SkyMiles IP Ltd. is not an EDGAR registrant.** It is *"a newly formed Cayman Islands
  exempted company … an indirect wholly-owned subsidiary of Delta"* (Ex. 99.2, same 8-K). An
  EDGAR company-name search for "SkyMiles" returns an empty result set. There is no filer, so
  there is no audit report, so there is nothing to read. **The brief's warning was correct and
  it generalises: no US airline has ever published audited standalone loyalty financials.**

**(b) A SkyMiles mile is a claim on a Delta seat, and Delta's own number is 97%.** From the
same presentation: *"In 2019, **97% of redemptions were on Delta**, allowing the flexibility
to manage costs by modifying inventory levels and value."* The FY2025 10-K puts the current
figure on the other side of the same transaction: *"In 2025, **12% of revenue miles flown on
Delta were from award travel**, as program members redeemed miles … for approximately 35
million award tickets."* One aeroplane seat in eight is already spoken for by the currency.

**(c) Most of the Amex money is a pre-sale of seats, and Delta's own revenue policy says so.**
Of $8.0bn of cash sales in 2025, only **$3,362M** is recognised as loyalty revenue outside
passenger revenue — the part allocated to *"brand value (using estimated royalties generated
from the use of our brand)"* and other non-travel obligations. The rest is deferred as award
travel and emerges in **passenger** revenue when the member flies. **58% of the "high-margin
loyalty business" is, on the filer's own allocation, deferred airline revenue.**

**(d) The margin is an intercompany transfer price.** The presentation states the mechanism:
*"Delta pays SMIP for each mile earned by Members"*, *"SMIP purchases seats from Delta"*, and
a *"Perpetual operating agreement from closing."* Both sides of the spread are prices Delta
set with itself, for the purpose of a financing. **Delta reports two segments — airline and
refinery — and SkyMiles is inside the airline segment.** There is no filed loyalty P&L, and
segment capital expenditure is disclosed for the refinery ($68M) and not for the programme.
The two-business method requires two businesses that transact with the outside world; here
the refinery does and the loyalty programme does not.

**(e) The collateral is already pledged, and it is covenanted.** At 2025-12-31 Delta still
owes **$3,422M of SkyMiles Notes and $588M under the SkyMiles Term Loan** — $4,010M secured
on the programme. The FY2025 risk factors: the SkyMiles financing agreements *"restrict our
ability to, among other things, **change the policies and procedures of the SkyMiles program
in a manner that would reasonably be expected to materially impair repayment of our SkyMiles
debt**,"* and impose a **$2.0 billion minimum-liquidity covenant** and a **$550 million
aggregate limit on the sale of pre-paid miles** (Note 6). A business whose product policy is
contractually constrained by its own lenders is a collateral package inside an airline, not a
separable franchise. *(This is the one place Delta is structurally **behind** United, which
redeemed its MileagePlus notes on 2025-07-07 and released the collateral entirely.)*

**(f) Close substitutes are four deep and the contract has an expiry.** AAdvantage with Citi
and Barclays; MileagePlus with Chase; Rapid Rewards with Chase; and American Express
Membership Rewards itself, whose points transfer into several competing programmes. The Amex
agreement was *"extend[ed] to 2029"* — it has a term, which means it is re-tendered.
**[E5-28]** scopes the claim: *"If you name some business that has incredible pricing power,
you're talking about a business that's a monopoly or a near monopoly."* SkyMiles is one of
three or four US co-brand currencies. The class does not apply.

### AND THEN THE ARITHMETIC THAT SETTLES IT — **[E3-62]**'s SECOND STEP

The bull case is that a franchise is bolted to a non-franchise. Test it by asking where the
money went. Between 2019 and 2025, deflating by CPI-U to 2025 dollars:

| | 2019, real 2025$ | 2025 | change |
|---|---:|---:|---:|
| Remuneration from American Express | **$5,163M** | **$8,200M** | **+$3,037M** |
| Total cash sales from marketing agreements | $5,289M | $8,000M | +$2,711M |
| **Consolidated real operating income** | **$8,334M** | **$5,822M** | **−$2,512M** |

**The loyalty stream added roughly $3.0 billion of real annual cash and consolidated real
operating income fell by $2.5 billion.** Every dollar of the franchise-like business was
consumed by the non-franchise business, and then $2.5 billion more. That is **[E3-62]**
exactly — *"how much is going to stay home and how much is just going to flow through to the
customer"* — answered from the filings for the one asset in this industry that looks like a
moat. **Nothing stuck to the ribs as owners.** A franchise whose entire gain is absorbed by
the business it is attached to is not separable, because the attachment is what consumes it.

### THE **[E4-55]** UNITS SERIES — ELEVEN YEARS, NOMINAL AND CPI-DEFLATED

Full working, provenance and caveats: `Test Runs/_research 2026-09-07 DAL/units_series.md`.
Sources: the operating-statistics tables of the DAL 10-Ks for FY2019 (0000027904-20-000004),
FY2021 (0000027904-22-000003), FY2023 (0000027904-24-000003) and FY2025
(0000027904-26-000013); overlapping years agree with no restatement. Deflator: BLS
**CUUR0000SA0** M13 annual averages.

| Year | ASMs (m) | LF % | PRASM nom | **PRASM real** | TRASM adj real | **CASM real** | CASM-Ex real |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2015 | 246,764 | 84.9 | 14.10 | **19.15** | n/d | **18.11** | n/d |
| 2017 | 254,325 | 85.6 | 14.53 | **19.08** | n/d | **18.16** | n/d |
| 2019 | 275,379 | 86.3 | 15.35 | **19.33** | **21.37** | **18.47** | **13.70** |
| 2020 | 134,339 | 55.0 | 9.59 | 11.93 | 14.77 | 27.38 | 19.42 |
| 2021 | 194,474 | 69.0 | 11.58 | 13.76 | 16.29 | 17.11 | 14.40 |
| 2022 | 233,226 | 84.0 | 17.24 | **18.97** | **21.51** | **22.13** | **14.16** |
| 2023 | 272,033 | 85.0 | 17.98 | **19.00** | **21.24** | **20.40** | **13.92** |
| 2024 | 288,394 | 85.0 | 17.65 | **18.11** | **20.28** | **19.81** | **13.90** |
| 2025 | 298,045 | 84.0 | 17.37 | **17.37** | **19.56** | **19.31** | **13.86** |

*(A defect in the UAL research file is corrected here and logged at the foot of this run:
that file recorded Delta's adjusted TRASM and CASM-Ex as undisclosed for 2019. They are
disclosed — in the FY2021 10-K's 2019 comparative column, at 16.97c and 10.88c. The
refinery-adjusted price series is therefore computable across the whole window and is used
above.)*

**THE TEST REPLICATES AND IT IS HARSHER ON DELTA THAN IT WAS ON UNITED.**
- **Real PRASM 2019 → 2025: −10.1%** (nominal +13.2%). Against 2017: **−9.0%**.
- **Real TRASM on Delta's own refinery-adjusted basis: −8.5%.** Real yield: **−7.4%**.
- **Three consecutive real PRASM declines** in the clean recovery years: 19.00 → 18.11 →
  17.37 (−4.7%, −4.1%).
- **Load factor 86.3% in 2019 to 84.0% in 2025 — down 2.3 points.** ASMs +8.2%, RPMs +5.0%.
  The aeroplanes are bigger and emptier.
- **AND THE COST SIDE WENT THE WRONG WAY TOO. Real CASM ROSE 4.5%** (18.47 → 19.31) and
  **real CASM-Ex rose 1.2%** (13.70 → 13.86).

**That last line is the single most important difference between Delta and United, and it cuts
against Delta.** United's real CASM *fell* 3.7% while its real PRASM fell 6.2% — it took cost
out and gave more than all of it away. **Delta's real cost per seat mile went UP 4.5% while
its real price per seat mile went DOWN 10.1%.** It did not have cost savings to give away; it
gave away price it did not have. On the [E4-55] instrument — *"the physical series is the
honest one"* — Delta's record is worse than that of the carrier this framework has already
rejected, on a company that is simultaneously the best operator in the industry. **Both facts
are true, and holding them together is exactly what [E2-58] describes: in a
persistent-over-capacity business without administered prices, long-term profitability is set
by the ratio of supply-tight to supply-ample years, and being least badly injured is not a
moat.**

### **[E2-44]** — THE TWO-CHARACTERISTIC TEST, BOTH HALVES, BOTH FAIL

**Half one: can it raise prices "even when product demand is flat and capacity is not fully
utilized"?** Capacity is demonstrably not fully utilised — **16% of the seats Delta flew in
2025 went out empty**. Its answer, from the FY2025 MD&A regional table, year on year:

| 2025 vs 2024 | Domestic | Atlantic | Latin America | Pacific | **Total** |
|---|---|---|---|---|---|
| ASMs (capacity) | +3% | +3% | +1% | +9% | **+3%** |
| Passenger mile yield | +2% | −1% | 0% | −5% | **0%** |
| **PRASM** | **−2%** | **−2%** | **−1%** | **0%** | **−2%** |
| Load factor (points) | −3 | −1 | −1 | +4 | **−2** |

**PRASM fell or was flat in all four geographic regions**, in a year of +3% capacity. Delta's
own explanation, in the first MD&A paragraph on revenue: a decline in main cabin revenue *"due
to **industry-wide supply exceeding demand** for main cabin travel in the uncertain economic
environment."* **That is [E2-58] written by the issuer.** Half one fails on the filed table.

**Half two: can it "grow dollar volume with only minor additional investment of capital"?**
Capital expenditure, filed cash-flow statements, FY2017 through FY2025:
3,891 + 5,168 + 4,936 + 1,899 + 3,247 + 6,366 + 5,323 + 5,140 + 4,499 = **$40,469 million**,
against 2025 real operating income **23.8% below** the 2017-2019 real mean. Firm aircraft
purchase commitments still outstanding at 2025-12-31: **$15.4 billion**, plus $6.0 billion of
contract-carrier minimum obligations, plus $11.2 billion of other purchase obligations, plus
**two aircraft orders signed in the six weeks after the balance-sheet date** — 30 Boeing
787-10 on 2026-01-12 and 16 Airbus A330-900 plus 15 A350-900 on 2026-01-27 — for which **no
dollar amount is disclosed anywhere in the filing.** Half two fails.

**And [E4-37], the inverse metric** — *"you can almost measure the strength of a business over
time by the agony they go through in determining whether a price increase can be sustained …
it's not a great business when you have to have a prayer session before you raise your prices
a penny."* Delta does not have to be inferred into the agony class; it files it in the first
person: *"**At times in the past, we often were not able to increase our fares to offset fully
the effect of increases in fuel costs, and we may not be able to do so in the future.**"*

### CRITERION BY CRITERION **[E3-03]**

- **Needed or desired [x] — passes.** Air travel between distant points has no substitute at
  all for most journeys, and Delta sold 249.6 billion revenue passenger miles of it.
- **No close substitute [ ] — FAILS, and the registrant names the substitutes.** FY2025 10-K
  Item 1A: *"The airline industry is **highly competitive**, marked by significant competition
  with respect to routes, fares, schedules … Our domestic operations are subject to
  significant competition from traditional network carriers, including **American Airlines and
  United Airlines**, national point-to-point carriers, including **Alaska Airlines, JetBlue
  Airways and Southwest Airlines**, and other discount or ultra-low-cost carriers, including
  **Allegiant Air, Frontier Airlines and Spirit Airlines**."* And Item 1: *"the industry is
  characterized by **significant price competition**."* The registrant even names the
  non-airline substitute: *"we compete to a lesser extent with surface transportation and
  technological alternatives such as **virtual meetings, teleconferencing or
  videoconferencing**."* **Eight named airline competitors and a named technological
  substitute, in the filer's own words.**
- **Not price-regulated [x] — passes.** *"Airlines set ticket prices in all domestic and most
  international city-pairs with minimal governmental regulation."* Note **[E2-59]**: the
  pre-1978 regime *did* administer airline prices and floored the industry's profits;
  *"That day is gone"* is exactly how that row says such a regime ends. **The absence of price
  regulation is not a moat.**

**Two of three. [E3-03] is conjunctive. Criterion (2) is the one that fails.**

### **[E3-33] / [E5-28]** — UNTAPPED PRICING POWER

**No, and the 2025 filing is a live experiment.** The test asks whether a manager could raise
the return enormously simply by raising prices, and has not. Delta added 3% capacity and its
unit revenue fell in every region. There is one place where Delta *does* hold a unilateral
price lever — the redemption value of a mile, which the SkyMiles presentation describes as a
*"**Dynamic pricing model** adjust[ing] the redemption value of miles based on demand strength
or weakness"* — and that is recorded here as the strongest surviving pricing-power argument
in this file. It is bounded three ways: by the lenders' covenant on programme policy, by four
substitute currencies, and by the arithmetic above, in which the entire loyalty gain was
already consumed. **[E5-28]** requires near-monopoly for the class and the competitor row
shows a five-way oligopoly. **The class does not apply.**

### **[E4-36]** — WHICH OF THE FOUR CAUSES OF EXTREME SUCCESS IS THIS?

Delta's outperformance is real and it is **an extreme max/min on one or two variables** —
operational reliability and premium-cabin mix — sitting on top of a **wave** **[E3-51]**. The
wave is nameable and filed: **jet fuel fell from $3.36 a gallon in 2022 to $2.30 in 2025.** At
4,269 million gallons that fall is worth **$4,525 million a year**, which is **78% of 2025
operating income**, and it is a commodity price, not an achievement. *"When a surfer gets up
and catches the wave … he can go a long, long time. But if he gets off the wave, he becomes
mired in shallows."* **A surfing run is not a moat.** What is left after the wave is the
operational max/min, and the honest measure of it is the *gap* over UAL — 16.1% against 13.1%
in 2025 — not the level.

### **[E2-53]** — THE DOMINANCE CLASS, TESTED ON ITS STRONGEST FORM AND REFUTED

*"Once dominant, the newspaper itself, not the marketplace, determines just how good or how
bad the paper will be. **Good or bad, it will prosper.**"* Delta is dominant by any measure
available: the largest US carrier by revenue, the most profitable in the industry in every
year of the window, holder of $5.9 billion of slot, route and tradename intangibles. In 2025
that dominance delivered capacity **+3.2%**, revenue **+2.8%**, and operating income
**−2.9%**, with unit revenue down in every region. **The marketplace determined how good the
year was, not the airline**, and Delta's own MD&A says so in the words *"industry-wide supply
exceeding demand."* **[E2-53] is refuted on this name by its own strongest form.**

### **[E4-04] / [E5-23]** — MUST THE MOAT BE CONTINUOUSLY REBUILT?

**Yes, and it is the excluded class, not the defended one.** The framework's test is *does the
spending defend the same advantage, or buy its replacement?* Item 2 Properties: **989 mainline
aircraft, average age 14.8 years**, plus 325 regional aircraft. Read the age profile rather
than the average:

| Fleet type | count | avg age |
|---|---:|---:|
| A320-200 | 46 | 29.0 |
| B-767-300ER | 37 | 29.0 |
| B-757-200 | 76 | 27.1 |
| B-767-400ER | 21 | 25.0 |
| B-717-200 | 80 | 24.3 |
| B-737-800 | 77 | 24.3 |
| A319-100 | 57 | 23.8 |
| B-757-300 | 16 | 22.9 |
| A330-200 | 11 | 20.8 |
| **subtotal, 20 years and older** | **421** | |

**421 of 989 mainline aircraft — 42.6% of the fleet — are twenty years old or more, and 180 of
them are twenty-five or more.** The firm order book is 256 airframes. A 25-year-old aeroplane
is a depleting asset and the $15.4 billion of commitments **buys its replacement**: it is
Mitsui's Rhodes Ridge, not Coca-Cola's advertising. A lapse in this spending does not narrow
the structure, it destroys it, because the fleet ages out. **This is also the single most
important input to (c) at Q4 and it is carried forward there.**

### THE COMPETITOR ROW — required **[E3-28]**

**Peers named: 5 of the industry's 5 remaining scale US competitors.** United, American,
Southwest, Alaska and JetBlue. Spirit is excluded and the exclusion is itself a finding: it
filed Chapter 11 twice inside 2024-2025 and is no longer a comparable going concern. **Buffett
says eight; the US industry no longer has eight.** All six filers have 31 December year ends,
so the window is identical with no alignment adjustment. Full tag-by-tag working:
`Test Runs/_research 2026-09-02 UAL/competitor_row.md` — reused rather than rebuilt, per the
brief, because it is the same filings and the same window.

**OPERATING MARGIN, `OperatingIncomeLoss` ÷ total operating revenue, both as filed** (%):

| FY | **DAL** | UAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| 2017 | **14.5** | 9.6 | 9.9 | 16.1 | 15.3 | 13.9 |
| 2018 | **11.8** | 7.8 | 6.0 | 14.6 | 7.8 | 3.5 |
| 2019 | **14.1** | 9.9 | 6.7 | 13.2 | 12.1 | 9.9 |
| 2020 | **(72.9)** | (41.4) | (60.1) | (42.2) | (49.8) | (58.0) |
| 2021 | **6.3** | (4.1) | (3.5) | 10.9 | 11.1 | (1.3) |
| 2022 | **7.2** | 5.2 | 3.3 | 4.3 | 0.7 | (3.3) |
| 2023 | **9.5** | 7.8 | 5.7 | 0.9 | 3.8 | (2.4) |
| 2024 | **9.7** | 8.9 | 4.8 | 1.2 | 4.9 | (7.4) |
| **2025** | **9.2** | **8.0** | **2.7** | **1.5** | **2.1** | **(4.1)** |

**BALANCE SHEET, 2025-12-31** (US$m; debt is the face-of-balance-sheet combined debt-and-
finance-lease lines plus both operating-lease lines, identically defined for all six):

| | **DAL** | UAL | AAL | LUV | ALK | JBLU |
|---|---:|---:|---:|---:|---:|---:|
| Total debt incl. all leases | **20,274** | 31,036 | 35,970 | 5,981 | 6,893 | 9,416 |
| Cash + short-term investments | **4,310** | 12,240 | 5,836 | 3,231 | 2,123 | 2,159 |
| **Net debt** | **15,964** | 18,796 | 30,134 | 2,750 | 4,770 | 7,257 |
| Stockholders' equity | **20,853** | 15,282 | **(3,727)** | 7,981 | 4,118 | 2,120 |
| Debt / (debt + equity) % | **49.3** | 67.0 | *deficit* | 42.8 | 62.6 | 81.6 |

**REAL PRASM, 2019 to 2025, 2025 cents, same CPI-U deflator, all filing-sourced:**

| | 2019 | 2025 | change |
|---|---:|---:|---:|
| UAL | 17.50 | 16.18 | **−7.6%** |
| **DAL** | **19.33** | **17.37** | **−10.1%** |
| AAL | 18.56 | 16.58 | −10.7% |
| LUV | 16.64 | 14.18 | −14.8% |

*(Alaska does not disclose consolidated PRASM before 2024.)*

**LOYALTY DISCLOSURE — a row the UAL run could not build and this one can:**

| | dollar co-brand figure disclosed? | standalone loyalty financials? | loyalty collateral outstanding at 2025-12-31 |
|---|---|---|---|
| **DAL** | **yes, every year — $8.2bn (2025)** | no — unaudited pro-forma 8-K exhibit only | **$4,010M still secured** |
| UAL | **never, in any filing** | no — pro-forma lender presentation only | nil, redeemed 2025-07-07 |
| AAL | no dollar figure | no — pro-forma lender presentation only | $6,842M, plus a new $1.0bn term loan in 2025 |

**WHAT THE ROW SHOWS, AND IT CUTS BOTH WAYS.**

*For Delta:* it is **first of six on operating margin in every year since 2019**, first of six
on both return metrics in **every year in the window**, it carries the **lowest leverage of the
three network carriers** (49.3% against UAL's 67.0% and American's deficit), it is the only US
network carrier with an **investment-grade rating** (Moody's Baa2, upgraded February 2025),
and it is the only one that discloses its co-brand economics in dollars. **Delta is the best
business in this industry and it is not close.**

*Against Delta:* **every one of the six earned a lower operating margin in 2025 than in 2017,
and a lower return on unleveraged net tangible operating assets in 2025 than in 2019, without
exception.** Delta's own return fell 30.3% (2017) → 22.4% (2019) → **16.1%** (2025).
**[E4-32]** says *direction outranks existence* and calls the moat widened every year *"the
primary criterion of a great business."* **Delta's direction is down in every year of the
window.** That is **[E3-28]**'s purpose discharged: a moat is a claim about relative position,
and relative position here is "least badly injured over a period when everyone was injured."

**And [E3-61]'s limit on the row is recorded rather than ignored:** *"In some businesses, the
participants behave like a demented Kellogg … I think you'd have to know the people
involved."* The row shows position; it cannot show conduct. If the four surviving scale
carriers permanently restrained capacity, the economics could change — that is the one path by
which this verdict is wrong, and it is written into Q6's reopening condition below. What the
filings show is the opposite: **Delta added 3.2% of capacity into a market its own MD&A calls
over-supplied.**

- **Untapped pricing power** — could a manager raise the return simply by raising prices, and
  has not? **[E3-33]** **No.** See above; the 2025 regional table is a live experiment and it
  went the other way in all four regions.
- **Class: [x] NONE** · **Direction: NARROWING.** Real unit revenue down 10.1% since 2019 on
  Delta's own filed series; real unit cost up 4.5%; return on unleveraged net tangible
  operating assets down in every year of the window.
- **VERDICT: [x] OUT**

**Why OUT and not UNRESEARCHED or UNKNOWABLE.** The separating question **[E4-19]** is *"can I
name the document that would resolve this?"* There is no missing document. The registrant
states the price competition and names eight competitors in its own risk factors; the
eleven-year physical series is filed and CPI-deflated on Delta's own refinery-adjusted basis;
the capital consumed is filed; and the two-business case was built at full strength from
Delta's own 8-K and returns one business. **The evidence is here and the business fails
criterion (2) of [E3-03].** That is the definition of OUT.

**⛔ THE FILE CLOSES HERE. Q3, Q4 and Q5 are recorded below as COMPUTATION ONLY, under the
heading operator rule 3 requires, because the run's output contract demands a price. They
carry no entry language and no clearance.**

## Q3 — ARE THEY HONEST, AND ARE THEY RATIONAL?

> **COMPUTATION — NOT A CLEARANCE.** The file closed at Q2. Operator rule 2 forbids treating
> anything below as a pass. It is recorded because the work was done and because a Q3 finding
> on a name the framework has rejected is still evidence about the framework.
> **[E4-19]'s "out" box is permanent; nothing here reopens it.**

### STEP 1 — THE WEIGHT CASE. Declared before anything else is read.

- [x] **Daily execution [E3-38, E2-70]** — an airline is the paradigm case. Delta carried
      *"over 200 million customers"* in 2025 to *"more than 300 destinations on six
      continents"* with 989 mainline and 325 regional aircraft and ~103,000 full-time
      equivalents, selling a product that is destroyed at the moment of departure if unsold.
      The 1977 root **[E2-70]** — an undifferentiated product magnifies the manager — applies
      exactly, and the competitor row is the proof: Delta earned a 9.2% operating margin in
      2025 and American earned 2.7% on the same routes with the same aircraft in the same
      year.
- [ ] **Control [E1-16]** — no. A minority public holding, exitable daily.
- [x] **Leverage [E3-29]** — $20,274M of debt and lease obligations against $20,853M of equity
      and $81,317M of assets. Equity is 25.6% of assets, and a 10% write-down of property and
      equipment ($39,743M) removes **19.1% of the equity**. *"Small asset errors destroy
      equity"* is satisfied, though **less severely than for any other US network carrier** —
      the same test removes 30% of United's equity and American has none to remove.

**Two of three ticked. Q3 is therefore a BINARY GATE, not an overlay, and no price
compensates [E1-16, E3-29, E5-35].** Stated because a run that does not declare its weight
case has not done Q3 — and because it means a cheap price could not have rescued this name
even had Q2 passed.

### HONESTY — binary, filings-based, dated to when each matter became PUBLIC **[E5-16]**

**No integrity disqualifier found.** Stated in the form the framework requires: *"A Q3 pass is
the absence of found disqualifiers, not a finding that the managers are honest"* **[E5-17]**.
- No restatement in the eleven years read. ICFR reported **effective at 2025-12-31**; auditor
  **Ernst & Young LLP, auditor since 2006**, which also audited internal control; **Item 9
  (changes in and disagreements with accountants): "None."**
- **Capacity antitrust multi-district litigation, public July 2015** — purported class actions
  alleging Delta, American, United and Southwest *"had conspired to restrain capacity"*, filed
  after DOJ civil investigative demands. Summary judgment **denied August 2023**;
  reconsideration and interlocutory appeal **denied September 2025**; *"The case will proceed
  to class discovery."* Delta says the claims are *"without merit."* Eleven years old, no
  adverse finding, recorded as a source to read rather than a checklist item, per the
  framework's own instruction. **[E5-22]** applies in both directions: penalty size is not
  seriousness. *(It is the same matter that appears in the UAL run, which is itself a fact
  about the industry rather than about either registrant.)*

### STEP 2 — THE FLAGS. Each a prompt to read, never a verdict **[E4-22, E5-15, E5-36]**

- [ ] **weak accounting** — not found. Straight-line depreciation on disclosed lives; the
      loyalty-programme ETV and breakage estimates are disclosed as critical accounting
      estimates **with their sensitivities quantified** (*"A hypothetical 10% change in the
      number of outstanding miles estimated to be redeemed would result in an impact of less
      than 1% of total operating revenue"*), which is the disclosure the framework asks for on
      an estimate-driven line **[E2-50]**.
- [ ] **unintelligible footnotes** — not found in the 10-K. See the proxy prompt below.
- [x] **trumpeted projections [E4-22, E5-30]** — mild but present, and it is forward-looking
      in three places at once: Amex remuneration *"which we expect to grow to $10 billion over
      the next few years"*; *"expected 2026 capital spend of approximately $5.5 billion"*; and
      *"We expect income tax cash payments to increase in 2026."* **[E3-48]**'s action was
      taken: the 2023 10-K guided Amex remuneration to *"increase by 10% in 2024"* and it
      increased 9%; the $10bn target has been carried unchanged since the 2023 10-K, where it
      read *"over the long-term"*, and now reads *"over the next few years"* — **a horizon
      that has shortened while the number has not moved.** Recorded as a prompt.
- [ ] **serial share issuance [E5-15]** — **does not fire.** Shares issued rose from
      654,571,606 to 659,669,346 over 2025, +0.78%, and the increase is CARES Act warrant
      exercises settled net-share, not a capital raise. No equity was sold.
- [ ] **EBITDA / adjusted-earnings promotion [E4-29]** — **DOES NOT FIRE, AND IT IS THE
      CLEANEST RESULT IN THE INDUSTRY.** The string **"EBITDA" appears zero times in the
      FY2025 10-K and zero times in the 2026 proxy statement.** United's 10-K was also clean
      but its proxy moved the pay metric to **Adjusted EBITDAR Margin** in 2025, deleting
      depreciation and aircraft rent together. Delta did neither. **[E5-41]**'s
      *"reverse float"* mechanism — the expense already paid, which EBITDA deletes — is not
      being deleted here, and in the most capital-intensive industry in this queue that is
      worth stating plainly as a credit.
- [ ] **filed-figure tells [E4-30]** — **neither fires.** Cash taxes as a share of reported
      pretax income are *rising*: current tax provision ÷ pre-tax income was **0.34% (2023),
      0.99% (2024), 1.15% (2025)**. All three are trivial, and the innocent explanation is
      filed and specific — net operating loss carryforwards generated in 2020, of which
      *"approximately $2.4 billion"* remained at 2025-12-31. Reported growth is not
      unnaturally smooth; it is violently unsmooth (net income $4,767M → −$12,385M → $280M →
      $1,318M → $4,609M → $3,457M → $5,005M). **The tell does not fire — but the same fact is
      the largest single input to Q4's owner earnings and it is carried there, not here.**
- [ ] **[E2-49] metric-switching** — **does not fire, and the opposite is on record.** The
      2026 proxy: *"the Personnel & Compensation Committee **retained the same performance
      measures** under the annual incentive plan"*, with one addition (reinstating Transpacific
      net-promoter goals). The annual incentive's financial measure is **Pre-Tax Income**,
      which is *"also the measure used under our broad-based Profit Sharing Program, thereby
      aligning the interests of Delta management with all employees"* — and executive awards
      are **capped at target if there is no profit-sharing payout to employees.** That is
      **[E2-49]**'s candor case, not its failure case.
- [x] **A NEW PROMPT THAT DOES FIRE — THREE DIFFERENT "PRE-TAX INCOME" FIGURES IN ONE PROXY,
      AND THE ONE USED TO SET PAY IS THE HIGHEST AND IS UNRECONCILED.** From the DEF 14A filed
      **2026-04-24, accession 0001308179-26-000345**:

      | measure | 2025 | where |
      |---|---:|---|
      | Pre-Tax Income, GAAP | **$6,185M** | 10-K income statement |
      | Pre-Tax Income, adjusted | **$4,977M** | proxy p.83, fully reconciled |
      | **Pre-Tax Income (non-GAAP), the Company-Selected Measure in the pay-versus-performance table** | **$6,799M** | proxy PvP table (`ecd:CoSelectedMeasureAmt`) |

      The pay-table measure is **$614M above GAAP** and **$1,822M above the proxy's own
      reconciled adjusted figure**, and **the proxy reconciles the second and not the third.**
      Adding back the 2025 profit-sharing charge of $1,337M to the reconciled $4,977M reaches
      $6,314M — still **$485M short** of the pay figure, and the proxy does not close the gap.
      A non-GAAP measure that sits *above* GAAP, is used to determine executive pay, and
      carries no reconciliation is exactly **[E4-22]**'s unintelligible-footnote prompt and
      **[E2-26]**'s half-owner test. **Recorded as a live prompt, not a finding of venality
      [E5-38].** The document that would resolve it is a reconciliation the proxy does not
      contain.
- [ ] **[E2-57] the "except for" flag** — not found. Special items are quantified and
      reconciled line by line.
- [ ] **[E3-53] restructuring charges** — none in the window. The 2023 *"Pilot agreement and
      related expenses"* of $864M is a real cost of running the business, disclosed on its own
      income-statement line, and is carried in the owner-earnings mean **[E5-33]**, not
      annualised away.

### STEP 3 — THE PRIMARY TEST **[E2-01]**, and its scope carve-out **[E2-47, E2-43]**

Net income ÷ average stockholders' equity, filed, nine years:

| 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| 30.0% | 30.0% | 32.8% | **(146.6)%** | 10.3% | 25.2% | 52.1% | 26.2% | 27.7% |

**Nine-year arithmetic mean: 9.7%.** The last three years read 52.1%, 26.2%, 27.7% and look
superb; the nine-year series is what **[E2-01]** asks for and it is 9.7%. The 2023 figure of
52.1% is an artefact of an equity base that had been destroyed in 2020 — **average equity of
$8,844M in 2023 against $15,358M in 2019** — which is **[E2-47]**'s "mis-stated asset values"
carve-out arriving from the other direction.

**[E2-47] also carves out "unusual debt-equity ratios," and [E2-43] supplies the denominator
that governs** — *unleveraged net tangible assets, "the best guide to the economic
attractiveness of the operation"*. Built from the FY2025 balance sheet:

| | US$m |
|---|---:|
| Total assets | 81,317 |
| less goodwill | (9,753) |
| less identifiable intangibles, net | (5,966) |
| less cash and equivalents (short-term investments are nil) | (4,310) |
| less non-interest-bearing current liabilities (air traffic 7,157 + AP 5,226 + accrued salaries 4,906 + loyalty deferred current 4,876 + fuel card 1,100 + other accrued 1,945) | (25,210) |
| **= unleveraged net tangible operating assets** | **36,078** |
| Operating income 2025 | 5,822 |
| **Return, pre-tax** | **16.1%** |

**The goodwill wedge is reported rather than hidden [E2-43]: $9,753M of Northwest-merger
goodwill sits outside that denominator and inside the invested-capital one.** On total
invested capital including what was paid for it — operating income ÷ (all debt and leases
$20,274M + equity $20,853M = $41,127M) — the return is **14.2% pre-tax, 11.5% after the 19.1%
effective tax rate.** Both are **first of six in the panel in every year of the window**, and
both are **falling in every year of the window.**

### THE HALF-OWNER TEST **[E2-26]** — and it substantially passes

Does the reporting tell me what I would want to know if the positions were reversed? Largely
yes, and it is worth saying so on a name being rejected:
- **The American Express dollar figure is disclosed every year, in three places.** No other
  US carrier discloses its co-brand economics in dollars at all. This is the single best
  disclosure in the industry.
- **Aircraft purchase commitments are given by year**, five years plus a "thereafter" line,
  and the fleet table gives **owned / finance lease / operating lease / average age by
  aircraft type**, which is what makes the 42.6%-over-twenty-years finding at Q2 computable
  at all.
- **The refinery is reported as its own segment** with revenue, cost of goods sold, D&A,
  operating income, total assets and capital expenditure — so a reader can strip it out. It is
  the reason Delta's own "TRASM, adjusted" exists.
- **The loyalty-programme estimate sensitivities are quantified** rather than described.
- **Against, and specifically:** the MD&A says 2025 *"other, net investing activities primarily
  included **proceeds from several sale-leaseback transactions**"* and the sale of two equity
  stakes, and **quantifies none of the three** — the whole of it is a single $589M "Other, net"
  line. Sale-leasebacks reduce reported net investing outflow while the aircraft stays on the
  ramp under a lease, which is exactly the item Q4's (c) needs. **United quantified its
  sale-leaseback gain at $427M in a footnote; Delta does not quantify its proceeds at all. On
  this one item Delta's disclosure is worse than United's.**

### THE INSTITUTIONAL IMPERATIVE — score all four **[E2-30]**

- [ ] **(1) resists any change in current direction** — not found. Delta ran a materially
      smaller order book than United through the cycle ($15.4bn against $57.0bn) and used
      older aircraft rather than matching peer capex.
- [x] **(2) projects or acquisitions materialise to soak up available funds** — **fires.**
      $15.4bn of firm aircraft commitments, $6.0bn of contract-carrier minimums and $11.2bn of
      other purchase obligations at 2025-12-31 — and then **61 more widebodies ordered in the
      six weeks after the balance-sheet date** (30 B787-10 on 2026-01-12 with options for 30
      more; 16 A330-900 and 15 A350-900 on 2026-01-27 with options for 20 more), **with no
      dollar amount disclosed anywhere in the filing**, plus a $276M equity stake in WestJet.
- [ ] **(3) staff studies to justify the leader's craving** — no evidence in the filings.
- [x] **(4) peer behaviour mindlessly imitated** — **fires.** Every US network carrier placed
      record widebody orders into the same delivery window, and Delta's January 2026 orders
      followed the industry's. This is **[E2-27]** with the **[E2-30]** mechanism named:
      *"Institutional dynamics, not venality or stupidity."*

### CAPITAL ALLOCATION — the buyback conditions **[E5-08, E4-31, E5-24, E5-25]**

- **(1) ample funds for operations and liquidity? NO, on [E5-25]'s standard.** Berkshire
  published its own conditions as numbers in advance — a $20bn liquidity floor, *"financial
  strength that is unquestionable takes precedence over all else."* **Delta's liquidity floor
  is $2.0 billion and it is imposed by its lenders' SkyMiles covenant, not chosen**, and its
  actual unrestricted cash is $4,310M against roughly $9.9bn of contracted 2026 calls (Q4).
- **(2) repurchases at a material discount to conservatively calculated intrinsic value?**
  **The question does not arise, and that is to their credit.** The Board authorised a
  **$1.0 billion opportunistic repurchase programme in the June 2025 quarter, open through
  2028-06-30, and NOT ONE SHARE was repurchased under it through 2025-12-31** — in a quarter
  when the stock traded between $56.17 and $66.61. Delta instead paid $440M of dividends and
  **repaid $4,827M of debt against $2,215M raised, a net repayment of $2,612M.**
- **→ NO CAPITAL-ALLOCATION FLAG IS RAISED, and the reasoning is [E5-31]'s ordering:**
  business needs first, then acquisitions versus repurchases by per-share value added at the
  price. Condition (1) fails, so **declining to repurchase is the correct application of
  [E5-08], not a failure of it.** **[E2-51]** — *"A manager who consistently turns his back on
  repurchases, when these clearly are in the interests of owners, reveals more than he knows
  of his motivations"* — requires the repurchase to be *clearly* in owners' interests, and
  with $4.3bn of cash against $9.9bn of contracted calls it was not. **This is the strongest
  Q3 finding in the file and it runs in Delta's favour.** **[E2-52]** is also checked and does
  not fire: the 2025 dividend was paid out of a year of **net debt repayment**, not out of
  issuance.
- *The one qualification: in January 2026 Delta entered a **$1.3 billion term loan due
  December 2026** to repay $957M of 1%/2% Payroll Support Program loans due 2031 and "for
  general corporate purposes" — refinancing 2031 money into 2026 money. Recorded at Q4 under
  strength (3), not as an allocation flag.*

### PAY VERSUS PERFORMANCE **[E2-49]** — from `ecd` facts filed with the DEF 14A

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|
| PEO compensation actually paid ($) | 11,616,466 | 7,613,922 | 39,811,315 | 56,429,052 | **105,500,600** |
| PEO summary-comp total ($) | 12,360,420 | 9,606,387 | 34,214,328 | 27,117,069 | 19,222,401 |
| Company-selected measure, Pre-Tax Income (non-GAAP) ($m) | (3,144) | 3,619 | **7,021** | **7,052** | **6,799** |
| DAL TSR, $100 invested 2020-12-31 | 97 | 82 | 101 | 152 | **177** |
| NYSE ARCA Airline Index TSR, same basis | 98 | 64 | 83 | 83 | **88** |

Three observations, each filed:
1. **The company-selected measure is flat to down.** 7,021 → 7,052 → 6,799 across 2023-2025,
   **−3.2% in two years**, while compensation actually paid to the CEO moved $39.8M → $56.4M →
   **$105.5M**. The pay outcome is a share-price outcome, not an earnings outcome — the
   reconciliation in the proxy shows **$70.1M of the $105.5M** is the change in fair value of
   awards granted in prior years that vested during 2025.
2. **The base salary was raised on a market-comparison rationale**, from $995,000 to
   $1,100,000, *"to align his fixed compensation more closely with market practice"* — which
   is **[E2-30]**(4)'s peer imitation applied to pay, and it is small.
3. **In fairness, and it is a large fairness:** DAL's TSR of $177 against an airline peer group
   at $88 is a 2x relative outcome over five years, and the annual financial metric is
   pre-tax income shared with 103,000 employees through profit sharing ($1.3 billion paid for
   2025). **[E3-59]** asks how well they ran the business *"against the hand they were dealt"*,
   and against this hand they ran it better than anyone else in the industry.

### THE GUARDRAIL — checked before the verdict **[E2-37, E2-38, E3-39]**

- [x] **Confirmed: nothing in this Q3 is being used to promote the name.** Delta's management
      is, on the filed record, **the best in this industry on every metric this framework
      measures** — first of six on operating margin, first of six on both return metrics in
      every year, no EBITDA anywhere in its filings, the only dollar disclosure of co-brand
      economics in the industry, an unused buyback authorisation, a net debt repayment, and
      an overfunded pension. **None of that repairs Q2.** *"A textile company that allocates
      capital brilliantly within its industry is a remarkable textile company — but not a
      remarkable business"* **[E2-37]**. *"Good jockeys will do well on good horses, but not
      on broken-down nags"* **[E2-38]**.
- [x] **Key-person dependence is recorded at Q2 as a moat defect [E4-23]**, not here as a
      strength. The corpus's own test is whether you can name the CEO. You have to be able to
      name Delta's, because the whole difference between a 9.2% margin and American's 2.7% in
      the same year on the same routes with the same aircraft is management. *"If a business
      requires a superstar to produce great results, the business itself cannot be deemed
      great."*
- [x] **Is the franchise already intact and the damage excisable [E2-35, E2-36]?** Not
      applicable. There is no localised excisable cancer here; there is no franchise to
      operate on. The manager is not the plan because the manager is already excellent and the
      returns still fell.

**VERDICT: NOT REACHED — the file closed at Q2.** Had it been reached, the honest form would
have been **IN** in the narrow sense the framework defines — no disqualifier found — carrying
**one live prompt** (the unreconciled pay-table pre-tax income measure) and **no
capital-allocation flag**, which is a better Q3 than United's. **IN never promotes.**

## Q4 — WILL IT SURVIVE?

> **COMPUTATION — NOT A CLEARANCE.** The file closed at Q2.

### OWNER EARNINGS — THE ONE NUMBER **[E2-23]**

Base = mean of (operating cash flow − share-based compensation), the project's stated
convention, because OCF nets the working-capital increment from one audited line, which is
[E2-23] constraint 3. Eleven years, filed:

| FY | OCF | equity comp expense | **OCF − SBC** | D&A | capex | deferred tax add-back in OCF |
|---|---:|---:|---:|---:|---:|---:|
| 2015 | 7,927 | 76 | **7,851** | 1,835 | 2,945 | 2,581 |
| 2016 | 7,205 | 154 | **7,051** | 1,902 | 3,391 | 2,223 |
| 2017 | 5,148 | 169 | **4,979** | 2,235 | 3,891 | 2,071 |
| 2018 | 7,014 | 159 | **6,855** | 2,329 | 5,168 | 1,364 |
| 2019 | 8,425 | 161 | **8,264** | 2,581 | 4,936 | 1,473 |
| 2020 | (3,793) | 119 | **(3,912)** | 2,312 | 1,899 | (3,110) |
| 2021 | 3,264 | 149 | **3,115** | 1,998 | 3,247 | 115 |
| 2022 | 6,363 | 150 | **6,213** | 2,107 | 6,366 | 591 |
| 2023 | 6,464 | 180 | **6,284** | 2,341 | 5,323 | 980 |
| 2024 | 8,025 | 236 | **7,789** | 2,513 | 5,140 | 1,155 |
| 2025 | 8,342 | 313 | **8,029** | 2,443 | 4,499 | 1,109 |

**Stock compensation subtracted in full [E5-06], with the mechanics disclosed.** Delta's
cash-flow statement carries **no share-based-compensation add-back line at all**; the Note 11
figure is *"Equity compensation expense, **including awards payable in common stock or cash**"*
— $313M in 2025 — of which the equity-settled portion appears in the equity statement as
$120M of additional paid-in capital. Subtracting the full $313M may therefore double-count the
cash-settled portion, at most ~$190M in 2025 and less in every earlier year. **The full
expense is subtracted anyway, as the standing convention applied unchanged**; the alternative
treatment raises every owner-earnings figure below by roughly $150M and changes no verdict.
This is **not** counted as a second windage: it is the convention, not a haircut.
**[E3-70]**'s market-value standard would raise the subtraction further and the reported
charge is treated as its floor.

### MAINTENANCE CAPEX — (c) IS A DISCLOSED JUDGMENT AND THE D&A END IS INVALID **[E5-20]**

**The brief said [E5-20] governs. It does, and it is confirmed five independent ways on
Delta's own filings.**

1. **The corpus rules it out by name, and names airlines specifically.** *"in the case of all
   railroads, **merely spending their depreciation expense will not keep them in the same
   place** … the true maintenance capex … is **higher than 60 percent**"* **[E5-20]**, and
   **[E3-44]** names the class in the same answer that supplies the D&A default: *"Businesses
   you have to worry about — I mean, **an airline business is a good case. In the airlines,
   you know, you just have to keep spending money like crazy.**"* The D&A default explicitly
   does not reach this class.
2. **The ratio says so.** Capex ÷ D&A is **1.84x in 2025**, 2.05x in 2024, 2.27x in 2023,
   1.99x on the five-year mean and 1.90x on the eleven-year mean. A business that has spent
   roughly twice its depreciation for a decade is not one where depreciation approximates
   renewal.
3. **Management says so, in its own forward number.** FY2025 MD&A: *"Our **expected 2026
   capital spend of approximately $5.5 billion**, which may vary depending on financing
   decisions, will be primarily for aircraft, including deliveries and advance deposit
   payments, as well as fleet modifications and technology enhancements."* That is **2.25x the
   2025 depreciation charge** and 22% above 2025 actual capex.
4. **THE FLEET AGE PROFILE IS THE DECISIVE EVIDENCE, AND IT IS SPECIFIC TO DELTA.** The reason
   Delta's capex looks modest beside United's is that **42.6% of its 989 mainline aircraft are
   twenty years old or more and 18.2% are twenty-five or more** (Q2, Item 2 Properties). The
   depreciation charged on a B-757 bought in the 1990s is charged in 1990s dollars against a
   replacement priced in 2026 dollars. That is **[E4-47]** operating in the exact form it
   describes: *"under high inflation, replacement capex in current dollars outruns depreciation
   charged in old dollars."* **Delta's low capex is a deferred bill, not an avoided one.**
5. **The independent replacement arithmetic.** A 989-aircraft mainline fleet on a 27-year
   economic life needs **37 replacements a year**. The disclosed commitment book is $15,430M
   for 256 airframes, or **$60 million each**; 37 airframes a year at $60M is **$2.2 billion
   for mainline replacement alone**, before the 325 regional aircraft, spare engines, cabin
   retrofits, airport construction, ground equipment and IT — all of which are also
   depreciating and all of which sit inside the same $2,443M depreciation charge.

**(c), as a disclosed guess:** somewhere between **60% of adjusted capital spend**
([E5-20]'s own stated floor) and **all of it**. Total GAAP capex is used as the working (c)
below because it sits inside that band and is the only figure taken directly from an audited
statement — and because, as the leakage below shows, **it is the GENEROUS end of the valid
range, not the conservative one.**

**THE LEAKAGE, QUANTIFIED — and the brief's item 3 answered.** The supplemental "Non-Cash
Transactions" schedule at the foot of Delta's FY2025 cash-flow statement:

| | 2025 | 2024 | 2023 |
|---|---:|---:|---:|
| Right-of-use assets acquired **or modified** under operating leases | 375 | 327 | 661 |
| Flight and ground equipment acquired **or modified** under finance leases | **184** | (17) | 31 |
| Operating leases converted to finance leases | 312 | 25 | 84 |
| Debt agreements modified | 371 | 0 | 0 |

**Adjusted capital spend 2025 = $4,499M cash + $184M finance-lease + $375M operating-lease ROU
= $5,058M**, against management's $5.5bn guide for 2026. Pre-delivery deposits are **inside**
reported capex — the line reads *"Flight equipment, **including advance payments**"* — so there
is no PDP leakage, which is a point in Delta's favour and the opposite of what the brief
feared. **Sale-leasebacks are the unquantified item:** the MD&A says 2025 "other, net"
investing *"primarily included proceeds from several sale-leaseback transactions"* and gives no
amount inside a $589M line. **That is a genuine hole and it is named rather than guessed.**

### MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE **[E4-25]**

**The brief's mandatory correction 1 was applied: six windows, both capex ends, and a second
axis the published screen row does not carry.** Market capitalisation $52,722M.

| window | base (OCF−SBC) | (c) = total capex | **OE** | yield | **OE, cash-tax normalised** | yield | *OE at D&A — INVALID [E5-20]* |
|---|---:|---:|---:|---:|---:|---:|---:|
| 3-yr, 2023-25 | 7,367 | 4,987 | **2,380** | 4.51% | **1,299** | 2.46% | *4,935 / 9.36%* |
| 5-yr, 2021-25 | 6,286 | 4,915 | **1,371** | 2.60% | **581** | 1.10% | *4,006 / 7.60%* |
| 7-yr, 2019-25 | 5,112 | 4,487 | **625** | 1.18% | **(150)** | (0.28)% | *2,784 / 5.28%* |
| 9-yr, 2017-25 | 5,291 | 4,497 | **794** | 1.51% | **(190)** | (0.36)% | *2,973 / 5.64%* |
| 11-yr, 2015-25 | 5,683 | 4,255 | **1,428** | 2.71% | **186** | 0.35% | *3,447 / 6.54%* |
| **9 clean yrs, ex 2020-21** | **7,035** | **4,629** | **2,406** | **4.56%** | **901** | **1.71%** | *4,781 / 9.07%* |
| clean-9 at [E5-20]'s 60% floor | 7,035 | 2,777 | **4,258** | 8.08% | **2,753** | 5.22% | — |

**THE SECOND AXIS, AND IT IS THE LARGEST SINGLE FINDING IN THIS FILE.** *"Cash-tax normalised"*
subtracts the deferred-income-tax add-back from operating cash flow — i.e. it asks what owner
earnings would have been had Delta paid its **book** tax provision in cash. It matters because
**Delta has paid essentially no US federal cash income tax for the whole of the window**:
current tax provision was **$19M (2023), $46M (2024), $71M (2025)** against pre-tax income of
$5,608M, $4,658M and $6,185M. And the 10-K says the shield is **over**:

> *"During 2025, we utilized **substantially all of our remaining pre-2018 net operating loss
> carryforwards** and, due to the limitations on post-2017 net operating losses, **began making
> cash federal income tax payments**. **We expect income tax cash payments to increase in
> 2026** … As of December 31, 2025, we had approximately **$2.4 billion** of U.S. federal
> pre-tax net operating loss carryforwards which we are expecting to utilize **during 2026**."*

**This is [E4-41] exactly** — *"normalize the mean DOWN for luck … Favourable exogenous breaks
in the window are named and removed before the mean is trusted"* — and the break is worth
roughly **$1.1 billion a year**, which is between 45% and 175% of the owner-earnings figure at
every window. Neither end of the tax axis is right: the as-filed end assumes a shield the
registrant says is exhausted, and the fully-normalised end ignores the genuine recurring
deferral that $5.5bn a year of new aircraft generates. **So both ends are carried, and the
width between them is part of the range, which is what [E4-25] requires.**

- **Short-window mean (3-yr): $2,380M. Long-window mean (9-yr): $794M.**
- **Spread across windows at the capex end, as filed: the 9-year window is 67% BELOW the
  3-year window.** The `run.py` threshold for "the spread is part of the range, not a
  tiebreak" is 15%. This is four and a half times it.
- **REBUILT COMBINED RANGE, valid constructions only (capex end, both tax bases):
  −$190M to +$2,406M.** The range **crosses zero**, so no ratio is defined across it — which is
  a stronger statement than any percentage.
- **Including the [E5-20]-invalid D&A end, purely to display what the default would have
  produced: −$190M to $4,935M.**
- **AGAINST THE PUBLISHED SCREEN ROW.** The published figures were `oe_bottom 1137`,
  `oe_top 4935`, spread 334%. Both are reproduced exactly by `Screens/floor_screen.py`
  (`5y_capex` = $1,136.8M, `3y_da` = $4,935.0M). **The rebuilt bottom on the as-filed tax basis
  is $625M — 45% BELOW the published bottom — and on the cash-tax-normalised basis it is
  negative.** **The brief's warning holds for a ninth consecutive run: the true width is larger
  than published, and here it is not merely larger, it is unbounded, because it crosses zero.**
- **Is that range too wide to reach a conclusion? YES, and [E4-25] says that IS the
  conclusion:** *"Usually, the range must be so wide that no useful conclusion can be
  reached."* **Q4 would independently return UNKNOWABLE on the owner-earnings width even if
  Q2 had passed. The file does not need Q2 to close it.**
- **[E5-11] — the wide spread is itself a Q4 finding about earnings reliability.** Name the
  distorted years: **fiscal 2020 and fiscal 2021**, in which operating cash flow was −$3,793M
  and +$3,264M against a 2019 base of +$8,425M.
- **[E3-55], scoped honestly against my own conclusion:** *"If we have a business about which
  we're extremely confident as to the business result, we would prefer that it have high
  volatility."* Volatility with a certain endgame is not a defect. **The endgame here is not
  certain** — that is the difference between See's losing money eight months a year and an
  airline losing $12.5 billion of operating income and 90% of its book equity in one.

**OWNER EARNINGS BY YEAR, at the valid (total-capex) end.** Three of eleven years are negative:

| 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4,906 | 3,660 | 1,088 | 1,687 | 3,328 | **(5,811)** | **(132)** | **(153)** | 961 | 2,649 | 3,530 |

### THE BOOM-WINDOW TEST **[E4-41]** — `level_shift` and `best_year_dependence`, run

From `Screens/floor_screen.py`, imported directly, on the owner-earnings series above.

| series | `level_shift` | `best_year_dependence` |
|---|---|---|
| 11-yr, capex end | **2.22 — "STEP UP, normalize down [E4-41]"** | 0.444 — **TWO YEARS JOINTLY CARRY THE WINDOW** |
| 9-yr 2017-25, capex end | **2,040.0 — uninterpretable (see DEFECTS)** | 0.948 — two years carry it |
| **9 clean years, capex end** | **0.98 — "no step"** | 0.130 — one year doing heavy lifting |
| 9 clean years, D&A end | 1.05 — "no step" | 0.032 — no single-year dependence |

**Interpretation, which the tool is forbidden to supply (operator rule 8).** On the clean
window the level is flat and no single year carries it — Delta's earnings are *not* a
two-year boom in the way United's were. The 2.22 on the eleven-year series is entirely the
2020-2021 hole and nothing else. **So the [E4-41] "normalize down" instruction does not bite
through the boom-window instrument here; it bites through the tax shield instead**, which the
instrument cannot see because the shield sits inside operating cash flow in every year of
every window. **That is the honest reading and it is the more dangerous one: the instrument
says "no step" on precisely the series whose largest exogenous support the registrant has just
announced is ending.**

**The second named break, quantified but NOT deducted, to keep the windage count at one:**
average jet fuel fell from **$3.36 per gallon in 2022 to $2.30 in 2025**. At 4,269 million
gallons that is **$4,525 million a year, 78% of 2025 operating income**, and it is a commodity
price, not an achievement. It is carried into the death mechanism below rather than removed
from the mean.

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

- [ ] great [ ] good [x] **GRUESOME**

The corpus names this business in the sentence that defines the class: *"The worst sort of
business is one that **grows rapidly, requires significant capital to engender the growth, and
then earns little or no money. Think airlines.**"* **[E4-20]**

**The framework does not permit that quotation to be the finding, so here is the arithmetic
instead, and [E4-43]'s warning against over-reading is applied FIRST and at full strength.**
[E4-43] says the *good* class **passes** and cites *"nothing shabby about earning $82 million
pre-tax on $400 million of net tangible assets"* — 20.5%. **[E5-40]** puts ~12% on retained
capital at "quite satisfactory." **Delta earns 16.1% pre-tax on unleveraged net tangible
operating assets, which sits squarely between those two marks, and 14.2% on total invested
capital including the Northwest goodwill. On that metric alone Delta reads as "GOOD", not
gruesome, and it is the best such reading in the industry. That is recorded as the case
against this verdict and it is a strong one.**

It fails anyway, for the reason **[E4-20]** actually gives, which is a **savings-account** test
about what the owner takes out:
- The account's interest rate, measured as the corpus measures it — owner earnings against the
  price paid — is **1.7% to 4.6%** across the judged constructions and **−0.4% to 8.1%** across
  the full valid range. The bond is **5.24%**.
- The account *"requires you to keep adding money at those disappointing returns"*: **$15.4bn
  of firm aircraft commitments, $6.0bn of contract-carrier minimums, $11.2bn of other purchase
  obligations, and 61 further widebodies ordered after the balance-sheet date with no price
  disclosed** — against a $52.7bn market capitalisation.
- Nine years of it produced **$40.5 billion of capital expenditure and real operating income
  23.8% BELOW the 2017-2019 real mean.**
- **[E4-43]'s own escape clause is the test, and it fails it:** cash-consuming growth is only
  gruesome *"unless the cash they consume gets to earn a reasonable return."* $40.5 billion
  consumed; real operating income down a quarter. **It did not.**

### STAYING POWER — SCORE ALL THREE **[E5-11]**

**(1) A large and reliable stream of earnings — LARGE, NOT RELIABLE. FAILS on "reliable."**
$63.4 billion of revenue and $5.8 billion of operating income is the largest in the industry.
But **operating income was −$12,469M in 2020**, owner earnings at the valid capex end were
negative in **three of the last eleven years**, and **[E5-29]** is respected — risk means
impairment, never price movement — and the impairment was real and enormous: **stockholders'
equity fell from $15,358M at 2019-12-31 to $1,534M at 2020-12-31, a 90.0% loss of book equity
in twelve months.**

**(2) Massive liquid assets — FAILS, and this is the strength United passed and Delta does
not.** Cash and cash equivalents **$4,310M**, and **short-term investments are nil**. The
MD&A's headline liquidity figure of **$7.4 billion** is cash **plus $3.1 billion of undrawn
revolving credit facilities**, and **[E5-39]** is applied strictly: *"We will never be
dependent on the kindness of strangers … cash is a lot like oxygen"* — **no bank lines
counted.** The [E5-11] number is therefore **$4,310M**, which is:
- **6.8% of revenue**, and less than the $4,499M Delta spent on capital expenditure in 2025;
- **one third of United's $12,240M**, on a larger revenue base;
- and **not fully discretionary**: the SkyMiles financing agreements impose a **$2.0 billion
  minimum-liquidity covenant**, so only ~$2.3bn is free if the revolver is unavailable —
  which is precisely the circumstance in which it would be needed.

*It is a chosen policy, not an accident: the FY2021 10-K said "By 2024, we expect liquidity to
be between $5 billion and $6 billion as we work to reduce our financial obligations and
reinvest in the business." Delta delivered on that plan. **[E2-55]** is the standard against
which the plan is judged — "we do not wish it to be only likely that we can meet our
obligations; **we wish that to be certain** … acceptable long-term results under
**extraordinarily adverse conditions**" — and a $4.3bn buffer against a business that consumed
$12.2bn of operating income swing in a single year does not meet it.*

**(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS — FAILS. This is the one [E5-11] says
"usually leads companies to experience unexpected problems."**

| contracted 2026 call | US$m | source |
|---|---:|---|
| Debt maturities | **1,367** | Note 6 future maturities |
| Finance lease payments | 256 | Note 7 undiscounted cash flows |
| Operating lease payments | 1,020 | Note 7 undiscounted cash flows |
| Interest | ~500 | MD&A, "approximately $500 million in 2026" |
| Aircraft purchase commitments | **3,650** | Note 9 |
| Contract carrier minimum obligations | 1,760 | Note 9 |
| Other purchase obligations | ~1,400 | MD&A |
| **Total contracted** | **≈9,953** | |
| plus dividends at the declared $0.1875/quarter | ~493 | Item 5, and the 2026-02-04 declaration |
| plus cash income taxes, "expected to increase", not quantified | n/d | MD&A |
| **against: cash and cash equivalents** | **4,310** | balance sheet |
| against: 2025 operating cash flow | 8,342 | cash-flow statement |

It closes only if operating cash flow holds, and it was topped up by refinancing anyway: **in
January 2026 Delta entered a $1.3 billion term loan due December 2026** to repay $957M of
1%/2% Payroll Support Program loans that were not due until 2031. **That is 2031 money
refinanced into 2026 money, six weeks after the balance-sheet date.** And the same six weeks
carry the two undisclosed-price widebody orders.

**Delta is now the sixth name in this project to fail an [E5-11] strength on [E5-39] — after
LOW, ITW, SHW, HD and UAL — and the second to fail two of the three.**

**[E2-54]'s coverage test — "all interest, both payable and accrued, comfortably met out of
current cash flow net of ample capital expenditures." THIS PASSES, and comfortably, which is
a real difference from United.**
- clean-9 means, as filed: (7,035 + ~1,000 interest paid) − 4,629 = **$3,406M** against ~$1,000M
  of interest = **3.4x**.
- On management's own 2026 capex guide: (8,342 + 850) − 5,500 = **$3,692M** against the guided
  ~$500M of 2026 interest = **7.4x**.
- On the cash-tax-normalised clean-9: (5,530 + 1,000) − 4,629 = **$1,901M** ÷ $1,000M =
  **1.9x. Thin, but covered.**
Delta's interest paid fell from $1,164M (2023) to $850M (2025) while United's runs near
$1.6bn on a smaller business. **[E2-54] is met at every construction. It is the clearest
Q4 pass in the file.**

**[E3-52] — read the terms, not just the quantity, and this cuts BOTH ways.**
*Against:* the $20.3bn is **covenanted, secured, dated** debt — a $2.0bn minimum-liquidity
covenant, a $550M limit on the sale of pre-paid miles, minimum coverage ratios in the SkyMiles
agreements that *"could trigger an early amortization event or … require us to post additional
collateral"*, and a restriction on changing the SkyMiles programme itself.
*For:* Delta also carries **$7,157M of air traffic liability and $9,262M of loyalty programme
deferred revenue = $16.4 billion of customer-prepaid, non-interest-bearing, covenant-free,
undated liabilities**, which genuinely is *"the benefit of debt … with none of its drawbacks"*
and is why the unleveraged net tangible operating asset base is only $36.1bn on $81.3bn of
assets. **It is the single best structural feature of this business and it is recorded as
such.**

**PENSION — the brief flagged it and the filing REFUTES the concern.** Note 8: the pension
plan's benefit obligation is **$15,022M** against plan assets of **$17,280M** — a funded
status of **+$2,258M, a surplus** — and *"Estimated funding by employer in next fiscal year:
**$5 million**."* The expected long-term return assumption is **6.96%** against an actual 2025
return of roughly 14.7%; **[E4-22]**'s *"fanciful pension assumptions"* flag does not fire.
Other postretirement and postemployment benefits are unfunded at **−$3,217M** with ~$489M of
benefits paid a year, which is a real recurring cost already inside operating cash flow.
**Combined net position −$959M against $20,853M of equity. The pension is not a threat to this
company and the prior is withdrawn.**

**Leverage, named and quantified [E4-16, E3-29]** — *there is no ratio ceiling in this framework
and the corpus supplies none:* $20,274M of debt and lease obligations, $15,964M net of cash,
against $20,853M of equity and $5,822M of operating income. **Net debt is 2.7x operating income
and 0.77x equity**, against United's 4.0x and 1.23x. Principal amount of debt and finance
leases $14.1bn; **Moody's upgraded Delta to Baa2, investment grade, in February 2025**, and
Fitch and S&P moved their outlooks to Positive. **Delta is the least leveraged and only
investment-grade US network carrier.** In 2020 this same structure met a 63.6% revenue decline
and lost 90% of its book equity.

### **[E3-24]** — NAME THE SPECIFIC WAY THIS BUSINESS DIES, QUANTIFIED, WITH A LIKELIHOOD

**The mechanism.** A demand shock or a fuel spike arrives while $15.4 billion of noncancelable
aircraft commitments is running — **$3.65 billion of it inside twelve months** — against
$4.3 billion of cash and a $2.0 billion covenant floor. The commitments cannot be cancelled
without liability. Capacity therefore keeps arriving into a falling market, which is
**[E2-27]** exactly, fares fall further, and the equity absorbs the difference. The
cash-tax shield that carried the last decade's operating cash flow is simultaneously expiring
by the registrant's own statement.

**Quantified from filed figures, three ways:**
1. **Fuel.** 4,269 million gallons at $2.30 = $9,819M in 2025. A return to the 2022 price of
   $3.36 costs **$4,525M — 78% of 2025 operating income** — with the company's own filed
   statement that *"we often were not able to increase our fares to offset fully the effect of
   increases in fuel costs."* A return only to 2023's $2.82 costs $2,220M, 38% of it.
2. **Demand.** A 10% fall in revenue passenger miles at the 2025 yield of 20.74c removes
   24,958 million RPMs × $0.2074 = **$5,176M of passenger revenue** — 89% of operating income
   — against a short-run cost base that is largely fixed.
3. **The 2020 stress test is filed, not modelled.** Revenue $47,007M → $17,095M (**−63.6%**);
   operating income +$6,618M → **−$12,469M**; operating cash flow +$8,425M → **−$3,793M**;
   **stockholders' equity $15,358M → $1,534M, a 90.0% loss.** Delta survived on the CARES Act
   payroll support programme, on capital markets, and above all on the **$9.0 billion SkyMiles
   financing of September 2020** — the single largest debt financing in aviation history at the
   time, and the only reason standalone SkyMiles figures exist at all.
   **AND THE FIRE EXTINGUISHER IS STILL HALF-DISCHARGED. $4,010 million of SkyMiles-secured
   debt remains outstanding at 2025-12-31 and the programme is encumbered by a covenant
   restricting changes to its policies. United's equivalent collateral was fully released on
   2025-07-07; Delta's is not.** The single largest unencumbered asset used to survive 2020 is
   still pledged.

**Likelihood: [x] a real possibility.** Not "a low-level possibility," and the reason is
**[E4-40]**: *"all of us in the industry made a fundamental underwriting mistake by focusing on
experience, rather than exposure."* The exposure is filed and it is enormous; the experience of
2022-2025 has been benign; a benign loss history late in a good cycle is *"not only useless,
but actually dangerous"* as a guide. The event occurred once in the last six years.

**VERDICT: NOT REACHED — the file closed at Q2. Had it been reached it would have returned
UNKNOWABLE on [E4-25] (the valid owner-earnings range crosses zero) with strengths (1), (2)
and (3) of [E5-11] all failing. Neither is a pass.**

---
⛔ **Q5 does not open unless Q1-Q4 each show IN. Q2 returned OUT. What follows is the price
the run's output contract requires, and nothing else.**

---
## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

# COMPUTATION — NOT A CLEARANCE

**Operator rule 3.** The file closed at Q2 (OUT). Every figure below is arithmetic produced
after a failed gate. **It carries no entry language, no ranking position, and no clearance.**

**Inputs.** Sovereign **5.24%** (US Treasury 30-year par yield, 2026-09-04, issuing authority).
Price **$80.17** (2026-09-04, aggregator, live quote only, flagged). Shares **657,623,030**
(10-Q cover, quarter ended 2026-06-30). **Market capitalisation $52,722M.**
**No risk premium is added to the rate [E3-42]** — certainty is priced at the understanding
gate and in the end discount, never in the discount rate.

**1. THE YIELD**
- owner earnings **−$190M .. $4,258M** (valid constructions only; the D&A end is excluded as
  INVALID **[E5-20]**) ÷ market cap **$52,722M** = **(0.36)% .. 8.08%** · sovereign **5.24%**
- **judged central band: $900M to $2,400M** — the nine clean years excluding 2020-2021, at
  total capex, carried on both tax bases because the filing itself says the tax basis is
  changing — = **1.71% to 4.56%**, i.e. **0.7 to 3.5 points BELOW the bond.**
- *For completeness the invalid D&A construction would read $4,935M and 9.36%. It is shown
  only so the reader can see what the default would have produced and why [E5-20] voids it.*

**2. WHAT THE PRICE ALREADY ASSUMES**
- Perpetual growth needed to justify the quote **at the sovereign discount rate**: **3.53%** at
  the tax-normalised clean-9, **0.68%** at the as-filed clean-9, **5.52%** at the tax-normalised
  seven-year window.
- Perpetual growth needed to reach the **[E4-28] 10% floor**: **8.29%** at the tax-normalised
  clean-9, **5.44%** at the as-filed clean-9.
- **What the business has actually done:** real operating income **−23.8%** against the
  2017-2019 real mean and **−30.1%** against 2019 alone. Real PRASM **−10.1%** since 2019. Real
  CASM **+4.5%**. Nominal revenue CAGR 2017-2025 is 5.5%, and all of it and more is inflation,
  volume and refinery sales.
- **[E4-35]'s base rate applies to the floor case:** sustained double-digit growth is a
  fewer-than-1-in-20 event among the 200 most profitable companies. This name needs 8.29%
  perpetual nominal growth merely to reach the quit-on line, against an eight-year record of
  minus a quarter in real terms. **[E4-44]** adds the second bound: *"the value of an asset …
  cannot over the long term grow faster than its earnings do."*

**3. WHAT YOU ARE PAID**
- At the judged owner-earnings band and zero growth: **1.71% to 4.56% against a 5.24%
  sovereign = −3.53 to −0.68 points over the sovereign.**
- Range across all valid constructions: **−5.60 points to +2.84 points.**

**THE FLOOR, BEFORE ANY RANKING [E4-28, E3-13].** *"That's the figure we quit on."*
**Honest pre-tax expectancy at this price: 1.71% to 4.56%** (judged), **8.08%** at the single
most generous valid construction ([E5-20]'s 60% floor on the clean-9 as-filed basis).
**Every one is below roughly 10%. The name is not ranked. It is quit on**, whatever the
sovereign is and whatever the rest of the opportunity set looks like. **[E4-28]** is explicit
that this holds *"whether short rates are 6 percent or whether short rates are 1 percent."*

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — 657.6M shares:

| construction | zero-growth value at the 5.24% sovereign | at the [E4-28] 10% floor |
|---|---|---|
| 9-yr window, cash-tax normalised, −$190M | *negative — no value* | *negative* |
| 7-yr window, as filed, $625M | ~**$18**/sh | ~**$9**/sh |
| **clean-9, cash-tax normalised, $901M** | ~**$26**/sh | ~**$14**/sh |
| 3-yr window, cash-tax normalised, $1,299M | ~**$38**/sh | ~**$20**/sh |
| **clean-9, as filed, $2,406M** | ~**$70**/sh | ~**$37**/sh |
| clean-9, tax-normalised, at [E5-20]'s 60% floor, $2,753M | ~**$80**/sh | ~**$42**/sh |
| clean-9, as filed, at [E5-20]'s 60% floor, $4,258M | ~**$124**/sh | ~**$65**/sh |

- **conservative ~$0-20 · judged ~$26-70 · optimistic ~$124 · current price $80.17**
- *The width of that range is not a presentation failure; it is the finding. **[E4-25]**:
  "Usually, the range must be so wide that no useful conclusion can be reached."*
- **[E2-63] — what bounds the upside is stated, not just the yield:** the $124 figure requires
  simultaneously that maintenance capex is only 60% of the spend on a fleet 42.6% of which is
  twenty years old, that the pandemic years are permanently excluded from the record, **and
  that Delta never pays cash income tax**, which its own 10-K says it has already started
  doing. **All three of those are assumptions the filing contradicts.**

**WHICH BAR** — **[x] Bar 2, the screamer test [E4-01]**, and it returns the middle outcome.
No margin is added on top; "startlingly low" is observed, not subtracted. **The price of
$80.17 sits INSIDE the range** ($0 to $124), which is the outcome the framework calls *"no
useful conclusion — move on."* Not a buy, not a short, no view. *Note however that $80.17 is
**above the entire range at the [E4-28] floor** ($0 to $65), which is the test that actually
governs entry.*
**Windage count: ONE.** Conservatism is spent once, at the (c) judgment, where total capex is
used because [E5-20] invalidates the D&A alternative. It is **not** re-spent in the discount
rate (no risk premium, **[E3-42]**), **not** in the growth rate, and **not** in a second end
margin. The cash-tax axis is **input realism under [E4-48]** — *"try to be as realistic as you
can on those numbers, but with any errors being on the conservative side"* — carried as a
disclosed range with both ends shown, not as a haircut; and the fuel tailwind is quantified at
Q4's death mechanism rather than deducted from the mean, for the same reason.

**VERDICT: NOT APPLICABLE. The gate did not open. Ranking position: none — the name is quit
on at the [E4-28] floor, not ranked against the opportunity set.**

## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Not reached. There is no position, so [E1-02]'s pre-commitment and [E2-28]'s sell rule have
nothing to bind.** What is recorded instead is **the one thing that would reopen this file**,
written now so that it is pre-committed rather than retrofitted **[E1-02]**:

**THE REOPENING CONDITION.** Q2 turned on **[E3-03]** criterion (2) and on the CPI-deflated
unit-revenue series. It would be reopened by, and only by, **five consecutive years in which US
industry available seat miles grow more slowly than US real GDP while Delta's real PRASM
rises.** That is the filed, observable signature of **[E2-58]**'s ratio of supply-tight to
supply-ample years permanently changing, and it is the one path — flagged at the competitor row
under **[E3-61]** — by which this verdict is wrong. Five years, because **[E4-17]** says *"those
beliefs change quite gradually"* and **[E2-42]** makes five years the default window. **Nothing
shorter counts, and a single good year counts for nothing.**

**A second, independent monitoring line, specific to Delta and not to the industry:** the
American Express remuneration figure against real operating income, both published here
annually. The bull case is that the loyalty stream eventually outgrows the airline's price
erosion. It has not: **+$3.0bn of real loyalty cash between 2019 and 2025 against −$2.5bn of
real operating income.** If that sign ever reverses for five consecutive years, the two-business
case becomes testable again.

**The monitoring metric, if anyone tracks it:** real PRASM and real CASM in constant dollars,
side by side, beside industry ASM growth. **[E4-32]**: direction outranks existence.

**And the corpus's own conduct on this exact security is on the record:** Berkshire held Delta
and exited in 2020 *"complete, weeks, no half measures"* once the view crystallised
**[E2-40]**. Q6 carries both halves — slow to conclude, fast once concluded.

**VERDICT: NOT REACHED.**

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, **Q2 OUT — file closed.**
      Q3, Q4, Q5 written as COMPUTATION under operator rule 3, each headed as such, none
      claiming a verdict.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only
      IN and it rests on the filed operating statistics, the filed revenue disaggregation and
      the filed fleet table.
- [x] No UNRESEARCHED verdict was issued. The separating question **[E4-19]** was asked aloud
      at Q2 and the answer was that no missing document exists — the price competition is in
      the registrant's own risk factors and the physical series is filed for eleven years.
- [x] No UNKNOWABLE verdict was issued at Q2. **Q4 would independently have returned
      UNKNOWABLE on [E4-25]** (a valid owner-earnings range that crosses zero) and that is
      stated in its section.
- [x] Step 0: the filing was read — MD&A, cash-flow statement including the supplemental
      non-cash schedule, and Notes 1, 2, 5, 6, 7, 8, 9, 10, 11 and 14 — with accession
      **0000027904-26-000013**, and figures were cross-checked **four ways**: the whole FY2025
      balance sheet reconstructed line by line to the filed totals and to equity; capex
      $(3,521) + $(978) = $(4,499)M against the XBRL fact and the MD&A; MD&A liquidity $7.4bn
      against cash $4,310M plus $3.1bn of revolvers; and fuel 4,269m gallons × $2.30 =
      $9,819M against the income-statement line.
- [x] Owner earnings on a multi-year mean; **six windows and two tax bases stated (twelve
      valid constructions plus six invalid ones)**; capex band disclosed as a judgment with the
      D&A end marked INVALID and the reason cited to the filing and to [E5-20]/[E3-44].
- [x] Competitor row filled — 5 of the 5 remaining scale US competitors, same metric, same
      window, filing-sourced, reused from the UAL run's working papers as the brief directed.
      Not marked PROVISIONAL.
- [x] Sovereign is for the earnings currency (USD), from the issuing authority (US Treasury),
      dated 2026-09-04.
- [x] Value stated as a round-number range, not a point estimate.
- [x] One bar chosen (Bar 2, the screamer test); **windage count stated: ONE.**
- [x] Prices dated; aggregator used for the live quote only and flagged.
- [x] Share count taken from the cover of the **latest periodic filing** (10-Q, 2026-06-30),
      not the 10-K, per the brief's correction 4.
- [x] Run committed to git after every gate.
- [x] **Operator rule 9 honoured:** the expectation (Q2 OUT) was pre-registered in writing at
      the head of this file before any filing was opened; the disconfirming evidence was hunted
      and is stated first and at full strength in four separate places (the return-on-assets
      table, the Amex growth series, the [E4-43] good-class reading of 16.1%, and the entire
      Q3 capital-allocation section); and the run says plainly and repeatedly that Delta is the
      best business in its industry.

## REGISTER
- Verdict: **[x] OUT (about the business)**
- One line: **DAL fails [E3-03] criterion (2) — no close substitute — on its own risk factors,
  which name eight competitors and "significant price competition"; the eleven-year
  CPI-deflated series shows real unit revenue down 10.1% and real unit cost UP 4.5% since 2019,
  and $40.5 billion of capital left real operating income 23.8% below its 2017-2019 mean —
  while the one asset that looks like a franchise, the American Express relationship, added
  $3.0 billion of real annual cash over the same period and was entirely consumed by the
  flying business.**
- **PASS/FAIL: FAIL. The file closed at Q2 (OUT).**
- **Price: $80.17, 2026-09-04.** Zero-growth value against the sovereign, valid constructions:
  **~$0 to ~$124 per share, judged ~$26-70.** At the [E4-28] floor: **~$0 to ~$65, judged
  ~$14-37 — the price is above the entire floor range.**
- **Honest pre-tax expectancy: 1.7% to 4.6% judged, 8.1% at the single most generous valid
  construction. All below the ~10% floor. Quit on, not ranked.**
- SkyMiles was tested separately as instructed, on the two-business method, using Delta's own
  2020 8-K exhibit. **The test returns one business, not two**: 97% of redemptions are on
  Delta, 12% of 2025 revenue miles flown were award travel, 58% of the $8.0bn of marketing cash
  is deferred airline revenue by Delta's own allocation, the margin is an intercompany transfer
  price, the filer reports the programme inside the airline segment, **no audited standalone
  financials exist**, and $4.0bn of debt is still secured on it under a covenant that restricts
  changing the programme.

---
## ADDENDUM 1 — 2026-09-07, same session: A LEDGER ROW WAS ADDED, AND WHY

*Recorded as a marked addendum rather than by editing Q2 above (operator rule 6).*

The brief asked for the corpus's airline verdict **quoted, by ledger id**, and said: *"if it
is in the corpus but not the ledger, PRIME RULE 6 says the ledger row must exist before the
rule is applied, so add it verbatim with year and source file."*

**It was in the corpus and only half in the ledger.** `principle_ledger.csv`'s **[E4-20]**
quotes the 2007 letter's gruesome-class paragraph as:

> *"Now let's move to the gruesome. The worst sort of business is one that grows rapidly,
> requires significant capital to engender the growth, and then earns little or no money.
> **Think airlines. [...] Investors have poured money into a bottomless pit** …"*

The material inside that ellipsis, read from `Shareholder Letters/2007 Letter.txt` lines
409-420, is:

> *"Think airlines. **Here a durable competitive advantage has proven elusive ever since the
> days of the Wright Brothers.** Indeed, if a farsighted capitalist had been present at Kitty
> Hawk, he would have done his successors a huge favor by shooting Orville down. **The airline
> industry's demand for capital ever since that first flight has been insatiable.** … And I, to
> my shame, participated in this foolishness when I had Berkshire buy U.S. Air preferred stock
> in 1989 … In the decade following our sale, the company went bankrupt. Twice."*

**The elided clause is the only place in the corpus where the airline verdict is stated as a
DURABILITY claim — which is Q2's question — rather than as a returns claim, which is Q4's.**
As the ledger stood, a run reaching for the corpus's airline verdict at Q2 had no row to cite.
**This is the second recorded instance of the same defect class: [E4-29] was likewise
"previously dropped by v4's own ellipsis" from the 2002 passage.**

**The row added is [E4-56]**, verbatim, 2007, `Shareholder Letters/2007 Letter.txt`.
**[E4-20] was NOT edited** — operator rule 6 forbids editing history — and the new row sits
beside it. `python tools/check_framework.py` **PASSES** on 267 rows, 0 phantom citations,
0 unlabelled numbers.

**Applied to Q2, and it does not change the verdict — it supplies the citation the verdict
already deserved.** Q2 returned OUT on **[E3-03]** criterion (2), evidenced from Delta's own
risk factors and its own eleven-year physical series. **[E4-56]** is the corpus's own
statement of the same conclusion about the industry, and **it is cited last rather than first
on purpose**: the framework does not permit a quotation to be the finding **[E5-36]**, and a
run that reached OUT by quoting *"a durable competitive advantage has proven elusive"* would
have been the lazy route the pre-registration at the head of this file was written to prevent.

**And note what [E4-56] does NOT say**, because reading it as a blanket prohibition would be
the same error in the other direction: it does not say every airline earns nothing, and it
records that Berkshire sold USAir *"for a hefty gain."* The claim is about the **advantage**,
not about any year's profit — which is exactly why this run had to build the Q2 case on
Delta's filings, and why Delta's genuinely excellent 16.1% return on unleveraged net tangible
operating assets is recorded at full strength beside it.

---
## DEFECTS FOUND — in the tools, in the brief, and in a prior run's working papers

**1. `Screens/floor_screen.py::level_shift()` — THE UAL RUN'S DEFECT 3 WAS ONLY HALF FIXED,
AND THE HALF THAT WAS APPLIED MAKES THE REMAINING HALF HARDER TO SEE.** The UAL run of
2026-09-02 reported that the function returns an uninterpretable value when the earlier-window
mean is near zero, and prescribed the fix in two parts: *"return `None` (or a distinct verdict)
when the earlier mean is negative **or when `abs(earlier)` is small relative to the series
dispersion.**"* The first part was implemented — the code now guards `if earlier <= 0` with two
worded verdicts and refuses the ratio. **The second part was not.** On DAL's nine-year
owner-earnings series at the capex end (2017-2025), the earlier window 2017-2022 contains
−5,811, −132 and −153 and its mean is **+$1.167M** — positive, so the guard passes — and the
function returns **`(2039.9999999999998, 'STEP UP - normalize down [E4-41]')`**. A ratio of two
thousand is presented with the same confident verdict string as a ratio of 1.7.
**A partially applied fix is worse than none, because the function now looks guarded.**
*Fix: after the `earlier <= 0` branch, refuse the ratio when `abs(earlier)` is small relative
to the dispersion of `vals` — e.g. `if abs(earlier) < 0.10 * statistics.pstdev(vals)` — or
whenever the early window itself contains a sign change. The worded-verdict pattern the
existing guard uses is already the right shape; it just needs the third branch.*

**2. `Screens/floor_screen.py::capital_acquired()` RETURNS ZERO FINANCE-LEASE ADDITIONS FOR
DELTA'S TWO MOST RECENT YEARS, AND NO FLAG FIRES — AND NO TAG-LIST FIX CAN REPAIR IT.**
`FINLEASE_TAGS = ["RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability"]`. Delta used
that element through FY2023 — 2018 $93M, 2019 $650M, 2020 $381M, **2021 $1,049M**, 2022 $91M,
2023 $31M — and then in FY2024 **re-tagged the line into its own namespace** as
`dal:RightOfUseAssetObtainedInExchangeForFinanceLeaseLiabilityReversal`, when the caption
changed from "acquired" to "acquired **or modified**". The FY2025 10-K's non-cash schedule
reports **$184M for 2025** and $(17)M for 2024; `capital_acquired()` returns **0** for both,
and `lease_capex_flag()` returns `None`, so nothing prompts a read.
**This is a strictly worse case than the UAL run's defect 5.** There, the right number sat
under a different *us-gaap* element and a tag-list change could have found it. Here the values
are in a **company-specific namespace that the SEC `companyfacts` API does not expose at all**
— Delta's `companyfacts` carries only `us-gaap`, `dei`, `ecd` and `ffd` — so **no tag list can
ever recover them.** The generalised rule the UAL run reached is now demonstrated twice and by
two different mechanisms: **read the supplemental non-cash schedule at the foot of the
cash-flow statement; a tag can only ever be a prompt.**
*Consequence for the published screen: `oe_bottom` of $1,137M rests on a five-year capex mean
that includes $1,049M of 2021 finance leases and zero for 2024 and 2025 — internally
inconsistent by construction.*

**3. THE PUBLISHED SPREAD UNDERSTATES THE WIDTH FOR A NINTH CONSECUTIVE RUN — AND HERE BY A
MECHANISM THE TOOL CANNOT IN PRINCIPLE SEE.** Published: bottom $1,137M, top $4,935M, spread
334%. Both reproduce **exactly** from `Screens/floor_screen.owner_earnings()`
(`5y_capex` = 1,136.8; `3y_da` = 4,935.0), so the screen is internally faithful. Rebuilt over
six windows, the as-filed capex-end bottom is **$625M (7-yr, 2019-2025) — 45% below the
published bottom** — because the published bottom is a five-year window and the seven- and
nine-year windows are worse. **And on the cash-tax-normalised basis the bottom is NEGATIVE
(−$190M), so the true range crosses zero and no spread percentage is defined at all.** The
tool cannot see this second axis because the cash-tax shield sits inside operating cash flow
in **every year of every window**; only the tax footnote and the MD&A reveal it, and the MD&A
sentence that reveals it (*"began making cash federal income tax payments"*) is prose, not a
tag. **A `current tax provision ÷ pre-tax income` line printed beside every owner-earnings
table would have flagged this filer at 1.15% in one glance, and it is a fetch-and-compute
addition that adds no judgment.** Offered as the one tooling suggestion this run makes.

**4. `da_annual()` WAS CHECKED FOR THE CERT DEFECT CLASS AND IS CLEAN FOR THIS FILER.** The
brief's correction 2 asked for the raw D&A series to be printed and eyeballed rather than
trusted. Printed: **1,511 / 1,523 / 1,565 / 1,658 / 1,771 / 1,835 / 1,902 / 2,235 / 2,329 /
2,581 / 2,312 / 1,998 / 2,107 / 2,341 / 2,513 / 2,443** for 2010-2025. Monotone to 2019, a
pandemic dip, and a recovery. **No discontinuity, no semantic break, largest step 20%.** The
check was run and it passed; recorded so that the next run knows it was actually performed.

**5. IN THE BRIEF — THE PENSION PRIOR IS REFUTED.** The instruction said *"Check the balance
sheet, the pension, and the debt maturity schedule."* The balance sheet and the maturities
repay the check. **The pension does not: Delta's defined-benefit pension is OVERFUNDED by
$2,258M** (obligation $15,022M, plan assets $17,280M) and *"Estimated funding by employer in
next fiscal year: **$5 million**."* The expected long-term return assumption of 6.96% is not
fanciful — the actual 2025 return was ~14.7%. The airline-pension-crisis prior is a 2005-era
fact about the industry and it is no longer true of this registrant. What *is* true, and is
the thing to check instead, is the **unfunded other-postretirement-and-postemployment
obligation of $3,217M** paying ~$489M of benefits a year, already inside operating cash flow.

**6. IN THE BRIEF — THE FLEET-PLAN LEAKAGE QUESTION, ANSWERED ITEM BY ITEM, AND ONE OF THE
THREE IS THE OPPOSITE OF WHAT WAS FEARED.**
- **Pre-delivery deposits are INSIDE reported capex.** Delta's cash-flow line reads *"Flight
  equipment, **including advance payments**."* No leakage. *(The brief's worry was reasonable
  and this filer does not have it.)*
- **Aircraft purchase commitments are outside and fully disclosed** — $15,430M by year, plus
  $6,030M of contract-carrier minimums and ~$11.2bn of other purchase obligations.
- **Sale-leasebacks are outside AND UNQUANTIFIED, and that is the real hole.** The MD&A says
  2025 "other, net" investing *"primarily included proceeds from several sale-leaseback
  transactions"* alongside two equity-stake disposals, inside a single **$589M** line, with no
  split. Sale-leasebacks reduce reported net investing outflow while the aircraft stays on the
  ramp under a lease — exactly what (c) needs to see. **This is a Delta disclosure gap, not a
  tooling gap, and it is the one place Delta's disclosure is worse than United's**, which
  quantified its sale-leaseback gain at $427M in a footnote.
- **A fourth item the brief did not name and should have: the two aircraft orders signed AFTER
  the balance-sheet date.** 30 Boeing 787-10 (2026-01-12) and 16 Airbus A330-900 plus 15
  A350-900 (2026-01-27), with options for 50 more, **and no dollar amount disclosed anywhere
  in the filing.** That is 61 firm widebodies added to a $15.4bn commitment book six weeks
  after the date the book was struck. It is the ORCL precedent — a contractual claim on future
  cash outside the disclosed total — arriving through a subsequent-events door rather than an
  uncommenced-lease one.

**7. IN THE BRIEF — THE REFINERY QUESTION, ANSWERED.** *"Decide whether it is part of the
business or a hedge, and whether it distorts owner earnings."* **It is part of the business
and the filing settles it**: Monroe is a **reportable operating segment** with its own revenue
($6,961M including intersegment), cost of goods sold ($6,259M), depreciation ($113M),
operating income ($157M), total assets ($2,552M) and capital expenditure ($68M). It is not a
hedge in any accounting sense. **It does NOT materially distort owner earnings** — $157M of
operating income is 2.7% of the total on 3.1% of assets, and $68M of capex is 1.5% of the
total. **It DOES severely distort the unit-revenue metrics**, which is why the [E4-55] test in
this run uses Delta's own *"TRASM, adjusted"* rather than as-filed TRASM: 21.26c against
19.56c in 2025 is a **1.70 cent gap, 8% of the metric**, and it is entirely third-party
refinery sales.

**8. A DEFECT IN A PRIOR RUN'S WORKING PAPERS, CORRECTED HERE.**
`Test Runs/_research 2026-09-02 UAL/units_series.md` records in section 6 that *"Delta adjusted
TRASM for 2019"* is *"Not disclosed in the FY2019 10-K"*, and caveat 2 concludes *"Delta is not
put on this line."* True of the FY2019 10-K; **false of the record.** Delta's **FY2021 10-K
(accession 0000027904-22-000003) discloses TRASM, adjusted = 16.97c and CASM-Ex = 10.88c for
2019** in its 2019 comparative column. Both series are therefore computable across the whole
2019-2025 window on Delta's own definitions, and both are used at Q2 above — the
refinery-adjusted real price series (−8.5%) and the real ex-fuel unit cost series (+1.2%).
**The generalisable lesson: a comparative column in a LATER filing is a source. "Not in the
filing where that year is primary" is not the same as "not disclosed", and the difference here
was one of the two decisive series in this run.**

**9. RESTATEMENT VARIANCE, DISCLOSED RATHER THAN SILENTLY RESOLVED.** `sources.annual()`
returns DAL FY2017 operating income of **$6,114M** on revenue of $41,244M (as originally
filed); the peer table's latest-filed comparative, after the ASC 606 full-retrospective
restatement, carries **$5,966M** on $41,138M. The Q2 real-operating-income table uses the
latter, for consistency with the six-carrier row. On the former, 2025 is **25.7%** below the
2017-2019 real mean instead of 23.8%. The conclusion does not move; the variance is recorded
because **[E4-38]** requires the window and the basis to be visible.

---
## ADDENDUM 2 — 2026-09-07, same session: FOUR CORRECTIONS TO THE TEXT ABOVE

*Operator rule 6: violations found later are corrected in an addendum, never by editing
history. All four were found in the closing arithmetic re-check; none changes a verdict, and
one of them is a factual error I made rather than a rounding difference.*

**1. Q3, the [E3-53] restructuring-charge flag: "none in the window" is WRONG.**
I wrote that there were no restructuring charges in the window. There were, and they are the
largest in Delta's history. The FY2021 10-K, accession 0000027904-22-000003, MD&A:

> *"During 2020, we recorded **restructuring charges of $8.2 billion** for items such as
> **fleet impairments and voluntary early retirement and separation programs** following
> strategic business decisions in response to the COVID-19 pandemic. In the year ended
> December 31, 2021, we recognized $19 million of adjustments to certain of those restructuring
> charges, representing changes in our estimates."*

The error was mechanical — the FY2025 10-K contains **zero** instances of the word
"restructuring", and I read that as the answer instead of reading the year the charge was
taken. **The correct reading, and it strengthens rather than weakens the file:**
- **[E5-33]** governs: the charges are real costs and belong in the owner-earnings mean —
  *"to tell owners year after year, 'Don't count this' … is misleading."* They **are** in the
  mean: 2020 sits in the eleven-year and nine-year windows at −$5,811M of owner earnings.
- The **cash** portion (severance under the voluntary programmes) is inside 2020's operating
  cash flow of −$3,793M. The **non-cash** portion (fleet impairments) is not, and correctly
  so — the cash for those airframes was spent in earlier years' capital expenditure, which
  **is** in the mean. That is why 2020 net income of −$12,385M is so much worse than 2020
  operating cash flow.
- **And the fleet-impairment half is Q4's (c) argument made concrete.** $8.2 billion of
  charges, most of it for aircraft Delta had bought and then retired early, is the filed proof
  that depreciation on this fleet was **not** tracking the economic consumption of it. It
  belongs beside the five reasons given at Q4 for why **[E5-20]** invalidates the D&A end, and
  it is the sixth.
- The flag itself does **not** fire as a *disclosure* flag under [E3-53] — the charge was
  disclosed in its own income-statement line, quantified by component, and the subsequent
  $19M estimate change was disclosed too, which is the candor case. But my statement of the
  facts was wrong and is corrected here.

**2. Q2, the [E2-53] and [E3-61] paragraphs: capacity growth in 2025 was +3.3%, not +3.2%.**
298,045 ÷ 288,394 − 1 = **+3.35%**. Delta's own MD&A rounds it to "+3%". The sentences read
"capacity +3.2%" and "Delta added 3.2% of capacity"; both should read **+3.3%**. No conclusion
moves.

**3. Q2, the Amex compound rate: 13.7%, not 13.6%.** ($8.2bn ÷ $2.0bn)^(1/11) − 1 = **13.7%**
on the stated endpoints (2014 and 2025). Recorded because a compound rate quoted to one decimal
should be right to one decimal.

**4. Q3, the primary test: the 2019 equity comparison mixed a year-end figure with an
average.** I wrote *"average equity of $8,844M in 2023 against $15,358M in 2019"*. $15,358M is
2019 **year-end** equity; the comparable 2019 **average** is (13,687 + 15,358) ÷ 2 =
**$14,523M**. On the correct like-for-like basis the 2023 denominator is **39% smaller** than
the 2019 one rather than 42% — **the point stands and the corrected figure is the one to
quote.**

**One source note, not a correction.** Q2 states that Delta's 2020 passenger revenue *"fell
70%"* while loyalty cash sales fell 31%. Sources: passenger revenue **$42,277M (2019)**, FY2019
10-K accession 0000027904-20-000004, and **$12,883M (2020)**, FY2021 10-K accession
0000027904-22-000003 comparative column — a fall of **69.5%**. Loyalty cash sales $4.2bn to
$2.9bn, Note 2 of the same filings, a fall of **31%**.

---
## ADDENDUM 3 — COMMIT PROVENANCE

*Recorded because the record should be readable, and reciprocating the note the concurrent
CRM run of the same day added to its own file.*

This run was written under the write-early protocol and committed gate by gate: `5ded372`
(Step 0), `8dba994` (Q1 and the units-series working paper), `82bd2b6` (Q2), `c62b779`
(Q3-Q6, self-audit, register), `4c8f6b8` (defects, addenda, ledger row E4-56, working papers).

**Two collisions with a concurrent CRM run in the same working tree, both benign and both
disclosed.** (1) Commit `c62b779`, which carries a DAL message, also swept in CRM's final two
edits; the CRM run has logged that from its side. (2) Commit `4c8f6b8`, which carries a DAL
message, also swept in an uncommitted edit to `Screens/floor_screen.py` — the new
`da_discontinuity_flag()` function written by that session after the CERT run. **No content was
lost or altered in either direction**, and `git add -A` in a shared working tree is the cause in
both. *(Run for completeness on this filer: `da_discontinuity_flag(DAL)` returns `None`, which
independently confirms the manual eyeball recorded at DEFECTS item 4.)*
