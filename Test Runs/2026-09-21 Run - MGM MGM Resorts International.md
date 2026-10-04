# Company Run - MGM Resorts International (MGM) - 2026-09-21
**Framework v4.1.** Governing document: `Framework/THE FRAMEWORK v4.md`. Where this
template and that document disagree, the document governs.

Fill top to bottom. **Stop at the first verdict that is not IN.**

---
## THE FOUR VERDICTS - every question returns exactly one

| | | |
|---|---|---|
| **IN** | evidence is here and it clears | continue |
| **OUT** | evidence is here and the business fails | **stop, permanent** |
| **UNRESEARCHED** | the evidence exists, I have not got it | **work order - not an answer** |
| **UNKNOWABLE** | evidence is in, the future is still indeterminate | **close without prejudice** |

**Ask aloud on every non-IN verdict: "Can I name the document that would resolve this?"**
YES → UNRESEARCHED, go and get it. NO → UNKNOWABLE, close it. **[E4-19]**

**A gate marked IN carrying "unverified", "general knowledge" or "provisional" is a
protocol violation - it is UNRESEARCHED.**

**No degree-of-difficulty credit.** If a verdict only holds after narrowing assumptions,
it is UNKNOWABLE. Gathering more evidence is legitimate; torturing the evidence you have
is not. **[E4-18]**

---
## STEP 0 - THE RATE, AND THE FILING

**Sovereign, for the currency the business EARNS in** - the currently observed rate, never
a forecast **[E4-15, E3-32]**:
- rate **5.34** % · date **2026-09-18** · source (issuing authority) **US Treasury daily par yield
  curve, 30 Yr column, CY2026 feed from home.treasury.gov. Struck fresh this run on 2026-09-21;
  the Friday 2026-09-18 row is the newest published. FRED DGS30 NOT used: it is the fallback,
  not the source (operator rule 5).**
- FX if the quote and the earnings differ in currency: **none needed for the quote, which is in
  USD. The earnings currency is mixed and that is recorded rather than smoothed: FY2025 net
  revenue was $12,411.6M United States, $4,464.1M China, $662.0M Other (10-K Note 17). The Macau
  pataca is pegged to the Hong Kong dollar, which is pegged to the US dollar, so the USD
  sovereign fits roughly 71% of revenue directly and the Macau leg by peg. The LeoVegas leg,
  3.8% of revenue and loss-making, is the part the USD rate does not fit.**

**The filing was read** - not tagged data **[E3-27, E4-14]**:
- [x] MD&A  [x] cash-flow statement incl. detail lines  [x] footnotes
- document · date · accession no.: **Form 10-K for FY2025, period ended 2025-12-31, filed
  2026-02-11, accession 0000789570-26-000018, primary document mgm-20251231.htm. Also read:
  Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-29, accession 0000789570-26-000076;
  Form 8-K of 2026-07-29 (Items 2.02, 9.01) accession 0000789570-26-000075 with EX-99.1;
  Form 8-K of 2026-04-07 (Items 1.01, 9.01) accession 0000789570-26-000029; Form 8-K of
  2026-05-14 (Items 1.01, 2.03, 9.01) accession 0001193125-26-224106; DEF 14A filed 2026-03-27,
  accession 0001193125-26-129074; and the FY2021 and FY2022 10-Ks for the pre-window cash flows.**
- figure cross-checked against the filed statement (say which): **three, each read off the filed
  statement rather than the tag. (1) Net cash provided by operating activities FY2025 =
  $2,529,378 thousand on the Consolidated Statements of Cash Flows, matching the tagged
  NetCashProvidedByUsedInOperatingActivities of $2,529.4M. (2) "Operating cash outflows from
  operating leases" FY2025 = $1,867,130 thousand in Note 11, which is the CASH rent, and it sits
  $391.3M BELOW the $2,258,405 thousand of "Triple net lease rent expense" in the Note 17
  reconciliation. Those are not the same number, and the gap is the subject of this run.
  (3) Total operating lease liabilities $25,068,747 thousand against total future minimum lease
  payments of $54,679,646 thousand, Note 11 maturity table.**

**THE PRICE, THE COUNT AND THE CAP - struck fresh, nothing inherited**
- price **$38.59** · date **2026-09-21** · source **Yahoo Finance chart endpoint via
  tools/sources.py price(). AGGREGATOR, and FLAGGED as such: permitted for live quotes only
  (operator rule 5). Intraday Monday quote.**
- share count **251,592,756** common shares, $0.01 par - read off the COVER of the latest
  periodic filing, the Form 10-Q for the quarter ended 2026-06-30, filed 2026-07-29,
  **accession 0000789570-26-000076**, via python Screens/cover_shares.py MGM.
- **ONE class.** The FY2025 balance sheet carries a single line: "Common stock, $0.01 par value:
  authorized 1,000,000,000 shares, issued and outstanding 258,323,143 and 294,374,189 shares".
  There is no second class to sum, so no charter question arises. The count has fallen 6.7M
  shares in the six and a half months between the two dates; that is the buyback, read at Q3.
- **market capitalisation = $38.59 × 251,592,756 = $9,709M.** The screen row of 2026-09-02
  carried $10,273M; the difference is the quote, not the count.
- *No split has occurred in this window, so the split-invariance correction is inert here.*

---
## Q1 - CAN I UNDERSTAND HOW THIS MAKES MONEY? **[E3-31]**
- Unit economics in my own words, no management language: **MGM sells time and space inside
  buildings it no longer owns. Four things are sold and the filed statement separates them: a
  house edge on wagers ($9,450.9M of casino revenue in FY2025, 53.9% of the total), hotel
  room-nights ($3,377.4M), food and drink ($3,046.0M), and entertainment, retail and other
  ($1,663.4M) - Consolidated Statements of Operations, FY2025 10-K. The casino take sets the
  rest: rooms and restaurants are priced off the traffic the gaming floor and the convention
  calendar bring, which is why Item 1 says "Our operating results are highly dependent on the
  volume of customers at our properties, which in turn affects the price we can charge for our
  hotel rooms and other amenities."**

  **Against that revenue sit four cost blocks a reader can name from the filed statements.
  Payroll: approximately 44,000 full-time and 18,000 part-time U.S. employees plus 16,000
  internationally, with collective bargaining agreements covering about 37,000 U.S. employees
  (Item 1). Gaming taxes: $3,119.9M across the four segments in FY2025 (Note 17), of which
  $1,969.0M is MGM China alone, where the concession carries a special gaming tax of 35% of gross
  gaming revenue plus a levy of up to 5% (Note 12). Depreciation and amortization: $1,017.8M.
  And RENT: $2,258.4M of triple net lease rent expense (Note 17 reconciliation), of which
  $1,867.1M was paid in cash in FY2025 (Note 11). The rent block is what makes this registrant a
  different animal from the company it was ten years ago, and it is a contractual, escalating,
  23-year-weighted-average obligation, not an operating cost management can flex.**

  **The structure the money passes through, from Note 1 and Note 2. MGM Resorts International is
  a Delaware holding company. It CONSOLIDATES (a) sixteen domestic casino resorts, (b)
  approximately 56% of MGM China Holdings Limited, separately listed in Hong Kong, whose
  subsidiary MGM Grand Paradise holds one of the six Macau gaming concessions, and (c) LeoVegas,
  the European online gaming subsidiary. It does NOT consolidate (d) BetMGM, the 50% North
  American online venture, because "the Company has joint control", (e) MGM Osaka, 50%, a VIE of
  which it is not the primary beneficiary, or (f) the Bellagio REIT Venture - its own landlord,
  in which it holds 5% and which is likewise a VIE it does not consolidate. So the reported
  revenue line contains Macau and LeoVegas in full and contains BetMGM and Osaka not at all;
  those two enter only through the single line "Income (loss) from unconsolidated affiliates",
  $69,982 thousand in FY2025 against $(90,653) thousand in FY2024. That answers the brief
  directly: the equity-method venture and the European online subsidiary sit INSIDE the reported
  numbers in one case and OUTSIDE them in the other, and the filing says which is which.**

- The scarce input this business controls: **the licence and the customer file - and NOT the
  land. This is the sharpest thing Q1 has to say about MGM, and it is a change of kind, not of
  degree. A gaming licence is scarce by statute: Macau has exactly six concessionaires (Item 1),
  and a Maryland, Massachusetts, Michigan, New Jersey, New York, Ohio or Mississippi licence is
  legislatively rationed. The customer file behind MGM Rewards is a real asset. But Las Vegas
  Strip frontage and every domestic regional site - the input that cannot be reproduced at any
  price - is now RENTED: "We lease the real estate assets of our domestic properties pursuant
  to triple net lease agreements" (Item 1, repeated in Note 1). The registrant sold the scarce
  input and signed a lease back on it. Item 1 calls this "an asset-light business model"; the
  balance sheet calls it a $25,068,747 thousand operating lease liability standing against
  $6,305,614 thousand of property and equipment, net.**

- Will the fundamentals look broadly the same in ten years? **Broadly yes, and this is the part
  that passes. People will still gamble, still hold conventions in Las Vegas, and still travel to
  Macau; the filing’s own description of the revenue engine would have been recognisable in 2005
  and is likely to be recognisable in 2035. Two dated edges are named in the documents rather
  than assumed: the Macau gaming concession EXPIRES in December 2032 (Note 12, with the Item 1
  risk list carrying the government’s rights to terminate without compensation in certain
  circumstances, to redeem from the eighth year on one year’s notice, or to refuse an extension),
  and the domestic master leases run 23 years on a weighted average with renewal options at the
  Company’s election (Note 11). Neither makes the business unintelligible. Both are read again at
  Q2 and Q4.**

- **The complexity is recorded, not waved through.** Four segments; a separately listed 56%
  subsidiary that took $315,010 thousand of FY2025 net income as noncontrolling interests against
  $205,862 thousand attributable to MGM’s own shareholders; two 50% ventures outside the
  consolidation; five master leases; and a $3.01 billion shortfall guarantee of the DEBT OF ITS
  OWN LANDLORD (Note 12). That is a complicated holding company. But **[E3-31]** asks whether the
  business is "relatively simple and stable in character" in how it makes money, and the
  money-making is simple: house edge, room nights, and a rent bill. The complexity is a
  MEASUREMENT problem - whose dollars are whose - and it is settled at Q4 where owner earnings
  are built. It is not dodged here.

- **VERDICT: [x] IN  [ ] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

## Q2 - IS IT A FRANCHISE? **[E3-03]**

### THE THREE CRITERIA, ONE AT A TIME

> a franchise is a product or service that "(1) is needed or desired; (2) is thought by its
> customers to have **no close substitute** and; (3) is not subject to price regulation."
> — **[E3-03]**, 1991 letter

- **(1) Needed or desired - [x] YES.** Gambling, Las Vegas rooms and convention space are
  wanted, and $17,537.7M of FY2025 net revenue is the evidence. Nothing here is in doubt.

