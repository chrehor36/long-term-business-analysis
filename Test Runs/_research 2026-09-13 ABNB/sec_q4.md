## Q4 — WILL IT SURVIVE?

> **RECORDED, NOT GOVERNING.** The file closed at Q2 (OUT). This section is written because the queue asks every run for a price and because the evidence was gathered; it decides nothing and cannot reopen Q2 [E2-37, E3-39].


### First: what is in operating cash, and what is not — the customer-funds separation
**Read from the cash-flow statement and Note 2 before any owner-earnings figure is stated.** Airbnb's
balances are of three kinds, and the filing classifies them differently:

| balance | what it is (filing's words) | 2024 → 2025 → 2026-06-30, $M | where its change sits |
|---|---|---|---|
| **Funds receivable and amounts held on behalf of customers** / **funds payable and amounts payable to customers** | *"cash received or in-transit from guests ... which the Company remits for payment to the hosts following check-in"*; *"a liability for the same amount is recorded"* | 5,931 → 6,959 → **12,224** (asset = liability, to the dollar) | **FINANCING**: *"Change in funds payable and amounts payable to customers"* +936 / +320 / +401 (2023-25), +5,426 (H1 2026); the cash sits in *"Cash and cash equivalents included in funds receivable and amounts held on behalf of customers"* (5,871 → 6,891 → 12,161) inside the cash-flow statement's restricted-cash total |
| **Unearned fees** | *"Host and guest fees are recorded as cash with a corresponding amount in unearned fees"*; *"subject to refund in the event of a cancellation"* | 1,616 → 1,743 → 2,831 | **OPERATING**: +242 / +200 / +122 (2023-25); +1,085 (H1 2026) |
| **Interest earned on customer funds** | *"Funds held on behalf of our hosts and guests ... do not impact Free Cash Flow, except interest earned on these funds"* (Q2 2026 letter) | not separately disclosed | **OPERATING**, inside interest income ($721M / $818M / $705M) |

**So the trap the brief named is smaller here than at PAY, and it is in a different place.** The hosts'
money (the $7-12bn) **never enters operating cash**: its swing is financing, and the 2020 refund wave
(*"Change in funds payable ... (1,024)"*) ran through financing too. **What does enter operating cash is
(a) Airbnb's own fees collected before the stay, which reverse when bookings shrink (2020: -$267M), and
(b) the interest on the hosts' money.** Owner earnings are therefore shown three ways:
- **A — as filed:** OCF − SBC − (c).
- **B — the fee float removed:** A − the change in unearned fees. *(The corpus's working-capital rule
  [E2-23] runs the other way here: this business does not require working capital to grow, it releases
  it. B shows the earnings without the release.)*
- **C — B less the interest attributable to customer funds.** **CONVENTION, confessed:** interest income
  × average customer funds ÷ (average customer funds + average own cash and short-term investments),
  year-end averages for 2019-2023 and five quarter-end points for 2024-2025 (Q2 2026 letter's quarterly
  summary). Removed **pre-tax**, because cash taxes paid ran 6.3% / 10.5% / 7.4% of pre-tax income in
  2023-25; the conservative direction. The attribution share ran 29-42%: **~$294M of 2025's $705M.**
  A pass-through of smaller size is left in A: lodging taxes collected and owed ($312M → $387M) sit in
  accrued liabilities; their +$75M swing in 2025 is not stripped (0.3% of cap; stated, not used).

### Owner earnings — the one number **[E2-23]**
**Inputs, all from the filed cash-flow statements (newest vintage) and the MD&A FCF reconciliations; $M.**
`_research .../q4calc.py`, output in `q4calc_out.txt`.

| year | OCF | SBC (add-back) | capex (MD&A) | D&A | Δ unearned fees | cust.-funds interest (C, est.) | **A capex end** | **A D&A end** | B capex / D&A | C capex / D&A | SBC/OCF |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2019 (pre-IPO) | 223 | 98 | 126 | 114 | 176 | n/a | 0 | 11 | -177 / -165 | n/a | 43.8% |
| **2020** | **-740** | **3,003** | 37 | 126 | -267 | 10 | **-3,780** | **-3,869** | -3,513 / -3,602 | -3,523 / -3,612 | n/m |
| 2021 | 2,313 | 899 | 25 | 138 | 496 | 4 | 1,389 | 1,276 | 893 / 780 | 889 / 776 | 38.9% |
| 2022 | 3,430 | 930 | 25 | 81 | 280 | 60 | 2,475 | 2,419 | 2,195 / 2,139 | 2,135 / 2,079 | 27.1% |
| 2023 | 3,884 | 1,120 | 47 | 44 | 242 | 253 | 2,717 | 2,720 | 2,475 / 2,478 | 2,222 / 2,225 | 28.8% |
| 2024 | 4,518 | 1,407 | 34 | 65 | 200 | 334 | 3,077 | 3,046 | 2,877 / 2,846 | 2,543 / 2,512 | 31.1% |
| 2025 | 4,646 | 1,592 | 33 | 91 | 122 | 294 | 3,021 | 2,963 | 2,899 / 2,841 | 2,605 / 2,547 | 34.3% |
| TTM 2026-06 | 4,860 | 1,707 | 33 | 84 | -29 | — | 3,120 | 3,069 | 3,149 / 3,098 | — | 35.1% |

*2020 is not dropped [E4-25]*: it is the pandemic trough **and** the IPO year — *"$2.8 billion of
stock-based compensation expense associated with the vesting of RSUs in connection with our IPO"*, years
of pre-IPO service recognised at once, plus the 2020 OCF restatement (-$629.7M filed, -$740M in the
FY2022 10-K). It is shown in every window that includes it.

### MORE THAN ONE WINDOW — THE SPREAD IS PART OF THE RANGE **[E4-25, E4-38]**
| window | A (capex end … D&A end) | yield on US$100,341.6M | B (fee float removed) | C (and cust.-funds interest) |
|---|---|---|---|---|
| **5y 2021-2025, ex-2020 (the corpus default [E2-42])** | **2,536 … 2,485** | **2.53% … 2.48%** | 2,268 … 2,217 (2.26-2.21%) | 2,079 … 2,028 (2.07-2.02%) |
| **5y 2020-2024, incl. 2020** | **1,176 … 1,118** | **1.17% … 1.11%** | 985 … 928 | 853 … 796 (0.85-0.79%) |
| 6y 2020-2025, full listed history | 1,483 … 1,426 | 1.48% … 1.42% | 1,304 … 1,247 | 1,145 … 1,088 |
| 3y 2023-2025 | 2,938 … 2,910 | 2.93% … 2.90% | 2,750 … 2,722 | 2,457 … 2,428 |
| 7y 2019-2025, incl. pre-IPO 2019 | 1,271 … 1,224 | 1.27% … 1.22% | 1,093 … 1,045 | n/a |
| TTM to 2026-06-30 | 3,120 … 3,069 | 3.11% … 3.06% | 3,149 … 3,098 | — |

- **Spread, conservative end:** the ex-2020 five-year window (D&A end, 2,485) against the incl.-2020
  five-year window (1,118) is **-55%**; against the float-stripped incl.-2020 window (796), **-68%**.
- **Combined range: $0.8bn (5y incl. 2020, C, D&A) to $3.1bn (TTM, A, capex).** Is it too wide to reach a
  conclusion? **Not for the question Q4 asks** — every window with 2020 removed lies at $2.0-3.1bn and every
  window with it lies at $0.8-1.5bn, and **all of them sit below the 5.35% sovereign at this price**. The
  width is a **level** uncertainty, not a sign uncertainty, and the distortion is named: one pandemic year
  combined with an IPO-year stock-compensation catch-up.
- **The distorted year, as a Q4 finding [E5-11]:** the stream is **not reliable through a travel stoppage**.
  2020: GBV -37%, OCF -$740M, a quarter of employees cut (*"approximately 1,800 employees in May 2020"*),
  and survival financed by strangers at a price (below).
- **Favourable exogenous breaks, removed before the mean is trusted [E4-41]:** interest income rose from
  $12.7M (2021) to $818M (2024) on rates, not on the business. C strips the customer-funds share; the
  interest on Airbnb's own $11bn (~$411M of 2025's $705M) is left in, and would fall with rates.

