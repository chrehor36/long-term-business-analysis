# Company Run — Broadcom Inc. (Nasdaq: AVGO) — 2026-10-07
**Framework v5** (`Framework/THE FRAMEWORK v5.md`, as amended to 2026-10-07). Governing rules: `Framework/OPERATOR-PROTOCOL.md`.
The run form is the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Every
judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or TOO HARD closes the run
and later questions are marked NOT REACHED. Copied from `Test Runs/_TEMPLATE - Company Run.md` before any fetch.

**Dispatched blind run** under `Screens/_daily/_dispatch_brief.md`; research folder `Test Runs/_research 2026-10-07 AVGO/`.

**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.

**CONTAMINATION, declared.** Not opened, listed or searched: `PORTFOLIO.md`, any holding review, the resume-state files, the run
queue, the prepped reading list, any other run file about Broadcom (the dispatch message says earlier ones exist; none was opened),
any other company's run or research file. Seen by accident and not used: (1) the subjects of the five most recent commits, which
name the boxes of four other companies' runs (ACLS, ACNB, AMAT, ATR); (2) the session's opening git status, which lists research
folders of other runs (AYI, BDC, CHD, ARCB) by name only; (3) the memory index loaded into the session, whose lines give the state of
the queue and a count of gate-clearers, with no ticker of this company; (4) comments in `.gitignore` naming other runs (SNPS, DELL,
MGM, AGCO, ATR, Ford) for file-size reasons; (5) after the closing commit, `git log` showed a concurrent commit subject of another
company's run ("BMI run: Step 0, foundations, standing rule, Q1 IN"). Nothing in any of them concerns Broadcom; nothing was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $375.81 (close 2026-10-06; aggregator quote via `tools/run.py`, flagged per operator rule 5, live quote only).
- **Shares by class:** one class, common stock $0.001 par; **4,773,629,865** shares outstanding as of 2026-08-28 (cover of the 10-Q
  for the quarter ended 2026-08-02, filed 2026-09-10, accession `0001730168-26-000080`; `python Screens/cover_shares.py AVGO`).
  Checked: the 10-Q balance sheet gives "4,774 and 4,741 shares issued and outstanding as of August 2, 2026 and November 2, 2025"
  (millions); Broadcom retires repurchased shares, so issued equals outstanding and there is no treasury stock. Filings after the
  10-Q: the 8-K of 2026-09-02 (earnings, `0001730168-26-000076`), the S-4 of 2026-09-10 and the 424B3 of 2026-09-18
  (`0001193125-26-395593`), a registered exchange of existing 4.926% notes due 2037 for like notes; no shares issued by any of them.