- **(2) No close substitute - [ ] FAILS, and it fails on the registrant’s own words.** Item 1
  of the FY2025 10-K, under the heading "Customers and Competition", says: *"We operate in
  highly competitive environments. We compete against gaming companies, as well as other
  hospitality companies in the markets in which we operate, neighboring markets, and in other
  parts of the world, including non-gaming resort destinations such as Hawaii."* And then, of
  the segment that is 48% of revenue: *"Our Las Vegas Strip Resorts also compete, in part, with
  each other."* And of the entry threat: *"Major competitors, including newer entrants, have
  either recently expanded their hotel room capacity and convention space offerings, or have
  plans to expand their capacity or construct new resorts in Las Vegas."* A registrant naming
  Hawaii, its rivals, and its own properties as substitutes for its product is not describing a
  franchise under clause (2). It is describing the competitive hospitality business it says it
  is in.

- **(3) Not subject to price regulation - [x] PASSES IN FORM, but read the whole sentence.**
  Room rates and table minimums are not set by any regulator, so clause (3) is met as written.
  What the government takes instead is a share of the price: gaming taxes of $3,119.9M across
  the four segments in FY2025 (Note 17) - $1,969.0M at MGM China, where the concession carries
  *"a special gaming tax of 35% of gross gaming revenue and a special levy of up to 5% of gross
  gaming revenue"* (Note 12), $763.2M at Regional Operations against $2,772.7M of regional
  casino revenue (27.5%), $230.0M in Las Vegas, and $157.7M at MGM Digital. That is a tax, not a
  price control, and the criterion is not failed by it. It is recorded because it bounds what any
  pricing power could ever be worth here.

**Clause (2) is failed on filed evidence. Under the four verdicts that is OUT - "the evidence is
here and the business fails" - not UNRESEARCHED and not UNKNOWABLE.** The rest of this section
is the disconfirming work operator rule 9 requires, because OUT was my early hypothesis and
**[E4-26]** says to hunt hardest against the favourite. Everything below either strengthens the
finding or is the best case I could build for the other side.

### THE COMPETITOR ROW - REQUIRED **[E3-28]**

> "**I can’t be an intelligent owner of a business unless I know what all the other businesses
> in that industry are doing.**" — **[E3-28]**

**Seven comparators taken, all SEC registrants, every figure from the filer’s own 10-K or 20-F
via its own XBRL company facts, same metric, same five-year window.** Six are operators - Las
Vegas Sands (CIK 0001300514), Wynn Resorts (0001174922), Caesars Entertainment (0001590895),
Boyd Gaming (0000906553), PENN Entertainment (0000921738) and Melco Resorts (0001381640, a 20-F
filer) - and the seventh is VICI Properties (0001705696), the REIT landlord, which describes the
same buildings from the other side of the lease. **Buffett says eight; I took seven and say so.**

**Where the row is INCOMPLETE, and it is said rather than glossed [E3-28].** Macau has six
concessionaires. Four of them are inside this row (MGM China, Sands China through LVS, Wynn Macau
through WYNN, and Melco). **Galaxy Entertainment and SJM Holdings are Hong Kong listed and are not
SEC registrants, so no same-metric filing-sourced line exists for them here.** Fontainebleau Las
Vegas, which opened on the Strip in December 2023 and is part of the capacity story below, is
private and files nothing.

**A. OPERATING MARGIN - OperatingIncomeLoss ÷ Revenues, each filer’s own annual report**

| Company | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| **MGM (subject)** | **23.5%** | **11.0%** | **11.7%** | **8.6%** | **5.7%** |
| Las Vegas Sands | -16.3% | -19.3% | 22.3% | 21.3% | **21.6%** |
| Boyd Gaming | 26.7% | 27.6% | 24.1% | 23.6% | **18.3%** |
| Caesars | 15.3% | 16.1% | 21.4% | 20.5% | **16.2%** |
| Wynn Resorts | -10.5% | -2.7% | 12.9% | 15.9% | **15.7%** |
| Melco Resorts | -28.7% | -55.0% | 1.7% | 10.4% | **11.6%** |
| PENN Entertainment | 17.9% | 15.2% | -10.8% | 1.1% | **-9.7%** |

**MGM has the largest revenue in the group by a factor of 1.3 over the next name and the lowest
operating margin of every peer that is profitable at all.** And the direction is the finding:
23.5% → 11.0% → 11.7% → 8.6% → 5.7%, four declines in five years, while LVS, WYNN and MLCO each
recovered from the pandemic trough and CZR and BYD held double digits. **[E4-32]** makes direction
the primary criterion - *"the moat widened every year"* is *"the primary criterion of a great
business"* - and here it narrows every year.

**B. THE ROW BUILT SO AN OWNER AND A TENANT ARE ON ONE SCALE.** The A row is not a fair fight on
its own: LVS, WYNN, BYD and MLCO own their real estate and pay no rent, so their margins carry a
cost MGM has moved into a lease line. So the same peers are measured again on the return earned
on the real estate they USE, owned or rented: **(OperatingIncomeLoss + OperatingLeaseCost) ÷
(property and equipment net + operating lease right-of-use asset)**, every input from the same
filings.

| Company | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| **MGM (subject)** | **12.1%** | **11.5%** | **14.2%** | **12.8%** | **11.2%** |
| Boyd Gaming | 31.3% | 35.2% | 31.9% | 31.8% | **25.8%** |
| Las Vegas Sands | -5.7% | -6.7% | 20.2% | 20.1% | **24.2%** |
| Wynn Resorts | -4.1% | -0.9% | 10.1% | 13.8% | **13.5%** |
| Caesars | 9.6% | 11.4% | 16.1% | 14.9% | **12.4%** |
| Melco Resorts | -9.2% | -12.3% | 1.5% | 9.5% | **12.0%** |
| PENN Entertainment | 11.2% | 17.4% | -8.9% | 0.9% | **-8.8%** |

**On the fairer measure MGM is still last among the profitable names, and still falling.** The
asset-light transformation did not move it up this table; it moved the same weak return from an
owned balance sheet onto a rented one. **[E3-46]** asks the second question about the business as
a number - *"the best businesses, by definition, are going to be businesses that earn very high
returns on capital employed over time"* - and 11.2% and falling, against 24-26% at the two best
peers, is the answer.

**THE ROW’S OWN LIMIT, stated [E3-61].** Identical structures produce opposite outcomes: *"In some
businesses, the participants behave like a demented Kellogg. In other businesses, they don’t …
I think you’d have to know the people involved."* This row shows position. It cannot show conduct,
and nothing in it should be read as predicting how the Las Vegas operators will price next year.

### THE LANDLORD’S OWN FILING - the same buildings, read from the other side

VICI Properties’ FY2025 10-K (accession 0001705696-26-000034, filed 2026-02-25) says four things
about MGM that MGM’s own filing does not put in one place:

1. *"Caesars and MGM, our two largest tenants representing **39% and 35%**, respectively, of our
   annualized rent as of December 31, 2025"* - **the landlord of MGM’s Las Vegas and regional
   real estate is also, and slightly more so, the landlord of Caesars.** The scarce asset is
   rented to MGM and to MGM’s nearest domestic rival by the same owner.
2. *"Under our respective lease agreements with Caesars and MGM, they are obligated to pay us
   approximately **$1.3 billion and $1.1 billion**, respectively, in estimated annual lease
   payments for 2026."*
3. *"MGM has executed guaranties with respect to the MGM Master Lease and MGM Grand/Mandalay Bay
   Lease guaranteeing the prompt and complete payment and performance in full of all monetary
   obligations of the tenants"* - **the parent guarantees; there is no property-level
   ring-fence.**
4. *"a default by the applicable tenant … may cause a default under certain circumstances with
   regard to the **entire portfolio** covered by the respective lease agreements"* - **the master
   lease is cross-defaulted, so a weak property cannot be handed back on its own.**

And on the escalator, in the landlord’s words: *"under the MGM Master Lease, the escalator is
fixed at 2.0% for years two through ten of the MGM Master Lease and, for the remainder of the
term, the escalator is the greater of 2.0% and CPI, subject to a 3.0% cap."*

### THE REST OF THE Q2 TESTS

**[E4-37] THE INVERSE METRIC - the agony of a price increase.** *"you can almost measure the
strength of a business over time by the agony they go through in determining whether a price
increase can be sustained."* MGM’s filed price series for the Las Vegas Strip Resorts, from the
MD&A table:

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Occupancy | 93% | 94% | **92%** |
| Average daily rate | $256 | $260 | **$249** |
| RevPAR | $237 | $245 | **$229** |

**There is no agony here because there was no price increase: the price FELL 4.2% with 8% of the
rooms empty.** The MD&A says it plainly - *"Las Vegas Strip Resorts rooms revenue decreased 9% in
2025 compared to 2024 due primarily to a decrease in RevPAR."* The Q2 2026 earnings release
(EX-99.1, accession 0000789570-26-000075) carries it forward: ADR $242 against $252, RevPAR $224
against $235, both down 4%, occupancy flat at 93%. **[E2-44]**’s first characteristic - can it
raise prices *"even when product demand is flat and capacity is not fully utilized"* - is failed
on the filed series, twice, in consecutive reporting periods.

**[E4-55] WHERE UNITS EXIST, MONITOR UNITS - and this is where the headline separates from the
business.** The physical series for the Las Vegas Strip Resorts, from the same MD&A table
(dollars in millions):

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Table games drop | $6,215 | $6,028 | **$6,127** |
| Slot handle | $23,920 | $23,840 | **$24,565** |
| Table games win % | 26.3% | 24.4% | **25.2%** |

Table drop in 2025 is still **below its 2023 level**. Then the second quarter of 2026, from the
earnings release: **table games drop $1,523M against $1,554M, DOWN 2%; slot handle $5,915M against
$5,886M, flat; and casino revenue UP 17%** - because table games win % went from 22.9% to 29.6%.
The registrant itself defines that number in the 10-K as *"‘win’ or ‘hold’ percentage, which is
**not fully controllable by us**."* **The release’s second headline bullet is "Second consecutive
quarter of Las Vegas Strip Resorts year-over-year revenue growth", and the filed unit series says
that growth is hold, not volume, against falling price.** This is the shape **[E4-55]** names.
Its corpus row is Precision Steel, whose volume fell from 69 million pounds to 46 million while
price rises held dollar revenue level: *"This decline in physical volume is a serious reverse,
not likely to disappear in some 'bounce back' effect."* At MGM the dollar revenue is flattered by
hold rather than by price, which is the same disease with a different flatterer. *(The sentence
"Dollar revenue flattered by pricing is how a shrinking franchise hides; the physical series is
the honest one" is `THE FRAMEWORK v4.md`'s own commentary on [E4-55], not a corpus quotation, and
is not quoted here as one.)*

**[E3-33] and [E5-28] UNTAPPED PRICING POWER - NO.** The class requires *"a monopoly or a near
monopoly"* **[E5-28]**, and the claim would have to be supported by the row above. MGM is not
near-monopoly in any market it reports; it competes with itself on the Strip by its own
statement; and a business with untapped pricing power does not cut ADR 4% two periods running.

**[E2-45] THE ATTACKER’S TEST - how would I compete with ample capital?** The 10-K answers for
me: *"Major competitors, including newer entrants, have either recently expanded their hotel room
capacity and convention space offerings, or have plans to expand their capacity or construct new
resorts in Las Vegas."* Entry is capital-heavy and licence-gated, but it is demonstrably open, and
the capacity it adds lands on a market where the incumbent is already discounting.

