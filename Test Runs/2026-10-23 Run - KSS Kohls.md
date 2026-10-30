# Company Run: Kohl's Corporation (NYSE: KSS), 2026-10-23
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Template:
`Test Runs/_TEMPLATE - Company Run.md`, copied to this file and committed (commit 2b97678b) before any fetch. A dispatched
purchase run of record under operator rule 10; the dispatching session holds the lock.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared:** nothing about Kohl's from any blind-listed file was seen. Seen by accident and not used: the
session's opening git status, which names research folders of other companies (`_research 2026-09-26 AYI`,
`_research 2026-09-27 ARCB`) and daily digest files; the five latest commit subjects (a BETA run and its fold, a utility-alert
restatement); and the auto-memory index lines on the queue state (a wave count, a count of gate-clearers, "nothing
buyable"), which name no company relevant here. The brief itself says an earlier Kohl's run exists; it was not opened, listed
or searched. Only this run's research folder was listed.

---
## STEP 0: THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $24.00 (2026-10-23, live quote via `tools/run.py`; an **aggregator quote, flagged** under operator rule 5).
- **Shares:** one class, common stock $.01 par. Cover of the 10-Q for the quarter ended August 1, 2026 (filed 2026-09-03,
  accession `0001193125-26-381893`): **113,376,445** shares as of 2026-08-28 (`python Screens/cover_shares.py KSS`).
  Cross-check against the same 10-Q's equity statement: 129 million issued less 16 million treasury = 113 million. No 8-K or
  prospectus filed after the 10-Q issues shares (the 8-Ks of 2026-08-25, 2026-08-31 are officer changes; 2026-08-18 a dividend).
- **Market cap:** 113.376M x $24.00 = **$2,721M**.
- **Sovereign for the earnings currency (USD):** **5.29%**, US Treasury daily par yield curve, 30-year, 10/22/2026
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4):
  - 10-K for fiscal 2025 (year ended January 31, 2026), filed 2026-03-19, accession `0001193125-26-115982`: Items 1, 1A, 2,
    3, 5, 7, the statements, notes 2 (debt), 3 (leases), 5 (taxes).
  - 10-K filings for fiscal 2016 to fiscal 2024 (the cycle): `0000885639-17-000007` (FY2016), `0001564590-18-006671`
    (FY2017), `0001564590-19-009005` (FY2018), `0001564590-20-011512` (FY2019), `0001564590-21-014145` (FY2020),
    `0000950170-22-004076` (FY2021), `0000950170-23-008444` (FY2022), `0000950170-24-034691` (FY2023),
    `0000950170-25-042662` (FY2024): statements, comparable sales, liquidity sections, buyback tables.
  - 10-Q for the quarter ended August 1, 2026, filed 2026-09-03, `0001193125-26-381893`: statements, debt note, MD&A.
  - Proxy (DEF 14A) filed 2026-04-10, `0001104659-26-041769`: CD&A summary, incentive design, ownership table.
  - 8-Ks: 2026-08-31 `0001193125-26-377068`, 2026-08-26 `0001193125-26-365860`, 2026-08-25 `0001193125-26-365317`,
    2026-08-18 `0001193125-26-355669`, 2026-07-29 `0001193125-26-323775`, 2026-07-01 `0001193125-26-292702`,
    2026-06-15 `0001193125-26-271291`, 2026-05-21 `0001193125-26-234927`, 2026-01-28 `0001193125-26-027292`,
    2025-05-01 `0001193125-25-109074`, 2025-05-08 `0001193125-25-115230`, 2022-07-01 `0001193125-22-186676`,
    2022-06-07 `0001193125-22-168602`, 2021-04-14 `0001193125-21-116440`.
  - **One figure cross-checked against the filed statement:** net cash provided by operating activities for fiscal 2025,
    $1,380M in the filed cash-flow statement of `0001193125-26-115982`, equals the XBRL figure `tools/run.py` printed (1,380).
- **`python tools/run.py KSS`, arithmetic lines only** (output kept in `Test Runs/_research 2026-10-23 KSS/run_py_output.txt`):
  OCF less SBC less capex, three years: 549, 152, 974 (FY2023 to FY2025); finance-lease principal printed as an alternate
  (78, 74, 75) and not in its capex column. The tool's figures are checked against the filed statements below and
  superseded by the run's own recast (Q4 material, written under AFTER THE STOP). Nothing it printed as a rule, a yield
  verdict or an id is used (Part VII, the tooling).

### The balance sheets, ten year-ends, read in Step 0 because the file closes before Q4
The rule: "balance sheets over an 8 or 10 year period before I even look at the income account" **[M2025-032]**.
From the filed balance sheets (FY2016, FY2019, FY2022, FY2025 10-Ks and the 10-Q; the run.py table is the transcription):

