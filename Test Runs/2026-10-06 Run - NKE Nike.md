# Company Run — NIKE, Inc. (NYSE: NKE) — 2026-10-06
**Framework v5** (`Framework/THE FRAMEWORK v5.md`). Governing rules: `Framework/OPERATOR-PROTOCOL.md`. The run form is
the one fifteen test runs used (`Framework/v5/tests/PROTOCOL - running a name under the v5 drafts.md`). Fill top to
bottom; every judgment cites a v5 ledger id in bold; every filing fact carries its accession; a STOP that returns OUT or
TOO HARD closes the run and later questions are marked NOT REACHED. Copied from `Test Runs/_TEMPLATE - Company Run.md`
to this dated name before any fetch. Research folder: `Test Runs/_research 2026-10-06 NKE/` (tool output and notes;
raw filings under its `cache/` subfolder, gitignored, re-fetchable from EDGAR by the accessions below).

**POSITION NOTE, declared before any verdict:** not checked; dispatched under a blind rule. `PORTFOLIO.md` was not
opened, and the analyst does not know whether the operator holds NKE.

**CONTAMINATION, declared:** no earlier NKE run, research folder, RE-LOOK file, register entry, reading-list entry,
session-state file or `tools/alerts.json` was opened. Seen without opening: the `Test Runs/` directory listing (names
of the 2026-10-05 run files, none of them NKE); a filename grep for the word "Nike" across the 2026-10-05 run files
returned eight other companies' runs (AMR, ATKR, LCII, MWA, OSIS, SHOE, WSC, YELP), none of which was opened. One
2026-10-05 run (WEN) was read for form only, its first sixty lines. The analyst's training memory holds a prior on
Nike (a dominant brand, a large buyback history, a share price far above today's); it is treated as a prior to be
replaced by the filings, and where the filings differ the filings are used. `tools/run.py` printed arithmetic only
(Part VII); nothing it printed as a rule, an id or a verdict was used.

---
## STEP 0 — THE RATE, THE PRICE, THE SHARES, THE FILING
- **Price:** $33.96 (close 2026-10-05, the quote `tools/run.py` fetched; **aggregator, live quote only**, flagged per
  operator rule 5).
- **Shares by class** from the latest filing's cover (10-Q for the quarter to 2026-08-31, filed 2026-10-02, accession
  `0000320187-26-000193`; `python Screens/cover_shares.py NKE`): Class A 281,387,752; Class B 1,203,921,077. **The
  charter note, read before adding:** "Each share of Class A Common Stock is convertible into one share of Class B
  Common Stock. [...] There are no differences in the dividend and liquidation preferences or participation rights of
  the holders of Class A and Class B Common Stock" (10-K FY2026, Note on capital stock, `0000320187-26-000088`). The
  classes differ in voting only (Class A elects three-quarters of the board, Item 1A of the same 10-K), so they are
  economically one class and are added: **1,485,308,829 shares.**
- **Market cap:** about **$50,441M** (1,485.31M x $33.96).
- **Sovereign for the earnings currency (USD):** **5.66%**, US Treasury daily par yield curve, 30-year, 2026-10-05
  (`python tools/sources.py`; the issuing authority). Earnings currency: USD (the filer reports in USD; 56% of revenue
  is outside the US and is translated).
- **Filings read** (operator rule 4): 10-K for FY2026 (year to 2026-05-31, filed 2026-07-15, `0000320187-26-000088`);
  10-K for FY2024 (filed 2024-07-25, `0000320187-24-000044`, for the FY2022 and FY2023 cash-flow lines); 10-Q for Q1
  FY2027 (quarter to 2026-08-31, filed 2026-10-02, `0000320187-26-000193`); proxy DEF 14A filed 2026-07-15
  (`0000320187-26-000089`); 8-K of 2026-10-01 with the Q1 FY2027 earnings release, Exhibit 99.1, and the Item 2.05
  "Pace" program (`0000320187-26-000184`); 8-K of 2026-06-30 with the Q4 FY2026 release, Exhibit 99.1
  (`0000320187-26-000076`); 8-K of 2026-03-05 (Item 2.05, the March 2026 severance plan, `0000320187-26-000017`); 8-K
  of 2026-06-23 (CFO transition, `0000320187-26-000070`); 8-K of 2026-09-16 (a director appointed,
  `0000320187-26-000170`). Competitors' filings are listed at Q2.