**[E2-58] THE COMMODITY-END EQUATION.** *"persistent over-capacity without administered prices
(or costs) equals poor profitability"*, with long-term profitability set by *"the ratio of
supply-tight to supply-ample years"*. Las Vegas room capacity has risen through the window while
MGM’s ADR, occupancy and RevPAR all fell in FY2025 and again in Q2 2026. **[E2-58]**’s one
exception is *"a cost advantage that is both wide and sustainable"*, and MGM does not have one:
it has the group’s largest revenue and its lowest margin, which is the opposite shape.

**[E2-53] THE DOMINANCE CLASS - the strongest reading, and it fails here.** *"Once dominant, the
newspaper itself, not the marketplace, determines just how good or how bad the paper will be.
Good or bad, it will prosper."* MGM is the largest operator on the Las Vegas Strip by rooms and
by revenue. It is not prospering relative to smaller rivals: it earns 5.7% where Boyd, a quarter
its size, earns 18.3%. **Position is not setting the economics here, which is the direct test
[E2-53] proposes and the direct evidence against the dominance reading.**

**[E4-23] DOES IT REQUIRE A SUPERSTAR? NO - and that is recorded as a non-finding, not a
compliment.** Nothing in the filings makes the result turn on one named person, so no key-person
moat defect is recorded at Q2.

**[E4-04] MUST THE MOAT BE CONTINUOUSLY REBUILT?** The framework’s 2026-09-20 ruling applies
[E4-04] as a competence limit, never as a fourth franchise criterion, so it cannot be the ground
of this verdict and is not used as one. Recorded for the reader: the domestic position must be
**re-secured** at the end of a 23-year weighted-average lease term by exercising renewal options
at rents that will by then have compounded at 2% or more for a quarter of a century, and the
Macau leg must be re-secured at the **December 2032** expiry of a concession the government may
decline to extend (Note 12). Neither is a rebuild from zero; both are dated.

### THE BEST CASE FOR THE OTHER SIDE, built deliberately **[E4-26, E4-51]**

*"I’m not entitled to have an opinion unless I can state the arguments against my position better
than the people who are in opposition"* **[E4-51]**. The franchise case is:

- **Strip frontage is genuinely finite.** Bellagio, Aria, MGM Grand, Mandalay Bay and The
  Cosmopolitan occupy sites that cannot be reproduced. There is a real locational scarcity here.
- **Licences are statutorily rationed.** Six concessions in Macau; one licence per region in
  Maryland, Massachusetts, New York and Ohio. MGM Digital’s own Item 1 makes the argument:
  *"By operating in licensed markets, which are subject to costs in the form of gaming taxes, we
  benefit from higher barriers to entry."*
- **Regional Operations looks franchise-shaped.** FY2025 Segment Adjusted EBITDAR margin 30.8%,
  up from 30.7%, on revenue up 1%, with slot handle and table drop both higher.
- **Macau is growing.** MGM China main floor table games drop $12,115M → $14,681M → $15,836M over
  three years, and Segment Adjusted EBITDAR up 11% in FY2025.
- **MGM Rewards is a real asset**, and the loyalty database has switching friction.

**Why it does not carry, and the answer is the same in every bullet: MGM sold the thing that was
scarce.** The locational scarcity is real and it now belongs to VICI, to the Bellagio REIT
Venture and to the other landlords, who collect it as contractually escalating rent from MGM and
from Caesars alike. The licence scarcity is a **regime’s** property, not the company’s, which is
exactly what **[E2-59]** distinguishes: profit troubles in an over-supplied commodity business
*"may be escaped, true, if prices or costs are administered in some manner and thereby insulated
at least partially from normal market forces"* - and the row’s own example of that escape is
pricing *"until recently"* administered for truckers and for financial institutions’ deposit
costs, which is to say an escape the state can withdraw. Macau’s regime carries a stated end date
of December 2032. *(The phrases "the moat belongs to the regime" and "That day is gone" are,
respectively, `THE FRAMEWORK v4.md`’s own wording and a source line recorded in the [E2-59]
ledger row’s evolution notes rather than in its quote_verbatim; neither is quoted here as the
row.)* Regional Operations is a
genuine narrow moat in **21.5% of revenue** ($3,772.3M of $17,537.7M), rented from the same
landlord, and cannot carry the registrant. And Macau’s growth is 25.4% of revenue of which
**approximately 44% belongs to somebody else** - the noncontrolling interests that took $315.0M
of FY2025 net income against the $205.9M MGM’s own shareholders received.

### CORRECTION TO MY OWN ROW, MADE BEFORE THE VERDICT WAS FILED

**Found while building Q4, after row A above was written: MGM’s reported operating income in
2021, 2022, 2023 and 2025 each contains a large item that is not operating.** Row A is the same
metric for every filer and is left standing as computed, because changing one company’s
definition and not the others would be worse. But the 2021 and 2022 figures in particular must
not be read as trading margins, and the claim that the margin fell in four consecutive years -
which I would have written from row A alone - **is wrong.** **[E3-41]**: *"you must not fool
yourself, and you’re the easiest person to fool."*

From each year’s own filed reconciliation and Note 16:

| year | operating income as filed | what is in it that is not operating | operating margin as filed | **margin with those items removed** |
|---|---|---|---|---|
| 2021 | $2,278.7M | $1,562.3M gain on consolidation of CityCenter; $67.7M net property gain | 23.5% | **6.7%** |
| 2022 | $1,439.4M | $2,277.7M gain on REIT transactions; $1,037.0M property gain (The Mirage); less a **one-off $2.5bn** amortisation of the old Macau gaming concession on the change in its useful life | 11.0% | **4.8%** |
| 2023 | $1,891.5M | $398.8M gain on the sale of Gold Strike Tunica operations, net of $28.3M other property losses | 11.7% | **9.4%** |
| 2024 | $1,490.5M | $81.3M of property transaction losses | 8.6% | **9.1%** |
| 2025 | $1,001.8M | $278.9M goodwill impairment; $126.0M of property transaction losses | 5.7% | **8.0%** |

**The corrected series is 6.7%, 4.8%, 9.4%, 9.1%, 8.0% - a post-pandemic recovery to 2023 and
two declines since, inside a band of 4.8% to 9.4%.** It is not a four-year slide. **The Q2
verdict does not turn on the shape of that line and does not change**: on the corrected figures
MGM is still last among the profitable peers in every year of the window, against 15.7% to 21.6%
at LVS, BYD, CZR and WYNN in 2025, and the two most recent years still fall. **The peer rows were
NOT adjusted the same way**, so the 2021 and 2022 cross-section in row A is unreliable in both
directions; the 2023-2025 cross-section is the one that carries weight.

### CLASS AND DIRECTION

- **Class: [ ] WIDE [ ] NARROW [x] NONE at the registrant level [ ] PROVISIONAL.** Narrow in
  Regional Operations alone, which is 21.5% of revenue; none at the level of the thing whose
  shares are quoted.
- **Direction: NARROWING, on every filed series.** Operating margin down four years running;
  lease-adjusted return on real estate used down from 14.2% to 11.2% in two years; ADR, RevPAR
  and occupancy all down in FY2025 and ADR and RevPAR down again in Q2 2026; table drop in 2025
  below 2023 and down again in Q2 2026.

- **Can I name the document that would resolve this?** *The question does not arise: the evidence
  is IN.* Five years of same-metric peer data from seven registrants’ own annual reports, the
  registrant’s own description of its competition, its own price and unit series, and its
  landlord’s own filing all say the same thing. **This is not UNRESEARCHED (no missing document
  would change it) and not UNKNOWABLE (the future is not what is indeterminate - the present
  position is measured).**

- **VERDICT: [ ] IN  [x] OUT  [ ] UNRESEARCHED → ____  [ ] UNKNOWABLE → ____**

**THE FILE CLOSES HERE.** Everything recorded below Q2 is recorded, not governing. No verdict box
below this line is ticked, and no valuation output below carries entry language (operator rules 2
and 3).

## Q3 - ARE THEY HONEST, AND ARE THEY RATIONAL?
### RECORDED, NOT GOVERNING - the file closed at Q2. No verdict box below is ticked.
*Q3 is written out in full because the framework’s guardrail runs both ways: Q3 can stop a run and
can never start one, so a Q3 finding cannot rescue a Q2 OUT, and a clean Q3 cannot either. It is
recorded because the register and any future reader are owed what the filings actually say.*

**STEP 1 - THE WEIGHT CASE, DECLARED [E3-38, E1-16, E3-29].**
- [x] **Daily execution.** Yield management, marketing spend, credit extension to players, and
  hold are decided every day across 30 properties. **[E3-43]**’s original form governs: *"a
  business, unlike a franchise, can be killed by poor management"* - and Q2 found no franchise
  at the registrant level.
- [ ] Control. This is a public-market read, not a purchase of the whole thing.
- [x] **Leverage, and it is the lease.** At 2025-12-31 total liabilities were $38,097.5M against
  **$2,429.9M** of equity attributable to MGM’s own shareholders - 15.7 to 1 - of which
  $25,068.7M is the operating lease liability and $6,230.1M is debt. **[E3-52]** says read the
  terms, not just the quantity, and the terms run the wrong way from Berkshire’s float: these are
  covenanted (*"requires the Company to comply with certain financial covenants, which, if not
  met, would require the Company to maintain either cash security or one or more letters of
  credit in favor of the landlord in amounts ranging from six months to two years of rent"*,
  Note 11), dated, escalating, parent-guaranteed, and - per VICI’s own 10-K - cross-defaulted
  across the whole portfolio.

**Two of three ticked → Q3 would be a BINARY GATE here, and no price would compensate
[E1-16, E3-29, E5-35].**

**HONESTY - the binary [E5-16], each matter dated to when it became public.** No finding of
personal misconduct by management is present in the filings read. The one conduct-adjacent matter
is the **September 2023 cybersecurity incident** (10-K Note 12): consumer class actions in the
U.S. and Canada, settled for **$45 million** covering the 2023 and a 2019 incident, *"paid by
insurance carriers into a settlement fund in February 2025"*, judgment entered June 2025;
**investigations by state regulators continue** and the Company *"cannot predict the timing or
outcome."* **[E5-22] governs the reading: penalty size is not seriousness in either direction** -
the Wells Fargo error was reading a $185M fine as small, and the failure that counts is *"they
didn’t act when they learned."* The filings disclose the incident, the settlement, the insurer
funding and the open regulatory matters; nothing in them shows a failure to act on knowledge.
**No disqualifier found. That is the absence of found disqualifiers, not a finding that the
managers are honest [E5-17].**

**STEP 2 - THE FLAGS. Each is a prompt to read, never a verdict [E5-36, E5-38].**