### Maintenance capex — a DISCLOSED JUDGMENT with a corpus DEFAULT **[E3-44, E2-41, E5-20]**
- **Which case is this?** The **default case, not the exception class.** The tag gap was a presentation
  change (Step 0). Capex is $25-47M a year since 2020 (0.27-1.1% of revenue); property and equipment, net,
  $107M. **Nothing in the filing says depreciation understates renewal**; the opposite holds: D&A ($44-138M)
  has exceeded capex in five of six listed years, because D&A carries acquired-intangible amortisation
  (HotelTonight, 2019; *"Amortization expense related to intangible assets was immaterial"* by 2023-25) and
  1.5-3-year software lives.
- **Band used: capex end to D&A end, which differ by $3-113M a year — under 5% of the owner-earnings
  figure in every window (5.2% in the incl.-2020 five-year window, under 2.1% in every window without 2020).** **The (c) guess does not move any verdict.** Where it sits: nearer the D&A end,
  **because the maintenance of this competitive position is expensed, not capitalised** — product development
  $2,354M and marketing $1,704M in 2025, and a $1.7bn data-hosting commitment through 2031 — so both ends
  of (c) are small only because OCF has already paid the real renewal bill. That is the reason to trust the
  small (c), and it is also the reason owner earnings are not larger.