| year-end | total assets | equity | cash | inventory | long-term debt | lease/financing obligations (cap/finance) | operating lease liab. |
|---|---|---|---|---|---|---|---|
| 2017-01-28 | 13,574 | 5,177 | 1,074 | 3,795 | 2,795 | 1,816 (131 + 1,685) | not on sheet (pre ASC 842) |
| 2019-02-02 | 12,469 | 5,527 | 934 | 3,475 | 1,861 | 1,638 | not on sheet |
| 2020-02-01 | 14,555 | 5,450 | 723 | 3,537 | 1,856 | 1,491 | 2,777 |
| 2022-01-29 | 15,054 | 4,661 | 1,587 | 3,067 | 1,910 | 2,251 | 2,624 |
| 2023-01-28 | 14,345 | 3,763 | 153 | 3,189 | 1,912 (incl. 275 current) + 85 revolver | 2,880 | 2,689 |
| 2026-01-31 | 13,362 | 4,048 | 674 | 2,745 | 1,436 | 2,450 | 2,744 |
| 2026-08-01 (10-Q) | 13,410 | 4,168 | 821 | 2,913 | 1,325 | 2,387 | 2,709 |

What moved and why. **Equity** fell from $5,177M to $4,048M over the nine fiscal years FY2017 to FY2025, in which the company earned a
cumulative $3.8B, bought back $3.2B of stock and paid $2.2B of dividends (cash-flow statements); the collapse of **retained earnings** from
$13,995M to $1,223M is not a loss: the FY2023 and FY2024 equity statements retire $11,155M and $1,811M of treasury stock
against retained earnings. There is **no goodwill** and no customer receivables on the sheet (the credit-card accounts are
owned by a bank). **Inventory** fell 28% (3,795 to 2,745) against net sales down 21% (18,686 to 14,775): inventory per dollar
of sales improved, which the FY2025 10-K credits to receipts down 8% and fewer clearance markdowns. **Cash** swung from
$1,587M (FY2021) to $153M (FY2022) after $1.4B and $0.7B of buybacks, a $85M revolver draw and a $275M current maturity,
then rebuilt to $821M. **Debt:** notes fell from $2,795M to $1,342M principal, but finance-lease and financing obligations
rose from $1.8B to $2.4B and operating-lease liabilities of $2.7B came onto the sheet in 2019; total borrowings plus all lease
liabilities were about $6.4B at January 31, 2026 (1,436 + 2,450 + 2,744) against equity of $4.0B. The newest note (2030,
10.000%, $360M) is **secured** by eleven distribution and fulfilment centres, and the 2031 notes carry a coupon that has
stepped up 175 basis points on downgrades (10-K note 2). What the figures cannot say: the value of the 402 owned stores and
242 ground-leased ones (Item 2), carried at depreciated cost.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would own Kohl's "if the market closed for five years" **[M1997-109]**, which
turns the question to what a department store chain will earn over a decade, not to the meme-stock trading of its shares.
No macro forecast enters: tariffs and the consumer named in Item 1A are not forecast here; what counts is "the average
profitability of the business over time and how strong its competitive mode is" **[M2015-016]** (the transcript's word).
Margin of safety: if the decision needs pencil and paper, "it’s too close to think about" **[M1996-084]**. The analyst's
habit, written down at once **[M1997-127]**. **Contrary evidence, written down as found:** (1) net sales fell from $19,204M
(FY2015) to $14,775M (FY2025), comparable sales were negative in seven of the ten years measured from FY2014 to FY2025 (FY2020 and FY2021 not
reported as comparable), and transactions fell about 4% in FY2025 (10-K FY2025); (2) Moody's corporate rating B2 and S&P B+ at January 31, 2026, down from Baa2/BBB in
2020; (3) the chief executive hired in January 2025 was terminated for cause on April 30, 2025 after an Audit Committee
investigation (8-K `0001193125-25-109074`); (4) the annual bonus for FY2025 paid 185.4% of target in a year when net sales
fell 4.0% (proxy). Against the case against: FY2025 gross margin rose 34 basis points to 37.5%, inventory fell 7%, operating
cash flow was $1.38B, no revolver borrowing at year-end, and Q2 FY2026 comparable sales were down only 0.9%.

## THE STANDING RULE
The buyer's own conduct: nothing in this run proposes borrowing to buy, a size that could force a sale, or an exposure that
could bring "sudden demands for large sums" **[L2014-024]** on the buyer; "Never risk permanent loss of capital." **[L2023-005]**
is the buyer's rule and is not engaged by a run that closes OUT. Not engaged.