- **Market cap:** 4,773.63M × $375.81 = **$1,793,980M**.
- **Sovereign for the earnings currency (USD):** **5.64%**, the 30-year par yield, US Treasury daily par yield curve, 2026-10-06
  (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K for FY2025 (year ended 2025-11-02, filed 2025-12-18, `0001730168-25-000121`); 10-Q for
  Q3 FY2026 (quarter ended 2026-08-02, filed 2026-09-10, `0001730168-26-000080`); proxy DEF 14A filed 2026-03-02
  (`0001193125-26-085691`); 10-Ks for FY2019 to FY2024 for the segment history and the acquisitions (`0001730168-19-000144`,
  `0001730168-20-000226`, `0001730168-21-000153`, `0001730168-22-000118`, `0001730168-23-000096`, `0001730168-24-000139`); the earnings
  releases of FY2024 Q4 (`0001730168-24-000125`), FY2025 Q4 (`0001730168-25-000116`), FY2026 Q1 (`0001730168-26-000011`), Q2
  (`0001730168-26-000051`) and Q3 (`0001730168-26-000076`); the 8-Ks of 2026-03-02 (`0001193125-26-085656`), 2026-04-02
  (`0001193125-26-140574`), 2026-04-06 (`0001193125-26-144028`), 2026-06-11 (`0001193125-26-266777`), 2026-06-18
  (`0001193125-26-275077`) and 2026-07-06 (`0001193125-26-295589`).
- **One figure cross-checked against the filed statement:** net cash provided by operating activities FY2025, $27,537M, as
  `tools/run.py` transcribes it, against the 10-K's consolidated statement of cash flows (`0001730168-25-000121`): "Net cash
  provided by operating activities | 27,537 | 19,962 | 18,085". Agrees, and so do FY2024 and FY2023.
- `tools/run.py AVGO`, arithmetic lines only (output kept at `_research 2026-10-07 AVGO/run_py_output.txt`): owner cash on the
  capex basis (operating cash less stock pay less capital spending) FY2023 $15,462M, FY2024 $13,673M, FY2025 $19,346M; five-year
  mean (FY2021 to FY2025) $14,975M. The "D&A basis" the tool prints subtracts amortization of acquired intangibles as well
  (FY2025 D&A $8,636M against depreciation of $574M in the 10-K), so it is not a maintenance figure; the capex basis is used, and
  depreciation ($574M FY2025) sits close to capital spending ($623M), so nearly all capital spending reads as maintenance. Stock
  pay is resolved and complete (tag ShareBasedCompensation each year, agreeing with the 10-K: "Stock-based compensation | 7,568 |
  5,741 | 2,171"). Nothing else the tool prints (its v4 lines, ids or floor) is used (Part VII).

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether the owner would be content holding this if the market closed for five years
**[M1997-109]**, and for Broadcom that turns on what its customers will be buying from it years out, which is Q1's question, not the
quotation's. The market serves and does not instruct **[M2006-077]**: a market value of about $1.79 trillion, up with the AI
revenue, tells the analyst only a price. Margin of safety: a close case needing pencil and paper "it’s too close to think about"
**[M1996-084]**. The analyst's habits govern the reading: look for "what’s wrong" and "what you’re missing" **[M2025-013]**, and
state the other side's case better than its holder before disagreeing **[M2016-055]**. **Contrary evidence, written down as found**
**[M1997-127]**: (1) the 8-K of 2026-04-06 (`0001193125-26-144028`) records a Long Term Agreement with Google for custom TPUs and a
supply assurance agreement "through up to 2031", and the 8-K of 2026-07-06 (`0001193125-26-295589`) multi-year agreements with
Apple "through 2031"; (2) the 10-Q (`0001730168-26-000080`) reports remaining performance obligations of "approximately $179.2
billion" under contracts that include ones "where customers do not have termination rights"; (3) the infrastructure software
segment (mainframe, VMware) earned $20,765M of segment operating income in FY2025 on $27,029M of revenue
(`0001730168-25-000121`), a franchise-like margin on an installed base. Each is a reason to think part of the next five years is
visible; each is weighed at Q1 below.

## THE STANDING RULE
Nothing in this run finances, sizes or holds a position; the rule binds the buyer's conduct, "We are never going to risk what we
have and need for what we don’t have and don’t need" **[M2012-081]**, and "borrowed money has no place in the investor's tool kit"
**[L2014-005]**. No breach arises from the analysis. (The target's own debt and its $29 billion lease backstop are Q9 matters,
recorded under AFTER THE STOP.)

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.

**The test as the draft states it.** "the first question is, can I understand it?" **[M1995-051]**, where understanding is "a
reasonable fix on about what the earning power and competitive position will look like in five or 10 years" **[M2012-065]** and
"being able to asses where the business will be in 10 years" **[M2000-037]**. Understanding the product is not enough: "We just
don’t know the economics of it 10 years from now" **[M2000-104]**.

**Which part decides (the business of parts, Q2's paragraph, which Q1's holding-company paragraph extends to operating segments).**
Segment operating income, from the 10-Ks (`0001730168-25-000121`, `0001730168-24-000139`, `0001730168-23-000096`), $ millions:

| fiscal year | semiconductor solutions | infrastructure software | unallocated |
|---|---|---|---|
| FY2021 | 10,976 | 4,936 | (7,393) |
| FY2022 | 15,075 | 5,219 | (6,069) |
| FY2023 | 16,486 | 5,639 | (5,918) |
| FY2024 | 16,759 | 13,977 | (17,273) |
| FY2025 | 21,232 | 20,765 | (16,513) |
| **five-year sum** | **80,528 (61.4%)** | **50,536 (38.6%)** | |

Semiconductor solutions carries more than half of five-year segment operating profit and **decides**; the software segment does
not. The trend runs further toward the semiconductor part: for the three quarters ended 2026-08-02 its operating income was
$29,554M against software's $18,295M, and its revenue was 70% of the third quarter's (`0001730168-26-000080`). A part that decides
and cannot be understood keeps the whole outside the circle, "if you have doubts about something being into your circle of
competence, it isn’t" **[M2002-092]**.

**What the semiconductor part now is, from the filings.**
- **It has become an AI business in three years.** AI revenue was $12.2B of FY2024's $30.1B semiconductor revenue, having "grew
  220 percent year-on-year" (release, `0001730168-24-000125`); in FY2026 it was $8.4B in Q1, $10.8B in Q2 and $16.7B in Q3, which
  "grew 221% year-over-year", with $21.7B guided for Q4 (releases `0001730168-26-000011`, `-000051`, `-000076`). Q3 FY2026 AI
  revenue alone ($16.7B) exceeds total quarterly revenue of a year earlier ($15,952M).
- **The customers are few and their own futures are the forecast.** One distributor customer was "50% and 46% of our net revenue
  for the fiscal quarter and three fiscal quarters ended August 2, 2026" (32% in FY2025, 28% in FY2024, 21% in FY2023); the top
  five end customers were "approximately 50% of our net revenue" for the three quarters (`0001730168-26-000080`; 10-K
  `0001730168-25-000121`). The Anthropic arrangement of 2026-04-06 states that its consumption "is dependent on Anthropic’s
  continued commercial success" (`0001193125-26-144028`).
- **The customers are also the competitors.** Customers may turn to "their internal development of competing products or
  customer-owned tooling"; competition increases "as new competitors, including our customers, enter our markets" (10-Q risk
  factors, `0001730168-26-000080`).
- **The company is financing the demand.** The 10-Q describes the "AI XPV platform", established "to enable more than 20 gigawatts in
  compute capacity [...] for the leading frontier AI labs through 2028", which "bridges the gap between the current cash flows of the
  leading frontier AI labs and significant upfront investments required for their businesses"; a first tranche of $35 billion was
  launched in June 2026 and Broadcom backstops a customer's five-year lease obligations with a "maximum potential liability under
  the Backstop upon the deployment of all AI racks, on an undiscounted basis, [of] approximately $29 billion" (Note 10,
  `0001730168-26-000080`).
