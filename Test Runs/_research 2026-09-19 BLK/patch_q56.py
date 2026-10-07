import io, os, re
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "2026-09-19 Run - BLK BlackRock.md")
s = io.open(P, encoding="utf-8").read()

# ---- Q5 ----
i = s.index("## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND?")
j = s.index("## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?")
Q5 = r"""## Q5 — WHAT IS IT WORTH, AGAINST A GOVERNMENT BOND? — **COMPUTATION — NOT A CLEARANCE**

> ⛔ **OPERATOR RULE 3.** Q2 is **OUT on the business**. Q1-Q4 do **not** all show IN, so Q5 is not
> open. Everything below is arithmetic produced to discharge the operator's instruction of
> 2026-09-01 that every name carries a price. **It is not a clearance, it is not a valuation
> opinion for entry, and no entry language appears in it.** Arithmetic:
> `Test Runs/_research 2026-09-19 BLK/q5.py`, output in `q5.txt`.

**THE PRICE, AND THE SHARE COUNT.**
- **Price: US$1,069.78, the close of 2026-09-18.** Source: `tools/sources.py price("BLK")`, which
  reads an aggregator chart endpoint. **FLAGGED as an aggregator, used for the live quote only**,
  as operator rule 5 permits. Cross-check that the order of magnitude is right from a primary
  document: the FY2025 10-K states *"the intrinsic value of outstanding performance-based RSUs was
  $726 million reflecting **a closing stock price of $1,070**"* at 2025-12-31.
- **Share count: 162,476,186 — 154,869,259 shares of common stock plus 7,606,927 Class B-2 common
  units of BlackRock Saturn Subco, LLC, exchangeable one-for-one into common stock.** Taken
  verbatim from the cover of the latest periodic filing, **as of 2026-07-31, 10-Q accession
  `0001193125-26-337177`**: *"As of July 31, 2026, there were 154,869,259 shares of the
  registrant's common stock outstanding (162,476,186 on a fully diluted basis, including 7,606,927
  Class B-2 common units of a consolidated subsidiary, BlackRock Saturn Subco, LLC, which are
  exchangeable on a one-for-one basis into common stock of the registrant)."*
  **The Subco Units are included because they are economically common stock** — they carry the HPS
  sellers' claim on the same earnings, the filer itself adds them to diluted shares and to its own
  "shares outstanding including Subco Units" line, and the contingent consideration will issue
  more of them. Excluding them would understate the price of the business by 4.7%.
- **Market capitalisation: US$173,814M** (on common stock alone, $165,676M — shown so the reader
  can see the size of the choice).
- **Split-invariance: `tools/sources.py split_factor_after("BLK","2026-06-30")` returns 1.0.** No
  split intervenes between the measurement date and the anchor.

**THE FLOOR, BEFORE ANY RANKING [E4-28, E3-13].** *"that's the figure we quit on … we don't want to
buy equities where our real expectancy is below 10 percent. Now, that's true whether short rates
are 6 percent or whether short rates are 1 percent."*

- Owner earnings, after tax, from Q4: **$4,756M to $5,583M**.
- Grossed to a pre-tax expectancy at the 2025 **book** rate of 22.0%: **$6,097M to $7,158M**; at the
  2025 **cash** rate of 30.2%: $6,814M to $7,999M. The conservative (book-rate) figures are used.
- **Honest pre-tax expectancy at this price: 3.51% to 4.12%, plus growth of roughly zero** —
  because owner earnings **per share** compounded at **+0.13% a year (c = capex) to −3.28% a year
  (c = D&A)** over 2021-2025, on the filed series in Q4.
- **THE FLOOR IS ~10%. THE SHORTFALL IS 5.9 TO 6.5 POINTS.** To reach the floor from this price the
  business would have to compound owner earnings per share at **5.88% to 6.49% a year, in
  perpetuity**, against a four-year record of zero. **[E4-35]** sets the burden of proof that
  belongs on that belief and it is heavy; **[E4-44]** sets the second bound — *"the value of an
  asset, whatever its character, cannot over the long term grow faster than its earnings do"*.
- **BELOW THE FLOOR. The name is not ranked; it is quit on [E4-28]. The ranking lines below are
  therefore not filled in.**

**1. THE YIELD**
- owner earnings **$4,756M to $5,583M** ÷ market cap **$173,814M** = **2.74% to 3.21%** ·
  sovereign **5.34%** (US Treasury 30-year par yield, 2026-09-18, issuing authority).
- On common stock alone: 2.87% to 3.37%. **Either way, the owner's earnings yield is roughly
  half the government bond.**

**2. WHAT THE PRICE ALREADY ASSUMES**
- Perpetual growth implied at the bare sovereign, no risk premium added **[E3-42]**:
  g = 5.34% − 2.74% = **2.60%** at the conservative end; 5.34% − 3.21% = **2.13%** at the
  optimistic end.
- **What the business has actually done: 0.0% to −3.3% a year in owner earnings per share over four
  years, on 40.3% more assets under management.** The quote requires perpetual real-ish growth from
  a business whose per-unit price has fallen every year in every organically owned product.

**3. WHAT YOU ARE PAID**
- **−2.60 to −2.13 points versus the sovereign.** The buyer accepts about two and a half points
  *less* than the 30-year Treasury, in exchange for the growth above.

**WHERE CERTAINTY IS PRICED — AND IT IS NOT IN THE RATE [E3-42].**
- Sovereign used **5.34%** — **the bare rate, no per-name premium added.** *"It may look
  mathematical. But it's mathematical gibberish."*
- Certainty was handled twice and neither place is the rate: at the understanding gate (**Q1 IN** —
  this business is understandable) and in the end discount, which is never reached because the
  floor already fails.
- **Windage count: ONE, and it was applied at Q4** — stock pay taken at the larger of the reported
  charge and the [E3-70] grant-date market value. No second application here. **[E4-11, E4-48]**.

**THE VALUE, AS A ROUND-NUMBER RANGE [E4-01]** — *"Using precise numbers is, in fact, foolish."*
- **Conservative — owner earnings capitalised at the bare sovereign with no growth:
  roughly $550 to $650 a share** ($89,064M to $104,551M).
- **Optimistic — the same range with 2% perpetual growth allowed (r − g = 3.34%):
  roughly $875 to $1,030 a share** ($142,395M to $167,156M).
- **Current price: $1,069.78 a share, $173,814M.**
- **The price sits ABOVE the whole range, including the optimistic end that already grants
  perpetual 2% growth to a business whose per-share owner earnings have not grown in four years.**

**WHAT THE BUYER IS PAYING FOR, IN WORDS** — required by the brief, and it is the most useful
paragraph here.
At $1,069.78 the buyer pays **$173.8 billion** for **$4.8 to $5.6 billion** of owner earnings:
**31 to 37 times**. Put in the units of the business itself, the buyer pays **1.13% of the $15.3
trillion of assets under management** for the right to earn **0.152% a year** on them — **nine
years of gross base fees, before a single cost, just to return the purchase price.** The multiple
of GAAP net income is 31.3x; of "as adjusted" net income, 22.5x; of book value per share, 2.88x.
**So what is actually being bought, in plain words:** a toll of fifteen hundredths of one per cent
on the world's savings, which has been cut in every product every year for five years, plus an
option on two things — that the $28.3 billion of purchased private-markets managers reach the
stated *"ambition to raise $400 billion in private markets by 2030"* at ninety basis points instead
of fifteen, and that Aladdin keeps compounding at ten per cent organically from 8.2% of revenue.
**Those two options are the entire difference between $650 and $1,070 a share.** The buyer is not
paying for the fee stream; the fee stream at the bare sovereign is worth about six hundred dollars
a share. The buyer is paying roughly **$450 a share, some $73 billion, for the private-markets and
technology options**, against $8.4 billion of contingent consideration still to be issued in paper
to the people who sold them.

**WHICH BAR** *(never both on the same number)*
- [ ] **Normal method [E4-11]** — not used. It is not reached: the floor fails before a margin is
      applied, and applying a margin to a price already above the optimistic end would be theatre.
- [x] **Screamer test [E4-01]** — does the price already clear the **conservative** case? **No. The
      price is above the whole range.** Three outcomes, and this is the third: *price above the
      whole range → no.* **[E3-25]**: *"it ought to just kind of scream at you."* It does not.

- **VERDICT: would be a FAIL ON PRICE, and BELOW THE FLOOR, had the gates been reached. NOT
  RANKED — quit on [E4-28]. No ranking position is assigned. This is a COMPUTATION, NOT A
  CLEARANCE.**

"""
s = s[:i] + Q5 + s[j:]