---
## Q1: CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
  five or 10 years" and "where the company will stand within the industry" **[M2012-065]**. The key variables, "evaluating how
  predictable they were first" **[M1998-044]**: (1) store traffic and comparable sales; (2) gross margin, which turns on markdowns and
  the private-brand mix (proprietary brands carry "lower selling prices, but higher gross margins", Item 1); (3) SG&A
  against a fixed store base of 1,153 stores (Item 2); (4) other revenue, chiefly the credit-card income from the program
  with Capital One that ends March 31, 2030 (FY2022 10-K, the amended agreement of March 14, 2022); (5) rent and lease
  renewals. Each is reported, by year, in the filings read; the history of each over a decade can be laid out from them.
- **Is the industry one of fast change that puts the ten-year economics out of reach?** The product is moderately priced
  apparel, footwear, home and beauty sold in strip-centre stores (936 of 1,153) and online (29% of net sales). The forecast is
  about customers, "laying out what their prospective customers will do in the future" **[M2017-019]**, "what we think we can project out in terms of consumer behavior"
  **[M2023-030]**. The industry's insiders do write such forecasts down (the company guides a sales decline of 2% to flat for
  2026, 10-K FY2025), so test 5 does not send it to TOO HARD (NATURE): these are not forecasts of which insiders "would say, “That’s too
  hard.”" **[M2000-105]**.
- **Contrary evidence on Q1 itself, written down:** the speakers name retail as the field they most often misjudged: "it’s
  easy to sort of think you understand retail, and then subsequently find out you don’t, as we did with the department store
  in Baltimore." **[M2014-052]**; and "if you have doubts about something being into your circle of competence, it isn’t."
  **[M2002-092]**. Weighed: the doubt the rows describe is about believing a retailer's future is good when it is not. The
  reading here forecasts no improvement; the ten-year economics it can foresee is a smaller chain at a lower margin, which
  is the direction every reported series has run for a decade. The routing rule fixes that a business whose economics can
  be seen passes to Q2, where "a castle shown on the evidence to be filling in closes OUT" (Q1, The routing, fixed).
- **VERDICT: IN.** The business is simple and its key variables are reported and readable over the cycle: "you really do know
  the key variables" **[M1998-044]**, and "a reasonable fix on about what the earning power and competitive position will look
  like in five or 10 years" **[M2012-065]** is available from the filings. The doubt ("it’s easy to sort of think you
  understand retail" **[M2014-052]**) is carried to Q2, where the castle is tested on the filings.

## Q2: WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what’s going to keep it standing or cause it not to be standing five,
10, 20 years from now." **[M1995-038]**. A moat is what "protects excellent returns on invested capital" **[L2007-004]**.

**The parts table.** None: the filer "operates as a single reportable segment" (10-K FY2025, note 1). The credit-card
income is not a segment but is read below, since in FY2025 other revenue ($752M, chiefly credit) exceeded operating income
($624M) (10-K FY2025, statement of operations).

**The castle tests, each with its filing fact.**
1. *What keeps it standing, and how permanent?* The draws the filer names are "product and value", with "Merchandise mix,
   brands, service, loyalty programs, credit availability, and customer experience" (Item 1, Competition). The one line that
   grew in FY2025 was Accessories "including Sephora", +2.0%; Women's -5.7%, Men's -4.8%, Home -4.3%, Children's -6.5%,
   Footwear -6.9% (MD&A). The Sephora shops are another company's brand on a shared-profit arrangement: "The parties share
   equally in the operating profit of the arrangement" (10-K FY2025, critical estimates). Asked for the "key factors" and
   "how permanent" they are **[M1995-038]**, the answer is that the growing draw is rented and its profit is split.
2. *Would it stand without the lord?* "In retailing, to coast is to fail." **[L1995-008]**; for a retailer the backward
   nephew "would be an express ticket to bankruptcy" **[L1995-009]**. Filing facts: the chief executive whose agreement was
   dated January 15, 2025 was terminated for cause on April 30, 2025 and a director became interim chief executive
   (8-K `0001193125-25-109074`; 10-K FY2025, executive officers); in 2026 the director of stores retired, the chief
   marketing officer's post was eliminated and the chief merchandising officer departed (8-Ks of 2026-01-28, 2026-08-25,
   2026-08-31). A business that needs its managers this much fails the test: "the poor business is one that can only succeed,
   or even survive, with great management." **[M1996-037]**
3. *The money test.* The attackers did not need to be imagined; they came with money and grew. From their own 10-K filings
   (XBRL facts of those filings, transcription): TJX revenue rose from $30,945M (FY2015) to $60,372M (FY2025); Ross from
   $11,940M to $22,751M; Burlington from $5,130M to $11,567M; Kohl's net sales fell from $19,204M to $14,775M over the same
   years. "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**; "there are some industries that are just
   never going to have barriers to entry" **[M2012-106]**; "one competitor is frequently enough to ruin a business."
   **[M2012-108]**.