- **The filer itself calls the field fast-changing and possibly a bubble.** "The semiconductor industry is undergoing profound change
  due to the adoption and proliferation of AI and has experienced a significant upturn, which may not be sustainable due to a
  market correction, the perceived existence of an AI spending "bubble" or other factors"; the industries are "characterized by
  rapid technological change [...] short product cycles, including due to AI-generated efficiencies" (`0001730168-26-000080`).
- **The business model is still moving.** The 10-K and 10-Q describe the move from selling chips to selling or leasing "AI racks or
  systems based on our XPUs", which "will likely increase our operating margin but compress or lower future gross margin"
  (`0001730168-25-000121`, `0001730168-26-000080`).

**The tests, applied.**
1. *Where will it be in ten years?* The FY2023 semiconductor segment ($28,182M revenue, AI about $3.8B implied by the FY2024 release's
   220% growth to $12.2B) does not describe the FY2026 one; the next ten years turn on the AI build-out of a handful of buyers.
2. *The key variables and how predictable they are* **[M1998-044]**: AI capital spending by five or so customers; whether they keep
   buying custom silicon from Broadcom or take it in house; the price of each accelerator generation; and whether the frontier labs
   can pay their leases. None is predictable from the filings; the company itself gives one quarter of guidance at a time.
3. *Do the past statements tell me the future ones?* **[M2008-033]**: no; three years ago the statements described a different
   business mix.
4. *Important and knowable?* The customers' ten-year AI spending is important. The filer's own description of it is that the upturn
   "may not be sustainable" and that one customer's consumption is "dependent on Anthropic’s continued commercial success" (above).
   So it is not knowable, and the row is plain: "If something’s important but unknowable, forget it." **[M2006-076]**.
5. *Would the insiders write it down?* The filer writes down one quarter and declines more. Its release says "Actual results will
   vary from the guidance and the variations may be material" (`0001730168-26-000076`). The row's case is exactly this one: "they
   would not want to put down on paper their predictions about where 10 companies you would choose in the tech field would be in 10
   years, in terms of their economics" **[M2000-105]**.
6. *Can I name the winner, not just the industry?* Custom accelerators against merchant GPUs against the customers' own designs is
   the contest of the moment; "there’s industries we know that may have a wonderful future, but we don’t have the faintest idea who
   the winners will be" **[M2012-067]**, and seeing "dramatic growth ahead for an industry does not mean we can judge what its profit
   margins and returns on capital will be as a host of competitors battle for supremacy" **[L2009-005]**.
7. *Customers or technology?* The forecast is of technology generations and of a few customers' capital programmes, not of consumer
   behaviour **[M2017-019]**.
8. *How far off could I be?* **[M2011-084]**: by a multiple; semiconductor operating income nearly doubled in nine months.
9. *Do I doubt it is inside?* Yes; "if you have doubts about something being into your circle of competence, it isn’t." **[M2002-092]**.

