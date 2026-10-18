# Company Run: LegalZoom.com, Inc. (Nasdaq: LZ), 2026-10-13
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**
*(Copied from `Test Runs/_TEMPLATE - Company Run.md` before any fetch; commit 17567db3.)*

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled by the dispatching session at the fold, after the run was committed: `PORTFOLIO.md` read for this one ticker (LZ, LegalZoom; also searched for LegalZoom); not held.*

**Dispatched run.** A dispatched analyst under `Screens/_daily/_dispatch_brief.md` as the overnight prompt departs from it
(the analyst derives the lines of evidence from Items 1, 1A and 7; see "Lines of evidence chosen" below).

**Contamination declared.** (1) To confirm my own paths did not already exist I ran a directory listing of `Test Runs/`
filtered for "LZ"; it printed one file name, `2026-07-16 Run - LZB (La-Z-Boy).md`, a different company (La-Z-Boy). Not
opened, not used. (2) The session's starting git status and recent commit subjects named other companies' runs (KIGRY,
AYI, ARCB research folders); none concerns LegalZoom; not opened, not used. (3) The memory index loaded with the session
names queue and holding states in general terms and nothing about LZ. Nothing else of the blind-listed files was seen.

**Lines of evidence chosen (the brief's stated departure), from the 10-K's Items 1, 1A and 7.** (a) Business formations,
the entrance product (Item 1A's first risk: "Our business primarily depends on business formations"), its price and LZ's
share against the U.S. Census EIN count, read across every 10-K since the IPO; (b) the subscription base: units, ARPU and
the annual small business retention rate; (c) customer acquisition through search and the shift to AI answer engines (Item
1A, marketing risk; the 2026 guidance cut); (d) competition, including free formation offers and state portals (Item 1A);
(e) stock-based compensation, which Item 7 shows at $113.7 million in 2025 against $15.4 million of net income, and the
buybacks run against it; (f) the accounts' history: the 2023 Item 4.02 restatement and the material weaknesses; (g) the
Formation Nation acquisition. Chosen because Items 1, 1A and 7 name each as what the results depend on.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $6.05 (close 2026-10-12, from `tools/run.py`'s live quote; an aggregator, flagged per operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, **171,264,812** shares as of 2026-07-31
  (10-Q for the quarter ended 2026-06-30, filed 2026-08-05, accession `0001286139-26-000031`; `python Screens/cover_shares.py LZ`
  prints the same). Check against issued less treasury: the 10-Q balance sheet shows 167,451 thousand shares "issued and
  outstanding" at 2026-06-30, with repurchased shares "purchased for immediate retirement" (no treasury stock). The cover
  count is 3.8 million higher a month later; the 10-Q's equity statement shows each quarter's "Issuance of common stock upon
  vesting of restricted stock unit awards" (1.5 to 1.9 million a quarter), and no 8-K or prospectus after the 10-Q was found
  in the EDGAR submissions list (8-Ks after 2026-08-05: none). The cover count is used; the proxy's 172,872,925 shares at
  2026-04-09 (DEF 14A, `0001193125-26-170325`) is consistent with it.
- **Market cap:** $1,036.2M (6.05 x 171.265M).
- **Sovereign for the earnings currency:** USD 30-year par yield **5.60%**, US Treasury daily par yield curve, 2026-10-09
  (`python tools/sources.py`).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-23, `0001286139-26-000012`), Items 1, 1A, 5, 7, 8 (statements
  and notes on acquisitions, tax and supplemental cash flow); 10-K FY2024 (`0001286139-25-000044`), FY2023
  (`0001286139-24-000031`), FY2022 (`0001286139-23-000036`), FY2021 (`0001286139-22-000048`): statements, key metrics and the
  competition and formation passages; the IPO prospectus 424B4 (2021-06-30, `0001193125-21-204774`) for the 2019 balance
  sheet; 10-Q Q2 2026 (`0001286139-26-000031`); proxy DEF 14A (2026-04-22, `0001193125-26-170325`), summary compensation and
  ownership; 8-K and 8-K/A Item 4.02 (2023-02-17 `0001286139-23-000005`, 2023-02-27 `0001286139-23-000019`); 8-K Formation
  Nation (2025-02-10, `0001286139-25-000014`); 8-K exhibits 99.1 for Q4 2025 (`0001286139-26-000007`) and Q2 2026
  (`0001286139-26-000029`). **One figure cross-checked against the filed statement:** cash and cash equivalents at
  2025-12-31, $203,100 thousand on the FY2025 balance sheet, equals the Liquidity section's $203.1 million and `tools/run.py`'s
  203; operating cash flow 2025, $178,197 thousand on the filed cash-flow statement, equals `tools/run.py`'s 178.2.
- `python tools/run.py LZ` arithmetic lines only (saved as `Test Runs/_research 2026-10-13 LZ/run_py.txt`): OCF 124.3 / 135.6 /
  178.2, SBC 66.0 / 71.5 / 113.7, capex 31.6 / 35.7 / 30.3 for 2023 to 2025, matching the filed statements. Two corrections
  from the filing: run.py's D&A for 2025 (36.3) is below the filed $44.1 million (its tag misses intangible amortization), and
  run.py's owner-earnings columns leave out **capitalized stock pay** ($4.1M, $6.0M, $5.3M in 2023 to 2025, supplemental cash
  flow data in each 10-K), which is stock pay that never passes through the expensed-SBC add-back. Owner cash below deducts it.
  Nothing run.py prints as a rule, an id or a verdict is used (Part VII).

**Owner cash after every real cost** (`Test Runs/_research 2026-10-13 LZ/q7_computation.py`, output in `q7_output.txt`; USD
millions; operating cash flow less expensed stock pay, less capitalized stock pay, less all capital spending; all-equity
column adds back cash interest paid and removes interest income on the cash after tax at 21%, a CONVENTION of this run,
rationale: the cash is netted in the all-equity basis, so its interest cannot also stay in the stream):

| Year | Revenue | OCF | Stock pay (exp + cap) | Capex | Owner cash, equity-only | Owner cash, all-equity | Acquisitions paid |
|---|---|---|---|---|---|---|---|
| 2019 | 408.4 | 52.7 | 5.2 | 18.3 | 29.2 | 29.2 | 0 |
| 2020 | 470.6 | 93.0 | 12.9 | 10.6 | 69.5 | 97.4 | 0.9 |
| 2021 | 575.1 | 54.2 | 113.3 | 11.7 | -70.9 | -58.6 | 61.5 |
| 2022 | 620.0 | 73.8 | 83.0 | 22.1 | -31.3 | -32.5 | 8.5 |
| 2023 | 660.7 | 124.3 | 70.1 | 31.6 | 22.6 | 15.3 | 0 |
| 2024 | 681.9 | 135.6 | 77.5 | 35.7 | 22.5 | 16.3 | 0 |
| 2025 | 756.0 | 178.2 | 119.0 | 30.3 | 28.9 | 23.0 | 48.5 |
| LTM 2026-06 | n/a | 175.2 | 103.1 | 25.6 | 46.5 | 40.8 | n/a |

Five-year average (2021 to 2025), all-equity: **-7.3**; equity-only -5.6. Never a net-income proxy (operator rule 5).

### The balance sheets, eight dates, read before the income account **[M2025-032]**
*(Step 0 reading, because the file closes before Q4. USD millions; 2019 from the 424B4, 2020 from the FY2021 10-K, 2021 to
2025 from each year's 10-K, 2026-06 from the Q2 10-Q.)*

| Date | Cash | Receivables | PP&E | Goodwill + intangibles | Total assets | Deferred revenue | Borrowings | Equity | Accumulated deficit | Shares out (M) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2019-12 | 49.2 | 10.2 | 60.1 | 12.9 | 200.0 | 106.7 | 518.4 | -557.0 (+70.9 preferred) | -644.3 | 124.4 |
| 2020-12 | 114.5 (+25.0 restricted) | 8.6 | 51.4 | 12.2 | 252.1 | 130.1 | 515.4 | -550.6 (+70.9 preferred) | -639.3 | 125.0 |
| 2021-12 | 239.3 | 10.6 | 47.0 | 75.9 | 431.0 | 147.9 | 0 | 197.6 | -748.0 | 198.1 |
| 2022-12 | 189.1 | 13.2 | 30.8 | 82.1 | 405.4 | 165.1 | 0 | 142.4 | -891.9 | 190.8 |
| 2023-12 | 225.7 | 11.7 | 48.2 | 77.1 | 447.8 | 168.4 | 0 | 168.8 | -933.1 | 188.5 |
| 2024-12 | 142.1 | 8.5 | 59.8 | 72.0 | 373.9 | 175.0 | 0 | 93.3 | -1,069.3 | 173.6 |
| 2025-12 | 203.1 | 20.6 | 58.0 | 158.9 | 511.5 | 203.9 | 0 | 171.9 | -1,134.4 | 177.6 |
| 2026-06 | 167.2 | 19.8 | 53.5 | 155.6 | 466.4 | 221.4 | 0 | 127.2 | -1,217.9 | 167.5 |

What the balance sheets say. (1) **The customers fund the business.** Deferred revenue has risen every year, 106.7 to 221.4,
and exceeds cash at every date from 2024; receivables are tiny (8.5 to 20.6) against revenue of 400 to 760, since customers
pay at order. Working capital is negative and is a source of cash as the subscription book grows. (2) **The debt is gone.**
A $515 million 2018 term loan (a leveraged recapitalization before the IPO) was repaid from the 2021 IPO proceeds
($581.8 million net plus an $85.1 million private placement, FY2022 10-K cash-flow statement); there have been no borrowings
since; a $100 million revolver to 2030 is undrawn (FY2025 10-K, Liquidity). (3) **Equity is made by issuing stock and spent
by retiring it.** Additional paid-in capital rose from 92.9 (2019) to 1,344.5 (2026-06), while the accumulated deficit grew
from -644 to -1,218 although the company reported net income in 2023, 2024 and 2025: repurchases are charged to the
deficit (FY2025 10-K: $80.5M repurchased in 2025, $165.0M in 2024, $54.9M in 2023, $95.1M in 2022; 10-Q: $89.0M in the
first half of 2026). Equity at 127 is what is left after $484.5 million of buybacks from 2022 to mid-2026 were set against
$397 million of stock pay over the same span ($376.6M expensed plus $20.5M capitalized), and shares outstanding fell from
198.1 million to 167.5 million. (4) **Goodwill doubled in 2025** (63.3 to 140.7) on Formation Nation, a $83.2
million purchase, mostly cash (FY2025 10-K, acquisition note); 2021's jump (11.4 to 59.9) was Earth Class Mail ($61.5M cash).
(5) **Cash moves with the buybacks, not the business**: down 83.7 in 2024 when $165M was repurchased, down 35.9 in the
first half of 2026 with $89M repurchased. (6) Deferred tax assets of 24 to 35 sit on the balance sheet throughout, against
federal NOLs of $27.5 million (FY2025 10-K). "what the figures are saying and what they don’t say" **[M2025-032]**: they say
a cash-generative, capital-light, debt-free service business whose owners' share is taken mainly in stock pay; they do not
say how the formation funnel will be fed, which is the question below.

---
## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether I "would" be "happy buying this stock if the market closed for five years"
**[M1997-109]**, which here turns on the business in five years, not on the fall from the $28.00 IPO price (424B4) to $6.05;
the market "just tells us prices" **[M2006-077]**. The analyst's habits govern this name more than most: the stock is far
below its IPO price and the company is buying its own stock, both of which invite a buyer to borrow the market's or the
management's conviction; the habit is to look for "what’s wrong in things" **[M2025-013]** and to read "to possibly reject
your original hypothesis" **[M1998-144]**. Who is paid to tell you: the company's releases feature Adjusted EBITDA and
"Non GAAP net income" and lead with growth; they are read last, after the statements. **Contrary evidence, written down as
found** **[M1997-127]**: (i) the FY2023 10-K says the company, "along with some of our online competitors, began to target
more price conscious customers by offering business formation transactions at little or no charge"; (ii) formations on LZ's
platform fell 17% in 2024 while U.S. formations fell 5%, rose 4% in 2025 "primarily due to formations driven by our
Formation Nation acquisition" while U.S. formations rose 9%, and fell 5% in Q2 2026 (FY2024 and FY2025 10-Ks; Q2 2026 10-Q);
(iii) subscription units fell 3% year on year to 1,892 thousand at 2026-06-30 and annual small business retention was about
57% (Q2 2026 10-Q); (iv) the August 2026 release cut the year's revenue outlook "reflecting the recent industry-wide shift
in customer discovery away from traditional search" (8-K `0001286139-26-000029`, Ex. 99.1); (v) stock pay was $113.7
million in 2025, more than seven times net income (FY2025 10-K). For the business: subscription revenue grew 13% in 2025 and
11% in Q2 2026, ARPU rose 5%, gross margin rose to 68% in the quarter, deferred revenue grows, and there is no debt.

## THE STANDING RULE
A purchase for cash, unlevered and sized so that the stock can fall by half without forcing a sale, puts the buyer at no risk
of ruin; "borrowed money has no place in the investor's tool kit" **[L2014-005]**, and nothing here asks the buyer to "risk
what we have and need for what we don’t have and don’t need" **[M2012-081]**. The rule is met by the buyer's conduct and is
not engaged further by this name.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" and "how the industry will develop and where the company will stand within the industry" **[M2012-065]**;
"a reasonable probability of being able to asses where the business will be in 10 years" **[M2000-037]**. The product is not
the difficulty: forming an LLC, acting as registered agent, filing annual reports, a legal plan staffed by network
attorneys, virtual mail. Every one is plain, and every one is required by state law of the customers (FY2025 10-K, Item 1).
The difficulty is the economics of LZ's position in ten years.

**The key variables, and how predictable they are** **[M1998-044]**:
1. *U.S. business formations*, the funnel's source. Measurable (the filer ties its count to Census EIN applications) but
   swinging: the filer's formations ran 292, 378, 447 thousand in 2019 to 2021 (FY2021 10-K; the FY2022 10-K restates 2021
   as 483 thousand on a definition that adds DBAs), then fell 2% in 2022, rose 23%
   in 2023 on free LLC formations, fell 17% in 2024, rose 4% in 2025 on an acquisition, fell 5% in Q2 2026. Volatile but
   bounded; not by itself the obstacle.
2. *LZ's share of formations, and the price it can charge for the first product.* Not predictable on the filings. The
   formation was the company's paid entrance product until 2023, when it and "some of our online competitors" moved to
   offering it "at little or no charge" (FY2023 10-K, Item 1A); formation average order value fell 25% that year (FY2023 10-K,
   Item 7); in 2025 the company reversed course, "reserving the LegalZoom brand for more premium offerings" and using the
   acquired Inc Authority brand "as a lower priced alternative" (FY2025 10-K, Item 1). Share was lost against the Census count
   in 2024, 2025 (organically) and Q2 2026. Item 1A adds that "some U.S. state and federal agencies have increased their
   offerings to our target customers [...] including through free and easy-to-use business formation services."
3. *How the customer finds the company.* The largest customer-acquisition spend is search engine marketing (FY2025 10-K,
   Item 1, Sales and marketing; customer acquisition marketing spend $175.6 million in 2025). The filer states that the
   change has already begun and has already cost it: "an increased prominence of AI on the search engine results page, have
   adversely affected, and may continue to adversely affect, the placement of our search result page ranking and the resulting
   traffic to our websites, as well as our customer acquisition costs" and "shifting preferences for AI chat platforms, has
   diminished and may continue to diminish the effectiveness of our current marketing practices" (FY2025 10-K, Item 1A). The
   August 2026 release cut the 2026 revenue outlook for "the recent industry-wide shift in customer discovery away from
   traditional search", and the chief executive said: "While demand for what we do is intact, discovery is moving [...] we
   haven't assumed how quickly this scales" (8-K `0001286139-26-000029`, Ex. 99.1).
4. *Whether the service itself is replaced.* The Q2 2026 10-Q, Item 1A: "As generative AI tools become more prevalent,
   potential customers may view these tools as replacements to some of the services we provide." The FY2025 10-K: "New market
   entrants that provide technologies that improve the delivery of legal solutions, such as AI and machine learning, have
   increased and could continue to increase the level of competition in the market" and "The online legal solutions market
   is evolving rapidly and is becoming increasingly competitive", a sentence printed in every 10-K from FY2021 to FY2025
   (in the FY2025 text it is broken across a page).
5. *Subscription retention.* About 58% (2025) and 57% (Q2 2026): roughly four subscriptions in ten lapse each year and must
   be replaced through the funnel of variables 2 and 3. The filer itself does "not view it as a predictor of future revenue."

**The tests applied.** Test 3, do the past statements tell me the future ones **[M2008-033]**: no. Owner cash ran 29, 97,
-59, -32, 15, 16, 23 from 2019 to 2025 (Step 0); the strategy changed in each of 2023 (free formations, lower-priced
products), 2024 (new chief executive in July, restructuring), 2025 (acquisition, two-brand pricing, DIFM concierge), and 2026
(guidance cut, a 13% workforce reduction "towards becoming a more agile, AI-native company", Q2 2026 10-Q, Note 13); and the
filer warns that "we have experienced and we expect to continue to experience increased volatility across our key business
metrics" (FY2025 10-K, Item 7). Test 5, would the insiders write it down **[M2000-105]**: the insiders have not, in the one
place they were asked; the chief executive's own statement is that the company has not "assumed how quickly" the new channel
scales, and the year's outlook was cut six months into the year. Test 6, can I name the winner, not just the industry
**[M2012-067]**: no; the field's rivals named in the FY2021 10-K (BizFilings, LegalShield, MyCorporation, RocketLawyer) file
no periodic reports with the SEC, the FY2025 10-K names none, and the one public player has lost formation share to them
while matching their free price. Test 7, is the forecast about customers or about technology **[M2017-019]**, **[M2023-030]**:
the demand (the state's requirements) is a customer fact and is stable; the share and the cost of reaching the customer are
technology facts, which channel AI search and AI drafting will route the customer through, and that is where the forecast
fails. Test 8, how far off could I be **[M2011-084]**: at ten years, from a business that keeps its formation and subscription
franchise behind a recognised brand to one whose entrance product is free everywhere and whose customers are reached through
answer engines it does not control; the range of outcomes is wider than the filings can narrow. Test 9, do I doubt it is
inside **[M2002-092]**: yes: "if you have doubts about something being into your circle of competence, it isn’t."

**Routing.** The rows put this case at Q1: "if something comes in where there’s a technological component that’s of
significance, or where we think the future technology could hurt the business as it presently exists [...] it won’t make it
through the filter" **[M1998-008]**; "whenever we look at a business and we see lots of change coming, 9 times out of 10,
we’re going to pass on that" **[M1999-063]**; "a business that must deal with fast-moving technology is not going to lend
itself to reliable evaluations of its long-term economics" **[L1993-023]**. The framework's routing sentence sends "a
business whose ten-year economics cannot be foreseen because its industry changes fast" to TOO HARD at Q1, and the filer's
own words supply the change ("evolving rapidly", "industry-wide shift in customer discovery", AI tools as "replacements").
"If something is not very predictable, forget it." **[M1998-044]**. It is not a bank, not a holding company, and reports one
segment (Q2 2026 10-Q, Note 12), so no other routing applies.

**Which cause.** NATURE, not WORK. The deciding question, how small-business owners will find and buy formation and
compliance services over the next ten years once answer engines and AI drafting tools stand between them and the providers,
is "important" but not "knowable" **[M2006-076]**: no filing not yet read answers it, the company's own management declined to
forecast it, and the rivals file nothing. It is a forecast "the nature of the industry" puts out of reach, the second cause of
**[L1993-023]**, which "We couldn't solve [...] even if we were to spend years intensely studying those industries." The
quick decision stands on the documents read: "we’re not going to learn enough in the followings five months to make up for
the fact that we went in deficient in the first place" **[M2008-086]**.

**What this is not.** It is not a finding that the business is poor or the price high: "It doesn’t mean it isn’t a good buy.
It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it."
**[M2000-038]**. It is the "too hard" box **[M2006-013]**, and by section I a lower price does not reopen it.

- **VERDICT: TOO HARD (NATURE)**, **[M2012-065]**, **[M2000-105]**, **[M2002-092]**, **[L1993-023]**, **[M1998-008]**; the
  filing facts are the free-formation passage (FY2023 10-K, `0001286139-24-000031`), the AI-search passages (FY2025 10-K,
  `0001286139-26-000012`; Q2 2026 10-Q, `0001286139-26-000031`) and the guidance cut (`0001286139-26-000029`).

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (the file closed at Q1). Facts found are under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets were read in Step 0.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The figures the operator asked for are under COMPUTATION, NOT A CLEARANCE, below.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)** at **Q1**: where LegalZoom's earning power and competitive position will stand in ten years turns on
how small businesses will find and buy formation and compliance services once AI answer engines and AI drafting tools sit
between them and the providers, a forecast the filer's own management declined to make in August 2026 and that no filing
answers **[M2012-065]**, **[M2000-105]**, **[L1993-023]**. Integrity facts recorded, not judged. COMPUTATION below (not a
clearance): central value $1.55 a share (no-growth case alone; literal window $0.21; cases beside up to $7.82) against
$6.05; no case built under Q7's construction earns the floor at the price. No research pass: the cause is NATURE, and by
Part VII no case of the range earns the floor at the price.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*(Written down as found **[M1997-127]**; no verdict; the box is unchanged, operator rule 2.)*

**Bearing on Q2 (the castle).**
- Free formation: "we, along with some of our online competitors, began to target more price conscious customers by
  offering business formation transactions at little or no charge while cross-selling compliance and other business
  services" (FY2023 10-K, Item 1A, `0001286139-24-000031`); formation average order value fell 25% in 2023 on "the nationwide
  rollout of free LLC formations" (same 10-K, Item 7).
- Share against the Census EIN count: LZ formations +23% vs U.S. +8% (2023, on free LLCs); -17% vs -5% (2024); +4% vs +9%
  (2025, "primarily due to formations driven by our Formation Nation acquisition"); -5% in Q2 2026 "primarily due to the
  impact of changing customer acquisition dynamics" (FY2023, FY2024, FY2025 10-Ks; Q2 2026 10-Q).
- Subscription units 921, 1,085, 1,329 thousand (2019 to 2021, FY2021 10-K), 1,441 (2022), 1,545 (2023), 1,766 (2024),
  1,939 (2025), then 1,892 at 2026-06-30, down 3% year on year with "a decrease in registered agent subscriptions"; ARPU up 5%
  "benefiting from pricing initiatives on our registered agent subscriptions" (Q2 2026 10-Q). Price rose on the product whose
  units fell.
- Annual small business retention about 58% (2025-12) and 57% (2026-06).
- Two-brand response: Inc Authority "as a lower priced alternative to service customers seeking DIY solutions, reserving the
  LegalZoom brand for more premium offerings" (FY2025 10-K, Item 1).
- State competition: agencies offering "free and easy-to-use business formation services" (FY2025 10-K, Item 1A).
- Search: "We bid for paid listings against our competitors and third parties that may outbid us for preferred placement"
  (FY2025 10-K, Item 1A); customer acquisition marketing spend $157.6M (2024), $175.6M (2025).
- Brand facts the filer gives: "over 5.0 million businesses" formed since inception; "a meaningful percentage of unpaid
  website traffic" (FY2025 10-K, Item 1). The release calls the company "America’s #1 online legal services company"
  (Ex. 99.1, Q2 2026), a claim with no figure behind it in the filings read.
- **The competitor row.** The FY2025 10-K names no rival. The FY2021 10-K (`0001286139-22-000048`, Item 1A) names
  BizFilings, LegalShield, MyCorporation and RocketLawyer. **None files periodic reports with the SEC**: Wolters Kluwer
  (BizFilings' parent, CIK 861967) files only SUPPL, ARS and F-6 forms; Rocket Lawyer (CIK 1452998) only Form D, last in
  2013; Pre-Paid Legal Services (LegalShield's former public parent, CIK 822792) nothing since 2010; no EDGAR entity was found
  for MyCorporation or LegalShield. **No competitor comparison from rivals' own filings was possible over any span.**
- The field's returns, from the filer only: owner cash after all stock pay as a share of sales was 7.1% (2019) and 20.7%
  (2020) before the IPO, -10.2% and -5.2% (2021, 2022), and 2.3%, 2.4%, 3.0% (2023 to 2025); stock pay ran $5.2M and $12.9M
  a year before the IPO and $66M to $114M a year after it (Step 0 table).

**Bearing on Q3 (capital).** Capital-light: PP&E $30.8M to $60.1M across the span; negative working capital funded by
deferred revenue ($221.4M at 2026-06); capex $10.6M to $35.7M a year, mostly capitalized internal-use software. Acquisitions:
Earth Class Mail, $61.5M cash (2021); Formation Nation, $83.2M total consideration, cash plus 2,205,445 restricted shares
(FY2025 10-K, acquisition note; 8-K `0001286139-25-000014`); Formation Nation contributed about $33.2M of transaction and
$18.2M of subscription revenue in 2025 (FY2025 10-K, Item 7). Revenue growth excluding it: 3.3% a year, 2023 to 2025.

**Bearing on Q4 (the accounts).** Item 4.02 non-reliance on the 2022 first, second and third quarter 10-Qs, an error in the
income tax provision (Section 162(m) officer identification), with material weaknesses in the control environment, the
financial close and the tax provision, and disclosure controls not effective at 2021-12-31 and each 2022 quarter (8-K/A
`0001286139-23-000019`; FY2022 10-K Item 9A). Management concluded internal control effective at 2023-12-31, 2024-12-31 and
2025-12-31, with PwC's attestation (Item 9A of each 10-K). The company features Adjusted EBITDA (23% margin, 2025) and "Non
GAAP net income" in its releases and gives quarterly and annual revenue and Adjusted EBITDA guidance (Ex. 99.1, Q4 2025 and
Q2 2026); the 2026 revenue outlook was cut from $805M to $825M to $795M to $805M in August. The FY2025 10-K's own list of
Adjusted EBITDA's limits says it "excludes stock-based compensation expense, which has been, and will continue to be, a
significant recurring expense for our business". Effective tax rate 52% (2025) and 61% (first half 2026), "primarily due to
the recognition of significant non-deductible stock-based compensation".

**Bearing on Q5 (who runs it). Integrity facts, recorded, not judged; any later run that reaches Q5 must answer them**
**[M2013-088]**. (i) The 2023 restatement and the 2021 to 2022 material weaknesses, above. (ii) Guidance given each quarter
and the year's outlook cut in August 2026; Adjusted EBITDA and non-GAAP net income featured in the releases. (iii) The chief
executive since July 2024, Jeffrey Stibel, is also Chair of the Board (Chair since October 2018, director since October 2014;
DEF 14A); on 2024-07-08 "the Board determined to transition from Dan Wernikoff", the predecessor (8-K `0001193125-24-176824`).
(iv) Pay: Mr. Stibel's 2024 total was $61,184,704, of which $60,700,819 stock awards (sign-on and 2024 PSUs); 2025 total
$1,334,775 (DEF 14A summary compensation table). In the first half of 2026 the company granted 10.7 million RSUs ($70.9M
grant-date value) and 5.3 million PSUs to the senior leadership team, 1.7 million of them to one member in the second quarter;
the PSUs pay 0% to 300% (revenue growth component) and 0% to 400% (relative TSR component) of target (Q2 2026 10-Q, Note 8).
Awards excluded from diluted shares as anti-dilutive: 38.4 million at 2026-06-30, about 22% of shares outstanding (Note 10).
(v) Owners: Francisco Partners 16.6%, BlackRock 10.1%, TCV 9.5%, Mr. Stibel 4.5% (DEF 14A, as of 2026-04-09); a director
nomination agreement with Francisco Partners entities dates from the IPO. (vi) Item 1A records negative reviews "including
dissatisfaction with our customer support, our billing policies and the way our subscriptions operate" (FY2025 10-K).

**Bearing on Q6 (the money and the owners).** Repurchases $95.1M (2022), $54.9M (2023), $165.0M (2024), $80.5M (2025),
$89.0M (first half 2026), plus $70.5M of shares surrendered for tax withholding 2023 to 2025; the program names no price:
repurchases "in such amounts as management deems appropriate" (FY2025 10-K, Item 5). Prices paid: $9.83 average in Q4 2025
(Item 5); $7.05 average in the first half of 2026 and $6.24 in Q2 2026 (Q2 2026 10-Q, repurchase note). Against the
COMPUTATION below (central value $1.55, literal window $0.21, the highest case beside $7.82), every average price paid sits
above the bottom of the range; recorded for Q6's buyback test, not weighed. Shares outstanding 198.1M (2021-12) to 167.5M
(2026-06), with 177.6M at 2025-12 above 173.6M at 2024-12 despite $80.5M repurchased in 2025. No dividends. Formation
Nation was paid mostly in cash (an acquisition, not a merger, in the framework's usage).

**Bearing on Q9 (could it ruin us).** No borrowings; the $100M revolver to 2030 is undrawn, with a 4.50x net first lien
leverage covenant tested only when drawings exceed 35% of commitments; operating leases $15.1M at 2026-06; vendor commitments
$41.2M remaining at 2025-12 (FY2025 10-K). The Arizona ABS structure "is generally untested in U.S. courts" (Item 1), an
unauthorized-practice-of-law exposure.

**Bearing on Q12.** The billing and subscription complaints in Item 1A, above; nothing found among the businesses the rows
name.

## COMPUTATION, NOT A CLEARANCE
*(Q7 is not reached; these are the operator's reporting figures, built by Q7's construction. Script and output:
`Test Runs/_research 2026-10-13 LZ/q7_computation.py`, `Test Runs/_research 2026-10-13 LZ/q7_output.txt`.)*

**Inputs.** Price $6.05; 171.265M shares; market value $1,036.2M. Net debt at 2026-06-30: borrowings 0, finance leases
nil, cash $167.2M, so net cash $167.2M (operating leases left out, as the convention says); the 10-Q's stated subsequent event
is a restructuring of about $6.0M in cash costs, not debt, so nothing is added. Enterprise value $868.9M. Sovereign 5.60%.
Tax: owner cash is after the company's own tax as paid; the federal NOL of $27.5M (expiring from 2036) is small against the
stream and is not priced separately.

**The base.** (a) The first window year, 2021, is aberrational on the filer's own description: "Stock-based compensation
expense increased significantly for the year ended December 31, 2021 due to the modification of certain equity awards in
connection with our IPO" (FY2021 10-K, Item 7; stock pay $112.6M against $12.9M in 2020), and the year carried $12.3M of
interest on the term loan the IPO repaid **[L2005-003]**. Against this, the same 10-K warned that "Over the next three years,
we will incur significant stock-based compensation expense as a result of certain modifications to equity awards that
occurred in connection with our IPO", so 2022 to 2024 also carry IPO-related stock pay, and stock pay in 2025 ($113.7M,
from PSUs granted in 2024) was as high as in 2021 with no IPO behind it. Whether 2021 is aberrational is therefore arguable
(its operating cash flow, $54.2M, was also depressed by a $76.2M jump in customer acquisition spend and by the loan interest);
the central figure takes it as aberrational and the literal window stands beside it; neither earns the floor, so the choice
decides nothing. The business has no
cycle, so "the average over the last full cycle" cannot be formed; **CONVENTION of this run**: the base is the average of the
window years after the aberrational one, 2022 to 2025, with the literal 2021 to 2025 window beside; rationale: specific (a)
removes an aberrational end year and gives no rule for a non-cyclical aberration. (b) The series changes sign (negative 2022,
positive 2023 to 2025) and the halves' comparison is meaningless across the change, so **the range is the no-growth case
alone**, said so. (c) Net purchases over the window ($57.0M, 2022 to 2025) exceed half of owner cash before purchases ($22.0M
summed, half $11.0M), so the company is a **serial acquirer** under the convention and the central figure is the **organic
pair** (purchases left out). (d) Working capital is in operating cash as filed (deferred revenue a source). (e) No maintenance
guess is separable in the filing (capex is mostly software development), so all capex is charged. (f) The cap does not bind
on the no-growth case.

| Case | Base owner cash ($M/yr) | Growth, ten years | Value at 5.60% a share | At 10% a share |
|---|---|---|---|---|
| **Central: 2022-2025 window, organic pair, no-growth (all-equity)** | 5.51 | 0% | **$1.55** | $1.30 |
| Central, equity-only (owner cash after interest, against market value) | 10.70 | 0% | $1.12 | $0.62 |
| Literal window 2021-2025, all-equity (shown beside) | -7.30 | 0% | $0.21 | $0.55 |
| Literal window, equity-only | -5.61 | 0% | -$0.59 | -$0.33 |
| Beside: 2023-2025, organic pair, no-growth end | 18.17 | 0% | $2.87 | $2.04 |
| Beside: 2023-2025, organic pair, organic-growth end | 18.17 | 3.27% | $3.43 | $2.30 |
| Beside: 2023-2025, default pair (purchases deducted, total growth) | 2.02 | 22.56% | $2.20 | $1.55 |
| Beside: LTM to 2026-06, no growth | 40.75 | 0% | $5.23 | $3.36 |
| Beside: LTM, organic growth | 40.75 | 3.27% | $6.48 | $3.95 |
| Beside: LTM, the company's 2026 revenue outlook growth (6%, a projection, flagged) | 40.75 | 6.00% | $7.82 | $4.57 |

**The floor, tested first** (the CONVENTION of about ten percent; "we don’t want to buy equities where our real expectancy is
below 10 percent" **[M2003-149]**). No case built by the construction (central, literal, or the 2023-2025 pairs) earns ten
percent at $6.05: at ten percent each is worth $0.55 to $2.30 a share. The most favourable base the filings support, the
latest twelve months (the highest owner cash in the record since the IPO, and not the construction's base), earns 4.7% on
the enterprise value with no growth, and needs owner cash to grow 10.9% a year for ten years to earn ten percent at the
price; the organic revenue growth shown is 3.3%. **Had Q7 been reached it would close OUT on the floor**, whatever the width.
Width, for the record: the central range is a single point by (b); across every case shown the values run from $0.21 to
$7.82 (the negative equity-only literal case aside).

**The two reporting figures (a reporting convention, not a verdict, no entry language; operator rule 3):**
- **(a) VALUE RANGE as Q7 builds it:** **$1.55 a share**, a point (the no-growth case alone, by specific (b)), central,
  all-equity basis, 2022-2025 window by specific (a) as this run applies it; the literal 2021-2025 window gives **$0.21**.
  Against $6.05.
- **(b) FAIR PRICE** (each end case valued at ten percent, averaged; owner cash after the company's own tax, no conversion):
  **$1.30 a share on the all-equity basis (the central figure)**; **$0.62 on the equity-only basis** beside it. Literal window:
  $0.55 all-equity, -$0.33 equity-only. Against $6.05.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit 17567db3); written question by question; committed after each
      (write-early). The file closed at Q1 (commit caaced97); the after-stop facts and the computation were committed after it.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (not written or
      touched here); the fold is the dispatcher's. A run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched, with one exception declared under
      contamination: a filtered listing of `Test Runs/` for "LZ" that printed one La-Z-Boy file name. Not opened, not used.
- [x] Every v5 id resolves and every quoted fragment beside an id is in that row (`Test Runs/_research 2026-10-13 LZ/check_ids.py`);
      every filing fact has its accession; every number carries a filing or a CONVENTION label.
- [x] The order was kept; Q1 closed the file; nothing after it is a clearance; the figures are headed COMPUTATION, NOT A
      CLEARANCE.
- [x] Owner cash after every real cost, expensed and capitalized stock pay included; never a net-income proxy (operator rule
      5); the sovereign from the US Treasury; the price is an aggregator quote and flagged.
- [x] Contrary evidence written down as found (foundations); the facts for later questions are under AFTER THE STOP, with the
      integrity flag in the box line.
- [x] Not a point-in-time run; no row dated after an anchor arises.
- [x] Only the arithmetic lines of `tools/run.py` were used, and two were corrected from the filing (D&A 2025; capitalized
      stock pay missing).
- [x] `python tools/check_framework.py` PASS before the final commit.

**Honest notes.** (1) The deciding judgment is mine, read from the filer's words: another analyst could hold that the
paperwork demand is stable enough to pass Q1 and close the file at Q2 instead, on the free-formation and share-loss facts; I
judged that the obstacle is foreseeing the position, which is Q1's own definition, and that I doubt it, which **[M2002-092]**
settles. Either route closes the file. (2) The AI-search shift is recent (the guidance cut is two months old); I have taken
the filer's statements as facts about the present and declined to forecast their size, which is the point. (3) The
2022-2025 base is a CONVENTION of this run; the literal window is lower, so the convention raised the figure, not lowered it.
(4) The removal of interest income at 21% is a CONVENTION of this run; it lowers the all-equity base by $1.2M to $7.4M a
year. (5) I did not read the proxy's full compensation discussion or the FY2023 and FY2024 MD&A in full; they bear on
questions not reached.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Specific (a) assumes a cyclical business.** It replaces an aberrational end year with "the average over the last full
cycle", which does not exist for a business whose aberration is an IPO year (stock pay and term-loan interest that will not
recur in that form). I dropped the year and showed the literal window beside, as a confessed CONVENTION of this run; the text
could say what to do with a non-cyclical aberration. (2) **The serial-acquirer test misfires on a small or negative base.**
"Net purchases over the window exceed half of owner cash before purchases" is met trivially when owner cash is near zero or
negative, as on the literal window here (owner cash summed to -$36.5M), so two modest acquisitions make the company a
"serial acquirer"; the test could carry a floor or be set against revenue. (3) **The all-equity basis and interest income.**
The convention nets cash against debt but does not say to remove the interest that cash earns from owner cash; leaving it
in counts the cash twice. I removed it after tax as a CONVENTION of this run. (4) **Capitalized stock pay.** Neither Q4 nor
`tools/run.py` names capitalized stock-based compensation (here $4M to $6M a year), which escapes the expensed-SBC
deduction; Q4's list of real costs could name it. (5) **Q1's routing for a business whose demand is stable but whose channel
is changing.** The routing sentence speaks of an industry that changes fast; here the legal demand is stable and what
changes is how customers are reached and whether software replaces the service. I read that as the industry changing, on
the filer's own words; the text does not say whether a change of channel counts. (6) **No rival files.** The brief asks for
the rivals the 10-K names that file with the SEC; the FY2025 10-K names none and the FY2021 10-K's four file nothing. Neither
the framework nor the brief says what Q2's "field's returns over the last full cycle" rests on when no rival files; it did
not arise here, as the file closed at Q1, but a run reaching Q2 would have only the filer's own record.
