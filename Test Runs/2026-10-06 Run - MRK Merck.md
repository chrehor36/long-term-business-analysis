# Company Run — Merck & Co., Inc. (NYSE: MRK) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. **Copy this file to its dated name before any fetch.**

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md`, holding
reviews, the session-state files, the register, the prepped reading list and `tools/alerts.json` were not opened, and
no attempt was made to learn whether anyone holds or wants this name.

**CONTAMINATION, declared.** (1) A directory listing of `Test Runs/` (taken to pick a run file for form) showed the names
of the 2026-10-05 runs, among them `2026-10-05 Run - OGN Organon.md`; Organon was spun out of Merck. That file was not
opened, and the form was taken from the HUBB run, which has nothing to do with this name. Whether an earlier MRK run or
research folder exists was not checked, and none was opened. (2) The analyst knows Merck in general terms from training
(Keytruda as its largest product, the Organon spin, its standing as an old research-based drug house); that is a prior,
and every fact below is from the filings cited. (3) The v5 ledger names Merck in two rows, one about other people's method and
one about drug companies' secrecy (**[M2021-047]**), neither about the business (**[M2003-069]**: "determining whether Pfizer or Merck is going to do better over the next 20
years"); it is quoted at Q1 for what it says about the method, not as a verdict on the company.

Working folder: `Test Runs/_research 2026-10-06 MRK/` (`fetch.py`, `owner_cash.py` and its output, `filing notes.md`,
the outputs of `tools/run.py`, `tools/sources.py` and `Screens/cover_shares.py`; raw filings in its gitignored `cache/`).

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $139.54 (close 2026-10-05; the quote `tools/run.py` takes from an aggregator, live quote only, flagged per
  operator rule 5).
- **Shares by class** from the latest filing's cover: one class, common stock, **2,467,171,638** as of 2026-07-31
  (Form 10-Q for the quarter to 2026-06-30, filed 2026-08-07, accession `0000310158-26-000212`;
  `python Screens/cover_shares.py MRK`, single class, undimensioned). The balance sheet's issued count (3,577.1M)
  includes treasury shares and is not used.
- **Market cap:** 2,467.17M x $139.54 = **$344,269M**.
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, dated
  2026-10-05 (`python tools/sources.py`, issuing authority).
- **Filings read** (operator rule 4): 10-K FY2025 (filed 2026-02-24, `0000310158-26-000063`): Item 1 in full to the
  trademarks paragraph (product sales, the franchises, competition, the health-care environment, the IRA, the MFN
  Agreement, China, the patent tables), the Item 1A summary and the patent, exclusivity, key-product and R&D risk
  factors, the income statement and the cash-flow statement; 10-K FY2022 (filed 2023-02-24, `0001628280-23-005061`):
  the cash-flow statement for 2020 to 2022; 10-Q Q2 2026 (filed 2026-08-07, `0000310158-26-000212`): cover, cash flows,
  the Cidara and Terns notes, product sales; proxy (DEF 14A filed 2026-04-08, `0001193125-26-147704`): fetched and
  opened, not read for Q5 or Q6, which the run does not reach; 8-K of 2026-08-04 (`0001104659-26-090045`), Exhibit 99.1,
  the Q2 2026 release: the headline page. Extracts are in `filing notes.md`.
- **One figure cross-checked against the filed statement:** operating cash flow FY2025 **$16,472M**, capital
  expenditures **$4,112M** and share-based compensation **$820M** in the filed Consolidated Statement of Cash Flows
  (10-K FY2025, `0000310158-26-000063`) against `tools/run.py`'s 16,472, 4,112 and 820: they agree.
- **`python tools/run.py MRK`, arithmetic lines only** (output saved as `run_py_output.txt`). The share count agrees with
  the cover; stock pay is resolved (645, 761, 820 for 2023 to 2025, as filed); no securities purchases or other stock-pay
  lines sit inside operating cash flow. Nothing it prints as a rule, id, floor or verdict is used (Part VII).

**Owner cash after every real cost** = operating cash flow (continuing operations) less stock pay less all capital
expenditures (USD millions). The fifth column is a variant the filings force on this name: the cash paid each year to
buy businesses and drug candidates (net of cash acquired, investing section of the same statements), because the 10-K
says the company's future "is dependent on its pipeline of new products, including [...] products that it is able to
obtain through license or acquisition" (Item 1A). `owner_cash.py` holds the arithmetic.

| FY | OCF | stock pay | capex | owner cash | bought (businesses, candidates) | after bought | source |
|---|---|---|---|---|---|---|---|
| 2021 | 13,122 | 479 | 4,448 | **8,195** | 12,907 (Acceleron, Pandion, other) | -4,712 | 10-K FY2022 `0001628280-23-005061` |
| 2022 | 19,095 | 541 | 4,388 | **14,166** | 121 | 14,045 | same |
| 2023 | 13,006 | 645 | 3,863 | **8,498** | 12,032 (Prometheus, Imago) | -3,534 | 10-K FY2025 `0000310158-26-000063` |
| 2024 | 21,468 | 761 | 3,372 | **17,335** | 4,093 (EyeBio, Elanco aqua, Harpoon, Curon) | 13,242 | same |
| 2025 | 16,472 | 820 | 4,112 | **11,540** | 10,042 (Verona Pharma) | 1,498 | same |
| **5-yr mean** | | | | **11,947** | 7,839 | **4,108** | |

In the first half of 2026 a further $14,621M was paid (Cidara $8,779M, Terns $5,842M, 10-Q `0000310158-26-000212`), and
$13,811M of "charges for research and development asset acquisitions" put the half year at a net loss. **COMPUTATION —
NOT A CLEARANCE** (operator rule 3): the five-year owner cash is 3.47% of the market value before purchases of drug
candidates and 1.19% after them, against a 5.66% sovereign. Nothing here is a value or an entry; Q7 is not reached.

## THE FOUNDATIONS (not a gate)
A share is a business: the test is whether one would be content to own Merck "if the market closed for five years"
**[M1997-109]**, which turns every question toward what the business will earn ten years out and away from the
quotation. No macro forecast enters **[M2000-094]**; the IRA, the MFN Agreement and the vaccine-schedule changes the
10-K describes enter only as facts about Merck's own cash, not as a forecast of policy. Who is paid to tell you: the
company's own releases lead with "Broad, Diverse Pipeline" (EX-99.1, `0001104659-26-090045`), and the speakers' warning
on a seller's projection of what he sells **[M2020-037]** is kept in mind when the pipeline is read. The analyst's
habits bear hardest: ask "What do I not know that I need to know?" **[M1999-129]**, look for "what you’re missing"
**[M2025-013]**, and distrust one's previous conclusion **[M2016-054]**; the prior from training is that big pharma is a
good business, and the rows themselves say the industry as a group was (Q1, below), so the hunt for disconfirming
evidence is aimed at that prior.

**Contrary evidence, written down as found** **[M1997-127]**:
1. Against a quick TOO HARD: the speakers called pharmaceuticals, as an industry, understandable and good: "the future
   of the pharmaceutical industry was easier to predict than the future of the high-technology sector" and "a far, far
   better record of returns on large amounts of equity over time" **[M2001-002]**; missing the 1993 group was "a
   mistake" **[M1997-120]**, **[M1999-043]**. Merck is one of the leading companies they meant.
2. Against a quick TOO HARD: Merck's business is broad. Animal Health ($6,354M, growing), vaccines with no generic
   threat in the ordinary sense (ProQuad/M-M-R II/Varivax $2,451M; the company is "the only manufacturer in the U.S. of
   MMRV vaccine (ProQuad) and varicella vaccine (Varivax)"), and late-patented launches (Winrevair, data exclusivity to
   2036; Capvaxive, 2038; Welireg, 2035; Keytruda Qlex, 2043) (10-K FY2025, Item 1).
3. For it: Keytruda was 49% of 2025 sales ("sales of Keytruda represented 49% of the Company’s total sales", Item 1A),
   and products whose key US patent expires between 2026 and 2028 were $42,748M, **65.8%** of 2025 sales (Keytruda,
   Gardasil/Gardasil 9, Januvia/Janumet, Bridion, Lynparza; Lenvima left out because its generic entry is "not expected
   until July 2030"; `owner_cash.py`).
4. For it: the 10-K expects Keytruda to be "materially negatively impacted by biosimilar competition between 2028 and
   2029", and separately expects Keytruda's selection for US government price setting effective 2029, after which "U.S.
   sales of Keytruda will decline materially" (Item 1).
5. For it: Gardasil/Gardasil 9 fell from $8,583M to $5,233M in one year, the China business "experienced significant
   contraction" (Item 1), and in January 2026 the US recommended HPV dose for adolescents was cut to one.
6. For it: in five years the company paid $39,195M, and $53,816M by mid-2026, for businesses and drug candidates; the
   five-year purchases (mean $7,839M) took about two thirds of the five-year owner cash (mean $11,947M).

## THE STANDING RULE
The run is a part-interest bought for cash with no borrowing, at whatever size Q10 would set; nothing in the purchase
lets "the other fellow" "call your tune" **[M2006-079]**, and the rule "Never risk permanent loss of capital." **[L2023-005]**
binds the buyer's sizing and financing, not this target. No ruin to the buyer from owning it, on those terms.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
**The test.** Understanding is "a reasonable probability of being able to asses where the business will be in 10
years" **[M2000-037]**, "a reasonable fix on about what the earning power and competitive position will look like in
five or 10 years" **[M2012-065]**; knowing the product is not enough: "We understand what it does for people. We just
don’t know the economics of it 10 years from now." **[M2000-104]**. The run takes the tests of Q1 in turn.

**1. Where will it be in ten years?** **[M1999-132]**. In 2035 Merck's earnings will come mostly from products it does
not sell today, or sells today in small amounts, or has not yet bought. The 10-K's patent table puts the key US patent
expiry of Januvia, Janumet, Bridion and Lenvima in 2026, Lynparza and Bravecto in 2027, Gardasil, Gardasil 9 and Keytruda
in 2028 (Item 1, `0000310158-26-000063`); the products whose key US patent ends in 2026 to 2028 were $42,748M, 65.8% of
2025 sales (Step 0). The company says what follows in its own words: "Expected declines in sales of products after the
loss of market exclusivity mean that the Company’s future success is dependent on its pipeline of new products,
including new products that it may develop through collaborations and joint ventures and products that it is able to
obtain through license or acquisition." (Item 1A). The ten-year picture is therefore a picture of the pipeline.

**2. The key variables, and how predictable they are** **[M1998-044]**. Three decide the 2035 earnings, each read from
the filing:
- *Keytruda after 2028.* Biosimilar competition "between 2028 and 2029", Europe in 2031, and US government price setting
  expected from 2029, after which "U.S. sales of Keytruda will decline materially" (Item 1); how much of the franchise
  the subcutaneous Keytruda Qlex (patent 2043; $463M in Q2 2026, EX-99.1) carries past the cliff is not stated anywhere
  in the filings, and it turns on how prescribers and payers choose between a new form and a cheaper biosimilar.
- *Which candidates succeed.* The 10-K lists one candidate under FDA review and nineteen Phase 3 candidates with US
  patents from 2029 to 2041 (Item 1). The filer's own words on the odds: "There is a high rate of failure inherent in the
  research and development process for new drugs and vaccines" and "failure can occur at any point in the process,
  including later in the process after significant funds have been invested" (Item 1A).
- *What is bought, and at what price.* $53,816M was paid for businesses and candidates from 2021 to mid-2026 (Step 0),
  including $16.0 billion in the first half of 2026 alone for Cidara and Terns (10-Q `0000310158-26-000212`). What the
  next decade's purchases will be, and what they will earn, cannot be read from anything filed.

A fourth variable is political: the IRA price setting, the MFN Agreement of December 2025 (new launches "subject to
"most-favored-nation" pricing"), and the vaccine-schedule changes of 2025 and 2026 (Item 1). The speakers declined to
judge exactly this for the industry: "much of it is in the political realm. And my judgment about the — what
politicians will do is probably not better than yours." **[M2005-098]**.

None of the three is predictable from where the analyst stands. "If something is not very predictable, forget it."
**[M1998-044]**.

**3. Do the past statements tell me the future ones?** **[M2008-033]**. No. The statements of 2021 to 2025 describe a
business half of whose sales came from one antibody whose US exclusivity ends inside the forecast horizon; they do not
tell what the 2035 statements will look like. Even the five-year owner cash is a poor guide: it is $11,947M a year
before, and $4,108M after, the purchases of candidates the company itself says it must make (Step 0).

**4. Is it important and knowable?** **[M2006-076]**. Important: the pipeline decides the whole of the earning power
past 2028. Knowable: no; see test 5.

**5. Would the insiders write it down?** **[M2000-105]**. The filer, who knows its own pipeline best, writes that
failure "can occur at any point" and that "no one can predict the effect of these and other factors on the Company’s
business" (Item 1, health-care environment); it gives no ten-year forecast. The speakers say the same of the field:
"when we invest in something like pharma, we don’t know the answer on the pipeline. It will be a different pipeline
anyway five years from now." **[M2008-113]**; "You shouldn’t be trying to guess whether, you know, one drug company has a
better drug pipeline than another." **[M2007-069]**; "we bring nothing to the table when it comes to evaluating patents
[...] So we simply don't get into judgments in those fields." **[L1999-019]**.

**6. Can I name the winner, not just the industry?** **[M2012-067]**. This test decides the run, and the rows answer it
for this industry by name. The industry, as a group, is inside the speakers' circle; a single company is not:
"it was within our circle of competence to identify the industry as likely to enjoy very high profits over time. It
would not have been within our circle of competence to try and pick a single company." **[M1998-073]**; "it’s easy for me
to figure out that Coca-Cola’s the soft drink company to be in [...] than it is for me to figure out which one in the
pharmaceutical." **[M1997-119]**; "I do think it’s very hard to pick out the winner. You know, so if I did buy them, I
would buy them — I would buy a group of the leading companies." **[M1999-044]**; "We would not have great insights on
specific companies. [...] It’s hard to evaluate the individual companies." **[M2002-060]**. The one row that names Merck
puts the question this run would have to answer, whether "Pfizer or Merck is going to do better over the next 20 years",
as the thing most professional managers wrongly think they can settle by hiring staff **[M2003-069]**.

**7. Is the forecast about customers or about technology?** **[M2017-019]**. About technology and regulators: whether
molecules work in trials, and what prices governments set. The customer (the prescriber, the payer) chooses on clinical
data and price, and the 10-K says competitors' new products "may result in price reductions and product displacements,
even for products protected by patents" (Item 1, Competition).

**8. How far off could I be?** **[M2011-084]**. Very far: the range runs from a Keytruda successor portfolio as large as
Keytruda, to a business whose owner cash is consumed for years by the purchases needed to replace it (2021 and 2023 show
negative owner cash after purchases, Step 0).

**9. Do I doubt it is inside?** "if you have doubts about something being into your circle of competence, it isn’t."
**[M2002-092]**. There is doubt, on the rows' own showing.

**The contrary evidence, weighed.** The rows that call pharma understandable (**[M2001-002]**, **[M1999-043]**) are rows
about the industry as a group bought "at a below-market multiple" **[M1999-043]**, and the same speakers say the group is
the only way they would take it **[M1999-044]**, **[M2008-113]**. Merck's breadth (Animal Health, the pediatric
vaccines, the late-patented launches) is real, but those lines were $13,526M of 2025 sales (Animal Health
$6,354M, ProQuad/M-M-R II/Varivax $2,451M, Winrevair $1,443M, Capvaxive $759M, Welireg $716M, Prevymis $978M,
Vaxneuvance $825M, Item 1) against $42,748M whose patents end by 2028; they do not carry the ten-year
picture. Munger's test fits the case exactly: "Take pharmaceuticals, if they had never invented any more
pharmaceuticals, it would be a terrible business." **[M1999-075]**. Merck has to keep inventing or buying, and the
rows do not claim to know who will succeed at that.

**Which box.** The framework's routing sends a business "whose ten-year economics cannot be foreseen" to TOO HARD at
Q1, "never OUT on the business" (Q1, Sent to TOO HARD), and the rows give ignorance as the reason, not a finding against
the business: "It doesn’t mean it isn’t a good buy. It doesn’t mean it isn’t selling for a fraction of its worth. It
just means that we don’t know how to evaluate it." **[M2000-038]**. **[M1999-075]** stands in the framework's "rules OUT"
list, but its row is filed as a test ("that dependence is a risk") and the industry it describes is the one the
speakers call good as a group (**[M2001-002]**), so OUT on the business would contradict the rows; the run reads it as
TOO HARD and records the ambiguity below.

**The cause** (section I, the two causes). **NATURE, not WORK.** The deciding question is which of nineteen Phase 3
candidates and an unknown number of future purchases will replace Keytruda's earnings, at prices governments have not
yet set. The filer would not write that forecast down (test 5), and the speakers say study does not cure it in this
field: "Sometimes our own intellectual shortcomings would stand in the way of understanding, and in other cases the
nature of the industry would be the roadblock." **[L1993-023]**; "we don’t know the answer on the pipeline. It will be a
different pipeline anyway five years from now." **[M2008-113]**. No research file is opened: "we’re not going to learn
enough in the followings five months to make up for the fact that we went in deficient in the first place."
**[M2008-086]**. A lower price does not reopen it **[M2000-038]**.

- **VERDICT: TOO HARD (NATURE).** The ten-year economics of a single research-based drug company, two thirds of whose
  2025 sales lose key US patent protection by 2028 (10-K FY2025, `0000310158-26-000063`), cannot be foreseen, and the rows
  place the choice of a single pharmaceutical winner outside the circle by name (**[M1998-073]**, **[M1997-119]**,
  **[M2008-113]**, **[M2012-067]**, **[M2002-092]**, **[M2006-013]**). The file closes here; nothing after this question is
  a clearance.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
NOT REACHED (closed at Q1). The competitor row was not filled.

## Q3 — HOW MUCH CAPITAL MUST GO IN to get the earnings out, and what does the added capital earn? WEIGHING.
NOT REACHED. (Step 0 records, as arithmetic only, the purchases of candidates beside the owner cash.)

## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS after every real cost? STOP on confusion or suspicion; otherwise WEIGHING.
NOT REACHED. The ten-year balance sheet table printed by `tools/run.py` is saved in `run_py_output.txt` and was not
read as a Q4 finding; the EX-99.1 headline (a non-GAAP loss per share that includes the Terns charge) was noted and not
judged.

## Q5 — WHO RUNS IT: able, honest, in love with the business, the same after being paid. STOP on integrity.
NOT REACHED. The proxy was fetched and not read for this question.

## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS? WEIGHING.
NOT REACHED.

## Q7 — WHAT IS IT WORTH? STOP.
NOT REACHED. No value range was computed; the owner-cash yields in Step 0 are headed COMPUTATION — NOT A CLEARANCE.

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
**TOO HARD (NATURE), decided at Q1.** Merck's earning power in ten years depends on which drug candidates, its own or
bought, replace Keytruda (49% of 2025 sales; US biosimilars from 2028 and US price setting from 2029) and the other
products whose key US patents end by 2028 (65.8% of 2025 sales together). The filer will not forecast that, and the rows
put the choice of a single pharmaceutical winner outside the circle by name **[M1998-073]**, **[M1997-119]**,
**[M2008-113]**. Q7 was not reached; no range is stated beside the price of $139.54. Not a judgment of quality
**[M2000-038]**, and a lower price does not reopen it. What would change the box is a change in the business, not the
price: a Merck whose ten-year cash came mainly from lines that do not depend on new inventions succeeding (Animal Health,
the pediatric vaccines) would have to be run again from Q1.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch (commit `f1e2c1b`); written question by question; committed after each
      (Step 0 `ca7144e`, Q1 `0c55bdb`, this close).
- [x] Every v5 id resolves (each grepped in `principle_ledger_v5.csv` before it was written; one id caught and replaced
      before the first commit: the "call your tune" words are **[M2006-079]**, not M2004-065); every filing fact has its
      accession; no number without a row or a filing.
- [x] The order was kept; the first STOP that failed (Q1) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost, never a net-income proxy (operator rule 5); the sovereign from the issuing
      authority; the aggregator price flagged.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (six items, Foundations; weighed at Q1).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; the run is dated
      today.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII).
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
(1) **OUT or TOO HARD for "Businesses that live on continued invention".** Q1's "What it rules OUT" list carries
**[M1999-075]** ("if they had never invented any more pharmaceuticals, it would be a terrible business") as an OUT, while
the routing paragraph and "Sent to TOO HARD, not OUT" send any business whose ten-year economics cannot be foreseen to
TOO HARD, and the row itself is filed as a test that names a risk, about an industry the same speakers call good
(**[M2001-002]**, **[M1999-043]**). Two analysts could close this name OUT or TOO HARD at choice, the same split the
correction pass of 2026-10-05 fixed for rapid change. The run chose TOO HARD on **[M2000-038]**'s reason; the item should
be moved beside the rapid-change item, or its box stated. (2) **The basket the rows prefer has no run form.** For this
industry the rows recommend "a group of the leading companies" bought at a below-market multiple (**[M1999-044]**,
**[M1999-043]**, **[M2008-113]**, **[M2002-060]**), and the open question in VI, Q1 (**[M2002-060]** and **[M2010-085]**
against **[M2002-092]**) is marked READER only. The template runs one company; nothing says whether a single member of
such an industry should be run at all, or how a group would be run and valued. (3) **Bought pipeline as a real cost.**
Owner cash "after every real cost" does not say whether cash paid to acquire drug candidates (here $7,839M a year,
recorded by the filer as investing cash, and expensed as acquired IPR&D in the income statement) is a cost of staying in
place or a growth outlay. For a company whose 10-K says its future depends on products "it is able to obtain through
license or acquisition", the choice moves the five-year owner cash from $11,947M to $4,108M. Step 0 shows both; Q3 or Q4
should say which governs before a drug company reaches Q7. (4) **Tool notes, no defect found.** `tools/run.py` printed
the arithmetic correctly against the filed statement; its five-year "OE capex" mean (11,943) differs from the
continuing-operations figure recomputed here (11,947) by four million; the cause was not traced
(the tool prints only three years); immaterial, recorded.