4. *Pricing power.* The filer's own words: "As consumer behavior shifts toward a value-seeking mindset", and the migration to
   digital channels "has increased our challenges in differentiating ourselves from other retailers especially as it relates
   to national brands" (Item 1A). Gross margin on net sales was 36.4% (FY2014), 36.0% (FY2017), 33.2% (FY2022), 37.5%
   (FY2025): no rise over the decade while unit volume fell, the opposite of "charge more for a product and maintain or
   increase market share" **[M2000-031]**.
5. *Unit volume.* The FY2025 sales decline "was driven by an approximately 4% decrease in transaction volume" (MD&A); FY2022
   net sales fell "as a result of lower traffic" (10-K FY2022, MD&A). Comparable sales: FY2014 -0.3%, FY2015 +0.7%, FY2016
   -2.4%, FY2017 +1.5%, FY2018 +1.7%, FY2019 -1.3%, FY2020 and FY2021 not reported, FY2022 -6.6%, FY2023 -4.7%, FY2024
   -6.5%, FY2025 -3.1%; Q2 FY2026 -0.9% (10-Q). "Fixed costs are high in the newspaper business, and that's bad news when
   unit volume heads south." **[L2006-009]** (said of newspapers; quoted for the mechanism only).
6. *The low-cost position.* Kohl's is not it. The off-price chains sell branded apparel and home goods and earn more on each
   dollar of sales and on their assets (competitor row below). "commodity businesses have risk unless you’re the low-cost
   producer" **[M1997-010]**; "you do not want to have something whose competitive position is going to erode over time."
   **[M2007-117]**.
7. *The brand.* Does the customer ask for it by name, "if they ask for you by name" **[M2023-073]**? The filer calls its brand and private brands "powerful
   sales and marketing tools" (Item 1A); the sales by line say the name is not pulling volume, and the growing line carries
   Sephora's name.
8. *The low bid.* The customer the filer describes is value-seeking and compares prices across channels (Item 1A). "most
   insureds don't care from whom they buy" **[L2004-003]** is the failing answer in its own field; the filer's description of
   its customer is the retail form of it.
9. *Ask the competitors.* Not available on the public record. The proxy's incentive "Performance Index" chooses eight
   retailers, Macy's, Nordstrom, Gap, Ross, TJX, Dick's, Foot Locker and Ulta (DEF 14A 2026, p. 83): the company measures
   itself against the off-price chains that took its volume.
10. *Widening or narrowing?* Narrowing on every filed series: net sales down 23% over ten years; other revenue $1,089M
    (FY2019) to $752M (FY2025); 1,154 stores at January 28, 2017 (10-K FY2016) and 1,153 at January 31, 2026 with sales
    per store lower; corporate ratings from Baa2/BBB (10-K FY2019) to B2/B+ (10-K FY2025). "the competitive position of each
    of our businesses grows either weaker or stronger" **[L2005-010]**; the newspaper "lost a notch" **[L1995-023]**, and
    this business has lost several.
11. *What could "destroy, or modify, or reduce the economic strengths"* **[M2000-014]**, five to fifteen years out: (a) the credit-card program agreement with Capital One
    "ends on March 31, 2030" (10-K FY2022, Liquidity), inside the ten years, and the other revenue it chiefly carries is larger
    than FY2025 operating income; the FY2025 10-K adds that the program's profitability "is sensitive to the economic health
    of our core moderate-income customer" (Item 1A); (b) continued traffic loss to off-price and online rivals (Item 1A).

**The competitor row**, same metrics, each from the rival's own 10-K filings (XBRL company facts of those filings,
transcription; latest 10-K accession given), ten fiscal years FY2016 to FY2025:

| company | latest 10-K read (accession) | revenue FY2015 to FY2025, $M | growth a year | net income / revenue, 10-yr sum | (OCF - capex) / revenue, 10-yr sum | net income / average total assets |
|---|---|---|---|---|---|---|
| Kohl's | `0001193125-26-115982` | net sales 19,204 to 14,775 (total revenue 15,527) | -2.6% (net sales) | 2.4% | 4.7% | 3.1% |
| Macy's | `0001628280-26-021721` | 27,079 to 22,621 | -1.8% | 1.6% | 4.3% | 2.1% |
| Nordstrom | `0000072333-25-000039` (FY2024, the last found) | 14,437 to 15,016 (FY2024) | +0.4% | 1.5% | 2.4% (9 yrs) | 2.6% |
| Dillard's | `0000028917-26-000006` | 6,755 to 6,563 | -0.3% | 6.7% | 8.4% | 12.3% |
| TJX | `0000109198-26-000008` | 30,945 to 60,372 | +6.9% | 7.3% | 7.2% | about 13% |
| Ross | `0000745732-26-000006` | 11,940 to 22,751 | +6.7% | 8.8% | 9.0% | 13.7% |
| Burlington | `0001193125-26-116001` | 5,130 to 11,567 | +8.5% | 4.1% | 3.4% | 5.4% |