**The other side's case, stated as strongly as I can** (the habit of **[M2016-055]**). Broadcom is not a start-up. It has
long-term agreements with Google for custom TPUs and rack components and with Apple for custom silicon, both running to 2031
(8-Ks above); $179.2B of committed remaining performance obligations, about 25% of it expected within twelve months; an Ethernet
switching and routing line sold to hyperscalers and carriers (10-K); and a software segment whose mainframe and VMware installed
bases have earned rising segment margins. Read in full, the case gives visibility of perhaps five years of contracted volume for a
few customers. It does not reach the ten-year economics the test asks for: the contracts end by 2031, they fix volumes or shares
rather than the profit on each generation, one of them is expressly contingent on a customer's commercial success, and the company
is now guaranteeing a customer's ability to pay. A position gained this fast is the case the row warns of: "usually if something can
gain competitive advantage very quickly, you have to worry about them losing it quickly, too" **[M2002-050]**.

**Routing.** "a business that must deal with fast-moving technology is not going to lend itself to reliable evaluations of its
long-term economics" **[L1993-023]**; "if something comes in where there’s a technological component that’s of significance [...] it
won’t make it through the filter" **[M1998-008]**; change is "more of a threat into the investment process than an opportunity"
**[M1999-063]**. The framework's routing sends this case to TOO HARD at Q1, never OUT on the business: "It doesn’t mean it isn’t a
good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It just means that we don’t know how to evaluate it."
**[M2000-038]**.

**Which cause.** NATURE, not WORK. The deciding question (the ten-year economics of custom AI silicon sold to a handful of
customers, some of them financed by the seller) is the one the industry's own insiders would not write down **[M2000-105]**; the
filer itself publishes one quarter. More reading would not cure it: "We couldn't solve this problem, moreover, even if we were to
spend years intensely studying those industries." **[L1993-023]**; "Our problem -- which we can't solve by studying up -- is that we
have no insights into which participants in the tech field possess a truly durable competitive advantage." **[L1999-018]**; "if we
can’t make a decision in five minutes, we can’t make it in five months" **[M2008-086]**. No research pass is opened.

- **VERDICT: TOO HARD (NATURE)** at Q1, on the deciding part, semiconductor solutions (61.4% of FY2021 to FY2025 segment operating
  income): its ten-year economics depend on the AI capital programmes and in-house plans of about five customers, on a rack-leasing
  model with a $29 billion backstop, and on technology generations the filer calls rapidly changing; **[M2000-037]**,
  **[M2000-105]**, **[L1993-023]**, **[M2002-092]**, **[M2000-038]**.

## Q2 — WHY IS THE CASTLE STILL STANDING? STOP.
NOT REACHED (closed at Q1). The competitor row and the parts' margins are recorded under AFTER THE STOP.

## Q3 — HOW MUCH CAPITAL MUST GO IN? WEIGHING.
NOT REACHED.

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The balance sheets are read under AFTER THE STOP, as the brief directs for a file that closes before Q4.

## Q5 — WHO RUNS IT? STOP on integrity.
NOT REACHED.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. The reporting figures are computed under AFTER THE STOP, headed COMPUTATION, NOT A CLEARANCE.

## Q8 — IS IT BETTER THAN THE ALTERNATIVES? STOP.
NOT REACHED.

## Q9 — COULD IT RUIN US? WEIGHING.
NOT REACHED.

## Q10 — IS IT THE FAT PITCH? WEIGHING.
NOT REACHED.

## Q12 (optional) — WOULD WE BE PROUD OF HOW THE MONEY IS MADE?
NOT REACHED.

---
## THE BOX
**TOO HARD (NATURE)**, decided at **Q1**: the deciding part, semiconductor solutions (61.4% of FY2021 to FY2025 segment operating
income), has ten-year economics that turn on about five customers' AI capital programmes, their in-house designs, a rack-leasing
model with a $29 billion backstop, and technology generations the filer calls rapidly changing; the insiders publish one quarter.
Integrity facts recorded, not judged (Q5 below). For the reporting figures only, computed after the stop (COMPUTATION, NOT A
CLEARANCE): central range $60.70 to $118.69 a share against $375.81.

## AFTER THE STOP: FACTS FOUND, NOT WEIGHED
*Facts found that bear on later questions, each with its source **[M1997-127]**; written down, not weighed; no verdict; the box
unchanged (operator rule 2).*