# ---- Q6 ----
i = s.index("## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?")
j = s.index("## SELF-AUDIT")
Q6 = r"""## Q6 — WHAT WOULD PROVE ME WRONG, AND WHEN DO I SELL?

**Nothing is held and nothing is being bought, so there is no sell rule to pre-commit. What [E1-02]
requires instead is that the yardsticks be written down BEFORE the fact, so the reopening of this
file is decided by evidence and not by a later mood:** *"I believe in establishing yardsticks prior
to the act."* **Nothing is armed. No band goes into `tools/alerts.json` and no `PORTFOLIO.md` row is
added, because the file closed at Q2 on the BUSINESS** — a price alert on a business rejected for
what it is would be a category error (the QLYS ruling, 2026-09-07).

**THE REFUTATION RECORD — what would prove this Q2 verdict wrong, stated so a future reader can
test it against a filing rather than against my judgment.**

| # | the claim this run made | the filed fact that would refute it | where it would appear |
|---|---|---|---|
| 1 | The ETF price is competed away and cannot be raised | **iShares Core S&P 500 (IVV) raises its total annual fund operating expense ratio above 0.03% and does not lose share**, or Vanguard raises VOO above 0.03% first | iShares Trust 485BPOS; Vanguard Index Funds 485BPOS |
| 2 | The blended fee rate holds only because product was bought | **The total effective fee rate rises for three consecutive years EX the private-markets leg** (base fees less private-markets fees ÷ average AUM less private-markets average AUM), from the 13.64bp of 2025 | 10-K MD&A, the base-fee and average-AUM-by-product tables |
| 3 | Base fees grow slower than the assets they are charged on | **Base-fee growth exceeds average-AUM growth for two consecutive years** | same tables |
| 4 | Owner earnings per share are going nowhere | **Owner earnings per share above $37.16 (the 2024 capex-end peak) for two consecutive years**, computed on ex-CIP operating cash less stock pay at the larger of charge and grant value | 10-K cash-flow statement, the CIP reconciliation, the stock-compensation note, the cover share count |
| 5 | The private-markets build is an option, not a franchise | **Private-markets fee-paying AUM reaches the stated $400bn by 2030 at a fee rate at or above 89.85bp, with no further acquisition consideration issued** | 10-K AUM roll-forward and revenue-by-product tables |
| 6 | Aladdin is too small to reclassify the whole | **Technology services and subscription revenue exceeds 20% of total revenue with organic ACV growth above 15%**, i.e. it becomes the business rather than a twelfth of it | 10-K revenue table and the ACV disclosure |

**THE MONITORING METRIC, if this name is ever looked at again: the effective fee rate by segment,
ex acquisitions.** **[E4-32]** — direction outranks existence — and **[E4-37]** — *"you can almost
measure the strength of a business over time by the agony they go through in determining whether a
price increase can be sustained."* The day a BlackRock filing describes an attempt to raise a price
is the day this file should be reopened. There is no such passage in five years of filings.

**[E4-17] and [E3-30] on how a view like this one should change:** *"beliefs change quite
gradually"*, and the monitoring question is *"whether this erosion is just part of an aberrational
cycle … or whether the business has slipped in a way that permanently reduces intrinsic business
values."* The finding here is not an erosion of BlackRock's *position* — its position is
strengthening, and iShares crossed $6 trillion. **It is that the position does not carry a price.**
That is a slower and more permanent thing than a cycle, and the refutation table above is
deliberately built out of three-consecutive-year and two-consecutive-year tests so that one good
quarter cannot reopen it and three good years must.

**The sell rule [E2-28] — recorded for completeness, not applied:** two triggers (the market
judging the business more valuable than the facts indicate; funds needed for something more
undervalued or better understood) and three hold conditions (return on equity capital
satisfactory, management competent and honest, market not overvaluing). **Not applicable: no
position exists.** Price appreciation and holding period remain explicitly rejected as reasons to
sell.

**Position size — a judgment, stated [E3-45]: ZERO, and not because of the price.** The business
failed Q2. **[E5-35]**: *"You can turn any investment into a bad deal by paying too much. What you
can't do is turn any investment into a good deal by paying little."* A lower price would make this
a cheaper non-franchise, which is a different thing from an opportunity. **Sized down further, if
that were possible, by the live capital-allocation flag at Q3.**

- **VERDICT: [x] IN** — the refutation record is written, dated, and tied to named filed series
  with thresholds pre-committed **[E1-02]**. Nothing is armed.

"""
s = s[:i] + Q6 + s[j:]

io.open(P, "w", encoding="utf-8").write(s)
print("Q5 and Q6 written")