Flagged: **JCPenney**, a direct department-store rival, is not a current SEC filer (sold out of bankruptcy in 2020; not
verified from a filing) and is not in the row. **Nordstrom** filed no 10-K after March 2025 in its XBRL facts and is shown to
FY2024. Amazon appears in the filer's 10-K only as a commercial counterparty (warrants issued 2019, note 6) and is not
compared. Scripts and output: `Test Runs/_research 2026-10-23 KSS/scripts/peer.py` and `peer2.py`.

**The field's returns over the last full cycle, judged in words.** The span covers the 2020 closure year, the 2021 rebound and
the 2022 to 2025 decline. Across it the field splits in two. The broad department stores (Kohl's, Macy's, Nordstrom) shrank
or stood still and earned two to three cents of net income on a dollar of sales and two to three percent on their assets:
poor returns, below any reading of ordinary. Dillard's earned well on its assets without growth. The off-price chains
doubled and earned seven to nine cents on the dollar (Burlington four) and up to about thirteen percent on assets. The
castle that protects "excellent returns" **[L2007-004]** is theirs, and they built it on the volume the broad department
stores lost. "you can have only two competitors and they’re still terrible businesses" **[M2013-052]** describes the broad
department store; "Another way to prosper in a commodity-type business is to be the low-cost operator." **[L2004-007]**: that route belongs to the off-price chain.

**A change for the better?** Q2 FY2026: comparable sales -0.9%, gross margin 43.0% (+305 basis points, with about $100M of
tariff refunds recognized in gross margin), net income $151M (10-Q). The Q2 convention credits a change for the better only
on the evidence of a full cycle (Q2, Change), since "you learn a lot about the durability of the economics of a business by
observing the behavior of — the price behavior" **[M2005-020]**; one quarter, flattered by
a one-off refund, is not that evidence and is not credited.

**The other side's case, stated as strongly as the filings allow:** operating cash flow was $1.38B in FY2025; inventory
discipline improved (receipts -8%); the owned store base (402 owned, 242 ground-leased) is real; FY2025 adjusted operating
income held at $510M against $509M while sales fell 4%; and the fall in comparable sales narrowed from -6.5% to -3.1% to
-0.9%. These are signs of a business managed for cash in decline, not of a castle; none shows the customer choosing Kohl's
over the low bid or the volume returning.

- **VERDICT: OUT.** The castle is shown open on the evidence of a decade: the attackers with money came and doubled while this
  business lost 23% of its net sales and had negative comparable sales in seven of ten measured years; it is not the low-cost
  operator in a field whose customer, by the filer's own account, buys on value; and the profit that remains leans on a
  credit agreement that ends in 2030. The castle question answered yes, "If the answer had been yes, we wouldn’t have done it." **[M2011-015]**, and
  "you do not want to have something whose competitive position is going to erode over time" **[M2007-117]**; it is "a declining department store" **[M2014-088]**, and "If you really think a business is declining,
  most of the time you should avoid it." **[M2012-062]**. Price does not reopen it: "What you can’t do is turn any investment
  into a good deal by paying little" **[M2019-015]**.

## Q3 to Q12: NOT REACHED
Q2 is a STOP and closed OUT; Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 and Q12 are NOT REACHED (operator rule 2). Q11 belongs to a
holding review. The facts already found that bear on them are below, written down and not weighed.

---
## THE BOX
**OUT at Q2** (the castle shown open on the evidence: ten years of lost volume to the off-price chains, not the low-cost
operator, the remaining profit leaning on a credit agreement that ends March 31, 2030). **Integrity facts recorded, not
judged** (Part VII): the chief executive terminated for cause in April 2025 after an Audit Committee investigation of an
undisclosed vendor relationship. COMPUTATION, NOT A CLEARANCE, beneath the stop: value range $32.94 to $102.23 a share
(all-equity, central) against $24.00.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Each with its source, "write it down in the first 30 minutes" **[M1997-127]**; no verdict; the box unchanged (operator rule 2).*

**Bearing on Q3 (capital):** capital spending $605M, $826M, $577M, $466M, $372M (FY2021 to FY2025) against depreciation and
amortization $838M, $808M, $749M, $743M, $700M; FY2026 capex guided at $350M to $400M (10-K FY2025). Spending has run at
about half of depreciation for two years while 27 stores and two fulfilment centres closed (10-K FY2025, MD&A). The filing
states no maintenance figure. Net income on average total assets 3.1% over FY2016 to FY2025 (competitor row).