### Bearing on Q2 (the parts, the field, the competitor row)
- **Segment operating margins** (segment operating income over segment revenue; segment figures exclude stock pay and amortization,
  which sit in "unallocated"; 10-Ks `0001730168-21-000153`, `0001730168-23-000096`, `0001730168-25-000121`, 10-Q
  `0001730168-26-000080`):

  | | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 9M FY2026 |
  |---|---|---|---|---|---|---|---|---|
  | semiconductor solutions | 49.0% | 49.7% | 53.8% | 58.4% | 58.5% | 55.7% | 57.6% | 61.1% |
  | infrastructure software | 65.8% | 65.9% | 69.8% | 70.7% | 73.8% | 65.1% | 76.8% | 80.5% |

- **The competitor row**, from each filer's own 10-K XBRL (GAAP operating income over revenue, fiscal years as each reports them;
  script `_research 2026-10-07 AVGO/peers.py`):

  | filer (latest 10-K accession) | span | GAAP operating margin by year, % |
  |---|---|---|
  | Broadcom (`0001730168-25-000121`) | FY2016 to FY2025 | -3.1, 13.4, 24.6, 15.2, 16.8, 31.0, 42.8, 45.2, 26.1, 39.9 |
  | Marvell (`0001835632-26-000011`) | FY2020 to FY2026 (the current registrant's XBRL starts there; earlier years sit under the predecessor registrant and were not read) | -9.0, -8.7, -7.8, 4.0, -10.3, -12.5, 16.1 |
  | NVIDIA (`0001045810-26-000021`) | FY2016 to FY2026 | 14.9, 28.0, 33.0, 32.5, 26.1, 27.2, 37.3, 15.7, 54.1, 62.4, 60.4 |
  | Qualcomm (`0000804328-25-000085`) | FY2016 to FY2025 | 27.6, 11.6, 2.7, 31.6, 26.6, 29.2, 35.9, 21.7, 25.8, 27.9 |
  | Microsoft (`0001193125-26-323660`) | FY2016 to FY2026 | 28.6, 30.1, 31.8, 34.1, 37.0, 41.6, 42.1, 41.8, 44.6, 45.6, 46.8 |
  | Oracle (`0001193125-26-277521`) | FY2016 to FY2026 | 34.0, 34.2, 33.7, 34.3, 35.6, 37.6, 25.7, 26.2, 29.0, 30.8, 30.6 |
  | VMware stand-alone, before the merger (`0001124610-23-000015`) | FY2016 to FY2023 | 20.7, 18.5, 18.8, 13.3, 20.3, 18.6, 15.1 |

  Owner cash (operating cash less stock pay less capital spending) over revenue, same sources: Broadcom 15.2% (FY2016) rising to
  44.5% (FY2022), then 26.5% (FY2024) and 30.3% (FY2025); Oracle 30.9% (FY2016) falling to -8.8% (FY2025) and -42.3% (FY2026) as its
  capital spending rose; Microsoft 16.4% in FY2026 against 24.5% to 29.7% before; NVIDIA 41.8% in FY2026; Qualcomm 9.9% to 26.1%;
  Marvell 1.3% to 15.8%. Not read and flagged: MediaTek (a custom-silicon rival, not an SEC filer); Alphabet's in-house TPU design
  work, which sits inside a filer but is not separately reported.
- **The customer-competitor overlap**: customers may turn to "their internal development of competing products or customer-owned
  tooling" (10-Q `0001730168-26-000080`); the Google and Apple agreements run to 2031 (`0001193125-26-144028`,
  `0001193125-26-295589`).
- **Software pricing and contract terms**: software revenue rose "primarily due to strong demand for our VCF product, including
  license revenue recognized on contracts where customers do not have the right to terminate and the transition to a subscription
  license model" (10-K `0001730168-25-000121`); "As of the fiscal quarter ended August 2, 2026, we no longer have termination for
  convenience provisions for the majority of new software contracts" (10-Q `0001730168-26-000080`).

### Bearing on Q3 (capital)
- Capital spending $443M to $623M a year FY2021 to FY2025, about 1% of revenue; depreciation $574M in FY2025; property and equipment
  $3,144M at 2026-08-02; capital spending $1,013M in 9M FY2026 (`0001730168-25-000121`, `0001730168-26-000080`).
- Working capital is growing with the AI revenue: trade receivables $7,145M to $13,707M, inventory $2,270M to $4,523M and other
  current assets $5,980M to $9,968M between 2025-11-02 and 2026-08-02; one customer was 44% of net receivables at 2025-11-02 (10-K).