- [x] **EBITDA / adjusted-earnings promotion - [E4-29], AND IT FIRES AT FULL STRENGTH. This is the
  sharpest thing in the file after the guarantor table.** *"Trumpeting EBITDA … is a particularly
  pernicious practice. Doing so implies that depreciation is not truly an expense, given that it
  is a ‘non-cash’ charge. That’s nonsense."* MGM does not merely trumpet EBITDA. **It trumpets
  EBITDAR - the same measure with the RENT taken out as well.** From Note 17 and repeated verbatim
  in the Q2 2026 earnings release: *"Segment Adjusted EBITDAR is a measure defined as earnings
  before interest and other non-operating income (expense), income taxes, depreciation and
  amortization, preopening and start-up expenses, property transactions, net, **triple net lease
  rent expense**, income (loss) from unconsolidated affiliates, goodwill impairment, and also
  excludes corporate expense and stock compensation expense."*
  **Quantified for FY2025: Segment Adjusted EBITDAR of $5,134.0M is struck before $1,017.8M of
  depreciation and amortization, $2,258.4M of triple net lease rent, $519.9M of corporate expense
  and $90.5M of stock compensation. Operating income was $1,001.8M.** The headline profit measure
  is 5.1 times the operating income, and the largest single thing it deletes is a **cash** cost
  that was paid in cash ($1,867.1M in FY2025, Note 11) and is contractually owed for 29 more
  years. **[E5-41]**’s inversion is doubly true here: depreciation is *"reverse float … you spend
  the money first and record the expense later"*, and rent is neither float nor reverse float -
  it is simply a bill, and EBITDAR deletes it.
  **The disclosure is technically correct and that is part of the finding**: because ASC 280 lets
  a registrant call its chief-operating-decision-maker measure the "reportable segment GAAP
  measure", MGM writes *"Segment Adjusted EBITDAR is our reportable segment GAAP measure"* - four
  times in the release. A reader who does not know Topic 280 reads the letters G-A-A-P next to a
  number struck before rent.

- [x] **Metric-switching - [E2-49], and it fires with its mitigations named.** *"Yardsticks seldom
  are discarded while yielding favorable readings. But when results deteriorate, most managers
  favor disposition of the yardstick rather than disposition of the manager."* From the DEF 14A
  filed 2026-03-27 (accession 0001193125-26-129074), **two yardsticks changed in the single year
  2025**: the Committee *"determined to remove Absolute TSR PSUs as a component of the long-term
  incentive program"*, and *"determined to modify the peer group for the Relative TSR PSUs … from
  the S&P 500 to the S&P 1500 Hotels, Restaurants and Leisure Index."* Removing absolute TSR
  removes the test that requires the share price to rise at all; moving from the S&P 500 to a
  sector index compares MGM with a set that moves with it. The stock closed 2021 at $44.88 and
  2025 at $36.49, so the changes did not follow favourable readings. **The mitigations are real
  and are stated rather than buried:** the change was announced in advance with the Committee’s
  reasons and its consultant named (F.W. Cook), and a guard survives - *"Funding capped at 100% of
  target if absolute TSR is negative, unless relative TSR is above the 75th percentile."* On
  [E2-49]’s own operational form (a switch announced ahead with reasons is the candor case), this
  sits between the two poles. It is recorded as fired, with the counter-evidence attached.

- [x] **What the pay actually vests on - [E4-27], read from the proxy.** *"Never, ever, think about
  something else when you should be thinking about the power of incentives."* From the DEF 14A:
  **75% of the annual bonus for the CEO, the CFO and the Chief Legal Officer turns on
  "Compensation Adjusted EBITDAR"** (50% for the digital president). That measure is EBITDAR -
  before rent - grossed up further by adding MGM China’s, BetMGM’s and Boa Lion’s *target*
  EBITDAR or EBITDA multiplied by MGM’s ownership percentage, and reduced by thirteen enumerated
  classes of exclusion including goodwill impairment, deal costs, and consequences of changes in
  tax law or accounting principles. The proxy states the target was *"consistent with the EBITDA
  approved by the Board in the budgeting process for 2025, **as further increased by the
  Company’s rental payments**."* **The rent is added back to the bonus target by name.** The 2025
  outturn was $4,304,248,000 and *"which resulted in each NEO receiving approximately 100% of their
  target award for this component of the bonus"* - in a year when consolidated operating income fell 33%, the guarantor
  group’s operating income fell 89%, and domestic operations lost $237.1M before tax. **The long
  term incentive is 50% relative-TSR PSUs and 50% time-vested RSUs, so no part of the pay package
  is measured after rent or after depreciation.**

- [x] **The cash-tax tell - [E4-30]. RECORDED WHETHER OR NOT IT FIRES, as the brief requires. It
  fires on the ratio, and the filing explains it, and the explanation is worse news than the
  flag.** Cash taxes paid as a share of reported pre-tax income: **23.4% (2023), 23.9% (2024),
  then MINUS 12.3% in 2025** (a net $34.6M refunded against $280.8M of pre-tax income). [E4-30]
  reads a falling cash-tax share as a fraud tell. Here Note 10 gives the mechanism outright and it
  is not fraud: **domestic operations produced a pre-tax LOSS of $(237,067) thousand in FY2025**,
  against $256,890 thousand in 2024 and $1,214,888 thousand in 2023, and the benefit is driven by
  a **$283.7M release of the federal deferred valuation allowance**. The tell led to the number
  that matters most in this file, which is what a prompt-to-read is for.

- [ ] **Weak accounting - DOES NOT FIRE, and the disclosure is better than most.** Stock
  compensation is expensed and disclosed ($90.5M in FY2025). The lease note gives cash rent,
  accounting rent, the maturity ladder, the escalators and the discount rate. Note 12 quantifies
  the Macau concession premiums, the investment commitment, the bank guarantees, the Bellagio
  shortfall guarantee and the Osaka funding. The Rule 13-01 guarantor table is given in full. **A
  reader who wants to know where the earnings are can find out from this filing**, which is the
  [E2-26] half-owner test and it passes.

- [ ] **Unintelligible footnotes - DOES NOT FIRE.**

- [ ] **Trumpeted earnings projections - DOES NOT FIRE [E4-22, E3-48, E5-30].** No numeric
  guidance appears in the Q2 2026 earnings release; the forward-looking language is qualitative.
  There is therefore no guidance record to set against outturn under **[E3-48]**, and the
  irreversible-ratchet warning of **[E5-30]** has not been triggered. **Recorded as a genuine
  positive.**

- [ ] **Serial share issuance - DOES NOT FIRE [E5-15]. The opposite happened**, and it is read
  under capital allocation below.

- [ ] **Dividends funded by issuance - DOES NOT FIRE [E2-52].** The dividend is suspended and the
  10-K says so in its own risk list: *"the fact that we suspended our payment of ongoing regular
  dividends to our stockholders, and may not elect to resume paying dividends in the foreseeable
  future or at all."*

- [x] **The except-for flag - [E2-57], in numeric form.** *"‘except for’ should be excised from
  the lexicon … you must count the runs scored against you in all nine innings."* The Q2 2026
  release reports GAAP diluted EPS of $1.11 against $0.18, a six-fold increase - and **Adjusted
  EPS of $0.59 against $0.79, a 25% DECREASE.** The gap is a $(1.13) per share property
  transactions gain (the sale of the MGM Northfield Park operations) partly offset by a $0.37
  goodwill impairment. Both directions are adjusted away, which is even-handed; but four separate
  non-GAAP measures now carry the narrative - Consolidated Adjusted EBITDA, Segment Adjusted
  EBITDAR, Same-Store Segment Adjusted EBITDAR and Adjusted EPS - and the reconciliations,
  though complete, are the ninth-inning problem [E2-57] names.

- [x] **The restructuring/impairment habit - [E3-53, E5-33].** Goodwill impairments of **$278.9M
  in FY2025** and **$111.0M in the second quarter of 2026** are excluded from Consolidated
  Adjusted EBITDA, from Segment Adjusted EBITDAR and from Compensation Adjusted EBITDAR. [E5-33]:
  *"to tell owners year after year, ‘Don’t count this’ … is misleading."* These are non-cash and so
  do not touch the owner-earnings construction at Q4; what they are is the delayed recognition of
  prices paid for businesses - the Regional Operations goodwill written down $256.1M in 2025 -
  and they belong in the reader’s judgment of the acquisitions, not out of it.

**FLAGS THAT CONVERGE ARE A DIFFERENT EVENT [E4-52].** The lollapalooza test asks whether several
flags point one way as a reinforcing system. Here three do, and they point the same way:
**the reported segment measure removes rent; the CEO’s bonus target removes rent and is then
increased BY the rent; and the equity awards are measured on share price alone.** Nothing in the
pay structure or the reported profit measure is computed after the $2,258.4M that the landlords
take. That is one system, not three prompts. **It is not a venality finding [E5-38]** - [E2-30]
governs: *"Institutional dynamics, not venality or stupidity, set businesses on these courses"* -
and the whole of the gaming industry reports EBITDAR. That it is an industry convention is the
[E2-30] point (4), peer behaviour mindlessly imitated, not a defence.

**STEP 3 - THE PRIMARY TEST [E2-01].** *"the achievement of a high earnings rate on equity capital
employed (without undue leverage, accounting gimmickry, etc.) and not the achievement of
consistent gains in earnings per share."* **The test cannot be run on book equity here and the
reason is [E2-47]’s own carve-out**, which excepts *"companies with unusual debt-equity ratios
or those with important assets carried at unrealistic balance sheet values."*
Equity attributable to MGM has been driven to $2,429.9M by $9,406.8M of buybacks over five years,
so a return on it is an artefact of the retirement, not a measure of the business. **[E2-43]’s
denominator is the one to use for an acquisitive, leveraged filer: unleveraged net tangible
assets, with the goodwill wedge reported separately.** At 2025-12-31 that is property and
equipment net $6,305.6M plus operating lease right-of-use assets $23,002.7M, against goodwill of
$4,902.0M and other intangibles of $1,356.7M reported separately. Clean operating income of
$1,406.7M on $29,308.3M of tangible operating assets is **4.8%**; the pre-rent version, the one
row B of the competitor table uses, is **11.2%**. Against LVS at 24.2% and BYD at 25.8% on the
identical construction.

**And the EPS series [E2-01] is defined against says the opposite of the business series, which is
exactly the situation the rule was written for.** Diluted EPS: $3.19 (2023), $2.40 (2024), $0.76
(2025) - falling. But per-share book, per-share revenue and per-share everything else were held up
by retiring 43% of the shares. The clean way to see it: **net income attributable to MGM fell from
$1,142.2M to $205.9M over two years while the share count fell 21%.** [E2-01] asks for the rate on
capital, and the rate on capital fell.

**THE HALF-OWNER TEST [E2-26] - PASSES, and it is the strongest thing on this page.** *"tell you
the business facts that we would want to know if our positions were reversed."* Three disclosures
carry it: the **Rule 13-01 guarantor summarized financial information**, which lets a reader see
that the note-guaranteeing domestic group earned $78.5M of operating income on $10,580.2M of
revenue; the **domestic/foreign split of pre-tax income** in Note 10, which shows the domestic
loss; and **Note 11’s separation of cash rent from accounting rent**. None of those three is in the
press release, and all three are in the 10-K. **The filing tells you what you would want to know.
The release does not, and the pay plan is computed on the release’s measure.**

**THE INSTITUTIONAL IMPERATIVE - SCORE ALL FOUR [E2-30].**
- [ ] **Resists any change in current direction** - no. The opposite: the company has re-made
  itself, selling the real estate of essentially every domestic property in six years.