**Bearing on Q4 (the accounts):** the ten balance sheets read in Step 0 raise no accounting suspicion found in this run:
inventory fell faster than sales, no goodwill, no receivables build. The retained-earnings fall is treasury-stock retirement
(equity statements FY2023, FY2024). Habits recorded for Q4 and Q5: the company gives annual guidance on "Adjusted operating
margin" and "Adjusted diluted EPS" (10-K FY2025, outlook); its earnings releases present "adjusted EBITDA, adjusted EBITDAR,
our leverage ratio (expressed as net debt + leases / EBITDAR)" (8-K `0001193125-26-365860`); the FY2025 adjustments remove
both the $129M legal-settlement gain and the closing costs (10-K FY2025, reconciliation), so the adjusted operating income
($510M) was below the GAAP figure ($624M) that year.

**Bearing on Q5 (integrity, recorded and not judged):** on April 30, 2025 the board terminated the chief executive for cause:
an investigation "conducted by outside counsel and overseen by the Audit Committee" found that he "had directed that the
Company conduct business with a vendor founded by an individual with whom Mr. Buchanan has a personal relationship on highly
unusual terms favorable to the vendor" and did not disclose it; he forfeited his equity awards and owes $2.5M of his signing
incentive; the 8-K states the matter "is not related to the Company’s performance, financial reporting or results of
operations" (8-K `0001193125-25-109074`). A director, Michael Bender, became interim chief executive and then chief
executive in November 2025 (10-K FY2025). Directors and executive officers as a group own 1.55% (DEF 14A 2026, ownership
table). Any later run that reaches Q5 must answer these facts: "If you’ve got doubts, forget it." **[M2013-088]**.

**Bearing on Q6 (the money and the owners):**
- Buybacks: $677M (FY2014), $1,001M (FY2015), $557M (FY2016), $306M (FY2017), $396M (FY2018), $470M (FY2019; fourth-quarter
  average price $50.53), $8M (FY2020), $1,355M (FY2021), $658M plus the ASR settlement (FY2022; the $500M ASR had "an average price of
  approximately $28 per share"), none since (cash-flow statements; 10-K FY2019 and FY2022, Item 5 and Liquidity). The program named no
  price; the 10-K says repurchases depend on "available cash balances, our stock price, and other factors". Against the
  COMPUTATION below, the FY2019 and FY2021 purchases near $50 sit above the bottom of the computed range ($32.94) and the
  FY2022 ASR near $28 below it; written down, not weighed.
- Dividend: $2.00 a share in FY2022 to FY2024, cut to $0.125 a quarter in 2025 ($0.50 for FY2025) and held there (8-K
  2026-08-18).
- Notes bought below par in the open market: $87M in Q4 FY2025 and $113M in the first half of FY2026, with gains on
  extinguishment of $11M and $15M (10-Q, note on debt).
- Sale process, 2022: more than 25 parties approached; a $60.00 a share proposal from Franchise Group, revised to $53 "without
  definitive financing arrangements"; the board ended the review on July 1, 2022 (8-K `0001193125-22-186676`). An activist
  group (Macellum, Legion, 4010, Ancora) settled for board seats in April 2021 (8-K `0001193125-21-116440`) and ran a proxy
  contest in 2022 (DEFC14A filed 2022-03-17, `0001308179-22-000076`, not read).
- Pay (DEF 14A 2026): the FY2025 annual incentive paid "185.4% of Target" on merchandise sales and adjusted operating margin
  in a year when net sales fell 4.0%, against an operating plan that "reflected an expectation of lower sales and a reduced
  operating margin relative to Fiscal 2024"; the 2025 to 2027 share units had their financial period shortened "from three
  years to one year", with the committee then capping the payout at 127% of target; the 2023 to 2025 share units missed every
  threshold but paid 50% "via the Performance Index Modifier"; say-on-pay support was "approximately 55%" in 2025. The 2026
  annual meeting added 5,200,000 shares to the equity plan (8-K `0001193125-26-234927`).

**Bearing on Q9 (debt and exposures):** notes of $1,342M principal at August 1, 2026: 2029 $42M (7.25%), 2030 $360M (10.000%,
secured by eleven distribution and fulfilment centres), 2031 $320M (5.13% after 175 basis points of step-ups), 2033 $107M,
2037 $86M, 2045 $427M (10-Q, debt note). Finance leases and financing obligations $2,387M; operating-lease liabilities
$2,709M (10-Q balance sheet). Revolver: $1.5B asset-based facility, maturity extended to June 30, 2031, nothing drawn at
August 1, 2026 (8-K `0001193125-26-292702`; 10-Q). Corporate ratings B2 (Moody's), B+ (S&P, negative), BB- (Fitch,
negative) at January 31, 2026. FY2025 operating income $624M (adjusted $510M) against net interest $288M. No sudden-demand
features were found in the notes read beyond the rating-linked coupon step on the 2031 notes.

### COMPUTATION, NOT A CLEARANCE: the value range and the fair price (the owner's reporting figures)
*Computed beneath the Q2 stop at the owner's request (Part VII, The owner's price). No entry language; neither figure is a
verdict. Script and full output: `Test Runs/_research 2026-10-23 KSS/scripts/compute.py`, `compute_output.txt`.*