- Capital paid for businesses: BRCM $35.7B (2016), Brocade $6.0B (2017), CA $18.8B (2018), Symantec's enterprise business $10.7B
  (2019) (10-K FY2020 `0001730168-20-000226`); VMware $86,290M total consideration (2023), of which $53,398M in 544 million shares
  and $30,788M in cash, with $54,206M allocated to goodwill and $45,572M to intangibles; VMware's end-user computing business sold
  for $3.5 billion on 2024-07-01 (10-K FY2024 `0001730168-24-000139`).

### Bearing on Q4 (the balance sheets, read first, eight to ten years **[M2025-032]**; and the accounts)
From `tools/run.py`'s ten-year table (first-filed XBRL) and the filed statements (10-Ks `0001730168-18-000084` to
`0001730168-25-000121`; 10-Q `0001730168-26-000080`), $ millions:
- **Equity against goodwill and intangibles.** Equity $20,285 (FY2017), $24,962 (FY2021), $81,292 (FY2025), $99,690 at 2026-08-02;
  the jump in FY2024 is the $53,398 of shares issued for VMware, not retained earnings. Goodwill $24,706 (FY2017) to $43,450 (FY2021,
  after CA and Symantec) to $97,801 (after VMware); intangibles $10,832 (FY2017), $17,554 (FY2019), $3,867 (FY2023), $40,583 (FY2024),
  $26,325 (2026-08-02). Tangible equity is negative at every year-end from FY2019 (FY2025: $81,292 less $97,801 less $32,273 is
  minus $48,782).
- **Retained earnings** stayed near zero through FY2024 (minus $129, $3,487, $0, $0, $748, $1,604, $2,682, $0 for FY2017 to FY2024):
  dividends and buybacks absorbed the earnings; $9,761 at FY2025 and $22,151 at 2026-08-02.
- **Debt** $17,431 (FY2017), $40,235 (FY2020, after CA and Symantec), $39,229 (FY2023), $67,566 (FY2024, after VMware), $65,136
  (FY2025), $59,419 at 2026-08-02 (principal $61,079: senior notes at effective rates of about 3.6% to 5.75% and $1,750 of term loans
  due 2028; an undrawn $7.5 billion revolver; a $4.0 billion commercial paper programme).
- **Cash** $11,204 (FY2017), $4,292 (FY2018), $12,163 (FY2021), $14,189 (FY2023), $9,348 (FY2024), $16,178 (FY2025), $23,975
  (2026-08-02).
- **Receivables and inventory against sales**: receivables $2,448 on revenue of $17,636 (FY2017) and $7,145 on $63,887 (FY2025);
  inventory $1,447 and $2,270; both doubled in the nine months to 2026-08-02 (above).
- **What the balance sheet does not show**: the $29 billion backstop and the $179.2B of committed contracts (Note 10 and the revenue
  note, `0001730168-26-000080`; "The fair value of the Backstop was not material").
- **The accounts**: the releases headline non-GAAP operating income and EPS beside GAAP, excluding "amortization of acquisition-related
  intangible assets, stock-based compensation expense, restructuring and other charges" among others (`0001730168-26-000076`); stock
  pay was $7,568M in FY2025 (11.8% of revenue) and $6,287M in 9M FY2026, with $18,221M unrecognized at 2026-08-02 (10-Q);
  restructuring and other charges appear in every year's statement of operations; amortization of acquired intangibles was $8,062M
  in FY2025 ($6,031M in cost of revenue, $2,031M in operating expenses), part of it software technology from CA, Symantec and
  VMware. The tool's "D&A basis" subtracts all of it.

