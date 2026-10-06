# Company Run — Cisco Systems, Inc. (NASDAQ: CSCO) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. Run from the
template `Test Runs/_TEMPLATE - Company Run.md`, copied to this dated file before any fetch. Every judgment cites a v5
ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run and later
questions are marked NOT REACHED. Research folder: `Test Runs/_research 2026-10-06 CSCO/` (`run_py_output.txt`,
`cover_shares_output.txt`, `sources_output.txt`, the fetch script `fetch.py`, the XBRL history `history.py` and
`history_xbrl.csv`, the sums `arithmetic.py` and `arithmetic_output.txt`; raw filings and text dumps under `cache/`,
gitignored).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, the holding
reviews, the session-state files, the queue register, the prepped reading list and `tools/alerts.json` were not opened.

**CONTAMINATION, declared.** (1) A directory listing of `Test Runs/` (made to check for name collisions) showed a file
named `2026-09-27 Run - CSCO Cisco Systems.md`. Its name says an earlier run of this ticker exists; it was not opened,
and its verdict is unknown to me. (2) The same listing showed the box lines of the 2026-10-05 runs, which I read for form
only; one of them, EXTR (Extreme Networks, a networking vendor), closed TOO HARD (NATURE) at Q1. I record it because it
is the nearest name in the listing and a reader may judge whether it leaned on my Q1; no figure or argument from it was
used. (3) My training memory of Cisco (its history as the leading network-equipment vendor, the 2000-2002 collapse of
its revenue and share price, the Splunk purchase) is a prior. Every fact below that bears on a verdict is taken from the
filings, and where I relied on memory I say so.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $112.82 (2026-10-05 close, live quote via `tools/run.py`; aggregator, flagged per operator rule 5, used for
  the quote only).