**Owner cash, recast from the filed cash-flow statements** ($M; OCF less stock pay less all capital spending; finance-lease
and financing-obligation payments deducted on the equity-only basis and added back, with interest paid after tax, on the
all-equity basis):

| FY | OCF | SBC | capex | lease/financing principal | interest paid | equity-only | all-equity |
|---|---|---|---|---|---|---|---|
| 2016 | 2,148 | 41 | 768 | 127 | 299 | 1,212 | 1,565 |
| 2017 | 1,691 | 55 | 672 | 138 | 297 | 826 | 1,189 |
| 2018 | 2,107 | 87 | 578 | 126 | 282 | 1,316 | 1,655 |
| 2019 | 1,657 | 56 | 855 | 113 | 193 | 633 | 892 |
| 2020 | 1,338 | 40 | 334 | 105 | 254 | 859 | 1,156 |
| 2021 | 2,271 | 48 | 605 | 125 | 246 | 1,493 | 1,804 |
| 2022 | 282 | 30 | 826 | 106 | 284 | -680 | -359 |
| 2023 | 1,168 | 42 | 577 | 93 | 331 | 456 | 800 |
| 2024 | 648 | 30 | 466 | 79 | 312 | 73 | 388 |
| 2025 | 1,380 | 34 | 372 | 83 | 295 | 891 | 1,197 |

Tax on the interest add-back: 24.3%, the FY2025 10-K's 21.0% federal plus 3.3% state and local (CONVENTION of this run: the
marginal rate the filer reports is used for the add-back; rationale: the all-equity basis needs interest after the company's
own tax and the filing gives that rate). Proceeds from property sales and from financing obligations are left out (small,
not recurring; leaving them out lowers the figure). No carryforward shelter worth pricing (state NOLs of $16M, note 5).
Working capital is counted, since it runs through operating cash (specific (d)). No business was bought or sold in the
window (specific (c) not engaged).

**The base and the growth.** The five-year window FY2021 to FY2025 averages **$766M all-equity** ($447M equity-only). Its
first year is aberrational on the filer's own description: FY2022's operating cash fell "primarily due to lower net income and
a decrease in accounts payable due to late arriving receipts in 2021. Additionally in 2021 we received a tax refund related to
the net loss we incurred in 2020" under the CARES Act (10-K FY2022, Liquidity). Specific (a) therefore applies: the base is
the cycle average and the growth is measured between the averages of successive cycles. Owner cash here alternates with
working capital year by year and marks no business cycle peak to peak; **CONVENTION of this run:** the window FY2021 to
FY2025, which holds the 2021 peak, the 2022 trough and the recovery, is taken as the last full cycle, and FY2016 to FY2020 as
the one before it; rationale: they are the only two complete swings in the series that do not cut a peak from its reversal.
Growth between them: all-equity $1,292M to $766M, **-9.92% a year**; equity-only $969M to $447M, -14.36% a year. Net sales
fell 2.59% a year FY2015 to FY2025 and 5.43% a year FY2021 to FY2025. Specific (b): the decline is carried as negative and
makes the bottom; the no-growth case is the top. Specific (e): the filing states no maintenance figure, so the all-spending
case is central and the depreciation variant is shown beside; **growth spending charged: $0 in year one and $0 in year ten**
(there is no growth case). Specific (f): not engaged (no growth carried). Sovereign 5.29%; zero nominal growth after year ten.
Net debt at August 1, 2026 (latest filed balance sheet; no subsequent event in that filing adds debt): long-term debt $1,325M
+ finance leases and financing obligations $92M + $2,295M + revolver $0 - cash $821M = **$2,891M**; operating leases left out
(their rent stays inside owner cash). Shares 113.376M.

| case (all-equity, central) | owner cash, year 1 basis | growth | value at 5.29% | per share | value at 10% | per share | return at $24.00 |
|---|---|---|---|---|---|---|---|
| top: no growth | 766 | 0% | 14,481 | $102.23 | 7,661 | $42.07 | 13.7% |
| bottom: decline ten years, then flat | 766 | -9.92% | 6,626 | $32.94 | 4,033 | $10.07 | 6.5% |