### Bearing on Q5 (integrity facts recorded, not judged; a later run that reaches Q5 must answer them)
- **Guidance**: each quarterly release gives next-quarter revenue and non-GAAP operating margin guidance ("Fourth quarter fiscal year
  2026 Non-GAAP operating income guidance of approximately 66 percent of projected revenue", `0001730168-26-000076`), and reports
  AI revenue against "our forecast" ("above our forecast", `0001730168-26-000011`, `0001730168-26-000051`).
- **The adjusted figure featured**: the release's opening bullets and the CFO's quote lead with non-GAAP growth ("We delivered
  non-GAAP operating income growth of 92% year-over-year", `0001730168-26-000076`).
- **CEO pay**: total FY2025 compensation of $205,278,006 in the summary table (pay ratio 543 to 1; $35,034,926 in the company's
  supplemental table, which leaves out the front-loaded award), proxy `0001193125-26-085691`. The 2025 Tan PSU Award pays 0% to
  300% of 610,521 target shares on "AI Revenue" over any four consecutive quarters in FY2028 to FY2030, threshold $60 billion,
  maximum $120 billion; the metric is revenue, not profit or return on capital, while the 10-Q records that the company backstops a
  customer's rack leases and finances AI capacity through the AI XPV platform (`0001730168-26-000080`).
- **Pledging**: a director (Dr. Samueli) pledged 16,175,000 shares on 2024-11-15 under a board-approved exception (proxy).
- **Officers**: the CFO retired effective 2026-06-12 and was succeeded by Alphabet's former chief accounting officer (8-K
  `0001193125-26-140574`).

### Bearing on Q6 (the money and the owners)
- **Dividends paid**: $5,913M, $6,733M, $7,645M, $9,814M, $11,142M (FY2021 to FY2025), $41,247M in all against five-year owner
  cash of $74,877M; $0.65 a quarter in FY2026 (`0001730168-26-000076`).
- **Buybacks and their prices** (split-adjusted; 10-K `0001730168-25-000121`, 10-Q `0001730168-26-000080`): FY2023 91 million shares
  for $5,824M (about $64 each); FY2024 67 million for $7,176M (about $107); FY2025 16 million for $2,450M (about $153); 9M FY2026 25
  million for $8,450M (about $338). Shares withheld for taxes on vesting cost $1,299M to $5,216M a year FY2021 to FY2025, nil in 9M
  FY2026. No programme names a price (programmes of $10 billion and $11 billion "from time to time"). Against the computed central
  range below ($60.70 to $118.69), the FY2023 purchases sit near its bottom, FY2024's inside it, and FY2025's and FY2026's above its
  top (COMPUTATION, NOT A CLEARANCE).
- **Issuance**: 544 million shares for VMware in 2023; shares outstanding rose from 4,741M to 4,774M in the nine months to
  2026-08-02 while 25M were repurchased (10-Q).

### Bearing on Q9 (debt and exposures)
- Net debt $35,444M at 2026-08-02 (debt $59,419M less cash $23,975M; no finance leases at FY2025; operating leases left out).
- The Backstop: "maximum potential liability under the Backstop upon the deployment of all AI racks, on an undiscounted basis, was
  approximately $29 billion", over five-year lease terms, the liability "equal to any difference between 85% of the outstanding
  amounts owed on the lease Backstop and the value of the AI racks"; and "Where necessary, we may provide residual value guarantees"
  (Note 10 and MD&A, `0001730168-26-000080`).
- Warranty and indemnification provisions "in agreements with some of our largest customers, are potentially unlimited" (10-K
  `0001730168-25-000121`, risk factors).

### COMPUTATION, NOT A CLEARANCE: the two reporting figures (the brief's reporting convention; not a verdict, no entry language)
Script and output: `_research 2026-10-07 AVGO/q7_computation.py` and `q7_computation_output.txt`. Q7's construction as the
framework writes it: five-year owner cash after every real cost, carried at the growth shown for ten years and then at zero nominal
growth, at the sovereign 5.64%; the ends are the no-growth and shown-growth cases; the all-equity basis central, equity-only beside.
- **Owner cash** (operating cash less stock pay less capital spending; never net income), $ millions: FY2021 11,617; FY2022 14,779;
  FY2023 15,462; FY2024 13,673; FY2025 19,346; five-year mean 14,975. Before interest (interest paid added back net of a 21% shield):
  12,853; 15,874; 16,649; 16,240; 21,457. **CONVENTION of this run: the interest shield at 21%, the US federal statutory rate**;
  rationale: the debt is the US parent's and the framework names no rate for the add-back.
- **The merger inside the window (specific (c))**: VMware's own owner cash before interest, from its 10-Ks, added for the years
  before the merger (fiscal year ended 2022-01-28: $3,054M; ended 2023-02-03: $2,791M, used again for Broadcom's FY2023 because
  VMware filed no later full year; an approximation, said so). Combined companies: 15,907; 18,665; 19,440; 16,240; 21,457; mean
  **$18,342M**; growth between end years **7.8%** a year. The deal's financing is already in today's net debt and share count, so
  it is not deducted a second time.
- **The window holds a merger, a divestiture (EUC) and the start of a boom**: the trailing four quarters (Q4 FY2025 plus 9M FY2026)
  give owner cash of $30,921M ($33,383M before interest), about twice the five-year mean; shown beside, not used as the base (one
  year, on the filer's own words "a significant upturn, which may not be sustainable").
- **Net debt** $35,444M; enterprise value at the price $1,829,422M; the central base is 1.00% of it, the trailing four quarters 1.82%.

| case | base, growth | value range a share (all-equity) | top over bottom | fair price |
|---|---|---|---|---|
| **A. central: combined companies, before interest** | $18,342M, 7.8% | **$60.70 to $118.69** | 1.85 | **$44.63** |
| B. beside: Broadcom as filed, acquisitions net of divestitures deducted, total growth credited | $12,124M, 13.7% | $37.61 to $125.09 | 2.94 | $38.18 |
| equity-only beside A: combined, after interest, against market value | $16,579M, 7.5% | $61.58 to $111.16 | 1.81 | $46.40 |
| C. shown only: trailing four quarters, combined growth | $33,383M, 7.8% | $116.57 to $222.11 | 1.85 | $87.32 |
| D. shown only: trailing four quarters, as-filed growth | $33,383M, 13.7% | $116.57 to $357.45 | 2.94 | $118.14 |

**The fair price** here is the per-share value, on the all-equity basis, of the midpoint of the two ends' cash streams discounted
at the floor of about ten percent (the mean of the no-growth and shown-growth streams' values at 10%, less net debt, over the
shares), owner cash after the company's own tax, no conversion. In every case, the boom year as base included, the price of
$375.81 sits above the top of the range.

---
## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early). Step 0 and Q1,
      the closing question, were committed together (`f11d0172`); the after-the-stop facts and the close in a second commit.
- [x] Dispatched: the brief allowed the per-question pathspec commits; the lock is the dispatching session's (a lock file was
      present in `Screens/_daily/` and was not touched). The fold is the dispatcher's; a run not in the register binds nothing.
- [x] No other run file, holding review or `PORTFOLIO.md` was opened, listed or searched; what was seen by accident is declared
      under CONTAMINATION and not used.
- [x] Every v5 id resolves in `principle_ledger_v5.csv` and every quoted fragment beside an id is in that row (check script
      `_research 2026-10-07 AVGO/check_ids.py`); every filing fact carries its accession.
- [x] The order was kept; Q1, the first STOP, closed the run; everything after it is a recorded fact or a COMPUTATION.
- [x] Owner cash after every real cost (operating cash less stock pay less capital spending), never net income; the sovereign from
      the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence written down as found (THE FOUNDATIONS, three items, weighed at Q1 as the other side's case); facts for later
      questions under AFTER THE STOP; the integrity flag in the box line.
- [x] Not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used; its "D&A basis" was set aside with the reason given.
- [x] `python tools/check_framework.py` PASS before the closing commit (result in the commit message).

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **Q7 specific (c), a merger inside the window**, says "valued on the combined companies' own averages, with the deal's financing
deducted", but does not say how to align a target whose fiscal years differ from the acquirer's (VMware's ended in January or
February), what to use for a pre-merger year the target never filed in full (Broadcom's FY2023), or whether "the deal's financing
deducted" means a second deduction when today's net debt and share count already carry it. This run aligned by nearest year, reused
VMware's last full year, and did not deduct twice; all three are said in the computation. (2) **The fair price** ("the price at
which the midpoint of the range earns the floor", Part VII and the template) does not say whether the midpoint is the midpoint value
or the midpoint cash stream valued again at the floor; the two differ. This run took the mean of the two ends' streams valued at
10%. (3) **The interest add-back** for the all-equity basis ("owner cash before interest and after the company's tax") names no rate
for the tax shield; this run confessed 21% as its own CONVENTION. (4) **The business of parts at Q1**: the decide-threshold is "more
than half of the company's five-year operating profit", but the filer's segment profit leaves out $16 to $17 billion a year of
"unallocated" stock pay and amortization; the run used the filer's segment measure, and the framework does not say which measure to
use. (5) **The brief's error, as the dispatch message asked**: the brief's reporting paragraph asks for "a whole-cycle variant beside
it if the five-year window holds a boom, a trough, a merger or a divestiture", but Q7 does not treat a merger as a cycle: specific
(a) covers peaks and troughs, while specific (c) makes the combined companies' own averages the treatment of a merger inside the
window, the central figure and not a variant beside it. This run followed Q7 (case A central) and showed the as-filed case and the
boom year beside it. The dispatch message's "Q7's section on acquisitions" also names a section Q7 does not have; the text is
specific (c) of the "Six more specifics". Smaller: the brief's "If Q1 to Q6 pass" treats Q3 and Q6, which are WEIGHINGs, as if they
passed or failed.