- [x] **Projects or acquisitions materialise to soak up available funds** - yes, and it is
  measurable. $3,914.7M of acquisitions net of cash acquired in 2021-2024 (CityCenter’s remaining
  half, The Cosmopolitan operations, LeoVegas, Push Gaming), plus a **remaining JPY356.9 billion,
  about $2.3 billion, to fund MGM Osaka through 2028** for a resort opening in 2030, newly part
  financed by a JPY54.2 billion senior **secured** yen term loan taken in October and November
  2025 - in the year the domestic business lost money before tax.
- [ ] Staff studies produced to justify the leader’s craving - not visible from filings.
- [x] **Peer behaviour mindlessly imitated** - the asset-light sale-leaseback model and the EBITDAR
  reporting convention are industry-wide (Caesars with VICI, PENN with GLPI). [E2-30]’s fourth
  behaviour is the one that describes this best, and its last clause governs the reading: these are
  institutional dynamics, **not venality or stupidity**.

**CAPITAL ALLOCATION - THE BUYBACK CONDITIONS [E5-08, E4-31, E5-24, E5-31].**
- **(1) Ample funds for operational and liquidity needs? - QUESTIONABLE, and it is stated as a
  question.** In the five years 2021-2025 MGM spent **$9,406.8M** retiring stock while owing
  $1.8bn of cash rent a year, carrying $6.3bn of debt, committing $2.3bn more to Osaka, and
  guaranteeing $3.01bn of its Bellagio landlord’s debt maturing in 2029. **[E5-25]** shows what
  real compliance looks like - Berkshire published both conditions as numbers in advance, with a
  liquidity floor, because *"financial strength that is unquestionable takes precedence over all
  else."* MGM publishes no liquidity floor.
- **(2) Repurchases at a material discount to conservatively calculated intrinsic value? - NOT
  DEMONSTRATED, and the market has now supplied an unusually direct test.** $7,653.3M was spent in
  2022-2025 retiring 195.5M shares, an average of roughly **$39.15** a share. The stock closed at
  **$36.49** on 2025-12-31 and trades at **$38.59** today. Four years and $7.7 billion later, the
  price is where the buying was done. That is not proof the purchases were above value - price is
  not value - but it is the absence of any evidence that they were below it, which is what
  condition (2) requires the buyer to have had. **Stated with the humility clause [E4-13]:** this
  rests on our range, not theirs, *"it is natural for CEOs to be optimistic about their own
  businesses. They also know a whole lot more about them than I do."*
- **(3) The third condition, from the earliest full statement [E4-31] - MET.** *"Shareholders
  should have been supplied all the information they need for estimating that value."* The
  guarantor table, the lease note and the domestic/foreign tax split are all filed.
- **THE SCORED TEST [E3-54] - AND IT FAILS.** At least $1 of market value per $1 retained, five
  years rolling. Market capitalisation 2020-12-31: 494.3M shares × $31.51 = **$15,575M**.
  2025-12-31: 258.3M × $36.49 = **$9,426M**. Cash returned to shareholders over 2021-2025:
  **$9,406.8M** of repurchases (the dividend is suspended and was immaterial before that). So
  ending value plus cash returned is $18,833M against $15,575M five years earlier, a gain of
  $3,258M, against **$4,822.2M** of net income attributable to MGM retained over the same five
  years. **$0.68 of market value per $1 retained.** Prices are from an aggregator and flagged as
  such; the test is [E3-54]’s own, and it is carried with the published 2009 self-correction
  Buffett attached to it.

**THE CONTROL CONTEST - a Q3 fact, filed, and the screen’s deal check did not see it.** On
**2026-06-01**, People Incorporated (f/k/a IAC) filed a Schedule 13D/A on MGM attaching a letter
from **Barry Diller**, who sits on MGM’s own board, proposing *"to acquire all of the outstanding
shares of common stock of MGM not already owned by IAC, for 100% cash consideration of **$48.30
per share**."* The letter says the price *"represents a premium of 24.1% to the volume-weighted
average price … for the 30 trading days ending on May 29, 2026 … and a 10.6% premium to the most
recent closing price"* (MGM closed at $43.67 on 2026-05-29; $43.67 × 1.106 = $48.30, which ties).
On **2026-04-03**, three months earlier, MGM had signed a Voting Agreement with IAC and Mr Diller
(8-K filed 2026-04-07, accession 0000789570-26-000029) under which IAC and Mr Diller vote any
securities above **25.73%** of total voting power in proportion to the other shareholders, in
exchange for the right to designate two directors.
**Read at Q3 under [E2-68]:** the conduct that matters is conduct across an information asymmetry,
and the discloser here is the bidder, not the company. MGM has filed no board response, no 14D-9
and no merger agreement; the only company acknowledgement is one clause in the forward-looking
paragraph of the Q2 2026 release and one bullet in the 10-Q risk list. An EDGAR full-text search
of MGM’s filings for "People Incorporated" returns **exactly three documents, the latest dated
2026-07-29**, so the proposal stands unresolved as of this run. **What it does to the run: it makes
the $38.59 quote a number inside an unresolved control contest rather than a clean
owner-earnings price.** The stock closed at **$47.81 on 2026-06-30** - within 1% of the offer -
and at **$37.81 on 2026-09-18**. Whatever moved it, the quote today is 20.1% below a live cash
proposal from the holder of a quarter of the votes, and that is not a fact a valuation can ignore.
*This is the ROKU finding in a new form and it is written up as a tooling defect in the fold.*

**THE GUARDRAIL - checked before anything above is used.**
- [x] Confirmed: nothing in this Q3 is being used to promote the name. It could not be - the file
  closed at Q2 - and **[E2-37, E2-38, E3-39]** would forbid it anyway. *"a good managerial record
  … is far more a function of what business boat you get into than it is of how effectively you
  row."*
- [x] The business does not require a superstar; no key-person moat defect was recorded at Q2.
- [x] Is the franchise intact with a localised excisable cancer **[E2-35, E2-36]**? **No.** The
  thing Q2 found is not a local lesion a skilled surgeon removes. It is the rent, and the rent is
  a signed 25-to-30-year contract with escalators, parent guarantees and cross-defaults. That is
  the Pygmalion case, not the GEICO case.

- **VERDICT: NOT TAKEN. The file closed at Q2.** No box ticked.

## Q4 - WILL IT SURVIVE?
### RECORDED, NOT GOVERNING - the file closed at Q2. No verdict box below is ticked.

### THE PERIMETER - settled from the filings, in the framework’s own words

**The brief asked whether the consolidation perimeter is measurable, and it is. It is MEASURABLE,
and the instrument is the Rule 13-01 guarantor summarized financial information the registrant is
already required to file.** This is the BN-class answer, not the HHH/RGTI-class one, and it is not
"blocked".

What is consolidated that is not wholly MGM’s: **approximately 56% of MGM China**, separately
listed in Hong Kong, and **LeoVegas**. What is not consolidated at all: **BetMGM (50%)**, **MGM
Osaka (50% interest, an approximately 43.5% equity share after minority funding)** and the
**Bellagio REIT Venture (5%)** - all three VIEs or joint-control ventures per Note 2, entering the
income statement only through *"Income (loss) from unconsolidated affiliates"*.

**Three filed measures of how much of the consolidated numbers are not MGM’s:**

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Net income attributable to **noncontrolling interests** | $172.7M | $318.1M | **$315.0M** |
| Net income attributable to **MGM Resorts International** | $1,142.2M | $746.6M | **$205.9M** |
| Cash actually **distributed to noncontrolling interest owners** | $177.1M | $188.6M | **$169.2M** |

**In FY2025 the minority shareholders of a Hong Kong listed subsidiary had a larger claim on the
year’s profit than MGM’s own shareholders did - $315.0M against $205.9M.** The consolidated
operating cash flow of $2,529.4M is therefore not an MGM shareholder number, and two disclosed
adjustments bracket the leak: **$169.2M** (the cash that actually left, a floor, because
undistributed Macau cash sits behind another listed company’s board) and **$315.0M** (the economic
claim on the year’s earnings).

**And the guarantor table says where the earnings are, which is the finding of this run.** From
the 10-K MD&A, for the registrant combined with its wholly owned material domestic guarantor
subsidiaries - a group that **excludes MGM China, LeoVegas, BetMGM, MGM Grand Detroit, MGM
National Harbor and MGM Springfield**, and **includes all nine Las Vegas Strip resorts**:

| | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| Net revenues | $10,783.2M | $10,825.1M | **$10,580.2M** | $5,430.2M |
| **Operating income** | **$1,324.6M** | **$733.7M** | **$78.5M** | $665.1M |
| Net income attributable to MGM Resorts International | - | - | $246.4M | $364.9M |

**The domestic group that guarantees the notes earned $78.5 million of operating income on $10.6
billion of revenue in FY2025 - a 0.74% margin - having earned $1,324.6 million two years
earlier on 1.9% more revenue.** The FY2025 and H1 2026 figures carry one-off items I cannot
allocate to the group precisely, so the bound is stated both ways: **even if every consolidated
special is assigned to the guarantor group** (the $278.9M goodwill impairment and $126.0M of
property transaction losses in 2025; the $370.5M net gain in 2023; the $81.3M loss in 2024), the
series reads approximately **$954M → $815M → $483M**, a 49% fall in two years on revenue that
fell. H1 2026’s $665.1M contains a gain of about $272.5M on the Northfield Park sale and a
$111.0M impairment; net of both it annualises near the FY2025 adjusted level, not the FY2023 one.

**Note 10 says the same thing in one line, and it is the plainest sentence in the filing.**
Income before income taxes, by origin:

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Domestic operations** | $1,214.9M | $256.9M | **$(237.1)M** |
| Foreign operations | $257.9M | $860.2M | **$517.8M** |

**In FY2025 the entire pre-tax income of MGM Resorts International came from abroad, and roughly
44% of the Macau part of it belongs to somebody else.** The domestic business - the Las Vegas
Strip and the regional casinos, which is what a buyer of this share thinks they are buying - lost
$237.1M before tax.

**The stock-consideration limit does not bind here (resume state section 5, first bullet), and it
is checked rather than assumed.** Every acquisition in the window was paid in cash: $1,789.6M
(2021, the remaining half of CityCenter), $1,889.1M (2022, The Cosmopolitan operations and
LeoVegas), $122.1M (2023, Push Gaming), $113.9M (2024) - **$3,914.7M, which reproduces the
screen’s $3,915M acquisition note to the dollar and confirms it is the 2021-2024 investing-cash
line, 40.3% of today’s $9,709M market capitalisation.** The screen’s warning - that the numerator
and the denominator may be different companies - is correct and is worse than it looks, because
the perimeter moved in **both** directions: in came CityCenter (2021), The Cosmopolitan and
LeoVegas (2022) and Push Gaming (2023); out went **The Mirage** operations (December 2022,
$1,054.3M proceeds, $90M of annual rent removed from the VICI lease), **Gold Strike Tunica**
(February 2023, $460.4M, $40M of rent removed) and **MGM Northfield Park** (agreed October 2025 at
$546M, closed in the second quarter of 2026, $53M of rent removed). **The FY2021 owner-earnings
figure and the FY2025 one are not measurements of the same company.**

### SBC RESOLVES AND IS COMPLETE - checked before any band was used