- **One figure cross-checked against the filed statement:** cash provided by operations FY2026, **$2,868M** on the
  filed Consolidated Statement of Cash Flows (10-K `0000320187-26-000088`), against 2,868 in `tools/run.py`'s XBRL
  transcription. They agree. The FY2022 and FY2023 lines (OCF 5,188 and 5,841; stock pay 638 and 755; capex 758 and
  969) were read from the filed statement in the FY2024 10-K (`0000320187-24-000044`).
- **`tools/run.py NKE` arithmetic lines** (saved: `_research 2026-10-06 NKE/run_py_output.txt`), checked against the
  filed cash-flow statements:

| FY (to 31 May) | OCF | stock pay | capex | **owner cash (capex basis)** | D&A | owner cash (D&A basis) |
|---|---|---|---|---|---|---|
| 2022 | 5,188 | 638 | 758 | **3,792** | 717 (depreciation; amortization in "other") | 3,833 |
| 2023 | 5,841 | 755 | 969 | **4,117** | 703 | 4,383 |
| 2024 | 7,429 | 804 | 812 | **5,813** | 796 | 5,829 |
| 2025 | 3,698 | 709 | 430 | **2,559** | 775 | 2,214 |
| 2026 | 2,868 | 715 | 684 | **1,469** | 747 | 1,406 |
| Q1 FY2027 (3 months) | 135 | 158 | 199 | (222) | 193 | (216) |

  USD millions. Owner cash = cash provided by operations (already after interest, cash taxes and operating-lease cash)
  less stock pay and less additions to property, plant and equipment. **Five-year average owner cash (FY2022 to
  FY2026): $3,550M**; D&A-basis variant $3,533M. Where maintenance sits: capex ran from 430 to 969 against
  depreciation of 703 to 796; the filings do not split maintenance from growth capex, so the capex basis is used and
  the D&A basis is shown. The working-capital swings inside OCF are large and are not smoothed away: inventory took
  1,676 in FY2022 and gave back 908 in FY2024; receivables took 1,207 in FY2026, of which $684M was the IEEPA tariff
  refund receivable, collected "substantially all" after year end (10-K FY2026, MD&A, Other Matters) and yet Q1 FY2027
  OCF was only $135M. No acquisitions in the window. The trend is the finding: 5,813, 2,559, 1,469, and a negative
  first quarter.