- **(a) VALUE RANGE (all-equity, central): $32.94 to $102.23 a share against $24.00.** Width 3.10 to 1.
- **(b) FAIR PRICE (all-equity, central): $26.07 a share** (each end case valued at ten percent, $42.07 and $10.07, averaged;
  after the company's own tax). **Equity-only beside: $27.67 a share** (equity-only range $24.44 to $74.46; ends at ten percent
  $39.39 and $15.94).
- Read as Q7 would read it, had Q7 been reached (computation only): the floor test first: the no-growth case earns about 13.7%
  at the price, so some case clears the floor; the range is wider than about three to one (3.10), which is the width at which
  "the range must be so wide that no useful conclusion can be reached" **[L2000-025]**. The stop at Q2 decides the box;
  this reading changes nothing.

**Shown beside, not central:**
- *The literal window, specific (b)'s halves rule* (the series changes sign in FY2022): all-equity first half FY2021 to FY2022
  $723M, second half FY2024 to FY2025 $793M, **+3.14% a year**; that growth case is $138.79 a share at 5.29% ($58.20 at ten
  percent); literal pair no-growth $102.23 and growth $138.79, fair $50.13. The halves are carried up by the FY2021 timing
  items above; shown because the text asks for the literal window beside.
- *Depreciation variant* (D&A in place of capex, all-equity): base $568M, -10.64% a year; range $15.50 to $69.15; fair $12.15.
  Capex has run at about half of depreciation for two years; "Depreciation charges [...] are almost always true costs."
  **[L2015-004]**.
- *Sensitivity:* the base without FY2021 (FY2022 to FY2025, $507M): no-growth $58.95, decline $13.14 a share at 5.29%; with
  the FY2025 legal settlement removed after tax ($747M base): range $31.45 to $98.97.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 2b97678b); written question by question; committed after Step 0 and
      Q1 (e49a41ea), after Q2 (02fb149e), and after the remainder (this commit).
- [x] Dispatched: the brief granted per-question pathspec commits; the lock is the dispatching session's. The run binds
      nothing until folded into the register (operator rule 10).
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; only this run's research folder
      was listed; what was seen by accident is declared under CONTAMINATION and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `Test Runs/_research 2026-10-23 KSS/scripts/check_ids.py`); every filing fact carries its document and accession.
- [x] The order was kept: Q1 IN, Q2 OUT closed the file; nothing after it is a clearance; the computation is headed so.
- [x] Owner cash after every real cost from the cash-flow statements, never a net-income proxy; stock pay deducted; all
      capex deducted; sovereign from the US Treasury; the price is an aggregator quote, flagged.
- [x] Contrary evidence written down as found (foundations, Q1, Q2's other-side paragraph); facts for later questions under
      AFTER THE STOP, with the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used, and they were superseded by the recast from the filings.
- [x] `python tools/check_framework.py` PASS before the final commit.
- Honest gaps: competitor figures are XBRL transcriptions of the rivals' 10-K filings, not read in the documents themselves;
  operating income was not tagged for several rivals, so net income and operating cash were compared instead; the FY2022
  finance-lease increase (to $2,880M) was not traced to its cause; the 2022 proxy contest filings were not read; JCPenney's
  status was not verified from a filing; the capital-spending categories are in a chart the text dump does not carry.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Three things. (1) **Specifics (a) and (b) collide on this series.** The first window year is aberrational, which sends the
base to "the average over the last full cycle" and the growth to "the averages of successive cycles" (a); the series also
changes sign in FY2022, which sends the growth to "the first and second halves of the window" (b). The two give -9.92% and
+3.14% a year, and the fair price moves from $26.07 to $50.13 on the choice. The text does not say which governs when both
apply; this run took (a), because the aberrational year is the reason the halves mislead, and showed (b) beside. (2) **"The
last full cycle, peak to peak" cannot be marked on a series that alternates with working capital every year.** Kohl's owner
cash has a local peak every second year; the run confessed its own CONVENTION (successive five-year windows as successive
cycles). A rule for a series with no visible business cycle, or a choice of the defining series (sales, or operating income,
rather than owner cash), would stop two analysts from choosing different cycles. (3) **The all-equity basis for a lessee
whose finance leases are a large part of its debt** is workable but not stated: the text names finance leases in net debt
and leaves operating leases out, but does not say that finance-lease principal and interest then leave owner cash, nor how
interest is taxed for the add-back; the run added back principal and interest after the filer's 24.3% marginal rate and said
so. A sentence in Q7 would settle both.