**The BE failure mode (a silent zero) and the Boeing failure mode (SBC under a tag no SBC element
contains) were both tested for.** The undimensioned `ShareBasedCompensation` cash-flow add-back
resolves for **every one of the 18 filed years, 2008 through 2025**, with no gaps:
$36.3M, $36.6M, $35.0M, $39.7M, $39.6M, $32.3M, $37.3M, $42.9M, $55.5M, $62.5M, $70.2M, $88.8M,
$107.0M, $65.2M, $71.3M, $73.6M, $80.2M, $90.5M. Cross-checked against the filed FY2025 cash-flow
statement: *"Stock-based compensation | 90,471"*. **SBC is COMPLETE. No year is silently
subtracting zero.** SBC is 3.6% of FY2025 operating cash flow, well under the 50% threshold at
which the resume state says to read the grant table by hand, so **[E3-70]**’s market-value
measure is noted as the stricter standard and the reported charge is used as its floor.

### THE SPREAD, REBUILT OVER EVERY WINDOW AND EVERY (c) END **[E4-25, E4-38]**

*The screen’s `spread_caveat` said the published band was a four-construction width that "CANNOT
see variation older than the 5-year window; rebuild it [E4-25]". Rebuilt below over eleven windows
and three (c) ends, 2008 to 2025.*

**Why there are THREE (c) ends here and not two - this is the `da_note` resolved.** The screen
flagged *"D&A steps 4.3x at 2023-12-31 - READ Note 1 and the cash-flow statement"*. Read: the step
is a step **DOWN**, from $3,482.1M in FY2022 to $814.1M in FY2023, and the FY2022 10-K states the
cause in its own MD&A - *"Depreciation and amortization expense increased $2.3 billion compared to
the prior year period, due primarily to an increase of **$2.5 billion in amortization expense of
the MGM Grand Paradise gaming concession as a result of the change in its useful life**"* - with
Note 7 of that filing confirming *"Amortization expense related to intangible assets was $2.7
billion, $197 million and $194 million for 2022, 2021, and 2020, respectively."* **That is the
write-off of a purchased Macau sub-concession on the day a new concession replaced it. It is not
depreciation of anything MGM must renew.** Using **[E3-44]**’s D&A default for (c) in 2022 would
charge $2.5bn of licence runoff as required capital spending. **This is the class of filer the
resume state warns about, where the corpus’s own default runs the wrong way, and only a reader
sees it.** So a third end is built: **(c) = depreciation only**, D&A less intangible amortisation.

**OWNER EARNINGS BY YEAR, $M** - operating cash flow, less SBC, less (c). Eighteen filed years.

| year | OCF | SBC | (c)=D&A | (c)=depr only | (c)=capex | **OE(D&A)** | **OE(depr)** | **OE(capex)** |
|---|---|---|---|---|---|---|---|---|
| 2008 | 753.0 | 36.3 | 778.2 | - | 781.8 | **-61.5** | - | **-65.0** |
| 2009 | 587.9 | 36.6 | 689.3 | - | 136.8 | **-137.9** | - | **414.5** |
| 2010 | 504.0 | 35.0 | 633.4 | 632.4 | 207.5 | **-164.4** | **-163.4** | **261.5** |
| 2011 | 675.1 | 39.7 | 817.1 | 636.1 | 301.2 | **-181.7** | **-0.7** | **334.2** |
| 2012 | 909.4 | 39.6 | 927.7 | 606.7 | 422.8 | **-57.9** | **263.1** | **447.0** |
| 2013 | 1310.4 | 32.3 | 849.2 | 606.2 | 562.1 | **428.9** | **671.9** | **716.0** |
| 2014 | 1130.7 | 37.3 | 815.8 | 583.8 | 872.0 | **277.6** | **509.6** | **221.4** |
| 2015 | 1005.1 | 42.9 | 819.9 | 620.9 | 1466.8 | **142.3** | **341.3** | **-504.6** |
| 2016 | 1534.0 | 55.5 | 849.5 | 669.5 | 2262.5 | **629.0** | **809.0** | **-784.0** |
| 2017 | 2206.4 | 62.5 | 993.5 | 820.5 | 1864.1 | **1150.4** | **1323.4** | **279.8** |
| 2018 | 1722.5 | 70.2 | 1178.0 | 1002.0 | 1486.8 | **474.3** | **650.3** | **165.5** |
| 2019 | 1810.4 | 88.8 | 1304.6 | 1112.6 | 739.0 | **416.9** | **608.9** | **982.6** |
| 2020 | -1493.0 | 107.0 | 1210.6 | 1016.6 | 270.6 | **-2810.6** | **-2616.6** | **-1870.6** |
| 2021 | 1373.4 | 65.2 | 1150.6 | 953.6 | 490.7 | **157.6** | **354.6** | **817.5** |
| 2022 | 1756.5 | 71.3 | 3482.1 | 782.1 | 765.1 | **-1796.9** | **903.1** | **920.1** |
| 2023 | 2690.8 | 73.6 | 814.1 | 711.1 | 931.8 | **1803.0** | **1906.0** | **1685.4** |
| 2024 | 2362.5 | 80.2 | 831.1 | 712.1 | 1150.6 | **1451.2** | **1570.2** | **1131.7** |
| 2025 | 2529.4 | 90.5 | 1017.8 | 878.8 | 1068.9 | **1421.1** | **1560.1** | **1370.0** |

**EVERY WINDOW, MEAN OWNER EARNINGS, $M.** *[E4-38]: publish every window, because
"growth-rate presentations can be significantly distorted by a calculated selection of either
initial or terminal dates."*

| window | n | mean OE, (c)=D&A | mean OE, (c)=depr only | mean OE, (c)=capex |
|---|---|---|---|---|
| 2023-2025 | 3 | **1,558.4** | 1,678.8 | 1,395.7 |
| 2022-2025 | 4 | 719.6 | 1,484.9 | 1,276.8 |
| **2021-2025 (the five-year default [E2-42])** | **5** | **607.2** | **1,258.8** | **1,184.9** |
| 2020-2025 | 6 | **37.6** | 612.9 | 675.7 |
| 2019-2025 | 7 | 91.8 | 612.3 | 719.5 |
| 2018-2025 | 8 | 139.6 | 617.1 | 650.3 |
| 2017-2025 | 9 | 251.9 | 695.6 | 609.1 |
| 2016-2025 | 10 | 289.6 | 706.9 | 469.8 |
| 2014-2025 | 12 | 276.3 | 660.0 | 367.9 |
| 2011-2025 | 15 | 233.7 | 590.3 | 394.1 |
| **2008-2025 (the whole filed record)** | **18** | **174.5** | 543.2 | 362.4 |
| 2015-2019 (five years, pre-COVID) | 5 | 562.6 | 746.6 | **27.9** |

- **Short-window mean** (2023-2025, (c)=depr only): **$1,678.8M**
- **Long-window mean** (2008-2025, (c)=D&A): **$37.6M is the floor across all windows (2020-2025);
  $174.5M over the full eighteen years**
- **Combined range, window spread × capex band: about $40M to about $1,680M.** The screen’s
  published band was $607M to $1,558M; **those reproduce exactly as the 2021-2025 and 2023-2025
  means at the (c)=D&A end, and the rebuild shows the true width is roughly 42 times wider at the
  bottom than the published one.** The `spread_caveat` was right and understated.
- **Is that range too wide to reach a conclusion? YES, and under [E4-25] that IS the conclusion:**
  *"Usually, the range must be so wide that no useful conclusion can be reached."* A band whose
  bottom is $40M and whose top is $1,680M against a $9,709M market capitalisation spans a yield of
  0.4% to 17.3%. Nothing can be ranked on that.
- **The wide spread is a Q4 finding in its own right [E5-11], and the distorted years are named,
  not hidden.** **FY2020** is the pandemic: operating cash flow of **minus $1,493.0M**, with
  accounts payable and accrued liabilities alone taking **minus $1,383.0M** out as the properties
  closed. **FY2021** is the rebound of that same line, **plus $442.6M**, which is 32.2% of the
  year’s $1,373.4M of operating cash - **this is exactly the screen’s `wc_note`, and it
  reproduces to the dollar from the filed FY2021 cash-flow statement.** Read against Note 8, the
  cause is visible: casino front money went from $133.1M to $206.2M and advance deposits and
  ticket sales from $123.1M to $283.2M as the resorts reopened. **It is neither the DELL shape
  (a payables stretch) nor the INOD shape (a customer prepayment); it is a COVID reopening swing,
  and it is genuinely non-repeating.** The two years are a matched pair: FY2020 understates by
  roughly $1.4bn and FY2021 overstates by roughly $0.4bn.
- **THE DISCLOSED WINDOW JUDGMENT, made in the open as the brief requires.** I do not pick one.
  **All eleven windows are published above**, which is [E4-38]’s own remedy. If a reader wants one
  sentence: the three years since the lease set was completed and the Macau concession reset
  (2023-2025) give $1,396M to $1,679M; the five-year default window [E2-42] gives $607M to
  $1,259M; and the full eighteen-year record gives $175M to $543M. **The spread between them is
  not noise to be resolved - it is the answer.** And the normalisation runs DOWN, not up
  **[E4-41]**: FY2025 operating cash flow was helped by a tax refund (cash taxes were **minus
  $34.6M**), and Q2 2026 Las Vegas casino revenue was helped by a table hold of 29.6% against
  22.9%, a number the registrant itself says is *"not fully controllable by us."*
- **And every figure above is BEFORE the minority leak.** Deduct the FY2025 noncontrolling
  interests’ claim of $315.0M and the 2023-2025 mean falls from $1,678.8M to about $1,364M; deduct
  only the cash that actually left, $169.2M, and it falls to about $1,510M.

### MAINTENANCE CAPEX - THE (c) JUDGMENT, DISCLOSED **[E2-23, E3-44, E2-41, E5-20]**

*"(c) must be a guess - and one sometimes very difficult to make."* **[E2-09, E2-23]**. Here is the
guess and its grounds.

- **The D&A-as-filed end is INVALID for this filer in at least one year and unreliable in the
  rest**, for the reason set out above: FY2022’s $3,482.1M contains $2.7bn of intangible
  amortisation, of which about $2.5bn is a single Macau concession write-off. A (c) that swings
  4.3x on a licence replacement is not measuring what **[E2-23]** calls the amount
  *"that the business requires to fully maintain its long-term competitive position and its unit
  volume."*
- **(c) is judged UPWARD, toward total capex, and there are three filed reasons.** First,
  **[E5-20]**’s exception class asks whether the business’s own filing says depreciation
  understates renewal, and MGM’s does so contractually: each triple net lease obligates the
  Company *"to spend a specified percentage of net revenues at the properties on capital
  expenditures"* (Note 11). **Capex here is not discretionary; it is a lease covenant.** Second,
  the record: capex exceeded depreciation-only in each of the last three years - $931.8M against
  $711.1M (2023), $1,150.6M against $712.1M (2024), $1,068.9M against $878.8M (2025). Third, the
  guidance-free but specific forward statement in the MD&A: *"We have planned capital
  expenditures in 2026 of approximately $950 million to $1.05 billion on a consolidated basis."*
  On flat revenue, that is a renewal rate, not a growth rate.
