import io, os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "2026-09-19 Run - BLK BlackRock.md")
s = io.open(P, encoding="utf-8").read()

OLD = """## Q2 — IS IT A FRANCHISE? **[E3-03]**
- Needed or desired [ ] · no close substitute [ ] · not price-regulated [ ]
- Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]** ____
- Primary moat metric, filing-sourced, and its trend: ____
"""

NEW = r"""## Q2 — IS IT A FRANCHISE? **[E3-03]**

### The three criteria, one line each

- **Needed or desired [x] — yes, unambiguously.** $698,261M of net inflows in 2025 and $867,778M in
  the twelve months to 2026-06-30. Nobody has to be persuaded to want an index fund.
- **No close substitute [ ] — NO, and this is where the file turns.** Two sections below.
- **Not subject to price regulation [x] — correct, there is no price regulation.** But note what
  [E2-59] warns: regulation *caps* a franchise and *floors* a commodity business, and neither
  creates the class. There is no administered price here at all. The price is set by competition,
  and the filing says so in Item 1A.

### Must the moat be continuously rebuilt? Does success depend on a great manager? **[E4-04]**

**Not a great manager.** The iShares platform survives any individual, and **[E4-23]** is satisfied:
nobody needs to know who runs an S&P 500 tracker. **No key-person moat defect is recorded here**,
and this run does not use Q3 to promote or demote the name.

**But the basis of the advantage is being periodically replaced with purchased product, and that is
the class [E4-04] excludes.** The framework's test is *"does a lapse in spending destroy the
structure, or merely narrow it — and does the spending defend the same advantage, or buy its
replacement?"* On these filings the spending buys the replacement:

| | GIP | Preqin | HPS |
|---|---|---|---|
| closed | 2024-10-01 | 2025-03-03 | 2025-07-01 |
| consideration, net of cash acquired | **$12,949M** | **$3,123M** | **$12,221M** |
| paid in | $2,913M cash + **6.9M shares at $5,904M** (struck at ~$855 after a two-year registration discount off a $950 quote) + **$4,200M deferred stock** | **$3,219M cash** | **8.5M Subco Units at $8,452M** + **$3,400M deferred units** + $613M of debt repaid |
| goodwill | **$10,278M of $12,949M — 79.4%** | $2,377M of $3,123M — 76.1% | $6,841M of $12,221M — 56.0% |

**$28.3 billion in twenty-one months, $22.0 billion of it paid in the company's own paper, with
$8,429M of contingent consideration still outstanding — GIP 4.0 to 5.2 million shares, HPS 2.8 to
4.4 million Subco Units.** Add the closing paper to the contingent maximum and **up to 25.0 million
shares and units — 15.4% of the 162.5 million now outstanding — will have been handed to the sellers
of two private-markets managers.** Goodwill and intangibles went from $33,643M at 2022-12-31 to
**$63,251M at 2025-12-31, against total BlackRock, Inc. stockholders' equity of $55,888M: tangible
equity is NEGATIVE $7,363M**, against positive $4,101M three years earlier. ElmTree and SpiderRock
sit inside the same programme and inside the $120,961M of AUM the roll-forward labels "Acquisitions".

**Why that is a Q2 finding and not merely a Q3 one is arithmetic, and it is in the next section:
the price of everything BlackRock already owned fell in every single year, and the only thing that
stopped the blended rate falling was the bought book.** The spending is not defending the same
advantage. It is buying a different, higher-priced product to hold up an average.

### Primary moat metric, filing-sourced, and its trend

**The metric is the effective fee rate on average assets under management, in basis points** — base
fees (investment advisory, administration fees and securities lending revenue) divided by the
filer's own full-year average AUM, which BlackRock defines as *"the average of the month-end spot
AUM amounts for the trailing thirteen months."* It is the right metric for the reasons the BAM run
of 2026-09-13 gave and this run re-tested: it **is** the price of the product, so it is what
**[E2-44]** (raise prices with flat demand), **[E3-33]** (untapped pricing power) and **[E4-37]**
(the agony of a price increase) are actually about; every competitor files it or its inputs; and it
is the first thing to move when close substitutes exist. **No figure was inherited from the BAM
row: all of them were recomputed here from the filings.**

**Sources: 10-K FY2025 `0001193125-26-071966` (2024, 2025); 10-K FY2023 `0000950170-24-019271`
(2022, 2023); 10-K FY2022 `0000950170-23-004343` (2021); 10-Q Q2 2026 `0001193125-26-337177`
(H1 2026). Arithmetic and inputs: `Test Runs/_research 2026-09-19 BLK/feerates.py`, output in
`feerates.txt`.**

| segment, bp on average AUM | 2021 | 2022 | 2023 | 2024 | 2025 | H1-26 ann. | **2021→2025** |
|---|---|---|---|---|---|---|---|
| **TOTAL** | **16.29** | **16.15** | **15.62** | **14.90** | **15.22** | **15.25** | **−6.6%** |
| **ETFs (all)** | **20.41** | **19.21** | **18.48** | **17.31** | **16.92** | **17.14** | **−17.1%** |
| Equity, active | 55.14 | 50.38 | 48.82 | 46.93 | 43.65 | 42.02 | **−20.8%** |
| Fixed income, active | 20.79 | 19.44 | 17.55 | 17.23 | 17.06 | 16.95 | **−18.0%** |
| Multi-asset, active | 19.21 | 17.94 | 15.28 | 13.55 | 12.42 | 12.03 | **−35.4%** |
| Non-ETF index | 3.83 | 3.80 | 3.79 | 3.52 | 3.52 | 3.47 | **−8.1%** |
| Private markets / illiquid alts | 70.49 | 66.71 | 69.64 | 77.36 | **89.85** | 80.06 | **+27.5%** |
| Cash management | 6.61 | 12.01 | 13.05 | 13.01 | 12.76 | 12.72 | +93.1% |

**Read it in the order that matters.**

1. **Every product BlackRock owned throughout the window got cheaper. Every single one.** ETFs
   −17.1%, active equity −20.8%, active fixed income −18.0%, active multi-asset −35.4%, non-ETF
   index −8.1%. **There is no organically-owned line in this company whose price rose.**
2. **The two lines that rose did not rise on price.** Cash management's 6.61bp in 2021 is a
   zero-interest-rate artefact — money-market fee waivers, and the filer states *"Investment
   advisory and administration fees for investment funds are shown **net of fee waivers**"*; from
   2022 the series reads 12.01 → 13.05 → 13.01 → **12.76 → 12.72, which is falling.** Private
   markets rose +27.5% because **GIP and HPS were bought**: that leg's average AUM went from
   $154,597M to $261,535M in a single year, $101,017M of it arriving as "Acquisitions" in the
   filer's own roll-forward, and the acquired books price higher than the legacy alternatives did.
3. **Take the bought leg out and the total is not flat — it is down 13.4%:** ex-private-markets,
   **15.74bp (2021) → 13.64bp (2025)**. The 15.22bp of 2025 is a mix effect purchased for
   $28.3 billion.
4. **The second reading says the same thing without using a rate at all.** AUM $10,010,143M at
   2021-12-31 → **$14,041,518M at 2025-12-31, +40.3%.** Base fees **$15,260M → $19,179M, +25.7%.**
   **Revenue grew 14.6 percentage points slower than the assets it is charged on over four years —
   and that is *after* $28.3bn of acquired, higher-priced AUM was added to the numerator.** This is
   **[E4-55]** inverted, exactly as the BAM run found it: volume flatters the dollars while the
   price per unit falls, and the rate is the honest series.
5. **Direction is what the framework weighs. [E4-32]:** the moat *widened every year* is *"the
   primary criterion of a great business"* — *"that does not necessarily mean that the profit is
   more this year than last year."* Here the profit is more and the moat is narrower. Every
   direction available in these filings points the same way.

**The filer says it, in Item 1A, and the word to notice is "additional":** *"This evolution,
together with the introduction of new technologies, as well as regulatory changes, continues to
alter the competitive landscape for investment managers, **which may lead to additional fee
compression** or require BlackRock to invest more to modify or adapt its product offerings to
attract and retain customers … Increased competition on the basis of any of these factors,
**including competition leading to fee reductions on existing or new business**, may cause the
Company's AUM, revenue and earnings to decline."* A business with no close substitute does not warn
about *additional* fee compression, because it has no first instalment to add to.

**And in Item 1 the filer names price as a competitive factor and claims no pricing power anywhere:**
*"Key competitive factors include investment performance track records, **the efficient delivery of
beta for index products**, investment style and discipline, **price**, client service and brand name
recognition."* "The efficient delivery of beta" is a description of a commodity, written by the
market leader.

**One more line from the MD&A, about a third of the assets:** *"institutional non-ETF index
assignments tend to be very large (multi-billion dollars) and **typically reflect low fee rates**.
Net flows in institutional index products generally have a small impact on BlackRock's revenues and
earnings."* **Non-ETF index is 29.8% of average AUM and 6.9% of base fees, at 3.52bp.** Four
trillion dollars of AUM are, on the company's own account, nearly immaterial to its earnings.

### THE COMPETITOR ROW — required **[E3-28]**

> *"I can't be an intelligent owner of a business unless I know what all the other businesses in
> that industry are doing."* — **[E3-28]**

**One specification for every line: the effective fee rate on average assets under management, in
basis points, from that company's own filing, for the five most recent fiscal years.** Where the
filer publishes the rate, the filer's rate is used and its definition is quoted; where it publishes
only period-end AUM, the average of beginning and ending AUM is used and labelled as computation,
not disclosure. Supporting evidence, verbatim definitions, accession numbers and arithmetic checks:
`Test Runs/_research 2026-09-19 BLK/peers/PEER_ROW.md`.

| Company | metric, as the filer defines it | 2021 | 2022 | 2023 | 2024 | 2025 | direction | source accession |
|---|---|---|---|---|---|---|---|---|
| **BLK (subject)** | base fees ÷ 13-month average AUM | **16.29** | **16.15** | **15.62** | **14.90** | **15.22** | **−6.6%; −13.4% ex private markets** | `0001193125-26-071966` |
| **State Street (STT)** | management fees ÷ average of opening and closing AUM — **my computation: STT publishes neither a fee rate nor an average AUM** | 5.40 | 5.09 | 4.95 | 4.82 | **4.62** | **−14.4%** | `0000093751-26-000124`, `0000093751-24-000498` |
| **Invesco (IVZ)** | its own *"U.S. GAAP gross revenue yield on AUM"* | 48.7 | 44.5 | 40.4 | 37.4 | **33.7** | **−30.8%** | `0000914208-26-000079` |
| **Invesco (IVZ)** | its own *"Net revenue yield ex performance fees"* — **definition changed in FY2025 to include QQQ; do not splice** | 39.1 | 35.5 | 32.4 / 28.4 | 30.2 / 25.4 | **23.0** | **down on every vintage** | `0000914208-26-000079`, `0000914208-25-000114` |
| **Invesco (IVZ)** | investment management fees ÷ its own published average AUM — my computation, matched to the others' construction | 33.31 | 30.01 | 27.36 | 25.36 | **23.08** | **−30.7%** | `0000914208-26-000079`, `0000914208-23-000297` |
| **T. Rowe Price (TROW)** | its own *"Investment advisory annualized effective fee rate (EFR)"*, excluding performance-based fees | 44.4 *(incl. perf. fees; the ex-perf. recast starts 2022)* | 42.6 | 41.9 | 41.0 | **39.4** | **−11.3% on the ex-perf. series, 2022→2025** | `0001628280-26-008002`, `0001113169-25-000007`, `0001113169-22-000005` |
| **Franklin Resources (BEN)**, FY to 30 Sep | its own *"effective investment management fee rate excluding performance fees (investment management fees excluding performance fees divided by average AUM)"*, on a 13-month average AUM | 41.8 | 41.6 | 42.1 | 41.1 | **40.5** | **−3.1%**, and a composite: Legg Mason, Lexington, Alcentra and Putnam all closed inside the window | `0000038777-25-000238`, `0000038777-23-000169` |
| **Blackstone (BX)** | management and advisory fees ÷ fee-earning AUM; the firm's own *"Annualized Base Management Fee Rate"* is **0.86%** | — | — | — | — | **92.2** *(86.2 on base fees)* | flat-to-down on its own disclosure | `0001193125-26-082531` *(figure from the committed BAM row of 2026-09-13; **not recomputed in this run**)* |
| **Brookfield Asset Mgmt (BAM)** | base management fees ÷ fee-bearing capital | — | — | 90.4 | 85.0 | **85.8** *(82.4 annualised in H1 2026)* | **down 8bp in two and a half years** | `0001628280-26-013098` *(committed BAM row; **not recomputed**)* |

- **Peers named: 8 lines covering 6 filing-sourced competitors**, plus the substitution test below,
  out of an industry that has perhaps a dozen real competitors to the index and ETF business and
  another dozen in private markets. **Buffett says eight [E3-28]; this row runs eight lines and
  names every one it could not pull.**

**THE DECISIVE READING OF THE ROW, and it is not that BlackRock is cheapest.** Of course it is
cheapest: 15.22bp against TROW's 39.4 and BEN's 40.5 is a statement about **product mix**, not about
franchise. BlackRock sells index beta; they sell active management. **What the row actually shows is
that the price of every asset-management product on it is falling at the same time, and that
BlackRock is falling too.** Six independent filers, six different definitions, six different
fiscal calendars, and one direction: **−6.6%, −14.4%, −30.8%, −11.3%, −3.1%, and −8bp on
fee-bearing capital.** **[E3-03] criterion 2 is a claim about the customer's alternatives, and the
customer is getting a better price every year from everybody.** This is [E2-58]'s equation applied
to a fee rather than a commodity price: capacity is ample, nobody administers the price, and the
long-run profitability is set by how often supply is tight — which, in an industry where the
marginal unit of index capacity costs almost nothing to add, is never.

### THE SUBSTITUTION TEST, which is criterion 2 at its sharpest

The competitor row is a *revenue* comparison across different products. Criterion 2 asks something
narrower: **is there a close substitute for the thing BlackRock actually sells?** For the product
that is 42% of long-term AUM and 45% of long-term base fees, the answer can be read off two
SEC-filed prospectuses, side by side, to the basis point.

| fund | manager | index tracked | total annual fund operating expenses, **2026** | same fund, **2021** | filing |
|---|---|---|---|---|---|
| **iShares Core S&P 500 ETF (IVV)** | **BlackRock Fund Advisors** | S&P 500 | **0.03%** | **0.03%** | iShares Trust 485BPOS, filed 2026-07-27, acc. `0001193125-26-318131`; 2021 filed 2021-07-26, acc. `0001193125-21-223259` |
| **Vanguard 500 Index Fund, ETF Shares (VOO)** | Vanguard | S&P 500 | **0.03%** | **0.03%** | Vanguard Index Funds 485BPOS, filed 2026-04-28, acc. `0000036405-26-000181`; 2021 filed 2021-04-29, acc. `0001683863-21-002763` |
| **SPDR S&P 500 ETF Trust (SPY)** | State Street Global Advisors | S&P 500 | **0.0945%** (capped by waiver to 2027-02-01) | **0.0945%** | SPDR S&P 500 ETF Trust 485BPOS, filed 2026-01-26, acc. `0001193125-26-022316`; 2021 filed 2021-01-14, acc. `0001193125-21-008848` |
| **iShares Core S&P Total U.S. Stock Market ETF (ITOT)** | **BlackRock Fund Advisors** | S&P Total Market | **0.03%** | — | acc. `0001193125-26-318131` |
| **Vanguard Total Stock Market Index Fund, ETF Shares (VTI)** | Vanguard | CRSP US Total Market | **0.03%** | **0.03%** | acc. `0000036405-26-000181`; 2021 acc. `0001683863-21-002763` |

**Two managers, the same index, the same exposure, the same price to four decimal places, for at
least five years.** That is not a near-substitute; on the only dimension a buyer of beta can
compare — cost of tracking — **it is the same product.** And the rival is structurally unable to be
out-priced: Vanguard's management company is owned by the funds it manages and runs them at cost, so
there is no margin to defend and no shareholder to disappoint. **[E3-03] criterion 2 fails on a
filed document, not on an inference.**

**What the substitution test does NOT say, stated at full strength because [E4-26] requires the
disconfirming read on the favourite hypothesis.** It does not say iShares has no advantage. iShares
crossed **$6 trillion** in AUM and *"roughly doubl[ed] in three years"* (8-K EX-99.1, 2026-07-15),
and the secondary-market liquidity of IVV is a genuine, unbuyable asset — a trader will pay a wider
implicit cost in a thinner fund at the same expense ratio. That is why iShares keeps winning share
at 3bp. **But an advantage that shows up as volume at a price you cannot raise is a scale advantage,
not a franchise**, and the framework has a name for what it does to the owner: **[E3-62]**'s second
step — *"how much is going to stay home and how much is just going to flow through to the
customer"*. The answer is in the table above: the savings went to the customer. Fee rate down 17.1%
on ETFs while ETF AUM rose 84% and ETF revenue rose 33%.

### The remaining Q2 tests, each answered

- **Untapped pricing power [E3-33, E5-28] — NO, and the opposite.** Claiming this class is claiming
  *"a monopoly or a near monopoly"* **[E5-28]**. BlackRock has ~13% of a market where the number two
  charges the identical price at cost and the number three is $6.6 trillion in the same product.
  There is no filed evidence of a price BlackRock could raise and has not. **[E4-37]**'s inverse
  metric — the agony of a price increase — cannot even be measured here, because in five years of
  filings **there is not one instance of a price increase to agonise over.** Rates went one way.
- **The two-characteristic test [E2-44] — fails on the first half, passes on the second.** Can it
  raise prices with flat demand and spare capacity? No: it cut them with *rising* demand. Can it
  grow dollar volume with only minor additional capital? **Yes, emphatically** — $375M of capex on
  $24.2bn of revenue, and AUM up $4.0 trillion in four years with no plant. **A business that
  passes the second half and fails the first is the definition of an efficient commodity producer.**
- **The second question is a number [E3-46]** — high returns on capital employed over time. GAAP
  return on average BlackRock, Inc. equity: **14.3% (2023), 14.7% (2024), 10.7% (2025)**, and
  **[E2-43]**'s unleveraged-net-tangible-assets denominator is now **negative**, so the honest
  reading is that the operating business earns a very high return on the tangible capital it uses
  and the *purchase price* of the acquired managers has been added to the denominator the
  shareholder actually funded. Both facts are true and both belong in the file.
- **The dominance class [E2-53] — NO.** *"Once dominant, the newspaper itself, not the marketplace,
  determines just how good or how bad the paper will be."* BlackRock is the largest manager on
  earth and **does not determine its own price**; the marketplace does. It is the clearest possible
  negative on this test: maximum scale, zero price-setting.
- **The attacker's test [E2-45].** With ample capital and skilled people, how would I compete with
  it? Exactly as Vanguard does: file the same index fund at the same 3bp and win on cost of capital,
  because a client-owned manager needs no margin. That attack is **already running and already
  works**, which is why criterion 2 fails.
- **Four causes of extreme success [E4-36] — which one is this?** Not an extreme max/min of one
  variable, not a nonlinear combination. It is **wave-riding [E3-51]**: the four-decade migration of
  the world's savings from active to index vehicles, which BlackRock rode better than anyone.
  *"When a surfer gets up and catches the wave and just stays there, he can go a long, long
  time."* **A surfing run is not a moat; the advantage lives in the wave.** The BAM run rejected
  wave-riding as a moat under [E3-51] and the same rejection applies here, to a different wave —
  with one honest difference recorded below.
- **Units, where units exist [E4-55].** The physical series here is AUM and it is rising strongly;
  the price series is falling. That is the inverse of Precision Steel and it is the benign form of
  the test: the franchise is not hiding a volume collapse behind price rises. **It is hiding a price
  collapse behind volume rises**, and the framework's answer is the same — take the honest series.

### THE CASE FOR IN, BUILT AT FULL STRENGTH AND REJECTED **[E4-26, E4-51]**

*[E4-51] requires a bear case its holders would accept as fairly stated. The same discipline is owed
to the bull case at the gate that closes the file.*

**The strongest case for a franchise, stated as its holders would state it.** BlackRock is not
selling a commodity; it is selling **access to the deepest pool of secondary liquidity in listed
index vehicles**, and that is not replicable with money. Iron evidence: it has taken share for a
decade at a price identical to Vanguard's, which means buyers are choosing iShares *for something
other than price* — the order book, the securities-lending revenue shared back into the fund, the
options market built on the ETF, the ability to trade $10bn in an afternoon. Aladdin is a second,
genuinely different business: **$1,981M of revenue growing 10.5% organically, on long-term
contracts, with an installed base that cannot switch cheaply.** The private-markets build is not a
treadmill but a one-time widening of the product set into the only part of the industry where fees
are 90bp instead of 3bp, and the earn-out revaluing **upward by $720M** in 2025 says HPS is
outperforming the case underwritten at the deal. And the total fee rate has been **essentially flat
for two years — 14.90, 15.22, 15.25 — while AUM went from $11.6tn to $15.3tn**: the compression is
decelerating, not accelerating. Cash management, 7% of AUM, is now a structurally profitable
12-13bp business it was not in 2021.

**Why it does not carry, one line each:**
1. **Criterion 2 is decided on a filed document, not on a judgment.** IVV 0.03%, VOO 0.03%, five
   years unchanged. A franchise is *"thought by its customers to have no close substitute"*
   **[E3-03]**, and the customer can read both prospectuses in a minute.
2. **Every organic product got cheaper, every year, without exception.** Direction outranks
   existence **[E4-32]**, and there is no counter-direction anywhere in the table.
3. **The flat blended rate is bought, not earned.** Strip the acquired private-markets book and the
   rate fell 13.4%. $28.3bn — $22.0bn of it in shares and units, up to 15.4% of the company — is
   what "flat" cost, and the moat's basis is being replaced rather than defended **[E4-04]**.
4. **The advantage is scale on a wave [E3-51, E4-36]**, and the gains from scale went to the buyer,
   not to the owner **[E3-62]**. Twenty-five per cent revenue growth on forty per cent asset growth
   is the arithmetic of a pass-through.
5. **Aladdin is real and it is 8.2% of revenue.** It cannot carry the classification of the other
   91.8%, and its own fees are *"generally determined using the value of positions on the Aladdin
   platform"* — i.e. partly the same market-linked base as everything else. Q4 records it; Q2
   cannot promote the whole on a twelfth.
6. **There is no untapped pricing power and no instance of a price increase in five years of
   filings [E3-33, E5-28, E4-37].**

**A conclusion that required fighting for it is worth less, not more [E4-18].** This one needed no
fighting: the subject's own Item 1A warns of *additional* fee compression, its own Item 1 lists
price as a competitive factor, and its own rate table falls in every organic line.

- **Class: [ ] WIDE  [ ] NARROW  [ ] NONE  [ ] PROVISIONAL → the class is NARROW AND NARROWING.**
  **Direction: DOWN, in every organically-owned product, in every year measured.**
- **Any peer unavailable?** **Yes, two, and both are named with the artifact that would resolve
  them, and neither can reverse the finding:**
  - **Vanguard** — the management company files no 10-K (it is owned by the funds it manages and
    has no public equity). **Resolved differently and better:** its *funds* file with the SEC, and
    the price of the actual substitute is taken from its own 485BPOS above. Not UNRESEARCHED.
  - **Fidelity (FMR LLC)** — private, no 10-K. **UNRESEARCHED, artifact named:** the Fidelity
    Concord Street Trust 485BPOS containing the fee table for the Fidelity ZERO index funds
    (CIK 0000819118; the four 2026 filings located — `0000819118-26-000018`, `-26-000072`,
    `-26-000136`, `-26-000137` — carry the Part C exhibit lists and the ZERO funds' names but the
    prospectus fee tables were not located in them). It matters only in one direction: a rival
    charging **zero** would strengthen the criterion-2 failure, never reverse it.
  - **Amundi** — **not an SEC registrant** (Euronext Paris). **UNRESEARCHED, artifact named:**
    Amundi's Universal Registration Document / annual report, English edition, which publishes a fee
    margin in basis points. Same one-directional logic: Amundi is a price-taker in European ETFs and
    has been cutting, not raising.
  - **The moat class is NOT held PROVISIONAL on these two absences**, and the reason is the one the
    BAM run gave: the row already decides, and the two missing filers can only push the same way.
    Holding the class provisional here would be *"narrowing assumptions until the answer appears"*
    in reverse **[E4-18]**.

- **VERDICT: [ ] IN  [x] OUT — ON THE BUSINESS. Permanent.**
  **Criterion 2 of [E3-03] fails on a filed price.** The product that is 42% of long-term AUM and
  45% of long-term base fees is sold by a rival at **0.03% against BlackRock's 0.03%**, unchanged
  for five years, and that rival is structurally incapable of needing a margin. Every organically
  owned product's price fell in the measured window — ETFs −17.1%, active equity −20.8%, active
  fixed income −18.0%, active multi-asset −35.4%, non-ETF index −8.1% — and the blended rate held
  only because **$28.3 billion, $22.0 billion of it in the company's own shares and units, bought a
  higher-priced book [E4-04]**. Base fees grew **14.6 points slower than the assets they are charged
  on** over four years **[E4-55]**. There is no untapped pricing power and not one filed instance of
  a price increase **[E3-33, E5-28, E4-37]**. The record is a **surfing run [E3-51, E4-36]** on the
  indexing wave, and the gains from scale flowed to the customer **[E3-62]**. **[E2-53]** is the
  sharpest single reading: the largest asset manager that has ever existed does not set its own
  price.
  *Not UNRESEARCHED: the row is complete on one metric, one window, from primary filings, and the
  substitution test is decided from two prospectuses. Not UNKNOWABLE: the evidence is in and it
  decides. **This is a very good business. It is not a franchise.***

**⛔ THE FILE CLOSES HERE. Q3, Q4, Q5 and Q6 below are RECORDED, NOT GOVERNING** — written because
the operator's instruction of 2026-09-01 requires a price and a refutation record on every name, and
because a run that stops writing at the closing gate destroys the evidence a future reader would
need to reopen it. **Q5 carries the heading `COMPUTATION — NOT A CLEARANCE` (operator rule 3) and
no entry language appears anywhere below.**
"""

assert OLD in s, "Q2 anchor not found"
s = s.replace(OLD, NEW, 1)
io.open(P, "w", encoding="utf-8").write(s)
print("Q2 written, chars:", len(NEW))