## THE FOUNDATIONS (not a gate)
A share is a business: the question is whether the analyst would be content to own Nike if the market closed for five
years **[M1997-109]**, and the price, which the training-memory prior holds to have been several times higher, says
nothing about value; "it just tells us prices" **[M2006-077]**. No projection is used: the company's FY2027 outlook
(revenue down high-single digits; an "Adjusted Diluted earnings per share" of $1.15 to $1.35) is recorded as the
company's own statement and is not an input, "we've never looked at a projection" **[M1995-050]**, **[M2003-065]**.
The analyst's habits govern the reading: look for "what's wrong" and "what you're missing" **[M2025-013]**, state the
bull's case better than its holder before disagreeing **[M2016-055]**, and destroy the prior conclusion **[M2016-054]**.
The bull's case, stated: the largest seller of athletic footwear and apparel in the world, $46.4B of revenue (10-K
FY2026), a demand-creation budget of $4.8B a year, a chief executive who returned after retiring from the company in 2020 (DEF 14A `0000320187-26-000089`), a new finance chief (8-K `0000320187-26-000070`), a cost program, a North
America business growing again, and a price that has fallen far. **Contrary evidence, written down as found**
**[M1997-127]**: (1) owner cash fell from $5,813M (FY2024) to $1,469M (FY2026), and Q1 FY2027 was negative; (2) the
company's own 10-K names "the rapid changes in technology and consumer preferences" as "significant risk factors" and
says of design trends and consumer preferences "This is a continuing risk" (10-K FY2026, Items 1 and 1A); (3) Converse,
the brand of the Chuck Taylor and All Star trademarks (10-K FY2026, Item 1), fell 31% in one year (Q4 FY2026 release); (4) NIKE Brand
Digital fell 12% in FY2026 and 13% in Q1 FY2027 while two newer running brands grew fast (competitor row, Q2); (5) the
company is "liquidating inventory through increased markdowns" and taking "higher sales returns and discounts with our
wholesale partners" (10-K FY2026, MD&A); (6) FY2026 net income of $3,108M carries a $986M pre-tax tariff-refund
benefit in cost of sales (same MD&A); (7) the company introduced an "Adjusted Diluted earnings per share" excluding
restructuring in the 2026-10-01 release, after $385M of severance in FY2026 and with $1.0B more charges planned through
FY2031 (8-K `0000320187-26-000184`).

## THE STANDING RULE
Owning this, bought with the buyer's own money, unlevered and sized as Q10 would size it, puts the buyer at no risk of
ruin; the rule binds the buyer's conduct, "never going to risk what we have and need for what we don't have and don't
need" **[M2012-081]**, and borrowed money has no place in the purchase **[L2014-005]**, **[M2004-065]**. Nothing in the
target forces the buyer to sell into a falling quote **[M2020-007]**. No breach.

---
## Q1 — CAN I UNDERSTAND IT? Where its economics will be in ten years, inside my perimeter. STOP.
- **The test as the draft states it:** "a reasonable fix on about what the earning power and competitive position will
  look like in five or 10 years" **[M2012-065]**, **[M2000-037]**; understanding "the economic dynamics of the
  industry", not the chemistry of the product **[M2011-014]**.
- **The economics, from the filings.** Nike designs and markets; it makes almost nothing: "Nearly all of our products
  are manufactured by independent contractors" (95 footwear factories in 11 countries; 52% of NIKE Brand footwear made
  in Vietnam), and it sells through wholesale accounts ($27.5B in FY2026) and its own stores and digital platforms
  ($17.7B) (10-K FY2026, Items 1 and 7, `0000320187-26-000088`). What it earns comes from the premium a branded product
  commands over its contract cost, net of the demand creation ($4,754M in FY2026) that keeps the brand in the
  customer's mind. The key variables are the brand's place in the consumer's mind, the share of product sold at full
  price, and the cost of goods including tariffs **[M1998-044]**.
- **Customers or technology?** The forecast is about consumer behaviour, not about technology **[M2017-019]**; the rows
  hold that consumer behaviour can be projected where "we want to see how a consumer product behaves under a lot of
  different circumstances" **[M2018-074]**, **[M2023-030]**. A running shoe ten years out is still a running shoe; this
  is not the fast-moving-technology case that the routing sends to TOO HARD at this question **[M1999-063]**.
- **Contrary evidence on Q1, written down** **[M1997-127]**: the past statements did not tell the next ones
  **[M2008-033]**: owner cash ran 3,792 / 4,117 / 5,813 and then 2,559 / 1,469; and the company itself names "the
  rapid changes in technology and consumer preferences in the markets for athletic and leisure footwear and apparel"
  as "significant risk factors" (10-K FY2026, Item 1, Competition). "How far off could I be?" **[M2011-084]** is
  answered by the record: very far, in three years. The retail half of the business (NIKE Direct, 38% of FY2026
  revenue) carries the speakers' own warning, "it's easy to sort of think you understand retail, and then
  subsequently find out you don't" **[M2014-052]**, **[M1997-024]**.