- **Band used: (c) between $878.8M (depreciation only, FY2025) and $1,068.9M (total capex,
  FY2025), and the honest point inside it sits nearer the capex end.** Rooms and casino floors
  are a renewal business; the MD&A attributes FY2025 capex to *"room remodels, casino floor
  remodels and equipment, and information technology"*, every item of which is maintenance in
  substance.
- **Stock compensation subtracted in full [E5-06]:** yes, every year, $90.5M in FY2025. Not
  added back, not netted, not thresholded.
- **The working-capital increment [E2-23] constraint 3:** included, because the construction
  starts from operating cash flow, which nets the change from one audited line. The 2020 and 2021
  swings above are that line doing its work.
- **[E2-60]’s third dimension - financial strength - and it bites.** Restricted earnings are
  those whose payout costs the business *"its ability to maintain … its financial strength"*; the
  rule that a payout funded by rising leverage means (c) was understated is `THE FRAMEWORK
  v4.md`’s reading of that row, and is applied here as such rather than quoted as corpus. MGM returned $9,406.8M to
  shareholders over 2021-2025 while cash fell from $4,703.1M to $2,063.0M and while signing a new
  secured yen term loan. **Part of the payout was funded by asset sales and by the balance sheet,
  not by earnings, which is [E2-60]’s own definition of the problem.**

### GREAT, GOOD, OR GRUESOME? **[E4-20]**

- [ ] great · [ ] good · **[x] GRUESOME, at the registrant level**

*"The worst sort of business is one that grows rapidly, requires significant capital to engender
the growth, and then earns little or no money … Investors have poured money into a bottomless
pit, attracted by growth when they should have been repelled by it."* The filed arithmetic:
**revenue grew 81% from $9,680.1M (2021) to $17,537.7M (2025)**; the growth consumed **$3,914.7M
of acquisitions plus $5,406.1M of capital expenditure** over the same five years, roughly $9.3bn;
and at the end of it **net income attributable to MGM’s own shareholders was $205.9M, domestic
operations lost $237.1M before tax, and the guarantor group’s operating income was $78.5M.**
**[E4-43] is applied honestly and does not rescue it:** the *good* class passes when capital-hungry
growth still earns a satisfactory return - *"nothing shabby about earning $82 million pre-tax on
$400 million of net tangible assets"*, which is 20.5%. MGM’s clean operating income of $1,406.7M
on $29,308.3M of tangible operating assets is **4.8%**, and the domestic half of it is negative.
**[E5-40]**’s benchmark for a satisfactory return on retention is about 12%. This is not that.

### STAYING POWER - SCORE ALL THREE **[E5-11]**, at 2026-06-30 where possible

- **(1) A large and reliable stream of earnings - PARTIAL, and the reliable part is not MGM’s.**
  $17.5bn of revenue is large. But FY2025 pre-tax income was $280.8M, all of it foreign;
  the domestic leg lost money; the segment that grew, MGM China, is 56% owned; and MGM Digital has
  lost money every year and is losing more - Segment Adjusted EBITDAR of $(32.4)M, $(77.2)M and
  $(90.3)M in 2023, 2024 and 2025, with a further $(31)M in the second quarter of 2026 alone.
- **(2) Massive liquid assets - NO, on the scale of the obligations.** Cash and equivalents of
  **$2,547.4M at 2026-06-30** ($2,063.0M at 2025-12-31, *"of which MGM China held $565 million"*),
  against $1,878.8M of operating lease payments due in the next twelve months alone. The
  $2.3 billion revolver was undrawn at 2025-12-31, which is real - but **[E5-39]** is explicit that bank lines are
  not counted: *"We will never be dependent on the kindness of strangers … we don’t count on bank
  lines. You know, we don’t count on … we don’t count on anything."* *(The often-repeated "cash is
  a lot like oxygen" is in the [E5-39] ledger row’s concept and evolution-notes fields, not in its
  quote_verbatim, and the source line it records reads "available cash **or credit** is a lot like
  oxygen"; it is therefore not quoted here.)*
- **(3) NO SIGNIFICANT NEAR-TERM CASH REQUIREMENTS - FAILS, and it fails by the widest margin of
  the three. [E5-11] says of it: *"Ignoring that last necessity is what usually leads companies to
  experience unexpected problems."***
  Named and quantified from the filings, for the twelve months from 2025-12-31:
  - **$1,878.8M of operating lease payments** (Note 11 maturity table), rising every year, to
    $2,010.2M by 2030 and **$54,679.6M in total undiscounted**;
  - **$89.2M of finance lease payments**;
  - **$1,150M of debt maturing in 2026** ($750M MGM China 5.875% notes, $400M parent 4.625% notes);
  - **approximately $350M of consolidated cash interest** in 2026 (MD&A), $210M of it excluding
    MGM China;
  - **$950M to $1,050M of planned capital expenditure** in 2026 (MD&A), part of it obliged by the
    lease covenants;
  - **approximately $269M a year of Macau concession premiums** through 2030 plus **$540M**
    thereafter to the December 2032 expiry, and **$19M a year** for the reverted gaming assets
    (Note 12);
  - **a remaining $2.3 billion of MGM Osaka funding**, to be paid *"on a quarterly basis through
    2028"* for a resort that opens in 2030 and earns nothing before then;
  - **MOP19.7 billion (about $2.5 billion) of committed gaming and non-gaming investment** over
    the ten-year Macau concession, of which MOP18 billion is designated for non-gaming projects.
  Against a consolidated operating cash flow of **$2,529.4M**, of which the domestic guarantor
  group generated the part that pays the $1.8bn of rent, and **that group’s operating income was
  $78.5M.**
- **Leverage, named and quantified - there is no ratio ceiling in this framework and none is
  imposed.** $6,230.1M of debt, net, plus $25,068.7M of operating lease liabilities and $255.0M of
  finance lease liabilities, against $2,429.9M of equity attributable to MGM at 2025-12-31.
  **[E2-54]’s coverage test is the one the corpus supplies**, and it is the right one here because
  it is built to defeat exactly the measure MGM reports: *"whenever someone creates a capital
  structure that does not allow all interest, both payable and accrued, to be comfortably met out
  of current cash flow **net of ample capital expenditures** - zip up your wallet."* Run it on the
  FY2025 filed figures: operating cash flow $2,529.4M, less capex $1,068.9M, leaves $1,460.5M
  against $389.1M of interest paid - **3.75 times, and comfortable**. Run it with the rent
  restored to where [E2-54] would put a fixed, cross-defaulted, parent-guaranteed 29-year
  obligation - that is, treat the $1,867.1M of cash rent as the financing charge it economically
  is - and the numerator becomes $1,460.5M + $1,867.1M = $3,327.6M against $2,256.2M of rent plus
  interest: **1.47 times.** **The framework does not supply a threshold and none is invented. The
  two numbers are reported and the reader is told which convention produced each.**
- **[E3-66] jurisdiction:** the registrant is a Delaware corporation and the US system is the one
  **[E3-66]** calls *"especially favorable to shareholder interests"*. But **44% of the only
  profitable leg sits inside a Hong Kong listed subsidiary operating under a Macau government
  concession**, where MGM’s shareholders stand behind MGM China’s own minority holders, MGM
  China’s own creditors, and a concession the government may decline to extend. That queue is
  stated because [E3-66] says a non-US exposure must state where its shareholders stand in it.

### THE SPECIFIC WAY THIS BUSINESS DIES **[E2-27, E3-24, E4-40, E4-51]**

**SHAPE #13, THE TENANT, is the mechanism - with SHAPE #1, CONTRACTED NOT TO STOP, as its
feature.** The index is the authority on the numbering and #13 was KEPT on 2026-09-20 on rows
[E3-79, E3-03]; its one-line mechanism is *"the only product is rented non-exclusively from a few
owners who rent it to every rival and reset the rent at each renewal."* **It fits, with one
honest amendment stated rather than glossed: MGM’s rent is not reset at renewal, it is escalated
by contract at 2% a year, floored at 2% and capped at 3% after year ten or fifteen depending on
the lease.** That difference cuts both ways - it protects MGM from a market reset, and it removes
any possibility that the rent falls when the business does. **No new shape is proposed.** The
non-exclusivity is established from the landlord’s own filing rather than inferred: VICI’s FY2025
10-K says Caesars and MGM are *"our two largest tenants representing 39% and 35%, respectively, of
our annualized rent"*, and the Bellagio landlord is a venture in which MGM holds 5%.

**THE MECHANISM, IN ONE SENTENCE.** MGM sold the only asset in its business that could not be
reproduced, kept the operations, and signed contracts obliging it to pay a rising real price for
the use of what it used to own - so any decline in the revenue the buildings produce lands
entirely on the shareholders’ residual, which is already thin, while the landlord’s claim rises 2%
a year whatever happens.

**QUANTIFIED FROM FILED FIGURES, in the corpus’s own form [E3-24] - "Consider some mathematics".**
- The domestic guarantor group earned **$78.5M** of operating income on $10,580.2M of revenue in
  FY2025, after **$2,258.4M** of triple net lease rent expense. Adjusted for the $278.9M
  impairment and $126.0M of property losses, call it **$483M**.
- Contractual rent rises **2.0%** a year, floored at 2% and capped at 3%. Two per cent of the
  FY2026 payment of $1,878.8M is **$37.6M a year, compounding**.
- Las Vegas Strip Resorts revenue fell **4.3%** in FY2025 ($8,816.1M to $8,441.5M) and Segment
  Adjusted EBITDAR fell **8.0%**. Regional Operations revenue fell **4%** in the second quarter of
  2026 as reported (up 3% same-store).
- **So: hold the domestic guarantor group’s revenue flat and let the rent escalate at 2%, and the
  $483M of adjusted operating income is consumed in roughly thirteen years by the escalator
  alone.** Now suppose instead a single recessionary year in which domestic revenue falls the
  **4.3%** it actually fell in Las Vegas in 2025, at the FY2025 domestic contribution margin
  implied by the segment tables (Las Vegas Strip Resorts Segment Adjusted EBITDAR margin 33.9%):
  **$10,580.2M × 4.3% × 33.9% = $154M of lost profit in one year**, against $483M of adjusted
  operating income and a rent bill that rises $37.6M in the same year. **Three such years in a row,
  with the escalator running, take the domestic group to roughly minus $150M of operating income
  while it still owes $2.0 billion of cash rent.** The holes are then filled from Macau dividends
  - of which **44 cents in the dollar go to other shareholders** and all of which require the
  approval of a separately listed company’s board - or from asset sales, of which three have
  already been made (The Mirage, Gold Strike Tunica, Northfield Park) and each one **reduced the
  revenue base as well as the rent**.
- **The covenant is the accelerator.** Note 11: failing the leases’ financial covenants *"would
  require the Company to maintain either cash security or one or more letters of credit in favor
  of the landlord in amounts ranging from **six months to two years of rent**"* - that is
  **$0.9bn to $3.8bn** of cash or letters of credit demanded precisely when the cash is scarcest.
  And per VICI’s own filing the master lease is **cross-defaulted across the entire portfolio**,
  so no single weak property can be handed back.