- **Capitalised stock compensation:** the equity statement's SBC ($1,146M / $1,424M / $1,600M, 2023-25)
  exceeds the cash-flow add-back ($1,120M / $1,407M / $1,592M) by $8-26M, capitalised into software. It is
  inside the D&A end (as amortisation) and outside the capex end; one more reason the D&A end is used as
  the conservative figure.
- *If the capex band changes the verdict → UNKNOWABLE.* **It does not.**

### Stock compensation — subtracted in full **[E5-06]**, and it RESOLVES and is COMPLETE
**Cross-checked to the dollar, 2025:** cash-flow add-back **$1,592M** = MD&A table (*"Operations and support
| $ | 90 ... Product development | 886 | ... | 1,017 ... Sales and marketing ... 212 ... General and administrative
... 273 ... Stock-based compensation expense | $ | 1,407 | ... | $ | 1,592"*: 90 + 1,017 + 212 + 273 = 1,592) =
Note 16 segment expense 1,592 = companyfacts `ShareBasedCompensation` 1,592.0. H1 2026: 63 + 561 + 122 +
151 = **897** = cash-flow add-back 897. Every year 2019-2025 resolves from the filed statement; no year is
missing, dimensioned, or zero (the item-3F defect cannot bite here).

**SBC / OCF, over the full filed history since the IPO:**
| span | SBC $M | OCF $M | **SBC/OCF** |
|---|---|---|---|
| **2020-2025 cumulative (listed history, incl. the IPO catch-up)** | 8,951 | 18,051 | **49.6%** |
| 2020 – H1 2026 | 9,848 | 21,029 | 46.8% |
| **2021-2025 cumulative (ex-2020)** | 5,948 | 18,791 | **31.7%** |
| 2021 – H1 2026 | 6,845 | 21,769 | 31.4% |
| by year 2021 / 22 / 23 / 24 / 25 / TTM | | | 38.9% / 27.1% / 28.8% / 31.1% / 34.3% / 35.1% |

**In the calibrated row: ACVA 330.5% · ROKU 140.2% · CALX 98.4% · ARM 96.6% · CRWD 68.0% · ABNB 49.6%
(cumulative since the IPO year) / 31.7% (ex-2020).** ABNB sits **below CRWD** — the name whose 68.0% closed
its file — on either reading. **But the direction is up for four straight years (27.1% → 35.1%), and SBC
is 13.0% of revenue.** SBC is subtracted in full; it is not the centre of this file the way it was at
CRWD, and saying so is the finding, not a softening.

**The market-value measure [E3-70] — the charge is the floor.** RSUs granted at grant-date fair value
(10-K Note 12; share counts rounded to millions in the filing, so ±$70M): 2024 13M × $153.36 ≈ $1,994M;
2025 16M × $136.11 ≈ $2,178M; less cancellations (2M × $143.07; 3M × $140.20) ≈ **$1.71bn (2024) and
$1.76bn (2025)**, plus ~1M options a year at $93.29 / $69.08 — against charges of $1,407M and $1,592M.
**On this measure owner earnings are ~$0.2-0.3bn a year lower than column A** (2025: ~$2.7bn). Stated as the
[E3-70] sensitivity; the charge-based figures above are the floor of the subtraction, as the framework says.

**The employee tax withholding on net share settlement — how it was treated.** A financing outflow:
*"Taxes paid related to tax on equity awards"* $1,527M (2020, the IPO settlement) / $177M / $607M / $1,224M
(2023, incl. *"$567 million of employee withholding tax"* on a May 2023 cashless option exercise) / $630M /
$561M / $305M (H1 2026). **Treatment: NOT subtracted from owner earnings a second time.** It is the cash
settlement of part of the same awards whose full grant value SBC already subtracts — economically the
company buying back, at market, the shares it would otherwise have issued. **It is counted with the
buybacks**, below, where it belongs: in the cost of holding the share count.

### Buybacks against dilution — the net share count
| | Dec 2020 | Dec 2021 | Dec 2022 | Dec 2023 | Dec 2024 | Dec 2025 | Jul 15 2026 (cover) |
|---|---|---|---|---|---|---|---|
| Class A + B outstanding (M) | 599.2 | 633.5 | 631 | 638 | 623 | 602 | **589.6** |
| gross repurchased (M) | — | — | 14 | 18 | 25 | 30 | 16 (H1) |
| repurchases $M | — | — | 1,500 | 2,252 | 3,430 | 3,789 | 2,139 (H1) |
| withholding $M | 1,527 | 177 | 607 | 1,224 | 630 | 561 | 305 (H1) |

- **Net change Dec 2022 → Jul 2026: -41.4M shares (-6.6%)** for **$16.4bn** of repurchases plus withholding —
  **~$397 of cash per net share retired**, against average repurchase prices of ~$107 (2022) to ~$140 (2024). Of ~103M shares
  bought from January 2022 (count 633.5M at Dec 2021), **~59M (net of withholding) were re-issued to employees**. The letter's own words:
  *"We repurchased $1.1 billion of Class A common stock during Q2 2026 to help manage the impact of share
  dilution"*; *"our fully diluted share count has decreased approximately 10%, driven by our share
  repurchases and cash used for employee tax obligations totaling over $16 billion"*.
- **Net change Dec 2020 → Jul 2026: -9.6M (-1.6%)**; Dec 2021 → Jul 2026: -43.9M (-6.9%).
- **The cash view, to the dollar:** OCF − capex − repurchases − withholding = **$1,298M / $361M / $424M /
  $263M** (2022-25). **Holding the count down ~3% a year absorbed 61% / 89% / 90% / 94% of operating cash.**
  That is capital allocation, not maintenance, and it is scored at Q3 — but it is the plainest measure of what
  employee ownership costs the other owners: **most of what the company earns is being spent buying back what
  it pays its people.**

### Taxes — a non-cash release, stated and set aside
2023 net income $4,792M includes a **$2,897M valuation-allowance release** (Schedule II, *"Credited to
Expenses | ( 2,897 )"*; cash-flow *"Deferred income taxes | ( 2,875 )"*). 2025 carries a **$213M valuation
allowance** against CAMT credits. **Neither touches cash; owner earnings come from cash; moved on.** Cash
taxes paid: $132M / $350M / $232M (2023-25).

### Great, good, or gruesome? **[E4-20]**
- [x] **great** — high return, rising, little capital needed
- [ ] good  [ ] gruesome
- Evidence: revenue 2.5× since 2019 ($4,805M → $12,241M) while capex **fell** ($126M → $33M) and property and
  equipment, net, is $107M. **The business runs on negative operating capital** — customer funds, unearned
  fees and payables exceed its operating assets — so the return on operating capital is not a meaningful
  number; income from operations $2,544M is earned on a balance sheet whose tangible operating base is
  approximately nil. **Qualification, stated:** the "little capital" is true of capex and false of people —
  ~$4.3bn a year of repurchases and withholding is what the equity-funded payroll consumes. The class is
  great on capital; the owner's share of it is thinned at the rate shown above.

### Staying power — score all three **[E5-11]**
- **(1) a large and reliable stream of earnings — PARTLY.** Large ($2.5-3.1bn ex-2020). **Not reliable
  through a travel stoppage**: 2020 OCF -$740M; in April 2020 the company took *"a $1.0 billion First Lien
  Credit and Guaranty Agreement"* at *"7.5% plus the London Interbank Offered Rate ... subject to a floor of
  1%"* and a second-lien loan with warrants, repaid in 2021 with *"Prepayment penalty on long-term debt |
  (213)"* and *"Loss from extinguishment of debt | 377"*. **That is the kindness of strangers [E5-39], priced.**
- **(2) massive liquid assets — YES.** Own cash, equivalents and short-term investments **$12.1bn**
  (2026-06-30; *"$12.1 billion of cash and cash equivalents, short-term investments, and restricted cash"*),
  undrawn $1.0bn revolver (*not counted* [E5-39]). The $12.2bn of customer funds is **not** counted: it is
  owed, and *"In certain jurisdictions, we are required to either safeguard customer funds in
  bankruptcy-remote bank accounts, or hold such funds in eligible liquid assets"*.
- **(3) no significant near-term cash requirements — YES, with one named exception.** Debt: **$2.5bn senior
  notes, first maturity $850M in March 2029**; interest ~$119M a year (my arithmetic on the 8-K coupons:
  850 × 4.400% + 850 × 4.650% + 800 × 5.250%). Leases $86M due 2026. Data hosting $219M due within a year.
  **The exception: the IRS Notice of Deficiency — *"$1.3 billion in tax, plus penalties and interest"*, which
  *"exceeds the current reserve ... by more than $1.0 billion"*,** in Tax Court since July 2024. Against $12.1bn
  of own liquidity it is survivable in full; it is named, not netted.
- **Score: 2.5 of 3.** Leverage, named and quantified [E4-16]: $2.5bn of covenant-light unsecured notes
  (*"limit the ability ... to ... create liens ... sale and leaseback ... consolidate"*; no financial covenant
  in the notes) against $12.1bn of own liquidity — **net cash ~$9.6bn**. **Coverage [E2-54]:** ~$119M of
  interest against ~$2.5-3.1bn of owner earnings net of capex — **~21-26×**. The revolver carries *"a leverage
  ratio and fixed charge coverage ratio"*; undrawn.

### Name the specific way THIS business dies **[E2-27, E3-24, E4-40]**
**The mechanism — THE PERMIT** *(a proposed seventeenth shape; checked against the index below).* **The
product is the right of private owners to rent their homes by the night, and that right is granted, capped
or withdrawn city by city by governments that the hotels lobby, while the same governments deputise the
platform to enforce the rules and collect — and increasingly pay — the tax.** The business does not die of a
competitor; it is **regulated out of its densest, highest-rate markets one ordinance at a time**, and each
jurisdiction also sends a bill.
- **Exposure, from the filing, not experience [E4-40]:** *"the City of New York has effectively banned
  short-term rentals, and this has led to similar restrictions being considered throughout the State of New
  York"*; *"the EU Short-Term Rental Regulation ... will enter into force in May 2026 and will require
  additional compliance efforts ... potentially discouraging and prohibiting current and potential hosts from
  listing properties"*; *"Host listings may also be limited by night caps, density restrictions, onerous
  permitting requirements, primary residence or host presence requirements, permit caps, minimum night stays,
  and/or discretionary permitting or lottery systems"*; *"Hotels and groups affiliated with hotels have engaged
  and will likely continue to engage in various lobbying and political efforts for stricter regulations"*;
  *"We have resolved some disputes by agreeing to remove listings or share data with authorities."*
- **What it has cost, from the filings:** **New York City: *"Prior to September, New York City represented
  approximately 1% of Airbnb global revenue"*** (Q3 2023 letter, `0001193125-23-268164`); *"Approximately 80%
  of our top 200 markets by revenue already have some form of regulation."* Italy: €576M + €139M + €179M =
  **$957M** settled for 2017-2023, with withholding now applied to Italian host payments. Spain: a proposed
  **€65M** fine for listing-rule non-compliance. Host withholding-tax reserves $199M (+$150-160M reasonably
  possible); lodging-tax reserves $114M (+$25-35M). G&A carried *"a $74 million increase from non-income taxes
  and related fees and penalties"* in 2025. **The 10-K quantifies no listing count or revenue lost to
  regulation beyond New York**; the absence is stated as "no instance found in the 10-Ks, 10-Qs and letters
  read".
- **Quantified, from filed figures (my arithmetic, 2025 base):** revenue $12,241M; merchant fees 13.6% of
  revenue are the only cost that falls one-for-one with bookings, so roughly **86% of lost revenue falls to
  operating income** in the short run. **A New York repeated across EMEA** — say one-fifth of EMEA's $4,729M
  (≈$946M, 7.7% of revenue) — takes ~$810M from operating income (2,544 → ~1,730) and owner earnings from
  ~$3.0bn toward ~$2.2bn: **survived.** **Owner earnings reach zero only when ~28-30% of revenue (~$3.5bn) is
  regulated away** — the equivalent of losing most of Europe, or North America's big cities and resort
  counties together. Even then, $12.1bn of own liquidity against $2.5bn of notes funds years of adjustment.
- **The second mechanism, carried beside it:** disintermediation of demand — *"If consumers become less reliant
  on search engines for travel searches and instead use AI apps and other channels, we may not be able to
  optimize for searches on these emerging channels"*; *"Some property managers and hosts encourage direct
  bookings, bypassing our platform"*. Not quantifiable from any filing read.
- **Likelihood:** [ ] likely · **[x] a real possibility** (continued erosion: market-by-market restriction that
  flattens nights growth in the core and raises the tax bill) · the death itself — ~30% of revenue regulated
  away — **a low-level possibility** on the filed record (New York was 1%; growth continued through it:
  nights +14% in 2023).
- **Against the index (16 shapes, four of them proposed, as read at 2026-09-13 after the IHG fold):** not #11 THE PASS-THROUGH (no capex race; gains are not competed away by
  customers but withdrawn by permit); not #13 THE TENANT (supply is millions of owners, none renting to
  every rival on a reset rent — though they do cross-list, see Q2); not #14 THE PATRON (no government funds the
  business; it permits it, and bills it); not #12 THE ADDRESS (one disputed jurisdiction); not #16 THE FLAG (owners re-flag to a rival brand at contract end — the
  nearest in kind, since Airbnb hosts also cross-list, but there is no contract end, no key money and no rival bid; the
  supply here is lost to the permit-giver, not to a rival). **Nearest is THE
  PATRON; the difference is that the patron pays and sets terms, while the permit-giver pays nothing, can
  withdraw the product itself, and makes the platform its tax collector.** Proposed as the seventeenth shape,
  pending the operator, like #13-#16.

- **VERDICT (RECORDED, NOT GOVERNING): [x] IN**  [ ] OUT  [ ] UNRESEARCHED  [ ] UNKNOWABLE
  *Owner earnings exist and are positive in every window without 2020 ($2.0-3.1bn) and in every window with it
  ($0.8-1.5bn); SBC resolves and is complete; (c) moves nothing; great on capital; [E5-11] 2.5 of 3; the named death
  (THE PERMIT) is a real possibility as erosion and a low-level possibility as death. Survival is not what closed this
  file.*

---