- **Where that evidence belongs.** It does not show that the industry's economics cannot be foreseen; it shows that
  this company's place in the customer's mind, and so its earning power, moved against it. The draft's own division
  is that Q1 asks whether the economics and position can be foreseen at all and Q2 asks what the foresight shows about
  the castle (section IV, Q1, The order). The structure of the industry (designer-marketers buying from shared contract
  factories and competing for the consumer's preference) is foreseeable ten years out; whether Nike holds its share
  of that preference is the castle question, and it is taken to Q2 rather than settled here. The doubt rule
  **[M2002-092]** is applied to the industry and found not to bite: the analyst has no doubt about how the industry
  makes money, only about whether this castle is holding.
- **VERDICT: IN**, narrowly, **[M2012-065]**, **[M2011-014]**, **[M2017-019]**. The contrary evidence above is carried
  to Q2 and tested there as castle evidence.

## Q2 — WHY IS THE CASTLE STILL STANDING, and what keeps it standing ten to twenty years? STOP.
The question: "why is that castle still standing? And what's going to keep it standing or cause it not to be standing
five, 10, 20 years from now" **[M1995-038]**. Every castle earning high returns is assumed under assault **[L2007-004]**.

**The competitor row** (same metrics, each from the competitor's own filing; `_research 2026-10-06 NKE/NOTES - filing
extracts and arithmetic.md`):

| company / brand | revenue, earlier | revenue, latest | change | gross margin, latest | filing |
|---|---|---|---|---|---|
| Nike, Inc. (FY to May) | FY2023 $51,217M | FY2026 $46,398M | -9.4% | 42.9% (40.8% without the $986M tariff refund) | 10-K `0000320187-26-000088` |
| Deckers, HOKA brand (FY to March) | FY2023 $1,412.9M | FY2026 $2,587.3M | +83% | Deckers whole 57.7% (50.3% in FY2023) | 10-K FY2026 `0001628280-26-037664`; 10-K FY2025 `0000910521-25-000017` |
| On Holding (calendar, CHF) | 2023 CHF 1,792.1M | 2025 CHF 3,014.0M | +68% in two years | 62.8% (60.6% in 2024) | 20-F FY2025 `0001858985-26-000008` |
| Under Armour (FY to March) | FY2024 $5,701.9M | FY2026 $4,966.4M | -12.9% | 45.5% (down 240bp) | 10-K FY2026 `0001336917-26-000073` |

adidas files no SEC report and its own annual report was not read; the row stands without it. The row's pattern: the
two older incumbents shrinking, the two newer brands growing fast at gross margins fifteen to twenty points above
Nike's.

**The castle tests, each with its filing fact.**
1. **What keeps it standing, and how permanent?** **[M1995-038]**. The 10-K names the key factors: "Product attributes
   such as quality; innovation and development; performance and reliability; new product style and design" and
   "Consumer connection, engagement and affinity for brands", with the rider that "We must, therefore, respond to
   trends and shifts in consumer preferences by adjusting the mix of existing product offerings and channels,
   developing new products, styles and categories [...] This is a continuing risk" (10-K FY2026, Item 1). The factors
   are real but must be renewed every season; leadership "provides no certainties" **[L1996-031]**.
2. **Would it stand without the lord?** The FY2025 and FY2026 decline is described by the company as the cost of
   undoing its own channel strategy: "Repositioning NIKE Brand Digital as a full-price platform and reinvesting in
   wholesale distribution", with markdowns, returns and discounts to clear inventory (10-K FY2026, MD&A, Factors
   Impacting Our Business). A business whose results swing this far on a management's channel choice is nearer "the
   poor business [...] that can only succeed, or even survive, with great management" than the one "that doesn't
   require good management" **[M1996-037]**; for the 38% that is its own retail, "a retailer must stay smart, day
   after" day **[L1995-008]**.
3. **The money test.** **[M2011-015]**: could a well-funded attacker take it? The filings answer that attackers far
   less funded already have, in Nike's own core category: HOKA grew from $1,412.9M to $2,587.3M and On from CHF
   1,792.1M to CHF 3,014.0M while Nike shrank, against Nike's $4,754M a year of demand creation. "If the answer had
   been yes, we wouldn't have done it." **[M2011-015]**; "one competitor is frequently enough to ruin a business"
   **[M2012-108]**.
4. **Pricing power and the agony before a rise.** **[M2005-020]**. Nike is "liquidating inventory through increased
   markdowns across NIKE Direct, and higher sales returns and discounts with our wholesale partners" (10-K FY2026,
   MD&A). Gross margin ran 46.0% (FY2022), 43.5%, 44.6%, 42.7%, and 40.8% in FY2026 without the one-time tariff refund
   (filed income statements; notes file). A strong position "manage[s] to pass through increases" in costs
   **[M2005-017]**; this one has not, and the pattern is the one the speakers name: "pushed their pricing too far to
   the point that they lost market share without [...] the moat that they thought they had" **[M2001-087]**.
5. **Unit volume and share of mind.** **[M1997-099]**, **[M2000-030]**. NIKE Direct revenue fell "primarily driven by
   a decrease in traffic"; NIKE Brand Digital fell 12% in FY2026 and 13% in Q1 FY2027; Converse fell 31% in FY2026
   and 28% in Q1 FY2027; Greater China revenue fell from $7,545M (FY2024) to $5,847M (FY2026) amid "declining store
   traffic, elevated promotional activity and higher levels of inventory" (10-K FY2026; releases of 2026-06-30 and
   2026-10-01). On the other side: wholesale revenue rose 6% in FY2026, North America revenue rose 5% to $20,511M, and
   inventories were flat "reflecting an increase in units" (10-K FY2026). Share of mind is falling in China, in the
   company's own digital channel and at Converse, and holding in North American wholesale.
6. **The low-cost position.** None: Nike buys from the same contract factory base as its rivals ("Nearly all [...]
   manufactured by independent contractors", 10-K Item 1), and Deckers' own 10-K says what that does to entry:
   "Barriers to entry have been reduced by access to offshore manufacturing and evolving technologies, allowing
   competitors to develop and scale products more quickly and at lower cost" (10-K `0001628280-26-037664`, Item 1A).
7. **The brand in the customer's mind.** "the brand has to stand for something in the consumer's mind" **[M2015-038]**,
   and "you're probably going to get better gross of margins if they ask for you by name" **[M2023-073]**. Nike is
   still the largest seller in the world (10-K Item 1), but the margin test runs the wrong way: the two growing brands
   earn 57.7% and 62.8% gross against Nike's 40.8% to 42.9%. Against the retailer, Nike has just handed volume back to
   wholesale partners after trying to take it from them, the Kraft Heinz pattern of the brand underrating "what the
   retailer is" **[M2019-041]**.
8. **Would the customer still choose it over the low bid?** **[M2017-009]**. Athletic footwear is not bought on the
   low bid, which favours the category; but the choice that matters here is among premium brands, and the row shows it
   moving away from Nike at full price toward HOKA and On.
9. **Ask the competitors.** **[M2017-022]**. On states its "vision to be the most premium global sportswear brand"
   (20-F FY2025, Item 4), and Deckers names Nike's game as one whose barriers "have been reduced" (Item 1A above). Nike
   names eleven competitors by name, from adidas to Anta and Li Ning (10-K Item 1). The attackers aim at the premium
   performance categories Nike's moat was supposed to protect.
10. **Widening or narrowing?** **[M1999-108]**, **[M2000-075]**. Narrowing over FY2024 to Q1 FY2027 on every measure
    the filings give: revenue, gross margin, segment EBIT (China $2,309M to $1,278M; EMEA $3,388M to $2,417M;
    Converse $474M to $18M; 10-K FY2026 segment table), owner cash, and share against the competitor row. The test for
    a bad year that is only cyclical is whether "we at least maintained, and in some instances widened, our
    competitive superiority" **[L1995-022]**; the row says it was not maintained. "lost a notch" **[L1995-023]**.
11. **What could destroy, modify or reduce it?** **[M2000-014]**. Taste moving to newer brands in performance running
    (the row), local brands in China (Anta and Li Ning named, 10-K Item 1), and tariffs on a product made almost wholly
    in Vietnam, Indonesia and China (10-K Item 1; the IEEPA tariffs and their refund, MD&A).

**Contrary evidence, written down** **[M1997-127]**: the castle is still the biggest in the field; North America and
wholesale grew in FY2026; the company reports a return on invested capital of 18.7% on its own (non-GAAP) definition
(10-K MD&A); management says the reset actions complete by December 2026; and a brand that has been the largest for
decades may recover its heat, as the speakers record that change can run toward a business as well as against it
**[M2017-026]**. These are reasons the castle still stands, not evidence that its walls are being rebuilt faster than
they are being breached.

**The reading.** The moat here is one that must be renewed every season, by the company's own description (test 1),
and the evidence shows the renewal failing over three fiscal years and into a fourth quarter: attackers with a
fraction of Nike's budget took share in its core category at higher margins (tests 3, 6, 7, 9), pricing power gave way
to markdowns (test 4), and revenue fell in four of five reporting segments on a currency-neutral basis in FY2026, North America the exception (test 5; 10-K segment table). That is the case the draft
lists under what Q2 rules OUT: "The moat that must be continuously rebuilt, where the evidence shows the rebuilding
failing" **[L2007-005]**, and "A moat that must be continuously rebuilt will eventually be no moat at all."
**[L2007-005]**; with it, the attacker test answered yes **[M2011-015]** and the industry where "you better be running
very fast" **[M2012-106]**. The alternative reading, that the castle's future simply cannot be judged and the box is
TOO HARD **[M2000-019]**, was weighed and set aside: the deciding evidence is not a forecast but what has already been
filed, a moat shown narrowing against named attackers, which the routing sends to OUT **[M2011-015]**,
**[M2006-013]**. A lower price does not reopen it: "What you can't do is turn any investment into a good deal by
paying little" **[M2019-015]**; "it pays to stay away from declining businesses" **[M2012-062]**.

**Reversal condition (one line):** filings showing the rebuilding succeeding, NIKE Brand revenue growing again with
gross margin back inside its FY2022 to FY2024 band (43.5% to 46.0%, without one-time items) for two fiscal years while
the competitor row's newer brands stop taking share, would reopen Q2; price alone would not.

- **VERDICT: OUT**, **[L2007-005]**, **[M2011-015]**, **[M2012-108]**, **[L1995-022]**. The run closes here; Q3 to Q12
  are NOT REACHED.

## Q3 — HOW MUCH CAPITAL MUST GO IN. NOT REACHED (closed at Q2).
## Q4 — DO THE NUMBERS SHOW WHAT IT EARNS. NOT REACHED. *(Recorded as found, not judged: the 2026-10-01 release
introduced an "Adjusted Diluted earnings per share" excluding restructuring and severance; EBIT, not EBITDA, is the
filer's other non-GAAP measure; 8-K `0000320187-26-000184`.)*
## Q5 — WHO RUNS IT. NOT REACHED.
## Q6 — WHAT WILL THEY DO WITH THE MONEY AND THE OWNERS. NOT REACHED.
## Q7 — WHAT IS IT WORTH. NOT REACHED. No value range was computed; the owner-cash table in Step 0 is arithmetic, not a
clearance.
## Q8 — BETTER THAN THE ALTERNATIVES. NOT REACHED.
## Q9 — COULD IT RUIN US. NOT REACHED.
## Q10 — THE FAT PITCH. NOT REACHED.
## Q12 (optional) — PROUD OF HOW THE MONEY IS MADE. NOT REACHED.

---
## THE BOX
**OUT at Q2.** The castle is one that must be rebuilt every season by the company's own description, and the filings
of FY2024 to Q1 FY2027 show the rebuilding failing against named attackers (HOKA +83% and On +68% while Nike fell
9.4%; gross margin from 46.0% to 40.8% without the one-time refund; owner cash from $5,813M to $1,469M and a negative
first quarter) **[L2007-005]**, **[M2011-015]**. Q7 was not reached; no value range. Price $33.96 against a market cap
of about $50,441M; the price does not reopen Q2 **[M2019-015]**. Reversal: two fiscal years of NIKE Brand growth with
gross margin back in the 43.5% to 46.0% band while the newer brands stop taking share.

## SELF-AUDIT
- [x] Copied to the dated file before any fetch; written question by question; committed after each (write-early):
      Step 0 to the standing rule, Q1, Q2, and this close, four commits.
- [x] Every v5 id resolves (checked by script against `principle_ledger_v5.csv` before each commit); every filing fact
      has its accession; no number without a row or a filing. The competitor row's gross margins are whole-company for
      Deckers and On, stated as such.
- [x] The order was kept; the first STOP that failed (Q2) closed the run; nothing after it is a clearance.
- [x] Owner cash after every real cost (OCF less stock pay less capex), never a net-income proxy (operator rule 5);
      the sovereign from the US Treasury; the price flagged as an aggregator quote.
- [x] Contrary evidence was written down as it was found **[M1997-127]** (foundations, Q1 and Q2).
- [x] No row dated after the anchor is cited in a point-in-time run (Part VII): not a point-in-time run; no anchor.
- [x] Only the arithmetic lines of `tools/run.py` were used (Part VII); its yield, implied-growth and spread lines were
      not used.
- [x] `python tools/check_framework.py` PASS before each commit.

## WHAT IN THE FRAMEWORK WAS WRONG OR UNCLEAR
Two boundaries were unclear and decided the run. First, the Q1/Q2 routing sends "a business whose ten-year economics
cannot be foreseen because its industry changes fast" to Q1 TOO HARD, and its rows speak of technology
(**[M1998-008]**, **[L1993-023]**); it does not say where a consumer-preference business goes when its own 10-K calls
"rapid changes in [...] consumer preferences" a significant risk. This run read the routing as technology-led change,
passed Q1 on the industry's economics, and took the company's lost share of mind to Q2; a second analyst could close
the same filings at Q1 TOO HARD (NATURE) on the doubt rule **[M2002-092]**. Second, at Q2 the draft sends "a castle shown
on the evidence to be filling in" to OUT and "a moat that's tenuous in any way" to TOO HARD **[M2000-019]**; every
filling-in castle is also tenuous, so the two overlap, and the draft gives no test for when narrowing evidence is enough
to be "shown". The run used the draft's own listed OUT item, the continuously rebuilt moat "where the evidence shows the
rebuilding failing" **[L2007-005]**, plus the attacker test already answered in the competitors' filings, and recorded
the TOO HARD reading as weighed and set aside. Neither choice is a CONVENTION the draft confesses; both would benefit
from one. **Tool notes (not fixed, reported):** `tools/run.py` could not find a current cover-page share count for this
two-class filer (it printed a 2015 dei count as STALE and used a weighted diluted average of 1,481.0M for its market
cap of $50.29B); `Screens/cover_shares.py` gave the correct two-class cover and the run used it. For FY2022 and
FY2023 the filed cash-flow statement shows "Depreciation" alone, with amortization inside "Amortization, impairment and
other", so the D&A-basis variant for those two years is depreciation only, in this run and in `tools/run.py`'s
five-year window alike; immaterial here, since Q7 was not reached.