- **Shares:** one class of common stock. 10-K for FY2026 (period ended 2026-07-25), filed 2026-09-02, accession
  `0000858877-26-000132`, cover: **3,942,586,873** shares of common stock outstanding (`python Screens/cover_shares.py
  CSCO`, which agrees with the cover's own count). The balance sheet at 2026-07-25 gives 3,946M issued and outstanding.
- **Market cap:** $112.82 × 3,942.59M = **$444.8B**.
- **Sovereign for the earnings currency (USD):** **5.66%**, the 30-year par yield, US Treasury daily par yield curve,
  dated 2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2026, `0000858877-26-000132` (Item 1 Business in full; Item 1A risk factors
  on competition, technology change and the service-provider and cloud market; MD&A overview and critical estimates; the
  balance sheet, statement of operations and cash-flow statement; Note 18 revenue by product category); 10-Q for the
  quarter ended 2026-04-25, filed 2026-05-19, `0000858877-26-000078` (cover and cash-flow statement only, since the
  10-K supersedes it); DEF 14A filed 2025-10-28, `0000858877-25-000150` (fetched; its subjects, Q5 and Q6, were not
  reached); 8-K of 2026-08-12, `0000858877-26-000106`, EX-99.1 (the Q4 FY2026 earnings release, read for its headline
  and its non-GAAP reconciliation); 8-K of 2026-05-13, `0000858877-26-000075` (fetched; Items 2.02, 2.05).
- **One figure cross-checked against the filed statement:** operating cash flow FY2026, $14,177M in `tools/run.py`
  (XBRL) and $14,177M on the filed Consolidated Statement of Cash Flows (10-K FY2026, page 59). Agrees. The 10-Q's
  nine-month figure is $8,791M, so the fourth quarter carried $5,386M.
- **`tools/run.py CSCO`, arithmetic lines only** (Part VII; its v4 wording and floor ignored). **Tool defect:** its "D&A"
  column (700, 1,028, 916 for FY2024 to FY2026) is the income statement's *amortization of purchased intangible assets*
  line, not the cash-flow statement's "Depreciation, amortization, and other" ($2,507M, $2,811M, $2,540M), so its "OE
  D&A" basis overstates owner cash by about $1.6B to $1.8B a year. Its ten-year balance-sheet table also prints two
  FY2018 rows (2018-07-28 and 2018-07-29), the second nearly empty. Neither enters below; owner cash is computed on the
  capital-spending basis only.

**Owner cash after every real cost** (operating cash flow, which adds stock pay back, less stock pay, less all capital
spending; USD millions; FY2024 to FY2026 from the filed 10-K FY2026 statements, FY2022 and FY2023 from the first-filed
XBRL facts of the 10-Ks `0000858877-22-000013` and `0000858877-23-000023`; `arithmetic_output.txt`):

| fiscal year | OCF | stock pay | capex | owner cash |
|---|---|---|---|---|
| 2022 | 13,226 | 1,886 | 477 | **10,863** |
| 2023 | 19,886 | 2,353 | 849 | **16,684** |
| 2024 | 10,880 | 3,074 | 670 | **7,136** |
| 2025 | 14,193 | 3,641 | 905 | **9,647** |
| 2026 | 14,177 | 3,830 | 1,410 | **8,937** |
| five-year mean | | | | **10,653** |

Five-year mean per share $2.70; owner-cash yield at the price **2.40%** against a sovereign of 5.66%. The FY2023 and
FY2024 figures swing on taxes: the FY2024 cash-flow statement carries "Income taxes, net" of −$4,539M (10-K FY2026,
page 59). The cash paid to withhold tax on vesting stock ($1,873M in FY2026, a financing line) is the cash side of the
stock pay already deducted and is not deducted again. FY2026 working capital absorbed $2,541M of inventory and $1,835M of
financing receivables.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is what Cisco will earn over a long holding, not the quote **[M1997-109]**, and the
quote, at 2.4% owner-cash yield against a 5.66% bond, tells me nothing about value by itself **[M2006-077]**. The analyst's
habits govern Q1 here: "What do I not know that I need to know?" **[M1999-129]**, and look for "what you’re missing"
**[M2025-013]**. Who is paid to tell you bears on the source of the story: the 10-K and the release are the seller's own
account of an AI "generational shift", and the release features non-GAAP earnings per share of $4.33 against GAAP $3.33,
the difference led by stock pay of $0.95 a share (EX-99.1, `0000858877-26-000106`); that is a Q4 matter and is recorded
here only as found. **Contrary evidence, written down as found** **[M1997-127]**: (a) Cisco's aggregate record is far
steadier than its industry's reputation: gross margin 58.9% to 64.9% and operating margin 17.8% to 27.6% in every fiscal
year from FY2008 to FY2026, revenue from $39.5B to $63.3B (2.65% a year), all from the filed XBRL facts
(`arithmetic_output.txt`); a reader could take that as a business whose past statements do tell its future ones. (b) The
speakers once bought a large position in an enterprise-technology vendor with a long record on exactly that reasoning,
"The chances of being way wrong in IBM are probably less, at least for us" **[M2012-073]**, and with less conviction
about its moat than about Coca-Cola's **[M2013-074]**. Both are carried into Q1 and answered there.

## THE STANDING RULE
Nothing in this name puts the buyer at risk of ruin if bought for cash and sized within the buyer's means; the rule binds
how a purchase is financed and held, not the target **[M2012-081]**, **[L2023-005]**. No purchase is made by this run.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**What the business is, from the 10-K FY2026 (`0000858877-26-000132`).** Product revenue $48.3B and services $15.0B
(76% and 24% of $63.3B). Product by category (Note 18): Networking $34.7B, Security $8.2B, Collaboration $4.3B,
Observability $1.1B. Networking grew 22% in FY2026, "particularly within our AI Infrastructure and Campus Networking
solutions"; AI infrastructure sold to hyperscalers was "approximately 6% of total revenue in fiscal 2026 compared with
less than 2% in fiscal 2025" (MD&A). The earnings release (EX-99.1, `0000858877-26-000106`) gives $9.3B of hyperscaler AI
orders in FY2026, about $4B of revenue from them, and $7.5B expected in FY2027. Manufacturing is outsourced; the moat
claims are silicon (Silicon One), software subscriptions on the installed base, services and the sales channel. Research
and development took 15.1% of revenue in FY2026 and has run 11.9% to 16.4% in every year tagged since FY2011.

**The test, as the draft states it** **[M1995-051]**, **[M2012-065]**: a "reasonable fix on about what the earning power
and competitive position will look like in five or 10 years", knowing "how the industry will develop and where the company
will stand within the industry". The product is understood; what is asked is the economics ten years out **[M2000-104]**.

**The key variables** **[M1998-044]**, and whether each is foreseeable:
1. *Cisco's share of the network inside the AI data center.* The 10-K: customers "select among competing network
   architectures before they select individual products. To the extent customers adopt architectures that are not
   designed to include the type of products and solutions we provide, our opportunities may be limited even if our
   products are superior. The competitors in these markets include semiconductor companies, systems providers, cloud
   providers and other technology companies" (Item 1A). The competitor list now names Nvidia, Broadcom, Amazon Web
   Services and Microsoft beside Arista, Huawei, HPE and Nokia (Item 1). A segment that went from under 2% to 6% of
   revenue in one year, with orders more than double the year's revenue, is a variable moving faster than any ten-year
   forecast can hold. Not foreseeable.
2. *Whether hyperscalers keep buying rather than building.* The 10-K names the customers' "decisions regarding whether
   to purchase solutions from us or other vendors or develop certain technologies internally" and "bespoke product
   designs and features that would be difficult to sell to alternate customers" (Item 1A, the service-provider and cloud
   risk factor). Not foreseeable from outside, and the filer does not claim to foresee it.