**THE LIKELIHOOD, in the corpus’s vocabulary:** **[x] a real possibility.** Not *likely*, because
the Macau leg is currently growing, BetMGM has turned profitable ($59.6M of MGM’s share of
operating income in FY2025 against $(110.1)M in FY2024), the revolver is undrawn and the 2026
maturities are modest against $2.5bn of cash. Not *a low-level possibility*, because **the
domestic leg has already crossed into a pre-tax loss and the guarantor group’s operating income
has already fallen 94% in two years while revenue was flat** - the mechanism is not a forecast,
it is in the filed record for FY2025.

**[E4-40] - EXPOSURE, NOT EXPERIENCE.** *"all of us in the industry made a fundamental
underwriting mistake by focusing on experience, rather than exposure."* The benign reading here
would be that MGM survived a total shutdown in 2020 and is still here. That is experience, and it
is dangerous as a guide, because **the balance sheet that survived 2020 owned Bellagio, MGM Grand,
Mandalay Bay, Aria and The Mirage outright, and could sell them - which is exactly what it did.
The exposure today is a company that has already spent that option.** The 2020 rescue is not
available a second time.

- **VERDICT: NOT TAKEN. The file closed at Q2.** No box ticked.

---
⛔ **Q5 does not open unless Q1-Q4 each show IN.** UNRESEARCHED and UNKNOWABLE both close
the file; neither is a pass.

---
## Q5 - WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?

# COMPUTATION — NOT A CLEARANCE
### RECORDED, NOT GOVERNING. Operator rules 2 and 3.
**Q5 DID NOT OPEN.** Q2 returned OUT, so no Q5 output is a clearance and no line below carries
entry language. The arithmetic is set down because the brief asked for the owner-earnings width
over every window, and because a register entry is more useful with the number beside the verdict.

**The inputs, all struck fresh in Step 0:** market capitalisation **$9,709M** ($38.59 ×
251,592,756 shares from the 10-Q cover, accession 0000789570-26-000076); sovereign **5.34%**, the
US Treasury 30-year par yield for 2026-09-18, from the issuing authority.

**THE YIELD, at every window and every (c) end, and then after the minority leak.** Owner earnings
÷ market capitalisation:

| window | (c)=D&A | (c)=depr only | (c)=capex |
|---|---|---|---|
| 2023-2025 | 16.0% | **17.3%** | 14.4% |
| 2021-2025 (the five-year default) | 6.3% | 13.0% | 12.2% |
| 2020-2025 | **0.4%** | 6.3% | 7.0% |
| 2008-2025 (the whole filed record) | 1.8% | 5.6% | 3.7% |

**After deducting the noncontrolling interests’ FY2025 claim of $315.0M** - because owner earnings
belong to the registrant’s shareholders and roughly 44% of the only profitable leg does not:

| window | (c)=D&A | (c)=depr only | (c)=capex |
|---|---|---|---|
| 2023-2025 | 12.8% | **14.1%** | 11.1% |
| 2021-2025 | **3.0%** | 9.7% | 9.0% |

**1. THE YIELD:** owner earnings **$40M to $1,680M** ÷ market cap **$9,709M** = **0.4% to 17.3%**,
or **3.0% to 14.1%** on the recent windows after the minority leak · sovereign **5.34%**.

**2. WHAT THE PRICE ALREADY ASSUMES:** the question cannot be answered, and saying so is the
answer. A quote that is simultaneously 0.4% and 17.3% of owner earnings depending on which of
eleven published windows and three disclosed (c) ends a reader picks does not embed a growth rate;
it embeds a choice of window. **[E4-38]** names that as the disease and publishing every window as
the cure, which is what the table above does.

**3. WHAT YOU ARE PAID:** between **minus 4.9 points** and **plus 12.0 points** over the 5.34%
sovereign. A range that wide is not a payment, it is an absence of information.

**THE FLOOR, WHICH IS ASKED FIRST [E4-28, E3-13].** *"that’s the figure we quit on … we don’t
want to buy equities where our real expectancy is below 10 percent."* **The band straddles the
floor**: the three-year window clears it on every (c) end even after the minority deduction
(11.1% to 14.1%); the five-year default window clears it on none of them after the deduction
(3.0% to 9.7%); the eighteen-year record clears it on none at all. **A name whose expectancy is
10% or 3% according to which honest window is used has not cleared the floor - it has failed to
produce an expectancy.**

**AND UNDER [E4-25] THAT IS ITSELF THE VERDICT, not an inconvenience:** *"Usually, the range must
be so wide that no useful conclusion can be reached."* The framework says that where the combined
range is too wide, the conclusion is that no useful conclusion can be reached. **It is.**

**NO RISK PREMIUM IS IN THE RATE [E3-42].** The sovereign used is the bare 5.34%. Certainty is
handled at the understanding gate and in the end discount, and it is spent once **[E4-11, E4-48]**.
**Windage count: ONE** - the (c) judgment is pushed toward the capex end, and nothing else is
shaded. The window is not narrowed to a flattering one; all eleven are published.

**THE PRICE IS NOT A CLEAN PRICE, AND THAT IS A FINDING IN ITSELF.** On 2026-06-01 People
Incorporated (f/k/a IAC), holder of more than 25.73% of the voting power and represented on MGM’s
board by Barry Diller, proposed in a Schedule 13D/A exhibit to buy every share it does not own for
**$48.30 in cash**. No merger agreement has been filed; no board response has been filed; the
proposal is *"a non-binding expression of interest only"* by its own terms. The stock closed at
**$47.81 on 2026-06-30**, within 1% of that price, and at **$37.81 on 2026-09-18**. **At $48.30 the
market capitalisation would be $12,152M and the three-year minority-adjusted band would yield 8.9%
to 11.2% - straddling the floor from the other side.** A Q5 that opened here would have been
pricing a control contest, not a business.

- **VERDICT: NOT TAKEN - Q5 DID NOT OPEN.** No box ticked.

## Q6 - WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?
### RECORDED, NOT GOVERNING - there is no position and no entry, so there is no exit to pre-commit.

**[E1-02]** requires the yardstick to be set *"prior to the act"*, and no act is taken. What is
owed instead, under the fold’s step 4 ruling of 2026-09-07, is **the reversal condition in words,
because a name that failed at Q2 failed on the BUSINESS and a price alert on it would be a
category error.**

**WHAT WOULD PROVE THIS VERDICT WRONG - the disconfirming evidence I would accept, named in
advance:**
1. **The guarantor group’s operating income recovering toward $1bn on flat revenue.** The FY2025
   figure was $78.5M and the adjusted figure about $483M, against $1,324.6M in FY2023. This is the
   single number that would say the domestic tenant business can carry its rent. It is filed
   annually in the 10-K MD&A under "Guarantor Financial Information" and semi-annually in the
   10-Q.
2. **Domestic pre-tax income returning to a sustained positive**, from Note 10’s domestic/foreign
   split. FY2025 was $(237.1)M.
3. **Las Vegas ADR and RevPAR rising while occupancy holds.** FY2025 was $249 and $229 with 92%
   occupancy, against $260 and $245 with 94% a year earlier; Q2 2026 was $242 and $224. **[E4-37]**
   says this series is how a moat downgrade is detected in real time, and it would be how an
   upgrade is detected too.
4. **Las Vegas table games drop and slot handle rising**, not hold. Q2 2026 casino revenue rose 17%
   on a 29.6% hold against 22.9%, with drop down 2% and handle flat. **[E4-55]**: the physical
   series is the honest one.
5. **A reported profit measure struck after rent.** If MGM began leading with a measure computed
   after the $2.26bn the landlords take, and paid its executives on it, the **[E4-29]** and
   **[E4-27]** findings would reverse.
6. **A renegotiation, buy-back or termination of the master leases** that materially reduced the
   contractual escalator or the 29-year obligation. This is the only thing that would change the
   mechanism rather than the weather.

**WHAT WOULD NOT CHANGE IT.** A higher share price. Completion of the People Incorporated
transaction at $48.30 or any other number - that is a liquidity event for a holder, not evidence
about the business. Another strong quarter at MGM China. A better hold percentage.

**NO PRICE ALERT IS ARMED AND NO PORTFOLIO ROW IS ADDED** (fold step 4, the QLYS ruling of
2026-09-07): the file closed at Q2, on the business, and a price band on a business finding is a
category error.

- **VERDICT: NOT TAKEN. The file closed at Q2.** No box ticked.

---
## SELF-AUDIT
- [x] Questions answered in order; no verdict skipped. Q1 IN, Q2 OUT, file closed. Q3 to Q6
      recorded beneath the close with no box ticked.
- [x] **No question marked IN carries an "unverified" or "provisional" caveat.** Q1 is the only IN
      and it rests on the FY2025 10-K read in full.
- [x] Every UNRESEARCHED verdict names the artifact and where it lives. **None was returned.**
- [x] Every UNKNOWABLE verdict states what specifically cannot be known. **None was returned.**
- [x] Step 0: the filing was read, with accession number; **three figures were cross-checked**
      against the filed statements (FY2025 operating cash flow, Note 11 cash rent against Note 17
      rent expense, and the Note 11 lease maturity total). A fourth cross-check was made in Q4:
      the FY2022 D&A of $3,482,050 thousand and its $2.7 billion intangible-amortisation component
      were read off the FY2022 10-K income statement and Note 7 directly, not off the tag.
- [x] Owner earnings on a multi-year mean; **eleven windows published**, not one; the capex band
      disclosed as a judgment with three (c) ends and the reason each exists.
- [x] Competitor row filled: **seven comparators**, same metric, same window, every figure from the
      filer’s own 10-K or 20-F. The two Macau concessionaires that are not SEC registrants are
      named as absent rather than glossed.
- [x] Sovereign is for the earnings currency, from the issuing authority, dated: US Treasury
      30-year par yield, 5.34%, 2026-09-18. The mixed earnings currency is disclosed.
- [x] Value stated as a range, not a point estimate - and the range is stated to be too wide to
      support a conclusion **[E4-25]**.
- [x] One bar chosen, not both. **Neither bar was applied**, because Q5 did not open; the windage
      count is stated as ONE.
- [x] Prices dated; the aggregator is used for live quotes only and is flagged, in Step 0 and again
      wherever a historical close is used in Q3.
- [x] **SBC verified to RESOLVE and be COMPLETE for all 18 filed years before any band was built.**
- [x] **My own error found and corrected inside the file rather than left standing**: the operating
      margin row in Q2 reads reported operating income, which in 2021, 2022, 2023 and 2025 contains
      large non-operating items, and the four-consecutive-declines reading it invited is wrong. The
      correction block sits inside Q2 above the verdict.
- [x] Run committed to git, with a pathspec, after every gate.

## REGISTER
- Verdict: [ ] IN **[x] OUT (about the business)** [ ] UNRESEARCHED (about my diligence)
  [ ] UNKNOWABLE (about my evidence)
- One line: **MGM sold the only scarce asset in its business - the land under the Las Vegas Strip
  and its regional casinos - and leased it back on 25-to-30-year triple net master leases with 2%
  contractual escalators, so the domestic group that guarantees its notes earned $78.5M of
  operating income on $10,580.2M of revenue in FY2025 after $2,258.4M of rent, domestic operations
  lost $237.1M before tax, and the registrant’s own Item 1 names its close substitutes.**
- **If UNRESEARCHED - THE WORK ORDER:** not applicable; no UNRESEARCHED verdict was returned.
- **If UNKNOWABLE:** not applicable; no UNKNOWABLE verdict was returned.