3. *Enterprise campus networking against white-box and cloud-managed rivals.* The 10-K: "as products related to network
   programmability, such as software-defined networking (SDN) products, have become more prevalent, we have faced
   increased competition from companies that develop networking products based on commoditized hardware, referred to as
   “white box” hardware", and "price-focused competition from competitors in Asia, especially from China" (Item 1, Item
   1A). This is the part closest to foreseeable: an installed base served through a channel, with $29.8B of deferred
   revenue at year end (balance sheet). It is the one variable I could argue to a range.
4. *Security and observability against specialist platforms* (Palo Alto Networks, Fortinet, CrowdStrike, Zscaler,
   Datadog, Dynatrace, all named by the filer). Security product revenue grew 2% in FY2026 after the Splunk addition;
   which security platform wins the decade is a forecast about technology, not about customer habit.

**The filer's own view of whether the ten-year economics can be written down** (test 5, **[M2000-105]**): "The markets
for our products and services are characterized by rapidly changing technology, evolving industry standards, new product
and service introductions, and evolving methods of building and operating networks"; "if our model of the evolution of
networking, security, or observability does not emerge as we believe it will, or these industries do not evolve as we
believe they will, or if our strategy for addressing this evolution is not successful, many of our strategic initiatives
and investments may be of no or limited value"; and "Barriers to entry are relatively low, and new ventures to create
products that do or could compete with our products are regularly formed" (Item 1A; Item 1, Competition). The insider
most able to write the forecast says, in its own annual report, that its model of the industry's evolution may not
emerge. That is the speakers' test answered by the industry itself: "They would say, “That’s too hard.”" **[M2000-105]**.

**The other tests.**
- *Is the forecast about customers or about technology?* (test 7, **[M2017-019]**, **[M2023-030]**). Here it is about
  technology and network architecture: what the AI data center is built from, and whether a switch is bought from a
  vendor or designed by the customer. The rows that admit a technology label distinguish a consumer business, whose
  customers' future behaviour can be laid out, from IBM's; Cisco's customers are IBM's kind **[M2017-019]**.
- *Can I name the winner, not just the industry?* (test 6). Networking will grow with AI traffic on the filer's account;
  "there’s industries we know that may have a wonderful future, but we don’t have the faintest idea who the winners will
  be" **[M2012-067]**; "Just because Charlie and I can clearly see dramatic growth ahead for an industry does not mean we
  can judge what its profit margins and returns on capital will be as a host of competitors battle for supremacy"
  **[L2009-005]**. I cannot name the winner of AI-data-center networking among Cisco, Nvidia, Broadcom-based systems,
  Arista and the hyperscalers' own designs.
- *How far off could I be?* (test 8, **[M2011-084]**). On the campus base, a fairly narrow range; on the data-center,
  hyperscaler and security halves, which drove all of FY2026's growth, very far.
- *Do I doubt it is inside?* (test 9). I do: "if you have doubts about something being into your circle of competence,
  it isn’t" **[M2002-092]**.

**The contrary evidence, answered.** (a) The steady aggregate record (gross margin within six points over nineteen years)
is real, and it is the strongest case for IN. But it was held at a price the filings show: about $53.8B of acquisitions
net of cash in the tagged years FY2008 to FY2026 (FY2019 to FY2021 untagged under that element), $26.0B of it in FY2024
alone for Splunk, and research spending of 12% to 16% of revenue every year (`arithmetic_output.txt`), while revenue grew
2.65% a year. The aggregate stayed level because the parts underneath it were replaced, which is the leader that must
"leverage its current leadership into new activities [...] Predicting whether somebody’s going to be able to do that in
advance is just — it’s too tough for us." **[M1997-022]**, and "Companies get left behind. We don’t want to be in
businesses where companies — where we feel companies can be left behind." **[M1997-023]**. A past that was kept steady by
continual reinvention does not tell me the next ten years' statements (test 3, **[M2008-033]**); "usually if something can
gain competitive advantage very quickly, you have to worry about them losing it quickly, too" **[M2002-050]**, and the
AI-infrastructure line gained its share of revenue in a single year. (b) The IBM purchase is the speakers' own narrated
case of this reasoning, and Buffett records the outcome: "I was wrong on the first one" **[M2017-019]**. It counts against
IN, not for it.

**Routing.** "A business whose ten-year economics cannot be foreseen because its industry changes fast closes here, at
Q1, in TOO HARD" (Q1, The routing, fixed; **[M1998-008]**, **[L1993-023]**). The rows give ignorance, not a finding against
Cisco, as the reason: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth.
It just means that we don’t know how to evaluate it." **[M2000-038]**. Not a bank, not a holding company.

**The cause.** NATURE, not WORK (section I, the two causes). The deciding question, Cisco's share of the network and of
security spending in 2036, is "a forecast the industry's own insiders would not write down" **[M2000-105]**, and the filer
says so in its risk factors. More reading would not cure it: "Our problem -- which we can't solve by studying up -- is that
we have no insights into which participants in the tech field possess a truly durable competitive advantage."
**[L1999-018]**; "We couldn't solve this problem, moreover, even if we were to spend years intensely studying those
industries." **[L1993-023]**. "If something’s important but unknowable, forget it." **[M2006-076]**. A lower price does not
reopen it **[M2000-038]**, and the circle is not widened to find something to buy **[M1995-018]**.

**VERDICT: TOO HARD (NATURE)** **[M2006-013]**. The file closes here.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (Q1 closed TOO HARD). One filing fact found on the way is recorded as found, not weighed: the filer's own
sentence "Barriers to entry are relatively low" (10-K FY2026, Item 1, Competition, `0000858877-26-000132`).

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. Recorded as found, not judged: the earnings release features non-GAAP figures that exclude stock pay (FY2026
non-GAAP EPS $4.33 against GAAP $3.33; stock pay $0.95 a share in the reconciliation; EX-99.1, `0000858877-26-000106`),
and gives annual guidance (FY2027 revenue $72.2B to $73.4B). Both would be read at Q4 under **[L2015-003]** and the
two-tell convention; neither was weighed here.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. (The proxy, `0000858877-25-000150`, was fetched and not read for judgment.)

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range is a finding of this run.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES: the bond, more of what I already own, the company's own stock? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US: the target's debt and exposures. WEIGHING.
NOT REACHED. (Total debt $29.5B at 2026-07-25 against cash and investments of $15.9B, MD&A, is recorded as found.)

## Q10 — IS IT THE FAT PITCH, and am I buying enough? WEIGHING.
NOT REACHED. The draft would have the buyer do nothing: inaction is the default **[M2004-045]**.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED (not asked; the operator did not choose it).

---
## THE BOX
**TOO HARD (NATURE), decided at Q1** **[M2006-013]**. The ten-year economics turn on Cisco's share of the AI data-center
network, on whether hyperscalers keep buying rather than designing their own, and on which security platform wins; the
filer itself says its "model of the evolution of networking, security, or observability" may not emerge as it believes
and that barriers to entry are relatively low, so the forecast is one the industry's insiders would not write down
**[M2000-105]**, **[L1993-023]**, **[L1999-018]**. The steady nineteen-year margin record is real contrary evidence, but it
was held by replacing the parts (about $53.8B of acquisitions, research at 12% to 16% of revenue) and so does not tell the
next ten years **[M1997-022]**, **[M2008-033]**. No research pass is opened (NATURE). Not a judgment of quality
**[M2000-038]**. **Reversal condition:** none by price; the box would reopen only if the filer's own account changed, that is,
if the data-center and security halves settled into a structure whose ten-year share could be written down as the campus
base can.

For reference only, **COMPUTATION — NOT A CLEARANCE** (operator rule 3; Q7 was not reached and none of this is a verdict):
five-year mean owner cash $10,653M, $2.70 a share, a 2.40% yield at $112.82; the no-growth case is worth $47.74 a share at
the 5.66% sovereign and $27.02 a share at the CONVENTION floor of ten percent; `tools/run.py` puts the growth the price
assumes at 13.3% a year at the sovereign. Aggregate owner cash fell 4.8% a year from FY2022 to FY2026 on the five-year
window, a figure distorted by the FY2023 and FY2024 tax swing, so no shown-growth case is computed.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). The
      template copy preceded every fetch; Step 0 to Q1 were committed together in `07d24c3` because Q1 closed the run
      and no question in between closed separately.
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before writing); every filing fact has its
      accession; no number without a row or a filing (the CONVENTION floor is labelled).
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost (OCF less stock pay less all capital spending), never a net-income proxy
      (operator rule 5); the sovereign from the US Treasury; the price quote flagged as aggregator.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (the foundations, (a) and (b)), and answered at Q1.
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the anchor is
      today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its D&A column was found defective and not used.
- [x] `python tools/check_framework.py` PASS before the commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Q1's routing sends "a business whose ten-year economics cannot be foreseen because its industry changes fast" to TOO
HARD, and its test 3 asks whether the past statements tell the future ones **[M2008-033]**; it gives no rule for the case
this name presents, an aggregate record that is steady for two decades (gross margin within six points) inside an industry
the filer itself calls fast-changing, where the steadiness was bought by continual replacement of the parts. I decided it
on the 1997 rows about leaders that must leverage into new activities **[M1997-022]**, **[M1997-023]**, the IBM outcome
**[M2017-019]**, and the doubt rule **[M2002-092]**; another analyst could weigh the steady record more and pass Q1 to fight
it out at Q2. A sentence saying whether a steady aggregate record answers test 3 when the filer's segments are being
replaced would make the close reproducible. Second, the Q7 range CONVENTION says the cash is carried "at the growth the
business has actually shown over those years, never above it", and is silent when the shown growth is negative because
of a base-year distortion inside the five-year window (here a tax-payment swing between FY2023 and FY2024); the
COMPUTATION above therefore shows only the no-growth case. Third, the "fair" and "cheap" prices the operator asks for are
not defined in the framework; the 2026-10-05 runs define them as reporting conventions (cheap: the no-growth owner cash at
the ten percent floor). Tool defects: `tools/run.py` reads the amortization of purchased intangibles as D&A for Cisco
(700, 1,028, 916 against the filed 2,507, 2,811, 2,540) and prints a duplicate, nearly empty FY2018 balance-sheet row.
